---
{"title": "run_init(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/run_init.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# run_init(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RUN_INIT(8)              System Manager's Manual              RUN_INIT(8)

## [](#NAME)NAME

           run_init - run an init script in the proper SELinux context

## [](#SYNOPSIS)SYNOPSIS

           run_init SCRIPT [[ARGS]...]

## [](#DESCRIPTION)DESCRIPTION

           Run a init script under the proper context, which is specified in
           /etc/selinux/POLICYTYPE/contexts/initrc_context.  It is generally
           used interactively as it requires either shadow or PAM user
           authentication (depending on compile-time options).  It should be
           possible to configure PAM such that interactive input is not
           required.  Check your PAM documentation.

## [](#FILES)FILES

           /etc/passwd - user account information
           /etc/shadow - encrypted passwords and age information
           /etc/selinux/POLICYTYPE/contexts/initrc_context - contains the
           context to run init scripts under

## [](#SEE_ALSO)SEE ALSO

           newrole(1), runcon(1)

## [](#AUTHORS)AUTHORS

           Wayne Salamon (wsalamon@tislabs.com)
           Dan Walsh (dwalsh@redhat.com)

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

    Security Enhanced Linux          May 2003                     RUN_INIT(8)

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
