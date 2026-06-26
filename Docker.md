## Docker Commands

```

// Pull 
docker pull IMAGE_NAME
docker pull IMAGE_NAME:version     // specify version or tag

docker images

// Run
docker run IMAGE_NAME
docker run -it IMAGE_NAME          // -it is interactive mode which allows us to access the terminal of the container
docker run -d IMAGE_NAME           //  -d Detach mode (runs in bg)
docker run -e KEY=val IMAGE_NAME   //   -e Environment variables
docker run --name CONT_NAME -d IMAGE_NAME  // give custom names to containers

exit    // used to stop the container


//Show containers
docker ps           // shows only running containers
docker ps -a        // shows all containers

// start or stop containers that are already built
docker start CONT_NAME or CONT_ID
docker stop CONT_NAME or CONT_ID

// Remove commands
docker rm CONT_NAME   // remove containers
docker rmi IMAGE_NAME  // remove images
// You have to delete assiociated containers before deleting the image


```

Docker-Hub

https://hub.docker.com/

```

// Port Binding

docker run -p<host>:<container> IMAGE_NAME


// Troubleshoot Commands

docker logs CONT_ID

//exec allows running commands in an already running container 
docker exec -it CONT_ID /bin/bash
docker exec -it CONT_ID /bin/sh

```

## Docker Network

```

docker network ls
docker network create NETWORK_NAME
docker network rm NETWORK_NAME

```

Types of Drivers:

- Bridge (default)

- Host

- Null

## Docker Compose

Docker compose is a tool for defining and running multi-container applications.

.yaml  → Yet Another Markup Language

```

// automatically runs on a same default network
services:
	mongo:
		image: mongo
		ports:
		- 27017:27017
		volumes:
		- local:container
		environment:
		- MONGO_INTDB_ROOT_USERNAME=admin 
			MONGO_INTDB_ROOT_PASSWORD: qwerty
	
	mongo-experss:
		image:mongo-express
		ports:
		- 8081:8081
		environment:
			ME_CONFIG_MONGODB_ADMINUSERNAME: admin
			ME_CONFIG_MONGODB_ADMINPASSWORD: qwerty
			ME_CONFIG_MONGODB_URL: mongodb://admin:qwerty@mongo:27017/

```

```

docker compose -f file.yaml up -d
docker compose -f file.yaml down

```

## Dockerizing our App

- Dockerfile 

```

FROM base image
WORKDIR 
COPY
RUN
CMD
EXPOSE
ENV

```

```

docker build -t testapp:1.0 .
docker run testapp:1.0
docker run -it testapp:1.0 bash

```

```

docker login
docker push IMAGE_NAME

```

## Docker Volumes

Volumes are persistent data stores for containers

```

docker run -v <abs-local-path>:<container-path> IMAGE_NAME
docker volume ls
docker volume create VOL_NAME
docker volume rm VOL_NAME
docker volume prune

```

```

docker run -v VOL_NAME:CONT_DIR  // named values, mostly used

docker run -v MOUNT_PATH         // Anonymous Volumes

docker run -v HOST_DIR:CONT_DIR  // Bind Mount

```
