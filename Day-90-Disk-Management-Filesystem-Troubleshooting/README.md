# Day 90 - Disk Management & Filesystem Troubleshooting

## Objective
Learn how to analyze disk usage, identify large directories and files, check inode usage, and inspect mounted filesystems in Linux.

## Environment
- Ubuntu 24.04
- Docker Container
- macOS Host

## Commands Used

```bash
df -h
du -sh /*
find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -10
df -i
mount | head -10
```

## Results

- Verified filesystem usage using `df -h`.
- Identified the largest directories using `du -sh /*`.
- Found the largest files in the system.
- Checked inode usage using `df -i`.
- Verified mounted filesystems using `mount`.

## What I Learned

- Disk space monitoring
- Directory size analysis
- Large file identification
- Inode usage monitoring
- Mounted filesystem inspection

## Conclusion

Successfully completed disk management and filesystem troubleshooting inside an Ubuntu Docker container using standard Linux commands.
