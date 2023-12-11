import 'package:app_dart/models/time.dart';
import 'package:jaguar/jaguar.dart';

final now = Route.get(
  "/api/time/now",
  (Context ctx) {
    return Response.json(
      Now(
        DateTime.now().toUtc().add(Duration(hours: 3)),
      ).toMap(),
    );
  },
);

final timeRoutes = [now];
