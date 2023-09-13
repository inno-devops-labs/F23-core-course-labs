FROM node:19-alpine3.15 AS builder
RUN addgroup -S rungroup && adduser -S runuser -G rungroup
WORKDIR /usr/src/app
COPY package*.json ./
RUN chown -R runuser:rungroup .

USER runuser
COPY . .
CMD ["node", "server.js"]