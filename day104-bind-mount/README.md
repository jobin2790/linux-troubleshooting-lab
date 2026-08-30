# Day 104 — Docker Bind Mounts

## Objective

Learn how Docker bind mounts allow containers to share files directly with the host machine.

## What I Learned

A bind mount maps a directory from the host machine into a container.

Unlike normal container storage, files stored through a bind mount remain on the host even after the container is removed.

## Practical Test

### 1. Created host directory

```bash
mkdir -p day104-bind-mount
