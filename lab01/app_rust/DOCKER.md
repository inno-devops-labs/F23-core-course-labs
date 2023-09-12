# Docker best practices

## Lightweight baseline

There are many images we can use as a baseline:
`rust:X`, `rust:X-slim-buster`, `scratch`, `distroless`.

For simplicity I don't use `musl` and static linking - therefore I prefer `rust:slim-buster`

## Least frequently changed layers on the top

Usually we change source code, and dependencies are fixed most of the time -
let's move it closer to baseline

## Fix dependencies

To have reproducible builds,
fix versions of dependencies for both `apt-get` and `cargo`

## No root inside

Create a user, use it inside the images.
Also remove permissions to write to the
binary for users other than `root` -
it can help to have same sources during process run (but if we use volumes or change entrypoint/cmd...)

## Setup healthcheck

Processes should be observable,
so we can handle it - a way to achieve it is to setup probes
