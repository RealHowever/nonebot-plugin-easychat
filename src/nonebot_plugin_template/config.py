from nonebot import get_driver, get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    ai_api_key: str = ""
    ai_base_url: str = "https://api.openai.com/v1/chat/completions"
    ai_model: str = "gpt-3.5-turbo"
    ai_prompt: str = "你是一个友好的助手，帮助用户解答问题。"


plugin_config: Config = get_plugin_config(Config)
global_config = get_driver().config

NICKNAME: str = next(iter(global_config.nickname), "")
