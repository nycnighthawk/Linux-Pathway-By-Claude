---
{"title": "switch_root(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/switch_root.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# switch_root(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SWITCH_ROOT(8)            System Administration            SWITCH_ROOT(8)

## [](#NAME)NAME

           switch_root - switch to another filesystem as the root of the
           mount tree

## [](#SYNOPSIS)SYNOPSIS

           switch_root [-hV]

           switch_root newroot init [arg...]

## [](#DESCRIPTION)DESCRIPTION

           switch_root moves already mounted /proc, /dev, /sys and /run to
           newroot and makes newroot the new root filesystem and starts init
           process.

           WARNING: switch_root removes recursively all files and directories
           on the current root filesystem.

## [](#OPTIONS)OPTIONS

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           switch_root returns 1 on failure, it never returns on success.

## [](#NOTES)NOTES

           switch_root will fail to function if newroot is not the root of a
           mount. If you want to switch root into a directory that does not
           meet this requirement then you can first use a bind-mounting trick
           to turn any directory into a mount point:

               mount --bind $DIR $DIR

## [](#AUTHORS)AUTHORS

           Peter Jones <pjones@redhat.com>, Jeremy Katz <katzj@redhat.com>,
           Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           chroot(2), init(8), mkinitrd(8), mount(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The switch_root command is part of the util-linux package which
           can be downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                 SWITCH_ROOT(8)

------------------------------------------------------------------------

Pages that refer to this page: [chroot(2)](../man2/chroot.2.html),  [pivot_root(2)](../man2/pivot_root.2.html),  [namespaces(7)](../man7/namespaces.7.html),  [pid_namespaces(7)](../man7/pid_namespaces.7.html),  [pivot_root(8)](../man8/pivot_root.8.html)

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
