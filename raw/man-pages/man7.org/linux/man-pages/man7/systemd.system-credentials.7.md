---
{"title": "systemd.system-credentials(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/systemd.system-credentials.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.system-credentials(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [WELL KNOWN SYSTEM CREDENTIALS](#WELL_KNOWN_SYSTEM_CREDENTIALS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD...EDENTIALS(7)  systemd.system-credentials SYSTEMD...EDENTIALS(7)

## [](#NAME)NAME

           systemd.system-credentials - System Credentials

## [](#DESCRIPTION)DESCRIPTION

           System and Service Credentials[1] are data objects that may be
           passed into booted systems or system services as they are invoked.
           They can be acquired from various external sources, and propagated
           into the system and from there into system services. Credentials
           may optionally be encrypted with a machine-specific key and/or
           locked to the local TPM2 device, and are only decrypted when the
           consuming service is invoked.

           System credentials may be used to provision and configure various
           aspects of the system. Depending on the consuming component
           credentials are only used on initial invocations or are needed for
           all invocations.

           Credentials may be used for any kind of data, binary or text, and
           may carry passwords, secrets, certificates, cryptographic key
           material, identity information, configuration, and more.

## [](#WELL_KNOWN_SYSTEM_CREDENTIALS)WELL KNOWN SYSTEM CREDENTIALS

           firstboot.keymap
               The console key mapping to set (e.g.  "de"). Read by
               systemd-firstboot(1), and only honoured if no console keymap
               has been configured before.

               Added in version 252.

           firstboot.hostname
               This credential specifies the static system hostname to set
               during first boot. The user will not be prompted for the
               hostname. Note that this controls the static hostname, not the
               transient hostname, and only has an effect on first boot,
               unlike system.hostname (see below). Read by
               systemd-firstboot(1) and only honoured if no static hostname
               has been configured before. The value may use the wildcard
               patterns documented in hostname(5) (e.g.  "$-$" or
               "foo-????"). When the credential is applied on the running
               system (the usual case, by systemd-firstboot.service on first
               boot), the wildcards are resolved against the machine ID and
               the resulting concrete name is written to /etc/hostname. The
               name is thus persisted once at first boot and does not change
               on subsequent boots even if the word lists are later updated
               or the pattern is changed (for example to add more "?"/"$"
               tokens for additional entropy), which is the recommended way
               to obtain a stable, per-machine generated hostname. (When
               systemd-firstboot(1) operates on an offline image via
               --root=/--image=, the target's machine ID is not yet known, so
               the pattern is written verbatim and, like a pattern placed
               directly in /etc/hostname, re-derived on every boot rather
               than persisted.)

               Added in version 261.

           firstboot.locale, firstboot.locale-messages
               The system locale to set (e.g.  "de_DE.UTF-8"). Read by
               systemd-firstboot(1), and only honoured if no locale has been
               configured before.  firstboot.locale sets "LANG", while
               firstboot.locale-message sets "LC_MESSAGES".

               Added in version 252.

           firstboot.timezone
               The system timezone to set (e.g.  "Europe/Berlin"). Read by
               systemd-firstboot(1), and only honoured if no system timezone
               has been configured before.

               Added in version 252.

           firstboot.machine-tags
               The machine tags to set, as a colon-separated list (e.g.
               "webserver:frontend:berlin"). Read by systemd-firstboot(1),
               and only honoured if /etc/machine-info has not been configured
               before. Written into the TAGS= field of that file, see
               machine-info(5) for details.

               Added in version 261.

           login.issue
               The data of this credential is written to
               /etc/issue.d/50-provision.conf, if the file does not exist
               yet.  agetty(8) reads this file and shows its contents at the
               login prompt of terminal logins. See issue(5) for details.

               Consumed by /usr/lib/tmpfiles.d/provision.conf, see
               tmpfiles.d(5).

               Added in version 252.

           login.motd
               The data of this credential is written to
               /etc/motd.d/50-provision.conf, if the file does not exist yet.
               pam_motd(8) reads this file and shows its contents as "message
               of the day" during terminal logins. See motd(5) for details.

               Consumed by /usr/lib/tmpfiles.d/provision.conf, see
               tmpfiles.d(5).

               Added in version 252.

           network.hosts
               The data of this credential is written to /etc/hosts, if the
               file does not exist yet. See hosts(5) for details.

               Consumed by /usr/lib/tmpfiles.d/provision.conf, see
               tmpfiles.d(5).

               Added in version 252.

           network.dns, network.search_domains
               DNS server information and search domains. Read by
               systemd-resolved.service(8).

               Added in version 253.

           network.conf.*, network.link.*, network.netdev.*,
           network.network.*
               Configures network devices. Read by
               systemd-network-generator.service(8). These credentials should
               contain valid networkd.conf(5), systemd.link(5),
               systemd.netdev(5), systemd.network(5) configuration data. From
               each matching credential a separate file is created. Example:
               the contents of a credential network.link.50-foobar will be
               copied into a file 50-foobar.link.

               Note that the resulting files are created world-readable, it
               is hence recommended to not include secrets in these
               credentials, but supply them via separate credentials directly
               to systemd-networkd.service, e.g.  network.wireguard.*  as
               described below.

               Added in version 256.

           network.wireguard.*
               Configures secrets for WireGuard netdevs. Read by
               systemd-networkd.service(8). For more information, refer to
               the [WireGuard] section of systemd.netdev(5).

               Added in version 256.

           passwd.hashed-password.root, passwd.plaintext-password.root
               May contain the password (either in UNIX hashed format, or in
               plaintext) for the root users. Read by both
               systemd-firstboot(1) and systemd-sysusers(8), and only
               honoured if no root password has been configured before.

               Added in version 252.

           passwd.shell.root
               The path to the shell program (e.g.  "/bin/bash") for the root
               user. Read by both systemd-firstboot(1) and
               systemd-sysusers(8), and only honoured if no root shell has
               been configured before.

               Added in version 252.

           ssh.ephemeral-authorized_keys-all
               Provides additional public keys, given in the customary
               authorized_keys format, for all users, for incoming
               connections via the generated AF_VSOCK and AF_UNIX socket
               units.

               The intended use of this is for a host system (in either VM or
               container configurations) to generate a keypair and inject the
               public key into the guest, using the private key to connect to
               any user account on the guest via ssh, without further
               authentication.

               Consumed by systemd-ssh-generator(8).

               Added in version 256.

           ssh.authorized_keys.root
               The data of this credential is written to
               /root/.ssh/authorized_keys, if the file does not exist yet.
               This allows provisioning SSH access for the system's root
               user.

               Consumed by /usr/lib/tmpfiles.d/provision.conf, see
               tmpfiles.d(5).

               Added in version 252.

           ssh.listen
               May be used to configure SSH sockets the system shall be
               reachable on. See systemd-ssh-generator(8) for details.

               Added in version 256.

           sysusers.extra
               Additional sysusers.d(5) lines to process during boot.

               Added in version 252.

           sysctl.extra
               Additional sysctl.d(5) lines to process during boot.

               Added in version 252.

           tmpfiles.extra
               Additional tmpfiles.d(5) lines to process during boot.

               Added in version 252.

           fstab.extra
               Additional mounts to establish at boot. For details, see
               systemd-fstab-generator(8).

               Added in version 254.

           vconsole.keymap, vconsole.keymap_toggle, vconsole.font,
           vconsole.font_map, vconsole.font_unimap
               Console settings to apply, see
               systemd-vconsole-setup.service(8) for details.

               Added in version 253.

           getty.auto
               Used for controlling the execution mode of
               systemd-getty-generator. See systemd-getty-generator(8) for
               details.

               Added in version 258.

           getty.ttys.serial, getty.ttys.container
               Used for spawning additional login prompts, see
               systemd-getty-generator(8) for details.

               Added in version 254.

           journal.forward_to_socket
               Used by systemd-journald(8) to determine where to forward log
               messages for socket forwarding, see journald.conf(5) for
               details.

               Added in version 256.

           journal.storage
               Used by systemd-journald(8) to determine where to store
               journal files, see journald.conf(5) for details.

               Added in version 256.

           vmm.notify_socket
               Configures an sd_notify(3) compatible AF_VSOCK socket the
               service manager will report status information, ready
               notification and exit status on. For details see systemd(1).

               Added in version 253.

           shell.prompt.prefix, shell.prompt.suffix
               Defines strings to prefix and suffix any interactive UNIX
               shell prompt with. For details see pam_systemd(8).

               Added in version 257.

           shell.welcome
               Define a string to print when an interactive UNIX shell
               initializes. For details see pam_systemd(8).

               Added in version 257.

           system.machine_id
               Takes a 128bit ID to initialize the machine ID from (if it is
               not set yet). Interpreted by the service manager (PID 1). For
               details see systemd(1).

               Added in version 254.

           system.hostname
               Accepts a (transient) hostname to configure during early boot.
               The static hostname specified in /etc/hostname, if configured,
               takes precedence over this setting. Interpreted by the service
               manager (PID 1). For details see systemd(1). Also see
               firstboot.hostname above. The value may use the wildcard
               patterns documented in hostname(5) ("?"  and "$"), which are
               expanded deterministically from the machine ID when the
               credential is applied. As this is a transient hostname that is
               re-applied on every boot, a wildcard value is re-derived each
               boot (and may change if the word lists change) and is never
               persisted; pass an already-resolved name if a stable hostname
               is required. Note also that the word-list tokens require the
               word lists to be present, which is generally not the case in
               the initrd so during initrd the default hostname is used and
               in late boot the resolved one becomes available.

               Added in version 254.

           home.add-signing-key.*
               Adds a new signing key for user records to the system. The
               credential contents should contain a user signing key, for
               example as reported by homectl get-signing-key. Multiple keys
               may be specified, and they will be put in place under the name
               of the credential name suffix (which must itself carry the
               .public suffix). For details see homectl(1).

               Added in version 258.

           home.create.*
               Creates a new home area for the specified user with the user
               record data passed in. For details see homectl(1).

               Added in version 256.

           home.register.*
               Registers an existing home area for the specified user with
               the user record data passed in. For details see homectl(1).

               Added in version 258.

           cryptsetup.passphrase, cryptsetup.tpm2-pin, cryptsetup.fido2-pin,
           cryptsetup.pkcs11-pin, cryptsetup.luks2-pin
               Specifies the passphrase/PINs to use for unlock encrypted
               storage volumes. For details see systemd-cryptsetup(8).

               Added in version 256.

           systemd.extra-unit.*, systemd.unit-dropin.*
               These credentials specify extra units and drop-ins to add to
               the system. For details see systemd-debug-generator(8).

               Added in version 256.

           udev.conf.*, udev.rules.*
               Configures udev configuration file and udev rules. Read by
               systemd-udev-load-credentials.service, which invokes udevadm
               control --load-credentials. These credentials directly
               translate to a matching udev.conf(5) or udev(7) rules file.
               Example: the contents of a credential udev.conf.50-foobar will
               be copied into a file /run/udev/udev.conf.d/50-foobar.conf,
               and udev.rules.50-foobar will be copied into a file
               /run/udev/rules.d/50-foobar.rules. See udev(7), udev.conf(5),
               and udevadm(8) for details.

               Added in version 256.

           import.pull
               Specified disk images (tarballs and DDIs) to automatically
               download and install at boot. For details see
               systemd-import-generator(8).

               Added in version 257.

           userdb.user.*, userdb.group.*, userdb.transient.user.*,
           userdb.transient.group.*
               Configure JSON user and group records. Read by
               systemd-userdb-load-credentials.service, which invokes
               userdbctl load-credentials. These credentials directly
               translate to matching JSON User[2] and JSON Group[3] records.
               Example: the contents of a credential userdb.user.foobar will
               be copied into a file /etc/userdb/foobar.user, and
               userdb.group.foobar will be copied into a file
               /etc/userdb/foobar.group. Symlinks for the uid/gid will also
               be created in /etc/userdb/, as well as the
               corresponding.membership files. See
               systemd-userdbd.service(7), nss-systemd(8), and userdbctl(1)
               for details.

               Any passed user records must contain uid and gid fields. Any
               passed group records must contain a gid field. For both user
               and group records, the credential suffix (for
               "userdb.user.foobar" the suffix is "foobar") must match the
               user or group name field from the user or group record.

               Note that the records created for userdb.user.*  and
               userdb.group.*  credentials are created in /etc/userdb/ and
               the records created for userdb.transient.user.*  and
               userdb.transient.group.*  are created in /run/userdb/
               (/etc/passwd and /etc/group are not modified).

               Added in version 258.

           fsck.*
               Read by systemd-fsck@.service, systemd-fsck-root.service, and
               systemd-fsck-usr.service. See systemd-fsck@.service(8) for
               more details.

               Added in version 258.

           quotacheck.*
               Read by systemd-quotacheck@.service and
               systemd-quotacheck-root.service. See systemd-quotacheck(8) for
               more details.

               Added in version 258.

           imds.*
               Read by systemd-imdsd@.service(8).

               Added in version 261.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), kernel-command-line(7), smbios-type-11(7)

## [](#NOTES)NOTES

            1. System and Service Credentials
               https://systemd.io/CREDENTIALS

            2. JSON User
               https://systemd.io/USER_RECORD

            3. JSON Group
               https://systemd.io/GROUP_RECORD

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

    systemd 262~devel                                  SYSTEMD...EDENTIALS(7)

------------------------------------------------------------------------

Pages that refer to this page: [systemd(1)](../man1/systemd.1.html),  [systemd-imds(1)](../man1/systemd-imds.1.html),  [hostname(5)](../man5/hostname.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [smbios-type-11(7)](../man7/smbios-type-11.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [nss-systemd(8)](../man8/nss-systemd.8.html),  [systemd-debug-generator(8)](../man8/systemd-debug-generator.8.html),  [systemd-getty-generator(8)](../man8/systemd-getty-generator.8.html),  [systemd-imds-generator(8)](../man8/systemd-imds-generator.8.html),  [systemd-import-generator(8)](../man8/systemd-import-generator.8.html),  [systemd-ssh-generator(8)](../man8/systemd-ssh-generator.8.html),  [systemd-sysinstall(8)](../man8/systemd-sysinstall.8.html)

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
