"""
一个智能体
"""

import os
import asyncio

from typing import List, Dict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from utils.web_ui import create_ui, theme, custom_css
from tools.tool_math import add, subtract, multiply, divide
from tools.tool_search import dashscope_search, SearchTool
from prompts.prompt_enhance import get_system_prompt


# 加载模型配置
# 请事先在 .env 中配置 DASHSCOPE_API_KEY
_ = load_dotenv()


# 全局变量
_agent = None  # 全局 Agent 实例
_greeting = ""  # 智能体自我介绍


async def get_agent():
    """获取全局 Agent 实例"""
    global _agent
    if _agent is None:
        llm = ChatOpenAI(
            model="qwen3-coder-plus",
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url=os.getenv("DASHSCOPE_BASE_URL"),
        )

        client = MultiServerMCPClient(  
            {
                "role_play": {
                    "command": "python",
                    "args": [os.path.abspath("./mcp/role_play.py")],
                    "transport": "stdio",
                },
                # "role_play": {
                #     "url": "http://localhost:8000/mcp",
                #     "transport": "streamable_http",
                # },
            }
        )
        mcp_tools = await client.get_tools()

        # 创建智能体
        _agent = create_agent(
            model=llm,
            tools=mcp_tools + [add, subtract, multiply, divide, dashscope_search],
            system_prompt=get_system_prompt(),
        )
    return _agent


def get_tools():
    """获取 Agent 的工具列表"""
    agent = asyncio.run(get_agent())
    node = agent.get_graph().nodes["tools"]
    tools = list(node.data.tools_by_name.values())

    return "\n".join([
        f"- `{tool.name}`: {tool.description.split('\n')[0]}" for tool in tools
    ])


def get_greeting():
    """获取 Agent 的自我介绍"""
    global _greeting
    if not _greeting:
        try:
            tools_info = get_tools()
            _greeting = "\n".join([
                "你好！我是你的智能助手，可以使用的工具包括：",
                tools_info,
                "\n请问有什么可以帮你的吗？",
            ])
        except Exception as e:
            print(f"获取工具列表时出错: {e}")
            _greeting = "你好！我是你的智能助手。\n请问有什么可以帮你的吗？"
    return _greeting


async def generate_response(message: str,
                      history: List[Dict[str, str]]
):
    """生成 Agent 的响应"""
    if not message:
        yield "", history
        return

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": ""})

    messages = history[:-1]

    agent = await get_agent()
    async for token, metadata in agent.astream(
        {"messages": messages},
        stream_mode="messages",
        context=SearchTool(api_key=os.getenv("DASHSCOPE_API_KEY")),
    ):
        if metadata["langgraph_node"] == "model":
            content = token.content_blocks
            if content and content[0].get("text", "") != "":
                history[-1]["content"] += content[0]["text"]
                yield "", history

    yield "", history


def main():
    """主函数"""
    app = create_ui(
        llm_func=generate_response,
        tab_name="Gradio APP - WebUI",
        main_title="Gradio WebUI Demo",
        sub_title="GitHub@luochang212",
        initial_message=[{"role": "assistant", "content": get_greeting()}]
    )

    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        theme=theme,
        css=custom_css
    )


if __name__ == "__main__":
    main()
