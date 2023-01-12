FROM python:3.9-alpine

COPY src/requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY src /usr/src
COPY .env /usr/.env
COPY start_script/run_parallel.sh /usr/run_parallel.sh
COPY start_script/run_specific.sh /usr/run_specific.sh

WORKDIR /usr
EXPOSE 8080
CMD ./run_specific.sh
