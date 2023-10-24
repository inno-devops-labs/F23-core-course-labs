FROM elixir:1.14.5

RUN addgroup --system app && adduser --system app -gecos app
USER app
ENV PATH /home/app/.local/bin:${PATH}
ENV MIX_ENV=prod

WORKDIR /app

COPY ./mix.exs ./mix.lock /app/
COPY ./config /app/config
COPY ./lib /app/lib

RUN mix local.hex --force
RUN mix local.rebar --force
RUN mix deps.get
RUN mix compile

EXPOSE 4000

CMD ["mix", "phx.server"]