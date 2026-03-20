---
description: "Kotlin coding style extending common rules"
globs: ["**/*.kt", "**/*.kts", "**/build.gradle.kts"]
alwaysApply: false
---
# Kotlin Coding Style

> This file extends the common coding style rule with Kotlin-specific content.

## Formatting

- 使用 **ktfmt** 或 **ktlint** 进行自动格式化（在项目或编辑器中配置）
- Use trailing commas in multiline declarations

## Immutability

The global immutability requirement is enforced in the common coding style rule.
For Kotlin specifically:

- Prefer `val` over `var`
- Use immutable collection types (`List`, `Map`, `Set`)
- Use `data class` with `copy()` for immutable updates

## Null Safety

- Avoid `!!` -- use `?.`, `?:`, `require`, or `checkNotNull`
- Handle platform types explicitly at Java interop boundaries

## Expression Bodies

Prefer expression bodies for single-expression functions:

```kotlin
fun isAdult(age: Int): Boolean = age >= 18
```

## Reference

See skill: `kotlin-patterns` for comprehensive Kotlin idioms and patterns.
