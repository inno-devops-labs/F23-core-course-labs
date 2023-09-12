# Express.js web application

This web application was developed using the Express.js framework, because it is a minimal and flexible Node.js web application framework. It provides a robust set of features for web and mobile applications.

## Why Express.js?

- **simplicity**: Express.js provides a simple interface for creating server-side applications with Node.js,
- **community support**: given its popularity, there are numerous resources, plugins, available for Express.js,
- **performance**: being a minimalistic framework, Express.js is lightweight and offers good performance for web applications.

## Usage:

Upon navigating to the application's homepage, users are greeted with the message "Hello, Express.js World!".

## Running the application:

Ensure you have Node.js and Express.js installed.

Navigate to the application directory and run: `node app.js`


Visit http://localhost:3000 to view the application.

## Docker:

### Building the Docker image:
```bash
docker build -t purfreak/lab2_devops:latest-js .
```

### Pulling the Docker image:
```bash
docker pull purfreak/lab2_devops:latest-js
```

### Running the Docker image:
```bash
docker run -d -p purfreak/lab2_devops:latest-js
```