FROM python:3.10

COPY ./ /proj

RUN useradd -ms /bin/bash appUser

WORKDIR /proj

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip3 install poetry
RUN poetry config virtualenvs.create false 
RUN poetry install

RUN mkdir /proj/data && chown appUser /proj/data
VOLUME /proj/data

USER appUser

EXPOSE 8080

ENTRYPOINT ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "8080", "src.app:app"]
