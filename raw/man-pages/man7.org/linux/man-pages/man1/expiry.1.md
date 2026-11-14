---
{"title": "expiry(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/expiry.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# expiry(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    EXPIRY(1)                     User Commands                     EXPIRY(1)

## [](#NAME)NAME

           expiry - check and enforce password expiration policy

## [](#SYNOPSIS)SYNOPSIS

           expiry option

## [](#DESCRIPTION)DESCRIPTION

           The expiry command checks (-c) the current password expiration and
           forces (-f) changes when required. It is callable as a normal user
           command.

## [](#OPTIONS)OPTIONS

           The options which apply to the expiry command are:

           -c, --check
               Check the password expiration of the current user.

           -f, --force
               Force a password change if the current user has an expired
               password.

           -h, --help
               Display help message and exit.

## [](#FILES)FILES

           /etc/passwd
               User account information.

           /etc/shadow
               Secure user account information.

## [](#SEE_ALSO)SEE ALSO

           passwd(5), shadow(5).

## [](#COLOPHON)COLOPHON

           This page is part of the shadow-utils (utilities for managing
           accounts and shadow password files) project.  Information about
           the project can be found at 
           ⟨https://github.com/shadow-maint/shadow⟩.  If you have a bug report
           for this manual page, send it to
           pkg-shadow-devel@alioth-lists.debian.net.  This page was obtained
           from the tarball shadow-4.19.0.tar fetched from
           ⟨https://github.com/shadow-maint/shadow/releases⟩ on 2026-08-04.
           If you discover any rendering problems in this HTML version of the
           page, or you believe there is a better or more up-to-date source
           for the page, or you have corrections or improvements to the
           information in this COLOPHON (which is not part of the original
           manual page), send a mail to man-pages@man7.org

    shadow-utils 4.19.0             08/04/2026                      EXPIRY(1)

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
