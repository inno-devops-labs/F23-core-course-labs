import express from 'express'
import path from 'path'
import { getMoscowTime } from './timezone'

const PORT = 4000
const app = express()

app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'pug')
app.use('/static', express.static(path.join(__dirname, 'static')))

app.get('/', (_req, res) => {
  const [date, time] = getMoscowTime()
  res.render('index', { date, time })
})

app.all('/*', (_req, res) => {
  res.redirect('/')
})

app.listen(PORT, () => {
  console.log(`app is listening on port ${PORT}`)
})
