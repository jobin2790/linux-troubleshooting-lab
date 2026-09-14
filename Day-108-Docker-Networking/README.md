# Day 108 — Docker Networking

## Objective

Learn how Docker containers communicate with each other using Docker networks.

This lab focuses on creating a custom Docker bridge network, connecting containers to the network, testing container-to-container communication, inspecting network configuration, and cleaning up Docker networking resources.

---

## Topics Covered

- Docker networking
- Docker bridge networks
- Creating a custom Docker network
- Connecting containers to a Docker network
- Container-to-container communication
- Docker internal DNS
- Network inspection
- Container IP addresses
- Testing network connectivity
- Stopping and removing containers
- Removing Docker networks

---

# 1. Check Existing Docker Networks

Before creating the custom network, existing Docker networks were checked.

```bash
docker network ls
```

Docker displayed the default networks:

```text
NETWORK ID     NAME      DRIVER    SCOPE
...            bridge    bridge    local
...            host      host      local
...            none      null      local
```

---

# 2. Create a Custom Docker Network

Created a custom bridge network named `app-network`.

```bash
docker network create app-network
```

Docker returned a network ID after successful creation.

Verified the network:

```bash
docker network ls
```

Example:

```text
NETWORK ID     NAME          DRIVER    SCOPE
...            app-network   bridge    local
...            bridge        bridge    local
...            host          host      local
...            none          null      local
```

The `app-network` network was successfully created using the Docker `bridge` driver.

---

# 3. Run a Web Server Container on the Custom Network

Created an Alpine Linux container named `web-server` and attached it to `app-network`.

```bash
docker run -dit --name web-server --network app-network alpine sh
```

The container was started in detached interactive mode.

---

# 4. Run a Client Container on the Custom Network

Created another Alpine Linux container named `client` and attached it to the same network.

```bash
docker run -dit --name client --network app-network alpine sh
```

Both containers were now connected to:

```text
app-network
```

---

# 5. Verify Running Containers

Checked the running containers:

```bash
docker ps
```

The `web-server` and `client` containers were visible as running containers.

---

# 6. Inspect the Docker Network

Inspected the custom Docker network:

```bash
docker network inspect app-network
```

The output showed information such as:

- Network name
- Network ID
- Driver
- Subnet
- Gateway
- Connected containers
- Container IP addresses

Example network configuration:

```text
Name: app-network
Driver: bridge
```

The inspection confirmed that the containers were attached to the custom network.

---

# 7. Test Container-to-Container Communication

The `client` container was used to test communication with the `web-server` container.

Entered the client container:

```bash
docker exec -it client sh
```

Tested connectivity using the container name:

```bash
ping -c 4 web-server
```

Successful ping responses confirmed that the containers could communicate with each other through the Docker network.

Exited the container:

```bash
exit
```

---

# 8. Docker Internal DNS

Docker's user-defined bridge networks provide internal DNS resolution.

The container name:

```text
web-server
```

can be used by the `client` container instead of manually using the web server's IP address.

For example:

```bash
ping -c 4 web-server
```

Docker resolves `web-server` to the container's IP address within the custom network.

This is useful because container IP addresses can change when containers are recreated, while the container/service name can remain stable.

---

# 9. Check Container IP Addresses

Container network information can be inspected using:

```bash
docker inspect web-server
```

and:

```bash
docker inspect client
```

The network section contains the IP address assigned to each container.

A shorter command can also be used:

```bash
docker inspect -f '{{.Name}} -> {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web-server client
```

Example:

```text
/web-server -> 172.xx.xx.xx
/client -> 172.xx.xx.xx
```

The exact IP addresses depend on Docker's network configuration.

---

# 10. Understand Docker Bridge Networking

The custom `app-network` was created using the Docker bridge driver.

A simplified communication model is:

```text
                 Docker Host
                     |
               app-network
              /           \
             /             \
      web-server          client
       Alpine              Alpine
          |                  |
       IP Address         IP Address
             \            /
              \          /
          Container Communication
```

Containers connected to the same user-defined bridge network can communicate with each other.

---

# 11. Default Bridge vs User-Defined Bridge

Docker provides a default `bridge` network.

However, user-defined bridge networks such as:

```text
app-network
```

provide better container-to-container communication and built-in DNS-based service discovery.

Example:

```bash
docker run -dit --name web-server --network app-network alpine sh
```

The client can communicate with the server using:

```bash
ping web-server
```

instead of depending on a manually configured IP address.

---

# 12. Stop the Test Containers

After completing the networking tests, the containers were stopped.

```bash
docker stop web-server client
```

---

# 13. Remove the Test Containers

Removed the containers after completing the lab:

```bash
docker rm web-server client
```

---

# 14. Remove the Custom Network

After the containers were removed, the custom network was removed:

```bash
docker network rm app-network
```

Docker confirmed that the network was removed.

Verified the remaining networks:

```bash
docker network ls
```

The custom `app-network` was no longer listed.

Only the standard Docker networks remained:

```text
bridge
host
none
```

---

# 15. Troubleshooting Commands

Useful commands for Docker networking troubleshooting:

### List networks

```bash
docker network ls
```

### Inspect a network

```bash
docker network inspect app-network
```

### List running containers

```bash
docker ps
```

### List all containers

```bash
docker ps -a
```

### Inspect a container

```bash
docker inspect web-server
```

### Test container connectivity

```bash
docker exec -it client ping -c 4 web-server
```

### Inspect container IP

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web-server
```

### Remove a network

```bash
docker network rm app-network
```

---

# 16. Troubleshooting Scenario

### Problem

A client container cannot communicate with another container.

### Troubleshooting steps

First check whether both containers are running:

```bash
docker ps
```

Check the Docker networks:

```bash
docker network ls
```

Inspect the network:

```bash
docker network inspect app-network
```

Verify that both containers appear under the network's `Containers` section.

Check the container IP addresses:

```bash
docker inspect web-server
docker inspect client
```

Test connectivity:

```bash
docker exec -it client ping -c 4 web-server
```

If the containers are not connected to the same network, connect the required container:

```bash
docker network connect app-network client
```

Then test communication again.

---

# 17. Key Commands Learned

| Command | Purpose |
|---|---|
| `docker network ls` | List Docker networks |
| `docker network create` | Create a Docker network |
| `docker network inspect` | Inspect network configuration |
| `docker network connect` | Connect a container to a network |
| `docker network disconnect` | Disconnect a container |
| `docker network rm` | Remove a Docker network |
| `docker run --network` | Start a container on a specific network |
| `docker exec` | Execute a command inside a container |
| `docker inspect` | Inspect container/network details |
| `ping` | Test network connectivity |

---

# 18. What I Learned

- Docker containers can communicate through Docker networks.
- Docker provides default networks such as `bridge`, `host`, and `none`.
- User-defined bridge networks can be created for application environments.
- Containers on the same user-defined network can communicate with each other.
- Docker provides internal DNS resolution for containers on user-defined networks.
- Container names can be used instead of hard-coding container IP addresses.
- `docker network inspect` is useful for troubleshooting network connectivity.
- Container IP addresses can be inspected using `docker inspect`.
- Docker networking problems can be diagnosed by checking containers, networks, IP addresses, and connectivity.
- Docker networks should be cleaned up after completing temporary labs.

---

# Conclusion

Day 108 demonstrated the fundamentals of Docker networking.

A custom bridge network named `app-network` was created and used to connect multiple Alpine Linux containers. Container-to-container communication was tested using the container name, network configuration was inspected, container IP addresses were examined, and the test resources were removed after completing the lab.

This provides a foundation for troubleshooting Docker networking issues in cloud and production environments.
