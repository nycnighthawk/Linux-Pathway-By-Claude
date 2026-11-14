---
{"title": "smtpd-filters(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/smtpd-filters.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# smtpd-filters(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [DESIGN](#DESIGN) \| [REPORT AND FILTER](#REPORT_AND_FILTER) \| [PROTOCOL](#PROTOCOL) \| [CONFIGURATION](#CONFIGURATION) \| [REPORT EVENTS](#REPORT_EVENTS) \| [FILTER REQUESTS](#FILTER_REQUESTS) \| [SEE ALSO](#SEE_ALSO) \| [HISTORY](#HISTORY) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SMTPD-FILTERS(7)     Miscellaneous Information Manual    SMTPD-FILTERS(7)

## [](#NAME)NAME

           smtpd-filters — filtering API for the smtpd daemon

## [](#DESCRIPTION)DESCRIPTION

           The smtpd(8) daemon provides a Simple Mail Transfer Protocol
           (SMTP) implementation, which allows ordinary machines to become
           Mail eXchangers (MX).  Some features that are commonly used by MX,
           such as delivery reporting or spam filtering, are outside the
           scope of SMTP and too complex to fit in smtpd(8).

           Because an MX may need to provide these features, smtpd(8)
           provides an API to extend its behavior through smtpd-filters.

           At runtime, smtpd(8) can report events to smtpd-filters, querying
           what it should answer to these events.  This allows the decision
           logic to rely on third-party programs.

## [](#DESIGN)DESIGN

           smtpd-filters are programs that run as unique standalone
           processes, they do not share smtpd(8) memory space.  They are
           executed by smtpd(8) at startup and expected to run in an infinite
           loop, reading events and filtering requests from stdin(4), writing
           responses to stdout(4) and logging to stderr(4).  They are not
           allowed to terminate.

           Because smtpd-filters are standalone programs that communicate
           with smtpd(8) through fd(4), they may run as different users than
           smtpd(8) and may be written in any language.  smtpd-filters must
           not use blocking I/O, they must support answering asynchronously
           to smtpd(8).

## [](#REPORT_AND_FILTER)REPORT AND FILTER

           The API relies on two streams, report and filter.

           The report stream is a one-way stream which allows smtpd(8) to
           inform smtpd-filters in real-time about events.  Report events do
           not expect an answer from smtpd-filters; they are just meant to
           provide information.  A filter should be able to replicate the
           smtpd(8) state for a session by gathering information coming from
           report events.  No decision is ever taken by the report stream.

           The filter stream is a two-way stream which allows smtpd(8) to
           query smtpd-filters about what it should do with a session at a
           given phase.  Filter requests expect an answer from smtpd-filters;
           smtpd(8) will not let the session move forward until then.  A
           decision must always be taken by the filter stream.

           It is sometimes possible to rely on filter requests to gather
           information, but because a response is expected by smtpd(8), this
           is more costly than using report events.  The correct pattern for
           writing filters is to use report events to create a local state
           for a session, then use filter requests to take decisions based on
           this state.  The only case when using filter requests instead of
           report events is correct is when a decision is required for the
           filter request and there is no need for more information than that
           of the event itself.

## [](#PROTOCOL)PROTOCOL

           The protocol consists of human-readable lines exchanged between
           smtpd-filters and smtpd(8), through fd(4).

           The protocol begins with a handshake.  First, smtpd(8) provides
           smtpd-filters with general configuration information in the form
           of key-value lines:

                 config|smtpd-version|7.8.0
                 config|protocol|0.7
                 config|smtp-session-timeout|300
                 config|subsystem|smtp-in
                 config|ready

           Then, smtpd-filters register the stream, subsystem and event they
           want to handle:

                 register|report|smtp-in|link-connect
                 register|ready

           Finally, smtpd(8) emits report events and filter requests,
           expecting smtpd-filters to respond or not depending on the stream:

                 report|0.7|1576146008.006099|smtp-in|link-connect|7641df9771b4ed00|mail.openbsd.org|pass|199.185.178.25:33174|45.77.67.80:25
                 report|0.7|1576147242.200225|smtp-in|link-connect|7641dfb3798eb5bf|mail.openbsd.org|pass|199.185.178.25:31205|45.77.67.80:25
                 report|0.7|1576148447.982572|smtp-in|link-connect|7641dfc063102cbd|mail.openbsd.org|pass|199.185.178.25:24786|45.77.67.80:25

           The character “|” may only appear in the last field of a payload,
           in which case it should be considered a regular character and not
           a separator.  No other field may contain a “|”.

           The list of subsystems and events, as well as the format of
           requests and responses, are documented in the sections below.

## [](#CONFIGURATION)CONFIGURATION

           During the initial handshake, smtpd(8) emits a series of
           configuration keys and values.  The list is meant to be ignored by
           smtpd-filters that do not require it and consumed gracefully by
           filters that do.

           There are currently three keys:

                 config|smtpd-version|7.8.0
                 config|protocol|0.7
                 config|smtp-session-timeout|300
                 config|subsystem|smtp-in

           When smtpd(8) has sent all configuration keys, it emits the
           following line:

                 config|ready

## [](#REPORT_EVENTS)REPORT EVENTS

           There is currently only one subsystem supported in the API: smtp-
           in.

           Each report event is generated by smtpd(8) as a single line
           similar to the one below:

                 report|0.7|1576146008.006099|smtp-in|link-connect|7641df9771b4ed00|mail.openbsd.org|pass|199.185.178.25:33174|45.77.67.80:25

           The format consists of a protocol prefix containing the stream,
           the protocol version, the timestamp, the subsystem, the event and
           the unique session identifier, separated by “|”:

                 report|0.7|1576146008.006099|smtp-in|link-connect|7641df9771b4ed00

           It is followed by a suffix containing the event-specific
           parameters, also separated by “|”:

                 mail.openbsd.org|pass|199.185.178.25:33174|45.77.67.80:25

           The list of events and event-specific parameters for smtp-in are
           as follows:

           link-connect: rdns fcrdns src dest
                   This event is generated upon connection.

                   rdns contains the reverse DNS hostname for the remote end
                   or an empty string if none.

                   fcrdns contains the string “pass” or “fail” depending on
                   if the remote end validates FCrDNS.

                   src contains either the IP address and port of the source
                   address, in the format “address:port”, or the path to a
                   UNIX socket in the format “unix:/path”.

                   dest holds either the IP address and port of the
                   destination address, in the format “address:port”, or the
                   path to a UNIX socket in the format “unix:/path”.

           link-greeting: hostname
                   This event is generated upon display of the server banner.

                   hostname contains the hostname displayed in the banner.

           link-identify: method identity
                   This event is generated upon “HELO” or “EHLO” command from
                   the client.

                   method contains the string “HELO” or “EHLO” indicating the
                   method used by the client.

                   identity contains the identity provided by the client.

           link-tls: tls-string
                   This event is generated upon successful negotiation of
                   TLS.

                   tls-string contains a colon-separated list of TLS
                   properties including the TLS version, the cipher suite
                   used by the session and the cipher strength in bits.

           link-disconnect
                   This event is generated upon disconnection of the client.

           link-auth: result username
                   This event is generated upon an authentication attempt by
                   the client.

                   result contains the string “pass”, “fail” or “error”
                   depending on the result of the authentication attempt.

                   username contains the username used for the authentication
                   attempt.

           tx-reset: [message-id]
                   This event is generated when a transaction is reset.

                   If reset took place during a transaction, message-id
                   contains the identifier of the transaction being reset.

           tx-begin: message-id
                   This event is generated when a transaction is initiated.

                   message-id contains the identifier for the transaction.

           tx-mail: message-id result address
                   This event is generated when client emits “MAIL FROM”.

                   message-id contains the identifier for the transaction.

                   result contains “ok” if the sender was accepted,
                   “permfail” if it was rejected or “tempfail” if it was
                   rejected for a transient error.

                   address contains the e-mail address of the sender.  The
                   address is normalized and sanitized, the characters “<”
                   and “>” are removed, along with any parameters to “MAIL
                   FROM”.

           tx-rcpt: message-id result address
                   This event is generated when client emits “RCPT TO”.

                   message-id contains the identifier for the transaction.

                   result contains “ok” if the recipient was accepted,
                   “permfail” if it was rejected or “tempfail” if it was
                   rejected for a transient error.

                   address contains the e-mail address of the recipient.  The
                   address is normalized and sanitized, the characters “<”
                   and “>” are removed, along with any parameters to “RCPT
                   TO”.

           tx-envelope: message-id envelope-id
                   This event is generated when an envelope is accepted.

                   envelope-id contains the unique identifier for the
                   envelope.

           tx-data: message-id result
                   This event is generated when client has emitted “DATA”.

                   message-id contains the unique identifier for the
                   transaction.

                   result contains “ok” if server accepted the message for
                   processing, “permfail” if it has not been accepted and
                   “tempfail” if a transient error prevented message
                   processing.

           tx-commit: message-id message-size
                   This event is generated when a transaction has been
                   accepted by the server.

                   message-id contains the unique identifier for the SMTP
                   transaction.

                   message-size contains the size of the message submitted in
                   the “DATA” phase of the SMTP transaction.

           tx-rollback: message-id
                   This event is generated when a transaction has been
                   rejected by the server.

                   message-id contains the unique identifier for the SMTP
                   transaction.

           protocol-client: command
                   This event is generated for every command submitted by the
                   client.  It contains the raw command as received by the
                   server.

                   command contains the command emitted by the client to the
                   server.

           protocol-server: response
                   This event is generated for every response emitted by the
                   server.  It contains the raw response as emitted by the
                   server.

                   response contains the response emitted by the server to
                   the client.

           filter-report: filter-kind name message
                   This event is generated when a filter emits a report.

                   filter-kind may be either “builtin” or “proc” depending on
                   if the filter is an smtpd(8) builtin filter or a proc
                   filter implementing the API.

                   name is the name of the filter that generated the report.

                   message is a filter-specific message.

           filter-response: phase response [param]
                   This event is generated when a filter responds to a
                   filtering request.

                   phase contains the phase name for the request.  The phases
                   are documented in the next section.

                   response contains the response of the filter to the
                   request, it is either one of “proceed”, “report”,
                   “reject”, “disconnect”, “junk” or “rewrite”.

                   If specified, param is the parameter to the response.

           timeout
                   This event is generated when a timeout happens for a
                   session.

## [](#FILTER_REQUESTS)FILTER REQUESTS

           There is currently only one subsystem supported in the API: smtp-
           in.

           Filter requests allow smtpd(8) to query smtpd-filters about what
           to do with a session at a particular phase.  In addition, they
           allow smtpd-filters to alter the content of a message by adding,
           modifying, or suppressing lines of input in a way that is similar
           to what program like sed(1) or grep(1) would do.

           Each filter request is generated by smtpd(8) as a single line
           similar to the one below.  Fields are separated by the “|”
           character.

                 filter|0.7|1576146008.006099|smtp-in|connect|7641df9771b4ed00|1ef1c203cc576e5d|mail.openbsd.org|199.185.178.25

           The format consists of a protocol prefix containing the stream,
           the protocol version, the timestamp, the subsystem, the filtering
           phase, the unique session identifier and an opaque token that the
           filter should provide in its response:

                 filter|0.7|1576146008.006099|smtp-in|connect|7641df9771b4ed00|1ef1c203cc576e5d

           It is followed by a suffix containing the phase-specific
           parameters of the filter request, also separated by “|”:

                 mail.openbsd.org|199.185.178.25

           Unlike with report events, smtpd(8) expects answers from filter
           requests and will not allow a session to move forward until the
           filter has instructed smtpd(8) how to treat it.

           For all phases except “data-line”, responses must follow the same
           construct: a message of type “filter-result”, followed by the
           unique session id, the opaque token, a decision and optional
           decision-specific parameters:

                 filter-result|7641df9771b4ed00|1ef1c203cc576e5d|proceed
                 filter-result|7641df9771b4ed00|1ef1c203cc576e5d|reject|550 nope

           The possible decisions for a “filter-result” message are
           documented below.

           For the “data-line” phase, smtpd-filters are fed a stream of lines
           corresponding to the message to filter, terminated by a single
           dot:

                 filter|0.7|1576146008.006099|smtp-in|data-line|7641df9771b4ed00|1ef1c203cc576e5d|line 1
                 filter|0.7|1576146008.006103|smtp-in|data-line|7641df9771b4ed00|1ef1c203cc576e5d|line 2
                 filter|0.7|1576146008.006105|smtp-in|data-line|7641df9771b4ed00|1ef1c203cc576e5d|.

           They are expected to return an output stream similarly terminated
           by a single dot.  A filter may add to, suppress, modify or echo
           back the lines it receives.  Ultimately, smtpd(8) assumes that the
           message consists of the output from smtpd-filters.

           Note that filters may be chained, and the lines that are input
           into a subsequent filter are the lines that are output from a
           previous filter.

           The response to “data-line” requests use their own construct.  A
           “filter-dataline” prefix, followed by the unique session
           identifier, the opaque token and the output line as follows:

                 filter-dataline|7641df9771b4ed00|1ef1c203cc576e5d|line 1
                 filter-dataline|7641df9771b4ed00|1ef1c203cc576e5d|line 2
                 filter-dataline|7641df9771b4ed00|1ef1c203cc576e5d|.

           The list of events and event-specific parameters for smtp-in are
           as follows:

           connect: rdns src
                   This request is emitted after connection, before the
                   banner is displayed.

                   src contains either the IP address of the source (a.b.c.d
                   for IPv4 or [x:x:x:x:x:x:x:x] IPv6) or “local” (for UNIX
                   sockets).

           helo: identity
                   This request is emitted after the client has emitted
                   “HELO”.

           ehlo: identity
                   This request is emitted after the client has emitted
                   “EHLO”.

           starttls: tls-string
                   This request is emitted after the client has requested
                   “STARTTLS”.

           auth: auth
                   This request is emitted after the client has requested
                   “AUTH”.

           mail-from: address
                   This request is emitted after the client has requested
                   “MAIL FROM”.

           rcpt-to: address
                   This request is emitted after the client has requested
                   “RCPT TO”.

           data    This request is emitted after the client has requested
                   “DATA”.

           data-line: line
                   This request is emitted for each line of input in the
                   “DATA” phase.  The lines are raw dot-escaped SMTP DATA
                   input, terminated with a single dot.

           commit  This request is emitted after the final single dot is
                   received.

           For every filtering phase, excepted “data-line”, the following
           decisions may be taken by a filter:

           proceed
                   No action is taken, session or transaction may be passed
                   to the next filter.

           junk    The session or transaction is marked as spam.  smtpd(8)
                   will prepend an “X-Spam” header to the message.

           reject error
                   The command is rejected with the message error.  The
                   message must be a valid SMTP message including status
                   code, 5xx or 4xx.

                   Messages starting with a 5xx status result in a permanent
                   failure, those starting with a 4xx status result in a
                   temporary failure.

                   Messages starting with a 421 status will result in a
                   client disconnect.

           disconnect error
                   The client is disconnected with the message error.  The
                   message must be a valid SMTP message including status
                   code, 5xx or 4xx.

                   Messages starting with a 5xx status result in a permanent
                   failure, those starting with a 4xx status result in a
                   temporary failure.

           rewrite parameter
                   The command parameter is rewritten.

                   This decision allows a filter to perform a rewrite of
                   client-submitted commands before they are processed by the
                   SMTP engine.  parameter is expected to be a valid SMTP
                   parameter for the command.

           report parameter
                   Generates a report with parameter for this filter.

## [](#SEE_ALSO)SEE ALSO

           smtpd(8)

## [](#HISTORY)HISTORY

           smtpd-filters first appeared in OpenBSD 6.6.

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

    GNU                          October 30, 2025            SMTPD-FILTERS(7)

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
