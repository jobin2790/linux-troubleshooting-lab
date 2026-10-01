# Day 114 — Docker Compose Troubleshooting Lab

## Objective

Build, deploy, test, intentionally break, troubleshoot, and recover a multi-container application using Docker Compose.

## Architecture

- Flask API
- Redis
- Docker Compose networking
- Health endpoint
- Visit counter endpoint
- Restart policy

## Services

### API

- Flask application
- Host port: 5001
- Container port: 5000
- Connects to Redis using the Docker service name redis

### Redis

- Redis 7 Alpine
- Container port: 6379
- Restart policy: unless-stopped

## Tests Performed

### 1. Docker Compose Deployment

docker compose up -d --build

### 2. Service Status

docker compose ps

Verified that the API and Redis services were running.

### 3. Health Check

curl http://localhost:5001/health

Expected: OK

### 4. Redis Visit Counter

curl http://localhost:5001/count

curl http://localhost:5001/count

Verified that the visit counter increased between requests.

### 5. Service-Name DNS Resolution

The API connected to Redis using the Docker Compose service name redis.

### 6. Failure Simulation

The Redis container was intentionally stopped/killed to simulate a service failure.

### 7. Logs and Troubleshooting

Docker Compose status, logs, and container information were inspected to identify the failed service.

### 8. Service Recovery

The failed service was recovered using Docker Compose.

### 9. Restart Policy

Redis was configured with the restart policy unless-stopped.

## Troubleshooting Skills Practiced

- Docker Compose deployment
- Container troubleshooting
- Service health checks
- Docker networking
- Service-name DNS resolution
- Logs and troubleshooting
- Failure simulation
- Service recovery
- Restart policies

## Result

Successfully deployed, tested, intentionally failed, troubleshot, and recovered a Docker Compose multi-container application.

**Day 114 completed.**
