# Day 80 - Disk Usage Troubleshooting

## Scenario

A Linux system is experiencing a disk usage issue caused by oversized log files.

The goal of this troubleshooting lab was to inspect filesystem usage, identify directories and files consuming disk space, remove an unnecessary test log file, and verify disk usage after cleanup.

## Environment

Ubuntu 26.04 LTS running inside a Docker container.

Container name:

```text
day80-disk-lab
```

## Step 1 - Verify Linux Environment

Verified the operating system using:

```bash
cat /etc/os-release
```

The output confirmed that the troubleshooting environment was Ubuntu Linux.

## Step 2 - Check Filesystem Usage

Checked filesystem disk usage using:

```bash
df -h
```

The main overlay filesystem showed approximately:

```text
Size: 224G
Used: 1.4G
Available: 211G
Use: 1%
```

The filesystem was not actually full.

This lab simulated an oversized log file investigation and cleanup scenario.

## Step 3 - Create the Test Log Directory

Created a test log directory using:

```bash
mkdir -p /var/log/day80-lab
```

## Step 4 - Simulate Oversized Log Files

Created a 200 MB application log file:

```bash
dd if=/dev/zero of=/var/log/day80-lab/app.log bs=1M count=200
```

Created a 300 MB error log file:

```bash
dd if=/dev/zero of=/var/log/day80-lab/error.log bs=1M count=300
```

Checked the total directory size:

```bash
du -sh /var/log/day80-lab
```

The directory was consuming approximately 500 MB of disk space.

## Step 5 - Identify the Large Directory

Inspected disk usage under `/var/log` using:

```bash
du -h /var/log | sort -h
```

The output identified `/var/log/day80-lab` as the largest directory under `/var/log`.

The directory was consuming approximately 501 MB.

## Step 6 - Identify the Largest Files

Used the following command:

```bash
du -ah /var/log/day80-lab | sort -rh | head
```

The output showed:

```text
501M  /var/log/day80-lab
300M  /var/log/day80-lab/error.log
200M  /var/log/day80-lab/app.log
```

The largest individual file was:

```text
/var/log/day80-lab/error.log
```

The file was consuming approximately 300 MB.

## Step 7 - Remove the Unnecessary Test Log

Because `error.log` was a controlled test file created specifically for this lab, it was safe to remove.

Removed the file using:

```bash
rm /var/log/day80-lab/error.log
```

In a production environment, a large log file should be investigated before deletion.

The application requirements, retention policy, and log rotation configuration should be checked before removing production logs.

## Step 8 - Verify Disk Cleanup

Checked the directory size again:

```bash
du -sh /var/log/day80-lab
```

The directory size decreased from approximately 501 MB to approximately 201 MB.

Checked the remaining files using:

```bash
du -ah /var/log/day80-lab | sort -rh | head
```

The remaining file was:

```text
200M  /var/log/day80-lab/app.log
```

## Step 9 - Verify Filesystem Usage

Checked filesystem usage again using:

```bash
df -h
```

The filesystem remained healthy and the oversized test log file had been successfully removed.

## Troubleshooting Workflow

1. Check filesystem usage using `df -h`.
2. Identify directories consuming disk space using `du`.
3. Sort disk usage results by size.
4. Identify the largest individual files.
5. Verify the file before taking action.
6. Remove unnecessary files only when safe.
7. Check directory usage again.
8. Check filesystem usage again.
9. Confirm disk cleanup.

## Commands Used

```bash
cat /etc/os-release
df -h
mkdir -p /var/log/day80-lab
dd if=/dev/zero of=/var/log/day80-lab/app.log bs=1M count=200
dd if=/dev/zero of=/var/log/day80-lab/error.log bs=1M count=300
du -sh /var/log/day80-lab
du -h /var/log | sort -h
du -ah /var/log/day80-lab | sort -rh | head
rm /var/log/day80-lab/error.log
du -sh /var/log/day80-lab
du -ah /var/log/day80-lab | sort -rh | head
df -h
```

## Key Learning

I learned how to investigate Linux disk usage using `df` and `du`.

I learned how to identify directories and individual files consuming disk space by combining `du`, `sort`, and `head`.

I also learned that large log files should not be blindly deleted on production systems. The file should be verified and application requirements, retention policies, and log rotation should be considered before cleanup.

## Result

Successfully investigated a simulated oversized log file issue inside an Ubuntu Linux Docker container.

Identified a 300 MB test error log as the largest individual file, removed it safely, and verified that the test log directory decreased from approximately 501 MB to 201 MB.
