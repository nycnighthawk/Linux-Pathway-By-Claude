---
{"title": "stg-reset(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-reset.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-reset(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-RESET(1)                   StGit Manual                  STG-RESET(1)

## [](#NAME)NAME

           stg-reset - Reset the patch stack to an earlier state

## [](#SYNOPSIS)SYNOPSIS

           stg reset [--hard] [<committish> [<patchname>...]]
           stg reset --hard

## [](#DESCRIPTION)DESCRIPTION

           Reset the patch stack to an earlier state. If no state is
           specified, reset only the changes in the worktree.

           The state is specified with a commit id from the stack log, which
           may be viewed with stg-log(1). Patch name arguments may optionally
           be provided to limit which patches are reset.

## [](#OPTIONS)OPTIONS

           --hard
               Discard changes in the index and worktree

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

    StGit 2.6.1                     08/04/2026                   STG-RESET(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg(1)](../man1/stg.1.html),  [stg-log(1)](../man1/stg-log.1.html),  [stg-repair(1)](../man1/stg-repair.1.html)

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
