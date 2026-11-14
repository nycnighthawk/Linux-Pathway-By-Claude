---
{"title": "git-whatchanged(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-whatchanged.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-whatchanged(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [WARNING](#WARNING) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-WHATCHANGED(1)              Git Manual             GIT-WHATCHANGED(1)

## [](#NAME)NAME

           git-whatchanged - Show logs with differences each commit
           introduces

## [](#SYNOPSIS)SYNOPSIS

           git whatchanged <option>...

## [](#WARNING)WARNING

           git whatchanged has been deprecated and is scheduled for removal
           in a future version of Git, as it is merely git log with different
           defaults.

## [](#DESCRIPTION)DESCRIPTION

           Shows commit logs and diff output each commit introduces.

           New users are encouraged to use git-log(1) instead. The
           whatchanged command is essentially the same as git-log(1) but
           defaults to showing the raw format diff output and skipping
           merges:

               git log --raw --no-merges

           The command is primarily kept for historical reasons; fingers of
           many people who learned Git long before git log was invented by
           reading the Linux kernel mailing list are trained to type it.

## [](#EXAMPLES)EXAMPLES

           git whatchanged -p v2.6.12.. include/scsi drivers/scsi
               Show as patches the commits since version v2.6.12 that changed
               any file in the include/scsi or drivers/scsi subdirectories

           git whatchanged --since="2 weeks ago" -- gitk
               Show the changes during the last two weeks to the file gitk.
               The "--" is necessary to avoid confusion with the branch named
               gitk

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

    Git 2.55.0.493.g5b2471          2026-08-03             GIT-WHATCHANGED(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-config(1)](../man1/git-config.1.html),  [git-log(1)](../man1/git-log.1.html),  [git-rev-list(1)](../man1/git-rev-list.1.html)

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
