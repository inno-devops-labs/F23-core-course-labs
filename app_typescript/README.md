![app_typescript](https://github.com/DaniilOkrug/dev-ops-inno/workflows/Typescript%20CI/badge.svg)

# Typescript Web Application Development

Author: Daniil Okrug

## Overview

The application displays USD exchange rates. In this project I used NextJS because it has built-in support for SSR/SSG, Typescript and follows modern standards for building web application architecture

## Structure

The /src folder contains the source code of the project in the Typescript language.

External files include NextJS configurations, linters, etc.

The /public folder contains the original HTML page and files necessary for successful rendering of the application in the browser

## Testing

You can run the application with npm run dev to test it. You should install dependencies with the npm ci command before running the application.

## Docker

The project uses Docker with three build stages.

The first stage is needed to install the project dependencies. The second stage builds the project. The third stage copies the necessary files with limited user rights and launches the project.

### Build

Local image building: \
`docker build -t app_ts:lab2 .` \
`app_ts:lab2` - can be any name you like for the image

### Docker Hub

Pull image from Docker Hub \
`docker pull bellissimo/devops-inno-daniil-okrug:lab2_ts`

### Run

Running localy builded image: \
`docker run -d -p 3000:3000 app_ts:lab2`

Running image from Docker Hub: \
`docker run -d -p 3000:3000 bellissimo/devops-inno-daniil-okrug:lab2_ts`
