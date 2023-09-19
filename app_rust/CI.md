# Best Practices

- Use an IDE plugin for help with syntax highlighting and linting of YAML files (YAML by Redhat for VSCode).
- Keep actions minimal and don’t install unnecessary dependencies.
- Use GitHub secrets when working with credentials or tokens.
- Use [GitHub actions’ default environment variables](https://docs.github.com/en/actions/learn-github-actions/environment-variables#default-environment-variables) when working with the **runner** file system.
- With DockerHub, it’s more secure to use a generated-token with only the necessary permissions instead of using the password.
- Optimize workflow running time by [caching dependencies](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows).
