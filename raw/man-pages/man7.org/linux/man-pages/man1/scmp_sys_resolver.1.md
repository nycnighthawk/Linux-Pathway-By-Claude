---
{"title": "scmp_sys_resolver(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/scmp_sys_resolver.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# scmp_sys_resolver(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    scmp_sys_resolver(1)     libseccomp Documentation    scmp_sys_resolver(1)

## [](#NAME)NAME

           scmp_sys_resolver - Resolve system calls

## [](#SYNOPSIS)SYNOPSIS

           scmp_sys_resolver [-h] [-a ARCH ] [-t] SYSCALL_NAME |
           SYSCALL_NUMBER

## [](#DESCRIPTION)DESCRIPTION

           This command resolves both system call names and numbers with
           respect to the given architecture supplied in the optional ARCH
           argument.  If the architecture is not supplied on the command line
           then the native architecture is used.  If the "-t" argument is
           specified along with a system call name, then the system call will
           be translated as necessary for the given architecture.  The "-t"
           argument has no effect if a system call number is specified.

           In some combinations of architecture and system call, a negative
           system call number will be displayed.  A negative system call
           number indicates that the system call is not defined for the given
           architecture and is treated in a special manner by libseccomp
           depending on the operation.

           -a ARCH
                  The architecture to use for resolving the system call.
                  Valid ARCH values are "x86", "x86_64", "x32", "arm",
                  "aarch64", "loongarch64", "m68k", "mips", "mipsel",
                  "mips64", "mipsel64", "mips64n32", "mipsel64n32", "parisc",
                  "parisc64", "ppc", "ppc64", "ppc64le", "s390", "s390x",
                  "sheb" and "sh".

           -t     If necessary, translate the system call name to the proper
                  system call number, even if the system call name is
                  different, e.g. socket(2) on x86.

           -h     A simple one-line usage display.

## [](#EXIT_STATUS)EXIT STATUS

           Returns zero on success, errno values on failure.

## [](#NOTES)NOTES

           The libseccomp project site, with more information and the source
           code repository, can be found at
           https://github.com/seccomp/libseccomp.  This tool, as well as the
           libseccomp library, is currently under development, please report
           any bugs at the project site or directly to the author.

## [](#AUTHOR)AUTHOR

           Paul Moore <paul@paul-moore.com>

## [](#COLOPHON)COLOPHON

           This page is part of the libseccomp (high-level API to the Linux
           Kernel's seccomp filter) project.  Information about the project
           can be found at ⟨https://github.com/seccomp/libseccomp⟩.  If you
           have a bug report for this manual page, see
           ⟨https://groups.google.com/d/forum/libseccomp⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/seccomp/libseccomp⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    paul@paul-moore.com            23 May 2013           scmp_sys_resolver(1)

------------------------------------------------------------------------

Pages that refer to this page: [seccomp(2)](../man2/seccomp.2.html)

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
