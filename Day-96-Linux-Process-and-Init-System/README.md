# Day 96 – Linux Process and Init System

## Objective
Learn Linux process management, identify running processes, manage background jobs, and understand the init system.

## Environment
- Host OS: macOS
- Shell: zsh

## Commands Practiced

```bash
top
ps aux | grep bash
ps aux | grep nginx
echo $$
sleep 300 &
jobs
ps -ef | grep sleep
kill 1589
jobs
ps -p 1
ps aux
```

## Observations

- Monitored running processes using `top`.
- Searched for specific processes using `ps` and `grep`.
- Displayed the current shell PID using `echo $$`.
- Created a background process using `sleep 300 &`.
- Listed background jobs using `jobs`.
- Found the background process using `ps -ef`.
- Terminated the process using `kill`.
- Verified the process was terminated.
- Checked PID 1 on macOS (`launchd`).
- Learned that some Linux `ps` options (`-ejH`, `--sort`) are not supported on macOS because it uses BSD `ps`.

## Result

Successfully practiced Linux process management commands and understood the differences between Linux and macOS process tools.
