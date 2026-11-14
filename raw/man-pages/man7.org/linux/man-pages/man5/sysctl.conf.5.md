---
{"title": "sysctl.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/sysctl.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sysctl.conf(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [BUGS](#BUGS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSCTL.CONF(5)             File Formats Manual             SYSCTL.CONF(5)

## [](#NAME)NAME

           sysctl.conf - Linux kernel configuration parameters

## [](#DESCRIPTION)DESCRIPTION

           sysctl.conf is a set of configuration files that contain Linux
           kernel configuration parameters to be read and set by sysctl(8).

           This man page describes the configuration files for procps sysctl.
           If you are using systemd-sysctl(8), refer to sysctl.d(5) and note
           that it won't use the file /etc/sysctl.conf.

       Configuration Format
           Each line of a file read by procps sysctl describes a kernel
           parameter in the following format.

                  token = value

           There is no need to use quotation marks for value, even if the
           value is a list of items.

           Blank lines and lines that start with “#” or “;” are ignored.

           If a line begins with a single “-”, a failing attempt to set the
           value is ignored.

## [](#FILES)FILES

           procps sysctl, when run with the --system option, reads files from
           directories in the order shown below.

                  /etc/sysctl.d/*.conf
                  /run/sysctl.d/*.conf
                  /usr/local/lib/sysctl.d/*.conf
                  /usr/lib/sysctl.d/*.conf
                  /lib/sysctl.d/*.conf

           Finally, procps sysctl reads /etc/sysctl.conf.  This file is not
           used by systemd-sysctl, which means that some kernel parameters
           are not set depending on the implementation of sysctl that is
           installed.

## [](#BUGS)BUGS

           The maximum supported length of value is 4096 characters due to a
           limitation on /proc entry length in the Linux kernel.

## [](#EXAMPLES)EXAMPLES

           #
           #
           kernel.domainname = example.com
           ; A value containing a space is written to the sysctl.
           kernel.modprobe = /sbin/mod probe
           # A list of items for the value
           net.ipv4.ip_local_reserved_ports=8080,9148

## [](#SEE_ALSO)SEE ALSO

           sysctl.d(5), sysctl(8), systemd-sysctl(8)

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

    procps-ng                       2025-05-29                 SYSCTL.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [sysctl.d(5)](../man5/sysctl.d.5.html),  [sysctl(8)](../man8/sysctl.8.html)

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
