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

## Requirements
- Linux or MacOS on your PC. Windows ~~must die~~ not supported
- Gradle 8.2.1