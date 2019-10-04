*Builds a Docker container using docker-compose*
*It uses the existing docker-compose.yml in the curren folder*
*which in turn uses all the Dockerfile declared as services in it*
docker-compose up --build

*Starts containers that were previously build*
docker-compose up

*Stops the container*
docker-compose stop

*Lists the running containers*
*Even when a container is stopped, it is still "alive" for Docker*
docker-compose stop

*Stops and remove all the running containers*
*This fixes the problem stated for the command above*
*It's a good practice to schedule this command once a week*
docker-compose rm -f

*The same as above, but for running manually*
docker rmi -f $(docker images -qf dangling=true)

*Create the python packages dependencies
pip install --editable .