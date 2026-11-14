---
{"title": "slapd-asyncmeta(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd-asyncmeta.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd-asyncmeta(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [CONFIGURATION](#CONFIGURATION) \| [SPECIAL CONFIGURATION DIRECTIVES](#SPECIAL_CONFIGURATION_DIRECTIVES) \| [TARGET SPECIFICATION](#TARGET_SPECIFICATION) \| [SCENARIOS](#SCENARIOS) \| [ACLs](#ACLs) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD-ASYNCMETA(5)         File Formats Manual         SLAPD-ASYNCMETA(5)

## [](#NAME)NAME

           slapd-asyncmeta - asynchronous metadirectory backend to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The asyncmeta backend to slapd(8) performs basic LDAP proxying
           with respect to a set of remote LDAP servers, called "targets".
           The information contained in these servers can be presented as
           belonging to a single Directory Information Tree (DIT).

           A good knowledge of the functionality of the slapd-meta(5) backend
           is recommended.   This  backend has been designed as an
           asynchronous version of the meta backend. Unlike meta , the
           operation handling threads are no longer pending on the response
           from the remote server, thus decreasing the number of threads
           necessary to handle the same load. While asyncmeta maintains the
           functionality of meta and has a largely similar codebase, some
           changes in operation and some new configuration directives have
           been added. Some configuration options, such as conn-pool-max ,
           conn-ttl , single-conn , and use-temporary-conn have been removed,
           as they are no longer relevant.

           New connection handling:

           Unlike meta, which caches bound connections, the asyncmeta works
           with a configured maximum number of connections per target.  For
           each request redirected to a target, a different connection is
           selected.  Each connection has a queue, to which the request is
           added before it is sent to the remote server, and is removed after
           the last response for that request is received.
            For each new request, a new connection is chosen using
           round-robin scheduling.

           Overlays:

           Due to implementation specifics, there is no guarantee that any of
           the existing OpenLDAP overlays will work with asyncmeta backend.

## [](#EXAMPLES)EXAMPLES

           Refer to slapd-meta(5) for configuration examples.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the ASYNCMETA backend database.
           That is, they must follow a "database asyncmeta" line and come
           before any subsequent "backend" or "database" lines.  Other
           database options are described in the slapd.conf(5) manual page.

## [](#SPECIAL_CONFIGURATION_DIRECTIVES)SPECIAL CONFIGURATION DIRECTIVES

           Target configuration starts with the "uri" directive.  All the
           configuration directives that are not specific to targets should
           be defined first for clarity, including those that are common to
           all backends.  They are:

           default-target none
                  This directive forces the backend to reject all those
                  operations that must resolve to a single target in case
                  none or multiple targets are selected.  They include: add,
                  delete, modify, modrdn; compare is not included, as well as
                  bind since, as they don't alter entries, in case of
                  multiple matches an attempt is made to perform the
                  operation on any candidate target, with the constraint that
                  at most one must succeed.  This directive can also be used
                  when processing targets to mark a specific target as
                  default.

           dncache-ttl {DISABLED|forever|<ttl>}
                  This directive sets the time-to-live of the DN cache.  This
                  caches the target that holds a given DN to speed up target
                  selection in case multiple targets would result from an
                  uncached search; forever means cache never expires;
                  disabled means no DN caching; otherwise a valid ( > 0 ) ttl
                  is required, in the format illustrated for the idle-timeout
                  directive.

           onerr {CONTINUE|report|stop}
                  This directive allows one to select the behavior in case an
                  error is returned by one target during a search.  The
                  default, continue, consists in continuing the operation,
                  trying to return as much data as possible.  If the value is
                  set to stop, the search is terminated as soon as an error
                  is returned by one target, and the error is immediately
                  propagated to the client.  If the value is set to report,
                  the search is continued to the end but, in case at least
                  one target returned an error code, the first non-success
                  error code is returned.

           max-timeout-ops <number>
                  Specify the number of consecutive timed out requests, after
                  which the connection will be considered faulty and dropped.

           max-pending-ops <number>
                  The maximum number of pending requests stored in a
                  connection's queue.  The default is 128. When this number
                  is exceeded, LDAP_BUSY will be returned to the client.

           max-target-conns <number>
                  The maximum number of connections per target. Unlike
                  slapd-meta(5), no new connections will be created once this
                  number is reached. The default value is 255.

           norefs <NO|yes>
                  If yes, do not return search reference responses.  By
                  default, they are returned unless request is LDAPv2.  If
                  set before any target specification, it affects all
                  targets, unless overridden by any per-target directive.

           noundeffilter <NO|yes>
                  If yes, return success instead of searching if a filter is
                  undefined or contains undefined portions.  By default, the
                  search is propagated after replacing undefined portions
                  with (!(objectClass=*)), which corresponds to the empty
                  result set.  If set before any target specification, it
                  affects all targets, unless overridden by any per-target
                  directive.

           protocol-version {0,2,3}
                  This directive indicates what protocol version must be used
                  to contact the remote server.  If set to 0 (the default),
                  the proxy uses the same protocol version used by the
                  client, otherwise the requested protocol is used.  The
                  proxy returns unwillingToPerform if an operation that is
                  incompatible with the requested protocol is attempted.  If
                  set before any target specification, it affects all
                  targets, unless overridden by any per-target directive.

           pseudoroot-bind-defer {YES|no}
                  This directive, when set to yes, causes the authentication
                  to the remote servers with the pseudo-root identity (the
                  identity defined in each idassert-bind directive) to be
                  deferred until actually needed by subsequent operations.
                  Otherwise, all binds as the rootdn are propagated to the
                  targets.

           quarantine <interval>,<num>[;<interval>,<num>[...]]
                  Turns on quarantine of URIs that returned LDAP_UNAVAILABLE,
                  so that an attempt to reconnect only occurs at given
                  intervals instead of any time a client requests an
                  operation.  The pattern is: retry only after at least
                  interval seconds elapsed since last attempt, for exactly
                  num times; then use the next pattern.  If num for the last
                  pattern is "+", it retries forever; otherwise, no more
                  retries occur.  This directive must appear before any
                  target specification; it affects all targets with the same
                  pattern.

           rebind-as-user {NO|yes}
                  If this option is given, the client's bind credentials are
                  remembered for rebinds, when trying to re-establish a
                  broken connection, or when chasing a referral, if
                  chase-referrals is set to yes.

           session-tracking-request {NO|yes}
                  Adds session tracking control for all requests.  The
                  client's IP and hostname, and the identity associated to
                  each request, if known, are sent to the remote server for
                  informational purposes.  This directive is incompatible
                  with setting protocol-version to 2.  If set before any
                  target specification, it affects all targets, unless
                  overridden by any per-target directive.

## [](#TARGET_SPECIFICATION)TARGET SPECIFICATION

           Target specification starts with a "uri" directive:

           uri <protocol>://[<host>]/<naming context> [...]
                  Identical to meta.  See slapd-meta(5) for details.

           acl-authcDN <administrative DN for access control purposes>
                  DN which is used to query the target server for acl
                  checking, as in the LDAP backend; it is supposed to have
                  read access on the target server to attributes used on the
                  proxy for acl checking.  There is no risk of giving away
                  such values; they are only used to check permissions.  The
                  acl-authcDN identity is by no means implicitly used by the
                  proxy when the client connects anonymously.

           acl-passwd <password>
                  Password used with the acl-authcDN above.

           bind-timeout <microseconds>
                  This directive defines the timeout, in microseconds, used
                  when polling for response after an asynchronous bind
                  connection. See slapd-meta(5) for details.

           chase-referrals {YES|no}
                  enable/disable automatic referral chasing, which is
                  delegated to the underlying libldap, with rebinding
                  eventually performed if the rebind-as-user directive is
                  used.  The default is to chase referrals.  If set before
                  any target specification, it affects all targets, unless
                  overridden by any per-target directive.

           client-pr {accept-unsolicited|DISABLE|<size>}
                  This feature allows one to use RFC 2696 Paged Results
                  control when performing search operations with a specific
                  target, irrespective of the client's request. See
                  slapd-meta(5) for details.

           conn-ttl <time> [<interval>]
                  This directive causes a persistent connection  to  be
                  dropped after it  has been established for the specified
                  time, no more often that one connection per interval per
                  target. The connection will be re-created the next time it
                  is selected for use.  If there are pending requests in its
                  queue, the connection will be marked as closing and no new
                  requests will be proxied through it.  It will be dropped
                  after the last request one has either received a result or
                  has timed out.  To avoid too many connections being dropped
                  at the same time, the interval directive is introduced, to
                  specify the minimum time interval between resetting a
                  connection to the same target.  The default value is 1
                  second. If time is set to 0, the oldest connection will be
                  chosen for reset at every interval period. If interval is
                  set to 0, all connections exceeding their ttl will be
                  dropped as soon as there are no more pending operations.

                  [<d>d][<h>h][<m>m][<s>[s]]

                  where <d>, <h>, <m> and <s> are respectively treated as
                  days, hours, minutes and seconds.

                  EXAMPLES

                  conn-ttl 60s 5s
                   - Connections older that 60 seconds will be reset, no more
                  often that one connection per target every 5 seconds.

                  conn-ttl 0 5s
                   - Every 5 seconds, the oldest connection of each target
                  will be reset.

                  conn-ttl 1h
                   - Connection older than 1h will be reset, no more often
                  than once a second per target.

                  If set before any target specification, it affects all
                  targets, unless overridden by any per-target directive. It
                  is disabled by default.

           default-target [<target>]
                  The "default-target" directive can also be used during
                  target specification.  With no arguments it marks the
                  current target as the default.  The optional number marks
                  target <target> as the default one, starting from 1.
                  Target <target> must be defined.

           filter <pattern>
                  This directive allows specifying a regex(5) pattern to
                  indicate what search filter terms are actually served by a
                  target.

                  In a search request, if the search filter matches the
                  pattern the target is considered while fulfilling the
                  request; otherwise the target is ignored. There may be
                  multiple occurrences of the filter directive for each
                  target.

           idassert-authzFrom <authz-regexp>
                  if defined, selects what local identities are authorized to
                  exploit the identity assertion feature.  The string <authz-
                  regexp> follows the rules defined for the authzFrom
                  attribute.  See slapd.conf(5), section related to
                  authz-policy, for details on the syntax of this field.

           idassert-bind bindmethod=none|simple|sasl [binddn=<simple DN>]
                  [credentials=<simple password>] [saslmech=<SASL mech>]
                  [secprops=<properties>] [realm=<realm>]
                  [authcId=<authentication ID>] [authzId=<authorization ID>]
                  [authz={native|proxyauthz}] [mode=<mode>] [flags=<flags>]
                  [starttls=no|yes|critical] [tls_cert=<file>]
                  [tls_key=<file>] [tls_cacert=<file>] [tls_cacertdir=<path>]
                  [tls_reqcert=never|allow|try|demand]
                  [tls_reqsan=never|allow|try|demand]
                  [tls_cipher_suite=<ciphers>] [tls_ecname=<names>]
                  [tls_protocol_min=<major>[.<minor>]]
                  [tls_crlcheck=none|peer|all] Allows one to define the
                  parameters of the authentication method that is internally
                  used by the proxy to authorize connections that are
                  authenticated by other databases. See slapd-meta(5) for
                  details.

           idle-timeout <time>
                  This directive causes a persistent connection  to  be
                  dropped after it  has been idle for the specified time. The
                  connection will be re-created the next time it is selected
                  for use. A connection is considered idle if no attempts
                  have been made by the backend to use it to send a request
                  to the backend server. If there are still pending requests
                  in its queue, the connection will be dropped after the last
                  request one has either received a result or has timed out.

                  [<d>d][<h>h][<m>m][<s>[s]]

                  where <d>, <h>, <m> and <s> are respectively treated as
                  days, hours, minutes and seconds.  If set before any target
                  specification, it affects all targets, unless overridden by
                  any per-target directive.

           keepalive <idle>:<probes>:<interval>
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

           tcp-user-timeout <milliseconds>
                  If non-zero, corresponds to the TCP_USER_TIMEOUT set on the
                  target connections, overriding the operating system
                  setting.  Only some systems support the customization of
                  this parameter, it is ignored otherwise and system-wide
                  settings are used.

           map {attribute|objectclass} [<local name>|*] {<foreign name>|*}
                  This maps object classes and attributes as in the LDAP
                  backend.  See slapd-ldap(5).

           network-timeout <time>
                  Sets the network timeout value after which
                  poll(2)/select(2) following a connect(2) returns in case of
                  no activity while sending an operation to the remote
                  target.  The value is in milliseconds, and it can be
                  specified as for idle-timeout.  If set before any target
                  specification, it affects all targets, unless overridden by
                  any per-target directive.

           nretries {forever|never|<nretries>}
                  This directive defines how many times forwarding an
                  operation should be retried in case of temporary failure in
                  contacting a target. The number of retries is per
                  operation, so if a bind to the target is necessary first,
                  the remaining number is decremented. If defined before any
                  target specification, it applies to all targets (by
                  default, 3 times); the global value can be overridden by
                  redefinitions inside each target specification.

           subtree-{exclude|include} <rule>
                  This directive allows one to indicate what subtrees are
                  actually served by a target. See slapd-meta(5) for details.

           suffixmassage <local suffix> <remote suffix>
                  slapd-asyncmeta does not support the rewrite engine used by
                  the LDAP and META backends.  suffixmassage can be used to
                  perform DN suffix rewriting, the same way as the obsoleted
                  suffixmassage directive previously used by the LDAP
                  backend.

           t-f-support {NO|yes|discover}
                  enable if the remote server supports absolute filters (see
                  RFC 4526 for details).  If set to discover, support is
                  detected by reading the remote server's root DSE.  If set
                  before any target specification, it affects all targets,
                  unless overridden by any per-target directive.

           timeout [<op>=]<val> [...]
                  This directive allows one to set per-operation timeouts.
                  Operations can be

                  <op> ::= bind, add, delete, modrdn, modify, compare, search

                  By default, the timeout for all operations is 2 seconds.

                  See slapd-meta(5) for details.

           tls {none|[try-]start|[try-]propagate|ldaps}
                  B [starttls=no] [tls_cert=<file>] [tls_key=<file>]
                  [tls_cacert=<file>] [tls_cacertdir=<path>]
                  [tls_reqcert=never|allow|try|demand]
                  [tls_reqsan=never|allow|try|demand]
                  [tls_cipher_suite=<ciphers>] [tls_ecname=<names>]
                  [tls_crlcheck=none|peer|all]
                  Specify TLS settings regular connections.

                  If the first parameter is not "none" then this configures
                  the TLS settings to be used for regular connections.  The
                  StartTLS extended operation will be used when establishing
                  the connection unless the URI directive protocol scheme is
                  ldaps://.  In that case this keyword may only be set to
                  "ldaps" and the StartTLS operation will not be used.

                  With propagate, the proxy issues the StartTLS operation
                  only if the original connection has a TLS layer set up.
                  The try- prefix instructs the proxy to continue operations
                  if the StartTLS operation failed; its use is not
                  recommended.

                  The TLS settings default to the same as the main slapd TLS
                  settings, except for tls_reqcert which defaults to
                  "demand", tls_reqsan which defaults to "allow", and
                  starttls which is overshadowed by the first keyword and
                  thus ignored.

                  If set before any target specification, it affects all
                  targets, unless overridden by any per-target directive.

## [](#SCENARIOS)SCENARIOS

           See slapd-meta(5) for configuration scenarios.

## [](#ACLs)ACLs

           ACL behavior is identical to meta. See slapd-meta(5).

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The asyncmeta backend does not honor all ACL semantics as
           described in slapd.access(5).  In general, access checking is
           delegated to the remote server(s).  Only read (=r) access to the
           entry pseudo-attribute and to the other attribute values of the
           entries returned by the search operation is honored, which is
           performed by the frontend.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-ldap(5), slapd-meta(5), slapo-pcache(5),
           slapd(8), regex(7), re_format(7).

## [](#AUTHOR)AUTHOR

           Nadezhda Ivanova, based on back-meta by Pierangelo Masarati.

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

    OpenLDAP LDVERSION             RELEASEDATE             SLAPD-ASYNCMETA(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.backends(5)](../man5/slapd.backends.5.html),  [slapd-meta(5)](../man5/slapd-meta.5.html)

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
