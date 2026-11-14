---
{"title": "babeltrace2-source.text.dmesg(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-source.text.dmesg.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-source.text.dmesg(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INITIALIZATION PARAMETERS](#INITIALIZATION_PARAMETERS) \| [PORTS](#PORTS) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-SOURCE()                                 BABELTRACE2-SOURCE()

## [](#NAME)NAME

           babeltrace2-source.text.dmesg - Babeltrace 2: Linux kernel ring
           buffer source component class

## [](#DESCRIPTION)DESCRIPTION

           A Babeltrace 2 source.text.dmesg message iterator reads the lines
           of a Linux kernel ring buffer, as printed by the dmesg(1) tool,
           and emits corresponding event messages.

               Linux kernel ring buffer
               lines (file or standard input)
                 |
                 |   +----------------+
                 |   | src.text.dmesg |
                 '-->|                |
                     |            out @--> Messages (single stream)
                     +----------------+

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

           A source.text.dmesg message iterator names the events it creates
           string. Each event contain a single payload string field named str
           which contains the corresponding ring buffer line.

           By default, a source.text.dmesg message iterator reads the lines
           of the standard input stream. You can make the message iterator
           read the lines of a text file instead with the path parameter.

           By default, the message iterator tries to extract the timestamps
           of the kernel ring buffer lines and use them as the timestamps of
           the created events. A typical dmesg(1) line looks like this:

               [87166.510937] PM: Finishing wakeup.

           The [87166.510937] part is the timestamp to extract. When this
           information is available, the component creates a clock class
           which does NOT have the Unix epoch as its origin.

           You can make the message iterator not extract timestamps from
           lines with the no-extract-timestamp parameter.

               Note

               It’s possible that the output of dmesg(1) contains unsorted
               lines, that is, their timestamps go back in time. You can see
               this with the --show-delta option of dmesg(1): some time
               differences can be negative.

               This is due to a 2019 change (see
               <https://lwn.net/Articles/780556/>) to the API of the kernel
               ring buffer.

               As of this version, a source.text.dmesg message iterator
               requires that the input kernel ring buffer lines be sorted by
               timestamp (when they have timestamps), failing otherwise.

## [](#INITIALIZATION_PARAMETERS)INITIALIZATION PARAMETERS

           no-extract-timestamp=VAL [optional boolean]
               If VAL is true, then do NOT extract timestamps from the kernel
               ring buffer lines: set the str payload field of the created
               event to the whole line, including any timestamp prefix.

               Default: false.

           path=PATH [optional string]
               Read the kernel ring buffer lines from the file PATH instead
               of the standard input stream.

## [](#PORTS)PORTS

               +----------------+
               | src.text.dmesg |
               |                |
               |            out @
               +----------------+

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

           babeltrace2-plugin-text(7), babeltrace2-intro(7)

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

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-plugin-text(7)](../man7/babeltrace2-plugin-text.7.html)

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
