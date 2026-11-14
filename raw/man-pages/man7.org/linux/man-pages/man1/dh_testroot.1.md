---
{"title": "dh_testroot(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_testroot.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_testroot(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_TESTROOT(1)                  Debhelper                  DH_TESTROOT(1)

## [](#NAME)NAME

           dh_testroot - ensure that a package is built with necessary level
           of root permissions

## [](#SYNOPSIS)SYNOPSIS

           dh_testroot [debhelper options]

## [](#DESCRIPTION)DESCRIPTION

           dh_testroot is used to determine if the target is being run with
           suffient access to root(-like) features.

           The definition of sufficient access depends on whether the builder
           (the tool invoking the debian/rules target) supports the
           Rules-Requires-Root (R³) field.  If the builder supports R³, then
           it will set the environment variable DEB_RULES_REQUIRES_ROOT and
           dh_testroot will validate that the builder followed the minimum
           requirements for the given value of DEB_RULES_REQUIRES_ROOT.

           If the builder does not support Rules-Requires-Root, then it will
           not set the DEB_RULES_REQUIRES_ROOT environment variable.  This
           will in turn make dh_testroot (and the rest of debhelper) fall
           back to assuming that (fake)root is implied.

           The following is a summary of how dh_testroot behaves based on the
           DEB_RULES_REQUIRES_ROOT environment variable (leading and trailing
           whitespace in the variable is ignored).

           -   If unset, or set to "binary-targets", then dh_testroot asserts
               that it is run as root or under fakeroot(1).

           -   If set to "no", then dh_testroot returns successfully (without
               performing any additional checks).

           -   If set to any other value than the above, then dh_testroot
               asserts that it is either run as root (or under fakeroot(1))
               or the builder has provided the DEB_GAIN_ROOT_CMD environment
               variable (e.g. via dpkg-buildpackage -r).

           Please note that dh_testroot does not read the Rules-Requires-Root
           field.  Which implies that dh_testroot may produce incorrect
           result if the builder lies in DEB_RULES_REQUIRES_ROOT.  On the
           flip side, it also enables things like testing for what will
           happen when DEB_RULES_REQUIRES_ROOT is set to a given value.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Joey Hess <joeyh@debian.org>

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

    13.29                           2026-01-15                 DH_TESTROOT(1)

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
