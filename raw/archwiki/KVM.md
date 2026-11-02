---
{"title": "KVM", "url": "https://wiki.archlinux.org/title/KVM", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# KVM

Related articles

-   [Category:Hypervisors](../en/Category:Hypervisors.html "Category:Hypervisors")
-   [Libvirt](../en/Libvirt.html "Libvirt")

**KVM**, [Kernel-based Virtual Machine](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine "wikipedia:Kernel-based Virtual Machine"), is a [hypervisor](https://en.wikipedia.org/wiki/hypervisor "wikipedia:hypervisor") built into the Linux kernel. It is similar to [Xen](../en/Xen.html "Xen") in purpose but much simpler to get running. Unlike native [QEMU](../en/QEMU.html "QEMU"), which uses emulation, KVM is a special operating mode of QEMU that uses CPU extensions ([HVM](https://en.wikipedia.org/wiki/Hardware-assisted_virtualization "wikipedia:Hardware-assisted virtualization")) for virtualization via a kernel module.

Using KVM, one can run multiple virtual machines running unmodified GNU/Linux, Windows, or any other operating system. (See [Guest Support Status](https://www.linux-kvm.org/page/Guest_Support_Status) for more information.) Each virtual machine has private virtualized hardware: a network card, disk, graphics card, etc.

Differences between KVM and [Xen](../en/Xen.html "Xen"), [VMware](../en/VMware.html "VMware"), or QEMU can be found at the [KVM FAQ](https://www.linux-kvm.org/page/FAQ#General_KVM_information).

This article does not cover features common to multiple emulators using KVM as a backend. You should see related articles for such information.

## Checking support for KVM {#Checking_support_for_KVM}

### Hardware support {#Hardware_support}

KVM requires that the virtual machine host\'s processor has virtualization support (named VT-x for Intel processors and AMD-V for AMD processors). You can check whether your processor supports hardware virtualization with the following command:

    $ LC_ALL=C.UTF-8 lscpu | grep Virtualization

Alternatively:

    $ grep -E --color=auto 'vmx|svm|0xc0f' /proc/cpuinfo

If nothing is displayed after running either command, then your processor does **not** support hardware virtualization, and you will **not** be able to use KVM.

**Note** You may need to enable virtualization support in your BIOS. All x86_64 processors manufactured by AMD and Intel in the last 10 years support virtualization. If it looks like your processor does not support virtualization, it is almost certainly turned off in the BIOS.

### Kernel support {#Kernel_support}

Arch Linux kernels provide the required [kernel modules](../en/Kernel_modules.html "Kernel modules") to support KVM.

-   One can check if the necessary modules, `kvm` and either `kvm_amd` or `kvm_intel`, are available in the kernel with the following command:

&nbsp;

    $ zgrep CONFIG_KVM= /proc/config.gz

The module is available only if it is set to either `y` or `m`.

-   Then, ensure that the kernel modules are automatically loaded, with the command:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ lsmod | grep kvm
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
kvm_intel             245760  0
kvmgt                  28672  0
mdev                   20480  2 kvmgt,vfio_mdev
vfio                   32768  3 kvmgt,vfio_mdev,vfio_iommu_type1
kvm                   737280  2 kvmgt,kvm_intel
irqbypass              16384  1 kvm
```

If the command returns nothing, the module needs to be loaded manually; see [Kernel modules#Manual module handling](../en/Kernel_modules.html#Manual_module_handling "Kernel modules").

**Tip** If modprobing `kvm_intel` or `kvm_amd` fails but modprobing `kvm` succeeds, and `lscpu` claims that hardware acceleration is supported, check the BIOS settings. Some vendors, especially laptop vendors, disable these processor extensions by default. To determine whether there is no hardware support or whether the extensions are disabled in BIOS, the output from [dmesg](../en/Core_utilities.html#Essentials "Dmesg") after having failed to modprobe will tell.

## Para-virtualization with Virtio {#Para-virtualization_with_Virtio}

Para-virtualization provides a fast and efficient means of communication for guests to use devices on the host machine. KVM provides para-virtualized devices to virtual machines using the **Virtio** API as a layer between the hypervisor and guest.

All Virtio devices have two parts: the host device and the guest driver.

### Kernel support {#Kernel_support_2}

Use the following command **inside the virtual machine** to check if the VIRTIO modules are available in the kernel:

    $ zgrep VIRTIO /proc/config.gz

Then, check if the kernel modules are automatically loaded with the command:

    $ lsmod | grep virtio

In case the above commands return nothing, you need to [load the kernel modules](../en/Kernel_modules.html#Manual_module_handling "Kernel modules") manually.

### List of para-virtualized devices {#List_of_para-virtualized_devices}

-   network device (virtio-net)
-   block device (virtio-blk)
-   controller device (virtio-scsi)
-   serial device (virtio-serial)
-   balloon device (virtio-balloon)

## How to use KVM {#How_to_use_KVM}

See the main article: [QEMU](../en/QEMU.html "QEMU").

## Tips and tricks {#Tips_and_tricks}

**Note** See [QEMU#Tips and tricks](../en/QEMU.html#Tips_and_tricks "QEMU") and [QEMU/Troubleshooting](../en/QEMU/Troubleshooting.html "QEMU/Troubleshooting") for general tips and tricks.

### Nested virtualization {#Nested_virtualization}

Nested virtualization enables existing virtual machines to be run on third-party hypervisors and on other clouds without any modifications to the original virtual machines or their networking.

On host, enable nested feature for `kvm_intel`:

**Note** the same can be done for AMD, just replace `intel` with `amd` where necessary

    # modprobe -r kvm_intel
    # modprobe kvm_intel nested=1

To make it permanent (see [Kernel modules#Setting module options](../en/Kernel_modules.html#Setting_module_options "Kernel modules")):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/kvm_intel.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
options kvm_intel nested=1
```

Verify that feature is activated:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ cat /sys/module/kvm_intel/parameters/nested
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Y
```

Enable the \"host passthrough\" mode to forward all CPU features to the guest system:

1.  If using [QEMU](../en/QEMU.html "QEMU"), run the guest virtual machine with the following command: `qemu-system-x86_64 -enable-kvm -cpu host`.
2.  If using *virt-manager*, change the CPU model to `host-passthrough`.
3.  If using *virsh*, use `virsh edit `*`vm-name`* and change the CPU line to `<cpu mode='host-passthrough' check='partial'/>`

Boot the virtual machine and check if the `vmx` flag is present:

    $ grep -E --color=auto 'vmx|svm' /proc/cpuinfo

### Enabling huge pages {#Enabling_huge_pages}

**This article or section is a candidate for merging with [QEMU](../en/QEMU.html "QEMU").**

**Notes:** qemu-kvm no longer exists. After the above issue is cleared, I suggest merging this section into [QEMU](../en/QEMU.html "QEMU"). (Discuss in [Talk:KVM](../en/Talk:KVM.html))

You may also want to enable hugepages to improve the performance of your virtual machine. With an up to date Arch Linux and a running KVM, you probably already have everything you need. Check if you have the directory `/dev/hugepages`. If not, create it. Now we need the right permissions to use this directory. The default permission is root\'s uid and gid with 0755, but we want anyone in the kvm group to have access to hugepages.

Add to your `/etc/fstab`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/fstab
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
hugetlbfs       /dev/hugepages  hugetlbfs       mode=01770,gid=kvm        0 0
```

Instead of specifying the group name directly, with `gid=kvm`, you can of course specify the gid as a number, but it must match the `kvm` group. The mode of `1770` allows anyone in the group to create files but not unlink or rename each other\'s files. Make sure `/dev/hugepages` is mounted properly:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# umount /dev/hugepages
# mount /dev/hugepages
$ mount | grep huge
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime,mode=1770,gid=78)
```

Now you can calculate how many hugepages you need. Check how large your hugepages are:

    $ grep Hugepagesize /proc/meminfo

Normally that should be 2048 kB ≙ 2 MB. Let us say you want to run your virtual machine with 1024 MB. 1024 / 2 = 512. Add a few extra so we can round this up to 550. Now tell your machine how many hugepages you want:

    # sysctl -w vm.nr_hugepages=550

If you had enough free memory, you should see:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ grep HugePages_Total /proc/meminfo
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
HugesPages_Total:  550
```

If the number is smaller, close some applications or start your virtual machine with less memory (number_of_pages x 2):

    $ qemu-system-x86_64 -enable-kvm -m 1024 -mem-path /dev/hugepages -hda <disk_image> [...]

Note the `-mem-path` parameter. This will make use of the hugepages.

Now you can check, while your virtual machine is running, how many pages are used:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ grep HugePages /proc/meminfo
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
HugePages_Total:     550
HugePages_Free:       48
HugePages_Rsvd:        6
HugePages_Surp:        0
```

Now that everything seems to work, you can enable hugepages by default if you like. Add to your `/etc/sysctl.d/40-hugepage.conf`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/sysctl.d/40-hugepage.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
vm.nr_hugepages = 550
```

See also:

-   [Summary of hugetlbpage support in the Linux kernel](https://docs.kernel.org/admin-guide/mm/hugetlbpage.html)
-   [Debian Wiki - Hugepages](https://wiki.debian.org/Hugepages "debian:Hugepages")

### Secure Boot {#Secure_Boot}

**This article or section is a candidate for merging with [QEMU#Enabling Secure Boot](../en/QEMU.html#Enabling_Secure_Boot "QEMU").**

**Notes:** This is not KVM-specific and would be a great addition to what is already described there. (Discuss in [Talk:KVM](../en/Talk:KVM.html))

KVM Secure boot has a few requirements before it can be enabled:

1.  You must use a UEFI with secure boot support compiled in.
2.  The UEFI must have keys enrolled.

**Note** Arch Linux does not currently have a secure boot key unlike distributions like Fedora. If you intend to secure boot Arch Linux you must create your own signing key and sign your kernel after following the steps below. See [Unified Extensible Firmware Interface/Secure Boot](../en/Unified_Extensible_Firmware_Interface/Secure_Boot.html "Unified Extensible Firmware Interface/Secure Boot") for more information.

To enable UEFI with secure boot support, install [edk2-ovmf](https://archlinux.org/packages/?name=edk2-ovmf) and set your virtual machine to use the secure boot enabled UEFI. If you are using [libvirt](../en/Libvirt.html "Libvirt"), you can do this by adding the following to the XML configuration of your virtual machine.

    <os firmware="efi">
      <loader readonly="yes" secure="yes" type="pflash">/usr/share/edk2/x64/OVMF_CODE.secboot.4m.fd</loader>
    </os>

Next you need to enroll some keys. In this example we will enroll Microsoft and Redhat\'s secure boot keys. Install [virt-firmware](https://archlinux.org/packages/?name=virt-firmware) and run the following. Replace *`vm_name`* with the name of your virtual machine.

    $ virt-fw-vars --input /usr/share/edk2/x64/OVMF_VARS.4m.fd --output /var/lib/libvirt/qemu/nvram/vm_name_SECURE_VARS.fd --secure-boot --enroll-redhat

Then edit the libvirt XML configuration of your virtual machine to point to the new VARS file.

    <os firmware="efi">
      <loader readonly="yes" secure="yes" type="pflash">/usr/share/edk2/x64/OVMF_CODE.secboot.4m.fd</loader>
      <nvram template="/usr/share/edk2/x64/OVMF_VARS.4m.fd">/var/lib/libvirt/qemu/nvram/{vm-name}_SECURE_VARS.fd</nvram>
    </os>

After this secure boot should automatically be enabled. You can double check by entering the virtual machine\'s BIOS by pressing `F2` when you see the UEFI boot logo.

## See also {#See_also}

-   [KVM Howto](https://www.linux-kvm.org/page/HOWTO)
-   [KVM FAQ](https://www.linux-kvm.org/page/FAQ#General_KVM_information)
