---
{"title": "Disjoint Namespace", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/disjoint-namespace", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Disjoint Namespace

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

A disjoint namespace occurs when one or more domain member computers have a primary Domain Name Service (DNS) suffix that does not match the DNS name of the Active Directory domain of which the computers are members. For example, a member computer that uses a primary DNS suffix of corp.fabrikam.com in an Active Directory domain named na.corp.fabrikam.com is using a disjoint namespace.

A disjoint namespace is more complex to administer, maintain, and troubleshoot than a contiguous namespace. In a contiguous namespace, the primary DNS suffix matches the Active Directory domain name. Network applications that are written to assume that the Active Directory namespace is identical to the primary DNS suffix for all domain member computers do not function properly in a disjoint namespace.

[](#support-for-disjoint-namespaces)

## Support for disjoint namespaces {#support-for-disjoint-namespaces .heading-anchor}

Domain member computers, including domain controllers, can function in a disjoint namespace. Domain member computers can register their host (A) resource record and IP version 6 (IPv6) host (AAAA) resource record in a disjoint DNS namespace. When domain member computers register their resource records in this way, domain controllers continue to register global and site-specific service (SRV) resource records in the DNS zone that is identical to the Active Directory domain name.

For example, assume that a domain controller for the Active Directory domain named na.corp.fabrikam.com that uses a primary DNS suffix of corp.fabrikam.com registers host (A) and IPv6 host (AAAA) resource records in the corp.fabrikam.com DNS zone. The domain controller continues to register global and site-specific service (SRV) resource records in the \_msdcs.na.corp.fabrikam.com and na.corp.fabrikam.com DNS zones, which makes service location possible.

Important

Although Windows operating systems may support a disjoint namespace, applications that are written to assume that the primary DNS suffix is the same as the Active Directory domain suffix may not function in such an environment. For this reason, you should test all applications and their respective operating systems carefully before you deploy a disjoint namespace.

A disjoint namespace should work (and is supported) in the following situations:

-   When a forest with multiple Active Directory domains uses a single DNS namespace, which is also known as a DNS zone

    An example of this is a company that uses regional domains with names such as na.corp.fabrikam.com, sa.corp.fabrikam.com, and asia.corp.fabrikam.com and uses a single DNS namespace, such as corp.fabrikam.com.

-   When a single Active Directory domain is split into separate DNS namespaces

    An example of this is a company with an Active Directory domain of corp.contoso.com that uses DNS zones such as hr.corp.contoso.com, production.corp.contoso.com, and it.corp.contoso.com.

A disjoint namespace does not work properly (and is not supported) in the following situations:

-   A disjoint suffix used by domain members matches an Active Directory domain name in this or another forest. This breaks Kerberos name-suffix routing.

-   The same disjoint suffix is used in another forest. This prevents routing these suffixes uniquely between forests.

-   When a domain member certification authority (CA) server changes its fully qualified domain name (FQDN) so that it no longer use the same primary DNS suffix that is used by the domain controllers of the domain to which the CA server is a member. In this case, you may have problems validating certificates the CA server issued, depending on what DNS names are used in the CRL Distribution Points. But if you place a CA server in a stable disjoint namespace, it works properly and is supported.

[](#considerations-for-disjoint-namespaces)

## Considerations for disjoint namespaces {#considerations-for-disjoint-namespaces .heading-anchor}

The following considerations may help you decide if you should use a disjoint namespace.

[](#application-compatibility)

### Application compatibility {#application-compatibility .heading-anchor}

As previously mentioned, a disjoint namespace can cause problems for any applications and services that are written to assume that a computer primary DNS suffix is identical to the name of the domain name of which it is a member. Before you deploy a disjoint namespace, you must check applications for compatibility issues. Also, be sure to check the compatibility of all applications that you use when you perform your analysis. This includes applications from Microsoft and from other software developers.

[](#advantages-of-disjoint-namespaces)

### Advantages of disjoint namespaces {#advantages-of-disjoint-namespaces .heading-anchor}

Using a disjoint namespace can have the following advantages:

-   Because the primary DNS suffix of a computer can indicate different information, you can manage the DNS namespace separately from the Active Directory domain name.

-   You can separate the DNS namespace based on business structure or geographical location. For example, you can separate the namespace based on business unit names or physical location such as continent, country/region, or building.

[](#disadvantages-of-disjoint-namespaces)

### Disadvantages of disjoint namespaces {#disadvantages-of-disjoint-namespaces .heading-anchor}

Using a disjoint namespace can have the following disadvantages:

-   You must create and manage separate DNS zones for each Active Directory domain in the forest that has member computers that use a disjoint namespace. (That is, it requires an additional and more complex configuration.)

-   You must perform manual steps to modify and manage the Active Directory attribute that allows domain members to use specified, primary DNS suffixes.

-   To optimize name resolution, you must perform manual steps to modify and maintain Group Policy to configure member computers with alternate primary DNS suffixes.

Note

The Windows Internet Name Service (WINS) could be used to offset this disadvantage by resolving single-label names. For more information about WINS, see the [WINS Technical Reference](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc736411(v=ws.10)).

-   When your environment requires multiple primary DNS suffixes, you must configure the DNS suffix search order for all of the Active Directory domains in the forest appropriately.

    To set the DNS suffix search order, you can use Group Policy objects or Dynamic Host Configuration Protocol (DHCP) Server service parameters. You can also modify the registry.

-   You must carefully test all applications for compatibility issues.

For more information about steps that you can take to address these disadvantages, see [Create a Disjoint Namespace](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755926(v=ws.10)).

[](#planning-a-namespace-transition)

### Planning a namespace transition {#planning-a-namespace-transition .heading-anchor}

Before you modify a namespace, review the following considerations, which apply to transitions from contiguous namespaces to disjoint namespaces (or the reverse):

-   Manually configured Service Principal Names (SPNs) may no longer match DNS names after a namespace change. This can cause authentication failures.

    For more information, see [Service Logons Fail Due to Incorrectly Set SPNs](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc772897(v=ws.10)).

    -   If you use Windows Server 2003-based computers with constrained delegation, those computers may require you to manually edit the **msDS-AllowedToDelegateTo** attribute in Active Directory. For more information, see the [ms-DS-Allowed-To-Delegate-To attribute](/en-us/windows/win32/adschema/a-msds-allowedtodelegateto).

    -   If you want to delegate permissions to modify SPNs to subordinate administrators, see [Delegating Authority to Modify SPNs](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770439(v=ws.10)).

-   If you use Lightweight Directory Access Protocol (LDAP) over Secure Sockets Layer (SSL) (known as LDAPS) with a CA in a deployment that has domain controllers that are configured in a disjoint namespace, you must use the appropriate Active Directory domain name and primary DNS suffix when you configure the LDAPS certificates.

    For more information about domain controller certificate requirements, see article 321051 in the Microsoft Knowledge Base, [How to enable LDAP over SSL with a third-party certification authority](https://support.microsoft.com/help/321051/).

    Note

    Domain controllers that use certificates for LDAPS may require you to redeploy their certificates. When you do so, domain controllers may not select an appropriate certificate until they are restarted. For more information about Lightweight Directory Access Protocol (LDAP) over Secure Sockets Layer (SSL) (LDAPS) authentication for Windows Server 2003, see article 938703 in the Microsoft Knowledge Base, [How to troubleshoot LDAP over SSL connection problems](https://support.microsoft.com/help/938703/).

[](#planning-for-disjoint-namespace-deployments)

### Planning for disjoint namespace deployments {#planning-for-disjoint-namespace-deployments .heading-anchor}

Take the following precautions if you deploy computers in an environment that has a disjoint namespace:

1.  Notify all software vendors with whom you do business that they must test and support a disjoint namespace. Ask them to verify that they support their applications in environments that use disjoint namespaces.

2.  Test all versions of operating systems and applications in disjoint namespace lab environments. When you do, follow these recommendations:

    1.  Resolve all software issues before you deploy the software into your environment.

    2.  When possible, participate in beta tests of operating systems and applications that you plan to deploy in disjoint namespaces.

3.  Ensure that administrators and helpdesk staff are aware of the disjoint namespace and its impact.

4.  Create a plan that makes it possible for you to transition from a disjoint namespace to a contiguous namespace, if necessary.

5.  Evangelize the importance of disjoint namespace support with operating system and application providers.

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Active Directory-Integrated DNS Zones](/en-us/windows-server/identity/ad-ds/plan/active-directory-integrated-dns-zones?source=recommendations)

    Learn more about: Active Directory-Integrated DNS Zones

-   [Integrating AD DS into an Existing DNS Infrastructure](/en-us/windows-server/identity/ad-ds/plan/integrating-ad-ds-into-an-existing-dns-infrastructure?source=recommendations)

    Learn more about: Integrating AD DS into an Existing DNS Infrastructure

-   [Domain Controller Location](/en-us/windows-server/identity/ad-ds/plan/domain-controller-location?source=recommendations)

    Learn more about: Domain Controller Location

-   [DNS for AD DS Owner Role](/en-us/windows-server/identity/ad-ds/deploy/assigning-the-dns-for-ad-ds-owner-role?source=recommendations)

    Information about the DNS for AD DS Owner role.

-   [DNS and AD DS](/en-us/windows-server/identity/ad-ds/plan/dns-and-ad-ds?source=recommendations)

    Learn more about: DNS and AD DS

-   [Reviewing DNS Concepts](/en-us/windows-server/identity/ad-ds/plan/reviewing-dns-concepts?source=recommendations)

    Learn more about: Reviewing DNS Concepts

Training

Module

[Secure Windows Server DNS - Training](/en-us/training/modules/secure-windows-server-domain-name-system/?source=recommendations)

Learn how to secure Windows Server DNS using split-horizon DNS, DNS policies for traffic management and geo-location routing, DNS cache locking, DNS socket pool, and DNSSEC for cryptographic zone signing.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
