---
{"title": "show-installed(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/show-installed.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# show-installed(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    show-installed(1)                                       show-installed(1)

## [](#NAME)NAME

           show-installed - show installed RPM packages and descriptions

## [](#SYNOPSIS)SYNOPSIS

           show-installed [options]

## [](#DESCRIPTION)DESCRIPTION

           show-installed gives a compact description of the packages
           installed (or given) making use of the comps groups found in the
           repositories.

## [](#OPTIONS)OPTIONS

           -h, --help
                  show this help message and exit

           -f FORMAT, --format=FORMAT
                  yum, kickstart or human; yum gives the result as a yum
                  command line; kickstart the content of a %packages section;
                  "human" readable is default.

           -i INPUT, --input=INPUT
                  File to read the package list from instead of using the
                  rpmdb. - for stdin. The file must contain package names
                  only separated by white space (including newlines). rpm -qa
                  --qf='%{name}\n' produces proper output.

           -o OUTPUT, --output=OUTPUT
                  File to write the result to. Stdout is used if option is
                  omitted.

           -q, --quiet
                  Do not show warnings.

           -e, --no-excludes
                  Only show groups that are installed completely. Do not use
                  exclude lines.

           --global-excludes
                  Print exclude lines at the end and not after the groups
                  requiring them.

           --global-addons
                  Print package names at the end and not after the groups
                  offering them as addon.

           --addons-by-group
                  Also show groups not selected to sort packages contained by
                  them. Those groups are commented out with a "# " at the
                  begin of the line.

           -m, --allow-mandatories
                  Check if just installing the mandatory packages gives
                  better results. Uses "." to mark those groups.

           -a, --allow-all
                  Check if installing all packages in the groups gives better
                  results. Uses "*" to mark those groups.

           --ignore-missing
                  Ignore packages missing in the repos.

           --ignore-missing-excludes
                  Do not produce exclude lines for packages not in the
                  repository.

## [](#COLOPHON)COLOPHON

           This page is part of the yum-utils (Yum Package Manager utilities)
           project.  Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/yum⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/yum-utils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2020-03-11.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Florian Festi                21 October 2010            show-installed(1)

------------------------------------------------------------------------

Pages that refer to this page: [yum-utils(1)](../man1/yum-utils.1.html)

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
