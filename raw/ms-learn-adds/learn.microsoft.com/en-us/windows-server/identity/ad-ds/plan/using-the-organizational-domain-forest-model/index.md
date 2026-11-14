---
{"title": "Using the Organizational Domain Forest Model", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/using-the-organizational-domain-forest-model", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Using the Organizational Domain Forest Model

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

In the organizational domain forest model, several autonomous groups each own a domain within a forest. Each group controls domain-level service administration, which enables them to manage certain aspects of service management autonomously while the forest owner controls forest-level service management.

The following illustration shows an organizational domain forest model.

[](#domain-level-service-autonomy)

## Domain-level service autonomy {#domain-level-service-autonomy .heading-anchor}

The organizational domain forest model enables the delegation of authority for domain-level service management. The following table lists the types of service management that can be controlled at the domain level.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------
  Type of service management                   Associated tasks
  -------------------------------------------- ----------------------------------------------------------------------------------------------------------------
  Management of domain controller operations   \- Creating and removing domain controllers\
                                               - Monitoring the functioning of domain controllers\
                                               - Managing services that are running on domain controllers\
                                               - Backing up and restoring the directory

  Configuration of domain-wide settings        \- Creating domain and domain user account policies, such as password, Kerberos, and account lockout policies\
                                               - Creating and applying domain-wide Group Policy

  Delegation of data-level administration      \- Creating organizational units (OUs) and delegating administration\
                                               - Repairing problems in the OU structure that OU owners do not have sufficient access rights to fix

  Management of external trusts                \- Establishing trust relationships with domains outside the forest
  -------------------------------------------------------------------------------------------------------------------------------------------------------------

Other types of service management, such as schema or replication topology management, are the responsibility of the forest owner.

[](#domain-owner)

## Domain owner {#domain-owner .heading-anchor}

In an organizational domain forest model, domain owners are responsible for domain-level service management tasks. Domain owners have authority over the entire domain as well as access to all other domains in the forest. For this reason, domain owners must be trusted individuals selected by the forest owner.

Delegate domain-level service management to a domain owner, if the following conditions are met:

-   All groups participating in the forest trust the new domain owner and the service management practices of the new domain.

-   The new domain owner trusts the forest owner and all the other domain owners.

-   All domain owners in the forest agree that the new domain owner has service administrator management and selection policies and practices that are equal to or more strict than their own.

-   All domain owners in the forest agree that domain controllers managed by the new domain owner in the new domain are physically secure.

Note that if a forest owner delegates domain-level service management to a domain owner, other groups might choose not to join that forest if they do not trust that domain owner.

All domain owners must be aware that if any of these conditions change in the future, it might become necessary to move the organizational domains into a multiple forest deployment.

Note

Another way to minimize security risks to a Windows Server 2008 Active Directory domain is to employ administrator role separation, which requires the deployment of a read-only domain controller (RODC) in your Active Directory infrastructure. An RODC is a new type of domain controller in the Windows Server 2008 operating system that hosts read-only partitions of the Active Directory database. Before the release of Windows Server 2008 , any server maintenance work on a domain controller had to be performed by a domain administrator. In Windows Server 2008 , you can delegate local administrative permissions for an RODC to any domain user without granting that user any administrative rights for the domain or other domain controllers. This permits the delegated user to log on to an RODC and perform maintenance work, such as upgrading a driver, on the server. However, this delegated user cannot log on to any other domain controller or perform any other administrative task in the domain. In this way, any trusted user can be delegated the ability to effectively manage the RODC without compromising the security of the rest of the domain. For more information about RODCs, see [AD DS: Read-Only Domain Controllers](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc732801(v=ws.10)).

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

-   [Forest Design Models](/en-us/windows-server/identity/ad-ds/plan/forest-design-models?source=recommendations)

    Learn more about: Forest Design Models

-   [Understanding the Active Directory Logical Model](/en-us/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model?source=recommendations)

    Learn more about: Understanding the Active Directory Logical Model

-   [Determining the Number of Domains Required](/en-us/windows-server/identity/ad-ds/plan/determining-the-number-of-domains-required?source=recommendations)

    Learn more about: Determining the Number of Domains Required

-   [Reviewing the Domain Models](/en-us/windows-server/identity/ad-ds/plan/reviewing-the-domain-models?source=recommendations)

    Learn more about: Reviewing the Domain Models

-   [Selecting the Forest Root Domain](/en-us/windows-server/identity/ad-ds/plan/selecting-the-forest-root-domain?source=recommendations)

    Learn more about: Selecting the Forest Root Domain

-   [Determining the Number of Forests Required](/en-us/windows-server/identity/ad-ds/plan/determining-the-number-of-forests-required?source=recommendations)

    Learn more about: Determining the Number of Forests Required

-   [AD DS Design and Planning](/en-us/windows-server/identity/ad-ds/plan/ad-ds-design-and-planning?source=recommendations)

    Learn more about: AD DS Design and Planning

-   [Reviewing OU Design Concepts](/en-us/windows-server/identity/ad-ds/plan/reviewing-ou-design-concepts?source=recommendations)

    Learn more about: Reviewing OU Design Concepts

Training

Module

[Deploy and manage Active Directory Domain Services domain controllers - Training](/en-us/training/modules/deploy-manage-active-directory-domain-services-domain-controllers/?source=recommendations)

This module introduces you to the topology of domain controllers within an Active Directory environment. It also starts you down the path of deploying, managing, and migrating a domain controller between servers.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
