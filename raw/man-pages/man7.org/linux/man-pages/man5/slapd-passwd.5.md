---
{"title": "slapd-passwd(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd-passwd.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd-passwd(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD-PASSWD(5)            File Formats Manual            SLAPD-PASSWD(5)

## [](#NAME)NAME

           slapd-passwd - /etc/passwd backend to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The PASSWD backend to slapd(8) serves up the user account
           information listed in the system passwd(5) file.  This backend is
           provided for demonstration purposes only.  The DN of each entry is
           "uid=<username>,<suffix>".  Note that non-base searches scan the
           entire passwd file, and are best suited for hosts with small
           passwd files.

## [](#CONFIGURATION)CONFIGURATION

           This slapd.conf option applies to the PASSWD backend database.
           That is, it must follow a "database passwd" line and come before
           any subsequent "backend" or "database" lines.  Other database
           options are described in the slapd.conf(5) manual page.

           file <filename>
                  Specifies an alternate passwd file to use.  The default is
                  /etc/passwd.

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The passwd backend does not honor any of the access control
           semantics described in slapd.access(5).  Only read (=r) access to
           the entry pseudo-attribute and to the other attribute values of
           the entries returned by the search operation is honored, which is
           performed by the frontend.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

           /etc/passwd
                  user account information

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd(8), passwd(5).

## [](#COLOPHON)COLOPHON

           This page is part of the OpenLDAP (an open source implementation
           of the Lightweight Directory Access Protocol) project.
           Information about the project can be found at 
           ⟨http://www.openldap.org/⟩.  If you have a bug report for this
           manual page, see ⟨http://www.openldap.org/its/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.openldap.org/openldap/openldap.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    OpenLDAP LDVERSION             RELEASEDATE                SLAPD-PASSWD(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.backends(5)](../man5/slapd.backends.5.html)

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
