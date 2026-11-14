---
{"title": "stg-float(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-float.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-float(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-FLOAT(1)                   StGit Manual                  STG-FLOAT(1)

## [](#NAME)NAME

           stg-float - Push patches to the top, even if applied

## [](#SYNOPSIS)SYNOPSIS

           stg float [OPTIONS] <patch>...
           stg float [OPTIONS] <-S|--series> <file>

## [](#DESCRIPTION)DESCRIPTION

           Push patches to the top, even if applied.

           Float one or more patches to be the topmost applied patches. The
           patches to be floated may currently be either applied or
           unapplied. The necessary pop and push operations will be performed
           to float the named patches. Patches not specified will remain
           applied or unapplied as they were prior to the float operation.

## [](#OPTIONS)OPTIONS

           --noapply
               Reorder patches without reapplying any patches

           -S <file>, --series=<file>
               Rearrange according to a series <file>

           -k, --keep
               Keep the local changes

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

    StGit 2.6.1                     08/04/2026                   STG-FLOAT(1)

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
