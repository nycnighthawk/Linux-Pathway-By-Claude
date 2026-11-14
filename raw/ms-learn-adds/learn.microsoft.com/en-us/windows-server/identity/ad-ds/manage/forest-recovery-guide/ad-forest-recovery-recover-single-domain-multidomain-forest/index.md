---
{"title": "Active Directory Forest Recovery - Recover a single domain in a multidomain forest", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-recover-single-domain-multidomain-forest", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Recover a single domain in a multidomain forest

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

In certain scenarios, it may be necessary to recover only a single domain within a forest that has multiple domains, rather than a full forest recovery. This topic covers considerations for recovering a single domain and possible strategies.

Similar to the forest recovery process, you restore one or more DCs from backup in the domain and perform metadata cleanup of remaining DCs. New domain controllers are then added by joining new members, installing AD DS roles and promoting them. You can also use **DC Cloning** or **Install from Media** for the task.

A single domain recovery presents a unique challenge for rebuilding global catalog (GC) servers. For example, if the first domain controller (DC) for the domain is restored from a backup that was created one week earlier, then all other GCs in the forest will have more up-to-date data for that domain than the restored DC. To re-establish GC data consistency, there are a couple options:

-   Unhost the recovered domains partition from all GCs in the forest, except those in the recovered domain, at the same time and once complete, rehost all GCs in the forest. Also make sure you don\'t overload the remaining GCs. In large environments, coordinating this activity can be very complex.

-   Follow the forest recovery process to recover the domain, and then remove lingering objects from GCs in other domains.

The following sections provide general considerations for each option. The complete set of steps that need to be done for the recovery will vary for different Active Directory environments.

[](#rehost-all-gcs)

## Rehost all GCs {#rehost-all-gcs .heading-anchor}

Warning

The login name and password of the default Domain Administrator user account ("RID-500") for all domains must available, and the account(s) enabled for use in case a problem that prevents access to a GC for logon.

Note

To allow logon without the GC verification, it\'s possible also to configure `HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa\\IgnoreGCFailures` value to 1.

*If unknown, obtain the* **Domain ID** *by using `whoami /all` for another account in each domain or run the following command to identify the RID 500.* `\$DomainSID = (Get-ADDomain).DomainSID.Value` `\$ObjSID = New-Object` `System.Security.Principal.SecurityIdentifier("\$DomainSID-500")` `\$RID500 = \$ObjSID.Translate([System.Security.Principal.NTAccount])` `\$RID500.Value`

Rehosting all GCs can be done using `repadmin /unhost` and `repadmin /rehost` commands (part of `repadmin /experthelp`). You would run the `repadmin` commands on every GC in each domain that isn\'t recovered. It needs to be ensured, that all GCs don\'t hold a copy of the recovered domain anymore. To achieve this, unhost the domain partition first from all domain controllers across all none-recovered domains of the forest first. Since GCs don\'t contain the partition anymore, you can rehost it. When rehosting, consider the site and replication structure of your forest. For example, finish the rehost of one DC per site prior to rehosting the other DCs of that site.

This option can be advantageous for a small organization that has only a few domain controllers for each domain. All of the GCs could be rebuilt on a Friday night and, if necessary, complete replication for all read-only domain partitions before Monday morning. However, if you need to recover a large domain that covers sites across the globe, rehosting the read-only domain partition on all GCs for other domains can significantly impact operations and potentially require down time.

[](#check-for-and-remove-lingering-objects)

## Check for and remove lingering objects {#check-for-and-remove-lingering-objects .heading-anchor}

On the GCs of all other domains in the forest, you check and remove the potentially lingering objects for the read-only partition of the recovered domain.

The source for the lingering object cleanup must be a DC in the recovered domain. To be certain that the source DC doesn\'t have any lingering objects for any domain partitions, you can remove the global catalog.

Removing lingering objects is advantageous for larger organizations that can\'t risk the down time associated with rehosting the domain naming context.

For more information, see [Use repadmin to remove lingering objects](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc785298(v=ws.10)).

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

-   [AD Forest Recovery - Redeploy remaining DCs](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-restore-additional-dcs?source=recommendations)

    Learn more about: AD Forest Recovery - Redeploy remaining DCs

-   [AD Forest Recovery - Cleanup](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-cleanup?source=recommendations)

    Learn more about: AD Forest Recovery - Cleanup

-   [Active Directory Forest Recovery - Determine how to recover the forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-determine-how-to-recover?source=recommendations)

    Recovering an entire Active Directory forest involves restoring at least one Domain Controller (DC) in every domain from available backup. Recovering the forest restores each domain in the forest to its state at the time of the last trusted backup. Consequently, the restore operation will result in the loss of at least the following Active Directory data\...

-   [Active Directory Forest Recovery - Perform initial recovery](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery?source=recommendations)

    Beginning with a writeable DC in the forest root domain, complete the steps in this section in order to restore the first DC.

-   [Active Directory Forest Recovery - Virtualization](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-virtualization?source=recommendations)

    Virtualized domain controller (DC) cloning simplifies and expedites the process for installing additional virtualized DCs in a domain, especially in centralized locations such as datacenters where several DCs run on hypervisors. After you restore one virtual DC in each domain from backup, additional DCs in each domain can be rapidly brought online by using the virtualized DC cloning process. You can prepare the first virtualized DC that you recover, shut it down, and then copy that virtual hard disk as many

-   [Active Directory Forest Recovery - Prerequisites](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-prerequisites?source=recommendations)

    The following document discusses prerequisites that you should be familiar with before devising a forest recovery plan or attempting a recovery.

-   [Active Directory Forest Recovery - Identify the problem](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-identify-the-problem?source=recommendations)

    When symptoms of a forest-wide failure appear, such as in event logs or other monitoring solutions, work with Microsoft Support to determine the cause of the failure and evaluate any possible remedies.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

------------------------------------------------------------------------

-    Last updated on 11/01/2024
