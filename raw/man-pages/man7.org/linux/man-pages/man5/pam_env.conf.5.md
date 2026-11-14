---
{"title": "pam_env.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/pam_env.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_env.conf(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_ENV.CONF(5)              Linux-PAM Manual             PAM_ENV.CONF(5)

## [](#NAME)NAME

           pam_env.conf, environment - the environment variables config files

## [](#DESCRIPTION)DESCRIPTION

           The /usr/share/pam/security/pam_env.conf and
           /etc/security/pam_env.conf files specify the environment variables
           to be set, unset or modified by pam_env(8). When someone logs in,
           these files are read and the environment variables are set
           according.

           Each line starts with the variable name, there are then two
           possible options for each variable DEFAULT and OVERRIDE. DEFAULT
           allows an administrator to set the value of the variable to some
           default value, if none is supplied then the empty string is
           assumed. The OVERRIDE option tells pam_env that it should enter in
           its value (overriding the default value) if there is one to use.
           When OVERRIDE is not used, "" is assumed and no override will be
           done.

           VARIABLE [DEFAULT=[value]] [OVERRIDE=[value]]

           (Possibly non-existent) environment variables may be used in
           values using the ${string} syntax and (possibly non-existent)
           PAM_ITEMs as well as HOME and SHELL may be used in values using
           the @{string} syntax. Both the $ and @ characters can be backslash
           escaped to be used as literal values values can be delimited with
           "", escaped " not supported. Note that many environment variables
           that you would like to use may not be set by the time the module
           is called. For example, ${HOME} is used below several times, but
           many PAM applications don't make it available by the time you need
           it. The special variables @{HOME} and @{SHELL} are expanded to the
           values for the user from the corresponding passwd entry.

           The "#" character at start of line (no space at front) can be used
           to mark this line as a comment line.

           The /usr/share/pam/environment and /etc/environment files specify
           the environment variables to be set. These files must consist of
           simple NAME=VALUE pairs on separate lines. The pam_env(8) module
           will read these files after the pam_env.conf file.

## [](#EXAMPLES)EXAMPLES

           These are some example lines which might be specified in
           /etc/security/pam_env.conf.

           Set the REMOTEHOST variable for any hosts that are remote, default
           to "localhost" rather than not being set at all

                     REMOTEHOST     DEFAULT=localhost OVERRIDE=@{PAM_RHOST}

           Set the DISPLAY variable if it seems reasonable

                     DISPLAY        DEFAULT=${REMOTEHOST}:0.0 OVERRIDE=${DISPLAY}

           Now some simple variables

                     PAGER          DEFAULT=less
                     MANPAGER       DEFAULT=less
                     LESS           DEFAULT="M q e h15 z23 b80"
                     NNTPSERVER     DEFAULT=localhost
                     PATH           DEFAULT=${HOME}/bin:/usr/local/bin:/bin\
                     :/usr/bin:/usr/local/bin/X11:/usr/bin/X11
                     XDG_DATA_HOME  DEFAULT=@{HOME}/share/

           Silly examples of escaped variables, just to show how they work.

                     DOLLAR         DEFAULT=\$
                     DOLLARDOLLAR   DEFAULT=        OVERRIDE=\$${DOLLAR}
                     DOLLARPLUS     DEFAULT=\${REMOTEHOST}${REMOTEHOST}
                     ATSIGN         DEFAULT=""      OVERRIDE=\@

## [](#SEE_ALSO)SEE ALSO

           pam_env(8), pam.d(5), pam(8), environ(7)

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

    Linux-PAM                       08/04/2026                PAM_ENV.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [pam_env(8)](../man8/pam_env.8.html)

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
