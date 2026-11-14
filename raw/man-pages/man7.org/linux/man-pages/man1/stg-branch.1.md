---
{"title": "stg-branch(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-branch.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-branch(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-BRANCH(1)                  StGit Manual                 STG-BRANCH(1)

## [](#NAME)NAME

           stg-branch - Branch operations: switch, list, create, rename,
           delete, ...

## [](#SYNOPSIS)SYNOPSIS

           stg branch
           stg branch [--merge] <branch>
           stg branch {--list,-l}
           stg branch {--create,-c} <new-branch> [committish]
           stg branch {--clone,-C} [new-branch]
           stg branch {--rename,-r} [old-name] <new-name>
           stg branch {--protect,-p} [branch]
           stg branch {--unprotect,-u} [branch]
           stg branch {--delete,-D} [--force] [branch]
           stg branch --cleanup [--force] [branch]
           stg branch {--describe,-d} <description> [branch]

## [](#DESCRIPTION)DESCRIPTION

           Create, clone, switch, rename, or delete StGit-enabled branches.

           With no arguments, the current branch is printed to stdout.

           With a single argument, switch to the named branch.

           StGit supports specifying a branch using the @{-<n>} syntax
           supported by git, including - as a synonym for @{-1}. Thus stg
           branch - may be used to switch to the last checked-out HEAD. Note
           that @{-<n>} refers to the <n>th last HEAD, which is not
           necessarily a local branch. Using an @{-<n>} value that refers to
           anything but a local branch will result in an error.

## [](#COMMANDS)COMMANDS

           --list
               List each branch in the current repository along with its
               description, if any. The current branch is prefixed with >.
               Branches initialized with StGit stacks are prefixed with s.
               Protected branches are prefixed with p.

           --create
               Create and switch to a new branch. The new branch is
               initialized as a StGit patch stack. The new branch will be
               based on the current HEAD, by default, unless an optional
               committish provided for the base.

               StGit attempts to detect the branch from which the new branch
               forked, as well as the remote repository of that parent branch
               such that stg-pull(1) will pull from the correct remote
               branch. A warning will be printed if the parent branch cannot
               be determined.

           --clone
               Clone the current branch as <new-branch>, if specified, or
               using the current branch name with a timestamp.

               The description of the new branch will indicate it is a clone
               of the current branch. The parent information of the new
               branch is copied from the current branch.

           --rename
               Rename an existing branch

           --protect
               Prevent StGit from modifying a branch

           --unprotect
               Allow StGit to modify a previously protected branch

           --delete
               Delete a branch.

               The branch will not be deleted if there are any patches
               remaining unless the --force option is provided.

               If the current branch is selected for deletion, its parent
               branch must be configured and the worktree must be clean. The
               parent branch will be checked-out after the current branch is
               deleted.

               A protected branch may not be deleted; it must be unprotected
               first.

           --cleanup
               Remove StGit patch stack from branch. The operation will be
               refused if any patches remain, unless the --force option is
               provided.

               A protected branch will not be cleaned up; it must be
               unprotected first.

               A cleaned up branch may be reinitialized using stg-init(1).

           --describe
               Set the branch description

## [](#OPTIONS)OPTIONS

           --merge
               Merge work tree changes into the other branch

       --DELETE OPTIONS
           --force
               Force deletion even if branch has patches

       --CLEANUP OPTIONS
           --force
               Force clean up even if branch has patches

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

    StGit 2.6.1                     08/04/2026                  STG-BRANCH(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg(1)](../man1/stg.1.html),  [stg-init(1)](../man1/stg-init.1.html)

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
