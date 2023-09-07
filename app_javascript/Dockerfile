FROM node:20-alpine

RUN useradd -m --no-log-init jsuser
USER jsuser

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

COPY . ./

EXPOSE 80

CMD ["npm", "start"]