# Jetpack Compose UI 组件设计规范

## 1. Camera App 核心 Compose 组件

### 1.1 组件清单

| 组件名 | 类型 | 用途 | 复杂度 |
|--------|------|------|:------:|
| `CameraPreview` | Screen | 相机预览主屏幕 | 高 |
| `CaptureButton` | Component | 拍照/录像按钮 | 中 |
| `ModeSelector` | Component | 拍摄模式切换 | 中 |
| `FilterStrip` | Component | 滤镜选择条 | 中 |
| `BeautyPanel` | Component | 美颜参数面板 | 高 |
| `GalleryThumbnail` | Component | 最近照片缩略图 | 低 |
| `ZoomControl` | Component | 缩放控制（滑杆+按钮） | 中 |
| `ExposureSlider` | Component | 曝光补偿滑杆 | 低 |
| `FocusIndicator` | Component | 对焦框动画 | 中 |
| `SettingsSheet` | Screen | 设置底部面板 | 中 |
| `MediaViewer` | Screen | 照片/视频查看器 | 高 |

### 1.2 组件设计模板

```kotlin
/**
 * 组件名称：[ComponentName]
 * 
 * 功能描述：[一句话描述]
 * 
 * 参数：
 * @param modifier     外部修饰符
 * @param state        组件状态（XXXState）
 * @param onAction     用户动作回调
 * 
 * 设计要点：
 * - [要点 1]
 * - [要点 2]
 * 
 * 无障碍：
 * - contentDescription: [描述]
 * - 触摸目标: >= 48dp
 */
@Composable
fun ComponentName(
    modifier: Modifier = Modifier,
    state: ComponentState,
    onAction: (Action) -> Unit
) {
    // Implementation
}
```

---

## 2. CameraPreview 屏幕设计

### 2.1 布局结构

```kotlin
@Composable
fun CameraScreen(
    viewModel: CameraViewModel = hiltViewModel()
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    
    Box(modifier = Modifier.fillMaxSize()) {
        // Layer 1: 相机预览（全屏底层）
        CameraPreviewSurface(
            modifier = Modifier.fillMaxSize(),
            cameraState = uiState.cameraState
        )
        
        // Layer 2: 对焦指示器（覆盖在预览上）
        FocusIndicator(
            position = uiState.focusPoint,
            isVisible = uiState.showFocusRing
        )
        
        // Layer 3: 网格线（可选显示）
        if (uiState.showGrid) {
            GridOverlay(modifier = Modifier.fillMaxSize())
        }
        
        // Layer 4: 顶部工具栏
        TopToolbar(
            modifier = Modifier
                .align(Alignment.TopCenter)
                .statusBarsPadding(),
            flashMode = uiState.flashMode,
            onFlashToggle = viewModel::toggleFlash,
            onSettingsClick = viewModel::openSettings
        )
        
        // Layer 5: 右侧缩放控制
        ZoomControl(
            modifier = Modifier.align(Alignment.CenterEnd),
            zoomRatio = uiState.zoomRatio,
            onZoomChange = viewModel::setZoom
        )
        
        // Layer 6: 底部控制区
        BottomControls(
            modifier = Modifier
                .align(Alignment.BottomCenter)
                .navigationBarsPadding(),
            captureMode = uiState.captureMode,
            isRecording = uiState.isRecording,
            onCapture = viewModel::capture,
            onModeChange = viewModel::switchMode
        )
    }
}
```

### 2.2 层叠结构图

```
┌─────────────────────────────────┐
│ [闪光灯] [HDR] [AI]    [设置]   │ ← Layer 4: TopToolbar
├─────────────────────────────────┤
│                                 │
│                                 │
│        相机预览 (全屏)           │ ← Layer 1: CameraPreview
│                                 │
│              ◎ (对焦框)          │ ← Layer 2: FocusIndicator
│                                 │
│         ┃ (网格线)  ┃           │ ← Layer 3: GridOverlay
│                           ├─┤  │
│                           │Z│  │ ← Layer 5: ZoomControl
│                           │o│  │
│                           │o│  │
│                           │m│  │
│                           ├─┤  │
├─────────────────────────────────┤
│ [滤镜列表 ← 水平滚动 →]         │ ← FilterStrip
├─────────────────────────────────┤
│   模式: 拍照 | 录像 | 全景 | ... │ ← ModeSelector
├─────────────────────────────────┤
│ [缩略图]    ◉ 拍照按钮    [翻转] │ ← BottomControls
└─────────────────────────────────┘
```

---

## 3. 核心组件 Compose 规范

### 3.1 CaptureButton（拍照/录像按钮）

