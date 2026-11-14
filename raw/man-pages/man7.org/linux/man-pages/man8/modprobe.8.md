---
{"title": "modprobe(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/modprobe.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# modprobe(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MODPROBE(8)                      modprobe                     MODPROBE(8)

## [](#NAME)NAME

           modprobe - Add and remove modules from the Linux Kernel

## [](#SYNOPSIS)SYNOPSIS

           modprobe [-v] [-V] [-C config-file] [-n] [-i] [-q] [-b] modulename
                    [module parameters]

           modprobe [-r] [-v] [-n] [-i] modulename

           modprobe [-c]

           modprobe [--show-modversions] filename

## [](#DESCRIPTION)DESCRIPTION

           modprobe intelligently adds or removes a module from the Linux
           kernel: note that for convenience, there is no difference between
           _ and - in module names (automatic underscore conversion is
           performed). modprobe looks in the module directory
           /lib/modules/$(uname -r) for all the modules and other files,
           except for the optional configuration files (see modprobe.d(5)).
           modprobe will also use module options specified on the kernel
           command line in the form of <module>.<option> and blacklists in
           the form of modprobe.blacklist=<module>.

           Note that unlike in 2.4 series Linux kernels (which are not
           supported by this tool) this version of modprobe does not do
           anything to the module itself: the work of resolving symbols and
           understanding parameters is done inside the kernel. So module
           failure is sometimes accompanied by a kernel message: see
           dmesg(8).

           modprobe expects an up-to-date modules.dep.bin file as generated
           by the corresponding depmod utility shipped along with modprobe
           (see depmod(8)). This file lists what other modules each module
           needs (if any), and modprobe uses this to add or remove these
           dependencies automatically.

           If any arguments are given after the modulename, they are passed
           to the kernel (in addition to any options listed in the
           configuration file).

           When loading modules, modulename can also be a path to the module.
           If the path is relative, it must explicitly start with "./". Note
           that this may fail when using a path to a module with dependencies
           not matching the installed depmod database.

## [](#OPTIONS)OPTIONS

           -a, --all
               Insert all module names on the command line.

           -b, --use-blacklist
               This option causes modprobe to apply the blacklist commands in
               the configuration files (if any) to module names as well. It
               is usually used by udev(7).

           -C directory, --config directory
               This option overrides the default configuration directory. See
               modprobe.d(5).

               This option is passed through install or remove commands to
               other modprobe commands in the MODPROBE_OPTIONS environment
               variable.

           -c, --show-config
               Print out the effective configuration from the config
               directory and exit.

               For compatibility reasons --showconfig is also accepted for
               this option but will be removed after kmod 36.

           --show-modversions
               Print out a list of module versioning information required by
               a module. This option is commonly used by distributions in
               order to package up a Linux kernel module using module
               versioning deps.

               For compatibility reasons --dump-modversions is also accepted
               for this option but will be removed after kmod 36.

           --show-exports
               Print out a list of symbols exported by the module. This
               option is commonly used to inspect the function list, while
               investigating loading of modules with partial or missing
               dependencies.

           -d, --dirname
               Root directory for modules, / by default.

           --first-time
               Normally, modprobe will succeed (and do nothing) if told to
               insert a module which is already present or to remove a module
               which isn't present. This is ideal for simple scripts;
               however, more complicated scripts often want to know whether
               modprobe really did something: this option makes modprobe fail
               in the case that it actually didn't do anything.

           --force-vermagic
               Every module contains a small string containing important
               information, such as the kernel and compiler versions. If a
               module fails to load and the kernel complains that the
               "version magic" doesn't match, you can use this option to
               remove it. Naturally, this check is there for your protection,
               so using this option is dangerous unless you know what you're
               doing.

               This applies to any modules inserted: both the module (or
               alias) on the command line and any modules on which it
               depends.

           --force-modversion
               When modules are compiled with CONFIG_MODVERSIONS set, a
               section detailing the versions of every interfaced used by (or
               supplied by) the module is created. If a module fails to load
               and the kernel complains that the module disagrees about a
               version of some interface, you can use --force-modversion to
               remove the version information altogether. Naturally, this
               check is there for your protection, so using this option is
               dangerous unless you know what you're doing.

               This applies to any modules inserted: both the module (or
               alias) on the command line and any modules on which it
               depends.

           -f, --force
               Try to strip any versioning information from the module which
               might otherwise stop it from loading: this is the same as
               using both --force-vermagic and --force-modversion. Naturally,
               these checks are there for your protection, so using this
               option is dangerous unless you know what you are doing.

               This applies to any modules inserted: both the module (or
               alias) on the command line and any modules on which it
               depends.

           -i, --ignore-install, --ignore-remove
               This option causes modprobe to ignore install and remove
               commands in the configuration file (if any) for the module
               specified on the command line (any dependent modules are still
               subject to commands set for them in the configuration file).
               Both install and remove commands will currently be ignored
               when this option is used regardless of whether the request was
               more specifically made with only one or other (and not both)
               of --ignore-install or --ignore-remove. See modprobe.d(5).

           -n, --dry-run
               This option does everything but actually insert or delete the
               modules (or run the install or remove commands). Combined with
               -v, it is useful for debugging problems.

               For compatibility reasons --show is also accepted for this
               option but will be removed after kmod 36.

           -q, --quiet
               With this flag, modprobe won't print an error message if you
               try to remove or insert a module it can't find (and isn't an
               alias or install/remove command). However, it will still
               return with a non-zero exit status. The kernel uses this to
               opportunistically probe for modules which might exist using
               request_module.

           -R, --show-alias
               Print all module names matching an alias. This can be useful
               for debugging module alias problems.

               For compatibility reasons --resolve-alias is also accepted for
               this option but will be removed after kmod 36.

           -r, --remove
               This option causes modprobe to remove rather than insert a
               module. If the modules it depends on are also unused, modprobe
               will try to remove them too. Unlike insertion, more than one
               module can be specified on the command line (it does not make
               sense to specify module parameters when removing modules).

               There is usually no reason to remove modules, but some buggy
               modules require it. Your distribution kernel may not have been
               built to support removal of modules at all.

           --remove-holders
               This option causes modprobe to remove the mentioned module(s),
               alongside other modules that depend on it/them - aka the
               reverse dependency list. This options implies --remove.

               For compatibility reasons --remove-dependencies is also
               accepted for this option but will be removed after kmod 36.

           -w TIMEOUT_MSEC, --wait TIMEOUT_MSEC
               This option causes modprobe -r to continue trying to remove a
               module if it fails due to the module being busy, i.e. its
               refcount is not 0 at the time the call is made. Modprobe tries
               to remove the module with an incremental sleep time between
               each tentative up until the maximum wait time in milliseconds
               passed in this option.

           -S version, --set-version version
               Set the kernel version, rather than using uname(2) to decide
               on the kernel version (which dictates where to find the
               modules).

           --show-depends
               List the dependencies of a module (or alias), including the
               module itself. This produces a (possibly empty) set of module
               filenames, one per line, each starting with "insmod" and is
               typically used by distributions to determine which modules to
               include when generating initrd/initramfs images. Install
               commands which apply are shown prefixed by "install". It does
               not run any of the install commands. Note that modinfo(8) can
               be used to extract dependencies of a module from the module
               itself, but knows nothing of aliases or install commands.

           -s, --syslog
               This option causes any error messages to go through the syslog
               mechanism (as LOG_DAEMON with level LOG_NOTICE) rather than to
               standard error. This is also automatically enabled when stderr
               is unavailable.

               This option is passed through install or remove commands to
               other modprobe commands in the MODPROBE_OPTIONS environment
               variable.

           -V, --version
               Show version of program and exit.

           -v, --verbose
               Print messages about what the program is doing. Usually
               modprobe only prints messages if something goes wrong.

               This option is passed through install or remove commands to
               other modprobe commands in the MODPROBE_OPTIONS environment
               variable.

