---
{"title": "git-mktree(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-mktree.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-mktree(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-MKTREE(1)                   Git Manual                  GIT-MKTREE(1)

## [](#NAME)NAME

           git-mktree - Build a tree-object from ls-tree formatted text

## [](#SYNOPSIS)SYNOPSIS

           git mktree [-z] [--missing] [--batch]

## [](#DESCRIPTION)DESCRIPTION

           Reads standard input in non-recursive ls-tree output format, and
           creates a tree object. The order of the tree entries is normalized
           by mktree so pre-sorting the input is not required. The object
           name of the tree object built is written to the standard output.

## [](#OPTIONS)OPTIONS

           -z
               Read the NUL-terminated ls-tree -z output instead.

           --missing
               Allow missing objects. The default behaviour (without this
               option) is to verify that each tree entry’s hash identifies an
               existing object. This option has no effect on the treatment of
               gitlink entries (aka "submodules") which are always allowed to
               be missing.

           --batch
               Allow building of more than one tree object before exiting.
               Each tree is separated by a single blank line. The final
               newline is optional. Note - if the -z option is used, lines
               are terminated with NUL.

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

    Git 2.55.0.493.g5b2471          2026-08-03                  GIT-MKTREE(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-merge-tree(1)](../man1/git-merge-tree.1.html)

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
