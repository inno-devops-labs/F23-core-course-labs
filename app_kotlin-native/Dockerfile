FROM gradle:8.3.0-jdk17 as cache
RUN mkdir -p /cache
WORKDIR /cache

ENV GRADLE_USER_HOME /gradle_cache
ENV KONAN_DATA_DIR /konan_cache
COPY build.gradle.kts /cache
RUN gradle clean nativeBinaries -i --stacktrace

FROM gradle:8.3.0-jdk17 as build
COPY --from=cache /gradle_cache /home/gradle/.gradle
COPY --from=cache /konan_cache /root/.konan
COPY build.gradle.kts gradle.properties settings.gradle.kts /build/
COPY src/ /build/src
WORKDIR /build
RUN gradle nativeBinaries -i --stacktrace
# Prepare passwd for scratch
RUN mkdir /user && \
    echo 'nobody:x:65534:65534:nobody:/:' > /user/passwd

FROM gcr.io/distroless/base-debian12:nonroot as run
WORKDIR /app

# Tool for healthcheck
COPY --from=ghcr.io/tarampampam/curl:8.0.1 /bin/curl /bin/curl

# Binary itself
COPY --from=build \
                  /usr/lib/x86_64-linux-gnu/libcrypt.so.1 \
                  /usr/lib/x86_64-linux-gnu/libgcc_s.so.1 \
                  /lib/x86_64-linux-gnu/

COPY --from=build /build/build/bin/native/releaseExecutable/app_kotlin-native.kexe /app/kexe

ENTRYPOINT  [ "/app/kexe" ]