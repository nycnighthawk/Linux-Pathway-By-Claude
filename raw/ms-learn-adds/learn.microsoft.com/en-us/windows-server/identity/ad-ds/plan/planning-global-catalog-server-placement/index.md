---
{"title": "Planning Global Catalog Server Placement", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/planning-global-catalog-server-placement", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Planning Global Catalog Server Placement

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Global catalog placement requires planning except if you have a single-domain forest. In a single-domain forest, configure all domain controllers as global catalog servers. Because every domain controller stores the only domain directory partition in the forest, configuring each domain controller as a global catalog server doesn\'t require any additional disk space usage, CPU usage, or replication traffic. In a single-domain forest, all domain controllers act as virtual global catalog servers; that is, they can all respond to any authentication or service request. This special condition for single-domain forests is by design. Authentication requests don\'t require contacting a global catalog server as they do when there are multiple domains, and a user can be a member of a universal group that exists in a different domain. However, only domain controllers that are designated as global catalog servers can respond to global catalog queries on the global catalog port 3268. To simplify administration in this scenario and to ensure consistent responses, designating all domain controllers as global catalog servers eliminates the concern about which domain controllers can respond to global catalog queries. Specifically, any time a user uses Start\\Search\\For People or Find Printers or expands Universal Groups, these requests go only to the global catalog.

In multiple-domain forests, global catalog servers facilitate user logon requests and forest-wide searches. The following illustration shows how to determine which locations require global catalog servers.

In most cases, it\'s recommended that you include the global catalog when you install new domain controllers. The following exceptions apply:

-   Limited bandwidth: In remote sites, if the wide area network (WAN) link between the remote site and the hub site is limited, you can use universal group membership caching in the remote site to accommodate the logon needs of users in the site.
-   Infrastructure operations master role incompatibility: Don\'t place the global catalog on a domain controller that hosts the infrastructure operations master role in the domain unless all domain controllers in the domain are global catalog servers or the forest has only one domain.

[](#adding-global-catalog-servers-based-on-application-requirements)

## Adding global catalog servers based on application requirements {#adding-global-catalog-servers-based-on-application-requirements .heading-anchor}

Certain applications, such as Microsoft Exchange, Message Queuing (also known as MSMQ), and applications using DCOM don\'t deliver adequate response over latent WAN links and therefore need a highly available global catalog infrastructure to provide low query latency. Determine whether any applications that perform poorly over a slow WAN link are running in locations or whether the locations require Microsoft Exchange Server. If your locations include applications that don\'t deliver adequate response over a WAN link, you must place a global catalog server at the location to reduce query latency.

Note

Read-only domain controllers (RODCs) can be promoted successfully to global catalog server status. However, certain directory-enabled applications cannot support an RODC as a global catalog server. For example, no version of Microsoft Exchange Server uses RODCs. However, Microsoft Exchange Server works in environments that include RODCs, as long as there are writable domain controllers available. Exchange Server 2007 effectively ignores RODCs. Exchange Server 2003 also ignores RODCs in default conditions where Exchange components automatically detect available domain controllers. No changes were made to Exchange Server 2003 to make it aware of read-only directory servers. Therefore, trying to force Exchange Server 2003 services and management tools to use RODCs may result in unpredictable behavior.

[](#adding-global-catalog-servers-for-a-large-number-of-users)

## Adding global catalog servers for a large number of users {#adding-global-catalog-servers-for-a-large-number-of-users .heading-anchor}

Place global catalog servers at all locations that contain more than 100 users to reduce congestion of network WAN links and to prevent productivity loss in case of WAN link failure.

[](#using-highly-available-bandwidth)

## Using highly available bandwidth {#using-highly-available-bandwidth .heading-anchor}

You don\'t need to place a global catalog at a location that doesn\'t include applications that require a global catalog server, includes less than 100 users, and is also connected to another location that includes a global catalog server by a WAN link that is 100 percent available for Active Directory Domain Services (AD DS). In this case, the users can access the global catalog server over the WAN link.

Roaming users need to contact the global catalog servers whenever they log on for the first time at any location. If the logon time over the WAN link is unacceptable, place a global catalog at a location that is visited by a large number of roaming users.

[](#enabling-universal-group-membership-caching)

## Enabling universal group membership caching {#enabling-universal-group-membership-caching .heading-anchor}

For locations that include less than 100 users and that don\'t include a large number of roaming users or applications that require a global catalog server, you can deploy domain controllers that are running Windows Server 2008 and enable universal group membership caching. Ensure that the global catalog servers aren\'t more than one replication hop from the domain controller on which universal group membership caching is enabled so that universal group information in the cache can be refreshed. For information about how universal group caching works, see the article [How the Global Catalog Works](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc737410(v=ws.10)).

For a worksheet to assist you in documenting where you plan to place global catalog servers and domain controllers with universal group caching enabled, see [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608), download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip, and open Domain Controller Placement (DSSTOPO_4.doc). See the information about locations in which you need to place global catalog servers when you deploy the forest root domain and regional domains.

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Active Directory Replication Concepts](/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts?source=recommendations)

    Learn more about: Active Directory Replication Concepts

-   [Planning Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-domain-controller-placement?source=recommendations)

    Learn more about: Planning Domain Controller Placement

-   [Read-Only DCs and the Active Directory Schema - Win32 apps](/en-us/windows/win32/ad/rodc-and-active-directory-schema?source=recommendations)

    Windows Server 2008 introduces a new type of domain controller, the Read-only Domain Controller (RODC).

-   [Active Directory Domain Services Replication Priority Boost](/en-us/windows-server/identity/ad-ds/manage/replication-priority-boost?source=recommendations)

    Learn about what the Active Directory Domain Services Replication Priority Boost feature is and how to manage it.

-   [Planning Regional Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-regional-domain-controller-placement?source=recommendations)

    Learn more about: Planning Regional Domain Controller Placement

-   [Introduction to Active Directory Replication and Topology Management Using Windows PowerShell (Level 100)](/en-us/windows-server/identity/ad-ds/manage/powershell/introduction-to-active-directory-replication-and-topology-management-using-windows-powershell--level-100-?source=recommendations)

    Learn more about: Introduction to Active Directory Replication and Topology Management Using Windows PowerShell (Level 100)

-   [Step 2 Configure the Multisite Infrastructure](/en-us/windows-server/remote/remote-access/ras/multisite/configure/step-2-configure-the-multisite-infrastructure?source=recommendations)

    Learn about how, to configure a multisite deployment, there are a number of steps required to modify network infrastructure settings.

Training

Module

[Manage AD DS domain controllers and FSMO roles - Training](/en-us/training/modules/manage-active-directory-domain-services-flexible-single-master-operation-roles/?source=recommendations)

Learn how to deploy and manage AD DS domain controllers, maintain availability with backup and recovery, manage the global catalog role, and transfer or seize FSMO roles including schema master, domain-naming master, RID master, infrastructure master, and PDC emulator.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
