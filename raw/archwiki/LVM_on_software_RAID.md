---
{"title": "LVM on software RAID", "url": "https://wiki.archlinux.org/title/LVM_on_software_RAID", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# LVM on software RAID

Related articles

-   [RAID](../en/RAID.html "RAID")
-   [LVM](../en/LVM.html "LVM")
-   [Installing with Fake RAID](../en/Installing_with_Fake_RAID.html "Installing with Fake RAID")
-   [Convert a single drive system to RAID](../en/Convert_a_single_drive_system_to_RAID.html "Convert a single drive system to RAID")

This article will provide an example of how to install and configure Arch Linux with Logical Volume Manager ([LVM](../en/LVM.html "LVM")) on top of a software [RAID](../en/RAID.html "RAID").

**Tip** LVM itself supports logical volumes in RAID configurations. See [LVM#RAID](../en/LVM.html#RAID "LVM") for an alternative to this article.

## Introduction {#Introduction}

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../en/Help:Style.html "Help:Style") for reference.**

**Reason:** This section should either be merged into the intro or renamed; [Help:Style#Preface or introduction](../en/Help:Style.html#Preface_or_introduction "Help:Style"). (Discuss in [Talk:LVM on software RAID](../en/Talk:LVM_on_software_RAID.html))

**Warning** Be sure to review the [RAID](../en/RAID.html "RAID") article and be aware of all applicable warnings, particularly if you select RAID5.

Although [RAID](../en/RAID.html "RAID") and [LVM](../en/LVM.html "LVM") may seem like analogous technologies they each present unique features. This article uses an example with three similar 1TB SATA hard drives. The article assumes that the drives are accessible as `/dev/sda`, `/dev/sdb`, and `/dev/sdc`.

**Tip** It is good practice to ensure that only the drives involved in the installation are attached while performing the installation.

  ------------------------- ---------------------- -- ------------- -------- ------------- -- ------------- -- ------------- --------- ------------- --
  **LVM Logical Volumes**   `/`                                     `/var`                    `/swap`                        `/home`                 
  **LVM Volume Groups**     `/dev/VolGroupArray`                                                                                                     
  **RAID Arrays**           `/dev/md0`                                                        `/dev/md1`                                             
  **Physical Partitions**   `/dev/sda1`               `/dev/sdb1`            `/dev/sdc1`      `/dev/sda2`      `/dev/sdb2`             `/dev/sdc2`   
  **Hard Drives**           `/dev/sda`                                       `/dev/sdb`                        `/dev/sdc`                            
  ------------------------- ---------------------- -- ------------- -------- ------------- -- ------------- -- ------------- --------- ------------- --

### Swap space {#Swap_space}

**Note** If you want extra performance, just let the kernel use distinct swap partitions as it does striping by default.

Many tutorials treat the swap space differently, either by creating a separate RAID1 array or a LVM logical volume. Creating the swap space on a separate array is not intended to provide additional redundancy, but instead, to prevent a corrupt swap space from rendering the system inoperable, which is more likely to happen when the swap space is located on the same partition as the root directory.

### Boot loader {#Boot_loader}

This tutorial will use [Syslinux](../en/Syslinux.html "Syslinux") instead of [GRUB](../en/GRUB.html "GRUB"). GRUB when used in conjunction with [GPT](../en/Partitioning.html#GUID_Partition_Table "GPT") requires an additional [BIOS boot partition](../en/BIOS_boot_partition.html "BIOS boot partition").

GRUB supports the default style of metadata currently created by mdadm (i.e. 1.2) when combined with an [initramfs](../en/Arch_boot_process.html#initramfs "Initramfs"), which has replaced in Arch Linux with [mkinitcpio](../en/Mkinitcpio.html "Mkinitcpio"). Syslinux only supports version 1.0, and therefore requires the `--metadata=1.0` option.

Some boot loaders (e.g. [GRUB Legacy](../en/GRUB_Legacy.html "GRUB Legacy"), [LILO](../en/LILO.html "LILO")) will not support any 1.x metadata versions, and instead require the older version, 0.90. If you would like to use one of those boot loaders make sure to add the option `--metadata=0.90` to the `/boot` array during [RAID installation](#RAID_installation).

## Installation {#Installation}

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../en/Help:Style.html "Help:Style") for reference.**

**Reason:** The installation environment should not be called an \"installer\". (Discuss in [Talk:LVM on software RAID](../en/Talk:LVM_on_software_RAID.html))

Obtain the latest installation media and boot the Arch Linux installer as outlined in the [installation guide](../en/Installation_guide.html "Installation guide").

### Load kernel modules {#Load_kernel_modules}

[Load](../en/Kernel_module.html#Manual_module_handling "Kernel module") the appropriate RAID (e.g. `raid0`, `raid1`, `raid5`, `raid6`, `raid10`) and LVM (i.e. `dm-mod`) modules. The following example makes use of RAID1 and RAID5.

    # modprobe raid1
    # modprobe raid5
    # modprobe dm-mod

### Prepare the hard drives {#Prepare_the_hard_drives}

[Partition](../en/Partitioning.html "Partition") each hard drive with a 1 GiB `/boot` partition, a 4 GiB `/swap` partition, and a `/` partition that takes up the remainder of the disk.

The boot partition must be RAID1; i.e it cannot be striped (RAID0) or RAID5, RAID6, etc.. This is because GRUB does not have RAID drivers. Any other level will prevent your system from booting. Additionally, if there is a problem with one boot partition, the boot loader can boot normally from the other two partitions in the `/boot` array.

**Note** Make sure to create the same exact partitions on each disk. If a group of partitions of different sizes are assembled to create a RAID partition, it will work, but *the redundant partition will be in multiples of the size of the smallest partition*, leaving the unallocated space to waste.

### RAID installation {#RAID_installation}

After creating the physical partitions, you are ready to setup the **/boot**, **/swap**, and **/** arrays with `mdadm`. It is an advanced tool for RAID management that will be used to create a `/etc/mdadm.conf` within the installation environment.

Create the **/** array at `/dev/md0`:

    # mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sd[abc]3

Create the **/swap** array at `/dev/md1`:

    # mdadm --create /dev/md1 --level=1 --raid-devices=3 /dev/sd[abc]2

**Note**

-   If the only reason you are using RAID is to prevent stored data loss (i.e. you are not concerned about some running applications crashing in the event of a disk failure), then there is no reason to RAID the swap partitions \-- you can use them as multiple individual swap partitions.
-   If you plan on installing a boot loader that does not support the 1.x version of RAID metadata make sure to add the `--metadata=0.90` option to the following command.

Create the **/boot** array at `/dev/md2`:

    # mdadm --create /dev/md2 --level=1 --raid-devices=3 --metadata=1.0 /dev/sd[abc]1

#### Synchronization {#Synchronization}

**Tip** If you want to avoid the initial resync with new hard drives add the `--assume-clean` flag.

After you create a RAID volume, it will synchronize the contents of the physical partitions within the array. You can monitor the progress by refreshing the output of `/proc/mdstat` ten times per second with:

    # watch -n .1 cat /proc/mdstat

Further information about the arrays is accessible with:

    # mdadm --misc --detail /dev/md[012]

Once synchronization is complete the `State` line should read `clean`. Each device in the table at the bottom of the output should read `spare` or `active sync` in the `State` column. `active sync` means each device is actively in the array.

**Note** Since the RAID synchronization is transparent to the file-system you can proceed with the installation and reboot your computer when necessary.

#### Scrubbing {#Scrubbing}

It is good practice to regularly run data [scrubbing](https://en.wikipedia.org/wiki/Data_scrubbing "wikipedia:Data scrubbing") to check for and fix errors.

**Note** Depending on the size/configuration of the array, a scrub may take multiple hours to complete.

To initiate a data scrub:

    # echo check > /sys/block/md0/md/sync_action

As with many tasks/items relating to mdadm, the status of the scrub can be queried:

    # cat /proc/mdstat

Example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ cat /proc/mdstat
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Personalities : [raid6] [raid5] [raid4] [raid1] 
md0 : active raid1 sdb1[0] sdc1[1]
      3906778112 blocks super 1.2 [2/2] [UU]
      [>....................]  check =  4.0% (158288320/3906778112) finish=386.5min speed=161604K/sec
      bitmap: 0/30 pages [0KB], 65536KB chunk
```

To stop a currently running data scrub safely:

    # echo idle > /sys/block/md0/md/sync_action

When the scrub is complete, admins may check how many blocks (if any) have been flagged as bad:

    # cat /sys/block/md0/md/mismatch_cnt

The check operation scans the drives for bad sectors and mismatches. Bad sectors are automatically repaired. If it finds mismatches, i.e., good sectors that contain bad data (the data in a sector does not agree with what the data from another disk indicates that it should be, for example the parity block + the other data blocks would cause us to think that this data block is incorrect), then no action is taken, but the event is logged (see below). This \"do nothing\" allows admins to inspect the data in the sector and the data that would be produced by rebuilding the sectors from redundant information and pick the correct data to keep.

##### General Notes on Scrubbing {#General_Notes_on_Scrubbing}

**Note** Users may alternatively *echo* `repair` to `/sys/block/md0/md/sync_action` but this is ill-advised since if a mismatch in the data is encountered, it would be automatically updated to be consistent. The danger is that we really do not know whether it is the parity or the data block that is correct (or which data block in case of RAID1). It is luck-of-the-draw whether or not the operation gets the right data instead of the bad data.

It is a good idea to set up a cron job as root to schedule a periodic scrub. See [raid-check](https://aur.archlinux.org/packages/raid-check/)^AUR^ which can assist with this.

##### RAID1 and RAID10 Notes on Scrubbing {#RAID1_and_RAID10_Notes_on_Scrubbing}

Due to the fact that RAID1 and RAID10 writes in the kernel are unbuffered, an array can have non-0 mismatch counts even when the array is healthy. These non-0 counts will only exist in transient data areas where they do not pose a problem. However, since we cannot tell the difference between a non-0 count that is just in transient data or a non-0 count that signifies a real problem. This fact is a source of false positives for RAID1 and RAID10 arrays. It is however recommended to still scrub to catch and correct any bad sectors there might be in the devices.

### LVM installation {#LVM_installation}

This section will convert the two RAIDs into physical volumes (PVs). Then combine those PVs into a volume group (VG). The VG will then be divided into logical volumes (LVs) that will act like physical partitions (e.g. `/`, `/var`, `/home`). If you did not understand that make sure you read the [LVM Introduction](../en/LVM.html#LVM_building_blocks "LVM") section.

#### Create physical volumes {#Create_physical_volumes}

Make the RAIDs accessible to LVM by converting them into physical volumes (PVs) using the following command. Repeat this action for each of the RAID arrays created above.

    # pvcreate /dev/md0

**Note** This might fail if you are creating PVs on an existing Volume Group. If so you might want to add `-ff` option.

Confirm that LVM has added the PVs with:

    # pvdisplay

#### Create the volume group {#Create_the_volume_group}

Next step is to create a volume group (VG) on the PVs.

Create a volume group (VG) with the first PV:

    # vgcreate VolGroupArray /dev/md0

Confirm that LVM has added the VG with:

    # vgdisplay

#### Create logical volumes {#Create_logical_volumes}

In this example we will create separate `/`, `/var`, `/swap`, `/home` LVs. The LVs will be accessible as `/dev/VolGroupArray/<lvname>`.

Create a **/** LV:

    # lvcreate -L 20G VolGroupArray -n lvroot

Create a **/var** LV:

    # lvcreate -L 15G VolGroupArray -n lvvar

**Note** If you would like to add the swap space to the LVM create a `/swap` LV with the `-C y` option, which creates a contiguous partition, so that your swap space does not get partitioned over one or more disks nor over non-contiguous physical extents:

    # lvcreate -C y -L 2G VolGroupArray -n lvswap

Create a **/home** LV that takes up the remainder of space in the VG:

    # lvcreate -l 100%FREE VolGroupArray -n lvhome

Confirm that LVM has created the LVs with:

    # lvdisplay

**Tip** You can start out with relatively small logical volumes and expand them later if needed. For simplicity, leave some free space in the volume group so there is room for expansion.

### Update RAID configuration {#Update_RAID_configuration}

Since the installer builds the [initramfs](../en/Arch_boot_process.html#initramfs "Initramfs") using `/etc/mdadm.conf` in the target system, you should update that file with your RAID configuration. The original file can simply be deleted because it contains comments on how to fill it correctly, and that is something mdadm can do automatically for you. So let us delete the original and have mdadm create you a new one with the current setup:

    # mdadm --examine --scan >> /etc/mdadm.conf

**Note** Read the note in the [Update configuration file](../en/RAID.html#Update_configuration_file "RAID") section about ensuring that you write to the correct `mdadm.conf` file from within the installer.

### Prepare hard drive {#Prepare_hard_drive}

Follow the directions outlined the in [#Installation](#Installation) section until you reach the *Prepare Hard Drive* section. Skip the first two steps and navigate to the *Manually Configure block devices, filesystems and mountpoints* page. Remember to only configure the PVs (e.g. `/dev/VolGroupArray/lvhome`) and **not** the actual disks (e.g. `/dev/sda1`).

**Warning** `mkfs.xfs` will not align the chunk size and stripe size for optimum performance (see: [Optimum RAID](https://www.linuxpromagazine.com/Issues/2009/108/RAID-Performance)).

### Configure system {#Configure_system}

**Warning** Follow the steps in the [Install Arch Linux on LVM#Adding mkinitcpio hooks](../en/Install_Arch_Linux_on_LVM.html#Adding_mkinitcpio_hooks "Install Arch Linux on LVM") section before proceeding with the installation.

#### mkinitcpio.conf

[mkinitcpio](../en/Mkinitcpio.html "Mkinitcpio") can use a hook to assemble the arrays on boot. For more information see [mkinitcpio Using RAID](../en/Mkinitcpio.html#Using_RAID "Mkinitcpio"). Add the `mdadm_udev` and `lvm2` hooks to the `HOOKS` array in `/etc/mkinitcpio.conf` after `udev`.

### Conclusion {#Conclusion}

Once it is complete you can safely reboot your machine:

    # reboot

### Install the boot loader on the Alternate Boot Drives {#Install_the_boot_loader_on_the_Alternate_Boot_Drives}

Once you have successfully booted your new system for the first time, you will want to install the [boot loader](../en/Boot_loader.html "Boot loader") onto the other two disks (or on the other disk if you have only 2 HDDs) so that, in the event of disk failure, the system can be booted from any of the remaining drives (e.g. by switching the boot order in the BIOS). The method depends on the boot loader system you are using:

#### Syslinux {#Syslinux}

Log in to your new system as root and do:

    # /usr/sbin/syslinux-install_update -iam

**Note** For this to work with [GPT](../en/Partitioning.html#GUID_Partition_Table "GPT"), the [gptfdisk](https://archlinux.org/packages/?name=gptfdisk) package is needed as the backend for setting the boot flag.

Syslinux will deal with installing the boot loader to the MBR on each of the members of the RAID array:

    Detected RAID on /boot - installing Syslinux with --raid
    Syslinux install successful

    Attribute Legacy Bios Bootable Set - /dev/sda1
    Attribute Legacy Bios Bootable Set - /dev/sdb1
    Installed MBR (/usr/lib/syslinux/gptmbr.bin) to /dev/sda
    Installed MBR (/usr/lib/syslinux/gptmbr.bin) to /dev/sdb

### Archive your filesystem partition scheme {#Archive_your_filesystem_partition_scheme}

Now that you are done, it is worth taking a second to archive off the partition state of each of your drives. This guarantees that it will be trivially easy to replace/rebuild a disk in the event that one fails. See [fdisk#Backup and restore partition table](../en/Fdisk.html#Backup_and_restore_partition_table "Fdisk").

## Management {#Management}

For further information on how to maintain your software RAID or LVM review the [RAID](../en/RAID.html "RAID") and [LVM](../en/LVM.html "LVM") articles.

## See also {#See_also}

-   [What is better LVM on RAID or RAID on LVM?](https://serverfault.com/questions/217666/what-is-better-lvm-on-raid-or-raid-on-lvm) on [Server Fault](https://en.wikipedia.org/wiki/Server_Fault "wikipedia:Server Fault")
-   [Managing RAID and LVM with Linux (v0.5)](http://www.gagme.com/greg/linux/raid-lvm.php) by Gregory Gulik
-   2011-09-08 - Arch Linux - [LVM & RAID (1.2 metadata) + SYSLINUX](https://bbs.archlinux.org/viewtopic.php?id=126172)
-   2011-04-20 - Arch Linux - [Software RAID and LVM questions](https://bbs.archlinux.org/viewtopic.php?pid=965357)
-   2011-03-12 - Arch Linux - [Some newbie questions about installation, LVM, grub, RAID](https://bbs.archlinux.org/viewtopic.php?id=114965)
