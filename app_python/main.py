import datetime
import http.server
import socketserver
import logging

log = logging.getLogger(__name__)

class TimeServer(http.server.SimpleHTTPRequestHandler):
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


if __name__ == '__main__':
    PORT = 8008

    with socketserver.TCPServer(('', PORT), TimeServer) as httpd:
        log.info(f'Server started on port {PORT}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.shutdown()
        except Exception as e:
            print(e)
            httpd.shutdown()
