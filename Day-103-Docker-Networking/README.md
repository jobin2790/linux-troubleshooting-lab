# Day 103 — Docker Networking

## Objective

Learn Docker container networking, custom bridge networks,
container DNS, network isolation, and port publishing.

## Commands Practiced

### Create custom network

docker network create day103-network

### Run nginx container

docker run -d \
  --name web-server \
  --network day103-network \
  -p 8080:80 \
  nginx

### Run Alpine client

docker run -dit \
  --name test-client \
  --network day103-network \
  alpine sh

### Test container connectivity

docker exec -it test-client sh

ping -c 3 web-server

### Install curl

apk add --no-cache curl

### Test HTTP connectivity

curl http://web-server

## What I Learned

- Docker containers can communicate through custom networks.
- Docker provides internal DNS resolution for container names.
- Containers on the same custom bridge network can communicate.
- Containers on different isolated networks cannot communicate.
- `-p 8080:80` publishes a container port to the host.
- `docker network inspect` can be used to troubleshoot networking.
- `ping` tests basic network connectivity.
- `curl` tests application-level HTTP connectivity.

## Troubleshooting Approach

If a container cannot reach another container:

1. Check whether both containers are running.
2. Check their network membership.
3. Inspect the Docker network.
4. Test DNS resolution.
5. Test connectivity with ping.
6. Test the application with curl.
7. Check port publishing if accessing from the host.

## Result

Successfully tested Docker container networking,
DNS-based service discovery, HTTP connectivity,
and network isolation.
