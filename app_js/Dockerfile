FROM node:14-slim

EXPOSE 3000

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

RUN useradd -m myuser
USER myuser

CMD [ "node", "server.js" ]