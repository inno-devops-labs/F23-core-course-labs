const http = require('http');
const app = require('./app'); // Import the app logic from another file
const promBundle = require('express-prom-bundle');

// Create a Prometheus metrics bundle using express-prom-bundle
const metricsMiddleware = promBundle({
  includeMethod: true,
  includePath: true,
});

app.use(metricsMiddleware);

const server = http.createServer(app);

const PORT = process.env.PORT || 5000;

server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});