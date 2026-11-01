---
{"title": "Flexible Single Master Operations roles in Active Directory Domain Services", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-fsmo-roles", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Flexible Single Master Operations roles in Active Directory Domain Services

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Domain controllers that hold operations master roles, also known as flexible single master operations (FSMO) roles, to keep the directory functioning properly by performing a unique set of domain and forest management tasks. FSMO roles prevent conflicts in the directory by ensuring that certain updates are processed by only one domain controller at a time. This article explains the five FSMO roles and provides guidelines for placing them effectively.

[](#operations-master-roles)

## Operations master roles {#operations-master-roles .heading-anchor}

Three operations master roles exist in each domain:

-   PDC Emulator

-   RID Master

-   Infrastructure Master

Two operations master roles are present at the forest level:

-   Schema Master

-   Domain Naming Master

[](#pdc-emulator)

### PDC Emulator {#pdc-emulator .heading-anchor}

The primary domain controller (PDC) emulator receives preferential replication of password changes that that occur through other domain controllers in the domain. The PDC emulator is the source for the latest password information whenever a sign-in attempt fails as a result of a bad password. It also processes account lockouts. It\'s a preferred point of administration for services (examples are Group Policy and Distributed File System, DFS). For this reason, of all operations master roles, the PDC emulator operations master role has the highest impact on the performance of the domain controller that hosts that role. The PDC emulator in the forest root domain is the authoritative Windows Time service (`W32time`) time source for the forest.

[](#rid-master)

### RID Master {#rid-master .heading-anchor}

The relative ID (RID) master allocates RID pools to all domain controllers to ensure that new security principals can be created with a unique identifier. Relative Identifier (RID) pool is used to assign unique Security Identifiers (SIDs) to objects within a domain. Each domain controller in an Active Directory domain is allocated a pool of RIDs from which it can draw to create unique SIDs for new security principals (such as users, groups, and computers). When a domain controller needs more SIDs, it requests a block of RIDs from the RID Master.

[](#infrastructure-master)

### Infrastructure Master {#infrastructure-master .heading-anchor}

The infrastructure master manages references from objects in its domain to objects in other domains. It also updates group-to-user references when the members of groups are renamed or changed. The infrastructure master represents references by GUID, SID, or DN of the object being referenced.

[](#schema-master)

### Schema Master {#schema-master .heading-anchor}

The schema master governs all changes to the schema naming context or `LDAP://cn=schema,cn=configuration,dc=<domain>`. The Active Directory schema defines the structure and rules for the directory\'s data. The schema determines what types of objects can exist in the directory, the attributes that these objects can have, and the relationships between different object types. For example, such as users, computers, and groups. There\'s only one schema master in an AD DS forest.

[](#domain-naming-master)

### Domain Naming Master {#domain-naming-master .heading-anchor}

The domain naming master adds and removes domain directory partitions and application directory partitions to and from the forest. It\'s responsible for the partitions configuration naming context or `LDAP://CN=Partitions, CN=Configuration, DC=<domain>`. This FSMO role is responsible for ensuring the uniqueness of domain names within a forest and for authorizing changes to forest namespace structure. It can also add or remove cross references to domains in external directories.

[](#role-placement-guidelines)

## Role placement guidelines {#role-placement-guidelines .heading-anchor}

You can assign the forest-level and domain-level operations master roles to any domain controller in the forest and domain. However, careful placement of your operations masters becomes more important as you add more domains and sites to your forest. To perform their respective operations, the domain controllers that host operations master roles must be consistently available. Operation masters must be located in areas where network reliability is high.

The following guidelines help to minimize administrative overhead and ensure the proper performance of Active Directory Domain Services (AD DS). The guidelines simplify the recovery process if a domain controller that is hosting an operations master role fails.

Guidelines for operations master role placement:

-   Configure another domain controller as the standby operations master for the forest-level roles.

-   Configure another domain controller as the standby operations master for the domain-level roles.

-   Place domain-level roles on a high-performance domain controller.

-   Leave forest-level roles on a domain controller in the forest root domain.

-   In your forest root domain, transfer the three domain-level roles to another domain controller that has a high performance level.

-   In all other domains, leave the domain-level roles on the first domain controller.

-   Adjust the workload of the PDC emulator, if necessary.

The PDC emulator role requires a powerful and reliable domain controller to ensure that the domain controller is available and capable of handling the workload. Of all the operations master roles, the PDC emulator role creates the most overhead on the server that is hosting the role. It has the most intensive daily interaction with other systems on the network. The PDC emulator has the greatest potential to affect daily operations of the directory.

Improper placement of infrastructure master role can cause the infrastructure master to perform incorrectly. If all the domain controllers in a domain also host the global catalog, all the domain controllers have the current data. When the Infrastructure Master runs on a Global Catalog server, it stops updating object information because it doesn\'t contain any references to objects that it doesn\'t hold. As a result, cross-domain object references in that domain aren\'t updated and a warning to that effect is logged on that domain controller\'s event log. When the Recycle Bin optional feature is enabled, every domain controller is responsible to update its cross-domain object references when the referenced object is moved, renamed, or deleted. In this case, there are no tasks associated with the Infrastructure FSMO role.

[](#next-steps)

## Next steps {#next-steps .heading-anchor}

-   [Transfer Flexible Single Master Operations (FSMO) roles](manage-fsmo-roles)

-   [Managing RID Issuance](managing-rid-issuance)

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

-   [Transfer Flexible Single Master Operations roles in Windows Server](/en-us/windows-server/identity/ad-ds/manage/manage-fsmo-roles?source=recommendations)

    Learn how to transfer FSMO roles in Active Directory Domain Services (AD DS) to optimize performance and simplify administration.

-   [Managing RID Issuance](/en-us/windows-server/identity/ad-ds/manage/managing-rid-issuance?source=recommendations)

    Learn more about: Managing RID Issuance

-   [Active Directory Flexible Single Master Operation (FSMO) roles in Windows - Windows Server](/en-us/troubleshoot/windows-server/active-directory/fsmo-roles?source=recommendations)

    This article talks about the Active Directory FSMO roles in Windows.

-   [Flexible Single-Master Operation (FSMO) placement and optimization on AD DCs - Windows Server](/en-us/troubleshoot/windows-server/active-directory/fsmo-placement-and-optimization-on-ad-dcs?source=recommendations)

    Certain operations are optimally done on a single domain controller. Describes how Active Directory FSMO roles are positioned in both the forest and the domain for these operations.

-   [Active Directory Replication Concepts](/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts?source=recommendations)

    Learn more about: Active Directory Replication Concepts

-   [Transfer and seize FSMO roles - Windows Server](/en-us/troubleshoot/windows-server/active-directory/fsmo-transfer-seizure-process?source=recommendations)

    Describes how to transfer and seize Flexible Single Master Operations (FSMO) roles.

-   [Planning Operations Master Role Placement](/en-us/windows-server/identity/ad-ds/plan/planning-operations-master-role-placement?source=recommendations)

    Learn more about: Planning Operations Master Role Placement

-   [Transfer or seize Operation Master roles - Windows Server](/en-us/troubleshoot/windows-server/active-directory/transfer-or-seize-operation-master-roles-in-ad-ds?source=recommendations)

    Describes how you can use the Ntdsutil.exe utility to move or to seize Operation Master roles, formerly known as Flexible Single Master Operations (FSMO) roles.

Training

Module

[Manage AD DS domain controllers and FSMO roles - Training](/en-us/training/modules/manage-active-directory-domain-services-flexible-single-master-operation-roles/?source=recommendations)

Learn how to deploy and manage AD DS domain controllers, maintain availability with backup and recovery, manage the global catalog role, and transfer or seize FSMO roles including schema master, domain-naming master, RID master, infrastructure master, and PDC emulator.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 07/02/2024
