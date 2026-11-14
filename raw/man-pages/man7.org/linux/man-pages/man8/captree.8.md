---
{"title": "captree(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/captree.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# captree(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CAPTREE(8)               System Manager's Manual               CAPTREE(8)

## [](#NAME)NAME

           captree - display tree of process capabilities

## [](#SYNOPSIS)SYNOPSIS

           captree [OPTIONS] [(pid|glob-name) ...]

## [](#DESCRIPTION)DESCRIPTION

           captree displays the capabilities on the mentioned processes
           indicated by pid or glob-name value(s) given on the command line.
           If no pid etc values are supplied, pid=1 is implied. A pid value
           of 0 displays all the processes known to the kernel.

           The POSIX.1e capabilities are displayed in double quotes in the
           cap_from_text(3) format. The IAB tuple of capabilities is
           displayed between square brackets in the text format described in
           cap_iab(3).  Both of these text formats are described in
           cap_text_formats(7).  Note, the IAB tuple text is omitted if it
           contains empty A and B components. This is because the regular
           POSIX.1e text contains information about the Inheritable flag
           already. This behavior can be overridden with the --verbose
           command line argument.

           Optional arguments (which must precede the list of pid|glob-name
           values):

           --help Displays usage information and exits. Note, modern Go
                  runtimes exit with status 0 in this case, but older
                  runtimes exit with status 2.

           --verbose
                  Displays capability sets and IAB tuples even when they are
                  empty, or redundant.

           --depth=n
                  Displays the process tree to a depth of n.  Note, the
                  default value for this parameter is 0, which implies
                  infinite depth.

           --colo[u]r=false
                  Colo[u]rs the targeted PIDs, if stdout is a TTY, in red.
                  This option defaults to true when running via a TTY. The
                  --color=false argument will suppress this color. Piping the
                  output into some other program will also suppress the use
                  of colo[u]r.

## [](#EXIT_STATUS)EXIT STATUS

           If the supplied target cannot be found the exit status is 1.
           Should an unrecognized option be provided, the exit status is 2.
           Otherwise, captree exits with status 0.

## [](#REPORTING_BUGS)REPORTING BUGS

           Please report bugs via the bugtracker referenced at:

           https://sites.google.com/site/fullycapable

## [](#SEE_ALSO)SEE ALSO

           cap_from_text(3), cap_text_formats(7), capabilities(7), and
           cap_iab(3).

           There is a longer article about captree, which includes some
           examples, here:

              https://sites.google.com/site/fullycapable/captree

## [](#AUTHOR)AUTHOR

           Andrew G. Morgan <morgan@kernel.org>

## [](#COLOPHON)COLOPHON

           This page is part of the libcap (capabilities commands and
           library) project.  Information about the project can be found at
           ⟨https://sites.google.com/site/fullycapable/⟩.  If you have a bug
           report for this manual page, send it to morgan@kernel.org (please
           put "libcap" in the Subject line).  This page was obtained from
           the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/libs/libcap/libcap.git/⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-30.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                    2026-04-07                     CAPTREE(8)

------------------------------------------------------------------------

Pages that refer to this page: [capsh(1)](../man1/capsh.1.html),  [libcap(3)](../man3/libcap.3.html),  [cap_text_formats(7)](../man7/cap_text_formats.7.html),  [getcap(8)](../man8/getcap.8.html),  [getpcaps(8)](../man8/getpcaps.8.html),  [setcap(8)](../man8/setcap.8.html)

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
