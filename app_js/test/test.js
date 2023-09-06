const request = require('supertest');
const chai = require('chai');
const app = require('../app');

const expect = chai.expect;

describe('GET /', () => {
  it('should return Hello, Express.js World!', (done) => {
    request(app)
      .get('/')
      .end((err, res) => {
        expect(res.statusCode).to.equal(200);
        expect(res.text).to.equal('Hello, Express.js World!');
        done();
      });
  });
});
