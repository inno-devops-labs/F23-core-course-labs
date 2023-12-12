# Metrics

## Prometheus

Calculating metrics in python application.

### Log Rotation

Log rotation for each service was specified in `docker-compose` file.

For best practices tag, max size of the file and driver type were specified.

### Memory Limits

Memory limits for each service were specified.

### Health Check

Healthcheck is implemented using `curl`.

Interval, Timeout and Start period for each service were specified.