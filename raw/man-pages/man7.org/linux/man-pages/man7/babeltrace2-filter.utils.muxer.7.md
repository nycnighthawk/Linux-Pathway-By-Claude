---
{"title": "babeltrace2-filter.utils.muxer(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-filter.utils.muxer.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-filter.utils.muxer(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [PORTS](#PORTS) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-FILTER()                                 BABELTRACE2-FILTER()

## [](#NAME)NAME

           babeltrace2-filter.utils.muxer - Babeltrace 2: Message muxer
           filter component class

## [](#DESCRIPTION)DESCRIPTION

           A Babeltrace 2 filter.utils.muxer message iterator muxes the
           messages that it consumes from one or more upstream message
           iterators into a linear sequence of messages ordered by time.

                           +-----------------+
                           | flt.utils.muxer |
                           |                 |
               Messages -->@ in0         out @--> Sorted messages
               Messages -->@ in1             |
               Messages -->@ in2             |
                           @ in3             |
                           +-----------------+

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

           A filter.utils.muxer message iterator doesn’t alter the messages
           it consumes: it only sorts them.

           The message iterator creates one upstream message iterator per
           connected input port.

               Note

               To support muxing messages with different default clock
               classes, the message iterator converts the message times to
               nanoseconds from the common origin (Unix epoch, for example).
               This means that the resulting message sequence could be
               incorrect if one or more clock classes have a frequency which
               is greater than 1 GHz.

## [](#PORTS)PORTS

               +-----------------+
               | flt.utils.muxer |
               |                 |
               @ in0         out @
               @ ...             |
               +-----------------+

       Input
           inN, where N is a decimal integer starting at 0
               Input port on which a filter.utils.muxer message iterator
               creates an upstream message iterator to consumes messages
               from.

               When the component is initialized, its only input port is in0.
               When you connect the in0 port, the component creates the in1
               input port, and so on.

               In other words, a filter.utils.muxer component always has an
               available input port.

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
