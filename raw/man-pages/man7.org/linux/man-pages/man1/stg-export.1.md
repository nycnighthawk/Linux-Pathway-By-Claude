---
{"title": "stg-export(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-export.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-export(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-EXPORT(1)                  StGit Manual                 STG-EXPORT(1)

## [](#NAME)NAME

           stg-export - Export patches to a directory

## [](#SYNOPSIS)SYNOPSIS

           stg export [OPTIONS] [patch]...

## [](#DESCRIPTION)DESCRIPTION

           Export a range of patches to a given directory in unified diff
           format. All applied patches are exported by default.

           Patches are exported to patches-<branch> by default. The --dir
           option may be used to specify a different output directory.

           The patch file output may be customized via a template file found
           at "$GIT_DIR/patchexport.tmpl",
           "~/.stgit/templates/patchexport.tmpl", or
           "$(prefix)/share/stgit/templates". The following variables are
           supported in the template file:

               %(description)s - patch description
               %(shortdescr)s  - the first line of the patch description
               %(longdescr)s   - the rest of the patch description, after the first line
               %(diffstat)s    - the diff statistics
               %(authname)s    - author name
               %(authemail)s   - author email
               %(authdate)s    - patch creation date (ISO-8601 format)
               %(commname)s    - committer name
               %(commemail)s   - committer email

## [](#OPTIONS)OPTIONS

           -b <branch>, --branch=<branch>
               Use <branch> instead of current branch

           -d <dir>, --dir=<dir>
               Export patches to <dir> instead of the default

           -p, --patch
               Suffix patch file names with ".patch"

           -e <ext>, --extension=<ext>
               Suffix patch file names with ".<ext>"

           -n, --numbered
               Prefix patch file names with order numbers.

           -t <file>, --template=<file>
               Use <file> as template

           -s, --stdout
               Export to stdout instead of directory

           -O <option>, --diff-opt=<option>
               Pass additional <option> to git diff.

               See the git-diff(1) man page. This option may be specified
               multiple times.

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

    StGit 2.6.1                     08/04/2026                  STG-EXPORT(1)

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
