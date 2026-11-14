---
{"title": "stg-sink(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-sink.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-sink(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-SINK(1)                    StGit Manual                   STG-SINK(1)

## [](#NAME)NAME

           stg-sink - Move patches deeper in the stack

## [](#SYNOPSIS)SYNOPSIS

           stg sink [OPTIONS] [patch]...

## [](#DESCRIPTION)DESCRIPTION

           Move the specified patches down the stack.

           If no patch is specified on the command line, the current
           (topmost) patch is sunk. By default, patches are sunk to the
           bottom of the stack, but the --above or --below (alias --to)
           options may be used to place them above or below any applied
           patch.

           Internally, sinking involves popping all patches to the bottom (or
           to the target patch if --above or --below is used), then pushing
           the patches to sink, and then, unless --nopush is specified,
           pushing back any other formerly applied patches.

           Sinking may be useful, for example, to group stable patches at the
           bottom of the stack where they less likely to be impacted by the
           push of another patch, and from where they can be more easily
           committed or pushed to another repository.

## [](#OPTIONS)OPTIONS

           -n, --nopush
               Do not push any formerly applied patches after sinking. Only
               the patches to sink are pushed.

           -t <target>, --below=<target>, --to=<target>
               Sink patches below <target> patch.

               Specified patches are placed below <target> instead of at the
               bottom of the stack.

           -T <target>, --above=<target>
               Sink patches above <target> patch.

               Specified patches are placed above <target> instead of at the
               bottom of the stack.

           -k, --keep
               Keep the local changes

           --committer-date-is-author-date
               Instead of using the current time as the committer date, use
               the author date of the commit as the committer date.

## [](#STGIT)STGIT

           Part of the StGit suite - see stg(1)

## [](#COLOPHON)COLOPHON

           This page is part of the stgit (Stacked Git) project.  Information
           about the project can be found at ⟨http://www.procode.org/stgit/⟩.
           If you have a bug report for this manual page, see
           ⟨http://www.procode.org/stgit/⟩.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/stacked-git/stgit.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-19.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    StGit 2.6.1                     08/04/2026                    STG-SINK(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg(1)](../man1/stg.1.html)

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
