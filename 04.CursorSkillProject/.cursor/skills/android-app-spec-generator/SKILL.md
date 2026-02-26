---
name: android-app-spec-generator
description: Generate Android app specification documents (PRD/式様書/设计文档) via a 6-phase structured workflow. Covers product definition, user personas, feature requirements, UI/UX design, technical architecture, and non-functional requirements. Use when planning an Android app, writing app specs, creating a PRD, product requirements document, technical specification, feature spec, design document, or requirements document for mobile apps. Supports Camera, Social, E-commerce, Tools, and other Android app types.
---

# Android App Specification Generator

Generate professional, detailed specification documents (式様書) for Android applications through a structured, interactive workflow.

**Output language: Chinese (中文)**. All generated specification documents MUST be written in Chinese.

## Quick Start

When the user wants to generate an Android app specification:

1. Identify the app type (Camera, Social, E-commerce, etc.)
2. Follow the 6-phase workflow below
3. Output each section for incremental validation
4. Compile the final document using the template in [spec-template.md](spec-template.md)

## 6-Phase Workflow

### Phase 1: Product Definition (产品定义)

**Goal**: Establish product vision, target users, and core value.

Ask ONE question at a time (prefer multiple-choice):

1. **App type**: Camera / Social / E-commerce / Tools / Health / Education / Finance / Other
2. **Target users**: Demographics, technical proficiency, usage scenarios
3. **Core value proposition**: What problem does this solve? Why will users choose this?
4. **Competitive landscape**: Top 3 competitors and differentiation points
5. **Target platforms**: Android min SDK, tablet support, foldable support
6. **Tech stack preference**: Kotlin/Java, Jetpack Compose/XML Views, architecture pattern

Output: `## 1. 产品概述` section (200-300 words), ask for confirmation before proceeding.

### Phase 2: User Personas & Journeys (用户画像与旅程)

**Goal**: Define who uses the app and how.

For each identified user type:

1. Create a persona card:
   - Name, age range, occupation
   - Pain points and goals
   - Tech proficiency level
   - Usage frequency and context

2. Map core user journeys:
   - Entry point → Key actions → Exit point
   - Happy path and error paths
   - Decision points and branches

Output: `## 2. 用户画像与用户旅程` section, ask for confirmation.

### Phase 3: Feature Requirements (功能需求)

**Goal**: Detailed feature specification with priority ranking.

For EACH feature module, use this structured approach:

1. **Explore with questions** (Socratic method, one at a time, max 4 questions per feature):
   - What does this feature do? (core behavior)
   - What triggers it? (user action / system event)
   - What are the edge cases? (error states, boundary conditions)
   - What permissions are needed? (Android runtime permissions)

2. **Propose 2-3 implementation approaches** with trade-offs and your recommendation

3. **Document each feature**:
   - Feature ID and name
   - Priority: P0 (must-have) / P1 (should-have) / P2 (nice-to-have)
   - Description (50-100 words)
   - Acceptance criteria (testable)
   - Dependencies and constraints
   - Android-specific considerations (permissions, hardware requirements)

Output: `## 3. 功能需求详细说明` section by module, validate each module.

### Phase 4: UI/UX Design Specification (界面设计规范)

**Goal**: Complete UI specification following Android design guidelines.

Cover these aspects:

1. **Navigation structure**: Bottom nav / drawer / tab layout
2. **Screen inventory**: List all screens with wireframe descriptions
3. **Interaction patterns**:
   - Touch targets (min 48dp per Material Design 3)
   - Gestures (swipe, pinch, long-press)
   - Transitions and animations
   - Loading states and skeleton screens
4. **Design system**:
   - Color palette (light/dark theme, Material You dynamic color)
   - Typography scale
   - Spacing and layout grid
   - Component patterns (buttons, cards, dialogs, bottom sheets)
5. **Accessibility**: Content descriptions, focus order, contrast ratios
6. **Responsive**: Phone, tablet, foldable, landscape modes

Output: `## 4. 界面设计规范` section, validate.

### Phase 5: Technical Architecture (技术架构)

**Goal**: Define the technical implementation plan.

Document:

1. **Architecture pattern**: MVVM / MVI / Clean Architecture layers
2. **Module structure**: Feature modules, core modules, dependencies
3. **Key technology choices**:
   - UI: Jetpack Compose vs XML Views
   - Navigation: Jetpack Navigation
   - DI: Hilt / Koin
   - Networking: Retrofit + OkHttp
   - Local storage: Room / DataStore
   - Image loading: Coil / Glide
   - Domain-specific APIs (e.g., CameraX, MediaCodec)
4. **Data flow**: State management, repository pattern
5. **System context diagram**: External dependencies (APIs, cloud services, OS services)
6. **Build and CI/CD**: Gradle modules, build variants, testing strategy

