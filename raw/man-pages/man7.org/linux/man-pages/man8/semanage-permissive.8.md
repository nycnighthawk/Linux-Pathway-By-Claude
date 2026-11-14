---
{"title": "semanage-permissive(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/semanage-permissive.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semanage-permissive(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    semanage-permissive(8)                             semanage-permissive(8)

## [](#NAME)NAME

           semanage-permissive - SELinux Policy Management permissive mapping
           tool

## [](#SYNOPSIS)SYNOPSIS

           semanage permissive [-h] [-n] [-N] [-S STORE] (--add TYPE |
           --delete TYPE | --deleteall | --extract | --list)

## [](#DESCRIPTION)DESCRIPTION

           semanage is used to configure certain elements of SELinux policy
           without requiring modification to or recompilation from policy
           sources.  semanage permissive adds or removes a SELinux Policy
           permissive module. Please note that this command can make any
           domain permissive, but can only remove the permissive property
           from domains where it was added by semanage permissive ("semanage
           permissive -d" can only be used on types listed as "Customized
           Permissive Types" by "semanage permissive -l").

## [](#OPTIONS)OPTIONS

           -h, --help
                  Show this help message and exit

           -a, --add
                  Add a record of the specified object type

           -d, --delete
                  Delete a record of the specified object type

           -D, --deleteall
                  Remove all local customizations of permissive domains

           -l, --list
                  List records of the specified object type

           -E, --extract
                  Extract customizable commands, for use within a transaction

           -n, --noheading
                  Do not print heading when listing the specified object type

           -N, --noreload
                  Do not reload the policy after commit

           -S STORE, --store STORE
                  Select an alternate SELinux Policy Store to manage

## [](#EXAMPLE)EXAMPLE

           List all permissive domains ("Builtin Permissive Types" where set by the system policy, or a custom policy module)
           # semanage permissive -l
           Make httpd_t (Web Server) a permissive domain
           # semanage permissive -a httpd_t

## [](#SEE_ALSO)SEE ALSO

           selinux(8), semanage(8)

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

                                     20130617          semanage-permissive(8)

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
