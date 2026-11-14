---
{"title": "stap-onboot(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/stap-onboot.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stap-onboot(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ARGUMENTS](#ARGUMENTS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAP-ONBOOT(8)           System Manager's Manual           STAP-ONBOOT(8)

## [](#NAME)NAME

           stap-onboot - Embed SystemTap scripts into initramfs for early-
           boot execution

## [](#SYNOPSIS)SYNOPSIS

           stap-onboot [OPTIONS] [SCRIPT...]

## [](#DESCRIPTION)DESCRIPTION

           The stap-onboot command compiles SystemTap scripts and uses dracut
           to embed them into an initramfs, allowing the scripts to run
           during early boot before the root filesystem is mounted. This is
           useful for debugging early-boot issues or applying CVE band-aid
           scripts that need to run as early as possible.

           Scripts are read from ${prefix}/etc/systemtap/script.d/.  Compiled
           modules are cached in ${prefix}/var/cache/systemtap/KERNEL/.

## [](#OPTIONS)OPTIONS

           -b     Backup the existing initramfs before overwriting it. The
                  backup is saved with a .bak extension.

           -c configfile
                  Specify an alternate configuration file instead of the
                  default ${prefix}/etc/systemtap/config.

           -o path.img
                  Specify the output initramfs file path. By default, the
                  initramfs for the current kernel is updated at
                  /boot/initramfs-KERNEL.img.

           -r kernelrelease
                  Specify the kernel release to build the initramfs for.
                  Defaults to the currently running kernel (uname -r).

## [](#ARGUMENTS)ARGUMENTS

           SCRIPT One or more script names (without the .stp extension) to
                  compile and embed in the initramfs. Scripts must exist in
                  ${prefix}/etc/systemtap/script.d/.  If no scripts are
                  specified, a clean initramfs without SystemTap scripts is
                  created.

## [](#EXAMPLES)EXAMPLES

           Compile and embed myScript.stp into the initramfs, backing up the
           original: # stap-onboot -b myScript

           Create an initramfs for a different kernel: # stap-onboot -r
           6.1.0-1.fc37.x86_64 earlyDebug

           Create a custom initramfs in a specific location: # stap-onboot -o
           /tmp/test-initramfs.img bandaid

           Remove all SystemTap scripts from the initramfs: # stap-onboot

## [](#FILES)FILES

           ${prefix}/etc/systemtap/script.d/SCRIPT.stp
                  Source SystemTap scripts to be embedded.

           ${prefix}/etc/systemtap/config
                  Configuration file for script options. Each script can have
                  options defined as SCRIPTNAME_OPT=....

           ${prefix}/var/cache/systemtap/KERNEL/
                  Directory where compiled .ko modules are cached.

           /boot/initramfs-KERNEL.img
                  Default output location for the generated initramfs.

           /usr/lib/dracut/modules.d/99stap
                  Dracut module directory for SystemTap integration.

## [](#SEE_ALSO)SEE ALSO

           stap(1), staprun(8), dracut(8), systemd.service(5)

## [](#COLOPHON)COLOPHON

           This page is part of the systemtap (a tracing and live-system
           analysis tool) project.  Information about the project can be
           found at ⟨https://sourceware.org/systemtap/⟩.  If you have a bug
           report for this manual page, send it to systemtap@sourceware.org.
           This page was obtained from the project's upstream Git repository
           ⟨git://sourceware.org/git/systemtap.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                               STAP-ONBOOT(8)

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
