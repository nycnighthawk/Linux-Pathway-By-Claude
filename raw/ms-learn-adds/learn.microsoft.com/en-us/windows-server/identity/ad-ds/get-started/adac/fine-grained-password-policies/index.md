---
{"title": "Configure fine grained password policies for Active Directory Domain Services", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/fine-grained-password-policies", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Configure fine grained password policies for Active Directory Domain Services

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Fine Grained Password Policies provide you with a way to define different password and account lockout policies for different sets of users in a domain. You can use fine grained password policies to specify multiple password policies within a single domain. You can also apply different restrictions for password and account lockout policies to different sets of users in a domain. For example, you can apply stricter settings to privileged accounts and less strict settings to the accounts of other users.

Fine-grained password policies apply only to global security groups and user objects. By default, only members of the Domain Admins group can set fine grained password policies. However, you can also delegate the ability to set these policies to other users.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

Before you can create fine grained password policies, you need to complete the following prerequisites.

-   The domain functional level must be Windows Server 2012 or higher.

-   You must be a member of the Domain Admins group.

-   You must have either of the following Remote Server Administration Tools (RSAT) installed:

    -   Active Directory Administrative Center (ADAC), **or** Active Directory module for Windows PowerShell.

[](#create-a-fine-grained-password-policy)

## Create a fine grained password policy {#create-a-fine-grained-password-policy .heading-anchor}

To create a new fine grained password policy, perform the following steps:

-   [Active Directory Administrative Center](#tabpanel_1_adac)
-   [PowerShell](#tabpanel_1_powershell)

Here\'s how to create a fine grained password policy using ADAC:

1.  Open Active Directory Administrative Center, either from the **Tools** menu of the Server Manager console or by running an elevated PowerShell session and typing **dsac.exe**.

2.  If the appropriate target domain isn\'t selected, choose **Manage**, choose **Add Navigation Nodes**, and select the appropriate target domain in the **Add Navigation Nodes** dialog box and then choose **OK**.

3.  In the ADAC navigation pane, open the **System** container, and then choose **Password Settings Container**.

4.  In the **Tasks** pane, choose **New**, and then choose **Password Settings**.

5.  Fill in or edit fields inside the property page to create a new **Password Settings** object. The **Name** and **Precedence** fields are required.

6.  Under **Directly Applies To**, choose **Add**, type the name of the group to which the fine grained password policy, and then choose **OK**.

7.  Choose **OK** to submit the creation.

[](#view-a-resultant-set-of-policies-for-a-user)

## View a resultant set of policies for a user {#view-a-resultant-set-of-policies-for-a-user .heading-anchor}

To view the resultant policy that applies to a specific user, perform the following steps:

-   [Active Directory Administrative Center](#tabpanel_2_adac)
-   [PowerShell](#tabpanel_2_powershell)

Here\'s how to view the resultant policy that applies to a specific user using ADAC:

1.  Open Active Directory Administrative Center, either from the Tools menu of the Server Manager console or by running an elevated PowerShell session and typing **dsac.exe**.

2.  If the appropriate target domain isn\'t selected, choose **Manage**, choose **Add Navigation Nodes**, and select the appropriate target domain in the **Add Navigation Nodes** dialog box and then choose **OK**.

3.  Navigate to the user for whom you wish to view the resultant policy settings.

4.  Choose **View Resultant Password Settings** in the **Tasks** pane.

5.  Examine the password setting policy and then choose **Cancel**.

[](#edit-a-fine-grained-password-policy)

## Edit a fine grained password policy {#edit-a-fine-grained-password-policy .heading-anchor}

Edit a fine grained password policy using the following steps:

-   [Active Directory Administrative Center](#tabpanel_3_adac)
-   [PowerShell](#tabpanel_3_powershell)

Here\'s how to edit a fine grained password policy using ADAC:

1.  Open Active Directory Administrative Center, either from the Tools menu of the Server Manager console or by running an elevated PowerShell session and typing **dsac.exe**.

2.  If the appropriate target domain isn\'t selected, choose **Manage**, choose **Add Navigation Nodes**, and select the appropriate target domain in the **Add Navigation Nodes** dialog box and then choose **OK**.

3.  In the ADAC **Navigation Pane**, expand **System** and then expand the **Password Settings Container**.

4.  Select the fine grained password policy you wish to edit and choose **Properties** in the **Tasks** pane.

5.  Modify the settings that you wish to change and choose **OK**.

[](#delete-a-fine-grained-password-policy)

## Delete a fine grained password policy {#delete-a-fine-grained-password-policy .heading-anchor}

Perform the following steps to delete a fine grained password policy:

-   [Active Directory Administrative Center](#tabpanel_4_adac)
-   [PowerShell](#tabpanel_4_powershell)

Here\'s how to delete a fine grained password policy using ADAC:

1.  Open Active Directory Administrative Center, either from the Tools menu of the Server Manager console or by running an elevated PowerShell session and typing **dsac.exe**.

2.  If the appropriate target domain isn\'t selected, choose **Manage**, choose **Add Navigation Nodes**, and select the appropriate target domain in the **Add Navigation Nodes** dialog box and then choose **OK**.

3.  In the ADAC Navigation Pane, expand **System** and then expand **Password Settings Container**.

4.  Select the fine grained password policy you wish to remove and in the **Tasks** pane choose **Properties**.

5.  Clear the **Protect from accidental deletion** checkbox and choose **OK**.

6.  Select the fine grained password policy, and in the **Tasks** pane choose **Delete**.

7.  Choose **OK** in the confirmation dialog to delete the policy.

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

-    Last updated on 06/16/2025
