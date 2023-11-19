# Programmer Profile App

## Table of contents

- [Description](#description)
- [Pre-requirements](#pre-requirements)
- [Build](#build)
- [Pull](#pull)
- [Run](#run)
- [Project repository](#project-repository)
- [CI Workflow](#ci-workflow)
- [Unit Tests](#unit-tests)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creator](#creator)
- [Copyright and license](#copyright-and-license)

## Description

Simple web app to show programmer profile. At this moment applications shows only information from github.

Main page shows my github profile. It is possible to check any public github profile using endpoint
`/profile/get/{username}`.

Moreover, you can mount your volume folder to `/volume/` folder inside container. Now app uses this folder to save visits inside `visits` file. `/visits` endpoint returns this number.

## Pre-requirements

- Docker

## Build

To build docker container use the following command:

`docker build -t docker pull programmer-profile-asp-net .`

## Pull

It is possible to pull the container from docker hub. To do is use the following command:

`docker pull nabiull2020/programmer-profile-asp-net:latest`

## Run

To run the container use the following command:

`docker run -p 8000:80 nabiull2020/programmer-profile-asp-net:latest`

or if you built it manually:

`docker run -p 8000:80 programmer-profile-asp-net`

The application will then be accessible at http://localhost:8000/

## Project repository

```text
app_c#/
├── ProgrammerProfile.sln
├── C#.md
├── ProgrammerProfile/
│   ├── bin (folder with builds)
│   └── ... (Code files)
└── UnitTests/
    ├── bin (folder with builds)
    └── app_tests.py
```

## CI Workflow

Jobs:

1. **Build**

    - Setup .NET - setup .Net with version 6.0.x

    - Cache dependencies - use cache to store dependencies

    - Dependencies install

    - Vulnerability check - using Snyk to check for vulnerabilities

    - Vulnerability report - generate report of vulnerabilities

    - Linter

    - Tests

2. **Docker**

    - Login - login to docker hub

    - Build and Push - build docker image and push it to docker hub

I used Snyk in build stage in case to reduce dependencies installations.

## Unit Tests

You can find project with unit tests in `UnitTests` folder.

Run test using:

`dotnet test`

## Bugs and feature requests

Not found yet ;)

## Contributing

Not available at this moment

## Creator

<https://github.com/DamirNabiull>

## Copyright and license

Code and documentation copyright 2023 the authors.