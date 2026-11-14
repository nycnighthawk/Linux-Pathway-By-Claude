---
{"title": "slapd-sock(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd-sock.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd-sock(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [PROTOCOL](#PROTOCOL) \| [KNOWN LIMITATIONS](#KNOWN_LIMITATIONS) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [EXAMPLE](#EXAMPLE) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD-SOCK(5)              File Formats Manual              SLAPD-SOCK(5)

## [](#NAME)NAME

           slapd-sock - Socket backend/overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The Socket backend to slapd(8) uses an external program to handle
           queries that listens on a Unix domain socket.  This makes it
           possible to have a pool of processes, which persist between
           requests. This allows multithreaded operation and a high level of
           efficiency. The external program must have been started
           independently; slapd(8) itself will not start it.

           This module may also be used as an overlay on top of some other
           database.  Use as an overlay allows external actions to be
           triggered in response to operations on the main database.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the SOCK backend database.  That
           is, they must follow a "database sock" line and come before any
           subsequent "backend" or "database" lines.  Other database options
           are described in the slapd.conf(5) manual page.

           Alternatively, to use this module as an overlay, these directives
           must follow an "overlay sock" line within an existing database
           definition.

           extensions [ binddn | peername | ssf | connid ]*
                  Enables the sending of additional meta-attributes with each
                  request.
                  binddn: <bound DN>
                  peername: IP=<address>:<port>
                  ssf: <SSF value>
                  connid: <connection ID>

           socketpath <pathname>
                  Gives the path to a Unix domain socket to which the
                  commands will be sent and from which replies are received.

                  When used as an overlay, these additional directives are
                  defined:

           sockops   [ bind | unbind | search | compare | modify | modrdn |
           add | delete | extended ]*
                  Specify which request types to send to the external
                  program. The default is empty (no requests are sent).

           sockresps [ result | search ]*
                  Specify which response types to send to the external
                  program. "result" sends just the results of an operation.
                  "search" sends all entries that the database returned for a
                  search request. The default is empty (no responses are
                  sent).

           sockdnpat <regexp>
                  Specify DN patterns for which the overlay will act. Only
                  operations on DNs matching the specified regular expression
                  will be processed. The default is empty (all DNs are
                  processed).

## [](#PROTOCOL)PROTOCOL

           The protocol uses a newline to terminate the command parameters.
           The following commands are sent:
                  ADD
                  msgid: <message id>
                  <repeat { "suffix:" <database suffix DN> }>
                  <entry in LDIF format>
                  <blank line>

                  BIND
                  msgid: <message id>
                  <repeat { "suffix:" <database suffix DN> }>
                  dn: <DN>
                  method: <method number>
                  credlen: <length of <credentials>>
                  cred: <credentials>
                  <blank line>

                  COMPARE
                  msgid: <message id>
                  <repeat { "suffix:" <database suffix DN> }>
                  dn: <DN>
                  <attribute>: <value>
                  <blank line>

                  DELETE
                  msgid: <message id>
                  <repeat { "suffix:" <database suffix DN> }>
                  dn: <DN>
                  <blank line>

                  EXTENDED
                  msgid: <message id>
                  <repeat { "suffix:" <database suffix DN> }>
                  oid: <OID>
                  value: <base64-value>
                  <blank line>

                  MODIFY
                  msgid: <message id>
                  <repeat { "suffix:" <database suffix DN> }>
                  dn: <DN>
                  <repeat {
                      <"add"/"delete"/"replace">: <attribute>
                      <repeat { <attribute>: <value> }>
                      -
                  }>
                  <blank line>

                  MODRDN
                  msgid: <message id>
                  <repeat { "suffix:" <database suffix DN> }>
                  dn: <DN>
                  newrdn: <new RDN>
                  deleteoldrdn: <0 or 1>
                  <if new superior is specified: "newSuperior: <DN>">
                  <blank line>

                  SEARCH
                  msgid: <message id>
                  <repeat { "suffix:" <database suffix DN> }>
                  base: <base DN>
                  scope: <0-2, see ldap.h>
                  deref: <0-3, see ldap.h>
                  sizelimit: <size limit>
                  timelimit: <time limit>
                  filter: <filter>
                  attrsonly: <0 or 1>
                  attrs: <"all" or space-separated attribute list>
                  <blank line>

                  UNBIND
                  msgid: <message id>
                  <repeat { "suffix:" <database suffix DN> }>
                  <blank line>

           The commands - except unbind - should output:
                  RESULT
                  code: <integer>
                  matched: <matched DN>
                  info: <text>
           where only RESULT is mandatory, and then close the socket.  The
           search RESULT should be preceded by the entries in LDIF format,
           each entry followed by a blank line.  Lines starting with `#' or
           `DEBUG:' are ignored.

           When used as an overlay, the external program should return a
           CONTINUE response if request processing should continue normally,
           or a regular RESULT response if the external program wishes to
           bypass the underlying database.

           If sockresps includes result or search, the overlay will also send
           any response messages to the external program (also see KNOWN
           LIMITATIONS). These will appear as an extended RESULT message or
           an ENTRY message respectively, both are defined below and the
           program is not expected to respond to these.

           The extended RESULT message is similar to the one above, but also
           includes the msgid and any configured extensions:
                  RESULT
                  msgid: <message id>
                  code: <integer>
                  matched: <matched DN>
                  info: <text>
                  <blank line>

           Typically both the msgid and the connid will be needed to match a
           result message to a request. The ENTRY message has the form
                  ENTRY
                  msgid: <message id>
                  <entry in LDIF format>
                  <blank line>

## [](#KNOWN_LIMITATIONS)KNOWN LIMITATIONS

           The sock backend does not process extended operation results from
           an external program.

           If sockresps is configured, sock overlay does not consider sockops
           nor sockdnpat to decide which responses are passed onto the
           external program, instead, all responses are currently passed on.

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The sock backend does not honor all ACL semantics as described in
           slapd.access(5).  In general, access to objects is checked by
           using a dummy object that contains only the DN, so access rules
           that rely on the contents of the object are not honored.  In
           detail:

           The add operation does not require write (=w) access to the
           children pseudo-attribute of the parent entry.

           The bind operation requires auth (=x) access to the entry pseudo-
           attribute of the entry whose identity is being assessed; auth (=x)
           access to the credentials is not checked, but rather delegated to
           the underlying program.

           The compare operation requires compare (=c) access to the entry
           pseudo-attribute of the object whose value is being asserted;
           compare (=c) access to the attribute whose value is being asserted
           is not checked.

           The delete operation does not require write (=w) access to the
           children pseudo-attribute of the parent entry.

           The modify operation requires write (=w) access to the entry
           pseudo-attribute; write (=w) access to the specific attributes
           that are modified is not checked.

           The modrdn operation does not require write (=w) access to the
           children pseudo-attribute of the parent entry, nor to that of the
           new parent, if different; write (=w) access to the distinguished
           values of the naming attributes is not checked.

           The search operation does not require search (=s) access to the
           entry pseudo_attribute of the searchBase; search (=s) access to
           the attributes and values used in the filter is not checked.

           The extended operation does not require any access special rights.
           The external program has to implement any sort of access control.

## [](#EXAMPLE)EXAMPLE

           There is an example script in the slapd/back-sock/ directory in
           the OpenLDAP source tree.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd(8).

## [](#AUTHOR)AUTHOR

           Brian Candler, with enhancements by Howard Chu

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

    OpenLDAP LDVERSION             RELEASEDATE                  SLAPD-SOCK(5)

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
