FROM python:3.7-alpine

RUN apk add --update \
        udev \
        ttf-freefont \
        chromium \
        chromium-chromedriver

RUN pip install requests selenium

WORKDIR /app
COPY ./config.json ./
COPY ./src/*.py ./

CMD ["python", "main.py"]
