---
{"title": "PR_SET_MM_EXE_FILE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_set_mm_exe_file.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_MM_EXE_FILE(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_MM_EXE_FILE(2const)                     PR_SET_MM_EXE_FILE(2const)

## [](#NAME)NAME

           PR_SET_MM_EXE_FILE - modify kernel memory map descriptor fields

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_MM, PR_SET_MM_EXE_FILE, long fd, 0L, 0L);

## [](#DESCRIPTION)DESCRIPTION

           Supersede the /proc/pid/exe symbolic link with a new one pointing
           to a new executable file identified by the file descriptor
           provided in the fd argument.  The file descriptor should be
           obtained with a regular open(2) call.

           To change the symbolic link, one needs to unmap all existing
           executable memory areas, including those created by the kernel
           itself (for example the kernel usually creates at least one
           executable memory area for the ELF .text section).

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EACCES The file is not executable.

           EBADF  The file descriptor passed in fd is not valid.

           EBUSY  This is the second attempt to change the /proc/pid/exe
                  symbolic link.

## [](#FILES)FILES

           /proc/pid/exe

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 3.5.

           In Linux 4.9 and earlier, the PR_SET_MM_EXE_FILE operation can be
           performed only once in a process's lifetime; attempting to perform
           the operation a second time results in the error EPERM.  This
           restriction was enforced for security reasons that were
           subsequently deemed specious, and the restriction was removed in
           Linux 4.10 because some user-space applications needed to perform
           this operation more than once.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_SET_MM(2const), proc_pid_exe(5)

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

    Linux man-pages 6.19            2026-02-08     PR_SET_MM_EXE_FILE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [PR_SET_MM(2const)](../man2/PR_SET_MM.2const.html),  [PR_SET_MM_MAP(2const)](../man2/PR_SET_MM_MAP.2const.html)

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
