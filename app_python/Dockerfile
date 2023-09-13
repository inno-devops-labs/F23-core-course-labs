FROM python:3.10-alpine
 
# Create app directory
WORKDIR /app
 
# Install app dependencies, enabling caching mechanisms 
COPY requirements.txt ./
 
RUN pip install --no-cache-dir -r requirements.txt 

# Copy files
COPY . .

ENV PORT=5000
ENV FLASK_APP=application.app
ENV FLASK_ENV=development

EXPOSE $PORT

# Creating new user
RUN adduser -D myuser && chown -R myuser /app

# Make executables owned by root and not writable
RUN chown root /app/* && chmod 755 /app/*

USER myuser

HEALTHCHECK --interval=5s CMD ["sh", "-c", "wget --spider http://localhost:$PORT || exit 1"] 

CMD ["sh", "-c", "flask run --host 0.0.0.0 --port $PORT"]