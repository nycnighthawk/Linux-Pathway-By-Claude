---
{"title": "stg-squash(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-squash.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-squash(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-SQUASH(1)                  StGit Manual                 STG-SQUASH(1)

## [](#NAME)NAME

           stg-squash - Squash two or more patches into one

## [](#SYNOPSIS)SYNOPSIS

           stg squash [OPTIONS] <patch>...

## [](#DESCRIPTION)DESCRIPTION

           Squash two or more patches, creating one patch with their combined
           changes.

           The squash process, at a high level:

            1. Pop all the given patches, plus any other patches on top of
               them.

            2. Push the given patches in the order they were given on the
               command line. This establishes a tree containing the combined
               changes from the given patches.

            3. Replace given patches with a new, squashed patch.

            4. Allow the user to interactively edit the commit message of the
               new, squashed patch.

            5. Push other patches that were popped in step (1), if any.

           Conflicts can occur whenever a patch is pushed; this is, in steps
           (2) and (5). If conflicts occur, the squash command will halt such
           that the conflicts may be resolved manually.

## [](#OPTIONS)OPTIONS

           -n <name>, --name=<name>
               Use <name> for the squashed patch

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

    StGit 2.6.1                     08/04/2026                  STG-SQUASH(1)

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
