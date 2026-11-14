---
{"title": "pam_env(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_env.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_env(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_ENV(8)                   Linux-PAM Manual                  PAM_ENV(8)

## [](#NAME)NAME

           pam_env - PAM module to set/unset environment variables

## [](#SYNOPSIS)SYNOPSIS

           pam_env.so [debug] [conffile=conf-file] [envfile=env-file]
                      [readenv=0|1] [user_envfile=env-file]
                      [user_readenv=0|1]

## [](#DESCRIPTION)DESCRIPTION

           The pam_env PAM module allows the (un)setting of environment
           variables. Supported is the use of previously set environment
           variables as well as PAM_ITEMs such as PAM_RHOST.

           By default rules for (un)setting of variables are taken from the
           config file /etc/security/pam_env.conf. If this file does not
           exist /usr/share/pam/security/pam_env.conf is used. An alternate
           file can be specified with the conffile option, which overrules
           all other files.

           Second a file (/etc/environment by default) with simple KEY=VAL
           pairs on separate lines will be read. If this file does not exist,
           /usr/share/pam/etc/environment is used. With the envfile option an
           alternate file can be specified, which overrules all other files.
           And with the readenv option this can be completely disabled.

           Third it will read a user configuration file
           ($HOME/.pam_environment by default). The default file can be
           changed with the user_envfile option and it can be turned on and
           off with the user_readenv option.

           Since setting of PAM environment variables can have side effects
           to other modules, this module should be the last one on the stack.

           This module is only executed if the main application calls
           pam_setcred(3) or pam_open_session(3). The module does nothing and
           returns PAM_IGNORE if called by pam_authenticate(3).

## [](#OPTIONS)OPTIONS

           conffile=/path/to/pam_env.conf
               Indicate an alternative pam_env.conf style configuration file
               to override the default. This can be useful when different
               services need different environments.

           debug
               A lot of debug information is printed with syslog(3).

           envfile=/path/to/environment
               Indicate an alternative environment file to override the
               default. The syntax are simple KEY=VAL pairs on separate
               lines. The export instruction can be specified for bash
               compatibility, but will be ignored. This can be useful when
               different services need different environments.

           readenv=0|1
               Turns on or off the reading of the file specified by envfile
               (0 is off, 1 is on). By default this option is on.

           user_envfile=filename
               Indicate an alternative .pam_environment file to override the
               default. The syntax is the same as for
               /etc/security/pam_env.conf. The filename is relative to the
               user home directory. This can be useful when different
               services need different environments.

           user_readenv=0|1
               Turns on or off the reading of the user specific environment
               file. 0 is off, 1 is on. By default this option is off as user
               supplied environment variables in the PAM environment could
               affect behavior of subsequent modules in the stack without the
               consent of the system administrator.

               Due to problematic security this functionality is deprecated
               since the 1.5.0 version and will be removed completely at some
               point in the future.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           The auth and session module types are provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_ABORT
               Not all relevant data or options could be gotten.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_IGNORE
               No pam_env.conf and environment file was found or the module
               got called by pam_authenticate(3).

           PAM_SUCCESS
               Environment variables were set.

## [](#FILES)FILES

           /usr/share/pam/security/pam_env.conf, /etc/security/pam_env.conf
               Default configuration file

           /usr/share/pam/environment, /etc/environment
               Default environment file

           $HOME/.pam_environment
               User specific environment file

## [](#SEE_ALSO)SEE ALSO

           pam_env.conf(5), pam.d(5), pam(8), environ(7).

## [](#AUTHOR)AUTHOR

           pam_env was written by Dave Kinchlea <kinch@kinch.ark.com>.

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

    Linux-PAM                       08/04/2026                     PAM_ENV(8)

------------------------------------------------------------------------

Pages that refer to this page: [runuser(1)](../man1/runuser.1.html),  [su(1)](../man1/su.1.html),  [pam_env.conf(5)](../man5/pam_env.conf.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [environ(7)](../man7/environ.7.html)

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
