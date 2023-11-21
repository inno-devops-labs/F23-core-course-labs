FROM rust:alpine AS builder

WORKDIR /app

COPY . .

RUN cargo build --release \ 
    && addgroup -S app && adduser -S app -G app \
    && chown -R app:app .

USER app

FROM debian:buster-slim

COPY --from=builder /app/target/release/web_server .

USER app

EXPOSE 30000


CMD ["web_server"]