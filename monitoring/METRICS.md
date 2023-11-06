# Monitoring lab

## Targets discovery

![containers](static/containers2.png)

## Service configuration

Now we store at most 1Kb file and 2 files with container log for each service

For applications I set 100Mb memory limit each, for infrastrcture - 1Gb

## Application-scraped metrics

![python-prometheus](static/python-prometheus.png)
![rust-prometheus](static/rust-prometheus.png)

## Healtchecks

![healtchecks](static/healthchecks.png)
