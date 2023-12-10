const chai = require('chai')
const chaiHttp = require('chai-http')
const server = require('../app')

chai.use(chaiHttp)
const expect = chai.expect

describe('HTTP Server', function () {
  let app

  before(function () {
    app = server.listen(5000)
  })

  after(function () {
    app.close()
  })

  it('should respond with "Hello, User!" on the root URL', function (done) {
    chai
      .request(app)
      .get('/')
      .end(function (err, res) {
        expect(res).to.have.status(200)
        expect(res).to.be.html
        expect(res.text).to.include('Hello, User!')
        done()
      })
  })

  it('should respond with "Invalid Request!" on an invalid URL', function (done) {
    chai
      .request(app)
      .get('/invalid')
      .end(function (err, res) {
        expect(res.text).to.equal('Invalid Request!')
        done()
      })
  })
})
