---
{"title": "findfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/findfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# findfs(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FINDFS(8)                 System Administration                 FINDFS(8)

## [](#NAME)NAME

           findfs - find a filesystem by label or UUID

## [](#SYNOPSIS)SYNOPSIS

           findfs TAGNAME=value

## [](#DESCRIPTION)DESCRIPTION

           findfs will search the block devices in the system for a
           filesystem or partition with the specified tag. The currently
           supported tags are:

              LABEL=label
                  Specifies a filesystem label.

              UUID=uuid
                  Specifies a filesystem UUID.

              PARTUUID=uuid
                  Specifies a partition UUID. Partition identifiers are
                  supported for example for GUID Partition Table (GPT)
                  partition tables.

              PARTLABEL=label
                  Specifies a partition label (name). Partition labels
                  are supported for example for GPT and MAC partition
                  tables.

           If the filesystem or partition is found, the device name will be
           printed on stdout. If the input is not in the format of
           TAGNAME=value, then the input will be copied to the output without
           any modification.

           You can get a complete overview about the filesystems and
           partitions in the system with one of the following commands:

              lsblk --fs

              partx --show disk

              blkid

## [](#OPTIONS)OPTIONS

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           0
               success

           1
               label or UUID cannot be found

           2
               usage error, wrong number of arguments or unknown option

## [](#ENVIRONMENT)ENVIRONMENT

           LIBBLKID_DEBUG=all
               Enable libblkid debug output.

## [](#AUTHORS)AUTHORS

           findfs was originally written by Theodore Ts’o <tytso@mit.edu> and
           re-written for the util-linux package by Karel Zak
           <kzak@redhat.com>.

## [](#SEE_ALSO)SEE ALSO

           blkid(8), lsblk(8), partx(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The findfs command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                      FINDFS(8)

------------------------------------------------------------------------

Pages that refer to this page: [open_by_handle_at(2)](../man2/open_by_handle_at.2.html),  [libblkid(3)](../man3/libblkid.3.html),  [blkid(8)](../man8/blkid.8.html),  [wipefs(8)](../man8/wipefs.8.html)

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
