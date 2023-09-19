FROM python:3.8

RUN useradd -ms /bin/bash myuser
RUN mkdir /myuser-dir && chown -R myuser /myuser-dir
RUN chown -R myuser /myuser-dir
USER myuser

COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
ENTRYPOINT [ "python", "run.py"]