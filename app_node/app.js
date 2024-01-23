const http = require('http');

const server = http.createServer((req, res) => {
    // Generate a random number between 1 and 21
    const randomNumber = Math.floor(Math.random() * 21) + 1;

    // Set the response headers
    res.writeHead(200, { 'Content-Type': 'text/plain' });

    // Send the random number as the response
    res.end(`Random Number: ${randomNumber}\n`);
});

const port = 3000;
server.listen(port, '0.0.0.0', () => {
    console.log(`Server is running on http://localhost:${port}`);
});
