# Day 113 — Docker Compose Multi-Container Application

## Objective

Deploy a Flask web application and Redis database using Docker Compose.

## Architecture

```text
Mac Host
   |
   | Port 5001
   v
Flask Web Container
   |
   | Docker Compose Network
   v
Redis Container


## Services

### Web Service

- Flask application
- Container port: 5000
- Host port: 5001
- Built using a custom Dockerfile

### Redis Service

- Redis 7 Alpine
- Container port: 6379
- Used for application data/cache
- Accessible through the Docker Compose network

## Docker Compose Commands

Build and start the services:

```bash
docker compose up -d --build

### Check running containers

```bash
docker compose ps

### Test Flask Application

```bash
curl http://localhost:5001
curl http://localhost:5001/health

docker compose exec redis redis-cli ping

docker compose logs web
docker compose logs redis

docker compose down
