---
{"title": "pldd(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pldd.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pldd(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    pldd(1)                  General Commands Manual                  pldd(1)

## [](#NAME)NAME

           pldd - display dynamic shared objects linked into a process

## [](#SYNOPSIS)SYNOPSIS

           pldd pid

           pldd option

## [](#DESCRIPTION)DESCRIPTION

           The pldd command displays a list of the dynamic shared objects
           (DSOs) that are linked into the process with the specified process
           ID (PID).  The list includes the libraries that have been
           dynamically loaded using dlopen(3).

## [](#OPTIONS)OPTIONS

           --help
           -?     Display a help message and exit.

           --usage
                  Display a short usage message and exit.

           --version
           -V     Display program version information and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success, pldd exits with the status 0.  If the specified
           process does not exist, the user does not have permission to
           access its dynamic shared object list, or no command-line
           arguments are supplied, pldd exists with a status of 1.  If given
           an invalid option, it exits with the status 64.

## [](#VERSIONS)VERSIONS

           Some other systems have a similar command.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           glibc 2.15.

## [](#NOTES)NOTES

           The command

               lsof -p PID

           also shows output that includes the dynamic shared objects that
           are linked into a process.

           The gdb(1) info shared command also shows the shared libraries
           being used by a process, so that one can obtain similar output to
           pldd using a command such as the following (to monitor the process
           with the specified pid):

               $ gdb -ex "set confirm off" \
                     -ex "set height 0" \
                     -ex "info shared" \
                     -ex "quit" \
                     -p $pid \
               | grep '^0x.*0x';

## [](#BUGS)BUGS

           From glibc 2.19 to glibc 2.29, pldd was broken: it just hung when
           executed.  This problem was fixed in glibc 2.30, and the fix has
           been backported to earlier glibc versions in some distributions.

## [](#EXAMPLES)EXAMPLES

           $ echo $$;               # Display PID of shell
           1143
           $ pldd $$;               # Display DSOs linked into the shell
           1143:   /usr/bin/bash
           linux-vdso.so.1
           /lib64/libtinfo.so.5
           /lib64/libdl.so.2
           /lib64/libc.so.6
           /lib64/ld-linux-x86-64.so.2
           /lib64/libnss_files.so.2

## [](#SEE_ALSO)SEE ALSO

           ldd(1), lsof(1), dlopen(3), ld.so(8)

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

    Linux man-pages 6.19            2026-02-08                        pldd(1)

------------------------------------------------------------------------

Pages that refer to this page: [ldd(1)](../man1/ldd.1.html),  [dlopen(3)](../man3/dlopen.3.html),  [ld.so(8)](../man8/ld.so.8.html)

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
