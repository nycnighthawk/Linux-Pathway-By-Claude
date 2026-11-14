---
{"title": "oomctl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/oomctl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# oomctl(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    OOMCTL(1)                         oomctl                        OOMCTL(1)

## [](#NAME)NAME

           oomctl - Analyze the state stored in systemd-oomd

## [](#SYNOPSIS)SYNOPSIS

           oomctl [OPTIONS...] {COMMAND}

## [](#DESCRIPTION)DESCRIPTION

           oomctl may be used to get information about the various contexts
           read in by the systemd(1) userspace out-of-memory (OOM) killer,
           systemd-oomd(8).

## [](#COMMANDS)COMMANDS

           The following commands are understood:

           dump
               Show the current state of the cgroups and system contexts
               stored by systemd-oomd.

               Added in version 247.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

           --no-pager
               Do not pipe output into a pager.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-oomd.service(8), oomd.conf(5)

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

    systemd 262~devel                                               OOMCTL(1)

------------------------------------------------------------------------

Pages that refer to this page: [oomd.conf(5)](../man5/oomd.conf.5.html),  [org.freedesktop.oom1(5)](../man5/org.freedesktop.oom1.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-oomd.service(8)](../man8/systemd-oomd.service.8.html)

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
