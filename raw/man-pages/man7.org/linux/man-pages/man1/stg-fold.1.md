---
{"title": "stg-fold(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-fold.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-fold(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-FOLD(1)                    StGit Manual                   STG-FOLD(1)

## [](#NAME)NAME

           stg-fold - Fold diff file into the current patch

## [](#SYNOPSIS)SYNOPSIS

           stg fold [OPTIONS] [file]

## [](#DESCRIPTION)DESCRIPTION

           Fold diff file into the current patch. The given GNU diff file (or
           standard input) is applied onto the current patch.

           With the --threeway option, the diff is applied onto the bottom of
           the current patch and a three-way merge is performed with the
           current top. With the --base option, the diff is applied onto the
           specified base and a three-way merge is performed with the current
           top.

## [](#OPTIONS)OPTIONS

           -t, --threeway
               Perform a three-way merge with the current patch

           -b <committish>, --base=<committish>
               Use <committish> instead of HEAD when applying the patch

           -p <n>, --strip=<n>
               Remove <n> leading components from diff paths (default 1)

           -C <n>
               Ensure <n> lines of matching context for each change

           --reject
               Leave rejected hunks in ".rej" files

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

    StGit 2.6.1                     08/04/2026                    STG-FOLD(1)

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
