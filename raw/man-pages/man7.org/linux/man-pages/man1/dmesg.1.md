---
{"title": "dmesg(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dmesg.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dmesg(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COLORS](#COLORS) \| [EXIT STATUS](#EXIT_STATUS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DMESG(1)                      User Commands                      DMESG(1)

## [](#NAME)NAME

           dmesg - print or control the kernel ring buffer

## [](#SYNOPSIS)SYNOPSIS

           dmesg [options]

           dmesg --clear

           dmesg --read-clear [options]

           dmesg --console-level level

           dmesg --console-on

           dmesg --console-off

## [](#DESCRIPTION)DESCRIPTION

           dmesg is used to examine or control the kernel ring buffer.

           The default action is to display all messages from the kernel ring
           buffer.

## [](#OPTIONS)OPTIONS

           The --clear, --read-clear, --console-on, --console-off, and
           --console-level options are mutually exclusive.

           -C, --clear
               Clear the ring buffer.

           -c, --read-clear
               Clear the ring buffer after first printing its contents.

           -D, --console-off
               Disable the printing of messages to the console.

           -d, --show-delta
               Display the timestamp and the time delta spent between
               messages. If used together with --notime then only the time
               delta without the timestamp is printed.

           -E, --console-on
               Enable printing messages to the console.

           -e, --reltime
               Display the local time and the delta in human-readable format.
               Be aware that conversion to the local time could be inaccurate
               (see -T for more details).

           -F, --file file
               Read the syslog messages from the given file. Note that -F
               does not support messages in kmsg format. See -K instead.

           -f, --facility list
               Restrict output to the given (comma-separated) list of
               facilities. For example:

               dmesg --facility=daemon

               will print messages from system daemons only. For all
               supported facilities see the --help output.

           -H, --human
               Enable human-readable output. See also --color, --reltime and
               --nopager.

           -J, --json
               Use JSON output format. The time output format is in
               "sec.usec" format only, log priority level is not decoded by
               default (use --decode to split into facility and priority),
               the other options to control the output format or time format
               are silently ignored.

           -K, --kmsg-file file
               Read the /dev/kmsg messages from the given file. Different
               record as expected to be separated by a NULL byte.

           -k, --kernel
               Print kernel messages.

           -L, --color[=when]
               Colorize the output. The optional argument when can be auto,
               never or always. If the when argument is omitted, it defaults
               to auto. The colors can be disabled; for the current built-in
               default see the --help output. See also the COLORS section
               below.

           -l, --level list
               Restrict output to the given (comma-separated) list of levels.
               For example:

               dmesg --level=err,warn

               will print error and warning messages only. For all supported
               levels see the --help output.

               Appending a plus + to a level name also includes all higher
               levels. For example:

               dmesg --level=err+

               will print levels err, crit, alert and emerg.

               Prepending it will include all lower levels.

           -n, --console-level level
               Set the level at which printing of messages is done to the
               console. The level is a level number or abbreviation of the
               level name. For all supported levels see the --help output.

               For example, -n 1 or -n emerg prevents all messages, except
               emergency (panic) messages, from appearing on the console. All
               levels of messages are still written to /proc/kmsg, so
               syslogd(8) can still be used to control exactly where kernel
               messages appear. When the -n option is used, dmesg will not
               print or clear the kernel ring buffer.

           --noescape
               The unprintable and potentially unsafe characters (e.g.,
               broken multi-byte sequences, terminal controlling chars, etc.)
               are escaped in format \x<hex> for security reason by default.
               This option disables this feature at all. It’s usable for
               example for debugging purpose together with --raw. Be careful
               and don’t use it by default.

           -P, --nopager
               Do not pipe output into a pager. A pager is enabled by default
               for --human output.

           -p, --force-prefix
               Add facility, level or timestamp information to each line of a
               multi-line message.

           -r, --raw
               Print the raw message buffer, i.e., do not strip the log-level
               prefixes, but all unprintable characters are still escaped
               (see also --noescape).

               Note that the real raw format depends on the method how dmesg
               reads kernel messages. The /dev/kmsg device uses a different
               format than syslog(2). For backward compatibility, dmesg
               returns data always in the syslog(2) format. It is possible to
               read the real raw data from /dev/kmsg by, for example, the
               command 'dd if=/dev/kmsg iflag=nonblock'.

           -S, --syslog
               Force dmesg to use the syslog(2) kernel interface to read
               kernel messages. The default is to use /dev/kmsg rather than
               syslog(2) since kernel 3.5.0.

           -s, --buffer-size size
               Use a buffer of size to query the kernel ring buffer. This is
               16392 by default. (The default kernel syslog buffer size was
               4096 at first, 8192 since 1.3.54, 16384 since 2.1.113.) If you
               have set the kernel buffer to be larger than the default, then
               this option can be used to view the entire buffer.

           -T, --ctime
               Print human-readable timestamps.

               Be aware that the timestamp could be inaccurate! The time
               source used for the logs is not updated after system
               SUSPEND/RESUME. Timestamps are adjusted according to current
               delta between boottime and monotonic clocks, this works only
               for messages printed after last resume.

           --since time
               Display record since the specified time. Supported is the
               subsecond granularity. The time is possible to specify in
               absolute way as well as by relative notation (e.g. '1 hour
               ago'). Be aware that the timestamp could be inaccurate and see
               --ctime for more details.

           --until time
               Display record until the specified time. Supported is the
               subsecond granularity. The time is possible to specify in
               absolute way as well as by relative notation (e.g. '1 hour
               ago'). Be aware that the timestamp could be inaccurate and see
               --ctime for more details.

           -t, --notime
               Do not print kernel’s timestamps.

           --time-format format
               Print timestamps using the given format, which can be ctime,
               reltime, delta, iso or raw. The first three formats are
               aliases of the time-format-specific options. The raw format
               uses the default timestamp format showing seconds since boot.
               The iso format is a dmesg implementation of the ISO-8601
               timestamp format. The purpose of this format is to make the
               comparing of timestamps between two systems, and any other
               parsing, easy. The definition of the iso timestamp is:
               YYYY-MM-DD<T>HH:MM:SS,<microseconds>←+><timezone offset from
               UTC>.

               The iso format has the same issue as ctime: the time may be
               inaccurate when a system is suspended and resumed.

               --time-format may be used multiple times with different values
               for format to output each specified format.

               The delta always follows ctime or raw if specified together.

           -u, --userspace
               Print userspace messages.

           -w, --follow
               Wait for new messages. This feature is supported only on
               systems with a readable /dev/kmsg (since kernel 3.5.0).

           -W, --follow-new
               Wait and print only new messages.

           -x, --decode
               Decode facility and level (priority) numbers to human-readable
               prefixes.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#COLORS)COLORS

           The output colorization is implemented by terminal-colors.d(5)
           functionality. Implicit coloring can be disabled by an empty file

              /etc/terminal-colors.d/dmesg.disable

           for the dmesg command or for all tools by

              /etc/terminal-colors.d/disable

           Since version 2.41, the $NO_COLOR environment variable is also
           supported to disable output colorization unless explicitly enabled
           by a command-line option.

           The user-specific $XDG_CONFIG_HOME/terminal-colors.d or
           $HOME/.config/terminal-colors.d overrides the global setting.

           Note that the output colorization may be enabled by default, and
           in this case terminal-colors.d directories do not have to exist
           yet.

           The logical color names supported by dmesg are:

           subsys
               The message sub-system prefix (e.g., "ACPI:").

           time
               The message timestamp.

           timebreak
               The message timestamp in short ctime format in --reltime or
               --human output.

           alert
               The text of the message with the alert log priority.

           crit
               The text of the message with the critical log priority.

           err
               The text of the message with the error log priority.

           warn
               The text of the message with the warning log priority.

           segfault
               The text of the message that inform about segmentation fault.

## [](#EXIT_STATUS)EXIT STATUS

           dmesg can fail reporting permission denied error. This is usually
           caused by dmesg_restrict kernel setting, please see syslog(2) for
           more details.

## [](#AUTHORS)AUTHORS

           Karel Zak <kzak@redhat.com>

           dmesg was originally written by Theodore Ts’o
           <tytso@athena.mit.edu>.

## [](#SEE_ALSO)SEE ALSO

           terminal-colors.d(5), syslogd(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The dmesg command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                       DMESG(1)

------------------------------------------------------------------------

Pages that refer to this page: [syslog(2)](../man2/syslog.2.html),  [proc(5)](../man5/proc.5.html),  [proc_kmsg(5)](../man5/proc_kmsg.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [terminal-colors.d(5)](../man5/terminal-colors.d.5.html),  [babeltrace2-plugin-text(7)](../man7/babeltrace2-plugin-text.7.html),  [babeltrace2-source.text.dmesg(7)](../man7/babeltrace2-source.text.dmesg.7.html),  [insmod(8)](../man8/insmod.8.html),  [iptables-extensions(8)](../man8/iptables-extensions.8.html),  [tc-bpf(8)](../man8/tc-bpf.8.html),  [wg(8)](../man8/wg.8.html)

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
