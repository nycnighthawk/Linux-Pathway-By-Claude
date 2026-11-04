---
{"title": "Back up, restore, migrate, and copy Group Policy Objects", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-backup-restore", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Back up, restore, migrate, and copy Group Policy Objects

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This article describes how to back up, restore, migrate, and copy existing Group Policy Objects (GPOs) by using the Group Policy Management Console (GPMC). These capabilities are important for protecting your Group Policy deployments against errors or disasters. They help you avoid having to manually recreate lost or damaged GPOs and repeat the planning, testing, and deployment phases. Part of your ongoing Group Policy operations plan should include regular backups of all GPOs.

You can also copy and import GPOs, both from the same domain and across domains. You can use the GPMC to migrate an existing GPO, for example, from an existing domain into a newly deployed domain. You can either copy GPOs or import policy settings from one GPO into another GPO. Importing GPOs allows you to transfer policy settings from a backed-up GPO into an existing GPO and is especially useful in situations where a trust relationship isn\'t present between the source and destination domains. If you want to reuse existing GPOs, copying also allows you to conveniently move GPOs from one production environment to another.

[](#back-up-gpos-and-view-gpo-backups)

## Back up GPOs and view GPO backups {#back-up-gpos-and-view-gpo-backups .heading-anchor}

The backup operation backs up a production GPO to the file system. The location of the backup can be any folder to which you have write access. After backing up GPOs, you must use the GPMC to display and manipulate the contents of your backup folder, either by using the GPMC directly or programmatically by using a script. After the GPOs are backed up, use the GPMC to process archived GPOs by using the import and restore operations.

Caution

Don\'t interact with archived GPOs directly through the file system.

You can back up multiple instances of the same GPO to the same location because the GPMC uniquely identifies each backup instance. This mechanism allows you to pick the instance of the archived GPO with which you want to work. For example, you can choose to display only the most recent backups when viewing the contents of a backup folder through the GPMC.

[](#back-up-all-gpos-in-a-domain)

### Back up all GPOs in a domain {#back-up-all-gpos-in-a-domain .heading-anchor}

To back up all GPOs in a domain, perform the following steps:

1.  To open the GPMC, select **Start**, enter **Group Policy Management** in the search box, and then select **Group Policy Management**.

2.  In the GPMC console tree, expand the forest or domain that contains the GPOs that you want to back up.

3.  Right-click **Group Policy Objects**, and then select **Back Up All**.

4.  In the **Back Up Group Policy Object** dialog, enter the path to the location where you want to store the GPO backups and enter a description. Alternatively, you can select **Browse**, locate the folder in which you want to store the GPO backups, and then select **OK**. Select **Back Up**.

5.  After the backup operation completes, a summary will list how many GPOs were successfully backed up and any GPOs that weren\'t backed up. Select **OK** to return to the GPMC.

[](#back-up-a-specific-gpo)

### Back up a specific GPO {#back-up-a-specific-gpo .heading-anchor}

To back up a specific GPO, perform the following steps:

1.  In the GPMC console tree, expand Group Policy Objects in the forest or domain that contains the GPO that you want to back up.

2.  Right-click the GPO you want to back up, and then select **Back Up**.

3.  In the **Backup Group Policy Object** dialog, enter the path to the location where you want to store the GPO backups and enter a description. Alternatively, you can select **Browse**, locate the folder in which you want to store the GPO backups, and then select **OK**. Select **Back Up**.

4.  After the backup operation completes, a summary will list how many GPOs were successfully backed up and any GPOs that weren\'t backed up. Select **OK** to return to the GPMC.

[](#view-gpo-backups)

### View GPO backups {#view-gpo-backups .heading-anchor}

To view a list of backed up GPOs, perform the following steps:

1.  In the GPMC console tree, expand the forest or domain that contains the GPOs that you want to back up.

2.  Right-click **Group Policy Objects**, and the select **Manage Backups**.

3.  In the **Manage Backups** dialog, enter the path to the location where you stored the GPO backups that you want to view. Alternatively, you can select **Browse**, locate the folder that contains the GPO backups, and then select **OK**.

4.  To specify that only the most recent version of the GPOs are displayed in the **Backed up GPOs** list, select the **Show only the latest version of each GPO** checkbox. Select **Close**.

[](#restore-gpos)

## Restore GPOs {#restore-gpos .heading-anchor}

You can also restore GPOs. This operation restores a backed-up GPO to the same domain from which it was backed up. You can\'t restore a GPO from a backup into a domain that\'s different from the GPO's original domain. To restore a previous version of an existing GPO, perform the following steps:

1.  In the GPMC console tree, expand Group Policy Objects in the forest or domain that contains the GPOs that you want to restore.

2.  Right-click the GPO that you want to restore to a previous version, and then select **Restore from Backup**.

3.  Select **Next** to get started.

4.  Enter the path to the location where the GPO backups are located, and then select **Next**.

5.  Select the backed-up GPO that you want to restore, and then select **Next**.

6.  Select **Finish** to restore the GPO.

To restore a deleted GPO, perform the following steps:

1.  In the GPMC console tree, expand the forest or domain that contains the GPO that you want to restore.

2.  Right-click **Group Policy Objects**, and then select **Manage Backups**.

3.  In the **Manage Backups** dialog, select **Browse**, and then locate the file that contains your backed-up GPOs.

4.  In the **Backed up GPOs** list, select the GPO that you want to restore, and then select **Restore**.

5.  When you\'re prompted to confirm the restore operation, select **OK**.

6.  After the restore operation completes, a summary will state whether the restore succeeded. Select **OK**, and then select **Close**.

[](#copy-gpos)

## Copy GPOs {#copy-gpos .heading-anchor}

The GPMC allows you to copy GPOs, both in the same domain and across domains, and import Group Policy settings from one GPO to another. Perform these operations as part of your staging process before deployment in your production environment. These operations are also useful for migrating GPOs from one production environment to another.

Although the collection of policy settings that comprises a GPO is logically a single entity, the data for a single GPO is stored in multiple locations and in various formats. Some data is contained in Active Directory and other data is stored in the Sysvol folder on domain controllers. This means that you can\'t copy GPOs by copying a folder from one computer to another.

A copy operation copies an existing, current GPO to the desired destination domain. A new GPO is always created as part of this process. The destination domain can be any trusted domain in which you have the right to create new GPOs. Add the desired forests and domains in the GPMC and use the GPMC to copy and paste (or drag and drop) the desired GPOs from one domain to another. To copy a GPO, you must have permission to create GPOs in the destination domain.

When copying GPOs, you can also copy the Discretionary Access Control List (DACL) on the GPO, in addition to the policy settings within the GPO. This is useful for ensuring that the new GPO that is created as part of the copy operation has the same security filtering and delegation options as the original GPO.

Importing a GPO allows you to transfer policy settings from a backed-up GPO to an existing GPO. Importing a GPO transfers only the GPO settings. It doesn\'t modify the existing security filtering or links on the destination GPO. Importing a GPO is useful for migrating GPOs across untrusted environments, because you only need access to the backed-up GPO, not the production GPO. Because an import operation only modifies policy settings, edit permissions on the destination GPO are sufficient to perform the operation.

When copying or importing a GPO, you can specify a migration table if the GPO contains security principals or UNC paths that might need to be updated when they\'re copied to the target domain. You use the Migration Table Editor (MTE) to create and edit migration tables. Migration tables are described later in this article.

To copy a GPO, perform the following steps:

1.  In the GPMC console tree, expand **Group Policy Objects** in the forest and domain containing the GPO that you want to copy.

2.  Right-click the GPO that you want to copy, and then select **Copy**.

3.  Perform one of the following actions:

    -   To place the copy of the GPO in the same domain as the source GPO, right-click **Group Policy Objects**, and then select **Paste**.
    -   To place the copy of the GPO in a different domain (either in the same or a different forest), expand the destination domain, right-click **Group Policy Objects**, and then select **Paste**.
    -   If you\'re copying within a domain, select **Use the default permissions for new GPOs** or **Preserve the existing permissions**, and then select **OK**.

4.  If you\'re copying to or from another domain, follow the instructions in the wizard that opens, and then select **Finish**.

[](#import-gpo-settings)

## Import GPO settings {#import-gpo-settings .heading-anchor}

To import policy settings from a backed-up GPO into another GPO, perform the following steps:

1.  In the GPMC console tree, expand **Group Policy Objects** in the forest and domain containing the GPO into which you want to import policy settings.

2.  Right-click the GPO that you want to import policy settings, and then select **Import Settings**.

3.  In the **Import Settings Wizard** dialog, select **Next** to get started.

4.  Select **Next**, or optionally, select **Backup**.

    1.  *Optional:* In the **Backup Group Policy Object** dialog, enter the path to the location where you want to store the GPO backups and enter a description. Alternatively, you can select **Browse**, locate the folder in which you want to store the GPO backups, and then select **OK**. Select **Back Up**.

    2.  After the backup operation completes, a summary will list how many GPOs were successfully backed up and any GPOs that weren\'t backed up. Select **OK** to return to the **Import Settings Wizard**, then select **Next**.

5.  Enter the path to the location where the GPO backups are located, then select **Next**.

6.  Select the backed-up GPO that you want to import, and then select **Next**.

7.  Review the scan results, and then select **Next**.

8.  Select **Finish** to import the GPO.

9.  After the import operation completes, a summary will state whether the import succeeded. Select **OK**.

[](#migration-tables)

## Migration tables {#migration-tables .heading-anchor}

Because some data in a GPO is domain-specific and might not be valid when copied directly to another domain, the GPMC provides migration tables. A migration table is a simple table that specifies a mapping between a source value and a destination value.

A migration table converts, during the copy or import operation, the references in a GPO to new references that work in the target domain. You can use migration tables to update security principals and UNC paths to new values as part of the import or copy operation. Migration tables are stored with the file name extension `.migtable` and are actually XML files. You don\'t need to know XML to create or edit migration tables. The GPMC provides the Migration Table Editor (MTE) for manipulating migration tables.

A migration table consists of one or more mapping entries. Each mapping entry consists of a source type, source reference, and destination reference. If you specify a migration table when performing an import or copy operation, each reference to the source entry is replaced with the destination entry when the policy settings are written into the destination GPO. Before you use a migration table, ensure that the destination references specified in the migration table already exist.

The following items can contain security principals and can be modified by using a migration table:

-   Security policy settings of the following types:

    -   User rights assignment
    -   Restricted groups
    -   System services
    -   File system
    -   Registry

-   Advanced folder redirection policy settings

-   The GPO DACL, if you choose to preserve it during a copy operation

-   The DACL on software installation objects, which is only preserved if the option to copy the GPO DACL is specified

The following items can contain UNC paths, which might need to be updated to new values as part of the import or copy operation. For example, servers in the original domain might not be accessible from the domain to which the GPO is being migrated.

-   Folder redirection Group Policy settings
-   Software installation Group Policy settings

References to scripts (such as for logon and startup scripts) that are stored outside the source GPO. The script itself isn\'t copied as part of the GPO copy or import operation, unless the script is stored inside the source GPO.

To create a migration table that maps an example UNC path, perform the following steps:

1.  In the GPMC console tree, expand **Group Policy Objects** in the forest and domain.

2.  Right-click **Group Policy Objects**, and then select **Open Migration Tables Editor**.

3.  From the menu, select **Tools** and then **Populate from GPO**.

4.  In the **Select GPO** dialog, select the GPO that contains the UNC path that you want to map, and then select **OK**.

5.  Enter the new destination value for the UNC path.

6.  From the menu, select **File** and then **Save As**.

7.  Browse to a location you want to use. Enter a name for the migration table, and then select **Save**.

To use a migration table during a copy or import operation, perform the following steps:

1.  In the GPMC console tree, expand **Group Policy Objects** in the forest and domain containing the GPO into which you want to import policy settings.

2.  Right-click the GPO into which you want to import policy settings, and then select **Import Settings**.

3.  In the **Import Settings Wizard** dialog, select **Next** to get started.

4.  Select **Next**, or optionally, select **Backup**.

    1.  *Optional:* In the **Backup Group Policy Object** dialog, enter the path to the location where you want to store the GPO backups and then enter a description. Alternatively, you can select **Browse**, locate the folder in which you want to store the GPO backups, and then select **OK**. Select **Back Up**.

    2.  After the backup operation completes, a summary will list how many GPOs were successfully backed up and any GPOs that weren\'t backed up. Select **OK** to return to the **Import Settings Wizard**, and then select **Next**.

5.  Enter the path to the location where the GPO backups are located, and then select **Next**.

6.  Select the backed-up GPO that you want to import, and then select **Next**.

7.  Review the scan results, and then select **Next**.

8.  Select **Using this migration table to map them in the destination GPO**, and then select **Browse** to locate the migration table you want to use. Select **Next**.

9.  Select **Finish** to import the GPO.

10. After the import operation completes, a summary will state whether the import succeeded. Select **OK**.

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Group Policy Processing](group-policy-processing)
-   [Group Policy Modeling and Group Policy Results](group-policy-modeling-results)
-   [Group Policy Management Console (GPMC)](group-policy-management-console)

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

-   [Group Policy processing for Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing?source=recommendations)

    Learn about how Group Policy processing works in Active Directory Domain Services on Windows Server and Windows client computers.

-   [Group Policy Management Console in Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-management-console?source=recommendations)

    Learn how to create, edit, link, and manage Group Policy Objects using the Group Policy Management Console.

-   [Export a GPO to a File - Microsoft Desktop Optimization Pack](/en-us/microsoft-desktop-optimization-pack/agpm/export-a-gpo-to-a-file?source=recommendations)

    Export a GPO to a File

-   [Group Policy preferences in Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-preferences?source=recommendations)

    Group Policy Preferences allow administrators to configure, deploy, and manage user and computer settings in Active Directory with greater flexibility in Windows.

-   [Group Policy overview for Windows Server](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview?source=recommendations)

    Learn about what Group Policy does and how it works with Active Directory Domain Services in Windows.

-   [Applying Group Policy troubleshooting guidance - Windows Server](/en-us/troubleshoot/windows-server/group-policy/applying-group-policy-troubleshooting-guidance?source=recommendations)

    Provides guidance to troubleshoot Group Policy.

Training

Module

[Implement Group Policy Objects - Training](/en-us/training/modules/implement-group-policy-objects/?source=recommendations)

Implement Group Policy Objects

------------------------------------------------------------------------

-    Last updated on 07/10/2025
