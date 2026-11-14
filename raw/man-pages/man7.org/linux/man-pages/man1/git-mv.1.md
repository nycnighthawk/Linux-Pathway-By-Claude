---
{"title": "git-mv(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-mv.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-mv(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SUBMODULES](#SUBMODULES) \| [BUGS](#BUGS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-MV(1)                       Git Manual                      GIT-MV(1)

## [](#NAME)NAME

           git-mv - Move or rename a file, a directory, or a symlink

## [](#SYNOPSIS)SYNOPSIS

           git mv [-v] [-f] [-n] [-k] <source> <destination>
           git mv [-v] [-f] [-n] [-k] <source>... <destination-directory>

## [](#DESCRIPTION)DESCRIPTION

           Move or rename a file, directory, or symlink.

           In the first form, it renames <source>, which must exist and be
           either a file, symlink or directory, to <destination>. In the
           second form, <destination-directory> has to be an existing
           directory; the given sources will be moved into this directory.

           The index is updated after successful completion, but the change
           must still be committed.

## [](#OPTIONS)OPTIONS

           -f, --force
               Force renaming or moving of a file even if the <destination>
               exists.

           -k
               Skip move or rename actions which would lead to an error
               condition. An error happens when a source is neither existing
               nor controlled by Git, or when it would overwrite an existing
               file unless -f is given.

           -n, --dry-run
               Do nothing; only show what would happen

           -v, --verbose
               Report the names of files as they are moved.

## [](#SUBMODULES)SUBMODULES

           Moving a submodule using a gitfile (which means they were cloned
           with a Git version 1.7.8 or newer) will update the gitfile and
           core.worktree setting to make the submodule work in the new
           location. It also will attempt to update the submodule.<name>.path
           setting in the gitmodules(5) file and stage that file (unless -n
           is used).

## [](#BUGS)BUGS

           Each time a superproject update moves a populated submodule (e.g.
           when switching between commits before and after the move) a stale
           submodule checkout will remain in the old location and an empty
           directory will appear in the new location. To populate the
           submodule again in the new location the user will have to run "git
           submodule update" afterwards. Removing the old directory is only
           safe when it uses a gitfile, as otherwise the history of the
           submodule will be deleted too. Both steps will be obsolete when
           recursive submodule update has been implemented.

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

    Git 2.55.0.493.g5b2471          2026-08-03                      GIT-MV(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-add(1)](../man1/git-add.1.html),  [git-commit(1)](../man1/git-commit.1.html)

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
