---
{"title": "git-get-tar-commit-id(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-get-tar-commit-id.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-get-tar-commit-id(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-GET-TAR-COMMIT-ID(1)        Git Manual       GIT-GET-TAR-COMMIT-ID(1)

## [](#NAME)NAME

           git-get-tar-commit-id - Extract commit ID from an archive created
           using git-archive

## [](#SYNOPSIS)SYNOPSIS

           git get-tar-commit-id

## [](#DESCRIPTION)DESCRIPTION

           Read a tar archive created by git archive from the standard input
           and extract the commit ID stored in it. It reads only the first
           1024 bytes of input, thus its runtime is not influenced by the
           size of the tar archive very much.

           If no commit ID is found, git get-tar-commit-id quietly exits with
           a return code of 1. This can happen if the archive had not been
           created using git archive or if the first parameter of git archive
           had been a tree ID instead of a commit ID or tag.

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

    Git 2.55.0.493.g5b2471          2026-08-03       GIT-GET-TAR-COMMIT-ID(1)

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
