---
{"title": "Active Directory Forest Recovery - Add the GC", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-add-gc", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Add the GC

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Use the following procedure to add the global catalog to a DC.

[](#add-the-global-catalog)

## Add the global catalog {#add-the-global-catalog .heading-anchor}

1.  Select **Start**, point to **All Programs**, point to **Administrative Tools**, and then select **Active Directory Sites and Services**.
2.  In the console tree, expand the **Sites** container, and then select the appropriate site that contains the target server.
3.  Expand the **Servers** container, and then expand the server object for the DC to which you want to add the global catalog.
4.  Right-click **NTDS Settings**, and then select **Properties**.
5.  Select the **Global Catalog** check box.

[](#add-the-global-catalog-using-repadmin)

## Add the global catalog using repadmin {#add-the-global-catalog-using-repadmin .heading-anchor}

-   Open an elevated command prompt, type the following command, and press ENTER:

    cli

    ``` {.inner-focus data-language="cli"}
    repadmin.exe /options DC_NAME +IS_GC
    ```

The following are ways to speed up the process of adding the global catalog to the DC in the root domain:

-   Ideally, the DC in the root domain should be a replication partner of the restored DCs in the nonroot domains. If so, confirm that the Knowledge Consistency Checker (KCC) has created the corresponding **repsFrom** object for the source DC and partition in the root DC. You can confirm this by running the `repadmin /showreps /v` command.

-   If there\'s no **repsFrom** object created, create this object for the configuration partition. This way, the DC in the root domain can determine which DCs in the nonroot domain have been deleted. You can do this with the following commands:

    cli

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="cli"}
    repadmin /add ConfigurationNamingContext DestinationDomainController SourceDomainControllerCNAME
    ```

    cli

    ``` {.inner-focus data-language="cli"}
    repadmin /options DSA -Disable_NTDSCONN_XLATE
    ```

    The format for the *SourceDomainControllerCNAME* is:

    cli

    ``` {.inner-focus data-language="cli"}
    sourceDCGuid._msdcs.root domain
    ```

    For example, the repadmin /add command for the configuration partition of the contoso.com domain could be:

    cli

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="cli"}
    repadmin /add cn=configuration,DC=contoso,DC=com DC01 937ef930-7356-43c8-88dc-8baaaa781cf6._msdcs.dDSP17A22.contoso.com
    ```

-   If the **repsFrom** object is present, try to sync the DC in the root domain with the DC in the nonroot domain as follows:

    cli

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="cli"}
    repadmin /sync DomainNamingContext DestinationDomainController SourceDomainControllerGUID
    ```

    Where *DestinationDomainController* is the DC in the root domain and *SourceDomainController* is the restored DC in the nonroot domain.

-   The root domain DNS server should have the alias (CNAME) resource records for the source DC. Ensure that the parent DNS zone contains delegation resource records (name server (NS) and host (A) resource records) for the correct DCs (the DCs that have been restored from backup) in the child zone.

-   Make sure that the DC in the root domain is contacting the correct Key Distribution Center (KDC) in the nonroot domain. To test this, at the command prompt, type the following command, and then press ENTER:

    cli

    ``` {.inner-focus data-language="cli"}
    nltest /dsgetdc:nonroot domain name /KDC /Force
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

-   [AD Forest Recovery - Remove the global catalog](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-remove-gc?source=recommendations)

    Learn more about: AD Forest Recovery - Removing the global catalog

-   [AD Forest Recovery - Configure DNS Server service](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-configure-dns?source=recommendations)

    Learn more about: AD Forest Recovery - Configuring the DNS Server service

-   [AD Forest Recovery - Raising RID pools](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-raise-rid-pool?source=recommendations)

    Learn more about: AD Forest Recovery - Raising the value of available RID pools

-   [AD Forest Recovery - Verify Replication](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-verify-replication?source=recommendations)

    Learn more about resources to verify replication.

-   [Active Directory Forest Recovery - Performing a nonauthoritative restore of Active Directory Domain Services](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-nonauthoritative-restore?source=recommendations)

    The following procedures use the wbadmin.exe to perform a nonauthoritative restore of Active Directory or Active Directory Domain Services (AD DS). If you\'re using a different backup solution or if you intend to complete the authoritative restore of SYSVOL later in the forest recovery process\...

-   [AD Forest Recovery - Performing an authoritative synchronization of DFSR-replicated SYSVOL](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-authoritative-recovery-sysvol?source=recommendations)

    There are different ways to perform an authoritative restore of SYSVOL. You can either edit the \*\*msDFSR-Options\*\* attribute or perform a system state restore using wbadmin --authsysvol. If you have the option to restore a system state backup (that is, you\'re restoring AD DS to the same hardware and operating system instance) then using wbadmin --authsysvol is simpler. But if you need to perform a bare metal restore, then you need to edit the \*\*msDFSR-Options\*\* attribute.

-   [AD Forest Recovery - Seizing an Operations Master Role](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-seizing-operations-master-role?source=recommendations)

    Learn more about: AD Forest Recovery - Seizing an operations master role

-   [Active Directory Forest Recovery - Procedures](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-procedures?source=recommendations)

    View a list of procedures that are used in backing up and restoring domain controllers and Active Directory.

Training

Module

[Manage AD DS domain controllers and FSMO roles - Training](/en-us/training/modules/manage-active-directory-domain-services-flexible-single-master-operation-roles/?source=recommendations)

Learn how to deploy and manage AD DS domain controllers, maintain availability with backup and recovery, manage the global catalog role, and transfer or seize FSMO roles including schema master, domain-naming master, RID master, infrastructure master, and PDC emulator.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
