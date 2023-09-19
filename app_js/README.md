# JS Web Application

This is a simple js web application developed using Svelte that displays the current time in Moscow.

## Overview

- [Project setup](#project-setup)
- [Compiles and minifies for production](#compiles-and-minifies-for-production)
- [Lints and fixes files](#lints-and-fixes-files)
- [Testing](#testing)
- [Docker](#docker)
- [Contributing](#contributing)

## Project setup

To run the project, you need to install the dependencies. To do this, run the following command:

- `npm install -D jsdom`
- `npm install --save-dev @testing-library/svelte`
- `npm install svelte svelte-loader axios moment`
- `npm install moment-timezone`
- `npm install @babel/core @babel/preset-env jest babel-jest svelte-jester -D`

After it you can run the project in development mode, run the following command:

> `npm run dev`

### Compiles and minifies for production

To build the project, run the following command:

> `npm run build`

After that, open your browser and visit the provided localhost URL to see the current time in Moscow

### Lints and fixes files

Linting is done automatically on commit. To run linting manually, run the following command:

> `npm run lint`

### Testing

To run unit tests, run the following command:

> `npm run test`

### Docker

First, you need to install docker on your machine. To do this, follow the instructions on the [official website](https://docs.docker.com/get-docker/).
After it you need to pull the image from docker hub. To do this, run the following command:

> `docker pull relisqu/svelte-app`

To run the project in docker, run the following command:

> `docker run -p 5173:5173 relisqu/svelte-app`

### Contributing

If you'd like to improve this project or report issues, please open an issue or submit a pull request.
