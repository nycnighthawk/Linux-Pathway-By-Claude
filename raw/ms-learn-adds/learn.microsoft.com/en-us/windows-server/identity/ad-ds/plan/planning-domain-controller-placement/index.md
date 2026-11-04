---
{"title": "Planning Domain Controller Placement", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/planning-domain-controller-placement", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Planning Domain Controller Placement

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

After you have gathered all of the network information that will be used to design your site topology, plan where you want to place domain controllers, including forest root domain controllers, regional domain controllers, operations master role holders, and global catalog servers.

In Windows Server 2008 , you can also take advantage of read-only domain controllers (RODCs). An RODC is a new type of domain controller that hosts read-only partitions of the Active Directory database. Except for account passwords, an RODC holds all the Active Directory objects and attributes that a writable domain controller holds. However, changes can\'t be made to the database that is stored on the RODC. Changes must be made on a writable domain controller and then replicated back to the RODC.

An RODC is designed primarily to be deployed in remote or branch office environments, which typically have relatively few users, poor physical security, relatively poor network bandwidth to a hub site, and personnel with limited knowledge of information technology (IT). Deploying RODCs results in improved security and more efficient access to network resources. For more information about RODC features, see [AD DS: Read-Only Domain Controllers](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc732801(v=ws.10)). For information about how to deploy an RODC, see the [Read-Only Domain Controllers Step-by-Step Guide](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc772234(v=ws.10))

Note

This guide does not explain how you determine the proper number of domain controllers and the domain controller hardware requirements for each domain that is represented in each site.

[](#in-this-section)

## In this section {#in-this-section .heading-anchor}

-   [Planning Forest Root Domain Controller Placement](planning-forest-root-domain-controller-placement)

-   [Planning Regional Domain Controller Placement](planning-regional-domain-controller-placement)

-   [Planning Global Catalog Server Placement](planning-global-catalog-server-placement)

-   [Planning Operations Master Role Placement](planning-operations-master-role-placement)

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

-   [Planning Regional Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-regional-domain-controller-placement?source=recommendations)

    Learn more about: Planning Regional Domain Controller Placement

-   [Designing the Site Topology](/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology?source=recommendations)

    Learn more about: Designing the Site Topology

-   [Active Directory Replication Concepts](/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts?source=recommendations)

    Learn more about: Active Directory Replication Concepts

-   [Creating a Site Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-design?source=recommendations)

    Learn more about: Creating a Site Design

-   [Collecting Network Information](/en-us/windows-server/identity/ad-ds/plan/collecting-network-information?source=recommendations)

    Learn more about: Collecting Network Information

-   [Planning Global Catalog Server Placement](/en-us/windows-server/identity/ad-ds/plan/planning-global-catalog-server-placement?source=recommendations)

    Learn more about: Planning Global Catalog Server Placement

-   [Understanding Active Directory Site Topology](/en-us/windows-server/identity/ad-ds/plan/understanding-active-directory-site-topology?source=recommendations)

    Learn more about: Understanding Active Directory Site Topology

-   [Planning Forest Root Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-forest-root-domain-controller-placement?source=recommendations)

    Learn more about: Planning Forest Root Domain Controller Placement

Training

Module

[Manage AD DS domain controllers and FSMO roles - Training](/en-us/training/modules/manage-active-directory-domain-services-flexible-single-master-operation-roles/?source=recommendations)

Learn how to deploy and manage AD DS domain controllers, maintain availability with backup and recovery, manage the global catalog role, and transfer or seize FSMO roles including schema master, domain-naming master, RID master, infrastructure master, and PDC emulator.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
