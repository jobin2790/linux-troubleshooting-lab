
# Day 110 — Docker Advanced Network Troubleshooting

## Objective

Learn how to troubleshoot Docker container network connectivity and DNS resolution issues.

This lab focuses on identifying hostname resolution failures, testing container connectivity using IP addresses, inspecting Docker network configuration, and restoring communication between containers.

---

## Environment

- OS: macOS (Apple Silicon M2)
- Docker: Docker Engine
- Network Driver: Bridge
- Custom Network: day110-network
- Subnet: 172.19.0.0/16
- Gateway: 172.19.0.1

---

## Lab Architecture

### Containers

- day110-web — Nginx web server
- day110-client — Client container used for troubleshooting

### Network

- day110-network — Custom Docker bridge network

The web container uses IP address 172.19.0.2.

The client container uses IP address 172.19.0.3 when connected to the network.

---

## 1. Test Web Server Using Hostname

Command:

```bash
curl -I http://day110-web
```

### Initial Result

```text
curl: (6) Could not resolve host: day110-web
```

### Observation

The hostname could not be resolved from the client container.

The web server itself was not necessarily down. Further network and DNS investigation was required.

---

## 2. Test Web Server Using IP Address

Command:

```bash
curl -I http://172.19.0.2
```

### Result

```text
HTTP/1.1 200 OK
Server: nginx/1.31.6
```

### Observation

The web server responded successfully using its IP address.

This confirmed that the web service was reachable through the tested IP address.

---

## 3. Inspect Docker Network Configuration

Command:

```bash
docker network inspect day110-network
```

### Findings

- Network driver: bridge
- Subnet: 172.19.0.0/16
- Gateway: 172.19.0.1
- Connected containers included day110-web and day110-client.

The network inspection was used to check container membership and IP addresses.

---

## 4. Simulate Network Connectivity Failure

Command:

```bash
docker network disconnect day110-network day110-client
```

Test hostname resolution:

```bash
docker exec day110-client \
  curl -I --max-time 5 http://day110-web
```

### Result

```text
curl: (6) Could not resolve host: day110-web
```

### Root Cause

The client container was disconnected from the Docker network required for communication with the web container.

---

## 5. Restore Network Connectivity

Command:

```bash
docker network connect day110-network day110-client
```

Verify hostname resolution:

```bash
docker exec day110-client \
  getent hosts day110-web
```

### Result

```text
172.19.0.2    day110-web    day110-web
```

### Observation

Docker's internal DNS resolved the container hostname after the client was connected to the appropriate network.

---

## 6. Verify Communication After Fix

Command:

```bash
docker exec day110-client \
  curl -I http://day110-web
```

### Result

```text
HTTP/1.1 200 OK
Server: nginx/1.31.6
```

### Conclusion

The client successfully communicated with the web server using its Docker hostname after restoring network connectivity.

---

## Troubleshooting Commands

```bash
docker network inspect day110-network
```

```bash
docker network disconnect day110-network day110-client
```

```bash
docker network connect day110-network day110-client
```

```bash
docker exec day110-client getent hosts day110-web
```

```bash
docker exec day110-client curl -I http://day110-web
```

---

## Key Learnings

1. Docker container names can be resolved through Docker's internal DNS when containers share a suitable user-defined network.
2. IP-based connectivity and hostname resolution are separate troubleshooting checks.
3. `docker network inspect` helps identify network membership and container IP addresses.
4. A disconnected container may lose access to another container's hostname.
5. Restoring network connectivity can restore DNS-based communication.

---

## Conclusion

Completed Day 110 — Docker Advanced Network Troubleshooting.

Successfully investigated hostname resolution failure, inspected Docker network configuration, reconnected the client container, and verified HTTP communication using Docker DNS.

---

## Status

Completed
