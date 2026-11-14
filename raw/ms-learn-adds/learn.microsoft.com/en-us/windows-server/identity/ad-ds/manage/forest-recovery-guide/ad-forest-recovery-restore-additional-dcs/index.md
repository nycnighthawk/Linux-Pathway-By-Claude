---
{"title": "Active Directory Forest Recovery - Redeploy remaining DCs", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-restore-additional-dcs", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Redeploy remaining DCs

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

The steps up to this point apply to all forests: find a valid backup for each domain, recover the domains in isolation, reconnect them, reset the global catalog, and clean up. In this next step, you\'ll redeploy the forest. The way to do this will greatly depend on your forest design, your service level agreements, site structure, available bandwidth, and numerous other factors. You\'ll need to design your own redeployment plan based on the principles and suggestions in this section, in a way that is best suited to your business requirements.

The next step is to install AD DS on all DCs that were present before the forest recovery took place. If the DCs still exist, the AD DS service will need to be removed forcibly, or the DCs can be reinstalled. Any existing backups for these DCs can\'t be reused, because the corresponding metadata has been removed during forest recovery. In an uncomplicated environment this redeployment process can be as simple as reconnecting the recovered DCs to the production network, and promoting new DCs as needed.

In a large enterprise faced with a worldwide infrastructure, a more sophisticated plan is needed. The first phase is usually to restore AD as a service; install strategically placed DCs such that all critical business divisions and applications can start working again. (It may be acceptable for branch offices to temporarily have reduced performance as a result of this.) As a second phase, all remaining and less critical DCs are redeployed.

There are two methods to install additional DCs, both of which can be automated:

[](#clone)

## Clone {#clone .heading-anchor}

You can automate the recovery of all virtualized DCs in a domain after you restore a single virtualized DC from backup. For more information about cloning and prerequisites, see [Introduction to Active Directory Domain Services (AD DS) Virtualization (Level 100)](../managing-rid-issuance).

[](#reinstall-ad-ds-using-windows-powershell)

## Reinstall AD DS using Windows Powershell {#reinstall-ad-ds-using-windows-powershell .heading-anchor}

To expedite reinstalling AD DS, you can use Install from Media (IFM) option to reduce replication traffic during the installation. For more information about using the `ntdsutil ifm` command to create installation media, see [Installing AD DS from Media](../managing-rid-issuance).

Consider the following additional points for each replica DC that is recovered in the forest by virtualized DC cloning or by installing AD DS (as opposed to restoring from backup):

-   All software on a DC that is used as the source for cloning must be able to be cloned. Applications and services that can\'t be cloned should be removed before cloning is initiated. If that isn\'t possible, an alternative virtualized DC should be chosen as the source.
-   If you clone additional virtualized DCs from the first virtualized DC to be restored, the source DC will need to be shut down while its VHDX file is copied. Then, it will need to be running and available online when the clone virtual DCs are first started. If the downtime required by the shutdown isn\'t acceptable for the first recovered DC, deploy an additional virtualized DC by installing AD DS to act as the source for cloning.
-   There is no restriction on the host name of the cloned virtualized DC or the server on which you want to install AD DS. You can use a new host name or the host name that was in use previously. For more information about DNS host name syntax, see [Creating DNS Computer Names](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc785282(v=ws.10)) ([https://go.microsoft.com/fwlink/?LinkId=74564](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc785282(v=ws.10))).
-   Configure each server with the first DNS server in the forest (the first DC that was restored in the root domain) as the preferred DNS server in the TCP/IP properties of its network adapter. For more information, see [Configure TCP/IP to use DNS](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc779282(v=ws.10)).
-   Redeploy all RODCs in the domain, either by virtualized DC cloning if several RODCs are deployed in a central location, or by the traditional method of rebuilding them by removing and reinstalling AD DS if they\'re deployed individually in isolated located locations such as branch offices.
    -   Rebuilding RODCs ensures that they don\'t contain any lingering objects and can help prevent replication conflicts from occurring later. When you remove AD DS from an RODC, *choose the option to retain DC metadata*. Using this option retains the krbtgt account for the RODC and retains the permissions for the delegated RODC administrator account and the Password Replication Policy (PRP), and prevents you from having to use Domain Admin credentials to remove and reinstall AD DS on an RODC. It also retains the DNS server and global catalog roles if they\'re installed on the RODC originally.
    -   When you rebuild DCs (RODCs or writeable DCs), there may be increased replication traffic during their reinstallation. To help reduce that impact, you can stagger the schedule of the RODC installations, and you can use the Install From Media (IFM) option. If you use the IFM option, run the `ntdsutil ifm` command on a writeable DC that you trust to be free of damaged data. This helps prevent possible corruption from appearing on the RODC after the AD DS reinstallation is complete. For more information about IFM, see [Installing AD DS from Media](../managing-rid-issuance).
    -   For more information about rebuilding RODCs, see [RODC Removal and Reinstallation](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc779282(v=ws.10)).
-   If a DC was running the DNS Server service before the forest malfunction, install and configure the DNS Server service during the installation of AD DS. Otherwise, configure its former DNS clients with other DNS servers.
-   If you require additional global catalogs to share authentication or query load for users or applications, you can either add the global catalog to the source virtualized DC before cloning or you can make a DC a global catalog server during the installation of AD DS.

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

-   [AD Forest Recovery - Cleanup](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-cleanup?source=recommendations)

    Learn more about: AD Forest Recovery - Cleanup

-   [Active Directory Forest Recovery - Recovering a single domain in a multidomain forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-recover-single-domain-multidomain-forest?source=recommendations)

    In certain scenarios, it may be necessary to recover only a single domain within a forest that has multiple domains, rather than a full forest recovery. This topic covers considerations for recovering a single domain and possible strategies for recovery.

-   [Active Directory Forest Recovery - Virtualization](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-virtualization?source=recommendations)

    Virtualized domain controller (DC) cloning simplifies and expedites the process for installing additional virtualized DCs in a domain, especially in centralized locations such as datacenters where several DCs run on hypervisors. After you restore one virtual DC in each domain from backup, additional DCs in each domain can be rapidly brought online by using the virtualized DC cloning process. You can prepare the first virtualized DC that you recover, shut it down, and then copy that virtual hard disk as many

-   [Active Directory Forest Recovery - Perform initial recovery](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery?source=recommendations)

    Beginning with a writeable DC in the forest root domain, complete the steps in this section in order to restore the first DC.

-   [Active Directory Forest Recovery - Identify the problem](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-identify-the-problem?source=recommendations)

    When symptoms of a forest-wide failure appear, such as in event logs or other monitoring solutions, work with Microsoft Support to determine the cause of the failure and evaluate any possible remedies.

-   [Active Directory Forest Recovery - Determine how to recover the forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-determine-how-to-recover?source=recommendations)

    Recovering an entire Active Directory forest involves restoring at least one Domain Controller (DC) in every domain from available backup. Recovering the forest restores each domain in the forest to its state at the time of the last trusted backup. Consequently, the restore operation will result in the loss of at least the following Active Directory data\...

-   [AD Forest Recovery - Configure DNS Server service](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-configure-dns?source=recommendations)

    Learn more about: AD Forest Recovery - Configuring the DNS Server service

Training

Module

[Manage AD DS domain controllers and FSMO roles - Training](/en-us/training/modules/manage-active-directory-domain-services-flexible-single-master-operation-roles/?source=recommendations)

Learn how to deploy and manage AD DS domain controllers, maintain availability with backup and recovery, manage the global catalog role, and transfer or seize FSMO roles including schema master, domain-naming master, RID master, infrastructure master, and PDC emulator.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
