# Day 83 - Linux Port & Service Accessibility Troubleshooting

## Objective
Learn how to verify whether a service is listening on a port and test service accessibility.

## Commands Used

```bash
service nginx start
ss -tulnp | grep nginx
ss -tuln | grep :80
curl http://localhost
ps aux | grep nginx
service nginx stop
curl http://localhost
```

## Results
- Verified Nginx was listening on port 80.
- Tested the web server using curl.
- Verified Nginx processes.
- Stopped the Nginx service.
- Confirmed that localhost was no longer reachable after stopping the service.

## What I Learned
- Check listening ports.
- Verify service accessibility.
- Understand the relationship between a running service and an open port.
- Use curl to test web services.
