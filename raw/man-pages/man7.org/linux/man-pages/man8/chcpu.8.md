---
{"title": "chcpu(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/chcpu.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chcpu(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHCPU(8)                  System Administration                  CHCPU(8)

## [](#NAME)NAME

           chcpu - configure CPUs

## [](#SYNOPSIS)SYNOPSIS

           chcpu -c|-d|-e|-g cpu-list

           chcpu -p mode

           chcpu -r|-h|-V

## [](#DESCRIPTION)DESCRIPTION

           chcpu can modify the state of CPUs. It can enable or disable CPUs,
           scan for new CPUs, change the CPU dispatching mode of the
           underlying hypervisor, and request CPUs from the hypervisor
           (configure) or return CPUs to the hypervisor (deconfigure).

           Some options have a cpu-list argument. Use this argument to
           specify a comma-separated list of CPUs. The list can contain
           individual CPU addresses or ranges of addresses. For example,
           0,5,7,9-11 makes the command applicable to the CPUs with the
           addresses 0, 5, 7, 9, 10, and 11.

## [](#OPTIONS)OPTIONS

           -c, --configure cpu-list
               Configure the specified CPUs. Configuring a CPU means that the
               hypervisor takes a CPU from the CPU pool and assigns it to the
               virtual hardware on which your kernel runs.

           -d, --disable cpu-list
               Disable the specified CPUs. Disabling a CPU means that the
               kernel sets it offline.

           -e, --enable cpu-list
               Enable the specified CPUs. Enabling a CPU means that the
               kernel sets it online. A CPU must be configured, see -c,
               before it can be enabled.

           -g, --deconfigure cpu-list
               Deconfigure the specified CPUs. Deconfiguring a CPU means that
               the hypervisor removes the CPU from the virtual hardware on
               which the Linux instance runs and returns it to the CPU pool.
               A CPU must be offline, see -d, before it can be deconfigured.

               chcpu -g is not supported on IBM z/VM, CPUs are always in a
               configured state.

               if chcpu -g is supported, any disabled CPUs should be
               deconfigured to inform the hypervisor that these CPUs won’t be
               used, avoiding potential performance penalties.

           -p, --dispatch mode
               Set the CPU dispatching mode (polarization). This option has
               an effect only if your hardware architecture and hypervisor
               support CPU polarization. Available modes are:

               horizontal
                   The workload is spread across all available CPUs.

               vertical
                   The workload is concentrated on few CPUs.

           -r, --rescan
               Trigger a rescan of CPUs. After a rescan, the Linux kernel
               recognizes the new CPUs. Use this option on systems that do
               not automatically detect newly attached CPUs.

           -s, --sysroot directory
               Configure CPUs for a Linux instance other than the instance
               from which the chcpu command is issued. The specified
               directory is the system root of the Linux instance to be
               configured.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           chcpu has the following exit status values:

           0
               success

           1
               failure

           64
               partial success

## [](#ENVIRONMENT)ENVIRONMENT

           ULPATH_DEBUG=all
               Enable path debug output.

## [](#AUTHORS)AUTHORS

           Heiko Carstens <heiko.carstens@de.ibm.com>

## [](#COPYRIGHT)COPYRIGHT

           Copyright IBM Corp. 2011

## [](#SEE_ALSO)SEE ALSO

           lscpu(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The chcpu command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-1062-f... 2026-08-03                       CHCPU(8)

------------------------------------------------------------------------

Pages that refer to this page: [lscpu(1)](../man1/lscpu.1.html)

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
