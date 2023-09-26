FROM node:14

# Create app directory
WORKDIR /app
 
# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install application dependencies
RUN npm install

# Copy files
COPY . .

ENV PORT=3000

EXPOSE $PORT

# Creating new user
RUN adduser --disabled-password  myuser && chown -R myuser /app

# Make executables owned by root and not writable
RUN chown root /app/* && chmod 755 /app/*

USER myuser

HEALTHCHECK --interval=5s CMD ["sh", "-c", "wget --spider http://localhost:$PORT || exit 1"] 

CMD ["node", "app.js"]