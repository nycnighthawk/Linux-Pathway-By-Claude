---
{"title": "_syscall(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/_syscall.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# \_syscall(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    _syscall(2)                System Calls Manual                _syscall(2)

## [](#NAME)NAME

           _syscall - invoking a system call without library support
           (OBSOLETE)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/unistd.h>

           A _syscall macro

           desired system call

## [](#DESCRIPTION)DESCRIPTION

           The important thing to know about a system call is its prototype.
           You need to know how many arguments, their types, and the function
           return type.  There are seven macros that make the actual call
           into the system easier.  They have the form:

               _syscallX(type,name,type1,arg1,type2,arg2,...)

           where

                  X is 0–6, which are the number of arguments taken by the
                  system call

                  type is the return type of the system call

                  name is the name of the system call

                  typeN is the Nth argument's type

                  argN is the name of the Nth argument

           These macros create a function called name with the arguments you
           specify.  Once you include the _syscall() in your source file, you
           call the system call by name.

## [](#FILES)FILES

           /usr/include/linux/unistd.h

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Starting around Linux 2.6.18, the _syscall macros were removed
           from header files supplied to user space.  Use syscall(2) instead.
           (Some architectures, notably ia64, never provided the _syscall
           macros; on those architectures, syscall(2) was always required.)

## [](#NOTES)NOTES

           The _syscall() macros do not produce a prototype.  You may have to
           create one, especially for C++ users.

           System calls are not required to return only positive or negative
           error codes.  You need to read the source to be sure how it will
           return errors.  Usually, it is the negative of a standard error
           code, for example, -EPERM.  The _syscall() macros will return the
           result r of the system call when r is nonnegative, but will return
           -1 and set the variable errno to -r when r is negative.  For the
           error codes, see errno(3).

           When defining a system call, the argument types must be passed by-
           value or by-pointer (for aggregates like structs).

## [](#EXAMPLES)EXAMPLES

           #include <stdio.h>
           #include <stdlib.h>
           #include <errno.h>
           #include <linux/unistd.h>       /* for _syscallX macros/related stuff */
           #include <linux/kernel.h>       /* for struct sysinfo */

           _syscall1(int, sysinfo, struct sysinfo *, info);

           int
           main(void)
           {
               struct sysinfo s_info;
               int error;

               error = sysinfo(&s_info);
               printf("code error = %d\n", error);
               printf("Uptime = %lds\nLoad: 1 min %lu / 5 min %lu / 15 min %lu\n"
                      "RAM: total %lu / free %lu / shared %lu\n"
                      "Memory in buffers = %lu\nSwap: total %lu / free %lu\n"
                      "Number of processes = %d\n",
                      s_info.uptime, s_info.loads[0],
                      s_info.loads[1], s_info.loads[2],
                      s_info.totalram, s_info.freeram,
                      s_info.sharedram, s_info.bufferram,
                      s_info.totalswap, s_info.freeswap,
                      s_info.procs);
               exit(EXIT_SUCCESS);
           }

       Sample output
           code error = 0
           uptime = 502034s
           Load: 1 min 13376 / 5 min 5504 / 15 min 1152
           RAM: total 15343616 / free 827392 / shared 8237056
           Memory in buffers = 5066752
           Swap: total 27881472 / free 24698880
           Number of processes = 40

## [](#SEE_ALSO)SEE ALSO

           intro(2), syscall(2), errno(3)

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

    Linux man-pages 6.19            2025-05-17                    _syscall(2)

------------------------------------------------------------------------

Pages that refer to this page: [intro(2)](../man2/intro.2.html),  [syscall(2)](../man2/syscall.2.html)

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
