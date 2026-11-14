---
{"title": "systemd-detect-virt(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-detect-virt.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-detect-virt(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-DETECT-VIRT(1)     systemd-detect-virt     SYSTEMD-DETECT-VIRT(1)

## [](#NAME)NAME

           systemd-detect-virt - Detect execution in a virtualized
           environment

## [](#SYNOPSIS)SYNOPSIS

           systemd-detect-virt [OPTIONS...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-detect-virt detects execution in a virtualized
           environment. It identifies the virtualization technology and can
           distinguish full machine virtualization from container
           virtualization.  systemd-detect-virt exits with a return value of
           0 (success) if a virtualization technology is detected, and
           non-zero (error) otherwise. By default, any type of virtualization
           is detected, and the options --container and --vm can be used to
           limit what types of virtualization are detected.

           When executed without --quiet will print a short identifier for
           the detected virtualization technology. The following technologies
           are currently identified:

           Table 1. Known virtualization technologies (both VM, i.e. full
           hardware virtualization, and container, i.e. shared kernel
           virtualization)
           ┌───────────┬────────────────┬────────────────────┐
           │ Type      │ ID             │ Product            │
           ├───────────┼────────────────┼────────────────────┤
           │ VM        │ qemu           │ QEMU software      │
           │           │                │ virtualization,    │
           │           │                │ without KVM        │
           │           ├────────────────┼────────────────────┤
           │           │ kvm            │ Linux KVM kernel   │
           │           │                │ virtual machine,   │
           │           │                │ in combination     │
           │           │                │ with QEMU. Not     │
           │           │                │ used for other     │
           │           │                │ virtualizers using │
           │           │                │ the KVM            │
           │           │                │ interfaces, such   │
           │           │                │ as Oracle          │
           │           │                │ VirtualBox or      │
           │           │                │ Amazon EC2 Nitro,  │
           │           │                │ see below.         │
           │           ├────────────────┼────────────────────┤
           │           │ amazon         │ Amazon EC2 Nitro   │
           │           │                │ using Linux KVM    │
           │           ├────────────────┼────────────────────┤
           │           │ zvm            │ s390 z/VM          │
           │           ├────────────────┼────────────────────┤
           │           │ vmware         │ VMware Workstation │
           │           │                │ or Server, and     │
           │           │                │ related products   │
           │           ├────────────────┼────────────────────┤
           │           │ microsoft      │ Hyper-V, also      │
           │           │                │ known as Viridian  │
           │           │                │ or Windows Server  │
           │           │                │ Virtualization     │
           │           ├────────────────┼────────────────────┤
           │           │ oracle         │ Oracle VM          │
           │           │                │ VirtualBox         │
           │           │                │ (historically      │
           │           │                │ marketed by        │
           │           │                │ innotek and Sun    │
           │           │                │ Microsystems), for │
           │           │                │ legacy and KVM     │
           │           │                │ hypervisor         │
           │           ├────────────────┼────────────────────┤
           │           │ powervm        │ IBM PowerVM        │
           │           │                │ hypervisor — comes │
           │           │                │ as firmware with   │
           │           │                │ some IBM POWER     │
           │           │                │ servers            │
           │           ├────────────────┼────────────────────┤
           │           │ xen            │ Xen hypervisor     │
           │           │                │ (only domU, not    │
           │           │                │ dom0)              │
           │           ├────────────────┼────────────────────┤
           │           │ bochs          │ Bochs Emulator     │
           │           ├────────────────┼────────────────────┤
           │           │ uml            │ User-mode Linux    │
           │           ├────────────────┼────────────────────┤
           │           │ parallels      │ Parallels Desktop, │
           │           │                │ Parallels Server   │
           │           ├────────────────┼────────────────────┤
           │           │ bhyve          │ bhyve, FreeBSD     │
           │           │                │ hypervisor         │
           │           ├────────────────┼────────────────────┤
           │           │ qnx            │ QNX hypervisor     │
           │           ├────────────────┼────────────────────┤
           │           │ acrn           │ ACRN hypervisor[1] │
           │           ├────────────────┼────────────────────┤
           │           │ apple          │ Apple              │
           │           │                │ virtualization     │
           │           │                │ framework[2]       │
           │           ├────────────────┼────────────────────┤
           │           │ sre            │ LMHS SRE           │
           │           │                │ hypervisor[3]      │
           │           ├────────────────┼────────────────────┤
           │           │ google         │ Google Compute     │
           │           │                │ Engine[4]          │
           ├───────────┼────────────────┼────────────────────┤
           │ Container │ openvz         │ OpenVZ/Virtuozzo   │
           │           ├────────────────┼────────────────────┤
           │           │ lxc            │ Linux container    │
           │           │                │ implementation by  │
           │           │                │ LXC                │
           │           ├────────────────┼────────────────────┤
           │           │ lxc-libvirt    │ Linux container    │
           │           │                │ implementation by  │
           │           │                │ libvirt            │
           │           ├────────────────┼────────────────────┤
           │           │ systemd-nspawn │ systemd's minimal  │
           │           │                │ container          │
           │           │                │ implementation,    │
           │           │                │ see                │
           │           │                │ systemd-nspawn(1)  │
           │           ├────────────────┼────────────────────┤
           │           │ docker         │ Docker container   │
           │           │                │ manager            │
           │           ├────────────────┼────────────────────┤
           │           │ podman         │ Podman[5]          │
           │           │                │ container manager  │
           │           ├────────────────┼────────────────────┤
           │           │ rkt            │ rkt app container  │
           │           │                │ runtime            │
           │           ├────────────────┼────────────────────┤
           │           │ wsl            │ Windows Subsystem  │
           │           │                │ for Linux[6]       │
           │           ├────────────────┼────────────────────┤
           │           │ proot          │ proot[7] userspace │
           │           │                │ chroot/bind mount  │
           │           │                │ emulation          │
           │           ├────────────────┼────────────────────┤
           │           │ pouch          │ Pouch[8] Container │
           │           │                │ Engine             │
           └───────────┴────────────────┴────────────────────┘

           If multiple virtualization solutions are used, only the
           "innermost" is detected and identified. That means if both machine
           and container virtualization are used in conjunction, only the
           latter will be identified (unless --vm is passed).

           Windows Subsystem for Linux is not a Linux container, but an
           environment for running Linux userspace applications on top of the
           Windows kernel using a Linux-compatible interface. WSL is
           categorized as a container for practical purposes. Multiple WSL
           environments share the same kernel and services should generally
           behave like when being run in a container.

           When executed with --cvm, instead of printing the virtualization
           technology, it will display the confidential virtual machine
           technology, if any. The following technologies are currently
           identified:

           Table 2. Known confidential virtualization technologies
           ┌────────┬──────────┬────────────────────┐
           │ Arch   │ ID       │ Technology         │
           ├────────┼──────────┼────────────────────┤
           │ x86_64 │ sev      │ AMD Secure         │
           │        │          │ Encrypted          │
           │        │          │ Virtualization     │
           │        ├──────────┼────────────────────┤
           │        │ sev-es   │ AMD Secure         │
           │        │          │ Encrypted          │
           │        │          │ Virtualization -   │
           │        │          │ Encrypted State    │
           │        ├──────────┼────────────────────┤
           │        │ sev-snp  │ AMD Secure         │
           │        │          │ Encrypted          │
           │        │          │ Virtualization -   │
           │        │          │ Secure Nested      │
           │        │          │ Paging             │
           │        ├──────────┼────────────────────┤
           │        │ tdx      │ Intel Trust Domain │
           │        │          │ Extensions         │
           ├────────┼──────────┼────────────────────┤
           │ s390x  │ protvirt │ IBM Protected      │
           │        │          │ Virtualization     │
           │        │          │ (Secure Execution) │
           ├────────┼──────────┼────────────────────┤
           │ arm64  │ cca      │ Arm Confidential   │
           │        │          │ Compute            │
           │        │          │ Architecture       │
           └────────┴──────────┴────────────────────┘

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -c, --container
               Only detects container virtualization (i.e. shared kernel
               virtualization).

           -v, --vm
               Only detects hardware virtualization.

           -r, --chroot
               Detect whether invoked in a chroot(2) environment. In this
               mode, no output is written, but the return value indicates
               whether the process was invoked in a chroot() environment or
               not.

               Added in version 228.

           --private-users
               Detect whether invoked in a user namespace. In this mode, no
               output is written, but the return value indicates whether the
               process was invoked inside of a user namespace or not. See
               user_namespaces(7) for more information.

               Added in version 232.

           --cvm
               Detect whether invoked in a confidential virtual machine. The
               result of this detection may be used to disable features that
               should not be used in confidential VMs. It must not be used to
               release security sensitive information. The latter must only
               be released after attestation of the confidential environment.

               Added in version 254.

           -q, --quiet
               Suppress output of the virtualization technology identifier.

           --list
               Output all currently known and detectable container and VM
               environments.

               Added in version 239.

           --list-cvm
               Output all currently known and detectable confidential
               virtualization technologies.

               Added in version 254.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           If a virtualization technology is detected, 0 is returned, a
           non-zero code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-nspawn(1), chroot(2), namespaces(7)

## [](#NOTES)NOTES

            1. ACRN hypervisor
               https://projectacrn.org

            2. Apple virtualization framework
               https://developer.apple.com/documentation/virtualization

            3. LMHS SRE hypervisor
               https://www.lockheedmartin.com/en-us/products/Hardened-Security-for-Intel-Processors.html

            4. Google Compute Engine
               https://cloud.google.com/compute

            5. Podman
               https://podman.io

            6. Windows Subsystem for Linux
               https://docs.microsoft.com/en-us/windows/wsl/about

            7. proot
               https://proot-me.github.io/

            8. Pouch
               https://github.com/alibaba/pouch

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

    systemd 262~devel                                  SYSTEMD-DETECT-VIRT(1)

------------------------------------------------------------------------

Pages that refer to this page: [org.freedesktop.systemd1(5)](../man5/org.freedesktop.systemd1.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.generator(7)](../man7/systemd.generator.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [udev(7)](../man7/udev.7.html)

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
