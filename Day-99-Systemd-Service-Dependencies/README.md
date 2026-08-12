# Day 99 — Systemd Service Dependencies & Ordering

## Objective

Learn how systemd manages service dependencies and startup ordering using
Requires=, Wants=, After=, and Before=.

## Topics Covered

- Systemd service dependencies
- Service startup ordering
- Requires=
- Wants=
- After=
- Before=
- systemctl list-dependencies
- systemctl show
- Service dependency troubleshooting

## Lab Environment

- Ubuntu
- Docker container
- systemd
- systemctl
- journalctl

## Services Created

### Base Service

day99-base.service

Runs continuously and prints:

Day 99 base service is running

### Dependent Service

day99-dependent.service

Configured with:

Wants=day99-base.service
After=day99-base.service

## Commands Practiced

systemctl daemon-reload
systemctl start day99-base.service
systemctl stop day99-base.service
systemctl start day99-dependent.service
systemctl status day99-base.service
systemctl status day99-dependent.service
systemctl list-dependencies day99-dependent.service
systemctl show day99-dependent.service -p Wants -p After
journalctl -u day99-base.service -n 20 --no-pager
journalctl -u day99-dependent.service -n 20 --no-pager

## What I Learned

### Requires=

Creates a strong dependency.

If the required service fails or is stopped, the dependent service can also
be stopped.

### Wants=

Creates a weaker dependency.

The dependent service can continue running even if the wanted service is
stopped.

### After=

Controls startup ordering.

After= does NOT create a dependency by itself.

### Before=

Controls startup ordering in the opposite direction.

## Testing

Initially the dependent service used:

Requires=day99-base.service
After=day99-base.service

The behavior was tested by stopping the base service.

The dependency was then changed to:

Wants=day99-base.service
After=day99-base.service

The dependent service remained active when the base service was stopped,
demonstrating the difference between Requires= and Wants=.

## Important Interview Question

### Does After= create a dependency?

No.

After= only controls startup ordering.

Requires= or Wants= creates the dependency.

## Result

Day 99 completed successfully.
