---
{"title": "lloadd.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/lloadd.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lloadd.conf(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SLAPD INTEGRATION](#SLAPD_INTEGRATION) \| [GLOBAL CONFIGURATION OPTIONS](#GLOBAL_CONFIGURATION_OPTIONS) \| [TLS OPTIONS](#TLS_OPTIONS) \| [BACKEND CONFIGURATION](#BACKEND_CONFIGURATION) \| [TIER OPTIONS](#TIER_OPTIONS) \| [BACKEND OPTIONS](#BACKEND_OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [LIMITATIONS](#LIMITATIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LLOADD.CONF(5)             File Formats Manual             LLOADD.CONF(5)

## [](#NAME)NAME

           lloadd.conf - configuration file for lloadd, the stand-alone LDAP
           daemon

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/lloadd.conf

## [](#DESCRIPTION)DESCRIPTION

           The file ETCDIR/lloadd.conf contains configuration information for
           the lloadd(8)daemon.

           The lloadd.conf file consists of a series of global configuration
           options that apply to lloadd as a whole (including all backends),
           followed by zero or more backend definitions that contain
           information specific how a backend instance should be contacted.
           The configuration options are case-insensitive; their value, on a
           case by case basis, may be case-sensitive.

           The general format of lloadd.conf is as follows:

               # The following two lines should only be present if configured as a
               # slapd module:
               backend lload
               listen <URIs to be managed by lloadd>
               # comment - these options apply to the server as a whole
               <global configuration options>
               # first tier definition
               tier <strategy>
               # first backend definition
               backend-server <backend 1 definition>
               # subsequent backend/tier definitions
               ...

           As many tiers and backend servers may be configured as desired.

           If a line begins with white space, it is considered a continuation
           of the previous line.  No physical line should be over 2000 bytes
           long.

           Blank lines and comment lines beginning with a `#' character are
           ignored.  Note: continuation lines are unwrapped before comment
           processing is applied.

           Arguments on configuration lines are separated by white space. If
           an argument contains white space, the argument should be enclosed
           in double quotes.  If an argument contains a double quote (`"') or
           a backslash character (`\'), the character should be preceded by a
           backslash character.

           The specific configuration options available are discussed below
           in the Global Configuration Options and General Backend Options.
           Refer to the "OpenLDAP Administrator's Guide" for more details on
           the lloadd configuration file.

## [](#SLAPD_INTEGRATION)SLAPD INTEGRATION

           Note that when lloadd is configured as a slapd module, any option
           that shares the same name as an option in slapd.conf(5), the slapd
           interpretation wins and the lloadd option mentioned is unavailable
           through slapd.conf(5) directly, instead, it would have to be
           configured via a dedicated attribute in cn=config. In particular,
           unless the TLSShareSlapdCTX option is set, lloadd keeps its own
           TLS context which cannot be configured except through the dynamic
           configuration.

           An additional option is available when running as a slapd module:

           listen <listen URIs>
                  The URIs the Load Balancer module should listen on. Must
                  not overlap with the ones that slapd uses for its own
                  listening sockets. The related cn=config attribute is
                  olcBkLloadListen with each URI provided as a separate
                  value. No changes to this attribute made after the server
                  has started up will take effect until it is restarted.

## [](#GLOBAL_CONFIGURATION_OPTIONS)GLOBAL CONFIGURATION OPTIONS

           Options described in this section apply to all backends. Arguments
           that should be replaced by actual text are shown in brackets <>.

           argsfile <filename>
                  The (absolute) name of a file that will hold the lloadd
                  server's command line (program name and options).

           concurrency <integer>
                  Specify a desired level of concurrency.  Provided to the
                  underlying thread system as a hint.  The default is not to
                  provide any hint.

           enable <feature>
                  Switch additional features supported by the LDAP Load
                  Balancer on.  Supported features are:
                         proxyauthz
                                when proxying an operation, pass the client's
                                authorized identity using the proxy
                                authorization control (RFC 4370). No control
                                is added to the operation if initiated by a
                                client whose bound identity matches the
                                identity configured in bindconf (no
                                normalisation of the DN is attempted). This
                                feature is enabled by default.

                                If SASL binds are issued by clients and this
                                feature is enabled, backend servers need to
                                support LDAP Who Am I? extended operation for
                                the Load Balancer to detect the correct
                                authorization identity.

           disable <feature>
                  Switch features supported by the LDAP Load Balancer off.
                  See features listed in the enable option for a list.

           include <filename>
                  Read additional configuration information from the given
                  file before continuing with the next line of the current
                  file.

           io-threads <integer>
                  Specify the number of threads to use for the connection
                  manager.  The default is 1 and this is typically adequate
                  for up to 16 CPU cores.  The value should be set to a power
                  of 2.

                  If modified after server starts up, a change to this option
                  will not take effect until the server has been restarted.

           logfile <filename>
                  Specify a file for recording lloadd debug messages. By
                  default these messages only go to stderr, are not recorded
                  anywhere else, and are unrelated to messages exposed by the

           logfile-format debug | syslog-utc | syslog-localtime
                  Specify the prefix format for messages written to the
                  logfile. The debug format is the normal format used for
                  slapd debug messages, with a timestamp in hexadecimal,
                  followed by a thread ID.  The other options are to use
                  syslog(3) style prefixes, with timestamps either in UTC or
                  in the local timezone. The default is debug format.
                  loglevel configuration parameter. Specifying a logfile
                  copies messages to both stderr and the logfile.

           logfile-only on | off
                  Specify that debug messages should only go to the
                  configured logfile, and not to stderr.

           logfile-rotate <max> <Mbytes> <hours>
                  Specify automatic rotation for the configured logfile as
                  the maximum number of old logfiles to retain, a maximum
                  size in megabytes to allow a logfile to grow before
                  rotation, and a maximum age in hours for a logfile to be
                  used before rotation. The maximum number must be in the
                  range 1-99.  Setting Mbytes or hours to zero disables the
                  size or age check, respectively.  At least one of Mbytes or
                  hours must be non-zero. By default no automatic rotation
                  will be performed.

           loglevel <integer> [...]
                  Specify the level at which debugging statements and
                  operation statistics should be syslogged (currently logged
                  to the syslogd(8) LOG_LOCAL4 facility).  They must be
                  considered subsystems rather than increasingly verbose log
                  levels.  Some messages with higher priority are logged
                  regardless of the configured loglevel as soon as any
                  logging is configured.  Log levels are additive, and
                  available levels are:
                         1      (0x1 trace) trace function calls
                         2      (0x2 packets) debug packet handling
                         4      (0x4 args) heavy trace debugging (function
                                args)
                         8      (0x8 conns) connection management
                         16     (0x10 BER) print out packets sent and
                                received
                         64     (0x40 config) configuration file processing
                         256    (0x100 stats) connections, LDAP operations,
                                results (recommended)
                         512    (0x200 stats2) stats log entries sent

                         32768  (0x8000 none) only messages that get logged
                                whatever log level is set
                  The desired log level can be input as a single integer that
                  combines the (ORed) desired levels, both in decimal or in
                  hexadecimal notation, as a list of integers (that are ORed
                  internally), or as a list of the names that are shown
                  between parentheses, such that

                      loglevel 513
                      loglevel 0x201
                      loglevel 512 1
                      loglevel 0x200 0x1
                      loglevel stats trace

                  are equivalent.  The keyword any can be used as a shortcut
                  to enable logging at all levels (equivalent to -1).  The
                  keyword none, or the equivalent integer representation,
                  causes those messages that are logged regardless of the
                  configured loglevel to be logged.  In fact, if loglevel is
                  set to 0, no logging occurs, so at least the none level is
                  required to have high priority messages logged.

                  The loglevel defaults to stats.  This level should usually
                  also be included when using other loglevels, to help
                  analyze the logs.

           pidfile <filename>
                  The (absolute) name of a file that will hold the lloadd
                  server's process ID (see getpid(2)).

           sockbuf_max_incoming_client <integer>
                  Specify the maximum LDAP PDU size accepted coming from
                  clients.  The default is 262143.

           sockbuf_max_incoming_upstream <integer>
                  Specify the maximum LDAP PDU size accepted coming from
                  upstream connections.  The default is 4194303.

           sockbuf_max_pending_client <integer>
                  Specify the maximum amount of data we can store toward a
                  client connection.  The default is 0, with no limit on the
                  data being buffered.

           tcp-buffer [listener=<URL>] [{read|write}=]<size>
                  Specify the size of the TCP buffer.  A global value for
                  both read and write TCP buffers related to any listener is
                  defined, unless the listener is explicitly specified, or
                  either the read or write qualifiers are used.  See tcp(7)
                  for details.  Note that some OS-es implement automatic TCP
                  buffer tuning.

           threads <integer>
                  Specify the maximum size of the primary thread pool.  The
                  default is 16; the minimum value is 2.

           threadqueues <integer>
                  Specify the number of work queues to use for the primary
                  thread pool.  The default is 1 and this is typically
                  adequate for up to 8 CPU cores.  The value should not
                  exceed the number of CPUs in the system.

           max_pdus_per_cycle <integer>
                  If set to 0, PDUs are handled by the I/O threads directly,
                  otherwise a task is queued to be picked up by the thread
                  pool. This task will process PDUs from the connection until
                  there is no more data to be read or this limit is reached
                  when the I/O thread can pick it up again.  Very high values
                  have a potential to cause some connections to be starved in
                  a very high-bandwidth environment. The default is 1000.

           client_max_pending <integer>
                  Will cause the load balancer to limit the number unfinished
                  operations for each client connection. The default is 0,
                  unlimited.

           iotimeout <integer>
                  Specify the number of milliseconds to wait before forcibly
                  closing a connection with an outstanding write. This allows
                  faster recovery from various network hang conditions.  An
                  iotimeout of 0 disables this feature.  The default is
                  10000.

           write_coherence <integer>
                  Specify the number of seconds after a write operation is
                  finished that lloadd will direct operations exclusively to
                  the last selected backend. A write operation is anything
                  not handled internally (certain exops, abandon), except
                  search, compare and bind operations. Bind operations also
                  reset this restriction. The default is 0, write operations
                  do not restrict selection. When negative, the restriction
                  is not time limited and will persist until the next bind.

           restrict_exop <OID> <action>
                  Tell lloadd that extended operation with a given OID should
                  be handled in a specific way.  OID 1.1 is special, setting
                  a default (only for operations not handled internally).
                  The meaning of the <action> argument is the same as in
                  restrict_control below.

           restrict_control <OID> <action>
                  Tell lloadd that a control with a given OID attached to any
                  operation should be handled in a specific way according to
                  the <action> argument. At the moment, only operations
                  passed intact are inspected in this way, in particular,
                  controls on bind and extended operations are not checked.

                  In order of descending priority (the control with highest
                  priority action wins), this is the action made:
                         reject operations that carry this control will be
                                rejected.
                         connection
                                once an upstream is selected, every future
                                operation from this client will be directed
                                to the same connection. Useful when state is
                                shared between client and upstream that the
                                load balancer doesn't track.
                         backend
                                like write except this does not time out.
                         write  this is treated like a write operation (see
                                write_coherence) above.
                         ignore does not influence restrictions, useful when
                                changing the global exop default.  This is
                                the default handling for exops/controls not
                                handled by the load balancer internally.

## [](#TLS_OPTIONS)TLS OPTIONS

           If lloadd is built with support for Transport Layer Security,
           there are more options you can specify.

           TLSShareSlapdCTX { on | off }
                  If set to no (the default), lloadd will use its own TLS
                  context (needs to be configured via cn=config unless lloadd
                  is run as a standalone daemon). If enabled, the options for
                  slapd apply instead, since the slapd's TLS context is used
                  then.

           The following options are available only when compiled as a
           standalone daemon.  When compiled as a slapd(8) module, the
           cn=config equivalents need to be used if a separate TLS context
           for the module is needed, otherwise use the TLSShareSlapdCTX
           option.

           TLSCipherSuite <cipher-suite-spec>
                  Permits configuring what ciphers will be accepted and the
                  preference order.  <cipher-suite-spec> should be a cipher
                  specification for the TLS library in use (OpenSSL or
                  GnuTLS).  This directive is not supported when using
                  MbedTLS.  Example:

                         OpenSSL:
                                TLSCipherSuite HIGH:MEDIUM:+SSLv2

                         GnuTLS:
                                TLSCiphersuite SECURE256:!AES-128-CBC

                  To check what ciphers a given spec selects in OpenSSL, use:

                       openssl ciphers -v <cipher-suite-spec>

                  With GnuTLS the available specs can be found in the manual
                  page of gnutls-cli(1) (see the description of the option
                  --priority).

                  In older versions of GnuTLS, where gnutls-cli does not
                  support the option --priority, you can obtain the — more
                  limited — list of ciphers by calling:

                       gnutls-cli -l

           TLSCACertificateFile <filename>
                  Specifies the file that contains certificates for all of
                  the Certificate Authorities that lloadd will recognize.
                  The certificate for the CA that signed the server
                  certificate must be included among these certificates. If
                  the signing CA was not a top-level (root) CA, certificates
                  for the entire sequence of CA's from the signing CA to the
                  top-level CA should be present. Multiple certificates are
                  simply appended to the file; the order is not significant.

           TLSCACertificatePath <path>
                  Specifies the path of a directory that contains Certificate
                  Authority certificates in separate individual files.
                  Usually only one of this or the TLSCACertificateFile is
                  used. This directive is not supported when using GnuTLS.

           TLSCertificateFile <filename>
                  Specifies the file that contains the lloadd server
                  certificate.

           TLSCertificateKeyFile <filename>
                  Specifies the file that contains the lloadd server private
                  key that matches the certificate stored in the
                  TLSCertificateFile file.  Currently, the private key must
                  not be protected with a password, so it is of critical
                  importance that it is protected carefully.

           TLSDHParamFile <filename>
                  This directive specifies the file that contains parameters
                  for Diffie-Hellman ephemeral key exchange.  This is
                  required in order to use a DSA certificate on the server,
                  or an RSA certificate missing the "key encipherment" key
                  usage.  Note that setting this option may also enable
                  Anonymous Diffie-Hellman key exchanges in certain non-
                  default cipher suites.  Anonymous key exchanges should
                  generally be avoided since they provide no actual client or
                  server authentication and provide no protection against
                  man-in-the-middle attacks.  You should append "!ADH" to
                  your cipher suites to ensure that these suites are not
                  used.  This directive is not supported when using MbedTLS.

           TLSECName <name>
                  Specify the name of a curve to use for Elliptic curve
                  Diffie-Hellman ephemeral key exchange.  This is required to
                  enable ECDHE algorithms in OpenSSL.  This option is not
                  used with GnuTLS; the curves may be chosen in the GnuTLS
                  ciphersuite specification.

           TLSProtocolMin <major>[.<minor>]
                  Specifies minimum SSL/TLS protocol version that will be
                  negotiated.  If the server doesn't support at least that
                  version, the SSL handshake will fail.  To require TLS 1.x
                  or higher, set this option to 3.(x+1), e.g.,

                       TLSProtocolMin 3.2

                  would require TLS 1.1.  Specifying a minimum that is higher
                  than that supported by the OpenLDAP implementation will
                  result in it requiring the highest level that it does
                  support.  This directive is ignored with GnuTLS.

           TLSRandFile <filename>
                  Specifies the file to obtain random bits from when
                  /dev/[u]random is not available.  Generally set to the name
                  of the EGD/PRNGD socket.  The environment variable RANDFILE
                  can also be used to specify the filename.  This directive
                  is ignored with GnuTLS.

           TLSVerifyClient <level>
                  Specifies what checks to perform on client certificates in
                  an incoming TLS session, if any.  The <level> can be
                  specified as one of the following keywords:

                  never  This is the default.  lloadd will not ask the client
                         for a certificate.

                  allow  The client certificate is requested.  If no
                         certificate is provided, the session proceeds
                         normally.  If a bad certificate is provided, it will
                         be ignored and the session proceeds normally.

                  try    The client certificate is requested.  If no
                         certificate is provided, the session proceeds
                         normally.  If a bad certificate is provided, the
                         session is immediately terminated.

                  demand | hard | true
                         These keywords are all equivalent, for compatibility
                         reasons.  The client certificate is requested.  If
                         no certificate is provided, or a bad certificate is
                         provided, the session is immediately terminated.

                  TLSCRLCheck <level>
                         Specifies if the Certificate Revocation List (CRL)
                         of the CA should be used to verify if the client
                         certificates have not been revoked. This requires
                         TLSCACertificatePath parameter to be set. This
                         directive is ignored with GnuTLS.  <level> can be
                         specified as one of the following keywords:

                         none   No CRL checks are performed

                         peer   Check the CRL of the peer certificate

                         all    Check the CRL for a whole certificate chain

                  TLSCRLFile <filename>
                         Specifies a file containing a Certificate Revocation
                         List to be used for verifying that certificates have
                         not been revoked. This directive is only valid when
                         using GnuTLS.

## [](#BACKEND_CONFIGURATION)BACKEND CONFIGURATION

           Options in this section describe how the lloadd connects and
           authenticates to the backend servers. Backends are organised in
           groups (tiers).  Backends in the first tier are tried first, if
           none of them are reachable, the following tier is tried in the
           same way. If there is a backend in the tier that has suitable
           connections, but they are busy, no further tier is consulted. This
           is useful in high availability scenarios where a group of servers
           (e.g. the local environment) should be contacted if possible.

           It is assumed all backend servers serve the same data. On startup,
           the configured connections are set up and those not dedicated to
           handle bind requests are authenticated with the backend using the
           information in the bindconf option. The authentication
           configuration is shared between them.

           bindconf
                  [bindmethod=simple|sasl] [binddn=<dn>] [saslmech=<mech>]
                  [authcid=<identity>] [authzid=<identity>]
                  [credentials=<passwd>] [realm=<realm>]
                  [secprops=<properties>] [timeout=<seconds>]
                  [network-timeout=<seconds>]
                  [keepalive=<idle>:<probes>:<interval>]
                  [tcp-user-timeout=<milliseconds>] [tls_cert=<file>]
                  [tls_key=<file>] [tls_cacert=<file>] [tls_cacertdir=<path>]
                  [tls_reqcert=never|allow|try|demand]
                  [tls_cipher_suite=<ciphers>] [tls_crlcheck=none|peer|all]
                  [tls_protocol_min=<major>[.<minor>]]

                  Specifies the bind credentials lloadd uses when setting up
                  its regular connections to all backends.

                  A bindmethod of simple requires the options binddn and
                  credentials and should only be used when adequate security
                  services (e.g. TLS or IPSEC) are in place.  REMEMBER:
                  simple bind credentials must be in cleartext!  A bindmethod
                  of sasl requires the option saslmech.  Depending on the
                  mechanism, an authentication identity and/or credentials
                  can be specified using authcid and credentials.  The
                  authzid parameter may be used to specify an authorization
                  identity.  Specific security properties (as with the
                  sasl-secprops keyword above) for a SASL bind can be set
                  with the secprops option. A non default SASL realm can be
                  set with the realm option.

                  The timeout parameter indicates how long an operation can
                  be pending a response (result, search entry, ...) from the
                  server in seconds. Due to how timeouts are detected, the
                  timeout might not be detected and handled up to timeout
                  seconds after it happens.

                  The network-timeout parameter sets how long the consumer
                  will wait to establish a network connection to the
                  provider. Once a connection is established, the timeout
                  parameter determines how long the consumer will wait for
                  the initial Bind request to complete.

                  Timeout set to 0 means no timeout is in effect and by
                  default, no timeouts are in effect.

                  The keepalive parameter sets the values of idle, probes,
                  and interval used to check whether a socket is alive; idle
                  is the number of seconds a connection needs to remain idle
                  before TCP starts sending keepalive probes; probes is the
                  maximum number of keepalive probes TCP should send before
                  dropping the connection; interval is interval in seconds
                  between individual keepalive probes.  Only some systems
                  support the customization of these values; the keepalive
                  parameter is ignored otherwise, and system-wide settings
                  are used.

                  The tcp-user-timeout parameter, if non-zero, corresponds to
                  the TCP_USER_TIMEOUT set on the upstream connections,
                  overriding the operating system setting.  Only some systems
                  support the customization of this parameter, it is ignored
                  otherwise and system-wide settings are used.

## [](#TIER_OPTIONS)TIER OPTIONS

           tier   <tier type>

                  Groups servers which should be considered in the same try.
                  If a viable connection is found even if busy, the load
                  balancer does not proceed to the next tier. The process of
                  selection a connection within a tier depends on the tier's
                  type.

           Available types are:

           roundrobin
                  Servers are tried in order and if one is selected
                  successfully, the following search will try from the one
                  next on the list.

           weighted
                  Backend servers accept a new option weight=<int> which
                  indicates how often it should be selected. If unspecified,
                  weight defaults to 0 and such backends have a slight chance
                  of being selected even when a non-zero weight backend is
                  configured in the tier. The selection process is along the
                  lines of RFC2782.

           bestof Like with weighted, backends accept the weight=<int>
                  option. Average latency multiplied by weight is measured
                  over time. The selection process chooses 2 backends at
                  random, compares their weighted latencies and the backend
                  with a better (lower) score is tried. If the backend is not
                  available (or is busy), the other backend is tried, then
                  backends are chosen in a round-robin order.

                  Note that unlike weighted, the higher the weight, the
                  higher the "effective" latency and lower the chance a
                  backend is selected.

## [](#BACKEND_OPTIONS)BACKEND OPTIONS

           backend-server
                  uri=ldap[s]://<hostname>[:port] [retry=<retry interval in
                  ms>] [starttls=yes|critical] [numconns=<conns>]
                  [bindconns=<conns>] [max-pending-ops=<ops>] [conn-max-
                  pending=<ops>]

                  Marks the beginning of a backend definition.

                  uri specifies the backend as an LDAP URI. If <port> is not
                  given, the standard LDAP port number (389 or 636) is used.

                  Lloadd will attempt to maintain numconns active connections
                  and also bindconns active connections dedicated to handling
                  client bind requests.

                  If an error occurs on a working connection, a new
                  connection attempt is made immediately, if one happens on
                  establishing a new connection to this backend, lloadd will
                  wait before a new reconnect attempt is made according to
                  the retry parameter (default is 5 seconds).

                  Operations will be distributed across the backend's
                  connections (upstreams).

                  The parameter conn-max-pending unless set to 0 (the
                  default), will limit the number unfinished operations per
                  upstream connection. Similarly, max-pending-ops will limit
                  the total number or unfinished operations across all
                  backend's connections, 0, the default, means no limit will
                  be imposed for this backend.

                  The starttls parameter specifies use of the StartTLS
                  extended operation to establish a TLS session before
                  Binding to the provider. If the critical argument is
                  supplied, the session will be aborted if the StartTLS
                  request fails. Otherwise the syncrepl session continues
                  without TLS. The tls_reqcert setting defaults to "demand"
                  and the other TLS settings default to the same as the main
                  slapd TLS settings.

## [](#EXAMPLES)EXAMPLES

           Here is a short example of a configuration file:

                  argsfile  LOCALSTATEDIR/run/lloadd.args
                  pidfile   LOCALSTATEDIR/run/lloadd.pid

                  # cancel not supported yet
                  restrict_exop 1.3.6.1.1.8 reject

                  # turn not supported
                  restrict_exop 1.3.6.1.1.19 reject

                  # TXN Exop if desired, otherwise reject
                  restrict_exop 1.3.6.1.1.21.1 connection

                  # Paged results control
                  restrict_control 1.2.840.113556.1.4.319 connection

                  # VLV control
                  restrict_control 2.16.840.1.113730.3.4.9 connection

                  bindconf
                      bindmethod=simple
                      binddn=cn=test
                      credentials=pass

                  tier weighted
                  backend-server
                      uri=ldap://ldap1.example.com
                      numconns=3
                      bindconns=2
                      retry=5000
                      max-pending-ops=5
                      conn-max-pending=3
                      weight=5

                  backend-server
                      uri=ldap://ldap2.example.com
                      numconns=3
                      bindconns=2
                      retry=5000
                      max-pending-ops=5
                      conn-max-pending=3
                      weight=10

           "OpenLDAP Administrator's Guide" contains a longer annotated
           example of a configuration file.  The original ETCDIR/lloadd.conf
           is another example.

## [](#LIMITATIONS)LIMITATIONS

           Support for proxying SASL Binds is limited to the EXTERNAL
           mechanism (and only to extract the DN of a client TLS certificate
           if used during the last renegotiation) and mechanisms that rely
           neither on connection metadata (as Kerberos does) nor establish a
           SASL integrity/confidentialiy layer (again, some Kerberos
           mechanisms, DIGEST-MD5 can negotiate this).

## [](#FILES)FILES

           ETCDIR/lloadd.conf
                  default lloadd configuration file

## [](#SEE_ALSO)SEE ALSO

           ldap(3), gnutls-cli(1), slapd.conf(5), tcp(7), lloadd(8),
           slapd(8).

           "OpenLDAP Administrator's Guide"
           (http://www.OpenLDAP.org/doc/admin/)

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

    OpenLDAP LDVERSION             RELEASEDATE                 LLOADD.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [lloadd(8)](../man8/lloadd.8.html)

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
