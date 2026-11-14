---
{"title": "partprobe(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/partprobe.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# partprobe(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PARTPROBE(8)                GNU Parted Manual                PARTPROBE(8)

## [](#NAME)NAME

           partprobe - inform the OS of partition table changes

## [](#SYNOPSIS)SYNOPSIS

           partprobe [-d] [-s] [devices...]

## [](#DESCRIPTION)DESCRIPTION

           This manual page documents briefly the partprobe command.

           partprobe is a program that informs the operating system kernel of
           partition table changes.

## [](#OPTIONS)OPTIONS

           This program uses short UNIX style options.

           -d, --dry-run
                  Don't update the kernel.

           -s, --summary
                  Show a summary of devices and their partitions.

           -h, --help
                  Show summary of options.

           -v, --version
                  Show version of program.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to <bug-parted@gnu.org>

## [](#SEE_ALSO)SEE ALSO

           parted(8).

## [](#AUTHOR)AUTHOR

           This manual page was written by Timshel Knoll
           <timshel@debian.org>, for the Debian GNU/Linux system (but may be
           used by others).

## [](#COLOPHON)COLOPHON

           This page is part of the GNU parted (partition table manipulation)
           project.  Information about the project can be found at 
           ⟨http://www.gnu.org/software/parted/⟩.  If you have a bug report
           for this manual page, send it to bug-parted@gnu.org.  This page
           was obtained from the project's upstream Git repository
           ⟨git://git.savannah.gnu.org/parted.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-26.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    parted                        March 18, 2002                 PARTPROBE(8)

------------------------------------------------------------------------

Pages that refer to this page: [addpart(8)](../man8/addpart.8.html),  [cfdisk(8)](../man8/cfdisk.8.html),  [delpart(8)](../man8/delpart.8.html),  [partx(8)](../man8/partx.8.html),  [resizepart(8)](../man8/resizepart.8.html),  [sfdisk(8)](../man8/sfdisk.8.html)

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
