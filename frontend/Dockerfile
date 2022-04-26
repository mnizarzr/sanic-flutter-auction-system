FROM ubuntu:20.04 as base

RUN apt-get update && apt-get install -yq curl file git unzip xz-utils zip && rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/flutter

ARG CHANNEL=stable

RUN git clone -b ${CHANNEL} https://github.com/flutter/flutter.git /opt/flutter
ENV PATH $PATH:/opt/flutter/bin
RUN flutter config --no-analytics --enable-web --no-enable-android --no-enable-ios
RUN flutter precache --web

WORKDIR /tmp/
# Ensuring precaching works, idk, feels comfortable.
RUN flutter create --platforms web dummy && rm -rf dummy


FROM base as dev

USER root
WORKDIR /app/
COPY . .

RUN flutter pub get

EXPOSE 8081

CMD ["flutter", "run", "-d", "web-server", "--web-run-headless", "--web-port", "8081", "--web-hostname", "0.0.0.0"]