# Day 106 — Docker Health Checks

## Objective

Learn how Docker HEALTHCHECK works and understand the difference between a running and healthy container.

## What I Learned

- A container can be running while the application inside is unhealthy.
- Docker HEALTHCHECK periodically tests application health.
- Docker reports health states such as starting, healthy, and unhealthy.
- docker inspect can be used to check health status and health-check logs.

## Dockerfile

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD wget -q --spider http://localhost/ || exit 1
## Commands Practiced

```bash
docker build -t day106-healthcheck .
docker run -d --name day106-web -p 8080:80 day106-healthcheck
docker ps
docker inspect --format='{{.State.Health.Status}}' day106-web
docker exec day106-web rm /usr/share/nginx/html/index.html
docker cp index.html day106-web:/usr/share/nginx/html/index.html
curl http://localhost:8080
curl -I http://localhost:8080
docker rm -f day106-web
docker rmi day106-healthcheck

## Practical Test

### Healthy State

The container initially reported:

    healthy

### Unhealthy State

I removed the Nginx index.html file:

    docker exec day106-web rm /usr/share/nginx/html/index.html

The web server remained running, but the health check failed.

Docker subsequently reported:

    unhealthy

### Recovery

I restored the file:

    docker cp index.html day106-web:/usr/share/nginx/html/index.html

After the health checks ran again, Docker reported:

    healthy

## Key Interview Concept

A container being running does not necessarily mean the application is healthy.

Docker HEALTHCHECK allows Docker to periodically test whether the application is responding correctly.

## Result

Successfully created, tested, intentionally failed, recovered, and verified a Docker container using HEALTHCHECK.
