import {app} from "./app";


app.listen(3000, () => {
    console.log('The application is listening on port 3000!');
})

process.on('SIGINT', function() {
  console.log( "\nGracefully shutting down from SIGINT (Ctrl-C)" );
  // some other closing procedures go here
  process.exit(0);
});