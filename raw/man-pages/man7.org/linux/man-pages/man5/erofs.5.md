---
{"title": "erofs(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/erofs.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# erofs(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [VERSIONS](#VERSIONS) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    erofs(5)                   File Formats Manual                   erofs(5)

## [](#NAME)NAME

           erofs - the Enhanced Read-Only File System

## [](#DESCRIPTION)DESCRIPTION

           erofs is a create-once read-only filesystem, with support for
           compression and a multi-device backing store.

           There are two inode formats:

           •  32-byte compact with 16-bit UID/GID, 32-bit file size, and no
              file times
           •  64-byte extended with 32-bit UID/GID, 64-bit file size, and a
              modification time (st_mtim).

       Mount options
           user_xattr
           nouser_xattr
                  Controls whether user extended attributes are exposed.
                  Defaults to yes.

           acl
           noacl  Controls whether POSIX acl(5)s are exposed.  Defaults to
                  yes.

           cache_strategy=disabled|readahead|readaround
                  Cache allocation for compressed files: never, if reading
                  from start of file, regardless of position.  Defaults to
                  readaround.

           dax
           dax=always|never
                  Direct Access control.  If always and the source device
                  supports DAX, uncompressed non-inlined files will be read
                  directly, without going through the page cache.  dax is a
                  synonym for always.  Defaults to unset, which is equivalent
                  to never.

           device=blobdev
                  Add extra device holding some of the data.  Must be given
                  as many times and in the same order as --blobdev was to
                  mkfs.erofs(1).

           domain_id=did
           fsid=id
                  Control CacheFiles on-demand read support.  To be
                  documented.

## [](#VERSIONS)VERSIONS

           erofs images are versioned through the use of feature flags; these
           are listed in the -E section of mkfs.erofs(1),

## [](#CONFIGURATION)CONFIGURATION

           Linux must be configured with the CONFIG_EROFS_FS option to mount
           EROFS filesystems.  There are sub-configuration items that
           restrict the availability of some of the parameters above.

## [](#SEE_ALSO)SEE ALSO

           mkfs.erofs(1), fsck.erofs(1), dump.erofs(1)

           Documentation/filesystems/erofs.rst in the Linux source.

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08                       erofs(5)

------------------------------------------------------------------------

Pages that refer to this page: [filesystems(5)](../man5/filesystems.5.html),  [repart.d(5)](../man5/repart.d.5.html)

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
