---
{"title": "AD DS Design Requirements", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/ad-ds-design-requirements", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# AD DS Design Requirements

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

[](#designing-the-active-directory-logical-structure)

## Designing the Active Directory logical structure {#designing-the-active-directory-logical-structure .heading-anchor}

Before you deploy Windows Server 2008 Active Directory Domain Services (AD DS), you must plan for and design the AD DS logical structure for your environment. The AD DS logical structure determines how your directory objects are organized, and it provides an effective method for managing your network accounts and shared resources. When you design your AD DS logical structure, you define a significant part of the network infrastructure of your organization.

To design the AD DS logical structure, determine the number of forests that your organization requires, and then create designs for domains, Domain Name System (DNS) infrastructure, and organizational units (OUs). The following illustration shows the process for designing the logical structure.

For more information, see [Designing the Logical Structure for Windows Server 2008 AD DS](designing-the-logical-structure).

[](#designing-the-site-topology)

## Designing the site topology {#designing-the-site-topology .heading-anchor}

After you design the logical structure for your AD DS infrastructure, you must design the site topology for your network. The site topology is a logical representation of your physical network. It contains information about the location of AD DS sites, the AD DS domain controllers within each site, and the site links and site link bridges that support AD DS replication between sites. The following illustration shows the site topology design process.

For more information, see [Designing the Site Topology for Windows Server 2008 AD DS](designing-the-site-topology).

[](#planning-domain-controller-capacity)

## Planning domain controller capacity {#planning-domain-controller-capacity .heading-anchor}

To ensure efficient AD DS performance, you must determine the appropriate number of domain controllers for each site and verify that they meet the hardware requirements for Windows Server 2008 . Careful capacity planning for your domain controllers ensures that you do not underestimate hardware requirements, which can cause poor domain controller performance and application response time. The following illustration shows the process of domain controller capacity planning.

[](#enabling-windows-server-2008-advanced-ad-ds-features)

## Enabling Windows Server 2008 advanced AD DS features {#enabling-windows-server-2008-advanced-ad-ds-features .heading-anchor}

You can use Windows Server 2008 AD DS to introduce advanced features into your environment by raising the domain or forest functional level. You can raise the functional level to Windows Server 2008 when all domain controllers in the domain or forest are running Windows Server 2008 .

For more information, see [Enabling Advanced Features for AD DS](enabling-advanced-features-for-ad-ds).

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

-   [Identifying Your AD DS Design and Deployment Requirements](/en-us/windows-server/identity/ad-ds/plan/identifying-your-ad-ds-design-and-deployment-requirements?source=recommendations)

    Learn more about: Identifying Your AD DS Design and Deployment Requirements

-   [AD DS Deployment Requirements](/en-us/windows-server/identity/ad-ds/plan/ad-ds-deployment-requirements?source=recommendations)

    Learn more about: AD DS Deployment Requirements

-   [AD DS Design and Planning](/en-us/windows-server/identity/ad-ds/plan/ad-ds-design-and-planning?source=recommendations)

    Learn more about: AD DS Design and Planning

-   [Mapping Your Requirements to an AD DS Deployment Strategy](/en-us/windows-server/identity/ad-ds/plan/mapping-your-requirements-to-an-ad-ds-deployment-strategy?source=recommendations)

    Learn more about: Mapping Your Requirements to an AD DS Deployment Strategy

-   [Understanding AD DS Design](/en-us/windows-server/identity/ad-ds/plan/understanding-ad-ds-design?source=recommendations)

    Learn more about: Understanding AD DS Design

-   [Evaluating AD DS Deployment Strategy Examples](/en-us/windows-server/identity/ad-ds/plan/evaluating-ad-ds-deployment-strategy-examples?source=recommendations)

    Learn more about: Evaluating AD DS Deployment Strategy Examples

-   [Designing the Logical Structure](/en-us/windows-server/identity/ad-ds/plan/designing-the-logical-structure?source=recommendations)

    Learn more about: Designing the Logical Structure

Training

Module

[Introduction to AD DS - Training](/en-us/training/modules/introduction-to-ad-ds/?source=recommendations)

Introduction to AD DS

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
