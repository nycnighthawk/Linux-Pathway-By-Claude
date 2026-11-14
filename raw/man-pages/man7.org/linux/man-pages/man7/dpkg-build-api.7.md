---
{"title": "dpkg-build-api(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/dpkg-build-api.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-build-api(7) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [API LEVELS](#API_LEVELS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-build-api(7)               dpkg suite              dpkg-build-api(7)

## [](#NAME)NAME

           dpkg-build-api - source package dpkg build API level

## [](#SYNOPSIS)SYNOPSIS

            Build-Depends:
             dpkg-build-api (= 1),

## [](#DESCRIPTION)DESCRIPTION

           The source package dpkg build API level, defines a versioned
           interface for source packages, where each API level provides
           specific behaviors and guarantees.

           These interfaces can then be adopted by packages in a gradual way,
           and phased out more easily than with global behavior changes.

           The declaration of this API level is done through
           build-dependencies, in one of Build-Depends, Build-Depends-Indep
           or Build-Depends-Arch, or via the environment variable
           DPKG_BUILD_API, which will override these if both are present, and
           might emit a warning in case they are different.

## [](#API_LEVELS)API LEVELS

           v2  This level is still under development, and cannot be declared
               via build-dependencies.

           v1  This is the recommended level.  Since dpkg 1.22.0.

               Changes from v0 are:

               •   dpkg-shlibdeps no longer uses the LD_LIBRARY_PATH
                   environment variable.  The -l option should be used
                   instead.

               •   dpkg-buildpackage defaults to Rules-Requires-Root value
                   no.  To restore the v0 behavior (from before dpkg 1.22.13)
                   Rules-Requires-Root should be set to binary-targets.

               •   dpkg-buildpackage expects all required debian/rules
                   targets to be supported and no longer has backwards
                   compatibility fallback code.  The required targets are
                   clean, build, build-indep, build-arch, binary-indep and
                   binary-arch.

               •   vendor.mk defaults to using dpkg_vendor_derives_from_v1
                   for the dpkg_vendor_derives_from macro.  To restore the v0
                   behavior set dpkg_vendor_derives_from to
                   dpkg_vendor_derives_from_v0.

               •   default.mk defaults to including buildtools.mk.

           v0  This is the current global level, equivalent to not specifying
               one.  The interfaces and behaviors provided are subject to the
               normal global interface updates, which tend to require longer
               deprecation cycles and/or coordinated transitions.

## [](#SEE_ALSO)SEE ALSO

           deb-src-control(5).

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

    1.22.12-10-g32fee               2025-01-01              dpkg-build-api(7)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-buildapi(1)](../man1/dpkg-buildapi.1.html)

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
