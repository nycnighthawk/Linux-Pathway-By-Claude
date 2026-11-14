---
{"title": "stg-import(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-import.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-import(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-IMPORT(1)                  StGit Manual                 STG-IMPORT(1)

## [](#NAME)NAME

           stg-import - Import patches to stack

## [](#SYNOPSIS)SYNOPSIS

           stg import [OPTIONS] <diff-path>
           stg import [OPTIONS] -m [<mail-path>|<Maildir-path>]
           stg import [OPTIONS] -M [<mbox-path>]
           stg import [OPTIONS] -S [<series-path>]
           stg import [OPTIONS] -u <diff-url>
           stg import [OPTIONS] -u -m <mail-url>
           stg import [OPTIONS] -u -M <mbox-url>
           stg import [OPTIONS] -u -S <series-url>

## [](#DESCRIPTION)DESCRIPTION

           Import patches from various sources to the stack.

           The simplest usage is to import a diff/patch file into the stack
           from a local file. By default, the file name is used as the patch
           name, but this can be overridden with --name. The patch can either
           be a normal file with the description at the top, or it can have
           standard mail format. The "Subject", "From", and "Date" headers
           will be used for the imported patch’s author details.

           Patches may also be imported from a mail file (-m/--mail), an mbox
           (-M/--mbox), or a series (-S/--series). Furthermore, the -u/--url
           option allows the patches source to be fetched from a url instead
           of from a local file.

           If a patch does not apply cleanly import is aborted unless
           --reject is specified, in which case it will apply to the work
           tree the parts of the patch that are applicable, leave the
           rejected hunks in corresponding *.rej files, and add an empty
           patch to the stack.

           The patch description must be separated from the diff with a "---"
           line.

## [](#OPTIONS)OPTIONS

           -m, --mail
               Import patch from an email file

           -M, --mbox
               Import patch series from an mbox file

           -S, --series
               Import patch series from a series file are tar archive.

           -u, --url
               Retrieve source from a url instead of local file

           -n <name>, --name=<name>
               Use <name> as the patch name

           -p <n>, --strip=<n>
               Remove <n> leading components from diff paths (default 1)

           --directory=<root>
               Prepend <root> to all filenames. If a "-p" argument is also
               passed, it is applied before prepending the new root.

           -t, --stripname
               Strip number and extension from patch name

           -C <n>
               Ensure <n> lines of matching context for each change

           -3, --3way
               Attempt 3-way merge if the patch records the identity of blobs
               it is supposed to apply to and those blobs are available
               locally.

           -i, --ignore
               Ignore the applied patches in the series

           --replace
               Replace the unapplied patches in the series

           -b <committish>, --base=<committish>
               Use <committish> instead of HEAD for file importing

           --reject
               Leave rejected hunks in ".rej" files

           --keep-cr
               Do not remove "\r" from email lines ending with "\r\n"

           --message-id
               Create Message-ID trailer in patch description based on the
               Message-ID email header. This option is applicable when
               importing with --mail or --mbox. This behavior may also be
               enabled via the "stgit.import.message-id" configuration
               option.

           -e, --edit
               Invoke editor for patch description

           -d, --diff
               Show diff when editing patch description

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

    StGit 2.6.1                     08/04/2026                  STG-IMPORT(1)

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
