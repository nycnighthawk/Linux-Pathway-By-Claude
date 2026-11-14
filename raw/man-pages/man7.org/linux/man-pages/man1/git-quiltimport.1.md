---
{"title": "git-quiltimport(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-quiltimport.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-quiltimport(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-QUILTIMPORT(1)              Git Manual             GIT-QUILTIMPORT(1)

## [](#NAME)NAME

           git-quiltimport - Applies a quilt patchset onto the current branch

## [](#SYNOPSIS)SYNOPSIS

           git quiltimport [--dry-run | -n] [--author <author>] [--patches <dir>]
                           [--series <file>] [--keep-non-patch]

## [](#DESCRIPTION)DESCRIPTION

           Applies a quilt patchset onto the current Git branch, preserving
           the patch boundaries, patch order, and patch descriptions present
           in the quilt patchset.

           For each patch the code attempts to extract the author from the
           patch description. If that fails it falls back to the author
           specified with --author. If the --author flag was not given the
           patch description is displayed and the user is asked to
           interactively enter the author of the patch.

           If a subject is not found in the patch description the patch name
           is preserved as the 1 line subject in the Git description.

## [](#OPTIONS)OPTIONS

           -n, --dry-run
               Walk through the patches in the series and warn if we cannot
               find all of the necessary information to commit a patch. At
               the time of this writing only missing author information is
               warned about.

           --author Author Name <Author Email>
               The author name and email address to use when no author
               information can be found in the patch description.

           --patches <dir>
               The directory to find the quilt patches.

               The default for the patch directory is patches or the value of
               the $QUILT_PATCHES environment variable.

           --series <file>
               The quilt series file.

               The default for the series file is <patches>/series or the
               value of the $QUILT_SERIES environment variable.

           --keep-non-patch
               Pass -b flag to git mailinfo (see git-mailinfo(1)).

## [](#GIT)GIT

           Part of the git(1) suite

## [](#COLOPHON)COLOPHON

           This page is part of the git (Git distributed version control
           system) project.  Information about the project can be found at 
           ⟨http://git-scm.com/⟩.  If you have a bug report for this manual
           page, see ⟨http://git-scm.com/community⟩.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/git/git.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Git 2.55.0.493.g5b2471          2026-08-03             GIT-QUILTIMPORT(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html)

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
