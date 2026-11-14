---
{"title": "systemd-ssh-issue(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-ssh-issue.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-ssh-issue(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-SSH-ISSUE(1)        systemd-ssh-issue        SYSTEMD-SSH-ISSUE(1)

## [](#NAME)NAME

           systemd-ssh-issue - Generator for SSH login prompt drop-ins

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/systemd-ssh-issue [OPTIONS...] make-vsock

           /usr/lib/systemd/systemd-ssh-issue [OPTIONS...] rm-vsock

## [](#DESCRIPTION)DESCRIPTION

           systemd-ssh-issue is a small tool that generates (when called with
           make-vsock) and removes (when called with rm-vsock) a
           /run/issue.d/50-ssh-vsock.issue drop-in file in case AF_VSOCK
           support is available in the kernel and the VM environment. The
           file contains brief information about how to contact the local
           system via SSH-over-AF_VSOCK, in particular it reports the
           system's AF_VSOCK CID. The file is typically read and displayed by
           agetty(8) on console or serial login prompts.

           This tool is automatically used by systemd-ssh-generator(8) in the
           AF_VSOCK socket units it generates.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --issue-path=
               Changes the path to the issue file to write to/remove. If not
               specified, defaults to /run/issue.d/50-ssh-vsock.issue. If
               specified as empty string or "-" writes the issue file
               contents to standard output.

               Added in version 258.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-ssh-generator(8), vsock(7), ssh(1), sshd(8),
           agetty(8)

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                    SYSTEMD-SSH-ISSUE(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
