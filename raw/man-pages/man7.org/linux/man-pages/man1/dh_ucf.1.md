---
{"title": "dh_ucf(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_ucf.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_ucf(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_UCF(1)                       Debhelper                       DH_UCF(1)

## [](#NAME)NAME

           dh_ucf - register configuration files with ucf

## [](#SYNOPSIS)SYNOPSIS

           dh_ucf [debhelper options] [-A] [-n] [file ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_ucf is a debhelper program that is responsible for generating
           the postinst and postrm commands that register files with ucf(1)
           and ucfr(1).

## [](#FILES)FILES

           debian/package.ucf
               List pairs of source and destination files to register with
               ucf. Each pair should be put on its own line, with the source
               and destination separated by whitespace. Both source and
               destination must be absolute paths. The source should be a
               file that is provided by your package, typically in
               /usr/share/, while the destination is typically a file in
               /etc/.

               A dependency on ucf will be generated in ${misc:Depends}.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

## [](#OPTIONS)OPTIONS

           -A, --all
               Install all files specified by command line parameters in ALL
               packages acted on.

           -n, --no-scripts
               Do not modify postinst/postrm scripts. Turns this command into
               a no-op.

           file ...
               Install these info files into the first package acted on. (Or
               in all packages if -A is specified).

## [](#NOTES)NOTES

           Note that this command is not idempotent. dh_prep(1) should be
           called between invocations of this command. Otherwise, it may
           cause multiple instances of the same text to be added to
           maintainer scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Joey Hess <joeyh@debian.org> Jeroen Schot <schot@a-eskwadraat.nl>

## [](#COLOPHON)COLOPHON

           This page is part of the debhelper (helper programs for
           debian/rules) project.  Information about the project can be found
           at [unknown -- if you know, please contact man-pages@man7.org] If
           you have a bug report for this manual page, send it to
           submit@bugs.debian.org.  This page was obtained from the project's
           upstream Git repository
           ⟨https://salsa.debian.org/debian/debhelper.git⟩ on 2026-08-03.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    13.23                           2025-01-02                      DH_UCF(1)

------------------------------------------------------------------------

Pages that refer to this page: [debhelper(7)](../man7/debhelper.7.html)

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
