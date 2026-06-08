# Scenario 2: Process Management

## Problem

A background application process was consuming resources.

## Investigation

ps aux | grep sleep

## Fix

kill <PID>

## Verification

ps aux | grep sleep

Process no longer running.

## Skills Demonstrated

- ps aux
- grep
- kill
- Process monitoring
- Process troubleshooting
