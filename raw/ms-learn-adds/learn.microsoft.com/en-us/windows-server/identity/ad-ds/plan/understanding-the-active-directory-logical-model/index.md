---
{"title": "Understanding the Active Directory Logical Model", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Understanding the Active Directory Logical Model

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Designing your logical structure for Active Directory Domain Services (AD DS) involves defining the relationships between the containers in your directory. These relationships might be based on administrative requirements, such as delegation of authority, or they might be defined by operational requirements, such as the need to control replication.

Before you design your Active Directory logical structure, it is important to understand the Active Directory logical model. AD DS is a distributed database that stores and manages information about network resources as well as application-specific data from directory-enabled applications. AD DS allows administrators to organize elements of a network (such as users, computers, and devices) into a hierarchical containment structure. The top-level container is the forest. Within forests are domains, and within domains are organizational units (OUs). This is called the logical model because it is independent of the physical aspects of the deployment, such as the number of domain controllers required within each domain and network topology.

[](#active-directory-forest)

## Active Directory forest {#active-directory-forest .heading-anchor}

A forest is a collection of one or more Active Directory domains that share a common logical structure, directory schema (class and attribute definitions), directory configuration (site and replication information), and global catalog (forest-wide search capabilities). Domains in the same forest are automatically linked with two-way, transitive trust relationships.

[](#active-directory-domain)

## Active Directory domain {#active-directory-domain .heading-anchor}

A domain is a partition in an Active Directory forest. Partitioning data enables organizations to replicate data only to where it is needed. In this way, the directory can scale globally over a network that has limited available bandwidth. In addition, the domain supports a number of other core functions related to administration, including:

-   Network-wide user identity. Domains allow user identities to be created once and referenced on any computer joined to the forest in which the domain is located. Domain controllers that make up a domain are used to store user accounts and user credentials (such as passwords or certificates) securely.

-   Authentication. Domain controllers provide authentication services for users and supply additional authorization data such as user group memberships, which can be used to control access to resources on the network.

-   Trust relationships. Domains can extend authentication services to users in domains outside their own forest by means of trusts.

-   Replication. The domain defines a partition of the directory that contains sufficient data to provide domain services and then replicates it between the domain controllers. In this way, all domain controllers are peers in a domain and are managed as a unit.

[](#active-directory-organizational-units)

## Active Directory organizational units {#active-directory-organizational-units .heading-anchor}

OUs can be used to form a hierarchy of containers within a domain. OUs are used to group objects for administrative purposes such as the application of Group Policy or delegation of authority. Control (over an OU and the objects within it) is determined by the access control lists (ACLs) on the OU and on the objects in the OU. To facilitate the management of large numbers of objects, AD DS supports the concept of delegation of authority. By means of delegation, owners can transfer full or limited administrative control over objects to other users or groups. Delegation is important because it helps to distribute the management of large numbers of objects across a number of people who are trusted to perform management tasks.

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Reviewing the Domain Models](/en-us/windows-server/identity/ad-ds/plan/reviewing-the-domain-models?source=recommendations)

    Learn more about: Reviewing the Domain Models

-   [Evaluating AD DS Deployment Strategy Examples](/en-us/windows-server/identity/ad-ds/plan/evaluating-ad-ds-deployment-strategy-examples?source=recommendations)

    Learn more about: Evaluating AD DS Deployment Strategy Examples

-   [AD DS Design and Planning](/en-us/windows-server/identity/ad-ds/plan/ad-ds-design-and-planning?source=recommendations)

    Learn more about: AD DS Design and Planning

-   [Creating a Forest Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-forest-design?source=recommendations)

    Learn more about: Creating a Forest Design

-   [Appendix A - Reviewing Key AD DS Terms](/en-us/windows-server/identity/ad-ds/plan/appendix-a--reviewing-key-ad-ds-terms?source=recommendations)

    Learn more about: Appendix A: Reviewing Key AD DS Terms

-   [Using the Organizational Domain Forest Model](/en-us/windows-server/identity/ad-ds/plan/using-the-organizational-domain-forest-model?source=recommendations)

    Learn more about: Using the Organizational Domain Forest Model

-   [Determining the Number of Forests Required](/en-us/windows-server/identity/ad-ds/plan/determining-the-number-of-forests-required?source=recommendations)

    Learn more about: Determining the Number of Forests Required

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
