from nonebot import logger, require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters
from nonebot.adapters import Event, Message
from nonebot import on_message
from nonebot.rule import to_me

require("nonebot_plugin_uninfo")

from .config import Config, plugin_config

__plugin_meta__ = PluginMetadata(
    name="AI回复",
    description="基于AI模型的自动回复插件",
    usage="@bot 发送消息进行AI对话",
    type="application",
    homepage="https://github.com/owner/nonebot-plugin-template",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_uninfo"),
    extra={"author": "owner <your@mail.com>"},
)

ai_reply = on_message(rule=to_me(), priority=10, block=False)


@ai_reply.handle()
async def _(event: Event, message: Message):
    msg_text = message.extract_plain_text().strip()
    if not msg_text:
        return

    api_key = plugin_config.ai_api_key
    base_url = plugin_config.ai_base_url
    model = plugin_config.ai_model
    system_prompt = plugin_config.ai_prompt

    if not api_key:
        logger.warning("AI API Key未配置")
        return

    try:
        import httpx
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": msg_text}
            ]
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(base_url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            reply_text = result["choices"][0]["message"]["content"].strip()
            await ai_reply.finish(reply_text)
    except Exception as e:
        logger.error(f"AI请求失败: {e}")
