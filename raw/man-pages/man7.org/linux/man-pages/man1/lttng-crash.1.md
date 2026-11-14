---
{"title": "lttng-crash(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-crash.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-crash(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-CRASH(1)                 LTTng Manual                LTTNG-CRASH(1)

## [](#NAME)NAME

           lttng-crash - Recover and read LTTng trace buffers in the event of
           a crash

## [](#SYNOPSIS)SYNOPSIS

           lttng-crash [--extract=DIR | --viewer=READER] [-verbose]... SHMDIR

## [](#DESCRIPTION)DESCRIPTION

           The Linux Trace Toolkit: next generation <https://lttng.org/> is
           an open-source software package used for correlated tracing of the
           Linux kernel, user applications, and user libraries.

           LTTng consists of Linux kernel modules (for Linux kernel tracing)
           and dynamically loaded libraries (for user application and library
           tracing).

           The lttng-crash command-line tool recovers LTTng trace buffers in
           the event of a system crash.

           lttng-crash reads files within the directory SHMDIR and does one
           of:

           Without the --extract option
               Launches a trace reader (see the --viewer option) to view the
               recovered traces.

           With the --extract=DIR option
               Extracts the files as uncorrupted LTTng traces to the DIR
               directory.

           SHMDIR is the directory specified as the argument of the --shm-
           path option of the lttng-create(1) command used to create the
           recording session for which to recover the traces.

## [](#OPTIONS)OPTIONS

           -x DIR, --extract=DIR
               Extract recovered traces to the directory DIR; do NOT execute
               any trace reader.

           -v, --verbose
               Increase verbosity.

               Specify this option up to three times to get more levels of
               verbosity.

           -e READER, --viewer=READER
               Use the trace reader READER to read the trace buffers.

               READER is the absolute path to the reader command to use, and
               it can contain command arguments as well.  lttng-crash passes
               the trace directory paths to the READER command as its last
               arguments.

               Without this option, lttng crash uses babeltrace2(1) if it’s
               available. Otherwise, it tries to use babeltrace(1).

       Program information
           -h, --help
               Show help.

               This option attempts to launch /usr/bin/man to view this
               manual page. Override the manual pager path with the
               LTTNG_MAN_BIN_PATH environment variable.

           --list-options
               List available command options and quit.

           -V, --version
               Show version and quit.

## [](#EXIT_STATUS)EXIT STATUS

           0
               Success

           1
               Error

           3
               Fatal error

## [](#RESOURCES)RESOURCES

           •   LTTng project website <https://lttng.org>

           •   LTTng documentation <https://lttng.org/docs>

           •   LTTng bug tracker <https://bugs.lttng.org>

           •   Git repositories <https://git.lttng.org>

           •   GitHub organization <https://github.com/lttng>

           •   Continuous integration <https://ci.lttng.org/>

           •   Mailing list <https://lists.lttng.org/> for support and
               development: lttng-dev@lists.lttng.org

           •   IRC channel <irc://irc.oftc.net/lttng>: #lttng on irc.oftc.net

           •   Mastodon <https://mastodon.social/@lttng>

## [](#COPYRIGHT)COPYRIGHT

           This program is part of the LTTng-tools project.

           LTTng-tools is distributed under the GNU General Public License
           version 2 <http://www.gnu.org/licenses/old-
           licenses/gpl-2.0.en.html>. See the LICENSE
           <https://github.com/lttng/lttng-tools/blob/master/LICENSE> file
           for details.

## [](#THANKS)THANKS

           Special thanks to Michel Dagenais and the DORSAL laboratory
           <http://www.dorsal.polymtl.ca/> at École Polytechnique de Montréal
           for the LTTng journey.

           Also thanks to the Ericsson teams working on tracing which helped
           us greatly with detailed bug reports and unusual test cases.

## [](#SEE_ALSO)SEE ALSO

           babeltrace2(1), lttng(1), lttng-create(1)

## [](#COLOPHON)COLOPHON

           This page is part of the LTTng-Tools (LTTng tools) project.
           Information about the project can be found at ⟨http://lttng.org/⟩.
           It is not known how to report bugs for this man page; if you know,
           please send a mail to man-pages@man7.org.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/lttng/lttng-tools.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    LTTng 2.15.1                   14 June 2021                LTTNG-CRASH(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng-create(1)](../man1/lttng-create.1.html),  [babeltrace2-source.ctf.fs(7)](../man7/babeltrace2-source.ctf.fs.7.html)

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
