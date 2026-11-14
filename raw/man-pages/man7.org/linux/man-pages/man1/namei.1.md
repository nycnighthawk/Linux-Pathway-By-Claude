---
{"title": "namei(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/namei.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# namei(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [BUGS](#BUGS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NAMEI(1)                      User Commands                      NAMEI(1)

## [](#NAME)NAME

           namei - follow a pathname until a terminal point is found

## [](#SYNOPSIS)SYNOPSIS

           namei [options] pathname...

## [](#DESCRIPTION)DESCRIPTION

           namei interprets its arguments as pathnames to any type of Unix
           file (symlinks, files, directories, and so forth). namei then
           follows each pathname until an endpoint is found (a file, a
           directory, a device node, etc). If it finds a symbolic link, it
           shows the link, and starts following it, indenting the output to
           show the context.

           This program is useful for finding "too many levels of symbolic
           links" problems.

           For each line of output, namei uses the following characters to
           identify the file type found:
           ┌────┬─────────────────────────┐
           │    │                         │
           │ f: │ the pathname currently  │
           │    │ being resolved          │
           ├────┼─────────────────────────┤
           │    │                         │
           │ d  │ directory               │
           ├────┼─────────────────────────┤
           │    │                         │
           │ l  │ symbolic link (both the │
           │    │ link and its contents   │
           │    │ are output)             │
           ├────┼─────────────────────────┤
           │    │                         │
           │ s  │ socket                  │
           ├────┼─────────────────────────┤
           │    │                         │
           │ b  │ block device            │
           ├────┼─────────────────────────┤
           │    │                         │
           │ c  │ character device        │
           ├────┼─────────────────────────┤
           │    │                         │
           │ p  │ FIFO (named pipe)       │
           ├────┼─────────────────────────┤
           │    │                         │
           │ -  │ regular file            │
           ├────┼─────────────────────────┤
           │    │                         │
           │ ?  │ an error of some kind   │
           └────┴─────────────────────────┘

           namei prints an informative message when the maximum number of
           symbolic links this system can have has been exceeded.

## [](#OPTIONS)OPTIONS

           -l, --long
               Use the long listing format (same as -m -o -v).

           -m, --modes
               Show the mode bits of each file type in the style of ls(1),
               for example 'rwxr-xr-x'.

           -n, --nosymlinks
               Don’t follow symbolic links.

           -o, --owners
               Show owner and group name of each file.

           -v, --vertical
               Vertically align the modes and owners.

           -x, --mountpoints
               Show mountpoint directories with a 'D' rather than a 'd'.

           -Z, --context
               Show security context of the file or "?" if not available. The
               support for security contexts is optional and does not have to
               be compiled to the namei binary.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#BUGS)BUGS

           To be discovered.

## [](#AUTHORS)AUTHORS

           The original namei program was written by Roger Southwick
           <rogers@amadeus.wr.tek.com>.

           The program was rewritten by Karel Zak <kzak@redhat.com>.

## [](#SEE_ALSO)SEE ALSO

           ls(1), stat(1), symlink(7)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The namei command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                       NAMEI(1)

------------------------------------------------------------------------

Pages that refer to this page: [symlink(2)](../man2/symlink.2.html),  [symlink(7)](../man7/symlink.7.html)

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
