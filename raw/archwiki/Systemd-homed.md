---
{"title": "Systemd-homed", "url": "https://wiki.archlinux.org/title/Systemd-homed", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Systemd-homed

Related articles

-   [Users and groups](../en/Users_and_groups.html "Users and groups")
-   [fscrypt](../en/Fscrypt.html "Fscrypt")
-   [Security](../en/Security.html "Security")
-   [PAM](../en/PAM.html "PAM")

[systemd-homed(8)](https://man.archlinux.org/man/systemd-homed.8) is a [systemd](../en/Systemd.html "Systemd") service providing portable human-user accounts that are not dependent on current system configuration.

It achieves portability by moving all user-related information into a storage medium, optionally encrypted, and creating an `~/.identity` file that contains signed information about the user, password, what groups they belong to, UID/GID and other information that would typically be scattered over multiple files in `/`.

This approach allows not only for a home directory portability, but also provides security by automatically managing a home directory encryption on login and locking it if the system is suspended.

## Installation {#Installation}

*systemd-homed* is part of and packaged with [systemd](https://archlinux.org/packages/?name=systemd). The [pambase](https://archlinux.org/packages/?name=pambase) package comes with the necessary [PAM configuration](../en/PAM.html#Configuration "PAM") to allow systemd-homed user sessions.

## Usage {#Usage}

[Start/enable](../en/Help:Reading.html#Control_of_systemd_units "Start/enable") the `systemd-homed.service` service.

### Utilities {#Utilities}

#### homectl

*homectl* is the main utility you will use for homed. With it, you can create, update, and inspect users; their home directories; and their `~/.identity` files controlled by the [systemd-homed(8)](https://man.archlinux.org/man/systemd-homed.8) service.

The simplest usage of [homectl(1)](https://man.archlinux.org/man/homectl.1) is:

    # homectl create username

This command will create a user with the specified username, a free UID [in range 60001--60513](https://systemd.io/UIDS-GIDS/), create a group with the same name and a GID equal to the chosen UID, set the specified user as its member, and set the user\'s default shell to `/bin/bash`.

The home directory mount point is set to `/home/`*`username`*. The storage mechanism is chosen in this order:

1.  `luks` if supported;
2.  `subvolume` if LUKS is not supported and subvolume is supported;
3.  `directory` if none of the above is supported and no other manual option is specified.

The image path for the LUKS mechanism is set to `/home/`*`username`*`.home`. The directory path for the directory mechanism is set to `/home/`*`username`*`.homedir`.

**Note** *homectl* does not manage group creation or deletion other than those matching the name and ID of users managed by systemd-homed.

**Warning** The `~/.identity` files are signed and must not be edited directly with a text editor as it will break the signature and render them invalid. Use `homectl update --identity=/path/to/.identity` to modify it.

#### userdbctl

A query tool used to inspect users, groups and group memberships provided by both classic UNIX mechanisms and systemd-homed.

### Storage mechanism {#Storage_mechanism}

#### LUKS home directory {#LUKS_home_directory}

**This article or section needs expansion.**

**Reason:** It does not have to be **removable** media. `homectl create` wipes the partition table of the block device specified by `--image-path`, i.e. when an empty device is available it can be used.[\[1\]](https://github.com/systemd/systemd/issues/15273#issuecomment-606462384) (Discuss in [Talk:Systemd-homed](../en/Talk:Systemd-homed.html))

A user home directory is stored in a Linux [file system](../en/File_system.html "File system"), inside an encrypted [LUKS](../en/Dm-crypt.html "LUKS") (*Linux Unified Key Setup*) volume inside a loopback file or any removable media. To use this mechanism provide `--storage=luks` to *homectl*.

If you are using a loopback file, in order to save space, the LUKS2 volume can be made to discard deleted data transparently. To use this mechanism provide `--luks-discard=true` and `--luks-offline-discard=true` to *homectl*. Doing so can, however, [reduce security under certain situations](https://superuser.com/questions/302710/trim-support-via-dm-crypt-device-mapper/318847#318847).

If you are using a removable media, make sure that these conditions are met:

-   The image contains a GPT partition table. For now it should only contain a single partition, and that partition must have the type UUID `773f91ef-66d4-49b5-bd83-d683bf40ad16`. Its partition label must be the user name.
-   This partition must contain a LUKS2 volume, whose label must be the user name. The LUKS2 volume must contain a LUKS2 token field of type systemd-homed. The JSON data of this token must have a record field, containing a string with base64-encoded data. This data is the JSON user record, in the same serialization as in `~/.identity`, though encrypted. The JSON data of this token must also have an iv field, which contains a base64-encoded binary initialization vector for the encryption. The encryption used is the same as the LUKS2 volume itself uses, unlocked by the same volume key, but based on its own IV.
-   Inside of this LUKS2 volume must be a Linux file system, one of [ext4](../en/Ext4.html "Ext4"), [btrfs](../en/Btrfs.html "Btrfs") and [XFS](../en/XFS.html "XFS"). The file system label must be the user name.
-   This file system should contain a single directory named after the user. This directory will become the home directory of the user when activated. It contains a second copy of the user record in the `~/.identity` file, like in the other storage mechanisms.

**Warning**

In the event of a forceful or unexpected shutdown or power outage, in the case of a loopback file, it is possible for it to be left in a dirty state which may permanently lock the user out. See [#Home directory in a dirty state](#Home_directory_in_a_dirty_state) for details.

#### fscrypt directory {#fscrypt_directory}

A user home directory is stored the same way as when using the above method, but this time a native filesystem encryption is used. To use this mechanism provide `--storage=fscrypt` to *homectl*.

**Tip** Filesystems with fscrypt support include [ext4](../en/Ext4.html "Ext4") and [F2FS](../en/F2FS.html "F2FS").

#### Directory or Btrfs subvolume {#Directory_or_Btrfs_subvolume}

A user home directory is stored in `/home/`*`username`*`.homedir` and mounted to `/home/`*`username`* using bind [mount](../en/File_systems.html#Mount_a_file_system "Mount") on unlocking. When this method is used no encryption is provided. To use this mechanism provide `--storage=directory` or `--storage=subvolume` to *homectl*.

#### CIFS server {#CIFS_server}

Here, the home directory is mounted from a CIFS (*Common Internet File System*) server at login. Note that CIFS is implemented via the [Samba](../en/Samba.html "Samba") protocol. Use `--storage=cifs` on the *homectl* command line. The local password of the user is used to log into the CIFS service.

### User record properties {#User_record_properties}

You can view an entire user record with:

    # homectl inspect username

You can modify or add to the user record with:

    # homectl update username --property=VALUE

See [homectl(1)](https://man.archlinux.org/man/homectl.1) for more options.

### Managing users {#Managing_users}

#### Creation {#Creation}

Create a user with LUKS encryption:

    # homectl create username --storage=luks

Create a user with fscrypt encryption (make sure that fscrypt is [enabled on the file system](../en/Fscrypt.html#File_system "Fscrypt")):

    # homectl create username --storage=fscrypt

Create a user with a specific UID, shell and groups:

    # homectl create username --shell=/usr/bin/zsh --uid=60100 --member-of=wheel,adm,uucp

Other options can be found in [homectl(1) § USER RECORD PROPERTIES](https://man.archlinux.org/man/homectl.1#USER_RECORD_PROPERTIES).

**Note** The caveat explained at [Users and groups#User management](../en/Users_and_groups.html#User_management "Users and groups") applies: the login shell must be one of those listed in `/etc/shells`.

#### Activation and deactivation {#Activation_and_deactivation}

By default, the home of a user is automatically activated upon login.

**Warning** This mounts the user\'s home directory, and will remain mounted until manually unmounted, or through login/logout due to automatic deactivation-on-logout.

    # homectl activate username
    # homectl deactivate username

#### Deletion {#Deletion}

It is possible to delete several users at the same time:

**Warning** The user deletion is instant, be careful!

    # homectl remove username username2

## Tips and tricks {#Tips_and_tricks}

### Default mount options for LUKS backend {#Default_mount_options_for_LUKS_backend}

By default, the home directory will be mounted with `compress=zstd:1` and `noacl`. See [\[2\]](https://github.com/systemd/systemd/blob/main/src/home/homework-mount.c#L39).

You can override this and/or add extra options with `--luks-extra-mount-options`. For example, to enable [ACLs](../en/Access_Control_Lists.html "ACL"), use the standard level 3 zstd compression level, and allow deleting subvolumes as a regular user, use

    $ homectl update user --luks-extra-mount-options acl,compress=zstd,user_subvol_rm_allowed

### Forget key on suspend {#Forget_key_on_suspend}

The `suspend` option can be used with `pam_systemd_home.so` entries in the files in `/etc/pam.d/` to enable forget key on suspend. **No session manager at the moment supports this feature.** Furthermore, TTY sessions do not support the reauthentication mechanism. So, when session managers start supporting this feature, the suspend option should only be enabled for them. Read [pam_systemd_home(8)](https://man.archlinux.org/man/pam_systemd_home.8) and the [Linux-PAM System Administrators\' Guide](https://github.com/linux-pam/linux-pam/blob/master/doc/sag/Linux-PAM_SAG.xml) for more details.

**Warning** Mistakes in [PAM](../en/PAM.html "PAM") configuration can break the system authorization up to not being able to login even as *root*. Backing up existing configuration files is recommended before making any changes.

### SSH remote unlocking {#SSH_remote_unlocking}

*systemd-homed* encrypts your home directory using your password, so SSH configured for public key authentication cannot mount it or read `authorized_keys`. A possible solution is to add authorized keys to your user record and require both public key and password for authentication. Add the following to `/etc/ssh/sshd_config`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/sshd_config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
PasswordAuthentication yes
PubkeyAuthentication yes
AuthenticationMethods publickey,password
```

Update your user record with your authorized keys while the user is unlocked using:

    # homectl update username --ssh-authorized-keys=@/path/to/mounted/home/.ssh/authorized_keys

From now on, SSH will ask you to enter your password after completing key-based authentication. *systemd-homed* will use it to unlock and mount your home directory.

### Mounting encrypted home directory for rescue {#Mounting_encrypted_home_directory_for_rescue}

If you need to mount a *systemd-homed*-encrypted directory from a rescue disk or another machine, you will need to decrypt the directory outside of the *systemd-homed* framework. You may wish to keep a text file or script of this solution from the [forums](https://bbs.archlinux.org/viewtopic.php?id=258152) on your rescue disk for emergencies:

    # losetup -fP --show username.home
    # cryptsetup open /dev/loopXpY mappername
    # mount /dev/mapper/mappername /mnt/mountpoint

where,

-   *`username`*`.home` is the file in the `/home` directory with your username and the *.home* extension as its name
-   *`loopXpY`* is the device in the `/dev` directory with the loop number of the loopback device created in the prior step and the partition number of the relevant partition, probably `/dev/loop0p1`
-   *`mappername`* is whatever alias you decide to adopt for the mapped device, e.g. `user_oldhome`
-   *`/mnt/mountpoint`* is wherever you want to mount your decrypted home directory

### Setup user with FIDO2 hmac-secret for authentication and encryption {#Setup_user_with_FIDO2_hmac-secret_for_authentication_and_encryption}

This setup requires a FIDO2 security device, and asks for a pin to login and decrypt the home directory:

    # homectl create username --storage=fscrypt --fido2-device=auto --fido2-with-client-pin=yes --fido2-with-user-presence=no --recovery-key=yes

Setting up a recovery key is recommended in case the device is lost or broken. The recovery key will be used like a password to access the user and files. Instead of using a device pin, it is also possible to ask only for user presence, which requires touching the security device. Currently, *homectl* also requires the user to set a password as alternative login which also works as a backup secret.

## Troubleshooting {#Troubleshooting}

### Home directory remains active after logging out of Plasma {#Home_directory_remains_active_after_logging_out_of_Plasma}

After logging out of [Plasma](../en/KDE.html#Plasma "Plasma"), there may still be active user processes (e.g. *dbus-daemon*) that prevent the home directory\'s deactivation.

This can be solved by [enabling Plasma\'s systemd startup](../en/KDE.html#systemd_startup "KDE").

### User umask is ignored {#User_umask_is_ignored}

There always is an [umask](../en/Umask.html "Umask") set in `/etc/login.defs`, so the user\'s own umask set via [homectl](#homectl) is currently ignored. See [systemd issue 23007](https://github.com/systemd/systemd/issues/23007).

To solve this, set the umask in your [login shell](../en/Login_shell.html "Login shell")\'s startup files e.g. `~/.bash_profile` or `~/.zprofile`.

### Home directory in a dirty state {#Home_directory_in_a_dirty_state}

In the event of a forceful or unexpected shutdown or power outage, it is possible for the home directory to be left in a dirty state. In this case, the user will be locked out and authenticating to the home directory *may* require manual intervention. The following steps assumes that the [LUKS2](../en/Dm-crypt.html "LUKS") encrypted loop back file storage mechanism is used, and [fsck](../en/Fsck.html "Fsck") can be used in the underlying filesystem to repair it.

First, confirm the state of the loop back file is *dirty* and determine the path of the user\'s loop back file:

    $ homectl inspect username

Next, using the path of the loop back file, follow the steps in [#Mounting encrypted home directory for rescue](#Mounting_encrypted_home_directory_for_rescue).

**Note** If the LUKS2 device was able to be opened at this point, to minimize potential risk after using *fsck*, it would be wise to recover any data within the mounted device.

Finally, attempt to repair the filesystem using *fsck* on the opened LUKS2 device:

    # fsck /dev/mapper/mappername

**Warning** Ensure a mount point does not exist for `/dev/mapper/`*`mappername`* before running *fsck*.

At this point, if the repair was successful, [close](../en/Dm-crypt/Device_encryption.html#Unlocking/Mapping_LUKS_partitions_with_the_device_mapper "Dm-crypt/Device encryption") the LUKS2 container, detach the loop back device, then attempt to re-authenticate normally via the systemd-homed service.

**This article or section needs expansion.**

**Reason:** Add links to bug reports for the issues mentioned in the note. (Discuss in [Talk:Systemd-homed](../en/Talk:Systemd-homed.html))

**Note** In other cases, such as when the loop back file itself is corrupted, recovery may not be possible which may **permanently** lock out the user. Moreover, *homectl* currently does not provide any native commands for recovering from dirty states. If this is a concern, then please prepare routine [backups](../en/System_maintenance.html "System maintenance") of the home directory or refrain from using systemd-homed entirely.

## See also {#See_also}

-   [https://systemd.io/CONVERTING_TO_HOMED/](https://systemd.io/CONVERTING_TO_HOMED/)
-   [https://systemd.io/HOME_DIRECTORY/](https://systemd.io/HOME_DIRECTORY/)
