FROM python:3.11.4

# Copy & install requirements first
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

# Set timezone
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add non-root user
RUN useradd app

USER app
WORKDIR /home/app
COPY . ./app_python

# Expose only needed port
EXPOSE 8080

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "app_python.main:app"]
