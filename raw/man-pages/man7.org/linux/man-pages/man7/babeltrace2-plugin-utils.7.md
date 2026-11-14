---
{"title": "babeltrace2-plugin-utils(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-plugin-utils.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-plugin-utils(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [COMPONENT CLASSES](#COMPONENT_CLASSES) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-PLUGIN()                                 BABELTRACE2-PLUGIN()

## [](#NAME)NAME

           babeltrace2-plugin-utils - Babeltrace 2: Common graph utilities
           plugin

## [](#DESCRIPTION)DESCRIPTION

           The Babeltrace 2 utils plugin contains common, generic utility
           component classes which you can use in any processing graph.

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

## [](#COMPONENT_CLASSES)COMPONENT CLASSES

           filter.utils.muxer
               Muxes messages by time.

               See babeltrace2-filter.utils.muxer(7).

           filter.utils.trimmer
               Discards all the consumed messages with a time outside a given
               time range, effectively “cutting” trace streams.

               See babeltrace2-filter.utils.trimmer(7).

           sink.utils.counter
               Prints the number of consumed messages, either once at the end
               or periodically.

               See babeltrace2-sink.utils.counter(7).

           sink.utils.dummy
               Consumes messages and discards them (does nothing with them).

               This is useful for testing and benchmarking a trace processing
               graph application, for example.

               See babeltrace2-sink.utils.dummy(7).

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

           This plugin is part of the Babeltrace 2 project.

           Babeltrace is distributed under the MIT license (see
           <https://opensource.org/licenses/MIT>).

## [](#SEE_ALSO)SEE ALSO

           babeltrace2-intro(7), babeltrace2-filter.utils.muxer(7),
           babeltrace2-filter.utils.trimmer(7),
           babeltrace2-sink.utils.counter(7), babeltrace2-sink.utils.dummy(7)

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

                                                         BABELTRACE2-PLUGIN()

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-filter.utils.muxer(7)](../man7/babeltrace2-filter.utils.muxer.7.html),  [babeltrace2-filter.utils.trimmer(7)](../man7/babeltrace2-filter.utils.trimmer.7.html),  [babeltrace2-intro(7)](../man7/babeltrace2-intro.7.html),  [babeltrace2-sink.utils.counter(7)](../man7/babeltrace2-sink.utils.counter.7.html),  [babeltrace2-sink.utils.dummy(7)](../man7/babeltrace2-sink.utils.dummy.7.html)

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
