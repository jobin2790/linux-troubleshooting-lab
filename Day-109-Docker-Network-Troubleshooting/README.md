
# Day 109 — Docker Network Troubleshooting

## Objective

Learn how to troubleshoot Docker container networking problems, including container name resolution, network isolation, and connecting containers to a shared network.

## Environment

- OS: macOS (Apple Silicon M2)
- Docker Version: 29.6.1
- Docker Network Driver: Bridge
- Tools: Docker CLI, Nginx, Alpine Linux, curl

## Lab 1 — Create a Custom Network

Created a user-defined bridge network:

```bash
docker network create day109-network
```

Verified the network using:

```bash
docker network ls
docker network inspect day109-network
```

## Lab 2 — Container-to-Container Communication

Created an Nginx web server:

```bash
docker run -d \
  --name web-server \
  --network day109-network \
  nginx:alpine
```

Created a test client:

```bash
docker run -dit \
  --name test-client \
  --network day109-network \
  alpine:latest \
  sh
```

Installed curl inside the test client:

```bash
apk add --no-cache curl
```

Tested communication:

```bash
curl http://web-server
```

### Result

The Nginx welcome page was returned successfully.

This confirmed that containers on the same user-defined network can communicate using container names.

## Lab 3 — Troubleshooting Network Isolation

Created a separate network:

```bash
docker network create isolated-network
```

Created an isolated client:

```bash
docker run -dit \
  --name isolated-client \
  --network isolated-network \
  alpine:latest \
  sh
```

Tested communication:

```bash
curl http://web-server
```

### Error

```text
curl: (6) Could not resolve host: web-server
(Domain name not found)
```

### Root Cause

The isolated client was connected to `isolated-network`, while the web server was connected to `day109-network`.

The isolated client could not resolve the web server's container name through the Docker DNS service on its own network.

## Lab 4 — Fix the Network Problem

Connected the isolated client to the web server's network:

```bash
docker network connect day109-network isolated-client
```

Verified the network:

```bash
docker network inspect day109-network
```

Tested communication again:

```bash
docker exec isolated-client curl http://web-server
```

### Result

The Nginx welcome page was returned successfully.

The connectivity issue was resolved by connecting both containers to the same user-defined network.

## Troubleshooting Commands

```bash
docker network ls
docker network inspect NETWORK_NAME
docker ps
docker inspect CONTAINER_NAME
docker network connect NETWORK_NAME CONTAINER_NAME
```

## Key Learnings

1. User-defined bridge networks provide container-to-container communication.
2. Docker DNS allows containers to resolve other containers by name on the same user-defined network.
3. Containers on separate networks may not resolve each other's names.
4. `docker network connect` attaches an existing container to another network.
5. Network inspection helps identify connectivity and configuration problems.

## Cleanup

Removed the practice containers:

```bash
docker rm -f web-server test-client isolated-client
```

Removed the practice networks:

```bash
docker network rm day109-network isolated-network
```

## Conclusion

Completed a Docker networking troubleshooting lab by identifying a network isolation problem, inspecting network configuration, connecting the container to the correct network, and verifying successful communication.
