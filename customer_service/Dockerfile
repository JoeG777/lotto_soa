FROM python:3.9-alpine

COPY src/requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY src /usr/src

WORKDIR /usr
EXPOSE 8080
CMD [ "uvicorn", "src.customer.application.app:api", "--host", "0.0.0.0", "--port", "8080" ]