---
{"title": "OpenSSH for Windows overview", "url": "https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-overview", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# OpenSSH for Windows overview

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows 11](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client), ✅ [Windows 10](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client)

OpenSSH is the open-source version of the Secure Shell (SSH) tools used by administrators of Linux and other non-Windows for cross-platform management of remote systems. Beginning with Windows 10 build 1809 and Windows Server 2019, OpenSSH is available as a feature on demand.

SSH is based on a client-server architecture where the system the user is working on is the client and the remote system being managed is the server. OpenSSH includes a range of components and tools designed to provide a secure and straightforward approach to remote system administration.

The following table lists the default install state of OpenSSH for Windows on different Windows releases.

  Windows release           SSH install state
  ------------------------- -----------------------------------------------------------
  Windows Server 2019       Not installed, install and enable using optional features
  Windows Server 2022       Not installed, install and enable using optional features
  Windows Server 2025       Installed but not enabled
  Windows 10 build 1809 +   Not installed, install and enable using optional features

OpenSSH for Windows has the following commands built in.

-   `ssh` is the SSH client component that runs on the user\'s local system
-   `sshd` is the SSH server component that must be running on the system being managed remotely
-   `ssh-keygen` generates, manages and converts authentication keys for SSH
-   `ssh-agent` stores private keys used for public key authentication
-   `ssh-add` adds private keys to the list allowed by the server
-   `ssh-keyscan` aids in collecting the public SSH host keys from hosts
-   `sftp` is the service that provides the Secure File Transfer Protocol, and runs over SSH
-   `scp` is a file copy utility that runs on SSH

Tip

The documentation focuses on how OpenSSH is used on Windows, including installation, and Windows-specific configuration, commands, and use cases. Additional detailed documentation for common OpenSSH features is available online at [OpenSSH.com](https://www.openssh.com/manual.html).

Feedback on Windows OpenSSH is welcomed and can be provided by creating GitHub issues in our [OpenSSH GitHub repo](https://github.com/PowerShell/openssh-portable). The [OpenSSH open source project](https://www.openssh.com) is managed by developers at the OpenBSD Project. The Microsoft fork of this project is in [GitHub](https://github.com/PowerShell/openssh-portable).

[](#next-steps)

## Next steps {#next-steps .heading-anchor}

-   [Get started with OpenSSH](openssh_install_firstuse)

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

-   [Get started with OpenSSH Server for Windows](/en-us/windows-server/administration/openssh/openssh_install_firstuse?source=recommendations)

    Learn how to install and connect to remote machines using the OpenSSH Client and Server for Windows.

-   [Key-Based Authentication in OpenSSH for Windows](/en-us/windows-server/administration/openssh/openssh_keymanagement?source=recommendations)

    Find out about OpenSSH Server key-based authentication, generation, and deployment for Windows. See how to use built-in Windows tools or PowerShell to manage keys.

-   [Manage OpenSSH with Group Policy](/en-us/windows-server/administration/openssh/openssh-group-policy?source=recommendations)

    Learn how to create a Group Policy object for OpenSSH

-   [Can\'t install OpenSSH Features - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/cant-install-openssh-features?source=recommendations)

    Resolves various issues that occur when you try to install OpenSSH Server and OpenSSH Client on different versions of Windows Server and Windows Client.

-   [Troubleshoot OpenSSH Communication Through Windows Firewall - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/troubleshoot-openssh-windows-firewall-port22?source=recommendations)

    Discusses how to troubleshoot issues that affect OpenSSH commands that pass through Windows Firewall.

-   [OpenSSH Client Can\'t Connect To a Server via SSH - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/open-client-can-not-connect-server?source=recommendations)

    Addresses multiple common causes and solutions when encountering OpenSSH connection errors related to host key algorithm mismatches on Windows systems.

-   [Troubleshoot Common SFTP Issues - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/troubleshoot-sftp-issues-using-openssh?source=recommendations)

    Explains how to resolve common SFTP issues when you use OpenSSH for Windows.

Training

Module

[Develop on a Remote Machine Using SSH with Visual Studio Code - Training](/en-us/training/modules/develop-on-remote-machine/?source=recommendations)

In this module, you\'ll learn how to seamlessly develop on a remote machine using the Visual Studio Code Remote - SSH extension. We\'ll explore how to run and debug code located on a remote machine, while locally using Visual Studio Code\'s full feature set.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 02/20/2025
