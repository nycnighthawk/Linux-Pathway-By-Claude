---
{"title": "chcat(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/chcat.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chcat(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [FILES](#FILES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHCAT(8)                      User Commands                      CHCAT(8)

## [](#NAME)NAME

           chcat - change SELinux security categories of files/users

## [](#SYNOPSIS)SYNOPSIS

           chcat category file...
           chcat -l category user...
           chcat [[+|-]category...]  file...
           chcat -l [[+|-]category...]  user...
           chcat [-d] file...
           chcat -l [-d] user...
           chcat -L [ -l ] [ user ... ]

## [](#DESCRIPTION)DESCRIPTION

           Use +/- to add/remove categories from a file or user (only a
           single category can be specified at a time). Or specify the
           desired list/range of categories to be applied (replacing the
           existing categories).

           Note: When removing a category you must specify '--' on the
           command line before using the -Category syntax. This tells the
           command that you have finished entering options and are now
           specifying a category name instead.

           -d     delete all categories from given FILE/USER.

           -L     list available categories.

           -l     Tells chcat to operate on users instead of files.

## [](#EXAMPLE)EXAMPLE

           Replace categories of user "test" with c0.c6
           # chcat -l c0.c6 test
           Add category c1023 to user "test"
           # chcat -l +c1023 test
           Remove category c5 from file "file"
           # chcat -- -c5 file
           Remove all categories from file "file"
           # chcat -d file

## [](#SEE_ALSO)SEE ALSO

           chcon(1),
                  selinux(8), semanage(8)

           When operating on files this script wraps the chcon command.

## [](#FILES)FILES

           /etc/selinux/{SELINUXTYPE}/setrans.conf
           /etc/selinux/{SELINUXTYPE}/seusers

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    chcat                         September 2005                     CHCAT(8)

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
