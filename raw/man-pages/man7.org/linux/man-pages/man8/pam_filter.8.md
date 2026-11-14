---
{"title": "pam_filter(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_filter.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_filter(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_FILTER(8)                Linux-PAM Manual               PAM_FILTER(8)

## [](#NAME)NAME

           pam_filter - PAM filter module

## [](#SYNOPSIS)SYNOPSIS

           pam_filter.so [debug] [new_term] [non_term] run1|run2 filter [...]

## [](#DESCRIPTION)DESCRIPTION

           This module is intended to be a platform for providing access to
           all of the input/output that passes between the user and the
           application. It is only suitable for tty-based and (stdin/stdout)
           applications.

           To function this module requires filters to be installed on the
           system. The single filter provided with the module simply
           transposes upper and lower case letters in the input and output
           streams. (This can be very annoying and is not kind to termcap
           based editors).

           Each component of the module has the potential to invoke the
           desired filter. The filter is always execv(2) with the privilege
           of the calling application and not that of the user. For this
           reason it cannot usually be killed by the user without closing
           their session.

## [](#OPTIONS)OPTIONS

           debug
               Print debug information.

           new_term
               The default action of the filter is to set the PAM_TTY item to
               indicate the terminal that the user is using to connect to the
               application. This argument indicates that the filter should
               set PAM_TTY to the filtered pseudo-terminal.

           non_term
               don't try to set the PAM_TTY item.

           runX
               In order that the module can invoke a filter it should know
               when to invoke it. This argument is required to tell the
               filter when to do this.

               Permitted values for X are 1 and 2. These indicate the precise
               time that the filter is to be run. To understand this concept
               it will be useful to have read the pam(3) manual page.
               Basically, for each management group there are up to two ways
               of calling the module's functions. In the case of the
               authentication and session components there are actually two
               separate functions. For the case of authentication, these
               functions are pam_authenticate(3) and pam_setcred(3), here
               run1 means run the filter from the pam_authenticate function
               and run2 means run the filter from pam_setcred. In the case of
               the session modules, run1 implies that the filter is invoked
               at the pam_open_session(3) stage, and run2 for
               pam_close_session(3).

               For the case of the account component. Either run1 or run2 may
               be used.

               For the case of the password component, run1 is used to
               indicate that the filter is run on the first occasion of
               pam_chauthtok(3) (the PAM_PRELIM_CHECK phase) and run2 is used
               to indicate that the filter is run on the second occasion (the
               PAM_UPDATE_AUTHTOK phase).

           filter
               The full pathname of the filter to be run and any command line
               arguments that the filter might expect.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (auth, account, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               The new filter was set successfully.

           PAM_ABORT
               Critical error, immediate abort.

## [](#EXAMPLES)EXAMPLES

           Add the following line to /etc/pam.d/login to see how to configure
           login to transpose upper and lower case letters once the user has
           logged in:

                       session required pam_filter.so run1 /lib/security/pam_filter/upperLOWER

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_filter was written by Andrew G. Morgan <morgan@kernel.org>.

## [](#COLOPHON)COLOPHON

           This page is part of the linux-pam (Pluggable Authentication
           Modules for Linux) project.  Information about the project can be
           found at ⟨http://www.linux-pam.org/⟩.  If you have a bug report
           for this manual page, see ⟨//www.linux-pam.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/linux-pam/linux-pam.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux-PAM                       08/04/2026                  PAM_FILTER(8)

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
