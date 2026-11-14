---
{"title": "slapd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/slapd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD(8C)                                                       SLAPD(8C)

## [](#NAME)NAME

           slapd - Stand-alone LDAP Daemon

## [](#SYNOPSIS)SYNOPSIS

           LIBEXECDIR/slapd [-V[V[V]] [-4|-6] [-T {acl|a[dd]|auth|c[at]|
           d[n]|i[ndex]|m[odify]|p[asswd]|s[chema]|t[est]}] [-d debug-level]
           [-f slapd-config-file] [-F slapd-config-directory] [-h URLs]
           [-n service-name] [-s syslog-level] [-l syslog-local-user]
           [-o option[=value]] [-r directory] [-u user] [-g group]
           [-c cookie]

## [](#DESCRIPTION)DESCRIPTION

           Slapd is the stand-alone LDAP daemon. It listens for LDAP
           connections on any number of ports (default 389), responding to
           the LDAP operations it receives over these connections.  slapd is
           typically invoked at boot time, usually out of /etc/rc.local.
           Upon startup, slapd normally forks and disassociates itself from
           the invoking tty.  If configured in the config file (or config
           directory), the slapd process will print its process ID (see
           getpid(2)) to a .pid file, as well as the command line options
           during invocation to an .args file (see slapd.conf(5)).  If the -d
           flag is given, even with a zero argument, slapd will not fork and
           disassociate from the invoking tty.

           See the "OpenLDAP Administrator's Guide" for more details on
           slapd.

## [](#OPTIONS)OPTIONS

           -V[V[V]]
                  Print version info and proceed with startup.  If -VV is
                  given, exit after providing version info. If -VVV is given,
                  additionally provide information on static overlays and
                  backends.

           -4     Listen on IPv4 addresses only.

           -6     Listen on IPv6 addresses only.

           -T tool
                  Run in Tool mode. The tool argument selects whether to run
                  as slapadd, slapcat, slapdn, slapindex, slapmodify,
                  slappasswd, slapschema, or slaptest (slapacl and slapauth
                  need the entire acl and auth option value to be spelled
                  out, as a is reserved to slapadd).  This option should be
                  the first option specified when it is used; any remaining
                  options will be interpreted by the corresponding slap tool
                  program, according to the respective man pages.  Note that
                  these tool programs will usually be symbolic links to
                  slapd.  This option is provided for situations where
                  symbolic links are not provided or not usable.

           -d debug-level
                  Turn on debugging as defined by debug-level.  If this
                  option is specified, even with a zero argument, slapd will
                  not fork or disassociate from the invoking terminal.  Some
                  general operation and status messages are printed for any
                  value of debug-level.  debug-level is taken as a bit
                  string, with each bit corresponding to a different kind of
                  debugging information.  See <ldap_log.h> for details.
                  Comma-separated arrays of friendly names can be specified
                  to select debugging output of the corresponding debugging
                  information.  All the names recognized by the loglevel
                  directive described in slapd.conf(5) are supported.  If
                  debug-level is ?, a list of installed debug-levels is
                  printed, and slapd exits.

                  Remember that if you turn on packet logging, packets
                  containing bind passwords will be output, so if you
                  redirect the log to a logfile, that file should be read-
                  protected.

           -s syslog-level
                  This option tells slapd at what debug-level debugging
                  statements should be logged to the syslog(8) facility.  The
                  value syslog-level can be set to any value or combination
                  allowed by the -d switch.  Slapd logs all messages selected
                  by syslog-level at the syslog(3) severity debug-level
                  DEBUG, on the unit specified with -l.

           -n service-name
                  Specifies the service name for logging and other purposes.
                  Defaults to basename of argv[0], i.e.: "slapd".

           -l syslog-local-user
                  Selects the local user of the syslog(8) facility. Value can
                  be LOCAL0, through LOCAL7, as well as USER and DAEMON.  The
                  default is LOCAL4.  However, this option is only permitted
                  on systems that support local users with the syslog(8)
                  facility.  Logging to syslog(8) occurs at the "DEBUG"
                  severity debug-level.

           -f slapd-config-file
                  Specifies the slapd configuration file. The default is
                  ETCDIR/slapd.conf.

           -F slapd-config-directory
                  Specifies the slapd configuration directory. The default is
                  ETCDIR/slapd.d.  If both -f and -F are specified, the
                  config file will be read and converted to config directory
                  format and written to the specified directory.  If neither
                  option is specified, slapd will attempt to read the default
                  config directory before trying to use the default config
                  file. If a valid config directory exists then the default
                  config file is ignored. All of the slap tools that use the
                  config options observe this same behavior.

           -h URLlist
                  slapd will by default serve ldap:/// (LDAP over TCP on all
                  interfaces on default LDAP port).  That is, it will bind
                  using INADDR_ANY and port 389.  The -h option may be used
                  to specify LDAP (and other scheme) URLs to serve.  For
                  example, if slapd is given -h "ldap://127.0.0.1:9009/
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

                  For LDAP over IPC, name is the name of the socket, and no
                  port is required, nor allowed; note that directory
                  separators must be URL-encoded, like any other characters
                  that are special to URLs; so the socket

                          /usr/local/var/ldapi

                  must be specified as

                          ldapi://%2Fusr%2Flocal%2Fvar%2Fldapi

                  The default location for the IPC socket is
                  LOCALSTATEDIR/run/ldapi

                  The listener permissions are indicated by
                  "x-mod=-rwxrwxrwx", "x-mod=0777" or "x-mod=777", where any
                  of the "rwx" can be "-" to suppress the related permission,
                  while any of the "7" can be any legal octal digit,
                  according to chmod(1).  The listeners can take advantage of
                  the "x-mod" extension to apply rough limitations to
                  operations, e.g. allow read operations ("r", which applies
                  to search and compare), write operations ("w", which
                  applies to add, delete, modify and modrdn), and execute
                  operations ("x", which means bind is required).  "User"
                  permissions apply to authenticated users, while "other"
                  apply to anonymous users; "group" permissions are ignored.
                  For example, "ldap:///????x-mod=-rw-------" means that read
                  and write is only allowed for authenticated connections,
                  and bind is required for all operations.  This feature is
                  experimental, and requires to be manually enabled at
                  configure time.

           -r directory
                  Specifies a directory to become the root directory.  slapd
                  will change the current working directory to this directory
                  and then chroot(2) to this directory.  This is done after
                  opening listeners but before reading any configuration file
                  or initializing any backend.  When used as a security
                  mechanism, it should be used in conjunction with -u and -g
                  options.

           -u user
                  slapd will run slapd with the specified user name or id,
                  and that user's supplementary group access list as set with
                  initgroups(3).  The group ID is also changed to this user's
                  gid, unless the -g option is used to override.  Note when
                  used with -r, slapd will use the user database in the
                  change root environment.

                  Note that on some systems, running as a non-privileged user
                  will prevent passwd back-ends from accessing the encrypted
                  passwords.  Note also that any shell back-ends will run as
                  the specified non-privileged user.

           -g group
                  slapd will run with the specified group name or id.  Note
                  when used with -r, slapd will use the group database in the
                  change root environment.

           -c cookie
                  This option provides a cookie for the syncrepl replication
                  consumer.  The cookie is a comma separated list of
                  name=value pairs.  Currently supported syncrepl cookie
                  fields are rid, sid, and csn.  rid identifies a replication
                  thread within the consumer server and is used to find the
                  syncrepl specification in slapd.conf(5) or slapd-config(5)
                  having the matching replication identifier in its
                  definition. The rid must be provided in order for any other
                  specified values to be used.  sid is the server id in a
                  multi-provider configuration.  csn is the commit sequence
                  number received by a previous synchronization and
                  represents the state of the consumer content which the
                  syncrepl engine will synchronize to the current provider
                  content.  In case of multi-provider replication agreement,
                  multiple csn values, semicolon separated, can appear.  Use
                  only the rid part to force a full reload.

           -o option[=value]
                  This option provides a generic means to specify options
                  without the need to reserve a separate letter for them.

                  It supports the following options:

                  slp={on|off|slp-attrs}
                         When SLP support is compiled into slapd, disable it
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

## [](#EXAMPLES)EXAMPLES

           To start slapd and have it fork and detach from the terminal and
           start serving the LDAP databases defined in the default config
           file, just type:

                LIBEXECDIR/slapd

           To start slapd with an alternate configuration file, and turn on
           voluminous debugging which will be printed on standard error,
           type:

                LIBEXECDIR/slapd -f /var/tmp/slapd.conf -d 255

           To test whether the configuration file is correct or not, type:

                LIBEXECDIR/slapd -Tt

## [](#SEE_ALSO)SEE ALSO

           ldap(3), slapd.conf(5), slapd-config(5), slapd.access(5),
           slapacl(8), slapadd(8), slapauth(8), slapcat(8), slapdn(8),
           slapindex(8), slapmodify(8), slappasswd(8), slapschema(8),
           slaptest(8).

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

    OpenLDAP LDVERSION             RELEASEDATE                      SLAPD(8C)

------------------------------------------------------------------------

Pages that refer to this page: [ldap(3)](../man3/ldap.3.html),  [ldap_sync(3)](../man3/ldap_sync.3.html),  [lloadd.conf(5)](../man5/lloadd.conf.5.html),  [slapd.access(5)](../man5/slapd.access.5.html),  [slapd-asyncmeta(5)](../man5/slapd-asyncmeta.5.html),  [slapd.backends(5)](../man5/slapd.backends.5.html),  [slapd.conf(5)](../man5/slapd.conf.5.html),  [slapd-config(5)](../man5/slapd-config.5.html),  [slapd-dnssrv(5)](../man5/slapd-dnssrv.5.html),  [slapd-ldap(5)](../man5/slapd-ldap.5.html),  [slapd-ldif(5)](../man5/slapd-ldif.5.html),  [slapd-mdb(5)](../man5/slapd-mdb.5.html),  [slapd-meta(5)](../man5/slapd-meta.5.html),  [slapd-monitor(5)](../man5/slapd-monitor.5.html),  [slapd-null(5)](../man5/slapd-null.5.html),  [slapd.overlays(5)](../man5/slapd.overlays.5.html),  [slapd-passwd(5)](../man5/slapd-passwd.5.html),  [slapd.plugin(5)](../man5/slapd.plugin.5.html),  [slapd-relay(5)](../man5/slapd-relay.5.html),  [slapd-sock(5)](../man5/slapd-sock.5.html),  [slapd-sql(5)](../man5/slapd-sql.5.html),  [slapd-wt(5)](../man5/slapd-wt.5.html),  [slapo-chain(5)](../man5/slapo-chain.5.html),  [slapo-dds(5)](../man5/slapo-dds.5.html),  [slapo-dynlist(5)](../man5/slapo-dynlist.5.html),  [slapo-homedir(5)](../man5/slapo-homedir.5.html),  [slapo-memberof(5)](../man5/slapo-memberof.5.html),  [slapo-nestgroup(5)](../man5/slapo-nestgroup.5.html),  [slapo-pbind(5)](../man5/slapo-pbind.5.html),  [slapo-pcache(5)](../man5/slapo-pcache.5.html),  [slapo-remoteauth(5)](../man5/slapo-remoteauth.5.html),  [slapo-retcode(5)](../man5/slapo-retcode.5.html),  [slapo-rwm(5)](../man5/slapo-rwm.5.html),  [slappw-argon2(5)](../man5/slappw-argon2.5.html),  [automount(8)](../man8/automount.8.html),  [lloadd(8)](../man8/lloadd.8.html),  [slapacl(8)](../man8/slapacl.8.html),  [slapadd(8)](../man8/slapadd.8.html),  [slapauth(8)](../man8/slapauth.8.html),  [slapcat(8)](../man8/slapcat.8.html),  [slapdn(8)](../man8/slapdn.8.html),  [slapindex(8)](../man8/slapindex.8.html),  [slapmodify(8)](../man8/slapmodify.8.html),  [slappasswd(8)](../man8/slappasswd.8.html),  [slapschema(8)](../man8/slapschema.8.html),  [slaptest(8)](../man8/slaptest.8.html)

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
