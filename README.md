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



```

docker run -it ubuntu
// run ubuntu in interactive mode

```



Docker-Hub

https://hub.docker.com/