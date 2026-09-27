# Day 111 – Docker Security

## Objective

Learn basic Docker container security by running containers with:

- Non-root user
- Read-only filesystem
- Dropped Linux capabilities
- No new privileges

## Security Configuration

```bash
docker run --rm -it \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --user 65534:65534 \
  --name day111-final \
  alpine sh


## Verification

### 1. Non-root user

```bash
id
uid=65534(nobody) gid=65534(nobody)


touch test.txt
touch: test.txt: Read-only file system

cat /proc/self/status | grep Cap
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 0000000000000000
CapAmb: 0000000000000000


cat /proc/self/status | grep NoNewPrivs
NoNewPrivs: 1


## Result

The container was successfully hardened using:

- Non-root user (`65534:65534`)
- Read-only filesystem
- All Linux capabilities dropped
- `no-new-privileges` enabled

These settings reduce the container's attack surface and limit what a compromised process can do.

## Cleanup

```bash
docker ps -a --filter name=day111
docker rm -f day111-final'''
