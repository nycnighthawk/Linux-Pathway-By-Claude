---
{"title": "stg-series(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-series.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-series(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-SERIES(1)                  StGit Manual                 STG-SERIES(1)

## [](#NAME)NAME

           stg-series - Display the patch series

## [](#SYNOPSIS)SYNOPSIS

           stg series [OPTIONS] [-A] [-U] [-H]
           stg series [OPTIONS] --all
           stg series [OPTIONS] --short
           stg series [OPTIONS] [patch]...

## [](#DESCRIPTION)DESCRIPTION

           Show all the patches in the series, or just those in the given
           range, ordered from bottom to top.

           The topmost applied patch is prefixed with >. All other applied
           patches are prefixed with +. Unapplied patches are prefixed with -
           and hidden patches with !.

           The --reverse option may be used to reverse the order in which
           patches are displayed. The reversed order is more stack-like, with
           the base of the stack appearing at the bottom of of the display.

           Empty patches are prefixed with a * when the --empty option is
           used.

## [](#OPTIONS)OPTIONS

           -b <branch>, --branch=<branch>
               Use <branch> instead of current branch

           -a, --all
               Select all patches, including hidden patches

           -s[=<n>], --short[=<n>]
               Select <n> patches around the topmost patch only

           -A, --applied
               Select the applied patches only

           -U, --unapplied
               Select the unapplied patches only

           -H, --hidden
               Select the hidden patches only

           -m <branch>, --missing=<branch>
               Select patches in <branch> not present in current branch

           --author
               Display author name for each patch

           -c, --count
               Display the number of selected patches and exit

           -i[=<length>], --commit-id[=<length>]
               Display the commit id for each patch.

               The optional length indicates how many prefix characters of
               the commit id to display. The default is "full", which
               displays the full commit id, but may alternatively be
               specified as a positive integer greater than or equal to 4.

           -d, --description
               Display short description for each patch

           -e, --empty
               Before the +, >, -, and !  prefixes, print a column that
               contains either 0 (for empty patches) or a space (for
               non-empty patches).

           -P, --no-prefix
               Do not display the patch status prefix

           -I, --indices
               Display absolute patch indicies

           -O, --offsets
               Display relative offsets from topmost patch or from the stack
               base if no patches are applied.

           -r, --reverse
               Display patches in reverse order.

               This causes the stack to be displayed "right-side up". By
               default, patches are printed in order from bottom to top; i.e.
               the first patch in the stack is printed first and the last
               patch is printed last. Thus with the default ordering, the
               stack is displayed upside down. Reversing the order flips the
               stack such that the bottom of the stack is spatially at the
               top of the display, which may be more intuitive.

           --showbranch
               Display the branch name with the listed patches

## [](#STGIT)STGIT

           Part of the StGit suite - see stg(1)

## [](#COLOPHON)COLOPHON

           This page is part of the stgit (Stacked Git) project.  Information
           about the project can be found at ⟨http://www.procode.org/stgit/⟩.
           If you have a bug report for this manual page, see
           ⟨http://www.procode.org/stgit/⟩.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/stacked-git/stgit.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-19.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    StGit 2.6.1                     08/04/2026                  STG-SERIES(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg(1)](../man1/stg.1.html)

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
