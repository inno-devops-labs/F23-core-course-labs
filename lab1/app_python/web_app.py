from flask import Flask, Response
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def home():
    html = """
    <html>
    <body>
        <h1 id="time">Current Time in Moscow: </h1>
        <script>
            function getTime(){
                var xhr = new XMLHttpRequest();
                xhr.open('GET', '/time');
                xhr.onload = function(){
                    if(xhr.status === 200){
                        document.getElementById('time').innerHTML = 'Current Time in Moscow: ' + xhr.responseText;
                    }
                };
                xhr.send();
            }
            getTime();
            setInterval(getTime, 1000);
        </script>
    </body>
    </html>
    """
    return Response(html)


@app.route('/time')
def time():
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H:%M:%S')
    return moscow_time


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
