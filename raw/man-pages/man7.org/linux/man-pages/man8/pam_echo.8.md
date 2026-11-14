---
{"title": "pam_echo(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_echo.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_echo(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_ECHO(8)                  Linux-PAM Manual                 PAM_ECHO(8)

## [](#NAME)NAME

           pam_echo - PAM module for printing text messages

## [](#SYNOPSIS)SYNOPSIS

           pam_echo.so [file=/path/message]

## [](#DESCRIPTION)DESCRIPTION

           The pam_echo PAM module is for printing text messages to inform
           user about special things. Sequences starting with the % character
           are interpreted in the following way:

           %H
               The name of the remote host (PAM_RHOST).

           %h
               The name of the local host.

           %s
               The service name (PAM_SERVICE).

           %t
               The name of the controlling terminal (PAM_TTY).

           %U
               The remote user name (PAM_RUSER).

           %u
               The local user name (PAM_USER).

           All other sequences beginning with % expands to the characters
           following the % character.

## [](#OPTIONS)OPTIONS

           file=/path/message
               The content of the file /path/message will be printed with the
               PAM conversion function as PAM_TEXT_INFO.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (auth, account, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_BUF_ERR
               Memory buffer error.

           PAM_SUCCESS
               Message was successful printed.

           PAM_IGNORE
               PAM_SILENT flag was given or message file does not exist, no
               message printed.

## [](#EXAMPLES)EXAMPLES

           For an example of the use of this module, we show how it may be
           used to print information about good passwords:

               password optional pam_echo.so file=/usr/share/doc/good-password.txt
               password required pam_unix.so

## [](#SEE_ALSO)SEE ALSO

           pam.conf(8), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           Thorsten Kukuk <kukuk@thkukuk.de>

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

    Linux-PAM                       08/04/2026                    PAM_ECHO(8)

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
