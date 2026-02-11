# Android 系统开发可用的 Cursor Skills

本文档从当前 Cursor Skills 中筛选出**与 Android 系统开发相关**的技能，按用途分类，并给出中文的**功能**与**使用方法**说明。
**未对 `skills` 文件夹做任何修改。**

---

## 一、直接相关（移动端 / 跨平台 / 应用商店）

| 技能 ID                                                  | 中文名                  | 功能                                                                                                                   | 使用方法                                                                                                                              |
| -------------------------------------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **mobile-design**                                  | 移动端 设计             | 面向 iOS 与 Android 的移动优先设计与工程规范，涵盖触控交互、性能、平台约定、离线行为与移动端最佳实践。                 | 做 Android/iOS 界面与交互设计、性能与平台规范时使用；对话中出现 mobile、ios、android、touch、performance、platform 等关键词时会触发。 |
| **mobile-developer**                               | 移动端 开发             | 使用 React Native、Flutter 或原生技术开发移动应用，掌握现代架构模式、跨平台开发、原生集成与离线同步等。                | 开发 Android/跨平台 App、做原生模块或离线同步时使用；关键词：mobile、react native、flutter、cross-platform。                          |
| **react-native-architecture**                      | React Native 架构       | 使用 Expo、导航、原生模块、离线同步与跨平台模式构建生产级 React Native 应用（含 Android）。                            | 开发或维护 React Native 项目（含 Android 端）、做导航/原生模块/离线同步时使用。                                                       |
| **flutter-expert**                                 | Flutter 专家            | 掌握 Flutter 与 Dart 3、高级组件、多平台部署，涵盖状态管理、动画、测试与性能优化（Android 为重要目标平台）。           | 用 Flutter 开发或优化 Android 应用时使用；关键词：flutter、dart、widgets、multi-platform。                                            |
| **app-store-optimization**                         | 应用商店 优化           | 完整的应用商店优化（ASO）工具集，用于调研、优化与追踪移动应用在**Google Play Store** 与 Apple App Store 的表现。 | 上架/优化 Android 应用在 Google Play 的列表、关键词与转化时使用；关键词：app store、ASO、mobile、Google Play。                        |
| **frontend-mobile-development-component-scaffold** | 前端 移动端 组件 脚手架 | 面向生产可用的移动端 React 组件架构，生成可访问、高性能的组件脚手架。                                                  | 为移动端（含 Android/RN）搭建或规范组件结构时使用。                                                                                   |
| **game-development/mobile-games**                  | 游戏 开发/移动端 游戏   | 移动端游戏开发原则：触控输入、电量、性能、应用商店发布等。                                                             | 做 Android 移动游戏或涉及触控/性能/上架时使用。                                                                                       |
| **multi-platform-apps-multi-platform**             | 多平台 应用             | 在 Web、移动端与桌面端一致地构建与部署同一功能，采用 API 优先架构与并行实现策略。                                      | 做 Android 与其它平台（Web/iOS）同一产品线时使用。                                                                                    |
| **expo-deployment**                                | Expo 部署               | 将 Expo 项目部署到生产环境（常用于 React Native，含 Android 构建与发布）。                                             | 使用 Expo 管理 RN 项目并部署 Android 版本时使用。                                                                                     |
| **upgrading-expo**                                 | 升级 Expo               | 升级 Expo SDK 版本，保障 RN/Expo 项目（含 Android）的依赖与兼容性。                                                    | 升级 Expo 或 RN 工程时使用；关键词：expo、upgrade、sdk。                                                                              |

---

## 二、语言与后端（Android 开发常用技术栈）

| 技能 ID                                         | 中文名                 | 功能                                                                                                                                                      | 使用方法                                                       |
| ----------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **java-pro**                              | Java 专业版            | 掌握 Java 21+ 与现代特性（虚拟线程、模式匹配、Spring Boot 3.x 等），适用于 Android 传统 Java 代码与后端服务。                                             | 编写或重构 Android Java 代码、或开发/对接 Java 后端时使用。    |
| **senior-architect**                      | 高级 架构师            | 全栈软件架构，涵盖 ReactJS、NextJS、NodeJS、Express、**React Native、Swift、Kotlin、Flutter**、Postgres、GraphQL 等，含架构图、技术选型与依赖分析。 | 做包含 Android/Kotlin/RN/Flutter 的系统架构或技术选型时使用。  |
| **api-design-principles**                 | API 设计 原则          | REST 与 GraphQL API 设计原则，便于 Android 客户端与后端约定接口。                                                                                         | 设计或评审 Android 应用所调用的 API 时使用。                   |
| **api-patterns**                          | API 模式               | API 设计决策：REST / GraphQL / tRPC 选型、响应格式、版本与分页等。                                                                                        | 确定 Android 端与后端的接口风格与约定时使用。                  |
| **firebase**                              | Firebase               | 快速搭建后端：认证、数据库、存储、云函数与托管；Android 官方推荐集成之一。                                                                                | 在 Android 项目中集成 Firebase 认证、Firestore、FCM 等时使用。 |
| **graphql** / **graphql-architect** | GraphQL / GraphQL 架构 | GraphQL 查询与架构设计，适合移动端按需拉取数据（含 Android 客户端）。                                                                                     | Android 使用 GraphQL 接口或做 BFF 设计时使用。                 |

