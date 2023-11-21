import express from "express";
import fs from 'fs';
/* eslint-disable */
const jester: any = require('jester-jokes');


export const app = express();

app.get('/', (req, res) => {
    const joke = jester.getJoke();
    res.send({joke});
})

const path = 'data/visits';

app.get('/visits', (req, res) => {
    let visits = 0;
    try {
        visits = parseInt(fs.readFileSync(path, 'utf8'));
        if (isNaN(visits)) {
            visits = 0;
        }
    } catch (err) {
        console.error(err)
    }
    visits++;
    fs.writeFileSync(path, visits.toString());
    res.send({visits});
})