# 6. Kubernetes für die Services, Ingress | ConfigMap | Volumes, Dokumentation der Ausführung

## Entities

### Ingress
_TBD_ #TODO

### ConfigMap
This file is similarly used compared to the .env-file proposed in the [Docker Compose Configuration](../infrastructure/README.md#executing-the-docker-compose-file). In here we collect all configuration values which we want to pass from outside to our whole application.

### Volumes

### Services
Services in Kubernetes provide the internal cluster with a single acess point to any given deployment of pods. Consequently, the represent an abstraction layer over the deployment and its possible scalability. For each of the applications in this architecture a separate service is created next to the respective deployment e.g. [drawing_service.yaml](./drawing_service.yaml)

## Configuration
The following variables and respective values are needed inside the ConfigMap. Changing of these values may need further adjustment in their corresponding deployments or services.

```
  RABBIT_MGMT_PORT:
  DRAW_SERVICE_PORT:
  CUSTOMER_SERVICE_PORT:
  DEFAULT_INTERNAL_SERVICE_PORT:

  MONGO_INITDB_ROOT_USERNAME:
  MONGO_INITDB_ROOT_PASSWORD:
  MONGO_PORT:
  MONGO_HOST:
  CUSTOMER_DATABASE_NAME:
  CUSTOMER_COLLECTION_NAME:

  RABBIT_INIT_ROOT_USERNAME:
  RABBIT_INIT_ROOT_PASSWORD:
  RABBIT_PORT:
  RABBIT_HOST:

  QUEUE_DRAWING_EVENT:
  DRAW_MESSAGE_EXCHANGE: 
```


## Execution

As the previous step for [configuring](#configuration) is done the whole application can be launched by executing the following command:
1. Change into **root-directory** of this project
2. Execute the following command (having a k8s engine running)
    ```bash
    kubectl apply -f ./k8s/
    ```


