---
{"title": "lloadd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lloadd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lloadd(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [RELATION TO SLAPD(8)](#RELATION_TO_SLAPD(8)) \| [CN=MONITOR INTERFACE](#CN=MONITOR_INTERFACE) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LLOADD(8C)                                                     LLOADD(8C)

## [](#NAME)NAME

           lloadd - LDAP Load Balancer Daemon

## [](#SYNOPSIS)SYNOPSIS

           LIBEXECDIR/lloadd [-4|-6] [-d debug-level] [-f lloadd-config-file]
           [-h URLs] [-n service-name] [-s syslog-level] [-l syslog-local-
           user] [-o option[=value]] [-r directory] [-u user] [-g group]

## [](#DESCRIPTION)DESCRIPTION

           Lloadd is the stand-alone LDAP daemon. It listens for LDAP
           connections on any number of ports (default 389), forwarding the
           LDAP operations it receives over these connections to be handled
           by the configured backends.  lloadd is typically invoked at boot
           time, usually out of /etc/rc.local.  Upon startup, lloadd normally
           forks and disassociates itself from the invoking tty.  If
           configured in the config file, the lloadd process will print its
           process ID (see getpid(2)) to a .pid file, as well as the command
           line options during invocation to an .args file (see
           lloadd.conf(5)).  If the -d flag is given, even with a zero
           argument, lloadd will not fork and disassociate from the invoking
           tty.

           See the "OpenLDAP Administrator's Guide" for more details on
           lloadd.

## [](#OPTIONS)OPTIONS

           -4     Listen on IPv4 addresses only.

           -6     Listen on IPv6 addresses only.

           -d debug-level
                  Turn on debugging as defined by debug-level.  If this
                  option is specified, even with a zero argument, lloadd will
                  not fork or disassociate from the invoking terminal.  Some
                  general operation and status messages are printed for any
                  value of debug-level.  debug-level is taken as a bit
                  string, with each bit corresponding to a different kind of
                  debugging information.  See <ldap_log.h> for details.
                  Comma-separated arrays of friendly names can be specified
                  to select debugging output of the corresponding debugging
                  information.  All the names recognized by the loglevel
                  directive described in lloadd.conf(5) are supported.  If
                  debug-level is ?, a list of installed debug-levels is
                  printed, and lloadd exits.

                  Remember that if you turn on packet logging, packets
                  containing bind passwords will be output, so if you
                  redirect the log to a logfile, that file should be read-
                  protected.

           -s syslog-level
                  This option tells lloadd at what debug-level debugging
                  statements should be logged to the syslog(8) facility.  The
                  value syslog-level can be set to any value or combination
                  allowed by the -d switch.  Lloadd logs all messages
                  selected by syslog-level at the syslog(3) severity debug-
                  level DEBUG, on the unit specified with -l.

           -n service-name
                  Specifies the service name for logging and other purposes.
                  Defaults to basename of argv[0], i.e.: "lloadd".

           -l syslog-local-user
                  Selects the local user of the syslog(8) facility. Value can
                  be LOCAL0, through LOCAL7, as well as USER and DAEMON.  The
                  default is LOCAL4.  However, this option is only permitted
                  on systems that support local users with the syslog(8)
                  facility.  Logging to syslog(8) occurs at the "DEBUG"
                  severity debug-level.

           -f lloadd-config-file
                  Specifies the lloadd configuration file. The default is
                  ETCDIR/lloadd.conf.

           -h URLlist
                  lloadd will by default serve ldap:/// (LDAP over TCP on all
                  interfaces on default LDAP port).  That is, it will bind
                  using INADDR_ANY and port 389.  The -h option may be used
                  to specify LDAP (and other scheme) URLs to serve.  For
                  example, if lloadd is given -h "ldap://127.0.0.1:9009/
                  ldaps:/// ldapi:///", it will listen on 127.0.0.1:9009 for
                  LDAP, 0.0.0.0:636 for LDAP over TLS, and LDAP over IPC
                  (Unix domain sockets).  Host 0.0.0.0 represents INADDR_ANY
                  (any interface).  A space separated list of URLs is
                  expected.  The URLs should be of the LDAP, PLDAP, LDAPS,
                  PLDAPS, or LDAPI schemes, and generally without a DN or
                  other optional parameters (excepting as discussed below).
                  Support for the latter three schemes depends on selected
                  configuration options. Hosts may be specified by name or
                  IPv4 and IPv6 address formats.  Ports, if specified, must
                  be numeric.  The default ldap:// port is 389 and the
                  default ldaps:// port is 636, same for the proxy enabled
                  variants.

                  The PLDAP and PLDAPS URL schemes provide support for the
                  HAProxy proxy protocol version 2, which allows a load
                  balancer or proxy server to provide the remote client IP
                  address to slapd to be used for access control or logging.
                  Ports configured for PLDAP or PLDAPS will only accept
                  connections that include the necessary proxy protocol
                  header. Connections to these ports should be restricted at
                  the network level to only trusted load balancers or proxies
                  to avoid spoofing of client IP addresses by third parties.

                  At the moment, the load balancer does not act on the
                  recorded address in any way.

                  For LDAP over IPC, name is the name of the socket, and no
                  port is required, nor allowed; note that directory
                  separators must be URL-encoded, like any other characters
                  that are special to URLs; so the socket

                          /usr/local/var/ldapi

                  must be specified as

                          ldapi://%2Fusr%2Flocal%2Fvar%2Fldapi

                  The default location for the IPC socket is
                  LOCALSTATEDIR/run/ldapi

           -r directory
                  Specifies a directory to become the root directory.  lloadd
                  will change the current working directory to this directory
                  and then chroot(2) to this directory.  This is done after
                  opening listeners but before reading any configuration file
                  or initializing any backend.  When used as a security
                  mechanism, it should be used in conjunction with -u and -g
                  options.

           -u user
                  lloadd will run lloadd with the specified user name or id,
                  and that user's supplementary group access list as set with
                  initgroups(3).  The group ID is also changed to this user's
                  gid, unless the -g option is used to override.  Note when
                  used with -r, lloadd will use the user database in the
                  change root environment.

           -g group
                  lloadd will run with the specified group name or id.  Note
                  when used with -r, lloadd will use the group database in
                  the change root environment.

           -o option[=value]
                  This option provides a generic means to specify options
                  without the need to reserve a separate letter for them.

                  It supports the following options:

                  slp={on|off|slp-attrs}
                         When SLP support is compiled into lloadd, disable it
                         (off),
                          enable it by registering at SLP DAs without
                         specific SLP attributes (on), or with specific SLP
                         attributes slp-attrs that must be an SLP attribute
                         list definition according to the SLP standard.

                         For example, "slp=(tree=production),(server-
                         type=OpenLDAP),(server-version=2.4.15)" registers at
                         SLP DAs with the three SLP attributes tree, server-
                         type and server-version that have the values given
                         above.  This allows one to specifically query the
                         SLP DAs for LDAP servers holding the production tree
                         in case multiple trees are available.

