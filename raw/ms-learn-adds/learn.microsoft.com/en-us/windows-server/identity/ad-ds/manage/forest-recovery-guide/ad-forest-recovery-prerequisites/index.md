---
{"title": "Active Directory Forest Recovery - Prerequisites", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-prerequisites", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Prerequisites

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

The following document discusses prerequisites that you should be familiar with before devising a forest recovery plan or attempting a recovery.

[](#assumptions)

## Assumptions {#assumptions .heading-anchor}

1.  You have worked with a Microsoft Support professional and:

    -   Determined the cause of the forest-wide failure. This guide doesn\'t suggest the causes for failure nor does it recommend procedures to prevent failure.
    -   Evaluated possible remedies.
    -   Concluded, in consultation with Microsoft Support, that restoring the whole forest to its state before the failure is the best way to recover from the failure. In many cases, forest recovery should be the last option.

2.  You have followed the Microsoft best-practice recommendations for using Active Directory--integrated Domain Name System (DNS). Specifically, there should be an Active Directory--integrated DNS zone for each Active Directory domain.

    If this isn\'t the case, you can still use the basic principles of this guide to perform forest recovery. However, you\'ll need to take specific measures for DNS recovery based on your own environment. For more information about using Active Directory--integrated DNS, see [Creating a DNS Infrastructure Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-dns-infrastructure-design).

3.  You may have a special configuration for the handling of Domain Controller disk volumes in your physical or virtual hosting, such as solutions to protect access to disk volumes, like BitLocker. As part of the procedure you may require access to emergency situation information like BitLocker Recovery keys. Ensure this information is available when needed during recovery.

4.  Although this guide is intended as a generic guide for forest recovery, not all possible scenarios are covered. For instance, there\'s a Server Core version, which is a version of Windows Server without a desktop experience. Although it\'s possible to recover a forest consisting of just DCs that run Server Core, this guide has no detailed instructions. However, based on the guidance discussed here, you\'ll be able to design the required command-line actions yourself.

Note

Although the objectives of this guide are to recover the forest and maintain or restore full DNS functionality, recovery can result in a DNS configuration that is changed from the configuration before the failure. After the forest is recovered, you can revert to the original DNS configuration. The recommendations in this guide do not describe how to configure DNS servers to perform name resolution of other portions of the corporate namespace where there are DNS zones that are not stored in AD DS.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

[](#you-are-familiar-with-active-directory-concepts)

### You are familiar with Active Directory concepts {#you-are-familiar-with-active-directory-concepts .heading-anchor}

Before you begin planning for recovery of an Active Directory forest, you should be familiar with the following:

-   Fundamental Active Directory concepts
-   The importance of operations master roles (formerly known as flexible singles master operations or FSMO) including:
    -   Forest-wide Operation Master Roles:
        -   Schema master
        -   Domain naming master
    -   Domain-wide Operation Master Roles:
        -   Relative ID (RID) master
        -   Primary domain controller (PDC) emulator master
        -   Infrastructure master

[](#you-have-a-documented-recovery-plan-with-procedures)

### You have a documented recovery plan with procedures {#you-have-a-documented-recovery-plan-with-procedures .heading-anchor}

You should have a documented recovery plan with procedures for AD DS domain/forest recoveries, object/subtree recoveries, and SYSVOL recoveries that have been tested in a lab environment using production backups. The recovery procedures should be vetted on a routine basis (for example, annually) and the documentation updated as required by OS upgrades, architectural changes to the AD DS environment, or any other changes that ensure the procedures are kept up to date. For more information and guidance on these procedures, refer to the [AD Forest Recovery -- Procedures](ad-forest-recovery-procedures) section of this guide.

Tip

Microsoft offers the **Active Directory Recovery Execution Service (ADRES)** service to assist customers with the development of this documentation/procedure. Contact your Customer Success Account Management (CSAM) for details.

[](#you-have-backed-up-and-restored-ad-ds-and-sysvol-in-a-lab-environment)

### You have backed up and restored AD DS and SYSVOL in a lab environment {#you-have-backed-up-and-restored-ad-ds-and-sysvol-in-a-lab-environment .heading-anchor}

You should have backed up and restored AD DS and SYSVOL in a lab environment on a regular basis. For more information, see [AD Forest Recovery - Backing up a full server](ad-forest-recovery-backing-up-a-full-server). and [Performing Nonauthoritative Restore of Active Directory Domain Services](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc816627(v=ws.10)).

[](#next-steps)

## Next steps {#next-steps .heading-anchor}

-   [AD Forest Recovery - Prerequisites](ad-forest-recovery-prerequisites)
-   [AD Forest Recovery - Devise a custom forest recovery plan](ad-forest-recovery-devise-a-plan)
-   [AD Forest Recovery - Steps to restore the forest](ad-forest-recovery-steps-for-restoring-the-forest)
-   [AD Forest Recovery - Identify the problem](ad-forest-recovery-identify-the-problem)
-   [AD Forest Recovery - Determine how to recover](ad-forest-recovery-determine-how-to-recover)
-   [AD Forest Recovery - Perform initial recovery](ad-forest-recovery-perform-initial-recovery)
-   [AD Forest Recovery - Procedures](ad-forest-recovery-procedures)
-   [AD Forest Recovery - Frequently Asked Questions (FAQ)](ad-forest-recovery-faq)
-   [AD Forest Recovery - Recover a single domain within a multidomain forest](ad-forest-recovery-recover-single-domain-multidomain-forest)
-   [AD Forest Recovery - Redeploy remaining DCs](ad-forest-recovery-restore-additional-dcs)
-   [AD Forest Recovery - Virtualization](ad-forest-recovery-virtualization)
-   [AD Forest Recovery - Cleanup](ad-forest-recovery-cleanup)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [AD Forest Recovery - Devising an AD Forest Recovery Plan](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-devise-a-plan?source=recommendations)

    Learn more about: AD Forest Recovery - Devising an AD Forest Recovery Plan

-   [Active Directory Forest Recovery - Determine how to recover the forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-determine-how-to-recover?source=recommendations)

    Recovering an entire Active Directory forest involves restoring at least one Domain Controller (DC) in every domain from available backup. Recovering the forest restores each domain in the forest to its state at the time of the last trusted backup. Consequently, the restore operation will result in the loss of at least the following Active Directory data\...

-   [Active Directory Forest Recovery Guide](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-guide?source=recommendations)

    This guide contains recommendations for recovering an Active Directory forest if a forest-wide failure renders all DCs in the forest incapable of functioning normally.

-   [AD Forest Recovery - Steps for Restoring the forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-steps-for-restoring-the-forest?source=recommendations)

    This section provides an overview of the recommended path for recovering a forest. The forest recovery steps are described in detail later.

-   [Active Directory Forest Recovery - Perform initial recovery](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery?source=recommendations)

    Beginning with a writeable DC in the forest root domain, complete the steps in this section in order to restore the first DC.

-   [Active Directory Forest Recovery - Procedures](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-procedures?source=recommendations)

    View a list of procedures that are used in backing up and restoring domain controllers and Active Directory.

-   [Active Directory Forest Recovery - Identify the problem](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-identify-the-problem?source=recommendations)

    When symptoms of a forest-wide failure appear, such as in event logs or other monitoring solutions, work with Microsoft Support to determine the cause of the failure and evaluate any possible remedies.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 11/01/2024
