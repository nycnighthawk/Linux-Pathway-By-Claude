---
{"title": "pam_cifscreds(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_cifscreds.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_cifscreds(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_CIFSCREDS(8)         System Manager's Manual         PAM_CIFSCREDS(8)

## [](#NAME)NAME

           pam_cifscreds - PAM module to manage NTLM credentials in kernel
           keyring

## [](#SYNOPSIS)SYNOPSIS

           Edit the PAM configuration files for the systems that you want to
           automatically register NTLM credentials for, e.g.
           /etc/pam.d/login, and modify as follows:

                  ...
                  auth       substack     system-auth
              +++ auth       optional     pam_cifscreds.so
                  auth       include      postlogin
                  ...

                  ...
                  session    include      system-auth
              +++ session    optional     pam_cifscreds.so domain=DOMAIN
                  session    include      postlogin
                  ...

           Change DOMAIN to the name of you Windows domain, or use host= as
           described below.

## [](#DESCRIPTION)DESCRIPTION

           The pam_cifscreds PAM module is a tool for automatically adding
           credentials (username and password) for the purpose of
           establishing sessions in multiuser mounts.

           When a cifs filesystem is mounted with the "multiuser" option, and
           does not use krb5 authentication, it needs to be able to get the
           credentials for each user from somewhere. The pam_cifscreds module
           can be used to provide these credentials to the kernel
           automatically at login.

           In the session section of the PAM configuration file, the module
           can either an NT domain name or a list of hostname or addresses.

## [](#OPTIONS)OPTIONS

           pam_cifscreds supports a couple options which can be set in the
           PAM configuration files. You must have one (and only one) of
           domain= or host=.

           debug  Turns on some extra debug logging.

           domain=<NT domain name>
                  Credentials will be added for the specified NT domain name.

           host=<hostname or IP address>[,...]
                  Credentials will be added for the specified hostnames or IP
                  addresses.

## [](#NOTES)NOTES

           The pam_cifscreds PAM module requires a kernel built with support
           for the login key type. That key type was added in v3.3 in
           mainline Linux kernels.

           Since pam_cifscreds adds keys to the session keyring, it is highly
           recommended that one use pam_keyinit to ensure that a session
           keyring is established at login time.

## [](#SEE_ALSO)SEE ALSO

           cifscreds(1), pam_keyinit(8)

## [](#AUTHOR)AUTHOR

           The pam_cifscreds PAM module was developed by Orion Poplawski <
           <orion@nwra.com> >.

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

                                                             PAM_CIFSCREDS(8)

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