## [](#RELATION_TO_SLAPD(8))RELATION TO SLAPD(8)

           Lloadd can be compiled as a slapd loadable module. In that case,
           it can be loaded as such:

               moduleload path/to/lloadd.la
               backend lload
               listen "listening URLs"

           This enables lloadd to provide additional features through the
           host slapd process like access to run-time statistics in
           cn=monitor and dynamic configuration from cn=config.

           The listening sockets specified will be under direct control of
           lloadd and need to be different from the sockets slapd is
           configured to listen on.  Clients connecting to these are
           completely separate from regular LDAP clients connecting to the
           usual slapd sockets - lloadd clients have no access to slapd
           databases, similarly, slapd client traffic does not propagate to
           the lloadd backend servers in any way.

## [](#CN=MONITOR_INTERFACE)CN=MONITOR INTERFACE

           As part of lloadd's cn=monitor interface it is possible to close a
           client connection it manages by writing to the corresponding
           entry, replacing the olmConnectionState attribute with the value
           closing.  This is subject to ACLs configured on the monitor
           database. The server will send a Notice of Disconnection to the
           client, refuse any new operations and once all pending operations
           have finished, close the connection.

           For example, to close connection number 42:

               dn: cn=connection 42,cn=incoming connections,cn=load balancer,cn=backends,cn=monitor
               changetype: modify
               replace: olmConnectionState
               olmConnectionState: closing

## [](#EXAMPLES)EXAMPLES

           To start lloadd and have it fork and detach from the terminal and
           start load-balancing the LDAP servers defined in the default
           config file, just type:

                LIBEXECDIR/lloadd

           To start lloadd with an alternate configuration file, and turn on
           voluminous debugging which will be printed on standard error,
           type:

                LIBEXECDIR/lloadd -f /var/tmp/lloadd.conf -d 255

           To start lloadd as a module inside a slapd process listening on
           ldap://:1389 and ldaps://, put the following in your slapd.conf
           (or its equivalent in cn=config):

               moduleload lloadd.la
               backend lload
               listen "ldap://:1389 ldaps://"

## [](#SEE_ALSO)SEE ALSO

           ldap(3), lloadd.conf(5), slapd-config(5), slapd-monitor(5),
           slapd(8).

           "OpenLDAP Administrator's Guide"
           (http://www.OpenLDAP.org/doc/admin/)

## [](#BUGS)BUGS

           See http://www.openldap.org/its/

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           OpenLDAP Software is developed and maintained by The OpenLDAP
           Project <http://www.openldap.org/>.  OpenLDAP Software is derived
           from the University of Michigan LDAP 3.3 Release.

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

    OpenLDAP LDVERSION             RELEASEDATE                     LLOADD(8C)

------------------------------------------------------------------------

Pages that refer to this page: [lloadd.conf(5)](../man5/lloadd.conf.5.html)

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
