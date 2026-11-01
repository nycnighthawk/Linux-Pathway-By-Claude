---
{"title": "Active Directory Forest Recovery - Invalidate the current RID pool", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-invaildate-rid-pool", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Invalidate the current RID pool

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Use the following procedure to use Windows PowerShell to invalidate the current RID pool on a domain controller. Windows PowerShell is enabled by default on Windows Server 2012 and Windows Server 2008 R2, but not Windows Server 2008 where it must be installed by using **Add Features**. It can be [downloaded](/en-us/troubleshoot/windows-server/system-management-components/windows-server-2003-service-pack-1-support-tools) to run on Windows Server 2003.

To verify the command completed successfully, check for event ID 16654 (source is Directory-Services-SAM) in the System log in Event Viewer in Windows Server 2012. Earlier versions of Windows don\'t log this event.

Note

After you invalidate the RID pool, you will receive an error when you first attempt to create security principal (user, computer, or group). The attempt to create an object triggers a request for a new RID pool. Retry of the operation succeeds because the new RID pool will be allocated.

[](#invalidate-the-current-rid-pool)

## Invalidate the current RID pool {#invalidate-the-current-rid-pool .heading-anchor}

-   Open an elevated Windows PowerShell session, run the following command and press ENTER:

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    $Domain = New-Object System.DirectoryServices.DirectoryEntry
    $DomainSid = $Domain.objectSid
    $RootDSE = New-Object System.DirectoryServices.DirectoryEntry("LDAP://RootDSE")
    $RootDSE.UsePropertyCache = $false
    $RootDSE.Put("invalidateRidPool", $DomainSid.Value)
    $RootDSE.SetInfo()
    ```

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

-   [AD Forest Recovery - Raising RID pools](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-raise-rid-pool?source=recommendations)

    Learn more about: AD Forest Recovery - Raising the value of available RID pools

-   [AD Forest Recovery - Seizing an Operations Master Role](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-seizing-operations-master-role?source=recommendations)

    Learn more about: AD Forest Recovery - Seizing an operations master role

-   [Managing RID Issuance](/en-us/windows-server/identity/ad-ds/manage/managing-rid-issuance?source=recommendations)

    Learn more about: Managing RID Issuance

-   [AD Forest Recovery - Resetting the computer account on the recovered DC](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-reset-computer-account-dc?source=recommendations)

    Learn more about: AD Forest Recovery - Resetting the computer account on the recovered DC

-   [Active Directory Forest Recovery - Performing a nonauthoritative restore of Active Directory Domain Services](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-nonauthoritative-restore?source=recommendations)

    The following procedures use the wbadmin.exe to perform a nonauthoritative restore of Active Directory or Active Directory Domain Services (AD DS). If you\'re using a different backup solution or if you intend to complete the authoritative restore of SYSVOL later in the forest recovery process\...

-   [AD Forest Recovery - Adding the GC](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-add-gc?source=recommendations)

    Learn more about: AD Forest Recovery - Adding the GC

-   [\[MS-ADTS\]: ISTG Selection](/en-us/openspecs/windows_protocols/ms-adts/9681607e-617f-4059-85e1-f7486a069c8d?source=recommendations)

    First, the KCC on a writable DC determines whether it acts as an ISTG for its site. Let s be the object such that

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
