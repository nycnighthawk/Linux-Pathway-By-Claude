---
{"title": "ctrlaltdel(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ctrlaltdel.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ctrlaltdel(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CTRLALTDEL(8)             System Administration             CTRLALTDEL(8)

## [](#NAME)NAME

           ctrlaltdel - set the function of the Ctrl-Alt-Del combination

## [](#SYNOPSIS)SYNOPSIS

           ctrlaltdel hard|soft

## [](#DESCRIPTION)DESCRIPTION

           Based on examination of the linux/kernel/reboot.c code, it is
           clear that there are two supported functions that the
           <Ctrl-Alt-Del> sequence can perform.

           hard
               Immediately reboot the computer without calling sync(2) and
               without any other preparation. This is the default.

           soft
               Make the kernel send the SIGINT (interrupt) signal to the init
               process (this is always the process with PID 1). If this
               option is used, the init(8) program must support this feature.
               Since there are now several init(8) programs in the Linux
               community, please consult the documentation for the version
               that you are currently using.

           When the command is run without any argument, it will display the
           current setting.

           The function of ctrlaltdel is usually set in the /etc/rc.local
           file.

## [](#OPTIONS)OPTIONS

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#FILES)FILES

           /etc/rc.local

## [](#AUTHORS)AUTHORS

           Peter Orbaek <poe@daimi.aau.dk>

## [](#SEE_ALSO)SEE ALSO

           init(8), systemd(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The ctrlaltdel command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                  CTRLALTDEL(8)

------------------------------------------------------------------------

Pages that refer to this page: [reboot(2)](../man2/reboot.2.html)

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
