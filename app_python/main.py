import datetime
import http.server
import socketserver


class TimeServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            moscow_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)  # Moscow is UTC + 3
            time_str = moscow_time.strftime('%Y-%m-%d %H:%M:%S')

            message = f'The current time in Moscow is {time_str} UTC+3.'
            self.wfile.write(message.encode())

            return


if __name__ == '__main__':
    PORT = 8008

    with socketserver.TCPServer(('', PORT), TimeServer) as httpd:
        print(f'Server started on port {PORT}')
        httpd.serve_forever()
