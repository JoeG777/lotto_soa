# 5. Docker Compose der Services, Dokumentation der Ausführung, NGNIX als Load Balancer

The attached [docker-compose.yaml-File](./docker-compose.yaml) configures the whole architecture with the following top-level entities:

### Services
- **drawing_service** - One service of the application responsible for drawing the winning numbers. Uses the docker compose mechanism of being built by the dockerfile, exposing the ports, attach to a docker network and supply the container with environment variables.
- **customer_service** - One service of the application responsible for handling bets registered by users and evaluating them based of the numbers supplied by the above service. Uses the docker compose mechanism of being built by the dockerfile, exposing the ports, attach to a docker network and supply the container with environment variables. Depends on the running rabbitmq-service to connect to on startup.
### Infrastructure
- **rabbitmq** - The message broker which holds the mechanisms for two services to asynchronously share messages
- **mongodb** - The NoSQL database is responsible for the persistance of data that flows through the system
- **ngnix** - GNIX acts as reverse proxy to bring abstraction over the access of the application from outside the network

### Volumes
Define volumes for making sure the persistence layer is independent from the lifecycle of the containers and above described components. As they are to be used only inside the application they are realized as docker managed without intended access for the developer or operator.

### Network
- **cnd_network** - One main docker network with the default driver `bridge` is created for two main reasones:
    1. During the development it is necessary to be able to access the whole application by optional port-forwarding onto the development machine for direct access
    2. During production we want to be able to access all the available services to talk to each other by using docker builtin DNS via the container names.

---

### Executing the Docker Compose File

Depending of the configuration mechanism of choice the actual command of executing the docker compose file needs to be slightly adjusted

1. Change into **root-directory** of this project
2. Create a .env file with the following content
    ```
    # INFRA_SPECIFIC ---

    RABBIT_MGMT_PORT=
    DRAW_SERVICE_PORT=
    CUSTOMER_SERVICE_PORT=
    DEFAULT_INTERNAL_SERVICE_PORT=

    # APPLICATION_SPECIFIC ---

    # MONGODB
    MONGO_INITDB_ROOT_USERNAME=
    MONGO_INITDB_ROOT_PASSWORD=
    MONGO_PORT=
    MONGO_HOST=

    # RABBITMQ
    RABBIT_INIT_ROOT_USERNAME=
    RABBIT_INIT_ROOT_PASSWORD=
    RABBIT_PORT=
    RABBIT_HOST=

    # DRAWING_SERVICE
    QUEUE_DRAWING_EVENT=
    DRAW_MESSAGE_EXCHANGE=

    # CUSTOMER_SERVICE
    CUSTOMER_DATABASE_NAME=
    CUSTOMER_COLLECTION_NAME=
    ```
    These environment variables will be passed down from the invocation of the compose file into each service which will use them for configuring themselves.
3. Execute the command
    - provide the path to the file as we reside in the **root directory** of this project
    - pass the .env-file as a parameter
    - tell docker compose to re-build the services if necessary

    The whole command to execute
    ```bash
    docker compose --env-file .env -f .\infrastructure\docker-compose.yaml up --build
    ```

    In case the `customer_service` does not start properly the first time and consequently the `nginx` service lacks a dependency execute the above command again with the addition of those two services.