---
{"title": "Support for using Hyper-V Replica for virtualized domain controllers", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/support-for-using-hyper-v-replica-for-virtualized-domain-controllers", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Support for using Hyper-V Replica for virtualized domain controllers

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This topic explains the supportability of using Hyper-V Replica to replicate a virtual machine (VM) that runs as a domain controller (DC). Hyper-V Replica is a new capability of Hyper-V beginning with Windows Server 2012 that provides a built-in replication mechanism at a VM level.

Hyper-V Replica asynchronously replicates selected VMs from a primary Hyper-V host to a replica Hyper-V host across either LAN or WAN links. After initial replication is complete, subsequent changes are replicated at an interval defined by the administrator.

Failover can be either planned or unplanned. A planned failover is initiated by an administrator on the primary VM, and any un-replicated changes are copied over to the replica VM to prevent any data loss. An unplanned failover is initiated on the replica VM in response to an unexpected failure of the primary VM. Data loss is possible because there is no opportunity to transmit changes on the primary VM that might not have been replicated yet.

For more information about Hyper-V Replica, see [Hyper-V Replica Overview](/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj134172(v=ws.11)) and [Deploy Hyper-V Replica](/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj134207(v=ws.11)).

Note

Hyper-V Replica can be run only on Windows Server Hyper-V, not the version of Hyper-V that runs on Windows 8.

[](#windows-server-2012-or-newer-domain-controllers-required)

## Windows Server 2012 or newer domain controllers required {#windows-server-2012-or-newer-domain-controllers-required .heading-anchor}

Windows Server 2012 Hyper-V introduced VM-GenerationID (VMGenID). VMGenID provides a way for the hypervisor to communicate to the guest OS when significant changes have occurred. For example, the hypervisor can communicate to a virtualized DC that a restore from snapshot has occurred (Hyper-V snapshot restore technology, not backup restore). AD DS in Windows Server 2012 and newer is aware of VMGenID VM technology and uses it to detect when hypervisor operations are performed, such as snapshot restore, which allows it to better protect itself.

Note

Only AD DS on Windows Server 2012 DCs or newer provide these safety measures resulting from VMGenID; DCs that run all previous releases of Windows Server are subject to problems such as USN rollback that can occur when a virtualized DC is restored using an unsupported mechanism, such as snapshot restore. For more information about these safeguards and when they are triggered, see [Virtualized Domain Controller Architecture](virtualized-domain-controller-architecture).

When a Hyper-V replica failover occurs (planned or unplanned), the virtualized DC detects a VMGenID reset, triggering the aforementioned safety features. Active Directory operations then proceed as normal. The replica VM runs in place of the primary VM.

Note

Given that now there are now two instances of the same DC identity, there is a potential for both the primary instance and the replicated instance to run. While Hyper-V Replica has control mechanisms in place to ensure the primary and replica VMs do not run simultaneously, it is possible for them to run at the same time in the event the link between them fails after replication of the VM. In the event of this unlikely occurrence, virtualized DCs that run Windows Server 2012 have safeguards to help protect AD DS, whereas virtualized DCs that run earlier versions of Windows Server do not.

When using Hyper-V Replica, ensure that you follow best practices for [running virtual domain controllers on Hyper-V](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd363553(v=ws.10)). This discusses, for example, recommendations for storing Active Directory files on virtual SCSI disks, which provides stronger guarantees of data durability.

[](#supported-and-unsupported-scenarios)

## Supported and unsupported scenarios {#supported-and-unsupported-scenarios .heading-anchor}

Only VMs that run Windows Server 2012 or newer are supported for unplanned failover and for testing failover. Even for planned failover, Windows Server 2012 or newer is recommended for the virtualized DC in order to mitigate risks in the event that an administrator inadvertently starts both the primary VM and the replicated VM at the same time.

VMs that run earlier versions of Windows Server are supported for planned failover but unsupported for unplanned failover because of the potential for USN rollback. For more information about USN rollback, see [USN and USN Rollback](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd363553(v=ws.10)).

Note

There are no functional level requirements for the domain or forest; there are only operating system requirements for the DCs that run as VMs that are replicated using Hyper-V Replica. The VMs can be deployed in a forest that contains other physical or virtual DCs that run earlier versions of Windows Server and may or may not also be replicated using Hyper-V Replica.

This support statement is based on tests that were performed in a single domain-forest, though multi-domain forest configurations are also supported. For these tests, virtualized domain controllers DC1 and DC2 are Active Directory replication partners in the same site, hosted on a server that runs Hyper-V on Windows Server 2012. The VM guest that runs DC2 has Hyper-V Replica enabled. The Replica server is hosted in another geographically distant datacenter. To help explain the test case processes outlined below, the VM running on the replica server is referred to as DC2-Rec (although in practice it retains the same name as the original VM).

[](#windows-server-2012)

### Windows Server 2012 {#windows-server-2012 .heading-anchor}

The following table explains support for virtualized DCs that run Windows Server 2012 and test cases.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Planned Failover                                                                                                                                                                                                                                                                                      | Unplanned Failover                                                                                                                                |
+=======================================================================================================================================================================================================================================================================================================+===================================================================================================================================================+
| Supported                                                                                                                                                                                                                                                                                             | Supported                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Test case:                                                                                                                                                                                                                                                                                            | The test case is the same as for a planned failover, with these exceptions:                                                                       |
|                                                                                                                                                                                                                                                                                                       |                                                                                                                                                   |
| \- DC1 and DC2 are running Windows Server 2012.                                                                                                                                                                                                                                                       | \- Any AD updates received on DC2 but not yet replicated by AD to a replication partner before the failover event will be lost.                   |
|                                                                                                                                                                                                                                                                                                       |                                                                                                                                                   |
| \- DC2 is shut down and a failover is performed on DC2-Rec. The failover can be either planned or unplanned.                                                                                                                                                                                          | \- AD updates received on DC2 after the time of the recovery point that were replicated by AD to DC1 will be replicated from DC1 back to DC2-Rec. |
|                                                                                                                                                                                                                                                                                                       |                                                                                                                                                   |
| \- After DC2-Rec starts, it checks whether the value of VMGenID that it has in its database is the same as the value from the virtual machine driver saved by the Hyper-V Replica server.                                                                                                             |                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                       |                                                                                                                                                   |
| \- As a result, DC2-Rec triggers virtualization safeguards; in other words, it resets its InvocationID, discards its RID pool, and sets an initial synchronization requirement before it will assume an operations master role. For more information about initial synchronization requirement, see . |                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                       |                                                                                                                                                   |
| \- DC2-Rec then saves the new value of VMGenID in its database and commits any subsequent updates in the context of the new InvocationID.                                                                                                                                                             |                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                       |                                                                                                                                                   |
| \- As a result of the InvocationID reset, DC1 will converge on all AD changes introduced by DC2-Rec even if it was rolled back in time, meaning any AD updates performed on DC2-Rec after the failover will safely converge                                                                           |                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

[](#windows-server-2008-r2-and-earlier-versions)

### Windows Server 2008 R2 and earlier versions {#windows-server-2008-r2-and-earlier-versions .heading-anchor}

The following table explains support for virtualized DCs that run Windows Server 2008 R2 and earlier versions.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Planned Failover                                                                                                                                                                                                                                                                                                                                | Unplanned Failover                                                                                                                                             |
+=================================================================================================================================================================================================================================================================================================================================================+================================================================================================================================================================+
| Supported but not recommended because DCs that run these versions of Windows Server do not support VMGenID or use associated virtualization safeguards. This places them at risk for USN rollback. For more information, see [USN and USN Rollback](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd363553(v=ws.10)). | Not supported                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                 | **Note:** Unplanned failover would be supported where USN rollback is not a risk, such as a single DC in the forest (a configuration that is not recommended). |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Test case:                                                                                                                                                                                                                                                                                                                                      | N/A                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                |
| \- DC1 and DC2 are running Windows Server 2008 R2.                                                                                                                                                                                                                                                                                              |                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                |
| \- DC2 is shut down and a planned failover is performed on DC2-Rec. All data on DC2 is replicated to DC2-Rec before the shutdown is complete.                                                                                                                                                                                                   |                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                |
| \- After DC2-Rec starts, it resumes replication with DC1 using the same invocationID as DC2.                                                                                                                                                                                                                                                    |                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

-   [Virtualized Domain Controller Cloning Test Guidance for Application Vendors](/en-us/windows-server/identity/ad-ds/reference/virtual-dc/virtualized-domain-controller-cloning-test-guidance-for-application-vendors?source=recommendations)

    Learn more about: Virtualized Domain Controller Cloning Test Guidance for Application Vendors

-   [Virtualizing domain controllers with Hyper-V](/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controllers-hyper-v?source=recommendations)

    Learn about considerations for virtualizing Windows Server Active Directory domain controllers (DCs) in Hyper-V.

-   [Safely virtualizing Active Directory Domain Services (AD DS)](/en-us/windows-server/identity/ad-ds/introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100?source=recommendations)

    USN Rollback and safe virtualization of Active Directory

-   [Host AD DCs in virtual hosting environments - Windows Server](/en-us/troubleshoot/windows-server/active-directory/ad-dc-in-virtual-hosting-environment?source=recommendations)

    Discusses the issues that affect a DC that runs as a guest operating system (OS) in virtual hosting environments in Windows Server.

-   [Configure a subnetted reverse lookup zone - Windows Server](/en-us/troubleshoot/windows-server/networking/configure-subnetted-reverse-lookup-zone?source=recommendations)

    Describes how to configure a subnetted reverse lookup zone.

-   [Virtualized Domain Controller Deployment and Configuration](/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-deployment-and-configuration?source=recommendations)

    Learn more about: Virtualized Domain Controller Deployment and Configuration

-   [Virtualized Domain Controller Troubleshooting](/en-us/windows-server/identity/ad-ds/manage/virtual-dc/virtualized-domain-controller-troubleshooting?source=recommendations)

    Learn more about: Virtualized Domain Controller Troubleshooting

-   [Step 2 Configure the Multisite Infrastructure](/en-us/windows-server/remote/remote-access/ras/multisite/configure/step-2-configure-the-multisite-infrastructure?source=recommendations)

    Learn about how, to configure a multisite deployment, there are a number of steps required to modify network infrastructure settings.

Training

Module

[Implement Hyper-V Replica - Training](/en-us/training/modules/implement-hyper-v-replica/?source=recommendations)

Implement Hyper-V Replica

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
