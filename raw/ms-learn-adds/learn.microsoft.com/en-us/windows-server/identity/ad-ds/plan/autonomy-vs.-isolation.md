---
{"title": "Autonomy vs. Isolation", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/autonomy-vs.-isolation", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Autonomy vs. Isolation {#autonomy-vs-isolation}

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

You can design your Active Directory logical structure to achieve either of the following:

-   **Autonomy**. Involves independent but not exclusive control of a resource. When you achieve autonomy, administrators have the authority to manage resources independently; however, administrators with greater authority exist who also have control over those resources and can take control away if necessary. You can design your Active Directory logical structure to achieve the following types of autonomy:

    -   **Service autonomy**. This type of autonomy involves control over all or part of service management.

    -   **Data autonomy**. This type of autonomy involves control over all or part of the data stored in the directory or on member computers joined to the directory.

-   **Isolation**. Involves independent and exclusive control of a resource. When you achieve isolation, administrators have the authority to manage a resource independently, and no other administrator can take away control of the resource. You can design your Active Directory logical structure to achieve the following types of isolation:

    -   **Service isolation**. Prevents administrators (other than those administrators who are specifically designated to control service management) from controlling or interfering with service management.

    -   **Data isolation**. Prevents administrators (other than those administrators who are specifically designated to control or view data) from controlling or viewing a subset of data in the directory or on member computers joined to the directory.

Administrators who require only autonomy accept that other administrators who have equal or greater administrative authority have equal or greater control over service or data management. Administrators who require isolation have exclusive control over service or data management. Creating a design to achieve autonomy is generally less expensive than creating a design to achieve isolation.

In Active Directory Domain Services (AD DS), administrators can delegate both service administration and data administration to achieve either autonomy or isolation between organizations. The combination of service management, data management, autonomy, and isolation requirements of an organization impact the Active Directory containers that are used to delegate administration.

[](#isolation-and-autonomy-requirements)

## Isolation and autonomy requirements {#isolation-and-autonomy-requirements .heading-anchor}

The number of forests that you need to deploy is based on the autonomy and isolation requirements of each group within your organization. To identify your forest design requirements, you must identify the autonomy and isolation requirements for all groups in your organization. Specifically, you must identify the need for data isolation, data autonomy, service isolation, and service autonomy. You must also identify areas of limited connectivity in your organization.

[](#data-isolation)

### Data isolation {#data-isolation .heading-anchor}

Data isolation involves exclusive control over data by the group or organization that owns the data. It\'s important to note that service administrators have the ability to take control of a resource away from data administrators. And data administrators don\'t have the ability to prevent service administrators from accessing the resources that they control. Therefore, you can\'t achieve data isolation when another group within the organization is responsible for service administration. If a group requires data isolation, that group must also assume responsibility for service administration.

Because data stored in AD DS and on computers joined to AD DS can\'t be isolated from service administrators, the only way for a group within an organization to achieve complete data isolation is to create a separate forest for that data. Organizations for which the consequences of an attack by malicious software or by a coerced service administrator are substantial might choose to create a separate forest to achieve data isolation. Legal requirements typically create a need for this type of data isolation. For example:

-   A financial institution is required by law to limit access to data that belongs to clients in a particular jurisdiction to users, computers, and administrators located in that jurisdiction. Although the institution trusts service administrators that work outside the protected area, if the access limitation is violated, the institution will no longer be able to do business in that jurisdiction. Therefore, the financial institution must isolate data from service administrators outside that jurisdiction. Note that encryption isn\'t always an alternative to this solution. Encryption might not protect data from service administrators.

-   A defense contractor is required by law to limit access to project data to a specified set of users. Although the contractor trusts service administrators who control computer systems related to other projects, a violation of this access limitation will cause the contractor to lose business.

    Note

    If you have a data isolation requirement, you must decide if you need to isolate your data from service administrators or from data administrators and ordinary users. If your isolation requirement is based on isolation from data administrators and ordinary users, you can use access control lists (ACLs) to isolate the data. For the purposes of this design process, isolation from data administrators and ordinary users is not considered a data isolation requirement.

[](#data-autonomy)

### Data autonomy {#data-autonomy .heading-anchor}

Data autonomy involves the ability of a group or organization to manage its own data, including making administrative decisions about the data and performing any required administrative tasks without the need for approval from another authority.

Data autonomy doesn\'t prevent service administrators in the forest from accessing the data. For example, a research group within a large organization might want to be able to manage their project-specific data themselves but not need to secure the data from other administrators in the forest.

[](#service-isolation)

### Service isolation {#service-isolation .heading-anchor}

Service isolation involves exclusive control of the Active Directory infrastructure. Groups that require service isolation require that no administrator outside of the group can interfere with the operation of the directory service.

Operational or legal requirements typically create a need for service isolation. For example:

-   A manufacturing company has a critical application that controls equipment on the factory floor. Interruptions in the service on other parts of the network of the organization can\'t be allowed to interfere with the operation of the factory floor.

-   A hosting company provides service to multiple clients. Each client requires service isolation so that any service interruption that affects one client doesn\'t affect the other clients.

[](#service-autonomy)

### Service autonomy {#service-autonomy .heading-anchor}

Service autonomy involves the ability to manage the infrastructure without a requirement for exclusive control; for example, when a group wants to make changes to the infrastructure (such as adding or removing domains, modifying the Domain Name System (DNS) namespace, or modifying the schema) without the approval of the forest owner.

Service autonomy might be required within an organization for a group that wants to be able to control the service level of AD DS (by adding and removing domain controllers, as needed) or for a group that needs to be able to install directory-enabled applications that require schema extensions.

[](#limited-connectivity)

## Limited connectivity {#limited-connectivity .heading-anchor}

If a group within your organization owns networks that are separated by devices that restrict or limit connectivity between networks (such as firewalls and Network Address Translation (NAT) devices), this can impact your forest design. When you identify your forest design requirements, be sure to note the locations where you have limited network connectivity. This information is required to enable you to make decisions regarding the forest design.

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

-   [Creating a Domain Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-domain-design?source=recommendations)

    Learn more about: Creating a Domain Design

-   [Creating a Forest Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-forest-design?source=recommendations)

    Learn more about: Creating a Forest Design

-   [Reviewing the Domain Models](/en-us/windows-server/identity/ad-ds/plan/reviewing-the-domain-models?source=recommendations)

    Learn more about: Reviewing the Domain Models

-   [Understanding the Active Directory Logical Model](/en-us/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model?source=recommendations)

    Learn more about: Understanding the Active Directory Logical Model

-   [Designing the Logical Structure](/en-us/windows-server/identity/ad-ds/plan/designing-the-logical-structure?source=recommendations)

    Learn more about: Designing the Logical Structure

-   [Identifying the Deployment Project Participants](/en-us/windows-server/identity/ad-ds/plan/identifying-the-deployment-project-participants?source=recommendations)

    Learn more about: Identifying the Deployment Project Participants

-   [Determining the Number of Domains Required](/en-us/windows-server/identity/ad-ds/plan/determining-the-number-of-domains-required?source=recommendations)

    Learn more about: Determining the Number of Domains Required

-   [Determining the Number of Forests Required](/en-us/windows-server/identity/ad-ds/plan/determining-the-number-of-forests-required?source=recommendations)

    Learn more about: Determining the Number of Forests Required

Training

Module

[Manage advanced features of AD DS - Training](/en-us/training/modules/manage-advanced-features-of-ad-ds/?source=recommendations)

Learn how to create trust relationships between AD DS forests and domains, implement Enhanced Security Administrative Environment (ESAE) forests, monitor and troubleshoot AD DS replication, and create custom AD DS partitions.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
