---
{"title": "systemd-vmspawn(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-vmspawn.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-vmspawn(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXAMPLES](#EXAMPLES) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-VMSPAWN(1)           systemd-vmspawn           SYSTEMD-VMSPAWN(1)

## [](#NAME)NAME

           systemd-vmspawn - Spawn an OS in a virtual machine

## [](#SYNOPSIS)SYNOPSIS

           systemd-vmspawn [OPTIONS...] [ARGS...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-vmspawn may be used to start a virtual machine from an OS
           image. In many ways it is similar to systemd-nspawn(1), but
           launches a full virtual machine instead of using namespaces.

           File descriptors for /dev/kvm and /dev/vhost-vsock can be passed
           to systemd-vmspawn via systemd's native socket passing interface
           (see sd_listen_fds(3) for details about the precise protocol used
           and the order in which the file descriptors are passed), these
           file descriptors must be passed with the names "kvm" and
           "vhost-vsock" respectively.

           Note: on Ubuntu/Debian derivatives systemd-vmspawn requires the
           user to be in the "kvm" group to use the VSOCK options.

## [](#OPTIONS)OPTIONS

           The excess arguments are passed as extra kernel command line
           arguments using SMBIOS.

           The following options are understood:

           -q, --quiet
               Turns off any status output by the tool itself. When this
               switch is used, the only output from vmspawn will be the
               console output of the Virtual Machine OS itself.

               Added in version 256.

           --system, --user
               Specify whether to interact with the user manager or the
               system manager and whether to register with the user machined
               instance or the system machined instance. If unspecified, the
               system manager and machined instance will be used when running
               as root, otherwise the user manager and machined instance will
               be used.

               Added in version 260.

       Image Options
           -D, --directory=
               Directory to use as file system root for the virtual machine.

               One of either --directory= or --image= must be specified. If
               neither are specified --directory=.  is assumed.

               Note: If mounting a non-root owned directory you may require
               --private-users= to map into the user's subuid namespace. An
               example of how to use /etc/subuid for this is given later.

               Added in version 256.

           -x, --ephemeral
               If specified, the VM is run with a temporary snapshot of its
               file system that is removed immediately when the VM
               terminates. Only works with --image= currently. Note that
               --ephemeral will not work with --extra-drive=.

               Added in version 260.

           -i, --image=
               Root file system disk image (or device node) for the virtual
               machine.

               Added in version 255.

           --image-format=FORMAT
               Specifies the format of the disk image passed to --image=.
               Takes either "raw" or "qcow2". Defaults to "raw". Note that
               "qcow2" is only supported for regular files, not block
               devices.

               Added in version 260.

           --image-disk-type=TYPE
               Specifies the disk type to use for the root disk passed to
               --image=. Extra drives added via --extra-drive= inherit this
               disk type unless overridden with an explicit disk type prefix.
               Takes one of "virtio-blk", "virtio-scsi", "nvme", or
               "scsi-cd". Defaults to "virtio-blk". When "scsi-cd" is
               specified, the disk is attached as a read-only CD-ROM drive.

               Added in version 261.

           --discard-disk=BOOL
               Controls whether qemu processes discard requests from the VM.
               This prevents long running VMs from using more disk space than
               required. This is enabled by default.

               Added in version 256.

           --grow-image=BYTES, -G BYTES
               Grows the image file specified by --image= to the specified
               size in bytes if it is smaller. Executes no operation if no
               image file is used or the image file is already as large or
               larger than requested. The specified size accepts the usual K,
               M, G suffixes (to the base of 1024). Specified values are
               rounded up to multiples of 4096.

               Added in version 258.

       Host Configuration
           --cpus=CPUS
               The number of CPUs to start the virtual machine with. Defaults
               to 1.

               Added in version 255.

           --ram=BYTES[:MAXBYTES[:SLOTS]]
               The amount of memory to start the virtual machine with.
               Defaults to 2G. If a maximum size is specified after a colon,
               memory hotplug is enabled with the given upper limit. The
               number of hotplug slots can optionally be specified after a
               second colon and defaults to 1.

               Added in version 255.

           --kvm=BOOL
               Controls whether to enable KVM acceleration. If not specified
               or set to auto, KVM support will be detected automatically. If
               true, KVM is insisted on. If false, disable KVM.

               Added in version 255.

           --vsock=BOOL
               Controls whether to allocate a VSOCK socket for guest. If not
               specified or set to auto, VSOCK networking support will be
               detected automatically. If true, VSOCK is insisted on. If
               false, VSOCK networking is disabled.

               Added in version 255.

           --vsock-cid=CID
               Sets the specific CID to use for the guest. Valid CIDs are in
               the range 3 to 4294967294 (0xFFFF_FFFE). CIDs outside of this
               range are reserved. By default, vmspawn will attempt to derive
               a CID for the guest derived from the machine name, falling
               back to a random CID if this CID is taken.

               Added in version 255.

           --tpm=BOOL
               Controls whether to serve a TPM device for guest, via
               swtpm(8). If not specified or set to auto, vmspawn will detect
               the presence of swtpm binary automatically. If yes, swtpm
               support is insisted on. If no, TPM is disabled.

               Added in version 256.

           --tpm-state=PATH|auto|off
               Configures where to place TPM state, in case TPM support is
               enabled (see --tpm= above). This takes an absolute file system
               path to a directory to persistently place the state in. If the
               directory is missing it is created as needed. If set to the
               special string "auto" a persistent path is automatically
               derived from the VM image path or directory path, with the
               ".tpmstate" suffix appended. If set to the special string
               "off" the TPM state is only maintained transiently and flushed
               out when the VM shuts down. This mode is not suitable for VMs
               which lock disk encryption keys to the TPM, as these keys will
               be lost on every reboot. Defaults to "auto".

               If --ephemeral is specified, "auto" behaves like "off".

               Added in version 258.

           --efi-nvram-template=PATH
               Takes an absolute path, or a relative path beginning with ./.
               Specifies the path to an EFI NVRAM template file to copy and
               use as the initial EFI variable NVRAM state. If not specified,
               the default NVRAM template from the firmware definition is
               copied and used. Cannot be used together with --coco=, as
               confidential computing firmware is stateless.

               Added in version 261.

           --efi-nvram-state=PATH|auto|off
               Configures where to place the EFI variable NVRAM state. This
               takes an absolute file system path to a regular file to
               persistently place the state in. If the file is missing it is
               created as needed. If set to the special string "auto" a
               persistent path is automatically derived from the VM image
               path or directory path, with the ".efinvramstate" suffix
               appended. If set to the special string "off" the EFI variable
               NVRAM state is only maintained transiently and flushed out
               when the VM shuts down. Defaults to "auto". An explicit path
               cannot be used together with --coco=, as confidential
               computing firmware is stateless.

               If --ephemeral is specified, "auto" behaves like "off".

               Added in version 261.

           --secure-boot=BOOL
               Configure whether to search for firmware which supports Secure
               Boot. Takes a boolean or "auto". Setting this to yes is
               equivalent to --firmware-features=secure-boot and setting this
               to no is equivalent to --firmware-features=~secure-boot.
               Setting this to "auto" removes "secure-boot" from both the
               included and excluded feature lists.

               With --coco=, setting this to "yes" additionally requires the
               "enrolled-keys" firmware feature, overriding its default
               exclusion: confidential computing firmware is stateless, so
               keys cannot be enrolled at runtime and Secure Boot is only
               operative with keys baked into the image at build time, which
               in turn makes the firmware refuse to boot unsigned images from
               the very first boot. The default exclusion of "enrolled-keys"
               hence keeps unsigned images bootable.

               Added in version 255.

           --firmware=PATH
               Selects which firmware to use in the VM. Takes one of "auto",
               "uefi", "bios", "none", an absolute path, or a relative path
               beginning with ./. Defaults to "auto", which selects UEFI
               firmware unless --linux= specifies a non-PE kernel image, in
               which case "none" is selected.  "uefi" loads OVMF firmware
               (use a path to a JSON firmware definition file to select a
               specific one).  "bios" skips OVMF loading and lets QEMU use
               its built-in BIOS (e.g. SeaBIOS on x86).  "none" disables
               firmware loading entirely and requires --linux= to be
               specified for direct kernel boot. Booting a UKI requires
               "uefi". If the special string "list" is specified, all
               discovered firmware definition files are listed. If the
               special string "describe" is specified, the UEFI firmware that
               would be selected (taking --firmware-features= and --coco=
               into account) is printed and the program exits. If an empty
               string is specified, the option is reset to its default.

               Added in version 256.

           --firmware-features=FEATURE[,FEATURE...]
               Takes a comma-delimited list of firmware feature strings. This
               option may be specified multiple times, in which case the
               feature lists are combined. When specified, only firmware
               definitions that have all the required features will be
               considered during automatic firmware discovery. Features
               prefixed with "~" are excluded: firmware that has such a
               feature will be skipped. If a feature appears in both the
               included and excluded lists, inclusion takes priority. By
               default, firmware with the "enrolled-keys" feature is
               excluded. If an empty string is passed, both the included and
               excluded feature lists are reset. If the special string "list"
               is specified, lists all available firmware features.

               Added in version 261.

           --coco=
               Caveat: This feature is experimental, and is likely to be
               changed (or removed in its current form) in a future version
               of systemd.

               Configures whether to run the guest as a confidential VM.
               Takes one of "no", "sev-snp" or "tdx". Defaults to "no".

               "sev-snp" enables AMD SEV-SNP. This requires KVM on an x86_64
               host with SNP-capable hardware and firmware. A suitable
               SNP-built OVMF firmware is picked automatically from the
               installed QEMU firmware descriptors, by requiring the
               "amd-sev-snp" firmware feature; use --firmware= with a path to
               a firmware descriptor file to select a specific one. Secure
               Boot is effectively off by default (see --secure-boot=).
               Direct kernel boot via --linux= is required so that the
               kernel, initrd and command line are hashed into the launch
               measurement ("kernel-hashes=on"); booting the kernel off the
               disk image via the firmware would leave it outside the
               measurement. Credentials passed via --set-credential= or
               --load-credential= are bundled into a cpio archive appended to
               the initrd (mirroring what systemd-stub does for ESP
               credentials), so they enter the launch measurement via
               "kernel-hashes=on"; the SMBIOS and fw_cfg channels normally
               used to deliver credentials are not used because they are
               unmeasured and would be discarded by PID1 in confidential
               guests. This channel is measured but not confidential with
               respect to the host or VMM: the initrd (and thus the
               credentials it carries) is supplied to QEMU as plaintext and
               only its hash enters the launch measurement, which guarantees
               integrity but does not keep the credentials secret from the
               host. This requires the guest to run a sufficiently recent
               version of systemd (supporting /.extra/system_credentials/). A
               vTPM, if attached via --tpm=, must be treated as untrusted by
               the guest.

               "tdx" enables Intel TDX. This requires KVM on an x86_64 host
               with TDX-capable hardware and a TDX-enabled host kernel. As
               with "sev-snp", a TDX-built OVMF (TDVF) firmware is picked
               automatically from the installed QEMU firmware descriptors, by
               requiring the "intel-tdx" firmware feature; use --firmware=
               with a path to a firmware descriptor file to select a specific
               one. The CPU model is fixed to "host". Firmware is measured
               into MRTD when the TD is built. Secure Boot cannot be enrolled
               at runtime (there is no writable NVRAM); its state is fixed by
               the selected TDVF image and is part of the measured firmware
               (see --secure-boot=). When booting a UKI, the whole UKI PE is
               measured into RTMR 1, and the loaded sections are measured
               individually by systemd-stub into RTMR 2. For direct linux
               boot, firmware measures the kernel PE into RTMR 1, and the
               Linux EFI stub measures initrd and command line into RTMR 2.
               Credentials passed via --set-credential= or --load-credential=
               are delivered through SMBIOS Type 11 OEM strings, which the
               firmware (TDVF) measures into RTMR 0. This channel is measured
               but not confidential with respect to the host or VMM, since
               the host assembles the SMBIOS table. A vTPM, if attached via
               --tpm=, must be treated as untrusted by the guest. To obtain
               TD Quotes for remote attestation, the guest is wired to the
               host's local TDX Quote Generation Service automatically: the
               unix socket /run/tdx-qgs/qgs.socket is used if it exists,
               otherwise vsock port 4050 on the host (cid 2). If the QGS is
               listening on neither channel, the guest's quote requests will
               fail.  Added in version 262.

               Added in version 261.

       Networking Options
           -n, --network-tap
               Create a TAP device to network with the virtual machine.

               Note: root privileges are required to use TAP networking.
               Additionally, systemd-networkd(8) must be running and
               correctly set up on the host to provision the host interface.
               The relevant ".network" file can be found at
               /usr/lib/systemd/network/80-vm-vt.network.

               Added in version 255.

           --network-user-mode
               Use user mode networking.

               Added in version 255.

       Execution Options
           --linux=PATH
               Set the linux kernel image to use for direct kernel boot. If a
               directory type image is used and --linux= was omitted, vmspawn
               will search for boot loader entries according to the UAPI.1
               Boot Loader Specification[1] assuming XBOOTLDR to be located
               at /boot and ESP to be /efi respectively. If no kernel was
               installed into the image then the image will fail to boot.

               Added in version 256.

           --initrd=PATH
               Set the initrd to use for direct kernel boot. If the --linux=
               supplied is a UAPI.1 Boot Loader Specification[1] Type #2
               entry, then this argument is not required. If no initrd was
               installed into the image then the image will fail to boot.

               --initrd= can be specified multiple times and vmspawn will
               merge them together.

               Added in version 256.

           --smbios11=STRING, -s STRING
               Passes the specified string into the VM as an SMBIOS Type #11
               vendor string. This is useful to parameterize the invoked VM
               in various ways. See smbios-type-11(7) for details.

               Added in version 258.

           --notify-ready=
               Configures support for notifications from the VM's init
               process to systemd-vmspawn. If true, systemd-vmspawn will
               consider the machine as ready only when it has received a
               "READY=1" message from the init process in the VM. If false,
               systemd-vmspawn will consider the machine as ready immediately
               after creation. In either case, systemd-vmspawn sends its own
               readiness notification to its manager after the spawned VM is
               ready. For more details about notifications see sd_notify(3).

               Defaults to true. (Note that this is unlike the option of the
               same name to systemd-nspawn(1) that defaults to false.)

               Added in version 258.

       System Identity Options
           -M, --machine=
               Sets the machine name for this virtual machine. This name may
               be used to identify this virtual machine during its runtime
               (for example in tools like machinectl(1) and similar).

               Added in version 255.

           --uuid=
               Set the specified UUID for the virtual machine. The init
               system will initialize /etc/machine-id from this if this file
               is not set yet. Note that this option takes effect only if
               /etc/machine-id in the virtual machine is unpopulated.

               Added in version 256.

       Property Options
           -S, --slice=
               Make the VM part of the specified slice, instead of the
               default machine.slice. This applies only if the machine is run
               in its own scope unit, i.e. if --keep-unit is not used.

               Added in version 258.

           --property=
               Set a unit property on the scope unit to register for the
               machine. This applies only if the machine is run in its own
               scope unit, i.e. if --keep-unit is not used. Takes unit
               property assignments in the same format as systemctl
               set-property. This is useful to set memory limits and similar
               for the VM.

               Added in version 258.

           --register=
               Controls whether the virtual machine is registered with
               systemd-machined(8). Takes a boolean argument or "auto", and
               defaults to "auto". This ensures that the virtual machine is
               accessible via machinectl(1). When set to "auto", registration
               is attempted but failures are ignored.

               Added in version 256.

       User Namespacing Options
           --private-users=UID_SHIFT[:UID_RANGE]
               Controls user namespacing under --directory=. If enabled,
               virtiofsd(1) is instructed to map user and group ids (UIDs and
               GIDs). This involves mapping the private UIDs/GIDs used in the
               virtual machine (starting with the virtual machine's root user
               0 and up) to a range of UIDs/GIDs on the host that are not
               used for other purposes (usually in the range beyond the
               host's UID/GID 65536).

               If one or two colon-separated numbers are specified, user
               namespacing is turned on.  UID_SHIFT specifies the first host
               UID/GID to map, UID_RANGE is optional and specifies number of
               host UIDs/GIDs to assign to the virtual machine. If UID_RANGE
               is omitted, 65536 UIDs/GIDs are assigned.

               When user namespaces are used, the GID range assigned to each
               virtual machine is always chosen identical to the UID range.

               Added in version 256.

       Mount Options
           --bind=PATH, --bind-ro=PATH
               Mount a directory from the host into the virtual machine.
               Takes one of: a path argument — in which case the specified
               path will be mounted from the host to the same path in the
               virtual machine, or a colon-separated pair of paths — in which
               case the first specified path is the source in the host, and
               the second path is the destination in the virtual machine. If
               the source path is not absolute, it is resolved relative to
               the current working directory. The --bind-ro= option creates
               read-only bind mounts. Backslash escapes are interpreted, so
               "\:" may be used to embed colons in either path. This option
               may be specified multiple times for creating multiple
               independent bind mount points.

               Added in version 256.

           --extra-drive=[FORMAT:][DISKTYPE:]PATH
               Takes a disk image or block device on the host and supplies it
               to the virtual machine as another drive. Optionally, the image
               format and/or disk type can be specified by prefixing the path
               with their values separated by colons. The format and disk
               type prefixes can appear in any order. The format defaults to
               "raw" and the disk type defaults to the value of
               --image-disk-type= (which itself defaults to "virtio-blk").
               Note that "qcow2" is only supported for regular files, not
               block devices.

               Added in version 256.

           --bind-volume=PROVIDER:VOLUME[:CONFIG][:K=V,...]
               Acquire a storage volume from a storagectl(1) provider and
               attach it to the virtual machine.  PROVIDER is the provider
               name (typically "block" or "fs").  VOLUME is the volume name
               passed to the provider's Acquire() method.  CONFIG selects the
               guest device type and takes one of "virtio-blk",
               "virtio-scsi", "nvme", or "scsi-cd". If empty or omitted,
               defaults to "virtio-blk".

               The trailing comma-separated K=V list passes parameters to
               io.systemd.StorageProvider.Acquire(): template=, create= (one
               of "any", "new", "open"), read-only= (or ro=; takes a boolean
               or "auto"), size= / create-size= (size for created volumes),
               request-as= (one of "blk", "reg", "dir"; "dir" is rejected by
               vmspawn).

               Each attached volume is identified by the name
               "PROVIDER:VOLUME". Volumes attached at startup via this option
               cannot be detached at runtime via machinectl unbind-volume;
               only volumes added at runtime via machinectl bind-volume are
               removable.

               The provider is looked up under
               /run/systemd/io.systemd.StorageProvider/ for system mode (or
               $XDG_RUNTIME_DIR/systemd/io.systemd.StorageProvider/ for user
               mode), matching the runtime scope chosen via --user /
               --system.

               Added in version 261.

           --bind-user=
               Binds the home directory of the specified user on the host
               into the virtual machine. Takes the name of an existing user
               on the host as argument. May be used multiple times to bind
               multiple users into the virtual machine. This does two things:

                1. The user's home directory is made available from the host
                   into /run/vmhost/home/ using virtiofs. virtiofsd id
                   translation to map the host user's UID/GID to its assigned
                   UID/GID in the virtual machine.

                2. JSON user and group records are generated in that
                   describes the mapped user which are passed into the
                   virtual machine using "userdb.transient.*"  credentials.
                   They contain a minimized representation of the host's user
                   record, adjusted to the UID/GID and home directory path
                   assigned to the user in the virtual machine. The
                   nss-systemd(8) glibc NSS module will pick up these records
                   from there and make them available in the virtual
                   machine's user/group databases.

               The combination of the two operations above ensures that it is
               possible to log into the virtual machine using the same
               account information as on the host. The user is only mapped
               transiently, while the virtual machine is running, and the
               mapping itself does not result in persistent changes to the
               virtual machine (except maybe for log messages generated at
               login time, and similar). Note that in particular the UID/GID
               assignment in the virtual machine is not made persistently. If
               the user is mapped transiently, it is best to not allow the
               user to make persistent changes to the virtual machine. If the
               user leaves files or directories owned by the user, and those
               UIDs/GIDs are reused during later virtual machine invocations
               (possibly with a different --bind-user= mapping), those files
               and directories will be accessible to the "new" user.

               The user/group record mapping only works if the virtual
               machine contains systemd 258 or newer, with nss-systemd
               properly configured in nsswitch.conf. See nss-systemd(8) for
               details.

               Note that the user record propagated from the host into the
               virtual machine will contain the UNIX password hash of the
               user, so that seamless logins in the virtual machine are
               possible. If the virtual machine is less trusted than the host
               it is hence important to use a strong UNIX password hash
               function (e.g. yescrypt or similar, with the "$y$" hash
               prefix).

               Added in version 259.

           --bind-user-shell=
               When used with --bind-user=, includes the specified shell in
               the user records of users bound into the virtual machine.
               Takes either a boolean or an absolute path.

               •   If false (the default), no shell is passed in the user
                   records for users bound into the virtual machine. This
                   causes bound users to the use the virtual machine's
                   default shell.

               •   If true, the shells specified by the host user records are
                   included in the user records of all users bound into the
                   virtual machine.

               •   If passed an absolute path, sets that path as the shell
                   for user records of all users bound into the virtual
                   machine.

               Note: This will not check whether the specified shells exist
               in the virtual machine.

               This operation is only supported in combination with
               --bind-user=.

               Added in version 259.

           --bind-user-group=NAME
               When used with --bind-user=, includes the specified group as
               an auxiliary group in the user records of users bound into the
               virtual machine. Takes a group name.

               Note: This will not check whether the specified groups exist
               in the virtual machine.

               This operation is only supported in combination with
               --bind-user=.

               Added in version 259.

       Logging Options
           --forward-journal=FILE|DIR
               Forward the virtual machine's journal to the host.
               systemd-journal-remote(8) is currently used to receive the
               guest VM's forwarded journal entries. This option determines
               where this journal is saved on the host and has the same
               semantics as -o/--output described in
               systemd-journal-remote(8).

               Added in version 256.

           --forward-journal-max-use=BYTES,
           --forward-journal-keep-free=BYTES,
           --forward-journal-max-file-size=BYTES,
           --forward-journal-max-files=N
               These options configure the corresponding settings of
               systemd-journal-remote(8) when forwarding journal entries from
               the VM. See journal-remote.conf(5) for the descriptions of
               these settings.

               Added in version 261.

       SSH Options
           --pass-ssh-key=BOOL
               By default, an SSH key is generated to allow systemd-vmspawn
               to open a D-Bus connection to the VM's systemd bus. Setting
               this to "no" will disable SSH key generation.

               The generated keys are ephemeral. That is they are valid only
               for the current invocation of systemd-vmspawn, and are
               typically not persisted.

               Added in version 256.

           --ssh-key-type=TYPE
               Configures the type of SSH key to generate, see ssh-keygen(1)
               for more information.

               By default, "ed25519" keys are generated, however "rsa" keys
               may also be useful if the VM has a particularly old version of
               sshd(8).

               Added in version 256.

       Input/Output Options
           --console=MODE
               Configures how to set up the console of the VM. Takes one of
               "interactive", "read-only", "native", "gui", "headless".
               Defaults to "interactive".  "interactive" provides an
               interactive terminal interface to the VM.  "read-only" is
               similar, but is strictly read-only, i.e. does not accept any
               input from the user.  "native" also provides a TTY-based
               interface, but uses qemu native implementation (which means
               the qemu monitor is available).  "gui" shows the qemu
               graphical UI.  "headless" runs the VM without any console,
               which is useful for automated or scripted usage.

               Added in version 256.

           --console-transport=TRANSPORT
               Configures the transport to use for the VM console. Takes one
               of "virtio" or "serial". Defaults to "virtio".  "virtio" uses
               a virtio-serial device, which appears as /dev/hvc0 in the VM.
               "serial" uses a regular serial port, which appears as
               /dev/ttyS0 (or /dev/ttyAMA0 on ARM) in the VM. This option
               only has an effect in --console=interactive,
               --console=read-only, and --console=native modes.

               Added in version 261.

           --background=COLOR
               Change the terminal background color to the specified ANSI
               color as long as the VM runs. The color specified should be an
               ANSI X3.64 SGR background color, i.e. strings such as "40",
               "41", ..., "47", "48;2;...", "48;5;...". See ANSI Escape Code
               (Wikipedia)[2] for details. Assign an empty string to disable
               any coloring. This only has an effect in --console=interactive
               and --console=read-only modes.

               Added in version 256.

       Credentials
           --load-credential=ID:PATH, --set-credential=ID:VALUE
               Pass a credential to the virtual machine. These two options
               correspond to the LoadCredential= and SetCredential= settings
               in unit files. See systemd.exec(5) for details about these
               concepts, as well as the syntax of the option's arguments.

               In order to embed binary data into the credential data for
               --set-credential=, use C-style escaping (i.e.  "\n" to embed a
               newline, or "\x00" to embed a NUL byte). Note that the
               invoking shell might already apply unescaping once, hence this
               might require double escaping!

               Credentials are preferably passed to the VM via SMBIOS Type 11
               strings or QEMU fw_cfg files. If neither mechanism is
               available, credentials are passed on the kernel command line
               using systemd.set_credential_binary= which is not a
               confidential channel. Do not use this for passing secrets to
               the VM in that case.

               Under --coco=sev-snp, SMBIOS and fw_cfg are not covered by the
               SNP launch measurement and are discarded by PID1 in
               confidential guests. Credentials are therefore packaged into a
               cpio archive containing .extra/system_credentials/ID.cred
               entries and appended to the initrd that QEMU loads, so they
               enter the launch measurement via "kernel-hashes=on". PID1
               imports them from the initramfs at boot. As with the kernel
               command line, this is a measured but not a confidential
               channel: QEMU receives the initrd (and thus the embedded
               credentials) as plaintext from the host and only its hash is
               covered by the launch measurement, so a modified initrd
               produces a different launch measurement that a relying party
               can detect via remote attestation, but the credentials are not
               hidden from the host or VMM. This requires the guest to run a
               sufficiently recent version of systemd (supporting
               /.extra/system_credentials/).

               Added in version 255.

       Other
           --no-pager
               Do not pipe output into a pager.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

           --no-ask-password
               Do not query the user for authentication for privileged
               operations.

## [](#ENVIRONMENT)ENVIRONMENT

           $SYSTEMD_LOG_LEVEL
               The maximum log level of emitted messages (messages with a
               higher log level, i.e. less important ones, will be
               suppressed). Takes a comma-separated list of values. A value
               may be either one of (in order of decreasing importance)
               emerg, alert, crit, err, warning, notice, info, debug, or an
               integer in the range 0...7. See syslog(3) for more
               information. Each value may optionally be prefixed with one of
               console, syslog, kmsg or journal followed by a colon to set
               the maximum log level for that specific log target (e.g.
               SYSTEMD_LOG_LEVEL=debug,console:info specifies to log at debug
               level except when logging to the console which should be at
               info level). Note that the global maximum log level takes
               priority over any per target maximum log levels.

           $SYSTEMD_LOG_COLOR
               A boolean. If true, messages written to the tty will be
               colored according to priority.

               This setting is only useful when messages are written directly
               to the terminal, because journalctl(1) and other tools that
               display logs will color messages based on the log level on
               their own.

           $SYSTEMD_LOG_TIME
               A boolean. If true, console log messages will be prefixed with
               a timestamp.

               This setting is only useful when messages are written directly
               to the terminal or a file, because journalctl(1) and other
               tools that display logs will attach timestamps based on the
               entry metadata on their own.

           $SYSTEMD_LOG_LOCATION
               A boolean. If true, messages will be prefixed with a filename
               and line number in the source code where the message
               originates.

               Note that the log location is often attached as metadata to
               journal entries anyway. Including it directly in the message
               text can nevertheless be convenient when debugging programs.

           $SYSTEMD_LOG_TID
               A boolean. If true, messages will be prefixed with the current
               numerical thread ID (TID).

               Note that the this information is attached as metadata to
               journal entries anyway. Including it directly in the message
               text can nevertheless be convenient when debugging programs.

           $SYSTEMD_LOG_TARGET
               The destination for log messages. One of console (log to the
               attached tty), console-prefixed (log to the attached tty but
               with prefixes encoding the log level and "facility", see
               syslog(3), kmsg (log to the kernel circular log buffer),
               journal (log to the journal), journal-or-kmsg (log to the
               journal if available, and to kmsg otherwise), auto (determine
               the appropriate log target automatically, the default), null
               (disable log output).

           $SYSTEMD_LOG_RATELIMIT_KMSG
               Whether to ratelimit kmsg or not. Takes a boolean. Defaults to
               "true". If disabled, systemd will not ratelimit messages
               written to kmsg.

           $SYSTEMD_PAGER, $PAGER
               Pager to use when --no-pager is not given.  $SYSTEMD_PAGER is
               used if set; otherwise $PAGER is used. If neither
               $SYSTEMD_PAGER nor $PAGER are set, a set of well-known pager
               implementations is tried in turn, including less(1) and
               more(1), until one is found. If no pager implementation is
               discovered, no pager is invoked. Setting those environment
               variables to an empty string or the value "cat" is equivalent
               to passing --no-pager.

               Note: if $SYSTEMD_PAGERSECURE is not set, $SYSTEMD_PAGER and
               $PAGER can only be used to disable the pager (with "cat" or
               ""), and are otherwise ignored.

           $SYSTEMD_LESS
               Override the options passed to less (by default "FRSXMK").

               Users might want to change two options in particular:

               K
                   This option instructs the pager to exit immediately when
                   Ctrl+C is pressed. To allow less to handle Ctrl+C itself
                   to switch back to the pager command prompt, unset this
                   option.

                   If the value of $SYSTEMD_LESS does not include "K", and
                   the pager that is invoked is less, Ctrl+C will be ignored
                   by the executable, and needs to be handled by the pager.

               X
                   This option instructs the pager to not send termcap
                   initialization and deinitialization strings to the
                   terminal. It is set by default to allow command output to
                   remain visible in the terminal even after the pager exits.
                   Nevertheless, this prevents some pager functionality from
                   working, in particular paged output cannot be scrolled
                   with the mouse.

               Note that setting the regular $LESS environment variable has
               no effect for less invocations by systemd tools.

               See less(1) for more discussion.

           $SYSTEMD_LESSCHARSET
               Override the charset passed to less (by default "utf-8", if
               the invoking terminal is determined to be UTF-8 compatible).

               Note that setting the regular $LESSCHARSET environment
               variable has no effect for less invocations by systemd tools.

           $SYSTEMD_PAGERSECURE
               Common pager commands like less(1), in addition to "paging",
               i.e. scrolling through the output, support opening of or
               writing to other files and running arbitrary shell commands.
               When commands are invoked with elevated privileges, for
               example under sudo(8) or pkexec(1), the pager becomes a
               security boundary. Care must be taken that only programs with
               strictly limited functionality are used as pagers, and
               unintended interactive features like opening or creation of
               new files or starting of subprocesses are not allowed. "Secure
               mode" for the pager may be enabled as described below, if the
               pager supports that (most pagers are not written in a way that
               takes this into consideration). It is recommended to either
               explicitly enable "secure mode" or to completely disable the
               pager using --no-pager or PAGER=cat when allowing untrusted
               users to execute commands with elevated privileges.

               This option takes a boolean argument. When set to true, the
               "secure mode" of the pager is enabled. In "secure mode",
               LESSSECURE=1 will be set when invoking the pager, which
               instructs the pager to disable commands that open or create
               new files or start new subprocesses. Currently only less(1) is
               known to understand this variable and implement "secure mode".

               When set to false, no limitation is placed on the pager.
               Setting SYSTEMD_PAGERSECURE=0 or not removing it from the
               inherited environment may allow the user to invoke arbitrary
               commands.

               When $SYSTEMD_PAGERSECURE is not set, systemd tools attempt to
               automatically figure out if "secure mode" should be enabled
               and whether the pager supports it. "Secure mode" is enabled if
               the effective UID is not the same as the owner of the login
               session, see geteuid(2) and sd_pid_get_owner_uid(3), or when
               running under sudo(8) or similar tools ($SUDO_UID is set [3]).
               In those cases, SYSTEMD_PAGERSECURE=1 will be set and pagers
               which are not known to implement "secure mode" will not be
               used at all. Note that this autodetection only covers the most
               common mechanisms to elevate privileges and is intended as
               convenience. It is recommended to explicitly set
               $SYSTEMD_PAGERSECURE or disable the pager.

               Note that if the $SYSTEMD_PAGER or $PAGER variables are to be
               honoured, other than to disable the pager,
               $SYSTEMD_PAGERSECURE must be set too.

           $SYSTEMD_COLORS
               Takes a boolean argument, or a special value. By default
               (unset), systemd and related utilities will use colors in
               their output if possible. If $COLORTERM is set to "truecolor"
               or "24bit", 24-bit colors will be enabled, 256 colors
               otherwise, unless $NO_COLOR or $TERM indicates colors are
               disabled.

               true
                   Same as unset, except that $NO_COLOR is ignored.

               false
                   The output will be monochrome.

               "16", "256", "24bit"
                   Always use the base 16 ANSI colors, 256 colors, or 24 bit
                   color, respectively.

               "auto-16", "auto-256", "auto-24bit"
                   Use the given quantity of colours, subject to $TERM, and
                   what the console is connected to.

           $SYSTEMD_URLIFY
               The value must be a boolean. Controls whether clickable links
               should be generated in the output for terminal emulators
               supporting this. This can be specified to override the
               decision that systemd makes based on $TERM and other
               conditions.

## [](#EXAMPLES)EXAMPLES

           Example 1. Run an Arch Linux VM image generated by mkosi

               $ mkosi -d arch -p systemd -p linux --autologin -o image.raw -f build
               $ systemd-vmspawn --image=image.raw

           Example 2. Import and run a Fedora 44 Cloud image using importctl

               $ curl -L \
                      -O https://download.fedoraproject.org/pub/fedora/linux/releases/44/Cloud/x86_64/images/Fedora-Cloud-Base-Generic-44-1.7.x86_64.qcow2 \
                      -O https://download.fedoraproject.org/pub/fedora/linux/releases/44/Cloud/x86_64/images/Fedora-Cloud-44-1.7-x86_64-CHECKSUM \
                      -O https://fedoraproject.org/fedora.gpg
               $ gpgv --keyring ./fedora.gpg Fedora-Cloud-44-1.7-x86_64-CHECKSUM
               $ sha256sum -c Fedora-Cloud-44-1.7-x86_64-CHECKSUM
               # importctl import-raw -m Fedora-Cloud-Base-Generic-44-1.7.x86_64.qcow2 fedora-44-cloud
               # systemd-vmspawn -M fedora-44-cloud

           Example 3. Build and run systemd's system image and forward the
           VM's journal to a local file

               $ mkosi build
               $ systemd-vmspawn \
                   -D mkosi.output/system \
                   --private-users $(grep $(whoami) /etc/subuid | cut -d: -f2) \
                   --linux mkosi.output/system.efi \
                   --forward-journal=vm.journal \
                   enforcing=0

           Note: this example also uses a kernel command line argument to
           ensure SELinux is not started in enforcing mode.

           Example 4. SSH into a running VM using systemd-ssh-proxy

               $ mkosi build
               $ my_vsock_cid=3735928559
               $ systemd-vmspawn \
                   -D mkosi.output/system \
                   --private-users $(grep $(whoami) /etc/subuid | cut -d: -f2) \
                   --linux mkosi.output/system.efi \
                   --vsock-cid $my_vsock_cid \
                   enforcing=0
               $ ssh root@vsock/$my_vsock_cid -i /run/user/$UID/systemd/vmspawn/machine-*-system-ed25519

## [](#EXIT_STATUS)EXIT STATUS

           If an error occurred the value errno is propagated to the return
           code. If EXIT_STATUS is supplied by the running image that is
           returned. Otherwise, EXIT_SUCCESS is returned.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), mkosi(1), machinectl(1), importctl(1), UAPI.1 Boot
           Loader Specification[1]

## [](#NOTES)NOTES

            1. UAPI.1 Boot Loader Specification
               https://uapi-group.org/specifications/specs/boot_loader_specification

            2. ANSI Escape Code (Wikipedia)
               https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters

            3. It is recommended for other tools to set and check $SUDO_UID
               as appropriate, treating it is a common interface.

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

    systemd 262~devel                                      SYSTEMD-VMSPAWN(1)

------------------------------------------------------------------------

Pages that refer to this page: [importctl(1)](../man1/importctl.1.html),  [machinectl(1)](../man1/machinectl.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-import-generator(8)](../man8/systemd-import-generator.8.html)

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
