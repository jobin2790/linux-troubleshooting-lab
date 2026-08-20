# Day 102 — Docker Multi-Stage Builds

## Objective

Learn how Docker multi-stage builds separate the build environment from the final runtime image.

## What I Learned

- Single-stage builds keep build dependencies in the final image.
- Multi-stage builds use separate build and runtime stages.
- The builder stage compiles/builds the application.
- The runtime stage copies only the required application files.
- Multi-stage builds can reduce image size and attack surface.

## Dockerfiles

### Single-stage

`Dockerfile.single` uses one image for both building and running the application.

### Multi-stage

`Dockerfile.multi` uses:

1. Build stage
2. Runtime stage

The runtime stage copies only the required files from the builder.

## Image Comparison

| Image | Size |
|---|---:|
| day102-single | 231 MB |
| day102-multi | 228 MB |

## Testing

### Single-stage

```bash
docker run -d --name day102-single-container -p 3001:3000 day102-single
curl http://localhost:3001

### Multi-stage

```bash
docker run -d --name day102-multi-container -p 3002:3000 day102-multi
curl http://localhost:3002

## Conclusion

Multi-stage Docker builds separate the build environment from the final runtime environment. The runtime stage copies only the required application files, producing a cleaner production image.
