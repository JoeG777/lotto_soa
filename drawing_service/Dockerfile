FROM python:3.9-alpine

ENV RABBIT_INIT_ROOT_USERNAME=${RABBIT_INIT_ROOT_USERNAME}
ENV RABBIT_INIT_ROOT_PASSWORD=${RABBIT_INIT_ROOT_PASSWORD}
ENV RABBIT_PORT=${RABBIT_PORT}
ENV RABBIT_HOST=${RABBIT_HOST}

ENV QUEUE_DRAWING_EVENT=${QUEUE_DRAWING_EVENT}
ENV DRAW_MESSAGE_EXCHANGE=${DRAW_MESSAGE_EXCHANGE}

COPY src/requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY src /usr/src

WORKDIR /usr
EXPOSE 8080
CMD [ "uvicorn", "src.draw.application.app:api", "--host", "0.0.0.0", "--port", "8080" ]