---
{"title": "Virtualized Domain Controller Technical Reference Appendix", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/reference/virtual-dc/virtualized-domain-controller-technical-reference-appendix", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Virtualized Domain Controller Technical Reference Appendix

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This topic covers:

-   [Terminology](#BKMK_Terms)

-   [FixVDCPermissions.ps1](#BKMK_FixPDCPerms)

[](#BKMK_Terms)

## Terminology {#BKMK_Terms .heading-anchor}

-   **Snapshot** - The state of a virtual machine at a particular point in time. It is dependent on the chain of previous snapshots taken, on the hardware, and on the virtualization platform.

-   **Clone** - A complete and separate copy of a virtual machine. It is dependent on the virtual hardware (hypervisor).

-   **Full Clone** - A full clone is an independent copy of a virtual machine that shares no resources with the parent virtual machine after the cloning operation. Ongoing operation of a full clone is entirely separate from the parent virtual machine.

-   **Differencing disk** - A copy of a virtual machine that shares virtual disks with the parent virtual machine in an ongoing manner. This usually conserves disk space and allows multiple virtual machines to use the same software installation.

-   **VM Copy**- A file system copy of all the related files and folders of a virtual machine.

-   **VHD File Copy** - A copy of a virtual machine\'s VHD

-   **VM Generation ID** - a 128-bit integer given to the virtual machine by the hypervisor. This ID is stored in memory and reset every time a snapshot is applied. The design uses a hypervisor-agnostic mechanism for surfacing the VM-Generation ID in the virtual machine. The Hyper-V implementation exposes the ID in the ACPI table of the virtual machine.

-   **Import/Export** - A Hyper-V feature that allows the user to save the entire virtual machine (VM files, VHD and the machine configuration). It then allows users to using that set of files to bring the machine back on the same machine as the same VM (Restore), on a different machine as the same VM (Move), or a new VM (copy)

[](#BKMK_FixPDCPerms)

## FixVDCPermissions.ps1 {#BKMK_FixPDCPerms .heading-anchor}

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
# Unsigned script, requires use of set-executionpolicy remotesigned -force
# You must run the Windows PowerShell console as an elevated administrator

# Load Active Directory Windows PowerShell Module and switch to AD DS drive
import-module activedirectory
cd ad:

## Get Domain NC
$domainNC = get-addomain

## Get groups and obtain their SIDs
$dcgroup = get-adgroup "Cloneable Domain Controllers"

$sid1 = (get-adgroup $dcgroup).sid

## Get the DACL of the domain
$acl = get-acl $domainNC

## The following object specific ACE grants extended right 'Allow a DC to create a clone of itself' for the CDC group to the Domain NC
## 3e0f7e18-2c7a-4c10-ba82-4d926db99a3e is the schemaIDGuid for 'DS-Clone-Domain-Controller"

$objectguid = new-object Guid 3e0f7e18-2c7a-4c10-ba82-4d926db99a3e
$ace1 = new-object System.DirectoryServices.ActiveDirectoryAccessRule $sid1,"ExtendedRight","Allow",$objectguid

## Add the ACE in the ACL and set the ACL on the object

$acl.AddAccessRule($ace1)
set-acl -aclobject $acl $domainNC
write-host "Done writing new VDC permissions."
cd c:
```

Reading mode disabled

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Safely virtualizing Active Directory Domain Services (AD DS)](/en-us/windows-server/identity/ad-ds/introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100?source=recommendations)

    USN Rollback and safe virtualization of Active Directory

-   [Virtualized Domain Controller Troubleshooting](/en-us/windows-server/identity/ad-ds/manage/virtual-dc/virtualized-domain-controller-troubleshooting?source=recommendations)

    Learn more about: Virtualized Domain Controller Troubleshooting

Training

Module

[Configure and manage Hyper-V virtual machines - Training](/en-us/training/modules/configure-manage-hyper-v-virtual-machines/?source=recommendations)

Learn how to configure Hyper-V virtual machines in Windows Server, including VM generations, VHD and VHDX formats, storage options, shared virtual hard disks, VHD Sets, and guest clustering for high availability.

Certification

[Microsoft Certified: Azure Virtual Desktop Specialty - Certifications](/en-us/credentials/certifications/azure-virtual-desktop-specialty/?source=recommendations)

Plan, deliver, manage, and monitor virtual desktop experiences and remote apps on Microsoft Azure for any device.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
