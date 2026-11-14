---
{"title": "Active Directory Domain Services overview", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Domain Services overview

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

A directory is a hierarchical structure that stores information about objects on a network. A directory service, such as Active Directory Domain Services (AD DS), provides the methods for storing directory data and making this data available to network users and administrators. For example, AD DS stores information about user accounts, such as names, passwords, phone numbers, and so on. AD DS also provides a way for authorized users on the same network to access this information.

AD DS stores information about objects on the network and makes this information easy for administrators and users to find and use. AD DS uses a structured data store as the basis for a logical, hierarchical organization of directory information.

This data store, also known as the directory, contains information about AD DS objects. These objects typically include shared resources such as servers, volumes, printers, and the network user and computer accounts. For more information about the AD DS data store, see [Directory data store](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc736627(v=ws.10)).

Security is integrated with AD DS through sign-in authentication and access control to objects in the directory. With a single network username and password, administrators can manage directory data and organization throughout their network, and authorized network users can access resources anywhere on the network. Policy-based administration eases the management of even the most complex network. For more information about AD DS security, see [Best practices for securing Active Directory](../../plan/security-best-practices/best-practices-for-securing-active-directory).

AD DS also includes:

-   A set of rules, the **schema**, that defines the classes of objects and attributes contained in the directory, the constraints and limits on instances of these objects, and the format of their names. For more information about the schema, see [Schema](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc756876(v=ws.10)).

-   A **global catalog** that contains information about every object in the directory. Users and administrators can use the catalog to find directory information regardless of the directory domain that actually contains the data. For more information about the global catalog, see [Global catalog](/en-us/windows/win32/ad/global-catalog).

-   A **query and index mechanism**, so that objects and their properties can be published and found by network users or applications. For more information about querying the directory, see [Searching in Active Directory Domain Services](/en-us/windows/win32/ad/searching-in-active-directory-domain-services).

-   A **replication service** that distributes directory data across a network. All domain controllers in a domain participate in replication and contain a complete copy of all directory information for their domain. Any change to directory data is replicated to all domain controllers in the domain. For more information about AD DS replication, see [Active Directory Replication Concepts](../replication/active-directory-replication-concepts).

[](#understand-ad-ds)

## Understand AD DS {#understand-ad-ds .heading-anchor}

This section provides links to core AD DS concepts:

-   [Active Directory Structure and Storage Technologies](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759186(v=ws.10))
-   [Domain Controller Roles](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc786438(v=ws.10))
-   [Active Directory Schema](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc771796(v=ws.10))
-   [Managing Trusts](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc771568(v=ws.10))
-   [Active Directory Replication Technologies](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc776877(v=ws.10))
-   [Active Directory Search and Publication Technologies](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc775686(v=ws.10))
-   [DNS Group Policy Settings](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd197486(v=ws.10))
-   [Active Directory Schema Technical Reference](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759402(v=ws.10))

For a detailed list of AD DS concepts, see [Understanding Active Directory](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc781408(v=ws.10)).

Reading mode disabled

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Training

Module

[Introduction to AD DS - Training](/en-us/training/modules/introduction-to-ad-ds/?source=recommendations)

Introduction to AD DS

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 03/11/2025
