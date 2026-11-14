---
{"title": "deb-conffiles(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-conffiles.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-conffiles(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-conffiles(5)                dpkg suite               deb-conffiles(5)

## [](#NAME)NAME

           deb-conffiles - package conffiles

## [](#SYNOPSIS)SYNOPSIS

           DEBIAN/conffiles

## [](#DESCRIPTION)DESCRIPTION

           A package declares its list of conffiles by including a conffiles
           file in its control archive (i.e. DEBIAN/conffiles during package
           creation).

           This file contains a list of files, one per line, with an optional
           leading flag separated by whitespace.  The conffiles must be
           listed as absolute pathnames.  Trailing whitespace will be
           trimmed, but empty or whitespace-only lines are not accepted.

           Files without a flag should exist in the binary package, otherwise
           dpkg(1) will ignore them.

           There is currently only one flag supported, remove-on-upgrade, to
           mark that a conffile needs to be removed on the next upgrade
           (since dpkg 1.20.6).  These files must not exist in the binary
           package, as both dpkg(1) and dpkg-deb(1) will not accept building
           nor processing such binary packages.

## [](#EXAMPLE)EXAMPLE

            /usr/local/etc/alternatives/README
            /usr/local/etc/cron.daily/dpkg
            /usr/local/etc/dpkg/dpkg.cfg
            /usr/local/etc/logrotate.d/dpkg
            remove-on-upgrade /etc/some-old-file.conf

## [](#SEE_ALSO)SEE ALSO

           dpkg-deb(1), dpkg(1).

## [](#COLOPHON)COLOPHON

           This page is part of the dpkg (Debian Package Manager) project.
           Information about the project can be found at 
           ⟨https://wiki.debian.org/Teams/Dpkg/⟩.  If you have a bug report
           for this manual page, see
           ⟨http://bugs.debian.org/cgi-bin/pkgreport.cgi?src=dpkg⟩.  This
           page was obtained from the project's upstream Git repository ⟨git
           clone https://git.dpkg.org/git/dpkg/dpkg.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    1.22.0-52-g1af0                 2023-08-30               deb-conffiles(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-maintscript-helper(1)](../man1/dpkg-maintscript-helper.1.html),  [deb(5)](../man5/deb.5.html)

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
