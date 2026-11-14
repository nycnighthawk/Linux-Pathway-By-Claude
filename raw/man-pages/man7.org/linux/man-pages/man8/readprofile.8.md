---
{"title": "readprofile(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/readprofile.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# readprofile(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [VERSION](#VERSION) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [BUGS](#BUGS) \| [EXAMPLE](#EXAMPLE) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    READPROFILE(8)            System Administration            READPROFILE(8)

## [](#NAME)NAME

           readprofile - read kernel profiling information

## [](#SYNOPSIS)SYNOPSIS

           readprofile [options]

## [](#VERSION)VERSION

           This manpage documents version 2.0 of the program.

## [](#DESCRIPTION)DESCRIPTION

           The readprofile command uses the /proc/profile information to
           print ascii data on standard output. The output is organized in
           three columns: the first is the number of clock ticks, the second
           is the name of the C function in the kernel where those many ticks
           occurred, and the third is the normalized `load' of the procedure,
           calculated as a ratio between the number of ticks and the length
           of the procedure. The output is filled with blanks to ease
           readability.

           This utility is a diagnostic tool and is not designed or intended
           for use in security-sensitive contexts (e.g., setuid, setgid,
           sudo, or similar privilege-elevation scenarios). It is installed
           without any special permissions.

## [](#OPTIONS)OPTIONS

           -a, --all
               Print all symbols in the mapfile. By default the procedures
               with reported ticks are not printed.

           -b, --histbin
               Print individual histogram-bin counts.

           -i, --info
               Info. This makes readprofile only print the profiling step
               used by the kernel. The profiling step is the resolution of
               the profiling buffer, and is chosen during kernel
               configuration (through make config), or in the kernel’s
               command line. If the -t (terse) switch is used together with
               -i only the decimal number is printed.

           -m, --mapfile mapfile
               Specify a mapfile, which by default is /boot/System.map. You
               should specify the map file on cmdline if your current kernel
               isn’t the last one you compiled, or if you keep System.map
               elsewhere. If the name of the map file ends with .gz it is
               decompressed on the fly.

           -n, --no-auto
               Disable automatic byte order detection.

           -M, --multiplier multiplier
               On some architectures it is possible to alter the frequency at
               which the kernel delivers profiling interrupts to each CPU.
               This option allows you to set the frequency, as a multiplier
               of the system clock frequency, HZ. Linux 2.6.16 dropped
               multiplier support for most systems. This option also resets
               the profiling buffer, and requires superuser privileges.

           -p, --profile pro-file
               Specify a different profiling buffer, which by default is
               /proc/profile. Using a different pro-file is useful if you
               want to `freeze' the kernel profiling at some time and read it
               later. The /proc/profile file can be copied using cat(1) or
               cp(1). There is no more support for compressed profile
               buffers, like in readprofile-1.1, because the program needs to
               know the size of the buffer in advance.

           -r, --reset
               Reset the profiling buffer. This can only be invoked by root,
               because /proc/profile is readable by everybody but writable
               only by the superuser.

           -s, --counters
               Print individual counters within functions.

           -v, --verbose
               Verbose. The output is organized in four columns and filled
               with blanks. The first column is the RAM address of a kernel
               function, the second is the name of the function, the third is
               the number of clock ticks and the last is the normalized load.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#FILES)FILES

           /proc/profile
               A binary snapshot of the profiling buffer.

           /usr/src/linux/System.map
               The symbol table for the kernel.

           /usr/src/linux/*
               The program being profiled :-)

## [](#BUGS)BUGS

           readprofile only works with a 1.3.x or newer kernel, because
           /proc/profile changed in the step from 1.2 to 1.3.

           This program only works with ELF kernels. The change for a.out
           kernels is trivial, and left as an exercise to the a.out user.

           To enable profiling, the kernel must be rebooted, because no
           profiling module is available, and it wouldn’t be easy to build.
           To enable profiling, you can specify profile=2 (or another number)
           on the kernel commandline. The number you specify is the
           two-exponent used as profiling step.

           Profiling is disabled when interrupts are inhibited. This means
           that many profiling ticks happen when interrupts are re-enabled.
           Watch out for misleading information.

## [](#EXAMPLE)EXAMPLE

           Browse the profiling buffer ordering by clock ticks:

                  readprofile | sort -nr | less

           Print the 20 most loaded procedures:

                  readprofile | sort -nr +2 | head -20

           Print only filesystem profile:

                  readprofile | grep _ext2

           Look at all the kernel information, with ram addresses:

                  readprofile -av | less

           Browse a 'frozen' profile buffer for a non current kernel:

                  readprofile -p ~/profile.freeze -m /zImage.map.gz

           Request profiling at 2kHz per CPU, and reset the profiling buffer:

                  readprofile -M 20

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The readprofile command is part of the util-linux package which
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                 READPROFILE(8)

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
