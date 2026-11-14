---
{"title": "PAM(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PAM(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM(8)                       Linux-PAM Manual                      PAM(8)

## [](#NAME)NAME

           PAM, pam - Pluggable Authentication Modules for Linux

## [](#DESCRIPTION)DESCRIPTION

           This manual is intended to offer a quick introduction to
           Linux-PAM. For more information the reader is directed to the
           Linux-PAM system administrators' guide.

           Linux-PAM is a system of libraries that handle the authentication
           tasks of applications (services) on the system. The library
           provides a stable general interface (Application Programming
           Interface - API) that privilege granting programs (such as
           login(1) and su(1)) defer to to perform standard authentication
           tasks.

           The principal feature of the PAM approach is that the nature of
           the authentication is dynamically configurable. In other words,
           the system administrator is free to choose how individual
           service-providing applications will authenticate users. This
           dynamic configuration is set by the contents of the single
           Linux-PAM configuration file /etc/pam.conf. Alternatively and
           preferably, the configuration can be set by individual
           configuration files located in a pam.d directory. The presence of
           this directory will cause Linux-PAM to ignore /etc/pam.conf.

           Vendor-supplied PAM configuration files might be installed in the
           system directory /usr/lib/pam.d/ or a configurable vendor specific
           directory instead of the machine configuration directory
           /etc/pam.d/. If no machine configuration file is found, the
           vendor-supplied file is used. All files in /etc/pam.d/ override
           files with the same name in other directories.

           From the point of view of the system administrator, for whom this
           manual is provided, it is not of primary importance to understand
           the internal behavior of the Linux-PAM library. The important
           point to recognize is that the configuration file(s) define the
           connection between applications (services) and the pluggable
           authentication modules (PAMs) that perform the actual
           authentication tasks.

           Linux-PAM separates the tasks of authentication into four
           independent management groups: account management; authentication
           management; password management; and session management. (We
           highlight the abbreviations used for these groups in the
           configuration file.)

           Simply put, these groups take care of different aspects of a
           typical user's request for a restricted service:

           account - provide account verification types of service: has the
           user's password expired?; is this user permitted access to the
           requested service?

           authentication - authenticate a user and set up user credentials.
           Typically this is via some challenge-response request that the
           user must satisfy: if you are who you claim to be please enter
           your password. Not all authentications are of this type, there
           exist hardware based authentication schemes (such as the use of
           smart-cards and biometric devices), with suitable modules, these
           may be substituted seamlessly for more standard approaches to
           authentication - such is the flexibility of Linux-PAM.

           password - this group's responsibility is the task of updating
           authentication mechanisms. Typically, such services are strongly
           coupled to those of the auth group. Some authentication mechanisms
           lend themselves well to being updated with such a function.
           Standard UN*X password-based access is the obvious example: please
           enter a replacement password.

           session - this group of tasks cover things that should be done
           prior to a service being given and after it is withdrawn. Such
           tasks include the maintenance of audit trails and the mounting of
           the user's home directory. The session management group is
           important as it provides both an opening and closing hook for
           modules to affect the services available to a user.

## [](#FILES)FILES

           /etc/pam.conf
               the configuration file

           /etc/pam.d
               the Linux-PAM configuration directory. Generally, if this
               directory is present, the /etc/pam.conf file is ignored.

           /usr/lib/pam.d
               the Linux-PAM vendor configuration directory. Files in
               /etc/pam.d override files with the same name in this
               directory.

           /usr/share/pam/pam.d
               additional Linux-PAM vendor configuration directory. Files in
               /etc/pam.d and /usr/lib/pam.d override files with the same
               name in this directory.

## [](#ERRORS)ERRORS

           Typically errors generated by the Linux-PAM system of libraries,
           will be written to syslog(3).

## [](#CONFORMING_TO)CONFORMING TO

           DCE-RFC 86.0, October 1995. Contains additional features, but
           remains backwardly compatible with this RFC.

## [](#SEE_ALSO)SEE ALSO

           pam(3), pam_authenticate(3), pam_sm_setcred(3), pam_strerror(3)

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

    Linux-PAM                       08/04/2026                         PAM(8)

------------------------------------------------------------------------

Pages that refer to this page: [runuser(1)](../man1/runuser.1.html),  [su(1)](../man1/su.1.html),  [misc_conv(3)](../man3/misc_conv.3.html),  [pam_acct_mgmt(3)](../man3/pam_acct_mgmt.3.html),  [pam_authenticate(3)](../man3/pam_authenticate.3.html),  [pam_chauthtok(3)](../man3/pam_chauthtok.3.html),  [pam_conv(3)](../man3/pam_conv.3.html),  [pam_error(3)](../man3/pam_error.3.html),  [pam_get_authtok(3)](../man3/pam_get_authtok.3.html),  [pam_getenv(3)](../man3/pam_getenv.3.html),  [pam_getenvlist(3)](../man3/pam_getenvlist.3.html),  [pam_info(3)](../man3/pam_info.3.html),  [pam_misc_drop_env(3)](../man3/pam_misc_drop_env.3.html),  [pam_misc_paste_env(3)](../man3/pam_misc_paste_env.3.html),  [pam_misc_setenv(3)](../man3/pam_misc_setenv.3.html),  [pam_prompt(3)](../man3/pam_prompt.3.html),  [pam_putenv(3)](../man3/pam_putenv.3.html),  [pam_sm_acct_mgmt(3)](../man3/pam_sm_acct_mgmt.3.html),  [pam_sm_authenticate(3)](../man3/pam_sm_authenticate.3.html),  [pam_sm_chauthtok(3)](../man3/pam_sm_chauthtok.3.html),  [pam_sm_close_session(3)](../man3/pam_sm_close_session.3.html),  [pam_sm_open_session(3)](../man3/pam_sm_open_session.3.html),  [pam_sm_setcred(3)](../man3/pam_sm_setcred.3.html),  [pam_strerror(3)](../man3/pam_strerror.3.html),  [pam_syslog(3)](../man3/pam_syslog.3.html),  [access.conf(5)](../man5/access.conf.5.html),  [capsule@.service(5)](../man5/capsule@.service.5.html),  [default_contexts(5)](../man5/default_contexts.5.html),  [faillock.conf(5)](../man5/faillock.conf.5.html),  [failsafe_context(5)](../man5/failsafe_context.5.html),  [group.conf(5)](../man5/group.conf.5.html),  [limits.conf(5)](../man5/limits.conf.5.html),  [login.defs(5)](../man5/login.defs.5.html),  [namespace.conf(5)](../man5/namespace.conf.5.html),  [pam.conf(5)](../man5/pam.conf.5.html),  [pam_env.conf(5)](../man5/pam_env.conf.5.html),  [pwhistory.conf(5)](../man5/pwhistory.conf.5.html),  [selinux_config(5)](../man5/selinux_config.5.html),  [sepermit.conf(5)](../man5/sepermit.conf.5.html),  [service_seusers(5)](../man5/service_seusers.5.html),  [seusers(5)](../man5/seusers.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [time.conf(5)](../man5/time.conf.5.html),  [user_contexts(5)](../man5/user_contexts.5.html),  [user@.service(5)](../man5/user@.service.5.html),  [environ(7)](../man7/environ.7.html),  [cron(8)](../man8/cron.8.html),  [faillock(8)](../man8/faillock.8.html),  [pam_access(8)](../man8/pam_access.8.html),  [pam_canonicalize_user(8)](../man8/pam_canonicalize_user.8.html),  [pam_cap(8)](../man8/pam_cap.8.html),  [pam_debug(8)](../man8/pam_debug.8.html),  [pam_deny(8)](../man8/pam_deny.8.html),  [pam_echo(8)](../man8/pam_echo.8.html),  [pam_env(8)](../man8/pam_env.8.html),  [pam_exec(8)](../man8/pam_exec.8.html),  [pam_faildelay(8)](../man8/pam_faildelay.8.html),  [pam_faillock(8)](../man8/pam_faillock.8.html),  [pam_filter(8)](../man8/pam_filter.8.html),  [pam_ftp(8)](../man8/pam_ftp.8.html),  [pam_group(8)](../man8/pam_group.8.html),  [pam_issue(8)](../man8/pam_issue.8.html),  [pam_keyinit(8)](../man8/pam_keyinit.8.html),  [pam_lastlog2(8)](../man8/pam_lastlog2.8.html),  [pam_limits(8)](../man8/pam_limits.8.html),  [pam_listfile(8)](../man8/pam_listfile.8.html),  [pam_localuser(8)](../man8/pam_localuser.8.html),  [pam_loginuid(8)](../man8/pam_loginuid.8.html),  [pam_mail(8)](../man8/pam_mail.8.html),  [pam_mkhomedir(8)](../man8/pam_mkhomedir.8.html),  [pam_motd(8)](../man8/pam_motd.8.html),  [pam_namespace(8)](../man8/pam_namespace.8.html),  [pam_nologin(8)](../man8/pam_nologin.8.html),  [pam_permit(8)](../man8/pam_permit.8.html),  [pam_pwhistory(8)](../man8/pam_pwhistory.8.html),  [pam_rhosts(8)](../man8/pam_rhosts.8.html),  [pam_rootok(8)](../man8/pam_rootok.8.html),  [pam_securetty(8)](../man8/pam_securetty.8.html),  [pam_selinux(8)](../man8/pam_selinux.8.html),  [pam_sepermit(8)](../man8/pam_sepermit.8.html),  [pam_setquota(8)](../man8/pam_setquota.8.html),  [pam_shells(8)](../man8/pam_shells.8.html),  [pam_stress(8)](../man8/pam_stress.8.html),  [pam_succeed_if(8)](../man8/pam_succeed_if.8.html),  [pam_systemd(8)](../man8/pam_systemd.8.html),  [pam_systemd_home(8)](../man8/pam_systemd_home.8.html),  [pam_time(8)](../man8/pam_time.8.html),  [pam_timestamp(8)](../man8/pam_timestamp.8.html),  [pam_timestamp_check(8)](../man8/pam_timestamp_check.8.html),  [pam_tty_audit(8)](../man8/pam_tty_audit.8.html),  [pam_umask(8)](../man8/pam_umask.8.html),  [pam_unix(8)](../man8/pam_unix.8.html),  [pam_userdb(8)](../man8/pam_userdb.8.html),  [pam_usertype(8)](../man8/pam_usertype.8.html),  [pam_warn(8)](../man8/pam_warn.8.html),  [pam_wheel(8)](../man8/pam_wheel.8.html),  [pam_xauth(8)](../man8/pam_xauth.8.html)

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
