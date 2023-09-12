FROM python:3.11.4-slim-buster

WORKDIR /app_python

COPY requirements.txt requirements.txt
RUN apt-get update && \
    apt-get --no-install-recommends install -y curl=7.64.0-4+deb10u6 && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

COPY main.py main.py

RUN chmod a-wx main.py && useradd -ms /bin/bash devuser
USER devuser

EXPOSE 8000

HEALTHCHECK CMD curl -f localhost:8000/health || exit 1

ENTRYPOINT ["python"]
CMD ["main.py"]
