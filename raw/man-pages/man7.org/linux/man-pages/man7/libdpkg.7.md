---
{"title": "libdpkg(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/libdpkg.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# libdpkg(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    libdpkg(7)                      dpkg suite                     libdpkg(7)

## [](#NAME)NAME

           libdpkg - Debian package manager C library

## [](#DESCRIPTION)DESCRIPTION

           The libdpkg C library provides functions and infrastructure for
           the dpkg tool set, and external projects that need to integrate
           tightly with it.

           The library provides a pkgconf(1) entry named libdpkg.

           Warning: The API provided by this library is highly volatile,
           still in the process of being cleaned up.  It is only supposed to
           be used internally by dpkg for now.  Header files, functions,
           variables and types might get renamed, removed or change
           semantics.  If you still have a need to use it, which you would be
           doing anyway, say by locally building dpkg to get the library,
           then define the C preprocessor macro LIBDPKG_VOLATILE_API in your
           build to acknowledge that fact.

           Due to the currently API volatility, only a static library is
           provided.

## [](#SEE_ALSO)SEE ALSO

           /usr/local/share/doc/dpkg/README.api,
           <https://www.dpkg.org/doc/libdpkg/>.

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

    1.23.7-121-gd39fb               2026-03-07                     libdpkg(7)

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
