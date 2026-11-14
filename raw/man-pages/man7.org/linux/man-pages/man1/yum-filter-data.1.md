---
{"title": "yum-filter-data(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/yum-filter-data.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-filter-data(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [GENERAL OPTIONS](#GENERAL_OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yum-filter-data(1)                                     yum-filter-data(1)

## [](#NAME)NAME

           yum filter data plugin

## [](#SYNOPSIS)SYNOPSIS

           yum [options] [command] [package ...]

## [](#DESCRIPTION)DESCRIPTION

           This plugin extends yum with some options, currently just for
           "update" and "list update" type commands, to allow filters to be
           placed on which packages should be used based on the data in those
           packages. Note that due to some of the data being unknown, and
           thus could possibly match, all unknown data is treated as a match.

## [](#GENERAL_OPTIONS)GENERAL OPTIONS

           These are the options added to yum that are available in the "list
           updates", "info updates", "check-update" and "update" commands.
           They are:

           --filter-vendors
                  This option includes packages which have a vendor which
                  matches one of the passed vendor wildcard strings, or is
                  unknown. Note that vendors can have spaces in their value,
                  so "," is the only way to specify multiple vendors as one
                  option argument.

           --filter-rpm-groups
                  This option includes packages which have a group which
                  matches one of the passed rpm group wildcard strings, or is
                  unknown. Note that rpm groups can have spaces in their
                  value, so "," is the only way to specify multiple rpm
                  groups as one option argument.

           --filter-packagers
                  This option includes packages which have a packager which
                  matches one of the passed packager wildcard strings, or is
                  unknown. Note that vendors can have spaces in their value,
                  so "," is the only way to specify multiple packagers as one
                  option argument.

           --filter-licenses
                  This option includes packages which have a license which
                  matches one of the passed license wildcard strings, or is
                  unknown. Note that licenses can have spaces in their value,
                  so "," is the only way to specify multiple licenses as one
                  option argument.

           --filter-arches
                  This option includes packages which have a arch which
                  matches one of the passed arch wildcard strings, or is
                  unknown.

           --filter-committers
                  This option includes packages which have a committer which
                  matches one of the passed committer wildcard strings, or is
                  unknown. Note that committers can have spaces in their
                  value, so "," is the only way to specify multiple
                  committers as one option argument. Also, committer values
                  are so loosely formed that they could contain commas too,
                  it is recommended to not do that but you can work around it
                  by using "?".

           --filter-buildhosts
                  This option includes packages which have a buildhost which
                  matches one of the passed buildhost wildcard strings, or is
                  unknown.

           --filter-urls
                  This option includes packages which have a url which
                  matches one of the passed url wildcard strings, or is
                  unknown.

           --filter-package-sizes
                  This option includes packages which have a packagesize
                  which is within one of the passed packagesize ranges, or is
                  unknown.

           --filter-archive-sizes
                  This option includes packages which have a archivesize
                  which is within one of the passed archivesize ranges, or is
                  unknown.

           --filter-installed-sizes
                  This option includes packages which have a installedsize
                  which is within one of the passed installedsize ranges, or
                  is unknown.

           --filter-groups
                  This option includes packages which are in a yum group
                  which matches one of the passed yum group id strings, or is
                  unknown. Note that yum groups can have spaces in their
                  value, so "," is the only way to specify multiple yum
                  groups as one option argument.

## [](#EXAMPLES)EXAMPLES

           To list all updates that are 1 MB or less use:

                  yum --filter-package-sizes=-1m check-update

           To apply updates that Dan Walsh has committed use:

                  yum --filter-committers='Dan Walsh *' update

           To list updates for a specific group use:

                  yum --filter-rpm-groups='App*/Sys*' list updates

           To apply updates to a specific set of groups use:

                  yum --filter-rpm-groups='App*/System,Devel*/Lib*,System
                  Environment/Base' update

           To list updates for a set of yum groups use:

                  yum --filter-groups='PostgreSQL Database,Web Server' list
                  updates

           To apply updates to a specific set of yum groups use:

                  yum --filter-groups='KDE,Core,Printing Support' update

## [](#SEE_ALSO)SEE ALSO

           yum-list-data(1)
           yum(8)
           yum.conf(5)

## [](#AUTHORS)AUTHORS

           James Antill <james.antill@redhat.com>.

## [](#BUGS)BUGS

           Currently yum can't filter packages in all of the commands, so for
           instance "yum list 'yum*'" doesn't get the results filtered.

           Apart from that there are no bugs, but should you find any, you
           should first consult the FAQ section on
           http://yum.baseurl.org/wiki/Faq and if unsuccessful in finding a
           resolution contact the mailing list: yum-devel@lists.baseurl.org.
           To file a bug use http://bugzilla.redhat.com for
           Fedora/RHEL/Centos related bugs and http://yum.baseurl.org/report
           for all other bugs.

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

    James Antill                 04 February 2008          yum-filter-data(1)

------------------------------------------------------------------------

Pages that refer to this page: [yum-list-data(1)](../man1/yum-list-data.1.html)

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
