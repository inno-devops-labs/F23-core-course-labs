#!/bin/sh

curl --fail -X GET http://localhost:80/time > /dev/null || return 1
