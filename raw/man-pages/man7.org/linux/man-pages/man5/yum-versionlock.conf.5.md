---
{"title": "yum-versionlock.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/yum-versionlock.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-versionlock.conf(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [FILES](#FILES) \| [FILE FORMAT](#FILE_FORMAT) \| [OPTIONS](#OPTIONS) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    YUM-VERSIONLOCK.CONF(5)        File Formats       YUM-VERSIONLOCK.CONF(5)

## [](#NAME)NAME

           yum-versionlock.conf(5)

## [](#SYNOPSIS)SYNOPSIS

           yum-versionlock.conf(5) is the configuration file for
           yum-versionlock(1) Yum plugin for excluding packages that aren't
           listed in the versionlock file.  The plugin will walk each line of
           the versionlock file, parse out the name and version of the
           package. It will then exclude any package by that name that
           doesn't match one of the versions listed within the file (or,
           optionally, any obsoleter of that package).  This is basically the
           same as doing an exclude for the package name itself (as you
           cannot exclude installed packages), but yum will still see the
           versions you have installed/versionlocked as available so that
           "yum reinstall" will still work, etc.  It can also work in the
           opposite way, like a fast exclude, by prefixing a '!'  character
           to the version.

## [](#FILES)FILES

           /etc/yum/pluginconf.d/versionlock.conf

## [](#FILE_FORMAT)FILE FORMAT

           yum-versionlock.conf(5) utilizes configuration options in the form
           of

           OPTION=VALUE

## [](#OPTIONS)OPTIONS

           follow_obsoletes
                  This option is a boolean flag which specifies if the
                  versionlock plugin should look at all the obsoletes, and
                  see if any of the packages specified have an obsoleter. If
                  an obsoleter is found then all versions of that package
                  will be excluded. This option is off by default, as
                  yum-versionlock(1) will take some time to do the obsoletes
                  processing, and for non-rename obsoletes any issues you had
                  which kept you at a specific version of a package should be
                  different with another package.

           locklist
                  This option is a string with points to the file which will
                  have the versionlock information in it. Note that the file
                  has to exist (or the versionlock plugin will make yum
                  exit). However it can be empty.

           show_hint
                  This option is a boolean flag which specifies if the
                  versionlock plugin should print a hint message whenever yum
                  runs saying how many package updates available from the
                  repos are being blocked due to versionlocks.  This hint
                  serves as a reminder that there are locks in effect and
                  that you may want to reconsider them since newer versions
                  of those packages have been released.  Default is 1 (show
                  the hint).

## [](#AUTHOR)AUTHOR

                  Chitlesh Goorah <chitlesh@fedoraproject.org>
                  James Antill <james@fedoraproject.org>

## [](#SEE_ALSO)SEE ALSO

           yum-versionlock(1)

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

                                   27 July 2008       YUM-VERSIONLOCK.CONF(5)

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
