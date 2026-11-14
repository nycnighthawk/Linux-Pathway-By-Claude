---
{"title": "Create a Key Distribution Service (KDS) root key", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/create-the-key-distribution-services-kds-root-key", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Create a Key Distribution Service (KDS) root key

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This article for IT professionals describes how to create a Key Distribution Service (kdssvc.dll) root key on the domain controller by using Windows PowerShell to generate group Managed Service Account passwords in Windows Server 2012 or later.

Domain controllers (DC) require a root key to begin generating gMSA passwords. The domain controllers will wait up to 10 hours from time of creation to allow all domain controllers to converge their Active Directory replication before allowing the creation of a gMSA. Waiting up to 10 hours is a safety measure to prevent password generation from occurring before all DCs in the environment are capable of answering gMSA requests. Trying to use a gMSA too soon might fail when the gMSA host attempts to retrieve the password, because the key might not have been replicated to all domain controllers. gMSA password retrieval failures can also occur when you use DCs with limited replication schedules or if there\'s a replication issue.

Note

Deleting and re-creating the root key can lead to issues where the old key continues to be used after deletion due to caching of the key. The KDC should be restarted on all domain controllers if the root key is re-created.

Membership in the **Domain Admins** or **Enterprise Admins** groups, or the equivalent, is the minimum requirement for completing this procedure. For detailed information about using the appropriate accounts and group memberships, see [Local and Domain Default Groups](/en-us/previous-versions/orphan-topics/ws.10/dd728026(v=ws.10)).

Note

A 64-bit architecture is required to run the Windows PowerShell commands that are used to administer group Managed Service Accounts.

[](#to-create-the-kds-root-key-by-using-the-add-kdsrootkey-cmdlet)

#### To create the KDS root key by using the Add-KdsRootKey cmdlet {#to-create-the-kds-root-key-by-using-the-add-kdsrootkey-cmdlet .heading-anchor}

1.  On the Windows Server 2012 or later domain controller, run Windows PowerShell from the Taskbar.

2.  At the command prompt for the Windows PowerShell Active Directory module, type the following commands, and then select **Enter**:

    **Add-KdsRootKey -EffectiveImmediately**

    Tip

    You can use the Effective time parameter to provide time for keys to be propagated to all DCs before use. Using Add-KdsRootKey -EffectiveImmediately will add a root key to the target DC that will be used by the KDS service immediately. However, other domain controllers won\'t be able to use the root key until replication is successful.

KDS root keys are stored in Active Directory in container `CN=Master Root Keys,CN=Group Key Distribution Service,CN=Services,CN=Configuration,DC=<forest name>;`. They have an attribute msKds-DomainID that links to the computer account of the domain controller that created the object. When this domain controller is demoted and removed from the domain, the value will refer to the tombstone of the computer account. You can ignore the broken value because it\'s only used to help the administrator track the object when it\'s freshly created. You can also change the attribute value to point it to the computer object of another domain controller in your forest.

For test environments that have only one DC, you can create a KDS root key and set the start time in the past to avoid the interval wait for key generation by using the following procedure. Validate that a 4004 event has been logged in the KDS event log.

[](#to-create-the-kds-root-key-in-a-test-environment-for-immediate-effectiveness)

#### To create the KDS root key in a test environment for immediate effectiveness {#to-create-the-kds-root-key-in-a-test-environment-for-immediate-effectiveness .heading-anchor}

1.  On the Windows Server 2012 or later domain controller, run the Windows PowerShell from the Taskbar.

2.  At the command prompt for the Windows PowerShell Active Directory module, type the following commands, and then select **Enter**:

    **\$a=Get-Date**

    **\$b=\$a.AddHours(-10)**

    **Add-KdsRootKey -EffectiveTime \$b**

    Or use a single command:

    **Add-KdsRootKey -EffectiveTime ((get-date).addhours(-10))**

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Manage Group Managed Service Accounts](manage-group-managed-service-accounts)

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

-   [Manage Group Managed Service Accounts](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/manage-group-managed-service-accounts?source=recommendations)

    Learn how to manage and use Group Managed Service Accounts (gMSA) in Windows Server.

-   [Group Managed Service Accounts overview](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview?source=recommendations)

    Learn about the group Managed Service Account; practical applications, changes in Microsoft\'s implementation, both hardware and software requirements.

-   [Troubleshoot gMSAs for Windows containers](/en-us/virtualization/windowscontainers/manage-containers/gmsa-troubleshooting?source=recommendations)

    How to troubleshoot group Managed Service Accounts (gMSAs) for Windows containers.

Training

Module

[Guided project - Administer Active Directory Domain Services - Training](/en-us/training/modules/guided-project-administer-active-directory-domain-services/?source=recommendations)

This guided project helps prepare you to manage Active Directory Domain services, including creating and deploying domains, configuring group policy objects, establishing and enforcing passwords, and maintaining security of Active Directory.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 07/11/2025
