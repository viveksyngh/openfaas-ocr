FROM python:3-alpine

# Alternatively use ADD https:// (which will not be cached by Docker builder)
RUN apk --no-cache \
    add curl \ 
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.6.9/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog \
    && apk del curl --no-cache

ENV TESSDATA_PREFIX /usr/share/tessdata

RUN set -x && apk add  --update --no-cache --virtual wget-dependencies \
    ca-certificates \
    openssl

RUN apk add build-base python-dev py-pip  jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories

RUN apk --update --no-cache --repository \
    http://dl-cdn.alpinelinux.org/alpine/edge/main --repository \
    http://dl-cdn.alpinelinux.org/alpine/edge/community  add tesseract-ocr

RUN wget -O ${TESSDATA_PREFIX}/osd.traineddata https://github.com/tesseract-ocr/tessdata/raw/3.04.00/osd.traineddata && \
    wget -O ${TESSDATA_PREFIX}/equ.traineddata https://github.com/tesseract-ocr/tessdata/raw/3.04.00/equ.traineddata && \
    wget -O ${TESSDATA_PREFIX}/eng.traineddata https://github.com/tesseract-ocr/tessdata/raw/4.00/eng.traineddata


WORKDIR /root/

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./index.py .
COPY ./sample1.jpg .

COPY function   function
RUN touch ./function/__init__.py

ENV fprocess="python3 index.py"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
