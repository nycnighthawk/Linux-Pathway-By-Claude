---
{"title": "pppd-radattr(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pppd-radattr.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pppd-radattr(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [USAGE](#USAGE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PPPD-RADATTR(8)          System Manager's Manual          PPPD-RADATTR(8)

## [](#NAME)NAME

           radattr.so - RADIUS utility plugin for pppd(8)

## [](#SYNOPSIS)SYNOPSIS

           pppd [ options ] plugin radius.so plugin radattr.so

## [](#DESCRIPTION)DESCRIPTION

           The radattr plugin for pppd causes all radius attributes returned
           by the RADIUS server at authentication time to be stored in the
           file /var/run/radattr.pppN where pppN is the name of the PPP
           interface.  The RADIUS attributes are stored one per line in the
           format "Attribute-Name Attribute-Value".  This format is
           convenient for use in /etc/ppp/ip-up and /etc/ppp/ip-down scripts.

           Note that you must load the radius.so plugin before loading the
           radattr.so plugin; radattr.so depends on symbols defined in
           radius.so.

## [](#USAGE)USAGE

           To use the plugin, simply supply the plugin radius.so plugin
           radattr.so options to pppd.

## [](#SEE_ALSO)SEE ALSO

           pppd(8) pppd-radius(8)

## [](#AUTHOR)AUTHOR

           Dianne Skoll <dianne@skoll.ca>

## [](#COLOPHON)COLOPHON

           This page is part of the ppp (An implementation of the Point-to-
           Point Protocol (PPP)) project.  Information about the project can
           be found at ⟨https://ppp.samba.org/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://github.com/paulusmack/ppp/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/paulusmack/ppp⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-25.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                              PPPD-RADATTR(8)

------------------------------------------------------------------------

Pages that refer to this page: [pppd-radius(8)](../man8/pppd-radius.8.html)

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
