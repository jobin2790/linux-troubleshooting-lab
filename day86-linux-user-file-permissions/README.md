# Day 86 – Linux User & File Permissions Lab

## Objective
Practice Linux user management, file ownership, and permissions.

## Commands Practiced

```bash
grep clouduser /etc/passwd
mkdir /project
touch /project/app.log
ls -ld /project
ls -l /project
chown clouduser:clouduser /project/app.log
chmod 640 /project/app.log
ls -l /project
id clouduser
```

## What I Learned

- Verified an existing Linux user.
- Created a project directory.
- Created a log file.
- Changed file ownership using `chown`.
- Set secure permissions using `chmod 640`.
- Verified permissions with `ls -l`.
- Checked user and group information with `id`.

## Result

Successfully managed Linux file ownership and permissions.
