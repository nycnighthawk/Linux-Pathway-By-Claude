---
{"title": "git-last-modified(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-last-modified.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-last-modified(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OUTPUT](#OUTPUT) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-LAST-MODIFIED(1)            Git Manual           GIT-LAST-MODIFIED(1)

## [](#NAME)NAME

           git-last-modified - EXPERIMENTAL: Show when files were last
           modified

## [](#SYNOPSIS)SYNOPSIS

           git last-modified [--recursive] [--show-trees] [--max-depth=<depth>] [-z]
                             [<revision-range>] [[--] <pathspec>...]

## [](#DESCRIPTION)DESCRIPTION

           Shows which commit last modified each of the relevant files and
           subdirectories. A commit renaming a path, or changing it’s mode is
           also taken into account.

           THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.

## [](#OPTIONS)OPTIONS

           -r, --recursive
               Recursively traverse into all subtrees. By default, the
               command only shows tree entries matching the <pathspec>. With
               this option, it descends into subtrees and displays all
               entries within them. Equivalent to --max-depth=-1.

           -t, --show-trees
               Show tree entries even when recursing into them.

           --max-depth=<depth>
               For each pathspec given on the command line, traverse at most
               <depth> levels into subtrees. A negative value means no limit.
               The default is 0, which shows all paths matching the pathspec
               without descending into subtrees.

           -z
               Terminate each line with a NUL character rather than a
               newline.

           <revision-range>
               Only traverse commits in the specified revision range. When no
               <revision-range> is specified, it defaults to HEAD (i.e. the
               whole history leading to the current commit). For a complete
               list of ways to spell <revision-range>, see the Specifying
               Ranges section of gitrevisions(7).

           [--] <pathspec>...
               Show the commit that last modified each path matching
               <pathspec>. If no <pathspec> is given, all files and
               subdirectories are included. See gitglossary(7) for details on
               pathspec syntax.

## [](#OUTPUT)OUTPUT

           The output is in the format:

                <oid> TAB <path> LF

           If a path contains any special characters, the path is C-style
           quoted. To avoid quoting, pass option -z to terminate each line
           with a NUL.

                <oid> TAB <path> NUL

## [](#SEE_ALSO)SEE ALSO

           git-blame(1), git-log(1).

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

    Git 2.55.0.493.g5b2471          2026-08-03           GIT-LAST-MODIFIED(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-format-rev(1)](../man1/git-format-rev.1.html)

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
