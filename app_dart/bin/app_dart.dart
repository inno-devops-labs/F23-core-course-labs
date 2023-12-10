import 'package:app_dart/routes/time.dart' show timeRoutes;
import 'package:jaguar/jaguar.dart';

void main() async {
  final server = Jaguar();

  server.add(timeRoutes);
  server.staticFiles("/*", "./static");

  await server.serve(logRequests: true);
}
