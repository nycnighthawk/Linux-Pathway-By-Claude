---
{"title": "Active Directory Forest Recovery - Clean the metadata of removed writable domain controllers", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-cleaning-metadata-of-removed-dcs", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Clean the metadata of removed writable domain controllers {#active-directory-forest-recovery----clean-the-metadata-of-removed-writable-domain-controllers}

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Metadata cleanup removes Active Directory data that identifies a DC to the replication system.

Note that outside of a Forest Recovery, metadata cleanup is part of the demotion process of domain controllers, however, when they aren\'t reachable anymore, this process also applies.

Use the following procedure to delete the DC objects for DCs that you plan to add back to the network by reinstalling AD DS.

[](#delete-a-domain-controller-using-active-directory-users-and-computers)

## Delete a domain controller using Active Directory Users and Computers {#delete-a-domain-controller-using-active-directory-users-and-computers .heading-anchor}

When you use the version of Active Directory Users and Computers or Active Directory Administrative Center in Remote Server Administration Tools (RSAT), metadata cleanup is performed automatically when you delete the DC object. The server object and the computer object are also deleted automatically.

As an alternative, you can also use Active Directory Sites and Services in RSAT to delete a DC object. If you use Active Directory Sites and Services, you must delete the associated server object and NTDS Settings object before you can delete the DC object. Metadata cleanup can also be done through command line, via NTDSUtil or using PowerShell with Active Directory Module.

For information about installing RSAT, see the article [Remote Server Administration Tools](/en-us/windows-server/remote/remote-server-administration-tools).

**To delete a domain controller object using Active Directory Users and Computers in RSAT**

1.  Select **Start**, select **Administrative Tools**, and then select **Active Directory Users and Computers**.
2.  In the console tree, double-click the domain container, and then double-click the **Domain Controllers** organizational unit (OU).
3.  In the details pane, right-click the DC that you want to delete, and then select **Delete**.
4.  Select **Yes** to confirm the deletion. Select the **This Domain Controller is permanently offline and can no longer be demoted using the Active Directory Domain Services Installation Wizard (DCPROMO)** check box and select **Delete**.
5.  If the DC was a global catalog server, select **Yes** confirm that the deletion.

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

-   [AD Forest Recovery - Adding the GC](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-add-gc?source=recommendations)

    Learn more about: AD Forest Recovery - Adding the GC

-   [AD Forest Recovery - Seizing an Operations Master Role](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-seizing-operations-master-role?source=recommendations)

    Learn more about: AD Forest Recovery - Seizing an operations master role

-   [AD Forest Recovery - Remove the global catalog](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-remove-gc?source=recommendations)

    Learn more about: AD Forest Recovery - Removing the global catalog

-   [Clean up AD DS server metadata](/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup?source=recommendations)

    Use built-in tools to clean up metadata from removed domain controllers

-   [Can\'t promote a domain controller to a global catalog server - Windows Server](/en-us/troubleshoot/windows-server/active-directory/cannot-promote-dc-to-global-catalog-server?source=recommendations)

    Describes a problem where you can\'t promote a Windows Server-based domain controller to be a global catalog server.

-   [DC rename doesn\'t rename all AD DFSR \`SYSVOL\` objects - Windows Server](/en-us/troubleshoot/windows-server/active-directory/sysvol-msdfsr-member-container-not-updated?source=recommendations)

    Fixes an issue where the \`SYSVOL\` msDFSR-Member container used by DFS Replication isn\'t updated.

-   [Active Directory Forest Recovery - Performing a nonauthoritative restore of Active Directory Domain Services](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-nonauthoritative-restore?source=recommendations)

    The following procedures use the wbadmin.exe to perform a nonauthoritative restore of Active Directory or Active Directory Domain Services (AD DS). If you\'re using a different backup solution or if you intend to complete the authoritative restore of SYSVOL later in the forest recovery process\...

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

------------------------------------------------------------------------

-    Last updated on 11/01/2024
