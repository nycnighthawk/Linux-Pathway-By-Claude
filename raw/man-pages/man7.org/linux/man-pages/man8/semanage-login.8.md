---
{"title": "semanage-login(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/semanage-login.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semanage-login(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    semanage-login(8)                                       semanage-login(8)

## [](#NAME)NAME

           semanage-login - SELinux Policy Management linux user to SELinux
           User mapping tool

## [](#SYNOPSIS)SYNOPSIS

           semanage login [-h] [-n] [-N] [-S STORE] [ --add -s SEUSER -r
           RANGE LOGIN | --delete LOGIN | --deleteall | --extract | --list
           [-C] | --modify -s SEUSER -r RANGE LOGIN ]

## [](#DESCRIPTION)DESCRIPTION

           semanage is used to configure certain elements of SELinux policy
           without requiring modification to or recompilation from policy
           sources.  semanage login controls the mapping between a Linux User
           and the SELinux User. It can be used to turn on confined users.
           For example you could define that a particular user or group of
           users will login to a system as the user_u user. Prefix the group
           name with a '%' sign to indicate a group name.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Show this help message and exit

           -n, --noheading
                  Do not print heading when listing the specified object type

           -N, --noreload
                  Do not reload policy after commit

           -C, --locallist
                  List local customizations

           -S STORE, --store STORE
                  Select an alternate SELinux Policy Store to manage

           -a, --add
                  Add a record of the specified object type

           -d, --delete
                  Delete a record of the specified object type

           -m, --modify
                  Modify a record of the specified object type

           -l, --list
                  List records of the specified object type

           -E, --extract
                  Extract customizable commands, for use within a transaction

           -D, --deleteall
                  Remove all local customizations

           -s SEUSER, --seuser SEUSER
                  SELinux user name

           -r RANGE, --range RANGE
                  MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range
                  for SELinux login mapping defaults to the SELinux user
                  record range. SELinux Range for SELinux user defaults to
                  s0.

## [](#EXAMPLE)EXAMPLE

           Set the default SELinux user on the system to guest_u
           # semanage login -m -s guest_u __default__
           Map user gijoe to SELinux user staff_u and assign MLS range SystemLow-Secret
           # semanage login -a -s staff_u -rSystemLow-Secret gijoe
           Map all users in the engineering group to SELinux user staff_u
           # semanage login -a -s staff_u %engineering

## [](#SEE_ALSO)SEE ALSO

           selinux(8), semanage(8), semanage-user(8)

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

                                     20130617               semanage-login(8)

------------------------------------------------------------------------

Pages that refer to this page: [semanage(8)](../man8/semanage.8.html),  [semanage-user(8)](../man8/semanage-user.8.html)

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
