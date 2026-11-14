---
{"title": "CA Backup and Restore Windows PowerShell cmdlets", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/ca-backup-and-restore-windows-powershell-cmdlets", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# CA Backup and Restore Windows PowerShell cmdlets

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

> **Author**: Justin Turner, Senior Support Escalation Engineer with the Windows group

Note

This content is written by a Microsoft customer support engineer, and is intended for experienced administrators and systems architects who are looking for deeper technical explanations of features and solutions in Windows Server 2012 R2 than topics on TechNet usually provide. However, it has not undergone the same editing passes, so some of the language may seem less polished than what is typically found on TechNet.

[](#overview)

## Overview {#overview .heading-anchor}

The ADCSAdministration Windows PowerShell module was introduced in Window Server 2012. Two new cmdlets were added to this module in Window Server 2012 R2 to support the Backup and Restore of a CA.

-   Backup-CARoleService

-   Restore-CARoleService

[](#backup-caroleservice)

## Backup-CARoleService {#backup-caroleservice .heading-anchor}

**ADCSAdministration Cmdlet: Backup-CARoleService**

+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Arguments - **Bold** arguments are required | Description                                                                                                                                        |
+=============================================+====================================================================================================================================================+
| **-Path**                                   | \- String - location to save the backup\                                                                                                           |
|                                             | - This is the only unnamed parameter\                                                                                                              |
|                                             | - positional parameter                                                                                                                             |
|                                             |                                                                                                                                                    |
|                                             | **Example:**                                                                                                                                       |
|                                             |                                                                                                                                                    |
|                                             | Backup-CARoleService.-Path c:\\adcsbackup1                                                                                                         |
|                                             |                                                                                                                                                    |
|                                             | Backup-CARoleService c:\\adcsbackup2                                                                                                               |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| -KeyOnly                                    | \- Backup the CA certificate without the database                                                                                                  |
|                                             |                                                                                                                                                    |
|                                             | **Example:**                                                                                                                                       |
|                                             |                                                                                                                                                    |
|                                             | Backup-CARoleService c:\\adcsbackup3 -KeyOnly                                                                                                      |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| -Password                                   | \- Specifies the password to protect CA certificates and private keys\                                                                             |
|                                             | - Must be a secure string\                                                                                                                         |
|                                             | - Not valid with the -DatabaseOnly parameter                                                                                                       |
|                                             |                                                                                                                                                    |
|                                             | Example:                                                                                                                                           |
|                                             |                                                                                                                                                    |
|                                             | Backup-CARoleService c:\\adcsbackup4 -Password (Read-Host -prompt \"Password:\" -AsSecureString)                                                   |
|                                             |                                                                                                                                                    |
|                                             | Backup-CARoleService c:\\adcsbackup5 -Password (ConvertTo-SecureString \"Pa55w0rd!\" -AsPlainText -Force)                                          |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| -DatabaseOnly                               | \- Backup the database without the CA certificate                                                                                                  |
|                                             |                                                                                                                                                    |
|                                             | Backup-CARoleService c:\\adcsbackup6 -DatabaseOnly                                                                                                 |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| -Force                                      | 1\. Allows you to overwrite the backup that pre-exists in the location specified in the -Path parameter                                            |
|                                             |                                                                                                                                                    |
|                                             | Backup-CARoleService c:\\adcsbackup1 -Force                                                                                                        |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| -Incremental                                | \- Perform an incremental backup                                                                                                                   |
|                                             |                                                                                                                                                    |
|                                             | Backup-CARoleService c:\\adcsbackup7 -Incremental                                                                                                  |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| -KeepLog                                    | 1\. Instructs the command to keep log files. If the switch isn\'t specified, log files are truncated by default except in the Incremental scenario |
|                                             |                                                                                                                                                    |
|                                             | Backup-CARoleService c:\\adcsbackup7 -KeepLog                                                                                                      |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

[](#-password-secure-string)

### -Password \<Secure String\> {#-password-secure-string .heading-anchor}

If the -Password parameter is used, the supplied password must be a secure string. Use the **Read-Host** cmdlet to launch an interactive prompt for secure password entry, or use the **ConvertTo-SecureString** cmdlet to specify the password in-line.

Review the following examples

**Specifying a secure string for the Password parameter using Read-Host**

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Backup-CARoleService c:\adcsbackup4 -Password (Read-Host -prompt "Password:" -AsSecureString)
```

**Specifying a secure string for the Password parameter using ConvertTo-SecureString**

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Backup-CARoleService c:\adcsbackup5 -Password (ConvertTo-SecureString "Pa55w0rd!" -AsPlainText -Force)
```

[](#restore-caroleservice)

## Restore-CARoleService {#restore-caroleservice .heading-anchor}

**ADCSAdministration Cmdlet: Restore-CARoleService**

+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Arguments - **Bold** arguments are required | Description                                                                                                       |
+=============================================+===================================================================================================================+
| **-Path**                                   | \- String - location to restore backup from\                                                                      |
|                                             | - This is the only unnamed parameter\                                                                             |
|                                             | - positional parameter                                                                                            |
|                                             |                                                                                                                   |
|                                             | **Example:**                                                                                                      |
|                                             |                                                                                                                   |
|                                             | Restore-CARoleService.-Path c:\\adcsbackup1 -Force                                                                |
|                                             |                                                                                                                   |
|                                             | Restore-CARoleService c:\\adcsbackup2 -Force                                                                      |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| -KeyOnly                                    | \- Restore the CA certificate without the database\                                                               |
|                                             | - Must be specified if the backup was taken with the -KeyOnly option                                              |
|                                             |                                                                                                                   |
|                                             | **Example:**                                                                                                      |
|                                             |                                                                                                                   |
|                                             | Restore-CARoleService c:\\adcsbackup3 -KeyOnly -Force                                                             |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| -Password                                   | \- Specifies the password of the CA certificates and private keys\                                                |
|                                             | - Must be a secure string                                                                                         |
|                                             |                                                                                                                   |
|                                             | **Example:**                                                                                                      |
|                                             |                                                                                                                   |
|                                             | Restore-CARoleService c:\\adcsbackup4 -Password (read-host -prompt \"Password:\" -AsSecureString) -Force          |
|                                             |                                                                                                                   |
|                                             | Restore-CARoleService c:\\adcsbackup5 -Password (ConvertTo-SecureString \"Pa55w0rd!\" -AsPlainText -Force) -Force |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| -DatabaseOnly                               | \- Restore the database without the CA certificate                                                                |
|                                             |                                                                                                                   |
|                                             | Restore-CARoleService c:\\adcsbackup6 -DatabaseOnly                                                               |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| -Force                                      | \- Allows you to overwrite the preexisting keys\                                                                  |
|                                             | - Is an optional parameter but when restoring in-place, it is likely required                                     |
|                                             |                                                                                                                   |
|                                             | Restore-CARoleService c:\\adcsbackup1 -Force                                                                      |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

[](#issues)

### Issues {#issues .heading-anchor}

A nonpassword protected backup is taken if the ConvertTo-SecureString function fails while using the Backup-CARoleService with the -Password parameter.

[](#common-errors)

### Common errors {#common-errors .heading-anchor}

+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Action                                                                                                             | Error                                                                                                                            | Comment                                                                                                                                     |
+====================================================================================================================+==================================================================================================================================+=============================================================================================================================================+
| **Restore-CARoleService C:\\ADCSBackup**                                                                           | Restore-CARoleService : The process can\'t access the file because it\'s being used by another process. (Exception from HRESULT: | Stop the Active Directory Certificate Services service prior to running the Restore-CARoleService cmdlet                                    |
|                                                                                                                    |                                                                                                                                  |                                                                                                                                             |
|                                                                                                                    | 0x80070020)                                                                                                                      |                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| **Restore-CARoleService C:\\ADCSBackup**                                                                           | Restore-CARoleService : The directory isn\'t empty. (Exception from HRESULT: 0x80070091)                                         | Use the -Force parameter to overwrite preexisting keys                                                                                      |
+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| **Backup-CARoleService C:\\ADCSBackup -Password (Read-Host -Prompt \"Password:\" -AsSecureString) -DatabaseOnly**  | Backup-CARoleService : Parameter set can\'t be resolved using the specified named parameters.                                    | The -Password parameter is only used to password protect private keys and is therefore invalid when you aren\'t backing them up             |
+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| **Restore-CARoleService C:\\ADCSBack15 -Password (Read-Host -Prompt \"Password:\" -AsSecureString) -DatabaseOnly** | Restore-CARoleService : Parameter set can\'t be resolved using the specified named parameters.                                   | The -Password parameter is only used to password protect private keys and is therefore invalid when you aren\'t restoring them              |
+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| **Restore-CARoleService C:\\ADCSBack14 -Password (Read-Host -Prompt \"Password:\" -AsSecureString)**               | Restore-CARoleService : The system can\'t find the file specified. (Exception from HRESULT: 0x80070002)                          | The path specified doesn\'t contain a valid database backup. Perhaps the path is invalid or the backup was taken with the -KeysOnly option? |
+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

[](#additional-resources)

## Additional Resources {#additional-resources .heading-anchor}

[Active Directory Certificate Services Migration Guide](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee126170(v=ws.10))

[Backing up a CA database and private key](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee126140(v=ws.10)#BKMK_BackUpDB)

[Restoring the CA database and configuration on the destination server](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee126140(v=ws.10)#BKMK_RestoreCA)

[](#try-this-backup-the-ca-in-your-lab-using-windows-powershell)

## Try This: Backup the CA in your lab using Windows PowerShell {#try-this-backup-the-ca-in-your-lab-using-windows-powershell .heading-anchor}

1.  Use the commands in this lesson to backup the CA database and private key secured with a password.

2.  Hold off on the restore of the CA at this time.

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

-   [How to move a certification authority to another server - Windows Server](/en-us/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/move-certification-authority-to-another-server?source=recommendations)

    Describes how to move a certification authority (CA) to a different server in Windows Server 2003 and in Windows 2000 Server.

-   [Migrate a Certification Authority in Windows Server](/en-us/windows-server/identity/ad-cs/migrate-certification-authority?source=recommendations)

    Learn how to migrate your Certification Authority with step-by-step instructions and best practices.

-   [Superseded Certificate Templates and impact on user\'s AD store - Windows Server](/en-us/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/superseded-certificate-templates-impact-user-ad-store?source=recommendations)

    Provides a resolution for the issue superseded Certificate Templates and impact on user\'s AD store

Training

Module

[Implement and manage Active Directory Certificate Services - Training](/en-us/training/modules/implement-manage-active-directory-certificate-services/?source=recommendations)

Implement and manage Active Directory Certificate Services

------------------------------------------------------------------------

-    Last updated on 05/17/2023
