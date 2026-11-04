---
{"title": "AD DS Deployment Requirements", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/ad-ds-deployment-requirements", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# AD DS Deployment Requirements

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

The structure of your existing environment determines your strategy for deploying Windows Server 2008 Active Directory Domain Services (AD DS). If you are creating an AD DS environment and you do not have an existing domain structure, complete your AD DS design before you begin creating your AD DS environment. Then, you can deploy a new forest root domain and deploy the rest of your domain structure according to your design.

Also, as part of your AD DS deployment, you might decide to upgrade and restructure your environment. For example, if your organization has an existing Windows 2000 domain structure, you might perform an in-place upgrade of some domains and restructure others. In addition, you might decide to reduce the complexity of your environment by either restructuring domains between forests or restructuring domains within a forest after you deploy AD DS.

[](#deploying-a-windows-server-2008-forest-root-domain)

## Deploying a Windows Server 2008 forest root domain {#deploying-a-windows-server-2008-forest-root-domain .heading-anchor}

The forest root domain provides the foundation for your AD DS forest infrastructure. To deploy AD DS, you must first deploy a forest root domain. To do this, you must review your AD DS design; configure the DNS service for the forest root domain; create the forest root domain, which consists of deploying forest root domain controllers, configuring the site topology for the forest root domain, and configuring operations master roles (also known as flexible single master operations or FSMO); and raise the forest and domain functional levels. The following illustration shows the overall process of deploying a forest root domain.

For more information, see [Deploying a Windows Server 2008 Forest Root Domain](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731174(v=ws.10)).

[](#deploying-windows-server-2008-regional-domains)

## Deploying Windows Server 2008 regional domains {#deploying-windows-server-2008-regional-domains .heading-anchor}

After you complete the deployment of the forest root domain, you are ready to deploy any new Windows Server 2008 regional domains that are specified by your design. To do this, you must deploy domain controllers for each regional domain. The following illustration shows the process of deploying regional domains.

For more information, see [Deploying Windows Server 2008 Regional Domains](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc755118(v=ws.10)).

[](#upgrading-active-directory-domains-to-windows-server-2008)

## Upgrading Active Directory domains to Windows Server 2008 {#upgrading-active-directory-domains-to-windows-server-2008 .heading-anchor}

Upgrading your Windows 2000 or Windows Server 2003 domains to Windows Server 2008 domains is an efficient, straightforward way to take advantage of additional Windows Server 2008 features and functionality. You can upgrade domains to maintain your current network and domain configuration while improving the security, scalability, and manageability of your network infrastructure. Upgrading from Windows 2000 or Windows Server 2003 to Windows Server 2008 requires minimal network configuration. Upgrading also has little impact on user operations. For more information, see [Upgrading Active Directory Domains to Windows Server 2008 and Windows Server 2008 R2 AD DS Domains](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731188(v=ws.10)).

[](#restructuring-ad-ds-domains)

## Restructuring AD DS domains {#restructuring-ad-ds-domains .heading-anchor}

When you restructure domains between Windows Server 2008 forests (interforest restructure), you can reduce the number of domains in your environment and therefore reduce administrative complexity and overhead. When you migrate objects between forests as part of this restructuring process, both the source domain and target domain environments exist simultaneously. This makes it possible for you to roll back to the source environment during the migration, if necessary.

When you restructure Windows Server 2008 domains within a Windows Server 2008 forest (intraforest restructure), you can consolidate your domain structure and therefore reduce administrative complexity and overhead. When you restructure domains within a forest, the migrated accounts no longer exist in the source domain.

For more information about how to use the Active Directory Migration Tool (ADMT) version 3.1 (ADMT v3.1) to restructure domains, see [ADMT Guide: Migrating and Restructuring Active Directory Domains](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc974332(v=ws.10)).

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
