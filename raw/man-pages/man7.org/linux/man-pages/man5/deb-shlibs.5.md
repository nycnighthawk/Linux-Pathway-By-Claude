---
{"title": "deb-shlibs(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-shlibs.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-shlibs(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SONAME FORMATS](#SONAME_FORMATS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-shlibs(5)                   dpkg suite                  deb-shlibs(5)

## [](#NAME)NAME

           deb-shlibs - Debian shared library information file

## [](#SYNOPSIS)SYNOPSIS

           debian/shlibs, debian/binary-name.shlibs, DEBIAN/shlibs

## [](#DESCRIPTION)DESCRIPTION

           shlibs files map shared library names and versions (SONAMEs) to
           dependencies suitable for a package control file.

           A shlibs file must be shipped in the same binary package as the
           shared libraries described within.  This is to guarantee that the
           mappings match the shared library being described, and so that the
           shlibs file can be found from the package owning the shared
           library.

           There is one entry per line.  Blank lines are not allowed.  Lines
           beginning with a # character are considered commentary, and are
           ignored.  All other lines must have the format:

               [type:] library version dependencies

           The library and version fields are whitespace-delimited, but the
           dependencies field extends to the end of the line.  The type field
           is optional and normally not needed.

           The dependencies field has the same syntax as the Depends field in
           a binary control file, see deb-control(5).

## [](#SONAME_FORMATS)SONAME FORMATS

           The SONAME formats supported are:

               name.so.version

           and

               name-version.so

           where name is usually prefixed by lib.

           The former tends to be used by shared libraries with stable
           interfaces.  The latter by shared libraries with unstable
           interfaces, where the whole version becomes part of the SONAME and
           needs to be specified in full when linking against those
           libraries.

## [](#EXAMPLES)EXAMPLES

           The shlibs file for a typical library package, named libcrunch1,
           that provides one library whose SONAME is libcrunch.so.1, might
           read

            libcrunch 1 libcrunch1 (>= 1.2-1)

           The dependencies must mention the most recent version of the
           package that added new symbols to the library: in the above
           example, new symbols were added to version 1.2 of libcrunch.  This
           is not the only reason the dependencies might need to be
           tightened.

## [](#SEE_ALSO)SEE ALSO

           deb-control(5), deb-symbols(5), dpkg-shlibdeps(1).

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

    1.23.7-216-gff7e9               2026-03-07                  deb-shlibs(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-shlibdeps(1)](../man1/dpkg-shlibdeps.1.html),  [deb(5)](../man5/deb.5.html)

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
