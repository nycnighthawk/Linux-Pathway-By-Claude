---
{"title": "Appendix A: Reviewing Key AD DS Terms", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-a--reviewing-key-ad-ds-terms", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Appendix A: Reviewing Key AD DS Terms

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

The following terms are relevant to the deployment process for Windows Server 2008 Active Directory Domain Services (AD DS).

[](#active-directory-domain)

## Active Directory domain {#active-directory-domain .heading-anchor}

An administrative unit in a computer network that, for management convenience, groups several capabilities, including the following:

-   **Network-wide user identity**. In domains, user identities can be created once and then referenced on any computer that is joined to the forest in which the domain is located. Domain controllers that make up a domain store user accounts and user credentials, such as passwords or certificates, securely.

-   **Authentication**. Domain controllers provide authentication services for users. They also supply additional authorization data, such as user group memberships. Administrators can use these services to control access to resources on the network.

-   **Trust relationships**. Domains extend authentication services to users in other domains in their own forest by means of automatic bidirectional trusts. Domains also extend authentication services to users in domains in other forests by means of either forest trusts or manually created external trusts.

-   **Policy administration**. A domain is a scope of administrative policies, such as password complexity and password reuse rules.

-   **Replication**. A domain defines a partition of the directory tree that provides data that is adequate to provide required services and that is replicated between domain controllers. In this way, all domain controllers are peers in a domain, and they are managed as a unit.

[](#active-directory-forest)

## Active Directory forest {#active-directory-forest .heading-anchor}

A collection of one or more Active Directory domains that share a common logical structure, directory schema, and network configuration, as well as automatic, two-way, transitive trust relationships. Each forest is a single instance of the directory, and it defines a security boundary.

[](#active-directory-functional-level)

## Active Directory functional level {#active-directory-functional-level .heading-anchor}

An AD DS setting that enables advanced domain-wide or forest-wide AD DS features.

[](#migration)

## Migration {#migration .heading-anchor}

The process of moving an object from a source domain to a target domain, while preserving or modifying characteristics of the object to make it accessible in the new domain.

[](#domain-restructure)

## Domain restructure {#domain-restructure .heading-anchor}

A migration process that involves changing the domain structure of a forest. A domain restructure can involve either the consolidation or the addition of domains, and it can take place between forests or within a forest.

[](#domain-consolidation)

## Domain consolidation {#domain-consolidation .heading-anchor}

A restructuring process that involves eliminating AD DS domains by merging their contents with the contents of other domains.

[](#domain-upgrade)

## Domain upgrade {#domain-upgrade .heading-anchor}

The process of upgrading the directory service of a domain to a later version of the directory service. This includes upgrading the operating system on all domain controllers and raising the AD DS functional level where applicable.

[](#in-place-domain-upgrade)

## In-place domain upgrade {#in-place-domain-upgrade .heading-anchor}

The process of upgrading the operating systems of all domain controllers in a given domain, for example, upgrading Windows Server 2003 to Windows Server 2008 , and raising the functional level of the domain, if applicable, while leaving domain objects, such as users and groups, in place.

[](#forest-root-domain)

## Forest root domain {#forest-root-domain .heading-anchor}

The first domain that is created in the Active Directory forest. This domain is automatically designated as the forest root domain. It provides the foundation for the Active Directory forest infrastructure.

[](#regional-domain)

## Regional domain {#regional-domain .heading-anchor}

A child domain that is created in a geographic region to optimize replication traffic.

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

-    Last updated on 05/12/2025
