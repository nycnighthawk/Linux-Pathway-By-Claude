---
{"title": "deb-postinst(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-postinst.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-postinst(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-postinst(5)                 dpkg suite                deb-postinst(5)

## [](#NAME)NAME

           deb-postinst - package post-installation maintainer script

## [](#SYNOPSIS)SYNOPSIS

           DEBIAN/postinst

## [](#DESCRIPTION)DESCRIPTION

           A package can perform several post-installation actions via
           maintainer scripts, by including an executable postinst file in
           its control archive (i.e. DEBIAN/postinst during package
           creation).

           The script can be called in the following ways:

           postinst configure old-version
               After the package was installed.

           postinst triggered "trigger-name..."
               After the package was triggered.  The list of space-separated
               trigger-names is passed as the second argument.

           old-postinst abort-upgrade new-version
               If prerm fails during upgrade or fails on failed-upgrade.

           old-postinst abort-remove
               If prerm fails during remove.

           postinst abort-deconfigure in-favour new-package new-version
                  [ removing old-package old-version ]
               If prerm fails during deconfigure in-favour of a package.

           postinst abort-remove in-favour new-package new-version
               If prerm fails during remove in-favour for replacement due to
               conflict.

## [](#SEE_ALSO)SEE ALSO

           dpkg(1).

## [](#COLOPHON)COLOPHON

           This page is part of the dpkg (Debian Package Manager) project.
           Information about the project can be found at 
           ⟨https://wiki.debian.org/Teams/Dpkg/⟩.  If you have a bug report
           for this manual page, see
           ⟨http://bugs.debian.org/cgi-bin/pkgreport.cgi?src=dpkg⟩.  This
           page was obtained from the project's upstream Git repository ⟨git
           clone https://git.dpkg.org/git/dpkg/dpkg.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    1.22.0-52-g1af0                 2023-08-30                deb-postinst(5)

------------------------------------------------------------------------

Pages that refer to this page: [deb(5)](../man5/deb.5.html)

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
