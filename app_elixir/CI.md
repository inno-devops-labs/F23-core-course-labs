# Best Practices in Elixir CI Workflow

The "Elixir CI" workflow follows best practices for continuous integration (CI) and automation. Here's a detailed description of the best practices applied in this workflow:

## Trigger on Specific Events

The workflow is triggered by the `push` event, but it is further constrained to specific paths to ensure it runs only when changes are made to the `app_elixir/` directory or the workflow file itself.

```yaml
on:
  push:
    paths:
      - "app_elixir/**"
      - ".github/workflows/elixir.yml"
```

## Environment Variables

Environment variables are used to configure the CI environment. This includes setting the `MIX_ENV`, `OTP_VERSION`, and `ELIXIR_VERSION` variables, allowing for easy customization of the Elixir and OTP versions used in the build process.

```yaml
env:
  MIX_ENV: test
  OTP_VERSION: "25.3.2.3"
  ELIXIR_VERSION: "1.14.5"
```

## Parallel Jobs

The workflow defines multiple jobs (`build-and-cache`, `check_formatted`, `test`, and `docker`), allowing for parallel execution of tasks. This approach optimizes resource usage and reduces the overall workflow execution time.

```yaml
jobs:
  build-and-cache:
    # ...
  check_formatted:
    # ...
  test:
    # ...
  docker:
    # ...
```

## Caching Dependencies

Caching is implemented for Elixir and Mix dependencies to improve build performance. It caches dependencies based on the Elixir and OTP versions, MIX_ENV, and the hash of the `mix.lock` file.

```yaml
- name: Restore Mix Deps Cache
  uses: actions/cache@v2
  id: deps-cache
  with:
    path: |
      deps
      _build
    key: ${{ runner.os }}-${{ env.ELIXIR_VERSION }}-${{ env.OTP_VERSION }}-${{ env.MIX_ENV }}-deps-${{ hashFiles('mix.lock') }}
    restore-keys: |
      ${{ runner.os }}-${{ env.ELIXIR_VERSION }}-${{ env.OTP_VERSION }}-${{ env.MIX_ENV }}-deps-
```

## Automated Formatting Checks

The workflow includes a step (`check_formatted`) for code formatting checks. It uses Elixir's `mix format --check-formatted` to ensure that the code adheres to the specified formatting guidelines.

```yaml
- name: Code formatting checks
  run: |
    mix deps.get
    mix format --check-formatted
```

## Automated Testing

The workflow includes a step (`test`) for running Elixir tests using `mix test`. This ensures that unit tests are executed, and any test failures will prevent the workflow from proceeding further.

```yaml
- name: mix test
  run: |
    mix deps.get
    mix test
```

## Docker Image Building and Publishing

The workflow handles Docker image building and publishing, following best practices for containerized applications. It logs in to Docker Hub securely using GitHub secrets and pushes the Docker image to a repository.

```yaml
- name: Cache Docker layers
  uses: actions/cache@v2
  with:
    path: ~/.docker
    key: ${{ runner.os }}-docker-${{ hashFiles('Dockerfile') }}
    restore-keys: |
      ${{ runner.os }}-docker-

- name: Login to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}

- name: Build and Push Docker Image
  run: |
    docker build -t nikitosing/app_elixir:latest .
    docker push nikitosing/app_elixir:latest
```
