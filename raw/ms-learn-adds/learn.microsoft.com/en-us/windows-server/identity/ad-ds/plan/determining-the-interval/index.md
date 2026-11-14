---
{"title": "Determining the Interval", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/determining-the-interval", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Determining the Interval

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

You must set the site link replication interval property to indicate how frequently you want replication to occur during the times when the schedule allows replication. For example, if the schedule allows replication between 02:00 hours and 04:00 hours, and the replication interval is set for 30 minutes, replication can occur up to four times during the scheduled time. The default replication interval is 180 minutes, or 3 hours. The minimum interval is 15 minutes.

Consider the following criteria to determine how often replication occurs within the schedule window:

-   A small interval decreases latency but increases the amount of wide area network (WAN) traffic.

-   To keep domain directory partitions up to date, low latency is preferred.

With a store-and-forward replication strategy, it is difficult to determine just how long a directory update might take to be replicated to every domain controller. To provide a conservative estimate of maximum latency, perform these tasks:

-   Create a table of all the sites on your network, as shown in the following example:

      Sites              Seattle   Boston   Los Angeles   New York   Washington, D.C.
      ------------------ --------- -------- ------------- ---------- ------------------
      Seattle            0.25                                        
      Boston                       0.25                              
      Los Angeles                           0.25                     
      New York                                            0.25       
      Washington, D.C.                                               0.25

    A worst-case latency within a site is estimated to be 15 minutes.

-   From the replication schedule, determine the maximum replication latency that is possible on any site link that connects two hub sites.

    For example, if replication occurs between Seattle and New York every three hours, the maximum delay for replication between these sites is three hours. If the replication delay between New York and Seattle is the longest scheduled delay among all hub sites, the maximum latency between all hubs is three hours.

-   For each hub site, create a table of the maximum latencies between the hub site and any of its satellite sites.

    For example, if replication occurs between New York and Washington, D.C., every four hours and this is the longest replication delay between New York and any of its satellite sites, the maximum latency between New York and its satellites is four hours.

-   Combine these maximum latencies to determine the maximum latency for the entire network.

    For example, if the maximum latency between Seattle and its satellite site in Los Angeles is one day, the maximum replication latency for this set of links (Washington, D.C.-New York-Seattle-Los Angeles) is 31 hours, that is, 4 (Washington, D.C.-New York) + 3 (New York-Seattle) + 24 (Seattle-Los Angeles), as shown in the following table.

      Sites              Seattle   Boston   Los Angeles   New York   Washington, D.C.
      ------------------ --------- -------- ------------- ---------- ------------------
      Seattle            0.25      4+3      24.00         3.00       4+3
      Boston                       0.25     4+3+24        4.00       4.00
      Los Angeles                           0.25          24 + 3     24+3+4
      New York                                            0.25       4.00
      Washington, D.C.                                               0.25

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

-   [Modify the default intra-site DC replication interval - Windows Server](/en-us/troubleshoot/windows-server/active-directory/modify-default-intra-site-dc-replication-interval?source=recommendations)

    Describes how to modify the default intra-site domain controller replication interval.

-   [Active Directory Replication Concepts](/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts?source=recommendations)

    Learn more about: Active Directory Replication Concepts

-   [Troubleshooting Active Directory Replication Problems](/en-us/windows-server/identity/ad-ds/manage/troubleshoot/troubleshooting-active-directory-replication-problems?source=recommendations)

    Learn more about: Troubleshooting Active Directory Replication Problems

-   [Determining the Cost](/en-us/windows-server/identity/ad-ds/plan/determining-the-cost?source=recommendations)

    Learn more about assigning cost values to links

-   [Avoid registering unwanted Network Interface Controllers (NICs) in Domain Name System (DNS) - Windows Server](/en-us/troubleshoot/windows-server/networking/unwanted-nic-registered-dns-mulithomed-dc?source=recommendations)

    This article provides a solution to an issue where unwanted NICs are registered in DNS on a multihomed domain controller.

-   [Duplicate Active Directory replication connections are created - Windows Server](/en-us/troubleshoot/windows-server/active-directory/duplicate-active-directory-replication-connections?source=recommendations)

    Provides a solution to an issue where duplicate Active Directory replication connections are created for one or more domain controllers across one or more sites.

Training

Module

[Implement Hyper-V Replica - Training](/en-us/training/modules/implement-hyper-v-replica/?source=recommendations)

Implement Hyper-V Replica

------------------------------------------------------------------------

-    Last updated on 05/12/2025
