#!/bin/bash

echo "System Health Report"
echo "--------------------"

echo "Hostname:"
hostname

echo ""
echo "Current User:"
whoami

echo ""
echo "Disk Usage:"
df -h /

echo ""
echo "Memory Usage:"
vm_stat

echo ""
echo "Current Date:"
date
