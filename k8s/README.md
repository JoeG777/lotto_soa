# 6. Kubernetes für die Services, Ingress | ConfigMap | Volumes, Dokumentation der Ausführung

## Entities

### Ingress
The ingress resource is controlled by an ingress controller which has to be installed (nginx) as a prerquisite for sucessfully deploying this application to k8s. It is acting as an entrypoint for the application and the cluster and therefore is responsible for distributing the requests to their corresponding targets which are [statically configured](./ingress.yaml).

### ConfigMap
This file is similarly used compared to the .env-file proposed in the [Docker Compose Configuration](../infrastructure/README.md#executing-the-docker-compose-file). In here we collect all configuration values which we want to pass from outside to our whole application.

### Volumes
As the MongoDB service acts as a persistence layer the present data should be independent from the lifecycle of any pod where the database is running. Therfore, a [persistente volume ressource](./persistent_volume.yaml) alongside with a [persistent volume claim ressource](./persistent_volume.yaml) are configured

### Services
Services in Kubernetes provide the internal cluster with a single acess point to any given deployment of pods. Consequently, the represent an abstraction layer over the deployment and its possible scalability. For each of the applications in this architecture a separate service is created next to the respective deployment e.g. [drawing_service.yaml](./drawing_service.yaml), [customer_service.yaml](./customer_service.yaml)

### Secrets
Some of the services need to authenticate agains other services with credentials. Those should not be present in plain text which is why a [secret ressource](./secrets.yaml) is configured to manage this sensitive date in a more secure way by passing it via environment variables.

## Configuration
The following variables and respective values are needed inside the ConfigMap. Changing of these values may need further adjustment in their corresponding deployments or services.

```
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

In case the `customer_service` does not start properly the first time execute the above command again or restart the deployment for this service again.
