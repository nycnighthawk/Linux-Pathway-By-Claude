---
{"title": "Using SELinux", "guide": "using_selinux", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_selinux/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Using SELinux {#using-selinux .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Prevent users and processes from performing unauthorized interactions with files and devices by using Security-Enhanced Linux (SELinux) {#prevent-users-and-processes-from-performing-unauthorized-interactions-with-files-and-devices-by-using-security-enhanced-linux-selinux .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140601391755040)

**Abstract**

By configuring SELinux, you can enhance your system's security. SELinux is an implementation of Mandatory Access Control (MAC), and provides an additional layer of security. The SELinux policy defines how users and processes can interact with the files on the system. You can control which users can perform which actions by mapping them to specific SELinux confined users.

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

## [Chapter 1. Getting started with SELinux](#getting-started-with-selinux) {#chapter-1.-getting-started-with-selinux .title}

Enhance your system's security by understanding the core concepts of Security Enhanced Linux (SELinux). Knowledge of the SELinux architecture, packages, and operation modes helps to manage your system policies effectively.

### [1.1. Introduction to SELinux](#introduction-to-selinux) {#introduction-to-selinux .title}

Security Enhanced Linux (SELinux) is an implementation of Mandatory Access Control (MAC) that strengthens system security. By enforcing granular policies restricting process interactions with files and network resources, SELinux mitigates compromised applications and prevents unauthorized access.

Standard Discretionary Access Control (DAC) bases access policies on user, group, and other permissions. This model prevents system administrators from creating fine-grained security policies. For example, DAC cannot restrict specific applications to only view log files while allowing other applications to append data to the same log files.

SELinux adds an additional layer of protection by enforcing Mandatory Access Control (MAC) policies. These policies answer the question: *May \<subject\> do \<action\> to \<object\>?* For example: *May a web server access files in users\' home directories?*

Every process and system resource has a special security label called an *SELinux context*. An SELinux context, sometimes referred to as an *SELinux label*, is an identifier that abstracts system-level details to focus on the security properties of the entity. This identifier provides a consistent way to reference objects in the SELinux policy and removes ambiguity found in other identification methods. For example, a file can have multiple valid path names on a system that uses bind mounts.

The SELinux policy uses the contexts in rules that define how processes interact with system resources. By default, the policy denies all interaction unless a rule explicitly grants access.

For more information, refer to `selinux(8)`{.literal} man page and man pages listed by the `man -k selinux`{.literal} command when the `selinux-policy-doc`{.literal} package is installed on your system.

Note

SELinux policy rules are checked after DAC rules. If DAC rules deny access, SELinux policy rules are not evaluated, and no SELinux denial is logged.

SELinux contexts have four fields: user, role, type, and security level. The type field is the most important for the SELinux policy. Most policy rules that define allowed interactions between processes and system resources use SELinux types rather than the full SELinux context. SELinux types end with `_t`{.literal}. For example, the type context for the web server is `httpd_t`{.literal}. Files and directories in `/var/www/html/`{.literal} use the `httpd_sys_content_t`{.literal} type. Files and directories in `/tmp`{.literal} and `/var/tmp/`{.literal} use `tmp_t`{.literal}. The type for web server ports is `http_port_t`{.literal}.

A policy rule permits Apache (the web server process running as `httpd_t`{.literal}) to access files and directories with a context normally found in `/var/www/html/`{.literal} and other web server directories (`httpd_sys_content_t`{.literal}). No allow rule exists in the policy for files normally found in `/tmp`{.literal} and `/var/tmp/`{.literal}, so access is not permitted. With SELinux, even if Apache is compromised and a malicious script gains access, it still cannot access the `/tmp`{.literal} directory.

**Figure 1.1. An example how can SELinux help to run Apache and MariaDB in a secure way.**

As the previous scheme shows, SELinux allows the Apache process running as `httpd_t`{.literal} to access the `/var/www/html/`{.literal} directory. It denies access to `/data/mysql/`{.literal} because no allow rule exists for the `httpd_t`{.literal} and `mysqld_db_t`{.literal} type contexts. Conversely, the MariaDB process running as `mysqld_t`{.literal} accesses `/data/mysql/`{.literal} but is denied access to `/var/www/html/`{.literal}, which is labeled as `httpd_sys_content_t`{.literal}.

**Additional resources**

-   [The SELinux Coloring Book](https://people.redhat.com/duffy/selinux/selinux-coloring-book_A4-Stapled.pdf)

### [1.2. Benefits of running SELinux](#benefits-of-running-selinux) {#benefits-of-running-selinux .title}

Use Security Enhanced Linux (SELinux) to reduce privilege escalation attacks and enforce data confidentiality. SELinux restricts how processes interact with files and system resources. This limits the impact of compromised applications.

Running SELinux provides the following security benefits:

-   All processes and files are labeled. SELinux policy rules define how processes interact with files and with each other. Access is allowed only if an SELinux policy rule allows it.
-   SELinux provides fine-grained access control. Traditional UNIX permissions use Linux user and group IDs. SELinux goes beyond this. SELinux uses all available information: user, role, type, and security level.
-   SELinux policy is defined by administrators and enforced system-wide.
-   SELinux can reduce privilege escalation attacks. Processes run in domains. This separates them from each other. SELinux policy rules define how processes access files and other processes. If a process is compromised, the attacker can only access that process's normal functions. They can only access files that the process is configured to access. For example, if the Apache HTTP Server is compromised, an attacker cannot read files in user home directories. The only exception is if you add a specific SELinux policy rule to allow it.
-   SELinux can enforce data confidentiality and integrity, and can protect processes from untrusted inputs.

SELinux enhances existing security solutions. It does not replace them. You still need antivirus software, secure passwords, and firewalls. When you run SELinux, continue to follow good security practices. Keep software up to date. Use strong passwords. Use firewalls.

### [1.3. SELinux examples](#selinux-examples) {#selinux-examples .title}

Security-Enhanced Linux (SELinux) provides benefits in many real scenarios. Real-world examples show how SELinux stops privilege attacks, config errors, and common bugs through process isolation and user limits.

SELinux adds security in several ways:

-   **The default action is deny.** If no SELinux policy rule allows access, SELinux blocks it. For example, if a policy does not allow a process to open a file, access is denied.
-   **Confined users have fewer rights.** You can map Linux users to confined SELinux users to apply security rules. For example, mapping a Linux user to `user_u`{.literal} stops that user from running `sudo`{.literal} and `su`{.literal}.
-   **SELinux *domains* increase process and data separation.** Use domains to define which processes can access specific files and directories. For example, an attacker who compromises a Samba server cannot access files used by MariaDB databases.
-   **SELinux stops config errors.** Attackers can exploit Domain Name System (DNS) zone transfers to inject false data. If you run Berkeley Internet Name Domain (BIND) as a DNS server on RHEL without limits on zone transfers, SELinux protects your system. The default policy stops the `named`{.literal} daemon and other processes from using zone transfers to update zone files [^\[1\]^](#ftn.idm140601403333584).
-   **SELinux stops path traversal attacks.** Attackers can exploit Apache bugs to access files using `../`{.literal}. SELinux in enforcing mode stops the `httpd`{.literal} process from accessing files outside its allowed paths.
-   **SELinux prevents kernel NULL pointer attacks.** Attackers can exploit a vulnerability in the `mmap`{.literal} function to place code on a null page (CVE-2019-9213). SELinux in enforcing mode prevents this attack.
-   **SELinux prevents \*PTRACE_TRACEME** exploits.\* You can use the `deny_ptrace`{.literal} boolean to protect your systems from the **PTRACE_TRACEME** vulnerability (CVE-2019-13272). This blocks attackers from gaining root access.
-   **SELinux prevents NFS misconfigurations.** Use the `nfs_export_all_rw`{.literal} and `nfs_export_all_ro`{.literal} booleans to prevent Network File System (NFS) misconfigurations. For example, SELinux can prevent accidentally sharing `/home`{.literal} directories.

**Additional resources**

-   [SELinux as a security pillar of an operating system - Real-world benefits and examples](https://access.redhat.com/articles/6964380)
-   [SELinux hardening with Ansible](https://access.redhat.com/articles/7047896)
-   [Ansible playbooks for SELinux hardening](https://github.com/fedora-selinux/selinux-playbooks)

\

------------------------------------------------------------------------

[^\[1\]^](#idm140601403333584) Text files that include DNS data, such as hostname to IP address mappings.

### [1.4. SELinux architecture and packages](#selinux-architecture-and-packages) {#selinux-architecture-and-packages .title}

The SELinux kernel subsystem enforces security policies and the `systemd`{.literal} daemon strengthens access control to protect system services. Identify the packages required to install and maintain SELinux to ensure you have the necessary utilities for administration.

SELinux is a Linux Security Module (LSM) built into the Linux kernel. It enforces security policies, which you manage, to control access. SELinux intercepts access requests and checks them against the loaded policy. If the policy permits the request, SELinux allows the action. Otherwise, SELinux blocks the action and reports an error.

SELinux caches decisions, such as allowing or denying access, in the Access Vector Cache (AVC). This cache improves performance by reducing policy rule checks. SELinux policy rules apply only if Discretionary Access Control (DAC) rules allow access first. SELinux logs audit messages to `/var/log/audit/audit.log`{.literal} using the `type=AVC`{.literal} identifier.

In RHEL 10, the `systemd`{.literal} daemon manages system services; `systemd`{.literal} starts and stops all services, and users and processes communicate with `systemd`{.literal} by using the `systemctl`{.literal} utility. The `systemd`{.literal} daemon checks the SELinux policy and verifies the labels of the calling process and the unit file to authorize access. This approach strengthens access control to critical system capabilities, such as starting and stopping system services.

The `systemd`{.literal} daemon also acts as an SELinux Access Manager. It retrieves the label of the process running `systemctl`{.literal} or sending a `D-Bus`{.literal} message. The daemon then looks up the label of the unit file that the process wanted to configure. Finally, `systemd`{.literal} queries the kernel to determine if the policy allows the specific access between the process label and the unit file label. This confinement restricts compromised applications. Policy writers can also use these controls to confine administrators.

If the SELinux policy denies `D-Bus`{.literal} communication between two processes, the system logs a `USER_AVC`{.literal} denial message and the communication times out. `D-Bus`{.literal} communication is bidirectional.

Important

To avoid incorrect SELinux labeling and subsequent problems, ensure that you start services by using a `systemctl start`{.literal} command.

RHEL 10 provides the following packages for working with SELinux:

-   policies: `selinux-policy-targeted`{.literal}, `selinux-policy-mls`{.literal}
-   tools: `policycoreutils`{.literal}, `policycoreutils-gui`{.literal}, `libselinux-utils`{.literal}, `policycoreutils-python-utils`{.literal}, `setools-console`{.literal}, `checkpolicy`{.literal}

### [1.5. SELinux states and modes](#selinux-states-and-modes) {#selinux-states-and-modes .title}

Enforcing, permissive, and disabled SELinux modes help effectively manage system security. You can use these states to enforce policies or troubleshoot access denials without disrupting system operations.

SELinux can run in one of three modes: enforcing, permissive, or disabled.

-   Enforcing mode is the default, and recommended, mode of operation; in enforcing mode SELinux operates normally, enforcing the loaded security policy on the entire system.
-   In permissive mode, the system acts as if SELinux is enforcing the loaded security policy. This includes labeling objects and logging access denials. However, the system does not actually deny any operations. While not recommended for production systems, permissive mode can be helpful for SELinux policy development and debugging.
-   Disabled mode is strongly discouraged. The system avoids enforcing the SELinux policy and does not label persistent objects such as files. This makes it difficult to enable SELinux in the future.

Use the `setenforce`{.literal} utility to change between enforcing and permissive mode. Changes made with `setenforce`{.literal} do not persist across reboots. To change to enforcing mode, enter the `setenforce 1`{.literal} command as the Linux root user. To change to permissive mode, enter the `setenforce 0`{.literal} command. Use the `getenforce`{.literal} utility to view the current SELinux mode:

``` {.language-plaintext tabindex="-1"}
# getenforce
Enforcing
```

``` {.language-plaintext tabindex="-1"}
# setenforce 0
# getenforce
Permissive
```

``` {.language-plaintext tabindex="-1"}
# setenforce 1
# getenforce
Enforcing
```

In Red Hat Enterprise Linux, you can set individual domains to permissive mode while the system runs in enforcing mode. For example, to make the *httpd_t* domain permissive:

``` {.language-plaintext tabindex="-1"}
# semanage permissive -a httpd_t
```

Note that permissive domains are a powerful tool that can compromise security of your system. Red Hat recommends to use permissive domains with caution, for example, when debugging a specific scenario.

## [Chapter 2. Changing SELinux states and modes](#changing-selinux-states-and-modes) {#chapter-2.-changing-selinux-states-and-modes .title}

Configure SELinux to run in enforcing, permissive, or disabled mode to control how the system enforces security policies. You can apply these states permanently or at boot time to troubleshoot access denials and ensure file systems are correctly labeled when enabling SELinux.

When enabled, SELinux can run in one of two modes: enforcing or permissive. By default, SELinux is enabled and runs in enforcing mode. Disabling SELinux or setting it to permissive mode prevents SELinux from protecting the system. Changing SELinux status by using the `setenforce`{.literal} command is temporary and reverts after restart. To permanently change SELinux status, you must change SELinux configuration files or kernel parameters.

### [2.1. Permanent changes in SELinux states and modes](#permanent-changes-in-selinux-states-and-modes) {#permanent-changes-in-selinux-states-and-modes .title}

SELinux modes determine how the system enforces security policies and logs access violations. Configuring the correct mode maintains system security and prevents boot failures caused by file system relabeling when enabling SELinux from a disabled state.

SELinux operates in an enabled or disabled state. When enabled, SELinux runs in enforcing or permissive mode. The `getenforce`{.literal} command reports the current mode as `Enforcing`{.literal}, `Permissive`{.literal}, or `Disabled`{.literal}.

The `sestatus`{.literal} command reports the SELinux status and information about the loaded SELinux policy, for example:

``` {.language-plaintext tabindex="-1"}
$ sestatus
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      31
```

Warning

When systems run SELinux in permissive mode, users and processes might label file system objects incorrectly. File system objects created while SELinux is disabled are not labeled at all. This behavior causes problems when changing to enforcing mode because SELinux relies on correct labels of file system objects.

**Next steps**

-   If you are changing from disabled to enabled state or have been running in permissive mode, relabel the file system to prevent boot failures. See [Relabel the file system when changing SELinux modes](#relabel-the-file-system-when-changing-selinux-modes "2.2. Relabeling the file system when changing SELinux modes").

### [2.2. Relabeling the file system when changing SELinux modes](#relabel-the-file-system-when-changing-selinux-modes) {#relabeling-the-file-system-when-changing-selinux-modes .title}

Relabel the file system to fix incorrectly labeled or unlabeled files after running SELinux in permissive mode or switching from disabled to enabled state. This prevents boot failures and ensures SELinux can enforce policies correctly.

When systems run SELinux in permissive mode, users and processes might label file system objects incorrectly. File system objects created while SELinux is disabled are not labeled at all. These incorrectly labeled and unlabeled files cause problems when changing to enforcing mode because SELinux relies on correct labels.

SELinux automatically relabels file systems when changing from the disabled state to permissive or enforcing mode. However, you must ensure the system boots in permissive mode during relabeling to prevent boot failures.

**Prerequisites**

-   Root access to the system.

**Procedure**

1.  Create the `/.autorelabel`{.literal} file with the `-F`{.literal} option to ensure files are relabeled on next reboot:

    ``` {.language-plaintext tabindex="-1"}
    # fixfiles -F onboot
    ```

2.  Configure the system to boot in permissive mode to prevent boot failures during relabeling:

    Add the `enforcing=0`{.literal} kernel option to the boot parameters. This ensures the system does not fail to boot if it contains unlabeled files required by `systemd`{.literal} before launching the `selinux-autorelabel`{.literal} service.

3.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

    The system relabels all file system objects during boot.

**Verification**

1.  After the system reboots, check that SELinux is running and the file system has been relabeled:

    ``` {.language-plaintext tabindex="-1"}
    # sestatus
    ```

    Verify that the output shows SELinux is enabled and the current mode matches your configuration.

2.  Check that the `/.autorelabel`{.literal} file has been removed after successful relabeling:

    ``` {.language-plaintext tabindex="-1"}
    # ls -la /.autorelabel
    ls: cannot access '/.autorelabel': No such file or directory
    ```

### [2.3. Changing SELinux to permissive mode](#changing-selinux-to-permissive-mode) {#changing-selinux-to-permissive-mode .title}

Configure SELinux to run in permissive mode to troubleshoot denial messages and debug security policies. In this mode, the system logs Access Vector Cache (AVC) events but does not enforce the active policy, so you can analyze impacts without blocking operations.

**Prerequisites**

-   The `selinux-policy-targeted`{.literal}, `libselinux-utils`{.literal}, and `policycoreutils`{.literal} packages are installed on your system.
-   The `selinux=0`{.literal} or `enforcing=0`{.literal} kernel parameters are not used.

**Procedure**

1.  Open the `/etc/selinux/config`{.literal} file in a text editor and configure the `SELINUX=permissive`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # This file controls the state of SELinux on the system.
    # SELINUX= can take one of these three values:
    #       enforcing - SELinux security policy is enforced.
    #       permissive - SELinux prints warnings instead of enforcing.
    #       disabled - No SELinux policy is loaded.
    SELINUX=permissive
    # SELINUXTYPE= can take one of these two values:
    #       targeted - Targeted processes are protected,
    #       mls - Multi Level Security protection.
    SELINUXTYPE=targeted
    ```

2.  Restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

1.  After the system restarts, confirm that the `getenforce`{.literal} command returns `Permissive`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ getenforce
    Permissive
    ```

### [2.4. Changing SELinux to enforcing mode](#changing-selinux-to-enforcing-mode) {#changing-selinux-to-enforcing-mode .title}

Configure SELinux to run in enforcing mode to protect your system by denying unauthorized access. In this mode, the system enforces the loaded security policy and blocks policy violations. If you are enabling SELinux from a disabled state, the system automatically relabels files on the next boot.

When you install the system with SELinux, RHEL enables enforcing mode by default.

**Prerequisites**

-   The `selinux-policy-targeted`{.literal}, `libselinux-utils`{.literal}, and `policycoreutils`{.literal} packages are installed on your system.
-   The `selinux=0`{.literal} or `enforcing=0`{.literal} kernel parameters are not used.

**Procedure**

1.  Open the `/etc/selinux/config`{.literal} file in a text editor and configure the `SELINUX=enforcing`{.literal} option:

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

2.  Save the change, and restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

    On the next boot, SELinux relabels all the files and directories within the system and adds SELinux context for files and directories that were created when SELinux was disabled.

**Verification**

1.  After the system restarts, confirm that the `getenforce`{.literal} command returns `Enforcing`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ getenforce
    Enforcing
    ```

**Troubleshooting**

After changing to enforcing mode, SELinux may deny some actions because of incorrect or missing SELinux policy rules.

-   To view what actions SELinux denies, enter the following command as root:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts today
    ```

-   Alternatively, with the `setroubleshoot-server`{.literal} package installed, enter:

    ``` {.language-plaintext tabindex="-1"}
    # grep "SELinux is preventing" /var/log/messages
    ```

-   If SELinux is active and the Audit daemon (`auditd`{.literal}) is not running on your system, then search for certain SELinux messages in the output of the `dmesg`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # dmesg | grep -i -e type=1300 -e type=1400
    ```

See [Troubleshooting problems related to SELinux](#troubleshooting-problems-related-to-selinux "Chapter 5. Troubleshooting problems related to SELinux") for more information.

### [2.5. Enabling SELinux on systems that previously had it disabled](#enabling-selinux-on-systems-that-previously-had-it-disabled) {#enabling-selinux-on-systems-that-previously-had-it-disabled .title}

Enable SELinux on systems that previously had it disabled to restore security protections and enforce mandatory access control. You must first run the system in permissive mode and relabel the file system to prevent boot failures caused by missing or incorrect security labels.

File-system objects created while SELinux is disabled do not have security labels. This lack of labels causes failures when changing directly to enforcing mode because the system relies on correct contexts to make access decisions.

Warning

Before rebooting the system for relabeling, make sure the system boots in permissive mode, for example, by using the `enforcing=0`{.literal} kernel option. This prevents the system from failing to boot in case the system contains unlabeled files required by `systemd`{.literal} before launching the `selinux-autorelabel`{.literal} service. For more information, see [RHBZ#2021835](https://bugzilla.redhat.com/show_bug.cgi?id=2021835).

**Procedure**

1.  Enable SELinux in permissive mode. For more information, see [Changing SELinux to permissive mode](#changing-selinux-to-permissive-mode "2.3. Changing SELinux to permissive mode").

2.  Restart your system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

3.  Check for SELinux denial messages. For more information, see [Identifying SELinux denials](#identifying-selinux-denials "5.1. Identifying SELinux denials").

4.  Ensure that files are relabeled upon the next reboot:

    ``` {.language-plaintext tabindex="-1"}
    # fixfiles -F onboot
    ```

    This creates the `/.autorelabel`{.literal} file containing the `-F`{.literal} option.

    Warning

    Always switch to permissive mode before entering the `fixfiles -F onboot`{.literal} command.

    By default, `autorelabel`{.literal} uses as many threads in parallel as the system has available CPU cores. To use only a single thread during automatic relabeling, use the `fixfiles -T 1 onboot`{.literal} command.

5.  If there are no denials, switch to enforcing mode. For more information, see [Changing SELinux modes at boot time](#changing-selinux-modes-at-boot-time "2.7. SELinux kernel boot parameters").

**Verification**

1.  After the system restarts, confirm that the `getenforce`{.literal} command returns `Enforcing`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ getenforce
    Enforcing
    ```

**Next steps**

To run custom applications with SELinux in enforcing mode, choose one of the following scenarios:

-   Run your application in the `unconfined_service_t`{.literal} domain.
-   Write a new policy for your application. See the [Writing a custom SELinux policy](#writing-a-custom-selinux-policy "Chapter 8. Writing a custom SELinux policy") section for more information.

**Additional resources**

-   [SELinux states and modes](#selinux-states-and-modes "1.5. SELinux states and modes")

### [2.6. Disabling SELinux](#disabling-selinux) {#disabling-selinux .title}

Disable SELinux by configuring the kernel command line to completely deactivate the security infrastructure. Use this mode only when necessary, because it stops the system from labeling files and makes re-enabling SELinux difficult.

When you disable SELinux, your system does not load the security policy or log Access Vector Cache (AVC) messages. Therefore, all [benefits of running SELinux](#benefits-of-running-selinux "1.2. Benefits of running SELinux") are lost.

Warning

Do not disable SELinux except in specific scenarios, such as performance-sensitive systems where weakened security is acceptable.

If you must debug your system in a production environment, temporarily use permissive mode instead of permanently disabling SELinux. See [Changing to permissive mode](#changing-selinux-to-permissive-mode "2.3. Changing SELinux to permissive mode") for more information about permissive mode.

**Prerequisites**

-   The `grubby`{.literal} package is installed:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm -q grubby
    grubby-<version>
    ```

**Procedure**

1.  Configure your boot loader to add `selinux=0`{.literal} to the kernel command line:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo grubby --update-kernel ALL --args selinux=0
    ```

2.  Restart your system:

    ``` {.language-plaintext tabindex="-1"}
    $ reboot
    ```

**Verification**

-   After the reboot, confirm that the `getenforce`{.literal} command returns `Disabled`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ getenforce
    Disabled
    ```

### [2.7. SELinux kernel boot parameters](#changing-selinux-modes-at-boot-time) {#selinux-kernel-boot-parameters .title}

Kernel boot parameters control the SELinux mode and system initialization at boot time. You can use these parameters to override the default security configuration during system startup.

`enforcing=0`{.literal}

:   Setting this parameter causes the system to start in permissive mode, which is useful when troubleshooting issues. Using permissive mode might be the only option to detect a problem if your file system is corrupted. Moreover, in permissive mode, the system creates labels correctly. The AVC messages generated in this mode can be different than in enforcing mode.

    In permissive mode, the system reports only the first denial from a series of the same denials. However, in enforcing mode, you might get a denial related to reading a directory, and an application stops. In permissive mode, you get the same AVC message, but the application continues reading files in the directory and you get an AVC for each denial.

`selinux=0`{.literal}

:   This parameter causes the kernel to not load any part of the SELinux infrastructure. The init scripts detect that the system booted with the `selinux=0`{.literal} parameter and touch the `/.autorelabel`{.literal} file. This causes the system to automatically relabel the next time you boot with SELinux enabled.

    Important

    Do not use the `selinux=0`{.literal} parameter in a production environment. To debug your system, temporarily use permissive mode instead of disabling SELinux.

`autorelabel=1`{.literal}

:   This parameter forces the system to relabel similarly to the following commands:

    ``` {.language-plaintext tabindex="-1"}
    # touch /.autorelabel
    # reboot
    ```

    If a file system contains a large amount of mislabeled objects, start the system in permissive mode to ensure the autorelabel process succeeds.

For additional SELinux kernel boot parameters, such as `checkreqprot`{.literal}, see the `/usr/share/doc/kernel-doc-`{.literal}*`<KERNEL_VER>`{.literal}*`/Documentation/admin-guide/kernel-parameters.txt`{.literal} file installed with the `kernel-doc`{.literal} package. Replace the *`<KERNEL_VER>`{.literal}* string with the version number of the installed kernel, for example:

``` {.language-plaintext tabindex="-1"}
# dnf install kernel-doc
$ less /usr/share/doc/kernel-doc-6.12.0-55.9.1/Documentation/admin-guide/kernel-parameters.txt
```

## [Chapter 3. Managing confined and unconfined users](#managing-confined-and-unconfined-users) {#chapter-3.-managing-confined-and-unconfined-users .title}

Control what actions Linux users and their processes can perform by mapping them to specific SELinux users defined in the policy. This method helps enforce granular security restrictions based on the assigned SELinux profile.

Each Linux user is mapped to an SELinux user according to the rules in the SELinux policy. Administrators can modify these rules by using the `semanage login`{.literal} utility or by assigning Linux users directly to specific SELinux users. Therefore, a Linux user has the restrictions of the SELinux user to which it is assigned. When a Linux user that is assigned to an SELinux user launches a process, this process inherits the SELinux user's restrictions, unless other rules specify a different role or type. See the `unconfined_selinux(8)`{.literal}, `user_selinux(8)`{.literal}, `staff_selinux(8)`{.literal}, and `sysadm_selinux(8)`{.literal} man pages installed with the `selinux-policy-doc`{.literal} package on your system for more information.

### [3.1. Confined and unconfined users in SELinux](#confined-and-unconfined-users-in-selinux) {#confined-and-unconfined-users-in-selinux .title}

By default, all Linux users in Red Hat Enterprise Linux, including users with administrative privileges, are mapped to the unconfined SELinux user `unconfined_u`{.literal}. You can improve the security of the system by assigning users to SELinux confined users.

The security context for a Linux user consists of the SELinux user, the SELinux role, and the SELinux type. For example:

``` {.language-plaintext tabindex="-1"}
user_u:user_r:user_t
```

Where:

`user_u`{.literal}
:   Is the SELinux user.

`user_r`{.literal}
:   Is the SELinux role.

`user_t`{.literal}
:   Is the SELinux type.

After a Linux user logs in, its SELinux user cannot change. However, its type and role can change, for example, during transitions.

To see the SELinux user mapping on your system, use the `semanage login -l`{.literal} command as root:

``` {.language-plaintext tabindex="-1"}
# semanage login -l
Login Name           SELinux User         MLS/MCS Range        Service

__default__          unconfined_u         s0-s0:c0.c1023       *
root                 unconfined_u         s0-s0:c0.c1023       *
```

In Red Hat Enterprise Linux, Linux users are mapped to the SELinux `__default__`{.literal} login by default, which is mapped to the SELinux `unconfined_u`{.literal} user. The following line defines the default mapping:

``` {.language-plaintext tabindex="-1"}
__default__          unconfined_u         s0-s0:c0.c1023       *
```

Confined users are restricted by SELinux rules explicitly defined in the current SELinux policy. Unconfined users are subject to only minimal restrictions by SELinux.

Confined and unconfined Linux users are subject to executable and writable memory checks, and are also restricted by MCS or MLS.

To list the available SELinux users, enter the following command:

``` {.language-plaintext tabindex="-1"}
$ seinfo -u
Users: 8
   guest_u
   root
   staff_u
   sysadm_u
   system_u
   unconfined_u
   user_u
   xguest_u
```

Note that the `seinfo`{.literal} command is provided by the `setools-console`{.literal} package, which is not installed by default.

If an unconfined Linux user executes an application that SELinux policy defines as one that can transition from the `unconfined_t`{.literal} domain to its own confined domain, the unconfined Linux user is still subject to the restrictions of that confined domain. The security benefit of this is that, even though a Linux user is running unconfined, the application remains confined. Therefore, the exploitation of a flaw in the application can be limited by the policy.

Similarly, we can apply these checks to confined users. Each confined user is restricted by a confined user domain. The SELinux policy can also define a transition from a confined user domain to its own target confined domain. In such a case, confined users are subject to the restrictions of that target confined domain. The main point is that special privileges are associated with the confined users according to their role.

### [3.2. Roles and access rights of SELinux users](#roles-and-access-rights-of-selinux-users) {#roles-and-access-rights-of-selinux-users .title}

Manage the permissions and access rights of SELinux users by adjusting policy booleans and mapping Linux users to appropriate roles. This process help ensures that users in RHEL have the correct authorizations for their specific tasks.

The SELinux policy maps each Linux user to an SELinux user. This allows Linux users to inherit the restrictions of SELinux users. You can customize the permissions for confined users in your SELinux policy according to specific needs by adjusting booleans in the policy. You can determine the current state of these booleans by using the `semanage boolean -l`{.literal} command. To list all SELinux users, their SELinux roles, and levels and ranges for MLS and MCS, use the `semanage user -l`{.literal} command as `root`{.literal}.

+--------------------------+--------------------------+--------------------------+
| User                     | Default role             | Additional roles         |
+:=========================+:=========================+:=========================+
| `unconfined_u`{.literal} | `unconfined_r`{.literal} | `system_r`{.literal}     |
+--------------------------+--------------------------+--------------------------+
| `guest_u`{.literal}      | `guest_r`{.literal}      |                          |
+--------------------------+--------------------------+--------------------------+
| `xguest_u`{.literal}     | `xguest_r`{.literal}     |                          |
+--------------------------+--------------------------+--------------------------+
| `user_u`{.literal}       | `user_r`{.literal}       |                          |
+--------------------------+--------------------------+--------------------------+
| `staff_u`{.literal}      | `staff_r`{.literal}      | `sysadm_r`{.literal}     |
+--------------------------+--------------------------+--------------------------+
|                          |                          | `unconfined_r`{.literal} |
+--------------------------+--------------------------+--------------------------+
|                          |                          | `system_r`{.literal}     |
+--------------------------+--------------------------+--------------------------+
| `sysadm_u`{.literal}     | `sysadm_r`{.literal}     |                          |
+--------------------------+--------------------------+--------------------------+
| `root`{.literal}         | `staff_r`{.literal}      | `sysadm_r`{.literal}     |
+--------------------------+--------------------------+--------------------------+
|                          |                          | `unconfined_r`{.literal} |
+--------------------------+--------------------------+--------------------------+
|                          |                          | `system_r`{.literal}     |
+--------------------------+--------------------------+--------------------------+
| `system_u`{.literal}     | `system_r`{.literal}     |                          |
+--------------------------+--------------------------+--------------------------+

: Table 3.1. Roles of SELinux users

Show more

Note that `system_u`{.literal} is a special user identity for system processes and objects, and `system_r`{.literal} is the associated role. Administrators must never associate this `system_u`{.literal} user and the `system_r`{.literal} role to a Linux user. Also, `unconfined_u`{.literal} and `root`{.literal} are unconfined users. For these reasons, the roles associated to these SELinux users are not included in the following table *Types and access rights of SELinux roles*.

Each SELinux role corresponds to an SELinux type and provides specific access rights.

+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| Role                     | Type                     | Log in using X Window System                                         | `su`{.literal} and `sudo`{.literal} | Execute in home directory and `/tmp`{.literal} (default) | Networking                                     |
+:=========================+:=========================+:=====================================================================+:====================================+:=========================================================+:===============================================+
| `unconfined_r`{.literal} | `unconfined_t`{.literal} | yes                                                                  | yes                                 | yes                                                      | yes                                            |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `guest_r`{.literal}      | `guest_t`{.literal}      | no                                                                   | no                                  | yes                                                      | no                                             |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `xguest_r`{.literal}     | `xguest_t`{.literal}     | yes                                                                  | no                                  | yes                                                      | web browsers only (Mozilla Firefox, GNOME Web) |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `user_r`{.literal}       | `user_t`{.literal}       | yes                                                                  | no                                  | yes                                                      | yes                                            |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `staff_r`{.literal}      | `staff_t`{.literal}      | yes                                                                  | only `sudo`{.literal}               | yes                                                      | yes                                            |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `auditadm_r`{.literal}   | `auditadm_t`{.literal}   |                                                                      | yes                                 | yes                                                      | yes                                            |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `dbadm_r`{.literal}      | `dbadm_r`{.literal}      |                                                                      | yes                                 | yes                                                      | yes                                            |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `logadm_r`{.literal}     | `logadm_t`{.literal}     |                                                                      | yes                                 | yes                                                      | yes                                            |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `webadm_r`{.literal}     | `webadm_r`{.literal}     |                                                                      | yes                                 | yes                                                      | yes                                            |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `secadm_r`{.literal}     | `secadm_t`{.literal}     |                                                                      | yes                                 | yes                                                      | yes                                            |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `sysadm_r`{.literal}     | `sysadm_t`{.literal}     | only when the `xdm_sysadm_login`{.literal} boolean is `on`{.literal} | yes                                 | yes                                                      | yes                                            |
+--------------------------+--------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+

: Table 3.2. Types and access rights of SELinux roles

Show more

For more detailed descriptions of the non-administrator roles, see [Confined non-administrator roles in SELinux](#confined-non-administrator-roles-in-selinux "3.3. Confined non-administrator roles in SELinux").

For more detailed descriptions of the administrator roles, see [Confined administrator roles in SELinux](#confined-administrator-roles-in-selinux "3.4. Confined administrator roles in SELinux").

To list all available roles, enter the `seinfo -r`{.literal} command:

``` {.language-plaintext tabindex="-1"}
$ seinfo -r
Roles: 14
   auditadm_r
   dbadm_r
   guest_r
   logadm_r
   nx_server_r
   object_r
   secadm_r
   staff_r
   sysadm_r
   system_r
   unconfined_r
   user_r
   webadm_r
   xguest_r
```

Note that the `seinfo`{.literal} command is provided by the `setools-console`{.literal} package, which is not installed by default. See the `seinfo(1)`{.literal}, `semanage-login(8)`{.literal}, and `xguest_selinux(8)`{.literal} man pages installed with the `selinux-policy-doc`{.literal} package on your system for more information.

**Additional resources**

-   [How to modify SELinux settings with booleans (Red Hat Sysadmin)](https://www.redhat.com/sysadmin/change-selinux-settings-boolean)

### [3.3. Confined non-administrator roles in SELinux](#confined-non-administrator-roles-in-selinux) {#confined-non-administrator-roles-in-selinux .title}

Confined non-administrator roles grant specific privileges for designated tasks. By assigning separate roles, you can provide different authorization levels to individual users based on their responsibilities.

You can also customize the permissions of SELinux roles by changing the related SELinux booleans on your system. To see the SELinux booleans and their current state, use the `semanage boolean -l`{.literal} command as root. You can get more detailed descriptions if you install the `selinux-policy-devel`{.literal} package.

``` {.language-plaintext tabindex="-1"}
# semanage boolean -l
SELinux boolean                State  Default Description
…
xguest_connect_network         (on   ,   on)  Allow xguest users to configure Network Manager and connect to apache ports
xguest_exec_content            (on   ,   on)  Allow xguest to exec content
…
```

Linux users in the `user_t`{.literal}, `guest_t`{.literal}, and `xguest_t`{.literal} domains can only run set user ID (`setuid`{.literal}) applications if SELinux policy permits it (for example, `passwd`{.literal}). These users cannot run the `setuid`{.literal} applications `su`{.literal} and `sudo`{.literal}, and therefore cannot use these applications to become root.

By default, Linux users in the `staff_t`{.literal}, `user_t`{.literal}, `guest_t`{.literal}, and `xguest_t`{.literal} domains can run applications in their home directories and `/tmp`{.literal}. Applications inherit the permissions of the user that ran them.

To prevent `guest_t`{.literal}, and `xguest_t`{.literal} users from running applications in directories in which they have write access, set the `guest_exec_content`{.literal} and `xguest_exec_content`{.literal} booleans to `off`{.literal}.

SELinux has the following confined non-administrator roles, each with specific privileges and limitations:

`guest_r`{.literal}

:   Has very limited permissions. Users assigned to this role cannot access the network, but can run files in the `/tmp`{.literal} and `/home`{.literal} directories.

    Related boolean:

    ``` {.language-plaintext tabindex="-1"}
    SELinux boolean                State  Default Description
    guest_exec_content             (on   ,   on)  Allow guest to exec content
    ```

`xguest_r`{.literal}

:   Has limited permissions. Users assigned to this role can log in to X Window, access web pages by using network browsers, and access media. They can also run files in the `/tmp`{.literal} and `/home`{.literal} directories.

    Related booleans:

    ``` {.language-plaintext tabindex="-1"}
    SELinux boolean                State  Default Description
    xguest_connect_network         (on   ,   on)  Allow xguest users to configure Network Manager and connect to apache ports
    xguest_exec_content            (on   ,   on)  Allow xguest to exec content
    xguest_mount_media             (on   ,   on)  Allow xguest users to mount removable media
    xguest_use_bluetooth           (on   ,   on)  Allow xguest to use blue tooth devices
    ```

`user_r`{.literal}

:   Has non-privileged access with full user permissions. Users assigned to this role can perform most actions that do not require administrative privileges.

    Related booleans:

    ``` {.language-plaintext tabindex="-1"}
    SELinux boolean                State  Default Description
    unprivuser_use_svirt           (off  ,  off)  Allow unprivileged user to create and transition to svirt domains.
    ```

`staff_r`{.literal}

:   Has permissions similar to `user_r`{.literal} and additional privileges. In particular, users assigned to this role are allowed to run `sudo`{.literal} to enter administrative commands that are normally reserved for the `root`{.literal} user. This changes roles and the effective user ID (EUID) but does not change the SELinux user.

    Related booleans:

    ``` {.language-plaintext tabindex="-1"}
    SELinux boolean                State  Default Description
    staff_exec_content             (on   ,   on)  Allow staff to exec content
    staff_use_svirt                (on   ,   on)  allow staff user to create and transition to svirt domains.
    ```

For additional information about each role and the associated types, see the `guest_selinux(8)`{.literal}, `xguest_selinux(8)`{.literal}, `user_selinux(8)`{.literal}, and `staff_selinux(8)`{.literal} man pages installed with the `selinux-policy-doc`{.literal} package on your system.

**Additional resources**

-   [Confining an administrator by using sudo and the sysadm_r role](#confining-an-administrator-by-using-sudo-and-the-sysadmr-role "3.9. Confining an administrator by using sudo and the sysadm_r role")

### [3.4. Confined administrator roles in SELinux](#confined-administrator-roles-in-selinux) {#confined-administrator-roles-in-selinux .title}

Confined administrator roles grant specific privileges to the Linux users assigned to them. By assigning different roles, you can divide administrative privileges across various system domains. This approach is useful when multiple administrators each manage a separate domain.

You can assign these roles to SELinux users by using the `semanage user`{.literal} command.

SELinux has the following confined administrator roles:

`auditadm_r`{.literal}

:   The audit administrator role allows managing processes related to the Audit subsystem.

    Related boolean:

    ``` {.language-plaintext tabindex="-1"}
    SELinux boolean                State  Default Description
    auditadm_exec_content          (on   ,   on)  Allow auditadm to exec content
    ```

`dbadm_r`{.literal}

:   The database administrator role allows managing MariaDB and PostgreSQL databases.

    Related booleans:

    ``` {.language-plaintext tabindex="-1"}
    SELinux boolean                State  Default Description
    dbadm_exec_content             (on   ,   on)  Allow dbadm to exec content
    dbadm_manage_user_files        (off  ,  off)  Determine whether dbadm can manage generic user files.
    dbadm_read_user_files          (off  ,  off)  Determine whether dbadm can read generic user files.
    ```

`logadm_r`{.literal}

:   The log administrator role allows managing logs, specifically, SELinux types related to the Rsyslog logging service and the Audit subsystem.

    Related boolean:

    ``` {.language-plaintext tabindex="-1"}
    SELinux boolean                State  Default Description
    logadm_exec_content            (on   ,   on)  Allow logadm to exec content
    ```

`webadm_r`{.literal}

:   The web administrator allows managing the Apache HTTP Server.

    Related booleans:

    ``` {.language-plaintext tabindex="-1"}
    SELinux boolean                State  Default Description
    webadm_manage_user_files       (off  ,  off)  Determine whether webadm can manage generic user files.
    webadm_read_user_files         (off  ,  off)  Determine whether webadm can read generic user files.
    ```

`secadm_r`{.literal}

:   The security administrator role allows managing the SELinux database.

    Related booleans:

    ``` {.language-plaintext tabindex="-1"}
    SELinux boolean                State  Default Description
    secadm_exec_content            (on   ,   on)  Allow secadm to exec content
    ```

`sysadm_r`{.literal}

:   The system administrator role allows doing everything of the previously listed roles and has additional privileges. In non-default configurations, security administration can be separated from system administration by disabling the `sysadm_secadm`{.literal} module in the SELinux policy.

    The `sysadm_u`{.literal} user cannot log in directly using SSH. To enable SSH logins for `sysadm_u`{.literal}, set the `ssh_sysadm_login`{.literal} boolean to `on`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool -P ssh_sysadm_login on
    ```

    Related booleans:

    ``` {.language-plaintext tabindex="-1"}
    SELinux boolean                State  Default Description
    ssh_sysadm_login               (on   ,   on)  Allow ssh logins as sysadm_r:sysadm_t
    sysadm_exec_content            (on   ,   on)  Allow sysadm to exec content
    xdm_sysadm_login               (on   ,   on)  Allow the graphical login program to login directly as sysadm_r:sysadm_t
    ```

For additional information about each role, and the associated types, see the relevant man pages installed with the `selinux-policy-doc`{.literal} package on your system: `auditadm_selinux(8)`{.literal}, `dbadm_selinux (8)`{.literal}, `logadm_selinux(8)`{.literal}, `webadm_selinux(8)`{.literal}, `secadm_selinux(8)`{.literal}, and `sysadm_selinux(8)`{.literal}.

**Additional resources**

-   [Separating system administration from security administration in MLS](#separating-system-administration-from-security-administration-in-mls "6.8. Separating system administration from security administration in MLS")
-   [Confining an administrator by mapping to sysadm_u](#confining-an-administrator-by-mapping-to-sysadm_u "3.8. Confining an administrator by mapping to sysadm_u")

### [3.5. Adding a new user automatically mapped to the SELinux unconfined_u user](#adding-a-new-user-automatically-mapped-to-the-selinux-unconfined_u-user) {#adding-a-new-user-automatically-mapped-to-the-selinux-unconfined_u-user .title}

Create a new Linux user that is automatically mapped to the default SELinux `unconfined_u`{.literal} user for scenarios where strict SELinux confinement is not required.

**Prerequisites**

-   The `root`{.literal} user is running unconfined, as it does by default in Red Hat Enterprise Linux.

**Procedure**

1.  Enter the following command to create a new Linux user named *`<example_user>`{.literal}*:

    ``` {.language-plaintext tabindex="-1"}
    # useradd <example_user>
    ```

2.  To assign a password to the Linux *`<example_user>`{.literal}* user:

    ``` {.language-plaintext tabindex="-1"}
    # passwd <example_user>
    Changing password for user <example_user>.
    New password:
    Retype new password:
    passwd: all authentication tokens updated successfully.
    ```

3.  Log out of your current session.

4.  Log in as the Linux *`<example_user>`{.literal}* user. When you log in, the `pam_selinux`{.literal} PAM module automatically maps the Linux user to an SELinux user (in this case, `unconfined_u`{.literal}), and sets up the resulting SELinux context. The Linux user's shell is then launched with this context.

**Verification**

1.  When logged in as the *`<example_user>`{.literal}* user, check the context of a Linux user:

    ``` {.language-plaintext tabindex="-1"}
    $ id -Z
    unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
    ```

### [3.6. Adding a new user as an SELinux-confined user](#adding-a-new-user-as-an-selinux-confined-user) {#adding-a-new-user-as-an-selinux-confined-user .title}

You can add a new SELinux-confined user to the system with the same command used to create the user account. Mapping users to a confined user, such as `staff_u`{.literal}, helps ensure the system is protected from potential security breaches.

**Prerequisites**

-   The `root`{.literal} user is running unconfined, as it does by default in Red Hat Enterprise Linux.

**Procedure**

1.  Enter the following command to create a new Linux user named *`<example_user>`{.literal}* and map it to the SELinux `staff_u`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    # useradd -Z staff_u <example_user>
    ```

2.  To assign a password to the Linux *`<example_user>`{.literal}* user:

    ``` {.language-plaintext tabindex="-1"}
    # passwd <example_user>
    Changing password for user <example_user>.
    New password:
    Retype new password:
    passwd: all authentication tokens updated successfully.
    ```

3.  Log out of your current session.

4.  Log in as the Linux *`<example_user>`{.literal}* user. The user's shell launches with the `staff_u`{.literal} context.

**Verification**

1.  When logged in as the *`<example_user>`{.literal}* user, check the context of a Linux user:

    ``` {.language-plaintext tabindex="-1"}
    $ id -Z
    uid=1000(<example_user>) gid=1000(<example_user>) groups=1000(<example_user>) context=staff_u:staff_r:staff_t:s0-s0:c0.c1023
    ```

### [3.7. Confining regular users in SELinux](#confining-regular-users-in-selinux) {#confining-regular-users-in-selinux .title}

Increase system security by mapping all regular RHEL 10 users to the confined `user_u`{.literal} SELinux profile. This configuration helps ensure that user accounts have limited privileges and cannot perform unauthorized tasks.

By default, all Linux users in Red Hat Enterprise Linux, including users with administrative privileges, are mapped to the unconfined SELinux user `unconfined_u`{.literal}. You can improve the security of the system by assigning users to SELinux confined users. This is also useful to conform with the [V-71971 Security Technical Implementation Guide](https://rhel7stig.readthedocs.io/en/latest/medium.html#v-71971-the-operating-system-must-prevent-non-privileged-users-from-executing-privileged-functions-to-include-disabling-circumventing-or-altering-implemented-security-safeguards-countermeasures-rhel-07-020020).

**Procedure**

1.  Display the list of SELinux login records. The list displays the mappings of Linux users to SELinux users:

    ``` {.language-plaintext tabindex="-1"}
    # semanage login -l

    Login Name    SELinux User  MLS/MCS Range   Service

    __default__   unconfined_u  s0-s0:c0.c1023       *
    root          unconfined_u  s0-s0:c0.c1023       *
    ```

2.  Map the `__default__`{.literal} user, which represents all users without an explicit mapping, to the `user_u`{.literal} SELinux user:

    ``` {.language-plaintext tabindex="-1"}
    # semanage login -m -s user_u -r s0 __default__
    ```

**Verification**

1.  Check that the `__default__`{.literal} user is mapped to the `user_u`{.literal} SELinux user:

    ``` {.language-plaintext tabindex="-1"}
    # semanage login -l

    Login Name    SELinux User   MLS/MCS Range    Service

    __default__   user_u         s0               *
    root          unconfined_u   s0-s0:c0.c1023   *
    ```

2.  Verify that the processes of a new user run in the `user_u:user_r:user_t:s0`{.literal} SELinux context.

    a.  Create a new user:

        ``` {.language-plaintext tabindex="-1"}
        # adduser <example_user>
        ```

    b.  Define a password for *`<example_user>`{.literal}*:

        ``` {.language-plaintext tabindex="-1"}
        # passwd <example_user>
        ```

    c.  Log out as `root`{.literal} and log in as the new user.

    d.  Show the security context for the user's ID:

        ``` {.language-plaintext tabindex="-1"}
        [<example_user>@localhost ~]$ id -Z
        user_u:user_r:user_t:s0
        ```

    e.  Show the security context of the user's current processes:

        ``` {.language-plaintext tabindex="-1"}
        [<example_user>@localhost ~]$ ps axZ
        LABEL                           PID TTY      STAT   TIME COMMAND
        -                                 1 ?        Ss     0:05 /usr/lib/systemd/systemd --switched-root --system --deserialize 18
        -                              3729 ?        S      0:00 (sd-pam)
        user_u:user_r:user_t:s0        3907 ?        Ss     0:00 /usr/lib/systemd/systemd --user
        -                              3911 ?        S      0:00 (sd-pam)
        user_u:user_r:user_t:s0        3918 ?        S      0:00 sshd: <example_user>@pts/0
        user_u:user_r:user_t:s0        3922 pts/0    Ss     0:00 -bash
        user_u:user_r:user_dbusd_t:s0  3969 ?        Ssl    0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
        user_u:user_r:user_t:s0        3971 pts/0    R+     0:00 ps axZ
        ```

### [3.8. Confining an administrator by mapping to sysadm_u](#confining-an-administrator-by-mapping-to-sysadm_u) {#confining-an-administrator-by-mapping-to-sysadm_u .title}

You can confine a user with administrative privileges by mapping the user directly to the `sysadm_u`{.literal} SELinux user. When the user logs in, the session runs in the `sysadm_u:sysadm_r:sysadm_t`{.literal} SELinux context. This minimizes the potential impact if an administrative account is compromised.

By default, all Linux users in Red Hat Enterprise Linux, including users with administrative privileges, are mapped to the unconfined SELinux user `unconfined_u`{.literal}. You can improve the security of the system by assigning users to SELinux confined users. This is useful to conform with the [V-71971 Security Technical Implementation Guide](https://rhel7stig.readthedocs.io/en/latest/medium.html#v-71971-the-operating-system-must-prevent-non-privileged-users-from-executing-privileged-functions-to-include-disabling-circumventing-or-altering-implemented-security-safeguards-countermeasures-rhel-07-020020).

**Prerequisites**

-   The `root`{.literal} user runs unconfined. This is the Red Hat Enterprise Linux default.

**Procedure**

1.  Optional: To allow `sysadm_u`{.literal} users to connect to the system by using SSH:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool -P ssh_sysadm_login on
    ```

2.  Map a new or existing user to the `sysadm_u`{.literal} SELinux user:

    -   To map a new user, add a new user to the `wheel`{.literal} user group and map the user to the `sysadm_u`{.literal} SELinux user:

        ``` {.language-plaintext tabindex="-1"}
        # adduser -G wheel -Z sysadm_u <example_user>
        ```

    -   To map an existing user, add the user to the `wheel`{.literal} user group and map the user to the `sysadm_u`{.literal} SELinux user:

        ``` {.language-plaintext tabindex="-1"}
        # usermod -G wheel -Z sysadm_u <example_user>
        ```

3.  Restore the context of the user's home directory:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -R -F -v /home/<example_user>
    ```

**Verification**

1.  Check that *`<example_user>`{.literal}* is mapped to the `sysadm_u`{.literal} SELinux user:

    ``` {.language-plaintext tabindex="-1"}
    # semanage login -l | grep <example_user>
    <example_user>     sysadm_u    s0-s0:c0.c1023   *
    ```

2.  Log in as *`<example_user>`{.literal}*, for example, by using SSH, and show the user's security context:

    ``` {.language-plaintext tabindex="-1"}
    [<example_user>@localhost ~]$ id -Z
    sysadm_u:sysadm_r:sysadm_t:s0-s0:c0.c1023
    ```

3.  Switch to the `root`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo -i
    [sudo] password for <example_user>:
    ```

4.  Verify that the security context remains unchanged:

    ``` {.language-plaintext tabindex="-1"}
    # id -Z
    sysadm_u:sysadm_r:sysadm_t:s0-s0:c0.c1023
    ```

5.  Try an administrative task, for example, restarting the `sshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sshd
    ```

    If there is no output, the command finished successfully.

    If the command does not finish successfully, it prints the following message:

    ``` {.language-plaintext tabindex="-1"}
    Failed to restart sshd.service: Access denied
    See system logs and 'systemctl status sshd.service' for details.
    ```

### [3.9. Confining an administrator by using sudo and the sysadm_r role](#confining-an-administrator-by-using-sudo-and-the-sysadmr-role) {#confining-an-administrator-by-using-sudo-and-the-sysadm_r-role .title}

You can map a specific user with administrative privileges to the `staff_u`{.literal} SELinux user, and configure `sudo`{.literal} so that the user can gain the `sysadm_r`{.literal} SELinux administrator role. In this role, the user can perform administrative tasks without SELinux denials.

When the user logs in, the session runs in the `staff_u:staff_r:staff_t`{.literal} SELinux context, but when the user enters a command by using `sudo`{.literal}, the session changes to the `staff_u:sysadm_r:sysadm_t`{.literal} context.

By default, all Linux users in Red Hat Enterprise Linux, including users with administrative privileges, are mapped to the unconfined SELinux user `unconfined_u`{.literal}. You can improve the security of the system by assigning users to SELinux confined users. This is useful to conform with the [V-71971 Security Technical Implementation Guide](https://rhel7stig.readthedocs.io/en/latest/medium.html#v-71971-the-operating-system-must-prevent-non-privileged-users-from-executing-privileged-functions-to-include-disabling-circumventing-or-altering-implemented-security-safeguards-countermeasures-rhel-07-020020).

**Prerequisites**

-   The `root`{.literal} user runs unconfined. This is the Red Hat Enterprise Linux default.

**Procedure**

1.  Map a new or existing user to the `staff_u`{.literal} SELinux user:

    a.  To map a new user, add a new user to the `wheel`{.literal} user group and map the user to the `staff_u`{.literal} SELinux user:

        ``` {.language-plaintext tabindex="-1"}
        # adduser -G wheel -Z staff_u <example_user>
        ```

    b.  To map an existing user, add the user to the `wheel`{.literal} user group and map the user to the `staff_u`{.literal} SELinux user:

        ``` {.language-plaintext tabindex="-1"}
        # usermod -G wheel -Z staff_u <example_user>
        ```

2.  Restore the context of the user's home directory:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -R -F -v /home/<example_user>
    ```

3.  To allow *`<example_user>`{.literal}* to gain the SELinux administrator role, create a new file in the `/etc/sudoers.d/`{.literal} directory, for example:

    ``` {.language-plaintext tabindex="-1"}
    # visudo -f /etc/sudoers.d/<example_user>
    ```

4.  Add the following line to the new file:

    ``` {.language-plaintext tabindex="-1"}
    <example_user> ALL=(ALL) TYPE=sysadm_t ROLE=sysadm_r ALL
    ```

**Verification**

1.  Check that *`<example_user>`{.literal}* is mapped to the `staff_u`{.literal} SELinux user:

    ``` {.language-plaintext tabindex="-1"}
    # semanage login -l | grep <example_user>
    <example_user>     staff_u    s0-s0:c0.c1023   *
    ```

2.  Log in as *`<example_user>`{.literal}*, for example, by using SSH, and switch to the `root`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    [<example_user>@localhost ~]$ sudo -i
    [sudo] password for <example_user>:
    ```

3.  Show the `root`{.literal} security context:

    ``` {.language-plaintext tabindex="-1"}
    # id -Z
    staff_u:sysadm_r:sysadm_t:s0-s0:c0.c1023
    ```

4.  Try an administrative task, for example, restarting the `sshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sshd
    ```

    If there is no output, the command finished successfully.

    If the command does not finish successfully, it prints the following message:

    ``` {.language-plaintext tabindex="-1"}
    Failed to restart sshd.service: Access denied
    See system logs and 'systemctl status sshd.service' for details.
    ```

### [3.10. Additional resources](#managing-confined-and-unconfined-users_310-additional-resources) {#additional-resources .title}

-   [How to configure a system with SELinux confined users (Red Hat Knowledgebase)](https://access.redhat.com/articles/3263671)
-   [How to modify SELinux settings with booleans (Red Hat Sysadmin)](https://www.redhat.com/sysadmin/change-selinux-settings-boolean)

## [Chapter 4. Configuring SELinux for applications and services with non-standard configurations](#configuring-selinux-for-applications-and-services-with-non-standard-configurations) {#chapter-4.-configuring-selinux-for-applications-and-services-with-non-standard-configurations .title}

Adjust the SELinux targeted policy when configuring applications to use non-standard ports or directories. This prevents SELinux denials and helps ensure services run correctly in enforcing mode.

When SELinux is in enforcing mode, the default policy is the targeted policy. You learn how to configure the SELinux policy for various services after you change configuration defaults, such as ports, database locations, or file-system permissions for processes. Such changes require changing SELinux types for non-standard ports, identifying and fixing incorrect labels for changes to default directories, and adjusting the policy by using SELinux booleans.

### [4.1. Customizing the SELinux policy for the Apache HTTP server in a non-standard configuration](#customizing-the-selinux-policy-for-the-apache-http-server-in-a-non-standard-configuration) {#customizing-the-selinux-policy-for-the-apache-http-server-in-a-non-standard-configuration .title}

Adjust the SELinux policy when configuring the Apache HTTP server to use non-standard ports or directories. This prevents access denials and helps ensure the web server operates securely in enforcing mode.

**Prerequisites**

-   The `httpd`{.literal} package is installed and the Apache HTTP server is configured to listen on TCP port 3131 and to use the `/var/test_www/`{.literal} directory instead of the default `/var/www/`{.literal} directory.
-   The `policycoreutils-python-utils`{.literal} and `setroubleshoot-server`{.literal} packages are installed on your system.

**Procedure**

1.  Start the `httpd`{.literal} service and check the status:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start httpd
    # systemctl status httpd
    …
    httpd[14523]: (13)Permission denied: AH00072: make_sock: could not bind to address [::]:3131
    …
    systemd[1]: Failed to start The Apache HTTP Server.
    …
    ```

2.  The SELinux policy assumes that `httpd`{.literal} runs on port 80:

    ``` {.language-plaintext tabindex="-1"}
    # semanage port -l | grep http
    http_cache_port_t              tcp      8080, 8118, 8123, 10001-10010
    http_cache_port_t              udp      3130
    http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
    pegasus_http_port_t            tcp      5988
    pegasus_https_port_t           tcp      5989
    ```

3.  Change the SELinux type of port 3131 to match port 80:

    ``` {.language-plaintext tabindex="-1"}
    # semanage port -a -t http_port_t -p tcp 3131
    ```

4.  Start `httpd`{.literal} again:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start httpd
    ```

5.  However, the content remains inaccessible:

    ``` {.language-plaintext tabindex="-1"}
    # wget localhost:3131/index.html
    …
    HTTP request sent, awaiting response... 403 Forbidden
    …
    ```

    Find the reason with the `sealert`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    # sealert -l "*"
    …
    SELinux is preventing httpd from getattr access on the file /var/test_www/html/index.html.
    …
    ```

6.  Compare SELinux types for the standard and the new path using the `matchpathcon`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    # matchpathcon /var/www/html /var/test_www/html
    /var/www/html       system_u:object_r:httpd_sys_content_t:s0
    /var/test_www/html  system_u:object_r:var_t:s0
    ```

7.  Change the SELinux type of the new `/var/test_www/html/`{.literal} content directory to the type of the default `/var/www/html`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -e /var/www /var/test_www
    ```

8.  Relabel the `/var`{.literal} directory recursively:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /var/
    …
    Relabeled /var/test_www/html from unconfined_u:object_r:var_t:s0 to unconfined_u:object_r:httpd_sys_content_t:s0
    Relabeled /var/test_www/html/index.html from unconfined_u:object_r:var_t:s0 to unconfined_u:object_r:httpd_sys_content_t:s0
    ```

**Verification**

1.  Check that the `httpd`{.literal} service is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status httpd
    …
    Active: active (running)
    …
    systemd[1]: Started The Apache HTTP Server.
    httpd[14888]: Server configured, listening on: port 3131
    ...
    ```

2.  Verify that the content provided by the Apache HTTP server is accessible:

    ``` {.language-plaintext tabindex="-1"}
    # wget localhost:3131/index.html
    …
    HTTP request sent, awaiting response... 200 OK
    Length: 0 [text/html]
    Saving to: 'index.html'
    …
    ```

### [4.2. Adjusting the policy for sharing NFS and CIFS volumes by using SELinux booleans](#adjusting-the-policy-for-sharing-nfs-and-cifs-volumes-by-using-selinux-booleans) {#adjusting-the-policy-for-sharing-nfs-and-cifs-volumes-by-using-selinux-booleans .title}

Modify the SELinux policy at runtime by using booleans to allow services to access NFS and CIFS volumes. This feature enables quick policy adjustments without reloading or recompiling the entire policy.

NFS mounts on the client side are labeled with a default context defined by a policy for NFS volumes. In RHEL, this default context uses the `nfs_t`{.literal} type. Also, Samba shares mounted on the client side are labeled with a default context defined by the policy. This default context uses the `cifs_t`{.literal} type. You can enable or disable booleans to control which services are allowed to access the `nfs_t`{.literal} and `cifs_t`{.literal} types.

See the `semanage-boolean(8)`{.literal}, `sepolicy-booleans(8)`{.literal}, `getsebool(8)`{.literal}, `setsebool(8)`{.literal}, `booleans(5)`{.literal}, and `booleans(8)`{.literal} man pages on your system for details about the commands used.

**Prerequisites**

-   Optionally, install the `selinux-policy-devel`{.literal} package to obtain clearer and more detailed descriptions of SELinux booleans in the output of the `semanage boolean -l`{.literal} command.

**Procedure**

1.  Identify SELinux booleans relevant for NFS, CIFS, and Apache:

    ``` {.language-plaintext tabindex="-1"}
    # semanage boolean -l | grep 'nfs\|cifs' | grep httpd
    httpd_use_cifs                 (off  ,  off)  Allow httpd to access cifs file systems
    httpd_use_nfs                  (off  ,  off)  Allow httpd to access nfs file systems
    ```

2.  List the current state of the booleans:

    ``` {.language-plaintext tabindex="-1"}
    $ getsebool -a | grep 'nfs\|cifs' | grep httpd
    httpd_use_cifs --> off
    httpd_use_nfs --> off
    ```

3.  Enable the identified booleans:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool httpd_use_nfs on
    # setsebool httpd_use_cifs on
    ```

    Note

    Use `setsebool`{.literal} with the `-P`{.literal} option to make the changes persistent across restarts. A `setsebool -P`{.literal} command requires a rebuild of the entire policy, and it might take some time depending on your configuration.

**Verification**

1.  Check that the booleans are `on`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ getsebool -a | grep 'nfs\|cifs' | grep httpd
    httpd_use_cifs --> on
    httpd_use_nfs --> on
    ```

### [4.3. Finding the correct SELinux type for managing access to non-standard directories](#finding-the-correct-selinux-type-for-managing-access-to-non-standard-directories) {#finding-the-correct-selinux-type-for-managing-access-to-non-standard-directories .title}

Find the correct SELinux type to manage access to directories not covered by the default policy. This involves searching for appropriate booleans or matching types, or defining a local policy module if necessary.

If you need to set access-control rules that the default SELinux policy does not cover, start by searching for a boolean that matches your use case. If you cannot find a suitable boolean, you can use a matching SELinux type or even create a local policy module.

See the `sesearch(1)`{.literal}, `semanage-fcontext(8)`{.literal}, `semanage-boolean(8)`{.literal}, and `getsebool(8)`{.literal} man pages on your system for details and more examples related to the commands used.

**Prerequisites**

-   The `selinux-policy-doc`{.literal} and `setools-console`{.literal} packages are installed on your system.

**Procedure**

1.  List all SELinux-related topics and limit the results to a component you want to configure. For example:

    ``` {.language-plaintext tabindex="-1"}
    # man -k selinux | grep samba
    samba_net_selinux (8) - Security Enhanced Linux Policy for the samba_net processes
    samba_selinux (8)    - Security Enhanced Linux Policy for the smbd processes
    …
    ```

    In the man page that corresponds to your scenario, find the related SELinux booleans, port types, and file types.

    Note that the `man -k selinux`{.literal} or `apropos selinux`{.literal} commands are available only after you install the `selinux-policy-doc`{.literal} package.

2.  Optional: You can display the default mapping of processes on default locations by using the `semanage fcontext -l`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -l | grep samba
    …
    /var/cache/samba(/.*)?                             all files          system_u:object_r:samba_var_t:s0
    …
    /var/spool/samba(/.*)?                             all files          system_u:object_r:samba_spool_t:s0
    …
    ```

3.  Use the `sesearch`{.literal} command to display rules in the default SELinux policy. You can find the type and boolean to use by listing the corresponding rule, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ sesearch -A | grep samba | grep httpd
    …
    allow httpd_t cifs_t:dir { getattr open search }; [ use_samba_home_dirs && httpd_enable_homedirs ]:True
    …
    ```

4.  An SELinux boolean might be the most straightforward solution for your configuration problem. You can display all available booleans and their values by using the `getsebool -a`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ getsebool -a | grep homedirs
    git_cgi_enable_homedirs --> off
    git_system_enable_homedirs --> off
    httpd_enable_homedirs --> off
    mock_enable_homedirs --> off
    mpd_enable_homedirs --> off
    openvpn_enable_homedirs --> on
    ssh_chroot_rw_homedirs --> off
    ```

5.  You can verify that the selected boolean does exactly what you want by using the `sesearch`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ sesearch -A | grep httpd_enable_homedirs
    …
    allow httpd_suexec_t autofs_t:dir { getattr open search }; [ use_nfs_home_dirs && httpd_enable_homedirs ]:True
    allow httpd_suexec_t autofs_t:dir { getattr open search }; [ use_samba_home_dirs && httpd_enable_homedirs ]:True
    …
    ```

6.  If no boolean matches your scenario, find an SELinux type that suits your case. You can find a type for your files by querying a corresponding rule from the default policy by using `sesearch`{.literal}, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ sesearch -A -s httpd_t -c file -p read
    …
    allow httpd_t httpd_t:file { append getattr ioctl lock open read write };
    allow httpd_t httpd_tmp_t:file { append create getattr ioctl link lock map open read rename setattr unlink write };
    …
    ```

7.  If none of the previous solutions cover your scenario, you can add a custom rule to the SELinux policy. See the [Creating a local SELinux policy module](#creating-a-local-selinux-policy-module "5.4. Creating a local SELinux policy module") section for more information.

### [4.4. Managing access to non-standard shared directories for unprivileged SELinux users](#managing-access-to-non-standard-shared-directories-for-unprivileged-selinux-users) {#managing-access-to-non-standard-shared-directories-for-unprivileged-selinux-users .title}

Configure access to a non-standard shared directory for the unprivileged SELinux user `user_u`{.literal}. This process restricts access by finding and mapping the appropriate SELinux file type to the directory.

The `user_u`{.literal} user has the default role `user_r`{.literal} and the default domain `user_t`{.literal}. See the `seinfo(1)`{.literal}, `semanage-fcontext(8)`{.literal}, and `user_selinux(8)`{.literal} man pages on your system for more information about the related commands and the generic unprivileged SELinux user `user_u`{.literal}.

**Prerequisites**

-   The `selinux-policy-doc`{.literal} and `setools-console`{.literal} packages are installed on your system.

**Procedure**

1.  Open the `user_selinux(8)`{.literal} man page:

    ``` {.language-plaintext tabindex="-1"}
    $ man user_selinux
    ```

    In the `MANAGED FILES`{.literal} section, find an attribute or a type that corresponds with your scenario. For example, the `user_home_type`{.literal} attribute.

2.  Optional: To list all types assigned to an attribute, use the `seinfo`{.literal} command with the `-x`{.literal} and `-a`{.literal} options, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ seinfo -x -a user_home_type

    Type Attributes: 1
       attribute user_home_type;
    …
        chrome_sandbox_home_t
        config_home_t
        cvs_home_t
        data_home_t
        dbus_home_t
        fetchmail_home_t
        gconf_home_t
        git_user_content_t
    …
    ```

3.  After you identify a candidate for the corresponding type, the `data_home_t`{.literal} type in this example, check its SELinux mapping:

    ``` {.language-plaintext tabindex="-1"}
    $ semanage fcontext -l | grep data_home_t
    …
    /root/\.local/share(/.*)?                          all files          system_u:object_r:data_home_t:s0
    …
    ```

4.  Map the corresponding type to a directory that you want to make accessible for `user_u`{.literal}, for example, `/shared-data`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ semanage fcontext -a -t data_home_t '/shared-data(/.*)?'
    ```

**Verification**

1.  Check the mapping of the directory you configured:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -l | grep "shared-data"
    /shared-data(/.*)?                              all files       system_u:object_r:data_home_t:s0
    ```

2.  Log in as a Linux user mapped to the `user_u`{.literal} SELinux user, and verify you can access the directory.

**Additional resources**

-   [Managing confined and unconfined users](#managing-confined-and-unconfined-users "Chapter 3. Managing confined and unconfined users")

## [Chapter 5. Troubleshooting problems related to SELinux](#troubleshooting-problems-related-to-selinux) {#chapter-5.-troubleshooting-problems-related-to-selinux .title}

If you plan to enable SELinux on systems where it has been previously disabled, or if you run a service in a non-standard configuration, you might need to troubleshoot situations that could be blocked by SELinux. Note that in most cases, SELinux denials are signs of misconfiguration.

### [5.1. Identifying SELinux denials](#identifying-selinux-denials) {#identifying-selinux-denials .title}

Identify problems related to SELinux by searching Audit logs for Access Vector Cache (AVC) denial messages. Checking the AVC logs helps quickly determine if SELinux is blocking your intended operation.

When your scenario is blocked by SELinux, the `/var/log/audit/audit.log`{.literal} file is the first place to check for more information about a denial. To query Audit logs, use the `ausearch`{.literal} tool.

Follow only the necessary steps from this procedure; in most cases, you need to perform just step 1.

**Procedure**

1.  Because the SELinux decisions, such as allowing or disallowing access, are cached and this cache is known as AVC, use the `AVC`{.literal} and `USER_AVC`{.literal} values for the message type parameter, for example:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts recent
    ```

    If there are no matches, check if the Audit daemon is running. If it does not, repeat the denied scenario after you start `auditd`{.literal} and check the Audit log again.

2.  In case `auditd`{.literal} is running, but there are no matches in the output of `ausearch`{.literal}, check messages provided by the `systemd`{.literal} Journal:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -t setroubleshoot
    ```

3.  If SELinux is active and the Audit daemon is not running on your system, then search for certain SELinux messages in the output of the `dmesg`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # dmesg | grep -i -e type=1300 -e type=1400
    ```

4.  Even after the previous three checks, it is still possible that you have not found anything. In this case, AVC denials can be silenced because of `dontaudit`{.literal} rules.

    To temporarily disable `dontaudit`{.literal} rules, allowing all denials to be logged:

    ``` {.language-plaintext tabindex="-1"}
    # semodule -DB
    ```

    After re-running your denied scenario and finding denial messages by using the previous steps, the following command enables `dontaudit`{.literal} rules in the policy again:

    ``` {.language-plaintext tabindex="-1"}
    # semodule -B
    ```

5.  If you apply all four previous steps, and the problem still remains unidentified, consider if SELinux really blocks your scenario:

    -   Switch to permissive mode:

        ``` {.language-plaintext tabindex="-1"}
        # setenforce 0
        $ getenforce
        Permissive
        ```

    -   Repeat your scenario.

    If the problem persists, something other than SELinux is blocking your scenario.

### [5.2. Analyzing SELinux denial messages](#analyzing-selinux-denial-messages) {#analyzing-selinux-denial-messages .title}

Analyze SELinux denial messages to understand the root cause and distinguish policy issues from other misconfigurations.

**Prerequisites**

-   The `policycoreutils-python-utils`{.literal} and `setroubleshoot-server`{.literal} packages are installed on your system.

**Procedure**

1.  List more details about a logged denial using the `sealert`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ sealert -l "*"
    SELinux is preventing /usr/bin/passwd from write access on the file
    /root/test.

    *****  Plugin leaks (86.2 confidence) suggests *****************************

    If you want to ignore passwd trying to write access the test file,
    because you believe it should not need this access.
    Then you should report this as a bug.
    You can generate a local policy module to dontaudit this access.
    Do
    # ausearch -x /usr/bin/passwd --raw | audit2allow -D -M my-passwd
    # semodule -X 300 -i my-passwd.pp

    *****  Plugin catchall (14.7 confidence) suggests **************************
    …
    Raw Audit Messages
    type=AVC msg=audit(1553609555.619:127): avc:  denied  { write } for
    pid=4097 comm="passwd" path="/root/test" dev="dm-0" ino=17142697
    scontext=unconfined_u:unconfined_r:passwd_t:s0-s0:c0.c1023
    tcontext=unconfined_u:object_r:admin_home_t:s0 tclass=file permissive=0
    …
    Hash: passwd,passwd_t,admin_home_t,file,write
    ```

2.  If `sealert`{.literal} returns only generic suggestions, enable full-path auditing for more detailed analysis:

    -   Enable full-path auditing to see full paths to accessed objects and to make additional Linux Audit event fields visible:

        ``` {.language-plaintext tabindex="-1"}
        # auditctl -w /etc/shadow -p w -k shadow-write
        ```

    -   Clear the `setroubleshoot`{.literal} cache:

        ``` {.language-plaintext tabindex="-1"}
        # rm -f /var/lib/setroubleshoot/setroubleshoot.xml
        ```

    -   Reproduce the problem.

    -   Repeat step 1.

        After you finish the process, disable full-path auditing:

        ``` {.language-plaintext tabindex="-1"}
        # auditctl -W /etc/shadow -p w -k shadow-write
        ```

3.  If `sealert`{.literal} returns only `catchall`{.literal} suggestions or suggests adding a new rule by using the `audit2allow`{.literal} command, match your problem with examples listed and explained in [SELinux denials in the Audit log](#selinux-denials-in-the-audit-log "5.5. SELinux denials in the Audit log").

### [5.3. Fixes of analyzed SELinux denials](#fixing-analyzed-selinux-denials) {#fixes-of-analyzed-selinux-denials .title}

Fix SELinux policy problems, prioritizing labeling issues and configuration adjustments suggested by the `sealert`{.literal} command. Avoid immediately generating local policy modules unless other troubleshooting steps fail.

In most cases, suggestions provided by `sealert`{.literal} provide the correct guidance about how to fix problems related to the SELinux policy. See [Analyzing SELinux denial messages](#analyzing-selinux-denial-messages "5.2. Analyzing SELinux denial messages") for information on how to use `sealert`{.literal} to analyze SELinux denials.

Be careful when the tool suggests using the `audit2allow`{.literal} command for configuration changes. You should not use `audit2allow`{.literal} to generate a local policy module as your first option when you see an SELinux denial. Troubleshooting should start with checking whether the problem is in the labeling. The second most common case is that you changed a process configuration, and you forgot to tell SELinux about it.

Labeling problems

:   A common cause of labeling problems is when a non-standard directory is used for a service. For example, instead of using `/var/www/html/`{.literal} for a website, an administrator might want to use `/srv/myweb/`{.literal}. On Red Hat Enterprise Linux, the `/srv`{.literal} directory is labeled with the `var_t`{.literal} type. Files and directories created in `/srv`{.literal} inherit this type. Also, newly-created objects in top-level directories, such as `/myserver`{.literal}, can be labeled with the `default_t`{.literal} type. SELinux prevents the Apache HTTP Server (`httpd`{.literal}) from accessing both of these types. To allow access, SELinux must know that the files in `/srv/myweb/`{.literal} are to be accessible by `httpd`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t httpd_sys_content_t "/srv/myweb(/.*)?"
    ```

    This `semanage`{.literal} command adds the context for the `/srv/myweb/`{.literal} directory and all files and directories under it to the SELinux file-context configuration. The `semanage`{.literal} utility does not change the context. As root, use the `restorecon`{.literal} utility to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -R -v /srv/myweb
    ```

Incorrect context

:   The `matchpathcon`{.literal} command checks the context of a file path and compares it to the default label for that path. The following example demonstrates the use of `matchpathcon`{.literal} on a directory that contains incorrectly labeled files:

    ``` {.language-plaintext tabindex="-1"}
    $ matchpathcon -V /var/www/html/*
    /var/www/html/index.html has context unconfined_u:object_r:user_home_t:s0, should be system_u:object_r:httpd_sys_content_t:s0
    /var/www/html/page1.html has context unconfined_u:object_r:user_home_t:s0, should be system_u:object_r:httpd_sys_content_t:s0
    ```

    In this example, the `index.html`{.literal} and `page1.html`{.literal} files are labeled with the `user_home_t`{.literal} type. This type is used for files in user home directories. Using the `mv`{.literal} command to move files from your home directory might result in files being labeled with the `user_home_t`{.literal} type. This type should not exist outside of home directories. Use the `restorecon`{.literal} utility to restore such files to their correct type:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -v /var/www/html/index.html
    restorecon reset /var/www/html/index.html context unconfined_u:object_r:user_home_t:s0->system_u:object_r:httpd_sys_content_t:s0
    ```

    To restore the context for all files under a directory, use the `-R`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -R -v /var/www/html/
    restorecon reset /var/www/html/page1.html context unconfined_u:object_r:samba_share_t:s0->system_u:object_r:httpd_sys_content_t:s0
    restorecon reset /var/www/html/index.html context unconfined_u:object_r:samba_share_t:s0->system_u:object_r:httpd_sys_content_t:s0
    ```

Confined applications configured in non-standard ways

:   You can run services in various ways. To account for that, you must specify how you run your services. You can achieve this through SELinux booleans that enable changing parts of the SELinux policy at runtime. This enables changes, such as allowing services access to NFS volumes, without reloading or recompiling SELinux policy. Also, running services on non-default port numbers requires policy configuration to be updated using the `semanage`{.literal} command.

    For example, to allow the Apache HTTP Server to communicate with MariaDB, enable the `httpd_can_network_connect_db`{.literal} boolean:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool -P httpd_can_network_connect_db on
    ```

    Note that the `-P`{.literal} option makes the setting persistent across system restarts.

    If SELinux denies access for a particular service, use the `getsebool`{.literal} and `grep`{.literal} utilities to see if any booleans are available to allow access. For example, use the `getsebool -a | grep ftp`{.literal} command to search for FTP related booleans:

    ``` {.language-plaintext tabindex="-1"}
    $ getsebool -a | grep ftp
    ftpd_anon_write --> off
    ftpd_full_access --> off
    ftpd_use_cifs --> off
    ftpd_use_nfs --> off

    ftpd_connect_db --> off
    httpd_enable_ftp_server --> off
    tftp_anon_write --> off
    ```

    To get a list of booleans and to discover if they are enabled or disabled, use the `getsebool -a`{.literal} command. To get a list of booleans, including their meaning and states, install the `selinux-policy-devel`{.literal} package and use the `semanage boolean -l`{.literal} command as root.

Port numbers

:   Depending on policy configuration, services can only be allowed to run on certain port numbers. Attempting to change the port a service runs on without changing policy might result in the service failing to start. For example, run the `semanage port -l | grep http`{.literal} command as root to list `http`{.literal} related ports:

    ``` {.language-plaintext tabindex="-1"}
    # semanage port -l | grep http
    http_cache_port_t              tcp      3128, 8080, 8118
    http_cache_port_t              udp      3130
    http_port_t                    tcp      80, 443, 488, 8008, 8009, 8443
    pegasus_http_port_t            tcp      5988
    pegasus_https_port_t           tcp      5989
    ```

    The `http_port_t`{.literal} port type defines the ports Apache HTTP Server can listen on, which in this case, are TCP ports 80, 443, 488, 8008, 8009, and 8443. If an administrator configures `httpd.conf`{.literal} so that `httpd`{.literal} listens on port 9876 (`Listen 9876`{.literal}), but policy is not updated to reflect this, the following command fails:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start httpd.service
    Job for httpd.service failed. See 'systemctl status httpd.service' and 'journalctl -xn' for details.

    # systemctl status httpd.service
    httpd.service - The Apache HTTP Server
       Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled)
       Active: failed (Result: exit-code) since Thu 2013-08-15 09:57:05 CEST; 59s ago
      Process: 16874 ExecStop=/usr/sbin/httpd $OPTIONS -k graceful-stop (code=exited, status=0/SUCCESS)
      Process: 16870 ExecStart=/usr/sbin/httpd $OPTIONS -DFOREGROUND (code=exited, status=1/FAILURE)
    ```

    An SELinux denial message similar to the following is logged to `/var/log/audit/audit.log`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    type=AVC msg=audit(1225948455.061:294): avc:  denied  { name_bind } for  pid=4997 comm="httpd" src=9876 scontext=unconfined_u:system_r:httpd_t:s0 tcontext=system_u:object_r:port_t:s0 tclass=tcp_socket
    ```

    To allow `httpd`{.literal} to listen on a port that is not listed for the `http_port_t`{.literal} port type, use the `semanage port`{.literal} command to assign a different label to the port:

    ``` {.language-plaintext tabindex="-1"}
    # semanage port -a -t http_port_t -p tcp 9876
    ```

    The `-a`{.literal} option adds a new record; the `-t`{.literal} option defines a type; and the `-p`{.literal} option defines a protocol. The last argument is the port number to add.

Corner cases, evolving or broken applications, and compromised systems

:   Applications can contain bugs that cause SELinux to deny access. Also, SELinux rules must evolve. The SELinux policy might lack a rule for an application running in a specific way, potentially causing it to deny access even though the application is working as expected. For example, if a new version of PostgreSQL is released, it might perform actions the current policy does not account for, resulting in denied access even though it should be allowed.

    For these situations, after access is denied, use the `audit2allow`{.literal} utility to create a custom policy module to allow access. You can report missing rules in the SELinux policy by filing a support case on the [**Red Hat Customer Portal**](https://access.redhat.com/support/cases/). Mention the `selinux-policy`{.literal} component and include the output of the `audit2allow -w -a`{.literal} and `audit2allow -a`{.literal} commands in the case.

    If an application asks for major security privileges, it could be a signal that the application is compromised. Use intrusion detection tools to inspect such suspicious behavior.

    The **[Solution Engine](https://access.redhat.com/solution-engine/)** on the [Red Hat Customer Portal](https://access.redhat.com/) can also provide guidance in the form of an article containing a possible solution for the same or very similar problem you have. Select the relevant product and version and use SELinux-related keywords, such as *selinux* or *avc*, together with the name of your blocked service or application, for example: `selinux samba`{.literal}.

### [5.4. Creating a local SELinux policy module](#creating-a-local-selinux-policy-module) {#creating-a-local-selinux-policy-module .title}

Create and add specific local SELinux policy modules to fix problems related to known issues or implement specific Red Hat solutions. Use extreme caution and only apply rules provided directly by Red Hat.

Adding specific SELinux policy modules to an active SELinux policy can fix certain problems with the SELinux policy. You can use this procedure to fix a specific Known Issue described in [Red Hat release notes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10) or to implement a particular [Red Hat Solution](https://access.redhat.com/solutions).

Warning

Use only rules provided by Red Hat. Red Hat does not support creating SELinux policy modules with custom rules because this falls outside of the [Production Support Scope of Coverage](https://access.redhat.com/support/offerings/production/soc/). If you are not an expert, contact your Red Hat sales representative and request consulting services.

**Prerequisites**

-   The `setools-console`{.literal} and `audit`{.literal} packages for verification.

**Procedure**

1.  Open a new `.cil`{.literal} file with a text editor, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi <local_module>.cil
    ```

    To keep your local modules better organized, use the `local_`{.literal} prefix in the names of local SELinux policy modules.

2.  Insert the custom rules from a Known Issue or a Red Hat Solution.

    Important

    Do not write your own rules. Use only the rules provided in a specific Known Issue or Red Hat Solution.

    -   For example, to resolve [SELinux denies cups-lpd read access to cups.sock in RHEL](https://access.redhat.com/solutions/5729251), insert the following rule:

        ``` {.language-plaintext tabindex="-1"}
        (allow cupsd_lpd_t cupsd_var_run_t (sock_file (read)))
        ```

        The example solution is fixed permanently for {ProductShortName} in [RHBA-2021:4420](https://access.redhat.com/errata/RHBA-2021:4420). Therefore, the parts of this procedure specific to this solution do not affect updated {ProductShortName} 8 and 9 systems, and are included only as examples of syntax.

        You can use either of the two SELinux rule syntaxes, Common Intermediate Language (CIL) and m4. For example, `(allow cupsd_lpd_t cupsd_var_run_t (sock_file (read)))`{.literal} in CIL is equivalent to the following in m4:

        ``` {.language-plaintext tabindex="-1"}
        module local_cupslpd-read-cupssock 1.0;

        require {
            type cupsd_var_run_t;
            type cupsd_lpd_t;
            class sock_file read;
        }

        #============= cupsd_lpd_t ==============
        allow cupsd_lpd_t cupsd_var_run_t:sock_file read;
        ```

3.  Save and close the file.

4.  Install the policy module:

    ``` {.language-plaintext tabindex="-1"}
    # semodule -i <local_module>.cil
    ```

    If you want to remove a local policy module you created by using `semodule -i`{.literal}, refer to the module name without the `.cil`{.literal} suffix. To remove a local policy module, use `semodule -r `{.literal}*`<local_module>`{.literal}*.

5.  Restart any services related to the rules:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart <service_name>
    ```

**Verification**

1.  List the local modules installed in your SELinux policy:

    ``` {.language-plaintext tabindex="-1"}
    # semodule -lfull | grep "local_"
    400 local_module  cil
    ```

    Because local modules have priority `400`{.literal}, you can filter them from the list also by using that value, for example, by using the `semodule -lfull | grep -v ^100`{.literal} command.

2.  Search the SELinux policy for the relevant allow rules:

    ``` {.language-plaintext tabindex="-1"}
    # sesearch -A --source=<SOURCENAME> --target=<TARGETNAME> --class=<CLASSNAME> --perm=<P1>,<P2>
    ```

    Where *`<SOURCENAME>`{.literal}* is the source SELinux type, *`<TARGETNAME>`{.literal}* is the target SELinux type, *`<CLASSNAME>`{.literal}* is the security class or object class name, and *`<P1>`{.literal}* and *`<P2>`{.literal}* are the specific permissions of the rule.

    For example, to resolve [SELinux denies cups-lpd read access to cups.sock in RHEL](https://access.redhat.com/solutions/5729251):

    ``` {.language-plaintext tabindex="-1"}
    # sesearch -A --source=cupsd_lpd_t --target=cupsd_var_run_t --class=sock_file --perm=read
    allow cupsd_lpd_t cupsd_var_run_t:sock_file { append getattr open read write };
    ```

    The last line should now include the `read`{.literal} operation.

3.  Verify that the relevant service runs confined by SELinux:

    a.  Identify the process related to the relevant service:

        ``` {.language-plaintext tabindex="-1"}
        $ systemctl status <service_name>
        ```

    b.  Check the SELinux context of the process listed in the output of the previous command:

        ``` {.language-plaintext tabindex="-1"}
        $ ps -efZ | grep <process_name>
        ```

4.  Verify that the service does not cause any SELinux denials:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -m AVC -i -ts recent
    <no matches>
    ```

    The `-i`{.literal} option interprets the numeric values into human-readable text.

**Additional resources**

-   [How to create a custom SELinux policy module wisely (Red Hat Knowledgebase)](https://access.redhat.com/articles/5494701)
-   [Troubleshooting problems related to SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/troubleshooting-problems-related-to-selinux)

### [5.5. SELinux denials in the Audit log](#selinux-denials-in-the-audit-log) {#selinux-denials-in-the-audit-log .title}

Interpret SELinux denial messages recorded by the Linux Audit system in the `/var/log/audit/audit.log`{.literal} file. Understanding fields such as source context and target context is essential for resolving policy errors.

The Linux Audit system stores log entries in the `/var/log/audit/audit.log`{.literal} file by default. To list only SELinux-related records, use the `ausearch`{.literal} command with the message type parameter set to `AVC`{.literal} and `AVC_USER`{.literal} at a minimum, for example:

``` {.language-plaintext tabindex="-1"}
# ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR
```

An SELinux denial entry in the Audit log file can look as follows:

``` {.language-plaintext tabindex="-1"}
type=AVC msg=audit(1395177286.929:1638): avc:  denied  { read } for  pid=6591 comm="httpd" name="webpages" dev="0:37" ino=2112 scontext=system_u:system_r:httpd_t:s0 tcontext=system_u:object_r:nfs_t:s0 tclass=dir
```

The most important parts of this entry are:

-   `avc: denied`{.literal} - the action performed by SELinux and recorded in Access Vector Cache (AVC)
-   `{ read }`{.literal} - the denied action
-   `pid=6591`{.literal} - the process identifier of the subject that tried to perform the denied action
-   `comm="httpd"`{.literal} - the name of the command that was used to call the analyzed process
-   `httpd_t`{.literal} - the SELinux type of the process
-   `nfs_t`{.literal} - the SELinux type of the object affected by the process action
-   `tclass=dir`{.literal} - the target object class

The previous log entry can be translated to:

*SELinux denied the `httpd`{.literal} process with PID 6591 and the `httpd_t`{.literal} type to read from a directory with the `nfs_t`{.literal} type.*

The following SELinux denial message occurs when the Apache HTTP Server attempts to access a directory labeled with a type for the Samba suite:

``` {.language-plaintext tabindex="-1"}
type=AVC msg=audit(1226874073.147:96): avc:  denied  { getattr } for  pid=2465 comm="httpd" path="/var/www/html/file1" dev=dm-0 ino=284133 scontext=unconfined_u:system_r:httpd_t:s0 tcontext=unconfined_u:object_r:samba_share_t:s0 tclass=file
```

-   `{ getattr }`{.literal} - the `getattr`{.literal} entry indicates the source process was trying to read the target file's status information. This occurs before reading files. SELinux denies this action because the process accesses the file and it does not have an appropriate label. Commonly seen permissions include `getattr`{.literal}, `read`{.literal}, and `write`{.literal}.
-   `path="/var/www/html/file1"`{.literal} - the path to the object (target) the process attempted to access.
-   `scontext="unconfined_u:system_r:httpd_t:s0"`{.literal} - the SELinux context of the process (source) that attempted the denied action. In this case, it is the SELinux context of the Apache HTTP Server, which is running with the `httpd_t`{.literal} type.
-   `tcontext="unconfined_u:object_r:samba_share_t:s0"`{.literal} - the SELinux context of the object (target) the process attempted to access. In this case, it is the SELinux context of `file1`{.literal}.

This SELinux denial can be translated to:

*SELinux denied the `httpd`{.literal} process with PID 2465 to access the `/var/www/html/file1`{.literal} file with the `samba_share_t`{.literal} type, which is not accessible to processes running in the `httpd_t`{.literal} domain unless configured otherwise.*

### [5.6. Additional resources](#troubleshooting-problems-related-to-selinux_56-additional-resources) {#additional-resources-1 .title}

-   [Basic SELinux Troubleshooting in CLI (Red Hat Knowledgebase)](https://access.redhat.com/articles/2191331)
-   [What is SELinux trying to tell me? The 4 key causes of SELinux errors (Fedora People)](https://fedorapeople.org/~dwalsh/SELinux/Presentations/selinux_four_things.pdf)

## [Chapter 6. Using Multi-Level Security (MLS)](#using-multi-level-security-mls) {#chapter-6.-using-multi-level-security-mls .title}

Use Multi-Level Security (MLS) and Multi-Category Security (MCS) features in SELinux to refine access control. With MLS and MCS, you can restrict access based on data sensitivity and organizational categories.

The MLS policy uses *levels* of clearance as initially designed by the US defense community. MLS meets a very narrow set of security requirements based on information management in rigidly controlled environments such as the military.

Using MLS is complex and does not map well to typical use cases.

### [6.1. Multi-Level Security (MLS)](#multi-level-security-mls) {#multi-level-security-mls .title}

Multi-Level Security (MLS) confines users and processes based on data sensitivity levels by using the Bell-La Padula Model. This configuration prevents unauthorized access to highly sensitive information by enforcing the \"no read up, no write down\" principle.

The Multi-Level Security (MLS) technology classifies data hierarchically by using information security levels, for example:

-   \[lowest\] Unclassified
-   \[low\] Confidential
-   \[high\] Secret
-   \[highest\] Top secret

By default, the MLS SELinux policy uses 16 sensitivity levels:

-   `s0`{.literal} is the least sensitive.
-   `s15`{.literal} is the most sensitive.

MLS uses specific terminology to address sensitivity levels:

-   Users and processes are called **subjects**, whose sensitivity level is called **clearance**.
-   Files, devices, and other passive components of the system are called **objects**, whose sensitivity level is called **classification**.

To implement MLS, SELinux uses the **Bell-La Padula Model** (BLP) model. This model specifies how information can flow within the system based on labels attached to each subject and object.

The basic principle of BLP is \"**No read up, no write down.**\" This means that users can only read files at their own sensitivity level and lower, and data can flow only from lower levels to higher levels, and never the reverse.

The MLS SELinux policy, which is the implementation of MLS on RHEL, applies a modified principle called **Bell-La Padula with write equality**. This means that users can read files at their own sensitivity level and lower, but can write only at exactly their own level. This prevents, for example, low-clearance users from writing content into top-secret files.

For example, by default, a user with clearance level `s2`{.literal}:

-   Can read files with sensitivity levels `s0`{.literal}, `s1`{.literal}, and `s2`{.literal}.
-   Cannot read files with sensitivity level `s3`{.literal} and higher.
-   Can modify files with sensitivity level of exactly `s2`{.literal}.
-   Cannot modify files with sensitivity level other than `s2`{.literal}.

Note

Security administrators can adjust this behavior by modifying the system's SELinux policy. For example, they can allow users to modify files at lower levels, which increases the file's sensitivity level to the user's clearance level.

In practice, users are typically assigned to a range of clearance levels, for example `s1-s2`{.literal}. A user can read files with sensitivity levels lower than the user's maximum level, and write to any files within that range.

For example, by default, a user with a clearance range `s1-s2`{.literal}:

-   Can read files with sensitivity levels `s0`{.literal} and `s1`{.literal}.
-   Cannot read files with sensitivity level `s2`{.literal} and higher.
-   Can modify files with sensitivity level `s1`{.literal}.
-   Cannot modify files with sensitivity level other than `s1`{.literal}.
-   Can change own clearance level to `s2`{.literal}.

The security context for a non-privileged user in an MLS environment is, for example:

``` {.language-plaintext tabindex="-1"}
user_u:user_r:user_t:s1
```

Where:

`user_u`{.literal}
:   Is the SELinux user.

`user_r`{.literal}
:   Is the SELinux role.

`user_t`{.literal}
:   Is the SELinux type.

`s1`{.literal}
:   Is the range of MLS sensitivity levels.

The system always combines MLS access rules with conventional file access permissions. For example, if a user with a security level of \"Secret\" uses Discretionary Access Control (DAC) to block access to a file by other users, even \"Top Secret\" users cannot access that file. A high security clearance does not automatically permit a user to browse the entire file system.

Users with top-level clearances do not automatically acquire administrative rights on multi-level systems. While they might have access to all sensitive information about the system, this is different from having administrative rights.

In addition, administrative rights do not provide access to sensitive information. For example, even when someone logs in as `root`{.literal}, they still cannot read top-secret information.

You can further adjust access within an MLS system by using categories. With Multi-Category Security (MCS), you can define categories such as projects or departments, and users can only access files in the categories to which they are assigned.

**Additional resources**

-   [Using Multi-Category Security (MCS) for data confidentiality](#using-multi-category-security-mcs-for-data-confidentiality "Chapter 7. Using Multi-Category Security (MCS) for data confidentiality")

### [6.2. SELinux roles in MLS](#selinux-roles-in-mls) {#selinux-roles-in-mls .title}

The SELinux policy maps each Linux user to an SELinux user. This allows Linux users to inherit the restrictions of SELinux users. Note that the MLS policy removes the default unconfined module, limiting privileges even for the root user.

Important

The MLS policy does not contain the `unconfined`{.literal} module, including unconfined users, types, and roles. As a result, users that would be unconfined, including `root`{.literal}, cannot access every object and perform every action they could in the targeted policy.

You can customize the permissions for confined users in your SELinux policy according to specific needs by adjusting the booleans in policy. You can determine the current state of these booleans by using the `semanage boolean -l`{.literal} command. To list all SELinux users, their SELinux roles, and MLS/MCS levels and ranges, use the `semanage user -l`{.literal} command as `root`{.literal}.

+----------------------+----------------------+------------------------+
| User                 | Default role         | Additional roles       |
+:=====================+:=====================+:=======================+
| `guest_u`{.literal}  | `guest_r`{.literal}  |                        |
+----------------------+----------------------+------------------------+
| `xguest_u`{.literal} | `xguest_r`{.literal} |                        |
+----------------------+----------------------+------------------------+
| `user_u`{.literal}   | `user_r`{.literal}   |                        |
+----------------------+----------------------+------------------------+
| `staff_u`{.literal}  | `staff_r`{.literal}  | `auditadm_r`{.literal} |
+----------------------+----------------------+------------------------+
|                      |                      | `secadm_r`{.literal}   |
+----------------------+----------------------+------------------------+
|                      |                      | `sysadm_r`{.literal}   |
+----------------------+----------------------+------------------------+
|                      |                      | `staff_r`{.literal}    |
+----------------------+----------------------+------------------------+
| `sysadm_u`{.literal} | `sysadm_r`{.literal} |                        |
+----------------------+----------------------+------------------------+
| `root`{.literal}     | `staff_r`{.literal}  | `auditadm_r`{.literal} |
+----------------------+----------------------+------------------------+
|                      |                      | `secadm_r`{.literal}   |
+----------------------+----------------------+------------------------+
|                      |                      | `sysadm_r`{.literal}   |
+----------------------+----------------------+------------------------+
|                      |                      | `system_r`{.literal}   |
+----------------------+----------------------+------------------------+
| `system_u`{.literal} | `system_r`{.literal} |                        |
+----------------------+----------------------+------------------------+

: Table 6.1. Roles of SELinux users in MLS

Show more

Note that `system_u`{.literal} is a special user identity for system processes and objects, and `system_r`{.literal} is the associated role. Administrators must never associate this `system_u`{.literal} user and the `system_r`{.literal} role to a Linux user. Also, `unconfined_u`{.literal} and `root`{.literal} are unconfined users. For these reasons, the roles associated to these SELinux users are not included in the following table Types and access of SELinux roles.

Each SELinux role corresponds to an SELinux type and provides specific access rights.

+------------------------+------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| Role                   | Type                   | Login using X Window System                                          | `su`{.literal} and `sudo`{.literal} | Execute in home directory and `/tmp`{.literal} (default) | Networking                                     |
+:=======================+:=======================+:=====================================================================+:====================================+:=========================================================+:===============================================+
| `guest_r`{.literal}    | `guest_t`{.literal}    | no                                                                   | no                                  | yes                                                      | no                                             |
+------------------------+------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `xguest_r`{.literal}   | `xguest_t`{.literal}   | yes                                                                  | no                                  | yes                                                      | web browsers only (Mozilla Firefox, GNOME Web) |
+------------------------+------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `user_r`{.literal}     | `user_t`{.literal}     | yes                                                                  | no                                  | yes                                                      | yes                                            |
+------------------------+------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `staff_r`{.literal}    | `staff_t`{.literal}    | yes                                                                  | only `sudo`{.literal}               | yes                                                      | yes                                            |
+------------------------+------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `auditadm_r`{.literal} | `auditadm_t`{.literal} |                                                                      | yes                                 | yes                                                      | yes                                            |
+------------------------+------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `secadm_r`{.literal}   | `secadm_t`{.literal}   |                                                                      | yes                                 | yes                                                      | yes                                            |
+------------------------+------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+
| `sysadm_r`{.literal}   | `sysadm_t`{.literal}   | only when the `xdm_sysadm_login`{.literal} boolean is `on`{.literal} | yes                                 | yes                                                      | yes                                            |
+------------------------+------------------------+----------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------+------------------------------------------------+

: Table 6.2. Types and access of SELinux roles in MLS

Show more

-   By default, the `sysadm_r`{.literal} role has the rights of the `secadm_r`{.literal} role, which means a user with the `sysadm_r`{.literal} role can manage the security policy. If this does not correspond to your use case, you can separate the two roles by disabling the `sysadm_secadm`{.literal} module in the policy. For additional information, see [Separating system administration from security administration in MLS](#separating-system-administration-from-security-administration-in-mls "6.8. Separating system administration from security administration in MLS").
-   You can use non-login roles `dbadm_r`{.literal}, `logadm_r`{.literal}, and `webadm_r`{.literal} for a subset of administrative tasks. By default, these roles are not associated with any SELinux user.

### [6.3. Switching the SELinux policy to MLS](#switching-the-selinux-policy-to-mls) {#switching-the-selinux-policy-to-mls .title}

Switch the SELinux policy from targeted mode to Multi-Level Security (MLS) mode. Ensure you switch to permissive mode first to relabel files, preventing potential boot failures.

Important

Do not use the MLS policy on a system that is running the X Window System. Furthermore, when you relabel the file system with MLS labels, the system might prevent confined domains from accessing, which prevents your system from starting correctly. Therefore, ensure that you switch SELinux to permissive mode before you relabel the files. On most systems, you see many SELinux denials after switching to MLS, and many of them are not trivial to fix.

**Procedure**

1.  Install the `selinux-policy-mls`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install selinux-policy-mls
    ```

2.  Open the `/etc/selinux/config`{.literal} file in a text editor of your choice, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/selinux/config
    ```

3.  Change SELinux mode from enforcing to permissive and switch from the targeted policy to MLS:

    ``` {.language-plaintext tabindex="-1"}
    SELINUX=permissive
    SELINUXTYPE=mls
    ```

    Save the changes, and quit the editor.

4.  Before you enable the MLS policy, you must relabel each file on the file system with an MLS label:

    ``` {.language-plaintext tabindex="-1"}
    # fixfiles -F onboot
    System relabels on next boot
    ```

5.  Restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

6.  Check for SELinux denials:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts recent -i
    ```

    Because the previous command does not cover all scenarios, see [Troubleshooting problems related to SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/troubleshooting-problems-related-to-selinux) for guidance on identifying, analyzing, and fixing SELinux denials.

7.  After you ensure that there are no problems related to SELinux on your system, switch SELinux back to enforcing mode by changing the corresponding option in `/etc/selinux/config`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    SELINUX=enforcing
    ```

8.  Restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

    Important

    If your system does not start or you are not able to log in after you switch to MLS, add the `enforcing=0`{.literal} parameter to your kernel command line. See [Changing SELinux modes at boot time](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/changing-selinux-states-and-modes#changing-selinux-modes-at-boot-time) for more information.

    Also note that in MLS, SSH logins as the `root`{.literal} user mapped to the `sysadm_r`{.literal} SELinux role differ from logging in as `root`{.literal} in `staff_r`{.literal}. Before you start your system in MLS for the first time, consider allowing SSH logins as `sysadm_r`{.literal} by setting the `ssh_sysadm_login`{.literal} SELinux boolean to `1`{.literal}. To enable `ssh_sysadm_login`{.literal} later, already in MLS, you must log in as `root`{.literal} in `staff_r`{.literal}, switch to `root`{.literal} in `sysadm_r`{.literal} by using the `newrole -r sysadm_r`{.literal} command, and then set the boolean to `1`{.literal}.

**Verification**

1.  Verify that SELinux runs in enforcing mode:

    ``` {.language-plaintext tabindex="-1"}
    # getenforce
    Enforcing
    ```

2.  Check that the status of SELinux returns the `mls`{.literal} value:

    ``` {.language-plaintext tabindex="-1"}
    # sestatus | grep mls
    Loaded policy name:             mls
    ```

### [6.4. Establishing user clearance in MLS](#establishing-user-clearance-in-mls) {#establishing-user-clearance-in-mls .title}

Assign specific security clearance levels to confined SELinux users after enabling MLS. This controls their access, preventing them from reading higher-level objects or writing to files at different sensitivity levels.

By default, a user with a given security clearance:

-   Cannot read objects that have a higher sensitivity level.
-   Cannot write to objects at a different sensitivity level.

**Prerequisites**

-   The SELinux policy is set to `mls`{.literal}.

-   The SELinux mode is set to `enforcing`{.literal}.

-   The `policycoreutils-python-utils`{.literal} package is installed.

-   A user assigned to an SELinux confined user:

    -   For a non-privileged user, assigned to `user_u`{.literal} (*example_user* in the following procedure).
    -   For a privileged user, assigned to `staff_u`{.literal} (*staff* in the following procedure) .

Important

Make sure that the users have been created when the MLS policy was active. Users created in other SELinux policies cannot be used in MLS.

**Procedure**

1.  Optional: To prevent adding errors to your SELinux policy, switch to the `permissive`{.literal} SELinux mode, which facilitates troubleshooting:

    ``` {.language-plaintext tabindex="-1"}
    # setenforce 0
    ```

    Note that **in permissive mode, SELinux does not enforce the active policy** but only logs Access Vector Cache (AVC) messages, which can be then used for troubleshooting and debugging.

2.  Define a clearance range for the `staff_u`{.literal} SELinux user. For example, this command sets the clearance range from `s1`{.literal} to `s15`{.literal} with `s1`{.literal} being the default clearance level:

    ``` {.language-plaintext tabindex="-1"}
    # semanage user -m -L s1 -r s1-s15 staff_u
    ```

3.  Generate SELinux file context configuration entries for user home directories:

    ``` {.language-plaintext tabindex="-1"}
    # genhomedircon
    ```

4.  Restore file security contexts to default:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -R -F -v /home/
    Relabeled /home/staff from staff_u:object_r:user_home_dir_t:s0 to staff_u:object_r:user_home_dir_t:s1
    Relabeled /home/staff/.bash_logout from staff_u:object_r:user_home_t:s0 to staff_u:object_r:user_home_t:s1
    Relabeled /home/staff/.bash_profile from staff_u:object_r:user_home_t:s0 to staff_u:object_r:user_home_t:s1
    Relabeled /home/staff/.bashrc from staff_u:object_r:user_home_t:s0 to staff_u:object_r:user_home_t:s1
    ```

5.  Assign a clearance level to the user:

    ``` {.language-plaintext tabindex="-1"}
    # semanage login -m -r s1 example_user
    ```

    Where *`s1`{.literal}* is the clearance level assigned to the user.

6.  Relabel the user's home directory to the user's clearance level:

    ``` {.language-plaintext tabindex="-1"}
    # chcon -R -l s1 /home/example_user
    ```

7.  Optional: If you previously switched to the `permissive`{.literal} SELinux mode, and after you verify that everything works as expected, switch back to the `enforcing`{.literal} SELinux mode:

    ``` {.language-plaintext tabindex="-1"}
    # setenforce 1
    ```

**Verification**

1.  Verify that the user is mapped to the correct SELinux user and has the correct clearance level assigned:

    ``` {.language-plaintext tabindex="-1"}
    # semanage login -l
    Login Name      SELinux User         MLS/MCS Range        Service
    __default__     user_u               s0-s0                *
    example_user    user_u               s1                   *
    …
    ```

2.  Log in as the user within MLS.

3.  Verify that the user's security level works correctly:

    Warning

    The files you use for verification should not contain any sensitive information in case the configuration is incorrect and the user actually can access the files without authorization.

    a.  Verify that the user cannot read a file with a higher-level sensitivity.
    b.  Verify that the user can write to a file with the same sensitivity.
    c.  Verify that the user can read a file with a lower-level sensitivity.

**Additional resources**

-   [Switching the SELinux policy to MLS](#switching-the-selinux-policy-to-mls "6.3. Switching the SELinux policy to MLS")
-   [Adding a new user as an SELinux-confined user](#adding-a-new-user-as-an-selinux-confined-user "3.6. Adding a new user as an SELinux-confined user")
-   [Permanent changes in SELinux states and modes](#changing-selinux-states-and-modes "Chapter 2. Changing SELinux states and modes")
-   [Troubleshooting problems related to SELinux](#troubleshooting-problems-related-to-selinux "Chapter 5. Troubleshooting problems related to SELinux")
-   [Basic SELinux Troubleshooting in CLI (Red Hat Knowledgebase)](https://access.redhat.com/articles/2191331)

### [6.5. Changing a user's clearance level within the defined security range in MLS](#changing-a-users-clearance-level-within-the-defined-security-range-in-mls) {#changing-a-users-clearance-level-within-the-defined-security-range-in-mls .title}

Change your current clearance level in MLS within the predefined range assigned by the administrator. With this capability, you can modify lower-sensitivity files without unintentionally elevating their classification level to your highest security clearance.

As a user in Multi-Level Security (MLS), you can never exceed the upper limit of your range or reduce your level below the lower limit of your range. For example, you can modify lower-sensitivity files without increasing their sensitivity level to your highest clearance level.

For example, as a user assigned to range `s1-s3`{.literal}:

-   You can switch to levels `s1`{.literal}, `s2`{.literal}, and `s3`{.literal}.
-   You can switch to ranges `s1-s2`{.literal}, and `s2-s3`{.literal}.
-   You cannot switch to ranges `s0-s3`{.literal} or `s1-s4`{.literal}.

Switching to a different level opens a new shell with the different clearance. This means you cannot return to your original clearance level in the same way as decreasing it. However, you can always return to the previous shell by entering `exit`{.literal}.

**Prerequisites**

-   The SELinux policy is set to `mls`{.literal}.
-   SELinux mode is set to `enforcing`{.literal}.
-   You can log in as a user assigned to a range of MLS clearance levels.

**Procedure**

1.  Log in as the user from a secure terminal.

    Secure terminals are defined in the `/etc/selinux/mls/contexts/securetty_types`{.literal} file. By default, the console is a secure terminal, but SSH is not.

2.  Check the current user's security context:

    ``` {.language-plaintext tabindex="-1"}
    $ id -Z
    user_u:user_r:user_t:s0-s2
    ```

    In this example, the user is assigned to the `user_u`{.literal} SELinux user, `user_r`{.literal} role, `user_t`{.literal} type, and the MLS security range `s0-s2`{.literal}.

3.  Switch to a different security clearance range within the user's clearance range:

    ``` {.language-plaintext tabindex="-1"}
    $ newrole -l s1
    ```

    You can switch to any range whose maximum is lower or equal to your assigned range. Entering a single-level range changes the lower limit of the assigned range. For example, entering `newrole -l s1`{.literal} as a user with a `s0-s2`{.literal} range is equivalent to entering `newrole -l s1-s2`{.literal}.

**Verification**

1.  Display the current user's security context:

    ``` {.language-plaintext tabindex="-1"}
    $ id -Z
    user_u:user_r:user_t:s1-s2
    ```

2.  Return to the previous shell with the original range by terminating the current shell:

    ``` {.language-plaintext tabindex="-1"}
    $ exit
    ```

**Additional resources**

-   [Establishing user clearance in MLS](#establishing-user-clearance-in-mls "6.4. Establishing user clearance in MLS")

### [6.6. Increasing file sensitivity levels in MLS](#increasing-file-sensitivity-levels-in-mls) {#increasing-file-sensitivity-levels-in-mls .title}

Allow MLS users to increase file sensitivity levels by adding a local SELinux policy module. When a user modifies a file, its sensitivity level is automatically raised to the lowest value of the user's current security range.

By default, Multi-Level Security (MLS) users cannot increase file sensitivity levels. However, the security administrator (`secadm_r`{.literal}) can change this default behavior to allow users to increase the sensitivity of files by adding the local module `mlsfilewrite`{.literal} to the system's SELinux policy. Then, users assigned to the SELinux type defined in the policy module can increase file classification levels by modifying the file. Any time a user modifies a file, the file's sensitivity level increases to the lower value of the user's current security range.

The security administrator, when logged in as a user assigned to the `secadm_r`{.literal} role, can change the security levels of files by using the `chcon -l `{.literal}*`s0`{.literal}*` `{.literal}*`/path/to/file`{.literal}* command. For more information, see [Changing file sensitivity in MLS](#changing-file-sensitivity-in-mls "6.7. Changing file sensitivity in MLS").

**Prerequisites**

-   The SELinux policy is set to `mls`{.literal}.

-   SELinux mode is set to `enforcing`{.literal}.

-   The `policycoreutils-python-utils`{.literal} package is installed.

-   The `mlsfilewrite`{.literal} local module is installed in the SELinux MLS policy.

-   You are logged in as a user in MLS which is:

    -   Assigned to a defined security range. This example shows a user with a security range `s0-s2`{.literal}.
    -   Assigned to the same SELinux type defined in the `mlsfilewrite`{.literal} module. This example requires the `(typeattributeset mlsfilewrite (user_t))`{.literal} module.

**Procedure**

1.  Optional: Display the security context of the current user:

    ``` {.language-plaintext tabindex="-1"}
    $ id -Z
    user_u:user_r:user_t:s0-s2
    ```

2.  Change the lower level of the user's MLS clearance range to the level which you want to assign to the file:

    ``` {.language-plaintext tabindex="-1"}
    $ newrole -l s1-s2
    ```

3.  Optional: Display the security context of the current user:

    ``` {.language-plaintext tabindex="-1"}
    $ id -Z
    user_u:user_r:user_t:s1-s2
    ```

4.  Optional: Display the security context of the file:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -Z /path/to/file
    user_u:object_r:user_home_t:s0 /path/to/file
    ```

5.  Change the file's sensitivity level to the lower level of the user's clearance range by modifying the file:

    ``` {.language-plaintext tabindex="-1"}
    $ touch /path/to/file
    ```

    Important

    The classification level reverts to the default value if the `restorecon`{.literal} command is used on the system.

6.  Optional: Exit the shell to return to the user's previous security range:

    ``` {.language-plaintext tabindex="-1"}
    $ exit
    ```

**Verification**

-   Display the security context of the file:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -Z /path/to/file
    user_u:object_r:user_home_t:s1 /path/to/file
    ```

**Additional resources**

-   [Allowing MLS users to edit files on lower levels](#allowing-mls-users-to-edit-files-on-lower-levels "6.10. Allowing MLS users to edit files on lower levels")

### [6.7. Changing file sensitivity in MLS](#changing-file-sensitivity-in-mls) {#changing-file-sensitivity-in-mls .title}

Manually increase a file's MLS classification level as an administrator. This action allows the file to be processed at a higher sensitivity level, helping protect data from lower-clearance users.

In the MLS SELinux policy, users can only modify files at their own sensitivity level. This is intended to prevent any highly sensitive information to be exposed to users at lower clearance levels, and also prevent low-clearance users creating high-sensitivity documents. Administrators, however, can manually increase a file's classification, for example for the file to be processed at the higher level.

**Prerequisites**

-   SELinux policy is set to `mls`{.literal}.

-   SELinux mode is set to enforcing.

-   You have security administration rights, which means that you are assigned to either:

    -   The `secadm_r`{.literal} role.
    -   If the `sysadm_secadm`{.literal} module is enabled, to the `sysadm_r`{.literal} role. The `sysadm_secadm`{.literal} module is enabled by default.

-   The `policycoreutils-python-utils`{.literal} package is installed.

-   A user assigned to any clearance level. For additional information, see [Establishing user clearance levels in MLS](#establishing-user-clearance-in-mls "6.4. Establishing user clearance in MLS") .

    In this example, *`User1`{.literal}* has clearance level `s1`{.literal}.

-   A file with a classification level assigned and to which you have access.

    In this example, *`/path/to/file`{.literal}* has classification level `s1`{.literal}.

**Procedure**

1.  Check the file's classification level:

    ``` {.language-plaintext tabindex="-1"}
    # ls -lZ /path/to/file
    -rw-r-----. 1 User1 User1 user_u:object_r:user_home_t:s1 0 12. Feb 10:43 /path/to/file
    ```

2.  Change the file's default classification level:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -r s2 /path/to/file
    ```

3.  Force the relabeling of the file's SELinux context:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -F -v /path/to/file
    Relabeled /path/to/file from user_u:object_r:user_home_t:s1 to user_u:object_r:user_home_t:s2
    ```

**Verification**

1.  Check the file's classification level:

    ``` {.language-plaintext tabindex="-1"}
    # ls -lZ /path/to/file
    -rw-r-----. 1 User1 User1 user_u:object_r:user_home_t:s2 0 12. Feb 10:53 /path/to/file
    ```

2.  Optional: Verify that the lower-clearance user cannot read the file:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /path/to/file
    cat: file: Permission denied
    ```

**Additional resources**

-   [Establishing user clearance levels in MLS](#establishing-user-clearance-in-mls "6.4. Establishing user clearance in MLS")

### [6.8. Separating system administration from security administration in MLS](#separating-system-administration-from-security-administration-in-mls) {#separating-system-administration-from-security-administration-in-mls .title}

Separate system administration from security administration by disabling the `sysadm_secadm`{.literal} module in MLS. This helps establish stricter control over security authorizations by assigning the `secadm_r`{.literal} role explicitly to a designated security administrator user.

By default, the `sysadm_r`{.literal} role has the rights of the `secadm_r`{.literal} role, which means a user with the `sysadm_r`{.literal} role can manage the security policy.

**Prerequisites**

-   The SELinux policy is set to `mls`{.literal}.

-   The SELinux mode is set to `enforcing`{.literal}.

-   The `policycoreutils-python-utils`{.literal} package is installed.

-   A Linux user that you assign to the `secadm_r`{.literal} role:

    -   The user is assigned to the `staff_u`{.literal} SELinux user
    -   A password for this user has been defined.

    Warning

    Make sure you can log in as the user that you assign to the `secadm`{.literal} role. If not, you can prevent any future modifications of the system's SELinux policy.

**Procedure**

1.  Create a new `sudoers`{.literal} file in the `/etc/sudoers.d`{.literal} directory for the user:

    ``` {.language-plaintext tabindex="-1"}
    # visudo -f /etc/sudoers.d/<sec_adm_user>
    ```

    To keep the `sudoers`{.literal} files organized, replace *`<sec_adm_user>`{.literal}* with the Linux user that you assign to the `secadm`{.literal} role.

2.  Add the following content into the `/etc/sudoers.d/`{.literal}*`<sec_adm_user>`{.literal}* file:

    ``` {.language-plaintext tabindex="-1"}
    <sec_adm_user> ALL=(ALL) TYPE=secadm_t ROLE=secadm_r ALL
    ```

    This line authorizes *`<sec_adm_user>`{.literal}* on all hosts to perform all commands, and maps the user to the `secadm`{.literal} SELinux type and role by default.

3.  Log in as the *\<sec_adm_user\>* user.

    To make sure that the SELinux context (which consists of SELinux user, role, and type) is changed, **log in using `ssh`{.literal}, the console, or `xdm`{.literal}**. Other ways, such as `su`{.literal} and `sudo`{.literal}, cannot change the entire SELinux context.

4.  Verify the user's security context:

    ``` {.language-plaintext tabindex="-1"}
    $ id
    uid=1000(<sec_adm_user>) gid=1000(<sec_adm_user>) groups=1000(<sec_adm_user>) context=staff_u:staff_r:staff_t:s0-s15:c0.c1023
    ```

5.  Run the interactive shell for the root user:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo -i
    [sudo] password for <sec_adm_user>:
    ```

6.  Verify the current user's security context:

    ``` {.language-plaintext tabindex="-1"}
    # id
    uid=0(root) gid=0(root) groups=0(root) context=staff_u:secadm_r:secadm_t:s0-s15:c0.c1023
    ```

7.  Disable the `sysadm_secadm`{.literal} module from the policy:

    ``` {.language-plaintext tabindex="-1"}
    # semodule -d sysadm_secadm
    ```

    Important

    Use the `semodule -d`{.literal} command instead of removing the system policy module by using the `semodule -r`{.literal} command. The `semodule -r`{.literal} command deletes the module from your system's storage, which means it cannot be loaded again without reinstalling the `selinux-policy-mls`{.literal} package.

**Verification**

1.  As the user assigned to the `secadm`{.literal} role, and in the interactive shell for the root user, verify that you can access the security policy data:

    ``` {.language-plaintext tabindex="-1"}
    # seinfo -xt secadm_t

    Types: 1
       type secadm_t, can_relabelto_shadow_passwords, (…) userdomain;
    ```

2.  Log out from the root shell:

    ``` {.language-plaintext tabindex="-1"}
    # logout
    ```

3.  Log out from the *`<sec_adm_user>`{.literal}* user:

    ``` {.language-plaintext tabindex="-1"}
    $ logout
    Connection to localhost closed.
    ```

4.  Display the current security context:

    ``` {.language-plaintext tabindex="-1"}
    # id
    uid=0(root) gid=0(root) groups=0(root) context=root:sysadm_r:sysadm_t:s0-s15:c0.c1023
    ```

5.  Attempt to enable the `sysadm_secadm`{.literal} module. The command should fail:

    ``` {.language-plaintext tabindex="-1"}
    # semodule -e sysadm_secadm
    SELinux:  Could not load policy file /etc/selinux/mls/policy/policy.31:  Permission denied
    /sbin/load_policy:  Can't load policy:  Permission denied
    libsemanage.semanage_reload_policy: load_policy returned error code 2. (No such file or directory).
    SELinux:  Could not load policy file /etc/selinux/mls/policy/policy.31:  Permission denied
    /sbin/load_policy:  Can't load policy:  Permission denied
    libsemanage.semanage_reload_policy: load_policy returned error code 2. (No such file or directory).
    semodule:  Failed!
    ```

6.  Attempt to display the details about the `sysadm_t`{.literal} SELinux type. The command should fail:

    ``` {.language-plaintext tabindex="-1"}
    # seinfo -xt sysadm_t
    [Errno 13] Permission denied: '/sys/fs/selinux/policy'
    ```

### [6.9. Defining a secure terminal in MLS](#defining-a-secure-terminal-in-mls) {#defining-a-secure-terminal-in-mls .title}

Allow logins from specific terminals considered insecure under the MLS policy by adding their types to the `/etc/selinux/mls/contexts/securetty_types`{.literal} file. This is necessary when MLS prevents users from logging in through common terminal types.

The SELinux policy checks the type of the terminal from which a user is connected, and allows running of certain SELinux applications, for example `newrole`{.literal}, only from secure terminals. Attempting this from an insecure terminal produces an error: `Error: you are not allowed to change levels on a non secure terminal;`{.literal}.

The `/etc/selinux/mls/contexts/securetty_types`{.literal} file defines secure terminals for the Multi-Level Security (MLS) policy.

Default contents of the file:

``` {.language-plaintext tabindex="-1"}
console_device_t
sysadm_tty_device_t
user_tty_device_t
staff_tty_device_t
auditadm_tty_device_t
secureadm_tty_device_t
```

Warning

Adding terminal types to the list of secure terminals can expose your system to security risks.

**Prerequisites**

-   SELinux policy is set to `mls`{.literal}.

-   You are connected from an already secure terminal, or SELinux is in permissive mode.

-   You have security administration rights, which means that you are assigned to either:

    -   The `secadm_r`{.literal} role.
    -   If the `sysadm_secadm`{.literal} module is enabled, to the `sysadm_r`{.literal} role. The `sysadm_secadm`{.literal} module is enabled by default.

-   The `policycoreutils-python-utils`{.literal} package is installed.

**Procedure**

1.  Determine the current terminal type:

    ``` {.language-plaintext tabindex="-1"}
    # ls -Z `tty`
    root:object_r:user_devpts_t:s0 /dev/pts/0
    ```

    In this example output, `user_devpts_t`{.literal} is the current terminal type.

2.  Add the relevant SELinux type on a new line in the `/etc/selinux/mls/contexts/securetty_types`{.literal} file.

3.  Optional: Switch SELinux to enforcing mode:

    ``` {.language-plaintext tabindex="-1"}
    # setenforce 1
    ```

**Verification**

-   Log in from the previously insecure terminal you have added to the `/etc/selinux/mls/contexts/securetty_types`{.literal} file.

### [6.10. Allowing MLS users to edit files on lower levels](#allowing-mls-users-to-edit-files-on-lower-levels) {#allowing-mls-users-to-edit-files-on-lower-levels .title}

By default, MLS users cannot write to files with a sensitivity level below the lower limit of the clearance range. If you want to allow users to edit files on lower levels, you can do so by creating a local SELinux module.

When MLS users write to files on lower levels, the file's sensitivity level increases to the lower value of the user's current range.

**Prerequisites**

-   The SELinux policy is set to `mls`{.literal}.
-   The SELinux mode is set to `enforcing`{.literal}.
-   The `policycoreutils-python-utils`{.literal} package is installed.
-   The `setools-console`{.literal} and `audit`{.literal} packages for verification.

**Procedure**

1.  Optional: Switch to permissive mode for easier troubleshooting.

    ``` {.language-plaintext tabindex="-1"}
    # setenforce 0
    ```

2.  Open a new `.cil`{.literal} file with a text editor, for example `~/local_mlsfilewrite.cil`{.literal}, and insert the following custom rule:

    ``` {.language-plaintext tabindex="-1"}
    (typeattributeset mlsfilewrite (_staff_t_))
    ```

    You can replace *`staff_t`{.literal}* with a different SELinux type. By specifying SELinux type here, you can control which SELinux roles can edit lower-level files.

    To keep your local modules better organized, use the `local_`{.literal} prefix in the names of local SELinux policy modules.

3.  Install the policy module:

    ``` {.language-plaintext tabindex="-1"}
    # semodule -i ~/local_mlsfilewrite.cil
    ```

    Note

    To remove the local policy module, use `semodule -r ~/`{.literal}*`local_mlsfilewrite`{.literal}*. Note that you must refer to the module name without the `.cil`{.literal} suffix.

4.  Optional: If you previously switched back to permissive mode, return to enforcing mode:

    ``` {.language-plaintext tabindex="-1"}
    # setenforce 1
    ```

**Verification**

1.  Find the local module in the list of installed SELinux modules:

    ``` {.language-plaintext tabindex="-1"}
    # semodule -lfull | grep "local_mls"
    400 local_mlsfilewrite  cil
    ```

    Because local modules have priority `400`{.literal}, you can list them also by using the `semodule -lfull | grep -v ^100`{.literal} command.

2.  Log in as a user assigned to the type defined in the custom rule, for example, *`staff_t`{.literal}*.

3.  Attempt to write to a file with a lower sensitivity level. This increases the file's classification level to the user's clearance level.

    Important

    The files you use for verification should not contain any sensitive information in case the configuration is incorrect and the user actually can access the files without authorization.

## [Chapter 7. Using Multi-Category Security (MCS) for data confidentiality](#using-multi-category-security-mcs-for-data-confidentiality) {#chapter-7.-using-multi-category-security-mcs-for-data-confidentiality .title}

You can use MCS to enhance the data confidentiality of your system by categorizing data, and then granting certain processes and users access to specific categories.

### [7.1. Multi-Category Security (MCS)](#multi-category-security-mcs) {#multi-category-security-mcs .title}

Use Multi-Category Security (MCS) to limit access based on category labels, such as project or department names. MCS ensures separation and privacy between different work areas.

Multi-Category Security (MCS) is an access control mechanism that uses categories assigned to processes and files. Files can be accessed only by processes assigned to the same categories. MCS maintains data confidentiality on your system.

MCS categories use values `c0`{.literal} to `c1023`{.literal}. You can also define a text label for each category or combination, such as \"Personnel\", \"ProjectX\", or \"ProjectX.Personnel\". The MCS Translation service (`mcstrans`{.literal}) replaces the category values with labels in system inputs and outputs. Users can then use these labels instead of the category values.

When users are assigned to categories, they can label any of their files with any of the categories to which they have been assigned.

MCS works on a simple principle: to access a file, a user must be assigned to all categories assigned to that file. The MCS check applies after normal Linux Discretionary Access Control (DAC) and SELinux Type Enforcement (TE) rules. Therefore, MCS can only further restrict existing security configuration.

#### [7.1.1. MCS within Multi-Level Security (MLS)](#mcs_within_multi_level_security_mls) {#mcs-within-multi-level-security-mls .title}

You can use MCS on its own as a non-hierarchical system. You can also use it with Multi-Level Security (MLS) as a non-hierarchical layer within a hierarchical system.

An example of MCS within MLS could be a secretive research organization, where files are classified as shown in the following table:

+:-------------------+:--------------:+:-----------------:+:-----------------:+:-----------------:+
| **Security level** | **Category**   |                   |                   |                   |
+--------------------+----------------+-------------------+-------------------+-------------------+
|                    | Not specified  | Project X         | Project Y         | Project Z         |
+--------------------+----------------+-------------------+-------------------+-------------------+
| Unclassified       | `s0`{.literal} | `s0:c0`{.literal} | `s0:c1`{.literal} | `s0:c2`{.literal} |
+--------------------+----------------+-------------------+-------------------+-------------------+
| Confidential       | `s1`{.literal} | `s1:c0`{.literal} | `s1:c1`{.literal} | `s1:c2`{.literal} |
+--------------------+----------------+-------------------+-------------------+-------------------+
| Secret             | `s2`{.literal} | `s2:c0`{.literal} | `s2:c1`{.literal} | `s2:c2`{.literal} |
+--------------------+----------------+-------------------+-------------------+-------------------+
| Top secret         | `s3`{.literal} | `s3:c0`{.literal} | `s3:c1`{.literal} | `s3:c2`{.literal} |
+--------------------+----------------+-------------------+-------------------+-------------------+

: Table 7.1. Example of combinations of security levels and categories

Show more

Note

A user with a range `s0:c0.1023`{.literal} can access all files assigned to all categories on level `s0`{.literal}. Other security mechanisms, such as DAC or type enforcement policy rules, might still prohibit access.

The resulting security context of a file or process is a combination of:

-   SELinux user
-   SELinux role
-   SELinux type
-   MLS sensitivity level
-   MCS category

For example, a non-privileged user with access to sensitivity level 1 and category 2 in an MLS/MCS environment could have the following SELinux context:

``` {.language-plaintext tabindex="-1"}
user_u:user_r:user_t:s1:c2
```

**Additional resources**

-   [Using Multi-Level Security (MLS)](#using-multi-level-security-mls "Chapter 6. Using Multi-Level Security (MLS)")

### [7.2. Configuring Multi-Category Security for data confidentiality](#configuring-multi-category-security-for-data-confidentiality) {#configuring-multi-category-security-for-data-confidentiality .title}

Configure Multi-Category Security (MCS) for users to help ensure data confidentiality in targeted and MLS policies. This involves creating a local SELinux module that constrains the user domain by MCS rules.

By default, Multi-Category Security (MCS) is active in the `targeted`{.literal} and `mls`{.literal} SELinux policies but is not configured for users. In the `targeted`{.literal} policy, MCS is configured only for:

-   OpenShift
-   virt
-   sandbox
-   network labeling
-   containers (`container-selinux`{.literal})

You can configure MCS to categorize users by creating a local SELinux module with a rule that constrains the `user_t`{.literal} SELinux type by MCS rules in addition to type enforcement.

Warning

Changing the categories of certain files might render some services non-operational. If you are not an expert, contact your Red Hat sales representative and request consulting services.

**Prerequisites**

-   SELinux mode is set to \`enforcing.
-   The SELinux policy is set to `targeted`{.literal} or `mls`{.literal}.
-   The `policycoreutils-python-utils`{.literal} and `setools-console`{.literal} packages are installed.

**Procedure**

1.  Create a new file named, for example, `local_mcs_user.cil`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # touch local_mcs_user.cil
    ```

2.  In a text editor, insert the following rule:

    ``` {.language-plaintext tabindex="-1"}
    (typeattributeset mcs_constrained_type (user_t))
    ```

3.  Install the policy module:

    ``` {.language-plaintext tabindex="-1"}
    # semodule -i local_mcs_user.cil
    ```

**Verification**

-   For each user domain, display additional details for all the components:

    ``` {.language-plaintext tabindex="-1"}
    # seinfo -xt user_t

    Types: 1
    type user_t, application_domain_type, nsswitch_domain, corenet_unlabeled_type, domain, kernel_system_state_reader, mcs_constrained_type, netlabel_peer_type, privfd, process_user_target, scsi_generic_read, scsi_generic_write, syslog_client_type, pcmcia_typeattr_1, user_usertype, login_userdomain, userdomain, unpriv_userdomain, userdom_home_reader_type, userdom_filetrans_type, xdmhomewriter, x_userdomain, x_domain, dridomain, xdrawable_type, xcolormap_type;
    ```

**Next step**

-   For more information about MCS in the context of containers, see the blog posts [How SELinux separates containers using Multi-Level Security](https://www.redhat.com/en/blog/how-selinux-separates-containers-using-multi-level-security) and [Why you should be using Multi-Category Security for your Linux containers](https://www.redhat.com/en/blog/why-you-should-be-using-multi-category-security-your-linux-containers).

**Additional resources**

-   [Creating a local SELinux policy module](#creating-a-local-selinux-policy-module "5.4. Creating a local SELinux policy module")

### [7.3. Defining category labels in MCS](#defining-category-labels-in-mcs) {#defining-category-labels-in-mcs .title}

Define human-readable labels for MCS categories or MLS level combinations by editing the `setrans.conf`{.literal} file. Defining these labels makes it easier for users to manage and use categories, although MCS functionality remains the same regardless.

By editing `setrans.conf`{.literal}, you can manage and maintain labels for MCS categories, or combinations of MCS categories with MLS levels. In this file, SELinux maintains a mapping between internal sensitivity and category levels and their human-readable labels. See the `setrans.conf(5)`{.literal} man page on your system.

Note

Category labels only make it easier for users to use the categories. MCS works the same whether you define labels or not.

**Prerequisites**

-   The SELinux mode is set to `enforcing`{.literal}.
-   The SELinux policy is set to `targeted`{.literal} or `mls`{.literal}.
-   The `policycoreutils-python-utils`{.literal} and `mcstrans`{.literal} packages are installed.

**Procedure**

1.  Modify existing categories or create new categories by editing the `/etc/selinux/`{.literal}*`<selinux_policy>`{.literal}*`/setrans.conf`{.literal} file in a text editor. Replace *`<selinux_policy>`{.literal}* with `targeted`{.literal} or `mls`{.literal} depending on the SELinux policy you use. For example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/selinux/targeted/setrans.conf
    ```

2.  In the `setrans.conf`{.literal} file for your policy, define the combinations of categories required by your scenario using the syntax `s_<security_level>_:c_<category_number>_=`{.literal}*`<category_name>`{.literal}*, for example:

    ``` {.language-plaintext tabindex="-1"}
    s0:c0=Marketing
    s0:c1=Finance
    s0:c2=Payroll
    s0:c3=Personnel
    ```

    -   You can use category numbers from `c0`{.literal} to `c1023`{.literal}.
    -   In the `targeted`{.literal} policy, use the `s0`{.literal} security level.
    -   In the `mls`{.literal} policy, you can label each combination of sensitivity levels and categories.

3.  Optional: In the `setrans.conf`{.literal} file, you can also label the MLS sensitivity levels.

4.  Save and exit the file.

5.  To make the changes effective, restart the MCS translation service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart mcstrans
    ```

**Verification**

-   Display the current categories:

    ``` {.language-plaintext tabindex="-1"}
    # chcat -L
    ```

    The previous example produces the following output:

    ``` {.language-plaintext tabindex="-1"}
    s0:c0                          Marketing
    s0:c1                          Finance
    s0:c2                          Payroll
    s0:c3                          Personnel
    s0
    s0-s0:c0.c1023                 SystemLow-SystemHigh
    s0:c0.c1023                    SystemHigh
    ```

### [7.4. Assigning categories to users in MCS](#assigning-categories-to-users-in-mcs) {#assigning-categories-to-users-in-mcs .title}

You can define user authorizations by assigning categories to Linux users. A user with assigned categories can access and modify files that have a subset of the user's categories. Users can also assign files they own to categories they have been assigned to.

A Linux user cannot be assigned to a category that is outside of the security range defined for the relevant SELinux user.

Note

Category access is assigned during login. Consequently, users do not have access to newly assigned categories until they log in again. Similarly, if you revoke a user's access to a category, this is effective only after the user logs in again.

**Prerequisites**

-   The SELinux mode is set to `enforcing`{.literal}.

-   The SELinux policy is set to `targeted`{.literal} or `mls`{.literal}.

-   The `policycoreutils-python-utils`{.literal} package is installed.

-   Linux users are assigned to SELinux confined users:

    -   Non-privileged users are assigned to `user_u`{.literal}.
    -   Privileged users are assigned to `staff_u`{.literal}.

**Procedure**

1.  Define the security range for the SELinux user.

    ``` {.language-plaintext tabindex="-1"}
    # semanage user -m -rs0:c0,c1-s0:c0.c9 <user_u>
    ```

    Use category numbers `c0`{.literal} to `c1023`{.literal} or category labels as defined in the `setrans.conf`{.literal} file. For additional information, see [Defining category labels in MCS](#defining-category-labels-in-mcs "7.3. Defining category labels in MCS") .

2.  Assign MCS categories to a Linux user. You can specify only a range within the range defined to the relevant SELinux user:

    ``` {.language-plaintext tabindex="-1"}
    # semanage login -m -rs0:c1 <Linux.user1>
    ```

    You can add or remove categories from Linux users by using the `chcat`{.literal} command. The following example adds *`<category1>`{.literal}* and removes *`<category2>`{.literal}* from *`<Linux.user1>`{.literal}* and *`<Linux.user2>`{.literal}*:

    ``` {.language-plaintext tabindex="-1"}
    # chcat -l -- +<category1>,-<category2> <Linux.user1>,<Linux.user2>
    ```

    You must specify `--`{.literal} on the command line before using the `-`{.literal}*`<category>`{.literal}* syntax. Otherwise, the `chcat`{.literal} command misinterprets the category removal as a command option. See the `chcat(8)`{.literal} man page on your system for more information.

**Verification**

-   List the categories assigned to Linux users:

    ``` {.language-plaintext tabindex="-1"}
    # chcat -L -l <Linux.user1>,<Linux.user2>
    <Linux.user1>: <category1>,<category2>
    <Linux.user2>: <category1>,<category2>
    ```

### [7.5. Assigning categories to files in MCS](#assigning-categories-to-files-in-mcs) {#assigning-categories-to-files-in-mcs .title}

Assign Multi-Category Security (MCS) categories to files to limit access to users in those categories. This improves privacy by limiting data access across different work groups.

You must have admin rights to assign MCS categories to users. Users can then assign categories to files. To change file categories, users must have access to that file. Users can only assign a file to a category they have.

Note

The system uses both category rules and normal file access rights. For example, if a user with category `bigfoot`{.literal} uses DAC to block access to a file, other `bigfoot`{.literal} users cannot access that file. Even a user with all categories might not access all files.

**Prerequisites**

-   The SELinux mode is set to `enforcing`{.literal}.

-   The SELinux policy is set to `targeted`{.literal} or `mls`{.literal}.

-   The `policycoreutils-python-utils`{.literal} package is installed on your system.

-   Access to a Linux user that is:

    -   Assigned to an SELinux user.
    -   Assigned to the category you want to give the file. For more details, see [Assigning categories to users in MCS](#assigning-categories-to-users-in-mcs "7.4. Assigning categories to users in MCS").

-   Access to the file you want to add to the category.

-   For testing: Access to a Linux user not assigned to this category

**Procedure**

-   Add categories to a file:

    ``` {.language-plaintext tabindex="-1"}
    $ chcat -- +<category1>,+<category2> <path/to/file1>
    ```

    Use category numbers `c0`{.literal} to `c1023`{.literal} or category labels from the `setrans.conf`{.literal} file. For more details, see [Defining category labels in MCS](#defining-category-labels-in-mcs "7.3. Defining category labels in MCS").

    You can remove categories from a file by using the same syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ chcat -- -<category1>,-<category2> <path/to/file1>
    ```

    Note

    When removing a category, you must type `--`{.literal} on the command line before using `-`{.literal}*`<category>`{.literal}*. If you skip this, the `chcat`{.literal} command reads the category as a command flag instead.

**Verification**

1.  Check the security context of the file to verify it has the correct categories:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -lZ <path/to/file>
    -rw-r--r--  <LinuxUser1> <Group1> root:object_r:user_home_t:_<sensitivity>_:_<category>_ <path/to/file>
    ```

    The actual security context of the file might differ.

2.  Optional: Try to access the file when logged in as a Linux user not in the same category as the file:

    ``` {.language-plaintext tabindex="-1"}
    $ cat <path/to/file>
    cat: <path/to/file>: Permission Denied
    ```

## [Chapter 8. Writing a custom SELinux policy](#writing-a-custom-selinux-policy) {#chapter-8.-writing-a-custom-selinux-policy .title}

Write and use a custom SELinux policy to confine your applications and increase the security of your host system. The custom policy defines precise access rules tailored to your application requirements.

### [8.1. Custom SELinux policies and related tools](#custom-selinux-policies-and-related-tools) {#custom-selinux-policies-and-related-tools .title}

A custom SELinux security policy contains rules that govern interactions between processes and system resources. The kernel enforces this policy by denying all access requests not explicitly allowed by the defined rules.

An SELinux security policy is a collection of SELinux rules. A policy is a core component of SELinux and is loaded into the kernel by SELinux user-space tools. The kernel enforces the use of an SELinux policy to evaluate access requests on the system. By default, SELinux denies all requests except those that match the rules specified in the loaded policy.

Each SELinux policy rule describes an interaction between a process and a system resource:

``` {.language-plaintext tabindex="-1"}
ALLOW apache_process apache_log:FILE READ;
```

You can read this example rule as: *The **Apache** process can **read** its **logging file**.* In this rule, `apache_process`{.literal} and `apache_log`{.literal} are **labels**. An SELinux security policy assigns labels to processes and defines relations to system resources. This way, a policy maps operating-system entities to the SELinux layer.

SELinux labels are stored as extended attributes of file systems, such as `ext2`{.literal}. You can list them using the `getfattr`{.literal} utility or a `ls -Z`{.literal} command, for example:

``` {.language-plaintext tabindex="-1"}
$ ls -Z /etc/passwd
system_u:object_r:passwd_file_t:s0 /etc/passwd
```

Where `system_u`{.literal} is an SELinux user, `object_r`{.literal} is an example of the SELinux role, and `passwd_file_t`{.literal} is an SELinux domain.

The default SELinux policy provided by the `selinux-policy`{.literal} packages contains rules for applications and daemons that are parts of Red Hat Enterprise Linux and are provided by packages in its repositories. Applications not described in this distribution policy are not confined by SELinux. To change this, you have to modify the policy by using a policy module, which contains additional definitions and rules.

In Red Hat Enterprise Linux, you can query the installed SELinux policy and generate new policy modules by using the `sepolicy`{.literal} tool. Scripts that `sepolicy`{.literal} generates together with the policy modules always contain a command by using the `restorecon`{.literal} utility. This utility is a basic tool for fixing labeling problems in a selected part of a file system.

See the `sepolicy(8)`{.literal} and `getfattr(1)`{.literal} man pages on your system for more information.

**Additional resources**

-   [Quick start to write a custom SELinux policy (Red Hat Knowledgebase)](https://access.redhat.com/articles/6999267)

### [8.2. Creating and enforcing an SELinux policy for a custom application](#creating-and-enforcing-an-selinux-policy-for-a-custom-application) {#creating-and-enforcing-an-selinux-policy-for-a-custom-application .title}

You can create and enforce a tailored SELinux policy to confine custom applications and increase the security of host systems and users\' data.

Because each application has specific requirements, modify this example procedure for creating an SELinux policy that confines a simple daemon according to your use case. See the `sepolgen(8)`{.literal}, `ausearch(8)`{.literal}, `audit2allow(1)`{.literal}, `audit2why(1)`{.literal}, `sealert(8)`{.literal}, and `restorecon(8)`{.literal} man pages on your system for details about commands used in the procedure.

**Prerequisites**

-   The `selinux-policy-devel`{.literal} package and its dependencies are installed on your system.

**Procedure**

1.  For this example procedure, prepare a simple daemon that opens the `/var/log/messages`{.literal} file for writing:

    a.  Create a new file, and open it in a text editor of your choice, for example:

        ``` {.language-plaintext tabindex="-1"}
        $ vi mydaemon.c
        ```

    b.  Insert the following code:

        ``` {.language-plaintext tabindex="-1"}
        #include <unistd.h>
        #include <stdio.h>

        FILE *f;

        int main(void)
        {
        while(1) {
        f = fopen("/var/log/messages","w");
                sleep(5);
                fclose(f);
            }
        }
        ```

    c.  Compile the file:

        ``` {.language-plaintext tabindex="-1"}
        $ gcc -o mydaemon mydaemon.c
        ```

    d.  Create a `systemd`{.literal} unit file for your daemon:

        ``` {.language-plaintext tabindex="-1"}
        $ vi mydaemon.service
        [Unit]
        Description=Simple testing daemon

        [Service]
        Type=simple
        ExecStart=/usr/local/bin/mydaemon

        [Install]
        WantedBy=multi-user.target
        ```

    e.  Install and start the daemon:

        ``` {.language-plaintext tabindex="-1"}
        # cp mydaemon /usr/local/bin/
        # cp mydaemon.service /usr/lib/systemd/system
        # systemctl start mydaemon
        # systemctl status mydaemon
        ● mydaemon.service - Simple testing daemon
           Loaded: loaded (/usr/lib/systemd/system/mydaemon.service; disabled; vendor preset: disabled)
           Active: active (running) since Sat 2020-05-23 16:56:01 CEST; 19s ago
         Main PID: 4117 (mydaemon)
            Tasks: 1
           Memory: 148.0K
           CGroup: /system.slice/mydaemon.service
                   └─4117 /usr/local/bin/mydaemon

        May 23 16:56:01 localhost.localdomain systemd[1]: Started Simple testing daemon.
        ```

    f.  Check that the new daemon is not confined by SELinux:

        ``` {.language-plaintext tabindex="-1"}
        $ ps -efZ | grep mydaemon
        system_u:system_r:unconfined_service_t:s0 root 4117    1  0 16:56 ?        00:00:00 /usr/local/bin/mydaemon
        ```

2.  Generate a custom policy for the daemon:

    ``` {.language-plaintext tabindex="-1"}
    $ sepolicy generate --init /usr/local/bin/mydaemon
    Created the following files:
    /home/example.user/mysepol/mydaemon.te # Type Enforcement file
    /home/example.user/mysepol/mydaemon.if # Interface file
    /home/example.user/mysepol/mydaemon.fc # File Contexts file
    /home/example.user/mysepol/mydaemon_selinux.spec # Spec file
    /home/example.user/mysepol/mydaemon.sh # Setup Script
    ```

3.  Rebuild the system policy with the new policy module using the configuration script created by the previous command:

    ``` {.language-plaintext tabindex="-1"}
    # ./mydaemon.sh
    Building and Loading Policy
    + make -f /usr/share/selinux/devel/Makefile mydaemon.pp
    Compiling targeted mydaemon module
    Creating targeted mydaemon.pp policy package
    rm tmp/mydaemon.mod.fc tmp/mydaemon.mod
    + /usr/sbin/semodule -i mydaemon.pp
    ...
    ```

    Note that the configuration script relabels the corresponding part of the file system by using the `restorecon`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    restorecon -v /usr/local/bin/mydaemon /usr/lib/systemd/system
    ```

4.  Restart the daemon, and check that it now runs confined by SELinux:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart mydaemon
    $ ps -efZ | grep mydaemon
    system_u:system_r:mydaemon_t:s0 root        8150       1  0 17:18 ?        00:00:00 /usr/local/bin/mydaemon
    ```

5.  Because the daemon is now confined by SELinux, SELinux also prevents it from accessing `/var/log/messages`{.literal}. Display the corresponding denial message:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -m AVC -ts recent
    ...
    type=AVC msg=audit(1590247112.719:5935): avc:  denied  { open } for  pid=8150 comm="mydaemon" path="/var/log/messages" dev="dm-0" ino=2430831 scontext=system_u:system_r:mydaemon_t:s0 tcontext=unconfined_u:object_r:var_log_t:s0 tclass=file permissive=1
    ...
    ```

6.  You can get additional information also using the `sealert`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    $ sealert -l "*"
    SELinux is preventing mydaemon from open access on the file /var/log/messages.

    *****  Plugin catchall (100. confidence) suggests   **************************

    If you believe that mydaemon should be allowed open access on the messages file by default.
    Then you should report this as a bug.
    You can generate a local policy module to allow this access.
    Do allow this access for now by executing:
    # ausearch -c 'mydaemon' --raw | audit2allow -M my-mydaemon
    # semodule -X 300 -i my-mydaemon.pp

    Additional Information:
    Source Context                system_u:system_r:mydaemon_t:s0
    Target Context                unconfined_u:object_r:var_log_t:s0
    Target Objects                /var/log/messages [ file ]
    Source                        mydaemon
    …
    ```

7.  Use the `audit2allow`{.literal} tool to suggest changes:

    ``` {.language-plaintext tabindex="-1"}
    $ ausearch -m AVC -ts recent | audit2allow -R

    require {
        type mydaemon_t;
    }

    #============= mydaemon_t ==============
    logging_write_generic_logs(mydaemon_t)
    ```

8.  Because rules suggested by `audit2allow`{.literal} can be incorrect for certain cases, use only a part of its output to find the corresponding policy interface. Inspect the `logging_write_generic_logs(mydaemon_t)`{.literal} macro with the `macro-expander`{.literal} tool, to see all allow rules the macro provides:

    ``` {.language-plaintext tabindex="-1"}
    $ macro-expander "logging_write_generic_logs(mydaemon_t)"
    allow mydaemon_t var_t:dir { getattr search open };
    allow mydaemon_t var_log_t:dir { getattr search open read lock ioctl };
    allow mydaemon_t var_log_t:dir { getattr search open };
    allow mydaemon_t var_log_t:file { open { getattr write append lock ioctl } };
    allow mydaemon_t var_log_t:dir { getattr search open };
    allow mydaemon_t var_log_t:lnk_file { getattr read };
    ```

9.  In this case, you can use the suggested interface, because it only provides read and write access to log files and their parent directories. Add the corresponding rule to your type enforcement file:

    ``` {.language-plaintext tabindex="-1"}
    $ echo "logging_write_generic_logs(mydaemon_t)" >> mydaemon.te
    ```

    Alternatively, you can add this rule instead of using the interface:

    ``` {.language-plaintext tabindex="-1"}
    $ echo "allow mydaemon_t var_log_t:file { open write getattr };" >> mydaemon.te
    ```

10. Reinstall the policy:

    ``` {.language-plaintext tabindex="-1"}
    # ./mydaemon.sh
    Building and Loading Policy
    + make -f /usr/share/selinux/devel/Makefile mydaemon.pp
    Compiling targeted mydaemon module
    Creating targeted mydaemon.pp policy package
    rm tmp/mydaemon.mod.fc tmp/mydaemon.mod
    + /usr/sbin/semodule -i mydaemon.pp
    ...
    ```

**Verification**

1.  Check that your application runs confined by SELinux, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ ps -efZ | grep mydaemon
    system_u:system_r:mydaemon_t:s0 root        8150       1  0 17:18 ?        00:00:00 /usr/local/bin/mydaemon
    ```

2.  Verify that your custom application does not cause any SELinux denials:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -m AVC -ts recent
    <no matches>
    ```

**Additional resources**

-   [Quick start to write a custom SELinux policy (Red Hat Knowledgebase)](https://access.redhat.com/articles/6999267)

### [8.3. Additional resources](#writing-a-custom-selinux-policy_83-additional-resources) {#additional-resources-2 .title}

-   [SELinux Policy Workshop (Red Hat \| Public Sector)](http://redhatgov.io/workshops/selinux_policy/)

## [Chapter 9. Creating SELinux policies for containers](#creating-selinux-policies-for-containers) {#chapter-9.-creating-selinux-policies-for-containers .title}

Use the Udica tool to create SELinux policies for containers. These policies improve container security. They control how containers access host resources, such as storage and network devices.

With Udica, you can protect your containers from security violations and meet compliance requirements.

### [9.1. Introduction to the udica SELinux policy generator](#introduction-to-the-udica-selinux-policy-generator) {#introduction-to-the-udica-selinux-policy-generator .title}

You can use Udica to create new SELinux policies for custom containers. You can use this tool to create a policy based on an inspection of the container JSON file, which contains Linux-capabilities, mount-points, and ports definitions.

The tool consequently combines rules generated from inspection results with rules inherited from a specified SELinux Common Intermediate Language (CIL) block.

The process of generating SELinux policy for a container by using Udica has three main parts:

1.  Parsing the container spec file in JSON format
2.  Finding suitable allow rules based on the results of the first part
3.  Generating final SELinux policy

During the parsing phase, Udica looks for Linux capabilities, network ports, and mount points.

Based on the results, Udica detects which Linux capabilities are required by the container and creates an SELinux rule allowing all these capabilities. If the container binds to a specific port, udica uses SELinux user-space libraries to get the correct SELinux label of a port that is used by the inspected container.

Afterward, Udica detects which directories are mounted to the container file-system namespace from the host.

The CIL block inheritance feature enables Udica to create templates of SELinux *allow rules* focusing on a specific action, for example:

-   *allow accessing home directories*
-   *allow accessing log files*
-   *allow accessing communication with X server*.

These templates are called blocks, and the final SELinux policy is created by merging the blocks.

**Additional resources**

-   [Generate SELinux policies for containers with Udica (Red Hat Blog)](https://www.redhat.com/en/blog/generate-selinux-policies-containers-with-udica)

### [9.2. Creating and using an SELinux policy for a custom container](#creating-and-using-an-selinux-policy-for-a-custom-container) {#creating-and-using-an-selinux-policy-for-a-custom-container .title}

Create and use an SELinux policy module generated by Udica to confine the container's access to the host system. This policy limits the container to only the necessary resources, minimizing the potential impact of a container compromise.

**Prerequisites**

-   The `podman`{.literal} tool for managing containers is installed. If it is not, use the `dnf install podman`{.literal} command.
-   A custom Linux container - *ubi8* in this example.

**Procedure**

1.  Install the `udica`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install -y udica
    ```

    Alternatively, install the `container-tools`{.literal} module, which provides a set of container software packages, including `udica`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # dnf module install -y container-tools
    ```

2.  Start the *ubi8* container that mounts the `/home`{.literal} directory with read-only permissions and the `/var/spool`{.literal} directory with permissions to read and write. The container exposes the port *21*.

    ``` {.language-plaintext tabindex="-1"}
    # podman run --env container=podman -v /home:/home:ro -v /var/spool:/var/spool:rw -p 21:21 -it ubi8 bash
    ```

    Note that now the container runs with the `container_t`{.literal} SELinux type. This type is a generic domain for all containers in the SELinux policy and it might be either too strict or too loose for your scenario.

3.  Open a new session, and enter the `podman ps`{.literal} command to obtain the ID of the container:

    ``` {.language-plaintext tabindex="-1"}
    # podman ps
    CONTAINER ID   IMAGE                                   COMMAND   CREATED          STATUS              PORTS   NAMES
    37a3635afb8f   registry.access.redhat.com/ubi8:latest  bash      15 minutes ago   Up 15 minutes ago           heuristic_lewin
    ```

4.  Create a container JSON file, and use the `udica`{.literal} command for creating a policy module based on the information in the JSON file:

    ``` {.language-plaintext tabindex="-1"}
    # podman inspect 37a3635afb8f > container.json
    # udica -j container.json my_container
    Policy my_container with container id 37a3635afb8f created!
    …
    ```

    Alternatively:

    ``` {.language-plaintext tabindex="-1"}
    # podman inspect 37a3635afb8f | udica my_container
    Policy my_container with container id 37a3635afb8f created!

    Please load these modules using:
    # semodule -i my_container.cil /usr/share/udica/templates/{base_container.cil,net_container.cil,home_container.cil}

    Restart the container with: "--security-opt label=type:my_container.process" parameter
    ```

5.  As suggested by the output of `udica`{.literal} in the previous step, load the policy module:

    ``` {.language-plaintext tabindex="-1"}
    # semodule -i my_container.cil /usr/share/udica/templates/{base_container.cil,net_container.cil,home_container.cil}
    ```

6.  Stop the container and start it again with the `--security-opt label=type:my_container.process`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # podman stop 37a3635afb8f
    # podman run --security-opt label=type:my_container.process -v /home:/home:ro -v /var/spool:/var/spool:rw -p 21:21 -it ubi8 bash
    ```

**Verification**

1.  Check that the container runs with the `my_container.process`{.literal} type:

    ``` {.language-plaintext tabindex="-1"}
    # ps -efZ | grep my_container.process
    unconfined_u:system_r:container_runtime_t:s0-s0:c0.c1023 root 2275 434  1 13:49 pts/1 00:00:00 podman run --security-opt label=type:my_container.process -v /home:/home:ro -v /var/spool:/var/spool:rw -p 21:21 -it ubi8 bash
    system_u:system_r:my_container.process:s0:c270,c963 root 2317 2305  0 13:49 pts/0 00:00:00 bash
    ```

2.  Verify that SELinux now allows access the `/home`{.literal} and `/var/spool`{.literal} mount points:

    ``` {.language-plaintext tabindex="-1"}
    [root@37a3635afb8f /]# cd /home
    [root@37a3635afb8f home]# ls
    username
    [root@37a3635afb8f ~]# cd /var/spool/
    [root@37a3635afb8f spool]# touch test
    [root@37a3635afb8f spool]#
    ```

3.  Check that SELinux allows binding only to the port 21:

    ``` {.language-plaintext tabindex="-1"}
    [root@37a3635afb8f /]# dnf install nmap-ncat
    [root@37a3635afb8f /]# nc -lvp 21
    …
    Ncat: Listening on :::21
    Ncat: Listening on 0.0.0.0:21
    ^C
    [root@37a3635afb8f /]# nc -lvp 80
    …
    Ncat: bind to :::80: Permission denied. QUITTING.
    ```

**Additional resources**

-   [Udica - Generate SELinux policies for containers (Github.com)](https://github.com/containers/udica#creating-selinux-policy-for-container)
-   [Building, running, and managing containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/index)

## [Chapter 10. Deploying the same SELinux configuration on multiple systems](#deploying-the-same-selinux-configuration-on-multiple-systems) {#chapter-10.-deploying-the-same-selinux-configuration-on-multiple-systems .title}

Deploy your tested and verified SELinux configuration efficiently across multiple systems. Automating deployment helps ensure consistent security policies across your infrastructure.

You can deploy your verified SELinux configuration on multiple systems by using one of the following methods:

-   Using the RHEL web console
-   Using `semanage`{.literal} export and import commands in your scripts

For automated deployment using RHEL system roles and Ansible, see [Configuring SELinux by using RHEL system roles](#configuring-selinux-by-using-rhel-system-roles "Chapter 11. Configuring SELinux by using RHEL system roles").

### [10.1. Creating an SELinux configuration Ansible Playbook in the web console](#creating-an-selinux-configuration-ansible-playbook-in-the-web-console) {#creating-an-selinux-configuration-ansible-playbook-in-the-web-console .title}

Generate an Ansible Playbook directly from the RHEL web console that captures your current SELinux configuration settings. You can copy this script and apply it to multiple systems to quickly deploy a consistent configuration.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click **SELinux**.

3.  Click View the automation script.

    A window with the generated script opens. You can navigate between a shell script and an Ansible Playbook generation options tab.

4.  Click the Copy to clipboard button to select the script or playbook and apply it.

    As a result, you have an automation script that you can apply to more machines. See the `ansible-playbook(1)`{.literal} man page on your system for more information.

### [10.2. Transferring SELinux settings to another system with semanage](#transferring-selinux-settings-to-another-system-with-semanage) {#transferring-selinux-settings-to-another-system-with-semanage .title}

Transfer verified, custom SELinux configuration settings between RHEL 10 systems by using the `semanage export`{.literal} and `semanage import`{.literal} commands. This is a reliable way to replicate security setups.

**Prerequisites**

-   The `policycoreutils-python-utils`{.literal} package is installed on your system.

**Procedure**

1.  Export your verified SELinux settings:

    ``` {.language-plaintext tabindex="-1"}
    # semanage export -f ./<my-selinux-settings.mod>
    ```

2.  Copy the file with the settings to the new system:

    ``` {.language-plaintext tabindex="-1"}
    # scp ./<my-selinux-settings.mod> <new-system-hostname>:
    ```

3.  Log in on the new system:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh root@<new-system-hostname>
    ```

4.  Import the settings on the new system:

    ``` {.language-plaintext tabindex="-1"}
    <new-system-hostname># semanage import -f ./<my-selinux-settings.mod>
    ```

## [Chapter 11. Configuring SELinux by using RHEL system roles](#configuring-selinux-by-using-rhel-system-roles) {#chapter-11.-configuring-selinux-by-using-rhel-system-roles .title}

Automate SELinux configuration across multiple systems by using the `selinux`{.literal} RHEL system role for consistent security policy management.

For example, use the `selinux`{.literal} role for the following tasks:

-   Cleaning local policy modifications related to SELinux booleans, file contexts, ports, and logins.
-   Setting SELinux policy booleans, file contexts, ports, and logins.
-   Restoring file contexts on specified files or directories.
-   Managing SELinux modules.

### [11.1. Restoring the SELinux context on directories by using the selinux RHEL system role](#restoring-the-selinux-context-on-directories-by-using-the-selinux-rhel-system-role) {#restoring-the-selinux-context-on-directories-by-using-the-selinux-rhel-system-role .title}

To remotely reset the SELinux context on directories, you can use the `selinux`{.literal} RHEL system role. With an incorrect SELinux context, applications can fail to access the files.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Managing SELinux
      hosts: managed-node-01.example.com
      tasks:
        - name: Restore SELinux context
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.selinux
          vars:
            selinux_restore_dirs:
              - /var/www/
              - /etc/
    ```

    The settings specified in the example playbook include the following:

    `selinux_restore_dirs: `{.literal}*`<list>`{.literal}*
    :   Defines the list of directories on which the role resets the SELinux context.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.selinux/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Display the SELinux context for files or directories for which you have reset the context. For example, to display the context on the `/var/www/`{.literal} directory, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ansible rhel10.example.com -m command -a 'ls -ldZ /var/www/'
    drwxr-xr-x. 4 root root system_u:object_r:httpd_sys_content_t:s0 33 Feb 28 13:20 /var/www/
    ```

### [11.2. Managing SELinux network port labels by using the selinux RHEL system role](#managing-selinux-network-port-labels-by-using-the-selinux-rhel-system-role) {#managing-selinux-network-port-labels-by-using-the-selinux-rhel-system-role .title}

If you want to run a service on a non-standard port, you must set the corresponding SELinux type label on this port to prevent SELinux denying permission to the service. By using the `selinux`{.literal} RHEL system role, you can automate this task and remotely assign a type label on ports.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Managing SELinux
      hosts: managed-node-01.example.com
      tasks:
        - name: Set http_port_t label on network port
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.selinux
          vars:
            selinux_ports:
              - ports: <port_number>
                proto: tcp
                setype: http_port_t
                state: present
    ```

    The settings specified in the example playbook include the following:

    `ports: `{.literal}*`<port_number>`{.literal}*
    :   Defines the port numbers to which you want to assign the SELinux label. Separate multiple values by comma.

    `setype: `{.literal}*`<type_label>`{.literal}*
    :   Defines the SELinux type label.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.selinux/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Display the port numbers that have the `http_port_t`{.literal} label assigned:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m shell -a 'semanage port --list | grep http_port_t'
    http_port_t      tcp     80, 81, 443, <port_number>, 488, 8008, 8009, 8443, 9000
    ```

### [11.3. Deploying an SELinux module by using the selinux RHEL system role](#deploying-an-selinux-module-by-using-the-selinux-rhel-system-role) {#deploying-an-selinux-module-by-using-the-selinux-rhel-system-role .title}

If the default SELinux policies do not meet your requirements, you can create custom modules to allow your application to access the required resources. By using the `selinux`{.literal} RHEL system role, you can automate this process and remotely deploy SELinux modules.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).

-   You are logged in to the control node as a user who can run playbooks on the managed nodes.

-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

-   The SELinux module you want to deploy is stored in the same directory as the playbook.

-   The SELinux module is available in the Common Intermediate Language (CIL) or policy package (PP) format.

    If you are using a PP module, ensure that `policydb`{.literal} version on the managed nodes is the same or later than the version used to build the PP module.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Managing SELinux
      hosts: managed-node-01.example.com
      tasks:
        - name: Deploying a SELinux module
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.selinux
          vars:
            selinux_modules:
              - path: <module_file>
            priority: <value>
                state: enabled
    ```

    The settings specified in the example playbook include the following:

    `path: `{.literal}*`<module_file>`{.literal}*
    :   Sets the path to the module file on the control node.

    `priority: `{.literal}*`<value>`{.literal}*
    :   Sets the SELinux module priority. `400`{.literal} is the default.

    `state: `{.literal}*`<value>`{.literal}*

    :   Defines the state of the module:

        -   `enabled`{.literal}: Install or enable the module.
        -   `disabled`{.literal}: Disable a module.
        -   `absent`{.literal}: Remove a module.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.selinux/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Remotely display the list of SELinux modules and filter for the one you used in the playbook:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m shell -a 'semodule -l | grep <module>'
    ```

    If the module is listed, it is installed and enabled.

## [Chapter 12. Configuring polyinstantiated directories](#configuring-polyinstantiated-directories) {#chapter-12.-configuring-polyinstantiated-directories .title}

Configure polyinstantiated directories for `/tmp`{.literal}, `/var/tmp`{.literal}, and home directories to protect against race-condition attacks and information leaks. This configuration creates separate, isolated mounts for each user, preventing exploitation of shared temporary storage.

By default, all programs, services, and users use the `/tmp`{.literal}, `/var/tmp`{.literal}, and home directories for temporary storage. This makes these directories vulnerable to race-condition attacks and information leaks based on file names. You can make `/tmp/`{.literal}, `/var/tmp/`{.literal}, and the home directory instantiated so that they are no longer shared between all users, and each user's `/tmp-inst`{.literal} and `/var/tmp/tmp-inst`{.literal} is separately mounted to the `/tmp`{.literal} and `/var/tmp`{.literal} directory. See the `/usr/share/doc/pam-docs/txts/README.pam_namespace`{.literal} file installed with the `pam-docs`{.literal} package for more information.

**Procedure**

1.  Enable polyinstantiation in SELinux:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool -P allow_polyinstantiation 1
    ```

    You can verify that polyinstantiation is enabled in SELinux by entering the `getsebool allow_polyinstantiation`{.literal} command.

2.  Create the directory structure for data persistence over reboot with the necessary permissions:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /tmp-inst /var/tmp/tmp-inst --mode 000
    ```

3.  Restore the entire security context including the SELinux user part:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Fv /tmp-inst /var/tmp/tmp-inst
    Relabeled /tmp-inst from unconfined_u:object_r:default_t:s0 to system_u:object_r:tmp_t:s0
    Relabeled /var/tmp/tmp-inst from unconfined_u:object_r:tmp_t:s0 to system_u:object_r:tmp_t:s0
    ```

4.  If your system uses the `fapolicyd`{.literal} application control framework, allow `fapolicyd`{.literal} to monitor file access events on the underlying file system when they are bind mounted by enabling the `allow_filesystem_mark`{.literal} option in the `/etc/fapolicyd/fapolicyd.conf`{.literal} configuration file.

    ``` {.language-plaintext tabindex="-1"}
    allow_filesystem_mark = 1
    ```

5.  Enable instantiation of the `/tmp`{.literal}, `/var/tmp/`{.literal}, and users\' home directories:

    Important

    Use `/etc/security/namespace.conf`{.literal} instead of a separate file in the `/etc/security/namespace.d/`{.literal} directory because the `pam_namespace_helper`{.literal} program does not read additional files in `/etc/security/namespace.d`{.literal}.

    a.  On a system with multi-level security (MLS), uncomment the last three lines in the `/etc/security/namespace.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        /tmp     /tmp-inst/             level     root,adm
        /var/tmp /var/tmp/tmp-inst/    level     root,adm
        $HOME    $HOME/$USER.inst/     level
        ```

    b.  On a system without multi-level security (MLS), add the following lines in the `/etc/security/namespace.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        /tmp     /tmp-inst/            user   root,adm
        /var/tmp /var/tmp/tmp-inst/    user      root,adm
        $HOME    $HOME/$USER.inst/     user
        ```

6.  Verify that the `pam_namespace.so`{.literal} module is configured for the session:

    ``` {.language-plaintext tabindex="-1"}
    $ grep namespace /etc/pam.d/login
    session    required     pam_namespace.so
    ```

7.  Optional: Enable cloud users to access the system with SSH keys:

    a.  Install the `openssh-keycat`{.literal} package.

    b.  Create a file in the `/etc/ssh/sshd_config.d/`{.literal} directory with the following content:

        ``` {.language-plaintext tabindex="-1"}
        AuthorizedKeysCommand /usr/libexec/openssh/ssh-keycat
        AuthorizedKeysCommandRunAs root
        ```

    c.  Verify that public key authentication is enabled by checking that the `PubkeyAuthentication`{.literal} variable in `sshd_config`{.literal} is set to `yes`{.literal}. By default, `PubkeyAuthentication`{.literal} is set to yes, even though the line in `sshd_config`{.literal} is commented out.

        ``` {.language-plaintext tabindex="-1"}
        $ grep -r PubkeyAuthentication /etc/ssh/
        /etc/ssh/sshd_config:#PubkeyAuthentication yes
        ```

8.  Add the `session required pam_namespace.so unmnt_remnt`{.literal} entry into the module for each service for which polyinstantiation should apply, after the `session include system-auth`{.literal} line. For example, in `/etc/pam.d/su`{.literal}, `/etc/pam.d/sudo`{.literal}, `/etc/pam.d/ssh`{.literal}, and `/etc/pam.d/sshd`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    …
    session        include        system-auth
    session        required    pam_namespace.so unmnt_remnt
    …
    ```

**Verification**

1.  Log in as a non-root user. Users that were logged in before polyinstantiation was configured must log out and log in before the changes take effect for them.

2.  Check that the `/tmp/`{.literal} directory is mounted under `/tmp-inst/`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ findmnt --mountpoint /tmp/
    TARGET SOURCE                   FSTYPE OPTIONS
    /tmp   /dev/vda1[/tmp-inst/<user>] xfs   rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota
    ```

    The `SOURCE`{.literal} output differs based on your environment. \* On virtual systems, it shows `/dev/vda_<number>_`{.literal}. \* On bare-metal systems, it shows `/dev/sda_<number>_`{.literal} or `/dev/nvme*`{.literal}

## [Legal Notice](#idm140601391755040) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
