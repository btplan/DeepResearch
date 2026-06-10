# Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 格式，版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Added
### Changed
### Fixed
### Removed

## [0.1.0] - 2026-01-31

### Added
- 基于 LangGraph StateGraph 的多 Agent 深度研究系统
- Coordinator 协调器：接收用户输入，判断任务类型并路由
- Background Investigator 背景调查节点：规划前进行网络预搜索
- Planner 规划器：自动生成结构化研究计划（含 thought、steps）
- Research Team 研究团队编排器：按 step_type 路由到 Researcher 或 Coder
- Researcher 研究员：网络搜索与资料调研，支持 MCP 扩展
- Coder 编码器：Python REPL 执行数据分析、计算、图表生成
- Reporter 报告生成器：汇总 observations 生成结构化 Markdown 报告
- Human Feedback 人工审核节点：支持 ACCEPTED / EDIT_PLAN 交互
- 多搜索引擎支持：Tavily、DuckDuckGo、Brave Search、ArXiv、SearX、Wikipedia
- MCP 协议支持：通过 langchain-mcp-adapters 接入外部工具
- 命令行参数：`--interactive`、`--debug`、`--max_plan_iterations`、`--max_step_num`、`--no-background-investigation`
- uv / pyproject.toml 项目管理

[Unreleased]: https://github.com/<user>/deep-research/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/<user>/deep-research/releases/tag/v0.1.0
