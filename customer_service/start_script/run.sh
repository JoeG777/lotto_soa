#!/bin/sh

uvicorn src.customer.application.app:api --host 0.0.0.0 --port $1 &
python -m src.customer.application.consumer