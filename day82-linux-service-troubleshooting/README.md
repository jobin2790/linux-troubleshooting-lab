# Day 82 - Linux Service Troubleshooting (Nginx)

## Objective
Learn how to troubleshoot a Linux service that is not running.

## Commands Used

```bash
nginx -v
service nginx status
service nginx start
service nginx status
ps aux | grep nginx
nginx -t
tail -20 /var/log/nginx/error.log
```

## Results
- Verified Nginx was installed.
- Confirmed Nginx was initially stopped.
- Started the Nginx service successfully.
- Verified the service was running.
- Checked the Nginx processes.
- Validated the Nginx configuration.
- Reviewed the Nginx error log.

## What I Learned
- Check service status.
- Start and verify services.
- Validate configuration before troubleshooting.
- Check running processes.
- Review logs to identify issues.
