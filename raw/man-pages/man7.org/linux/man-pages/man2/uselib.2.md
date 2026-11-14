---
{"title": "uselib(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/uselib.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uselib(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    uselib(2)                  System Calls Manual                  uselib(2)

## [](#NAME)NAME

           uselib - load shared library

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           [[deprecated]] int uselib(const char *library);

## [](#DESCRIPTION)DESCRIPTION

           The system call uselib() serves to load a shared library to be
           used by the calling process.  It is given a pathname.  The address
           where to load is found in the library itself.  The library can
           have any recognized binary format.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           In addition to all of the error codes returned by open(2) and
           mmap(2), the following may also be returned:

           EACCES The library specified by library does not have read or
                  execute permission, or the caller does not have search
                  permission for one of the directories in the path prefix.
                  (See also path_resolution(7).)

           ENFILE The system-wide limit on the total number of open files has
                  been reached.

           ENOEXEC
                  The file specified by library is not an executable of a
                  known type; for example, it does not have the correct magic
                  numbers.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           This obsolete system call is not supported by glibc.  No
           declaration is provided in glibc headers, but, through a quirk of
           history, glibc before glibc 2.23 did export an ABI for this system
           call.  Therefore, in order to employ this system call, it was
           sufficient to manually declare the interface in your code;
           alternatively, you could invoke the system call using syscall(2).

           In ancient libc versions (before glibc 2.0), uselib() was used to
           load the shared libraries with names found in an array of names in
           the binary.

           Since Linux 3.15, this system call is available only when the
           kernel is configured with the CONFIG_USELIB option.

## [](#SEE_ALSO)SEE ALSO

           ar(1), gcc(1), ld(1), ldd(1), mmap(2), open(2), dlopen(3),
           capabilities(7), ld.so(8)

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

    Linux man-pages 6.19            2026-02-08                      uselib(2)

------------------------------------------------------------------------

Pages that refer to this page: [fanotify_mark(2)](../man2/fanotify_mark.2.html),  [syscalls(2)](../man2/syscalls.2.html)

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
