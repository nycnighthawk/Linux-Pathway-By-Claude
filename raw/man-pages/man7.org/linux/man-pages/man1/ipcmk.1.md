---
{"title": "ipcmk(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ipcmk.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ipcmk(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPCMK(1)                      User Commands                      IPCMK(1)

## [](#NAME)NAME

           ipcmk - make various IPC resources

## [](#SYNOPSIS)SYNOPSIS

           ipcmk [options]

## [](#DESCRIPTION)DESCRIPTION

           ipcmk allows you to create POSIX and System V inter-process
           communication (IPC) objects: shared memory segments, message
           queues, and semaphore (arrays for System V).

## [](#OPTIONS)OPTIONS

           Resources can be specified with these options:

           -M, --shmem size
               Create a shared memory segment of size bytes. The size
               argument may be followed by the multiplicative suffixes KiB
               (=1024), MiB (=1024*1024), and so on for GiB, etc. (the "iB"
               is optional, e.g., "K" has the same meaning as "KiB") or the
               suffixes KB (=1000), MB (=1000*1000), and so on for GB, etc.

           -m, --posix-shmem size
               Create a POSIX shared memory segment of size bytes. The size
               argument may be followed by the multiplicative suffixes KiB
               (=1024), MiB (=1024*1024), and so on for GiB, etc. (the "iB"
               is optional, e.g., "K" has the same meaning as "KiB") or the
               suffixes KB (=1000), MB (=1000*1000), and so on for GB, etc.

           -Q, --queue
               Create a message queue.

           -q, --posix-mqueue
               Create a POSIX message queue.

           -S, --semaphore number
               Create a semaphore array with number of elements.

           -s, --posix-semaphore
               Create a POSIX named semaphore.

           -n, --name name
               Name of the POSIX IPC object. This option is mandatory for
               POSIX IPC objects.

           Other options are:

           -p, --mode mode
               Access permissions for the resource. Default is 0644.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#AUTHORS)AUTHORS

           Hayden A. James <hayden.james@gmail.com>, Prasanna Paithankar
           <paithankarprasanna@gmail.com>

## [](#SEE_ALSO)SEE ALSO

           ipcrm(1), ipcs(1), lsipc(1), sysvipc(7)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The ipcmk command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                       IPCMK(1)

------------------------------------------------------------------------

Pages that refer to this page: [ipcrm(1)](../man1/ipcrm.1.html),  [ipcs(1)](../man1/ipcs.1.html),  [lsipc(1)](../man1/lsipc.1.html),  [pcp-ipcs(1)](../man1/pcp-ipcs.1.html),  [sysvipc(7)](../man7/sysvipc.7.html)

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
