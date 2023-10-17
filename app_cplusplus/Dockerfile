FROM leimao/boost:1.80.0 as build

WORKDIR /app

COPY . .

RUN cmake -Bbuild -H. -DCMAKE_BUILD_TYPE=Release && cmake --build build

FROM ubuntu:22.04

RUN apt-get update && apt-get install -y curl

COPY --from=build /app/build/startServer /app/build/index.html /startServer/
WORKDIR /startServer
ENTRYPOINT ["./startServer", "10000"]