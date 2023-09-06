class Now {
  final DateTime timestamp;

  Now(this.timestamp);

  Map<String, dynamic> toMap() {
    return {
      "timestamp": timestamp.toIso8601String().replaceAll("Z", ""),
    };
  }
}
