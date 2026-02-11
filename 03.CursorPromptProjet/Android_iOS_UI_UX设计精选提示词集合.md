# Android / iOS UI/UX 设计精选提示词集合

> 整理时间：2026-02-10  
> 覆盖范围：UX研究、线框图、设计系统、移动端UI、无障碍、设计交付、应用商店优化等10大类  
> 来源：DocsBot、GitHub、Interaction Design Foundation、ProCreator、AppAgent、NNGroup 等

---

## 📑 目录

| 编号 | 类别 | 提示词数量 | 适用阶段 |
|------|------|-----------|---------|
| 1 | [UX研究与用户分析](#1-ux研究与用户分析) | 4 条 | 需求分析 → 用户画像 |
| 2 | [线框图与原型设计](#2-线框图与原型设计) | 4 条 | 概念设计 → 低/高保真原型 |
| 3 | [UI设计系统](#3-ui设计系统) | 3 条 | 设计规范 → 组件库 |
| 4 | [移动端UI设计哲学](#4-移动端ui设计哲学) | 2 条 | iOS HIG / Material Design 3 |
| 5 | [界面概念设计与生成](#5-界面概念设计与生成) | 3 条 | UI概念 → 可视化输出 |
| 6 | [无障碍设计](#6-无障碍设计accessibility) | 2 条 | WCAG合规 → ARIA实现 |
| 7 | [设计交付与代码转换](#7-设计交付与代码转换) | 3 条 | Figma → Compose/SwiftUI |
| 8 | [应用商店视觉优化](#8-应用商店视觉优化aso) | 2 条 | 图标设计 → 截图优化 |
| 9 | [微交互与动效设计](#9-微交互与动效设计) | 2 条 | 动画 → 手势反馈 |
| 10 | [可用性测试与设计评审](#10-可用性测试与设计评审) | 3 条 | 启发式评估 → 迭代改进 |

---

## 1. UX研究与用户分析

### 1.1 用户画像创建（User Persona Creator）

**出处**：[GitHub - claude-code-ui-agents](https://github.com/mustafakendiguzel/claude-code-ui-agents) / prompts/ux-research  
**适用模型**：Claude / ChatGPT / Gemini  
**难度**：中级

```
请为我的 [应用类型，如：健身追踪App] 创建详细的用户画像。考虑以下因素：

1. **人口统计**：年龄、性别、职业、收入、教育、地区
2. **心理特征**：生活方式、价值观、兴趣爱好
3. **技术素养**：设备偏好（iOS/Android）、App使用习惯、技术熟练度
4. **痛点与需求**：
   - 当前使用的替代方案及不满之处
   - 核心需求（功能性/情感性）
   - 使用场景（时间、地点、频率）
5. **用户目标**：
   - 主要目标（使用App的核心原因）
   - 次要目标（附带价值）
6. **行为模式**：使用频率、付费意愿、社交分享倾向

输出格式：
- 为每个画像提供一个虚拟姓名和照片描述
- 包含一段"典型一天"叙事
- 列出3-5个关键引语（代表用户心声）
- 标注设计启示（Design Implications）

请创建 3 个差异化的用户画像，覆盖主要用户群体和边缘用户群体。
```

---

### 1.2 用户研究框架（Who, Why, What, How）

**出处**：[Interaction Design Foundation](https://www.interaction-design.org/literature/article/chat-gpt-for-ux-design)  
**适用模型**：ChatGPT-4 / Claude  
**难度**：初级

```
帮我梳理我们新的 [App类型，如：移动健康管理App] 的 Who、Why、What、How 框架：

**Who（谁）**：
- 目标用户群体的详细画像
- 主要用户 vs 次要用户
- 用户的技术能力水平

**Why（为什么）**：
- 用户面临的核心痛点
- 现有解决方案的不足之处
- 我们的App能提供什么独特价值

**What（做什么）**：
- 必备功能（Must-have）列表
- 期望功能（Nice-to-have）列表
- MVP 阶段的功能范围

**How（怎么做）**：
- 用户如何发现和下载App
- 关键用户流程（注册→核心功能→留存）
- 主要交互模式和设计约束

请以结构化文档格式输出，每个部分包含具体的数据支持建议和设计启示。
```

---

### 1.3 用户旅程地图（Customer Journey Map）

**出处**：[UXPressia - AI Journey Mapping](https://uxpressia.com/blog/ai-journey-mapping-chatgpt)  
**适用模型**：ChatGPT / Claude  
**难度**：中级

```
为我的 [App名称/类型] 创建一个完整的用户旅程地图，覆盖以下阶段：

**阶段定义**：
1. 感知（Awareness）→ 2. 考虑（Consideration）→ 3. 获取（Acquisition）
→ 4. 首次使用（Onboarding）→ 5. 日常使用（Regular Use）→ 6. 推荐/流失（Advocacy/Churn）

每个阶段请提供：
- **用户行为**：用户在做什么？
- **触点（Touchpoints）**：通过什么渠道/界面与App交互？
- **用户想法**：用户在想什么？
- **情感曲线**：积极/中性/消极？标注情绪峰值和低谷
- **痛点**：遇到的困难和挫折
- **机会点（Opportunities）**：可以改善体验的设计机会

输出格式：
- 表格形式，行=阶段，列=维度
- 附加一个"关键时刻"（Moments of Truth）总结
- 列出前3个优先改善的触点及设计建议
```

---

### 1.4 用户访谈问题生成

**出处**：[Interaction Design Foundation](https://www.interaction-design.org/literature/article/chat-gpt-for-ux-design)  
**适用模型**：ChatGPT / Claude  
**难度**：初级

```
为我们的 [App类型，如：电商App] 生成一套用户访谈问题，重点了解以下方面：

1. **导航体验**：用户是否能轻松找到想要的内容？
2. **搜索功能**：搜索结果是否准确？筛选器是否有用？
3. **结账流程**：是否流畅？在哪个步骤容易放弃？
4. **视觉设计**：整体美感评价？哪些元素让用户印象深刻/困惑？
5. **信任感**：用户是否信任App的安全性？哪些因素影响信任？

要求：
- 每个方面5-7个问题
- 包含开放式问题和跟进追问（follow-up probes）
- 避免引导性问题
- 标注每个问题的设计洞察价值（高/中/低）
- 预估每个部分的访谈时长

目标时长：45分钟/每位用户
```

---

## 2. 线框图与原型设计

### 2.1 移动端线框图GPT提示词集

**出处**：[ProCreator Design](https://procreator.design/blog/guide-to-mobile-app-wireframe-gpt-prompts/)  
**适用模型**：ChatGPT / Claude  
**难度**：初级-中级

> **包含7个子提示词，覆盖线框设计全流程：**

**① 识别关键用户动作**
```
请为我的 [App类型] 的每个核心屏幕，概述用户在该屏幕上需要完成的主要动作。
如何通过视觉层次（大小、颜色、位置）来引导用户注意到这些关键动作？
请为每个屏幕提供布局建议。
```

**② 定义用户流程**
```
绘制一个简明的用户流程图，描述用户从 [入口点] 到 [主要目标，如：完成购买] 的完整路径。
每个屏幕如何衔接以促进这个旅程？标注每步的转化率优化建议。
```

**③ 处理空状态和错误状态**
```
为我的 [App类型] 设计以下特殊状态的界面方案：
- 空状态（首次使用无数据时）
- 加载状态（数据请求中）
- 错误状态（网络异常/服务器错误）
- 权限请求（相机/位置/通知等）
如何在保持用户参与度的同时，引导他们下一步操作？
```

**④ 原型化关键交互**
```
为以下交互元素创建简单的原型描述：
- [具体交互元素，如：底部弹出式选择器]
- [具体转场动画，如：卡片展开为详情页]
在用户测试中收到了混合反馈，请提供改进方案及动态交互规范。
```

**⑤ 可用性与可取性平衡**
```
基于以下可用性反馈，平衡"可用性"和"可取性"：
[粘贴用户反馈内容]
是否有用户想要但初始设计中未考虑的功能？如何在保持无缝用户体验的前提下融入这些功能？
```

**⑥ 结账/转化流程可视化**
```
为 [App类型] 设计完整的转化流程线框图：
[描述当前用户流程]
确保流程步骤最少化，每个阶段都有清晰的方向引导。
标注每步的最佳实践和常见反模式。
```

**⑦ 基于反馈的迭代**
```
初次用户测试后，发现以下区域存在困惑或挫折：
[提供具体的测试发现]
请基于反馈修订这些用户流程，目标是提升清晰度和易用性。
每项修改请说明修改理由和预期影响。
```

---

### 2.2 Google Stitch 线框图生成提示词（含WCAG合规）

**出处**：[DocsBot](https://docsbot.ai/prompts/productivity/google-stitch-wireframe-prompt)（免费）  
**适用模型**：Google Stitch AI / ChatGPT / Claude  
**难度**：高级

```
你是一位专家级提示词工程师，负责生成结构化的 Google Stitch AI 提示词，
用于创建完整的可视化线框图故事板。

设计要求：
- 为每个屏幕(WF#)生成一张极简、可访问的UI线框图
- 采用Figma风格布局，针对手机和平板优化
- 严格遵循WCAG 2.1 AA无障碍标准（字体对比度、可缩放文本）
- 每个布局必须包含：
  - 输入字段、开关、结果和逻辑的清晰标注
  - 数据字段标签对应SQL或Firestore Schema
  - 嵌入可追溯标签：FR#（功能需求）、WF#（线框图）、MOD#（模块）

需要生成的线框图：
- 模块1：引导流程
  - WF#1a: 头像选择屏幕（2个角色选项、心情滑块、继续按钮）
  - WF#1b: 同意与隐私协议（GDPR开关、时间戳审计字段）
  - WF#1c: 用户欢迎仪表盘（头像介绍、开始按钮、激励引语）
- 模块2：每日自检
  - WF#2a: 心情追踪器（表情量表、提交按钮、时间戳）
  - WF#2b: 睡眠质量输入（数字输入、单选按钮、备注区域）

输出格式：
- 每个线框图导出为 SVG 和 PNG
- 提供分层 PowerPoint 预览
- 模拟 Figma 卡片布局
- 关键UI元素包含标签、输入规则和评分计算逻辑

确保UI元素布局和功能逻辑的详细注释。
```

---

### 2.3 移动端App UX设计简报

**出处**：[DocsBot](https://docsbot.ai/prompts/writing/mobile-app-ux-brief)（免费）  
**适用模型**：ChatGPT / Gemini / Claude  
**难度**：中级

```
为一个计划在48小时内完成的移动App项目提供全面的UX设计简报。简报应清晰概述：

### 需要涵盖的步骤：
1. **定义目标**：明确App旨在解决的问题和主要目标
2. **识别目标受众**：描述用户的人口统计和心理特征
3. **关键功能**：列出App必须包含的核心功能
4. **设计考虑**：记录任何品牌指南、配色方案和设计原则
5. **时间线**：讨论48小时时间线及任务优先级安排
6. **交付物**：明确最终输出（线框图、原型、用户流程图等）
7. **用户痛点**：分析用户可能面临的问题及App如何解决
8. **用户流程**：描述App内的关键导航路径

### 输出格式
设计简报应分为清晰标注的章节，便于阅读。列表处使用要点符号，确保信息逻辑流畅。
```

---

### 2.4 Promptframes（提示词框架）— 将线框图与AI结合

**出处**：[NNGroup](https://www.nngroup.com/articles/promptframes/)  
**适用模型**：ChatGPT / Claude  
**难度**：中级

```
将以下线框图描述转化为"Promptframe"——结合线框图布局和AI提示词的新方法：

## 屏幕：[屏幕名称，如：产品详情页]
## 应用类型：[iOS/Android电商App]

### 布局结构：
- 顶部区域：[导航栏描述]
- 主要内容区：[主要内容描述]
- 交互区域：[按钮/表单描述]
- 底部区域：[标签栏描述]

### 内容目标（Content Goals）：
为每个内容区域编写AI生成提示词，要求：
1. 标题文案：用一句话传达 [核心价值主张]，字数控制在 [X] 字以内
2. 描述文案：强调 [关键特性]，语调 [专业/亲切/简洁]
3. CTA按钮：激发 [购买/注册/探索] 的行动意愿

### 数据约束：
- 产品名称不超过30个字符
- 价格显示格式：¥XX.XX
- 评分显示：星级 + 评价数

请为这个Promptframe生成实际的内容示例（替换Lorem ipsum），
使其在可用性测试中提供更真实的用户反馈。
```

---

## 3. UI设计系统

### 3.1 完整设计系统生成器

**出处**：[GitHub - claude-code-ui-agents](https://github.com/mustafakendiguzel/claude-code-ui-agents) / prompts/ui-design  
**适用模型**：Claude / ChatGPT  
**难度**：高级

```
我需要你为我的项目创建一套完整的设计系统：

品牌背景：
- 品牌名称：[BRAND_NAME]
- 行业：[INDUSTRY_TYPE]
- 品牌个性：[描述品牌特质，如：专业、现代、值得信赖]
- 目标受众：[描述目标用户]

设计系统组件：

1. 颜色系统：
   - 主色调（如有偏好请提供Hex值）
   - 辅助色/强调色
   - 中性灰色阶
   - 语义颜色（成功/警告/错误/信息）
   - 亮色/暗色模式变体

2. 排版系统：
   - 字体推荐（Web安全字体+回退方案）
   - 字号阶梯（H1-H6、正文、说明文字）
   - 行高和间距
   - 可用字重

3. 间距系统：
   - 基础单位系统（4px / 8px 网格）
   - Margin/Padding 阶梯
   - 布局间距指南

4. 组件规范：
   - 按钮变体（主要/次要/幽灵/禁用状态）
   - 表单元素（输入框、选择器、复选框、单选按钮）
   - 卡片和容器
   - 导航元素

5. 无障碍指南：
   - 颜色对比度要求
   - 焦点指示器
   - 最小文字尺寸

输出格式：
1. 设计令牌（JSON / CSS自定义属性）
2. CSS工具类
3. 组件文档+示例
4. 使用指南（Do's & Don'ts）
5. 开发者实现指南
```

---

### 3.2 基于截图反推设计系统

**出处**：[DocsBot](https://docsbot.ai/prompts/technical/ui-design-system-creation)（免费）  
**适用模型**：ChatGPT-4V / Claude（支持图像输入）  
**难度**：中级

```
基于提供的图像创建UI设计系统。

### 步骤：
1. **分析图像**：全面检查图像的结构、元素、颜色、排版和布局
2. **定义调色板**：识别主色、辅助色和中性色
3. **排版分析**：分析字体和文本样式，定义字体族、大小、字重和文本层级
4. **组件识别**：列出图像中可见的所有UI组件（按钮、输入框、导航栏等）
5. **设计模式**：确定布局或流程中使用的设计模式
6. **创建风格指南**：将以上所有元素记录到基础风格指南中

### 输出格式
提供每个识别元素（颜色、排版、组件）的详细描述。包含Hex色值和CSS代码片段。

### 示例
- **调色板**：
  - 主色：#FFFFFF（白色）
  - 辅助色：#000000（黑色）
  - 强调色：#FF5733（橙色）

- **排版示例**：
  body { font-family: 'Roboto', sans-serif; font-size: 16px; }
  h1 { font-size: 32px; font-weight: 700; }
```

---

### 3.3 配色方案推荐

**出处**：[Interaction Design Foundation](https://www.interaction-design.org/literature/article/chat-gpt-for-ux-design)  
**适用模型**：ChatGPT / Claude  
**难度**：初级

```
为一款 [App类型，如：健康与养生App] 推荐合适的配色方案。
考虑以下因素：
- 用户情绪：App应传达什么情感？（如：平静、信任、活力）
- 可信度：配色如何增强用户对App的信任感？
- 可读性：文本与背景的对比度是否足够？
- 品牌一致性：与品牌标识的协调性
- 文化因素：目标市场的颜色文化含义

请提供：
1. 主色调及其心理学含义
2. 完整的色板（主色、辅色、强调色、中性色，各含Hex值）
3. 亮色模式和暗色模式的配色方案
4. WCAG AA/AAA对比度合规性验证
5. 在不同UI元素中的应用示例
```

---

## 4. 移动端UI设计哲学

### 4.1 Apple级移动端设计哲学（全面指南）

**出处**：[GitHub - claude-code-ui-agents](https://github.com/mustafakendiguzel/claude-code-ui-agents) / prompts/ui-design/mobile-design-philosophy  
**适用模型**：Claude / ChatGPT  
**难度**：高级  
**⭐ 强烈推荐 — 这是最全面的移动端UI设计提示词之一**

```
我需要你创建一套移动端设计系统和实施指南，遵循Apple级设计美学和现代移动UX原则：

项目背景：
- 应用类型：[iOS App / Android App / PWA / 响应式Web]
- 行业：[指定行业背景]
- 目标受众：[人口统计和技术水平]
- 品牌个性：[专业 / 活泼 / 高端 / 平易近人]

设计决策框架：
对每个设计元素，思考：
1. 目的：这个元素为什么存在？
2. 层级：在信息架构中有多重要？
3. 上下文：与周围元素的关系？
4. 无障碍：所有用户都能有效交互吗？
5. 性能：是否影响加载或交互速度？

Apple级设计美学：
- 对每个元素精益求精的细节关注
- 感觉自然的直觉式用户体验
- 干净、精致的视觉呈现
- 全局一致的间距和对齐
- 通过精心的微交互传达高端感
- 像素级完美的对齐和间距
- 每个用户操作都有细腻但有意义的反馈

触控界面设计：
- 最小触摸目标：44×44px（iOS）/ 48×48px（Android）
- 触摸目标间距：最少8px
- 拇指可达区域：将主要操作放在易触达区域
- 手势冲突：避免竞争手势（滑动 vs 滚动）
- 触觉反馈：仅在重要确认时使用
- 触摸反馈：100ms内提供视觉响应

移动端导航模式：
- 底部标签栏：最多5个标签
- 底部弹出面板（Bottom Sheet）
- 浮动操作按钮（FAB）
- 下拉刷新
- 滑动操作（删除/归档/分享）

移动端排版：
- 最小正文字号：16px（防止iOS自动缩放）
- 行高：正文1.4-1.6，标题1.1-1.3
- 每行字符数：45-75个（最优可读性）
- 字重层级：最多3种以保持一致性

移动端颜色系统：
- 主色梯度（6-9个色阶）+ 无障碍合规
- 语义颜色（成功/警告/错误/信息）
- 暗色模式所有颜色变体
- 高对比模式支持
- 颜色独立性（永不仅依赖颜色传达信息）

性能优化：
- 关键渲染路径：内联关键CSS，延迟非关键资源
- 图像优化：WebP格式，响应式图片，懒加载
- 动画性能：使用transform和opacity，避免布局属性
- 60fps动画：硬件加速 + will-change属性

无障碍标准：
- WCAG AA合规：最低4.5:1对比度
- 触控无障碍：足够大的目标+清晰的焦点指示器
- 屏幕阅读器支持：语义化标记 + ARIA标签
- 运动障碍：无时间限制 + 替代输入方式
- 认知负荷：简洁语言 + 清晰指引 + 错误预防

输出要求：
1. 完整的移动端设计系统（颜色令牌+排版阶梯）
2. 触控界面指南和交互模式
3. 针对移动端优化的组件库
4. 性能优化的动画库
5. 无障碍检查清单和实施指南
6. 平台特定考虑（iOS vs Android vs Web）
7. 移动端体验测试方法论
```

---

### 4.2 Material Design 3 / iOS HIG 设计规范提示词

**出处**：综合 [Material Design 3](https://m3.material.io/) + [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/)  
**适用模型**：ChatGPT / Claude  
**难度**：中级

```
请作为高级UI设计师，为我的 [App类型] 创建符合平台规范的设计指南：

## 如果是 Android App（Material Design 3）：
1. **动态颜色（Dynamic Color）**：基于用户壁纸生成个性化配色方案
   - 定义 Primary / Secondary / Tertiary 色调表面
   - 提供 TonalPalette 的完整色阶（0-100）
2. **Material You 组件**：
   - NavigationBar（底部导航）
   - TopAppBar（大/中/小变体）
   - FAB / ExtendedFAB
   - Card（Filled / Elevated / Outlined）
   - 列表项（1行 / 2行 / 3行）
3. **形状系统**：
   - 圆角半径阶梯（ExtraSmall → Full）
   - 各组件的默认形状映射
4. **排版系统**：使用 TypeScale（Display / Headline / Title / Body / Label）

## 如果是 iOS App（Human Interface Guidelines）：
1. **系统颜色**：
   - 使用 iOS 语义颜色（systemBlue, label, secondaryLabel等）
   - 支持 Light / Dark / Tinted 模式
2. **SF Symbols**：定义图标使用规范和权重
3. **组件规范**：
   - TabBar / NavigationBar / Toolbar
   - Sheet / Alert / ActionSheet
   - List / Form / DisclosureGroup
4. **Safe Area / Dynamic Island 适配**
5. **SwiftUI 设计模式**：
   - ViewModifier 设计令牌
   - Environment 颜色方案

输出要求：
- 设计令牌表（JSON格式）
- 组件使用规范文档
- 暗色模式完整适配方案
- 可直接用于 Jetpack Compose / SwiftUI 的代码示例
```

---

## 5. 界面概念设计与生成

### 5.1 移动端App UI概念设计

**出处**：[DocsBot](https://docsbot.ai/prompts/creative/mobile-app-ui-design-1)（免费）  
**适用模型**：ChatGPT / Gemini / Claude  
**难度**：初级

```
为一款移动应用创建用户界面（UI）设计概念。

设计应优先考虑可用性和美学，确保直观的布局和吸引人的视觉风格。
包含以下细节：
- 配色方案
- 排版选择
- 按钮样式
- 整体布局结构

在设计中考虑无障碍性和用户体验最佳实践。
```

---

### 5.2 iOS App Mockup 生成

**出处**：[DocsBot](https://docsbot.ai/prompts/productivity/ios-mobile-app-mockup)（免费）  
**适用模型**：ChatGPT / Gemini / Claude  
**难度**：中级

```
创建一个为iOS设备设计的移动App详细Mockup。

注重直觉式用户界面设计，恰当使用iOS设计指南，布局适合手机屏幕。

步骤：
1. 确定App的主要目的和功能
2. 绘制关键屏幕，包括主屏幕、导航和重要交互屏幕
3. 使用iOS设计元素：标签栏、导航栏、按钮和图标，保持iOS风格一致性
4. 确保可用性功能：无障碍和响应式设计

输出格式：
以结构化格式提供Mockup描述，列出每个屏幕及其组件和布局的详细说明。
可选附加视觉风格、颜色和交互的文字描述。

示例：
屏幕：主屏幕
- 顶部：带App名称的标题栏
- 中部：带图片和简短描述的可滚动列表
- 底部：包含首页、搜索、个人资料图标的标签栏
```

---

### 5.3 移动端App UI代码生成（HTML/Tailwind）

**出处**：[DocsBot](https://docsbot.ai/prompts/creative/ui-generation-for-mobile-app)（免费）  
**适用模型**：ChatGPT / Claude  
**难度**：中级

```
使用HTML、CSS、JavaScript和Tailwind CSS生成一个现代、优雅、专业的移动App UI。

布局应包含以下组件：

1. **导航栏**：
   - 最左侧：返回箭头图标
   - 居中：水平对齐文本"订单详情"

2. **主体区域**：
   - 订单编号：135sdv5
   - 客户：Abc公司
   - 联系方式：7894651230
   - 计划日期：[日期]
   - 取件时间：[日期时间]
   - 状态：已完成

3. **附件列表**：显示附件名称，右侧有"下载"按钮

4. **配色方案**：主要使用 #dc3545 作为强调色

5. **底部导航栏**：四个图标代表App的不同功能

确保整个UI响应式、视觉吸引力强、用户友好，遵循现代设计原则。
```

---

## 6. 无障碍设计（Accessibility）

### 6.1 WCAG无障碍审计提示词

**出处**：[AI Unpacker](https://aiunpacker.com/prompts/accessibility-audit-checklist-ai-prompts-for-ux-designers/) + [AIForPro](https://aiforpro.net/accessibility-guidelines-prompts/)  
**适用模型**：ChatGPT / Claude  
**难度**：中级

```
请对我的 [App名称/类型] 进行全面的WCAG 2.1 AA无障碍审计，使用POUR框架组织：

### P — 可感知（Perceivable）
- [ ] 所有图像和图标是否有替代文本（alt text）？
- [ ] 视频内容是否提供字幕/音频描述？
- [ ] 文本与背景的对比度是否达到4.5:1（正文）/ 3:1（大文本）？
- [ ] 信息传达是否不仅仅依赖颜色？
- [ ] 内容是否支持200%缩放且不丢失功能？

### O — 可操作（Operable）
- [ ] 所有交互元素是否可通过键盘访问？
- [ ] 焦点指示器是否清晰可见？
- [ ] 触摸目标是否达到最小尺寸（iOS: 44×44pt / Android: 48×48dp）？
- [ ] 是否避免了仅靠手势才能完成的操作？
- [ ] 是否有跳过重复导航的机制？

### U — 可理解（Understandable）
- [ ] 表单是否有清晰的标签和错误提示？
- [ ] 操作结果是否可预测？
- [ ] 错误消息是否提供具体的修复建议？
- [ ] 语言是否简洁易懂？

### R — 健壮（Robust）
- [ ] 是否使用语义化HTML/原生组件？
- [ ] ARIA角色和属性是否正确使用？
- [ ] 在不同辅助技术（VoiceOver / TalkBack）中是否正常工作？

输出格式：
1. 每项检查的通过/失败/不适用状态
2. 失败项的具体截图位置描述
3. 每项失败的修复建议和优先级（高/中/低）
4. 整体无障碍评分（0-100）
```

---

### 6.2 ARIA实现专家提示词

**出处**：[GitHub - claude-code-ui-agents](https://github.com/mustafakendiguzel/claude-code-ui-agents) / prompts/accessibility  
**适用模型**：Claude / ChatGPT  
**难度**：高级

```
你是一位ARIA实现专家，专注于复杂UI组件的WCAG合规无障碍设计。

请为以下移动端UI组件提供完整的ARIA实现方案：

1. **自定义下拉选择器（Custom Dropdown/Select）**
   - role="combobox" 的完整ARIA属性
   - 键盘交互模式（上下箭头、Enter、Escape）
   - 屏幕阅读器的通知方式

2. **底部弹出面板（Bottom Sheet / Modal）**
   - 焦点陷阱（Focus Trap）实现
   - aria-modal="true" 的正确使用
   - 关闭时焦点恢复策略

3. **可滑动卡片列表（Swipeable Card List）**
   - 滑动操作的键盘替代方案
   - aria-live区域通知状态变化
   - 删除确认的无障碍交互

4. **标签栏导航（Tab Bar Navigation）**
   - role="tablist" / "tab" / "tabpanel" 映射
   - aria-selected 状态管理
   - 键盘导航（左右箭头切换）

5. **Toast通知 / Snackbar**
   - aria-live="polite" vs "assertive" 使用场景
   - 自动消失通知的屏幕阅读器处理
   - 包含操作按钮时的焦点管理

每个组件请提供：
- HTML/JSX 代码示例
- 对应的 SwiftUI（iOS）或 Jetpack Compose（Android）实现说明
- VoiceOver / TalkBack 测试脚本
- 常见错误及避免方法
```

---

## 7. 设计交付与代码转换

### 7.1 Figma → Jetpack Compose 代码生成

**出处**：[Google AI Studio 指南](https://medium.com/@ahmetbostanciklioglu) + [Builder.io](https://builder.io/blog/convert-figma-to-jetpack-compose)  
**适用模型**：Gemini / ChatGPT-4V / Claude（支持图像输入）  
**难度**：中级

```
作为Android开发专家，根据提供的Figma设计截图，使用Jetpack Compose构建界面，
使Compose Preview尽可能接近原始设计。

要求：
1. 包含完整的 import 语句
2. 使用 Material 3 组件和主题
3. 遵循以下结构：
   - @Composable 函数命名使用 PascalCase
   - 使用 Modifier 链式调用控制布局
   - 颜色使用 MaterialTheme.colorScheme
   - 间距使用一致的 dp 值

4. 布局规范：
   - 标注精确的尺寸（宽度、高度、间距）
   - 颜色值使用Hex
   - 字体大小使用 sp
   - 圆角使用 RoundedCornerShape

5. 响应式处理：
   - 使用 BoxWithConstraints 适配不同屏幕
   - 正确处理 Safe Area / Cutout

6. 提供 @Preview 注解以便预览

请同时生成对应的 ViewModel 数据模型（如需要）。
```

---

### 7.2 Figma → SwiftUI 代码生成

**出处**：[PragmaticCoders](https://www.pragmaticcoders.com/blog/ai-ui-prototyping-for-android-and-ios)  
**适用模型**：ChatGPT-4V / Claude（支持图像输入）  
**难度**：中级

```
作为iOS开发专家，根据提供的Figma设计截图，使用SwiftUI构建界面。

要求：
1. 使用最新的 SwiftUI API（iOS 17+）
2. 遵循以下规范：
   - 使用 VStack / HStack / ZStack 组合布局
   - 颜色使用 Color.accentColor 或自定义 Color Extension
   - 字体使用 .font(.system(size:weight:design:))
   - 间距使用 .padding() 和 Spacer()

3. 组件设计：
   - 将可复用部分提取为独立 View
   - 使用 @State / @Binding / @ObservedObject 管理状态
   - 支持 Light / Dark 模式
   - 适配 Dynamic Type（可变字体大小）

4. 无障碍：
   - 添加 .accessibilityLabel() 和 .accessibilityHint()
   - 为图像添加 .accessibilityElement()

5. 动画：
   - 使用 .animation(.spring()) 为过渡添加动效
   - 标注关键动画时长和曲线

请提供完整的 Swift 文件代码，包含 #Preview 宏。
```

---

### 7.3 设计交付规范文档生成

**出处**：综合 [Figma Dev Mode](https://help.figma.com/hc/en-us/articles/23920389749655) 最佳实践  
**适用模型**：ChatGPT / Claude  
**难度**：中级

```
为以下UI设计稿创建完整的开发交付规范文档：

## 需要记录的内容：

### 1. 视觉规范
- 每个元素的精确尺寸（宽×高，单位：px/dp/pt）
- 间距和边距（元素间距、容器内边距）
- 颜色值（Hex + RGBA + 设计令牌名称）
- 字体规范（字体族、字号、字重、行高、字间距）
- 阴影（X偏移、Y偏移、模糊半径、颜色、透明度）
- 圆角（各角半径值）

### 2. 交互规范
- 按钮状态（默认/悬停/按下/禁用/加载中）
- 输入框状态（空/聚焦/填充/错误/成功）
- 过渡动画（类型、持续时间、缓动函数）
- 手势交互（点击/长按/滑动/拖拽及其反馈）

### 3. 响应式断点
- iPhone SE / iPhone 15 / iPhone 15 Pro Max
- Android Small (360dp) / Medium (411dp) / Large (600dp+)
- 横屏适配方案

### 4. 资源清单
- 图标列表（名称、尺寸、格式、@1x/@2x/@3x）
- 图片资源（尺寸、压缩格式、CDN路径）
- Lottie动画文件

输出格式：Markdown表格 + JSON设计令牌
```

---

## 8. 应用商店视觉优化（ASO）

### 8.1 Midjourney App图标设计提示词

**出处**：[AppAgent](https://appagent.com/blog/how-to-prompt-midjourney-to-develop-stunning-app-icons/)  
**适用模型**：Midjourney / DALL-E 3 / Stable Diffusion  
**难度**：中级

```
## Midjourney App图标提示词公式：

[主体描述], [风格], [配色], app icon, [附加修饰符] --ar 1:1 --v 6

### 示例提示词集：

#### 健身App图标：
a minimalist flame icon, gradient from orange to red, 
modern flat design, rounded square app icon, 
clean vector style, slight 3D depth --ar 1:1 --v 6

#### 冥想App图标：
a serene lotus flower, soft purple to blue gradient,
zen-inspired minimalist design, rounded square app icon,
clean lines, no text --ar 1:1 --v 6

#### 金融App图标：
an abstract upward arrow made of stacked coins,
green and gold color scheme, modern 3D render,
rounded square app icon, professional look --ar 1:1 --v 6

### 设计要点（来自AppAgent最佳实践）：
1. 简洁性：远距离和小尺寸下仍可辨识
2. 独特性：与竞品图标区分开
3. 一致性：与App内部视觉风格协调
4. A/B测试：准备3-5个变体进行转化率测试

### 后期处理建议：
- 在Figma中调整为精确的圆角矩形
- 导出 1024×1024 母版尺寸
- 验证在浅色/深色背景上的可见性
- 检查在小尺寸（29×29pt）下的清晰度
```

---

### 8.2 应用商店截图设计提示词

**出处**：[ASO.dev](https://aso.dev/figma/) + 最佳实践综合  
**适用模型**：ChatGPT / Claude  
**难度**：中级

```
为我的 [App名称] 设计一套应用商店截图方案（适用于App Store和Google Play）：

### 截图策略：
1. **第一张截图**（最关键）：
   - 传达App的核心价值主张
   - 使用大标题文案（不超过30个字符）
   - 展示App最吸引人的界面

2. **截图序列规划**（总共5-8张）：
   - 截图1：核心价值 / Hero Shot
   - 截图2：主要功能展示
   - 截图3：独特差异化功能
   - 截图4：社交证明（评分/获奖/用户数）
   - 截图5：次要功能/设置
   - 截图6-8：更多功能 / 使用场景

3. **每张截图的设计规范**：
   - 文案：简短有力的标题（问题→解决方案框架）
   - 设备帧：是否使用设备Mockup（趋势：减少设备帧，更多全幅设计）
   - 背景：纯色/渐变/场景化
   - 注释/箭头：指向关键功能的标注

4. **尺寸适配**：
   - iPhone 6.7" (1290×2796px)
   - iPhone 6.5" (1242×2688px)
   - iPad 12.9" (2048×2732px)
   - Google Play (1080×1920px 推荐)

5. **本地化考虑**：
   - 文案翻译工作流
   - 截图自动化更新机制
   - 不同市场的文化适配

请为每张截图提供：标题文案、视觉描述、设计要点。
```

---

## 9. 微交互与动效设计

### 9.1 微交互设计专家提示词

**出处**：[GitHub - claude-code-ui-agents](https://github.com/mustafakendiguzel/claude-code-ui-agents) / prompts/animation  
**适用模型**：Claude / ChatGPT  
**难度**：高级

```
你是一位微交互设计专家，专注于性能优化的UI动画。

请为以下移动端App场景设计微交互方案：

### 1. 点赞/收藏动画
- 触发方式：单击 / 双击
- 动画描述（关键帧、时长、缓动曲线）
- 触觉反馈类型（iOS: UIImpactFeedbackGenerator / Android: HapticFeedback）
- 性能要求：60fps，使用硬件加速属性

### 2. 下拉刷新
- 拉动阶段：弹性阻尼效果
- 触发阈值：75dp
- 加载指示器：自定义 vs 系统默认
- 成功/失败状态的不同反馈

### 3. 页面转场
- 共享元素过渡（Shared Element Transition）
- Hero动画参数（duration、interpolator）
- 手势驱动的交互式转场（interruptible）

### 4. 骨架屏（Skeleton Loading）
- 闪烁动画（shimmer effect）实现
- 占位符形状与实际内容的匹配
- 从骨架到实际内容的过渡时机

### 5. 按钮交互
- 按下缩放效果（scale: 0.95 → 1.0）
- Ripple效果（Android Material）
- 加载状态转换（文字→spinner→成功✓）

每个微交互请提供：
- 动画参数（duration、delay、easing curve）
- Lottie JSON 描述或 CSS/Compose/SwiftUI 代码
- 触觉反馈配对方案
- 性能优化注意事项
- 无障碍降级方案（prefers-reduced-motion）
```

---

### 9.2 手势交互设计提示词

**出处**：综合 Apple HIG + Material Design 手势指南  
**适用模型**：ChatGPT / Claude  
**难度**：中级

```
为我的 [App类型] 设计完整的手势交互系统：

### 基础手势映射：
| 手势 | 操作 | 反馈 | 冲突处理 |
|------|------|------|----------|
| 单击 | ? | ? | ? |
| 双击 | ? | ? | ? |
| 长按 | ? | ? | ? |
| 左滑 | ? | ? | ? |
| 右滑 | ? | ? | ? |
| 捏合 | ? | ? | ? |
| 拖拽 | ? | ? | ? |

### 需要考虑的方面：
1. **手势发现性**：用户如何知道可以滑动？（引导提示/边缘暗示）
2. **手势冲突**：滑动操作与页面滚动如何区分？
3. **撤销机制**：误操作后如何恢复？（如：邮件滑动删除→Undo）
4. **无障碍替代**：每个手势操作都必须有非手势替代方案
5. **跨平台差异**：
   - iOS：从左边缘右滑 = 返回（系统级）
   - Android：返回按钮/手势导航

### 输出：
- 完整的手势映射表
- 每个手势的动画规范
- 手势引导设计方案（首次使用引导）
- 冲突解决策略
```

---

## 10. 可用性测试与设计评审

### 10.1 启发式评估（Nielsen's 10 Heuristics）

**出处**：[Medium - Nielsen's Heuristics](https://medium.com/design-bootcamp/leveraging-nielsens-10-heuristics-for-enhanced-ai-user-experience) + 综合  
**适用模型**：ChatGPT-4V / Claude（支持截图分析）  
**难度**：中级

```
请基于 Jakob Nielsen 的10条可用性启发原则，对我的 [App名称] 界面进行评估：

### 评估维度：

1. **系统状态可见性**
   - 用户是否随时知道正在发生什么？
   - 加载状态、进度指示器是否清晰？

2. **系统与真实世界匹配**
   - 语言是否使用用户熟悉的词汇？
   - 图标含义是否直观？

3. **用户控制和自由**
   - 是否有清晰的"撤销"和"退出"选项？
   - 返回导航是否一致？

4. **一致性和标准**
   - 相同操作在不同屏幕是否表现一致？
   - 是否遵循平台规范（iOS HIG / Material Design）？

5. **错误预防**
   - 高风险操作是否有确认步骤？
   - 表单是否有实时验证？

6. **识别而非回忆**
   - 选项和操作是否可见？
   - 是否减少了用户的记忆负担？

7. **灵活性和效率**
   - 是否为高级用户提供快捷方式？
   - 是否支持个性化/自定义？

8. **美学和极简设计**
   - 每个元素是否都有存在的必要？
   - 视觉噪音是否最小化？

9. **帮助用户识别、诊断和恢复错误**
   - 错误消息是否用普通语言说明问题？
   - 是否提供具体的解决建议？

10. **帮助和文档**
    - 是否提供上下文帮助？
    - 帮助信息是否易于搜索和理解？

### 输出格式：
每条原则评分（1-5分），附具体问题描述和改善建议。
计算总体可用性得分和优先改善清单。
```

---

### 10.2 线框图改进分析

**出处**：[Interaction Design Foundation](https://www.interaction-design.org/literature/article/chat-gpt-for-ux-design)  
**适用模型**：ChatGPT-4V / Claude（需配合截图使用）  
**难度**：中级

```
分析这个移动端旅行预订App的线框图，并建议改进方案以实现更流畅的用户流程。

重点关注以下元素：
- **菜单位置**：是否符合拇指热区？建议最佳位置
- **按钮尺寸**：是否满足最小触摸目标？是否足够醒目？
- **表单字段排列**：顺序是否逻辑？是否可以减少字段数量？
- **信息层级**：最重要的信息是否最先被看到？
- **导航深度**：到达核心功能需要几次点击？是否可以减少？

请基于设计最佳实践提供具体的、可操作的建议。
每项建议包含：
1. 当前问题描述
2. 改进方案
3. 预期对用户体验的影响
4. 实施难度（高/中/低）
```

---

### 10.3 设计评审检查清单

**出处**：综合 [NNGroup](https://www.nngroup.com/) + 最佳实践  
**适用模型**：ChatGPT / Claude  
**难度**：中级

```
为我的移动端App设计进行全面评审，使用以下检查清单：

## 视觉设计检查
- [ ] 颜色使用是否一致？是否符合品牌规范？
- [ ] 排版层级是否清晰（标题/副标题/正文/说明文字）？
- [ ] 间距系统是否统一（8px网格）？
- [ ] 图标风格是否一致（线条粗细、圆角、填充）？
- [ ] 暗色模式是否完整适配？

## 交互设计检查
- [ ] 所有可点击元素是否有明确的可交互暗示？
- [ ] 操作反馈是否即时（<100ms视觉反馈）？
- [ ] 加载状态是否有骨架屏或进度指示？
- [ ] 错误状态是否有清晰的恢复路径？
- [ ] 空状态是否提供引导操作？

## 信息架构检查
- [ ] 导航结构是否扁平（≤3层深度）？
- [ ] 标签文案是否清晰易懂？
- [ ] 搜索功能是否易于发现和使用？
- [ ] 关键操作是否可在3次点击内完成？

## 平台一致性检查
- [ ] iOS：是否遵循 Human Interface Guidelines？
- [ ] Android：是否遵循 Material Design 3？
- [ ] 返回导航是否符合平台规范？
- [ ] 系统字体和原生组件是否正确使用？

## 性能感知检查
- [ ] 列表滚动是否流畅（60fps）？
- [ ] 图片是否有占位符和渐进式加载？
- [ ] 动画是否使用硬件加速？
- [ ] 首屏内容加载时间是否<2秒？

输出：每项检查的通过/失败状态 + 改进建议 + 优先级排序
```

---

## 📊 快速选择指南

| 你需要做什么？ | 推荐使用的提示词 | 推荐AI模型 |
|--------------|----------------|-----------|
| 创建用户画像 | 1.1 用户画像创建 | ChatGPT / Claude |
| 规划用户旅程 | 1.3 用户旅程地图 | ChatGPT / Claude |
| 快速线框图 | 2.1 线框图GPT提示词集 | ChatGPT |
| 建立设计系统 | 3.1 设计系统生成器 | Claude / ChatGPT |
| iOS/Android设计规范 | 4.1 移动端设计哲学 ⭐ | Claude |
| 从截图反推设计系统 | 3.2 基于截图反推 | ChatGPT-4V / Claude |
| 生成界面Mockup | 5.2 iOS App Mockup | ChatGPT / Gemini |
| 无障碍审计 | 6.1 WCAG审计 | ChatGPT / Claude |
| Figma→代码 | 7.1（Android）/ 7.2（iOS） | Gemini / ChatGPT-4V |
| 设计App图标 | 8.1 Midjourney提示词 | Midjourney / DALL-E 3 |
| 动效设计 | 9.1 微交互专家 | Claude / ChatGPT |
| 可用性评估 | 10.1 启发式评估 | ChatGPT-4V / Claude |

---

## 📚 完整来源索引

| 来源 | 类型 | 链接 |
|------|------|------|
| DocsBot | 免费提示词库 | [docsbot.ai/prompts](https://docsbot.ai/prompts) |
| GitHub claude-code-ui-agents | 开源提示词集 | [github.com/mustafakendiguzel/claude-code-ui-agents](https://github.com/mustafakendiguzel/claude-code-ui-agents) |
| Interaction Design Foundation | UX设计教育 | [interaction-design.org](https://www.interaction-design.org/literature/article/chat-gpt-for-ux-design) |
| ProCreator Design | 线框图GPT指南 | [procreator.design/blog](https://procreator.design/blog/guide-to-mobile-app-wireframe-gpt-prompts/) |
| NNGroup | UX研究权威 | [nngroup.com](https://www.nngroup.com/articles/promptframes/) |
| UXPressia | 用户旅程工具 | [uxpressia.com](https://uxpressia.com/blog/ai-journey-mapping-chatgpt) |
| AppAgent | ASO优化 | [appagent.com](https://appagent.com/blog/how-to-prompt-midjourney-to-develop-stunning-app-icons/) |
| ASO.dev | 应用商店优化 | [aso.dev/figma](https://aso.dev/figma/) |
| AI Unpacker | 无障碍审计提示词 | [aiunpacker.com](https://aiunpacker.com/prompts/accessibility-audit-checklist-ai-prompts-for-ux-designers/) |
| Material Design 3 | Google设计系统 | [m3.material.io](https://m3.material.io/) |
| Apple HIG | Apple设计指南 | [developer.apple.com/design](https://developer.apple.com/design/human-interface-guidelines/) |
| Motiff Help | AI生成UI指南 | [motiff.com](https://www.motiff.com/help/docs/articles/341351705918724) |
| PragmaticCoders | AI原型设计 | [pragmaticcoders.com](https://www.pragmaticcoders.com/blog/ai-ui-prototyping-for-android-and-ios) |

---

> **使用建议**：  
> 1. 所有提示词中的 `[方括号内容]` 需替换为你的实际项目信息  
> 2. 标注 ⭐ 的提示词为全面程度最高的推荐项  
> 3. 涉及截图分析的提示词需要使用支持图像输入的模型（GPT-4V、Claude 3.5+、Gemini）  
> 4. 建议按照：**用户研究(1)→线框图(2)→设计系统(3-4)→界面设计(5)→无障碍(6)→交付(7)→ASO(8)** 的顺序使用
