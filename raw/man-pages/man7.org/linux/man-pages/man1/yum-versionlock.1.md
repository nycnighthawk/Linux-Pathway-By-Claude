---
{"title": "yum-versionlock(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/yum-versionlock.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-versionlock(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [BUGS](#BUGS) \| [AVAILABILITY](#AVAILABILITY) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    YUM-VERSIONLOCK(1)             User Manuals            YUM-VERSIONLOCK(1)

## [](#NAME)NAME

           yum-versionlock - Version lock rpm packages

## [](#SYNOPSIS)SYNOPSIS

           yum-versionlock [ package-name [ package-name]] ...

## [](#DESCRIPTION)DESCRIPTION

           yum-versionlock(1) is a Yum plugin that takes a set of
           name/versions for packages and excludes all other versions of
           those packages (including optionally following obsoletes).  This
           allows you to protect packages from being updated by newer
           versions.

           The plugin provides a command "versionlock" which allows you to
           view and edit the list of locked packages easily.

           yum versionlock add <package-wildcard>...
                  Add a versionlock for all of the packages in the rpmdb
                  matching the given wildcards.

           yum versionlock exclude <package-wildcard>...
                  Opposite; disallow currently available versions of the
                  packages matching the given wildcards.

           yum versionlock list
                  List the current versionlock entries.

           yum versionlock status
                  List any available updates that are currently blocked by
                  versionlock.  That is, for each entry in the lock list,
                  print the newest package available in the repos unless it
                  is the particular locked/excluded version.

           yum versionlock delete <entry-wildcard>...
                  Remove any matching versionlock entries.

           yum versionlock clear
                  Remove all versionlock entries.

## [](#FILES)FILES

           /etc/yum/pluginconf.d/versionlock.conf
                  The system wide configuration file. See
                  yum-versionlock.conf(5) for more information.
           /etc/yum/pluginconf.d/versionlock.list
                  The default place to put package version lock information
                  (one package and version per. line). The file takes entries
                  in the following format EPOCH:NAME-VERSION-RELEASE.ARCH See
                  rpm(8) for more information on custom query formats. If the
                  package does not have an EPOCH the number will default to
                  0.

## [](#BUGS)BUGS

           There are of course no bugs, but should you find any, you should
           first consult the FAQ section on http://yum.baseurl.org/wiki/Faq
           and if unsuccessful in finding a resolution contact the mailing
           list: yum-devel@lists.baseurl.org.  To file a bug use
           http://bugzilla.redhat.com for Fedora/RHEL/Centos related bugs and
           http://yum.baseurl.org/report for all other bugs.

## [](#AVAILABILITY)AVAILABILITY

           yum-versionlock is available via:
           # yum install yum-versionlock

## [](#AUTHORS)AUTHORS

           Panu Matilainen <pmatilai@laiskiainen.org>
           James Antill <james@and.org>
           Documentation modified by:
           Gerhardus Geldenhuis <gerhardus.geldenhuis@gmail.com>

## [](#SEE_ALSO)SEE ALSO

           yum(1)

## [](#COLOPHON)COLOPHON

           This page is part of the yum-utils (Yum Package Manager utilities)
           project.  Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/yum⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/yum-utils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2020-03-11.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                 28 December 2009          YUM-VERSIONLOCK(1)

------------------------------------------------------------------------

Pages that refer to this page: [yum-versionlock(1)](../man1/yum-versionlock.1.html),  [yum-versionlock.conf(5)](../man5/yum-versionlock.conf.5.html)

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
