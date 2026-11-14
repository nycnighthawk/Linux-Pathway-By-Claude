---
{"title": "Active Directory forest recovery - procedures", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-procedures", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory forest recovery - procedures

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This section contains procedures related to the forest recovery process.

Following is a list of procedures that are used in backing up and restoring domain controllers and Active Directory.

-   [Back up a full server](ad-forest-recovery-backing-up-a-full-server)
-   [Back up the system state data](ad-forest-recovery-backing-up-system-state)
-   [Perform a full server recovery](ad-forest-recovery-perform-full-server-recovery)
-   [Perform an authoritative synch of DFSR-replicated SYSVOL](ad-forest-recovery-authoritative-recovery-sysvol)
-   [Perform a nonauthoritative restore of Active Directory Domain Services](ad-forest-recovery-perform-nonauthoritative-restore)

These steps explain how to perform an authoritative restore of SYSVOL at the same time.

-   [Configure the DNS Server service](ad-forest-recovery-configure-dns)
-   [Remove the global catalog](ad-forest-recovery-remove-gc)
-   [Increase the value of available RID pools](ad-forest-recovery-raise-rid-pool)
-   [Invalidate the current RID pool](ad-forest-recovery-invaildate-rid-pool)
-   [Seize an operations master role](ad-forest-recovery-seizing-operations-master-role)
-   [Clean up after a restore](ad-forest-recovery-cleanup)
-   [Clean the metadata of removed writable domain controllers](ad-forest-recovery-cleaning-metadata-of-removed-dcs)
-   [Reset the computer account password of the domain controller](ad-forest-recovery-reset-computer-account-dc)
-   [Reset the krbtgt password](ad-forest-recovery-reset-the-krbtgt-password)
-   [Reset a trust password on one side of the trust](ad-forest-recovery-reset-trust)
-   [Add the global catalog](ad-forest-recovery-add-gc)
-   [Resources to verify replication is working](ad-forest-recovery-verify-replication)

[](#related-content)

## Related content {#related-content .heading-anchor}

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

-   [Active Directory Forest Recovery - Perform initial recovery](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery?source=recommendations)

    Beginning with a writeable DC in the forest root domain, complete the steps in this section in order to restore the first DC.

-   [Active Directory Forest Recovery - Determine how to recover the forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-determine-how-to-recover?source=recommendations)

    Recovering an entire Active Directory forest involves restoring at least one Domain Controller (DC) in every domain from available backup. Recovering the forest restores each domain in the forest to its state at the time of the last trusted backup. Consequently, the restore operation will result in the loss of at least the following Active Directory data\...

-   [Active Directory Forest Recovery - Recovering a single domain in a multidomain forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-recover-single-domain-multidomain-forest?source=recommendations)

    In certain scenarios, it may be necessary to recover only a single domain within a forest that has multiple domains, rather than a full forest recovery. This topic covers considerations for recovering a single domain and possible strategies for recovery.

-   [AD Forest Recovery - Steps for Restoring the forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-steps-for-restoring-the-forest?source=recommendations)

    This section provides an overview of the recommended path for recovering a forest. The forest recovery steps are described in detail later.

-   [AD Forest Recovery - Devising an AD Forest Recovery Plan](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-devise-a-plan?source=recommendations)

    Learn more about: AD Forest Recovery - Devising an AD Forest Recovery Plan

-   [Active Directory Forest Recovery - Prerequisites](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-prerequisites?source=recommendations)

    The following document discusses prerequisites that you should be familiar with before devising a forest recovery plan or attempting a recovery.

-   [AD Forest Recovery - Cleanup](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-cleanup?source=recommendations)

    Learn more about: AD Forest Recovery - Cleanup

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 07/11/2025
