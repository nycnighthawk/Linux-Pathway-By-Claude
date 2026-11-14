---
{"title": "rpm-rpmrc(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/rpm-rpmrc.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-rpmrc(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [FILES](#FILES) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-RPMRC(5)               File Formats Manual               RPM-RPMRC(5)

## [](#NAME)NAME

           rpm-rpmrc - rpm platform compatibility configuration

## [](#SYNOPSIS)SYNOPSIS

           VARIABLE: {ARCH|OS}: VALUE ...

           VARIABLE: ARCH VALUE

## [](#FILES)FILES

           /usr/lib/rpm/rpmrc
           /usr/lib/rpm/<vendor>/rpmrc
           /etc/rpmrc
           ~/.config/rpm/rpmrc

## [](#DESCRIPTION)DESCRIPTION

           The low-level machine architecture and OS configuration in rpm is
           managed via a set of rpmrc files as defined by the rpmrc path.
           Most users never need to look at, much less touch these files.

           Each file in the colon separated rpmrc path is read sequentially
           by rpm for configuration information. Tildes will be expanded to
           the value of the environment variable HOME. The first file in the
           path must exist, others are considered optional.

           If a value is defined multiple times, the last entry wins. The
           default rpmrc path uses this to achieve the following hierarchy of
           platform configuration:
           1.  Generic rpm factory defaults
           2.  Vendor (distribution) specific configuration
           3.  Host specific configuration
           4.  User specific configuration

           In older rpm versions the path of per-user rpmrc was ~/.rpmrc.
           This is still processed if it exists and the new configuration
           directory does not exist.

## [](#CONFIGURATION)CONFIGURATION

           ARCH and OS relate to uname(2) machine and operating system
           information, but are not 1:1 equivalent. The following directives
           are supported in the rpmrc files:

           arch_canon ARCH: CANON_ARCH ARCH_NUM
               Names and numbers of known architectures to alias different
               spellings to a canonical one. CANON_ARCH is what the ARCH
               entries in other rpmrc directives refer to.

               The number is not used for any calculations by rpm but must be
               present for historical reasons.

           arch_compat: ARCH: COMPAT_ARCH ...
               Declare compatibility between machine architectures, ie. ARCH
               machines can install packages for COMPAT_ARCH architecture.

           archcolor: ARCH COLOR
               Declare the "color" of ARCH. The color relates to the word
               length aka bitness of the architecture:
               •   0 means none (noarch packages and similar)
               •   1 means 32-bit
               •   2 means 64-bit

           buildarch_compat: ARCH: COMPAT_ARCH ...
               Declare compatibility between build architectures targets, ie.
               ARCH machines can produce COMPAT_ARCH binaries.

           buildarchtranslate: ARCH: TRANSLATE_ARCH
               Automatically translate detected host architecture ARCH to
               TRANSLATE_ARCH when building packages. This is used to map
               sub-architectures to a main one, for example when building on
               a x86_64_v2 host we typically want the generated package to be
               of the main x86_64 architecture.

           optflags: ARCH OPTFLAGS
               Compiler flags to use when building packages for ARCH
               architecture. The OPTFLAGS value is available as %{optflags}
               macro in spec files.

           os_canon: OS: CANON_OS OS_NUM
               Names and numbers of known operating systems to alias
               different spellings to a canonical one. CANON_OS is what the
               OS entries in other rpmrc directives refer to.

               The number is not used for any calculations by rpm but must be
               present for historical reasons.

           os_compat: OS: COMPAT_OS ...
               Declare compatibility between operating systems, ie. OS
               machine can install packages for COMPAT_OS operating system.

## [](#ENVIRONMENT)ENVIRONMENT

           If XDG_CONFIG_HOME environment variable is set, it replaces
           ~/.config in the rpmrc path.

## [](#SEE_ALSO)SEE ALSO

           rpm(8), rpm-common(8), rpm-config(5), rpm-macros(7)

## [](#COLOPHON)COLOPHON

           This page is part of the rpm (RPM Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/rpm⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/rpm.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-27.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    RPM 6.1.90                      2026-08-03                   RPM-RPMRC(5)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild(1)](../man1/rpmbuild.1.html),  [rpmbuild-config(5)](../man5/rpmbuild-config.5.html),  [rpm-config(5)](../man5/rpm-config.5.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [rpm-spec-macros(7)](../man7/rpm-spec-macros.7.html),  [rpm(8)](../man8/rpm.8.html),  [rpm-common(8)](../man8/rpm-common.8.html)

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
