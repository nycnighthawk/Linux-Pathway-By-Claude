---
{"title": "Clevis", "url": "https://wiki.archlinux.org/title/Clevis", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Clevis

Related articles

-   [Booster](../en/Booster.html "Booster")
-   [Mkinitcpio](../en/Mkinitcpio.html "Mkinitcpio")
-   [Dracut](../en/Dracut.html "Dracut")
-   [Dm-crypt](../en/Dm-crypt.html "Dm-crypt")
-   [YubiKey](../en/YubiKey.html "YubiKey")
-   [Trusted Platform Module](../en/Trusted_Platform_Module.html "Trusted Platform Module")

[Clevis](https://github.com/latchset/clevis/) allows binding a LUKS volume to a system by creating a key and encrypting it using the TPM, and sealing the key using PCR values which represent the system state at the time of the Clevis pin creation.

Passwords manually entered by a user is a traditional and widely used way to unlock encrypted LUKS partitions. But it has a few disadvantages:

-   It requires manual intervention and thus does not work with setups that require automatic boot (e.g. a large server farm).
-   An average human brain is capable of remembering relatively simple passwords (\~20-30 bits of entropy) that are much weaker than keys used for modern block ciphers (128/256 bits).

A solution for it would be encrypting data with a strong key stored securely somewhere else, for example at your [TPM](../en/Trusted_Platform_Module.html "TPM") chip or [YubiKey](../en/YubiKey.html "YubiKey") or some network service. Clevis is a framework that implements this idea. It allows encrypting (in terms of clevis *bind*) data with a pluggable *pin*. Currently clevis implements 3 pins:

-   TPM2 data binding (works only if you have a [Trusted Platform Module](../en/Trusted_Platform_Module.html "Trusted Platform Module") chip at your computer)
-   Network service (called [Tang](https://github.com/latchset/tang)) data binding
-   [Shamir\'s Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing "wikipedia:Shamir's Secret Sharing") that allows you to combine other pins.
-   YubiKey binding using an [external plugin](https://github.com/anatol/clevis.go/blob/main/clevis-encrypt-yubikey).

**Warning** If you use this method on your root volume, this means that, as long as the previously mentioned certain conditions are met, your computer will **unlock automatically** at boot without needing to enter an encryption password.

-   This means that access to data is not protected in case the hardware gets stolen.
-   Be aware that this method makes you more vulnerable to [cold boot attacks](https://en.wikipedia.org/wiki/Cold_boot_attack "wikipedia:Cold boot attack"), because even if your computer has been powered off for a long time (ensuring the memory is completely cleared), an attacker could simply turn it on and wait for the TPM to load the key automatically. This may be a concern for high-value targets.

## Installation {#Installation}

To use clevis [install](../en/Help:Reading.html#Installation_of_packages "Install") [clevis](https://archlinux.org/packages/?name=clevis) package.

## Bind some data {#Bind_some_data}

Here is an example of data binding with TPM2:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ clevis encrypt tpm2 '{}' <<< 'hello, world'
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
eyJhbGciOiJkaXIiLCJjbGV2aXMiOnsicGluIjoidHBtMiIsInRwbTIiOnsiaGFzaCI6InNoYTI1NiIsImp3a19wcml2IjoiQU80QUlJQkxxT3FVenVDU1FmWkprNmdDN2wzMW43V3M2Y2FZd0VZS1BSR3Q0OHJEQUJBV2Z4M3pTUUNUTmtHZE9BM2FZd2RTZk9GcXZWdnVlQ3lPamFsWldCT2R4RlJKSzl5ZVRCM0pkNFktcF9HalhhNmlnLWxxNmtmMHZTWWkzOWMxVEpES1RYRVZTdnlXSlpEbGdxQ0JPMVNxeGJBd2tfSnIyRlRNY3hvNGtpSmNtMEVjbWd5dFdyME00QmcySlg4aVo3MEt1MTVjNzFORU5Ra3RjdGMtREhBVGFQcHJ2VzI2Z3d1YmUxckRfX19aV2tHaG9mX053M0M1OHlOcXF2RUpPZUwzNTZHNXJHNVVtYmUtWWV4Ujl2SEppZWlua3ZaNTJoMFVRYWVNSm9LYjJuNjlVTGZHb2J1NElTN20iLCJqd2tfcHViIjoiQUM0QUNBQUxBQUFFMGdBQUFCQUFJQ2poWDBVeTJKZVpSNU9pRU0ySktSeEtnUElYQ3dGNnRNR09NTDZ0ZnE5aiIsImtleSI6ImVjYyJ9fSwiZW5jIjoiQTI1NkdDTSJ9..1P2Emag_4k-GlhyY.MuQQYPa8QHrysZ74uA.0ddDxfZA3R-cCmaKu5yUZA
```

This long base64-encoded message is our text encrypted with an internal TPM key. It can be decrypted at the current computer only. Trying to decrypt it from another computer (or rather with another TPM chip) will return an error.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ clevis decrypt tpm2 '{}' <<< 'eyJhbGciOiJkaXIiLCJjbGV2aXMiOnsicGluIjoidHBtMiIsInRwbTIiOnsiaGFzaCI6InNoYTI1NiIsImp3a19wcml2IjoiQU80QUlJQkxxT3FVenVDU1FmWkprNmdDN2wzMW43V3M2Y2FZd0VZS1BSR3Q0OHJEQUJBV2Z4M3pTUUNUTmtHZE9BM2FZd2RTZk9GcXZWdnVlQ3lPamFsWldCT2R4RlJKSzl5ZVRCM0pkNFktcF9HalhhNmlnLWxxNmtmMHZTWWkzOWMxVEpES1RYRVZTdnlXSlpEbGdxQ0JPMVNxeGJBd2tfSnIyRlRNY3hvNGtpSmNtMEVjbWd5dFdyME00QmcySlg4aVo3MEt1MTVjNzFORU5Ra3RjdGMtREhBVGFQcHJ2VzI2Z3d1YmUxckRfX19aV2tHaG9mX053M0M1OHlOcXF2RUpPZUwzNTZHNXJHNVVtYmUtWWV4Ujl2SEppZWlua3ZaNTJoMFVRYWVNSm9LYjJuNjlVTGZHb2J1NElTN20iLCJqd2tfcHViIjoiQUM0QUNBQUxBQUFFMGdBQUFCQUFJQ2poWDBVeTJKZVpSNU9pRU0ySktSeEtnUElYQ3dGNnRNR09NTDZ0ZnE5aiIsImtleSI6ImVjYyJ9fSwiZW5jIjoiQTI1NkdDTSJ9..1P2Emag_4k-GlhyY.MuQQYPa8QHrysZ74uA.0ddDxfZA3R-cCmaKu5yUZA'
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
hello, world
```

## Bind a LUKS volume {#Bind_a_LUKS_volume}

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../en/Help:Style.html "Help:Style") for reference.**

**Reason:** please use the first argument of the template to provide a brief explanation. (Discuss in [Talk:Clevis](../en/Talk:Clevis.html))

**Warning** Set a strong backup password in case the TPM unsealing fails, using:

    # cryptsetup luksAddKey /dev/sdX

To bind a LUKS volume to the TPM, use:

    # clevis luks bind -d /dev/sdX tpm2 '{}'

where `'{}'` contains the configuration: even with no parameters the drive cannot be decrypted from another computer, unless the attacker knows the backup password.

**Note** To seal the LUKS key against the UEFI settings and the [Secure Boot](../en/Secure_Boot.html "Secure Boot") policy, use:

    '{"pcr_ids":"1,7"}'

If the UEFI or Secure Boot settings are modified, the TPM will compute different PCR values and decryption will fail. This gives protection against [evil maid attacks](https://en.wikipedia.org/wiki/Evil_maid_attack "wikipedia:Evil maid attack").

For a list of parameters, see [clevis-encrypt-tpm2(1) § CONFIG](https://man.archlinux.org/man/clevis-encrypt-tpm2.1#CONFIG).

For a simplified explanation of the meaning of PCRs, see [Trusted Platform Module#Accessing PCR registers](../en/Trusted_Platform_Module.html#Accessing_PCR_registers "Trusted Platform Module").

For a full explanation of the meanings of PCRs, see the [TCG specification](https://trustedcomputinggroup.org/wp-content/uploads/PC-ClientSpecific_Platform_Profile_for_TPM_2p0_Systems_v51.pdf) (§ 2.3.4).

If this fails with `ERROR: pcr-input-file filesize does not match pcr set-list`, you should specify a different pcr bank:

    '{"pcr_bank":"sha256","pcr_ids":"1,7"}'

As of August 2022 Clevis only supports sha1 (default) and sha256 banks, so naturally the only different option is sha256 - you can look up available and used banks using `# tpm2_pcrread`.

To generate a new Clevis pin after changes in system configuration that result in different PCR values, for example updating the UEFI when PCR 0 is used, run

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# cryptsetup luksDump /dev/sdX
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Tokens:
  token slot: clevis
        Keyslot:  keyslot
```

to find the slot used for the Clevis pin, then

    # clevis luks regen -d /dev/sdX -s keyslot

To remove the Clevis binding, run:

    # clevis luks unbind -d /dev/sdX -s keyslot 

**Warning** Double check you have chosen the right slot, or you might lose access to your volume.

You can unlock a TPM-bound volume using:

    # clevis luks unlock -d /dev/sdX

For automated decryption of volumes in [/etc/crypttab](../en/Dm-crypt/System_configuration.html#crypttab "Dm-crypt/System configuration"), [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") `clevis-luks-askpass.path`.

For automated decryption of the root volume, we should make some changes to our [Initramfs](../en/Arch_boot_process.html#initramfs "Initramfs") generators:

### Mkinitcpio hook {#Mkinitcpio_hook}

Install the [mkinitcpio-clevis-hook](https://aur.archlinux.org/packages/mkinitcpio-clevis-hook/)^AUR^ package. Then enable the clevis hook editing [mkinitcpio.conf](../en/Mkinitcpio.html#Configuration "Mkinitcpio.conf"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/mkinitcpio.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# Edit the hooks and add clevis before the 'encrypt' hook. Eg:
HOOKS=(.. clevis encrypt ..)
```

**Note** If you are using plymouth, replace the `plymouth-encrypt` hook with encrypt. `plymouth-encrypt` is reported to be buggy when the device is already unlocked. [More info.](https://github.com/kishorv06/arch-mkinitcpio-clevis-hook/issues/1)

**Note** Clevis\'s integration with Tang requires [curl](https://archlinux.org/packages/?name=curl) present in the initramfs. Add it to the `BINARIES` array:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/mkinitcpio.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
BINARIES=(/usr/bin/curl)
```

Do not forget to perform network configuration. Using the mkinitcpio [net hook](../en/Mkinitcpio.html#Using_net "Mkinitcpio") is one way to do so.

At the end [regenerate the initramfs](../en/Regenerate_the_initramfs.html "Regenerate the initramfs").

### Booster {#Booster}

Luckily [Booster](../en/Booster.html "Booster") automatically decrypts LUKS volumes bound using Clevis out of the box!

Booster is also able to read the LUKS tokens, decode clevis information, reconstruct the password and unlock the partition automatically.

*Tang* (network binding) pin requires network enabled. Please refer to [Booster#Configuration](../en/Booster.html#Configuration "Booster") section for more information on network configuration with booster.

### Dracut {#Dracut}

[Dracut](../en/Dracut.html "Dracut") needs the following extra packages:

-   [libpwquality](https://archlinux.org/packages/?name=libpwquality)
-   [luksmeta](https://archlinux.org/packages/?name=luksmeta)
-   [nmap](https://archlinux.org/packages/?name=nmap)

Followed by an initramfs regeneration:

    # dracut -f

**Note** If you intend to use Clevis\' tang PIN to unlock your drive(s), `curl` must be included in the kernel image. Add a file to `/etc/dracut.conf.d` telling dracut to include it before running `dracut -f`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/dracut.conf.d/curl.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
install_items+=" /usr/bin/curl "
```

## Tips and tricks {#Tips_and_tricks}

### YubiKey binding {#YubiKey_binding}

Clevis allows binding a LUKS partition using YubiKey\'s challenge-response mode. To bind a LUKS partition, run

    # clevis luks bind -d /dev/sdX yubikey '{"slot":1}'

Install [yubikey-personalization](https://archlinux.org/packages/?name=yubikey-personalization). Edit the configuration file and add following option:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/booster.yaml
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
extra_files: ykchalresp
```

[Regenerate the booster images](../en/Booster.html#Usage "Booster"). Booster will detect this configuration during boot and use the present YubiKey to unlock the drive.

## See also {#See_also}

-   [Project homepage](https://github.com/latchset/clevis/)
-   [mkinitcpio-clevis-hook\'s homepage](https://github.com/kishorv06/arch-mkinitcpio-clevis-hook)
