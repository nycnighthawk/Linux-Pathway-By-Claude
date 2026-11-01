---
{"title": "Creating a Site Design", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/creating-a-site-design", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Creating a Site Design

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Creating a site design involves deciding which locations will become sites, creating site objects, creating subnet objects, and associating the subnets with sites.

[](#deciding-which-locations-will-become-sites)

## Deciding which locations will become sites {#deciding-which-locations-will-become-sites .heading-anchor}

Decide which locations to create sites for as follows:

-   Create sites for all locations in which you plan to place domain controllers. Refer to the information documented in the \"Domain Controller Placement\" (DSSTOPO_4.doc) worksheet to identify locations that include domain controllers.
-   Create sites for those locations that include servers that are running applications that require a site to be created. Certain applications, such as Distributed File System Namespaces (DFSN), use site objects to locate the closest servers to clients.

Note

If your organization has multiple networks in close proximity with fast, reliable connections, you can include all of the subnets for those networks in a single Active Directory site. For example, if the round-trip return network latency between two servers in different subnets is 10 ms or less, you can include both subnets in the same Active Directory site. If the network latency between the two locations is greater than 10 ms, you should not include the subnets in a single Active Directory site. Even when latency is 10 ms or less, you may elect to deploy separate sites if you want to segment the traffic between sites for Active Directory-based applications.

-   If a site is not required for a location, add the subnet of the location to a site for which the location has the maximum wide area network (WAN) speed and available bandwidth.

Document locations that will become sites and the network addresses and subnet masks within each location. For a worksheet to assist you in documenting sites, see [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608), download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip, and open \"Associating Subnets with Sites\" (DSSTOPO_6.doc).

[](#creating-a-site-object-design)

## Creating a site object design {#creating-a-site-object-design .heading-anchor}

For every location where you have decided to create sites, plan to create site objects in Active Directory Domain Services (AD DS). Document locations that will become sites in the \"Associating Subnets with Sites\" worksheet.

For more information about how to create site objects, see the article [Create a Site](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc772304(v=ws.11)).

[](#creating-a-subnet-object-design)

## Creating a subnet object design {#creating-a-subnet-object-design .heading-anchor}

For every IP subnet and subnet mask associated with each location, plan to create subnet objects in AD DS representing all the IP addresses within the site.

When creating an Active Directory subnet object, the information about network IP subnet and subnet mask is automatically translated into the network prefix length notation format \<IP address\>/\<prefix length\>. For example, the network IP version 4 (IPv4) address 172.16.4.0 with a subnet mask 255.255.252.0 appears as 172.16.4.0/22. In addition to IPv4 addresses, Windows Server 2008 also supports IP version 6 (IPv6) subnet prefixes, for example, 3FFE:FFFF:0:C000::/64. For more information about IP subnets in each location, see the \"Locations and Subnets\" (DSSTOPO_2.doc) worksheet in [Collecting Network Information](collecting-network-information) and [Appendix A: Locations and Subnet Prefixes](appendix-a--locations-and-subnet-prefixes).

Associate each subnet object with a site object by referring to the \"Associating Subnets with Sites\" (DSSTOPO_6.doc) worksheet in \"Deciding Which Locations Will Become Sites\" section to determine which subnet is to be associated with which site. Document the Active Directory subnet object associated with each location in the \"Associating Subnets with Sites\" (DSSTOPO_6.doc) worksheet.

For more information about how to create subnet objects, see the article [Create a Subnet](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc770372(v=ws.11)).

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Creating a Site Link Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-link-design?source=recommendations)

    Learn more about: Creating a Site Link Design

-   [Creating a Site Link Bridge Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-link-bridge-design?source=recommendations)

    Learn more about: Creating a Site Link Bridge Design

-   [Designing the Site Topology](/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology?source=recommendations)

    Learn more about: Designing the Site Topology

-   [Collecting Network Information](/en-us/windows-server/identity/ad-ds/plan/collecting-network-information?source=recommendations)

    Learn more about: Collecting Network Information

-   [Appendix A - Locations and Subnet Prefixes](/en-us/windows-server/identity/ad-ds/plan/appendix-a--locations-and-subnet-prefixes?source=recommendations)

    Learn more about: Appendix A: Locations and Subnet Prefixes

-   [Active Directory Replication Concepts](/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts?source=recommendations)

    Learn more about: Active Directory Replication Concepts

-   [Planning Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-domain-controller-placement?source=recommendations)

    Learn more about: Planning Domain Controller Placement

-   [Understanding Active Directory Site Topology](/en-us/windows-server/identity/ad-ds/plan/understanding-active-directory-site-topology?source=recommendations)

    Learn more about: Understanding Active Directory Site Topology

Training

Module

[Introduction to AD DS - Training](/en-us/training/modules/introduction-to-ad-ds/?source=recommendations)

Introduction to AD DS

Certification

[Microsoft Certified: Azure Network Engineer Associate - Certifications](/en-us/credentials/certifications/azure-network-engineer-associate/?source=recommendations)

Demonstrate the design, implementation, and maintenance of Azure networking infrastructure, load balancing traffic, network routing, and more.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
