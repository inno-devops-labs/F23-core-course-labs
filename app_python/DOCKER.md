Image: https://hub.docker.com/r/vlasovegorl/devops-python-app

- No root access, even with --privileged flag, to prevent exploitation.
- Dependency management ensures minimal layers and avoids unnecessary layer production.
- Minimal memory usage due to minimized number of layers.
- Poetry cache is removed to keep the image clean.
- Exact version of the base image is used to avoid unexpected behavior caused by version bumps.
