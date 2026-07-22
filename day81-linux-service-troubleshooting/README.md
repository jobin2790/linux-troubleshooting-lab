# Day 81 - Linux Service Down Troubleshooting

## Objective

Learn how to troubleshoot a Linux service by installing, starting, stopping, and verifying the Nginx web server inside an Ubuntu Docker container.

## Environment

- Ubuntu 24.04 Docker Container
- Docker Desktop
- MacBook Air M2

## Commands Used

```bash
apt update
apt install nginx -y
service nginx start
service nginx status
ps aux | grep nginx
service nginx stop
service nginx status
ps aux | grep nginx
```

## What I Learned

- Installed the Nginx web server.
- Started the Nginx service.
- Verified that the service was running.
- Used `ps aux | grep nginx` to verify the master and worker processes.
- Stopped the service.
- Confirmed that the service was no longer running.
- Verified that all Nginx processes disappeared after stopping the service.

## Result

Successfully simulated a Linux service being started and stopped inside an Ubuntu Docker container and verified the service status using Linux troubleshooting commands.
