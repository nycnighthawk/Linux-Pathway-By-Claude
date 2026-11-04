---
{"title": "How to configure SPN", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/how-to-configure-spn", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# How to configure SPN

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

The `setspn` command-line tool is used to read, modify, and delete the Service Principal Name (SPN) directory property for an Active Directory (AD) service account. SPNs are essential for locating a target principal name associated with a service. With `setspn`, you can view existing SPNs, reset an account\'s default SPNs, and add or remove additional SPNs as needed.

It\'s unnecessary to manually modify SPNs since they\'re automatically set up when a computer joins a domain or when services are installed. However, SPN information can become outdated in certain cases. For instance, if a computer\'s name changes, the SPNs tied to its services need updating to match the new name. Additionally, some services and applications might require manual updates to a service account\'s SPN settings to ensure proper authentication.

In AD, the `servicePrincipalName` attribute is a multivalued, nonlinked attribute built from the Domain Name System (DNS) host name. SPNs are used for mutual authentication between the client and the server hosting a service. The client locates a computer account using the SPN of the service it\'s trying to connect to.

[](#spn-format)

## SPN format {#spn-format .heading-anchor}

When you modify SPNs using `setspn`, the SPN must be entered in the correct format. The format of an SPN is *serviceclass/host:port/servicename*, in which each item represents a name or value. Unless the service name and port aren\'t standard, you don\'t have to enter them when you use `setspn`. For example, the default SPNs for a server named WSRV2022 that is providing remote desktop (RDP) services over the default port TCP 3389 registers the following two SPNs in its own AD computer object:

``` {.inner-focus data-language=""}
TERMSRV/WSRV2022

TERMSRV/WSRV2022.contoso1.com
```

If you need to specify a nonstandard SPN configuration, see [Name Formats for Unique SPNs](/en-us/windows/win32/ad/name-formats-for-unique-spns).

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

-   The **Active Directory Domain Services** (AD DS) role must be installed on your device. To learn more, see [Install or Uninstall Roles, Role Services, or Features](/en-us/windows-server/administration/server-manager/install-or-uninstall-roles-role-services-or-features).

-   The devices in your environment must be domain-joined.

-   You must be a member of the **Domain Admins** or **Enterprise Admins** group.

    -   If you aren\'t a member of either the Domain Admins or Enterprise Admins groups, you must have *read* and *write* permissions on the `servicePrincipalName` attribute of the object in AD.

[](#manage-spns)

## Manage SPNs {#manage-spns .heading-anchor}

Configuring SPNs in your environment can be performed using an elevated command prompt or elevated PowerShell window. See the following steps in configuring SPNs for your environment.

[](#command-prompt-method)

### Command prompt method {#command-prompt-method .heading-anchor}

-   [Add SPNs](#tabpanel_1_add)
-   [View SPNs](#tabpanel_1_view)
-   [Reset SPNs](#tabpanel_1_reset)
-   [Remove SPNs](#tabpanel_1_remove)

To add an SPN, run the following command. Replace *service/name* with the SPN you want to add and *hostname* with the host name of the computer object you want to update:

``` {.inner-focus data-language=""}
setspn -S <service/name> <hostname>
```

For example, if there\'s an AD DC with the host name server1.contoso.com that requires an SPN for the Lightweight Directory Access Protocol (LDAP), type:

``` {.inner-focus data-language=""}
setspn -S ldap/server1.contoso.com server1
```

[](#powershell-method)

### PowerShell method {#powershell-method .heading-anchor}

In PowerShell, the `Set-ADUser` cmdlet is used for user accounts and `Set-ADComputer` for the computer name.

-   [Add SPNs](#tabpanel_2_add)
-   [View SPNs](#tabpanel_2_view)
-   [Reset SPNs](#tabpanel_2_reset)
-   [Remove SPNs](#tabpanel_2_remove)

To add an SPN, run the following command. Replace `UserName`, `ComputerName`, and `$spn = " "` with the appropriate values for the user account or computer name:

PowerShell

``` {.inner-focus data-language="powershell"}
$userID = "UserName"
$spn = "HTTP/webserver.domain.com"

Set-ADUser -Identity $userID -Add @{ServicePrincipalName=$spn}
```

PowerShell

``` {.inner-focus data-language="powershell"}
$computerID = "ComputerName"
$spn = "HTTP/computerserver.domain.com"

Set-ADComputer -Identity $computerID -Add @{ServicePrincipalName=$spn}
```

[](#grant-spn-permissions-to-non-admins)

## Grant SPN permissions to non admins {#grant-spn-permissions-to-non-admins .heading-anchor}

For users who aren\'t part of the Domain Admins or Enterprise Admins group, they need the proper permissions to modify the SPNs. Granting these permissions can be performed through Active Directory Users and Computers (ADUC) or PowerShell. See the following steps.

-   [ADUC](#tabpanel_3_aduc)
-   [PowerShell](#tabpanel_3_powershell)

1.  In **Server Manager**, select **Tools**, then select **Active Directory Users and Computers**.

2.  Select the **View** tab, then select **Advanced Features**.

3.  In the left pane, right-click on the domain where you want to allow a disjoint namespace, then select **Properties**.

4.  Select the **Security** tab, select **Advanced**.

5.  Under the **Permissions** tab, select **Add**.

6.  Select **Select a principal**, under **Enter the object names to select**, type the group or user account name to which you want to delegate permission, then select **OK**.

    To view all available groups and user accounts in your domain, select **Advanced**, then select **Find Now**.

7.  Under **Applies to**, select **Descendant Computer objects**.

8.  Under **Permissions**, select **Validated write to service principal name** checkbox, then select **OK** on the three open dialog boxes to apply your changes.

[](#see-also)

## See also {#see-also .heading-anchor}

-   [Service principal names](/en-us/windows/win32/ad/service-principal-names)

-   [Service Logons Fail Due to Incorrectly Set SPNs](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc772897(v=ws.10))

-   [SetSPN command reference](/en-us/windows-server/administration/windows-commands/setspn)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Setspn](/en-us/windows-server/administration/windows-commands/setspn?source=recommendations)

    The setspn command reads, modifies, and deletes the Service Principal Names (SPN) directory property for an Active Directory service account.

-   [Service principal names - Win32 apps](/en-us/windows/win32/ad/service-principal-names?source=recommendations)

    A service principal name (SPN) is a unique identifier of a service instance.

-   [Service Principal Name &lt;spn&gt;](/en-us/iis/configuration/system.webserver/security/authentication/windowsauthentication/extendedprotection/spn?source=recommendations)

    Overview The \<spn\> element adds a Service Principal Name (SPN) to the collection of SPNs. Each SPN specifies a unique endpoint for client activity usin\...

-   [Can\'t access SMB file server through DNS CNAME - Windows Server](/en-us/troubleshoot/windows-server/networking/dns-cname-alias-cannot-access-smb-file-server-share?source=recommendations)

    Describes an issue in which you can\'t access SMB file server share by using the DNS CNAME. Provides a resolution.

-   [SPN and UPN uniqueness](/en-us/windows-server/identity/ad-ds/manage/component-updates/spn-and-upn-uniqueness?source=recommendations)

    Learn more about: SPN and UPN uniqueness

-   [Enable Kerberos event logging - Windows Server](/en-us/troubleshoot/windows-server/active-directory/enable-kerberos-event-logging?source=recommendations)

    Discusses how to turn on detailed Kerberos logging on a particular computer, and how to use that information for troubleshooting.

-   [Kerberos Authentication Troubleshooting Guidance - Windows Server](/en-us/troubleshoot/windows-server/windows-security/kerberos-authentication-troubleshooting-guidance?source=recommendations)

    Provides guidance to troubleshoot Kerberos authentication issues.

Training

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 03/24/2025