**尺寸**: 72dp (外圈) / 60dp (内圈)

**状态**:

| 状态 | 外观 | 动画 |
|------|------|------|
| 拍照待机 | 白色外圈 + 白色内圆 | 无 |
| 拍照按下 | 外圈缩小、内圆缩小 | 150ms spring |
| 拍照完成 | 闪烁 → 恢复 | 200ms 淡入淡出 |
| 录像待机 | 白色外圈 + 红色内圆 | 无 |
| 录像中 | 外圈旋转动画 + 红色方块 | 持续旋转 |
| 录像暂停 | 外圈暂停 + 红色暂停图标 | 脉冲动画 |

```kotlin
@Composable
fun CaptureButton(
    modifier: Modifier = Modifier,
    mode: CaptureMode,           // Photo / Video
    isRecording: Boolean = false,
    recordingDuration: Duration = Duration.ZERO,
    onTap: () -> Unit,           // 拍照 or 开始/停止录像
    onLongPress: () -> Unit = {} // 长按录像（拍照模式下）
) {
    // 72dp 触摸目标，含 ripple 效果
}
```

### 3.2 ModeSelector（模式切换）

**交互**: 水平滑动切换，当前模式居中高亮

```kotlin
@Composable
fun ModeSelector(
    modifier: Modifier = Modifier,
    modes: List<CaptureMode>,
    selectedMode: CaptureMode,
    onModeSelected: (CaptureMode) -> Unit
) {
    // LazyRow，带 SnapFlingBehavior 居中对齐
    // 当前项: 白色粗体文字
    // 其他项: 半透明普通文字
    // 切换动画: 300ms 滑动 + 缩放
}
```

**式样参数**:
- 文字大小: 选中 14sp / 未选中 12sp
- 间距: 每项 24dp
- 动画: 300ms `EaseInOutCubic`
- 触摸区域: 每项 >= 48dp 高

### 3.3 FilterStrip（滤镜选择条）

```kotlin
@Composable
fun FilterStrip(
    modifier: Modifier = Modifier,
    filters: List<Filter>,
    selectedFilter: Filter?,
    previewBitmap: Bitmap?,     // 当前帧缩略图用于预览
    onFilterSelected: (Filter) -> Unit
) {
    // LazyRow 水平滚动
    // 每个项: 64dp x 64dp 圆角缩略图 + 滤镜名称
    // 选中项: 2dp 白色边框 + 名称加粗
}
```

### 3.4 BeautyPanel（美颜面板）

```kotlin
@Composable
fun BeautyPanel(
    modifier: Modifier = Modifier,
    params: BeautyParams,
    onParamChange: (BeautyParamType, Float) -> Unit,
    onReset: () -> Unit
) {
    // BottomSheet 或可拖拽面板
    // 包含多个 SliderRow:
    //   [图标] [参数名] [────●────] [数值]
    // 底部: [重置] 按钮
}
```

**SliderRow 式样**:
- 图标: 24dp Material Icon
- 参数名: 12sp, 40dp 宽
- Slider: Material3 Slider, 主色调
- 数值: 12sp, 32dp 宽, 右对齐
- 行高: 48dp

---

## 4. 手势处理规范

### 4.1 相机预览手势

| 手势 | Compose 实现 | 行为 |
|------|-------------|------|
| 单击 | `Modifier.pointerInput { detectTapGestures { onTap } }` | 点击对焦 |
| 双击 | `detectTapGestures { onDoubleTap }` | 切换前后摄像头 |
| 长按 | `detectTapGestures { onLongPress }` | 锁定曝光/对焦 |
| 双指缩放 | `detectTransformGestures { onZoom }` | 变焦 |
| 上下滑动 | `detectVerticalDragGestures` | 曝光补偿 |
| 左右滑动 | `detectHorizontalDragGestures` | 切换拍摄模式 |

### 4.2 手势冲突处理

```
优先级（高→低）:
1. 双指缩放（变焦）— 最高优先级
2. 底部面板拖拽（滤镜/美颜切换）
3. 单指垂直滑动（曝光补偿）
4. 单指水平滑动（模式切换）
5. 单击（对焦）
6. 双击（前后摄像头切换）
```

---

## 5. 状态管理规范

### 5.1 UI 状态定义

