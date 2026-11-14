---
{"title": "sysctl(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/_sysctl.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sysctl(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sysctl(2)                  System Calls Manual                  sysctl(2)

## [](#NAME)NAME

           sysctl - read/write system parameters

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>
           #include <linux/sysctl.h>

           [[deprecated]] int _sysctl(struct __sysctl_args *args);

## [](#DESCRIPTION)DESCRIPTION

           This system call no longer exists on current kernels!  See NOTES.

           The _sysctl() call reads and/or writes kernel parameters.  For
           example, the hostname, or the maximum number of open files.  The
           argument has the form

               struct __sysctl_args {
                   int    *name;    /* integer vector describing variable */
                   int     nlen;    /* number of elements of this vector */
                   void   *oldval;  /* 0 or address where to store old value */
                   size_t *oldlenp; /* available room for old value,
                                       overwritten by actual size of old value */
                   void   *newval;  /* 0 or address of new value */
                   size_t  newlen;  /* size of new value */
               };

           This call does a search in a tree structure, possibly resembling a
           directory tree under /proc/sys, and if the requested item is found
           calls some appropriate routine to read or modify the value.

## [](#RETURN_VALUE)RETURN VALUE

           Upon successful completion, _sysctl() returns 0.  Otherwise, a
           value of -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EACCES
           EPERM  No search permission for one of the encountered
                  "directories", or no read permission where oldval was
                  nonzero, or no write permission where newval was nonzero.

           EFAULT The invocation asked for the previous value by setting
                  oldval non-NULL, but allowed zero room in oldlenp.

           ENOTDIR
                  name was not found.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           4.4BSD, Linux 1.3.57.  Removed in Linux 5.5, glibc 2.32.

           Only Linux has the /proc/sys mirror, and the object naming schemes
           differ between Linux and 4.4BSD, but the declaration of the
           sysctl() function is the same in both.

## [](#NOTES)NOTES

           Use of this system call was long discouraged: since Linux 2.6.24,
           uses of this system call result in warnings in the kernel log, and
           in Linux 5.5, the system call was finally removed.  Use the
           /proc/sys interface instead.

           Note that on older kernels where this system call still exists, it
           is available only if the kernel was configured with the
           CONFIG_SYSCTL_SYSCALL option.  Furthermore, glibc does not provide
           a wrapper for this system call, necessitating the use of
           syscall(2).

## [](#BUGS)BUGS

           The object names vary between kernel versions, making this system
           call worthless for applications.

           Not all available objects are properly documented.

           It is not yet possible to change operating system by writing to
           /proc/sys/kernel/ostype.

## [](#EXAMPLES)EXAMPLES

           #define _GNU_SOURCE
           #include <stdcountof.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <string.h>
           #include <sys/syscall.h>
           #include <unistd.h>

           #include <linux/sysctl.h>

           int _sysctl(struct __sysctl_args *args);

           #define OSNAMESZ 100

           int
           main(void)
           {
               int                   name[] = { CTL_KERN, KERN_OSTYPE };
               char                  osname[OSNAMESZ];
               size_t                osnamelth;
               struct __sysctl_args  args;

               memset(&args, 0, sizeof(args));
               args.name = name;
               args.nlen = countof(name);
               args.oldval = osname;
               args.oldlenp = &osnamelth;

               osnamelth = sizeof(osname);

               if (syscall(SYS__sysctl, &args) == -1) {
                   perror("_sysctl");
                   exit(EXIT_FAILURE);
               }
               printf("This machine is running %*s\n", (int) osnamelth, osname);
               exit(EXIT_SUCCESS);
           }

## [](#SEE_ALSO)SEE ALSO

           proc(5)

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

    Linux man-pages 6.19            2026-02-10                      sysctl(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [proc_sys(5)](../man5/proc_sys.5.html),  [sctp(7)](../man7/sctp.7.html)

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
