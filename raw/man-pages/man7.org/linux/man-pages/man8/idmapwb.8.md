---
{"title": "idmapwb(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/idmapwb.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# idmapwb(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IDMAPWB.SO(8)            System Manager's Manual            IDMAPWB.SO(8)

## [](#NAME)NAME

           idmapwb.so - winbind ID mapping plugin for cifs-utils

## [](#DESCRIPTION)DESCRIPTION

           This plugin allows the utilities in cifs-utils to work in
           conjuction with the winbind facility of Samba suite. It handles
           several functions including mapping UID and GID to SIDs and vice
           versa.

           Utilities are usually configured to use the correct plugin by
           creating a symlink at /etc/cifs-utils/idmap-plugin that points to
           the correct plugin that you wish to use.

           This plugin requires that winbindd(8) be properly configured and
           running.

## [](#SEE_ALSO)SEE ALSO

           getcifsacl(1), setcifsacl(1), cifs.idmap(8), samba(7),
           smb.conf(5), winbindd(8)

## [](#AUTHOR)AUTHOR

           idmapwb.so was written by Jeff Layton < <jlayton@samba.org> >

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

                                                                IDMAPWB.SO(8)

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
