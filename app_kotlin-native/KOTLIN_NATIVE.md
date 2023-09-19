# Explanation of decisions

## Kotlin/Multiplatform as a language (why not Kotlin/JVM)
Primary reason - Kotlin/Multiplatform (aka Kotlin Native when target is binary), it doesn't require some complicated and heavyweight runtime.

## Gradle as a Build System
There are two ways to compile Kotlin code:
- Using Gradle
- Using CLI Compiler

I would like to follow first way because it's primary method of dealing with Kotlin Native. Also, it will be overcomplication to write Makefiles for each file and then manually link them

## Ktor as a Server Framework
Unfortunately, Kotlin Native is not so popular thing to use, so Ktor with CIO engine is the only actively-maintained server framework

## Tests
Test framework is provided by Kotlin Multiplatform standard library. No need to reinvent bycicle. There is essential test for one and only incorrect case.