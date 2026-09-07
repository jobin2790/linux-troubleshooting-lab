# Day 105 — Docker Volumes

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
- `docker volume ls` can be used to list Docker volumes.

## Commands Used

### Create a Named Volume

```bash
docker volume create day105-data
```

### Verify the Volume

```bash
docker volume ls
```

Expected output should include:

```text
day105-data
```

### Run a Container with the Volume

```bash
docker run -d \
  --name day105-container-1 \
  -v day105-data:/data \
  alpine \
  sleep 3600
```

### Create a File Inside the Mounted Volume

```bash
docker exec day105-container-1 sh -c 'echo "Docker Volume Day 105" > /data/test.txt'
```

### Read the File

```bash
docker exec day105-container-1 cat /data/test.txt
```

Expected output:

```text
Docker Volume Day 105
```

## Test Volume Persistence

The important part of this lab is verifying that the data remains available after the original container is removed.

### Remove the First Container

```bash
docker rm -f day105-container-1
```

### Create a New Container Using the Same Volume

```bash
docker run -d \
  --name day105-container-2 \
  -v day105-data:/data \
  alpine \
  sleep 3600
```

### Verify Data Persistence

```bash
docker exec day105-container-2 cat /data/test.txt
```

Expected output:

```text
Docker Volume Day 105
```

This confirms that the data persisted even after the original container was removed.

## Inspect the Volume

```bash
docker volume inspect day105-data
```

This displays information such as:

- Volume name
- Driver
- Mount point
- Scope

## List Docker Volumes

```bash
docker volume ls
```

## Cleanup

### Remove the Test Container

```bash
docker rm -f day105-container-2
```

### Remove the Docker Volume

```bash
docker volume rm day105-data
```

### Verify the Volume Was Removed

```bash
docker volume ls
```

The `day105-data` volume should no longer appear.

## Result

Successfully tested Docker named volume persistence by:

1. Creating a named Docker volume.
2. Mounting the volume into a container.
3. Creating data inside the mounted volume.
4. Removing the original container.
5. Creating a new container using the same volume.
6. Accessing the original data from the new container.
7. Inspecting and removing the Docker volume.

This demonstrates that Docker named volumes allow data to persist independently of the container lifecycle.
