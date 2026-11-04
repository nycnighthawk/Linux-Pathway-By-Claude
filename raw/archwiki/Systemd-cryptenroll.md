---
{"title": "Systemd-cryptenroll", "url": "https://wiki.archlinux.org/title/Systemd-cryptenroll", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Systemd-cryptenroll

Related articles

-   [dm-crypt](../en/Dm-crypt.html "Dm-crypt")
-   [Smartcards](../en/Smartcards.html "Smartcards")
-   [Universal 2nd Factor](../en/Universal_2nd_Factor.html "Universal 2nd Factor")
-   [Trusted Platform Module](../en/Trusted_Platform_Module.html "Trusted Platform Module")
-   [Unified Extensible Firmware Interface/Secure Boot](../en/Unified_Extensible_Firmware_Interface/Secure_Boot.html "Unified Extensible Firmware Interface/Secure Boot")

From [systemd-cryptenroll(1)](https://man.archlinux.org/man/systemd-cryptenroll.1):

systemd-cryptenroll is a tool for enrolling hardware security tokens and devices into a LUKS2 encrypted volume, which may then be used to unlock the volume during boot.

*systemd-cryptenroll* allows enrolling [smartcards](../en/Smartcards.html "Smartcards"), [FIDO2](../en/Universal_2nd_Factor.html "Universal 2nd Factor") tokens and [Trusted Platform Module](../en/Trusted_Platform_Module.html "Trusted Platform Module") security chips into [LUKS](../en/Dm-crypt.html "LUKS") devices, as well as regular passphrases. These devices are later unlocked by [systemd-cryptsetup@.service(8)](https://man.archlinux.org/man/systemd-cryptsetup%40.service.8), using the enrolled tokens.

## Installation {#Installation}

*systemd-cryptenroll* is part of and packaged with [systemd](https://archlinux.org/packages/?name=systemd). However, extra packages are required to use hardware devices as keys:

-   To use PKCS#11 tokens, [install](../en/Help:Reading.html#Installation_of_packages "Install") [libp11-kit](https://archlinux.org/packages/?name=libp11-kit), you may also need [opensc](https://archlinux.org/packages/?name=opensc).
-   To use FIDO2 tokens, install [libfido2](https://archlinux.org/packages/?name=libfido2).
-   To use TPM2 devices, install [tpm2-tss](https://archlinux.org/packages/?name=tpm2-tss).

## List keyslots {#List_keyslots}

*systemd-cryptenroll* can list the keyslots in a LUKS device, similar to `cryptsetup` [luksDump](../en/Dm-crypt/Device_encryption.html#Key_management "Dm-crypt/Device encryption"), but in a more user-friendly format.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# systemd-cryptenroll /dev/disk
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
SLOT TYPE    
   0 password
   1 recovery
   2 tpm2
```

## Erasing keyslots {#Erasing_keyslots}

    # systemd-cryptenroll /dev/disk --wipe-slot=SLOT

Where *SLOT* can be:

-   A single keyslot index, as represented in [#List keyslots](#List_keyslots)
-   A type of keyslot, which will erase all keyslots of that type. Valid types are `empty`, `password`, `recovery`, `pkcs11`, `fido2`, `tpm2`
-   A combination of all of the above, separated by commas
-   The string `all`, which erases all keyslots on the device. This option can only be used when enrolling another device or passphrase at the same time.

The `--wipe-slot` operation can be used in combination with all enrollment options, which is useful to update existing device enrollments:

    # systemd-cryptenroll /dev/disk --wipe-slot=fido2 --fido2-device=auto

## Enrolling passphrases {#Enrolling_passphrases}

### Regular password {#Regular_password}

This is equivalent to `cryptsetup luksAddKey`.

    # systemd-cryptenroll /dev/disk --password

### Recovery key {#Recovery_key}

From [systemd-cryptenroll(1)](https://man.archlinux.org/man/systemd-cryptenroll.1):

Recovery keys are mostly identical to passphrases, but are computer-generated instead of being chosen by a human, and thus have a guaranteed high entropy. The key uses a character set that is easy to type in, and may be scanned off screen via a QR code.

A recovery key is designed to be used as a fallback if the hardware tokens are unavailable, and can be used in place of regular passphrases whenever they are required.

    # systemd-cryptenroll /dev/disk --recovery-key

## Enrolling hardware devices {#Enrolling_hardware_devices}

The `--`*`type`*`-device` options must point to a valid device path of their respective type. A list of available devices can be obtained by passing the `list` argument to this option. Alternatively, if you only have a single device of the desired type connected, the `auto` option can be used to automatically select it.

**Note** After enrolling the hardware tokens into the LUKS2 volumes, you must configure your system to use them when appropriate. See [dm-crypt/System configuration#Trusted Platform Module and FIDO2 keys](../en/Dm-crypt/System_configuration.html#Trusted_Platform_Module_and_FIDO2_keys "Dm-crypt/System configuration") for volumes that should be unlocked in early userspace like the root filesystem, and [dm-crypt/System configuration#Unlocking in late userspace](../en/Dm-crypt/System_configuration.html#Unlocking_in_late_userspace "Dm-crypt/System configuration") for other partitions.

### PKCS#11 tokens or smartcards {#PKCS#11_tokens_or_smartcards}

The token or smartcard must contain a RSA key pair, which will be used to encrypt the generated key that will be used to unlock the volume.

    # systemd-cryptenroll /dev/disk --pkcs11-token-uri=device

### FIDO2 tokens {#FIDO2_tokens}

Any FIDO2 token that supports the \"hmac-secret\" extension can be used with *systemd-cryptenroll*. The following example would enroll a FIDO2 token to an encrypted LUKS2 block device, requiring only user presence as authentication:

    # systemd-cryptenroll /dev/disk --fido2-device=device --fido2-with-client-pin=no

In addition, *systemd-cryptenroll* supports using the token\'s built-in user verification methods:

-   `--fido2-with-user-presence` defines whether to verify the user presence (i.e. by tapping the token) before unlocking, defaults to yes
-   `--fido2-with-user-verification` defines whether to require user verification before unlocking, defaults to no

**Note**

-   These options will have no effect if the token does not support these features.
-   See [User Presence vs User Verification](https://developers.yubico.com/WebAuthn/WebAuthn_Developer_Guide/User_Presence_vs_User_Verification.html) for more information on the difference between the two.

By default, the cryptographic algorithm used when generating a FIDO2 credential is *es256* which denotes Elliptic Curve Digital Signature Algorithm (ECDSA) over NIST P-256 with SHA-256. If desired and provided by the FIDO2 token, a different cryptographic algorithm can be specified during enrollment.

**Note** This may also be desirable for those concerned with ECDSA. See [SSH keys#ECDSA](../en/SSH_keys.html#ECDSA "SSH keys") for details.

**The factual accuracy of this article or section is disputed.**

**Reason:** [systemd-cryptenroll(1) § LIMITATIONS](https://man.archlinux.org/man/systemd-cryptenroll.1#LIMITATIONS) should be mentioned. Another issue with multiple tokens using user-presence (PIN) is that systemd cannot enumerate the correct device. If they have different PIN (which can be expected), it can happen that a cached PIN exhausts the FIDO2 tries of attached tokens.[\[1\]](https://github.com/systemd/systemd/issues/41830) Using no PIN solves it, but is usually not desired. (Discuss in [Talk:Systemd-cryptenroll](../en/Talk:Systemd-cryptenroll.html))

Suppose that a previous FIDO2 token has already been enrolled; if the user wishes to enroll another, the following generates an *eddsa* credential which denotes [EdDSA](https://datatracker.ietf.org/doc/html/rfc8032) over Curve25519 with SHA-512 and authenticates the device with a previous enrolled token instead of a password:

    # systemd-cryptenroll /dev/disk --fido2-device=device --fido2-credential-algorithm=eddsa --unlock-fido2-device=auto

**Note** Both tokens must be plugged in to the system for successful enrollment.

### Trusted Platform Module {#Trusted_Platform_Module}

**This article or section needs expansion.**

**Reason:** Document `--tpm2-seal-key-handle` `--tpm2-device-key` `--tpm2-pcrlock` (Discuss in [Talk:Systemd-cryptenroll](../en/Talk:Systemd-cryptenroll.html))

*systemd-cryptenroll* has native support for enrolling LUKS keys in TPMs. It requires the following:

-   [tpm2-tss](https://archlinux.org/packages/?name=tpm2-tss) must be [installed](../en/Help:Reading.html#Installation_of_packages "Install"),
-   A LUKS2 device (currently the default type used by [cryptsetup](../en/Dm-crypt/Device_encryption.html#Cryptsetup_usage "Cryptsetup")),
-   If you intend to use this method on your root partition, some tweaks need to be made to the [initramfs](../en/Arch_boot_process.html#initramfs "Initramfs") (see [dm-crypt/System configuration#Using systemd-cryptsetup-generator](../en/Dm-crypt/System_configuration.html#Using_systemd-cryptsetup-generator "Dm-crypt/System configuration") for advanced configuration) :
    -   [mkinitcpio](../en/Mkinitcpio.html "Mkinitcpio") users: enable the `systemd` and `sd-encrypt` [hooks](../en/Mkinitcpio.html#HOOKS "Mkinitcpio").
        **Note** The order of the entries in the hooks is important. A nonstandard ordering [can make the system unbootable](https://bbs.archlinux.org/viewtopic.php?id=273945) (you will need to [regenerate the initramfs](../en/Regenerate_the_initramfs.html "Regenerate the initramfs") from within [arch-chroot](../en/Chroot.html#Using_arch-chroot "Arch-chroot") to recover). See [dm-crypt/System configuration#Examples](../en/Dm-crypt/System_configuration.html#Examples "Dm-crypt/System configuration") for an example of the correct order.
    -   [dracut](../en/Dracut.html "Dracut") users: enable the `tpm2-tss` [module](../en/Dracut.html#dracut_modules "Dracut").

To begin, run the following command to list your installed TPMs and the driver in use:

    $ systemd-cryptenroll --tpm2-device=list

**Tip**

-   If your computer has multiple TPMs installed, specify the one you wish to use with `--tpm2-device=`*`/path/to/tpm2_device`* in the following steps.
-   Consider using [PCR policies](../en/Trusted_Platform_Module.html#PCR_policies "Trusted Platform Module") instead of binding secrets to raw PCR values.

A key may be enrolled in both the TPM and the LUKS volume using only one command. The following example generates a new random key, adds it to the volume so it can be used to unlock it in addition to the existing keys, and binds this new key to PCR 7 ([Secure Boot](../en/Secure_Boot.html "Secure Boot") state):

    # systemd-cryptenroll --tpm2-device=auto --tpm2-pcrs=7 /dev/sdX

where `/dev/`*`sdX`* is the full path to the encrypted LUKS volume. Use `--unlock-key-file=`*`/path/to/keyfile`* if the LUKS volume is unlocked by a keyfile instead of a passphrase.

Refer to [systemd-cryptenroll(1)](https://man.archlinux.org/man/systemd-cryptenroll.1) and [Trusted Platform Module#Accessing PCR registers](../en/Trusted_Platform_Module.html#Accessing_PCR_registers "Trusted Platform Module") for common PCR measurements in Linux. Adjust `--tpm2-pcrs=7` as necessary (parameters are separated by the `+` symbol).

**Warning**

-   Make sure [Secure Boot](../en/Secure_Boot.html "Secure Boot") is active and in user mode when binding to PCR 7, otherwise, unauthorized boot devices could unlock the encrypted volume.
-   The state of PCR 7 can change if firmware certificates change, which can risk locking the user out. This can be implicitly done by [fwupd](../en/Fwupd.html "Fwupd")[\[2\]](https://github.com/systemd/systemd/blob/ed272a9ff59a26beedaab508dd3c9d631de67165/TODO#L664-L673) or explicitly by rotating Secure Boot keys.
-   Only binding to PCRs measured pre-boot (PCRs 0-7) opens a vulnerability from rogue operating systems. A rogue partition with metadata copied from the real root filesystem (such as partition UUID) can mimic the original partition. Then, initramfs will attempt to mount the rogue partition as the root filesystem (decryption failure will fall back to password entry), leaving pre-boot PCRs unchanged. The rogue root filesystem with files controlled by an attacker is still able to receive the decryption key for the real root partition. See [Brave New Trusted Boot World](https://0pointer.net/blog/brave-new-trusted-boot-world.html) and [BitLocker documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/countermeasures) for additional information.
-   A solution for the root volume is to bind to an empty PCR 15 using `--tpm2-pcrs=`*`other_pcrs`*`+15:sha256=0000000000000000000000000000000000000000000000000000000000000000`. If you set any `rd.luks` kernel parameters or use `/etc/crypttab` with the `x-initrd.attach` option, additionally add the `tpm2-measure-pcr=yes` option to `rd.luks.options=` or the fourth field in `/etc/crypttab`; this is not required when relying on [GPT partition automounting](../en/Systemd.html#GPT_partition_automounting "Systemd"). After the root volume is unlocked in early userspace, PCR 15 will change and the enrolled key will no longer be retrievable.
-   Another cleaner solution is described in [dm-crypt/System configuration#Pinning a LUKS volume](../en/Dm-crypt/System_configuration.html#Pinning_a_LUKS_volume "Dm-crypt/System configuration").

The combination of PCRs to bind to depends on the individual case to balance usability and lock-down. For example, you may require UEFI firmware updates without manual intervention to the [Secure Boot](../en/Secure_Boot.html "Secure Boot") state, or different boot devices. As another example, Microsoft\'s [Bitlocker](https://learn.microsoft.com/en-us/windows-hardware/test/hlk/testref/954cf796-a640-4134-b742-eaf0ed2663ff#troubleshooting) prefers PCR `7+11`, but may also use other PCR combinations.

**Note**

-   It is possible to require a PIN to be entered in addition to the TPM state being correct. Simply add the option `--tpm2-with-pin=yes` to the command above and enter the PIN when prompted.
-   *systemd-cryptenroll* does not check the TPM measurement before asking for the PIN, therefore consider using a unique PIN since the environment may be untrustworthy.

To check that the new key was enrolled, dump the LUKS configuration and look for a `systemd-tpm2` token entry, as well as an additional entry in the *Keyslots* section:

    # cryptsetup luksDump /dev/sdX

To test that the key works, run the following command while the LUKS volume is closed:

    # systemd-cryptsetup attach mapping_name /dev/sdX none tpm2-device=auto

where *`mapping_name`* is your chosen name for the volume once opened.

See [dm-crypt/System configuration#crypttab](../en/Dm-crypt/System_configuration.html#crypttab "Dm-crypt/System configuration") and [dm-crypt/System configuration#Trusted Platform Module and FIDO2 keys](../en/Dm-crypt/System_configuration.html#Trusted_Platform_Module_and_FIDO2_keys "Dm-crypt/System configuration") in order to unlock the volume at boot time.

**Note** While you may specify the UUID of your LUKS volume in place of the pathname in `/etc/crypttab`, the *systemd-cryptenroll* command itself currently only supports path names.

See [systemd-cryptenroll(1)](https://man.archlinux.org/man/systemd-cryptenroll.1) and [crypttab(5)](https://man.archlinux.org/man/crypttab.5) for more information and examples.

## See also {#See_also}

-   [Lennart\'s blog: Unlocking LUKS2 volumes with TPM2, FIDO2, PKCS#11 Security Hardware (systemd 248)](https://0pointer.net/blog/unlocking-luks2-volumes-with-tpm2-fido2-pkcs11-security-hardware-on-systemd-248.html)
-   [Lennart\'s blog: Brave New Trusted Boot World (systemd 254)](https://0pointer.net/blog/brave-new-trusted-boot-world.html)
