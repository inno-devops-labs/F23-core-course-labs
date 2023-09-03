# Bash Web Application
## Overview
This web application checks if the host is available(can be pinged) or not.
## Dependency installation
Nmap package is required, install it using your package manager(you would need `ncat` and `nping` from nmap).
## Usage
First argument is target host, second is port to listen.

Example:

```
./main.sh moodle.innopolis.university 8000
```
## Test
```
./test.sh
```