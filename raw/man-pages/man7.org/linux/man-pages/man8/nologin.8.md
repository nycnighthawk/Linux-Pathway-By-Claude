---
{"title": "nologin(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/nologin.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nologin(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [HISTORY](#HISTORY) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NOLOGIN(8)                System Administration                NOLOGIN(8)

## [](#NAME)NAME

           nologin - politely refuse a login

## [](#SYNOPSIS)SYNOPSIS

           nologin [-V] [-h]

## [](#DESCRIPTION)DESCRIPTION

           nologin displays a message that an account is not available and
           exits non-zero. It is intended as a replacement shell field to
           deny login access to an account.

           If the file /etc/nologin.txt exists, nologin displays its contents
           to the user instead of the default message.

           The exit status returned by nologin is always 1.

## [](#OPTIONS)OPTIONS

           -c, --command command

           --init-file

           -i --interactive

           --init-file file

           -i, --interactive

           -l, --login

           --noprofile

           --norc

           --posix

           --rcfile file

           -r, --restricted

           These shell command-line options are ignored to avoid nologin
           error.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#NOTES)NOTES

           nologin is a per-account way to disable login (usually used for
           system accounts like http or ftp). nologin uses /etc/nologin.txt
           as an optional source for a non-default message, the login access
           is always refused independently of the file.

           pam_nologin(8) PAM module usually prevents all unprivileged users
           from logging into the system. pam_nologin(8) functionality is
           controlled by /var/run/nologin or the /etc/nologin file.

## [](#HISTORY)HISTORY

           The nologin command appeared in 4.4BSD.

## [](#AUTHORS)AUTHORS

           Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           login(1), passwd(5), pam_nologin(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The nologin command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     NOLOGIN(8)

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
