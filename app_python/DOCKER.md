# Docker best practices

1. Created non-root user for running app as it enhances safety.
2. Install only what need in runtime (no poetry test deps).
3. Used [hadolint](https://github.com/hadolint/hadolint) as linter for dockefiles.
4. Added `.dockerignore` to not include poetry env in project and other.
5. Exposed only used port (8080) in order to reduce possible attack range.
6. Used [official python docker image](https://hub.docker.com/_/python).
