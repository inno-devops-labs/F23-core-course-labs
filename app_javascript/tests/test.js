const chai = require('chai')
const { expect } = chai
const { getRandomQuote } = require('../app')

describe('Random Quote Generator', () => {
  it('should return a random quote from the quotes array', () => {
    const quote = getRandomQuote()
    expect(quote).to.be.a('string')
  })
})