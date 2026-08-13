# Day 101 — Docker Image Optimization

## Objective
Learn how Dockerfile structure and layer management affect Docker image size.

## What I Practiced

- Compared a poorly optimized Docker image with an optimized image
- Used `docker images` to compare image sizes
- Used `docker history` to inspect Docker image layers
- Used `apk add --no-cache` to reduce unnecessary package cache
- Compared Dockerfile layers and build results
- Tested the final optimized image

## Images Compared

| Image | Size |
|---|---:|
| day101-app-bad | ~27.8 MB |
| day101-app-optimized | ~21.7 MB |
| day101-app-final | ~13.5 MB |

## Key Learning

Docker image optimization depends heavily on:

1. Choosing a small base image
2. Reducing unnecessary layers
3. Avoiding package-cache files
4. Combining related commands when appropriate
5. Keeping only required files in the final image

## Commands Practiced

```bash
docker images
docker history day101-app-bad
docker history day101-app-optimized
docker history day101-app-final
docker run --rm day101-app-final
