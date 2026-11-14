---
{"title": "DC Locator performance counters", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/dc-locator-performance-counters", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# DC Locator performance counters

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Beginning with Windows Server 2025, you can use Active Directory Domain Service Domain Controller (DC) Locator performance counters to monitor the performance of DC locator clients. These counters provide insights into the performance of DC locator requests per second by type, average success and failure latency, and other metrics.

DC location refers to the algorithm the client machine uses to find a suitable domain controller (DC). DC location is a critical baseline functionality in all enterprise environments. To learn more about the DC location process, see [Active Directory DC locator changes](manage/dc-locator-changes).

There are the following domain controller locator performance counter sets:

-   DC Locator (Client)
-   DC Locator (DC)
-   DC Locator (Netlogon)

You can access these performance counters using Performance Monitor (`perfmon.exe`).

[](#dc-locator-client)

## DC Locator (Client) {#dc-locator-client .heading-anchor}

DC Locator (Client) performance counters measure per process running on the local client machine. You can break down requests based on which flags are used, such as the number of requests per second with the GC flag required, KDC flag required, and so on. Examples of available counters include Average Failure Latency (secs), Average Success Latency (secs), Failures/sec, Successes/sec, and Total Active Site Name Queries/sec.

The following table shows the client counters that can be added when using the DC Locator (Client) performance counter set.

  Counter name                                     Description
  ------------------------------------------------ -------------------------------------------------------------------------------------------------------------
  `Flags: DS Required (W2K+) Requests/sec`         The number of requests per second that have the Windows 2000 and later Directory Service flag set
  `Flags: DS Required (WS2008+) Requests/sec`      The number of requests per second that have the Windows Server 2008 and later Directory Service flag set
  `Flags: DS Required (WS2012 R2+) Requests/sec`   The number of requests per second that have the Windows Server 2012 R2 and later Directory Service flag set
  `Flags: DS Required (WS2012+) Requests/sec`      The number of requests per second that have the Windows Server 2012 and later Directory Service flag set
  `Flags: DS Required (WS2016+) Requests/sec`      The number of requests per second that have the Windows Server 2016 and later Directory Service flag set
  `Flags: Force Rediscovery Requests/sec`          The number of requests per second that have the force rediscovery flag set
  `Flags: GC Required Requests/sec`                Number of requests per second that have the Global Catalog flag set
  `Flags: KDC Required Requests/sec`               Number of requests per second that have the Key Distribution Center flag set
  `Flags: KeyList Support Required Requests/sec`   Number of requests per second that have the KeyList support flag set
  `Flags: PDC Required Requests/sec`               Requests per second that have the Primary Domain Controller flag set
  `Flags: Time Server Required Requests/sec`       Requests per second that have the Time Server flag set
  `Flags: TryNextClosestSite Requests/sec`         Requests per second that have the `TryNextClosestSite` flag set
  `Flags: Writable Required Requests/sec`          Requests per second that have the Writable flag set
  `Requests: Average Failure Latency (secs)`       The average latency of failed requests in seconds
  `Requests: Average Success Latency (secs)`       The average latency of successful requests in seconds
  `Requests: Failures/sec`                         Number of failed requests per second
  `Requests: Successes/sec`                        Number of successful requests per second
  `Requests: Total Active`                         The total number of active requests per second
  `Site Name Queries/sec`                          Number of site name queries per second

[](#dc-locator-dc)

## DC Locator (DC) {#dc-locator-dc .heading-anchor}

DC Locator (DC) counters exist only on the domain controller. The DC Locator (DC) counters measured the number of incoming LDAP and mailslot pings and requests received for locating domain controllers.

The following table shows the server-side counters that can be added when using the DC Locator (DC) performance counter set.

  Counter name                                    Description
  ----------------------------------------------- -----------------------------------------------------------
  `Pings: Active Mailslot Pings`                  Returns the number of active Mailslot pings
  `Pings: Active UDP LDAP Pings`                  Returns the number of active UDP LDAP pings
  `Pings: Average Mailslot Ping Latency (secs)`   Returns the average latency of Mailslot pings in seconds
  `Pings: Average UDP LDAP Ping Latency (secs)`   Returns the average latency of IJDP LDAP pings in seconds
  `Pings: Mailslot Pings Received/sec`            Returns the number of Mailslot pings received per second
  `Pings: UDP LDAP Pings Received/sec`            Returns the number of UDP LDAP pings received per second

[](#dc-locator-netlogon)

## DC Locator (Netlogon) {#dc-locator-netlogon .heading-anchor}

The Netlogon service downloads and caches naming information about domains and child domains in all trusting forests. The DC Locator (Netlogon) performance counters are similar to DC Locator (Client) counters except the counter instances are organized by name lookup. There are also a few more cache-based counters available, such as Cache: Hits/sec and Cache: Misses/sec. You can use these objects to see how many times a lookup is resolved from the cache or over the wire.

The following table shows the counters that can be added when using the DC Locator (Netlogon) performance counter set.

  Counter name                                     Description
  ------------------------------------------------ -------------------------------------------------------------------------------------------------------------
  `Cache: Hits/sec`                                Returns the number of cache hits per second
  `Cache: Misses/sec`                              Returns the number of cache misses per second
  `DNS Query Failures/sec`                         Returns the number of DNS query failures per second
  `Flags: DS Required (W2K+) Requests/sec`         The number of requests per second that have the Windows 2000 and later Directory Service flag set
  `Flags: DS Required (WS2008+) Requests/sec`      The number of requests per second that have the Windows Server 2008 and later Directory Service flag set
  `Flags: DS Required (WS2012 R2+) Requests/sec`   The number of requests per second that have the Windows Server 2012 R2 and later Directory Service flag set
  `Flags: DS Required (WS2012+) Requests/sec`      The number of requests per second that have the Windows Server 2012 and later Directory Service flag set
  `Flags: DS Required (WS2016+) Requests/sec`      The number of requests per second that have the Windows Server 2016 and later Directory Service flag set
  `Flags: Force Rediscovery Requests/sec`          The number of requests per second that have the force rediscovery flag set
  `Flags: GC Required Requests/sec`                Number of requests per second that have the Global Catalog flag set
  `Flags: KDC Required Requests/sec`               Number of requests per second that have the Key Distribution Center flag set
  `Flags: KeyList Support Required`                Number of requests per second that have the KeyList support flag set
  `Flags: PDC Required Requests/sec`               Requests per second that have the Primary Domain Controller flag set
  `Flags: Time Server Required Requests/sec`       Requests per second that have the Time Server flag set
  `Flags: TryNextClosestSite Requests/sec`         Requests per second that have the `TryNextClosestSite` flag set
  `Flags: Writable Required Requests/sec`          Requests per second that have the Writable flag set
  `Pings: Mailslot Pings Sent/sec`                 Returns the number of Mailslot pings sent per second
  `Pings: UDP Pings Sent/sec`                      Returns the number of UDP pings sent per second
  `Requests: Average Failure Latency (secs)`       Returns the average latency of failed requests in seconds
  `Requests: Average Success Latency (secs)`       Returns the average latency of successful requests in seconds
  `Requests: Failures/sec`                         Returns the number of failed requests per second
  `Requests: Rejected/sec`                         Returns the number of rejected requests per second
  `Requests: Successes/sec`                        Returns the number of successful requests per second
  `Requests: Total Active`                         Returns the total number of active requests
  `UDP Ports Opened`                               Returns the number of UDP ports opened

[](#next-steps)

## Next steps {#next-steps .heading-anchor}

-   [How domain controllers are located in Windows](/en-us/troubleshoot/windows-server/active-directory/how-domain-controllers-are-located)

-   [Active Directory DC locator changes](manage/dc-locator-changes)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Troubleshoot domain controller location issues in Windows - Windows Server](/en-us/troubleshoot/windows-server/windows-security/troubleshoot-domain-controller-location-issues?source=recommendations)

    Helps troubleshoot domain controller location issues in Windows.

-   [Locating Active Directory Domain Controllers in Windows and Windows Server](/en-us/windows-server/identity/ad-ds/manage/dc-locator?source=recommendations)

    Learn how domain controllers are located in Windows and Windows Server using the DC locator algorithm.

-   [Offline defragmentation of Active Directory database - Windows Server](/en-us/troubleshoot/windows-server/active-directory/ad-database-offline-defragmentation?source=recommendations)

    Describes how to How to perform offline defragmentation of the Active Directory database.

-   [Errors when you run DCDIAG commands - Windows Server](/en-us/troubleshoot/windows-server/active-directory/dcdiag-commands-running-errors?source=recommendations)

    Fixes errors that occur when you run DCDIAG.EXE /E or /A or /C commands.

-   [Domain members fail authentication when DC is shut down - Windows Server](/en-us/troubleshoot/windows-server/windows-security/cannot-authenticate-users-shut-down-domain-controller?source=recommendations)

    This article fixes an issue where the application can\'t authenticate users when you shut down a Domain Controller.

-   [Advanced Active Directory Replication and Topology Management Using Windows PowerShell (Level 200)](/en-us/windows-server/identity/ad-ds/manage/powershell/advanced-active-directory-replication-and-topology-management-using-windows-powershell--level-200-?source=recommendations)

    Learn more about: Advanced Active Directory Replication and Topology Management Using Windows PowerShell (Level 200)

-   [Troubleshoot domain controller deployment - Windows Server](/en-us/troubleshoot/windows-server/active-directory/troubleshoot-domain-controller-deployment?source=recommendations)

    Provides information about troubleshooting domain controller deployment.

-   [Verify that SRV Domain Name System (DNS) records have been created - Windows Server](/en-us/troubleshoot/windows-server/networking/verify-srv-dns-records-have-been-created?source=recommendations)

    Describes how to verify Service Location (SRV) locator resource records for a domain controller after you install the Active Directory directory service.

------------------------------------------------------------------------

-    Last updated on 10/25/2024
