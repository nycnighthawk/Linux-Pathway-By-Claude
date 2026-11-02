---
{"title": "Systemd-repart", "url": "https://wiki.archlinux.org/title/Systemd-repart", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Systemd-repart

[systemd-repart(8)](https://man.archlinux.org/man/systemd-repart.8) is a tool for manipulating [GUID Partition Tables (GPTs)](../en/Partitioning.html#GUID_Partition_Table "Partitioning").

## Installation {#Installation}

systemd-repart is part of [systemd](../en/Systemd.html "Systemd"). It is also present on the Arch Linux installation ISO.

## Usage {#Usage}

### During Arch Linux Installation {#During_Arch_Linux_Installation}

systemd-repart can be used to create and format the necessary partitions during the [Arch Linux installation process](../en/Installation_guide.html "Installation guide"). Follow the steps below to set up your partitions.

First, create the required [repart.d(5)](https://man.archlinux.org/man/repart.d.5) configuration files. The following examples illustrate how to define partitions; adjust the parameters as needed for your specific setup.

Create the directory for the repart configuration files:

    # mkdir /etc/repart.d

Then, create the configuration files for each partition:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/repart.d/00-esp.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Partition]
Type=esp
SizeMinBytes=1G
SizeMaxBytes=1G
Format=vfat
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/repart.d/10-root.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Partition]
Type=root
SizeMinBytes=23G
Encrypt=tpm2
Format=btrfs
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/repart.d/30-swap.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Partition]
Type=swap
SizeMinBytes=4G
SizeMaxBytes=4G
Encrypt=tpm2
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/repart.d/50-home.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Partition]
Type=home
Format=btrfs
```

**Note** The `Encrypt=tpm2` option requires a compatible [TPM](../en/Trusted_Platform_Module.html "TPM") (Trusted Platform Module) to be present on your system. If you do not have a TPM, you may omit this option or use a different encryption method.

After creating the configuration files, you can check the proposed changes by running:

    # systemd-repart --empty=allow /dev/disk

**Tip** Using `--empty=allow` automatically creates a [GPT](../en/Partitioning.html#GUID_Partition_Table "GPT") partition table if it does not exist. See [systemd-repart(8) § OPTIONS](https://man.archlinux.org/man/systemd-repart.8#OPTIONS).

If the output meets your expectations, you can apply the changes by executing:

    # systemd-repart --dry-run=no --empty=allow /dev/disk

This command will create the partitions as specified in your configuration files, and automatically encrypt and/or format them if required. Ensure that you have backed up any important data before proceeding, as this operation may overwrite existing data on the specified disk.

For more advanced configurations, refer to [repart.d(5)](https://man.archlinux.org/man/repart.d.5).

Then, mount the required partitions and proceed with the rest of the installation:

    # cryptsetup open /dev/disk/by-partlabel/root-x86-64 root
    # mount /dev/mapper/root /mnt
    # mount -m /dev/disk/by-partlabel/esp /mnt/boot

**Note** In the example above, none of the partitions require any entry in [fstab](../en/Fstab.html "Fstab") or [crypttab](../en/Dm-crypt/System_configuration.html#crypttab "Crypttab"), they will automatically be decrypted and mounted if using [systemd#GPT partition automounting](../en/Systemd.html#GPT_partition_automounting "Systemd"). The swap partition will also be automatically configured (i.e. no need to run `mkswap` on it).
