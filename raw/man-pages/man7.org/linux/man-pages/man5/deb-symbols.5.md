---
{"title": "deb-symbols(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-symbols.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-symbols(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-symbols(5)                  dpkg suite                 deb-symbols(5)

## [](#NAME)NAME

           deb-symbols - Debian's extended shared library information file

## [](#SYNOPSIS)SYNOPSIS

           DEBIAN/symbols

## [](#DESCRIPTION)DESCRIPTION

           The symbol files are shipped in Debian binary packages, and its
           format is a subset of the template symbol files used by
           dpkg-gensymbols(1) in Debian source packages, see
           deb-src-symbols(5).

           A symbols file must be shipped in the same binary package as the
           shared libraries described within.  This is to guarantee that the
           symbols descriptions match the shared library being described, and
           so that the symbols file can be found from the package owning the
           shared library.

           The format for an extended shared library dependency information
           entry in these files is:

            library-soname main-dependency-template
            [| alternative-dependency-template]
            [...]
            [* field-name: field-value]
            [...]
             symbol minimal-version [id-of-dependency-template]

           The library-soname is exactly the value of the SONAME field as
           exported by objdump(1).  A dependency-template is a dependency
           where #MINVER# is dynamically replaced either by a version check
           like “(>= minimal-version)” or by nothing (if an unversioned
           dependency is deemed sufficient).

           Each exported symbol (listed as name@version, with version being
           “Base” if the library is not versioned) is associated to a
           minimal-version of its dependency template (the main dependency
           template is always used and will end up being combined with the
           dependency template referenced by id-of-dependency-template if
           present).  The first alternative dependency template is numbered
           1, the second one 2, etc.  Each column is separated by exactly a
           single whitespace.

           Each entry for a library can also have some fields of
           meta-information.  Those fields are stored on lines starting with
           an asterisk.  Currently, the only valid fields are:

           Build-Depends-Package
               It indicates the name of the “-dev” package associated to the
               library and is used by dpkg-shlibdeps to make sure that the
               dependency generated is at least as strict as the
               corresponding build dependency.

               Supported since dpkg 1.14.13.

           Build-Depends-Packages
               The same as Build-Depends-Package but accepts a
               comma-separated list of package names.  This field will
               override any Build-Depends-Package field present, and is
               mostly useful with “-dev” packages and metapackages depending
               on these, say for a transition period.

               Supported since dpkg 1.20.0.

           Allow-Internal-Symbol-Groups
               It indicates what internal symbol groups should be ignored, as
               a whitespace separated list, so that the symbols contained in
               those groups get included in the output file.  This should
               only be necessary for toolchain packages providing those
               internal symbols.  The available groups are system dependent,
               for ELF and GNU-based systems these are aeabi and gomp.

               Supported since dpkg 1.20.1.

## [](#EXAMPLES)EXAMPLES

       Simple symbols file
            libftp.so.3 libftp3 #MINVER#
             DefaultNetbuf@Base 3.1-1-6
             FtpAccess@Base 3.1-1-6
             [...]

       Advanced symbols file
            libGL.so.1 libgl1
            | libgl1-mesa-glx #MINVER#
            * Build-Depends-Package: libgl1-mesa-dev
             publicGlSymbol@Base 6.3-1
             [...]
             implementationSpecificSymbol@Base 6.5.2-7 1
             [...]

## [](#SEE_ALSO)SEE ALSO

           <https://wiki.debian.org/Projects/ImprovedDpkgShlibdeps>,
           deb-src-symbols(5), dpkg-shlibdeps(1), dpkg-gensymbols(1).

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

    1.23.7-216-gff7e9               2026-03-07                 deb-symbols(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-gensymbols(1)](../man1/dpkg-gensymbols.1.html),  [dpkg-shlibdeps(1)](../man1/dpkg-shlibdeps.1.html),  [deb(5)](../man5/deb.5.html),  [deb-shlibs(5)](../man5/deb-shlibs.5.html),  [deb-src-symbols(5)](../man5/deb-src-symbols.5.html)

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
