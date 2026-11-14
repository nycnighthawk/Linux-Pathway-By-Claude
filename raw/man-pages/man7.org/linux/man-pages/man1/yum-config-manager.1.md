---
{"title": "yum-config-manager(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/yum-config-manager.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-config-manager(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ADDITIONAL OPTIONS](#ADDITIONAL_OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yum-config-manager(1)                               yum-config-manager(1)

## [](#NAME)NAME

           yum-config-manager - manage yum configuration options and yum
           repositories

## [](#SYNOPSIS)SYNOPSIS

           yum-config-manager [options] [section ...]

## [](#DESCRIPTION)DESCRIPTION

           yum-config-manager is a program that can manage main yum
           configuration options, toggle which repositories are enabled or
           disabled, and add new repositories.

           Unless --add-repo is used, the program will output the current
           configuration of the selected sections, and optionally save it
           back to the corresponding files.

           By default, if no positional arguments are specified, the program
           will select the [main] section and each enabled repository.  You
           can override this by specifying your own list of sections as
           arguments (these may also include disabled repositories).  A
           section can either be main or a repoid.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Display a help message, and then quit.

           --setopt=option=value
                  Set any config option in yum config or repo files. For
                  options in the global config just use:
                  --setopt=option=value for repo options use:
                  --setopt=repoid.option=value.  The latter form accepts
                  wildcards in repoid that will be expanded to the selected
                  sections.  If repoid contains no wildcard, it will
                  automatically be selected; this is useful if you are
                  addressing a disabled repo, in which case you don't have to
                  additionally pass it as an argument.

           --save Save the current options (useful with --setopt).

           --enable
                  Enable the specified repos (automatically saves). To enable
                  all repositories run "yum-config-manager --enable \*".

           --disable
                  Disable the specified repos (automatically saves). To
                  disable all repositories run "yum-config-manager --disable
                  \*".

           --add-repo=ADDREPO
                  Add (and enable) the repo from the specified file or url.

## [](#ADDITIONAL_OPTIONS)ADDITIONAL OPTIONS

           Yum-config-manager inherits all other options from yum. See the
           yum(8) man page for more information.

## [](#EXAMPLES)EXAMPLES

           Show the configuration of [main] and the repos foo and bar:

                  yum-config-manager main foo bar

           Enable the repos foo and bar:

                  yum-config-manager --enable foo bar

           Change a global option:

                  yum-config-manager --setopt=installonly_limit=5 --save

           Change a repo option of the repo foo (works even if foo is
           disabled):

                  yum-config-manager --setopt=foo.skip_if_unavailable=1
                  --save

           Change a repo option of more repos at once:

                  yum-config-manager --setopt=\*.skip_if_unavailable=1 --save
                  foo bar baz

           Change a repo option of all the enabled repos:

                  yum-config-manager --setopt=\*.skip_if_unavailable=1 --save

           Change a repo option of all the configured (that is, enabled and
           disabled) repos:

                  yum-config-manager --setopt=\*.skip_if_unavailable=1 --save
                  \*

## [](#SEE_ALSO)SEE ALSO

           yum.conf(5)
           http://yum.baseurl.org/

## [](#AUTHORS)AUTHORS

           See the Authors file included with this program.

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

                                 13 January 2013        yum-config-manager(1)

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
