# Joke Display Web Application

This simple web application fetches jokes from the [JokeAPI](https://v2.jokeapi.dev/)
and displays them in the center of the screen. You can press the "Another Joke"
button to get a new joke. If a "joke" property is available in the response,
it will be displayed. If the "joke" property is null, it will display the "setup"
and "delivery" properties as a complete joke.

## Installation

To run this application locally, follow these steps:

1. Make sure you have [Node.js](https://nodejs.org/) installed on your computer.

2. Navigate to the project directory:

   ```bash
   cd app_js
   ```

3. Start a simple HTTP server using Node.js:

   ```bash
   node server.js
   ```

4. Open your web browser and visit [http://localhost:3000](http://localhost:3000) to use the application.

### Build and run with Docker
1. Clone the repository. Go to `app_js` folder
2. Build an image

   ```
   docker build -t maksktl/app_js:latest .
   ```

   or pull an image from docker hub

   ```
   docker pull maksktl/app_js:latest
   ```
3. Create and run a container from the built image
   ```
   docker run -d -p 3000:3000 maksktl/app_js
   ```
4. Access the website `localhost:3000`

## Usage

- When you open the application in your web browser, you will initially see "Loading..." in the center of the screen.

- Press the "Another Joke" button to fetch and display a new joke from the JokeAPI.

- If the "joke" property is available in the response, it will be displayed.

- If the "joke" property is null, it will display the "setup" and "delivery" properties as a complete joke.

- If there is an error in fetching the joke, it will display an error message.

## Technologies Used

- JavaScript
- HTML
- CSS
- XMLHttpRequest
- Node.js (for serving the application)
- Docker
- Docker linter: hadolint
## Author

- Name: Maxim Matantsev
- Email: m.matantsev@innopolis.university
