import datetime
import http.server
import socketserver
import logging
from prometheus_client import start_http_server, Counter, generate_latest

log = logging.getLogger(__name__)

REQUEST_COUNTER = Counter('http_requests_total',
                          'Total number of HTTP requests')


class TimeServer(http.server.SimpleHTTPRequestHandler):
    def log_request(self, code='-', size='-'):
        REQUEST_COUNTER.inc()

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            moscow_time = datetime.datetime.utcnow()
            moscow_time += datetime.timedelta(hours=3)
            time_str = moscow_time.strftime('%Y-%m-%d %H:%M:%S')

            message = f'The current time in Moscow is {time_str} UTC+3.'
            self.wfile.write(message.encode())

            return
        elif self.path == '/healthcheck':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("Ok".encode())
        elif self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(generate_latest())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Not Found".encode())


if __name__ == '__main__':
    PORT = 8008

    with socketserver.TCPServer(('', PORT), TimeServer) as httpd:
        log.info(f'Server started on port {PORT}')
        try:
            start_http_server(8080)
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.shutdown()
        except Exception as e:
            print(e)
            httpd.shutdown()
