---
{"title": "babeltrace2-source.ctf.lttng-live(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-source.ctf.lttng-live.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-source.ctf.lttng-live(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INITIALIZATION PARAMETERS](#INITIALIZATION_PARAMETERS) \| [PORTS](#PORTS) \| [QUERY OBJECTS](#QUERY_OBJECTS) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-SOURCE()                                 BABELTRACE2-SOURCE()

## [](#NAME)NAME

           babeltrace2-source.ctf.lttng-live - Babeltrace 2: LTTng live
           source component class

## [](#DESCRIPTION)DESCRIPTION

           A Babeltrace 2 source.ctf.lttng-live message iterator connects to
           a local or remote LTTng (see <https://lttng.org/>) relay daemon,
           receives the streams of a specific tracing session, and emits
           corresponding messages.

               CTF streams over
               LTTng live (TCP)
                 |
                 |   +--------------------+
                 |   | src.ctf.lttng-live |
                 '-->|                    |
                     |                out @--> Sorted messages of one
                     +--------------------+    or more streams

           More information about LTTng live is available in the LTTng
           Documentation (see <https://lttng.org/docs/#doc-lttng-live>).

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

           A source.ctf.lttng-live component has a single output port: its
           message iterator muxes (sorts) the messages from the various CTF
           data streams internally.

           A source.ctf.lttng-live message iterator handles the messages of
           one, and only one LTTng tracing session. A single LTTng tracing
           session can contain one or more traces, depending on the active
           tracing domains and the configured user space buffering scheme.

           The component connects to an LTTng relay daemon using the inputs
           parameter. This is an array of exactly one string which is the URL
           of the LTTng relay daemon to connect to.

           By default, if the remote tracing session name doesn’t exist, then
           the message iterator returns "try again later". This default mode
           makes the message iterator never end: even if the remote tracing
           session is destroyed, the message iterator keeps on waiting for a
           tracing session with the same name to exist. You can change this
           behaviour with the session-not-found-action initialization
           parameter.

               Note

               As of this version, you can only create one message iterator
               per source.ctf.lttng-live component. This is because the LTTng
               live protocol accepts at most one client per tracing session
               per LTTng relay daemon.

           As of this version, a source.ctf.lttng-live component can connect
           to an LTTng relay daemon using the LTTng 2.4 or LTTng 2.15
           protocol. The latter is required for CTF 2 (see
           <https://diamon.org/ctf/>) support.

           The "get supported MIP versions" method of source.ctf.lttng-live
           always reports to support MIP versions 0 and 1. If you attempt to
           make a source.ctf.lttng-live component read a CTF 2 recording
           session within a trace processing graph configured with MIP 0,
           then the message iterator will fail at initialization or "next"
           method call time.

## [](#INITIALIZATION_PARAMETERS)INITIALIZATION PARAMETERS

           inputs=URL [array of one string]
               Use URL to connect to the LTTng relay daemon.

               URL is an array of exactly one string of which the format is:

                   net[4]://RDHOST[:RDPORT]/host/TGTHOST/SESSION

               RDHOST
                   Host name or IP address of the LTTng relay daemon.

               RDPORT
                   Listening port of the LTTng relay daemon.

                   If not specified, then the component uses the default port
                   (5344).

               TGTHOST
                   Target host name or IP address.

               SESSION
                   Name of the LTTng tracing session from which to receive
                   data.

           session-not-found-action=(continue | fail | end) [optional string]
               When the message iterator doesn’t find the specified remote
               tracing session (SESSION part of the inputs parameter), do one
               of:

               continue (default)
                   Keep on trying, returning "try again later" to the
                   downstream user until the tracing session exists.

                   With this action, the message iterator never ends, as the
                   LTTng live protocol cannot currently indicate that a
                   tracing session will never exist.

               fail
                   Fail.

               end
                   End.

## [](#PORTS)PORTS

               +--------------------+
               | src.ctf.lttng-live |
               |                    |
               |                out @
               +--------------------+

       Output
           out
               Single output port.

## [](#QUERY_OBJECTS)QUERY OBJECTS

       babeltrace.support-info
           See babeltrace2-query-babeltrace.support-info(7) to learn more
           about this query object.

           For a string input which honors the LTTng live URL format (see the
           inputs parameter), the result object is 0.75.

       sessions
           You can query the sessions object to get a list of available LTTng
           tracing sessions for a given LTTng relay daemon URL.

           Parameters:

           url=URL [string]
               Use URL to connect to the LTTng relay daemon.

               The format of URL is:

                   net[4]://RDHOST[:RDPORT]

               RDHOST
                   Host name or IP address of the LTTng relay daemon.

               RDPORT
                   Listening port of the LTTng relay daemon.

                   If not specified, then the query operation uses the
                   default port (5344).

           Result object (array of maps, one element for each available
           tracing session):

           client-count [unsigned integer]
               Current number of LTTng live clients connected to the relay
               daemon to receive data from this tracing session.

           session-name [string]
               Tracing session name.

           stream-count [unsigned integer]
               Current number of CTF streams in this tracing sessions,
               including the metadata streams.

           target-hostname [string]
               Hostname of the tracing session.

               This isn’t necessarily the hostname of the relay daemon.

           timer-us [unsigned integer]
               Configured period (µs) of the live timer of the tracing
               session (see lttng-create(1)).

           trace-format [string]
               Format of the trace(s) of the tracing session amongst:

               ctf-1.8
                   CTF 1.8 (see <https://diamon.org/ctf/v1.8.3/>)

               ctf-2.0
                   CTF 2 (see <https://diamon.org/ctf/>)

           url [string]
               URL to use as the first element of the inputs parameter to
               connect to the same LTTng relay daemon and receive data from
               this tracing session.

## [](#BUGS)BUGS

           If you encounter any issue or usability problem, please report it
           on the Babeltrace bug tracker (see
           <https://bugs.lttng.org/projects/babeltrace>).

## [](#RESOURCES)RESOURCES

           The Babeltrace project shares some communication channels with the
           LTTng project (see <https://lttng.org/>).

           •   Babeltrace website (see <https://babeltrace.org/>)

           •   Mailing list (see <https://lists.lttng.org>) for support and
               development: lttng-dev@lists.lttng.org

           •   IRC channel (see <irc://irc.oftc.net/lttng>): #lttng on
               irc.oftc.net

           •   Bug tracker (see <https://bugs.lttng.org/projects/babeltrace>)

           •   Git repository (see
               <https://git.efficios.com/?p=babeltrace.git>)

           •   GitHub project (see <https://github.com/efficios/babeltrace>)

           •   Continuous integration (see
               <https://ci.lttng.org/view/Babeltrace/>)

           •   Code review (see
               <https://review.lttng.org/q/project:babeltrace>)

## [](#AUTHORS)AUTHORS

           The Babeltrace 2 project is the result of hard work by many
           regular developers and occasional contributors.

           The current project maintainer is Jérémie Galarneau
           <mailto:jeremie.galarneau@efficios.com>.

## [](#COPYRIGHT)COPYRIGHT

           This component class is part of the Babeltrace 2 project.

           Babeltrace is distributed under the MIT license (see
           <https://opensource.org/licenses/MIT>).

## [](#SEE_ALSO)SEE ALSO

           babeltrace2-intro(7), babeltrace2-plugin-ctf(7), lttng-relayd(8),
           lttng-create(1)

## [](#COLOPHON)COLOPHON

           This page is part of the babeltrace (trace read and write
           libraries and a trace converter) project.  Information about the
           project can be found at ⟨http://www.efficios.com/babeltrace⟩.  If
           you have a bug report for this manual page, send it to
           lttng-dev@lists.lttng.org.  This page was obtained from the
           project's upstream Git repository
           ⟨git://git.efficios.com/babeltrace.git⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-17.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                         BABELTRACE2-SOURCE()

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-convert(1)](../man1/babeltrace2-convert.1.html),  [babeltrace2-plugin-ctf(7)](../man7/babeltrace2-plugin-ctf.7.html)

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
