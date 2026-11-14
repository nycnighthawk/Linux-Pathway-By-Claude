---
{"title": "faillock.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/faillock.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# faillock.conf(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FAILLOCK.CONF(5)             Linux-PAM Manual            FAILLOCK.CONF(5)

## [](#NAME)NAME

           faillock.conf - pam_faillock configuration file

## [](#DESCRIPTION)DESCRIPTION

           faillock.conf provides a way to configure the default settings for
           locking the user after multiple failed authentication attempts.
           This file is read by the pam_faillock module and is the preferred
           method over configuring pam_faillock directly.

           The file has a very simple name = value format with possible
           comments starting with # character. The whitespace at the
           beginning of line, end of line, and around the = sign is ignored.

## [](#OPTIONS)OPTIONS

           dir=/path/to/tally-directory
               The directory where the user files with the failure records
               are kept. The default is /var/run/faillock.

               Note: These files will disappear after reboot on systems
               configured with directory /var/run/faillock mounted on virtual
               memory.

           audit
               Will log the user name into the system log if the user is not
               found.

           silent
               Don't print informative messages to the user. Please note that
               when this option is not used there will be difference in the
               authentication behavior for users which exist on the system
               and non-existing users.

           no_log_info
               Don't log informative messages via syslog(3).

           local_users_only
               Only track failed user authentications attempts for local
               users in /etc/passwd and ignore centralized (AD, IdM, LDAP,
               etc.) users. The faillock(8) command will also no longer track
               user failed authentication attempts. Enabling this option will
               prevent a double-lockout scenario where a user is locked out
               locally and in the centralized mechanism.

           nodelay
               Don't enforce a delay after authentication failures.

           deny=n
               Deny access if the number of consecutive authentication
               failures for this user during the recent interval exceeds n.
               The default is 3.

           fail_interval=n
               The length of the interval during which the consecutive
               authentication failures must happen for the user account lock
               out is n seconds. The default is 900 (15 minutes).

           unlock_time=n
               The access will be re-enabled after n seconds after the lock
               out. The value 0 has the same meaning as value never - the
               access will not be re-enabled without resetting the faillock
               entries by the faillock(8) command. The default is 600 (10
               minutes).

               Note that the default directory that pam_faillock uses is
               usually cleared on system boot so the access will be also
               re-enabled after system reboot. If that is undesirable a
               different tally directory must be set with the dir option.

               Also note that it is usually undesirable to permanently lock
               out users as they can become easily a target of denial of
               service attack unless the usernames are random and kept secret
               to potential attackers.

           even_deny_root
               Root account can become locked as well as regular accounts.

           root_unlock_time=n
               This option implies even_deny_root option. Allow access after
               n seconds to root account after the account is locked. In case
               the option is not specified the value is the same as of the
               unlock_time option.

           admin_group=name
               If a group name is specified with this option, members of the
               group will be handled by this module the same as the root
               account (the options even_deny_root and root_unlock_time will
               apply to them. By default the option is not set.

## [](#EXAMPLES)EXAMPLES

           /etc/security/faillock.conf file example:

               deny=4
               unlock_time=1200
               silent

## [](#FILES)FILES

           /etc/security/faillock.conf
               the config file for custom options

## [](#SEE_ALSO)SEE ALSO

           faillock(8), pam_faillock(8), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_faillock was written by Tomas Mraz. The support for
           faillock.conf was written by Brian Ward.

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

    Linux-PAM                       08/04/2026               FAILLOCK.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [pam_faillock(8)](../man8/pam_faillock.8.html)

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
