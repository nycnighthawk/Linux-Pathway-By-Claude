---
{"title": "stg-refresh(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-refresh.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-refresh(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-REFRESH(1)                 StGit Manual                STG-REFRESH(1)

## [](#NAME)NAME

           stg-refresh - Incorporate worktree changes into current patch

## [](#SYNOPSIS)SYNOPSIS

           stg refresh [OPTIONS] [path]...

## [](#DESCRIPTION)DESCRIPTION

           Include the latest work tree and index changes in the current
           patch. This command generates a new git commit object for the
           patch; the old commit is no longer visible.

           Refresh will warn if the index is dirty, and require use of either
           the --index or --force options to override this check. This is to
           prevent accidental full refresh when only some changes were staged
           using git add interactive mode.

           You may optionally list one or more files or directories relative
           to the current working directory; if you do, only matching files
           will be updated.

           Behind the scenes, stg refresh first creates a new temporary patch
           with your updates, and then merges that patch into the patch you
           asked to have refreshed. If you asked to refresh a patch other
           than the topmost patch, there can be conflicts; in that case, the
           temporary patch will be left for you to take care of, for example
           with stg squash.

           The creation of the temporary patch is recorded in a separate
           entry in the patch stack log; this means that one undo step will
           undo the merge between the other patch and the temp patch, and two
           undo steps will additionally get rid of the temp patch.

## [](#OPTIONS)OPTIONS

           -u, --update
               Only update the current patch files

           -i, --index
               Instead of setting the patch top to the current contents of
               the worktree, set it to the current contents of the index.

           -F, --force
               Instead of warning the user when some work has already been
               staged (such as with git add interactive mode) force a full
               refresh.

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

           -p <patch>, --patch=<patch>
               Refresh (applied) <patch> instead of the top patch

           -a <note>, --annotate=<note>
               Annotate the patch log entry with <note>

           --submodules
               Include submodules in patch content

           --no-submodules
               Exclude submodules in patch content

           -e, --edit
               Invoke editor for patch description

           -d, --diff
               Show diff when editing patch description

           -m <message>, --message=<message>
               Use message instead of invoking the editor

           -f <path>, --file=<path>
               Use the contents of file instead of invoking the editor. Use
               "-" to read from stdin.

           --no-verify
               Disable commit-msg hook

           -s[=<value>], --signoff[=<value>]
               Add "Signed-off-by" message trailer.

               The value is optional and defaults to the committer name and
               email. This option may be provided multiple times.

           --ack[=<value>]
               Add "Acked-by" message trailer.

               The value is optional and defaults to the committer’s name and
               email. This option may be provided multiple times.

           --review[=<value>]
               Add "Reviewed-by" message trailer.

               The value is optional and defaults to the committer’s name and
               email. This option may be provided multiple times.

           --author=<name-and-email>
               Set the author "name <email>"

           --authname=<name>
               Set the author name

           --authemail=<email>
               Set the author email

           --authdate=<date>
               Set the date the patch was authored.

               Use "now" to use the current time and date.

           --committer-date-is-author-date
               Instead of using the current time as the committer date, use
               the author date of the commit as the committer date.

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

    StGit 2.6.1                     08/04/2026                 STG-REFRESH(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg(1)](../man1/stg.1.html),  [stg-new(1)](../man1/stg-new.1.html)

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
