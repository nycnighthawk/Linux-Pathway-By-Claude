---
{"title": "stg-push(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-push.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-push(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-PUSH(1)                    StGit Manual                   STG-PUSH(1)

## [](#NAME)NAME

           stg-push - Push (apply) one or more unapplied patches

## [](#SYNOPSIS)SYNOPSIS

           stg push [OPTIONS] [patch]...
           stg push [OPTIONS] -n <number>
           stg push [OPTIONS] --all

## [](#DESCRIPTION)DESCRIPTION

           Push one or more unapplied patches from the series onto the stack.

           By default, the first unapplied patch is pushed.

           Unapplied patches may be pushed in arbitrary order, but out of
           order pushes may result in merge conflicts. If there are conflicts
           while pushing a patch, the conflicts are written to the work tree
           and the push command halts. Conflicts may then be resolved using
           the normal Git methods, or alternatively the push may be undone
           using stg-undo(1).

## [](#OPTIONS)OPTIONS

           -a, --all
               Push all unapplied patches

           -n <n>, --number=<n>
               Push the specified number of patches.

               A negative number indicates to push all but that number of
               patches

           --reverse
               Push the patches in reverse order

           --noapply
               Reorder patches by pushing without applying

           --set-tree
               Push patches keeping their original trees.

               For each patch pushed, instead of performing a merge, the
               patch is pushed such the resulting tree will be identical to
               the tree associated with the patch.

               This can be useful when splitting a patch by first popping the
               patch and creating a new patch with some of the changes.
               Pushing the original patch with --set-tree will avoid
               conflicts and only the remaining changes will be in the patch.

           -k, --keep
               Keep the local changes

           -m, --merged
               Check for patches merged upstream

           --committer-date-is-author-date
               Instead of using the current time as the committer date, use
               the author date of the commit as the committer date.

           --conflicts[=<policy>]
               Either "allow" or "disallow" pushing a patch with conflicts.

               Using --conflicts=allow (or just --conflicts) allows pushing a
               patch that may result in unresolved merge conflicts. The patch
               will be pushed and files with conflicts will be left with
               conflict markers to be resolved manually; or the operation
               undone with stg undo --hard. This is the default behavior and
               also corresponds to the "stgit.push.allow-conflicts" variable
               being set to "true".

               Using --conflicts=disallow disallows pushing any patch that
               would result in merge conflicts. The operation will stop on
               the last patch that can be pushed without conflicts. This
               behavior can be configured by setting
               "stgit.push.allow-conflicts" to "false".

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

    StGit 2.6.1                     08/04/2026                    STG-PUSH(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg(1)](../man1/stg.1.html),  [stg-edit(1)](../man1/stg-edit.1.html)

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
