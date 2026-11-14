---
{"title": "smtpd-tables(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/smtpd-tables.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# smtpd-tables(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [DESIGN](#DESIGN) \| [PROTOCOL](#PROTOCOL) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [HISTORY](#HISTORY) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SMTPD-TABLES(7)      Miscellaneous Information Manual     SMTPD-TABLES(7)

## [](#NAME)NAME

           smtpd-tables — table API for the smtpd daemon

## [](#DESCRIPTION)DESCRIPTION

           The smtpd(8) daemon provides a Simple Mail Transfer Protocol
           (SMTPD) implementation, which allows ordinary machines to become
           Mail eXchangers (MX).  Some features that are commonly used by MX,
           such as querying databases for user credentials, are outside of
           the scope of SMTP and too complex to fit in smtpd(8).

           Because an MX may need to provide these features, smtpd(8)
           provides an API to implement table(5) backends with a simple text-
           based protocol.

## [](#DESIGN)DESIGN

           smtpd-tables are programs that run as unique standalone processes,
           they do not share smtpd(8) address space.  They are executed by
           smtpd(8) at startup and expected to run in an infinite loop,
           reading events and queries from standard input and writing
           responses to standard output.  They are not allowed to terminate.

           Because smtpd-tables are standalone programs that communicate with
           smtpd(8), they may run as different users than smtpd(8) and may be
           written in any language.  smtpd-tables must not use blocking I/O,
           they must support answering asynchronously to smtpd(8).

## [](#PROTOCOL)PROTOCOL

           The protocol consist of human-readable lines exchanged between
           smtpd-tables and smtpd(8).

           The protocol begins with a handshake.  First, smtpd(8) provides
           smtpd-tables with general configuration information in the form of
           key-value lines, terminated by ‘config|ready’.  For example:

                 config|smtpd-version|7.8.0
                 config|protocol|0.1
                 config|tablename|devs
                 config|ready

           Then, smtpd-tables register the supported services, terminating
           with ‘register|ready’.  For example:

                 register|alias
                 register|credentials
                 register|ready

           Finally, smtpd(8) can start querying the table.  For example:

                 table|0.1|1713795082.354255|devs|lookup|alias|b72508d|op

           The “|” character is used to separate the fields and may only
           appear verbatim in the last field of the payload, in which case it
           should be considered a regular character and not a separator.  No
           other field may contain a “|”.

           Each request has a common set of fields, followed by some other
           fields that are operation-specific.  The common format consists of
           a protocol prefix ‘table’, the protocol version, the timestamp and
           the table name.  For example:

                 table|0.1|1713795091.202157|devs

           The protocol is inherently asynchronous, so multiple request may
           be sent without waiting for the table to reply.  All the replies
           have a common prefix, followed by the operation-specific response.
           The common format consist of a prefix with the operation name in
           followed by ‘-result’, and the unique ID of the request.  For
           example:

                 lookup-result|b72508d

           The list of operations, operation-specific parameters and
           responses are as follows:

           update id
                   Ask the table to reload its configuration.  The result is
                   either ‘ok’ on success or ‘error’ and a message upon a
                   failure to do so.

           check service id query
                   Check whether query is present in the table.  The result
                   is ‘found’ if found, ‘not-found’ if not, or ‘error’ and a
                   message upon an error.

           lookup service id query
                   Look up a value in the table for given the query.  The
                   result is ‘found’ and the value if found, ‘not-found’ if
                   not found, or ‘error’ and a message upon an error.

           fetch service id
                   Fetch the next item from the table, eventually wrapping
                   around.  It is only supported for the source and relayhost
                   services.  The result is ‘found’ and the value if found,
                   ‘not-found’ if the table is empty, or ‘error’ and a
                   message upon an error.

           Each service has a specific format for the result.  The exact
           syntax for the values and eventually the keys are described in
           table(5).  The services and their result format are as follows:

           alias        One or more aliases separated by a comma.
           auth         Only usable for check.  Lookup key is username and
                        cleartext password separated by ‘:’.
           domain       A domain name.
           credentials  The user name, followed by ‘:’ and the encrypted
                        password as per smtpctl(8) encrypt subcommand.
           netaddr      IPv4 and IPv6 address or netmask.
           userinfo     The user id, followed by ‘:’ then the group id, then
                        ‘:’ and finally the home directory.
           source       IPv4 and IPv6 address.
           mailaddr     An username, a domain or a full email address.
           addrname     Used to map IP addresses to hostnames.

## [](#EXAMPLES)EXAMPLES

           Assuming the table is called “devs”, here's an example of a failed
           update transaction:

                 table|0.1|1713795097.394049|devs|update|478ff0d2
                 update-result|478ff0d2|error|failed to connect to the database

           A check request for the netaddr service for the 192.168.0.7 IPv4
           address which is not in the table:

                 table|0.1|1713795103.314423|devs|check|netaddr|e5862859|192.168.0.7
                 check-result|e5862859|not-found

           A successful lookup request for the userinfo service for the user
           ‘op’:

                 table|0.1|1713795110.354921|devs|lookup|userinfo|f993c74|op
                 lookup-result|f993c74|found|1000:1000:/home/op

           A series of fetch requests for the source service that wraps
           around:

                 table|0.1|1713795116.227321|devs|fetch|source|189bd3ee
                 lookup-result|189bd3ee|found|192.168.1.7
                 table|0.1|1713795120.162438|devs|fetch|source|9e4c56d4
                 lookup-result|9e4c56d4|found|10.0.0.8
                 table|0.1|1713795122.930928|devs|fetch|source|f2c8b906
                 lookup-result|f2c8b906|found|192.168.1.7

## [](#SEE_ALSO)SEE ALSO

           smtpd(8)

## [](#HISTORY)HISTORY

           smtpd-tables first appeared in OpenBSD 7.6.

## [](#COLOPHON)COLOPHON

           This page is part of the OpenSMTPD (a FREE implementation of the
           server-side SMTP protocol) project.  Information about the project
           can be found at https://www.opensmtpd.org/.  If you have a bug
           report for this manual page, see
           ⟨https://github.com/OpenSMTPD/OpenSMTPD/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/OpenSMTPD/OpenSMTPD.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-03-26.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    GNU                          October 30, 2025             SMTPD-TABLES(7)

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
