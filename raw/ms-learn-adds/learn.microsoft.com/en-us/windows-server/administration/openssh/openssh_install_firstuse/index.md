---
{"title": "Get started with OpenSSH for Windows", "url": "https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Get started with OpenSSH for Windows

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows 11](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client), ✅ [Windows 10](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client)

OpenSSH is a connectivity tool for remote sign-in that uses the SSH protocol. It encrypts all traffic between client and server to eliminate eavesdropping, connection hijacking, and other attacks.

An OpenSSH-compatible client can be used to connect to Windows Server and Windows client devices.

This article uses the in-box OpenSSH Feature on Demand in Windows and Windows Server. Microsoft supports and services this version through Windows Update, so it\'s the recommended option for most users.

Microsoft also maintains [PowerShell/openssh-portable](https://github.com/PowerShell/openssh-portable), a fork of the upstream, open-source OpenSSH project. Its releases might differ from the version in Windows.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

Before you start, your computer must meet the following requirements:

-   A device running at least Windows Server 2019 or Windows 10 (build 1809).

-   PowerShell 5.1 or later.

-   An account that is a member of the built-in Administrators group.

[](#prerequisites-check)

### Prerequisites check {#prerequisites-check .heading-anchor}

To validate your environment, open an elevated PowerShell session and do the following:

-   Enter *winver.exe* and press enter to see the version details for your Windows device.

-   Run `$PSVersionTable.PSVersion`. Verify your major version is at least 5, and your minor version at least 1. Learn more about [installing PowerShell on Windows](/en-us/powershell/scripting/install/installing-powershell-on-windows).

-   To check when you\'re an administrator, run the following command. The output shows `True` when you\'re a member of the built-in Administrators group.

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    (New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    ```

[](#enable-openssh-server)

## Enable OpenSSH Server {#enable-openssh-server .heading-anchor}

Beginning with Windows Server 2025, OpenSSH is now installed by default. You can also enable or disable the `sshd` service in Server Manager.

-   [GUI](#tabpanel_1_gui)
-   [PowerShell](#tabpanel_1_powershell)

To enable SSHD using Server Manager:

1.  In **Server Manager**, on the navigation pane to the left, select **Local Server**.

2.  In the **Properties** window, locate **Remote SSH Access**.

3.  Select **Enabled** to enable the OpenSSH service.

Note

If you need to allow or restrict specific users or groups from using OpenSSH for remote access, add them to the **OpenSSH Users** user group.

[](#install-openssh-server--client)

## Install OpenSSH Server & Client {#install-openssh-server-client .heading-anchor data-id="install-openssh-server--client"}

-   [GUI](#tabpanel_2_gui)
-   [PowerShell](#tabpanel_2_powershell)

To install the OpenSSH components on Windows Server devices:

1.  Select **Start**, type *Optional Features* in the search box, then select **Optional Features**.

2.  Scan the list to see if the OpenSSH is already installed. If not, at the top of the page, select **Views features**, then:

    -   Search for and select **OpenSSH Client**, then select **Add**

    -   Search for and select **OpenSSH Server**, then select **Add**

3.  Open the **Services** desktop app. (Select **Start**, type *services.msc* in the search box, and then select the **Services** app or press ENTER.)

4.  In the details pane, double-click **OpenSSH SSH Server**.

5.  On the **General** tab, from the **Startup type** drop-down menu, select **Automatic** and then select **Ok**.

6.  To start the service, select **Start**.

Note

Installing OpenSSH Server creates and enables a firewall rule named `OpenSSH-Server-In-TCP`. This rule allows inbound SSH traffic on port 22. If this rule isn\'t enabled and this port isn\'t open, connections are refused or reset.

[](#install-openssh-server--client-1)

## Install OpenSSH Server & Client {#install-openssh-server-client-1 .heading-anchor data-id="install-openssh-server--client-1"}

-   [GUI](#tabpanel_3_gui)
-   [PowerShell](#tabpanel_3_powershell)

To install the OpenSSH components on Windows Server devices:

1.  Select **Start**, type *Optional Feature* in the search box, then select **Add an optional feature**.

2.  Scan the list to see if the OpenSSH is already installed. If not, at the top of the page, select **Add a feature**, then:

    -   Search for **OpenSSH Client**, then select **Install**

    -   Search for **OpenSSH Server**, then select **Install**

3.  Open the **Services** desktop app. (Select **Start**, type *services.msc* in the search box, and then select the **Services** app or press ENTER.)

4.  In the details pane, double-click **OpenSSH SSH Server**.

5.  On the **General** tab, from the **Startup type** drop-down menu, select **Automatic** and then select **Ok**.

6.  To start the service, select **Start**.

Note

Installing OpenSSH Server creates and enables a firewall rule named `OpenSSH-Server-In-TCP`. This rule allows inbound SSH traffic on port 22. If this rule isn\'t enabled and this port isn\'t open, connections are refused or reset.

[](#install-openssh-server--client-2)

## Install OpenSSH Server & Client {#install-openssh-server-client-2 .heading-anchor data-id="install-openssh-server--client-2"}

-   [GUI](#tabpanel_4_gui)
-   [PowerShell](#tabpanel_4_powershell)

To install the OpenSSH components on Windows Server devices:

1.  Select **Start**, type *Optional Features* in the search box, then select **Optional Features** (also referred to as **Manage optional features**).

2.  Scan the list to see if the OpenSSH is already installed. If not, at the top of the page, select **Add a feature**, then:

    -   Search for **OpenSSH Client**, then select **Install**

    -   Search for **OpenSSH Server**, then select **Install**

3.  Open the **Services** desktop app. (Select **Start**, type *services.msc* in the search box, and then select the **Services** app or press ENTER.)

4.  In the details pane, double-click **OpenSSH SSH Server**.

5.  On the **General** tab, from the **Startup type** drop-down menu, select **Automatic** and then select **Ok**.

6.  To start the service, select **Start**.

Note

Installing OpenSSH Server creates and enables a firewall rule named `OpenSSH-Server-In-TCP`. This rule allows inbound SSH traffic on port 22. If this rule isn\'t enabled and this port isn\'t open, connections are refused or reset.

[](#connect-to-openssh-server)

## Connect to OpenSSH Server {#connect-to-openssh-server .heading-anchor}

Once installed, you can connect to OpenSSH Server from a Windows or Windows Server device with the OpenSSH client installed. From a PowerShell prompt, run the following command.

PowerShell

``` {.inner-focus data-language="powershell"}
ssh domain\username@servername
```

Once connected, you get a message similar to the following output.

PowerShell

``` {.inner-focus data-language="powershell"}
The authenticity of host 'servername (10.00.00.001)' can't be established.
ECDSA key fingerprint is SHA256:(<a large string>).
Are you sure you want to continue connecting (yes/no)?
```

Entering *yes* adds that server to the list of known SSH hosts on your Windows client.

At this point, the service prompts you for your password. As a security precaution, the characters of your password aren\'t displayed as you enter them.

Once connected, you should see the following Windows command shell prompt:

PowerShell

``` {.inner-focus data-language="powershell"}
domain\username@SERVERNAME C:\Users\username>
```

[](#disable-openssh-server)

## Disable OpenSSH Server {#disable-openssh-server .heading-anchor}

You can disable the `sshd` service in Server Manager.

-   [GUI](#tabpanel_5_gui)
-   [PowerShell](#tabpanel_5_powershell)

To disable SSHD using Server Manager:

1.  In **Server Manager**, on the navigation pane to the left, select **Local Server**.

2.  In the **Properties** window, locate **Remote SSH Access**.

3.  Select **Disabled** to disable the OpenSSH service.

Note

If you need to allow or restrict specific users or groups from using OpenSSH for remote access, add them to the **OpenSSH Users** user group.

[](#uninstall-openssh-server--client)

## Uninstall OpenSSH Server & Client {#uninstall-openssh-server-client .heading-anchor data-id="uninstall-openssh-server--client"}

-   [GUI](#tabpanel_6_gui)
-   [PowerShell](#tabpanel_6_powershell)

To uninstall OpenSSH using Windows Settings:

1.  Select **Start**, type *Optional Features* in the search box, then select **Optional feature**.

2.  Scan the list to see if the OpenSSH is installed:

    -   Search for and select **OpenSSH Client**, then select **Remove**

    -   Search for and select **OpenSSH Server**, then select **Remove**

[](#uninstall-openssh-server--client-1)

## Uninstall OpenSSH Server & Client {#uninstall-openssh-server-client-1 .heading-anchor data-id="uninstall-openssh-server--client-1"}

-   [GUI](#tabpanel_7_gui)
-   [PowerShell](#tabpanel_7_powershell)

To uninstall OpenSSH using Windows Settings:

1.  Select **Start**, type *Optional Features* in the search box, then select **Optional features** (also referred to as **Manage optional features** or **See optional feature history**).

2.  In the list, select **OpenSSH Client** or **OpenSSH Server**.

3.  Select **Uninstall**.

If the service was in use when you uninstalled it, you should restart Windows.

[](#next-steps)

## Next steps {#next-steps .heading-anchor}

Now that you\'re done installing OpenSSH Server for Windows, here are some articles that can help you learn how to use it:

-   Learn more about using key pairs for authentication in [OpenSSH key management](openssh_keymanagement)

-   Learn more about the [OpenSSH Server configuration for Windows](openssh_server_configuration)

**Note:** The author created this article with assistance from AI. [Learn more](/principles-for-ai-generated-content)

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

-   [OpenSSH Server Configuration for Windows](/en-us/windows-server/administration/openssh/openssh-server-configuration?source=recommendations)

    Learn about the Windows-specific configuration options for OpenSSH Server on Windows Server and Windows.

-   [Key-Based Authentication in OpenSSH for Windows](/en-us/windows-server/administration/openssh/openssh_keymanagement?source=recommendations)

    Find out about OpenSSH Server key-based authentication, generation, and deployment for Windows. See how to use built-in Windows tools or PowerShell to manage keys.

-   [OpenSSH for Windows overview](/en-us/windows-server/administration/openssh/openssh-overview?source=recommendations)

    Overview of the OpenSSH tools used by Windows administrators for cross-platform management of remote systems.

-   [Troubleshoot OpenSSH Communication Through Windows Firewall - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/troubleshoot-openssh-windows-firewall-port22?source=recommendations)

    Discusses how to troubleshoot issues that affect OpenSSH commands that pass through Windows Firewall.

-   [Manage OpenSSH with Group Policy](/en-us/windows-server/administration/openssh/openssh-group-policy?source=recommendations)

    Learn how to create a Group Policy object for OpenSSH

-   [OpenSSH Client Can\'t Connect To a Server via SSH - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/open-client-can-not-connect-server?source=recommendations)

    Addresses multiple common causes and solutions when encountering OpenSSH connection errors related to host key algorithm mismatches on Windows systems.

-   [Upgrade in-box OpenSSH to the Latest OpenSSH Release - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/upgrade-in-box-openssh-to-latest-openssh-release?source=recommendations)

    Discusses the difference between the in-box and GitHub versions of OpenSSH, how to back up your existing configuration, and how to upgrade safely while keeping your service settings intact.

-   [Can\'t install OpenSSH Features - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/cant-install-openssh-features?source=recommendations)

    Resolves various issues that occur when you try to install OpenSSH Server and OpenSSH Client on different versions of Windows Server and Windows Client.

Training

Module

[Develop on a Remote Machine Using SSH with Visual Studio Code - Training](/en-us/training/modules/develop-on-remote-machine/?source=recommendations)

In this module, you\'ll learn how to seamlessly develop on a remote machine using the Visual Studio Code Remote - SSH extension. We\'ll explore how to run and debug code located on a remote machine, while locally using Visual Studio Code\'s full feature set.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 09/04/2025
