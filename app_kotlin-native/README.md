# Dx Dice Thrower

This application is a UNIX-way inspired service which allow you to throw a Dice with arbitrary number of sides

## Getting started
1. Install the Gradle
2. Run `gradle nativeBinaries`
3. Run the binary
```bash
./build/bin/native/releaseExecutable/app_kotlin-native.kexe
```
4. Throw classic D6:
```bash
http://127.0.0.1:8080/?d=20
```

## Miscellaneous
### Run the linter
1. Download `ktlint` by following [the official manual](https://pinterest.github.io/ktlint/1.0.0/install/cli/)
2. Run linter
```bash
ktlint
```

## Requirements
- Linux or MacOS on your PC. Windows ~~must die~~ not supported
- Gradle 8.2.1