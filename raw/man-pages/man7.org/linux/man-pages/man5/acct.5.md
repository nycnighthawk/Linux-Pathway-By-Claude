---
{"title": "acct(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/acct.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# acct(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    acct(5)                    File Formats Manual                    acct(5)

## [](#NAME)NAME

           acct - process accounting file

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/acct.h>

## [](#DESCRIPTION)DESCRIPTION

           If the kernel is built with the process accounting option enabled
           (CONFIG_BSD_PROCESS_ACCT), then calling acct(2) starts process
           accounting, for example:

               acct("/var/log/pacct");

           When process accounting is enabled, the kernel writes a record to
           the accounting file as each process on the system terminates.
           This record contains information about the terminated process, and
           is defined in <sys/acct.h> as follows:

               #define ACCT_COMM 16

               typedef u_int16_t comp_t;

               struct acct {
                   char ac_flag;           /* Accounting flags */
                   u_int16_t ac_uid;       /* Accounting user ID */
                   u_int16_t ac_gid;       /* Accounting group ID */
                   u_int16_t ac_tty;       /* Controlling terminal */
                   u_int32_t ac_btime;     /* Process creation time
                                              (seconds since the Epoch) */
                   comp_t    ac_utime;     /* User CPU time */
                   comp_t    ac_stime;     /* System CPU time */
                   comp_t    ac_etime;     /* Elapsed time */
                   comp_t    ac_mem;       /* Average memory usage (kB) */
                   comp_t    ac_io;        /* Characters transferred (unused) */
                   comp_t    ac_rw;        /* Blocks read or written (unused) */
                   comp_t    ac_minflt;    /* Minor page faults */
                   comp_t    ac_majflt;    /* Major page faults */
                   comp_t    ac_swaps;     /* Number of swaps (unused) */
                   u_int32_t ac_exitcode;  /* Process termination status
                                              (see wait(2)) */
                   char      ac_comm[ACCT_COMM+1];
                                           /* Command name (basename of last
                                              executed command; null-terminated) */
                   char      ac_pad[X];    /* padding bytes */
               };

               enum {          /* Bits that may be set in ac_flag field */
                   AFORK = 0x01,           /* Has executed fork, but no exec */
                   ASU   = 0x02,           /* Used superuser privileges */
                   ACORE = 0x08,           /* Dumped core */
                   AXSIG = 0x10            /* Killed by a signal */
               };

           The comp_t data type is a floating-point value consisting of a
           3-bit, base-8 exponent, and a 13-bit mantissa.  A value, c, of
           this type can be converted to a (long) integer as follows:

               v = (c & 0x1fff) << (((c >> 13) & 0x7) * 3);

           The ac_utime, ac_stime, and ac_etime fields measure time in "clock
           ticks"; divide these values by sysconf(_SC_CLK_TCK) to convert
           them to seconds.

       Version 3 accounting file format
           Since Linux 2.6.8, an optional alternative version of the
           accounting file can be produced if the CONFIG_BSD_PROCESS_ACCT_V3
           option is set when building the kernel.  With this option is set,
           the records written to the accounting file contain additional
           fields, and the width of c_uid and ac_gid fields is widened from
           16 to 32 bits (in line with the increased size of UID and GIDs in
           Linux 2.4 and later).  The records are defined as follows:

               struct acct_v3 {
                   char      ac_flag;      /* Flags */
                   char      ac_version;   /* Always set to ACCT_VERSION (3) */
                   u_int16_t ac_tty;       /* Controlling terminal */
                   u_int32_t ac_exitcode;  /* Process termination status */
                   u_int32_t ac_uid;       /* Real user ID */
                   u_int32_t ac_gid;       /* Real group ID */
                   u_int32_t ac_pid;       /* Process ID */
                   u_int32_t ac_ppid;      /* Parent process ID */
                   u_int32_t ac_btime;     /* Process creation time */
                   float     ac_etime;     /* Elapsed time */
                   comp_t    ac_utime;     /* User CPU time */
                   comp_t    ac_stime;     /* System time */
                   comp_t    ac_mem;       /* Average memory usage (kB) */
                   comp_t    ac_io;        /* Characters transferred (unused) */
                   comp_t    ac_rw;        /* Blocks read or written
                                              (unused) */
                   comp_t    ac_minflt;    /* Minor page faults */
                   comp_t    ac_majflt;    /* Major page faults */
                   comp_t    ac_swaps;     /* Number of swaps (unused) */
                   char      ac_comm[ACCT_COMM]; /* Command name */
               };

## [](#VERSIONS)VERSIONS

           Although it is present on most systems, it is not standardized,
           and the details vary somewhat between systems.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           glibc 2.6.

           Process accounting originated on BSD.

## [](#NOTES)NOTES

           Records in the accounting file are ordered by termination time of
           the process.

           Up to and including Linux 2.6.9, a separate accounting record is
           written for each thread created using the NPTL threading library;
           since Linux 2.6.10, a single accounting record is written for the
           entire process on termination of the last thread in the process.

           The /proc/sys/kernel/acct file, described in proc(5), defines
           settings that control the behavior of process accounting when disk
           space runs low.

## [](#SEE_ALSO)SEE ALSO

           lastcomm(1), acct(2), accton(8), sa(8)

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

    Linux man-pages 6.19            2026-02-08                        acct(5)

------------------------------------------------------------------------

Pages that refer to this page: [lastcomm(1)](../man1/lastcomm.1.html),  [acct(2)](../man2/acct.2.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [accton(8)](../man8/accton.8.html),  [sa(8)](../man8/sa.8.html)

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
