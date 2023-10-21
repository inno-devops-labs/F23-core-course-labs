// app.js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' })
    const moscowDatetimeStr = new Date().toLocaleString('en-US', { timeZone: 'Europe/Moscow' })
    res.write('<html><body><p>Hello, User! Date and time are: ' + moscowDatetimeStr + '.</p></body></html>')
    res.end()
  } else {
    res.end('Invalid Request!')
  }
});

module.exports = app;