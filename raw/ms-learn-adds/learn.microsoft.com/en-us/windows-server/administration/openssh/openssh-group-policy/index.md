---
{"title": "How to manage OpenSSH with Group Policy", "url": "https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-group-policy", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# How to manage OpenSSH with Group Policy

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows 11](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client), ✅ [Windows 10](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client)

Group Policy allows you to specify managed configurations for users and computers. This page will help you create a Group Policy object to manage the OpenSSH Server component.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

Before you start, the following prerequisites must be met:

-   You have administrator rights on the local device and the appropriate permissions to update Group Policy on your domain controller
-   You are managing the in-box version of OpenSSH
-   You are managing Operating Systems where both OpenSSH and Group Policy are present

[](#create-a-group-policy-object)

## Create a Group Policy Object {#create-a-group-policy-object .heading-anchor}

To create a Group Policy to manage OpenSSH perform the following steps:

1.  Open the Group Policy Management tool.
2.  In the navigation pane, expand `Forest: your forest name`, expand `Domains`, expand your domain.
3.  Select `Group Policy Objects`.
4.  Right-click `Group Policy Objects`, then select New to create a new Object.
5.  Name the Object so that it can be identified as managing OpenSSH.
6.  Double-click the new Object.
7.  Navigate to the `Settings` tab.
8.  Right-click on `Computer Configuration`, then select `Edit...`.
9.  In the navigation pane, expand `Computer Configuration`, expand `Policies`, expand `Windows Settings`, expand `Security Settings`, then select `System Services`.
10. Double-click `OpenSSH SSH Server` in the services list.
11. Click the checkmark `Define this policy setting`.
12. Select the desired service startup mode; `Automatic`, `Manual`, `Disabled`.
13. Select `Apply`.

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

-   [OpenSSH for Windows overview](/en-us/windows-server/administration/openssh/openssh-overview?source=recommendations)

    Overview of the OpenSSH tools used by Windows administrators for cross-platform management of remote systems.

-   [Get started with OpenSSH Server for Windows](/en-us/windows-server/administration/openssh/openssh_install_firstuse?source=recommendations)

    Learn how to install and connect to remote machines using the OpenSSH Client and Server for Windows.

-   [Key-Based Authentication in OpenSSH for Windows](/en-us/windows-server/administration/openssh/openssh_keymanagement?source=recommendations)

    Find out about OpenSSH Server key-based authentication, generation, and deployment for Windows. See how to use built-in Windows tools or PowerShell to manage keys.

-   [How to Enable OpenSSH Verbose Logging - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/enable-openssh-verbose-logging?source=recommendations)

    Explains how to enable verbose logging for the OpenSSH service.

-   [Troubleshoot Common SFTP Issues - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/troubleshoot-sftp-issues-using-openssh?source=recommendations)

    Explains how to resolve common SFTP issues when you use OpenSSH for Windows.

-   [Can\'t install OpenSSH Features - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/cant-install-openssh-features?source=recommendations)

    Resolves various issues that occur when you try to install OpenSSH Server and OpenSSH Client on different versions of Windows Server and Windows Client.

-   [Upgrade in-box OpenSSH to the Latest OpenSSH Release - Windows Server](/en-us/troubleshoot/windows-server/system-management-components/upgrade-in-box-openssh-to-latest-openssh-release?source=recommendations)

    Discusses the difference between the in-box and GitHub versions of OpenSSH, how to back up your existing configuration, and how to upgrade safely while keeping your service settings intact.

Training

Module

[Create and configure Group Policy Objects in Active Directory - Training](/en-us/training/modules/create-configure-group-policy-objects-active-directory/?source=recommendations)

This module focuses on Group Policy objects, including using them to enforce a robust password policy.

------------------------------------------------------------------------

-    Last updated on 02/13/2024
