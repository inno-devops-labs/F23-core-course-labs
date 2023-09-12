FROM rust:1.72-slim-buster as builder

RUN cargo new app_rust

WORKDIR /app_rust

COPY Cargo.toml Cargo.lock ./
RUN cargo build --release
COPY src src
ARG RUSTFLAGS=''
RUN RUSTFLAGS=${RUSTFLAGS} cargo install --path .

FROM rust:1.72-slim-buster

RUN apt-get update && \
   apt-get --no-install-recommends install -y curl libc-bin libc6 && \
   rm -rf /var/lib/apt/lists/*

COPY --from=builder /app_rust/target/release/app_rust app_rust
RUN chmod -R a-w+rx app_rust && useradd -ms /bin/bash devuser
USER devuser

EXPOSE 8000

HEALTHCHECK CMD curl -f localhost:8000/health || exit 1
ENTRYPOINT ["./app_rust"]
