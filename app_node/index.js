const express = require('express')

const app = express()
const port = process.env.APP_NODE_PORT ?? 8000

app.get('/', (req, res) => {
    res.send(new Date().toLocaleString('en-US', { timeZone: 'Europe/Moscow', timeZoneName: 'long' }))
})

app.listen(port, () => console.log(`Listening on port ${port}`))
