---
{"title": "pam_access(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_access.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_access(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_ACCESS(8)                Linux-PAM Manual               PAM_ACCESS(8)

## [](#NAME)NAME

           pam_access - PAM module for logdaemon style login access control

## [](#SYNOPSIS)SYNOPSIS

           pam_access.so [debug] [noaudit] [nodefgroup] [nodns] [quiet_log]
                         [accessfile=file] [fieldsep=sep] [listsep=sep]

## [](#DESCRIPTION)DESCRIPTION

           The pam_access PAM module is mainly for access management. It
           provides logdaemon style login access control based on login
           names, host or domain names, internet addresses or network
           numbers, or on terminal line names, X $DISPLAY values, or PAM
           service names in case of non-networked logins.

           By default rules for access management are taken from config file
           /etc/security/access.conf or, if that one is not present, the file
           /usr/share/pam/security/access.conf. These settings can be
           overruled by setting in a config file explicitly specified with
           the accessfile option. Then individual *.conf files from the
           /etc/security/access.d/ and /usr/share/pam/security/access.d
           directories are read. If /etc/security/access.d/@filename@.conf
           exists, then /usr/share/pam/security/access.d/@filename@.conf will
           not be used. All access.d/*.conf files are sorted by their
           @filename@.conf in lexicographic order regardless of which of the
           directories they reside in. The effect of the individual files is
           the same as if all the files were concatenated together in the
           order of parsing. This means that once a pattern is matched in
           some file no further files are parsed. If a config file is
           explicitly specified with the accessfile option the files in the
           above directories are not parsed.

           If Linux PAM is compiled with audit support the module will report
           when it denies access based on origin (host, tty, etc.).

## [](#OPTIONS)OPTIONS

           accessfile=/path/to/access.conf
               Indicate an alternative access.conf style configuration file
               to override the default. This can be useful when different
               services need different access lists.

           debug
               A lot of debug information is printed with syslog(3).

           noaudit
               Do not report logins from disallowed hosts and ttys to the
               audit subsystem.

           nodefgroup
               User tokens which are not enclosed in parentheses will not be
               matched against the group database. The backwards compatible
               default is to try the group database match even for tokens not
               enclosed in parentheses.

           nodns
               Do not try to resolve tokens as hostnames, only IPv4 and IPv6
               addresses will be resolved. Which means to allow login from a
               remote host, the IP addresses need to be specified in
               access.conf.

           quiet_log
               Do not log denials with syslog(3).

           fieldsep=separators
               This option modifies the field separator character that
               pam_access will recognize when parsing the access
               configuration file. For example: fieldsep=| will cause the
               default `:' character to be treated as part of a field value
               and `|' becomes the field separator. Doing this may be useful
               in conjunction with a system that wants to use pam_access with
               X based applications, since the PAM_TTY item is likely to be
               of the form "hostname:0" which includes a `:' character in its
               value. But you should not need this.

           listsep=separators
               This option modifies the list separator character that
               pam_access will recognize when parsing the access
               configuration file. For example: listsep=, will cause the
               default ` ' (space) and `\t' (tab) characters to be treated as
               part of a list element value and `,' becomes the only list
               element separator. Doing this may be useful on a system with
               group information obtained from a Windows domain, where the
               default built-in groups "Domain Users", "Domain Admins"
               contain a space.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (auth, account, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               Access was granted.

           PAM_PERM_DENIED
               Access was not granted.

           PAM_IGNORE
               pam_setcred was called which does nothing.

           PAM_ABORT
               Not all relevant data or options could be gotten.

           PAM_USER_UNKNOWN
               The user is not known to the system.

## [](#FILES)FILES

           /etc/security/access.conf
               Default configuration file

           /usr/share/pam/security/access.conf
               Default configuration file if /etc/security/access.conf does
               not exist.

## [](#SEE_ALSO)SEE ALSO

           access.conf(5), pam.d(5), pam(8).

## [](#AUTHORS)AUTHORS

           The logdaemon style login access control scheme was designed and
           implemented by Wietse Venema. The pam_access PAM module was
           developed by Alexei Nogin <alexei@nogin.dnttm.ru>. The IPv6
           support and the network(address) / netmask feature was developed
           and provided by Mike Becher <mike.becher@lrz-muenchen.de>.

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

    Linux-PAM                       08/04/2026                  PAM_ACCESS(8)

------------------------------------------------------------------------

Pages that refer to this page: [access.conf(5)](../man5/access.conf.5.html)

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
