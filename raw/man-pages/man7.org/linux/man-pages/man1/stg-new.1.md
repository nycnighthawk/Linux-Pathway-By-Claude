---
{"title": "stg-new(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-new.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-new(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-NEW(1)                     StGit Manual                    STG-NEW(1)

## [](#NAME)NAME

           stg-new - Create a new patch at top of the stack

## [](#SYNOPSIS)SYNOPSIS

           stg new [OPTIONS] [patchname] [-- <path>...]
           stg new [OPTIONS] [--name <patchname>] [-- <path>...]

## [](#DESCRIPTION)DESCRIPTION

           Create a new, empty patch on the current stack. The new patch is
           created on top of the currently applied patches, and is made the
           new top of the stack. Uncommitted changes in the work tree are not
           included in the patch — that is handled by stg-refresh.

           The given patch name must be unique in the stack. If no name is
           given, one is generated from the first line of the patch’s commit
           message.

           Patch names follow the rules for Git references with the
           additional constraint that patch names may not contain the /
           character. See git-check-ref-format(1) for details.

           Patch names may start with a leading -. When specifying such a
           patch name on the command line, the leading - may be escaped with
           a single backslash as in \-patch-name to disambiguate the patch
           name from command line options.

           An editor will be launched to edit the commit message to be used
           for the patch, unless the --message flag already specified one.
           The patchdescr.tmpl template file (if available) is used to
           pre-fill the editor.

## [](#OPTIONS)OPTIONS

           -n <name>, --name=<name>
               Alternative to the [patchname] argument for specifying the
               name of the new patch. This option allows the patch name to
               start with an unescaped leading -.

           -r, --refresh
               Refresh the new patch with changes from work tree. New patches
               are empty by default, but with this option the new patch will
               capture outstanding changes in the work tree as if
               stg-refresh(1) was run. Use --index to refresh from the index
               instead of the work tree.

           -i, --index
               Instead of refreshing the patch with the current contents of
               the worktree, use the current contents of the index.

           -F, --force
               Force refresh with staged and unstaged changes.

               By default, if there are staged changes in the index along
               with unstaged changes in the work tree, the command will
               abort. This option forces the command to proceed using both
               the staged and unstaged changes.

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

           --save-template=<file>
               Instead of running the command, just write the patch
               description to FILE, and exit. (If FILE is "-", write to
               stdout.)

               When driving StGit from another program, it may be useful to
               first call a command with --save-template, then let the user
               edit the message, and then call the same command with --file.

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

    StGit 2.6.1                     08/04/2026                     STG-NEW(1)

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
