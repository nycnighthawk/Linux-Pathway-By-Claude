---
{"title": "Creating a Site Link Bridge Design", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/creating-a-site-link-bridge-design", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Creating a Site Link Bridge Design

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

A site link bridge connects two or more site links and enables transitivity between site links. Each site link in a bridge must have a site in common with another site link in the bridge. The Knowledge Consistency Checker (KCC) uses the information on each site link to compute the cost of replication between sites in one site link and sites in the other site links of the bridge. Without the presence of a common site between site links, the KCC also cannot establish direct connections between domain controllers in the sites that are connected by the same site link bridge.

By default, all site links are transitive. We recommend that you keep transitivity enabled by not changing the default value of **Bridge all site links** (enabled by default). However, you will need to disable **Bridge all site links** and complete a site link bridge design if:

-   Your IP network is not fully routed. When you disable **Bridge all site links**, all site links are considered nontransitive, and you can create and configure site link bridge objects to model the actual routing behavior of your network.
-   You need to control the replication flow of the changes made in Active Directory Domain Services (AD DS). By disabling **Bridge all site links** for the site link IP transport and configuring a site link bridge, the site link bridge becomes the equivalent of a disjointed network. All site links within the site link bridge can route transitively, but they do not route outside of the site link bridge.

For more information about how to use the Active Directory Sites and Services snap-in to disable the **Bridge all site links** setting, see the article [Enable or disable site link bridges](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc738789(v=ws.10)).

[](#controlling-ad-ds-replication-flow)

## Controlling AD DS replication flow {#controlling-ad-ds-replication-flow .heading-anchor}

Two scenarios in which you need a site link bridge design to control replication flow include controlling replication failover and controlling replication through a firewall.

[](#controlling-replication-failover)

### Controlling replication failover {#controlling-replication-failover .heading-anchor}

If your organization has a hub-and-spoke network topology, you generally do not want the satellite sites to create replication connections to other satellite sites if all domain controllers in the hub site fail. In such scenarios, you must disable **Bridge all site links** and create site link bridges so that replication connections are created between the satellite site and another hub site that is just one or two hops away from the satellite site.

[](#controlling-replication-through-a-firewall)

### Controlling replication through a firewall {#controlling-replication-through-a-firewall .heading-anchor}

If two domain controllers representing the same domain in two different sites are specifically allowed to communicate with each other only through a firewall, you can disable **Bridge all site links** and create site link bridges for sites on the same side of the firewall. Therefore, if your network is separated by firewalls, we recommend that you disable transitivity of site links and create site link bridges for the network on one side of the firewall.

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

-   [Creating a Site Link Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-link-design?source=recommendations)

    Learn more about: Creating a Site Link Design

-   [Creating a Site Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-site-design?source=recommendations)

    Learn more about: Creating a Site Design

-   [Designing the Site Topology](/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology?source=recommendations)

    Learn more about: Designing the Site Topology

-   [Determining the Cost](/en-us/windows-server/identity/ad-ds/plan/determining-the-cost?source=recommendations)

    Learn more about assigning cost values to links

-   [Collecting Network Information](/en-us/windows-server/identity/ad-ds/plan/collecting-network-information?source=recommendations)

    Learn more about: Collecting Network Information

-   [Setting Site Link Properties](/en-us/windows-server/identity/ad-ds/plan/setting-site-link-properties?source=recommendations)

    Learn more about: Setting Site Link Properties

-   [Appendix A - Locations and Subnet Prefixes](/en-us/windows-server/identity/ad-ds/plan/appendix-a--locations-and-subnet-prefixes?source=recommendations)

    Learn more about: Appendix A: Locations and Subnet Prefixes

-   [Site functions](/en-us/windows-server/identity/ad-ds/plan/site-functions?source=recommendations)

    Learn more about various site functions in AD DS

Training

Certification

[Microsoft Certified: Azure Network Engineer Associate - Certifications](/en-us/credentials/certifications/azure-network-engineer-associate/?source=recommendations)

Demonstrate the design, implementation, and maintenance of Azure networking infrastructure, load balancing traffic, network routing, and more.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
