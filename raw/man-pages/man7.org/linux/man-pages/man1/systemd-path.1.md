---
{"title": "systemd-path(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-path.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-path(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-PATH(1)                systemd-path               SYSTEMD-PATH(1)

## [](#NAME)NAME

           systemd-path - List and query system and user paths

## [](#SYNOPSIS)SYNOPSIS

           systemd-path [OPTIONS...] [NAME...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-path may be used to query system and user paths. The tool
           makes many of the paths described in file-hierarchy(7) available
           for querying.

           When invoked without arguments, a list of known paths and their
           current values is shown. When at least one argument is passed, the
           path with this name is queried and its value shown. The variables
           whose name begins with "search-" do not refer to individual paths,
           but instead to a list of colon-separated search paths, in their
           order of precedence.

           Note that paths which depend on environment variables are computed
           with systemd-path's invoked environment, and not the system or
           user manager's environment. As such, the output of systemd-path
           may not reflect the behavior of manager processes.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --suffix=
               Printed paths are suffixed by the specified string.

               Added in version 215.

           --no-pager
               Do not pipe output into a pager.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), file-hierarchy(7)

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                         SYSTEMD-PATH(1)

------------------------------------------------------------------------

Pages that refer to this page: [sd-path(3)](../man3/sd-path.3.html),  [sd_path_lookup(3)](../man3/sd_path_lookup.3.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [file-hierarchy(7)](../man7/file-hierarchy.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
