---
{"title": "dselect.cfg(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/dselect.cfg.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dselect.cfg(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dselect.cfg(5)                  dpkg suite                 dselect.cfg(5)

## [](#NAME)NAME

           dselect.cfg - dselect configuration file

## [](#DESCRIPTION)DESCRIPTION

           This file contains default options for dselect.  Each line
           contains a single option which is exactly the same as a normal
           command line option for dselect except for the leading hyphens
           which are not used here.  Quotes surrounding option values are
           stripped.  Comments are allowed by starting a line with a hash
           sign (‘#’).

## [](#FILES)FILES

           /usr/local/etc/dpkg/dselect.cfg.d/[0-9a-zA-Z_-]*

           /usr/local/etc/dpkg/dselect.cfg

           ~/.dselect.cfg

## [](#SEE_ALSO)SEE ALSO

           dselect(1).

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

    1.22.6-77-g86fe7                2024-03-10                 dselect.cfg(5)

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
