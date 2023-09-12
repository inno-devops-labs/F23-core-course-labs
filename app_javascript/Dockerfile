FROM node:14-slim AS build

WORKDIR /app
COPY main.js package-lock.json package.json ./

RUN npm install

FROM node:14-slim AS final_image

WORKDIR /app
COPY --from=build /app/main.js /app/package-lock.json /app/package.json ./

RUN chmod a-wx main.js && useradd -ms /bin/bash myuser
USER myuser

EXPOSE 5000
ENTRYPOINT ["node", "main.js"]
