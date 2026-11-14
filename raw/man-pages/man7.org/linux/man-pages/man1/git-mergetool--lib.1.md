---
{"title": "git-mergetool--lib(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-mergetool--lib.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-mergetool\--lib(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FUNCTIONS](#FUNCTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-MERGETOOL--LIB(1)           Git Manual          GIT-MERGETOOL--LIB(1)

## [](#NAME)NAME

           git-mergetool--lib - Common Git merge tool shell scriptlets

## [](#SYNOPSIS)SYNOPSIS

           TOOL_MODE=(diff|merge) . "$(git --exec-path)/git-mergetool--lib"

## [](#DESCRIPTION)DESCRIPTION

           This is not a command the end user would want to run. Ever. This
           documentation is meant for people who are studying the
           Porcelain-ish scripts and/or are writing new ones.

           The git-mergetool--lib scriptlet is designed to be sourced (using
           .) by other shell scripts to set up functions for working with Git
           merge tools.

           Before sourcing git-mergetool--lib, your script must set TOOL_MODE
           to define the operation mode for the functions listed below. diff
           and merge are valid values.

## [](#FUNCTIONS)FUNCTIONS

           get_merge_tool
               Returns a merge tool. The return code is 1 if we returned a
               guessed merge tool, else 0.  $GIT_MERGETOOL_GUI may be set to
               true to search for the appropriate guitool.

           get_merge_tool_cmd
               Returns the custom command for a merge tool.

           get_merge_tool_path
               Returns the custom path for a merge tool.

           initialize_merge_tool
               Brings merge tool specific functions into scope so they can be
               used or overridden.

           run_merge_tool
               Launches a merge tool given the tool name and a true/false
               flag to indicate whether a merge base is present.  $MERGED,
               $LOCAL, $REMOTE, and $BASE must be defined for use by the
               merge tool.

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

    Git 2.55.0.493.g5b2471          2026-08-03          GIT-MERGETOOL--LIB(1)

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
