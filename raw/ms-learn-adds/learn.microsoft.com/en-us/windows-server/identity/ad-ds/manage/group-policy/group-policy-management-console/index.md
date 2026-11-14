---
{"title": "Group Policy Management Console", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-management-console", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Group Policy Management Console

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

The Group Policy Management Console (GPMC) provides unified management of all aspects of Group Policy across multiple forests in an organization. The GPMC lets you manage all Group Policy Objects (GPOs), Windows Management Instrumentation (WMI) filters, and Group Policy--related permissions in your network. Think of the GPMC as your primary access point to Group Policy, with all the Group Policy management tools available from the GPMC interface.

The GPMC consists of a set of scriptable interfaces for managing Group Policy and an MMC-based user interface (UI). The GPMC is included with Windows Server and the Remote Server Administration Tools.

The GPMC provides the following capabilities:

-   Import and exporting GPOs.
-   Copy and pasting GPOs.
-   Back up and restoring GPOs.
-   Search for existing GPOs.
-   Report capabilities.
-   Group Policy Modeling. Allows you to simulate Resultant Set of Policy (RsoP) data for planning Group Policy deployments before implementing them in the production environment.
-   Group Policy Results. Allows you to view GPO interaction and to troubleshoot Group Policy deployments.
-   Support for migration tables to facilitate the importing and copying of GPOs across domains and across forests. A migration table is a file that maps references to users, groups, computers, and Universal Naming Convention (UNC) paths in the source GPO to new values in the destination GPO.
-   Reporting GPO settings and RSoP data in HTML reports that you can save and print.
-   Scriptable interfaces that allow all operations that are available within the GPMC. You can\'t use scripts to edit individual policy settings in a GPO.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

To use the GPMC, you must complete the following prerequisites.

-   Have the Group Policy Management feature installed on a computer running Windows Server or a Windows client operating system.
-   Have *Edit settings*, *delete*, and *modify* security permissions on the GPO.
-   To link GPOs, you need the *modify* permission on that site, domain, or OU. By default, only Domain Administrators and Enterprise Administrators have this permission.
    -   Users and groups with permission to link GPOs to a specific site, domain, or OU can link GPOs, change link order, and set block inheritance on that site, domain, or OU.

[](#create-an-unlinked-gpo)

## Create an unlinked GPO {#create-an-unlinked-gpo .heading-anchor}

To create an unlinked GPO, perform the following steps:

1.  To open the GPMC, select **Start**, enter **Group Policy Management** in the search box, and then select **Group Policy Management**.
2.  In the GPMC console tree, right-click **Group Policy Objects** in the forest and domain in which you want to create a new unlinked GPO.
3.  Select **New**.
4.  In the New GPO dialog box, specify a name for the new GPO, and then select **OK**.

[](#edit-an-existing-gpo)

## Edit an existing GPO {#edit-an-existing-gpo .heading-anchor}

To change policy settings within an existing GPO, perform the following steps:

1.  In the GPMC console tree, expand Group Policy Objects in the forest and domain containing the GPO that you want to edit.
2.  Right-click the GPO that you want to edit, and then select **Edit**.
3.  In the console tree of the Group Policy Management Editor, expand items as needed to locate the policy item that contains the policy settings that you want to modify. Select an item to view the associated policy settings in the details pane.
4.  In the details pane, double-click the names of the policy setting that you want to edit.
5.  In the Properties dialog box, modify policy settings as needed, and then select **OK**.
6.  After completing the necessary modifications, close the Group Policy Management Editor.

[](#link-a-gpo)

## Link a GPO {#link-a-gpo .heading-anchor}

The primary way to apply the policy settings in a GPO to users and computers is by linking the GPO to a container in Active Directory. GPOs can be linked to three types of containers in Active Directory: sites, domains, and organizational units (OUs). A GPO can be linked to multiple Active Directory containers.

GPOs are stored on a per-domain basis. For example, if you link a GPO to an OU, the GPO isn\'t stored in that OU. A GPO is a per-domain object that can be linked anywhere in the forest. The UI in the GPMC helps clarify the distinction between links and actual GPOs.

In the GPMC, you can link an existing GPO to Active Directory containers by using either of the following methods:

-   Right-click a site, domain, or OU item, and then select **Link an Existing GPO**. This procedure requires that the GPO already exist in the domain.
-   Drag a GPO from under the Group Policy Objects item to the OU to which you want to link the GPO. This drag-and-drop functionality works only within the same domain.

[](#change-gpo-link-order)

## Change GPO link order {#change-gpo-link-order .heading-anchor}

Within each site, domain, and OU, the link order controls the order in which GPOs are applied. To change the precedence of a link, you can change the link order, moving each link up or down in the list to the appropriate location. Links with the lowest number have higher precedence for a given site, domain, or OU.

For example, you want the last GPO that you added to have the highest precedence. You can adjust the link order of the GPO to a link order of 1 to make it the highest. To change the link order for GPO links for a site, domain, or OU, use the GPMC.

[](#unlink-a-gpo-from-a-site-domain-or-ou)

## Unlink a GPO from a site, domain, or OU {#unlink-a-gpo-from-a-site-domain-or-ou .heading-anchor}

Unlinking a GPO means that the linked GPO no longer applies to the location where it was originally linked. To unlink a GPO:

1.  In the GPMC console tree, expand Group Policy Objects in the forest and domain containing the GPO that you want to unlink.
2.  Select the GPO that you want to unlink.
3.  In the details pane, select the **Scope** tab.
4.  In the Links section, right-click the Active Directory object with the link you want to delete, and then select **Delete Link(s)**.

Deleting a link to a GPO is different than deleting a GPO. If a GPO link the GPO remains available. Other links from other domains to that GPO also remain present. When you delete a GPO, you\'re prompted to delete the GPO and all links to it in the selected domain. Doing the GPO and all links doesn\'t delete links to the GPO from other domains. Be sure to remove links to the GPO in other domains before deleting this GPO from this domain.

[](#disable-user-configuration-or-computer-configuration-settings-in-a-gpo)

## Disable User Configuration or Computer Configuration settings in a GPO {#disable-user-configuration-or-computer-configuration-settings-in-a-gpo .heading-anchor}

To create a GPO to set only user-related policy settings, disable the Computer Configuration settings in the GPO. Disabling the computer configure slightly reduces computer startup time because the Computer Configuration settings in the GPO don\'t have to be evaluated. If you\'re configuring only computer-related policy settings, disable the User Configuration settings in the GPO. To disable User Configuration or Computer configuration:

1.  In the GPMC console tree, expand Group Policy Objects in the forest and domain containing the GPO that contains the policy settings you want to disable.
2.  Right-click the GPO that contains the policy settings that you want to disable.
3.  In the GPO Status list, select one of the following options:
    -   All policy settings disabled
    -   Computer configuration settings disabled
    -   Enabled (default)
    -   User configuration settings disabled

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Group Policy Processing](group-policy-processing)
-   [Backing up, restoring, migrating, and copying Group Policy Objects (GPOs)](group-policy-backup-restore)
-   [Group Policy Modeling and Group Policy Results](group-policy-modeling-results)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Group Policy processing for Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing?source=recommendations)

    Learn about how Group Policy processing works in Active Directory Domain Services on Windows Server and Windows client computers.

-   [Back Up and Restore Group Policy in Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-backup-restore?source=recommendations)

    Learn how to back up, restore, migrate, and copy Group Policy Objects by using the Group Policy Management Console in Windows.

-   [Group Policy overview for Windows Server](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview?source=recommendations)

    Learn about what Group Policy does and how it works with Active Directory Domain Services in Windows.

-   [Group Policy preferences in Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-preferences?source=recommendations)

    Group Policy Preferences allow administrators to configure, deploy, and manage user and computer settings in Active Directory with greater flexibility in Windows.

-   [Group Policy scope in Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-scope?source=recommendations)

    Learn about how Group Policy scope defines specific users, computers, and organizational units within an Active Directory environment in Windows.

-   [Group Policy Modeling and Results in Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-modeling-results?source=recommendations)

    Learn how to model group policy results and evaluate group policy settings using the Group Policy Management Console in Windows Server.

-   [Export a GPO to a File - Microsoft Desktop Optimization Pack](/en-us/microsoft-desktop-optimization-pack/agpm/export-a-gpo-to-a-file?source=recommendations)

    Export a GPO to a File

Training

Module

[Implement Group Policy Objects - Training](/en-us/training/modules/implement-group-policy-objects/?source=recommendations)

Implement Group Policy Objects

------------------------------------------------------------------------

-    Last updated on 05/14/2025
