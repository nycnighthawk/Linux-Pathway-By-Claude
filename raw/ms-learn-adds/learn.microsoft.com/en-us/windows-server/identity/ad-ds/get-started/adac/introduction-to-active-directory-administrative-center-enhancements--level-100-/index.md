---
{"title": "Advanced AD DS Management using Active Directory Administrative Center (Level 200)", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Advanced AD DS Management using Active Directory Administrative Center (Level 200)

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This article covers the updated Active Directory Administrative Center with its Active Directory Recycle Bin, fine-grained password policies, and Windows PowerShell History Viewer in detail, including architecture, examples for common tasks, and troubleshooting information. For an introduction, see [Introduction to Active Directory Administrative Center Enhancements (Level 100)](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831702(v=ws.11)).

[](#active-directory-administrative-center-architecture)

## Active Directory Administrative Center architecture {#active-directory-administrative-center-architecture .heading-anchor}

[](#active-directory-administrative-center-executables-and-dlls)

### Active Directory Administrative Center executables and DLLs {#active-directory-administrative-center-executables-and-dlls .heading-anchor}

The module and underlying architecture of Active Directory Administrative Center hasn\'t changed with the recycle bin, fine-grained password policies, and history viewer capabilities.

-   Microsoft.ActiveDirectory.Management.UI.dll
-   Microsoft.ActiveDirectory.Management.UI.resources.dll
-   Microsoft.ActiveDirectory.Management.dll
-   Microsoft.ActiveDirectory.Management.resources.dll
-   ActiveDirectoryPowerShellResources.dll

The underlying Windows PowerShell and layer of operations for the recycle bin functionality are illustrated here:

[](#enabling-and-managing-the-active-directory-recycle-bin-by-using-active-directory-administrative-center)

## Enabling and managing the Active Directory Recycle bin by using Active Directory Administrative Center {#enabling-and-managing-the-active-directory-recycle-bin-by-using-active-directory-administrative-center .heading-anchor}

[](#capabilities)

### Capabilities {#capabilities .heading-anchor}

-   The Windows Server 2012 or newer Active Directory Administrative Center enables you to configure and manage the Active Directory recycle bin for any domain partition in a forest. There\'s no longer a requirement to use Windows PowerShell or Ldp.exe to enable the Active Directory recycle bin or restore objects in domain partitions.
-   The Active Directory Administrative Center has advanced filtering criteria, making targeted restoration easier in large environments with many intentionally deleted objects.

[](#limitations)

### Limitations {#limitations .heading-anchor}

-   Because the Active Directory Administrative Center can only manage domain partitions, it can\'t restore deleted objects from the Configuration, Domain DNS, or Forest DNS partitions. (You can\'t delete objects from the Schema partition.) To restore objects from nondomain partitions, use [Restore-ADObject](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee617262(v=technet.10)).

-   The Active Directory Administrative Center can\'t restore subtrees of objects in a single action. For example, if you delete an OU with nested OUs, users, groups, and computers, restoring the base OU doesn\'t restore the child objects.

    Note

    The Active Directory Administrative Center batch restore operation does a \"best effort\" sort of the deleted objects *within the selection only*, so parents are ordered before the children for the restore list. In simple test cases, subtrees of objects can be restored in a single action. But corner cases, such as a selection that contains partial trees (trees with some of the deleted parent nodes missing) or error cases, such as skipping the child objects when parent restore fails, might not work as expected. For this reason, you should always restore subtrees of objects as a separate action after you restore the parent objects.

The Active Directory recycle bin requires a Windows Server 2008 R2 forest functional level, and you must be a member of the Enterprise Admins group. After Active Directory recycle bin is enabled, you can\'t disable it. Active Directory recycle bin increases the size of the Active Directory database (NTDS.DIT) on every domain controller in the forest. Disk space used by the recycle bin continues to increase over time as it preserves objects and all their attribute data.

[](#enabling-active-directory-recycle-bin-using-active-directory-administrative-center)

### Enabling Active Directory recycle bin using Active Directory Administrative Center {#enabling-active-directory-recycle-bin-using-active-directory-administrative-center .heading-anchor}

To enable the Active Directory recycle bin, open the **Active Directory Administrative Center** and select the name of your forest in the navigation pane. From the **Tasks** pane, select **Enable Recycle Bin**.

The Active Directory Administrative Center shows the **Enable Recycle Bin Confirmation** dialog. This dialog warns you that enabling the recycle bin is irreversible. Select **OK** to enable the Active Directory recycle bin. The Active Directory Administrative Center shows another dialog to remind you that the Active Directory recycle bin isn\'t fully functional until all domain controllers replicate the configuration change.

Important

The option to enable the Active Directory recycle bin is unavailable if:

-   The forest functional level is less than Windows Server 2008 R2.
-   It\'s already enabled.

The equivalent Active Directory Windows PowerShell cmdlet is:

PowerShell

``` {.inner-focus data-language="powershell"}
Enable-ADOptionalFeature
```

For more information about using Windows PowerShell to enable the Active Directory recycle bin, see the [Active Directory recycle bin step-by-step guide](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831702(v=ws.11)#active-directory-recycle-bin).

[](#managing-active-directory-recycle-bin-by-using-active-directory-administrative-center)

### Managing Active Directory recycle bin by using Active Directory Administrative Center {#managing-active-directory-recycle-bin-by-using-active-directory-administrative-center .heading-anchor}

This section uses the example of an existing domain named `corp.contoso.com`. This domain organizes users into a parent OU named **UserAccounts**. The **UserAccounts** OU contains three child OUs named by department. Each of these child OUs contains further OUs, users, and groups.

[](#storage-and-filtering)

#### Storage and filtering {#storage-and-filtering .heading-anchor}

The Active Directory recycle bin preserves all objects deleted in the forest. It saves these objects according to the **msDS-deletedObjectLifetime** attribute, which by default is set to match the **tombstoneLifetime** attribute of the forest. In any forest created using Windows Server 2003 SP1 or later, the value of **tombstoneLifetime** is set to 180 days by default. In any forest upgraded from Windows 2000 or installed with Windows Server 2003 (no service pack), the default **tombstoneLifetime** attribute is not set and Windows therefore uses the internal default of 60 days. All of this is configurable. You can use the Active Directory Administrative Center to restore any objects deleted from the domain partitions of the forest. You must continue to use the cmdlet `Restore-ADObject` to restore deleted objects from other partitions, such as Configuration. Enabling the Active Directory recycle bin makes the **Deleted Objects** container visible under every domain partition in the Active Directory Administrative Center.

The **Deleted Objects** container shows all the restorable objects in that domain partition. Deleted objects older than **msDS-deletedObjectLifetime** are known as *recycled objects*. The Active Directory Administrative Center doesn\'t show recycled objects, and you can\'t restore these objects by using Active Directory Administrative Center.

For a deeper explanation of the recycle bin architecture and processing rules, see [The Active Directory Recycle Bin: Understanding, Implementing, Best Practices, and Troubleshooting](/en-us/archive/blogs/askds/the-ad-recycle-bin-understanding-implementing-best-practices-and-troubleshooting).

The Active Directory Administrative Center artificially limits the default number of objects returned from a container to 20,000 objects. You can increase this limit as high as 100,000 objects by selecting the **Manage** menu and then selecting **Management List Options**.

[](#restoration)

#### Restoration {#restoration .heading-anchor}

[](#filtering)

##### Filtering {#filtering .heading-anchor}

Active Directory Administrative Center offers powerful criteria and filtering options that you should become familiar with before you need to use them in a real-life restoration. Domains intentionally delete many objects over their lifetime. Because the deleted object lifetime is probably 180 days, you can\'t restore all objects when an accident occurs.

Rather than writing complex LDAP filters and converting UTC values into dates and times, use the basic and advanced **Filter** menu to list only the relevant objects. If you know the day of deletion, the names of objects, or any other key data, use that to your advantage when filtering. Toggle the advanced filter options by selecting the chevron to the right of the search box.

The restore operation supports all the standard filter criteria options, the same as any other search. Of the built-in filters, the important ones for restoring objects are typically:

-   ANR (ambiguous name resolution - not listed in the menu, but it\'s used when you type in the **Filter** box)
-   Last modified between given dates
-   Object is user/inetorgperson/computer/group/organization unit
-   Name
-   When deleted
-   Last known parent
-   Type
-   Description
-   City
-   Country/region
-   Department
-   Employee ID
-   First name
-   Job title
-   Last name
-   SAM accountname
-   State/Province
-   Telephone number
-   UPN
-   ZIP/Postal code

You can add multiple criteria. For example, you can find all user objects deleted on September 24, 2012, from Chicago, Illinois, with a job title of Manager.

You can also add, modify, or reorder the column headers to provide more detail when evaluating which objects to recover.

For more information about ANR, see [ANR Attributes](/en-us/windows/win32/adschema/attributes-anr).

[](#single-object)

##### Single object {#single-object .heading-anchor}

Restoring deleted objects has always been a single operation. The Active Directory Administrative Center makes that operation easier. To restore a deleted object, such as a single user:

1.  Select the domain name in the navigation pane of the Active Directory Administrative Center.
2.  Double-click **Deleted Objects** in the management list.
3.  Right-click the object and then select **Restore**, or select **Restore** from the **Tasks** pane.

The object restores to its original location.

Select **Restore To** to change the restore location. This option is useful if the deleted object\'s parent container was also deleted but you don\'t want to restore the parent.

[](#multiple-peer-objects)

##### Multiple peer objects {#multiple-peer-objects .heading-anchor}

You can restore multiple peer-level objects, such as all the users in an OU. Hold down the CTRL key and select one or more deleted objects that you want to restore. Select **Restore** from the Tasks pane. You can also select all displayed objects by holding down the CTRL and A keys, or a range of objects by using SHIFT and clicking.

[](#multiple-parent-and-child-objects)

##### Multiple parent and child objects {#multiple-parent-and-child-objects .heading-anchor}

It\'s critical to understand the restoration process for a multi-parent-child restoration because the Active Directory Administrative Center can\'t restore a nested tree of deleted objects with a single action.

1.  Restore the top-most deleted object in a tree.
2.  Restore the immediate children of that parent object.
3.  Restore the immediate children of those parent objects.
4.  Repeat as necessary until all objects restore.

You can\'t restore a child object before restoring its parent. Attempting this restoration returns the following error:

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
The operation could not be performed because the object's parent is either uninstantiated or deleted.
```

The **Last Known Parent** attribute shows the parent relationship of each object. The **Last Known Parent** attribute changes from the deleted location to the restored location when you refresh the Active Directory Administrative Center after restoring a parent. Therefore, you can restore that child object when a parent object\'s location no longer shows the distinguished name of the deleted object\'s container.

Consider the scenario where an administrator accidentally deletes the Sales OU, which contains child OUs and users.

First, observe the value of the **Last Known Parent** attribute for all the deleted users and how it reads **OU=Sales\\0ADEL:*\<guid+deleted object\'s container distinguished name\>***:

Filter on the ambiguous name Sales to return the deleted OU, which you then restore:

Refresh the Active Directory Administrative Center to see the deleted user object\'s Last Known Parent attribute change to the restored Sales OU distinguished name:

Filter on all the Sales users. Hold down **CTRL + A** to select all the deleted Sales users. Select **Restore** to move the objects from the **Deleted Objects** container to the Sales OU with their group memberships and attributes intact.

If the **Sales** OU contained child OUs of its own, you should restore the child OUs first before restoring their children, and so on.

To restore all nested deleted objects by specifying a deleted parent container, see [Appendix B: Restore Multiple, Deleted Active Directory Objects (Sample Script)](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd379504(v=ws.10)).

The Active Directory Windows PowerShell cmdlet for restoring deleted objects is:

PowerShell

``` {.inner-focus data-language="powershell"}
Restore-ADObject
```

The `Restore-ADObject` cmdlet functionality didn\'t change between Windows Server 2008 R2 and Windows Server 2012.

[](#server-side-filtering)

##### Server-side filtering {#server-side-filtering .heading-anchor}

It\'s possible that over time the Deleted Objects container will accumulate more than 20,000 (or even 100,000) objects in medium and large enterprises and have difficulty showing all objects. Because the filter mechanism in Active Directory Administrative Center relies on client-side filtering, it can\'t show these additional objects. To work around this limitation, use the following steps to perform a server-side search:

1.  Right-click the **Deleted Objects** container and select **Search under this node**.
2.  Select the chevron to expose the **+Add** criteria menu, select **+Add** and add **Last modified between given dates**. The Last Modified time (the **whenChanged** attribute) is a close approximation of the deletion time. In most environments, they\'re identical. This query performs a server-side search.
3.  Locate the deleted objects to restore by using further display filtering, sorting, and so on, in the results, and then restore them normally.

[](#configuring-and-managing-fine-grained-password-policies-using-active-directory-administrative-center)

## Configuring and managing fine-grained password policies using Active Directory Administrative Center {#configuring-and-managing-fine-grained-password-policies-using-active-directory-administrative-center .heading-anchor}

[](#configuring-fine-grained-password-policies)

### Configuring fine-grained password policies {#configuring-fine-grained-password-policies .heading-anchor}

The Active Directory Administrative Center enables you to create and manage fine-grained password policy (FGPP) objects. Windows Server 2008 introduced the FGPP feature, but Windows Server 2012 has the first graphical management interface for it. You apply fine-grained password policies at a domain level, and it enables overriding the single domain password required by Windows Server 2003. If you create different FGPP with different settings, individual users or groups get differing password policies in a domain.

For information about fine-grained password policies, see [AD DS Fine-Grained Password and Account Lockout Policy Step-by-Step Guide (Windows Server 2008 R2)](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770842(v=ws.10)).

In the **Navigation** pane, select **Tree View**, select your domain, select **System**, and then select **Password Settings Container**. In the **Tasks** pane, select **New**, and then select **Password Settings**.

[](#managing-fine-grained-password-policies)

### Managing fine-grained password policies {#managing-fine-grained-password-policies .heading-anchor}

Creating a new FGPP or editing an existing one brings up the **Password Settings** editor. From here, you configure all desired password policies, as you would have in Windows Server 2008 or Windows Server 2008 R2, only now with a purpose-built editor.

Fill out all required (red asterisk) fields and any optional fields, and then select **Add** to set the users or groups that receive this policy. FGPP overrides default domain policy settings for those specified security principals. In the preceding screenshot, a restrictive policy applies only to the built-in Administrator account, to prevent compromise. The policy is far too complex for standard users to comply with, but is perfect for a high-risk account used only by IT professionals.

You also set precedence and to which users and groups the policy applies within a given domain.

The Active Directory Windows PowerShell cmdlets for fine-grained password policy are:

PowerShell

``` {.inner-focus data-language="powershell"}
Add-ADFineGrainedPasswordPolicySubject
Get-ADFineGrainedPasswordPolicy
Get-ADFineGrainedPasswordPolicySubject
New-ADFineGrainedPasswordPolicy
Remove-ADFineGrainedPasswordPolicy
Remove-ADFineGrainedPasswordPolicySubject
Set-ADFineGrainedPasswordPolicy
```

Fine-grained password policy cmdlet functionality didn\'t change between Windows Server 2008 R2 and Windows Server 2012. The following diagram illustrates the associated arguments for cmdlets:

The Active Directory Administrative Center also enables you to locate the resultant set of applied FGPP for a specific user. Right-click any user and select **View resultant password settings** to open the **Password Settings** page that applies to that user through implicit or explicit assignment:

Examining the **Properties** of any user or group shows the **Directly Associated Password Settings**, which are the explicitly assigned FGPPs:

Implicit FGPP assignment doesn\'t display here. For that, you need to use the **View resultant password settings** option.

[](#using-the-active-directory-administrative-center-windows-powershell-history-viewer)

## Using the Active Directory Administrative Center Windows PowerShell History Viewer {#using-the-active-directory-administrative-center-windows-powershell-history-viewer .heading-anchor}

The future of Windows management is Windows PowerShell. Layering graphical tools on top of a task automation framework makes the management of the most complex distributed systems consistent and efficient. You need to understand how Windows PowerShell works in order to reach your full potential and maximize your computing investments.

The Active Directory Administrative Center now provides a complete history of all the Windows PowerShell cmdlets it runs and their arguments and values. You can copy the cmdlet history elsewhere for study or modification and re-use. You can create task notes to help isolate the Windows PowerShell results for your Active Directory Administrative Center commands. You can also filter the history to find points of interest.

The purpose of the Active Directory Administrative Center Windows PowerShell History Viewer is for you to learn through practical experience.

Select the arrow to show Windows PowerShell History Viewer.

Then, create a user or modify a group\'s membership. The history viewer continually updates with a collapsed view of each cmdlet that the Active Directory Administrative Center ran with the arguments specified.

Expand any line item of interest to see all values provided to the cmdlet\'s arguments:

Select **Start Task** to create a manual notation before you use Active Directory Administrative Center to create, modify, or delete an object. Type in what you were doing. When done with your change, select **End Task**. The task note groups all of the actions performed into a collapsible note that you can use for better understanding.

For example, to see the Windows PowerShell commands used to change a user\'s password and remove the user from a group:

Selecting the **Show All** box also shows the Get-\* verb Windows PowerShell cmdlets that only retrieve data.

The history viewer shows the literal commands run by the Active Directory Administrative Center. You might note that some cmdlets appear to run unnecessarily. For example, you can create a new user with:

PowerShell

``` {.inner-focus data-language="powershell"}
New-ADUser
```

The Active Directory Administrative Center design required minimal code usage and modularity. Therefore, instead of a set of functions that create new users and another set that modify existing users, it minimally does each function and then chains them together with the cmdlets. Keep this in mind when you\'re learning Active Directory Windows PowerShell. You can also use that as a learning technique, where you see how simply you can use Windows PowerShell to complete a single task.

[](#manage-different-domains-in-active-directory-administrative-center)

## Manage different domains in Active Directory Administrative Center {#manage-different-domains-in-active-directory-administrative-center .heading-anchor}

When you open Active Directory Administrative Center, the domain that you\'re currently logged on to on this computer (the local domain) appears in the Active Directory Administrative Center navigation pane (the left pane). Depending on the rights of your current set of sign-in credentials, you can view or manage the Active Directory objects in this local domain.

You can also use the same set of sign-in credentials and the same instance of Active Directory Administrative Center to view or manage Active Directory objects in any other domain in the same forest, or a domain in another forest that has an established trust with the local domain. Both one-way trusts and two-way trusts are supported. There\'s no minimum group membership required to complete this procedure.

Note

If there\'s a one-way trust between domain A and domain B through which users in domain A can access resources in domain B but users in domain B can\'t access resources in domain A, if you\'re running Active Directory Administrative Center on the computer where domain A is your local domain, you can connect to domain B with the current set of sign-in credentials and in the same instance of Active Directory Administrative Center.

But if you\'re running Active Directory Administrative Center on the computer where domain B is your local domain, you can\'t connect to domain A with the same set of credentials in the same instance of the Active Directory Administrative Center.

[](#windows-server-2012-to-manage-a-foreign-domain-in-the-selected-instance-of-active-directory-administrative-center-using-the-current-set-of-sign-in-credentials)

### Windows Server 2012: To manage a foreign domain in the selected instance of Active Directory Administrative Center using the current set of sign-in credentials {#windows-server-2012-to-manage-a-foreign-domain-in-the-selected-instance-of-active-directory-administrative-center-using-the-current-set-of-sign-in-credentials .heading-anchor}

1.  To open Active Directory Administrative Center, in **Server Manager**, select **Tools**, and then select **Active Directory Administrative Center**.

2.  To open Add Navigation Nodes, select **Manage**, and then select **Add Navigation Nodes**.

3.  In **Add Navigation Nodes**, select **Connect to other domains**.

4.  In **Connect to**, type the name of the foreign domain that you want to manage (for example, `contoso.com`), and then select **OK**.

5.  When you\'re successfully connected to the foreign domain, browse through the columns in the **Add Navigation Nodes** window, select the container or containers to add to your Active Directory Administrative Center navigation pane, and then select **OK**.

[](#windows-server-2008-r2-to-manage-a-foreign-domain-in-the-selected-instance-of-active-directory-administrative-center-using-the-current-set-of-sign-in-credentials)

### Windows Server 2008 R2: To manage a foreign domain in the selected instance of Active Directory Administrative Center using the current set of sign-in credentials {#windows-server-2008-r2-to-manage-a-foreign-domain-in-the-selected-instance-of-active-directory-administrative-center-using-the-current-set-of-sign-in-credentials .heading-anchor}

1.  To open Active Directory Administrative Center, select **Start**, select **Administrative Tools**, and then select **Active Directory Administrative Center**.

    Tip

    Another way to open Active Directory Administrative Center is to select **Start**, select **Run**, and then type **dsac.exe**.

2.  Then open Add Navigation Nodes, near the top of the Active Directory Administrative Center window, select **Add Navigation Nodes**.

    Tip

    Another way to open Add Navigation Nodes is to right-click anywhere in the empty space in the Active Directory Administrative Center navigation pane and then select **Add Navigation Nodes**.

3.  In **Add Navigation Nodes**, select **Connect to other domains**.

4.  In **Connect to**, type the name of the foreign domain that you want to manage (for example, `contoso.com`), and then select **OK**.

5.  When you\'re successfully connected to the foreign domain, browse through the columns in the **Add Navigation Nodes** window, select the container or containers to add to your Active Directory Administrative Center navigation pane, and then select **OK**.

[](#manage-a-domain-using-sign-in-credentials-that-are-different-from-the-current-set-of-sign-in-credentials)

### Manage a domain using sign-in credentials that are different from the current set of sign-in credentials {#manage-a-domain-using-sign-in-credentials-that-are-different-from-the-current-set-of-sign-in-credentials .heading-anchor}

To open Active Directory Administrative Center at the command prompt, type the following command, and then select **Enter**:

Windows Command Prompt

``` {.inner-focus data-language="cmd"}
runas /user:<domain\user> dsac
```

`<domain\user>` is the set of credentials that you want to open Active Directory Administrative Center with, and `dsac` is the Active Directory Administrative Center executable file name.

When Active Directory Administrative Center is open, browse through the navigation pane to view or manage your Active Directory domain.

[](#troubleshooting-ad-ds-management)

## Troubleshooting AD DS management {#troubleshooting-ad-ds-management .heading-anchor}

[](#troubleshooting-options)

### Troubleshooting options {#troubleshooting-options .heading-anchor}

[](#logging-options)

#### Logging Options {#logging-options .heading-anchor}

The Active Directory Administrative Center now contains built-in logging, as part of a tracing config file. Create/modify the following file in the same folder as dsac.exe:

**dsac.exe.config**

Create the following contents:

XML

``` {.inner-focus data-language="xml"}
<appSettings>
  <add key="DsacLogLevel" value="Verbose" />
</appSettings>
<system.diagnostics>
 <trace autoflush="false" indentsize="4">
  <listeners>
   <add name="myListener"
    type="System.Diagnostics.TextWriterTraceListener"
    initializeData="dsac.trace.log" />
   <remove name="Default" />
  </listeners>
 </trace>
</system.diagnostics>
```

The verbosity levels for **DsacLogLevel** are **None**, **Error**, **Warning**, **Info**, and **Verbose**. The output file name is configurable and writes to the same folder as dsac.exe. The output can tell you more about how Active Directory Administrative Center is operating, which domain controllers it contacted, what Windows PowerShell commands ran, what the responses were, and further details.

For example, when you use the **Info** level, which returns all results except the trace-level verbosity:

-   DSAC.exe starts.

-   Logging starts.

-   The domain controller is requested to return initial domain information.

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
    [12:42:49][TID 3][Info] Command Id, Action, Command, Time, Elapsed Time ms (output), Number objects (output)
    [12:42:49][TID 3][Info] 1, Invoke, Get-ADDomainController, 2012-04-16T12:42:49
    [12:42:49][TID 3][Info] Get-ADDomainController-Discover:$null-DomainName:"CORP"-ForceDiscover:$null-Service:ADWS-Writable:$null
    ```

-   Domain controller DC1 returned from domain Corp.

-   PS Active Directory virtual drive loaded.

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
    [12:42:49][TID 3][Info] 1, Output, Get-ADDomainController, 2012-04-16T12:42:49, 1
    [12:42:49][TID 3][Info] Found the domain controller 'DC1' in the domain 'CORP'.
    [12:42:49][TID 3][Info] 2, Invoke, New-PSDrive, 2012-04-16T12:42:49
    [12:42:49][TID 3][Info] New-PSDrive-Name:"ADDrive0"-PSProvider:"ActiveDirectory"-Root:""-Server:"dc1.corp.contoso.com"
    [12:42:49][TID 3][Info] 2, Output, New-PSDrive, 2012-04-16T12:42:49, 1
    [12:42:49][TID 3][Info] 3, Invoke, Get-ADRootDSE, 2012-04-16T12:42:49
    ```

-   Get domain root DSE information.

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
    [12:42:49][TID 3][Info] Get-ADRootDSE -Server:"dc1.corp.contoso.com"
    [12:42:49][TID 3][Info] 3, Output, Get-ADRootDSE, 2012-04-16T12:42:49, 1
    [12:42:49][TID 3][Info] 4, Invoke, Get-ADOptionalFeature, 2012-04-16T12:42:49
    ```

-   Get domain Active Directory recycle bin information.

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
    [12:42:49][TID 3][Info] Get-ADOptionalFeature -LDAPFilter:"(msDS-OptionalFeatureFlags=1)" -Server:"dc1.corp.contoso.com"
    [12:42:49][TID 3][Info] 4, Output, Get-ADOptionalFeature, 2012-04-16T12:42:49, 1
    [12:42:49][TID 3][Info] 5, Invoke, Get-ADRootDSE, 2012-04-16T12:42:49
    [12:42:49][TID 3][Info] Get-ADRootDSE -Server:"dc1.corp.contoso.com"
    [12:42:49][TID 3][Info] 5, Output, Get-ADRootDSE, 2012-04-16T12:42:49, 1
    [12:42:49][TID 3][Info] 6, Invoke, Get-ADRootDSE, 2012-04-16T12:42:49
    [12:42:49][TID 3][Info] Get-ADRootDSE -Server:"dc1.corp.contoso.com"
    [12:42:49][TID 3][Info] 6, Output, Get-ADRootDSE, 2012-04-16T12:42:49, 1
    [12:42:49][TID 3][Info] 7, Invoke, Get-ADOptionalFeature, 2012-04-16T12:42:49
    [12:42:49][TID 3][Info] Get-ADOptionalFeature -LDAPFilter:"(msDS-OptionalFeatureFlags=1)" -Server:"dc1.corp.contoso.com"
    [12:42:50][TID 3][Info] 7, Output, Get-ADOptionalFeature, 2012-04-16T12:42:50, 1
    [12:42:50][TID 3][Info] 8, Invoke, Get-ADForest, 2012-04-16T12:42:50
    ```

-   Get Active Directory forest.

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
    [12:42:50][TID 3][Info] Get-ADForest -Identity:"corp.contoso.com" -Server:"dc1.corp.contoso.com"
    [12:42:50][TID 3][Info] 8, Output, Get-ADForest, 2012-04-16T12:42:50, 1
    [12:42:50][TID 3][Info] 9, Invoke, Get-ADObject, 2012-04-16T12:42:50
    ```

-   Get schema information for supported encryption types, FGPP, and certain user information.

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
    [12:42:50][TID 3][Info] Get-ADObject
    -LDAPFilter:"(|(ldapdisplayname=msDS-PhoneticDisplayName)(ldapdisplayname=msDS-PhoneticCompanyName)(ldapdisplayname=msDS-PhoneticDepartment)(ldapdisplayname=msDS-PhoneticFirstName)(ldapdisplayname=msDS-PhoneticLastName)(ldapdisplayname=msDS-SupportedEncryptionTypes)(ldapdisplayname=msDS-PasswordSettingsPrecedence))"
    -Properties:lDAPDisplayName
    -ResultPageSize:"100"
    -ResultSetSize:$null
    -SearchBase:"CN=Schema,CN=Configuration,DC=corp,DC=contoso,DC=com"
    -SearchScope:"OneLevel"
    -Server:"dc1.corp.contoso.com"
    [12:42:50][TID 3][Info] 9, Output, Get-ADObject, 2012-04-16T12:42:50, 7
    [12:42:50][TID 3][Info] 10, Invoke, Get-ADObject, 2012-04-16T12:42:50
    ```

-   Get all information about the domain object to display to administrator who clicked on the domain head.

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
    [12:42:50][TID 3][Info] Get-ADObject
    -IncludeDeletedObjects:$false
    -LDAPFilter:"(objectClass=*)"
    -Properties:allowedChildClassesEffective,allowedChildClasses,lastKnownParent,sAMAccountType,systemFlags,userAccountControl,displayName,description,whenChanged,location,managedBy,memberOf,primaryGroupID,objectSid,msDS-User-Account-Control-Computed,sAMAccountName,lastLogonTimestamp,lastLogoff,mail,accountExpires,msDS-PhoneticCompanyName,msDS-PhoneticDepartment,msDS-PhoneticDisplayName,msDS-PhoneticFirstName,msDS-PhoneticLastName,pwdLastSet,operatingSystem,operatingSystemServicePack,operatingSystemVersion,telephoneNumber,physicalDeliveryOfficeName,department,company,manager,dNSHostName,groupType,c,l,employeeID,givenName,sn,title,st,postalCode,managedBy,userPrincipalName,isDeleted,msDS-PasswordSettingsPrecedence
    -ResultPageSize:"100"
    -ResultSetSize:"20201"
    -SearchBase:"DC=corp,DC=contoso,DC=com"
    -SearchScope:"Base"
    -Server:"dc1.corp.contoso.com"
    ```

Setting the **Verbose** level also shows the .NET stacks for each function, but these don\'t include enough data to be useful except when you\'re troubleshooting after the dsac.exe suffers an access violation or crash. The two likely causes of this issue are:

-   Active Directory Web Services isn\'t running on any accessible domain controllers.
-   Network communications are blocked to Active Directory Web Services from the computer running Active Directory Administrative Center.

Important

There\'s also an out-of-band version of the service called the [Active Directory Management Gateway](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd391908(v=ws.10)#what-does-the-active-directory-management-gateway-service-do), which runs on Windows Server 2008 SP2 and Windows Server 2003 SP2.

The following errors are shown when no Active Directory Web Services instances are available:

  Error                                                                                                                                 Operation
  ------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------
  \"Cannot connect to any domain. Refresh or try again when connection is available\"                                                   Shown at start of the Active Directory Administrative Center application
  \"Cannot find an available server in the *\<NetBIOS domain name\>* domain that is running the Active Directory Web Service (ADWS)\"   Shown when you try to select a domain node in the Active Directory Administrative Center application

To troubleshoot this issue, use these steps:

1.  Validate that Active Directory Web Services is started on at least one domain controller in the domain (and preferably on all domain controllers in the forest). Ensure that it\'s set to start automatically on all domain controllers.

2.  From the computer running the Active Directory Administrative Center, validate that you can locate a server running Active Directory Web Services by running these NLTest.exe commands:

    ``` {.inner-focus data-language=""}
    nltest /dsgetdc:<domain NetBIOS name> /ws /force
    nltest /dsgetdc:<domain fully qualified DNS name> /ws /force
    ```

    If those tests fail even though Active Directory Web Services is running, the issue is with name resolution or LDAP and not Active Directory Web Services or Active Directory Administrative Center. This test fails with error \"1355 0x54B ERROR_NO_SUCH_DOMAIN\" if Active Directory Web Services isn\'t running on any domain controllers though, so double-check before reaching any conclusions.

3.  On the domain controller returned by Nltest, dump the listening port list with this command:

    ``` {.inner-focus data-language=""}
    Netstat -anob > ports.txt
    ```

    Examine the ports.txt file and validate that the Active Directory Web Services service is listening on port 9389. For example:

    ``` {.inner-focus data-language=""}
    TCP    0.0.0.0:9389    0.0.0.0:0    LISTENING    1828
    [Microsoft.ActiveDirectory.WebServices.exe]

    TCP    [::]:9389       [::]:0       LISTENING    1828
    [Microsoft.ActiveDirectory.WebServices.exe]
    ```

    If the service is listening, validate the Windows Firewall rules and ensure that they allow 9389 TCP inbound. By default, domain controllers enable firewall rule \"Active Directory Web Services (TCP-in).\" If the service isn\'t listening, validate again that it\'s running on this server and restart it. Validate that no other process is already listening on port 9389.

4.  Install NetMon or another network capture utility on the computer running Active Directory Administrative Center and on the domain controller returned by Nltest. Gather simultaneous network captures from both computers, where you start Active Directory Administrative Center and see the error before stopping the captures. Validate that the client is able to send to and receive from the domain controller on port TCP 9389. If packets are sent but never arrive, or they arrive and the domain controller replies but they never reach the client, it\'s likely that there\'s a firewall in between the computers on the network dropping packets on that port. This firewall can be software or hardware, and can be part of non-Microsoft endpoint protection (antivirus) software.

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Active Directory Recycle Bin, fine-grained password policy, and PowerShell History Viewer](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831702(v=ws.11))

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Use the Active Directory Administrative Center Windows PowerShell History Viewer in Windows Server](/en-us/windows-server/identity/ad-ds/get-started/adac/use-active-directory-administrative-center-powershell-history?source=recommendations)

    Learn how to use the Windows PowerShell History Viewer in Active Directory Administrative Center to construct Windows PowerShell scripts.

-   [Manage User Accounts with Active Directory Users and Computers in Windows Server](/en-us/windows-server/identity/ad-ds/manage-user-accounts-in-windows-server?source=recommendations)

    Create, delete, and manage user accounts in Active Directory Users and Computers. Learn how to manage user account properties, group memberships, and passwords.

-   [Active Directory Domain Services overview](/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview?source=recommendations)

    Find out about Active Directory Domain Services, a directory service that makes network resource data available to authorized network users and administrators.

-   [Install Active Directory Domain Services on Windows Server](/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-?source=recommendations)

    Learn more about how to install Active Directory Domain Services in Windows Server using PowerShell, or Server Manager.

-   [Solutions and Scenario Guides](/en-us/windows-server/identity/solution-guides/solutions-and-scenario-guides?source=recommendations)

    Learn more about: Solutions and Scenario Guides

-   [AD DS Simplified Administration](/en-us/windows-server/identity/ad-ds/manage/ad-ds-simplified-administration?source=recommendations)

    Learn more about: AD DS Simplified Administration

-   [Overview of Active Directory Domain Services](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/active-directory-domain-services-overview?source=recommendations)

    Learn about how Active Directory Domain Services, provides the methods for storing directory data and making this data available to network users and administrators.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 07/08/2025
