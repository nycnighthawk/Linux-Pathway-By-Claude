---
{"title": "Active Directory Forest Recovery - Cleanup", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-cleanup", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Cleanup

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Perform the following post recovery steps as needed:

[](#revert-to-the-original-dns-configuration)

## Revert to the original DNS configuration {#revert-to-the-original-dns-configuration .heading-anchor}

After the entire forest is recovered, you can revert to the original DNS configuration, including configuration of the preferred and alternate DNS servers on each of the DCs. After the DNS servers are configured as they were before the malfunction, their previous name resolution capabilities will be restored. Delete any DNS records for DCs that haven\'t been recovered.

[](#delete-windows-internet-name-service-wins-records)

## Delete Windows Internet Name Service (WINS) records {#delete-windows-internet-name-service-wins-records .heading-anchor}

Delete Windows Internet Name Service (WINS) records for all DCs that haven\'t been recovered.

[](#transfer-operations-master-roles-to-other-dcs)

## Transfer operations master roles to other DCs {#transfer-operations-master-roles-to-other-dcs .heading-anchor}

You can transfer the operations master roles to other DCs in the domain or forest and add more global catalog servers based on the configuration before the failure.

[](#recreate-missing-objects)

## Recreate missing objects {#recreate-missing-objects .heading-anchor}

Because the entire forest is restored to a previous state, any objects (such as users and computers) that were added and all updates (such as password changes) that were made to existing objects after this point are lost. Therefore, you should recreate these missing objects and reapply the missing updates as appropriate.

[](#restore-outgoing-domains-and-trusts)

## Restore outgoing domains and trusts {#restore-outgoing-domains-and-trusts .heading-anchor}

You might also need to restore outgoing trusts with external domains and forests, because these external trust relationships aren\'t restored automatically from backups.

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

-   [AD Forest Recovery - Redeploy remaining DCs](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-restore-additional-dcs?source=recommendations)

    Learn more about: AD Forest Recovery - Redeploy remaining DCs

-   [Active Directory Forest Recovery - Recovering a single domain in a multidomain forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-recover-single-domain-multidomain-forest?source=recommendations)

    In certain scenarios, it may be necessary to recover only a single domain within a forest that has multiple domains, rather than a full forest recovery. This topic covers considerations for recovering a single domain and possible strategies for recovery.

-   [Active Directory Forest Recovery - Virtualization](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-virtualization?source=recommendations)

    Virtualized domain controller (DC) cloning simplifies and expedites the process for installing additional virtualized DCs in a domain, especially in centralized locations such as datacenters where several DCs run on hypervisors. After you restore one virtual DC in each domain from backup, additional DCs in each domain can be rapidly brought online by using the virtualized DC cloning process. You can prepare the first virtualized DC that you recover, shut it down, and then copy that virtual hard disk as many

-   [Active Directory Forest Recovery - Perform initial recovery](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery?source=recommendations)

    Beginning with a writeable DC in the forest root domain, complete the steps in this section in order to restore the first DC.

-   [Active Directory Forest Recovery - Determine how to recover the forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-determine-how-to-recover?source=recommendations)

    Recovering an entire Active Directory forest involves restoring at least one Domain Controller (DC) in every domain from available backup. Recovering the forest restores each domain in the forest to its state at the time of the last trusted backup. Consequently, the restore operation will result in the loss of at least the following Active Directory data\...

-   [Active Directory Forest Recovery - Identify the problem](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-identify-the-problem?source=recommendations)

    When symptoms of a forest-wide failure appear, such as in event logs or other monitoring solutions, work with Microsoft Support to determine the cause of the failure and evaluate any possible remedies.

-   [Active Directory Forest Recovery - Prerequisites](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-prerequisites?source=recommendations)

    The following document discusses prerequisites that you should be familiar with before devising a forest recovery plan or attempting a recovery.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
