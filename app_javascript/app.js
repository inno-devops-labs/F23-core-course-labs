const http = require('http')

const server = http.createServer(function (req, res) {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' })
    const moscowDatetimeStr = new Date().toLocaleString('en-US', { timeZone: 'Europe/Moscow' })
    res.write('<html><body><p>Hello, User! Date and time are: ' + moscowDatetimeStr + '.</p></body></html>')
    res.end()
  } else {
    res.end('Invalid Request!')
  }
})

module.exports = server
