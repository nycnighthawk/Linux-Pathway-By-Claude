---
{"title": "Verify DNS Functionality to Support Directory Replication", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/troubleshoot/verify-dns-functionality-to-support-directory-replication", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Verify DNS Functionality to Support Directory Replication

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

To check Domain Name System (DNS) settings that might interfere with Active Directory replication, you can begin by running the basic test that ensures that DNS is operating properly for your domain. After you run the basic test, you can test other aspects of DNS functionality, including resource record registration and dynamic update.

Although you can run this test of basic DNS functionality on any domain controller, typically you run this test on domain controllers that you think may be experiencing replication issues, for example, domain controllers that report Event IDs 1844, 1925, 2087, or 2088 in the Event Viewer Directory Service DNS log.

[](#running-the-domain-controller-basic-dns-test)

## Running the domain controller basic DNS test {#running-the-domain-controller-basic-dns-test .heading-anchor}

The basic DNS test checks the following aspects of DNS functionality:

-   **Connectivity:** The test determines whether domain controllers are registered in DNS, can be contacted by the `ping` command, and have Lightweight Directory Access Protocol / remote procedure call (LDAP/RPC) connectivity. If the connectivity test fails on a domain controller, no other tests are run against that domain controller. The connectivity test is performed automatically before any other DNS test is run.
-   **Essential services:** The test confirms that the following services are running and available on the tested domain controller: DNS Client service, Net Logon service, Key Distribution Center (KDC) service, and DNS Server service (if DNS is installed on the domain controller).
-   **DNS client configuration:** The test confirms that DNS servers on all network adapters of the DNS client computer are reachable.
-   **Resource record registrations:** The test confirms that the host (A) resource record of each domain controller is registered on at least one of the DNS servers that is configured on the client computer.
-   **Zone and start of authority (SOA):** If the domain controller is running the DNS Server service, the test confirms that the Active Directory domain zone and start of authority (SOA) resource record for the Active Directory domain zone are present.
-   **Root zone:** Checks whether the root (.) zone is present.

Membership in Enterprise Admins, or equivalent, is the minimum required to complete these procedures.

You can use the following procedure to verify basic DNS functionality.

[](#to-verify-basic-dns-functionality)

### To verify basic DNS functionality: {#to-verify-basic-dns-functionality .heading-anchor}

1.  On the domain controller that you want to test or on a domain member computer that has Active Directory Domain Services (AD DS) Tools installed, open a command prompt as an administrator. To open a command prompt as an administrator, click **Start**.

2.  In Start Search, type Command Prompt.

3.  At the top of the Start menu, right-click Command Prompt, and then click Run as administrator. If the User Account Control dialog box appears, confirm that the action it displays is what you want, and then click Continue.

4.  At the command prompt, type the following command, and then press ENTER: `dcdiag /test:dns /v /s:<DCName> /DnsBasic /f:dcdiagreport.txt`\
    \
    Substitute the actual distinguished name, NetBIOS name, or DNS name of the domain controller for \<DCName\>. As an alternative, you can test all the domain controllers in the forest by typing /e: instead of /s:. The /f switch specifies a file name, which in the previous command is dcdiagreport.txt. If you want to place the file in a location other than the current working directory, you can specify a file path, such as /f:c:reportsdcdiagreport.txt.

5.  Open the dcdiagreport.txt file in Notepad or a similar text editor. To open the file in Notepad, at the command prompt, type notepad dcdiagreport.txt, and then press ENTER. If you placed the file in a different working directory, include the path to the file. For example, if you placed the file in c:reports, type notepad c:reportsdcdiagreport.txt, and then press ENTER.

6.  Scroll to the Summary table near the bottom of the file.\
    \
    Note the names of all the domain controllers that report \"Warn\" or \"Fail\" status in the Summary table. Try to determine if there is a problem domain controller by finding the detailed breakout section by searching for the string \"DC: DCName,\" where DCName is the actual name of the domain controller.

If you see obvious configuration changes that are required, make them, as appropriate. For example, if you notice that one of your domain controllers has an obviously incorrect IP address, you can correct it. Then, rerun the test.

To validate the configuration changes, rerun the Dcdiag /test:DNS /v command with the /e: or /s: switch, as appropriate. If you do not have IP version 6 (IPv6) enabled on the domain controller, you should expect the host (AAAA) validation portion of the test to fail, but if you are not using IPv6 on your network, these records are not necessary.

[](#verifying-resource-record-registration)

## Verifying resource record registration {#verifying-resource-record-registration .heading-anchor}

The destination domain controller uses the DNS alias (CNAME) resource record to locate its source domain controller replication partner. Although domain controllers running Windows Server (starting with Windows Server 2003 with Service Pack 1 (SP1)) can locate source replication partners by using fully qualified domain names (FQDNs)or, if that fails, NetBIOS names the presence of the alias (CNAME) resource record is expected and should be verified for proper DNS functioning.

You can use the following procedure to verify resource record registration, including alias (CNAME) resource record registration.

[](#to-verify-resource-record-registration)

### To verify resource record registration {#to-verify-resource-record-registration .heading-anchor}

1.  Open a command prompt as an administrator. To open a command prompt as an administrator, click Start. In Start Search, type Command Prompt.
2.  At the top of the Start menu, right-click Command Prompt, and then click Run as administrator. If the User Account Control dialog box appears, confirm that the action it displays is what you want, and then click Continue.\
    \
    You can use the Dcdiag tool to verify registration of all the resource records that are essential for domain controller location by running the `dcdiag /test:dns /DnsRecordRegistration` command.

This command verifies registration of the following resource records in DNS:

-   **alias (CNAME):** the globally unique identifier (GUID)-based resource record that locates a replication partner
-   **host (A):** the host resource record that contains the IP address of the domain controller
-   **LDAP SRV:** the service (SRV) resource records that locate LDAP servers
-   **GC SRV**: the service (SRV) resource records that locate global catalog servers
-   **PDC SRV**: the service (SRV) resource records that locate primary domain controller (PDC) emulator operations masters

You can use the following procedure to verify alias (CNAME) resource record registration alone.

[](#to-verify-alias-cname-resource-record-registration)

### To verify alias (CNAME) resource record registration {#to-verify-alias-cname-resource-record-registration .heading-anchor}

1.  Open the DNS snap-in. To open DNS, click Start. In Start Search, type dnsmgmt.msc, and then press ENTER. If the User Account Control dialog box appears, confirm that it displays the action you want, and then click Continue.
2.  Use the DNS snap-in to locate any domain controller that is running the DNS Server service, where the server hosts the DNS zone with the same name as the Active Directory domain of the domain controller.
3.  In the console tree, click the zone that is named \_msdcs.Dns_Domain_Name.
4.  In the details pane, verify that the following resource records are present: an alias (CNAME) resource record that is named Dsa_Guid.\_msdcs.\<Dns_Domain_Name\> and a corresponding host (A) resource record for the name of the DNS server.

If the alias (CNAME) resource record is not registered, verify that dynamic update is functioning properly. Use the test in the following section to verify dynamic update.

[](#verifying-dynamic-update)

## Verifying dynamic update {#verifying-dynamic-update .heading-anchor}

If the basic DNS test shows that resource records do not exist in DNS, use the dynamic update test to determine why the Net Logon service did not register the resource records automatically. To verify that the Active Directory domain zone is configured to accept secure dynamic updates and to perform registration of a test record (\_dcdiag_test_record), use the following procedure. The test record is deleted automatically after the test.

[](#to-verify-dynamic-update)

### To verify dynamic update {#to-verify-dynamic-update .heading-anchor}

1.  Open a command prompt as an administrator. To open a command prompt as an administrator, click Start. In Start Search, type Command Prompt. At the top of the Start menu, right-click Command Prompt, and then click Run as administrator. If the User Account Control dialog box appears, confirm that the action it displays is what you want, and then click Continue.
2.  At the command prompt, type the following command, and then press ENTER: `dcdiag /test:dns /v /s:<DCName> /DnsDynamicUpdate`\
    \
    Substitute the distinguished name, NetBIOS name, or DNS name of the domain controller for \<DCName\>. As an alternative, you can test all the domain controllers in the forest by typing /e: instead of /s:. If you do not have IPv6 enabled on the domain controller, you should expect the host (AAAA) resource record portion of the test to fail, which is a normal condition when IPv6 is not enabled.

If secure dynamic updates are not configured, you can use the following procedure to configure them.

[](#to-enable-secure-dynamic-updates)

### To enable secure dynamic updates {#to-enable-secure-dynamic-updates .heading-anchor}

1.  Open the DNS snap-in. To open DNS, click Start.
2.  In Start Search, type dnsmgmt.msc, and then press ENTER. If the User Account Control dialog box appears, confirm that it displays the action you want and then click Continue.
3.  In the console tree, right-click the applicable zone, and then click Properties.
4.  On the General tab, verify that the zone type is Active Directory-integrated.
5.  In Dynamic Updates, click Secure only.

[](#registering-dns-resource-records)

## Registering DNS resource records {#registering-dns-resource-records .heading-anchor}

If DNS resource records do not appear in DNS for the source domain controller, you have verified dynamic updates, and you want to register DNS resource records immediately, you can force registration manually by using the following procedure. The Net Logon service on a domain controller registers the DNS resource records that are required for the domain controller to be located on the network. The DNS Client service registers the host (A) resource record that the alias (CNAME) record points to.

[](#to-register-dns-resource-records-manually)

### To register DNS resource records manually {#to-register-dns-resource-records-manually .heading-anchor}

1.  Open a command prompt as an administrator. To open a command prompt as an administrator, click Start.
2.  In Start Search, type Command Prompt.
3.  At the top of the Start, right-click Command Prompt, and then click Run as administrator. If the User Account Control dialog box appears, confirm that the action it displays is what you want, and then click Continue.
4.  To initiate registration of domain controller locator resource records manually on the source domain controller, at the command prompt, type the following command, and then press ENTER: `net stop netlogon && net start netlogon`
5.  To initiate registration of the host (A) resource record manually, at the command prompt, type the following command, and then press ENTER: `ipconfig /flushdns && ipconfig /registerdns`
6.  At the command prompt, type the following command, and then press ENTER: `dcdiag /test:dns /v /s:<DCName>`\
    \
    Substitute the distinguished name, NetBIOS name, or DNS name of the domain controller for \<DCName\>. Review the output of the test to ensure that the DNS tests passed. If you do not have IPv6 enabled on the domain controller, you should expect the host (AAAA) resource record portion of the test to fail, which is a normal condition when IPv6 is not enabled.

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

-   [Errors when you run DCDIAG commands - Windows Server](/en-us/troubleshoot/windows-server/active-directory/dcdiag-commands-running-errors?source=recommendations)

    Fixes errors that occur when you run DCDIAG.EXE /E or /A or /C commands.

-   [AD Replication error 1908 - Windows Server](/en-us/troubleshoot/windows-server/active-directory/ad-replication-error-1908-not-find-domain-controller?source=recommendations)

    Provides a resolution for troubleshooting AD Replication error 1908, which is Could not find the domain controller for this domain.

-   [Troubleshoot DNS Event ID 4013 - Windows Server](/en-us/troubleshoot/windows-server/networking/troubleshoot-dns-event-id-4013?source=recommendations)

    Solves an issue that the DNS server can\'t load AD-integrated DNS zones.

-   [Force synchronization for Distributed File System Replication (DFSR) replicated sysvol replication - Windows Server](/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization?source=recommendations)

    Describes how to restart DFSR on a server, either authoritatively or non-authoritative.

-   [The NETLOGON share is not present after you install Active Directory Domain Services on a new full or read-only Windows Server 2008-based domain controller - Windows Server](/en-us/troubleshoot/windows-server/active-directory/netlogon-share-not-present-after-install-ad-ds-on-full-read-only-domain-controller?source=recommendations)

    This article contains a workaround for a problem that occurs after you install AD DS on a new full or read-only Windows Server 2008-based domain controller.

-   [Troubleshoot FRS and DFS - Windows Server](/en-us/troubleshoot/windows-server/networking/troubleshoot-file-replication-service-ditributed-file-system?source=recommendations)

    Describes how to troubleshoot the File Replication Service and the Distributed File System

-   [Troubleshoot domain controller deployment - Windows Server](/en-us/troubleshoot/windows-server/active-directory/troubleshoot-domain-controller-deployment?source=recommendations)

    Provides information about troubleshooting domain controller deployment.

-   [Distributed File System Replication (DFSR) SYSVOL fails to migrate or replicate - Windows Server](/en-us/troubleshoot/windows-server/group-policy/dfsr-sysvol-fails-migrate-replicate?source=recommendations)

    Provides a solution to issues where DFSR SYSVOL fails to migrate or replicate, or SYSVOL isn\'t shared.

Training

Module

[Implement Windows Server DNS - Training](/en-us/training/modules/implement-windows-server-dns/?source=recommendations)

Learn how to deploy and configure DNS in Windows Server, including DNS architecture, forward and reverse lookup zones, AD-integrated zones, zone transfers, forwarders, conditional forwarding, and stub zones.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
