---
{"title": "Site Topology Owner Role", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/site-topology-owner-role", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Site Topology Owner Role

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

The administrator who manages the site topology is known as the site topology owner. The site topology owner understands the conditions of the network between sites and has the authority to change settings in Active Directory Domain Services (AD DS) to implement changes to the site topology. Changes to the site topology affect changes in the replication topology. The site topology owner\'s responsibilities include:

-   Controlling changes to the site topology if network connectivity changes.

-   Obtaining and maintaining information about network connections and routers from the network group. The site topology owner must maintain a list of subnet addresses, subnet masks, and the location to which each belongs. The site topology owner must also understand any issues about network speed and capacity that affect site topology to effectively set costs for site links.

-   Moving Active Directory server objects representing domain controllers between sites if a domain controller\'s IP address changes to a different subnet in a different site, or if the subnet itself is assigned to a different site. In either case, the site topology owner must manually move the Active Directory server object of the domain controller to the new site.

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Understanding Active Directory Site Topology](/en-us/windows-server/identity/ad-ds/plan/understanding-active-directory-site-topology?source=recommendations)

    Learn more about: Understanding Active Directory Site Topology

-   [Site functions](/en-us/windows-server/identity/ad-ds/plan/site-functions?source=recommendations)

    Learn more about various site functions in AD DS

-   [Designing the Site Topology](/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology?source=recommendations)

    Learn more about: Designing the Site Topology

-   [Collecting Network Information](/en-us/windows-server/identity/ad-ds/plan/collecting-network-information?source=recommendations)

    Learn more about: Collecting Network Information

-   [Creating a Site Link Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-link-design?source=recommendations)

    Learn more about: Creating a Site Link Design

-   [Creating a Site Link Bridge Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-link-bridge-design?source=recommendations)

    Learn more about: Creating a Site Link Bridge Design

-   [Creating a Site Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-design?source=recommendations)

    Learn more about: Creating a Site Design

-   [Planning Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-domain-controller-placement?source=recommendations)

    Learn more about: Planning Domain Controller Placement

Training

Module

[Deploy and manage Active Directory Domain Services domain controllers - Training](/en-us/training/modules/deploy-manage-active-directory-domain-services-domain-controllers/?source=recommendations)

This module introduces you to the topology of domain controllers within an Active Directory environment. It also starts you down the path of deploying, managing, and migrating a domain controller between servers.

Certification

[Microsoft 365 Certified: Administrator Expert - Certifications](/en-us/credentials/certifications/m365-administrator-expert/?source=recommendations)

If you're an administrator who deploys and manages Microsoft 365 and performs Microsoft 365 tenant-level implementation and administration of cloud and hybrid environments, this certification is designed for you.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
