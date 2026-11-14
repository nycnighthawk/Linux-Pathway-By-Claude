---
{"title": "PR_SET_TAGGED_ADDR_CTRL(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_set_tagged_addr_ctrl.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_TAGGED_ADDR_CTRL(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_TAGGED_ADDR_CTRL(2const)           PR_SET_TAGGED_ADDR_CTRL(2const)

## [](#NAME)NAME

           PR_SET_TAGGED_ADDR_CTRL - control support for passing tagged user-
           space addresses to the kernel

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_TAGGED_ADDR_CTRL, long mode, 0L, 0L, 0L);

## [](#DESCRIPTION)DESCRIPTION

           Controls support for passing tagged user-space addresses to the
           kernel (i.e., addresses where bits 56—63 are not all zero).

           The level of support is selected by support, which can be one of
           the following:

           0L     Addresses that are passed for the purpose of being
                  dereferenced by the kernel must be untagged.

           PR_TAGGED_ADDR_ENABLE
                  Addresses that are passed for the purpose of being
                  dereferenced by the kernel may be tagged, with the
                  exceptions summarized below.

           On success, the mode specified in mode is set for the calling
           thread.

           If prctl(PR_SET_TAGGED_ADDR_CTRL, 0L, 0L, 0L, 0L) fails with
           EINVAL, then all addresses passed to the kernel must be untagged.

           Irrespective of which mode is set, addresses passed to certain
           interfaces must always be untagged:

           •  brk(2), mmap(2), shmat(2), shmdt(2), and the new_address
              argument of mremap(2).

              (Prior to Linux 5.6 these accepted tagged addresses, but the
              behavior may not be what you expect.  Don't rely on it.)

           •  ‘polymorphic’ interfaces that accept pointers to arbitrary
              types cast to a void * or other generic type, specifically
              prctl(), ioctl(2), and in general setsockopt(2) (only certain
              specific setsockopt(2) options allow tagged addresses).

           This list of exclusions may shrink when moving from one kernel
           version to a later kernel version.  While the kernel may make some
           guarantees for backwards compatibility reasons, for the purposes
           of new software the effect of passing tagged addresses to these
           interfaces is unspecified.

           The mode set by this call is inherited across fork(2) and
           clone(2).  The mode is reset by execve(2) to 0 (i.e., tagged
           addresses not permitted in the user/kernel ABI).

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL mode is invalid or unsupported.

           EINVAL This feature is disabled via /proc/sys/abi/
                  tagged_addr_disabled.

## [](#FILES)FILES

           /proc/sys/abi/tagged_addr_disabled

## [](#STANDARDS)STANDARDS

           Linux.  arm64 only.

## [](#HISTORY)HISTORY

           Linux 5.4 (arm64).

## [](#CAVEATS)CAVEATS

           This call is primarily intended for use by the run-time
           environment.  A successful PR_SET_TAGGED_ADDR_CTRL call elsewhere
           may crash the calling process.  The conditions for using it safely
           are complex and system-dependent.  Don't use it unless you know
           what you are doing.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_SET_TAGGED_ADDR_CTRL(2const)

           For more information, see the kernel source file
           Documentation/arm64/tagged-address-abi.rst.

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

    Linux man-pages 6.19            2026-02-08PR_SET_TAGGED_ADDR_CTRL(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_GET_TAGGED_ADDR_CTRL(2const)](../man2/PR_GET_TAGGED_ADDR_CTRL.2const.html),  [PR_SET_TAGGED_ADDR_CTRL(2const)](../man2/PR_SET_TAGGED_ADDR_CTRL.2const.html)

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
