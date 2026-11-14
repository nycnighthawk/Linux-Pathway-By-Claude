---
{"title": "dh_installinitramfs(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installinitramfs.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installinitramfs(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLINITRAMFS(1)          Debhelper          DH_INSTALLINITRAMFS(1)

## [](#NAME)NAME

           dh_installinitramfs - install initramfs hooks and setup
           maintscripts

## [](#SYNOPSIS)SYNOPSIS

           dh_installinitramfs [debhelper options] [-n]

## [](#DESCRIPTION)DESCRIPTION

           dh_installinitramfs is a debhelper program that is responsible for
           installing Debian package provided initramfs hooks.

           If dh_installinitramfs installs or detects one or more initramfs
           hooks in the package, then it also automatically generates the
           noawait trigger update-initframfs command needed to interface with
           the Debian initramfs system.  This trigger is inserted into the
           packaging by dh_installdeb(1).

## [](#FILES)FILES

           debian/package.initramfs-hook
               Assumed to be an initramfs hook that will be installed into
               usr/share/initramfs-tools/hooks/package in the package build
               directory. See HOOK SCRIPTS in initramfs-tools(8) for more
               information about initramfs hooks.

## [](#OPTIONS)OPTIONS

           -n, --no-scripts
               Do not add the update-initramfs trigger even if it seems like
               the package might need it.  The option is called --no-scripts
               for historical reasons as dh_installinitramfs would previously
               generate maintainer scripts that called update-initramfs -u.

               Use this option, if you need to interface with the
               update-initramfs system that is not satisfied by the noawait
               trigger (e.g. because you need the extra guarantees and
               head-aches of a await trigger).

## [](#NOTES)NOTES

           Note that this command is not idempotent. dh_prep(1) should be
           called between invocations of this command. Otherwise, it may
           cause multiple instances of the same text to be added to triggers
           file.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7) update-initramfs(8) initramfs-tools(8)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Niels Thykier <niels@thykier.net>

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

    13.23                           2025-01-02         DH_INSTALLINITRAMFS(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh(1)](../man1/dh.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
