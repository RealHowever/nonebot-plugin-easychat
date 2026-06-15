<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="310" alt="logo"></a>

## ✨ {plugin-name} ✨
[![LICENSE](https://img.shields.io/github/license/{owner}/{plugin-name}.svg)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/{plugin-name}.svg)](https://pypi.python.org/pypi/{plugin-name})
[![python](https://img.shields.io/badge/python-3.10|3.11|3.12|3.13-blue.svg)](https://www.python.org)
[![uv](https://img.shields.io/badge/package%20manager-uv-black?style=flat-square&logo=uv)](https://github.com/astral-sh/uv)
<br/>
[![ruff](https://img.shields.io/badge/code%20style-ruff-black?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff)
[![pre-commit](https://results.pre-commit.ci/badge/github/{owner}/{plugin-name}/master.svg)](https://results.pre-commit.ci/latest/github/{owner}/{plugin-name})

</div>

## 📖 介绍

基于AI模型的自动回复插件，支持通过@bot发送消息进行AI对话，支持自定义API地址、模型和系统提示词。

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install {plugin-name} --upgrade
使用 **pypi** 源安装

    nb plugin install {plugin-name} --upgrade -i "https://pypi.org/simple"
使用**清华源**安装

    nb plugin install {plugin-name} --upgrade -i "https://pypi.tuna.tsinghua.edu.cn/simple"


</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details open>
<summary>uv</summary>

    uv add {plugin-name}
安装仓库 master 分支

    uv add git+https://github.com/{owner}/{plugin-name}@master
</details>

<details>
<summary>pdm</summary>

    pdm add {plugin-name}
安装仓库 master 分支

    pdm add git+https://github.com/{owner}/{plugin-name}@master
</details>
<details>
<summary>poetry</summary>

    poetry add {plugin-name}
安装仓库 master 分支

    poetry add git+https://github.com/{owner}/{plugin-name}@master
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_template"]

</details>

<details>
<summary>使用 nbr 安装(使用 uv 管理依赖可用)</summary>

[nbr](https://github.com/fllesser/nbr) 是一个基于 uv 的 nb-cli，可以方便地管理 nonebot2

    nbr plugin install {plugin-name}
使用 **pypi** 源安装

    nbr plugin install {plugin-name} -i "https://pypi.org/simple"
使用**清华源**安装

    nbr plugin install {plugin-name} -i "https://pypi.tuna.tsinghua.edu.cn/simple"

</details>


## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的配置

| 配置项  | 必填  | 默认值 |   说明   |
| :-----: | :---: | :----: | :------: |
| AI_API_KEY |  是   |   无   | AI服务的API密钥 |
| AI_BASE_URL |  否   | https://api.openai.com/v1/chat/completions | AI接口地址 |
| AI_MODEL |  否   | gpt-3.5-turbo | 使用的AI模型名称 |
| AI_PROMPT |  否   | 你是一个友好的助手，帮助用户解答问题。 | 系统提示词，定义AI角色 |

## 🎉 使用
### 指令表
| 指令  | 权限  | 需要@ | 范围  |   说明   |
| :---: | :---: | :---: | :---: | :------: |
| @bot + 消息 | 群员  |  是   | 群聊/私聊  | 发送消息进行AI对话 |

### 🎨 使用示例
```
@bot 你好，今天天气怎么样？
@bot 帮我写一段Python代码
@bot 解释一下量子计算
```