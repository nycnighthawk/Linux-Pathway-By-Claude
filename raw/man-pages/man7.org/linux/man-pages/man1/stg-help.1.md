---
{"title": "stg-help(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-help.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-help(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-HELP(1)                    StGit Manual                   STG-HELP(1)

## [](#NAME)NAME

           stg-help - Print this message or the help of the given
           subcommand(s)

## [](#SYNOPSIS)SYNOPSIS

           stg help branch --list
           stg help branch --create
           stg help branch --clone
           stg help branch --rename
           stg help branch --protect
           stg help branch --unprotect
           stg help branch --delete
           stg help branch --cleanup
           stg help branch --describe
           stg help clean
           stg help commit
           stg help completion bash
           stg help completion fish
           stg help completion zsh
           stg help completion list aliases
           stg help completion list commands
           stg help completion list commands-and-aliases
           stg help completion man
           stg help delete
           stg help diff
           stg help edit
           stg help email format
           stg help email send
           stg help export
           stg help files
           stg help float
           stg help fold
           stg help goto
           stg help hide
           stg help id
           stg help import
           stg help init
           stg help log
           stg help name
           stg help new
           stg help next
           stg help patches
           stg help pick
           stg help pop
           stg help prev
           stg help pull
           stg help push
           stg help rebase
           stg help redo
           stg help refresh
           stg help rename
           stg help repair
           stg help reset
           stg help series
           stg help show
           stg help sink
           stg help spill
           stg help squash
           stg help sync
           stg help top
           stg help uncommit
           stg help undo
           stg help unhide
           stg help version
           stg help help

## [](#DESCRIPTION)DESCRIPTION

           Print this message or the help of the given subcommand(s)

## [](#COMMANDS)COMMANDS

           branch --list
               List branches in this repository

           branch --create
               Create and switch to a new branch

           branch --clone
               Clone the contents of the current branch

           branch --rename
               Rename an existing branch

           branch --protect
               Prevent StGit from modifying a branch

           branch --unprotect
               Allow StGit to modify a previously protected branch

           branch --delete
               Delete a branch

           branch --cleanup
               Remove StGit patch stack from branch

           branch --describe
               Set the branch description

           clean
               Delete empty patches from the series

           commit
               Finalize patches to the stack base

           completion bash
               Generate bash completion script

           completion fish
               Generate fish shell completion script

           completion zsh
               Generate zsh completion script

           completion list aliases
               List aliases

           completion list commands
               List StGit commands

           completion list commands-and-aliases
               List StGit commands and aliases

           completion man
               Generate asciidoc man pages

           delete
               Delete patches

           diff
               Show a diff

           edit
               Edit a patch

           email format
               Format patches as email files

           email send
               Send patches as emails

           export
               Export patches to a directory

           files
               Show files modified by a patch

           float
               Push patches to the top, even if applied

           fold
               Fold diff file into the current patch

           goto
               Go to patch by pushing or popping as necessary

           hide
               Hide patches in the series

           id
               Print git hash of a StGit revision

           import
               Import patches to stack

           init
               Initialize a StGit stack on a branch

           log
               Display or optionally clear the stack changelog

           name
               Print patch name of a StGit revision

           new
               Create a new patch at top of the stack

           next
               Print the name of the next patch

           patches
               Show patches that modify files

           pick
               Import a patch from another branch or a commit object

           pop
               Pop (unapply) one or more applied patches

           prev
               Print the name of the previous patch

           pull
               Pull changes from a remote repository

           push
               Push (apply) one or more unapplied patches

           rebase
               Move the stack base to another point in history

           redo
               Undo the last undo operation

           refresh
               Incorporate worktree changes into current patch

           rename
               Rename a patch

           repair
               Repair stack after branch is modified with git commands

           reset
               Reset the patch stack to an earlier state

           series
               Display the patch series

           show
               Show patch commits

           sink
               Move patches deeper in the stack

           spill
               Spill changes from the topmost patch

           squash
               Squash two or more patches into one

           sync
               Synchronize patches with a branch or a series

           top
               Print the name of the top patch

           uncommit
               Convert regular Git commits into StGit patches

           undo
               Undo the last command

           unhide
               Unhide hidden patches

           version
               Print version information and exit

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

    StGit 2.6.1                     08/04/2026                    STG-HELP(1)

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
