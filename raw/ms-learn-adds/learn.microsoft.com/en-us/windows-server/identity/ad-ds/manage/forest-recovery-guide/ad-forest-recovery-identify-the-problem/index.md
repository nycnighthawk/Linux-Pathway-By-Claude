---
{"title": "Active Directory Forest Recovery - Identify the problem", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-identify-the-problem", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Identify the problem

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

When symptoms of a forest-wide failure appear, such as in event logs or other monitoring solutions, work with Microsoft Support to determine the cause of the failure and evaluate any possible remedies.

Important

This guide doesn\'t cover security recommendations for how to recover a forest that has been hacked or compromised. In general, it\'s recommended to follow [Best Practices for Securing Active Directory](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory) and Pass-the-Hash mitigation techniques to harden the environment. For more information, see [Mitigating Pass-the-Hash (PtH) Attacks and Other Credential Theft Techniques](https://www.microsoft.com/download/details.aspx?id=36036).

[](#examples-of-forest-wide-failures)

## Examples of forest-wide failures {#examples-of-forest-wide-failures .heading-anchor}

-   All DCs are logically corrupted or physically damaged to a point that business continuity is impossible; for example, all business applications that depend on AD DS aren\'t functional.
-   A rogue administrator compromised the Active Directory environment.
-   An attacker intentionally --- or an administrator accidentally --- runs a script that spreads data corruption across the forest.
-   An attacker intentionally --- or an administrator accidentally --- extends the Active Directory schema with malicious or conflicting changes.
-   The content, or a backup of a Domain Controller, has been exposed to an external party, but leaked credentials haven\'t been used to modify AD data. In this case, you may not need to restore the AD database from backup and reinstall all DCs. You may need to reset all password of users, computers, trusts and (g)MSA accounts.
-   An attacker installed malicious software on DCs, and you were advised by Microsoft Support to recover the forest from backup.
-   None of the DCs can replicate with their replication partners.
-   Changes can\'t be made to AD DS at any domain controller.
-   New DCs can\'t be installed in any domain.

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
