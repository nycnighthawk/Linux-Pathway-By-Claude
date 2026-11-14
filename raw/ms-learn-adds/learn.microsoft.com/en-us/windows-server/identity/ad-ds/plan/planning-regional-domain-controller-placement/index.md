---
{"title": "Planning Regional Domain Controller Placement", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/planning-regional-domain-controller-placement", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Planning Regional Domain Controller Placement

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

To ensure cost efficiency, plan to place as few regional domain controllers as possible. First, review the \"Geographic Locations and Communication Links\" (DSSTOPO_1.doc) worksheet used in [Collecting Network Information](collecting-network-information) to determine whether a location is a hub.

Plan to place regional domain controllers for each domain that is represented in each hub location. After you place regional domain controllers in all hub locations, evaluate the need for placing regional domain controllers at satellite locations. Eliminating unnecessary regional domain controllers from satellite locations reduces the support costs required to maintain a remote server infrastructure.

In addition, ensure the physical security of domain controllers in hub and satellite locations so that unauthorized personnel can\'t access them. Don\'t place writable domain controllers in hub and satellite locations in which you can\'t guarantee the physical security of the domain controller. A person who has physical access to a writable domain controller can attack the system by:

-   Accessing physical disks by starting an alternate operating system on a domain controller.
-   Removing (and possibly replacing) physical disks on a domain controller.
-   Obtaining and manipulating a copy of a domain controller system state backup.

Add writable regional domain controllers only to locations in which you can guarantee their physical security.

In locations with inadequate physical security, deploying a read-only domain controller (RODC) is the recommended solution. Except for account passwords, an RODC holds all the Active Directory objects and attributes that a writable domain controller holds. However, changes can\'t be made to the database that is stored on the RODC. Changes must be made on a writable domain controller and then replicated back to the RODC.

To authenticate client logons and access to local file servers, most organizations place regional domain controllers for all regional domains that are represented in a given location. However, you must consider many variables when evaluating whether a business location requires its clients to have local authentication or the clients can rely on authentication and query over a wide area network (WAN) link. The following illustration shows how to determine whether to place domain controllers at satellite locations.

[](#onsite-technical-expertise-availability)

## Onsite technical expertise availability {#onsite-technical-expertise-availability .heading-anchor}

Domain controllers need to be managed continuously for various reasons. Place a regional domain controller only in locations that include personnel who can administer the domain controller, or be sure that the domain controller can be managed remotely.

In branch office environments with typically poor physical security and personnel with little information technology knowledge, deploying an RODC is often the recommended solution. Local administrative permissions for an RODC can be delegated to any domain user without granting that user any user rights for the domain or other domain controllers. This permits a local branch user to log on to an RODC and perform maintenance work on the server, such as upgrading a driver. However, the branch user can\'t log on to any other domain controller or perform any other administrative task in the domain. In this way, the branch user can be delegated the ability to effectively manage the RODC in the branch office without compromising the security of the rest of the domain or the forest.

[](#wan-link-availability)

## WAN link availability {#wan-link-availability .heading-anchor}

WAN links that experience frequent outages can cause significant productivity loss to users if the location doesn\'t include a domain controller that can authenticate the users. If your WAN link availability isn\'t 100 percent and your remote sites can\'t tolerate a service outage, place a regional domain controller in locations where the users require the ability to log on or exchange server access when the WAN link is down.

[](#authentication-availability)

## Authentication availability {#authentication-availability .heading-anchor}

Certain organizations, such as banks, require that users be authenticated at all times. Place a regional domain controller in a location where the WAN link availability isn\'t 100 percent but users require authentication at all times.

[](#logon-performance-over-wan-links)

## Logon performance over WAN links {#logon-performance-over-wan-links .heading-anchor}

If your WAN link availability is highly reliable, placing a domain controller at the location depends on the logon performance requirements over the WAN link. Factors that influence logon performance over the WAN include link speed and available bandwidth, number of users and usage profiles, and the amount of logon network traffic versus replication traffic.

[](#wan-link-speed-and-bandwidth-utilization)

### WAN link speed and bandwidth utilization {#wan-link-speed-and-bandwidth-utilization .heading-anchor}

The activities of a single user can congest a slow WAN link. Place a domain controller at a location if logon performance over the WAN link is unacceptable.

The average percentage of bandwidth utilization indicates how congested a network link is. If a network link has average bandwidth utilization that is greater than an acceptable value, place a domain controller at that location.

[](#number-of-users-and-usage-profiles)

### Number of users and usage profiles {#number-of-users-and-usage-profiles .heading-anchor}

The number of users and their usage profiles at a given location can help determine whether you need to place regional domain controllers at that location. To avoid productivity loss if a WAN link fails, place a regional domain controller at a location that has 100 or more users.

The usage profiles indicate how the users use the network resources. You don\'t need to place a domain controller in a location that contains only a few users who don\'t frequently access network resources.

[](#logon-network-traffic-vs-replication-traffic)

### Logon network traffic vs. replication traffic {#logon-network-traffic-vs-replication-traffic .heading-anchor}

If a domain controller isn\'t available within the same location as the Active Directory client, the client creates logon traffic on the network. The amount of logon network traffic that is created on the physical network is influenced by several factors, including group memberships; number and size of Group Policy objects (GPOs); logon scripts; and features such as offline folders, folder redirection, and roaming profiles.

On the other hand, a domain controller that is placed at a given location generates replication traffic on the network. The frequency and amount of updates made on the partitions hosted on the domain controllers influence the amount of replication traffic that is created on the network. The different types of updates that can be made on the partitions hosted on the domain controllers include adding or changing users and user attributes, changing passwords, and adding or changing global groups, printers, or volumes.

To determine if you need to place a regional domain controller at a location, compare the cost of logon traffic created by a location without a domain controller versus the cost of replication traffic created by placing a domain controller at the location.

For example, consider a network that has branch offices that are connected through slow links to the headquarters and in which domain controllers can easily be added. If the daily logon and directory lookup traffic of a few remote site users causes more network traffic than replicating all company data to the branch, consider adding a domain controller to the branch.

If reducing the cost of maintaining domain controllers is more important than network traffic, either centralize the domain controllers for that domain and don\'t place any regional domain controllers at the location or consider placing RODCs at the location.

For a worksheet to assist you in documenting the placement of regional domain controllers and the number of users for each domain that is represented in each location, see [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608), download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip, and open \"Domain Controller Placement\" (DSSTOPO_4.doc).

You\'ll need to refer to the information about locations in which you need to place regional domain controllers when you deploy regional domains. For more information about deploying regional domains, see [Deploying Windows Server 2008 Regional Domains](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755118(v=ws.10)).

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

-   [Planning Forest Root Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-forest-root-domain-controller-placement?source=recommendations)

    Learn more about: Planning Forest Root Domain Controller Placement

-   [Planning Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-domain-controller-placement?source=recommendations)

    Learn more about: Planning Domain Controller Placement

-   [Collecting Network Information](/en-us/windows-server/identity/ad-ds/plan/collecting-network-information?source=recommendations)

    Learn more about: Collecting Network Information

-   [Designing the Site Topology](/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology?source=recommendations)

    Learn more about: Designing the Site Topology

-   [Planning Global Catalog Server Placement](/en-us/windows-server/identity/ad-ds/plan/planning-global-catalog-server-placement?source=recommendations)

    Learn more about: Planning Global Catalog Server Placement

-   [Creating a Site Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-design?source=recommendations)

    Learn more about: Creating a Site Design

-   [Active Directory Replication Concepts](/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts?source=recommendations)

    Learn more about: Active Directory Replication Concepts

-   [Understanding Active Directory Site Topology](/en-us/windows-server/identity/ad-ds/plan/understanding-active-directory-site-topology?source=recommendations)

    Learn more about: Understanding Active Directory Site Topology

Training

Module

[Manage AD DS domain controllers and FSMO roles - Training](/en-us/training/modules/manage-active-directory-domain-services-flexible-single-master-operation-roles/?source=recommendations)

Learn how to deploy and manage AD DS domain controllers, maintain availability with backup and recovery, manage the global catalog role, and transfer or seize FSMO roles including schema master, domain-naming master, RID master, infrastructure master, and PDC emulator.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
