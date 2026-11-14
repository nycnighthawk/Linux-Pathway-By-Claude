---
{"title": "git-write-tree(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-write-tree.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-write-tree(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-WRITE-TREE(1)               Git Manual              GIT-WRITE-TREE(1)

## [](#NAME)NAME

           git-write-tree - Create a tree object from the current index

## [](#SYNOPSIS)SYNOPSIS

           git write-tree [--missing-ok] [--prefix=<prefix>/]

## [](#DESCRIPTION)DESCRIPTION

           Creates a tree object using the current index. The name of the new
           tree object is printed to standard output.

           The index must be in a fully merged state.

           Conceptually, git write-tree sync()s the current index contents
           into a set of tree files. In order to have that match what is
           actually in your directory right now, you need to have done a git
           update-index phase before you did the git write-tree.

## [](#OPTIONS)OPTIONS

           --missing-ok
               Normally git write-tree ensures that the objects referenced by
               the directory exist in the object database. This option
               disables this check.

           --prefix=<prefix>/
               Writes a tree object that represents a subdirectory <prefix>.
               This can be used to write the tree object for a subproject
               that is in the named subdirectory.

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

    Git 2.55.0.493.g5b2471          2026-08-03              GIT-WRITE-TREE(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-commit-tree(1)](../man1/git-commit-tree.1.html),  [git-merge-tree(1)](../man1/git-merge-tree.1.html),  [git-read-tree(1)](../man1/git-read-tree.1.html)

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
