---
{"title": "Planning Forest Root Domain Controller Placement", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/planning-forest-root-domain-controller-placement", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Planning Forest Root Domain Controller Placement

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Forest root domain controllers are needed to create trust paths for clients that need to access resources in domains other than their own. Place forest root domain controllers in hub locations and at locations that host datacenters. If users in a given location need to access resources from other domains in the same location, and the network availability between the datacenter and the user location is unreliable, you can either add a forest root domain controller in the location or create a shortcut trust between the two domains. It is more cost efficient to create a shortcut trust between the domains unless you have other reasons to place a forest root domain controller in that location.

Shortcut trusts help to optimize authentication requests made from users located in either domain. For more information about shortcut trusts between domains, see the article [Understanding When to Create a Shortcut Trust](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc754538(v=ws.11)).

For a worksheet to assist you in documenting your forest root domain controller placement, see [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608), download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip, and open \"Domain Controller Placement\" (DSSTOPO_4.doc).

You will need to refer to this information when you create the forest root domain. For more information about deploying the forest root domain, see [Deploying a Windows Server 2008 Forest Root Domain](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731174(v=ws.10)).

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

-   [Planning Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-domain-controller-placement?source=recommendations)

    Learn more about: Planning Domain Controller Placement

-   [Collecting Network Information](/en-us/windows-server/identity/ad-ds/plan/collecting-network-information?source=recommendations)

    Learn more about: Collecting Network Information

-   [Designing the Site Topology](/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology?source=recommendations)

    Learn more about: Designing the Site Topology

-   [Creating a Site Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-design?source=recommendations)

    Learn more about: Creating a Site Design

-   [Planning Global Catalog Server Placement](/en-us/windows-server/identity/ad-ds/plan/planning-global-catalog-server-placement?source=recommendations)

    Learn more about: Planning Global Catalog Server Placement

Training

Module

[Manage AD DS domain controllers and FSMO roles - Training](/en-us/training/modules/manage-active-directory-domain-services-flexible-single-master-operation-roles/?source=recommendations)

Learn how to deploy and manage AD DS domain controllers, maintain availability with backup and recovery, manage the global catalog role, and transfer or seize FSMO roles including schema master, domain-naming master, RID master, infrastructure master, and PDC emulator.

Certification

[Microsoft Certified: Azure Virtual Desktop Specialty - Certifications](/en-us/credentials/certifications/azure-virtual-desktop-specialty/?source=recommendations)

Plan, deliver, manage, and monitor virtual desktop experiences and remote apps on Microsoft Azure for any device.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
