---
{"title": "systemd-stub(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/linuxia32.efi.stub.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-stub(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMPANION FILES](#COMPANION_FILES) \| [MULTI-PROFILE UKIS](#MULTI-PROFILE_UKIS) \| [TPM PCR NOTES](#TPM_PCR_NOTES) \| [EFI VARIABLES](#EFI_VARIABLES) \| [INITRD RESOURCES](#INITRD_RESOURCES) \| [SMBIOS TYPE 11 STRINGS](#SMBIOS_TYPE_11_STRINGS) \| [ASSEMBLING KERNEL IMAGES](#ASSEMBLING_KERNEL_IMAGES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-STUB(7)                systemd-stub               SYSTEMD-STUB(7)

## [](#NAME)NAME

           systemd-stub, sd-stub, linuxx64.efi.stub, linuxia32.efi.stub,
           linuxaa64.efi.stub - A simple UEFI kernel boot stub

## [](#SYNOPSIS)SYNOPSIS

               /usr/lib/systemd/boot/efi/linuxx64.efi.stub
               /usr/lib/systemd/boot/efi/linuxia32.efi.stub
               /usr/lib/systemd/boot/efi/linuxaa64.efi.stub
               ESP/.../foo.efi.extra.d/*.addon.efi
               ESP/.../foo.efi.extra.d/*.cred
               ESP/.../foo.efi.extra.d/*.raw
               ESP/.../foo.efi.extra.d/*.sysext.raw
               ESP/.../foo.efi.extra.d/*.confext.raw
               ESP/loader/addons/*.addon.efi
               ESP/loader/credentials/*.cred
               ESP/loader/extensions/*.raw
               ESP/loader/extensions/*.sysext.raw
               ESP/loader/extensions/*.confext.raw

## [](#DESCRIPTION)DESCRIPTION

           systemd-stub (stored in per-architecture files linuxx64.efi.stub,
           linuxia32.efi.stub, linuxaa64.efi.stub on disk) is a simple UEFI
           boot stub. An UEFI boot stub is attached to a Linux kernel binary
           image, and is a piece of code that runs in the UEFI firmware
           environment before transitioning into the Linux kernel
           environment. The UEFI boot stub ensures a Linux kernel is
           executable as regular UEFI binary, and is able to do various
           preparations before switching the system into the Linux world.

           The UEFI boot stub looks for various resources for the kernel
           invocation inside the UEFI PE binary itself. This allows combining
           various resources inside a single PE binary image (a "Unified
           Kernel Image" or "UKI" for short), which may then be signed via
           UEFI SecureBoot as a whole, covering all individual resources at
           once. Specifically it may include the following PE sections:

           •   A ".linux" section with the ELF Linux kernel image. This
               section is required.

           •   An optional ".osrel" section with OS release information, i.e.
               the contents of the os-release(5) file of the OS the kernel
               belongs to.

           •   An optional ".cmdline" section with the kernel command line to
               pass to the invoked kernel.

           •   An optional ".initrd" section with the initrd.

           •   An optional ".ucode" section with an initrd containing
               microcode, to be handed to the kernel before any other initrd.
               This initrd must not be compressed.

           •   An optional ".splash" section with an image (in the Windows
               .BMP format) to show on screen before invoking the kernel.

           •   An optional ".dtb" section with a compiled binary DeviceTree.

           •   Zero or more ".dtbauto" sections.  systemd-stub will always
               use the first matching one. The match is performed by taking
               the first DeviceTree's "compatible" string supplied by the
               firmware in configuration tables and comparing it with the
               first "compatible" string from each of the ".dtbauto"
               sections. If the firmware does not provide a DeviceTree, the
               match is done using the ".hwids" section instead. After
               selecting the matching entry in the ".hwids" section (see the
               description below), the "compatible" string from that entry
               will be used to perform the same matching procedure. If a
               match is found, that ".dtbauto" section will be loaded and
               will override ".dtb" if present.

           •   Zero or more ".efifw" sections for the firmware image. It
               works in many ways similar to ".dtbauto" sections.
               systemd-stub will always use the first matching one. The match
               is performed by first selecting the most appropriate entry in
               the ".hwids" section based on the hardware IDs supplied by
               SMBIOS (see below). If a suitable entry is found, the "fwid"
               string from that entry will be used to perform the matching
               procedure for firmware blobs in ".efifw" section. The first
               matching firmware will be loaded.

           •   An optional ".hwids" section with hardware IDs of the machines
               to match DeviceTrees.  systemd-stub will use the SMBIOS data
               to calculate hardware IDs of the machine (as per
               specification[1]), and then it will try to find any of them in
               the ".hwids" section. The first matching entry will be used.

           •   An optional ".uname" section with the kernel version
               information, i.e. the output of uname -r for the kernel
               included in the ".linux" section.

           •   An optional ".sbat" section with SBAT[2] revocation metadata.

           •   An optional ".pcrsig" section with a set of cryptographic
               signatures for the expected TPM2 PCR values after the kernel
               has been booted, in JSON format. This is useful for
               implementing TPM2 policies that bind disk encryption and
               similar to kernels that are signed by a specific key.

           •   An optional ".pcrpkey" section with a public key in the PEM
               format matching the signature data in the ".pcrsig" section.

           In a basic UKI, the sections listed above appear at most once,
           with the exception of ".dtbauto" and ".efifw" sections. In a
           multi-profile UKI, multiple sets of these sections are present in
           a single file and form "profiles", one of which can be selected at
           boot. For this, the PE section ".profile" is defined to be used as
           the separator between sets of sections. The ".profile" section
           itself may contain meta-information about the section, and follows
           a similar structure as the contents of the ".osrel" section. For
           further details about multi-profile UKIs, see below.

           If UEFI SecureBoot is enabled and the ".cmdline" section is
           present in the executed image, any attempts to override the kernel
           command line by passing one as invocation parameters to the EFI
           binary are ignored. Thus, in order to allow overriding the kernel
           command line, either disable UEFI SecureBoot, or do not include a
           kernel command line PE section in the kernel image file. If a
           command line is accepted via EFI invocation parameters to the EFI
           binary it is measured into TPM PCR 12 (if a TPM is present).

           If a DeviceTree is embedded in the ".dtb" section, it replaces an
           existing DeviceTree in the corresponding EFI configuration table.
           systemd-stub will ask the firmware via the "EFI_DT_FIXUP_PROTOCOL"
           for hardware specific fixups to the DeviceTree.

           The contents of 11 of these 12 sections are measured into TPM PCR
           11. It is otherwise not used and thus the result can be
           pre-calculated without too much effort. The ".pcrsig" section is
           not included in this PCR measurement, since it is supposed to
           contain signatures for the output of the measurement operation,
           and thus cannot also be input to it. If an UKI contains multiple
           profiles, only the PE sections of the selected profile (and those
           of the base profile, except if overridden) are measured.

           If non-zero, the selected numeric profile is measured into PCR 12.

           When ".pcrsig" and/or ".pcrpkey" sections are present in a unified
           kernel image their contents are passed to the booted kernel in an
           synthetic initrd cpio archive that places them in the
           /.extra/tpm2-pcr-signature.json and
           /.extra/tpm2-pcr-public-key.pem files. Typically, a tmpfiles.d(5)
           line then ensures they are copied into
           /run/systemd/tpm2-pcr-signature.json and
           /run/systemd/tpm2-pcr-public-key.pem where they remain accessible
           even after the system transitions out of the initrd environment
           into the host file system. Tools such
           systemd-cryptsetup@.service(8), systemd-cryptenroll(1) and
           systemd-creds(1) will automatically use files present under these
           paths to unlock protected resources (encrypted storage or
           credentials) or bind encryption to booted kernels.

           For further details about the UKI concept, see the UAPI.5 UKI
           specification[3].

## [](#COMPANION_FILES)COMPANION FILES

           The systemd-stub UEFI boot stub automatically collects three types
           of auxiliary companion files optionally placed in drop-in
           directories on the same partition as the EFI binary, dynamically
           generates cpio initrd archives from them, and passes them to the
           kernel. Specifically:

           •   For a kernel binary called foo.efi, it will look for files
               with the .cred suffix in a directory named foo.efi.extra.d/
               next to it. If the kernel binary uses a counter for the
               purpose of Automatic Boot Assessment[4], this counter will be
               ignored. For example, foo+3-0.efi will look in directory
               foo.efi.extra.d/. A cpio archive is generated from all files
               found that way, placing them in the /.extra/credentials/
               directory of the initrd file hierarchy. The main initrd may
               then access them in this directory. This is supposed to be
               used to store auxiliary, encrypted, authenticated credentials
               for use with LoadCredentialEncrypted in the UEFI System
               Partition. See systemd.exec(5) and systemd-creds(1) for
               details on encrypted credentials. The generated cpio archive
               is measured into TPM PCR 12 (if a TPM is present).

           •   Similarly, files foo.efi.extra.d/*.sysext.raw are packed up in
               a cpio archive and placed in the /.extra/sysext/ directory in
               the initrd file hierarchy. This is supposed to be used to pass
               additional UKI-specific system extension images to the initrd.
               See systemd-sysext(8) for details on system extension images.
               The generated cpio archive containing these system extension
               images is measured into TPM PCR 13 (if a TPM is present).

           •   Similarly, files /loader/extensions/*.sysext.raw are packed up
               in a cpio archive and placed in the /.extra/global_sysext/
               directory in the initrd file hierarchy. This is supposed to be
               used to pass additional global system extension images to the
               initrd. See systemd-sysext(8) for details on system extension
               images. The generated cpio archive containing these system
               extension images is measured into TPM PCR 13 (if a TPM is
               present).

           •   Similarly, files foo.efi.extra.d/*.confext.raw are packed up
               in a cpio archive and placed in the /.extra/confext/ directory
               in the initrd file hierarchy. This is supposed to be used to
               pass additional UKI-specific configuration extension images to
               the initrd. See systemd-confext(8) for details on
               configuration extension images. The generated cpio archive
               containing these configuration extension images is measured
               into TPM PCR 12 (if a TPM is present).

           •   Similarly, files /loader/extensions/*.confext.raw are packed
               up in a cpio archive and placed in the /.extra/global_confext/
               directory in the initrd file hierarchy. This is supposed to be
               used to pass additional global configuration extension images
               to the initrd. See systemd-confext(8) for details on
               configuration extension images. The generated cpio archive
               containing these configuration extension images is measured
               into TPM PCR 12 (if a TPM is present).

           •   Similarly, files foo.efi.extra.d/*.addon.efi are loaded and
               verified as PE binaries and specific sections are loaded from
               them. Addons are used to pass additional kernel command line
               parameters (".cmdline" section), or DeviceTree blobs (".dtb"
               section), additional initrds (".initrd" section), and
               microcode updates (".ucode" section). Addons allow those
               resources to be passed regardless of the kernel version being
               booted, for example allowing platform vendors to ship
               platform-specific configuration.

               In case Secure Boot is enabled, these files will be validated
               using keys in UEFI DB, Shim's DB or Shim's MOK, and only
               loaded if the check passes. Additionally, if both the addon
               and the UKI contain a ".uname" section, the addon will be
               rejected if they do not match exactly. It is recommended to
               always add a ".sbat" section to all signed addons, so that
               they may be revoked with a SBAT policy update, without
               requiring blocklisting via DBX/MOKX. The ukify(1) tool will
               add a SBAT policy by default if none is passed when building
               addons. For more information on SBAT see Shim
               documentation[2].

               Addon files are sorted, loaded, and measured into TPM PCR 12
               (if a TPM is present) and appended to the kernel command line.
               UKI command line options are listed first, then options from
               addons in /loader/addons/*.addon.efi, and finally UKI-specific
               addons. Device tree blobs are loaded and measured following
               the same algorithm. Microcode addons are passed to the kernel
               in inverse order (UKI specific addons, global addons, UKI
               embedded section). This is because the microcode update driver
               stops on the first matching filename. Addons are always loaded
               in the same order based on the filename, so that, given the
               same set of addons, the same set of measurements can be
               expected in PCR12. However, note that the filename is not
               protected by the PE signature, and as such an attacker with
               write access to the ESP could potentially rename these files
               to change the order in which they are loaded, in a way that
               could alter the functionality of the kernel, as some options
               might be order-dependent. If you sign such addons, you should
               pay attention to the PCR12 values and make use of an
               attestation service so that improper use of your signed addons
               can be detected and dealt with using one of the aforementioned
               revocation mechanisms.

           •   Files /loader/credentials/*.cred are packed up in a cpio
               archive and placed in the /.extra/global_credentials/
               directory of the initrd file hierarchy. This is supposed to be
               used to pass additional credentials to the initrd, regardless
               of the kernel version being booted. The generated cpio archive
               is measured into TPM PCR 12 (if a TPM is present).

           •   Additionally, files /loader/addons/*.addon.efi are loaded and
               verified as PE binaries, and ".cmdline", ".dtb", ".initrd",
               and ".ucode" sections are parsed from them. This is supposed
               to be used to pass additional command line parameters,
               DeviceTree blobs, initrds, and microcode updates to the
               kernel, regardless of the kernel version being booted.

           These mechanisms may be used to parameterize and extend trusted
           (i.e. signed), immutable initrd images in a reasonably safe way:
           all data they contain is measured into TPM PCRs. On access they
           should be further validated: in case of the credentials case by
           encrypting/authenticating them via TPM, as exposed by
           systemd-creds encrypt -T (see systemd-creds(1) for details); in
           case of the system extension images by using signed Verity images.

           Note that earlier components of the boot process might register
           additional initrds, and thus additional "companion" resources such
           as system extensions, configuration extensions and credentials for
           consumption by the kernel and OS eventually booted. For example,
           systemd-boot(7) does this for resources configured in UAPI.1 Type
           #1 "extra" lines.  systemd-stub will combine any resources
           provided that way with the companion file resources it acquires
           itself.

## [](#MULTI-PROFILE_UKIS)MULTI-PROFILE UKIS

           In many contexts it is useful to allow invocation of a single UKI
           in multiple different modes (or "profiles") without compromising
           the cryptographic integrity, measurements and so on of the boot
           process. For example, a single UKI might provide three distinct
           profiles: a regular boot one, one that invokes a "factory reset"
           operation, and one that boots into a storage target mode (as in
           systemd-storagetm.service(8)). Each profile would then use the
           same ".linux" and ".initrd" sections, but would have a separate
           ".cmdline" section. For example the latter two profiles would
           extend the regular kernel command line with
           "systemd.unit=factory-reset.target" or
           "rd.systemd.unit=storagetm.target".

           A single UKI may support multiple profiles by means of the special
           ".profile" PE section. This section acts as separator between the
           PE sections of the individual profiles.  ".profile" PE sections
           hence may appear multiple times in a single UKI, and the other PE
           sections listed above may appear multiple times too, if ".profile"
           are used, but only once before the first ".profile" section, once
           between each subsequent pair, and once after the last appearance
           of ".profile". The sections listed before the first ".profile" are
           considered the "base" profile of the UKI. Each ".profile" section
           then introduces a new profile, which are numbered starting from
           zero. The PE sections following each ".profile" are specific to
           that profile. When booting into a specific profile, the base
           section's profiles are used in combination with the specific
           profile's sections: if the same section is defined in both, the
           per-profile section overrides the base profile's version,
           otherwise the base profile sections are used.

           A UKI that contains no ".profile" is consider equivalent to one
           that just contains a single ".profile", as having only a single
           profile "@0".

           Here's a simple example for a multi-profile UKI's sections,
           inspired by the setup suggested above:

           Table 1. Multi-Profile UKI Example
           ┌────────────┬──────────────┐
           │ Section    │ Profile      │
           ├────────────┼──────────────┤
           │ ".linux"   │              │
           ├────────────┤              │
           │ ".osrel"   │              │
           ├────────────┤ Base profile │
           │ ".cmdline" │              │
           ├────────────┤              │
           │ ".initrd"  │              │
           ├────────────┼──────────────┤
           │ ".profile" │ Profile @0   │
           ├────────────┼──────────────┤
           │ ".profile" │              │
           ├────────────┤ Profile @1   │
           │ ".cmdline" │              │
           ├────────────┼──────────────┤
           │ ".profile" │              │
           ├────────────┤ Profile @2   │
           │ ".cmdline" │              │
           └────────────┴──────────────┘

           The section list above would define three profiles. The first four
           sections make up the base profile. A ".profile" section then
           introduces profile @0. It does not override any sections (or add
           any) from the base section, hence it is immediately followed by
           another ".profile" section that then introduces section @1. This
           profile overrides the kernel command line. Finally, the last two
           sections define section @2, again overriding the command line.
           (Note that in this example the first ".cmdline" could also moved
           behind the first ".profile" with equivalent effect. To keep things
           nicely extensible, it is probably a good idea to keep the generic
           command line in the base section instead of profile 0, in case
           later added profiles might want to reuse it.)

           The profile to boot may be controlled via the UKI's own command
           line: if the first argument starts with "@", followed by a
           positive integer number in decimal, it selects the profile to boot
           into. If the first argument is not specified like that, the UKI
           will automatically boot into profile 0.

           A ".profile" section may contain meta-information about the
           profile. It follows a similar format as ".osrel" (i.e. an
           environment-variable-assignment-block-like list of newline
           separated strings). Currently two fields are defined: "ID=" is
           supposed to carry a short identifying string that identifies the
           profile (e.g.  "ID=factory-reset").  "TITLE=" should contain a
           human-readable string that may appear in the boot menu entry for
           this profile (e.g.  "TITLE='Factory Reset this Device'").

## [](#TPM_PCR_NOTES)TPM PCR NOTES

           Note that when a unified kernel using systemd-stub is invoked the
           firmware will measure it as a whole to TPM PCR 4, covering all
           embedded resources, such as the stub code itself, the core kernel,
           the embedded initrd and kernel command line (see above for a full
           list), including all UKI profiles.

           Also note that when systemd-stub measures a PE section, it will
           measure the amount of bytes that the section takes up in memory
           (VirtualSize) and not the amount of bytes that the section takes
           up on disk (SizeOfRawData). This means that if the size in memory
           is larger than the size on disk, systemd-stub will end up
           measuring extra zeroes. To avoid this from happening, it is
           recommended to make sure that the size in memory of each section
           that is measured by systemd-stub is always smaller than or equal
           to the size on disk.  ukify automatically makes sure this is the
           case when building UKIs or addons.

           Also note that the Linux kernel will measure all initrds it
           receives into TPM PCR 9. This means every type of initrd (of the
           selected UKI profile) will possibly be measured two or three
           times: the initrds embedded in the kernel image will be measured
           to PCR 4, PCR 9 and PCR 11; the initrd synthesized from
           credentials (and the one synthesized from configuration
           extensions) will be measured to both PCR 9 and PCR 12; the initrd
           synthesized from system extensions will be measured to both PCR 4
           and PCR 9. Let's summarize the OS resources and the PCRs they are
           measured to:

           Table 2. OS Resource PCR Summary
           ┌──────────────────────────┬─────────────────┐
           │ OS Resource              │ Measurement PCR │
           ├──────────────────────────┼─────────────────┤
           │ systemd-stub code (the   │ 4               │
           │ entry point of the       │                 │
           │ unified PE binary)       │                 │
           ├──────────────────────────┼─────────────────┤
           │ Core kernel code         │ 4 + 11          │
           │ (embedded in unified PE  │                 │
           │ binary)                  │                 │
           ├──────────────────────────┼─────────────────┤
           │ OS release information   │ 4 + 11          │
           │ (embedded in the unified │                 │
           │ PE binary)               │                 │
           ├──────────────────────────┼─────────────────┤
           │ Main initrd (embedded in │ 4 + 9 + 11      │
           │ unified PE binary)       │                 │
           ├──────────────────────────┼─────────────────┤
           │ Microcode initrd         │ 4 + 9 + 11      │
           │ (embedded in unified PE  │                 │
           │ binary)                  │                 │
           ├──────────────────────────┼─────────────────┤
           │ Default kernel command   │ 4 + 11          │
           │ line (embedded in        │                 │
           │ unified PE binary)       │                 │
           ├──────────────────────────┼─────────────────┤
           │ Overridden kernel        │ 12              │
           │ command line             │                 │
           ├──────────────────────────┼─────────────────┤
           │ Boot splash (embedded in │ 4 + 11          │
           │ the unified PE binary)   │                 │
           ├──────────────────────────┼─────────────────┤
           │ TPM2 PCR signature JSON  │ 4 + 9           │
           │ (embedded in unified PE  │                 │
           │ binary, synthesized into │                 │
           │ initrd)                  │                 │
           ├──────────────────────────┼─────────────────┤
           │ TPM2 PCR PEM public key  │ 4 + 9 + 11      │
           │ (embedded in unified PE  │                 │
           │ binary, synthesized into │                 │
           │ initrd)                  │                 │
           ├──────────────────────────┼─────────────────┤
           │ Credentials (synthesized │ 9 + 12          │
           │ initrd from companion    │                 │
           │ files)                   │                 │
           ├──────────────────────────┼─────────────────┤
           │ System Extensions        │ 9 + 13          │
           │ (synthesized initrd from │                 │
           │ companion files)         │                 │
           ├──────────────────────────┼─────────────────┤
           │ Configuration Extensions │ 9 + 12          │
           │ (synthesized initrd from │                 │
           │ companion files)         │                 │
           ├──────────────────────────┼─────────────────┤
           │ Selected profile unless  │ 12              │
           │ zero                     │                 │
           └──────────────────────────┴─────────────────┘

## [](#EFI_VARIABLES)EFI VARIABLES

           The following EFI variables are defined, set and read by
           systemd-stub, under the vendor UUID
           "4a67b082-0a4c-41cf-b6c7-440b29bb8c4f", for communication between
           the boot stub and the OS:

           LoaderDevicePartUUID
               Contains the partition UUID of the partition the boot loader
               has been started from on the current boot (usually a EFI
               System Partition). If already set by the boot loader, this
               will remain untouched by systemd-stub. If not set yet, this
               will be set to the partition UUID of the partition the unified
               kernel is started from, in order to support systems that
               directly boot into a unified kernel image, bypassing any boot
               loader.  systemd-gpt-auto-generator(8) uses this information
               to automatically find the disk booted from, in order to
               discover various other partitions on the same disk
               automatically.

               Added in version 224.

           LoaderFirmwareInfo, LoaderFirmwareType
               Brief firmware information. Use bootctl(1) to view this data.

               Added in version 250.

           LoaderTpm2ActivePcrBanks
               Hexadecimal string representation of a bitmask with values
               defined by the TCG EFI Protocol Specification for TPM 2.0 as
               EFI_TCG2_BOOT_HASH_ALG_*. If no TPM2 support or no active
               banks were detected, will be set to 0. Set by the boot loader.
               Use systemd-analyze(1) to view this data.

               Added in version 258.

           LoaderImageIdentifier
               The file system path to the EFI executable of the boot loader
               for the current boot, relative to the partition's root
               directory (i.e. relative to the partition indicated by
               LoaderDevicePartUUID, see above). If not set yet, this will be
               set to the file system path of the EFI executable of the
               booted unified kernel, in order to support systems that
               directly boot into a unified kernel image, bypassing any boot
               loader. Use bootctl(1) to view this data.

               Added in version 237.

           StubDevicePartUUID, StubImageIdentifier
               Similar to LoaderDevicePartUUID and LoaderImageIdentifier, but
               indicates the location of the unified kernel image EFI binary
               rather than the location of the boot loader binary, regardless
               of whether booted via a boot loader or not.

               Added in version 257.

           StubDeviceURL
               If the kernel image has been invoked via network booting this
               variable contains the originating URL. This may be used to
               automatically acquire additional resources from the same
               source.

               Added in version 258.

           StubInfo
               Brief stub information. Use bootctl(1) to view this data.

               Added in version 250.

           StubPcrKernelImage
               The PCR register index the kernel image, initrd image, boot
               splash, devicetree database, and the embedded command line are
               measured into, formatted as decimal ASCII string (e.g.  "11").
               This variable is set if a measurement was successfully
               completed, and remains unset otherwise.

               Added in version 252.

           StubPcrKernelParameters
               The PCR register index the kernel command line and credentials
               are measured into, formatted as decimal ASCII string (e.g.
               "12"). This variable is set if a measurement was successfully
               completed, and remains unset otherwise.

               Added in version 252.

           StubPcrInitRDSysExts
               The PCR register index the system extensions for the initrd,
               which are picked up from the file system the kernel image is
               located on. Formatted as decimal ASCII string (e.g.  "13").
               This variable is set if a measurement was successfully
               completed, and remains unset otherwise.

               Added in version 252.

           StubPcrInitRDConfExts
               The PCR register index the configuration extensions for the
               initrd, which are picked up from the file system the kernel
               image is located on. Formatted as decimal ASCII string (e.g.
               "12"). This variable is set if a measurement was successfully
               completed, and remains unset otherwise.

               Added in version 255.

           StubProfile
               The numeric index of the selected profile, without the "@",
               formatted as decimal string. Set both on single-profile and
               multi-profile UKIs. (In the former case this variable will be
               set to "0" unconditionally.)

               Added in version 257.

           LoaderPcrSMBIOS
               The PCR register index select SMBIOS structures are measured
               into — type 1 (system information, with the volatile "Wake-up
               Type" field zeroed out), type 2 (baseboard information) and
               type 11 (OEM strings). Formatted as decimal ASCII string (e.g.
               "1"). This variable is set if a measurement was successfully
               completed, and remains unset otherwise.  systemd-stub performs
               this measurement only if it has not already been done in the
               same boot (e.g. by the boot loader), as indicated by this
               variable being set already.

               Added in version 261.

           LoaderBootSecret
               A non-volatile EFI variable only accessible from the pre-boot
               environment (i.e. access from the OS is not permitted) that
               contains a per-system secret. It is set automatically by
               systemd-stub if not present already. A secret derived from the
               value of this EFI variable is passed to the OS in
               /.extra/boot-secret, see below.

               Added in version 261.

           Note that some of the variables above may also be set by the boot
           loader. The stub will only set them if they are not set already.
           Some of these variables are defined by the Boot Loader
           Interface[5].

## [](#INITRD_RESOURCES)INITRD RESOURCES

           The following resources are passed as initrd cpio archives to the
           booted kernel, and thus make up the initial file system hierarchy
           in the initrd execution environment:

           /
               The main initrd from the ".initrd" PE section of the unified
               kernel image.

               Added in version 252.

           /.extra/credentials/*.cred
               Credential files (suffix ".cred") that are placed next to the
               unified kernel image (as described above) are copied into the
               /.extra/credentials/ directory in the initrd execution
               environment.

               Added in version 252.

           /.extra/global_credentials/*.cred
               Similarly, credential files in the /loader/credentials/
               directory in the file system the unified kernel image is
               placed in are copied into the /.extra/global_credentials/
               directory in the initrd execution environment.

               Added in version 252.

           /.extra/sysext/*.sysext.raw
               System extension image files (suffix ".sysext.raw") that are
               placed next to the unified kernel image (as described above)
               are copied into the /.extra/sysext/ directory in the initrd
               execution environment.

               Added in version 252.

           /.extra/global_sysext/*.sysext.raw
               Similarly, system extension image files (suffix ".sysext.raw")
               that are placed in the /loader/extensions/ directory in the
               file system the unified kernel image is placed in are copied
               into the /.extra/global_sysext/ directory in the initrd
               execution environment.

               Added in version 258.

           /.extra/confext/*.confext.raw
               Configuration extension image files (suffix ".confext.raw")
               that are placed next to the unified kernel image (as described
               above) are copied into the /.extra/confext/ directory in the
               initrd execution environment.

               Added in version 255.

           /.extra/global_confext/*.confext.raw
               Similarly, configuration extension image files (suffix
               ".confext.raw") that are placed in the /loader/extensions/
               directory in the file system the unified kernel image is
               placed in are copied into the /.extra/global_confext/
               directory in the initrd execution environment.

               Added in version 258.

           /.extra/tpm2-pcr-signature.json
               The TPM2 PCR signature JSON object included in the ".pcrsig"
               PE section of the unified kernel image is copied into the
               /.extra/tpm2-pcr-signature.json file in the initrd execution
               environment.

               Added in version 252.

           /.extra/tpm2-pcr-public-key.pem
               The PEM public key included in the ".pcrpkey" PE section of
               the unified kernel image is copied into the
               /.extra/tpm2-pcr-public-key.pem file in the initrd execution
               environment.

               Added in version 252.

           /.extra/profile, /.extra/os-release
               The contents of the ".profile" and ".osrel" sections of the
               selected profile, if any.

               Added in version 257.

           /.extra/boot-secret
               A 32 byte per-system secret which is derived from a 32 byte
               secret stored in an EFI variable (LoaderBootSecret, see
               above), which itself is only accessible to the pre-boot
               environment. This may be used for various early-boot
               cryptographic purposes, and OS file system access to it is
               restricted to root. The IMAGE_ID=/ID= data from the ".osrel"
               is hashed into the secret, to ensure that different images get
               a distinct secret passed. Moreover, a randomized 32 byte value
               stored in the ESP in the "/loader/boot-secret-mixin" file is
               hashed in as well, ensuring that distinct disks will result in
               different boot secrets.

               Note: this boot secret is ultimately protected only by
               firmware-enforced access controls on the EFI variable. This is
               generally a much weaker protection than TPM-based approaches
               have, and it is hence strongly recommended to use the TPM on
               systems that possess one. The boot secret is primarily
               intended to be a lower-security fallback for cases where a TPM
               is not available.

               Applications should never protect resources directly with this
               secret, but derive their own secret from it (by hashing it
               together with some application ID, in HMAC mode for example),
               in order not to accidentally leak the primary boot secret.

               Note that the boot secret is only available if the pre-boot
               environment had a suitable RNG source at the current boot or
               an earlier one. This source can be an initialized on-disk
               random seed or the EFI RNG support, or both.

               Added in version 261.

           Note that all these files are located in the "tmpfs" file system
           the kernel sets up for the initrd file hierarchy and are thus lost
           when the system transitions from the initrd execution environment
           into the host file system. If these resources shall be kept around
           over this transition they need to be copied to a place that
           survives the transition first, for example via a suitable
           tmpfiles.d(5) line. By default, this is done for the TPM2 PCR
           signature and public key files.

## [](#SMBIOS_TYPE_11_STRINGS)SMBIOS TYPE 11 STRINGS

           systemd-stub can be configured using SMBIOS Type 11 strings.
           Applicable strings consist of a name, followed by "=", followed by
           the value. Unless systemd-stub detects it is running inside a
           confidential computing environment, systemd-stub will search the
           table for a string with a specific name, and if found, use its
           value. The following strings are read:

           io.systemd.stub.kernel-cmdline-extra
               If set, the value of this string is added to the list of
               kernel command line arguments that are measured in PCR12 and
               passed to the kernel.

               Added in version 254.

           io.systemd.boot.loglevel
               If set, the value of this string is used as log level. Valid
               values (from most to least critical) are "emerg", "alert",
               "crit", "err", "warning", "notice", "info", and "debug".

               Added in version 261.

## [](#ASSEMBLING_KERNEL_IMAGES)ASSEMBLING KERNEL IMAGES

           In order to assemble a bootable Unified Kernel Image from various
           components as described above, use ukify(1).

## [](#SEE_ALSO)SEE ALSO

           systemd-boot(7), systemd.exec(5), systemd-creds(1),
           systemd-sysext(8), UAPI.1 Boot Loader Specification[6], Boot
           Loader Interface[5], ukify(1), systemd-measure(1), TPM2 PCR
           Measurements Made by systemd[7]

## [](#NOTES)NOTES

            1. specification
               https://learn.microsoft.com/en-us/windows-hardware/drivers/install/specifying-hardware-ids-for-a-computer

            2. SBAT
               https://github.com/rhboot/shim/blob/main/SBAT.md

            3. UAPI.5 UKI specification
               https://uapi-group.org/specifications/specs/unified_kernel_image/

            4. Automatic Boot Assessment
               https://systemd.io/AUTOMATIC_BOOT_ASSESSMENT

            5. Boot Loader Interface
               https://systemd.io/BOOT_LOADER_INTERFACE

            6. UAPI.1 Boot Loader Specification
               https://uapi-group.org/specifications/specs/boot_loader_specification

            7. TPM2 PCR Measurements Made by systemd
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

    systemd 262~devel                                         SYSTEMD-STUB(7)

------------------------------------------------------------------------

Pages that refer to this page: [systemd(1)](../man1/systemd.1.html),  [systemd-cryptenroll(1)](../man1/systemd-cryptenroll.1.html),  [systemd-measure(1)](../man1/systemd-measure.1.html),  [ukify(1)](../man1/ukify.1.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [smbios-type-11(7)](../man7/smbios-type-11.7.html),  [systemd-boot(7)](../man7/systemd-boot.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-boot-random-seed.service(8)](../man8/systemd-boot-random-seed.service.8.html),  [systemd-gpt-auto-generator(8)](../man8/systemd-gpt-auto-generator.8.html),  [systemd-pcrlock(8)](../man8/systemd-pcrlock.8.html),  [systemd-pcrphase.service(8)](../man8/systemd-pcrphase.service.8.html),  [systemd-random-seed.service(8)](../man8/systemd-random-seed.service.8.html),  [systemd-sysext(8)](../man8/systemd-sysext.8.html),  [systemd-tpm2-swtpm.service(8)](../man8/systemd-tpm2-swtpm.service.8.html)

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
