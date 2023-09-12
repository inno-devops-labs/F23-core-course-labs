const express = require('express');
const app = express();

app.get('/', (req, res) => {
    const moscowTime = new Date().toLocaleTimeString('en-US', { timeZone: 'Europe/Moscow' });
    res.send(`Current time in Moscow: ${moscowTime}`);
});

module.exports = app;
