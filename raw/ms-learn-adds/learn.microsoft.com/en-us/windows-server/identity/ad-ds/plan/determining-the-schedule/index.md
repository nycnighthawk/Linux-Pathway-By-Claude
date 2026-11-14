---
{"title": "Determining the Schedule", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/determining-the-schedule", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Determining the Schedule

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

You can control site link availability by setting a schedule for site links. When replication between two sites traverses multiple site links, the intersection of the replication schedules on all the relevant links determines the connection schedule between the two sites.

To plan for setting the site link schedule, create two overlapping schedules between site links that contain domain controllers that directly replicate with each other. Use the default (100-percent available) schedule on those links unless you want to block replication traffic during peak hours. By blocking replication, you give priority to other traffic, but you also increase replication latency.

Domain controllers store time in Coordinated Universal Time (UTC). Time settings in site link object schedules conform to the local time of the site and computer on which the schedule is set. When a domain controller contacts a computer that is in a different site and time zone, the schedule on the domain controller displays the time setting according to the local time for the site of the computer.

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

-   [Determining the Interval](/en-us/windows-server/identity/ad-ds/plan/determining-the-interval?source=recommendations)

    Learn more about: Determining the Interval

-   [Setting Site Link Properties](/en-us/windows-server/identity/ad-ds/plan/setting-site-link-properties?source=recommendations)

    Learn more about: Setting Site Link Properties

-   [Determining the Cost](/en-us/windows-server/identity/ad-ds/plan/determining-the-cost?source=recommendations)

    Learn more about assigning cost values to links

-   [Modify the default intra-site DC replication interval - Windows Server](/en-us/troubleshoot/windows-server/active-directory/modify-default-intra-site-dc-replication-interval?source=recommendations)

    Describes how to modify the default intra-site domain controller replication interval.

-   [Active Directory Replication Concepts](/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts?source=recommendations)

    Learn more about: Active Directory Replication Concepts

------------------------------------------------------------------------

-    Last updated on 05/12/2025
