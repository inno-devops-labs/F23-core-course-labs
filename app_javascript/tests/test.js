const chai = require('chai')
const { expect } = chai
const request = require('supertest')

const myVariables = require('../app.js')

describe('Random Quote Generator', () => {
  // Test for testing if function getRandomQuote() returns a string object
  it('should return a random quote from the quotes array', () => {
    const quote = myVariables.getRandomQuote()
    expect(quote).to.be.a('string')
  })

  // Test for testing if GET request on /get-random-quote responds
  // with status code 200 and returns string object
  it('should return a JSON response with a random quote on GET /get-quote', async () => {
    const response = await request(myVariables.app).get('/get-quote')
    expect(response.status).to.equal(200)
    expect(response.body).to.have.property('quote').that.is.a('string')
  })

  // Test for testing if app shutdowns gracefully using ctrl+c and returns status code 500
  it('should handle SIGINT gracefully', (done) => {
    const server = myVariables.app.listen(0, () => {
      const requestPromise = request(myVariables.app).get('/get-quote')

      process.kill(process.pid, 'SIGINT')
      server.close(done)

      requestPromise.then((response) => {
        expect(response.status).to.equal(500)
      })
    })
  })
})
