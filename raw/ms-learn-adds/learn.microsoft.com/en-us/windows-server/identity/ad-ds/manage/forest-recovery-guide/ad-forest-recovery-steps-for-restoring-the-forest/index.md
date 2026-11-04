---
{"title": "Active Directory Forest Recovery - Steps to restore the forest", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-steps-for-restoring-the-forest", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Steps to restore the forest

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This section provides an overview of the recommended path for recovering a forest. The forest recovery steps are described in detail later.

We recommend you run through a forest recovery on a regular basis to:

-   Practice the recovery.
-   Ensure the custom steps you defined for your environment are still working.
-   If steps don\'t work, you notice and update the existing plan to adopt for a new kind of potential failure.
-   Verify the defaults you have for selecting the DCs to restore in each of the domains is still a good choice.

The following list summarizes the recovery steps at a high level:

1.  [Identify the problem](ad-forest-recovery-identify-the-problem) Work with IT and Microsoft Support to determine the scope of the problem and potential causes, and evaluate possible remedies with all business stakeholders. In many cases, total forest recovery should be the last option.
2.  [Determine how to recover the forest](ad-forest-recovery-determine-how-to-recover) After you determine that forest recovery is necessary, complete preliminary steps to prepare for it.
3.  [Perform initial recovery](ad-forest-recovery-perform-initial-recovery) In isolation, recover one DC for each domain, clean it, and reconnect the domains. Reset privileged accounts, and rectify problems caused by security breaches in this phase.
4.  [Redeploy remaining DCs](ad-forest-recovery-restore-additional-dcs) Redeploy the forest to return it to its state before the failure. Adapt this step to your specific design and requirements. Virtualized domain controller cloning can help expedite this process.
5.  [Cleanup](ad-forest-recovery-cleanup) After functionality has been restored, reconfigure name resolution as needed, and get LOB applications working.

The steps in this guide are designed to minimize the possibility of reintroducing dangerous data into the recovered forest. You may have to modify these steps to account for such factors as:

-   Scalability
-   Remote manageability
-   Speed of recovery

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

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3 hidden=""}

------------------------------------------------------------------------

-    Last updated on 11/01/2024
