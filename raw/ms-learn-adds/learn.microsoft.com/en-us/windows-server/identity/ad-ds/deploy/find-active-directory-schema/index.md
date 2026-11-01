---
{"title": "Find the current Active Directory schema version", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/find-active-directory-schema", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Find the current Active Directory schema version

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

An Active Directory (AD) schema is a set of rules that defines what kinds of object classes you can create in an AD forest. For more information, see [Active Directory schema (AD DS)](/en-us/windows/win32/ad/active-directory-schema).

This article walks you through how to find the schema version and Exchange Services schema version that your forest uses.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

To perform the tasks described in this article, ensure that your environment meets the following requirements:

-   Your machine should run Microsoft Exchange Server 2016 or later.
-   You must install the Active Directory Domain Services (AD DS) role. To learn more, see [Install or uninstall roles, role services, or features](../../../administration/server-manager/install-or-uninstall-roles-role-services-or-features).
-   The server must be a domain controller (DC).
-   Users must be part of the Domain Admins or Enterprise Admins group.

[](#finding-the-schema-version)

## Finding the schema version {#finding-the-schema-version .heading-anchor}

To find the current Active Directory schema version:

Note

The internal root domain used in this demo is **contoso.local**. You need to modify the DC= field to correspond with the AD configuration in your own environment.

Depending on your configuration, you might also need to import the AD PowerShell module by running the `Import-Module ActiveDirectory` command before you can start running AD cmdlets.

-   [GUI](#tabpanel_1_gui)
-   [CMD](#tabpanel_1_cmd)
-   [PowerShell](#tabpanel_1_powershell)

1.  Open the **Start** menu.

2.  Enter **ADSIEdit.msc**, and then select **Enter** to open **ADSI Edit**.

3.  In the pane on the left side of the window, right-click **ADSI Edit**, and then select **Connect to**.

4.  In the **Connection Settings** window, under **Select a well known Naming Context**, select **Schema**, and then select **OK**.

5.  In the pane on the left side of the window, expand the schema for your DC.

6.  Right-click **CN=Schema,CN=Configuration,DC=contoso,DC=local** and then select **Properties**.

7.  In the **Attribute** list, scroll down until you find the *objectvVersion* attribute. The value is the schema version.

When you finish, use the table in [Mapping the objectVersion attribute](#mapping-the-objectversion-attribute) to find which operating system (OS) version corresponds to your version number.

[](#mapping-the-objectversion-attribute)

### Mapping the objectVersion attribute {#mapping-the-objectversion-attribute .heading-anchor}

The following table maps the number shown in the **objectVersion** attribute with its corresponding OS version:

  Version   Operating system
  --------- -----------------------------------------------------------------------------------
  91        Windows Server 2025
  88        Windows Server 2022
  88        Windows Server 2019
  87        Windows Server 2016
  69        Windows Server 2012 R2
  56        Windows Server 2012
  47        Windows Server 2008 R2
  44        Windows Server 2008 RTM
  31        Windows Server 2003 R2
  30        Windows Server 2003 RTM, Windows 2003 Service Pack 1, Windows 2003 Service Pack 2

[](#find-the-current-exchange-schema-version)

## Find the current Exchange Schema version {#find-the-current-exchange-schema-version .heading-anchor}

To find the current Exchange Schema version, you can use one of the following methods:

-   [GUI](#tabpanel_2_gui)
-   [CMD](#tabpanel_2_cmd)
-   [PowerShell](#tabpanel_2_powershell)

1.  Open the **Start** menu.

2.  Enter **ADSIEdit.msc**, and then select **Enter** to open **ADSI Edit**.

3.  In the pane on the left side of the window, right-click **ADSI Edit**, and then select **Connect to**.

4.  In the **Connection Settings** window, under **Select a well known Naming Context**, select **Schema**, and then select **OK**.

5.  In the pane on the left side of the window, expand the schema for your DC.

6.  Select **CN=Schema,CN=Configuration,DC=contoso,DC=local**.

7.  In the pane in the center of the window, scroll down the **Name** list and open **CN=ms-Exch-Schema-Version-Pt**.

8.  In the **Attribute** list, scroll down until you find the *rangeUpper* attribute. The value is the schema version.

When you finish, use the information in [Mapping the rangeUpper attribute](#mapping-the-rangeupper-attribute) to determine which version of Exchange Schema corresponds to your attribute value.

[](#mapping-the-rangeupper-attribute)

### Mapping the rangeUpper attribute {#mapping-the-rangeupper-attribute .heading-anchor}

The following articles show how to map the **rangeUpper** attribute value with its corresponding Exchange Schema version:

-   [Exchange 2016 Active Directory versions](/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2016&preserve-view=true#exchange-2016-active-directory-versions)
-   [Exchange 2019 Active Directory versions](/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019&preserve-view=true#exchange-2019-active-directory-versions)

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Windows Server Active Directory schema updates](schema-updates)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Schema updates in Windows Server](/en-us/windows-server/identity/ad-ds/deploy/schema-updates?source=recommendations)

    Schema changes made by Adprep.exe listed by operating system version.

-   [Active Directory domain-wide schema updates](/en-us/windows-server/identity/ad-ds/deploy/domain-wide-updates?source=recommendations)

    Domain-wide schema updates performed by adprep /domainprep when promoting a Domain Controller

-   [Raise Domain and Forest Functional Levels in AD DS on Windows Server](/en-us/windows-server/identity/ad-ds/plan/raise-domain-forest-functional-levels?source=recommendations)

    Learn how to raise domain and forest functional levels in Active Directory Domain Services on Windows Server.

-   [Active Directory Domain Services Functional Levels](/en-us/windows-server/identity/ad-ds/active-directory-functional-levels?source=recommendations)

    Discover the capabilities of Active Directory Domain Services functional levels and learn how they impact domain controllers and Windows Server compatibility.

-   [Diagnose AD replication failures - Windows Server](/en-us/troubleshoot/windows-server/active-directory/diagnose-replication-failures?source=recommendations)

    Describes how to diagnose Active Directory replication failures.

-   [Verify DNS Functionality to Support Directory Replication](/en-us/windows-server/identity/ad-ds/manage/troubleshoot/verify-dns-functionality-to-support-directory-replication?source=recommendations)

    Learn more about: Verify DNS Functionality to Support Directory Replication

-   [Troubleshooting replication error 8418\--Schema mismatch - Windows Server](/en-us/troubleshoot/windows-server/active-directory/replication-error-8418?source=recommendations)

    Helps you to diagnose possible causes replication error 8418, and to determine whether you have to take action or seek assistance.

-   [Active Directory replication error 8453 - Windows Server](/en-us/troubleshoot/windows-server/active-directory/replication-error-8453?source=recommendations)

    This article describes how to troubleshoot Active Directory replication error 8453.

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 07/21/2025
