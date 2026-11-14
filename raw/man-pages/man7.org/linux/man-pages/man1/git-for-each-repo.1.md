---
{"title": "git-for-each-repo(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-for-each-repo.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-for-each-repo(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SUBPROCESS BEHAVIOR](#SUBPROCESS_BEHAVIOR) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-FOR-EACH-REPO(1)            Git Manual           GIT-FOR-EACH-REPO(1)

## [](#NAME)NAME

           git-for-each-repo - Run a Git command on a list of repositories

## [](#SYNOPSIS)SYNOPSIS

           git for-each-repo --config=<config> [--] <arguments>

## [](#DESCRIPTION)DESCRIPTION

           Run a Git command on a list of repositories. The arguments after
           the known options or -- indicator are used as the arguments for
           the Git subprocess.

           THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.

           For example, we could run maintenance on each of a list of
           repositories stored in a maintenance.repo config variable using

               git for-each-repo --config=maintenance.repo maintenance run

           This will run git -C <repo> maintenance run for each value <repo>
           in the multi-valued config variable maintenance.repo.

## [](#OPTIONS)OPTIONS

           --config=<config>
               Use the given config variable as a multi-valued list storing
               absolute path names. Iterate on that list of paths to run the
               given arguments.

               These config values are loaded from system, global, and local
               Git config, as available. If git for-each-repo is run in a
               directory that is not a Git repository, then only the system
               and global config is used.

           --keep-going
               Continue with the remaining repositories if the command failed
               on a repository. The exit code will still indicate that the
               overall operation was not successful.

               Note that the exact exit code of the failing command is not
               passed through as the exit code of the for-each-repo command:
               If the command failed in any of the specified repositories,
               the overall exit code will be 1.

## [](#SUBPROCESS_BEHAVIOR)SUBPROCESS BEHAVIOR

           If any git -C <repo> <arguments> subprocess returns a non-zero
           exit code, then the git for-each-repo process returns that exit
           code without running more subprocesses.

           Each git -C <repo> <arguments> subprocess inherits the standard
           file descriptors stdin, stdout, and stderr.

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

    Git 2.55.0.493.g5b2471          2026-08-03           GIT-FOR-EACH-REPO(1)

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
