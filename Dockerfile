FROM python:3.6.9-alpine3.9

WORKDIR /usr/src

RUN apk update && apk upgrade --update && \
    apk add --update \
        chromium \
        udev \
        chromium-chromedriver \
        openssl && \
    pip install \
        requests \
        selenium && \
    cp /usr/lib/chromium/chromedriver /usr/src/
# RUN pip install chromedriver-binary

COPY . .

ENTRYPOINT ["python", "/usr/src/main.py"]

