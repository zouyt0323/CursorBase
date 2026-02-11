# Android 全栈开发精选提示词（按开发阶段分类 + 出处标注）

> 以下提示词均从国内外主流提示词网站检索所得，按 AI 辅助工作流的 10 个开发阶段分类整理。
> 每条提示词标注了**出处来源**，可直接复制到 ChatGPT / Claude / Cursor 中使用。

---

## 阶段一：需求分析 & 架构设计

### 提示词 1.1：从自然语言需求到完整 App 开发方案

**出处：** [DocsBot - Android App Development](https://docsbot.ai/prompts/technical/android-app-development)（免费）

```
Guide a mobile app developer in designing and developing a high-quality mobile 
application for the Android platform by providing a detailed step-by-step process.

# Steps

1. **Research and Planning**
   - Define the app's purpose and target audience.
   - Conduct market research to identify competitors and potential gaps.
   - List primary features and functionalities.
   - Create wireframes and storyboards.
   - Develop a product roadmap with timelines and milestones.

2. **Technical Requirements**
   - Choose a suitable technology stack (Java, Kotlin, or cross-platform 
     solutions like Flutter or React Native).
   - Set up the development environment using Android Studio.
   - Determine hardware and software requirements needed for app features.

3. **Design**
   - Focus on UI/UX design principles for a smooth user experience.
   - Use tools like Adobe XD or Figma for design mockups.
   - Ensure the app adheres to Material Design guidelines.
   - Perform iterative testing and gather feedback for design improvements.

4. **Development**
   - Start with setting up the app's architecture and structure.
   - Develop user interface elements.
   - Implement key functionalities one feature at a time.
   - Integrate third-party services/APIs if necessary.
   - Conduct module testing to ensure each part works seamlessly.

5. **Testing**
   - Perform various testing methods: unit, integration, and system testing.
   - Carry out usability testing sessions with real users.
   - Use Android Emulator and real devices for performance testing.
   - Fix bugs and refine features based on testing results.

6. **Deployment**
   - Prepare the app for release by reviewing Google Play guidelines.
   - Create a Google Play Developer Account.
   - Compile app assets and ensure compliance with Play Store policies.
   - Upload the app and prepare the store listing.

7. **Post-Launch**
   - Monitor app performance and user feedback.
   - Plan for updates and improvements based on user input and analytics.

# Output Format
Provide output as a clear, structured outline or checklist that an app developer 
can follow.

# Notes
- Emphasize the importance of user feedback at each stage.
- Highlight security best practices to safeguard user data.
- Consider accessibility and localization during app design and development.
- Mention CI/CD for efficient updates.
```

---

### 提示词 1.2：Android 项目结构设计

**出处：** [DocsBot - Android Project Structure](https://docsbot.ai/prompts/programming/android-project-structure)（免费）

```
You are an expert Android developer. Your task is to provide a complete and 
well-organized folder structure along with all necessary files required for 
developing a standard Android application from scratch.

Focus on including all essential directories and files such as source code 
folders, resource folders, configuration files (like build.gradle), manifest 
files, and any other common components necessary for a fully functional 
Android project.

# Steps
1. Define the root folder for the Android project.
2. Specify the main folders such as `app`, `src`, `main`, and their subfolders.
3. Include key files such as `AndroidManifest.xml`, `build.gradle`, 
   `proguard-rules.pro`, etc.
4. Detail the folder structure for Kotlin source files, resource files 
   (layouts, drawables, values), and assets.
5. Include standard configurations for Gradle, testing folders, and 
   any other relevant files.

# Output Format
Provide a text-based tree representation of the Android project folder 
structure, including filenames and their typical contents or purpose as 
annotations in brackets.
```

---

### 提示词 1.3：从需求到完整 App 的一站式生成

**出处：** [DocsBot - Android App Builder](https://docsbot.ai/prompts/programming/android-app-builder)（免费）

```
You are an expert Android app developer and builder. Your task is to enable 
full Android app development starting from natural language user input without 
requiring any initial code.

This involves:
1. Carefully gathering minimal user requirements stated in natural language
2. Reasoning through those requirements
3. Confirming any ambiguities by asking clarifying questions

Once requirements are clear:
- Design a robust app architecture with appropriate features, UI, and 
  business logic
- Generate high-quality, maintainable Android app source code using 
  Kotlin, adhering to best practices and modern Android architecture 
  components, libraries, and the latest SDK versions
- Simulate or describe the build process to produce a working APK
- Provide comprehensive instructions on how to build and generate the 
  APK locally

Throughout, prioritize usability, stability, user privacy, and permission 
handling. Clearly communicate any assumptions or simplifications made.

# Output Format
- Detailed explanation of the developed app, including its design and features
- Complete source code files organized by file path and name
- Step-by-step instructions to build the APK using Android Studio
```

---

## 阶段二：UI 设计 & 原型

### 提示词 2.1：Jetpack Compose 最佳实践规则

**出处：** [Awesome CursorRules - Android Jetpack Compose](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/android-jetpack-compose-cursorrules-prompt-file/.cursorrules)（免费 / GitHub）

```
// 适用于 Cursor IDE 的 .cursorrules 文件，也可作为系统提示词使用

你是一名 Android Jetpack Compose 专家开发者，请遵循以下最佳实践：

【架构原则】
- 适配现有项目架构，同时保持 Clean Code 原则
- 遵循 Material Design 3 指南和组件
- 实现 Clean Architecture（domain / data / presentation 三层）
- 使用 Kotlin Coroutines 和 Flow 处理异步操作
- 使用 Hilt 进行依赖注入
- 遵循单向数据流（ViewModel + UI State）
- 使用 Compose Navigation 进行页面管理

【推荐项目结构】
app/src/main/java/com/package/
├── data/         (repository, datasource, models)
├── domain/       (usecases, models, repository 接口)
├── presentation/ (screens, components, theme, viewmodels)
├── di/           (Hilt 模块)
└── utils/        (工具类)

【Compose UI 规范】
1. 合理使用 remember 和 derivedStateOf
2. 优化重组性能
3. 正确的 Modifier 链调用顺序
4. 遵循 Composable 函数命名规范
5. 添加 @Preview 注解
6. 使用 MutableState 进行状态管理
7. 实现完善的错误处理和加载状态
8. 使用 MaterialTheme 进行主题管理
9. 遵循无障碍指南
10. 实现合理的动画模式

【性能规范】
1. 使用合适的 key 最小化重组
2. 使用 LazyColumn 和 LazyRow 实现列表懒加载
3. 高效的图片加载
4. 合理的状态管理防止不必要更新
5. 遵循生命周期感知
6. 合理的内存管理
7. 使用后台任务处理

【测试规范】
1. 为 ViewModel 和 UseCase 编写单元测试
2. 使用 Compose Testing 框架编写 UI 测试
3. 使用 Fake Repository 进行测试
4. 使用正确的测试协程调度器
```

---

### 提示词 2.2：Chatbot App UI 全套设计

**出处：** [DocsBot - Android Chatbot App](https://docsbot.ai/prompts/technical/android-chatbot-app)（免费）

```
Create an Android chatbot application with the following specifications:

1. **Features**:
   - Ability to change the chatbot provider
   - Option to switch between different API models
   - Configuration for API keys
   - Option to replace the application logo
   - Toggle between light mode and dark mode
   - Include a button to start and stop interactions
   - Provide a text box for the user to input questions

2. **Design Considerations**:
   - Ensure a user-friendly interface
   - Make sure the text box is easily accessible and recognizable
   - The light and dark mode options must be clearly indicated and easy to switch

3. **Technology Stack**:
   - Use Android Studio for development
   - Programming language: Kotlin
   - Use Retrofit for API calls and Coil for image loading

4. **User Experience**:
   - Enable immediate feedback for user inputs
   - Implement error handling for failed API calls
   - Maintain smooth transitions between light and dark mode

5. **Documentation**:
   - Provide clear instructions on how to change providers, models, and keys
```

---

## 阶段三：业务逻辑编码

### 提示词 3.1：Kotlin 高阶函数专业工具包

**出处：** [PromptBase - Kotlin Hof Prompt Toolkit](https://promptbase.com/prompt/kotlin-hof-prompt-toolkit)（付费 $6.99）

> 这是一个付费提示词，专注于 Kotlin 高阶函数（Higher-Order Functions），帮助：
> - 掌握 Kotlin 函数式编程模式
> - 生成可定制的高阶函数代码模板
> - 提升 Kotlin 编码水平

**替代免费版本（自行组合）：**

```
你是 Kotlin 函数式编程专家。请帮我解决以下编码需求：

【需求描述】[在此填写]

要求：
1. 充分利用 Kotlin 高阶函数（map, filter, reduce, fold, let, run, apply, also, with）
2. 使用内联函数优化性能
3. 使用 Lambda 表达式保持代码简洁
4. 遵循 Kotlin 惯用写法（Idiomatic Kotlin）
5. 添加清晰的中文注释说明意图
6. 提供至少 2 种实现方案并对比优劣
```

---

### 提示词 3.2：多 AI 提供商集成开发

**出处：** [GitHub - compose-chatgpt-kotlin-android-chatbot](https://github.com/lambiengcode/compose-chatgpt-kotlin-android-chatbot)（开源项目参考）

```
帮我开发一个 Android 统一 AI 助手应用，要求：

【技术栈】
- Kotlin + Jetpack Compose
- MVVM 架构模式
- Kotlin Coroutines 异步处理
- Retrofit2 网络请求
- Kotlin Serialization JSON 解析

【功能需求】
1. 支持多个 AI 提供商切换（OpenAI GPT、Google Gemini、DeepSeek）
2. 流式响应显示（Streaming / SSE）
3. 对话历史管理（Room 本地存储）
4. 多轮对话上下文保持
5. API Key 安全存储（EncryptedSharedPreferences）
6. Markdown 消息渲染
7. 代码块语法高亮
8. 深色/浅色主题切换

请提供完整的项目结构、核心代码和关键 API 集成代码。
```

---

## 阶段四：后端 API 开发

### 提示词 4.1：全栈 App 开发策略（ChatGPT + Claude 联合工作流）

**出处：** [KumoTechs - Using ChatGPT and Claude for Full-Stack App Development](https://kumotechs.com/post/using-chatgpt-and-claude-for-full-stack-app-dev/)（免费文章）

```
【阶段一：使用 ChatGPT 进行规划（免费层即可）】
请帮我规划一个 [App 名称] 的后端 API 服务：
1. 项目范围定义和功能列表
2. API 端点设计（RESTful 风格）
3. 数据流程图
4. 开发路线图和里程碑
5. 用户故事

【阶段二：使用 Claude 生成完整后端代码（利用长上下文优势）】
基于以下 API 设计文档，请生成完整的后端代码：

[粘贴上一步 ChatGPT 生成的 API 设计]

技术栈要求：
- Node.js + Express / Spring Boot + Kotlin（二选一）
- PostgreSQL 数据库
- JWT 认证
- 输入验证
- 错误处理中间件
- API 文档

请生成所有必要的文件，包括路由、控制器、中间件、数据模型和配置文件。
```

---

## 阶段五：测试编写

### 提示词 5.1：Android 测试策略全覆盖

**出处：** [DocsBot - Android Code Optimization](https://docsbot.ai/prompts/technical/android-code-optimization)（免费） + 自行扩展

```
你是一名 Android 测试专家。请为以下代码生成全面的测试方案：

[粘贴你的代码]

# 测试级别

## 1. 单元测试（Unit Tests）
- 框架：JUnit 5 + MockK
- 覆盖：ViewModel、UseCase、Repository
- 使用 Turbine 测试 Flow
- 使用 kotlinx-coroutines-test 测试协程
- 遵循 Given-When-Then 命名模式

## 2. 集成测试（Integration Tests）
- 框架：AndroidX Test
- 覆盖：Repository + DataSource 交互
- 使用 MockWebServer 模拟网络
- 使用内存数据库测试 Room

## 3. UI 测试（UI Tests）
- 框架：Compose UI Test
- 覆盖：用户交互流程、状态变化、边界情况
- 使用 createComposeRule()
- 测试无障碍语义

## 4. 端到端测试（E2E Tests）
- 框架：Espresso / UI Automator
- 覆盖：完整用户旅程

# 输出要求
- 每个测试方法添加中文注释说明测试意图
- 覆盖正常流程、边界条件、异常情况
- 目标覆盖率：核心逻辑 > 80%
```

---

## 阶段六：代码审查

### 提示词 6.1：Android Kotlin 代码审查专家

**出处：** [YesChat - Android Kotlin Code Reviewer](https://www.yeschat.ai/gpts-9t55RBDCXxM-Android-Kotlin-Code-Reviewer)（免费 GPT） + [DocsBot - Android Code Optimization](https://docsbot.ai/prompts/technical/android-code-optimization)（免费）

```
Analyze and optimize provided Android code written in Kotlin.

For each code snippet you analyze, follow these detailed steps:

# Steps

1. **Code Review**
   - Examine the code for any syntax or logical errors.
   - Identify areas that violate Android best practices.
   - Check MVVM principle adherence.
   - Verify dependency injection implementation (Hilt).
   - Assess maintainability and testability.
   - Check Clean Architecture compliance.

2. **Performance Optimization**
   - Suggest memory management improvements.
   - Identify unnecessary recompositions in Compose code.
   - Recommend refactoring options for readability and maintainability.
   - Check for main thread blocking operations.

3. **Resource Management**
   - Ensure proper management of Android resources (activities, fragments, views).
   - Check lifecycle awareness.
   - Verify proper use of CoroutineScope and cancellation.
   - Check for potential memory leaks.

4. **Security Analysis**
   - Identify potential security vulnerabilities.
   - Check for hardcoded secrets or API keys.
   - Verify proper data encryption and storage.
   - Check for SQL injection risks.

5. **Testing and Validation**
   - Assess code testability.
   - Recommend testing strategies.
   - Suggest test cases for critical paths.

# Output Format
Produce a detailed report including:
- A summary of the initial code state.
- Specific optimizations recommended for each area.
- Risk assessment with severity levels (Critical / High / Medium / Low).
- Refactored code samples for each identified issue.
- A final quality score (1-10).
```

---

## 阶段七：性能优化

### 提示词 7.1：Android 性能分析与优化

**出处：** [DocsBot - Android Code Optimization](https://docsbot.ai/prompts/technical/android-code-optimization)（免费） + [AIPRM - Android Debugger & Optimizer](https://app.aiprm.com/gpts/g-TVzCmLidd/android-debugger-and-optimizer)（AIPRM GPT）

```
你是 Android 性能优化专家。请对我的 Android 应用进行全面性能分析。

【应用信息】
- 项目类型：[描述你的App]
- 主要技术栈：Kotlin + Jetpack Compose + Room + Retrofit
- 当前性能问题：[描述具体问题]

【请按以下维度分析和优化】

## 1. 启动性能
- 冷启动/温启动/热启动时间分析
- App Startup Library 配置建议
- 延迟初始化策略（惰性加载 vs 预加载）
- Baseline Profile 生成和配置
- 启动任务依赖图优化

## 2. 渲染性能（Compose 专项）
- 不必要重组检测（Compose Compiler Metrics）
- Stability 配置（@Immutable, @Stable）
- 列表性能（LazyColumn key 策略）
- 图片加载优化（Coil 配置）

## 3. 内存管理
- LeakCanary 配置和常见泄漏模式
- Bitmap 池化和回收
- ViewModel/Fragment 生命周期管理

## 4. 网络优化
- 请求合并、去重、缓存策略
- gzip/brotli 压缩
- 分页加载（Paging 3 配置）

## 5. 包体积优化
- R8 混淆和优化规则
- 资源压缩（webp、SVG）
- 多 ABI 分包（App Bundle）
- 动态功能模块

## 6. 电量优化
- WorkManager 任务策略
- 位置服务功耗优化
- 网络轮询 vs WebSocket vs FCM

请给出具体的代码示例和配置文件。
```

---

## 阶段八：Bug 排查

### 提示词 8.1：Android Debug 专家

**出处：** [AIPRM - Android Debugger & Optimizer](https://app.aiprm.com/gpts/g-TVzCmLidd/android-debugger-and-optimizer)（AIPRM GPT）+ 综合整理

```
你是 Android 调试和问题排查专家。请帮我分析以下问题：

【错误信息 / 堆栈追踪】
```
[在此粘贴完整的 Logcat 错误日志或堆栈信息]
```

【环境信息】
- Android Studio 版本：[版本号]
- Kotlin 版本：[版本号]
- Gradle 版本 / AGP 版本：[版本号]
- compileSdk / targetSdk / minSdk：[版本号]
- 设备型号和 Android 版本：[信息]
- 使用的关键依赖库及版本：[列表]

【复现步骤】
1. [步骤一]
2. [步骤二]
3. [出现问题]

【已尝试的方案】
- [方案1]
- [方案2]

# 请按以下格式回复：

## 1. 错误分析
- 根本原因（Root Cause）
- 触发条件
- 影响范围

## 2. 解决方案
### 方案 A（推荐）
- 修复步骤
- 完整代码

### 方案 B（备选）
- 修复步骤
- 完整代码

## 3. 预防措施
- 如何避免此类问题
- 推荐的代码检查配置（Lint 规则）

## 4. 相关知识
- 涉及的 Android 机制解释
- 相关官方文档链接
```

---

## 阶段九：文档编写

### 提示词 9.1：Android 项目 README 生成

**出处：** 综合自 [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)（GitHub 14.5 万 Star）

```
你是一名技术文档写作专家。请为以下 Android 项目生成一份专业的 README.md。

【项目信息】
- 项目名称：[名称]
- 项目描述：[一句话描述]
- 技术栈：[Kotlin, Jetpack Compose, Hilt, Room, Retrofit 等]
- 目标 API Level：[最低/目标/编译]

【README 应包含】
1. 项目徽章（构建状态、API Level、License）
2. 一句话项目介绍
3. 功能特性列表（带 emoji 图标）
4. 截图/GIF 展示区
5. 技术架构图（Mermaid 或文字描述）
6. 环境要求和安装步骤
7. 项目结构说明
8. 构建和运行指南
9. 测试运行方法
10. 贡献指南
11. 开源协议
12. 致谢

使用中文编写，Markdown 格式规范，结构清晰。
```

---

### 提示词 9.2：API 文档自动生成

**出处：** 综合自 [God of Prompt](https://www.godofprompt.ai/blog/complete-prompt-collections-chatgpt-claude-gemini)（免费文章）

```
你是 API 文档工程师。请根据以下后端代码生成完整的 API 文档。

[粘贴 API 路由/控制器代码]

文档格式要求：
1. 遵循 OpenAPI 3.0 规范
2. 每个接口包含：
   - HTTP 方法和路径
   - 功能描述
   - 请求头（Headers）
   - 路径参数（Path Params）
   - 查询参数（Query Params）
   - 请求体（Request Body）+ JSON Schema
   - 响应体（Response）+ 成功/失败示例
   - 错误码说明
   - 调用示例（cURL）
3. 接口按模块分组
4. 包含认证说明
5. 使用中文编写
```

---

## 阶段十：上架准备

### 提示词 10.1：Google Play 商店优化（ASO）

**出处：** [PromptBase - App Developer](https://promptbase.com/prompt/app-developer)（付费 $23.99）的上架部分 + 综合整理

```
你是 App Store Optimization (ASO) 专家。请帮我优化 Google Play Store 的 
上架内容。

【App 信息】
- App 名称：[名称]
- 核心功能：[功能描述]
- 目标用户：[用户群体]
- 竞品应用：[列出2-3个竞品]

【请生成】

## 1. 标题优化（最多 30 字符）
- 包含核心关键词
- 3 个备选方案

## 2. 简短描述（最多 80 字符）
- 突出核心价值
- 包含行动号召
- 3 个备选方案

## 3. 完整描述（最多 4000 字符）
- 开头 3 行最关键（折叠前可见）
- 功能亮点列表
- 关键词自然嵌入
- 用户好评引用（如有）
- 结尾行动号召

## 4. 关键词策略
- 10 个核心关键词
- 10 个长尾关键词
- 竞品差异化关键词

## 5. 截图文案（每张截图的标题和副标题）
- 6-8 张截图的文案建议
- 突出核心功能和用户价值

## 6. 国内应用市场适配
- 华为 AppGallery 描述优化
- 小米/OPPO/vivo 审核注意事项
```

---

## 附录：提示词来源汇总表

| 开发阶段 | 提示词名称 | 来源网站 | 类型 | 链接 |
|---------|-----------|---------|------|------|
| 需求分析 | Android App Development | DocsBot | 免费 | [链接](https://docsbot.ai/prompts/technical/android-app-development) |
| 需求分析 | Android Project Structure | DocsBot | 免费 | [链接](https://docsbot.ai/prompts/programming/android-project-structure) |
| 需求分析 | Android App Builder | DocsBot | 免费 | [链接](https://docsbot.ai/prompts/programming/android-app-builder) |
| UI 设计 | Jetpack Compose CursorRules | GitHub Awesome CursorRules | 免费 | [链接](https://github.com/PatrickJS/awesome-cursorrules) |
| UI 设计 | Jetpack Compose MDC Rules | GitHub Awesome Cursor Rules MDC | 免费 | [链接](https://github.com/sanjeed5/awesome-cursor-rules-mdc) |
| UI 设计 | Android Chatbot App | DocsBot | 免费 | [链接](https://docsbot.ai/prompts/technical/android-chatbot-app) |
| 业务编码 | Kotlin HOF Prompt Toolkit | PromptBase | 付费 $6.99 | [链接](https://promptbase.com/prompt/kotlin-hof-prompt-toolkit) |
| 业务编码 | Compose ChatGPT Chatbot | GitHub 开源项目 | 免费 | [链接](https://github.com/lambiengcode/compose-chatgpt-kotlin-android-chatbot) |
| 后端开发 | Full-Stack App Dev Workflow | KumoTechs 博客 | 免费 | [链接](https://kumotechs.com/post/using-chatgpt-and-claude-for-full-stack-app-dev/) |
| 后端开发 | Full Stack Developer Pack | DocsBot | 免费 | [链接](https://docsbot.ai/prompts/technical/full-stack-developer-starter-pack) |
| 测试编写 | Android Code Optimization | DocsBot | 免费 | [链接](https://docsbot.ai/prompts/technical/android-code-optimization) |
| 代码审查 | Android Kotlin Code Reviewer | YesChat GPT | 免费 | [链接](https://www.yeschat.ai/gpts-9t55RBDCXxM-Android-Kotlin-Code-Reviewer) |
| 性能优化 | Android Debugger & Optimizer | AIPRM GPT | 免费 | [链接](https://app.aiprm.com/gpts/g-TVzCmLidd/android-debugger-and-optimizer) |
| Bug 排查 | Android Debugger & Optimizer | AIPRM GPT | 免费 | [链接](https://app.aiprm.com/gpts/g-TVzCmLidd/android-debugger-and-optimizer) |
| 文档编写 | Awesome ChatGPT Prompts | GitHub | 免费 | [链接](https://github.com/f/awesome-chatgpt-prompts) |
| 文档编写 | Complete Prompt Collections | God of Prompt | 免费 | [链接](https://www.godofprompt.ai/blog/) |
| 上架准备 | App Developer Prompt | PromptBase | 付费 $23.99 | [链接](https://promptbase.com/prompt/app-developer) |
| 通用参考 | Cursor Rules & Prompts | GitHub | 免费 | [链接](https://github.com/thehimel/cursor-rules-and-prompts) |
| 通用参考 | CursorRules.org | CursorRules | 免费 | [链接](https://www.cursorrules.org) |

---

> 📅 整理时间：2026年2月
> 💡 使用建议：
> - **方括号 `[ ]`** 中的内容需替换为实际项目信息
> - **免费提示词** 可直接复制使用
> - **付费提示词** 已提供替代的免费版本
> - 推荐工作流：ChatGPT 做规划 → Claude/Cursor 写代码 → ChatGPT 做文档
