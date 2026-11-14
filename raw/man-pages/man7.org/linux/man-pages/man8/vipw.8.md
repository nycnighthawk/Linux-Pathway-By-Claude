---
{"title": "vipw(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/vipw.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# vipw(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    VIPW(8)                 System Management Commands                VIPW(8)

## [](#NAME)NAME

           vipw, vigr - edit the password, group, shadow-password or
           shadow-group file

## [](#SYNOPSIS)SYNOPSIS

           vipw [options]

           vigr [options]

## [](#DESCRIPTION)DESCRIPTION

           The vipw and vigr commands edit the files /etc/passwd and
           /etc/group, respectively. With the -s flag, they will edit the
           shadow versions of those files, /etc/shadow and /etc/gshadow,
           respectively. The programs will set the appropriate locks to
           prevent file corruption. When looking for an editor, the programs
           will first try the environment variable $VISUAL, then the
           environment variable $EDITOR, and finally the default editor,
           vi(1).

## [](#OPTIONS)OPTIONS

           The options which apply to the vipw and vigr commands are:

           -g, --group
               Edit group database.

           -h, --help
               Display help message and exit.

           -p, --passwd
               Edit passwd database.

           -q, --quiet
               Quiet mode.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

           -s, --shadow
               Edit shadow or gshadow database.

## [](#ENVIRONMENT)ENVIRONMENT

           VISUAL
               Editor to be used.

           EDITOR
               Editor to be used if VISUAL is not set.

## [](#FILES)FILES

           /etc/group
               Group account information.

           /etc/gshadow
               Secure group account information.

           /etc/passwd
               User account information.

           /etc/shadow
               Secure user account information.

## [](#SEE_ALSO)SEE ALSO

           vi(1), group(5), gshadow(5) , passwd(5), , shadow(5).

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

    shadow-utils 4.19.0             08/04/2026                        VIPW(8)

------------------------------------------------------------------------

Pages that refer to this page: [group(5)](../man5/group.5.html),  [passwd(5)](../man5/passwd.5.html)

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
