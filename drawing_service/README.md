# Drawing Service

This service offers endpoints for 
    - `/trigger_draw` - triggering a lotto draw
The endpoints and their documentation via a Swagger UI is reacheable on the `/docs` endpoint once the application is running.

### Configuration
The service needs the following environment variables at runtime:

    ```
    RABBIT_PORT= {host of the RabbitMQ instance}
    RABBIT_HOST= {port of the RabbitMQ instance}
    QUEUE_DRAWING_EVENT= {name of the queue to publish to on the RabbitMQ instance}
    DRAW_MESSAGE_EXCHANGE= {exchange key on the RabbitMQ instance}

    DEFAULT_INTERNAL_SERVICE_PORT= {default port where the application should run (only for docker)}
    ```
This can be achieved by manually setting them or putting them into an `.env` file. This file can be conveniently used for [docker execution](#docker) as well.

### Execution
1. Install the dependencies
    ```bash
    pip install -r src/requirements.txt
    ```
2. Make sure a RabbitMQ instance is running and has been configured via the environment variables to be reached by the publisher
3. Start the service by excuting the following command
    ```bash
    uvicorn src.draw.application.app:api --host 127.0.0.1 --port 8080
    ```

### Docker
1. Build the docker container with a desired name and tag
    ```
    docker build -t drawing_service:0.1.0 .
    ```
2. Run it 
    ```
    docker run --rm --env-file .env -p 8080:8080 drawing_service:0.1.0
    ```