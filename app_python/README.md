# Lab1
![workflow](https://github.com/nikitosing/core-course-labs/actions/workflows/python.yml/badge.svg)

Lab1 DevOps course [F23]

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Unit testing](#unit-testing)

## Project Overview

Simple CurrentTime python project

## Getting Started

Easy to start with the following guide:

### Prerequisites

- `python 3.10+`

### Installation

```bash
$ git clone https://github.com/nikitosing/core-course-labs.git
$ cd core-course-labs
$ pip install -r requirements.txt
```

## Usage

```bash
$ flask run --host=0.0.0.0 --port=80
```

Access http://0.0.0.0/time to get MSK time

## Docker

### Run with docker:

```bash
$ docker run -p 80:80 nikitosing/app_python
```

### Build an image:

```bash
$ docker build -t app_python --build-arg port=80 .
```

### Run built image

```bash
$ docker run -p 80:80 app_python
```

### Pull the image

```bash
$ docker pull nikitosing/app_python
```

## Unit testing

To run tests:

```bash
$ pytest
```

## Endpoints

- `/visits` - return request count, which saved in `/app/visits/visits`