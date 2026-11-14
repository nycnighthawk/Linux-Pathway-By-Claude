---
{"title": "slapo-dyngroup(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-dyngroup.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-dyngroup(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [BACKWARD COMPATIBILITY](#BACKWARD_COMPATIBILITY) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-DYNGROUP(5)          File Formats Manual          SLAPO-DYNGROUP(5)

## [](#NAME)NAME

           slapo-dyngroup - Dynamic Group overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The Dynamic Group overlay allows clients to use LDAP Compare
           operations to test the membership of a dynamic group the same way
           they would check against a static group. Compare operations
           targeting a group's static member attribute will be intercepted
           and tested against the configured dynamic group's URL attribute.

           Note that this intercept only happens if the actual Compare
           operation does not return a LDAP_COMPARE_TRUE result. So if a
           group has both static and dynamic members, the static member list
           will be checked first.

## [](#CONFIGURATION)CONFIGURATION

           This slapd.conf option applies to the Dynamic Group overlay.  It
           should appear after the overlay directive.

           attrpair <memberAttr> <URLattr>
                  Specify the attributes to be compared. A compare operation
                  on the memberAttr will cause the URLattr to be evaluated
                  for the result.

## [](#EXAMPLES)EXAMPLES

             database mdb
             ...
             overlay dyngroup
             attrpair member memberURL

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#BACKWARD_COMPATIBILITY)BACKWARD COMPATIBILITY

           The dyngroup overlay has been reworked with the 2.5 release to use
           a consistent namespace as with other overlays. As a side-effect
           the following cn=config parameters are deprecated and will be
           removed in a future release: olcDGAttrPair is replaced with
           olcDynGroupAttrPair olcDGConfig is replaced with olcDynGroupConfig

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5).

## [](#AUTHOR)AUTHOR

           Howard Chu

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

    OpenLDAP LDVERSION             RELEASEDATE              SLAPO-DYNGROUP(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.overlays(5)](../man5/slapd.overlays.5.html)

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
