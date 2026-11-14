---
{"title": "semanage-module(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/semanage-module.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semanage-module(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    semanage-module(8)                                     semanage-module(8)

## [](#NAME)NAME

           semanage-module - SELinux Policy Management module mapping tool

## [](#SYNOPSIS)SYNOPSIS

           semanage module [-h] [-n] [-N] [-S STORE] (-a | -r | -e | -d |
           --extract | --list [-C] | --deleteall) [module_name]

## [](#DESCRIPTION)DESCRIPTION

           semanage is used to configure certain elements of SELinux policy
           without requiring modification to or recompilation from policy
           sources.  semanage module installs, removes, disables, or enables
           SELinux Policy modules.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Show this help message and exit

           -n, --noheading
                  Do not print heading when listing the specified object type

           -N, --noreload
                  Do not reload policy after commit

           -S STORE, --store STORE
                  Select an alternate SELinux Policy Store to manage

           -a, --add
                  Install specified module. Accepts both binary policy files
                  (.pp) and CIL source files

           -r, --remove
                  Remove specified module

           -D, --deleteall
                  Remove all local customizations related to modules

           -d --disable
                  Disable specified module

           -e --enable
                  Enable specified module

           -E, --extract
                  Extract customizable commands, for use within a transaction

           -l, --list
                  List records of the specified object type

           -C, --locallist
                  List local customizations

## [](#EXAMPLE)EXAMPLE

           List all modules
           # semanage module -l
           Disable unconfined module
           # semanage module --disable unconfined
           Install custom apache policy module (same as #semodule -i myapache.pp)
           # semanage module -a myapache.pp

## [](#SEE_ALSO)SEE ALSO

           selinux(8), semanage(8), semodule(8)

## [](#AUTHOR)AUTHOR

           This man page was written by Daniel Walsh <dwalsh@redhat.com>

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

                                     20130617              semanage-module(8)

------------------------------------------------------------------------

Pages that refer to this page: [semanage(8)](../man8/semanage.8.html)

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
