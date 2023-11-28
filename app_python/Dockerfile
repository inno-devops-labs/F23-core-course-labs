FROM python:3.11-alpine3.18 as staging

EXPOSE 80
ARG projdir=/proj
ARG appdir=${projdir}/app
ARG appuser=appuser

WORKDIR ${projdir}
COPY . ${projdir}
COPY healthcheck.sh /bin/healthcheck
RUN \
    adduser -D -u 1001 ${appuser} &&\
    mkdir /appdata && chown -R ${appuser} /appdata &&\
    chmod 755 ${projdir} &&\
    pip3 install --no-cache-dir -r requirements.txt &&\
    apk add curl=8.4.0-r0 --no-cache

FROM staging as testing
RUN \
    apk add make=4.4.1-r1 --no-cache
# while running tests, switch to production user to make sure no permission errors
USER ${appuser}
RUN \
    make lint &&\
    make test

FROM staging as production
# cleanup and hardening
RUN \
    rm -f Makefile requirements.txt
WORKDIR app
USER ${appuser}
CMD ["python3", "-u", "main.py", "0.0.0.0", "80"]