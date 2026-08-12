# Day 97 — Linux systemd Services & Service Management

## Objective

Learn how to manage Linux services using systemd and systemctl.

## Topics Covered

- systemd and PID 1
- systemctl
- Checking systemd status
- Listing running services
- Creating a custom systemd service
- Starting and stopping services
- Restarting services
- Enabling and disabling services
- Checking service status
- Viewing service logs with journalctl
- Testing automatic service restart
- Checking service processes and Main PID

## Commands Practiced

```bash
ps -p 1 -o pid,comm,args

systemctl --version

systemctl status

systemctl list-units --type=service --state=running

systemctl list-unit-files --type=service

systemctl daemon-reload

systemctl start day97-demo.service

systemctl stop day97-demo.service

systemctl restart day97-demo.service

systemctl status day97-demo.service

systemctl enable day97-demo.service

systemctl disable day97-demo.service

systemctl is-enabled day97-demo.service

systemctl show -p MainPID day97-demo.service

journalctl -u day97-demo.service -n 20 --no-pager
