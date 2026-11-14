---
{"title": "insmod(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/insmod.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# insmod(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    INSMOD(8)                         insmod                        INSMOD(8)

## [](#NAME)NAME

           insmod - Simple program to insert a module into the Linux Kernel

## [](#SYNOPSIS)SYNOPSIS

           insmod [OPTIONS] filename [module options]

## [](#DESCRIPTION)DESCRIPTION

           insmod is a trivial program to insert a module into the kernel.
           Most users will want to use modprobe(8) instead, which is more
           clever and can handle module dependencies.

           Only the most general of error messages are reported: as the work
           of trying to link the module is now done inside the kernel, the
           dmesg(1) usually gives more information about errors.

## [](#OPTIONS)OPTIONS

           -f, --force
               This option can be extremely dangerous: it tells the kernel to
               ignore the module version and vermagic fields when loading.
               With this option, you can load modules build locally or by
               third parties, although this can lead to memory corruption,
               system crashes and data loss. This is the same as using both
               --force-vermagic and --force-modversion.

           --force-modversion
               When modules are compiled with CONFIG_MODVERSIONS set, a
               section detailing the versions of every interfaced used by (or
               supplied by) the module is created. If a module fails to load
               and the kernel complains that the module disagrees about a
               version of some interface, you can use --force-modversion to
               remove the version information altogether.

           --force-vermagic
               Every module contains a small string containing important
               information, such as the kernel and compiler versions. If a
               module fails to load and the kernel complains that the
               "version magic" doesn't match, you can use this option to
               remove it. Naturally, this check is there for your protection,
               so using this option is dangerous unless you know what you're
               doing.

           -s, --syslog
               Send errors to syslog instead of standard error.

           -v, --verbose
               Print messages about what the program is doing. Usually insmod
               prints messages only if something goes wrong.

           -V, --version
               Show version of program and exit.

           -h, --help
               Print the help message and exit.

## [](#SEE_ALSO)SEE ALSO

           modprobe(8), rmmod(8), lsmod(8), modinfo(8), depmod(8)

## [](#AUTHORS)AUTHORS

           Numerous contributions have come from the linux-modules mailing
           list <linux-modules@vger.kernel.org> and Github. If you have a
           clone of kmod.git itself, the output of git-shortlog(1) and
           git-blame(1) can show you the authors for specific parts of the
           project.

           Lucas De Marchi <lucas.de.marchi@gmail.com> is the current
           maintainer of the project.

## [](#BUGS)BUGS

           Please direct any bug reports to kmod's issue tracker at
           https://github.com/kmod-project/kmod/issues/ alongside with
           version used, steps to reproduce the problem and the expected
           outcome.

## [](#COLOPHON)COLOPHON

           This page is part of the kmod (userspace tools for managing kernel
           modules) project.  Information about the project can be found at
           [unknown -- if you know, please contact man-pages@man7.org] If you
           have a bug report for this manual page, send it to
           linux-modules@vger.kernel.org.  This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-28.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    kmod                            2026-08-03                      INSMOD(8)

------------------------------------------------------------------------

Pages that refer to this page: [sk98lin(4)](../man4/sk98lin.4.html),  [wavelan(4)](../man4/wavelan.4.html),  [lvmthin(7)](../man7/lvmthin.7.html),  [kmod(8)](../man8/kmod.8.html),  [lsmod(8)](../man8/lsmod.8.html),  [modprobe(8)](../man8/modprobe.8.html),  [rmmod(8)](../man8/rmmod.8.html)

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
