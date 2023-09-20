const chai = require('chai');
const chaiHttp = require('chai-http');
const http = require('http');
const expect = chai.expect;

chai.use(chaiHttp);

describe('Random Number Server', () => {
    let server;

    before((done) => {
        // Create and start the server before running tests
        server = http.createServer((req, res) => {
            const randomNumber = Math.floor(Math.random() * 21) + 1;
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end(`Random Number: ${randomNumber}\n`);
        });
        const port = 3000;
        server.listen(port, () => {
            console.log(`Server is running on http://localhost:${port}`);
            done();
        });
    });

    after(() => {
        // Close the server after all tests have run
        server.close();
    });

    it('should generate a random number between 1 and 21 exactly once', (done) => {
        chai.request(server)
            .get('/')
            .end((err, res) => {
                expect(err).to.be.null;
                expect(res).to.have.status(200);
                const randomNumber = parseInt(res.text.split(' ')[2]);
                expect(randomNumber).to.be.within(1, 21);
                done();
            });
    });
});
