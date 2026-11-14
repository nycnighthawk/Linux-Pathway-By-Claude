---
{"title": "swaplabel(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/swaplabel.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# swaplabel(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SWAPLABEL(8)              System Administration              SWAPLABEL(8)

## [](#NAME)NAME

           swaplabel - print or change the label or UUID of a swap area

## [](#SYNOPSIS)SYNOPSIS

           swaplabel [-L label] [-U UUID] device

## [](#DESCRIPTION)DESCRIPTION

           swaplabel will display or change the label or UUID of a swap
           partition located on device (or regular file).

           If the optional arguments -L and -U are not given, swaplabel will
           simply display the current swap-area label and UUID of device.

           If an optional argument is present, then swaplabel will change the
           appropriate value on device. These values can also be set during
           swap creation using mkswap(8). The swaplabel utility allows
           changing the label or UUID on an actively used swap device.

## [](#OPTIONS)OPTIONS

           -L, --label label
               Specify a new label for the device. Swap partition labels can
               be at most 16 characters long. If label is longer than 16
               characters, swaplabel will truncate it and print a warning
               message.

           -U, --uuid UUID
               Specify a new UUID for the device. The UUID must be in the
               standard 8-4-4-4-12 character format, such as is output by
               uuidgen(1).

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           LIBBLKID_DEBUG=all
               Enable libblkid debug output.

## [](#AUTHORS)AUTHORS

           swaplabel was written by Jason Borden <jborden@bluehost.com> and
           Karel Zak <kzak@redhat.com>.

## [](#SEE_ALSO)SEE ALSO

           uuidgen(1), mkswap(8), swapon(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The swaplabel command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                   SWAPLABEL(8)

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
