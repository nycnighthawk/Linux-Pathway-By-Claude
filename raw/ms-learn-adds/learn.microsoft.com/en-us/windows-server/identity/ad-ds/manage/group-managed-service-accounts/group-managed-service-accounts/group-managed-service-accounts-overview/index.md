---
{"title": "Group Managed Service Accounts overview", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Group Managed Service Accounts overview

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This article for IT professionals introduces the group Managed Service Account (gMSA) by describing practical applications, changes in Microsoft\'s implementation, and hardware and software requirements.

[](#feature-description)

## Feature description {#feature-description .heading-anchor}

A standalone Managed Service Account (sMSA) is a managed domain account that provides automatic password management, simplified service principal name (SPN) management, and the ability to delegate the management to other administrators. Domain administrators can delegate service management to service administrators, who can manage the entire lifecycle of a Managed Service Account or the group Managed Service Account. Existing client computers are able to authenticate to any such service without knowing which service instance they\'re authenticating to. This type of managed service account (MSA) was introduced in Windows Server 2008 R2 and Windows 7.

The group Managed Service Account (gMSA) provides the same functionality within the domain and also extends that functionality over multiple servers. This minimizes the administrative overhead of a service account by allowing Windows to handle password management for these accounts. When you connect to a service hosted on a server farm, such as a Network Load Balanced solution, the authentication protocols supporting mutual authentication require all instances of the services to use the same principal. When you use a gMSA as a service principal, the Windows operating system manages the password for the account instead of relying on the administrator to manage the password.

The Microsoft Key Distribution Service (`kdssvc.dll`) lets you securely obtain the latest key or a specific key with a key identifier for an Active Directory account. The Key Distribution Service shares a secret that\'s used to create keys for the account. These keys periodically change. For a gMSA, the domain controller computes the password on the key that the Key Distribution Services provides, along with other attributes of the gMSA. Member hosts can obtain the current and preceding password values by contacting a domain controller.

[](#practical-applications)

## Practical applications {#practical-applications .heading-anchor}

gMSAs provide a single identity solution for services running on a server farm or on systems behind Network Load Balancer. By providing a gMSA solution, you can configure services for the new gMSA principal while Windows handles the password management.

When services or service administrators use a gMSA, they don\'t need to manage password synchronization between service instances. The gMSA supports hosts kept offline for an extended time period and manages member hosts for all instances of a service. You can deploy a server farm that supports a single identity that existing client computers can authenticate without having to know which service instance they\'re connecting to.

Although failover clusters don\'t provide support for gMSAs, services that operate on the Cluster service can utilize a gMSA or sMSA if they\'re a Windows service, an app pool, a scheduled task, or natively support gMSA or sMSA.

[](#software-requirements)

## Software requirements {#software-requirements .heading-anchor}

In order to run the Windows PowerShell commands you need to administer gMSAs, you must have a 64-bit architecture.

A managed service account depends upon Kerberos supported encryption types. When a client computer authenticates to a server using Kerberos, the DC creates a Kerberos service ticket protected with encryption that both the DC and server support. The DC uses the account\'s **msDS-SupportedEncryptionTypes** attribute to determine what encryption the server supports. If there isn\'t an attribute, the DC treats the client computer like it doesn\'t support stronger encryption types. If you\'ve configured the host to not support RC4, then authentication always fails. For this reason, you should always configure AES for MSAs.

Note

As of Windows Server 2008 R2, DES is disabled by default. For more information about supported encryption types, see [Changes in Kerberos Authentication](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd560670(v=ws.10)).

Note

gMSAs aren\'t applicable to Windows operating systems earlier than Windows Server 2012. For Windows Server 2012, the Windows PowerShell cmdlets default to managing the gMSAs instead of the server Managed Service Accounts.

[](#server-manager-information)

## Server Manager information {#server-manager-information .heading-anchor}

You don\'t need to do any extra configuration to implement MSA and gMSA using Server Manager or the `Install-WindowsFeature` cmdlet.

[](#next-steps)

## Next steps {#next-steps .heading-anchor}

Here are some other resources you can read to learn more about Managed Service Accounts:

-   [Managed Service Accounts Documentation for Windows 7 and Windows Server 2008 R2](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff641731(v=ws.10))
-   [Service Accounts Step-by-Step Guide](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd548356(v=ws.10))
-   [Manage Group Managed Service Accounts](manage-group-managed-service-accounts)
-   [Managed Service Accounts in Active Directory Domain Services](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd378925(v=ws.10))
-   [Managed Service Accounts: Understanding, Implementing, Best Practices, and Troubleshooting](/en-us/archive/blogs/askds/managed-service-accounts-understanding-implementing-best-practices-and-troubleshooting)
-   [Active Directory Domain Services Overview](active-directory-domain-services-overview)

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

-   [Create a Key Distribution Service (KDS) Root Key](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/create-the-key-distribution-services-kds-root-key?source=recommendations)

    Learn how to create a Key Distribution Service root key on a domain controller by using Windows PowerShell to generate group Managed Service Account passwords in Windows Server 2012 or later.

-   [Troubleshoot gMSAs for Windows containers](/en-us/virtualization/windowscontainers/manage-containers/gmsa-troubleshooting?source=recommendations)

    How to troubleshoot group Managed Service Accounts (gMSAs) for Windows containers.

-   [Service Accounts in Windows Server](/en-us/windows-server/identity/ad-ds/manage/understand-service-accounts?source=recommendations)

    Learn how service accounts work in Windows Server, including sMSA, gMSA, dMSA, and virtual accounts, and the password policy and minimum length for each type.

Training

Module

[Manage Windows Server settings using PowerShell cmdlets - Training](/en-us/training/modules/manage-windows-server-settings-use-powershell-cmdlets/?source=recommendations)

This module covers cmdlets that are used to configure settings related to Group Policy, Server Manager, Hyper-V, and Internet Information Services (IIS).

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 07/01/2025
