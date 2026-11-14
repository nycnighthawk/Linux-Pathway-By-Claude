---
{"title": "deb-changes(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-changes.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-changes(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FIELDS](#FIELDS) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-changes(5)                  dpkg suite                 deb-changes(5)

## [](#NAME)NAME

           deb-changes - Debian upload changes control file format

## [](#SYNOPSIS)SYNOPSIS

           filename.changes

## [](#DESCRIPTION)DESCRIPTION

           Each Debian upload is composed of a .changes control file, which
           contains a number of fields in deb822(5) format.

           Each field begins with a tag, such as Source or Binary (case
           insensitive), followed by a colon, and the body of the field (case
           sensitive unless stated otherwise).  Fields are delimited only by
           field tags.  In other words, field text may be multiple lines in
           length, but the installation tools will generally join lines when
           processing the body of the field (except in case of the multiline
           fields Description, Changes, Files, Checksums-Sha1 and
           Checksums-Sha256, see below).

           The control data might be enclosed in an OpenPGP ASCII Armored
           signature, as specified in RFC9580.

## [](#FIELDS)FIELDS

           Format: format-version (required)
               The value of this field declares the format version of the
               file.  The syntax of the field value is a version number with
               a major and minor component.  Backward incompatible changes to
               the format will bump the major version, and backward
               compatible changes (such as field additions) will bump the
               minor version.  The current format version is 1.8.

           Date: release-date (required)
               The date the package was built or last edited.  It must be in
               the same format as the date in a deb-changelog(5) entry.

               The value of this field is usually extracted from the
               debian/changelog file.

           Source: source-name [(source-version)] (required)
               The name of the source package.  If the source version differs
               from the binary version, then the source-name will be followed
               by a source-version in parenthesis.  This can happen when the
               upload is a binary-only non-maintainer upload.

           Binary: binary-package-list (required in context)
               This folded field is a space-separated list of binary packages
               to upload.  If the upload is source-only, then the field is
               omitted (since dpkg 1.19.3).

           Architecture: arch-list
               Lists the architectures of the files currently being uploaded.

               Common architectures are amd64, armel, i386, etc.  Note that
               the special all value is meant for packages that are
               architecture independent (such as shell and Perl scripts or
               documentation).  If the source for the package is also being
               uploaded, the special entry source is also present.

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

           Distribution: distributions (required)
               Lists one or more space-separated distributions where this
               version should be installed when it is uploaded to the
               archive.

           Urgency: urgency (recommended)
               The urgency of the upload.  The currently known values, in
               increasing order of urgency, are: low, medium, high, critical
               and emergency.

           Maintainer: fullname-email (required)
               Should be in the format “Joe Bloggs <jbloggs@example.org>”,
               and is typically the person who created the package, as
               opposed to the author of the software that was packaged.

               The format is described in deb-email(7).

           Changed-By: fullname-email
               Should be in the format “Joe Bloggs <jbloggs@example.org>”,
               and is typically the person who prepared the package changes
               for this release.

               The format is described in deb-email(7).

           Description: (recommended)
            binary-package-name - binary-package-summary
               This multiline field contains a list of binary package names
               followed by a space, a dash (‘-’) and their possibly truncated
               short descriptions.  If the upload is source-only, then the
               field is omitted (since dpkg 1.19.3).

           Closes: bug-number-list
               A space-separated list of bug report numbers for bug reports
               that have been resolved with this upload.  The distribution
               archive software might use this field to automatically close
               the referred bug numbers in the distribution bug tracking
               system.

           Binary-Only: yes
               This field denotes that the upload is a binary-only
               non-maintainer build.  It originates from the binary-only=yes
               key/value from the changelog metadata entry.

           Built-For-Profiles: profile-list
               This field specifies a whitespace separated list of build
               profile names (without exclamation marks) that this upload was
               built with.

           Changes: (required)
            changelog-entries
               This multiline field contains the concatenated text of all
               changelog entries that are part of the upload.  To make this a
               valid multiline field empty lines are replaced with a single
               full stop (‘.’) and all lines are indented by one space
               character.  The exact content depends on the changelog format.

           Files: (required)
            md5sum size section priority filename
               This multiline field contains a list of files with an md5sum,
               size, section and priority for each one.

               The first line of the field value (the part on the same line
               as the field name followed by a colon) is always empty.  The
               content of the field is expressed as continuation lines, one
               line per file.  Each line consists of space-separated entries
               describing the file: the md5sum, the file size, the file
               section, the file priority, and the file name.

               If the section is omitted in the source package template
               control file, it defaults to unknown (since dpkg 1.22.13).

               If the priority is omitted in the source package template
               control file, it defaults to optional (since dpkg 1.22.13).

               This field lists all files that make up the upload.  The list
               of files in this field must match the list of files in the
               other related Checksums fields.

               Note: The MD5 checksum is considered weak, and should never be
               assumed to be sufficient for secure verification, but this
               field cannot be omitted as it provides metadata not available
               anywhere else.

           Checksums-Sha1: (required, weak)
           Checksums-Sha256: (required, strong)
            checksum size filename
               These multiline fields contain a list of files with a checksum
               and size for each one.  These fields have the same syntax and
               differ only in the checksum algorithm used: SHA-1 for
               Checksums-Sha1 and SHA-256 for Checksums-Sha256.

               The first line of the field value (the part on the same line
               as the field name followed by a colon) is always empty.  The
               content of the field is expressed as continuation lines, one
               line per file.  Each line consists of space-separated entries
               describing the file: the checksum, the file size, and the file
               name.

               These fields list all files that make up the upload.  The list
               of files in these fields must match the list of files in the
               Files field and the other related Checksums fields.

               Note: The SHA-1 checksum is considered weak, and should never
               be assumed to be sufficient for secure verification.

## [](#BUGS)BUGS

           The Files field is inconsistent with the other Checksums fields.
           The Changed-By and Maintainer fields have confusing names.  The
           Distribution field contains information about what is commonly
           referred to as a suite.

## [](#SEE_ALSO)SEE ALSO

           deb822(5), deb-src-control(5), deb-email(7), deb-version(7).

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

    1.23.7-216-gff7e9               2026-03-07                 deb-changes(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-genchanges(1)](../man1/dpkg-genchanges.1.html),  [deb-buildinfo(5)](../man5/deb-buildinfo.5.html),  [deb-changelog(5)](../man5/deb-changelog.5.html),  [deb-src-control(5)](../man5/deb-src-control.5.html)

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
