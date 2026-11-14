---
{"title": "modinfo(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/modinfo.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# modinfo(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MODINFO(8)                       modinfo                       MODINFO(8)

## [](#NAME)NAME

           modinfo - Show information about a Linux Kernel module

## [](#SYNOPSIS)SYNOPSIS

           modinfo [-0] [-F field] [-k kernel] modulename|filename

           modinfo -V

           modinfo -h

## [](#DESCRIPTION)DESCRIPTION

           modinfo extracts information from the Linux Kernel modules given
           on the command line. If the module name is not a filename, then
           the /lib/modules/ version directory is searched, as is also done
           by modprobe(8) when loading kernel modules.

           modinfo by default lists each attribute of the module in form
           fieldname : value, for easy reading. The filename is listed the
           same way (although it's not really an attribute).

           This version of modinfo can understand modules of any Linux Kernel
           architecture.

## [](#OPTIONS)OPTIONS

           -V, --version
               Print the modinfo version.

           -F field, --field field
               Only print this field value, one per line. This is most useful
               for scripts. Field names are case-insensitive. Common fields
               (which may not be in every module) include author,
               description, license, parm, depends, and alias. There are
               often multiple parm, alias and depends fields. The special
               field filename lists the filename of the module.

           -b basedir, --basedir basedir
               Root directory for modules, / by default.

           -k kernel
               Provide information about a kernel other than the running one.
               This is particularly useful for distributions needing to
               extract information from a newly installed (but not yet
               running) set of kernel modules. For example, you wish to find
               which firmware files are needed by various modules in a new
               kernel for which you must make an initrd/initramfs image prior
               to booting.

           -0, --null
               Use the ASCII zero character to separate field values, instead
               of a new line. This is useful for scripts, since a new line
               can theoretically appear inside a field.

           -a --author, -d --description, -l --license, -p --parameters, -n
           --filename
               These are shortcuts for the --field flag's author,
               description, license, parm and filename arguments, to ease the
               transition from the old modutils modinfo.

           -h, --help
               Print the help message and exit.

## [](#SEE_ALSO)SEE ALSO

           modprobe(8)

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

    kmod                            2026-08-03                     MODINFO(8)

------------------------------------------------------------------------

Pages that refer to this page: [query_module(2)](../man2/query_module.2.html),  [modules.dep(5)](../man5/modules.dep.5.html),  [insmod(8)](../man8/insmod.8.html),  [kmod(8)](../man8/kmod.8.html),  [lsmod(8)](../man8/lsmod.8.html),  [modprobe(8)](../man8/modprobe.8.html),  [rmmod(8)](../man8/rmmod.8.html)

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