## [](#ENVIRONMENT)ENVIRONMENT

           The MODPROBE_OPTIONS environment variable can also be used to pass
           command line arguments to modprobe. The format is intentionally
           left undocumented, since the use by third-party tools and scripts
           is discouraged.

           The environment variable originates with the implementation of the
           install rules.

## [](#SEE_ALSO)SEE ALSO

           modprobe.d(5), insmod(8), rmmod(8), lsmod(8), modinfo(8),
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

    kmod                            2026-08-03                    MODPROBE(8)

------------------------------------------------------------------------

Pages that refer to this page: [delete_module(2)](../man2/delete_module.2.html),  [init_module(2)](../man2/init_module.2.html),  [sk98lin(4)](../man4/sk98lin.4.html),  [modprobe.d(5)](../man5/modprobe.d.5.html),  [modules.dep(5)](../man5/modules.dep.5.html),  [modules-load.d(5)](../man5/modules-load.d.5.html),  [sysctl.d(5)](../man5/sysctl.d.5.html),  [lvmthin(7)](../man7/lvmthin.7.html),  [depmod(8)](../man8/depmod.8.html),  [insmod(8)](../man8/insmod.8.html),  [kmod(8)](../man8/kmod.8.html),  [lsmod(8)](../man8/lsmod.8.html),  [modinfo(8)](../man8/modinfo.8.html),  [rmmod(8)](../man8/rmmod.8.html)

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
