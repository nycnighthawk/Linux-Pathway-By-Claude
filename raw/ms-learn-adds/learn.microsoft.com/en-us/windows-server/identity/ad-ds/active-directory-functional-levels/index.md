---
{"title": "Active Directory Domain Services functional levels", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Domain Services functional levels

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Functional levels determine the available Active Directory Domain Services (AD DS) domain or forest capabilities. They also determine which Windows Server operating systems you can run on domain controllers in the domain or forest. However, functional levels don\'t affect which operating systems you can run on workstations and member servers joined to the domain or forest. This article describes which functioning levels are compatible with which versions of Windows Server.

When you deploy AD DS, set the domain and forest functional levels to the highest value that your environment can support in order to use as many AD DS features as possible. When you deploy a new forest, you need to set both the forest and domain functional levels. You can set a domain functional level higher than the forest functional level. You can\'t set a domain functional level lower than the forest functional level.

[](#windows-server-functional-level-interoperability)

## Windows Server functional level interoperability {#windows-server-functional-level-interoperability .heading-anchor}

The following interoperability matrix summarizes which Windows Server versions you can run as domain controllers for each currently supported AD DS forest and domain functional level.

  Windows Server version (DC)   Windows Server 2025 functional level   Windows Server 2016 functional level   Windows Server 2012 R2 functional level
  ----------------------------- -------------------------------------- -------------------------------------- -----------------------------------------
  Windows Server 2025           ✅ Supported                           ✅ Supported                           ❌ Not supported
  Windows Server 2022           ❌ Not supported                       ✅ Supported                           ✅ Supported
  Windows Server 2019           ❌ Not supported                       ✅ Supported                           ✅ Supported
  Windows Server 2016           ❌ Not supported                       ✅ Supported                           ✅ Supported
  Windows Server 2012 R2        ❌ Not supported                       ❌ Not supported                       ✅ Supported

✅ Supported means you can run a domain controller with that Windows Server release at the specified forest and domain functional level; ❌ Not supported means you cannot.

Note

Windows Server 2019 and Windows Server 2022 use Windows Server 2016 as the most recent functional level. For earlier functional levels (for example Windows Server 2008 R2), see [Understanding Active Directory Domain Services (AD DS) Functional Levels](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754918(v=ws.10)).

[](#windows-server-2025-functional-levels)

### Windows Server 2025 functional levels {#windows-server-2025-functional-levels .heading-anchor}

You can use the following operating systems as domain controllers (DCs) with the Windows Server 2025 forest and domain functional level.

-   Windows Server 2025

[](#windows-server-2025-forest-and-domain-functional-level-features)

#### Windows Server 2025 forest and domain functional level features {#windows-server-2025-forest-and-domain-functional-level-features .heading-anchor}

The Windows Server 2025 domain functional level includes all features available in earlier domain functional levels, but also has the following new features:

-   Database 32k pages optional feature. To learn more about using the 32k database page size, see [Database 32k pages for Active Directory](/en-us/windows-server/identity/ad-ds/32k-pages-optional-feature).

To learn more about new features, see [What\'s new in Windows Server 2025](../../get-started/whats-new-windows-server-2025).

Note

Windows Server 2019 and Windows Server 2022 use Windows Server 2016 as the most recent functional levels.

[](#windows-server-2016-functional-levels)

### Windows Server 2016 functional levels {#windows-server-2016-functional-levels .heading-anchor}

You can use the following operating systems as domain controllers (DCs) with the Windows Server 2016 forest and domain functional level.

-   Windows Server 2025
-   Windows Server 2022
-   Windows Server 2019
-   Windows Server 2016

Note

Domains must use DFSR as the engine to replicate SYSVOL. To learn more about migrating to DFSR, see [Streamlined Migration of FRS to DFSR SYSVOL](https://techcommunity.microsoft.com/blog/filecab/streamlined-migration-of-frs-to-dfsr-sysvol/425405). Windows Server 2016 is the last Windows Server release that supports the File Replication Service (FRS). See [Windows Server version 1709 no longer supports FRS](/en-us/troubleshoot/windows-server/networking/windows-server-version-1709-no-longer-supports-frs) for information on how to work around this issue.

[](#windows-server-2016-forest-and-domain-functional-level-features)

#### Windows Server 2016 forest and domain functional level features {#windows-server-2016-forest-and-domain-functional-level-features .heading-anchor}

All default Active Directory features in earlier forest functional levels are available, plus the following features:

-   [Privileged access management (PAM) using Microsoft Identity Manager (MIM)](../whats-new-active-directory-domain-services#privileged-access-management)

All default Active Directory features in earlier domain functional levels are available, plus the following features:

-   DCs can support automatic rolling of the New Technology LAN Manager (NTLM) and other password-based secrets on a user account configured to require public key infrastructure (PKI) authentication. This configuration is also known as *Smart card required for interactive logon*.

-   DCs can support allowing network NTLM when a user is restricted to specific domain-joined devices.

-   Kerberos clients successfully authenticating with the PKInit Freshness Extension get the fresh public key identity security identifier (SID).

    For more information, see [What\'s New in Kerberos Authentication](../../get-started/whats-new-in-windows-server-2016#kerberos-authentication).

[](#windows-server-2012-r2-functional-levels)

### Windows Server 2012 R2 functional levels {#windows-server-2012-r2-functional-levels .heading-anchor}

You can use the following operating systems as domain controllers (DCs) with the Windows Server 2012 R2 forest and domain functional level.

-   Windows Server 2022
-   Windows Server 2019
-   Windows Server 2016
-   Windows Server 2012 R2

[](#windows-server-2012-r2-forest-and-domain-functional-level-features)

#### Windows Server 2012 R2 forest and domain functional level features {#windows-server-2012-r2-forest-and-domain-functional-level-features .heading-anchor}

All default Active Directory features, all features from the Windows Server 2012 domain functional level, plus the following features:

-   DC-side protections for Protected Users. When Protected Users authenticate to a Windows Server 2012 R2 domain, they\'re no longer able to:

    -   Authenticate with NTLM authentication.

    -   Use DES or RC4 cipher suites in Kerberos preauthentication.

    -   Be delegated with unconstrained or constrained delegation.

    -   Renew user tickets (TGTs) beyond the initial four hour lifetime.

-   Authentication policies

    -   New forest-based authentication policies can be applied to accounts. The policies can control which hosts an account can sign on from, and apply access control conditions for authentication to services running as an account.

-   Authentication policy silos

    -   A new forest-based Active Directory object to be used to classify accounts for authentication policies or for authentication isolation. The new object can create a relationship between user, managed service, and computer accounts.

[](#functional-and-domain-levels-in-previous-versions-of-windows-server)

### Functional and domain levels in previous versions of Windows Server {#functional-and-domain-levels-in-previous-versions-of-windows-server .heading-anchor}

If you want to identify functional levels for a previous version of Windows Server, such as Windows Server 2008 R2, see [Understanding Active Directory Domain Services (AD DS) Functional Levels](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754918(v=ws.10)).

[](#related-content)

## Related content {#related-content .heading-anchor}

-   Use the PowerShell command [Set-ADForestMode](/en-us/powershell/module/activedirectory/set-adforestmode) to raise the forest functional level.

-   Use the PowerShell command [Set-ADDomainMode](/en-us/powershell/module/activedirectory/set-addomainmode) to raise the domain functional level.

-   To learn more about raising the domain and forest functional levels, see [How to raise Active Directory domain and forest functional levels](/en-us/troubleshoot/windows-server/active-directory/raise-active-directory-domain-forest-functional-levels).

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Raise Domain and Forest Functional Levels in AD DS on Windows Server](/en-us/windows-server/identity/ad-ds/plan/raise-domain-forest-functional-levels?source=recommendations)

    Learn how to raise domain and forest functional levels in Active Directory Domain Services on Windows Server.

-   [Learn about upgrading your domain and forest functional levels in Active Directory Domain Services.](/en-us/windows-server/identity/ad-ds/plan/identifying-your-functional-level-upgrade?source=recommendations)

    Upgrade your domain and forest functional level in Active Director Domain Services for Windows Server

-   [How to raise Active Directory domain and forest functional levels - Windows Server](/en-us/troubleshoot/windows-server/active-directory/raise-active-directory-domain-forest-functional-levels?source=recommendations)

    Describes how to raise Active Directory domain and forest functional levels.

-   [Database 32k pages for Active Directory on Windows Server](/en-us/windows-server/identity/ad-ds/32k-pages-optional-feature?source=recommendations)

    Learn about Database 32k page optional feature for Active Directory Domain Services and Active Directory Lightweight Domain Services on Windows Server.

-   [Upgrade domain controllers to a newer version of Windows Server](/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers?source=recommendations)

    This article describes how to upgrade from an earlier version of Windows Server to a later version.

-   [Enable Database 32k pages optional feature in Active Directory Domain Services on Windows Server](/en-us/windows-server/identity/ad-ds/enable-32k-pages-optional-feature?source=recommendations)

    Learn how-to enable the Database 32k pages optional feature in Active Directory Domain Services and how to enable the optional feature using PowerShell.

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 10/30/2025
