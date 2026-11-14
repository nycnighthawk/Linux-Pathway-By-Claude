---
{"title": "rpm-version(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/rpm-version.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-version(7) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-VERSION(7)       Miscellaneous Information Manual      RPM-VERSION(7)

## [](#NAME)NAME

           rpm-version - RPM version system

## [](#SYNOPSIS)SYNOPSIS

           [EPOCH:]VERSION[-RELEASE]

## [](#DESCRIPTION)DESCRIPTION

           A label known as EVR is used to refer to software versions in RPM,
           consisting of up to three components:

           •   VERSION reflects the actual packaged software version.
           •   RELEASE reflects packaging revisions within that software
               version.
           •   EPOCH is an artificial override to allow working around
               versioning anomalies.

           Only the VERSION component is mandatory in an EVR label. All RPM
           packages have a VERSION and a RELEASE, however.

       Version
           The VERSION string reflects the actual packaged software version.

           The string consists of ASCII alphanumeric characters, optionally
           segmented with the separators period (.), underscore (_) and the
           plus sign (+), and operators tilde (~) and caret (^).

           The operators are used to map pre- and post-release version
           strings into a coherent upgrade.

           Notably, the dash character (-) can NOT be used in VERSION or
           RELEASE as it is the component separator.

       Release
           The RELEASE reflects a revision within a single software version.
           Ideally, RELEASE is a simple integer that is incremented whenever
           changes are made to a package, and should be reset (to 1) whenever
           the software version changes.

           Technically, the format is exactly the same as for VERSION.

       Epoch
           The EPOCH is a non-negative integer, separated from the version
           with a colon (:). It's the most significant part of an EVR,
           skewing version comparison to make an older version to appear
           newer. It's sometimes necessary to work around version anomalies
           such as a software project changing its versioning scheme, but
           also packaging errors.

           An omitted EPOCH  has an implicit value of zero.

           The epoch should be only used as a last resort. It violates the
           principle of least surprise, and changing it requires all related
           versioned dependencies in other packages to be updated
           accordingly.

       Comparing
           Two EVRs are compared left to right, one component at a time. The
           components are compared left to right, a segment at a time. The
           comparison stops as soon as a segment or component level
           difference is found, so if eg. the epochs differ, the rest of the
           EVR is not considered at all.

           Within components, consecutive alphabetic characters and
           consecutive numbers form implicit segments. Explicit segments are
           denoted by separators and operators. Numeric segments are compared
           numerically as integers with leading zeros ignored, otherwise
           lexicographical comparison is used. That is, abc123 consists of
           two segments: abc and 123 and is equal to abc0123, abc.123 and
           abc.000123 despite difference in appearance.

           Numeric segments are considered newer than alphabetic segments
           regardless of the actual content. When otherwise equal, the
           component with more segments is considered newer, and similarly an
           EVR with more components is considered newer. For example, 0.0 is
           newer than 0 and 1.xyz is older than 1.0 but newer than 1.

           The segment separator characters are not compared, so they can be
           used interchangeably, and multiple consecutive separators are
           treated as if only one separator was used. Thus, 1.0 is equal to
           1+0 and 1+.+0.

           The tilde operator causes a segment to sort older, and is used for
           pre-release versions. For example 2.0~beta1 is older than 2.0 or
           2.0~rc1, and newer than 1.0. The caret operator is essentially the
           opposite of tilde. It causes a segment to sort newer, and is used
           for post-release snapshots that exist between actual software
           releases. For example, 2.0^150825 is newer than 2.0 but older than
           2.0.1.

## [](#EXAMPLES)EXAMPLES

           123
               A simple one-segment version 123. Newer than 99, older than
               321.

           1.0.1
               A segmented version string 1.0.1, such as commonly used in
               software projects to indicate major.minor.micro semantics.
               Newer than 1.0, older than 1.0.2.

           2.60.1-1
               First release of version 2.60.1. Newer than 2.0 or 2.60, but
               older than 3.0.

           1.0-5
               Fifth release of version 1.0, newer than 1.0 or 1.0-1, older
               than 1.0.1.

           5:3.0-1
               First release of version 3.0, with epoch of 5. Newer than for
               6.0-1, or 4:6.0-1, older than 5:3.1-1.

           1.0~beta2
               Pre-release beta2 of version 1.0. Newer than 0.99 and
               1.0~beta1, older than 1.0.

           2.0^20250611
               Post-release snapshot 20250611 of version 2.0. Newer than 2.0,
               older than 2.0.1.

## [](#BUGS)BUGS

           Various non-obvious behaviors and dark corners exist within the
           version comparison algorithm, but are difficult to address due to
           high risk of breaking existing packages:

           •   Non-ASCII characters are ignored and thus equal: 1.1.α equals
               1.1.β and even 1.1.ββ. rpmbuild(1) rejects such EVRs but it's
               possible to encounter "illegal" values via API usage, very old
               packages and packages created with 3rd party tools.
           •   Implicit segments can be deceptive: 1.f is newer than 1c.f.
               The result becomes more obvious by making the segments
               explicit: 1.f is newer than 1.c.f because the segments are
               compared one by one, and c sorts lower than f
               lexicographically.

           rpm(8) rpmbuild(1) rpmsort(1)

           http://www.rpm.org/ 

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

    RPM 6.1.90                      2026-08-03                 RPM-VERSION(7)

------------------------------------------------------------------------

Pages that refer to this page: [rpmsort(1)](../man1/rpmsort.1.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [rpm-scriptlets(7)](../man7/rpm-scriptlets.7.html),  [rpm(8)](../man8/rpm.8.html),  [rpm-plugin-syslog(8)](../man8/rpm-plugin-syslog.8.html)

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
