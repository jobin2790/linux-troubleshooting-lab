# Day 94 – System Performance Tuning

## Objective
Learn how to monitor CPU, memory, and disk performance using Linux monitoring tools.

## Commands Used

```bash
stress-ng --cpu 2 --timeout 60s
mpstat 1 5
iostat -x 1 5
vmstat 1 5
```

## Observations

- Installed stress-ng.
- Generated CPU load using stress-ng.
- Monitored CPU usage with mpstat.
- Monitored disk I/O with iostat.
- Monitored system performance with vmstat.
- The stress test completed successfully.
