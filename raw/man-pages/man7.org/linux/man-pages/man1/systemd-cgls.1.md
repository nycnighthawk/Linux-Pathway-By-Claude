---
{"title": "systemd-cgls(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-cgls.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-cgls(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-CGLS(1)                systemd-cgls               SYSTEMD-CGLS(1)

## [](#NAME)NAME

           systemd-cgls - Recursively show control group contents

## [](#SYNOPSIS)SYNOPSIS

           systemd-cgls [OPTIONS...] [CGROUP...]

           systemd-cgls [OPTIONS...] --unit|--user-unit [UNIT...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-cgls recursively shows the contents of the selected Linux
           control group hierarchy in a tree. If arguments are specified,
           shows all member processes of the specified control groups plus
           all their subgroups and their members. The control groups may
           either be specified by their full file paths or are assumed in the
           systemd control group hierarchy. If no argument is specified and
           the current working directory is beneath the control group mount
           point /sys/fs/cgroup/, shows the contents of the control group the
           working directory refers to. Otherwise, the full systemd control
           group hierarchy is shown.

           By default, empty control groups are not shown.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --all
               Do not hide empty control groups in the output.

           -l, --full
               Do not ellipsize process tree members.

               Added in version 198.

           -u, --unit
               Show cgroup subtrees for the specified units.

               Added in version 233.

           --user-unit
               Show cgroup subtrees for the specified user units.

               Added in version 233.

           -k
               Include kernel threads in output.

           -M MACHINE, --machine=MACHINE
               Limit control groups shown to the part corresponding to the
               container MACHINE.

               Added in version 203.

           --xattr[=BOOL], -x
               Controls whether to include information about extended
               attributes of the listed control groups in the output. With
               the long option only, optionally accepts a boolean value.
               Defaults to no.

               Added in version 250.

           --cgroup-id[=BOOL], -c
               Controls whether to include the numeric ID of the listed
               control groups in the output. With the long option only,
               optionally accepts a boolean value. Defaults to no.

               Added in version 250.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

           --no-pager
               Do not pipe output into a pager.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), systemd-cgtop(1), systemd-nspawn(1),
           ps(1)

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                         SYSTEMD-CGLS(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd(1)](../man1/systemd.1.html),  [systemd-cgtop(1)](../man1/systemd-cgtop.1.html),  [cgroups(7)](../man7/cgroups.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-machined.service(8)](../man8/systemd-machined.service.8.html)

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
