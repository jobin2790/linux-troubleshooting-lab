# Day 88 – Linux System Logs & Troubleshooting

## Objective

Learned how to inspect Linux log files and troubleshoot Nginx using system logs and diagnostic commands.

## Commands Practiced

```bash
ls -l /var/log
ls -l /var/log/nginx
tail -20 /var/log/nginx/access.log
tail -20 /var/log/nginx/error.log
ps aux | grep nginx
curl http://localhost
nginx -t
```

## Topics Learned

- Exploring the /var/log directory
- Viewing Nginx access logs
- Viewing Nginx error logs
- Checking running processes
- Testing a web server using curl
- Validating Nginx configuration
- Understanding "Address already in use" errors

## Troubleshooting Performed

- Verified Nginx processes using `ps aux`
- Confirmed the web server was working using `curl http://localhost`
- Investigated Nginx error logs
- Identified that port 80 was already in use because Nginx was already running

## Outcome

Successfully diagnosed an Nginx startup issue and confirmed the web server was functioning correctly by analyzing logs, checking processes, and testing HTTP responses.
