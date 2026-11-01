---
{"title": "Managing, monitoring, and updating the kernel", "guide": "managing_monitoring_and_updating_the_kernel", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_monitoring_and_updating_the_kernel/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Managing, monitoring, and updating the kernel {#managing-monitoring-and-updating-the-kernel .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## A guide to managing the Linux kernel on Red Hat Enterprise Linux 10 {#a-guide-to-managing-the-linux-kernel-on-red-hat-enterprise-linux-10 .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140443122904688)

**Abstract**

As a system administrator, you can configure the Linux kernel to optimize the operating system. Changes to the Linux kernel can improve system performance, security, and stability, as well as your ability to audit the system and troubleshoot problems.

------------------------------------------------------------------------

## [Providing feedback on Red Hat documentation](#providing-feedback-on-red-hat-documentation) {#providing-feedback-on-red-hat-documentation .title}

We are committed to providing high-quality documentation and value your feedback. To help us improve, you can submit suggestions or report errors through the Red Hat Jira tracking system.

**Procedure**

1.  Log in to the [Jira](https://redhat.atlassian.net/jira/software/c/projects/RHELDOCS/issues/) website.

    If you do not have an account, select the option to create one.

2.  Click **Create** in the top navigation bar.

3.  Enter a descriptive title in the **Summary** field.

4.  Enter your suggestion for improvement in the **Description** field. Include links to the relevant parts of the documentation.

5.  Click **Create** at the bottom of the window.

## [Chapter 1. The Linux kernel](#the-linux-kernel) {#chapter-1.-the-linux-kernel .title}

The Red Hat kernel RPM package provides the Linux kernel. You must keep the kernel updated to ensure your system has the latest bug fixes, performance enhancements, patches, and hardware compatibility.

### [1.1. What the kernel is](#what-the-kernel-is) {#what-the-kernel-is .title}

The kernel is a core part of a Linux operating system that manages the system resources and provides an interface between hardware and software applications.

The Red Hat kernel is a custom-built kernel based on the upstream Linux mainline kernel that Red Hat engineers further develop and harden with a focus on stability and compatibility with the latest technologies and hardware.

The Red Hat kernels are packaged in the RPM format to upgrade and verify by the **DNF** package manager.

Warning

Red Hat only supports kernels that are compiled by Red Hat.

**Additional resources**

-   [Learn what the kernel version string means on RHEL 8, RHEL 9, and RHEL 10](#understanding-rhel-kernel-version-numbers "1.2. Understanding RHEL kernel version numbers")

### [1.2. Understanding RHEL kernel version numbers](#understanding-rhel-kernel-version-numbers) {#understanding-rhel-kernel-version-numbers .title}

The kernel version string reported by your system identifies the Red Hat Enterprise Linux (RHEL) kernel package. It does not describe all of the code in that kernel.

On RHEL, the output of the `uname -r`{.literal} command and the version of the `kernel`{.literal} RPM package use the same naming pattern, for example, `6.12.0-124.15.1.el10_1.x86_64`{.literal}. The string has the following parts:

-   An upstream Linux base version, such as `6.12`{.literal}.
-   A Red Hat patch count, such as `-124`{.literal}.
-   An optional additional patch level, such as `.15.1`{.literal}.
-   A RHEL release tag, such as `.el10_1`{.literal}.
-   The system architecture, such as `x86_64`{.literal}.

The RHEL release tag identifies the RHEL major or minor stream that built the package. It does not mean that every driver or subsystem in the kernel matches that upstream base version.

**Additional resources**

-   [What are the kernel-core, kernel-modules, and kernel-modules-extras packages?](https://access.redhat.com/articles/3739611)
-   [Red Hat Enterprise Linux release dates](https://access.redhat.com/articles/3078)

#### [1.2.1. What the version string does not mean](#what-the-rhel-kernel-version-string-does-not-mean) {#what-the-version-string-does-not-mean .title}

The upstream base number in the kernel version string does not list every change in the kernel source.

Red Hat does not treat the upstream base number as a promise that your kernel behaves like an unmodified upstream kernel at that tag.

Over the life of a RHEL major release, Red Hat backports fixes and enhancements from newer upstream Linux kernels into the same major kernel stream. As a result, the following situations can occur:

-   Individual drivers and core subsystems can include code from upstream kernels that are newer than the base version in the string.
-   The difference between the version string and upstream mainline grows as the RHEL major release matures.
-   You cannot use the version string alone to determine whether a specific upstream feature, API, or driver behavior is present.

This model applies across supported RHEL majors, including RHEL 8, RHEL 9, and RHEL 10.

#### [1.2.2. How RHEL kernels evolve](#how-rhel-kernels-evolve) {#how-rhel-kernels-evolve .title}

After Red Hat stabilizes a RHEL major release, the kernel continues to change through backports and Red Hat-specific work.

When Red Hat stabilizes a new RHEL major release, engineers select an upstream Linux base as the starting point for that major's kernel stream. That base appears in the version string for the life of the major release.

After that point, Red Hat continues to update the kernel by adding the following:

-   Backports of security fixes, bug fixes, and selected features from newer upstream kernels
-   Hardware and platform enablement for supported configurations
-   Red Hat-specific hardening, testing, and integration work

The base upstream version chosen for the `.0`{.literal} release does not limit which upstream changes can be backported later in the same RHEL major lifecycle.

#### [1.2.3. Examples on RHEL 8, RHEL 9, and RHEL 10](#examples-of-rhel-kernel-version-strings) {#examples-on-rhel-8-rhel-9-and-rhel-10 .title}

Review typical RHEL kernel version strings on RHEL 8, RHEL 9, and RHEL 10.

The following table shows typical version-string shapes with examples. They are not a full list of what is backported into each release.

+------------+-------------------------------------------+-----------------------------------+
| RHEL major | Example version string                    | Upstream base in the string       |
+:===========+:==========================================+:==================================+
| RHEL 8     | `4.18.0-553.28.1.el8_10.x86_64`{.literal} | Linux 4.18                        |
+------------+-------------------------------------------+-----------------------------------+
| RHEL 9     | `5.14.0-503.23.1.el9_5.x86_64`{.literal}  | Linux 5.14                        |
+------------+-------------------------------------------+-----------------------------------+
| RHEL 10    | `6.12.0-124.15.1.el10_1.x86_64`{.literal} | Linux 6.12                        |
+------------+-------------------------------------------+-----------------------------------+

: Table 1.1. Typical RHEL kernel version strings

Show more

For example, a RHEL 10.1 system can report a `6.12`{.literal} base in `uname -r`{.literal} while individual subsystems include changes from much newer upstream kernel versions. The same backport model applies on RHEL 8 and RHEL 9 over their respective lifecycles.

#### [1.2.4. How to determine kernel capabilities](#determining-rhel-kernel-capabilities) {#how-to-determine-kernel-capabilities .title}

Use the kernel version string together with release documentation and package details to determine whether a capability is supported on your system.

Use the version string to identify the installed RHEL kernel package and to distinguish RHEL kernel builds from non-Red Hat kernels. To determine whether a specific capability is supported on your system, also review the following items:

-   RHEL release notes and feature documentation for your major and minor release
-   Hardware and software certification and support statements for your platform
-   The installed `kernel`{.literal} package details, for example, by using the `dnf info kernel`{.literal} command

If you rely on vulnerability management or compliance tooling, remember that live kernel patches can fix some issues on the running kernel before a new kernel package is installed. Note that the version string from `uname -r`{.literal} alone might not reflect that state.

**Additional resources**

-   [CVE reporting for kernel live patches](#cve-reporting-for-kernel-live-patches "9.10. CVE reporting for kernel live patches")
-   [Identifying CVEs patched by kernel live patches](#identifying-cves-patched-by-kernel-live-patches "9.11. Identifying CVEs patched by kernel live patches")

### [1.3. RPM packages](#rpm-packages) {#rpm-packages .title}

An RPM package consists of an archive of files and metadata used to install and erase these files on Red Hat Enterprise Linux (RHEL).

Specifically, the RPM package contains the following parts:

-   GPG signature

    The GPG signature is used to verify the integrity of the package.

-   Header (package metadata)

    The RPM package manager uses this metadata to determine package dependencies, where to install files, and other information.

-   Payload

    The payload is a `cpio`{.literal} archive that contains files to install to the system.

There are two types of RPM packages. Both types share the file format and tooling, but have different contents and serve different purposes:

-   Source RPM (SRPM)

    An SRPM contains source code and a `spec`{.literal} file, which describes how to build the source code into a binary RPM. Optionally, the SRPM can contain patches to source code.

-   Binary RPM

    A binary RPM contains the binaries built from the sources and patches.

### [1.4. The Linux kernel RPM package overview](#the-linux-kernel-rpm-package-overview) {#the-linux-kernel-rpm-package-overview .title}

The `kernel`{.literal} RPM is a meta package that does not contain any files, but rather ensures that all required subpackages are properly installed.

The following list includes required packages:

`kernel-core`{.literal}
:   Provides the binary image of the Linux kernel (`vmlinuz`{.literal}).

`kernel-modules-core`{.literal}
:   Provides the basic kernel modules to ensure core functionality. This includes the modules essential for the proper functioning of the most commonly used hardware.

`kernel-modules`{.literal}
:   Provides the remaining kernel modules that are not present in `kernel-modules-core`{.literal}.

The `kernel-core`{.literal} and `kernel-modules-core`{.literal} subpackages together can be used in virtualized and cloud environments to provide a RHEL 10 kernel with a quick boot time and a small disk size footprint. `kernel-modules`{.literal} subpackage is usually unnecessary for such deployments.

Optional kernel packages are for example:

`kernel-modules-extra`{.literal}
:   Provides kernel modules for uncommonly used kernel modules. Loading of the modules in this package is disabled by default.

`kernel-debug`{.literal}
:   Provides a kernel with many debugging options enabled for kernel diagnosis, at the expense of reduced performance.

`kernel-tools`{.literal}
:   Provides tools for manipulating the Linux kernel and supporting documentation.

`kernel-devel`{.literal}
:   Provides the kernel headers and makefiles that are enough to build modules against the `kernel`{.literal .package} package.

`kernel-abi-stablelists`{.literal}
:   Provides information pertaining to the RHEL kernel ABI, including a list of kernel symbols required by external Linux kernel modules and a `dnf`{.literal .package} plugin to aid enforcement.

`kernel-headers`{.literal}
:   Includes the C header files that specify the interface between the Linux kernel and user-space libraries and programs. The header files define structures and constants required for building most standard programs.

`kernel-uki-virt`{.literal}

:   Contains the Unified Kernel Image (UKI) of the RHEL kernel.

    UKI combines the Linux kernel, `initramfs`{.literal} (initial RAM file system), and the kernel command line into a single signed binary which can be booted directly from the UEFI firmware.

    `kernel-uki-virt`{.literal} contains the required kernel modules to run in virtualized and cloud environments and can be used instead of the `kernel-core`{.literal} subpackage.

**Additional resources**

-   [What are the kernel-core, kernel-modules, and kernel-modules-extras packages?](https://access.redhat.com/articles/3739611)

### [1.5. Displaying contents of the kernel package](#displaying-contents-of-the-kernel-package) {#displaying-contents-of-the-kernel-package .title}

To check if a kernel package provides a specific file, such as a module, query the repository. You can display the file list without downloading or installing the package.

Use the `dnf`{.literal} utility to query the file list, for example, of the `kernel-core`{.literal}, `kernel-modules-core`{.literal}, or `kernel-modules`{.literal} package. Note that the `kernel`{.literal} package is a meta package that does not contain any files.

**Procedure**

1.  List the available versions of a package:

    ``` {.language-plaintext tabindex="-1"}
    $ dnf repoquery <package_name>
    ```

2.  Display the list of files in a package:

    ``` {.language-plaintext tabindex="-1"}
    $ dnf repoquery -l <package_name>
    ```

**Additional resources**

-   [Packaging and distributing software](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/packaging_and_distributing_software)

### [1.6. Installing specific kernel versions](#installing-specific-kernel-versions) {#installing-specific-kernel-versions .title}

You can install new kernels by using the DNF package manager.

**Procedure**

-   To install a specific kernel version, enter the following command:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kernel-<version>
    ```

**Additional resources**

-   [Red Hat Enterprise Linux Release Dates](https://access.redhat.com/articles/3078)

### [1.7. Updating the kernel](#updating-the-kernel) {#updating-the-kernel .title}

You can update the kernel by using the DNF package manager.

**Procedure**

1.  To update the kernel, enter the following command:

    ``` {.language-plaintext tabindex="-1"}
    # dnf upgrade kernel
    ```

    This command updates the kernel along with all dependencies to the latest available version.

2.  Reboot your system for the changes to take effect.

    See the `dnf(8)`{.literal} man page on your system for more information.

**Additional resources**

-   [Managing software with the DNF tool](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/index)

### [1.8. Setting a kernel as default](#setting-a-kernel-as-default) {#setting-a-kernel-as-default .title}

To set a specific kernel as the default, use the `grubby`{.literal} command-line tool and GRUB configuration.

**Procedure**

-   Setting the kernel as default by using the `grubby`{.literal} tool.

    -   Enter the following command to set the kernel as default using the `grubby`{.literal} tool:

        ``` {.language-plaintext tabindex="-1"}
        # grubby --set-default $kernel_path
        ```

-   Setting the kernel as default by using the `version`{.literal} argument.

    -   List the boot entries using the kernel keyword and then set an intended kernel as default:

        ``` {.language-plaintext tabindex="-1"}
        # select k in /boot/vmlinuz-*; do grubby --set-default=$k; break; done
        ```

        Note

        To list the boot entries using the `title`{.literal} argument, enter `# `{.literal}**`grubby --info=ALL | grep title`{.literal}**.

-   Setting the default kernel for only the next boot.

    -   Enter the following command to set the default kernel for only the next reboot using the `grub2-reboot`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        # grub2-reboot <index|title|id>
        ```

        Warning

        Set the default kernel for only the next boot with care. Installing new kernel RPMs, self-built kernels, and manually adding the entries to the `/boot/loader/entries/`{.literal} directory might change the index values.

## [Chapter 2. The 64k page size kernel](#what-is-kernel-64k) {#chapter-2.-the-64k-page-size-kernel .title}

`kernel-64k`{.literal} is an additional, optional 64-bit ARM architecture kernel package that supports 64k pages. This additional kernel exists alongside the RHEL 10 for ARM kernel, which supports 4k pages.

Optimal system performance directly relates to different memory configuration requirements. These requirements are addressed by the two variants of kernel, each suitable for different workloads. RHEL 10 on 64-bit ARM hardware thus offers two MMU page sizes:

-   4k pages kernel for efficient memory usage in smaller environments,
-   `kernel-64k`{.literal} for workloads with large, contiguous memory working sets.

The 4k pages kernel and `kernel-64k`{.literal} do not differ in the user experience as the user space is the same. You can choose the variant that addresses your situation the best.

4k pages kernel

:   Use 4k pages for more efficient memory usage in smaller environments, such as those in Edge and lower-cost, small cloud instances. In these environments, increasing the physical system memory amounts is not practical due to space, power, and cost constraints. Furthermore, not all 64-bit ARM architecture processors support a 64k page size.

    The 4k pages kernel supports graphical installation by using Anaconda, system or cloud image-based installations, as well as advanced installations by using Kickstart.

`kernel-64k`{.literal}

:   The 64k page size kernel is a useful option for large datasets on ARM platforms. `kernel-64k`{.literal} is suitable for memory-intensive workloads as it has significant gains in overall system performance, namely in large database, HPC, and high network performance.

    You must choose page size on 64-bit ARM architecture systems at the time of installation. You can install `kernel-64k`{.literal} only by Kickstart by adding the `kernel-64k`{.literal} package to the package list in the `Kickstart`{.literal} file.

### [2.1. Determining kernel page size by system architecture](#determining-kernel-page-size-by-system-architecture) {#determining-kernel-page-size-by-system-architecture .title}

You can determine the kernel page size for different system architectures.

**Procedure**

1.  Identify the system architecture:

    ``` {.language-plaintext tabindex="-1"}
    # uname -r
    ```

    ``` {.language-plaintext tabindex="-1"}
    6.12.0-55.9.1.el10_0.x86_64
    ```

    In this output, `x86_64`{.literal} indicates a 64-bit Intel or AMD architecture.

2.  Check the default page size:

    ``` {.language-plaintext tabindex="-1"}
    # getconf PAGE_SIZE
    ```

    ``` {.language-plaintext tabindex="-1"}
    4096
    ```

    On x86_64 systems, the output is 4096 B, which means the default page size is 4 KB.

    On ppc64le systems, the output is 65536 B, which means the default page size is 64 KB.

## [Chapter 3. Managing kernel modules](#managing-kernel-modules) {#chapter-3.-managing-kernel-modules .title}

Kernel modules extend kernel functionality. Obtain module information and perform administrative tasks such as loading, unloading, and configuring modules at boot time.

### [3.1. Introduction to kernel modules](#introduction-to-kernel-modules) {#introduction-to-kernel-modules .title}

Kernel modules extend the Red Hat Enterprise Linux kernel with optional functionality without rebooting the system. On Red Hat Enterprise Linux 10, they package extra kernel code in compressed *`<replaceable>`{.literal}*.ko.xz\` object files.

Loadable Kernel Modules (LKMs)
:   LKMs can be dynamically loaded into and unloaded from the running Linux kernel. You can add device drivers or filesystem support without requiring a system reboot or recompiling the entire kernel.

The most common functionality enabled by kernel modules are:

-   Device driver which adds support for new hardware
-   Support for a file system such as GFS2 or NFS
-   System calls

On modern systems, kernel modules are automatically loaded when needed. However, in some cases it is necessary to load or unload modules manually.

Similarly to the kernel, modules accept parameters that customize their behavior.

You can use the kernel tools to perform the following actions on modules:

-   Inspect modules that are currently running.
-   Inspect modules that are available to load into the kernel.
-   Inspect parameters that a module accepts.
-   Enable a mechanism to load and unload kernel modules into the running kernel.

### [3.2. Kernel module dependencies](#kernel-module-dependencies) {#kernel-module-dependencies .title}

Certain kernel modules sometimes depend on one or more other kernel modules. The `/lib/modules/<KERNEL_VERSION>/modules.dep`{.literal} file contains a complete list of kernel module dependencies for the corresponding kernel version.

`depmod`{.literal}

:   The dependency file is generated by the `depmod`{.literal} program, included in the `kmod`{.literal} package. Many utilities provided by `kmod`{.literal .package} consider module dependencies when performing operations. Therefore, **manual** dependency-tracking is rarely necessary.

    Warning

    The code of kernel modules executes in kernel-space in the unrestricted mode. Be cautious about the modules you are loading.

`weak-modules`{.literal}
:   In addition to `depmod`{.literal}, Red Hat Enterprise Linux provides the `weak-modules`{.literal} script, which is a part of the `kmod`{.literal} package. The `weak-modules`{.literal} script determines the modules that are kABI-compatible with installed kernels. While checking modules kernel compatibility, `weak-modules`{.literal} processes modules symbol dependencies from higher to lower release of kernel for which they were built. It processes each module independently of the kernel release.

**Additional resources**

-   [What is the purpose of weak-modules script shipped with Red Hat Enterprise Linux?](https://access.redhat.com/articles/9749)
-   [What is Kernel Application Binary Interface (kABI)? (Red Hat Knowledgebase)](https://access.redhat.com/solutions/444773)

### [3.3. Listing installed kernels](#listing-installed-kernels) {#listing-installed-kernels .title}

The `grubby --info=ALL`{.literal} command displays an indexed list of installed kernels on `BLS`{.literal} installs. With Boot Loader Specification (BLS), you can standardize the way of specifying boot entries. BLS is natively supported by `systemd-boot`{.literal}, and you can configure GRUB to use BLS.

**Procedure**

-   List the installed kernels:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --info=ALL | grep title
    ```

    The list of all installed kernels is displayed:

    ``` {.language-plaintext tabindex="-1"}
    title="Red Hat Enterprise Linux (6.12.0-55.9.1.el10_0.x86_64) 10.0"
    title="Red Hat Enterprise Linux (0-rescue-0d772916a9724907a5d1350bcd39ac92) 10.0"
    ```

    This is the list of installed kernels of grubby-8.40-17 from the GRUB menu.

### [3.4. Listing currently loaded kernel modules](#listing-currently-loaded-kernel-modules) {#listing-currently-loaded-kernel-modules .title}

Use the `lsmod`{.literal} command to list currently loaded kernel modules.

**Prerequisites**

-   The `kmod`{.literal} package is installed.

**Procedure**

-   List all currently loaded kernel modules:

    ``` {.language-plaintext tabindex="-1"}
    $ lsmod
    ```

    ``` {.language-plaintext tabindex="-1"}
    Module                  Size  Used by
    fuse                  126976  3
    uinput                 20480  1
    xt_CHECKSUM            16384  1
    ipt_MASQUERADE         16384  1
    xt_conntrack           16384  1
    ipt_REJECT             16384  1
    nft_counter            16384  16
    nf_nat_tftp            16384  0
    nf_conntrack_tftp      16384  1 nf_nat_tftp
    tun                    49152  1
    bridge                192512  0
    stp                    16384  1 bridge
    llc                    16384  2 bridge,stp
    nf_tables_set          32768  5
    nft_fib_inet           16384  1
    ...
    ```

    In this example:

    a.  The `Module`{.literal} column provides the **names** of currently loaded modules.
    b.  The `Size`{.literal} column displays the amount of **memory** per module in KB.
    c.  The `Used by`{.literal} column shows the number, and optionally the names of modules that are **dependent** on a particular module.

### [3.5. Displaying information about kernel modules](#displaying-information-about-kernel-modules) {#displaying-information-about-kernel-modules .title}

You can use the `modinfo`{.literal} command to display detailed information about the specified kernel module.

**Prerequisites**

-   The `kmod`{.literal} package is installed.

**Procedure**

-   Display information about any kernel module:

    ``` {.language-plaintext tabindex="-1"}
    $ modinfo <pass:quotes[KERNEL_MODULE_NAME]>
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    $ modinfo virtio_net
    ```

    ``` {.language-plaintext tabindex="-1"}
    filename:       /lib/modules/6.12.0-55.9.1.el10_0.x86_64/kernel/drivers/net/virtio_net.ko.xz
    license:        GPL
    description:    Virtio network driver
    rhelversion:    9.0
    srcversion:     8809CDDBE7202A1B00B9F1C
    alias:          virtio:d00000001v*
    depends:        net_failover
    retpoline:      Y
    intree:         Y
    name:           virtio_net
    vermagic:       6.12.0-55.9.1.el10_0.x86_64 SMP mod_unload modversions
    ...
    parm:           napi_weight:int
    parm:           csum:bool
    parm:           gso:bool
    parm:           napi_tx:bool
    ```

    You can query information about all available modules, regardless of whether they are loaded. The `parm`{.literal} entries show parameters the user is able to set for the module, and what type of value they expect.

    Note

    When entering the name of a kernel module, do not append the `.ko.xz`{.literal} extension to the end of the name. Kernel module names do not have extensions. However, their corresponding files do.

### [3.6. Loading kernel modules at system runtime](#loading-kernel-modules-at-system-runtime) {#loading-kernel-modules-at-system-runtime .title}

The optimal way to expand the functionality of the Linux kernel is by loading kernel modules. Use the `modprobe`{.literal} command to find and load a kernel module into the currently running kernel.

Important

The changes described in this procedure **will not persist** after rebooting the system. For information about how to load kernel modules to **persist** across system reboots, see [Loading kernel modules automatically at system boot time](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/managing-kernel-modules#loading-kernel-modules-automatically-at-system-boot-time).

**Prerequisites**

-   You have root permissions on the system.
-   The `kmod`{.literal} package is installed.
-   The corresponding kernel module is not loaded. To ensure this, list the [Listing currently loaded kernel modules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/managing-kernel-modules#listing-currently-loaded-kernel-modules).

**Procedure**

1.  Select a kernel module you want to load.

    The modules are located in the `/lib/modules/$(uname -r)/kernel/<SUBSYSTEM>/`{.literal} directory.

2.  Load the relevant kernel module:

    ``` {.language-plaintext tabindex="-1"}
    # modprobe <pass:quotes[MODULE_NAME]>
    ```

    Note

    When entering the name of a kernel module, do not append the `.ko.xz`{.literal} extension to the end of the name. Kernel module names do not have extensions; their corresponding files do.

**Verification**

-   Optionally, verify the relevant module is loaded:

    ``` {.language-plaintext tabindex="-1"}
    $ lsmod | grep <pass:quotes[MODULE_NAME]>
    ```

    If the module is loaded correctly, you can display it:

    ``` {.language-plaintext tabindex="-1"}
    $ lsmod | grep serio_raw
    ```

    ``` {.language-plaintext tabindex="-1"}
    serio_raw              16384  0
    ```

    See the `modprobe(8)`{.literal} man page on your system for more information.

### [3.7. Unloading kernel modules at system runtime](#unloading-kernel-modules-at-system-runtime) {#unloading-kernel-modules-at-system-runtime .title}

You can use the `modprobe`{.literal} command to find and unload a kernel module at system runtime from the currently loaded kernel.

Warning

You must not unload the kernel modules that are active in the running system. This can lead to an unstable or non-operational system.

**Prerequisites**

-   You have root permissions on the system.
-   The `kmod`{.literal} package is installed.

**Procedure**

1.  List all the loaded kernel modules:

    ``` {.language-plaintext tabindex="-1"}
    # lsmod
    ```

2.  Select the kernel module to unload.

    If a kernel module has dependencies, unload those before unloading the kernel module.

3.  Unload the relevant kernel module:

    ``` {.language-plaintext tabindex="-1"}
    # modprobe -r <pass:quotes[MODULE_NAME]>
    ```

    When entering the name of a kernel module, do not append the `.ko.xz`{.literal} extension to the end of the name. Kernel module names do not have extensions; their corresponding files do.

    Important

    Unloading inactive kernel modules will not disable modules configured for automatic loading at boot. These modules will be automatically loaded again when the system restarts.

**Verification**

-   Optionally, verify the relevant module is unloaded:

    ``` {.language-plaintext tabindex="-1"}
    $ lsmod | grep <pass:quotes[MODULE_NAME]>
    ```

    If the module is unloaded successfully, this command does not display any output.

**Additional resources**

-   [Preventing kernel modules from being automatically loaded at system boot time](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/managing-kernel-modules#preventing-kernel-modules-from-being-automatically-loaded-at-system-boot-time)
-   [Listing currently loaded kernel modules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/managing-kernel-modules#listing-currently-loaded-kernel-modules)
-   [Kernel module dependencies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/managing-kernel-modules#kernel-module-dependencies)

### [3.8. Unloading kernel modules at early stages of the boot process](#unloading-kernel-modules-at-early-stages-of-the-boot-process) {#unloading-kernel-modules-at-early-stages-of-the-boot-process .title}

To temporarily block a kernel module from loading early in the boot process, use the boot loader. This is useful when a module causes the system to become unresponsive before you can permanently disable it.

You can edit the relevant boot loader entry to unload the required kernel module before the booting sequence continues.

Important

The changes described in this procedure **do not persist** across system reboots. For information about how to add a kernel module to a denylist, see [Preventing kernel modules from being automatically loaded at system boot time](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/managing-kernel-modules#preventing-kernel-modules-from-being-automatically-loaded-at-system-boot-time).

**Prerequisites**

-   You have a loadable kernel module that you want to prevent from loading.

**Procedure**

1.  Boot the system into the boot loader.

2.  Use the cursor keys to highlight the relevant boot loader entry.

3.  Press the e key to edit the entry.

4.  Use the cursor keys to navigate to the line that starts with **linux**.

5.  Append `modprobe.blacklist=`{.literal}*`module_name`{.literal}* to the end of the line.

    The `serio_raw`{.literal} kernel module illustrates a rogue module to be unloaded early in the boot process.

6.  Press Ctrl+X to boot by using the modified configuration.

**Verification**

-   After the system boots, verify that the relevant kernel module is not loaded:

    ``` {.language-plaintext tabindex="-1"}
    # lsmod | grep serio_raw
    ```

**Additional resources**

-   [Managing kernel modules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/managing-kernel-modules)

### [3.9. Loading kernel modules automatically at system boot time](#loading-kernel-modules-automatically-at-system-boot-time) {#loading-kernel-modules-automatically-at-system-boot-time .title}

You can configure a kernel module to load automatically during the boot process.

**Prerequisites**

-   Root permissions
-   The `kmod`{.literal} package is installed.

**Procedure**

1.  Select a kernel module you want to load during the boot process.

    The modules are located in the `/lib/modules/$(uname -r)/kernel/<SUBSYSTEM>/`{.literal} directory.

2.  Create a configuration file for the module:

    ``` {.language-plaintext tabindex="-1"}
    # echo <MODULE_NAME> > /etc/modules-load.d/<MODULE_NAME>.conf
    ```

    Note

    When entering the name of a kernel module, do not append the `.ko.xz`{.literal} extension to the end of the name. Kernel module names do not have extensions; their corresponding files do.

**Verification**

1.  After reboot, verify the relevant module is loaded:

    ``` {.language-plaintext tabindex="-1"}
    $ lsmod | grep <MODULE_NAME>
    ```

    Important

    The changes described in this procedure **will persist** after rebooting the system.

    See the `modules-load.d(5)`{.literal} man page on your system for more information.

### [3.10. Preventing kernel modules from being automatically loaded at system boot time](#preventing-kernel-modules-from-being-automatically-loaded-at-system-boot-time) {#preventing-kernel-modules-from-being-automatically-loaded-at-system-boot-time .title}

Prevent the system from loading a kernel module automatically during the boot process by listing the module in the `modprobe`{.literal} configuration file with a corresponding command.

**Prerequisites**

-   The commands in this procedure require root privileges. Either use `su -`{.literal} to switch to the root user or preface the commands with `sudo`{.literal}.
-   The `kmod`{.literal} package is installed.
-   Ensure that your current system configuration does not require a kernel module you plan to deny.

**Procedure**

1.  List modules loaded to the currently running kernel by using the `lsmod`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ lsmod
    ```

    ``` {.language-plaintext tabindex="-1"}
    Module                  Size  Used by
    tls                   131072  0
    uinput                 20480  1
    snd_seq_dummy          16384  0
    snd_hrtimer            16384  1
    …
    ```

    In the output, identify the module you want to prevent from getting loaded.

    -   Alternatively, identify an unloaded kernel module you want to prevent from potentially loading in the `/lib/modules/`{.literal}*`<KERNEL-VERSION>`{.literal}*`/kernel/`{.literal}*`<SUBSYSTEM>`{.literal}*`/`{.literal} directory, for example:

        ``` {.language-plaintext tabindex="-1"}
        $ ls /lib/modules/6.12.0-55.9.1.el10_0.x86_64/kernel/crypto/
        ```

        ``` {.language-plaintext tabindex="-1"}
        ansi_cprng.ko.xz        chacha20poly1305.ko.xz  md4.ko.xz               serpent_generic.ko.xz
        anubis.ko.xz            cmac.ko.xz…
        ```

2.  Create a configuration file serving as a denylist:

    ``` {.language-plaintext tabindex="-1"}
    # touch /etc/modprobe.d/denylist.conf
    ```

3.  In a text editor of your choice, combine the names of modules you want to exclude from automatic loading to the kernel with the `blacklist`{.literal} configuration command, for example:

    ``` {.language-plaintext tabindex="-1"}
    # Prevents <KERNEL-MODULE-1> from being loaded
    blacklist <MODULE-NAME-1>
    install <MODULE-NAME-1> /bin/false

    # Prevents <KERNEL-MODULE-2> from being loaded
    blacklist <MODULE-NAME-2>
    install <MODULE-NAME-2> /bin/false
    …
    ```

    Because the `blacklist`{.literal} command does not prevent the module from getting loaded as a dependency for another kernel module that is not in a denylist, you must also define the `install`{.literal} line. In this case, the system runs `/bin/false`{.literal} instead of installing the module. The lines starting with a hash sign are comments you can use to make the file more readable.

    Note

    When entering the name of a kernel module, do not append the `.ko.xz`{.literal} extension to the end of the name. Kernel module names do not have extensions; their corresponding files do.

4.  Create a backup copy of the current initial RAM disk image before rebuilding:

    ``` {.language-plaintext tabindex="-1"}
    # cp /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).bak.$(date +%m-%d-%H%M%S).img
    ```

    -   Alternatively, create a backup copy of an initial RAM disk image which corresponds to the kernel version for which you want to prevent kernel modules from automatic loading:

        ``` {.language-plaintext tabindex="-1"}
        # cp /boot/initramfs-<VERSION>.img /boot/initramfs-<VERSION>.img.bak.$(date +%m-%d-%H%M%S)
        ```

5.  Generate a new initial RAM disk image to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # dracut -f -v
    ```

    -   If you build an initial RAM disk image for a different kernel version than your system currently uses, specify both target `initramfs`{.literal} and kernel version:

        ``` {.language-plaintext tabindex="-1"}
        # dracut -f -v /boot/initramfs-<TARGET-VERSION>.img <CORRESPONDING-TARGET-KERNEL-VERSION>
        ```

6.  Restart the system:

    ``` {.language-plaintext tabindex="-1"}
    $ reboot
    ```

    Important

    The changes described in this procedure **will take effect and persist** after rebooting the system. If you incorrectly list a key kernel module in the denylist, you can switch the system to an unstable or non-operational state.

**Additional resources**

-   [How do I prevent a kernel module from loading automatically? (Red Hat Knowledgebase)](https://access.redhat.com/solutions/41278)

### [3.11. Compiling custom kernel modules](#compiling-custom-kernel-modules) {#compiling-custom-kernel-modules .title}

Build a sample kernel module as requested by various configurations at hardware and software level.

**Prerequisites**

-   You installed the `kernel-devel`{.literal}, `gcc`{.literal}, and `elfutils-libelf-devel`{.literal} packages.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kernel-devel-$(uname -r) gcc elfutils-libelf-devel
    ```

-   You have root permissions.

-   You created the `/root/testmodule/`{.literal} directory where you compile the custom kernel module.

**Procedure**

1.  Create the `/root/testmodule/test.c`{.literal} file with the following content.

    ``` {.language-plaintext tabindex="-1"}
    #include <linux/module.h>
    #include <linux/kernel.h>

    int init_module(void)
        { printk("Hello World\n This is a test\n"); return 0; }

    void cleanup_module(void)
        { printk("Good Bye World"); }

    MODULE_LICENSE("GPL");
    ```

    The `test.c`{.literal} file is a source file that provides the main functionality to the kernel module. The file has been created in a dedicated `/root/testmodule/`{.literal} directory for organizational purposes. After the module compilation, the `/root/testmodule/`{.literal} directory will contain multiple files.

    The `test.c`{.literal} file includes from the system libraries:

    -   The `linux/kernel.h`{.literal} header file is necessary for the `printk()`{.literal} function in the example code.
    -   The `linux/module.h`{.literal} file contains function declarations and macro definitions that are shared across several source files written in C programming language.

2.  Follow the `init_module()`{.literal} and `cleanup_module()`{.literal} functions to start and end the kernel logging function `printk()`{.literal}, which prints text.

3.  Create the `/root/testmodule/Makefile`{.literal} file with the following content.

    ``` {.language-plaintext tabindex="-1"}
    obj-m := test.o
    ```

    The Makefile contains instructions for the compiler to produce an object file named `test.o`{.literal}. The `obj-m`{.literal} directive specifies that the resulting `test.ko`{.literal} file is going to be compiled as a loadable kernel module. Alternatively, the `obj-y`{.literal} directive can instruct to build `test.ko`{.literal} as a built-in kernel module.

4.  Compile the kernel module:

    ``` {.language-plaintext tabindex="-1"}
    # make -C /lib/modules/$(uname -r)/build M=/root/testmodule modules
    ```

    ``` {.language-plaintext tabindex="-1"}
    make: Entering directory '/usr/src/kernels/6.12.0-55.9.1.el10_0.x86_64'
      CC [M]  /root/testmodule/test.o
      MODPOST /root/testmodule/Module.symvers
      CC [M]  /root/testmodule/test.mod.o
      LD [M]  /root/testmodule/test.ko
      BTF [M] /root/testmodule/test.ko
    Skipping BTF generation for /root/testmodule/test.ko due to unavailability of vmlinux
    make: Leaving directory '/usr/src/kernels/6.12.0-55.9.1.el10_0.x86_64'
    ```

    The compiler creates an object file (`test.o`{.literal}) for each source file (`test.c`{.literal}) as an intermediate step before linking them together into the final kernel module (`test.ko`{.literal}).

    After a successful compilation, `/root/testmodule/`{.literal} contains additional files that relate to the compiled custom kernel module. The compiled module itself is represented by the `test.ko`{.literal} file.

**Verification**

1.  Optional: check the contents of the `/root/testmodule/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # ls -l /root/testmodule/
    ```

    ``` {.language-plaintext tabindex="-1"}
    total 152
    -rw-r--r--. 1 root root    16 Jul 26 08:19 Makefile
    -rw-r--r--. 1 root root    25 Jul 26 08:20 modules.order
    -rw-r--r--. 1 root root     0 Jul 26 08:20 Module.symvers
    -rw-r--r--. 1 root root   224 Jul 26 08:18 test.c
    -rw-r--r--. 1 root root 62176 Jul 26 08:20 test.ko
    -rw-r--r--. 1 root root    25 Jul 26 08:20 test.mod
    -rw-r--r--. 1 root root   849 Jul 26 08:20 test.mod.c
    -rw-r--r--. 1 root root 50936 Jul 26 08:20 test.mod.o
    -rw-r--r--. 1 root root 12912 Jul 26 08:20 test.o
    ```

2.  Copy the kernel module to the `/lib/modules/$(uname -r)/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp /root/testmodule/test.ko /lib/modules/$(uname -r)/
    ```

3.  Update the modular dependency list:

    ``` {.language-plaintext tabindex="-1"}
    # depmod -a
    ```

4.  Load the kernel module:

    ``` {.language-plaintext tabindex="-1"}
    # modprobe -v test
    ```

    ``` {.language-plaintext tabindex="-1"}
    insmod /lib/modules/6.12.0-55.9.1.el10_0.x86_64/test.ko
    ```

5.  Verify that the kernel module was successfully loaded:

    ``` {.language-plaintext tabindex="-1"}
    # lsmod | grep test
    ```

    ``` {.language-plaintext tabindex="-1"}
    test                   16384  0
    ```

6.  Read the latest messages from the kernel ring buffer:

    ``` {.language-plaintext tabindex="-1"}
    # dmesg
    ```

    ``` {.language-plaintext tabindex="-1"}
    [74422.545004] Hello World
                    This is a test
    ```

## [Chapter 4. Configuring kernel command-line parameters](#configuring-kernel-command-line-parameters) {#chapter-4.-configuring-kernel-command-line-parameters .title}

Use kernel command-line parameters to change the behavior of certain aspects of the Red Hat Enterprise Linux kernel at boot time. System administrators control which options are set at boot. Note that certain kernel behaviors can only be set at boot time.

Important

Changing the behavior of the system by modifying kernel command-line parameters can have negative effects on your system. Always test changes before deploying them in production. For further guidance, contact Red Hat Support.

### [4.1. What are kernel command-line parameters](#understanding-kernel-command-line-parameters) {#what-are-kernel-command-line-parameters .title}

With kernel command-line parameters, you can overwrite default values and set specific hardware settings. At boot time, you can configure the Red Hat Enterprise Linux kernel, the initial RAM disk, and user space features.

By default, the kernel command-line parameters for systems by using the GRUB boot loader are defined in the boot entry configuration file for each kernel boot entry.

You can manipulate boot loader configuration files by using the `grubby`{.literal} utility. With `grubby`{.literal}, you can perform these actions:

-   Change the default boot entry.
-   Add or remove arguments from a GRUB menu entry.

### [4.2. Understanding boot entries](#what-boot-entries-are) {#understanding-boot-entries .title}

Understand boot entries to manage your system's kernel configurations.

A boot entry is a collection of options stored in a configuration file and tied to a particular kernel version. In practice, you have at least as many boot entries as your system has installed kernels. The boot entry configuration file is located in the `/boot/loader/entries/`{.literal} directory:

``` {.language-plaintext tabindex="-1"}
d8712ab6d4f14683c5625e87b52b6b6e-6.12.0.el10_0.x86_64.conf
```

The file name consists of a machine ID stored in the `/etc/machine-id`{.literal} file, and a kernel version.

The boot entry configuration file contains information about the kernel version, the initial ramdisk image, and the kernel command-line parameters. The following example shows the contents of a boot entry config:

``` {.language-plaintext tabindex="-1"}
title Red Hat Enterprise Linux (6.12.0-0.el10_0.x86_64) 10.0
version 6.12.0-0.el10_0.x86_64
linux /vmlinuz-6.12.0-0.el10_0.x86_64
initrd /initramfs-6.12.0-0.el10_0.x86_64.img
options root=/dev/mapper/rhel_kvm--02--guest08-root ro crashkernel=2G-64G:256M,64G-:512M resume=/dev/mapper/rhel_kvm--02--guest08-swap rd.lvm.lv=rhel_kvm-02-guest08/root rd.lvm.lv=rhel_kvm-02-guest08/swap console=ttyS0,115200
grub_users $grub_users
grub_arg --unrestricted
grub_class kernel
```

### [4.3. Changing kernel command-line parameters for all boot entries](#changing-kernel-command-line-parameters-for-all-boot-entries) {#changing-kernel-command-line-parameters-for-all-boot-entries .title}

Change kernel command-line parameters for all boot entries on your system.

Important

When installing a newer version of the kernel in Red Hat Enterprise Linux 10 systems, the `grubby`{.literal} tool passes the kernel command-line arguments from the previous kernel version.

**Prerequisites**

-   `grubby`{.literal} utility is installed on your system.
-   `zipl`{.literal} utility is installed on your IBM Z system.

**Procedure**

-   To add a parameter:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=ALL --args="<NEW_PARAMETER>"
    ```

    For systems that use the GRUB boot loader and, on IBM Z that use the zIPL boot loader, the command adds a new kernel parameter to each `/boot/loader/entries/<`{.literal}*`ENTRY`{.literal}*`>.conf`{.literal} file.

    -   On IBM Z, update the boot menu:

        ``` {.language-plaintext tabindex="-1"}
        # zipl
        ```

-   To remove a parameter:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=ALL --remove-args="<PARAMETER_TO_REMOVE>"
    ```

    -   On IBM Z, update the boot menu:

        ``` {.language-plaintext tabindex="-1"}
        # zipl
        ```

        Note

        There is no need to update boot menu for the systems the use the GRUB boot loader.

**Additional resources**

-   [What are kernel command-line parameters](#understanding-kernel-command-line-parameters "4.1. What are kernel command-line parameters")

### [4.4. Changing kernel command-line parameters for a single boot entry](#changing-kernel-command-line-parameters-for-a-single-boot-entry) {#changing-kernel-command-line-parameters-for-a-single-boot-entry .title}

Make changes in kernel command-line parameters for a single boot entry on your system.

**Prerequisites**

-   `grubby`{.literal} and `zipl`{.literal} utilities are installed on your system.

**Procedure**

-   To add a parameter:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=/boot/vmlinuz-$(uname -r) --args="<NEW_PARAMETER>"
    ```

    -   On IBM Z, update the boot menu:

        ``` {.language-plaintext tabindex="-1"}
        # grubby --args="<NEW_PARAMETER> --update-kernel=ALL --zipl
        ```

-   To remove a parameter:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=/boot/vmlinuz-$(uname -r) --remove-args="<PARAMETER_TO_REMOVE>"
    ```

    -   On IBM Z, update the boot menu:

        ``` {.language-plaintext tabindex="-1"}
        # grubby --args="<NEW_PARAMETER> --update-kernel=ALL --zipl
        ```

        Important

        `grubby`{.literal} modifies and stores the kernel command-line parameters of an individual kernel boot entry in the `/boot/loader/entries/<`{.literal}*`ENTRY`{.literal}*`>.conf`{.literal} file.

### [4.5. Changing kernel command-line parameters temporarily at boot time](#changing-kernel-command-line-parameters-temporarily-at-boot-time) {#changing-kernel-command-line-parameters-temporarily-at-boot-time .title}

Make temporary changes to a Kernel Menu Entry by changing the kernel parameters only during a single boot process. This procedure applies only for a single boot and does not persist after system reboot.

**Procedure**

1.  Boot into the GRUB boot menu.

2.  Select the kernel you want to start.

3.  Press the e key to edit the kernel parameters.

4.  Find the kernel command line by moving the cursor down.

5.  Move the cursor to the end of the line.

6.  Edit the kernel parameters as required. For example, to run the system in emergency mode, add the `emergency`{.literal} parameter at the end of the `linux`{.literal} line:

    ``` {.language-plaintext tabindex="-1"}
    linux   ($root)/vmlinuz-6.12.0-0.el10_0.x86_64 root=/dev/mapper/rhel-root ro crashkernel=2G-64G:256M,64G-:512M resume=/dev/mapper/rhel-swap rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet emergency
    ```

    To enable the system messages, remove the `rhgb`{.literal} and `quiet`{.literal} parameters.

7.  Press Ctrl+x to boot with the selected kernel and the modified command line parameters.

    Important

    If you press the Esc key to leave command line editing, it will drop all the user made changes.

### [4.6. Configuring GRUB settings to enable serial console connection](#configuring-grub-2-settings-to-enable-serial-console-connection) {#configuring-grub-settings-to-enable-serial-console-connection .title}

To connect to a headless server or embedded system when the network is down, you can configure GRUB 2 to enable a serial console connection. This also provides login access on a different system to avoid security rules.

You need to configure some default GRUB settings to use the serial console connection.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Add the following two lines to the `/etc/default/grub`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    GRUB_TERMINAL="serial"
    GRUB_SERIAL_COMMAND="serial --speed=9600 --unit=0 --word=8 --parity=no --stop=1"
    ```

    The first line configures GRUB to use the serial command line instead of the graphical interface. The `GRUB_TERMINAL`{.literal} key overrides values of `GRUB_TERMINAL_INPUT`{.literal} and `GRUB_TERMINAL_OUTPUT`{.literal} keys.

    The second line adjusts the baud rate (`--speed`{.literal}), parity and other values to fit your environment and hardware. Note that a higher baud rate, for example 115200, is preferable for tasks such as following log files.

2.  Update the GRUB configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # grub2-mkconfig -o /boot/grub2/grub.cfg
    ```

    This applies to both, BIOS and UEFI based machines.

3.  Reboot the system for the changes to take effect.

### [4.7. Changing boot entries with the GRUB configuration file](#changing-boot-entries-with-the-grub-configuration-file) {#changing-boot-entries-with-the-grub-configuration-file .title}

To change boot entries for the Linux kernel, you can modify the `/etc/default/grub`{.literal} configuration file. This file contains the `GRUB_CMDLINE_LINUX`{.literal} key, which lists the kernel command-line arguments.

The `GRUB_CMDLINE_LINUX`{.literal} key in `/etc/default/grub`{.literal} lists kernel command-line arguments:

``` {.language-plaintext tabindex="-1"}
GRUB_CMDLINE_LINUX="crashkernel=2G-64G:256M,64G-:512M resume=/dev/mapper/rhel-swap rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap"
```

To change the boot entries, overwrite Boot Loader Specification (BLS) snippets with the contents of the `GRUB_CMDLINE_LINUX`{.literal} values.

**Prerequisites**

-   A fresh Red Hat Enterprise Linux 10 installation.

**Procedure**

1.  Add or remove a kernel parameter for individual kernels in a post installation script with `grubby`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel <PATH_TO_KERNEL> --args "<NEW_ARGUMENTS>"
    ```

    For example, add the `noapic`{.literal} parameter to the chosen kernel:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel /boot/vmlinuz-6.12.0-0.el10_0.x86_64 --args "noapic"
    ```

    The parameter is propagated into the BLS snippets, but not into the `/etc/default/grub`{.literal} file.

2.  Overwrite BLS snippets with the contents of the `GRUB_CMDLINE_LINUX`{.literal} values present in the `/etc/default/grub`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # grub2-mkconfig -o /boot/grub2/grub.cfg --update-bls-cmdline
    ```

    ``` {.language-plaintext tabindex="-1"}
    Generating grub configuration file ...
    Adding boot menu entry for UEFI Firmware Settings ...
    done
    ```

    Note

    Other changes to keys in `/etc/default/grub`{.literal}, such as `GRUB_TIMEOUT`{.literal}, are propagated to the new `grub.cfg`{.literal} file when you run `grub2-mkconfig`{.literal}.

**Verification**

1.  Reboot your system.

2.  Verify that the parameters are included in the `/proc/cmdline`{.literal} file.

    For example, if you added the `noapic`{.literal} parameter, the `/proc/cmdline`{.literal} file contains the following:

    ``` {.language-plaintext tabindex="-1"}
    BOOT_IMAGE=(hd0,gpt2)/vmlinuz-6.12.0-0.el10_0.x86_64 root=/dev/mapper/RHELCSB-Root ro vconsole.keymap=us crashkernel=2G-64G:256M,64G-:512M rd.lvm.lv=RHELCSB/Root rd.luks.uuid=luks-d8a28c4c-96aa-4319-be26-96896272151d rhgb quiet noapic rd.luks.key=d8a28c4c-96aa-4319-be26-96896272151d=/keyfile:UUID=c47d962e-4be8-41d6-8216-8cf7a0d3b911 ipv6.disable=1
    ```

    **Additional resources**

    -   [Changing kernel command-line parameters for all boot entries](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/configuring-kernel-command-line-parameters#changing-kernel-command-line-parameters-for-all-boot-entries)

## [Chapter 5. Configuring kernel parameters at runtime](#configuring-kernel-parameters-at-runtime) {#chapter-5.-configuring-kernel-parameters-at-runtime .title}

Modify the behavior of the Red Hat Enterprise Linux kernel at runtime by using the `sysctl`{.literal} command and by modifying configuration files in the `/etc/sysctl.d/`{.literal} and `/proc/sys/`{.literal} directories.

Important

Configuring kernel parameters on a production system requires careful planning. Unplanned changes can render the kernel unstable, requiring a system reboot. Verify that you are using valid options before changing any kernel values.

### [5.1. What are kernel parameters](#what-are-kernel-parameters) {#what-are-kernel-parameters .title}

Kernel parameters are tunable values that you can adjust while the system is running. Note that for changes to take effect, you do not need to reboot the system or recompile the kernel.

The difference between kernel parameters and kernel command line parameters is; Kernel parameters can configure the Linux kernel with all the options, while kernel command line parameters are the specific arguments passed to the kernel during boot, allowing runtime configuration without kernel recompilation.

It is possible to address the kernel parameters through:

-   The `sysctl`{.literal} command
-   The virtual file system mounted at the `/proc/sys/`{.literal} directory
-   The configuration files in the `/etc/sysctl.d/`{.literal} directory

Tunables are divided into classes by the kernel subsystem. Red Hat Enterprise Linux has the following tunable classes:

+----------------------+-----------------------------------------------------+
| Tunable class        | Subsystem                                           |
+:=====================+:====================================================+
| `abi`{.literal}      | Execution domains and personalities                 |
+----------------------+-----------------------------------------------------+
| `crypto`{.literal}   | Cryptographic interfaces                            |
+----------------------+-----------------------------------------------------+
| `debug`{.literal}    | Kernel debugging interfaces                         |
+----------------------+-----------------------------------------------------+
| `dev`{.literal}      | Device-specific information                         |
+----------------------+-----------------------------------------------------+
| `fs`{.literal}       | Global and specific file system tunables            |
+----------------------+-----------------------------------------------------+
| `kernel`{.literal}   | Global kernel tunables                              |
+----------------------+-----------------------------------------------------+
| `net`{.literal}      | Network tunables                                    |
+----------------------+-----------------------------------------------------+
| `sunrpc`{.literal}   | Sun Remote Procedure Call (NFS)                     |
+----------------------+-----------------------------------------------------+
| `user`{.literal}     | User Namespace limits                               |
+----------------------+-----------------------------------------------------+
| `vm`{.literal}       | Tuning and management of memory, buffers, and cache |
+----------------------+-----------------------------------------------------+

: Table 5.1. Table of sysctl classes

Show more

**Additional resources**

-   [Tuning Red Hat Enterprise Linux for IBM DB2](https://access.redhat.com/solutions/3530941)

### [5.2. Configuring kernel parameters temporarily with sysctl](#configuring-kernel-parameters-temporarily-with-sysctl) {#configuring-kernel-parameters-temporarily-with-sysctl .title}

You can use the `sysctl`{.literal} command to temporarily set kernel parameters at runtime. The command is also useful for listing and filtering tunables.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  List all parameters and their values.

    ``` {.language-plaintext tabindex="-1"}
    # sysctl -a
    ```

    Note

    The `sysctl -a`{.literal} command displays kernel parameters, which can be adjusted at runtime and at boot time.

2.  To configure a parameter temporarily, enter:

    ``` {.language-plaintext tabindex="-1"}
    # sysctl <TUNABLE_CLASS>.<PARAMETER>=<TARGET_VALUE>
    ```

    This sample changes the parameter value while the system is running. The changes take effect immediately and it does not require system reboot.

    Note

    The changes return back to default after your system reboots.

**Additional resources**

-   [Using configuration files in /etc/sysctl.d/ to adjust kernel parameters](#using-configuration-files-in-etc-sysctl-d-to-adjust-kernel-parameters "5.4. Using configuration files in /etc/sysctl.d/ to adjust kernel parameters")

### [5.3. Configuring kernel parameters permanently with sysctl](#configuring-kernel-parameters-permanently-with-sysctl) {#configuring-kernel-parameters-permanently-with-sysctl .title}

You can use the `sysctl`{.literal} command to permanently set kernel parameters.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  List all parameters:

    ``` {.language-plaintext tabindex="-1"}
    # sysctl -a
    ```

    The command displays all kernel parameters that can be configured at runtime.

2.  Configure a parameter permanently:

    ``` {.language-plaintext tabindex="-1"}
    # sysctl -w <TUNABLE_CLASS>.<PARAMETER>=<TARGET_VALUE> >> /etc/sysctl.conf
    ```

    The sample command changes the tunable value and writes it to the `/etc/sysctl.conf`{.literal} file, which overrides the default values of kernel parameters. The changes take effect immediately and persistently, without a need for restart.

    Note

    To permanently modify kernel parameters, you can also make manual changes to the configuration files in the `/etc/sysctl.d/`{.literal} directory.

**Additional resources**

-   [Using configuration files in /etc/sysctl.d/ to adjust kernel parameters](#using-configuration-files-in-etc-sysctl-d-to-adjust-kernel-parameters "5.4. Using configuration files in /etc/sysctl.d/ to adjust kernel parameters")

### [5.4. Using configuration files in /etc/sysctl.d/ to adjust kernel parameters](#using-configuration-files-in-etc-sysctl-d-to-adjust-kernel-parameters) {#using-configuration-files-in-etcsysctl.d-to-adjust-kernel-parameters .title}

To permanently set kernel parameters, manually modify the configuration files in the `/etc/sysctl.d/`{.literal} directory.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Create a new configuration file in `/etc/sysctl.d/`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # vim /etc/sysctl.d/<some_file.conf>
    ```

2.  Include kernel parameters, one per line:

    ``` {.language-plaintext tabindex="-1"}
    <TUNABLE_CLASS>.<PARAMETER>=<TARGET_VALUE>
    <TUNABLE_CLASS>.<PARAMETER>=<TARGET_VALUE>
    ```

3.  Save the configuration file.

4.  Reboot the machine for the changes to take effect.

    -   Alternatively, apply changes without rebooting:

        ``` {.language-plaintext tabindex="-1"}
        # sysctl -p /etc/sysctl.d/<some_file.conf>
        ```

        With this command, you can read values from the configuration file which you created earlier.

        See `sysctl(8)`{.literal} and `sysctl.d(5)`{.literal} man pages on your system for more information.

### [5.5. Configuring kernel parameters temporarily through /proc/sys/](#configuring-kernel-parameters-temporarily-through-proc-sys) {#configuring-kernel-parameters-temporarily-through-procsys .title}

To set kernel parameters temporarily, modify the files in the `/proc/sys/`{.literal} virtual file system directory.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Identify a kernel parameter you want to configure:

    ``` {.language-plaintext tabindex="-1"}
    # ls -l /proc/sys/<TUNABLE_CLASS>/
    ```

    The writable files returned by the command can be used to configure the kernel. The files with read-only permissions provide feedback on the current settings.

2.  Assign a target value to the kernel parameter:

    ``` {.language-plaintext tabindex="-1"}
    # echo <TARGET_VALUE> > /proc/sys/<TUNABLE_CLASS>/<PARAMETER>
    ```

    The configuration changes applied by using a command are not permanent and will disappear after system reboot.

**Verification**

1.  Verify the value of the newly set kernel parameter:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/sys/<TUNABLE_CLASS>/<PARAMETER>
    ```

## [Chapter 6. Configuring kernel parameters permanently by using RHEL system roles](#configuring-kernel-parameters-permanently-by-using-rhel-system-roles) {#chapter-6.-configuring-kernel-parameters-permanently-by-using-rhel-system-roles .title}

You can use the `kernel_settings`{.literal} RHEL system role to configure kernel parameters on multiple clients at once.

Simultaneous configuration has the following advantages:

-   Provides a friendly interface with efficient input setting.
-   Keeps all intended kernel parameters in one place.

After you run the `kernel_settings`{.literal} role from the control machine, the kernel parameters are applied to the managed systems immediately and persist across reboots.

Important

Note that RHEL system roles delivered over RHEL channels are available to RHEL customers as an RPM package in the default AppStream repository. RHEL system roles are also available as a collection to customers with Ansible subscriptions over Ansible Automation Hub.

### [6.1. Applying selected kernel parameters by using the kernel_settings RHEL system role](#applying-selected-kernel-parameters-by-using-the-kernelsettings-productshortname-system-role) {#applying-selected-kernel-parameters-by-using-the-kernel_settings-rhel-system-role .title}

You can use the `kernel_settings`{.literal} RHEL system role to remotely configure various kernel parameters across multiple managed operating systems with persistent effects.

For example, by using the `kernel_settings`{.literal} role, you can configure:

-   Transparent hugepages to increase performance by reducing the overhead of managing smaller pages.
-   The largest packet sizes are to be transmitted over the network with the loopback interface.
-   Limits on files, which can be opened simultaneously.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configuring kernel settings
      hosts: managed-node-01.example.com
      tasks:
        - name: Configure hugepages, packet size for loopback device, and limits on simultaneously open files.
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.kernel_settings
          vars:
            kernel_settings_sysctl:
              - name: fs.file-max
                value: 400000
              - name: kernel.threads-max
                value: 65536
            kernel_settings_sysfs:
              - name: /sys/class/net/lo/mtu
                value: 65000
            kernel_settings_transparent_hugepages: madvise
            kernel_settings_reboot_ok: true
    ```

    The settings specified in the example playbook include the following:

    `kernel_settings_sysfs: `{.literal}*`<list_of_sysctl_settings>`{.literal}*
    :   A YAML list of `sysctl`{.literal} settings and the values you want to assign to these settings.

    `kernel_settings_transparent_hugepages: `{.literal}*`<value>`{.literal}*
    :   Controls the memory subsystem Transparent Huge Pages (THP) setting. You can disable THP support (`never`{.literal}), enable it system wide (`always`{.literal}) or inside `MAD_HUGEPAGE`{.literal} regions (`madvise`{.literal}).

    `kernel_settings_reboot_ok: `{.literal}*`<true|false>`{.literal}*

    :   The default is `false`{.literal}. If set to `true`{.literal}, the system role determines if a reboot of the managed host is necessary for the requested changes to take effect and reboot it. If set to `false`{.literal}, the role returns the variable `kernel_settings_reboot_required`{.literal} with a value of `true`{.literal}, indicating that a reboot is required. In this case, a user must reboot the managed node manually.

        For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.kdump/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Verify the affected kernel parameters:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'sysctl fs.file-max kernel.threads-max net.ipv6.conf.lo.mtu'
    # ansible managed-node-01.example.com -m command -a 'cat /sys/kernel/mm/transparent_hugepage/enabled'
    ```

## [Chapter 7. Managing kernel command-line parameters with UKI](#managing-kernel-command-line-parameters-with-uki) {#chapter-7.-managing-kernel-command-line-parameters-with-uki .title}

Unified Kernel Image (UKI) combines the kernel, initial RAM disk (initrd), and boot command line into a single executable binary.

### [7.1. Understanding kernel command-line parameters with UKI](#understanding-kernel-command-line-parameters-with-uki) {#understanding-kernel-command-line-parameters-with-uki .title}

With Unified Kernel Image (UKI), `systemd-boot`{.literal}, specifically `systemd-stub`{.literal}, handles the kernel command-line parameters. The UKI delivered by Red Hat includes the basic kernel command-line parameter `console=tty0 console=ttyS0`{.literal}.

You can add additional kernel command-line parameters by using UKI add-ons. Alternatively, you can generate your own UKI to contain any arguments you require.

Important

Secure Boot revokes improperly signed UKIs and add-ons. These signatures can also alter Platform Configuration Register (PCR) measurements in the Trusted Platform Module (TPM), which can potentially affect boot sequence.

### [7.2. Understanding boot entries](#understanding-boot-entries) {#understanding-boot-entries-1 .title}

You manage boot entries directly in UEFI NVRAM. This means they are no longer stored on disk. You can use tools such as `kernel-bootcfg`{.literal} or `efibootmgr`{.literal} to alter boot entries directly.

The following is an example of a boot entry:

``` {.language-plaintext tabindex="-1"}
Boot0001* redhat HD(1,GPT,9192a707-8768-4c9f-bb11-fdd7c7e307e7,0x800,0x100000)/\EFI\redhat\shimx64.efi\EFI\Linux\ffffffffffffffffffffffffffffffff-6.12.0-174.el10.x86_64.efi
```

### [7.3. Acquire UKI add-ons to add kernel command-line parameters](#acquire-uki-add-ons-to-add-kernel-command-line-parameters) {#acquire-uki-add-ons-to-add-kernel-command-line-parameters .title}

Officially signed UKI add-ons in the `kernel-uki-virt-addons`{.literal} packages from Red Hat provide kernel command-line parameters. Red Hat signs these add-ons with the same certificates as their associated UKIs. The default installation path is `/lib/modules/$(uname -r)/vmlinuz-virt.efi.extra.d/`{.literal}.

Note

Add-ons take effect only after you copy them to the correct location for the target UKI or for all boot entries.

If you need add-ons other than the signed add-ons from the package, or you prefer to sign add-ons yourself, create them with tools such as `systemd-ukify`{.literal} or `dracut`{.literal}.

**Additional resources**

-   [Understanding kernel command-line parameters with UKI](#understanding-kernel-command-line-parameters-with-uki "7.1. Understanding kernel command-line parameters with UKI")
-   [Changing kernel command-line parameters for all boot entries](#changing-kernel-command-line-parameters-for-all-boot-entries-with-uki "7.4. Changing kernel command-line parameters for all boot entries")
-   [Changing kernel command-line parameters for a single UKI](#changing-kernel-command-line-parameters-for-a-single-uki "7.5. Changing kernel command-line parameters for a single UKI")
-   [Creating UKI to contain customized kernel command-line parameters](#creating-uki-to-contain-customized-kernel-command-line-parameters "7.6. Creating UKI to contain customized kernel command-line parameters")

### [7.4. Changing kernel command-line parameters for all boot entries](#changing-kernel-command-line-parameters-for-all-boot-entries-with-uki) {#changing-kernel-command-line-parameters-for-all-boot-entries-1 .title}

To change kernel command-line parameters for all boot entries, add the UKI add-ons to the global add-ons directory `/boot/efi/loader/addons/`{.literal}.

**Prerequisites**

-   You have root permissions on the system.
-   You have `.addon.efi`{.literal} file.

**Procedure**

1.  Copy the add-on file to the `/boot/efi/loader/addons/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp <my-addon>.addon.efi /boot/efi/loader/addons/
    ```

2.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

-   Verify the new parameter depends on the type of the added add-on. For example, check the kernel command line:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/cmdline
    ```

### [7.5. Changing kernel command-line parameters for a single UKI](#changing-kernel-command-line-parameters-for-a-single-uki) {#changing-kernel-command-line-parameters-for-a-single-uki .title}

To change kernel command-line parameters for a single UKI, manage the add-ons on a per-UKI basis. The revocation mechanism applies to UKI and its associated add-ons locally.

By default, UKIs are located at the following path:

`/boot/efi/EFI/Linux/`{.literal}*`<machine_id>`{.literal}*`-`{.literal}*`<kernel_version>`{.literal}*`.efi`{.literal}

The effective add-ons designated to this UKI are located at the following path:

`/boot/efi/EFI/Linux/`{.literal}*`<machine_id>`{.literal}*`-`{.literal}*`<kernel_version>`{.literal}*`.efi.extra.d/`{.literal}

**Prerequisites**

-   You have root permissions on the system.
-   You have an `.addon.efi`{.literal} add-on file.

**Procedure**

1.  Identify the running kernel version and machine ID:

    ``` {.language-plaintext tabindex="-1"}
    # uname -r
    # cat /etc/machine-id
    ```

2.  Copy the add-on file to the specific directory associated with the UKI:

    ``` {.language-plaintext tabindex="-1"}
    # cp <my-addon>.addon.efi /boot/efi/EFI/Linux/<machine_id>-<kernel_version>.efi.extra.d/
    ```

3.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

-   Verify the new parameter depends on the type of the added add-on. For example, check the kernel command line:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/cmdline
    ```

Note

When you update the `kernel-uki-virt`{.literal} package, the system installs a new UKI version. The update also copies the currently effective add-ons to the directory for the new UKI, provided that the `kernel-uki-virt-addons`{.literal} package is installed at the same time. This happens automatically, for example, when you run `dnf update`{.literal}.

**Additional resources**

-   [Acquire UKI add-ons to add kernel command-line parameters](#acquire-uki-add-ons-to-add-kernel-command-line-parameters "7.3. Acquire UKI add-ons to add kernel command-line parameters")
-   [Understanding kernel command-line parameters with UKI](#understanding-kernel-command-line-parameters-with-uki "7.1. Understanding kernel command-line parameters with UKI")
-   [Changing kernel command-line parameters for all boot entries](#changing-kernel-command-line-parameters-for-all-boot-entries-with-uki "7.4. Changing kernel command-line parameters for all boot entries")

### [7.6. Creating UKI to contain customized kernel command-line parameters](#creating-uki-to-contain-customized-kernel-command-line-parameters) {#creating-uki-to-contain-customized-kernel-command-line-parameters .title}

To customize the Linux kernel, initial RAM disk, or initrd, and kernel command-line parameters, you can create your own UKI by using tools such as `systemd-ukify`{.literal} or `dracut`{.literal}.

**Procedure**

-   For example, to create a custom UKI by using `systemd-ukify`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # ukify build --initrd /boot/initramfs-$(uname -r).img --linux /lib/modules/$(uname -r)/vmlinuz --uname $(uname -r) --cmdline "console=tty0 console=ttyS0 emergency" --output uki.unsigned.efi
    ```

## [Chapter 8. Configuring the GRUB 2 boot loader by using RHEL system roles](#configuring-the-grub-2-boot-loader-by-using-rhel-system-roles) {#chapter-8.-configuring-the-grub-2-boot-loader-by-using-rhel-system-roles .title}

By using the `bootloader`{.literal} RHEL system role, you can automate the configuration and management tasks related to the GRUB2 boot loader.

This role currently supports configuring the GRUB2 boot loader, which runs on the following CPU architectures:

-   AMD and Intel 64-bit architectures (x86-64)
-   The 64-bit ARM architecture (ARMv8.0)
-   IBM Power Systems, Little Endian (POWER9)

### [8.1. Updating the existing boot loader entries by using the bootloader RHEL system role](#updating-the-existing-boot-loader-entries-by-using-the-bootloader-rhel-system-role) {#updating-the-existing-boot-loader-entries-by-using-the-bootloader-rhel-system-role .title}

You can use the `bootloader`{.literal} RHEL system role to update the existing entries in the GRUB2 boot menu in an automated fashion. This way you can efficiently pass specific kernel command-line parameters that can optimize the performance or behavior of your systems.

For example, if you leverage systems, where detailed boot messages from the kernel and init system are not necessary, use `bootloader`{.literal} to apply the `quiet`{.literal} parameter to your existing boot loader entries on your managed nodes to achieve a cleaner, less cluttered, and more user-friendly booting experience.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   You identified the kernel that corresponds to the boot loader entry you want to update.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configuration and management of GRUB2 boot loader
      hosts: managed-node-01.example.com
      tasks:
        - name: Update existing boot loader entries
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.bootloader
          vars:
            bootloader_settings:
              - kernel:
                  path: /boot/vmlinuz-6.12.0-0.el10_0.aarch64
                options:
                  - name: quiet
                    state: present
            bootloader_reboot_ok: true
    ```

    The settings specified in the example playbook include the following:

    `kernel`{.literal}
    :   Specifies the kernel connected with the boot loader entry that you want to update.

    `options`{.literal}
    :   Specifies the kernel command-line parameters to update for your chosen boot loader entry (kernel).

    `bootloader_reboot_ok: `{.literal}*`true`{.literal}*
    :   The role detects that a reboot is needed for the changes to take effect and performs a restart of the managed node.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.bootloader/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Check that your specified boot loader entry has updated kernel command-line parameters:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m ansible.builtin.command -a 'grubby --info=ALL'
    managed-node-01.example.com | CHANGED | rc=0 >>
    ...
    index=1
    kernel="/boot/vmlinuz-6.12.0-0.el10_0.aarch64"
    args="ro crashkernel=2G-4G:256M,4G-64G:320M,64G-:576M rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap $tuned_params quiet"
    root="/dev/mapper/rhel-root"
    initrd="/boot/initramfs-6.12.0-0.el10_0.aarch64.img $tuned_initrd"
    title="Red Hat Enterprise Linux (6.12.0-0.el10_0.aarch64) 10"
    id="2c9ec787230141a9b087f774955795ab-6.12.0-0.el10_0.aarch64"
    ...
    ```

### [8.2. Securing the boot menu with password by using the bootloader RHEL system role](#securing-the-boot-menu-with-password-by-using-the-bootloader-rhel-system-role) {#securing-the-boot-menu-with-password-by-using-the-bootloader-rhel-system-role .title}

You can use the `bootloader`{.literal} RHEL system role to set a password to the GRUB2 boot menu in an automated fashion. This way you can efficiently prevent unauthorized users from modifying boot parameters, and to have better control over the system boot.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Store your sensitive variables in an encrypted file:

    a.  Create the vault:

        ``` {.language-plaintext tabindex="-1"}
        $ ansible-vault create ~/vault.yml
        New Vault password: <vault_password>
        Confirm New Vault password: <vault_password>
        ```

    b.  After the `ansible-vault create`{.literal} command opens an editor, enter the sensitive data in the *`<key>`{.literal}*`: `{.literal}*`<value>`{.literal}* format:

        ``` {.language-plaintext tabindex="-1"}
        pwd: <password>
        ```

    c.  Save the changes, and close the editor. Ansible encrypts the data in the vault.

2.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configuration and management of GRUB2 boot loader
      hosts: managed-node-01.example.com
      vars_files:
        - ~/vault.yml
      tasks:
        - name: Set the bootloader password
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.bootloader
          vars:
            bootloader_password: "{{ pwd }}"
            bootloader_reboot_ok: true
    ```

    The settings specified in the example playbook include the following:

    `bootloader_password: `{.literal}*`"{{ pwd }}"`{.literal}*
    :   The variable ensures protection of boot parameters with a password.

    `bootloader_reboot_ok: `{.literal}*`true`{.literal}*
    :   The role detects that a reboot is needed for the changes to take effect and performs a restart of the managed node.

    Important

    Changing the boot loader password is not an idempotent transaction. This means that if you apply the same Ansible playbook again, the result are not the same, and the state of the managed node changes.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.bootloader/README.md`{.literal} file on the control node.

3.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check --ask-vault-pass ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

4.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --ask-vault-pass ~/playbook.yml
    ```

**Verification**

1.  On your managed node during the GRUB2 boot menu screen, press the e key for edit.

2.  You will be prompted for a username and a password.

    `Enter username: root`{.literal}
    :   The boot loader username is always `root`{.literal} and you do not need to specify it in your Ansible playbook.

    `Enter password: `{.literal}*`<password>`{.literal}*
    :   The boot loader password corresponds to the `pwd`{.literal} variable that you defined in the `vault.yml`{.literal} file.

3.  You can view or edit configuration of the particular boot loader entry.

**Additional resources**

-   [Ansible vault](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/ansible-vault)

### [8.3. Setting a timeout for the boot loader menu by using the bootloader RHEL system role](#setting-a-timeout-for-the-boot-loader-menu-by-using-the-bootloader-rhel-system-role) {#setting-a-timeout-for-the-boot-loader-menu-by-using-the-bootloader-rhel-system-role .title}

You can use the `bootloader`{.literal} RHEL system role to configure a timeout for the GRUB2 boot loader menu in an automated fashion. This way you can efficiently update a period of time during which you can intervene and select a non-default boot entry for various purposes.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configuration and management of GRUB2 boot loader
      hosts: managed-node-01.example.com
      tasks:
        - name: Update the boot loader timeout
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.bootloader
          vars:
            bootloader_timeout: 10
    ```

    The settings specified in the example playbook include the following:

    `bootloader_timeout: 10`{.literal}
    :   Input an integer to control for how long the GRUB2 boot loader menu is displayed before booting the default entry.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.bootloader/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

1.  Remotely restart your managed node:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m ansible.builtin.reboot
    managed-node-01.example.com | CHANGED => {
        "changed": true,
        "elapsed": 21,
        "rebooted": true
    }
    ```

2.  On the managed node, observe the GRUB2 boot menu screen.

    `The highlighted entry will be executed automatically in 10s`{.literal}

    :   For how long this boot menu is displayed before GRUB2 automatically uses the default entry.

        -   Alternative: you can remotely query for the \"timeout\" settings in the `/boot/grub2/grub.cfg`{.literal} file of your managed node:

            ``` {.language-plaintext tabindex="-1"}
            # ansible managed-node-01.example.com -m ansible.builtin.command -a "grep 'timeout' /boot/grub2/grub.cfg"
            managed-node-01.example.com | CHANGED | rc=0 >>
            if [ x$feature_timeout_style = xy ] ; then
              set timeout_style=menu
              set timeout=10
            # Fallback normal timeout code in case the timeout_style feature is
              set timeout=10
            if [ x$feature_timeout_style = xy ] ; then
                set timeout_style=menu
                set timeout=10
                set orig_timeout_style=${timeout_style}
                set orig_timeout=${timeout}
                  # timeout_style=menu + timeout=0 avoids the countdown code keypress check
                  set timeout_style=menu
                  set timeout=10
                  set timeout_style=hidden
                  set timeout=10
            if [ x$feature_timeout_style = xy ]; then
              if [ "${menu_show_once_timeout}" ]; then
                set timeout_style=menu
                set timeout=10
                unset menu_show_once_timeout
                save_env menu_show_once_timeout
            ```

### [8.4. Collecting the boot loader configuration information by using the bootloader RHEL system role](#collecting-the-boot-loader-configuration-information-by-using-the-bootloader-rhel-system-role) {#collecting-the-boot-loader-configuration-information-by-using-the-bootloader-rhel-system-role .title}

You can use the `bootloader`{.literal} RHEL system role to gather information about the GRUB2 boot loader entries in an automated fashion. This way you can quickly identify that your systems are set up to boot correctly, all entries point to the right kernels and initial RAM disk images.

As a result, you can for example:

-   Prevent boot failures.
-   Revert to a known good state when troubleshooting.
-   Be sure that security-related kernel command-line parameters are correctly configured.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configuration and management of GRUB2 boot loader
      hosts: managed-node-01.example.com
      tasks:
        - name: Gather information about the boot loader configuration
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.bootloader
          vars:
            bootloader_gather_facts: true

        - name: Display the collected boot loader configuration information
          debug:
            var: bootloader_facts
    ```

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.bootloader/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   After you run the preceding playbook on the control node, you will see a similar command-line output as in the following example:

    ``` {.language-plaintext tabindex="-1"}
    ...
        "bootloader_facts": [
            {
                "args": "ro crashkernel=1G-4G:256M,4G-64G:320M,64G-:576M rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap $tuned_params quiet",
                "default": true,
                "id": "2c9ec787230141a9b087f774955795ab-6.12.el10_0.aarch64",
                "index": "1",
                "initrd": "/boot/initramfs-6.12.0.el10_0.aarch64.img $tuned_initrd",
                "kernel": "/boot/vmlinuz-6.12.0-0.el10_0.aarch64",
                "root": "/dev/mapper/rhel-root",
                "title": "Red Hat Enterprise Linux (6.12.0-0.el10_0.aarch64) 10"
            }
        ]
    ...
    ```

    The command-line output shows the following notable configuration information about the boot entry:

    `args`{.literal}
    :   Command-line parameters passed to the kernel by the GRUB2 boot loader during the boot process. They configure various settings and behaviors of the kernel, initramfs, and other boot-time components.

    `id`{.literal}
    :   Unique identifier assigned to each boot entry in a boot loader menu. It consists of machine ID and the kernel version.

    `root`{.literal}
    :   The root filesystem for the kernel to mount and use as the primary filesystem during the boot.

## [Chapter 9. Applying patches with kernel live patching](#applying-patches-with-kernel-live-patching) {#chapter-9.-applying-patches-with-kernel-live-patching .title}

The Red Hat Enterprise Linux kernel live patching solution patches a running kernel without rebooting or restarting processes. System administrators can apply critical security patches immediately, maintain system uptime, and reduce reboots. Live patching does not address all critical or important CVEs.

Important

RHEL 10 kpatch support starts from RHEL 10.2. The first kpatch-supported kernel is `kernel-6.12.0-211.16.1.el10_2`{.literal}. Older kernel versions and older minor releases are not eligible for kpatch.

Warning

Some incompatibilities exist between kernel live patching and other kernel subcomponents. The next section, *Limitations of kpatch*, documents these incompatibilities. Read it before you use kernel live patching.

### [9.1. Limitations of kpatch](#limitations-of-kpatch) {#limitations-of-kpatch .title}

Kernel live patching with `kpatch`{.literal} applies a defined class of security and bug fixes while the system runs, but you must follow rules that keep other tools from blocking patches. The list below covers `kpatch`{.literal} scope and restrictions on `SystemTap`{.literal} and `kprobe`{.literal} while a live patch is active.

-   **Intended scope**: The `kpatch`{.literal} feature can apply simple security and bug fix updates that do not require an immediate system reboot.
-   **SystemTap and kprobe**: You must not use the `SystemTap`{.literal} or `kprobe`{.literal} tool during or after loading a patch. The patch might not take effect until the probes are removed.

### [9.2. Support for third-party live patching](#support-for-third-party-live-patching) {#support-for-third-party-live-patching .title}

The `kpatch`{.literal} utility is the only kernel live patching utility supported by Red Hat with the RPM modules provided by Red Hat repositories. Red Hat does not support live patches provided by a third party.

**Additional resources**

-   [As a customer how does Red Hat support me when I use third party components?](https://access.redhat.com/articles/1067)

### [9.3. Access to kernel live patches](#access-to-kernel-live-patches) {#access-to-kernel-live-patches .title}

Red Hat delivers kernel live patching as a kernel module (`kmod`{.literal}) in an RPM package. Standard subscriptions provide access to live patches through regular channels. Without extended support, new patches for the current minor release stop when the next minor release becomes available.

For example, with a standard subscription, you can live patch the RHEL 10.2 kernel until Red Hat releases the RHEL 10.3 kernel. After that release, Red Hat no longer provides live patches for RHEL 10.2.

The components of kernel live patching are as follows:

Kernel patch module

:   -   The delivery mechanism for kernel live patches.
    -   A kernel module built specifically for the kernel being patched.
    -   The patch module contains the code of the required fixes for the kernel.
    -   Patch modules register with the `livepatch`{.literal} kernel subsystem and specify the original functions to replace, along with pointers to the replacement functions. Kernel patch modules are delivered as RPMs.
    -   The naming convention is `kpatch_<kernel version>_<kpatch version>_<kpatch release>`{.literal}. The \"kernel version\" part of the name has *dots* replaced with *underscores*.

The `kpatch`{.literal} utility
:   A command-line utility for managing patch modules.

The `kpatch`{.literal} service
:   A systemd service required by `multiuser.target`{.literal}. This target loads the kernel patch module at boot time.

The `kpatch-dnf`{.literal} package
:   A DNF plugin delivered in the form of an RPM package. This plugin manages automatic subscription to kernel live patches.

**Additional resources**

-   [Kernel Live Patch Support Cadence Update](https://access.redhat.com/articles/7057149)
-   [Kernel Live Patch life cycles](https://access.redhat.com/articles/4499631)

### [9.4. The process of live patching kernels](#the-process-of-live-patching-kernels) {#the-process-of-live-patching-kernels .title}

The `kpatch`{.literal} kernel patching solution uses the `livepatch`{.literal} kernel subsystem to redirect outdated functions to updated ones.

Applying a live kernel patch to a system triggers the following processes:

1.  The kernel patch module is copied to the `/var/lib/kpatch/`{.literal} directory and registered for re-application to the kernel by systemd on next boot.
2.  The `kpatch`{.literal} module loads into the running kernel and the new functions are registered to the `ftrace`{.literal} mechanism with a pointer to the location in memory of the new code.

When the kernel accesses the patched function, the `ftrace`{.literal} mechanism redirects it, bypassing the original functions and leading the kernel to the patched version of the function.

**Figure 9.1. How kernel live patching works**

### [9.5. Applying patches with kernel live patching in the web console](#applying-patches-with-kernel-live-patching-in-the-web-console) {#applying-patches-with-kernel-live-patching-in-the-web-console .title}

You can configure the `kpatch`{.literal} framework, which applies kernel security patches without forcing system restarts, in the RHEL web console.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click **Software Updates**.

3.  Check the status of your kernel patching settings.

    a.  If the patching is not installed, click Install.

    b.  To enable kernel patching, click Enable.

    c.  Select the checkbox for applying kernel patches.

    d.  Select whether you want to apply patches for current and future kernels or the current kernel only. If you decide to subscribe to applying patches for future kernels, the system also applies patches for the upcoming kernel releases.

    e.  Click Apply.

**Verification**

-   Check that the kernel patching is now **Enabled** in the **Settings** table of the **Software updates** section.

### [9.6. Subscribing the currently installed kernels to the live patching stream](#subscribing-the-currently-installed-kernels-to-the-live-patching-stream) {#subscribing-the-currently-installed-kernels-to-the-live-patching-stream .title}

To subscribe installed kernels to the live patching stream, install the specific kernel patch module RPMs. These packages are cumulatively updated.

The following procedure explains how to subscribe to all future cumulative live patching updates for a given kernel. Because live patches are cumulative, you cannot select which individual patches are deployed for a given kernel.

Warning

Red Hat does not support any third party live patches applied to a Red Hat supported system.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Optional: Check your kernel version:

    ``` {.language-plaintext tabindex="-1"}
    # uname -r
    ```

    ``` {.language-plaintext tabindex="-1"}
    6.12.0-211.16.1.el10_2.x86_64
    ```

2.  Search for a live patching package that corresponds to the version of your kernel:

    ``` {.language-plaintext tabindex="-1"}
    # dnf search $(uname -r)
    ```

3.  Install the live patching package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kpatch
    ```

    This command installs and applies the latest cumulative live patches for that specific kernel only.

    If the version of a live patching package is 1-1 or higher, the package will contain a patch module. In that case the kernel will be automatically patched during the installation of the live patching package.

    The kernel patch module is also installed into the `/var/lib/kpatch/`{.literal} directory to be loaded by the systemd system and service manager during the future reboots.

    Note

    An empty live patching package will be installed when there are no live patches available for a given kernel. An empty live patching package will have a *kpatch_version-kpatch_release* of 0-0, for example `kpatch-patch-6_12_0_211_16_1-0-0.el10_2.x86_64.rpm`{.literal}. The installation of the empty RPM subscribes the system to all future live patches for the given kernel.

**Verification**

-   Verify that all installed kernels have been patched:

    ``` {.language-plaintext tabindex="-1"}
    # kpatch list
    ```

    ``` {.language-plaintext tabindex="-1"}
    Loaded patch modules:
    kpatch_6_12_0_211_16_1_0_1 [enabled]

    Installed patch modules:
    kpatch_6_12_0_211_16_1_0_1 (6.12.0-211.16.1.el10_2.x86_64)
    ...
    ```

    The output shows that the kernel patch module has been loaded into the kernel that is now patched with the latest fixes from the `kpatch-patch-6_12_0_211_16_1-0-1.el10_2.x86_64.rpm`{.literal} package.

    See the `kpatch(1)`{.literal} man page on your system for more information.

    Note

    Entering the `kpatch list`{.literal} command does not return an empty live patching package. Use the `rpm -qa | grep kpatch`{.literal} command instead.

    ``` {.language-plaintext tabindex="-1"}
    # rpm -qa | grep kpatch
    ```

    \+

    ``` {.language-plaintext tabindex="-1"}
    kpatch-dnf-0.4-3.el10.noarch
    kpatch-0.9.7-2.el10.noarch
    kpatch-patch-6_12_0_211_16_1-0-1.el10_2.x86_64
    ```

### [9.7. Automatically subscribing any future kernel to the live patching stream](#automatically-subscribing-any-future-kernel-to-the-live-patching-stream) {#automatically-subscribing-any-future-kernel-to-the-live-patching-stream .title}

To subscribe to fixes delivered by the kernel patch module, also known as kernel live patches, use the `kpatch-dnf`{.literal} DNF plugin. The plugin activates **automatic** subscription for any kernel the system currently uses, and also for kernels **to-be-installed in the future**.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Optional: Check all installed kernels and the kernel you are currently running:

    ``` {.language-plaintext tabindex="-1"}
    # dnf list installed | grep kernel
    ```

    ``` {.language-plaintext tabindex="-1"}
    Updating Subscription Management repositories.
    Installed Packages
    ...
    kernel-core.x86_64            6.12.0-211.16.1.el10_2          @beaker-BaseOS
    kernel-core.x86_64            6.12.0-211.16.1.el10_2          @@commandline
    ...
    ```

    ``` {.language-plaintext tabindex="-1"}
    # uname -r
    ```

    ``` {.language-plaintext tabindex="-1"}
    6.12.0-211.16.1.el10_2.x86_64
    ```

2.  Install the `kpatch-dnf`{.literal} plugin:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kpatch-dnf
    ```

3.  Enable automatic subscription to kernel live patches:

    ``` {.language-plaintext tabindex="-1"}
    # dnf kpatch auto
    ```

    ``` {.language-plaintext tabindex="-1"}
    Updating Subscription Management repositories.
    Last metadata expiration check: 1:38:21 ago on Fri 17 Sep 2021 07:29:53 AM EDT.
    Dependencies resolved.
    ==================================================
     Package                             Architecture
    ==================================================
    Installing:
     kpatch-patch-6_12_0_211_16_1-1      x86_64
     kpatch-patch-6_12_0_211_16_1-2      x86_64

    Transaction Summary
    ===================================================
    Install  2 Packages
    ...
    ```

    This command subscribes all currently installed kernels to receiving kernel live patches. Also, it installs and applies the latest cumulative live patches, if any, for all installed kernels.

    When you update the kernel, live patches are installed automatically during the new kernel installation process.

    The kernel patch module is also installed into the `/var/lib/kpatch/`{.literal} directory that is loaded by the systemd system and service manager during future reboots.

    Note

    An empty live patching package will be installed when there are no live patches available for a given kernel. An empty live patching package will have a *kpatch_version-kpatch_release* of 0-0, for example `kpatch-patch-6_12_0_211_16_1-0-0.el10_2.x86_64.rpm`{.literal}.

    The installation of the empty RPM subscribes the system to all future live patches for the given kernel.

**Verification**

-   Verify that all installed kernels are patched:

    ``` {.language-plaintext tabindex="-1"}
    # kpatch list
    ```

    ``` {.language-plaintext tabindex="-1"}
    Loaded patch modules:
    kpatch_6_12_0_211_16_1_0_1 [enabled]

    Installed patch modules:
    kpatch_6_12_0_211_16_1_0_1 (6.12.0-211.16.1.el10_2.x86_64)
    ```

    The output shows that the kernel you are running has been patched with fixes from the `kpatch-patch-6_12_0_211_16_1-0-1.el10_2.x86_64.rpm`{.literal} package.

    Note

    Entering the `kpatch list`{.literal} command does not return an empty live patching package. Use the `rpm -qa | grep kpatch`{.literal} command instead.

    ``` {.language-plaintext tabindex="-1"}
    # rpm -qa | grep kpatch
    ```

    \+

    ``` {.language-plaintext tabindex="-1"}
    kpatch-dnf-0.9.7_0.4-4.el10.noarch
    kpatch-0.9.7-4.el10.noarch
    kpatch-patch-6_12_0_211_16_1-0-1.el10_2.x86_64
    ```

### [9.8. Disabling automatic subscription to the live patching stream](#disabling-automatic-subscription-to-the-live-patching-stream) {#disabling-automatic-subscription-to-the-live-patching-stream .title}

To disable the automatic installation of `kpatch-patch`{.literal} packages, you can turn off the automatic subscription feature after subscribing to kernel patch module fixes.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Optional: Check all installed kernels and the kernel you are currently running:

    ``` {.language-plaintext tabindex="-1"}
    # dnf list installed | grep kernel
    ```

    ``` {.language-plaintext tabindex="-1"}
    Updating Subscription Management repositories.
    Installed Packages
    ...
    kernel-core.x86_64            6.12.0-0.el10              @beaker-BaseOS
    kernel-core.x86_64            6.12.0-0.el10              @@commandline
    ...
    ```

    ``` {.language-plaintext tabindex="-1"}
    # uname -r
    ```

    ``` {.language-plaintext tabindex="-1"}
    6.12.0-0.el10_0.x86_64
    ```

2.  Disable automatic subscription to kernel live patches:

    ``` {.language-plaintext tabindex="-1"}
    # dnf kpatch manual
    ```

    ``` {.language-plaintext tabindex="-1"}
    Updating Subscription Management repositories.
    ```

    See `kpatch(1)`{.literal} and `dnf-kpatch(8)`{.literal} manual pages for more information.

**Verification**

-   You can check for the successful outcome:

    ``` {.language-plaintext tabindex="-1"}
    # yum kpatch status
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    Updating Subscription Management repositories.
    Last metadata expiration check: 0:30:41 ago on Tue Jun 14 15:59:26 2022.
    Kpatch update setting: *manual*
    ```

### [9.9. Updating kernel patch modules](#updating-kernel-patch-modules) {#updating-kernel-patch-modules .title}

To update kernel patch modules, use the standard RPM update process. Red Hat delivers these modules as cumulative RPM packages.

**Prerequisites**

-   The system is subscribed to the live patching stream, as described in [Subscribing the currently installed kernels to the live patching stream](#subscribing-the-currently-installed-kernels-to-the-live-patching-stream "9.6. Subscribing the currently installed kernels to the live patching stream").

**Procedure**

-   Update to a new cumulative version for the current kernel:

    ``` {.language-plaintext tabindex="-1"}
    # dnf update kpatch
    ```

    This command automatically installs and applies any updates that are available for the currently running kernel. Including any future released cumulative live patches.

-   Alternatively, update all installed kernel patch modules:

    ``` {.language-plaintext tabindex="-1"}
    # dnf update kpatch
    ```

    Note

    When the system reboots into the same kernel, the kernel is automatically live patched again by the `kpatch.service`{.literal} systemd service.

**Additional resources**

-   [Updating software packages](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/updating-rhel-content#updating-packages)

### [9.10. CVE reporting for kernel live patches](#cve-reporting-for-kernel-live-patches) {#cve-reporting-for-kernel-live-patches .title}

The `kpatch list`{.literal} command reports Common Vulnerabilities and Exposures (CVE) identifiers from `kpatch-patch`{.literal} RPM changelogs for loaded kernel live patch modules.

Starting in `kpatch`{.literal} version 0.9.10 on Red Hat Enterprise Linux 10.2, the `kpatch list`{.literal} command lists CVE identifiers under each loaded patch module. The identifiers come from the full changelog of the `kpatch-patch`{.literal} RPM that provides the module.

Use this output to confirm which security fixes are active on the running kernel before the on-disk `kernel`{.literal} package is updated. The kernel version from `uname -r`{.literal} does not change when you apply a live patch. External vulnerability scanners might still report the base kernel as vulnerable until you reboot into an updated kernel package or adjust scanner configuration.

Live patching does not address all critical or important CVEs.

**Additional resources**

-   [Limitations of kpatch](#limitations-of-kpatch "9.1. Limitations of kpatch")
-   [Red Hat CVE database](https://access.redhat.com/security/security-updates/cve)
-   [Is live kernel patch (kpatch) supported in Red Hat Enterprise Linux?](https://access.redhat.com/solutions/2206511)

### [9.11. Identifying CVEs patched by kernel live patches](#identifying-cves-patched-by-kernel-live-patches) {#identifying-cves-patched-by-kernel-live-patches .title}

To display Common Vulnerabilities and Exposures (CVE) identifiers for active fixes, run `kpatch list`{.literal} on a loaded kernel live patch.

**Prerequisites**

-   You have root permissions on the system.
-   The `kpatch`{.literal} package version 0.9.10 or later is installed.
-   A loaded `kpatch-patch`{.literal} package with version 1-1 or higher is installed on a kpatch-supported kernel on Red Hat Enterprise Linux 10.2 or later, as described in [Subscribing the currently installed kernels to the live patching stream](#subscribing-the-currently-installed-kernels-to-the-live-patching-stream "9.6. Subscribing the currently installed kernels to the live patching stream").

**Procedure**

1.  List loaded kernel live patch modules and the CVE identifiers they address:

    ``` {.language-plaintext tabindex="-1"}
    # kpatch list
    ```

2.  Review the command output and confirm that a loaded patch module appears in the enabled state with CVE identifiers indented underneath:

    ``` {.language-plaintext tabindex="-1"}
    Loaded patch modules:
    kpatch_6_12_0_211_16_1_0_1 [enabled]
        CVE-2026-46243
        CVE-2026-46331

    Installed patch modules:
    kpatch_6_12_0_211_16_1_0_1 (6.12.0-211.16.1.el10_2.x86_64)
    ```

### [9.12. Removing the live patching package](#removing-the-live-patching-package) {#removing-the-live-patching-package .title}

To disable the kernel live patching solution, remove the live patching package.

**Prerequisites**

-   You have root permissions on the system.
-   The live patching package is installed.

**Procedure**

1.  Select the live patching package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf list installed | grep kpatch-patch
    ```

    ``` {.language-plaintext tabindex="-1"}
    kpatch-patch-6.12.0-0.el10_0.x86_64        0-0.el10        @@commandline
    ...
    ```

    The example output lists live patching packages that you installed.

2.  Remove the live patching package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf remove kpatch-patch-6.12.0-0.el10_0.x86_64
    ```

    When a live patching package is removed, the kernel remains patched until the next reboot, but the kernel patch module is removed from disk. On future reboot, the corresponding kernel will no longer be patched.

3.  Reboot your system.

4.  Verify the live patching package is removed:

    ``` {.language-plaintext tabindex="-1"}
    # dnf list installed | grep kpatch-patch
    ```

    The command displays no output if the package has been successfully removed.

**Verification**

1.  Verify the kernel live patching solution is disabled:

    ``` {.language-plaintext tabindex="-1"}
    # kpatch list
    ```

    ``` {.language-plaintext tabindex="-1"}
    Loaded patch modules:
    ```

    The example output shows that the kernel is not patched and the live patching solution is not active because there are no patch modules that are currently loaded.

Important

Currently, Red Hat does not support reverting live patches without rebooting your system. In case of any issues, contact our support team.

**Additional resources**

-   [Removing installed packages](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/removing-rhel-content#removing-installed-packages)

### [9.13. Uninstalling the kernel patch module](#uninstalling-the-kernel-patch-module) {#uninstalling-the-kernel-patch-module .title}

To prevent the kernel live patching solution from applying a kernel patch module on subsequent boots, uninstall it.

**Prerequisites**

-   You have root permissions on the system.
-   A live patching package is installed.
-   A kernel patch module is installed and loaded.

**Procedure**

1.  Select a kernel patch module:

    ``` {.language-plaintext tabindex="-1"}
    # kpatch list
    ```

    ``` {.language-plaintext tabindex="-1"}
    Loaded patch modules:
    kpatch_6_12_0_1_0_1 [enabled]

    Installed patch modules:
    kpatch_6_12_0_1_0_1 (6.12.0.el10_0.x86_64)
    ...
    ```

2.  Uninstall the selected kernel patch module.

    ``` {.language-plaintext tabindex="-1"}
    # kpatch uninstall kpatch_6_12_0_1_0_1
    ```

    ``` {.language-plaintext tabindex="-1"}
    uninstalling kpatch_6_12_0_1_0_1 (6.12.0.el10_0.x86_64)
    ```

    -   Note that the uninstalled kernel patch module is still loaded:

        ``` {.language-plaintext tabindex="-1"}
        # kpatch list
        ```

        ``` {.language-plaintext tabindex="-1"}
        Loaded patch modules:
        kpatch_6_12_0_1_0_1 [enabled]

        Installed patch modules:
        kpatch_6_12_0_1_0_1 (6.12.0.el10_0.x86_64)
        ```

        When the selected module is uninstalled, the kernel remains patched until the next reboot, but the kernel patch module is removed from disk.

3.  Reboot your system.

**Verification**

1.  Verify that the kernel patch module is uninstalled:

    ``` {.language-plaintext tabindex="-1"}
    # kpatch list
    ```

    ``` {.language-plaintext tabindex="-1"}
    Loaded patch modules:
    ...
    ```

    This example output shows no loaded or installed kernel patch modules, therefore the kernel is not patched and the kernel live patching solution is not active.

### [9.14. Disabling kpatch.service](#disabling-kpatch-service) {#disabling-kpatch.service .title}

To prevent the kernel live patching solution from applying all kernel patch modules globally on subsequent boots, disable the `kpatch`{.literal} service.

**Prerequisites**

-   You have root permissions on the system.
-   A live patching package is installed.
-   A kernel patch module is installed and loaded.

**Procedure**

1.  Verify `kpatch.service`{.literal} is enabled.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl is-enabled kpatch.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    enabled
    ```

2.  Disable `kpatch.service`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl disable kpatch.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    Removed /etc/systemd/system/multi-user.target.wants/kpatch.service.
    ```

    -   Note that the applied kernel patch module is still loaded:

        ``` {.language-plaintext tabindex="-1"}
        # kpatch list
        ```

        ``` {.language-plaintext tabindex="-1"}
        Loaded patch modules:
        kpatch_6_12_0_1_0_1 [enabled]

        Installed patch modules:
        kpatch_6_12_0_1_0_1 (6.12.0.el10_0.x86_64)
        ```

3.  Reboot your system.

4.  Optional: Verify the status of `kpatch.service`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status kpatch.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    ● kpatch.service - "Apply kpatch kernel patches"
       Loaded: loaded (/usr/lib/systemd/system/kpatch.service; disabled; vendor preset: disabled)
       Active: inactive (dead)
    ```

    The example output testifies that `kpatch.service`{.literal} is disabled. Thereby, the kernel live patching solution is not active.

5.  Verify that the kernel patch module has been unloaded.

    ``` {.language-plaintext tabindex="-1"}
    # kpatch list
    ```

    ``` {.language-plaintext tabindex="-1"}
    Loaded patch modules:

    Installed patch modules:
    kpatch_6_12_0_1_0_1 (6.12.0.el10_0.x86_64)
    ```

    The example output shows that a kernel patch module is still installed but the kernel is not patched.

    Important

    Currently, Red Hat does not support reverting live patches without rebooting your system. In case of any issues, contact our support team.

**Additional resources**

-   [Using systemd unit files to customize and optimize your system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/index)

## [Chapter 10. Keeping kernel panic parameters disabled in virtualized environments](#keeping-kernel-panic-parameters-disabled-in-virtualized-environments) {#chapter-10.-keeping-kernel-panic-parameters-disabled-in-virtualized-environments .title}

Do not enable the `softlockup_panic`{.literal} and `nmi_watchdog`{.literal} kernel parameters when configuring virtual machines in Red Hat Enterprise Linux 10. These parameters can cause spurious soft lockups that result in a kernel panic.

The reasons behind this advice are as follows.

### [10.1. What is a soft lockup](#what-is-a-soft-lockup) {#what-is-a-soft-lockup .title}

A soft lockup usually indicates a bug. The affected task runs in kernel space on one CPU without rescheduling. The task also does not allow any other task to run on that particular CPU.

As a result, a warning is displayed to a user through the system console. This problem is also referred to as the soft lockup firing.

**Additional resources**

-   [What is a CPU soft lockup?](https://access.redhat.com/articles/371803)

### [10.2. Parameters controlling kernel panic](#parameters-controlling-kernel-panic) {#parameters-controlling-kernel-panic .title}

Control system behavior during soft lockups by configuring certain kernel parameters. You can enable detection mechanisms, adjust thresholds, and determine if the kernel panics to manage system stability.

`softlockup_panic`{.literal}

:   Controls whether the kernel panics when a soft lockup is detected.

    +-------------------+---------+----------------------------------------+
    | Type              | Value   | Effect                                 |
    +:==================+:========+:=======================================+
    | Integer           | 0       | kernel does not panic on soft lockup   |
    +-------------------+---------+----------------------------------------+
    | Integer           | 1       | kernel panics on soft lockup           |
    +-------------------+---------+----------------------------------------+

    : Table 10.1. Valid values for softlockup_panic

    Show more

    By default, on RHEL 10, this value is 0.

    The system needs to detect a hard lockup first to be able to panic. The detection is controlled by the `nmi_watchdog`{.literal} parameter.

`nmi_watchdog`{.literal}

:   Controls whether lockup detection mechanisms (`watchdogs`{.literal}) are active or not. This parameter is of integer type.

    +-----------------------------------+-----------------------------------+
    | Value                             | Effect                            |
    +:==================================+:==================================+
    | 0                                 | disables lockup detector          |
    +-----------------------------------+-----------------------------------+
    | 1                                 | enables lockup detector           |
    +-----------------------------------+-----------------------------------+

    : Table 10.2. Valid values for nmi_watchdog

    Show more

    The hard lockup detector monitors each CPU for its ability to respond to interrupts.

`watchdog_thresh`{.literal}

:   Controls frequency of watchdog `hrtimer`{.literal}, NMI events, and soft or hard lockup thresholds.

    +-----------------------------------+-----------------------------------+
    | Default threshold                 | Soft lockup threshold             |
    +:==================================+:==================================+
    | 10 seconds                        | 2 \* `watchdog_thresh`{.literal}  |
    +-----------------------------------+-----------------------------------+

    : Table 10.3. Relationship between default threshold and soft lockup threshold for watchdog_thresh

    Show more

    Setting this parameter to zero disables lockup detection altogether.

**Additional resources**

-   [Softlockup detector and hardlockup detector](https://www.kernel.org/doc/Documentation/lockup-watchdogs.txt)
-   [Kernel sysctl](https://www.kernel.org/doc/Documentation/sysctl/kernel.txt)

### [10.3. Spurious soft lockups in virtualized environments](#spurious-soft-lockups-in-virtualized-environments) {#spurious-soft-lockups-in-virtualized-environments .title}

The soft lockup firing on physical hosts usually represents a kernel or a hardware bug. The same phenomenon happening on guest operating systems in virtualized environments might represent a false warning.

Heavy workload on a host or high contention over some specific resource, such as memory, can cause a spurious soft lockup firing because the host might schedule out the guest CPU for a period longer than 20 seconds. When the guest CPU is again scheduled to run on the host, it experiences a *time jump* that triggers the due timers. The timers also include the `hrtimer`{.literal} watchdog that can report a soft lockup on the guest CPU.

Soft lockup in a virtualized environment can be false. You must not enable the kernel parameters that trigger a system panic when a soft lockup reports to a guest CPU.

Important

To understand soft lockups in guests, it is essential to know that the host schedules the guest as a task, and the guest then schedules its own tasks.

**Additional resources**

-   [Virtual machine components and their interaction](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_windows_virtual_machines/basic-concepts-of-virtualization-in-rhel#rhel-virtual-machine-components-and-their-interaction)
-   [What is a soft lockup](#what-is-a-soft-lockup "10.1. What is a soft lockup")

## [Chapter 11. Adjusting kernel parameters for database servers](#adjusting-kernel-parameters-for-database-servers) {#chapter-11.-adjusting-kernel-parameters-for-database-servers .title}

Configure the required kernel parameters to ensure efficient operation of database servers and databases.

### [11.1. Introduction to database servers](#introduction-to-database-servers) {#introduction-to-database-servers .title}

A database server is a service that provides features of a database management system (DBMS). DBMS provides utilities for database administration and interacts with end users, applications, and databases.

Red Hat Enterprise Linux 10 provides the following database management systems:

-   **MariaDB 10.11**
-   **MySQL 8.4**
-   **PostgreSQL 16**
-   **Valkey 7.2**

### [11.2. Parameters affecting performance of database applications](#parameters-affecting-performance-of-database-applications) {#parameters-affecting-performance-of-database-applications .title}

Review the kernel parameters that affect database application performance, such as `fs.aio-max-nr`{.literal}, `fs.file-max`{.literal}, `kernel.shmall`{.literal} and others. Adjusting these settings helps you manage asynchronous I/O, file handles, and shared memory for optimal database efficiency.

`fs.aio-max-nr`{.literal}

:   Defines the maximum number of asynchronous I/O operations the system can handle on the server.

    Note

    Raising the `fs.aio-max-nr`{.literal} parameter produces no additional changes beyond increasing the aio limit.

`fs.file-max`{.literal}

:   Defines the maximum number of file handles (temporary file names or IDs assigned to open files) the system supports at any instance.

    The kernel dynamically allocates file handles whenever a file handle is requested by an application. However, the kernel does not free these file handles when they are released by the application. It recycles these file handles instead. The total number of allocated file handles will increase over time even though the number of currently used file handles might be low.

`kernel.shmall`{.literal}
:   Defines the total number of shared memory pages that can be used system-wide. To use the entire main memory, the value of the `kernel.shmall`{.literal} parameter should be ≤ total main memory size.

`kernel.shmmax`{.literal}
:   Defines the maximum size in bytes of a single shared memory segment that a Linux process can allocate in its virtual address space.

`kernel.shmmni`{.literal}
:   Defines the maximum number of shared memory segments the database server is able to handle.

`net.ipv4.ip_local_port_range`{.literal}
:   The system uses this port range for programs that connect to a database server without specifying a port number.

`net.core.rmem_default`{.literal}
:   Defines the default receive socket memory through Transmission Control Protocol (TCP).

`net.core.rmem_max`{.literal}
:   Defines the maximum receive socket memory through Transmission Control Protocol (TCP).

`net.core.wmem_default`{.literal}
:   Defines the default send socket memory through Transmission Control Protocol (TCP).

`net.core.wmem_max`{.literal}
:   Defines the maximum send socket memory through Transmission Control Protocol (TCP).

`vm.dirty_bytes`{.literal} / `vm.dirty_ratio`{.literal}
:   Defines a threshold in bytes / in percentage of dirty-able memory at which a process generating dirty data is started in the `write()`{.literal} function.

Note

**Either** `vm.dirty_bytes`{.literal} **or** `vm.dirty_ratio`{.literal} can be specified at a time.

`vm.dirty_background_bytes`{.literal} / `vm.dirty_background_ratio`{.literal}
:   Defines a threshold in bytes / in percentage of dirty-able memory at which the kernel tries to actively write dirty data to hard-disk.

Note

**Either** `vm.dirty_background_bytes`{.literal} **or** `vm.dirty_background_ratio`{.literal} can be specified at a time.

`vm.dirty_writeback_centisecs`{.literal}

:   Defines a time interval between periodic wake-ups of the kernel threads responsible for writing dirty data to hard-disk.

    This kernel parameters measures in 100th's of a second.

`vm.dirty_expire_centisecs`{.literal}

:   Defines the time of dirty data that becomes old to be written to hard-disk.

    This kernel parameters measures in 100th's of a second.

**Additional resources**

-   [Dirty pagecache writeback and vm.dirty parameters](https://access.redhat.com/articles/45002#control-parameters-4)

## [Chapter 12. Configuring huge pages](#configuring-huge-pages) {#chapter-12.-configuring-huge-pages .title}

The system manages physical memory in fixed-size pages. The default 4KiB page size on x86_64 is suitable for general workloads, but applications with large data sets benefit from huge pages. Configure huge pages in Red Hat Enterprise Linux 10 to improve performance and reduce resource usage.

### [12.1. Available huge page features](#available-huge-page-features) {#available-huge-page-features .title}

With Red Hat Enterprise Linux, you can use huge pages for applications that work with big data sets, and improve the performance of such applications.

The following are the huge page methods, which are supported in RHEL:

`HugeTLB pages`{.literal}

:   HugeTLB pages are also called static huge pages. There are two ways of reserving HugeTLB pages:

    -   `At boot time`{.literal}: It increases the possibility of success because the memory has not yet been significantly fragmented. However, on NUMA machines, the number of pages is automatically split among the NUMA nodes.
    -   `At runtime`{.literal}: It allows you to reserve the huge pages per NUMA node. If the runtime reservation is done as early as possible in the boot process, the probability of memory fragmentation is lower.

`Transparent HugePages (THP)`{.literal}

:   With THP, the kernel automatically assigns huge pages to processes, and therefore there is no need to manually reserve the static huge pages. The following are the two modes of operation in THP:

    -   `system-wide`{.literal}: Here, the kernel tries to assign huge pages to a process whenever it is possible to allocate the huge pages and the process is using a large contiguous virtual memory area.

    -   `per-process`{.literal}: Here, the kernel only assigns huge pages to the memory areas of individual processes which you can specify using the `madvise`{.literal}() system call.

        Note

        The THP feature only supports `2 MB`{.literal} pages.

**Additional resources**

-   [Parameters for reserving HugeTLB pages at boot time](#parameters-for-reserving-hugetlb-pages-at-boot-time "12.2. Parameters for reserving HugeTLB pages at boot time")
-   [Configuring HugeTLB at boot time](#configuring-hugetlb-at-boot-time "12.3. Configuring HugeTLB at boot time")
-   [Parameters for reserving HugeTLB pages at run time](#parameters-for-reserving-hugetlb-pages-at-run-time "12.4. Parameters for reserving HugeTLB pages at run time")
-   [Configuring HugeTLB at run time](#configuring-hugetlb-at-run-time "12.5. Configuring HugeTLB at run time")
-   [Managing transparent hugepages](#managing-transparent-hugepages "12.6. Managing transparent huge pages")

### [12.2. Parameters for reserving HugeTLB pages at boot time](#parameters-for-reserving-hugetlb-pages-at-boot-time) {#parameters-for-reserving-hugetlb-pages-at-boot-time .title}

Influence HugeTLB page behavior at boot time by using certain kernel parameters.

For more information about how to use these parameters to configure HugeTLB pages at boot time, see [Configuring HugeTLB at boot time](#configuring-hugetlb-at-boot-time "12.3. Configuring HugeTLB at boot time").

+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Parameter                      | Description                                                                                                                                                                               | Default value                                                                                                       |
+:===============================+:==========================================================================================================================================================================================+:====================================================================================================================+
| `hugepages`{.literal}          | Defines the number of persistent huge pages configured in the kernel at boot time.                                                                                                        | The default value is `0`{.literal}.                                                                                 |
|                                |                                                                                                                                                                                           |                                                                                                                     |
|                                | In a NUMA system, huge pages, that have this parameter defined, are divided equally between nodes.                                                                                        | To update this value at boot, change the value of this parameter in the `/proc/sys/vm/nr_hugepages`{.literal} file. |
|                                |                                                                                                                                                                                           |                                                                                                                     |
|                                | You can assign huge pages to specific nodes at runtime by changing the value of the nodes in the `/sys/devices/system/node/node_id/hugepages/hugepages-size/nr_hugepages`{.literal} file. |                                                                                                                     |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| `hugepagesz`{.literal}         | Defines the size of persistent huge pages configured in the kernel at boot time.                                                                                                          | Valid values are `2 MB`{.literal} and `1 GB`{.literal}. The default value is `2 MB`{.literal}.                      |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| `default_hugepagesz`{.literal} | Defines the default size of persistent huge pages configured in the kernel at boot time.                                                                                                  | Valid values are `2 MB`{.literal} and `1 GB`{.literal}. The default value is `2 MB`{.literal}.                      |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

: Table 12.1. Parameters used to configure HugeTLB pages at boot time

Show more

### [12.3. Configuring HugeTLB at boot time](#configuring-hugetlb-at-boot-time) {#configuring-hugetlb-at-boot-time .title}

With the Huge Translation Lookaside Buffer (HugeTLB), you can use huge pages by reserving them at boot time. You can minimize the memory fragmentation to ensure that sufficient resources are available for workloads that can benefit from larger memory pages.

#### [12.3.1. Configuring HugeTLB by using kernel command line parameters](#configuring-hugetlb-by-using-kernel-command-line-parameters) {#configuring-hugetlb-by-using-kernel-command-line-parameters .title}

To reserve Huge Translation Lookaside Buffer (HugeTLB) pages at the earliest boot stage, you can use kernel command-line parameters. This method ensures the highest chance of successfully reserving the required number and size of huge pages, as memory is allocated during the kernel boot.

Prefer reserving HugeTLB pages by using kernel boot parameters, as this method ensures allocation of larger contiguous memory regions compared to using a systemd unit.

Note

The examples in the procedure demonstrate how to use the command-line options for configuring HugeTLB pages. These examples do not necessarily apply to your system configuration. Review your system requirements and objectives before applying these settings in your environment.

**Prerequisites**

-   You must have root privileges on your system.

**Procedure**

-   Update the kernel command line to include HugeLTB options.

    -   To reserve HugeTLB pages of the default size for your architecture, enter:

        ``` {.language-plaintext tabindex="-1"}
        # grubby --update-kernel=ALL --args="hugepages=10"
        ```

        This command reserves 10 HugeTLB pages of the default pool size. For example, on `x86_64`{.literal}, the default pool size is `2 MB`{.literal}. On systems with Non-Uniform Memory Access (NUMA), the allocation is distributed evenly across NUMA nodes. If the system has two NUMA nodes, each node reserves five pages.

    -   To reserve different sizes of HugeTLB pages, specify the `hugepagesz`{.literal} and `hugepages`{.literal} options in the kernel command line, enter:

        ``` {.language-plaintext tabindex="-1"}
        # grubby --update-kernel=ALL --args="hugepagesz=2M hugepages=10 hugepagesz=1G hugepages=1"
        ```

        This command reserves 10 pages of `2 MB`{.literal} each and 1 page of `1 GB`{.literal}.

        The system reserves the specified number and size of HugeTLB pages at boot time, ensuring that memory is allocated before the operating system begins normal operation.

        Important

        The order of the options is significant. Each `hugepagesz=`{.literal} option must be immediately followed by its corresponding `hugepages=`{.literal} option.

#### [12.3.2. Configuring HugeTLB by using systemd service unit](#configuring-hugetlb-by-using-systemd-service-unit) {#configuring-hugetlb-by-using-systemd-service-unit .title}

To configure Huge Translation Lookaside Buffer (HugeTLB) pages during user-space booting, use a systemd service unit. This reserves memory after kernel initialization but before most services start, ensuring applications have access to the required pages.

**Prerequisites**

-   You must have root privileges on your system.

**Procedure**

1.  Create a new file called `hugetlb-gigantic-pages.service`{.literal} in the `/usr/lib/systemd/system/`{.literal} directory and add the following content:

    ``` {.language-bash tabindex="-1"}
    [Unit]
    Description=HugeTLB Gigantic Pages Reservation
    DefaultDependencies=no
    Before=dev-hugepages.mount
    ConditionPathExists=/sys/devices/system/node
    ConditionKernelCommandLine=hugepagesz=1G

    [Service]
    Type=oneshot
    RemainAfterExit=yes
    ExecStart=/usr/lib/systemd/hugetlb-reserve-pages.sh

    [Install]
    WantedBy=sysinit.target
    ```

2.  Create a new file called `hugetlb-reserve-pages.sh`{.literal} in the `/usr/lib/systemd/`{.literal} directory and add the following content:

    ``` {.language-bash tabindex="-1"}
    #!/bin/sh

    nodes_path=/sys/devices/system/node/
    if [ ! -d $nodes_path ]; then
        echo "ERROR: $nodes_path does not exist"
        exit 1
    fi

    reserve_pages()
    {
        echo $1 > $nodes_path/$2/hugepages/hugepages-1048576kB/nr_hugepages
    }

    reserve_pages <number_of_pages> <node>
    ```

    Replace *`<number_of_pages>`{.literal}* with the number of 1GB pages you want to reserve, and *`<node>`{.literal}* with the node name on which to reserve these pages. For example, to reserve two 1 GB pages on `node0`{.literal} and one 1GB page on `node1`{.literal}, replace *`<number_of_pages>`{.literal}* with `2`{.literal} for `node0`{.literal} and `1`{.literal} for `node1`{.literal}.

3.  Create an executable script:

    ``` {.language-plaintext tabindex="-1"}
    # chmod +x /usr/lib/systemd/hugetlb-reserve-pages.sh
    ```

4.  Enable early boot reservation:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable hugetlb-gigantic-pages.service
    ```

    Note

    -   You can try reserving more 1 GB pages at runtime by writing to the `nr_hugepages`{.literal} attribute at any time. However, to prevent failures due to memory fragmentation, reserve 1 GB pages early during the boot process.
    -   Reserving static huge pages can effectively reduce the amount of memory available to the system, and prevent it from using its full memory capacity. Although a properly sized pool of reserved huge pages can be beneficial to applications that use it, an oversized or unused pool of reserved huge pages will eventually be detrimental to the overall system performance. When setting a reserved huge page pool, ensure that the system can properly use its full memory capacity.

### [12.4. Parameters for reserving HugeTLB pages at run time](#parameters-for-reserving-hugetlb-pages-at-run-time) {#parameters-for-reserving-hugetlb-pages-at-run-time .title}

Influence HugeTLB page behavior at run time by using certain kernel parameters.

For more information about how to use these parameters to configure HugeTLB pages at run time, see [Configuring HugeTLB at run time](#configuring-hugetlb-at-run-time "12.5. Configuring HugeTLB at run time").

+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| Parameter                           | Description                                                                                                                                                                                                                                                                                          | File name                                                                          |
+:====================================+:=====================================================================================================================================================================================================================================================================================================+:===================================================================================+
| `nr_hugepages`{.literal}            | Defines the number of huge pages of a specified size assigned to a specified NUMA node.                                                                                                                                                                                                              | `/sys/devices/system/node/node_id/hugepages/hugepages-size/nr_hugepages`{.literal} |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| `nr_overcommit_hugepages`{.literal} | Defines the maximum number of additional huge pages that can be created and used by the system through overcommitting memory.                                                                                                                                                                        | `/proc/sys/vm/nr_overcommit_hugepages`{.literal}                                   |
|                                     |                                                                                                                                                                                                                                                                                                      |                                                                                    |
|                                     | Writing any nonzero value into this file indicates that the system obtains that number of huge pages from the kernel's normal page pool if the persistent huge page pool is exhausted. As these surplus huge pages become unused, they are then freed and returned to the kernel's normal page pool. |                                                                                    |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

: Table 12.2. Parameters used to configure HugeTLB pages at run time

Show more

### [12.5. Configuring HugeTLB at run time](#configuring-hugetlb-at-run-time) {#configuring-hugetlb-at-run-time .title}

Configure HugeTLB pages at runtime to improve memory performance for applications that require large memory allocations. Reserve huge pages on specific NUMA nodes with specified sizes.

**Procedure**

1.  Display the memory statistics:

    ``` {.language-plaintext tabindex="-1"}
    # numastat -cm | egrep 'Node|Huge'
    ```

    ``` {.language-plaintext tabindex="-1"}
                     Node 0 Node 1 Node 2 Node 3  Total add
    AnonHugePages         0      2      0      8     10
    HugePages_Total       0      0      0      0      0
    HugePages_Free        0      0      0      0      0
    HugePages_Surp        0      0      0      0      0
    ```

2.  Add the number of huge pages of a specified size to the node:

    ``` {.language-plaintext tabindex="-1"}
    # echo 20 > /sys/devices/system/node/node2/hugepages/hugepages-2048kB/nr_hugepages
    ```

    Replace the following values:

    -   *20* with the number of huge pages you want to reserve

    -   *2048* with the size of the huge pages in KiB

    -   *node2* with the NUMA node on which you want to reserve the pages

        Note

        The directory name format in the path is `hugepages-`{.literal}*`size_KiB`{.literal}* where *size* is specified in KiB. The actual directory name might appear as `hugepages-2048KiB`{.literal} or `hugepages-2048kB`{.literal} depending on your system.

**Verification**

-   Ensure that the number of huge pages are added:

    ``` {.language-plaintext tabindex="-1"}
    # numastat -cm | egrep 'Node|Huge'
    ```

    ``` {.language-plaintext tabindex="-1"}
                     Node 0 Node 1 Node 2 Node 3  Total
    AnonHugePages         0      2      0      8     10
    HugePages_Total       0      0     40      0     40
    HugePages_Free        0      0     40      0     40
    HugePages_Surp        0      0      0      0      0
    ```

    See `numastat(8)`{.literal} man page for more information.

### [12.6. Managing transparent huge pages](#managing-transparent-hugepages) {#managing-transparent-huge-pages .title}

Red Hat Enterprise Linux 10 enables transparent huge pages (THP) by default. However, you can enable, disable, or set the transparent huge pages to `madvise`{.literal} with runtime configuration, TuneD profiles, kernel command line parameters, or systemd unit file.

#### [12.6.1. Managing transparent huge pages with runtime configuration](#managing-transparent-hugepages-with-runtime-configuration) {#managing-transparent-huge-pages-with-runtime-configuration .title}

To optimize memory usage, manage transparent huge pages (THP) at runtime. Note that runtime configuration does not persist across reboots.

**Procedure**

1.  Check the status of THP:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /sys/kernel/mm/transparent_hugepage/enabled
    ```

2.  Configure THP.

    -   Enabling THP:

        ``` {.language-plaintext tabindex="-1"}
        $ echo always > /sys/kernel/mm/transparent_hugepage/enabled
        ```

    -   Disabling THP:

        ``` {.language-plaintext tabindex="-1"}
        $ echo never > /sys/kernel/mm/transparent_hugepage/enabled
        ```

    -   Setting THP to `madvise`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        $ echo madvise > /sys/kernel/mm/transparent_hugepage/enabled
        ```

        To prevent applications from allocating more memory resources than necessary, disable the system-wide transparent huge pages and only enable them for the applications that explicitly request it through the `madvise`{.literal} system call.

        Note

        Sometimes, providing low latency to short-lived allocations has higher priority than immediately achieving the best performance with long-lived allocations. In such cases, you can disable direct compaction while leaving THP enabled.

        Direct compaction is a synchronous memory compaction during the huge page allocation. Disabling direct compaction provides no guarantee of saving memory, but can decrease the risk of higher latencies during frequent page faults. Also, disabling direct compaction allows synchronous compaction of Virtual Memory Areas (VMAs) highlighted in `madvise`{.literal} only. Note that if the workload benefits significantly from THP, the performance decreases. Disable direct compaction:

        \$ echo never \> /sys/kernel/mm/transparent_hugepage/defrag

        See the `madvise(2)`{.literal} man page on your system for more information.

#### [12.6.2. Managing transparent huge pages with TuneD profiles](#managing-transparent-hugepages-with-tuned-profiles) {#managing-transparent-huge-pages-with-tuned-profiles .title}

To manage transparent huge pages (THP) persistently, use TuneD profiles. Configure these profiles in the `tuned.conf`{.literal} file.

**Prerequisites**

-   `TuneD`{.literal} package is installed.
-   `TuneD`{.literal} service is enabled.

**Procedure**

1.  Copy the active profile to the `/etc/tuned/profiles/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo cp -R /usr/lib/tuned/profiles/<profile> /etc/tuned/profiles/<new_profile>
    ```

2.  Edit the `/etc/tuned/profiles/`{.literal}*`<new_profile>`{.literal}*`/tuned.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo vi /etc/tuned/profiles/<new_profile>/tuned.conf
    ```

    -   To enable THP, add the line:

        ``` {.language-plaintext tabindex="-1"}
        [bootloader]

        cmdline = transparent_hugepage=always
        ```

    -   To disable THP, add the line:

        ``` {.language-plaintext tabindex="-1"}
        [bootloader]

        cmdline = transparent_hugepage=never
        ```

    -   To set THP to `madvise`{.literal}, add the line:

        ``` {.language-plaintext tabindex="-1"}
        [bootloader]

        cmdline = transparent_hugepage=madvise
        ```

3.  Restart the `TuneD`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl restart tuned
    ```

4.  Set the new profile active:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo tuned-adm profile <new_profile>
    ```

**Verification**

1.  Verify that the new profile is active:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo tuned-adm active
    ```

2.  Verify that the required mode of THP is set:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /sys/kernel/mm/transparent_hugepage/enabled
    ```

#### [12.6.3. Managing transparent huge pages with kernel command line parameters](#managing-transparent-hugepages-with-kernel-command-line-parameters) {#managing-transparent-huge-pages-with-kernel-command-line-parameters .title}

To manage transparent huge pages (THP) at boot time, modify the kernel parameters. This configuration persists across reboots.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Get the current kernel command line parameters:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --info=$(grubby --default-kernel)
    ```

    ``` {.language-plaintext tabindex="-1"}
    kernel="/boot/vmlinuz-6.12.X-XXX.XX.X.el10_0.x86_64"
    args="ro crashkernel=1G-4G:192M,4G-64G:256M,64G-:512M resume=UUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXXX console=tty0 console=ttyS0"
    root="UUID=XXXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
    initrd="/boot/initramfs-6.12.X-XXX.XX.X.el10_0.x86_64.img"
    title="Red Hat Enterprise Linux (6.12.X-XXX.XX.X.el10_0.x86_64) 10.0"
    id="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-6.12.X-XXX.XX.X.el10_0.x86_64"
    ```

2.  Configure THP by adding kernel parameters.

    -   To enable THP:

        ``` {.language-plaintext tabindex="-1"}
        # grubby --args="transparent_hugepage=always" --update-kernel=DEFAULT
        ```

    -   To disable THP:

        ``` {.language-plaintext tabindex="-1"}
        # grubby --args="transparent_hugepage=never" --update-kernel=DEFAULT
        ```

    -   To set THP to `madvise`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # grubby --args="transparent_hugepage=madvise" --update-kernel=DEFAULT
        ```

3.  Reboot the system for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

-   To verify the status of THP, view the following files:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/kernel/mm/transparent_hugepage/enabled
    ```

    ``` {.language-plaintext tabindex="-1"}
    always madvise [never]
    ```

    ``` {.language-plaintext tabindex="-1"}
    # grep AnonHugePages: /proc/meminfo
    ```

    ``` {.language-plaintext tabindex="-1"}
    AnonHugePages:         0 kB
    ```

    ``` {.language-plaintext tabindex="-1"}
    # grep nr_anon_transparent_hugepages /proc/vmstat
    ```

    ``` {.language-plaintext tabindex="-1"}
    nr_anon_transparent_hugepages 0
    ```

#### [12.6.4. Managing transparent huge pages with a systemd unit file](#managing-transparent-hugepages-with-a-systemd-unit-file) {#managing-transparent-huge-pages-with-a-systemd-unit-file .title}

To manage transparent huge pages (THP) at system startup, use systemd unit files. Creating a service ensures consistent THP configuration across reboots.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Create new systemd service files for enabling, disabling and setting THP to `madvise`{.literal}. For example, `/etc/systemd/system/disable-thp.service`{.literal}.

2.  Configure THP by adding the following contents to a new systemd service file.

    -   To enable THP, add the following content to `<new_thp_file>.service`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [Unit]
        Description=Enable Transparent Hugepages
        After=local-fs.target
        Before=sysinit.target

        [Service]
        Type=oneshot
        RemainAfterExit=yes
        ExecStart=/bin/sh -c 'echo always > /sys/kernel/mm/transparent_hugepage/enabled

        [Install]
        WantedBy=multi-user.target
        ```

    -   To disable THP, add the following content to `<new_thp_file>.service`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [Unit]
        Description=Disable Transparent Hugepages
        After=local-fs.target
        Before=sysinit.target

        [Service]
        Type=oneshot
        RemainAfterExit=yes
        ExecStart=/bin/sh -c 'echo never > /sys/kernel/mm/transparent_hugepage/enabled

        [Install]
        WantedBy=multi-user.target
        ```

    -   To set THP to `madvise`{.literal}, add the following content to `<new_thp_file>.service`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [Unit]
        Description=Madvise Transparent Hugepages
        After=local-fs.target
        Before=sysinit.target

        [Service]
        Type=oneshot
        RemainAfterExit=yes
        ExecStart=/bin/sh -c 'echo madvise > /sys/kernel/mm/transparent_hugepage/enabled

        [Install]
        WantedBy=multi-user.target
        ```

3.  Enable and start the service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable <new_thp_file>.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start <new_thp_file>.service
    ```

**Verification**

-   To verify the status of THP, view the following files:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /sys/kernel/mm/transparent_hugepage/enabled
    ```

### [12.7. Impact of page size on translation lookaside buffer size](#impact-of-page-size-on-translation-lookaside-buffer-size) {#impact-of-page-size-on-translation-lookaside-buffer-size .title}

Reading address mappings from the page table is time-consuming and resource-expensive, so CPU designs include a cache for recently-used addresses, called the Translation Lookaside Buffer (TLB). However, the default TLB can only cache a certain number of address mappings.

If a requested address mapping is not in the TLB, called a TLB miss, the system still needs to read the page table to determine the physical to virtual address mapping. Because of the relationship between application memory requirements and the size of pages used to cache address mappings, applications with large memory requirements are more likely to suffer performance degradation from TLB misses than applications with minimal memory requirements. It is therefore important to avoid TLB misses wherever possible.

Both HugeTLB and Transparent Huge Page features allow applications to use pages larger than `4 KB`{.literal}. This allows addresses stored in the TLB to reference more memory, which reduces TLB misses and improves application performance.

### [12.8. Additional resources](#configuring-huge-pages_128-additional-resources) {#additional-resources .title}

-   [TuneD profiles distributed with RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/optimizing-system-performance-with-tuned#tuned-profiles-distributed-with-rhel)
-   [TuneD plugins](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/optimizing-system-performance-with-tuned#tuned-plug-ins)

## [Chapter 13. Managing memory devices](#managing-memory-devices) {#chapter-13.-managing-memory-devices .title}

As a system administrator, you can configure how Red Hat Enterprise Linux (RHEL) manages newly added memory devices. By default, RHEL uses `udev`{.literal} rules to automatically online hot-plugged memory. You can disable this behavior if you require manual control over memory onlining.

### [13.1. Automatic memory onlining with udev](#automatic-memory-onlining-with-udev) {#automatic-memory-onlining-with-udev .title}

Red Hat Enterprise Linux (RHEL) uses `udev`{.literal} rules to automatically online newly added memory devices, including Compute Express Link (CXL) memory. This mechanism ensures that hot-plugged memory blocks are immediately available to the operating system without manual intervention.

The default `udev`{.literal} rule for memory hot-plug operations is located at `/usr/lib/udev/rules.d/40-redhat-hotplug.rules`{.literal}. This file contains the configuration that triggers automatic memory onlining and, where applicable, assigns memory blocks to `ZONE_MOVABLE`{.literal}.

In RHEL bare metal, `ZONE_MOVABLE`{.literal} is configured automatically through this default `udev`{.literal} rule set. This ensures that when memory is dynamically added to the system, the kernel reserves a portion as `ZONE_MOVABLE`{.literal}, which can be safely removed later if needed. No manual configuration is required for hot-plugged memory devices.

**Additional resources**

-   [Configuring memory onlining in virtual machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/optimizing-virtual-machine-performance#configuring-memory-onlining-in-virtual-machines)
-   [Comparison of memory onlining configurations](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/optimizing-virtual-machine-performance#comparison-of-memory-onlining-configurations)
-   [Configuring Memory Hot(Un)Plug](https://www.kernel.org/doc/html/latest/admin-guide/mm/memory-hotplug.html#configuring-memory-hot-un-plug)

### [13.2. Configuring ZONE_NORMAL for GPGPU and other CXL accelerator memory use cases](#configuring-zone-normal-for-gpgpu-and-other-cxl-accelerator-memory-use-cases) {#configuring-zone_normal-for-gpgpu-and-other-cxl-accelerator-memory-use-cases .title}

Configure CXL memory as `ZONE_NORMAL`{.literal} when GPGPU or other accelerator workloads require stable direct memory access (DMA) to shared CXL memory. During DMA transfers, page addresses must stay fixed, so the kernel allocates that memory from `ZONE_NORMAL`{.literal}.

Configuring CXL memory as `ZONE_NORMAL`{.literal} through a `udev`{.literal} override applies to GPGPU devices and other CXL-based accelerators that require stable DMA access to CXL memory.

Regular processes use the `ZONE_MOVABLE`{.literal} memory area, but the kernel and drivers do not. If the kernel or drivers use areas on a memory device, you cannot hot-remove that device.

GPGPU devices and other CXL-based accelerators might need to use areas of a CXL memory device for artificial intelligence (AI) processing. In such cases, the default `udev`{.literal} setting assigns memory to ZONE_MOVABLE and can prevent stable DMA transfers in the following workloads:

-   Storing and referencing data between GPUs by using shared CXL memory. For example, a key-value cache in AI or large language model workloads.
-   Handling large-scale GPGPU data that exceeds the capacity of onboard GPU memory or standard double data rate (DDR) memory.

**Prerequisites**

-   You have root privileges on your system.

-   You reviewed your device driver documentation and confirmed that stable DMA to CXL memory requires `ZONE_NORMAL`{.literal} memory.

    Important

    When you configure memory as `ZONE_NORMAL`{.literal}, the kernel and drivers can use it. You might no longer safely hot-remove the associated memory device. Use this configuration only when your workload requires device DMA access to CXL memory and hot-remove is not required for the affected memory device.

**Procedure**

1.  Copy the default rule to the local override directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp /usr/lib/udev/rules.d/40-redhat-hotplug.rules /etc/udev/rules.d/
    ```

2.  Edit `/etc/udev/rules.d/40-redhat-hotplug.rules`{.literal} in a text editor by changing `online_movable`{.literal} to `online_kernel`{.literal} in the memory hot-plug rule:

    Before:

    ``` {.language-bash tabindex="-1"}
    ENV{.state}="online"
    CONST{virt}=="none", ENV{.state}="online_movable"
    ATTR{state}=="offline", ATTR{state}="$env{.state}"
    ```

    After:

    ``` {.language-bash tabindex="-1"}
    ENV{.state}="online"
    CONST{virt}=="none", ENV{.state}="online_kernel"
    ATTR{state}=="offline", ATTR{state}="$env{.state}"
    ```

3.  Reload `udev`{.literal} rules to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # udevadm control --reload-rules
    ```

4.  Reboot the system.

    Alternatively, remove the device and add it back to the system to ensure the new configuration takes effect.

**Verification**

-   Verify that after you apply this configuration, RHEL assigns new memory blocks on bare metal systems to `ZONE_NORMAL`{.literal} instead of `ZONE_MOVABLE`{.literal}. Device drivers can allocate DMA-capable memory from those blocks when your hardware and driver stack support it.

### [13.3. Disabling automatic memory onlining](#disabling-automatic-memory-onlining) {#disabling-automatic-memory-onlining .title}

To prevent newly added memory devices from becoming immediately available to the operating system, disable automatic memory onlining in Red Hat Enterprise Linux by modifying the relevant `udev`{.literal} rules.

**Prerequisites**

-   You have root privileges on your system.

**Procedure**

1.  Copy the default rule to the local override directory:

    ``` {.language-plaintext tabindex="-1"}
    cp /usr/lib/udev/rules.d/40-redhat-hotplug.rules /etc/udev/rules.d/
    ```

2.  Edit the `/etc/udev/rules.d/40-redhat-hotplug.rules`{.literal} file in a text editor and comment out the lines that handle memory hot-plug operations:

    ``` {.language-bash tabindex="-1"}
    # Memory hotadd request
    #SUBSYSTEM!="memory", GOTO="memory_hotplug_end"
    #ACTION!="add", GOTO="memory_hotplug_end"
    #CONST{arch}=="s390*", GOTO="memory_hotplug_end"
    #CONST{arch}=="ppc64*", GOTO="memory_hotplug_end"
    #ENV{.state}="online"
    #CONST{virt}=="none", ENV{.state}="online_movable"
    #ATTR{state}=="offline", ATTR{state}="$env{.state}"
    #LABEL="memory_hotplug_end"
    ```

3.  Reload `udev`{.literal} rules to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    udevadm control --reload-rules
    ```

4.  Reboot the system, or remove the device and add it back to the system to ensure the new configuration takes effect.

**Verification**

-   After disabling automatic onlining, newly added memory blocks will remain offline until you manually online them.

### [13.4. Manually onlining memory](#manually-onlining-memory) {#manually-onlining-memory .title}

If you have disabled automatic memory onlining, newly added memory blocks, such as those from a hot-plugged CXL device, remain offline by default. You can manually online these memory blocks by using the `sysfs`{.literal} interface.

**Prerequisites**

-   You have root privileges on your system.

**Procedure**

1.  Identify the offline memory block identifier using the `lsmem`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # lsmem
    ```

    ``` {.language-plaintext tabindex="-1"}
    RANGE                                  SIZE  STATE REMOVABLE BLOCK
    0x0000000000000000-0x000000007fffffff    2G online       yes  0-1
    0x0000000100000000-0x000000087fffffff   30G online       yes  4-33
    0x0000000880000000-0x00000008ffffffff    2G offline           34-41

    Memory block size:       256M
    Total online memory:      32G
    Total offline memory:      2G
    ```

    In this example, the offline memory blocks are `34-41`{.literal}.

2.  Online a specific memory block by writing to its state file:

    ``` {.language-plaintext tabindex="-1"}
    echo online > /sys/devices/system/memory/memory<_identifier_>/state
    ```

    Replace `memory<_identifier_>`{.literal} with the identifier of the memory block, for example, `memory34`{.literal}.

**Verification**

-   Verify the memory block is online:

    ``` {.language-plaintext tabindex="-1"}
    cat /sys/devices/system/memory/memory<_identifier_>/state
    ```

    ``` {.language-plaintext tabindex="-1"}
    online
    ```

### [13.5. Managing CXL memory devices](#managing-cxl-memory-devices) {#managing-cxl-memory-devices .title}

CXL v2 memory hot-plugging enables you to add and remove memory resources dynamically in Red Hat Enterprise Linux environments, supporting data center flexibility. With CXL devices and external switches, you can create shared memory pools beyond traditional hardware limits when your system supports CXL v2.

CXL v2 introduces enhanced memory management and hot-plug capabilities, and extends support to bare-metal systems. These enhancements help reduce the risks associated with manual memory node removal, thereby improving system stability and reliability.

Note

Before configuring CXL v2 memory hot-plugging, verify that your system firmware and hardware are compatible with CXL v2.

#### [13.5.1. CXL memory device status levels](#cxl-memory-device-status-levels) {#cxl-memory-device-status-levels .title}

A Compute Express Link (CXL) memory device transitions through several states in response to specific system events. The terms \"Level 0\" through \"Level 4\" describe the state transitions of a CXL memory device during hot-plug operations.

In RHEL, CXL memory is managed in units called memory regions. A memory region can correspond to a single CXL device or span multiple devices by specifying interleave during creation. Memory incorporated into memory regions must be brought \"online\" before it is available to the operating system.

You must modify or configure memory regions manually in several scenarios. For example, during a hot-add event, the driver detects the hardware connection but does not automatically configure memory regions or bring the memory online. Similarly, you must manually create memory regions when you want to interleave memory across multiple CXL devices to improve performance, as the driver cannot automatically determine the interleave topology you want.

Level 0

:   The CXL driver does not detect the CXL device.

    At this stage, the device is not recognized by the kernel.

Level 1

:   The CXL driver detects the hardware and establishes a connection.

    The device is recognized on system boot, or an interrupt is raised for hot-adding a CXL device. This level indicates the device is connected but unconfigured.

Level 2

:   A memory region is created for the CXL device.

    A specific memory region has been defined and allocated for the device, but it is not yet enabled.

Level 3

:   The memory region is enabled but not yet online for the Operating System.

    The CXL memory region is active, but the memory blocks have not been transitioned to the \"online\" state for kernel use.

Level 4

:   The OS can use the hot-added CXL memory device.

    At this point, memory blocks are online and available to the operating system. If memory blocks are taken offline, the device returns to Level 3.

**Additional resources**

-   [Hot-removing CXL memory devices](#hot-removing-cxl-memory-devices "13.5.5. Hot-removing CXL memory devices")
-   [CXL Command Manual](https://docs.pmem.io/ndctl-user-guide/cxl-man-pages/cxl-1)

#### [13.5.2. Safe offline of hot-removable memory](#safe-offline-of-hot-removable-memory) {#safe-offline-of-hot-removable-memory .title}

In Red Hat Enterprise Linux (RHEL), you cannot offline or hot-remove memory that the kernel or drivers use. RHEL cannot migrate data from these areas, which can block hot-remove operations.

By default, the kernel and drivers can use all memory areas. This behavior prevents other memory devices, such as Compute Express Link (CXL), from being hot-plugged or hot-removed. To avoid this limitation, RHEL allows you to create a `ZONE_MOVABLE`{.literal}. This memory area is not used by the kernel or drivers, ensuring that it can be safely hot-removed.

For bare-metal systems, RHEL automatically configures `ZONE_MOVABLE`{.literal} through the default `udev`{.literal} rules for hot-plugged memory. This configuration ensures safer hot-removal of devices such as CXL without manual configuration.

#### [13.5.3. Preventing triggering the OOM Killer when hot-adding memory](#preventing-triggering-the-oom-killer-when-hot-adding-memory) {#preventing-triggering-the-oom-killer-when-hot-adding-memory .title}

The kernel requires memory capacity to manage hot-added memory, known as the `memmap`{.literal} area. This area uses about 1.6% of total memory, for example 16 GB for 1 TB. By default, the kernel allocates it from `ZONE_NORMAL`{.literal}. If `ZONE_NORMAL`{.literal} lacks free memory, this allocation can trigger the OOM Killer.

Allocating the `memmap`{.literal} area from the hot-added memory itself avoids exhausting `ZONE_NORMAL`{.literal}. Specific devices, such as Compute Express Link (CXL) devices and standard Dual Inline Memory Modules (DIMMs), support this feature.

**Prerequisites**

-   You have root permissions on the system.
-   Your memory hardware supports allocating `memmap`{.literal} on the device itself. Refer to your hardware manufacturer's documentation for more information.

**Procedure**

1.  Enable the `memmap_on_memory`{.literal} feature by adding the following kernel boot option:

    ``` {.language-bash tabindex="-1"}
    memory_hotplug.memmap_on_memory=1
    ```

2.  Reboot the system for the change to take effect.

**Verification**

-   Verify the setting is enabled:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/module/memory_hotplug/parameters/memmap_on_memory
    ```

    ``` {.language-plaintext tabindex="-1"}
    Y
    ```

#### [13.5.4. Hot-plugging CXL memory devices](#hot-plugging-cxl-memory-devices) {#hot-plugging-cxl-memory-devices .title}

To dynamically increase system memory, you can hot-plug memory devices, such as Compute Express Link (CXL) modules or Dual Inline Memory Modules (DIMMs), in Red Hat Enterprise Linux.

**Prerequisites**

-   You are running Red Hat Enterprise Linux 8 or later.
-   You have root privileges on your system.
-   Your system firmware such as BIOS or UEFI, and hardware components such as a CXL switch or backplane, must support memory hot-plug events.

**Procedure**

1.  Insert the supported memory device into the appropriate slot according to your hardware vendor's instructions.

    The hot-plug event can originate from a physical installation of a memory module into a slot, or from a logical allocation, such as dynamically assigning memory from a CXL shared memory pool.

2.  List the online status of memory blocks and confirm if the newly added memory was automatically onlined:

    ``` {.language-plaintext tabindex="-1"}
    # lsmem
    ```

    ``` {.language-plaintext tabindex="-1"}
    RANGE                                  SIZE  STATE REMOVABLE BLOCK
    0x0000000000000000-0x000000007fffffff    2G online       yes  0-1
    0x0000000100000000-0x000000087fffffff   30G online       yes  4-33
    0x0000000880000000-0x00000008ffffffff    2G offline           34-41

    Memory block size:       256M
    Total online memory:      32G
    Total offline memory:      2G
    ```

    Note

    If the memory remains offline, verify if automatic memory onlining is disabled. For more information, see [Disabling automatic memory onlining](#disabling-automatic-memory-onlining "13.3. Disabling automatic memory onlining"). You must manually online the memory blocks if the operation did not complete automatically.

**Verification**

-   Check the system memory and NUMA topology to ensure the new memory is fully integrated:

    ``` {.language-plaintext tabindex="-1"}
    # free -h
    # numactl -H
    ```

Important

If you encounter issues, review hardware documentation and ensure all prerequisites are met.

**Troubleshooting**

-   Optional: Review the relevant logs for errors or warnings:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -k | grep -i memory
    # dmesg | tail
    ```

#### [13.5.5. Hot-removing CXL memory devices](#hot-removing-cxl-memory-devices) {#hot-removing-cxl-memory-devices .title}

To safely hot-remove a Compute Express Link (CXL) memory device, you must ensure that the memory is no longer in use by the kernel. You can safely hot-remove a CXL memory device by taking the memory offline and disabling the associated memory regions.

**Prerequisites**

-   You have root privileges on your system.

**Procedure**

1.  Set the memory to offline.

    This allows the kernel to migrate data away from the memory area being removed, ensuring it is no longer in use.

2.  Disable the CXL memory region if it is still active:

    ``` {.language-plaintext tabindex="-1"}
    # cxl disable-region
    ```

    Note

    The `cxl disable-region`{.literal} command also automatically takes the memory offline if it is still online.

3.  Destroy the CXL memory region:

    ``` {.language-plaintext tabindex="-1"}
    # cxl destroy-region
    ```

4.  Disable the memory device:

    ``` {.language-plaintext tabindex="-1"}
    # cxl disable-memdev
    ```

5.  After all commands complete successfully, physically remove the CXL device or disconnect it using your hardware's management interface.

**Additional resources**

-   [CXL Command Manual](https://docs.pmem.io/ndctl-user-guide/cxl-man-pages/cxl-1)

#### [13.5.6. Verifying CXL memory status](#verifying-cxl-memory-status) {#verifying-cxl-memory-status .title}

You can verify the status and configuration of Compute Express Link (CXL) memory devices by using various command-line tools.

**Prerequisites**

-   You have root privileges.
-   The `pciutils`{.literal} package is installed (for `lspci`{.literal}).
-   The `numactl`{.literal} package is installed.

**Procedure**

1.  Check the CXL device connection by using the `lspci`{.literal} command:

    Because CXL is an extension of PCIe, you can use `lspci`{.literal} to view device details.

    ``` {.language-plaintext tabindex="-1"}
    # lspci -vvv
    ```

    ``` {.language-plaintext tabindex="-1"}
    01:00.0 CXL: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX [CXL Memory Device (CXL 2.x)]
            Subsystem: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            ...
            NUMA node: 0
            ...
    ```

2.  Check the CXL memory status as NUMA nodes:

    CXL memory is treated as CPU-less NUMA nodes. Use the `numactl`{.literal} command to check the status.

    ``` {.language-plaintext tabindex="-1"}
    # numactl -H --cpu-compress
    ```

    ``` {.language-plaintext tabindex="-1"}
    available: 4 nodes (0-3)
    node 0 cpus: 0-95, 192-287 (192)
    node 0 size: 15219 MB
    ...
    node 2 cpus: (0)
    node 2 size: 258048 MB
    ...
    ```

3.  Verify BIOS/EFI configuration support by checking specifically for a \"soft reserved\" area in the BIOS-e820 output using `dmesg`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [    0.000000] BIOS-e820: [mem 0x0000001070000000-0x000000506fffffff] soft reserved
    ```

    Support for configuring CXL memory devices depends on the `EFI_MEMORY_SP`{.literal} BIOS feature. If this setting is not enabled, Red Hat Enterprise Linux (RHEL) treats the CXL device as ordinary RAM. If this setting is not configured, the kernel treats the CXL device as DDR DRAM. Refer to your platform's firmware configuration manual for instructions.

#### [13.5.7. Using CXL memory as shared memory between servers](#using-cxl-memory-as-shared-memory-between-servers) {#using-cxl-memory-as-shared-memory-between-servers .title}

When using Compute Express Link (CXL) memory as shared memory between servers, ensure the device is set to Level 3 (Memory region enabled but not online for the OS).

The standard OS memory management system operates at level 4. However, using shared memory between servers requires a dedicated interface and cannot be handled by traditional RHEL memory management.

To use CXL memory as shared memory between servers, keep it offline. To keep the memory offline, you must create custom `udev`{.literal} rules to prevent the automatic online operation that RHEL performs by default.

**Additional resources**

-   [Disabling automatic memory onlining](#disabling-automatic-memory-onlining "13.3. Disabling automatic memory onlining")

#### [13.5.8. Considerations for hot-unplugging memory devices](#troubleshooting-memory-hot-removal) {#considerations-for-hot-unplugging-memory-devices .title}

When planning to hot-remove memory devices, consider the following potential issues and limitations.

Migration failure messages
:   When offlining memory, you can see migration failure messages such as:

``` {.language-plaintext tabindex="-1"}
[ 6381.169189] page dumped because: migration failure
[ 6381.181353] migrating pfn 8842600 failed ret:2
...
```

This indicates a failure to move data from the memory targeted for removal. The kernel retries memory migration, and it usually completes successfully. However, hot removal fails depending on system conditions:

Insufficient memory after removal
:   If memory capacity is insufficient after removal, memory migration might fail. Ensure enough free memory remains before starting the hot removal.

Using Transparent Hugepages
:   If Transparent Hugepages are used, there might not be enough free memory for 2MB pages, which can cause migration delays or failures. Consider disabling Transparent Hugepages or ensuring that sufficient free memory is available.

Using Hugetlb Pages

:   -   **1GB hugepages**: Hot removal is not supported.

    -   **2MB hugepages**: Requires contiguous free memory for migration. If the memory is not available, hot removal fails.

        Out of Memory (OOM) Killer risks
        :   If a process is bound to a Non-Uniform Memory Access (NUMA) node through `mbind(MPOL_BIND)`{.literal} and you hot-remove that node, the kernel triggers the OOM Killer due to insufficient memory.

Stop these processes before performing the hot removal.

**Additional resources**

-   [Configuring Memory Hot(Un)Plug](https://www.kernel.org/doc/html/latest/admin-guide/mm/memory-hotplug.html#configuring-memory-hot-un-plug)

## [Chapter 14. Getting started with kernel logging](#getting-started-with-kernel-logging) {#chapter-14.-getting-started-with-kernel-logging .title}

Kernel logging in Red Hat Enterprise Linux uses the `syslog`{.literal} service to record system, kernel, service, and application events into log files for auditing and troubleshooting.

### [14.1. What is the kernel ring buffer](#what-is-the-kernel-ring-buffer) {#what-is-the-kernel-ring-buffer .title}

The kernel uses a ring buffer to store `printk()`{.literal} messages, preserving critical information during system startup. This preserves early boot messages before services such as `syslog`{.literal} can read and save them to permanent storage.

The ring buffer is a cyclic data structure that has a fixed size, and is hard-coded into the kernel. Users can display data stored in the kernel ring buffer through the `dmesg`{.literal} command or the `/var/log/boot.log`{.literal} file. When the ring buffer is full, the new data overwrites the old.

See `syslog(2)`{.literal} and `dmesg(1)`{.literal} man pages on your system for more information.

### [14.2. Role of printk on log-levels and kernel logging](#role-of-printk-on-log-levels-and-kernel-logging) {#role-of-printk-on-log-levels-and-kernel-logging .title}

Kernel messages have log-levels that indicate their importance. The kernel ring buffer collects all messages. The `kernel.printk`{.literal} parameter controls which buffer messages reach the console.

The log-level values break down in this order:

0
:   Kernel emergency. The system is unusable.

1
:   Kernel alert. Action must be taken immediately.

2
:   Condition of the kernel is considered critical.

3
:   General kernel error condition.

4
:   General kernel warning condition.

5
:   Kernel notice of a normal but significant condition.

6
:   Kernel informational message.

7
:   Kernel debug-level messages.

By default, `kernel.printk`{.literal} in RHEL 10 has the following values:

``` {.language-plaintext tabindex="-1"}
# sysctl kernel.printk
kernel.printk = 7   4   1   7
```

The four values define the following, in order:

1.  Console log-level, defines the lowest priority of messages printed to the console.

2.  Default log-level for messages without an explicit log-level attached to them.

3.  Sets the lowest possible log-level configuration for the console log-level.

4.  Sets default value for the console log-level at boot time.

    Each of these values defines a different rule for handling error messages.

Important

The default `7 4 1 7`{.literal} `printk`{.literal} value allows for better debugging of kernel activity. However, when coupled with a serial console, this `printk`{.literal} setting might cause intense I/O bursts that might lead to a RHEL system becoming temporarily unresponsive. To avoid these situations, setting a `printk`{.literal} value of `4 4 1 7`{.literal} typically works, but at the expense of losing the extra debugging information.

Also note that certain kernel command line parameters, such as `quiet`{.literal} or `debug`{.literal}, change the default `kernel.printk`{.literal} values.

See the `syslog(2)`{.literal} man page on your system for more information.

**Additional resources**

-   [What is the kernel ring buffer](#what-is-the-kernel-ring-buffer "14.1. What is the kernel ring buffer")

## [Chapter 15. Reinstalling GRUB](#reinstalling-grub) {#chapter-15.-reinstalling-grub .title}

Reinstall the GRUB boot loader to resolve issues caused by incorrect installation, missing files, or system corruption. Reinstalling GRUB is also necessary when upgrading packages, adding boot information to another drive, or restoring control over installed operating systems.

Note

GRUB restores files only if they are not corrupted.

### [15.1. Reinstalling GRUB on BIOS-based machines](#reinstalling-grub-on-bios-based-machines) {#reinstalling-grub-on-bios-based-machines .title}

To ensure your BIOS-based system remains functional at startup, reinstall the GRUB boot loader on the system after updating GRUB packages.

Important

This overwrites the existing GRUB to install the new GRUB. Ensure that the system does not cause data corruption or boot crash during the installation.

**Procedure**

1.  Install `grub2-pc`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # grub2-pc
    ```

2.  Reinstall GRUB on the device where it is installed. For example, if `sda`{.literal} is your device:

    ``` {.language-plaintext tabindex="-1"}
    # grub2-install /dev/sda
    ```

3.  Reboot your system for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

    See the `grub2-pc(8)`{.literal} man page on your system for more information.

### [15.2. Reinstalling GRUB on UEFI-based machines](#reinstalling-grub-on-uefi-based-machines) {#reinstalling-grub-on-uefi-based-machines .title}

To resolve boot issues, reinstall the GRUB boot loader on your UEFI-based system.

Important

Ensure that the system does not cause data corruption or boot crash during the installation.

**Procedure**

1.  Reinstall the `grub2-efi`{.literal} and `shim`{.literal} boot loader files:

    ``` {.language-plaintext tabindex="-1"}
    # dnf reinstall grub2-efi-x64 shim
    ```

2.  Reboot your system for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

### [15.3. Reinstalling GRUB on IBM Power machines](#reinstalling-grub-on-ibm-power-machines) {#reinstalling-grub-on-ibm-power-machines .title}

To maintain system bootability on IBM Power systems, reinstall the GRUB boot loader on the Power PC Reference Platform (PReP) boot partition after updating GRUB packages.

Important

This overwrites the existing GRUB to install the new GRUB. Ensure that the system does not cause data corruption or boot crash during the installation.

**Procedure**

1.  List the disk partition that stores GRUB:

    ``` {.language-plaintext tabindex="-1"}
    # bootlist -m normal -o
    ```

    ``` {.language-plaintext tabindex="-1"}
    sda1
    ```

2.  Reinstall GRUB on the disk partition:

    ``` {.language-plaintext tabindex="-1"}
    # grub2-install partition
    ```

    Replace *`partition`{.literal}* with the identified GRUB partition, such as `/dev/sda1`{.literal}.

3.  Reboot your system for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

    See the `grub-install(1)`{.literal} man page on your system for more information.

### [15.4. Resetting GRUB](#resetting-grub) {#resetting-grub .title}

To fix boot failures caused by corrupted files or invalid configurations, reset GRUB. This process removes current settings and reinstalls the boot loader with default values.

Important

The following procedure will remove all the customization made by the user.

**Procedure**

1.  Remove the configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # rm /etc/grub.d/*
    # rm /etc/sysconfig/grub
    ```

2.  Reinstall packages.

    -   On BIOS-based machines:

        ``` {.language-plaintext tabindex="-1"}
        # dnf reinstall grub2-pc grub2-tools
        ```

    -   On UEFI-based machines:

        ``` {.language-plaintext tabindex="-1"}
        # dnf reinstall grub2-efi shim grub2-tools grub2-common
        ```

3.  Rebuild the `grub.cfg`{.literal .filename} file for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # grub2-mkconfig -o /boot/grub2/grub.cfg
    ```

    This applies to both, BIOS and UEFI based systems.

    Warning

    The path to rebuild `grub.cfg`{.literal} is same for both BIOS and UEFI based machines. Actual `grub.cfg`{.literal} is present at BIOS path only. The UEFI path has a stub file that must not be modified or recreated using `grub2-mkconfig`{.literal} command.

4.  Follow [Reinstalling GRUB](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/reinstalling-grub) procedure to restore GRUB on the `/boot/`{.literal} partition.

## [Chapter 16. Installing kdump](#installing-kdump) {#chapter-16.-installing-kdump .title}

The `kdump`{.literal} service is installed and activated by default on Red Hat Enterprise Linux installations. You can enable and configure `kdump`{.literal} during installation with Anaconda or afterward on the command line.

### [16.1. What is kdump](#what-is-kdump) {#what-is-kdump .title}

The `kdump`{.literal} utility provides a crash dumping mechanism that generates a `vmcore`{.literal} file for analysis. By using the `kexec`{.literal} system call, `kdump`{.literal} boots into a reserved *capture kernel* without a reboot. It then saves the crashed kernel's memory to a file.

Important

A kernel crash dump can be the only information available if a system failure occurs. Therefore, operational kdump is important in mission-critical environments. You must regularly update and test `kexec-tools`{.literal}, `kdump-utils`{.literal}, and `makedumpfile`{.literal} packages in your normal kernel update cycle. This is important when you install new kernel features.

If you have multiple kernels on a machine, you can enable kdump for all installed kernels or for specified kernels only. When you install `kdump`{.literal}, the system creates a default `/etc/kdump.conf`{.literal} file. `/etc/kdump.conf`{.literal} includes the default minimum kdump configuration, which you can edit to customize the kdump configuration.

### [16.2. Installing kdump using Anaconda](#installing-kdump-anaconda) {#installing-kdump-using-anaconda .title}

To configure `kdump`{.literal} during an interactive installation, use the **Anaconda** installer's graphical interface. With this feature, you can enable `kdump`{.literal} and reserve the necessary memory.

**Procedure**

1.  On the Anaconda installer, click **KDUMP** and enable `kdump`{.literal}.
2.  In **Kdump Memory Reservation**, select **Manual** if you must customize the memory reserve.
3.  In **KDUMP \> Memory To Be Reserved (MB)**, set the required memory reserve for `kdump`{.literal}.

### [16.3. Installing kdump on the command line](#installing-kdump-command-line) {#installing-kdump-on-the-command-line .title}

To enable `kdump`{.literal} when it is not installed by default, such as in custom **Kickstart** installations, install the required packages and confirm the installation.

**Prerequisites**

-   An active Red Hat Enterprise Linux subscription.
-   A repository containing the `kexec-tools`{.literal}, `kdump-utils`{.literal}, and `makedumpfile`{.literal} packages for your system CPU architecture.
-   Fulfilled requirements for `kdump`{.literal} configurations and targets. For details, see [Supported kdump configurations and targets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/supported-kdump-configurations-and-targets).

**Procedure**

1.  Check if `kdump`{.literal} is installed on your system:

    ``` {.language-plaintext tabindex="-1"}
    # rpm -q kexec-tools kdump-utils makedumpfile
    ```

2.  If the `kdump`{.literal} is not installed, install required packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kexec-tools kdump-utils makedumpfile
    ```

## [Chapter 17. Configuring kdump on the command line](#configuring-kdump-on-the-command-line) {#chapter-17.-configuring-kdump-on-the-command-line .title}

Configure `kdump`{.literal} memory reservation in the GRUB configuration file. The reserved memory size depends on the `crashkernel=`{.literal} value and the system's physical memory size.

### [17.1. Estimating the kdump size](#estimating-the-kdump-size) {#estimating-the-kdump-size .title}

To plan and build your `kdump`{.literal} environment effectively, estimate the space required by the crash dump file.

The `makedumpfile --mem-usage`{.literal} command estimates the space required by the crash dump file. It generates a memory usage report. The report helps you decide the dump level and the pages that are safe to exclude.

**Procedure**

-   Enter the following command to generate a memory usage report:

    ``` {.language-plaintext tabindex="-1"}
    # makedumpfile --mem-usage /proc/kcore
    ```

    ``` {.language-plaintext tabindex="-1"}
    TYPE        PAGES    EXCLUDABLE    DESCRIPTION
    -------------------------------------------------------------
    ZERO          501635      yes        Pages filled with zero
    CACHE         51657       yes        Cache pages
    CACHE_PRIVATE 5442        yes        Cache pages + private
    USER          16301       yes        User process pages
    FREE          77738211    yes        Free pages
    KERN_DATA     1333192     no         Dumpable kernel data
    ```

    Important

    The `makedumpfile --mem-usage`{.literal} command reports required memory in pages. This means that you must calculate the size of memory in use against the kernel page size.

    By default the RHEL kernel uses 4 KB sized pages on AMD64 and Intel 64 CPU architectures, and 64 KB sized pages on IBM POWER architectures.

### [17.2. Configuring kdump memory usage](#configuring-kdump-memory-usage) {#configuring-kdump-memory-usage .title}

Configure the memory reservation for `kdump`{.literal}. The `kdump-utils`{.literal} package provides default `crashkernel=`{.literal} values that you can use as a reference when setting memory manually.

The automatic memory allocation for `kdump`{.literal} varies based on the system hardware architecture and available memory size. For example, on AMD64 and Intel 64-bit architectures, the default value for the `crashkernel=`{.literal} parameter works only when the available memory is more than 2 GB. The `kdump-utils`{.literal} utility configures the following default memory reserves on AMD64 and Intel 64-bit architecture:

``` {.language-plaintext tabindex="-1"}
crashkernel=2G-64G:256M,64G-:512M
```

You can also run `kdumpctl estimate`{.literal} to get an approximate value without triggering a crash. The estimated `crashkernel=`{.literal} value might not be an exact one but can serve as a reference to set an appropriate `crashkernel=`{.literal} value.

Note that the `crashkernel=1G-4G:192M,4G-64G:256M,64G:512M`{.literal} option in the boot command line is no longer supported on RHEL 10 and later releases.

Warning

The commands to test `kdump`{.literal} configuration cause the kernel to crash with data loss. Follow the instructions with care. Do not use an active production system to test the `kdump`{.literal} configuration.

**Prerequisites**

-   You have root permissions on the system.
-   You have fulfilled `kdump`{.literal} requirements for configurations and targets. For details, see [Supported kdump configurations and targets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/supported-kdump-configurations-and-targets).
-   You have installed the `zipl`{.literal} utility if it is the IBM Z system.

**Procedure**

1.  Configure the default value for crash kernel:

    ``` {.language-plaintext tabindex="-1"}
    # kdumpctl reset-crashkernel --kernel=ALL
    ```

    When configuring the `crashkernel=`{.literal} value, test the configuration by rebooting the system with `kdump`{.literal} enabled. If the `kdump`{.literal} kernel fails to boot, increase the memory size gradually to set an acceptable value.

2.  To use a custom `crashkernel=`{.literal} value

    a.  Configure the required memory reserve:

        ``` {.language-plaintext tabindex="-1"}
        crashkernel=192M
        ```

        Optionally, you can set the amount of reserved memory to a variable depending on the total amount of installed memory by using the syntax `crashkernel=`{.literal}*`<range1>:<size1>,<range2>:<size2>`{.literal}*. For example:

        ``` {.language-plaintext tabindex="-1"}
        crashkernel=1G-4G:192M,2G-64G:256M
        ```

        The example reserves 192 MB of memory if the total amount of system memory is 1 GB or higher and lower than 4 GB. If the total amount of memory is more than 4 GB, 256 MB is reserved for `kdump`{.literal}.

    b.  Optional: Offset the reserved memory.

        Some systems must reserve memory at a certain fixed offset. The `crashkernel`{.literal} reservation occurs early during the boot process, and the system uses some memory areas for special purposes. Setting a memory offset ensures that the reserved crash memory does not overlap with these areas, which helps prevent boot failures and ensures reliable crash dump capture. To offset the reserved memory, use the following syntax:

        ``` {.language-plaintext tabindex="-1"}
        crashkernel=192M@16M
        ```

        The example reserves 192 MB of memory starting at 16 MB (physical address 0x01000000). If you offset to 0 or do not specify a value, `kdump`{.literal} offsets the reserved memory automatically. You can also offset memory when setting a variable memory reservation by specifying the offset as the last value. For example, `crashkernel=1G-4G:192M,2G-64G:256M@16M`{.literal}.

    c.  Update the boot loader configuration:

        ``` {.language-plaintext tabindex="-1"}
        # grubby --update-kernel ALL --args "crashkernel=<custom-value>"
        ```

        The *`<custom-value>`{.literal}* must contain the custom `crashkernel=`{.literal .option} value that you have configured for the crash kernel.

3.  Reboot for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

Cause the kernel to crash by activating the `sysrq`{.literal} key. The `address-YYYY-MM-DD-HH:MM:SS/vmcore`{.literal} file is saved to the target location as specified in the `/etc/kdump.conf`{.literal} file. If you select the default target location, the `vmcore`{.literal} file is saved in the partition mounted under `/var/crash/`{.literal}.

1.  Activate the `sysrq`{.literal} key to boot into the `kdump`{.literal} kernel:

    ``` {.language-plaintext tabindex="-1"}
    # echo c > /proc/sysrq-trigger
    ```

    The command causes kernel to crash and reboots the kernel if required.

2.  Display the `/etc/kdump.conf`{.literal} file and check if the `vmcore`{.literal} file is saved in the target destination.

    See the `grubby(8)`{.literal} man page on your system for more information.

**Additional resources**

-   [How to manually modify the boot parameter in grub before the system boots Red Hat Knowledgebase)](https://access.redhat.com/solutions/32726)

### [17.3. Configuring the kdump target](#configuring-the-kdump-target) {#configuring-the-kdump-target .title}

Configure where `kdump`{.literal} stores crash dump files. You can store dumps locally or send them over a network by using NFS or SSH. You can configure only one storage option at a time. By default, `kdump`{.literal} stores crash dumps in `/var/crash/`{.literal} on the local file system.

**Prerequisites**

-   You have root permissions on the system.
-   Fulfilled requirements for `kdump`{.literal} configurations and targets. For details, see [Supported kdump configurations and targets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/supported-kdump-configurations-and-targets).

**Procedure**

-   To store the crash dump file in `/var/crash/`{.literal} directory of the local file system, edit the `/etc/kdump.conf`{.literal} file and specify the path:

    ``` {.language-plaintext tabindex="-1"}
    path /var/crash
    ```

    The option `path /var/crash`{.literal} represents the path to the file system in which `kdump`{.literal} saves the crash dump file.

    When you specify a dump target in the `/etc/kdump.conf`{.literal} file, the path is **relative** to the specified dump target. When you do not specify a dump target, the path represents the **absolute** path from the root directory. Depending on the file system mounted in the current system, the dump target and the adjusted dump path are configured automatically.

-   To secure the crash dump file and the accompanying files produced by `kdump`{.literal}, you must configure proper attributes for the target destination directory. These attributes include user permissions and SELinux contexts. Additionally, you can define a script, for example `kdump_post.sh`{.literal} in the `kdump.conf`{.literal} file as follows:

    ``` {.language-plaintext tabindex="-1"}
    kdump_post <path_to_kdump_post.sh>
    ```

    The `kdump_post`{.literal} directive specifies a shell script or a command. This script runs after `kdump`{.literal} has captured and saved a crash dump to the specified destination. You can use this mechanism to extend the functionality of `kdump`{.literal} to perform actions including the adjustments in file permissions.

-   Displaying and understanding the `kdump`{.literal} target configuration:

    a.  Show the effective configuration by filtering out comments and empty lines:

        ``` {.language-bash tabindex="-1"}
        # grep -v '^#' /etc/kdump.conf | grep -v '^$'
        ```

    b.  Example output:

        ``` {.language-plaintext tabindex="-1"}
        ext4 /dev/mapper/vg00-varcrashvol
        path /var/crash
        core_collector makedumpfile -c --message-level 1 -d 31
        ```

        The dump target is specified (`ext4 /dev/mapper/vg00-varcrashvol`{.literal}), and, therefore, it is mounted at `/var/crash`{.literal}. The `path`{.literal} option is also set to `/var/crash`{.literal}. Therefore, the `kdump`{.literal} saves the `vmcore`{.literal} file in the `/var/crash/var/crash`{.literal} directory.

-   To change the local directory for saving the crash dump, edit the `/etc/kdump.conf`{.literal} configuration file as a `root`{.literal} user:

    a.  Remove the hash sign (`#`{.literal}) from the beginning of the `#path /var/crash`{.literal} line.

    b.  Replace the value with the intended directory path. For example:

        ``` {.language-plaintext tabindex="-1"}
        path /usr/local/cores
        ```

        Important

        In Red Hat Enterprise Linux 10, the directory defined as the `kdump`{.literal} target using the `path`{.literal} directive must exist before the `kdump`{.literal} systemd service starts. Otherwise, the service fails. The directory is no longer created automatically if it does not exist when the service starts.

-   To write the file to a different partition, edit the `/etc/kdump.conf`{.literal} configuration file:

    a.  Remove the hash sign (`#`{.literal}) from the beginning of the `#ext4`{.literal} line, depending on your choice.

        -   device name (the `#ext4 /dev/vg/lv_kdump`{.literal} line)
        -   file system label (the `#ext4 LABEL=/boot`{.literal} line)
        -   UUID (the `#ext4 UUID=03138356-5e61-4ab3-b58e-27507ac41937`{.literal} line)

    b.  Change the file system type and the device name, label or UUID, to the required values. The correct syntax for specifying UUID values is both `UUID="correct-uuid"`{.literal} and `UUID=correct-uuid`{.literal}. For example:

        ``` {.language-plaintext tabindex="-1"}
        ext4 UUID=03138356-5e61-4ab3-b58e-27507ac41937
        ```

        Important

        You must specify storage devices by using a `LABEL=`{.literal} or `UUID=`{.literal}. Disk device names such as `/dev/sda3`{.literal} are not guaranteed to be consistent across reboot.

        When you use Direct Access Storage Device (DASD) on IBM Z hardware, verify the dump device configuration. Ensure the dump devices are correctly specified in `/etc/dasd.conf`{.literal} before proceeding with `kdump`{.literal}.

-   To write the crash dump directly to a device, edit the `/etc/kdump.conf`{.literal} configuration file:

    a.  Remove the hash sign (`#`{.literal}) from the beginning of the `#raw /dev/vg/lv_kdump`{.literal} line.

    b.  Replace the value with the intended device name. For example:

        ``` {.language-plaintext tabindex="-1"}
        raw /dev/sdb1
        ```

-   To store the crash dump to a remote machine by using the `NFS`{.literal} protocol:

    a.  Remove the hash sign (`#`{.literal}) from the beginning of the `#nfs my.server.com:/export/tmp`{.literal} line.

    b.  Replace the value with a valid hostname and directory path. For example:

        ``` {.language-plaintext tabindex="-1"}
        nfs penguin.example.com:/export/cores
        ```

    c.  Restart the `kdump`{.literal} service for the changes to take effect:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo systemctl restart kdump.service
        ```

        Note

        When you use the NFS directive to specify the NFS target, `kdump.service`{.literal} automatically attempts to mount the target. This mount verifies the available disk space. There is no need to mount the NFS target in advance. To prevent `kdump.service`{.literal} from mounting the target, use the `dracut_args --mount`{.literal} directive in `kdump.conf`{.literal}. This enables `kdump.service`{.literal} to call the `dracut`{.literal} utility with the `--mount`{.literal} argument to specify the NFS target.

-   To store the crash dump to a remote machine by using the SSH protocol:

    a.  Remove the hash sign (`#`{.literal}) from the beginning of the `#ssh user@my.server.com`{.literal} line.

    b.  Replace the value with a valid username and hostname.

    c.  Include your SSH key in the configuration.

        i.  Remove the hash sign from the beginning of the `#sshkey /root/.ssh/kdump_id_rsa`{.literal} line.

        ii. Change the value to the location of a key valid on the server you are trying to dump to. For example:

            ``` {.language-plaintext tabindex="-1"}
            ssh john@penguin.example.com
            sshkey /root/.ssh/mykey
            ```

**Additional resources**

-   [Files produced by kdump after system crash](#files-produced-by-kdump-after-system-crash "17.9. Files produced by kdump after system crash")

### [17.4. Understanding the kdump core collector](#understanding-the-kdump-core-collector) {#understanding-the-kdump-core-collector .title}

The `core_collector`{.literal} directive in `/etc/kdump.conf`{.literal} runs the `makedumpfile`{.literal} utility with options that control crash dump compression, page filtering, and log output during collection.

The `makedumpfile`{.literal} utility is the default core collector in Red Hat Enterprise Linux. It reduces crash dump size by compressing data and excluding unnecessary pages.

During crash dump collection, `makedumpfile`{.literal} can do the following:

-   Compress the crash dump file and copy only necessary pages by using various dump levels
-   Exclude unnecessary crash dump pages
-   Filter the page types to include in the crash dump

Note

Crash dump file compression is enabled by default.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    core_collector makedumpfile -l --message-level 1 -d 31
    ```

Options

:   -   `-c`{.literal}, `-l`{.literal}, `-p`{.literal}, or `-z`{.literal}: Specify the compressed dump file format for each page. Use `zlib`{.literal} for `-c`{.literal}, `lzo`{.literal} for `-l`{.literal}, `snappy`{.literal} for `-p`{.literal}, or `zstd`{.literal} for `-z`{.literal}.
    -   `-d`{.literal} `(dump_level)`{.literal}: Exclude pages so that they are not copied to the dump file.
    -   `--message-level`{.literal}: Specify the message types. You can restrict output by setting `message_level`{.literal} with this option. For example, `message_level`{.literal} 7 prints common messages and error messages. The maximum value of `message_level`{.literal} is 31.

**Additional resources**

-   [Configure the kdump core collector](#configuring-the-kdump-core-collector "17.5. Configuring the kdump core collector")
-   [Supported kdump filtering levels](#supported-kdump-filtering-levels "19.4. Supported kdump filtering levels")

### [17.5. Configuring the kdump core collector](#configuring-the-kdump-core-collector) {#configuring-the-kdump-core-collector .title}

Set the `core_collector`{.literal} line in `/etc/kdump.conf`{.literal} to control how `makedumpfile`{.literal} collects and compresses crash dumps.

The `makedumpfile`{.literal} utility reduces the size of crash dump files by:

-   Compressing pages and copying only necessary data by using various dump levels.
-   Excluding unnecessary crash dump pages.
-   Filtering the page types to be included in the crash dump.

Note

Crash dump file compression is enabled by default.

If you need to customize the crash dump file compression, follow this procedure.

Syntax

:   

``` {.language-plaintext tabindex="-1"}
core_collector makedumpfile -l --message-level 1 -d 31
```

Options

:   -   `-c`{.literal}, `-l`{.literal} or `-p`{.literal}: specify compress dump file format by each page using either, `zlib`{.literal} for `-c`{.literal} option, `lzo`{.literal} for `-l`{.literal} option, `snappy`{.literal} for `-p`{.literal} option or `zstd`{.literal} for `-z`{.literal} option.
    -   `-d`{.literal} `(dump_level)`{.literal}: excludes pages so that they are not copied to the dump file.
    -   `--message-level`{.literal} : specify the message types. You can restrict outputs printed by specifying `message_level`{.literal} with this option. For example, specifying 7 as `message_level`{.literal} prints common messages and error messages. The maximum value of `message_level`{.literal} is 31.

**Prerequisites**

-   You have root permissions on the system.
-   Fulfilled requirements for `kdump`{.literal} configurations and targets. For details, see [Supported kdump configurations and targets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/supported-kdump-configurations-and-targets).

**Procedure**

1.  As a `root`{.literal}, edit the `/etc/kdump.conf`{.literal} configuration file. Remove the hash sign (\"#\") from the beginning of the `#core_collector makedumpfile -l --message-level 1 -d 31`{.literal} line.

2.  Enter the following command to enable crash dump file compression:

    ``` {.language-plaintext tabindex="-1"}
    core_collector makedumpfile -l --message-level 1 -d 31
    ```

    The `-l`{.literal} option sets the compressed file format to LZO. The `-d`{.literal} option sets the dump level to 31. The `--message-level`{.literal} option sets the message level to 1. You can also use the `-c`{.literal}, `-p`{.literal}, or `-z`{.literal} options to specify other compression formats.

    See `makedumpfile(8)`{.literal} man page on your system for more information.

### [17.6. Configuring the kdump default failure responses](#configuring-the-kdump-default-failure-responses) {#configuring-the-kdump-default-failure-responses .title}

To configure the default failure response for `kdump`{.literal}, specify an action other than the default reboot. This determines the system behavior when saving the core dump fails.

The additional actions include the following options:

`dump_to_rootfs`{.literal}
:   Saves the core dump to the `root`{.literal} file system.

`reboot`{.literal}
:   Reboots the system, losing the core dump in the process.

`halt`{.literal}
:   Stops the system, losing the core dump in the process.

`poweroff`{.literal}
:   Power the system off, losing the core dump in the process.

`shell`{.literal}
:   Runs a shell session from within the `initramfs`{.literal}, you can record the core dump manually.

`final_action`{.literal}
:   Enables additional operations such as `reboot`{.literal}, `halt`{.literal}, and `poweroff`{.literal} after a successful `kdump`{.literal} or when shell or `dump_to_rootfs`{.literal} failure action completes. The default is `reboot`{.literal}.

`failure_action`{.literal}
:   Specifies the action to perform when a dump might fail in a kernel crash. The default is `reboot`{.literal}.

**Prerequisites**

-   You have root permissions on the system.
-   You have fulfilled requirements for `kdump`{.literal} configurations and targets.

**Procedure**

1.  As a `root`{.literal} user, remove the hash sign (`#`{.literal}) from the beginning of the `#failure_action`{.literal} line in the `/etc/kdump.conf`{.literal} configuration file.

2.  Replace the value with a required action.

    ``` {.language-plaintext tabindex="-1"}
    failure_action poweroff
    ```

**Additional resources**

-   [Supported kdump configurations and targets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/supported-kdump-configurations-and-targets)
-   [Configuring the kdump target](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line#configuring-the-kdump-target)

### [17.7. Configuration file for kdump](#configuration-file-for-kdump) {#configuration-file-for-kdump .title}

The configuration file for `kdump`{.literal} kernel is `/etc/sysconfig/kdump`{.literal}. This file controls the `kdump`{.literal} kernel command line parameters. For most configurations, use the default options.

However, in some scenarios you might have to modify certain parameters to control the `kdump`{.literal} kernel behavior. For example, you can modify the `KDUMP_COMMANDLINE_APPEND`{.literal} option to append the `kdump`{.literal} kernel command-line for detailed debugging output. You can also modify the `KDUMP_COMMANDLINE_REMOVE`{.literal} option to remove arguments from the `kdump`{.literal} command line.

`KDUMP_COMMANDLINE_REMOVE`{.literal}

:   This option removes arguments from the current `kdump`{.literal} command line. It removes parameters that can cause `kdump`{.literal} errors or `kdump`{.literal} kernel boot failures. These parameters might have been parsed from the previous `KDUMP_COMMANDLINE`{.literal} process or inherited from the `/proc/cmdline`{.literal} file.

    When this variable is not configured, it inherits all values from the `/proc/cmdline`{.literal} file. Configuring this option also provides information that is helpful in debugging an issue.

    To remove certain arguments, add them to `KDUMP_COMMANDLINE_REMOVE`{.literal} as follows:

    ``` {.language-plaintext tabindex="-1"}
    # KDUMP_COMMANDLINE_REMOVE="hugepages hugepagesz slub_debug quiet log_buf_len swiotlb"
    ```

`KDUMP_COMMANDLINE_APPEND`{.literal}

:   This option appends arguments to the current command line. These arguments might have been parsed by the previous `KDUMP_COMMANDLINE_REMOVE`{.literal} variable.

    For the `kdump`{.literal} kernel, disabling certain modules such as `mce`{.literal}, `cgroup`{.literal}, `numa`{.literal}, `hest_disable`{.literal} can help prevent kernel errors. These modules can consume a significant part of the kernel memory reserved for `kdump`{.literal} or cause `kdump`{.literal} kernel boot failures.

    To disable memory cgroups on the `kdump`{.literal} kernel command line, run the command as follows:

    ``` {.language-plaintext tabindex="-1"}
    KDUMP_COMMANDLINE_APPEND="cgroup_disable=memory"
    ```

    See `/etc/sysconfig/kdump`{.literal} file for more information.

### [17.8. Testing the kdump configuration](#testing-the-kdump-configuration) {#testing-the-kdump-configuration .title}

After configuring `kdump`{.literal}, manually test a system crash and ensure that `kdump`{.literal} generates the `vmcore`{.literal} file in the defined target. The freshly booted kernel captures the `vmcore`{.literal} file, which contains critical information for debugging a kernel crash.

Warning

Do not test `kdump`{.literal} on active production systems. The commands to test `kdump`{.literal} cause the kernel to crash with data loss. Depending on your system architecture, schedule significant maintenance time. The `kdump`{.literal} testing might require several reboots with a long boot time.

If the `vmcore`{.literal} file is not generated during the `kdump`{.literal} test, identify and fix the issues. Then, run the test again to verify successful `kdump`{.literal} operation.

If you make any manual system modifications, you must test the `kdump`{.literal} configuration at the end of any system modification. For example, if you make any of the following changes, ensure that you test the `kdump`{.literal} configuration for optimal `kdump`{.literal} performance for:

-   Package upgrades.
-   Hardware level changes, for example, storage or networking changes.
-   Firmware upgrades.
-   New installation and application upgrades that include third party modules.
-   If you use the hot-plugging mechanism to add more memory on hardware that support this mechanism.
-   After you make changes in the `/etc/kdump.conf`{.literal} or `/etc/sysconfig/kdump`{.literal} file.

**Prerequisites**

-   You have root permissions on the system.
-   You have saved all important data. The commands to test `kdump`{.literal} cause the kernel to crash with loss of data.
-   You have scheduled significant machine maintenance time depending on the system architecture.

**Procedure**

1.  Enable the `kdump`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # kdumpctl restart
    ```

2.  Check the status of the `kdump`{.literal} service with the `kdumpctl`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # kdumpctl status
    ```

    ``` {.language-plaintext tabindex="-1"}
    kdump:Kdump is operational
    ```

    Optionally, if you use the `systemctl`{.literal} command, the output prints in the systemd journal.

3.  Start a kernel crash to test the `kdump`{.literal} configuration. The `sysrq-trigger`{.literal} key combination causes the kernel to crash and might reboot the system if required.

    ``` {.language-plaintext tabindex="-1"}
    # echo c > /proc/sysrq-trigger
    ```

    On a kernel reboot, the *`address`{.literal}*`-`{.literal}*`YYYY-MM-DD`{.literal}*`-`{.literal}*`HH:MM:SS`{.literal}*`/vmcore`{.literal} file is created at the location you have specified in the `/etc/kdump.conf`{.literal} file. The default is `/var/crash/`{.literal}.

**Additional resources**

-   [Configuring the kdump target](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line#configuring-the-kdump-target)

### [17.9. Files produced by kdump after system crash](#files-produced-by-kdump-after-system-crash) {#files-produced-by-kdump-after-system-crash .title}

After your system crashes, the `kdump`{.literal} service captures the kernel memory in a dump file (`vmcore`{.literal}). The service also generates diagnostic files to aid in troubleshooting and postmortem analysis.

Files produced by `kdump`{.literal}:

-   `vmcore`{.literal} - main kernel memory dump file containing system memory at the time of the crash. It includes data according to the configuration of the `core_collector`{.literal} program specified in `kdump`{.literal} configuration. By default, it includes the kernel data structures, process information, stack traces, and other diagnostic information.
-   `vmcore-dmesg.txt`{.literal} - contents of the kernel ring buffer log (`dmesg`{.literal}) from the primary kernel that panicked.
-   `kexec-dmesg.log`{.literal} - kernel and system log messages from the capture kernel while it collects the `vmcore`{.literal} data.

**Additional resources**

-   [What is the kernel ring buffer](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/getting-started-with-kernel-logging#what-is-the-kernel-ring-buffer)

### [17.10. Enabling and disabling the kdump service](#enabling-and-disabling-the-kdump-service) {#enabling-and-disabling-the-kdump-service .title}

To manage `kdump`{.literal} functionality on specific or all installed kernels, you can enable or disable it. Routine testing is required to validate that `kdump`{.literal} operates correctly.

**Prerequisites**

-   You have root permissions on the system.
-   You have completed `kdump`{.literal} requirements for configurations and targets. See [Supported kdump configurations and targets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/supported-kdump-configurations-and-targets).
-   All configurations for installing `kdump`{.literal} are set up as required.

**Procedure**

1.  Enable the `kdump`{.literal} service for `multi-user.target`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable kdump.service
    ```

2.  Start the service in the current session:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start kdump.service
    ```

3.  Stop the `kdump`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop kdump.service
    ```

4.  Disable the `kdump`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl disable kdump.service
    ```

    Warning

    It is advisable to set `kptr_restrict=1`{.literal} as default. When `kptr_restrict`{.literal} is set to (1) as default, the `kdumpctl`{.literal} service loads the crash kernel regardless of Kernel Address Space Layout (`KASLR`{.literal}) is enabled.

    If `kptr_restrict`{.literal} is not set to `1`{.literal} and KASLR is enabled, the contents of `/proc/kore`{.literal} file are generated as all zeros. The `kdumpctl`{.literal} service fails to access the `/proc/kcore`{.literal} file and load the crash kernel. The `kexec-kdump-howto.txt`{.literal} file displays a warning message to set `kptr_restrict=1`{.literal}. Verify for the following in the `sysctl.conf`{.literal} file to ensure that `kdumpctl`{.literal} service loads the crash kernel:

    -   Kernel `kptr_restrict=1`{.literal} in the `sysctl.conf`{.literal} file.

### [17.11. Preventing kernel drivers from loading for kdump](#preventing-kernel-drivers-from-loading-for-kdump) {#preventing-kernel-drivers-from-loading-for-kdump .title}

To prevent specific kernel drivers from loading in the capture kernel, use the `KDUMP_COMMANDLINE_APPEND=`{.literal} variable in `/etc/sysconfig/kdump`{.literal}. This stops the `kdump`{.literal} initramfs from loading modules, helping to avoid out-of-memory (OOM) errors and other crash kernel failures.

You can append the `KDUMP_COMMANDLINE_APPEND=`{.literal} variable by using one of the following configuration options:

-   `rd.driver.blacklist=`{.literal}*`<modules>`{.literal}*
-   `modprobe.blacklist=`{.literal}*`<modules>`{.literal}*

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Display the list of modules that are loaded to the currently running kernel. Select the kernel module that you intend to block from loading:

    ``` {.language-plaintext tabindex="-1"}
    $ lsmod
    ```

    ``` {.language-plaintext tabindex="-1"}
    Module                  Size  Used by
    fuse                  126976  3
    xt_CHECKSUM            16384  1
    ipt_MASQUERADE         16384  1
    uinput                 20480  1
    xt_conntrack           16384  1
    ```

2.  Update the `KDUMP_COMMANDLINE_APPEND=`{.literal} variable in the `/etc/sysconfig/kdump`{.literal} file. For example:

    ``` {.language-plaintext tabindex="-1"}
    KDUMP_COMMANDLINE_APPEND="rd.driver.blacklist=hv_vmbus,hv_storvsc,hv_utils,hv_netvsc,hid-hyperv"
    ```

    Also, consider the following example by using the `modprobe.blacklist=`{.literal}*`<modules>`{.literal}* configuration option:

    ``` {.language-plaintext tabindex="-1"}
    KDUMP_COMMANDLINE_APPEND="modprobe.blacklist=emcp modprobe.blacklist=bnx2fc modprobe.blacklist=libfcoe modprobe.blacklist=fcoe"
    ```

3.  Restart the `kdump`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart kdump
    ```

    See the `dracut.cmdline`{.literal} man page on your system for more information.

### [17.12. Running kdump on systems with encrypted disk](#running-kdump-on-systems-with-encrypted-disk) {#running-kdump-on-systems-with-encrypted-disk .title}

To run `kdump`{.literal} on systems with LUKS encrypted partitions, ensure sufficient available memory. Insufficient memory causes `cryptsetup`{.literal} to fail mounting the partition, preventing `vmcore`{.literal} capture in the second kernel (capture kernel).

The `kdumpctl estimate`{.literal} command helps you estimate the amount of memory you need for `kdump`{.literal}. `kdumpctl estimate`{.literal} prints the `crashkernel`{.literal} value, which is the most suitable memory size required for `kdump`{.literal}.

The `crashkernel`{.literal} value is calculated based on the current kernel size, kernel module, initramfs, and the LUKS encrypted target memory requirement.

If you are using the custom `crashkernel=`{.literal} option, `kdumpctl estimate`{.literal} prints the `LUKS required size`{.literal} value. The value is the memory size required for LUKS encrypted target.

**Procedure**

1.  Print the estimate `crashkernel=`{.literal} value:

    ``` {.language-plaintext tabindex="-1"}
    # kdumpctl estimate
    ```

    ``` {.language-plaintext tabindex="-1"}
    Encrypted kdump target requires extra memory, assuming using the keyslot with minimum memory requirement
       Reserved crashkernel:    256M
       Recommended crashkernel: 652M

       Kernel image size:   47M
       Kernel modules size: 8M
       Initramfs size:      20M
       Runtime reservation: 64M
       LUKS required size:  512M
       Large modules: <none>
       WARNING: Current crashkernel size is lower than recommended size 652M.
    ```

2.  Configure the amount of required memory by increasing the `crashkernel=`{.literal} value.

3.  Reboot the system.

    Note

    If the `kdump`{.literal} service still fails to save the dump file to the encrypted target, increase the `crashkernel=`{.literal} value as required.

## [Chapter 18. Enabling kdump](#enabling-kdump) {#chapter-18.-enabling-kdump .title}

Enable or disable `kdump`{.literal} functionality on a specific kernel or all installed kernels in Red Hat Enterprise Linux. Test and validate the `kdump`{.literal} functionality regularly to ensure it works correctly.

### [18.1. Enabling kdump for all installed kernels](#enabling-kdump-for-all-installed-kernels) {#enabling-kdump-for-all-installed-kernels .title}

To enable the `kdump`{.literal} service for all kernels installed on the machine, enable `kdump.service`{.literal} after the `kdump-utils`{.literal} package is installed.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Add the `crashkernel=`{.literal} command-line parameter to all installed kernels:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=ALL --args="crashkernel=xxM"
    ```

    `xxM`{.literal} is the required memory in megabytes.

2.  For Unified Kernel Images (UKI), add the `crashkernel=`{.literal} command-line parameter to all installed UKIs. Copy the add-on associated with the required argument from `/lib/modules/$(uname -r)/vmlinuz-virt.efi.extra.d/`{.literal} to `/boot/efi/loader/addons/`{.literal}.

3.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

4.  Enable the `kdump`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now kdump.service
    ```

**Verification**

-   Check that the `kdump`{.literal} service is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status kdump.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    kdump.service - Crash recovery kernel arming
         Loaded: loaded (/usr/lib/systemd/system/kdump.service; enabled; vendor preset: disabled)
         Active: active (live)
    ```

### [18.2. Enabling kdump for a specific installed kernel](#enabling-kdump-for-a-specific-installed-kernel) {#enabling-kdump-for-a-specific-installed-kernel .title}

To enable the `kdump`{.literal} service for a specific installed kernel, configure the `crashkernel`{.literal} parameter in Grand Unified Bootloader (GRUB). Select the target kernel and enable the service to capture crash dumps.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  List the kernels installed on the machine:

    ``` {.language-plaintext tabindex="-1"}
    # ls -a /boot/vmlinuz-*
    ```

    ``` {.language-plaintext tabindex="-1"}
    /boot/vmlinuz-0-rescue-2930657cd0dc43c2b75db480e5e5b4a9
    /boot/vmlinuz-6.12.0-55.9.1.el10_0.x86_64
    /boot/vmlinuz-6.12.0-55.9.1.el10_0.x86_64
    ```

2.  Add a specific `kdump`{.literal} kernel to the system's Grand Unified Boot Loader (GRUB) configuration:

    For example:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=vmlinuz-6.12.0-55.9.1.el10_0.x86_64 --args="crashkernel=xxM"
    ```

    `xxM`{.literal} is the required memory reserve in megabytes.

3.  For Unified Kernel Images (UKI), add the `crashkernel=`{.literal} command-line parameter to a specific UKI. Copy the add-on associated with the required argument from `/lib/modules/$(uname -r)/vmlinuz-virt.efi.extra.d/`{.literal} to `/boot/efi/EFI/Linux/`{.literal}*`<machine-id>`{.literal}*`-`{.literal}*`<kernel-version>`{.literal}*`.efi.extra.d/`{.literal}.

4.  Enable the `kdump`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now kdump.service
    ```

**Verification**

-   Check that the `kdump`{.literal} service is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status kdump.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    kdump.service - Crash recovery kernel arming
         Loaded: loaded (/usr/lib/systemd/system/kdump.service; enabled; vendor preset: disabled)
         Active: active (live)
    ```

### [18.3. Disabling the kdump service](#disabling-the-kdump-service) {#disabling-the-kdump-service .title}

You can stop the `kdump`{.literal} service and disable the service from starting on your Red Hat Enterprise Linux systems.

**Prerequisites**

-   Fulfilled requirements for `kdump`{.literal} configurations and targets.

**Procedure**

1.  To stop the `kdump`{.literal} service in the current session:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop kdump.service
    ```

2.  To disable the `kdump`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl disable kdump.service
    ```

    Warning

    You must set `kptr_restrict=1`{.literal} as default. When `kptr_restrict`{.literal} is set to (1) as default, the `kdumpctl`{.literal} service loads the crash kernel regardless of whether the Kernel Address Space Layout (`KASLR`{.literal}) is enabled.

    If `kptr_restrict`{.literal} is not set to `1`{.literal} and `KASLR`{.literal} is enabled, the contents of `/proc/kore`{.literal} file are generated as all zeros. The `kdumpctl`{.literal} service fails to access the `/proc/kcore`{.literal} file and load the crash kernel. The `kexec-kdump-howto.txt`{.literal} file displays a warning message, which suggest you to set `kptr_restrict=1`{.literal}. Verify for the following in the `sysctl.conf`{.literal} file to ensure that `kdumpctl`{.literal} service loads the crash kernel:

    -   Kernel `kptr_restrict=1`{.literal} in the `sysctl.conf`{.literal} file.

**Additional resources**

-   [Supported kdump configurations and targets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/supported-kdump-configurations-and-targets)
-   [Using systemd unit files to customize and optimize your system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/index)

## [Chapter 19. Supported kdump configurations and targets](#supported-kdump-configurations-and-targets) {#chapter-19.-supported-kdump-configurations-and-targets .title}

The `kdump`{.literal} mechanism generates crash dump files when kernel crashes occur, providing critical information for root cause analysis. Identify supported configurations and targets, configure `kdump`{.literal}, and verify its operation on Red Hat Enterprise Linux systems.

### [19.1. Memory requirements for kdump](#memory-requirements-for-kdump) {#memory-requirements-for-kdump .title}

`kdump`{.literal} requires permanently reserved system memory for a capture kernel to store crash dumps for analysis. The main kernel cannot access this memory.

The memory requirements vary based on certain system parameters. One of the major factors is the system's hardware architecture. To identify the exact machine architecture, such as Intel 64 and AMD64, also known as x86_64, and print it to standard output, use the following command:

``` {.language-plaintext tabindex="-1"}
$ uname -m
```

With the stated list of minimum memory requirements, you can set the appropriate memory size to automatically reserve a memory for `kdump`{.literal} on the latest available versions. The memory size depends on the system's architecture and total available physical memory.

+-----------------------------------------+----------------------+-------------------------+
| Architecture                            | Available Memory     | Minimum Reserved Memory |
+:========================================+:=====================+:========================+
| AMD64 and Intel 64 (`x86_64`{.literal}) | 2 GB to 64 GB        | 256 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
|                                         | 64 GB and more       | 512 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
| 64-bit ARM (4k pages)                   | 1 GB to 4 GB         | 256 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
|                                         | 4 GB to 64 GB        | 320 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
|                                         | 64 GB and more       | 576 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
| 64-bit ARM (64k pages)                  | 1 GB to 4 GB         | 356 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
|                                         | 4 GB to 64 GB        | 420 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
|                                         | 64 GB and more       | 676 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
| IBM Power Systems (`ppc64le`{.literal}) | 2 GB to 4 GB         | 384 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
|                                         | 4 GB to 16 GB        | 512 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
|                                         | 16 GB to 64 GB       | 1 GB of RAM             |
+-----------------------------------------+----------------------+-------------------------+
|                                         | 64 GB to 128 GB      | 2 GB of RAM             |
+-----------------------------------------+----------------------+-------------------------+
|                                         | 128 GB and more      | 4 GB of RAM             |
+-----------------------------------------+----------------------+-------------------------+
| IBM Z (`s390x`{.literal})               | 2 GB to 64 GB        | 256 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+
|                                         | 64 GB and more       | 512 MB of RAM           |
+-----------------------------------------+----------------------+-------------------------+

: Table 19.1. Minimum amount of reserved memory required for kdump

Show more

On many systems, `kdump`{.literal} is able to estimate the amount of required memory and reserve it automatically. This behavior is enabled by default, but only works on systems that have more than a certain amount of total available memory, which varies based on the system architecture.

Important

The automatic configuration of reserved memory based on the total amount of memory in the system is a best effort estimation. The actual required memory might vary due to other factors such as I/O devices. Not using enough memory might cause debug kernel unable to boot as a capture kernel in the case of kernel panic. To avoid this problem, increase the crash kernel memory sufficiently.

**Additional resources**

-   [Red Hat Enterprise Linux Technology Capabilities and Limits](https://access.redhat.com/articles/rhel-limits)

### [19.2. Minimum threshold for automatic memory reservation](#minimum-threshold-for-automatic-memory-reservation) {#minimum-threshold-for-automatic-memory-reservation .title}

The `kdump-utils`{.literal} utility automatically reserves memory for `kdump`{.literal} by using the `crashkernel`{.literal} parameter. However, this requires a minimum amount of system memory, which varies by architecture. If your system's memory is less than the threshold, you must configure the reservation manually.

+-----------------------------------------+-----------------------------------+
| Architecture                            | Required Memory                   |
+:========================================+:==================================+
| AMD64 and Intel 64 (`x86_64`{.literal}) | 2 GB                              |
+-----------------------------------------+-----------------------------------+
| IBM Power Systems (`ppc64le`{.literal}) | 2 GB                              |
+-----------------------------------------+-----------------------------------+
| IBM  Z (`s390x`{.literal})              | 2 GB                              |
+-----------------------------------------+-----------------------------------+
| 64-bit ARM                              | 2 GB                              |
+-----------------------------------------+-----------------------------------+

: Table 19.2. Minimum amount of memory required for automatic memory reservation

Show more

Note

The `crashkernel=1G-4G:192M,4G-64G:256M,64G:512M`{.literal} option in the boot command line is no longer supported from RHEL 10.

### [19.3. Supported kdump targets](#supported-kdump-targets) {#supported-kdump-targets .title}

When a kernel crash occurs, the operating system saves the dump file on the configured or default target location. You can save the dump to a device, as a file on a local file system, or over a network. The following list shows which `kdump`{.literal} targets Red Hat Enterprise Linux currently supports or does not support.

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Target type          | Supported Targets                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Unsupported Targets                                                                                                                                     |
+:=====================+:========================================================================================================================================================================================================================================================================================================================================================================================================================================================================+:========================================================================================================================================================+
| Physical Storage     | -   Logical Volume Manager (LVM).                                                                                                                                                                                                                                                                                                                                                                                                                                       | -   BIOS RAID.                                                                                                                                          |
|                      | -   Thin provisioning volume.                                                                                                                                                                                                                                                                                                                                                                                                                                           | -   Software `iSCSI`{.literal} with `iBFT`{.literal}. Currently supported transports are `bnx2i`{.literal}, `cxgb3i`{.literal}, and `cxgb4i`{.literal}. |
|                      | -   Fibre Channel (FC) disks such as `qla2xxx`{.literal}, `lpfc`{.literal}, `bnx2fc`{.literal}, and `bfa`{.literal}.                                                                                                                                                                                                                                                                                                                                                    | -   Software iSCSI with hybrid device driver such as `be2iscsi`{.literal}.                                                                              |
|                      | -   An `iSCSI`{.literal} software-configured logical device on a networked storage server.                                                                                                                                                                                                                                                                                                                                                                              | -   Fibre Channel over Ethernet (`FCoE`{.literal}).                                                                                                     |
|                      | -   The `mdraid`{.literal} subsystem as a software `RAID`{.literal} solution.                                                                                                                                                                                                                                                                                                                                                                                           | -   Legacy IDE.                                                                                                                                         |
|                      | -   Hardware RAID such as `smartpqi`{.literal}, `hpsa`{.literal}, `megaraid`{.literal}, `mpt3sas`{.literal}, `aacraid`{.literal}, and `mpi3mr`{.literal}.                                                                                                                                                                                                                                                                                                               | -   `GlusterFS`{.literal} servers.                                                                                                                      |
|                      | -   `SCSI`{.literal} and `SATA`{.literal} disks.                                                                                                                                                                                                                                                                                                                                                                                                                        | -   `GFS2`{.literal} file system.                                                                                                                       |
|                      | -   `iSCSI`{.literal} and `HBA`{.literal} offloads.                                                                                                                                                                                                                                                                                                                                                                                                                     | -   Clustered Logical Volume Manager (CLVM).                                                                                                            |
|                      | -   Hardware `FCoE`{.literal} such as `qla2xxx`{.literal} and `lpfc`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                         | -   High availability LVM volumes (HA-LVM).                                                                                                             |
|                      | -   Software `FCoE`{.literal} such as `bnx2fc`{.literal}. For software `FCoE`{.literal} to function, additional memory configuration might be required.                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Network              | -   Hardware using kernel modules such as `igb`{.literal}, `ixgbe`{.literal}, `ice`{.literal}, `i40e`{.literal}, `e1000e`{.literal}, `igc`{.literal}, `tg3`{.literal}, `bnx2x`{.literal}, `bnxt_en`{.literal}, `qede`{.literal}, `cxgb4`{.literal}, `be2net`{.literal}, `enic`{.literal}, `sfc`{.literal}, `mlx4_en`{.literal}, `mlx5_core`{.literal}, `r8169`{.literal}, `atlantic`{.literal}, `nfp`{.literal}, and `nicvf`{.literal} on 64-bit ARM architecture only. | -   Hardware using kernel modules such as `sfc SRIOV`{.literal}, `cxgb4vf`{.literal}, and `pch_gbe`{.literal}.                                          |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | -   IPv6 protocol.                                                                                                                                      |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | -   Wireless connections.                                                                                                                               |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | -   InfiniBand networks.                                                                                                                                |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | -   VLAN network over bridge and team.                                                                                                                  |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hypervisor           | -   Kernel-based virtual machines (KVM).                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                         |
|                      | -   Xen hypervisor in certain configurations only.                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                         |
|                      | -   ESXi 6.6, 6.7, 7.0.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                         |
|                      | -   Hyper-V 2012 R2 on RHEL Gen1 UP Guest only and later version.                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Filesystem           | The `ext[234]fs`{.literal}, `XFS`{.literal}, `virtiofs`{.literal}, and NFS file systems.                                                                                                                                                                                                                                                                                                                                                                                | The `Btrfs`{.literal} file system.                                                                                                                      |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Firmware             | -   BIOS-based systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                         |
|                      | -   UEFI Secure Boot.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 19.3. kdump targets on RHEL 10

Show more

**Additional resources**

-   [Configuring the kdump target](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line#configuring-the-kdump-target)

### [19.4. Supported kdump filtering levels](#supported-kdump-filtering-levels) {#supported-kdump-filtering-levels .title}

To reduce dump file size, `kdump`{.literal} uses `makedumpfile`{.literal} to compress data and exclude unwanted information. See the table for supported filtering levels, such as excluding `hugepages`{.literal}.

+-----------------------------------+-----------------------------------+
| Option                            | Description                       |
+:==================================+:==================================+
| `1`{.literal .option}             | Zero pages                        |
+-----------------------------------+-----------------------------------+
| `2`{.literal .option}             | Cache pages                       |
+-----------------------------------+-----------------------------------+
| `4`{.literal .option}             | Cache private                     |
+-----------------------------------+-----------------------------------+
| `8`{.literal .option}             | User pages                        |
+-----------------------------------+-----------------------------------+
| `16`{.literal .option}            | Free pages                        |
+-----------------------------------+-----------------------------------+

: Table 19.4. Filtering levels for kdump

Show more

**Additional resources**

-   [Configuring the kdump core collector](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line#configuring-the-kdump-core-collector)

### [19.5. Supported default failure responses](#supported-default-failure-responses) {#supported-default-failure-responses .title}

By default, when `kdump`{.literal} fails to create a core dump, the operating system reboots. However, you can configure `kdump`{.literal} to perform a different operation in case it fails to save the core dump to the primary target.

`dump_to_rootfs`{.literal}
:   Attempt to save the core dump to the root file system. This option is especially useful in combination with a network target: if the network target is unreachable, this option configures kdump to save the core dump locally. The system is rebooted afterwards.

`reboot`{.literal}
:   Reboot the system, losing the core dump in the process.

`halt`{.literal}
:   Halt the system, losing the core dump in the process.

`poweroff`{.literal}
:   Power off the system, losing the core dump in the process.

`shell`{.literal}
:   Run a shell session from within the initramfs, allowing the user to record the core dump manually.

`final_action`{.literal}
:   Enable additional operations such as `reboot`{.literal}, `halt`{.literal}, and `poweroff`{.literal} actions after a successful `kdump`{.literal} or when `shell`{.literal} or `dump_to_rootfs`{.literal} failure action completes. The default `final_action`{.literal} option is `reboot`{.literal}.

`failure_action`{.literal}
:   Specifies the action to perform when a dump might fail in case of a kernel crash. The default `failure_action`{.literal} option is `reboot`{.literal}.

**Additional resources**

-   [Configuring the kdump default failure responses](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line#configuring-the-kdump-default-failure-responses)

### [19.6. Using final_action parameter](#using-final_action-parameter) {#using-final_action-parameter .title}

To perform operations such as `reboot`{.literal}, `halt`{.literal}, or `poweroff`{.literal} after `kdump`{.literal} succeeds or fails, use the `final_action`{.literal} parameter. The default action is `reboot`{.literal}.

**Procedure**

1.  To configure `final_action`{.literal}, edit the `/etc/kdump.conf`{.literal} file and add one of the following options:

    -   `final_action reboot`{.literal}
    -   `final_action halt`{.literal}
    -   `final_action poweroff`{.literal}

2.  Restart the `kdump`{.literal} service for the changes to take effect.

    ``` {.language-plaintext tabindex="-1"}
    # kdumpctl restart
    ```

### [19.7. Using failure_action parameter](#using-failure_action-parameter) {#using-failure_action-parameter .title}

To specify the action when a crash dump fails, use the `failure_action`{.literal} parameter. The default action is `reboot`{.literal}.

The parameter recognizes the following actions to take:

`reboot`{.literal}
:   Reboots the system after a dump failure.

`dump_to_rootfs`{.literal}
:   Saves the dump file on a root file system when a non-root dump target is configured.

`halt`{.literal}
:   Halts the system.

`poweroff`{.literal}
:   Stops the running operations on the system.

`shell`{.literal}
:   Starts a shell session inside `initramfs`{.literal}, from which you can manually perform additional recovery actions.

**Procedure**

1.  To configure an action to take if the dump fails, edit the `/etc/kdump.conf`{.literal} file and specify one of the `failure_action`{.literal} options:

    -   `failure_action reboot`{.literal}
    -   `failure_action halt`{.literal}
    -   `failure_action poweroff`{.literal}
    -   `failure_action shell`{.literal}
    -   `failure_action dump_to_rootfs`{.literal}

2.  Restart the `kdump`{.literal} service for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # kdumpctl restart
    ```

## [Chapter 20. Firmware assisted dump mechanisms](#firmware-assisted-dump-mechanisms) {#chapter-20.-firmware-assisted-dump-mechanisms .title}

Firmware assisted dump (`fadump`{.literal}) is an alternative to `kdump`{.literal} on IBM POWER systems. It uses onboard firmware to isolate memory regions and prevent accidental overwriting of crash analysis data. The `fadump`{.literal} utility is optimized for Red Hat Enterprise Linux on IBM POWER systems.

### [20.1. Firmware assisted dump on IBM PowerPC hardware](#firmware-assisted-dump-on-ibm-powerpc-hardware) {#firmware-assisted-dump-on-ibm-powerpc-hardware .title}

The `fadump`{.literal} utility captures `vmcore`{.literal} from a fully-reset system by using firmware to preserve memory during a crash. It reuses `kdump`{.literal} scripts to save the file. Preserved regions include all system memory except boot memory, registers, and hardware page tables.

The `fadump`{.literal} mechanism offers improved reliability over the traditional dump type, by rebooting the partition and using a new kernel to dump the data from the previous kernel crash. The `fadump`{.literal} requires an IBM POWER6 processor-based or later version hardware platform.

For further details about the `fadump`{.literal} mechanism, including PowerPC specific methods of resetting hardware, see the `/usr/share/doc/kdump-utils/fadump-howto.txt`{.literal} file.

Note

The area of memory that is not preserved, known as boot memory, is the amount of RAM required to successfully boot the kernel after a crash event. By default, the boot memory size is 256MB or 5% of total system RAM, whichever is larger.

Unlike `kexec-initiated`{.literal} event, the `fadump`{.literal} mechanism uses the production kernel to recover a crash dump. When booting after a crash, PowerPC hardware makes the device node `/proc/device-tree/rtas/ibm.kernel-dump`{.literal} available to the `proc`{.literal} filesystem (`procfs`{.literal}). The `fadump-aware kdump`{.literal} scripts, check for the stored `vmcore`{.literal}, and then complete the system reboot cleanly.

### [20.2. Enabling firmware assisted dump mechanism](#enabling-firmware-assisted-dump-mechanism) {#enabling-firmware-assisted-dump-mechanism .title}

To enhance the crash dumping capabilities of IBM POWER systems, enable the firmware assisted dump (`fadump`{.literal}) mechanism.

In the Secure Boot environment, the GRUB boot loader allocates a boot memory region, known as the Real Mode Area (RMA). The RMA has a size of 512 MB, divided among the boot components. If a component exceeds its size allocation, `GRUB`{.literal} fails with an out-of-memory (`OOM`{.literal}) error.

Warning

Do not enable firmware assisted dump (`fadump`{.literal}) mechanism in the Secure Boot environment on RHEL 9.1 and earlier versions. The GRUB boot loader fails with the following error:

``` {.language-plaintext tabindex="-1"}
error: ../../grub-core/kern/mm.c:376:out of memory.
Press any key to continue…
```

The system is recoverable only if you increase the default `initramfs`{.literal} size due to the `fadump`{.literal} configuration.

For information about workaround methods to recover the system, see the [System boot ends in GRUB Out of Memory (OOM)](https://www.ibm.com/support/pages/node/6846531) article.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Install the `kexec-tools`{.literal}, `kdump-utils`{.literal}, and `makedumpfile`{.literal} packages.

2.  Configure the default value for `crashkernel`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # kdumpctl reset-crashkernel --fadump=on --kernel=ALL
    ```

3.  Optional: Reserve boot memory instead of the default value:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel ALL --args="fadump=on crashkernel=xxM"
    ```

    `xxM`{.literal} is the required memory size in megabytes.

    Note

    When specifying boot configuration options, test the configurations by rebooting the kernel with `kdump`{.literal} enabled. If the `kdump`{.literal} kernel fails to boot, increase the `crashkernel`{.literal} value gradually to set an appropriate value.

4.  Reboot for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

### [20.3. Firmware assisted dump mechanisms on IBM Z hardware](#firmware-assisted-dump-mechanisms-on-ibm-z-hardware) {#firmware-assisted-dump-mechanisms-on-ibm-z-hardware .title}

Use firmware assisted dump mechanisms, such as `sadump`{.literal} and `VMDUMP`{.literal}, to capture the machine state on IBM Z systems. These tools operate during the early boot phase, so you can analyze system failures that occur before the `kdump`{.literal} service starts.

IBM Z systems support the following firmware assisted dump mechanisms:

-   `Stand-alone dump (sadump)`{.literal}
-   `VMDUMP`{.literal}

The `kdump`{.literal} infrastructure is supported and used on IBM Z systems. However, using one of the firmware assisted dump (`fadump`{.literal}) methods for IBM Z has the following benefits:

-   The system console initiates and controls the `sadump`{.literal} mechanism, and stores it on an `IPL`{.literal} bootable device.
-   The `VMDUMP`{.literal} mechanism is similar to `sadump`{.literal}. This tool is also initiated from the system console, but retrieves the resulting dump from hardware and copies it to the system for analysis.
-   These methods (similarly to other hardware based dump mechanisms) have the ability to capture the state of a machine in the early boot phase, before the `kdump`{.literal} service starts.
-   Although `VMDUMP`{.literal} contains a mechanism to receive the dump file into a Red Hat Enterprise Linux system, the configuration and control of `VMDUMP`{.literal} is managed from the IBM Z Hardware console.

**Additional resources**

-   [Stand-alone dump](https://www.ibm.com/docs/en/zos/2.3.0?topic=aids-stand-alone-dump)
-   [Creating dumps on z/VM with VMDUMP](https://www.ibm.com/docs/en/linux-on-systems?topic=85-zvm-dump-vmdump)

### [20.4. Using sadump on Fujitsu PRIMEQUEST systems](#using-sadump-on-fujitsu-primequest-systems) {#using-sadump-on-fujitsu-primequest-systems .title}

To capture a fallback dump when `kdump`{.literal} fails on Fujitsu PRIMEQUEST systems, use `sadump`{.literal}. Configure `kdump`{.literal} using the Management Board (`MMB`{.literal}) interface, then enable and manually start `sadump`{.literal}.

**Procedure**

1.  Add or edit the following lines in the `/etc/sysctl.conf`{.literal} file to ensure that `kdump`{.literal} starts as expected for `sadump`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    kernel.panic=0
    kernel.unknown_nmi_panic=1
    ```

    Warning

    In particular, ensure that after `kdump`{.literal}, the system does not reboot. If the system reboots after `kdump`{.literal} has failed to save the `vmcore`{.literal} file, then it is not possible to start the `sadump`{.literal}.

2.  Set the `failure_action`{.literal} parameter in `/etc/kdump.conf`{.literal} appropriately as `halt`{.literal} or `shell`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    failure_action shell
    ```

    See the FUJITSU Server PRIMEQUEST 2000 Series Installation Manual for more information.

## [Chapter 21. Analyzing a core dump](#analyzing-a-core-dump) {#chapter-21.-analyzing-a-core-dump .title}

The crash utility analyzes core dumps generated by the kdump, netdump, diskdump, or xendump mechanisms to identify system crash causes. It provides a GDB-like interactive prompt. Alternatively, use the Kernel Oops Analyzer or Kdump Helper tool.

### [21.1. Installing the crash utility](#installing-the-crash-utility) {#installing-the-crash-utility .title}

To analyze a system's state during runtime or after a kernel crash by examining the `vmcore`{.literal} dump file, install the `crash`{.literal} utility. This utility provides an interactive shell for debugging running systems and analyzing crash dumps.

**Procedure**

1.  Enable the relevant repositories:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable baseos repository
    ```

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable appstream repository
    ```

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable rhel-10-for-x86_64-baseos-debug-rpms
    ```

2.  Install the `crash`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install crash
    ```

3.  Install the `kernel-debuginfo`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kernel-debuginfo
    ```

    The package `kernel-debuginfo`{.literal} corresponds to the running kernel and provides the data necessary for the dump analysis.

### [21.2. Running and exiting the crash utility](#running-and-exiting-the-crash-utility) {#running-and-exiting-the-crash-utility .title}

To analyze a system crash and troubleshoot kernel-related problems, use the `crash`{.literal} utility on a `vmcore`{.literal} dump file. Use this tool to gain insights into the system's state at the time of the crash and identify the root cause of the issue.

**Prerequisites**

-   Identify the currently running kernel (for example `6.12.0-55.9.1.el10_0.x86_64`{.literal}).

**Procedure**

1.  To start the `crash`{.literal} utility, two necessary parameters need to be passed to the command:

    -   The debug-info (a decompressed vmlinuz image), for example `/usr/lib/debug/lib/modules/6.12.0-55.9.1.el10_0.x86_64/vmlinux`{.literal} provided through a specific `kernel-debuginfo`{.literal} package.

    -   The actual vmcore file, for example `/var/crash/127.0.0.1-2021-09-13-14:05:33/vmcore`{.literal}

        The resulting `crash`{.literal} command then looks:

        ``` {.language-plaintext tabindex="-1"}
        # crash /usr/lib/debug/lib/modules/6.12.0-55.9.1.el10_0.x86_64/vmlinux /var/crash/127.0.0.1-2021-09-13-14:05:33/vmcore
        ```

        Use the same *\<kernel\>* version that was captured by `kdump`{.literal}.

2.  Running the crash utility.

    The following example shows analyzing a core dump created using the 6.12.0-55.9.1.el10_0.x86_64 kernel.

    ``` {.language-plaintext tabindex="-1"}
    ...
    WARNING: kernel relocated [202MB]: patching 90160 gdb minimal_symbol values

          KERNEL: /usr/lib/debug/lib/modules/6.12.0-55.9.1.el10_0.x86_64/vmlinux
        DUMPFILE: /var/crash/127.0.0.1-2021-09-13-14:05:33/vmcore  [PARTIAL DUMP]
            CPUS: 2
            DATE: Mon Sep 13 14:05:16 2021
          UPTIME: 01:03:57
    LOAD AVERAGE: 0.00, 0.00, 0.00
           TASKS: 586
        NODENAME: localhost.localdomain
         RELEASE: 6.12.0-55.9.1.el10_0.x86_64
         VERSION: #1 SMP Wed Aug 29 11:51:55 UTC 2018
         MACHINE: x86_64  (2904 Mhz)
          MEMORY: 2.9 GB
           PANIC: "sysrq: SysRq : Trigger a crash"
             PID: 10635
         COMMAND: "bash"
            TASK: ffff8d6c84271800  [THREAD_INFO: ffff8d6c84271800]
             CPU: 1
           STATE: TASK_RUNNING (SYSRQ)

    crash>
    ```

3.  To exit the interactive prompt and stop the crash utility, type `exit`{.literal} or `q`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    crash> exit
    ~]#
    ```

    Note

    The `crash`{.literal} command is also used as a powerful tool for debugging a live system. However, you must use it with caution to avoid system-level issues.

**Additional resources**

-   [A Guide to Unexpected System Restarts](https://access.redhat.com/articles/206873)

### [21.3. Displaying various indicators in the crash utility](#displaying-various-indicators-in-the-crash-utility) {#displaying-various-indicators-in-the-crash-utility .title}

To display system indicators like the kernel message buffer, backtrace, process status, virtual memory info, and open files, use the `crash`{.literal} utility.

**Procedure**

-   To display the kernel message buffer, type the `log`{.literal} command at the interactive prompt:

    ``` {.language-plaintext tabindex="-1"}
    crash> log
    ... several lines omitted ...
    EIP: 0060:[<c068124f>] EFLAGS: 00010096 CPU: 2
    EIP is at sysrq_handle_crash+0xf/0x20
    EAX: 00000063 EBX: 00000063 ECX: c09e1c8c EDX: 00000000
    ESI: c0a09ca0 EDI: 00000286 EBP: 00000000 ESP: ef4dbf24
     DS: 007b ES: 007b FS: 00d8 GS: 00e0 SS: 0068
    Process bash (pid: 5591, ti=ef4da000 task=f196d560 task.ti=ef4da000)
    Stack:
     c068146b c0960891 c0968653 00000003 00000000 00000002 efade5c0 c06814d0
    <0> fffffffb c068150f b7776000 f2600c40 c0569ec4 ef4dbf9c 00000002 b7776000
    <0> efade5c0 00000002 b7776000 c0569e60 c051de50 ef4dbf9c f196d560 ef4dbfb4
    Call Trace:
     [<c068146b>] ? __handle_sysrq+0xfb/0x160
     [<c06814d0>] ? write_sysrq_trigger+0x0/0x50
     [<c068150f>] ? write_sysrq_trigger+0x3f/0x50
     [<c0569ec4>] ? proc_reg_write+0x64/0xa0
     [<c0569e60>] ? proc_reg_write+0x0/0xa0
     [<c051de50>] ? vfs_write+0xa0/0x190
     [<c051e8d1>] ? sys_write+0x41/0x70
     [<c0409adc>] ? syscall_call+0x7/0xb
    Code: a0 c0 01 0f b6 41 03 19 d2 f7 d2 83 e2 03 83 e0 cf c1 e2 04 09 d0 88 41 03 f3 c3 90 c7 05 c8 1b 9e c0 01 00 00 00 0f ae f8 89 f6 <c6> 05 00 00 00 00 01 c3 89 f6 8d bc 27 00 00 00 00 8d 50 d0 83
    EIP: [<c068124f>] sysrq_handle_crash+0xf/0x20 SS:ESP 0068:ef4dbf24
    CR2: 0000000000000000
    ```

    Type `help log`{.literal} for more information about the command usage.

    Note

    The kernel message buffer includes the most essential information about the system crash. It is always dumped first into the `vmcore-dmesg.txt`{.literal} file. If you fail to obtain the full `vmcore`{.literal} file, for example, due to insufficient space on the target location, you can obtain the required information from the kernel message buffer. By default, `vmcore-dmesg.txt`{.literal} is placed in the `/var/crash/`{.literal} directory.

-   To display the kernel stack trace, use the `bt`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    crash> bt
    PID: 5591   TASK: f196d560  CPU: 2   COMMAND: "bash"
     #0 [ef4dbdcc] crash_kexec at c0494922
     #1 [ef4dbe20] oops_end at c080e402
     #2 [ef4dbe34] no_context at c043089d
     #3 [ef4dbe58] bad_area at c0430b26
     #4 [ef4dbe6c] do_page_fault at c080fb9b
     #5 [ef4dbee4] error_code (via page_fault) at c080d809
        EAX: 00000063  EBX: 00000063  ECX: c09e1c8c  EDX: 00000000  EBP: 00000000
        DS:  007b      ESI: c0a09ca0  ES:  007b      EDI: 00000286  GS:  00e0
        CS:  0060      EIP: c068124f  ERR: ffffffff  EFLAGS: 00010096
     #6 [ef4dbf18] sysrq_handle_crash at c068124f
     #7 [ef4dbf24] __handle_sysrq at c0681469
     #8 [ef4dbf48] write_sysrq_trigger at c068150a
     #9 [ef4dbf54] proc_reg_write at c0569ec2
    #10 [ef4dbf74] vfs_write at c051de4e
    #11 [ef4dbf94] sys_write at c051e8cc
    #12 [ef4dbfb0] system_call at c0409ad5
        EAX: ffffffda  EBX: 00000001  ECX: b7776000  EDX: 00000002
        DS:  007b      ESI: 00000002  ES:  007b      EDI: b7776000
        SS:  007b      ESP: bfcb2088  EBP: bfcb20b4  GS:  0033
        CS:  0073      EIP: 00edc416  ERR: 00000004  EFLAGS: 00000246
    ```

    Type `bt `{.literal}*`<pid>`{.literal}* to display the backtrace of a specific process or type `help bt`{.literal} for more information about `bt`{.literal} usage.

-   To display the status of processes in the system, use the `ps`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    crash> ps
       PID    PPID  CPU   TASK    ST  %MEM     VSZ    RSS  COMM
    >     0      0   0  c09dc560  RU   0.0       0      0  [swapper]
    >     0      0   1  f7072030  RU   0.0       0      0  [swapper]
          0      0   2  f70a3a90  RU   0.0       0      0  [swapper]
    >     0      0   3  f70ac560  RU   0.0       0      0  [swapper]
          1      0   1  f705ba90  IN   0.0    2828   1424  init
    ... several lines omitted ...
       5566      1   1  f2592560  IN   0.0   12876    784  auditd
       5567      1   2  ef427560  IN   0.0   12876    784  auditd
       5587   5132   0  f196d030  IN   0.0   11064   3184  sshd
    >  5591   5587   2  f196d560  RU   0.0    5084   1648  bash
    ```

    Use `ps `{.literal}*`<pid>`{.literal}* to display the status of a single specific process. Use *help ps* for more information about `ps`{.literal} usage.

-   To display basic virtual memory information, type the `vm`{.literal} command at the interactive prompt:

    ``` {.language-plaintext tabindex="-1"}
    crash> vm
    PID: 5591   TASK: f196d560  CPU: 2   COMMAND: "bash"
       MM       PGD      RSS    TOTAL_VM
    f19b5900  ef9c6000  1648k    5084k
      VMA       START      END    FLAGS  FILE
    f1bb0310    242000    260000 8000875  /lib/ld-2.12.so
    f26af0b8    260000    261000 8100871  /lib/ld-2.12.so
    efbc275c    261000    262000 8100873  /lib/ld-2.12.so
    efbc2a18    268000    3ed000 8000075  /lib/libc-2.12.so
    efbc23d8    3ed000    3ee000 8000070  /lib/libc-2.12.so
    efbc2888    3ee000    3f0000 8100071  /lib/libc-2.12.so
    efbc2cd4    3f0000    3f1000 8100073  /lib/libc-2.12.so
    efbc243c    3f1000    3f4000 100073
    efbc28ec    3f6000    3f9000 8000075  /lib/libdl-2.12.so
    efbc2568    3f9000    3fa000 8100071  /lib/libdl-2.12.so
    efbc2f2c    3fa000    3fb000 8100073  /lib/libdl-2.12.so
    f26af888    7e6000    7fc000 8000075  /lib/libtinfo.so.5.7
    f26aff2c    7fc000    7ff000 8100073  /lib/libtinfo.so.5.7
    efbc211c    d83000    d8f000 8000075  /lib/libnss_files-2.12.so
    efbc2504    d8f000    d90000 8100071  /lib/libnss_files-2.12.so
    efbc2950    d90000    d91000 8100073  /lib/libnss_files-2.12.so
    f26afe00    edc000    edd000 4040075
    f1bb0a18   8047000   8118000 8001875  /bin/bash
    f1bb01e4   8118000   811d000 8101873  /bin/bash
    f1bb0c70   811d000   8122000 100073
    f26afae0   9fd9000   9ffa000 100073
    ... several lines omitted ...
    ```

    Use `vm `{.literal}*`<pid>`{.literal}* to display information about a single specific process, or use `help vm`{.literal} for more information about `vm`{.literal} usage.

-   To display information about open files, use the `files`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    crash> files
    PID: 5591   TASK: f196d560  CPU: 2   COMMAND: "bash"
    ROOT: /    CWD: /root
     FD    FILE     DENTRY    INODE    TYPE  PATH
      0  f734f640  eedc2c6c  eecd6048  CHR   /pts/0
      1  efade5c0  eee14090  f00431d4  REG   /proc/sysrq-trigger
      2  f734f640  eedc2c6c  eecd6048  CHR   /pts/0
     10  f734f640  eedc2c6c  eecd6048  CHR   /pts/0
    255  f734f640  eedc2c6c  eecd6048  CHR   /pts/0
    ```

    Use `files `{.literal}*`<pid>`{.literal}* to display files opened by only one selected process, or use `help files`{.literal} for more information about `files`{.literal} usage.

### [21.4. Using Kernel Oops Analyzer](#using-kernel-oops-analyzer) {#using-kernel-oops-analyzer .title}

To analyze crash dumps, use the Kernel Oops Analyzer. It compares `oops`{.literal} messages with known issues in the Knowledgebase.

**Prerequisites**

-   An `oops`{.literal} message is secured to feed the Kernel Oops Analyzer.

**Procedure**

1.  Access the Kernel Oops Analyzer tool.

2.  To diagnose a kernel crash issue, upload a kernel oops log generated in `vmcore`{.literal}.

    -   Alternatively, you can diagnose a kernel crash issue by providing a text message or a `vmcore-dmesg.txt`{.literal} as an input.

3.  Click `DETECT`{.literal} to compare the `oops`{.literal} message based on information from the `makedumpfile`{.literal} against known solutions.

**Additional resources**

-   [The Kernel Oops Analyzer](https://access.redhat.com/labs/kerneloopsanalyzer/)

### [21.5. The Kdump Helper tool](#the-kdump-helper-tool) {#the-kdump-helper-tool .title}

The Kdump Helper tool helps to set up the `kdump`{.literal} by using the provided information. Kdump Helper generates a configuration script based on your preferences. Initiating and running the script on your server sets up the `kdump`{.literal} service.

**Additional resources**

-   [Kdump Helper](https://access.redhat.com/labs/kdumphelper/wizard)

## [Chapter 22. Automating crash dump analysis](#automating-crash-dump-analysis) {#chapter-22.-automating-crash-dump-analysis .title}

After `kdump`{.literal} collects a `vmcore`{.literal} dump file, you can automate the analysis process by using the `crash`{.literal} utility together with `systemd`{.literal} path units. Instead of manually invoking the `crash`{.literal} utility after every reboot, you configure the system to detect new `vmcore`{.literal} files and analyze them automatically. A `systemd`{.literal} path unit monitors the `/var/crash/`{.literal} directory and a `systemd`{.literal} service unit triggers an analysis script. The script extracts diagnostic information such as kernel backtraces and forwards the results to a report file or logging service.

### [22.1. Creating a systemd path unit for vmcore detection](#creating-a-systemd-path-unit-for-vmcore-detection) {#creating-a-systemd-path-unit-for-vmcore-detection .title}

To automatically trigger crash dump analysis when `kdump`{.literal} saves a new `vmcore`{.literal} file, create a `systemd`{.literal} path unit. This unit monitors the `/var/crash/`{.literal} directory and activates the `vmcore-analysis.service`{.literal} unit when new crash dump directories appear.

**Prerequisites**

-   The `kdump`{.literal} service is installed and enabled.
-   The `crash`{.literal} and `kernel-debuginfo`{.literal} packages are installed.
-   The `kdump`{.literal} target directory is set to `/var/crash/`{.literal}, which is the default.

**Procedure**

1.  Create the `systemd`{.literal} path unit file `/etc/systemd/system/vmcore-analysis.path`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [Unit]
    Description=Monitor /var/crash for new vmcore dumps

    [Path]
    DirectoryNotEmpty=/var/crash
    MakeDirectory=yes

    [Install]
    WantedBy=multi-user.target
    ```

2.  Create the matching `systemd`{.literal} service unit file `/etc/systemd/system/vmcore-analysis.service`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [Unit]
    Description=Analyze new vmcore crash dumps
    After=kdump.service

    [Service]
    Type=oneshot
    ExecStart=/usr/local/bin/vmcore-analyze.sh
    ```

3.  Reload the `systemd`{.literal} daemon to register the new units:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

4.  Enable and start the path unit:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now vmcore-analysis.path
    ```

**Verification**

1.  Verify that the path unit is active and monitoring:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status vmcore-analysis.path
    ```

    The output shows `active (waiting)`{.literal} if the unit is monitoring correctly.

2.  Optional: Test the trigger by simulating a crash dump with `kdump`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # echo c > /proc/sysrq-trigger
    ```

    After the system reboots and the `vmcore`{.literal} file is saved to `/var/crash/`{.literal}, the `vmcore-analysis.service`{.literal} unit activates automatically.

3.  Check that the analysis service ran after the reboot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status vmcore-analysis.service
    ```

    Note

    The `DirectoryNotEmpty`{.literal} directive triggers the service whenever the `/var/crash/`{.literal} directory is non-empty. If previous crash dumps remain in the directory, the `vmcore-analysis.service`{.literal} unit triggers on every reboot. To avoid repeated triggers, configure the `/usr/local/bin/vmcore-analyze.sh`{.literal} script to process only unanalyzed dumps and, optionally, move or archive processed dumps after analysis. For details about path unit directives, see the `systemd.path(5)`{.literal} man page.

**Additional resources**

-   [Scripting `crash`{.literal} utility commands for `vmcore`{.literal} analysis](#scripting-crash-utility-commands-for-vmcore-analysis "22.2. Scripting crash utility commands for vmcore analysis")

### [22.2. Scripting crash utility commands for vmcore analysis](#scripting-crash-utility-commands-for-vmcore-analysis) {#scripting-crash-utility-commands-for-vmcore-analysis .title}

To analyze `vmcore`{.literal} crash dumps without manual interaction, create a script that invokes the `crash`{.literal} utility in batch mode. The script locates the latest dump, identifies the matching debug kernel, runs a predefined set of diagnostic commands, and saves the output to a report file.

**Prerequisites**

-   The `crash`{.literal} package is installed.
-   The `kernel-debuginfo`{.literal} package matching the kernel that produced the `vmcore`{.literal} is installed.
-   The `vmcore`{.literal} file exists in a subdirectory of `/var/crash/`{.literal}.

**Procedure**

1.  Create the analysis script at `/usr/local/bin/vmcore-analyze.sh`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    #!/bin/bash

    CRASH_DIR="/var/crash"
    REPORT_SUFFIX="crash-report.txt"

    for dump_dir in "$CRASH_DIR"/*/; do
        vmcore="$dump_dir/vmcore"
        report="$dump_dir/$REPORT_SUFFIX"

        # Skip directories without a vmcore or already analyzed
        [ -f "$vmcore" ] || continue
        [ -f "$report" ] && continue

        # Determine the kernel version from the vmcore-dmesg.txt
        dmesg_file="$dump_dir/vmcore-dmesg.txt"
        if [ -f "$dmesg_file" ]; then
            kver=$(grep -oP 'Linux version \K[^ ]+' "$dmesg_file" | head -1)
        fi

        # Fall back to the currently running kernel if detection fails
        kver="${kver:-$(uname -r)}"

        vmlinux="/usr/lib/debug/lib/modules/$kver/vmlinux"

        if [ ! -f "$vmlinux" ]; then
            echo "ERROR: vmlinux not found for kernel $kver" > "$report"
            continue
        fi

        # Run crash in batch mode with diagnostic commands
        crash "$vmlinux" "$vmcore" --minimal << 'CRASH_CMDS' > "$report" 2>&1
    sys
    bt -a
    log
    ps
    mod
    exit
    CRASH_CMDS

        echo "Analysis complete: $report"
    done
    ```

2.  Make the script executable:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 755 /usr/local/bin/vmcore-analyze.sh
    ```

3.  Optional: Run the script manually to verify it works against an existing `vmcore`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # /usr/local/bin/vmcore-analyze.sh
    ```

**Verification**

-   Confirm that a `crash-report.txt`{.literal} file was generated in the crash dump directory:

    ``` {.language-plaintext tabindex="-1"}
    # ls /var/crash/<host-timestamp>/crash-report.txt
    ```

-   Review the report content to verify that backtrace and system information were captured:

    ``` {.language-plaintext tabindex="-1"}
    # head -50 /var/crash/<host-timestamp>/crash-report.txt
    ```

    Note

    The `--minimal`{.literal} flag starts the `crash`{.literal} utility without loading all kernel module debug data, which reduces startup time for automated batch analysis. If your diagnostic commands require full module symbols, remove the `--minimal`{.literal} flag.

**Additional resources**

-   [Running and exiting the crash utility](#running-and-exiting-the-crash-utility "21.2. Running and exiting the crash utility")
-   [Displaying various indicators in the crash utility](#displaying-various-indicators-in-the-crash-utility "21.3. Displaying various indicators in the crash utility")
-   [Creating a `systemd`{.literal} path unit for `vmcore`{.literal} detection](#creating-a-systemd-path-unit-for-vmcore-detection "22.1. Creating a systemd path unit for vmcore detection")

### [22.3. Extracting backtraces from vmcore programmatically](#extracting-backtraces-from-vmcore-programmatically) {#extracting-backtraces-from-vmcore-programmatically .title}

To extract specific backtrace information from a `vmcore`{.literal} crash dump and forward it to logging infrastructure, use the `crash`{.literal} utility with a targeted command file. This approach produces concise, parseable output suitable for alerting systems, log aggregators, or automated bug-reporting workflows.

**Prerequisites**

-   The `crash`{.literal} package is installed.
-   The `kernel-debuginfo`{.literal} package matching the crashed kernel is installed.
-   A `vmcore`{.literal} file exists in `/var/crash/`{.literal}.

**Procedure**

1.  Create a `crash`{.literal} command file at `/usr/local/share/vmcore-backtrace.cmd`{.literal} that extracts only the panic backtrace:

    ``` {.language-plaintext tabindex="-1"}
    bt
    bt -l
    sys
    exit
    ```

2.  Run the `crash`{.literal} utility with the command file to extract the backtrace from a specific `vmcore`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # crash /usr/lib/debug/lib/modules/<kernel-version>/vmlinux /var/crash/<host-timestamp>/vmcore < /usr/local/share/vmcore-backtrace.cmd > /var/crash/<host-timestamp>/backtrace.txt 2>&1
    ```

    Replace *\<kernel-version\>* with the version of the kernel that crashed and *\<host-timestamp\>* with the crash dump directory name.

3.  Forward the extracted backtrace to the system journal. For details about journal options, see the `journalctl(1)`{.literal} man page.

    ``` {.language-plaintext tabindex="-1"}
    # systemd-cat -t vmcore-analysis -p err < /var/crash/<host-timestamp>/backtrace.txt
    ```

4.  Query the journal for crash analysis entries:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -t vmcore-analysis --no-pager
    ```

5.  Optional: Configure `/etc/rsyslog.d/vmcore-forward.conf`{.literal} to forward the backtrace to a remote `syslog`{.literal} server. For details about configuration syntax, see the `rsyslog.conf(5)`{.literal} man page.

    ``` {.language-plaintext tabindex="-1"}
    if $programname == 'vmcore-analysis' then @@loghost.example.com:514
    ```

    Restart the `rsyslog`{.literal} service to apply the change:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart rsyslog
    ```

**Verification**

-   Verify that the backtrace file contains the expected panic trace:

    ``` {.language-plaintext tabindex="-1"}
    # grep -c "crash_kexec\|die\|oops_end" /var/crash/<host-timestamp>/backtrace.txt
    ```

    A non-zero count confirms that crash-related frames were captured.

-   Confirm the journal received the analysis output:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -t vmcore-analysis --since today
    ```

    Note

    For integration with `abrt`{.literal} (Automatic Bug Reporting Tool), place the backtrace output in a format compatible with `abrt-server`{.literal}. The `abrt-addon-vmcore`{.literal} package, if available, can monitor `/var/crash/`{.literal} and create problem entries automatically. Install it with `dnf install abrt-addon-vmcore`{.literal} and enable the `abrt-vmcore.service`{.literal} unit.

**Additional resources**

-   [Scripting `crash`{.literal} utility commands for `vmcore`{.literal} analysis](#scripting-crash-utility-commands-for-vmcore-analysis "22.2. Scripting crash utility commands for vmcore analysis")
-   [Displaying various indicators in the crash utility](#displaying-various-indicators-in-the-crash-utility "21.3. Displaying various indicators in the crash utility")

## [Chapter 23. Using early kdump to capture boot time crashes](#using-early-kdump-to-capture-boot-time-crashes) {#chapter-23.-using-early-kdump-to-capture-boot-time-crashes .title}

Early kdump captures `vmcore`{.literal} files when crashes occur during early boot phases before system services start. It loads the crash kernel and `initramfs`{.literal} earlier in memory to preserve troubleshooting information that would otherwise be lost.

### [23.1. Enabling early kdump](#enabling-early-kdump) {#enabling-early-kdump .title}

The `early kdump`{.literal} feature sets up the crash kernel and the initial RAM disk image (`initramfs`{.literal}) to load early enough to capture the `vmcore`{.literal} information for an early crash. This helps to eliminate the risk of losing information about the early boot kernel crashes.

**Prerequisites**

-   An active Red Hat Enterprise Linux subscription.
-   A repository containing the `kexec-tools`{.literal}, `kdump-utils`{.literal}, and `makedumpfile`{.literal} packages for your system CPU architecture.
-   Fulfilled `kdump`{.literal} configuration and targets requirements. For more information see, [Supported kdump configurations and targets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/supported-kdump-configurations-and-targets).

**Procedure**

1.  Verify that the `kdump`{.literal} service is enabled and active:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl is-enabled kdump.service && systemctl is-active kdump.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    enabled
    active
    ```

    If `kdump`{.literal} is not enabled and running, set all required configurations and verify that `kdump`{.literal} service is enabled.

2.  Rebuild the `initramfs`{.literal} image of the booting kernel with the `early kdump`{.literal} functionality:

    ``` {.language-plaintext tabindex="-1"}
    # dracut -f --add earlykdump
    ```

3.  Add the `rd.earlykdump`{.literal} kernel command line parameter:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=/boot/vmlinuz-$(uname -r) --args="rd.earlykdump"
    ```

4.  Reboot the system to reflect the changes:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

-   Verify that `rd.earlykdump`{.literal} is successfully added and `early kdump`{.literal} feature is enabled:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/cmdline
    ```

    ``` {.language-plaintext tabindex="-1"}
    BOOT_IMAGE=(hd0,msdos1)/vmlinuz-6.12.0-55.9.1.el10_0.x86_64 root=/dev/mapper/rhel-root ro crashkernel=2G-64G:256M,64G-:512M resume=/dev/mapper/rhel-swap rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet rd.earlykdump
    ```

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -x | grep early-kdump
    ```

    ``` {.language-plaintext tabindex="-1"}
    Sep 13 15:46:11 redhat dracut-cmdline[304]: early-kdump is enabled.
    Sep 13 15:46:12 redhat dracut-cmdline[304]: kexec: loaded early-kdump kernel
    ```

    See the `/usr/share/doc/kdump-utils/early-kdump-howto.txt`{.literal} file for more information.

**Additional resources**

-   [What is early kdump support and how do I configure it? (Red Hat Knowledgebase)](https://access.redhat.com/solutions/3700611)

## [Chapter 24. Signing a kernel and modules for Secure Boot](#signing-a-kernel-and-modules-for-secure-boot) {#chapter-24.-signing-a-kernel-and-modules-for-secure-boot .title}

Enhance system security by using signed kernels and kernel modules. On UEFI-based systems with Secure Boot enabled, self-sign privately built kernels or modules and import the public key into target systems.

If Secure Boot is enabled, all of the following components have to be signed with a private key and authenticated with the corresponding public key:

-   UEFI operating system boot loader
-   The Red Hat Enterprise Linux kernel
-   All kernel modules

If any of these components are not signed and authenticated, the system cannot finish the booting process.

Red Hat Enterprise Linux includes:

-   Signed boot loaders
-   Signed kernels
-   Signed kernel modules

In addition, the signed first-stage boot loader (shim) and the signed kernel include embedded Red Hat public keys. These signed executable binaries and embedded keys enable Red Hat Enterprise Linux to install, boot, and run with the Microsoft UEFI Secure Boot Certification Authority keys. These keys are provided by the UEFI firmware on systems that support UEFI Secure Boot.

Note

-   Not all UEFI-based systems include support for Secure Boot.
-   The build system, where you build and sign your kernel module, does not need to have UEFI Secure Boot enabled and does not even need to be a UEFI-based system.

### [24.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   To be able to sign externally built kernel modules, install the utilities from the following packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pesign openssl kernel-devel mokutil keyutils
    ```

    +-----------------------+--------------------------+---------------+--------------------------------------------------------------------+
    | Utility               | Provided by package      | Used on       | Purpose                                                            |
    +:======================+:=========================+:==============+:===================================================================+
    | `efikeygen`{.literal} | `pesign`{.literal}       | Build system  | Generates public and private X.509 key pair                        |
    +-----------------------+--------------------------+---------------+--------------------------------------------------------------------+
    | `openssl`{.literal}   | `openssl`{.literal}      | Build system  | Exports the unencrypted private key                                |
    +-----------------------+--------------------------+---------------+--------------------------------------------------------------------+
    | `sign-file`{.literal} | `kernel-devel`{.literal} | Build system  | Executable file used to sign a kernel module with the private key  |
    +-----------------------+--------------------------+---------------+--------------------------------------------------------------------+
    | `mokutil`{.literal}   | `mokutil`{.literal}      | Target system | Optional utility used to manually enroll the public key            |
    +-----------------------+--------------------------+---------------+--------------------------------------------------------------------+
    | `keyctl`{.literal}    | `keyutils`{.literal}     | Target system | Optional utility used to display public keys in the system keyring |
    +-----------------------+--------------------------+---------------+--------------------------------------------------------------------+

    : Table 24.1. Required utilities

    Show more

### [24.2. What is UEFI Secure Boot](#what-is-uefi-secure-boot) {#what-is-uefi-secure-boot .title}

With Unified Extensible Firmware Interface (UEFI) Secure Boot technology, you can prevent execution of kernel-space code that lacks a trusted signature. A cryptographic key signs the system boot loader, and the firmware's public key database authorizes that key.

You can subsequently verify a signature in the next-stage boot loader and the kernel.

UEFI Secure Boot establishes a chain of trust from the firmware to the signed drivers and kernel modules as follows:

-   An UEFI private key signs, and a public key authenticates the `shim`{.literal} first-stage boot loader. A *certificate authority* (CA) in turn signs the public key. The CA is stored in the firmware database.
-   The `shim`{.literal} file contains the Red Hat public key **Red Hat Secure Boot (CA key 1)** to authenticate the GRUB boot loader and the kernel.
-   The kernel in turn contains public keys to authenticate drivers and modules.

Secure Boot is the boot path validation component of the UEFI specification. The specification defines:

-   Programming interface for cryptographically protected UEFI variables in non-volatile storage.
-   Storing the trusted X.509 root certificates in UEFI variables.
-   Validation of UEFI applications such as boot loaders and drivers.
-   Procedures to revoke known-bad certificates and application hashes.

UEFI Secure Boot helps in the detection of unauthorized changes but does **not**:

-   Prevent installation or removal of second-stage boot loaders.
-   Require explicit user confirmation of such changes.
-   Stop boot path manipulations. Signatures are verified during booting but not when the boot loader is installed or updated.

If the boot loader or the kernel are not signed by a system trusted key, Secure Boot prevents them from starting.

### [24.3. UEFI Secure Boot support](#uefi-secure-boot-support) {#uefi-secure-boot-support .title}

You can install and run Red Hat Enterprise Linux 10 on systems with UEFI Secure Boot enabled if the kernel and all loaded drivers carry a trusted signature. Red Hat provides signed kernels and drivers that applicable Red Hat keys authenticate.

If you want to load externally built kernels or drivers, you must sign them as well.

Restrictions imposed by UEFI Secure Boot

:   -   The system only runs the kernel-mode code after its signature has been properly authenticated.
    -   GRUB module loading is disabled because there is no infrastructure for signing and verification of GRUB modules. Allowing module loading would run untrusted code within the security perimeter defined by Secure Boot.
    -   Red Hat provides a signed GRUB binary that has all supported modules on Red Hat Enterprise Linux.

**Additional resources**

-   [Restrictions Imposed by UEFI Secure Boot](https://access.redhat.com/articles/1351013)

### [24.4. Requirements for authenticating kernel modules with X.509 keys](#requirements-for-authenticating-kernel-modules-with-x-509-keys) {#requirements-for-authenticating-kernel-modules-with-x.509-keys .title}

Review the requirements for authenticating kernel modules with X.509 keys. The kernel validates module signatures against trusted keyrings, such as `.builtin_trusted_keys`{.literal} and `.platform`{.literal}, to enforce security policies based on the UEFI Secure Boot configuration.

In Red Hat Enterprise Linux 10, when a kernel module is loaded, the kernel checks the signature of the module against the public X.509 keys from the kernel system keyring (`.builtin_trusted_keys`{.literal}) and the kernel platform keyring (`.platform`{.literal}). The `.platform`{.literal} keyring provides keys from third-party platform providers and custom public keys. The keys from the kernel system `.blacklist`{.literal} keyring are excluded from verification.

You need to meet certain conditions to load kernel modules on systems with enabled UEFI Secure Boot functionality:

-   If UEFI Secure Boot is enabled or if the `module.sig_enforce`{.literal} kernel parameter has been specified:

    -   You can only load those signed kernel modules whose signatures were authenticated against keys from the system keyring (`.builtin_trusted_keys`{.literal}) or the platform keyring (`.platform`{.literal}).
    -   The public key must not be on the system revoked keys keyring (`.blacklist`{.literal}).

-   If UEFI Secure Boot is disabled and the `module.sig_enforce`{.literal} kernel parameter has not been specified:

    -   You can load unsigned kernel modules and signed kernel modules without a public key.

-   If the system is not UEFI-based or if UEFI Secure Boot is disabled:

    -   Only the keys embedded in the kernel are loaded onto `.builtin_trusted_keys`{.literal} and `.platform`{.literal}.
    -   You have no ability to augment that set of keys without rebuilding the kernel.

+---------------+--------------------------------------+------------------------+-------------------------+-------------+----------------+
| Module signed | Public key found and signature valid | UEFI Secure Boot state | `sig_enforce`{.literal} | Module load | Kernel tainted |
+:==============+:=====================================+:=======================+:========================+:============+:===============+
| Unsigned      | \-                                   | Not enabled            | Not enabled             | Succeeds    | Yes            |
+---------------+--------------------------------------+------------------------+-------------------------+-------------+----------------+
|               |                                      | Not enabled            | Enabled                 | Fails       | \-             |
+---------------+--------------------------------------+------------------------+-------------------------+-------------+----------------+
|               |                                      | Enabled                | \-                      | Fails       | \-             |
+---------------+--------------------------------------+------------------------+-------------------------+-------------+----------------+
| Signed        | No                                   | Not enabled            | Not enabled             | Succeeds    | Yes            |
+---------------+--------------------------------------+------------------------+-------------------------+-------------+----------------+
|               |                                      | Not enabled            | Enabled                 | Fails       | \-             |
+---------------+--------------------------------------+------------------------+-------------------------+-------------+----------------+
|               |                                      | Enabled                | \-                      | Fails       | \-             |
+---------------+--------------------------------------+------------------------+-------------------------+-------------+----------------+
| Signed        | Yes                                  | Not enabled            | Not enabled             | Succeeds    | No             |
+---------------+--------------------------------------+------------------------+-------------------------+-------------+----------------+
|               |                                      | Not enabled            | Enabled                 | Succeeds    | No             |
+---------------+--------------------------------------+------------------------+-------------------------+-------------+----------------+
|               |                                      | Enabled                | \-                      | Succeeds    | No             |
+---------------+--------------------------------------+------------------------+-------------------------+-------------+----------------+

: Table 24.2. Kernel module authentication requirements for loading

Show more

### [24.5. Sources for public keys](#sources-for-public-keys) {#sources-for-public-keys .title}

Review the sources of X.509 keys that the kernel loads into system keyrings during boot. The kernel uses these keys, derived from persistent stores like the UEFI database and the Machine Owner Key (MOK) list, to verify the integrity of modules and binaries.

-   The system keyring (`.builtin_trusted_keys`{.literal})
-   The `.platform`{.literal} keyring
-   The system `.blacklist`{.literal} keyring

+----------------------------------------------+-------------------+------------------------+-----------------------------------+
| Source of X.509 keys                         | User can add keys | UEFI Secure Boot state | Keys loaded during boot           |
+:=============================================+:==================+:=======================+:==================================+
| Embedded in kernel                           | No                | \-                     | `.builtin_trusted_keys`{.literal} |
+----------------------------------------------+-------------------+------------------------+-----------------------------------+
| UEFI `db`{.literal}                          | Limited           | Not enabled            | No                                |
+----------------------------------------------+-------------------+------------------------+-----------------------------------+
|                                              |                   | Enabled                | `.platform`{.literal}             |
+----------------------------------------------+-------------------+------------------------+-----------------------------------+
| Embedded in the `shim`{.literal} boot loader | No                | Not enabled            | No                                |
+----------------------------------------------+-------------------+------------------------+-----------------------------------+
|                                              |                   | Enabled                | `.platform`{.literal}             |
+----------------------------------------------+-------------------+------------------------+-----------------------------------+
| Machine Owner Key (MOK) list                 | Yes               | Not enabled            | No                                |
+----------------------------------------------+-------------------+------------------------+-----------------------------------+
|                                              |                   | Enabled                | `.platform`{.literal}             |
+----------------------------------------------+-------------------+------------------------+-----------------------------------+

: Table 24.3. Sources for system keyrings

Show more

`.builtin_trusted_keys`{.literal}

:   -   A keyring that is built on boot.
    -   Provides trusted public keys.
    -   `root`{.literal} privileges are required to view the keys.

`.platform`{.literal}

:   -   A keyring that is built on boot.
    -   Provides keys from third-party platform providers and custom public keys.
    -   `root`{.literal} privileges are required to view the keys.

`.blacklist`{.literal}

:   -   A keyring with X.509 keys which have been revoked.
    -   A module signed by a key from `.blacklist`{.literal} will fail authentication even if your public key is in `.builtin_trusted_keys`{.literal}.
    -   `root`{.literal} privileges are required to view the keys.

UEFI Secure Boot `db`{.literal}

:   -   A signature database.
    -   Stores keys (hashes) of UEFI applications, UEFI drivers, and boot loaders.
    -   The keys can be loaded on the machine.

UEFI Secure Boot `dbx`{.literal}

:   -   A revoked signature database.
    -   Prevents keys from getting loaded.
    -   The revoked keys from this database are added to the `.blacklist`{.literal} keyring.

### [24.6. Generating a public and private key pair](#generating-a-public-and-private-key-pair) {#generating-a-public-and-private-key-pair .title}

To use a custom kernel or modules on a Secure Boot system, generate an X.509 key pair. Sign the kernel or modules with the private key, and enroll the public key in the Machine Owner Key (MOK) list for validation.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

-   Create an X.509 public and private key pair.

    -   If you only want to sign custom kernel *modules*:

        ``` {.language-plaintext tabindex="-1"}
        # efikeygen --dbdir /etc/pki/pesign \
                    --self-sign \
                    --module \
                    --common-name 'CN=Organization signing key' \
                    --nickname 'Custom Secure Boot key'
        ```

    -   If you want to sign custom *kernel*:

        ``` {.language-plaintext tabindex="-1"}
        # efikeygen --dbdir /etc/pki/pesign \
                    --self-sign \
                    --kernel \
                    --common-name 'CN=Organization signing key' \
                    --nickname 'Custom Secure Boot key'
        ```

    -   When the RHEL system is running FIPS mode:

        ``` {.language-plaintext tabindex="-1"}
        # efikeygen --dbdir /etc/pki/pesign \
                    --self-sign \
                    --kernel \
                    --common-name 'CN=Organization signing key' \
                    --nickname 'Custom Secure Boot key' \
                    --token 'NSS FIPS 140-2 Certificate DB'
        ```

        Note

        In FIPS mode, you must use the `--token`{.literal} option so that `efikeygen`{.literal} finds the default \"NSS Certificate DB\" token in the PKI database.

        The public and private keys are now stored in the `/etc/pki/pesign/`{.literal} directory. See the `openssl(1)`{.literal} man page on your system for more information.

        Important

        It is a good security practice to sign the kernel and the kernel modules within the validity period of its signing key. However, the `sign-file`{.literal} utility does not warn you and the key will be usable in Red Hat Enterprise Linux 10 regardless of the validity dates.

**Additional resources**

-   [Creating and managing TLS keys and certificates](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/creating-and-managing-tls-keys-and-certificates)
-   [Enrolling public key on target system by adding the public key to the MOK list](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot#enrolling-public-key-on-target-system-by-adding-the-public-key-to-the-mok-list)

### [24.7. Example output of system keyrings](#example-output-of-system-keyrings) {#example-output-of-system-keyrings .title}

You can display information about the keys on the system keyrings using the `keyctl`{.literal} utility from the `keyutils`{.literal} package.

Keyrings output

:   The following is a shortened example output of `.builtin_trusted_keys`{.literal}, `.platform`{.literal}, and `.blacklist`{.literal} keyrings from a Red Hat Enterprise Linux 10 system where UEFI Secure Boot is enabled.

    ``` {.language-plaintext tabindex="-1"}
    # keyctl list %:.builtin_trusted_keys
    ```

    ``` {.language-plaintext tabindex="-1"}
    6 keys in keyring:
    ...asymmetric: Red Hat Enterprise Linux Driver Update Program (key 3): bf57f3e87...
    ...asymmetric: Red Hat Secure Boot (CA key 1): 4016841644ce3a810408050766e8f8a29...
    ...asymmetric: Microsoft Corporation UEFI CA 2011: 13adbf4309bd82709c8cd54f316ed...
    ...asymmetric: Microsoft Windows Production PCA 2011: a92902398e16c49778cd90f99e...
    ...asymmetric: Red Hat Enterprise Linux kernel signing key: 4249689eefc77e95880b...
    ...asymmetric: Red Hat Enterprise Linux kpatch signing key: 4d38fd864ebe18c5f0b7...
    ```

    ``` {.language-plaintext tabindex="-1"}
    # keyctl list %:.platform
    ```

    ``` {.language-plaintext tabindex="-1"}
    4 keys in keyring:
    ...asymmetric: VMware, Inc.: 4ad8da0472073...
    ...asymmetric: Red Hat Secure Boot CA 5: cc6fafe72...
    ...asymmetric: Microsoft Windows Production PCA 2011: a929f298e1...
    ...asymmetric: Microsoft Corporation UEFI CA 2011: 13adbf4e0bd82...
    ```

    ``` {.language-plaintext tabindex="-1"}
    # keyctl list %:.blacklist
    ```

    ``` {.language-plaintext tabindex="-1"}
    4 keys in keyring:
    ...blacklist: bin:f5ff83a...
    ...blacklist: bin:0dfdbec...
    ...blacklist: bin:38f1d22...
    ...blacklist: bin:51f831f...
    ```

    The `.builtin_trusted_keys`{.literal} keyring in the example shows the addition of two keys from the UEFI Secure Boot `db`{.literal} keys and the `Red Hat Secure Boot (CA key 1)`{.literal}, which is embedded in the `shim`{.literal} boot loader.

Kernel console output

:   The following example shows the kernel console output. The messages identify the keys with an UEFI Secure Boot related source. These include UEFI Secure Boot `db`{.literal}, embedded `shim`{.literal}, and MOK list.

    ``` {.language-plaintext tabindex="-1"}
    # dmesg | grep -E 'integrity.*cert'
    ```

    ``` {.language-plaintext tabindex="-1"}
    [1.512966] integrity: Loading X.509 certificate: UEFI:db
    [1.513027] integrity: Loaded X.509 cert 'Microsoft Windows Production PCA 2011: a929023...
    [1.513028] integrity: Loading X.509 certificate: UEFI:db
    [1.513057] integrity: Loaded X.509 cert 'Microsoft Corporation UEFI CA 2011: 13adbf4309...
    [1.513298] integrity: Loading X.509 certificate: UEFI:MokListRT (MOKvar table)
    [1.513549] integrity: Loaded X.509 cert 'Red Hat Secure Boot CA 5: cc6fa5e72868ba494e93...
    ```

See `keyctl(1)`{.literal} and `dmesg(1)`{.literal} man pages on your system for more information.

### [24.8. Enrolling public key on target system by adding the public key to the MOK list](#enrolling-public-key-on-target-system-by-adding-the-public-key-to-the-mok-list) {#enrolling-public-key-on-target-system-by-adding-the-public-key-to-the-mok-list .title}

To access the kernel or kernel modules, you must authenticate your public key. Enroll the key in the target system's platform keyring (`.platform`{.literal}).

On Unified Extensible Firmware Interface (UEFI) Secure Boot systems, the kernel imports keys from the `db`{.literal} database. It does not import keys that the `dbx`{.literal} database marks as revoked.

The Machine Owner Key (MOK) facility allows expanding the UEFI Secure Boot key database. On a UEFI-based system, you can boot RHEL 10 with Secure Boot enabled. Keys on the MOK list are then added to the platform keyring (`.platform`{.literal}), along with keys from the Secure Boot database.

The MOK list is stored securely and persists across reboots. It is separate from the Secure Boot databases.

The MOK facility is supported by `shim`{.literal}, `MokManager`{.literal}, `GRUB`{.literal}, and the `mokutil`{.literal} utility. Together, they enable secure key management and authentication for UEFI-based systems.

Note

To get the authentication service of your kernel module on your systems, consider requesting your system vendor to incorporate your public key into the UEFI Secure Boot key database in their factory firmware image.

**Prerequisites**

-   You have generated a public and private key pair and know the validity dates of your public keys. For details, see [Generating a public and private key pair](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot#generating-a-public-and-private-key-pair).

**Procedure**

1.  Export your public key to the `sb_cert.cer`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # certutil -d /etc/pki/pesign \
               -n 'Custom Secure Boot key' \
               -Lr \
               > sb_cert.cer
    ```

2.  Import your public key into the MOK list:

    ``` {.language-plaintext tabindex="-1"}
    # mokutil --import sb_cert.cer
    ```

3.  Enter a new password for this MOK enrollment request.

4.  Reboot the machine.

    The `shim`{.literal} boot loader notices the pending MOK key enrollment request and it launches `MokManager.efi`{.literal} to enable you to complete the enrollment from the UEFI console.

5.  Choose `Enroll MOK`{.literal}, enter the password you previously associated with this request when prompted, and confirm the enrollment.

    Your public key is added to the MOK list, which is persistent.

    Once a key is on the MOK list, it is automatically propagated to the `.platform`{.literal} keyring on this and subsequent boots when UEFI Secure Boot is enabled.

### [24.9. Signing a kernel with the private key](#signing-a-kernel-with-the-private-key) {#signing-a-kernel-with-the-private-key .title}

To enhance system security on UEFI Secure Boot systems, load a kernel signed with a private key.

**Prerequisites**

-   You have generated a public and private key pair and know the validity dates of your public keys. For details, see [Generating a public and private key pair](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot#generating-a-public-and-private-key-pair).
-   You have enrolled your public key on the target system. For details, see [Enrolling public key on target system by adding the public key to the MOK list](#enrolling-public-key-on-target-system-by-adding-the-public-key-to-the-mok-list "24.8. Enrolling public key on target system by adding the public key to the MOK list").
-   You have a kernel image in the ELF format available for signing.

**Procedure**

-   On the x64 architecture:

    a.  Create a signed image:

        ``` {.language-plaintext tabindex="-1"}
        # pesign --certificate 'Custom Secure Boot key' \
                 --in vmlinuz-version \
                 --sign \
                 --out vmlinuz-version.signed
        ```

        Replace *`version`{.literal}* with the version suffix of your `vmlinuz`{.literal} file, and *`Custom Secure Boot key`{.literal}* with the name that you chose earlier.

    b.  Optional: Check the signatures:

        ``` {.language-plaintext tabindex="-1"}
        # pesign --show-signature \
                 --in vmlinuz-version.signed
        ```

    c.  Overwrite the unsigned image with the signed image:

        ``` {.language-plaintext tabindex="-1"}
        # mv vmlinuz-version.signed vmlinuz-version
        ```

-   On the 64-bit ARM architecture:

    a.  Decompress the `vmlinuz`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # zcat vmlinuz-version > vmlinux-version
        ```

    b.  Create a signed image:

        ``` {.language-plaintext tabindex="-1"}
        # pesign --certificate 'Custom Secure Boot key' \
                 --in vmlinux-version \
                 --sign \
                 --out vmlinux-version.signed
        ```

    c.  Optional: Check the signatures:

        ``` {.language-plaintext tabindex="-1"}
        # pesign --show-signature \
                 --in vmlinux-version.signed
        ```

    d.  Compress the `vmlinux`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # gzip --to-stdout vmlinux-version.signed > vmlinuz-version
        ```

    e.  Remove the uncompressed `vmlinux`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # rm vmlinux-version*
        ```

### [24.10. Signing a GRUB build with the private key](#signing-a-grub-build-with-the-private-key) {#signing-a-grub-build-with-the-private-key .title}

To use a custom GRUB build on a UEFI Secure Boot system, sign it with a private key. You need this for custom builds or if you remove the Microsoft trust anchor.

**Prerequisites**

-   You have generated a public and private key pair and know the validity dates of your public keys. For details, see [Generating a public and private key pair](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot#generating-a-public-and-private-key-pair).
-   You have enrolled your public key on the target system. For details, see [Enrolling public key on target system by adding the public key to the MOK list](#enrolling-public-key-on-target-system-by-adding-the-public-key-to-the-mok-list "24.8. Enrolling public key on target system by adding the public key to the MOK list").
-   You have a GRUB EFI binary available for signing.

**Procedure**

-   On the x64 architecture:

    a.  Create a signed GRUB EFI binary:

        ``` {.language-plaintext tabindex="-1"}
        # pesign --in /boot/efi/EFI/redhat/grubx64.efi \
                 --out /boot/efi/EFI/redhat/grubx64.efi.signed \
                 --certificate 'Custom Secure Boot key' \
                 --sign
        ```

        Replace *`Custom Secure Boot key`{.literal}* with the name that you chose earlier.

    b.  Optional: Check the signatures:

        ``` {.language-plaintext tabindex="-1"}
        # pesign --in /boot/efi/EFI/redhat/grubx64.efi.signed \
                 --show-signature
        ```

    c.  Overwrite the unsigned binary with the signed binary:

        ``` {.language-plaintext tabindex="-1"}
        # mv /boot/efi/EFI/redhat/grubx64.efi.signed \
             /boot/efi/EFI/redhat/grubx64.efi
        ```

        Warning

        When overwriting the grub binary, your system might fail to boot normally and you might require reinstalling the grub from the system image.

-   On the 64-bit ARM architecture:

    a.  Create a signed GRUB EFI binary:

        ``` {.language-plaintext tabindex="-1"}
        # pesign --in /boot/efi/EFI/redhat/grubaa64.efi \
                 --out /boot/efi/EFI/redhat/grubaa64.efi.signed \
                 --certificate 'Custom Secure Boot key' \
                 --sign
        ```

        Replace *`Custom Secure Boot key`{.literal}* with the name that you chose earlier.

    b.  Optional: Check the signatures:

        ``` {.language-plaintext tabindex="-1"}
        # pesign --in /boot/efi/EFI/redhat/grubaa64.efi.signed \
                 --show-signature
        ```

    c.  Overwrite the unsigned binary with the signed binary:

        ``` {.language-plaintext tabindex="-1"}
        # mv /boot/efi/EFI/redhat/grubaa64.efi.signed \
             /boot/efi/EFI/redhat/grubaa64.efi
        ```

### [24.11. Signing kernel modules with the private key](#signing-kernel-modules-with-the-private-key) {#signing-kernel-modules-with-the-private-key .title}

To enhance security on UEFI Secure Boot systems, load kernel modules signed with a private key.

Your signed kernel module is also loadable on systems where UEFI Secure Boot is disabled or on a non-UEFI system. As a result, you do not need to provide both, a signed and unsigned version of your kernel module.

**Prerequisites**

-   You have generated a public and private key pair and know the validity dates of your public keys. For details, see [Generating a public and private key pair](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot#generating-a-public-and-private-key-pair).
-   You have enrolled your public key on the target system. For details, see [Enrolling public key on target system by adding the public key to the MOK list](#enrolling-public-key-on-target-system-by-adding-the-public-key-to-the-mok-list "24.8. Enrolling public key on target system by adding the public key to the MOK list").
-   You have a kernel module in ELF image format available for signing.

**Procedure**

1.  Export your public key to the `sb_cert.cer`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # certutil -d /etc/pki/pesign \
               -n 'Custom Secure Boot key' \
               -Lr \
               > sb_cert.cer
    ```

2.  Extract the key from the NSS database as a PKCS #12 file:

    ``` {.language-plaintext tabindex="-1"}
    # pk12util -o sb_cert.p12 \
               -n 'Custom Secure Boot key' \
               -d /etc/pki/pesign
    ```

3.  When the previous command prompts, enter a new password that encrypts the private key.

4.  Export the unencrypted private key:

    ``` {.language-plaintext tabindex="-1"}
    # openssl pkcs12 \
             -in sb_cert.p12 \
             -out sb_cert.priv \
             -nocerts \
             -noenc
    ```

    Important

    Keep the unencrypted private key secure.

5.  Sign your kernel module. The following command appends the signature directly to the ELF image in your kernel module file:

    ``` {.language-plaintext tabindex="-1"}
    # /usr/src/kernels/$(uname -r)/scripts/sign-file \
              sha256 \
              sb_cert.priv \
              sb_cert.cer \
              my_module.ko
    ```

    Your kernel module is now ready for loading.

    Important

    In Red Hat Enterprise Linux 10, the validity dates of the key pair matter. The key does not expire, but the kernel module must be signed within the validity period of its signing key. The `sign-file`{.literal} utility will not warn you of this.

    For example, a key that is only valid in 2021 can be used to authenticate a kernel module signed in 2021 with that key. However, users cannot use that key to sign a kernel module in 2022.

**Verification**

1.  Display information about the kernel module's signature:

    ``` {.language-plaintext tabindex="-1"}
    # modinfo my_module.ko | grep signer
    ```

    ``` {.language-plaintext tabindex="-1"}
      signer:         Your Name Key
    ```

    Check that the signature lists your name as entered during generation.

    Note

    The appended signature is not contained in an ELF image section and is not a formal part of the ELF image. Therefore, utilities such as `readelf`{.literal} cannot display the signature on your kernel module.

2.  Load the module:

    ``` {.language-plaintext tabindex="-1"}
    # insmod my_module.ko
    ```

3.  Remove the module:

    ``` {.language-plaintext tabindex="-1"}
    # modprobe -r my_module.ko
    ```

**Additional resources**

-   [Generating a public and private key pair](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot#generating-a-public-and-private-key-pair)
-   [Enrolling public key on target system by adding the public key to the MOK list](#enrolling-public-key-on-target-system-by-adding-the-public-key-to-the-mok-list "24.8. Enrolling public key on target system by adding the public key to the MOK list")
-   [Displaying information about kernel modules](#displaying-information-about-kernel-modules "3.5. Displaying information about kernel modules")

### [24.12. Loading signed kernel modules](#loading-signed-kernel-modules) {#loading-signed-kernel-modules .title}

To load signed kernel modules, enroll your public key in the platform keyring and Machine Owner Key (MOK) list, then use the `modprobe`{.literal} command.

**Prerequisites**

-   You have generated the public and private key pair. For details, see [Generating a public and private key pair](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot#generating-a-public-and-private-key-pair).

-   You have enrolled the public key into the platform keyring. For details, see [Enrolling public key on target system by adding the public key to the MOK list](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot#enrolling-public-key-on-target-system-by-adding-the-public-key-to-the-mok-list).

-   You have signed a kernel module with the private key. For details, see [Signing kernel modules with the private key](#signing-kernel-modules-with-the-private-key "24.11. Signing kernel modules with the private key").

-   Install the `kernel-modules-extra`{.literal} package, which creates the `/lib/modules/$(uname -r)/extra/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y install kernel-modules-extra
    ```

**Procedure**

1.  Verify that your public keys are on the platform keyring:

    ``` {.language-plaintext tabindex="-1"}
    # keyctl list %:.platform
    ```

2.  Copy the kernel module into the `extra/`{.literal} directory of the kernel that you want:

    ``` {.language-plaintext tabindex="-1"}
    # cp my_module.ko /lib/modules/$(uname -r)/extra/
    ```

3.  Update the modular dependency list:

    ``` {.language-plaintext tabindex="-1"}
    # depmod -a
    ```

4.  Load the kernel module:

    ``` {.language-plaintext tabindex="-1"}
    # modprobe -v my_module
    ```

5.  Optional: To load the module on boot, add it to the `/etc/modules-loaded.d/`{.literal}*`my_module`{.literal}*`.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # echo "my_module" > /etc/modules-load.d/my_module.conf
    ```

**Verification**

-   Verify that the module was successfully loaded:

    ``` {.language-plaintext tabindex="-1"}
    # lsmod | grep my_module
    ```

**Additional resources**

-   [Managing kernel modules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/managing-kernel-modules)

## [Chapter 25. Updating the Secure Boot Revocation List](#updating-the-secure-boot-revocation-list) {#chapter-25.-updating-the-secure-boot-revocation-list .title}

Update the UEFI Secure Boot Revocation List to identify software with known security issues and prevent it from compromising the boot process.

### [25.1. The Secure Boot Revocation List](#the-secure-boot-revocation-list) {#the-secure-boot-revocation-list .title}

The UEFI Secure Boot Revocation List, or the Secure Boot Forbidden Signature Database (`dbx`{.literal}), is a list that identifies software that Secure Boot no longer allows to run.

When a security issue or a stability problem is found in software that interfaces with Secure Boot, such as in the GRUB boot loader, the Revocation List stores its hash signature. Software with such a recognized signature cannot run during boot, and the system boot fails to prevent compromising the system.

For example, a certain version of GRUB might contain a security issue that allows an attacker to bypass the Secure Boot mechanism. When the issue is found, the Revocation List adds hash signatures of all GRUB versions that contain the issue. As a result, only secure GRUB versions can boot on the system.

The Revocation List requires regular updates to recognize newly found issues. When updating the Revocation List, make sure to use a safe update method that does not cause your currently installed system to no longer boot.

### [25.2. Applying an online Revocation List update](#applying-an-online-revocation-list-update) {#applying-an-online-revocation-list-update .title}

To prevent known security issues, you can update the Secure Boot Revocation List on your system. This procedure is safe and ensures that the update does not prevent your system from booting.

**Prerequisites**

-   Secure Boot is enabled on your system.
-   Your system is connected to internet for updates.

**Procedure**

1.  Determine the current version of the Revocation List:

    ``` {.language-plaintext tabindex="-1"}
    # *fwupdmgr get-devices*
    ```

    See the `Current version`{.literal} field under `UEFI dbx`{.literal}.

2.  Enable the LVFS Revocation List repository:

    ``` {.language-plaintext tabindex="-1"}
    # *fwupdmgr enable-remote lvfs*
    ```

3.  Refresh the repository metadata:

    ``` {.language-plaintext tabindex="-1"}
    # *fwupdmgr refresh*
    ```

4.  Apply the Revocation List update:

    -   On the command line:

        ``` {.language-plaintext tabindex="-1"}
        # *fwupdmgr update*
        ```

    -   In the graphical interface:

        i.  Open the **Software** application
        ii. Navigate to the **Updates** tab.
        iii. Find the **Secure Boot dbx Configuration Update** entry.
        iv. Click Update.

5.  At the end of the update, `fwupdmgr`{.literal} or **Software** asks you to reboot the system. Confirm the reboot.

**Verification**

-   After the reboot, check the current version of the Revocation List again:

    ``` {.language-plaintext tabindex="-1"}
    # *fwupdmgr get-devices*
    ```

### [25.3. Applying an offline Revocation List update](#applying-an-offline-revocation-list-update) {#applying-an-offline-revocation-list-update .title}

To prevent known security issues on a system with no internet connection, you can update the Secure Boot Revocation List from Red Hat Enterprise Linux. This procedure is safe and ensures that the update does not prevent your system from booting.

**Procedure**

1.  Identify the current version of the Revocation List:

    ``` {.language-plaintext tabindex="-1"}
    # *fwupdmgr get-devices*
    ```

    See the `Current version`{.literal} field under `UEFI dbx`{.literal}.

2.  List the updates available from RHEL:

    ``` {.language-plaintext tabindex="-1"}
    # *ls /usr/share/dbxtool/*
    ```

3.  Select the most recent update file for your architecture. The file names use the following format:

    ``` {.language-plaintext tabindex="-1"}
    DBXUpdate-date-architecture.cab
    ```

4.  Install the selected update file:

    ``` {.language-plaintext tabindex="-1"}
    # fwupdmgr install /usr/share/dbxtool/DBXUpdate-date-architecture.cab
    ```

5.  At the end of the update, `fwupdmgr`{.literal} asks you to reboot the system. Confirm the reboot.

**Verification**

-   After the reboot, check the current version of the Revocation List again:

    ``` {.language-plaintext tabindex="-1"}
    # *fwupdmgr get-devices*
    ```

## [Chapter 26. Enabling HTTPS boot encryption](#enabling-https-boot-encryption) {#chapter-26.-enabling-https-boot-encryption .title}

HTTPS boot encryption protects boot files in transit and authenticates the download server during network boot. Configure UEFI firmware to download the kernel and initial RAM file system (initramfs) over HTTPS with transport encryption and signature verification.

### [26.1. HTTPS boot encryption on RHEL](#https-boot-encryption-on-rhel) {#https-boot-encryption-on-rhel .title}

HTTPS boot encryption downloads the kernel and initial RAM file system (initramfs) over HTTPS with transport encryption, digital signature verification, and server authentication before boot.

With firmware Transport Layer Security (TLS) support and trusted security certificates, you manage HTTPS boot encryption on your system. Digital signatures ensure boot file integrity and reliability before the firmware loads the downloaded image. The firmware must have decryption capabilities. Plain HTTP boot does not provide the same transport protection as HTTPS boot encryption.

You configure the CA certificate in client firmware in UEFI mode for UEFI HTTPS boot without a graphical interface.

Note

Each firmware vendor has its own procedure for enrolling certificates. Consult your firmware vendor documentation to enable HTTPS boot encryption.

**Additional resources**

-   [Booting the installation from a network by using HTTP](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/booting-the-installation-media#booting-the-installation-from-a-network-using-http)

### [26.2. Configuring HTTPS boot encryption on TianoCore firmware](#configuring-https-boot-encryption-on-tianocore-firmware) {#configuring-https-boot-encryption-on-tianocore-firmware .title}

To enable UEFI HTTPS boot for the kernel and initial RAM file system (initramfs), configure OVMF or other TianoCore-based firmware to download them over HTTPS, set the boot source, enroll a Certificate Authority (CA) certificate, and put the UEFI HTTPS boot option first in the boot order.

**Prerequisites**

-   You have root privileges on your system.
-   You have an HTTPS server configured and serving signed kernel and initial RAM file system images.
-   You have a CA certificate file available in the `/etc/pki/`{.literal} directory on your HTTPS server.
-   Optional: You have a Dynamic Host Configuration Protocol (DHCP) server configured with a boot file option, or the HTTPS boot server URL is configured in the firmware.

**Procedure**

1.  Restart the system and open the UEFI firmware settings:

    Note

    These steps provide separate instructions for physical hardware and for Open Virtual Machine Firmware (OVMF) virtual machines. Follow only the option that matches your platform.

    -   On physical hardware, press the firmware setup key that your vendor documents at startup.
    -   On a virtual machine with Open Virtual Machine Firmware (OVMF), press Esc at startup.

2.  Optional: On OVMF with the NT32 network simulator, start the NT32 simulator from the UEFI menu.

3.  Configure the boot source by using one of the following options:

    -   When DHCP provides a boot file option, select **UEFI HTTPv4** or **UEFI HTTPv6** in **Boot Manager**. The firmware resolves the boot server URL from DHCP.
    -   When DHCP is unavailable on a virtual machine with OVMF, open **Device Manager** \> **Network Device List** \> **MAC:\**\<your-mac-address\>* \> \*HTTP Boot Configuration** and enter the HTTPS boot server URL. The MAC address in the menu label matches your network adapter.
    -   When DHCP is unavailable on physical hardware, configure the HTTPS boot server URL in the HTTP boot settings. Consult your firmware vendor documentation for the menu path.

4.  Open the certificate management settings in the UEFI firmware:

    -   On physical hardware, open the certificate or truststore menu that your firmware vendor provides. This menu can be labeled **Certificate Management**, **Trusted Certificates**, or **CA Certificates**.
    -   On a virtual machine with Open Virtual Machine Firmware (OVMF), open **Device Manager** \> **TLS Authentication Configuration** \> **Server CA Configuration**.

5.  Select the option to enroll a new certificate:

    -   On physical hardware, select the option your firmware vendor provides, such as **Add New Certificate**.

    -   On a virtual machine with Open Virtual Machine Firmware (OVMF), select **Enroll Cert**.

        The firmware shows the certificate enrollment interface.

6.  Add the CA certificate in the firmware interface:

    -   On physical hardware, add the certificate by using manual input or certificate file upload from a connected USB drive as your firmware vendor provides.

    -   On a virtual machine with Open Virtual Machine Firmware (OVMF), upload the CA certificate file from a connected USB drive. When prompted, enter the globally unique identifier (GUID) for the certificate file.

        The certificate file must be in Distinguished Encoding Rules binary format.

        When your certificate is in the Privacy-Enhanced Mail (PEM) text format, convert it to the Distinguished Encoding Rules (DER) format on the host system before you upload the file:

        ``` {.language-plaintext tabindex="-1"}
        # openssl x509 -in <ca-certificate>.pem -outform DER -out <ca-certificate>.der
        ```

        Follow the on-screen prompts to complete the upload. After the upload, the firmware displays the certificate details.

7.  Verify that the displayed certificate details match your CA certificate.

8.  Verify that UEFI HTTPS boot is enabled and set as the first entry in the boot order.

    Warning

    Incorrect UEFI settings can prevent the system from booting. Review your hardware documentation before you change firmware options.

9.  Save the UEFI firmware settings and exit.

10. Reboot the system.

**Verification**

-   After the system reboots, the firmware starts the UEFI HTTPS boot process and downloads the boot image from the configured server.

**Additional resources**

-   [HTTPS boot encryption on Red Hat Enterprise Linux](#https-boot-encryption-on-rhel "26.1. HTTPS boot encryption on RHEL")
-   [Loading the CA certificate for HTTPS boot encryption on QEMU and libvirt](#loading-the-ca-certificate-for-https-boot-encryption-on-qemu-and-libvirt "26.3. Loading the CA certificate for HTTPS boot encryption on QEMU and libvirt")

### [26.3. Loading the CA certificate for HTTPS boot encryption on QEMU and libvirt](#loading-the-ca-certificate-for-https-boot-encryption-on-qemu-and-libvirt) {#loading-the-ca-certificate-for-https-boot-encryption-on-qemu-and-libvirt .title}

Load the EFI signature list for the HTTPS boot CA certificate on Quick EMUlator (QEMU) or libvirt virtual machines when you do not enroll the certificate through the firmware interface.

**Prerequisites**

-   You created a root CA signature list file in EFI signature list format with the `.esl`{.literal} extension.
-   You have root privileges on the host system.
-   The virtual machine uses Open Virtual Machine Firmware (OVMF) with HTTPS boot support.

Note

The signature list file contains your HTTPS boot Certificate Authority certificate in EFI Signature List format.

When the HTTPS server uses a CA certificate from the host truststore, run `update-ca-trust`{.literal} on the host and use `/etc/pki/ca-trust/extracted/edk2/cacerts.bin`{.literal} as the file in the `fw_cfg`{.literal} parameter.

When you use a dedicated CA certificate, create an EFI signature list file with the `.esl`{.literal} extension that contains only that certificate before you load it through `fw_cfg`{.literal}.

**Procedure**

-   Load the CA certificate by using one of the following methods:

    -   For QEMU, add the following parameter to the `qemu-system-x86_64`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        # qemu-system-x86_64 <existing-qemu-options> -fw_cfg name=etc/edk2/https/cacerts,file=<path-to-root-ca>.esl
        ```

    -   For libvirt, add the following XML inside the `domain`{.literal} element of the virtual machine configuration:

        ``` {.language-plaintext tabindex="-1"}
        <qemu:commandline>
          <qemu:arg value='-fw_cfg'/>
          <qemu:arg value='name=etc/edk2/https/cacerts,file=<path-to-root-ca>.esl'/>
        </qemu:commandline>
        ```

        Important

        The name value must be `etc/edk2/https/cacerts`{.literal}. This is how EDK2 identifies the root CA signature list.

**Verification**

-   Start the virtual machine and confirm that UEFI HTTPS boot completes without a certificate trust error from the configured HTTPS server.

**Additional resources**

-   [Configuring HTTPS boot encryption on TianoCore firmware](#configuring-https-boot-encryption-on-tianocore-firmware "26.2. Configuring HTTPS boot encryption on TianoCore firmware")
-   [HTTPS boot encryption on Red Hat Enterprise Linux](#https-boot-encryption-on-rhel "26.1. HTTPS boot encryption on RHEL")

## [Chapter 27. Enhancing security with the kernel integrity subsystem](#enhancing-security-with-the-kernel-integrity-subsystem) {#chapter-27.-enhancing-security-with-the-kernel-integrity-subsystem .title}

Use components of the kernel integrity subsystem to improve system security. Configure relevant components such as IMA signature-based appraisal and remote attestation.

### [27.1. The kernel integrity subsystem](#the-kernel-integrity-subsystem) {#the-kernel-integrity-subsystem .title}

The kernel integrity subsystem protects system integrity by detecting file tampering and enabling remote attestation. It includes the Integrity Measurement Architecture (IMA) and the Extended Verification Module (EVM).

Integrity Measurement Architecture (IMA)

:   IMA maintains the integrity of file content. It includes three features that you can enable through an IMA policy:

    -   `IMA-Measurement`{.literal}: Collect the file content hash or signature and store the measurements in the kernel. If a TPM is available, each measurement extends a TPM PCR, which enables remote attestation with an attestation quote.
    -   `IMA-Appraisal`{.literal}: Verify file integrity by comparing the calculated file hash with a known good reference value or by verifying a signature stored in the security.ima attribute. If verification fails, the system denies access.
    -   `IMA-Audit`{.literal}: Store the calculated file content hash or signature in the system audit log.

Extended Verification Module (EVM)
:   The EVM protects file metadata, including extended attributes related to system security such as `security.ima`{.literal} and `security.selinux`{.literal}. EVM stores a reference hash or HMAC for these security attributes in `security.evm`{.literal} and uses it to detect if the file metadata has been changed maliciously.

**Additional resources**

-   [Security hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening)
-   [Using SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/index)

### [27.2. Enabling kernel's runtime integrity monitoring through IMA-signature based appraisal](#enabling-kernels-runtime-integrity-monitoring-through-ima-signature-based-appraisal) {#enabling-kernels-runtime-integrity-monitoring-through-ima-signature-based-appraisal .title}

To ensure the system executes only authorized package files, enable signature-based IMA appraisal by running the `ima-setup`{.literal} command with the sample policy. From RHEL 9, Red Hat signs all package files per file.

**Procedure**

1.  Run `ima-setup`{.literal} to enable signature-based IMA appraisal:

    ``` {.language-plaintext tabindex="-1"}
    # ima-setup --policy=/usr/share/ima/policies/01-appraise-executable-and-lib-signatures
    ```

    This command:

    -   Stores package file signature in `security.ima`{.literal} for all installed packages.
    -   Includes the `dracut`{.literal} integrity module to load the IMA code signing key to kernel.
    -   Copies the policy to `/etc/ima/ima-policy`{.literal} so systemd loads it at boot time.

**Verification**

-   The `ip`{.literal} command can be successfully executed.

-   If `ip`{.literal} is copied to `/tmp`{.literal}, by default, it loses its `security.ima`{.literal} and therefore `ip`{.literal} command is not executed.

    ``` {.language-plaintext tabindex="-1"}
    # cp /usr/sbin/ip /tmp
    # /tmp/ip
    ```

    ``` {.language-plaintext tabindex="-1"}
    bash: /tmp/ip: Permission denied
    ```

    ``` {.language-plaintext tabindex="-1"}
    # /tmp/ip doesn't have security.ima
    # getfattr -m security.ima -d /tmp/ip
    # whereas /usr/sbin/ip has
    # getfattr -m security.ima /usr/sbin/ip
    # file: usr/sbin/ip
    ```

    ``` {.language-plaintext tabindex="-1"}
    security.ima=0sAwIE0zIESQBnMGUCMQCLXZ7ukyDcguLgPYwzXU16dcVrmlHxOta7vm7EUfX07Nf0xnP1MyE//AZaqeNIKBoCMFHNDOuA4uNvS+8OOAy7YEn8oathfsF2wsDSZi+NAoumC6RFqIB912zkRKxraSX8sA==
    ```

If the sample policy `01-appraise-executable-and-lib-signatures`{.literal} does not meet your requirements, you can create and use a custom policy.

### [27.3. Enabling remote attestation with IMA measurement](#enabling-remote-attestation-with-ima-measurement) {#enabling-remote-attestation-with-ima-measurement .title}

To verify system integrity by using remote attestation tools such as `Keylime`{.literal}, enable Integrity Measurement Architecture (IMA) measurement. A signed sample measurement policy is at `/usr/share/ima/policies/02-keylime-remote-attestation`{.literal}. Deploy and run a policy that meets your requirements.

**Prerequisites**

-   A signed measurement policy is available at `/usr/share/ima/policies/02-keylime-remote-attestation`{.literal}.

**Procedure**

1.  Install the `rpm-plugin-ima`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rpm-plugin-ima
    ```

2.  Reinstall the `ima-evm-utils`{.literal} package so that the sample policies have IMA signatures stored in extended attributes:

    ``` {.language-plaintext tabindex="-1"}
    # dnf reinstall ima-evm-utils
    ```

3.  Confirm that the IMA signature has been stored:

    ``` {.language-plaintext tabindex="-1"}
    # evmctl ima_verify -k /etc/keys/ima/redhatimarelease-10.der /usr/share/ima/policies/02-keylime-remote-attestation
    ```

    ``` {.language-plaintext tabindex="-1"}
    keyid d3320449 (from /etc/keys/ima/redhatimarelease-10.der)
    key 1: d3320449 /etc/keys/ima/redhatimarelease-10.der
    /usr/share/ima/policies/02-keylime-remote-attestation: verification is OK
    ```

4.  Copy the signed measurement policy with extended attributes preserved to `/etc/ima/ima-policy`{.literal} so systemd automatically loads it on boot:

    ``` {.language-plaintext tabindex="-1"}
    # cp --preserve=xattr /usr/share/ima/policies/02-keylime-remote-attestation /etc/ima/ima-policy
    ```

5.  Enable the dracut integrity module so the IMA key loads at boot time:

    ``` {.language-plaintext tabindex="-1"}
    # cp --preserve=xattr /usr/share/ima/dracut-98-integrity.conf /etc/dracut.conf.d/ima.conf
    ```

6.  Regenerate the initramfs to include the `integrity`{.literal} module:

    ``` {.language-plaintext tabindex="-1"}
    # dracut -f
    ```

    -   On `s390x`{.literal} systems, additionally run `zipl`{.literal} to apply the changes for the next IPL (initial program load):

        ``` {.language-plaintext tabindex="-1"}
        # zipl
        ```

7.  Reboot to load the IMA key:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reboot
    ```

    Warning

    On systems with Secure Boot enabled, the kernel does not accept unsigned IMA policies. If you load a policy before the IMA code-signing key is available to the kernel, the load fails and the next reboot can hang. Therefore, you must load the policy after the key is available.

    If the sample policy does not meet your requirements, see [Loading an IMA policy signed by your custom IMA key](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/extending-customizing-and-troubleshooting-kernel-integrity-subsystem#loading-an-ima-policy-signed-by-your-custom-ima-key).

**Verification**

-   Verify that the policy is loaded:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/kernel/security/integrity/ima/policy
    ```

**Additional resources**

-   [Extending, customizing, and troubleshooting the kernel integrity subsystem](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/extending-customizing-and-troubleshooting-kernel-integrity-subsystem)

## [Chapter 28. Extending, customizing, and troubleshooting kernel integrity subsystem](#extending-customizing-and-troubleshooting-kernel-integrity-subsystem) {#chapter-28.-extending-customizing-and-troubleshooting-kernel-integrity-subsystem .title}

Extend, customize, and troubleshoot the kernel integrity subsystem to meet specific security requirements in different operational environments.

### [28.1. Generate good reference values for IMA appraisal](#generate-good-reference-values-for-ima-appraisal) {#generate-good-reference-values-for-ima-appraisal .title}

Before you deploy an Integrity Measurement Architecture (IMA) policy that includes IMA-appraisal rules, ensure that all files governed by these rules have valid reference values in the `security.ima`{.literal} extended attribute. Missing reference values can prevent proper boot or deny access to files.

``` {.language-bash tabindex="-1"}
# ima-appraise-file </path/to/file>
```

#### [28.1.1. Adding IMA signatures as good references for immutable files](#adding-ima-signatures-as-good-references-for-immutable-files) {#adding-ima-signatures-as-good-references-for-immutable-files .title}

To support integrity verification, you can use IMA signatures as trusted reference values for immutable files. This approach helps ensure that only files with valid signatures are accessed, which strengthens system security and compliance.

**Prerequisites**

-   You have created an IMA policy that includes IMA-appraisal rules.

**Procedure**

1.  Install the `rpm-plugin-ima`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install rpm-plugin-ima -yq
    ```

    This ensures that package files have IMA signature stored in `security.xattr`{.literal} automatically during package installation, reinstallation, or upgradation.

2.  Reinstall all the packages:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf reinstall "*" -y
    ```

    This ensures that the `security.xattr`{.literal} extended attribute is updated for all packages.

3.  Enable the dracut integrity module so the official IMA code-signing key in `/etc/keys/ima`{.literal} loads automatically on boot:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dracut -f
    ```

**Verification**

-   Verify that signature is correctly stored in `security.ima`{.literal} extended attribute:

    ``` {.language-plaintext tabindex="-1"}
    $ # evmctl ima_verify -k /etc/keys/ima/redhatimarelease-10.der /usr/lib/systemd/systemd
    ```

    ``` {.language-plaintext tabindex="-1"}
    keyid d3320449 (from /etc/keys/ima/redhatimarelease-10.der)
    key 1: d3320449 /etc/keys/ima/redhatimarelease-10.der
    /usr/lib/systemd/systemd: verification is OK
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ # evmctl ima_verify -k /etc/keys/ima/redhatimarelease-10.der /bin/bash
    ```

    ``` {.language-plaintext tabindex="-1"}
    keyid d3320449 (from /etc/keys/ima/redhatimarelease-10.der)
    key 1: d3320449 /etc/keys/ima/redhatimarelease-10.der
    /bin/bash: verification is OK
    ...
    ```

#### [28.1.2. Generating good reference values for mutable files](#generating-good-reference-values-for-mutable-files) {#generating-good-reference-values-for-mutable-files .title}

To maintain integrity for files that might change over time, generate and update reference values as needed. This ensures that the system accurately verifies the authenticity of mutable files and prevent unauthorized modifications.

**Prerequisites**

-   You have root privileges on the system.
-   You have created an IMA policy that includes IMA-appraisal rules.
-   You have generated good reference values for IMA appraisal.
-   Secure Boot is disabled.

**Procedure**

1.  Optional: Enable your chosen IMA-appraisal policy or skip this step if you only use your custom policy. Take built-in `ima_policy=appraise_tcb`{.literal} as an example:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=/boot/vmlinuz-$(uname -r) --args="ima_policy=appraise_tcb"
    ```

    -   Additionally for `s390x`{.literal} systems:

        ``` {.language-plaintext tabindex="-1"}
        # zipl
        ```

2.  Enable IMA-appraisal fix mode by adding the `ima_appraise=fix`{.literal} kernel command line parameter:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=/boot/vmlinuz-$(uname -r) --args="ima_appraise=fix"
    ```

    -   Additionally for `s390x`{.literal} systems:

        ``` {.language-plaintext tabindex="-1"}
        # zipl
        ```

3.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

4.  Optional: Load your custom IMA policy:

    ``` {.language-plaintext tabindex="-1"}
    # echo <path_to_your_custom_ima_policy> > /sys/kernel/security/ima/policy
    ```

5.  Re-label the whole system:

    ``` {.language-plaintext tabindex="-1"}
    # find / -fstype xfs -type f -uid 0 -exec head -c 0 '{}' \;
    ```

6.  Turn off IMA-appraisal fix mode by removing the `ima_appraise=fix`{.literal} kernel command line parameter:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=/boot/vmlinuz-$(uname -r) --remove-args="ima_appraise=fix"
    ```

    -   Additionally for `s390x`{.literal} systems:

        ``` {.language-plaintext tabindex="-1"}
        # zipl
        ```

7.  Enable the secure boot if it is disabled.

**Additional resources**

-   [Changing kernel command-line parameters for a single boot entry](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/configuring-kernel-command-line-parameters#changing-kernel-command-line-parameters-for-a-single-boot-entry)

### [28.2. Writing custom IMA policy](#writing-custom-ima-policy) {#writing-custom-ima-policy .title}

If built-in IMA policies from kernel parameters such as `ima_policy=tcb`{.literal} or `ima_policy=critical_data`{.literal}, or sample policies in `/usr/share/ima/policies/`{.literal}, do not meet your requirements, create custom IMA policy rules. When systemd loads `/etc/ima/ima-policy`{.literal}, it replaces the built-in IMA policy.

Warning

After you define your IMA policy, generate good reference values if the policy includes IMA-appraisal rules before you deploy it. If your policy does not include IMA-appraisal rules, you can verify the policy by running `echo /PATH-TO-YOUR-DRAFT-IMA-POLICY > /sys/kernel/security/integrity/ima/policy`{.literal}. This approach helps prevent system boot failures.

See [Generate good reference values for IMA appraisal](#generate-good-reference-values-for-ima-appraisal "28.1. Generate good reference values for IMA appraisal").

**Procedure**

-   Review the rule format and an example policy.

    An IMA policy rule uses the format `action [condition …​]`{.literal} to specify an action that is triggered under certain conditions. For example, the sample policy in `/usr/share/ima/policies/01-appraise-executable-and-lib-signatures`{.literal} includes the following rules:

    ``` {.language-bash tabindex="-1"}
    # Skip some unsupported filesystems
    # For a list of these filesystems, see
    # https://www.kernel.org/doc/Documentation/ABI/testing/ima_policy
    # PROC_SUPER_MAGIC
    dont_appraise fsmagic=0x9fa0
    …
    appraise func=BPRM_CHECK appraise_type=imasig
    ```

    The first rule, `dont_appraise fsmagic=0x9fa0`{.literal}, instructs IMA to skip appraising files in the `PROC_SUPER_MAGIC`{.literal} filesystem. The last rule, `appraise func=BPRM_CHECK appraise_type=imasig`{.literal}, enforces signature verification when a file is executed.

**Additional resources**

-   [Generate good reference values for IMA appraisal](#generate-good-reference-values-for-ima-appraisal "28.1. Generate good reference values for IMA appraisal")

### [28.3. Creating custom IMA keys by using OpenSSL](#creating-custom-ima-keys-by-using-openssl) {#creating-custom-ima-keys-by-using-openssl .title}

To secure your code, use `OpenSSL`{.literal} to generate a Certificate Signing Request (CSR) for your digital certificates.

The kernel searches the `.ima`{.literal} keyring for a code signing key to verify an Integrity Measurement Architecture (IMA) signature. Before you add a code signing key to the `.ima`{.literal} keyring, you need to ensure that IMA CA key signed this key in the `.builtin_trusted_keys`{.literal} or `.secondary_trusted_keys`{.literal} keyrings.

**Prerequisites**

-   The custom IMA CA key has the following extensions:

    -   The basic constraints extension with the CA boolean asserted.
    -   The `KeyUsage`{.literal} extension with the `keyCertSign`{.literal} bit asserted but **without** the `digitalSignature`{.literal} asserted.

-   The custom IMA code signing key falls under the following criteria:

    -   The IMA CA key signed this custom IMA code signing key.
    -   The custom key includes the `subjectKeyIdentifier`{.literal} extension.

-   UEFI Secure Boot on `x86_64`{.literal} or `aarch64`{.literal} systems or PowerVM Secure Boot on `ppc64le`{.literal} systems is enabled.

**Procedure**

1.  To generate a custom IMA CA key pair, run:

    ``` {.language-plaintext tabindex="-1"}
    # openssl req -new -x509 -utf8 -sha256 -days 3650 -batch -config ima_ca.conf -outform DER -out custom_ima_ca.der -keyout custom_ima_ca.priv
    ```

2.  Optional: To check the content of the `ima_ca.conf`{.literal} file, run:

    ``` {.language-plaintext tabindex="-1"}
    # cat ima_ca.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    [ req ]
    default_bits = 2048
    distinguished_name = req_distinguished_name
    prompt = no
    string_mask = utf8only
    x509_extensions = ca

    [ req_distinguished_name ]
    O = YOUR_ORG
    CN =  YOUR_COMMON_NAME IMA CA
    emailAddress = YOUR_EMAIL

    [ ca ]
    basicConstraints=critical,CA:TRUE
    subjectKeyIdentifier=hash
    authorityKeyIdentifier=keyid:always,issuer
    keyUsage=critical,keyCertSign,cRLSign
    ```

3.  To generate a private key and a certificate signing request (CSR) for the IMA code signing key, run:

    ``` {.language-plaintext tabindex="-1"}
    # openssl req -new -utf8 -sha256 -days 365 -batch -config ima.conf -out custom_ima.csr -keyout custom_ima.priv
    ```

4.  Optional: To check the content of the `ima.conf`{.literal} file, run:

    ``` {.language-plaintext tabindex="-1"}
    # cat ima.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    [ req ]
    default_bits = 2048
    distinguished_name = req_distinguished_name
    prompt = no
    string_mask = utf8only
    x509_extensions = code_signing

    [ req_distinguished_name ]
    O = YOUR_ORG
    CN = YOUR_COMMON_NAME IMA signing key
    emailAddress = YOUR_EMAIL

    [ code_signing ]
    basicConstraints=critical,CA:FALSE
    keyUsage=digitalSignature
    subjectKeyIdentifier=hash
    authorityKeyIdentifier=keyid:always,issuer
    ```

5.  Use the IMA CA private key to sign the CSR to create the IMA code signing certificate:

    ``` {.language-plaintext tabindex="-1"}
    # openssl x509 -req -in custom_ima.csr -days 365 -extfile ima.conf -extensions code_signing -CA custom_ima_ca.der -CAkey custom_ima_ca.priv -CAcreateserial -outform DER -out ima.der
    ```

### [28.4. Loading an IMA policy signed by your custom IMA key](#loading-an-ima-policy-signed-by-your-custom-ima-key) {#loading-an-ima-policy-signed-by-your-custom-ima-key .title}

To maintain your system integrity and meet the security requirements for your organization, you can load an Integrity Measurement Architecture (IMA) policy signed with your own custom IMA key. This ensures the system applies only trusted, authenticated policies during startup or runtime.

Note

This procedure applies only to `x86_64`{.literal} and `aarch64`{.literal} systems with UEFI Secure Boot enabled, and to `ppc64le`{.literal} systems running PowerVM Secure Boot.

**Prerequisites**

-   You must have root privileges on your system.
-   UEFI Secure Boot is enabled for Red Hat Enterprise Linux or the kernel is booted with the `ima_policy=secure_boot`{.literal} parameter to ensure only signed IMA policy can be loaded.
-   The custom IMA CA key has been added to the MOK list. For more information, see [Enrolling public key on target system by adding the public key to the MOK list](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot#enrolling-public-key-on-target-system-by-adding-the-public-key-to-the-mok-list).
-   The kernel version is 5.14 or later.
-   Good reference values have been generated for the IMA policy. For more information, see [Generate good reference values for IMA appraisal](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/extending-customizing-and-troubleshooting-kernel-integrity-subsystem#generate-good-reference-values-for-ima-appraisal).

**Procedure**

1.  Add your custom IMA code signing key to the `.ima`{.literal} keyring:

    ``` {.language-plaintext tabindex="-1"}
    # keyctl padd asymmetric <KEY_SUBJECT> %:.ima < <PATH_TO_YOUR_CUSTOM_IMA_KEY>
    ```

2.  Prepare your IMA policy and sign it with your custom IMA code signing key:

    ``` {.language-plaintext tabindex="-1"}
    # evmctl ima_sign <PATH_TO_YOUR_CUSTOM_IMA_POLICY> -k <PATH_TO_YOUR_CUSTOM_IMA_KEY>
    ```

3.  Load the signed IMA policy:

    ``` {.language-plaintext tabindex="-1"}
    # echo <PATH_TO_YOUR_CUSTOM_SIGNED_IMA_POLICY> > /sys/kernel/security/ima/policy
    ```

4.  Verify that the policy loaded successfully:

    ``` {.language-plaintext tabindex="-1"}
    # *echo $?*
    ```

    ``` {.language-plaintext tabindex="-1"}
    0
    ```

    `0`{.literal}

    :   indicates that the IMA policy was loaded successfully. If the command returns a nonzero value, the IMA policy was not loaded successfully.

        Warning

        Do not skip this step. If you do, your system might fail to boot and you need to recover your system.

        If the IMA policy fails to load, repeat the steps 2 and 3 to fix the issue.

5.  Copy the signed IMA policy to `/etc/ima/ima-policy`{.literal} to enable systemd load it automatically on boot:

    ``` {.language-plaintext tabindex="-1"}
    # cp --preserve=xattr <PATH_TO_YOUR_CUSTOM_IMA_POLICY> /etc/ima/ima-policy
    ```

6.  Copy your custom IMA key to the `/etc/keys/ima/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp <PATH_TO_YOUR_CUSTOM_IMA_KEY> /etc/keys/ima/
    ```

7.  Copy the `dracut`{.literal} integrity configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # *cp --preserve=xattr /usr/share/ima/dracut-98-integrity.conf /etc/dracut.conf.d/98-integrity.conf*
    ```

8.  Rebuild the initial RAM disk:

    ``` {.language-plaintext tabindex="-1"}
    # *dracut -f*
    ```

    -   Additionally for `s390x`{.literal} systems:

        ``` {.language-plaintext tabindex="-1"}
        # zipl
        ```

**Verification**

-   Verify that the IMA policy is loaded successfully:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/kernel/security/ima/policy
    ```

    The output should include the rules from your custom IMA policy.

### [28.5. Troubleshooting systemd failure to load the IMA policy](#troubleshooting-systemd-failure-to-load-the-ima-policy) {#troubleshooting-systemd-failure-to-load-the-ima-policy .title}

When systemd does not load `/etc/ima/ima-policy`{.literal}, the system hangs with a `systemd[1]: Freezing execution`{.literal} error message.

The failure can appear as follows:

``` {.language-plaintext tabindex="-1"}
[    5.829882] ima: policy update failed
[    5.830094] ima: signed policy file (specified as an absolute pathname) required
[!!!!!!] Failed to load IMA policy.
…
[    5.859994] systemd[1]: Freezing execution.
```

There are three methods that you can use to recover your system:

-   **Turn off Secure Boot**: Use this method if the error indicates a missing signature on a UEFI system.
-   **Booting with `init=/bin/bash`{.literal}**: Use this method to open a shell and fix the policy file.
-   **Booting with `initcall_blacklist=init_ima`{.literal}**: Use this method to start the system with IMA disabled.

#### [28.5.1. Turn off Secure Boot](#turn-off-secure-boot) {#turn-off-secure-boot .title}

If a policy lacks a signature, the kernel prevents it from loading and logs specific error messages.

``` {.language-bash tabindex="-1"}
[    5.661906] ima: policy update failed
[    5.662290] ima: signed policy file (specified as an absolute pathname) required
[    5.662496] systemd[1]: Failed to load the IMA custom policy file /etc/ima/ima-policy1: Permission denied
[    5.662663] ima: policy update failed
[    5.662856] audit: type=1800 audit(1744968172.925:7): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=system_u:system_r:init_t:s0 op=appraise_data cause=IMA-signature-required comm="systemd" name="/etc/ima/ima-policy" dev="vda3" ino=25679834 res=0 errno=0
[    5.663205] audit: type=1802 audit(1744968172.925:8): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=system_u:system_r:init_t:s0 op=policy_update cause=failed comm="systemd" res=0 errno=0
[!!!!!!] Failed to load IMA policy.
```

As a workaround, you can turn off Secure Boot temporarily and follow [Loading an IMA policy signed by your custom IMA key](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/extending-customizing-and-troubleshooting-kernel-integrity-subsystem#loading-an-ima-policy-signed-by-your-custom-ima-key) to fix the issue.

#### [28.5.2. Booting the system with the init=/bin/bash kernel parameter](#booting-the-system-with-the-init-bin-bash-kernel-parameter) {#booting-the-system-with-the-initbinbash-kernel-parameter .title}

To start the system with the `init=/bin/bash`{.literal} kernel parameter, add it to the boot loader entry and run the required commands in the recovery shell. You can then correct and verify the IMA policy before rebooting normally.

**Procedure**

1.  Modify the boot loader entry and add the `init=/bin/bash`{.literal} kernel parameter.

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel="$(grubby --default-kernel)" --args="init=/bin/bash"
    ```

2.  After you access the shell, remount the system with write permissions:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o remount,rw /
    ```

3.  Rename `/etc/ima/ima-policy`{.literal} to `/etc/ima/ima-policy.bak`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mv /etc/ima/ima-policy /etc/ima/ima-policy.bak
    ```

4.  Enable the `SysRq`{.literal} magic key:

    ``` {.language-plaintext tabindex="-1"}
    # echo 1 > /proc/sys/kernel/sysrq
    ```

5.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    # printf "s\nb" > /proc/sysrq-trigger
    ```

6.  Resolve any issues in `/etc/ima/ima-policy.bak`{.literal} and verify that the policy can be loaded:

    ``` {.language-plaintext tabindex="-1"}
    # echo /etc/ima/ima-policy.bak >> /sys/kernel/security/integrity/ima/policy
    ```

7.  Rename `/etc/ima/ima-policy.bak`{.literal} to `/etc/ima/ima-policy`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mv /etc/ima/ima-policy.bak /etc/ima/ima-policy
    ```

#### [28.5.3. Booting the system with initcall_blacklist=init_ima kernel parameter](#booting-the-system-with-initcall-blacklist-init-ima-kernel-parameter) {#booting-the-system-with-initcall_blacklistinit_ima-kernel-parameter .title}

To start the system with the `initcall_blacklist=init_ima`{.literal} kernel parameter when the system hangs with `systemd[1]: Freezing execution`{.literal}, add the parameter to the boot loader entry and run the required commands. You can then correct and verify the IMA policy before rebooting normally.

**Procedure**

1.  Modify the boot loader entry and add the `initcall_blacklist=init_ima`{.literal} kernel parameter.

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel="$(grubby --default-kernel)" --args="initcall_blacklist=init_ima"
    ```

2.  Rename `/etc/ima/ima-policy`{.literal} to `/etc/ima/ima-policy.bak`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mv /etc/ima/ima-policy /etc/ima/ima-policy.bak
    ```

3.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reboot
    ```

4.  Resolve any issues in `/etc/ima/ima-policy.bak`{.literal} and verify that the policy can be loaded:

    ``` {.language-plaintext tabindex="-1"}
    # echo /etc/ima/ima-policy.bak >> /sys/kernel/security/integrity/ima/policy
    ```

5.  Rename `/etc/ima/ima-policy.bak`{.literal} to `/etc/ima/ima-policy`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mv /etc/ima/ima-policy.bak /etc/ima/ima-policy
    ```

### [28.6. Signing custom built packages](#signing-custom-built-packages) {#signing-custom-built-packages .title}

To maintain the integrity of your system, it is important to sign custom built packages before deployment. With the `rpm-sign`{.literal} tool and IMA code signing key, you can sign your custom built packages.

**Prerequisites**

-   You have root privileges on your system.
-   You have a custom built package that you want to sign.
-   You have the IMA code signing key.
-   You have the `rpm-sign`{.literal} tool installed.
-   Custom IMA keys are created. See [Creating custom IMA keys by using OpenSSL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/extending-customizing-and-troubleshooting-kernel-integrity-subsystem#creating-custom-ima-keys-using-openssl).

**Procedure**

1.  Use `rpmsign –signfiles`{.literal} to sign package files:

    ``` {.language-plaintext tabindex="-1"}
    # rpmsign --define "gpg_name _<GPG_KEY_NAME>" --addsign --signfiles --fskpass --fskpath=<PATH_TO_YOUR_PRIVATE_IMA_CODE_SIGNING_KEY> <PATH_TO_YOUR_RPM>
    ```

    `--define "`{.literal}*`gpg_name _<GPG_KEY_NAME>`{.literal}*`"`{.literal}
    :   The GPG key signs the package, and the IMA code signing key signs each file in the package.

    `--addsign`{.literal}
    :   Adds the signature to the package.

    `--signfiles`{.literal}
    :   Signs each file in the package.

    `--fskpass`{.literal}
    :   Avoids repeatedly entering the password for the IMA code signing key.

    `--fskpath`{.literal}
    :   Specifies the path to the IMA code signing key.

**Verification**

-   To verify that the package is signed, you can use the following command:

    ``` {.language-plaintext tabindex="-1"}
    # rpm -q --queryformat "[%{FILENAMES} %{FILESIGNATURES}\n] <PATH_TO_YOUR_RPM>"
    ```

    ``` {.language-plaintext tabindex="-1"}
    /usr/bin/YOUR_BIN 030204...
    /usr/lib/YOUR_LIB.so 030204...
    ...
    ```

**Additional resources**

-   [Packaging software with RPM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/packaging_and_distributing_software/packaging-software-with-rpm)

### [28.7. Selecting between IMA and fapolicyd](#selecting-between-ima-and-fapolicyd) {#selecting-between-ima-and-fapolicyd .title}

IMA and `fapolicyd`{.literal} are two different tools for enforcing file integrity. IMA is a kernel module that enforces file integrity by verifying the integrity of files at boot time. `fapolicyd`{.literal} is a daemon that enforces file integrity by verifying the integrity of files at runtime.

The following list can help you determine which tool meets your requirements:

-   IMA verifies digital signatures to ensure integrity, while `fapolicyd`{.literal} currently supports only hash-based verification.
-   IMA operates in kernel space, while `fapolicyd`{.literal} operates in user space.
-   `fapolicyd`{.literal} supports basic integrity verification by checking file size and can also verify reference hash values stored in `security.ima`{.literal}.
-   IMA and `fapolicyd`{.literal} use different policy syntax. For example, `fapolicyd`{.literal} supports path-based policies, but IMA does not.

## [Chapter 29. Using systemd to manage resources used by applications](#using-systemd-to-manage-resources-used-by-applications) {#chapter-29.-using-systemd-to-manage-resources-used-by-applications .title}

Red Hat Enterprise Linux 10 binds `cgroup`{.literal} hierarchies to the `systemd`{.literal} unit tree, moving resource management from processes to applications. Manage resources with `systemctl`{.literal} or `systemd`{.literal} unit files. `systemd`{.literal} applies configuration to process groups by using kernel system calls, `cgroups`{.literal}, and namespaces.

Note

You can review the full set of configuration options for `systemd`{.literal} in the following manual pages:

-   `systemd.resource-control(5)`{.literal}
-   `systemd.exec(5)`{.literal}

### [29.1. Role of systemd in resource management](#role-of-systemd-in-resource-management) {#role-of-systemd-in-resource-management .title}

The systemd system and service manager provides service management, supervision, and resource management capabilities for system services and applications.

The systemd system and service manager:

-   ensures that managed services start at the right time and in the correct order during the boot process.
-   ensures that managed services run smoothly to use the underlying hardware platform optimally.
-   provides capabilities to define resource management policies.
-   provides capabilities to tune various options, which can improve the performance of the service.

Important

In general, it is advisable to you use systemd for controlling the usage of system resources. You must not manually configure the cgroups virtual file system unless it is a special case.

### [29.2. Distribution models of system sources](#distribution-models-of-system-sources) {#distribution-models-of-system-sources .title}

To control system resource usage, apply distribution models such as weights, limits, and protections. These settings determine how resources like CPU and memory are shared among control groups (cgroups).

Distribution models of system sources include the following options:

Weights

:   You can distribute the resource by adding up the weights of all sub-groups and giving each sub-group the fraction matching its ratio against the sum.

    For example, if you have 10 cgroups, each with weight of value 100, the sum is 1000. Each cgroup receives one tenth of the resource.

    Weight is usually used to distribute stateless resources. For example, the *CPUWeight=* option is an implementation of this resource distribution model.

Limits

:   A cgroup can consume up to the configured amount of the resource. The sum of sub-group limits can exceed the limit of the parent cgroup. Therefore it is possible to overcommit resources in this model.

    For example, the *MemoryMax=* option is an implementation of this resource distribution model.

Protections

:   You can configure a protected amount of a resource for a cgroup. If the resource usage is less than the protection boundary, the kernel will try not to penalize this cgroup in favor of other cgroups that compete for the same resource. An overcommit is also possible.

    For example the *MemoryLow=* option is an implementation of this resource distribution model.

Allocations
:   Exclusive allocations of an absolute amount of a finite resource. An overcommit is not possible. An example of this resource type in Linux is the real-time budget.

unit file option

:   A setting for resource control configuration.

    For example, you can configure CPU resource with options such as *CPUAccounting=*, or *CPUQuota=*. Similarly, you can configure memory or I/O resources with options such as *AllowedMemoryNodes=* and *IOAccounting=*.

### [29.3. Allocating system resources using systemd](#allocating-system-resources-using-systemd) {#allocating-system-resources-using-systemd .title}

Allocating system resources by using systemd involves creating and managing systemd services and units. You can configure them to start, stop, or restart at specific times or in response to certain system events. You can change unit file options for your service or use the `systemctl`{.literal} command.

**Procedure**

-   By using the `systemctl`{.literal} command.

    a.  Check the assigned values for the service of your choice:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl show --property <unit file option> <service name>
        ```

    b.  Set the required value of the CPU time allocation policy option:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl set-property <service name> <unit file option>=<value>
        ```

        See `systemd.resource-control(5)`{.literal} and `systemd.exec(5)`{.literal} man pages for more information.

**Verification**

-   Check the newly assigned values for the service of your choice:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl show --property <unit file option> <service name>
    ```

### [29.4. Overview of systemd hierarchy for cgroups](#overview-of-systemd-hierarchy-for-cgroups) {#overview-of-systemd-hierarchy-for-cgroups .title}

Systemd organizes processes in control groups by using `slice`{.literal}, `scope`{.literal}, and `service`{.literal} units. You can modify this hierarchy by creating custom unit files or by using `systemctl`{.literal}. Systemd automatically mounts controller hierarchies at `/sys/fs/cgroup/`{.literal}.

For resource control, you can use the following three systemd unit types:

Service

:   A process or a group of processes, which systemd started according to a unit configuration file.

    Services encapsulate the specified processes so that they can be started and stopped as one set. Services are named in the following way:

    ``` {.language-plaintext tabindex="-1"}
    <name>.service
    ```

Scope

:   A group of externally created processes. Scopes encapsulate processes that are started and stopped by the arbitrary processes through the `fork()`{.literal} function and then registered by systemd at runtime. For example, user sessions, containers, and virtual machines are treated as scopes. Scopes are named as follows:

    ``` {.language-plaintext tabindex="-1"}
    <name>.scope
    ```

Slice

:   A group of hierarchically organized units. Slices organize a hierarchy in which scopes and services are placed.

    The actual processes are contained in scopes or in services. Every name of a slice unit corresponds to the path to a location in the hierarchy.

    The dash (`-`{.literal}) character acts as a separator of the path components to a slice from the `-.slice`{.literal} root slice. In the following example:

    ``` {.language-plaintext tabindex="-1"}
    <parent-name>.slice
    ```

    `parent-name.slice`{.literal} is a sub-slice of `parent.slice`{.literal}, which is a sub-slice of the `-.slice`{.literal} root slice. `parent-name.slice`{.literal} can have its own sub-slice named `parent-name-name2.slice`{.literal}, and so on.

The `service`{.literal}, the `scope`{.literal}, and the `slice`{.literal} units directly map to objects in the control group hierarchy. When these units are activated, they map directly to control group paths built from the unit names.

The following is an abbreviated example of a control group hierarchy:

``` {.language-plaintext tabindex="-1"}
Control group /:
-.slice
├─user.slice
│ ├─user-42.slice
│ │ ├─session-c1.scope
│ │ │ ├─ 967 gdm-session-worker [pam/gdm-launch-environment]
│ │ │ ├─1035 /usr/libexec/gdm-x-session gnome-session --autostart /usr/share/gdm/greeter/autostart
│ │ │ ├─1054 /usr/libexec/Xorg vt1 -displayfd 3 -auth /run/user/42/gdm/Xauthority -background none -noreset -keeptty -verbose 3
│ │ │ ├─1212 /usr/libexec/gnome-session-binary --autostart /usr/share/gdm/greeter/autostart
│ │ │ ├─1369 /usr/bin/gnome-shell
│ │ │ ├─1732 ibus-daemon --xim --panel disable
│ │ │ ├─1752 /usr/libexec/ibus-dconf
│ │ │ ├─1762 /usr/libexec/ibus-x11 --kill-daemon
│ │ │ ├─1912 /usr/libexec/gsd-xsettings
│ │ │ ├─1917 /usr/libexec/gsd-a11y-settings
│ │ │ ├─1920 /usr/libexec/gsd-clipboard
…​
├─init.scope
│ └─1 /usr/lib/systemd/systemd --switched-root --system --deserialize 18
└─system.slice
  ├─rngd.service
  │ └─800 /sbin/rngd -f
  ├─systemd-udevd.service
  │ └─659 /usr/lib/systemd/systemd-udevd
  ├─chronyd.service
  │ └─823 /usr/sbin/chronyd
  ├─auditd.service
  │ ├─761 /sbin/auditd
  │ └─763 /usr/sbin/sedispatch
  ├─accounts-daemon.service
  │ └─876 /usr/libexec/accounts-daemon
  ├─example.service
  │ ├─ 929 /bin/bash /home/jdoe/example.sh
  │ └─4902 sleep 1
  …​
```

This example shows that services and scopes contain processes and are placed in slices that do not contain processes of their own.

**Additional resources**

-   [Managing system services with systemctl](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/managing-system-services-with-systemctl)
-   [Introducing kernel resource controllers](#introducing-kernel-resource-controllers "30.2. Introducing kernel resource controllers")

### [29.5. Listing systemd units](#listing-systemd-units) {#listing-systemd-units .title}

To list systemd units, use the system and service manager commands.

**Procedure**

-   List all active units on the system with the `systemctl`{.literal} utility. At the command line, you see output similar to the following example:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl
    ```

    ``` {.language-plaintext tabindex="-1"}
    UNIT                                                LOAD   ACTIVE SUB       DESCRIPTION
    ...
    init.scope                                          loaded active running   System and Service Manager
    session-2.scope                                     loaded active running   Session 2 of user jdoe
    abrt-ccpp.service                                   loaded active exited    Install ABRT coredump hook
    abrt-oops.service                                   loaded active running   ABRT kernel log watcher
    abrt-vmcore.service                                 loaded active exited    Harvest vmcores for ABRT
    abrt-xorg.service                                   loaded active running   ABRT Xorg log watcher
    ...
    -.slice                                             loaded active active    Root Slice
    machine.slice                                       loaded active active    Virtual Machine and Container Slice system-getty.slice                                                                       loaded active active    system-getty.slice
    system-lvm2\x2dpvscan.slice                         loaded active active    system-lvm2\x2dpvscan.slice
    system-sshd\x2dkeygen.slice                         loaded active active    system-sshd\x2dkeygen.slice
    system-systemd\x2dhibernate\x2dresume.slice         loaded active active    system-systemd\x2dhibernate\x2dresume>
    system-user\x2druntime\x2ddir.slice                 loaded active active    system-user\x2druntime\x2ddir.slice
    system.slice                                        loaded active active    System Slice
    user-1000.slice                                     loaded active active    User Slice of UID 1000
    user-42.slice                                       loaded active active    User Slice of UID 42
    user.slice                                          loaded active active    User and Session Slice
    ...
    ```

    `UNIT`{.literal}
    :   A name of a unit that also reflects the unit position in a control group hierarchy. The units relevant for resource control are a *slice*, a *scope*, and a *service*.

    `LOAD`{.literal}
    :   Indicates whether the unit configuration file was properly loaded. If the unit file failed to load, the field provides the state *error* instead of *loaded*. Other unit load states are: *stub*, *merged*, and *masked*.

    `ACTIVE`{.literal}
    :   The high-level unit activation state, which is a generalization of `SUB`{.literal}.

    `SUB`{.literal}
    :   The low-level unit activation state. The range of possible values depends on the unit type.

    `DESCRIPTION`{.literal}
    :   The description of the unit content and functionality.

-   List all active and inactive units:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl --all
    ```

-   Limit the amount of information in the output:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl --type service,masked
    ```

    The `--type`{.literal} option requires a comma-separated list of unit types such as a *service* and a *slice*, or unit load states such as *loaded* and *masked*.

    See `systemd.resource-control(5)`{.literal} and `systemd.exec(5)`{.literal} man pages on your system for more information.

**Additional resources**

-   [Managing system services with systemctl](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/managing-system-services-with-systemctl)

### [29.6. Viewing systemd cgroups hierarchy](#viewing-systemd-cgroups-hierarchy) {#viewing-systemd-cgroups-hierarchy .title}

Display control groups (cgroups) hierarchy and processes running in specific cgroups.

**Procedure**

-   Display the whole cgroups hierarchy on your system with the `systemd-cgls`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    # systemd-cgls
    ```

    ``` {.language-plaintext tabindex="-1"}
    Control group /:
    -.slice
    ├─user.slice
    │ ├─user-42.slice
    │ │ ├─session-c1.scope
    │ │ │ ├─ 965 gdm-session-worker [pam/gdm-launch-environment]
    │ │ │ ├─1040 /usr/libexec/gdm-x-session gnome-session --autostart /usr/share/gdm/greeter/autostart
    ...
    ├─init.scope
    │ └─1 /usr/lib/systemd/systemd --switched-root --system --deserialize 18
    └─system.slice
      ...
      ├─example.service
      │ ├─6882 /bin/bash /home/jdoe/example.sh
      │ └─6902 sleep 1
      ├─systemd-journald.service
        └─629 /usr/lib/systemd/systemd-journald
      ...
    ```

    The example output returns the entire cgroups hierarchy, where the highest level is formed by *slices*.

-   Display the cgroups hierarchy filtered by a resource controller with the `systemd-cgls <`{.literal}*`resource_controller`{.literal}*`>`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    # systemd-cgls memory
    ```

    ``` {.language-plaintext tabindex="-1"}
    Controller memory; Control group /:
    ├─1 /usr/lib/systemd/systemd --switched-root --system --deserialize 18
    ├─user.slice
    │ ├─user-42.slice
    │ │ ├─session-c1.scope
    │ │ │ ├─ 965 gdm-session-worker [pam/gdm-launch-environment]
    ...
    └─system.slice
      |
      ...
      ├─chronyd.service
      │ └─844 /usr/sbin/chronyd
      ├─example.service
      │ ├─8914 /bin/bash /home/jdoe/example.sh
      │ └─8916 sleep 1
      ...
    ```

    The example output lists the services that interact with the selected controller.

-   Display detailed information about a certain unit and its part of the cgroups hierarchy with the `systemctl status <`{.literal}*`system_unit`{.literal}*`>`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status example.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    ● example.service - My example service
       Loaded: loaded (/usr/lib/systemd/system/example.service; enabled; vendor preset: disabled)
       Active: active (running) since Tue 2019-04-16 12:12:39 CEST; 3s ago
     Main PID: 17737 (bash)
        Tasks: 2 (limit: 11522)
       Memory: 496.0K (limit: 1.5M)
       CGroup: /system.slice/example.service
               ├─17737 /bin/bash /home/jdoe/example.sh
               └─17743 sleep 1
    Apr 16 12:12:39 redhat systemd[1]: Started My example service.
    Apr 16 12:12:39 redhat bash[17737]: The current time is Tue Apr 16 12:12:39 CEST 2019
    Apr 16 12:12:40 redhat bash[17737]: The current time is Tue Apr 16 12:12:40 CEST 2019
    ```

### [29.7. Viewing cgroups of processes](#viewing-cgroups-of-processes) {#viewing-cgroups-of-processes .title}

A process belongs to a *control group* (cgroup). `/proc/`{.literal}*`PID`{.literal}*`/cgroup`{.literal} records its cgroup path, and controllers plus controller-specific configuration files appear under the matching path in `/sys/fs/cgroup/`{.literal}.

**Procedure**

1.  To view which cgroup a process belongs to, run the \# **cat /proc/\<*PID*\>/cgroup** command:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/2467/cgroup
    ```

    ``` {.language-plaintext tabindex="-1"}
    0::/system.slice/example.service
    ```

    The example output relates to a process of interest. In this case, it is a process identified by `PID 2467`{.literal}, which belongs to the `example.service`{.literal} unit. You can check if the process was placed in a correct control group as defined by the systemd unit file specifications.

2.  Display which controllers the cgroup uses:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/fs/cgroup/system.slice/example.service/cgroup.controllers
    ```

    ``` {.language-plaintext tabindex="-1"}
    memory pids
    ```

3.  List configuration files and other cgroup files in the cgroup directory for the `example.service`{.literal} cgroup:

    ``` {.language-plaintext tabindex="-1"}
    # ls /sys/fs/cgroup/system.slice/example.service/
    ```

    ``` {.language-plaintext tabindex="-1"}
    cgroup.controllers
    cgroup.events
    ...
    cpu.pressure
    cpu.stat
    io.pressure
    memory.current
    memory.events
    ...
    pids.current
    pids.events
    pids.max
    ```

    The version 1 hierarchy of cgroups uses a per-controller model. Therefore the output from the `/proc/`{.literal}*`PID`{.literal}*`/cgroup`{.literal} file shows which cgroups under each controller the PID belongs to. You can find the cgroups under the controller directories at `/sys/fs/cgroup/`{.literal}*`<controller_name>`{.literal}*`/`{.literal}.

    Refer to the `/usr/share/doc/kernel-doc-<kernel_version>/Documentation/admin-guide/cgroup-v2.rst`{.literal} file (after installing the `kernel-doc`{.literal} package) for more information.

**Additional resources**

-   [Introducing kernel resource controllers](#introducing-kernel-resource-controllers "30.2. Introducing kernel resource controllers")

### [29.8. Monitoring resource consumption](#monitoring-resource-consumption) {#monitoring-resource-consumption .title}

To view a list of running control groups (cgroups) and their real-time resource consumption, use the monitoring tools.

**Procedure**

1.  Display a dynamic account of currently running cgroups with the `systemd-cgtop`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # systemd-cgtop
    ```

    ``` {.language-plaintext tabindex="-1"}
    Control Group                            Tasks   %CPU   Memory  Input/s Output/s
    /                                          607   29.8     1.5G        -        -
    /system.slice                              125      -   428.7M        -        -
    /system.slice/ModemManager.service           3      -     8.6M        -        -
    /system.slice/NetworkManager.service         3      -    12.8M        -        -
    /system.slice/accounts-daemon.service        3      -     1.8M        -        -
    /system.slice/boot.mount                     -      -    48.0K        -        -
    /system.slice/chronyd.service                1      -     2.0M        -        -
    /system.slice/cockpit.socket                 -      -     1.3M        -        -
    /system.slice/colord.service                 3      -     3.5M        -        -
    /system.slice/crond.service                  1      -     1.8M        -        -
    /system.slice/cups.service                   1      -     3.1M        -        -
    /system.slice/dev-hugepages.mount            -      -   244.0K        -        -
    /system.slice/dev-mapper-rhel\x2dswap.swap   -      -   912.0K        -        -
    /system.slice/dev-mqueue.mount               -      -    48.0K        -        -
    /system.slice/example.service                2      -     2.0M        -        -
    /system.slice/firewalld.service              2      -    28.8M        -        -
    ...
    ```

    The example output displays currently running cgroups ordered by their resource usage (CPU, memory, disk I/O load). The list refreshes every 1 second by default. Therefore, it offers a dynamic insight into the actual resource usage of each control group.

    See the `systemd-cgtop(1)`{.literal} man page on your system for more information.

### [29.9. Using systemd unit files to set limits for applications](#using-systemd-unit-files-to-set-limits-for-applications) {#using-systemd-unit-files-to-set-limits-for-applications .title}

Set resource limits for applications by modifying systemd unit files. Configure memory, CPU, or other resource constraints to control how applications use system resources.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Edit the `/usr/lib/systemd/system/example.service`{.literal} file to limit the memory usage of a service:

    ``` {.language-plaintext tabindex="-1"}
    …​
    [Service]
    MemoryMax=1500K
    …​
    ```

    The configuration limits the maximum memory that the processes in a control group cannot exceed. The `example.service`{.literal} service is part of such a control group which has imposed limitations. You can use suffixes K, M, G, or T to identify Kilobyte, Megabyte, Gigabyte, or Terabyte as a unit of measurement.

2.  Reload all unit configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

3.  Restart the service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart example.service
    ```

**Verification**

1.  Check that the changes took effect:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/fs/cgroup/system.slice/example.service/memory.max
    ```

    ``` {.language-plaintext tabindex="-1"}
    1536000
    ```

    This output shows that the memory consumption was limited at around 1,500 KB.

**Additional resources**

-   [Managing system services with systemctl](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/managing-system-services-with-systemctl)

### [29.10. Using the systemctl command to set CPU affinity for applications](#using-the-systemctl-command-to-set-cpu-affinity-for-applications) {#using-the-systemctl-command-to-set-cpu-affinity-for-applications .title}

CPU affinity settings restrict the access of a particular process to some CPUs. Effectively, the CPU scheduler never schedules the process to run on the CPU that is not in the affinity mask of the process.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Check the `CPUAffinity`{.literal} value for the service:

    The default CPU affinity mask applies to all systemd services. To set affinity for one service, use the `CPUAffinity=`{.literal} unit file option with `systemctl set-property`{.literal}. The option accepts a list of CPUs or CPU ranges that systemd merges into the affinity mask. You can also configure a global default in the `[Manager]`{.literal} section of `/etc/systemd/system.conf`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl show --property CPUAffinity <service name>
    ```

2.  As the root user, set the `CPUAffinity`{.literal} value for the CPU ranges used as the affinity mask:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl set-property <service name> CPUAffinity=<value>
    ```

3.  Restart the service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart <service name>
    ```

**Additional resources**

-   [Setting global default CPU affinity through manager configuration](#setting-global-default-cpu-affinity-through-manager-configuration "29.11. Setting global default CPU affinity through manager configuration")

### [29.11. Setting global default CPU affinity through manager configuration](#setting-global-default-cpu-affinity-through-manager-configuration) {#setting-global-default-cpu-affinity-through-manager-configuration .title}

To set a global default CPU affinity, configure the `CPUAffinity`{.literal} option in `/etc/systemd/system.conf`{.literal}. This applies to PID 1 and its child processes, but you can override this setting per service.

Set the default CPU affinity mask for all systemd services by using the `/etc/systemd/system.conf`{.literal} file.

**Procedure**

1.  Set the CPU numbers for the `CPUAffinity=`{.literal} option in the `[Manager]`{.literal} section of the `/etc/systemd/system.conf`{.literal} file.

2.  Save the edited file and reload the systemd service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

3.  Reboot the server to apply the changes.

    See the `systemd.resource-control(5)`{.literal} man page on your system for more information.

### [29.12. Configuring NUMA policies by using systemd](#configuring-numa-policies-by-using-systemd) {#configuring-numa-policies-by-using-systemd .title}

To optimize memory access performance for applications on Non-Uniform Memory Access (NUMA) systems, configure NUMA policies for services by using systemd unit files.

On NUMA systems, memory close to the CPU has lower latency (local memory) than memory that is local for a different CPU (foreign memory) or is shared between a set of CPUs.

In terms of the Linux kernel, NUMA policy governs where (for example, on which NUMA nodes) the kernel allocates physical memory pages for the process.

systemd provides unit file options `NUMAPolicy`{.literal} and `NUMAMask`{.literal} to control memory allocation policies for services.

Important

When you configure a strict NUMA policy, for example `bind`{.literal}, make sure that you also appropriately set the `CPUAffinity=`{.literal} unit file option.

**Procedure**

1.  Set the NUMA memory policy through the `NUMAPolicy`{.literal} unit file option.

    a.  Check the values of the `NUMAPolicy`{.literal} unit file option for the service of your choice:

        ``` {.language-plaintext tabindex="-1"}
        $ systemctl show --property <NUMA policy configuration option> <service name>
        ```

    b.  As a root, set the required policy type of the `NUMAPolicy`{.literal} unit file option:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl set-property <service name> NUMAPolicy=<value>
        ```

2.  Restart the service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart <service name>
    ```

**Additional resources**

-   [NUMA policy configuration options for systemd](#numa-policy-configuration-options-for-systemd "29.13. NUMA policy configuration options for systemd")

### [29.13. NUMA policy configuration options for systemd](#numa-policy-configuration-options-for-systemd) {#numa-policy-configuration-options-for-systemd .title}

Non-Uniform Memory Access (NUMA) policies for processes include `NUMAPolicy`{.literal} and `NUMAMask`{.literal}. The policy type and node lists determine how the system controls memory allocation.

Systemd unit options for NUMA policy include:

`NUMAPolicy`{.literal}

:   Controls the NUMA memory policy of the executed processes. You can use these policy types:

    -   default
    -   preferred
    -   bind
    -   interleave
    -   local

`NUMAMask`{.literal}

:   Controls the NUMA node list that is associated with the selected NUMA policy.

    Note that you do not have to specify the `NUMAMask`{.literal} option for the following policies:

    -   default

    -   local

        For the preferred policy, the list specifies only a single NUMA node.

See `systemd.resource-control(5)`{.literal}, `systemd.exec(5)`{.literal}, and `set_mempolicy(2)`{.literal} man pages on your system for more information.

### [29.14. Creating transient cgroups using systemd-run command](#creating-transient-control-groups) {#creating-transient-cgroups-using-systemd-run-command .title}

To limit resources consumed by a service or scope during its runtime, use transient control groups (cgroups).

**Procedure**

-   To create a transient control group, use the `systemd-run`{.literal} command in the following format:

    ``` {.language-plaintext tabindex="-1"}
    # systemd-run --unit=<name> --slice=<name>.slice <command>
    ```

    This command creates and starts a transient service or a scope unit and runs a custom command in such a unit.

    -   The `--unit=<name>`{.literal} option gives a name to the unit. If `--unit`{.literal} is not specified, the name is generated automatically.

    -   The `--slice=<`{.literal}*`name`{.literal}*`>.slice`{.literal} option makes your service or scope unit a member of a specified slice. Replace `<`{.literal}*`name`{.literal}*`>.slice`{.literal} with the name of an existing slice (as shown in the output of `systemctl -t slice`{.literal}), or create a new slice by passing a unique name. By default, services and scopes are created as members of the `system.slice`{.literal}.

    -   Replace `<`{.literal}*`command`{.literal}*`>`{.literal} with the command you want to enter in the service or the scope unit.

        The following message is displayed to confirm that you created and started the service or the scope successfully:

        ``` {.language-plaintext tabindex="-1"}
        # Running as unit <name>.service
        ```

-   *Optional*: Keep the unit running after its processes finished to collect runtime information:

    ``` {.language-plaintext tabindex="-1"}
    # systemd-run --unit=<name> --slice=<name>.slice --remain-after-exit <command>
    ```

    The command creates and starts a transient service unit and runs a custom command in the unit. The `--remain-after-exit`{.literal} option ensures that the service keeps running after its processes have finished.

### [29.15. Removing transient control groups](#removing-transient-control-groups) {#removing-transient-control-groups .title}

To remove transient control groups (cgroups) when they are no longer needed, use the systemd system and service manager.

Transient cgroups are automatically released when all the processes that a service or a scope unit contains finish.

**Procedure**

-   To stop the service unit with all its processes, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop <name>.service
    ```

-   To terminate one or more of the unit processes, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl kill <name>.service --kill-who=PID,…​ --signal=<signal>
    ```

    The command uses the `--kill-who`{.literal} option to select process(es) from the control group you want to terminate. To kill multiple processes at the same time, pass a comma-separated list of PIDs. The `--signal`{.literal} option determines the type of POSIX signal to be sent to the specified processes. The default signal is *SIGTERM*.

**Additional resources**

-   [Introducing control groups](#introducing-control-groups "30.1. Introducing control groups")
-   [Introducing kernel resource controllers](#introducing-kernel-resource-controllers "30.2. Introducing kernel resource controllers")
-   [Introducing control groups](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/setting-system-resource-limits-for-applications-by-using-control-groups#introducing-control-groups)
-   [Using systemd unit files to customize and optimize your system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/index)

## [Chapter 30. Setting system resource limits for applications by using control groups](#setting-system-resource-limits-for-applications-by-using-control-groups) {#chapter-30.-setting-system-resource-limits-for-applications-by-using-control-groups .title}

Use control groups (`cgroups`{.literal}) kernel functionality to control application resource usage. Set limits for system resource allocation, prioritize hardware resources for specific processes, and isolate processes from obtaining hardware resources.

### [30.1. Introducing control groups](#introducing-control-groups) {#introducing-control-groups .title}

Using the control groups Linux kernel feature, you can organize processes into hierarchically ordered groups called cgroups. You define the hierarchy by providing structure to the cgroups virtual file system, mounted by default on the `/sys/fs/cgroup/`{.literal} directory.

The systemd service manager uses cgroups to organize all units and services that it governs. Manually, you can manage the hierarchies of cgroups by creating and removing sub-directories in the `/sys/fs/cgroup/`{.literal} directory.

The resource controllers in the kernel then modify the behavior of processes in cgroups by limiting, prioritizing or allocating system resources, of those processes. These resources include the following:

-   CPU time
-   Memory
-   Network bandwidth
-   Combinations of these resources

The primary use case of cgroups is aggregating system processes and dividing hardware resources among applications and users. This makes it possible to increase the efficiency, stability, and security of your environment.

Control groups version 1

:   *Control groups version 1* (`cgroups-v1`{.literal}) provides a separate hierarchy for each resource controller. Resources such as CPU, memory, or I/O has its own control group hierarchy. You can combine different control group hierarchies so that one controller can coordinate with another in managing their individual resources. However, when the two controllers belong to different process hierarchies, the coordination is limited.

    The `cgroups-v1`{.literal} controllers were developed across a large time span, resulting in inconsistent behavior and naming of their control files.

Control groups version 2

:   *Control groups version 2* (`cgroups-v2`{.literal}) provides a single control group hierarchy against which all resource controllers are mounted.

    The control file behavior and naming is consistent among different controllers.

    Important

    RHEL 10, by default, mounts and uses `cgroups-v2`{.literal}.

For more details about `cgroups-v1`{.literal} and `cgroups-v2`{.literal}, install the `kernel-doc`{.literal} RPM package. After installation, the documentation is in the `/usr/share/doc/kernel-doc-`{.literal}*`<version>`{.literal}*`/Documentation`{.literal} directory on the local system. The `cgroups-v1`{.literal} documentation files are in the `Documentation/admin-guide/cgroup-v1/`{.literal} directory. This directory has multiple files for different controllers. The `cgroups-v2`{.literal} documentation is in the `Documentation/admin-guide/cgroup-v2.rst`{.literal} file.

**Additional resources**

-   [Introducing kernel resource controllers](#introducing-kernel-resource-controllers "30.2. Introducing kernel resource controllers")

### [30.2. Introducing kernel resource controllers](#introducing-kernel-resource-controllers) {#introducing-kernel-resource-controllers .title}

Kernel resource controllers provide the functionality of control groups. RHEL 10 supports various controllers for *control groups version 1* (`cgroups-v1`{.literal}) and *control groups version 2* (`cgroups-v2`{.literal}).

A resource controller, also called a control group subsystem, is a kernel subsystem that represents a single resource, such as CPU time, memory, network bandwidth or disk I/O. The Linux kernel provides a range of resource controllers that are mounted automatically by the systemd service manager.

You can find a list of the currently mounted resource controllers in the `/proc/cgroups`{.literal} file.

Controllers available for `cgroups-v1`{.literal}

:   -   `blkio`{.literal}: Sets limits on input/output access to and from block devices.
    -   `cpu`{.literal}: Adjusts the parameters of the default scheduler for a control group's tasks. The `cpu`{.literal} controller is mounted together with the `cpuacct`{.literal} controller on the same mount.
    -   `cpuacct`{.literal}: Creates automatic reports on CPU resources used by tasks in a control group. The `cpuacct`{.literal} controller is mounted together with the `cpu`{.literal} controller on the same mount.
    -   `cpuset`{.literal}:Restricts control group tasks to run only on a specified subset of CPUs and to direct the tasks to use memory only on specified memory nodes.
    -   `devices`{.literal}: Controls access to devices for tasks in a control group.
    -   `freezer`{.literal}: Suspends or resumes tasks in a control group.
    -   `memory`{.literal}: Sets limits on memory use by tasks in a control group and generates automatic reports on memory resources used by those tasks.
    -   `net_cls`{.literal}: Tags network packets with a class identifier (`classid`{.literal}) that enables the Linux traffic controller (the `tc`{.literal} command) to identify packets that originate from a particular control group task. A subsystem of `net_cls`{.literal}, the `net_filter`{.literal} (iptables), can also use this tag to perform actions on such packets.
    -   `net_filter`{.literal}: Tags network sockets with a firewall identifier (`fwid`{.literal}) that allows the Linux firewall to identify packets that originate from a particular control group task (by using the `iptables`{.literal} command).
    -   `net_prio`{.literal}: Sets the priority of network traffic.
    -   `pids`{.literal}: Sets limits for multiple processes and their children in a control group.
    -   `perf_event`{.literal}: Groups tasks for monitoring by the `perf`{.literal} performance monitoring and reporting utility.
    -   `rdma`{.literal}: Sets limits on Remote Direct Memory Access/InfiniBand specific resources in a control group.
    -   `hugetlb`{.literal}: Limits the usage of large size virtual memory pages by tasks in a control group.

Controllers available for `cgroups-v2`{.literal}

:   -   `io`{.literal}: Sets limits on input/output access to and from block devices.
    -   `memory`{.literal}: Sets limits on memory use by tasks in a control group and generates automatic reports on memory resources used by those tasks.
    -   `pids`{.literal}: Sets limits for multiple processes and their children in a control group.
    -   `rdma`{.literal}: Sets limits on Remote Direct Memory Access/InfiniBand specific resources in a control group.
    -   `cpu`{.literal}: Adjusts the parameters of the default scheduler for a control group's tasks and creates automatic reports on CPU resources used by tasks in a control group.
    -   `cpuset`{.literal}: Restricts control group tasks to run only on a specified subset of CPUs and to direct the tasks to use memory only on specified memory nodes. Supports only the core functionality (`cpus{,.effective}`{.literal}, `mems{,.effective}`{.literal}) with a new partition feature.
    -   `perf_event`{.literal}: Groups tasks for monitoring by the `perf`{.literal} performance monitoring and reporting utility. `perf_event`{.literal} is enabled automatically on the v2 hierarchy.

Important

A resource controller can be used either in a `cgroups-v1`{.literal} hierarchy or a `cgroups-v2`{.literal} hierarchy, not simultaneously in both.

### [30.3. Introducing namespaces](#introducing-namespaces) {#introducing-namespaces .title}

Namespaces create separate spaces for organizing and identifying software objects. This keeps them from affecting each other. As a result, each software object contains its own set of resources, for example, a mount point, a network device, or a hostname, even though they share the same system.

One of the most common technologies that use namespaces are containers.

Changes to a particular global resource are visible only to processes in that namespace and do not affect the rest of the system or other namespaces.

To inspect which namespaces a process is a member of, you can check the symbolic links in the `/proc/<`{.literal}*`PID`{.literal}*`>/ns/`{.literal} directory.

+-----------------------------------+-------------------------------------------+
| Namespace                         | Isolates                                  |
+:==================================+:==========================================+
| **Mount**                         | Mount points                              |
+-----------------------------------+-------------------------------------------+
| **UTS**                           | Hostname and NIS domain name              |
+-----------------------------------+-------------------------------------------+
| **IPC**                           | SysV IPC, POSIX message queues            |
+-----------------------------------+-------------------------------------------+
| **PID**                           | Process IDs                               |
+-----------------------------------+-------------------------------------------+
| **Network**                       | Network devices, stacks, ports, and so on |
+-----------------------------------+-------------------------------------------+
| **User**                          | User and group IDs                        |
+-----------------------------------+-------------------------------------------+
| **Control groups**                | Control group root directory              |
+-----------------------------------+-------------------------------------------+

: Table 30.1. Supported namespaces and resources which they isolate:

Show more

See `namespaces(7)`{.literal} and `cgroup_namespaces(7)`{.literal} man pages on your system for more information.

## [Chapter 31. Using cgroupfs to manually manage cgroups](#using-cgroupfs-to-manually-manage-cgroups) {#chapter-31.-using-cgroupfs-to-manually-manage-cgroups .title}

Manage `cgroup`{.literal} hierarchies by creating directories on the `cgroupfs`{.literal} virtual file system, which is mounted by default on `/sys/fs/cgroup/`{.literal}. Specify required configurations in dedicated control files.

Note

`cgroups-v1`{.literal} support is deprecated by `systemd`{.literal} and therefore, `cgroups-v1`{.literal} will be removed from future Red Hat Enterprise Linux 10 releases. You must use `cgroups-v2`{.literal} from future releases of RHEL 10.

Important

You must use `systemd`{.literal} for controlling the usage of system resources. You must not manually configure the `cgroups`{.literal} virtual file system unless it is a special case.

### [31.1. Creating cgroups and enabling controllers in cgroups-v2 file system](#creating-cgroups-and-enabling-controllers-in-cgroups-v2-file-system) {#creating-cgroups-and-enabling-controllers-in-cgroups-v2-file-system .title}

To manage control groups (cgroups), create or remove directories in the cgroups virtual file system, usually at `/sys/fs/cgroup/`{.literal}. To use controller settings, enable them for child cgroups. Create at least two levels of child cgroups to organize files and optimize controller usage.

**Prerequisites**

-   You have root permissions on the system.

**Procedure**

1.  Create the `/sys/fs/cgroup/Example/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /sys/fs/cgroup/Example/
    ```

    The `/sys/fs/cgroup/Example/`{.literal} directory defines a child group. When you create the `/sys/fs/cgroup/Example/`{.literal} directory, some `cgroups-v2`{.literal} interface files are automatically created in the directory. The `/sys/fs/cgroup/Example/`{.literal} directory also contains controller-specific files for the `memory`{.literal} and `pids`{.literal} controllers.

2.  Optional: Inspect the newly created child control group:

    ``` {.language-plaintext tabindex="-1"}
    # ll /sys/fs/cgroup/Example/
    ```

    ``` {.language-plaintext tabindex="-1"}
    -r--r--r--. 1 root root 0 Jun  1 10:33 cgroup.controllers
    -r--r--r--. 1 root root 0 Jun  1 10:33 cgroup.events
    -rw-r--r--. 1 root root 0 Jun  1 10:33 cgroup.freeze
    -rw-r--​r--. 1 root root 0 Jun  1 10:33 cgroup.procs
    ...
    -rw-r--r--. 1 root root 0 Jun  1 10:33 cgroup.subtree_control
    -r--r--r--. 1 root root 0 Jun  1 10:33 memory.events.local
    -rw-r--r--. 1 root root 0 Jun  1 10:33 memory.high
    -rw-r--r--. 1 root root 0 Jun  1 10:33 memory.low
    ...
    -r--r--r--. 1 root root 0 Jun  1 10:33 pids.current
    -r--r--r--. 1 root root 0 Jun  1 10:33 pids.events
    -rw-r--r--. 1 root root 0 Jun  1 10:33 pids.max
    ```

    The example output shows general cgroup control interface files such as `cgroup.procs`{.literal} or `cgroup.controllers`{.literal}. These files are common to all control groups, regardless of enabled controllers.

    The files such as `memory.high`{.literal} and `pids.max`{.literal} relate to the `memory`{.literal} and `pids`{.literal} controllers, which are in the root control group (`/sys/fs/cgroup/`{.literal}), and are enabled by default by systemd.

    By default, the newly created child group inherits all settings from the parent cgroup. In this case, there are no limits from the root cgroup.

3.  Verify that the required controllers are available in the `/sys/fs/cgroup/cgroup.controllers`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/fs/cgroup/cgroup.controllers
    ```

    ``` {.language-plaintext tabindex="-1"}
    cpuset cpu io memory hugetlb pids rdma
    ```

4.  Enable the required controllers. In this example it is `cpu`{.literal} and `cpuset`{.literal} controllers:

    ``` {.language-plaintext tabindex="-1"}
    # echo "+cpu" >> /sys/fs/cgroup/cgroup.subtree_control
    # echo "+cpuset" >> /sys/fs/cgroup/cgroup.subtree_control
    ```

    These commands enable the `cpu`{.literal} and `cpuset`{.literal} controllers for the immediate child groups of the `/sys/fs/cgroup/`{.literal} root control group. This includes the newly created `Example`{.literal} control group. A *child group* is where you can specify processes and apply control checks to each of the processes based on your criteria.

    Users can read the contents of the `cgroup.subtree_control`{.literal} file at any level to get an idea of what controllers are available to enable in the immediate child group.

    Note

    By default, the `/sys/fs/cgroup/cgroup.subtree_control`{.literal} file in the root control group contains `memory`{.literal} and `pids`{.literal} controllers.

5.  Enable the required controllers for child cgroups of the `Example`{.literal} control group:

    ``` {.language-plaintext tabindex="-1"}
    # echo "+cpu +cpuset" >> /sys/fs/cgroup/Example/cgroup.subtree_control
    ```

    This command ensures that the immediate child control group will *only* have controllers relevant to regulate the CPU time distribution - not to `memory`{.literal} or `pids`{.literal} controllers.

6.  Create the `/sys/fs/cgroup/Example/tasks/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /sys/fs/cgroup/Example/tasks/
    ```

    The `/sys/fs/cgroup/Example/tasks/`{.literal} directory defines a child group with files that relate purely to `cpu`{.literal} and `cpuset`{.literal} controllers. You can now assign processes to this control group and use `cpu`{.literal} and `cpuset`{.literal} controller options for your processes.

7.  Optional: Inspect the child control group:

    ``` {.language-plaintext tabindex="-1"}
    # ll /sys/fs/cgroup/Example/tasks
    ```

    ``` {.language-plaintext tabindex="-1"}
    -r--r--r--. 1 root root 0 Jun  1 11:45 cgroup.controllers
    -r--r--r--. 1 root root 0 Jun  1 11:45 cgroup.events
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cgroup.freeze
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cgroup.max.depth
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cgroup.max.descendants
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cgroup.procs
    -r--r--r--. 1 root root 0 Jun  1 11:45 cgroup.stat
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cgroup.subtree_control
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cgroup.threads
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cgroup.type
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cpu.max
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cpu.pressure
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cpuset.cpus
    -r--r--r--. 1 root root 0 Jun  1 11:45 cpuset.cpus.effective
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cpuset.cpus.partition
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cpuset.mems
    -r--r--r--. 1 root root 0 Jun  1 11:45 cpuset.mems.effective
    -r--r--r--. 1 root root 0 Jun  1 11:45 cpu.stat
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cpu.weight
    -rw-r--r--. 1 root root 0 Jun  1 11:45 cpu.weight.nice
    -rw-r--r--. 1 root root 0 Jun  1 11:45 io.pressure
    -rw-r--r--. 1 root root 0 Jun  1 11:45 memory.pressure
    ```

    Important

    The `cpu`{.literal} controller is only activated if the relevant child control group has at least 2 processes which compete for time on a single CPU.

**Verification**

-   Optional: confirm that you have created a new cgroup with only the required controllers active:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/fs/cgroup/Example/tasks/cgroup.controllers
    ```

    ``` {.language-plaintext tabindex="-1"}
    cpuset cpu
    ```

**Additional resources**

-   [Introducing kernel resource controllers](#introducing-kernel-resource-controllers "30.2. Introducing kernel resource controllers")

### [31.2. Controlling distribution of CPU time for applications by adjusting CPU weight](#controlling-distribution-of-cpu-time-for-applications-by-adjusting-cpu-weight) {#controlling-distribution-of-cpu-time-for-applications-by-adjusting-cpu-weight .title}

To regulate the distribution of CPU time to applications, assign weights to the relevant files of the `cpu`{.literal} controller in the cgroup tree.

**Prerequisites**

-   You have root permissions on the system.

-   You have applications for which you want to control distribution of CPU time.

-   You mounted `cgroups-v2`{.literal} filesystem.

-   You created a two level hierarchy of *child control groups* inside the `/sys/fs/cgroup/`{.literal} *root control group* as in the following example:

    ``` {.language-plaintext tabindex="-1"}
    ...
      ├── Example
      │   ├── g1
      │   ├── g2
      │   └── g3
    ...
    ```

-   You enabled the `cpu`{.literal} controller in the parent control group and in child control groups similarly as described in [Creating cgroups and enabling controllers in cgroups-v2 file system](#creating-cgroups-and-enabling-controllers-in-cgroups-v2-file-system "31.1. Creating cgroups and enabling controllers in cgroups-v2 file system").

**Procedure**

1.  Configure the required CPU weights to achieve resource restrictions within the control groups:

    ``` {.language-plaintext tabindex="-1"}
    # echo "150" > /sys/fs/cgroup/Example/g1/cpu.weight
    # echo "100" > /sys/fs/cgroup/Example/g2/cpu.weight
    # echo "50" > /sys/fs/cgroup/Example/g3/cpu.weight
    ```

2.  Add the applications\' PIDs to the `g1`{.literal}, `g2`{.literal}, and `g3`{.literal} child groups:

    ``` {.language-plaintext tabindex="-1"}
    # echo "33373" > /sys/fs/cgroup/Example/g1/cgroup.procs
    # echo "33374" > /sys/fs/cgroup/Example/g2/cgroup.procs
    # echo "33377" > /sys/fs/cgroup/Example/g3/cgroup.procs
    ```

    These commands ensure that the required applications become members of the `Example/g*/`{.literal} child cgroups and will get their CPU time distributed based on the configuration of those cgroups.

    The weights of the children cgroups (`g1`{.literal}, `g2`{.literal}, `g3`{.literal}) that have running processes are summed up at the level of the parent cgroup (`Example`{.literal}). The CPU resource is then distributed proportionally based on the assigned weights.

    As a result, when all processes run at the same time, the kernel allocates to each of them the proportionate CPU time based on the assigned cgroup's `cpu.weight`{.literal} file:

    +-----------------+-----------------------------+-----------------------------------+
    | Child cgroup    | `cpu.weight`{.literal} file | CPU time allocation               |
    +:================+:============================+:==================================+
    | g1              | 150                         | \~50% (150/300)                   |
    +-----------------+-----------------------------+-----------------------------------+
    | g2              | 100                         | \~33% (100/300)                   |
    +-----------------+-----------------------------+-----------------------------------+
    | g3              | 50                          | \~16% (50/300)                    |
    +-----------------+-----------------------------+-----------------------------------+

    : Table 31.1. CPU time allocation with all processes running

    Show more

    The value of the `cpu.weight`{.literal} controller file is not a percentage.

    If one process stopped running, leaving cgroup `g2`{.literal} with no running processes, the calculation would omit the cgroup `g2`{.literal} and only account weights of cgroups `g1`{.literal} and `g3`{.literal}:

    +-----------------+-----------------------------+-----------------------------------+
    | Child cgroup    | `cpu.weight`{.literal} file | CPU time allocation               |
    +:================+:============================+:==================================+
    | g1              | 150                         | \~75% (150/200)                   |
    +-----------------+-----------------------------+-----------------------------------+
    | g3              | 50                          | \~25% (50/200)                    |
    +-----------------+-----------------------------+-----------------------------------+

    : Table 31.2. CPU time allocation without g2 processes

    Show more

    Important

    If a child cgroup has multiple running processes, the CPU time allocated to the cgroup is distributed equally among its member processes.

**Verification**

1.  Verify that the applications run in the specified control groups:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/33373/cgroup /proc/33374/cgroup /proc/33377/cgroup
    ```

    ``` {.language-plaintext tabindex="-1"}
    0::/Example/g1
    0::/Example/g2
    0::/Example/g3
    ```

    The command output shows the processes of the specified applications that run in the `Example/g*/`{.literal} child cgroups.

2.  Inspect the current CPU consumption of the throttled applications:

    ``` {.language-plaintext tabindex="-1"}
    # top
    ```

    ``` {.language-plaintext tabindex="-1"}
    top - 05:17:18 up 1 day, 18:25,  1 user,  load average: 3.03, 3.03, 3.00
    Tasks:  95 total,   4 running,  91 sleeping,   0 stopped,   0 zombie
    %Cpu(s): 18.1 us, 81.6 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.3 hi,  0.0 si,  0.0 st
    MiB Mem :   3737.0 total,   3233.7 free,    132.8 used,    370.5 buff/cache
    MiB Swap:   4060.0 total,   4060.0 free,      0.0 used.   3373.1 avail Mem

        PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
      33373 root      20   0   18720   1748   1460 R  *49.5*   0.0 415:05.87 sha1sum
      33374 root      20   0   18720   1756   1464 R  *32.9*   0.0 412:58.33 sha1sum
      33377 root      20   0   18720   1860   1568 R  *16.3*   0.0 411:03.12 sha1sum
        760 root      20   0  416620  28540  15296 S   0.3   0.7   0:10.23 tuned
          1 root      20   0  186328  14108   9484 S   0.0   0.4   0:02.00 systemd
          2 root      20   0       0      0      0 S   0.0   0.0   0:00.01 kthread
    ...
    ```

    Note

    All processes run on a single CPU for clear illustration. The CPU weight applies the same principles when used on multiple CPUs.

    Notice that the CPU resource for the `PID 33373`{.literal}, `PID 33374`{.literal}, and `PID 33377`{.literal} was allocated based on the 150, 100, and 50 weights you assigned to child cgroups. The weights correspond to around 50%, 33%, and 16% allocation of CPU time for each application.

## [Chapter 32. Analyzing system performance with eBPF](#analyzing-system-performance-with-ebpf) {#chapter-32.-analyzing-system-performance-with-ebpf .title}

Use the `bpftrace`{.literal} and BPF Compiler Collection (BCC) library to create tools for analyzing Linux system performance and gathering information that is difficult to obtain through other interfaces.

### [32.1. Using the bpftrace package](#using-the-bpftrace-package) {#using-the-bpftrace-package .title}

`bpftrace`{.literal} is a powerful tracing tool for Red Hat Enterprise Linux systems that uses extended Berkeley Packet Filter (eBPF) technology. With `bpftrace`{.literal}, you can trace and analyze kernel and user-space events dynamically without modifying the kernel code.

**Procedure**

1.  Install the `bpftrace`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install bpftrace
    ```

2.  Run the test:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @ = count(); } interval:s:1 { print(@); clear(@); }'
    ```

    This command displays a high-level overview of system activity by observing the rate of system calls made.

    You are now ready to use `bpftrace`{.literal}. You can explore example scripts located at `/usr/share/bpftrace/tools/`{.literal}, learn scripts online or create your own scripts to trace events and analyze system behavior.

**Additional resources**

-   [Bpftrace](https://bpftrace.org)
-   [Example one-liners](https://github.com/bpftrace/bpftrace/blob/master/README.md#example-one-liners)
-   [Official tools](https://github.com/bpftrace/bpftrace/blob/master/tools/README.md)
-   [User tools](https://github.com/bpftrace/user-tools/blob/master/TOOLS.md)

### [32.2. Installing the bcc-tools package](#installing-the-bcc-tools-package) {#installing-the-bcc-tools-package .title}

Install the `bcc-tools`{.literal} package, which also installs the BPF Compiler Collection (BCC) library as a dependency.

**Procedure**

-   Install `bcc-tools`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install bcc-tools
    ```

    The BCC tools are installed in the `/usr/share/bcc/tools/`{.literal} directory.

**Verification**

-   Inspect the installed tools:

    ``` {.language-plaintext tabindex="-1"}
    # ls -l /usr/share/bcc/tools/
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    -rwxr-xr-x. 1 root root  4198 Dec 14 17:53 dcsnoop
    -rwxr-xr-x. 1 root root  3931 Dec 14 17:53 dcstat
    -rwxr-xr-x. 1 root root 20040 Dec 14 17:53 deadlock_detector
    -rw-r--r--. 1 root root  7105 Dec 14 17:53 deadlock_detector.c
    drwxr-xr-x. 3 root root  8192 Mar 11 10:28 doc
    -rwxr-xr-x. 1 root root  7588 Dec 14 17:53 execsnoop
    -rwxr-xr-x. 1 root root  6373 Dec 14 17:53 ext4dist
    -rwxr-xr-x. 1 root root 10401 Dec 14 17:53 ext4slower
    ...
    ```

    The `doc`{.literal} directory in the listing contains documentation for each tool.

### [32.3. Using selected bcc-tools for performance analyses](#using-selected-bcc-tools-for-performance-analyses) {#using-selected-bcc-tools-for-performance-analyses .title}

Use the pre-created programs from the BPF Compiler Collection (BCC) library to analyze system performance on a per-event basis. You can use the programs in the BCC library as examples to create additional programs.

**Prerequisites**

-   You have root permissions on the system.
-   [You have installed the bcc-tools package](#installing-the-bcc-tools-package "32.2. Installing the bcc-tools package").

**Procedure**

-   Use `execsnoop`{.literal} to examine the new system processes.

    a.  Run the `execsnoop`{.literal} program in one command line session:

        ``` {.language-plaintext tabindex="-1"}
        # /usr/share/bcc/tools/execsnoop
        ```

    b.  To create a short-lived process of the `ls`{.literal} command, in another command line session, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ ls /usr/share/bcc/tools/doc/
        ```

    c.  The command line session that runs `execsnoop`{.literal} shows the output similar to the following:

        ``` {.language-plaintext tabindex="-1"}
        PCOMM    PID    PPID   RET ARGS
        ls      8382   8287     0 /usr/bin/ls --color=auto /usr/share/bcc/tools/doc/
        ...
        ```

        The `execsnoop`{.literal} program prints a line of output for each new process that consumes system resources. It even detects processes of programs that run very shortly, such as `ls`{.literal}, and most monitoring tools would not register them.

        The `execsnoop`{.literal} output displays the following fields:

        PCOMM
        :   The process name. (`ls`{.literal})

        PID
        :   The process ID. (`8382`{.literal})

        PPID
        :   The parent process ID. (`8287`{.literal})

        RET
        :   The return value of the `exec()`{.literal} system call (`0`{.literal}), which loads program code into new processes.

        ARGS
        :   The location of the started program with arguments.

        To see more details, examples, and options for `execsnoop`{.literal}, see `/usr/share/bcc/tools/doc/execsnoop_example.txt`{.literal} file. For more information about `exec()`{.literal}, see `exec(3)`{.literal} manual pages.

-   Use `opensnoop`{.literal} to track what files a command opens.

    a.  In one command line session, run the `opensnoop`{.literal} program to print the output for files opened only by the process of the `uname`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        # /usr/share/bcc/tools/opensnoop -n uname
        ```

    b.  In another command line session, enter the command to open certain files:

        ``` {.language-plaintext tabindex="-1"}
        $ uname
        ```

    c.  The command line session that runs `opensnoop`{.literal} shows the output similar to the following:

        ``` {.language-plaintext tabindex="-1"}
        PID    COMM  FD ERR PATH
        8596   uname    3  0   /etc/ld.so.cache
        8596   uname    3  0   /lib64/libc.so.6
        8596   uname    3  0   /usr/lib/locale/locale-archive
        ...
        ```

        The `opensnoop`{.literal} program watches the `open()`{.literal} system call across the whole system, and prints a line of output for each file that `uname`{.literal} tried to open along the way.

        The `opensnoop`{.literal} output displays the following fields:

        PID
        :   The process ID. (`8596`{.literal})

        COMM
        :   The process name. (`uname`{.literal})

        FD
        :   The file descriptor - a value that `open()`{.literal} returns to refer to the open file. (`3`{.literal})

        ERR
        :   Any errors.

        PATH
        :   The location of files that `open()`{.literal} tried to open.

        If a command tries to read a non-existent file, then the `FD`{.literal} column returns `-1`{.literal} and the `ERR`{.literal} column prints a value corresponding to the relevant error. As a result, `opensnoop`{.literal} can help you identify an application that does not behave properly.

        To see more details, examples, and options for `opensnoop`{.literal}, see `/usr/share/bcc/tools/doc/opensnoop_example.txt`{.literal} file. For more information about `open()`{.literal}, see `open(2)`{.literal} manual pages.

-   Use the `biotop`{.literal} to monitor the top processes performing I/O operations on the disk.

    a.  Run the `biotop`{.literal} program in one command line session with argument `30`{.literal} to produce a 30-second summary:

        ``` {.language-plaintext tabindex="-1"}
        # /usr/share/bcc/tools/biotop 30
        ```

        Note

        When no argument provided, the output screen by default refreshes every 1 second.

    b.  In another command line session, enter the command to read the content from the local hard disk device and write the output to the `/dev/zero`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # dd if=/dev/vda of=/dev/zero
        ```

        This step generates certain I/O traffic to illustrate `biotop`{.literal}.

    c.  The command line session that runs `biotop`{.literal} shows the output similar to the following:

        ``` {.language-plaintext tabindex="-1"}
        PID    COMM             D MAJ MIN DISK       I/O  Kbytes     AVGms
        9568   dd               R 252 0   vda      16294 14440636.0  3.69
        48     kswapd0          W 252 0   vda       1763 120696.0    1.65
        7571   gnome-shell      R 252 0   vda        834 83612.0     0.33
        1891   gnome-shell      R 252 0   vda       1379 19792.0     0.15
        7515   Xorg             R 252 0   vda        280  9940.0     0.28
        7579   llvmpipe-1       R 252 0   vda        228  6928.0     0.19
        9515   gnome-control-c  R 252 0   vda         62  6444.0     0.43
        8112   gnome-terminal-  R 252 0   vda         67  2572.0     1.54
        7807   gnome-software   R 252 0   vda         31  2336.0     0.73
        9578   awk              R 252 0   vda         17  2228.0     0.66
        7578   llvmpipe-0       R 252 0   vda        156  2204.0     0.07
        9581   pgrep            R 252 0   vda         58  1748.0     0.42
        7531   InputThread      R 252 0   vda         30  1200.0     0.48
        7504   gdbus            R 252 0   vda          3  1164.0     0.30
        1983   llvmpipe-1       R 252 0   vda         39   724.0     0.08
        1982   llvmpipe-0       R 252 0   vda         36   652.0     0.06
        ...
        ```

        The `biotop`{.literal} output displays the following fields:

        PID
        :   The process ID. (`9568`{.literal})

        COMM
        :   The process name. (`dd`{.literal})

        DISK
        :   The disk performing the read operations. (`vda`{.literal})

        I/O
        :   The number of read operations performed. (16294)

        Kbytes
        :   The amount of Kbytes reached by the read operations. (14,440,636)

        AVGms
        :   The average I/O time of read operations. (3.69)

        For more details, examples, and options for `biotop`{.literal}, see the `/usr/share/bcc/tools/doc/biotop_example.txt`{.literal} file. For more information about `dd`{.literal}, see `dd(1)`{.literal} manual pages.

-   Use `xfsslower`{.literal} to expose unexpectedly slow file system operations.

    The `xfsslower`{.literal} measures the time spent by XFS file system in performing read, write, open or sync (`fsync`{.literal}) operations. The `1`{.literal} argument ensures that the program shows only the operations that are slower than 1 ms.

    a.  Run the `xfsslower`{.literal} program in one command line session:

        ``` {.language-plaintext tabindex="-1"}
        # /usr/share/bcc/tools/xfsslower 1
        ```

        Note

        When no arguments provided, `xfsslower`{.literal} by default displays operations slower than 10 ms.

    b.  In another command line session, enter the command to create a text file in the `vim`{.literal} editor to start interaction with the XFS file system:

        ``` {.language-plaintext tabindex="-1"}
        $ vim text
        ```

    c.  The command line session that runs `xfsslower`{.literal} shows something similar upon saving the file from the previous step:

        ``` {.language-plaintext tabindex="-1"}
        TIME     COMM           PID    T BYTES   OFF_KB   LAT(ms) FILENAME
        13:07:14 b'bash'        4754   R 256     0           7.11 b'vim'
        13:07:14 b'vim'         4754   R 832     0           4.03 b'libgpm.so.2.1.0'
        13:07:14 b'vim'         4754   R 32      20          1.04 b'libgpm.so.2.1.0'
        13:07:14 b'vim'         4754   R 1982    0           2.30 b'vimrc'
        13:07:14 b'vim'         4754   R 1393    0           2.52 b'getscriptPlugin.vim'
        13:07:45 b'vim'         4754   S 0       0           6.71 b'text'
        13:07:45 b'pool'        2588   R 16      0           5.58 b'text'
        ...
        ```

        Each line represents an operation in the file system, which took more time than a certain threshold. `xfsslower`{.literal} detects possible file system problems, which can take form of unexpectedly slow operations.

        The `xfsslower`{.literal} output displays the following fields:

        COMM
        :   The process name. (`b’bash'`{.literal})

        T

        :   The operation type. (`R`{.literal})

            -   **R**ead
            -   **W**rite
            -   **S**ync

        OFF_KB
        :   The file offset in KB. (0)

        FILENAME
        :   The file that is read, written, or synced.

        To see more details, examples, and options for `xfsslower`{.literal}, see `/usr/share/bcc/tools/doc/xfsslower_example.txt`{.literal} file. For more information about `fsync`{.literal}, see `fsync(2)`{.literal} manual pages.

## [Legal Notice](#idm140443122904688) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
