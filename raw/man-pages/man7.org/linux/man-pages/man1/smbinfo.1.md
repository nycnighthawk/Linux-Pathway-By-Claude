---
{"title": "smbinfo(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/smbinfo.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# smbinfo(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMAND](#COMMAND) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    smbinfo(1)               General Commands Manual               smbinfo(1)

## [](#Name)Name

           smbinfo - Userspace helper to display SMB-specific file
           information for the Linux SMB client file system (CIFS)

## [](#SYNOPSIS)SYNOPSIS

              smbinfo [-v] [-h] [-V] {command} {file system object}

## [](#DESCRIPTION)DESCRIPTION

           This tool is part of the cifs-utils suite.

           smbinfo is a userspace helper program for the Linux SMB client
           file system (CIFS). It is intended to display SMB-specific file
           informations such as Security Descriptors and Quota.

           This tool works by making an CIFS_QUERY_INFO IOCTL call to the
           Linux SMB client which in turn issues a SMB Query Info request and
           returns the result. This differs from getcifsacl which uses
           extended file attributes.

## [](#OPTIONS)OPTIONS

           -v     Print version number and exit.

           -V     Verbose output.

           -h     Print help explaining the command line options.

## [](#COMMAND)COMMAND

           fileaccessinfo: Prints the FileAccessInformation class

           filealigninfo: Prints the FileAlignmentInformation class

           fileallinfo: Prints the FileAllInformation class

           filebasicinfo: Prints the FileBasicInformation class

           fileeainfo: Prints the FileEaInformation class

           filefsfullsizeinfo: Prints the FileFsFullSizeInformation class

           fileinternalinfo: Prints the FileInternalInformation class

           filemodeinfo: Prints the FileModeInformation class

           filepositioninfo: Prints the FilePositionInformation class

           filestandardinfo: Prints the FileStandardInformation class

           filestreaminfo: Prints the FileStreamInformation class

           filecompressioninfo: Prints the FileCompressionInformation class

           fsctl-getobjid: Prints the ObjectID

           getcompression: Prints the compression setting for the file.

           setcompression -c <no|default|lznt1>: Sets the compression setting
           for the file.

           list-snapshots: Lists the previous versions of the volume that
           backs this file

           quota: Print the quota for the volume in the form - SID Length -
           Change Time - Quota Used - Quota Threshold - Quota Limit - SID

           secdesc: Print the security descriptor in the form - Revision -
           Control - Owner SID - Group SID - ACL - File types - File flags

           keys: Dump session id, encryption keys and decryption keys so that
           the SMB3 traffic of this mount can be decryped e.g. via wireshark
           (requires root).

           gettconinfo: Prints both the TCON Id and Session Id for a cifs
           file.

           notify: Query a directory for change notifications.

## [](#NOTES)NOTES

           Kernel support for smbinfo utilities requires the CIFS_QUERY_INFO
           IOCTL which was initially introduced in the 4.20 kernel and is
           only implemented for mount points using SMB2 or above (see
           mount.cifs(8) vers option).

## [](#SEE_ALSO)SEE ALSO

           mount.cifs(8), getcifsacl(1)

## [](#AUTHOR)AUTHOR

           Ronnie Sahlberg wrote the smbinfo program.

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

                                                                   smbinfo(1)

------------------------------------------------------------------------

Pages that refer to this page: [smb2-quota(1)](../man1/smb2-quota.1.html)

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
