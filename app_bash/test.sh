#!/bin/bash
set -m

test_base() {
    ./main.sh "$1" &
    sleep 1
    curl http://localhost:8000 --http0.9 | grep "$2"
}

test_yes () {
    test_base google.com YES
}

test_no () {
    test_base NO_WAY_THIS_HOST_EXISTS NO
}

( test_yes &> /dev/null) && echo "test_yes success" || echo "test_yes failed"; killall main.sh ncat &> /dev/null
( test_no &> /dev/null) && echo "test_no success" || echo "test_no failed"; killall main.sh ncat &> /dev/null
exit 0