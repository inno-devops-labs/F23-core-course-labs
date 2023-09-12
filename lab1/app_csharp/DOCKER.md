# Docker Best Practices

1. **Non-root User**: We created a non-root user in the Dockerfile to enhance security. Running applications as a non-root user can prevent malicious processes from gaining root privileges.

2. **Minimal Base Image**: We used `mcr.microsoft.com/dotnet/aspnet:7.0` as our base image to keep the image small and reduce the attack surface.

3. **No Secrets in dockerfile**: We avoided the use secrets in dockerfile config.

4. **Use COPY instead of ADD**: We used `COPY` instead of `ADD` to copy files into our Docker image. `COPY` is more transparent and straightforward than `ADD`.
