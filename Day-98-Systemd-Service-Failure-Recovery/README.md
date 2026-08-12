# Day 98 – Systemd Service Failure & Recovery

## Objective

Learn how to troubleshoot a failed systemd service, identify the root cause, fix the service configuration, and verify automatic service recovery.

## Topics Covered

- Diagnosing failed systemd services
- Understanding systemd exit codes
- Understanding `203/EXEC`
- Checking service status with `systemctl`
- Checking service logs with `journalctl`
- Identifying invalid `ExecStart` commands
- Fixing a broken systemd service
- Reloading systemd configuration
- Testing service recovery
- Checking Main PID
- Testing automatic restart
- Enabling a service

## Lab Environment

- Ubuntu
- Docker container
- systemd
- systemctl
- journalctl

## Problem Created

A deliberately broken service was created:

```text
day98-broken.service
