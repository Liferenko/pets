FROM golang:latest

ARG app_env
ENV APP_ENV $app_env




COPY ./app /go/src/github.com/Liferenko/go/app
WORKDIR /go/src/github.com/Liferenko/go/app

RUN go get ./
RUN go build

CMD if [ ${APP_ENV} == production ]; \
    then \
    app; \
    else \
    go get github.com/pilu/fresh && \
    fresh; \
    fi
EXPOSE 8080
