---
{"title": "yum-ovl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/yum-ovl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-ovl(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [OPTIONS](#OPTIONS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [AUTHOR](#AUTHOR) \| [LICENSE](#LICENSE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yum-ovl(1)                     User Manual                     yum-ovl(1)

## [](#NAME)NAME

           yum-ovl - Performs an initial copy-up of yum(8) package database.

## [](#OPTIONS)OPTIONS

           -d debug-level If debug level is 2 and more, print out the number
           of files copied up from the lower layer

## [](#DESCRIPTION)DESCRIPTION

           Opening a file on OverlayFS in read-only mode causes the file from
           lower layer to be opened, then later on, if the same file is
           opened
           in write mode, a copy-up into the upper    layer    takes
           place,
           resulting into a new file being opened.
           Since yum(8) needs to open the RPMdb first read-only, and then
           also with write access, we need to copy-up the files beforehand to
           make sure that the access is consistent.

## [](#FILES)FILES

           /usr/lib/yum-plugins/ovl.py Plugin itself

           /etc/yum/pluginconf.d/ovl.conf Configuration file allowing to
           enable/disable the plugin

## [](#AUTHOR)AUTHOR

           Pavel Odvody podvody@redhat.com

## [](#LICENSE)LICENSE

           2015, Red Hat, Licensed under GPLv2+

## [](#SEE_ALSO)SEE ALSO

           yum(1) yum(8) rpmdb(8)

## [](#COLOPHON)COLOPHON

           This page is part of the yum-utils (Yum Package Manager utilities)
           project.  Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/yum⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/yum-utils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2020-03-11.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Red Hat                       September 2015                   yum-ovl(1)

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
