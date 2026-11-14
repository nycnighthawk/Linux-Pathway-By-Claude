---
{"title": "seunshare(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/seunshare.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# seunshare(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SEUNSHARE(8)                  User Commands                  SEUNSHARE(8)

## [](#NAME)NAME

           seunshare - Run cmd with alternate homedir, tmpdir and/or SELinux
           context

## [](#SYNOPSIS)SYNOPSIS

           seunshare [ -v ] [ -C ] [ -k ] [ -t tmpdir ] [ -h homedir ] [ -Z
           context ] -- executable [args]

## [](#DESCRIPTION)DESCRIPTION

           Run the executable within the specified context, using custom home
           directory and /tmp directory. The seunshare command unshares from
           the default namespace, then mounts the specified homedir and
           tmpdir over the default homedir and /tmp. Finally it tells the
           kernel to execute the application under the specified SELinux
           context.

           -h homedir
                  Alternate homedir to be used by the application. Homedir
                  must be owned by the user

           -t tmpdir
                  Use alternate temporary directory to mount on /tmp. tmpdir
                  must be owned by the user

           -r runuserdir
                  Use alternate temporary directory to mount on
                  XDG_RUNTIME_DIR (/run/user/$UID). runuserdir must be owned
                  by the user

           -C --capabilities
                  Retained for compatibility; has no effect. seunshare always
                  drops all capabilities and sets the no-root securebits so
                  setuid-root programs run without capabilities, but leaves
                  the bounding set intact so programs with file capabilities
                  continue to work.

           -k --kill
                  Kill all processes with matching MCS level

           -Z context
                  Use alternate SELinux context while running the executable

           -v     Verbose output

## [](#EXAMPLE)EXAMPLE

           Run bash with temporary /home and /tmp directory
           # USERHOMEDIR=`mktemp -d /tmp/home.XXXXXX`; USERTEMPDIR=`mktemp -d /tmp/temp.XXXXXX`
           # seunshare -v -h ${USERHOMEDIR} -t ${USERTEMPDIR} -- /bin/bash

## [](#SEE_ALSO)SEE ALSO

           runcon(1),
                  sandbox(8), selinux(8)

## [](#AUTHOR)AUTHOR

           This manual page was written by Dan Walsh <dwalsh@redhat.com> and
           Thomas Liu <tliu@fedoraproject.org>

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

    seunshare                        May 2010                    SEUNSHARE(8)

------------------------------------------------------------------------

Pages that refer to this page: [sandbox(8)](../man8/sandbox.8.html)

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
