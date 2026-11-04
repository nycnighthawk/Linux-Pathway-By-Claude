---
{"title": "Determining the Cost", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/determining-the-cost", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Determining the Cost

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

You assign cost values to site links to favor inexpensive connections over expensive connections. Certain applications and services, such as Domain Controller Locator (DCLocator) and Distributed File System Namespaces (DFSN), also use cost information to locate the nearest resources. Site link cost can be used to determine which domain controller is contacted by clients in one site if the domain controller for the specified domain doesn\'t exist at that site. The client contacts the domain controller by using the site link that has the lowest cost assigned to it.

We recommend that the cost value be defined on a site-wide basis. Cost is usually based not only on the total bandwidth of the link but also on the availability, latency, and monetary cost of the link.

To determine the costs to place on site links, document the connection speed for each site link. Refer to the \"Geographic Locations and Communication Links\" (DSSTOPO_1.doc) worksheet in [Collecting Network Information](collecting-network-information) for information about the connection speed that you identified.

The following table lists the speeds for different types of networks.

  Network type                                 Speed
  -------------------------------------------- ----------------------------------------------------------------------------
  Very slow                                    56 kilobits per second (Kbps)
  Slow                                         64 Kbps
  Integrated Services Digital Network (ISDN)   64 Kbps or 128 Kbps
  Frame relay                                  Variable rate, commonly between 56 Kbps and 1.5 megabits per second (Mbps)
  T1                                           1.5 Mbps
  T3                                           45 Mbps
  10BaseT                                      10 Mbps
  Asynchronous transfer mode (ATM)             Variable rate, commonly between 155 Mbps and 622 Mbps
  100BaseT                                     100 Mbps
  Gigabit Ethernet                             1 gigabit per second (Gbps)

Use the following table to calculate the cost of each site link based on wide area network speed (WAN) link speed. For WAN link speed that isn\'t listed in the table, you can calculate a relative cost factor by dividing 1,024 by the logarithm of the available bandwidth, as measured in Kbps.

  Available bandwidth (Kbps)   Cost
  ---------------------------- -------
  9.6                          1,042
  19.2                         798
  38.4                         644
  56                           586
  64                           567
  128                          486
  256                          425
  512                          378
  1,024                        340
  2,048                        309
  4,096                        283

These costs don\'t reflect differences in reliability between network links. Set higher costs on any failure-prone network links so that you don\'t have to rely on those links for replication. By setting higher site link costs, you can control replication failover when a site link fails.

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

-   [Creating a Site Link Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-link-design?source=recommendations)

    Learn more about: Creating a Site Link Design

-   [Creating a Site Link Bridge Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-link-bridge-design?source=recommendations)

    Learn more about: Creating a Site Link Bridge Design

-   [Determining the Schedule](/en-us/windows-server/identity/ad-ds/plan/determining-the-schedule?source=recommendations)

    Learn more about: Determining the Schedule

-   [Creating a Site Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-design?source=recommendations)

    Learn more about: Creating a Site Design

-   [Setting Site Link Properties](/en-us/windows-server/identity/ad-ds/plan/setting-site-link-properties?source=recommendations)

    Learn more about: Setting Site Link Properties

-   [Troubleshooting Active Directory Replication Problems](/en-us/windows-server/identity/ad-ds/manage/troubleshoot/troubleshooting-active-directory-replication-problems?source=recommendations)

    Learn more about: Troubleshooting Active Directory Replication Problems

-   [Designing the Site Topology](/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology?source=recommendations)

    Learn more about: Designing the Site Topology

-   [Determining the Interval](/en-us/windows-server/identity/ad-ds/plan/determining-the-interval?source=recommendations)

    Learn more about: Determining the Interval

------------------------------------------------------------------------

-    Last updated on 05/12/2025
