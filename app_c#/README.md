# Programmer Profile App

## Table of contents

- [Description](#description)
- [Pre-requirements](#pre-requirements)
- [Build](#build)
- [Pull](#pull)
- [Run](#run)
- [Project repository](#project-repository)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creator](#creator)
- [Copyright and license](#copyright-and-license)

## Description

Simple web app to show programmer profile. At this moment applications shows only information from github.

Main page shows my github profile. It is possible to check any public github profile using endpoint
`/profile/get/{username}`.

## Pre-requirements

- Docker

## Build

To build docker container use the following command:

`docker build -t docker pull programmer-profile-asp-net .`

## Pull

It is possible to pull the container from docker hub. To do is use the following command:

`docker pull nabiull2020/programmer-profile-asp-net:1.0.0`

## Run

To run the container use the following command:

`docker run -p 8000:80 nabiull2020/programmer-profile-asp-net:1.0.0`

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

## Bugs and feature requests

Not found yet ;)

## Contributing

Not available at this moment

## Creator

<https://github.com/DamirNabiull>

## Copyright and license

Code and documentation copyright 2023 the authors.