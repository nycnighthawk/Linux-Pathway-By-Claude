---
{"title": "Customizing Anaconda", "guide": "customizing_anaconda", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/customizing_anaconda/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Customizing Anaconda {#customizing-anaconda .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Changing the installer appearance and creating custom add-ons on Red Hat Enterprise Linux {#changing-the-installer-appearance-and-creating-custom-add-ons-on-red-hat-enterprise-linux .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140620592861536)

**Abstract**

Anaconda is the installer used by Red Hat Enterprise Linux. You can customize Anaconda for extending capabilities when you install RHEL in your environment.

------------------------------------------------------------------------

## [Chapter 1. Introduction to Anaconda customization](#introduction-to-anaconda-customization) {#chapter-1.-introduction-to-anaconda-customization .title}

The Red Hat Enterprise Linux and Fedora installation program, **Anaconda**, brings many improvements in its most recent versions. One of these improvements is enhanced customizability. Now write add-ons to extend the base installer functionality, and change the appearance of the graphical user interface.

Customization is available for the following components:

-   Boot menu - pre-configured options, color scheme and background
-   Appearance of the graphical interface - logo, backgrounds, product name
-   Installer functionality - add-ons which can enhance the installer by adding new Kickstart commands and new screens in the graphical and textual user interfaces

Important

Procedures described in this book are written for Red Hat Enterprise Linux 10 or a similar systems. On other systems, the tools and applications used (such as `xorrisofs`{.literal} for creating custom ISO images) may be different, and procedures may need to be adjusted.

Support Statement
:   Red Hat supports only customizing the Red Hat Enterprise Linux installation media and images by using Red Hat Enterprise Linux Image Builder. Alternatively, you can use Kickstart to deploy consistent systems in your infrastructure.

## [Chapter 2. Performing the pre-customization tasks](#performing-the-pre-customization-tasks) {#chapter-2.-performing-the-pre-customization-tasks .title}

You can customize the Red Hat Enterprise Linux installation media by downloading the Red Hat Enterprise Linux 10 boot images from the Red Hat Customer Portal. Once downloaded, extract their contents and rebuild the boot image with specific modifications to support tailored deployment needs.

### [2.1. Working with ISO images](#working-with-iso-images) {#working-with-iso-images .title}

Customizing the installer requires working with the distribution ISO: extract the image to modify its contents, then build a new boot image that includes those changes. For example, add-ons, `product.img`{.literal}, or other Anaconda customizations. This workflow covers:

-   Extracting a Red Hat Enterprise Linux ISO to a working directory.
-   Creating a new boot image that contains the customizations.

### [2.2. Downloading RHEL boot images](#downloading-rh-boot-images) {#downloading-rhel-boot-images .title}

Before you begin to customize the installer, download the Red Hat-provided boot images. You can obtain Red Hat Enterprise Linux 10 boot media from the **Red Hat Customer Portal** after logging in to your account.

Note

-   Your account must have sufficient entitlements to download Red Hat Enterprise Linux 10 images.
-   You must download either the `Binary DVD`{.literal} or `Boot ISO`{.literal} image.
-   You cannot customize the installer by using the other available downloads, such as the KVM Guest Image or Supplementary DVD.

**Additional resources**

-   [Red Hat Customer Portal](https://access.redhat.com/downloads/content/486/ver=/rhel---10/10/x86_64/product-software)
-   [Product Downloads](https://access.redhat.com/downloads/content/rhel)

### [2.3. Extracting Red Hat Enterprise Linux boot images](#extracting-red-hat-enterprise-linux-boot-images) {#extracting-red-hat-enterprise-linux-boot-images .title}

You can extract the contents of a boot image to a working directory and modify the contents to create a new boot image. You can find the boot images on the Red Hat Customer Portal.

**Procedure**

1.  Ensure that the directory *`/mnt/iso`{.literal}* exists and nothing is currently mounted there.

2.  Mount the downloaded image.

    ``` {.language-plaintext tabindex="-1"}
    # mount -t iso9660 -o loop path/to/image.iso /mnt/iso
    ```

    Where *path/to/image.iso* is the path to the downloaded boot image.

3.  Create a working directory where you want to place the contents of the ISO image.

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir /tmp/ISO
    ```

4.  Copy all contents of the mounted image to your new working directory. Ensure that you use the `-p`{.literal} option to preserve file and directory permissions and ownership.

    ``` {.language-plaintext tabindex="-1"}
    # cp -pRf /mnt/iso /tmp/ISO
    ```

5.  Unmount the image.

    ``` {.language-plaintext tabindex="-1"}
    # umount /mnt/iso
    ```

**Additional resources**

-   [Product Downloads](https://access.redhat.com/downloads/content/rhel)

## [Chapter 3. Customizing the boot menu](#customizing-the-boot-menu) {#chapter-3.-customizing-the-boot-menu .title}

You can customize the boot menu options to suit your specific requirements. With the available options, you can modify the boot process, select different startup behaviors, and configure settings that affect how the system initializes.

The Boot menu customization involves the following high-level tasks:

1.  Complete the prerequisites.
2.  Customize the Boot menu.
3.  Create a custom Boot image.

### [3.1. Customizing the boot menu](#customizing-boot-menu) {#customizing-the-boot-menu .title}

The *Boot menu* is the menu that opens when you boot your system using an installation image. Normally, by using this menu, you can choose between options such as `Install Red Hat Enterprise Linux`{.literal}, `Boot from local drive`{.literal} or `Rescue an installed system`{.literal}.

To customize the Boot menu, you can:

-   Customize the default options.
-   Add more options.
-   Change the visual style (color and background).

An installation media consists of a **GRUB2** boot loader. The **GRUB2** boot loader is used on systems with UEFI firmware.

Customizing the boot menu options can especially be useful with Kickstart. Kickstart files must be provided to the installer before the installation begins. Normally, you can do this by manually editing one of the existing boot options to add the `inst.ks=`{.literal} boot option. You can add this option to one of the pre-configured entries, if you edit boot loader configuration files on the media.

### [3.2. Systems with legacy BIOS firmware](#systems-with-bios-firmware) {#systems-with-legacy-bios-firmware .title}

The `boot/grub2/grub.cfg`{.literal} configuration file on the boot media contains a list of preconfigured menu entries and other directives that control the appearance and the Boot menu functionality.

In the configuration file, the default menu entry for Red Hat Enterprise Linux (Test this media & install Red Hat Enterprise Linux 10) is defined in the following block:

``` {.language-plaintext tabindex="-1"}
menuentry 'Install Red Hat Enterprise Linux 10.0' --class fedora --class gnu-linux --class gnu --class os {
    linux /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64 quiet
    initrd /images/pxeboot/initrd.img
}
menuentry 'Test this media & install Red Hat Enterprise Linux 10.0' --class fedora --class gnu-linux --class gnu --class os {
    linux /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64 rd.live.check quiet
    initrd /images/pxeboot/initrd.img
}
```

Where:

-   `menuentry`{.literal} - Defines the title of the entry. It is specified in single or double quotes (\' or \"). You can use the `--class`{.literal} option to group menu entries into different classes, which can then be styled differently using GRUB2 themes.

    Note

    You must enclose each menu entry definition in curly braces ({}).

-   `linux`{.literal} - Defines the kernel that boots (`/images/pxeboot/vmlinuz`{.literal} in the example) and the other additional options, if any. You can customize these options to change the behavior of the boot entry. One of the notable options is `inst.ks=`{.literal}. You can use this option to specify a location of a Kickstart file. You can place a Kickstart file on the boot ISO image and use the `inst.ks=`{.literal} option to specify its location; for example, you can place a `kickstart.ks`{.literal} file into the image's root directory and use `inst.ks=hd:LABEL=RHEL-10-0-BaseOS-x86_64:/kickstart.ks`{.literal}. You can also use dracut options which are listed on the `dracut.cmdline(7)`{.literal} man page.

    Important

    When using a disk label to refer to a certain drive, for example, `inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64`{.literal}, replace all spaces with `\x20`{.literal}.

-   `initrd`{.literal} - Location of the initial RAM disk (`initrd`{.literal}) image to be loaded. Other options used in the `grub.cfg`{.literal} configuration file are:

    -   `set timeout`{.literal} - determines how long is the boot menu displayed before the default menu entry is automatically used. The default value is 60, which means the menu is displayed for 60 seconds. Setting this value to `-1`{.literal} disables the timeout completely.

        Note

        Setting the timeout to 0 is useful when performing a headless installation, because this setting immediately activates the default boot entry.

-   `submenu`{.literal} - A submenu block allows you to create a sub-menu and group some entries under it, instead of displaying them in the main menu. The Troubleshooting submenu in the default configuration contains entries for rescuing an existing system. The title of the entry is in single or double quotes (\' or \"). The submenu block contains one or more menuentry definitions and the entire block is enclosed in curly braces ({}). For example:

    ``` {.language-plaintext tabindex="-1"}
    submenu 'Submenu title' {
      menuentry 'Submenu option 1' {
        linux /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64 nomodeset quiet
        initrd /images/pxeboot/initrd.img
      }
      menuentry 'Submenu option 2' {
        linux /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64 inst.rescue quiet
        initrd /images/pxeboot/initrd.img
      }
    }
    ```

-   `set default`{.literal} - Determines the default entry. The entry numbers start from 0. If you want to make the third entry the default one, use set `default=2`{.literal} and so on.

-   `theme`{.literal} - Determines the directory which contains GRUB2 theme files. You can use the themes to customize visual aspects of the boot loader - background, fonts, and colors of specific elements.

**Additional resources**

-   [Managing, monitoring and updating the kernel](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/index)

### [3.3. Systems with UEFI firmware](#systems-with-uefi-firmware) {#systems-with-uefi-firmware .title}

The `EFI/BOOT/grub.cfg`{.literal} configuration file on the boot media contains a list of preconfigured menu entries and other directives that control the appearance and the Boot menu functionality.

In the configuration file, the default menu entry for Red Hat Enterprise Linux (`Test this media & install Red Hat Enterprise Linux 10`{.literal}) is defined in the following block:

``` {.language-plaintext tabindex="-1"}
menuentry 'Test this media & install Red Hat Enterprise Linux 10.0' --class fedora --class gnu-linux --class gnu --class os {
    linuxefi /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64 rd.live.check quiet
    initrdefi /images/pxeboot/initrd.img
}
```

Where:

-   `menuentry`{.literal} - Defines the title of the entry. It is specified in single or double quotes (`'`{.literal} or `"`{.literal}). You can use the `--class`{.literal} option to group menu entries into different *classes*, which can then be styled differently by using **GRUB2** themes.

    Note

    As shown in the preceding example, you must enclose each menu entry definition in curly braces (`{}`{.literal}).

-   `linuxefi`{.literal} - Defines the kernel that boots (`/images/pxeboot/vmlinuz`{.literal} from the example) and the other additional options, if any.

    You can customize these options to change the behavior of the boot entry.

    One of the notable options is `inst.ks=`{.literal}, which allows you to specify a location of a Kickstart file. You can place a Kickstart file on the boot ISO image and use the inst.ks= option to specify its location; for example, you can place a `kickstart.ks`{.literal} file into the image's root directory and use `inst.ks=hd:LABEL=RHEL-10-0-BaseOS-x86_64:/kickstart.ks`{.literal}.

    You can also use `dracut`{.literal} options which are listed on the `dracut.cmdline(7)`{.literal} man page on your system.

    Important

    When using a disk label to refer to a certain drive, for example, `inst.stage2=hd:LABEL=RHEL-10-BaseOS-x86_64`{.literal}, replace all spaces with `\x20`{.literal}.

-   `initrdefi`{.literal} - Location of the initial RAM disk (initrd) image to be loaded.

Other options used in the `grub.cfg`{.literal} configuration file are:

-   `set timeout`{.literal} - Determines how long is the boot menu displayed before the default menu entry is automatically used. The default value is `60`{.literal}, which means the menu is displayed for 60 seconds. Setting this value to `-1`{.literal} disables the timeout completely.

    Note

    Setting the timeout to `0`{.literal} is useful when performing a headless installation, because this setting immediately activates the default boot entry.

-   `submenu`{.literal} - A *submenu* block allows you to create a sub-menu and group some entries under it, instead of displaying them in the main menu. The `Troubleshooting`{.literal} submenu in the default configuration contains entries for rescuing an existing system.

    The title of the entry is in single or double quotes (`'`{.literal} or `"`{.literal}).

    The `submenu`{.literal} block contains one or more `menuentry`{.literal} definitions as described earlier, and the entire block is enclosed in curly braces (`{}`{.literal}) For example:

    ``` {.language-plaintext tabindex="-1"}
    submenu 'Submenu title' {
      menuentry 'Submenu option 1' {
        linuxefi /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64 nomodeset quiet
        initrdefi /images/pxeboot/initrd.img
      }
      menuentry 'Submenu option 2' {
        linuxefi /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64 inst.rescue quiet
        initrdefi /images/pxeboot/initrd.img
      }
    }
    ```

-   `set default`{.literal} - Determines the default entry. The entry numbers start from `0`{.literal}. If you want to make the *third* entry the default one, use `set default=2`{.literal} and so on.

-   `theme`{.literal} - Determines the directory which contains **GRUB2** theme files. You can use the themes to customize visual aspects of the boot loader - background, fonts, and colors of specific elements.

**Additional resources**

-   [*Managing, monitoring and updating the kernel*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/index)

## [Chapter 4. Branding and chroming the graphical user interface](#branding-and-chroming-the-graphical-user-interface) {#chapter-4.-branding-and-chroming-the-graphical-user-interface .title}

The customization of Anaconda user interface might include the customization of graphical elements and the customization of product name.

The user interface customization involves the following high-level tasks:

1.  Complete the prerequisites.

2.  Create custom branding material (if you plan to customize the graphical elements).

3.  Customize the graphical elements (if you plan to customize them).

4.  Customize the product name (if you plan to customize it).

5.  Create a product.img file.

6.  Create a custom Boot image.

    Note

    To create the custom branding material, first refer to the default graphical element files type and dimensions. You can accordingly create the custom material. Details about default graphical elements are available in the sample files that are provided in the `/usr/share/anaconda/pixmaps/`{.literal} directory in the installer runtime file system.

### [4.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   You have downloaded and extracted the ISO image.
-   You have created your own branding material.

### [4.2. Customizing graphical elements](#customizing-graphical-elements) {#customizing-graphical-elements .title}

To customize the graphical elements, modify or replace the customisable elements by using the custom branded material and update the container files. This helps in customizing the graphical elements of the installer.

The customisable graphical elements of the installer are stored in the `/usr/share/anaconda/pixmaps/`{.literal} directory in the installer runtime file system. This directory contains the following customisable files:

``` {.language-plaintext tabindex="-1"}
pixmaps
├─ anaconda-password-show-off.svg
├─ anaconda-password-show-on.svg
├─ right-arrow-icon.png
├─ sidebar-bg.png
├─ sidebar-logo.png
└─ topbar-bg.png
```

Additionally, `/usr/share/anaconda/`{.literal} contains a base CSS stylesheet named `anaconda-gtk.css`{.literal}, which determines the file names and parameters of the main UI elements. They include the logo and the backgrounds for the sidebar and top bar. Product-specific stylesheet customizations are located in a separate file (`/usr/share/anaconda/pixmaps/redhat.css`{.literal}) and override the defaults from the `anaconda-gtk.css`{.literal} file. Use a product-specific file for CSS customizations as it only overrides the particular elements of the stylesheet as needed.

The product-specific `redhat.css`{.literal} file has the following content that can be customized as per your requirement (for the full stylesheet specifications, see content of the `anaconda-gtk.css`{.literal} file):

``` {.language-plaintext tabindex="-1"}
/* theme colors/images */

@define-color product_bg_color @redhat;

/* logo and sidebar classes */

.logo-sidebar {
   background-image: url('/usr/share/anaconda/pixmaps/sidebar-bg.png');
   background-color: @product_bg_color;
   background-repeat: no-repeat;
}

/* Add a logo to the sidebar */

.logo {
   background-image: url('/usr/share/anaconda/pixmaps/sidebar-logo.png');
   background-position: 50% 20px;
   background-repeat: no-repeat;
   background-color: transparent;
}

/* This is a placeholder to be filled by a product-specific logo. */

.product-logo {
   background-image: none;
   background-color: transparent;
}

AnacondaSpokeWindow #nav-box {
   background-color: @product_bg_color;
   background-image: url('/usr/share/anaconda/pixmaps/topbar-bg.png');
   background-repeat: no-repeat;
   color: white;
}
```

The most important part of the CSS file is the way in which it handles scaling based on resolution. The PNG image backgrounds do not scale, they are always displayed in their true dimensions. Instead, the backgrounds have a transparent background, and the stylesheet defines a matching background color on the `@define-color`{.literal} line. Therefore, the background *images* \"fade\" into the background *color*, which means that the backgrounds work on all resolutions without a need for image scaling.

You could also change the `background-repeat`{.literal} parameters to tile the background, or, if you are confident that every system you will be installing on has the same display resolution, you can use background images which fill the entire bar.

You can customize any of the files listed earlier. Once you do so, follow the instructions in [Creating a product.img File](#creating-a-product-img-file "6.1. Creating a product.img file") to create your own `product.img`{.literal} with custom graphics, and then [Creating Custom Boot Images](#creating-custom-boot-images "6.2. Creating custom boot images") to create a new bootable ISO image with your changes included.

### [4.3. Customizing the product name](#customizing-the-product-name) {#customizing-the-product-name .title}

You can customize the product name by creating a custom `.buildstamp`{.literal} file. This helps to add a custom name to the installer.

**Procedure**

1.  Create a new `.buildstamp`{.literal} file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [Main]
    Product=My Distribution
    Version=10
    BugURL=https://bugzilla.redhat.com/
    IsFinal=True
    ```

    Change *My Distribution* to the name that you want to display in the installer.

2.  After you create the custom `.buildstamp`{.literal} file, follow [Creating a product.img file](#creating-a-product-img-file "6.1. Creating a product.img file") section to create a new `product.img`{.literal} file containing your customizations, and the [Creating custom boot images](#creating-custom-boot-images "6.2. Creating custom boot images") section to create a new bootable ISO file with your changes included.

### [4.4. Configuring the default configuration files](#configuring-the-default-configuration-files) {#configuring-the-default-configuration-files .title}

You can write the Anaconda configuration files in the `.ini`{.literal} file format. The Anaconda configuration file consists of sections, options and comments. Each section is defined by a `section`{.literal} header, the comments starting with a `#`{.literal} character and the `key = value`{.literal} pairs to define the `options`{.literal}.

The resulting configuration file is processed with the `configparser`{.literal} Python configuration file parser.

The default configuration file, located at `/etc/anaconda/anaconda.conf`{.literal}, contains sections and options that are supported. The file provides a full default configuration of the installer. You can create custom configuration files in `/etc/anaconda/conf.d/`{.literal} directory.

The following configuration file describes the default configuration:

``` {.language-plaintext tabindex="-1"}
# Anaconda configuration file.

[Anaconda]
# Run Anaconda in the debugging mode.
debug = False

# List of Anaconda DBus modules that can be activated.
# Supported patterns: MODULE.PREFIX., MODULE.NAME activatable_modules = org.fedoraproject.Anaconda.Modules.
    org.fedoraproject.Anaconda.Addons.*

# List of Anaconda DBus modules that are not allowed to run.
# Supported patterns: MODULE.PREFIX., MODULE.NAME forbidden_modules = # List of Anaconda DBus modules that can fail to run. # The installation won't be aborted because of them. # Supported patterns: MODULE.PREFIX., MODULE.NAME
optional_modules =
    org.fedoraproject.Anaconda.Modules.Subscription
    org.fedoraproject.Anaconda.Addons.*

[Installation System]
# Type of the installation system.
# FIXME: This is a temporary solution.
type = UNKNOWN

# Should the installer show a warning about enabled SMT?
can_detect_enabled_smt = False

[Installation Target]
# Type of the installation target.
type = HARDWARE

# A path to the physical root of the target.
physical_root = /mnt/sysimage

# A path to the system root of the target.
system_root = /mnt/sysroot

# Should we install the network configuration?
can_configure_network = True

# Should we copy input kickstart to target system?
can_copy_input_kickstart = True

# Should we save kickstart equivalent to installation settings to the new system?
can_save_output_kickstart = True

# Should we save logs from the installation to the new system?
can_save_installation_logs = True

[Network]
# Network device to be activated on boot if none was configured so.
# Valid values:
#
#   NONE                   No device
#   DEFAULT_ROUTE_DEVICE   A default route device
#   FIRST_WIRED_WITH_LINK  The first wired device with link
#
default_on_boot = NONE

[Payload]
# Default package environment.
default_environment =

# List of ignored packages.
ignored_packages =

# Names of repositories that provide latest updates.
updates_repositories =

# Names of repositories disabled by default.
# Supported patterns: REPO-NAME, PREFIX*, SUFFIX, *INFIX
disabled_repositories =
    source
    debuginfo
    updates-testing
    updates-testing-modular

# List of .treeinfo variant types to enable.
# Valid items:
#
#   addon
#   optional
#   variant
#
enabled_repositories_from_treeinfo = addon optional variant

# Enable installation from the closest mirror.
enable_closest_mirror = True

# Default installation source.
# Valid values:
#
#    CLOSEST_MIRROR  Use closest public repository mirror.
#    CDN             Use Content Delivery Network (CDN).
#
default_source = CLOSEST_MIRROR

# Enable ssl verification for all HTTP connection
verify_ssl = True

# GPG keys to import to RPM database by default.
# Specify paths on the installed system, each on a line.
# Substitutions for $releasever and $basearch happen automatically.
default_rpm_gpg_keys =

[Security]
# Enable SELinux usage in the installed system.
# Valid values:
#
#  -1  The value is not set.
#   0  SELinux is disabled.
#   1  SELinux is enabled.
#
selinux = -1

[Bootloader]
# Type of the bootloader.
# Supported values:
#
#   DEFAULT   Choose the type by platform.
#   EXTLINUX  Use extlinux as the bootloader.
#   SDBOOT    Use systemd-boot as the bootloader.
#
type = DEFAULT

# Name of the EFI directory.
efi_dir = default

# Hide the GRUB menu.
menu_auto_hide = False

# Are non-iBFT iSCSI disks allowed?
nonibft_iscsi_boot = False

# Arguments preserved from the installation system.
preserved_arguments =
    cio_ignore zfcp.allow_lun_scan
    speakup_synth apic noapic apm ide noht acpi video
    pci nodmraid nompath nomodeset noiswmd fips selinux
    biosdevname ipv6.disable net.ifnames net.ifnames.prefix
    nosmt vga

[Storage]
# Enable iBFT usage during the installation.
ibft = True

# Tell multipathd to use user friendly names when naming devices during the installation.
multipath_friendly_names = True

# Create GPT discoverable partition type IDs, if possible
gpt_discoverable_partitions = True

# Do you want to allow imperfect devices (for example, degraded mdraid array devices)?
allow_imperfect_devices = False

# Btrfs compression algorithm and level. For example, zstd:1.
btrfs_compression =

# Default disk label type.
# Valid values:
#
#    gpt  Prefer creation of GPT disk labels.
#    mbr  Prefer creation of MBR disk labels.
#
#    If not specified, use whatever Blivet uses by default.
#
disk_label_type =

# Default file system type. Use whatever Blivet uses by default.
file_system_type =

# Default partitioning.
# Specify a mount point and its attributes on each line.
#
# Valid attributes:
#
#   size <SIZE>    The size of the mount point.
#   min <MIN_SIZE> The size will grow from MIN_SIZE to MAX_SIZE.
#   max <MAX_SIZE> The max size is unlimited by default.
#   free <SIZE>    The required available space.
#   btrfs          The mount point will be created only for the Btrfs scheme
#
default_partitioning =
    /     (min 1 GiB, max 70 GiB)
    /home (min 500 MiB, free 50 GiB)

# Default partitioning scheme.
# Valid values:
#
#   PLAIN      Create standard partitions.
#   BTRFS      Use the Btrfs scheme.
#   LVM        Use the LVM scheme.
#   LVM_THINP  Use LVM Thin Provisioning.
#
default_scheme = LVM

# Default version of LUKS.
# Valid values:
#
#   luks1  Use version 1 by default.
#   luks2  Use version 2 by default.
#
luks_version = luks2

[Storage Constraints]

# Minimal size of the total memory.
min_ram = 320 MiB

# Minimal size of the available memory for LUKS2.
luks2_min_ram = 128 MiB

# Should we recommend to specify a swap partition?
swap_is_recommended = False

# Recommended minimal sizes of partitions.
# Specify a mount point and a size on each line.
min_partition_sizes =
    /      250 MiB
    /usr   250 MiB
    /tmp   50  MiB
    /var   384 MiB
    /home  100 MiB
    /boot  512 MiB

# Required minimal sizes of partitions.
# Specify a mount point and a size on each line.
req_partition_sizes =

# Allowed device types of the / partition if any.
# Valid values:
#
#   LVM        Allow LVM.
#   MD         Allow RAID.
#   PARTITION  Allow standard partitions.
#   BTRFS      Allow Btrfs.
#   DISK       Allow disks.
#   LVM_THINP  Allow LVM Thin Provisioning.
#
root_device_types =

# Mount points that must be on a linux file system.
# Specify a list of mount points.
must_be_on_linuxfs = / /var /tmp /usr /home /usr/share /usr/lib

# Paths that must be directories on the / file system.
# Specify a list of paths.
must_be_on_root = /bin /dev /sbin /etc /lib /root /mnt lost+found /proc

# Paths that must NOT be directories on the / file system.
# Specify a list of paths.
must_not_be_on_root =

# Mount points that are recommended to be reformatted.
#
# It will be recommended to create a new file system on a mount point
# that has an allowed prefix, but doesn't have a blocked one.
# Specify lists of mount points.
reformat_allowlist = /boot /var /tmp /usr
reformat_blocklist = /home /usr/local /opt /var/www

[User Interface]
# The path to a custom stylesheet.
custom_stylesheet =

# A list of spokes to hide in UI.
# FIXME: Use other identification then names of the spokes.
hidden_spokes =

# Should the UI allow to change the configured root account?
can_change_root = False

# Should the UI allow to change the configured user accounts?
can_change_users = False

# Define the default password policies.
# Specify a policy name and its attributes on each line.
#
# Valid attributes:
#
#   quality <NUMBER>  The minimum quality score (see libpwquality).
#   length <NUMBER>   The minimum length of the password.
#   empty             Allow an empty password.
#   strict            Require the minimum quality.
#
password_policies =
    root (quality 1, length 6)
    user (quality 1, length 6, empty)
    luks (quality 1, length 6)

# Should kernel options be shown in the software selection spoke?
show_kernel_options = True

[License]
# A path to EULA (if any)
#
# If the given distribution has an EULA & feels the need to
# tell the user about it fill in this variable by a path
# pointing to a file with the EULA on the installed system.
#
# This is currently used just to show the path to the file to
# the user at the end of the installation.
eula =

[Timezone]
# URL for geolocation data provider.
# This is used for automatic language and timezone detection.
#
# Known valid providers:
#
#   https://geoip.fedoraproject.org/city
#   https://api.hostip.info/get_json.php
#
# If left empty, geolocation does not run.
#
geolocation_provider = https://geoip.fedoraproject.org/city

[Localization]
# Should geolocation be used when setting the language ?
#
use_geolocation = True
```

Content of files in the `conf.d`{.literal} directory overrides defaults from `anaconda.conf`{.literal}. The files are named in a \<priority\>-\<config-description\>.conf form, for example `100-my-distribution.conf`{.literal}. The file with the highest priority is applied last, overriding all configuration files applied earlier.

Here is an example of a customization configuration file content:

``` {.language-plaintext tabindex="-1"}
# Anaconda configuration file for My Distribution

[Profile]
 Define the profile.
profile_id = my_distribution

[Profile Detection]
 Match os-release values.
os_id = my_distribution

[Network]
default_on_boot = NONE

[Storage]
file_system_type = xfs
default_partitioning =
    /     (min 2 GiB, max 50 GiB)
    /home (min 20 GiB, free 10 GiB)
    /test (size 256 MiB)
    swap

[Storage Constraints]
swap_is_recommended = True

[User Interface]
custom_stylesheet = /usr/share/anaconda/pixmaps/my_distribution.css
```

## [Chapter 5. Developing installer add-ons](#developing-installer-add-ons) {#chapter-5.-developing-installer-add-ons .title}

Details about Anaconda and its architecture explain its back end and the various plug points necessary for add-ons to function. This information supports the development of custom add-ons tailored to specific requirements.

### [5.1. Introduction to Anaconda and add-ons](#introduction-to-anaconda-and-add-ons) {#introduction-to-anaconda-and-add-ons .title}

**Anaconda** is the operating system installer used in Fedora, Red Hat Enterprise Linux, and their derivatives. It is a set of Python modules and scripts together with some additional files like `Gtk`{.literal} widgets (written in C), `systemd`{.literal} units, and `dracut`{.literal} libraries.

Together, they form a tool to configure parameters of the resulting (target) system and then configure this system on a machine. The installation process has four major steps:

1.  Prepare installation destination (usually disk partitioning)
2.  Install package and data
3.  Install and configure boot loader
4.  Configure newly installed system

By using Anaconda, you can install Fedora, Red Hat Enterprise Linux, and their derivatives in the following three ways:

**Using graphical user interface (GUI):**

This is the most common installation method. By using this interface, you can install the system interactively with little or no configuration required before starting the installation. This method covers all common use cases, including configuring complicated partitioning layouts.

The graphical interface supports remote access over Remote Desktop Protocol (`RDP`{.literal}), so you can use the GUI even on systems with no graphics cards or attached monitor.

**Using text user interface (TUI):**

The TUI works similar to a monochrome line printer, which allows it to work on serial consoles that do not support cursor movement, colors and other advanced features. The text mode is limited and allows you to customize only the most common options, such as network settings, language options or installation (package) source; advanced features such as manual partitioning are not available in this interface.

**Using Kickstart file:**

A Kickstart file is a plain text file with shell-like syntax that can contain data to drive the installation process. A Kickstart file allows you to partially or completely automate the installation. A set of commands that configures all required areas is necessary to completely automate the installation. If one or more commands are missed, the installation requires interaction.

Apart from automation of the installer itself, Kickstart files can contain custom scripts that are run at specific moments during the installation process.

### [5.2. Anaconda architecture overview](#anaconda-architecture-) {#anaconda-architecture-overview .title}

**Anaconda** is a set of Python modules and scripts. It also uses several external packages and libraries.

The major components of this toolset include the following packages:

-   `pykickstart`{.literal} - parses and validates the Kickstart files. Also, provides data structure that stores values that drive the installation.
-   `dnf`{.literal} - the package manager that installs packages and resolves dependencies
-   `blivet`{.literal} - handles all activities related to storage management
-   `pyanaconda`{.literal} - contains the user interface and modules for **Anaconda**, such as keyboard and timezone selection, network configuration, and user creation. Also provides various utilities to perform system-oriented functions
-   `python-meh`{.literal} - contains an exception handler that gathers and stores additional system information in case of a crash and passes this information to the `libreport`{.literal} library, which itself is a part of the **ABRT Project**.
-   `dasbus`{.literal} - communicates between the `D-Bus`{.literal} library with modules of anaconda and with external components
-   `python-simpleline`{.literal} - text UI framework library to manage user interaction in the **Anaconda** text mode
-   `gtk`{.literal} - the Gnome toolkit library for creating and managing GUI

Apart from the division into packages previously mentioned, **Anaconda** is internally divided into the user interface and a set of modules that run as separate processes and communicate by using the `D-Bus`{.literal} library. These modules are:

-   `Boss`{.literal} - manages the internal module discovery, lifecycle, and coordination
-   `Localization`{.literal} - manages locales
-   `Network`{.literal} - handles network
-   `Payloads`{.literal} - handles data for installation in different formats, such as `rpm`{.literal}, `ostree`{.literal}, `tar`{.literal} and other installation formats. Payloads manage the sources of data for installation; sources can vary in format such as CD-ROM, HDD, NFS, URLs, and other sources
-   `Security`{.literal} - manages security related aspects
-   `Services`{.literal} - handles services
-   `Storage`{.literal} - manages storage by using `blivet`{.literal}
-   `Subscription`{.literal} - handles the `subscription-manager`{.literal} tool and Red Hat Lightspeed.
-   `Timezone`{.literal} - deals with time, date, zones, and time synchronization.
-   `Users`{.literal} - creates users and groups.

Each module declares which parts of Kickstart it handles, and has methods to apply the configuration from Kickstart to the installation environment and to the installed system.

The Python code portion of Anaconda (`pyanaconda`{.literal}) starts as a \"main\" process that owns the user interface. Any Kickstart data you provide are parsed by using the `pykickstart`{.literal} module and the `Boss`{.literal} module is started, it discovers all other modules, and starts them. The main process then sends Kickstart data to the modules according to their declared capabilities. Modules process the data, apply the configuration to the installation environment, and the UI validates if all required choices have been made. If not, you must supply the data in an interactive installation mode. Once all required choices have been made, the installation can start; the modules write data to the installed system.

**Additional resources**

-   [ABRT Project](https://fedorahosted.org/abrt/)

### [5.3. Anaconda user interface](#anaconda-user-interface) {#anaconda-user-interface .title}

The Anaconda user interface (UI) has a non-linear structure, also known as hub and spoke model.

The advantages of **Anaconda** hub and spoke model are:

-   Flexibility to follow the installer screens.
-   Flexibility to retain the default settings.
-   Provides an overview of the configured values.
-   Supports extensibility. You can add hubs without the need to reorder anything and can resolve some complex ordering dependencies.
-   Supports installation in graphical and text mode.

The following diagram shows the installer layout and the possible interactions between *hubs* and *spokes* (screens):

**Figure 5.1. Hub and spoke model**

In the diagram, screens 2-13 are called *normal spokes*, and screens 1 and 14 are *standalone spokes*. Standalone spokes are the screens that can be used before or after the standalone spoke or hub. For example, the `Welcome`{.literal} screen at the beginning of the installation that prompts you to choose your language for the rest of the installation.

Note

-   The `Installation Summary`{.literal} is the only hub in Anaconda. It shows a summary of configured options before the installation begins

Each spoke has the following predefined *properties* that reflect the hub.

-   `ready`{.literal} - states whether or not you can visit a spoke. For example, when the installer is configuring a package source, the spoke is colored in gray, and you cannot access it until the configuration is complete.
-   `completed`{.literal} - marks whether or not the spoke is complete (all required values are set).
-   `mandatory`{.literal} - determines whether you *must* visit the spoke before continuing the installation; for example, you must visit the `Installation Destination`{.literal} spoke, even if you want to use automatic disk partitioning
-   `status`{.literal} - provides a short summary of values configured within the spoke (displayed under the spoke name in the hub)

To make the user interface clearer, spokes are grouped together into *categories*. For example, the `Localization`{.literal} category groups together spokes for keyboard layout selection, language support and time zone settings.

Each spoke contains UI controls that display and allow modification of values from one or more modules. This behavior also applies to spokes provided by add-ons. During a Kickstart installation, some spokes may remain hidden while still processing their data automatically without requiring them to be opened.

### [5.4. Communication across Anaconda threads](#communication-across-anaconda-threads-) {#communication-across-anaconda-threads .title}

Some actions that you need to perform during the installation process may take a long time. For example, scanning disks for existing partitions or downloading package metadata. To prevent you from waiting and remaining responsive, **Anaconda** runs these actions in separate threads.

The **Gtk** toolkit does not support element changes from multiple threads. The main event loop of **Gtk** runs in the main thread of the **Anaconda** process. Therefore, all actions pertaining to the GUI must be performed in the main thread. To do so, use `GLib.idle_add`{.literal}, which is not always easy. Several helper functions and decorators that are defined in the **pyanaconda.ui.gui.utils** module might add to the difficulty.

The `@gtk_action_wait`{.literal} and `@gtk_action_nowait`{.literal} decorators change the decorated function or method in such a way that when this function or method is called, it is automatically queued into Gtk's main loop that runs in the main thread. The return value is either returned to the caller or dropped, respectively.

In a spoke and hub communication, a spoke announces when it is ready and is not blocked. The `hubQ`{.literal} message queue handles this function, and periodically checks the main event loop. When a spoke becomes accessible, it sends a message to the queue announcing the change and that it should no longer be blocked.

The same applies in a situation where a spoke needs to refresh its status or complete a flag. The `Configuration and Progress`{.literal} hub has a different queue called `progressQ`{.literal} which serves as a medium to transfer installation progress updates.

These mechanisms are also used for the text-based interface. In the text mode, there is no main loop, but the keyboard input takes most of the time.

### [5.5. Anaconda modules and D-Bus library](#anaconda-modules-and-d-bus-library) {#anaconda-modules-and-d-bus-library .title}

Modules in Anaconda run as independent processes. To communicate with these processes by using their `D-Bus`{.literal} API, use the `dasbus`{.literal} library.

Calls to methods through the `D-Bus`{.literal} API are asynchronous, but with the `dasbus`{.literal} library you can convert them to synchronous method calls in Python. You can also write either of the following programs:

-   program with asynchronous calls and return handlers
-   A program with synchronous calls that makes the caller wait until the call is complete.

Additionally, Anaconda uses task objects running in modules. Tasks have a `D-Bus`{.literal} API and methods that are automatically processed in additional threads. To successfully run the tasks, use the `sync_run_task`{.literal} and `async_run_task`{.literal} helper functions.

**Additional resources**

-   [Communication across Anaconda threads](#communication-across-anaconda-threads- "5.4. Communication across Anaconda threads")

### [5.6. The Hello World addon example](#the-hello-world-addon-example) {#the-hello-world-addon-example .title}

Anaconda developers publish an example add-on called \"Hello World\", available on [GitHub](https://github.com/rhinstaller/hello-world-anaconda-addon/). The descriptions in further sections are reproduced in this document.

### [5.7. Anaconda add-on structure](#anaconda-add-on-structure) {#anaconda-add-on-structure .title}

An **Anaconda** add-on is a Python package that contains a directory with an `init.py`{.literal} and other source directories (subpackages). Because by using Python, you can import each package name only once, specify a unique name for the package top-level directory.

You can use an arbitrary name, because add-ons are loaded regardless of their name. The only requirement is that they must be placed in a specific directory.

The suggested naming convention for add-ons is similar to Java packages or D-Bus service names.

To make the directory name a unique identifier for a Python package, prefix the add-on name with the reversed domain name of your organization, by using underscores (`_`{.literal}) instead of dots. For example, `com_example_hello_world`{.literal}.

Important

Ensure that you create an `init.py`{.literal} file in each directory. Directories missing this file are considered as invalid Python packages.

When writing an add-on, ensure the following:

-   Support for each interface (graphical interface and text interface) is available in a separate subpackage and these subpackages are named `gui`{.literal} for the graphical interface and `tui`{.literal} for the text-based interface.
-   The `gui`{.literal} and `tui`{.literal} packages contain a `spokes`{.literal} subpackage. [^\[1\]^](#ftn.idm140620589879904)
-   Modules contained in the packages have an arbitrary name.
-   The `gui/`{.literal} and `tui/`{.literal} directories contain Python modules with any name.
-   There is a service that performs the actual work of the addon. This service can be written in Python or any other language.
-   The service implements support for D-Bus and Kickstart.
-   The addon contains files that enable automatic startup of the service.

Following is a sample directory structure for an add-on which supports every interface (Kickstart, GUI and TUI):

``` {.language-plaintext tabindex="-1"}
com_example_hello_world
├─ gui
│  ├─ init.py
│  └─ spokes
│     └─ init.py
└─ tui
   ├─ init.py
   └─ spokes
   └─ init.py
```

Each package must contain at least one module with an arbitrary name defining the classes that are inherited from one or more classes defined in the API.

Note

For all add-ons, follow Python's **PEP 8** and **PEP 257** guidelines for docstring conventions. There is no consensus on the format of the actual content of docstrings in **Anaconda**. The only requirement is that they are human-readable. If you plan to use auto-generated documentation for your add-on, docstrings follow the guidelines for the toolkit that you use to accomplish this.

You can include a category subpackage if an add-on needs to define a new category, but this is not recommended.

**Additional resources**

-   [PEP 8](http://www.python.org/dev/peps/pep-0008/)
-   [PEP 257](http://www.python.org/dev/peps/pep-0257/)

\

------------------------------------------------------------------------

[^\[1\]^](#idm140620589879904) The **gui** package may also contain a **categories** subpackage if the add-on needs to define a new category, but this is not recommended.

### [5.8. Anaconda services and configuration files](#anaconda-services-and-configuration-files) {#anaconda-services-and-configuration-files .title}

Anaconda services and configuration files are included in data/ directory. These files are required to start the add-ons service and to configure D-Bus.

Following are some examples of Anaconda Hello World add-on:

**Example 5.1. Example of *addon-name*.conf:**

``` {.language-plaintext tabindex="-1"}
<!DOCTYPE busconfig PUBLIC
"-//freedesktop//DTD D-BUS Bus Configuration 1.0//EN"
"http://www.freedesktop.org/standards/dbus/1.0/busconfig.dtd">
<busconfig>
       <policy user="root">
               <allow own="org.fedoraproject.Anaconda.Addons.HelloWorld"/>
               <allow send_destination="org.fedoraproject.Anaconda.Addons.HelloWorld"/>
       </policy>
       <policy context="default">
               <deny own="org.fedoraproject.Anaconda.Addons.HelloWorld"/>
               <allow send_destination="org.fedoraproject.Anaconda.Addons.HelloWorld"/>
       </policy>
</busconfig>
```

This file must be placed in the `/usr/share/anaconda/dbus/confs/`{.literal} directory in the installation environment. The string `org.fedoraproject.Anaconda.Addons.HelloWorld`{.literal} must correspond to the location of add-on's service on D-Bus.

**Example 5.2. Example of *addon-name*.service:**

``` {.language-plaintext tabindex="-1"}
[D-BUS Service]
# Start the org.fedoraproject.Anaconda.Addons.HelloWorld service.
# Runs org_fedora_hello_world/service/main.py
Name=org.fedoraproject.Anaconda.Addons.HelloWorld
Exec=/usr/libexec/anaconda/start-module org_fedora_hello_world.service
User=root
```

This file must be placed in the `/usr/share/anaconda/dbus/services/`{.literal} directory in the installation environment. The string `org.fedoraproject.Anaconda.Addons.HelloWorld`{.literal} must correspond to the location of addon's service on D-Bus. The value on the line starting with `Exec=`{.literal} must be a valid command that starts the service in the installation environment.

### [5.9. GUI Add-on basic features](#gui-add-on-basic-features) {#gui-add-on-basic-features .title}

Similarly to Kickstart support in add-ons, GUI support requires that every part of the add-on contains at least one module with a definition of a class inherited from a particular class defined by the API.

For the graphical add-on support, the only class to add is the `NormalSpoke`{.literal} class, defined in `pyanaconda.ui.gui.spokes`{.literal}, as a class for the normal spoke type of screen. See [Anaconda user interface](#anaconda-user-interface "5.3. Anaconda user interface").

To implement a new class inherited from `NormalSpoke`{.literal}, you must define the following class attributes that the API requires:

-   `builderObjects`{.literal} - lists all top-level objects from the spoke's `.glade`{.literal} file that should be exposed to the spoke with their children objects (recursively). In case everything should be exposed to the spoke, the list should be empty.
-   `mainWidgetName`{.literal} - contains the id of the main window widget (Add Link) as defined in the `.glade`{.literal} file.
-   `uiFile`{.literal} - contains the name of the `.glade`{.literal} file.
-   `category`{.literal} - contains the class of the category the spoke belongs to.
-   `icon`{.literal} - contains the identifier of the icon that will be used for the spoke on the hub.
-   `title`{.literal} - defines the title that will be used for the spoke on the hub.

### [5.10. Adding support for the Add-on graphical user interface (GUI)](#adding-support-for-the-add-on-graphical-user-interface-gui) {#adding-support-for-the-add-on-graphical-user-interface-gui .title}

Define a `NormalSpoke`{.literal}-derived class to add GUI support for your add-on. Implement the required attributes, *`init`{.literal}*, `initialize`{.literal}, `refresh`{.literal}, `apply`{.literal}, and `execute`{.literal} methods, along with the `status`{.literal} property and the `ready`{.literal}, `completed`{.literal}, and `mandatory`{.literal} properties.

**Prerequisites**

-   Your add-on includes support for Kickstart. See [Anaconda add-on structure](#anaconda-add-on-structure "5.7. Anaconda add-on structure").
-   Install the `anaconda-widgets`{.literal} and `anaconda-widgets-devel`{.literal} packages, which contain Gtk widgets specific for `Anaconda`{.literal}, such as `SpokeWindow`{.literal}.

**Procedure**

-   Create the following modules with all required definitions to add support for the Add-on graphical user interface (GUI), according to the following examples.

    ``` {.language-plaintext tabindex="-1"}
    # will never be translated
    _ = lambda x: x
    N_ = lambda x: x

    # the path to addons is in sys.path so we can import things from org_fedora_hello_world
    from org_fedora_hello_world.gui.categories.hello_world import HelloWorldCategory
    from pyanaconda.ui.gui.spokes import NormalSpoke

    # export only the spoke, no helper functions, classes or constants
    all = ["HelloWorldSpoke"]

    class HelloWorldSpoke(FirstbootSpokeMixIn, NormalSpoke):
        """
        Class for the Hello world spoke. This spoke will be in the Hello world
        category and thus on the Summary hub. It is a very simple example of a unit
        for the Anaconda's graphical user interface. Since it is also inherited form
        the FirstbootSpokeMixIn, it will also appear in the Initial Setup (successor
        of the Firstboot tool).

        :see: pyanaconda.ui.common.UIObject
        :see: pyanaconda.ui.common.Spoke
        :see: pyanaconda.ui.gui.GUIObject
        :see: pyanaconda.ui.common.FirstbootSpokeMixIn
        :see: pyanaconda.ui.gui.spokes.NormalSpoke

        """

        # class attributes defined by API #

        # list all top-level objects from the .glade file that should be exposed
        # to the spoke or leave empty to extract everything
        builderObjects = ["helloWorldSpokeWindow", "buttonImage"]

        # the name of the main window widget
        mainWidgetName = "helloWorldSpokeWindow"

        # name of the .glade file in the same directory as this source
        uiFile = "hello_world.glade"

        # category this spoke belongs to
        category = HelloWorldCategory

        # spoke icon (will be displayed on the hub)
        # preferred are the -symbolic icons as these are used in Anaconda's spokes
        icon = "face-cool-symbolic"

        # title of the spoke (will be displayed on the hub)
        title = N_("_HELLO WORLD")
    ```

    The `__all__`{.literal} attribute exports the `spoke`{.literal} class, followed by the first lines of its definition including definitions of attributes previously mentioned in [GUI Add-on basic features](#gui-add-on-basic-features "5.9. GUI Add-on basic features"). These attribute values are referencing widgets defined in the `com_example_hello_world/gui/spokes/hello.glade`{.literal} file. Two other notable attributes are present:

-   `category`{.literal}, which has its value imported from the `HelloWorldCategory`{.literal} class from the `com_example_hello_world.gui.categories`{.literal} module. The `HelloWorldCategory`{.literal} that the path to add-ons is in `sys.path`{.literal} so that values can be imported from the `com_example_hello_world`{.literal} package. The `category`{.literal} attribute is part of the `N_ function`{.literal} name, which marks the string for translation; but returns the non-translated version of the string, as the translation happens in a later stage.

-   `title`{.literal}, which contains one underscore in its definition. The `title`{.literal} attribute underscore marks the beginning of the title itself and makes the spoke reachable by using the `Alt+H`{.literal} keyboard shortcut.

    What usually follows the header of the class definition and the class `attributes`{.literal} definitions is the constructor that initializes an instance of the class. In case of the Anaconda graphical interface objects, there are two methods initializing a new instance: the `__init__`{.literal} method and the `initialize`{.literal} method.

    The reason behind two such functions is that the GUI objects may be created in memory at one time and fully initialized at a different time, as the `spoke`{.literal} initialization could be time consuming. Therefore, the `__init__`{.literal} method should only call the parent's `__init__`{.literal} method and, for example, initialize non-GUI attributes. On the other hand, the `initialize`{.literal} method that is called when the installer's graphical user interface initializes should finish the full initialization of the spoke.

    In the `Hello World add-on`{.literal} example, define these two methods as follows. Note the number and description of the arguments passed to the `__init__`{.literal} method. For example:

    ``` {.language-plaintext tabindex="-1"}
    def __init__(self, data, storage, payload):
        """
        :see: pyanaconda.ui.common.Spoke.init
        :param data: data object passed to every spoke to load/store data
        from/to it
        :type data: pykickstart.base.BaseHandler
        :param storage: object storing storage-related information
        (disks, partitioning, boot loader, etc.)
        :type storage: blivet.Blivet
        :param payload: object storing packaging-related information
        :type payload: pyanaconda.packaging.Payload

        """

        NormalSpoke.init(self, data, storage, payload)
        self._hello_world_module = HELLO_WORLD.get_proxy()

    def initialize(self):
        """
        The initialize method that is called after the instance is created.
        The difference between init and this method is that this may take
        a long time and thus could be called in a separate thread.
        :see: pyanaconda.ui.common.UIObject.initialize
        """
        NormalSpoke.initialize(self)
        self._entry = self.builder.get_object("textLines")
        self._reverse = self.builder.get_object("reverseCheckButton")
    ```

    The data parameter passed to the `__init__`{.literal} method is the in-memory tree-like representation of the Kickstart file where all data is stored. In one of the ancestors\' `__init__`{.literal} methods it is stored in the `self.data`{.literal} attribute, which allows all other methods in the class to read and modify the structure.

    Note

    The `storage object`{.literal} is no longer usable as of RHEL10. If your add-on needs to interact with storage configuration, use the `Storage DBus`{.literal} module.

    Because the HelloWorldData class has already been defined in [The Hello World addon example](#the-hello-world-addon-example "5.6. The Hello World addon example"), there already is a subtree in self.data for this add-on. Its root, an instance of the class, is available as `self.data.addons.com_example_hello_world`{.literal}.

    Another action that an ancestor's `__init__`{.literal} does is initializing an instance of the GtkBuilder with the `spoke’s .glade`{.literal} file and storing it as `self.builder`{.literal}. The `initialize`{.literal} method uses this to get the `GtkTextEntry`{.literal} used to show and modify the text from the Kickstart file's %addon section.

    The `__init__`{.literal} and `initialize`{.literal} methods are both important when the spoke is created. However, the main role of the spoke is to be visited by a user who wants to change or review the spoke's values it shows and sets. To enable this, three other methods are available:

-   `refresh`{.literal} - called when the spoke is about to be visited; this method refreshes the state of the spoke, mainly its UI elements, to ensure that the displayed data matches internal data structures and, with that, to ensure that current values stored in the self.data structure are displayed.

-   `apply`{.literal} - called when the spoke is left and used to store values from UI elements back into the `self.data`{.literal} structure.

-   `execute`{.literal} - called when users leave the spoke and used to perform any runtime changes based on the new state of the spoke.

    These functions are implemented in the sample Hello World add-on in the following way:

    ``` {.language-plaintext tabindex="-1"}
    def refresh(self):
        """
        The refresh method that is called every time the spoke is displayed.
        It should update the UI elements according to the contents of
        internal data structures.
        :see: pyanaconda.ui.common.UIObject.refresh
        """
        lines = self._hello_world_module.Lines
        self._entry.get_buffer().set_text("".join(lines))
        reverse = self._hello_world_module.Reverse
        self._reverse.set_active(reverse)

    def apply(self):
        """
        The apply method that is called when user leaves the spoke. It should
        update the D-Bus service with values set in the GUI elements.
        """
        buf = self._entry.get_buffer()
        text = buf.get_text(buf.get_start_iter(),
                            buf.get_end_iter(),
                            True)
        lines = text.splitlines(True)
        self._hello_world_module.SetLines(lines)

        self._hello_world_module.SetReverse(self._reverse.get_active())

    def execute(self):
      """
      The execute method that is called when the spoke is exited. It is
      supposed to do all changes to the runtime environment according to
      the values set in the GUI elements.

      """

      # nothing to do here
      pass
    ```

    You can use several additional methods to control the spoke's state:

-   `ready`{.literal} - determines whether the spoke is ready to be visited; if the value is \"False\", the `spoke`{.literal} is not accessible, for example, the `Package Selection`{.literal} spoke before a package source is configured.

-   `completed`{.literal} - determines if the spoke has been completed.

-   `mandatory`{.literal} - determines if the spoke is mandatory or not, for example, the `Installation Destination`{.literal} spoke, which must always be visited, even if you want to use automatic partitioning.

    All of these attributes need to be dynamically determined based on the current state of the installation process. Here is a sample implementation of these methods in the Hello World add-on, which requires a certain value to be set in the text attribute of the `HelloWorldData`{.literal} class:

    ``` {.language-plaintext tabindex="-1"}
    @property
    def ready(self):
        """
        The ready property reports whether the spoke is ready, that is, can be visited
        or not. The spoke is made (in)sensitive based on the returned value of the ready
        property.

        :rtype: bool

        """

        # this spoke is always ready
        return True

    @property
    def mandatory(self):
        """
        The mandatory property that tells whether the spoke is mandatory to be
        completed to continue in the installation process.

        :rtype: bool

        """

        # this is an optional spoke that is not mandatory to be completed
        return False
    ```

    After these properties are defined, the spoke can control its accessibility and completeness, but it cannot provide a summary of the values configured within - you must visit the spoke to see how it is configured. For this reason, an additional property called `status`{.literal} exists. This property contains a single line of text with a short summary of configured values, which can then be displayed in the hub under the spoke title.

    The status property is defined in the `Hello World`{.literal} example add-on as follows:

    ``` {.language-plaintext tabindex="-1"}
    @property
    def status(self):
        """
        The status property that is a brief string describing the state of the
        spoke. It should describe whether all values are set and if possible
        also the values themselves. The returned value will appear on the hub
        beneath the spoke's title.
        :rtype: str
        """
        lines = self._hello_world_module.Lines
        if not lines:
            return _("No text added")
        elif self._hello_world_module.Reverse:
            return _("Text set with {} lines to reverse").format(len(lines))
        else:
            return _("Text set with {} lines").format(len(lines))
    ```

    After defining all properties described in the examples, the add-on has full support for showing a graphical user interface (GUI) as well as Kickstart.

    Note

    The example demonstrated here is very simple and does not contain any controls; knowledge of Python Gtk programming is required to develop a functional, interactive spoke in the GUI.

    One notable restriction is that each spoke must have its own main window - an instance of the `SpokeWindow`{.literal} widget. This widget, along with other widgets specific to Anaconda, is found in the `anaconda-widgets`{.literal} package. You can find other files required for development of add-ons with GUI support, such as `Glade`{.literal} definitions, in the `anaconda-widgets-devel`{.literal} package.

    Once your graphical interface support module contains all necessary methods you can continue with the following section to add support for the text-based user interface.

### [5.11. Add-on GUI advanced features](#add-on-gui-advanced-features) {#add-on-gui-advanced-features .title}

The `pyanaconda`{.literal} package contains several helper and utility functions, as well as constructs which may be used by hubs and spokes. Most of them are located in the `pyanaconda.ui.gui.utils`{.literal} package.

The sample `Hello World`{.literal} add-on demonstrates usage of the `englightbox`{.literal} content manager which **Anaconda** also uses. This content manager can put a window into a lightbox to increase its visibility and focus it to prevent users interacting with the underlying window. To demonstrate this function, the sample add-on contains a button which opens a new dialog window; the dialog itself is a special HelloWorldDialog inheriting from the GUIObject class, which is defined in pyanaconda.ui.gui.*init*.

The dialog class defines the run method that runs and destroys an internal Gtk dialog accessible through the self.window attribute, which is populated by using a mainWidgetName class attribute with the same meaning. Therefore, the code defining the dialog is very simple, as demonstrated in the following example:

**Example 5.3. Defining an enlightbox dialog**

``` {.language-plaintext tabindex="-1"}
        # every GUIObject gets ksdata in init
        dialog = HelloWorldDialog(self.data)

        # show dialog above the lightbox
        with self.main_window.enlightbox(dialog.window):
            dialog.run()
```

The `Defining an englightbox Dialog`{.literal} example code creates an instance of the dialog and then uses the enlightbox context manager to run the dialog within a lightbox. The context manager has a reference to the window of the spoke and only needs the dialog's window to instantiate the lightbox for the dialog.

### [5.12. TUI Add-on basic features](#tui-add-on-basic-features) {#tui-add-on-basic-features .title}

Anaconda also supports a text-based interface (TUI). This interface is more limited in its capabilities, but on some systems it might be the only choice for an interactive installation.

Note

To add support for the text interface into your add-on, create a new set of subpackages under the tui directory as described in **Anaconda add-on structure**.

The text mode support in the installer is based on the `simpleline`{.literal} library, which only allows very simple user interaction. The text mode interface:

-   Does not support cursor movement - instead, it acts like a line printer.
-   Does not support any visual enhancements, such as using different colors or fonts, for example.

Internally, the `simpleline`{.literal} toolkit has three main classes: `App`{.literal}, `UIScreen`{.literal} and `Widget`{.literal}. Widgets are units containing information to be printed on the screen. They are placed on UIScreens that are switched by a single instance of the `App`{.literal} class. On top of the basic elements, `hubs`{.literal}, `spokes`{.literal} and `dialogs`{.literal} all contain various widgets in a way similar to the graphical interface.

The most important classes for an add-on are `NormalTUISpoke`{.literal} and various other classes defined in the `pyanaconda.ui.tui.spokes`{.literal} package. All those classes are based on the `TUIObject`{.literal} class, which itself is an equivalent of the `GUIObject`{.literal} class. Each TUI spoke is a Python class inheriting from the `NormalTUISpoke`{.literal} class, overriding special arguments and methods defined by the API. Because the text interface is simpler than the GUI, there are only two such arguments:

-   `title`{.literal} - determines the title of the spoke, similar to the title argument in the GUI.
-   `category`{.literal} - determines the category of the spoke as a string; the category name is not displayed anywhere, it is only used for grouping.

Note

The TUI handles categories differently than the GUI. Assign a pre-existing category to your new spoke. Creating a new category would require patching Anaconda, and brings little benefit.

Each spoke is also expected to override several methods, namely *`init`{.literal}*, `initialize`{.literal}, `refresh`{.literal}, `apply`{.literal}, `execute`{.literal}, `input`{.literal}, `prompt`{.literal}, and properties (`ready`{.literal}, `completed`{.literal}, `mandatory`{.literal}, and `status`{.literal}).

**Additional resources**

-   [Adding support for the Add-on GUI](#adding-support-for-the-add-on-graphical-user-interface-gui "5.10. Adding support for the Add-on graphical user interface (GUI)")
-   [Anaconda add-on structure](#anaconda-add-on-structure "5.7. Anaconda add-on structure")
-   [Introduction to Anaconda and add-ons](#introduction-to-anaconda-and-add-ons "5.1. Introduction to Anaconda and add-ons")

### [5.13. Defining a simple TUI Spoke](#defining-a-simple-tui-spoke) {#defining-a-simple-tui-spoke .title}

You can implement a simple Text User Interface (TUI) spoke by defining a class inherited from the `NormalTUISpoke`{.literal} class.

**Prerequisites**

-   You have created a new set of subpackages under the tui directory as described in [Anaconda add-on structure](#anaconda-add-on-structure "5.7. Anaconda add-on structure").

**Procedure**

-   Create modules with all required definitions to add support for the add-on text user interface (TUI), according to the following examples:

    ``` {.language-plaintext tabindex="-1"}
    class HelloWorldSpoke(NormalTUISpoke):
        # category this spoke belongs to
        category = HelloWorldCategory

    def init(self, *args, kwargs): """ Create the representation of the spoke. :see: simpleline.render.screen.UIScreen """ super().init(*args, kwargs)
        self.title = N_("Hello World")
        self._hello_world_module = HELLO_WORLD.get_proxy()
        self._container = None
        self._reverse = False
        self._lines = ""

    def initialize(self):
        """
        The initialize method that is called after the instance is created.
        The difference between init and this method is that this may take
        a long time and thus could be called in a separate thread.

        :see: pyanaconda.ui.common.UIObject.initialize
        """
        # nothing to do here
        super().initialize()

    def setup(self, args=None):
        """
        The setup method that is called right before the spoke is entered.
        It should update its state according to the contents of DBus modules.

        :see: simpleline.render.screen.UIScreen.setup
        """
        super().setup(args)

        self._reverse = self._hello_world_module.Reverse
        self._lines = self._hello_world_module.Lines

        return True

    def refresh(self, args=None):
        """
        The refresh method that is called every time the spoke is displayed.
        It should generate the UI elements according to its state.

        :see: pyanaconda.ui.common.UIObject.refresh
        :see: simpleline.render.screen.UIScreen.refresh
        """
        super().refresh(args)

        self._container = ListColumnContainer(
            columns=1
        )
        self._container.add(
            CheckboxWidget(
                title="Reverse",
                completed=self._reverse
            ),
            callback=self._change_reverse
        )
        self._container.add(
            EntryWidget(
                title="Hello world text",
                value="".join(self._lines)
            ),
            callback=self._change_lines
        )

        self.window.add_with_separator(self._container)

    def _change_reverse(self, data):
        """
        Callback when user wants to switch checkbox.
        Flip state of the "reverse" parameter which is boolean.
        """
        self._reverse = not self._reverse

    def _change_lines(self, data):
        """
        Callback when user wants to input new lines.
        Show a dialog and save the provided lines.
        """
        dialog = Dialog("Lines")
        result = dialog.run()
        self._lines = result.splitlines(True)

    def input(self, args, key):
        """
        The input method that is called by the main loop on user's input.

        * If the input should not be handled here, return it.
        * If the input is invalid, return InputState.DISCARDED.
        * If the input is handled and the current screen should be refreshed,
          return InputState.PROCESSED_AND_REDRAW.
        * If the input is handled and the current screen should be closed,
          return InputState.PROCESSED_AND_CLOSE.

        :see: simpleline.render.screen.UIScreen.input
        """
        if self._container.process_user_input(key):
            return InputState.PROCESSED_AND_REDRAW

        if key.lower() == Prompt.CONTINUE:
            self.apply()
            self.execute()
            return InputState.PROCESSED_AND_CLOSE

        return super().input(args, key)

    def apply(self):
        """
        The apply method is not called automatically for TUI. It should be called
        in input() if required. It should update the contents of internal data
        structures with values set in the spoke.
        """
        self._hello_world_module.SetReverse(self._reverse)
        self._hello_world_module.SetLines(self._lines)

    def execute(self):
        """
        The execute method is not called automatically for TUI. It should be called
        in input() if required. It is supposed to do all changes to the runtime
        environment according to the values set in the spoke.
        """
        # nothing to do here
        pass
    ```

    For more details and latest code, see the [Hello World Anaconda Addon - GitHub Repository](https://github.com/rhinstaller/hello-world-anaconda-addon/blob/rhel-10/org_fedora_hello_world/tui/spokes/hello_world.py).

    Note

    It is not necessary to override the *`init`{.literal}* method if it only calls the ancestor's *`init`{.literal}*, but the comments in the example describe the arguments passed to constructors of spoke classes in an understandable way.

    In the preceding example:

-   The `setup`{.literal} method configures a default value for the internal attribute of the spoke on every entry, which is then displayed by the `refresh`{.literal} method, updated by the `input`{.literal} method and used by the `apply`{.literal} method to update internal data structures.

-   The `execute`{.literal} method has the same purpose as the equivalent method in the GUI; in this case, the method has no effect.

-   The `input`{.literal} method is specific to the text interface; there are no equivalents in Kickstart or GUI. The `input`{.literal} methods are responsible for user interaction.

-   The `input`{.literal} method processes the entered string and takes action depending on its type and value. The preceding example asks for any value and then stores it as an internal attribute (key). In more complex add-ons, you typically need to perform some non-trivial actions, such as parse letters as actions, convert numbers into integers, show additional screens or toggle boolean values.

-   The `return`{.literal} value of the input class must be either the `InputState`{.literal} enum or the `input`{.literal} string itself, in case this input should be processed by a different screen. In contrast to the graphical mode, the `apply`{.literal} and `execute`{.literal} methods are not called automatically when leaving the spoke; they must be called explicitly from the input method. The same applies to closing (hiding) the spoke's screen: it must be called explicitly from the `close`{.literal} method.

    To show another screen, for example if you need additional information that was entered in a different spoke, you can instantiate another `TUIObject`{.literal} and use `ScreenHandler.push_screen_modal()`{.literal} to show it.

    Due to restrictions of the text-based interface, TUI spokes tend to have a very similar structure, that consists of a list of checkboxes or entries that should be checked or unchecked and populated by the user.

### [5.14. Using NormalTUISpoke to define a text interface spoke](#using-normaltuispoke-to-define-a-text-interface-spoke) {#using-normaltuispoke-to-define-a-text-interface-spoke .title}

The [Defining a Simple TUI Spoke](#defining-a-simple-tui-spoke "5.13. Defining a simple TUI Spoke") example showed a way to implement a TUI spoke where its methods handle printing and processing the available and provided data.

There is a different way to accomplish this by using the `NormalTUISpoke`{.literal} class from the `pyanaconda.ui.tui.spokes`{.literal} package. By inheriting this class, you can implement a typical TUI spoke by only specifying fields and attributes that should be set in it. The following example demonstrates this:

**Prerequisites**

-   You have added a new set of subpackages under the `TUI`{.literal} directory, as described in [Anaconda add-on structure](#anaconda-add-on-structure "5.7. Anaconda add-on structure").

**Procedure**

-   Create modules with all required definitions to add support for the Add-on text user interface (TUI), according to the following examples.

    ``` {.language-plaintext tabindex="-1"}
    class HelloWorldEditSpoke(NormalTUISpoke):
        """Example class demonstrating usage of editing in TUI"""
        category = HelloWorldCategory

        def init(self, data, storage, payload):
            """
            :see: simpleline.render.screen.UIScreen
            :param data: data object passed to every spoke to load/store data
                         from/to it
            :type data: pykickstart.base.BaseHandler
            :param storage: object storing storage-related information
                            (disks, partitioning, boot loader, etc.)
            :type storage: blivet.Blivet
            :param payload: object storing packaging-related information
            :type payload: pyanaconda.packaging.Payload
            """
            super().init(self, *args, **kwargs)

            self.title = N_("Hello World Edit")
            self._container = None

            # values for user to set
            self._checked = False
            self._unconditional_input = ""
            self._conditional_input = ""

        def refresh(self, args=None):
            """
            The refresh method that is called every time the spoke is displayed.
            It should update the UI elements according to the contents of self.data.
            :see: pyanaconda.ui.common.UIObject.refresh
            :see: simpleline.render.screen.UIScreen.refresh
            :param args: optional argument that may be used when the screen is
                         scheduled
            :type args: anything
            """
            super().refresh(args)
            self._container = ListColumnContainer(columns=1)

            # add ListColumnContainer to window (main window container)
            # this will automatically add numbering and will call callbacks when required
            self.window.add(self._container)

            self._container.add(CheckboxWidget(title="Simple checkbox", completed=self._checked),
                                callback=self._checkbox_called)
            self._container.add(EntryWidget(title="Unconditional text input",
                                            value=self._unconditional_input),
                                callback=self._get_unconditional_input)

            # show conditional input only if the checkbox is checked
            if self._checked:
                self._container.add(EntryWidget(title="Conditional password input",
                                                value="Password set" if self._conditional_input
                                                else ""),
                                    callback=self._get_conditional_input)

            self.window.add_with_separator(self._container)

        def _checkbox_called(self, data):  # pylint: disable=unused-argument
            """Callback when user wants to switch checkbox.

            :param data: can be passed when adding callback in container (not used here)
            :type data: anything
            """
            self._checked = not self._checked

        def _get_unconditional_input(self, data):  # pylint: disable=unused-argument
            """Callback when the user wants to set unconditional input.

            :param data: can be passed when adding callback in container (not used here)
            :type data: anything
            """
            dialog = Dialog(
                "Unconditional input",
                conditions=[self._check_user_input]
            )
            self._unconditional_input = dialog.run()

        def _get_conditional_input(self, data):  # pylint: disable=unused-argument
            """Callback when the user wants to set conditional input.

            :param data: can be passed when adding callback in container (not used here)
            :type data: anything
            """
            dialog = PasswordDialog(
                "Unconditional password input",
                policy_name=PASSWORD_POLICY_ROOT
            )
            self._conditional_input = dialog.run()

        def _check_user_input(self, user_input, report_func):
            """Check if the user has written a valid value.

            :param user_input: user input for validation
            :type user_input: str

            :param report_func: function for reporting errors on user input
            :type report_func: func with one param
            """
            if re.match(r'^\w+$', user_input):
                return True
            else:
                report_func("You must set at least one word")
                return False

        def input(self, args, key):
            """
            The input method that is called by the main loop on user's input.

            :param args: optional argument that may be used when the screen is
                         scheduled
            :type args: anything
            :param key: user's input
            :type key: unicode
            :return: if the input should not be handled here, return it, otherwise
                     return InputState.PROCESSED or InputState.DISCARDED if the input was
                     processed successfully or not respectively
            :rtype: enum InputState
            """
            if self._container.process_user_input(key):
                return InputState.PROCESSED_AND_REDRAW
            else:
                return super().input(args, key)

        @property
        def completed(self):
            # completed if user entered something non-empty to the Conditioned input
            return bool(self._conditional_input)

        @property
        def status(self):
            return "Hidden input %s" % ("entered" if self._conditional_input
                                        else "not entered")

        def apply(self):
            # nothing needed here, values are set in the self.args tree
            pass
    ```

    For more details and latest code, see the [Hello World NormalTUISpoke - GitHub Repository](https://github.com/rhinstaller/hello-world-anaconda-addon/blob/rhel-10/org_fedora_hello_world/tui/spokes/hello_world.py#L245).

### [5.15. Deploying and testing an Anaconda add-on](#deploying-and-testing-an-anaconda-add-on) {#deploying-and-testing-an-anaconda-add-on .title}

You can deploy and test your own Anaconda add-on into the installation environment. To do so, follow the steps:

**Prerequisites**

-   You created an Add-on.
-   You have access to your `D-Bus`{.literal} files.
-   You have installed the `lorax`{.literal} package.

**Procedure**

1.  Create a directory *`DIR`{.literal}* at the place of your preference.

2.  Add the `Add-on`{.literal} python files into *`DIR`{.literal}*`/usr/share/anaconda/addons/`{.literal}.

3.  Copy your `D-Bus`{.literal} service file into *`DIR`{.literal}*`/usr/share/anaconda/dbus/services/`{.literal}.

4.  Copy your `D-Bus`{.literal} service configuration file to `/usr/share/anaconda/dbus/confs/`{.literal}.

5.  Create the *updates* image.

    Access the *`DIR`{.literal}* directory:

    ``` {.language-plaintext tabindex="-1"}
    cd DIR
    ```

    Locate the *updates* image.

    ``` {.language-plaintext tabindex="-1"}
    find . | cpio -c -o | pigz -9cv > DIR/updates.img
    ```

6.  Use the mkksiso utility to include the **`updates`{.literal}** image into the ISO boot image:

    ``` {.language-plaintext tabindex="-1"}
    sudo mkksiso -u updates.img boot.iso new_boot.iso
    ```

7.  Boot the resulting *new_boot.iso*.

    It automatically applies the embedded *updates* image with the addon, resulting in your addon being used during installation.

    For specific instructions on unpacking an existing boot image, creating a `product.img`{.literal} file and repackaging the image, see [Extracting Red Hat Enterprise Linux boot images](#extracting-red-hat-enterprise-linux-boot-images "2.3. Extracting Red Hat Enterprise Linux boot images").

## [Chapter 6. Completing post customization tasks](#completing-post-customization-tasks) {#chapter-6.-completing-post-customization-tasks .title}

To complete the customizations made, perform the following tasks:

-   Create a product.img image file (applies only for graphical customizations).
-   Create a custom boot image.

This section provides information about how to create a product.img image file and to create a custom boot image.

### [6.1. Creating a product.img file](#creating-a-product-img-file) {#creating-a-product.img-file .title}

A `product.img`{.literal} image file is an archive containing new installer files that replace the existing ones at runtime.

During a system boot, **Anaconda** loads the `product.img`{.literal} file from the `images/`{.literal} directory on the boot media. It then uses the files that are present in this directory to replace identically named files in the installer's file system. The replaced files customize the installer, for example by replacing default images with custom ones.

Note

The `product.img`{.literal} image must contain a directory structure identical to the installer. For more information about the installer directory structure, see the following table:

+----------------------------------------------+--------------------------------------------------+
| Type of custom content                       | File system location                             |
+:=============================================+:=================================================+
| Pixmaps (logo, sidebar, top bar, and so on.) | `/usr/share/anaconda/pixmaps/`{.literal}         |
+----------------------------------------------+--------------------------------------------------+
| GUI stylesheet                               | `/usr/share/anaconda/anaconda-gtk.css`{.literal} |
+----------------------------------------------+--------------------------------------------------+
| Anaconda add-ons                             | `/usr/share/anaconda/addons/`{.literal}          |
+----------------------------------------------+--------------------------------------------------+
| Profile configuration files                  | `/etc/anaconda/profile.d/`{.literal}             |
+----------------------------------------------+--------------------------------------------------+
| Custom configuration files                   | `/etc/anaconda/conf.d/`{.literal}                |
+----------------------------------------------+--------------------------------------------------+
| Anaconda DBus service conf files             | `/usr/share/anaconda/dbus/confs/`{.literal}      |
+----------------------------------------------+--------------------------------------------------+
| Anaconda DBus service files                  | `/usr/share/anaconda/dbus/services/`{.literal}   |
+----------------------------------------------+--------------------------------------------------+

: Table 6.1. Installer directory structure and custom contents

Show more

**Procedure**

1.  Navigate to a working directory such as `/tmp`{.literal}, and create a subdirectory named `product/`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ cd /tmp
    ```

2.  Create a subdirectory product/

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir product/
    ```

3.  Create a directory structure identical to the location of the file you want to replace. For example, if you want to test an add-on that is present in the `/usr/share/anaconda/addons`{.literal} directory on the installation system, create the same structure in your working directory:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p product/usr/share/anaconda/addons
    ```

    Note

    To view the installer's runtime filesystem, boot the installation and switch to virtual console 1 (Ctrl+Alt+F1) and then switch to the second **tmux** window (Ctrl+b+2). A shell prompt that can be used to browse a file system opens.

4.  Place your customized files (in this example, custom add-on for **Anaconda**) into the newly created directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp -r ~/path/to/custom/addon/ product/usr/share/anaconda/addons/
    ```

5.  Repeat steps 3 and 4 (create a directory structure and place the custom files into it) for every file you want to add to the installer.

6.  Create a `.buildstamp`{.literal} file in the root of the directory. The `.buildstamp`{.literal} file describes the system version, the product and several other parameters. The following is an example of a `.buildstamp`{.literal} file from Red Hat Enterprise Linux 8.4:

    ``` {.language-plaintext tabindex="-1"}
    [Main]
    Product=Red Hat Enterprise Linux
    Version=8.4
    BugURL=https://bugzilla.redhat.com/
    IsFinal=True
    UUID=202007011344.x86_64
    [Compose]
    Lorax=28.14.49-1
    ```

    The `IsFinal`{.literal} parameter specifies whether the image is for a release (GA) version of the product (`True`{.literal}), or a pre-release such as Alpha, Beta, or an internal milestone (`False`{.literal}).

7.  Navigate to the `product/`{.literal} directory, and create the `product.img`{.literal} archive:

    ``` {.language-plaintext tabindex="-1"}
    $ cd product
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ find . | cpio -c -o | gzip -9cv > ../product.img
    ```

    This creates a `product.img`{.literal} file one level above the `product/`{.literal} directory.

8.  Move the `product.img`{.literal} file to the `images/`{.literal} directory of the extracted ISO image.

    The `product.img`{.literal} file is now created and the customizations that you want to make are placed in the respective directories.

    Note

    Instead of adding the `product.img`{.literal} file on the boot media, you can place this file into a different location and use the `inst.updates=`{.literal} boot option at the boot menu to load it. In that case, the image file can have any name, and it can be placed in any location (USB flash drive, hard disk, HTTP, FTP or NFS server), as long as this location is reachable from the installation system.

### [6.2. Creating custom boot images](#creating-custom-boot-images) {#creating-custom-boot-images .title}

After you customize the boot images and the GUI layout, create a new image that includes the changes you made. This helps you to test the changes you made in the installation environment.

**Procedure**

1.  Ensure that all of your changes are included in the working directory. For example, if you are testing an add-on, ensure that you place the `product.img`{.literal} in the `images/`{.literal} directory.

2.  Ensure that your current working directory is the top-level directory of the extracted ISO image, for example, `/tmp/ISO/iso/`{.literal}.

3.  Install the following packages: `isomd5sum`{.literal}, `xorriso`{.literal}, `lorax`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install isomd5sum xorriso lorax
    ```

4.  Create an EFI boot image by using `mkefiboot`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mkefiboot --label=ANACONDA /tmp/ISO/iso/EFI/BOOT/ /tmp/ISO/iso/images/efiboot.img
    ```

5.  Create a new ISO image by using the `xorrisofs`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # xorrisofs -o ../NEWISO.iso -R -J -V RHEL-10-0-BaseOS-x86_64 --grub2-mbr /usr/lib/grub/i386-pc/boot_hybrid.img -partition_offset 16 -appended_part_as_gpt -append_partition 2 C12A7328-F81F-11D2-BA4B-00A0C93EC93B /tmp/ISO/iso/images/efiboot.img -iso_mbr_part_type EBD0A0A2-B9E5-4433-87C0-68B6B72699C7 -c boot.cat --boot-catalog-hide -b images/eltorito.img -no-emul-boot -boot-load-size 4 -boot-info-table --grub2-boot-info -eltorito-alt-boot -e --interval:appended_partition_2:all:: -no-emul-boot -graft-points .discinfo=/tmp/ISO/iso/.discinfo images/install.img=/tmp/ISO/iso/images/install.img images/pxeboot=/tmp/ISO/iso/images/pxeboot boot/grub2=/tmp/ISO/iso/boot/grub2 boot/grub2/i386-pc=/usr/lib/grub/i386-pc images/eltorito.img=/tmp/ISO/iso/images/eltorito.img EFI/BOOT=/tmp/ISO/iso/EFI/BOOT
    ```

    In the preceding example:

    -   Ensure the value for the `-V`{.literal} option matches the image's boot loader configuration, if you are using the `LABEL=`{.literal} directive for options that require a location to load a file on the same disk. If your boot loader configuration (`boot/grub2/grub.cfg`{.literal} for BIOS and `EFI/BOOT/grub.cfg`{.literal} for UEFI) uses the `inst.stage2=LABEL=`{.literal}*`disk_label`{.literal}* stanza to load the second stage of the installer from the same disk, then the disk labels must match.

        Important

        In boot loader configuration files, replace all spaces in disk labels with `\x20`{.literal}. For example, if you create an ISO image with a `RHEL 10.0`{.literal} label, boot loader configuration should use `RHEL\x2010.0`{.literal}.

    -   Replace the value of the `-o`{.literal} option (`-o ../NEWISO.iso`{.literal}) with the file name of your new image. The value in the example creates the `NEWISO.iso`{.literal} file in the directory *above* the current one. For more information about this command, see the `xorrisofs(1)`{.literal} man page on your system.

6.  Implant an MD5 checksum into the image. Note that without an MD5 checksum, the image verification check might fail (the `rd.live.check`{.literal} option in the boot loader configuration) and the installation can hang.

    ``` {.language-plaintext tabindex="-1"}
    # implantisomd5 ../NEWISO.iso
    ```

    In the preceding example, replace *../NEWISO.iso* with the file name and the location of the ISO image that you have created in the previous step.

    You can now write the new ISO image to physical media or a network server to boot it on physical hardware, or you can use it to start installing a virtual machine.

**Additional resources**

-   [Advanced installation boot options](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/index#installation-source-boot-options)
-   [Configuring and managing Linux virtual machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/index)

## [Legal Notice](#idm140620592861536) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
