---
{"title": "Compile kernel module", "url": "https://wiki.archlinux.org/title/Compile_kernel_module", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Compile kernel module

Related articles

-   [Kernel](../en/Kernel.html "Kernel")
-   [Kernel modules](../en/Kernel_modules.html "Kernel modules")
-   [Dynamic Kernel Module Support](../en/Dynamic_Kernel_Module_Support.html "Dynamic Kernel Module Support")

Sometimes you may wish to compile Linux\'s [Kernel module](../en/Kernel_module.html "Kernel module") without recompiling the whole kernel.

**Note** You can only replace existing module if it is compiled as module (M) and not builtin (y) into kernel.

## Build environment {#Build_environment}

Firstly you will need to install build dependencies such as a compiler ([base-devel](https://archlinux.org/packages/?name=base-devel)) and [linux-headers](https://archlinux.org/packages/?name=linux-headers).

Next you will need to **get the source code** for the kernel version the module is intended to run on. You may try using newer kernel sources but most likely the compiled module will not load.

In case the intended kernel version is the installed kernel, find its version with

    $ uname -r

There are two main options to acquire the required source. Each option has slightly different usage methods and directory structure.

### Traditional compilation {#Traditional_compilation}

See [Kernel/Traditional compilation#Download the kernel source](../en/Kernel/Traditional_compilation.html#Download_the_kernel_source "Kernel/Traditional compilation"). If you fetch latest source using [Git](../en/Git.html "Git") you will need to checkout needed version using tag (eg. v4.1).

### Arch Build System {#Arch_Build_System}

For a general overview on Arch Build System read [ABS](../en/Arch_build_system.html "ABS"). See [Kernel/Arch build system](../en/Kernel/Arch_build_system.html "Kernel/Arch build system") for acquiring the kernel source, as well as the directory structure, and other details.

## Source configuration {#Source_configuration}

When you have the source code, enter its directory.

### Non-PKGBUILD sources {#Non-PKGBUILD_sources}

The output from `make help` is beneficial here. Start by cleaning with

    $ make mrproper

**Note** it will delete both `.config` and `.config.old`. You might want to save those files some where else before cleaning.

An appropriate `.config` file is now required. If none is nearby, perhaps from a saved `.config`, and the intended kernel version is the running kernel, you can use its configuration file:

    $ zcat /proc/config.gz > .config

Next ensure the `.config` file is adjusted for the kernel version. If you are using kernel sources for the exact current version then it should not ask anything. But for another version than the current kernel you might be asked about some options. In any case, for the [#Arch Build System](#Arch_Build_System) option, you might want to examine the `PKGBUILD::prepare()` function.

If the module you want to compile have some compilation options such as debug build, or it was not compiled before, you can also, possibly must, adjust the kernel configuration. You can do this with one of the many configuration targets mentioned by make help.

    $ make oldconfig

In order to compile and load our module cleanly, we must find the value of the EXTRAVERSION component of the current kernel version number so we can match the version number exactly in our kernel source. EXTRAVERSION is a variable set in the kernel top-level Makefile, but the Makefile in a vanilla kernel source will have EXTRAVERSION empty; it is set only as part of the Arch kernel build process. If relevant, the value of the current kernel\'s EXTRAVERSION can be found by looking at the output of the `uname -r` command. In general, the kernel version is the concatenation of three components. Namely, the numeric version, the EXTRAVERSION, and the LOCALVERSION. The numeric version itself is a concatenation of three numbers. If built by a [PKGBUILD](../en/PKGBUILD.html "PKGBUILD") file, the LOCALVERSION will be taken from the `pkgrel` variable, prefixed by a hyphen. And the EXTRAVERSION will be the suffix of the `pkgver` variable, where the period character to the right of the third numeric number of the numeric version is replaced by a hyphen. For example, with the linux package `linux 5.5.8.arch1-1`, the LOCALVERSION is `-1`. The EXTRAVERSION is `-arch1`. The output of `uname -r` will be `5.5.8-arch1-1` in that example.

Once the EXTRAVERSION value is known, we prepare the source for module compilation:

    $ make EXTRAVERSION=<YOUR EXTRAVERSION HERE> modules_prepare

Example:

    $ make EXTRAVERSION=-arch1 modules_prepare

Alternatively, if you are happy to load modules with *modprobe* using the `--force-vermagic` option to ignore mismatches in the kernel version number, you can simply run:

    $ make modules_prepare

**Note** Using the EXTRAVERSION that is recorded in the top level Makefile to avoid manually specifying the EXTRAVERSION on the command line could cause a version mismatch. The kernel build process would recognize that, causing it to append a `+` character to the LOCALVERSION configuration setting. For example: `5.5.8-arch1-1+`.

### Arch Build System {#Arch_Build_System_2}

In the [#Arch Build System](#Arch_Build_System) case, the source is unpacked by `makepkg --nobuild` to `src/linux-$version/` down from where the PKGBUILD is, together with a config file matching the kernel version (i.e. the same as `/proc/config.gz` when running the same version).

You now need to provide the correct `Module.symvers` file, either by building the whole kernel (missing the point of this whole page), or by copying it from the binary package built from the checked out source. In case that is the kernel package currently installed, you can just symlink it:

    $ ln -s /usr/lib/modules/$(uname -r)/build/Module.symvers .

In order to compile and load our module cleanly, the version numbers in your source tree must exactly match the version numbers of the kernel which loads it. When you got the source from [#Arch Build System](#Arch_Build_System), the versions will be configured by `makepkg` based on the [PKGBUILD](../en/PKGBUILD.html "PKGBUILD"), so modules built from that source tree will be compatible with the Kernel packages from archlinux repos.

## Module compilation {#Module_compilation}

Finally, compile wanted module by specifying its directory name. You can find the module location, thus also its directory name, with *modinfo* or *find*.

    $ make M=fs/btrfs

As a last resort, if nothing else has worked, you can build all the modules from the kernel configuration with:

    $ make modules

### out-of-tree module compilation {#out-of-tree_module_compilation}

When your module source is not (yet) merged into the kernel source tree:

Get the official source code of the current running linux kernel as described in [Kernel/Arch build system](../en/Kernel/Arch_build_system.html "Kernel/Arch build system"):

    $ cd && mkdir build
    $ pkgctl repo clone linux

then point to the checked out source when compiling the module:

    $ cd build/mymod
    $ make -C ~/build/linux/src/archlinux-linux M=$PWD modules

## Module installation {#Module_installation}

After successful compilation you can find your compiled module as a `*.ko` file in its source directory. Now you just need to copy it over for your current kernel. Optionally compress first:

    $ zstd fs/btrfs/btrfs.ko

If you are replacing some **existing module**, place your binary in the updates folder:

    # mkdir -p /usr/lib/modules/$(uname -r)/updates/fs/btrfs/
    # cp fs/btrfs/btrfs.ko.zst /usr/lib/modules/$(uname -r)/updates/fs/btrfs/

Alternatively, overwrite the original file (and remember that reinstalling [linux](https://archlinux.org/packages/?name=linux) will replace it with default module)

    # cp -f fs/btrfs/btrfs.ko.zst /usr/lib/modules/$(uname -r)/kernel/fs/btrfs/

\
However if you are adding a **new module** you can just copy it to extramodules (note, this is just example as btrfs will not get loaded from here)

    # cp fs/btrfs/btrfs.ko.zst /usr/lib/modules/$(uname -r)/extramodules/

\
In any case, to load it you need to rebuild the module dependency tree with \"depmod\" to use installed modules. Confirm your module is ready to load by looking at the `filename` printed by invoking `modinfo`.

If you are compiling a module for early boot (e.g. updated module) which is copied to [Initramfs](../en/Arch_boot_process.html#initramfs "Initramfs") then you must remember to regenerate it (otherwise your compiled module will not be loaded):

    # mkinitcpio -p linux

## possible errors {#possible_errors}

If EXTRAVERSION is not set correctly the following errors may occur

    # insmod mymod.ko
    insmod: ERROR: could not insert module mymod.ko: Invalid module format
    # modprobe mymod
    modprobe: ERROR: could not insert 'mymod': Exec format error

Inspecting [dmesg](../en/Core_utilities.html#Essentials "Dmesg") shows the differing version strings:

    i915: version magic '7.2.4-arch1-2-mylocalpkgrel SMP preempt mod_unload ' should be '7.2.4-arch1-2 SMP preempt mod_unload

Adding force-vermagic makes it ignore the version mismatch

    modprobe mymod --force-vermagic

But make sure the module has indeed been compiled for that kernel, and optimally adjust the version string to match it (see above).

## See also {#See_also}

-   [Linux Kernel Newbies](https://kernelnewbies.org/)
-   [The Linux Kernel Module Programming Guide](https://sysprog21.github.io/lkmpg/)
