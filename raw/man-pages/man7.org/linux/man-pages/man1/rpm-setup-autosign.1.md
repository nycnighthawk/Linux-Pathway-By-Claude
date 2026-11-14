---
{"title": "rpm-setup-autosign(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rpm-setup-autosign.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-setup-autosign(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [EXIT STATUS](#EXIT_STATUS) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-SETUP-AUTOSIGN(1)    General Commands Manual    RPM-SETUP-AUTOSIGN(1)

## [](#NAME)NAME

           rpm-setup-autosign - Set up automatic signing for rpmbuild

## [](#SYNOPSIS)SYNOPSIS

           rpm-setup-autosign [options]

## [](#DESCRIPTION)DESCRIPTION

           rpm-setup-autosign is used to set up automatic signing from
           rpmbuild(1). It generates a user- and host-specific, passwordless
           OpenPGP key, configures rpmbuild(1) to use that key and exports
           the public key (aka certificate) for importing to the persistent
           rpm(8) keyring.

           The purpose of automatic signing is to make testing local builds
           painless. For distributing packages, it's recommended to use a
           separate signing account that cannot be compromised by a build.

## [](#OPTIONS)OPTIONS

           -p <gpg|sq>, --prog <gpg|sq>
               Specify the signing program to use: GnuPG or Sequoia PGP's sq.

## [](#CONFIGURATION)CONFIGURATION

           On successful completion, one or more of the following macros will
           be configured in the user's macro configuration file. See
           rpm-config(5) for details:
           •   %_openpgp_autosign_id
           •   %_openpgp_sign

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#FILES)FILES

           ~/.config/rpm/rpmbuild-*.asc
           ~/.config/rpm/macros

## [](#EXAMPLES)EXAMPLES

           rpm-setup-autosign -p sq
               Set up rpmbuild(1) autosigning using Sequoia-sq.

## [](#SEE_ALSO)SEE ALSO

           rpm(8) rpmsign(1) rpmbuild(1)

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

    RPM 6.1.90                      2026-08-03          RPM-SETUP-AUTOSIGN(1)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild(1)](../man1/rpmbuild.1.html)

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
