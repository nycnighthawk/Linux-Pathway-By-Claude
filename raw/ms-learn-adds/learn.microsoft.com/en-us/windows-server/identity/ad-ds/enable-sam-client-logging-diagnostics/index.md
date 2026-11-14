---
{"title": "Enable SAM client logging and diagnostics", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/enable-sam-client-logging-diagnostics", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Enable SAM client logging and diagnostics

-   Applies to: ✅ [Windows 11](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client)

Security Account Manager (SAM) client event logging is a diagnostic capability in Windows that helps identify sources of excessive SAM traffic that can cause domain controller high central processing unit (CPU) usage and authentication delays. It records SAM client operations, such as account lookups and domain enumeration, through a dedicated event log channel.

When you troubleshoot an overloaded domain controller, you need to know which clients are generating the SAM traffic behind it. Enabling SAM client event logging pinpoints the processes, services, and executables responsible and reveals unexpected usage patterns, so you can target the actual source instead of guessing.

In this article, you enable and disable the SAM client event log, configure its logging options, and review the events it records and where to find them.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

-   Windows 11 with the [2026-06 Security Update (KB5095093)](https://support.microsoft.com/help/5095093) or later
-   Administrator or equivalent access to the Windows system.

[](#enable-the-sam-client-event-log)

## Enable the SAM client event log {#enable-the-sam-client-event-log .heading-anchor}

The SAM client event logging feature uses a dedicated event log channel that records SAM client operations in a consistent, administrator-friendly format.

To help protect potentially sensitive diagnostic data, only users with appropriate administrative privileges can enable the feature and access the resulting logs.

The SAM client event log records activity from any Windows system that generates SAM traffic toward a domain controller. This activity includes client and server stock keeping units (SKUs) and both domain-joined and non-domain-joined systems.

To enable SAM client logging, follow these steps:

1.  Select the **Start** button, type **Event Viewer**, and open **Event Viewer** from the best match list.

2.  In Event Viewer, go to **Applications and Services Logs** \> **Microsoft** \> **Windows** \> **SAMLIB**.

3.  Select and hold (or right-click) **Debug**, and then select **Enable Log**.

    [](media/enable-sam-client-logging-diagnostics/enable-samlib-debug-log.png#lightbox)

When you enable the SAM client event log, it records operations such as connections, handle operations, domain lookups, and enumeration requests.

To stop logging, repeat these steps and select **Disable Log** in step 3.

[](#review-sam-client-events)

## Review SAM client events {#review-sam-client-events .heading-anchor}

SAM client events record the operation and the process responsible for the call. The following table summarizes the common event IDs in the SAM client event log (the **SAMLIB** \> **Debug** channel in Event Viewer).

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Event ID          Operation                          Event text                                Description
  ----------------- ---------------------------------- ----------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  1000              `SamConnect`                       SamConnect called:\                       Indicates a client connecting to a SAM server. Captures the target server and calling process.
                                                       ServerName: `<server>`\                   
                                                       DesiredAccess: `<access>`\                
                                                       Calling process: `<process>`              

  1002              `SamCloseHandle`                   SamCloseHandle called:\                   Records cleanup of SAM handles. Useful for validating proper client behavior.
                                                       SamHandle: `<handle>`\                    
                                                       Calling process: `<process>`              

  1010              `SamLookupDomainInSamServer`       SamLookupDomainInSamServer called:\       Records domain lookup operations. Useful when correlating name resolution and lookup behavior.
                                                       ServerHandle: `<handle>`\                 
                                                       Name: `<name>`\                           
                                                       Calling process: `<process>`              

  1012              `SamEnumerateDomainsInSamServer`   SamEnumerateDomainsInSamServer called:\   Indicates enumeration of available domains. Often appears during group or account queries.
                                                       ServerHandle: `<handle>`\                 
                                                       PreferredMaximumLength: `<length>`\       
                                                       Calling process: `<process>`              

  1014              `SamOpenDomain`                    SamOpenDomain called:\                    Indicates that a client opens a domain handle. Helps identify access patterns and permission-related activity.
                                                       ServerHandle: `<handle>`\                 
                                                       DesiredAccess: `<access>`\                
                                                       DomainId: `<domain ID>`\                  
                                                       Calling process: `<process>`              

  1100              `SamGetCompatibilityMode`          SamGetCompatibilityMode called:\          Records the compatibility checks the client performs. Useful for understanding client behavior during initialization.
                                                       Handle: `<handle>`\                       
                                                       Calling process: `<process>`              
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use these events to correlate process-level activity with observed behavior on domain controllers. The following screenshot shows an example of Event 1000 (SamConnect) in Event Viewer, including the server name, desired access, and calling process.

[](media/enable-sam-client-logging-diagnostics/sam-event-1000-samconnect.png#lightbox)

[The Event 1000 properties show: SamConnect called, ServerName (blank for local), DesiredAccess 0x30, and the calling process path (for example, \`C:\\Windows\\system32\\lsass.exe\`). The Log Name is Microsoft-Windows-SAMLIB/Debug, Source is SAMLIB, and Level is Information.](media/enable-sam-client-logging-diagnostics/sam-event-1000-samconnect.png#lightbox)

[](media/enable-sam-client-logging-diagnostics/sam-event-1000-samconnect.png#lightbox)

[](#manage-command-line-argument-logging)

## Manage command-line argument logging {#manage-command-line-argument-logging .heading-anchor}

By default, SAM client events identify the calling executable but omit command-line arguments. This default behavior protects against inadvertent exposure of sensitive data. For advanced scenarios, you can enable command-line argument logging by using a registry key.

Caution

Because command-line arguments can contain sensitive information such as credentials or user data, enable this setting only when necessary for targeted diagnostics and disable it immediately after data collection.

To enable command-line argument logging, follow these steps:

1.  Open Registry Editor.

2.  Go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SAMLIB`.

3.  Set the `IncludeArguments` `REG_DWORD` value to `1` to enable command-line argument logging.

    [](media/enable-sam-client-logging-diagnostics/samlib-includearguments-registry.png#lightbox)

4.  To disable command-line argument logging, set `IncludeArguments` back to `0`.

After you change the registry value, restart the computer for the new setting to take effect.

The following table summarizes the `IncludeArguments` registry value behavior:

  Value           Behavior
  --------------- -----------------------------------------------------------------
  `0` (default)   Events show the calling process without command-line arguments.
  `1`             Events include the full command line of the calling process.

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Security Account Manager Remote (SAMR) protocol](/en-us/openspecs/windows_protocols/ms-samr/96952411-1d17-4fe4-879c-d5b48a264314)

**Note:** The author created this article with assistance from AI. [Learn more](/principles-for-ai-generated-content)

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

-    Last updated on 07/16/2026
