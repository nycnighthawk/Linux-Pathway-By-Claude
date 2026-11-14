---
{"title": "stg-pull(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-pull.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-pull(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-PULL(1)                    StGit Manual                   STG-PULL(1)

## [](#NAME)NAME

           stg-pull - Pull changes from a remote repository

## [](#SYNOPSIS)SYNOPSIS

           stg pull [OPTIONS] [repository]

## [](#DESCRIPTION)DESCRIPTION

           Pull the latest changes from a remote repository.

           The remote repository may be specified on the command line, but
           defaults to branch.<name>.remote from the git configuration, or
           "origin" if not configured.

           This command works by popping all currently applied patches from
           the stack, pulling the changes from the remote repository,
           updating the stack base to the new remote HEAD, and finally
           pushing all formerly applied patches back onto the stack. Merge
           conflicts may occur during the final push step. Those conflicts
           need to be resolved manually.

           See git-fetch(1) for the format of remote repository argument.

## [](#OPTIONS)OPTIONS

           -n, --nopush
               Do not push back patches after pulling

           -m, --merged
               Check for patches that may have been merged upstream.

               When pushing-back patches, each patch is checked to see if its
               changes already exist in the just-pulled upstream changes. If
               a patch’s changes have already been merged upstream, the patch
               will still exist in the stack, but become empty after the pull
               operation.

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

    StGit 2.6.1                     08/04/2026                    STG-PULL(1)

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
