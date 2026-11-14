---
{"title": "ovn-controller-vtep(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ovn-controller-vtep.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ovn-controller-vtep(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ovn-controller-vtep(8)          OVN Manual         ovn-controller-vtep(8)

## [](#NAME)NAME

           ovn-controller-vtep - Open Virtual Network local controller for
           vtep enabled physical switches.

## [](#SYNOPSIS)SYNOPSIS

           ovn-controller-vtep [options] [--vtep-db=vtep-database] [--ovnsb-
           db=ovnsb-database]

## [](#DESCRIPTION)DESCRIPTION

           ovn-controller-vtep is the local controller daemon in OVN, the
           Open Virtual Network, for VTEP enabled physical switches. It
           connects up to the OVN Southbound database (see ovn-sb(5)) over
           the OVSDB protocol, and down to the VTEP database (see vtep(5))
           over the OVSDB protocol.

       PKI Options
           PKI configuration is required in order to use SSL/TLS for the
           connections to the VTEP and Southbound databases.

                  -p privkey.pem
                  --private-key=privkey.pem
                       Specifies a PEM file containing the private key used
                       as identity for outgoing SSL connections.

                  -c cert.pem
                  --certificate=cert.pem
                       Specifies a PEM file containing a certificate that
                       certifies the private key specified on -p or
                       --private-key to be trustworthy. The certificate must
                       be signed by the certificate authority (CA) that the
                       peer in SSL connections will use to verify it.

                  -C cacert.pem
                  --ca-cert=cacert.pem
                       Specifies a PEM file containing the CA certificate for
                       verifying certificates presented to this program by
                       SSL peers. (This may be the same certificate that SSL
                       peers use to verify the certificate specified on -c or
                       --certificate, or it may be a different one, depending
                       on the PKI design in use.)

                  -C none
                  --ca-cert=none
                       Disables verification of certificates presented by SSL
                       peers. This introduces a security risk, because it
                       means that certificates cannot be verified to be those
                       of known trusted hosts.

                  --bootstrap-ca-cert=cacert.pem
                         When cacert.pem exists, this option has the same
                         effect as -C or --ca-cert. If it does not exist,
                         then the executable will attempt to obtain the CA
                         certificate from the SSL peer on its first SSL
                         connection and save it to the named PEM file. If it
                         is successful, it will immediately drop the
                         connection and reconnect, and from then on all SSL
                         connections must be authenticated by a certificate
                         signed by the CA certificate thus obtained.

                         This option exposes the SSL connection to a man-in-
                         the-middle attack obtaining the initial CA
                         certificate, but it may be useful for bootstrapping.

                         This option is only useful if the SSL peer sends its
                         CA certificate as part of the SSL certificate chain.
                         The SSL protocol does not require the server to send
                         the CA certificate.

                         This option is mutually exclusive with -C and
                         --ca-cert.

                  --peer-ca-cert=peer-cacert.pem
                         Specifies a PEM file that contains one or more
                         additional certificates to send to SSL peers. peer-
                         cacert.pem should be the CA certificate used to sign
                         the program’s own certificate, that is, the
                         certificate specified on -c or --certificate. If the
                         program’s certificate is self-signed, then
                         --certificate and --peer-ca-cert should specify the
                         same file.

                         This option is not useful in normal operation,
                         because the SSL peer must already have the CA
                         certificate for the peer to have any confidence in
                         the program’s identity. However, this offers a way
                         for a new installation to bootstrap the CA
                         certificate on its first SSL connection.

       Other Options
           --unixctl=socket
                  Sets the name of the control socket on which program
                  listens for runtime management commands (see RUNTIME
                  MANAGEMENT COMMANDS, below). If socket does not begin with
                  /, it is interpreted as relative to . If --unixctl is not
                  used at all, the default socket is /program.pid.ctl, where
                  pid is program’s process ID.

                  On Windows a local named pipe is used to listen for runtime
                  management commands. A file is created in the absolute path
                  as pointed by socket or if --unixctl is not used at all, a
                  file is created as program in the configured OVS_RUNDIR
                  directory. The file exists just to mimic the behavior of a
                  Unix domain socket.

                  Specifying none for socket disables the control socket
                  feature.

           -h
           --help
                Prints a brief help message to the console.

           -V
           --version
                Prints version information to the console.

## [](#CONFIGURATION)CONFIGURATION

           ovn-controller-vtep retrieves its configuration information from
           both the ovnsb and the vtep database. If the database locations
           are not given from command line, the default is the db.sock in
           local OVSDB’s ’run’ directory. The database location must take one
           of the following forms:

                  •      ssl:host:port

                         The specified SSL/TLS port on the give host, which
                         can either be a DNS name (if built with unbound
                         library) or an IP address (IPv4 or IPv6). If host is
                         an IPv6 address, then wrap host with square
                         brackets, e.g.: ssl:[::1]:6640. The --private-key,
                         --certificate and either of --ca-cert or
                         --bootstrap-ca-cert options are mandatory when this
                         form is used.

                  •      tcp:host:port

                         Connect to the given TCP port on host, where host
                         can be a DNS name (if built with unbound library) or
                         IP address (IPv4 or IPv6). If host is an IPv6
                         address, then wrap host with square brackets, e.g.:
                         tcp:[::1]:6640.

                  •      unix:file

                         On POSIX, connect to the Unix domain server socket
                         named file.

                         On Windows, connect to a localhost TCP port whose
                         value is written in file.

           ovn-controller-vtep assumes it gets configuration information from
           the following keys in the Global table of the connected
           hardware_vtep database:

                  other_config:ovn-match-northd-version
                         The boolean flag indicates if ovn-controller-vtep
                         needs to check ovn-northd version. If this flag is
                         set to true and the ovn-northd’s version (reported
                         in the Southbound database) doesn’t match with the
                         ovn-controller-vtep’s internal version, then it will
                         stop processing the southbound and connected
                         hardware_vtep database changes. The default value is
                         considered false if this option is not defined.

                  other_config:ovn-remote-probe-interval
                         The inactivity probe interval of the connection to
                         the OVN Southbound database, in milliseconds. If the
                         value is zero, it disables the connection keepalive
                         feature.

                         If the value is nonzero, then it will be forced to a
                         value of at least 1000 ms.

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

    OVN 24.09.90               ovn-controller-vtep     ovn-controller-vtep(8)

------------------------------------------------------------------------

Pages that refer to this page: [ovn-sb(5)](../man5/ovn-sb.5.html)

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
