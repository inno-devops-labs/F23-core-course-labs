var http = require('http'); 

var server = http.createServer(function (req, res) {   
    if (req.url == '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' }); 
        let moscow_datetime_str = new Date().toLocaleString("en-US", { timeZone: "Europe/Moscow" });
        res.write('<html><body><p>Hello, User! Date and time are: '+ moscow_datetime_str +'.</p></body></html>');
        res.end();
    
    }
    else
        res.end('Invalid Request!');

});

server.listen(5000);

console.log('Node.js web server at port 5000 is running..')