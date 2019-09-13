FROM python:3.6.9-alpine3.9

WORKDIR /usr/src

RUN apk update && apk upgrade
RUN apk add --update chromium
RUN apk add --update chromium-chromedriver

RUN pip install requests
RUN pip install selenium
# RUN pip install chromedriver-binary

COPY . .

ENTRYPOINT ["python", "/usr/src/main.py"]

