FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp postgresql-dev gcc python3-dev libc-dev linux-headers musl-dev jpeg-dev zlib-dev

RUN pip install -r /requirements.txt

RUN apk del .tmp

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user

RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]
