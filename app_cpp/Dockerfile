FROM ubuntu:22.04 as build

# Install Boost
ARG CMAKE_VERSION=3.1
ARG BOOST_VERSION=1.83.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        autoconf \
        automake \
        libtool \
        pkg-config \
        ca-certificates \
        libssl-dev \
        wget \
        git \
        curl \
        language-pack-en \
        locales \
        locales-all \
        vim \
        gdb \
        valgrind \
        cmake && \
    apt-get clean \

RUN cd /tmp && \
    BOOST_VERSION_MOD=$(echo $BOOST_VERSION | tr . _) && \
    wget https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VERSION}/source/boost_${BOOST_VERSION_MOD}.tar.bz2 && \
    tar --bzip2 -xf boost_${BOOST_VERSION_MOD}.tar.bz2 && \
    cd boost_${BOOST_VERSION_MOD} && \
    ./bootstrap.sh --prefix=/usr/local && \
    ./b2 install && \
    rm -rf /tmp/*

WORKDIR /app
COPY ./src/main.cpp ./src/CMakeLists.txt ./
RUN cmake -Bbuild -H. -DCMAKE_BUILD_TYPE=Release && cmake --build build


FROM ubuntu:22.04
COPY --from=build /app/build/startServer /app/

RUN useradd -ms /bin/bash user_start && chown -R user_start /app/
USER user_start
WORKDIR /app
ENTRYPOINT ["./startServer", "8080"]