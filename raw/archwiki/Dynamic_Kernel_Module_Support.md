---
{"title": "Dynamic Kernel Module Support", "url": "https://wiki.archlinux.org/title/Dynamic_Kernel_Module_Support", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Dynamic Kernel Module Support

From [Wikipedia](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support "wikipedia:Dynamic Kernel Module Support"):

Dynamic Kernel Module Support (DKMS) is a program/framework that enables generating Linux kernel modules whose sources generally reside outside the kernel source tree. The concept is to have DKMS modules automatically rebuilt when a new kernel is installed.

This means that a user does not have to wait for a company, project, or package maintainer to release a new version of the module. Since the introduction of [pacman hooks](../en/Pacman_hooks.html "Pacman hooks"), the rebuild of the modules is handled automatically when a kernel is upgraded.

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [dkms](https://archlinux.org/packages/?name=dkms) package **and** the [headers](https://unix.stackexchange.com/a/47334) for the target kernel(s)---for example, for the default [linux](https://archlinux.org/packages/?name=linux) kernel this would be [linux-headers](https://archlinux.org/packages/?name=linux-headers); other kernels have their own respective headers packages.

A good number of modules that lie [outside](https://docs.kernel.org/kbuild/modules.html) the kernel source tree have a DKMS variant; a few are hosted in the [official repositories](https://archlinux.org/packages/?&q=dkms), most are found in the [AUR](https://aur.archlinux.org/packages/?SeB=n&K=dkms).

**Note** The modules built by DKMS will fail to load if the kernel [enforces](../en/Security.html#Restricting_module_loading "Security") loading only signed modules, e.g. when using [kernel lockdown](../en/Security.html#Kernel_lockdown_mode "Security").

## Upgrades {#Upgrades}

Though the rebuild of the DKMS modules is usually seamless during a kernel upgrade, it may still happen that the rebuild fails. You should pay extra attention to the [pacman](../en/Pacman.html "Pacman") output. This applies in particular if the system relies on the DKMS module to boot successfully and/or if you use DKMS with a custom kernel not in the [official repositories](../en/Official_repositories.html "Official repositories").

To deal with changes in the kernel, fix bugs, or add necessary features consider upgrading the DKMS package before rebooting.

## Usage {#Usage}

Usage for invoking DKMS manually.

Tab-completion is available by doing:

    # source /usr/share/bash-completion/completions/dkms

### List modules {#List_modules}

To list the current status of modules, versions and kernels within the tree:

    # dkms status

### Rebuild modules {#Rebuild_modules}

Rebuild all modules for the currently running kernel:

    # dkms autoinstall

or for a specific kernel:

    # dkms autoinstall -k 3.16.4-1-ARCH

To build a *specific* module for the currently running kernel:

    # dkms install -m nvidia -v 334.21

or simply:

    # dkms install nvidia/334.21

To build a module for *all* kernels:

    # dkms install nvidia/334.21 --all

### Remove modules {#Remove_modules}

To remove a module (old ones are not automatically removed):

    # dkms remove -m nvidia -v 331.49 --all

or simply:

    # dkms remove nvidia/331.49 --all

If the package [dkms](https://archlinux.org/packages/?name=dkms) is removed the information regarding previous module build files is lost. If this is the case, go through `/usr/lib/modules/`*`kernel_release`* and `/var/lib/dkms/`*`package_name`* and delete all files and directories no longer in use.

## DKMS package creation {#DKMS_package_creation}

See [DKMS package guidelines](../en/DKMS_package_guidelines.html "DKMS package guidelines").

## See also {#See_also}

-   [Linux Journal: Exploring Dynamic Kernel Module Support](https://www.linuxjournal.com/article/6896)
