---
{"title": "git-sh-i18n--envsubst(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-sh-i18n--envsubst.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-sh-i18n\--envsubst(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-SH-I18N--ENVSUBST(1)        Git Manual       GIT-SH-I18N--ENVSUBST(1)

## [](#NAME)NAME

           git-sh-i18n--envsubst - Git's own envsubst(1) for i18n fallbacks

## [](#SYNOPSIS)SYNOPSIS

           eval_gettext () {
                   printf "%s" "$1" | (
                           export PATH $(git sh-i18n--envsubst --variables "$1");
                           git sh-i18n--envsubst "$1"
                   )
           }

## [](#DESCRIPTION)DESCRIPTION

           This is not a command the end user would want to run. Ever. This
           documentation is meant for people who are studying the plumbing
           scripts and/or are writing new ones.

           git sh-i18n--envsubst is Git’s stripped-down copy of the GNU
           envsubst(1) program that comes with the GNU gettext package. It’s
           used internally by git-sh-i18n(1) to interpolate the variables
           passed to the eval_gettext function.

           No promises are made about the interface, or that this program
           won’t disappear without warning in the next version of Git. Don’t
           use it.

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

    Git 2.55.0.493.g5b2471          2026-08-03       GIT-SH-I18N--ENVSUBST(1)

------------------------------------------------------------------------

Pages that refer to this page: [git-sh-i18n(1)](../man1/git-sh-i18n.1.html)

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
