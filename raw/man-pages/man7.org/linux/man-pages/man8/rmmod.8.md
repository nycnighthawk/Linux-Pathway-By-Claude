---
{"title": "rmmod(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rmmod.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rmmod(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RMMOD(8)                          rmmod                          RMMOD(8)

## [](#NAME)NAME

           rmmod - Simple program to remove a module from the Linux Kernel

## [](#SYNOPSIS)SYNOPSIS

           rmmod [OPTIONS] modulenames

## [](#DESCRIPTION)DESCRIPTION

           rmmod is a trivial program to remove a module or a list of modules
           from the kernel (when module unloading support is provided). Most
           users will want to use modprobe(8) with the -r option instead
           since it removes unused dependent modules as well.

           When a list of modules is provided, the program will process them
           one at a time. If a module is not found, rmmod will immediately
           exit with an error code. Should the module removal fail, the
           program will log an error AND continue with the next module. This
           behaviour is NOT controlled by the --force option.

## [](#OPTIONS)OPTIONS

           -f, --force
               This option can be extremely dangerous: it has no effect
               unless CONFIG_MODULE_FORCE_UNLOAD was set when the kernel was
               compiled. With this option, you can remove modules which are
               being used, or which are not designed to be removed, or have
               been marked as unsafe (see lsmod(8)).

           -s, --syslog
               Send errors to syslog instead of standard error.

           -v, --verbose
               Print messages about what the program is doing. Usually rmmod
               prints messages only if something goes wrong.

           -V, --version
               Show version of program and exit.

           -h, --help
               Print the help message and exit.

## [](#SEE_ALSO)SEE ALSO

           modprobe(8), insmod(8), lsmod(8), modinfo(8), depmod(8)

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

    kmod                            2026-08-03                       RMMOD(8)

------------------------------------------------------------------------

Pages that refer to this page: [delete_module(2)](../man2/delete_module.2.html),  [insmod(8)](../man8/insmod.8.html),  [kmod(8)](../man8/kmod.8.html),  [modprobe(8)](../man8/modprobe.8.html)

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
