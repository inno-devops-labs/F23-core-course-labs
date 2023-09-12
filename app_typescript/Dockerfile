FROM node:lts as dependencies
WORKDIR /app_ts

COPY package.json package-lock.json ./

RUN npm install --frozen-lockfile

FROM node:lts as builder
WORKDIR /app_ts

ENV APP_USER=myuser

COPY /public ./public
COPY /src ./src
# COPY .eslintrc.json .eslintrc.json
COPY tsconfig.json tsconfig.json
COPY next.config.js next.config.js
COPY package.json package.json
COPY --from=dependencies --chown=$APP_USER:$APP_USER /app_ts/node_modules ./node_modules

RUN npm run build

FROM node:lts as runner
WORKDIR /app_ts
ENV NODE_ENV production
ENV APP_USER=myuser

COPY --from=builder --chown=$APP_USER:$APP_USER /app_ts/public ./public
COPY --from=builder --chown=$APP_USER:$APP_USER /app_ts/package.json ./package.json
COPY --from=builder --chown=$APP_USER:$APP_USER /app_ts/.next ./.next
COPY --from=builder --chown=$APP_USER:$APP_USER /app_ts/node_modules ./node_modules

EXPOSE 3000
CMD ["npm", "start"]