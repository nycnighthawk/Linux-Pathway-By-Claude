---
{"title": "Active Directory Forest Recovery - Raise the value of available RID pools", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-raise-rid-pool", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Raise the value of available RID pools

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Use the following procedure to raise the value of the relative ID (RID) pools that the RID operations master will allocate after that DC is restored. By raising the value of the available RID pools, you can ensure that no DC allocates a RID for a security principal that was created after the backup that was used to restore the domain.

[](#active-directory-rid-pools-and-ridavailablepool)

## Active Directory RID Pools and rIDAvailablePool {#active-directory-rid-pools-and-ridavailablepool .heading-anchor}

Each domain has an object **CN=RID Manager\$,CN=System,DC**=\<*domain_name*\>. This object has an attribute named **rIDAvailablePool**. This attribute value maintains the global RID space for an entire domain. The value is a large integer with upper and lower parts. The upper part defines the number of security principals that can be allocated for each domain (0x3FFFFFFF or just over 1 billion). The lower part is the number of RIDs that have been allocated in the domain.

Note

In Windows Server 2016 and 2012, the number of security principals that can be allocated is increased to just over 2 billion. For more information, see [Managing RID issuance](../managing-rid-issuance).

-   Sample Value: 4611686014132422708
-   Low Part: 2100 (beginning of the next RID pool to be allocated)
-   Upper Part: 1073741823 (total number of RIDs that can be created in a domain)

When you increase the value of the large integer, you increase the value of the low part. For example, if you add 100,000 to the sample value of 4611686014132422708 for a sum of 4611686014132522708, the new low part is 102100. This indicates that the next RID pool that will be allocated by the RID master will begin with 102100 instead of 2100.

[](#raise-the-value-of-available-rid-pools-using-adsiedit-and-the-calculator)

### Raise the value of available RID pools using adsiedit and the calculator {#raise-the-value-of-available-rid-pools-using-adsiedit-and-the-calculator .heading-anchor}

1.  Open Server Manager, select **Tools** and select **ADSI Edit**.
2.  Right-click, select **Connect to** and connect do the Default Naming Context and select **OK**.
3.  Browse to the following distinguished name path: **CN=RID Manager\$,CN=System,DC=\<domain name\>**.
4.  Right-click and select the properties of **CN=RID Manager\$**.
5.  Select the attribute **rIDAvailablePool**, select **Edit**, and then copy the large integer value to the clipboard.
6.  Start calculator, and from the **View** menu, select **Scientific Mode**.
7.  Add 100,000 to the current value.
8.  Using ctrl-c, or the **Copy** command from the **Edit** menu, copy the value to the clipboard.
9.  In the edit dialog of adsiedit, paste this new value.
10. Select **OK** in the dialog, and **Apply** in the property sheet to update the **rIDAvailablePool** attribute.

[](#raise-the-value-of-available-rid-pools-using-ldp)

### Raise the value of available RID pools using LDP {#raise-the-value-of-available-rid-pools-using-ldp .heading-anchor}

1.  At the command prompt, type the following command, and then press ENTER: **ldp**
2.  Select **Connection**, select **Connect**, type the name of RID manager, and then select **OK**.
3.  Select **Connection**, select **Bind**, select **Bind with credentials** and type your administrative credentials, and then select **OK**.
4.  Select **View**, select **Tree** and then type the following distinguished name path: CN=RID Manager\$,CN=System,DC=*domain name*
5.  Select **Browse**, and then select **Modify**.
6.  Add 100,000 to the current **rIDAvailablePool** value, and then type the sum into **Values**.
7.  In **Dn**, type `cn=RID Manager$,cn=System,dc=`*\<domain name\>*.
8.  In **Edit Entry Attribute**, type `rIDAvailablePool`.
9.  Select **Replace** as the operation, and then select **Enter**.
10. Select **Run** to run the operation. Select **Close**.
11. To validate the change, select **View**, select **Tree**, and then type the following distinguished name path: CN=RID Manager\$,CN=System,DC=*domain name*. Check the **rIDAvailablePool** attribute.

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

-   [AD Forest Recovery - Invalidating the RID Pool](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-invaildate-rid-pool?source=recommendations)

    Learn more about: AD Forest Recovery - Invalidating the current RID pool

-   [Active Directory Forest Recovery - Performing a nonauthoritative restore of Active Directory Domain Services](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-nonauthoritative-restore?source=recommendations)

    The following procedures use the wbadmin.exe to perform a nonauthoritative restore of Active Directory or Active Directory Domain Services (AD DS). If you\'re using a different backup solution or if you intend to complete the authoritative restore of SYSVOL later in the forest recovery process\...

-   [AD Forest Recovery - Remove the global catalog](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-remove-gc?source=recommendations)

    Learn more about: AD Forest Recovery - Removing the global catalog

-   [AD Forest Recovery - Adding the GC](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-add-gc?source=recommendations)

    Learn more about: AD Forest Recovery - Adding the GC

-   [AD Forest Recovery - Configure DNS Server service](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-configure-dns?source=recommendations)

    Learn more about: AD Forest Recovery - Configuring the DNS Server service

-   [AD Forest Recovery - Seizing an Operations Master Role](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-seizing-operations-master-role?source=recommendations)

    Learn more about: AD Forest Recovery - Seizing an operations master role

-   [Active Directory Forest Recovery - Perform initial recovery](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery?source=recommendations)

    Beginning with a writeable DC in the forest root domain, complete the steps in this section in order to restore the first DC.

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
