# 实战：基于 LangChain 的流式对话应用

![gradio-app](./images/gradio_app.png)

## 💻 技术栈

- **前端**：`Gradio`
- **后端**：
    - `LangChain`
    - `LangGraph`
- **MCP**：`fastmcp`

## 🔧 工具

- **tools**：
    - **联网搜索**：[tool_search.py](./tools/tool_search.py)
    - **数学计算**：[tool_math.py](./tools/tool_math.py)
- **MCP**：
    - **角色扮演**：[role_play.py](./mcp/role_play.py)

## 🚀 启动方式

### 1）安装依赖

```bash
# 基础版
pip install -r requirements.txt

## 增强版
# pip install -r requirements.txt -U -i https://mirrors.aliyun.com/pypi/simple/
```

### 2）配置环境变量

```bash
cp .env.example .env
```

### 3）启动 Agent 和 MCP Server

```bash
python app.py
```

## 🔭 架构

```text
.
├── README.md
├── app.py                  # 主应用入口
├── requirements.txt        # 项目依赖
├── .env.example            # 环境变量示例
├── images                  # 图片资源
│   ├── ai.png
│   ├── gradio_app.png
│   └── user.png
├── logs                    # 日志目录
├── mcp                     # MCP Server
│   └── role_play.py
├── prompts                 # 系统提示词模块
│   ├── __init__.py
│   ├── prompt.py
│   ├── prompt_base.py
│   └── prompt_enhance.py
├── tools                   # 工具模块
│   ├── __init__.py
│   ├── tool_math.py
│   └── tool_search.py
└── utils                   # 实用脚本模块
    ├── __init__.py
    ├── device_info.py
    └── web_ui.py
```
