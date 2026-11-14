---
{"title": "stg-rebase(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-rebase.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-rebase(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-REBASE(1)                  StGit Manual                 STG-REBASE(1)

## [](#NAME)NAME

           stg-rebase - Move the stack base to another point in history

## [](#SYNOPSIS)SYNOPSIS

           stg rebase [OPTIONS] [committish]

## [](#DESCRIPTION)DESCRIPTION

           Pop all patches from the current stack, move the stack base to the
           given new base and push the patches back.

           Merge conflicts may arise when patches are being pushed-back onto
           the stack. If this occurs, resolve the conflicts and then continue
           the rebase with the following sequence:

               stg add --update
               stg refresh
               stg goto top-patch

           Or to skip the conflicting patch:

               stg undo --hard
               stg push next-patch..top-patch

## [](#OPTIONS)OPTIONS

           -i, --interactive
               Interactively manipulate patches in editor

           -n, --nopush
               Do not push back patches after rebasing

           -m, --merged
               Check for patches that may have been merged upstream.

               When pushing-back patches, each patch is checked to see if its
               changes already exist in the new stack base. If a patch’s
               changes are detected to have been merged, the patch will still
               exist in the stack, but become empty after the rebase
               operation.

           --committer-date-is-author-date
               Instead of using the current time as the committer date, use
               the author date of the commit as the committer date.

           --autostash
               Automatically create a temporary stash before the operation
               begins, and apply it after the operation completes. This
               allows a rebase to be performed on a dirty work tree. Note
               however that the final stash application may result in
               non-trivial conflicts.

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

           -x <cmd>, --exec=<cmd>
               Execute the given shell command after each patch is
               successfully applied during the rebase operation. If the
               command fails (exits with non-zero status), the entire
               transaction is rolled back and no patches remain applied.

               This option may be specified multiple times to run multiple
               commands in sequence after each patch.

               This is similar to git rebase --exec, but note that stgit
               rolls back the entire operation on failure rather than leaving
               you at the failing point.

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

    StGit 2.6.1                     08/04/2026                  STG-REBASE(1)

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
