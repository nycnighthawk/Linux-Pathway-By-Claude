---
{"title": "reboot(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/reboot.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# reboot(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    reboot(2)                  System Calls Manual                  reboot(2)

## [](#NAME)NAME

           reboot - reboot or enable/disable Ctrl-Alt-Del

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           /* Since Linux 2.1.30 there are symbolic names LINUX_REBOOT_*
              for the constants and a fourth argument to the call: */

           #include <linux/reboot.h>  /* Definition of LINUX_REBOOT_* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_reboot, int magic, int magic2, int op, void *arg);

           /* Under glibc and most alternative libc's (including uclibc, dietlibc,
              musl and a few others), some of the constants involved have gotten
              symbolic names RB_*, and the library call is a 1-argument
              wrapper around the system call: */

           #include <sys/reboot.h>    /* Definition of RB_* constants */
           #include <unistd.h>

           int reboot(int op);

## [](#DESCRIPTION)DESCRIPTION

           The reboot() call reboots the system, or enables/disables the
           reboot keystroke (abbreviated CAD, since the default is Ctrl-Alt-
           Delete; it can be changed using loadkeys(1)).

           This system call fails (with the error EINVAL) unless magic equals
           LINUX_REBOOT_MAGIC1 (that is, 0xfee1dead) and magic2 equals
           LINUX_REBOOT_MAGIC2 (that is, 0x28121969).  However, since Linux
           2.1.17 also LINUX_REBOOT_MAGIC2A (that is, 0x05121996) and since
           Linux 2.1.97 also LINUX_REBOOT_MAGIC2B (that is, 0x16041998) and
           since Linux 2.5.71 also LINUX_REBOOT_MAGIC2C (that is, 0x20112000)
           are permitted as values for magic2.  (The hexadecimal values of
           these constants are meaningful.)

           The op argument can have the following values:

           LINUX_REBOOT_CMD_CAD_OFF
                  (RB_DISABLE_CAD, 0).  CAD is disabled.  This means that the
                  CAD keystroke will cause a SIGINT signal to be sent to init
                  (process 1), whereupon this process may decide upon a
                  proper action (maybe: kill all processes, sync, reboot).

           LINUX_REBOOT_CMD_CAD_ON
                  (RB_ENABLE_CAD, 0x89abcdef).  CAD is enabled.  This means
                  that the CAD keystroke will immediately cause the action
                  associated with LINUX_REBOOT_CMD_RESTART.

           LINUX_REBOOT_CMD_HALT
                  (RB_HALT_SYSTEM, 0xcdef0123; since Linux 1.1.76).  The
                  message "System halted." is printed, and the system is
                  halted.  Control is given to the ROM monitor, if there is
                  one.  If not preceded by a sync(2), data will be lost.

           LINUX_REBOOT_CMD_KEXEC
                  (RB_KEXEC, 0x45584543, since Linux 2.6.13).  Execute a
                  kernel that has been loaded earlier with kexec_load(2).
                  This option is available only if the kernel was configured
                  with CONFIG_KEXEC.

           LINUX_REBOOT_CMD_POWER_OFF
                  (RB_POWER_OFF, 0x4321fedc; since Linux 2.1.30).  The
                  message "Power down." is printed, the system is stopped,
                  and all power is removed from the system, if possible.  If
                  not preceded by a sync(2), data will be lost.

           LINUX_REBOOT_CMD_RESTART
                  (RB_AUTOBOOT, 0x1234567).  The message "Restarting system."
                  is printed, and a default restart is performed immediately.
                  If not preceded by a sync(2), data will be lost.

           LINUX_REBOOT_CMD_RESTART2
                  (0xa1b2c3d4; since Linux 2.1.30).  The message "Restarting
                  system with command '%s'" is printed, and a restart (using
                  the command string given in arg) is performed immediately.
                  If not preceded by a sync(2), data will be lost.

           LINUX_REBOOT_CMD_SW_SUSPEND
                  (RB_SW_SUSPEND, 0xd000fce1; since Linux 2.5.18).  The
                  system is suspended (hibernated) to disk.  This option is
                  available only if the kernel was configured with
                  CONFIG_HIBERNATION.

           Only the superuser may call reboot().

           The precise effect of the above actions depends on the
           architecture.  For the i386 architecture, the additional argument
           does not do anything at present (2.1.122), but the type of reboot
           can be determined by kernel command-line arguments ("reboot=...")
           to be either warm or cold, and either hard or through the BIOS.

       Behavior inside PID namespaces
           Since Linux 3.4, if reboot() is called from a PID namespace other
           than the initial PID namespace with one of the op values listed
           below, it performs a "reboot" of that namespace: the "init"
           process of the PID namespace is immediately terminated, with the
           effects described in pid_namespaces(7).

           The values that can be supplied in op when calling reboot() in
           this case are as follows:

           LINUX_REBOOT_CMD_RESTART
           LINUX_REBOOT_CMD_RESTART2
                  The "init" process is terminated, and wait(2) in the parent
                  process reports that the child was killed with a SIGHUP
                  signal.

           LINUX_REBOOT_CMD_POWER_OFF
           LINUX_REBOOT_CMD_HALT
                  The "init" process is terminated, and wait(2) in the parent
                  process reports that the child was killed with a SIGINT
                  signal.

           For the other op values, reboot() returns -1 and errno is set to
           EINVAL.

## [](#RETURN_VALUE)RETURN VALUE

           For the values of op that stop or restart the system, a successful
           call to reboot() does not return.  For the other op values, zero
           is returned on success.  In all cases, -1 is returned on failure,
           and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Problem with getting user-space data under
                  LINUX_REBOOT_CMD_RESTART2.

           EINVAL Bad magic numbers or op.

           EPERM  The calling process has insufficient privilege to call
                  reboot(); the caller must have the CAP_SYS_BOOT inside its
                  user namespace.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#SEE_ALSO)SEE ALSO

           systemctl(1), systemd(1), kexec_load(2), sync(2), bootparam(7),
           capabilities(7), ctrlaltdel(8), halt(8), shutdown(8)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08                      reboot(2)

------------------------------------------------------------------------

Pages that refer to this page: [systemctl(1)](../man1/systemctl.1.html),  [kexec_load(2)](../man2/kexec_load.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [org.freedesktop.login1(5)](../man5/org.freedesktop.login1.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [pid_namespaces(7)](../man7/pid_namespaces.7.html),  [systemd-poweroff.service(8)](../man8/systemd-poweroff.service.8.html)

------------------------------------------------------------------------

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
