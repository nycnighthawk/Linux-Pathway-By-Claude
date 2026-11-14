---
{"title": "getcifsacl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/getcifsacl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getcifsacl(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GETCIFSACL(1)            General Commands Manual            GETCIFSACL(1)

## [](#NAME)NAME

           getcifsacl - Userspace helper to display an ACL in a security
           descriptor for Common Internet File System (CIFS)

## [](#SYNOPSIS)SYNOPSIS

              getcifsacl [-v|-r] {file system object}

## [](#DESCRIPTION)DESCRIPTION

           This tool is part of the cifs-utils suite.

           getcifsacl is a userspace helper program for the Linux CIFS client
           file system. It is intended to display a security descriptor,
           including DACL and SACL for a file system object.

           This program uses a plugin to handle the mapping of SIDs to user
           and group names. /etc/cifs-utils/idmap-plugin should be a symlink
           that points to the correct plugin to use.

           Fields of an ACE such as SID, type, flags, and mask are displayed
           separated by /. Numeric values of type, flags, and mask are
           displayed in hexadecimal format.

## [](#OPTIONS)OPTIONS

           -v     Print version number and exit.

           -r     Display a security descriptor in raw mode. Values such as
                  type and flags are displayed in hexadecimal format, a SID
                  is not mapped to a name.

           -R     List the ACLs of all files and directories recursively.

## [](#NOTES)NOTES

           Kernel support for getcifsacl/setcifsacl utilities was initially
           introduced in the 2.6.37 kernel.

## [](#SEE_ALSO)SEE ALSO

           mount.cifs(8), setcifsacl(1)

## [](#AUTHOR)AUTHOR

           Shirish Pargaonkar wrote the getcifsacl program.

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

                                                                GETCIFSACL(1)

------------------------------------------------------------------------

Pages that refer to this page: [setcifsacl(1)](../man1/setcifsacl.1.html),  [smbinfo(1)](../man1/smbinfo.1.html),  [idmapwb(8)](../man8/idmapwb.8.html),  [mount.cifs(8)](../man8/mount.cifs.8.html)

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
