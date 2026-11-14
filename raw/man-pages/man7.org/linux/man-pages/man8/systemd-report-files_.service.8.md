---
{"title": "systemd-report-files@.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-report-files@.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-report-files@.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD...SERVICE(8)  systemd-report-files@.service  SYSTEMD...SERVICE(8)

## [](#NAME)NAME

           systemd-report-files@.service, systemd-report-files.socket,
           systemd-report-files - Report the contents of files as system
           report metrics

## [](#SYNOPSIS)SYNOPSIS

           systemd-report-files@.service

           systemd-report-files.socket

           /usr/lib/systemd/systemd-report-files

## [](#DESCRIPTION)DESCRIPTION

           systemd-report-files@.service is a metrics source for
           systemd-report(1). It reports the contents of a configurable set
           of files as metrics, by implementing the io.systemd.Metrics
           Varlink interface on a socket linked into the /run/systemd/report/
           directory.

           The files to report are picked up from report.files/
           subdirectories of the usual configuration directories, i.e. from
           /etc/systemd/report.files/, /run/systemd/report.files/,
           /var/lib/systemd/report.files/,
           /usr/local/lib/systemd/report.files/ and
           /usr/lib/systemd/report.files/. Typically these directories
           contain symlinks pointing to the actual files in the file system
           whose contents shall be reported. Entries with the same name in an
           earlier directory override those in a later one.

           Each entry is reported as a metric named "io.systemd.Files.NAME",
           where NAME is the name of the entry (which must be a valid metric
           field name). The metric value is the verbatim contents of the
           file. Files that cannot be read (for example because a symlink is
           dangling) are skipped, as are files whose contents are not valid
           UTF-8 text.

           Note that access to this service is unprivileged, but it runs
           privileged. This means take care when symlinking files into the
           various report.files/ directories: this service might provide read
           access even if the client does not have the required direct access
           rights itself.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-report(1)

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

    systemd 262~devel                                    SYSTEMD...SERVICE(8)

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
