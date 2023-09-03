# Flutter App

This app shows the current Moscow time in ISO format

### Setup
First, you have to [download Flutter](https://docs.flutter.dev/get-started/install/)
```
brew tap dart-lang/dart
brew install dart
dart pub global activate webdev
```

### Run
Move to the `app_dart/app` directory
```
flutter pub get
flutter run -d chrome 
```

### Test
Run this in the `app_dart/app` directory
```
flutter test test/widget_test.dart --platform chrome
```