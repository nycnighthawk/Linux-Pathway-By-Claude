---
{"title": "ovn-detrace(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ovn-detrace.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ovn-detrace(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ovn-detrace(1)                  OVN Manual                 ovn-detrace(1)

## [](#NAME)NAME

           ovn-detrace - convert ``ovs-appctl ofproto/trace'' output to
           combine OVN logical flow information.

## [](#SYNOPSIS)SYNOPSIS

           ovn-detrace < file

           Common options:
                  [-h | --help] [-V | --version]

## [](#DESCRIPTION)DESCRIPTION

           The ovn-detrace program reads ovs-appctl ofproto/trace output on
           stdin, looking for flow cookies, and displays for each cookie the
           OVN south-bound records that contributed to its creation. It
           further displays the related north-bound information when
           applicable, e.g., the ACL that generated the logical flow that
           gets translated to an OpenFlow rule with a given cookie.

## [](#OPTIONS)OPTIONS

           -h
           --help Prints a brief help message to the console.

           -V
           --version
                  Prints version information to the console.

           --ovnsb=server
                  The OVN Southbound DB remote to contact.  If the OVN_SB_DB
                  environment variable is set, its value is used as the
                  default.  Otherwise, the default is
                  unix:@RUNDIR@/ovnsb_db.sock, but this default is unlikely
                  to be useful outside of single-machine OVN test
                  environments.

           --ovnnb=server
                  The OVN Northbound DB remote to contact.  If the OVN_NB_DB
                  environment variable is set, its value is used as the
                  default.  Otherwise, the default is
                  unix:@RUNDIR@/ovnnb_db.sock, but this default is unlikely
                  to be useful outside of single-machine OVN test
                  environments.

           --ovs= Also decode flow information (like OVS ofport) from the
                  flows by connecting to the OVS DB.

           --no-leader-only
                  Connect to any cluster member, not just the leader. The
                  option works for OVN Southbound DB and OVN Northbound DB.

           --ovsdb=server
                  The OVS DB remote to contact if --ovs is present.  If the
                  OVS_RUNDIR environment variable is set, its value is used
                  as the default. Otherwise, the default is
                  unix:@RUNDIR@/db.sock, but this default is unlikely to be
                  useful outside of single-machine OVN test environments.

           -p privkey.pem
           --private-key=privkey.pem
                  Specifies a PEM file containing the private key used as
                  ovn-detrace's identity for outgoing SSL/TLS connections.

           -c cert.pem
           --certificate=cert.pem
                  Specifies a PEM file containing a certificate that
                  certifies the private key specified on -p or --private-key
                  to be trustworthy.  The certificate must be signed by the
                  certificate authority (CA) that the peer in SSL/TLS
                  connections will use to verify it.

           -C cacert.pem
           --ca-cert=cacert.pem
                  Specifies a PEM file containing the CA certificate that
                  ovn-detrace should use to verify certificates presented to
                  it by SSL/TLS peers.  (This may be the same certificate
                  that SSL/TLS peers use to verify the certificate specified
                  on -c or --certificate, or it may be a different one,
                  depending on the PKI design in use.)

## [](#SEE_ALSO)SEE ALSO

           ovs-appctl(8),ovn-sbctl(8),ovn-nbctl(8),ovn-trace(8)

## [](#COLOPHON)COLOPHON

           This page is part of the Open Virtual Network (Daemons for Open
           vSwitch that translate virtual network configurations into
           OpenFlow) project.  Information about the project can be found at
           ⟨https://www.ovn.org/⟩.  If you have a bug report for this manual
           page, send it to bugs@openvswitch.org.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/ovn-org/ovn⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-31.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    OVN                              24.09.90                  ovn-detrace(1)

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
