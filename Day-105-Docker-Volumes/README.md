# Day 105 – Docker Volumes

## Objective

Learn how Docker named volumes provide persistent storage for containers.

## What I Learned

- Docker containers are temporary by default.
- Data stored only inside a container can be lost when the container is removed.
- Docker volumes allow data to persist independently of the container.
- A named volume can be mounted into a container using `-v`.
- The same volume can be mounted into multiple containers.
- Data stored in a named volume remains available even after the original container is removed.
- `docker volume inspect` can be used to inspect volume details.

## Commands Used

### Create a named volume

```bash
docker volume create day105-data
```

### Run a container with the volume

```bash
docker run -d \
  --name day105-container-5 \
  -v day105-data:/data \
  alpine \
  sleep 3600
```

### Create a file inside the mounted volume

```bash
docker exec day105-container-5 sh -c 'echo "Docker Volume Day 105" > /data/test.txt'
```

### Read the file

```bash
docker exec day105-container-5 cat /data/test.txt
```

Expected output:

```text
Docker Volume Day 105
```

### Remove the first container

```bash
docker rm -f day105-container-5
```

### Create a new container using the same volume

```bash
docker run -d \
  --name day105-container-6 \
  -v day105-data:/data \
  alpine \
  sleep 3600
```

### Verify data persistence

```bash
docker exec day105-container-6 cat /data/test.txt
```

Expected output:

```text
Docker Volume Day 105
```

This confirms that the data persisted even after the original container was removed.

### Inspect the volume

```bash
docker volume inspect day105-data
```

### List Docker volumes

```bash
docker volume ls
```

## Cleanup

Remove the test container:

```bash
docker rm -f day105-container-6
```

Remove the Docker volume:

```bash
docker volume rm day105-data
```

Verify that the volume was removed:

```bash
docker volume ls
```

## Result

Successfully tested Docker named volume persistence by creating data in one container, removing that container, and accessing the same data from a new container using the same Docker volume.
