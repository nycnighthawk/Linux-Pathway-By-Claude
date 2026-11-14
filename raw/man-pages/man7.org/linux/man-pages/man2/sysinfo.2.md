---
{"title": "sysinfo(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/sysinfo.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sysinfo(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sysinfo(2)                 System Calls Manual                 sysinfo(2)

## [](#NAME)NAME

           sysinfo - return system information

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/sysinfo.h>

           int sysinfo(struct sysinfo *info);

## [](#DESCRIPTION)DESCRIPTION

           sysinfo() returns certain statistics on memory and swap usage, as
           well as the load average.

           Until Linux 2.3.16, sysinfo() returned information in the
           following structure:

               struct sysinfo {
                   long uptime;             /* Seconds since boot */
                   unsigned long loads[3];  /* 1, 5, and 15 minute load averages */
                   unsigned long totalram;  /* Total usable main memory size */
                   unsigned long freeram;   /* Available memory size */
                   unsigned long sharedram; /* Amount of shared memory */
                   unsigned long bufferram; /* Memory used by buffers */
                   unsigned long totalswap; /* Total swap space size */
                   unsigned long freeswap;  /* Swap space still available */
                   unsigned short procs;    /* Number of current processes */
                   char _f[22];             /* Pads structure to 64 bytes */
               };

           In the above structure, the sizes of the memory and swap fields
           are given in bytes.

           Since Linux 2.3.23 (i386) and Linux 2.3.48 (all architectures) the
           structure is:

               struct sysinfo {
                   long uptime;             /* Seconds since boot */
                   unsigned long loads[3];  /* 1, 5, and 15 minute load averages */
                   unsigned long totalram;  /* Total usable main memory size */
                   unsigned long freeram;   /* Available memory size */
                   unsigned long sharedram; /* Amount of shared memory */
                   unsigned long bufferram; /* Memory used by buffers */
                   unsigned long totalswap; /* Total swap space size */
                   unsigned long freeswap;  /* Swap space still available */
                   unsigned short procs;    /* Number of current processes */
                   unsigned long totalhigh; /* Total high memory size */
                   unsigned long freehigh;  /* Available high memory size */
                   unsigned int mem_unit;   /* Memory unit size in bytes */
                   char _f[20-2*sizeof(long)-sizeof(int)];
                                            /* Padding to 64 bytes */
               };

           In the above structure, sizes of the memory and swap fields are
           given as multiples of mem_unit bytes.

## [](#RETURN_VALUE)RETURN VALUE

           On success, sysinfo() returns zero.  On error, -1 is returned, and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT info is not a valid address.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 0.98.pl6.

## [](#NOTES)NOTES

           All of the information provided by this system call is also
           available via /proc/meminfo and /proc/loadavg.

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

    Linux man-pages 6.19            2026-02-08                     sysinfo(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [get_phys_pages(3)](../man3/get_phys_pages.3.html)

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
