---
{"title": "sysctl(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sysctl.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sysctl(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PARAMETERS](#PARAMETERS) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSCTL(8)                System Manager's Manual                SYSCTL(8)

## [](#NAME)NAME

           sysctl - configure kernel parameters at runtime

## [](#SYNOPSIS)SYNOPSIS

           sysctl [option ...] variable[=value] ...

           sysctl -p file-or-regexp ...

## [](#DESCRIPTION)DESCRIPTION

           sysctl is used to modify kernel parameters at runtime.  The
           parameters available are those listed under /proc/sys/.  Procfs is
           required for sysctl support in Linux.  You can use sysctl to both
           read and write sysctl data.

## [](#PARAMETERS)PARAMETERS

           variable
                  The name of a key to read from.  An example is
                  kernel.ostype.  The '/' separator is also accepted in place
                  of a '.'.

           variable=value
                  To set a key, use the form variable=value where variable is
                  the key and value is the value to set it to.  If the value
                  contains quotes or characters which are parsed by the
                  shell, you may need to enclose the value in double quotes.

           -n, --values
                  Use this option to disable printing of the key name when
                  printing values.

           -e, --ignore
                  Use this option to ignore errors about unknown keys.

           -N, --names
                  Use this option to only print the names.  It may be useful
                  with shells that have programmable completion.

           -q, --quiet
                  Use this option to not display the values set to stdout.

           -w, --write
                  Force all arguments to be write arguments and print an
                  error if they cannot be parsed this way.

           -p[FILE], --load[=FILE]
                  Load in sysctl settings from the file specified or
                  /etc/sysctl.conf if none given.  Specifying - as filename
                  means reading data from standard input. Using this option
                  will mean arguments to sysctl are files, which are read in
                  the order they are specified.  The file argument may be
                  specified as regular expression.

           -a, --all
                  Display all values currently available except deprecated
                  and verboten parameters.

           --deprecated
                  Include deprecated parameters to --all values listing.

           -b, --binary
                  Print value without new line.

           --system
                  Load settings from all system configuration files. See the
                  SYSTEM FILE PRECEDENCE section below.

           -r, --pattern pattern
                  Only apply settings that match pattern.  The pattern uses
                  extended regular expression syntax.

           -A     Alias of -a

           -d     Alias of -h

           -f     Alias of -p

           -X     Alias of -a

           -o     Does nothing, exists for BSD compatibility.

           -x     Does nothing, exists for BSD compatibility.

           -h, --help
                  Display help text and exit.

           -V, --version
                  Display version information and exit.

## [](#FILES)FILES

           /proc/sys
           /etc/sysctl.d/*.conf
           /run/sysctl.d/*.conf
           /usr/local/lib/sysctl.d/*.conf
           /usr/lib/sysctl.d/*.conf
           /lib/sysctl.d/*.conf
           /etc/sysctl.conf

## [](#NOTES)NOTES

       System file precedence
           When using the --system option, sysctl will read files from
           directories in the following list in given order from top to
           bottom. Once a file of a given filename is loaded, any file of the
           same name in subsequent directories is ignored.

           /etc/sysctl.d/*.conf
           /run/sysctl.d/*.conf
           /usr/local/lib/sysctl.d/*.conf
           /usr/lib/sysctl.d/*.conf
           /lib/sysctl.d/*.conf

           All configuration files are sorted in lexicographic order,
           regardless of the directory they reside in. Configuration files
           can either be completely replaced (by having a new configuration
           file with the same name in a directory of higher priority) or
           partially replaced (by having a configuration file that is ordered
           later).

           The file /etc/sysctl.conf is read last which means it can
           replace/override any parameters previously set in files in the
           listed directories.

       Deprecated parameters
           The base_reachable_time and retrans_time are deprecated.  The
           sysctl command does not allow changing values of these parameters.
           Users who insist to use deprecated kernel interfaces should push
           values to /proc file system by other means.  For example:

           echo 256 > /proc/sys/net/ipv6/neigh/eth0/base_reachable_time

       Verboten parameters
           Certain kernel parameters should not be read due to side-effects
           and will be skipped by sysctl using the --all option.

           stat_refresh
                  This parameter returns no value but flushes per-cpu vm
                  statistics.

## [](#EXAMPLES)EXAMPLES

           /sbin/sysctl -a
           /sbin/sysctl -n kernel.hostname
           /sbin/sysctl -w kernel.domainname="example.com"
           /sbin/sysctl -p/etc/sysctl.conf
           /sbin/sysctl -a --pattern forward
           /sbin/sysctl -a --pattern forward$
           /sbin/sysctl -a --pattern 'net.ipv4.conf.(eth|wlan)0.arp'
           /sbin/sysctl --pattern '^net.ipv6' --system

## [](#SEE_ALSO)SEE ALSO

           proc(5), sysctl.conf(5), regex(7)

## [](#REPORTING_BUGS)REPORTING BUGS

           Please send bug reports to ⟨procps@freelists.org⟩.

## [](#COLOPHON)COLOPHON

           This page is part of the procps-ng (/proc filesystem utilities)
           project.  Information about the project can be found at 
           ⟨https://gitlab.com/procps-ng/procps⟩.  If you have a bug report
           for this manual page, see
           ⟨https://gitlab.com/procps-ng/procps/blob/master/Documentation/bugs.md⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://gitlab.com/procps-ng/procps.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    procps-ng                       2024-07-19                      SYSCTL(8)

------------------------------------------------------------------------

Pages that refer to this page: [perfalloc(1)](../man1/perfalloc.1.html),  [pmdadarwin(1)](../man1/pmdadarwin.1.html),  [pmdaperfevent(1)](../man1/pmdaperfevent.1.html),  [coredump.conf(5)](../man5/coredump.conf.5.html),  [lxc.container.conf(5)](../man5/lxc.container.conf.5.html),  [proc(5)](../man5/proc.5.html),  [sysctl.conf(5)](../man5/sysctl.conf.5.html),  [sysctl.d(5)](../man5/sysctl.d.5.html),  [flowtop(8)](../man8/flowtop.8.html),  [systemd-coredump(8)](../man8/systemd-coredump.8.html),  [systemd-sysctl.service(8)](../man8/systemd-sysctl.service.8.html)

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
