---
{"title": "Active Directory Forest Recovery - Reset a trust password on one side of the trust", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-reset-trust", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Reset a trust password on one side of the trust

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

If the forest recovery is related to a security breach, use the following procedure to reset a trust password on one side of the trust. This includes implicit trusts between child and parent domains as well as explicit trusts between this domain (the trusting domain) and another domain (the trusted domain).

Reset the password on only the trusting domain side of the trust, also known as the incoming trust (the side where this domain belongs). Then, use the same password on the trusted domain side of the trust, also known as the outgoing trust. Reset the password of the outgoing trust when you restore the first DC in each of the other (trusted) domains.

Resetting the trust password ensures that the DC doesn\'t replicate with potentially bad DCs outside its domain. By setting the same trust password while restoring the first DC in each of the domains, you ensure that this DC replicates with each of the recovered DCs. Subsequent DCs in the domain that are recovered by installing AD DS will automatically replicate these new passwords during the installation process.

[](#reset-a-trust-password-on-one-side-of-the-trust)

## Reset a trust password on one side of the trust {#reset-a-trust-password-on-one-side-of-the-trust .heading-anchor}

1.  At a command prompt, type the following command, and then press ENTER:

    cli

    ``` {.inner-focus data-language="cli"}
    netdom experthelp trust
    ```

2.  Use the syntax that this command provides for using the NetDom tool to reset the trust password. For example, if there are two domains in the forest---parent and child---and you\'re running this command on the restored DC in the parent domain, use the following command syntax:

    cli

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="cli"}
    netdom trust parent domain name /domain:child domain name /resetOneSide /passwordT:password /userO:administrator /passwordO:*
    ```

    When you run this command in the child domain, use the following command syntax:

    cli

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="cli"}
    netdom trust child domain name /domain:parent domain name /resetOneSide /passwordT:password /userO:administrator /passwordO:*
    ```

    Note

    **passwordT** should be the same value on both sides of the trust. Run this command only once (unlike the **netdom resetpwd** command) because it automatically resets the password twice.

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

-   [Netdom trust](/en-us/windows-server/administration/windows-commands/netdom-trust?source=recommendations)

    Netdom trust is a command-line utility that manages, establishes, verifies, or resets trust relationships between domains in Windows Server.

-   [AD Forest Recovery - Resetting the computer account on the recovered DC](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-reset-computer-account-dc?source=recommendations)

    Learn more about: AD Forest Recovery - Resetting the computer account on the recovered DC

-   [Active Directory Replication Concepts](/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts?source=recommendations)

    Learn more about: Active Directory Replication Concepts

-   [Troubleshoot replication error 8461 - Windows Server](/en-us/troubleshoot/windows-server/active-directory/adrepl-troubleshoot-replication-error-8461?source=recommendations)

    This article describes the symptoms, cause, and resolution steps for cases when Active Directory replication fails with error 8461.

-   [dcdiag](/en-us/windows-server/administration/windows-commands/dcdiag?source=recommendations)

    DCDiag is used to diagnose Active Directory domain controller health and as a troubleshooting tool by performing several network connectivity tests.

-   [Errors when you run DCDIAG commands - Windows Server](/en-us/troubleshoot/windows-server/active-directory/dcdiag-commands-running-errors?source=recommendations)

    Fixes errors that occur when you run DCDIAG.EXE /E or /A or /C commands.

-   [Troubleshooting Active Directory Replication Problems](/en-us/windows-server/identity/ad-ds/manage/troubleshoot/troubleshooting-active-directory-replication-problems?source=recommendations)

    Learn more about: Troubleshooting Active Directory Replication Problems

Training

Module

[Manage advanced features of AD DS - Training](/en-us/training/modules/manage-advanced-features-of-ad-ds/?source=recommendations)

Learn how to create trust relationships between AD DS forests and domains, implement Enhanced Security Administrative Environment (ESAE) forests, monitor and troubleshoot AD DS replication, and create custom AD DS partitions.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
