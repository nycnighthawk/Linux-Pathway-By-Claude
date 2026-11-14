---
{"title": "Simplified Administration Appendix", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/simplified-administration-appendix", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Simplified Administration Appendix

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

-   [Server Manager Add Servers Dialog (Active Directory)](simplified-administration-appendix#BKMK_AddServers)

-   [Server Manager Remote Server Status](simplified-administration-appendix#BKMK_ServerMgrStatus)

-   [Windows PowerShell Module Loading](simplified-administration-appendix#BKMK_PSLoadModule)

-   [RID Issuance Hotfixes for Previous Operating Systems](simplified-administration-appendix#BKMK_Rid)

-   [Ntdsutil.exe Install from Media Changes](simplified-administration-appendix#BKMK_IFM)

[](#BKMK_AddServers)

## Server Manager Add Servers Dialog (Active Directory) {#BKMK_AddServers .heading-anchor}

The **Add Servers** dialog allows searching Active Directory for servers, by operating system, using wildcards, and by location. The dialog also allows using DNS queries by fully qualified domain name or prefix name. These searches use native DNS and LDAP protocols implemented through .NET, not AD Windows PowerShell against the AD Management Gateway through SOAP - meaning that the domain controllers contacted by Server Manager can even run Windows Server 2003. You can also import a file with server names for provisioning purposes.

The Active Directory search uses the following LDAP filters:

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
(&(ObjectCategory=computer)

(&(ObjectCategory=computer)(cn=dc*)(OperatingSystemVersion=6.2*))

(&(ObjectCategory=computer)(OperatingSystemVersion=6.1*))

(&(ObjectCategory=computer)(OperatingSystemVersion=6.0*))

(&(ObjectCategory=computer)(|(OperatingSystemVersion=5.2*)(OperatingSystemVersion=5.1*)))
```

The Active Directory search returns the following attributes:

``` {.inner-focus data-language=""}
( dnsHostName )( operatingSystem )( cn )
```

[](#BKMK_ServerMgrStatus)

## Server Manager Remote Server Status {#BKMK_ServerMgrStatus .heading-anchor}

Server Manager tests remote server accessibility using Address Routing Protocol. Any servers not responding to ARP requests aren\'t listed, even if they are in the pool.

If ARP responds, then DCOM and WMI connections are made to the server to return status information. If RPC, DCOM, and WMI are unreachable, server manager can\'t fully manage the server.

[](#BKMK_PSLoadModule)

## Windows PowerShell Module Loading {#BKMK_PSLoadModule .heading-anchor}

Windows PowerShell 3.0 implements dynamic module loading. Using the **Import-Module** cmdlet is typically no longer required; instead, simply invoking the cmdlet, alias, or function automatically loads the module.

To see loaded modules, use the **Get-Module** cmdlet.

``` {.inner-focus data-language=""}
Get-Module
```

To see all installed modules with their exported functions and cmdlets, use:

``` {.inner-focus data-language=""}
Get-Module -ListAvailable
```

The main case for using the **import-module** command is when you need access to the \"AD:\" Windows PowerShell virtual drive and nothing else has already loaded the module. For example, using the following commands:

``` {.inner-focus data-language=""}
import-module activedirectory
cd ad:
dir
```

[](#BKMK_Rid)

## RID Issuance Hotfixes for Previous Operating Systems {#BKMK_Rid .heading-anchor}

See [An update is available to detect and prevent too much consumption of the global RID pool on a domain controller that is running Windows Server 2008 R2](https://support.microsoft.com/kb/2618669).

[](#BKMK_IFM)

## Ntdsutil.exe Install from Media Changes {#BKMK_IFM .heading-anchor}

Windows Server 2012 adds two additional options to the Ntdsutil.exe command-line tool for the **IFM (IFM Media Creation)** menu. These allow you to create IFM stores without first performing an offline defrag of the exported NTDS.DIT database file. When disk space isn\'t a premium, this saves time creating the IFM.

The following table describes the two new menu items:

  Menu Item                        Explanation
  -------------------------------- ----------------------------------------------------------------------------------------------
  Create Full NoDefrag %s          Create IFM media without defragmenting for a full AD DC or an AD/LDS instance into folder %s
  Create Sysvol Full NoDefrag %s   Create IFM media with SYSVOL and without defragmenting for a full AD DC into folder %s

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

-   [AD DS Simplified Administration](/en-us/windows-server/identity/ad-ds/manage/ad-ds-simplified-administration?source=recommendations)

    Learn more about: AD DS Simplified Administration

-   [Install Active Directory Domain Services on Windows Server](/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-?source=recommendations)

    Learn more about how to install Active Directory Domain Services in Windows Server using PowerShell, or Server Manager.

-   [Install a Windows Server 2012 Active Directory Read-Only Domain Controller (RODC) (Level 200)](/en-us/windows-server/identity/ad-ds/deploy/rodc/install-a-windows-server-2012-active-directory-read-only-domain-controller--rodc---level-200-?source=recommendations)

    This article explains how to create a staged RODC account and then attach a server to that account during RODC installation. This article also explains how to install an RODC without performing a staged installation.

-   [Upgrading AD RMS to Windows Server 2016](/en-us/windows-server/identity/ad-rms/adrms-deploy?source=recommendations)

    Learn more about: Upgrading AD RMS to Windows Server 2016

-   [Install a Replica Windows Server 2012 Domain Controller in an Existing Domain (Level 200)](/en-us/windows-server/identity/ad-ds/deploy/install-a-replica-windows-server-2012-domain-controller-in-an-existing-domain--level-200-?source=recommendations)

    Learn more about: Install a Replica Windows Server 2012 Domain Controller in an Existing Domain (Level 200)

-   [Active Directory overview - Windows Server](/en-us/troubleshoot/windows-server/active-directory/active-directory-overview?source=recommendations)

    Overview of Active Directory troubleshooting articles.

-   [Safely virtualizing Active Directory Domain Services (AD DS)](/en-us/windows-server/identity/ad-ds/introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100?source=recommendations)

    USN Rollback and safe virtualization of Active Directory

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
