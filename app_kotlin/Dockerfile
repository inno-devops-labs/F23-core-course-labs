FROM eclipse-temurin:17-jdk AS builder

WORKDIR /app

# Useless files are excluded in .dockerignore file
COPY . .

RUN ./gradlew clean build

FROM eclipse-temurin:17-jre

RUN addgroup --system app && adduser --system --group app

# Set the working directory
WORKDIR /app

# Copy the .jar file from the builder stage
COPY --chown=app:app --from=builder /app/build/libs/base-converter-0.0.1.jar /app
RUN chown app:app -R /app/

USER app

# Expose the application port
EXPOSE 8080

# Run the application
ENTRYPOINT ["java","-jar","/app/base-converter-0.0.1.jar"]