FROM python:3.6.9-alpine3.9

WORKDIR /usr/src

RUN apk update && apk upgrade
RUN apk add --update \
        chromium \
        udev \
        chromium-chromedriver \
        openssl

RUN pip install \
        requests \
        selenium
# RUN pip install chromedriver-binary

RUN cp /usr/lib/chromium/chromedriver /usr/src/

COPY . .

ENTRYPOINT ["python", "/usr/src/main.py"]

