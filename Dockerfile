FROM python:3.8.1-alpine3.11

WORKDIR /usr/src

RUN apk update && apk upgrade --update && \
    apk add --update \
        chromium \
        udev \
        chromium-chromedriver \
        openssl && \
    pip install \
        requests \
        selenium==2.53.6 && \
    cp /usr/lib/chromium/chromedriver /usr/src/

# バージョンが変わって動かないので、コメントアウト
# RUN pip install chromedriver-binary
# COPY . .
# ENTRYPOINT ["python", "/usr/src/main.py"]
