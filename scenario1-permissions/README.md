# Scenario 1: File Permission Issue

## Problem
Application could not access app.log because of incorrect permissions.

## Investigation

```bash
ls -l app.log
Output:

-r--------@

## Fix

chmod 644 app.log

## Verification

ls -l app.log

Output:

-rw-r--r--

## Skills Demonstrated

- chmod
- ls -l
- Linux file permissions
- Troubleshooting
