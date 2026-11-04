---
{"title": "Use the Active Directory Administrative Center Windows PowerShell History Viewer", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/use-active-directory-administrative-center-powershell-history", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Use the Active Directory Administrative Center Windows PowerShell History Viewer

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Active Directory Administrative Center now provides a complete history of all the Windows PowerShell cmdlets it runs and their arguments and values. You can copy the cmdlet history elsewhere for learning, modification, and re-use. You can create task notes to assist with understanding what your Active Directory Administrative Center commands resulted in Windows PowerShell. You can also filter the history to find points of interest.

In this article, you\'ll learn how to use the Windows PowerShell History Viewer in Active Directory Administrative Center (ADAC) to construct a Windows PowerShell script.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

Before you can use the Windows PowerShell History Viewer in Active Directory Administrative Center (ADAC), you need to complete the following prerequisites.

-   You must be using a supported version of Windows Server. To learn more about supported versions of Windows Server, see [Release information](../../../../get-started/windows-server-release-info).

-   You must have the following Remote Server Administration Tools (RSAT) installed:

    -   Active Directory Administrative Center (ADAC)

    -   Active Directory module for Windows PowerShell.

-   Have a basic understanding of Windows PowerShell. For example, you need to know how piping in Windows PowerShell works. For more information about piping in Windows PowerShell, see [about_Pipelines](/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines).

[](#construct-a-script)

## Construct a script {#construct-a-script .heading-anchor}

The Active Directory Administrative Center Windows PowerShell History Viewer\'s purpose is for you to learn through practical experience. As actions are executed in the user interface, the equivalent Windows PowerShell command is shown to the user in Windows PowerShell History Viewer.

Using the Active Directory Administrative Center (ADAC), create a user and then use the Windows PowerShell History Viewer to construct a Windows PowerShell script.

1.  Sign in to a computer that has the Active Directory module for Windows PowerShell installed.

2.  Open Active Directory Administrative Center, either from the Tools menu of the Server Manager console or by running an elevated PowerShell session and typing **dsac.exe**.

3.  Select the appropriate target domain in the navigation pane.

4.  Navigate to the organizational unit where you want to create the user.

5.  In the **Tasks** pane, under **Users**, select **New**, then **User**.

6.  Fill in the required fields and click **OK**.

7.  Expand the **Windows PowerShell History** pane at the bottom of the ADAC screen.

8.  Review the command that was just generated, copy it, and paste it into your desired editor to construct your script. For example, you can now modify the command to create a different user, or create a user in a different organizational unit.

You can repeat this process for other tasks in Active Directory Administrative Center.

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Advanced AD DS Management Using Active Directory Administrative Center (Level 200)](advanced-ad-ds-management-using-active-directory-administrative-center--level-200-)

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
