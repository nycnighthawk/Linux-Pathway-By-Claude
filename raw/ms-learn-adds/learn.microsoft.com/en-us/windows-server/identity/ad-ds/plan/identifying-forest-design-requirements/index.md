---
{"title": "Identifying Forest Design Requirements", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/identifying-forest-design-requirements", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Identifying Forest Design Requirements

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

To create a forest design for your organization, you must identify the business requirements that your directory structure needs to accommodate. This involves determining how much autonomy the groups in your organization need to manage their network resources and whether or not each group needs to isolate their resources on the network from other groups.

Active Directory Domain Services (AD DS) enables you to design a directory infrastructure that accommodates multiple groups within an organization that have unique management requirements and to achieve structural and operational independence between groups as needed.

Groups in your organization might have some of the following types of requirements:

-   **Organizational structure requirements**. Parts of an organization might participate in a shared infrastructure to save costs but require the ability to operate independently from the rest of the organization. For example, a research group within a large organization might need to maintain control over all of their own research data.

-   **Operational requirements**. One part of an organization might place unique constraints on the directory service configuration, availability, or security, or use applications that place unique constraints on the directory. For example, individual business units within an organization might deploy directory-enabled applications that modify the directory schema that are not deployed by other business units. Because the directory schema is shared between all the domains in the forest, creating multiple forests is one solution for such a scenario. Other examples are found in the following organizations and scenarios:

    -   Military organizations

    -   Hosting scenarios

    -   Organizations maintaining a directory that is available both internally and externally (such as those publicly accessible to users on the Internet)

-   **Legal requirements**. Some organizations have legal requirements to operate in a specific way, for example, restricting access to certain information as specified in a business contract. Some organizations have security requirements to operate on isolated internal networks. Failure to meet these requirements can result in loss of the contract and possibly legal action.

Part of identifying your forest design requirements involves identifying the degree to which groups in your organization can trust the potential forest owners and their service administrators and identifying the autonomy and isolation requirements for each group in your organization.

The design team must document the isolation and autonomy requirements for service and data administration for each group in the organization that intends to use AD DS. The team must also note any areas of limited connectivity that might affect the deployment of AD DS.

The design team must document the isolation and autonomy requirements for service and data administration for each group in the organization that intends to use AD DS. The team must also note any areas of limited connectivity that might affect the deployment of AD DS. For a worksheet to assist you in documenting the regions you identified, download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip from [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608) and open \"Forest Design Requirements\" (DSSLOGI_2.doc).

[](#in-this-section)

## In this section {#in-this-section .heading-anchor}

-   [Service Administrator Scope of Authority](service-administrator-scope-of-authority)

-   [Autonomy vs. Isolation](autonomy-vs.-isolation)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Identifying the Deployment Project Participants](/en-us/windows-server/identity/ad-ds/plan/identifying-the-deployment-project-participants?source=recommendations)

    Learn more about: Identifying the Deployment Project Participants

-   [Determining the Number of Forests Required](/en-us/windows-server/identity/ad-ds/plan/determining-the-number-of-forests-required?source=recommendations)

    Learn more about: Determining the Number of Forests Required

-   [Service Administrator Scope of Authority](/en-us/windows-server/identity/ad-ds/plan/service-administrator-scope-of-authority?source=recommendations)

    Learn more about: Service Administrator Scope of Authority

-   [Reviewing the Domain Models](/en-us/windows-server/identity/ad-ds/plan/reviewing-the-domain-models?source=recommendations)

    Learn more about: Reviewing the Domain Models

-   [Creating a Forest Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-forest-design?source=recommendations)

    Learn more about: Creating a Forest Design

-   [Designing the Logical Structure](/en-us/windows-server/identity/ad-ds/plan/designing-the-logical-structure?source=recommendations)

    Learn more about: Designing the Logical Structure

-   [Understanding the Active Directory Logical Model](/en-us/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model?source=recommendations)

    Learn more about: Understanding the Active Directory Logical Model

-   [Forest Design Models](/en-us/windows-server/identity/ad-ds/plan/forest-design-models?source=recommendations)

    Learn more about: Forest Design Models

Training

Module

[Introduction to AD DS - Training](/en-us/training/modules/introduction-to-ad-ds/?source=recommendations)

Introduction to AD DS

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
