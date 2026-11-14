---
{"title": "depmod.d(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/depmod.d.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# depmod.d(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION FORMAT](#CONFIGURATION_FORMAT) \| [CONFIGURATION DIRECTORIES AND PRECEDENCE](#CONFIGURATION_DIRECTORIES_AND_PRECEDENCE) \| [COMMANDS](#COMMANDS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DEPMOD.D(5)                      depmod.d                     DEPMOD.D(5)

## [](#NAME)NAME

           depmod.d - Configuration directory for depmod

## [](#SYNOPSIS)SYNOPSIS

           /etc/depmod.d/*.conf

           /run/depmod.d/*.conf

           /usr/local/lib/depmod.d/*.conf

           /usr/local/lib/depmod.d/*.conf

           /lib/depmod.d/*.conf

## [](#DESCRIPTION)DESCRIPTION

           On execution depmod reads the configuration files from the above
           location and based on that it processes the available modules and
           their dependencies. For example: one can change the search order,
           exclude folders, override specific module's location and more.

           This is typically useful in cases where built-in kernel modules
           are complemented by custom built versions of the same and the user
           wishes to affect the priority of processing in order to override
           the module version supplied by the kernel.

## [](#CONFIGURATION_FORMAT)CONFIGURATION FORMAT

           The configuration files contain one command per line, with blank
           lines and lines starting with '#' ignored (useful for adding
           comments). A '\' at the end of a line causes it to continue on the
           next line, which makes the files a bit neater.

           See the COMMANDS section below for more.

## [](#CONFIGURATION_DIRECTORIES_AND_PRECEDENCE)CONFIGURATION DIRECTORIES AND PRECEDENCE

           Configuration files are read from directories in listed in
           SYNOPSIS in that order of precedence. Once a file of a given
           filename is loaded, any file of the same name in subsequent
           directories is ignored.

           All configuration files are sorted in lexicographic order,
           regardless of the directory they reside in. Configuration files
           can either be completely replaced (by having a new configuration
           file with the same name in a directory of higher priority) or
           partially replaced (by having a configuration file that is ordered
           later).

## [](#COMMANDS)COMMANDS

           search subdirectory
               This allows you to specify the order in which /lib/modules (or
               other configured module location) subdirectories will be
               processed by depmod. Directories are listed in order, with the
               highest priority given to the first listed directory and the
               lowest priority given to the last directory listed. The
               special keyword built-in refers to the standard module
               directories installed by the kernel. Another special keyword
               external refers to the list of external directories, defined
               by the external command.

               By default, depmod will give a higher priority to a directory
               with the name updates using this built-in search string:
               "updates built-in" but more complex arrangements are possible
               and are used in several popular distributions.

           override modulename kernelversion modulesubdirectory
               This command allows you to override which version of a
               specific module will be used when more than one module sharing
               the same name is processed by the depmod command. It is
               possible to specify one kernel or all kernels using the *
               wildcard. modulesubdirectory is the name of the subdirectory
               under /lib/modules (or other module location) where the target
               module is installed.

               For example, it is possible to override the priority of an
               updated test module called kmod by specifying the following
               command: "override kmod * extra". This will ensure that any
               matching module name installed under the extra subdirectory
               within /lib/modules (or other module location) will take
               priority over any likenamed module already provided by the
               kernel.

           external kernelversion absolutemodulesdirectory
               This specifies a list of directories, which will be checked
               according to the priorities in the search command. The order
               matters also, the first directory has the higher priority.

               The kernelversion is a POSIX regular expression or * wildcard,
               like in the override.

           exclude excludedir
               This specifies the trailing directories that will be excluded
               during the search for kernel modules.

               The excludedir is the trailing directory to exclude.

## [](#SEE_ALSO)SEE ALSO

           depmod(8)

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

    kmod                            2026-08-03                    DEPMOD.D(5)

------------------------------------------------------------------------

Pages that refer to this page: [depmod(8)](../man8/depmod.8.html)

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
