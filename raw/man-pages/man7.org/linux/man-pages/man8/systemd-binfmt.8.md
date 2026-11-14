---
{"title": "systemd-binfmt.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-binfmt.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-binfmt.service(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-BINFMT.SERVICE(8) systemd-binfmt.serviceSYSTEMD-BINFMT.SERVICE(8)

## [](#NAME)NAME

           systemd-binfmt.service, systemd-binfmt - Configure additional
           binary formats for executables at boot

## [](#SYNOPSIS)SYNOPSIS

           systemd-binfmt.service

           /usr/lib/systemd/systemd-binfmt

## [](#DESCRIPTION)DESCRIPTION

           systemd-binfmt.service is an early boot service that registers
           additional binary formats for executables in the kernel.

           See binfmt.d(5) for information about the configuration of this
           service.

## [](#OPTIONS)OPTIONS

           --unregister
               If passed, instead of registering configured binary formats in
               the kernel, the reverse operation is executed: all currently
               registered binary formats are unregistered from the kernel.

               Added in version 246.

           --cat-config
               Copy the contents of config files to standard output. Before
               each file, the filename is printed as a comment.

           --tldr
               Copy the contents of config files to standard output. Only the
               "interesting" parts of the configuration files are printed,
               comments and empty lines are skipped. Before each file, the
               filename is printed as a comment.

           --no-pager
               Do not pipe output into a pager.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), binfmt.d(5), wine(8)

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

    systemd 262~devel                               SYSTEMD-BINFMT.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [binfmt.d(5)](../man5/binfmt.d.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
