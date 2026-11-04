---
{"title": "Overview of Active Directory Domain Services", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/active-directory-domain-services-overview", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Overview of Active Directory Domain Services

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

A directory is a hierarchical structure that stores information about objects on the network. A directory service, such as Active Directory Domain Services (AD DS), provides the methods for storing directory data and making this data available to network users and administrators. For example, AD DS stores information about user accounts, such as names, passwords, phone numbers, and so on, and enables other authorized users on the same network to access this information.

Active Directory stores information about objects on the network and makes this information easy for administrators and users to find and use. Active Directory uses a structured data store as the basis for a logical, hierarchical organization of directory information.

This data store, also known as the directory, contains information about Active Directory objects. These objects typically include shared resources such as servers, volumes, printers, and the network user and computer accounts. For more information about the Active Directory data store, see [Directory data store](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc736627(v=ws.10)).

Security is integrated with Active Directory through logon authentication and access control to objects in the directory. With a single network logon, administrators can manage directory data and organization throughout their network, and authorized network users can access resources anywhere on the network. Policy-based administration eases the management of even the most complex network. For more information about Active Directory security, see Security overview.

Active Directory also includes:

-   A set of rules, **the schema**, that defines the classes of objects and attributes contained in the directory, the constraints and limits on instances of these objects, and the format of their names. For more information about the schema, see Schema.

-   A **global catalog** that contains information about every object in the directory. This allows users and administrators to find directory information regardless of which domain in the directory actually contains the data. For more information about the global catalog, see The role of the global catalog.

-   A **query and index mechanism**, so that objects and their properties can be published and found by network users or applications. For more information about querying the directory, see Finding directory information.

-   A **replication service** that distributes directory data across a network. All domain controllers in a domain participate in replication and contain a complete copy of all directory information for their domain. Any change to directory data is replicated to all domain controllers in the domain. For more information about Active Directory replication, see Replication overview.

[](#understanding-active-directory)

## Understanding Active Directory {#understanding-active-directory .heading-anchor}

This section provides links to core Active Directory concepts:

-   [Active Directory Structure and Storage Technologies](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759186(v=ws.10))
-   [Domains Controller Roles](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc786438(v=ws.10))
-   Active Directory Schema
-   [Understanding Trusts](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771294(v=ws.10))
-   [Active Directory Replication Technologies](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc786438(v=ws.10))
-   [Active Directory Search and Publication Technologies](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc775686(v=ws.10))
-   Interoperating with DNS and Group Policy
-   [Understanding Schema](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759402(v=ws.10))

For a detailed list of Active Directory concepts, see [Understanding Active Directory](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc781408(v=ws.10)).

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

-   [Active Directory Domain Services overview](/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview?source=recommendations)

    Find out about Active Directory Domain Services, a directory service that makes network resource data available to authorized network users and administrators.

Training

Module

[Introduction to AD DS - Training](/en-us/training/modules/introduction-to-ad-ds/?source=recommendations)

Introduction to AD DS

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 11/01/2024
