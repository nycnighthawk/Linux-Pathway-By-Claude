---
{"title": "babeltrace2-query-babeltrace.trace-infos(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-query-babeltrace.trace-infos.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-query-babeltrace.trace-infos(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [PARAMETERS](#PARAMETERS) \| [RESULT OBJECT](#RESULT_OBJECT) \| [EXAMPLES](#EXAMPLES) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-QUERY-(7)      Babeltrace 2 manual      BABELTRACE2-QUERY-(7)

## [](#NAME)NAME

           babeltrace2-query-babeltrace.trace-infos - Babeltrace 2: Trace
           infos query object

## [](#DESCRIPTION)DESCRIPTION

           The babeltrace.trace-infos Babeltrace 2 query object indicates
           time range information about specific traces and their streams,
           and which output ports of an eventual source component will serve
           the messages for a given stream.

           The babeltrace2-convert(1) command queries this object from all
           the source component classes to support the --stream-intersection
           feature.

## [](#PARAMETERS)PARAMETERS

           The parameters for this query operation are exactly the same as
           you would pass as the initialization parameters of a component
           created from the queried component class.

## [](#RESULT_OBJECT)RESULT OBJECT

           The result object is an array of trace info maps (see “Trace info
           map”).

       Trace info map
           A trace info map contains:

           stream-infos=STREAM-INFOS [array of stream info maps]
               Stream info maps (see “Stream info map”) for this trace.

       Stream info map
           A stream info map contains:

           range-ns=RANGE [range map]
               The time range of this stream, a map containing:

               begin=NS [signed integer]
                   Beginning time of this stream (nanoseconds since the
                   origin of the default clock class of the stream class).

               end=NS [signed integer]
                   End time of this stream (nanoseconds since the origin of
                   the default clock class of the stream class).

           port-name=PORT-NAME [string]
               For an eventual source component initialized with the same
               parameters: name of the output port which serves the messages
               of this stream.

## [](#EXAMPLES)EXAMPLES

       Result object
           Example 1. Two trace infos: one with three stream infos, one with
           two stream infos.

               - stream-infos:
                 - range-ns:
                     begin: 1509556764975082000
                     end: 1509557102181554400
                   port-name: trace0-cpu0
                 - range-ns:
                     begin: 1509556764947050800
                     end: 1509557102182771000
                   port-name: trace0-cpu1
                 - range-ns:
                     begin: 1509556764956409300
                     end: 1509557102182770400
                   port-name: trace0-cpu2
               - stream-infos:
                 - range-ns:
                     begin: 1509556764918082000
                     end: 1509557103849928400
                   port-name: trace1-cpu0
                 - range-ns:
                     begin: 1509556761888820000
                     end: 1509557109928100400
                   port-name: trace1-cpu1

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

           This query object is part of the Babeltrace 2 project.

           Babeltrace is distributed under the MIT license (see
           <https://opensource.org/licenses/MIT>).

## [](#SEE_ALSO)SEE ALSO

           babeltrace2-intro(7), babeltrace2-query(1), babeltrace2-convert(1)

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

    Babeltrace 2.2.0rc1         14 September 2019       BABELTRACE2-QUERY-(7)

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2-convert(1)](../man1/babeltrace2-convert.1.html),  [babeltrace2-source.ctf.fs(7)](../man7/babeltrace2-source.ctf.fs.7.html)

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
