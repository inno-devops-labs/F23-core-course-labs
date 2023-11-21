// app.js
const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();

const filePath = '/data/visitors.json';
const defaultContent = { visitors: 0 };


function readAndUpdateVisitors() {
  fs.readFile(filePath, 'utf8', (readErr, data) => {
  console.error('read start1', data);
    if (readErr) {
      console.error('Error reading the file:', readErr);
      return;
    }
    try {
      const jsonData = JSON.parse(data);
      let ret_vis = jsonData.visitors;
      let numberOfVisitors = ret_vis;
      numberOfVisitors++;
      console.log('Number of visitors:', numberOfVisitors);
      jsonData.visitors = numberOfVisitors;
      fs.writeFile(filePath, JSON.stringify(jsonData), 'utf8', (writeErr) => {
        if (writeErr) {
          console.error('Error writing to the file:', writeErr);
          return;
        }
        console.log('File updated with new number of visitors:', numberOfVisitors);
      });
    } catch (jsonError) {
      console.error('Error parsing JSON:', jsonError);
    }
  });
  return ret_vis;
}

app.get('/', (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' })
    readAndUpdateVisitors();
    const moscowDatetimeStr = new Date().toLocaleString('en-US', { timeZone: 'Europe/Moscow' })
    res.write('<html><body><p>Hello, User! Date and time are: ' + moscowDatetimeStr + '.</p></body></html>')
    res.end()
  } else {
    res.end('Invalid Request!')
  }
});

app.get('/visits', (req, res) => {
  if (req.url === '/visits') {
    res.writeHead(200, { 'Content-Type': 'text/html' })
    res.write('<html><body><p>Visitors: ' + readAndUpdateVisitors() + '.</p></body></html>')
    res.end()
  } else {
    res.end('Invalid Request!')
  }
});

module.exports = app;