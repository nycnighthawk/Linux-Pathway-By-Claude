---
{"title": "PR_MPX_ENABLE_MANAGEMENT(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_mpx_disable_management.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_MPX_ENABLE_MANAGEMENT(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_MPX_ENABLE_MANAGEMENT(2const)         PR_MPX_ENABLE_MANAGEMENT(2const)

## [](#NAME)NAME

           PR_MPX_ENABLE_MANAGEMENT, PR_MPX_DISABLE_MANAGEMENT - enable or
           disable kernel management of Memory Protection eXtensions (MPX)

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           [[deprecated]] int prctl(PR_MPX_ENABLE_MANAGEMENT, 0L, 0L, 0L, 0L);
           [[deprecated]] int prctl(PR_MPX_DISABLE_MANAGEMENT, 0L, 0L, 0L, 0L);

## [](#DESCRIPTION)DESCRIPTION

           Enable or disable kernel management of Memory Protection
           eXtensions (MPX) bounds tables.

           MPX is a hardware-assisted mechanism for performing bounds
           checking on pointers.  It consists of a set of registers storing
           bounds information and a set of special instruction prefixes that
           tell the CPU on which instructions it should do bounds
           enforcement.  There is a limited number of these registers and
           when there are more pointers than registers, their contents must
           be "spilled" into a set of tables.  These tables are called
           "bounds tables" and the MPX prctl() operations control whether the
           kernel manages their allocation and freeing.

           When management is enabled, the kernel will take over allocation
           and freeing of the bounds tables.  It does this by trapping the
           #BR exceptions that result at first use of missing bounds tables
           and instead of delivering the exception to user space, it
           allocates the table and populates the bounds directory with the
           location of the new table.  For freeing, the kernel checks to see
           if bounds tables are present for memory which is not allocated,
           and frees them if so.

           Before enabling MPX management using PR_MPX_ENABLE_MANAGEMENT, the
           application must first have allocated a user-space buffer for the
           bounds directory and placed the location of that directory in the
           bndcfgu register.

           These calls fail if the CPU or kernel does not support MPX.
           Kernel support for MPX is enabled via the CONFIG_X86_INTEL_MPX
           configuration option.  You can check whether the CPU supports MPX
           by looking for the mpx CPUID bit, like with the following command:

               cat /proc/cpuinfo | grep ' mpx '

           A thread may not switch in or out of long (64-bit) mode while MPX
           is enabled.

           All threads in a process are affected by these calls.

           The child of a fork(2) inherits the state of MPX management.
           During execve(2), MPX management is reset to a state as if
           PR_MPX_DISABLE_MANAGEMENT had been called.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           ENXIO  The kernel or the CPU does not support MPX management.
                  Check that the kernel and processor have MPX support.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           Linux 3.19.  Removed in Linux 5.4.  Only on x86.

           Due to a lack of toolchain support, PR_MPX_ENABLE_MANAGEMENT and
           PR_MPX_DISABLE_MANAGEMENT are not supported in Linux 5.4 and
           later.

## [](#SEE_ALSO)SEE ALSO

           prctl(2)

           For further information on Intel MPX, see the kernel source file
           Documentation/x86/intel_mpx.rst.

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

    Linux man-pages 6.19            2026-02-08PR_MPX_ENABLE_MANAGEMENT(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html)

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
