---
{"title": "Active Directory Forest Recovery - Reset the krbtgt password", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-reset-the-krbtgt-password", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Reset the krbtgt password

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Use the following procedure to reset the krbtgt password for the domain. The following procedure applies to writeable DCs, but not read-only domain controllers (RODC).

Important

If you plan to recover RODC during the forest recovery, don\'t delete the krbtgt accounts for the RODC. The krbtgt account for an RODC is listed in the format krbtgt\_*number*.

If you use a customized password filter (such as passfilt.dll) on a DC, then you might receive an error when you try to reset the krbtgt password. For more information, including a workaround, see Microsoft Knowledge Base [article 2549833](https://support.microsoft.com/kb/2549833).

[](#reset-the-krbtgt-password)

## Reset the krbtgt password {#reset-the-krbtgt-password .heading-anchor}

1.  Select **Start**, point to **Control Panel**, point to **Administrative Tools**, and then select **Active Directory Users and Computers**.
2.  Select **View**, and then select **Advanced Features**.
3.  In the console tree, double-click the domain container, and then select **Users**.
4.  In the details pane, right-click the **krbtgt** user account, and then select **Reset Password**.
5.  In **New password**, type a new password, retype the password in **Confirm password**, and then select **OK**. The password that you specify isn\'t significant because the system generates a strong password automatically independent of the password that you specify.

Important

You should perform this operation twice. You must wait 10 hours between password resets. 10 hours are the default **Maximum lifetime for user ticket** and **Maximum lifetime for service ticket** policy settings, hence in a case where the Maximum lifetime period changes, the minimum waiting period between resets should be greater than the configured value.

Note

The password history value for the krbtgt account is 2, meaning it includes the two most recent passwords. By resetting the password twice you effectively clear any old passwords from the history, so there\'s no way another DC replicates with this DC by using an old password.

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

-   [AD Forest Recovery - Resetting a trust password](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-reset-trust?source=recommendations)

    Learn more about: Resetting a trust password on one side of the trust

-   [Detect and Remediate RC4 Usage in Kerberos](/en-us/windows-server/security/kerberos/detect-remediate-rc4-kerberos?source=recommendations)

    Learn how to detect and limit or disable RC4 usage in Kerberos to enhance security in Active Directory domain environments.

-   [\[MS-ADA2\]: Attribute msDS-ExpirePasswordsOnSmartCardOnlyAccounts](/en-us/openspecs/windows_protocols/ms-ada2/1ba3e699-77ab-4ba6-9d70-74616b1e11d4?source=recommendations)

    This attribute controls whether the passwords on smart-card-only accounts expire in accordance with the password policy.

-   [TGS requests for krbtgt account fail - Windows Server](/en-us/troubleshoot/windows-server/windows-security/tgs-request-for-krbtgt-account-fails?source=recommendations)

    Describes an issue that causes S4U Kerberos authentication to fail for a user in a trusted forest. Occurs when selective authentication is enabled on the forest trust and when an application calls LsalogonUser by using a Kerberos S4U client request.

-   [\[MS-ADTS\]: dSHeuristics](/en-us/openspecs/windows_protocols/ms-adts/e5899be4-862e-496f-9a38-33950617d2c5?source=recommendations)

    dSHeuristics is a Unicode string attribute. Each character in the string represents a heuristic that is used to determine

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

------------------------------------------------------------------------

-    Last updated on 05/22/2025