---

## 三、架构、代码质量与性能

| 技能 ID                                                          | 中文名                   | 功能                                                                    | 使用方法                                            |
| ---------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------- | --------------------------------------------------- |
| **architecture**                                           | 架构                     | 架构决策框架：需求分析、权衡评估与 ADR 文档化。                         | 做 Android 模块划分、技术选型或记录架构决策时使用。 |
| **architecture-patterns**                                  | 架构 模式                | 实现清洁架构、六边形架构、领域驱动设计等后端/全栈架构模式。             | 为 Android 应用设计分层或模块边界时使用。           |
| **clean-code** / **code-refactoring-refactor-clean** | 整洁代码 / 重构          | 整洁代码原则、SOLID 与重构实践。                                        | 审查或重构 Android 代码质量时使用。                 |
| **code-review-checklist** / **code-reviewer**        | 代码评审 清单 / 代码评审 | 覆盖功能、安全、性能与可维护性的评审清单与 AI 辅助代码审查。            | 对 Android 代码做 Code Review 时使用。              |
| **application-performance-performance-optimization**       | 应用 性能 优化           | 应用层性能优化思路与实践。                                              | 优化 Android 启动、内存、卡顿或耗电时使用。         |
| **react-best-practices**                                   | React 最佳 实践          | React/Next 性能与最佳实践（若 Android 端使用 RN，可参考前端性能思路）。 | 做 React Native 性能优化或最佳实践时使用。          |

---

## 四、认证、安全与合规

| 技能 ID                                     | 中文名                    | 功能                                                                            | 使用方法                                               |
| ------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **auth-implementation-patterns**      | 认证 实现 模式            | 认证与授权模式：JWT、OAuth2、会话管理与 RBAC，便于在 Android 端实现登录与权限。 | 在 Android 中实现登录、Token 刷新或权限控制时使用。    |
| **mobile-security-coder**             | 移动端 安全 编码          | 移动端安全编码：输入校验、WebView 安全与移动端特有安全模式。                    | 处理 Android 输入校验、WebView、存储与通信安全时使用。 |
| **frontend-mobile-security-xss-scan** | 前端 移动端 安全 XSS 扫描 | 前端/移动端 XSS 与注入类漏洞检测与防护（含 WebView 与混合内容）。               | 对 Android 内 WebView 或混合页面做安全审查时使用。     |
| **api-security-best-practices**       | API 安全 最佳 实践        | API 安全设计：认证、授权、输入校验、限流与常见 API 漏洞防护。                   | 设计或加固 Android 调用的 API 安全时使用。             |
| **gdpr-data-handling**                | GDPR 数据 处理            | 符合 GDPR 的数据处理：同意管理、数据主体权利与隐私设计。                        | Android 应用处理欧盟用户数据或隐私合规时使用。         |

---

## 五、测试与质量

| 技能 ID                                                    | 中文名                  | 功能                                                              | 使用方法                                             |
| ---------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------- | ---------------------------------------------------- |
| **testing-patterns**                                 | 测试 模式               | Jest 等测试模式、工厂函数、Mock 策略与 TDD 流程。                 | 编写 Android/RN 单元测试或建立测试规范时使用。       |
| **javascript-testing-patterns**                      | Javascript 测试 模式    | 使用 Jest、Vitest、Testing Library 的单元/集成/E2E 与 Mock 策略。 | React Native（JS/TS）测试时使用。                    |
| **e2e-testing-patterns**                             | E2E 测试 模式           | 端到端测试设计与实践。                                            | 设计或实现 Android/RN 端到端或 UI 自动化测试时使用。 |
| **unit-testing-test-generate**                       | 单元 测试 生成          | 跨语言生成可维护的单元测试与边界用例。                            | 为 Android 或后端代码补充单元测试时使用。            |
| **test-driven-development** / **tdd-workflow** | 测试驱动开发 / TDD 流程 | TDD 流程与 RED-GREEN-REFACTOR 实践。                              | 按 TDD 方式开发 Android 功能时使用。                 |
| **debugger** / **systematic-debugging**        | 调试器 / 系统化 调试    | 针对错误、测试失败与异常行为的调试思路与步骤。                    | 排查 Android 崩溃、ANR 或测试失败时使用。            |
| **playwright-skill**                                 | Playwright 技能         | 浏览器自动化与测试（可用于 RN/Web 或配套 Web 管理端测试）。       | 做与 Android 相关的 Web 端或 E2E 自动化时使用。      |