```kotlin
@Stable
data class CameraUiState(
    // 相机状态
    val cameraState: CameraState = CameraState.Initializing,
    val lensFacing: LensFacing = LensFacing.Back,
    val flashMode: FlashMode = FlashMode.Off,
    val zoomRatio: Float = 1.0f,
    
    // 拍摄模式
    val captureMode: CaptureMode = CaptureMode.Photo,
    val isRecording: Boolean = false,
    val recordingDuration: Duration = Duration.ZERO,
    
    // 对焦
    val focusPoint: Offset? = null,
    val showFocusRing: Boolean = false,
    
    // 滤镜 & 美颜
    val selectedFilter: Filter? = null,
    val beautyParams: BeautyParams = BeautyParams.Default,
    
    // AI
    val detectedScene: Scene? = null,
    
    // UI 设置
    val showGrid: Boolean = false,
    val showBeautyPanel: Boolean = false,
    val showFilterStrip: Boolean = true,
    
    // 错误
    val error: CameraError? = null
)

sealed interface CameraState {
    data object Initializing : CameraState
    data object Ready : CameraState
    data class Error(val message: String) : CameraState
}
```

### 5.2 ViewModel 结构

```kotlin
@HiltViewModel
class CameraViewModel @Inject constructor(
    private val cameraRepository: CameraRepository,
    private val filterRepository: FilterRepository,
    private val beautyProcessor: BeautyProcessor,
    private val sceneDetector: SceneDetector,
    savedStateHandle: SavedStateHandle
) : ViewModel() {
    
    private val _uiState = MutableStateFlow(CameraUiState())
    val uiState: StateFlow<CameraUiState> = _uiState.asStateFlow()
    
    // User actions
    fun capture() { /* ... */ }
    fun switchMode(mode: CaptureMode) { /* ... */ }
    fun toggleFlash() { /* ... */ }
    fun setZoom(ratio: Float) { /* ... */ }
    fun focusAt(point: Offset) { /* ... */ }
    fun selectFilter(filter: Filter) { /* ... */ }
    fun updateBeautyParam(type: BeautyParamType, value: Float) { /* ... */ }
}
```

---

## 6. 动画规范

### 6.1 Camera App 专用动画

| 动画 | 触发 | 时长 | 缓动 | 实现 |
|------|------|------|------|------|
| 对焦框出现 | 点击预览 | 200ms | EaseOut | `animateFloatAsState` |
| 对焦框消失 | 对焦完成 | 300ms | EaseIn | `delay + fadeOut` |
| 快门闪烁 | 拍照瞬间 | 100ms | Linear | `Canvas alpha` |
| 模式切换 | 左右滑动 | 300ms | EaseInOutCubic | `AnimatedContent` |
| 滤镜切换 | 选择滤镜 | 200ms | EaseOut | `crossfade` |
| 美颜面板展开 | 点击美颜 | 300ms | Spring(0.8f) | `BottomSheet` |
| 录像计时器 | 录像中 | 持续 | Linear | `LaunchedEffect` |
| 前后摄像头切换 | 双击/按钮 | 400ms | EaseInOut | `rotation + fade` |

### 6.2 Compose 动画 API 选用指南

| 场景 | 推荐 API | 理由 |
|------|---------|------|
| 简单属性变化 | `animateXxxAsState` | 最简洁 |
| 可见性切换 | `AnimatedVisibility` | 自带入场/退场 |
| 内容切换 | `AnimatedContent` | 自动处理过渡 |
| 复杂多属性 | `Transition` | 多属性协调 |
| 手势跟随 | `Animatable` | 可中断、可弹簧 |
| 无限循环 | `rememberInfiniteTransition` | 录像指示器等 |

---

## 7. 主题与 Material Design 3

### 7.1 Camera App 配色方案

```kotlin
// 相机应用推荐使用深色主题为主
val CameraDarkColorScheme = darkColorScheme(
    primary = Color(0xFF_BB86FC),        // 主按钮/高亮
    onPrimary = Color(0xFF_000000),
    secondary = Color(0xFF_03DAC6),      // 次要操作
    background = Color(0xFF_000000),     // 相机背景（纯黑）
    surface = Color(0xFF_1E1E1E),        // 面板背景
    onSurface = Color(0xFF_FFFFFF),      // 文字/图标
    error = Color(0xFF_CF6679),          // 错误状态
    surfaceVariant = Color(0xFF_2D2D2D), // 工具栏背景
)

// 录像状态强调色
val RecordingRed = Color(0xFF_FF3B30)

// 滤镜选中色
val FilterSelectedBorder = Color(0xFF_FFFFFF)
```

### 7.2 触摸目标尺寸

```kotlin
// Camera App 中的最小触摸目标
val MinTouchTarget = 48.dp    // Material Design 3 标准
val CaptureButtonSize = 72.dp  // 拍照按钮（加大目标）
val ToolbarIconSize = 48.dp   // 工具栏图标触摸区
val FilterItemSize = 64.dp    // 滤镜缩略图
```
