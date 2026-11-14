---
{"title": "git-diagnose(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-diagnose.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-diagnose(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-DIAGNOSE(1)                 Git Manual                GIT-DIAGNOSE(1)

## [](#NAME)NAME

           git-diagnose - Generate a zip archive of diagnostic information

## [](#SYNOPSIS)SYNOPSIS

           git diagnose [(-o | --output-directory) <path>] [(-s | --suffix) <format>]
                          [--mode=<mode>]

## [](#DESCRIPTION)DESCRIPTION

           Collects detailed information about the user’s machine, Git
           client, and repository state and packages that information into a
           zip archive. The generated archive can then, for example, be
           shared with the Git mailing list to help debug an issue or serve
           as a reference for independent debugging.

           By default, the following information is captured in the archive:

           •   git version --build-options

           •   The path to the repository root

           •   The available disk space on the filesystem

           •   The name and size of each packfile, including those in
               alternate object stores

           •   The total count of loose objects, as well as counts broken
               down by .git/objects subdirectory

           Additional information can be collected by selecting a different
           diagnostic mode using the --mode option.

           This tool differs from git-bugreport(1) in that it collects much
           more detailed information with a greater focus on reporting the
           size and data shape of repository contents.

## [](#OPTIONS)OPTIONS

           -o <path>, --output-directory <path>
               Place the resulting diagnostics archive in <path> instead of
               the current directory.

           -s <format>, --suffix <format>
               Specify an alternate suffix for the diagnostics archive name,
               to create a file named git-diagnostics-<formatted-suffix>.
               This should take the form of a strftime(3) format string; the
               current local time will be used.

           --mode=(stats|all)
               Specify the type of diagnostics that should be collected. The
               default behavior of git diagnose is equivalent to
               --mode=stats.

               The --mode=all option collects everything included in
               --mode=stats, as well as copies of .git, .git/hooks,
               .git/info, .git/logs, and .git/objects/info directories. This
               additional information may be sensitive, as it can be used to
               reconstruct the full contents of the diagnosed repository.
               Users should exercise caution when sharing an archive
               generated with --mode=all.

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

    Git 2.55.0.493.g5b2471          2026-08-03                GIT-DIAGNOSE(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-bugreport(1)](../man1/git-bugreport.1.html)

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
