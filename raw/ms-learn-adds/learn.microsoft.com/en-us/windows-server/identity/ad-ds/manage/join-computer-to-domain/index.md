---
{"title": "Join a computer to a domain", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/join-computer-to-domain", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Join a computer to a domain

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Joining a server or client device to a domain is an essential step for achieving centralized management and improved security within an organization\'s network. Whether you\'re configuring a new device or optimizing your network setup, follow this guide for a seamless integration into your domain environment.

Important

**KB5020276** is a Microsoft update that strengthens the security of the domain join process. This update introduces enhanced validation and authentication to help prevent unauthorized devices from joining a Windows domain, ensuring that only trusted devices can be added to your network. To learn more, see [KB5020276 - Netjoin: Domain join hardening changes](https://support.microsoft.com/topic/kb5020276-netjoin-domain-join-hardening-changes-2b65a0f3-1f4c-42ef-ac0f-1caaf421baf8).

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

**Server requirements**

Your Windows Server device must have the **Active Directory Domain Services** role installed to use the Active Directory Users and Computers (ADUC) tool. To learn more, see [Install or Uninstall Roles, Role Services, or Features](/en-us/windows-server/administration/server-manager/install-or-uninstall-roles-role-services-or-features).

You must be a member of the Administrators group or have administrative privileges on both the local account and domain account.

**Client requirements**

The user account must have administrative privileges on the local machine to join a domain.

Your client device must have one of the following versions of Windows installed:

-   Enterprise
-   Enterprise N
-   Pro
-   Pro N
-   Pro Education
-   Pro Education N
-   Pro for Workstations
-   Pro N for Workstations

Note

To keep time synchronized, organizations often use the Windows Time Service or a Network Time Protocol (NTP) server. Within a domain, computers typically sync their clocks with the Domain Controller, which should be aligned with a dependable time source. This process ensures consistent time settings across all devices in the domain, minimizing potential issues with Kerberos authentication.

[](#prestage-a-device-using-aduc)

## Prestage a device using ADUC {#prestage-a-device-using-aduc .heading-anchor}

This step is optional and not mandatory for joining a device to a domain. However, prestaging a device in Active Directory can streamline the process by pre-assigning the computer account to the appropriate organizational unit (OU) and ensuring proper permissions are in place before the device joins the domain.

1.  In **Server Manager**, select the **Tools** button from the top right menu.

2.  In the drop-down menu, select **Active Directory Users and Computers**.

3.  In the left pane, navigate to and select the appropriate organizational unit (OU).

4.  Select the **Actions** tab, select **New**, then select **Computer**.

5.  Enter the computer name and configure which user or group the device should belong to.

6.  Select **OK** This can help prepare for when the client is ready to join the domain.

[](#join-a-device-to-a-domain)

## Join a device to a domain {#join-a-device-to-a-domain .heading-anchor}

Joining a device to a domain can be done using either graphical user interface (GUI) methods or command-line tools, depending on your preference and the needs of your environment. Both approaches ensure integration into the domain.

[](#server-manager-method)

### Server Manager method {#server-manager-method .heading-anchor}

1.  In **Server Manager**, select **Local Server**, under **Workgroup**, select the workgroup or domain name hyperlink.

2.  Under the **Computer Name** tab, select **Change**.

3.  Under **Member of**, select **Domain**, type the name of the domain that you wish the computer to join, and then select **OK**.

4.  Provide the credentials needed to join the domain, then select **OK**.

5.  After the device successfully joins the domain, a notification confirms the device\'s domain membership. Select **OK**, and you\'re prompted to restart your device.

[](#control-panel-method)

### Control Panel method {#control-panel-method .heading-anchor}

1.  Select **Start**, type **Control Panel**, and then press **ENTER**.

2.  Ensure that from the **View by** drop-down menu at the top right is set to **Category**.

3.  Navigate to **System and Security**, then select **System**.

4.  Select **Domain or workgroup**, under the **Computer Name** tab, select **Change**.

5.  Under **Member of**, select **Domain**, type the name of the domain that you wish the computer to join, and then select **OK**.

6.  Provide the credentials needed to join the domain, then select **OK**.

7.  After the device successfully joins the domain, a notification confirms the device\'s domain membership. Select **OK**, and you\'re prompted to restart your device.

1.  Select **Start**, type **Control Panel**, and then press **ENTER**.

2.  Ensure that from the **View by** drop-down menu at the top right is set to **Category**.

3.  Navigate to **System and Security**, then select **System**.

4.  Select **Advanced system settings**, then select **Change settings**.

5.  Under the **Computer Name** tab, select **Change**. \'

6.  Under **Member of**, select **Domain**, type the name of the domain that you wish the computer to join, and then select **OK**.

7.  Provide the credentials needed to join the domain, then select **OK**.

8.  After the device successfully joins the domain, a notification confirms the device\'s domain membership. Select **OK**, and you\'re prompted to restart your device.

1.  Select **Start**, type **Control Panel**, and then press **ENTER**.

2.  Ensure that from the **View by** drop-down menu at the top right is set to **Category**.

3.  Navigate to **System and Security**, then select **System**.

4.  Under **Computer name, domain, and workgroup settings**, select **Change settings**.

5.  Under the **Computer Name** tab, select **Change**. \'

6.  Under **Member of**, select **Domain**, type the name of the domain that you wish the computer to join, and then select **OK**.

7.  Provide the credentials needed to join the domain, then select **OK**.

8.  After the device successfully joins the domain, a notification confirms the device\'s domain membership. Select **OK**, and you\'re prompted to restart your device.

[](#settings-app-method)

### Settings app method {#settings-app-method .heading-anchor data-id="settings-app-method"}

1.  Select **Start**, select **Settings**, then select **Accounts**.

2.  Select **Access work or school**, then select **Connect**.

3.  Select **Join this device to a local Active Directory domain**.

4.  Enter the domain name, select **Next**, and the account credentials, then select **OK**.

5.  Restart the device.

[](#command-line-method)

### Command line method {#command-line-method .heading-anchor}

Adding a device to a domain can be performed through the command prompt or PowerShell.

-   [Command Prompt](#tabpanel_1_cmd)
-   [PowerShell](#tabpanel_1_powershell)

1.  Open an elevated command prompt window.

2.  Run the following command replacing `YourDomainName` and `DomainUsername` with your values:

    Windows Command Prompt

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="cmd"}
    netdom join %COMPUTERNAME% /domain:YourDomainName /userd:DomainUsername /passwordd:*
    ```

3.  The system prompts you to enter the password for the specified domain user account.

4.  Reboot your device. Once you sign in, you\'re joined to the domain.

[](#rejoin-a-disjoined-device-to-a-domain)

## Rejoin a disjoined device to a domain {#rejoin-a-disjoined-device-to-a-domain .heading-anchor}

In cases where a client or server device is disjoined from the domain, you can restore its trust relationship by removing the device from the domain and then rejoining it. This process re-establishes the connection between the device and the domain. The process in leaving a domain is similar to joining one.

[](#rejoin-a-domain-using-server-manager)

### Rejoin a domain using Server Manager {#rejoin-a-domain-using-server-manager .heading-anchor}

To leave a domain using the *Server Manager*, follow the previous steps to join the domain until you reach the **System Properties** window.

1.  Under **Member of**, select **Workgroup**, type the name of a workgroup to temporarily join, and then select **OK**.

2.  Select **OK** again and then reboot your device.

3.  Once you sign back into the local account, repeat the steps to join your device to the domain it was disjoined from previously.

[](#rejoin-a-server-to-a-domain-using-control-panel)

### Rejoin a server to a domain using Control Panel {#rejoin-a-server-to-a-domain-using-control-panel .heading-anchor}

To leave a domain using the *Control Panel*, follow the previous steps to join the domain until you reach the **System Properties** window.

1.  Under **Member of**, select **Workgroup**, type the name of a workgroup to temporarily join, and then select **OK**.

2.  Select **OK** again and then reboot your device.

3.  Once you sign back into the local account, repeat the steps to join your device to the domain it was disjoined from previously.

[](#rejoin-a-client-to-a-domain-using-control-panel)

### Rejoin a client to a domain using Control Panel {#rejoin-a-client-to-a-domain-using-control-panel .heading-anchor data-id="rejoin-a-client-to-a-domain-using-control-panel"}

To leave a domain using the *Control Panel*, follow the previous steps to join the domain until you reach the **System Properties** window.

1.  Under **Member of**, select **Workgroup**, type the name of a workgroup to temporarily join, and then select **OK**.

2.  Select **OK** again and then reboot your device.

3.  Once you sign back into the local account, repeat the steps to rejoin your device to the domain it was disjoined from previously.

[](#rejoin-a-domain-using-settings)

### Rejoin a domain using Settings {#rejoin-a-domain-using-settings .heading-anchor data-id="rejoin-a-domain-using-settings"}

To leave a domain using the *Settings app*, follow the previous steps to join the domain until you reach the **Access work or school** window.

1.  Under your account, select **Disconnect**, then select **Yes**.

2.  Reboot your device.

3.  Once you sign back into the local account, repeat the steps to rejoin your device to the domain it was disjoined from previously.

[](#rejoin-a-domain-using-the-command-line)

### Rejoin a domain using the command line {#rejoin-a-domain-using-the-command-line .heading-anchor}

To leave a domain using the *command line*, follow these steps:

-   [Command Prompt](#tabpanel_2_cmd)
-   [PowerShell](#tabpanel_2_powershell)

1.  Open an elevated command prompt window.

2.  Run the following command replacing `YourDomainName` and `DomainUsername` with your values:

    Windows Command Prompt

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="cmd"}
    netdom remove %COMPUTERNAME% /domain:YourDomainName /userd:DomainUsername /passwordd:*
    ```

3.  The system prompts you to enter the password for the specified domain user account.

4.  After your device reboots, sign into the local account.

5.  Follow the steps provided in [Command line method](#command-line-method) to rejoin the domain.

[](#repair-domain-trust-relationship)

## Repair domain trust relationship {#repair-domain-trust-relationship .heading-anchor}

You might encounter the following error when the secure channel between a domain-joined computer and the domain controller is disrupted:

error

``` {.inner-focus data-language="error"}
The trust relationship between this workstation and the primary domain failed.
```

This error typically occurs when the machine\'s password isn\'t synchronized with the domain database. It can also happen if the computer account in the domain was deleted or became corrupt. You can resolve the trust relationship issue between the device and the domain using the command line.

-   [Command Prompt](#tabpanel_3_cmd)
-   [PowerShell](#tabpanel_3_powershell)

1.  Sign in with the local administrator account.

2.  Open an elevated command prompt window.

3.  Test the secure channel by running the following command replacing `ComputerName` and `YourDomainName` with your values:

    Windows Command Prompt

    ``` {.inner-focus data-language="cmd"}
    netdom verify ComputerName /domain:YourDomainName
    ```

4.  Reset the machine password by running the following command replacing `DomainControllerName` and `Domain\Username` with your values:

    Windows Command Prompt

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="cmd"}
    netdom resetpwd /server:DomainControllerName /userd:Domain\Username /passwordd:*
    ```

    You\'re prompted to provide the password for the account.

5.  Run the following command replacing `YourDomainName` and `DomainUsername` with your values to reset the secure channel:

    Windows Command Prompt

    ``` {.inner-focus data-language="cmd"}
    netdom reset /domain:YourDomainName /userd:DomainUsername /passwordd:*
    ```

    You\'re prompted to provide the password for the account.

6.  Restart your device for changes to take effect. Follow the steps provided in [Command line method](#command-line-method) to rejoin the domain.

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

-   [Active Directory domain join permissions in Windows Server](/en-us/windows-server/identity/ad-ds/manage/active-directory-domain-join-permissions?source=recommendations)

    This article describes the permissions required in Active Directory to successfully join computers to a Windows Server domain using a new computer account or an existing account.

-   [Active Directory domain join troubleshooting guidance - Windows Server](/en-us/troubleshoot/windows-server/active-directory/active-directory-domain-join-troubleshooting-guidance?source=recommendations)

    Provides guidance to troubleshoot domain join issues.

-   [Manage User Accounts with Active Directory Users and Computers in Windows Server](/en-us/windows-server/identity/ad-ds/manage-user-accounts-in-windows-server?source=recommendations)

    Create, delete, and manage user accounts in Active Directory Users and Computers. Learn how to manage user account properties, group memberships, and passwords.

-   [Active Directory Accounts](/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts?source=recommendations)

    This article discusses how to create default local Windows Server Active Directory accounts on a domain controller.

-   [Netdom join](/en-us/windows-server/administration/windows-commands/netdom-join?source=recommendations)

    Netdom is a command-line utility that joins a workstation or member server to a domain in Windows Server.

-   [Failure When You Use an Existing Computer Account to Join a Domain - Windows Server](/en-us/troubleshoot/windows-server/active-directory/failure-when-you-use-an-existing-computer-account-to-join-a-domain?source=recommendations)

    Addresses the issue of failing to join a computer to a domain when an existing computer account with the same name already exists.

-   [You cannot start the Active Directory Users and Computers tool because the server is not operational - Windows Server](/en-us/troubleshoot/windows-server/active-directory/cannot-start-active-directory-users-and-computers-tool?source=recommendations)

    Provides a solution to an issue where you cannot start the Active Directory Users and Computers tool because the server is not operational.

-   [Access is denied when joining computers - Windows Server](/en-us/troubleshoot/windows-server/active-directory/access-denied-when-joining-computers?source=recommendations)

    Provides a solution to an error message when non-administrator users who have been delegated control try to join computers to a domain.

Training

Module

[Guided project - Administer Active Directory Domain Services - Training](/en-us/training/modules/guided-project-administer-active-directory-domain-services/?source=recommendations)

This guided project helps prepare you to manage Active Directory Domain services, including creating and deploying domains, configuring group policy objects, establishing and enforcing passwords, and maintaining security of Active Directory.

------------------------------------------------------------------------

-    Last updated on 06/06/2025
