---
{"title": "Enable Database 32k pages optional feature in Active Directory Domain Services", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/enable-32k-pages-optional-feature", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Enable Database 32k pages optional feature in Active Directory Domain Services

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

The *Database 32k pages optional feature* offers a huge improvement in scalability. Beginning with Windows Server 2025, new Active Directory forest and domains are installed with a 32k page database format. By default these new forests and domains use an 8k page simulation mode to support previous versions. An upgraded DC continues to use an 8K database format and pages. Moving to a 32k database page-size is a forest-wide operation and requires that all domain controllers in the forest have a 32k page capable database. For more information about the considerations when using the 32k page database format, see [Database 32k pages optional feature](32k-pages-optional-feature).

Warning

Once you have enabled the Database 32k pages optional feature, you can\'t revert back to the previous 8k page simulation mode. As a result, any 8k-page backup media created prior to enabling the feature will be unusable unless a complete authoritative forest recovery is performed.

In this article, you learn how to enable the Database 32k pages optional feature in Active Directory Domain Services using PowerShell.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

Before you can enable the Database 32k pages optional feature in Active Directory Domain Services, you need to complete the following prerequisites.

-   Review the article [32k pages in Active Directory Domain Services and Active Directory Lightweight Domain Services](32k-pages-optional-feature) for other considerations before enabling the 32k page feature.
-   Your Active Directory domain is operational and free from replication errors. To learn more about replication errors, see [Diagnose Active Directory replication failures](/en-us/troubleshoot/windows-server/active-directory/diagnose-replication-failures).
-   All domain controllers are running Windows Server 2025 or later, and have a 32k page capable database.
-   Domain and forest functional levels must be upgraded to Windows Server 2025 or later. To learn more about raising the functional levels, see the article [Raise Active Directory domain and forest functional levels](/en-us/troubleshoot/windows-server/active-directory/raise-active-directory-domain-forest-functional-levels).
-   Identify all your domain controllers hosting the Global Catalog (GC) and FSMO roles. Create and verify backups of these Active Directory Domain Services domain controllers before making changes.
-   Validate your backup software is compatible with the 32k page database format by backing up and restoring a 32k page capable database in a test environment.
-   Your account must be a member of the Enterprise Admins group or have equivalent permissions.

[](#optional-verify-you-have-a-32k-page-capable-database)

## Optional: Verify you have a 32k page capable database {#optional-verify-you-have-a-32k-page-capable-database .heading-anchor}

If you want to manually verify the page database size on each domain controller before enabling the Database 32k pages optional feature, you can use the following steps.

Note

When you enable the feature using the `Enable-ADOptionalFeature` cmdlet in the [Enable the Database 32k pages optional feature](#enable-the-database-32k-pages-optional-feature) section, the command checks all domain controllers have a 32k page capable database.

-   [Desktop](#tabpanel_1_desktop)
-   [PowerShell](#tabpanel_1_PowerShell)

To verify the page database size of a domain controller using ADSI Edit, follow these steps.

1.  Sign on to a computer with the AD DS Remote Server Administration Tools (RSAT) installed.

2.  Select the **Start** button, type **ADSI Edit**, and then select **ADSI Edit** from the search results.

3.  Right-click **ADSI Edit** from the console tree, then select **Connect to**.

4.  In the **Connection Settings** dialog box, select the **Select a well known Naming Context** radio button, and then select **Configuration** from the drop-down list.

5.  Expand the domain and server you want to check. For example, a server called FABRIKAMDC01, in the Corp Datacenter AD site in the `fabrikam.com` domain, would have the path **Configuration \> CN=Configuration,DC=Fabrikam,DC=com \> CN=Sites \> CN=Corp Datacenter \> CN=Servers \> CN=FABRIKAMDC01**.

6.  Right-click the **CN=NTDS Settings** object for the server you want to check, and then select **Properties**.

7.  Find the **msDS-JetDBPageSize** attribute in the attributes list. The value is the page database size capability. A value of `32768` means it\'s a 32k page database capable domain controller. A value of `8192` means an 8k page database size. No value means the domain controller is running Windows Server 2022 or earlier.

[](#enable-the-database-32k-pages-optional-feature)

## Enable the Database 32k pages optional feature {#enable-the-database-32k-pages-optional-feature .heading-anchor}

The 32k page database size is an optional feature in AD and isn\'t enabled by default. To enable the Database 32k pages optional feature in your forest or domain, follow the steps.

1.  Sign in to a domain controller.

2.  Open an elevated PowerShell prompt.

3.  Run the following command to enable the Database 32k pages optional feature. In this example, the command enables this feature for the device named `FABRIKAMDC01` in the `fabrikam.com` domain. Make sure to replace the values for the `Server` and `Target` parameters with your own values.

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    $params = @{
        Identity = 'Database 32k pages feature'
        Scope = 'ForestOrConfigurationSet'
        Server = 'FABRIKAMDC01'
        Target = 'fabrikam.com'
    }
    Enable-ADOptionalFeature @params
    ```

4.  When you run the command, you\'re prompted to confirm the action. Enter **Yes** or **Yes to All** to proceed. An example of the output is shown in the following image.

    [](media/enable-32k-pages-optional-feature/powershell-output.png#lightbox)

5.  After the Database 32k pages optional feature is enabled, monitor the replication traffic after the change.

The Database 32k pages optional feature in Active Directory Domain Services is now enabled.

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
