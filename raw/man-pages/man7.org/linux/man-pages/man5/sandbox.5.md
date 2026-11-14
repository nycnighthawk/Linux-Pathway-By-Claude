---
{"title": "sandbox(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/sandbox.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sandbox(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sandbox.conf(5)        Linux System Administration        sandbox.conf(5)

## [](#NAME)NAME

           sandbox.conf - user config file for the SELinux sandbox

## [](#DESCRIPTION)DESCRIPTION

           When running sandbox with the -C argument, it will be confined
           using control groups and a system administrator can specify how
           the sandbox is confined.

           Everything after "#" is ignored, as are empty lines.  All
           arguments should be separated by and equals sign ("=").

           These keywords are allowed.

                  NAME   The name of the sandbox control group.  Default is
                         "sandbox".

                  CPUAFFINITY
                         Which cpus to assign sandbox to.  The default is
                         ALL, but users can specify a comma-separated list
                         with dashes ("-") to represent ranges.  Ex: 0-2,5

                  MEMUSAGE
                         How much memory to allow sandbox to use.  The
                         default is 80%.  Users can specify either a
                         percentage or a value in the form of a number
                         followed by one of the suffixes K, M, G to denote
                         kilobytes, megabytes or gigabytes respectively.  Ex:
                         50% or 100M

                  CPUUSAGE
                         Percentage of cpu sandbox should be allowed to use.
                         The default is 80%.  Specify a value followed by a
                         percent sign ("%"). Ex: 50%

## [](#SEE_ALSO)SEE ALSO

           sandbox(8)

## [](#AUTHOR)AUTHOR

           This manual page was written by Thomas Liu
           <tliu@fedoraproject.org>

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

    sandbox.conf                    June 2010                 sandbox.conf(5)

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
