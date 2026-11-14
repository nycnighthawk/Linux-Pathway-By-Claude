---
{"title": "Command line process auditing", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Command line process auditing

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

**Author**: Justin Turner, Senior Support Escalation Engineer with the Windows group

Note

This content is written by a Microsoft customer support engineer, and is intended for experienced administrators and systems architects who are looking for deeper technical explanations of features and solutions in Windows Server 2012 R2 than topics on TechNet usually provide. However, it has not undergone the same editing passes, so some of the language may seem less polished than what is typically found on TechNet.

[](#overview)

## Overview {#overview .heading-anchor}

-   The pre-existing process creation audit event ID 4688 will now include audit information for command line processes.

-   It will also log SHA1/2 hash of the executable in the Applocker event log

    -   Application and Services Logs\\Microsoft\\Windows\\AppLocker

-   You enable via GPO, but it\'s disabled by default

    -   \"Include command line in process creation events\"

**Figure SEQ Figure \\\* ARABIC 16 Event 4688**

Review the updated event ID 4688 in REF \_Ref366427278 \\h Figure 16. Prior to this update none of the information for **Process Command Line** gets logged. Because of this additional logging we can now see that not only was the wscript.exe process started, but that it was also used to execute a VB script.

[](#configuration)

## Configuration {#configuration .heading-anchor}

To see the effects of this update, you\'ll need to enable two policy settings.

[](#you-must-have-audit-process-creation-auditing-enabled-to-see-event-id-4688)

### You must have Audit Process Creation auditing enabled to see event ID 4688. {#you-must-have-audit-process-creation-auditing-enabled-to-see-event-id-4688 .heading-anchor}

To enable the Audit Process Creation policy, edit the following group policy:

**Policy location:** Computer Configuration \> Policies \> Windows Settings \> Security Settings \> Advanced Audit Configuration \> Detailed Tracking

**Policy Name:** Audit Process Creation

**Supported on:** Windows 7 and above

**Description/Help:**

This security policy setting determines whether the operating system generates audit events when a process is created (starts) and the name of the program or user that created it.

These audit events can help you understand how a computer is being used and to track user activity.

Event volume: Low to medium, depending on system usage

**Default:** Not configured

[](#in-order-to-see-the-additions-to-event-id-4688-you-must-enable-the-new-policy-setting-include-command-line-in-process-creation-events)

### In order to see the additions to event ID 4688, you must enable the new policy setting: Include command line in process creation events {#in-order-to-see-the-additions-to-event-id-4688-you-must-enable-the-new-policy-setting-include-command-line-in-process-creation-events .heading-anchor}

**Table SEQ Table \\\* ARABIC 19 Command line process policy setting**

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Policy Configuration              | Details                                                                                                                                                                                                                                                                                                                                                                             |
+===================================+=====================================================================================================================================================================================================================================================================================================================================================================================+
| **Path**                          | Administrative Templates\\System\\Audit Process Creation                                                                                                                                                                                                                                                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Setting**                       | **Include command line in process creation events**                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default setting**               | Not Configured (not enabled)                                                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Supported on:**                 | ?                                                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Description**                   | This policy setting determines what information is logged in security audit events when a new process has been created.                                                                                                                                                                                                                                                             |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                     |
|                                   | This setting only applies when the Audit Process Creation policy is enabled. If you enable this policy setting the command line information for every process will be logged in plain text in the security event log as part of the Audit Process Creation event 4688, \"a new process has been created,\" on the workstations and servers on which this policy setting is applied. |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                     |
|                                   | If you disable or don\'t configure this policy setting, the process\'s command line information won\'t be included in Audit Process Creation events.                                                                                                                                                                                                                                |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                     |
|                                   | Default: Not configured                                                                                                                                                                                                                                                                                                                                                             |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                     |
|                                   | Note: When this policy setting is enabled, any user with access to read the security events will be able to read the command line arguments for any successfully created process. Command line arguments can contain sensitive or private information such as passwords or user data.                                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

When you use Advanced Audit Policy Configuration settings, you need to confirm that these settings aren\'t overwritten by basic audit policy settings. Event 4719 is logged when the settings are overwritten.

The following procedure shows how to prevent conflicts by blocking the application of any basic audit policy settings.

[](#to-ensure-that-advanced-audit-policy-configuration-settings-arent-overwritten)

### To ensure that Advanced Audit Policy Configuration settings aren\'t overwritten {#to-ensure-that-advanced-audit-policy-configuration-settings-arent-overwritten .heading-anchor}

1.  Open the Group Policy Management console

2.  Right-click Default Domain Policy, and then select Edit.

3.  Double-click Computer Configuration, double-click Policies, and then double-click Windows Settings.

4.  Double-click Security Settings, double-click Local Policies, and then select Security Options.

5.  Double-click Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings, and then select Define this policy setting.

6.  Select Enabled, and then select OK.

[](#additional-resources)

## Additional Resources {#additional-resources .heading-anchor}

[Audit Process Creation](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd941613(v=ws.10))

[Advanced Security Audit Policy Step-by-Step Guide](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd408940(v=ws.10))

[AppLocker: Frequently Asked Questions](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee619725(v=ws.10))

[](#try-this-explore-command-line-process-auditing)

## Try This: Explore command line process auditing {#try-this-explore-command-line-process-auditing .heading-anchor}

1.  Enable **Audit Process Creation** events and ensure the Advance Audit Policy configuration isn\'t overwritten

2.  Create a script that generates some events of interest and execute the script. Observe the events. The script used to generate the event in the lesson looked like this:

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
    mkdir c:\systemfiles\temp\commandandcontrol\zone\fifthward
    copy \\192.168.1.254\c$\hidden c:\systemfiles\temp\hidden\commandandcontrol\zone\fifthward
    start C:\systemfiles\temp\hidden\commandandcontrol\zone\fifthward\ntuserrights.vbs
    del c:\systemfiles\temp\*.* /Q
    ```

3.  Enable the command line process auditing

4.  Execute the same script as before and observe the events

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Advanced Audit Policy Configuration settings](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration?source=recommendations)

    The Advanced Audit Policy Configuration settings in Group Policy allows admins to specify which security events are audited on Windows systems for tracking activities, security monitoring, and incident detection.

Training

Module

[Implement Windows Server auditing and diagnostics - Training](/en-us/training/modules/implement-windows-server-auditing-diagnostics/?source=recommendations)

Learn how to implement Windows Server auditing for regulatory compliance and security, including basic and advanced audit policies, User Access Logging (UAL), and Setup and Boot Event Collection.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
