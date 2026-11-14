---
{"title": "git-sh-i18n(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-sh-i18n.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-sh-i18n(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FUNCTIONS](#FUNCTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-SH-I18N(1)                  Git Manual                 GIT-SH-I18N(1)

## [](#NAME)NAME

           git-sh-i18n - Git's i18n setup code for shell scripts

## [](#SYNOPSIS)SYNOPSIS

           . "$(git --exec-path)/git-sh-i18n"

## [](#DESCRIPTION)DESCRIPTION

           This is not a command the end user would want to run. Ever. This
           documentation is meant for people who are studying the
           Porcelain-ish scripts and/or are writing new ones.

           The 'git sh-i18n scriptlet is designed to be sourced (using .) by
           Git’s porcelain programs implemented in shell script. It provides
           wrappers for the GNU gettext and eval_gettext functions accessible
           through the gettext.sh script, and provides pass-through fallbacks
           on systems without GNU gettext.

## [](#FUNCTIONS)FUNCTIONS

           gettext
               Currently a dummy fall-through function implemented as a
               wrapper around printf(1). Will be replaced by a real gettext
               implementation in a later version.

           eval_gettext
               Currently a dummy fall-through function implemented as a
               wrapper around printf(1) with variables expanded by the
               git-sh-i18n--envsubst(1) helper. Will be replaced by a real
               gettext implementation in a later version.

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

    Git 2.55.0.493.g5b2471          2026-08-03                 GIT-SH-I18N(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-sh-i18n\--envsubst(1)](../man1/git-sh-i18n--envsubst.1.html)

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
