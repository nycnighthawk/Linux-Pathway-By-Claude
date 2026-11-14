---
{"title": "cifs.idmap(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cifs.idmap.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cifs.idmap(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION FOR KEYCTL](#CONFIGURATION_FOR_KEYCTL) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CIFS.IDMAP(8)            System Manager's Manual            CIFS.IDMAP(8)

## [](#NAME)NAME

           cifs.idmap - Userspace helper for mapping ids for Common Internet
           File System (CIFS)

## [](#SYNOPSIS)SYNOPSIS

              cifs.idmap [--help|-h] [--timeout|-t] [--version|-v] {keyid}

## [](#DESCRIPTION)DESCRIPTION

           This tool is part of the cifs-utils suite.

           cifs.idmap  is a userspace helper program for the linux CIFS
           client filesystem. There are a number of activities that the
           kernel cannot easily do itself. This program is a callout program
           that does these things for the kernel and then returns the result.

           cifs.idmap  is generally intended to be run when the kernel calls
           request-key(8) for a particular key type. While it can be run
           directly from the command-line, it is not generally intended to be
           run that way.

           This program is only called if a share is mounted with the cifsacl
           mount option. The kernel will only upcall to do this conversion if
           that mount option is specified.

           cifs.idmap  relies on a plugin to handle the ID mapping. If it
           can't find the plugin then it will not work properly. The plugin
           (or a symlink to it) must be at /etc/cifs-utils/idmap-plugin.

           In the case where cifs.idmap or the plugin are unavailable, file
           objects in a mounted share are assigned uid and gid of the
           credentials of the process that mounted the share. It is strongly
           recomemended to use mount options of uid and gid to specify a
           default uid and gid to map owner SIDs and group SIDs in this
           situation.

## [](#OPTIONS)OPTIONS

           --help|-h
                  Print the usage message and exit.

           --timeout|-t
                  Set the expiration timer, in seconds on the key. The
                  default is 600 seconds (10 minutes). Setting this to 0 will
                  cause the key to never expire.

           --version|-v
                  Print version number and exit.

## [](#CONFIGURATION_FOR_KEYCTL)CONFIGURATION FOR KEYCTL

           cifs.idmap  is designed to be called from the kernel via the
           request-key callout program. This requires that request-key be
           told where and how to call this program.  Currently cifs.idmap
           handles a key type of:

              cifs.idmap

           This keytype is for mapping a SID to either an uid or a gid.

           To make this program useful for CIFS, you will need to set up
           entry for it in request-key.conf(5). Here is an example of an
           entry for this key type:

              #OPERATION  TYPE           D C PROGRAM ARG1 ARG2...
              #=========  =============  = = ================================
              create      cifs.idmap     * * /usr/local/sbin/cifs.idmap %k

           See request-key.conf(5) for more info on each field.

## [](#NOTES)NOTES

           Support for upcalls to cifs.idmap was initially introduced in the
           3.0 kernel.

## [](#SEE_ALSO)SEE ALSO

           request-key.conf(5), mount.cifs(8)

## [](#AUTHOR)AUTHOR

           Shirish Pargaonkar wrote the cifs.idmap program.

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

                                                                CIFS.IDMAP(8)

------------------------------------------------------------------------

Pages that refer to this page: [idmapwb(8)](../man8/idmapwb.8.html)

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
