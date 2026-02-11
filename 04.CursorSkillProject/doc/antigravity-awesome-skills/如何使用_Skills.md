# 如何使用 Cursor Skills（以 i18n-localization 为例）

下面以 **i18n-localization** 为例，说明在 Cursor 里使用任意一个 Skill 的通用步骤。

---

## 一、让 Cursor 能加载到 Skills

Cursor 只会从**固定目录**里读取 Skills。你需要先把技能放到那个目录里，有两种常见做法。

### 方式 A：用官方安装器（推荐）

在终端执行（会克隆整库到 Cursor 的 skills 目录）：

```bash
npx antigravity-awesome-skills --cursor
```

若报 404，可改用：

```bash
npx github:sickn33/antigravity-awesome-skills --cursor
```

安装完成后，所有技能（包含 `i18n-localization`）会在 Cursor 使用的目录里，无需再拷贝。

### 方式 B：手动链接或拷贝本项目的 skills

你当前项目里技能在：

- 路径：`<项目根>/skills/skills/`
- 例如 i18n-localization：`skills/skills/i18n-localization/`

Cursor 的 Skills 目录一般是：

- **macOS/Linux**：`~/.cursor/skills/` 或工作区下的 `.cursor/skills/`
- **Windows**：`%USERPROFILE%\.cursor\skills\`

操作示例（在项目根目录执行）：

```bash
# 若 Cursor 使用 ~/.cursor/skills，可把本仓库的 skills 子目录链过去
mkdir -p ~/.cursor/skills
# 只链单个技能（软链接）
ln -sf "$(pwd)/skills/skills/i18n-localization" ~/.cursor/skills/i18n-localization

# 或整库链过去（所有技能都可用）
ln -sf "$(pwd)/skills/skills" ~/.cursor/skills/antigravity-skills
```

（Windows 下可用「创建符号链接」或直接复制 `i18n-localization` 文件夹到 `%USERPROFILE%\.cursor\skills\`。）

---

## 二、在 Cursor 里使用 i18n-localization

### 1. 在对话中 @ 引用

1. 打开 Cursor 的 **Chat**（和 AI 对话的输入框）。
2. 输入 **`@`**，会弹出可选的技能/文件列表。
3. 输入 **`i18n`** 或 **`i18n-localization`**，选中 **i18n-localization**（或列表里显示的该技能名称）。
4. 然后输入你的问题或任务。

### 2. 示例提问（可直接复制使用）

- **“请用 @i18n-localization 帮我在当前项目里找出所有硬编码的界面文案，并给出改成 i18n 的建议。”**
- **“用 i18n-localization 技能：我们准备支持中英文，请按最佳实践设计 locales 目录结构和 key 的命名规范。”**
- **“参考 @i18n-localization：这段 React 代码里有哪些字符串应该抽成翻译 key？请改写成 react-i18next 的用法。”**
- **“我们要支持阿拉伯语 RTL，请按 i18n-localization 的规范给一份实现清单和注意事项。”**

只要在同一条消息里 **@ 了 i18n-localization**，Cursor 就会加载该技能的 `SKILL.md` 内容，按里面的 i18n/L10n 规范来回答和改代码。

---

## 三、i18n-localization 技能本身能做什么

该技能主要提供：

- **概念**：i18n、L10n、Locale、RTL 等含义。
- **何时做 i18n**：按项目类型（公开 Web、SaaS、内部工具等）判断。
- **实现方式**：React（react-i18next）、Next.js（next-intl）、Python（gettext）等示例。
- **目录与文件**：`locales/` 结构、多语言 JSON 组织。
- **硬编码检测**：如何发现未抽成翻译的字符串。
- **RTL**：阿拉伯语等从右到左语言的支持要点。

所以你可以把「检测硬编码」「设计 key 和目录」「写 React/Next/Python 示例」「RTL 清单」等需求，都放在同一条 @i18n-localization 的提问里。

---

## 四、其它技能怎么用（通用）

对任意技能（例如 `mobile-developer`、`java-pro`）：

1. **确保已安装/链接**：用方式 A 或 B 让该技能出现在 Cursor 的 skills 目录中。
2. **在 Chat 里 @ 技能名**：输入 `@` 后选对应技能（如 `mobile-developer`）。
3. **在问题中说明任务**：例如“用 @mobile-developer 技能，帮我设计一个 Android 登录模块的架构”。

更多技能的中文说明见：`doc/00_分类索引.md` 及各 `skills_*.md`。
