---
{"title": "slapo-homedir(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-homedir.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-homedir(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [REPLICATION](#REPLICATION) \| [EXAMPLE](#EXAMPLE) \| [BUGS](#BUGS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                               |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-HOMEDIR(5)           File Formats Manual           SLAPO-HOMEDIR(5)

## [](#NAME)NAME

           slapo-homedir - Home directory provisioning overlay

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The homedir overlay causes slapd(8) to notice changes involving
           RFC-2307bis style user-objects and make appropriate changes to the
           local filesystem.  This can be performed on both master and
           replica systems, so it is possible to perform remote home
           directory provisioning.

## [](#CONFIGURATION)CONFIGURATION

           Both slapd.conf and back-config style configuration is supported.

           overlay homedir
                  This directive adds the homedir overlay to the current
                  database, or to the frontend, if used before any database
                  instantiation; see slapd.conf(5) for details.

           homedir-skeleton-path <pathname>

           olcSkeletonPath: pathname
                  These options set the path to the skeleton account
                  directory.  (Generally, /etc/skel) Files in this directory
                  will be copied into newly created home directories.
                  Copying is recursive and handles symlinks and fifos, but
                  will skip most specials.

           homedir-min-uidnumber <user id number>

           olcMinimumUidNumber: number
                  These options configure the minimum userid to use in any
                  home directory attempt.  This is a basic safety measure to
                  prevent accidentally using system accounts.  See
                  REPLICATION for more flexible options for selecting
                  accounts.

           homedir-regexp <regexp> <path>

           olcHomedirRegexp: regexp path
                  These options configure a set of regular expressions to use
                  for matching and optionally remapping incoming
                  homeDirectory attribute values to pathnames on the local
                  filesystem.  $number expansion is supported to access
                  values captured in parentheses.

                  For example, to accept any directory starting with home and
                  use it verbatim on the local filesystem:

                  homedir-regexp ^(/home/[-_/a-z0-9]+)$ $1

                  To match the same set of directories, but create them
                  instead under exporthome, as is popular on Solaris NFS
                  servers:

                  homedir-regexp ^(/home/[-_/a-z0-9]+)$ /export$1

           homedir-delete-style style

           olcHomedirDeleteStyle: style
                  These options configure how deletes of posixAccount entries
                  or their attributes are handled; valid styles are IGNORE,
                  which does nothing, and DELETE, which immediately performs
                  a recursive delete on the home directory, and ARCHIVE,
                  which archives the home directory contents in a TAR file
                  for later examination.  The default is IGNORE.  Use with
                  caution.  ARCHIVE requires homedir-archive-path to be set,
                  or it functions similar to IGNORE.

           homedir-archive-path <pathname>

           olcHomedirArchivePath: pathname
                  These options specify the destination path for TAR files
                  created by the ARCHIVE delete style.

## [](#REPLICATION)REPLICATION

           The homedir overlay can operate on either master or replica
           systems with no changes.  See slapd.conf(5) or slapd-config(5) for
           more information on configure syncrepl.

           Partial replication (e.g. with filters) is especially useful for
           providing different provisioning options to different sets of
           users.

## [](#EXAMPLE)EXAMPLE

           The following LDIF could be used to add this overlay to cn=config
           (adjust to suit)

                  dn: cn=module{0},cn=config
                  changetype: modify
                  add: olcModuleLoad
                  olcModuleLoad: homedir

                  dn: olcOverlay=homedir,olcDatabase={1}mdb,cn=config
                  changetype: add
                  objectClass: olcOverlayConfig
                  objectClass: olcHomedirConfig
                  olcOverlay: homedir
                  olcSkeletonPath: /etc/skel
                  olcMinimumUidNumber: 1000
                  olcHomedirRegexp: ^(/home/[-_/a-z0-9]+)$ /export/$1
                  olcHomedirDeleteStyle: ARCHIVE
                  olcHomedirArchivePath: /archive

## [](#BUGS)BUGS

           DELETE, MOD, and MODRDN operations that remove the unix attributes
           when delete style is set to DELETE will recursively delete the
           (regex modified) home directory from the disk.  Please be careful
           when deleting or changing values.

           MOD and MODRDN will correctly respond to homeDirectory changes and
           perform a non-destructive rename() operation on the filesystem,
           but this does not correctly retry with a recursive copy when
           moving between filesystems.

           The recursive copy/delete/chown/tar functions are not aware of
           ACLs, extended attributes, forks, sparse files, or hard links.
           Block and character device archival is non-portable, but should
           not be an issue in home directories, hopefully.

           Copying and archiving may not support files larger than 2GiB on
           some architectures.  Bare POSIX UStar archives cannot support
           internal files larger than 8GiB.  The current tar generator does
           not attempt to resolve uid/gid into symbolic names.

           No attempt is made to try to mkdir() the parent directories needed
           for a given home directory or archive path.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

           /etc/skel (or similar)
                  source of new homedir files.

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd(8), RFC-2307, RFC-2307bis.

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           This module was written in 2009 by Emily Backes for Symas
           Corporation.

## [](#COLOPHON)COLOPHON

           This page is part of the OpenLDAP (an open source implementation
           of the Lightweight Directory Access Protocol) project.
           Information about the project can be found at 
           ⟨http://www.openldap.org/⟩.  If you have a bug report for this
           manual page, see ⟨http://www.openldap.org/its/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.openldap.org/openldap/openldap.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    OpenLDAP LDVERSION             RELEASEDATE               SLAPO-HOMEDIR(5)

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
