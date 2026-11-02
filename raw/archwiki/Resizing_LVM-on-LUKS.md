---
{"title": "Resizing LVM-on-LUKS", "url": "https://wiki.archlinux.org/title/Resizing_LVM-on-LUKS", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Resizing LVM-on-LUKS

**This article or section is a candidate for merging with [LVM#Shrinking](../en/LVM.html#Shrinking "LVM").**

**Notes:** This howto only aggregates information from other articles (thus duplicating it) for a too specific case: if some explanations are clearer here, they should be merged into [LVM#Shrinking](../en/LVM.html#Shrinking "LVM"), and then the little remaining wrapping part about dm-crypt should be merged into [Dm-crypt/Specialties](../en/Dm-crypt/Specialties.html "Dm-crypt/Specialties") with a link to [LVM#Shrinking](../en/LVM.html#Shrinking "LVM") for the LVM resizing. (Discuss in [Talk:Resizing LVM-on-LUKS](../en/Talk:Resizing_LVM-on-LUKS.html))

This article follows the process of resizing an LVM-on-LUKS-on-GPT partition. You can also use [GParted](../en/Parted.html "GParted") GUI tool to resize LUKS partition, which may be easier and quicker for beginners.

## Method {#Method}

The filesystem we work on will have the following structure:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# lsblk
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
NAME                MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sda                   8:0    0 111.8G  0 disk
├─sda1                8:1    0    99M  0 part  /boot
└─sda2                8:2    0 111.7G  0 part
  └─vgroup          254:0    0 111.7G  0 crypt
    ├─vgroup-lvroot 254:1    0    30G  0 lvm   /
    └─vgroup-lvhome 254:2    0  81.7G  0 lvm   /home
```

The goal is to clear up unused space and create a new partition, `sda3`, without any data loss. All filesystems are assumed to be `ext4`.

The entire process should run from a live USB Arch system to avoid any filesystem corruption.

## Process {#Process}

**Warning** **Do not** run any of this code by copy-pasting, you need to adapt all these commands to your specific setup.

**Note**

-   It is highly recommended to check your work after each step by checking the filesystem, LVM, and/or LUKS volume integrity.
-   It is highly recommended to write out the exact transition plan so that at each step you know exactly which partition size you are going to need.

## Shrink LVM-on-LUKS {#Shrink_LVM-on-LUKS}

### Boot and setup {#Boot_and_setup}

Boot into your live [USB flash installation media](../en/USB_flash_installation_media.html "USB flash installation media").

Decrypt the LUKS volume:

    # cryptsetup luksOpen /dev/sda2 cryptdisk

### Resize filesystem and LVM logical volume {#Resize_filesystem_and_LVM_logical_volume}

Follow [these instructions](../en/LVM.html#Resizing_the_logical_volume_and_file_system_in_one_go "LVM").

You can run a `fsck` just to make sure nothing broke:

    # e2fsck -f /dev/vgroup/lvhome

### Resize LVM physical Volume {#Resize_LVM_physical_Volume}

To calculate the new LVM physical volume size, use a simple formula: `NEW_VOLUME_BYTES = PE_SIZE * PE_COUNT + UNUSABLE_SIZE`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
pvdisplay --units B /dev/mapper/cryptdisk
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
PV Size               1020108419892 B / not usable 4194304 B
...
PE Size               4194304 B
...
Allocated PE          116303
...
```

Using the formula above: `4194304 * 116303 + 4194304 = 487814332416`.

Resize the volume. Note the \"B\" (Bytes) appended to the end of the value for size. This command is safe since it will exit early if the new size would not fit all the existing extents:

    # pvresize --setphysicalvolumesize 487814332416B /dev/mapper/cryptdisk

### Resize LUKS volume {#Resize_LUKS_volume}

To calculate the new LUKS volume size, use a simple formula: `NEW_LUKS_SECTOR_COUNT = PV_EXTENT_COUNT * PV_EXTENT_SIZE `**`IN BYTES`**` / LUKS_SECTOR_SIZE`

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# pvdisplay /dev/mapper/cryptdisk
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
PV Size               454.31 GiB / not usable 3.00 MiB
...
PE Size               4.00 MiB
Total PE              116303
...
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# cryptsetup status cryptdisk
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
sector size:  512
...
```

    (116303 extents + 1 unusable extent) * 4194304 B/extent / 512 B/sector = 952762368 sectors

Resize the LUKS volume:

    # cryptsetup -b $NEW_LUKS_SECTOR_COUNT resize cryptdisk

### Resize the partition {#Resize_the_partition}

To calculate the new partition size, use a simple formula: `NEW_PARTITION_SECTOR_END = PARTITION_SECTOR_START + (LUKS_SIZE_SECTORS + LUKS_OFFSET_SECTORS) - 1`. The `- 1` is because parted takes an inclusive sector end parameter.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# cryptsetup status cryptdisk
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
offset:  4096 sectors
size:    952762368 sectors
```

Close the LUKS volume to resize offline. You will probably need to deactivate LVM volumes on the cryptdisk or it will not close.

    # vgchange -a n vgroup
    # cryptsetup close cryptdisk

Use `parted` to resize the partition:

    # parted /dev/sda
     (parted) unit
     Unit?  [compact]? s
     (parted) p
     ...
      2      8003584s  2000408575s  1992404992s

Using the formula above returns: `8003584 + (952762368 + 4096) - 1 = 960770047`

    (parted) resizepart 2 960770047
     Warning: Shrinking a partition can cause data loss, are you sure you want to continue?
     Yes/No? y
     (parted) q

At this point you can reopen the LUKS volume and remount partitions. You will need to manually reactive the LVM partitions since if you manually deactivated them above.

    # cryptsetup luksOpen /dev/sda2 cryptdisk
    # vgchange -a y vgroup

## Enlarge LVM on LUKS {#Enlarge_LVM_on_LUKS}

Enlarging a LVM-on-LUKS logical partition, for instance after migrating to a larger hard disk, is done in the opposite way - from the outermost to the innermost partition:

    primary partition(LUKS device{volume group[(logical partition1)(logical partition2-->)]})

### Preparation {#Preparation}

Create a new partition on the new hard disk of wanted size, f.i. by using [GNU Parted](../en/GNU_Parted.html "GNU Parted"), and clone the old partition `sdX1`, containing your LUKS container, into the new partition `sdY1`:

    # dd if=/dev/sdX1 of=/dev/sdY1 bs=4M

### Extending the physical segments of the cryptdevice {#Extending_the_physical_segments_of_the_cryptdevice}

Now, open the cryptdevice `CryptDisk` on the new hard disk:

    # cryptsetup open /dev/sdY1 CryptDisk

Take a look at your current physical volume. In this example, we have a cryptdevice `CryptDisk` containing a volume group `CryptVolumeGroup` of two partitions `root` and `home`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# pvdisplay -m
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
 --- Physical volume ---
 PV Name               /dev/mapper/CryptDisk
 VG Name               CryptVolumeGroup
 PV Size               <118.75 GiB / not usable 3.00 MiB
 Allocatable           yes (but full)
 PE Size               4.00 MiB
 Total PE              30399
 Free PE               0
 Allocated PE          30399
 PV UUID               hu0iA9-i8fv-2SC1-C6ys-LQCz-sptQ-RSOUE5

 --- Physical Segments ---
 Physical extent 0 to 6399:
   Logical volume      /dev/CryptVolumeGroup/root
   Logical extents     0 to 6399
 Physical extent 6400 to 30398:
   Logical volume      /dev/CryptVolumeGroup/home
   Logical extents     0 to 23998
```

By taking the total physical extents (PE) times the PE\'s size, we get the total size of the physical volume (PV), in this case 118.75 GiB. Although pvdisplay does not show the free extents, we can enlarge the PV to use all the available remaining space of the partition:

    # pvresize /dev/mapper/CryptDisk

Now we get:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# pvdisplay -m
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
 --- Physical Segments ---
 Physical extent 0 to 6399:
   Logical volume      /dev/CryptVolumeGroup/root
   Logical extents     0 to 6399
 Physical extent 6400 to 30398:
   Logical volume      /dev/CryptVolumeGroup/home
   Logical extents     0 to 23998
 Physical extent 30399 to 60922:
   FREE
```

Note the free extents at the end of the PV. Calculate the size difference by taking the free physical extends times PE size - in that case (60922-30399)\*4 MiB = 119.2 GiB.

### Resizing the logical volume {#Resizing_the_logical_volume}

Now we are going to resize the second logical volume (LV), in this case containing the /home partition, by the size of the free physical extents minus some safety space:

    # lvresize -L +119G /dev/CryptVolumeGroup/home

Note the new size of the second logical volume. Calculate its total size by taking the total logical extends time the PE size - in that case 53438 \* 4 MiB = 208.7 GiB:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# pvdisplay -m
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
 --- Physical Segments ---
 Physical extent 0 to 6399:
   Logical volume      /dev/CryptVolumeGroup/root
   Logical extents     0 to 6399
 Physical extent 6400 to 59838:
   Logical volume      /dev/CryptVolumeGroup/home
   Logical extents     0 to 53438
 Physical extent 59839 to 60922:
   FREE
```

### Resizing the encrypted volume {#Resizing_the_encrypted_volume}

Now we are going to resize the encrypted volume itself. By taking in account the total size of the logical volume minus some safety space:

    # resize2fs -p /dev/CryptVolumeGroup/Home 208G

Execute e2fsck, if asked. That\'s it.
