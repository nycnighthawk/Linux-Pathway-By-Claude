---
{"title": "pppd-radius(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pppd-radius.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pppd-radius(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [USAGE](#USAGE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PPPD-RADIUS(8)           System Manager's Manual           PPPD-RADIUS(8)

## [](#NAME)NAME

           radius.so - RADIUS authentication plugin for pppd(8)

## [](#SYNOPSIS)SYNOPSIS

           pppd [ options ] plugin radius.so

## [](#DESCRIPTION)DESCRIPTION

           The RADIUS plugin for pppd permits pppd to perform PAP, CHAP, MS-
           CHAP and MS-CHAPv2 authentication against a RADIUS server instead
           of the usual /etc/ppp/pap-secrets and /etc/ppp/chap-secrets files.

           The RADIUS plugin is built on a library called radiusclient which
           has its own configuration files (usually in /etc/radiusclient),
           consult those files for more information on configuring the RADIUS
           plugin

## [](#OPTIONS)OPTIONS

           The RADIUS plugin introduces one additional pppd option:

           radius-config-file filename
                  The file filename is taken as the radiusclient
                  configuration file.  If this option is not used, then the
                  plugin uses /etc/radiusclient/radiusclient.conf as the
                  configuration file.

           avpair attribute=value
                  Adds an Attribute-Value pair to be passed on to the RADIUS
                  server on each request.

           map-to-ifname
                  Sets Radius NAS-Port attribute to number equal to interface
                  name (Default)

           map-to-ttyname
                  Sets Radius NAS-Port attribute value via libradiusclient
                  library

## [](#USAGE)USAGE

           To use the plugin, simply supply the plugin radius.so option to
           pppd, and edit /etc/radiusclient/radiusclient.conf appropriately.
           If you use the RADIUS plugin, the normal pppd authentication
           schemes (login, checking the /etc/ppp/*-secrets files) are
           skipped.  The RADIUS server should assign an IP address to the
           peer using the RADIUS Framed-IP-Address attribute.

## [](#SEE_ALSO)SEE ALSO

           pppd(8) pppd-radattr(8)

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

                                                               PPPD-RADIUS(8)

------------------------------------------------------------------------

Pages that refer to this page: [pppd-radattr(8)](../man8/pppd-radattr.8.html)

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
