# Day 85 - Linux Process Monitoring & Resource Troubleshooting

## Objective
Learn how to monitor system processes, view resource usage, and terminate running processes.

## Commands Used

```bash
uptime
ps aux
top
vmstat 1 5
sleep 300 &
ps aux | grep sleep
kill <PID>
ps aux | grep sleep
```

## Results
- Checked system uptime.
- Viewed running processes.
- Monitored CPU and memory usage.
- Checked virtual memory statistics.
- Created a background process.
- Located the process by PID.
- Terminated the process successfully.
- Verified the process was no longer running.

## What I Learned
- Monitor active processes.
- Identify processes by PID.
- Kill unnecessary processes.
- Use top and vmstat to observe system resources.
