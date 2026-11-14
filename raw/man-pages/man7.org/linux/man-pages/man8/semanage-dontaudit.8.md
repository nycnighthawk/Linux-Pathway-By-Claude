---
{"title": "semanage-dontaudit(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/semanage-dontaudit.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semanage-dontaudit(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    semanage-dontaudit(8)                               semanage-dontaudit(8)

## [](#NAME)NAME

           semanage-dontaudit - SELinux Policy Management dontaudit tool

## [](#SYNOPSIS)SYNOPSIS

           semanage dontaudit [-h] [-S STORE] [-N] {on,off}

## [](#DESCRIPTION)DESCRIPTION

           semanage is used to configure certain elements of SELinux policy
           without requiring modification to or recompilation from policy
           sources.  semanage dontaudit toggles whether or not dontaudit
           rules will be in the policy. Policy writers use dontaudit rules to
           cause confined applications to use alternative paths. Dontaudit
           rules are denied but not reported in the logs. Sometimes dontaudit
           rules can cause bugs in applications but policy writers will not
           realize it since the AVC is not audited. Turn off dontaudit rules
           with this command to see if the kernel is blocking an access.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Show this help message and exit

           -S STORE, --store STORE
                  Select an alternate SELinux Policy Store to manage

           -N, --noreload
                  Do not reload the policy after commit

## [](#EXAMPLE)EXAMPLE

           Turn off dontaudit rules
           # semanage dontaudit off

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

                                     20130617           semanage-dontaudit(8)

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
