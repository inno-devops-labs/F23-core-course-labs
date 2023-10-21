FROM node:14-slim AS build

WORKDIR /app
COPY app.js main.js package-lock.json package.json ./

RUN npm install
RUN chmod a-wx main.js && useradd -ms /bin/bash myuser
USER myuser

EXPOSE 5000
ENTRYPOINT ["node", "main.js"]
