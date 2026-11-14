---
{"title": "pam_loginuid(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_loginuid.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_loginuid(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_LOGINUID(8)              Linux-PAM Manual             PAM_LOGINUID(8)

## [](#NAME)NAME

           pam_loginuid - Record user's login uid to the process attribute

## [](#SYNOPSIS)SYNOPSIS

           pam_loginuid.so [require_auditd]

## [](#DESCRIPTION)DESCRIPTION

           The pam_loginuid module sets the loginuid process attribute for
           the process that was authenticated. This is necessary for
           applications to be correctly audited. This PAM module should only
           be used for entry point applications like: login, sshd, gdm,
           vsftpd, crond and atd. There are probably other entry point
           applications besides these. You should not use it for applications
           like sudo or su as that defeats the purpose by changing the
           loginuid to the account they just switched to.

## [](#OPTIONS)OPTIONS

           require_auditd
               This option, when given, will cause this module to query the
               audit daemon status and deny logins if it is not running.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the session module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               The loginuid value is set and auditd is running if check
               requested.

           PAM_IGNORE
               The /proc/self/loginuid file is not present on the system or
               the login process runs inside uid namespace and kernel does
               not support overwriting loginuid.

           PAM_SESSION_ERR
               Any other error prevented setting loginuid or auditd is not
               running.

## [](#EXAMPLES)EXAMPLES

               #%PAM-1.0
               auth       required     pam_unix.so
               auth       required     pam_nologin.so
               account    required     pam_unix.so
               password   required     pam_unix.so
               session    required     pam_unix.so
               session    required     pam_loginuid.so

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8), auditctl(8), auditd(8)

## [](#AUTHOR)AUTHOR

           pam_loginuid was written by Steve Grubb <sgrubb@redhat.com>

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

    Linux-PAM                       08/04/2026                PAM_LOGINUID(8)

------------------------------------------------------------------------

Pages that refer to this page: [audit_setloginuid(3)](../man3/audit_setloginuid.3.html),  [ausearch(8)](../man8/ausearch.8.html),  [pam_systemd(8)](../man8/pam_systemd.8.html)

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
