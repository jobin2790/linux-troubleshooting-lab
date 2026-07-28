# Day 91 - Filesystem Integrity & Disk Repair (fsck)

## Objective
Learn how to inspect Linux filesystems and understand filesystem integrity checks using `fsck`.

## Commands Practiced

```bash
lsblk
df -h
mount
fsck -N /dev/vda1
fsck -n /dev/vda1
```

## Output Summary

- Listed block devices using `lsblk`.
- Checked filesystem usage with `df -h`.
- Displayed mounted filesystems using `mount`.
- Previewed the `fsck` command with `fsck -N`.
- Attempted a read-only filesystem check using `fsck -n`.
- Observed that `fsck` cannot safely check a mounted filesystem inside a Docker container.

## What I Learned

- `lsblk` displays available disks and partitions.
- `df -h` shows filesystem usage in a human-readable format.
- `mount` lists mounted filesystems.
- `fsck -N` previews what `fsck` would do without making changes.
- `fsck` should be run on an unmounted filesystem to avoid corruption.
- Docker containers have limitations for filesystem repair because the root filesystem is mounted.

## Conclusion

Successfully explored Linux filesystem integrity concepts and understood how `fsck` works and why it should not be run on a mounted root filesystem.
