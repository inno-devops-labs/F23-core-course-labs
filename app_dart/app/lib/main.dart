import 'package:flutter/material.dart';
import 'package:timezone/browser.dart' as tz;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<StatefulWidget> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String? _text;

  @override
  void initState() {
    _setMoscowTime();
    super.initState();
  }

  Future<void> _setMoscowTime() async {
    final time = await _moscowTime();
    setState(() {
      _text = time;
    });
  }

  Future<String> _moscowTime() async {
    await tz.initializeTimeZone();
    final moscow = tz.getLocation('Europe/Moscow');
    return tz.TZDateTime.now(moscow).toIso8601String();
  }

  @override
  Widget build(BuildContext context) => MaterialApp(
        home: Material(
          child: Center(
            child: _text == null
                ? const CircularProgressIndicator()
                : Text(
                    _text!,
                    key: const Key('time-text'),
                    style: const TextStyle(fontSize: 40),
                  ),
          ),
        ),
      );
}
