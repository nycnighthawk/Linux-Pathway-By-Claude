---
{"title": "rpm-manifest(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/rpm-manifest.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-manifest(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-MANIFEST(5)            File Formats Manual            RPM-MANIFEST(5)

## [](#NAME)NAME

           rpm-manifest - rpm package manifest file format

## [](#SYNOPSIS)SYNOPSIS

           GLOB ...

           # COMMENT

## [](#DESCRIPTION)DESCRIPTION

           RPM package manifest files are plaintext files containing one or
           more glob(7) entries that are expected to match either RPM package
           files or other package manifests.

           Package manifests can be used as a way to document installation of
           large package sets in an RPM-native way, without having to set up
           repositories and configure external dependency resolver programs
           to use them. For end-user purposes manifests are clumsy, but for
           example to quickly install a base image from a pre-determined set
           of package versions from local directory, a manifest may well be
           easier and faster than using a depsolver for the task. A manifest
           can be also used to work around command line length limitations.

           Relative globs are interpreted relative to the user's current
           directory. Multiple globs per line are permitted, but for
           readability it's recommended to use one per line instead.

           Lines beginning with # are considered comments. Empty lines and
           lines consisting of only whitespace are ignored.

## [](#EXAMPLES)EXAMPLES

       Example 1. Manifest of all myproj-1.0 releases and their dependencies
               /mnt/myproj/rpm/myproj-1.0-*.x86_64.rpm
               /mnt/deplib/rpm/mylib-2.1-*.x86_64.rpm

       Example 2. Manifest of all noarch packages in the default rpmbuild(1)
           location
               ~/rpmbuild/RPMS/noarch/*.rpm

       Example 3. Manifest as a simple base image
           Create a manifest called mymanifest.mft of currently installed
           packages, assuming a base path of /mnt/Packages for the RPM
           package files, and install it to an alternative system root at
           /srv/test:

               rpm -qa --qf '/mnt/Packages/%{nevra}.rpm\n' > mymanifest.mft
               rpm -Uv --root /srv/test mymanifest.mft

## [](#SEE_ALSO)SEE ALSO

           rpm(8) rpm-common(8)

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

    RPM 6.1.90                      2026-08-03                RPM-MANIFEST(5)

------------------------------------------------------------------------

Pages that refer to this page: [rpmgraph(1)](../man1/rpmgraph.1.html),  [rpm(8)](../man8/rpm.8.html)

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
