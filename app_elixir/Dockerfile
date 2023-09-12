FROM hexpm/elixir:1.14.5-erlang-25.3.2.4-alpine-3.18.2 AS builder

WORKDIR /app_elixir

# set build ENV
ENV MIX_ENV=prod
ENV PORT=4000

COPY lib ./lib
COPY config ./config
COPY rel ./rel
COPY *.exs ./
COPY mix.lock ./

RUN mix local.hex --force
RUN mix do deps.get, local.rebar --force, deps.compile

RUN mix compile
RUN mix release

RUN mkdir -p /opt/release
RUN mix release
RUN mv _build/${MIX_ENV}/rel/devops_web /opt/release

###
FROM hexpm/elixir:1.14.5-erlang-25.3.2.4-alpine-3.18.2

ARG RELEASE_VERSION=0.0.1
ENV RELEASE_VERSION=${RELEASE_VERSION}

WORKDIR /app

COPY --from=builder /opt/release/devops_web .

# Add new non-root user
RUN adduser -D defaultuser

# Use this user to make container root-less
USER defaultuser

ENTRYPOINT ["bin/devops_web", "start"]