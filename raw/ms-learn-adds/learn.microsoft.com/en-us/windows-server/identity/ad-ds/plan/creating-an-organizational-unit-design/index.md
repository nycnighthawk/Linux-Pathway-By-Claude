---
{"title": "Creating an Organizational Unit Design", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/creating-an-organizational-unit-design", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Creating an Organizational Unit Design

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Forest owners are responsible for creating organizational unit (OU) designs for their domains. Creating an OU design involves designing the OU structure, assigning the OU owner role, and creating account and resource OUs.

Initially, design your OU structure to enable delegation of administration. When the OU design is complete, you can create additional OU structures for the application of Group Policy to the users and computers and to limit the visibility of objects. For more information, see [Designing a Group Policy Infrastructure](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc786524(v=ws.10)).

[](#ou-owner-role)

## OU owner role {#ou-owner-role .heading-anchor}

The forest owner designates an OU owner for each OU that you design for the domain. OU owners are data managers who control a subtree of objects in Active Directory Domain Services (AD DS). OU owners can control how administration is delegated and how policy is applied to objects within their OU. They can also create new subtrees and delegate administration of OUs within those subtrees.

Because OU owners do not own or control the operation of the directory service, you can separate ownership and administration of the directory service from ownership and administration of objects, reducing the number of service administrators who have high levels of access.

OUs provide administrative autonomy and the means to control visibility of objects in the directory. OUs provide isolation from other data administrators, but they do not provide isolation from service administrators. Although OU owners have control over a subtree of objects, the forest owner retains full control over all subtrees. This enables the forest owner to correct mistakes, such as an error in an access control list (ACL), and to reclaim delegated subtrees when data administrators are terminated.

[](#account-ous-and-resource-ous)

## Account OUs and resource OUs {#account-ous-and-resource-ous .heading-anchor}

Account OUs contain user, group, and computer objects. Forest owners must create an OU structure to manage these objects and then delegate control of the structure to the OU owner. If you are deploying a new AD DS domain, create an account OU for the domain so that you can delegate control of the accounts in the domain.

Resource OUs contain resources and the accounts that are responsible for managing those resources. The forest owner is also responsible for creating an OU structure to manage these resources and for delegating control of that structure to the OU owner. Create resource OUs as needed based on the requirements of each group within your organization for autonomy in the management of data and equipment.

[](#documenting-the-ou-design-for-each-domain)

## Documenting the OU design for each domain {#documenting-the-ou-design-for-each-domain .heading-anchor}

Assemble a team to design the OU structure that you use to delegate control over resources within the forest. The forest owner might be involved in the design process and must approve the OU design. You might also involve at least one service administrator to ensure that the design is valid. Other design team participants might include the data administrators who will work on the OUs and the OU owners who will be responsible for managing them.

It is important to document your OU design. List the names of the OUs that you plan to create. And, for each OU, document the type of OU, the OU owner, the parent OU (if applicable), and the origin of that OU.

For a worksheet to assist you in documenting your OU design, download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip from [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608) and open \"Identifying OUs for Each Domain\" (DSSLOGI_9.doc).

[](#in-this-section)

## In this section {#in-this-section .heading-anchor}

-   [Reviewing OU Design Concepts](reviewing-ou-design-concepts)

-   [Delegating Administration by Using OU Objects](delegating-administration-by-using-ou-objects)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Reviewing OU Design Concepts](/en-us/windows-server/identity/ad-ds/plan/reviewing-ou-design-concepts?source=recommendations)

    Learn more about: Reviewing OU Design Concepts

-   [Understanding the Active Directory Logical Model](/en-us/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model?source=recommendations)

    Learn more about: Understanding the Active Directory Logical Model

-   [Finding Additional Resources for Logical Structure Design](/en-us/windows-server/identity/ad-ds/plan/finding-additional-resources-for-logical-structure-design?source=recommendations)

    Learn more about: Finding Additional Resources for Logical Structure Design

-   [Appendix A - Reviewing Key AD DS Terms](/en-us/windows-server/identity/ad-ds/plan/appendix-a--reviewing-key-ad-ds-terms?source=recommendations)

    Learn more about: Appendix A: Reviewing Key AD DS Terms

-   [Using the Organizational Domain Forest Model](/en-us/windows-server/identity/ad-ds/plan/using-the-organizational-domain-forest-model?source=recommendations)

    Learn more about: Using the Organizational Domain Forest Model

-   [Reviewing the Domain Models](/en-us/windows-server/identity/ad-ds/plan/reviewing-the-domain-models?source=recommendations)

    Learn more about: Reviewing the Domain Models

-   [Install Active Directory Domain Services on Windows Server](/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-?source=recommendations)

    Learn more about how to install Active Directory Domain Services in Windows Server using PowerShell, or Server Manager.

-   [Delegating Administration of Account OUs and Resource OUs](/en-us/windows-server/identity/ad-ds/plan/delegating-administration-of-account-ous-and-resource-ous?source=recommendations)

    Learn more about: Delegating Administration of Account OUs and Resource OUs

Training

Module

[Introduction to AD DS - Training](/en-us/training/modules/introduction-to-ad-ds/?source=recommendations)

Introduction to AD DS

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
