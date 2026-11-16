# Lab: a character driver's file operations, in user space

No kernel build is needed. `setup` writes `kshim.h` (a stand-in for `copy_to_user`, `copy_from_user`, `struct file` and the ioctl macros), `mydev.h` (the interface) and `mydev.c` with three stub callbacks that return `-ENOSYS`.

## Your task

Implement `my_read`, `my_write` and `my_ioctl` in `mydev.c` exactly as the comments describe. They follow the real `file_operations` conventions:

- return the number of bytes transferred, **0 at end of data**, or a negative errno,
- use `*ppos` as the file position and advance it,
- a failed `copy_to_user` or `copy_from_user` (it returns the bytes *not* copied) is `-EFAULT`,
- an unknown ioctl command is `-ENOTTY`.

`check` builds a harness around your code and reports each behaviour that is wrong. Moving the same code into a real module needs only `file_operations`, `module_init` and registration with `misc_register` (covered in the lesson); that step needs a kernel build tree and is not part of the automatic check.
