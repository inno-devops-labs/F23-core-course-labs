#syntax=docker/dockerfile:1
FROM node:20

RUN groupadd -r sveltegroup && useradd -r -g sveltegroup relisqu

WORKDIR /svelte-app
 

COPY package.json ./
COPY package-lock.json ./

RUN npm install --production
RUN npm install jsdom axios moment moment-timezone

COPY . .

RUN npm run Build

EXPOSE 5173

CMD npm run dev -- --host 
