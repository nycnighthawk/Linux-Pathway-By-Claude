---
{"title": "Credential Guard protected machine accounts", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/credential-guard-protected-machine-accounts", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Credential Guard protected machine accounts

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Important

Starting with the April Windows security update ([KB5055523](https://aka.ms/WinServer2025/5055523)), Credential Guard protected machine accounts is temporarily disabled in Windows Server 2025 and Windows 11, version 24H2. This feature has been disabled due to an issue with machine password rotation using Kerberos. The feature remains disabled until a permanent fix is available. To learn more about the machine password rotation issue, see the [Windows Server 2025 known issues and notifications](/en-us/windows/release-health/status-windows-server-2025?context=%2Fwindows-server%2Fcontext%2Fwindows-server-get-started) article.

Recent Windows features, such as the Flexible Authentication Secure Tunneling (FAST) Kerberos extension, also known as Kerberos Armoring, became increasingly dependent on machine accounts to enhance security. The machine account is used to add entropy to the client\'s secret key and both gMSA and dMSA service accounts now rely on machine accounts and grant them access to service accounts. However, this reliance on machine accounts created a vulnerability in service account security, as machine accounts can be easily extracted from the registry and used to access highly secured service accounts.

In order to strengthen service account security, the opt-in feature of machine accounts in Credential Guard is now available in Windows Server 2025 devices that have Credential Guard enabled. It\'s crucial to take measures to address this issue. This feature relocates the storage of machine account credentials from the registry to Credential Guard, which provides a separate trusted execution environment for the machine account password. Security is improved by ensuring that:

-   The password can\'t be accessed by unprivileged users, administrators, or drivers.
-   The security of machine accounts is enhanced, which hardens the overall security of service accounts in Active Directory (AD).

[](#machine-identity-isolation)

## Machine Identity Isolation {#machine-identity-isolation .heading-anchor}

Enabling machine identity isolation allows for virtualization-based protection of AD machine accounts. When enabled, the machine account credentials of the device will be relocated into Credential Guard. As a result, all future machine account authentications, such as logging into a domain-joined device, will be routed through Credential Guard. However, if Credential Guard fails to start after a device reboot, it results in the inability to complete domain authentication, potentially requiring intervention from a local administrator account to recover.

[](#machine-identity-isolation-configuration)

### Machine Identity Isolation Configuration {#machine-identity-isolation-configuration .heading-anchor}

To enable the **Machine Identity Isolation Configuration** setting, open **Group Policy** and navigate to the following path, and select **Enabled**:

-   **Computer Configuration\\Administrative Templates\\System\\Device Guard\\Turn On Virtualization Based Security**

The available options for this specific setting are:

-   **Disabled**: Turns off Machine Identity Isolation. If this policy was previously set to *Enabled in audit mode*, no further action is needed. If this policy was previously set to *Enabled in enforcement mode*, the device must be unjoined and rejoined to the domain, as it\'s unable to authenticate otherwise.

    Note

    -   If local cached logon is enabled when this setting is disabled, local logon will still work while the cache is fresh, but domain authentication will break.

    -   Only the local administrator account can be used to unjoin and rejoin the machine.

-   **Enabled in audit mode**: This option creates a new secret in Credential Guard and copies it into the Local Security Authority (LSA). The old LSA secret is then deleted. When auditing, attempts to authenticate the machine identity will first try to use the copy in Credential Guard. If that fails, authentication falls back to using the original machine identity from LSA.

    Note

    If the policy was previously set to enforcement mode, the device must be manually unjoined and rejoined.

-   **Enabled in enforcement mode**: This option moves the machine account secret into Credential Guard and deletes it from LSA. This makes the machine account secret inaccessible except as utilized by Credential Guard for machine authentication.

-   **Not Configured**: Leaves the policy setting undefined. Group Policy doesn\'t write the policy setting to the registry and has no impact on computers or users. If there\'s a current setting in the registry, it won\'t be modified.

[](#see-also)

## See also {#see-also .heading-anchor}

-   [Credential Guard overview](/en-us/windows/security/identity-protection/credential-guard)

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

-   [Credential Guard overview](/en-us/windows/security/identity-protection/credential-guard/?source=recommendations)

    Learn about Credential Guard and how it isolates secrets so that only privileged system software can access them.

-   [Additional mitigations](/en-us/windows/security/identity-protection/credential-guard/additional-mitigations?source=recommendations)

    Learn how to improve the security of your domain environment with additional mitigations for Credential Guard and sample code.

-   [Considerations and known issues when using Credential Guard](/en-us/windows/security/identity-protection/credential-guard/considerations-known-issues?source=recommendations)

    Considerations, recommendations, and known issues when using Credential Guard.

-   [Configure added LSA protection](/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection?source=recommendations)

    See how to configure added protection for the Local Security Authority (LSA) process to prevent code injection that can compromise credentials.

-   [How Credential Guard works](/en-us/windows/security/identity-protection/credential-guard/how-it-works?source=recommendations)

    Learn how Credential Guard uses virtualization to protect secrets, so that only privileged system software can access them.

-   [Configure Credential Guard](/en-us/windows/security/identity-protection/credential-guard/configure?source=recommendations)

    Learn how to configure Credential Guard using MDM, Group Policy, or the registry.

-   [LsaCfgFlags](/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-deviceguard-unattend-lsacfgflags?source=recommendations)

    Use to enable the Credential Guard, which uses virtualization-based security to isolate secrets so that only privileged system software can access them when they are stored on disk or in memory. For more information, see Credential Guard.

Training

Module

[Secure Windows Server user accounts - Training](/en-us/training/modules/secure-windows-server-user-accounts/?source=recommendations)

Learn how to secure Active Directory user accounts using least privilege, Protected Users group, authentication policy silos, Windows Defender Credential Guard, NTLM blocking, and account remediation techniques.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 04/11/2025
