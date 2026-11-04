---
{"title": "Active Directory Forest Recovery - Seize an operations master role", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-seizing-operations-master-role", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Seize an operations master role

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Use the following procedure to seize an operations master role (also known as a flexible single master operations (FSMO) role). You can use Ntdsutil.exe, a command-line tool that is installed automatically on all DCs.

[](#seize-an-operations-master-role)

## Seize an operations master role {#seize-an-operations-master-role .heading-anchor}

1.  At the command prompt, type the following command, and then press ENTER:

    cli

    ``` {.inner-focus data-language="cli"}
    ntdsutil
    ```

2.  At the **ntdsutil:** prompt, type the following command, and then press ENTER:

    cli

    ``` {.inner-focus data-language="cli"}
    roles
    ```

3.  At the **FSMO maintenance:** prompt, type the following command, and then press ENTER:

    cli

    ``` {.inner-focus data-language="cli"}
    connections
    ```

4.  At the **server connections:** prompt, type the following command, and then press ENTER:

    cli

    ``` {.inner-focus data-language="cli"}
    Connect to server ServerFQDN
    ```

    Where *ServerFQDN* is the fully qualified domain name (FQDN) of this DC, for example: **connect to server nycdc01.example.com**.

    If *ServerFQDN* does not succeed, use the NetBIOS name of the DC.

5.  At the **server connections:** prompt, type the following command, and then press ENTER:

    cli

    ``` {.inner-focus data-language="cli"}
    quit
    ```

6.  Depending on the role that you want to seize, at the **FSMO maintenance:** prompt, type the appropriate command as described in the following table, and then press ENTER.

  Role                                                                                                                                                                                                                                          Credentials         Command
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------- ---------------------------------
  Domain naming master                                                                                                                                                                                                                          Enterprise Admins   **Seize naming master**
  Schema master                                                                                                                                                                                                                                 Schema Admins       **Seize schema master**
  Infrastructure master **Note:** After you seize the infrastructure master role, you may receive an error later if you need to run Adprep /Rodcprep. For more information, see KB article [949257](https://support.microsoft.com/kb/949257).   Domain Admins       **Seize infrastructure master**
  PDC emulator master                                                                                                                                                                                                                           Domain Admins       **Seize pdc**
  RID master                                                                                                                                                                                                                                    Domain Admins       **Seize rid master**

After you confirm the request, Active Directory or AD DS attempts to transfer the role. When the transfer fails, some error information appears, and Active Directory or AD DS proceeds with the seizure. After the seizure is complete, a list of the roles and the Lightweight Directory Access Protocol (LDAP) name of the server that currently holds each role appears. You can also run **Netdom Query FSMO** at an elevated command prompt to verify current role holders.

Note

If this computer was not a RID master before the failure and you attempt to seize the RID master role, the computer tries to synchronize with a replication partner before accepting this role. However, because this step is performed when the computer is isolated, it will not succeed in synchronizing with a partner. Therefore, a dialog box appears asking you whether you want to continue with the operation despite this computer not being able to synchronize with a partner. Click **Yes**.

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

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3 hidden=""}

------------------------------------------------------------------------

-    Last updated on 05/12/2025
