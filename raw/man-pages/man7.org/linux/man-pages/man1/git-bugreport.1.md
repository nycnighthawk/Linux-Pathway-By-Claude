---
{"title": "git-bugreport(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-bugreport.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-bugreport(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-BUGREPORT(1)                Git Manual               GIT-BUGREPORT(1)

## [](#NAME)NAME

           git-bugreport - Collect information for user to file a bug report

## [](#SYNOPSIS)SYNOPSIS

           git bugreport [(-o | --output-directory) <path>]
                           [(-s | --suffix) <format> | --no-suffix]
                           [--diagnose[=<mode>]]

## [](#DESCRIPTION)DESCRIPTION

           Collects information about the user’s machine, Git client, and
           repository state, in addition to a form requesting information
           about the behavior the user observed, and stores it in a single
           text file which the user can then share, for example to the Git
           mailing list, in order to report an observed bug.

           The following information is requested from the user:

           •   Reproduction steps

           •   Expected behavior

           •   Actual behavior

           The following information is captured automatically:

           •   git version --build-options

           •   uname sysname, release, version, and machine strings

           •   Compiler-specific info string

           •   A list of enabled hooks

           •   $SHELL

           Additional information may be gathered into a separate zip archive
           using the --diagnose option, and can be attached alongside the
           bugreport document to provide additional context to readers.

           This tool is invoked via the typical Git setup process, which
           means that in some cases, it might not be able to launch - for
           example, if a relevant config file is unreadable. In this kind of
           scenario, it may be helpful to manually gather the kind of
           information listed above when manually asking for help.

## [](#OPTIONS)OPTIONS

           -o <path>, --output-directory <path>
               Place the resulting bug report file in <path> instead of the
               current directory.

           -s <format>, --suffix <format>, --no-suffix
               Specify an alternate suffix for the bugreport name, to create
               a file named git-bugreport-<formatted-suffix>. This should
               take the form of a strftime(3) format string; the current
               local time will be used.  --no-suffix disables the suffix and
               the file is just named git-bugreport without any
               disambiguation measure.

           --no-diagnose, --diagnose[=<mode>]
               Create a zip archive of supplemental information about the
               user’s machine, Git client, and repository state. The archive
               is written to the same output directory as the bug report and
               is named git-diagnostics-<formatted-suffix>.

               Without mode specified, the diagnostic archive will contain
               the default set of statistics reported by git diagnose. An
               optional mode value may be specified to change which
               information is included in the archive. See git-diagnose(1)
               for the list of valid values for mode and details about their
               usage.

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

    Git 2.55.0.493.g5b2471          2026-08-03               GIT-BUGREPORT(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-diagnose(1)](../man1/git-diagnose.1.html)

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
