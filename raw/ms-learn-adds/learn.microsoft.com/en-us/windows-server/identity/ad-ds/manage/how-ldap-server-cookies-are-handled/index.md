---
{"title": "How LDAP server cookies are handled", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/how-ldap-server-cookies-are-handled", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# How LDAP server cookies are handled

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

In LDAP, some queries result in a large result set. Such queries pose certain challenges to Windows Server.

Collecting and building these large result sets is significant work. Many of the attributes need to be converted from an internal representation to the LDAP wire representation. For many attributes, a conversion from an internal, often binary, format needs to happen to a text-based UTF-8 format in the LDAP response frame.

Another challenge is that result sets with tens of thousands of objects require enormous amounts of storage space, easily several hundred Mega-Bytes. These then require lots of virtual address space. The transfer over network encounters issues because the whole effort is lost when the TCP session breaks down in transit.

These capacity and logistic issues encouraged the Microsoft LDAP developers to create an LDAP extension known as \"Paged Query\". Paged Query implements an LDAP control to separate one huge query into chunks of smaller result sets. Paged Query is an RFC standard: [RFC 2696](https://datatracker.ietf.org/doc/rfc2696/).

[](#cookie-handling-on-client)

## Cookie handling on client {#cookie-handling-on-client .heading-anchor}

The Paged Query method uses the page size either set by the client or through a [LDAP Policy](https://support.microsoft.com/kb/315071/en-us) (\"MaxPageSize\"). The client always needs to enable paging by sending an LDAP control.

When working on a query with many results, at some point the maximum number of objects allowed is reached. The LDAP server packages up the response message and adds a cookie that contains information it needs to later continue the search.

The client application must treat the cookie as an opaque blob. It can retrieve the object count in the response and can continue the search based on the presence of the cookie. To continue the search. the client sends the same query to the LDAP server, including the cookie value from the previous response.

If the number of objects doesn\'t fill a page, the LDAP query is complete, and the response contains no page cookie. If the server doesn\'t return a cookie, the client must consider the paged search to be successfully complete.

If the server returns an error, the client must consider the paged search to be unsuccessful. Retrying the search results in restarting the search from the first page.

[](#server-side-cookie-handling)

## Server-side Cookie handling {#server-side-cookie-handling .heading-anchor}

The Windows Server returns the cookie to the client and sometimes stores information related to the cookie on the server. This information is stored on the server in a cache and is subject to certain limits.

In this case, the cookie sent to the client by the Server is also used by the server to lookup the information from the cache on the Server. When the client continues the paged search, Windows Server uses the client cookie and any related information from the server cookie cache to continue the search. If the server can\'t find related cookie information from the server cache due to any reason, the search is discontinued and error is returned to the client.

[](#how-the-cookie-pool-is-managed)

## How the cookie pool is managed {#how-the-cookie-pool-is-managed .heading-anchor}

Obviously, the LDAP server is serving more than one client at a time. Also, more than one client at a time can launch queries that require the use of server cookie cache. Therefore in the Windows Server implementation there\'s a tracking of cookie pool usage and limits are put into place so the cookie pool isn\'t taking up too much resources. Administrators can set limits using the following settings in LDAP Policy. The defaults and explanations are as follows.

**MinResultSets: 4**

The LDAP server doesn\'t look at the maximum pool size, if there are fewer than MinResultSets entries in the server cookie cache.

**MaxResultSetSize: 262,144 bytes**

The total cookie cache size on the server must not exceed the maximum of MaxResultSetSize in bytes. If it does, cookies starting from the oldest are deleted until the pool is smaller than MaxResultSetSize bytes or less than MinResultSets cookies are in the pool. When using the default settings, the LDAP server considers a pool of 450KB to be OK if there are only 3 cookies stored.

**MaxResultSetsPerConn: 10**

The LDAP server allows no more than MaxResultSetsPerConn cookies per LDAP connection in the pool.

[](#handling-deleted-cookies)

## Handling deleted cookies {#handling-deleted-cookies .heading-anchor}

The removal of cookie information from LDAP Server cache doesn\'t result in an immediate error for applications in all cases. Applications may restart the paged search from the start and complete it on another attempt. Some applications have this kind of a retry mechanism to add robustness.

Some applications can go through a page search and never complete it. This uncompleted search can leave entries in the LDAP server cookie cache, which are handled through the mechanism described earlier. This mechanism is essential to free up memory on the server for active LDAP searches.

What happens when such a cookie is deleted on the server and the client continues the search with this cookie handle? The LDAP Server doesn\'t find the cookie in the server cookie cache and returns an error for the query. The error response is similar to:

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
00000057: LdapErr: DSID-xxxxxxxx, comment: Error processing control, data 0, v1db1
```

Note

The hexadecimal value behind \"DSID\" will vary depending on the build version of the LDAP server binaries.

[](#reporting-on-the-cookie-pool)

## Reporting on the cookie pool {#reporting-on-the-cookie-pool .heading-anchor}

The LDAP Server has the ability to log events through category `16 Ldap Interface` in the [NTDS diagnostics key](https://support.microsoft.com/kb/314980/en-us). If you set this category to `2`, you can get the following events:

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
Log Name:      Directory Service
Source:        Microsoft-Windows-ActiveDirectory_DomainService
Event ID:      2898
Task Category: LDAP Interface
Level:         Information
Description:
Internal event: The LDAP server has reached the limit of the number of Result Sets it will maintain for a single connection.  A stored Result Set will be discarded.  This will result in a client being unable to continue a paged LDAP search.
Maximum number of Result Sets allowed per LDAP connection:
10
Current number of Result Sets for this LDAP connection:
11

User Action
The client should consider a more efficient search filter.  The limit for Maximum Result Sets per Connection may also be increased.
```

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
Log Name:      Directory Service
Source:        Microsoft-Windows-ActiveDirectory_DomainService
Event ID:      2899
Task Category: LDAP Interface
Level:         Information
Description:
Internal event: The LDAP server has exceeded the limit of the LDAP Maximum Result Set Size. A stored Result Set will be discarded. This will result in a client being unable to continue a paged LDAP search.

Number of result sets currently stored:
4
Current Result Set Size:
263504
Maximum Result Set Size:
262144
Size of single Result Set being discarded:
40876
User Action
The client should consider a more efficient search filter.  The limit for Maximum Result Set Size may also be increased.
```

The events signal that a stored cookie was removed. It **doesn\'t** mean a client has seen the LDAP error, but only that the LDAP Server has reached the administration limits for the cache. In some cases, an LDAP client may have abandoned the paged search and may never see the error.

[](#monitoring-the-cookie-pool)

## Monitoring the cookie pool {#monitoring-the-cookie-pool .heading-anchor}

If you never experience LDAP search errors in your domain, you may never need to monitor the LDAP server page search cookie pool. In case you see LDAP page search related errors in your environment, you may have an issue with the cookie pool administrator limits.

Events 2898 and 2899 are the only ways to know that the LDAP server has reached the administrator limits. When you experience that LDAP queries error because of the control processing error, you should consider increasing limits on one or more of the LDAP Policy settings. You can find the limits in the [How the cookie pool is managed](#how-the-cookie-pool-is-managed) section, depending on which event you\'re getting.

If you\'re seeing event 2898 on your DC/LDAP Server, we recommend you set MaxResultSetsPerConn to 25. More than 25 parallel paged searches on a single LDAP connection isn\'t usual. If you continue to see event 2898, consider investigating your LDAP client application, which encounters the error. The suspicion would be that it somehow gets stuck retrieving more paged results, leaves the cookie pending and restarts a new query. See whether the application would at some point have sufficient cookies for its purposes. You can also increase the value of MaxResultSetsPerConn beyond 25. When you see events 2899 logged on your domain controllers, the plan would be different. If your DC/LDAP server runs on a machine with sufficient memory (several GBs of free memory), we recommend you set the MaxResultsetSize on the LDAP server to \>=250MB. This limit is large enough to accommodate large volumes of LDAP page searches even on very large directories.

If you\'re still seeing events 2899 with a pool of 250MB or more, you\'re likely having many clients with very high number of objects returned, queried in a frequent manner. The data you can gather with the [Active Directory Data Collector Set](/en-us/archive/blogs/askds/son-of-spa-ad-data-collector-sets-in-win2008-and-beyond) can help you find repetitive paged queries that keep your LDAP Servers busy. These queries show with a number of \"Entries returned\" that matches the size of the page used.

If possible, you should review the application design, and implement a different approach with a lower frequency, data volume and/or fewer client instances querying this data. If there are applications for which you have source code access, see [Creating efficient AD-Enabled Applications](/en-us/previous-versions/ms808539(v=msdn.10)) for help with understanding the optimal way for applications to access AD.

If the query behavior can\'t be changed, one approach is also adding more replicated instances of the naming contexts needed and to redistribute the clients. Replicating the instance and distributing the client can reduce the load on the individual LDAP Servers.

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

-   [Active Directory Domain Services Replication Priority Boost](/en-us/windows-server/identity/ad-ds/manage/replication-priority-boost?source=recommendations)

    Learn about what the Active Directory Domain Services Replication Priority Boost feature is and how to manage it.

-   [Managing RID Issuance](/en-us/windows-server/identity/ad-ds/manage/managing-rid-issuance?source=recommendations)

    Learn more about: Managing RID Issuance

-   [Directory Services component updates](/en-us/windows-server/identity/ad-ds/manage/component-updates/directory-services-component-updates?source=recommendations)

    Learn more about: Directory Services component updates

-   [Control Access Rights (AD DS) - Win32 apps](/en-us/windows/win32/ad/control-access-rights?source=recommendations)

    All objects in Active Directory Domain Services support a standard set of access rights defined in the ADS\\\_RIGHTS\\\_ENUM enumeration.

-   [Advanced Active Directory Replication and Topology Management Using Windows PowerShell (Level 200)](/en-us/windows-server/identity/ad-ds/manage/powershell/advanced-active-directory-replication-and-topology-management-using-windows-powershell--level-200-?source=recommendations)

    Learn more about: Advanced Active Directory Replication and Topology Management Using Windows PowerShell (Level 200)

-   [Active Directory Replication and Topology Management Using Windows PowerShell](/en-us/windows-server/identity/ad-ds/manage/powershell/active-directory-replication-and-topology-management-using-windows-powershell?source=recommendations)

    Learn more about: Active Directory Replication and Topology Management Using Windows PowerShell

-   [Locating Active Directory Domain Controllers in Windows and Windows Server](/en-us/windows-server/identity/ad-ds/manage/dc-locator?source=recommendations)

    Learn how domain controllers are located in Windows and Windows Server using the DC locator algorithm.

-   [Active Directory Replication Concepts](/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts?source=recommendations)

    Learn more about: Active Directory Replication Concepts

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
