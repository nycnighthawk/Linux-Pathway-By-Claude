---
{"title": "Interactively installing RHEL from installation media", "guide": "interactively_installing_rhel_from_installation_media", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/interactively_installing_rhel_from_installation_media/index", "retrieved": "2026-11-02", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Interactively installing RHEL from installation media {#interactively-installing-rhel-from-installation-media .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Installing RHEL on a local system using the graphical installer {#installing-rhel-on-a-local-system-using-the-graphical-installer .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140363049890944)

**Abstract**

You can install RHEL by using the graphical installer on one system at a time. Use this method to install RHEL on one or a few systems if you prefer the graphical interface. The installation source can be an installation media, an ISO file, or the Red Hat content delivery network (CDN).

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

## [Chapter 1. System requirements and supported architectures](#system-requirements-and-supported-architectures) {#chapter-1.-system-requirements-and-supported-architectures .title}

Red Hat Enterprise Linux 10 delivers a stable, secure, consistent foundation across hybrid cloud deployments. It includes the tools needed to deliver workloads faster with less effort. You can deploy RHEL as a guest on supported hypervisors, cloud provider environments, and physical infrastructure.

Applications can take advantage of innovations in leading hardware architecture platforms. Review the guidelines provided for system, hardware, security, memory, and storage configuration before installing.

If you want to use your system as a virtualization host, review the necessary hardware requirements for virtualization.

RHEL supports the following architectures:

-   AMD and Intel 64-bit architectures
-   The 64-bit ARM architecture
-   IBM Power Systems, Little Endian
-   64-bit IBM Z architectures

### [1.1. Supported installation targets](#supported-installation-targets) {#supported-installation-targets .title}

An installation target is a storage device that stores Red Hat Enterprise Linux and boots the system. Red Hat Enterprise Linux supports the following installation targets for IBM Z, IBM Power, AMD64, Intel 64, and 64-bit ARM systems.

-   Storage connected by a standard internal interface, such as DASD, SCSI, SATA, or SAS
-   BIOS/firmware RAID devices on the Intel64, AMD64 and arm64 architectures
-   Fibre Channel Host Bus Adapters and multipath devices. Some can require vendor-provided drivers.
-   Xen block devices on Intel processors in Xen virtual machines.
-   VirtIO block devices on Intel processors in KVM virtual machines.

Red Hat does not support installation to USB drives or SD memory cards.

**Additional resources**

-   [Red Hat Hardware Compatibility List](https://catalog.redhat.com/en/search?searchType=Hardware&certified_RedHat_Platforms=Red+Hat+Enterprise+Linux&certified_versions=Red+Hat+Enterprise+Linux+10)

### [1.2. Disk and memory requirements](#disk-and-memory-requirements) {#disk-and-memory-requirements .title}

When installing multiple operating systems, verify that the allocated disk space is separate from the disk space required by Red Hat Enterprise Linux.

In some cases, it is important to dedicate specific partitions to Red Hat Enterprise Linux. For example, for AMD64, Intel 64, and 64-bit ARM, at least two partitions (`/`{.literal} and `swap`{.literal}) must be dedicated to RHEL. Or, for IBM Power Systems servers, up to three partitions (`/`{.literal}, `swap`{.literal}, and potentially a `PReP`{.literal} boot partition) must be dedicated to RHEL.

Additionally, you must have a minimum of 10 GiB of available disk space. To install Red Hat Enterprise Linux, you must have a minimum of 10 GiB of space in either unpartitioned disk space or in partitions that can be deleted.

+-----------------------------------------+---------------------------------------------------------+
| Installation type                       | Minimum RAM                                             |
+:========================================+:========================================================+
| Local media installation (USB, DVD)     | -   1.5 GiB for aarch64, IBM Z and x86_64 architectures |
|                                         | -   3 GiB for ppc64le architecture                      |
+-----------------------------------------+---------------------------------------------------------+
| NFS network installation                | -   1.5 GiB for aarch64, IBM Z and x86_64 architectures |
|                                         | -   3 GiB for ppc64le architecture                      |
+-----------------------------------------+---------------------------------------------------------+
| HTTP, HTTPS or FTP network installation | -   3 GiB for IBM Z and x86_64 architectures            |
|                                         | -   4 GiB for aarch64 and ppc64le architectures         |
+-----------------------------------------+---------------------------------------------------------+

: Table 1.1. Minimum RAM requirements

Show more

It is possible to complete the installation with less memory than the minimum requirements. The exact requirements depend on your environment and installation path. Test various configurations to determine the minimum required RAM for your environment. Installing Red Hat Enterprise Linux using a Kickstart file has the same minimum RAM requirements as a standard installation. However, additional RAM may be required if your Kickstart file includes commands that require additional memory, or write data to the RAM disk.

**Additional resources**

-   [Automatically installing RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/index)

### [1.3. Graphics display resolution requirements](#graphics-display-resolution-requirements) {#graphics-display-resolution-requirements .title}

Your system must have the following minimum resolution to ensure a smooth and error-free installation of Red Hat Enterprise Linux.

+-----------------------------------+-----------------------------------+
| Product version                   | Resolution                        |
+:==================================+:==================================+
| Red Hat Enterprise Linux 10       | **Minimum**: 800 x 600            |
|                                   |                                   |
|                                   | **Recommended**: 1024 x 768       |
+-----------------------------------+-----------------------------------+

: Table 1.2. Display resolution

Show more

### [1.4. UEFI Secure Boot and Beta release requirements](#uefi-secure-boot-and-beta-release-requirements) {#uefi-secure-boot-and-beta-release-requirements .title}

If you plan to install a Beta release of Red Hat Enterprise Linux on a system with UEFI Secure Boot enabled, disable UEFI Secure Boot option first. Then begin the installation.

UEFI Secure Boot requires that the operating system kernel is signed with a recognized private key, which the system's firmware verifies using the corresponding public key.

For Red Hat Enterprise Linux Beta releases, the kernel is signed with a Red Hat Beta-specific public key, which the system fails to recognize by default. As a result, the system fails to even boot the installation media.

**Additional resources**

-   [IBM installation documentation](https://www.ibm.com/docs/en/linux-on-systems?topic=servers-quick-start-guides-installing-linux)
-   [Security hardening](https://docs.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/html-single/security_hardening/)
-   [Composing a customized RHEL system image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/index)
-   [Red Hat ecosystem catalog](https://catalog.redhat.com/en/search?searchType=Hardware&certified_RedHat_Platforms=Red+Hat+Enterprise+Linux&certified_versions=Red+Hat+Enterprise+Linux+10)
-   [RHEL technology capabilities and limits](https://access.redhat.com/articles/rhel-limits)
-   [Necessary hardware requirements for virtualization](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/index#preparing-an-amd64-or-intel64-system-to-host-virtual-machines)

## [Chapter 2. The value of registering your RHEL system to Red Hat](#the-value-of-registering-your-rhel-system-to-red-hat) {#chapter-2.-the-value-of-registering-your-rhel-system-to-red-hat .title}

Registration establishes an authorized connection between your system and Red Hat. Red Hat issues the registered system, a physical or virtual, a certificate that identifies and authenticates the system.

With the certificate, you can receive protected content, software updates, security patches, support, and managed services from Red Hat. With a valid subscription, you can register a Red Hat Enterprise Linux system in the following ways:

-   During the installation process, using an installer graphical user interface (GUI)
-   After installation, using the command line interface (CLI)
-   Automatically, during or after installation, using a kickstart script or an activation key

The specific steps to register your system depend on the version of RHEL that you are using and the registration method that you choose.

Registering your system to Red Hat enables features and capabilities that you can use to manage your system and report data. For example, a registered system is authorized to access protected content repositories for subscribed products through the Content Delivery Network (CDN) or a Red Hat Satellite Server.

These content repositories contain Red Hat software packages and updates, available only to customers with an active subscription. The packages and updates include security patches, bug fixes, and new features for RHEL and other Red Hat products.

## [Chapter 3. Customizing the installation media](#customizing-the-installation-media) {#chapter-3.-customizing-the-installation-media .title}

Customize RHEL installation media to create tailored system images with specific configurations, packages, and settings. Use this feature to deploy pre-configured systems that meet specific organizational requirements and reduce post-installation configuration time.

For details, see [Composing a customized RHEL system image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/index).

## [Chapter 4. Creating a bootable installation medium for RHEL](#creating-a-bootable-installation-medium-for-rhel) {#chapter-4.-creating-a-bootable-installation-medium-for-rhel .title}

You can download the ISO file from the Customer Portal to prepare the bootable physical installation medium, such as a USB or DVD. Starting with RHEL 8, Red Hat no longer provides separate variants for `Server`{.literal} and `Workstation`{.literal}.

**Red Hat Enterprise Linux for x86_64** includes both `Server`{.literal} and `Workstation`{.literal} capabilities. The distinction between `Server`{.literal} and `Workstation`{.literal} is managed through the System Purpose Role during the installation or configuration process. After downloading an ISO file from the Customer Portal, create a bootable physical installation medium, such as a USB or DVD to continue the installation process.

For secure environment cases where USB drives are prohibited, consider using the Image Builder to create and deploy reference images. This method ensures compliance with security policies while maintaining system integrity.

### [4.1. Installation boot media options](#choose-an-installation-boot-method) {#installation-boot-media-options .title}

There are several options available to boot the Red Hat Enterprise Linux installation program.

Full installation DVD or USB flash drive
:   Create a full installation DVD or USB flash drive by using the **DVD ISO** image. The DVD or USB flash drive can be used as a boot device and as an installation source for installing software packages.

Minimal installation DVD or USB flash drive
:   Create a minimal installation DVD or USB flash drive by using the **Boot ISO** image. This image contains only the minimum files necessary to boot the system and start the installation program. If you are not using the Content Delivery Network (CDN) to download the required software packages, the **Boot ISO** image requires an installation source that contains the required software packages.

### [4.2. Creating a bootable DVD](#creating-a-bootable-dvd) {#creating-a-bootable-dvd .title}

You can create a bootable installation DVD by using a burning software and a DVD burner. The exact steps to produce a DVD from an ISO image file vary and depend on the operating system and disc burning software installed.

Consult your system's burning software documentation for the exact steps to burn a DVD from an ISO image file.

Warning

You can create a bootable DVD by using either the DVD ISO image (full install) or the Boot ISO image (minimal install). However, the DVD ISO image is larger than 4.7 GB, and as a result, it might not fit on a single or dual-layer DVD. Check the size of the DVD ISO image file before you proceed. Use a USB flash drive when using the DVD ISO image to create bootable installation media.

**Additional resources**

-   [Image builder documentation for the environment cases where USB drives are prohibited](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_installing_and_managing_rhel_for_edge_images/index)

### [4.3. Creating a bootable USB device on Linux](#creating-a-bootable-usb-device-on-linux) {#creating-a-bootable-usb-device-on-linux .title}

Create a bootable USB device which you can then use to install Red Hat Enterprise Linux on other machines. This procedure overwrites the existing data on the USB drive without any warning. Back up any data or use an empty flash drive. A bootable USB drive cannot be used for storing data.

**Prerequisites**

-   You have downloaded the full installation DVD ISO or minimal installation Boot ISO image from the [Product Downloads](https://access.redhat.com/downloads/content/rhel) page.
-   You have a USB flash drive with enough capacity for the ISO image. The required size varies, but the minimum recommended USB size is 16 GB.

**Procedure**

1.  Connect the USB flash drive to the system.

2.  Log in as a root user:

    ``` {.language-plaintext tabindex="-1"}
    $ su -
    ```

    Enter your root password when prompted.

3.  Find the device node assigned to the drive in the log of recent events. Messages resulting from the attached USB flash drive are displayed at the bottom of the log. In this example, the drive name is `sdd`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # dmesg|tail
    ```

    ``` {.language-plaintext tabindex="-1"}
    [288954.686557] usb 2-1.8: New USB device strings: Mfr=0, Product=1, SerialNumber=2
    [288954.686559] usb 2-1.8: Product: USB Storage
    [288954.686562] usb 2-1.8: SerialNumber: 000000009225
    [288954.712590] usb-storage 2-1.8:1.0: USB Mass Storage device detected
    [288954.712687] scsi host6: usb-storage 2-1.8:1.0
    [288954.712809] usbcore: registered new interface driver usb-storage
    [288954.716682] usbcore: registered new interface driver uas
    [288955.717140] scsi 6:0:0:0: Direct-Access     Generic  STORAGE DEVICE   9228 PQ: 0 ANSI: 0
    [288955.717745] sd 6:0:0:0: Attached scsi generic sg4 type 0
    [288961.876382] sd 6:0:0:0: sdd Attached SCSI removable disk
    ```

4.  If the inserted USB device mounts automatically, unmount it before continuing with the next steps. For unmounting, use the `umount`{.literal} command. For more information, see [Unmounting a file system with umount](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/index#unmounting-a-file-system-with-umount).

5.  Write the ISO image directly to the USB device:

    ``` {.language-plaintext tabindex="-1"}
    # dd if=/image_directory/image.iso of=/dev/device
    ```

    -   Replace */image_directory/image.iso* with the full path to the ISO image file that you downloaded,

    -   Replace *device* with the device name that you retrieved with the `dmesg`{.literal} command.

        In this example, the full path to the ISO image is `/home/testuser/Downloads/rhel-10-x86_64-boot.iso`{.literal}, and the device name is `sdd`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # dd if=/home/testuser/Downloads/rhel-10-x86_64-boot.iso of=/dev/sdd
        ```

        Partition names are usually device names with a numerical suffix. For example, `sdd`{.literal} is a device name, and `sdd1`{.literal} is the name of a partition on the device `sdd`{.literal}.

6.  Wait for the `dd`{.literal} command to finish writing the image to the device. Run the `sync`{.literal} command to synchronize cached writes to the device. The data transfer is complete when the **\#** shell prompt appears. When you see the prompt, log out of the root account and unplug the USB drive. The USB drive is now ready to use as a boot device.

### [4.4. Creating a bootable USB device on Windows](#creating-a-bootable-usb-device-on-windows) {#creating-a-bootable-usb-device-on-windows .title}

You can create a bootable USB device on a Windows system with various tools. You can use [Fedora Media Writer](https://github.com/FedoraQt/MediaWriter/releases), which is a community product. Red Hat does not support this tool. You can report any issues with the tool at [Fedora Media Writer issues](https://github.com/FedoraQt/MediaWriter/issues).

Creating a bootable drive overwrites existing data on the USB drive without any warning. Back up any data or use an empty flash drive. A bootable USB drive cannot be used for storing data.

**Prerequisites**

-   You have downloaded the full installation DVD ISO or minimal installation Boot ISO image from the [Product Downloads](https://access.redhat.com/downloads/content/rhel) page.
-   You have a USB flash drive with enough capacity for the ISO image. The required size varies.

**Procedure**

1.  Download and install Fedora Media Writer from [https://github.com/FedoraQt/MediaWriter/releases](https://github.com/FedoraQt/MediaWriter/releases).
2.  Connect the USB flash drive to the system.
3.  Open Fedora Media Writer.
4.  From the main window, click Custom Image and select the previously downloaded Red Hat Enterprise Linux ISO image.
5.  From the **Write Custom Image** window, select the drive that you want to use.
6.  Click Write to disk. The boot media creation process starts. Do not unplug the drive until the operation completes. The operation may take several minutes, depending on the size of the ISO image, and the write speed of the USB drive.
7.  When the operation completes, unmount the USB drive. The USB drive is now ready to be used as a boot device.

### [4.5. Creating a bootable USB device on macOS](#creating-a-bootable-usb-device-on-macos) {#creating-a-bootable-usb-device-on-macos .title}

Create a bootable USB device that you can then use to install Red Hat Enterprise Linux on other machines. Creating a bootable USB drive overwrites any data previously stored on the USB drive without any warning. Back up any data or use an empty flash drive. A bootable USB drive cannot be used for storing data.

**Prerequisites**

-   You have downloaded the full installation DVD ISO or minimal installation Boot ISO image from the [Product Downloads](https://access.redhat.com/downloads/content/rhel) page.
-   You have a USB flash drive with enough capacity for the ISO image. The required size varies.

**Procedure**

1.  Connect the USB flash drive to the system.

2.  Identify the device path with the `diskutil list`{.literal} command. The device path has the format of *`/dev/disknumber`{.literal}*, where `number`{.literal} is the number of the disk. The disks are numbered starting at zero (0). Typically, `disk0`{.literal} is the OS X recovery disk, and `disk1`{.literal} is the main OS X installation. In the following example, the USB device is `disk2`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ diskutil list
    ```

    ``` {.language-plaintext tabindex="-1"}
    /dev/disk0
    #:                       TYPE NAME                    SIZE       IDENTIFIER
    0:      GUID_partition_scheme                        *500.3 GB   disk0
    1:                        EFI EFI                     209.7 MB   disk0s1
    2:          Apple_CoreStorage                         400.0 GB   disk0s2
    3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3
    4:          Apple_CoreStorage                         98.8 GB    disk0s4
    5:                 Apple_Boot Recovery HD             650.0 MB   disk0s5
    /dev/disk1
    #:                       TYPE NAME                    SIZE       IDENTIFIER
    0:                  Apple_HFS YosemiteHD             *399.6 GB   disk1
    Logical Volume on disk0s1
    8A142795-8036-48DF-9FC5-84506DFBB7B2
    Unlocked Encrypted
    /dev/disk2
    #:                       TYPE NAME                    SIZE       IDENTIFIER
    0:     FDisk_partition_scheme                        *8.1 GB     disk2
    1:               Windows_NTFS SanDisk USB             8.1 GB     disk2s1
    ```

3.  Identify your USB flash drive by comparing the NAME, TYPE and SIZE columns to your flash drive. For example, the NAME should be the title of the flash drive icon in the **Finder** tool. You can also compare these values to those in the information panel of the flash drive.

4.  Unmount the flash drive's file system volumes:

    ``` {.language-plaintext tabindex="-1"}
    $ diskutil unmountDisk /dev/disknumber
    ```

    ``` {.language-plaintext tabindex="-1"}
    Unmount of all volumes on disknumber was successful
    ```

    When the command completes, the icon for the flash drive disappears from your desktop. If the icon does not disappear, you may have selected the wrong disk. Attempting to unmount the system disk accidentally returns a **failed to unmount** error.

5.  Write the ISO image to the flash drive. macOS provides both a block (`/dev/disk*`{.literal}) and character device (`/dev/rdisk*`{.literal}) file for each storage device. Writing an image to the `/dev/rdisknumber`{.literal} character device is faster than writing to the `/dev/disknumber`{.literal} block device. For example, to write the *`/Users/user_name/Downloads/rhel-{ProductNumber}-x86_64-boot.iso`{.literal}* file to the *`/dev/rdisk2`{.literal}* device, enter the following command:

    ``` {.language-plaintext tabindex="-1"}
    # sudo dd if=/Users/user_name/Downloads/rhel-{ProductNumber}-x86_64-boot.iso of=/dev/rdisk2 bs=512K status=progress
    ```

    -   `if=`{.literal} - Path to the installation image.
    -   `of=`{.literal} - The raw disk device *(/dev/rdisknumber)* representing the target disk.
    -   `bs=512K`{.literal} - Sets the block size to 512 KB for faster data transfer.
    -   `status=progress`{.literal} - Displays a progress indicator during the operation.

6.  Wait for the `dd`{.literal} command to finish writing the image to the device. The data transfer is complete when the **\#** prompt appears. When the prompt is displayed, log out of the root account and unplug the USB drive. The USB drive is now ready to be used as a boot device.

**Additional resources**

-   [ISO for RHEL 8/9 Server or Workstation](https://access.redhat.com/solutions/4203571)
-   [Customer Portal](https://access.redhat.com/downloads/content/rhel)
-   [Image builder documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_installing_and_managing_rhel_for_edge_images/index)

## [Chapter 5. Installing RHEL as a virtual machine](#creating-a-kernel-based-virtual-machine-and-booting-the-installation-iso-in-the-vm) {#chapter-5.-installing-rhel-as-a-virtual-machine .title}

To install RHEL as a guest operating system on an existing RHEL host, you can use an installation ISO to create a virtual machine (KVM) and start the RHEL installation.

**Prerequisites**

-   Virtualization is enabled on your host system. For instructions, see [Preparing RHEL to host virtual machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/preparing-rhel-to-host-virtual-machines).

-   You have a sufficient amount of system resources to allocate to your VMs, such as disk space, RAM, or CPUs. The recommended values might vary significantly depending on the intended tasks and workload of the VMs.

-   An operating system (OS) installation source is available locally or on a network. This can be one of the following formats:

    -   An ISO image of an installation medium
    -   A disk image of an existing VM installation. Such a disk image can also be created from a `bootc`{.literal} container. For instructions, see [Creating QEMU disk images by using bootc-image-builder](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/creating-bootc-compatible-base-disk-images-by-using-bootc-image-builder#creating-qcow2-images-by-using-bootc-image-builder).

-   To create a VM that uses the `system`{.literal} connection of `libvirt`{.literal}, you must have root privileges or be in the `libvirt`{.literal} user group on the host. For more information, see [User-space connection types for virtualization](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/basic-concepts-of-virtualization-in-rhel#user-space-connection-types-for-virtualization).

-   On IBM Z systems, the KVM host must run RHEL installed in LPAR mode. For details, see [Installing in an LPAR](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/index#installing-in-an-lpar).

**Procedure**

-   Create virtual machine with the instance of Red Hat Enterprise Linux as a KVM guest operating system, use the following `virt-install`{.literal} command on the KVM host:

    ``` {.language-plaintext tabindex="-1"}
    $ virt-install --name=<guest_name> --disk size=<disksize_in_GB> --memory=<memory_size_in_MB> --cdrom <filepath_to_iso> --graphics vnc
    ```

    For more examples, see [Creating virtual machines by using the command line](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/creating-virtual-machines#creating-virtual-machines-by-using-the-command-line-interface).

    1.  The graphical console of the VM opens and you can start the installation.

**Troubleshooting**

-   If the VM is successfully created but the graphical console does not open, connect to the VM manually. For instructions, see [Connecting to virtual machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/connecting-to-virtual-machines).

**Next steps**

-   [Customizing the system in the installer](#customizing-the-system-in-the-installer "Chapter 10. Customizing the system in the installer")

**Additional resources**

-   [Creating virtual machines by using the command line](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/creating-virtual-machines#creating-virtual-machines-by-using-the-command-line-interface)
-   [Deploying a RHEL container image by using KVM with a QEMU disk image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/deploying-the-rhel-bootc-images#deploying-a-container-image-by-using-kvm-with-a-qcow2-disk-image)

## [Chapter 6. Booting the installation media](#booting-the-installation-media-) {#chapter-6.-booting-the-installation-media .title}

You can boot the Red Hat Enterprise Linux installation by using USB or DVD media and begin the installation process. You can register RHEL by using the Red Hat Content Delivery Network (CDN).

The CDN is a geographically distributed series of web servers. These servers provide, for example, packages and updates to RHEL hosts with a valid subscription. During the installation, registering and installing RHEL from the CDN offers the following benefits:

-   Use the latest packages for an up-to-date system immediately after installation and
-   Integrated support for connecting to Red Hat Lightspeed and enabling System Purpose.

Important

In RHEL 10, the Defense Information Systems Agency (DISA) Security Technical Implementation Guide (STIG) and other security profiles do not automatically enable Federal Information Processing Standards (FIPS) mode at first boot. To remain FIPS compliant, you must manually enable 1FIPS mode before the installation. You can either do it by adding the `fips=1`{.literal} kernel boot option or by using a Kickstart configuration that explicitly enables FIPS. If FIPS is not enabled before the beginning of the installation, systems built with these security profiles might not be compliant and users might unknowingly deploy non-compliant systems. To avoid compliance issues, ensure that FIPS is enabled during the boot phase, before launching the graphical or text-based installer. For more information, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/switching-rhel-to-fips-mode).

**Prerequisites**

-   You have created bootable installation media (USB or DVD).

**Procedure**

1.  Power off the system to which you are installing Red Hat Enterprise Linux.

2.  Disconnect any drives from the system.

3.  Power on the system.

4.  Insert the bootable installation media (USB or DVD).

5.  Power off the system but do not remove the boot media.

6.  Power on the system.

    You might need to press a specific key or combination of keys to boot from the media. You can also configure the Basic Input/Output System (BIOS) of your system to boot from the media. For more information, see the documentation that came with your system.

    The **Red Hat Enterprise Linux boot** window opens and displays information about a variety of available boot options.

7.  Use the arrow keys on your keyboard to select the boot option that you require, and press Enter to select the boot option. The **Welcome to Red Hat Enterprise Linux** window opens and you can install Red Hat Enterprise Linux by using the graphical user interface.

    The installation program automatically begins if no action is performed in the boot window within 60 seconds.

8.  Optional: Press e to enter the edit mode and change the predefined command line to add or remove boot options.

9.  Press Ctrl+X to confirm your choice.

**Additional resources**

-   [Customizing the system in the installer](#customizing-the-system-in-the-installer "Chapter 10. Customizing the system in the installer")
-   [Boot options reference](#boot-options-reference "Chapter 18. Boot options reference")

## [Chapter 7. Optional: Customizing boot options](#optional-customizing-boot-options) {#chapter-7.-optional-customizing-boot-options .title}

When you are installing RHEL on `x86_64`{.literal} or `ARM64`{.literal} architectures, you can edit the boot options to customize the installation process based on your specific environment.

### [7.1. Boot options](#types-of-boot-options) {#boot-options .title}

You can append multiple options separated by space to the boot command line. Boot options specific to the installation program always start with `inst`{.literal}. The following are the available boot options.

Options with an equals \"=\" sign
:   You must specify a value for boot options that use the `=`{.literal} symbol. For example, the `inst.lang=`{.literal} option must contain a value, in this example, a language code. The correct syntax for this example is `inst.lang=en_US`{.literal}.

Options without an equals \"=\" sign
:   This boot option does not accept any values or parameters. For example, the `rd.live.check`{.literal} option forces the installation program to verify the installation media before starting the installation. If this boot option is present, the installation program performs the verification and if the boot option is not present, the verification is skipped.

You can customize boot options for a particular menu entry by pressing the `e`{.literal} key and adding custom boot options to the command line. When ready, press `Ctrl+X`{.literal} to boot the modified option.

**Additional resources**

-   [Editing the GRUB2 menu](#editing-the-grub2-menu-for-the-uefi-based-systems "7.2. Editing the GRUB2 menu")
-   [Boot options reference](#boot-options-reference "Chapter 18. Boot options reference")

### [7.2. Editing the GRUB2 menu](#editing-the-grub2-menu-for-the-uefi-based-systems) {#editing-the-grub2-menu .title}

You can edit the GRUB2 boot menu during RHEL installation to customize boot parameters and kernel options. It enables configuration of specific settings such as FIPS mode, network parameters, and other system requirements before the installation begins.

**Prerequisites**

-   You have created bootable installation media (USB or DVD) or have configured a server providing PXE or UEFI HTTP boot-related services.
-   You have booted the installation from the media or from the network, and the installation boot menu is open.

**Procedure**

1.  From the boot menu window, select the required option and press e.

2.  Move the cursor to the end of the kernel command line and add the parameters as required. For example, to enable the cryptographic module self-checks mandated by the Federal Information Processing Standard (FIPS) 140, add `fips=1`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    linuxefi /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64 rd.live.\
    check quiet fips=1
    ```

3.  When you finish editing, press Ctrl+X to start the installation using the specified options.

## [Chapter 8. Updating drivers during installation](#updating-drivers-during-installation) {#chapter-8.-updating-drivers-during-installation .title}

You can update drivers during the Red Hat Enterprise Linux installation process. Updating drivers is completely optional. Do not perform a driver update unless it is necessary.

Ensure you have been notified by Red Hat, your hardware vendor, or a trusted third-party vendor that a driver update is required during Red Hat Enterprise Linux installation.

### [8.1. Overview](#overview) {#overview .title}

Red Hat Enterprise Linux supports drivers for many hardware devices but some newly-released drivers may not be supported. A driver update should only be performed if an unsupported driver prevents the installation from completing.

Updating drivers during installation is typically only required to support a particular configuration. For example, installing drivers for a storage adapter card that provides access to your system's storage devices.

Warning

Driver update disks may disable conflicting kernel drivers. In rare cases, unloading a kernel module may cause installation errors.

### [8.2. Types of driver update](#types-of-driver-update) {#types-of-driver-update .title}

Red Hat, your hardware vendor, or a trusted third party provides the driver update as an ISO image file. Once you receive the ISO image file, choose the type of driver update.

Types of driver update

:   -   **Automatic**: In this driver update method; a storage device (including a CD, DVD, or USB flash drive) labeled `OEMDRV`{.literal} is physically connected to the system. If the `OEMDRV`{.literal} storage device is present when the installation starts, it is treated as a driver update disk, and the installation program automatically loads its drivers.
    -   **Assisted**: The installation program prompts you to locate a driver update. You can use any local storage device with a label other than `OEMDRV`{.literal}. The `inst.dd`{.literal} boot option is specified when starting the installation. If you use this option without parameters, the installation program displays all storage devices connected to the system. It then prompts you to select a device that contains a driver update.
    -   **Manual**: Manually specify a path to a driver update image or an RPM package. You can use any local storage device with a label other than `OEMDRV`{.literal}, or a network location accessible from the installation system. The `inst.dd=location`{.literal} boot option is specified when starting the installation, where *location* is the path to a driver update disk or ISO image. When you specify this option, the installation program attempts to load any driver updates found at the specified location. With manual driver updates, you can specify local storage devices or a network location (HTTP, HTTPS or FTP server). You can use both `inst.dd=location`{.literal} and `inst.dd`{.literal} simultaneously, where *location* is the path to a driver update disk or ISO image. In this scenario, the installation program attempts to load any available driver updates from the location and also prompts you to select a device that contains the driver update.

Limitations
:   On UEFI systems with the Secure Boot technology enabled, all drivers must be signed with a valid certificate. Red Hat drivers are signed by one of Red Hat's private keys and authenticated by its corresponding public key in the kernel. If you load additional, separate drivers, verify that they are signed.

### [8.3. Preparing a driver update CD or DVD](#preparing-a-driver-update) {#preparing-a-driver-update-cd-or-dvd .title}

You can prepare a driver update on a CD or DVD to perform a driver update during installation.

**Prerequisites**

-   You have received the driver update ISO image from Red Hat, your hardware vendor, or a trusted third-party vendor.
-   You have burned the driver update ISO image to a CD or DVD.

Warning

If only a single ISO image file ending in `.iso`{.literal} is available on the CD or DVD, the burn process has not been successful. See your system's burning software documentation for instructions on how to burn ISO images to a CD or DVD.

**Procedure**

1.  Insert the driver update CD or DVD into your system's CD/DVD drive, and browse it by using the system's file manager tool.
2.  Verify that a single file `rhdd3`{.literal} is available. `rhdd3`{.literal} is a signature file that contains the driver description and a directory named `rpms`{.literal}. It contains the RPM packages with the actual drivers for various architectures.

### [8.4. Preparing a driver update USB drive](#preparing-a-driver-update-usb-drive) {#preparing-a-driver-update-usb-drive .title}

You can prepare a driver update on a USB flash drive to perform a driver update during installation.

**Prerequisites**

-   You have received the driver update ISO image from Red Hat, your hardware vendor, or a trusted third-party vendor.
-   You have prepared a USB flash drive with a file system compatible with RHEL to place the driver update ISO on.

**Procedure**

1.  Connect the USB drive to your computer and determine what device it was assigned by the system. To determine the assigned device, you can inspect the output of `dmesg`{.literal} or `lsblk -o +MOUNTPOINT`{.literal} command.

2.  Determine if the drive has been mounted and what the mount point is (based on the output of `lsblk`{.literal} command). If it's not mounted, mount it manually:

    a.  Optional: Create a mount point directory:

        ``` {.language-plaintext tabindex="-1"}
        mkdir /path/to/mountpoint
        ```

    b.  Mount the USB device's partition in the mount point directory. The following example assumes that the device's partition that will be used for storing the driver update ISO file is `/dev/sdb1`{.literal} and the mount point is `/mnt/usbdrive`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        sudo mount /dev/sdb1 /mnt/usbdrive
        ```

3.  Copy the driver update ISO file on the USB drive.

    The following example assumes that the mount point is `/mnt/usbdrive`{.literal} and the ISO file's location is `/home/user/driverdisk.iso`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    sudo cp /home/user/driverdisk.iso /mnt/usbdrive
    ```

4.  Unmount the USB device by using the `umount`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    sudo umount /mnt/usbdrive
    ```

### [8.5. Performing an automatic driver update](#performing-an-automatic-driver-update) {#performing-an-automatic-driver-update .title}

You can perform an automatic driver update during installation.

**Prerequisites**

-   You have placed the driver update image on a standard disk partition with an OEMDRV label. Alternatively, you have written the OEMDRV image to a CD, DVD, or USB drive.
-   Before starting the installation process, you have connected a block device with an OEMDRV volume label containing the driver update disk. Alternatively, you have inserted the prepared CD, DVD, or USB drive into the system.

**Procedure**

-   When you complete the prerequisite steps, the drivers load automatically when the installation program starts and installs during the system's installation process.

### [8.6. Performing an assisted driver update](#performing-an-assisted-driver-update) {#performing-an-assisted-driver-update .title}

You can perform an assisted driver update during installation to install necessary drivers for new or existing hardware.

**Prerequisites**

-   You have connected a block device without an `OEMDRV`{.literal} volume label to your system and copied the driver disk image to this device. Or
-   You have prepared a driver update CD or DVD and inserted it into your system's CD or DVD drive. Or
-   You have prepared a USB device with the driver disk and connected it to your computer before starting the installation process.

Note

If you burn an ISO image to a CD or DVD, or write it to a USB drive, the image might not have the OEMDRV volume label. In this case, use the `inst.dd`{.literal} option without arguments. The installation program provides an option to scan and select drivers from the CD, DVD or USB drive. In this scenario, the installation program does not prompt you to select a driver update ISO image. Another scenario is to use the CD, DVD or USB drive with the `inst.dd=`{.literal}*`location`{.literal}* boot option. This allows the installation program to automatically scan the CD, DVD or USB drive for driver updates. For more information, see [Performing a driver update](#updating-drivers-during-installation "Chapter 8. Updating drivers during installation")

**Procedure**

1.  From the boot menu window, press the **E** key on your keyboard to display the boot command line.

2.  Append the `inst.dd`{.literal} boot option to the command line beginning with `linux`{.literal} or `linuxefi`{.literal} and press **Ctrl+X** to start the boot process.

3.  From the menu, select a local disk partition or a CD, DVD, or USB device. The installation program scans for ISO files, or driver update RPM packages.

4.  Optional: Select the driver update ISO file.

    This step is not required if the selected device or partition contains driver update RPM packages rather than an ISO image file. For example, an optical drive containing a driver update CD, DVD or a USB drive that the ISO file has been written on.

5.  Select the required drivers.

    a.  Use the number keys on your keyboard followed by **Enter** key to toggle the driver selection.
    b.  Press **c** followed by **Enter** to install the selected driver. The selected driver is loaded and after pressing **c** and **Enter** again to exit the driver disk device selection, the installation process starts.

### [8.7. Performing a manual driver update](#performing-a-manual-driver-update) {#performing-a-manual-driver-update .title}

You can perform a manual driver update during installation to install necessary drivers for new or existing hardware.

**Prerequisites**

-   You have placed the driver update ISO image file on a USB flash drive or a web server and connected it to your computer.

**Procedure**

1.  From the boot menu window, press the **E** key on your keyboard to display the boot command line.
2.  Append the `inst.dd=`{.literal}*`location`{.literal}* boot option to the command line, where location is a path to the driver update. Typically, the image file is located on a web server, for example, http://server.example.com/dd.iso, or on a USB flash drive, for example, `/dev/sdb1`{.literal}. It is also possible to specify an RPM package containing the driver update, for example http://server.example.com/dd.rpm.
3.  Press **Ctrl+X** to start the boot process. The drivers available at the specified location are automatically loaded and the installation begins.

**Additional resources**

-   [The `inst.dd`{.literal} boot option](https://github.com/rhinstaller/anaconda/blob/rhel-8.0/docs/boot-options.rst/#instdd)

### [8.8. Disabling a driver](#disabling-a-driver) {#disabling-a-driver .title}

You can disable a malfunctioning driver during the installation process.

**Prerequisites**

-   You have booted into the installation media's bootloader (GRUB) menu.

**Procedure**

1.  From the boot menu, press the **E** key on your keyboard to display the boot command line.

2.  Append the `modprobe.blacklist=`{.literal}*`driver_name`{.literal}* boot option to the command line.

    Replace *driver_name* with the name of the driver or drivers you want to disable, for example:

    ``` {.language-plaintext tabindex="-1"}
    modprobe.blacklist=ahci
    ```

    Drivers disabled by using the `modprobe.blacklist=`{.literal} boot option remain disabled on the installed system and appear in the `/etc/modprobe.d/anaconda-blacklist.conf`{.literal} file.

3.  Press **Enter** to start the boot process.

## [Chapter 9. Consoles and logging during installation](#consoles-and-logging-during-installation) {#chapter-9.-consoles-and-logging-during-installation .title}

The Red Hat Enterprise Linux installer uses the **tmux** terminal multiplexer to manage multiple windows alongside the main interface. Each window serves a distinct purpose and displays logs that help troubleshoot issues during the installation process.

One window provides an interactive shell with `root`{.literal} privileges, unless disabled by using a boot option or a Kickstart command. The terminal multiplexer is running in virtual console 1. To switch from the actual installation environment to **tmux**, press Ctrl+Alt+F1. To go back to the main installation interface which runs in virtual console 6, press Ctrl+Alt+F6. During text mode, installation starts in virtual console 1 (**tmux**), and switching to console 6 opens a shell prompt instead of a graphical interface.

The console running **tmux** has five available windows. Their contents are described in the following table, along with keyboard shortcuts. Note that the keyboard shortcuts are two-part: first press Ctrl+b, then release both keys, and press the number key for the window you want to use.

You can also use Ctrl+b n, Alt+ Tab, and Ctrl+b p to switch to the next or previous **tmux** window, respectively.

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Shortcut                          | Contents                                                                                                                                                                   |
+:==================================+:===========================================================================================================================================================================+
| Ctrl+b 1                          | Main installation program window. Contains text-based prompts (used for text mode and also for interactive entry of RDP credentials), and also some debugging information. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ctrl+b 2                          | Interactive shell with `root`{.literal} privileges.                                                                                                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ctrl+b 3                          | Installation log; displays messages stored in `/tmp/anaconda.log`{.literal}.                                                                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ctrl+b 4                          | Storage log; displays messages related to storage devices and configuration, stored in `/tmp/storage.log`{.literal}.                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ctrl+b 5                          | Program log; displays messages from utilities run during the installation process, stored in `/tmp/program.log`{.literal}.                                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ctrl+b 6                          | Packaging log; displays messages related to packages, stored in `/tmp/packaging.log`{.literal}.                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.1. Available tmux windows

Show more

## [Chapter 10. Customizing the system in the installer](#customizing-the-system-in-the-installer) {#chapter-10.-customizing-the-system-in-the-installer .title}

During the customization phase of the installation, you must perform certain configuration tasks to enable the installation of Red Hat Enterprise Linux. These tasks include:

-   Configuring the storage and assigning mount points.
-   Selecting a base environment with software to be installed.
-   Setting a password for the root user or creating a local user.

Optionally, you can further customize the system, for example, by configuring system settings and connecting the host to a network.

### [10.1. Setting the installer language](#setting-the-installer-language) {#setting-the-installer-language .title}

You can select the language and regional settings for the RHEL installation program interface to ensure proper localization during the installation process. It affects the installer interface language and regional formatting conventions.

**Prerequisites**

-   You have created installation media.
-   You have specified an installation source if you are using the Boot ISO image file.
-   You have booted from the media to the bootloader menu.

**Procedure**

1.  After you select the **Red hat Enterprise Linux** option from the boot menu, the installation program starts and **Welcome to Red Hat Enterprise Screen** appears.

2.  From the left-hand pane of the **Welcome to Red Hat Enterprise Linux** window, select a language. Alternatively, search the preferred language by using the text box.

    Note

    A language is pre-selected by default. The pre-selected language is determined by the automatic location detection feature of the **GeoIP** module. If you use the `inst.lang=`{.literal} option on the boot command line, then the language that you define with the boot option is selected.

3.  From the right-hand pane of the **Welcome to Red Hat Enterprise Linux** window, select a location specific to your region.

4.  Click Continue to proceed to the graphical installation window.

5.  If you are installing a pre-release version of Red Hat Enterprise Linux, a warning message is displayed about the pre-release status of the installation media.

    a.  To continue with the installation, click I want to proceed, or
    b.  To quit the installation and reboot the system, click I want to exit.

### [10.2. Configuring the storage devices](#configuring-the-storage-devices) {#configuring-the-storage-devices .title}

You can install Red Hat Enterprise Linux on a large variety of storage devices. You can configure basic, locally accessible, storage devices in the **Installation Destination** window.

Basic storage devices directly connected to the local system, such as disks and solid-state drives, are displayed in the **Local Standard Disks** section. On 64-bit IBM Z systems, this section contains activated Direct Access Storage Devices (DASDs).

#### [10.2.1. Configuring installation destination](#configuring-installation-destination) {#configuring-installation-destination .title}

You can select and configure storage devices for RHEL installation the **Installation Destination** window, including disk selection, partitioning options, and encryption settings. It determines where the operating system is installed and how storage is managed on the target system.

**Prerequisites**

-   The **Installation Summary** window is open.
-   Back up your data if you plan to use a disk that already contains data. Manipulating partitions always carries a risk. For example, if the process is interrupted or fails for any reason data on the disk can be lost.

**Procedure**

1.  From the **Installation Summary** window, click **Installation Destination**. Perform the following operations in the **Installation Destination** window that opens:

    a.  From the **Local Standard Disks** section, select the storage device that you require; a white check mark indicates your selection. Disks without a white check mark are not used during the installation process; they are ignored if you choose automatic partitioning, and they are not available in manual partitioning.

        The **Local Standard Disks** shows all locally available storage devices. For example, SATA, NVMe™ and SCSI disks, USB flash and external disks. Storage devices connected post starting the installation program are not detected, unless you follow the step 2. If you use a removable drive to install RHEL, your system is unusable if you remove the device.

    b.  Optional: Click the **Refresh** link in the lower right-hand side of the window if you want to configure additional local storage devices connected after the installation program has started. The **Rescan Disks** dialog box opens.

        i.  Click Rescan Disks and wait until the scanning process completes.

            All storage changes that you make during the installation are lost when you click **Rescan Disks**.

        ii. Click OK to return to the **Installation Destination** window. All detected disks including any new ones are displayed under the **Local Standard Disks** section.

2.  Optional: Click Add a disk...​ to add a specialized storage device.

    The **Storage Device Selection** window opens and lists all storage devices that the installation program has access to.

3.  Optional: Under **Storage Configuration**, select the **Automatic** radio button for automatic partitioning.

    You can also configure custom partitioning. For more details, see [Configuring manual partitioning](#configuring-manual-partitioning "10.5. Configuring manual partitioning").

4.  Optional: Select **Free up space by removing or shrinking existing partitions** to reclaim space from an existing partitioning layout. For example, if any disk already has a different operating system and you want to make this system's partitions smaller to allow more room for Red Hat Enterprise Linux.

5.  Optional: Select **Encrypt my data** to encrypt all partitions except the ones needed to boot the system (such as `/boot`{.literal}) by using *Linux Unified Key Setup* (LUKS). Encrypting your disk adds an extra layer of security.

    a.  Click Done. The **Disk Encryption Passphrase** dialog box opens.

        i.  Type the passphrase in the **Passphrase** and **Confirm** fields.

        ii. Click Save Passphrase to complete disk encryption.

            Warning

            If you lose the LUKS passphrase, any encrypted partitions and their data is completely inaccessible. There is no way to recover a lost passphrase. However, if you perform a Kickstart installation, you can save encryption passphrases and create backup encryption passphrases during the installation.

6.  Optional: Click the **Full disk summary and bootloader** link in the lower left-hand side of the window to select which storage device contains the boot loader. For more information, see [Configuring boot loader](#configuring-boot-loader "10.2.3. Configuring boot loader").

    In most cases it is sufficient to leave the boot loader in the default location. Some configurations, for example, systems that require chain loading from another boot loader require the boot drive to be specified manually.

7.  Click Done.

8.  Optional: The **Reclaim Disk Space** dialog box appears if you selected **automatic partitioning** and the **Free up space by removing or shrinking existing partitions** option. It also appears when there is not enough free space on the selected disks to install Red Hat Enterprise Linux. It lists all configured disk devices and all partitions on those devices. The dialog box displays information about the minimal disk space the system needs for an installation with the currently selected package set and how much space you have reclaimed. To start the reclaiming process:

    a.  Review the displayed list of available storage devices. The **Reclaimable Space** column shows how much space can be reclaimed from each entry.

    b.  Select a disk or partition to reclaim space.

    c.  Use the Shrink button to use free space on a partition while preserving the existing data.

    d.  Use the Delete button to delete that partition or all partitions on a selected disk including existing data.

    e.  Use the Delete all button to delete all existing partitions on all disks including existing data and make this space available to install Red Hat Enterprise Linux.

    f.  Click Reclaim space to apply the changes and return to graphical installations.

        No disk changes are made until you click Begin Installation on the **Installation Summary** window. The **Reclaim Space** dialog only marks partitions for resizing or deletion; no action is performed.

**Additional resources**

-   [How to use dm-crypt on IBM Z, LinuxONE and with the PAES cipher](https://www.ibm.com/docs/en/linux-on-systems?topic=volumes-creating-volume-pervasive-encryption)

#### [10.2.2. Special cases for installation destination configuration](#special-cases-for-installation-destination-configuration) {#special-cases-for-installation-destination-configuration .title}

Following are some special cases to consider when you are configuring installation destinations:

-   Some BIOS types do not support booting from a RAID card. In these instances, the `/boot`{.literal} partition must be created on a partition outside of the RAID array, such as on a separate disk. It is necessary to use an internal disk for partition creation with problematic RAID cards. A `/boot`{.literal} partition is also necessary for software RAID setups. If you choose to partition your system automatically, you should manually edit your `/boot`{.literal} partition.
-   To configure the Red Hat Enterprise Linux boot loader to chain load from another boot loader, specify the boot drive manually. Click the Full disk summary and bootloader link in the **Installation Destination** window.
-   When you install Red Hat Enterprise Linux on a system with multipath and non-multipath storage devices, the automatic partitioning layout can create volume groups containing both device types. This defeats the purpose of multipath storage. Select either multipath or non-multipath devices on the **Installation Destination** window. Alternatively, proceed to manual partitioning.

#### [10.2.3. Configuring boot loader](#configuring-boot-loader) {#configuring-boot-loader .title}

RHEL uses GRand Unified Bootloader version 2 (**GRUB2**) as the boot loader for AMD64 and Intel 64, IBM Power Systems, and ARM. For 64-bit IBM Z, the **zipl** boot loader is used.

The boot loader is the first program that runs when the system starts and is responsible for loading and handing over control to an operating system. **GRUB2** can boot any compatible operating system (including Microsoft Windows) and can also use chain loading to hand over control to other boot loaders for unsupported operating systems.

Warning

Installing **GRUB2** may overwrite your existing boot loader.

If an operating system is already installed, the Red Hat Enterprise Linux installation program attempts to automatically detect and configure the boot loader to start the other operating system. If the boot loader is not detected, you can manually configure any additional operating systems after you finish the installation.

If you are installing Red Hat Enterprise Linux with more than one disk, you might want to manually specify the disk where you want to install the boot loader.

**Procedure**

1.  From the **Installation Destination** window, click the **Full disk summary and bootloader** link. The **Selected Disks** dialog box opens.

    The boot loader is installed on the device of your choice, or, on a UEFI system. The **EFI system partition** is created on the target device and used to store the boot loader files.

2.  To change the boot device, select a device from the list and click Set as Boot Device. You can set only one device as the boot device.

3.  To disable a new boot loader installation, select the device currently marked for boot and click Do not install boot loader. This ensures **GRUB2** is not installed on any device.

    Warning

    If you choose not to install a boot loader, you cannot boot the system directly and you must use another boot method, such as a standalone commercial boot loader application. Use this option only if you have another way to boot your system.

    The boot loader may require a special partition, depending on whether your system uses BIOS or UEFI firmware. It can also depend on whether the boot drive uses a *GUID Partition Table* (GPT) or a *Master Boot Record* (MBR, also known as msdos) label. If you use automatic partitioning, the installation program creates the partition.

#### [10.2.4. Storage device selection](#storage-device-selection) {#storage-device-selection .title}

The storage device selection window lists all storage devices that the installation program can access. Depending on your system and available hardware, some tabs might not be displayed. The devices are grouped under the following tabs:

Multipath Devices
:   Storage devices accessible through more than one path, such as through multiple SCSI controllers or Fiber Channel ports on the same system. The installation program only detects multipath storage devices with serial numbers that are 16 or 32 characters long.

Other SAN Devices
:   Devices available on a Storage Area Network (SAN).

Firmware RAID
:   Storage devices attached to a firmware RAID controller.

IBM Z Devices
:   Storage devices, or Logical Units (LUNs), DASD, attached through the zSeries Linux FCP (Fiber Channel Protocol) driver.

#### [10.2.5. Filtering storage devices](#filtering-storage-devices) {#filtering-storage-devices .title}

You can filter and select specific storage devices during RHEL installation by using WWID, port, target, or LUN identifiers. It helps identify and configure specialized storage devices for installation, ensuring proper device selection in complex storage environments.

**Prerequisites**

-   The **Installation Summary** window is open.

**Procedure**

1.  From the **Installation Summary** window, click **Installation Destination**. The **Installation Destination** window opens, listing all available drives.

2.  Under the **Specialized & Network Disks** section, click Add a disk. The storage devices selection window opens.

3.  Click the **Search by** tab to search by port, target, LUN, or WWID.

    Searching by WWID or LUN requires additional values in the corresponding input text fields.

4.  Select the option that you require from the **Search** drop-down menu.

5.  Click Find to start the search. Each device is presented on a separate row with a corresponding checkbox.

6.  Select the checkbox to enable the device that you require during the installation process.

    Later in the installation process, you can choose to install Red Hat Enterprise Linux on any selected device. You can also automatically mount other selected devices as part of the installed system. The installation process does not automatically erase selected devices. Selecting a device does not put stored data at risk.

    Note

    You can add devices to the system after installation by modifying the `/etc/fstab`{.literal} file.

7.  Click Done to return to the **Installation Destination** window.

    Any storage devices that you do not select are hidden from the installation program entirely. To chain load the boot loader from a different boot loader, select all the devices present.

### [10.3. Advanced storage options](#advanced-storage-options) {#advanced-storage-options .title}

To use an advanced storage device, configure an iSCSI (SCSI over TCP/IP) target or FCoE (Fibre Channel over Ethernet) SAN (Storage Area Network).

To use iSCSI storage devices for the installation, the installation program must discover them as iSCSI targets and create an iSCSI session to access them. Each of these steps might require a user name and password for Challenge Handshake Authentication Protocol (CHAP) authentication. Additionally, configure an iSCSI target to authenticate the iSCSI initiator on the system which hosts the target (reverse CHAP), both for discovery and for the session. Used together, CHAP and reverse CHAP are called mutual CHAP or two-way CHAP. Mutual CHAP provides the greatest level of security for iSCSI connections, particularly if the user name and password are different for CHAP authentication and reverse CHAP authentication.

Repeat the iSCSI discovery and iSCSI login steps to add all required iSCSI storage. You cannot change the name of the iSCSI initiator after you attempt discovery for the first time. To change the iSCSI initiator name, you must restart the installation.

#### [10.3.1. iSCSI target configuration](#iscsi-target-configuration) {#iscsi-target-configuration .title}

With iSCSI, you can use remote network-based storage devices as installation targets during Red Hat Enterprise Linux installation. Using iSCSI storage, you can centralize storage management and provide flexible storage configurations for systems installed across a network.

The installation program supports automatic and manual discovery of iSCSI targets.

iSCSI Boot Firmware Table (iBFT)
:   The installer checks whether the system firmware or add-on boot ROMs support iBFT, which is a firmware extension for systems that boot from iSCSI. If iBFT support is available, the installer reads the configured iSCSI target information for the boot disk, logs in to the target automatically, and makes it available during installation. To enable automatic connection to an iSCSI target, activate a network device using the `ip=ibft`{.literal} boot option.

Manual iSCSI target discovery
:   You can also manually discover and start iSCSI sessions in the graphical user interface (GUI). Manual discovery enables the installer to identify available iSCSI targets and use them as installation destinations.

**Additional resources**

-   [Network boot options](#network-boot-options "18.2. Network boot options")

#### [10.3.2. Discovering and starting an iSCSI session](#discovering-and-starting-an-iscsi-session) {#discovering-and-starting-an-iscsi-session .title}

You can discover and start an iSCSI session during Red Hat Enterprise Linux installation to identify available iSCSI targets and connect to network-based storage devices from the graphical user interface (GUI).

**Prerequisites**

-   The **Installation Summary** window is open.

**Procedure**

1.  From the **Installation Summary** window, click **Installation Destination**. The **Installation Destination** window opens, listing all available drives.

2.  Under the **Specialized & Network Disks** section, click Add a disk. The storage devices selection window opens.

3.  Click Add iSCSI target. The **Add iSCSI Storage Target** window opens.

    Important

    You cannot place the `/boot`{.literal} partition on iSCSI targets that you have manually added by using this method. An iSCSI target containing a `/boot`{.literal} partition must be configured for use with iBFT. However, in instances where the installed system is expected to boot from iSCSI with iBFT configuration provided by a method other than firmware iBFT. For example, by using iPXE, you can remove the `/boot`{.literal} partition restriction by using the `inst.nonibftiscsiboot`{.literal} installer boot option.

    a.  Enter the IP address of the iSCSI target in the **Target IP Address** field.

    b.  Type a name in the **iSCSI Initiator Name** field for the iSCSI initiator in iSCSI qualified name (IQN) format. A valid IQN entry contains the following information:

        -   The string `iqn.`{.literal} (note the period).

        -   A date code specifies the year and month when your organization's Internet domain or subdomain was registered. Use four digits for the year, a dash, and two digits for the month, followed by a period. For example, represent September 2010 as `2010-09`{.literal}.

        -   Your organization's Internet domain or subdomain name, presented in reverse order with the top-level domain first. For example, represent the subdomain `storage.example.com`{.literal} as `com.example.storage`{.literal}.

        -   A colon followed by a string that uniquely identifies this particular iSCSI initiator within your domain or subdomain. For example `:diskarrays-sn-a8675309`{.literal}.

            A complete IQN is `iqn.2010-09.storage.example.com:diskarrays-sn-a8675309`{.literal}. The installation program pre-populates the `iSCSI Initiator Name`{.literal} field with a name in this format to help you with the structure. For more information about IQNs, see *3.2.6. iSCSI Names* in *RFC 3720 - Internet Small Computer Systems Interface (iSCSI)* and *1. iSCSI Names and Addresses* in *RFC 3721 - Internet Small Computer Systems Interface (iSCSI) Naming and Discovery*. Both documents are available from `tools.ietf.org`{.literal}.

    c.  Select the `Discovery Authentication Type`{.literal} drop-down menu to specify the type of authentication to use for iSCSI discovery. The following options are available:

        -   No credentials
        -   CHAP pair
        -   CHAP pair and a reverse pair

    d.  Do one of the following:

        i.  If you selected the `CHAP pair`{.literal} as the authentication type, enter the user name and password for the iSCSI target in the `CHAP Username`{.literal} and `CHAP Password`{.literal} fields.
        ii. If you selected CHAP pair and a reverse pair as the authentication type, enter the iSCSI target credentials in the `CHAP Username`{.literal} and `CHAP Password`{.literal} fields. Enter the iSCSI initiator credentials in the `Reverse CHAP Username`{.literal} and `Reverse CHAP Password`{.literal} fields.

    e.  Optional: Select the `Bind targets to network interfaces`{.literal} checkbox.

    f.  Click Start Discovery.

        The installation program attempts to discover an iSCSI target based on the information provided. If discovery succeeds, the `Add iSCSI Storage Target`{.literal} window displays a list of all iSCSI nodes discovered on the target.

4.  Select the checkboxes for the nodes that you want to use for installation.

    The `Node login authentication type`{.literal} menu contains the same options as the `Discovery Authentication Type`{.literal} menu. However, if you need credentials for discovery authentication, use the same credentials to log in to a discovered node.

5.  Click the additional `Use the credentials from discovery`{.literal} drop-down menu. When you provide the proper credentials, the Log In button becomes available.

6.  Click Log In to initiate an iSCSI session.

    While the installer uses `iscsiadm`{.literal} to find and log into iSCSI targets, `iscsiadm`{.literal} automatically stores any information about these targets in the `iscsiadm`{.literal} iSCSI database. The installer copies this database to the installed system. It also marks any iSCSI targets that are not used for root partition. This allows the system to automatically log in to them when it starts. If the root partition is placed on an iSCSI target, `initrd`{.literal} logs into this target. The installer does not include this target in start up scripts to avoid multiple attempts to log into the same target.

#### [10.3.3. Configuring FCoE parameters](#configuring-fcoe-parameters) {#configuring-fcoe-parameters .title}

You can discover the FCoE (Fibre Channel over Ethernet) devices from the **Installation Destination** window by configuring the FCoE parameters accordingly.

**Prerequisites**

-   The **Installation Summary** window is open.

**Procedure**

1.  From the **Installation Summary** window, click **Installation Destination**. The **Installation Destination** window opens, listing all available drives.

2.  Under the **Specialized & Network Disks** section, click Add a disk. The storage devices selection window opens.

3.  Click Add FCoE SAN. A dialog box opens for you to configure network interfaces for discovering FCoE storage devices.

4.  Select a network interface that is connected to an FCoE switch in the `NIC`{.literal} drop-down menu.

5.  Click Add FCoE disk(s) to scan the network for SAN devices.

6.  Select the required boxes:

    -   **Use DCB:***Data Center Bridging* (DCB) is a set of enhancements to the Ethernet protocols designed to increase the efficiency of Ethernet connections in storage networks and clusters. Select the checkbox to enable or disable the installation program's awareness of DCB. Enable this option only for network interfaces that require a host-based DCBX client. For configurations on interfaces that use a hardware DCBX client, disable the checkbox.
    -   **Use auto vlan:***Auto VLAN* is enabled by default and indicates whether VLAN discovery should be performed. If this option is enabled, then the FIP (FCoE Initiation Protocol) VLAN discovery protocol runs on the Ethernet interface when the link configuration has been validated. If they are not already configured, network interfaces for any discovered FCoE VLANs are automatically created and FCoE instances are created on the VLAN interfaces.

7.  Discovered FCoE devices are displayed under the `Other SAN Devices`{.literal} tab in the **Installation Destination** window.

#### [10.3.4. Configuring DASD storage devices](#configuring-dasd-storage-devices) {#configuring-dasd-storage-devices .title}

You can discover and configure the DASD storage devices from the **Installation Destination** window.

**Prerequisites**

-   The **Installation Summary** window is open.

**Procedure**

1.  From the **Installation Summary** window, click **Installation Destination**. The **Installation Destination** window opens, listing all available drives.

2.  Under the **Specialized & Network Disks** section, click Add a disk. The storage devices selection window opens.

3.  Click Add DASD ECKD. The **Add DASD Storage Target** dialog box opens and prompts to specify a device number, such as **0.0.0204**. You can also attach additional DASDs that were not detected when the installation started.

4.  Type the device number of the DASD that you want to attach in the **Device number** field.

5.  Click Start Discovery.

    If a DASD with the specified device number is found and not already attached, the dialog box closes and the newly-discovered drives appear in the list of drives. You can then select the checkboxes for the required devices and click Done. The new DASDs are available for selection, marked as `DASD device 0.0.`{.literal}*`xxxx`{.literal}* in the **Local Standard Disks** section of the **Installation Destination** window.

    If you entered an invalid device number, or if the specified DASD is already attached to the system, an error message appears in the dialog box. The message explains the error and prompts you to try again with a different device number.

#### [10.3.5. Configuring FCP devices](#configuring-fcp-devices) {#configuring-fcp-devices .title}

FCP devices enable 64-bit IBM Z to use SCSI devices rather than, or in addition to, Direct Access Storage Device (DASD) devices. FCP devices provide a switched fabric topology that enables 64-bit IBM Z systems to use SCSI LUNs as disk devices in addition to traditional DASD devices.

**Prerequisites**

-   The **Installation Summary** window is open.
-   For an FCP-only installation, you have removed the `DASD=`{.literal} option from the CMS configuration file or the `rd.dasd=`{.literal} option from the parameter file to indicate that no DASD is present.

**Procedure**

1.  From the **Installation Summary** window, click **Installation Destination**. The **Installation Destination** window opens, listing all available drives.

2.  Under the **Specialized & Network Disks** section, click Add a disk. The storage devices selection window opens.

3.  Click Add ZFCP LUN. The **Add zFCP Storage Target** dialog box opens allowing you to add a FCP (Fibre Channel Protocol) storage device.

    64-bit IBM Z requires that you enter any FCP device manually so that the installation program can activate FCP LUNs. You can enter FCP devices either in the graphical installation, or as a unique parameter entry in the parameter or CMS configuration file. The values that you enter must be unique to each site that you configure.

4.  Type the 4 digit hexadecimal device number in the **Device number** field.

5.  Provide following details when the `zFCP`{.literal} device is not configured in NPIV mode or `auto LUN`{.literal} scanning is disabled by the `zfcp.allow_lun_scan=0`{.literal} kernel module parameter:

    a.  Type the 16 digit hexadecimal World Wide Port Number (WWPN) in the **WWPN** field.
    b.  Type the 16 digit hexadecimal FCP LUN identifier in the **LUN** field.

6.  Click Start Discovery to connect to the FCP device.

    The newly-added devices are displayed in the **IBM Z** tab of the **Installation Destination** window.

    Use only lower-case letters in hex values. If you enter an incorrect value and click Start Discovery, the installation program displays a warning. You can edit the configuration information and retry the discovery attempt. For more information about these values, consult the hardware documentation and check with your system administrator.

#### [10.3.6. Configuring NVMe over fabrics devices](#configuring-nvme-over-fabrics-devices) {#configuring-nvme-over-fabrics-devices .title}

Configure the Non-volatile Memory Express™ (NVMe™) over fabrics by using the graphical installation to use it as an installation target. Additionally, if the device meets the requirements for booting, you can also set the device as a boot device.

**Prerequisites**

-   A NVMe™ over fabrics device is present on the system.
-   The initial installation process has been completed and the **Installation Summary** window is open.

**Procedure**

1.  From the **Installation Summary** window, click **Installation Destination**.

    The **Installation Destination** window opens, listing all available devices. This includes local (PCI Express transport) NVMe™ devices.

2.  Under the **Specialized & Network Disks** section, click **Add a disk...​**.

    The storage devices selection window opens.

3.  Click the **NVMe™ Fabrics Devices** tab.

4.  Optional: If the device list is too long, use the **Filter by** option to view specific devices.

5.  Select the devices from the list by using checkboxes.

6.  Click **Done** to return to the **Installation Destination** window.

    The NVMe™ device that you reconfigured is displayed in the **Specialized & Network Disks** section.

7.  Click **Done** to return to the Installation Summary window.

**Additional resources**

-   [Configuring NVMe™ over fabrics using NVMe™](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_storage_devices/index#configuring-an-nvme-rdma-controller-using-configfs)

### [10.4. Configuring the root account and creating users](#configuring-the-root-user-and-creating-local-accounts) {#configuring-the-root-account-and-creating-users .title}

You can configure the root account and create users to access the system from the **Installation Summary** screen.

#### [10.4.1. Configuring a root account](#configuring-a-root-password) {#configuring-a-root-account .title}

You can configure a `root`{.literal} account during the installation process to log in as an administrator.

The root user can perform many system administration tasks, including the following:

-   Installing and updating software packages
-   Changing system-wide configuration such as network and firewall settings, storage options
-   Adding or modifying users, groups and file permissions.

To gain root privileges for the installed systems, you can either use a `root`{.literal} account or create a user account with administrative privileges (member of the `wheel`{.literal} group). The `root`{.literal} account is always created during the installation. Switch to the administrator account only when you need administrator access for tasks.

Warning

The `root`{.literal} account has complete control over the system. If unauthorized personnel gain access to the account, they can access or delete users\' personal files.

**Procedure**

1.  From the **Installation Summary** window, select **User Settings \> Root Account**. The **Root Account** window opens.

    By default, the **Disable root account** option is selected.

2.  To enable root account, select the **Enable root account** option.

3.  Type your password in the **Root Password** field.

    The root password is case-sensitive and must be at least **eight** characters long containing **numbers**, **letters** (upper and lower case) and **symbols**.

4.  Type the same password in the **Confirm** field.

5.  Optional: Select the `Allow root SSH login with password`{.literal} option to enable SSH access (with password) to this system as the root user. By default the password-based SSH root access is disabled.

6.  Click Done to confirm your root password and return to the **Installation Summary** window.

    If you proceed with a weak password, you must click Done twice.

#### [10.4.2. Creating a user account](#creating-a-user-account) {#creating-a-user-account .title}

Create a user account during RHEL installation to establish a non-root user for daily system operations from the **Installation Summary** window. It improves security by avoiding the use of the root account for regular tasks and provides proper user management from the start of system deployment.

Note

You should only use the root account to perform privileged tasks. Using the root account instead of a non-privileged user account to perform regular tasks can introduce a security risk.

**Procedure**

1.  On the **Installation Summary** window, select **User Settings \> User Creation**. The **Create User** window opens.

2.  Type the user account name into the **Full name** field, for example: John Smith.

3.  Type the username into the **User name** field, for example: jsmith.

    The **User name** is used to log in from a command line; if you install a graphical environment, then your graphical login manager uses the **Full name**.

4.  The **Add administrative privileges to this...​** option is selected by default. Deselect this option if you do not want to share administrative privileges to this account. By default, new users have administrative privileges to the system.

    An administrator user can use the `sudo`{.literal} command to perform tasks that are only available to `root`{.literal} by using the user password, instead of the `root`{.literal} password. Though it is more convenient, it can also introduce a security risk.

5.  The **Require a password to use this account** option is selected by default. Disable it if you want to use this account without a password.

    If you give administrator privileges to a user, ensure the account is password protected. Never give a user administrator privileges without assigning a password to the account.

6.  Type a password into the **Password** field.

7.  Type the same password into the **Confirm password** field.

8.  Click Done to apply the changes and return to the **Installation Summary** window.

#### [10.4.3. Editing advanced user settings](#editing-advanced-user-settings) {#editing-advanced-user-settings .title}

You can configure advanced user account settings during RHEL installation to customize home directories, user and group IDs, and group memberships. This provides fine-grained control over user account configuration and system security policies.

**Procedure**

1.  On the **Create User** window, click Advanced.

2.  Edit the details in the **Home directory** field, if required. The field is populated by default with `/home/`{.literal}*`username`{.literal}* .

3.  In the **User and Groups IDs** section you can:

    a.  Select the **Specify a user ID manually** checkbox and use + or - to enter the required value.

        The default value is 1000. User IDs (UIDs) 0-999 are reserved by the system so they cannot be assigned to a user.

    b.  Select the **Specify a group ID manually** checkbox and use + or - to enter the required value.

        The default group name is the same as the user name, and the default Group ID (GID) is 1000. GIDs 0-999 are reserved by the system so they cannot be assigned to a user group.

4.  Specify additional groups as a comma-separated list in the **Group Membership** field. Groups that do not already exist are created; you can specify custom GIDs for additional groups in parentheses. If you do not specify a custom GID for a new group, the new group receives a GID automatically.

    The user account created always has one default group membership (the user's default group with an ID set in the **Specify a group ID manually** field).

5.  Click Save Changes to apply the updates and return to the **Create User** window.

### [10.5. Configuring manual partitioning](#configuring-manual-partitioning) {#configuring-manual-partitioning .title}

You can use manual partitioning to configure your disk partitions and mount points and define the file system that Red Hat Enterprise Linux is installed on. Before installation, you should consider whether you want to use partitioned or unpartitioned disk devices.

You have different partitioning and storage options available, including `Standard Partitions`{.literal}, `LVM`{.literal}, and `LVM thin provisioning`{.literal}. These options provide various benefits and configurations for managing your system's storage effectively.

Standard partition
:   A standard partition contains a file system or swap space. Standard partitions are most commonly used for `/boot`{.literal} and the `BIOS Boot`{.literal} and `EFI System partitions`{.literal}. You can use the LVM logical volumes in most other uses.

LVM
:   Choosing `LVM`{.literal} (or Logical Volume Management) as the device type creates an LVM logical volume. LVM improves performance when using physical disks. You can configure advanced setups such as using multiple physical disks for one mount point and configuring software RAID for increased performance, reliability, or both.

LVM thin provisioning
:   Thin provisioning manages a storage pool of free space, known as a thin pool. The system can allocate this to an arbitrary number of devices when needed by applications. You can dynamically expand the pool when needed for cost-effective allocation of storage space.

An installation of Red Hat Enterprise Linux requires a minimum of one partition but uses at least the following partitions or volumes: `/`{.literal}, `/home`{.literal}, `/boot`{.literal}, and `swap`{.literal}. You can also create additional partitions and volumes as you require.

To prevent data loss it is recommended that you backup your data before proceeding. If you are upgrading or creating a dual-boot system, you should back up any data you want to keep on your storage devices.

#### [10.5.1. Recommended partitioning scheme](#recommended-partitioning-scheme) {#recommended-partitioning-scheme .title}

Create separate file systems at the following mount points. However, if required, you can also create the file systems at `/usr`{.literal}, `/var`{.literal}, and `/tmp`{.literal} mount points.

-   `/boot`{.literal}
-   `/`{.literal} (root)
-   `/home`{.literal}
-   `swap`{.literal}
-   `/boot/efi`{.literal}
-   `PReP`{.literal}

This partition scheme is recommended for bare metal deployments and it does not apply to virtual and cloud deployments.

`/boot`{.literal} partition - recommended size at least 2 GiB

:   The partition mounted on `/boot`{.literal} contains the operating system kernel that allows system to boot Red Hat Enterprise Linux 10, along with files used during the bootstrap process. Due to the limitations of most firmwares, create a small partition to hold these. In most scenarios, a 2 GiB boot partition is adequate. However, in some cases 2 GiB might not be sufficient. Systems that require additional hardware firmware generate larger `initramfs`{.literal} images because the firmware blobs are included. If the `/boot`{.literal} partition is too small, insufficient disk space can cause future kernel updates to fail. Consider allocating more than 2 GiB in environments with additional hardware drivers or firmware requirements. Unlike other mount points, using an LVM volume for `/boot`{.literal} is not possible. `/boot`{.literal} must be located on a separate disk partition.

    If you have a RAID card, be aware that some BIOS types do not support booting from the RAID card. In such a case, the `/boot`{.literal} partition must be created on a partition outside of the RAID array, such as on a separate disk.

Warning

-   Normally, the `/boot`{.literal} partition is created automatically by the installation program. Create a separate `/boot`{.literal} partition smaller than 2 TiB if the `/`{.literal} (root) partition is larger than 2 TiB and the system uses (U)EFI booting. This configuration is required for successful booting.
-   Ensure the `/boot`{.literal} partition is located within the first 2 TB of the disk while manual partitioning. Placing the `/boot`{.literal} partition beyond the 2 TB boundary might result in a successful installation, but the system fails to boot because BIOS cannot read the `/boot`{.literal} partition beyond this limit.

`root`{.literal} - recommended size of at least 10 GiB

:   This is where \"`/`{.literal}\", or the root directory, is located. The root directory is the top-level of the directory structure. By default, all files are written to this file system unless a different file system is mounted in the path being written to. For example, `/boot`{.literal} or `/home`{.literal}.

    While a 5 GiB root file system allows you to install a minimal installation, allocate at least 10 GiB. This allows you to install as many package groups as you want.

Do not confuse the `/`{.literal} directory with the `/root`{.literal} directory. The `/root`{.literal} directory is the home directory of the root user. The `/root`{.literal} directory is sometimes referred to as *slash root* to distinguish it from the root directory.

`/home`{.literal} - recommended size at least 1 GiB
:   To store user data separately from system data, create a dedicated file system for the `/home`{.literal} directory. Base the file system size on the amount of data that is stored locally, number of users, and so on. You can upgrade or reinstall Red Hat Enterprise Linux 10 without erasing user data files. If you select automatic partitioning, have at least 55 GiB of disk space available for the installation, to ensure that the `/home`{.literal} file system is created.

`swap`{.literal} partition - recommended size at least 1 GiB

:   Swap file systems support virtual memory; data is written to a swap file system when there is not enough RAM to store the data your system is processing. Swap size is a function of system memory workload, not total system memory and therefore is not equal to the total system memory size. It is important to analyze what applications a system will be running and the load those applications will serve to determine the system memory workload. Application providers and developers can provide guidance.

    When the system runs out of swap space, the kernel stops processes as the system RAM memory is exhausted. Configuring too much swap space results in storage devices being allocated but idle and is a poor use of resources. Too much swap space can also hide memory leaks. The maximum size for a swap partition and other additional information can be found in the `mkswap(8)`{.literal} manual page.

    The following table provides the recommended size of a swap partition depending on the amount of RAM in your system and if you want sufficient memory for your system to hibernate. If you let the installation program partition your system automatically, the swap partition size is established by using these guidelines. Automatic partitioning configuration assumes hibernation is not in use. The maximum size of the swap partition is limited to 10 percent of the total size of the disk. The installation program cannot create swap partitions more than 1TiB. To configure enough swap space for hibernation, you might need to increase the swap partition size beyond the default limits. In this case, you must edit the partitioning layout manually.

+-----------------------------+--------------------------------------+----------------------------------------------------+
| Amount of RAM in the system | Recommended swap space               | Recommended swap space if allowing for hibernation |
+:============================+:=====================================+:===================================================+
| Less than 2 GiB             | 2 times the amount of RAM            | 3 times the amount of RAM                          |
+-----------------------------+--------------------------------------+----------------------------------------------------+
| 2 GiB - 8 GiB               | Equal to the amount of RAM           | 2 times the amount of RAM                          |
+-----------------------------+--------------------------------------+----------------------------------------------------+
| 8 GiB - 64 GiB              | 4 GiB to 0.5 times the amount of RAM | 1.5 times the amount of RAM                        |
+-----------------------------+--------------------------------------+----------------------------------------------------+
| More than 64 GiB            | Workload dependent (at least 4GiB)   | Hibernation not recommended                        |
+-----------------------------+--------------------------------------+----------------------------------------------------+

: Table 10.1. Recommended system swap space

Show more

At the border between each range, such as systems with 2 GiB, 8 GiB, or 64 GiB of RAM, you can choose the swap space size. You can also decide whether to support hibernation. If your system resources allow for it, increasing the swap space can lead to better performance.

Distributing swap space over multiple storage devices - particularly on systems with fast drives, controllers and interfaces - also improves swap space performance.

Many systems have more partitions and volumes than the minimum required. Choose partitions based on your particular system needs. If you are unsure about configuring partitions, accept the automatic default partition layout provided by the installation program.

`/boot/efi`{.literal} partition - recommended size of 600 MiB
:   UEFI-based AMD64, Intel 64, and 64-bit ARM require an EFI system partition. The recommended minimum size is 500 MiB. When using automatic partitioning, the installer creates a 600 MiB `/boot/efi`{.literal} partition. When manually partitioning the disk, you can specify a different partition size. BIOS systems do not require an EFI system partition.

`PReP`{.literal} boot partition - recommended size of 4 to 8 MiB
:   When installing Red Hat Enterprise Linux on IBM Power System servers, the first partition of the disk should include a `PReP`{.literal} boot partition. This contains the GRUB2 boot loader, which allows other IBM Power Systems servers to boot Red Hat Enterprise Linux.

`BIOS`{.literal} boot partition - recommended size of 1 MiB
:   When installing Red Hat Enterprise Linux on a BIOS system with a GPT-partitioned disk, a separate partition is required to boot from the particular disk. This partition is called `BIOS`{.literal} boot and is used to store the boot loader.

Note

Allocate storage capacity only to the partitions that are required immediately. Additional free space can be assigned at any time to address future requirements.

#### [10.5.2. Supported hardware storage](#supported-hardware-storage) {#supported-hardware-storage .title}

It is important to understand how storage technologies are configured and how support for them may have changed between major versions of Red Hat Enterprise Linux.

Hardware RAID
:   Any RAID functions provided by the mainboard of your computer, or attached controller cards, need to be configured before you begin the installation process. Each active RAID array appears as one drive within Red Hat Enterprise Linux.

Software RAID

:   On systems with more than one disk, you can use the Red Hat Enterprise Linux installation program to operate several of the drives as a Linux software RAID array. With a software RAID array, RAID functions are controlled by the operating system rather than the dedicated hardware.

    Note

    When all member devices of a pre-existing RAID array are unpartitioned disks, the installation program treats the array as a single disk. It does not provide a method to remove the array.

USB Disks
:   You can connect and configure external USB storage after installation. Most devices are recognized by the kernel, but some devices may not be recognized. If it is not a requirement to configure these disks during installation, disconnect them to avoid potential problems.

Considerations for Intel BIOS RAID Sets
:   Red Hat Enterprise Linux uses `mdraid`{.literal} for installing on Intel BIOS RAID sets. These sets are automatically detected during the boot process and their device node paths can change across several booting processes. Replace device node paths (such as `/dev/sda`{.literal}) with file system labels or device UUIDs. You can find the file system labels and device UUIDs by using the `blkid`{.literal} command.

#### [10.5.3. Starting manual partitioning](#starting-manual-partitioning) {#starting-manual-partitioning .title}

You can configure custom disk partitioning during RHEL installation to create a storage layout that meets your specific requirements. Manual partitioning provides full control over disk usage, mount points, and file system types for optimized system performance and data organization.

**Prerequisites**

-   The **Installation Summary** screen is open.
-   All disks are available to the installation program.

**Procedure**

1.  Select disks for installation:

    a.  Click **Installation Destination** to open the **Installation Destination** window.
    b.  Select the disks that you require for installation by clicking the corresponding icon. A selected disk has a check-mark displayed on it.
    c.  Under **Storage Configuration**, select the **Custom** radio-button.
    d.  Click **Done**.

2.  Detected mount points are listed in the left-hand pane. The mount points are organized by detected operating system installations. As a result, some file systems may be displayed multiple times if a partition is shared among several installations.

    a.  Select the mount points in the left pane; the options that can be customized are displayed in the right pane.

    b.  Optional: If your system contains existing file systems, ensure that enough space is available for the installation. To remove any partitions, select them in the list and click the - button. The dialog has a checkbox that you can use to remove all other partitions used by the system to which the deleted partition belongs.

    c.  Optional: If there are no existing partitions and you want to create a set of partitions as a starting point, select your preferred partitioning scheme from the left pane. The default partitioning scheme for Red Hat Enterprise Linux is LVM. Then, click the **Click here to create them automatically** link.

        Note

        A `/boot`{.literal} partition, a `/`{.literal} (root) volume, and a `swap`{.literal} volume proportional to available storage are created and listed in the left pane. Additional partitions can also be created, depending on system properties such as architecture. These are the file systems for a typical installation, but you can add additional file systems and mount points.

3.  Optional: Continue with adding mount points and configuring the individual mount points.

4.  Click Done to confirm any changes and return to the **Installation Summary** window.

#### [10.5.4. Supported file systems](#supported-file-systems) {#supported-file-systems .title}

When configuring manual partitioning, you can optimize performance, ensure compatibility, and effectively manage disk space by utilizing the various file systems and partition types available in Red Hat Enterprise Linux.

xfs
:   The XFS file system is the default file system on Red Hat Enterprise Linux. It is a highly scalable, high-performance file system. It supports file systems up to 16 exabytes and files up to 8 exabytes. It also supports directory structures containing tens of millions of entries. XFS supports metadata journaling for faster crash recovery. `XFS`{.literal} also supports metadata journaling for faster crash recovery. The maximum supported size of a single XFS file system is 1 PB. XFS cannot be shrunk to get free space.

ext4
:   The `ext4`{.literal} file system is based on the `ext3`{.literal} file system and features a number of improvements. These features include support for larger file systems and larger files. They also provide faster and more efficient disk space allocation, unlimited subdirectories, faster file system checking, and more robust journaling. The maximum supported size of a single `ext4`{.literal} file system is 50 TB.

ext3
:   The `ext3`{.literal} file system is based on the `ext2`{.literal} file system and has one main advantage - journaling. A journaling file system recovers faster after an unexpected stop. You do not need to run `fsck`{.literal} every time to check metadata consistency.

ext2
:   An `ext2`{.literal} file system supports standard Unix file types, including regular files, directories, or symbolic links. It provides the ability to assign long file names, up to 255 characters.

swap
:   Swap partitions are used to support virtual memory. In other words, data is written to a swap partition when there is not enough RAM to store the data your system is processing.

vfat

:   The `VFAT`{.literal} file system is a Linux file system that is compatible with Microsoft Windows long file names on the FAT file system.

    Note

    Support for the `VFAT`{.literal} file system is not available for Linux system partitions. For example, `/`{.literal}, `/var`{.literal}, `/usr`{.literal} and so on.

BIOS Boot
:   A very small partition required for booting from a device with a GUID partition table (GPT) on BIOS systems and UEFI systems in BIOS compatibility mode.

EFI System Partition
:   A small partition required for booting a device with a GUID partition table (GPT) on a UEFI system.

PReP
:   This small boot partition is located on the first partition of the disk. The `PReP`{.literal} boot partition contains the GRUB2 boot loader, which allows other IBM Power Systems servers to boot Red Hat Enterprise Linux.

**Additional resources**

-   [Red Hat Enterprise Linux Technology Capabilities and Limits (Red Hat Knowledgebase)](https://access.redhat.com/articles/rhel-limits)

#### [10.5.5. Adding a file system mount point](#adding-a-mount-point-file-system) {#adding-a-file-system-mount-point .title}

You can add multiple file system mount points. Use any of the file systems and partition types available, such as XFS, ext4, ext3, ext2, swap, and VFAT. You can also use specific partitions such as BIOS Boot, EFI System Partition, and PReP. It helps you to configure the system's storage.

**Prerequisites**

-   You have planned your partitions.
-   You haven't specified mount points at paths with symbolic links, such as `/var/mail`{.literal}, `/usr/tmp`{.literal}, `/lib`{.literal}, `/sbin`{.literal}, `/lib64`{.literal}, and `/bin`{.literal}. The payload, including RPM packages, depends on creating symbolic links to specific directories.

**Procedure**

1.  Click + to create a new file system and related mount point. The **Add a New Mount Point** dialog opens.

2.  Select one of the preset paths from the **Mount Point** drop-down menu or type your own; for example, select `/`{.literal} for the root partition or `/boot`{.literal} for the boot partition.

3.  Enter the size of the file system into the **Desired Capacity** field; for example, `2GiB`{.literal}.

    If you do not specify a value in **Desired Capacity**, or if you specify a size bigger than available space, then all remaining free space is used.

4.  Click Add mount point to create the partition and return to the **Manual Partitioning** window.

#### [10.5.6. Configuring storage for a mount point file system](#configuring-storage-for-a-mount-point-file-system) {#configuring-storage-for-a-mount-point-file-system .title}

For each manually created mount point, you can set the partitioning scheme. GUI options are **Standard Partition**, **LVM**, and **LVM Thin Provisioning**. Btrfs support was removed in Red Hat Enterprise Linux 10. The `/boot`{.literal} partition always uses a standard partition.

**Procedure**

1.  To change the devices that a single non-LVM mount point should be located on, select the required mount point from the left-hand pane.
2.  Under the **Device(s)** heading, click Modify. The **Configure Mount Point** dialog opens.
3.  Select one or more devices and click Select to confirm your selection and return to the **Manual Partitioning** window.
4.  Click Update Settings to apply the changes.
5.  In the lower left-hand side of the **Manual Partitioning** window, click the **storage device selected** link to open the **Selected Disks** dialog and review disk information.
6.  Optional: Click the Rescan button (circular arrow button) to refresh all local disks and partitions; this is only required after performing advanced partition configuration outside the installation program. Clicking the Rescan Disks button resets all configuration changes made in the installation program.

#### [10.5.7. Customizing a mount point file system](#customizing-a-mount-point-file-system) {#customizing-a-mount-point-file-system .title}

While you can customize a partition or volume to apply specific settings, partitioning `/usr`{.literal} or `/var`{.literal} separately from the root volume makes the boot process more complex because these directories contain critical system components.

In some cases, such as when `/usr`{.literal} or `/var`{.literal} are located on an iSCSI drive or FCoE location, the system might fail to boot or hang with a `Device is busy`{.literal} error during shutdown or reboot. This limitation applies only to `/usr`{.literal} or `/var`{.literal}, not to their subdirectories. For example, a separate `/var/www`{.literal} partition works correctly.

**Procedure**

1.  From the left pane, select the mount point.

2.  From the right-hand pane, you can customize the following options:

    a.  Enter the file system mount point into the **Mount Point** field. For example, if a file system is the root file system, enter `/`{.literal}; enter `/boot`{.literal} for the `/boot`{.literal} file system, and so on. For a swap file system, do not set the mount point as setting the file system type to `swap`{.literal} is sufficient.

    b.  Enter the size of the file system in the **Desired Capacity** field. You can use common size units such as KiB or GiB. The default is MiB if you do not set any other unit.

    c.  Select the device type that you require from the drop-down **Device Type** menu: `Standard Partition`{.literal}, `LVM`{.literal}, or `LVM Thin Provisioning`{.literal}.

        Note

        `RAID`{.literal} is available only if two or more disks are selected for partitioning. If you choose `RAID`{.literal}, you can also set the `RAID Level`{.literal}. Similarly, if you select `LVM`{.literal}, you can specify the `Volume Group`{.literal}.

    d.  Select the **Encrypt** checkbox to encrypt the partition or volume. You must set a password later in the installation program.

    e.  Select the appropriate file system type for this partition or volume from the **File system** drop-down menu.

        Note

        Support for the `VFAT`{.literal} file system is not available for Linux system partitions. For example, `/`{.literal}, `/var`{.literal}, `/usr`{.literal}, and so on.

    f.  Select the **Reformat** checkbox to format an existing partition, or clear the **Reformat** checkbox to retain your data. The newly-created partitions and volumes must be reformatted, and the checkbox cannot be cleared.

    g.  Type a label for the partition in the **Label** field. Use labels to easily recognize and address individual partitions.

    h.  Type a name in the **Name** field. The standard partitions are named automatically when they are created and you cannot edit the names of standard partitions. For example, you cannot edit the `/boot`{.literal} name `sda1`{.literal}.

3.  Click Update Settings to apply your changes and if required, select another partition to customize. Changes are not applied until you click Begin Installation from the **Installation Summary** window.

4.  Optional: Click Reset All to discard your partition changes.

5.  Click Done when you have created and customized all file systems and mount points. If you choose to encrypt a file system, you are prompted to create a passphrase.

    A **Summary of Changes** dialog box opens, displaying a summary of all storage actions for the installation program.

6.  Click Accept Changes to apply the changes and return to the **Installation Summary** window.

#### [10.5.8. Preserving the /home directory](#preserving-the-home-directory) {#preserving-the-home-directory .title}

During a Red Hat Enterprise Linux 10 graphical installation, you can keep the `/home`{.literal} directory from an existing Red Hat Enterprise Linux 9 system only if it resides on a separate `/home`{.literal} partition.

Retaining the `/home`{.literal} directory preserves various user configuration settings. Consequently, the GNOME Shell environment on the new Red Hat Enterprise Linux 10 system can appear the same as it did on the Red Hat Enterprise Linux 9 system. This behavior applies only to users whose user name and ID match those on the earlier Red Hat Enterprise Linux 9 installation.

**Prerequisites**

-   You have RHEL 9 installed on your computer.
-   The `/home`{.literal} directory is located on a separate `/home`{.literal} partition on your RHEL 9 system.
-   The Red Hat Enterprise Linux 10 `Installation Summary`{.literal} window is open.

**Procedure**

1.  Click **Installation Destination** to open the **Installation Destination** window.

2.  Under **Storage Configuration**, select the **Custom** radio button. Click **Done**.

3.  Click Done, the **Manual Partitioning** window opens.

4.  Choose the `/home`{.literal} partition, fill in `/home`{.literal} under `Mount Point:`{.literal} and clear the **Reformat** checkbox.

    **Figure 10.1. Ensuring that /home is not formatted**

5.  Optional: You can also customize various aspects of the `/home`{.literal} partition required for your Red Hat Enterprise Linux 10 system as described in [Customizing a mount point file system](#customizing-a-mount-point-file-system "10.5.7. Customizing a mount point file system"). However, to preserve `/home`{.literal} from your RHEL 9 system, it is necessary to clear the **Reformat** checkbox.

6.  After you customized all partitions according to your requirements, click Done. The **Summary of changes** dialog box opens.

7.  Verify that the **Summary of changes** dialog box does not show any change for `/home`{.literal}. This means that the `/home`{.literal} partition is preserved.

8.  Click Accept Changes to apply the changes, and return to the **Installation Summary** window.

#### [10.5.9. Software RAID support](#software-raid-support) {#software-raid-support .title}

Redundant Arrays of Independent Disks (RAID) devices consists of multiple storage devices. These device combine to provide increased performance and, in some configurations, greater fault tolerance. You can create a RAID device in one step and add or remove disks as necessary.

You can configure one RAID partition for each physical disk in your system. The number of disks available to the installation program determines the levels of RAID device available. For example, if your system has two disks, you cannot create a `RAID 10`{.literal} device, as it requires a minimum of three separate disks. To optimize system's storage performance and reliability, RHEL supports software `RAID 0`{.literal}, `RAID 1`{.literal}, `RAID 4`{.literal}, `RAID 5`{.literal}, `RAID 6`{.literal}, and `RAID 10`{.literal} types with LVM and LVM Thin Provisioning to configure storage.

Note

On 64-bit IBM Z®, the storage subsystem uses RAID transparently. You do not have to configure software RAID manually.

#### [10.5.10. Creating a software RAID during the installation](#creating-a-software-raid-during-the-installation) {#creating-a-software-raid-during-the-installation .title}

You can create a software RAID during Red Hat Enterprise Linux installation to configure multiple disks as a single logical device. This can improve performance, reliability, or both.

**Prerequisites**

-   You have selected two or more disks for installation before RAID configuration options are visible. Depending on the RAID type you want to create, at least two disks are required.
-   You have selected the Custom radio button on the **Installation Destination** window. You have entered the Manual Partitioning window by clicking on the **Done** button.
-   You have created a mount point. By configuring a mount point, you can configure the RAID device.

**Procedure**

1.  From the left pane of the **Manual Partitioning** window, select the required partition.
2.  Click the **Device Type** drop-down menu and select **RAID**.
3.  Under the **Device(s)** section, click Modify. The **Configure Mount Point** dialog box opens.
4.  Select the disks that you want to include in the RAID device and click Select to close the dialog box.
5.  Click the **File System** drop-down menu and select your preferred file system type.
6.  Click the **RAID Level** drop-down menu and select your preferred level of RAID.
7.  Click Update Settings to save your changes.
8.  Click Done to apply the settings to return to the **Installation Summary** window.

**Additional resources**

-   [Creating a RAID LV with DM integrity](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_logical_volumes/configuring-raid-logical-volumes#creating-a-raid-logical-volume-with-dm-integrity)
-   [Managing RAID](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_storage_devices/managing-raid)

#### [10.5.11. Creating an LVM logical volume](#creating-an-lvm-logical-volume) {#creating-an-lvm-logical-volume .title}

Logical Volume Management (LVM) provides a logical view of physical storage such as disks or LUNs. Partitions become physical volumes that you group into volume groups. You can divide each group into logical volumes, which function like disk partitions and can span multiple physical disks.

Important

-   LVM configuration is available only in the graphical and the Kickstart installation. During text-mode installation, LVM configuration is not available.
-   To create an LVM configuration in the text mode, press Ctrl+Alt+F2 to use a shell prompt in a different virtual console. You can run `vgcreate`{.literal} and `lvm`{.literal} commands in this shell. To return to the text-mode installation, press Ctrl+Alt+F1.

**Procedure**

1.  From the **Manual Partitioning** window, create a new mount point by using any of the following options:

    -   Use the **Click here to create them automatically** option or click the **+** button.

    -   Select Mount Point from the drop-down list or enter manually.

    -   Enter the size of the file system in to the **Desired Capacity** field; for example, 70 GiB for `/`{.literal}, 2 GiB for `/boot`{.literal}.

        Note: Skip this step to use the existing mount point.

2.  Select the mount point.

3.  Select `LVM`{.literal} in the drop-down menu. The **Volume Group** drop-down menu is displayed with the newly-created volume group name.

    Note

    You cannot specify the size of the volume group's physical extents in the configuration dialog. The size is always set to the default value of 4 MiB. If you want to create a volume group with different physical extents, create it manually by switching to an interactive shell and using the `vgcreate`{.literal} command. You can also use a Kickstart file with the `volgroup --pesize=`{.literal}*`size`{.literal}* command.

4.  Click Done to return to the **Installation Summary** window.

**Additional resources**

-   [Configuring and managing logical volumes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_logical_volumes/index)

#### [10.5.12. Configuring an LVM logical volume](#configuring-an-lvm-logical-volume) {#configuring-an-lvm-logical-volume .title}

You can configure a newly-created LVM logical volume based on your requirements.

**Procedure**

1.  From the **Manual Partitioning** window, create a mount point by using any of the following options:

    -   Use the **Click here to create them automatically** option or click the **+** button.

    -   Select Mount Point from the drop-down list or enter manually.

    -   Enter the size of the file system in to the **Desired Capacity** field; for example, 70 GiB for `/`{.literal}, 2 GiB for `/boot`{.literal}.

        Skip this step to use the existing mount point.

        Warning

        Red Hat does not support placing the `/boot`{.literal} partition on a Logical Volume Manager (LVM) volume.

2.  Select the mount point.

3.  Click the **Device Type** drop-down menu and select `LVM`{.literal}. The **Volume Group** drop-down menu is displayed with the newly-created volume group name.

4.  Click Modify to configure the newly-created volume group. The **Configure Volume Group** dialog box opens.

    Note

    You cannot specify the size of the volume group's physical extents in the configuration dialog. The size is always set to the default value of 4 MiB. If you want to create a volume group with different physical extents, create it manually by switching to an interactive shell and by using the `vgcreate`{.literal} command. You can also use a Kickstart file with the `volgroup --pesize=`{.literal}*`size`{.literal}* command. For more information, see the [Automatically installing RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/index) document.

5.  Optional: From the **RAID Level** drop-down menu, select the RAID level that you require.

    The available RAID levels are the same as with actual RAID devices.

6.  Select the **Encrypt** checkbox to encrypt the volume group.

7.  From the **Size policy** drop-down menu, select any of the following size policies for the volume group:

    The available policy options are:

    Automatic
    :   The size of the volume group is set automatically so that it is large enough to contain the configured logical volumes. This is optimal if you do not need free space within the volume group.

    As large as possible
    :   The volume group is created with maximum size, regardless of the size of the configured logical volumes it contains. This is optimal if you plan to keep most of your data on LVM and later need to increase the size of some existing logical volumes, or if you need to create additional logical volumes within this group.

    Fixed
    :   You can set an exact size of the volume group. Any configured logical volumes must then fit within this fixed size. This is useful if you know exactly how large you need the volume group to be.

8.  Click Save to apply the settings and return to the **Manual Partitioning** window.

9.  Click Update Settings to save your changes.

10. Click Done to return to the **Installation Summary** window.

#### [10.5.13. Understanding disk partitioning strategies](#advice-on-partitions) {#understanding-disk-partitioning-strategies .title}

There is no best way to partition every system. The optimal configuration depends on how you plan to use the system being installed. However, these tips may help you find the optimal layout for your needs.

-   Create partitions that have specific requirements first, for example, if a particular partition must be on a specific disk.

-   Consider encrypting any partitions and volumes which might contain sensitive data. Encryption prevents unauthorized people from accessing the data on the partitions, even if they have access to the physical storage device. In most cases, you should at least encrypt the `/home`{.literal} partition, which contains user data.

-   In some cases, creating separate mount points for directories other than `/`{.literal}, `/boot`{.literal} and `/home`{.literal} may be useful. For example, a separate `/var/lib/mysql`{.literal} mount point preserves a MySQL database during reinstallation, eliminating the need to restore the database from backup afterward. However, having unnecessary separate mount points makes storage administration more difficult.

-   Some special restrictions apply to certain directories with regards to which partitioning layouts can be placed. Notably, the `/boot`{.literal} directory must always be on a physical partition (not on an LVM volume).

-   Each kernel requires approximately: 60MiB (initrd 28MiB, 16MiB vmlinuz, and 9MiB System.map)

-   For rescue mode: 100MiB (initrd 56MiB, 16MiB vmlinuz, and 9MiB System map)

-   When `kdump`{.literal} is enabled in system it takes another approximately 40MiB (another initrd with 33MiB)

    The default partition size of 2 GiB for `/boot`{.literal} should suffice for most common use cases. However, increase the size of this partition if you are planning on retaining multiple kernel releases or errata kernels.

-   The `/var`{.literal} directory holds content for a number of applications, including the Apache web server, and is used by the DNF package manager to temporarily store downloaded package updates. Ensure that the partition or volume containing `/var`{.literal} has at least 5 GiB.

-   The `/usr`{.literal} directory holds the majority of software on a typical Red Hat Enterprise Linux installation. The partition or volume containing this directory should therefore be at least 5 GiB for minimal installations, and at least 10 GiB for installations with a graphical environment.

-   If you partition `/usr`{.literal} or `/var`{.literal} separately from the rest of the root volume, the boot process becomes complex as these directories contain boot-critical components. In some situations, such as when these directories are on an iSCSI drive or FCoE location, the system may be unable to boot. It can also hang with a `Device is busy`{.literal} error during shutdown or reboot.

    This limitation only applies to `/usr`{.literal} or `/var`{.literal}, not to directories under them. For example, a separate partition for `/var/www`{.literal} works without issues.

    Important

    Some security policies require the separation of `/usr`{.literal} and `/var`{.literal}, even though it makes administration more complex.

-   Consider leaving a portion of the space in an LVM volume group unallocated. This unallocated space gives you flexibility if your space requirements change but you do not want to remove data from other volumes. You can also select the `LVM Thin Provisioning`{.literal} device type for the partition to have the unused space handled automatically by the volume.

-   The size of an XFS file system cannot be reduced. If you need to make a partition or volume with this file system smaller, you must back up your data, destroy the file system, and create a new, smaller one in its place. Therefore, if you plan to alter your partitioning layout later, you should use the `ext4`{.literal} file system instead.

-   Use Logical Volume Management (LVM) if you anticipate expanding your storage by adding more disks or expanding virtual machine disks post-installation. With LVM, create physical volumes on the new drives and then assign them to any volume group and logical volume as you see fit. For example, you can easily expand your system's `/home`{.literal} (or any other directory residing on a logical volume).

-   Creating a BIOS Boot partition or an EFI System Partition may be necessary, depending on your system's firmware, boot drive size, and boot drive disk label. You cannot create a BIOS Boot or EFI System Partition in graphical installation if your system does **not** require one. In that case, they are hidden from the menu.

**Additional resources**

-   [How to use dm-crypt on IBM Z, LinuxONE and with the PAES cipher](https://www.ibm.com/docs/en/linux-on-systems?topic=volumes-creating-volume-pervasive-encryption)
-   [Linux File system Hierarchy Standard](http://refspecs.linuxfoundation.org/FHS_2.3/fhs-2.3.html)

#### [10.5.14. Additional resources](#configuring-manual-partitioning_10514-additional-resources) {#additional-resources .title}

-   [Advantages and disadvantages of using partitioning on LUNs (Red Hat Knowledgebase)](https://access.redhat.com/solutions/163853)

### [10.6. Configuring the base environment and additional software](#configuring-the-base-environment-and-additional-software) {#configuring-the-base-environment-and-additional-software .title}

You can choose the appropriate base environment and additional software packages during Red Hat Enterprise Linux installation from the **Software Selection** window to customize your system for specific use cases.

**Prerequisites**

-   You have configured the installation source.
-   The installation program has downloaded package metadata.
-   The **Installation Summary** window is open.

**Procedure**

1.  From the **Installation Summary** window, click **Software Selection**. The **Software Selection** window opens.

2.  From the **Base Environment** pane, select a base environment. You can select only one base environment, for example, Server with GUI (default), Server, Minimal Install, Workstation, Custom Operating System, Virtualization Host. By default, the **Server with GUI** base environment is selected.

3.  Optional: For installations on ARM based systems, select the **Page size** that you want to use from **Kernel Options**.

    By default, Kernel with a **4k** page size is selected.

4.  From the **Additional Software for Selected Environment** pane, select one or more options.

5.  Click Done to apply the settings and return to graphical installations.

**Additional resources**

-   [The 4k and 64k page size Kernel Options](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_monitoring_and_updating_the_kernel/index#what-is-kernel-64k)

### [10.7. Optional: Configuring the network and host name](#optional-configuring-the-network-and-host-name) {#optional-configuring-the-network-and-host-name .title}

You can use the **Network and Host name** window to configure network interfaces. Options that you select here are available both during the installation for tasks such as downloading packages from a remote location, and on the installed system.

#### [10.7.1. Configuring network and host name](#configuring-network-and-host-name) {#configuring-network-and-host-name .title}

You can configure network interfaces and set the system hostname during RHEL installation from the **Network and Hostname** section. It enables network connectivity for package downloads, remote installations, and ensures proper system identification on your network infrastructure.

**Procedure**

1.  From the **Installation Summary** window, click Network and Host Name.

2.  From the list in the left-hand pane, select an interface. The details are displayed in the right-hand pane.

3.  Toggle the ON/OFF switch to enable or disable the selected interface.

    You cannot add or remove interfaces manually.

4.  Click + to add a virtual network interface, which can be either: Bond, Bridge, or VLAN.

5.  Click - to remove a virtual interface.

6.  Click Configure to change settings such as IP addresses, DNS servers, or routing configuration for an existing interface (both virtual and physical).

7.  Type a host name for your system in the **Host Name** field.

    The host name can either be a fully qualified domain name (FQDN) in the format *`hostname.domainname`{.literal}*, or a short hostname without the domain. Many networks have a Dynamic Host Configuration Protocol (DHCP) service that automatically supplies connected systems with a domain name. To allow the DHCP service to assign the domain name to this system, specify only the short host name.

    Host names can only contain alphanumeric characters and `-`{.literal} or `.`{.literal}. Host name should be equal to or less than 64 characters. Host names cannot start or end with `-`{.literal} and `.`{.literal}. To be compliant with DNS, each part of a FQDN should be equal to or less than 63 characters. Also, the FQDN total length, including dots, should not exceed 255 characters.

    The value `localhost`{.literal} means that no specific static host name for the target system is configured. Also, the actual host name of the installed system is configured during the processing of the network configuration, for example, by NetworkManager using DHCP or DNS.

    When using static IP and host name configuration, it depends on the planned system use case whether to use a short name or FQDN. Red Hat Identity Management configures FQDN during provisioning but some 3rd party software products may require a short name. In either case, to ensure availability of both forms in all situations, add an entry for the host in `/etc/hosts`{.literal} in the format `IP FQDN short-alias`{.literal}.

8.  Click Apply to apply the host name to the installer environment.

9.  Alternatively, in the **Network and Hostname** window, you can choose the Wireless option. Click Select network in the right-hand pane to select your wifi connection, enter the password if required, and click Connect.

**Additional resources**

-   [Automatically installing RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/index#creating-kickstart-files_rhel-installer)
-   [Configuring and managing networking](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_networking/index/)

#### [10.7.2. Adding a virtual network interface](#adding-a-virtual-network-interface) {#adding-a-virtual-network-interface .title}

You can add virtual network interfaces during RHEL installation to configure advanced networking features such as bonding, bridging, and VLANs. It enables high availability, load balancing, and network segmentation for improved network performance and reliability.

**Procedure**

1.  From the **Network & Host name** window, click the + button to add a virtual network interface. The **Add a device** dialog opens.

2.  Select one of the four available types of virtual interfaces:

    -   **Bond**: NIC (*Network Interface Controller*) Bonding, a method to bind multiple physical network interfaces together into a single bonded channel.
    -   **Bridge**: Represents NIC Bridging, a method to connect multiple separate networks into one aggregate network.
    -   **Vlan** (*Virtual LAN*): A method to create multiple distinct broadcast domains which are mutually isolated.

3.  Select the interface type and click Add. An editing interface dialog box opens, allowing you to edit any available settings for your chosen interface type. For more information, see [Editing network interface](#editing-network-interface-configuration "10.7.3. Editing network interface configuration").

4.  Click Save to confirm the virtual interface settings and return to the **Network & Host name** window.

5.  Optional: To change the settings of a virtual interface, select the interface and click Configure.

#### [10.7.3. Editing network interface configuration](#editing-network-interface-configuration) {#editing-network-interface-configuration .title}

You can edit network interface configuration during RHEL installation to customize network settings for wired and wireless connections. This enables configuration of IP addresses, DNS settings, routing, and other network parameters to meet specific network requirements.

On 64-bit IBM Z® systems, you cannot add a new network connection. You must group network subchannels and set them online during the boot phase, which is the only supported time for this configuration.

**Procedure**

-   To configure a network connection manually, select the interface from the **Network and Host name** window and click Configure.

    An editing dialog specific to the selected interface opens. The available options are different depending on whether the connection type is a physical interface or virtual interface. Physical interface can be a wired or wireless network interface controller. Virtual interface can be Bond, Bridge, Team (deprecated), or Vlan, which was previously configured in [Adding a virtual interface](#adding-a-virtual-network-interface "10.7.2. Adding a virtual network interface").

#### [10.7.4. Enabling or Disabling the Interface Connection](#enabling-or-disabling-the-interface-connection) {#enabling-or-disabling-the-interface-connection .title}

You can enable or disable network interface connections during RHEL installation to control network access and connectivity. This configuration determines which network interfaces are active and how they connect automatically, affecting system network behavior and security.

**Procedure**

1.  Click the **General** tab.

2.  Select the **Connect automatically with priority** checkbox to enable connection by default. Keep the default priority setting at `0`{.literal}.

3.  Optional: Enable or disable all users on the system from connecting to this network by using the **All users may connect to this network** option. If you disable this option, only `root`{.literal} will be able to connect to this network.

    Important

    When enabled on a wired connection, the system automatically connects during startup or reboot. On a wireless connection, the interface attempts to connect to any known wireless networks in range. For further information about NetworkManager, including the `nm-connection-editor`{.literal} tool, see the [*Configuring and managing networking*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_networking/index) document.

4.  Click Save to apply the changes and return to the **Network and Host name** window.

    It is not possible to only allow a specific user other than `root`{.literal} to use this interface, as no other users are created at this point during the installation. If you need a connection for a different user, you must configure it after the installation.

#### [10.7.5. Setting up Static IPv4 or IPv6 Settings](#setting-up-static-ipv4-or-ipv6-settings) {#setting-up-static-ipv4-or-ipv6-settings .title}

By default, both IPv4 and IPv6 use automatic configuration. This means when the interface is connected, IP addresses, DNS, and other settings are set automatically. In many cases, this is sufficient, but you can also provide static configuration in the **IPv4 Settings** and **IPv6 Settings** tabs.

**Procedure**

1.  To set static network configuration, navigate to one of the IPv Settings tabs and from the **Method** drop-down menu, select a method other than **Automatic**, for example, **Manual**. The **Addresses** pane is enabled.

2.  Optional: In the **IPv6 Settings** tab, you can also set the method to **Ignore** to disable IPv6 on this interface.

3.  Click Add and enter your address settings.

4.  Type the IP addresses in the **Additional DNS servers** field; it accepts one or more IP addresses of DNS servers, for example, `10.0.0.1,10.0.0.8`{.literal}.

5.  Select the **Require IPv*X* addressing for this connection to complete** checkbox.

    Selecting this option in the **IPv4 Settings** or **IPv6 Settings** tabs allow this connection only if IPv4 or IPv6 was successful. If this option remains disabled for both IPv4 and IPv6, the interface is able to connect if configuration succeeds on either IP protocol.

6.  Click Save to apply the changes and return to the **Network & Host name** window.

#### [10.7.6. Configuring Routes](#configuring-routes) {#configuring-routes .title}

You can control the access of specific connections by configuring routes.

**Procedure**

1.  In the **IPv4 Settings** and **IPv6 Settings** tabs, click Routes to configure routing settings for a specific IP protocol on an interface. An editing routes dialog specific to the interface opens.

2.  Click Add to add a route.

3.  Select the **Ignore automatically obtained routes** checkbox to configure at least one static route and to disable all routes not specifically configured.

4.  Select the **Use this connection only for resources on its network** checkbox to prevent the connection from becoming the default route.

    This option can be selected even if you did not configure any static routes. This route is used only to access certain resources, such as intranet pages that require a local or VPN connection. Another (default) route is used for publicly available resources. Unlike the additional routes configured, this setting is transferred to the installed system. This option is useful only when you configure more than one interface.

5.  Click OK to save your settings and return to the editing routes dialog that is specific to the interface.

6.  Click Save to apply the settings and return to the **Network and Host Name** window.

### [10.8. Optional: Configuring the keyboard layout](#optional-configuring-the-keyboard-layout) {#optional-configuring-the-keyboard-layout .title}

Configure keyboard layouts during installation from the **Installation Summary** screen to support different languages and regional input methods. This configuration ensures proper character input, special symbols, and keyboard shortcuts for international users and multilingual environments.

Add the **English** (**United States**) layout if you use a keyboard layout without Latin characters (for example, **Russian**). Latin characters are required to enter paraphrases or user credentials during the installation process.

**Procedure**

1.  From the **Installation Summary** window, click **Keyboard**.

2.  Click + to open the **Add a Keyboard Layout** window to change to a different layout.

3.  Select a layout by browsing the list or use the **Search** field.

4.  Select the required layout and click Add. The new layout appears under the default layout.

5.  Optional: Click Options to configure a keyboard switch that you can use to cycle between available layouts in the installed system (this is not used during the installation). The **Layout Switching Options** window opens.

    -   To configure key combinations for switching, select one or more key combinations and click OK to confirm your selection.

6.  Optional: When you select a layout, click the **Keyboard** button to open a new dialog box displaying a visual representation of the selected layout.

7.  Click Done to apply the settings and return to graphical installations.

### [10.9. Optional: Configuring the language support](#optional-configuring-the-language-support) {#optional-configuring-the-language-support .title}

During RHEL installation, configure additional language support from **Installation Summary** to enable localization for specific regions and languages. It ensures proper character encoding, date formats, and cultural conventions for international, multilingual deployments.

**Procedure**

1.  From the **Installation Summary** window, click **Language Support**. The **Language Support** window opens. The left pane lists the available language groups. If at least one language from a group is configured, a check mark is displayed and the supported language is highlighted.
2.  From the left pane, click a group to select additional languages, and from the right pane, select regional options. Repeat this process for all the languages that you want to configure.
3.  Optional: Search the language group by typing in the text box, if required.
4.  Click Done to apply the settings and return to graphical installations.

### [10.10. Optional: Configuring the date and time-related settings](#optional-configuring-the-date-and-time-related-settings) {#optional-configuring-the-date-and-time-related-settings .title}

Configure date, time, and timezone settings from the *Installation Summary* screen during Red Hat Enterprise Linux installation. It ensures proper time synchronization and regional timezone configuration. You can configure NTP for automatic synchronization to select the appropriate timezone for your location.

**Procedure**

1.  From the **Installation Summary** window, click **Time & Date**. The **Time & Date** window opens.
2.  Under **Time zone**, select the **Region** by using the drop-down menu. Select **Etc** as your region to configure a time zone relative to Greenwich Mean Time (GMT) without setting your location to a specific region.
3.  From the **City** drop-down menu, select the city, or the city closest to your location in the same time zone.
4.  The **Automatic date and time** option is selected by default. It uses network time synchronization by using the Network Time Protocol (NTP). NTP keeps your system time correct as long as the system can access the internet. By default, one NTP pool is configured.
5.  Optional: Use the Configure NTP button to add a new NTP, or disable or remove the default options.
6.  Select **Manual date and time** option to set date and time manually by using the controls displayed on the screen.
7.  Click Done to apply the settings and return to graphical installations.

### [10.11. Optional: Subscribing and activating Red Hat Lightspeed](#optional-subscribing-and-activating-red-hat-insights) {#optional-subscribing-and-activating-red-hat-lightspeed .title}

Red Hat Lightspeed is a Software-as-a-Service (SaaS) offering. It provides continuous, in-depth analysis of registered Red Hat-based systems. The analysis proactively identifies threats to security, performance, and stability across physical, virtual, cloud, and container environments.

You can register your Red Hat Enterprise Linux system using your account or activation key to connect to Red Hat Lightspeed. This Software-as-a-Service (SaaS) offering provides predictive analytics and continuous analysis to maintain a secure IT environment.

**Procedure**

1.  From the **Installation Summary** screen, under **Software**, click **Connect to Red Hat**.

2.  Select **Account** or **Activation Key**.

    a.  If you select **Account**, enter your Red Hat Customer Portal username and password details.

    b.  If you select **Activation Key**, enter your organization ID and activation key.

        You can enter more than one activation key, separated by a comma, as long as the activation keys are registered to your subscription.

3.  Select the **Set System Purpose** checkbox. Setting system purpose values are important for accurate reporting of consumption in the subscription services.

4.  Select the required **Role**, **SLA**, and **Usage** from the corresponding drop-down lists.

5.  The **Connect to Red Hat Lightspeed** checkbox is enabled by default. Clear the checkbox if you do not want to connect to Red Hat Lightspeed.

6.  Optional: Expand **Options**.

    a.  Select the **Use HTTP proxy** checkbox if you have configured the network environment to allow external Internet access, or access to content servers through an HTTP proxy. Clear the **Use HTTP proxy** checkbox if an HTTP proxy is not used.

7.  Click Register to register the system. When the system is successfully registered and subscriptions are attached, the **Connect to Red Hat** window displays the attached subscription details.

    Depending on the amount of subscriptions, the registration and attachment process might take up to a minute to complete.

8.  Click Done to return to the **Installation Summary** window.

    A *Registered* message is displayed under **Connect to Red Hat**.

**Additional resources**

-   [About Red Hat Lightspeed](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/release_notes/index)

### [10.12. Optional: Using network-based repositories](#optional-using-network-based-repositories) {#optional-using-network-based-repositories .title}

You can configure an installation source from auto-detected media, Red Hat CDN, or the network. When the **Installation Summary** window opens, the installation source is set based on the boot media. The full Red Hat Enterprise Linux Server DVD configures the source as local media.

**Prerequisites**

-   You have downloaded the full installation DVD ISO or minimal installation Boot ISO image from the [Product Downloads](https://access.redhat.com/downloads/content/rhel) page.
-   You have created bootable installation media.
-   The **Installation Summary** window is open.

**Procedure**

1.  From the **Installation Summary** window, click **Installation Source**. The **Installation Source** window opens.

    The **Auto-detected installation media** option is selected by default if you started the installation program from media containing an installation source, for example, a DVD.

2.  Optional: Select the **Red Hat CDN** option to register your system, attach RHEL subscriptions, and install RHEL from the Red Hat Content Delivery Network (CDN).

3.  Optional: Select the **On the network** option to download and install packages from a network location instead of local media. This option is available only when a network connection is active. See [Configuring network and host name options](#optional-configuring-the-network-and-host-name "10.7. Optional: Configuring the network and host name") for information about how to configure network connections in the GUI.

    a.  Select the **On the network** drop-down menu to specify the protocol for downloading packages. This setting depends on the server that you want to use.

    b.  Type the server address (without the protocol) into the address field. If you choose NFS, a second input field opens where you can specify custom **NFS mount options**. This field accepts options listed in the `nfs(5)`{.literal} man page on your system.

    c.  When selecting an NFS installation source, specify the address with a colon (`:`{.literal}) character separating the host name from the path. For example, `server.example.com:/path/to/directory`{.literal}.

        The following steps are optional and are only required if you use a proxy for network access.

    d.  Click Proxy setup to configure a proxy for an HTTP or HTTPS source.

        i.  Select the **Enable HTTP proxy** checkbox and type the URL into the **Proxy Host** field.
        ii. Select the **Use Authentication** checkbox if the proxy server requires authentication.
        iii. Type in your user name and password.
        iv. Click OK to finish the configuration and exit the **Proxy Setup...​** dialog box.

4.  Optional: If your HTTP or HTTPS URL refers to a repository mirror, select the required option from the **URL type** drop-down list. All environments and additional software packages are available for selection when you finish configuring the sources.

5.  Click Done to apply the settings and return to the **Installation Summary** window.

### [10.13. Optional: Configuring Kdump kernel crash-dumping mechanism](#optional-configuring-kdump-kernel-crash-dumping-mechanism) {#optional-configuring-kdump-kernel-crash-dumping-mechanism .title}

`Kdump`{.literal} is a kernel crash-dumping mechanism that captures system memory contents during a crash. You can analyze the captured memory to determine the cause of the crash. If `Kdump`{.literal} is enabled, a small portion of system RAM is reserved for it and is inaccessible to the main kernel.

**Procedure**

1.  From the **Installation Summary** window, click **Kdump**. The **Kdump** window opens.

2.  Select the **Enable kdump** checkbox.

3.  Select either the **Automatic** or **Manual** memory reservation setting.

4.  If you select **Manual**, enter the amount of memory (in megabytes) that you want to reserve in the **Memory to be reserved** field using the **+** and **-** buttons. The **Usable System Memory** readout shows how much memory remains available after your reservation.

5.  Click Done to apply the settings and return to graphical installations.

    The amount of memory that you reserve is determined by your system architecture. For example, AMD64 and Intel 64 have different requirements than IBM Power. The amount of memory also depends on the total amount of system memory. In most cases, automatic reservation is satisfactory.

    Configure additional settings, such as the kernel crash dump location, after installation. Use the `system-config-kdump`{.literal} graphical interface or manually edit the `/etc/kdump.conf`{.literal} configuration file.

## [Chapter 11. Registering your RHEL system](#registering-your-rhel-system) {#chapter-11.-registering-your-rhel-system .title}

After installing Red Hat Enterprise Linux, register your system to receive updates and to access Red Hat services. You can register your system by using various methods:

-   RHC client
-   Graphical user interface
-   Subscription manager
-   Registration assistant

The RHC client provides the following flexible features to register your RHEL system and manage the extent of data collection:

-   Access to Red Hat content: Provides access to Red Hat CDN repositories.
-   Analytics for Red Hat Lightspeed: Enables data collection for Red Hat Lightspeed.
-   Remote management: Establishes an additional MQTT network connection to Red Hat services for remote execution of certain actions from console.redhat.com.

By default, the RHC client enables all available features. However, you can override this behavior by enabling or disabling specific features based on your connectivity requirements. Review the available options and select the appropriate features based on your internal policies on data and network connectivity.

Note

Use the RHC client only for systems directly connecting to Hybrid Cloud Console, the RHC client currently does not support Satellite.

### [11.1. Registering a system by using the RHC client](#registering-a-system-by-using-the-rhc-client-with-the-default-feature-levels) {#registering-a-system-by-using-the-rhc-client .title}

Register your RHEL system by using the RHC client to connect to Red Hat services with the default feature levels. This enables all available features: access to Red Hat content, analytics for Red Hat Lightspeed, and remote management.

**Prerequisites**

-   You have an activation key and an organization ID to register your system.

**Procedure**

1.  Open the command-line window.

2.  Do one of the following:

    a.  To register the system with the default feature level and ensure system runs the **Remediation** and **Tasks** from Red Hat Lightspeed:

        ``` {.language-plaintext tabindex="-1"}
        # rhc connect --activation-key=<activation_key> --organization=<organization_ID>
        ```

        ``` {.language-plaintext tabindex="-1"}
        # dnf install -y rhc-worker-playbook
        ```

    b.  To disable any of the features while registering your system:

        ``` {.language-plaintext tabindex="-1"}
        # rhc connect --activation-key=<activation_key> --organization=<organization_ID> --disable-feature <feature>
        ```

        Where *feature* can be replaced with:

        -   content - Provides access to Red Hat CDN repositories.

        -   analytics - Enables data collection for Red Hat Lightspeed.

        -   remote-management - Establishes an additional MQTT network connection to Red Hat services for remote execution of certain actions from console.redhat.com.

            For example, to register your system with remote management disabled, enter the following command. In this configuration, the system cannot be managed remotely but still accesses RHEL content and collects data for Red Hat Lightspeed analytics.

            ``` {.language-plaintext tabindex="-1"}
            # rhc connect --activation-key=<activation_key> --organization=<organization_ID> --disable-feature remote-management
            ```

**Verification**

-   Confirm the active features when registering with default options:

    ``` {.language-plaintext tabindex="-1"}
    # rhc status
    ```

    ``` {.language-plaintext tabindex="-1"}
    Connection status:
    ✓ Connected to Red Hat Subscription Management
    ✓ Connected to Red Hat Lightspeed
    ✓ The yggdrasil service is active
    Manage your connected systems: https://red.ht/connector
    ```

-   Confirm the active features with remote-management disabled:

    ``` {.language-plaintext tabindex="-1"}
    # rhc status
    ```

    ``` {.language-plaintext tabindex="-1"}
    Connection status:
    ✓ Connected to Red Hat Subscription Management
    ✓ Connected to Red Hat Lightspeed
    ● The yggdrasil service is inactive
    ```

**Additional resources**

-   [Remote Host Configuration and Management](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/remote_host_configuration_and_management/index)

### [11.2. Registering your system using the subscription manager](#registering-your-system-using-the-command-line) {#registering-your-system-using-the-subscription-manager .title}

You can register your Red Hat Enterprise Linux subscription by using the command line to get software updates and access Red Hat services.

Use the RHC client for an improved and simplified experience registering your hosts to Red Hat. The RHC client registers your system to Red Hat making your system ready for Red Hat Lightspeed data collection. It also enables direct issue remediation from Red Hat Lightspeed for Red Hat Enterprise Linux. For more information, see [RHC registration](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/getting_started_with_rhel_system_registration/index#assembly-basic-reg-rhel-cli-rhc_assembly-basic-reg-rhel-cli-rhc).

**Prerequisites**

-   You have an active, non-evaluation Red Hat Enterprise Linux subscription.
-   Your Red Hat subscription status is verified.
-   You have successfully installed Red Hat Enterprise Linux and logged into the system as root.

**Procedure**

1.  Open the command-line interface (CLI) as a root user.

2.  Register your Red Hat Enterprise Linux system by using the activation key:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager register --activationkey=<activation_key_name> --org=<organization_ID>
    ```

    When the system is successfully registered, an output similar to the following is displayed:

    ``` {.language-plaintext tabindex="-1"}
    The system has been registered with ID:
    62edc0f8-855b-4184-b1b8-72a9dc793b96
    ```

**Additional resources**

-   [Using an activation key to register a system with Red Hat Subscription Manager](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/getting_started_with_rhel_system_registration/index#assembly-basic-reg-rhel-cli-rhc_assembly-basic-reg-rhel-cli-rhc)
-   [Getting Started with RHEL System Registration](https://docs.redhat.com/en/documentation/subscription_central/2023/html/getting_started_with_rhel_system_registration/index)

### [11.3. Registering RHEL 10 using the installer GUI](#registering-rhel-using-the-installer-gui) {#registering-rhel-10-using-the-installer-gui .title}

You can register a Red Hat Enterprise Linux by using the RHEL installer GUI to get software updates and access Red Hat services.

**Prerequisites**

-   You have a valid user account on the Red Hat Customer Portal. See the [Create a Red Hat Login page](https://www.redhat.com/wapps/ugc/register.html?_flowId=register-flow&_flowExecutionKey=e1s1).
-   You have a valid Activation Key and Organization ID.

**Procedure**

1.  From the **Installation Summary** screen, under **Software**, click **Connect to Red Hat**.

2.  Authenticate your Red Hat account using the **Account** or **Activation Key** option.

3.  Optional: In the **Set System Purpose** field select the **Role**, **SLA**, and **Usage** attribute that you want to set from the drop-down menu.

    At this point, your Red Hat Enterprise Linux system has been successfully registered.

### [11.4. Registration Assistant](#registration-assistant) {#registration-assistant .title}

Registration Assistant is designed to help you choose the most suitable registration option for your Red Hat Enterprise Linux environment:

-   For assistance with using a username and password to register RHEL with the Subscription Manager client, see the [RHEL registration assistant](https://access.redhat.com/labs/registrationassistant/) on the Customer Portal.
-   For assistance with registering your RHEL system to Red Hat Lightspeed, see the [Red Hat Lightspeed registration assistant](https://console.redhat.com/lightspeed/registration#SIDs=&tags=) on the Hybrid Cloud Console.

### [11.5. Additional resources](#registering-your-rhel-system_115-additional-resources) {#additional-resources-1 .title}

-   [Using an activation key to register a system with Red Hat Subscription Manager](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/getting_started_with_rhel_system_registration/index#proc-reg-rhel-rhc-act-key)
-   [Getting Started with RHEL System Registration](https://docs.redhat.com/documentation/en-us/subscription_central/2023/html/getting_started_with_rhel_system_registration/index)
-   [Red Hat Satellite Documentation](https://docs.redhat.com/en/documentation/red_hat_satellite)

## [Chapter 12. Configuring System Purpose with subscription-manager CLI](#configuring-system-purpose-with-subscription-manager-cli) {#chapter-12.-configuring-system-purpose-with-subscription-manager-cli .title}

To optimize Red Hat Enterprise Linux subscription usage, use the system purpose feature. In the Red Hat Hybrid Cloud Console SaaS application of your Red Hat account, view subscription usage. You can configure system purpose attributes on activation keys or with subscription-manager.

**Prerequisites**

-   You have installed and registered your Red Hat Enterprise Linux 10 system, but system purpose is not configured.
-   You are logged in as a `root`{.literal} user.

**Procedure**

1.  From the command line, run the following command to set the intended role of the system:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager syspurpose role --set VALUE
    ```

    Replace `VALUE`{.literal} with the role that you want to assign:

    -   `Red Hat Enterprise Linux Server`{.literal}
    -   `Red Hat Enterprise Linux Workstation`{.literal}
    -   `Red Hat Enterprise Linux Compute Node`{.literal}

    For example:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager syspurpose role --set Red Hat Enterprise Linux Server
    ```

    a.  Optional: Before setting a value, see the available roles supported by the subscriptions for your organization:

        ``` {.language-plaintext tabindex="-1"}
        # subscription-manager syspurpose role --list
        ```

    b.  Optional: Run the following command to unset the role:

        ``` {.language-plaintext tabindex="-1"}
        # subscription-manager syspurpose role --unset
        ```

2.  Run the following command to set the intended Service Level Agreement (SLA) of the system:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager syspurpose service-level --set VALUE
    ```

    Replace `VALUE`{.literal} with the SLA that you want to assign:

    -   `Premium`{.literal}
    -   `Standard`{.literal}
    -   `Self-Support`{.literal}

    For example:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager syspurpose service-level --set "Standard"
    ```

    a.  Optional: Before setting a value, see the available service-levels supported by the subscriptions for your organization:

        ``` {.language-plaintext tabindex="-1"}
        # subscription-manager syspurpose service-level --list
        ```

    b.  Optional: Run the following command to unset the SLA:

        ``` {.language-plaintext tabindex="-1"}
        # subscription-manager syspurpose service-level --unset
        ```

3.  Run the following command to set the intended usage of the system:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager syspurpose usage --set "VALUE"
    ```

    Replace `VALUE`{.literal} with the usage that you want to assign:

    -   `Production`{.literal}
    -   `Disaster Recovery`{.literal}
    -   `Development/Test`{.literal}

    For example:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager syspurpose usage --set "Production"
    ```

    a.  Optional: Before setting a value, see the available usages supported by the subscriptions for your organization:

        ``` {.language-plaintext tabindex="-1"}
        # subscription-manager syspurpose usage --list
        ```

    b.  Optional: Run the following command to unset the usage:

        ``` {.language-plaintext tabindex="-1"}
        # subscription-manager syspurpose usage --unset
        ```

4.  Run the following command to show the current system purpose properties:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager syspurpose --show
    ```

    a.  Optional: For more detailed syntax information run the following command to access the `subscription-manager`{.literal} man page and browse to the SYSPURPOSE OPTIONS:

        ``` {.language-plaintext tabindex="-1"}
        # man subscription-manager
        ```

**Verification**

-   To verify the system's subscription status:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager status
    ```

    ``` {.language-plaintext tabindex="-1"}
    +-------------------------------------------+
       System Status Details
    +-------------------------------------------+
    Overall Status: Registered
    ```

    For more information about the subscriptions services, see the [Getting Started with the Subscriptions Service guide](https://docs.redhat.com/en/documentation/subscription_central/2023/html-single/getting_started_with_the_subscriptions_service/index#doc-wrapper).

## [Chapter 13. Post-installation security hardening](#post-installation-security-hardening) {#chapter-13.-post-installation-security-hardening .title}

RHEL is designed with robust security features enabled by default. However, you can enhance its security further through additional hardening measures.

For more information about:

-   Processes and practices for securing RHEL servers and workstations against local and remote intrusion, exploitation, and malicious activity, see [Security hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/index).
-   Control how users and processes interact with the files on the system or control which users perform what actions by mapping them to specific SELinux confined users, see [Using SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/index).
-   Tools and techniques to improve the security of your networks and lower the risks of data breaches and intrusions, see [Securing networks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/index).
-   Packet filters, such as firewalls, that use rules to control incoming, outgoing, and forwarded network traffic, see [Configuring firewalls and packet filters](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/index).

## [Chapter 14. Changing a subscription service](#changing-a-subscription-service) {#chapter-14.-changing-a-subscription-service .title}

To manage the subscriptions, register a RHEL system with either Red Hat Subscription Management Server or Red Hat Satellite Server. If required, you can change the subscription service at a later point.

To change the subscription service under which you are registered, unregister the system from the current service and then register it with a new service.

To receive the system updates, register your system with either of the management servers.

This section contains information about how to unregister your RHEL system from the Red Hat Subscription Management Server and Red Hat Satellite Server.

### [14.1. Prerequisites](#prerequisites) {#prerequisites .title}

You have registered your system with any one of the following:

-   Red Hat Subscription Management Server
-   Red Hat Satellite Server version 6.17

To receive the system updates, register your system with either of the management servers.

### [14.2. Unregistering from Subscription Management Server](#unregistering-from-subscription-management-server) {#unregistering-from-subscription-management-server .title}

You can unregister a RHEL system from Red Hat Subscription Management Server by using a command line and the Subscription Manager user interface.

#### [14.2.1. Unregistering using command line](#unregistering-using-command-line) {#unregistering-using-command-line .title}

Use the `unregister`{.literal} command to unregister a RHEL system from Red Hat Subscription Management Server.

**Procedure**

-   Run the unregister command as a root user or `sudo`{.literal}, without any additional parameters.

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager unregister
    ```

    The system is unregistered from the Subscription Management Server, and the status \'System Not Registered\' is displayed with the Register System.. button enabled.

    To continue uninterrupted services, re-register the system with either of the management services. If you do not register the system with a management service, you may fail to receive the system updates.

**Additional resources**

-   [Using and Configuring Red Hat Subscription Manager](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/getting_started_with_rhel_system_registration/index#assembly-adv-reg-rhel-using-rhsm_assembly-adv-reg-rhel-using-rhsm)
-   [Registering your system using the command line](#registering-your-system-using-the-command-line "11.2. Registering your system using the subscription manager")

#### [14.2.2. Unregistering by using Subscription Manager user interface](#unregistering-using-subscription-manager-user-interface) {#unregistering-by-using-subscription-manager-user-interface .title}

You can unregister a RHEL system from Red Hat Subscription Management Server by using the Subscription Manager user interface.

**Procedure**

1.  Log in to your system.

2.  From the top left-hand side of the window, click **Activities**.

3.  From the menu options, click the **Show Applications** icon.

4.  Click the **Settings** icon, or enter **Settings Manager** in the search.

5.  In the left side column, select the **System** options, then on the new screen select **Registration**.

    The Registration screen displays the current status of your Subscription.

6.  Click the **Remove Registration...** button and confirm your choice.

7.  Enter your administrator password in the **Authentication Required** dialog box. The system is unregistered from the **Subscription Management Server**, and the status **System Not Registered** is displayed with the **Register System...** button enabled.

    To continue uninterrupted services, re-register the system with either of the management services. If you do not register the system with a management service, you may fail to receive the system updates.

**Additional resources**

-   [Registering your system using the Subscription Manager User Interface](#registering-your-rhel-system "Chapter 11. Registering your RHEL system")
-   [Using an activation key to register a system with Red Hat Subscription Manager](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/getting_started_with_rhel_system_registration/index#proc-reg-rhel-rhc-act-key)

### [14.3. Unregistering from Satellite Server](#unregistering-from-satellite-server) {#unregistering-from-satellite-server .title}

Removing a RHEL system from Satellite Server updates only the server-side status. The local system registration remains unchanged. To fully transition to Red Hat Subscription Management (RHSM), manually unregister the system and restore `/etc/rhsm/rhsm.conf`{.literal} to its default configuration.

**Procedure**

1.  [Remove the host from the Satellite server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html/managing_hosts/administering_hosts_managing-hosts#Removing_a_Host_from_Server_managing-hosts).

2.  Unregister the system:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager unregister
    ```

3.  Revert the `/etc/rhsm/rhsm.conf`{.literal} configuration file to its default values:

    ``` {.language-plaintext tabindex="-1"}
    # cd /etc/rhsm/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # mv rhsm.conf.bak rhsm.conf
    ```

    Note

    You can restore this file only if the original content of the file was backed up earlier. Otherwise, you must manually restore the file from a non-modified RHEL machine.

4.  Verify that the `/etc/rhsm/rhsm.conf`{.literal} file has been reverted to default values:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager config --list
    ```

    ``` {.language-plaintext tabindex="-1"}
    [server]
       hostname = [subscription.rhsm.redhat.com]
       insecure = [0]
       no_proxy = []
       port = [443]
       prefix = [/subscription]
       proxy_hostname = []
       proxy_password = []
       proxy_port = []
       proxy_scheme = [http]
       proxy_user = []
       server_timeout = [180]
       ssl_verify_depth = [3]

    [rhsm]
       auto_enable_yum_plugins = [1]
       baseurl = [https://cdn.redhat.com]
       ca_cert_dir = [/etc/rhsm/ca/]
       consumercertdir = [/etc/pki/consumer]
       entitlementcertdir = [/etc/pki/entitlement]
       full_refresh_on_yum = [0]
       inotify = [1]
       manage_repos = [1]
       package_profile_on_trans = [0]
       pluginconfdir = [/etc/rhsm/pluginconf.d]
       plugindir = [/usr/share/rhsm-plugins]
       productcertdir = [/etc/pki/product]
       repo_ca_cert = /etc/rhsm/ca/redhat-uep.pem
       repomd_gpg_url = []
       report_package_profile = [1]

    [rhsmcertd]
       auto_registration = [0]
       auto_registration_interval = [60]
       autoattachinterval = [1440]
       certcheckinterval = [240]
       disable = [0]
       splay = [1]

    [logging]
       default_log_level = [INFO]

    [] - Default value in use
    ```

5.  Register the system:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager register
    ```

    ``` {.language-plaintext tabindex="-1"}
    Username: <_redhat_portal_admin_username_>
    Password:
    ```

6.  Enable the required repositories:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --disable "*"
    ```

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos
    ```

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable=<repo-id>
    ```

## [Chapter 15. Changing basic environment settings](#changing-basic-environment-settings) {#chapter-15.-changing-basic-environment-settings .title}

If your requirements change after installation, you can update the basic system settings accordingly. These basic system settings include Keyboard layout, Date and time, and System locale.

### [15.1. Configuring the keyboard layout](#configuring-the-keyboard-layout) {#configuring-the-keyboard-layout .title}

The keyboard layout settings control the layout used on the text console. If RHEL was installed with a different keyboard layout than the one you use after the installation, you can change the layout.

**Procedure**

1.  To list available keymaps:

    ``` {.language-plaintext tabindex="-1"}
    $ localectl list-keymaps
    ```

    ``` {.language-plaintext tabindex="-1"}
    ANSI-dvorak
    al
    al-plisi
    amiga-de
    de
    de-nodeadkeys
    ...
    ```

2.  Optional: Display the current keymap settings:

    ``` {.language-plaintext tabindex="-1"}
    $ localectl status
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    VC Keymap: us
    ...
    ```

3.  Change the system keymap, for example:

    ``` {.language-plaintext tabindex="-1"}
    # localectl set-keymap de-nodeadkeys
    ```

    For more information, see the `localectl(1)`{.literal}, `locale(7)`{.literal}, and `locale.conf(5)`{.literal} man pages on your system.

### [15.2. Configuring the date, time and timezone settings manually](#configuring-the-date-and-time) {#configuring-the-date-time-and-timezone-settings-manually .title}

For accurate timekeeping, you can manually configure date, time, and time zone settings on Red Hat Enterprise Linux systems. Proper time configuration is essential for authentication, logging, troubleshooting, and consistency across systems. Prefer time synchronization by using `chrony`{.literal}.

**Procedure**

1.  Optional: List the timezones:

    ``` {.language-plaintext tabindex="-1"}
    # timedatectl list-timezones
    ```

    ``` {.language-plaintext tabindex="-1"}
      Europe/Berlin
    ```

2.  Set the time zone:

    ``` {.language-plaintext tabindex="-1"}
    # timedatectl set-timezone <time_zone>
    ```

3.  Set the date and time:

    ``` {.language-plaintext tabindex="-1"}
    # timedatectl set-time <YYYY-mm-dd HH:MM-SS>
    ```

**Verification**

1.  Display the date, time, and timezone:

    ``` {.language-plaintext tabindex="-1"}
    # date
    ```

    ``` {.language-plaintext tabindex="-1"}
    Mon May 5 09:11:55 CEST 2025
    ```

2.  To see more details, use the timedatectl command:

    ``` {.language-plaintext tabindex="-1"}
    # timedatectl
    ```

    ``` {.language-plaintext tabindex="-1"}
     Local time: Mon 2025-05-05 09:11:55 CEST
               Universal time: Mon 2025-05-05 07:11:55 UTC
                     RTC time: Mon 2025-05-05 07:11:55
                    Time zone: Europe/Berlin (CEST, +0200)
    System clock synchronized: no
                  NTP service: inactive
              RTC in local TZ: no
    ```

    For more information, see the `date(1)`{.literal} and `timedatectl(1)`{.literal} man pages on your system.

### [15.3. Configuring the system locale](#configuring-the-system-locale) {#configuring-the-system-locale .title}

The system locale specifies the language settings used by system services and user interfaces. System-wide locale settings determine the language, region, and formatting conventions used by the operating system and its applications.

These settings are stored in the `/etc/locale.conf`{.literal} file, which the `systemd`{.literal} daemon reads during early boot. Services and users inherit the locale settings configured in `/etc/locale.conf`{.literal}, unless individual users or programs override them.

**Procedure**

1.  Optional: Display the current system locales settings:

    ``` {.language-plaintext tabindex="-1"}
    # localectl status
    ```

    ``` {.language-plaintext tabindex="-1"}
    System Locale: LANG=C.UTF-8
        VC Keymap: de-nodeadkeys
       X11 Layout: de
    ```

2.  List available system locale settings:

    ``` {.language-plaintext tabindex="-1"}
    $ localectl list-locales
    ```

    ``` {.language-plaintext tabindex="-1"}
    C.UTF-8
    ...
    en_US.UTF-8
    en_ZA.UTF-8
    en_ZW.UTF-8
    ...
    ```

3.  Update the system locale setting, for example::

    ``` {.language-plaintext tabindex="-1"}
    # localectl set-locale LANG=en_US.UTF-8
    ```

    For more information, see the `localectl(1)`{.literal}, `locale(7)`{.literal}, and `locale.conf(5)`{.literal} man pages on your system.

## [Chapter 16. Tools and tips for troubleshooting and bug reporting](#troubleshooting-at-the-start-of-the-installation) {#chapter-16.-tools-and-tips-for-troubleshooting-and-bug-reporting .title}

The troubleshooting information in these sections might be helpful when diagnosing issues at the start of the installation process. These sections are for all supported architectures. However, if an issue is for a particular architecture, it is specified at the start of the section.

### [16.1. Dracut](#dracut) {#dracut .title}

`Dracut`{.literal} is a tool that manages the `initramfs`{.literal} image during the Linux operating system boot process. The `dracut`{.literal} emergency shell is an interactive mode that can be initiated while the `initramfs`{.literal} image is loaded. You can run basic troubleshooting commands from the `dracut`{.literal} emergency shell.

For more information, see the **Troubleshooting** section of the `dracut`{.literal} man page on your system.

### [16.2. Using installation log files](#using-installation-log-files) {#using-installation-log-files .title}

For debugging purposes, the installation program logs installation actions in files that are located in the `/tmp`{.literal} directory. The table lists the log files.

+-------------------------------------+--------------------------------------------------------------------------------------------------+
| Log file                            | Contents                                                                                         |
+:====================================+:=================================================================================================+
| `/tmp/anaconda.log`{.literal}       | General messages.                                                                                |
+-------------------------------------+--------------------------------------------------------------------------------------------------+
| `/tmp/program.log`{.literal}        | All external programs run during the installation.                                               |
+-------------------------------------+--------------------------------------------------------------------------------------------------+
| `/tmp/storage.log`{.literal}        | Extensive storage module information.                                                            |
+-------------------------------------+--------------------------------------------------------------------------------------------------+
| `/tmp/packaging.log`{.literal}      | dnf and rpm package installation messages.                                                       |
+-------------------------------------+--------------------------------------------------------------------------------------------------+
| `/tmp/dbus.log`{.literal}           | Information about the `dbus`{.literal} session that is used for installation program modules.    |
+-------------------------------------+--------------------------------------------------------------------------------------------------+
| `/tmp/sensitive-info.log`{.literal} | Configuration information that is not part of other logs and not copied to the installed system. |
+-------------------------------------+--------------------------------------------------------------------------------------------------+
| `/tmp/syslog`{.literal}             | Hardware-related system messages. This file contains messages from other Anaconda files.         |
+-------------------------------------+--------------------------------------------------------------------------------------------------+

: Table 16.1. Log files generated during the installation

Show more

If the installation fails, the messages are consolidated into `/tmp/anaconda-tb-identifier`{.literal}, where identifier is a random string. After a successful installation, these files are copied to the installed system under the directory `/var/log/anaconda/`{.literal}. However, if the installation is unsuccessful, or if the `inst.nosave=all`{.literal} or `inst.nosave=logs`{.literal} options are used when booting the installation system, these logs only exist in the installation program's RAM disk. This means that the logs are not saved permanently and are lost when the system is powered down. To store them permanently, copy the files to another system on the network or copy them to a mounted storage device such as a USB flash drive.

#### [16.2.1. Creating pre-installation log files](#creating-pre-installation-log-files) {#creating-pre-installation-log-files .title}

You can set the `inst.debug`{.literal} option to create log files before the installation process starts. These log files contain, for example, the current storage configuration.

**Prerequisites**

-   The Red Hat Enterprise Linux boot menu is open.

**Procedure**

1.  Select the **Install Red Hat Enterprise Linux** option from the boot menu.

2.  Press the Tab key on BIOS-based systems or the e key on UEFI-based systems to edit the selected boot options.

3.  Append `inst.debug`{.literal} to the options. For example:

    ``` {.language-plaintext tabindex="-1"}
    vmlinuz ... inst.debug
    ```

4.  Press the Enter key on your keyboard. The system stores the pre-installation log files in the `/tmp/pre-anaconda-logs/`{.literal} directory before the installation program starts.

5.  Press Ctrl + Alt + F2 to switch to the console and access the log files.

6.  Change to the `/tmp/pre-anaconda-logs/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cd /tmp/pre-anaconda-logs/
    ```

**Additional resources**

-   [Boot options reference](#boot-options-reference "Chapter 18. Boot options reference")
-   [Console logging during installation](#consoles-and-logging-during-installation "Chapter 9. Consoles and logging during installation")

#### [16.2.2. Transferring installation log files to a USB drive](#transferring-installation-log-files-to-a-usb-drive) {#transferring-installation-log-files-to-a-usb-drive .title}

You can transfer installation log files to a USB drive to share it further.

**Prerequisites**

-   You have backed up data from the USB drive.
-   You are logged into a root account and you have access to the installation program's temporary file system.

**Procedure**

1.  Press Ctrl + Alt + F2 to access a shell prompt on the system you are installing.

2.  Connect a USB flash drive to the system and run the `dmesg`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # dmesg
    ```

    A log detailing all recent events is displayed. At the end of this log, a set of messages is displayed. For example:

    ``` {.language-plaintext tabindex="-1"}
    [ 170.171135] sd 5:0:0:0: [sdb] Attached SCSI removable disk
    ```

3.  Note the name of the connected device. In the earlier example, it is `sdb`{.literal}.

4.  Navigate to the `/mnt`{.literal} directory and create a new directory that serves as the mount target for the USB drive. This example uses the name `usb`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir usb
    ```

5.  Mount the USB flash drive onto the newly created directory. In most cases, you do not want to mount the whole drive, but a partition on it. Do not use the name `sdb`{.literal}, use the name of the partition you want to write the log files to. In this example, the name `sdb1`{.literal} is used:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/sdb1 /mnt/usb
    ```

6.  Verify that you mounted the correct device and partition by accessing it and listing its contents:

    ``` {.language-plaintext tabindex="-1"}
    # cd /mnt/usb
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls
    ```

7.  Copy the log files to the mounted device.

    ``` {.language-plaintext tabindex="-1"}
    # cp /tmp/*log /mnt/usb
    ```

8.  Unmount the USB flash drive. If you receive an error message that the target is busy, change your working directory to outside the mount (for example, /).

    ``` {.language-plaintext tabindex="-1"}
    # umount /mnt/usb
    ```

#### [16.2.3. Transferring installation log files over the network](#transferring-installation-log-files-over-the-network) {#transferring-installation-log-files-over-the-network .title}

Transfer RHEL installation log files over the network to analyze installation issues and troubleshoot problems. By using this method, you can collect diagnostic information from systems where local access is limited or when you need to share logs with support teams.

**Prerequisites**

-   You are logged into a root account and you have access to the installation program's temporary file system.

**Procedure**

1.  Press Ctrl + Alt + F2 to access a shell prompt on the system you are installing.

2.  Switch to the `/tmp`{.literal} directory where the log files are located:

    ``` {.language-plaintext tabindex="-1"}
    # cd /tmp
    ```

3.  Copy the log files onto another system on the network using the `scp`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # scp *log user@address:path
    ```

    a.  Replace **user** with a valid user name on the target system. Replace **address** with the target system's address or host name. Replace **path** with the path to the directory where you want to save the log files. For example, if you want to log in as `john`{.literal} on a system with an IP address of 192.168.0.122. To store log files in the `/home/john/logs/`{.literal} directory on that system, use the following command:

        ``` {.language-plaintext tabindex="-1"}
        # scp *log john@192.168.0.122:/home/john/logs/
        ```

        When connecting to the target system for the first time, the SSH client asks you to confirm that the fingerprint of the remote system is correct and that you want to continue:

        ``` {.language-plaintext tabindex="-1"}
        The authenticity of host '192.168.0.122 (192.168.0.122)' can't be established.
        ECDSA key fingerprint is a4:60:76:eb:b2:d0:aa:23:af:3d:59:5c:de:bb:c4:42.
        Are you sure you want to continue connecting (yes/no)?
        ```

    b.  Type **yes** and press Enter to continue. Provide a valid password when prompted. The files are transferred to the specified directory on the target system.

### [16.3. Verifying boot media](#verifying-boot-media) {#verifying-boot-media .title}

Verifying ISO images helps to avoid problems that are sometimes encountered during installation. These sources include DVD and ISO images stored on a disk or NFS server. You can test the integrity of an ISO-based installation source before using it to install Red Hat Enterprise Linux.

**Prerequisites**

-   You have accessed the Red Hat Enterprise Linux boot menu.

**Procedure**

1.  From the boot menu, select **Test this media & install Red Hat Enterprise Linux 10** to test the boot media.
2.  The boot process tests the media and highlights any issues.
3.  Optional: You can start the verification process by appending `rd.live.check`{.literal} to the boot command line. For more information, see [Customizing boot options](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/optional-customizing-boot-options#optional-customizing-boot-options).

### [16.4. Display settings and device drivers](#display-settings-and-device-drivers) {#display-settings-and-device-drivers .title}

Some video cards have trouble booting into the Red Hat Enterprise Linux graphical installation program. If the installation program does not run using its default settings, it attempts to run in a lower resolution mode. If that fails, the installation program attempts to run in text mode.

There are several possible solutions to resolve display issues, most of which involve specifying custom boot options:

For more information, see [Console boot options](#console-boot-options "18.3. Console boot options").

+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Solution                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+:========================================+:========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| Use the basic graphics mode             | You can attempt to perform the installation using the basic graphics driver. To do this, either select **Troubleshooting \> Install Red Hat Enterprise Linux in basic graphics mode** from the boot menu.                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Use the text mode                       | You can attempt to perform the installation using the text mode. For details, refer to [Installing RHEL in text mode](https://access.redhat.com/articles/4323781).                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Specify the display resolution manually | If the installation program fails to detect your screen resolution, you can override the automatic detection and specify it manually. To do this, append the **inst.resolution=x** option at the boot menu, where **x** is your display's resolution, for example, 1024x768. For more information, see [Customizing boot options](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/optional-customizing-boot-options#optional-customizing-boot-options). |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Use an alternate video driver           | You can attempt to specify a custom video driver, overriding the installation program's automatic detection.                                                                                                                                                                                                                                                                                                                                                                                                                            |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Perform the installation using RDP      | If the earlier listed options fail, you can use a separate system to access the graphical installation over the network, by using the [Remote Desktop Protocol (RDP)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/index#starting-a-remote-installation-by-using-the-remote-desktop-protocol).                                                                                                                                                              |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 16.2. Solutions

Show more

-   If specifying a custom video driver solves your problem, you should report it as a bug in [Jira](https://issues.redhat.com/projects/RHEL/issues). The installation program should be able to detect your hardware automatically and use the appropriate driver without intervention.

## [Chapter 17. Troubleshooting after installation](#troubleshooting-after-installation) {#chapter-17.-troubleshooting-after-installation .title}

The troubleshooting information in these sections might be helpful when diagnosing issues after the installation process. These sections are for all supported architectures. However, if an issue is for a particular architecture, it is specified at the start of the section.

### [17.1. Resuming an interrupted download attempt](#resuming-an-interrupted-download-attempt) {#resuming-an-interrupted-download-attempt .title}

You can resume interrupted RHEL ISO image downloads using the `curl`{.literal} command to avoid re-downloading large files from the beginning. It saves time and bandwidth when network interruptions occur during the download process, ensuring efficient acquisition of installation media.

**Prerequisites**

-   You have navigated to the **Product Downloads** section of the Red Hat Customer Portal at [https://access.redhat.com/downloads](https://access.redhat.com/downloads), and selected the required variant, version, and architecture.
-   You have right-clicked on the required ISO file, and selected **Copy Link Location** to copy the URL of the ISO image file to your clipboard.

**Procedure**

1.  Download the ISO image from the new link. Add the `--continue-at -`{.literal} option to automatically resume the download:

    ``` {.language-plaintext tabindex="-1"}
    $ curl --output directory-path/filename.iso 'new_copied_link_location' --continue-at -
    ```

2.  Use a checksum utility such as **sha256sum** to verify the integrity of the image file after the download finishes:

    ``` {.language-plaintext tabindex="-1"}
    $ sha256sum rhel-x.x-x86_64-dvd.iso
                `85a...46c rhel-x.x-x86_64-dvd.iso`
    ```

    Compare the output with reference checksums provided on the Red Hat Enterprise Linux **Product Download** web page.

    *Resuming an interrupted download attempt*

    :   The following is an example of a `curl`{.literal} command for a partially downloaded ISO image:

        ``` {.language-plaintext tabindex="-1"}
        $ curl --output _rhel-x.x-x86_64-dvd.iso 'https://access.cdn.redhat.com//content/origin/files/sha256/85/85a...46c/rhel-x.x-x86_64-dvd.iso?_auth=141...963' --continue-at -
        ```

### [17.2. Disks are not detected](#disks-are-not-detected) {#disks-are-not-detected .title}

If the installation program cannot find a writable storage device to install to, it returns this error message in the **Installation Destination** window. **No disks detected. Please shut down the computer, connect at least one disk, and restart to complete installation.**

Check these items:

-   Your system has at least one storage device attached.
-   If your system uses a hardware RAID controller; verify that the controller is properly configured and working as expected. See your controller's documentation for instructions.
-   If you are installing on one or more iSCSI devices without local storage, verify that all required LUNs are presented to the appropriate Host Bus Adapter (HBA).

If the error message is still displayed after rebooting the system and starting the installation process, the installation program failed to detect the storage. In many cases the error message is a result of attempting to install on an iSCSI device that is not recognized by the installation program.

In this scenario, you must perform a driver update before starting the installation. Check your hardware vendor's website to determine if a driver update is available.

For more general information about driver updates, see the [*Updating drivers during installation*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/index#updating-drivers-during-installation).

You can also consult the Red Hat Hardware Compatibility List, available at [https://access.redhat.com/ecosystem/search/#/category/Server](https://access.redhat.com/ecosystem/search/#/category/Server).

### [17.3. Cannot boot with a RAID card](#cannot-boot-with-a-raid-card) {#cannot-boot-with-a-raid-card .title}

If you cannot boot your system after the installation, you might need to reinstall and repartition your system's storage. Some BIOS types do not support booting from RAID cards.

After you finish the installation and reboot the system for the first time, a text-based screen displays the boot loader prompt (for example, `grub>`{.literal}). It might also display a flashing cursor. If this is the case, you must repartition your system and move your `/boot`{.literal} partition and the boot loader outside of the RAID array. The `/boot`{.literal} partition and the boot loader must be on the same drive. Once these changes are made, you can finish your installation and boot the system properly.

### [17.4. Graphical boot sequence is not responding](#graphical-boot-sequence-is-not-responding) {#graphical-boot-sequence-is-not-responding .title}

When rebooting your system for the first time after installation, the system might be unresponsive during the graphical boot sequence.

If this occurs, a reset is required. In this scenario, the boot loader menu is displayed successfully. But selecting any entry and attempting to boot the system results in a halt. This usually indicates that there is a problem with the graphical boot sequence. To resolve the issue, you must disable the graphical boot by temporarily altering the setting at boot time before changing it permanently.

#### [17.4.1. Disabling the graphical boot permanently](#disabling-the-graphical-boot-permanently) {#disabling-the-graphical-boot-permanently .title}

You can disable the graphical boot permanently by using the grubby tool.

**Procedure**

1.  Log in to the root account on your system.

2.  Use the grubby tool to find the default GRUB2 kernel:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --default-kernel
    ```

    ``` {.language-plaintext tabindex="-1"}
    /boot/vmlinuz-6.12.0-0.el10_0.x86_64
    ```

3.  Use the grubby tool to remove the `rhgb`{.literal} boot option from the default kernel in your GRUB2 configuration. For example:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --remove-args="rhgb" --update-kernel /boot/vmlinuz-6.12.0-0.el10_0.x86_64
    ```

4.  Reboot the system. The graphical boot sequence is no longer used. If you want to enable the graphical boot sequence, follow the same procedure, replacing the `--remove-args="rhgb"`{.literal} parameter with the `--args="rhgb"`{.literal} parameter. This restores the `rhgb`{.literal} boot option to the default kernel in your GRUB2 configuration.

#### [17.4.2. Disabling the graphical boot temporarily](#disabling-the-graphical-boot-temporarily) {#disabling-the-graphical-boot-temporarily .title}

You can disable the graphical boot temporarily by using the boot loader menu.

**Procedure**

1.  Start your system and wait until the boot loader menu is displayed. If you set your boot timeout period to `0`{.literal}, press the Esc key to access it.

2.  From the boot loader menu, use your cursor keys to highlight the entry you want to boot. Press the Tab key on BIOS-based systems or the e key on UEFI-based systems to edit the selected entry options.

3.  In the list of options, find the kernel line - that is, the line beginning with the keyword **linux**. On this line, locate and delete `rhgb`{.literal}.

4.  Press F10 or Ctrl+X to boot your system with the edited options.

    If the system started successfully, you can log in normally. However, if you do not disable graphical boot permanently, you must perform this procedure every time the system boots.

### [17.5. Setting memory manually if RAM is not recognized](#setting-memory-manually-if-ram-is-not-recognized) {#setting-memory-manually-if-ram-is-not-recognized .title}

If the kernel does not detect all installed memory (RAM), you can manually configure the amount of memory using the `mem=`{.literal} boot option to ensure your system uses the expected capacity.

If the reported memory size is lower than the installed amount, one or more memory modules might be faulty. On legacy BIOS-based systems, you can use the Memtest86+ utility to test system memory.

Certain hardware configurations reserve a portion of RAM, making it unavailable to the operating system. For example, laptops with integrated graphics cards often reserve memory for the GPU, so a system with 4 GiB of RAM might show only about 3.7 GiB as available memory.

The kdump crash kernel dumping mechanism also reserves memory for the secondary kernel used during a primary kernel failure. This feature is enabled by default on most Red Hat Enterprise Linux systems, and the reserved memory is not shown as available.

**Procedure**

1.  Check the amount of memory that your system currently reports in MiB:

    ``` {.language-plaintext tabindex="-1"}
    $ free -m
    ```

2.  Reboot your system and wait until the boot loader menu is displayed.

    If your boot timeout period is set to `0`{.literal}, press the Esc key to access the menu.

3.  From the boot loader menu, use your cursor keys to highlight the entry you want to boot. Press the Tab key on BIOS-based systems or the e key on UEFI-based systems to edit the selected entry options.

4.  In the list of options, find the kernel line: that is, the line beginning with the keyword `linux`{.literal}. Append the following option to the end of this line:

    ``` {.language-plaintext tabindex="-1"}
    mem=xxM
    ```

5.  Replace *`xx`{.literal}* with the amount of RAM you have in MiB.

6.  Press F10 or Ctrl+X to boot your system with the edited options.

7.  Wait for the system to boot, log in, and open a command line.

8.  Check the amount of memory that your system reports in MiB:

    ``` {.language-plaintext tabindex="-1"}
    $ free -m
    ```

9.  If the total amount of RAM displayed by the command now matches your expectations, make the change permanent:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=ALL --args="mem=xxM"
    ```

### [17.6. System is displaying signal 11 errors](#system-is-displaying-signal-11-errors) {#system-is-displaying-signal-11-errors .title}

A signal 11 error, commonly known as a segmentation fault, means a program accessed a memory location not allocated to it. A signal 11 error can occur due to a bug in one of the software programs that are installed, or faulty hardware.

If you receive a signal 11 error during the installation process, verify that you are using the most recent installation images. Prompt the installation program to verify them to ensure they are not corrupt.

For more information, see [Verifying Boot media](#verifying-boot-media "16.3. Verifying boot media").

Faulty installation media (such as an improperly burned or scratched optical disk) are a common cause of signal 11 errors. Verify the integrity of the installation media before every installation. For information about obtaining the most recent installation media, refer to the [Product Downloads](https://access.redhat.com/downloads/content/rhel) page.

To perform a media check before the installation starts, append the `rd.live.check`{.literal} boot option at the boot menu. If you performed a media check without any errors and you still have issues with segmentation faults, it usually indicates that your system encountered a hardware error. In this scenario, the problem is most likely in the system's memory (RAM). This can be a problem even if you previously used a different operating system on the same computer without any errors.

Note

For AMD, Intel 64-bit, and 64-bit ARM architectures on BIOS-based systems, use the `Memtest86+`{.literal} memory testing module included on the installation media. Use this module to perform a thorough memory test.

Other possible causes are beyond this document's scope. Consult your hardware manufacturer's documentation and also see the Red Hat Hardware Compatibility List, available online at [https://access.redhat.com/ecosystem/search/#/category/Server](https://access.redhat.com/ecosystem/search/#/category/Server).

### [17.7. Unable to IPL from network storage on IBM Power Systems](#unable-to-ipl-from-network-storage-on-ibm-power-systems) {#unable-to-ipl-from-network-storage-on-ibm-power-systems .title}

If you experience difficulties when trying to IPL from Network Storage Space (NWSSTG), it is most likely due to a missing PReP partition. In this scenario, you must reinstall the system and create this partition during the partitioning phase or in the Kickstart file.

### [17.8. Using rescue mode](#using-rescue-mode) {#using-rescue-mode .title}

The installation program's rescue mode is a minimal Linux environment that you can boot from the Red Hat Enterprise Linux DVD or other boot media. It contains command-line utilities for repairing a wide variety of issues.

Rescue mode can be accessed from the **Troubleshooting** menu of the boot menu. In this mode, you can mount file systems as read-only, denylist or add a driver provided on a driver disc, install or upgrade system packages, or manage partitions.

Note

The installation program's rescue mode is different from rescue mode (an equivalent to single-user mode) and emergency mode, which are provided as parts of the `systemd`{.literal} system and service manager.

To boot into rescue mode, you must boot the system by using Red Hat Enterprise Linux boot media, such as a minimal boot disc, USB drive, or full installation DVD.

Important

Configure advanced storage, such as iSCSI or zFCP devices, by using dracut boot options such as `rd.zfcp=`{.literal} or `root=iscsi:`{.literal} *options*. Alternatively, use the CMS configuration file on 64-bit IBM Z. You cannot configure these storage devices interactively after booting into rescue mode. For information about `dracut`{.literal} boot options, see the `dracut.cmdline(7)`{.literal} man page on your system.

#### [17.8.1. Booting into rescue mode](#booting-into-rescue-mode) {#booting-into-rescue-mode .title}

Boot your RHEL system into rescue mode to troubleshoot and repair system issues when the normal boot process fails. Rescue mode provides a minimal environment to diagnose problems, recover data, and fix configuration issues that prevent normal system operation.

**Procedure**

1.  Boot the system from either minimal boot media, or a full installation DVD or USB drive, and wait for the boot menu to be displayed.

2.  From the boot menu, either select **Troubleshooting** \> **Rescue a Red Hat Enterprise Linux system** option, or append the `inst.rescue`{.literal} option to the boot command line. To enter the boot command line, press the Tab key on BIOS-based systems or the e key on UEFI-based systems.

3.  Optional: If your system requires a third-party driver provided on a driver disc to boot, append the `inst.dd=driver_name`{.literal} to the boot command line:

    ``` {.language-plaintext tabindex="-1"}
    inst.rescue inst.dd=driver_name
    ```

4.  Optional: If a driver that is part of the Red Hat Enterprise Linux distribution prevents the system from booting, append the `modprobe.blacklist=`{.literal} option to the boot command line:

    ``` {.language-plaintext tabindex="-1"}
    inst.rescue modprobe.blacklist=driver_name
    ```

5.  Press Enter (BIOS-based systems) or Ctrl+X (UEFI-based systems) to boot the modified option. Wait until the following message is displayed:

    ``` {.language-plaintext tabindex="-1"}
    The rescue environment now attempts to find your Linux installation and mount it under the directory: /mnt/sysroot/. You can then make any changes required to your system. Choose 1 to proceed with this step. You can choose to mount your file systems read-only instead of read-write by choosing 2. If for some reason this process does not work, choose 3 to skip directly to a shell.

    1) Continue
    2) Read-only mount
    3) Skip to shell
    4) Quit (Reboot)
    ```

    If you select **1**, the installation program attempts to mount your file system under the directory `/mnt/sysroot/`{.literal}. You are notified if it fails to mount a partition. If you select **2**, it attempts to mount your file system under the directory `/mnt/sysroot/`{.literal}, but in read-only mode. If you select **3**, your file system is not mounted.

    For the system root, the installer supports two mount points `/mnt/sysimage`{.literal} and `/mnt/sysroot`{.literal}. The `/mnt/sysroot`{.literal} path is used to mount `/`{.literal} of the target system. Usually, the physical root and the system root are the same, so `/mnt/sysroot`{.literal} is attached to the same file system as `/mnt/sysimage`{.literal}. The only exceptions are rpm-ostree systems, where the system root changes based on the deployment. Then, `/mnt/sysroot`{.literal} is attached to a subdirectory of `/mnt/sysimage`{.literal}. Use `/mnt/sysroot`{.literal} for chroot.

6.  Select **1** to continue. Once your system is in rescue mode, a prompt appears on VC (virtual console) 1 and VC 2. Use the `Ctrl+Alt+F1`{.literal} key combination to access VC 1 and `Ctrl+Alt+F2`{.literal} to access VC 2:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2#
    ```

7.  Even if your file system is mounted, the default root partition in rescue mode is a temporary root partition. It is not the root partition used during normal user mode (multi-user.target or graphical.target). If you selected to mount your file system and it mounted successfully, change the rescue mode root partition to your file system root partition. Run the following command:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2# chroot /mnt/sysroot
    ```

    This is useful if you need to run commands, such as `rpm`{.literal}, that require your root partition to be mounted as `/`{.literal}. To exit the chroot environment, type **exit** to return to the prompt.

8.  If you selected **3**, you can still try to mount a partition or LVM2 logical volume manually inside rescue mode. To do so, create a directory, such as `/directory/`{.literal}, and run the following command:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2# mount -t xfs /dev/mapper/VolGroup00-LogVol02 /directory
    ```

    In this command, `/directory/`{.literal} is the directory that you created and `/dev/mapper/VolGroup00-LogVol02`{.literal} is the LVM2 logical volume you want to mount. If the partition is a different type than XFS, replace the xfs string with the correct type (such as ext4).

9.  If you do not know the names of all physical partitions, use the following command to list them:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2# fdisk -l
    ```

    If you do not know the names of all LVM2 physical volumes, volume groups, or logical volumes, use the `pvdisplay`{.literal}, `vgdisplay`{.literal} or `lvdisplay`{.literal} commands.

#### [17.8.2. Using an SOS report in rescue mode](#using-an-sos-report-in-rescue-mode) {#using-an-sos-report-in-rescue-mode .title}

The `sos report`{.literal} command-line utility collects configuration and diagnostic data, including the kernel version, loaded modules, and system and service configuration files. The output is saved as a tar archive in `/var/tmp/`{.literal}. It helps analyze, troubleshoot errors, and can be captured in rescue mode.

**Prerequisites**

-   You have booted into rescue mode.
-   You have mounted the installed system `/ (root)`{.literal} partition in read-write mode.
-   You have contacted Red Hat Support about your case and received a case number.

**Procedure**

1.  Change the root directory to the `/mnt/sysroot/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2# chroot /mnt/sysroot/
    ```

2.  Run the `sos report`{.literal} command to generate an archive with system configuration and diagnostic information:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2# sos report
    ```

    `sos report`{.literal} prompts you to enter your name and the case number you received from Red Hat Support. Use only letters and numbers because adding any of the following characters or spaces could render the report unusable: `` # % & { } \ < > > * ? / $ ~ ' " : @ + ` | = ``{.literal}

3.  Optional: If you want to transfer the generated archive to a new location by using the network, it is necessary to have a network interface configured. In this scenario, use the dynamic IP addressing as no other steps are required. However, when using static addressing, enter the following command to assign an IP address (for example 10.13.153.64/23) to a network interface, for example dev eth0:

    ``` {.language-plaintext tabindex="-1"}
    bash-4.2# ip addr add 10.13.153.64/23 dev eth0
    ```

4.  Exit the chroot environment:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2# exit
    ```

5.  Store the generated archive in a new location, from where it can be easily accessible:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2# cp /mnt/sysroot/var/tmp/sos report new_location
    ```

6.  For transferring the archive through the network, use the `scp`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2# scp /mnt/sysroot/var/tmp/sos report username@hostname:sos report
    ```

    **Additional resources**

    -   [What is an sos report and how to create one in Red Hat Enterprise Linux?](https://access.redhat.com/solutions/3592)
    -   [How to generate sos report from the rescue environment](https://access.redhat.com/solutions/2872)
    -   [How do I make sos report write to an alternative location?](https://access.redhat.com/solutions/1847)
    -   [sos report fails. What data should I provide in its place?](https://access.redhat.com/solutions/68996)

#### [17.8.3. Reinstalling the GRUB2 boot loader](#reinstalling-the-grub2-boot-loader) {#reinstalling-the-grub2-boot-loader .title}

In some scenarios, the GRUB2 boot loader is mistakenly deleted, corrupted, or replaced by other operating systems. You can reinstall GRUB2 on the master boot record (MBR) on AMD64 and Intel 64 systems with BIOS.

**Prerequisites**

-   You have booted into rescue mode.
-   You have mounted the installed system `/ (root)`{.literal} partition in read-write mode.
-   You have mounted the `/boot`{.literal} mount point in read-write mode.

**Procedure**

1.  Change the root partition:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2# chroot /mnt/sysroot/
    ```

2.  Reinstall the GRUB2 boot loader, where the `install_device`{.literal} block device was installed:

    ``` {.language-plaintext tabindex="-1"}
    sh-4.2# /sbin/grub2-install install_device
    ```

    Important

    Running the `grub2-install`{.literal} command could lead to the machine being unbootable if all the following conditions apply:

    -   The system is an AMD64 or Intel 64 with Extensible Firmware Interface (EFI).
    -   Secure Boot is enabled.

    After you run the `grub2-install`{.literal} command, you cannot boot the AMD64 or Intel 64 systems that have Extensible Firmware Interface (EFI) and Secure Boot enabled. This issue occurs because the `grub2-install`{.literal} command installs an unsigned GRUB2 image that boots directly instead of using the shim application. When the system boots, the shim application validates the image signature, which when not found fails to boot the system.

3.  Reboot the system.

#### [17.8.4. Using dnf to add or remove a driver](#using-dnf-to-add-or-remove-a-driver) {#using-dnf-to-add-or-remove-a-driver .title}

You can use the `dnf`{.literal} package manager in rescue mode to add updated or missing drivers, or remove malfunctioning drivers that prevent the system from booting.

**Prerequisites**

-   You have booted into rescue mode.
-   You have mounted the installed system in read-write mode.

**Procedure**

1.  To add a new driver using `dnf`{.literal}:

    a.  Make the RPM package that contains the driver available. For example, mount a CD or USB flash drive and copy the RPM package to a location of your choice under `/mnt/sysroot/`{.literal}, for example: `/mnt/sysroot/root/drivers/`{.literal}.

    b.  Change the root directory to `/mnt/sysroot/`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        sh-4.2# chroot /mnt/sysroot/
        ```

    c.  Use the `dnf install`{.literal} command to install the driver package. For example, run the following command to install the `xorg-x11-drv-wacom`{.literal} driver package from `/root/drivers/`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        sh-4.2# dnf install /root/drivers/xorg-x11-drv-wacom-0.23.0-6.el7.x86_64.rpm
        ```

        Note

        The `/root/drivers/`{.literal} directory in this chroot environment is the `/mnt/sysroot/root/drivers/`{.literal} directory in the original rescue environment.

    d.  Exit the chroot environment:

        ``` {.language-plaintext tabindex="-1"}
        sh-4.2# exit
        ```

2.  To remove a driver by using `dnf`{.literal}:

    a.  Change the root directory to the `/mnt/sysroot/`{.literal} directory:

        ``` {.language-plaintext tabindex="-1"}
        sh-4.2# chroot /mnt/sysroot/
        ```

    b.  Use the `dnf remove`{.literal} command to remove the driver package. For example, to remove the `xorg-x11-drv-wacom`{.literal} driver package, run:

        ``` {.language-plaintext tabindex="-1"}
        sh-4.2# dnf remove xorg-x11-drv-wacom
        ```

    c.  Exit the chroot environment:

        ``` {.language-plaintext tabindex="-1"}
        sh-4.2# exit
        ```

        If you cannot remove a malfunctioning driver for some reason, you can instead blocklist the driver so that it does not load at boot time.

    d.  After you remove the drivers, reboot the system.

        Warning

        When you install a driver from a driver disk, the driver disk updates all `initramfs`{.literal} images on the system to use this driver. If a problem with a driver prevents a system from booting, you cannot rely on booting the system from another `initramfs`{.literal} image.

### [17.9. ip= boot option returns an error](#ip-boot-option-returns-an-error) {#ip-boot-option-returns-an-error .title}

Using the `ip=`{.literal} boot option format `ip=[ip address]`{.literal} for example, `ip=192.168.1.1`{.literal} returns the error message `Fatal for argument 'ip=[insert ip here]'\n sorry, unknown value [ip address] refusing to continue`{.literal}.

In previous releases of Red Hat Enterprise Linux, the boot option format was:

``` {.language-plaintext tabindex="-1"}
ip=192.168.1.15 netmask=255.255.255.0 gateway=192.168.1.254 nameserver=192.168.1.250 hostname=myhost1
```

However, in Red Hat Enterprise Linux 10, the boot option format is:

``` {.language-plaintext tabindex="-1"}
ip=192.168.1.15::192.168.1.254:255.255.255.0:myhost1::none: nameserver=192.168.1.250
```

To resolve the issue, use the format: `ip=ip::gateway:netmask:hostname:interface:none`{.literal} where:

-   `ip`{.literal} specifies the client ip address. You can specify IPv6 addresses in square brackets, for example, `[2001:DB8::1]`{.literal}.
-   `gateway`{.literal} is the default gateway. IPv6 addresses are also accepted.
-   `netmask`{.literal} is the netmask to be used. This can be either a full netmask, for example, 255.255.255.0, or a prefix, for example, `64`{.literal}.
-   `hostname`{.literal} is the host name of the client system. This parameter is optional.

**Additional resources**

-   [Network boot options](#network-boot-options "18.2. Network boot options")

### [17.10. Troubleshooting graphical installation on iLO or iDRAC devices](#troubleshooting-graphical-installation-on-ilo-or-idrac-devices) {#troubleshooting-graphical-installation-on-ilo-or-idrac-devices .title}

The graphical installer for a remote ISO installation on Integrated Lights-Out (iLO) or Integrated Dell Remote Access Controller (iDRAC) devices may not be available due to a slow internet connection. To proceed with the installation, choose a suitable method.

**Procedure**

1.  Avoid the timeout. To do this:

    a.  Press the Tab key in case of BIOS usage, or the e key in case of UEFI usage when booting from an installation media. This allows you to modify the kernel command line arguments.

    b.  To proceed with the installation, append the `rd.live.ram=1`{.literal} and press Enter in case of BIOS usage, or Ctrl+x in case of UEFI usage.

        This might take longer to load the installation program.

2.  Another option to extend the loading time for the graphical installer is to set the `inst.xtimeout`{.literal} kernel argument in seconds.

    ``` {.language-plaintext tabindex="-1"}
    inst.xtimeout=N
    ```

3.  You can install the system in text mode. For more details, see [Installing RHEL in text mode](https://access.redhat.com/articles/4323781).

4.  In the remote management console, such as iLO or iDRAC, use the direct URL to the installation ISO file instead of a local media source. Get the ISO file from the [Download center](https://access.redhat.com/downloads) on the Red Hat Customer Portal. You must be logged in to access this section.

### [17.11. Rootfs image is not initramfs](#rootfs-image-is-not-initramfs) {#rootfs-image-is-not-initramfs .title}

You might get the following message on the console during booting the installer, the transfer of the installer `initrd.img`{.literal} might have had errors.

``` {.language-plaintext tabindex="-1"}
[ ...] rootfs image is not initramfs
```

To resolve this issue, download `initrd`{.literal} again or run the `sha256sum`{.literal} with `initrd.img`{.literal} and compare it with the checksum stored in the `.treeinfo`{.literal} file on the installation medium, for example,

``` {.language-plaintext tabindex="-1"}
$ sha256sum dvd/images/pxeboot/initrd.img
```

``` {.language-plaintext tabindex="-1"}
fdb1a70321c06e25a1ed6bf3d8779371b768d5972078eb72b2c78c925067b5d8 dvd/images/pxeboot/initrd.img
```

To view the checksum in `.treeinfo`{.literal}:

``` {.language-plaintext tabindex="-1"}
$ grep sha256 dvd/.treeinfo
```

``` {.language-plaintext tabindex="-1"}
images/efiboot.img = sha256:d357d5063b96226d643c41c9025529554a422acb43a4394e4ebcaa779cc7a917
images/install.img = sha256:8c0323572f7fc04e34dd81c97d008a2ddfc2cfc525aef8c31459e21bf3397514
images/pxeboot/initrd.img = sha256:fdb1a70321c06e25a1ed6bf3d8779371b768d5972078eb72b2c78c925067b5d8
images/pxeboot/vmlinuz = sha256:b9510ea4212220e85351cbb7f2ebc2b1b0804a6d40ccb93307c165e16d1095db
```

Even with the correct `initrd.img`{.literal}, you might see the following kernel messages during installer boot. This issue often occurs when a boot parameter is missing or misspelled, preventing the installer from loading stage2. The stage2 image is typically specified by the `inst.repo=`{.literal} parameter and provides the full installer initial ramdisk for the in-memory root file system:

``` {.language-plaintext tabindex="-1"}
[ ...] No file system could mount root, tried:
[ ...] Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(1,0)
[ ...] CPU: 0 PID: 1 Comm: swapper/0 Not tainted 6.12.0.el10_0.s390x #1
[ ...] ...
[ ...] Call Trace:
[ ...] ([<...>] show_trace+0x.../0x...)
[ ...]  [<...>] show_stack+0x.../0x...
[ ...]  [<...>] panic+0x.../0x...
[ ...]  [<...>] mount_block_root+0x.../0x...
[ ...]  [<...>] prepare_namespace+0x.../0x...
[ ...]  [<...>] kernel_init_freeable+0x.../0x...
[ ...]  [<...>] kernel_init+0x.../0x...
[ ...]  [<...>] kernel_thread_starter+0x.../0x...
[ ...]  [<...>] kernel_thread_starter+0x.../0x…
```

To resolve this issue, check

-   if the installation source specified is correct on the kernel command line (`inst.repo=`{.literal}) or in the kickstart file
-   the network configuration is specified on the kernel command line (if the installation source is specified as network)
-   the network installation source is accessible from another system

## [Chapter 18. Boot options reference](#boot-options-reference) {#chapter-18.-boot-options-reference .title}

You can use the boot options to modify the default behavior of the installation program.

### [18.1. Installation source boot options](#installation-source-boot-options) {#installation-source-boot-options .title}

You can configure installation source boot options to specify where RHEL installation files are located. These options enable installations from various sources including local media, network servers, and additional repositories, providing flexibility in deployment scenarios.

inst.repo=

:   The `inst.repo=`{.literal} boot option specifies the installation source, that is, the location providing the package repositories and a valid `.treeinfo`{.literal} file that describes them. For example: `inst.repo=cdrom`{.literal}. The target of the `inst.repo=`{.literal} option must be one of the following installation media:

    -   an installable tree, which is a directory structure containing the installation program images, packages, and repository data as well as a valid `.treeinfo`{.literal} file

    -   a DVD (a physical disk present in the system DVD drive)

    -   an ISO image of the full Red Hat Enterprise Linux installation DVD, placed on a disk or a network location accessible to the system.

        Use the `inst.repo=`{.literal} boot option to configure different installation methods by using different formats. The following table contains details of the `inst.repo=`{.literal} boot option syntax:

        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Source type                                                                                                                                                                                                                                | Boot option format                                                                                                                                          | Source format                                                                                                                                                                  |
        +:===========================================================================================================================================================================================================================================+:============================================================================================================================================================+:===============================================================================================================================================================================+
        | CD/DVD drive                                                                                                                                                                                                                               | `inst.repo=cdrom:`{.literal}*`<device>`{.literal}*                                                                                                          | Installation DVD as a physical disk. [^\[a\]^](#ftn.idm140363038621328)                                                                                                        |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Mountable device (HDD and USB stick)                                                                                                                                                                                                       | `inst.repo=hd:`{.literal}*`<device>`{.literal}*`:/`{.literal}*`<path>`{.literal}*                                                                           | Image file of the installation DVD.                                                                                                                                            |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NFS Server                                                                                                                                                                                                                                 | `inst.repo=nfs:[`{.literal}*`options`{.literal}*`:]`{.literal}*`<server>`{.literal}*`:/`{.literal}*`<path>`{.literal}*                                      | Image file of the installation DVD, or an installation tree, which is a complete copy of the directories and files on the installation DVD. [^\[b\]^](#ftn.idm140363038606128) |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | HTTP Server                                                                                                                                                                                                                                | `inst.repo=http://`{.literal}*`<host>`{.literal}*`/`{.literal}*`<path>`{.literal}*                                                                          | Installation tree that is a complete copy of the directories and files on the installation DVD.                                                                                |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | HTTPS Server                                                                                                                                                                                                                               | `inst.repo=https://`{.literal}*`<host>`{.literal}*`/`{.literal}*`<path>`{.literal}*                                                                         |                                                                                                                                                                                |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | FTP Server                                                                                                                                                                                                                                 | `inst.repo=ftp://`{.literal}*`<username>`{.literal}*`:`{.literal}*`<password>`{.literal}*`@`{.literal}*`<host>`{.literal}*`/`{.literal}*`<path>`{.literal}* |                                                                                                                                                                                |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | HMC                                                                                                                                                                                                                                        | `inst.repo=hmc`{.literal}                                                                                                                                   |                                                                                                                                                                                |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | [^\[a\]^](#idm140363038621328) If *device* is left out, installation program automatically searches for a drive containing the installation DVD.                                                                                           |                                                                                                                                                             |                                                                                                                                                                                |
        |                                                                                                                                                                                                                                            |                                                                                                                                                             |                                                                                                                                                                                |
        | [^\[b\]^](#idm140363038606128) The NFS Server option uses NFS protocol version 3 by default. To use a different version, add `nfsvers=`{.literal}*`X`{.literal}* to *options*, replacing *X* with the version number that you want to use. |                                                                                                                                                             |                                                                                                                                                                                |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        : Table 18.1. Types and format for the inst.repo= boot option and installation source

        Show more

Set disk device names with the following formats:

-   Kernel device name, for example `/dev/sda1`{.literal} or `sdb2`{.literal}

-   File system label, for example `LABEL=Flash`{.literal} or `LABEL=RHEL8`{.literal}

-   File system UUID, for example `UUID=8176c7bf-04ff-403a-a832-9557f94e61db`{.literal}

    Non-alphanumeric characters must be represented as `\xNN`{.literal}, where *NN* is the hexadecimal representation of the character. For example, `\x20`{.literal} is a white space `(" ")`{.literal}.

    inst.addrepo=

    :   Use the `inst.addrepo=`{.literal} boot option to add an additional repository that you can use as another installation source along with the main repository (`inst.repo=`{.literal}). You can use the `inst.addrepo=`{.literal} boot option multiple times during one boot. The following table contains details of the `inst.addrepo=`{.literal} boot option syntax.

        Note

        The `REPO_NAME`{.literal} is the name of the repository and is required in the installation process. These repositories are only used during the installation process; they are not installed on the installed system.

        +--------------------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Installation source                              | Boot option format                                                                                          | Additional information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
        +:=================================================+:============================================================================================================+:=====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | Installable tree at a URL                        | `inst.addrepo=REPO_NAME,[http,https,ftp]://`{.literal}*`<host>`{.literal}*`/`{.literal}*`<path>`{.literal}* | Looks for the installable tree at a given URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
        +--------------------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Installable tree at an NFS path                  | `inst.addrepo=REPO_NAME,nfs://`{.literal}*`<server>`{.literal}*`:/`{.literal}*`<path>`{.literal}*           | Looks for the installable tree at a given NFS path. A colon is required after the host. The installation program passes everything after `nfs://`{.literal} directly to the mount command instead of parsing URLs according to RFC 2224.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
        +--------------------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Installable tree in the installation environment | `inst.addrepo=REPO_NAME,file://`{.literal}*`<path>`{.literal}*                                              | Looks for the installable tree at the given location in the installation environment. To use this option, the repository must be mounted before the installation program attempts to load the available software groups. The benefit of this option is that you can have multiple repositories on one bootable ISO, and you can install both the main repository and additional repositories from the ISO. The path to the additional repositories is `/run/install/source/REPO_ISO_PATH`{.literal}. Additionally, you can mount the repository directory in the `%pre`{.literal} section in the Kickstart file. The path must be absolute and start with `/`{.literal}, for example `inst.addrepo=REPO_NAME,file:///`{.literal}*`<path>`{.literal}* |
        +--------------------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Disk                                             | `inst.addrepo=REPO_NAME,hd:`{.literal}*`<device>`{.literal}*`:`{.literal}*`<path>`{.literal}*               | Mounts the given *\<device\>* partition and installs from the ISO that is specified by the *\<path\>*. If the *\<path\>* is not specified, the installation program looks for a valid installation ISO on the *\<device\>*. This installation method requires an ISO with a valid installable tree.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
        +--------------------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        : Table 18.2. Installation sources and boot option format

        Show more

    inst.stage2=

    :   The `inst.stage2=`{.literal} boot option specifies the location of the installation program's runtime image. This option expects the path to a directory that contains a valid `.treeinfo`{.literal} file and reads the runtime image location from the `.treeinfo`{.literal} file. If the `.treeinfo`{.literal} file is not available, the installation program attempts to load the image from `images/install.img`{.literal}.

        When you do not specify the `inst.stage2`{.literal} option, the installation program attempts to use the location specified with the `inst.repo`{.literal} option.

        You can use this option when you want to manually specify the installation source in the installation program at a later time. For example, when you want to select the Content Delivery Network (CDN) as an installation source. The installation DVD and Boot ISO already contain a suitable `inst.stage2`{.literal} option to boot the installation program from the respective ISO.

        If you want to specify an installation source, use the `inst.repo=`{.literal} option instead.

        Note

        By default, the `inst.stage2=`{.literal} boot option is used on the installation media and is set to a specific label. For example, `inst.stage2=hd:LABEL=RHEL-x-0-0-BaseOS-x86_64`{.literal}. If you modify the default label of the runtime image file system, verify that the `inst.stage2=`{.literal} boot option is set correctly. Also verify it when using a customized installation boot procedure.

    inst.noverifyssl

    :   Use the `inst.noverifyssl`{.literal} boot option to prevent the installer from verifying SSL certificates for HTTPS connections. For additional Kickstart repositories, you can set `--noverifyssl`{.literal} separately for each repository.

        For example, the `inst.noverifyssl`{.literal} boot option enables the installer to complete the installation without verifying the SSL certificates when remote installation source is using self-signed SSL certificates. For example, when specifying the source by using `inst.stage2=`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        inst.stage2=https://hostname/path_to_install_image/ inst.noverifyssl
        ```

        And for example when specifying the source by using `inst.repo=`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        inst.repo=https://hostname/path_to_install_repository/ inst.noverifyssl
        ```

    inst.stage2.all

    :   Use the `inst.stage2.all`{.literal} boot option to specify several HTTP, HTTPS, or FTP sources. You can use the `inst.stage2=`{.literal} boot option multiple times with the `inst.stage2.all`{.literal} option to fetch the image from the sources sequentially until one succeeds. For example:

        ``` {.language-plaintext tabindex="-1"}
        inst.stage2.all
        inst.stage2=http://hostname1/path_to_install_tree/
        inst.stage2=http://hostname2/path_to_install_tree/
        inst.stage2=http://hostname3/path_to_install_tree/
        ```

    inst.dd=
    :   The `inst.dd=`{.literal} boot option is used to perform a driver update during the installation.

    inst.repo=hmc

    :   This option eliminates the requirement of an external network configuration and expands the installation options. When booting from a Binary DVD, the installation program prompts you to enter additional kernel parameters. To set the DVD as an installation source, append the `inst.repo=hmc`{.literal} option to the kernel parameters. The installation program then enables support element (SE) and hardware management console (HMC) file access. It also fetches the images for stage2 from the DVD. It provides access to the packages on the DVD for software selection.

        Important

        To use the `inst.repo`{.literal} boot option, ensure the user is configured with a **minimum of Privilege Class B**.

    inst.proxy=

    :   This boot option is used when performing an installation from a HTTP, HTTPS, and FTP protocol in the following form:

        ``` {.language-plaintext tabindex="-1"}
        [PROTOCOL://][USERNAME[:PASSWORD]@]HOST[:PORT]
        For example:
        http://proxyuser:proxypassword@10.1.2.3:3128
        ```

    inst.nosave=

    :   Use the `inst.nosave=`{.literal} boot option to control the installation logs and related files that are not saved to the installed system. For example `input_ks`{.literal}, `output_ks`{.literal}, `all_ks`{.literal}, `logs`{.literal} and `all`{.literal}. You can combine multiple values separated by a comma. For example,

        ``` {.language-plaintext tabindex="-1"}
        inst.nosave=input_ks,logs
        ```

    Note

    The `inst.nosave`{.literal} boot option is used for excluding files from the installed system that cannot be removed by a Kickstart %post script, such as logs and input/output Kickstart results.

    `input_ks`{.literal}
    :   Disables the ability to save the input Kickstart results.

    `output_ks`{.literal}
    :   Disables the ability to save the output Kickstart results generated by the installation program.

    `all_ks`{.literal}
    :   Disables the ability to save the input and output Kickstart results.

    `logs`{.literal}
    :   Disables the ability to save all installation logs.

    `all`{.literal}
    :   Disables the ability to save all Kickstart results, and all logs.

    inst.multilib
    :   Use the `inst.multilib`{.literal} boot option to set DNF's `multilib_policy`{.literal} to **all**, instead of **best**.

    inst.memcheck
    :   The `inst.memcheck`{.literal} boot option performs a check to verify that the system has enough RAM to complete the installation. If there is not enough RAM, the installation process is stopped. The system check is approximate and memory usage during installation depends on the package selection, user interface, for example graphical or text, and other parameters.

    inst.nomemcheck
    :   The `inst.nomemcheck`{.literal} boot option does not perform a check to verify if the system has enough RAM to complete the installation. Any attempt to perform the installation with less than the minimum amount of memory is unsupported, and might result in the installation process failing.

**Additional resources**

-   [*Updating drivers during installation*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/index#updating-drivers-during-installation)
-   [*User Privilege Class B - IBM documentation*](https://www.ibm.com/docs/en/zvm/7.2?topic=privilege-zvm)

### [18.2. Network boot options](#network-boot-options) {#network-boot-options .title}

You can configure network boot options to enable RHEL installation over network connections. With these options, configure network interfaces, specify IP addresses, configure bonding, bridging, and VLANs for network-based installations and remote system deployment.

Note

Initialize the network with the `dracut`{.literal} tool. For a complete list of `dracut`{.literal} options, see the `dracut.cmdline(7)`{.literal} man page on your system.

ip=

:   Use the `ip=`{.literal} boot option to configure one or more network interfaces. To configure multiple interfaces, use one of the following methods

    -   use the `ip`{.literal} option multiple times, once for each interface; to do so, use the `rd.neednet=1`{.literal} option, and specify a primary boot interface using the `bootdev`{.literal} option.

    -   use the `ip`{.literal} option once, and then use Kickstart to configure further interfaces. While `ip=`{.literal} configuration applies early in the installation process, Kickstart configuration applies later, after the installation program starts.

        This option accepts several different formats. The following tables contain information about the most common options. In the following tables:

    -   The `ip`{.literal} parameter specifies the client IP address and `IPv6`{.literal} requires square brackets, for example 192.0.2.1 or \[2001:db8::99\].

    -   The `gateway`{.literal} parameter is the default gateway. `IPv6`{.literal} requires square brackets.

    -   The `netmask`{.literal} parameter is the netmask to be used. This can be either a full netmask (for example, 255.255.255.0) or a prefix (for example, 64).

    -   The `hostname`{.literal} parameter is the host name of the client system. This parameter is optional.

        +--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
        | Boot option format                                                                   | Configuration method                                                                                                        |
        +:=====================================================================================+:============================================================================================================================+
        | `ip=`{.literal}*`method`{.literal}*                                                  | Automatic configuration of all interfaces.                                                                                  |
        +--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
        | `ip=`{.literal}*`interface:method`{.literal}*                                        | Automatic configuration of a specific interface                                                                             |
        +--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
        | `ip=`{.literal}*`ip::gateway:netmask:hostname:interface`{.literal}*`:none`{.literal} | Static configuration, for example, IPv4: `ip=192.0.2.1::192.0.2.254:255.255.255.0:server.example.com:enp1s0:none`{.literal} |
        |                                                                                      |                                                                                                                             |
        |                                                                                      | IPv6: `ip=[2001:db8::1]::[2001:db8::fffe]:64:server.example.com:enp1s0:none`{.literal}                                      |
        +--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
        | `ip=`{.literal}*`ip::gateway:netmask:hostname:interface:method:mtu`{.literal}*       | Automatic configuration of a specific interface with an override                                                            |
        +--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

        : Table 18.3. Boot option formats to configure the network interface

        Show more

Configuration methods for the automatic interface

:   The method `automatic configuration of a specific interface with an override`{.literal} opens the interface using automatic configuration such as `dhcp`{.literal}. It then overrides parameters like IP address, gateway, netmask, host name, or other settings. All parameters are optional, so specify only the parameters that you want to override. For the values of the `method`{.literal} parameter, see the `dracut.cmdline(7)`{.literal} man page on your system.

    Note

    -   If you use a boot option that requires network access, such as `inst.ks=http://host/path`{.literal}, without specifying the `ip`{.literal} option, the default value of the `ip`{.literal} option is `ip=dhcp`{.literal}..
    -   To connect to an iSCSI target automatically, activate a network device for accessing the target by using the `ip=ibft`{.literal} boot option.

    -   `nameserver=`{.literal} - The `nameserver=`{.literal} option specifies the address of the name server. You can use this option multiple times.

        Note

        The `ip=`{.literal} parameter requires square brackets. However, an IPv6 address does not work with square brackets. An example of the correct syntax to use for an IPv6 address is `nameserver=2001:db8::1`{.literal}.

    -   `bootdev=`{.literal} - The `bootdev=`{.literal} option specifies the boot interface. This option is mandatory if you use more than one `ip`{.literal} option.

    -   `ifname=`{.literal} - The `ifname=`{.literal} options assigns an interface name to a network device with a given MAC address. You can use this option multiple times. The syntax is `ifname=interface:MAC`{.literal}. For example:

        ``` {.language-plaintext tabindex="-1"}
        ifname=eth0:01:23:45:67:89:ab
        ```

        Note

        The `ifname=`{.literal} option is the only supported way to set custom network interface names during installation.

    -   `inst.dhcpclass=`{.literal} - The `inst.dhcpclass=`{.literal} option specifies the DHCP vendor class identifier. The `dhcpd`{.literal} service recognizes this value as `vendor-class-identifier`{.literal}. The default value is `anaconda-$(uname -srm)`{.literal}. To ensure the `inst.dhcpclass=`{.literal} option is applied correctly, request network activation during the early stage of installation by also adding the `ip`{.literal} option.

    -   `inst.waitfornet=`{.literal} - Using the `inst.waitfornet=SECONDS`{.literal} boot option causes the installation system to wait for network connectivity before installation. The value in the `SECONDS`{.literal} argument specifies the maximum wait time for network connectivity. After the timeout, the installation process continues even if network connectivity is unavailable.

    -   `vlan=`{.literal}- Use the `vlan=`{.literal} option to configure a Virtual LAN (VLAN) device on a specified interface with a given name. The syntax is `vlan=name:interface`{.literal}. For example:

        ``` {.language-plaintext tabindex="-1"}
        vlan=vlan5:enp0s1
        ```

        This configures a VLAN device named `vlan5`{.literal} on the `enp0s1`{.literal} interface. The name can take the following forms:

        -   VLAN_PLUS_VID: `vlan0005`{.literal}
        -   VLAN_PLUS_VID_NO_PAD: `vlan5`{.literal}
        -   DEV_PLUS_VID: `enp0s1.0005`{.literal}
        -   DEV_PLUS_VID_NO_PAD: `enp0s1.5`{.literal}

    -   `bond=`{.literal} - Use the `bond=`{.literal} option to configure a bonding device with the following syntax: `bond=name[:interfaces][:options]`{.literal}. Replace *name* with the bonding device name, *interfaces* with a comma-separated list of physical (Ethernet) interfaces, and *options* with a comma-separated list of bonding options. For example:

        ``` {.language-plaintext tabindex="-1"}
        bond=bond0:enp0s1,enp0s2:mode=active-backup,tx_queues=32,downdelay=5000
        ```

        For a list of available options, run the `modinfo bonding`{.literal} command.

    -   `bridge=`{.literal} - Use the `bridge=`{.literal} option to configure a bridge device with the following syntax: `bridge=name:interfaces`{.literal}. Replace *name* with the name of the bridge device that you want and *interfaces* with a comma-separated list of physical (Ethernet) devices to be used as underlying interfaces in the bridge device. For example:

        ``` {.language-plaintext tabindex="-1"}
        bridge=bridge0:enp0s1,enp0s2
        ```

**Additional resources**

-   [Configuring and managing networking](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_networking/index/)

### [18.3. Console boot options](#console-boot-options) {#console-boot-options .title}

You can configure boot options for your console, monitor display, and keyboard to customize the installation process.

console=
:   Use the `console=`{.literal} option to specify a device that you want to use as the primary console. For example, to use a console on the first serial port, use `console=ttyS0`{.literal}. When using the `console=`{.literal} argument, the installation starts with a text UI. If you must use the `console=`{.literal} option multiple times, the boot message is displayed on all specified consoles. However, the installation program uses only the last specified console. For example, if you specify `console=ttyS0 console=ttyS1`{.literal}, the installation program uses `ttyS1`{.literal}.

inst.lang=
:   Use the `inst.lang=`{.literal} option to set the language that you want to use during the installation. To view the list of locales, enter the command `locale -a | grep _`{.literal} or the `localectl list-locales | grep _`{.literal} command.

inst.geoloc=

:   Use the `inst.geoloc=`{.literal} option to configure geolocation usage in the installation program. Geolocation is used to preset the language and time zone, and uses the following syntax: `inst.geoloc=value`{.literal}. The `value`{.literal} can be any of the following parameters:

    -   Disable geolocation: `inst.geoloc=0`{.literal}
    -   Use the Fedora GeoIP API: `inst.geoloc=provider_fedora_geoip`{.literal}. This option is deprecated.
    -   Use the Hostip.info GeoIP API: `inst.geoloc=provider_hostip`{.literal}. This option is deprecated.

inst.keymap=
:   Use the `inst.keymap=`{.literal} option to specify the keyboard layout to use for the installation.

inst.cmdline
:   Use the `inst.cmdline`{.literal} option to force the installation program to run in command-line mode. This mode does not allow any interaction, and you must specify all options in a Kickstart file or on the command line.

inst.graphical
:   Use the `inst.graphical`{.literal} option to force the installation program to run in graphical mode. The graphical mode is the default.

inst.text
:   Use the `inst.text`{.literal} option to force the installation program to run in text mode instead of graphical mode.

inst.noninteractive
:   Use the `inst.noninteractive`{.literal} boot option to run the installation program in a non-interactive mode. User interaction is not permitted in the non-interactive mode, and `inst.noninteractive`{.literal} you can use the `inst.nointeractive`{.literal} option with a graphical or text installation. When you use the `inst.noninteractive`{.literal} option in text mode, it behaves the same as the `inst.cmdline`{.literal} option.

Note

It only makes sense to use the `inst.noninteractive`{.literal} option when performing a Kickstart installation.

inst.resolution=
:   Use the `inst.resolution=`{.literal} option to specify the screen resolution in graphical mode. The format is `NxM`{.literal}, where *N* is the screen width and *M* is the screen height (in pixels). The recommended resolution is 1024x768.

inst.rdp
:   Use the `inst.rdp`{.literal} option to run the graphical installation by using Remote Desktop Protocol (RDP). To set an RDP username and password, use the `inst.rdp.username=`{.literal} and `inst.rdp.password=`{.literal} options together with the `inst.rdp`{.literal} option. If you do not specify the username or password, the installation program prompts you to provide them interactively.

inst.rdp.username=
:   Use the `inst.rdp.username=`{.literal} option to set the username for the RDP session. This option only applies when used together with the `inst.rdp`{.literal} option.

inst.rdp.password=
:   Use the `inst.rdp.password=`{.literal} option to set the password for the RDP session. This option only applies when used together with the `inst.rdp`{.literal} option.

modprobe.blacklist=

:   Use the `modprobe.blacklist=`{.literal} option to blocklist or completely disable one or more drivers. Drivers (modules) that you disable using this option cannot load when the installation starts. After the installation finishes, the installed system retains these settings. You can find a list of the blocklisted drivers in the `/etc/modprobe.d/`{.literal} directory. Use a comma-separated list to disable multiple drivers. For example:

    ``` {.language-plaintext tabindex="-1"}
    modprobe.blacklist=ahci,firewire_ohci
    ```

    Note

    You can use `modprobe.blacklist`{.literal} in combination with the different command line options. For example, use it with the `inst.dd`{.literal} option to ensure that an updated version of an existing driver is loaded from a driver update disc:

    ``` {.language-plaintext tabindex="-1"}
    modprobe.blacklist=virtio_blk
    ```

inst.sshd

:   Use the `inst.sshd`{.literal} option to start the `sshd`{.literal} service during installation. This enables you to connect to the system during the installation by using SSH and monitor the installation progress. For more information about SSH, see the `ssh(1)`{.literal} man page on your system. By default, the `sshd`{.literal} service is automatically started only on the 64-bit IBM Z architecture. On other architectures, `sshd`{.literal} is not started unless you use the `inst.sshd`{.literal} option.

    Note

    During installation, the root account has no password by default. You can set a root password during installation with the `sshpw`{.literal} Kickstart command.

inst.kdump_addon=
:   Use the `inst.kdump_addon=`{.literal} option to enable or disable the Kdump configuration screen (add-on) in the installation program. This screen is enabled by default; use `inst.kdump_addon=off`{.literal} to disable it. Disabling the add-on disables the Kdump screens in both the graphical and text-based interface as well as the `%addon com_redhat_kdump`{.literal} Kickstart command.

### [18.4. Debug boot options](#debug-boot-options) {#debug-boot-options .title}

You can use several options when debugging issues to troubleshoot and fix issues.

inst.rescue
:   Use the `inst.rescue`{.literal} option to run the rescue environment for diagnosing and fixing systems.

inst.updates=

:   Use the `inst.updates=`{.literal} option to specify the location of the `updates.img`{.literal} file that you want to apply during installation. The `updates.img`{.literal} file can be derived from one of several sources.

    +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Source                            | Description                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                                                                                       |
    +:==================================+:========================================================================================================================================================================================================================================+:==============================================================================================================================================================================================================================================================================================================================+
    | Updates from a network            | Specify the network location of `updates.img`{.literal}. This does not require any modification to the installation tree. To use this method, edit the kernel command line to include `inst.updates`{.literal}.                         | `inst.updates=http://website.com/path/to/updates.img`{.literal}.                                                                                                                                                                                                                                                              |
    +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Updates from a disk image         | Save an `updates.img`{.literal} on a USB key.                                                                                                                                                                                           | `inst.updates=sda1:/images/updates.img`{.literal} for an updates image located in the `images`{.literal} directory on the `sda1`{.literal} device or `inst.updates=UUID=b4234403-dafb-44c1-b878-4d57b40c9843:/updates.img`{.literal} for an update image located in the root directory of a partition identified by its UUID. |
    +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Updates from an installation tree | If you are using a CD, disk, HTTP, HTTPS, or FTP installation, save the `updates.img`{.literal} in the installation tree so that all installations can detect the `.img`{.literal} file. The file name must be `updates.img`{.literal}. | For NFS installs, save the file in the `images/`{.literal} directory, or in the `RHupdates/`{.literal} directory.                                                                                                                                                                                                             |
    +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    : Table 18.4. updates.img file sources

    Show more

inst.syslog=
:   Sends log messages to the `syslog`{.literal} process on the specified host when the installation starts. You can use `inst.syslog=<host>[:port]`{.literal} only if the remote `syslog`{.literal} process is configured to accept incoming connections.

inst.virtiolog=
:   Use the `inst.virtiolog=<name>`{.literal} option to specify which virtio port (a character device at `/dev/virtio-ports/<name>`{.literal}) to use for forwarding logs. The default value is `org.fedoraproject.anaconda.log.0`{.literal}.

rd.live.ram
:   Copies the stage 2 image in `images/install.img`{.literal} into RAM. This increases the memory required for installation by the size of the image that might result in an additional requirement of approximately 1 GiB of RAM or more.

inst.nokill
:   Prevent the installation program from rebooting when a fatal error occurs, or at the end of the installation process. Use it capture installation logs which would be otherwise lost upon reboot.

inst.noshell
:   Prevent a shell on terminal session 2 (tty2) including tmux window 2, during installation.

inst.notmux
:   Prevent the use of tmux during installation. The output is generated without the terminal control characters and is meant for non-interactive uses.

**Additional resources**

-   [Repair a filesystem in rescue mode (Red Hat Knowledgebase)](https://access.redhat.com/solutions/9541)

### [18.5. Storage boot options](#storage-boot-options) {#storage-boot-options .title}

You can specify the following options to customize booting from a storage device.

inst.nompath

:   Disables support for multipath devices. Use this option only if your system has a false-positive that incorrectly identifies a normal block device as a multipath device.

    Warning

    Use this option with caution. Do not use this option with multipath hardware. Using this option to install to a single path of a multipath device is not supported.

inst.gpt
:   Prefer creation of GPT disk labels. This option is deprecated and will be removed in future releases. Use `inst.disklabel=gpt`{.literal} instead.

inst.disklabel=
:   Prefer creation of the specified disk label type. Specify `gpt`{.literal} to prefer creation of GPT disk labels (default). Specify `mbr`{.literal} to prefer creation of MBR disk labels if supported.

inst.wait_for_disks=
:   Use the `inst.wait_for_disks=`{.literal} option to specify the number of seconds installation program to wait for disk devices to appear at the beginning of the installation. Use this option when you use the `OEMDRV-labeled`{.literal} device to automatically load the Kickstart file or the kernel drivers but the device takes a longer time to appear during the boot process. By default, the installation program waits for `5`{.literal} seconds. Use `0`{.literal} seconds to minimize the delay.

inst.nonibftiscsiboot
:   The `inst.nonibftiscsiboot`{.literal} option enables placement of the boot loader on `iSCSI`{.literal} devices that are not configured through the `iSCSI`{.literal} boot firmware table (`iBFT`{.literal}).

## [Legal Notice](#idm140363049890944) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
