# Lab: lint a mailed patch

Reviewers spend their time on substance only if the mechanics are right. `setup` writes `lint.py`; implement `lint` for the checks listed in the file: subject prefix and length, sign-off, long message lines, whitespace and indentation style for the kernel and for QEMU.

The rules here are a simplified subset of `checkpatch.pl` in each project (to verify the current limits; the kernel's checker uses 75 columns for commit messages and QEMU's style document sets its own rules). Always run the real checker before sending.
