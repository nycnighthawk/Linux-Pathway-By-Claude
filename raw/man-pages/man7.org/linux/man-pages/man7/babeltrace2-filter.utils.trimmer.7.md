---
{"title": "babeltrace2-filter.utils.trimmer(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-filter.utils.trimmer.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-filter.utils.trimmer(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INITIALIZATION PARAMETERS](#INITIALIZATION_PARAMETERS) \| [PORTS](#PORTS) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-FILTER()                                 BABELTRACE2-FILTER()

## [](#NAME)NAME

           babeltrace2-filter.utils.trimmer - Babeltrace 2: Trimmer filter
           component class

## [](#DESCRIPTION)DESCRIPTION

           A Babeltrace 2 filter.utils.trimmer message iterator discards all
           the consumed messages with a time less than a given beginning time
           and greater than a given end time. It effectively “cuts”, or trims
           trace streams.

                           +-------------------+
                           | flt.utils.trimmer |
                           |                   |
               Messages -->@ in            out @--> Less messages
                           +-------------------+

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

           A filter.utils.trimmer message iterator makes its upstream message
           iterator seek the configured beginning time (see the begin
           parameter) before it starts to consume messages. This seeking
           operation can have an effect on the times of stream beginning,
           packet beginning, discarded events, and discarded packets messages
           so that they fall within the configured trimming time range.

           As such, when a filter.utils.trimmer message iterator consumes a
           message of which the time is greater than the configured end time
           (see the end parameter), it can alter the time of stream end,
           packet end, discarded events, and discarded packets messages so
           that they fall within the configured trimming time range.

           A filter.utils.trimmer message iterator requires that all the
           upstream messages it consumes have times, except for stream
           beginning and end messages, returning an error status otherwise.

## [](#INITIALIZATION_PARAMETERS)INITIALIZATION PARAMETERS

           begin=TIME [optional string or signed integer]
               Set the beginning time of the trimming time range to TIME.

               If TIME is a string, see below for its format. If TIME is a
               signed integer, then the component converts it to a string and
               treats it as such.

               If you don’t specify this parameter, then the component
               discards no events until the end of the trimming time range.

               The format of TIME when it’s a string is one of:

                   YYYY-MM-DD HH:II[:SS[.NANO]]
                   HH:II[:SS[.NANO]]
                   [-]SEC[.NANO]

               YYYY
                   4-digit year.

               MM
                   2-digit month (January is 01).

               DD
                   2-digit day.

               HH
                   2-digit hour (24-hour format).

               II
                   2-digit minute.

               SS
                   2-digit second.

               NANO
                   Nanoseconds (up to nine digits).

               SEC
                   Seconds since origin.

               If TIME has no date information, then the message iterator
               uses the time of the first upstream message to determine the
               date.

           end=TIME [optional string or signed integer]
               Set the end time of the trimming time range to TIME.

               If TIME is a string, see the begin parameter for its format.
               If TIME is a signed integer, then the component converts it to
               a string and treats it as such.

               If you don’t specify this parameter, then the component
               discards no events from the beginning of the trimming time
               range.

           gmt=VAL [optional boolean]
               If VAL is true, then set the time zone of the begin and end
               parameters to GMT instead of the local time zone.

               Default: false.

## [](#PORTS)PORTS

               +-------------------+
               | flt.utils.trimmer |
               |                   |
               @ in            out @
               +-------------------+

       Input
           in
               Single input port.

       Output
           out
               Single output port.

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

           babeltrace2-intro(7), babeltrace2-plugin-utils(7)

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

                                                         BABELTRACE2-FILTER()

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-convert(1)](../man1/babeltrace2-convert.1.html),  [babeltrace2-plugin-utils(7)](../man7/babeltrace2-plugin-utils.7.html)

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
