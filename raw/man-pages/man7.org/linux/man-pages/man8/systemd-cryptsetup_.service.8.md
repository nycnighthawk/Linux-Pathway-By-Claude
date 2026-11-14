---
{"title": "systemd-cryptsetup(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-cryptsetup@.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-cryptsetup(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CREDENTIALS](#CREDENTIALS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-CRYPTSETUP(8)       systemd-cryptsetup      SYSTEMD-CRYPTSETUP(8)

## [](#NAME)NAME

           systemd-cryptsetup, systemd-cryptsetup@.service - Full disk
           decryption logic

## [](#SYNOPSIS)SYNOPSIS

           systemd-cryptsetup [OPTIONS...] attach VOLUME SOURCE-DEVICE
                              [KEY-FILE] [CRYPTTAB-OPTIONS]

           systemd-cryptsetup [OPTIONS...] detach VOLUME

           systemd-cryptsetup@.service

           system-systemd\x2dcryptsetup.slice

## [](#DESCRIPTION)DESCRIPTION

           systemd-cryptsetup is used to set up (with attach) and tear down
           (with detach) access to an encrypted block device. It is primarily
           used via systemd-cryptsetup@.service during early boot, but may
           also be called manually. The positional arguments VOLUME,
           SOURCE-DEVICE, KEY-FILE, and CRYPTTAB-OPTIONS have the same
           meaning as the fields in crypttab(5).

           systemd-cryptsetup@.service is a service responsible for providing
           access to encrypted block devices. It is instantiated for each
           device that requires decryption.

           systemd-cryptsetup@.service instances are part of the
           system-systemd\x2dcryptsetup.slice slice, which is destroyed only
           very late in the shutdown procedure. This allows the encrypted
           devices to remain up until filesystems have been unmounted.

           systemd-cryptsetup@.service will ask for hard disk passwords via
           the password agent logic[1], in order to query the user for the
           password using the right mechanism at boot and during runtime.

           At early boot and when the system manager configuration is
           reloaded, /etc/crypttab is translated into
           systemd-cryptsetup@.service units by
           systemd-cryptsetup-generator(8).

           In order to unlock a volume a password or binary key is required.
           systemd-cryptsetup@.service tries to acquire a suitable password
           or binary key via the following mechanisms, tried in order:

            1. If a key file is explicitly configured (via the third column
               in /etc/crypttab), a key read from it is used. If a PKCS#11
               token, FIDO2 token or TPM2 device is configured (using the
               pkcs11-uri=, fido2-device=, tpm2-device= options) the key is
               decrypted before use.

            2. If no key file is configured explicitly this way, a key file
               is automatically loaded from /etc/cryptsetup-keys.d/volume.key
               and /run/cryptsetup-keys.d/volume.key, if present. Here too,
               if a PKCS#11/FIDO2/TPM2 token/device is configured, any key
               found this way is decrypted before use.

            3. If the try-empty-password option is specified then unlocking
               the volume with an empty password is attempted.

            4. If the password-cache= option is set to "yes" or "read-only",
               the kernel keyring is then checked for a suitable cached
               password from previous attempts.

            5. Finally, the user is queried for a password, possibly multiple
               times, unless the headless option is set.

           If no suitable key may be acquired via any of the mechanisms
           describes above, volume activation fails.

## [](#CREDENTIALS)CREDENTIALS

           systemd-cryptsetup supports the service credentials logic as
           implemented by ImportCredential=/LoadCredential=/SetCredential=
           (see systemd.exec(5) for details). The following credentials are
           used by "systemd-crypsetup@root.service" (generated by
           systemd-gpt-auto-generator) when passed in:

           cryptsetup.passphrase
               This credential specifies the passphrase of the LUKS volume.

               Added in version 256.

           cryptsetup.tpm2-pin
               This credential specifies the TPM pin.

               Added in version 256.

           cryptsetup.fido2-pin
               This credential specifies the FIDO2 token pin.

               Added in version 256.

           cryptsetup.pkcs11-pin
               This credential specifies the PKCS11 token pin.

               Added in version 256.

           cryptsetup.luks2-pin
               This credential specifies the pin requested by generic LUKS2
               token modules.

               Added in version 256.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-cryptsetup-generator(8), crypttab(5),
           systemd-cryptenroll(1), cryptsetup(8), TPM2 PCR Measurements Made
           by systemd[2]

## [](#NOTES)NOTES

            1. password agent logic
               https://systemd.io/PASSWORD_AGENTS/

            2. TPM2 PCR Measurements Made by systemd
               https://systemd.io/TPM2_PCR_MEASUREMENTS

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                   SYSTEMD-CRYPTSETUP(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-cryptenroll(1)](../man1/systemd-cryptenroll.1.html),  [systemd-measure(1)](../man1/systemd-measure.1.html),  [crypttab(5)](../man5/crypttab.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-stub(7)](../man7/systemd-stub.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [pam_systemd_loadkey(8)](../man8/pam_systemd_loadkey.8.html),  [systemd-cryptsetup-generator(8)](../man8/systemd-cryptsetup-generator.8.html),  [systemd-gpt-auto-generator(8)](../man8/systemd-gpt-auto-generator.8.html),  [systemd-pcrlock(8)](../man8/systemd-pcrlock.8.html)

------------------------------------------------------------------------

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
