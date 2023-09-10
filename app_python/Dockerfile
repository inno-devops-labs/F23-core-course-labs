FROM python:3

EXPOSE 7098

RUN useradd -ms /bin/bash python_runner
USER python_runner
ENV PATH="/home/python_runner/.local/bin:${PATH}"
WORKDIR /home/python_runner/python/src/app

COPY requirements/requirements.txt ./

RUN pip install --user --no-cache-dir -r requirements.txt

COPY . ./app_python

CMD ["python", "-m",  "app_python.src.main"]