---
{"title": "smb2-quota(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/smb2-quota.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# smb2-quota(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SMB2-QUOTA(1)            General Commands Manual            SMB2-QUOTA(1)

## [](#NAME)NAME

           smb2-quota - Userspace helper to display quota information for the
           Linux SMB client file system (CIFS)

## [](#SYNOPSIS)SYNOPSIS

              smb2-quota [-h] {options} {file system object}

## [](#DESCRIPTION)DESCRIPTION

           This tool is part of the cifs-utils suite.

           smb2-quota is a userspace helper program for the Linux SMB client
           file system (CIFS).

           This tool works by making an CIFS_QUERY_INFO IOCTL call to the
           Linux SMB client which in turn issues a SMB Query Info request and
           returns the result.

## [](#OPTIONS)OPTIONS

           --help/-h: Print help explaining the command line options.

           --tabular/-t: Print quota information for the volume in tabular
           format.  Amount Used | Quota Limit | Warning Level | Percent Used
           | Status | SID

           --csv/-c: Print quota information for the volume in csv format.
           SID,Amount Used,Quota Limit,Warning Level

           --list/-l: Print quota information for the volume in raw format.
           - SID - Quota Used - Quota Threshold - Quota Limit

           --tabular/-t is the default action if none is given.

## [](#NOTES)NOTES

           Kernel support for smb2-quota requires the CIFS_QUERY_INFO IOCTL
           which was initially introduced in the 4.20 kernel and is only
           implemented for mount points using SMB2 or above (see
           mount.cifs(8) vers option).

## [](#SEE_ALSO)SEE ALSO

           smbinfo(1)

## [](#AUTHOR)AUTHOR

           Kenneth D'souza < <kdsouza@redhat.com> >

           The Linux CIFS Mailing list is the preferred place to ask
           questions regarding these programs.

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

                                                                SMB2-QUOTA(1)

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
