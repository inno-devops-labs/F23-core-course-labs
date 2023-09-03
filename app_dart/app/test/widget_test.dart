import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:timezone/browser.dart' as tz;

import 'package:app/main.dart';

void main() {
  testWidgets(
    'Moscow time app test',
    (tester) async {
      await tester.runAsync(() async {
        await tester.pumpWidget(const MyApp());
        await tester.pumpAndSettle();

        final timeWidget =
            find.byKey(const Key('time-text')).evaluate().firstOrNull;
        expect(timeWidget, isNotNull);

        final textTime = timeWidget! as Text;
        expect(textTime.data, isNot(null));

        final appTime = DateTime.parse(textTime.data!);
        final realTime = await _moscowTime();
        expect(appTime, equals(realTime));
      });
    },
  );
}

Future<String> _moscowTime() async {
  await tz.initializeTimeZone();
  final moscow = tz.getLocation('Europe/Moscow');
  return tz.TZDateTime.now(moscow).toIso8601String();
}
