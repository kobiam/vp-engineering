# Start Redis In Development

To start the Redis nodes with replication:

`docker-compose up -d`

list the containers:

`docker ps`

connect to the nodes:

`docker exec -it [container-id] /bin/bash`

run the cli inside the container:

`redis-cli`

connect to the master from the cli node: (your IP may be diffrent)

`connect 172.19.0.2 6379`
