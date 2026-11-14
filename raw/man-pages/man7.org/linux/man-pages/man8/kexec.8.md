---
{"title": "kexec(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/kexec.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# kexec(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [USAGE](#USAGE) \| [EXAMPLE](#EXAMPLE) \| [OPTIONS](#OPTIONS) \| [SUPPORTED KERNEL FILE TYPES AND OPTIONS](#SUPPORTED_KERNEL_FILE_TYPES_AND_OPTIONS) \| [ARCHITECTURE OPTIONS](#ARCHITECTURE_OPTIONS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    kexec(8)                       User Manuals                      kexec(8)

## [](#NAME)NAME

           kexec - directly boot into a new kernel

## [](#SYNOPSIS)SYNOPSIS

           /sbin/kexec [-v (--version)] [-f (--force)] [-x (--no-ifdown)] [-y
           (--no-sync)] [-l (--load)] [-p (--load-panic)] [-u (--unload)] [-e
           (--exec)] [-t (--type)] [--mem-min=addr] [--mem-max=addr]

## [](#DESCRIPTION)DESCRIPTION

           kexec is a system call that enables you to load and boot into
           another kernel from the currently running kernel.  kexec performs
           the function of the boot loader from within the kernel. The
           primary difference between a standard system boot and a kexec boot
           is that the hardware initialization normally performed by the BIOS
           or firmware (depending on architecture) is not performed during a
           kexec boot. This has the effect of reducing the time required for
           a reboot.

           Make sure you have selected CONFIG_KEXEC=y when configuring the
           kernel. The CONFIG_KEXEC option enables the kexec system call.

## [](#USAGE)USAGE

           Using kexec consists of

                  (1) loading the kernel to be rebooted to into memory, and
                  (2) actually rebooting to the pre-loaded kernel.

           To load a kernel, the syntax is as follows:

                  kexec -l kernel-image --append=command-line-options
                  --initrd=initrd-image

           where kernel-image is the kernel file that you intend to reboot
           to.

           Insert the command-line parameters that must be passed to the new
           kernel into command-line-options.  Passing the exact contents of
           /proc/cmdline into command-line-options is the safest way to
           ensure that correct values are passed to the rebooting kernel.

           The optional initrd-image is the initrd image to be used during
           boot.

           It's also possible to invoke kexec without an option parameter. In
           that case, kexec loads the specified kernel and then invokes
           shutdown(8).  If the shutdown scripts of your Linux distribution
           support kexec-based rebooting, they then call kexec -e just before
           actually rebooting the machine. That way, the machine does a clean
           shutdown including all shutdown scripts.

## [](#EXAMPLE)EXAMPLE

           For example, if the kernel image you want to reboot to is
           /boot/vmlinux, the contents of /proc/cmdline is root=/dev/hda1,
           and the path to the initrd is /boot/initrd, then you would use the
           following command to load the kernel:

                  kexec -l /boot/vmlinux
                  --append=root=/dev/hda1 --initrd=/boot/initrd

           After this kernel is loaded, assuming the user-space supports
           kexec-based rebooting, it can be booted to, with a clean shutdown,
           using the command:

                  reboot

           Alternatively, it can also be booted to, without calling
           shutdown(8), with the command:

                  kexec -e

## [](#OPTIONS)OPTIONS

           -d (--debug)
                  Enable debugging messages.

           -S (--status)
                  Return 1 if the type (by default crash) is loaded, 0 if
                  not. Can be used in conjuction with -l or -p to toggle the
                  type. Note this option supersedes other options and it will
                  not load or unload the kernel.

           -e (--exec)
                  Run the currently loaded kernel. Note that it will reboot
                  into the loaded kernel without calling shutdown(8).

           -f (--force)
                  Force an immediate kexec call, do not call shutdown(8)
                  (contrary to the default action without any option
                  parameter). This option performs the same actions like
                  executing -l and -e in one call.

           -h (--help)
                  Open a help file for kexec.

           --hotplug
                  Setup kexec segments such that kernel can safely update
                  them on CPU/Memory hot add/remove events. If this option is
                  enabled, kernel does in-kernel update of kexec segments on
                  CPU/Memory hot add/remove events, thus avoiding the need to
                  reload kdump kernel.

           -i (--no-checks)
                  Fast reboot, no memory integrity checks.

           -l (--load) kernel
                  Load the specified kernel into the current kernel.

           -p (--load-panic)
                  Load the new kernel for use on panic.

           -t (--type=type)
                  Specify that the new kernel is of this type.

           -s (--kexec-file-syscall)
                  Specify that the new KEXEC_FILE_LOAD syscall should be used
                  exclusively.  Ignored on XEN.

           -c (--kexec-syscall)
                  Specify that the old KEXEC_LOAD syscall should be used
                  exclusively.

           -a (--kexec-syscall-auto)
                  Try the new KEXEC_FILE_LOAD syscall first and when it is
                  not supported or the kernel does not understand the
                  supplied image fall back to the old KEXEC_LOAD interface.

                  There is no one single interface that always works, so this
                  is the default.

                  KEXEC_FILE_LOAD is required on systems that use locked-down
                  secure boot to verify the kernel signature.  KEXEC_LOAD may
                  be also disabled in the kernel configuration.

                  KEXEC_LOAD is required for some kernel image formats and on
                  architectures that do not implement KEXEC_FILE_LOAD.

           -u (--unload)
                  Unload the current kexec target kernel. If a capture kernel
                  is being unloaded then specify -p with -u.

           -v (--version)
                  Return the version number of the installed utility.

           -x (--no-ifdown)
                  Shut down the running kernel, but restore the interface on
                  reload.

           -y (--no-sync)
                  Shut down the running kernel, but skip syncing the
                  filesystems.

           --mem-min=addr
                  Specify the lowest memory address addr to load code into.

           --mem-max=addr
                  Specify the highest memory address addr to load code into.

           --entry=addr
                  Specify the jump back address. (0 means it's not jump back
                  or preserve context)

           --load-preserve-context
                  Load the new kernel and preserve context of current kernel
                  during kexec.

           --load-jump-back-helper
                  Load a helper image to jump back to original kernel.

           --reuseinitrd
                  Reuse initrd from first boot.

           --print-ckr-size
                  Print crash kernel region size, if available.

## [](#SUPPORTED_KERNEL_FILE_TYPES_AND_OPTIONS)SUPPORTED KERNEL FILE TYPES AND OPTIONS

           Beoboot-x86

                  --args-elf
                         Pass ELF boot notes.

                  --args-linux
                         Pass Linux kernel style options.

                  --real-mode
                         Use the kernel's real mode entry point.

           elf-x86

                  --append=string
                         Append string to the kernel command line.

                  --command-line=string
                         Set the kernel command line to string.

                  --reuse-cmdline
                         Use the command line from the running system. When a
                         panic kernel is loaded, it strips the crashkernel
                         parameter automatically. The BOOT_IMAGE parameter is
                         also stripped.

                  --initrd=file
                         Use file as the kernel's initial ramdisk.

                  --ramdisk=file
                         Use file as the kernel's initial ramdisk.

           bzImage-x86

                  --append=string
                         Append string to the kernel command line.

                  --command-line=string
                         Set the kernel command line to string.

                  --reuse-cmdline
                         Use the command line from the running system. When a
                         panic kernel is loaded, it strips the crashkernel
                         parameter automatically. The BOOT_IMAGE parameter is
                         also stripped.

                  --initrd=file
                         Use file as the kernel's initial ramdisk.

                  --ramdisk=file
                         Use file as the kernel's initial ramdisk.

                  --real-mode
                         Use real-mode entry point.

           multiboot-x86

                  --command-line=string
                         Set the kernel command line to string.

                  --reuse-cmdline
                         Use the command line from the running system. When a
                         panic kernel is loaded, it strips the crashkernel
                         parameter automatically. The BOOT_IMAGE parameter is
                         also stripped.

                  --module=mod arg1 arg2 ...
                         Load module mod with command-line arguments arg1
                         arg2 ...  This parameter can be specified multiple
                         times.

           multiboot2-x86

                  --command-line=string
                         Set the kernel command line to string.

                  --reuse-cmdline
                         Use the command line from the running system. When a
                         panic kernel is loaded, it strips the crashkernel
                         parameter automatically. The BOOT_IMAGE parameter is
                         also stripped.

                  --module=mod arg1 arg2 ...
                         Load module mod with command-line arguments arg1
                         arg2 ...  This parameter can be specified multiple
                         times.

           elf-ppc64

                  --reuse-cmdline
                         Use the kernel command line from the running system.

                  --command-line=string
                         Set the kernel command line to string.

                  --append=string
                         Set the kernel command line to string.

                  --ramdisk=file
                         Use file as the initial RAM disk.

                  --initrd=file
                         Use file as the initial RAM disk.

                  --devicetreeblob=file
                         Specify device tree blob file. Not applicable while
                         using --kexec-file-syscall.

                  --dtb=file
                         Specify device tree blob file. Not applicable while
                         using --kexec-file-syscall.

## [](#ARCHITECTURE_OPTIONS)ARCHITECTURE OPTIONS

           --console-serial
                  Enable the serial console.

           --console-vga
                  Enable the VGA console.

           --elf32-core-headers
                  Prepare core headers in ELF32 format.

           --elf64-core-headers
                  Prepare core headers in ELF64 format.

           --reset-vga
                  Attempt to reset a standard VGA device.

           --serial=port
                  Specify the serial port for debug output.

           --serial-baud=baud_rate
                  Specify the baud rate of the serial port.

           --dt-no-old-root
                  Do not reuse old kernel root=<device> param while creating
                  flatten device tree.

## [](#COLOPHON)COLOPHON

           This page is part of the kexec-tools (kexec-tools) project.
           Information about the project can be found at 
           ⟨https://projects.horms.net/projects/kexec/⟩.  If you have a bug
           report for this manual page, send it to kexec@lists.infradead.org.
           This page was obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/utils/kernel/kexec/kexec-tools.git⟩
           on 2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-20.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Linux                           April 2006                       kexec(8)

------------------------------------------------------------------------

Pages that refer to this page: [kexec_load(2)](../man2/kexec_load.2.html)

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
