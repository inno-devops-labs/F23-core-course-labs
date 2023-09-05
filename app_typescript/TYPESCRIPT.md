## This application is written using Typescript programming language

### In order to run application you need
    - have Node.js installed https://nodejs.org/ru
    - go to `app_typescript` directory
    - perform `npm ci`
    - run `npm run dev` or `npm run run`. The only difference is that the 1st command will be watching on changes in source files
    - Application will be running on localhost:4000

For this app I decided to use Express.js (https://expressjs.com/) framework for its simplicity. It is not as big as `Nest.js` for example, but it has all necessary features to complete this task.

This application does actually the same thing as the first one. It responses with HTML document on '/' url, which is created using 'pug' template engine (https://pugjs.org). Then this HTML document requests css file, which is served by Express.js.

The moscow time is computed as UTC time + 3 hours offset