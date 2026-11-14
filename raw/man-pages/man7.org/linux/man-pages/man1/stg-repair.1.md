---
{"title": "stg-repair(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-repair.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-repair(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-REPAIR(1)                  StGit Manual                 STG-REPAIR(1)

## [](#NAME)NAME

           stg-repair - Repair stack after branch is modified with git
           commands

## [](#SYNOPSIS)SYNOPSIS

           stg repair [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           If a branch with a StGit stack is modified with certain git
           commands such as git-commit(1), git-pull(1), git-merge(1), or
           git-rebase(1), the StGit stack metadata will become inconsistent
           with the branch state. There are a few options for resolving this
           kind of situation:

            1. Use stg-undo(1) to undo the effect of the git commands. Or
               similarly use stg-reset(1) to reset the stack/branch to any
               previous stack state.

            2. Use stg repair. This will repair the StGit stack metadata to
               accommodate the modifications to the branch made by the git
               commands. Specifically, it will do the following:

               •   If regular git commits were made on top of the stack of
                   StGit patches (i.e. by using plain git commit), stg repair
                   will convert those commits to StGit patches, preserving
                   their content.

               •   However, merge commits cannot become patches. So if a
                   merge was committed on top of the stack, stg repair will
                   mark all patches below the merge commit as unapplied,
                   since they are no longer reachable. An alternative when
                   this is not the desired behavior is to use stg undo to
                   first get rid of the offending merge and then run stg
                   repair again.

               •   The applied patches are supposed to be precisely those
                   that are reachable from the branch head. If, for example,
                   git-reset(1) was used to move the head, some applied
                   patches may no longer be reachable and some unapplied
                   patches may have become reachable. In this case, stg
                   repair will correct the applied/unapplied state of such
                   patches.

           stg repair will repair these inconsistencies reliably, so there
           are valid workflows where git commands are used followed by stg
           repair. For example, new patches can be created by first making
           commits with a graphical commit tool and then running stg repair
           to convert those commits into patches.

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

    StGit 2.6.1                     08/04/2026                  STG-REPAIR(1)

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
