const request = require('supertest');
const chai = require('chai');
const app = require('../app');

const expect = chai.expect;

describe('GET /', function() {
  this.timeout(5000);

  it('should return varying Moscow times with request delay', async function() {
    const response1 = await request(app).get('/');
    expect(response1.statusCode).to.equal(200);
    expect(response1.text).to.include('Current time in Moscow');
    const time1 = response1.text;

    return new Promise((resolve) => {
      // Delay of 2 seconds
      setTimeout(async () => {
        // Second request after delay
        const response2 = await request(app).get('/');
        expect(response2.statusCode).to.equal(200);
        expect(response2.text).to.include('Current time in Moscow');
        const time2 = response2.text;

        expect(time1).to.not.equal(time2);

        resolve();
      }, 2000);
    });
  });
});
