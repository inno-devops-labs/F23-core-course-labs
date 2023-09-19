# Node.js Web Application Project: Random Quote Generator

## Description

This project aims to develop a Node.js web application that displays random quotes to users each time they press the button. The application provides an engaging and inspirational experience for users by presenting them with thought-provoking quotes. It doesn't use any databases, keeping the implementation simple and lightweight.

## Table of Contents

- [Project Name](#project-name)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Project Structure](#project-structure)
  - [License](#license)
  - [Author](#author)

## Installation

To run this Node.js web application on your local machine, follow these steps:

```bash
# Clone the repository
git clone https://github.com/Q-Tify/core-course-labs-devops.git

# Change to the project directory
cd core-course-labs-devops
cd app_javascript

# Install Dependencies:
npm install

# Start the Application:
node app.js

# Access the Application
Open a web browser and navigate to http://localhost:3000 to use the Random Quote Generator.

```

## Usage
Upon accessing the application in your web browser, you will see a "Get New Quote" button. Clicking this button will display a random quote on the page.

## Features
- Displays random quotes to users.
- User-friendly web interface.
- No database required, quotes are selected from a predefined list.
- Simple and responsive design for various devices.
- Provides users with inspirational and thought-provoking content.

## Technologies Used
- Node.js: The core runtime environment for building server-side applications.
- Express.js: A web application framework for Node.js used to handle HTTP requests and routes.
- HTML/CSS: Frontend design and structure using HTML and CSS.
- JavaScript: Used for client-side interactivity and fetching random quotes from the server.
- Docker: Containerization technology used to package and deploy the application in a consistent and isolated environment, ensuring portability and ease of deployment across various platforms and environments.

## Project Structure

The project structure is organized as follows:
- public/: Directory for static assets (HTML, CSS, JS).
- css/: Directory for CSS stylesheets.
- style.css: Stylesheet for the web application.
- index.html: The HTML template for the web page.
- js/: Directory for client-side JavaScript.
- main.js: Handles client-side interactions and fetches quotes.
- app.js: The main Node.js application file that sets up the Express.js server.
- tests/: Directory for tests.
- README.md: Project documentation file.
- JAVASCRIPT.md: Best practices documentation file.
- LICENSE: The license information for this project.
- .dockerignore: File specifying which files and directories should be ignored when creating a Docker image, ensuring only necessary files are included.
- Dockerfile: The Dockerfile that defines how the Docker image for the application should be built.
- Docker.md: Documentation file providing instructions and best practices for using Docker in the project.

## License
This project is licensed under the MIT License.

## Author
Arseniy Rubtsov

<br>

# Docker section
This project includes a Dockerfile that allows you to containerize the Node.

## This particular case
```
git clone https://github.com/Q-Tify/core-course-labs-devops/tree/lab2
cd app_javascript
docker build -t arseniy5443/randomquote:latest .
docker run -p 80:3000 --rm arseniy5443/randomquote:latest

docker login
docker push arseniy5443/randomquote:latest

docker pull arseniy5443/randomquote
```

## How to build docker image?
```
docker build -t [image name]:[image tag] [path to dockerfile]
```

## How to run docker container?
```
docker run -p [local port]:[docker port] --rm [image name]:[image tag]

docker run -d -p [local port]:[docker port] --rm --name [container name] [image name]:[image tag]

docker start [container name]
docker stop [container name]
```

Possible to add ENV:
```
docker run -p [local port]:[docker port] -e PORT=80 [image name]:[image tag]
```
Or to take it from file, create dir config and there .env file, put there all variables and use command:
```
docker run -p [local port]:[docker port] --env-file ./config/.env [image name]:[image tag]
```

## How to upload to docker hub?

```
docker login
```
It is important that the name of the image should contain docker username + / + image name:
```
docker push [docker username]/[image name]:[image tag]
```

To rename image:
```
docker tag [old image] [docker username]/[new image]
```

## How to download image from docker hub?
```
docker pull [image name]
```

<br><br>

## How to delete all stopped containers?
```
docker container prune
```

## How to delete all images?
```
docker image prune -a
```

## How to see all containers?
```
docker ps -a
```

## How to see all images?
```
docker images
```

## How to delete:
- all stopped containers
- all networks not used by at least one container
- all dangling images
- all dangling build cache
```
docker system prune
```

<br>

# Unit Tests
To run the tests for this application you can use precommit, with linting (changes should be staged) the app will be tested:
```
npm run precommit
```
Or you can run test separately with command:
```
npm run test
```