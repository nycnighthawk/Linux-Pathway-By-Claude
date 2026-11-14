---
{"title": "Forest Design Models", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/forest-design-models", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Forest Design Models

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

You can apply one of the following three forest design models in your Active Directory environment:

-   Organizational forest model

-   Resource forest model

-   Restricted access forest model

It is likely that you will need to use a combination of these models to meet the needs of all the different groups in your organization.

[](#organizational-forest-model)

## Organizational forest model {#organizational-forest-model .heading-anchor}

In the organizational forest model, user accounts and resources are contained in the forest and managed independently. The organizational forest can be used to provide service autonomy, service isolation, or data isolation, if the forest is configured to prevent access to anyone outside the forest.

If users in an organizational forest need to access resources in other forests (or the reverse), trust relationships can be established between one organizational forest and the other forests. This makes it possible for administrators to grant access to resources in the other forest. The following illustration shows the organizational forest model.

Every Active Directory design includes at least one organizational forest.

[](#resource-forest-model)

## Resource forest model {#resource-forest-model .heading-anchor}

In the resource forest model, a separate forest is used to manage resources. Resource forests do not contain user accounts other than those required for service administration and those required to provide alternate access to the resources in that forest, if the user accounts in the organizational forest become unavailable. Forest trusts are established so that users from other forests can access the resources contained in the resource forest. The following illustration shows the resource forest model.

Resource forests provide service isolation that is used to protect areas of the network that need to maintain a state of high availability. For example, if your company includes a manufacturing facility that needs to continue to operate when there are problems on the rest of the network, you can create a separate resource forest for the manufacturing group.

[](#restricted-access-forest-model)

## Restricted access forest model {#restricted-access-forest-model .heading-anchor}

In the restricted access forest model, a separate forest is created to contain user accounts and data that must be isolated from the rest of the organization. Restricted access forests provide data isolation in situations where the consequences of compromising project data are severe. The following illustration shows a restricted access forest model.

Users from other forests cannot be granted access to the restricted data because no trust exists. In this model, users have an account in an organizational forest for access to general organizational resources and a separate user account in the restricted access forest for access to the classified data. These users must have two separate workstations, one connected to the organizational forest and the other connected to the restricted access forest. This protects against the possibility that a service administrator from one forest can gain access to a workstation in the restricted forest.

In extreme cases, the restricted access forest might be maintained on a separate physical network. Organizations that work on classified government projects sometimes maintain restricted access forests on separate networks to meet security requirements.

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Using the Organizational Domain Forest Model](/en-us/windows-server/identity/ad-ds/plan/using-the-organizational-domain-forest-model?source=recommendations)

    Learn more about: Using the Organizational Domain Forest Model

-   [Mapping Design Requirements to Forest Design Models](/en-us/windows-server/identity/ad-ds/plan/mapping-design-requirements-to-forest-design-models?source=recommendations)

    Learn more about: Mapping Design Requirements to Forest Design Models

-   [Determining the Number of Forests Required](/en-us/windows-server/identity/ad-ds/plan/determining-the-number-of-forests-required?source=recommendations)

    Learn more about: Determining the Number of Forests Required

-   [Reviewing the Domain Models](/en-us/windows-server/identity/ad-ds/plan/reviewing-the-domain-models?source=recommendations)

    Learn more about: Reviewing the Domain Models

-   [Understanding the Active Directory Logical Model](/en-us/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model?source=recommendations)

    Learn more about: Understanding the Active Directory Logical Model

-   [Determining the Number of Domains Required](/en-us/windows-server/identity/ad-ds/plan/determining-the-number-of-domains-required?source=recommendations)

    Learn more about: Determining the Number of Domains Required

-   [Creating a Forest Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-forest-design?source=recommendations)

    Learn more about: Creating a Forest Design

-   [Identifying Forest Design Requirements](/en-us/windows-server/identity/ad-ds/plan/identifying-forest-design-requirements?source=recommendations)

    Learn more about: Identifying Forest Design Requirements

Training

Module

[Manage advanced features of AD DS - Training](/en-us/training/modules/manage-advanced-features-of-ad-ds/?source=recommendations)

Learn how to create trust relationships between AD DS forests and domains, implement Enhanced Security Administrative Environment (ESAE) forests, monitor and troubleshoot AD DS replication, and create custom AD DS partitions.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
