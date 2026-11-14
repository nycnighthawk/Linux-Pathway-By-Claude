---
{"title": "dh_movetousr(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_movetousr.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_movetousr(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_MOVETOUSR(1)                 Debhelper                 DH_MOVETOUSR(1)

## [](#NAME)NAME

           dh_movetousr - canonicalize location according to merged-/usr

## [](#SYNOPSIS)SYNOPSIS

           dh_movetousr [debhelper options] [--fail-noop | --warn-noop]

## [](#DESCRIPTION)DESCRIPTION

           dh_movetousr is a debhelper program that canonicalizes paths
           inside packages according to merged-/usr.  Shipping aliased paths
           is known to cause problems with dpkg, so this helper moves all
           affected files to /usr regardless of how they were installed.  The
           compatibility symlinks ensure that converted packages continue to
           work.  In the process, absolute symbolic links may become relative
           or vice versa due to Debian policy section 10.5.

           Please keep in mind that moving files in this way is known to
           cause problems.  Known problems have been documented at
           <https://people.debian.org/~helmutg/dep17.html>.  For instance, if
           files have been moved between packages, use of this tool may cause
           file loss during upgrades (P1).  Most problems can be detected by
           <https://salsa.debian.org/helmutg/dumat>, which uses the Debian
           bug tracking for feedback.  Therefore, it is recommended to upload
           to experimental when moving files (e.g. using this helper) or
           restructuring packages that earlier moved files.  A particular
           problem not being detected is about dpkg-statoverride (P5).
           Please review uses of dpkg-statoverride in maintainer scripts and
           update them as needed.  For these reasons, dh_movetousr is not
           automatically enabled in e.g. a compatibility level.

           While we want to move files to /usr in trixie and beyond, we do
           not want to move them in bookworm and earlier.  This poses
           challenges to backporting packages, because any such moves have to
           be reverted during the backport.  A backport of debhelper to
           bookworm shall include a stub for this helper doing nothing to
           achieve this goal.  For packages that do not need to be backported
           (e.g. packages targeting forky and beyond), consider updating
           locations instead of using this helper.  When the only affected
           type of file is systemd units, consider using dh_installsystemd or
           detecting the unit location from "pkgconf
           --variable=systemdsystemunitdir systemd" instead of this helper as
           both will work in backports.

           For further information on the state of the transition refer to
           <https://wiki.debian.org/UsrMerge>.

           dh_movetousr shall be removed from debhelper during forky+1 is
           release cycle.

## [](#OPTIONS)OPTIONS

           --fail-noop
               Fail if no files were found in aliased locations and therefore
               no change has been performed.

           --warn-noop
               Warn if no files were found in aliased locations and therefore
               no change has been performed.

## [](#EXAMPLES)EXAMPLES

             Build-Depends: dh-sequence-movetousr

           Enable this tool in a package that uses dh.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Helmut Grohne <helmut@subdivi.de>

## [](#COLOPHON)COLOPHON

           This page is part of the debhelper (helper programs for
           debian/rules) project.  Information about the project can be found
           at [unknown -- if you know, please contact man-pages@man7.org] If
           you have a bug report for this manual page, send it to
           submit@bugs.debian.org.  This page was obtained from the project's
           upstream Git repository
           ⟨https://salsa.debian.org/debian/debhelper.git⟩ on 2026-08-03.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    13.29                           2026-01-15                DH_MOVETOUSR(1)

------------------------------------------------------------------------

Pages that refer to this page: [debhelper(7)](../man7/debhelper.7.html)

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
