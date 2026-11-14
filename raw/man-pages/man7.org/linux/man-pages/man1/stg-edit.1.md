---
{"title": "stg-edit(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-edit.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-edit(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-EDIT(1)                    StGit Manual                   STG-EDIT(1)

## [](#NAME)NAME

           stg-edit - Edit a patch

## [](#SYNOPSIS)SYNOPSIS

           stg edit [OPTIONS] [patch]

## [](#DESCRIPTION)DESCRIPTION

           Edit a patch. Various aspects of a patch may be edited, including
           the message, author, patch name, or even the patch’s diff.

           By default, the topmost patch is edited.

           With no options or when --edit is specified, the patch details are
           edited interactively. Alternatively, command line options may be
           used to modify the patch non-interactively.

           The --diff option causes the patch’s diff to be appended to the
           patch description when editing interactively. This diff may be
           edited interactively (or just used as a reference when editing the
           patch’s message). The StGit attempts to apply the modified diff to
           the patch’s parent tree. If the updated diff does not apply, no
           changes are made to the patch and the edited patch is saved to a
           file which may be corrected and then fed-back into stg edit
           --file.

## [](#OPTIONS)OPTIONS

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

           -t <treeish>, --set-tree=<treeish>
               Set the patch’s git tree to the specified treeish without
               changing the tree of any other patches. When used on the top
               patch, the index and work tree will be updated to match the
               new tree. This low-level option is primarily meant to be used
               by tools built on top of StGit, such as the Emacs mode. See
               also the --set-tree flag of stg-push(1).

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

    StGit 2.6.1                     08/04/2026                    STG-EDIT(1)

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
