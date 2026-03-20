# Android RTL / LTR 本地化适配指南

> 定位：面向 Android 工程师的 RTL 布局适配技术规范
> 范围：View 体系 + Jetpack Compose 双框架
> 版本：v6.2 · 2026-03-04
> 来源：[飞书文档](https://thundersoft.feishu.cn/docx/CbOEdzpOXo2ovKxtAznceN3Pnyg)

---

## 拿到就用：3 步搞定

**第 1 步** — 把下面（`RTL_LTR本地化适配指南.md`）文件放到你项目的 `.cursor/rules/` 目录下

**第 2 步** — 打开 Cursor IDE

**第 3 步** — 在对话框中输入以下任一指令，AI 会自动扫描你的代码并修复 RTL 问题：

| 场景 | 输入指令 |
|------|----------|
| 全项目扫描 | "帮我检查项目的 RTL 适配问题" |
| 扫描 XML | "扫描所有 XML 布局文件中的 Left/Right 属性" |
| 检查自定义 View | "检查自定义 View 是否正确处理了 RTL" |
| 修复指定页面 | "修复这个页面的 RTL 布局问题" |
| 适配某个 Fragment | "@DetailFragment.kt 帮我做 RTL 适配" |

> 不用 Cursor？也可以直接当技术文档阅读 — 往下看导读部分了解阅读顺序。

---

## 导读

| 阶段 | 时间 | 推荐章节 |
|------|------|----------|
| 快速了解 | 10 分钟 | 第一章 + 速查表 |
| 完整掌握 | 40 分钟 | 第一章至第七章 |
| 深度参考 | 按需 | 第八章至附录 |

---

## 速查表

- 检测 RTL → `resources.configuration.layoutDirection == LAYOUT_DIRECTION_RTL`
- XML 属性 → `Start / End` 代替 `Left / Right`
- 文字对齐 → `Gravity.START / END`
- 方向性图标 → `autoMirrored="true"` 或 `scaleX = -1f` 或 `rotationY`
- 非方向性图标 → 不翻转
- Drawable 代码 → `setCompoundDrawablesRelative()`
- 自定义控件 → `setText` 可能重置 gravity → 数据刷新后必须重新设置
- 自定义绘制 → Canvas 不自动翻转 → `onDraw` 需手动 scale
- 坐标系 → `getLeft/getRight/getX` 值不变 → 绘制和触摸需手动计算
- 时序安全 → `view?.post { applyRtlIfNeeded() }`
- Container scaleX → XML 必须设 `layoutDirection="ltr"`
- 浮窗/PIP → 绝对位置不翻转 → 需手动计算镜像坐标
- Compose 方向 → `CompositionLocalProvider(LocalLayoutDirection provides Rtl)`
- Compose 图标 → `Icons.AutoMirrored.Filled.ArrowBack`

---

## 一、核心概念

### 1.1 什么是 RTL

RTL（Right-to-Left）是 Android 对从右到左书写语言的 UI 适配机制。它不仅改变文字方向，而是对整个界面做水平镜像翻转。

### 1.2 镜像规则（Material Design 官方标准）

**需要镜像：** 布局位置、方向性图标、进度条方向、列表缩进、文字对齐方向、导航抽屉方向、返回按钮、撤销/重做

**不需要镜像：** 播放/暂停/停止、收藏/设置/搜索、品牌Logo/头像、数字/时钟、未翻译的LTR文本、图表/数据可视化、相机/话筒等实物图标、对号/加号/减号

**判断标准：** 图标是否暗示一个水平方向？是 → 镜像。否 → 保持不变。

### 1.3 RTL 语言

| 语言 | 代码 | 使用人口 |
|------|------|----------|
| 阿拉伯语 | ar | ~4.2 亿 |
| 乌尔都语 | ur | ~2.3 亿 |
| 波斯语 | fa | ~1.1 亿 |
| 普什图语 | ps | ~6000 万 |
| 希伯来语 | he | ~900 万 |

### 1.4 代码检测

```kotlin
// 方式一：Configuration（推荐）
val isRtl = resources.configuration.layoutDirection == View.LAYOUT_DIRECTION_RTL

// 方式二：TextUtils
val isRtl = TextUtilsCompat.getLayoutDirectionFromLocale(Locale.getDefault()) == ViewCompat.LAYOUT_DIRECTION_RTL

// 方式三：View 级别
val isRtl = view.layoutDirection == View.LAYOUT_DIRECTION_RTL
```

---

## 二、基础适配

### 2.1 Manifest 声明

```xml
<application android:supportsRtl="true" />
```

### 2.2 XML 属性替换

将所有 `Left/Right` 替换为 `Start/End`：

- `marginLeft` → `marginStart`, `paddingLeft` → `paddingStart`
- `marginRight` → `marginEnd`, `paddingRight` → `paddingEnd`
- `drawableLeft` → `drawableStart`, `Gravity.LEFT` → `Gravity.START`

**一键操作：** Android Studio → Refactor → Add RTL Support Where Possible

### 2.3 方向性图标处理

**方式一 autoMirrored（VectorDrawable）**

```xml
<vector android:autoMirrored="true">
    <path android:pathData="..." />
</vector>
```

**方式二 scaleX（代码动态）**

```kotlin
binding.btnBack.scaleX = if (isRtl) -1f else 1f
```

**方式三 rotationY（XML静态+资源联动）**

```xml
<!-- values/integers.xml -->
<integer name="icon_rotation">0</integer>
<!-- values-ldrtl/integers.xml -->
<integer name="icon_rotation">180</integer>
<!-- 布局中引用 -->
<ImageView android:rotationY="@integer/icon_rotation" />
```

### 2.4 文字对齐

```kotlin
textView.gravity = Gravity.START or Gravity.CENTER_VERTICAL
```

### 2.5 代码中的方向性 API

```kotlin
// 错误：固定方向
textView.setCompoundDrawables(icon, null, null, null)
// 正确：相对方向
textView.setCompoundDrawablesRelative(icon, null, null, null)
```

### 2.6 全局样式配置

```xml
<style name="AppTextStyle" parent="...">
    <item name="android:gravity">start</item>
    <item name="android:textDirection">locale</item>
    <item name="android:textAlignment">viewStart</item>
</style>
```

### 2.7 资源限定符目录

- `drawable-ldrtl/` → RTL 专用 Drawable
- `anim-ldrtl/` → RTL 专用动画
- `values-ldrtl/` → RTL 专用 values

> `ldrtl` 限定符在 API 17+ 可用

---

## 三、布局容器 RTL 行为

| 容器 | RTL 表现 | 关键注意 |
|------|----------|----------|
| ConstraintLayout | Start/End 约束自动镜像 | Left/Right 不响应 RTL |
| LinearLayout | 水平方向子View顺序翻转 | - |
| RelativeLayout | alignParentStart/End 跟随 RTL | alignParentLeft/Right 不跟随 |
| FrameLayout | layout_gravity start/end 自动镜像 | - |
| DrawerLayout | layout_gravity start 自动切换到右侧 | 必须用 start/end |
| RecyclerView | LinearLayoutManager 自动适配 | ViewHolder复用注意gravity |
| ViewPager (v1) | 不支持 RTL | 迁移到 ViewPager2 |
| TextInputLayout | 自动适配 hint | 内部 EditText 也需设 textDirection |

---

## 四、适配方案选型

- **方案A Native RTL（推荐）：** 系统 `layoutDirection=RTL` 驱动，天然支持嵌套
- **方案B Container scaleX：** 容器 `scaleX=-1f` 视觉翻转，适合简单扁平组件

### 方案A 代码模板

```kotlin
class DetailFragment : Fragment(R.layout.fragment_detail) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        view?.post { applyRtlIfNeeded() }
    }

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)
        view?.post { applyRtlIfNeeded() }
    }

    private fun applyRtlIfNeeded() {
        val isRtl = resources.configuration.layoutDirection == View.LAYOUT_DIRECTION_RTL
        val scale = if (isRtl) -1f else 1f
        binding.btnPrev.scaleX = scale
        binding.btnNext.scaleX = scale
        binding.btnBack.scaleX = scale
        binding.textContent.gravity =
            if (isRtl) Gravity.END or Gravity.CENTER_VERTICAL
            else Gravity.START or Gravity.CENTER_VERTICAL
    }
}
```

### 方案B 代码模板

```kotlin
fun applyRtlFixes(isRtl: Boolean) {
    val container = binding.root as? ViewGroup ?: return
    val scale = if (isRtl) -1f else 1f
    container.scaleX = scale
    for (i in 0 until container.childCount) {
        val child = container.getChildAt(i)
        child.scaleX = when (child.id) {
            R.id.btn_prev, R.id.btn_next -> 1f
            else -> scale
        }
    }
}
```

> **方案B前提：** XML 必须设 `layoutDirection="ltr"` 防止双重翻转

---

## 五、常见陷阱

### 陷阱 1：图标"面对面"（角对角）

**现象：** 前进/后退按钮从"背靠背"变成"面对面"。

**原因：** 系统镜像了按钮位置，但自定义 Icon 控件的 Drawable 方向没有跟着变。

**修复：**

```kotlin
binding.btnPrev.scaleX = if (isRtl) -1f else 1f
binding.btnNext.scaleX = if (isRtl) -1f else 1f
```

### 陷阱 2：setText 重置 gravity

**现象：** 页面打开时文字对齐正确，切换数据后文字跳到错误位置。

**原因：** 某些自定义 TextView 在 `setText()` 内部重置了 gravity。

**修复：** 在每次数据更新后重新应用 RTL 修正。

```kotlin
viewModel.observe { data ->
    binding.textContent.text = data.content
    view?.post { applyRtlIfNeeded() }
}
```

### 陷阱 3：setBackgroundResource 异步重置 scaleX

**现象：** 按钮方向偶尔错误（非必现）。

**原因：** `setBackgroundResource()` 可能触发异步操作，完成后重置 scaleX。

**修复：** `view?.post { applyRtlIfNeeded() }` 延迟到下一帧。

### 陷阱 4：DataBinding 覆盖 View tag

**现象：** 用 `view.tag == "skip_rtl"` 判断是否跳过，但实际不生效。

**原因：** DataBinding 框架会覆盖 View 的 tag 属性。

**修复：** 使用类型检查。

```kotlin
if (view is CustomPlayerView) return   // 可靠
if (view.tag == "skip_rtl") return     // 被 DataBinding 覆盖
```

### 陷阱 5：RecyclerView ItemDecoration 间距错乱

**现象：** 切换 RTL 后列表项间距异常。

**原因：** `ItemDecoration.getItemOffsets()` 中使用了 left/right 硬编码。

**修复：**

```kotlin
val isRtl = parent.layoutDirection == View.LAYOUT_DIRECTION_RTL
outRect.left  = if (isRtl) 0 else 16
outRect.right = if (isRtl) 16 else 0
```

### 陷阱 6：getLeft/getRight 坐标系不变

**现象：** 自定义 View 的 `onDraw()` 在 RTL 下绘制位置不对。

**原因：** RTL 改变的是布局方向，但 `View.getLeft()`、`View.getRight()`、`View.getX()` 等返回值不变。

**修复：** 在绘制逻辑中手动翻转坐标。

```kotlin
override fun onDraw(canvas: Canvas) {
    val isRtl = layoutDirection == View.LAYOUT_DIRECTION_RTL
    if (isRtl) {
        canvas.scale(-1f, 1f, width / 2f, height / 2f)
    }
}
```

### 陷阱 7：侧滑返回手势冲突

**现象：** RTL 下侧滑返回手势方向与用户预期相反。

**修复：**

```kotlin
val edgeFlags = if (isRtl) GestureDetector.EDGE_RIGHT else GestureDetector.EDGE_LEFT
```

### View.post 机制

`View.post(Runnable)` 将操作插入 MessageQueue 末尾，确保在当前帧所有同步操作完成后执行。

**必须使用 post 的四个场景：**

1. `onViewCreated` - 布局可能尚未完全 measure/layout
2. `onConfigurationChanged` - forceLayoutDirection 同步执行
3. 数据观察回调 - setText/setBackground 可能异步重置属性
4. `onCreate` 初始 RTL - Fragment 事务尚未完成

**幂等性要求：**

```kotlin
binding.btn.scaleX = if (isRtl) -1f else 1f   // 幂等：调用N次结果一致
binding.btn.scaleX *= -1f                       // 非幂等：调用2次恢复原值
```

---

## 六、不可重建 Activity

适用于车载系统、媒体播放器等不允许 Activity 重建的场景。

### 6.1 声明 configChanges

```xml
<activity android:configChanges="locale|layoutDirection" />
```

必须同时声明两者。只声明其一，切换语言时 Activity 仍会重建。

**车载系统完整配置：**

```xml
<activity
    android:configChanges="locale|layoutDirection|fontScale|uiMode|orientation|screenSize|keyboard|keyboardHidden"
    android:launchMode="singleTask" />
```

### 6.2 手动递归刷新 layoutDirection

声明 `configChanges` 后系统不再自动更新 View 树的 layoutDirection，需手动递归：

```kotlin
private fun forceLayoutDirection(view: View, direction: Int) {
    if (view is CustomPlayerView) return
    if (view is ViewGroup) {
        view.layoutDirection = direction
        for (i in 0 until view.childCount) {
            forceLayoutDirection(view.getChildAt(i), direction)
        }
    }
}
```

### 6.3 执行时序

`Activity.onConfigurationChanged()` 执行顺序：

1. `super` → `Fragment.onConfigChanged` → `view?.post{applyRtl}` 入队
2. `forceLayoutDirection(root, RTL)` 同步完成
3. `playerView.applyRtlFixes(true)` 同步完成
4. Fragment 的 `post{applyRtl}` 在下一帧执行

### 6.4 首次 RTL 启动

`configChanges` 声明后，首次以 RTL 语言启动时 `onConfigurationChanged` 不会被调用。

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    val isRtl = resources.configuration.layoutDirection == View.LAYOUT_DIRECTION_RTL
    if (isRtl) {
        binding.root.post {
            forceLayoutDirection(window.decorView, View.LAYOUT_DIRECTION_RTL)
        }
    }
}
```

### 6.5 PIP / 浮窗位置适配

浮窗的绝对位置不会因 RTL 自动翻转，需手动计算镜像坐标：

```kotlin
private fun adjustWindowForRtl(rect: Rect): Rect {
    val isRtl = resources.configuration.layoutDirection == View.LAYOUT_DIRECTION_RTL
    if (!isRtl) return rect
    val screenWidth = Resources.getSystem().displayMetrics.widthPixels
    return Rect(
        screenWidth - rect.right, rect.top,
        screenWidth - rect.left, rect.bottom
    )
}
```

---

## 七、Jetpack Compose 适配

### 7.1 自动支持

Compose 在系统 Locale 为 RTL 时自动处理：

- `Modifier.padding(start, end)` 自动映射
- `Alignment.Start / End` 自动镜像
- `Row` 子元素顺序自动反转
- `LazyRow / LazyColumn` 滚动方向自动适配

### 7.2 检测与控制

```kotlin
val isRtl = LocalLayoutDirection.current == LayoutDirection.Rtl

