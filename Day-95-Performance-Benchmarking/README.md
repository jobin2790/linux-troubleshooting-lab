# Day 95 – Performance Benchmarking

## Objective
Benchmark Linux system performance using CPU, memory, and disk monitoring tools.

## Commands Used

```bash
stress-ng --cpu 4 --timeout 120s
mpstat 1 5
iostat -x 1 5
vmstat 1 5
```

## Observations

- Installed and verified sysstat and stress-ng.
- Generated CPU load using stress-ng.
- Monitored CPU utilization with mpstat.
- Checked disk I/O statistics using iostat.
- Monitored memory and CPU activity using vmstat.
- Performance monitoring completed successfully.

## Outcome

Successfully benchmarked Linux system performance using standard monitoring tools.
