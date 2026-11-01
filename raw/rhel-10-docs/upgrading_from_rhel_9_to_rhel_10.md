---
{"title": "Upgrading from RHEL 9 to RHEL 10", "guide": "upgrading_from_rhel_9_to_rhel_10", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/upgrading_from_rhel_9_to_rhel_10/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Upgrading from RHEL 9 to RHEL 10 {#upgrading-from-rhel-9-to-rhel-10 .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Instructions for an in-place upgrade from Red Hat Enterprise Linux 9 to Red Hat Enterprise Linux 10 {#instructions-for-an-in-place-upgrade-from-red-hat-enterprise-linux-9-to-red-hat-enterprise-linux-10 .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140084711943584)

**Abstract**

The RHEL in-place upgrade uses the Leapp utility to perform an upgrade from Red Hat Enterprise Linux 9 to Red Hat Enterprise Linux 10. During the in-place upgrade, the existing RHEL 9 operating system is replaced by a RHEL 10 version.

------------------------------------------------------------------------

## [Providing feedback on Red Hat documentation](#providing-feedback-on-red-hat-documentation) {#providing-feedback-on-red-hat-documentation .title}

We are committed to providing high-quality documentation and value your feedback. To help us improve, you can submit suggestions or report errors through the Red Hat Jira tracking system.

**Procedure**

1.  Log in to the [Jira](https://redhat.atlassian.net/jira/software/c/projects/RHELDOCS/issues/) website.

    If you do not have an account, select the option to create one.

2.  Click **Create** in the top navigation bar.

3.  Enter a descriptive title in the **Summary** field.

4.  Enter your suggestion for improvement in the **Description** field. Include links to the relevant parts of the documentation.

5.  Click **Create** at the bottom of the window.

## [Key migration terminology](#key-migration-terminology) {#key-migration-terminology .title}

While the following migration terms are commonly used in the software industry, these definitions are specific to Red Hat Enterprise Linux (RHEL).

**Update**

Sometimes called a software patch, an update is an addition to the current version of the application, operating system, or software that you are running. A software update addresses any issues or bugs to provide a better experience of working with the technology. In RHEL, an update relates to a minor release, for example, updating from RHEL 8.1 to 8.2.

**Upgrade**

An upgrade is when you replace the application, operating system, or software that you are currently running with a newer version. Typically, you first back up your data according to instructions from Red Hat. When you upgrade RHEL, you have two options:

-   **In-place upgrade:** During an in-place upgrade, you replace the earlier version with the new version without removing the earlier version first. The installed applications and utilities, along with the configurations and preferences, are incorporated into the new version.
-   **Clean install:** A clean install removes all traces of the previously installed operating system, system data, configurations, and applications and installs the latest version of the operating system. A clean install is ideal if you do not need any of the previous data or applications on your systems or if you are developing a new project that does not rely on prior builds.

**Operating system conversion**

A conversion is when you convert your operating system from a different Linux distribution to Red Hat Enterprise Linux. Typically, you first back up your data according to instructions from Red Hat.

**Migration**

Typically, a migration indicates a change of platform: software or hardware. Moving from Windows to Linux is a migration. Moving a user from one laptop to another or a company from one server to another is a migration. However, most migrations also involve upgrades, and sometimes the terms are used interchangeably.

-   **Migration to RHEL:** Conversion of an existing operating system to RHEL
-   **Migration across RHEL:** Upgrade from one version of RHEL to another

## [Chapter 1. Supported upgrade paths](#supported-upgrade-paths) {#chapter-1.-supported-upgrade-paths .title}

The in-place upgrade replaces the RHEL 9 operating system on your system with a RHEL 10 version.

Important

You can perform the in-place upgrade only from one major RHEL version to the next consecutive one, for example, RHEL 8 to RHEL 9 or RHEL 9 to RHEL 10. If you want to upgrade a system across multiple versions, such as from RHEL 8 to RHEL 10, you must perform multiple in-place upgrades to reach your target version.

Currently, you can perform an in-place upgrade from the following source RHEL 9 minor versions to the following target RHEL 10 minor versions:

+-------------------------+-----------------------+------------------------+
| System configuration    | Source OS version     | Target OS version      |
+:========================+:======================+:=======================+
| RHEL                    | RHEL 9.6 (EUS)        | RHEL 10.0 (EUS)        |
+-------------------------+-----------------------+------------------------+
|                         | RHEL 9.8              | RHEL 10.2              |
+-------------------------+-----------------------+------------------------+
| RHEL with SAP NetWeaver | RHEL 9.6 (E4S or EUS) | RHEL 10.0 (E4S or EUS) |
+-------------------------+-----------------------+------------------------+
|                         | RHEL 9.8 (E4S or EUS) | RHEL 10.2 (E4S or EUS) |
+-------------------------+-----------------------+------------------------+
| RHEL with SAP HANA      | RHEL 9.6 (E4S)        | RHEL 10.0 (E4S)        |
+-------------------------+-----------------------+------------------------+

: Table 1.1. Supported upgrade paths

Show more

Important

In-place upgrade paths in this table are guaranteed only for systems that use Red Hat Subscription Manager (RHSM). For Pay-As-You-Go (PAYG) RHEL systems that use Red Hat Update Infrastructure (RHUI), only the latest available upgrade path is supported. Note that this does not impact RHEL systems with SAP HANA installed.

**Additional resources**

-   [Supported in-place upgrade paths for Red Hat Enterprise Linux](https://access.redhat.com/articles/4263361)
-   [In-place upgrade Support Policy](https://access.redhat.com/support/policy/ipu-support)
-   [In-place upgrades over multiple RHEL major versions by using Leapp](https://access.redhat.com/articles/7115868)

## [Chapter 2. Planning an upgrade to RHEL 10](#planning-an-upgrade-to-rhel-10) {#chapter-2.-planning-an-upgrade-to-rhel-10 .title}

In-place upgrades allow you to upgrade to the latest version of RHEL without losing existing configurations and system subscriptions.

In general, in-place upgrades are less time-consuming and costly than a fresh install of RHEL. However, not all systems are eligible for an in-place upgrade. Before beginning your upgrade from RHEL 9 to RHEL 10, review system requirements, limitations, and other considerations.

### [2.1. Planning an upgrade from RHEL 9 to RHEL 10](#planning-an-upgrade-from-rhel-9-to-rhel-10) {#planning-an-upgrade-from-rhel-9-to-rhel-10 .title}

An in-place upgrade is the recommended and supported method for upgrading your system to the next major version of RHEL.

Consider the following before upgrading to RHEL 10:

-   **Ansible** - You can automate parts of the in-place upgrade process by using Ansible roles. Ansible roles allow you to quickly and efficiently upgrade large numbers of systems. For more information, see [Upgrading large deployments by using Ansible roles](#upgrading-large-deployments-by-using-ansible-roles "Chapter 5. Upgrading large deployments by using Ansible roles").

-   **Applications** - You can migrate applications installed on your system by using the `Leapp`{.literal} utility. However, in certain cases, you have to create custom actors, which specify actions to be performed by `Leapp`{.literal} during the upgrade, for example, reconfiguring an application or installing a specific hardware driver. For more information, see [Handling the migration of your custom and third-party applications](https://access.redhat.com/articles/4977891#actors). Note that custom actors are unsupported by Red Hat.

    Important

    The SHA-1 algorithm has been deprecated in RHEL 9. If your system contains any packages with RSA/SHA-1 signatures, the upgrade is inhibited. Before upgrading, either remove these packages or contact the vendor for packages with RSA/SHA-256 signatures. For more information, see [SHA-1 deprecation in Red Hat Enterprise Linux 9](https://access.redhat.com/articles/6846411).

-   **Boot loader** - You cannot switch the boot loader from BIOS to UEFI on RHEL 9 or RHEL 10. If your RHEL 9 system uses BIOS and you want your RHEL 10 system to use UEFI, perform a fresh install of RHEL 9 instead of an in-place upgrade. For more information, see [Is it possible to switch the BIOS boot to UEFI boot on preinstalled Red Hat Enterprise Linux machine?](https://access.redhat.com/solutions/1990803)

-   **Customization** - To use custom repositories, see the [Configuring custom repositories](https://access.redhat.com/articles/4977891#repos-config) Knowledgebase article.

-   **Downtime** - The upgrade process can take from several minutes to several hours.

-   **High Availability** - If you are using the High Availability add-on, follow the [Recommended Practices for Applying Software Updates to a RHEL High Availability or Resilient Storage Cluster](https://access.redhat.com/articles/2059253) Knowledgebase article.

-   **Language** - All `Leapp`{.literal} reports, logs, and other generated documentation are in English, regardless of the language configuration.

-   **Operating system** - The operating system is upgradable by the `Leapp`{.literal} utility under the following conditions:

    -   The source OS version is installed on a system with one of the following supported architectures:

        -   AMD and Intel 64-bit architectures (x86-64-v3)

        -   64-bit ARM architecture (ARMv8.0-A)

            Important

            For the 64-bit ARM architecture, in-place upgrades are supported only on systems running the `4k`{.literal} page size kernel. The Leapp utility does not support in-place upgrades if the system is booted with the `64k`{.literal} page size kernel.

        -   IBM Power Systems, Little Endian (POWER9)

        -   64-bit IBM Z (IBM z14 or IBM LinuxONE II or later)

            For more information, see [Red Hat certified hardware](https://catalog.redhat.com/hardware).

    -   Minimum [hardware requirements](https://access.redhat.com/articles/rhel-limits) for RHEL 10 are met.

    -   You have access to up-to-date content for the selected source and target OS versions. See [Preparing a RHEL 9 system for the upgrade](#preparing-a-rhel-9-system-for-the-upgrade "3.1. Preparing a RHEL 9 system for the upgrade") for more information.

-   **Public clouds**

    -   **Pay-As-You-Go**

        -   **RHUI** - The in-place upgrade is supported for on-demand Pay-As-You-Go (PAYG) instances that use Red Hat Update Infrastructure (RHUI) on Amazon Web Services (AWS) on all supported architectures, and on Microsoft Azure and Google Cloud only on the Intel architecture. For all supported clouds and architectures with PAYG using RHUI but not SAP HANA, only the latest upgrade path is supported.

        -   **CDN** - The in-place upgrade is supported for on-demand Pay-As-You-Go (PAYG) instances that use Red Hat Content Delivery Network (CDN).

            Note

            You can verify that your RHEL cloud instance consumes RHEL content from CDN by confirming that you have the `redhat-cloud-client-configuration-cdn`{.literal} package installed. If it is not installed, then you are consuming the content from RHUI.

    -   **Bring Your Own Subscription** - The in-place upgrade is supported for Bring Your Own Subscription instances on all public clouds that use RHSM for a RHEL subscription.

-   **Real Time for Network Functions Virtualization (NFV) in Red Hat OpenStack Platform** - Upgrades on real-time systems are supported.

-   **RHEL for Real Time** - Upgrades on real-time systems are supported.

-   **SAP HANA** - If you are using SAP HANA, follow the [Upgrading SAP environments from RHEL 9 to RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/10/html/upgrading_sap_environments_from_rhel_9_to_rhel_10/index) guide instead. Note that the upgrade path for RHEL with SAP HANA might differ.

-   **Satellite**

    -   **Client** - If you manage your hosts through Satellite, you can upgrade multiple hosts simultaneously from RHEL 9 to RHEL 10 using the Satellite web UI. For more information, see [Upgrading Hosts to Next Major Red Hat Enterprise Linux Release](https://docs.redhat.com/en/documentation/red_hat_satellite/6.12/html/managing_hosts/upgrading_hosts_to_next_major_rhel_release_managing-hosts).
    -   **Server and Capsule** - You can upgrade Satellite Servers and Capsules starting in Satellite 6.16. For more information, see [Upgrading Satellite or Capsule to RHEL 9 in-place by using Leapp](https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/upgrading_connected_red_hat_satellite_to_6.16/index#upgrading-satellite-or-capsule-in-place-using-leapp_upgrading-connected).

-   **Security** - Evaluate this aspect before the upgrade and take additional steps when the upgrade process completes. Consider especially the following:

    -   Before the upgrade, define the security standard your system has to comply with and understand the [security changes in RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/considerations_in_adopting_rhel_10/security).
    -   During the upgrade process, the `Leapp`{.literal} utility sets SELinux mode to permissive.
    -   `Leapp`{.literal} supports in-place upgrades of RHEL 9.6 and later systems in Federal Information Processing Standard (FIPS) 140 mode to RHEL 10 FIPS-mode-enabled systems. **FIPS mode** stays enabled throughout the complete upgrade process.
    -   After the upgrade is finished, re-evaluate and re-apply your security policies. For information about applying and updating security policies, see [Applying security policies](#applying-security-policies "Chapter 8. Applying security policies").

-   **Storage and file systems**

    -   **Backup** - You should always back up your system before upgrading. For example, you can use the [Relax-and-Recover (ReaR) utility](https://access.redhat.com/solutions/2115051), [LVM snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_and_managing_logical_volumes/index), [RAID splitting](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/configuring-raid-logical-volumes_configuring-and-managing-logical-volumes#splitting-and-merging-a-raid-image_configuring-raid-logical-volumes), or a virtual machine snapshot.

        Note

        File systems formats are intact. As a consequence, file systems have the same limitations as when they were originally created.

    -   **Encryption** - Systems with encrypted storage can be upgraded if the storage uses the LUKS2 format configured with the Clevis TPM 2.0 token. For more information, see [Configuring manual enrollment of LUKS-encrypted volumes by using a TPM 2.0 policy](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-by-using-policy-based-decryption#configuring-manual-enrollment-of-luks-encrypted-volumes-by-using-a-tpm2-policy).

Notable known limitations of the `Leapp`{.literal} utility include:

-   **Known limitations** - Notable known limitations of `Leapp`{.literal} currently include:

    -   Network based multipath and network storage that use Ethernet or Infiniband are not supported for the upgrade. This includes SAN using FCoE and booting from SAN using FC. Note that SAN using FC is supported.
    -   The in-place upgrade is not supported for systems with Ansible Automation Platform installed. To use a RHEL 9 Ansible Automation Platform installation on RHEL 10, see the Red Hat Knowledgebase solution [How do I migrate my Ansible Automation Platform installation from one environment to another?](https://access.redhat.com/solutions/5994961).
    -   Red Hat JBoss Enterprise Application Platform (EAP) is not supported for the upgrade to RHEL 10. You must manually install and configure JBoss EAP on your system after the upgrade.
    -   The Stratis filesystem is not supported for the upgrade.

You can use **[Red Hat Lightspeed](https://console.redhat.com/lightspeed/dashboard)** to determine which of the systems you have registered to Red Hat Lightspeed is on a supported upgrade path to RHEL 10. Note that the Advisor recommendation considers only the RHEL 9 minor version and does not perform a pre-upgrade assessment of the system. See also [Advisor-service recommendations overview](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/assessing_rhel_configuration_issues_by_using_the_red_hat_lightspeed_advisor_service/adv-assess-recommendations).

**Additional resources**

-   [What are RHEL in-place upgrades?](https://www.redhat.com/en/blog/what-are-rhel-place-upgrades)
-   [The best practices and recommendations for performing RHEL Upgrade using Leapp](https://access.redhat.com/articles/7012979)
-   [Leapp upgrade FAQ (Frequently Asked Questions)](https://access.redhat.com/articles/7013172)

## [Chapter 3. Preparing for the upgrade](#preparing-for-the-upgrade) {#chapter-3.-preparing-for-the-upgrade .title}

To prevent issues after the upgrade and to ensure that your system is ready to be upgraded to the next major version of RHEL, complete all necessary preparation steps before upgrading.

### [3.1. Preparing a RHEL 9 system for the upgrade](#preparing-a-rhel-9-system-for-the-upgrade) {#preparing-a-rhel-9-system-for-the-upgrade .title}

Before the in-place upgrade to RHEL 10, you must install upgrade-related files and prepare the system for the upgrade. Skipping these required steps could cause serious issues during the upgrade.

If you do not plan to use Red Hat Subscription Manager (RHSM) during the upgrade process, follow instructions in [Performing an in-place upgrade without Red Hat Subscription Manager](https://access.redhat.com/articles/4977891#upgrade-without-rhsm).

**Prerequisites**

-   The system meets conditions listed in [Planning an upgrade](#planning-an-upgrade-to-rhel-10 "Chapter 2. Planning an upgrade to RHEL 10").
-   If the system has been previously upgraded from RHEL 8 to RHEL 9, ensure that all required post-upgrade steps have been completed. For more information, see [Performing post-upgrade tasks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/upgrading_from_rhel_8_to_rhel_9/index#performing-post-upgrade-tasks-on-the-rhel-9-system_upgrading-from-rhel-8-to-rhel-9) in the Upgrading from RHEL 8 to RHEL 9 guide.
-   Optional: You have reviewed the best practices in [The best practices and recommendations for performing RHEL Upgrade using Leapp](https://access.redhat.com/articles/7012979) Knowledgebase article.
-   You have ensured that your system has been successfully registered to the Red Hat Content Delivery Network (CDN) or Red Hat Satellite by using RHSM.
-   Satellite-registered systems only: You have completed the steps in [Preparing a Satellite system for the upgrade](#preparing-a-satellite-registered-system-for-the-upgrade "3.2. Preparing a Satellite-registered system for the upgrade") to ensure that your system meets the requirements for the upgrade.

**Procedure**

1.  Optional: Unmount non-system OS file systems that are not required for the upgrade and comment them out from the `/etc/fstab`{.literal} file. For example, this includes file systems containing only data files unrelated to the system itself. This can reduce the amount of time needed for the upgrade process and prevent potential issues related to third-party applications that are not migrated properly during the upgrade by custom or third-party actors.

2.  Ensure you have appropriate repositories enabled. The following command enables the Base and AppStream repositories for the 64-bit Intel and AMD architectures; for other architectures, see [RHEL 9 repositories](#appendix-rhel-9-repositories "Appendix A. RHEL 9 repositories").

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable rhel-9-for-x86_64-baseos-rpms --enable rhel-9-for-x86_64-appstream-rpms
    ```

    Note

    Optional: Enable the CodeReady Linux Builder (also known as Optional) or Supplementary repositories. For more information about the content of these repositories, see the [Package manifest](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/package_manifest).

3.  Set the system release version to the source OS version, for example:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager release --set <source_os_version>
    ```

    Replace *\<source_os_version\>* with the source OS version, for example `9.6`{.literal}.

4.  If you are upgrading by using Red Hat Update Infrastructure (RHUI) on a public cloud, set the expected system release version manually:

    ``` {.language-plaintext tabindex="-1"}
    # rhui-set-release --set <source_os_version>
    ```

    Important

    If the `rhui-set-release`{.literal} command is not available on your system, you can set the expected system release version by updating the `/etc/dnf/vars/release`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # echo "<source_os_version>" > /etc/dnf/vars/releasever
    ```

5.  If you use the `dnf versionlock`{.literal} plugin to lock packages to a specific version, clear the lock by running:

    ``` {.language-plaintext tabindex="-1"}
    # dnf versionlock clear
    ```

6.  If you are upgrading by using Red Hat Update Infrastructure (RHUI) on a public cloud, enable required RHUI repositories and install required RHUI packages to ensure your system is ready for upgrade:

    a.  For AWS:

        ``` {.language-plaintext tabindex="-1"}
        # dnf config-manager --set-enabled rhui-client-config-server-9
        # dnf -y install leapp-rhui-aws
        ```

    b.  For Microsoft Azure:

        ``` {.language-plaintext tabindex="-1"}
        # dnf config-manager --set-enabled rhui-microsoft-azure-rhel9
        # dnf -y install rhui-azure-rhel8 leapp-rhui-azure
        ```

    c.  For Google Cloud, follow the [Leapp RHUI packages for Google Cloud](https://access.redhat.com/articles/6981918) Knowledgebase article.

7.  Ensure that you have up-to-date `leapp`{.literal} and `leapp-repository`{.literal} packages:

    a.  RHEL 9.6: version `0.19.0`{.literal} of the `leapp`{.literal} package and version `0.22.0`{.literal} of the `leapp-repository`{.literal} package.

    b.  RHEL 9.8: version `0.21.0`{.literal} of the `leapp`{.literal} package and version `0.24.0`{.literal} of the `leapp-repository`{.literal} package.

        The `leapp-repository`{.literal} package contains the `leapp-upgrade-el9toel10`{.literal} RPM package.

        Note

        Disconnected systems only:download the following packages from the [Red Hat Customer Portal](https://access.redhat.com/downloads/content/479/ver=/rhel---9/9.5/x86_64/packages):

        -   `leapp`{.literal}

        -   `leapp-deps`{.literal}

        -   `python3-leapp`{.literal}

        -   `leapp-upgrade-el9toel10`{.literal}

        -   `leapp-upgrade-el9toel10-deps`{.literal}

        -   `leapp-upgrade-el9toel10-fapolicyd`{.literal}

            -   Include only if you installed the `fapolicyd`{.literal} RPM package on your system.

8.  Install the `Leapp`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install leapp-upgrade
    ```

9.  Update all packages so your system is up-to-date before the upgrade and reboot:

    ``` {.language-plaintext tabindex="-1"}
    # dnf update
    # reboot
    ```

10. Optional: Review, remediate, and then remove the `rpmnew`{.literal} and `rpmsave`{.literal} files.

11. If you use a configuration management system, ensure that it does not interfere with the in-place upgrade process:

    -   If your configuration management system has a client-server architecture, such as Puppet, Salt, or Chef, disable the system before running the `leapp preupgrade`{.literal} command. Do not enable the configuration management system until after the upgrade is complete to prevent issues during the upgrade.

    -   If your configuration management system has agentless architecture, do not run the configuration and deployment file. For example, if your system has Ansible, do not run an Ansible playbook during the upgrade.

        Warning

        For information about automating the upgrade process by using configuration management systems, see [Using configuration management systems to automate parts of the Leapp pre-upgrade and upgrade process on Red Hat Enterprise Linux](https://access.redhat.com/articles/6313281).

12. If you are upgrading by using an ISO image, verify that the ISO image contains the target OS version, for example, RHEL 10.0, and is saved to a persistent local mount point to ensure that the `Leapp`{.literal} utility can access the image throughout the upgrade process.

### [3.2. Preparing a Satellite-registered system for the upgrade](#preparing-a-satellite-registered-system-for-the-upgrade) {#preparing-a-satellite-registered-system-for-the-upgrade .title}

Before you can perform an in-place upgrade to RHEL 10 of a system that is registered to Satellite, you must prepare your system. Perform these steps are performed on the Satellite Server.

Important

Users on Satellite systems must complete the preparatory steps described both in this procedure and in [Preparing a RHEL 9 system for the upgrade](#preparing-a-rhel-9-system-for-the-upgrade "3.1. Preparing a RHEL 9 system for the upgrade").

**Prerequisites**

-   You have administrative privileges for the Satellite Server.
-   Satellite is on a version in full or maintenance support. For more information, see [Red Hat Satellite Product Life Cycle](https://access.redhat.com/support/policy/updates/satellite) and [Which RHEL versions and architectures are supported as client systems managed by Red Hat Satellite server?](https://access.redhat.com/solutions/1156723)

**Procedure**

1.  Import a subscription manifest with a RHEL subscription into Satellite Server. For more information, see the Managing Red Hat Subscriptions chapter in the Managing Content Guide for the particular version of [Red Hat Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/).

2.  Enable and synchronize all required RHEL 9 and RHEL 10 repositories on the Satellite Server with the latest updates for the source and target OS versions. Required repositories must be available in the content view and enabled in the associated activation key.

    Note

    For RHEL 10 repositories, enable the target OS minor version, for example, RHEL 10.0, of each repository. If you enable only the RHEL 10 version of the repositories, the in-place upgrade is inhibited.

    For example, for the Intel architecture without an Extended Update Support (EUS) subscription, enable at minimum the following repositories:

    -   Red Hat Enterprise Linux 9 for x86_64 - AppStream (RPMs)

        rhel-9-for-x86_64-appstream-rpms

        x86_64 *\<source_os_version\>*

    -   Red Hat Enterprise Linux 9 for x86_64 - BaseOS (RPMs)

        rhel-9-for-x86_64-baseos-rpms

        x86_64 *\<source_os_version\>*

    -   Red Hat Enterprise Linux 10 for x86_64 - AppStream (RPMs)

        rhel-10-for-x86_64-appstream-rpms

        x86_64 *\<target_os_version\>*

    -   Red Hat Enterprise Linux 10 for x86_64 - BaseOS (RPMs)

        rhel-10-for-x86_64-baseos-rpms

        x86_64 *\<target_os_version\>*

        Replace *\<source_os_version\>* and *\<target_os_version\>* with the source OS version and target OS version respectively, for example, 9.6 and 10.0.

        For other architectures, see [RHEL 9 repositories](#appendix-rhel-9-repositories "Appendix A. RHEL 9 repositories") and [RHEL 10 repositories](#appendix-rhel-10-repositories "Appendix B. RHEL 10 repositories").

        For more information, see the *Importing Content* chapter in the *Managing Content Guide* for the particular version of [Red Hat Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/).

3.  Attach the content host to a content view containing the required RHEL 9 and RHEL 10 repositories.

    For more information, see the *Managing Content Views* chapter in the *Managing Content Guide* for the particular version of [Red Hat Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/).

**Verification**

1.  Verify that the correct RHEL 9 and RHEL 10 repositories have been added to the correct content view on Satellite Server.

    a.  In the Satellite web UI, navigate to **Content \> Lifecycle \> Content Views** and click the name of the content view.

    b.  Click the **Repositories** tab and verify that the repositories appear as expected.

        Note

        You can also verify that the repositories have been added to the content view by using the following commands:

        ``` {.language-plaintext tabindex="-1"}
        # hammer repository list --search 'content_label ~ rhel-9' --content-view <content_view_name> --organization <organization> --lifecycle-environment <lifecycle_environment>
        # hammer repository list --search 'content_label ~ rhel-10' --content-view <content_view_name> --organization <organization> --lifecycle-environment <lifecycle_environment>
        ```

        Replace *\<content_view_name\>* with the name of the content view, *\<organization\>* with the organization, and *\<lifecycle_environement*\> with the name of the lifecycle environment..

2.  Verify that the correct RHEL 10 repositories are enabled in the activation key associated with the content view:

    a.  In Satellite web UI navigate to **Content \> Lifecycle \> Activation Keys** and click the name of the activation key.
    b.  Click the **Repository Sets** tab and verify that the statuses of the required repositories are `Enabled`{.literal}.

3.  Verify that all expected RHEL 9 repositories are enabled in the host. For example:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --list-enabled | grep "^Repo ID"
    Repo ID:   rhel-9-for-x86_64-baseos-rpms
    Repo ID:   rhel-9-for-x86_64-appstream-rpms
    ```

### [3.3. Configuring the upgrade from RHEL 9.8 to RHEL 10.2 with LiveMode](#configuring-the-upgrade-with-livemode) {#configuring-the-upgrade-from-rhel-9.8-to-rhel-10.2-with-livemode .title}

LiveMode is an alternative method of preparing and booting to the upgrade environment when upgrading from RHEL 9.8 to RHEL 10.2.

LiveMode uses the standard booting process. The standard booting process can prevent or help diagnose certain problems that occur during the upgrade, such as issues related to the storage initialization.

Note that LiveMode requires approximately 700 MB of additional disk space to create and store the upgrade environment before the reboot.

Important

LiveMode is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

When using LiveMode, you can also configure the upgrade experience beyond the default specifications. This can be useful when troubleshooting during the upgrade process or if you want to view the upgrade's progress by using an SSH connection.

If you are using LiveMode without any modifications to the default settings, you do not need to complete any preparation steps for LiveMode before the upgrade. If you want to change the default specifications, you must create and modify a YAML file.

**Procedure**

1.  If you want to modify LiveMode's default specifications, create a YAML file in the `/etc/leapp/actor_conf.d/`{.literal} file, for example `livemode.yaml`{.literal}.

2.  Enter the LiveMode configuration that you want into the YAML file.

    +---------------------------------------------+-----------------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
    | Configuration field                         | Value type            | Default                                     | Description                                                                                                                              |
    +:============================================+:======================+:============================================+:=========================================================================================================================================+
    | `additional_packages`{.literal}             | `List[str]`{.literal} | `[]`{.literal}                              | Additional packages to be installed into the upgrade image.                                                                              |
    +---------------------------------------------+-----------------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
    | `autostart_upgrade_after_reboot`{.literal}  | `bool`{.literal}      | `True`{.literal}                            | If set to `True`{.literal}, the upgrade starts automatically after the reboot. Otherwise, a manual trigger is required.                  |
    +---------------------------------------------+-----------------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
    | `capture_strace_info_into`{.literal}        | `str`{.literal}       | `''`{.literal}                              | If set to a non-empty string, `leapp`{.literal} is run under `strace`{.literal} and results are stored within the provided file path.    |
    +---------------------------------------------+-----------------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
    | `dracut_network`{.literal}                  | `str`{.literal}       | `''`{.literal}                              | Dracut network arguments. Required if the `url_to_load_squashfs_`{.literal} from option is set to a non-empty string.                    |
    +---------------------------------------------+-----------------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
    | `setup_network_manager`{.literal}           | `bool`{.literal}      | `False`{.literal}                           | If set to `False`{.literal}, the Leapp utility enables Network Manager in the upgrade image.                                             |
    +---------------------------------------------+-----------------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
    | `setup_opensshd_using_auth_keys`{.literal}  | `str`{.literal}       | `''`{.literal}                              | If set to a non-empty string, `openssh`{.literal} daemon is configured within the upgrade image using the provided authorized keys file. |
    +---------------------------------------------+-----------------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
    | `setup_passwordless_root`{.literal}         | `bool`{.literal}      | `False`{.literal}                           | If set to `True`{.literal}, the root account of the upgrade image has an empty password. Use with caution.                               |
    +---------------------------------------------+-----------------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
    | `squashfs_image_path`{.literal}             | `str`{.literal}       | `/var/lib/leapp/live-upgrade.img`{.literal} | Location of the upgrade image of the minimal target system.                                                                              |
    +---------------------------------------------+-----------------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
    | `url_to_load_squashfs_image_from`{.literal} | `str`{.literal}       | `''`{.literal}                              | URL of the upgrade image.                                                                                                                |
    +---------------------------------------------+-----------------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

    : Table 3.1. LiveMode configuration

    Show more

    The following is an example of a `/etc/leapp/actor_conf.d/livemode.yaml`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    livemode:
      additional_packages : [ vim ]
      autostart_upgrade_after_reboot : false
      setup_network_manager : true
      setup_opensshd_using_auth_keys : /root/.ssh/authorized_keys
    ```

    The example file results in the following actions:

    -   The Leapp utility installs the `vim`{.literal} package into the upgrade environment.
    -   The upgrade does not start automatically after reboot. You must manually restart it. This allows you to manually inspect the system and verify that the upgrade finished as expected and the system is ready for use before starting.
    -   The Leapp utility attempts to enable NetworkManager inside the upgrade environment by using the source system's network profiles.
    -   The Leapp utility enables the `opensshd`{.literal} service. If the system establishes network access successfully, you can use SSH to log in to the upgrade environment by using the root account and interact with the system.

## [Chapter 4. Manually upgrading small deployments](#manually-upgrading-small-deployments) {#chapter-4.-manually-upgrading-small-deployments .title}

You can upgrade your system manually by using the command-line interface and web console. This method is preferred when upgrading a small number of machines because manual upgrades are usually easier and less time-consuming than using Ansible roles.

### [4.1. Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report) {#reviewing-the-pre-upgrade-report .title}

To assess upgradability of your system, start the pre-upgrade process by using the `leapp preupgrade`{.literal} command. During this phase, the `Leapp`{.literal} utility collects data about the system, assesses upgradability, and generates a pre-upgrade report.

#### [4.1.1. About the pre-upgrade report](#about-the-pre-upgrade-report) {#about-the-pre-upgrade-report .title}

The pre-upgrade report summarizes potential problems and suggests recommended solutions. The report also helps you decide whether it is possible or advisable to proceed with the upgrade.

Reviewing a pre-upgrade report can also be useful if you want to perform a fresh installation of a RHEL 9 system instead of the in-place upgrade process.

Always review the entire pre-upgrade report, even when the report finds no inhibitors to the upgrade. The pre-upgrade report contains recommended actions to complete before the upgrade to ensure that the upgraded system functions correctly.

Important

The pre-upgrade assessment does not modify the system configuration, but it does consume non-negligible space in the `/var/lib/leapp`{.literal} directory. In most cases, the pre-upgrade assessment requires up to 4 GB of space, but the actual size depends on your system configuration. If there is not enough space in the hosted file system, the pre-upgrade report might not show complete results of the analysis. To prevent issues, ensure that your system has enough space in the `/var/lib/leapp`{.literal} directory or move the directory to a dedicated partition so that space consumption does not affect other parts of the system.

You can assess upgradability in the pre-upgrade phase using either of the following ways:

-   Review the pre-upgrade report in the generated `leapp-report.txt`{.literal} file and manually resolve reported problems by using the command-line interface.
-   Use the web console to review the report, apply automated remediations where available, and fix remaining problems using the suggested remediation hints.

Note

You can process the pre-upgrade report by using your own custom scripts, for example, to compare results from multiple reports across different environments. For more information, see [Automating your Red Hat Enterprise Linux pre-upgrade report workflow](https://access.redhat.com/articles/5777571).

Important

The pre-upgrade report cannot simulate the entire in-place upgrade process and therefore cannot identify all inhibiting problems with your system. As a result, the Leapp utility might still terminate your in-place upgrade even after you have reviewed and remediated all problems in the report. For example, the pre-upgrade report cannot detect issues related to broken package downloads.

#### [4.1.2. Assessing upgradability from the command line](#assessing-upgradability-of-rhel-9-to-rhel-10-from-the-command-line) {#assessing-upgradability-from-the-command-line .title}

You can identify potential upgrade problems during the pre-upgrade phase before the upgrade by using the command line.

**Prerequisites**

-   You completed the in [Preparing for the upgrade](#preparing-for-the-upgrade "Chapter 3. Preparing for the upgrade") procedure.

-   You are logged in as the root user with the unconfined SELinux role.

    Note

    If you use the `sudo`{.literal} command, you must use the `-r unconfined_r -t unconfined_t`{.literal} options when entering each `leapp`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo -r unconfined_r -t unconfined_t leapp preupgrade
    ```

**Procedure**

1.  On your RHEL 9 system, perform the pre-upgrade phase:

    ``` {.language-plaintext tabindex="-1"}
    # leapp preupgrade --target <_target_os_version_>
    ```

    Replace *target_os_version* with the target OS version, for example `10.0`{.literal}. If no target OS version is defined, `Leapp`{.literal} uses the default target OS version specified in the table 1.1 in [Supported upgrade paths](#supported-upgrade-paths "Chapter 1. Supported upgrade paths").

    -   If you are using [custom repositories](https://access.redhat.com/articles/4977891#repos) from the `/etc/yum.repos.d/`{.literal} directory for the upgrade, enable the selected repositories as follows:

        ``` {.language-plaintext tabindex="-1"}
        # leapp preupgrade --enablerepo <repository_id1> --enablerepo <repository_id2> ...
        ```

        Replace *repository_id* with the repository IDs.

    -   If you are [upgrading without RHSM](https://access.redhat.com/articles/4977891#upgrade-without-rhsm) or by using RHUI, add the `--no-rhsm`{.literal} option.

    -   If you have an [Extended Upgrade Support (EUS)](https://access.redhat.com/articles/rhel-eus), Advanced Update Support (AUS), or [Update Services for SAP Solutions (E4S)](https://access.redhat.com/solutions/3082481) subscription, add the `--channel `{.literal}*`<channel>`{.literal}* option. Replace *\<channel\>* with the channel name, for example, `eus`{.literal} or `aus`{.literal}. Note that SAP HANA customers should perform the in-place upgrade by using the [Upgrading SAP environments from RHEL 9 to RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/10/html/upgrading_sap_environments_from_rhel_9_to_rhel_10/index) guide.

    -   If you are using RHEL for Real Time or the Real Time for Network Functions Virtualization (NFV) in your Red Hat OpenStack Platform, enable the deployment by using the `--enablerepo`{.literal} option. For example:

        ``` {.language-plaintext tabindex="-1"}
        # leapp preupgrade --enablerepo rhel-10-for-x86_64-rt-rpms
        ```

        For more information, see [Configuring Real-Time Compute](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/14/html/advanced_overcloud_customization/realtime-compute).

2.  Examine the report in the `/var/log/leapp/leapp-report.txt`{.literal} file and manually resolve all the reported problems. Some reported problems contain remediation suggestions. **Inhibitor** problems prevent you from upgrading until you have resolved them.

    The report contains the following risk factor levels:

    -   **High** - Very likely to result in a deteriorated system state.
    -   **Medium** - Can impact both the system and applications.
    -   **Low** - Should not impact the system but can have an impact on applications.
    -   **Info** - Informational with no expected impact to the system or applications.

3.  In certain system configurations, the `Leapp`{.literal} utility generates true or false questions that you must answer manually. If the pre-upgrade report contains a **Missing required answers in the answer file** message, complete the following steps:

    a.  Open the `/var/log/leapp/answerfile`{.literal} file and review the true or false questions.

    b.  Manually edit the `/var/log/leapp/answerfile`{.literal} file, uncomment the confirm line of the file by deleting the `#`{.literal} symbol, and confirm your answer as `True`{.literal} or `False`{.literal}. For more information, see the [Troubleshooting tips](#troubleshooting-tips "9.2. Troubleshooting tips").

        Note

        Alternatively, you can answer the true or false question by running the following command:

        ``` {.language-plaintext tabindex="-1"}
        # leapp answer --section <question_section>.<field_name>=<answer>
        ```

4.  Repeat the previous steps to rerun the pre-upgrade report to verify that you have resolved all critical issues.

#### [4.1.3. Assessing upgradability and applying automated remediations through the web console](#assessing-upgradability-of-rhel-9-to-rhel-10-and-applying-automated-remediations-through-the-web-console) {#assessing-upgradability-and-applying-automated-remediations-through-the-web-console .title}

You can identify potential problems in the pre-upgrade phase before the upgrade and apply automated remediations by using the web console. See [Getting started using the RHEL web console for more information about the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_systems_using_the_rhel_9_web_console/index).

**Prerequisites**

-   You completed the in [Preparing for the upgrade](#preparing-for-the-upgrade "Chapter 3. Preparing for the upgrade") procedure.

-   You are logged in as the root user with the unconfined SELinux role.

    Note

    If you use the `sudo`{.literal} command, you must use the `-r unconfined_r -t unconfined_t`{.literal} options when entering each `leapp`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo -r unconfined_r -t unconfined_t leapp preupgrade
    ```

**Procedure**

1.  Install the `cockpit-leapp`{.literal} plug-in:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install cockpit-leapp
    ```

2.  Log in to the web console as `root`{.literal} or as a user that has permissions to enter administrative commands with `sudo`{.literal}.

3.  On your RHEL 9 system, perform the pre-upgrade phase either from the command line or from the web console command line:

    ``` {.language-plaintext tabindex="-1"}
    # leapp preupgrade --target <target_os_version>
    ```

    Replace *target_os_version* with the target OS version, for example `10.0`{.literal}. If no target OS version is defined, `Leapp`{.literal} uses the default target OS version specified in the table 1.1 in [Supported upgrade paths](#supported-upgrade-paths "Chapter 1. Supported upgrade paths").

    -   If you are using [custom repositories](https://access.redhat.com/articles/4977891#repos) from the `/etc/yum.repos.d/`{.literal} directory for the upgrade, enable the selected repositories as follows:

        ``` {.language-plaintext tabindex="-1"}
        # leapp preupgrade --enablerepo <repository_id1> --enablerepo <repository_id2> ...
        ```

    -   If you are [upgrading without RHSM](https://access.redhat.com/node/4977891/#upgrade-without-rhsm) or by using RHUI, add the `--no-rhsm`{.literal} option.

    -   If you have an [Extended Upgrade Support (EUS)](https://access.redhat.com/articles/rhel-eus), Advanced Update Support (AUS), or [Update Services for SAP Solutions (E4S)](https://access.redhat.com/solutions/3082481) subscription, add the `--channel `{.literal}*`<channel>`{.literal}* option. Replace *\<channel\>* with the channel name, for example, `eus`{.literal} or `aus`{.literal}. Note that SAP HANA customers should perform the in-place upgrade using the [Upgrading SAP environments from RHEL 9 to RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/10/html/upgrading_sap_environments_from_rhel_9_to_rhel_10/index) guide.

    -   If you are using RHEL for Real Time or the Real Time for Network Functions Virtualization (NFV) in your Red Hat OpenStack Platform, enable the deployment by using the `--enablerepo`{.literal} option. For example:

        ``` {.language-plaintext tabindex="-1"}
        # leapp preupgrade --enablerepo rhel-10-for-x86_64-rt-rpms
        ```

        For more information, see [Configuring Real-Time Compute](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/14/html/advanced_overcloud_customization/realtime-compute).

4.  In the web console, select **Upgrade Report** from the navigation menu to review all reported problems. **Inhibitor** problems prevent you from upgrading until you have resolved them. To view a problem in detail, select the row to open the Detail pane.

    **Figure 4.1. In-place upgrade report in the web console**

    The report contains the following risk factor levels:

    -   **High** - Very likely to result in a deteriorated system state.
    -   **Medium** - Can impact both the system and applications.
    -   **Low** - Should not impact the system but can have an impact on applications.
    -   **Info** - Informational with no expected impact to the system or applications.

5.  In certain configurations, the `Leapp`{.literal} utility generates true or false questions that you must answer manually. If the Upgrade Report contains a **Missing required answers in the answer file** row, complete the following steps:

    a.  Select the **Missing required answers in the answer file** row to open the **Detail** pane. The default answer is stated at the end of the remediation command.

    b.  To confirm the default answer, select **Add to Remediation Plan** to start the remediation later or **Run Remediation** to start the remediation immediately.

    c.  To select the non-default answer instead, run the `leapp answer`{.literal} command in the command line, specifying the question you are responding to and your confirmed answer.

        ``` {.language-plaintext tabindex="-1"}
        # leapp answer --section <question_section>.<field_name>=<answer>
        ```

        Note

        You can also manually edit the `/var/log/leapp/answerfile`{.literal} file, uncomment the confirm line of the file by deleting the `#`{.literal} symbol, and confirm your answer as `True`{.literal} or `False`{.literal}. For more information, see the [Troubleshooting tips](#troubleshooting-tips "9.2. Troubleshooting tips").

6.  Some problems have remediation commands that you can run to automatically resolve the problems. You can run remediation commands individually or all together in the remediation command.

    a.  To run a single remediation command, open the **Detail** pane for the problem and click **Run Remediation**.

    b.  To add a remediation command to the remediation plan, open the **Detail** pane for the problem and click **Add to Remediation Plan**.

        **Figure 4.2. Detail pane**

    c.  To run the remediation plan containing all added remediation commands, click the **Remediation plan** link in the top right corner above the report. Click **Execute Remediation Plan** to run all listed commands.

7.  After reviewing the report and resolving all reported problems, repeat steps 3-7 to rerun the report to verify that you have resolved all critical issues.

### [4.2. Performing the upgrade](#performing-the-upgrade) {#performing-the-upgrade .title}

After you have completed the preparatory steps and reviewed and resolved the problems found in the pre-upgrade report, you can perform the in-place upgrade on your system.

#### [4.2.1. Performing the upgrade from RHEL 9.8 to RHEL 10.2](#performing-the-upgrade-from-rhel-9-to-rhel-10) {#performing-the-upgrade-from-rhel-9.8-to-rhel-10.2 .title}

You can perform the upgrade from RHEL 9 to RHEL 10 by using the `Leapp`{.literal} utility.

**Prerequisites**

-   You completed the [Preparing for the upgrade](#preparing-for-the-upgrade "Chapter 3. Preparing for the upgrade") procedure, including a full system backup.

-   You completed the [Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report "4.1. Reviewing the pre-upgrade report") procedure and all reported issues resolved.

-   You have temporarily disabled antivirus software and configured health checks, including IPMI watchdogs, to prevent the upgrade from failing.

    Warning

    It is critical to temporarily disable configured health checks before performing the in-place upgrade to prevent the upgrade process from being interrupted during critical phases, causing system loss.

**Procedure**

1.  Ensure that you have a full system backup or a virtual machine snapshot. You can use the following backup options:

    -   Create a full backup of your system by using the Relax-and-Recover (ReaR) utility. For more information, see [Recovering and restoring a system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/assembly_recovering-and-restoring-a-system_configuring-basic-system-settings) and [What is Relax and Recover (ReaR) and how can I use it for disaster recovery?](https://access.redhat.com/solutions/2115051).

    -   Create a snapshot of your system by using LV snapshots or RAID splitting. For more information, see [Managing logical volume snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_and_managing_logical_volumes/index#managing-lv-snapshots_advanced-logical-volume-management) or [Splitting off a RAID image as a separate logical volume](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_and_managing_logical_volumes/index#splitting-off-a-raid-image-as-a-separate-logical-volume_configuring-raid-logical-volumes). In case of upgrading a virtual machine, you can create a snapshot of the whole VM. You can also manage snapshot and rollback boot entries by using the Boom utility. For more information, see [What is BOOM and how to install it?](https://access.redhat.com/solutions/3750001) and [Managing system upgrades with snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/managing-system-upgrades-with-snapshots_configuring-and-managing-logical-volumes).

        Note

        Because LVM snapshots do not create a full backup of your system, you might not be able to recover your system after certain upgrade failures. As a result, it is safer to create a full backup by using the ReaR utility.

2.  On your RHEL 9 system, start the upgrade process:

    ``` {.language-plaintext tabindex="-1"}
    # leapp upgrade --target <_target_os_version_>
    ```

    Replace *target_os_version* with the target OS version, for example `10.0`{.literal}. If no target OS version is defined, `Leapp`{.literal} uses the default target OS version specified in the table 1.1 in [Supported upgrade paths](#supported-upgrade-paths "Chapter 1. Supported upgrade paths").

    -   If you are using [custom repositories](https://access.redhat.com/articles/4977891#repos) from the `/etc/yum.repos.d/`{.literal} directory for the upgrade, enable the selected repositories as follows:

        ``` {.language-plaintext tabindex="-1"}
        # leapp upgrade --enablerepo <repository_id1> --enablerepo <repository_id2> ...
        ```

    -   If you are [upgrading without RHSM](https://access.redhat.com/node/4977891/#upgrade-without-rhsm) or by using RHUI, add the `--no-rhsm`{.literal} option.

    -   If you are upgrading by using an ISO image, add the `--no-rhsm`{.literal} and `--iso `{.literal}*`<file_path>`{.literal}* options. Replace *\<file_path\>* with the file path to the saved ISO image, for example `/home/rhel9.iso`{.literal}.

    -   If you have an [Extended Upgrade Support (EUS)](https://access.redhat.com/articles/rhel-eus), Advanced Update Support (AUS), or [Update Services for SAP Solutions (E4S)](https://access.redhat.com/solutions/3082481) subscription, add the `--channel `{.literal}*`channel`{.literal}* option. Replace *channel* with the value you used with the `leapp preupgrade`{.literal} command, for example, `eus`{.literal} or `aus`{.literal}. Note that you must use the same value with the `--channel`{.literal} option in both the `leapp preupgrade`{.literal} and `leapp upgrade`{.literal} commands.

    -   If you are using RHEL for Real Time or the Real Time for Network Functions Virtualization (NFV) in your Red Hat OpenStack Platform, enable the deployment by using the `--enablerepo`{.literal} option. For example:

        ``` {.language-plaintext tabindex="-1"}
        # leapp upgrade --enablerepo rhel-10-for-x86_64-rt-rpms
        ```

        For more information, see [Configuring Real-Time Compute](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/14/html/advanced_overcloud_customization/realtime-compute).

    -   If you are upgrading with LiveMode, set the `LEAPP_UNSUPPORTED=1`{.literal} environment variable and use the `--enable-experimental-feature`{.literal} option with the `livemode`{.literal} value. For example:

        ``` {.language-plaintext tabindex="-1"}
        # LEAPP_UNSUPPORTED=1 leapp upgrade --enable-experimental-feature livemode
        ```

        For more information, see [Configuring the upgrade from RHEL 9.7 to RHEL 10.1 with LiveMode](#configuring-the-upgrade-with-livemode "3.3. Configuring the upgrade from RHEL 9.8 to RHEL 10.2 with LiveMode").

        Important

        LiveMode is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

        For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

3.  At the beginning of the upgrade process, `Leapp`{.literal} repeats the pre-upgrade phase described in [Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report "4.1. Reviewing the pre-upgrade report"):

    -   If the system is upgradable, `Leapp`{.literal} downloads necessary data and prepares an RPM transaction for the upgrade.
    -   If your system does not meet the parameters for a reliable upgrade, `Leapp`{.literal} terminates the upgrade process and provides a record describing the issue and a recommended solution in the `/var/log/leapp/leapp-report.txt`{.literal} file. For more information, see [Troubleshooting](#troubleshooting "Chapter 9. Troubleshooting").

4.  Manually restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

    The system boots into a RHEL 10-based initial RAM disk image, initramfs. `Leapp`{.literal} upgrades all packages and automatically restarts to the RHEL 10 system.

    Alternatively, you can run the `leapp upgrade`{.literal} command with the `--reboot`{.literal} option and skip this manual step.

    If a failure occurs, investigate logs and known issues as described in [Troubleshooting](#troubleshooting "Chapter 9. Troubleshooting").

5.  Log in to the RHEL 10 system and verify its state as described in [Verifying the post-upgrade state](#verifying-the-post-upgrade-state "Chapter 6. Verifying the post-upgrade state").

6.  Perform all post-upgrade tasks described in the upgrade report and in [Performing post-upgrade tasks](#performing-post-upgrade-tasks-on-the-rhel-10-system "Chapter 7. Performing post-upgrade tasks on the RHEL 10 system").

#### [4.2.2. Performing the upgrade from RHEL 9.6 to RHEL 10.0](#performing-the-upgrade-from-rhel-9.6-to-rhel-10.0) {#performing-the-upgrade-from-rhel-9.6-to-rhel-10.0 .title}

You can perform the upgrade from RHEL 9 to RHEL 10 by using the `Leapp`{.literal} utility.

**Prerequisites**

-   You completed the [Preparing for the upgrade](#preparing-for-the-upgrade "Chapter 3. Preparing for the upgrade") procedure, including a full system backup.
-   You completed the [Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report "4.1. Reviewing the pre-upgrade report") procedure and all reported issues resolved.
-   You have temporarily disabled antivirus software to prevent the upgrade from failing.

**Procedure**

1.  Ensure that you have a full system backup or a virtual machine snapshot. You can use the following backup options:

    -   Create a full backup of your system by using the Relax-and-Recover (ReaR) utility. For more information, see [Recovering and restoring a system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/assembly_recovering-and-restoring-a-system_configuring-basic-system-settings) and [What is Relax and Recover (ReaR) and how can I use it for disaster recovery?](https://access.redhat.com/solutions/2115051).

    -   Create a snapshot of your system by using LV snapshots or RAID splitting. For more information, see [Managing logical volume snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_and_managing_logical_volumes/index#managing-lv-snapshots_advanced-logical-volume-management) or [Splitting off a RAID image as a separate logical volume](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_and_managing_logical_volumes/index#splitting-off-a-raid-image-as-a-separate-logical-volume_configuring-raid-logical-volumes). In case of upgrading a virtual machine, you can create a snapshot of the whole VM. You can also manage snapshot and rollback boot entries by using the Boom utility. For more information, see [What is BOOM and how to install it?](https://access.redhat.com/solutions/3750001) and [Managing system upgrades with snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/managing-system-upgrades-with-snapshots_configuring-and-managing-logical-volumes).

        Note

        Because LVM snapshots do not create a full backup of your system, you might not be able to recover your system after certain upgrade failures. As a result, it is safer to create a full backup by using the ReaR utility.

2.  On your RHEL 9 system, start the upgrade process:

    ``` {.language-plaintext tabindex="-1"}
    # leapp upgrade --target <_target_os_version_>
    ```

    Replace *target_os_version* with the target OS version, for example `10.0`{.literal}. If no target OS version is defined, `Leapp`{.literal} uses the default target OS version specified in the table 1.1 in [Supported upgrade paths](#supported-upgrade-paths "Chapter 1. Supported upgrade paths").

    -   If you are using [custom repositories](https://access.redhat.com/articles/4977891#repos) from the `/etc/yum.repos.d/`{.literal} directory for the upgrade, enable the selected repositories as follows:

        ``` {.language-plaintext tabindex="-1"}
        # leapp upgrade --enablerepo <repository_id1> --enablerepo <repository_id2> ...
        ```

    -   If you are [upgrading without RHSM](https://access.redhat.com/node/4977891/#upgrade-without-rhsm), add the `--no-rhsm`{.literal} option.

    -   If you are upgrading by using an ISO image, add the `--no-rhsm`{.literal} and `--iso `{.literal}*`<file_path>`{.literal}* options. Replace *\<file_path\>* with the file path to the saved ISO image, for example `/home/rhel9.iso`{.literal}.

    -   If you have an [Extended Upgrade Support (EUS)](https://access.redhat.com/articles/rhel-eus) or Advanced Update Support (AUS) subscription, add the `--channel `{.literal}*`channel`{.literal}* option. Replace *channel* with the value you used with the `leapp preupgrade`{.literal} command, for example, `eus`{.literal} or `aus`{.literal}. Note that you must use the same value with the `--channel`{.literal} option in both the `leapp preupgrade`{.literal} and `leapp upgrade`{.literal} commands.

    -   If you are using RHEL for Real Time or the Real Time for Network Functions Virtualization (NFV) in your Red Hat OpenStack Platform, enable the deployment by using the `--enablerepo`{.literal} option. For example:

        ``` {.language-plaintext tabindex="-1"}
        # leapp upgrade --enablerepo rhel-10-for-x86_64-rt-rpms
        ```

        For more information, see [Configuring Real-Time Compute](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/14/html/advanced_overcloud_customization/realtime-compute).

3.  At the beginning of the upgrade process, `Leapp`{.literal} repeats the pre-upgrade phase described in [Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report "4.1. Reviewing the pre-upgrade report").

    -   If the system is upgradable, `Leapp`{.literal} downloads necessary data and prepares an RPM transaction for the upgrade.
    -   If your system does not meet the parameters for a reliable upgrade, `Leapp`{.literal} terminates the upgrade process and provides a record describing the issue and a recommended solution in the `/var/log/leapp/leapp-report.txt`{.literal} file. For more information, see [Troubleshooting](#troubleshooting "Chapter 9. Troubleshooting").

4.  Manually restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

    In this phase, the system boots into a RHEL 10-based initial RAM disk image, initramfs. `Leapp`{.literal} upgrades all packages and automatically restarts to the RHEL 10 system.

    Alternatively, you can run the `leapp upgrade`{.literal} command with the `--reboot`{.literal} option and skip this manual step.

    If a failure occurs, investigate logs and known issues as described in [Troubleshooting](#troubleshooting "Chapter 9. Troubleshooting").

5.  Log in to the RHEL 10 system and verify its state as described in [Verifying the post-upgrade state](#verifying-the-post-upgrade-state "Chapter 6. Verifying the post-upgrade state").

6.  Perform all post-upgrade tasks described in the upgrade report and in [Performing post-upgrade tasks](#performing-post-upgrade-tasks-on-the-rhel-10-system "Chapter 7. Performing post-upgrade tasks on the RHEL 10 system").

## [Chapter 5. Upgrading large deployments by using Ansible roles](#upgrading-large-deployments-by-using-ansible-roles) {#chapter-5.-upgrading-large-deployments-by-using-ansible-roles .title}

To streamline pre-upgrade reporting, remediation, and the upgrade itself, you can use Ansible roles to handle the upgrade process.

### [5.1. Ansible roles for upgrading large deployments](#ansible-roles-for-upgrading-large-deployments) {#ansible-roles-for-upgrading-large-deployments .title}

You can automate the process of upgrading large numbers of systems from RHEL 9 to RHEL 10 by using the `analysis`{.literal}, `remediate`{.literal}, and `upgrade`{.literal} Ansible roles as follows:

-   `analysis`{.literal} - This Ansible role runs the pre-upgrade report, which analyzes the target system for upgradability and flags potential issues. Along with the `remediate`{.literal} role, this role replaces the [Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report "4.1. Reviewing the pre-upgrade report") manual procedure.
-   `remediate`{.literal} - This Ansible role fixes issues found in the pre-upgrade report. Along with the `analysis`{.literal} role, this role replaces the [Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report "4.1. Reviewing the pre-upgrade report") manual procedure.
-   `upgrade`{.literal} - This Ansible role runs the upgrade from RHEL 9 to RHEL 10 on the target system and verifies that the upgrade was successful. This role replaces the [Performing the upgrade](#performing-the-upgrade "4.2. Performing the upgrade") and [Verifying the upgrade](#verifying-the-post-upgrade-state "Chapter 6. Verifying the post-upgrade state") manual procedures.

To use the `analysis`{.literal}, `remediate`{.literal}, and `upgrade`{.literal} Ansible roles to upgrade from RHEL 9 to RHEL 10, you must install and run the roles from an Ansible control node running on RHEL 10. These Ansible roles are part of the `ansible-collection-redhat-leapp`{.literal} package available in the RHEL 10 AppStream repository and are supported by Red Hat.

Note

You can also use these Ansible roles to upgrade from [RHEL 7 to RHEL 8](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/upgrading_from_rhel_7_to_rhel_8/upgrading-large-deployments-by-using-ansible-roles_upgrading-from-rhel-7-to-rhel-8) or from [RHEL 8 to RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/upgrading_from_rhel_8_to_rhel_9/upgrading-large-deployments-by-using-ansible-roles_upgrading-from-rhel-8-to-rhel-9) from an Ansible control node running on RHEL 9.

### [5.2. Running the pre-upgrade report by using Ansible roles](#running-the-pre-upgrade-report-by-using-ansible-roles) {#running-the-pre-upgrade-report-by-using-ansible-roles .title}

You can use the `analysis`{.literal} Ansible role to run the pre-upgrade report on the target system. The pre-upgrade report summarizes potential problems and suggests recommended solutions. The report also helps you decide whether it is possible or advisable to proceed with the upgrade.

The `analysis`{.literal} Ansible role is best used in conjunction with the `remediate`{.literal} Ansible role, which completes the pre-upgrade process by remediating and fixing issues found within the report. These two roles replace the manual procedure described in [Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report "4.1. Reviewing the pre-upgrade report").

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).

-   You are logged in to the control node as a user who can run playbooks on the managed nodes.

-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

-   You have completed the [Planning an upgrade to RHEL 10](#planning-an-upgrade-to-rhel-10 "Chapter 2. Planning an upgrade to RHEL 10") and [Preparing for the upgrade](#preparing-for-the-upgrade "Chapter 3. Preparing for the upgrade") procedures.

-   You have installed the `ansible-collection-redhat-leapp`{.literal} package to an Ansible control node running on RHEL 10.

    Note

    To upgrade a RHEL 9 managed node, you must use a RHEL 10 control node. Only a RHEL 10 control node supports managing RHEL 10 nodes and includes the `ansible-collection-redhat-leapp`{.literal} package.

**Procedure**

1.  Create a playbook file, for example `~/analysis.yml`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: RHEL pre-upgrade analysis
      hosts: managed-node-01.example.com

      tasks:
        - name: Generate pre-upgrade analysis report
          ansible.builtin.import_role:
            name: redhat.leapp.analysis
          vars:
            leapp_upgrade_type: satellite
            leapp_satellite_organization: <satellite_org>
            leapp_satellite_activation_key_post_analysis: <activation_key_post_analysis>
            leapp_satellite_activation_key: <activation_key>
    ```

    The settings specified in the example playbook include the following:

    `leapp_upgrade_type: `{.literal}*`<upgrade_type>`{.literal}*
    :   Optional: The type of upgrade being performed. The default value is `cdn`{.literal}, which must be used for hosts registered with Red Hat CDN. Set to `satellite`{.literal} for hosts registered with Satellite, `rhui`{.literal} for hosts using RHUI repositories, and `custom`{.literal} for custom repositories. Note that the preceding playbook example uses Satellite, not the default CDN.

    `leapp_satellite_organization: `{.literal}*`<organization>`{.literal}*
    :   Optional: Organization used in Satellite definition. Use only if upgrading by using Satellite. You can omit this variable if the system is registered with an activation key for a content view that includes both the current RHEL version and the next version repositories.

    `leapp_satellite_activation_key_post_analysis: `{.literal}*`<activation_key_post_analysis>`{.literal}*
    :   Optional: Activation key for the current RHEL version content view to register to after analysis. Use only if upgrading by using Satellite. You can omit this variable if the system is registered with an activation key for the content view, including both the current RHEL version and the next version.

    `leapp_satellite_activation_key: `{.literal}*`<activation_key>`{.literal}*
    :   Optional: Activation key for the content view, including both the current RHEL version and the next version. Use only if upgrading by using Satellite. You can omit this variable if the system is registered with an activation key for the content view, including both the current RHEL version and the next version.

    `leapp_preupg_opts: `{.literal}*`<options>`{.literal}*

    :   Optional: List of command line options to run with the pre-upgrade command, namely:

        -   `--target-version `{.literal}*`<target_os_version>`{.literal}*
        -   `--enablerepo `{.literal}*`<repository_id>`{.literal}* if you are upgrading with custom repositories
        -   `--no-rhsm`{.literal} if you are upgrading with custom repositories
        -   `--channel `{.literal}*`<channel>`{.literal}* if you have an EUS or AUS subscription

    `leapp_answerfile: `{.literal}*`<answerfile>`{.literal}*
    :   Optional: In certain system configurations, the pre-upgrade report requires you to respond to certain true or false questions. This variable sets the true or false answer to the designated question.

    For details about all variables that can be used in the playbook, see the `/usr/share/ansible/collections/ansible_collections/redhat/leapp/roles/analysis/README.md`{.literal} file on the control node.

    Note that if you upgrade systems that run different RHEL versions, you can specify their variables within Ansible `host_vars`{.literal} files.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/analysis.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but syntactically valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/analysis.yml
    ```

4.  Review the output to confirm that the analysis was successful:

    ``` {.language-plaintext tabindex="-1"}
    RUNNING HANDLER [redhat.leapp.analysis : Pre-upgrade analysis report is done] *************************************************************************************************
    ok: [managed-node-01.example.com] => {
        "msg": "The pre-upgrade analysis report generation is now complete. SUCCESS: No inhibitors found. Review the tasks above or the result file at /var/log/leapp/leapp-report.txt."
    }
    ```

5.  Review the pre-upgrade report at one of the following locations:

    -   `/var/log/leapp/leapp-report.txt`{.literal} on the managed node.
    -   *`<workdir>`{.literal}*`/ansible_leapp_`{.literal}*`<role_name>`{.literal}*`_logs_`{.literal}*`<timestamp>`{.literal}* directory on the control node. This directory contains subdirectories for each managed node.

**Next steps**

-   [Remediating the pre-upgrade report by using Ansible roles](#remediating-the-pre-upgrade-report-by-using-ansible-roles "5.3. Remediating the pre-upgrade report by using Ansible roles")

### [5.3. Remediating the pre-upgrade report by using Ansible roles](#remediating-the-pre-upgrade-report-by-using-ansible-roles) {#remediating-the-pre-upgrade-report-by-using-ansible-roles .title}

You can use the `remediate`{.literal} Ansible role to remediate and fix problems found on the target system by the pre-upgrade report. The report summarizes potential problems and suggests recommended solutions. The report also helps you decide whether it is possible or advisable to proceed with the upgrade.

The `remediate`{.literal} Ansible role is best used in conjunction with the `analysis`{.literal} Ansible role, which starts the pre-upgrade process by analyzing the target system and generating the pre-upgrade report. These two roles replace the manual procedure described in [Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report "4.1. Reviewing the pre-upgrade report").

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   You have completed the [Planning an upgrade to RHEL 10](#planning-an-upgrade-to-rhel-10 "Chapter 2. Planning an upgrade to RHEL 10") and [Preparing for the upgrade](#preparing-for-the-upgrade "Chapter 3. Preparing for the upgrade") procedures.
-   You have installed the `ansible-collection-redhat-leapp`{.literal} package to an Ansible control node running on RHEL 10.
-   You have generated the pre-upgrade report by using the `analysis`{.literal} Ansible role. See [Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report "4.1. Reviewing the pre-upgrade report") and [Running the pre-upgrade report by using Ansible roles](#running-the-pre-upgrade-report-by-using-ansible-roles "5.2. Running the pre-upgrade report by using Ansible roles") for more information.

**Procedure**

1.  Review the `host_vars`{.literal} files created by the analysis role on the control node. By default, the `host_vars`{.literal} files are created in the playbook location. These files contain instructions on which remediate role tasks can be applied to remediate the upgrade inhibitors detected by the analysis role.

    Note

    Not all inhibitors can be remediated by the `remediate`{.literal} Ansible role, and either must instead be remediated manually or cannot be remediated.

    The following is an example of a `host_vars`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    ---
    leapp_remediation_todo:
    - leapp_nfs_detected
    - leapp_remote_using_root
    leapp_satellite_activation_key: <activation_key>
    leapp_satellite_activation_key_post_analysis: <activation_key_post_analysis>
    leapp_satellite_activation_key_post_upgrade: <activation_key_post_upgrade>
    ```

2.  Use the `remediate.yml`{.literal} playbook, generated by the `analysis`{.literal} role, to resolve the identified inhibitors. This playbook runs the `remediation`{.literal} role and you can customize the playbook to meet your requirements. For example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Remediate
      hosts: managed-node-01.example.com
      tasks:
        - name: Perform remediations on the system
          ansible.builtin.include_role:
            name: redhat.leapp.remediate
    ```

    Note

    You can also create a new remediation playbook instead of copying the generated playbook. For more information, see the `/usr/share/ansible/collections/ansible_collections/redhat/leapp/roles/remediate/README.md`{.literal} file on the control node.

3.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/remediate.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

4.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/remediate.yml
    ```

5.  After remediations are applied, re-run the pre-upgrade report. For more information, see [Running the pre-upgrade report by using Ansible roles](#running-the-pre-upgrade-report-by-using-ansible-roles "5.2. Running the pre-upgrade report by using Ansible roles").

### [5.4. Upgrading to RHEL 10 by using Ansible roles](#upgrading-to-rhel-10-by-using-ansible-roles) {#upgrading-to-rhel-10-by-using-ansible-roles .title}

You can use the `upgrade`{.literal} Ansible role to upgrade the RHEL 9 target system to RHEL 10 and to run verification steps to ensure the upgrade was successful.

The `upgrade`{.literal} role replaces the [Performing the upgrade](#performing-the-upgrade "4.2. Performing the upgrade") and [Verifying the upgrade](#verifying-the-post-upgrade-state "Chapter 6. Verifying the post-upgrade state") manual procedures.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   You have completed the [Planning an upgrade to RHEL 10](#planning-an-upgrade-to-rhel-10 "Chapter 2. Planning an upgrade to RHEL 10") and [Preparing for the upgrade](#preparing-for-the-upgrade "Chapter 3. Preparing for the upgrade") procedures.
-   You have installed the `ansible-collection-redhat-leapp`{.literal} package to an Ansible control node running on RHEL 10.
-   You have generated and remediated the pre-upgrade report, either by manually running the pre-upgrade report or by using the `analysis`{.literal} and `remediate`{.literal} Ansible roles, and no longer have any inhibitors in the report. See [Reviewing the pre-upgrade report](#reviewing-the-pre-upgrade-report "4.1. Reviewing the pre-upgrade report"), [Running the pre-upgrade report by using Ansible roles](#running-the-pre-upgrade-report-by-using-ansible-roles "5.2. Running the pre-upgrade report by using Ansible roles"), and [Remediating the pre-upgrade report by using Ansible roles](#remediating-the-pre-upgrade-report-by-using-ansible-roles "5.3. Remediating the pre-upgrade report by using Ansible roles") for more information.

**Procedure**

1.  Create a playbook file, for example `~/upgrade.yml`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: RHEL upgrade
      hosts: managed-node-01.example.com

        tasks:
        - name: Perform OS upgrade
          ansible.builtin.import_role:
            name: redhat.leapp.upgrade
          vars:
            leapp_upgrade_type: satellite
            leapp_satellite_organization: <satellite_org>
            leapp_satellite_activation_key: <activation_key>
            leapp_satellite_activation_key_post_upgrade: <activation_key_post_upgrade>
            leapp_upgrade_opts: --target-version 10.2
            leapp_selinux_mode: permissive
    ```

    The settings specified in the example playbook include the following:

    `leapp_upgrade_type: `{.literal}*`<upgrade_type>`{.literal}*
    :   Optional: The type of upgrade being performed. The default value is `cdn`{.literal}, which should be used for hosts registered with Red Hat CDN. Set to `satellite`{.literal} for hosts registered with Satellite, `rhui`{.literal} for hosts using RHUI repositories, and `custom`{.literal} for custom repositories.

    `leapp_satellite_organization: `{.literal}*`<satellite_org>`{.literal}*
    :   Optional: Organization used in Satellite definition. Use only if upgrading by using Satellite. You can omit this variable if the system is registered with an activation key for the content view, including both the current RHEL version and the next version.

    `leapp_satellite_activation_key: `{.literal}*`<activation_key>`{.literal}*
    :   Optional: Activation key for the content view, including both the current RHEL version and the next version. Use only if upgrading by using Satellite. You can omit this variable if the system is registered with an activation key for the content view, including both the current RHEL version and the next version.

    `leapp_satellite_activation_key_post_upgrade: `{.literal}*`<activation_key_post_upgrade>`{.literal}*
    :   Optional: Activation key for the content view with the next RHEL version to register to after the upgrade. Use only if upgrading by using Satellite. You can omit this variable if the system is registered with an activation key for the content view, including both the current RHEL version and the next version.

    `leapp_upgrade_opts: `{.literal}*`<options>`{.literal}*

    :   Optional: List of command line options to run with the upgrade command, namely:

        -   `--target-version `{.literal}*`<target_os_version>`{.literal}*
        -   `--enablerepo `{.literal}*`<repository_id>`{.literal}* if you are upgrading with custom repositories
        -   `--no-rhsm`{.literal} if you are upgrading with custom repositories
        -   `--channel `{.literal}*`<channel>`{.literal}* if you have an EUS or AUS subscription

    `leapp_selinux_mode: `{.literal}*`<mode>`{.literal}*
    :   Optional: By default, the SELinux mode on the RHEL 10 system is set to whichever mode was selected in RHEL 9. Enter `enforcing`{.literal}, `permissive`{.literal}, or `disabled`{.literal} to change the mode in RHEL 10.

    For details about all variables used in the playbook, see the `/usr/share/ansible/collections/ansible_collections/redhat/leapp/roles/upgrade/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/upgrade.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/upgrade.yml
    ```

**Verification**

-   Verify that the following message appears in the Ansible role output:

    ``` {.language-plaintext tabindex="-1"}
    RUNNING HANDLER [redhat.leapp.upgrade : Ansible leapp in-place OS upgrade is done] ******************************************************************************************
    ok: [managed-node-01.example.com] => {
        "msg": "The in-place OS upgrade is now complete. Engage partner teams to begin application validation."
    }
    ```

**Next steps**

-   [Verifying the post-upgrade state](#verifying-the-post-upgrade-state "Chapter 6. Verifying the post-upgrade state")

## [Chapter 6. Verifying the post-upgrade state](#verifying-the-post-upgrade-state) {#chapter-6.-verifying-the-post-upgrade-state .title}

After performing the in-place upgrade to RHEL 10, verify that the system is in the correct state. Doing so allows you to identify and correct any critical errors that could impact your system.

### [6.1. Verifying the post-upgrade state of the RHEL 10 system](#verifying-the-post-upgrade-state-of-the-rhel-10-system) {#verifying-the-post-upgrade-state-of-the-rhel-10-system .title}

After the upgrade to RHEL 10 is completed, determine whether the system is in the required state.

**Prerequisites**

-   The system has been upgraded following the steps described in [Performing the upgrade](#performing-the-upgrade "4.2. Performing the upgrade") and you have been able to log in to RHEL 10.

**Procedure**

-   Verify that the Leapp utility has finished all actions in the upgrade process and the system is ready to be used:

    ``` {.language-plaintext tabindex="-1"}
    # [ -e "/etc/systemd/system/leapp_resume.service" ] || ps -e | grep -q leapp && echo "Leapp has not finished the execution yet!"
    ```

    Important

    If you attempt to use the system before the upgrade is complete, serious issues could occur.

-   Verify that the current OS version is RHEL 10. For example:

    ``` {.language-plaintext tabindex="-1"}
    # cat /etc/redhat-release
    Red Hat Enterprise Linux release 10.1 (Coughlan)
    ```

-   Check the OS kernel version. For example:

    ``` {.language-plaintext tabindex="-1"}
    # uname -r
    6.12.0-124.15.1.el10_1.x86_64
    ```

    Note that `.el10`{.literal} is important and the version should not be earlier than `6.12.0`{.literal}. The upstream base in the string is `6.12`{.literal}. To learn what that number means, see [Understanding RHEL kernel version numbers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/the-linux-kernel#understanding-rhel-kernel-version-numbers).

-   If you are using the Red Hat Subscription Manager:

    -   Verify that the correct product is installed. For example:

        ``` {.language-plaintext tabindex="-1"}
        # subscription-manager list --installed
        +-----------------------------------------+
                  Installed Product Status
        +-----------------------------------------+
        Product Name: Red Hat Enterprise Linux for x86_64
        Product ID:   479
        Version:      10.1
        Arch:         x86_64
        Status:       Subscribed
        ```

    -   Verify that the release version is set to the expected target OS version immediately after the upgrade. For example:

        ``` {.language-plaintext tabindex="-1"}
        # subscription-manager release
        Release: 10.1
        ```

-   Verify that network services are operational, for example, try to connect to a server using SSH.

-   Check the post-upgrade status of your applications. In some cases, you might need to perform migration and configuration changes manually. For example, to migrate your databases, follow instructions in [Configuring and using database servers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_database_servers/index).

## [Chapter 7. Performing post-upgrade tasks on the RHEL 10 system](#performing-post-upgrade-tasks-on-the-rhel-10-system) {#chapter-7.-performing-post-upgrade-tasks-on-the-rhel-10-system .title}

After the in-place upgrade, clean up your RHEL 10 system by removing unneeded packages, disable incompatible repositories, and update the rescue kernel and initial RAM disk.

### [7.1. Performing post-upgrade tasks](#performing-post-upgrade-tasks) {#performing-post-upgrade-tasks .title}

After performing the upgrade to RHEL 10, complete the following recommended major tasks.

**Prerequisites**

\*You completed the [Performing the upgrade](#performing-the-upgrade "4.2. Performing the upgrade") procedure and you have been able to log in to RHEL 10.

-   You verified the status of the in-place upgrade as described in [Verifying the post-upgrade state](#verifying-the-post-upgrade-state "Chapter 6. Verifying the post-upgrade state"). This includes verification that the Leapp utility has finished the upgrade process.

**Procedure**

1.  Remove any remaining `Leapp`{.literal} packages from the exclude list in the `/etc/dnf/dnf.conf`{.literal} configuration file, including the `snactor`{.literal} package, which is a tool for upgrade extension development. During the in-place upgrade, `Leapp`{.literal} packages that were installed with the `Leapp`{.literal} utility are automatically added to the exclude list to prevent critical files from being removed or updated. After the in-place upgrade, these `Leapp`{.literal} packages must be removed from the exclude list before they can be removed from the system.

    -   To manually remove packages from the exclude list, edit the `/etc/dnf/dnf.conf`{.literal} configuration file and remove the `Leapp`{.literal} packages from the exclude list.

    -   To remove all packages from the exclude list:

        ``` {.language-plaintext tabindex="-1"}
        # dnf config-manager --save --setopt exclude=''
        ```

2.  Remove remaining RHEL 9 packages, including remaining `Leapp`{.literal} packages.

    a.  Locate remaining RHEL 9 packages:

        ``` {.language-plaintext tabindex="-1"}
        # rpm -qa | grep -e '\.el[789]' | grep -vE '^(gpg-pubkey|libmodulemd|katello-ca-consumer)' | sort
        ```

    b.  Remove remaining RHEL 9 packages from your RHEL 10 system. To ensure that RPM dependencies are maintained, use the `dnf remove`{.literal} command.

        For example:

        ``` {.language-plaintext tabindex="-1"}
        # dnf remove $(rpm -qa | grep \.el[789] | grep -vE 'gpg-pubkey|libmodulemd|katello-ca-consumer')
        ```

        Important

        This step might also remove third-party packages. Review the transaction before accepting to ensure no packages are unintentionally removed.

    c.  Remove remaining `Leapp`{.literal} dependency packages:

        ``` {.language-plaintext tabindex="-1"}
        # dnf remove leapp-deps-el10 leapp-repository-deps-el10
        ```

3.  Optional: Remove all remaining upgrade-related data from the system:

    ``` {.language-plaintext tabindex="-1"}
    # rm -rf /var/log/leapp /root/tmp_leapp_py3 /var/lib/leapp
    ```

    Important

    Removing this data might limit Red Hat Support's ability to investigate and troubleshoot post-upgrade problems.

4.  Disable DNF repositories whose packages are not RHEL 10-compatible. Repositories managed by RHSM are handled automatically. To disable these repositories:

    ``` {.language-plaintext tabindex="-1"}
    # dnf config-manager --set-disabled <repository_id>
    ```

    Replace *repository_id* with the repository ID.

5.  Verify that the rescue kernel is present on the system:

    ``` {.language-plaintext tabindex="-1"}
    # ls /boot/vmlinuz*rescue* 2>/dev/null || echo "No rescue kernel installed."
    ```

    If the rescue kernel is present, replace the old rescue kernel and initial RAM disk with the current kernel and disk:

    a.  Install the `dracut-config-rescue`{.literal} RPM:

        ``` {.language-plaintext tabindex="-1"}
        # dnf -y install dracut-config-rescue
        ```

    b.  Remove the existing rescue kernel and initial RAM disk:

        ``` {.language-plaintext tabindex="-1"}
        # rm /boot/vmlinuz-*rescue* /boot/initramfs-*rescue* 
        ```

    c.  Reinstall the rescue kernel and related initial RAM disk:

        ``` {.language-plaintext tabindex="-1"}
        # /usr/lib/kernel/install.d/51-dracut-rescue.install add "$(uname -r)" /boot "/boot/vmlinuz-$(uname -r)"
        ```

    d.  If your system is on the IBM Z architecture, update the `zipl`{.literal} boot loader:

        ``` {.language-plaintext tabindex="-1"}
        # zipl
        ```

6.  Check existing configuration files:

    -   Review, remediate, and then remove the `rpmnew`{.literal}, `rpmsave`{.literal}, and `leappsave`{.literal} files. Note that `rpmsave`{.literal} and `leappsave`{.literal} are equivalent and can be handled similarly. For more information, see [What are rpmnew & rpmsave files?](https://access.redhat.com/solutions/60263)
    -   Remove configuration files for RHEL 9 DNF modules from the `/etc/dnf/modules.d/`{.literal} directory that are no longer valid. Note that these files have no effect on the system when related DNF modules do not exist.

7.  Re-evaluate and re-apply your security policies. Especially, change the SELinux mode to enforcing. For details, see [Applying security policies](#applying-security-policies "Chapter 8. Applying security policies").

**Verification**

1.  Verify that the previously removed rescue kernel and rescue initial RAM disk files have been created for the current kernel:

    ``` {.language-plaintext tabindex="-1"}
    # ls /boot/vmlinuz-*rescue* /boot/initramfs-*rescue* 
    # lsinitrd /boot/initramfs-*rescue*.img | grep -qm1 "$(uname -r)/kernel/" && echo "OK" || echo "FAIL"
    ```

2.  Verify the rescue boot entry refers to the existing rescue files. See the `grubby`{.literal} output:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --info /boot/vmlinuz-*rescue*
    ```

3.  Review the `grubby`{.literal} output and verify that no RHEL 9 boot entries are configured:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --info ALL
    ```

4.  Verify that no files related to previous RHEL are present in the `/boot/loader/entries`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # grep -r ".el9" "/boot/loader/entries/" || echo "Everything seems ok."
    ```

## [Chapter 8. Applying security policies](#applying-security-policies) {#chapter-8.-applying-security-policies .title}

During the in-place upgrade process, the Leapp utility must switch the SELinux policy to permissive mode. Furthermore, security profiles might contain changes between major releases.

To restore system security, switch SELinux to enforcing mode again. You might also want to remediate the system to be compliant with a specific security profile. Also, some security-related components require pre-update steps for a correct upgrade.

The in-place upgrade process preserves the system-wide cryptographic policy you used in RHEL 9. Custom cryptographic policies are also preserved across the in-place upgrade.

### [8.1. Changing SELinux mode to enforcing](#changing-selinux-mode-to-enforcing) {#changing-selinux-mode-to-enforcing .title}

During the in-place upgrade process, the Leapp utility sets SELinux mode to permissive. After you finish the system upgrade, you must manually change SELinux mode to enforcing.

**Prerequisites**

-   The system has been upgraded and you have performed the Verification described in [Verifying the post-upgrade state](#verifying-the-post-upgrade-state "Chapter 6. Verifying the post-upgrade state").

**Procedure**

1.  Ensure that there are no SELinux denials, for example, by using the `ausearch`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -m AVC,USER_AVC -ts boot
    ```

    Note that the previous step covers only the most common scenario. To check for all possible SELinux denials, see the [Identifying SELinux denials](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/troubleshooting-problems-related-to-selinux#identifying-selinux-denials) section in the Using SELinux title, which provides a complete procedure.

2.  Open the `/etc/selinux/config`{.literal} file in a text editor of your choice, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/selinux/config
    ```

3.  Configure the `SELINUX=enforcing`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # This file controls the state of SELinux on the system.
    # SELINUX= can take one of these three values:
    #       enforcing - SELinux security policy is enforced.
    #       permissive - SELinux prints warnings instead of enforcing.
    #       disabled - No SELinux policy is loaded.
    SELINUX=enforcing
    # SELINUXTYPE= can take one of these two values:
    #       targeted - Targeted processes are protected,
    #       mls - Multi Level Security protection.
    SELINUXTYPE=targeted
    ```

4.  Save the change, and restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

-   After the system restarts, confirm that the `getenforce`{.literal} command returns `Enforcing`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ getenforce
    Enforcing
    ```

**Additional resources**

-   [Troubleshooting problems related to SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/troubleshooting-problems-related-to-selinux)
-   [Changing SELinux states and modes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/getting-started-with-selinux#selinux-states-and-modes_getting-started-with-selinux)

### [8.2. Upgrading a system hardened to a security baseline](#upgrading-a-system-hardened-to-a-security-baseline) {#upgrading-a-system-hardened-to-a-security-baseline .title}

To get a fully hardened system after a successful upgrade to RHEL 10, you can use automated remediation provided by the OpenSCAP suite.

OpenSCAP remediations align your system with security baselines, such as PCI-DSS, OSPP, or ACSC Essential Eight. The configuration compliance recommendations differ among major versions of RHEL due to the evolution of the security offering.

When upgrading a hardened RHEL 9 system, the Leapp utility does *not* provide direct means to retain the full hardening. Depending on the changes in the component configuration, the system might diverge from the recommendations for RHEL 10 during the upgrade.

Note

You cannot use the same SCAP content for scanning RHEL 9 and RHEL 10. Update the management platforms if the compliance of the system is managed by tools such as Red Hat Satellite or Red Hat Lightspeed.

As an alternative to automated remediations, you can make the changes manually by following an OpenSCAP-generated report. For information about generating a compliance report, see [Scanning the system for configuration compliance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance).

Important

Automated remediations support RHEL systems in the default configuration. Because the system configuration has been altered after the upgrade, running automated remediations might not make the system fully compliant with the required security profile. You might need to fix some requirements manually.

The following example procedure hardens your system settings according to the PCI-DSS profile.

**Prerequisites**

-   The `scap-security-guide`{.literal} package is installed on your RHEL 10 system.

**Procedure**

1.  Find the appropriate security compliance data stream `.xml`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ ls /usr/share/xml/scap/ssg/content/
    …
    ssg-rhel10-ds.xml
    …
    ```

    See the [Viewing profiles for configuration compliance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#viewing-profiles-for-configuration-compliance) section for more information.

2.  Remediate the system according to the selected profile from the appropriate data stream:

    ``` {.language-plaintext tabindex="-1"}
    # oscap xccdf eval --profile <profile_ID> --remediate /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    Replace *`<profile_ID>`{.literal}* with the ID of the profile according to which you want to harden your system. For a full list of profiles supported in RHEL 10, see [SCAP Security Guide profiles supported in RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#scap-security-guide-profiles-supported-in-rhel-10).

    Warning

    If not used carefully, running the system evaluation with the `--remediate`{.literal} option enabled might render the system non-functional. Red Hat does not provide any automated method to revert changes made by security-hardening remediations. Remediations are supported on RHEL systems in the default configuration. If your system has been altered after the installation, running remediation might not make it compliant with the required security profile.

3.  Restart your system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

1.  Verify that the system is compliant with the profile, and save the results in an HTML file:

    ``` {.language-plaintext tabindex="-1"}
    $ oscap xccdf eval --report pcidss_report.html --profile pci-dss /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

**Additional resources**

-   [Scanning the system for configuration compliance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance)
-   [Red Hat Lightspeed Security Policy](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/assessing_and_monitoring_security_vulnerabilities_on_rhel_systems/index)
-   [Red Hat Satellite Security Policy](https://docs.redhat.com/en/documentation/red_hat_satellite/6.10/html/administering_red_hat_satellite/chap-administering-security_compliance_management)

## [Chapter 9. Troubleshooting](#troubleshooting) {#chapter-9.-troubleshooting .title}

The in-place upgrade is a complex process, and it is common to encounter issues and roadblocks. Refer to the following troubleshooting resources and tips for help on resolving these issues.

### [9.1. Troubleshooting resources](#troubleshooting-resources) {#troubleshooting-resources .title}

You can use various troubleshooting resources can help you diagnose and troubleshoot issues you encounter throughout the upgrade process.

**Console output**

By default, only error and critical log level messages are printed to the console output by the `Leapp`{.literal} utility. To change the log level, use the `--verbose`{.literal} or `--debug`{.literal} options with the `leapp upgrade`{.literal} command.

-   In *verbose* mode, `Leapp`{.literal} prints info, warning, error, and critical messages.
-   In *debug* mode, `Leapp`{.literal} prints debug, info, warning, error, and critical messages.

**Logs**

-   The `/var/log/leapp/leapp-upgrade.log`{.literal} file lists issues found during the initramfs phase.
-   The `/var/log/leapp/dnf-debugdata/`{.literal} directory contains transaction debug data. This directory is present only if the `leapp upgrade`{.literal} command is run with the `--debug`{.literal} option.
-   The `/var/log/leapp/answerfile`{.literal} contains questions required to be answered by `Leapp`{.literal}.
-   The `journalctl`{.literal} utility provides complete logs.

**Reports**

-   The `/var/log/leapp/leapp-report.txt`{.literal} file lists issues found during the pre-upgrade phase. The report is also available in the web console, see [Assessing upgradability and applying automated remediations through the web console](#assessing-upgradability-of-rhel-9-to-rhel-10-and-applying-automated-remediations-through-the-web-console "4.1.3. Assessing upgradability and applying automated remediations through the web console").
-   The `/var/log/leapp/leapp-report.json`{.literal} file lists issues found during the pre-upgrade phase in a machine-readable format, which enables you to process the report using custom scripts. For more information, see [Automating your Red Hat Enterprise Linux pre-upgrade report workflow](https://access.redhat.com/articles/5777571).

### [9.2. Troubleshooting tips](#troubleshooting-tips) {#troubleshooting-tips .title}

When diagnosing and troubleshooting issues that occur during the in-place upgrade process, make sure to check for these frequently skipped steps and use these helpful resources.

**Pre-upgrade phase**

-   Verify that your system meets all conditions listed in [Planning an upgrade](#planning-an-upgrade-to-rhel-10 "Chapter 2. Planning an upgrade to RHEL 10").

-   Make sure you have followed all steps described in [Preparing for the upgrade](#preparing-for-the-upgrade "Chapter 3. Preparing for the upgrade"), for example, your system does not use more than one Network Interface Card (NIC) with a name based on the prefix used by the kernel (`eth`{.literal}).

-   Make sure you have answered all questions required by `Leapp`{.literal} in the `/var/log/leapp/answerfile`{.literal} file. If any answers are missing, `Leapp`{.literal} inhibits the upgrade. For example:

    -   Are there no VDO devices on the system?

-   Make sure you have resolved all problems identified in the pre-upgrade report, located at `/var/log/leapp/leapp-report.txt`{.literal}. To achieve this, you can also use the web console, as described in [Assessing upgradability and applying automated remediations through the web console](#assessing-upgradability-of-rhel-9-to-rhel-10-and-applying-automated-remediations-through-the-web-console "4.1.3. Assessing upgradability and applying automated remediations through the web console").

**Example 9.1. Leapp answerfile**

The following is an example of an unedited `/var/log/leapp/answerfile`{.literal} file that has one unanswered question:

``` {.language-plaintext tabindex="-1"}
[check_vdo]
# Title:              None
# Reason:             Confirmation
# ============================= check_vdo.confirm =============================
# Label:              Are all VDO devices, if any, successfully converted to LVM management?
# Description:        Enter True if no VDO devices are present on the system or all VDO devices on the system have been successfully converted to LVM management. Entering True will circumvent check of failures and undetermined devices. Recognized VDO devices that have not been converted to LVM management can still block the upgrade despite the answer.All VDO devices must be converted to LVM management before upgrading.
# Reason:             To maximize safety all block devices on a system that meet the criteria as possible VDO devices are checked to verify that, if VDOs, they have been converted to LVM management. If the devices are not converted and the upgrade proceeds the data on unconverted VDO devices will be inaccessible. In order to perform checking the 'vdo' package must be installed. If the 'vdo' package is not installed and there are any doubts the 'vdo' package should be installed and the upgrade process re-run to check for unconverted VDO devices. If the check of any device fails for any reason an upgrade inhibiting report is generated. This may be problematic if devices are dynamically removed from the system subsequent to having been identified during device discovery. If it is certain that all VDO devices have been successfully converted to LVM management this dialog may be answered in the affirmative which will circumvent block device checking.
# Type:               bool
# Default:            None
# Available choices: True/False
# Unanswered question. Uncomment the following line with your answer
# confirm =
```

The `Label`{.literal} field specifies the question that requires an answer. In this example, the question is **Are all VDO devices, if any, successfully converted to LVM management?**

To answer the question, uncomment the last line and enter an answer of `True`{.literal} or `False`{.literal}. In this example, the selected answer is `True`{.literal}:

``` {.language-plaintext tabindex="-1"}
[check_vdo]
...
# Available choices: True/False
# Unanswered question. Uncomment the following line with your answer
confirm = True
```

**Download phase**

-   If a problem occurs during downloading RPM packages, examine transaction debug data located in the `/var/log/leapp/dnf-debugdata/`{.literal} directory.

    Note

    The `/var/log/leapp/dnf-debugdata/`{.literal} directory is empty or does not exist if no transaction debug data was produced. This might occur when the required repositories are not available.

**Initramfs phase**

-   During this phase, potential failures redirect you to the Dracut shell. Check the Journal log:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl
    ```

    Alternatively, restart the system from the Dracut shell using the `reboot`{.literal} command and check the `/var/log/leapp/leapp-upgrade.log`{.literal} file.

**Post-upgrade phase**

-   If your system seems to be successfully upgraded but booted with the old RHEL 9 kernel, restart the system and check the kernel version of the default entry in GRUB.

-   Make sure you have followed the recommended steps in [Verifying the post-upgrade state](#verifying-the-post-upgrade-state "Chapter 6. Verifying the post-upgrade state").

-   If your application or a service stops working or behaves incorrectly after you have switched SELinux to enforcing mode, search for denials using the `ausearch`{.literal}, `journalctl`{.literal}, or `dmesg`{.literal} utilities:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -m AVC,USER_AVC -ts boot
    # journalctl -t setroubleshoot
    # dmesg | grep -i -e selinux -e type=1400
    ```

    The most common problems are caused by incorrect labeling. See [Troubleshooting problems related to SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/troubleshooting-problems-related-to-selinux) for more details.

### [9.3. Known issues for the RHEL 9.8 to RHEL 10.2 upgrade](#known-issues-for-the-rhel-9-to-rhel-10-upgrade) {#known-issues-for-the-rhel-9.8-to-rhel-10.2-upgrade .title}

There are a variety of known issues that you might encounter when upgrading from RHEL 9.8 to RHEL 10.2.

-   If your RHEL 9 system uses a device driver that is provided by Red Hat but is not available in RHEL 10, `Leapp`{.literal} inhibits the upgrade. However, if the RHEL 9 system uses a third-party device driver that `Leapp`{.literal} does not have data for in the `/etc/leapp/files/device_driver_deprecation_data.json`{.literal} file, `Leapp`{.literal} does not detect such a driver and proceeds with the upgrade. Consequently, the system might fail to boot after the upgrade.

-   If the name of a third-party package, not signed by Red Hat, installed on your system is the same as the name of a package provided by Red Hat, the in-place upgrade fails. To work around this problem, choose one of the following options prior to upgrading:

    a.  Remove the third-party package
    b.  Replace the third-party package with the package provided by Red Hat

-   The in-place upgrade might fail on systems with Software Redundant Array of Independent Disks (RAID). (BZ#[1957192](https://bugzilla.redhat.com/show_bug.cgi?id=1957192))

-   If any of the mounted file systems that are defined in the `/etc/fstab`{.literal} file do not have the `shared`{.literal} propagation flag set, the upgrade might fail. To prevent this issue, remount these file systems to set them as shared:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o remount --make-shared <mountpoint>
    ```

    Replace *mountpoint* with the mountpoint of each file system.

    For more information, see the Red Hat Knowledgebase solution [Leapp \"Cannot load RPM file\" during the DNF transaction check](https://access.redhat.com/solutions/7052390). ([RHEL-23449](https://issues.redhat.com/browse/RHEL-23449))

-   If you use an HTTP proxy, you must configure Red Hat Subscription Manager (RHSM) to use such a proxy, or you must run the `subscription-manager`{.literal} command with the `--proxy <hostname>`{.literal} option. Otherwise, an execution of the `subscription-manager`{.literal} command fails. If you use the `--proxy`{.literal} option instead of the configuration change, the upgrade process fails because `Leapp`{.literal} is unable to detect the proxy. To prevent this problem from occurring, manually edit the `rhsm.conf`{.literal} file. For more information, see the Red Hat Knowledgebase solution [How to configure HTTP Proxy for Red Hat Subscription Management](https://access.redhat.com/solutions/57669). (BZ#[1689294](https://bugzilla.redhat.com/show_bug.cgi?id=1689294))

-   For systems that require a proxy to access RHEL 9 content, you usually need to configure the use of the proxy by DNF in the `/etc/dnf/dnf.conf`{.literal} configuration file. If the current DNF configuration is not compatible with the DNF version on the target system, specify the valid target configuration in the `/etc/leapp/files/dnf.conf`{.literal} configuration file. For more information, see the Red Hat Knowledgebase solution [How does Leapp work with a proxy?](https://access.redhat.com/node/7073762)

-   The upgrade might fail if you are upgrading by using Red Hat Update Infrastructure (RHUI) with an ISO image. You can work around this issue by not using the `--iso`{.literal} option with the upgrade or see the Red Hat Knowledgebase solution [Offline Leapp upgrade using ISO fails with \"Failed to synchronize cache for repo \'rhul-microsoft-azure-rhel8\', ignoring this repo](https://access.redhat.com/solutions/7031554). ([RHEL-3296](https://issues.redhat.com/browse/RHEL-3296))

-   If you are upgrading by using Red Hat Update Infrastructure (RHUI), files in the `/usr/share/leapp-repository/repositories/system_upgrade/common/files/rhui/`{.literal} directory are incorrectly reported as custom files in the pre-upgrade report. Unless you modified these files manually, you can ignore the warnings about these files in the report and the in-place upgrade will not be affected. ([RHEL-40115](https://issues.redhat.com/browse/RHEL-40115))

-   When upgrading systems by using Red Hat Upgrade Infrastructure (RHUI), the upgrade could fail if the RHUI setup of the system differs from defaults implemented in the in-place upgrade solution RHUI systems expected by the `Leapp`{.literal} utility. To resolve this problem, configure the upgrade process to adjust it for your RHUI setup. For more information, see [Using RHUI to configure an in-place upgrade](https://access.redhat.com/articles/7115872).

-   The upgrade might fail on systems with multiple LUKS devices. For more information about the issue and possible workaround, see [leapp upgrade fails when LUKS devices are present even though TPM2 is used to decrypt them](https://access.redhat.com/solutions/7137280). ([RHEL-145136](https://redhat.atlassian.net/browse/RHEL-145136))

-   The upgrade might fail on systems with installed Identity Management packages. To work around this problem, complete the following steps:

    1.  Add the following packages to the `/etc/leapp/transaction/to_remove`{.literal} file:

        -   `tomcat-servlet-4.0-api`{.literal}
        -   `tomcat-el-3.0-api`{.literal}
        -   `tomcat-jsp-2.3-api`{.literal}
        -   `tomcat-lib`{.literal}
        -   `tomcat`{.literal}
        -   `tomcat-admin-webapps`{.literal}
        -   `tomcat-docs-webapp`{.literal}
        -   `tomcat-webapps`{.literal}

    2.  Add the following packages to the `/etc/leapp/transaction/to_install`{.literal} file:

        -   `tomcat9`{.literal}
        -   `tomcat9-el-3.0-api`{.literal}
        -   `tomcat9-jsp-2.3-api`{.literal}
        -   `tomcat9-lib`{.literal}
        -   `tomcat9-servlet-4.0-api`{.literal}

    ([RHEL-164811](https://redhat.atlassian.net/browse/RHEL-164811))

### [9.4. Known issues for the RHEL 9.6 to RHEL 10.0 upgrade](#known-issues-for-the-rhel-9.6-to-rhel-10.0-upgrade) {#known-issues-for-the-rhel-9.6-to-rhel-10.0-upgrade .title}

There are a variety of known issues that you might encounter when upgrading from RHEL 9.6 to RHEL 10.1.

-   If your RHEL 9 system uses a device driver that is provided by Red Hat but is not available in RHEL 10, `Leapp`{.literal} inhibits the upgrade. However, if the RHEL 9 system uses a third-party device driver that `Leapp`{.literal} does not have data for in the `/etc/leapp/files/device_driver_deprecation_data.json`{.literal} file, `Leapp`{.literal} does not detect such a driver and proceeds with the upgrade. Consequently, the system might fail to boot after the upgrade.

-   If the name of a third-party package, not signed by Red Hat, installed on your system is the same as the name of a package provided by Red Hat, the in-place upgrade fails. To work around this problem, choose one of the following options prior to upgrading:

    a.  Remove the third-party package
    b.  Replace the third-party package with the package provided by Red Hat

-   The in-place upgrade might fail on systems with Software Redundant Array of Independent Disks (RAID). (BZ#[1957192](https://bugzilla.redhat.com/show_bug.cgi?id=1957192))

-   During the in-place upgrade, the `Leapp`{.literal} utility usually preserves the network interface controller (NIC) names between RHEL 9 and RHEL 10. However, on some systems, such as systems with network bonding, the NIC names might need to be updated between RHEL 9 and RHEL 10. On those systems, perform the following steps:

    a.  Set the `LEAPP_NO_NETWORK_RENAMING=1`{.literal} environment variable to prevent the Leapp utility from incorrectly preserving the original RHEL 9 NIC names.

    b.  Perform the in-place upgrade.

    c.  Verify that your network is working correctly. If needed, manually update the network configuration.

        (BZ#[1919382](https://bugzilla.redhat.com/show_bug.cgi?id=1919382))

-   If any of the mounted file systems that are defined in the `/etc/fstab`{.literal} file do not have the `shared`{.literal} propagation flag set, the upgrade might fail. To prevent this issue, remount these file systems to set them as shared:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o remount --make-shared <mountpoint>
    ```

    Replace *mountpoint* with the mountpoint of each file system.

    For more information, see the Red Hat Knowledgebase solution [Leapp \"Cannot load RPM file\" during the DNF transaction check](https://access.redhat.com/solutions/7052390). ([RHEL-23449](https://issues.redhat.com/browse/RHEL-23449))

-   If you use an HTTP proxy, Red Hat Subscription Manager must be configured to use such a proxy, or the `subscription-manager`{.literal} command must be run with the `--proxy <hostname>`{.literal} option. Otherwise, an execution of the `subscription-manager`{.literal} command fails. If you use the `--proxy`{.literal} option instead of the configuration change, the upgrade process fails because `Leapp`{.literal} is unable to detect the proxy. To prevent this problem from occurring, manually edit the `rhsm.conf`{.literal} file. For more information, see the Red Hat Knowledgebase solution [How to configure HTTP Proxy for Red Hat Subscription Management](https://access.redhat.com/solutions/57669). (BZ#[1689294](https://bugzilla.redhat.com/show_bug.cgi?id=1689294))
-   For systems that require a proxy to access RHEL 9 content, you usually need to configure the use of the proxy by DNF in the `/etc/dnf/dnf.conf`{.literal} configuration file. If the current DNF configuration is not compatible with the DNF version on the target system, specify the valid target configuration in the `/etc/leapp/files/dnf.conf`{.literal} configuration file. For more information, see the Red Hat Knowledgebase solution [How does Leapp work with a proxy?](https://access.redhat.com/node/7073762)

-   The kerberos client might break after the upgrade if it is configured to use the deprecated `/etc/ssl/certs/ca-certificates.crt`{.literal} file for root certificates. To fix the configuration, use the `/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem`{.literal} file instead. ([RHEL-65265](https://issues.redhat.com/browse/RHEL-65265))

-   On IBM Z machines, the upgrade might fail if the system is on multipath LVM SCSI LUNs. ([RHEL-76159](https://issues.redhat.com/browse/RHEL-76159))

-   If `dracut`{.literal} is configured to include the deprecated `network-legacy`{.literal} module, the system does not boot after the upgrade. This issue often occurs on systems that have been in-place upgraded to RHEL 9. To prevent this problem, perform the following actions:

    a.  Remove the `network-legacy`{.literal} module from the `dracut`{.literal} configuration.

    b.  Rebuild existing initramfs images.

    c.  Reboot the system before you start the upgrade.

        For more information see the [leapp upgrade fails to boot after upgrading to RHEL 10.0](https://access.redhat.com/solutions/7127576) Knowledgebase solution.

        ([RHEL-102591](https://issues.redhat.com/browse/RHEL-102591))

-   The upgrade might fail on systems with multiple LUKS devices. For more information about the issue and possible workaround, see [leapp upgrade fails when LUKS devices are present even though TPM2 is used to decrypt them](https://access.redhat.com/solutions/7137280). ([RHEL-145136](https://redhat.atlassian.net/browse/RHEL-145136))

### [9.5. Obtaining support](#obtaining-support) {#obtaining-support .title}

To open a support case, select *RHEL 9* as the product, and provide a `sosreport`{.literal} from your system.

-   To generate a `sosreport`{.literal} on your system, run:

``` {.language-plaintext tabindex="-1"}
# sosreport
```

Note that you can leave the case ID empty.

For more information about generating a sosreport, see the Red Hat Knowledgebase solution [What is an sosreport and how to create one in Red Hat Enterprise Linux?](https://access.redhat.com/solutions/3592).

For more information about opening and managing a support case on the Customer Portal, see the Red Hat Knowledgebase solution, [How do I open and manage a support case on the Customer Portal?](https://access.redhat.com/articles/38363).

## [Chapter 10. Related information](#related-information) {#chapter-10.-related-information .title}

You can refer to the following instructional materials:

-   [Upgrade your Red Hat Enterprise Linux Infrastructure](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux/upgrade-rhel)
-   [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits)
-   [Supported in-place upgrade paths for Red Hat Enterprise Linux](https://access.redhat.com/articles/4263361)
-   [In-place upgrade Support Policy](https://access.redhat.com/support/policy/ipu-support)
-   [Considerations in adopting RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/considerations_in_adopting_rhel_10/)
-   [Customizing your Red Hat Enterprise Linux in-place upgrade](https://access.redhat.com/articles/4977891)
-   [Automating your Red Hat Enterprise Linux pre-upgrade report workflow](https://access.redhat.com/articles/5777571)
-   [Using configuration management systems to automate parts of the Leapp pre-upgrade and upgrade process on Red Hat Enterprise Linux](https://access.redhat.com/articles/6313281)
-   [Upgrading from RHEL 8 to RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/upgrading_from_rhel_8_to_rhel_9/)
-   [Red Hat Lightspeed Documentation](https://docs.redhat.com/en/documentation/red_hat_lightspeed)
-   [Upgrades-related Knowledgebase articles and solutions](https://access.redhat.com/solutions/4120411) (Red Hat Knowledgebase)
-   [The best practices and recommendations for performing RHEL Upgrade using Leapp](https://access.redhat.com/articles/7012979)
-   [Leapp upgrade FAQ (Frequently Asked Questions)](https://access.redhat.com/articles/7013172)

## [Appendix A. RHEL 9 repositories](#appendix-rhel-9-repositories) {#appendix-a.-rhel-9-repositories .title}

If your system is registered to the Red Hat Content Delivery Network (CDN) using the Red Hat Subscription Manager (RHSM), RHEL 9 repositories are automatically enabled during the in-place upgrade.

However, on systems registered to Red Hat Satellite using RHSM, you must manually enable and synchronize both RHEL 9 and RHEL 10 repositories before running the pre-upgrade report.

Note

Make sure to enable the source OS version of each repository, for example 9.6. If you have enabled only the RHEL 9 version of the repositories, the in-place upgrade is inhibited.

If you plan to use Red Hat Satellite during the upgrade, you must enable and synchronize at least the following RHEL 9 repositories before the upgrade using either the Satellite web UI or the `hammer repository-set enable`{.literal} and `hammer product synchronize`{.literal} commands:

+---------------------------+-------------+-----------------------------------------------+------------------------------------------------------------------------+---------------------------------+
| Architecture              | Repository  | Repository ID                                 | Repository name                                                        | Release version                 |
+:==========================+:============+:==============================================+:=======================================================================+:================================+
| 64-bit Intel and AMD      | BaseOS      | `rhel-9-for-x86_64-baseos-rpms`{.literal}     | Red Hat Enterprise Linux 9 for x86_64 - BaseOS (RPMs)                  | x86_64 *\<source_os_version\>*  |
+---------------------------+-------------+-----------------------------------------------+------------------------------------------------------------------------+---------------------------------+
|                           | AppStream   | `rhel-9-for-x86_64-appstream-rpms`{.literal}  | Red Hat Enterprise Linux 9 for x86_64 - AppStream (RPMs)               | x86_64 *\<source_os_version\>*  |
+---------------------------+-------------+-----------------------------------------------+------------------------------------------------------------------------+---------------------------------+
| 64-bit ARM                | BaseOS      | `rhel-9-for-aarch64-baseos-rpms`{.literal}    | Red Hat Enterprise Linux 9 for ARM 64 - BaseOS (RPMs)                  | aarch64 *\<source_os_version\>* |
+---------------------------+-------------+-----------------------------------------------+------------------------------------------------------------------------+---------------------------------+
|                           | AppStream   | `rhel-9-for-aarch64-appstream-rpms`{.literal} | Red Hat Enterprise Linux 9 for ARM 64 - AppStream (RPMs)               | aarch64 *\<source_os_version\>* |
+---------------------------+-------------+-----------------------------------------------+------------------------------------------------------------------------+---------------------------------+
| IBM Power (little endian) | BaseOS      | `rhel-9-for-ppc64le-baseos-rpms`{.literal}    | Red Hat Enterprise Linux 9 for Power, little endian - BaseOS (RPMs)    | ppc64le *\<source_os_version\>* |
+---------------------------+-------------+-----------------------------------------------+------------------------------------------------------------------------+---------------------------------+
|                           | AppStream   | `rhel-9-for-ppc64le-appstream-rpms`{.literal} | Red Hat Enterprise Linux 9 for Power, little endian - AppStream (RPMs) | ppc64le *\<source_os_version\>* |
+---------------------------+-------------+-----------------------------------------------+------------------------------------------------------------------------+---------------------------------+
| IBM Z                     | BaseOS      | `rhel-9-for-s390x-baseos-rpms`{.literal}      | Red Hat Enterprise Linux 9 for IBM z Systems - BaseOS (RPMs)           | s390x *\<source_os_version\>*   |
+---------------------------+-------------+-----------------------------------------------+------------------------------------------------------------------------+---------------------------------+
|                           | AppStream   | `rhel-9-for-s390x-appstream-rpms`{.literal}   | Red Hat Enterprise Linux 9 for IBM z Systems - AppStream (RPMs)        | s390x *\<source_os_version\>*   |
+---------------------------+-------------+-----------------------------------------------+------------------------------------------------------------------------+---------------------------------+

: Table A.1. RHEL 9 repositories

Show more

Replace *\<source_os_version\>* with the source OS version, for example `9.6`{.literal}.

## [Appendix B. RHEL 10 repositories](#appendix-rhel-10-repositories) {#appendix-b.-rhel-10-repositories .title}

If your system is registered to the Red Hat Content Delivery Network (CDN) by using the Red Hat Subscription Manager (RHSM), RHEL 10 repositories are automatically enabled during the in-place upgrade.

However, on systems registered to Red Hat Satellite by using RHSM, you must manually enable and synchronize both RHEL 9 and RHEL 10 repositories before running the pre-upgrade report.

Note

Make sure to enable the target OS version of each repository, for example 10.0. If you have enabled only the RHEL 10 version of the repositories, the in-place upgrade is inhibited.

If you plan to use Red Hat Satellite during the upgrade, you must enable and synchronize at least the following RHEL 10 repositories before the upgrade by using either the Satellite web UI or the `hammer repository-set enable`{.literal} and `hammer product synchronize`{.literal} commands:

+---------------------------+-------------+------------------------------------------------+-------------------------------------------------------------------------+---------------------------------+
| Architecture              | Repository  | Repository ID                                  | Repository name                                                         | Release version                 |
+:==========================+:============+:===============================================+:========================================================================+:================================+
| 64-bit Intel and AMD      | BaseOS      | `rhel-10-for-x86_64-baseos-rpms`{.literal}     | Red Hat Enterprise Linux 10 for x86_64 - BaseOS (RPMs)                  | x86_64 *\<target_os_version\>*  |
+---------------------------+-------------+------------------------------------------------+-------------------------------------------------------------------------+---------------------------------+
|                           | AppStream   | `rhel-10-for-x86_64-appstream-rpms`{.literal}  | Red Hat Enterprise Linux 10 for x86_64 - AppStream (RPMs)               | x86_64 *\<target_os_version\>*  |
+---------------------------+-------------+------------------------------------------------+-------------------------------------------------------------------------+---------------------------------+
| 64-bit ARM                | BaseOS      | `rhel-10-for-aarch64-baseos-rpms`{.literal}    | Red Hat Enterprise Linux 10 for ARM 64 - BaseOS (RPMs)                  | aarch64 *\<target_os_version\>* |
+---------------------------+-------------+------------------------------------------------+-------------------------------------------------------------------------+---------------------------------+
|                           | AppStream   | `rhel-10-for-aarch64-appstream-rpms`{.literal} | Red Hat Enterprise Linux 10 for ARM 64 - AppStream (RPMs)               | aarch64 *\<target_os_version\>* |
+---------------------------+-------------+------------------------------------------------+-------------------------------------------------------------------------+---------------------------------+
| IBM Power (little endian) | BaseOS      | `rhel-10-for-ppc64le-baseos-rpms`{.literal}    | Red Hat Enterprise Linux 10 for Power, little endian - BaseOS (RPMs)    | ppc64le *\<target_os_version\>* |
+---------------------------+-------------+------------------------------------------------+-------------------------------------------------------------------------+---------------------------------+
|                           | AppStream   | `rhel-10-for-ppc64le-appstream-rpms`{.literal} | Red Hat Enterprise Linux 10 for Power, little endian - AppStream (RPMs) | ppc64le *\<target_os_version\>* |
+---------------------------+-------------+------------------------------------------------+-------------------------------------------------------------------------+---------------------------------+
| IBM Z                     | BaseOS      | `rhel-10-for-s390x-baseos-rpms`{.literal}      | Red Hat Enterprise Linux 10 for IBM z Systems - BaseOS (RPMs)           | s390x *\<target_os_version\>*   |
+---------------------------+-------------+------------------------------------------------+-------------------------------------------------------------------------+---------------------------------+
|                           | AppStream   | `rhel-10-for-s390x-appstream-rpms`{.literal}   | Red Hat Enterprise Linux 10 for IBM z Systems - AppStream (RPMs)        | s390x *\<target_os_version\>*   |
+---------------------------+-------------+------------------------------------------------+-------------------------------------------------------------------------+---------------------------------+

: Table B.1. RHEL 10 repositories

Show more

Replace *\<target_os_version\>* with the target OS version, for example `10.0`{.literal}.

## [Legal Notice](#idm140084711943584) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
