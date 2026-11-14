---
{"title": "cifscreds(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cifscreds.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cifscreds(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CIFSCREDS(1)             General Commands Manual             CIFSCREDS(1)

## [](#NAME)NAME

           cifscreds - manage NTLM credentials in kernel keyring

## [](#SYNOPSIS)SYNOPSIS

              cifscreds add|clear|clearall|update [-u username] [-d]
              host|domain [-t timeout]

## [](#DESCRIPTION)DESCRIPTION

           The cifscreds  program is a tool for managing credentials
           (username and password) for the purpose of establishing sessions
           in multiuser mounts.

           When a cifs filesystem is mounted with the "multiuser" option, and
           does not use krb5 authentication, it needs to be able to get the
           credentials for each user from somewhere. The cifscreds program is
           the tool used to provide these credentials to the kernel.

           The first non-option argument to cifscreds is a command (see the
           COMMANDS  section below). The second non-option argument is a
           hostname or address, or an NT domain name.

## [](#COMMANDS)COMMANDS

           add    Add credentials to the kernel to be used for connecting to
                  the given server, or servers in the given domain.

           clear  Clear credentials for a particular host or domain from the
                  kernel.

           clearall
                  Clear all cifs credentials from the kernel.

           update Update stored credentials in the kernel with a new username
                  and password.

## [](#OPTIONS)OPTIONS

           -d, --domain
                  The provided host/domain argument is a NT domainname.

                  Ordinarily the second argument provided to cifscreds is
                  treated as a hostname or IP address. This option causes the
                  cifscreds program to treat that argument as an NT
                  domainname instead.

                  If there are not host specific credentials for the mounted
                  server, then the kernel will next look for a set of domain
                  credentials equivalent to the domain= option provided at
                  mount time.

           -u, --username
                  Ordinarily, the username is derived from the unix username
                  of the user adding the credentials. This option allows the
                  user to substitute a different username.

           -t, --timeout
                  Sets the key timeout in seconds. If not set, will use the
                  system default timeout for logon keys.

## [](#NOTES)NOTES

           The cifscreds utility requires a kernel built with support for the
           login key type. That key type was added in v3.3 in mainline Linux
           kernels.

           Since cifscreds adds keys to the session keyring, it is highly
           recommended that one use pam_keyinit to ensure that a session
           keyring is established at login time.

## [](#SEE_ALSO)SEE ALSO

           pam_keyinit(8)

## [](#AUTHORS)AUTHORS

           The cifscreds program was originally developed by Igor Druzhinin <
           <jaxbrigs@gmail.com> >. This manpage and a redesign of the code
           was done by Jeff Layton < <jlayton@samba.org> >.

## [](#COLOPHON)COLOPHON

           This page is part of the LinuxCIFS utils (network filesystem
           mounts from Linux (e.g. to Samba, ksmbd, etc.)) project.
           Information about the project can be found at 
           ⟨https://wiki.samba.org/index.php/LinuxCIFS_utils⟩.  If you have a
           bug report for this manual page, send it to
           linux-cifs@vger.kernel.org, samba-technical@lists.samba.org.  This
           page was obtained from the project's upstream Git repository
           ⟨git://git.samba.org/cifs-utils.git⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-09.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                                 CIFSCREDS(1)

------------------------------------------------------------------------

Pages that refer to this page: [pam_cifscreds(8)](../man8/pam_cifscreds.8.html)

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