---

## 六、国际化、UI 与文档

| 技能 ID                                                      | 中文名                | 功能                                                                                        | 使用方法                                           |
| ------------------------------------------------------------ | --------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **i18n-localization**                                  | 国际化 本地化         | 国际化与本地化：硬编码字符串检测、翻译管理、多语言资源与 RTL 支持。                         | Android 多语言、字符串资源与 RTL 适配时使用。      |
| **ui-ux-pro-max**                                      | UI/UX 专业 版         | UI/UX 设计智能体，支持多种技术栈（含**React Native、Flutter**）的样式、配色与图表等。 | 设计或统一 Android/RN/Flutter 的界面与体验时使用。 |
| **documentation-templates** / **docs-architect** | 文档 模板 / 文档 架构 | 文档结构与从代码生成技术文档的实践。                                                        | 为 Android 模块或 API 编写/维护文档时使用。        |

---

## 七、CI/CD、部署与运维

| 技能 ID                                     | 中文名              | 功能                                                                  | 使用方法                                          |
| ------------------------------------------- | ------------------- | --------------------------------------------------------------------- | ------------------------------------------------- |
| **cicd-automation-workflow-automate** | CI/CD 自动化        | 设计高效的 CI/CD 流水线、GitHub Actions 与自动化开发流程。            | 为 Android 项目配置构建、测试与发布流水线时使用。 |
| **github-actions-templates**          | GitHub Actions 模板 | GitHub Actions 工作流模板。                                           | 为 Android 仓库配置构建、测试或发布 job 时使用。  |
| **deployment-pipeline-design**        | 部署 流水线 设计    | 多阶段 CI/CD、审批门禁、安全检查与部署编排。                          | 设计 Android 应用的构建与发布流程时使用。         |
| **docker-expert**                     | Docker 专家         | 容器化、多阶段构建、镜像优化与编排（可用于 Android 构建或后端服务）。 | 用 Docker 做 Android 构建环境或后端服务时使用。   |

---

## 八、参考：iOS 与双平台

| 技能 ID                 | 中文名   | 功能                                                                                | 使用方法                                          |
| ----------------------- | -------- | ----------------------------------------------------------------------------------- | ------------------------------------------------- |
| **ios-developer** | iOS 开发 | 使用 Swift/SwiftUI 开发原生 iOS 应用；与 Android 双平台开发时可参考架构与发布思路。 | 同时维护 iOS 与 Android 或参考 iOS 端设计时使用。 |

---

## 使用方式小结

- **在 Cursor 中**：在对话里通过 **@技能名**（如 `@mobile-developer`、`@java-pro`）或提及上述**关键词**即可触发对应技能。
- **详细说明**：每个技能的完整中文说明（功能、使用领域、使用场景）见 `doc` 下对应分类文档（如 `skills_development.md`、`skills_security.md` 等）。
- **数据来源**：技能列表与分类来自 `skills/CATALOG.md`，未修改 `skills` 文件夹内任何文件。

---

## 按用途快速索引

- **做 Android 原生 / Kotlin**：java-pro、senior-architect、architecture、mobile-security-coder
- **做 React Native（含 Android）**：mobile-developer、react-native-architecture、expo-deployment、upgrading-expo、javascript-testing-patterns
- **做 Flutter（含 Android）**：flutter-expert、mobile-developer、ui-ux-pro-max
- **上架与推广**：app-store-optimization
- **接口与后端**：api-design-principles、api-patterns、firebase、graphql、auth-implementation-patterns
- **安全与合规**：auth-implementation-patterns、mobile-security-coder、api-security-best-practices、gdpr-data-handling
- **测试与调试**：testing-patterns、e2e-testing-patterns、unit-testing-test-generate、debugger、playwright-skill
- **多语言与 UI**：i18n-localization、ui-ux-pro-max
- **流水线与发布**：cicd-automation-workflow-automate、github-actions-templates、deployment-pipeline-design
