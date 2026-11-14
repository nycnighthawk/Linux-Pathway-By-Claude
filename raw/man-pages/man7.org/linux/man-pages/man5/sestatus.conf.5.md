---
{"title": "sestatus.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/sestatus.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sestatus.conf(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sestatus.conf(5)       sestatus configuration file       sestatus.conf(5)

## [](#NAME)NAME

           sestatus.conf - The sestatus(8) configuration file.

## [](#DESCRIPTION)DESCRIPTION

           The sestatus.conf file is used by the sestatus(8) command with the
           -v option to determine what file and process security contexts
           should be displayed.

           The fully qualified path name of the configuration file is:
                  /etc/sestatus.conf or <vendordir>/sestatus.conf if it is
                  not available

           The file consists of two optional sections as described in the
           FILE FORMAT section. Whether these exist or not, the following
           will always be displayed:
                  The current process context
                  The init process context
                  The controlling terminal file context

## [](#FILE_FORMAT)FILE FORMAT

           The format consists of two optional sections as follows:
                  [files]
                  file_name
                  [file_name]
                  ...

                  [process]
                  executable_file_name
                  [executable_file_name]
                  ...

           Where:
                  [files]
                         The start of the file list block.
                  file_name
                         One or more fully qualified file names, each on a
                         new line will that will have its context displayed.
                         If the file does not exist, then it is ignored. If
                         the file is a symbolic link, then sestatus -v will
                         also display the target file context.

                  [process]
                         The start of the process list block.
                  executable_file_name
                         One or more fully qualified executable file names
                         that should it be an active process, have its
                         context displayed. Each entry is on a new line.

## [](#EXAMPLE)EXAMPLE

           # /etc/sestatus.conf
           [files]
           /etc/passwd
           /etc/shadow
           /bin/bash
           /bin/login
           /lib/libc.so.6
           /lib/ld-linux.so.2
           /lib/ld.so.1

           [process]
           /sbin/mingetty
           /sbin/agetty
           /usr/sbin/sshd

## [](#SEE_ALSO)SEE ALSO

           selinux(8), sestatus(8)

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Security Enhanced Linux        26-Nov-2011               sestatus.conf(5)

------------------------------------------------------------------------

Pages that refer to this page: [sestatus(8)](../man8/sestatus.8.html)

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
