FROM alpine:latest

WORKDIR /MIDAS
RUN apk add --no-cache bash

CMD ["echo", "'Hello", "world'"]
