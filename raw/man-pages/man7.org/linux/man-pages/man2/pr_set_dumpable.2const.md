---
{"title": "PR_SET_DUMPABLE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_set_dumpable.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_DUMPABLE(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_DUMPABLE(2const)                           PR_SET_DUMPABLE(2const)

## [](#NAME)NAME

           PR_SET_DUMPABLE - set the "dumpable" attribute of the calling
           process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_DUMPABLE, long dumpable);

## [](#DESCRIPTION)DESCRIPTION

           Set the state of the "dumpable" attribute, which determines
           whether core dumps are produced for the calling process upon
           delivery of a signal whose default behavior is to produce a core
           dump.

           dumpable must be either 0L (SUID_DUMP_DISABLE, process is not
           dumpable) or 1L (SUID_DUMP_USER, process is dumpable).

           Normally, the "dumpable" attribute is set to 1.  However, it is
           reset to the current value contained in the file /proc/sys/fs/
           suid_dumpable (which by default has the value 0), in the following
           circumstances:

           •  The process's effective user or group ID is changed.

           •  The process's filesystem user or group ID is changed (see
              credentials(7)).

           •  The process executes (execve(2)) a set-user-ID or set-group-ID
              program, resulting in a change of either the effective user ID
              or the effective group ID.

           •  The process executes (execve(2)) a program that has file
              capabilities (see capabilities(7)), but only if the permitted
              capabilities gained exceed those already permitted for the
              process.

           Processes that are not dumpable can not be attached via ptrace(2)
           PTRACE_ATTACH; see ptrace(2) for further details.

           If a process is not dumpable, the ownership of files in the
           process's /proc/pid directory is affected as described in
           proc_pid(5).

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL arg2 is neither SUID_DUMP_DISABLE nor SUID_DUMP_USER.

## [](#FILES)FILES

           /proc/sys/fs/suid_dumpable

           /proc/pid/

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.3.20.

           Between Linux 2.6.13 and Linux 2.6.17, the value 2L was also
           permitted, which caused any binary which normally would not be
           dumped to be dumped readable by root only; for security reasons,
           this feature has been removed.  (See also the description of
           /proc/sys/fs/suid_dumpable in proc_sys_fs(5).)

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_SET_DUMPABLE(2const)

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

    Linux man-pages 6.19            2026-02-08        PR_SET_DUMPABLE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_GET_DUMPABLE(2const)](../man2/PR_GET_DUMPABLE.2const.html),  [PR_SET_DUMPABLE(2const)](../man2/PR_SET_DUMPABLE.2const.html)

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
