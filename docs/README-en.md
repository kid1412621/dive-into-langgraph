<div style="text-align: center;">
    <img src="../img/cute.png" width="100%">
    <h1>Dive into LangGraph</h1>
</div>

<div style="text-align: center;">
  <img src="https://img.shields.io/github/stars/luochang212/dive-into-langgraph?style=flat&logo=github" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/luochang212/dive-into-langgraph?style=flat&logo=github" alt="GitHub forks"/>
  <img src="https://img.shields.io/badge/language-English-brightgreen?style=flat" alt="Language"/>
  <a href="https://github.com/luochang212/dive-into-langgraph"><img src="https://img.shields.io/badge/GitHub-Project-blue?style=flat&logo=github" alt="GitHub Project"></a>
  <a href="https://github.com/luochang212/langgraph-tutorial/actions/workflows/deploy-book.yml"><img src="https://github.com/luochang212/langgraph-tutorial/actions/workflows/deploy-book.yml/badge.svg?branch=main" alt="deploy-book"/></a>
</div>

<div style="text-align: center;">

[中文](../README.md) | English

</div>

<div style="text-align: center;">
  <p><a href="https://luochang212.github.io/dive-into-langgraph/">📚 Online Reading</a></p>
  <h3>📖 LangGraph 1.0 Complete Guide</h3>
  <p><em>Build powerful agents from scratch</em></p>
</div>

---

## 1. Introduction

> In mid-October 2025, LangGraph released version 1.0. The team announced this as a stable release and expects the interfaces not to change significantly, so now is a great time to learn it.

[LangGraph](https://github.com/langchain-ai/langgraph) is an open-source agent framework developed by the LangChain team. It’s powerful — memory, MCP, guardrails, state management, and multi-agent capabilities are all built in. LangGraph is typically used together with [LangChain](https://github.com/langchain-ai/langchain): LangChain provides the building blocks and tools, while LangGraph focuses on workflow orchestration and state management. To help you ramp up quickly, I’ve extracted the most important features from both libraries and organized them into 11 chapters.

## 2. Installation

```bash
pip install -r requirements.txt
```

<details>
  <summary>Dependency list</summary>

  The following packages are listed in `requirements.txt`:

  ```text
  pydantic
  python-dotenv
  langchain[openai]
  langchain-community
  langchain-mcp-adapters
  langchain-text-splitters
  langgraph
  langgraph-cli[inmem]
  langgraph-supervisor
  langgraph-checkpoint-sqlite
  langmem
  ipynbname
  fastmcp
  bs4
  ```
</details>

## 3. Contents

Quick overview of the tutorial:

| # | Chapter |
| -- | -- |
| 1 | [Quickstart](../1.quickstart.ipynb) |
| 2 | [State Graph](../2.stategraph.ipynb) |
| 3 | [Middleware](../3.middleware.ipynb) |
| 4 | [Human-in-the-Loop](../4.human_in_the_loop.ipynb) |
| 5 | [Memory](../5.memory.ipynb) |
| 6 | [Context Engineering](../6.context.ipynb) |
| 7 | [MCP Server](../7.mcp_server.ipynb) |
| 8 | [Supervisor Pattern](../8.supervisor.ipynb) |
| 9 | [Parallelism](../9.parallel.ipynb) |
| 10 | [Deep Agents](../10.deep_agents.ipynb) |
| 11 | [Debug UI](../11.langgraph_cli.ipynb) |

Important examples not covered above are placed under the repository’s `tests` directory:

| Code | Description |
| -- | -- |
| [/tests/test_rag.py](../tests/test_rag.py) | Use `RAG` to inject local document snippets into the agent |
| [/tests/test_langmem.py](../tests/test_langmem.py) | Use `LangMem` to manage an agent’s long-term memory |
| [/tests/test_store.py](../tests/test_store.py) | Use `RedisStore` for fast read/write of long-term memory |
| [/tests/test_router.py](../tests/test_router.py) | Implement a simple agent router |

> [!NOTE]
>
> Commitment: This tutorial is written entirely against LangGraph v1.0, with no residual content from v0.6.

## 4. Debug UI

`langgraph-cli` provides a debugging UI that can be launched quickly.

```bash
langgraph dev
```

See [Chapter 11](../11.langgraph_cli.ipynb) for details.

## 5. References

- [LangChain](https://docs.langchain.com/oss/python/langchain/overview)
- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)
- [LangMem](https://langchain-ai.github.io/langmem/)
- [langgraph-101](https://github.com/langchain-ai/langgraph-101)
- [langchain-academy](https://github.com/langchain-ai/langchain-academy)
