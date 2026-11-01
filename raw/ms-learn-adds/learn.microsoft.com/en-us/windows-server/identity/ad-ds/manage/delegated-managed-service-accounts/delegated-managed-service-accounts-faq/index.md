---
{"title": "Delegated Managed Service Accounts FAQ", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/delegated-managed-service-accounts-faq", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Delegated Managed Service Accounts FAQ

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This article contains answers to frequently asked questions (FAQs) about using Delegated Managed Service Accounts (dMSA) in Windows Server 2025.

[](#general)

## General {#general .title .is-2 .margin-top-sm .margin-bottom-xs .heading-anchor}

[](#can-i-just-extend-the-schema-to-windows-server-2025-and-then-use-a-windows-server-2025-member-server-to-start-using-dmsa-without-having-a-windows-server-2025-domain-controller--dc-)

### Can I just extend the schema to Windows Server 2025 and then use a Windows Server 2025 member server to start using dMSA without having a Windows Server 2025 Domain Controller (DC)? {#can-i-just-extend-the-schema-to-windows-server-2025-and-then-use-a-windows-server-2025-member-server-to-start-using-dmsa-without-having-a-windows-server-2025-domain-controller--dc- .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

No, you must have at least one Windows Server 2025 DC, which must be discoverable by the client or member server.

[](#my-application-server-running-a-service-account-is-behind-a-read-only-dc--rodc--with-no-connectivity-to-a-read-write-dc--is-this-a-supported-configuration-for-dmsa-)

### My application server running a service account is behind a Read-Only DC (RODC) with no connectivity to a Read/Write DC. Is this a supported configuration for dMSA? {#my-application-server-running-a-service-account-is-behind-a-read-only-dc--rodc--with-no-connectivity-to-a-read-write-dc--is-this-a-supported-configuration-for-dmsa- .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

Yes, this configuration is supported provided the following prerequisites are met:

1.  The dMSA account must be cached on the RODC.

2.  The dMSA account must be manually added to the **PrincipalsAllowedToRetrieveManagedPassword** attribute of the machine by running the following command:

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Set-ADServiceAccount -Identity dMSAFinApp -PrincipalsAllowedToRetrieveManagedPassword Client$
    ```

[](#can-i-force-a-password-reset-for-a-dmsa-account)

### Can I force a password reset for a dMSA account? {#can-i-force-a-password-reset-for-a-dmsa-account .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

No, you can\'t force a password reset for a dMSA account.

[](#migration)

## Migration {#migration .title .is-2 .margin-top-sm .margin-bottom-xs .heading-anchor}

[](#can-i-migrate-a-gmsa-to-a-dmsa-account)

### Can I migrate a gMSA to a dMSA account? {#can-i-migrate-a-gmsa-to-a-dmsa-account .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

No, this scenario isn\'t supported. To learn more, see [Delegated Managed Service Accounts overview](/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/delegated-managed-service-accounts-overview).

[](#i-have-three-service-accounts-in-my-environment-running-different-application-workloads--can-i-migrate-all-three-service-accounts-to-a-single-dmsa)

### I have three service accounts in my environment running different application workloads. Can I migrate all three service accounts to a single dMSA? {#i-have-three-service-accounts-in-my-environment-running-different-application-workloads--can-i-migrate-all-three-service-accounts-to-a-single-dmsa .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

No, each service account must have its own dMSA. You can\'t migrate multiple service accounts to a single dMSA.

[](#instead-of-migrating-the-service-account--can-i-reconfigure-all-of-my-services-to-a-new-dmsa--if-i-have-a-sql-server-farm-currently-using-a-service-account--and-want-to-avoid-the-hassle-of-migration--can-i-replace-my-service-account-with-a-dmsa-)

### Instead of migrating the service account, can I reconfigure all of my services to a new dMSA? If I have a SQL Server farm currently using a service account, and want to avoid the hassle of migration, can I replace my service account with a dMSA? {#instead-of-migrating-the-service-account--can-i-reconfigure-all-of-my-services-to-a-new-dmsa--if-i-have-a-sql-server-farm-currently-using-a-service-account--and-want-to-avoid-the-hassle-of-migration--can-i-replace-my-service-account-with-a-dmsa- .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

Yes, you can replace the service account with a dMSA. This process would require:

1.  Creating a new dMSA account.
2.  Reconfiguring the service to use the new dMSA account.
3.  Retiring the old service account.

[](#will-my-service-start-using-the-dmsa-during-the-migration-process-or-only-after-the-migration-is-complete)

### Will my service start using the dMSA during the migration process or only after the migration is complete? {#will-my-service-start-using-the-dmsa-during-the-migration-process-or-only-after-the-migration-is-complete .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

The service will start using the newly created and configured dMSA only after the migration process is complete.

[](#can-i-delete-the-service-account-after-migration--what-should-i-do-with-the-service-account-post-migration-)

### Can I delete the service account after migration? What should I do with the service account post-migration? {#can-i-delete-the-service-account-after-migration--what-should-i-do-with-the-service-account-post-migration- .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

The service account is disabled, and its information, including permissions, SPNs, and delegation, will be moved to the dMSA account. However, you should keep the service account intact because:

1.  The service is still configured with the service account and won\'t automatically change to the dMSA account. Deleting the service account stops the service.
2.  The service account has forward and backward links to the dMSA account.

[](#i-have-three-windows-server-2022-operating-systems-and-one-windows-server-2025-operating-system-running-my-sql-application--can-i-migrate-to-dmsa-in-a-windows-server-2025-domain-environment-)

### I have three Windows Server 2022 operating systems and one Windows Server 2025 operating system running my SQL application. Can I migrate to dMSA in a Windows Server 2025 domain environment? {#i-have-three-windows-server-2022-operating-systems-and-one-windows-server-2025-operating-system-running-my-sql-application--can-i-migrate-to-dmsa-in-a-windows-server-2025-domain-environment- .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

No, all your clients and/or servers must be running on dMSA-supported operating system to perform the migration.

[](#can-i-reset-the-password-of-my-service-account-after-i-have-started-the-migration-process-but-before-it-s-complete)

### Can I reset the password of my service account after I have started the migration process but before it\'s complete? {#can-i-reset-the-password-of-my-service-account-after-i-have-started-the-migration-process-but-before-it-s-complete .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

No, it isn\'t recommended to reset the password during the migration process.

[](#what-if-i-mistakenly-migrated-a-service-account-that-shouldn-t-have-been-migrated--can-i-undo-or-unlink-the-migration)

### What if I mistakenly migrated a service account that shouldn\'t have been migrated? Can I undo or unlink the migration? {#what-if-i-mistakenly-migrated-a-service-account-that-shouldn-t-have-been-migrated--can-i-undo-or-unlink-the-migration .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

Yes, you can undo a migration or unlink a service account and start from scratch. Use the `Undo-ADServiceAccountMigration` or `Reset-ADServiceAccountMigration` cmdlets.

[](#i-have-migrated-a-service-account--and-it-s-now-automatically-disabled--can-i-move-the-service-account-to-a-different-organizational-unit--ou-)

### I have migrated a service account, and it\'s now automatically disabled. Can I move the service account to a different Organizational Unit (OU)? {#i-have-migrated-a-service-account--and-it-s-now-automatically-disabled--can-i-move-the-service-account-to-a-different-organizational-unit--ou- .title .is-3 .margin-top-sm .margin-bottom-xs .heading-anchor}

Yes, you can move the disabled service account to another OU.

[](#see-also)

## See also {#see-also .heading-anchor}

-   [Setting up Delegated Managed Service Accounts](delegated-managed-service-accounts-set-up-dmsa)

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

-    Last updated on 09/15/2025
