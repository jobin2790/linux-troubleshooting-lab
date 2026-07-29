# Day 92 - Filesystem Performance Troubleshooting

## Objective
Learn how to analyze filesystem and system performance on macOS.

## Commands Used
- df -h
- du -sh ~/*
- iostat
- top -l 1
- vm_stat
- find ~/Library/Logs -type f -size +10M

## Observations
- Checked disk usage.
- Analyzed directory sizes.
- Monitored disk I/O using iostat.
- Viewed running processes using top.
- Checked virtual memory using vm_stat.
- No log files larger than 10 MB were found.

## Notes
- macOS System Integrity Protection (SIP) caused "Operation not permitted" for some system folders.
- vmstat is not available by default on macOS, so vm_stat was used.

## Key Learnings
- How to analyze disk usage.
- How to monitor CPU, memory, and disk performance.
- How to troubleshoot filesystem performance on macOS.
