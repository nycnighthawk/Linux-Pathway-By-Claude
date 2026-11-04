---
{"title": "Systemd-firstboot", "url": "https://wiki.archlinux.org/title/Systemd-firstboot", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Systemd-firstboot

Starting with version 216 of [systemd](../en/Systemd.html "Systemd"), the command *systemd-firstboot* allows for setting of basic system settings before or during the first boot of a newly created system. The tool is able of initialize the following system settings: [timezone](../en/System_time.html#Time_zone "Timezone"), [locale](../en/Locale.html "Locale"), [hostname](../en/Network_configuration.html#Set_the_hostname "Hostname"), the root password, as well as automated generation of a machine ID.

As *systemd-firstboot* interacts with the filesystem directly and does not make use of the related systemd services (such as timedatectl, hostnamectl or localectl), it should not be executed on an already running system.

Settings can be specified non-interactively when externally used on filesystem images, or interactively if executed during the early boot process.

A default Arch Linux installation will set most variables *systemd-firstboot* is able to manipulate, or facilitate the creation of skeleton files which prevent its use when installing the systemd package through pacstrap.

## Installation {#Installation}

*systemd-firstboot* is part of and packaged with [systemd](https://archlinux.org/packages/?name=systemd).

## Usage {#Usage}

**Warning** Doing this on an existing Arch Linux instance may break your system. The following steps should only be used on new installations.

### Interactively configure system settings during boot of a fresh Arch Linux installation {#Interactively_configure_system_settings_during_boot_of_a_fresh_Arch_Linux_installation}

Allowing *systemd-firstboot* to manipulate a previously un-booted Arch Linux installation is particularly useful in situations where installation is undertaken by an individual other than the eventual end user, such as in the distribution of laptops with a pre-loaded install.

The following steps should be appended to the end of the [Configure the system section](../en/Installation_guide.html#Configure_the_system "Installation guide") of the [Installation guide](../en/Installation_guide.html "Installation guide"), before the target partitions are unmounted, thus taking place within the chroot of the new installation. Make sure all locales you want available have been generated, non-generated ones will not be offered as a possible setting.

#### Delete existing settings {#Delete_existing_settings}

If the following files are present, *systemd-firstboot* will not prompt for the setting they relate to.

    # rm /etc/{machine-id,localtime,hostname,shadow,locale.conf}

[Edit](../en/Help:Reading.html#Append,_add,_create,_edit "Textedit") `/etc/passwd` and remove the root account from it, otherwise the root will be treating as configured and *systemd-firstboot* will not prompt for the root password.

#### Modify and enable systemd-firstboot.service {#Modify_and_enable_systemd-firstboot.service}

Use a [drop-in file](../en/Drop-in_file.html "Drop-in file") in which `--prompt` makes *systemd-firstboot* query for all possible settings and the `[Install]` section specifies where in the boot process the service is to be activated.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/systemd-firstboot.service.d/install.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
ExecStart=
ExecStart=/usr/bin/systemd-firstboot --prompt

[Install]
WantedBy=sysinit.target
```

[Enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") `systemd-firstboot.service`

#### Finalize installation {#Finalize_installation}

Continue installing as per the [Installation guide](../en/Installation_guide.html "Installation guide"). Unless more configuration is to be undertaken, exit the chroot, unmount the partitions and shut down. Upon the next boot, *systemd-firstboot* will execute. Presuming **no other changes to system configuration are made**, removing the files above and rebooting will trigger systemd-firstboot again, in case you wish to test whether the installation worked.

## See also {#See_also}

-   [systemd-firstboot(1)](https://man.archlinux.org/man/systemd-firstboot.1)
-   [Out-of-the-Box Experience](../en/Out-of-the-Box_Experience.html "Out-of-the-Box Experience")
