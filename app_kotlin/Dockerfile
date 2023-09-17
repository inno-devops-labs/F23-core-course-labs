### Application builder image
FROM eclipse-temurin:17-jdk AS APP_BUILDER

# Set working directory
WORKDIR /app_kotlin

# Copy project files excepting those in .dockerignore
COPY . .

# build application
RUN ./gradlew build


### Application executable image
FROM eclipse-temurin:17-jre

# Set non-root user
RUN addgroup --system user && adduser --system --group user
USER user

# Set working directory
WORKDIR /app_kotlin

COPY --from=APP_BUILDER app_kotlin/build/libs/app_kotlin-1.0.0.jar .

EXPOSE 8080
ENTRYPOINT [ "java", "-jar", "/app_kotlin/app_kotlin-1.0.0.jar" ]
