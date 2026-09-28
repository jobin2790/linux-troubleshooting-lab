# Day 112 — Docker Multi-Stage Builds

## Objective

Learn how to use Docker multi-stage builds to separate the build environment from the final runtime image.

The main goal was to:

- Create a Python virtual environment in a builder stage
- Install application dependencies
- Copy only the required virtual environment and application files into the runtime stage
- Reduce unnecessary build dependencies from the final image
- Build and run the final Docker image successfully

---

## Project Structure

```text
Day-112-Docker-Multi-Stage-Builds/
├── app/
│   └── app.py
├── screenshots/
│   ├── Screenshot 2026-09-29 at 2.59.21 AM.png
│   ├── Screenshot 2026-09-29 at 2.59.27 AM.png
│   └── Screenshot 2026-09-29 at 2.59.32 AM.png
├── Dockerfile
├── requirements.txt
└── README.md
