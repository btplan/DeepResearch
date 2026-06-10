# Ace Research

Ace Research 是一个基于 LangChain 和 LangGraph 构建的智能研究 Agent 系统。它能够执行背景调查、制定计划并执行多步骤任务，通过集成多种工具（如搜索、Python REPL 等）来回答用户提出的复杂问题。

## ✨ 主要特性

*   **智能工作流**：基于 LangGraph 的图结构工作流，支持复杂的任务编排。
*   **背景调查**：在制定计划前自动进行网络搜索（可配置），以获取更充分的上下文信息。
*   **迭代规划**：支持多轮计划迭代，根据反馈动态调整执行步骤。
*   **MCP 支持**：内置 Model Context Protocol (MCP) 支持，例如 GitHub Trending 集成。
*   **交互模式**：提供命令行交互界面，方便连续对话和调试。
*   **多工具集成**：
    *   🔍 **网络搜索**：集成 Tavily Search 和 DuckDuckGo Search。
    *   🐍 **代码执行**：支持 Python REPL 执行代码。
    *   🗣️ **TTS**：文本转语音能力。

## 🛠️ 环境要求

*   Python >= 3.12
*   [uv](https://github.com/astral-sh/uv) (推荐用于依赖管理)

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone <repository-url>
cd ace-research
```

### 2. 安装依赖

本项目使用 `uv` 进行依赖管理。

```bash
uv sync
```

或者使用 pip：

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制 `.env.example` 文件为 `.env`，并填入必要的 API Key。

```bash
cp .env.example .env
```

需要配置以下环境变量：

*   `TAVILY_API_KEY`: Tavily Search API Key (用于网络搜索)
*   `DASHSCOPE_API_KEY`: 阿里云 DashScope API Key (默认使用 Qwen 大模型)

### 4. 运行项目

#### 命令行模式

直接在命令行中输入查询：

```bash
python main.py "嘉靖大礼议事件的起因和结果"
```

#### 交互模式

进入交互式对话环境：

```bash
python main.py --interactive
```

## ⚙️ 常用参数

`main.py` 支持多种参数来调整运行行为：

*   `--interactive`: 启用交互模式。
*   `--debug`: 启用调试日志，查看详细的 Agent 思考和工具调用过程。
*   `--max_plan_iterations`: 最大计划迭代次数 (默认: 1)。
*   `--max_step_num`: 每个计划的最大步骤数 (默认: 3)。
*   `--no-background-investigation`: 禁用初始的背景调查步骤。

**示例：**

启用调试模式并禁用背景调查：

```bash
python main.py "如何使用 LangChain" --debug --no-background-investigation
```

## 📂 项目结构

```text
ace-research/
├── agents/             # Agent 定义与 LLM 配置
├── config/             # 配置文件
├── graph/              # LangGraph 图结构定义
├── prompts/            # Prompt 模板
├── tools/              # 工具实现 (搜索, REPL 等)
├── utils/              # 通用工具函数
├── main.py             # 程序入口
├── workflow.py         # 工作流执行逻辑
├── graph.py            # 图构建逻辑
└── pyproject.toml      # 项目依赖配置
```

## 🤝 贡献说明

欢迎提交 Issue 和 Pull Request 来改进本项目。

## 📄 许可证

[License Link]
