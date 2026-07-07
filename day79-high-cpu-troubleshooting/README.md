# Day 79 - High CPU Troubleshooting

## Scenario

A system is experiencing slow performance due to high CPU usage.

The goal of this troubleshooting lab was to identify the process consuming high CPU, inspect the process, terminate it safely, and verify that CPU usage returned to normal.

## Step 1 - Simulate High CPU Usage

Created a CPU-intensive process using:

```bash
yes > /dev/null &
```

The process started in the background and generated continuous CPU load.

## Step 2 - Monitor CPU Usage

Used the following command to monitor system resource usage:

```bash
top
```

The `yes` process was identified consuming 100% CPU.

The process details observed were:

```text
PID: 2017
COMMAND: yes
CPU: 100%
```

## Step 3 - Inspect the Process

Used the following command to inspect the high CPU process:

```bash
ps -p 2017 -o pid,ppid,user,%cpu,%mem,command
```

The output confirmed that the `yes` process was owned by the current user and was consuming 100% CPU.

The process inspection helped verify the PID, parent process ID, user, CPU usage, memory usage, and command before taking action.

## Step 4 - Terminate the Process

The high CPU process was terminated using:

```bash
kill 2017
```

The `kill` command sent the default SIGTERM signal to the process.

SIGTERM was used to request normal process termination instead of immediately forcing termination with SIGKILL.

## Step 5 - Verify Process Termination

Verified whether the process was still running using:

```bash
ps -p 2017
```

The process was no longer listed, confirming that it had been terminated.

## Step 6 - Verify System Recovery

CPU usage was checked again using:

```bash
top
```

The `yes` process was no longer present.

CPU idle percentage returned to approximately 98%, confirming that CPU usage returned to normal.

## Troubleshooting Workflow

1. Monitor system CPU usage using `top`.
2. Identify the process consuming high CPU.
3. Note the Process ID (PID).
4. Inspect the process using `ps`.
5. Verify the process details before taking action.
6. Terminate the process safely using `kill`.
7. Verify that the process is no longer running.
8. Check CPU usage again.
9. Confirm system recovery.

## Commands Used

```bash
yes > /dev/null &
top
ps -p 2017 -o pid,ppid,user,%cpu,%mem,command
kill 2017
ps -p 2017
top
```

## Key Learning

I learned how to troubleshoot a high CPU usage issue by identifying a resource-intensive process, inspecting its process details, terminating it safely using SIGTERM, and verifying system recovery.

I also learned that a process should be inspected and verified before termination instead of immediately using `kill -9`.

## Environment

macOS Terminal using Unix process monitoring and troubleshooting commands.

The troubleshooting workflow and commands practiced in this lab are relevant to Linux system administration and cloud support troubleshooting.

## Result

Successfully identified a process consuming 100% CPU, inspected the process, terminated it safely, and verified that CPU usage returned to normal
