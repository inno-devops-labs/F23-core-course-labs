# Moscow Time Web App

## Table of contents

- [Description](#description)
- [Pre-requirements](#pre-requirements)
- [Quick start](#quick-start)
- [Project repository](#project-repository)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creator](#creator)
- [Copyright and license](#copyright-and-license)

## Description

Simple web app to fetch current time in Moscow.

## Pre-requirements

- Python 3.11
- Poetry

## Getting started

Install dependencies

```bash
poetry install
```

Run application

```bash
gunicorn main:app
```

## Miscellaneous

Run linter

```bash
ruff main.py
```

Run tests

```bash
pytest
```
