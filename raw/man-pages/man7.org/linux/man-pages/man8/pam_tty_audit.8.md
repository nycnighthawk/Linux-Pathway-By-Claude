---
{"title": "pam_tty_audit(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_tty_audit.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_tty_audit(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_TTY_AUDIT(8)             Linux-PAM Manual            PAM_TTY_AUDIT(8)

## [](#NAME)NAME

           pam_tty_audit - Enable or disable TTY auditing for specified users

## [](#SYNOPSIS)SYNOPSIS

           pam_tty_audit.so [disable=patterns] [enable=patterns]

## [](#DESCRIPTION)DESCRIPTION

           The pam_tty_audit PAM module is used to enable or disable TTY
           auditing. By default, the kernel does not audit input on any TTY.

## [](#OPTIONS)OPTIONS

           disable=patterns
               For each user matching patterns, disable TTY auditing. This
               overrides any previous enable option matching the same user
               name on the command line. See NOTES for further description of
               patterns.

           enable=patterns
               For each user matching patterns, enable TTY auditing. This
               overrides any previous disable option matching the same user
               name on the command line. See NOTES for further description of
               patterns.

           open_only
               Set the TTY audit flag when opening the session, but do not
               restore it when closing the session. Using this option is
               necessary for some services that don't fork() to run the
               authenticated session, such as sudo.

           log_passwd
               Log keystrokes when ECHO mode is off but ICANON mode is
               active. This is the mode in which the tty is placed during
               password entry. By default, passwords are not logged. This
               option may not be available on older kernels (3.9?).

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the session type is supported.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SESSION_ERR
               Error reading or modifying the TTY audit flag. See the system
               log for more details.

           PAM_SUCCESS
               Success.

## [](#NOTES)NOTES

           When TTY auditing is enabled, it is inherited by all processes
           started by that user. In particular, daemons restarted by a user
           will still have TTY auditing enabled, and audit TTY input even by
           other users unless auditing for these users is explicitly
           disabled. Therefore, it is recommended to use disable=* as the
           first option for most daemons using PAM.

           To view the data that was logged by the kernel to audit use the
           command aureport --tty.

           The patterns are comma separated lists of glob patterns or ranges
           of uids. A range is specified as min_uid:max_uid where one of
           these values can be empty. If min_uid is empty only user with the
           uid max_uid will be matched. If max_uid is empty users with the
           uid greater than or equal to min_uid will be matched.

           Please note that passwords in some circumstances may be logged by
           TTY auditing even if the log_passwd is not used. For example, all
           input to an ssh session will be logged - even if there is a
           password being typed into some software running at the remote host
           because only the local TTY state affects the local TTY auditing.

## [](#EXAMPLES)EXAMPLES

           Audit all administrative actions.

               session   required pam_tty_audit.so disable=* enable=root

## [](#SEE_ALSO)SEE ALSO

           aureport(8), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_tty_audit was written by Miloslav Trmač <mitr@redhat.com>. The
           log_passwd option was added by Richard Guy Briggs
           <rgb@redhat.com>.

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

    Linux-PAM                       08/04/2026               PAM_TTY_AUDIT(8)

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