// 强制 RTL
CompositionLocalProvider(LocalLayoutDirection provides LayoutDirection.Rtl) {
    Content()
}

// 保持 LTR
CompositionLocalProvider(LocalLayoutDirection provides LayoutDirection.Ltr) {
    Text("+86 138 0000 0000")
}
```

### 7.3 图标镜像

```kotlin
Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back")

fun Modifier.autoMirror() = composed {
    if (LocalLayoutDirection.current == LayoutDirection.Rtl)
        graphicsLayer(scaleX = -1f) else this
}
```

### 7.4 Arrangement

```kotlin
Arrangement.spacedBy(8.dp)            // 自动适配 RTL
Arrangement.Absolute.spacedBy(8.dp)   // 固定从左到右
```

### 7.5 View vs Compose 对比

| 能力 | View | Compose |
|------|------|---------|
| 启用 RTL | Manifest + XML 改造 | 自动 |
| 布局方向 | `view.layoutDirection` | `LocalLayoutDirection` |
| 图标镜像 | `autoMirrored` / `scaleX` | `Icons.AutoMirrored` / `graphicsLayer` |
| 强制方向 | `view.layoutDirection = LTR` | `CompositionLocalProvider` |
| 动画 | 手动取反 `translationX` | `slideInHorizontally` 自动适配 |

---

## 八、资源与文本

### 8.1 Drawable

| 类型 | RTL 处理 |
|------|----------|
| VectorDrawable | `autoMirrored="true"` |
| PNG | 放到 `drawable-ldrtl/` 或 `scaleX = -1f` |

### 8.2 自定义 View 绘制（Canvas RTL）

**方式一：Canvas 全局翻转（推荐简单场景）**

```kotlin
override fun onDraw(canvas: Canvas) {
    val isRtl = layoutDirection == View.LAYOUT_DIRECTION_RTL
    if (isRtl) {
        canvas.save()
        canvas.scale(-1f, 1f, width / 2f, height / 2f)
    }
    drawContent(canvas)
    if (isRtl) canvas.restore()
}
```

**方式二：逐属性翻转（精细控制）**

```kotlin
override fun onDraw(canvas: Canvas) {
    val isRtl = layoutDirection == View.LAYOUT_DIRECTION_RTL
    val startX = if (isRtl) width - paddingEnd.toFloat() else paddingStart.toFloat()
    val dir = if (isRtl) -1f else 1f
    canvas.drawLine(startX, 0f, startX + 100f * dir, 0f, paint)
}
```

> 自定义 View 重写 `onRtlPropertiesChanged(layoutDirection: Int)` 可在方向变更时接收回调。

### 8.3 文字方向

```xml
android:textDirection="locale"        <!-- 跟随系统 -->
android:textDirection="anyRtl"        <!-- 含 RTL 字符则按 RTL -->
android:textDirection="firstStrong"   <!-- 首个强方向字符决定 -->
```

### 8.4 字符串拼接

```kotlin
// 错误：硬拼接
val text = prefix + " " + title
// 正确：字符串模板
val text = getString(R.string.format, prefix, title)
```

混合方向文本使用 BidiFormatter：

```kotlin
val formatter = BidiFormatter.getInstance()
val safeText = formatter.unicodeWrap("John")
```

### 8.5 XML 布局注意事项

- 避免约束冲突：Start/End 各一个约束，不要同方向两个。
- 保持 LTR 的内容（电话号码、URL、时间戳）：

```xml
<TextView android:layoutDirection="ltr" android:textDirection="ltr" />
```

### 8.6 RecyclerView

列表项使用 Start/End 即可自动适配。ViewHolder 复用时注意修正 gravity：

```kotlin
override fun onBindViewHolder(holder: VH, position: Int) {
    holder.binding.title.text = items[position].title
    val isRtl = holder.itemView.layoutDirection == View.LAYOUT_DIRECTION_RTL
    holder.binding.title.gravity =
        if (isRtl) Gravity.END or Gravity.CENTER_VERTICAL
        else Gravity.START or Gravity.CENTER_VERTICAL
}
```

---

## 九、动画与手势

动画和手势的水平方向在 RTL 下需要取反。

### 9.1 translationX 动画

```kotlin
val dir = if (isRtl) -1f else 1f
view.animate().translationX(300f * dir).setDuration(300).start()
```

### 9.2 属性动画（ObjectAnimator）

```kotlin
val dir = if (isRtl) -1f else 1f
ObjectAnimator.ofFloat(view, "translationX", 0f, 200f * dir).apply {
    duration = 250
    start()
}
```

### 9.3 RTL 专用动画资源

- `res/anim/slide_in.xml` → LTR：从右滑入
- `res/anim-ldrtl/slide_in.xml` → RTL：从左滑入（方向反转）

### 9.4 手势方向

```kotlin
val effective = if (isRtl) -velocityX else velocityX
if (effective > threshold) onSwipeForward()
```

### 9.5 Compose 动画

```kotlin
AnimatedVisibility(
    visible = visible,
    enter = slideInHorizontally { it },
    exit = slideOutHorizontally { -it }
)
```

---

## 十、工具与调试

### 10.1 快速测试方法

| 方法 | 操作 | 适用场景 |
|------|------|----------|
| 开发者选项 | 设置 → 开发者选项 → 强制使用从右到左 | 最快速，不改语言 |
| adb 切换语言 | 见下方命令 | 模拟真实 RTL 环境 |
| 代码强制 RTL | `Configuration.setLocale()` + `createConfigurationContext()` | 单元测试 |

### 10.2 adb 命令

```bash
adb shell "setprop persist.sys.locale ar-SA; stop; start"   # 切换阿拉伯语
adb shell "setprop persist.sys.locale zh-CN; stop; start"   # 恢复中文
```

### 10.3 Layout Inspector

重点检查以下属性：

| 属性 | LTR 预期 | RTL 预期 |
|------|----------|----------|
| layoutDirection | 0 (LTR) | 1 (RTL) |
| scaleX（方向图标） | 1.0 | -1.0 |
| gravity（文字） | START (8388611) | END (8388613) |

### 10.4 Lint 检查

```groovy
android {
    lintOptions {
        enable 'RtlHardcoded', 'RtlEnabled', 'RtlSymmetry'
    }
}
```

| 规则 | 检测内容 |
|------|----------|
| RtlHardcoded | 使用了 left/right 而非 start/end |
| RtlEnabled | 未声明 `supportsRtl="true"` |
| RtlSymmetry | paddingLeft 有但 paddingRight 没有（不对称） |

### 10.5 调试日志模板

```kotlin
Log.d(TAG, "RTL: isRtl=$isRtl, scaleX=${btn.scaleX}, gravity=${text.gravity}, dir=${root.layoutDirection}")
```

---

## 十一、项目迁移

按以下步骤对现有项目进行 RTL 改造，建议分模块逐步推进。

### 11.1 迁移步骤

1. Manifest 添加 `supportsRtl="true"`
2. Refactor → Add RTL Support（一键替换 Left/Right）
3. 手动检查：电话号码/时间/URL 需保留 Left/Right
4. 方向性 Drawable 添加 `autoMirrored="true"`
5. 自定义控件编写 `applyRtlIfNeeded()`
6. 全面测试（参照第十二章清单）

### 11.2 代码替换对照表

| 旧写法 | 新写法 |
|--------|--------|
| `setPadding(l, t, r, b)` | `setPaddingRelative(start, t, end, b)` |
| `Gravity.LEFT / RIGHT` | `Gravity.START / END` |
| `translationX = 300f` | `translationX = 300f * direction` |
| `setCompoundDrawables(l, t, r, b)` | `setCompoundDrawablesRelative(s, t, e, b)` |
| `view.paddingLeft / paddingRight` | `view.paddingStart / paddingEnd` |

---

## 十二、测试清单

提交前逐项检查。

| 分类 | 检查项 | 优先级 |
|------|--------|--------|
| 功能 | LTR → RTL → LTR 多次切换无异常 | ★ |
| 功能 | 首次以 RTL 语言冷启动正常 | ★ |
| 功能 | 后台切换语言后返回正常 | - |
| 视觉 | 方向性按钮始终"背靠背" | ★ |
| 视觉 | 非方向性图标未被翻转 | - |
| 视觉 | 文字对齐正确，数据刷新后不变 | ★ |
| 视觉 | 进度条/滑块方向正确 | - |
| 交互 | RecyclerView 列表项镜像正确 | - |
| 交互 | RecyclerView ItemDecoration 间距正确 | - |
| 交互 | ViewPager2 滑动方向正确 | - |
| 交互 | 弹窗/Dialog 正确 | - |
| 交互 | 侧滑返回手势方向正确 | - |
| 内容 | 电话号码/URL/时间保持 LTR | - |
| 内容 | 混合语言文本显示正确 | - |
| 内容 | 动画和手势方向正确 | - |
| 绘制 | 自定义 View Canvas 绘制方向正确 | - |
| 绘制 | 浮窗/PIP 窗口位置正确 | - |
| 绘制 | setCompoundDrawablesRelative 方向正确 | - |

---

## 附录

### A. API 兼容性速查

| 特性 | 最低版本 | 备注 |
|------|----------|------|
| supportsRtl / Start/End / layoutDirection | API 17 | 基础能力 |
| setCompoundDrawablesRelative() | API 17 | 替代 setCompoundDrawables |
| onRtlPropertiesChanged() | API 17 | 自定义 View 方向变更回调 |
| ldrtl 资源限定符 | API 17 | drawable / anim / values |
| BidiFormatter | API 18 | 混合方向文本处理 |
| autoMirrored | API 19 | VectorDrawable 自动镜像 |
| ViewCompat.setLayoutDirection() | AndroidX | 向下兼容封装 |
| Compose RTL | Compose 1.0+ | 自动支持 |
| Icons.AutoMirrored | Material3 1.2+ | Compose 图标自动镜像 |

### B. 性能注意事项

| 操作 | 影响 | 建议 |
|------|------|------|
| forceLayoutDirection 递归 | 触发 requestLayout() | 仅在配置变更时调用，加标记位 |
| scaleX 翻转 | 启用硬件层 | 性能开销可忽略 |
| RecyclerView onBind | 高频调用 | 直接设置属性，不用 post |
| Canvas scale | 每帧执行 | 配合 save/restore，开销极小 |

### C. 核心原则

1. **XML 优先：** Start/End 替代 Left/Right
2. **幂等设计：** `applyRtlIfNeeded()` 可安全重复调用
3. **时序安全：** `View.post` 避免竞争条件
4. **持续修正：** 数据更新后重新应用 RTL
5. **分类处理：** 区分方向性/非方向性图标
6. **相对 API：** `setCompoundDrawablesRelative` / `paddingStart` / `Gravity.START`
7. **坐标不变：** `getLeft/getRight/getX` 不因 RTL 变化
8. **全面测试：** 冷启动·热切换·刷新·导航

### D. 参考资料

**官方文档**

| 资源 | 链接 |
|------|------|
| Android 官方 RTL 指南 | https://developer.android.com/training/basics/supporting-devices/languages |
| Material Design 双向性 | https://m2.material.io/design/usability/bidirectionality.html |
| Compose 布局方向 | https://kotlinlang.org/docs/multiplatform/compose-rtl.html |
| Unicode 双向算法 | https://www.w3.org/International/articles/inline-bidi-markup/uba-basics |

**社区实践**

| 资源 | 链接 |
|------|------|
| RTL 布局适配实战 | https://blog.csdn.net/qq_24535745/article/details/125064883 |
| 阿拉伯语适配详解 | https://blog.csdn.net/qq_34947883/article/details/90607299 |
| RTL 海外适配策略 | https://blog.csdn.net/qq_40611604/article/details/140654875 |
| 左右舵镜像支持 | https://blog.csdn.net/weixin_35691921/article/details/141232473 |
| RTL 车载适配总结 | https://blog.csdn.net/sinat_31057219/article/details/133710145 |
| ProAndroidDev RTL Design | https://proandroiddev.com/supporting-rtl-design-on-android-d6ef0ac31874 |
