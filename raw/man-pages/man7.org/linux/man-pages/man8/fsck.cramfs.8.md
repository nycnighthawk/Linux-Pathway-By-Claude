---
{"title": "fsck.cramfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/fsck.cramfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fsck.cramfs(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FSCK.CRAMFS(8)            System Administration            FSCK.CRAMFS(8)

## [](#NAME)NAME

           fsck.cramfs - fsck compressed ROM filesystem

## [](#SYNOPSIS)SYNOPSIS

           fsck.cramfs [options] file

## [](#DESCRIPTION)DESCRIPTION

           fsck.cramfs is used to check the cramfs filesystem.

## [](#OPTIONS)OPTIONS

           -v, --verbose
               Enable verbose messaging.

           -b, --blocksize blocksize
               Use this blocksize, defaults to page size. Must be equal to
               what was set at creation time. Only used for --extract.

           --extract[=directory]
               Test to uncompress the whole filesystem. Optionally extract
               contents of the file to directory.

           -a
               This option is silently ignored.

           -y
               This option is silently ignored.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           0
               success

           4
               filesystem was left uncorrected

           8
               operation error, such as unable to allocate memory

           16
               usage information was printed

## [](#SEE_ALSO)SEE ALSO

           mount(8), mkfs.cramfs(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The fsck.cramfs command is part of the util-linux package which
           can be downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                 FSCK.CRAMFS(8)

------------------------------------------------------------------------

Pages that refer to this page: [fsck(8@@e2fsprogs)](../man8/fsck.8@@e2fsprogs.html),  [fsck(8)](../man8/fsck.8.html),  [mkfs.cramfs(8)](../man8/mkfs.cramfs.8.html),  [systemd-fsck@.service(8)](../man8/systemd-fsck@.service.8.html)

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
