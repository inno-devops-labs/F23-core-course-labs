#stage 1: build the application
FROM node:20 AS builder

RUN groupadd -r sveltegroup && useradd -r -g sveltegroup relisqu

WORKDIR /svelte-app
 

COPY package.json ./
COPY package-lock.json ./

RUN npm install --production
RUN npm install jsdom axios moment moment-timezone

COPY . .

RUN npm run build

# Stage 2: Create the production image from first stage
FROM node:20

RUN groupadd -r sveltegroup && useradd -r -g sveltegroup relisqu
USER relisqu
WORKDIR /svelte-app

COPY --from=builder /svelte-app .

EXPOSE 5173

# Start the application
CMD npm run dev -- --host
