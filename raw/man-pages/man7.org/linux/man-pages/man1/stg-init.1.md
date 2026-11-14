---
{"title": "stg-init(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-init.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-init(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-INIT(1)                    StGit Manual                   STG-INIT(1)

## [](#NAME)NAME

           stg-init - Initialize a StGit stack on a branch

## [](#SYNOPSIS)SYNOPSIS

           stg init [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           Initialize a StGit stack on a branch.

           Initializing a branch with a StGit stack commits initial, empty
           stack state for the branch to the repository. Theses stack
           metadata commits are tracked by the refs/stacks/<branch>
           reference. Updated stack state is committed by each StGit command
           that modifies the stack. StGit users do not have to do anything
           with the refs/stacks/<branch> ref directly.

           Some StGit commands, such as stg new and stg uncommit, will
           automatically initialize the stack, so it is often not necessary
           to explicitly initialize the stack on a branch. Also, branches
           created with stg branch --create are automatically initialized.

           The branch must already exist and point to a commit before
           initializing a StGit stack.

           StGit stack metadata can be deinitialized from a branch using stg
           branch --cleanup. See stg-branch(1) for more details.

## [](#OPTIONS)OPTIONS

           -b <branch>, --branch=<branch>
               Use <branch> instead of current branch

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

    StGit 2.6.1                     08/04/2026                    STG-INIT(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg(1)](../man1/stg.1.html),  [stg-branch(1)](../man1/stg-branch.1.html)

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
