#! /bin/sh

uvicorn src.customer.application.app:api --host 0.0.0.0 --port 8080 &
python -m src.customer.application.consumer