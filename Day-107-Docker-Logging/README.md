# Day 107 — Docker Logging & Log Management

## Objective

Learn how to inspect, monitor, filter, and manage Docker container logs.

## Topics Covered

- Docker container logs
- `docker logs`
- Live log monitoring
- Tail logs
- Timestamps
- Time-based log filtering
- Docker logging drivers
- Log rotation
- Log size limits
- Container troubleshooting

## 1. Create Logging Container

Created an Alpine Linux container that continuously generates application logs.

```bash
docker run -d \
  --name logging-demo \
  alpine sh -c 'while true; do echo "Application log: $(date)"; sleep 2; done'
