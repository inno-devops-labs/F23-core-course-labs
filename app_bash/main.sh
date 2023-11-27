#!/bin/bash

source prometheus.bash

HOST="moodle.innopolis.university"
PORT=9000

if [[ "$HOST" == "" ]]; then
    echo "Please, specify host"
    exit 1
fi
echo "Host is $HOST"
if [[ "$PORT" == "" ]]; then
    echo "Please, specify port"
    exit 1
fi
echo "Running on port $PORT"

while true
do
    io::prometheus::NewGauge name=start_time help='When the run began'
    io::prometheus::PushAdd job=ncat instance='' gateway=http://pushgateway:9091

    ncat -l -p "$PORT" -c "echo -e \"HTTP/1.1 200 OK\n\n \
    <html>\
    <h1>Is $HOST available?</h1>\
    $(nmap -p 80 "$HOST" | grep 'open' -q && echo '<h1 style="color:green">YES</h1>'\
    || echo '<h1 style="color:red">NO</h1>')\
    </html>\""
    echo "Responsed."
    io::prometheus::NewGauge name=end_time help='When the run ended'
    io::prometheus::PushAdd job=ncat instance='' gateway=http://pushgateway:9091
done
