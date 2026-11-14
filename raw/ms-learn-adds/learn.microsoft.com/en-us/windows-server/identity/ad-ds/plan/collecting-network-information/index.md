---
{"title": "Collecting Network Information", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/collecting-network-information", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Collecting Network Information

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

The first step in designing an effective site topology in Active Directory Domain Services (AD DS) is to consult your organization\'s networking group to collect information and communicate with them regularly about your physical network topology.

[](#creating-a-location-map)

## Creating a location map {#creating-a-location-map .heading-anchor}

Create a location map that represents the physical network infrastructure of your organization. On the location map, identify the geographic locations that contain groups of computers with internal connectivity of 10 megabits per second (Mbps) or higher (local area network (LAN) speed or better).

[](#listing-communication-links-and-available-bandwidth)

## Listing communication links and available bandwidth {#listing-communication-links-and-available-bandwidth .heading-anchor}

After creating a location map, document the type of communication link, its link speed, and the available bandwidth between each location. Obtain a wide area network (WAN) topology from your networking group. For a list of common WAN circuit types and their bandwidths, see \"Determining the cost\" section in [Creating a Site Link Design](creating-a-site-link-design). You will need this information to create site links later in the site topology design process.

Bandwidth refers to the amount of data that you can transmit across a communication channel in a given amount of time. Available bandwidth refers to the amount of bandwidth actually available for use by AD DS. You can obtain available bandwidth information from your networking group, or you can analyze traffic on each link by using a protocol analyzer such as Network Monitor. For information about installing Network Monitor, see the article [Monitoring network traffic](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc783075(v=ws.10)).

Document each location and the other locations that are linked to it. In addition, record the type of communication link and its available bandwidth. For a worksheet to assist you in listing communication links and available bandwidth, see [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608), download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip, and open \"Geographic Locations and Communication Links\" (DSSTOPO_1.doc).

[](#listing-ip-subnets-within-each-location)

## Listing IP subnets within each location {#listing-ip-subnets-within-each-location .heading-anchor}

After you document the communication links and the available bandwidth between each location, record the IP subnets within each location. If you do not already know the subnet mask and IP address within each location, consult your networking group.

AD DS associates a workstation with a site by comparing the workstation\'s IP address with the subnets that are associated with each site. As you add domain controllers to a domain, AD DS also examines their IP addresses and places them in the most appropriate site.

For a worksheet to assist you in listing the IP subnets within each location, see [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608), download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip, and open \"Locations and Subnets\" (DSSTOPO_2.doc).

Note

In addition to IP version 4 (IPv4) addresses, Windows Server also supports IP version 6 (IPv6) subnet prefixes. For a worksheet to assist you in listing the IPv6 subnet prefixes, see [Appendix A: Locations and subnet prefixes](appendix-a--locations-and-subnet-prefixes).

[](#listing-domains-and-number-of-users-for-each-location)

## Listing domains and number of users for each location {#listing-domains-and-number-of-users-for-each-location .heading-anchor}

The number of users for each regional domain that is represented in a location is one of the factors that determine the placement of regional domain controllers and global catalog servers, which is the next step in the site topology design process. For example, plan to place a regional domain controller in a location that contains more than 100 regional domain users so they can still log on to the domain if the WAN link fails.

Record the locations, the domains that are represented in each location, and the number of users for each domain that is represented in each location. For a worksheet to assist you in listing the domains and the number of users that are represented in each location, see [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608), download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip, and open \"Domains and Users in Each Location\" (DSSTOPO_3.doc).

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

-   [Creating a Site Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-design?source=recommendations)

    Learn more about: Creating a Site Design

-   [Creating a Site Link Bridge Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-link-bridge-design?source=recommendations)

    Learn more about: Creating a Site Link Bridge Design

-   [Designing the Site Topology](/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology?source=recommendations)

    Learn more about: Designing the Site Topology

-   [Creating a Site Link Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-link-design?source=recommendations)

    Learn more about: Creating a Site Link Design

-   [Planning Regional Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-regional-domain-controller-placement?source=recommendations)

    Learn more about: Planning Regional Domain Controller Placement

-   [Planning Domain Controller Placement](/en-us/windows-server/identity/ad-ds/plan/planning-domain-controller-placement?source=recommendations)

    Learn more about: Planning Domain Controller Placement

-   [Site functions](/en-us/windows-server/identity/ad-ds/plan/site-functions?source=recommendations)

    Learn more about various site functions in AD DS

-   [Appendix A - Locations and Subnet Prefixes](/en-us/windows-server/identity/ad-ds/plan/appendix-a--locations-and-subnet-prefixes?source=recommendations)

    Learn more about: Appendix A: Locations and Subnet Prefixes

Training

Module

[Introduction to AD DS - Training](/en-us/training/modules/introduction-to-ad-ds/?source=recommendations)

Introduction to AD DS

Certification

[Microsoft Certified: Azure Network Engineer Associate - Certifications](/en-us/credentials/certifications/azure-network-engineer-associate/?source=recommendations)

Demonstrate the design, implementation, and maintenance of Azure networking infrastructure, load balancing traffic, network routing, and more.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
