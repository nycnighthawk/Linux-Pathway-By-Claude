---
{"title": "deb-buildinfo(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-buildinfo.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-buildinfo(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FIELDS](#FIELDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-buildinfo(5)                dpkg suite               deb-buildinfo(5)

## [](#NAME)NAME

           deb-buildinfo - Debian build information file format

## [](#SYNOPSIS)SYNOPSIS

           filename.buildinfo

## [](#DESCRIPTION)DESCRIPTION

           Each Debian source package build can record the build information
           in a .buildinfo control file, which contains a number of fields in
           deb822(5) format.

           Each field begins with a tag, such as Source or Binary (case
           insensitive), followed by a colon, and the body of the field (case
           sensitive unless stated otherwise).  Fields are delimited only by
           field tags.  In other words, field text may be multiple lines in
           length, but the installation tools will generally join lines when
           processing the body of the field (except in case of the multiline
           fields Binary-Only-Changes, Installed-Build-Depends, Environment,
           Checksums-Md5, Checksums-Sha1 and Checksums-Sha256, see below).

           The control data might be enclosed in an OpenPGP ASCII Armored
           signature, as specified in RFC9580.

           The name of the .buildinfo file will depend on the type of build
           and will be as specific as necessary but not more; the name will
           be:

           source-name_binary-version_arch.buildinfo
               for a build that includes any

           source-name_binary-version_all.buildinfo
               otherwise for a build that includes all

           source-name_source-version_source.buildinfo
               otherwise for a build that includes source

## [](#FIELDS)FIELDS

           Format: format-version (required)
               The value of this field declares the format version of the
               file.  The syntax of the field value is a version number with
               a major and minor component.  Backward incompatible changes to
               the format will bump the major version, and backward
               compatible changes (such as field additions) will bump the
               minor version.  The current format version is 1.0.

           Source: source-name [(source-version)] (required)
               The name of the source package.  If the source version differs
               from the binary version, then the source-name will be followed
               by a source-version in parenthesis.  This can happen when the
               build is for a binary-only non-maintainer upload.

           Binary: binary-package-list (required in context)
               This folded field is a space-separated list of binary packages
               built.  If the build is source-only, then the field is omitted
               (since dpkg 1.20.0).

           Architecture: arch-list (required)
               The architecture list specifies on which type of machine this
               package runs.  The value should be a list of architecture
               names separated by spaces.

               Common architectures are amd64, armel, i386, etc.  Note that
               the special all value is meant for packages that are
               architecture independent (such as shell and Perl scripts or
               documentation).  If the source for the package is also being
               built, the special entry source is also present.

               Note: Architecture wildcards are not allowed in this context.

           Version: version-string (required)
               Typically, this is the original package's version number in
               whatever form the program's author uses.  It may also include
               a Debian revision number (for non-native packages).  The exact
               format and sorting algorithm are described in deb-version(7).

               Note: On some vendors, dpkg has been made to permit native
               sources with non-native versions, making this incoherent and
               adding to the confusion of the concept, where in addition this
               tends to be a trap for accidental mistakes.

           Binary-Only-Changes:
            changelog-entry
               This multiline field contains the concatenated text of the
               changelog entry for a binary-only non-maintainer upload
               (binNMU) if that is the case.  To make this a valid multiline
               field empty lines are replaced with a single full stop (‘.’)
               and all lines are indented by one space character.  The exact
               content depends on the changelog format.

           Checksums-Md5: (required, weak)
           Checksums-Sha1: (required, weak)
           Checksums-Sha256: (required, strong)
            checksum size filename
               These multiline fields contain a list of files with a checksum
               and size for each one.  These fields have the same syntax and
               differ only in the checksum algorithm used: MD5 for
               Checksums-Md5, SHA-1 for Checksums-Sha1 and SHA-256 for
               Checksums-Sha256.

               Note: The MD5 and SHA-1 checksums are considered weak, and
               should never be assumed to be sufficient for secure
               verification.

               The first line of the field value (the part on the same line
               as the field name followed by a colon) is always empty.  The
               content of the field is expressed as continuation lines, one
               line per file.  Each line consists of space-separated entries
               describing the file: the checksum, the file size, and the file
               name.

               These fields list all files that make up the build.

           Build-Origin: name
               The name of the distribution this package is originating from.

           Build-Architecture: arch (required)
               The Debian architecture for the installation the packages is
               being built in.  Common architectures are amd64, armel, i386,
               etc.

           Build-Date: build-date
               The date the package was built.  It must be in the same format
               as the date in a deb-changelog(5) entry.

           Build-Kernel-Version: build-kernel-version
               The release and version (in an unspecified format) of the
               kernel running on the build system.  This field is only going
               to be present if the builder has explicitly requested it, to
               avoid leaking possibly sensitive information.

           Build-Path: build-path
               The absolute build path, which correspond to the unpacked
               source tree.  This field is only going to be present if the
               vendor has allowed it via some pattern match to avoid leaking
               possibly sensitive information.

               On Debian and derivatives only build paths starting with
               /build/ will emit this field.

           Build-Tainted-By:
            taint-reason-list
               This folded field contains a space-separated list of
               non-exhaustive reason tags (formed by alphanumeric and dash
               characters) which identify why the current build has been
               tainted.

               Supported since dpkg 1.19.5.

               On Debian and derivatives the following reason tags can be
               emitted:

               usr-local-has-configs
                   The system has configuration files under /usr/local/etc.

               usr-local-has-includes
                   The system has header files under /usr/local/include.

               usr-local-has-programs
                   The system has programs under /usr/local/bin or
                   /usr/local/sbin.

               usr-local-has-libraries
                   The system has libraries, either static or shared under
                   /usr/local/lib.

               can-execute-cross-built-programs
                   The system can execute cross built programs, either
                   directly or via some emulation layer.

                   Since dpkg 1.21.10.

           Installed-Build-Depends: (required)
            package-list
               The list of installed and configured packages that might
               affect the package build process.

               The list consists of each package name, optionally
               arch-qualified for foreign architectures, with an exact
               version restriction, separated by commas.

               The list includes all essential packages, packages listed in
               Build-Depends, Build-Depends-Arch, Build-Depends-Indep source
               control fields, any vendor specific builtin dependencies, and
               all their recursive dependencies.  On Debian and derivatives
               the dependency builtin is build-essential.

               For dependencies coming from the source control fields, all
               dependency alternatives and all providers of virtual packages
               depended on will be included.

           Environment:
            variable-list
               The list of environment variables that are known to affect the
               package build process, with each environment variable followed
               by an equal sign (‘=’) and the variable's quoted value, using
               double quotes (‘"’), and backslashes escaped (‘\\’).

## [](#SEE_ALSO)SEE ALSO

           deb822(5), deb-changes(5), deb-version(7), dpkg-genbuildinfo(1).

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

    1.23.7-216-gff7e9               2026-03-07               deb-buildinfo(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-genbuildinfo(1)](../man1/dpkg-genbuildinfo.1.html)

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
