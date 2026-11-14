---
{"title": "deb-changelog(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-changelog.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-changelog(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-changelog(5)                dpkg suite               deb-changelog(5)

## [](#NAME)NAME

           deb-changelog - dpkg source packages' changelog file format

## [](#SYNOPSIS)SYNOPSIS

           debian/changelog

## [](#DESCRIPTION)DESCRIPTION

           Changes in the packaged version of a project are explained in the
           changelog file debian/changelog.  This includes modifications made
           in the source package compared to the upstream one as well as
           other changes and updates to the package.

           The format of the debian/changelog allows the package building
           tools to discover which version of the package is being built and
           find out other release-specific information.

           That format is a series of entries like this:

            package (version) distributions; metadata
                     [optional blank line(s), stripped]
             * change-details
               more-change-details
                     [blank line(s), included in dpkg-parsechangelog(1)
           output]
             * even-more-change-details
                     [optional blank line(s), stripped]
             -- maintainer-name <email-address>  date

           package and version are the source package name and version
           number.  version is delimited by parenthesis U+00028 ‘(’ and
           U+0029 ‘)’.

           distributions lists one or more space-separated distributions
           where this version should be installed when it is uploaded; it is
           copied to the Distribution field in the .changes file.
           distributions must be terminated by a semicolon (U+003B ‘;’).

           metadata lists zero or more comma-separated keyword=value items.
           Each keyword can contain only minus and case insensitive
           alphanumeric characters, as they need to be mapped to deb822(5)
           field names.  The only keywords currently supported by dpkg are:

           urgency
               Its value is used for the Urgency field in the .changes file
               for the upload.

           binary-only
               With a yes value, it is used to denote that this changelog
               entry is for a binary-only non-maintainer upload (an automatic
               binary rebuild with the only change being the changelog
               entry).

           The change details may in fact be any series of lines starting
           with at least two spaces (U+0020 SPACE), but conventionally each
           change starts with an asterisk and a separating space and
           continuation lines are indented so as to bring them in line with
           the start of the text above.  Blank lines may be used here to
           separate groups of changes, if desired.

           If this upload resolves bugs recorded in the distribution bug
           tracking system, they may be automatically closed on the inclusion
           of this package into the distribution archive by including the
           string:

               Closes: #nnnnn

           in the change details, where #nnnnn is the bug number.  The exact
           Perl regular expression is:

               /closes:\s*(?:bug)?\#?\s?\d+(?:,\s*(?:bug)?\#?\s?\d+)*/i

           That is, the string should consist of the word closes: followed by
           a comma-separated list of bug numbers.  Bug numbers may be
           preceded by the word bug and/or a # sign, as in "Closes: 42,
           bug#43, #44, bug 45".  The words closes: and bug are not case
           sensitive.  The list of bug numbers may span multiple lines.

           This information is conveyed via the Closes field in the .changes
           file.  Where, depending on the archive maintenance software, all
           the bug numbers listed might get automatically closed.

           The maintainer name and email address used in the changelog should
           be the details of the person who prepared this release of the
           package.  They are not necessarily those of the uploader or usual
           package maintainer.  The format for the name and email address is
           described in deb-email(7).  The information here will be copied to
           the Changed-By field in the .changes file, and then later might be
           used to send an acknowledgment when the upload has been installed
           in the distribution archive.

           The date has the following format (compatible and with the same
           semantics of RFC2822 and RFC5322, or what «date -R» generates):

               day-of-week, dd month yyyy hh:mm:ss +zzzz

           where:

           day-of-week
               Is one of: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

           dd  Is a one- or two-digit day of the month (01-31), where the
               leading zero is optional, but conventionally does not get
               omitted.

           month
               Is one of: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct,
               Nov, Dec.

           yyyy
               Is the four-digit year (e.g. 2010).

           hh  Is the two-digit hour (00-23).

           mm  Is the two-digit minutes (00-59).

           ss  Is the two-digit seconds (00-60).

           [+-]zzzz
               Is the time zone offset from Coordinated Universal Time (UTC).
               ‘+’ indicates that the time is ahead of (i.e., east of) UTC
               and ‘-’ indicates that the time is behind (i.e., west of) UTC.
               The first two digits indicate the hour difference from UTC and
               the last two digits indicate the number of additional minutes
               difference from UTC.  The last two digits must be in the range
               00-59.

           The first “title” line with the package name must start at the
           left hand margin.  The “trailer” line with the maintainer and date
           details must be preceded by exactly one space (U+0020 SPACE).  The
           maintainer details and the date must be separated by exactly two
           spaces (U+0020 SPACE).  Each part of the date can be separated by
           one or more spaces (U+0020 SPACE), except after the comma where it
           can be separated by zero or more spaces (U+0020 SPACE).

           Any line that consists entirely (i.e., no leading whitespace) of #
           or /* */ style comments or RCS keywords should be ignored.

           Vim modelines or Emacs local variables, and ancient changelog
           entries with other formats at the end of the file should be
           accepted and preserved on output, but their contents might be
           otherwise ignored and parsing stopped at that point.

           The entire changelog must be encoded in UTF-8.

## [](#FILES)FILES

           debian/changelog

## [](#EXAMPLES)EXAMPLES

            dpkg (1.17.18) unstable; urgency=low

             [ Guillem Jover ]
             * Handle empty minimum versions when initializing dependency versions,
               as the code is mapping the minimum version 0 to '' to avoid outputting
               useless versions. Regression introduced in dpkg 1.17.17. Closes: #764929

             [ Updated programs translations ]
             * Catalan (Guillem Jover).

             [ Updated dselect translations ]
             * Catalan (Guillem Jover).
             * German (Sven Joachim).

             -- Guillem Jover <guillem@debian.org>  Sun, 12 Oct 2014 15:47:44 +0200

## [](#SEE_ALSO)SEE ALSO

           deb822(5), deb-changes(5), deb-email(7), deb-version(7),
           dpkg-parsechangelog(1).

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

    1.23.7-216-gff7e9               2026-03-07               deb-changelog(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-genchanges(1)](../man1/dpkg-genchanges.1.html),  [dpkg-gencontrol(1)](../man1/dpkg-gencontrol.1.html),  [dpkg-parsechangelog(1)](../man1/dpkg-parsechangelog.1.html),  [dpkg-source(1)](../man1/dpkg-source.1.html),  [deb-buildinfo(5)](../man5/deb-buildinfo.5.html),  [deb-changes(5)](../man5/deb-changes.5.html)

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
