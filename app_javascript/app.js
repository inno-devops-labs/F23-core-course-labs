const express = require('express')
const app = express()
const path = require('path')

module.exports = {
  getRandomQuote
}

app.use(express.static(path.join(__dirname, 'public')))

const quotes = [
  'Do the small stuff. A consistent little will earn you a lot.',
  'Innovation distinguishes between a leader and a follower. - SteYou never know who is the killer and when he will attack you, he could take a lot of faces and bodies.ve Jobs',
  'A little conflict can create a lot of creativity.',
  'Problems are not stop signs; they are guidelines.',
  'Remember that guy that gave up? Neither does anyone else.',
  'When you come to the edge of all that you know, you must believe one of two things: There will be ground to stand. Or you will grow wings to fly.',
  "It's better to be in the arena, getting stomped by a bull, than to be up in the stands or out in the parking lot.",
  "Success isn't permanent and failure isn't fatal; it's the courage to continue that counts.",
  "Courage doesn't always roar. Sometimes courage is the little voice at the end of the day that says I'll try again tomorrow.",
  "You shouldn't focus on why you can't do something, which is what most people do. You should focus on why perhaps you can, and be one of the exceptions.",
  "There's nothing wrong or evil about having a bad day. There's everything wrong with making others have to have it with you.",
  'Some days you tame the tiger. And some days the tiger has you for lunch.',
  "You make mistakes. Mistakes don't make you.",
  'Most of the important things in the world have been accomplished by people who have kept on trying when there seemed to be no hope at all.',
  "Many of life's failures are people who did not realize how close they were to success when they gave up.",
  "It's just a bad day. Not a bad life.",
  'Life is short. Smile while you still have teeth.',
  "Don't be discouraged. It's often the last key in the bunch that opens the lock.",
  "No one is going to hand me success. I must go out and get it myself. That's why I'm here. To dominate. To conquer. Both the world and myself.",
  'Every strike brings me closer to the next home run.',
  "The happiest people don't necessarily have the best of everything, they just make the best out of everything that comes their way.",
  'What lies behind you and what lies in front of you pales in comparison to what lies inside of you.',
  'Pain is temporary. Quitting lasts forever.',
  'You yourself, as much as anybody in the entire universe, deserve your love and affection.',
  'The only time you fail is when you fall down and stay down.',
  'Count your age by friends, not years. Count your life by smiles, not tears.',
  'Tough times never last, but tough people do.',
  'For every minute you are angry you lose 60 seconds of happiness.',
  "Being happy doesn't mean you're perfect. It just means you've decided to look beyond the imperfections.",
  "Every day may not be good, but there's something good in every day."
]

function getRandomQuote () {
  const randomIndex = Math.floor(Math.random() * quotes.length)
  return quotes[randomIndex]
}

app.get('/get-quote', (req, res) => {
  const randomQuote = getRandomQuote()
  res.json({ quote: randomQuote })
})

const port = process.env.PORT || 3000
const server = app.listen(port, () => {
  console.log(`Server is running on port ${port}`)
})

process.on('SIGINT', () => {
  console.log('Received SIGINT. Shutting down gracefully...')

  server.close(() => {
    console.log('Server has been gracefully stopped.')
    process.exit(0)
  })
})
