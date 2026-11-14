---
{"title": "sepolicy-manpage(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sepolicy-manpage.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sepolicy-manpage(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sepolicy-manpage(8)                                   sepolicy-manpage(8)

## [](#NAME)NAME

           sepolicy-manpage - Generate a man page based on the installed
           SELinux Policy

## [](#SYNOPSIS)SYNOPSIS

           sepolicy manpage [-w] [-h] [-p PATH ] [-r ROOTDIR ] [-a | -d ]

## [](#DESCRIPTION)DESCRIPTION

           Use sepolicy manpage to generate manpages based on SELinux Policy.

## [](#OPTIONS)OPTIONS

           -a, --all
                  Generate Man Pages for All Domains

           -d, --domain
                  Generate a Man Page for the specified domain. (Supports
                  multiple commands)

           -h, --help
                  Display help message

           -o, --os
                  Specify the name of the OS to be used in the man page (only
                  affects HTML man pages)

           -p, --path
                  Specify the directory to store the created man pages.
                  (Default to /tmp)

           -r, --root
                  Specify alternative root directory to generate man pages
                  from. (Default to /)

           --source_files
                  Use file_contexts and policy.xml files from the specified
                  root directory (the alternative root needs to include both
                  files)

           -w, --web
                  Generate an additional HTML man pages for the specified
                  domain(s)

## [](#EXAMPLE)EXAMPLE

           Generate man pages for all available domains
           # sepolicy manpage -a
           Generate an HTML man page for domain alsa_t, setting the OS name to "My_distro"
           # sepolicy manpage -o My_distro -d alsa_t -w

## [](#AUTHOR)AUTHOR

           This man page was written by Daniel Walsh <dwalsh@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           sepolicy(8), selinux(8)

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                     20121005             sepolicy-manpage(8)

------------------------------------------------------------------------

Pages that refer to this page: [sepolicy(8)](../man8/sepolicy.8.html)

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
