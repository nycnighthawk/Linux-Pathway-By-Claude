---
{"title": "Automatically installing RHEL", "guide": "automatically_installing_rhel", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/automatically_installing_rhel/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Automatically installing RHEL {#automatically-installing-rhel .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Deploying RHEL on one or more systems from a predefined configuration {#deploying-rhel-on-one-or-more-systems-from-a-predefined-configuration .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139687890991456)

**Abstract**

You can automate the RHEL installation by using Kickstart. Use this method to deploy the same RHEL configuration on many systems. Kickstart installs RHEL based on the parameters that you specify in a configuration file. The installation source can be an installation media, an ISO file, the Red Hat content delivery network (CDN), or a server in your local network.

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

## [Chapter 5. Preparing network-based repositories](#preparing-network-based-repositories) {#chapter-5.-preparing-network-based-repositories .title}

You must prepare repositories to install RHEL from your network system.

### [5.1. Creating an installation source on an NFS server](#creating-an-installation-source-on-an-nfs-server) {#creating-an-installation-source-on-an-nfs-server .title}

You can configure an NFS server to host RHEL installation files for network-based installations. It enables multiple systems to install from a shared network location, providing efficient deployment across your infrastructure without requiring physical media for each system.

**Prerequisites**

-   You have administrator-level access to a server with Red Hat Enterprise Linux 10, and this server is on the same network as the system to be installed.
-   You have downloaded the full installation DVD ISO from the [Product Downloads](https://access.redhat.com/downloads/content/rhel) page.

Important

Ensure that you use different paths in `inst.ks`{.literal} and `inst.repo`{.literal}. When using NFS to host the installation source, you cannot use the same nfs share to host the Kickstart.

**Procedure**

1.  Install the `nfs-utils`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install nfs-utils
    ```

2.  Copy the DVD ISO image to a directory on the NFS server. This example assumes the DVD ISO is copied to the `/nfs/rhel10-install/`{.literal} directory on the NFS server.

3.  Open the `/etc/exports`{.literal} file using a text editor and add a line with the following syntax:

    ``` {.language-plaintext tabindex="-1"}
    /exported_directory/ clients
    ```

    -   Replace */exported_directory/* with the full path to the directory with the ISO image.

    -   Replace *clients* with one of the following:

        -   The host name or IP address of the target system
        -   The subnetwork that all target systems can use to access the ISO image
        -   To allow any system with network access to the NFS server to use the ISO image, the asterisk sign (`*`{.literal})

        See the `exports(5)`{.literal} man page for detailed information about the format of this field.

        For example, a basic configuration that makes the `/nfs/rhel10-install/`{.literal} directory available as read-only to all clients is:

        ``` {.language-plaintext tabindex="-1"}
        /nfs/rhel10-install *
        ```

4.  Save the `/etc/exports`{.literal} file and exit the text editor.

5.  Enable the NFS service in firewalld:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service nfs
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=mountd
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=rpc-bind
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

6.  Start the nfs service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now nfs-server.service
    ```

    If the service was running before you changed the `/etc/exports`{.literal} file, reload the NFS server configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload nfs-server.service
    ```

    The ISO image is now accessible over NFS and ready to be used as an installation source.

    When configuring the installation source, use `nfs:`{.literal} as the protocol, the server host name or IP address, the colon sign `(:)`{.literal}, and the directory holding the ISO image. For example, if the server host name is `myserver.example.com`{.literal} and you have saved the ISO image in `/nfs/rhel10-install/`{.literal}:

    -   On kernel command line, define the NFS installation source as `inst.repo=nfs:myserver.example.com:/nfs/rhel10-install/`{.literal} and
    -   In the Kickstart file, define the NFS installation source as `nfs --server=myserver.example.com --dir=/nfs/rhel10-install/`{.literal}.

**Additional resources**

-   [Deploying an NFS server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/index#deploying-an-nfs-server)

### [5.2. Creating an installation source by using HTTP or HTTPS](#creating-an-installation-source-using-http-or-https) {#creating-an-installation-source-by-using-http-or-https .title}

You can create an installation source for a network-based installation by using an installation tree. It is a directory containing extracted contents of the DVD ISO image and a valid `.treeinfo`{.literal} file. The installation source is accessed over HTTP or HTTPS.

**Prerequisites**

-   You have administrator-level access to a server with Red Hat Enterprise Linux 10, and this server is on the same network as the system to be installed.
-   You have downloaded the full installation DVD ISO from the [Product Downloads](https://access.redhat.com/downloads/content/rhel) page.

Important

If you use an HTTPS server with a self-signed certificate, you must boot the installation program with the `noverifyssl`{.literal} option.

**Procedure**

1.  Install the httpd package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install httpd
    ```

2.  Optional: Install the `mod_ssl`{.literal} package if you want to use the https installation source:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install mod_ssl
    ```

3.  Copy the DVD ISO image to the HTTP(S) server.

4.  Create a suitable directory for mounting the DVD ISO image, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /mnt/rhel10-install/
    ```

5.  Mount the DVD ISO image to the directory:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o loop,ro -t iso9660 /image_directory/image.iso /mnt/rhel10-install/
    ```

    Replace */image_directory/image.iso* with the path to the DVD ISO image.

6.  Copy the files from the mounted image to the HTTP(S) server root.

    ``` {.language-plaintext tabindex="-1"}
    # cp -r /mnt/rhel10-install/ /var/www/html/
    ```

    This command creates the `/var/www/html/rhel10-install/`{.literal} directory with the content of the image. Note that some other copying methods might skip the `.treeinfo`{.literal} file which is required for a valid installation source. Entering the `cp`{.literal} command for entire directories copies `.treeinfo`{.literal} correctly.

7.  Unmount the DVD ISO:

    ``` {.language-plaintext tabindex="-1"}
    # umount /mnt/rhel10-install/
    ```

8.  Enable the http service in firewalld:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=http
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

9.  Optional: Enable the https service in firewalld:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=https
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

10. Start the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now httpd.service
    ```

    The installation tree is now accessible and ready to be used as the installation source.

    Note

    When configuring the installation source, use `http://`{.literal} or `https://`{.literal} as the protocol. Specify the server host name or IP address and the directory containing the ISO image files relative to the HTTP server root. For example, if you use HTTP, the server host name is `myserver.example.com`{.literal}, and you have copied the files from the image to `/var/www/html/rhel10-install/`{.literal}, specify `http://myserver.example.com/rhel10-install/`{.literal} as the installation source.

**Additional resources**

-   [Configuring the Apache HTTP web server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/index#setting-up-the-apache-http-web-server)

### [5.3. Creating an installation source by using FTP](#creating-an-installation-source-using-ftp) {#creating-an-installation-source-by-using-ftp .title}

You can configure an FTP server to host RHEL installation files for network-based installations. It enables multiple systems to install from a centralized source, providing efficient deployment across your network infrastructure using the FTP protocol.

**Prerequisites**

-   You have administrator-level access to a server with Red Hat Enterprise Linux 10, and this server is on the same network as the system to be installed.
-   You have downloaded the full installation DVD ISO from the [Product Downloads](https://access.redhat.com/downloads/content/rhel) page.
-   The `vsftpd`{.literal} package is installed.

**Procedure**

1.  Install the vsftpd package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install vsftpd
    ```

2.  Open and edit the `/etc/vsftpd/vsftpd.conf`{.literal} configuration file in a text editor.

    a.  Change the line `anonymous_enable=NO`{.literal} to `anonymous_enable=YES`{.literal}

    b.  Change the line `write_enable=YES`{.literal} to `write_enable=NO`{.literal}.

    c.  Add lines `pasv_min_port=<`{.literal}*`min_port`{.literal}*`>`{.literal} and `pasv_max_port=<`{.literal}*`max_port`{.literal}*`>`{.literal}. Replace \<*min_port*\> and \<*max_port*\> with the port number range used by the FTP server in passive mode, for example, `10000`{.literal} and `11000`{.literal}.

        This step might be necessary in network environments featuring various firewall/NAT setups.

    d.  Optional: Add custom changes to your configuration. For available options, see the **vsftpd.conf(5)** man page. This procedure assumes that default options are used.

    e.  Configure the firewall to allow the FTP port and port range from the previous step:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --add-port min_port-max_port/tcp --permanent
        ```

        Replace \<*min_port*\> and \<*max_port*\> with the port numbers you entered into the `/etc/vsftpd/vsftpd.conf`{.literal} configuration file.

    f.  Configure the firewall to allow FTP service

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --add-service ftp --permanent
        ```

    g.  Reload the firewall to apply the new rules:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --reload
        ```

3.  Copy the DVD ISO image to the FTP server.

4.  Create a suitable directory for mounting the DVD ISO image, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /mnt/rhel10-install
    ```

5.  Mount the DVD ISO image to the directory:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o loop,ro -t iso9660 /image-directory/image.iso /mnt/rhel10-install
    ```

    Replace *`/image-directory/image.iso`{.literal}* with the path to the DVD ISO image.

6.  Copy the files from the mounted image to the FTP server root:

    ``` {.language-plaintext tabindex="-1"}
    # cp -r /mnt/rhel10-install/ /var/ftp/
    ```

    This command creates the `/var/ftp/rhel10-install/`{.literal} directory with the content of the image. Some copying methods can skip the `.treeinfo`{.literal} file which is required for a valid installation source. Entering the `cp`{.literal} command for whole directories as shown in this procedure will copy `.treeinfo`{.literal} correctly.

7.  Start the `vsftpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now vsftpd.service
    ```

    If the service was running before you changed the `/etc/vsftpd/vsftpd.conf`{.literal} file, restart the service to load the edited file:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart vsftpd.service
    ```

    The installation tree is now accessible and ready to be used as the installation source.

    When configuring the installation source, use `ftp://`{.literal} as the protocol. Specify the server host name or IP address and the directory containing the ISO image files relative to the FTP server root. For example, if the server host name is `myserver.example.com`{.literal} and you have copied the files from the image to `/var/ftp/rhel10-install/`{.literal}, specify `ftp://myserver.example.com/rhel10-install/`{.literal} as the installation source.

## [Chapter 6. Preparing a UEFI HTTP installation source](#preparing-a-uefi-http-installation-source) {#chapter-6.-preparing-a-uefi-http-installation-source .title}

As an administrator of a server on a local network, you can configure an HTTP server to enable HTTP boot and network installation for other systems on your network.

### [6.1. Network installation overview](#network-install-overview_HTTP) {#network-installation-overview .title}

A network installation allows you to install Red Hat Enterprise Linux to a system that has access to an installation server. At a minimum, two systems are required for a network installation:

Server
:   A system running a DHCP server, an HTTP, HTTPS, FTP, or NFS server, and in the PXE boot case, a TFTP server. Although each server can run on a different physical system, the procedures in this section assume a single system is running all servers.

Client
:   The system to which you are installing Red Hat Enterprise Linux. Once installation starts, the client queries the DHCP server. It receives the boot files from the HTTP or TFTP server. Then it downloads the installation environment image from the HTTP, HTTPS, FTP or NFS server. Unlike other installation methods, the client does not require any physical boot media for the installation to start.

To boot a client from the network, enable network boot in the firmware or in a quick boot menu on the client. On some hardware, the option to boot from a network might be disabled, or not available.

The workflow to prepare for an installation of Red Hat Enterprise Linux from a network by using HTTP or PXE is as follows:

1.  Export the installation ISO image or the installation tree to an NFS, HTTPS, HTTP, or FTP server.
2.  Configure the HTTP or TFTP server and DHCP server, and start the HTTP or TFTP service on the server.
3.  Boot the client and start the installation.

You can choose between the following network boot protocols:

HTTP
:   Use the HTTP boot if your client UEFI supports it. HTTP boot is usually more reliable.

PXE (TFTP)
:   PXE boot is more widely supported by client systems, but sending the boot files over TFTP protocol might be slow and result in timeout failures.

**Additional resources**

-   [Preparing network based repositories](#preparing-network-based-repositories "Chapter 5. Preparing network-based repositories")
-   [Red Hat Satellite product documentation](https://docs.redhat.com/en/documentation/red_hat_satellite/6.16)

### [6.2. Configuring the DHCPv4 server for network boot](#configuring-the-dhcpv4-server-for-network-boot_HTTP) {#configuring-the-dhcpv4-server-for-network-boot .title}

Enable the DHCP version 4 (DHCPv4) service on your server, so that it can provide network boot functionality.

**Prerequisites**

-   You are preparing network installation over the IPv4 protocol.

-   Find the network addresses of the server.

    In the following examples, the server has a network interface `enp1s0`{.literal} with this configuration:

    IPv4 address
    :   192.168.124.2/24

    IPv4 gateway + DNS server
    :   192.168.124.1

**Procedure**

1.  Install the DHCP server:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kea
    ```

2.  Configure a DHCPv4 server. Enter the following configuration in the `/etc/kea/kea-dhcp4.conf`{.literal} file. Replace the addresses to match your network card.

    ``` {.language-plaintext tabindex="-1"}
    {
      "Dhcp4": {
        "interfaces-config": {
          "interfaces": [ "enp1s0" ]
        },
        "subnet4": [
          {
            "id": 1,
            "subnet": "192.168.124.0/24",
            "pools": [
              {
                "pool": "192.168.124.100 - 192.168.124.200"
              }
            ],
            "option-data": [
              {
                "space": "dhcp4",
                "name": "routers",
                "code": 3,
                "data": "192.168.124.10"
              },
              {
                "space": "dhcp4",
                "name": "domain-name-servers",
                "code": 6,
                "data": "192.168.124.10"
              }
            ]
          }
        ],
        "client-classes": [
          {
            "name": "uefi PXE Clients",
            "test": "substring(option[60].hex,0,9) == 'PXEClient' and option[93].hex == 0x0007",
            "next-server": "192.168.124.2",
            "boot-file-name": "/uefi/BOOT/BOOTX64.EFI"
          },
          {
            "name": "bios PXE Clients",
            "test": "substring(option[60].hex,0,9) == 'PXEClient' and option[93].hex == 0x0000",
            "next-server": "192.168.124.2",
            "boot-file-name": "syslinux/pxelinux.0"
          },
          {
            "name": "uefi HTTP Clients",
            "test": "substring(option[60].hex,0,10) == 'HTTPClient' and option[93].hex == 0x0007",
            "option-data": [
              {
                "space": "dhcp4",
                "name": "vendor-class-identifier",
                "code": 60,
                "data": "HTTPClient"
              }
            ],
            "next-server": "192.168.124.2",
            "boot-file-name": "http://192.168.124.2/uefi/BOOT/BOOTX64.EFI"
          }
        ]
      }
    }
    ```

3.  Start the DHCPv4 service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now kea-dhcp4
    ```

### [6.3. Configuring the DHCPv6 server for network boot](#configuring-the-dhcpv6-server-for-network-boot_HTTP) {#configuring-the-dhcpv6-server-for-network-boot .title}

Enable the DHCP version 6 (DHCPv4) service on your server, so that it can provide network boot functionality.

**Prerequisites**

-   You are preparing network installation over the IPv6 protocol.

-   Find the network addresses of the server.

    In the following examples, the server has a network interface `enp1s0`{.literal} with this configuration:

    IPv6 address
    :   fd33::2/64

    IPv6 gateway
    :   fd33::1

**Procedure**

1.  Install the DHCP server:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kea
    ```

2.  Configure a DHCPv6 server. Enter the following configuration in the `/etc/kea/kea-dhcp6.conf`{.literal} file. Replace the addresses to match your network card.

    ``` {.language-plaintext tabindex="-1"}
    {
      "Dhcp6": {
        "interfaces-config": {
          "interfaces": [ "enp1s0" ]
        },
        "subnet6": [
          {
            "id": 1,
            "subnet": "fd33::/64",
            "interface": "enp1s0",
            "pools": [
              {
                "pool": "fd33::100-fd33::200"
              }
            ]
          }
        ],
        "client-classes": [
          {
            "name": "uefi PXE Clients",
            "test": "substring(option[16].hex,6,9) == 'PXEClient' and substring(option[16].hex,21,5) == '00007'",
            "option-data": [
              {
                "space": "dhcp6",
                "name": "bootfile-url",
                "code": 59,
                "data": "tftp://[fd33::2]/uefi/BOOT/BOOTX64.EFI"
              }
            ]
          },
          {
            "name": "bios PXE Clients",
            "test": "substring(option[16].hex,6,9) == 'PXEClient' and substring(option[16].hex,21,5) == '00000'",
            "option-data": [
              {
                "space": "dhcp6",
                "name": "bootfile-url",
                "code": 59,
                "data": "tftp://[fd33::2]/syslinux/pxelinux.0"
              }
            ]
          },
          {
            "name": "uefi HTTP Clients",
            "test": "substring(option[16].hex,6,10) == 'HTTPClient' and substring(option[16].hex,22,5) == '00007'",
            "option-data": [
              {
                "space": "dhcp6",
                "name": "bootfile-url",
                "code": 59,
                "data": "http://[fd33::2]/uefi/BOOT/BOOTX64.EFI"
              }
            ]
          }
        ]
      }
    }
    ```

3.  Start the DHCPv6 service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now kea-dhcp6
    ```

4.  If DHCPv6 packets are dropped by the RP filter in the firewall, check its log. If the log contains the `rpfilter_DROP`{.literal} entry, disable the filter using the following configuration in the `/etc/firewalld/firewalld.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    IPv6_rpfilter=no
    ```

### [6.4. Configuring the HTTP server for HTTP boot](#configuring-the-http-server-for-http-boot) {#configuring-the-http-server-for-http-boot .title}

You must install and enable the `httpd`{.literal} service on your server so that the server can provide HTTP boot resources on your network.

**Prerequisites**

-   You have downloaded the RHEL DVD ISO file. See [All Red Hat Enterprise Linux Downloads](https://access.redhat.com/downloads/content/479).

-   Find the network addresses of the server.

    In the following examples, the server has a network card with the `192.168.124.2`{.literal} IPv4 address.

**Procedure**

1.  Install the HTTP server:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install httpd
    ```

2.  Create the `/var/www/html/redhat`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /var/www/html/redhat
    ```

3.  Create a mount point for the downloaded ISO file and then mount the ISO file.

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /var/www/html/redhat/iso
    ```

    ``` {.language-plaintext tabindex="-1"}
    # mount -o loop,ro -t iso9660 path-to-RHEL-DVD.iso /var/www/html/redhat/iso
    ```

4.  Copy the boot loader, kernel, and `initramfs`{.literal} from the mounted ISO file into your HTML directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp -r /var/www/html/redhat/iso/images /var/www/html/redhat
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cp -r /var/www/html/redhat/iso/EFI /var/www/html/redhat
    ```

5.  Make the boot loader configuration editable and ensure the boot files are owned by the user running httpd server (apache):

    ``` {.language-plaintext tabindex="-1"}
    # chmod 644 /var/www/html/redhat/EFI/BOOT/grub.cfg
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chown -R apache:apache /var/www/html/redhat/EFI
    ```

6.  Edit the `/var/www/html/redhat/EFI/BOOT/grub.cfg`{.literal} file and replace its content with the following:

    ``` {.language-plaintext tabindex="-1"}
    set default="1"

    function load_video {
      insmod efi_gop
      insmod efi_uga
      insmod video_bochs
      insmod video_cirrus
      insmod all_video
    }

    load_video
    set gfxpayload=keep

    set timeout=60

    menuentry 'Install Red Hat Enterprise Linux 10.0' --class fedora --class gnu-linux --class gnu --class os {
            linuxefi /redhat/images/pxeboot/vmlinuz inst.repo=http://192.168.124.2/redhat/iso quiet
            initrdefi /redhat/images/pxeboot/initrd.img
    }
    submenu 'Troubleshooting -->' {
            menuentry 'Install Red Hat Enterprise Linux 10.0 in text mode' --class fedora --class gnu-linux --class gnu --class os {
                    linuxefi /redhat/images/pxeboot/vmlinuz inst.repo=http://192.168.124.2/redhat/iso inst.text quiet
                    initrdefi /redhat/images/pxeboot/initrd.img
            }
            menuentry 'Rescue a Red Hat Enterprise Linux system' --class fedora --class gnu-linux --class gnu --class os {
                    linuxefi /redhat/images/pxeboot/vmlinuz inst.stage2=http://192.168.124.2/redhat/iso inst.rescue quiet
                    initrdefi /redhat/images/pxeboot/initrd.img
            }
    }
    ```

    In this file, update the following strings:

    *Install Red Hat Enterprise Linux 10.0*
    :   Edit the version number to match the version of RHEL that you downloaded.

    *192.168.124.2*
    :   Replace with the IP address of your server.

7.  Open ports in the firewall to allow HTTP (80), DHCP (67, 68) and DHCPv6 (546, 547) traffic:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --zone public \
                   --add-port={80/tcp,67/udp,68/udp,546/udp,547/udp}
    ```

    This command enables temporary access until the next server reboot. To enable permanent access, add the `--permanent`{.literal} option to the command.

8.  Reload firewall rules and start the HTTP server.

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now httpd
    ```

9.  Make the `html`{.literal} directory and its content readable and executable:

    ``` {.language-plaintext tabindex="-1"}
    # chmod -cR u=rwX,g=rX,o=rX /var/www/html
    ```

10. Restore the SELinux context of the `html`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -FvvR /var/www/html
    ```

## [Chapter 7. Preparing a PXE installation source](#preparing-a-pxe-installation-source) {#chapter-7.-preparing-a-pxe-installation-source .title}

You must configure TFTP and DHCP on a PXE server to enable PXE boot and network installation.

### [7.1. Network installation overview](#network-install-overview_PXE-installation) {#network-installation-overview-1 .title}

A network installation allows you to install Red Hat Enterprise Linux to a system that has access to an installation server. At a minimum, two systems are required for a network installation:

Server
:   A system running a DHCP server, an HTTP, HTTPS, FTP, or NFS server, and in the PXE boot case, a TFTP server. Although each server can run on a different physical system, the procedures in this section assume a single system is running all servers.

Client
:   The system to which you are installing Red Hat Enterprise Linux. Once installation starts, the client queries the DHCP server. It receives the boot files from the HTTP or TFTP server. Then it downloads the installation environment image from the HTTP, HTTPS, FTP or NFS server. Unlike other installation methods, the client does not require any physical boot media for the installation to start.

To boot a client from the network, enable network boot in the firmware or in a quick boot menu on the client. On some hardware, the option to boot from a network might be disabled, or not available.

The workflow to prepare for an installation of Red Hat Enterprise Linux from a network by using HTTP or PXE is as follows:

1.  Export the installation ISO image or the installation tree to an NFS, HTTPS, HTTP, or FTP server.
2.  Configure the HTTP or TFTP server and DHCP server, and start the HTTP or TFTP service on the server.
3.  Boot the client and start the installation.

You can choose between the following network boot protocols:

HTTP
:   Use the HTTP boot if your client UEFI supports it. HTTP boot is usually more reliable.

PXE (TFTP)
:   PXE boot is more widely supported by client systems, but sending the boot files over TFTP protocol might be slow and result in timeout failures.

**Additional resources**

-   [Preparing network based repositories](#preparing-network-based-repositories "Chapter 5. Preparing network-based repositories")
-   [Red Hat Satellite product documentation](https://docs.redhat.com/en/documentation/red_hat_satellite/6.16)

### [7.2. Configuring the DHCPv4 server for network boot](#configuring-the-dhcpv4-server-for-network-boot_PXE-installation) {#configuring-the-dhcpv4-server-for-network-boot-1 .title}

Enable the DHCP version 4 (DHCPv4) service on your server, so that it can provide network boot functionality.

**Prerequisites**

-   You are preparing network installation over the IPv4 protocol.

-   Find the network addresses of the server.

    In the following examples, the server has a network interface `enp1s0`{.literal} with this configuration:

    IPv4 address
    :   192.168.124.2/24

    IPv4 gateway + DNS server
    :   192.168.124.1

**Procedure**

1.  Install the DHCP server:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kea
    ```

2.  Configure a DHCPv4 server. Enter the following configuration in the `/etc/kea/kea-dhcp4.conf`{.literal} file. Replace the addresses to match your network card.

    ``` {.language-plaintext tabindex="-1"}
    {
      "Dhcp4": {
        "interfaces-config": {
          "interfaces": [ "enp1s0" ]
        },
        "subnet4": [
          {
            "id": 1,
            "subnet": "192.168.124.0/24",
            "pools": [
              {
                "pool": "192.168.124.100 - 192.168.124.200"
              }
            ],
            "option-data": [
              {
                "space": "dhcp4",
                "name": "routers",
                "code": 3,
                "data": "192.168.124.10"
              },
              {
                "space": "dhcp4",
                "name": "domain-name-servers",
                "code": 6,
                "data": "192.168.124.10"
              }
            ]
          }
        ],
        "client-classes": [
          {
            "name": "uefi PXE Clients",
            "test": "substring(option[60].hex,0,9) == 'PXEClient' and option[93].hex == 0x0007",
            "next-server": "192.168.124.2",
            "boot-file-name": "/uefi/BOOT/BOOTX64.EFI"
          },
          {
            "name": "bios PXE Clients",
            "test": "substring(option[60].hex,0,9) == 'PXEClient' and option[93].hex == 0x0000",
            "next-server": "192.168.124.2",
            "boot-file-name": "syslinux/pxelinux.0"
          },
          {
            "name": "uefi HTTP Clients",
            "test": "substring(option[60].hex,0,10) == 'HTTPClient' and option[93].hex == 0x0007",
            "option-data": [
              {
                "space": "dhcp4",
                "name": "vendor-class-identifier",
                "code": 60,
                "data": "HTTPClient"
              }
            ],
            "next-server": "192.168.124.2",
            "boot-file-name": "http://192.168.124.2/uefi/BOOT/BOOTX64.EFI"
          }
        ]
      }
    }
    ```

3.  Start the DHCPv4 service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now kea-dhcp4
    ```

### [7.3. Configuring the DHCPv6 server for network boot](#configuring-the-dhcpv6-server-for-network-boot_PXE-installation) {#configuring-the-dhcpv6-server-for-network-boot-1 .title}

Enable the DHCP version 6 (DHCPv4) service on your server, so that it can provide network boot functionality.

**Prerequisites**

-   You are preparing network installation over the IPv6 protocol.

-   Find the network addresses of the server.

    In the following examples, the server has a network interface `enp1s0`{.literal} with this configuration:

    IPv6 address
    :   fd33::2/64

    IPv6 gateway
    :   fd33::1

**Procedure**

1.  Install the DHCP server:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kea
    ```

2.  Configure a DHCPv6 server. Enter the following configuration in the `/etc/kea/kea-dhcp6.conf`{.literal} file. Replace the addresses to match your network card.

    ``` {.language-plaintext tabindex="-1"}
    {
      "Dhcp6": {
        "interfaces-config": {
          "interfaces": [ "enp1s0" ]
        },
        "subnet6": [
          {
            "id": 1,
            "subnet": "fd33::/64",
            "interface": "enp1s0",
            "pools": [
              {
                "pool": "fd33::100-fd33::200"
              }
            ]
          }
        ],
        "client-classes": [
          {
            "name": "uefi PXE Clients",
            "test": "substring(option[16].hex,6,9) == 'PXEClient' and substring(option[16].hex,21,5) == '00007'",
            "option-data": [
              {
                "space": "dhcp6",
                "name": "bootfile-url",
                "code": 59,
                "data": "tftp://[fd33::2]/uefi/BOOT/BOOTX64.EFI"
              }
            ]
          },
          {
            "name": "bios PXE Clients",
            "test": "substring(option[16].hex,6,9) == 'PXEClient' and substring(option[16].hex,21,5) == '00000'",
            "option-data": [
              {
                "space": "dhcp6",
                "name": "bootfile-url",
                "code": 59,
                "data": "tftp://[fd33::2]/syslinux/pxelinux.0"
              }
            ]
          },
          {
            "name": "uefi HTTP Clients",
            "test": "substring(option[16].hex,6,10) == 'HTTPClient' and substring(option[16].hex,22,5) == '00007'",
            "option-data": [
              {
                "space": "dhcp6",
                "name": "bootfile-url",
                "code": 59,
                "data": "http://[fd33::2]/uefi/BOOT/BOOTX64.EFI"
              }
            ]
          }
        ]
      }
    }
    ```

3.  Start the DHCPv6 service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now kea-dhcp6
    ```

4.  If DHCPv6 packets are dropped by the RP filter in the firewall, check its log. If the log contains the `rpfilter_DROP`{.literal} entry, disable the filter using the following configuration in the `/etc/firewalld/firewalld.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    IPv6_rpfilter=no
    ```

### [7.4. Configuring a TFTP server for BIOS-based clients](#configuring-a-tftp-server-for-bios-based-clients) {#configuring-a-tftp-server-for-bios-based-clients .title}

You must configure a TFTP server and DHCP server and start the TFTP service on the PXE server for BIOS-based AMD and Intel 64-bit systems to enable automated network booting.

**Procedure**

1.  As root, install the following package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tftp-server
    ```

2.  Allow incoming connections to the `tftp service`{.literal} in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-service=tftp
    ```

    This command enables temporary access until the next server reboot.

3.  Optional: To enable permanent access, repeat the previous command together with the `--permanent`{.literal} option.

    Depending on the location of the installation ISO file, you might have to allow incoming connections for HTTP or other services.

4.  Install `syslinux-tftpboot`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y install syslinux-tftpboot
    ```

5.  Create a `pxelinux`{.literal} directory in the `/var/lib/tftpboot`{.literal} directory and copy all the files provided by the `syslinux-tftpboot`{.literal} package (located in `/tftpboot`{.literal} directory) into the `pxelinux`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /var/lib/tftpboot/pxelinux
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cp /tftpboot/* /var/lib/tftpboot/pxelinux
    ```

6.  Create the directory `pxelinux.cfg`{.literal} in the `pxelinux`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /var/lib/tftpboot/pxelinux/pxelinux.cfg
    ```

7.  Create a configuration file named `default`{.literal} and add it to the `pxelinux.cfg`{.literal} directory as shown in the following example:

    ``` {.language-plaintext tabindex="-1"}
    DEFAULT menu.c32

    MENU TITLE Red Hat Enterprise Linux 10.0 Installation
    TIMEOUT 600

    LABEL default
        MENU LABEL ^Install Red Hat Enterprise Linux 10.0
        KERNEL /pxelinux/images/RHEL-10/vmlinuz
        APPEND initrd=/pxelinux/images/RHEL-10/initrd.img inst.repo=http://192.168.124.2/redhat/iso quiet

    LABEL text
        MENU LABEL Install Red Hat Enterprise Linux 10.0 in ^text mode
        KERNEL /pxelinux/images/RHEL-10/vmlinuz
        APPEND initrd=/pxelinux/images/RHEL-10/initrd.img inst.repo=http://192.168.124.2/redhat/iso inst.text quiet

    LABEL rescue
        MENU LABEL ^Rescue a Red Hat Enterprise Linux system
        KERNEL /pxelinux/images/RHEL-10/vmlinuz
        APPEND initrd=/pxelinux/images/RHEL-10/initrd.img inst.stage2=http://192.168.124.2/redhat/iso inst.rescue quiet

    LABEL local
        MENU LABEL Boot from ^local drive
        LOCALBOOT 0xffff
    ```

    -   The installation program cannot boot without its runtime image. Use the `inst.stage2`{.literal} boot option to specify location of the image. Alternatively, you can use the `inst.repo=`{.literal} option to specify the image as well as the installation source.
    -   The installation source location used with `inst.repo`{.literal} must contain a valid `.treeinfo`{.literal} file.
    -   When you select the content of RHEL10 installation DVD as the installation source, the `.treeinfo`{.literal} file points to the BaseOS and the AppStream repositories. You can use a single `inst.repo`{.literal} option to load both repositories.

8.  Create a subdirectory to store the boot image files in the `/var/lib/tftpboot`{.literal} directory, and copy the boot image files to the directory. In this example, the directory is `/var/lib/tftpboot/pxelinux/images/RHEL-10`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /var/lib/tftpboot/pxelinux/images/RHEL-10
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cp /path_to_x86_64_images/pxeboot/{vmlinuz,initrd.img} /var/lib/tftpboot/pxelinux/images/RHEL-10/
    ```

9.  Start and enable the `tftp.socket`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now tftp.socket
    ```

    The PXE boot server is now ready to serve PXE clients. You can start the client, which is the system to which you are installing Red Hat Enterprise Linux. Select **PXE Boot** or **Network Boot** when prompted to specify a boot source, and start the network installation.

### [7.5. Configuring a TFTP server for UEFI-based clients](#configuring-a-tftp-server-for-uefi-based-clients) {#configuring-a-tftp-server-for-uefi-based-clients .title}

You must configure a TFTP server and DHCP server and start the TFTP service on the PXE server for UEFI-based AMD64, Intel 64, and 64-bit ARM systems.

**Procedure**

1.  As root, install the following package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tftp-server
    ```

2.  Allow incoming connections to the `tftp service`{.literal} in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-service=tftp
    ```

    This command enables temporary access until the next server reboot.

3.  Optional: To enable permanent access, repeat the previous command together with the `--permanent`{.literal} option.

    Depending on the location of the installation ISO file, you might have to allow incoming connections for HTTP or other services.

4.  Access the EFI boot image files from the DVD ISO image:

    ``` {.language-plaintext tabindex="-1"}
    # mount -t iso9660 /path_to_image/name_of_image.iso /mount_point -o loop,ro
    ```

5.  Copy the EFI boot images from the DVD ISO image:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /var/lib/tftpboot/redhat
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cp -r /mount_point/EFI /var/lib/tftpboot/redhat/
    ```

6.  Create a subdirectory to store the boot image files in the `/var/lib/tftpboot/`{.literal} directory, and copy the boot image files to the directory. In this example, the directory is `/var/lib/tftpboot/images/RHEL-10/`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /var/lib/tftpboot/images/RHEL-10/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cp /mount_point/images/pxeboot/{vmlinuz,initrd.img} /var/lib/tftpboot/images/RHEL-10/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # umount /mount_point
    ```

7.  Fix the permissions of the copied files:

    ``` {.language-plaintext tabindex="-1"}
    # chmod -R 755 /var/lib/tftpboot/redhat/
    ```

    Important

    In addition to the default `grub.cfg`{.literal} menu file, Red Hat Enterprise Linux 10 UEFI PXE boot supports a lowercase file name format for a MAC-based GRUB menu file. For example, the MAC address file name format for GRUB can be `grub.cfg-01-aa-bb-cc-dd-ee-ff`{.literal}.

8.  Replace the content of `/var/lib/tftpboot/redhat/EFI/BOOT/grub.cfg`{.literal} with the following example:

    ``` {.language-plaintext tabindex="-1"}
    set default="1"
    set timeout=60

    function load_video {
      insmod efi_gop
      insmod efi_uga
      insmod video_bochs
      insmod video_cirrus
      insmod all_video
    }

    load_video
    set gfxpayload=keep

    menuentry 'Install Red Hat Enterprise Linux 10.0' --class fedora --class gnu-linux --class gnu --class os {
            linuxefi /images/RHEL-10/vmlinuz inst.repo=http://192.168.124.2/redhat/iso quiet
            initrdefi /images/RHEL-10/initrd.img
    }
    submenu 'Troubleshooting -->' {
            menuentry 'Install Red Hat Enterprise Linux 10.0 in text mode' --class fedora --class gnu-linux --class gnu --class os {
                    linuxefi /images/RHEL-10/vmlinuz inst.repo=http://192.168.124.2/redhat/iso inst.text quiet
                    initrdefi /images/RHEL-10/initrd.img
            }
            menuentry 'Rescue a Red Hat Enterprise Linux system' --class fedora --class gnu-linux --class gnu --class os {
                    linuxefi /images/RHEL-10/vmlinuz inst.stage2=http://192.168.124.2/redhat/iso inst.rescue quiet
                    initrdefi /images/RHEL-10/initrd.img
            }
    }
    ```

    -   The installation program cannot boot without its runtime image. Use the `inst.stage2`{.literal} boot option to specify location of the image. Alternatively, you can use the `inst.repo=`{.literal} option to specify the image as well as the installation source.
    -   The installation source location used with `inst.repo`{.literal} must contain a valid `.treeinfo`{.literal} file.
    -   When you select the RHEL10 installation DVD as the installation source, the `.treeinfo`{.literal} file points to the BaseOS and the AppStream repositories. You can use a single `inst.repo`{.literal} option to load both repositories.

9.  Start and enable the `tftp.socket`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now tftp.socket
    ```

    The PXE boot server is now ready to serve PXE clients. You can start the client, which is the system to which you are installing Red Hat Enterprise Linux. Select **PXE Boot** or **Network Boot** when prompted to specify a boot source, and start the network installation.

**Additional resources**

-   [Using the Shim Program](https://www.rodsbooks.com/efi-bootloaders/secureboot.html#shim)

## [Chapter 8. Preparing a RHEL installation on 64-bit IBM Z](#preparing-a-rhel-installation-on-64-bit-ibm-z) {#chapter-8.-preparing-a-rhel-installation-on-64-bit-ibm-z .title}

You can install Red Hat Enterprise Linux on the 64-bit IBM Z architecture.

### [8.1. Planning for installation on 64-bit IBM Z](#planning-for-installation-on-64-bit-ibm-z) {#planning-for-installation-on-64-bit-ibm-z .title}

Red Hat Enterprise Linux 10 runs on **IBM z15** or **IBM LinuxONE III** systems, or later.

The installation process assumes that you are familiar with the 64-bit IBM Z and can configure *logical partitions* (LPARs) and z/VM guest virtual machines. For Red Hat Enterprise Linux installation on 64-bit IBM Z, Red Hat supports Direct Access Storage Device (DASD) and SCSI disk devices attached over Fiber Channel Protocol (FCP). It also supports `virtio-blk`{.literal} and `virtio-scsi`{.literal} devices. When using FCP devices, use them in multipath configuration for better reliability.

Important

DASDs are disks that allow a maximum of three partitions per device. For example, `dasda`{.literal} can have partitions `dasda1`{.literal}, `dasda2`{.literal}, and `dasda3`{.literal}.

Pre-installation decisions

:   -   Whether the operating system is to be run on an LPAR, KVM, or as a z/VM guest operating system.

    -   Network configuration. Red Hat Enterprise Linux 10 for 64-bit IBM Z supports the following network devices:

        -   Real and virtual *Open Systems Adapter* (OSA)
        -   Real and virtual HiperSockets
        -   `virtio-net`{.literal} devices
        -   RDMA over Converged Ethernet (RoCE)

    -   Ensure you select machine type as *`ESA`{.literal}* for your z/VM VMs, because selecting any other machine types might prevent RHEL from installing.

Note

When initializing swap space on a Fixed Block Architecture (FBA) DASD by using the **SWAPGEN** utility, the `FBAPART`{.literal} option must be used.

**Additional resources**

-   [Steps for defining a main virtual machine for Linux - IBM documentation](https://www.ibm.com/docs/en/zvm/7.3?topic=linux-steps-defining-master-virtual-machine)
-   [RHEL Technology Capabilities and Limits](https://access.redhat.com/articles/rhel-limits)
-   [IT infrastructure - IBM documentation](https://www.ibm.com/it-infrastructure/z)
-   [Secure boot for Linux on IBM Z](https://www.ibm.com/docs/en/linux-on-systems?topic=security-secure-boot-linux-onibm-z-linuxone)
-   [Servers quick start guides - IBM documentation](https://www.ibm.com/docs/en/linux-on-systems?topic=servers-quick-start-guides-installing-linux)
-   [Red Hat Ecosystem Catalog](https://catalog.redhat.com)

### [8.2. Boot media compatibility for IBM Z servers](#boot-media-compatibility-for-ibm-z-servers) {#boot-media-compatibility-for-ibm-z-servers .title}

The table lists the detailed information about the supported boot media options for installing Red Hat Enterprise Linux on 64-bit IBM Z servers. It outlines the compatibility of each boot medium with different system types and indicates whether the `zipl`{.literal} boot loader is used.

Use this information to determine the most suitable boot medium for your specific environment.

+------------------------------------------------+-----------------------+-----------+-----------+-----------+
| System type / Boot media                       | Uses zipl boot loader | z/VM      | KVM       | LPAR      |
+:===============================================+:======================+:==========+:==========+:==========+
| z/VM Reader                                    | No                    | Yes       | N/A       | N/A       |
+------------------------------------------------+-----------------------+-----------+-----------+-----------+
| SE or HMC (remote SFTP, FTPS, FTP server, DVD) | No                    | N/A       | N/A       | Yes       |
+------------------------------------------------+-----------------------+-----------+-----------+-----------+
| DASD                                           | Yes                   | Yes       | Yes       | Yes       |
+------------------------------------------------+-----------------------+-----------+-----------+-----------+
| FCP SCSI LUNs                                  | Yes                   | Yes       | Yes       | Yes       |
+------------------------------------------------+-----------------------+-----------+-----------+-----------+
| FCP SCSI DVD                                   | Yes                   | Yes       | Yes       | Yes       |
+------------------------------------------------+-----------------------+-----------+-----------+-----------+

Show more

N/A indicates that the boot medium is not applicable for the specified system type.

### [8.3. Supported environments and components for IBM Z servers](#supported-environments-and-components-for-ibm-z-servers) {#supported-environments-and-components-for-ibm-z-servers .title}

The following tables list the supported environments, network devices, machine types, and storage types for different system types when installing Red Hat Enterprise Linux on 64-bit IBM Z servers. Use these tables to identify the compatibility of various components with your specific system configuration.

+-------------------------------------+-------------+-------------+-------------+
| Network device                      | z/VM        | KVM         | LPAR        |
+:====================================+:============+:============+:============+
| Open Systems Adapter (OSA)          | Yes         | N/A         | Yes         |
+-------------------------------------+-------------+-------------+-------------+
| HiperSockets                        | Yes         | N/A         | Yes         |
+-------------------------------------+-------------+-------------+-------------+
| virtio-net                          | N/A         | Yes         | N/A         |
+-------------------------------------+-------------+-------------+-------------+
| RDMA over Converged Ethernet (RoCE) | Yes         | Yes         | Yes         |
+-------------------------------------+-------------+-------------+-------------+

: Table 8.1. Network device compatibility for system types

Show more

N/A indicates that the component is not applicable for the specified system type.

+---------------------------+-------------+-------------+-------------+
| Machine type              | z/VM        | KVM         | LPAR        |
+:==========================+:============+:============+:============+
| ESA                       | Yes         | N/A         | N/A         |
+---------------------------+-------------+-------------+-------------+
| s390-virtio-ccw           | N/A         | Yes         | N/A         |
+---------------------------+-------------+-------------+-------------+

: Table 8.2. Machine type compatibility for system types

Show more

N/A indicates that the component is not applicable for the specified system type.

+---------------------------------------------------------------------------+-------------+---------------------------------------+-------------+
| Storage type                                                              | z/VM        | KVM                                   | LPAR        |
+:==========================================================================+:============+:======================================+:============+
| DASD                                                                      | Yes         | Yes                                   | Yes         |
+---------------------------------------------------------------------------+-------------+---------------------------------------+-------------+
| FCP SCSI                                                                  | Yes         | Yes[^\[a\]^](#ftn.idm139687901598640) | Yes         |
+---------------------------------------------------------------------------+-------------+---------------------------------------+-------------+
| virtio-blk                                                                | N/A         | Yes                                   | N/A         |
+---------------------------------------------------------------------------+-------------+---------------------------------------+-------------+
| [^\[a\]^](#idm139687901598640) Conditional support based on configuration |             |                                       |             |
+---------------------------------------------------------------------------+-------------+---------------------------------------+-------------+

: Table 8.3. Storage type compatibility for system types

Show more

N/A indicates that the component is not applicable for the specified system type.

### [8.4. Overview of installation process on 64-bit IBM Z servers](#overview-of-installation-process-on-64-bit-ibm-z-servers) {#overview-of-installation-process-on-64-bit-ibm-z-servers .title}

You can install Red Hat Enterprise Linux on 64-bit IBM Z interactively or in unattended mode. Installation on 64-bit IBM Z differs from other architectures as it is typically performed over a network, and not from local media. The installation consists of three phases:

1.  Booting the installation.

    -   Connect to the mainframe.
    -   Customize the boot parameters.
    -   Perform an initial program load (IPL), or boot from the media containing the installation program.

2.  Connecting to the installation system.

    -   From a local machine, connect to the remote 64-bit IBM Z system by using SSH, and start the installation program by using Remote Desktop Protocol (RDP).

3.  Completing the installation by using the RHEL installation program.

### [8.5. Boot media for installing RHEL on 64-bit IBM Z servers](#boot-media-for-installing-rhel-on-64-bit-ibm-z-servers) {#boot-media-for-installing-rhel-on-64-bit-ibm-z-servers .title}

After establishing a connection with the mainframe, you need to perform an initial program load (IPL), or boot, from the medium containing the installation program.

In general, you can boot the Linux installation system by using any method. It includes the kernel (`kernel.img`{.literal}), initial RAM disk (`initrd.img`{.literal}), and parameters from `generic.prm`{.literal} plus user-defined parameters. Additionally, a `generic.ins`{.literal} file is loaded which determines file names and memory addresses for the initrd, kernel and `generic.prm`{.literal}.

The Linux installation system is also called the *installation program* in this book.

You can use the following boot media only if Linux is to run as a guest operating system under z/VM:

-   z/VM reader

You can use the following boot media only if Linux is to run in LPAR mode:

-   SE or HMC through a remote SFTP, FTPS or FTP server
-   SE or HMC DVD

You can use the following boot media for both z/VM and LPAR:

-   DASD
-   SCSI disk device that is attached through an FCP channel

If you use DASD or an FCP-attached SCSI disk device as boot media, you must have a configured `zipl`{.literal} boot loader.

### [8.6. Customization of boot parameters](#customization-of-boot-parameters) {#customization-of-boot-parameters .title}

Before the installation begins, configure some mandatory boot parameters. When installing through `z/VM`{.literal}, these parameters must be configured before you boot into the `generic.prm`{.literal} file. When installing on an `LPAR`{.literal}, the `rd.cmdline`{.literal} parameter is set to `ask`{.literal} by default.

It means the system prompts you to enter these boot parameters. In both cases, the required parameters are the same. All network configuration can either be specified by using a parameter file, or at the prompt.

Installation source
:   An installation source must always be configured.

You can use the `inst.repo`{.literal} option to specify the package source for the installation.

Network devices

:   Network configuration must be provided if network access will be required during the installation. If you plan to perform an unattended (Kickstart-based) installation by using only local media such as a disk, network configuration can be omitted.

    `ip=`{.literal}
    :   You can use the `ip=`{.literal} option for basic network configuration, and other options as required.

    `rd.znet=`{.literal}

    :   Also, you can use the `rd.znet=`{.literal} kernel option, which takes a network protocol type. It is a comma delimited list of sub-channels, and, optionally, comma delimited `sysfs`{.literal} parameter and value pairs for qeth devices. This parameter can be specified multiple times to activate multiple network devices.

        For example:

        ``` {.language-plaintext tabindex="-1"}
        rd.znet=qeth,0.0.0600,0.0.0601,0.0.0602,layer2=1,portno=<number>
        ```

        When specifying multiple `rd.znet`{.literal} boot options, only the last one is passed on to the kernel command line of the installed system. This does not affect the networking of the system since all network devices configured during installation are properly activated and configured at boot.

        The qeth device driver assigns the same interface name for Ethernet and Hipersockets devices: `enc`{.literal}*`<device number>`{.literal}*. The bus ID is composed of the channel subsystem ID, subchannel set ID, and device number, separated by dots. The device number is the last part of the bus ID, without leading zeroes and dots. For example, a device with the bus ID `0.0.0a00`{.literal} uses the interface name `enca00`{.literal}.

Storage devices

:   At least one storage device must always be configured for text mode installations.

    The `rd.dasd=`{.literal} option takes a Direct Access Storage Device (DASD) adapter device bus identifier. For multiple DASDs, specify the parameter multiple times, or use a comma separated list of bus IDs. To specify a range of DASDs, specify the first and the last bus ID.

    For example:

    ``` {.language-plaintext tabindex="-1"}
    rd.dasd=0.0.0200 rd.dasd=0.0.0202(ro),0.0.0203(ro:failfast),0.0.0205-0.0.0207
    ```

    All DASDs that were specified using the `rd.dasd=`{.literal} kernel argument during the installation process are automatically activated on the installed system. This activation occurs regardless of whether the DASDs were used for partitioning during the installation. All disks made visible to the installer through `rd.dasd=`{.literal} will be online and available on the first boot of the installed system.

    The rd.zfcp= option takes a SCSI over FCP (zFCP) adapter device bus identifier, a target WWPN, and an FCP LUN. It then activates one path to a SCSI disk. This parameter needs to be specified at least twice to activate multiple paths to the same disk. This parameter can be specified multiple times to activate multiple disks, each with multiple paths.

    Since 10, a target world wide port name (WWPN) and an FCP LUN are required only if the zFCP device is not configured in NPIV mode. They are also required when auto LUN scanning is disabled with the `zfcp.allow_lun_scan=0`{.literal} kernel parameter. It provides access to all SCSI devices found in the storage area network attached to the FCP device with the specified bus ID. This parameter needs to be specified at least twice to activate multiple paths to the same disks.

    ``` {.language-plaintext tabindex="-1"}
    rd.zfcp=0.0.4000,0x5005076300C213e9,0x5022000000000000
    rd.zfcp=0.0.4000
    ```

Kickstart options

:   If you are using a Kickstart file to perform an automatic installation, you must always specify the location of the Kickstart file by using the `inst.ks=`{.literal} option. For an unattended, fully automatic Kickstart installation, the `inst.cmdline`{.literal} option is also useful. An example customized `generic.prm`{.literal} file containing all mandatory parameters look similar to the following example:

    ``` {.language-plaintext tabindex="-1"}
    ro ramdisk_size=40000 cio_ignore=all,!condev
    inst.repo=http://example.com/path/to/repository
    rd.znet=qeth,0.0.0600,0.0.0601,0.0.0602,layer2=1,portno=0,portname=foo
    ip=192.168.17.115::192.168.17.254:24:foobar.systemz.example.com:enc600:none
    nameserver=192.168.17.1
    rd.dasd=0.0.0200 rd.dasd=0.0.0202
    rd.zfcp=0.0.4000,0x5005076300c213e9,0x5022000000000000
    rd.zfcp=0.0.5000,0x5005076300dab3e9,0x5022000000000000
    inst.ks=http://example.com/path/to/kickstart
    ```

    Some installation methods require a file that maps installation data locations on the HMC DVD or FTP server. The file also specifies the memory locations where the data is copied.

    The file is typically named `generic.ins`{.literal}, and contains file names for the initial RAM disk, kernel image, and parameter file (`generic.prm`{.literal}) and a memory location for each file. An example `generic.ins`{.literal} will look similar to the following example:

    ``` {.language-plaintext tabindex="-1"}
    images/kernel.img 0x00000000
    images/initrd.img 0x02000000
    images/genericdvd.prm 0x00010480
    images/initrd.addrsize 0x00010408
    ```

    A valid `generic.ins`{.literal} file is provided by Red Hat along with all other files required to boot the installer. Modify this file only if you want to, for example, load a different kernel version than default.

**Additional resources**

-   [`inst.repo`{.literal}](#installation-source-boot-options "23.1. Installation source boot options")
-   [`ip=`{.literal}](#network-boot-options "23.2. Network boot options")

### [8.7. Preparing an installation in a z/VM guest virtual machine](#preparing-an-installation-in-a-z-vm-guest-virtual-machine) {#preparing-an-installation-in-a-zvm-guest-virtual-machine .title}

Use the `x3270`{.literal} or `c3270`{.literal} emulator to log in to z/VM from Linux systems. You can also use the IBM 3270 command-line tool on the 64-bit IBM Z® Hardware Management Console (HMC). Microsoft Windows users can use several alternatives, including `wc3270`{.literal}.

When creating z/VM virtual machines, select the **ESA** machine type. Using other machine types might prevent successful Red Hat Enterprise Linux installation. See the [IBM documentation](https://www.ibm.com/docs/en/zvm/7.3?topic=linux-steps-defining-master-virtual-machine).

**Procedure**

1.  Log in to the `z/VM`{.literal} guest virtual machine chosen for the Linux installation.

2.  Optional: If your 3270 connection is interrupted and you cannot log in again because the previous session is still active. In this case, you can replace the old session with a new one by entering the following command on the `z/VM`{.literal} logon screen:

    ``` {.language-plaintext tabindex="-1"}
    logon user here
    ```

    Replace *user* with the name of the `z/VM`{.literal} guest virtual machine. Depending on whether an external security manager, for example RACF, is used, the logon command might vary.

3.  If you are not already running **CMS** (single-user operating system shipped with z/VM) in your guest, boot it now by entering the command:

    ``` {.language-plaintext tabindex="-1"}
    cp ipl cms
    ```

4.  Be sure not to use CMS disks such as your A disk (often device number 0191) as installation targets. To determine which disks are in use by CMS, use the following query:

    ``` {.language-plaintext tabindex="-1"}
    query disk
    ```

5.  You can use the following CP (z/VM Control Program, which is the z/VM hypervisor) query commands to determine about the device configuration of your z/VM guest virtual machine:

    a.  Query the available main memory, which is called *storage* in 64-bit IBM Z terminology. Your guest should have at least 1 GiB of main memory.

        ``` {.language-plaintext tabindex="-1"}
        cp query virtual storage
        ```

    b.  Query available network devices by type:

        `osa`{.literal}
        :   OSA - CHPID type OSD, real or virtual (VSWITCH or GuestLAN), both in QDIO mode

        `hsi`{.literal}
        :   HiperSockets - CHPID type IQD, real or virtual (GuestLAN type Hipers)

        `lcs`{.literal}
        :   LCS - CHPID type OSE

        For example, to query all of the network device types mentioned earlier, run:

        ``` {.language-plaintext tabindex="-1"}
        cp query virtual osa
        ```

    c.  Query available DASDs. Only those that are flagged `RW`{.literal} for read-write mode can be used as installation targets:

        ``` {.language-plaintext tabindex="-1"}
        cp query virtual dasd
        ```

    d.  Query available FCP devices (vHBAs):

        ``` {.language-plaintext tabindex="-1"}
        cp query virtual fcp
        ```

### [8.8. Parameters and configuration files on 64-bit IBM Z](#parameters-and-configuration-files-on-64-bit-ibm-z) {#parameters-and-configuration-files-on-64-bit-ibm-z .title}

You can customize and configure RHEL by using the parameters and configuration files on 64-bit IBM Z.

#### [8.8.1. Required configuration file parameters on 64-bit IBM Z](#required-configuration-file-parameters-on-64-bit-ibm-z) {#required-configuration-file-parameters-on-64-bit-ibm-z .title}

Several parameters are required and must be included in the parameter file. These parameters are also provided in the file `generic.prm`{.literal} in directory `images/`{.literal} of the installation DVD.

-   `ro`{.literal}

    Mounts the root file system, which is a RAM disk, read-only.

-   `ramdisk_size=`{.literal}*`size`{.literal}*

    Modifies the memory size reserved for the RAM disk to ensure that the Red Hat Enterprise Linux installation program fits within it. For example: `ramdisk_size=40000`{.literal}.

The `generic.prm`{.literal} file also contains the additional parameter \"cio_ignore=all,!condev\". This setting speeds up boot and device detection on systems with many devices. The installation program transparently handles the activation of ignored devices.

**Additional resources**

-   [cio_ignore - List devices to be ignored](https://www.ibm.com/docs/en/linux-on-systems?topic=parameters-cio-ignore)

#### [8.8.2. 64-bit IBM z/VM configuration file](#ibm-z-64-bit-vm-configuration-file) {#bit-ibm-zvm-configuration-file .title}

Under z/VM, you can use a configuration file on a CMS-formatted disk. The purpose of the CMS configuration file is to save space in the parameter file by moving parameters that configure the initial network configuration, DASD, and FCP specification out of it.

Each line of the CMS configuration file contains a single variable and its associated value, in the following shell-style syntax: *`variable`{.literal}*`=`{.literal}*`value`{.literal}*.

You must also add the `CMSDASD`{.literal} and `CMSCONFFILE`{.literal} parameters to the parameter file. These parameters point the installation program to the configuration file:

`CMSDASD=`{.literal}*`cmsdasd_address`{.literal}*

:   Where *cmsdasd_address* is the device number of a CMS-formatted disk that contains the configuration file. This is usually the CMS user's `A`{.literal} disk.

    For example: `CMSDASD=191`{.literal}

`CMSCONFFILE=`{.literal}*`configuration_file`{.literal}*

:   Where *configuration_file* is the name of the configuration file. **This value must be specified in lower case.** It is specified in a Linux file name format: *`CMS_file_name`{.literal}*`.`{.literal}*`CMS_file_type`{.literal}*.

    The CMS file `REDHAT CONF`{.literal} is specified as `redhat.conf`{.literal}. The CMS file name and the file type can each be from one to eight characters that follow the CMS conventions.

    For example: `CMSCONFFILE=redhat.conf`{.literal}

#### [8.8.3. Installation network, DASD and FCP parameters](#installation-network-dasd-and-fcp-parameters) {#installation-network-dasd-and-fcp-parameters .title}

You can use these parameters to automatically configure the preliminary network, and define in the CMS configuration file. Additionally, you can use these parameters in a CMS configuration file. All other parameters in other sections must be specified in the parameter file.

`NETTYPE="`{.literal}*`type`{.literal}*`"`{.literal}

:   Where *type* must be one of the following: `qeth`{.literal}, `lcs`{.literal}, or `ctc`{.literal}. The default is `qeth`{.literal}.

    Choose `qeth`{.literal} for:

    -   OSA-Express features

    -   HiperSockets

    -   Virtual connections on z/VM, including VSWITCH and Guest LAN

        Select `ctc`{.literal} for:

    -   Channel-to-channel network connections

`SUBCHANNELS="`{.literal}*`device_bus_IDs`{.literal}*`"`{.literal}

:   Where *device_bus_IDs* is a comma-separated list of two or three device bus IDs. The IDs must be specified in lowercase.

    Provides required device bus IDs for the various network interfaces:

    ``` {.language-plaintext tabindex="-1"}
    qeth: SUBCHANNELS="read_device_bus_id,write_device_bus_id,data_device_bus_id"
    lcs or ctc: SUBCHANNELS="read_device_bus_id,write_device_bus_id"
    ```

    For example (a sample qeth SUBCHANNEL statement):

    ``` {.language-plaintext tabindex="-1"}
    SUBCHANNELS="0.0.f5f0,0.0.f5f1,0.0.f5f2"
    ```

`PORTNO="`{.literal}*`portnumber`{.literal}*`"`{.literal}
:   You can add either `PORTNO="0"`{.literal} (to use port 0) or `PORTNO="1"`{.literal} (to use port 1 of OSA features with two ports per CHPID).

`LAYER2="`{.literal}*`value`{.literal}*`"`{.literal}

:   Where *value* can be `0`{.literal} or `1`{.literal}.

    Use `LAYER2="0"`{.literal} to operate an OSA or HiperSockets device in layer 3 mode (`NETTYPE="qeth"`{.literal}). Use `LAYER2="1"`{.literal} for layer 2 mode. For virtual network devices under z/VM this setting must match the definition of the GuestLAN or VSWITCH to which the device is coupled.

    To use network services that operate on layer 2 (the Data Link Layer or its MAC sublayer) such as DHCP, layer 2 mode is a good choice.

    The qeth device driver default for OSA devices is now layer 2 mode. To continue using the previous default of layer 3 mode, set `LAYER2="0"`{.literal} explicitly.

`VSWITCH="`{.literal}*`value`{.literal}*`"`{.literal}

:   Where *value* can be `0`{.literal} or `1`{.literal}.

    Specify `VSWITCH="1"`{.literal} when connecting to a z/VM VSWITCH or GuestLAN, or `VSWITCH="0"`{.literal} (or nothing at all) when using directly attached real OSA or directly attached real HiperSockets.

`MACADDR="`{.literal}*`MAC_address`{.literal}*`"`{.literal}

:   If you specify `LAYER2="1"`{.literal} and `VSWITCH="0"`{.literal}, you can optionally use this parameter to specify a MAC address. Linux requires six colon-separated octets as pairs of lower case hex digits - for example, `MACADDR=62:a3:18:e7:bc:5f`{.literal}. This is different from the notation used by z/VM.

    If you specify `LAYER2="1"`{.literal} and `VSWITCH="1"`{.literal}, you must not specify the `MACADDR`{.literal}, because z/VM assigns a unique MAC address to virtual network devices in layer 2 mode.

`CTCPROT="`{.literal}*`value`{.literal}*`"`{.literal}

:   Where *value* can be `0`{.literal}, `1`{.literal}, or `3`{.literal}.

    Specifies the CTC protocol for `NETTYPE="ctc"`{.literal}. The default is `0`{.literal}.

`HOSTNAME="`{.literal}*`string`{.literal}*`"`{.literal}
:   Where *string* is the host name of the newly-installed Linux instance.

`IPADDR="`{.literal}*`IP`{.literal}*`"`{.literal}
:   Where *IP* is the IP address of the new Linux instance.

`NETMASK="`{.literal}*`netmask`{.literal}*`"`{.literal}

:   Where *netmask* is the netmask.

    The netmask supports the syntax of a prefix integer (from 1 to 32) as specified in IPv4 *classless interdomain routing* (CIDR). For example, you can specify `24`{.literal} instead of `255.255.255.0`{.literal}, or `20`{.literal} instead of `255.255.240.0`{.literal}.

`GATEWAY="`{.literal}*`gw`{.literal}*`"`{.literal}
:   Where *gw* is the gateway IP address for this network device.

`MTU="`{.literal}*`mtu`{.literal}*`"`{.literal}
:   Where *mtu* is the *Maximum Transmission Unit* (MTU) for this network device.

`DNS="`{.literal}*`server1:server2:additional_server_terms:serverN`{.literal}*`"`{.literal}

:   Where \"*server1:server2:additional_server_terms:serverN*\" is a list of DNS servers, separated by colons. For example:

    ``` {.language-plaintext tabindex="-1"}
    DNS="10.1.2.3:10.3.2.1"
    ```

`SEARCHDNS="`{.literal}*`domain1:domain2:additional_dns_terms:domainN`{.literal}*`"`{.literal}

:   Where \"*domain1:domain2:additional_dns_terms:domainN*\" is a list of the search domains, separated by colons. For example:

    ``` {.language-plaintext tabindex="-1"}
    SEARCHDNS="subdomain.domain:domain"
    ```

    You only need to specify `SEARCHDNS=`{.literal} if you specify the `DNS=`{.literal} parameter.

`DASD=`{.literal}

:   Defines the DASD or range of DASDs to configure for the installation.

    The installation program supports a comma-separated list of device bus IDs, or ranges of device bus IDs with the optional attributes `ro`{.literal}, `diag`{.literal}, `erplog`{.literal}, and `failfast`{.literal}. Optionally, you can abbreviate device bus IDs to device numbers with leading zeros stripped. Any optional attributes should be separated by colons and enclosed in parentheses. Optional attributes follow a device bus ID or a range of device bus IDs.

    The only supported global option is `autodetect`{.literal}. This does not support the specification of non-existent DASDs to reserve kernel device names for later addition of DASDs. Use persistent DASD device names such as `/dev/disk/by-path/name`{.literal} to enable transparent addition of disks later. Other global options such as `probeonly`{.literal}, `nopav`{.literal}, or `nofcx`{.literal} are not supported by the installation program.

    Only specify those DASDs that need to be installed on your system. All unformatted DASDs specified here must be formatted after a confirmation later on in the installation program.

    Add any data DASDs that are not needed for the root file system or the `/boot`{.literal} partition after installation.

    For example:

    ``` {.language-plaintext tabindex="-1"}
    DASD="eb1c,0.0.a000-0.0.a003,eb10-eb14(diag),0.0.ab1c(ro:diag)"
    ```

`FCP_`{.literal}*`n`{.literal}*`="`{.literal}*`device_bus_ID`{.literal}*` [`{.literal}*`WWPN`{.literal}*` `{.literal}*`FCP_LUN`{.literal}*`]"`{.literal}

:   For FCP-only environments, remove the `DASD=`{.literal} option from the CMS configuration file to indicate no DASD is present.

    ``` {.language-plaintext tabindex="-1"}
    FCP_n="device_bus_ID [WWPN FCP_LUN]"
    ```

    Where:

    -   *n* is typically an integer value (for example `FCP_1`{.literal} or `FCP_2`{.literal}) but could be any string with alphabetic or numeric characters or underscores.

    -   *device_bus_ID* specifies the device bus ID of the FCP device representing the *host bus adapter* (HBA) (for example `0.0.fc00`{.literal} for device fc00).

    -   *WWPN* is the world wide port name used for routing (often in conjunction with multipathing) and is as a 16-digit hex value (for example `0x50050763050b073d`{.literal}).

    -   *FCP_LUN* refers to the storage logical unit identifier and is specified as a 16-digit hexadecimal value padded with zeroes to the right (for example `0x4020400100000000`{.literal}).

        Note

        Provide a target WWPN and `FCP_LUN`{.literal} if the zFCP device is not configured in NPIV mode. They are also required when auto LUN scanning is disabled with `zfcp.allow_lun_scan=0`{.literal} or when installing RHEL-9.0 or older releases. Otherwise, only the `device_bus_ID`{.literal} value is mandatory.

    -   These variables can be used on systems with FCP devices to activate FCP LUNs such as SCSI disks. Additional FCP LUNs can be activated during the installation interactively or by means of a Kickstart file. An example value looks similar to the following:

        ``` {.language-plaintext tabindex="-1"}
        FCP_1="0.0.fc00 0x50050763050b073d 0x4020400100000000"
        FCP_2="0.0.4000"
        ```

        Each of the values used in the FCP parameters (for example `FCP_1`{.literal} or `FCP_2`{.literal}) are site-specific and are normally supplied by the FCP storage administrator.

#### [8.8.4. Parameters for kickstart installations on 64-bit IBM Z](#parameters-for-kickstart-installations-on-64-bit-ibm-z) {#parameters-for-kickstart-installations-on-64-bit-ibm-z .title}

The following parameters can be defined in a parameter file but do not work in a CMS configuration file.

`inst.ks=`{.literal}*`URL`{.literal}*
:   References a Kickstart file, which usually resides on the network for Linux installations on 64-bit IBM Z. Replace *URL* with the full path including the file name of the Kickstart file. This parameter activates automatic installation with Kickstart.

`inst.cmdline`{.literal}
:   This requires installation with a Kickstart file that answers all questions, because the installation program does not support interactive user input in cmdline mode. Ensure that your Kickstart file contains all required parameters before you use the `inst.cmdline`{.literal} option. If a required command is missing, the installation will fail.

#### [8.8.5. Additional Boot Parameters for 64-bit IBM Z](#miscellaneous-parameters-on-64-bit-ibm-z) {#additional-boot-parameters-for-64-bit-ibm-z .title}

You can define the following parameters in a parameter file but they do not work in a CMS configuration file.

`rd.live.check`{.literal}
:   Turns on testing of an ISO-based installation source; for example, when using `inst.repo=`{.literal} with an ISO on local disk or mounted with NFS.

`inst.nompath`{.literal}
:   Disables support for multipath devices.

`inst.proxy=[`{.literal}*`protocol`{.literal}*`://][`{.literal}*`username`{.literal}*`[:`{.literal}*`password`{.literal}*`]@]`{.literal}*`host`{.literal}*`[:`{.literal}*`port`{.literal}*`]`{.literal}
:   Specify a proxy to use with installation over HTTP, HTTPS or FTP.

`inst.rescue`{.literal}
:   Boot into a rescue system running from a RAM disk that can be used to fix and restore an installed system.

`inst.stage2=`{.literal}*`URL`{.literal}*

:   Specifies a path to a tree containing `install.img`{.literal}, not to the `install.img`{.literal} directly. Otherwise, it follows the same syntax as `inst.repo=`{.literal}. If `inst.stage2`{.literal} is specified, it typically takes precedence over other methods of finding `install.img`{.literal}. However, if **Anaconda** finds `install.img`{.literal} on local media, the `inst.stage2`{.literal} URL will be ignored.

    If `inst.stage2`{.literal} is not specified and `install.img`{.literal} cannot be found locally, **Anaconda** looks to the location given by `inst.repo=`{.literal} or `method=`{.literal}.

    If only `inst.stage2=`{.literal} is given without `inst.repo=`{.literal} or `method=`{.literal}, **Anaconda** uses whatever repos the installed system would have enabled by default for installation.

    Use the option multiple times to specify multiple HTTP, HTTPS or FTP sources. The HTTP, HTTPS or FTP paths are then tried sequentially until one succeeds:

    ``` {.language-plaintext tabindex="-1"}
    inst.stage2=http://hostname/path_to_install_tree/
    inst.stage2=http://hostname/path_to_install_tree/
    inst.stage2=http://hostname/path_to_install_tree/
    ```

`inst.syslog=`{.literal}*`IP/hostname`{.literal}*`[:`{.literal}*`port`{.literal}*`]`{.literal}
:   Sends log messages to a remote syslog server.

The boot parameters described here are the most useful for installations and trouble shooting on 64-bit IBM Z, but only a subset of those that influence the installation program.

#### [8.8.6. Sample parameter file and CMS configuration file](#sample-parameter-file-and-cms-configuration-file) {#sample-parameter-file-and-cms-configuration-file .title}

To change the parameter file, begin by extending the shipped `generic.prm`{.literal} file.

Example of `generic.prm`{.literal} file:

``` {.language-plaintext tabindex="-1"}
ro ramdisk_size=40000 cio_ignore=all,!condev
CMSDASD="191" CMSCONFFILE="redhat.conf"
inst.rdp
inst.repo=http://example.com/path/to/dvd-contents
```

Example of `redhat.conf`{.literal} file configuring a QETH network device (pointed to by `CMSCONFFILE`{.literal} in `generic.prm`{.literal}):

``` {.language-plaintext tabindex="-1"}
NETTYPE="qeth"
SUBCHANNELS="0.0.0600,0.0.0601,0.0.0602"
PORTNAME="FOOBAR"
PORTNO="0"
LAYER2="1"
MACADDR="02:00:be:3a:01:f3"
HOSTNAME="foobar.systemz.example.com"
IPADDR="192.168.17.115"
NETMASK="255.255.255.0"
GATEWAY="192.168.17.254"
DNS="192.168.17.1"
SEARCHDNS="systemz.example.com:example.com"
DASD="200-203"
```

## [Chapter 9. Automated installation workflow](#automated-installation-workflow) {#chapter-9.-automated-installation-workflow .title}

You can perform the Kickstart installations by using a local DVD, a local disk, or an NFS, FTP, HTTP, or HTTPS server.

The high level overview of Kickstart usage is as follows:

1.  Create a Kickstart file. You can write it by hand, copy a Kickstart file saved after a manual installation, or use an online generator tool to create the file, and edit it afterward.
2.  Make the Kickstart file available to the installation program on removable media, a disk or a network location by using an HTTP(S), FTP, or NFS server.
3.  Create the boot medium that is used to begin the installation.
4.  Make the installation source available to the installation program.
5.  Start the installation by using the boot medium and the Kickstart file.

If the Kickstart file contains all mandatory commands and sections, the installation starts and finishes automatically. If one or more of these mandatory parts are missing, user input is required to start the automated installation. If a critical error occurs, the installation is canceled and the user is informed about the error.

**Additional resources**

-   [Creating Kickstart files](#creating-kickstart-files "Chapter 10. Creating Kickstart files")
-   [Creating installation sources for Kickstart installations](#preparing-network-based-repositories "Chapter 5. Preparing network-based repositories")
-   [Starting Kickstart installations](#starting-kickstart-installations "Chapter 13. Starting Kickstart installations")
-   [Adding the Kickstart file to a UEFI HTTP or PXE installation source](#adding-the-kickstart-file-to-a-uefi-http-or-pxe-installation-source "Chapter 11. Adding the Kickstart file to a UEFI HTTP or PXE installation source")
-   [Making Kickstart files available to the RHEL installer](#semi-automated-installations-making-kickstart-files-available-to-the-rhel-installer "Chapter 12. Semi-automated installations: Making Kickstart files available to the RHEL installer")

## [Chapter 10. Creating Kickstart files](#creating-kickstart-files) {#chapter-10.-creating-kickstart-files .title}

You can create a Kickstart file by using the following different methods:

-   Use the online Kickstart configuration tool.
-   Copy the Kickstart file created as a result of installation.
-   Write the entire Kickstart file manually.
-   Convert the Red Hat Enterprise Linux 9 Kickstart file for Red Hat Enterprise Linux 10 installation.
-   In case of virtual and cloud environments, create a custom system image by using Image Builder.

Some highly specific installation options can be configured only by manual editing of the Kickstart file.

### [10.1. Creating a Kickstart file with the Kickstart Generator](#creating-a-kickstart-file-with-the-kickstart-generator) {#creating-a-kickstart-file-with-the-kickstart-generator .title}

Use the Red Hat Customer Portal Kickstart Generator to create automated installation files through a web-based interface. The Kickstart generator simplifies the creation of Kickstart files for automated RHEL deployments without requiring manual file editing or syntax knowledge.

**Prerequisites**

-   You have a Red Hat Customer Portal account and an active Red Hat subscription.

**Procedure**

1.  Open the [Kickstart generator](https://access.redhat.com/labsinfo/kickstartconfig) lab.

2.  Click the **Go to Application** button to the left of the heading and wait for the next page to load.

3.  Select **Red Hat Enterprise Linux 10** in the drop-down menu and wait for the page to update.

4.  Describe the system to be installed by using the fields in the form.

    You can use the links on the left side of the form to quickly navigate between sections of the form.

5.  To download the generated Kickstart file, click the red **Download** button at the top of the page.

    Your web browser saves the file.

6.  Install the **pykickstart** package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pykickstart
    ```

7.  Run `ksvalidator`{.literal} on your Kickstart file.

    ``` {.language-plaintext tabindex="-1"}
    $ ksvalidator -v RHEL10 /path/to/kickstart.ks
    ```

    Replace */path/to/kickstart.ks* with the path to the Kickstart file you want to verify.

    The validation tool cannot guarantee the installation will be successful. It ensures only that the syntax is correct and that the file does not include deprecated options. It does not attempt to validate the `%pre`{.literal}, `%post`{.literal} and `%packages`{.literal} sections of the Kickstart file.

### [10.2. Creating a Kickstart file from a manual installation](#creating-a-kickstart-file-from-a-manual-installation) {#creating-a-kickstart-file-from-a-manual-installation .title}

You can use the Kickstart file created by a manual installation of Red Hat Enterprise Linux. After a graphical installation completes, all choices made during the installation are saved into a Kickstart file named `anaconda-ks.cfg`{.literal}. This file is located in the `/root/`{.literal} directory on the installed system.

Use the `anaconda-ks.cfg`{.literal} file to reproduce the installation in the same way as before. Alternatively, copy the file, make any changes you need, and use the resulting configuration file for further installations.

**Procedure**

1.  Install RHEL. For more details, see [Interactively installing RHEL from installation media](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/index).

    During the installation, create a user with administrator privileges.

2.  Finish the installation and reboot into the installed system.

3.  Log into the system with the administrator account.

4.  Copy the file `/root/anaconda-ks.cfg`{.literal} to a location of your choice. The file contains information about users and passwords.

    -   To display the file contents at the command line:

        ``` {.language-plaintext tabindex="-1"}
        # cat /root/anaconda-ks.cfg
        ```

        You can copy the output and save to another file of your choice.

    -   To copy the file to another location, use the file manager. Remember to change permissions on the copy, so that the file can be read by non-root users.

5.  Install the **pykickstart** package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pykickstart
    ```

6.  Run `ksvalidator`{.literal} on your Kickstart file.

    ``` {.language-plaintext tabindex="-1"}
    $ ksvalidator -v RHEL10 /path/to/kickstart.ks
    ```

    Replace */path/to/kickstart.ks* with the path to the Kickstart file you want to verify.

    Important

    The validation tool cannot guarantee the installation will be successful. It ensures only that the syntax is correct and that the file does not include deprecated options. It does not attempt to validate the `%pre`{.literal}, `%post`{.literal} and `%packages`{.literal} sections of the Kickstart file.

### [10.3. Converting a Kickstart file from previous RHEL installation](#converting-a-kickstart-file-from-previous-rhel-installation) {#converting-a-kickstart-file-from-previous-rhel-installation .title}

You can use the Kickstart Converter tool to convert a RHEL 8 Kickstart file for use with RHEL 9. You can also convert a RHEL 9 Kickstart file for use with RHEL 10.

**Procedure**

-   After you prepare your kickstart file, install the **pykickstart** package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pykickstart
    ```

-   Run `ksvalidator`{.literal} on your Kickstart file.

    ``` {.language-plaintext tabindex="-1"}
    $ ksvalidator -v RHEL10 /path/to/kickstart.ks
    ```

    Replace */path/to/kickstart.ks* with the path to the Kickstart file you want to verify.

    Important

    The validation tool cannot guarantee the installation will be successful. It ensures only that the syntax is correct and that the file does not include deprecated options. It does not attempt to validate the `%pre`{.literal}, `%post`{.literal} and `%packages`{.literal} sections of the Kickstart file.

**Additional resources**

-   [Kickstart converter](https://access.redhat.com/labs/kickstartconvert/)

### [10.4. Creating a custom image by using Image Builder](#creating-a-custom-image-using-image-builder) {#creating-a-custom-image-by-using-image-builder .title}

You can use Red Hat Image Builder to create a customized system image for virtual and cloud deployments.

For more information about creating customized images, using Image Builder, see the [*Composing a customized RHEL system image*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/index) document.

## [Chapter 11. Adding the Kickstart file to a UEFI HTTP or PXE installation source](#adding-the-kickstart-file-to-a-uefi-http-or-pxe-installation-source) {#chapter-11.-adding-the-kickstart-file-to-a-uefi-http-or-pxe-installation-source .title}

After your Kickstart file is ready, you can make it available for the installation on the destination system.

### [11.1. Sharing the installation files on an NFS server](#sharing-the-installation-files-on-an-nfs-server) {#sharing-the-installation-files-on-an-nfs-server .title}

You can store Kickstart files on an NFS server to enable automated installations across multiple systems. It eliminates the need for physical media and provides centralized management of installation configurations for efficient system deployment over network file sharing.

**Prerequisites**

-   You have administrator-level access to a server with Red Hat Enterprise Linux 10 on the local network.
-   The system to be installed can connect to the server.

Important

Ensure that you use different paths in `inst.ks`{.literal} and `inst.repo`{.literal}. When using NFS to host the Kickstart, you cannot use the same nfs share to host the installation source.

**Procedure**

1.  Install the `nfs-utils`{.literal} package by running the following command as root:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install nfs-utils
    ```

2.  Copy the Kickstart file to a directory on the NFS server.

3.  Open the `/etc/exports`{.literal} file by using a text editor and add a line with the following syntax:

    ``` {.language-plaintext tabindex="-1"}
    /exported_directory/ clients
    ```

    Replace */exported_directory/* with the full path to the directory holding the Kickstart file. Instead of *clients*, use the host name or IP address of the computer to be installed from this NFS server. You can also specify a subnetwork for multiple computers. Use an asterisk sign (`*`{.literal}) to allow any computer with network access to the NFS server to use the ISO image. See the *exports(5)* man page for detailed information about the format of this field. A basic configuration that makes the `/nfs/rhel10-kickstart/`{.literal} directory available as read-only to all clients is:

    ``` {.language-plaintext tabindex="-1"}
    /nfs/rhel10-kickstart/ *
    ```

4.  Enable the NFS service in firewalld.

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service nfs
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=mountd
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=rpc-bind
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

5.  Save the `/etc/exports`{.literal} file and exit the text editor.

6.  Start the nfs service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now nfs-server.service
    ```

    If the service was running before you changed the `/etc/exports`{.literal} file, enter the following command, in order for the running NFS server to reload its configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload nfs-server.service
    ```

    The Kickstart file is now accessible over NFS and ready to be used for installation.

    Note

    When specifying the Kickstart source, use `nfs:`{.literal} as the protocol, the server's host name or IP address, the colon sign (`:`{.literal}), and the path inside the directory holding the file. For example, if the server's host name is `myserver.example.com`{.literal} and you have saved the file in `/nfs/rhel10-kickstart/my-ks.cfg`{.literal}, specify `inst.ks=nfs:myserver.example.com:/nfs/rhel10-kickstart/my-ks.cfg`{.literal} as the installation source boot option.

**Additional resources**

-   [Preparing a remote installation by using RDP](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/index#remote-desktop-protocol-overview)

### [11.2. Sharing the installation files on an HTTP or HTTPS server](#sharing-the-installation-files-on-an-http-or-https-server) {#sharing-the-installation-files-on-an-http-or-https-server .title}

You can store Kickstart files on an HTTP or HTTPS server to enable automated installations across multiple systems. It eliminates the need for physical media and provides centralized management of installation configurations for efficient system deployment.

**Prerequisites**

-   You have administrator-level access to a server with Red Hat Enterprise Linux 10 on the local network.
-   The system to be installed can connect to the server.

**Procedure**

1.  To store the Kickstart file on an HTTP, install the `httpd`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install httpd
    ```

2.  Optional: To store the Kickstart file on an HTTPS, install `httpd`{.literal} and `mod_ssl`{.literal} packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install httpd mod_ssl
    ```

    Important

    If you use an HTTPS server with a self-signed certificate, you must boot the installation program with the `inst.noverifyssl`{.literal} option.

3.  Copy the Kickstart file to the HTTP(S) server into a subdirectory of the `/var/www/html/`{.literal} directory.

4.  Enable the http service in firewalld.

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=http
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

5.  Optional: Enable the `https`{.literal} service in firewalld:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=https
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

6.  Start the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now httpd.service
    ```

    The Kickstart file is now accessible and ready to be used for installation.

    When specifying the location of the Kickstart file, use `http://`{.literal} or `https://`{.literal} as the protocol. Specify the server's host name or IP address and the path of the Kickstart file relative to the HTTP server root. For example, if you are using HTTP, the server's host name is `myserver.example.com`{.literal}, and you have copied the Kickstart file as `/var/www/html/rhel10-install/my-ks.cfg`{.literal}, specify `http://myserver.example.com/rhel10-install/my-ks.cfg`{.literal} as the file location.

**Additional resources**

-   [Deploying Web Servers and Proxies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/index)
-   [Configuring and using Database Servers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_database_servers/index)

### [11.3. Sharing the installation files on an FTP server](#sharing-the-installation-files-on-an-ftp-server) {#sharing-the-installation-files-on-an-ftp-server .title}

You can store Kickstart files on an FTP server to enable automated installations across multiple systems. It eliminates the need for physical media and provides centralized management of installation configurations for efficient system deployment by using the FTP protocol.

**Prerequisites**

-   You have administrator-level access to a server with Red Hat Enterprise Linux 10 on the local network.
-   The system to be installed can connect to the server.

**Procedure**

1.  Install the `vsftpd`{.literal} package by running the following command as root:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install vsftpd
    ```

2.  Open and edit the `/etc/vsftpd/vsftpd.conf`{.literal} configuration file in a text editor.

    a.  Change the line `anonymous_enable=NO`{.literal} to `anonymous_enable=YES`{.literal}

    b.  Change the line `write_enable=YES`{.literal} to `write_enable=NO`{.literal}.

    c.  Add lines `pasv_min_port=`{.literal}*`min_port`{.literal}* and `pasv_max_port=`{.literal}*`max_port`{.literal}*. Replace *`min_port`{.literal}* and *`max_port`{.literal}* with the port number range used by the FTP server in passive mode, for example, `10021`{.literal} and `10031`{.literal}.

        This step can be necessary in network environments featuring various firewall/NAT setups.

    d.  Optional: Add custom changes to your configuration. For available options, see the **vsftpd.conf(5)** man page. This procedure assumes that default options are used.

3.  Configure the firewall to allow the FTP port and port range from the previous step:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-port min_port-max_port/tcp --permanent
    ```

    Replace *min_port*-*max_port* with the port numbers you entered into the `/etc/vsftpd/vsftpd.conf`{.literal} configuration file.

4.  Configure the firewall to allow FTP service.

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-service ftp --permanent
    ```

5.  Reload the firewall to apply the new rules.

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

6.  Copy the Kickstart file to the FTP server into the `/var/ftp/`{.literal} directory or its subdirectory.

7.  Ensure that the correct SELinux context and access mode is set on the file:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -r /var/ftp/your-kickstart-file.ks
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chmod 444 /var/ftp/your-kickstart-file.ks
    ```

8.  Start the `vsftpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now vsftpd.service
    ```

    If the service was running before you changed the `/etc/vsftpd/vsftpd.conf`{.literal} file, restart the service to load the edited file:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart vsftpd.service
    ```

    The Kickstart file is now accessible and ready to be used for installations by systems on the same network.

    Note

    When configuring the installation source, use `ftp://`{.literal} as the protocol, the server's host name or IP address, and the path of the Kickstart file, relative to the FTP server root. For example, if the server's host name is `myserver.example.com`{.literal} and you have copied the file to `/var/ftp/my-ks.cfg`{.literal}, specify `ftp://myserver.example.com/my-ks.cfg`{.literal} as the installation source.

## [Chapter 12. Semi-automated installations: Making Kickstart files available to the RHEL installer](#semi-automated-installations-making-kickstart-files-available-to-the-rhel-installer) {#chapter-12.-semi-automated-installations-making-kickstart-files-available-to-the-rhel-installer .title}

After your Kickstart file is ready, you can make it available for installation on the destination system.

### [12.1. Sharing the installation files on a local volume](#sharing-the-installation-files-on-a-local-volume) {#sharing-the-installation-files-on-a-local-volume .title}

You can store Kickstart files on a local storage volume to enable automated installations without network dependencies. It is ideal for isolated environments or systems where network access is limited, providing a portable solution for unattended RHEL deployments.

**Prerequisites**

-   You have a drive that can be moved to the machine to be installed, such as a USB stick.
-   The drive contains a partition that can be read by the installation program. The supported types are `ext2`{.literal}, `ext3`{.literal}, `ext4`{.literal}, `xfs`{.literal}, and `fat`{.literal}.
-   The drive is connected to the system and its volumes are mounted.

**Procedure**

1.  List volume information and note the UUID of the volume to which you want to copy the Kickstart file.

    ``` {.language-plaintext tabindex="-1"}
    # lsblk -l -p -o name,rm,ro,hotplug,size,type,mountpoint,uuid
    ```

2.  Navigate to the file system on the volume.

3.  Copy the Kickstart file to this file system.

4.  Make a note of the string to use later with the `inst.ks=`{.literal} option. This string is in the form `hd:UUID=`{.literal}*`volume-UUID`{.literal}*`:`{.literal}*`path/to/kickstart-file.cfg`{.literal}*. Note that the path is relative to the file system root, not to the `/`{.literal} root of file system hierarchy. Replace *volume-UUID* with the UUID you noted earlier from the output of `lsblk`{.literal}.

5.  Unmount all drive volumes:

    ``` {.language-plaintext tabindex="-1"}
    # umount /dev/xyz ...
    ```

    (add all the volumes to the command, separated by spaces.)

### [12.2. Sharing installation files on a local volume for auto-detection](#sharing-installation-files-on-a-local-volume-for-auto-detection) {#sharing-installation-files-on-a-local-volume-for-auto-detection .title}

You can configure a local storage volume with a specially named and labeled Kickstart file for automatic detection during installation. It enables completely automated installations without manual intervention or network dependencies, making it ideal for unattended deployments.

**Prerequisites**

-   You have a drive that can be moved to the machine to be installed, such as a USB stick.
-   The drive contains a partition that can be read by the installation program. The supported types are `ext2`{.literal}, `ext3`{.literal}, `ext4`{.literal}, `xfs`{.literal}, and `fat`{.literal}.
-   The drive is connected to the system and its volumes are mounted.

**Procedure**

1.  List volume information to which you want to copy the Kickstart file.

    ``` {.language-plaintext tabindex="-1"}
    # lsblk -l -p
    ```

2.  Navigate to the file system on the volume.

3.  Copy the Kickstart file into the root of this file system.

4.  Rename the Kickstart file to `ks.cfg`{.literal}.

5.  Rename the volume as `OEMDRV`{.literal}:

    -   For `ext2`{.literal}, `ext3`{.literal}, and `ext4`{.literal} file systems:

        ``` {.language-plaintext tabindex="-1"}
        # e2label /dev/xyz OEMDRV
        ```

    -   For the XFS file system:

        ``` {.language-plaintext tabindex="-1"}
        # xfs_admin -L OEMDRV /dev/xyz
        ```

    Replace */dev/xyz* with the path to the volume's block device.

6.  Unmount all drive volumes:

    ``` {.language-plaintext tabindex="-1"}
    # umount /dev/xyz ...
    ```

    (add all the volumes to the command, separated by spaces.)

## [Chapter 13. Starting Kickstart installations](#starting-kickstart-installations) {#chapter-13.-starting-kickstart-installations .title}

You can start Kickstart installations in multiple ways:

-   Automatically by editing the boot options in network boot configuration.
-   Automatically by providing the file on a volume with a specific name.
-   Manually by providing inst.ks= kernel command line option in bootloader menu.

You can register RHEL using the Red Hat Content Delivery Network (CDN). CDN is a geographically distributed series of web servers. These servers provide, for example, packages and updates to RHEL hosts with a valid subscription.

During the installation, registering and installing RHEL from the CDN offers the following benefits:

-   Use the latest packages for an up-to-date system immediately after installation and
-   Integrated support for connecting to Red Hat Lightspeed and enabling System Purpose.

### [13.1. Starting an automated Kickstart installation over PXE or HTTP boot](#starting-an-automated-kickstart-installation-over-pxe-or-http-boot) {#starting-an-automated-kickstart-installation-over-pxe-or-http-boot .title}

You can completely automate a Kickstart installation, including the boot process, using a PXE server. When you configure the PXE server or UEFI HTTP boot, add the boot option into the boot loader configuration file to start the installation automatically.

AMD64, Intel 64, 64-bit ARM, and IBM Power® servers can boot using a PXE server. This procedure is intended as a general reference because the detailed steps differ based on your system's architecture. Not all options are available on all architectures. For example, you cannot use a PXE boot on 64-bit IBM Z®.

**Prerequisites**

-   You have a Kickstart file ready in a location accessible from the system to be installed.
-   You have a PXE server that can be used to boot the system and begin the installation and an HTTP server configured for UEFI HTTP boot.

**Procedure**

1.  Open the boot loader configuration file on your PXE server, and add the `inst.ks=`{.literal} boot option to the appropriate line. The name of the file and its syntax depends on your system's architecture and hardware:

    a.  On AMD64 and Intel 64 systems with BIOS, the file name can be either default or based on your system's IP address. In this case, add the `inst.ks=`{.literal} option to the append line in the installation entry. A sample append line in the configuration file looks similar to the following:

        ``` {.language-plaintext tabindex="-1"}
        append initrd=initrd.img inst.ks=http://192.168.124.2/kickstarts/ks.cfg
        ```

    b.  On systems using the GRUB2 boot loader (AMD64, Intel 64, and 64-bit ARM systems with UEFI firmware and IBM Power Systems servers), the file name will be `grub.cfg`{.literal}. In this file, append the `inst.ks=`{.literal} option to the kernel line in the installation entry. A sample kernel line in the configuration file will look similar to the following:

        ``` {.language-plaintext tabindex="-1"}
        linuxefi /redhat/images/pxeboot/vmlinuz inst.ks=http://192.168.124.2/kickstarts/ks.cfg
        ```

2.  If you want to configure an automated Kickstart installation by using UEFI HTTP boot, locate the bootloader configuration file (grub.cfg) served by the HTTP server. Edit it in a similar way as in step 1.b:

    ``` {.language-plaintext tabindex="-1"}
    linuxefi /redhat/images/pxeboot/vmlinuz inst.ks=http://192.168.124.2/kickstarts/ks.cfg
    ```

3.  Boot the installation from the network server.

    The installation begins now by using the installation options specified in the Kickstart file. If the Kickstart file is valid and contains all required commands, the installation is completely automated.

    Note

    If you have installed a Red Hat Enterprise Linux Beta release, on systems having UEFI Secure Boot enabled, then add the Beta public key to the system's Machine Owner Key (MOK) list.

**Additional resources**

-   [Preparing a PXE installation source](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/index#preparing-a-pxe-installation-source)
-   [Configuring the HTTP server for HTTP boot](#configuring-the-http-server-for-http-boot "6.4. Configuring the HTTP server for HTTP boot")
-   [Sharing the installation files on an HTTP or HTTPS server](#sharing-the-installation-files-on-an-http-or-https-server "11.2. Sharing the installation files on an HTTP or HTTPS server")

### [13.2. Starting an automated Kickstart installation from a local volume](#starting-an-automated-kickstart-installation-from-a-local-volume) {#starting-an-automated-kickstart-installation-from-a-local-volume .title}

You can configure automated Kickstart installations using a local storage volume with a properly labeled and named Kickstart file. It enables unattended installations without network dependencies, making it suitable for isolated environments or systems without network access.

**Prerequisites**

-   You have a volume prepared with [label `OEMDRV`{.literal} and the Kickstart file present in its root as `ks.cfg`{.literal}](#sharing-the-installation-files-on-a-local-volume "12.1. Sharing the installation files on a local volume").
-   A drive containing this volume is available on the system as the installation program boots.

**Procedure**

1.  Boot the system by using a local media (a CD, DVD, or a USB flash drive).

2.  At the boot prompt, specify the required boot options.

    a.  If a required repository is in a network location, you may need to configure the network by using the `ip=`{.literal} option. The installer tries to configure all network devices by using the DHCP protocol by default without this option.

    b.  To access a software source from which necessary packages will be installed, you may need to add the `inst.repo=`{.literal} option. If you do not specify this option, you must specify the installation source in the Kickstart file.

        For more information about installation sources, see [Kickstart commands for installation program configuration and flow control](#kickstart-commands-for-installation-program-configuration-and-flow-control "22.2. Kickstart commands for installation program configuration and flow control").

3.  Start the installation by confirming your added boot options.

    The installation begins now, and the Kickstart file is automatically detected and used to start an automated Kickstart installation.

    Note

    If you have installed a Red Hat Enterprise Linux Beta release, on systems having UEFI Secure Boot enabled, then add the Beta public key to the system's Machine Owner Key (MOK) list. For more information about UEFI Secure Boot and Red Hat Enterprise Linux Beta releases, see the [UEFI Secure Boot and Beta release requirements](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/index#uefi-secure-boot-and-beta-release-requirements).

### [13.3. Booting the installation on IBM Z to install RHEL in an LPAR](#installing-in-an-lpar) {#booting-the-installation-on-ibm-z-to-install-rhel-in-an-lpar .title}

You can boot the installation on IBM Z to install RHEL in an LPAR.

#### [13.3.1. Booting the RHEL installation from an SFTP, FTPS, or FTP server](#booting-the-rhel-installation-from-an-sftp-ftps-or-ftp-server) {#booting-the-rhel-installation-from-an-sftp-ftps-or-ftp-server .title}

You can install RHEL into an LPAR by using an SFTP, FTPS, or FTP server.

**Procedure**

1.  Log in on the IBM Z Hardware Management Console (HMC) or the Support Element (SE) as a user with sufficient privileges to install a new operating system to an LPAR.

2.  On the **Systems** tab, select the mainframe you want to work with, then on the **Partitions** tab select the LPAR to which you want to install.

3.  At the bottom of the screen, under **Daily**, find **Operating System Messages**. Double-click **Operating System Messages** to show the text console on which Linux boot messages appear.

4.  Double-click **Load from Removable Media or Server**.

5.  In the dialog box that follows, select **SFTP/FTPS/FTP Server**, and enter the following information:

    -   **Host Computer** - Host name or IP address of the FTP server you want to install from, for example **ftp.redhat.com**
    -   **User ID** - Your user name on the FTP server. Or, specify anonymous.
    -   **Password** - Your password. Use your email address if you are logging in as anonymous.
    -   **File location (optional)** - Directory on the FTP server holding the Red Hat Enterprise Linux for IBM Z, for example **/rhel/s390x/**.

6.  Click **Continue**.

7.  In the dialog that follows, keep the default selection of **generic.ins** and click **Continue**.

#### [13.3.2. Booting the RHEL installation from a prepared DASD](#booting-the-rhel-installation-from-a-prepared-dasd) {#booting-the-rhel-installation-from-a-prepared-dasd .title}

You can install Red Hat Enterprise Linux into an LPAR by using an already prepared DASD.

**Procedure**

1.  Log in on the IBM Z Hardware Management Console (HMC) or the Support Element (SE) as a user with sufficient privileges to install a new operating system to an LPAR.
2.  On the **Systems** tab, select the mainframe you want to work with, then on the **Partitions** tab select the LPAR to which you want to install.
3.  At the bottom of the screen, under **Daily**, find **Operating System Messages**. Double-click **Operating System Messages** to show the text console on which Linux boot messages appear.
4.  Double-click **Load**.
5.  In the dialog box that follows, select **Normal** as the **Load type**.
6.  As Load **address**, fill in the device number of the DASD.
7.  Click the **OK** button.

#### [13.3.3. Booting the RHEL installation from an FCP-attached SCSI disk](#booting-the-rhel-installation-from-an-fcp-attached-scsi-disk) {#booting-the-rhel-installation-from-an-fcp-attached-scsi-disk .title}

You can install Red Hat Enterprise Linux into an LPAR by using an already prepared FCP attached SCSI disk.

**Procedure**

1.  Log in on the IBM Z Hardware Management Console (HMC) or the Support Element (SE) as a user with sufficient privileges to install a new operating system to an LPAR.
2.  On the **Systems** tab, select the mainframe you want to work with, then on the **Partitions** tab select the LPAR to which you want to install.
3.  At the bottom of the screen, under **Daily**, find **Operating System Messages**. Double-click **Operating System Messages** to show the text console on which Linux boot messages appear.
4.  Double-click **Load**.
5.  In the dialog box that follows, select **SCSI** as the **Load type**.
6.  As **Load address**, fill in the device number of the FCP channel connected with the SCSI disk.
7.  As **World wide port name**, fill in the WWPN of the storage system containing the disk as a 16-digit hexadecimal number.
8.  As **Logical unit number**, fill in the LUN of the disk as a 16-digit hexadecimal number.
9.  Leave the **Boot record logical block address** as **0** and the **Operating system specific load parameters** empty.
10. Click the **OK** button.

### [13.4. Booting the installation on IBM Z to install RHEL in z/VM](#booting-the-installation-on-ibm-z-to-install-rhel-in-zvm) {#booting-the-installation-on-ibm-z-to-install-rhel-in-zvm .title}

When installing under z/VM, you can boot from the `z/VM`{.literal} virtual reader or a DASD or an FCP-attached SCSI disk prepared with the **zipl** boot loader in supported system configurations.

#### [13.4.1. Booting the RHEL installation by using the z/VM Reader](#booting-the-rhel-installation-by-using-the-z-vm-reader) {#booting-the-rhel-installation-by-using-the-zvm-reader .title}

Booting the Red Hat Enterprise Linux installation using the z/VM Reader is designed for IBM Z (s390x) environments. It delivers boot images directly to a virtual machine and enables installation when DASD or FCP boot methods are unavailable or impractical.

**Procedure**

1.  If necessary, add the device containing the z/VM TCP/IP tools to your CMS disk list. For example:

    ``` {.language-plaintext tabindex="-1"}
    cp link tcpmaint 592 592
    acc 592 fm
    ```

    Replace *fm* with any `FILEMODE`{.literal} letter.

2.  For a connection to an FTPS server, enter:

    ``` {.language-plaintext tabindex="-1"}
    ftp <host> (secure
    ```

    Where `host`{.literal} is the host name or IP address of the FTP server that hosts the boot images (`kernel.img`{.literal} and `initrd.img`{.literal}).

3.  Log in and run the following commands. Use the `(repl`{.literal} option if you are overwriting existing `kernel.img`{.literal}, `initrd.img`{.literal}, `generic.prm`{.literal}, or `redhat.exec`{.literal} files:

    ``` {.language-plaintext tabindex="-1"}
    cd /location/of/install-tree/images/
    ascii
    get generic.prm (repl
    get redhat.exec (repl
    locsite fix 80
    binary
    get kernel.img (repl
    get initrd.img (repl
    quit
    ```

4.  Optional: Check whether the files were transferred correctly by using the CMS command `filelist`{.literal} to show the received files and their format. It is important that `kernel.img`{.literal} and `initrd.img`{.literal} have a fixed record length format denoted by F in the Format column and a record length of 80 in the Lrecl column. For example:

    ``` {.language-plaintext tabindex="-1"}
    VMUSER FILELIST A0 V 169 Trunc=169 Size=6 Line=1 Col=1 Alt=0
    ```

    ``` {.language-plaintext tabindex="-1"}
    Cmd Filename Filetype    Fm  Format  Lrecl   Records Blocks  Date    Time
    REDHAT  EXEC        B1  V   22  1   1   4/15/10 9:30:40
    GENERIC PRM     B1  V   44  1   1   4/15/10 9:30:32
    INITRD  IMG     B1  F   80  118545  2316    4/15/10 9:30:25
    KERNEL  IMG     B1  F   80  74541   912 4/15/10 9:30:17
    ```

    Press PF3 to quit filelist and return to the CMS prompt.

5.  Customize boot parameters in `generic.prm`{.literal} as necessary. For details, see [Customizing boot parameters](#customization-of-boot-parameters "8.6. Customization of boot parameters").

    Another way to configure storage and network devices is by using a CMS configuration file. In such a case, add the *`CMSDASD=`{.literal}* and *`CMSCONFFILE=`{.literal}* parameters to `generic.prm`{.literal}.

6.  Finally, run the REXX script redhat.exec to boot the installation program:

    ``` {.language-plaintext tabindex="-1"}
    redhat
    ```

#### [13.4.2. Booting the RHEL installation by using a prepared DASD](#booting-the-rhel-installation-by-using-a-prepared-dasd) {#booting-the-rhel-installation-by-using-a-prepared-dasd .title}

Booting the Red Hat Enterprise Linux installation from a prepared Direct Access Storage Device (DASD) is commonly used on IBM Z (s390x) systems. It ensures a consistent, repeatable installation process and integrates easily into larger provisioning workflows.

**Procedure**

-   Boot from the prepared DASD and select the **zipl** boot menu entry referring to the Red Hat Enterprise Linux installation program. Use a command of the following form:

    ``` {.language-plaintext tabindex="-1"}
    cp ipl DASD_device_number loadparm boot_entry_number
    ```

    Replace *DASD_device_number* with the device number of the boot device, and *boot_entry_number* with the **zipl** configuration menu for this device. For example:

    ``` {.language-plaintext tabindex="-1"}
    cp ipl eb1c loadparm 0
    ```

#### [13.4.3. Booting the installation by using a prepared FCP SCSI disk](#booting-the-installation-by-using-a-prepared-fcp-scsi-disk) {#booting-the-installation-by-using-a-prepared-fcp-scsi-disk .title}

Booting Red Hat Enterprise Linux from a prepared FCP-attached SCSI disk is common on IBM Z (s390x) systems, especially with Fibre Channel Protocol (FCP) storage. Use this method to install RHEL on systems that rely on external SAN storage instead of local DASD devices.

**Procedure**

1.  Configure the SCSI boot loader of z/VM to access the prepared SCSI disk in the FCP Storage Area Network. Select the prepared **zipl** boot menu entry referring to the Red Hat Enterprise Linux installation program. Use a command of the following form:

    ``` {.language-plaintext tabindex="-1"}
    cp set loaddev portname WWPN lun LUN bootprog boot_entry_number
    ```

    Replace *WWPN* with the World Wide Port Name of the storage system and *LUN* with the Logical Unit Number of the disk. The 16-digit hexadecimal numbers must be split into two pairs of eight digits each. For example:

    ``` {.language-plaintext tabindex="-1"}
    cp set loaddev portname 50050763 050b073d lun 40204011 00000000 bootprog 0
    ```

2.  Optional: Confirm your settings with the command:

    ``` {.language-plaintext tabindex="-1"}
    query loaddev
    ```

3.  Boot the FCP device connected with the storage system containing the disk with the following command:

    ``` {.language-plaintext tabindex="-1"}
    cp ipl FCP_device
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    cp ipl fc00
    ```

## [Chapter 14. Consoles and logging during installation](#consoles-and-logging-during-installation) {#chapter-14.-consoles-and-logging-during-installation .title}

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

: Table 14.1. Available tmux windows

Show more

## [Chapter 15. Installing Kernel-64k on ARM by using the command line](#installing-kernel-64k-on-arm-using-the-command-line) {#chapter-15.-installing-kernel-64k-on-arm-by-using-the-command-line .title}

By default, RHEL 10 is distributed with a kernel supporting a 4k page size. The 4k kernel is sufficient for efficient memory usage in smaller environments or small cloud instances. In these cases, the usage of a 64k page kernel is not practical due to space, power, and cost constraints.

You can install the `kernel-64k`{.literal} package by using the command line if you have already installed Red Hat Enterprise Linux on a 64-bit ARM architecture with the default 4k page size kernel.

Important

Do not move between 4k and 64k page size kernels after the initial boot without reinstalling the operating system.

**Procedure**

1.  Open the command line window as the root user, and enter:

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y install kernel-64k
    ```

2.  To set the `kernel-64k`{.literal} as default, enter:

    ``` {.language-plaintext tabindex="-1"}
    # k=$(echo /boot/vmlinuz*64k)
    ```

    ``` {.language-plaintext tabindex="-1"}
    # grubby --set-default=$k \
               --update-kernel=$k \
               --args="crashkernel=2G-:640M"
    ```

3.  Set the system boot order to use RHEL as the default option.

    a.  Obtain the current boot order. For example:

        ``` {.language-plaintext tabindex="-1"}
        # efibootmgr
        ```

        ``` {.language-plaintext tabindex="-1"}
        BootCurrent: 0000
        Timeout: 5 seconds
        BootOrder: 0003,0004,0001,0000,0002,0005
        Boot0000\* Red Hat Enterprise Linux
        ```

    b.  Set the boot order to prioritize RHEL. For example, for the output in the previous step, use the following command:

        ``` {.language-plaintext tabindex="-1"}
        # efibootmgr -o 0000,0001,0002,0003,0004,0005
        ```

4.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

5.  Optional: After reboot, remove the 4k kernel:

    ``` {.language-plaintext tabindex="-1"}
    # dnf remove kernel-core
    ```

    Keeping both versions accidentally can make the 4k kernel default when you update the kernel in future using the `yum update`{.literal} command.

**Verification**

-   To verify the page size, open the command line window and run the following command as any user:

    ``` {.language-plaintext tabindex="-1"}
    $ getconf PAGESIZE
    ```

    ``` {.language-plaintext tabindex="-1"}
    65536
    ```

    The output `65536`{.literal} indicates that the 64k kernel is in use.

-   To verify swap is enabled, enter:

    ``` {.language-plaintext tabindex="-1"}
    $ free
    ```

    ``` {.language-plaintext tabindex="-1"}
                   total        used        free      shared  buff/cache   available
    Mem:        35756352     3677184    34774848       25792      237120    32079168
    Swap:        6504384           0     6504384
    ```

    The total and free columns are non-zero, which indicates the swap is enabled successfully.

## [Chapter 16. Registering your RHEL system](#registering-your-rhel-system) {#chapter-16.-registering-your-rhel-system .title}

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

### [16.1. Registering a system by using the RHC client](#registering-a-system-by-using-the-rhc-client-with-the-default-feature-levels) {#registering-a-system-by-using-the-rhc-client .title}

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

### [16.2. Registering your system using the subscription manager](#registering-your-system-using-the-command-line) {#registering-your-system-using-the-subscription-manager .title}

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

### [16.3. Registering RHEL 10 using the installer GUI](#registering-rhel-using-the-installer-gui) {#registering-rhel-10-using-the-installer-gui .title}

You can register a Red Hat Enterprise Linux by using the RHEL installer GUI to get software updates and access Red Hat services.

**Prerequisites**

-   You have a valid user account on the Red Hat Customer Portal. See the [Create a Red Hat Login page](https://www.redhat.com/wapps/ugc/register.html?_flowId=register-flow&_flowExecutionKey=e1s1).
-   You have a valid Activation Key and Organization ID.

**Procedure**

1.  From the **Installation Summary** screen, under **Software**, click **Connect to Red Hat**.

2.  Authenticate your Red Hat account using the **Account** or **Activation Key** option.

3.  Optional: In the **Set System Purpose** field select the **Role**, **SLA**, and **Usage** attribute that you want to set from the drop-down menu.

    At this point, your Red Hat Enterprise Linux system has been successfully registered.

### [16.4. Registration Assistant](#registration-assistant) {#registration-assistant .title}

Registration Assistant is designed to help you choose the most suitable registration option for your Red Hat Enterprise Linux environment:

-   For assistance with using a username and password to register RHEL with the Subscription Manager client, see the [RHEL registration assistant](https://access.redhat.com/labs/registrationassistant/) on the Customer Portal.
-   For assistance with registering your RHEL system to Red Hat Lightspeed, see the [Red Hat Lightspeed registration assistant](https://console.redhat.com/lightspeed/registration#SIDs=&tags=) on the Hybrid Cloud Console.

### [16.5. Additional resources](#registering-your-rhel-system_165-additional-resources) {#additional-resources .title}

-   [Using an activation key to register a system with Red Hat Subscription Manager](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/getting_started_with_rhel_system_registration/index#proc-reg-rhel-rhc-act-key)
-   [Getting Started with RHEL System Registration](https://docs.redhat.com/documentation/en-us/subscription_central/2023/html/getting_started_with_rhel_system_registration/index)
-   [Red Hat Satellite Documentation](https://docs.redhat.com/en/documentation/red_hat_satellite)

## [Chapter 17. Configuring System Purpose with subscription-manager CLI](#configuring-system-purpose-with-subscription-manager-cli) {#chapter-17.-configuring-system-purpose-with-subscription-manager-cli .title}

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

## [Chapter 18. Post-installation security hardening](#post-installation-security-hardening) {#chapter-18.-post-installation-security-hardening .title}

RHEL is designed with robust security features enabled by default. However, you can enhance its security further through additional hardening measures.

For more information about:

-   Processes and practices for securing RHEL servers and workstations against local and remote intrusion, exploitation, and malicious activity, see [Security hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/index).
-   Control how users and processes interact with the files on the system or control which users perform what actions by mapping them to specific SELinux confined users, see [Using SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/index).
-   Tools and techniques to improve the security of your networks and lower the risks of data breaches and intrusions, see [Securing networks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/index).
-   Packet filters, such as firewalls, that use rules to control incoming, outgoing, and forwarded network traffic, see [Configuring firewalls and packet filters](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/index).

## [Chapter 19. Changing a subscription service](#changing-a-subscription-service) {#chapter-19.-changing-a-subscription-service .title}

To manage the subscriptions, register a RHEL system with either Red Hat Subscription Management Server or Red Hat Satellite Server. If required, you can change the subscription service at a later point.

To change the subscription service under which you are registered, unregister the system from the current service and then register it with a new service.

To receive the system updates, register your system with either of the management servers.

This section contains information about how to unregister your RHEL system from the Red Hat Subscription Management Server and Red Hat Satellite Server.

### [19.1. Prerequisites](#prerequisites) {#prerequisites .title}

You have registered your system with any one of the following:

-   Red Hat Subscription Management Server
-   Red Hat Satellite Server version 6.17

To receive the system updates, register your system with either of the management servers.

### [19.2. Unregistering from Subscription Management Server](#unregistering-from-subscription-management-server) {#unregistering-from-subscription-management-server .title}

You can unregister a RHEL system from Red Hat Subscription Management Server by using a command line and the Subscription Manager user interface.

#### [19.2.1. Unregistering using command line](#unregistering-using-command-line) {#unregistering-using-command-line .title}

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
-   [Registering your system using the command line](#registering-your-system-using-the-command-line "16.2. Registering your system using the subscription manager")

#### [19.2.2. Unregistering by using Subscription Manager user interface](#unregistering-using-subscription-manager-user-interface) {#unregistering-by-using-subscription-manager-user-interface .title}

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

-   [Registering your system using the Subscription Manager User Interface](#registering-your-rhel-system "Chapter 16. Registering your RHEL system")
-   [Using an activation key to register a system with Red Hat Subscription Manager](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/getting_started_with_rhel_system_registration/index#proc-reg-rhel-rhc-act-key)

### [19.3. Unregistering from Satellite Server](#unregistering-from-satellite-server) {#unregistering-from-satellite-server .title}

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

## [Chapter 20. Configuring a Linux instance on 64-bit IBM Z](#configuring-a-linux-instance-on-64-bit-ibm-z) {#chapter-20.-configuring-a-linux-instance-on-64-bit-ibm-z .title}

Perform these common tasks for configuring Red Hat Enterprise Linux on 64-bit IBM Z.

### [20.1. Adding DASDs to a z/VM system](#adding-dasds-to-a-z-vm-system) {#adding-dasds-to-a-zvm-system .title}

Direct Access Storage Devices (DASDs) are a type of storage commonly used with 64-bit IBM Z. This example is how to set a DASD online, format it, and make the change persistent.

Verify that the device is attached or linked to the Linux system if running under z/VM.

``` {.language-plaintext tabindex="-1"}
CP ATTACH EB1C TO *
```

To link a mini disk to which you have access, run the following commands:

``` {.language-plaintext tabindex="-1"}
CP LINK RHEL7X 4B2E 4B2E MR
DASD 4B2E LINKED R/W
```

**Additional resources**

-   [Working with DASDs](https://www.ibm.com/docs/en/linux-on-systems?topic=d-working-dasds-2)

### [20.2. Setting DASDs online dynamically](#setting-dasds-online-dynamically) {#setting-dasds-online-dynamically .title}

You can set DASDs online dynamically to add or activate storage devices without rebooting.

**Procedure**

1.  Use the `cio_ignore`{.literal} utility to remove the DASD from the list of ignored devices and make it visible to Linux:

    ``` {.language-plaintext tabindex="-1"}
    # cio_ignore -r device_number
    ```

    Replace *device_number* with the device number of the DASD. For example:

    ``` {.language-plaintext tabindex="-1"}
    # cio_ignore -r 4b2e
    ```

2.  Set the device online. Use a command of the following form:

    ``` {.language-plaintext tabindex="-1"}
    # chccwdev -e device_number
    ```

    Replace *device_number* with the device number of the DASD. For example:

    ``` {.language-plaintext tabindex="-1"}
    # chccwdev -e 4b2e
    ```

    For instructions on how to set a DASD online persistently, see [Persistently setting DASDs online](#persistently-setting-dasds-online "20.4. Persistently setting DASDs online").

### [20.3. Preparing a new DASD with low-level formatting](#preparing-a-new-dasd-with-low-level-formatting) {#preparing-a-new-dasd-with-low-level-formatting .title}

Once the disk is online, change back to the `/root`{.literal} directory and low-level format the device. This is required only once for a DASD during its entire lifetime.

**Procedure**

1.  Change back to the `/root`{.literal} directory.

    ``` {.language-plaintext tabindex="-1"}
    # cd /root
    ```

    ``` {.language-plaintext tabindex="-1"}
    # dasdfmt -b 4096 -d cdl -p /dev/disk/by-path/ccw-0.0.4b2e
    Drive Geometry: 10017 Cylinders * 15 Heads =  150255 Tracks

    I am going to format the device /dev/disk/by-path/ccw-0.0.4b2e in the following way:
    Device number of device : 0x4b2e
    Labelling device        : yes
    Disk label              : VOL1
    Disk identifier         : 0X4B2E
    Extent start (trk no)   : 0
    Extent end (trk no)     : 150254
    Compatible Disk Layout  : yes
    Blocksize               : 4096

    --->> ATTENTION! <<---
    All data of that device will be lost.
    Type "yes" to continue, no will leave the disk untouched: yes
    cyl    97 of  3338 |#----------------------------------------------|   2%
    ```

2.  When the progress bar reaches the end and the format is complete, **dasdfmt** prints the following output:

    ``` {.language-plaintext tabindex="-1"}
    Rereading the partition table...
    Exiting...
    ```

3.  Use **fdasd** to partition the DASD. You can create up to three partitions on a DASD. In our example here, we create one partition spanning the whole disk:

    ``` {.language-plaintext tabindex="-1"}
    # fdasd -a /dev/disk/by-path/ccw-0.0.4b2e
    ```

    ``` {.language-plaintext tabindex="-1"}
    reading volume label ..: VOL1
    reading vtoc ..........: ok

    auto-creating one partition for the whole disk...
    writing volume label...
    writing VTOC...
    rereading partition table...
    ```

    After a (low-level formatted) DASD is online, it can be used like any other disk under Linux. For example, you can create file systems, LVM physical volumes, or swap space on its partitions, for example `/dev/disk/by-path/ccw-0.0.4b2e-part1`{.literal}. Never use the full DASD device (`dev/dasdb`{.literal}) for anything but the commands `dasdfmt`{.literal} and `fdasd`{.literal}. If you want to use the entire DASD, create a single partition spanning the entire drive, as demonstrated in the `fdasd`{.literal} example.

    To add additional disks later without breaking existing disk entries in, for example, `/etc/fstab`{.literal}, use the persistent device symbolic links under `/dev/disk/by-path/`{.literal}.

### [20.4. Persistently setting DASDs online](#persistently-setting-dasds-online) {#persistently-setting-dasds-online .title}

The earlier instructions described how to activate DASDs dynamically in a running system. However, such changes are not persistent and do not survive a reboot.

Making changes to the DASD configuration persistent in your Linux system depends on whether the DASDs belong to the root file system. Those DASDs required for the root file system need to be activated very early during the boot process by the `initramfs`{.literal} to mount the root file system.

The `cio_ignore`{.literal} commands are handled seamlessly for persistent device configurations and you do not need to free devices from the ignore list manually.

### [20.5. DASDs that are part of the root file system](#dasds-that-are-part-of-the-root-file-system) {#dasds-that-are-part-of-the-root-file-system .title}

The file you have to modify to add DASDs that are part of the root file system has changed in Red Hat Enterprise Linux 8. Rather than editing the `/etc/zipl.conf`{.literal} file, identify the appropriate configuration file and its location by running the relevant commands.

``` {.language-plaintext tabindex="-1"}
# machine_id=$(cat /etc/machine-id)
```

``` {.language-plaintext tabindex="-1"}
# kernel_version=$(uname -r)
```

``` {.language-plaintext tabindex="-1"}
# ls /boot/loader/entries/$machine_id-$kernel_version.conf
```

There is one boot option to activate DASDs early in the boot process: `rd.dasd=`{.literal}. This option takes a Direct Access Storage Device (DASD) adapter device bus identifier. For multiple DASDs, specify the parameter multiple times, or use a comma separated list of bus IDs. To specify a range of DASDs, specify the first and the last bus ID. Following is an example of the `/boot/loader/entries/4ab74e52867b4f998e73e06cf23fd761-4.18.0-80.el8.s390x.conf`{.literal} file for a system that uses physical volumes on partitions of two DASDs for an LVM volume group `vg_devel1`{.literal} that contains a logical volume `lv_root`{.literal} for the root file system.

``` {.language-plaintext tabindex="-1"}
title Red Hat Enterprise Linux (4.18.0-80.el8.s390x) 8.0 (Ootpa)
version 4.18.0-80.el8.s390x
linux /boot/vmlinuz-4.18.0-80.el8.s390x
initrd /boot/initramfs-4.18.0-80.el8.s390x.img
options root=/dev/mapper/vg_devel1-lv_root crashkernel=auto rd.dasd=0.0.0200 rd.dasd=0.0.0207 rd.lvm.lv=vg_devel1/lv_root rd.lvm.lv=vg_devel1/lv_swap cio_ignore=all,!condev rd.znet=qeth,0.0.0a00,0.0.0a01,0.0.0a02,layer2=1,portno=0
id rhel-20181027190514-4.18.0-80.el8.s390x
grub_users $grub_users
grub_arg --unrestricted
grub_class kernel
```

To add another physical volume on a partition of a third DASD with device bus ID `0.0.202b`{.literal}. To do this, add `rd.dasd=0.0.202b`{.literal} to the parameters line of your boot kernel in `/boot/loader/entries/4ab74e52867b4f998e73e06cf23fd761-4.18.0-32.el8.s390x.conf`{.literal}:

``` {.language-plaintext tabindex="-1"}
title Red Hat Enterprise Linux (4.18.0-80.el8.s390x) 8.0 (Ootpa)
version 4.18.0-80.el8.s390x
linux /boot/vmlinuz-4.18.0-80.el8.s390x
initrd /boot/initramfs-4.18.0-80.el8.s390x.img
options root=/dev/mapper/vg_devel1-lv_root crashkernel=auto rd.dasd=0.0.0200 rd.dasd=0.0.0207 rd.dasd=0.0.202b rd.lvm.lv=vg_devel1/lv_root rd.lvm.lv=vg_devel1/lv_swap cio_ignore=all,!condev rd.znet=qeth,0.0.0a00,0.0.0a01,0.0.0a02,layer2=1,portno=0
id rhel-20181027190514-4.18.0-80.el8.s390x
grub_users $grub_users
grub_arg --unrestricted
grub_class kernel
```

Run `zipl`{.literal} to apply the changes of the configuration file for the next IPL:

``` {.language-plaintext tabindex="-1"}
# zipl -V
```

``` {.language-plaintext tabindex="-1"}
Using config file '/etc/zipl.conf'
Using BLS config file '/boot/loader/entries/4ab74e52867b4f998e73e06cf23fd761-4.18.0-80.el8.s390x.conf'
Target device information
  Device..........................: 5e:00
  Partition.......................: 5e:01
  Device name.....................: dasda
  Device driver name..............: dasd
  DASD device number..............: 0201
  Type............................: disk partition
  Disk layout.....................: ECKD/compatible disk layout
  Geometry - heads................: 15
  Geometry - sectors..............: 12
  Geometry - cylinders............: 13356
  Geometry - start................: 24
  File system block size..........: 4096
  Physical block size.............: 4096
  Device size in physical blocks..: 262152
Building bootmap in '/boot'
Building menu 'zipl-automatic-menu'
Adding #1: IPL section '4.18.0-80.el8.s390x' (default)
  initial ramdisk...: /boot/initramfs-4.18.0-80.el8.s390x.img
  kernel image......: /boot/vmlinuz-4.18.0-80.el8.s390x
  kernel parmline...: 'root=/dev/mapper/vg_devel1-lv_root crashkernel=auto rd.dasd=0.0.0200 rd.dasd=0.0.0207 rd.dasd=0.0.202b rd.lvm.lv=vg_devel1/lv_root rd.lvm.lv=vg_devel1/lv_swap cio_ignore=all,!condev rd.znet=qeth,0.0.0a00,0.0.0a01,0.0.0a02,layer2=1,portno=0'
  component address:
    kernel image....: 0x00010000-0x0049afff
    parmline........: 0x0049b000-0x0049bfff
    initial ramdisk.: 0x004a0000-0x01a26fff
    internal loader.: 0x0000a000-0x0000cfff
Preparing boot menu
  Interactive prompt......: enabled
  Menu timeout............: 5 seconds
  Default configuration...: '4.18.0-80.el8.s390x'
Preparing boot device: dasda (0201).
Syncing disks...
Done.
```

### [20.6. DASDs that are not part of the root file system](#dasds-that-are-not-part-of-the-root-file-system) {#dasds-that-are-not-part-of-the-root-file-system .title}

Direct Access Storage Devices (DASDs) that are not part of the root file system, that is, *data disks*, are persistently configured in the `/etc/dasd.conf`{.literal} file. This file contains one DASD per line, where each line begins with the DASD's bus ID.

When adding a DASD to the `/etc/dasd.conf`{.literal} file, use key-value pairs to specify the options for each entry. Separate the key and its value with an equal (=) sign. When adding multiple options, use a space or a tab to separate each option. For example, the `/etc/dasd.conf`{.literal} file contains:

``` {.language-plaintext tabindex="-1"}
0.0.0207
0.0.0200 use_diag=1 readonly=1
```

\+ Changes to `/etc/dasd.conf`{.literal} take effect after a system reboot or after dynamically adding a new DASD. For example, a DASD can be attached under z/VM by changing the system I/O configuration. Alternatively, to activate a DASD that you have added to the `/etc/dasd.conf`{.literal} file, complete the following steps:

1.  Remove the DASD from the list of ignored devices and make it visible using the `cio_ignore`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # cio_ignore -r device_number
    ```

    where *`device_number`{.literal}* is the DASD device number.

    For example, if the device number is `021a`{.literal}, run:

    ``` {.language-plaintext tabindex="-1"}
    # cio_ignore -r 021a
    ```

2.  Activate the DASD by writing to the device's `uevent`{.literal} attribute:

    ``` {.language-plaintext tabindex="-1"}
    # echo add > /sys/bus/ccw/devices/dasd-bus-ID/uevent
    ```

    where *`dasd-bus-ID`{.literal}* is the DASD's bus ID.

    For example, if the bus ID is `0.0.021a`{.literal}, run:

    ``` {.language-plaintext tabindex="-1"}
    # echo add > /sys/bus/ccw/devices/0.0.021a/uevent
    ```

### [20.7. FCP LUNs that are part of the root file system](#fcp-luns-that-are-part-of-the-root-file-system) {#fcp-luns-that-are-part-of-the-root-file-system .title}

The only file you have to modify for adding FCP LUNs that are part of the root file system has changed in Red Hat Enterprise Linux 10. Instead of editing the `/etc/zipl.conf`{.literal} file, determine the correct configuration file and its location by running the appropriate commands.

``` {.language-plaintext tabindex="-1"}
# machine_id=$(cat /etc/machine-id)
```

``` {.language-plaintext tabindex="-1"}
# kernel_version=$(uname -r)
```

``` {.language-plaintext tabindex="-1"}
# ls /boot/loader/entries/$machine_id-$kernel_version.conf
```

Red Hat Enterprise Linux provides a parameter to activate FCP LUNs early in the boot process: `rd.zfcp=`{.literal}. The value is a comma-separated list containing the FCP device bus ID and the target WWPN. The WWPN must be a 16-digit hexadecimal number prefixed with `0x`{.literal}. The list also includes the FCP LUN prefixed with `0x`{.literal} and padded with trailing zeroes to 16 hexadecimal digits.

The WWPN and FCP LUN values are only necessary if the zFCP device is not configured in NPIV mode. They are also required when auto LUN scanning is disabled with the `zfcp.allow_lun_scan=0`{.literal} kernel parameter or when installing RHEL-9.0 or older releases. Otherwise, they can be omitted, for example, `rd.zfcp=0.0.4000`{.literal}. Following is an example of the /boot/loader/entries/4ab74e52867b4f998e73e06cf23fd761-5.14.0-55.el9.s390x.conf file. The example shows a system using a physical volume on an FCP-attached SCSI disk partition with two paths. The system uses the `vg_devel1`{.literal} LVM volume group, which contains the `lv_root`{.literal} logical volume for the root file system.

``` {.language-plaintext tabindex="-1"}
title Red Hat Enterprise Linux (5.14.0-55.el9.s390x) 9.0 (Plow)
version 5.14.0-55.el9.s390x
linux /boot/vmlinuz-5.14.0-55.el9.s390x
initrd /boot/initramfs-5.14.0-55.el9.s390x.img
options root=/dev/mapper/vg_devel1-lv_root crashkernel=auto rd.zfcp=0.0.fc00,0x5105074308c212e9,0x401040a000000000 rd.zfcp=0.0.fcd0,0x5105074308c2aee9,0x401040a000000000 rd.lvm.lv=vg_devel1/lv_root rd.lvm.lv=vg_devel1/lv_swap cio_ignore=all,!condev rd.znet=qeth,0.0.0a00,0.0.0a01,0.0.0a02,layer2=1,portno=0
id rhel-20181027190514-5.14.0-55.el9.s390x
grub_users $grub_users
grub_arg --unrestricted
grub_class kernel
```

To add another physical volume on a second FCP-attached SCSI disk, use FCP LUN `0x401040a300000000`{.literal}. Use the same two paths as the existing physical volume. Add `rd.zfcp=0.0.fc00,0x5105074308c212e9,0x401040a300000000`{.literal} and `rd.zfcp=0.0.fcd0,0x5105074308c2aee9,0x401040a300000000`{.literal} to the kernel parameters line in `/boot/loader/entries/4ab74e52867b4f998e73e06cf23fd761-5.14.0-55.el9.s390x.conf`{.literal}. For example:

``` {.language-plaintext tabindex="-1"}
title Red Hat Enterprise Linux (5.14.0-55.el9.s390x) 9.0 (Plow)
version 5.14.0-55.el9.s390x
linux /boot/vmlinuz-5.14.0-55.el9.s390x
initrd /boot/initramfs-5.14.0-55.el9.s390x.img
options root=/dev/mapper/vg_devel1-lv_root crashkernel=auto rd.zfcp=0.0.fc00,0x5105074308c212e9,0x401040a000000000 rd.zfcp=0.0.fcd0,0x5105074308c2aee9,0x401040a000000000 rd.zfcp=0.0.fc00,0x5105074308c212e9,0x401040a300000000 rd.zfcp=0.0.fcd0,0x5105074308c2aee9,0x401040a300000000 rd.lvm.lv=vg_devel1/lv_root rd.lvm.lv=vg_devel1/lv_swap cio_ignore=all,!condev rd.znet=qeth,0.0.0a00,0.0.0a01,0.0.0a02,layer2=1,portno=0
id rhel-20181027190514-5.14.0-55.el9.s390x
grub_users $grub_users
grub_arg --unrestricted
grub_class kernel
```

Warning

Ensure that the length of the kernel command line in the configuration file does not exceed 896 bytes. Otherwise, the boot loader cannot be saved, and the installation fails.

-   Run `dracut -f`{.literal} to update the initial RAM disk of your target kernel.

-   Run `zipl`{.literal} to apply the changes of the configuration file for the next IPL:

    ``` {.language-plaintext tabindex="-1"}
    # zipl -V
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using config file '/etc/zipl.conf'
    Using BLS config file '/boot/loader/entries/4ab74e52867b4f998e73e06cf23fd761-5.14.0-55.el9.s390x.conf'
    Run /lib/s390-tools/zipl_helper.device-mapper /boot
    Target device information
    Device..........................: fd:00
    Partition.......................: fd:01
    Device name.....................: dm-0
    Device driver name..............: device-mapper
    Type............................: disk partition
    Disk layout.....................: SCSI disk layout
    Geometry - start................: 2048
    File system block size..........: 4096
    Physical block size.............: 512
    Device size in physical blocks..: 10074112
    Building bootmap in '/boot/'
    Building menu 'zipl-automatic-menu'
    Adding #1: IPL section '5.14.0-55.el9.s390x' (default)
    kernel image......: /boot/vmlinuz-5.14.0-55.el9.s390x
    kernel parmline...: 'root=/dev/mapper/vg_devel1-lv_root crashkernel=auto rd.zfcp=0.0.fc00,0x5105074308c212e9,0x401040a000000000 rd.zfcp=0.0.fcd0,0x5105074308c2aee9,0x401040a000000000 rd.zfcp=0.0.fc00,0x5105074308c212e9,0x401040a300000000 rd.zfcp=0.0.fcd0,0x5105074308c2aee9,0x401040a300000000 rd.lvm.lv=vg_devel1/lv_root rd.lvm.lv=vg_devel1/lv_swap cio_ignore=all,!condev rd.znet=qeth,0.0.0a00,0.0.0a01,0.0.0a02,layer2=1,portno=0'
    initial ramdisk...: /boot/initramfs-5.14.0-55.el9.s390x.img component address:
    kernel image....: 0x00010000-0x007a21ff
    parmline........: 0x00001000-0x000011ff
    initial ramdisk.: 0x02000000-0x028f63ff
    internal loader.: 0x0000a000-0x0000a3ff
    Preparing boot device: dm-0.
    Detected SCSI PCBIOS disk layout.
    Writing SCSI master boot record.
    Syncing disks...
    Done.
    ```

Warning

IBM Z systems use `zipl`{.literal} to create a bootmap containing raw block addresses of the kernel and `initramfs`{.literal}. If the `initramfs`{.literal} is regenerated, its physical layout on disk might change. Because `dracut`{.literal} does not automatically update the bootmap, manually run `zipl`{.literal} after regenerating the `initramfs`{.literal}. Failing to do so may result in a stale bootloader reference and cause the system to fail to boot.

**Additional resources**

-   [Kernel panic on s390x after manual `initramfs`{.literal} regeneration without zipl execution (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7119686)

### [20.8. FCP LUNs that are not part of the root file system](#fcp-luns-that-are-not-part-of-the-root-file-system) {#fcp-luns-that-are-not-part-of-the-root-file-system .title}

FCP LUNs that are not part of the root file system, such as data disks, are persistently configured in the file `/etc/zfcp.conf`{.literal}. It contains one FCP LUN per line.

Each line has three space- or tab-separated fields: the FCP adapter device bus ID, target WWPN, and FCP LUN. The WWPN is a 16-digit hexadecimal number prefixed with `0x`{.literal}. The FCP LUN is prefixed with `0x`{.literal} and right-padded with zeroes to 16 hexadecimal digits.

The WWPN and FCP LUN values are necessary if the zFCP device is not configured in NPIV mode. They are also required when auto LUN scanning is disabled or when installing RHEL-9.0 or older releases. Otherwise they can be omitted and only the device bus ID is mandatory.

Entries in `/etc/zfcp.conf`{.literal} are activated and configured by udev when an FCP adapter is added to the system. At boot time, all FCP adapters visible to the system are added and trigger **udev**.

Example content of `/etc/zfcp.conf`{.literal}:

``` {.language-plaintext tabindex="-1"}
0.0.fc00 0x5105074308c212e9 0x401040a000000000
0.0.fc00 0x5105074308c212e9 0x401040a100000000
0.0.fc00 0x5105074308c212e9 0x401040a300000000
0.0.fcd0 0x5105074308c2aee9 0x401040a000000000
0.0.fcd0 0x5105074308c2aee9 0x401040a100000000
0.0.fcd0 0x5105074308c2aee9 0x401040a300000000
0.0.4000
0.0.5000
```

Changes to `/etc/zfcp.conf`{.literal} become effective only after a system reboot or the dynamic addition of a new FCP channel. For example, a channel can be attached under `z/VM`{.literal} by changing the system I/O configuration. Alternatively, you can trigger the activation of a new entry in `/etc/zfcp.conf`{.literal} for an FCP adapter that was previously not active. To do so, run the following commands:

1.  Use the `zfcp_cio_free`{.literal} utility to remove the FCP adapters from the list of ignored devices and make them visible to Linux:

    ``` {.language-plaintext tabindex="-1"}
    # zfcp_cio_free
    ```

2.  To apply the additions from `/etc/zfcp.conf`{.literal} to the running system, issue:

    ``` {.language-plaintext tabindex="-1"}
    # zfcpconf.sh
    ```

### [20.9. Configuring IBM Z network devices for network root file system](#configuring-ibm-z-network-devices-for-network-root-file-system) {#configuring-ibm-z-network-devices-for-network-root-file-system .title}

To add a network device that is required to access the root file system, you only have to change the boot options. The boot options can be in a parameter file, however, the `/etc/zipl.conf`{.literal} file no longer contains specifications of the boot records.

**Procedure**

-   Locate the file by using the following commands that needs to be modified:

    ``` {.language-plaintext tabindex="-1"}
    # machine_id=$(cat /etc/machine-id)
    ```

    ``` {.language-plaintext tabindex="-1"}
    # kernel_version=$(uname -r)
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /boot/loader/entries/$machine_id-$kernel_version.conf
    ```

    **Dracut**, the **mkinitrd** successor that provides the functionality in the initramfs that in turn replaces **initrd**, provides a boot parameter to activate network devices on 64-bit IBM Z early in the boot process: `rd.znet=`{.literal}.

    This parameter takes a comma-separated list as input. The list includes the NETTYPE (qeth, lcs, or ctc) and two (lcs, ctc) or three (qeth) device bus IDs. It can also include optional key-value pairs for network device `sysfs`{.literal} attributes. This parameter configures and activates the 64-bit IBM Z network hardware. The configuration of IP addresses and other network specifics works the same as for other platforms. See the **dracut** documentation for more details.

    The **cio_ignore** commands for the network channels are handled seamlessly on boot.

    Example boot options for a root file system accessed over the network through NFS:

    ``` {.language-plaintext tabindex="-1"}
    root=10.16.105.196:/nfs/nfs_root cio_ignore=all,!condev rd.znet=qeth,0.0.0a00,0.0.0a01,0.0.0a02,layer2=1,portno=0,portname=OSAPORT ip=10.16.105.197:10.16.105.196:10.16.111.254:255.255.248.0:nfs‑server.subdomain.domain:enc9a0:none rd_NO_LUKS rd_NO_LVM rd_NO_MD rd_NO_DM LANG=en_US.UTF-8 SYSFONT=latarcyrheb-sun16 KEYTABLE=us
    ```

### [20.10. Additional resources](#additional_resources_2) {#additional-resources-1 .title}

-   [Device Drivers, Features, and Commands on RHEL](https://www.ibm.com/docs/en/linux-on-systems?topic=commands-red-hat-enterprise-linux-92)

## [Chapter 21. Kickstart script file format reference](#kickstart-script-file-format-reference) {#chapter-21.-kickstart-script-file-format-reference .title}

This reference describes in detail the kickstart file format.

### [21.1. Kickstart file format](#kickstart-file-format) {#kickstart-file-format .title}

Kickstart scripts are plain text files that contain keywords recognized by the installation program, which serve as directions for the installation.

Use any text editor to save files as ASCII text, such as `Gedit`{.literal} or `vim`{.literal} on Linux systems or `Notepad`{.literal} on Windows systems, to create and edit Kickstart files. The file name of your Kickstart configuration does not matter. However, it is recommended to use a simple name as you will need to specify this name later in other configuration files or dialogs.

Commands
:   Commands are keywords that serve as directions for installation. Each command must be on a single line. Commands can take options. Specifying commands and options is similar to using Linux commands in a shell.

Sections
:   Certain special commands that begin with the percent `%`{.literal} character start a section. Interpretation of commands in sections is different from commands placed outside sections. Every section must be finished with the `%end`{.literal} command.

Section types

:   The available sections are:

    -   **Add-on sections**. These sections use the `%addon `{.literal}*`addon_name`{.literal}* command.
    -   **Package selection sections**. Start with `%packages`{.literal}. Use it to list packages for installation, including indirect means such as package groups or modules.
    -   **Script sections**. These start with `%pre`{.literal}, `%pre-install`{.literal}, `%post`{.literal}, and `%onerror`{.literal}. These sections are not required.
    -   **Certificate sections**. These sections could be used to include certificates to be used by installation. For more information, see [Kickstart certificates section](#kickstart-certificates-section "21.6. Kickstart certificates section").

Command section
:   The command section is a term used for the commands in the Kickstart file that are not part of any script section or `%packages`{.literal} section.

Script section count and ordering
:   All sections except the command section are optional and can be present multiple times. When a script section type is evaluated, all sections of that type in the Kickstart file are processed in order of appearance. For example, two `%post`{.literal} sections are evaluated one after another. However, you do not have to specify the various types of script sections in any order. It does not matter if there are `%post`{.literal} sections before `%pre`{.literal} sections.

Comments
:   Kickstart comments are lines starting with the hash `#`{.literal} character. These lines are ignored by the installation program.

Items that are not required can be omitted. Omitting a required item causes the installation program to switch to interactive mode. You can then provide the missing information similar to a regular interactive installation. It is also possible to declare the kickstart script as non-interactive with the `cmdline`{.literal} command. In non-interactive mode, any missing answer aborts the installation process.

Note

If user interaction is needed during kickstart installation in text or graphical mode, enter only the windows where updates are mandatory to complete the installation. Entering spokes might lead to resetting the kickstart configuration. Resetting of the configuration applies specifically to the kickstart commands related to storage after entering the Installation Destination window.

### [21.2. Package selection in Kickstart](#package-selection-in-kickstart) {#package-selection-in-kickstart .title}

Kickstart uses sections started by the `%packages`{.literal} command for selecting packages to install. You can install packages, groups, and environments this way.

#### [21.2.1. Package selection section](#package-selection-section) {#package-selection-section .title}

Use the `%packages`{.literal} command to begin a Kickstart section which describes the software packages to be installed. The `%packages`{.literal} section must end with the `%end`{.literal} command.

You can specify packages by environment, group, module stream, module profile, or by their package names. Several environments and groups that contain related packages are defined. See the *`repository`{.literal}*`/repodata/*-comps-`{.literal}*`repository`{.literal}*`.`{.literal}*`architecture`{.literal}*`.xml`{.literal} file on the Red Hat Enterprise Linux 10 Installation DVD for a list of environments and groups.

The `*-comps-`{.literal}*`repository`{.literal}*`.`{.literal}*`architecture`{.literal}*`.xml`{.literal} file contains a structure describing available environments (marked by the `<environment>`{.literal} tag) and groups (the `<group>`{.literal} tag). Each entry has an ID, user visibility value, name, description, and package list. If the group is selected for installation, the packages marked `mandatory`{.literal} in the package list are always installed, the packages marked `default`{.literal} are installed if they are not specifically excluded elsewhere. The packages marked `optional`{.literal} must be specifically included elsewhere even when the group is selected.

You can specify a package group or environment by using either its ID (the `<id>`{.literal} tag) or name (the `<name>`{.literal} tag).

If you are not sure what package should be installed, select the **Minimal Install** environment. **Minimal Install** provides only the packages that are essential for running Red Hat Enterprise Linux 10. This will substantially reduce the chance of the system being affected by a vulnerability. If necessary, additional packages can be added later after the installation.

Important

To install a 32-bit package on a 64-bit system:

-   specify the `--multilib`{.literal} option for the `%packages`{.literal} section
-   append the package name with the 32-bit architecture for which the package was built; for example, `glibc.i686`{.literal}

**Additional resources**

-   [Installing the Minimum Amount of Packages Required](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/index)

#### [21.2.2. Package selection commands](#package-selection-commands) {#package-selection-commands .title}

You can use the following commands within the `%packages`{.literal} section of a Kickstart file.

Specifying an environment

:   Specify an entire environment to be installed as a line starting with the `@^`{.literal} symbols:

    ``` {.language-plaintext tabindex="-1"}
    %packages
    @^Infrastructure Server
    %end
    ```

    This installs all packages which are part of the `Infrastructure Server`{.literal .GUI} environment. All available environments are described in the *`repository`{.literal}*`/repodata/*-comps-`{.literal}*`repository`{.literal}*`.`{.literal}*`architecture`{.literal}*`.xml`{.literal} file on the Red Hat Enterprise Linux 10 Installation DVD.

    Only a single environment should be specified in the Kickstart file. If more environments are specified, only the last specified environment is used.

Specifying groups

:   Specify groups, one entry to a line, starting with an `@`{.literal} symbol, and then the full group name or group id as given in the `*-comps-`{.literal}*`repository`{.literal}*`.`{.literal}*`architecture`{.literal}*`.xml`{.literal} file. For example:

    ``` {.language-plaintext tabindex="-1"}
    %packages
    @X Window System
    @Desktop
    @Sound and Video
    %end
    ```

    The `Core`{.literal .GUI} group is always selected - it is not necessary to specify it in the `%packages`{.literal} section.

Specifying individual packages

:   Specify individual packages by name, one entry to a line. You can use the asterisk character (`*`{.literal}) as a wildcard in package names. For example:

    ``` {.language-plaintext tabindex="-1"}
    %packages
    sqlite
    curl
    aspell
    docbook*
    %end
    ```

    The `docbook*`{.literal} entry includes the packages `docbook-dtds`{.literal} and `docbook-style`{.literal} that match the pattern represented with the wildcard.

Specifying profiles of module streams

:   Specify profiles for module streams, one entry to a line, using the syntax for profiles:

    ``` {.language-plaintext tabindex="-1"}
    %packages
    @module:stream/profile
    %end
    ```

    This installs all packages listed in the specified profile of the module stream.

    -   When a module has a default stream specified, you can leave it out. When the default stream is not specified, you must specify it.
    -   When a module stream has a default profile specified, you can leave it out. When the default profile is not specified, you must specify it.
    -   Installing a module multiple times with different streams is not possible.
    -   Installing multiple profiles of the same module and stream is possible.

    Modules and groups use the same syntax starting with the `@`{.literal} symbol. When a module and a package group exist with the same name, the module takes precedence.

    In Red Hat Enterprise Linux 10, modules are present only in the AppStream repository. To list available modules, use the `dnf module list`{.literal} command on an installed Red Hat Enterprise Linux 10 system.

    It is also possible to enable module streams using the `module`{.literal} Kickstart command and then install packages contained in the module stream by naming them directly.

Excluding environments, groups, or packages

:   Use a leading dash (`-`{.literal}) to specify packages or groups to exclude from the installation. For example:

    ``` {.language-plaintext tabindex="-1"}
    %packages
    -@Graphical Administration Tools
    -autofs
    -ipa*compat
    %end
    ```

Important

Installing all available packages using only `*`{.literal} in a Kickstart file is not supported.

You can change the default behavior of the `%packages`{.literal} section by using several options. Some options work for the entire package selection, others are used with only specific groups.

**Additional resources**

-   [Managing Software with the DNF Tool](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/index)

#### [21.2.3. Common package selection options](#common-package-selection-options) {#common-package-selection-options .title}

You can use the following options in the `%packages`{.literal} sections. To use an option, append it to the start of the package selection section. For example:

``` {.language-plaintext tabindex="-1"}
%packages --multilib --ignoremissing
```

`--default`{.literal}
:   Install the default set of packages. This corresponds to the package set which would be installed if no other selections were made in the **Package Selection** screen during an interactive installation.

`--excludedocs`{.literal}
:   Do not install any documentation contained within packages. In most cases, this excludes any files normally installed in the `/usr/share/doc`{.literal} directory, but the specific files to be excluded depend on individual packages.

`--ignoremissing`{.literal}
:   Ignore any packages, groups, module streams, module profiles, and environments missing in the installation source, instead of halting the installation to ask if the installation should be stopped or continued.

`--inst-langs`{.literal}
:   Specify a list of languages to install. This is different from package group level selections. This option does not describe which package groups should be installed; instead, it sets RPM macros controlling which translation files from individual packages should be installed.

`--multilib`{.literal}

:   Configure the installed system for multilib packages, to allow installing 32-bit packages on a 64-bit system, and install packages specified in this section as such.

    Normally, on an AMD64 and Intel 64 system, you can install only the x86_64 and the noarch packages. However, with the \--multilib option, you can automatically install the 32-bit AMD and the i686 Intel system packages available, if any.

    This only applies to packages explicitly specified in the `%packages`{.literal} section. Packages installed only as dependencies and not specified in the Kickstart file are installed only for the required architecture versions. This applies even if the packages are available for multiple architectures.

    You can configure Anaconda to install packages in `multilib`{.literal} mode during the installation of the system. Use one of the following options to enable `multilib`{.literal} mode:

    1.  Configure Kickstart file with the following lines:

        ``` {.language-plaintext tabindex="-1"}
        %packages --multilib --default
        %end
        ```

    2.  Add the inst.multilib boot option during booting the installation image.

`--nocore`{.literal}

:   Disables installation of the `@Core`{.literal} package group which is otherwise always installed by default. Disabling the `@Core`{.literal} package group with `--nocore`{.literal} should only be used for creating lightweight containers; installing a desktop or server system with `--nocore`{.literal} results in an unusable system.

    Note

    Using `-@Core`{.literal} to exclude packages in the `@Core`{.literal} package group does not work. The only way to exclude the `@Core`{.literal} package group is with the `--nocore`{.literal} option. Also, the `@Core`{.literal} package group is defined as a minimal set of packages needed for installing a working system. It is not related in any way to core packages as defined in the [Package Manifest](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/package_manifest/index) and [Scope of Coverage Details](https://access.redhat.com/support/offerings/production/scope_moredetail).

`--exclude-weakdeps`{.literal}
:   Disables installation of packages from weak dependencies. These are packages linked to the selected package set by Recommends and Supplements flags. By default, weak dependencies are installed.

`--retries=`{.literal}
:   Sets the number of times `dnf`{.literal} will attempt to download packages (retries). The default value is 10. This option only applies during the installation, and will not affect `dnf`{.literal} configuration on the installed system.

`--timeout=`{.literal}
:   Sets the `dnf`{.literal} timeout in seconds. The default value is 30. This option only applies during the installation, and will not affect `dnf`{.literal} configuration on the installed system.

#### [21.2.4. Options for specific package groups](#options-for-specific-package-groups) {#options-for-specific-package-groups .title}

The options in this list only apply to a single package group. Instead of using them at the `%packages`{.literal} command in the Kickstart file, append them to the group name. For example:

``` {.language-plaintext tabindex="-1"}
%packages
@Graphical Administration Tools --optional
%end
```

`--nodefaults`{.literal}
:   Only install the group's mandatory packages, not the default selections.

`--optional`{.literal}

:   Install packages marked as optional in the group definition in the `*-comps-`{.literal}*`repository`{.literal}*`.`{.literal}*`architecture`{.literal}*`.xml`{.literal} file, in addition to installing the default selections.

    Some package groups, such as `Scientific Support`{.literal}, do not have any mandatory or default packages specified - only optional packages. In this case the `--optional`{.literal} option must always be used, otherwise no packages from this group will be installed.

Important

The `--nodefaults`{.literal} and `--optional`{.literal} options cannot be used together. You can install only mandatory packages during the installation using `--nodefaults`{.literal} and install the optional packages on the installed system post installation.

#### [21.2.5. Installing the kernel-64k package on 64-bit ARM by using Kickstart](#installing-the-kernel-64k-package-on-64-bit-arm-by-using-kickstart) {#installing-the-kernel-64k-package-on-64-bit-arm-by-using-kickstart .title}

You can install the `kernel-64k`{.literal} package during a Kickstart installation of Red Hat Enterprise Linux on 64-bit ARM architectures to support workloads that require large physical memory configurations. This package provides a kernel that supports a 64k memory management unit (MMU) page size for optimal performance.

**Procedure**

-   In the `%packages`{.literal} section of the kickstart file, add the following list of packages:

    ``` {.language-plaintext tabindex="-1"}
    %packages
    kernel-64k
    -kmod-kvdo
    -vdo
    -kernel
    %end
    ```

**Verification**

-   To verify the page size, after installation is completed and the system is rebooted, open the terminal and run:

    ``` {.language-plaintext tabindex="-1"}
    $ getconf PAGESIZE
    ```

    ``` {.language-plaintext tabindex="-1"}
    65536
    ```

    The output `65536`{.literal} indicates that the 64k kernel is in use.

-   To verify that the swap partition is enabled, enter:

    ``` {.language-plaintext tabindex="-1"}
    $ free
    ```

    ``` {.language-plaintext tabindex="-1"}
                   total        used        free      shared  buff/cache   available
    Mem:        35756352     3677184    34774848       25792      237120    32079168
    Swap:        6504384           0     6504384
    ```

The total and free columns are non-zero, which indicates the swap is enabled successfully.

### [21.3. Scripts in Kickstart file](#scripts-in-kickstart-file) {#scripts-in-kickstart-file .title}

A kickstart file can include the following scripts:

-   `%pre`{.literal}
-   `%pre-install`{.literal}
-   `%post`{.literal}

This section provides the following details about the scripts:

-   Execution time
-   Types of commands that can be included in the script
-   Purpose of the script
-   Script options

#### [21.3.1. %pre script](#pre-script) {#pre-script .title}

The `%pre`{.literal} scripts are run on the system immediately after the Kickstart file has been loaded, but before it is completely parsed and installation begins. Each of these sections must start with `%pre`{.literal} and end with `%end`{.literal}.

You can use the `%pre`{.literal} script for activating and configuring networking and storage devices. It is also possible to run scripts by using interpreters available in the installation environment. Adding a `%pre`{.literal} script can be useful if you have networking and storage that needs special configuration before proceeding with the installation. For example, you can use a script to set up additional logging parameters or environment variables.

Debugging problems with `%pre`{.literal} scripts can be difficult, so it is recommended only to use a `%pre`{.literal} script when necessary.

Important

The `%pre`{.literal} section of Kickstart runs at the stage of installation which happens after the installer image (`inst.stage2`{.literal}) is fetched. This means **after** root switches to the installer environment (the installer image) and **after** the `Anaconda`{.literal} installer itself starts. Then the configuration in `%pre`{.literal} is applied and can be used to fetch packages from installation repositories configured, for example, by URL in Kickstart. However, you **cannot** use it to configure the network to fetch the image (`inst.stage2`{.literal}) from the network.

Commands related to networking, storage, and file systems are available to use in the `%pre`{.literal} script. This is in addition to most of the utilities in the installation environment `/sbin`{.literal} and `/bin`{.literal} directories.

You can access the network in the `%pre`{.literal} section. However, the name service has not been configured at this point, so only IP addresses work, not URLs.

Note

The pre script does not run in the chroot environment.

##### [21.3.1.1. %pre script section options](#pre-script-section-options) {#pre-script-section-options .title}

The following options can be used to change the behavior of pre-installation scripts. To use an option, append it to the `%pre`{.literal} line at the beginning of the script. For example:

``` {.language-plaintext tabindex="-1"}
%pre --interpreter=/usr/libexec/platform-python
-- Python script omitted --
%end
```

`--interpreter=`{.literal}

:   Allows you to specify a different scripting language, such as Python. Any scripting language available on the system can be used; in most cases, these are `/usr/bin/sh`{.literal}, `/usr/bin/bash`{.literal}, and `/usr/libexec/platform-python`{.literal}.

    Note that the `platform-python`{.literal} interpreter uses Python version 3.6. You must change your Python scripts from previous RHEL versions for the new path and version. Additionally, `platform-python`{.literal} is meant for system tools: Use the `python36`{.literal} package outside the installation environment. For more details about Python in Red Hat Enterprise Linux, see [Introduction to Python](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_and_using_dynamic_programming_languages/installing-and-using-python).

`--erroronfail`{.literal}
:   Displays an error and halts the installation if the script fails. The error message will direct you to where the cause of the failure is logged. The installed system might get into an unstable and unbootable state. You can use the `inst.nokill`{.literal} option to debug the script.

`--log=`{.literal}

:   Logs the script's output into the specified log file. For example:

    ``` {.language-plaintext tabindex="-1"}
    %pre --log=/tmp/ks-pre.log
    ```

#### [21.3.2. %pre-install script](#pre-install-script) {#pre-install-script .title}

The commands in the `pre-install`{.literal} script are run after the following tasks are complete:

-   System is partitioned
-   Filesystems are created and mounted under /mnt/sysroot
-   Network has been configured according to any boot options and kickstart commands

Each of the `%pre-install`{.literal} sections must start with `%pre-install`{.literal} and end with `%end`{.literal}.

The `%pre-install`{.literal} scripts can be used to modify the installation, and to add users and groups with guaranteed IDs before package installation.

It is recommended to use the `%post`{.literal} scripts for any modifications required in the installation. Use the `%pre-install`{.literal} script only if the `%post`{.literal} script falls short for the required modifications.

The `pre-install`{.literal} script does not run in the chroot environment.

##### [21.3.2.1. %pre-install script section options](#pre-install-script-section-options) {#pre-install-script-section-options .title}

The following options can be used to change the behavior of `pre-install`{.literal} scripts. To use an option, append it to the `%pre-install`{.literal} line at the beginning of the script. For example:

``` {.language-plaintext tabindex="-1"}
%pre-install --interpreter=/usr/libexec/platform-python
-- Python script omitted --
%end
```

You can have multiple `%pre-install`{.literal} sections, with same or different interpreters. They are evaluated in their order of appearance in the Kickstart file.

`--interpreter=`{.literal}

:   Allows you to specify a different scripting language, such as Python. Any scripting language available on the system can be used; in most cases, these are `/usr/bin/sh`{.literal}, `/usr/bin/bash`{.literal}, and `/usr/libexec/platform-python`{.literal}.

    The `platform-python`{.literal} interpreter uses Python version 3.6. You must change your Python scripts from previous RHEL versions for the new path and version. Additionally, `platform-python`{.literal} is meant for system tools: Use the `python36`{.literal} package outside the installation environment. For more details about Python in Red Hat Enterprise Linux, see [Introduction to Python](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_and_using_dynamic_programming_languages/installing-and-using-python).

`--erroronfail`{.literal}
:   Displays an error and halts the installation if the script fails. The error message will direct you to where the cause of the failure is logged. The installed system might get into an unstable and unbootable state. You can use the `inst.nokill`{.literal} option to debug the script.

`--log=`{.literal}

:   Logs the script's output into the specified log file. For example:

    ``` {.language-plaintext tabindex="-1"}
    %pre-install --log=/mnt/sysroot/root/ks-pre.log
    ```

#### [21.3.3. %post script](#post-script) {#post-script .title}

The %post script is a post-installation script that is run after the installation is complete, but before the system is rebooted for the first time. You can use this section to run tasks such as system subscription.

You have the option of adding commands to run on the system once the installation is complete, but before the system is rebooted for the first time. This section must start with `%post`{.literal} and end with `%end`{.literal}.

The `%post`{.literal} section is useful for functions such as installing additional software or configuring an additional name server. The post-install script is run in a `chroot`{.literal} environment, therefore, performing tasks such as copying scripts or RPM packages from the installation media does not work by default. You can change this behavior by using the `--nochroot`{.literal} option as described in the following section. Then the `%post`{.literal} script will run in the installation environment, not in `chroot`{.literal} on the installed target system.

Because the post-install script runs in a `chroot`{.literal} environment, most `systemctl`{.literal} commands will refuse to perform any action.

During execution of the `%post`{.literal} section, the installation media must be still inserted.

##### [21.3.3.1. %post script section options](#post-script-section-options) {#post-script-section-options .title}

The following options can be used to change the behavior of post-installation scripts. To use an option, append it to the `%post`{.literal} line at the beginning of the script. For example:

``` {.language-plaintext tabindex="-1"}
%post --interpreter=/usr/libexec/platform-python
-- Python script omitted --
%end
```

`--interpreter=`{.literal}

:   Allows you to specify a different scripting language, such as Python. For example:

    ``` {.language-plaintext tabindex="-1"}
    %post --interpreter=/usr/libexec/platform-python
    ```

    Any scripting language available on the system can be used; in most cases, these are `/usr/bin/sh`{.literal}, `/usr/bin/bash`{.literal}, and `/usr/libexec/platform-python`{.literal}.

    The `platform-python`{.literal} interpreter uses Python version 3.6. You must change your Python scripts from previous RHEL versions for the new path and version. Additionally, `platform-python`{.literal} is meant for system tools: Use the `python36`{.literal} package outside the installation environment. For more details about Python in Red Hat Enterprise Linux, see [Introduction to Python](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_and_using_dynamic_programming_languages/installing-and-using-python).

`--nochroot`{.literal}

:   Allows you to specify commands that you would like to run outside of the chroot environment.

    The following example copies the file /etc/resolv.conf to the file system that was just installed.

    ``` {.language-plaintext tabindex="-1"}
    %post --nochroot
    cp /etc/resolv.conf /mnt/sysroot/etc/resolv.conf
    %end
    ```

`--erroronfail`{.literal}
:   Displays an error and halts the installation if the script fails. The error message will direct you to where the cause of the failure is logged. The installed system might get into an unstable and unbootable state. You can use the `inst.nokill`{.literal} option to debug the script.

`--log=`{.literal}

:   Logs the script's output into the specified log file. The path of the log file must take into account whether or not you use the `--nochroot`{.literal} option. For example, without `--nochroot`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    %post --log=/root/ks-post.log
    ```

    and with `--nochroot`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    %post --nochroot --log=/mnt/sysroot/root/ks-post.log
    ```

##### [21.3.3.2. Example: Mounting NFS in a post-install script](#example-mounting-nfs-in-a-post-install-script) {#example-mounting-nfs-in-a-post-install-script .title}

This example of a `%post`{.literal} section mounts an NFS share and executes a script named `runme`{.literal} located at `/usr/new-machines/`{.literal} on the share. The NFS file locking is not supported while in Kickstart mode, therefore the `-o nolock`{.literal} option is required.

``` {.language-plaintext tabindex="-1"}
# Start of the %post section with logging into /root/ks-post.log
%post --log=/root/ks-post.log

# Mount an NFS share
mkdir /mnt/temp
mount -o nolock 10.10.0.2:/usr/new-machines /mnt/temp
openvt -s -w -- /mnt/temp/runme
umount /mnt/temp

# End of the %post section
%end
```

### [21.4. Kickstart error handling section](#kickstart-error-handling-section) {#kickstart-error-handling-section .title}

Starting with Red Hat Enterprise Linux 7, Kickstart installations run custom scripts when fatal installation program errors occur. Examples include missing packages, RDP startup failures from configuration settings, or storage device scanning errors. In such cases, the installation aborts.

To analyze these events, the installation program runs all `%onerror`{.literal} scripts chronologically as provided in the Kickstart file. In the event of traceback, you can run the `%onerror`{.literal} scripts.

Each `%onerror`{.literal} script is required to end with `%end`{.literal}.

You can trigger command-line mode by using inst.cmdline; in this mode, all errors are treated as fatal by default.

Error handling sections accept the following options:

`--erroronfail`{.literal}
:   Displays an error and halts the installation if the script fails. The error message will direct you to where the cause of the failure is logged. The installed system might get into an unstable and unbootable state. You can use the `inst.nokill`{.literal} option to debug the script.

`--interpreter=`{.literal}

:   Allows you to specify a different scripting language, such as Python. For example:

    ``` {.language-plaintext tabindex="-1"}
    %onerror --interpreter=/usr/libexec/platform-python
    ```

    Any scripting language available on the system can be used; in most cases, these are `/usr/bin/sh`{.literal}, `/usr/bin/bash`{.literal}, and `/usr/libexec/platform-python`{.literal}.

    The `platform-python`{.literal} interpreter uses Python version 3.6. You must change your Python scripts from previous RHEL versions for the new path and version. Additionally, `platform-python`{.literal} is meant for system tools: Use the `python36`{.literal} package outside the installation environment. For more details about Python in Red Hat Enterprise Linux, see [Introduction to Python](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_and_using_dynamic_programming_languages/installing-and-using-python).

`--log=`{.literal}
:   Logs the script's output into the specified log file.

### [21.5. Kickstart add-on sections](#kickstart-add-on-sections) {#kickstart-add-on-sections .title}

Starting with Red Hat Enterprise Linux 7, Kickstart installations support add-ons. These add-ons can expand the basic Kickstart (and Anaconda) functionality in many ways.

To use an add-on in your Kickstart file, use the `%addon `{.literal}*`addon_name`{.literal}*` `{.literal}*`options`{.literal}* command, and finish the command with an `%end`{.literal} statement, similar to pre-installation and post-installation script sections. For example, if you want to use the Kdump add-on, which is distributed with Anaconda by default, use the following commands:

``` {.language-plaintext tabindex="-1"}
%addon com_redhat_kdump --enable --reserve-mb=auto
%end
```

The `%addon`{.literal} command does not include any options of its own - all options are dependent on the actual add-on.

### [21.6. Kickstart certificates section](#kickstart-certificates-section) {#kickstart-certificates-section .title}

The `%certificate`{.literal} section specifies the certificates that will be installed into the installer environment and the installed system. The certificate content must be in Base64 ASCII encoding format. The certificate will be written into a `.pem`{.literal} file.

You can specify the location to install the certificate and file details by using the following options:

Options

:   -   `--filename`{.literal} FILENAME

        Specifies the name of the certificate file.

    -   `--dir`{.literal} DIR

        Specifies the directory where the certificate should be installed.

Example Usage

:   A certificate bundle can be installed as part of a single %certificate section.

    ``` {.language-plaintext tabindex="-1"}
    %certificate --dir /etc/pki/dns/extracted/pem/ --filename tls-ca-bundle.pem
    -----BEGIN CERTIFICATE-----
    MIIBhDCCASugAwIBAgIUO27jF1hTk3lMZ5O6yMCC87FdLZcwCgYIKoZIzj0EAwIw
    EzERMA8GA1UEAwwIVHJ1c3RlZENBMB4XDTI1MDQwMTEyMDAwMFoXDTM1MDMzMDEy
    MDAwMFowEzERMA8GA1UEAwwIVHJ1c3RlZENBMFYwEAYHKoZIzj0CAQYFK4EEAAoD
    QgAErPu3eF/MBcNfFh1lYWfLzQz9O5sWu/bOXMIQ5iU6GZ4H17Q5aHpDJvuBq+nv
    uZYucGrdKj6GSa2KoD2Rz6GxDQIDAQABozEwLzAOBgNVHQ8BAf8EBAMCAQYwDwYD
    VR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMCAQYwCgYIKoZIzj0EAwIDRwAwRAIg
    A+3Txsfb5XQxpyq1dhK1c9Wy+F0dHZBaM4lKl8Zlf50CIHZ+bE5+8q90f5oRO2/f
    CZtCWZZRAquC/hXoNcGxM2b7
    -----END CERTIFICATE-----
    %end
    ```

## [Chapter 22. Kickstart commands and options reference](#kickstart-commands-and-options-reference) {#chapter-22.-kickstart-commands-and-options-reference .title}

This reference is a complete list of all Kickstart commands supported by the Red Hat Enterprise Linux installation program. The commands are sorted alphabetically in a few broad categories. If a command can fall under multiple categories, it is listed in all of them.

### [22.1. Kickstart changes](#kickstart-changes) {#kickstart-changes .title}

The following sections describe the changes in Kickstart commands and options in Red Hat Enterprise Linux 10.

#### [22.1.1. Deprecated Kickstart commands and options](#deprecated-kickstart-commands-and-options) {#deprecated-kickstart-commands-and-options .title}

The following Kickstart commands and options have been deprecated in Red Hat Enterprise Linux 10.

Where only specific options are listed, the base command and its other options are still available and not deprecated.

module
:   Anaconda has deprecated its support for DNF modularity, and as a consequence the module kickstart command has been deprecated. This might impact you if you are using modules in the `%packages`{.literal} section of your kickstart files or the module kickstart command.

#### [22.1.2. Removed Kickstart commands and options](#removed-kickstart-commands-and-options) {#removed-kickstart-commands-and-options .title}

The following Kickstart commands and options have been removed in Red Hat Enterprise Linux 10.

`auth or authconfig`{.literal}
:   As a replacement, use the `authselect`{.literal} kickstart command.

`inst.xdriver`{.literal} and `inst.usefbx`{.literal}
:   The graphical system for the installation image switched from the Xorg server to a Wayland compositor. As Wayland operates without relying on X drivers, making it incompatible with loading any such drivers, the `inst.xdriver`{.literal} option is no longer applicable. Additionally, the `inst.usefbx`{.literal} boot option, previously used to load a generic framebuffer X driver, has also been removed.

Few options of the timezone command

:   The following options of the timezone Kickstart command have been removed:

    -   `--isUtc`{.literal}: Use the option `--utc`{.literal} instead.
    -   `--ntpservers`{.literal}: Use the option `--ntp-server`{.literal} of the `timesource`{.literal} kickstart command instead.
    -   `--nontp`{.literal}: Use the option `--ntp-disable`{.literal} of the `timesource`{.literal} kickstart command instead.

`--level`{.literal} parameter of the logging command
:   The `--level`{.literal} parameter of the logging kickstart command has been removed. It is no longer possible to set the level of logging of the installation process.

`pwpolicy`{.literal}
:   The support for the deprecated `pwpolicy`{.literal} Kickstart command has been removed.

`%anaconda`{.literal}
:   Alternatively, use the kernel arguments and command line options to update the configuration in the Anaconda configuration files.

`network`{.literal}
:   The `--teamslaves`{.literal} and `--teamconfig`{.literal} options used for configuring team devices in the network kickstart command have been removed. To configure similar network settings, use the `--bondslaves`{.literal} and `--bondopts`{.literal} options to configure a Bond device.

`%packages`{.literal}
:   the `--excludeWeakdeps`{.literal} and `--instLangs`{.literal} options used in the `%packages`{.literal} section have been removed. To maintain similar functionality, use the updated options `--exclude-weakdeps`{.literal} and `--inst-langs`{.literal} instead.

`btrfs`{.literal}
:   The support for the deprecated `btrfs`{.literal} Kickstart command has been removed.

`nvdimm`{.literal}
:   The support for reconfiguring NVDIMM devices during the Kickstart installation has been removed. However, the NVDIMM devices in the sector mode can still be usable in the installation program.

`method`{.literal}
:   The support for the deprecated `method`{.literal} Kickstart command has been removed.

`vnc`{.literal}
:   VNC kickstart command is removed in RHEL 10. Use RDP instead.

### [22.2. Kickstart commands for installation program configuration and flow control](#kickstart-commands-for-installation-program-configuration-and-flow-control) {#kickstart-commands-for-installation-program-configuration-and-flow-control .title}

The Kickstart commands in this list control the mode and course of installation, and what happens at its end.

#### [22.2.1. bootc](#bootc) {#bootc .title}

You can use the `bootc`{.literal} command to install a system from a native bootable container image. Use this command to specify the source container image, the target image for future updates, and the stateroot for the installation. You can use the following Kickstart commands:

-   `clearpart`{.literal}, `zerombr`{.literal}
-   `bootloader`{.literal} (only the `--append`{.literal} option)
-   `autopart`{.literal}, `reqpart`{.literal}, `part`{.literal}, `volgroup`{.literal}, `logvol`{.literal}
-   `reboot`{.literal}, `halt`{.literal}, `poweroffgraphical`{.literal}, `cmdline`{.literal}, `text`{.literal}, `rdp`{.literal}
-   `%pre`{.literal}, `%post`{.literal}, `%include`{.literal}
-   `keyboard`{.literal}
-   `lang`{.literal}
-   `network`{.literal}
-   `rhsm`{.literal}
-   `rootpw`{.literal}
-   `sshkey`{.literal}
-   `timezone`{.literal}
-   `user`{.literal}

Important

`bootc`{.literal} is provided as a Technology Preview only. Technology Preview features are not supported with Red Hat production Service Level Agreements (SLAs), might not be functionally complete, and Red Hat does not recommend using them for production. These previews provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

See [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview) on the Red Hat Customer Portal for information about the support scope for Technology Preview features.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    # bootc [--stateroot STATEROOT] --source-imgref SOURCEIMGREF [--target-imgref TARGETIMGREF]
    ```

Options

:   -   `--stateroot`{.literal}: Defines the name of the state directory, which is also referred to as the `osname`{.literal}.
    -   `--source-imgref`{.literal}: Specifies the explicit source location from which the system is installed. It must be specified in `<transport>:<image-url>`{.literal} format, for example, `registry:registry.example.com/rhel-10/rhel-bootc:10.2`{.literal}.
    -   `--target-imgref`{.literal}: Identifies the image reference that the system uses for future system updates. If this option is not specified, it defaults to the value provided in `--source-imgref`{.literal}. Although this option is not mandatory, currently it needs to be specified for the image reference configuration in the installed system. As opposed to the `--source-imgref`{.literal} option, it cannot start with a transport prefix (for example, `registry.example.com/rhel-10/rhel-bootc:10.2`{.literal} is a correct format). The `bootc`{.literal} tool in the installed system implicitly uses a `registry`{.literal} transport.

Note

Do not use this command with the `ostreesetup`{.literal}, `ostreecontainer`{.literal}, `liveimg`{.literal}, `%packages`{.literal}, and installation source commands such as `cdrom`{.literal}, `url`{.literal}, or `repo`{.literal}.

**Additional resources**

-   [Installing RHEL from a bootable container image by using the bootc Kickstart command (Red Hat Knowledgebase)](https://access.redhat.com/articles/7140131)
-   [Accessing private registries with pull secrets on Anaconda installations](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/deploying-the-rhel-bootc-images#accessing-private-registries-with-pull-secrets-on-anaconda-installations)

#### [22.2.2. cdrom](#cdrom) {#cdrom .title}

The `cdrom`{.literal} Kickstart command is optional. It performs the installation from the first optical drive on the system. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    cdrom
    ```

Notes

:   -   This command has no options.
    -   To actually run the installation, you must specify one of `cdrom`{.literal}, `harddrive`{.literal}, `hmc`{.literal}, `nfs`{.literal}, `liveimg`{.literal}, `ostreesetup`{.literal}, `rhsm`{.literal}, or `url`{.literal} unless the `inst.repo`{.literal} option is specified on the kernel command line.

#### [22.2.3. cmdline](#cmdline) {#cmdline .title}

The `cmdline`{.literal} Kickstart command is optional. It performs the installation in a completely non-interactive command line mode. Any prompt for interaction halts the installation. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    cmdline
    ```

Notes

:   -   For a fully automatic installation, you must either specify one of the available modes (`graphical`{.literal}, `text`{.literal}, or `cmdline`{.literal}) in the Kickstart file, or you must use the `console=`{.literal} boot option. If no mode is specified, the system will use graphical mode if possible, or prompt you to choose from RDP and text mode.
    -   This command has no options.
    -   This mode is useful on 64-bit IBM Z systems with the x3270 terminal.

#### [22.2.4. driverdisk](#driverdisk) {#driverdisk .title}

The `driverdisk`{.literal} Kickstart command is optional. Use it to provide additional drivers to the installation program.

Driver disks can be used during Kickstart installations to provide additional drivers not included by default. You must copy the driver disks contents to the root directory of a partition on the system's disk. Then, you must use the `driverdisk`{.literal} command to specify that the installation program should look for a driver disk and its location. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    driverdisk [partition|--source=url|--biospart=biospart]
    ```

Options

:   You must specify the location of driver disk in one way out of these:

    -   *partition* - Partition containing the driver disk. The partition must be specified as a full path (for example, `/dev/sdb1`{.literal}), *not* just the partition name (for example, `sdb1`{.literal}).

    -   `--source=`{.literal} - URL for the driver disk. Examples include:

        ``` {.language-plaintext tabindex="-1"}
        driverdisk --source=ftp://path/to/dd.img
        driverdisk --source=http://path/to/dd.img
        driverdisk --source=nfs:host:/path/to/dd.img
        ```

    -   `--biospart=`{.literal} - BIOS partition containing the driver disk (for example, `82p2`{.literal}).

Notes

:   You can load the driver disks from a local disk or a similar device instead of being loaded over the network or from `initrd`{.literal}. To do this:

    1.  Load the driver disk on a disk drive, a USB or any similar device.

    2.  Set the label, for example, *DD*, to this device.

    3.  Add the following line to your Kickstart file:

        ``` {.language-plaintext tabindex="-1"}
        driverdisk LABEL=DD:/e1000.rpm
        ```

        Replace *DD* with a specific label and replace *e1000.rpm* with a specific name. Use anything supported by the `inst.repo`{.literal} command instead of *LABEL* to specify your disk drive.

#### [22.2.5. eula](#eula) {#eula .title}

The `eula`{.literal} Kickstart command is optional. Use this option to accept the End User License Agreement (EULA) without user interaction.

Specifying this option prevents Initial Setup from prompting you to accept the license agreement after you finish the installation and reboot the system for the first time. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    eula [--agreed]
    ```

Options

:   -   `--agreed`{.literal} (required) - Accepts the EULA. This option must always be used, otherwise the `eula`{.literal} command is meaningless.

#### [22.2.6. firstboot](#firstboot) {#firstboot .title}

The `firstboot`{.literal} Kickstart command is optional. It determines whether the `Initial Setup`{.literal .GUI} application starts the first time the system is booted. If enabled, the **initial-setup** package must be installed. If not specified, this option is disabled by default. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    firstboot OPTIONS
    ```

Options

:   -   `--enable`{.literal} or `--enabled`{.literal} - Initial Setup is started the first time the system boots.
    -   `--disable`{.literal} or `--disabled`{.literal} - Initial Setup is not started the first time the system boots.
    -   `--reconfig`{.literal} - Enable the Initial Setup to start at boot time in reconfiguration mode. This mode enables the root password, time & date, and networking & host name configuration options in addition to the default ones.

#### [22.2.7. graphical](#graphical) {#graphical .title}

The `graphical`{.literal} Kickstart command is optional. It performs the installation in graphical mode. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    graphical [--non-interactive]
    ```

Options

:   -   `--non-interactive`{.literal} - Performs the installation in a completely non-interactive mode. This mode will stop the installation when user interaction is required.

Notes

:   -   For a fully automatic installation, you must either specify one of the available modes (`graphical`{.literal}, `text`{.literal}, or `cmdline`{.literal}) in the Kickstart file, or you must use the `console=`{.literal} boot option. If no mode is specified, the system will use graphical mode if possible, or prompt you to choose from RDP and text mode.

#### [22.2.8. halt](#halt) {#halt .title}

The `halt`{.literal} Kickstart command is optional. Use this command to halt the system after the installation has successfully completed.

This is similar to a manual installation, where Anaconda displays a message and waits for the user to press a key before rebooting. During a Kickstart installation, if no completion method is specified, this option is used as the default. Use this command only once. This command has no options.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    halt
    ```

Notes

:   -   The `halt`{.literal} command is equivalent to the `shutdown -H`{.literal} command. For more details, see the *shutdown(8)* man page on your system.
    -   For other completion methods, see the `poweroff`{.literal}, `reboot`{.literal}, and `shutdown`{.literal} commands.

#### [22.2.9. harddrive](#harddrive) {#harddrive .title}

The `harddrive`{.literal} Kickstart command is optional. It performs the installation from a Red Hat installation tree or full installation ISO image on a local drive.

You must format the drive with a file system the installation program can mount: `ext2`{.literal}, `ext3`{.literal}, `ext4`{.literal}, `vfat`{.literal}, or `xfs`{.literal}. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    harddrive OPTIONS
    ```

Mandatory options

:   -   `--partition=`{.literal} - Partition to install from (such as `sdb2`{.literal}).
    -   `--dir=`{.literal} - Directory containing the installation tree, or the ISO image of the full installation DVD.

Example

:   

``` {.language-plaintext tabindex="-1"}
harddrive --partition=hdb2 --dir=/tmp/install-tree
```

Note

:   -   To actually run the installation, you must specify one of `cdrom`{.literal}, `harddrive`{.literal}, `hmc`{.literal}, `nfs`{.literal}, `liveimg`{.literal}, `ostreesetup`{.literal}, `rhsm`{.literal}, or `url`{.literal} unless the `inst.repo`{.literal} option is specified on the kernel command line.

#### [22.2.10. liveimg](#liveimg) {#liveimg .title}

The `liveimg`{.literal} Kickstart command is optional. It performs the installation from a disk image instead of packages. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    liveimg --url=SOURCE [OPTIONS]
    ```

Mandatory options

:   -   `--url=`{.literal} - The location to install from. Supported protocols are `HTTP`{.literal}, `HTTPS`{.literal}, `FTP`{.literal}, and `file`{.literal}.

Optional options

:   -   `--proxy=`{.literal} - Specify an `HTTP`{.literal}, `HTTPS`{.literal} or `FTP`{.literal} proxy to use while performing the installation.
    -   `--checksum=`{.literal} - An argument with the `SHA256`{.literal} checksum of the image file, used for verification.
    -   `--noverifyssl`{.literal} - Disable SSL verification when connecting to an `HTTPS`{.literal} server.

Example

:   

``` {.language-plaintext tabindex="-1"}
liveimg --url=file:///images/install/squashfs.img --checksum=03825f567f17705100de3308a20354b4d81ac9d8bed4bb4692b2381045e56197 --noverifyssl
```

Notes

:   -   The image can be the squashfs.img file from a live ISO image or a compressed tar file. Supported tar formats include `.tar`{.literal}, `.tbz`{.literal}, `.tgz`{.literal}, `.txz`{.literal}, `.tar.bz2`{.literal}, `.tar.gz`{.literal}, and `.tar.xz`{.literal}. The image can also use any file system mountable by the installation media. Supported file systems are `ext2`{.literal}, `ext3`{.literal}, `ext4`{.literal}, `vfat`{.literal}, and `xfs`{.literal}.
    -   When using the `liveimg`{.literal} installation mode with a driver disk, drivers on the disk will not automatically be included in the installed system. If necessary, these drivers should be installed manually, or in the `%post`{.literal} section of a kickstart script.
    -   To actually run the installation, you must specify one of `cdrom`{.literal}, `harddrive`{.literal}, `hmc`{.literal}, `nfs`{.literal}, `liveimg`{.literal}, `ostreesetup`{.literal}, `rhsm`{.literal}, or `url`{.literal} unless the `inst.repo`{.literal} option is specified on the kernel command line.

#### [22.2.11. logging](#logging) {#logging .title}

The `logging`{.literal} Kickstart command is optional. It controls the error logging of Anaconda during installation. It has no effect on the installed system. Use this command only once.

Logging is supported over TCP only. For remote logging, ensure that the port number that you specify in `--port=`{.literal} option is open on the remote server. The default port is 514.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    logging OPTIONS
    ```

Optional options

:   -   `--host=`{.literal} - Send logging information to the given remote host, which must be running a syslogd process configured to accept remote logging.
    -   `--port=`{.literal} - If the remote syslog process uses a port other than the default port, set it by using this option.

#### [22.2.12. mediacheck](#mediacheck) {#mediacheck .title}

The `mediacheck`{.literal} Kickstart command is optional. This command forces the installation program to perform a media check before starting the installation. This command requires that installations be attended, so it is disabled by default. Use this command only once. This command has no options.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    mediacheck
    ```

Note

:   -   This Kickstart command is equivalent to the `rd.live.check`{.literal} boot option.

#### [22.2.13. nfs](#nfs) {#nfs .title}

The `nfs`{.literal} Kickstart command is optional. It performs the installation from a specified NFS server. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    nfs OPTIONS
    ```

Options

:   -   `--server=`{.literal} - Server from which to install (host name or IP).
    -   `--dir=`{.literal} - Directory containing the `Packages/`{.literal} directory of the installation tree.
    -   `--opts=`{.literal} - Mount options to use for mounting the NFS export. (optional)

Example

:   

``` {.language-plaintext tabindex="-1"}
nfs --server=nfsserver.example.com --dir=/tmp/install-tree
```

Note

:   -   To actually run the installation, you must specify one of `cdrom`{.literal}, `harddrive`{.literal}, `hmc`{.literal}, `nfs`{.literal}, `liveimg`{.literal}, `ostreesetup`{.literal}, `rhsm`{.literal}, or `url`{.literal} unless the `inst.repo`{.literal} option is specified on the kernel command line.

#### [22.2.14. ostreesetup](#ostreesetup) {#ostreesetup .title}

The `ostreesetup`{.literal} Kickstart command is optional. It is used to configure OStree-based installations. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    ostreesetup --osname=OSNAME [--remote=REMOTE] --url=URL --ref=REF [--nogpg]
    ```

Mandatory options

:   -   `--osname=`{.literal}*`OSNAME`{.literal}* - Management root for OS installation.
    -   `--url=`{.literal}*`URL`{.literal}* - URL of the repository to install from.
    -   `--ref=`{.literal}*`REF`{.literal}* - Name of the branch from the repository to be used for installation.

Optional options

:   -   `--remote=`{.literal}*`REMOTE`{.literal}* - A remote repository location.

    -   `--nogpg`{.literal} - Disable GPG key verification.

        For more information about the OStree tools, see the upstream documentation: [https://ostreedev.github.io/ostree/](https://ostreedev.github.io/ostree/)

#### [22.2.15. ostreecontainer](#ostreecontainer) {#ostreecontainer .title}

The **ostreecontainer** Kickstart command is optional. Use this command for OSTree installations from your custom containers.

Important

The **ostreecontainer** is provided as a Technology Preview only. Technology Preview features are not supported with Red Hat production Service Level Agreements (SLAs), might not be functionally complete, and Red Hat does not recommend using them for production. These previews provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. See [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview) on the Red Hat Customer Portal for information about the support scope for Technology Preview features.

Usage with bootc-image-builder

:   When using `bootc-image-builder`{.literal} to create bootable ISOs, the tool automatically injects the `%ostreecontainer`{.literal} command into the embedded Kickstart file. Note the following:

    -   The end-to-end process from image creation to installation is considered a Technology Preview.
    -   The support status remains Technology Preview regardless of whether you write the Kickstart file manually or the tool generates it.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    ostreecontainer [--stateroot STATEROOT] --url URL [--transport TRANSPORT] [--remote REMOTE] [--no-signature-verification]
    ```

Options

:   -   `--no-signature-verification`{.literal}: Use this option to disable verification for an ostree remote.

    -   `--stateroot`{.literal}: Name of the state directory, also known as \"osname\". Default value is `default`{.literal}.

    -   `--url`{.literal}: Name of the container image for the registry transport. For example, `quay.io/exampleos/foo:latest`{.literal}.

    -   `--transport`{.literal}: The transport, for example, registry or oci. The default value is `registry`{.literal}.

        When performing Kickstart installations, the following commands are available together with `ostreecontainer`{.literal}:

    -   `graphical`{.literal}, `text`{.literal}, or `cmdline`{.literal}

    -   `clearpart`{.literal} and `zerombr`{.literal}

    -   `autopart`{.literal}

    -   `part`{.literal}

    -   `logvol`{.literal} and `volgroup`{.literal}

    -   `reboot`{.literal} and `shutdown`{.literal}

    -   `lang`{.literal}

    -   `rootpw`{.literal}

    -   `sshkey`{.literal}

    -   `bootloader`{.literal} (available only with the `--append`{.literal} optional parameter)

    -   `user`{.literal} - When you specify a group within the user command, the user account can be assigned only to a group that already exists in the container image.

        The following Kickstart commands are unsupported together with `ostreecontainer`{.literal}:

    -   `authconfig`{.literal} and `authselect`{.literal} (provide relevant configuration in the container image instead)

    -   `ostreesetup`{.literal}

    -   `liveimg`{.literal}

    -   `module`{.literal}

    -   `%packages`{.literal} (any necessary packages must be already available in the container image)

    -   `repo`{.literal}

    -   `url`{.literal} (if installation requires a `stage2`{.literal} image, such as during PXE installations, use `inst.stage2=`{.literal} on the kernel command line. Do not provide a `stage2`{.literal} URL in the Kickstart file.)

    -   `zfcp`{.literal}

    -   `zipl`{.literal}

        Kickstart commands not listed here can be used with the `ostreecontainer`{.literal} command. However, they are not guaranteed to work as expected in the same way as with package-based installations.

Note

:   -   The `ostreecontainer`{.literal} option cannot be used with the `ostreesetup`{.literal} command.

#### [22.2.16. poweroff](#poweroff) {#poweroff .title}

The `poweroff`{.literal} Kickstart command is optional. It shuts down the system after completing the installation. Normally during a manual installation, Anaconda displays a message and waits for the user to press a key before rebooting. Use this command only once. This command has no options.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    poweroff
    ```

Notes

:   -   The `poweroff`{.literal} option is equivalent to the `shutdown -P`{.literal} command. For more details, see the *shutdown(8)* man page on your system.
    -   For other completion methods, see the `halt`{.literal}, `reboot`{.literal}, and `shutdown`{.literal} Kickstart commands. The `halt`{.literal} option is the default completion method if no other methods are explicitly specified in the Kickstart file.
    -   The `poweroff`{.literal} command is highly dependent on the system hardware in use. Specifically, certain hardware components such as the BIOS, APM (advanced power management), and ACPI (advanced configuration and power interface) must be able to interact with the system kernel. Consult your hardware documentation for more information about your system's APM/ACPI abilities.

#### [22.2.17. reboot](#reboot) {#reboot .title}

The `reboot`{.literal} Kickstart command is optional. It instructs the installation program to reboot after the installation is successfully completed. Normally, Kickstart displays a message and waits for the user to press a key before rebooting. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    reboot OPTIONS
    ```

Options

:   -   `--eject`{.literal} - Attempt to eject the bootable media (DVD, USB, or other media) before rebooting.

    -   `--kexec`{.literal} - Uses the `kexec`{.literal} system call instead of performing a full reboot that immediately loads the installed system into memory. This bypasses the hardware initialization normally performed by the BIOS or firmware.

        Important

        This option is deprecated and available as a Technology Preview only. For information about Red Hat scope of support for Technology Preview features, see the [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview) document.

        When `kexec`{.literal} is used, device registers (which would normally be cleared during a full system reboot) might stay filled with data, which could potentially create issues for some device drivers.

Notes

:   -   Use of the `reboot`{.literal} option *might* result in an endless installation loop, depending on the installation media and method.
    -   The `reboot`{.literal} option is equivalent to the `shutdown -r`{.literal} command. For more details, see the *shutdown(8)* man page on your system.
    -   Specify `reboot`{.literal} to automate installation fully when installing in command line mode on 64-bit IBM Z.
    -   For other completion methods, see the `halt`{.literal}, `poweroff`{.literal}, and `shutdown`{.literal} Kickstart options. The `halt`{.literal} option is the default completion method if no other methods are explicitly specified in the Kickstart file.

#### [22.2.18. rhsm](#rhsm) {#rhsm .title}

The `rhsm`{.literal} Kickstart command is optional. It instructs the installation program to register and install RHEL from the CDN. It can also connect the installed system to Red Hat Lightspeed. Use this command only once.

The `rhsm`{.literal} Kickstart command eliminates the requirement of custom `%post`{.literal} scripts when registering the system.

Options

:   -   `--organization=`{.literal} - Uses the organization ID to register and install RHEL from the CDN.
    -   `--activation-key=`{.literal} - Uses the activation key to register and install RHEL from the CDN. Option can be used multiple times, once per activation key, as long as the activation keys used are registered to your subscription.
    -   `--connect-to-insights`{.literal} - Connects the target system to Red Hat Lightspeed.
    -   `--proxy=`{.literal} - Sets the HTTP proxy.
    -   `--server-hostname=`{.literal} - Sets the Satellite instance hostname for registration.

Important

-   To switch the installation source repository to the CDN by using the `rhsm`{.literal} Kickstart command, you must meet the following conditions:

    -   On the kernel command line, you have used `inst.stage2=`{.literal}*`<URL>`{.literal}* to fetch the installation image but have not specified an installation source using `inst.repo=`{.literal}.
    -   In the Kickstart file, you have not specified an installation source by using the `url`{.literal}, `cdrom`{.literal}, `harddrive`{.literal}, `liveimg`{.literal}, `nfs`{.literal} and `ostree`{.literal} setup commands.

-   An installation source URL specified using a boot option or included in a Kickstart file takes precedence over the CDN, even if the Kickstart file contains the `rhsm`{.literal} command with valid credentials. The system is registered, but it is installed from the URL installation source. This ensures that earlier installation processes operate as normal.

#### [22.2.19. shutdown](#shutdown) {#shutdown .title}

The `shutdown`{.literal} Kickstart command is optional. It shuts down the system after the installation has successfully completed. Use this command only once. This command has no options.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    shutdown
    ```

Notes

:   -   The `shutdown`{.literal} Kickstart option is equivalent to the `shutdown`{.literal} command. For more details, see the *shutdown(8)* man page on your system.
    -   For other completion methods, see the `halt`{.literal}, `poweroff`{.literal}, and `reboot`{.literal} Kickstart options. The `halt`{.literal} option is the default completion method if no other methods are explicitly specified in the Kickstart file.

#### [22.2.20. sshpw](#sshpw) {#sshpw .title}

The `sshpw`{.literal} Kickstart command is optional. During the installation, you can interact with the installation program and monitor its progress over an `SSH`{.literal} connection.

Use the `sshpw`{.literal} command to create temporary accounts through which to log in. Each instance of the command creates a separate account that exists only in the installation environment. These accounts are not transferred to the installed system.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    sshpw --username=name [OPTIONS] password
    ```

Mandatory options

:   -   `--username`{.literal}=*name* - Provides the name of the user. This option is required.
    -   *`password`{.literal}* - The password to use for the user. This argument is required.

Optional options

:   -   `--iscrypted`{.literal} - If this option is present, the password argument is assumed to already be encrypted. This option is mutually exclusive with `--plaintext`{.literal}. To create an encrypted password, you can use Python:

    ``` {.language-plaintext tabindex="-1"}
    $ python3 -c 'import crypt,getpass;pw=getpass.getpass();print(crypt.crypt(pw) if (pw==getpass.getpass("Confirm: ")) else exit())'
    ```

    This generates a sha512 crypt-compatible hash of your password by using a random salt.

    -   `--plaintext`{.literal} - If this option is present, the password argument is assumed to be in plain text. This option is mutually exclusive with `--iscrypted`{.literal}
    -   `--lock`{.literal} - If this option is present, this account is locked by default. This means that the user will not be able to log in from the console.
    -   `--sshkey`{.literal} - If this option is present, then the *\<password\>* string is interpreted as an ssh key value.

Notes

:   -   By default, the `ssh`{.literal} server is not started during the installation. To make `ssh`{.literal} available during the installation, boot the system with the kernel boot option `inst.sshd`{.literal}.

    -   If you want to disable root `ssh`{.literal} access, while allowing another user `ssh`{.literal} access, use the following:

        ``` {.language-plaintext tabindex="-1"}
        sshpw --username=example_username example_password --plaintext
        ```

        ``` {.language-plaintext tabindex="-1"}
        sshpw --username=root example_password --lock
        ```

    -   To disable root `ssh`{.literal} access, use the following:

        ``` {.language-plaintext tabindex="-1"}
        sshpw --username=root example_password --lock
        ```

#### [22.2.21. text](#text) {#text .title}

The `text`{.literal} Kickstart command is optional. It performs the Kickstart installation in text mode. Kickstart installations are performed in graphical mode by default. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    text [--non-interactive]
    ```

Options

:   -   `--non-interactive`{.literal} - Performs the installation in a completely non-interactive mode. This mode will stop the installation when user interaction is required.

Note

:   -   For a fully automatic installation, you must either specify one of the available modes (`graphical`{.literal}, `text`{.literal}, or `cmdline`{.literal}) in the Kickstart file, or you must use the `console=`{.literal} boot option. If no mode is specified, the system will use graphical mode if possible, or prompt you to choose from RDP and text mode.

#### [22.2.22. url](#url) {#url .title}

The `url`{.literal} Kickstart command is optional. It is used to install from an installation tree image on a remote server by using the FTP, HTTP, or HTTPS protocol. You can only specify one URL. Use this command only once.

You must specify one of the `--url`{.literal}, `--metalink`{.literal} or `--mirrorlist`{.literal} options.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    url --url=FROM [OPTIONS]
    ```

Options

:   -   `--url=`{.literal}*`FROM`{.literal}* - Specifies the `HTTP`{.literal}, `HTTPS`{.literal}, `FTP`{.literal}, or `file`{.literal} location to install from.
    -   `--mirrorlist=`{.literal} - Specifies the mirror URL to install from.
    -   `--proxy=`{.literal} - Specifies an `HTTP`{.literal}, `HTTPS`{.literal}, or `FTP`{.literal} proxy to use during the installation.
    -   `--noverifyssl`{.literal} - Disables SSL verification when connecting to an `HTTPS`{.literal} server.
    -   `--metalink=`{.literal}*`URL`{.literal}* - Specifies the metalink URL to install from. Variable substitution is done for `$releasever`{.literal} and `$basearch`{.literal} in the *URL*.

Examples

:   -   To install from a FTP server:

        ``` {.language-plaintext tabindex="-1"}
        url --url=ftp://username:password@server/path
        ```

    -   To install from a HTTP server:

        ``` {.language-plaintext tabindex="-1"}
        url --url=http://server/path
        ```

Note

:   -   To actually run the installation, you must specify one of `cdrom`{.literal}, `harddrive`{.literal}, `hmc`{.literal}, `nfs`{.literal}, `liveimg`{.literal}, `ostreesetup`{.literal}, `rhsm`{.literal}, or `url`{.literal} unless the `inst.repo`{.literal} option is specified on the kernel command line.

#### [22.2.23. hmc](#hmc) {#hmc .title}

The hmc kickstart command is optional. Use it to install from an installation medium by using SE/HMC on IBM Z. This command does not have any options.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    hmc
    ```

#### [22.2.24. rdp](#rdp) {#rdp .title}

Use the `rdp`{.literal} command to perform a graphical installation remotely by using the Remote Desktop Protocol (RDP). This method is preferred over text-mode installations because text mode lacks several features available in the graphical user interface.

If you use the `rdp`{.literal} command without any options, the installation program enables RDP and prompts you to manually set a username and password on the local console.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    # rdp [--username USERNAME] [--password PASSWORD]
    ```

Options

:   -   \--username --- Specifies the username required for the RDP client to connect to the installation session.
    -   \--password --- Specifies the password required for the RDP client to connect to the installation session.

**Additional resources**

-   [Starting a remote installation by using the Remote Desktop Protocol](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/starting-a-remote-installation-by-using-the-remote-desktop-protocol)

#### [22.2.25. %include](#include) {#include .title}

The `%include`{.literal} Kickstart command is optional. Use the %include command to include the contents of another file in the Kickstart file. The included contents are treated as if they were at the `%include`{.literal} command location in the Kickstart file.

This inclusion is evaluated only after the `%pre`{.literal} script sections and can thus be used to include files generated by scripts in the `%pre`{.literal} sections. To include files before evaluation of `%pre`{.literal} sections, use the `%ksappend`{.literal} command.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    %include path/to/file
    ```

#### [22.2.26. %ksappend](#ksappend) {#ksappend .title}

The `%ksappend`{.literal} Kickstart command is optional. Use `%ksappend`{.literal} to include another file in the Kickstart file as if that file's contents appeared at the `%ksappend`{.literal} line.

This inclusion is evaluated before the `%pre`{.literal} script sections, unlike inclusion with the `%include`{.literal} command.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    %ksappend path/to/file
    ```

### [22.3. Kickstart commands for system configuration](#kickstart-commands-for-system-configuration) {#kickstart-commands-for-system-configuration .title}

The Kickstart commands in this list configure further details on the resulting system such as users, repositories, or services.

#### [22.3.1. authselect](#authselect) {#authselect .title}

The `authselect`{.literal} Kickstart command is optional. It sets up the authentication options for the system using the `authselect`{.literal} command, which can also be run on the command line after the installation finishes. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    authselect [OPTIONS]
    ```

Notes

:   -   This command passes all options to the `authselect`{.literal} command. Refer to the *authselect(8)* manual page and the `authselect --help`{.literal} command for more details.
    -   Passwords are shadowed by default.
    -   When using OpenLDAP with the `SSL`{.literal} protocol for security, ensure that the `SSLv2`{.literal} and `SSLv3`{.literal} protocols are disabled in the server configuration. This is due to the POODLE SSL vulnerability (CVE-2014-3566). For more information, see the Red Hat Knowledgebase solution [Resolution for POODLE SSLv3.0 vulnerability](https://access.redhat.com/solutions/1234843).

#### [22.3.2. firewall](#firewall) {#firewall .title}

The `firewall`{.literal} Kickstart command is optional. It specifies the firewall configuration for the installed system.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    firewall --enabled|--disabled [incoming] [OPTIONS]
    ```

Mandatory options

:   -   `--enabled`{.literal} or `--enable`{.literal} - Reject incoming connections that are not in response to outbound requests, such as DNS replies or DHCP requests. If access to services running on this machine is needed, you can choose to allow specific services through the firewall.
    -   `--disabled`{.literal} or `--disable`{.literal} - Do not configure any iptables rules.

Optional options

:   -   `--trust`{.literal} - Listing a device here, such as `em1`{.literal}, allows all traffic coming to and from that device to go through the firewall. To list more than one device, use the option more times, such as `--trust em1 --trust em2`{.literal}. Do not use a comma-separated format such as `--trust em1, em2`{.literal}.

    -   `--remove-service`{.literal} - Close ports for comma-separated list of services.

    -   *incoming* - Replace with one or more of the following to allow the specified services through the firewall.

        -   `--ssh`{.literal}
        -   `--smtp`{.literal}
        -   `--http`{.literal}
        -   `--ftp`{.literal}

    -   `--port=`{.literal} - You can specify that ports be allowed through the firewall using the port:protocol format. For example, to allow IMAP access through your firewall, specify `imap:tcp`{.literal}. Numeric ports can also be specified explicitly; for example, to allow UDP packets on port 1234 through, specify `1234:udp`{.literal}. To specify multiple ports, separate them by commas.

    -   `--service=`{.literal} - This option provides a higher-level way to allow services through the firewall. Some services (such as `cups`{.literal}, `avahi`{.literal}, and so on) require multiple ports to be open or other special configuration in order for the service to work. You can specify each individual port with the `--port`{.literal} option, or specify `--service=`{.literal} and open them all at once.

        Valid options are anything recognized by the `firewall-offline-cmd`{.literal} program in the **firewalld** package. If the `firewalld`{.literal} service is running, `firewall-cmd --get-services`{.literal} provides a list of known service names.

    -   `--use-system-defaults`{.literal} - Do not configure the firewall at all. This option instructs anaconda to do nothing and allows the system to rely on the defaults that were provided with the package or ostree. If this option is used with other options then all other options will be ignored.

#### [22.3.3. group](#group) {#group .title}

The `group`{.literal} Kickstart command is optional. It creates a new user group on the system.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    group --name=name [--gid=gid]
    ```

Mandatory options

:   -   `--name=`{.literal} - Provides the name of the group.

Optional options

:   -   `--gid=`{.literal} - The group's GID. If not provided, defaults to the next available non-system GID.

Notes

:   -   If a group with the given name or GID already exists, this command fails.
    -   The `user`{.literal} command can be used to create a new group for the newly created user.

#### [22.3.4. keyboard](#keyboard) {#keyboard .title}

The `keyboard`{.literal} Kickstart command is required. It sets one or more available keyboard layouts for the system. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    keyboard --vckeymap|--xlayouts OPTIONS
    ```

Options

:   -   `--vckeymap=`{.literal} - Specify a `VConsole`{.literal} keymap which should be used. Valid names correspond to the list of files in the `/usr/lib/kbd/keymaps/xkb/`{.literal} directory, without the `.map.gz`{.literal} extension.

    -   `--xlayouts=`{.literal} - Specify a list of X layouts that should be used as a comma-separated list without spaces. Accepts values in the same format as `setxkbmap(1)`{.literal}, either in the *`layout`{.literal}* format (such as `cz`{.literal}), or in the *`layout`{.literal}*` (`{.literal}*`variant`{.literal}*`)`{.literal} format (such as `cz (qwerty)`{.literal}).

        All available layouts can be viewed on the `xkeyboard-config(7)`{.literal} man page under `Layouts`{.literal}.

    -   `--switch=`{.literal} - Specify a list of layout-switching options (shortcuts for switching between multiple keyboard layouts). Multiple options must be separated by commas without spaces. Accepts values in the same format as `setxkbmap(1)`{.literal}.

        Available switching options can be viewed on the `xkeyboard-config(7)`{.literal} man page under `Options`{.literal}.

Example

:   The following example sets up two keyboard layouts (`English (US)`{.literal} and `Czech (qwerty)`{.literal}) using the `--xlayouts=`{.literal} option, and allows to switch between them using Alt+Shift:

    ``` {.language-plaintext tabindex="-1"}
    keyboard --xlayouts=us,'cz (qwerty)' --switch=grp:alt_shift_toggle
    ```

Note

:   -   Either the `--vckeymap=`{.literal} or the `--xlayouts=`{.literal} option must be used.

#### [22.3.5. lang](#lang) {#lang .title}

The `lang`{.literal} Kickstart command is required. It sets the language to use during installation and the default language to use on the installed system. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    lang language [--addsupport=language,...]
    ```

Mandatory options

:   -   *`language`{.literal}* - Install support for this language and set it as system default.

Optional options

:   -   `--addsupport=`{.literal} - Add support for additional languages. Takes the form of comma-separated list without spaces. For example:

    ``` {.language-plaintext tabindex="-1"}
    lang en_US --addsupport=cs_CZ,de_DE,en_UK
    ```

Notes

:   -   The `locale -a | grep _`{.literal} or `localectl list-locales | grep _`{.literal} commands return a list of supported locales.
    -   Certain languages (for example, Chinese, Japanese, Korean, and Indic languages) are not supported during text-mode installation. If you specify one of these languages with the `lang`{.literal} command, the installation process continues in English, but the installed system uses your selection as its default language.

Example

:   To set the language to English, the Kickstart file should contain the following line:

    ``` {.language-plaintext tabindex="-1"}
    lang en_US
    ```

#### [22.3.6. module](#module) {#module .title}

The `module`{.literal} Kickstart command is optional. Use this command to enable a package module stream within the kickstart script.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    module --name=NAME [--stream=STREAM]
    ```

Mandatory options

:   -   `--name=`{.literal} : Specifies the name of the module to enable. Replace *NAME* with the actual name.

Optional options

:   -   `--stream=`{.literal} : Specifies the name of the module stream to enable. Replace *STREAM* with the actual name.

    You do not need to specify this option for modules with a default stream defined. For modules without a default stream, this option is mandatory and leaving it out results in an error. Enabling a module multiple times with different streams is not possible.

Notes

:   -   Using a combination of this command and the `%packages`{.literal} section allows you to install packages provided by the enabled module and stream combination, without specifying the module and stream explicitly. Modules must be enabled before package installation. After enabling a module with the `module`{.literal} command, you can install the packages enabled by this module by listing them in the `%packages`{.literal} section.
    -   A single `module`{.literal} command can enable only a single module and stream combination. To enable multiple modules, use multiple `module`{.literal} commands. Enabling a module multiple times with different streams is not possible.
    -   In Red Hat Enterprise Linux 10, modules are present only in the AppStream repository. To list available modules, use the `dnf module list`{.literal} command on an installed Red Hat Enterprise Linux Red Hat Enterprise Linux system with a valid subscription.

**Additional resources**

-   [Managing Software with the DNF Tool](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/index)

#### [22.3.7. repo](#repo) {#repo .title}

The `repo`{.literal} Kickstart command is optional. It configures additional dnf repositories that can be used as sources for package installation. You can add multiple `repo`{.literal} lines.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    repo --name=repoid [--baseurl=url|--mirrorlist=url|--metalink=url] [OPTIONS]
    ```

Mandatory options

:   -   `--name=`{.literal} - The repository id. This option is required. If a repository has a name which conflicts with another previously added repository, it is ignored. Because the installation program uses a list of preset repositories, this means that you cannot add repositories with the same names as the preset ones.

URL options

:   These options are mutually exclusive and optional. The variables that can be used in dnf repository configuration files are not supported here. You can use the strings `$releasever`{.literal} and `$basearch`{.literal} which are replaced by the respective values in the URL.

    -   `--baseurl=`{.literal} - The URL to the repository.
    -   `--mirrorlist=`{.literal} - The URL pointing at a list of mirrors for the repository.
    -   `--metalink=`{.literal} - The URL with metalink for the repository.

Optional options

:   -   `--install`{.literal} - Save the provided repository configuration on the installed system in the `/etc/yum.repos.d/`{.literal} directory. Without using this option, a repository configured in a Kickstart file will only be available during the installation process, not on the installed system.
    -   `--cost=`{.literal} - An integer value to assign a cost to this repository. If multiple repositories provide the same packages, this number is used to prioritize which repository will be used before another. Repositories with a lower cost take priority over repositories with higher cost.
    -   `--excludepkgs=`{.literal} - A comma-separated list of package names that must *not* be pulled from this repository. This is useful if multiple repositories provide the same package and you want to ensure it comes from a particular repository. Both full package names (such as `publican`{.literal}) and globs (such as `gnome-*`{.literal}) are accepted.
    -   `--includepkgs=`{.literal} - A comma-separated list of package names and globs that are allowed to be pulled from this repository. Any other packages provided by the repository will be ignored. This is useful if you want to install just a single package or set of packages from a repository while excluding all other packages the repository provides.
    -   `--proxy=[`{.literal}*`protocol`{.literal}*`://][`{.literal}*`username`{.literal}*`[:`{.literal}*`password`{.literal}*`]@]`{.literal}*`host`{.literal}*`[:`{.literal}*`port`{.literal}*`]`{.literal} - Specify an HTTP/HTTPS/FTP proxy to use just for this repository. This setting does not affect any other repositories, nor how the `install.img`{.literal} is fetched on HTTP installations.
    -   `--noverifyssl`{.literal} - Disable SSL verification when connecting to an `HTTPS`{.literal} server.

Note

:   -   Repositories used for installation must be stable. The installation can fail if a repository is modified before the installation concludes.

#### [22.3.8. rootpw](#rootpw) {#rootpw .title}

The `rootpw`{.literal} Kickstart command is required. It sets the system's root password to the *password* argument. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    rootpw [--iscrypted|--plaintext] [--lock] password
    ```

Mandatory options

:   -   *password* - Password specification. Either plain text or an encrypted string. See `--iscrypted`{.literal} and `--plaintext`{.literal} in the following options.

Optional options

:   -   `--iscrypted`{.literal} - If this option is present, the password argument is assumed to already be encrypted. This option is mutually exclusive with `--plaintext`{.literal}. To create an encrypted password, you can use python:

    ``` {.language-plaintext tabindex="-1"}
    $ python -c 'import crypt,getpass;pw=getpass.getpass();print(crypt.crypt(pw) if (pw==getpass.getpass("Confirm: ")) else exit())'
    ```

    This generates a sha512 crypt-compatible hash of your password by using a random salt.

    -   `--plaintext`{.literal} - If this option is present, the password argument is assumed to be in plain text. This option is mutually exclusive with `--iscrypted`{.literal}.
    -   `--lock`{.literal} - If this option is present, the root account is locked by default. This means that the root user will not be able to log in from the console. This option will also disable the **Root Password** screens in both the graphical and text-based manual installation.
    -   `--allow-ssh`{.literal} - If this option is present, the root user can login to the system by using SSH with a password.

#### [22.3.9. selinux](#selinux) {#selinux .title}

The `selinux`{.literal} Kickstart command is optional. It sets the state of SELinux on the installed system. The default SELinux policy is `enforcing`{.literal}. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    selinux [--disabled|--enforcing|--permissive]
    ```

Options

:   -   `--enforcing`{.literal} - Enables SELinux with the default targeted policy being `enforcing`{.literal}.
    -   `--permissive`{.literal} - Outputs warnings based on the SELinux policy, but does not actually enforce the policy.
    -   `--disabled`{.literal} - Disables SELinux completely on the system.

**Additional resources**

-   [Using SElinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/index)

#### [22.3.10. services](#services) {#services .title}

The `services`{.literal} Kickstart command is optional. It modifies the default set of services that will run under the default systemd target. The list of disabled services is processed before the list of enabled services. Therefore, if a service appears on both lists, it will be enabled.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    services [--disabled=list] [--enabled=list]
    ```

Options

:   -   `--disabled=`{.literal} - Disable the services given in the comma separated list.
    -   `--enabled=`{.literal} - Enable the services given in the comma separated list.

Notes

:   -   When using the `services`{.literal} element to enable `systemd`{.literal} services, ensure you include packages containing the specified service file in the `%packages`{.literal} section.

    -   Multiple services should be included separated by comma, without any spaces. For example, to disable four services, enter:

        ``` {.language-plaintext tabindex="-1"}
        services --disabled=auditd,cups,smartd,nfslock
        ```

        If you include any spaces, Kickstart enables or disables only the services up to the first space. For example:

        ``` {.language-plaintext tabindex="-1"}
        services --disabled=auditd, cups, smartd, nfslock
        ```

        That disables only the `auditd`{.literal} service. To disable all four services, this entry must include no spaces.

#### [22.3.11. skipx](#skipx) {#skipx .title}

The `skipx`{.literal} Kickstart command is optional. If present, the system is configured to boot in text mode. Use this command only once. This command has no options.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    skipx
    ```

#### [22.3.12. sshkey](#sshkey) {#sshkey .title}

The `sshkey`{.literal} Kickstart command is optional. It adds a SSH public key to the `authorized_keys`{.literal} file of the specified user on the installed system.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    sshkey --username=user "ssh_key"
    ```

Mandatory options

:   -   `--username=`{.literal} - The user for which the key will be installed.
    -   *`ssh_key`{.literal}* - The complete SSH public key. It must be wrapped with quotes.

#### [22.3.13. syspurpose](#syspurpose) {#syspurpose .title}

The `syspurpose`{.literal} Kickstart command is optional. Use it to set the system purpose which describes how the system will be used after installation. This information helps apply the correct subscription entitlement to the system. Use this command only once.

Note

In Red Hat Enterprise Linux 9.0 and later you can manage and display system purpose attributes with the `subscription-manager syspurpose`{.literal} module. The module includes the `role`{.literal}, `service-level`{.literal}, `usage`{.literal}, and `addons`{.literal} subcommands. Previously, system administrators used one of four standalone `syspurpose`{.literal} commands to manage each attribute. This standalone `syspurpose`{.literal} command is deprecated starting with RHEL 9.0 and is planned to be removed in post RHEL 9. Red Hat provides bug fixes and support for this feature during the current release lifecycle, but this feature does not receive enhancements. Starting with RHEL 9, the single `subscription-manager syspurpose`{.literal} command and its associated subcommands is the only way to use system purpose. These changes only apply to the command line tools for system purpose configuration used on installed systems and do not influence the functionality of the `syspurpose`{.literal} kickstart command.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    syspurpose [OPTIONS]
    ```

Options

:   -   `--role=`{.literal} - Set the intended system role. Available values are:

        -   Red Hat Enterprise Linux Server
        -   Red Hat Enterprise Linux Workstation
        -   Red Hat Enterprise Linux Compute Node

    -   `--sla=`{.literal} - Set the Service Level Agreement. Available values are:

        -   Premium
        -   Standard
        -   Self-Support

    -   `--usage=`{.literal} - The intended usage of the system. Available values are:

        -   Production
        -   Disaster Recovery
        -   Development/Test

Notes

:   -   Enter the values with spaces and enclose them in double quotes:

    ``` {.language-plaintext tabindex="-1"}
    syspurpose --role="Red Hat Enterprise Linux Server"
    ```

    -   While it is strongly recommended that you configure System Purpose, it is an optional feature of the Red Hat Enterprise Linux installation program.
    -   Additional values might be used based on how subscriptions are configured for the given account

#### [22.3.14. timezone](#timezone) {#timezone .title}

The `timezone`{.literal} Kickstart command is required. It sets the system time zone. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    timezone timezone [OPTIONS]
    ```

Mandatory options

:   -   *timezone* - the time zone to set for the system.

Optional options

:   -   `--utc`{.literal} - If present, the system assumes the hardware clock is set to UTC (Greenwich Mean) time.

Note
:   In Red Hat Enterprise Linux 10, time zone names are validated using the `pytz.all_timezones`{.literal} list, provided by the **pytz** package. In previous releases, the names were validated against `pytz.common_timezones`{.literal}, which is a subset of the currently used list. Note that the graphical and text mode interfaces still use the more restricted `pytz.common_timezones`{.literal} list; you must use a Kickstart file to use additional time zone definitions.

#### [22.3.15. timesource](#timesource) {#timesource .title}

The `timesource`{.literal} kickstart command is optional. Use it to set NTP, NTS servers, and pools that provide time data, as well as control whether NTP services are enabled or disabled on the system.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    timesource [--ntp-server NTP_SERVER | --ntp-pool NTP_POOL | --ntp-disable] [--nts]
    ```

Mandatory options

:   It is mandatory to specify one of the following options when you use the `timesource`{.literal} command:

    -   `--ntp-server`{.literal} - adds one NTP server as a time source. You can add this option only once to a single command to add one NTP time source server. To add multiple sources, add multiple timesource commands each with a single `--ntp-server`{.literal} or `--ntp-pool`{.literal} option each time. For example, to add multiple sources for *Europe* timezone.

    ``` {.language-plaintext tabindex="-1"}
    timezone Europe
    timesource --ntp-server 0.rhel.pool.ntp.org
    timesource --ntp-server 1.rhel.pool.ntp.org
    timesource --ntp-server 2.rhel.pool.ntp.org
    ```

    -   `--ntp-pool`{.literal} - adds a NTP server pool as a time source. This option can be added only once to add a single NTP time source pool. Repeat the timesource command to add multiple sources.
    -   `--ntp-disable`{.literal} - disables NTP time sources for the installed system.

Optional options

:   -   `--nts`{.literal} - the server or pool added with this command uses the NTS protocol. Note that this option can be added even with \--ntp-disable, but it has no effect.

#### [22.3.16. user](#user) {#user .title}

The `user`{.literal} Kickstart command is optional. It creates a new user on the system.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    user --name=username [OPTIONS]
    ```

Mandatory options

:   -   `--name=`{.literal} - Provides the name of the user. This option is required.

Optional options

:   -   `--gecos=`{.literal} - Provides the GECOS information for the user. This is a string of various system-specific fields separated by a comma. It is frequently used to specify the user's full name, office number, and so on. See the `passwd(5)`{.literal} man page for more details.

    -   `--groups=`{.literal} - In addition to the default group, a comma separated list of group names the user should belong to. The groups must exist before the user account is created. See the `group`{.literal} command.

    -   `--homedir=`{.literal} - The home directory for the user. If not provided, this defaults to `/home/`{.literal}*`username`{.literal}*.

    -   `--lock`{.literal} - If this option is present, this account is locked by default. This means that the user will not be able to log in from the console. This option will also disable the **Create User** screens in both the graphical and text-based manual installation.

    -   `--password=`{.literal} - The new user's password. If not provided, the account will be locked by default.

    -   `--iscrypted`{.literal} - If this option is present, the password argument is assumed to already be encrypted. This option is mutually exclusive with `--plaintext`{.literal}. To create an encrypted password, you can use python:

        ``` {.language-plaintext tabindex="-1"}
        $ python -c 'import crypt,getpass;pw=getpass.getpass();print(crypt.crypt(pw) if (pw==getpass.getpass("Confirm: ")) else exit())'
        ```

        This generates a sha512 crypt-compatible hash of your password by using a random salt.

    -   `--plaintext`{.literal} - If this option is present, the password argument is assumed to be in plain text. This option is mutually exclusive with `--iscrypted`{.literal}

    -   `--shell=`{.literal} - The user's login shell. If not provided, the system default is used.

    -   `--uid=`{.literal} - The user's UID (User ID). If not provided, this defaults to the next available non-system UID.

    -   `--gid=`{.literal} - The GID (Group ID) to be used for the user's group. If not provided, this defaults to the next available non-system group ID.

Notes

:   -   Consider using the `--uid`{.literal} and `--gid`{.literal} options to set IDs of regular users and their default groups at range starting at `5000`{.literal} instead of `1000`{.literal}. That is because the range reserved for system users and groups, `0`{.literal}-`999`{.literal}, might increase in the future and thus overlap with IDs of regular users.

    -   Files and directories are created with various permissions, dictated by the application used to create the file or directory. For example, the `mkdir`{.literal} command creates directories with all permissions enabled. However, applications are prevented from granting certain permissions to newly created files, as specified by the `user file-creation mask`{.literal} setting.

        The `user file-creation mask`{.literal} can be controlled with the `umask`{.literal} command. The default setting of the `user file-creation mask`{.literal} for new users is defined by the `UMASK`{.literal} variable in the `/etc/login.defs`{.literal} configuration file on the installed system. If unset, it defaults to `022`{.literal}. This means that by default when an application creates a file, it is prevented from granting write permission to users other than the owner of the file. However, this can be overridden by other settings or scripts.

#### [22.3.17. xconfig](#xconfig) {#xconfig .title}

The `xconfig`{.literal} Kickstart command is optional. If used with the `--startxonboot`{.literal} option it configures the installed system to start in graphical mode. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    xconfig [--startxonboot]
    ```

Options

:   -   `--startxonboot`{.literal} - Use a graphical login on the installed system.

Note

:   -   Because Red Hat Enterprise Linux 10 does not include the KDE Desktop Environment, do not use the `--defaultdesktop=`{.literal} documented upstream.

### [22.4. Kickstart commands for network configuration](#kickstart-commands-for-network-configuration) {#kickstart-commands-for-network-configuration .title}

The Kickstart commands in this list let you configure networking on the system.

#### [22.4.1. network](#network) {#network .title}

Use the optional `network`{.literal} Kickstart command to configure target system network settings and activate network devices in the installation environment. The device in the first `network`{.literal} command activates automatically. You can also explicitly activate a device by using the `--activate`{.literal} option.

Warning

Re-configuration of already active network devices that are in use by the running installer may lead to an installation failure or freeze. In such a case, avoid re-configuration of network devices used to access the installer runtime image (*stage2*) over NFS.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    network OPTIONS
    ```

Options

:   -   `--activate`{.literal} - activate this device in the installation environment.

    If you use the `--activate`{.literal} option on a device that is already activated, the device is reactivated with the settings specified in the Kickstart file. For example, this can occur on an interface configured with boot options to retrieve the Kickstart file.

Use the `--nodefroute`{.literal} option to prevent the device from using the default route.

-   `--no-activate`{.literal} - do not activate this device in the installation environment.

    By default, Anaconda activates the first network device in the Kickstart file regardless of the `--activate`{.literal} option. You can disable the default setting by using the `--no-activate`{.literal} option.

-   `--bootproto=`{.literal} - One of `dhcp`{.literal}, `bootp`{.literal}, `ibft`{.literal}, or `static`{.literal}. The default option is `dhcp`{.literal}; the `dhcp`{.literal} and `bootp`{.literal} options are treated the same. To disable `ipv4`{.literal} configuration of the device, use `--noipv4`{.literal} option.

    Note

    This option configures the ipv4 configuration of the device. For ipv6 configuration use `--ipv6`{.literal} and `--ipv6gateway`{.literal} options.

    The DHCP method uses a DHCP server system to obtain its networking configuration. The BOOTP method is similar, requiring a BOOTP server to supply the networking configuration. To direct a system to use DHCP:

    ``` {.language-plaintext tabindex="-1"}
    network --bootproto=dhcp
    ```

    To direct a machine to use BOOTP to obtain its networking configuration, use the following line in the Kickstart file:

    ``` {.language-plaintext tabindex="-1"}
    network --bootproto=bootp
    ```

    To direct a machine to use the configuration specified in iBFT, use:

    ``` {.language-plaintext tabindex="-1"}
    network --bootproto=ibft
    ```

    The `static`{.literal} method requires that you specify at least the IP address and netmask in the Kickstart file. This information is static and is used during and after the installation.

    All static networking configuration information must be specified on *one* line; you cannot wrap lines by using a backslash (`\`{.literal}) as you can on a command line.

    ``` {.language-plaintext tabindex="-1"}
    network --bootproto=static --ip=10.0.2.15 --netmask=255.255.255.0 --gateway=10.0.2.254 --nameserver=10.0.2.1
    ```

    You can also configure multiple nameservers at the same time. To do so, use the `--nameserver=`{.literal} option once, and specify each of their IP addresses, separated by commas:

    ``` {.language-plaintext tabindex="-1"}
    network --bootproto=static --ip=10.0.2.15 --netmask=255.255.255.0 --gateway=10.0.2.254 --nameserver=192.168.2.1,192.168.3.1
    ```

-   `--device=`{.literal} - specifies the device to be configured (and eventually activated in Anaconda) with the `network`{.literal} command.

    If the `--device=`{.literal} option is missing on the *first* use of the `network`{.literal} command, the value of the `inst.ks.device=`{.literal} Anaconda boot option is used, if available. This is considered deprecated behavior; in most cases, you should always specify a `--device=`{.literal} for every `network`{.literal} command.

    The behavior of any subsequent `network`{.literal} command in the same Kickstart file is unspecified if its `--device=`{.literal} option is missing. Verify you specify this option for any `network`{.literal} command beyond the first.

    You can specify a device to be activated in any of the following ways:

    -   the device name of the interface, for example, `em1`{.literal}
    -   the MAC address of the interface, for example, `01:23:45:67:89:ab`{.literal}
    -   the keyword `link`{.literal}, which specifies the first interface with its link in the `up`{.literal} state
    -   the keyword `bootif`{.literal}, which uses the MAC address that pxelinux set in the `BOOTIF`{.literal} variable. Set `IPAPPEND 2`{.literal} in your `pxelinux.cfg`{.literal} file to have pxelinux set the `BOOTIF`{.literal} variable.

    For example:

    ``` {.language-plaintext tabindex="-1"}
    network --bootproto=dhcp --device=em1
    ```

-   `--ipv4-dns-search`{.literal}/`--ipv6-dns-search`{.literal} - Set the DNS search domains manually. You must use these options together with `--device`{.literal} options and mirror their respective NetworkManager properties, for example:

    ``` {.language-plaintext tabindex="-1"}
    network --device ens3 --ipv4-dns-search domain1.example.com,domain2.example.com
    ```

-   `--ipv4-ignore-auto-dns`{.literal}/`--ipv6-ignore-auto-dns`{.literal} - Set to ignore the DNS settings from DHCP. You must use these options together with `--device`{.literal} options and these options do not require any arguments.

-   `--ip=`{.literal} - IP address of the device.

-   `--ipv6=`{.literal} - IPv6 address of the device, in the form of *address*\[/*prefix* *length*\] - for example, `3ffe:ffff:0:1::1/128`{.literal}. If the *prefix* is omitted, `64`{.literal} is used. You can also use `auto`{.literal} for automatic configuration, or `dhcp`{.literal} for DHCPv6-only configuration (no router advertisements).

-   `--gateway=`{.literal} - Default gateway as a single IPv4 address.

-   `--ipv6gateway=`{.literal} - Default gateway as a single IPv6 address.

-   `--nodefroute`{.literal} - Prevents the interface being set as the default route. Use this option when you activate additional devices with the `--activate=`{.literal} option, for example, a NIC on a separate subnet for an iSCSI target.

-   `--nameserver=`{.literal} - DNS name server, as an IP address. To specify more than one name server, use this option once, and separate each IP address with a comma.

-   `--netmask=`{.literal} - Network mask for the installed system.

-   `--hostname=`{.literal} - Used to configure the target system's host name. The host name can either be a fully qualified domain name (FQDN) in the format `hostname.domainname`{.literal}, or a short host name without the domain. Many networks have a Dynamic Host Configuration Protocol (DHCP) service that automatically supplies connected systems with a domain name. To allow the DHCP service to assign the domain name to this machine, specify only the short host name.

    When using static IP and host name configuration, it depends on the planned system use case whether to use a short name or FQDN. Red Hat Identity Management configures FQDN during provisioning but some 3rd party software products may require a short name. In either case, to ensure availability of both forms in all situations, add an entry for the host in `/etc/hosts`{.literal} in the format `IP FQDN short-alias`{.literal}.

    Host names can only contain alphanumeric characters and `-`{.literal} or `.`{.literal}. Host name should be equal to or less than 64 characters. Host names cannot start or end with `-`{.literal} and `.`{.literal}. To be compliant with DNS, each part of a FQDN should be equal to or less than 63 characters. Also, the FQDN total length, including dots, should not exceed 255 characters.

    If you only want to configure the target system's host name, use the `--hostname`{.literal} option in the `network`{.literal} command and do not include any other option.

    If you provide additional options when configuring the host name, the `network`{.literal} command configures a device by using the options specified. If you do not specify which device to configure by using the `--device`{.literal} option, the default `--device link`{.literal} value is used. Additionally, if you do not specify the protocol by using the `--bootproto`{.literal} option, the device is configured to use DHCP by default.

-   `--ethtool=`{.literal} - Specifies additional low-level settings for the network device which will be passed to the ethtool program.

-   `--onboot=`{.literal} - Whether or not to enable the device at boot time.

-   `--dhcpclass=`{.literal} - The DHCP class.

-   `--mtu=`{.literal} - The MTU of the device.

-   `--noipv4`{.literal} - Disable IPv4 on this device.

-   `--noipv6`{.literal} - Disable IPv6 on this device.

-   `--bondslaves=`{.literal} - When this option is used, the bond device specified by the `--device=`{.literal} option is created using secondary devices defined in the `--bondslaves=`{.literal} option. For example:

    ``` {.language-plaintext tabindex="-1"}
    network --device=bond0 --bondslaves=em1,em2
    ```

    This command creates a bond device named `bond0`{.literal} by using the `em1`{.literal} and `em2`{.literal} interfaces as its secondary devices.

-   `--bondopts=`{.literal} - a list of optional parameters for a bonded interface, which is specified by using the `--bondslaves=`{.literal} and `--device=`{.literal} options. Options in this list must be separated by commas (",") or semicolons (";"). If an option itself contains a comma, use a semicolon to separate the options. For example:

    ``` {.language-plaintext tabindex="-1"}
    network --bondopts=mode=active-backup,balance-rr;primary=eth1
    ```

    Important

    The `--bondopts=mode=`{.literal} parameter only supports full mode names such as `balance-rr`{.literal} or `broadcast`{.literal}, not their numerical representations such as `0`{.literal} or `3`{.literal}. For the list of available and supported modes, see the [Configuring and Managing Networking Guide](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_networking/index#configuring-a-network-bond).

-   `--vlanid=`{.literal} - Specifies virtual LAN (VLAN) ID number (802.1q tag) for the device created by using the device specified in `--device=`{.literal} as a parent. For example, `network --device=em1 --vlanid=171`{.literal} creates a virtual LAN device `em1.171`{.literal}.

-   `--interfacename=`{.literal} - Specify a custom interface name for a virtual LAN device. This option should be used when the default name generated by the `--vlanid=`{.literal} option is not desirable. This option must be used along with `--vlanid=`{.literal}. For example:

    ``` {.language-plaintext tabindex="-1"}
    network --device=em1 --vlanid=171 --interfacename=vlan171
    ```

    This command creates a virtual LAN interface named `vlan171`{.literal} on the `em1`{.literal} device with an ID of `171`{.literal}.

    The interface name can be arbitrary (for example, `my-vlan`{.literal}), but in specific cases, the following conventions must be followed:

    -   If the name contains a dot (`.`{.literal}), it must take the form of *`NAME`{.literal}*`.`{.literal}*`ID`{.literal}*. The *NAME* is arbitrary, but the *ID* must be the VLAN ID. For example: `em1.171`{.literal} or `my-vlan.171`{.literal}.
    -   Names starting with `vlan`{.literal} must take the form of `vlan`{.literal}*`ID`{.literal}* - for example, `vlan171`{.literal}.

-   `--bridgeslaves=`{.literal} - When this option is used, the network bridge with the device name specified by using the `--device=`{.literal} option is created. Devices defined in the `--bridgeslaves=`{.literal} option are added to the bridge. For example:

    ``` {.language-plaintext tabindex="-1"}
    network --device=bridge0 --bridgeslaves=em1
    ```

-   `--bridgeopts=`{.literal} - An optional comma-separated list of parameters for the bridged interface. Available values are `stp`{.literal}, `priority`{.literal}, `forward-delay`{.literal}, `hello-time`{.literal}, `max-age`{.literal}, and `ageing-time`{.literal}. For information about these parameters, see the *bridge setting* table in the `nm-settings(5)`{.literal} man page or at [Network Configuration Setting Specification](https://developer.gnome.org/NetworkManager/0.9/ref-settings.html).

    Also see the [Configuring and managing networking](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_networking/index) document for general information about network bridging.

-   `--bindto=mac`{.literal} - Bind the device configuration file on the installed system to the device MAC address (`HWADDR`{.literal}) instead of the default binding to the interface name (`DEVICE`{.literal}). This option is independent of the `--device=`{.literal} option - `--bindto=mac`{.literal} will be applied even if the same `network`{.literal} command also specifies a device name, `link`{.literal}, or `bootif`{.literal}.

    Notes

    :   

-   The `ethN`{.literal} device names such as `eth0`{.literal} are no longer available in Red Hat Enterprise Linux due to changes in the naming scheme. For more information about the device naming scheme, see the upstream document [Predictable Network Interface Names](https://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/).

-   If you used a Kickstart or boot option to specify a network installation repository and no network is available at installation start, the installation program displays the **Network Configuration** window. Use this window to configure a network connection before the **Installation Summary** window appears. For more details, see [Configuring network and host name options](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/index#optional-configuring-the-network-and-host-name).

#### [22.4.2. realm](#realm) {#realm .title}

The `realm`{.literal} Kickstart command is optional. Use it to join an Active Directory or IPA domain. For more information about this command, see the `join`{.literal} section of the `realm(8)`{.literal} man page on your system.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    realm join [OPTIONS] domain
    ```

Mandatory options

:   -   *`domain`{.literal}* - The domain to join.

Options

:   -   `--computer-ou=OU=`{.literal} - Provide the distinguished name of an organizational unit to create the computer account. The exact format of the distinguished name depends on the client software and membership software. The root DSE portion of the distinguished name can usually be left out.
    -   `--no-password`{.literal} - Join automatically without a password.
    -   `--one-time-password=`{.literal} - Join using a one-time password. This is not possible with all types of realm.
    -   `--client-software=`{.literal} - Only join realms which can run this client software. Valid values include `sssd`{.literal} and `winbind`{.literal}. Not all realms support all values. By default, the client software is chosen automatically.
    -   `--server-software=`{.literal} - Only join realms which can run this server software. Possible values include `active-directory`{.literal} or `freeipa`{.literal}.
    -   `--membership-software=`{.literal} - Use this software when joining the realm. Valid values include `samba`{.literal} and `adcli`{.literal}. Not all realms support all values. By default, the membership software is chosen automatically.

### [22.5. Kickstart commands for handling storage](#kickstart-commands-for-handling-storage) {#kickstart-commands-for-handling-storage .title}

The Kickstart commands in this section configure aspects of storage such as devices, disks, partitions, LVM, and filesystems.

Important

The `sdX`{.literal} (or `/dev/sdX`{.literal}) format does not guarantee consistent device names across reboots, which can complicate the usage of some Kickstart commands. When a command requires a device node name, you can use any item from `/dev/disk`{.literal} as an alternative. For example, instead of using the following device name:

`part / --fstype=xfs --onpart=sda1`{.literal}

You can use an entry similar to one of the following:

`part / --fstype=xfs --onpart=/dev/disk/by-path/pci-0000:00:05.0-scsi-0:0:0:0-part1`{.literal}

`part / --fstype=xfs --onpart=/dev/disk/by-id/ata-ST3160815AS_6RA0C882-part1`{.literal}

By using this approach, the command always targets the same storage device. This is especially useful in large storage environments. To explore the available device names on the system, you can use the `ls -lR /dev/disk`{.literal} command during the interactive installation.

#### [22.5.1. ignoredisk](#ignoredisk) {#ignoredisk .title}

The `ignoredisk`{.literal} Kickstart command is optional. It causes the installation program to ignore the specified disks.

This is useful if you use automatic partitioning and want to be sure that some disks are ignored. For example, without `ignoredisk`{.literal}, attempting to deploy on a SAN-cluster the Kickstart would fail, as the installation program detects passive paths to the SAN that return no partition table. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    ignoredisk --drives=drive1,drive2,... | --only-use=drive
    ```

Options

:   -   `--drives=`{.literal}*`driveN`{.literal}*`,…​`{.literal} - Replace *driveN* with one of `sda`{.literal}, `sdb`{.literal},...​, `hda`{.literal},...​ and so on.

    -   `--only-use=`{.literal}*`driveN`{.literal}*`,…​`{.literal} - Specifies a list of disks for the installation program to use. All other disks are ignored. For example, to use disk `sda`{.literal} during installation and ignore all other disks:

        ``` {.language-plaintext tabindex="-1"}
        ignoredisk --only-use=sda
        ```

        To include a multipath device that does not use LVM:

        ``` {.language-plaintext tabindex="-1"}
        ignoredisk --only-use=disk/by-id/dm-uuid-mpath-2416CD96995134CA5D787F00A5AA11017
        ```

        To include a multipath device that uses LVM:

        ``` {.language-plaintext tabindex="-1"}
        ignoredisk --only-use=disk/by-id/scsi-58095BEC5510947BE8C0360F604351918
        ```

        You must specify only one of the `--drives`{.literal} or `--only-use`{.literal}.

Notes

:   -   To specify a multipath device, use the format `disk/by-id/scsi-WWID`{.literal}, where WWID is the world-wide identifier for the device. For example, to specify a disk with WWID `58095BEC5510947BE8C0360F604351918`{.literal}, use:

    ``` {.language-plaintext tabindex="-1"}
    ignoredisk --only-use=disk/by-id/scsi-58095BEC5510947BE8C0360F604351918
    ```

    This format is preferable for all multipath devices. If errors occur, multipath devices that do not use LVM can also use the `disk/by-id/dm-uuid-mpath-WWID`{.literal} format, where WWID is the world-wide identifier for the device. For example, to specify a disk with WWID `2416CD96995134CA5D787F00A5AA11017`{.literal}, use:

    ``` {.language-plaintext tabindex="-1"}
    ignoredisk --only-use=disk/by-id/dm-uuid-mpath-2416CD96995134CA5D787F00A5AA11017
    ```

    Never specify multipath devices by device names like mpatha. Device names such as this are not specific to a particular disk. The disk named /dev/mpatha during installation might not be the one that you expect it to be. Therefore, the clearpart command could target the wrong disk.

    -   The `sdX`{.literal} (or `/dev/sdX`{.literal}) format does not guarantee consistent device names across reboots, which can complicate the usage of some Kickstart commands. When a command requires a device node name, you can use any item from `/dev/disk`{.literal} as an alternative. For example, instead of using the following device name:

        ``` {.language-plaintext tabindex="-1"}
        ignoredisk --only-use=sda
        ```

        You can use an entry similar to one of the following:

        ``` {.language-plaintext tabindex="-1"}
        ignoredisk --only-use=/dev/disk/by-path/pci-0000:00:05.0-scsi-0:0:0:0
        ```

        ``` {.language-plaintext tabindex="-1"}
        ignoredisk --only-use=/dev/disk/by-id/ata-ST3160815AS_6RA0C882
        ```

        By using this approach, the command always targets the same storage device. This is especially useful in large storage environments. To explore the available device names on the system, you can use the `ls -lR /dev/disk`{.literal} command during the interactive installation. For more information about different ways to consistently refer to storage devices, see [Persistent naming attributes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_storage_devices/index#persistent-naming-attributes).

#### [22.5.2. clearpart](#clearpart) {#clearpart .title}

The `clearpart`{.literal} Kickstart command is optional. It removes partitions from the system, before creating new partitions. By default, no partitions are removed. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    clearpart OPTIONS
    ```

Options

:   -   `--all`{.literal} - Erases all partitions from the system.

    This option will erase all disks which can be reached by the installation program, including any attached network storage. Use this option with caution.

    You can prevent `clearpart`{.literal} from wiping storage you want to preserve by using the `--drives=`{.literal} option and specifying only the drives to clear. You can also attach network storage later, for example in the `%post`{.literal} section of the Kickstart file. Another option is to blocklist the kernel modules used to access network storage.

    -   `--drives=`{.literal} - Specifies which drives to clear partitions from. For example, the following clears all the partitions on the first two drives on the primary IDE controller:

        ``` {.language-plaintext tabindex="-1"}
        clearpart --drives=hda,hdb --all
        ```

        To clear a multipath device, use the format `disk/by-id/scsi-`{.literal}*`WWID`{.literal}*, where *WWID* is the world-wide identifier for the device. For example, to clear a disk with WWID `58095BEC5510947BE8C0360F604351918`{.literal}, use:

        ``` {.language-plaintext tabindex="-1"}
        clearpart --drives=disk/by-id/scsi-58095BEC5510947BE8C0360F604351918
        ```

        This format is preferable for all multipath devices. If errors occur, multipath devices that do not use LVM can also use the format `disk/by-id/dm-uuid-mpath-`{.literal}*`WWID`{.literal}*, where *WWID* is the world-wide identifier for the device. For example, to clear a disk with WWID `2416CD96995134CA5D787F00A5AA11017`{.literal}, use:

        ``` {.language-plaintext tabindex="-1"}
        clearpart --drives=disk/by-id/dm-uuid-mpath-2416CD96995134CA5D787F00A5AA11017
        ```

        Never specify multipath devices by device names like `mpatha`{.literal}. Device names such as this are not specific to a particular disk. The disk named `/dev/mpatha`{.literal} during installation might not be the one that you expect it to be. Therefore, the `clearpart`{.literal} command could target the wrong disk.

    -   `--initlabel`{.literal} - Initializes a disk (or disks) by creating a default disk label for all disks in their respective architecture that have been designated for formatting (for example, gpt for x86). Because `--initlabel`{.literal} can see all disks, it is important to ensure only those drives that are to be formatted are connected. Disks cleared by `clearpart`{.literal} will have the label created even in case the `--initlabel`{.literal} is not used.

        ``` {.language-plaintext tabindex="-1"}
        clearpart --initlabel --drives=names_of_disks
        ```

        For example:

        ``` {.language-plaintext tabindex="-1"}
        clearpart --initlabel --drives=dasda,dasdb,dasdc
        ```

    -   `--list=`{.literal} - Specifies which partitions to clear. This option overrides the `--all`{.literal} and `--linux`{.literal} options if used. Can be used across different drives. For example:

        ``` {.language-plaintext tabindex="-1"}
        clearpart --list=sda2,sda3,sdb1
        ```

    -   `--disklabel=`{.literal}*`LABEL`{.literal}* - Set the default disklabel to use. Only disklabels supported for the platform will be accepted. For example, on the 64-bit Intel and AMD architectures, the `msdos`{.literal} and `gpt`{.literal} disklabels are accepted, but `dasd`{.literal} is not accepted.

    -   `--linux`{.literal} - Erases all Linux partitions.

    -   `--none`{.literal} (default) - Do not remove any partitions.

    -   `--cdl`{.literal} - Reformat any LDL DASDs to CDL format.

Notes

:   -   On the `x86_64`{.literal} systems running in Legacy BIOS mode, the GPT disklabel is the default. To ensure these systems can boot properly with GPT, add a dedicated BIOS boot partition. For automated installations, consider using the `reqpart`{.literal} kickstart command to create this BIOS boot partition when required automatically. Optionally, use the `part`{.literal} kickstart command, for example: `part biosboot --size=1`{.literal}. If you prefer to stick with the older MBR partitioning scheme instead of GPT, you have two options:

        -   During a kickstart installation, use the `--disklabel msdos`{.literal} option with the `clearpart`{.literal} command.
        -   Alternatively, add the `inst.disklabel=mbr`{.literal} boot option at the installer's boot prompt.

    -   To specify a multipath device, use the format `disk/by-id/scsi-WWID`{.literal}, where WWID is the world-wide identifier for the device. For example, to specify a disk with WWID `58095BEC5510947BE8C0360F604351918`{.literal}, use:

        ``` {.language-plaintext tabindex="-1"}
        ignoredisk --only-use=disk/by-id/scsi-58095BEC5510947BE8C0360F604351918
        ```

        This format is preferable for all multipath devices. If errors occur, multipath devices that do not use LVM can also use the `disk/by-id/dm-uuid-mpath-WWID`{.literal} format, where WWID is the device world-wide identifier. For example, to specify a disk with WWID 2416CD96995134CA5D787F00A5AA11017, use:

        ``` {.language-plaintext tabindex="-1"}
        ignoredisk --only-use=disk/by-id/dm-uuid-mpath-2416CD96995134CA5D787F00A5AA11017
        ```

        Never specify multipath devices by device names like mpatha. Device names such as this are not specific to a particular disk. The disk named /dev/mpatha during installation might not be the one that you expect it to be. Therefore, the `ignoredisk`{.literal} command could target the wrong disk.

    -   The `sdX`{.literal} (or `/dev/sdX`{.literal}) format does not guarantee consistent device names across reboots, which can complicate the usage of some Kickstart commands. When a command requires a device node name, you can use any item from `/dev/disk`{.literal} as an alternative. For example, instead of using the following device name:

        ``` {.language-plaintext tabindex="-1"}
        clearpart --drives=sda
        ```

        You can use an entry similar to one of the following:

        ``` {.language-plaintext tabindex="-1"}
        clearpart --drives=/dev/disk/by-path/pci-0000:00:05.0-scsi-0:0:0:0
        ```

        ``` {.language-plaintext tabindex="-1"}
        clearpart --drives=/dev/disk/by-id/ata-ST3160815AS_6RA0C882
        ```

        By using this approach, the command always targets the same storage device. This is especially useful in large storage environments. To explore the available device names on the system, you can use the `ls -lR /dev/disk`{.literal} command during the interactive installation. For more information about different ways to consistently refer to storage devices, see [Persistent naming attributes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_storage_devices/index#persistent-naming-attributes).

    -   If the `clearpart`{.literal} command is used, then the `part --onpart`{.literal} command cannot be used on a logical partition.

#### [22.5.3. zerombr](#zerombr) {#zerombr .title}

The `zerombr`{.literal} Kickstart command is optional. The `zerombr`{.literal} initializes any invalid partition tables that are found on disks and destroys all of the contents of disks with invalid partition tables.

This command is required when performing an installation on an 64-bit IBM Z system with unformatted Direct Access Storage Device (DASD) disks. Otherwise, the unformatted disks are not formatted and used during the installation. Use this command only once. This command has no options.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    zerombr
    ```

Notes

:   -   On 64-bit IBM Z, if you specify `zerombr`{.literal}, any Direct Access Storage Device (DASD) visible to the installation program which is not already low-level formatted is automatically low-level formatted with `dasdfmt`{.literal}. The command also prevents user choice during interactive installations.
    -   If you do not specify `zerombr`{.literal} and there is at least one unformatted DASD visible to the installation program, a non-interactive Kickstart installation exits unsuccessfully.
    -   If you do not specify `zerombr`{.literal} and at least one unformatted DASD is visible to the installation program, the interactive installation exits. This occurs if the user does not agree to format all visible unformatted DASDs. To circumvent this, only activate those DASDs that you will use during installation. You can always add more DASDs after installation is complete.

#### [22.5.4. bootloader](#bootloader) {#bootloader .title}

The `bootloader`{.literal} Kickstart command is required. It specifies how the boot loader should be installed. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    bootloader [OPTIONS]
    ```

Options

:   -   `--append=`{.literal} - Specifies additional kernel parameters. To specify multiple parameters, separate them with spaces. For example:

    ``` {.language-plaintext tabindex="-1"}
    bootloader --location=mbr --append="hdd=ide-scsi ide=nodma"
    ```

    When the `plymouth`{.literal} package is installed, the `rhgb`{.literal} and `quiet`{.literal} parameters are automatically added. This happens even if you do not specify them here or do not use the `--append=`{.literal} command. To disable this behavior, explicitly disallow installation of `plymouth`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    %packages
    -plymouth
    %end
    ```

    This option is useful for disabling mechanisms which were implemented to mitigate the Meltdown and Spectre speculative execution vulnerabilities found in most modern processors (CVE-2017-5754, CVE-2017-5753, and CVE-2017-5715). In some cases, these mechanisms may be unnecessary, and keeping them enabled causes decreased performance with no improvement in security. To disable these mechanisms, add the options to do so into your Kickstart file - for example, `bootloader --append="nopti noibrs noibpb"`{.literal} on AMD64/Intel 64 systems.

    Warning

    Ensure your system is not at risk of attack before disabling any of the vulnerability mitigation mechanisms. See the [Red Hat vulnerability response article](https://access.redhat.com/security/vulnerabilities/speculativeexecution) for information about the Meltdown and Spectre vulnerabilities.

    -   `--boot-drive=`{.literal} - Specifies which drive the boot loader should be written to, and therefore which drive the computer will boot from. If you use a multipath device as the boot drive, specify the device by using its disk/by-id/dm-uuid-mpath-WWID name.

        Important

        The `--boot-drive=`{.literal} option is currently being ignored in Red Hat Enterprise Linux installations on 64-bit IBM Z systems by using the `zipl`{.literal} boot loader. When `zipl`{.literal} is installed, it determines the boot drive on its own.

    -   `--leavebootorder`{.literal} - This option is applicable for Power and UEFI systems. The installation program adds Red Hat Enterprise Linux 10 to the list of the installed systems in UEFI. It does not add the installed system to the boot order. All existing boot entries as well as their order are preserved.

    -   `--driveorder=`{.literal} - Specifies which drive is first in the BIOS boot order. For example:

        ``` {.language-plaintext tabindex="-1"}
        bootloader --driveorder=sda,hda
        ```

    -   `--location=`{.literal} - Specifies where the boot record is written. Valid values are the following:

        -   `mbr`{.literal} - The default option. Depends on whether the drive uses the Master Boot Record (MBR) or GUID Partition Table (GPT) scheme:

            On a GPT-formatted disk, this option installs stage 1.5 of the boot loader into the BIOS boot partition.

            On an MBR-formatted disk, stage 1.5 is installed into the empty space between the MBR and the first partition.

        -   `partition`{.literal} - Install the boot loader on the first sector of the partition containing the kernel.

        -   `none`{.literal} - Do not install the boot loader.

        In most cases, this option does not need to be specified.

    -   `--nombr`{.literal} - Do not install the boot loader to the MBR.

    -   `--password=`{.literal} - If using GRUB2, set the boot loader password to the one specified with this option. This should be used to restrict access to the GRUB2 shell, where arbitrary kernel options can be passed.

        If a password is specified, GRUB2 also asks for a user name. The user name is always `root`{.literal}.

    -   `--iscrypted`{.literal} - Normally, when you specify a boot loader password by using the `--password=`{.literal} option, it is stored in the Kickstart file in plain text. If you want to encrypt the password, use this option and an encrypted password.

        To generate an encrypted password, use the `grub2-mkpasswd-pbkdf2`{.literal} command, enter the password you want to use, and copy the command's output (the hash starting with `grub.pbkdf2`{.literal}) into the Kickstart file. An example `bootloader`{.literal} Kickstart entry with an encrypted password looks similar to the following:

        ``` {.language-plaintext tabindex="-1"}
        bootloader --iscrypted --password=grub.pbkdf2.sha512.10000.5520C6C9832F3AC3D149AC0B24BE69E2D4FB0DBEEDBD29CA1D30A044DE2645C4C7A291E585D4DC43F8A4D82479F8B95CA4BA4381F8550510B75E8E0BB2938990.C688B6F0EF935701FF9BD1A8EC7FE5BD2333799C98F28420C5CC8F1A2A233DE22C83705BB614EA17F3FDFDF4AC2161CEA3384E56EB38A2E39102F5334C47405E
        ```

    -   `--timeout=`{.literal} - Specifies the amount of time the boot loader waits before booting the default option (in seconds).

    -   `--default=`{.literal} - Sets the default boot image in the boot loader configuration.

    -   `--extlinux`{.literal} - Use the extlinux boot loader instead of GRUB2. This option only works on systems supported by extlinux.

    -   `--disabled`{.literal} - This option is a stronger version of `--location=none`{.literal}. While `--location=none`{.literal} disables boot loader installation, `--disabled`{.literal} disables boot loader installation and also disables installation of the package containing the boot loader, thus saving space.

Notes

:   -   Red Hat recommends setting up a boot loader password on every system. An unprotected boot loader can allow a potential attacker to modify the system's boot options and gain unauthorized access to the system.

    -   In some cases, a special partition is required to install the boot loader on AMD64, Intel 64, and 64-bit ARM systems. The type and size of this partition depend on whether the boot disk uses a Master Boot Record (MBR) or a GUID Partition Table (GPT) schema for the boot loader. For more information, see the [Configuring boot loader](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/index#configuring-boot-loader) section.

    -   The `sdX`{.literal} (or `/dev/sdX`{.literal}) format does not guarantee consistent device names across reboots, which can complicate the usage of some Kickstart commands. When a command requires a device node name, you can use any item from `/dev/disk`{.literal} as an alternative. For example, instead of using the following device name:

        ``` {.language-plaintext tabindex="-1"}
        bootloader --boot-drive=sda
        ```

        You can use an entry similar to one of the following:

        ``` {.language-plaintext tabindex="-1"}
        bootloader --boot-drive=/dev/disk/by-path/pci-0000:00:05.0-scsi-0:0:0:0
        bootloader --boot-drive=/dev/disk/by-id/ata-ST3160815AS_6RA0C882
        ```

        By using this approach, the command always targets the same storage device. This is especially useful in large storage environments. To explore the available device names on the system, you can use the `ls -lR /dev/disk`{.literal} command during the interactive installation. For more information about different ways to consistently refer to storage devices, see [Persistent naming attributes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_storage_devices/index#persistent-naming-attributes).

#### [22.5.5. autopart](#autopart) {#autopart .title}

The `autopart`{.literal} Kickstart command is optional. It automatically creates partitions.

The automatically created partitions are: a root (`/`{.literal}) partition (1 GiB or larger), a `swap`{.literal} partition, and an appropriate `/boot`{.literal} partition for the architecture. On large enough drives (50 GiB and larger), this also creates a `/home`{.literal} partition. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    autopart OPTIONS
    ```

Options

:   -   `--type=`{.literal} - Selects one of the predefined automatic partitioning schemes you want to use. Accepts the following values:

        -   `lvm`{.literal}: The LVM partitioning scheme.
        -   `plain`{.literal}: Regular partitions with no LVM.
        -   `thinp`{.literal}: The LVM Thin Provisioning partitioning scheme.

    -   `--fstype=`{.literal} - Selects one of the available file system types. The available values are `ext2`{.literal}, `ext3`{.literal}, `ext4`{.literal}, `xfs`{.literal}, and `vfat`{.literal}. The default file system is `xfs`{.literal}.

    -   `--nohome`{.literal} - Disables automatic creation of the `/home`{.literal} partition.

    -   `--nolvm`{.literal} - Do not use LVM for automatic partitioning. This option is equal to `--type=plain`{.literal}.

    -   `--noboot`{.literal} - Do not create a `/boot`{.literal} partition.

    -   `--noswap`{.literal} - Do not create a swap partition.

    -   `--encrypted`{.literal} - Encrypts all partitions with Linux Unified Key Setup (LUKS). This is equivalent to checking the **Encrypt partitions** checkbox on the initial partitioning screen during a manual graphical installation.

        Note

        When encrypting one or more partitions, Anaconda attempts to gather 256 bits of entropy to ensure the partitions are encrypted securely. Gathering entropy can take some time - the process will stop after a maximum of 10 minutes, regardless of whether sufficient entropy has been gathered.

        The process can be speed up by interacting with the installation system (typing on the keyboard or moving the mouse). If you are installing in a virtual machine, you can also attach a `virtio-rng`{.literal} device (a virtual random number generator) to the guest.

    -   `--luks-version=`{.literal}*`LUKS_VERSION`{.literal}* - Specifies which version of LUKS format should be used to encrypt the filesystem. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--passphrase=`{.literal} - Provides a default system-wide passphrase for all encrypted devices.

    -   `--escrowcert=`{.literal}*`URL_of_X.509_certificate`{.literal}* - Stores data encryption keys of all encrypted volumes as files in `/root`{.literal}, encrypted by using the X.509 certificate from the URL specified with *URL_of_X.509_certificate*. The keys are stored as a separate file for each encrypted volume. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--backuppassphrase`{.literal} - Adds a randomly-generated passphrase to each encrypted volume. Store these passphrases in separate files in `/root`{.literal}, encrypted by using the X.509 certificate specified with `--escrowcert`{.literal}. This option is only meaningful if `--escrowcert`{.literal} is specified.

    -   `--cipher=`{.literal} - Specifies the type of encryption to use if the Anaconda default aes-xts-plain64 is not satisfactory. You must use this option together with the `--encrypted`{.literal} option; by itself it has no effect. Available types of encryption are listed in the [Security hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/) document. For example, `aes-xts-plain64`{.literal}.

    -   `--pbkdf=`{.literal}*`PBKDF`{.literal}* - Sets Password-Based Key Derivation Function (PBKDF) algorithm for LUKS keyslot. See also the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--pbkdf-memory=`{.literal}*`PBKDF_MEMORY`{.literal}* - Sets the memory cost for PBKDF. See also the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--pbkdf-time=`{.literal}*`PBKDF_TIME`{.literal}* - Sets the number of milliseconds to spend with PBKDF passphrase processing. See also `--iter-time`{.literal} in the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified, and is mutually exclusive with `--pbkdf-iterations`{.literal}.

    -   `--pbkdf-iterations=`{.literal}*`PBKDF_ITERATIONS`{.literal}* - Sets the number of iterations directly and avoids PBKDF benchmark. See also `--pbkdf-force-iterations`{.literal} in the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified, and is mutually exclusive with `--pbkdf-time`{.literal}.

Notes

:   -   The `autopart`{.literal} option cannot be used together with the `part/partition`{.literal}, `raid`{.literal}, `logvol`{.literal}, or `volgroup`{.literal} options in the same Kickstart file.
    -   The `autopart`{.literal} command is not mandatory, but you must include it if there are no `part`{.literal} or `mount`{.literal} commands in your Kickstart script.
    -   It is recommended to use the `autopart --nohome`{.literal} Kickstart option when installing on a single FBA DASD of the CMS type. This ensures that the installation program does not create a separate `/home`{.literal} partition. The installation then proceeds successfully.
    -   If you lose the LUKS passphrase, any encrypted partitions and their data is completely inaccessible. There is no way to recover a lost passphrase. However, you can save encryption passphrases with the `--escrowcert`{.literal} and create backup encryption passphrases with the `--backuppassphrase`{.literal} options.
    -   Ensure that the disk sector sizes are consistent when using `autopart`{.literal}, `autopart --type=lvm`{.literal}, or `autopart=thinp`{.literal}.

#### [22.5.6. reqpart](#reqpart) {#reqpart .title}

The `reqpart`{.literal} Kickstart command is optional. It automatically creates partitions required by your hardware platform. These include a `/boot/efi`{.literal} partition for systems with UEFI firmware, a `biosboot`{.literal} partition for systems with BIOS firmware and GPT, and a `PRePBoot`{.literal} partition for IBM Power Systems.

Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    reqpart [--add-boot]
    ```

Options

:   -   `--add-boot`{.literal} - Creates a separate `/boot`{.literal} partition in addition to the platform-specific partition created by the base command.

Note

:   -   This command cannot be used together with `autopart`{.literal}, because `autopart`{.literal} does everything the `reqpart`{.literal} command does and, in addition, creates other partitions or logical volumes such as `/`{.literal} and `swap`{.literal}. In contrast with `autopart`{.literal}, this command only creates platform-specific partitions and leaves the rest of the drive empty, allowing you to create a custom layout.

#### [22.5.7. part or partition](#part-or-partition) {#part-or-partition .title}

The `part`{.literal} or `partition`{.literal} Kickstart command is required. It creates a partition on the system.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    part|partition mntpoint [OPTIONS]
    ```

Options

:   -   *mntpoint* - Where the partition is mounted. The value must be of one of the following forms:

        -   `/`{.literal}*`path`{.literal}*

            For example, `/`{.literal}, `/usr`{.literal}, `/home`{.literal}

        -   `swap`{.literal}

            The partition is used as swap space.

            To determine the size of the swap partition automatically, use the `--recommended`{.literal} option:

            ``` {.language-plaintext tabindex="-1"}
            swap --recommended
            ```

            The size assigned will be effective but not precisely calibrated for your system.

            To determine the size of the swap partition automatically but also allow extra space for your system to hibernate, use the `--hibernation`{.literal} option:

            ``` {.language-plaintext tabindex="-1"}
            swap --hibernation
            ```

            The size assigned will be equivalent to the swap space assigned by `--recommended`{.literal} plus the amount of RAM on your system. For the swap sizes assigned by these commands, see [Recommended Partitioning Scheme](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/index#recommended-partitioning-scheme) for AMD64, Intel 64, and 64-bit ARM systems.

        -   `raid.`{.literal}*`id`{.literal}*

            The partition is used for software RAID (see `raid`{.literal}).

        -   `pv.`{.literal}*`id`{.literal}*

            The partition is used for LVM (see `logvol`{.literal}).

        -   `biosboot`{.literal}

            The partition will be used for a BIOS Boot partition. A 1 MiB BIOS boot partition is necessary on BIOS-based AMD64 and Intel 64 systems using a GUID Partition Table (GPT); the boot loader will be installed into it. It is not necessary on UEFI systems. See also the `bootloader`{.literal} command.

        -   `/boot/efi`{.literal}

            An EFI System Partition. A 50 MiB EFI partition is necessary on UEFI-based AMD64, Intel 64, and 64-bit ARM; the recommended size is 200 MiB. It is not necessary on BIOS systems. See also the `bootloader`{.literal} command.

    -   `--size=`{.literal} - The minimum partition size in MiB. Specify an integer value here such as `500`{.literal} (do not include the unit). Installation fails if size specified is too small. Set the `--size`{.literal} value as the minimum amount of space you require. For size recommendations, see [Recommended Partitioning Scheme](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/index#recommended-partitioning-scheme).

    -   `--grow`{.literal} - Specifies the partition to grow to fill available space (if any), or up to the maximum size setting, if one is specified. If you use `--grow`{.literal} without setting `--maxsize=`{.literal} on a swap partition, Anaconda limits the maximum size of the swap partition. For systems that have less than 2 GiB of physical memory, the imposed limit is twice the amount of physical memory. For systems with more than 2 GiB, the imposed limit is the size of physical memory plus 2GiB.

    -   `--maxsize=`{.literal} - The maximum partition size in MiB when the partition is set to grow. Specify an integer value here such as `500`{.literal} (do not include the unit).

    -   `--noformat`{.literal} - Specifies that the partition should not be formatted, for use with the `--onpart`{.literal} command.

    -   `--onpart=`{.literal} or `--usepart=`{.literal} - Specifies the device on which to place the partition. Uses an existing blank device and formats it to the new specified type. For example:

        ``` {.language-plaintext tabindex="-1"}
        partition /home --onpart=hda1
        ```

        puts `/home`{.literal} on `/dev/hda1`{.literal}.

        These options can also add a partition to a logical volume. For example:

        ``` {.language-plaintext tabindex="-1"}
        partition pv.1 --onpart=hda2
        ```

        The device must already exist on the system; the `--onpart`{.literal} option will not create it.

        It is also possible to specify an entire drive, rather than a partition, in which case Anaconda will format and use the drive without creating a partition table. However, installation of GRUB2 is not supported on a device formatted in this way, and must be placed on a drive with a partition table.

        ``` {.language-plaintext tabindex="-1"}
        partition pv.1 --onpart=hdb
        ```

    -   `--ondisk=`{.literal} or `--ondrive=`{.literal} - Creates a partition (specified by the `part`{.literal} command) on an existing disk.This command always creates a partition. Forces the partition to be created on a particular disk. For example, `--ondisk=sdb`{.literal} puts the partition on the second SCSI disk on the system.

        Note

        To specify a multipath device, use the format `disk/by-id/scsi-WWID`{.literal}, where WWID is the world-wide identifier for the device. For example, to specify a disk with WWID `58095BEC5510947BE8C0360F604351918`{.literal}, use:

        ``` {.language-plaintext tabindex="-1"}
        part / --size=5000 --ondisk=disk/by-id/scsi-58095BEC5510947BE8C0360F604351918
        ```

        This format is preferable for all multipath devices. If errors occur, multipath devices that do not use LVM can also use the `disk/by-id/dm-uuid-mpath-WWID`{.literal} format, where WWID is the world-wide identifier for the device. For example, to specify a disk with WWID `2416CD96995134CA5D787F00A5AA11017`{.literal}, use:

        ``` {.language-plaintext tabindex="-1"}
        part / --size=5000 --ondisk=disk/by-id/dm-uuid-mpath-2416CD96995134CA5D787F00A5AA11017
        ```

        Never specify multipath devices by device names like mpatha. Device names such as this are not specific to a particular disk. The disk named /dev/mpatha during installation might not be the one that you expect it to be. Therefore, the `part`{.literal} command could target the wrong disk.

    -   `--asprimary`{.literal} - Forces the partition to be allocated as a *primary* partition. If the partition cannot be allocated as primary (usually due to too many primary partitions being already allocated), the partitioning process fails. This option only makes sense when the disk uses a Master Boot Record (MBR); for GUID Partition Table (GPT)-labeled disks this option has no meaning.

    -   `--fsprofile=`{.literal} - Specifies a usage type to be passed to the program that makes a filesystem on this partition. A usage type defines a variety of tuning parameters to be used when making a filesystem. For this option to work, the filesystem must support the concept of usage types and there must be a configuration file that lists valid types. For `ext2`{.literal}, `ext3`{.literal}, `ext4`{.literal}, this configuration file is `/etc/mke2fs.conf`{.literal}.

    -   `--mkfsoptions=`{.literal} - Specifies additional parameters to be passed to the program that makes a filesystem on this partition. This is similar to `--fsprofile`{.literal} but works for all filesystems, not just the ones that support the profile concept. No processing is done on the list of arguments, so they must be supplied in a format that can be passed directly to the mkfs program. This means multiple options should be comma-separated or surrounded by double quotes, depending on the filesystem. For example,

        ``` {.language-plaintext tabindex="-1"}
        part /opt/foo1 --size=512 --fstype=ext4 --mkfsoptions="-O ^has_journal,^flex_bg,^metadata_csum"
        ```

        ``` {.language-plaintext tabindex="-1"}
        part /opt/foo2 --size=512 --fstype=xfs --mkfsoptions="-m bigtime=0,finobt=0"
        ```

        For details, see the man pages of the filesystems you are creating. For example, `mkfs.ext4`{.literal} or `mkfs.xfs`{.literal}.

    -   `--fstype=`{.literal} - Sets the file system type for the partition. Valid values are `xfs`{.literal}, `ext2`{.literal}, `ext3`{.literal}, `ext4`{.literal}, `swap`{.literal}, `vfat`{.literal}, `efi`{.literal} and `biosboot`{.literal}.

    -   `--fsoptions`{.literal} - Specifies a free form string of options to be used when mounting the filesystem. This string will be copied into the `/etc/fstab`{.literal} file of the installed system and should be enclosed in quotes.

        Note

        In the EFI system partition (`/boot/efi`{.literal}), anaconda hard codes the value and ignores the users specified `--fsoptions`{.literal} values.

    -   `--label=`{.literal} - assign a label to an individual partition.

    -   `--recommended`{.literal} - Determine the size of the partition automatically. For details about the recommended scheme, see [Recommended Partitioning Scheme](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/index#recommended-partitioning-scheme) for AMD64, Intel 64, and 64-bit ARM. This option can only be used for partitions which result in a file system such as the `/boot`{.literal} partition and `swap`{.literal} space. It cannot be used to create LVM physical volumes or RAID members.

    -   `--onbiosdisk`{.literal} - Forces the partition to be created on a particular disk as discovered by the BIOS.

    -   `--encrypted`{.literal} - Specifies that this partition should be encrypted with Linux Unified Key Setup (LUKS) by using the passphrase provided in the `--passphrase`{.literal} option. If you do not specify a passphrase, Anaconda uses the default, system-wide passphrase set with the `autopart --passphrase`{.literal} command. It also stops the installation and prompts you to provide a passphrase if no default is set.

        Note

        When encrypting one or more partitions, Anaconda attempts to gather 256 bits of entropy to ensure the partitions are encrypted securely. Gathering entropy can take some time - the process will stop after a maximum of 10 minutes, regardless of whether sufficient entropy has been gathered. The process can be sped up by interacting with the installation system (typing on the keyboard or moving the mouse). If you are installing in a virtual machine, you can also attach a `virtio-rng`{.literal} device (a virtual random number generator) to the guest.

    -   `--luks-version=`{.literal}*`LUKS_VERSION`{.literal}* - Specifies which version of LUKS format should be used to encrypt the filesystem. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--passphrase=`{.literal} - Specifies the passphrase to use when encrypting this partition. You must use this option together with the `--encrypted`{.literal} option; by itself it has no effect.

    -   `--cipher=`{.literal} - Specifies the type of encryption to use if the Anaconda default aes-xts-plain64 is not satisfactory. You must use this option together with the `--encrypted`{.literal} option; by itself it has no effect. Available types of encryption are listed in the [Security hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/) document. For example, `aes-xts-plain64`{.literal}.

    -   `--escrowcert=`{.literal}*`URL_of_X.509_certificate`{.literal}* - Store data encryption keys of all encrypted partitions as files in `/root`{.literal}, encrypted by using the X.509 certificate from the URL specified with *URL_of_X.509_certificate*. The keys are stored as a separate file for each encrypted partition. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--backuppassphrase`{.literal} - Add a randomly-generated passphrase to each encrypted partition. Store these passphrases in separate files in `/root`{.literal}, encrypted by using the X.509 certificate specified with `--escrowcert`{.literal}. This option is only meaningful if `--escrowcert`{.literal} is specified.

    -   `--pbkdf=`{.literal}*`PBKDF`{.literal}* - Sets Password-Based Key Derivation Function (PBKDF) algorithm for LUKS keyslot. See also the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--pbkdf-memory=`{.literal}*`PBKDF_MEMORY`{.literal}* - Sets the memory cost for PBKDF. See also the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--pbkdf-time=`{.literal}*`PBKDF_TIME`{.literal}* - Sets the number of milliseconds to spend with PBKDF passphrase processing. See also `--iter-time`{.literal} in the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified, and is mutually exclusive with `--pbkdf-iterations`{.literal}.

    -   `--pbkdf-iterations=`{.literal}*`PBKDF_ITERATIONS`{.literal}* - Sets the number of iterations directly and avoids PBKDF benchmark. See also `--pbkdf-force-iterations`{.literal} in the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified, and is mutually exclusive with `--pbkdf-time`{.literal}.

    -   `--resize`{.literal} - Resize an existing partition. When using this option, specify the target size (in MiB) by using the `--size=`{.literal} option and the target partition by using the `--onpart=`{.literal} option.

Notes

:   -   The `part`{.literal} command is not mandatory, but you must include either `part`{.literal}, `autopart`{.literal} or `mount`{.literal} in your Kickstart script.

    -   If partitioning fails for any reason, diagnostic messages appear on virtual console 3.

    -   All partitions created are formatted as part of the installation process unless `--noformat`{.literal} and `--onpart`{.literal} are used.

    -   The `sdX`{.literal} (or `/dev/sdX`{.literal}) format does not guarantee consistent device names across reboots, which can complicate the usage of some Kickstart commands. When a command requires a device node name, you can use any item from `/dev/disk`{.literal} as an alternative. For example, instead of using the following device name:

        ``` {.language-plaintext tabindex="-1"}
        part / --fstype=xfs --onpart=sda1
        ```

        You can use an entry similar to one of the following:

        ``` {.language-plaintext tabindex="-1"}
        part / --fstype=xfs --onpart=/dev/disk/by-path/pci-0000:00:05.0-scsi-0:0:0:0-part1
        ```

        ``` {.language-plaintext tabindex="-1"}
        part / --fstype=xfs --onpart=/dev/disk/by-id/ata-ST3160815AS_6RA0C882-part1
        ```

        By using this approach, the command always targets the same storage device. This is especially useful in large storage environments. To explore the available device names on the system, you can use the `ls -lR /dev/disk`{.literal} command during the interactive installation. For more information about different ways to consistently refer to storage devices, see [Persistent naming attributes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_storage_devices/index#persistent-naming-attributes).

    -   If you lose the LUKS passphrase, any encrypted partitions and their data is completely inaccessible. There is no way to recover a lost passphrase. However, you can save encryption passphrases with the `--escrowcert`{.literal} and create backup encryption passphrases with the `--backuppassphrase`{.literal} options.

#### [22.5.8. raid](#raid) {#raid .title}

The `raid`{.literal} Kickstart command is optional. It assembles a software RAID device.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    raid mntpoint --level=level --device=device-name partitions*
    ```

Options

:   -   *mntpoint* - Location where the RAID file system is mounted. If it is `/`{.literal}, the RAID level must be 1 unless a boot partition (`/boot`{.literal}) is present. If a boot partition is present, the `/boot`{.literal} partition must be level 1 and the root (`/`{.literal}) partition can be any of the available types. The *partitions\** (which denotes that multiple partitions can be listed) lists the RAID identifiers to add to the RAID array.

    Important

    -   On IBM Power Systems, ensure the RAID metadata version is 0.90 or 1.0 if the RAID device was prepared and not reformatted during installation. This requirement applies when placing `/boot`{.literal} and `PReP`{.literal} partitions on the RAID device. The `mdadm`{.literal} metadata versions 1.1 and 1.2 are not supported for the `/boot`{.literal} and `PReP`{.literal} partitions.
    -   The `PReP`{.literal} Boot partitions are not required on PowerNV systems.

    -   `--level=`{.literal} - RAID level to use (0, 1, 4, 5, 6, or 10).

    -   `--device=`{.literal} - Name of the RAID device to use - for example, `--device=root`{.literal}.

        Important

        Do not use `mdraid`{.literal} names in the form of `md0`{.literal} - these names are not guaranteed to be persistent. Instead, use meaningful names such as `root`{.literal} or `swap`{.literal}. Using meaningful names creates a symbolic link from `/dev/md/`{.literal}*`name`{.literal}* to whichever `/dev/md`{.literal}*`X`{.literal}* node is assigned to the array.

        If you have an old (v0.90 metadata) array that you cannot assign a name to, you can specify the array by a filesystem label or UUID. For example, `--device=LABEL=root`{.literal} or `--device=UUID=93348e56-4631-d0f0-6f5b-45c47f570b88`{.literal}.

        You can use the UUID of the file system on the RAID device or UUID of the RAID device itself. The UUID of the RAID device should be in the `8-4-4-4-12`{.literal} format. UUID reported by mdadm is in the `8:8:8:8`{.literal} format which needs to be changed. For example `93348e56:4631d0f0:6f5b45c4:7f570b88`{.literal} should be changed to `93348e56-4631-d0f0-6f5b-45c47f570b88`{.literal}.

    -   `--chunksize=`{.literal} - Sets the chunk size of a RAID storage in KiB. In certain situations, using a different chunk size than the default (`512 Kib`{.literal}) can improve the performance of the RAID.

    -   `--spares=`{.literal} - Specifies the number of spare drives allocated for the RAID array. Spare drives are used to rebuild the array in case of drive failure.

    -   `--fsprofile=`{.literal} - Specifies a usage type to be passed to the program that makes a filesystem on this partition. A usage type defines a variety of tuning parameters to be used when making a filesystem. For this option to work, the filesystem must support the concept of usage types and there must be a configuration file that lists valid types. For ext2, ext3, and ext4, this configuration file is `/etc/mke2fs.conf`{.literal}.

    -   `--fstype=`{.literal} - Sets the file system type for the RAID array. Valid values are `xfs`{.literal}, `ext2`{.literal}, `ext3`{.literal}, `ext4`{.literal}, `swap`{.literal}, and `vfat`{.literal}.

    -   `--fsoptions=`{.literal} - Specifies a free form string of options to be used when mounting the filesystem. This string will be copied into the `/etc/fstab`{.literal} file of the installed system and should be enclosed in quotes. In the EFI system partition (`/boot/efi`{.literal}), anaconda hard codes the value and ignores the users specified `--fsoptions`{.literal} values.

    -   `--mkfsoptions=`{.literal} - Specifies additional parameters to be passed to the program that makes a filesystem on this partition. No processing is done on the list of arguments, so they must be supplied in a format that can be passed directly to the mkfs program. This means multiple options should be comma-separated or surrounded by double quotes, depending on the filesystem. For example,

        ``` {.language-plaintext tabindex="-1"}
        part /opt/foo1 --size=512 --fstype=ext4 --mkfsoptions="-O ^has_journal,^flex_bg,^metadata_csum"
        ```

        ``` {.language-plaintext tabindex="-1"}
        part /opt/foo2 --size=512 --fstype=xfs --mkfsoptions="-m bigtime=0,finobt=0"
        ```

        For details, see the man pages of the filesystems you are creating. For example, `mkfs.ext4`{.literal} or `mkfs.xfs`{.literal}.

    -   `--label=`{.literal} - Specify the label to give to the filesystem to be made. If the given label is already in use by another filesystem, a new label will be created.

    -   `--noformat`{.literal} - Use an existing RAID device and do not format the RAID array.

    -   `--useexisting`{.literal} - Use an existing RAID device and reformat it.

    -   `--encrypted`{.literal} - Specifies that this RAID device should be encrypted with Linux Unified Key Setup (LUKS) by using the passphrase provided in the `--passphrase`{.literal} option. If you do not specify a passphrase, Anaconda uses the default, system-wide passphrase set with the `autopart --passphrase`{.literal} command. It also stops the installation and prompts you to provide a passphrase if no default is set.

        Note

        When encrypting one or more partitions, Anaconda attempts to gather 256 bits of entropy to ensure the partitions are encrypted securely. Gathering entropy can take some time - the process will stop after a maximum of 10 minutes, regardless of whether sufficient entropy has been gathered.

        The process can be sped up by interacting with the installation system (typing on the keyboard or moving the mouse). If you are installing in a virtual machine, you can also attach a `virtio-rng`{.literal} device (a virtual random number generator) to the guest.

    -   `--luks-version=`{.literal}*`LUKS_VERSION`{.literal}* - Specifies which version of LUKS format should be used to encrypt the filesystem. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--cipher=`{.literal} - Specifies the type of encryption to use if the Anaconda default aes-xts-plain64 is not satisfactory. You must use this option together with the `--encrypted`{.literal} option; by itself it has no effect. Available types of encryption are listed in the [Security hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/) document. For example, `aes-xts-plain64`{.literal}.

    -   `--passphrase=`{.literal} - Specifies the passphrase to use when encrypting this RAID device. You must use this option together with the `--encrypted`{.literal} option; by itself it has no effect.

    -   `--escrowcert=`{.literal}*`URL_of_X.509_certificate`{.literal}* - Store the data encryption key for this device in a file in `/root`{.literal}, encrypted by using the X.509 certificate from the URL specified with *URL_of_X.509_certificate*. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--backuppassphrase`{.literal} - Add a randomly-generated passphrase to this device. Store the passphrase in a file in `/root`{.literal}, encrypted by using the X.509 certificate specified with `--escrowcert`{.literal}. This option is only meaningful if `--escrowcert`{.literal} is specified.

    -   `--pbkdf=`{.literal}*`PBKDF`{.literal}* - Sets Password-Based Key Derivation Function (PBKDF) algorithm for LUKS keyslot. See also the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--pbkdf-memory=`{.literal}*`PBKDF_MEMORY`{.literal}* - Sets the memory cost for PBKDF. See also the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--pbkdf-time=`{.literal}*`PBKDF_TIME`{.literal}* - Sets the number of milliseconds to spend with PBKDF passphrase processing. See also `--iter-time`{.literal} in the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified, and is mutually exclusive with `--pbkdf-iterations`{.literal}.

    -   `--pbkdf-iterations=`{.literal}*`PBKDF_ITERATIONS`{.literal}* - Sets the number of iterations directly and avoids PBKDF benchmark. See also `--pbkdf-force-iterations`{.literal} in the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified, and is mutually exclusive with `--pbkdf-time`{.literal}.

Example

:   The following example shows how to create a RAID level 1 partition for `/`{.literal}, and a RAID level 5 for `/home`{.literal}, assuming there are three SCSI disks on the system. It also creates three swap partitions, one on each drive.

    ``` {.language-plaintext tabindex="-1"}
    part raid.01 --size=6000 --ondisk=sda
    part raid.02 --size=6000 --ondisk=sdb
    part raid.03 --size=6000 --ondisk=sdc
    part swap --size=512 --ondisk=sda
    part swap --size=512 --ondisk=sdb
    part swap --size=512 --ondisk=sdc
    part raid.11 --size=1 --grow --ondisk=sda
    part raid.12 --size=1 --grow --ondisk=sdb
    part raid.13 --size=1 --grow --ondisk=sdc
    raid / --level=1 --device=rhel8-root --label=rhel8-root raid.01 raid.02 raid.03
    raid /home --level=5 --device=rhel8-home --label=rhel8-home raid.11 raid.12 raid.13
    ```

Note

:   -   If you lose the LUKS passphrase, any encrypted partitions and their data is completely inaccessible. There is no way to recover a lost passphrase. However, you can save encryption passphrases with the `--escrowcert`{.literal} and create backup encryption passphrases with the `--backuppassphrase`{.literal} options.

#### [22.5.9. volgroup](#volgroup) {#volgroup .title}

The `volgroup`{.literal} Kickstart command is optional. It creates a Logical Volume Manager (LVM) group.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    volgroup name [OPTIONS] [partition*]
    ```

Mandatory options

:   -   *name* - Name of the new volume group.

Options

:   -   *partition* - Physical volume partitions to use as backing storage for the volume group. At least one partition has to be specified when creating a new volume group.

    -   `--noformat`{.literal} - Use an existing volume group and do not format it.

    -   `--useexisting`{.literal} - Use an existing volume group and reformat it. If you use this option, do not specify a *partition*. For example:

        ``` {.language-plaintext tabindex="-1"}
        volgroup rhel00 --useexisting --noformat
        ```

    -   `--pesize=`{.literal} - Set the size of the volume group's physical extents in KiB. The default value is 4096 (4 MiB), and the minimum value is 1024 (1 MiB).

    -   `--reserved-space=`{.literal} - Specify an amount of space to leave unused in a volume group in MiB. Applicable only to newly created volume groups.

    -   `--reserved-percent=`{.literal} - Specify a percentage of total volume group space to leave unused. Applicable only to newly created volume groups.

Notes

:   -   Create the partition first, then create the logical volume group, and then create the logical volume. For example:

    ``` {.language-plaintext tabindex="-1"}
    part pv.01 --size 10000
    volgroup my_volgrp pv.01
    logvol / --vgname=my_volgrp --size=2000 --name=root
    ```

    -   Do not use the dash (`-`{.literal}) character in logical volume and volume group names when installing Red Hat Enterprise Linux by using Kickstart. If this character is used, the installation finishes normally, but the `/dev/mapper/`{.literal} directory will list these volumes and volume groups with every dash doubled. For example, a volume group named `volgrp-01`{.literal} containing a logical volume named `logvol-01`{.literal} will be listed as `/dev/mapper/volgrp--01-logvol--01`{.literal}.

        This limitation only applies to newly created logical volume and volume group names. If you are reusing existing ones by using the `--noformat`{.literal} option, their names will not be changed.

#### [22.5.10. logvol](#logvol) {#logvol .title}

The `logvol`{.literal} Kickstart command is optional. It creates a logical volume for Logical Volume Manager (LVM).

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    logvol mntpoint --vgname=name --name=name [OPTIONS]
    ```

Mandatory options

:   -   *`mntpoint`{.literal}*: The mount point where the partition is mounted. Must be of one of the following forms:

        -   `/`{.literal}*`path`{.literal}*

            For example, `/`{.literal} or `/home`{.literal}

        -   `swap`{.literal}

            The partition is used as swap space.

            To determine the size of the swap partition automatically, use the `--recommended`{.literal} option:

            ``` {.language-plaintext tabindex="-1"}
            swap --recommended
            ```

            To determine the size of the swap partition automatically and also allow extra space for your system to hibernate, use the `--hibernation`{.literal} option:

            ``` {.language-plaintext tabindex="-1"}
            swap --hibernation
            ```

            The size assigned will be equivalent to the swap space assigned by `--recommended`{.literal} plus the amount of RAM on your system. For the swap sizes assigned by these commands, see [Recommended Partitioning Scheme](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/index#recommended-partitioning-scheme) for AMD64, Intel 64, and 64-bit ARM systems.

    -   `--vgname=`{.literal}*`name`{.literal}*: Name of the volume group.

    -   `--name=`{.literal}*`name`{.literal}*: Name of the logical volume.

Optional options

:   -   `--noformat`{.literal}: Use an existing logical volume and do not format it.

    -   `--useexisting`{.literal}: Use an existing logical volume and reformat it.

    -   `--fstype=`{.literal}: Sets the file system type for the logical volume. Valid values are `xfs`{.literal}, `ext2`{.literal}, `ext3`{.literal}, `ext4`{.literal}, `swap`{.literal}, and `vfat`{.literal}.

    -   `--fsoptions=`{.literal}: Specifies a free form string of options to be used when mounting the filesystem. This string will be copied into the `/etc/fstab`{.literal} file of the installed system and should be enclosed in quotes.

        Note

        In the EFI system partition (`/boot/efi`{.literal}), anaconda hard codes the value and ignores the users specified `--fsoptions`{.literal} values.

    -   `--mkfsoptions=`{.literal}: Specifies additional parameters to be passed to the program that makes a filesystem on this partition. No processing is done on the list of arguments, so they must be supplied in a format that can be passed directly to the mkfs program. This means multiple options should be comma-separated or surrounded by double quotes, depending on the filesystem. For example,

        ``` {.language-plaintext tabindex="-1"}
        part /opt/foo1 --size=512 --fstype=ext4 --mkfsoptions="-O ^has_journal,^flex_bg,^metadata_csum"
        ```

        ``` {.language-plaintext tabindex="-1"}
        part /opt/foo2 --size=512 --fstype=xfs --mkfsoptions="-m bigtime=0,finobt=0"
        ```

        For details, see the man pages of the filesystems you are creating. For example, `mkfs.ext4`{.literal} or `mkfs.xfs`{.literal}.

    -   `--fsprofile=`{.literal}: Specifies a usage type to be passed to the program that makes a filesystem on this partition. A usage type defines a variety of tuning parameters to be used when making a filesystem. For this option to work, the filesystem must support the concept of usage types and there must be a configuration file that lists valid types. For `ext2`{.literal}, `ext3`{.literal}, and `ext4`{.literal}, this configuration file is `/etc/mke2fs.conf`{.literal}.

    -   `--label=`{.literal}: Sets a label for the logical volume.

    -   `--grow`{.literal}: Extends the logical volume to occupy the available space (if any), or up to the maximum size specified, if any. The option must be used only if you have pre-allocated a minimum storage space in the disk image, and would want the volume to grow and occupy the available space. In a physical environment, this is a one-time-action. However, in a virtual environment, the volume size increases as and when the virtual machine writes any data to the virtual disk.

    -   `--size=`{.literal}: The size of the logical volume in MiB. This option cannot be used together with the `--percent=`{.literal} option.

    -   `--percent=`{.literal}: The size of the logical volume, as a percentage of the free space in the volume group after any statically-sized logical volumes are taken into account. This option cannot be used together with the `--size=`{.literal} option.

        Important

        When creating a new logical volume, either specify its size statically by using the `--size=`{.literal} option, or as a percentage of remaining free space by using the `--percent=`{.literal} option. You cannot use both of these options on the same logical volume.

    -   `--maxsize=`{.literal}: The maximum size in MiB when the logical volume is set to grow. Specify an integer value here such as `500`{.literal} (do not include the unit).

    -   `--recommended`{.literal}: Use this option when creating a logical volume to determine the size of this volume automatically, based on your system's hardware. For details about the recommended scheme, see [Recommended Partitioning Scheme](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/index#recommended-partitioning-scheme) for AMD64, Intel 64, and 64-bit ARM systems.

    -   `--resize`{.literal}: Resize a logical volume. If you use this option, you must also specify `--useexisting`{.literal} and `--size`{.literal}.

    -   `--encrypted`{.literal}: Specifies that this logical volume should be encrypted with Linux Unified Key Setup (LUKS) by using the passphrase provided in the `--passphrase=`{.literal} option. If you do not specify a passphrase, the installation program stops the installation and prompts you to provide a passphrase if no default is set.

        Note

        When encrypting one or more partitions, Anaconda attempts to gather 256 bits of entropy to ensure the partitions are encrypted securely. Gathering entropy can take some time - the process will stop after a maximum of 10 minutes, regardless of whether sufficient entropy has been gathered. The process can be sped up by interacting with the installation system (typing on the keyboard or moving the mouse). If you are installing in a virtual machine, you can also attach a `virtio-rng`{.literal} device (a virtual random number generator) to the guest.

    -   `--passphrase=`{.literal}: Specifies the passphrase to use when encrypting this logical volume. You must use this option together with the `--encrypted`{.literal} option; it has no effect by itself.

    -   `--cipher=`{.literal}: Specifies the type of encryption to use if the Anaconda default aes-xts-plain64 is not satisfactory. You must use this option together with the `--encrypted`{.literal} option; by itself it has no effect. Available types of encryption are listed in [Security hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/). For example, `aes-xts-plain64`{.literal}.

    -   `--escrowcert=`{.literal}*`URL_of_X.509_certificate`{.literal}*: Store data encryption keys of all encrypted volumes as files in `/root`{.literal}, encrypted by using the X.509 certificate from the URL specified with *URL_of_X.509_certificate*. The keys are stored as a separate file for each encrypted volume. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--luks-version=`{.literal}*`LUKS_VERSION`{.literal}*: Specifies which version of LUKS format should be used to encrypt the filesystem. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--backuppassphrase`{.literal}: Add a randomly-generated passphrase to each encrypted volume. Store these passphrases in separate files in `/root`{.literal}, encrypted by using the X.509 certificate specified with `--escrowcert`{.literal}. This option is only meaningful if `--escrowcert`{.literal} is specified.

    -   `--pbkdf=`{.literal}*`PBKDF`{.literal}*: Sets Password-Based Key Derivation Function (PBKDF) algorithm for LUKS keyslot. See also the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--pbkdf-memory=`{.literal}*`PBKDF_MEMORY`{.literal}*: Sets the memory cost for PBKDF. See also the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified.

    -   `--pbkdf-time=`{.literal}*`PBKDF_TIME`{.literal}*: Sets the number of milliseconds to spend with PBKDF passphrase processing. See also `--iter-time`{.literal} in the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified, and is mutually exclusive with `--pbkdf-iterations`{.literal}.

    -   `--pbkdf-iterations=`{.literal}*`PBKDF_ITERATIONS`{.literal}*: Sets the number of iterations directly and avoids PBKDF benchmark. See also `--pbkdf-force-iterations`{.literal} in the man page *cryptsetup(8)*. This option is only meaningful if `--encrypted`{.literal} is specified, and is mutually exclusive with `--pbkdf-time`{.literal}.

    -   `--thinpool`{.literal}: Creates a thin pool of logical volume. (Use a mount point of `none`{.literal})

    -   `--metadatasize=`{.literal}*`size`{.literal}*: Specify the metadata area size (in MiB) for a new thin pool device.

    -   `--chunksize=`{.literal}*`size`{.literal}*: Specify the chunk size (in KiB) for a new thin pool device.

    -   `--thin`{.literal}: Create a thin logical volume. (Requires use of `--poolname`{.literal})

    -   `--poolname=`{.literal}*`name`{.literal}*: Specify the name of the thin pool in which to create a thin logical volume. Requires the `--thin`{.literal} option.

    -   `--profile=`{.literal}*`name`{.literal}*: Specify the configuration profile name to use with thin logical volumes. If used, the name will also be included in the metadata for the given logical volume. By default, the available profiles are `default`{.literal} and `thin-performance`{.literal} and are defined in the `/etc/lvm/profile/`{.literal} directory. See the `lvm(8)`{.literal} man page for additional information.

    -   `--cachepvs=`{.literal}: A comma-separated list of physical volumes which should be used as a cache for this volume.

    -   `--cachemode=`{.literal}: Specify which mode should be used to cache this logical volume - either `writeback`{.literal} or `writethrough`{.literal}.

        Note

        For more information about cached logical volumes and their modes, see the `lvmcache(7)`{.literal} man page on your system.

    -   `--cachesize=`{.literal}: Size of cache attached to the logical volume, specified in MiB. This option requires the `--cachepvs=`{.literal} option.

Notes

:   -   Do not use the dash (`-`{.literal}) character in logical volume and volume group names when installing Red Hat Enterprise Linux by using Kickstart. If this character is used, the installation finishes normally, but the `/dev/mapper/`{.literal} directory will list these volumes and volume groups with every dash doubled. For example, a volume group named `volgrp-01`{.literal} containing a logical volume named `logvol-01`{.literal} will be listed as `/dev/mapper/volgrp—​01-logvol—​01`{.literal}. This limitation only applies to newly created logical volume and volume group names. If you are reusing existing ones by using the `--noformat`{.literal} option, their names will not be changed.
    -   If you lose the LUKS passphrase, any encrypted partitions and their data is completely inaccessible. There is no way to recover a lost passphrase. However, you can save encryption passphrases with the `--escrowcert`{.literal} and create backup encryption passphrases with the `--backuppassphrase`{.literal} options.

Examples

:   -   Create the partition first, create the volume group, and then create the logical volume:

    ``` {.language-plaintext tabindex="-1"}
    part pv.01 --size 3000
    volgroup myvg pv.01
    logvol / --vgname=myvg --size=2000 --name=rootvol
    ```

    -   Create the partition first, create the volume group, and then create the logical volume to occupy 90% of the remaining space in the volume group:

        ``` {.language-plaintext tabindex="-1"}
        part pv.01 --size 1 --grow
        volgroup myvg pv.01
        logvol / --vgname=myvg --name=rootvol --percent=90
        ```

**Additional resources**

-   [Configuring and managing logical volumes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_logical_volumes/index)

#### [22.5.11. snapshot](#snapshot) {#snapshot .title}

The `snapshot`{.literal} Kickstart command is optional. Use it to create LVM thin volume snapshots during the installation process. This enables you to back up a logical volume before or after the installation.

To create multiple snapshots, add the `snaphost`{.literal} Kickstart command multiple times.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    snapshot vg_name/lv_name --name=snapshot_name --when=pre-install|post-install
    ```

Options

:   -   *`vg_name`{.literal}*`/`{.literal}*`lv_name`{.literal}* - Sets the name of the volume group and logical volume to create the snapshot from.
    -   `--name=`{.literal}*`snapshot_name`{.literal}* - Sets the name of the snapshot. This name must be unique within the volume group.
    -   `--when=`{.literal}*`pre-install|post-install`{.literal}* - Sets if the snapshot is created before the installation begins or after the installation is completed.

#### [22.5.12. mount](#mount) {#mount .title}

The `mount`{.literal} Kickstart command is optional. It assigns a mount point to an existing block device, and optionally reformats it to a given format.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    mount [OPTIONS] device mountpoint
    ```

Mandatory options

:   -   *`device`{.literal}* - The block device to mount.
    -   *`mountpoint`{.literal}* - Where to mount the *`device`{.literal}*. It must be a valid mount point, such as `/`{.literal} or `/usr`{.literal}, or `none`{.literal} if the device is unmountable (for example `swap`{.literal}).

Optional options

:   -   `--reformat=`{.literal} - Specifies a new format (such as `ext4`{.literal}) to which the device should be reformatted.
    -   `--mkfsoptions=`{.literal} - Specifies additional options to be passed to the command which creates the new file system specified in `--reformat=`{.literal}. The list of options provided here is not processed, so they must be specified in a format that can be passed directly to the `mkfs`{.literal} program. The list of options should be either comma-separated or surrounded by double quotes, depending on the file system. See the `mkfs`{.literal} man page for the file system you want to create (for example `mkfs.ext4(8)`{.literal} or `mkfs.xfs(8)`{.literal}) for specific details.
    -   `--mountoptions=`{.literal} - Specifies a free form string that contains options to be used when mounting the file system. The string will be copied to the `/etc/fstab`{.literal} file on the installed system and should be enclosed in double quotes. See the `mount(8)`{.literal} man page for a full list of mount options, and `fstab(5)`{.literal} for basics.

Notes

:   -   Unlike most other storage configuration commands in Kickstart, `mount`{.literal} does not require you to describe the entire storage configuration in the Kickstart file. You only need to ensure that the described block device exists on the system. However, if you want to *create* the storage stack with all the devices mounted, you must use other commands such as `part`{.literal} to do so.
    -   You cannot use `mount`{.literal} together with other storage-related commands such as `part`{.literal}, `logvol`{.literal}, or `autopart`{.literal} in the same Kickstart file.

#### [22.5.13. zipl](#zipl) {#zipl .title}

The `zipl`{.literal} Kickstart command is optional. It specifies the ZIPL configuration for 64-bit IBM Z. Use this command only once.

Options

:   -   `--secure-boot`{.literal} - Enables secure boot if it is supported by the installing system.
    -   `--no-secure-boot`{.literal} - Disables secure boot.
    -   `--force-secure-boot`{.literal} - Enables secure boot unconditionally.

Notes

:   -   When installed on a system that is later than IBM z14, the installed system cannot be booted from an IBM z14 or earlier model.
    -   Secure Boot is not supported on IBM z14 and earlier models. Use `--no-secure-boot`{.literal} if you intend to boot the installed system on IBM z14 and earlier models.

#### [22.5.14. fcoe](#fcoe) {#fcoe .title}

The `fcoe`{.literal} Kickstart command is optional. It specifies which FCoE devices should be activated automatically in addition to those discovered by Enhanced Disk Drive Services (EDD).

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    fcoe --nic=name [OPTIONS]
    ```

Options

:   -   `--nic=`{.literal} (required) - The name of the device to be activated.
    -   `--dcb=`{.literal} - Establish Data Center Bridging (DCB) settings.
    -   `--autovlan`{.literal} - Discover VLANs automatically. This option is enabled by default.

#### [22.5.15. iscsi](#iscsi) {#iscsi .title}

The `iscsi`{.literal} Kickstart command is optional. It specifies additional iSCSI storage to be attached during installation.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    iscsi --ipaddr=address [OPTIONS]
    ```

Mandatory options

:   -   `--ipaddr=`{.literal} (required) - the IP address of the target to connect to.

Optional options

:   -   `--port=`{.literal} (required) - the port number. If not present, `--port=3260`{.literal} is used automatically by default.
    -   `--target=`{.literal} - the target IQN (iSCSI Qualified Name).
    -   `--iface=`{.literal} - bind the connection to a specific network interface instead of using the default one determined by the network layer. Once used, it must be specified in all instances of the `iscsi`{.literal} command in the entire Kickstart file.
    -   `--user=`{.literal} - the user name required to authenticate with the target
    -   `--password=`{.literal} - the password that corresponds with the user name specified for the target
    -   `--reverse-user=`{.literal} - the user name required to authenticate with the initiator from a target that uses reverse CHAP authentication
    -   `--reverse-password=`{.literal} - the password that corresponds with the user name specified for the initiator

Notes

:   -   If you use the `iscsi`{.literal} command, you must also assign a name to the iSCSI node by using the `iscsiname`{.literal} command. The `iscsiname`{.literal} command must appear before the `iscsi`{.literal} command in the Kickstart file.
    -   Wherever possible, configure iSCSI storage in the system BIOS or firmware (iBFT for Intel systems) rather than use the `iscsi`{.literal} command. Anaconda automatically detects and uses disks configured in BIOS or firmware and no special configuration is necessary in the Kickstart file.
    -   If you must use the `iscsi`{.literal} command, ensure that networking is activated at the beginning of the installation. The `iscsi`{.literal} command must appear in the Kickstart file *before* you refer to iSCSI disks with commands such as `clearpart`{.literal} or `ignoredisk`{.literal}.

#### [22.5.16. iscsiname](#iscsiname) {#iscsiname .title}

The `iscsiname`{.literal} Kickstart command is optional. It assigns a name to an iSCSI node specified by the `iscsi`{.literal} command. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    iscsiname iqname
    ```

Options

:   -   *`iqname`{.literal}* - Name to assign to the iSCSI node.

Note

:   -   If you use the `iscsi`{.literal} command in your Kickstart file, you must specify `iscsiname`{.literal} *earlier* in the Kickstart file.

#### [22.5.17. zfcp](#zfcp) {#zfcp .title}

The `zfcp`{.literal} Kickstart command is optional. It defines a Fibre channel device.

This option only applies on 64-bit IBM Z.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    zfcp --devnum=devnum [--wwpn=wwpn --fcplun=lun]
    ```

Options

:   -   `--devnum=`{.literal} - The device number (zFCP adapter device bus ID).
    -   `--wwpn=`{.literal} - The device's World Wide Port Name (WWPN). Takes the form of a 16-digit number, preceded by `0x`{.literal}.
    -   `--fcplun=`{.literal} - The device's Logical Unit Number (LUN). Takes the form of a 16-digit number, preceded by `0x`{.literal}.

Example

:   

``` {.language-plaintext tabindex="-1"}
zfcp --devnum=0.0.4000 --wwpn=0x5005076300C213e9 --fcplun=0x5022000000000000
zfcp --devnum=0.0.4000
```

#### [22.5.18. Additional resources](#kickstart-commands-for-handling-storage_22518-additional-resources) {#additional-resources-2 .title}

-   [Persistent naming attributes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_storage_devices/index#persistent-naming-attributes)

### [22.6. Kickstart commands for addons supplied with the RHEL installation program](#kickstart-commands-for-addons-supplied-with-the-rhel-installation-program) {#kickstart-commands-for-addons-supplied-with-the-rhel-installation-program .title}

The Kickstart commands in this section are related to add-ons supplied by default with the Red Hat Enterprise Linux installation program.

#### [22.6.1. %addon com_redhat_kdump](#addon-comredhatkdump) {#addon-com_redhat_kdump .title}

The `%addon com_redhat_kdump`{.literal} Kickstart command is optional. This command configures the kdump kernel crash dumping mechanism.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    %addon com_redhat_kdump [OPTIONS]
    %end
    ```

Note

The syntax for this command is different because it is an add-on rather than a built-in Kickstart command.

Kdump is a kernel crash dumping mechanism that you can use to save the contents of the system's memory for later analysis. It relies on `kexec`{.literal}, which you can use to boot a Linux kernel from the context of another kernel without rebooting the system. It also preserves the contents of the first kernel's memory that would otherwise be lost.

In case of a system crash, `kexec`{.literal} boots into a second kernel (a capture kernel). This capture kernel resides in a reserved part of the system memory. Kdump then captures the contents of the crashed kernel's memory (a crash dump) and saves it to a specified location. The location cannot be configured using this Kickstart command; it must be configured after the installation by editing the `/etc/kdump.conf`{.literal} configuration file.

For more information about Kdump, see the [Installing kdump](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/index#what-is-kdump).

Options

:   -   `--enable`{.literal} - Enable kdump on the installed system.

    -   `--disable`{.literal} - Disable kdump on the installed system.

    -   `--reserve-mb=`{.literal} - The amount of memory you want to reserve for kdump, in MiB. For example:

        ``` {.language-plaintext tabindex="-1"}
        %addon com_redhat_kdump --enable --reserve-mb=128
        %end
        ```

        You can also specify `auto`{.literal} instead of a numeric value. In that case, the installation program will determine the amount of memory automatically based on the criteria described in the [Memory requirements for kdump](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/index#memory-requirements-for-kdump) section of the *Managing, monitoring and updating the kernel* document.

        If you enable kdump and do not specify a `--reserve-mb=`{.literal} option, the value `auto`{.literal} will be used.

    -   `--enablefadump`{.literal} - Enable firmware-assisted dumping on systems which allow it (notably, IBM Power Systems servers).

### [22.7. Kickstart commands for system recovery](#kickstart-commands-for-system-recovery) {#kickstart-commands-for-system-recovery .title}

The Kickstart command in this section repairs an installed system.

#### [22.7.1. rescue](#rescue) {#rescue .title}

The `rescue`{.literal} Kickstart command is optional. It provides a shell environment with root privileges and a set of system management tools to repair the installation and to troubleshoot the issues like:

-   Mount file systems as read-only
-   Blocklist or add a driver provided on a driver disc
-   Install or upgrade system packages
-   Manage partitions

Note

The Kickstart rescue mode is different from the rescue mode and emergency mode, which are provided as part of the systemd and service manager.

The `rescue`{.literal} command does not modify the system on its own. It only sets up the rescue environment by mounting the system under /mnt/sysroot in a read-write mode. You can choose not to mount the system, or to mount it in read-only mode. Use this command only once.

Syntax

:   ``` {.language-plaintext tabindex="-1"}
    rescue [--nomount|--romount]
    ```

Options

:   -   `--nomount`{.literal} or `--romount`{.literal} - Controls how the installed system is mounted in the rescue environment. By default, the installation program finds your system and mount it in read-write mode, telling you where it has performed this mount. You can optionally select to not mount anything (the `--nomount`{.literal} option) or mount in read-only mode (the `--romount`{.literal} option). Only one of these two options can be used.

Notes

:   To run a rescue mode, make a copy of the Kickstart file, and include the `rescue`{.literal} command in it. Using the `rescue`{.literal} command causes the installer to perform the following steps:

    1.  Run the `%pre`{.literal} script.

    2.  Configure the environment for rescue mode.

        The following kickstart commands take effect:

        a.  updates
        b.  sshpw
        c.  logging
        d.  lang
        e.  network

    3.  Configure an advanced storage environment.

        The following kickstart commands take effect:

        a.  fcoe
        b.  iscsi
        c.  iscsiname
        d.  nvdimm
        e.  zfcp

    4.  Mount the system.

        ``` {.language-plaintext tabindex="-1"}
        rescue [--nomount|--romount]
        ```

    5.  Run %post script

        This step is run only if the installed system is mounted in read-write mode.

    6.  Start shell.

    7.  Reboot system.

## [Chapter 23. Boot options reference](#boot-options-reference) {#chapter-23.-boot-options-reference .title}

You can use the boot options to modify the default behavior of the installation program.

### [23.1. Installation source boot options](#installation-source-boot-options) {#installation-source-boot-options .title}

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
        | CD/DVD drive                                                                                                                                                                                                                               | `inst.repo=cdrom:`{.literal}*`<device>`{.literal}*                                                                                                          | Installation DVD as a physical disk. [^\[a\]^](#ftn.idm139687894051856)                                                                                                        |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Mountable device (HDD and USB stick)                                                                                                                                                                                                       | `inst.repo=hd:`{.literal}*`<device>`{.literal}*`:/`{.literal}*`<path>`{.literal}*                                                                           | Image file of the installation DVD.                                                                                                                                            |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NFS Server                                                                                                                                                                                                                                 | `inst.repo=nfs:[`{.literal}*`options`{.literal}*`:]`{.literal}*`<server>`{.literal}*`:/`{.literal}*`<path>`{.literal}*                                      | Image file of the installation DVD, or an installation tree, which is a complete copy of the directories and files on the installation DVD. [^\[b\]^](#ftn.idm139687894036736) |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | HTTP Server                                                                                                                                                                                                                                | `inst.repo=http://`{.literal}*`<host>`{.literal}*`/`{.literal}*`<path>`{.literal}*                                                                          | Installation tree that is a complete copy of the directories and files on the installation DVD.                                                                                |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | HTTPS Server                                                                                                                                                                                                                               | `inst.repo=https://`{.literal}*`<host>`{.literal}*`/`{.literal}*`<path>`{.literal}*                                                                         |                                                                                                                                                                                |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | FTP Server                                                                                                                                                                                                                                 | `inst.repo=ftp://`{.literal}*`<username>`{.literal}*`:`{.literal}*`<password>`{.literal}*`@`{.literal}*`<host>`{.literal}*`/`{.literal}*`<path>`{.literal}* |                                                                                                                                                                                |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | HMC                                                                                                                                                                                                                                        | `inst.repo=hmc`{.literal}                                                                                                                                   |                                                                                                                                                                                |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | [^\[a\]^](#idm139687894051856) If *device* is left out, installation program automatically searches for a drive containing the installation DVD.                                                                                           |                                                                                                                                                             |                                                                                                                                                                                |
        |                                                                                                                                                                                                                                            |                                                                                                                                                             |                                                                                                                                                                                |
        | [^\[b\]^](#idm139687894036736) The NFS Server option uses NFS protocol version 3 by default. To use a different version, add `nfsvers=`{.literal}*`X`{.literal}* to *options*, replacing *X* with the version number that you want to use. |                                                                                                                                                             |                                                                                                                                                                                |
        +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        : Table 23.1. Types and format for the inst.repo= boot option and installation source

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

        : Table 23.2. Installation sources and boot option format

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

### [23.2. Network boot options](#network-boot-options) {#network-boot-options .title}

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

        : Table 23.3. Boot option formats to configure the network interface

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

### [23.3. Console boot options](#console-boot-options) {#console-boot-options .title}

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

### [23.4. Debug boot options](#debug-boot-options) {#debug-boot-options .title}

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

    : Table 23.4. updates.img file sources

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

### [23.5. Storage boot options](#storage-boot-options) {#storage-boot-options .title}

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

## [Legal Notice](#idm139687890991456) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
