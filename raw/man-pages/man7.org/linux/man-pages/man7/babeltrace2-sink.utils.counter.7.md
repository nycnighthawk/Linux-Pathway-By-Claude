---
{"title": "babeltrace2-sink.utils.counter(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-sink.utils.counter.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-sink.utils.counter(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INITIALIZATION PARAMETERS](#INITIALIZATION_PARAMETERS) \| [PORTS](#PORTS) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-SINK.(7)       Babeltrace 2 manual       BABELTRACE2-SINK.(7)

## [](#NAME)NAME

           babeltrace2-sink.utils.counter - Babeltrace 2: Message counter
           sink component class

## [](#DESCRIPTION)DESCRIPTION

           A Babeltrace 2 sink.utils.counter component prints to the standard
           output the number of messages it consumes with a count for each
           type.

                           +--------------------+
                           | sink.utils.counter |
                           |                    +--> Statistics to the
               Messages -->@ in                 |    standard output
                           +--------------------+

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

           The output of the component looks like this:

                       3842964 Event messages
                             4 Stream beginning messages
                             1 Stream end messages
                            18 Packet beginning messages
                            14 Packet end messages
                           189 Discarded event messages
                             0 Discarded packet messages
                             3 Message iterator inactivity messages
                       3843000 messages (TOTAL)

           By default, a sink.utils.counter component prints a new block of
           statistics every 1000 consumed messages, whatever their types. You
           can use the step parameter to override this default period.

           The component always prints a block of statistics when there’s no
           more messages to consume from its upstream message iterator and
           the last block was different.

           By default, a sink.utils.counter component prints the count of
           messages for each type, even if this count is 0. You can make it
           hide the zero counts with the hide-zero parameter.

## [](#INITIALIZATION_PARAMETERS)INITIALIZATION PARAMETERS

           hide-zero=VAL [optional boolean]
               If VAL is true, then don’t print the statistics lines where
               the count is zero.

               Default: false.

           step=STEP [optional unsigned integer]
               Print a new block of statistics every STEP consumed messages
               instead of 1000.

               If STEP is 0, then the component only prints statistics when
               there’s no more messages to consume.

## [](#PORTS)PORTS

               +--------------------+
               | sink.utils.counter |
               |                    |
               @ in                 |
               +--------------------+

       Input
           in
               Single input port.

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

    Babeltrace 2.2.0rc1          1 September 2023        BABELTRACE2-SINK.(7)

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-plugin-utils(7)](../man7/babeltrace2-plugin-utils.7.html)

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
