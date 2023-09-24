const app = require('./app');  // path to your app.js
const port = 3000;

app.listen(port, () => {
  console.log(`Web application is running at http://localhost:${port}`);
});
