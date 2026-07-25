# Day 89 – Linux Network Troubleshooting

## Objective

Learned how to troubleshoot network connectivity and verify network services in Ubuntu.

## Commands Practiced

```bash
ip addr
ip route
hostname
ping -c 4 google.com
getent hosts google.com
ss -tuln
ss -tuln | grep :80
curl http://localhost
ss -tun
```

## Topics Learned

- Checking network interfaces
- Viewing the routing table
- Verifying hostname
- Testing internet connectivity
- DNS resolution using getent
- Viewing listening ports
- Confirming Nginx is listening on port 80
- Testing a local web server
- Viewing active TCP connections

## Outcome

Successfully verified network connectivity, DNS resolution, listening services, and confirmed the Nginx web server was accessible on port 80.
