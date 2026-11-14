---
{"title": "pam_exec(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_exec.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_exec(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_EXEC(8)                  Linux-PAM Manual                 PAM_EXEC(8)

## [](#NAME)NAME

           pam_exec - PAM module which calls an external command

## [](#SYNOPSIS)SYNOPSIS

           pam_exec.so [debug] [expose_authtok] [seteuid] [quiet] [quiet_log]
                       [stdout] [log=file] [type=type] command [...]

## [](#DESCRIPTION)DESCRIPTION

           pam_exec is a PAM module that can be used to run an external
           command.

           The child's environment is set to the current PAM environment
           list, as returned by pam_getenvlist(3) In addition, the following
           PAM items are exported as environment variables: PAM_RHOST,
           PAM_RUSER, PAM_SERVICE, PAM_TTY, PAM_USER and PAM_TYPE, which
           contains one of the module types: account, auth, password,
           open_session and close_session.

           Commands called by pam_exec need to be aware of that the user can
           have control over the environment.

## [](#OPTIONS)OPTIONS

           debug
               Print debug information.

           expose_authtok
               During authentication and password change the calling command
               can read the password from stdin(3). Only first
               PAM_MAX_RESP_SIZE bytes of a password are provided to the
               command.

           log=file
               The output of the command is appended to file

           type=type
               Only run the command if the module type matches the given
               type.

           stdout
               Per default the output of the executed command is written to
               /dev/null. With this option, the stdout output of the executed
               command is redirected to the calling application. It's in the
               responsibility of this application what happens with the
               output. The log option is ignored.

           quiet
               Per default pam_exec.so will echo the exit status of the
               external command if it fails. Specifying this option will
               suppress the message.

           quiet_log
               Per default pam_exec.so will log the exit status of the
               external command if it fails. Specifying this option will
               suppress the log message.

           seteuid
               Per default pam_exec.so will execute the external command with
               the real user ID of the calling process. Specifying this
               option means the command is run with the effective user ID.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (auth, account, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               The external command was run successfully.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_CONV_ERR
               The conversation method supplied by the application failed to
               obtain the username.

           PAM_INCOMPLETE
               The conversation method supplied by the application returned
               PAM_CONV_AGAIN.

           PAM_SERVICE_ERR
               No argument or a wrong number of arguments were given.

           PAM_SYSTEM_ERR
               A system error occurred or the command to execute failed.

           PAM_IGNORE
               pam_setcred was called, which does not execute the command.
               Or, the value given for the type= parameter did not match the
               module type.

## [](#EXAMPLES)EXAMPLES

           Add the following line to /etc/pam.d/passwd to rebuild the NIS
           database after each local password change:

                       password optional pam_exec.so seteuid /usr/bin/make -C /var/yp

           This will execute the command

               make -C /var/yp

           with effective user ID.

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_exec was written by Thorsten Kukuk <kukuk@thkukuk.de> and Josh
           Triplett <josh@joshtriplett.org>.

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

    Linux-PAM                       08/04/2026                    PAM_EXEC(8)

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
