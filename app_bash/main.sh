#!/bin/bash
HOST=$1
PORT=8000

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
    ncat -l -p "$PORT" -c "echo -e \"HTTP/1.1 200 OK\n\n \
    <html>\
    <h1>Is $HOST available?</h1>\
    $(nmap -p 80 "$HOST" | grep 'open' -q && echo '<h1 style="color:green">YES</h1>'\
    || echo '<h1 style="color:red">NO</h1>')\
    </html>\""
    echo "Responsed."
done
