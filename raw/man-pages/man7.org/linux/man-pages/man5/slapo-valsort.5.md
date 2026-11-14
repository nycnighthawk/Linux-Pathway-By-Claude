---
{"title": "slapo-valsort(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-valsort.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-valsort(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-VALSORT(5)           File Formats Manual           SLAPO-VALSORT(5)

## [](#NAME)NAME

           slapo-valsort - Value Sorting overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The Value Sorting overlay can be used with a backend database to
           sort the values of specific multi-valued attributes within a
           subtree. The sorting occurs whenever the attributes are returned
           in a search response.

           Sorting can be specified in ascending or descending order, using
           either numeric or alphanumeric sort methods. Additionally, a
           "weighted" sort can be specified, which uses a numeric weight
           prepended to the attribute values.  The weighted sort is always
           performed in ascending order, but may be combined with the other
           methods for values that all have equal weights. The weight is
           specified by prepending an integer weight {<weight>} in front of
           each value of the attribute for which weighted sorting is desired.
           This weighting factor is stripped off and not returned in search
           results unless the valsort control is specified
           (1.3.6.1.4.1.4203.666.5.14).

           The valsort control requires a value consisting of a Sequence that
           contains a boolean flag. The weighting factor is only returned if
           the boolean value is TRUE. In lber-encode(3) format, the required
           value must conform to "{b}" syntax.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the Value Sorting overlay.  They
           should appear after the overlay directive.

           valsort-attr <attribute> <baseDN> (<sort-method> | weighted
           [<sort-method>])
                  Configure a sorting method for the specified attribute in
                  the subtree rooted at baseDN.  The sort-method may be one
                  of alpha-ascend, alpha-descend, numeric-ascend, or
                  numeric-descend.  If the special weighted method is
                  specified, a secondary sort-method may also be specified.
                  It is an error to specify an alphanumeric sort-method for
                  an attribute with Integer or NumericString syntax, and it
                  is an error to specify a numeric sort-method for an
                  attribute with a syntax other than Integer or
                  NumericString.

## [](#EXAMPLES)EXAMPLES

                database mdb
                suffix dc=example,dc=com
                ...
                overlay valsort
                valsort-attr member ou=groups,dc=example,dc=com alpha-ascend

           To invoke ldapsearch(1) with the valsort control, the control
           value must be set appropriately.  The following octets represent
           the desired "{b}" encoding:

                0x30 0x03 0x01 0x01 0xff

           The control can be sent from the command-line using the base64
           encoding of the value:

                ldapsearch -E 1.3.6.1.4.1.4203.666.5.14=::MAMBAf8=

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5).

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           This module was written in 2005 by Howard Chu of Symas
           Corporation. The work was sponsored by Stanford University.

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

    OpenLDAP LDVERSION             RELEASEDATE               SLAPO-VALSORT(5)

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
