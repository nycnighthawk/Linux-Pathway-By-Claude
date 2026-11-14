---
{"title": "Active Directory Forest Recovery - Remove the global catalog", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-remove-gc", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Remove the global catalog

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Use the following procedure to remove the global catalog from a DC.

Restoring a global catalog server from backup could result in the global catalog holding newer data for one of its partial replicas than the corresponding domain that is authoritative for that partial replica. In such a case, the newer data won\'t be removed from the global catalog and might even replicate to other global catalog servers. As a result, even if you did restore a DC that was a global catalog server, either inadvertently or because that was the solitary backup you trusted, you should remove the global catalog soon after the restore operation is complete. When the global catalog is removed, the computer removes all its partial replicas.

[](#remove-the-global-catalog-using-active-directory-sites-and-services)

## Remove the global catalog using Active Directory Sites and Services {#remove-the-global-catalog-using-active-directory-sites-and-services .heading-anchor}

1.  Open Server Manager, select **Tools** and select **Active Directory Sites and Services**.
2.  In the console tree, expand the **Sites** container, and then select the appropriate site that contains the target server.
3.  Expand the **Servers** container, and then expand the *server* object for the DC from which you want to remove the global catalog.
4.  Right-click **NTDS Settings**, and then select **Properties**.
5.  Clear the **Global Catalog** check box.
6.  Select **Apply**.

[](#remove-the-global-catalog-using-repadmin)

## Remove the global catalog using Repadmin {#remove-the-global-catalog-using-repadmin .heading-anchor}

Open an elevated command prompt, type the following command, and press ENTER:

cli

``` {.inner-focus data-language="cli"}
repadmin.exe /options DC_NAME –IS_GC
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

-   [AD Forest Recovery - Configure DNS Server service](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-configure-dns?source=recommendations)

    Learn more about: AD Forest Recovery - Configuring the DNS Server service

-   [Active Directory Forest Recovery - Performing a nonauthoritative restore of Active Directory Domain Services](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-nonauthoritative-restore?source=recommendations)

    The following procedures use the wbadmin.exe to perform a nonauthoritative restore of Active Directory or Active Directory Domain Services (AD DS). If you\'re using a different backup solution or if you intend to complete the authoritative restore of SYSVOL later in the forest recovery process\...

-   [AD Forest Recovery - Cleaning metadata of removed writable domain controllers](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-cleaning-metadata-of-removed-dcs?source=recommendations)

    Metadata cleanup removes Active Directory data that identifies a DC to the replication system. Note that outside of a Forest Recovery, metadata cleanup is part of the demotion process of domain controllers, however, when they aren\'t reachable anymore, this process also applies. Use the following procedure to delete the DC objects for DCs that you plan to add back to the network by reinstalling AD DS.

-   [AD Forest Recovery - Raising RID pools](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-raise-rid-pool?source=recommendations)

    Learn more about: AD Forest Recovery - Raising the value of available RID pools

-   [AD Forest Recovery - Performing an authoritative synchronization of DFSR-replicated SYSVOL](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-authoritative-recovery-sysvol?source=recommendations)

    There are different ways to perform an authoritative restore of SYSVOL. You can either edit the \*\*msDFSR-Options\*\* attribute or perform a system state restore using wbadmin --authsysvol. If you have the option to restore a system state backup (that is, you\'re restoring AD DS to the same hardware and operating system instance) then using wbadmin --authsysvol is simpler. But if you need to perform a bare metal restore, then you need to edit the \*\*msDFSR-Options\*\* attribute.

-   [AD Forest Recovery - Seizing an Operations Master Role](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-seizing-operations-master-role?source=recommendations)

    Learn more about: AD Forest Recovery - Seizing an operations master role

-   [AD Forest Recovery - Verify Replication](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-verify-replication?source=recommendations)

    Learn more about resources to verify replication.

Training

Module

[Manage AD DS domain controllers and FSMO roles - Training](/en-us/training/modules/manage-active-directory-domain-services-flexible-single-master-operation-roles/?source=recommendations)

Learn how to deploy and manage AD DS domain controllers, maintain availability with backup and recovery, manage the global catalog role, and transfer or seize FSMO roles including schema master, domain-naming master, RID master, infrastructure master, and PDC emulator.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
