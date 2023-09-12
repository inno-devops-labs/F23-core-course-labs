# Docker best practices

## Lightweight baseline

There are many images we can use as a baseline:
`python:X`, `python:X-slim`, `...slim-buster`, `alpine`.
Despite alpine is less than debian-based,
it is less error-prone to use the later one

## Least frequently changed layers on the top

Usually we change source code, and dependencies are fixed most of the time -
let's move it closer to baseline

## Fix dependencies

To have reproducible builds,
fix versions of dependencies for both `apt-get` and `pip`

## No root inside

Create a user, use it inside the images.
Also remove permissions to write and execute
sources for users other than `root` -
it can help to have same sources during process run (but if we use volumes...)

## Setup healthcheck

Processes should be observable,
so we can handle it - a way to achieve it is to setup probes
