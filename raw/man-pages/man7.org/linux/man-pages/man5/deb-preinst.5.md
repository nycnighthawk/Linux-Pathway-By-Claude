---
{"title": "deb-preinst(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-preinst.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-preinst(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-preinst(5)                  dpkg suite                 deb-preinst(5)

## [](#NAME)NAME

           deb-preinst - package pre-installation maintainer script

## [](#SYNOPSIS)SYNOPSIS

           DEBIAN/preinst

## [](#DESCRIPTION)DESCRIPTION

           A package can perform several pre-installation actions via
           maintainer scripts, by including an executable preinst file in its
           control archive (i.e. DEBIAN/preinst during package creation).

           The script can be called in the following ways:

           new-preinst install
               Before the package is installed.

           new-preinst install old-version new-version
               Before a removed package is upgraded.

               Support for new-version since dpkg 1.18.5.

           new-preinst upgrade old-version new-version
               Before the package is upgraded.

               Support for new-version since dpkg 1.18.5.

           old-preinst abort-upgrade new-version
               If postrm fails during upgrade or fails on failed upgrade.

## [](#SEE_ALSO)SEE ALSO

           dpkg(1).

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

    1.23.7-216-gff7e9               2026-03-07                 deb-preinst(5)

------------------------------------------------------------------------

Pages that refer to this page: [deb(5)](../man5/deb.5.html)

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
