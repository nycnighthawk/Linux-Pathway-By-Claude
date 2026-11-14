---
{"title": "AD DS Troubleshooting", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-ds-troubleshooting", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# AD DS Troubleshooting

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This section includes troubleshooting recommendations and procedures for diagnosing and fixing problems that may occur during Active Directory replication. It focuses on how to respond to Directory Service event log entries and how to interpret messages that tools such as Repadmin.exe and Dcdiag.exe might report.

Repadmin.exe and Dcdiag.exe are available on all domain controllers that run Windows Server 2012 R2 or later versions. For more information about how to use these tools to troubleshoot problems, see the following articles.

-   [Configuring a Computer for Troubleshooting Active Directory](troubleshoot/configuring-a-computer-for-troubleshooting)
-   [Troubleshooting Active Directory Replication Problems](troubleshoot/troubleshooting-active-directory-replication-problems)

Another useful technology is Event Tracing for Windows (ETW). You can use ETW to troubleshoot LDAP communications among the domain controllers. For more information, see [Using ETW to troubleshoot LDAP connections](troubleshoot/troubleshoot-ldap-using-etw).

You can also install Remote Server Administration Tools (RSAT) on a member server that is running Windows 10. For information about how to install RSAT, see [Remote Server Administration Tools](../../../remote/remote-server-administration-tools).

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

-   [Troubleshooting Active Directory Replication Problems](/en-us/windows-server/identity/ad-ds/manage/troubleshoot/troubleshooting-active-directory-replication-problems?source=recommendations)

    Learn more about: Troubleshooting Active Directory Replication Problems

-   [Active Directory Replication Concepts](/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts?source=recommendations)

    Learn more about: Active Directory Replication Concepts

-   [Additional Resources](/en-us/windows-server/identity/additional-resources_12?source=recommendations)

    Learn more about: Additional Resources

-   [Configuring a Computer for Troubleshooting](/en-us/windows-server/identity/ad-ds/manage/troubleshoot/configuring-a-computer-for-troubleshooting?source=recommendations)

    Learn more about: Configuring a Computer for Troubleshooting

-   [Global Catalog - Win32 apps](/en-us/windows/win32/ad/global-catalog?source=recommendations)

    A Domain run by Active Directory Domain Services can consist of many partitions or naming contexts.

-   [Active Directory Domain Services Replication Priority Boost](/en-us/windows-server/identity/ad-ds/manage/replication-priority-boost?source=recommendations)

    Learn about what the Active Directory Domain Services Replication Priority Boost feature is and how to manage it.

-   [Use Ntdsutil to manage AD files - Windows Server](/en-us/troubleshoot/windows-server/active-directory/use-ntdsutil-manage-ad-files?source=recommendations)

    Describes how to manage the Active Directory database file, Ntds.dit, from the command line.

-   [Using ETW to troubleshoot LDAP connections](/en-us/windows-server/identity/ad-ds/manage/troubleshoot/troubleshoot-ldap-using-etw?source=recommendations)

    How to turn on and use ETW to trace LDAP connections between AD DS domain controllers.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
