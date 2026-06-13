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

```