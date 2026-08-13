# Day 100 — Docker Compose

## Objective

Learn how to use Docker Compose to define, start, monitor, test, and stop multiple containers as a single application.

## What I Learned

- Docker Compose basics
- Creating a `compose.yaml` file
- Running multiple services together
- Container networking
- Service discovery using Docker DNS
- Viewing container status
- Viewing container logs
- Testing services with curl
- Stopping and removing Compose resources

## Lab Architecture

The Compose application contains:

- `app` — BusyBox application container
- `web` — Nginx web server

The services communicate through the default Docker Compose network.

## Commands Practiced

### Check Docker versions

```bash
docker --version
docker compose version
