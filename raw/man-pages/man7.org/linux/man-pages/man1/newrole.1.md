---
{"title": "newrole(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/newrole.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# newrole(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NEWROLE(1)               General Commands Manual               NEWROLE(1)

## [](#NAME)NAME

           newrole - run a shell with a new SELinux role

## [](#SYNOPSIS)SYNOPSIS

           newrole [-r|--role] ROLE [-t|--type] TYPE [-l|--level]
           [-p|--preserve-environment] LEVEL [-- [ARGS]...]

## [](#DESCRIPTION)DESCRIPTION

           Run a new shell in a new context.  The new context is derived from
           the old context in which newrole is originally executed.  If the
           -r or --role option is specified, then the new context will have
           the role specified by ROLE.  If the -t or --type option is
           specified, then the new context will have the type (domain)
           specified by TYPE.  If a role is specified, but no type is
           specified, the default type is derived from the specified role.
           If the -l or --level option is specified, then the new context
           will have the sensitivity level specified by LEVEL.  If LEVEL is a
           range, the new context will have the sensitivity level and
           clearance specified by that range.  If the -p or --preserve-
           environment option is specified, the shell with the new SELinux
           context will preserve environment variables, otherwise a new
           minimal environment is created.

           Additional arguments ARGS may be provided after a -- option, in
           which case they are supplied to the new shell.  In particular, an
           argument of -- -c will cause the next argument to be treated as a
           command by most command interpreters.

           If a command argument is specified to newrole and the command name
           is found in /etc/selinux/newrole_pam.conf, then the pam service
           name listed in that file for the command will be used rather than
           the normal newrole pam configuration.  This allows for per-command
           pam configuration when invoked via newrole, e.g. to skip the
           interactive re-authentication phase.

           The new shell will be the shell specified in the user's entry in
           the /etc/passwd file.

           The -V or --version shows the current version of newrole

## [](#EXAMPLE)EXAMPLE

           Changing role:
              # id -Z
              staff_u:staff_r:staff_t:SystemLow-SystemHigh
              # newrole -r sysadm_r
              # id -Z
              staff_u:sysadm_r:sysadm_t:SystemLow-SystemHigh

           Changing sensitivity only:
              # id -Z
              staff_u:sysadm_r:sysadm_t:Unclassified-SystemHigh
              # newrole -l Secret
              # id -Z
              staff_u:sysadm_r:sysadm_t:Secret-SystemHigh

           Changing sensitivity and clearance:
              # id -Z
              staff_u:sysadm_r:sysadm_t:Unclassified-SystemHigh
              # newrole -l Secret-Secret
              # id -Z
              staff_u:sysadm_r:sysadm_t:Secret

           Running a program in a given role or level:
              # newrole -r sysadm_r -- -c "/path/to/app arg1 arg2..."
              # newrole -l Secret -- -c "/path/to/app arg1 arg2..."

## [](#FILES)FILES

           /etc/passwd - user account information
           /etc/shadow - encrypted passwords and age information
           /etc/selinux/<policy>/contexts/default_type - default types for
           roles
           /etc/selinux/<policy>/contexts/securetty_types - securetty types
           for level changes
           /etc/selinux/newrole_pam.conf - optional mapping of commands to
           separate pam service names

## [](#SEE_ALSO)SEE ALSO

           runcon(1)

## [](#AUTHORS)AUTHORS

           Anthony Colatrella
           Tim Fraser
           Steve Grubb <sgrubb@redhat.com>
           Darrel Goeddel <DGoeddel@trustedcs.com>
           Michael Thompson <mcthomps@us.ibm.com>
           Dan Walsh <dwalsh@redhat.com>

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Security Enhanced Linux        October 2000                    NEWROLE(1)

------------------------------------------------------------------------

Pages that refer to this page: [default_type(5)](../man5/default_type.5.html),  [securetty_types(5)](../man5/securetty_types.5.html),  [run_init(8)](../man8/run_init.8.html)

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
