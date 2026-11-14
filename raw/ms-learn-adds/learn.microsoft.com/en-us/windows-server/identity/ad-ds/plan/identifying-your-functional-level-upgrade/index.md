---
{"title": "Identifying your functional level upgrade", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/identifying-your-functional-level-upgrade", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Identifying your functional level upgrade

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

In this article learn about the process for upgrading your domain and forest functional levels in Active Directory Domain Services.

Before you can raise domain and forest functional levels, evaluate your current environment and identify your target functional level. Assess your current environment by identifying:

-   The domains in your forest

-   The domain controllers that are located in each domain

-   The operating system and updates that each domain controller is running

-   When you plan to upgrade the domain controllers.

If you plan to retire a domain controller, make sure that you understand the full impact that doing so will have on your environment.

Consider the following items when assessing your current environment:

-   Your domain controllers meet or exceed the hardware requirements for the operating system that you plan to upgrade to. To learn more about hardware requirements, see [Perform a Feature Update of Windows Server](../../../get-started/upgrade-in-place).

-   Your Active Directory domain is operational and free from replication errors. To learn more about replication errors, see [Diagnose Active Directory replication failures](/en-us/troubleshoot/windows-server/active-directory/diagnose-replication-failures).

-   Identify all your domain controllers hosting the Global Catalog (GC) and Flexible Single Master Operation (FSMO) roles. Create and verify backups of these Active Directory Domain Services domain controllers before making changes.

-   Check for any incompatible software or applications that might prevent you from upgrading to a newer version of Windows Server.

-   Check for removed features to make sure that none are being used. To learn more about removed features, see [Features removed or no longer developed in Windows Server](../../../get-started/removed-deprecated-features-windows-server).

Documenting this information can help you identify the steps to take to ensure that you have a fully functional Windows Server environment.

After you assess your current environment, identify the target functional level upgrade. To learn more about the functional levels, see [Forest and Domain Functional Levels](../active-directory-functional-levels).

This article discusses the following upgrade options:

-   Upgrade to a Windows Server 2025 forest

-   Upgrade to a Windows Server 2016 forest

[](#upgrade-functional-levels-to-windows-server-2025)

## Upgrade functional levels to Windows Server 2025 {#upgrade-functional-levels-to-windows-server-2025 .heading-anchor}

In an environment consisting of only Windows Server 2025-based domain controllers, the functional levels default to Windows Server 2025. If your Active Directory Domain Services environment contains a mix of Windows Server releases, your functional levels might be set to a lower level.

To use all the forest-level and domain-level features in Windows Server 2025, you have to upgrade to the Windows Server 2025 forest and domain functional levels. To upgrade your domain controllers to Windows Server 2025, you must meet the following prerequisites:

-   For new Active Directory forests, the minimum domain and forest functional level that can be set is Windows Server 2016.

-   Existing domains must be at the Windows Server 2016 domain and forest functional levels to promote a Windows Server 2025 domain controller.

You can upgrade the functional levels by using the following options:

-   Set up a new Active Directory domain with the new domain and forest functional levels when promoting the first Domain Controller for the new domain

-   Introduce new Windows Server 2025 domain controllers into the forest, then retire or upgrade all domain controllers running an older version of Windows Server. After you\'ve upgraded or retired all domain controllers running an older version of Windows Server, you can raise the domain and forest functional levels to Windows Server 2025.

-   Perform a Feature Update of all existing domain controllers running an older version of Windows Server. To learn more about performing a Feature Update, see [Perform a Feature Update of Windows Server](../../../get-started/upgrade-in-place). Then raise the domain and forest functional levels to Windows Server 2025.

A Windows Server 2025 domain controller can only be added to an existing domain that is running Windows Server 2016 Domain Functional Level or newer version. You must also ensure that all hardware and software requirements for Windows Server 2025 are met.

[](#upgrade-functional-levels-in-a-windows-server-2016-active-directory-forest)

## Upgrade functional levels in a Windows Server 2016 Active Directory forest {#upgrade-functional-levels-in-a-windows-server-2016-active-directory-forest .heading-anchor}

In an environment that consisting of Windows Server 2016, 2019 and 2022-based domain controllers, the functional levels are set by default to the Windows Server 2016 domain and forest functional level. The Windows Server 2016 domain and forest functional level is the most recent functional level for Windows Server 2019 and 2022. The functional level remains at these levels until you raise them manually after an upgrade to Windows Server 2025 or later.

To use all the forest-level and domain-level features in Windows Server 2016, you have to upgrade to the Windows Server 2016 forest and domain functional levels. To upgrade your domain controllers to Windows Server 2016, you must meet the following prerequisites:

-   All domain controllers must be running Windows Server 2016, Windows Server 2019, or Windows Server 2022.

-   The Active Directory forest functional level must be at least Windows Server 2012.

There are two upgrade options to choose from, as follows:

-   Set up a new Active Directory domain with the new domain and forest functional levels when promoting the first Domain Controller for the new domain

-   Introduce new Windows Server 2016, 2019 or 2022 domain controllers into the forest, then retire or upgrade all domain controllers running an older version of Windows Server. After you\'ve upgraded or retired all domain controllers running an older version of Windows Server, you can raise the domain and forest functional levels to Windows Server 2016.

-   Perform a feature update of all existing domain controllers running an older version of Windows Server. To learn more about performing a feature update, see [Perform a Feature Update of Windows Server](../../../get-started/upgrade-in-place). Then raise the domain and forest functional levels to Windows Server 2016.

[](#upgrade-functional-levels-in-a-previous-version-of-windows-server)

## Upgrade functional levels in a previous version of Windows Server {#upgrade-functional-levels-in-a-previous-version-of-windows-server .heading-anchor}

If you\'re looking to identify functional levels for a previous version of Windows Server, see [Identifying your functional level upgrade](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc754209(v=ws.10)).

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

-   [How to raise Active Directory domain and forest functional levels - Windows Server](/en-us/troubleshoot/windows-server/active-directory/raise-active-directory-domain-forest-functional-levels?source=recommendations)

    Describes how to raise Active Directory domain and forest functional levels.

-   [Raise Domain and Forest Functional Levels in AD DS on Windows Server](/en-us/windows-server/identity/ad-ds/plan/raise-domain-forest-functional-levels?source=recommendations)

    Learn how to raise domain and forest functional levels in Active Directory Domain Services on Windows Server.

-   [Active Directory Domain Services Functional Levels](/en-us/windows-server/identity/ad-ds/active-directory-functional-levels?source=recommendations)

    Discover the capabilities of Active Directory Domain Services functional levels and learn how they impact domain controllers and Windows Server compatibility.

-   [Database 32k pages for Active Directory on Windows Server](/en-us/windows-server/identity/ad-ds/32k-pages-optional-feature?source=recommendations)

    Learn about Database 32k page optional feature for Active Directory Domain Services and Active Directory Lightweight Domain Services on Windows Server.

-   [Upgrade domain controllers to a newer version of Windows Server](/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers?source=recommendations)

    This article describes how to upgrade from an earlier version of Windows Server to a later version.

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 10/25/2024
