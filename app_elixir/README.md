# Lab1

Lab1 DevOps course [F23]

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)

## Project Overview

Simple CurrentTime elixir project

## Getting Started

Easy to start with the following guide:

### Prerequisites

- `asdf`

### Installation

```bash
$ asdf install
$ mix deps.get
```

### Usage

```bash
$ cd devops_web
$ mix phx.server
```

Access http://0.0.0.0:4000/time to get MSK time

# Devops

**TODO: Add description**

## Installation

If [available in Hex](https://hex.pm/docs/publish), the package can be installed
by adding `devops` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:devops, "~> 0.1.0"}
  ]
end
```

Documentation can be generated with [ExDoc](https://github.com/elixir-lang/ex_doc)
and published on [HexDocs](https://hexdocs.pm). Once published, the docs can
be found at <https://hexdocs.pm/devops>.

## Docker

### Run with docker:

```bash
$ docker run -p 4000:4000 -e SECRET_KEY_BASE='WPcE2F5vjA5X3XBE+QcK7OHMiAuPovP4e62Gsl0VFxRHvu+xS2AiQWY0H3Qz6Q3O' nikitosing/app_elixir
```

### Build an image:

```bash
$ docker build -t app_elixir .
```

### Run built image

```bash
$ docker run -p 4000:4000 -e SECRET_KEY_BASE='WPcE2F5vjA5X3XBE+QcK7OHMiAuPovP4e62Gsl0VFxRHvu+xS2AiQWY0H3Qz6Q3O' app_elixir  
```

### Pull the image

```bash
$ docker pull nikitosing/app_elixir
```