Output: `## 5. 技术架构` section, validate.

### Phase 6: Non-Functional Requirements (非功能需求)

**Goal**: Define quality attributes and constraints.

Cover:

1. **Performance targets**:
   - Cold start: < 1.5s
   - Frame rate: 60fps (UI), configurable for camera
   - Memory: < 200MB typical
   - APK size: < 50MB
2. **Security**: Data encryption, permission model, API key protection
3. **Privacy**: GDPR/privacy policy, data collection, consent
4. **Offline support**: Graceful degradation, sync strategy
5. **Localization**: Supported languages, RTL support
6. **Testing strategy**: Unit/integration/UI test coverage targets
7. **Release plan**: Versioning, rollout strategy, crash monitoring

Output: `## 6. 非功能需求` and `## 7. 发布计划` sections.

## Output Rules

1. **Language**: All specification content MUST be in Chinese (中文)
2. **Incremental validation**: Present each major section (200-300 words), confirm before moving on
3. **YAGNI**: Remove unnecessary features — if a module has >5 P0 features, explicitly ask "哪3个功能是 MVP 最核心的？" to force prioritization
4. **Concrete over vague**: Every feature must have testable acceptance criteria with specific numbers (e.g., "< 200ms" not "fast")
5. **Android-native**: Follow Material Design 3, use Jetpack libraries as defaults
6. **File output**: Before saving, ensure `docs/specs/` directory exists (create if missing). Confirm the output path with the user. Save to `docs/specs/YYYY-MM-DD-<app-name>-spec.md`

## Recovery & Flow Control

Handle these situations gracefully:

- **User skips a phase**: Note the skipped phase as "待补充" (TBD) in the document. Continue to the next phase. Remind the user at the end which phases need completion.
- **User gives multiple answers at once**: Acknowledge all answers, fill in the corresponding spec sections, then continue with the next unresolved question.
- **User wants to go back**: Update the earlier section and check if downstream sections need adjustment (e.g., changing tech stack in Phase 1 may affect Phase 4/5).
- **User gives vague answers**: Ask a follow-up with 2-3 concrete options. Example: if user says "需要好的性能", ask "具体来说，冷启动目标是 <1秒 / <1.5秒 / <2秒？"
- **User rejects a section**: Ask what needs to change, revise that section, then re-present for confirmation.
- **User wants to add features mid-process**: Add them to the appropriate module, re-evaluate priority ranking, and flag if scope has grown significantly.

## App-Type Specific Modules

For specialized app types, automatically include domain-specific sections and load the corresponding resource files:

### Camera App (相机应用)

**Resource loading order:**
1. Before Phase 3 → Read [camera-checklist.md](camera-checklist.md) for API selection and permission planning
2. During Phase 3, if filters/beauty/AI features are in scope → Read [camera-advanced.md](camera-advanced.md)
3. During Phase 4, if Jetpack Compose is chosen → Read [compose-guidelines.md](compose-guidelines.md)
4. When compiling final document → Use [example-camera-spec.md](example-camera-spec.md) as quality benchmark

Additional sections to include:

- **Camera API selection**: CameraX (recommended) vs Camera2 comparison
- **Capture modes**: Photo, Video, Time-lapse, Slow-motion, Panorama, Night mode
- **Image processing pipeline**: Preview → Capture → Post-processing → Save
- **Filter/Effect system**: Real-time preview filters, GPU shader pipeline
- **Media management**: Gallery integration, EXIF data, file format support
- **Hardware requirements**: Camera sensor specs, OIS, flash, depth sensor

### Social App (社交应用)

- User authentication and profile system
- Feed algorithms and content distribution
- Messaging and notification system
- Content moderation strategy

### E-commerce App (电商应用)

- Product catalog and search
- Shopping cart and checkout flow
- Payment integration (WeChat Pay, Alipay, etc.)
- Order management and logistics tracking

### Tools App (工具应用)

- Core utility workflow
- Widget and shortcut support
- Background processing and scheduling

## Key Principles

- **One question at a time** — Never overwhelm with multiple questions
- **Multiple choice preferred** — Easier to answer than open-ended
- **Explore alternatives** — Always propose 2-3 approaches before settling
- **Incremental validation** — Present design in sections, validate each
- **Android-first thinking** — Consider Android-specific constraints (permissions, lifecycle, battery)
- **Production ready** — Specs should be detailed enough for a developer to implement directly

## Additional Resources

- For the complete output template, see [spec-template.md](spec-template.md)
- For Camera app specific checklist, see [camera-checklist.md](camera-checklist.md)
- For Camera advanced features (filters, beauty, AI), see [camera-advanced.md](camera-advanced.md)
- For Jetpack Compose UI component guidelines, see [compose-guidelines.md](compose-guidelines.md)
- For a complete example specification, see [example-camera-spec.md](example-camera-spec.md)
