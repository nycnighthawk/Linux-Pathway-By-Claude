---
{"title": "stg-pick(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-pick.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-pick(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-PICK(1)                    StGit Manual                   STG-PICK(1)

## [](#NAME)NAME

           stg-pick - Import a patch from another branch or a commit object

## [](#SYNOPSIS)SYNOPSIS

           stg pick [OPTIONS] <source>...
           stg pick [OPTIONS] [--name NAME] [--parent COMMITTISH] <source>
           stg pick [OPTIONS] --fold [--file PATH]... <source>...
           stg pick [OPTIONS] --update <source>...

## [](#DESCRIPTION)DESCRIPTION

           Import one or more patches from another branch or commit object
           into the current series.

           By default, the imported patch’s name is reused, but may be
           overridden with the --name option. A commit object can be reverted
           with the --revert option.

           When using the --expose option, the format of the commit message
           is determined by the stgit.pick.expose-format configuration
           option. This option is a format string as may be supplied to the
           --pretty option of git-show(1). The default is
           "format:%B%n(imported from commit %H)", which appends the commit
           hash of the picked commit to the patch’s commit message.

## [](#OPTIONS)OPTIONS

           -B <branch>, --ref-branch=<branch>
               Pick patches from <branch>

           -r, --revert
               Revert the given commit object

           -x, --expose
               Append the imported commit id to the patch log

           --noapply
               Keep the imported patch unapplied

           -n <name>, --name=<name>
               Use <name> for the patch name

           -p <committish>, --parent=<committish>
               Use <committish> as parent

           --committer-date-is-author-date
               Instead of using the current time as the committer date, use
               the author date of the commit as the committer date.

           --fold
               Fold the commit object into the current patch

           --update
               Like fold but only update the current patch’s files

           -f <path>, --file=<path>
               Only fold the given file (may be used multiple times)

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

    StGit 2.6.1                     08/04/2026                    STG-PICK(1)

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
