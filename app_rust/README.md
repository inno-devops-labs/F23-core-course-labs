![Rust CI](https://github.com/Asem-Abdelhady/core-course-labs/actions/workflows/app_rust.yaml/badge.svg)

# Time App

- Sample app that shows current time for DevOps course

## Used technology

- HTML, CSS, JS.
- Rust (packages: regex).
- Docker (images: alpine).

## Endpoints

```bash
$ flask routes
Endpoint            Methods  Rule
------------------  -------  -----------------------
home                GET      /
```

## Development

`Cargo` is used to install packages and make the binary:

```bash
cargo build --release
./target/release/web_Server
```

## Unit Tests

Unit tests are on the lib module following rust best paractice

```bash
cargo test
```

## Release

```bash
export DOCKERHUB_ID=<YOUR_DOCKERHUB_ID>
export APP_NAME=app_rust

# To build app image
docker build -t $DOCKERHUB_ID/$APP_NAME .

# Testing the built image locally (http://localhost:8080)
docker run -p5000:5000 $DOCKERHUB_ID/$APP_NAME

# Tag image with last commit SHA (and/or use semantic versioning)
docker tag $DOCKERHUB_ID/$APP_NAME $DOCKERHUB_ID/$APP_NAME:$(git rev-parse --short HEAD)

# Login and push image to dockerhub
docker login -u $DOCKERHUB_ID # Enter password/token when prompted
docker push $DOCKERHUB_ID/$APP_NAME --all-tags
```

## CI

- The workflow is done using Github actions
- The workflow includes:
  - buulding, testing and linting job
  - building and deploying image on dockerhub
  - checking security valnurabilities with Synk
- The workflow uses ubuntu as a base for every job
