# 开发与技术（development-technical）

共 5 个技能。MCP 服务器开发、Web 应用测试、技能创建、GIF 制作

---

## mcp-builder

**中文名**：MCP 服务器构建

### 功能

创建高质量的 MCP（模型上下文协议）服务器的指南，使大语言模型能够通过精心设计的工具与外部服务交互。支持 Python（FastMCP）和 Node/TypeScript（MCP SDK）两种技术栈。质量以 LLM 完成真实任务的能力衡量。工作流包括研究规划、API 覆盖率分析、工具命名、上下文管理和错误消息处理等阶段。

**英文原文**：

Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

### 使用领域

AI 工具开发、API 集成、LLM 工具链、MCP 协议

### 使用场景

当构建 MCP 服务器以集成外部 API 或服务时使用，无论使用 Python（FastMCP）还是 Node/TypeScript（MCP SDK）。


> **许可证**：Apache 2.0 开源，详见 LICENSE.txt

---

## skill-creator

**中文名**：技能创建器

### 功能

创建有效技能的指南。技能是模块化的软件包，可通过专业知识、工作流和工具集成来扩展 Claude 的能力。强调简洁性、适当的自由度（高/中/低），以及技能结构（SKILL.md 加可选资源）。包含初始化、打包和快速验证脚本。

**英文原文**：

Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.

### 使用领域

AI 工具开发、技能扩展、Claude 定制、插件开发

### 使用场景

当用户想要创建新技能或更新现有技能以扩展 Claude 的能力（包括专业知识、工作流或工具集成）时使用。


> **许可证**：Apache 2.0 开源，详见 LICENSE.txt

---

## slack-gif-creator

**中文名**：Slack GIF 制作

### 功能

为 Slack 创建优化的动画 GIF 的知识和工具。提供约束（尺寸：128x128 表情符号、480x480 消息）、验证工具和动画概念。使用 GIFBuilder 和 PIL 构建帧、添加并保存为 Slack 友好的优化格式。

**英文原文**：

Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack."

### 使用领域

动画制作、GIF 创作、Slack 集成、视觉通信

### 使用场景

当用户请求为 Slack 创建动画 GIF 时使用，例如「为我做一个 X 做 Y 动作的 Slack GIF」。


> **许可证**：Apache 2.0 开源，详见 LICENSE.txt

---

## web-artifacts-builder

**中文名**：Web 制品构建器

### 功能

使用现代前端技术（React、Tailwind CSS、shadcn/ui）创建精细的多组件 HTML 制品的工具套件。技术栈：React 18 + TypeScript + Vite + Parcel + Tailwind CSS + shadcn/ui。工作流包括初始化、编辑代码、打包和展示。适用于需要状态管理、路由或 shadcn/ui 组件的复杂制品。

**英文原文**：

Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

### 使用领域

前端开发、组件构建、React 应用、UI 工具链

### 使用场景

当需要使用 React、Tailwind CSS、shadcn/ui 创建复杂的多组件 HTML 制品时使用。不适用于简单的单文件 HTML/JSX 制品。


> **许可证**：Apache 2.0 开源，详见 LICENSE.txt

---

## webapp-testing

**中文名**：Web 应用测试

### 功能

使用 Playwright 交互和测试本地 Web 应用的工具包。支持验证前端功能、调试 UI 行为、捕获浏览器截图和查看浏览器日志。提供 with_server.py 脚本管理服务器生命周期，支持静态和动态应用、单服务器和多服务器场景。

**英文原文**：

Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

### 使用领域

Web 测试、前端测试、UI 自动化、Playwright

### 使用场景

当需要与本地 Web 应用交互并测试时使用，包括验证前端功能、调试 UI 行为、捕获截图和查看日志。


> **许可证**：Apache 2.0 开源，详见 LICENSE.txt
