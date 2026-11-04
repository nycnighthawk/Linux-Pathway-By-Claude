---
{"title": "Setting Site Link Properties", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/setting-site-link-properties", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Setting Site Link Properties

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Intersite replication occurs according to the properties of the connection objects. When the Knowledge Consistency Checker (KCC) creates connection objects, it derives the replication schedule from properties of the site link objects. Each site link object represents the wide area network (WAN) connection between two or more sites.

Setting site link object properties includes the following steps:

-   Determining the cost that is associated with that replication path. The KCC uses cost to determine the least expensive route for replication between two sites that replicate the same directory partition.

-   Determining the schedule that defines the times during which intersite replication can occur.

-   Determining the replication interval that defines how frequently replication should occur during the times when replication is allowed, as defined in the schedule.

[](#in-this-guide)

## In this guide {#in-this-guide .heading-anchor}

-   [Determining the Cost](determining-the-cost)

-   [Determining the Schedule](determining-the-schedule)

-   [Determining the Interval](determining-the-interval)

Reading mode disabled

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3 hidden=""}

------------------------------------------------------------------------

-    Last updated on 05/12/2025
