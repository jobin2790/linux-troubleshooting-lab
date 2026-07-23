# Day 84 - Linux Log Analysis & Disk Space Troubleshooting

## Objective
Learn how to analyze logs, monitor disk usage, identify large files, and check memory and inode usage.

## Commands Used

```bash
df -h
du -sh /*
find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -10
tail -20 /var/log/nginx/error.log
grep -i error /var/log/nginx/error.log
free -h
df -i
```

## Results
- Checked filesystem disk usage.
- Measured directory sizes.
- Identified the largest files.
- Viewed Nginx error logs.
- Searched logs for errors.
- Checked memory usage.
- Verified inode usage.

## What I Learned
- Monitor available disk space.
- Identify directories and files consuming storage.
- Analyze log files.
- Check system memory.
- Verify inode availability.
