---
{"title": "Managing IdM users, groups, hosts, and access control rules", "guide": "managing_idm_users_groups_hosts_and_access_control_rules", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_idm_users_groups_hosts_and_access_control_rules/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Managing IdM users, groups, hosts, and access control rules {#managing-idm-users-groups-hosts-and-access-control-rules .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Configuring users and hosts, managing them in groups, and controlling access with host-based and role-based access control rules {#configuring-users-and-hosts-managing-them-in-groups-and-controlling-access-with-host-based-and-role-based-access-control-rules .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139997968406128)

**Abstract**

The main feature of Red Hat Identity Management (IdM) is the management of users, groups, hosts, and access control rules, such as host-based access control (HBAC) and role-based access control (RBAC). You can configure them by using the command line, the IdM Web UI, and Ansible Playbooks.

The management tasks include configuring Kerberos policies and security, automating group memberships, and delegating permissions.

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

## [Chapter 1. Managing user accounts using the command line](#managing-user-accounts-using-the-command-line) {#chapter-1.-managing-user-accounts-using-the-command-line .title}

Manage the complete user lifecycle in Identity Management (IdM) using command-line tools. Create, activate, preserve, delete, and restore user accounts to handle employee onboarding, departures, and returns.

### [1.1. User life cycle](#user-life-cycle_managing-user-accounts-using-the-command-line) {#user-life-cycle .title}

Identity Management (IdM) user accounts progress through three states: Stage, Active, and Preserved. Understanding this lifecycle helps you provision new accounts, manage departures, and restore users when needed.

-   **Stage** users are not allowed to authenticate. This is an initial state. Some of the user account properties required for active users cannot be set, for example, group membership.
-   **Active** users are allowed to authenticate. All required user account properties must be set in this state.
-   **Preserved** users are former active users that are considered inactive and cannot authenticate to IdM. Preserved users retain most of the account properties they had as active users, but they are not part of any user groups.

You can delete user entries permanently from the IdM database.

Important

Deleted user accounts cannot be restored. When you delete a user account, all the information associated with the account is permanently lost.

A new administrator can only be created by a user with administrator rights, such as the default admin user. If you accidentally delete all administrator accounts, the Directory Manager must create a new administrator manually in the Directory Server.

Warning

Do not delete the `admin`{.literal} user. As `admin`{.literal} is a pre-defined user required by IdM, this operation causes problems with certain commands. If you want to define and use an alternative admin user, disable the pre-defined `admin`{.literal} user with `ipa user-disable admin`{.literal} after you granted admin permissions to at least one different user.

Warning

Do not add local users to IdM. The Name Service Switch (NSS) always resolves IdM users and groups before resolving local users and groups. This means that, for example, IdM group membership does not work for local users.

### [1.2. Adding users using the command line](#adding-users-using-the-command-line) {#adding-users-using-the-command-line .title}

Add user accounts to Identity Management (IdM) from the command line to provision access for new employees or prepare stage accounts in advance. You can create active users who can authenticate immediately or stage users who require activation before use.

The following procedure describes adding active users to the IdM server with the `ipa user-add`{.literal} command.

Similarly, you can create stage user accounts with the `ipa stageuser-add`{.literal} command.

Warning

IdM automatically assigns a unique user ID (UID) to new user accounts. You can assign a UID manually by using the `--uid=INT`{.literal} option with the `ipa user-add`{.literal} command, but the server does not validate whether the UID number is unique. Consequently, multiple user entries might have the same UID number. A similar problem can occur with user private group IDs (GIDs) if you assign a GID to a user account manually by using the `--gidnumber=INT`{.literal} option. To check if you have multiple user entries with the same ID, enter `ipa user-find --uid=<uid>`{.literal} or `ipa user-find --gidnumber=<gidnumber>`{.literal}.

Red Hat recommends you do not have multiple entries with the same UIDs or GIDs. If you have objects with duplicate IDs, security identifiers (SIDs) are not generated correctly. SIDs are crucial for trusts between IdM and Active Directory and for Kerberos authentication to work correctly.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   Obtained a Kerberos ticket. For details, see link:[Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Open terminal and connect to the IdM server.

2.  Add user login, user's first name, last name and optionally, you can also add their email address.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-add user_login --first=first_name --last=last_name --email=email_address
    ```

    IdM supports user names that can be described by the following regular expression:

    ``` {.language-plaintext tabindex="-1"}
    [a-zA-Z0-9_.][a-zA-Z0-9_.-]{0,252}[a-zA-Z0-9_.$-]?
    ```

    Note

    User names ending with the trailing dollar sign (\$) are supported to enable Samba 3.x machine support.

    If you add a user name containing uppercase characters, IdM automatically converts the name to lowercase when saving it. Therefore, IdM always requires to enter user names in lowercase when logging in. Additionally, it is not possible to add user names which differ only in letter casing, such as **user** and **User**.

    The default maximum length for user names is 32 characters. To change it, use the `ipa config-mod --maxusername`{.literal} command. For example, to increase the maximum user name length to 64 characters:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa config-mod --maxusername=64
     Maximum username length: 64
     ...
    ```

    The `ipa user-add`{.literal} command includes a lot of parameters. To list them all, use the ipa help command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa help user-add
    ```

    For details about `ipa help`{.literal} command, see [What is the IPA help](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/introduction-to-the-idm-command-line-utilities#what-is-the-ipa-help).

**Verification**

1.  List all IdM user accounts:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-find
    ```

**Additional resources**

-   [Strengthening Kerberos security with PAC information](#strengthening-kerberos-security-with-pac-information "Chapter 14. Strengthening Kerberos security with PAC information")
-   [Are user/group collisions supported in Red Hat Enterprise Linux? (Red Hat Knowledgebase)](https://access.redhat.com/solutions/529333)

### [1.3. Activating users using the command line](#activating-users-using-the-command-line) {#activating-users-using-the-command-line .title}

Activate a stage user account to enable authentication. Use the `ipa stageuser-activate`{.literal} command to move prepared accounts from stage to active status when the user is ready to begin work.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   Obtained a Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Open terminal and connect to the IdM server.

2.  Activate the user account with the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa stageuser-activate user_login
    -------------------------
    Stage user user_login activated
    -------------------------
    ...
    ```

**Verification**

-   List all IdM user accounts:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-find
    ```

### [1.4. Preserving users using the command line](#preserving-users-using-the-command-line) {#preserving-users-using-the-command-line .title}

Preserve a user account using the Identity Management (IdM) CLI to remove the account from active use while retaining the option to restore it later.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   Obtained a Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Open terminal and connect to the IdM server.

2.  Preserve the user account with the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-del --preserve user_login
    --------------------
    Deleted user "user_login"
    --------------------
    ```

    Note

    Despite the output saying the user account was deleted, it has been preserved.

### [1.5. Deleting users using the command line](#deleting-users-using-the-command-line) {#deleting-users-using-the-command-line .title}

Permanently delete user accounts from Identity Management (IdM) when the account data is no longer needed. You can delete active, stage, or preserved users using the appropriate `ipa`{.literal} command.

Use the following commands to delete users based on their account state:

-   `ipa user-del`{.literal} - Delete active or preserved users
-   `ipa stageuser-del`{.literal} - Delete stage users

When deleting multiple users, use the `--continue`{.literal} option to force the command to continue regardless of errors. A summary of the successful and failed operations is printed to the `stdout`{.literal} standard output stream when the command completes.

``` {.language-plaintext tabindex="-1"}
$ *ipa user-del --continue user1 user2 user3*
```

If you do not use `--continue`{.literal}, the command proceeds with deleting users until it encounters an error, after which it stops and exits.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   Obtained a Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Open terminal and connect to the IdM server.

2.  Delete the user account with the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-del user_login
    --------------------
    Deleted user "user_login"
    --------------------
    ```

    The user account has been permanently deleted from IdM.

### [1.6. Restoring users using the command line](#restoring-users-using-the-command-line) {#restoring-users-using-the-command-line .title}

Restore a preserved user account to active or stage status to, for example, re-enable access for returning employees. You can restore preserved users to active or stage status.

Restoring a user account does not restore all of the account's previous attributes. For example, the user's password is not restored and must be set again.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   Obtained a Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Open terminal and connect to the IdM server.

2.  Activate the user account with the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-undel user_login
    ------------------------------
    Undeleted user account "user_login"
    ------------------------------
    ```

    Alternatively, you can restore user accounts as staged:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-stage user_login
    ------------------------------
    Staged user account "user_login"
    ------------------------------
    ```

**Verification**

-   You can verify if the new user account is successfully created by listing all IdM user accounts:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-find
    ```

    This command lists all user accounts with details.

### [1.7. Additional resources](#managing-user-accounts-using-the-command-line_17-additional-resources) {#additional-resources .title}

-   [Introduction to the IdM command-line utilities](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/introduction-to-the-idm-command-line-utilities) :!context:

## [Chapter 2. Managing user accounts using the IdM Web UI](#managing-user-accounts-using-the-idm-web-ui) {#chapter-2.-managing-user-accounts-using-the-idm-web-ui .title}

Manage the complete user lifecycle in the Identity Management (IdM) Web UI. Create, activate, disable, enable, preserve, restore, and delete user accounts to handle employee onboarding, temporary leaves, and departures.

### [2.1. User life cycle](#user-life-cycle_managing-user-accounts-using-the-idm-web-ui) {#user-life-cycle-1 .title}

Identity Management (IdM) user accounts progress through three states: Stage, Active, and Preserved. Understanding this lifecycle helps you provision new accounts, manage departures, and restore users when needed.

-   **Stage** users are not allowed to authenticate. This is an initial state. Some of the user account properties required for active users cannot be set, for example, group membership.
-   **Active** users are allowed to authenticate. All required user account properties must be set in this state.
-   **Preserved** users are former active users that are considered inactive and cannot authenticate to IdM. Preserved users retain most of the account properties they had as active users, but they are not part of any user groups.

You can delete user entries permanently from the IdM database.

Important

Deleted user accounts cannot be restored. When you delete a user account, all the information associated with the account is permanently lost.

A new administrator can only be created by a user with administrator rights, such as the default admin user. If you accidentally delete all administrator accounts, the Directory Manager must create a new administrator manually in the Directory Server.

Warning

Do not delete the `admin`{.literal} user. As `admin`{.literal} is a pre-defined user required by IdM, this operation causes problems with certain commands. If you want to define and use an alternative admin user, disable the pre-defined `admin`{.literal} user with `ipa user-disable admin`{.literal} after you granted admin permissions to at least one different user.

Warning

Do not add local users to IdM. The Name Service Switch (NSS) always resolves IdM users and groups before resolving local users and groups. This means that, for example, IdM group membership does not work for local users.

### [2.2. Adding users in the Web UI](#adding-users-in-the-web-ui) {#adding-users-in-the-web-ui .title}

Create user accounts in the Identity Management (IdM) Web UI to provision access for new employees. You can create active users who can authenticate immediately or stage users who require activation before use.

**Prerequisites**

-   Administrator privileges for managing IdM or `User Administrator`{.literal} role.

**Procedure**

1.  Log in to the IdM Web UI.

    For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

2.  Go to **Users → Stage Users** tab.

    Alternatively, you can add the user account in the **Users → Active users**, however, you cannot add user groups to the account.

3.  Click the **+ Add** icon.

4.  Optional: In the **User login** field, add a login name.

    If you leave it empty, the IdM server creates the login name in the following pattern: The first letter of the first name and the surname. The whole login name can have up to 32 characters.

5.  Enter **First name** and **Last name** of the new user.

6.  Optional: In the GID drop down menu, select groups in which the user should be included.

    Note that this option is only available on the **Active Users** dialog box.

7.  Optional: In the **Password** and **Verify password** fields, enter your password and confirm it, ensuring they both match.

8.  Click the **Add** button.

    At this point, you can see the user account in the **Stage Users** or **Active Users** table.

    If you click on the user name, you can edit advanced settings, such as adding a phone number, address, or occupation.

    Warning

    IdM automatically assigns a unique user ID (UID) to new user accounts. You can assign a UID manually, or even modify an already existing UID. However, the server does not validate whether the new UID number is unique. Consequently, multiple user entries might have the same UID number assigned. A similar problem can occur with user private group IDs (GIDs) if you assign GIDs to user accounts manually. You can use the `ipa user-find --uid=<uid>`{.literal} or `ipa user-find --gidnumber=<gidnumber>`{.literal} commands on the IdM CLI to check if you have multiple user entries with the same ID.

    You should not have multiple entries with the same UIDs or GIDs. If you have objects with duplicate IDs, security identifiers (SIDs) are not generated correctly. SIDs are crucial for trusts between IdM and Active Directory and for Kerberos authentication to work correctly.

**Additional resources**

-   [Strengthening Kerberos security with PAC information](#strengthening-kerberos-security-with-pac-information "Chapter 14. Strengthening Kerberos security with PAC information")
-   [Are user/group collisions supported in Red Hat Enterprise Linux? (Red Hat Knowledgebase)](https://access.redhat.com/solutions/529333)

### [2.3. Activating stage users in the IdM Web UI](#activating-stage-users-in-the-idm-web-ui) {#activating-stage-users-in-the-idm-web-ui .title}

Activate a stage user account in the Identity Management (IdM) Web UI to enable the user to log in to IdM and be added to groups. This step is required before the user can authenticate.

**Prerequisites**

-   Administrator privileges for managing the IdM Web UI or `User Administrator`{.literal} role.
-   At least one staged user account in IdM.

**Procedure**

1.  Log in to the IdM Web UI.

    For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

2.  Go to **Users → Stage users** tab.

3.  Click the checkbox of the user account you want to activate.

4.  Click on the **Activate** button.

5.  Click **OK** on the **Confirmation** dialog box.

    If the activation is successful, the IdM Web UI displays a green confirmation that the user has been activated and the user account has been moved to **Active users**. The account is active and the user can authenticate to the IdM domain and IdM Web UI. The user is prompted to change their password on the first login.

    Additionally, at this stage, you can add the active user account to user groups.

### [2.4. Disabling user accounts in the Web UI](#disabling-user-accounts-in-the-web-ui) {#disabling-user-accounts-in-the-web-ui .title}

Disable active user accounts temporarily to prevent authentication while preserving group memberships and account data. Disabled accounts remain in the active users list and can be re-enabled later.

Disabled user accounts still exist within Identity Management (IdM) and all of the associated information remains unchanged. Unlike preserved user accounts, disabled user accounts remain in the active state and can be a member of user groups.

Note

After disabling a user account, any existing connections remain valid until the user's Kerberos TGT and other tickets expire. After the ticket expires, the user will not be able to renew it.

**Prerequisites**

-   Administrator privileges for managing the IdM Web UI or User Administrator role.

**Procedure**

1.  Log in to the IdM Web UI.

    For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

2.  Go to **Users → Active users** tab.

3.  Click the checkbox of the user accounts you want to disable.

4.  Click the **Disable** button.

5.  Click the **OK** button on the **Confirmation** dialog box.

    If the accounts are disabled successfully, you can verify this in the Status column in the **Active users** table.

### [2.5. Enabling user accounts in the Web UI](#enabling-user-accounts-in-the-web-ui) {#enabling-user-accounts-in-the-web-ui .title}

Re-enable a disabled user account in the Identity Management (IdM) Web UI to restore authentication capabilities.

**Prerequisites**

-   Administrator privileges for managing the IdM Web UI or User Administrator role.

**Procedure**

1.  Log in to the IdM Web UI.

2.  Go to **Users → Active users** tab.

3.  Click the checkbox of the user accounts you want to enable.

4.  Click the **Enable** button.

5.  Click the **OK** button on the **Confirmation** dialog box.

    If the change is successful, you can verify this in the Status column in the **Active Users** table.

### [2.6. Preserving active users in the IdM Web UI](#preserving-active-users-in-the-idm-web-ui) {#preserving-active-users-in-the-idm-web-ui .title}

Preserve user accounts in the IdM Web UI to remove them from active use while retaining account data for potential restoration.

Preserve a user account if an employee leaves the company. If you want to disable user accounts for a couple of weeks or months (parental leave, for example), disable the account. For details, see [Disabling user accounts in the Web UI](#disabling-user-accounts-in-the-web-ui "2.4. Disabling user accounts in the Web UI"). The preserved accounts are not active and users cannot use them to access your internal network, however, the account stays in the database with all the data.

You can move the restored accounts back to the active mode.

**Prerequisites**

-   Administrator privileges for managing the IdM (Identity Management) Web UI or User Administrator role.

**Procedure**

1.  Log in to the IdM Web UI.

    For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

2.  Go to **Users → Active users** tab.

3.  Click the checkbox of the user accounts you want to preserve.

4.  Click the **Delete** button.

5.  On the **Remove users** dialog box, click **preserve**.

6.  Click the **Delete** button.

    The user account is moved to **Preserved users**.

**Next steps**

-   If you need to restore preserved users, see the [Restoring users in the IdM Web UI](#restoring-users-in-the-idm-web-ui "2.7. Restoring users in the IdM Web UI").

### [2.7. Restoring users in the IdM Web UI](#restoring-users-in-the-idm-web-ui) {#restoring-users-in-the-idm-web-ui .title}

Restore preserved user accounts in the Identity Management (IdM) Web UI to, for example, re-enable access for returning employees. You can restore preserved users to active or stage status.

**Prerequisites**

-   Administrator privileges for managing the IdM Web UI or User Administrator role.

**Procedure**

1.  Log in to the IdM Web UI.

    For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

2.  Go to **Users → Preserved users** tab.

3.  Click the checkbox at the user accounts you want to restore.

4.  Click the **Restore** button.

5.  On the **Confirmation** dialog box, click the **OK** button.

    The IdM Web UI displays a green confirmation and moves the user accounts to the **Active users** tab.

### [2.8. Deleting users in the IdM Web UI](#deleting-users-in-the-idm-web-ui) {#deleting-users-in-the-idm-web-ui .title}

Permanently delete user accounts from Identity Management (IdM) when the account data is no longer needed. This irreversible operation removes the account, group memberships, and passwords from the IdM database.

You can delete:

-   Active users --- the IdM Web UI offers you with the options:

    -   Preserving users temporarily. For details, see the [Preserving active users in the IdM Web UI](#preserving-active-users-in-the-idm-web-ui "2.6. Preserving active users in the IdM Web UI").
    -   Deleting users permanently.

-   Stage users --- you can just delete stage users permanently.

-   Preserved users --- you can delete preserved users permanently.

The following procedure describes deleting active users. Similarly, you can delete user accounts on:

-   The **Stage users** tab
-   The **Preserved users** tab

**Prerequisites**

-   Administrator privileges for managing the IdM Web UI or User Administrator role.

**Procedure**

1.  Log in to the IdM Web UI.

    For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

2.  Go to **Users → Active users** tab.

    Alternatively, you can delete the user account in the **Users → Stage users** or **Users → Preserved users**.

3.  Click the **Delete** icon.

4.  On the **Remove users** dialog box, click **delete**.

5.  Click the **Delete** button.

    The users accounts are permanently deleted from IdM.

## [Chapter 3. Managing user accounts using Ansible playbooks](#managing-user-accounts-using-ansible-playbooks) {#chapter-3.-managing-user-accounts-using-ansible-playbooks .title}

Create, modify, and remove Identity Management (IdM) user accounts using Ansible playbooks to automate user lifecycle management across your domain. IdM supports three user account states: **Stage**, **Active**, **Preserved**.

For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-user.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/user`{.literal} directory on the control node.

### [3.1. Ensuring the presence of an IdM user using an Ansible playbook](#ensuring-the-presence-of-an-idm-user-using-an-ansible-playbook) {#ensuring-the-presence-of-an-idm-user-using-an-ansible-playbook .title}

Create or verify if an IdM user account exists using an Ansible playbook to automate user provisioning in your domain.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create an Ansible playbook file with the data of the user whose presence in IdM you want to ensure. To simplify this step, you can copy and modify the example in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/user/add-user.yml`{.literal} file. For example, to create user named *idm_user* and add *Password123* as the user password:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Playbook to handle users
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Create user idm_user
        freeipa.ansible_freeipa.ipauser:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: idm_user
          first: Alice
          last: Acme
          uid: 1000111
          gid: 10011
          phone: "+555123457"
          email: idm_user@acme.com
          passwordexpiration: "2023-01-19 23:59:59"
          password: "Password123"
          update_password: on_create
    ```

    You must use the following options to add a user:

    -   **name**: the login name
    -   **first**: the first name string
    -   **last**: the last name string

    For the full list of available user options, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-user.md`{.literal} Markdown file.

    Note

    If you use the `update_password: on_create`{.literal} option, Ansible only creates the user password when it creates the user. If the user is already created with a password, Ansible does not generate a new password.

2.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i path_to_inventory_directory/inventory.file path_to_playbooks_directory/add-IdM-user.yml
    ```

**Verification**

-   You can verify if the new user account exists in IdM by using the `ipa user-show`{.literal} command:

    1.  Log into `ipaserver`{.literal} as admin:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh admin@server.idm.example.com
        Password:
        [admin@server /]$
        ```

    2.  Request a Kerberos ticket for admin:

        ``` {.language-plaintext tabindex="-1"}
        $ kinit admin
        Password for admin@IDM.EXAMPLE.COM:
        ```

    3.  Request information about *idm_user*:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa user-show idm_user
          User login: idm_user
          First name: Alice
          Last name: Acme
          ....
        ```

    The user named *idm_user* is present in IdM.

### [3.2. Ensuring the presence of multiple IdM users using Ansible playbooks](#ensuring-the-presence-of-multiple-idm-users-using-ansible-playbooks) {#ensuring-the-presence-of-multiple-idm-users-using-ansible-playbooks .title}

Create or verify multiple Identity Management (IdM) user accounts in a single Ansible playbook run to efficiently provision users in bulk.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create an Ansible playbook file with the data of the users whose presence you want to ensure in IdM. To simplify this step, you can copy and modify the example in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/user/ensure-users-present.yml`{.literal} file. For example, to create users *idm_user_1*, *idm_user_2*, and *idm_user_3*, and add *Password123* as the password of *idm_user_1*:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Playbook to handle users
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Create user idm_users
        freeipa.ansible_freeipa.ipauser:
          ipaadmin_password: "{{ ipaadmin_password }}"
          users:
          - name: idm_user_1
            first: Alice
            last: Acme
            uid: 10001
            gid: 10011
            phone: "+555123457"
            email: idm_user@acme.com
            passwordexpiration: "2023-01-19 23:59:59"
            password: "Password123"
          - name: idm_user_2
            first: Bob
            last: Acme
            uid: 100011
            gid: 10011
          - name: idm_user_3
            first: Eve
            last: Acme
            uid: 1000111
            gid: 10011
    ```

    Note

    If you do not specify the **update_password: on_create** option, Ansible re-sets the user password every time the playbook is run: if the user has changed the password since the last time the playbook was run, Ansible re-sets password.

2.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i path_to_inventory_directory/inventory.file path_to_playbooks_directory/add-users.yml
    ```

**Verification**

-   You can verify if the user account exists in IdM by using the `ipa user-show`{.literal} command:

    1.  Log into `ipaserver`{.literal} as administrator:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh administrator@server.idm.example.com
        Password:
        [admin@server /]$
        ```

    2.  Display information about *idm_user_1*:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa user-show idm_user_1
          User login: idm_user_1
          First name: Alice
          Last name: Acme
          Password: True
          ....
        ```

    The user named *idm_user_1* is present in IdM.

### [3.3. Ensuring the presence of multiple IdM users from a JSON file using Ansible playbooks](#ensuring-the-presence-of-multiple-idm-users-from-a-json-file-using-ansible-playbooks) {#ensuring-the-presence-of-multiple-idm-users-from-a-json-file-using-ansible-playbooks .title}

Import user accounts from a `JSON`{.literal} file using Ansible to bulk-provision users from external data sources or HR systems.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create an Ansible playbook file with the necessary tasks. Reference the `JSON`{.literal} file with the data of the users whose presence you want to ensure. To simplify this step, you can copy and modify the example in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-user.md`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Ensure users' presence
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Include users_present.json
        include_vars:
          file: users_present.json

      - name: Users present
        freeipa.ansible_freeipa.ipauser:
          ipaadmin_password: "{{ ipaadmin_password }}"
          users: "{{ users }}"
    ```

2.  Create the `users.json`{.literal} file, and add the IdM users into it. To simplify this step, you can copy and modify the example in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-user.md`{.literal} file. For example, to create users *idm_user_1*, *idm_user_2*, and *idm_user_3*, and add *Password123* as the password of *idm_user_1*:

    ``` {.language-yaml tabindex="-1"}
    {
      "users": [
       {
        "name": "idm_user_1",
        "first": "First 1",
        "last": "Last 1",
        "password": "Password123"
       },
       {
        "name": "idm_user_2",
        "first": "First 2",
        "last": "Last 2"
       },
       {
        "name": "idm_user_3",
        "first": "First 3",
        "last": "Last 3"
       }
      ]
    }
    ```

3.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i path_to_inventory_directory/inventory.file path_to_playbooks_directory/ensure-users-present-jsonfile.yml
    ```

**Verification**

-   You can verify if the user accounts are present in IdM using the `ipa user-show`{.literal} command:

    1.  Log into `ipaserver`{.literal} as administrator:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh administrator@server.idm.example.com
        Password:
        [admin@server /]$
        ```

    2.  Display information about *idm_user_1*:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa user-show idm_user_1
          User login: idm_user_1
          First name: Alice
          Last name: Acme
          Password: True
          ....
        ```

    The user named *idm_user_1* is present in IdM.

### [3.4. Ensuring the absence of users using Ansible playbooks](#ensuring-the-absence-of-users-using-ansible-playbooks) {#ensuring-the-absence-of-users-using-ansible-playbooks .title}

Remove IdM user accounts using Ansible to automate user deprovisioning when employees leave or accounts are no longer needed.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create an Ansible playbook file with the users whose absence from IdM you want to ensure. To simplify this step, you can copy and modify the example in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/user/ensure-users-present.yml`{.literal} file. For example, to delete users *idm_user_1*, *idm_user_2*, and *idm_user_3*:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Playbook to handle users
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Delete users idm_user_1, idm_user_2, idm_user_3
        freeipa.ansible_freeipa.ipauser:
          ipaadmin_password: "{{ ipaadmin_password }}"
          users:
          - name: idm_user_1
          - name: idm_user_2
          - name: idm_user_3
          state: absent
    ```

2.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i path_to_inventory_directory/inventory.file path_to_playbooks_directory/delete-users.yml
    ```

**Verification**

You can verify that the user accounts do not exist in IdM by using the `ipa user-show`{.literal} command:

1.  Log into `ipaserver`{.literal} as administrator:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh administrator@server.idm.example.com
    Password:
    [admin@server /]$
    ```

2.  Request information about *idm_user_1*:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-show idm_user_1
    ipa: ERROR: idm_user_1: user not found
    ```

    The user named *idm_user_1* does not exist in IdM.

**Additional resources**

-   [User life cycle](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-user-accounts-using-the-command-line#user-life-cycle)

## [Chapter 4. Modifying user and group attributes in IdM](#modifying-user-and-group-attributes-in-idm) {#chapter-4.-modifying-user-and-group-attributes-in-idm .title}

Customize the Identity Management (IdM) user and group schema to match your organization's requirements. Modify LDAP object classes and attributes to control what information can be stored for users and groups.

IdM stores information as LDAP attributes. When you create a user entry, IdM automatically assigns it LDAP object classes that define which attributes are available to that entry. You can modify these object classes and their attributes to customize the schema. For example, you can change attribute formats such as the maximum characters allowed in a user name.

### [4.1. The default IdM user attributes](#the-default-idm-user-attributes) {#the-default-idm-user-attributes .title}

IdM user entries contain attributes that are set automatically or manually. Understanding which attributes are required, optional, or have default values helps you create user accounts correctly.

+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Web UI field            | Command-line option  | Required, optional, or default                                                                              |
+:========================+:=====================+:============================================================================================================+
| User login              | **username**         | Required                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| First name              | \--first             | Required                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Last name               | \--last              | Required                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Full name               | \--cn                | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Display name            | \--displayname       | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Initials                | \--initials          | Default                                                                                                     |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Home directory          | \--homedir           | Default                                                                                                     |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| GECOS field             | \--gecos             | Default                                                                                                     |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Shell                   | \--shell             | Default                                                                                                     |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Kerberos principal      | \--principal         | Default                                                                                                     |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Email address           | \--email             | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Password                | \--password          | Optional. Note that the script prompts for a new password, rather than accepting a value with the argument. |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| User ID number          | \--uid               | Default                                                                                                     |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Group ID number         | \--gidnumber         | Default                                                                                                     |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Street address          | \--street            | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| City                    | \--city              | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| State/Province          | \--state             | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Zip code                | \--postalcode        | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Telephone number        | \--phone             | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Mobile telephone number | \--mobile            | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Pager number            | \--pager             | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Fax number              | \--fax               | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Organizational unit     | \--orgunit           | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Job title               | \--title             | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Manager                 | \--manager           | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Car license             | \--carlicense        | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
|                         | \--noprivate         | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| SSH Keys                | \--sshpubkey         | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Additional attributes   | \--addattr           | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Department Number       | \--departmentnumber  | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Employee Number         | \--employeenumber    | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Employee Type           | \--employeetype      | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+
| Preferred Language      | \--preferredlanguage | Optional                                                                                                    |
+-------------------------+----------------------+-------------------------------------------------------------------------------------------------------------+

: Table 4.1. Default IdM user attributes

Show more

You can also add any attributes available in the following object classes, even if no Web UI or command-line argument for that attribute exists.

+---------------------------------------------------------------------+-------------------------------------------+
| Object classes                                                      | Description                               |
+:====================================================================+:==========================================+
| ipaobject, ipasshuser                                               | IdM object classes                        |
+---------------------------------------------------------------------+-------------------------------------------+
| person, organizationalperson, inetorgperson, inetuser, posixAccount | Person object classes                     |
+---------------------------------------------------------------------+-------------------------------------------+
| krbprincipalaux, krbticketpolicyaux                                 | Kerberos object classes                   |
+---------------------------------------------------------------------+-------------------------------------------+
| mepOriginEntry                                                      | Managed entries (template) object classes |
+---------------------------------------------------------------------+-------------------------------------------+

: Table 4.2. Default IdM user object classes

Show more

### [4.2. Considerations in changing the default user and group schema](#considerations-in-changing-the-default-user-and-group-schema) {#considerations-in-changing-the-default-user-and-group-schema .title}

Review these considerations before creating custom LDAP object classes or attributes for user and group entries. Schema modifications affect all future entries and require careful planning to avoid breaking existing functionality.

When you modify object classes, IdM provides the following validation:

-   All of the object classes and their specified attributes must be known to the LDAP server.
-   All default attributes that are configured for the entry must be supported by the configured object classes.

The IdM schema validation has limitations and the IdM server does not check that the defined user or group object classes contain all of the required object classes for IdM entries. For example, all IdM entries require the `ipaobject`{.literal} object class. However, if the user or group schema is changed, the server does not check if this object class is included. If the object class is accidentally deleted and you then try to add a new user, the attempt fails.

All object class changes are atomic, not incremental. You must define the entire list of default object classes every time a change occurs. For example, you may decide to create a custom object class to store employee information such as birthdays and employment start dates. In this scenario, you cannot simply add the custom object class to the list. Instead, you must set the entire list of current default object classes **plus** the new object class. If you do not include the **existing** default object classes when you update the configuration, the current settings are overwritten. This causes serious performance problems.

Note

After you modify the list of default object classes, new user and group entries contain the custom object classes but any old entries are not modified.

**Additional resources**

-   [Default IdM user object classes](#tab-default-idm-user-object-classes "Table 4.2. Default IdM user object classes")
-   [Default IdM user attributes](#tab_default-idm-user-attributes "Table 4.1. Default IdM user attributes")

### [4.3. Modifying user object classes in the IdM Web UI](#modifying-user-object-classes-in-the-idm-web-ui) {#modifying-user-object-classes-in-the-idm-web-ui .title}

Modify user object classes in the Identity Management (IdM) Web UI to add custom attributes to future user entries. New entries will have different attributes than existing user entries.

**Prerequisites**

-   You are logged in as the IdM administrator.

**Procedure**

1.  Open the **IPA Server** tab.

2.  Select the **Configuration** subtab.

3.  Scroll to the **User Options** area.

4.  Keep all the object classes listed in the [Default IdM user object classes](#tab-default-idm-user-object-classes "Table 4.2. Default IdM user object classes") table.

    Important

    If any object classes required by IdM are not included, then subsequent attempts to add a user entry will fail with object class violations.

5.  At the bottom of the users area, click **Add** for a new field to appear.

6.  Enter the name of the user object class you want to add.

7.  Click `Save`{.literal} at the top of the `Configuration`{.literal} page.

### [4.4. Modifying user object classes in the IdM CLI](#modifying-user-object-classes-in-the-idm-cli) {#modifying-user-object-classes-in-the-idm-cli .title}

Modify user object classes using the Identity Management (IdM) CLI to add custom attributes to future user entries. New entries will have different attributes than existing user entries.

**Prerequisites**

-   You have enabled the `brace expansion`{.literal} feature:

    ``` {.language-plaintext tabindex="-1"}
    # set -o braceexpand
    ```

-   You are logged in as the IdM administrator.

**Procedure**

-   Use the `ipa config-mod`{.literal} command to modify the current schema. For example, to add `top`{.literal} and `mailRecipient`{.literal} object classes to the future user entries:

    ``` {.language-plaintext tabindex="-1"}
    [bjensen@server ~]$ ipa config-mod --userobjectclasses={person,organizationalperson,inetorgperson,inetuser,posixaccount,krbprincipalaux,krbticketpolicyaux,ipaobject,ipasshuser,mepOriginEntry,top,mailRecipient}
    ```

    The command adds all the [ten user object classes that are native to IdM](#tab-default-idm-user-object-classes "Table 4.2. Default IdM user object classes") as well as the two new ones, `top`{.literal} and `mailRecipient`{.literal}.

    Important

    The information passed with the `config-mod`{.literal} command overwrites the previous values. If any user object classes required by IdM are not included, then subsequent attempts to add a user entry will fail with object class violations.

    Alternatively, you can add a user object class by using the `ipa config-mod --addattr ipauserobjectclasses=`{.literal}*`<user object class>`{.literal}* command. In this way, you do not risk forgetting a native IdM class in the list. For example, to add the `mailRecipient`{.literal} user object class without overwriting the current configuration, enter `ipa config-mod --addattr ipauserobjectclasses=mailRecipient`{.literal}. Analogously, to remove only the `mailRecipient`{.literal} object class, enter `ipa config-mod --delattr ipauserobjectclasses=mailRecipient`{.literal}.

### [4.5. Modifying group object classes in the IdM Web UI](#modifying-group-object-classes-in-the-idm-web-ui) {#modifying-group-object-classes-in-the-idm-web-ui .title}

Modify group object classes in the IdM Web UI to add custom attributes to future group entries. New groups will have different attributes than existing group entries.

The following group objects are available by default: \* top \* groupofnames \* nestedgroup \* ipausergroup \* ipaobject

In this example, you learn how to add additional group object classes to the future group entries.

**Prerequisites**

-   You are logged in as the IdM administrator.

**Procedure**

1.  Open the **IPA Server** tab.

2.  Select the **Configuration** subtab.

3.  Locate the **Group Options** area.

4.  Keep the default IdM group object classes.

    Important

    If any group object classes required by IdM are not included, then subsequent attempts to add a group entry will fail with object class violations.

5.  Click **Add** for a new field to appear.

6.  Enter the name of the group object class you want to add.

7.  Click **Save** at the top of the **Configuration** page.

### [4.6. Modifying group object classes in the IdM CLI](#modifying-group-object-classes-in-the-idm-cli) {#modifying-group-object-classes-in-the-idm-cli .title}

Modify group object classes using the Identity Management (IdM) CLI to add custom attributes to future group entries. New groups will have different attributes than existing group entries.

The following group objects are available by default: \* top \* groupofnames \* nestedgroup \* ipausergroup \* ipaobject

In this example, you add the `ipasshuser`{.literal} and `employee`{.literal} group object classes to the future group entries.

**Prerequisites**

-   You have enabled the `brace expansion`{.literal} feature:

    ``` {.language-plaintext tabindex="-1"}
    # set -o braceexpand
    ```

-   You are logged in as the IdM administrator.

**Procedure**

-   Use the `ipa config-mod`{.literal} command to modify the current schema. For example, to add `ipasshuser`{.literal} and `employee`{.literal} group object classes to the future user entries:

    ``` {.language-plaintext tabindex="-1"}
    [bjensen@server ~]$ ipa config-mod --groupobjectclasses={top,groupofnames,nestedgroup,ipausergroup,ipaobject,ipasshuser,employeegroup}
    ```

    The command adds all the default group object classes as well as the two new ones, `ipasshuser`{.literal} and `employeegroup`{.literal}.

    Important

    If any group object classes required by IdM are not included, then subsequent attempts to add a group entry will fail with object class violations.

    Note

    Instead of the comma-separated list inside curly braces with no spaces allowed that is used in the example above, you can use the `--groupobjectclasses`{.literal} argument repeatedly.

### [4.7. Default user and group attributes in IdM](#default-user-and-group-attributes-in-idm) {#default-user-and-group-attributes-in-idm .title}

Identity Management (IdM) uses templates with default values when creating new user and group entries. Customize these defaults to match your organization's requirements for home directories, shells, and naming conventions.

The template for users is more specific than the template for groups. IdM uses default values for several core attributes for IdM user accounts. These defaults can define actual values for user account attributes, such as the home directory location, or they can define the formats of attribute values, such as the user name length. The template also defines the object classes assigned to users.

For groups, the template only defines the assigned object classes.

In the IdM LDAP directory, these default definitions are all contained in a single configuration entry for the IdM server, `cn=ipaconfig,cn=etc,dc=example,dc=com`{.literal}.

You can modify the configuration of default user parameters in IdM by using the `ipa config-mod`{.literal} command. The table below summarizes some of the key parameters, the command-line options that you can use with `ipa config-mod`{.literal} to modify them, and the parameter descriptions.

+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Web UI field                     | Command-line option              | Description                                                                                                        |
+:=================================+:=================================+:===================================================================================================================+
| Maximum user name length         | `--maxusername`{.literal}        | Sets the maximum number of characters for user names. Default: 32.                                                 |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Root for home directories        | `--homedirectory`{.literal}      | Sets the default directory for user home directories. Default: `/home`{.literal}.                                  |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Default shell                    | `--defaultshell`{.literal}       | Sets the default shell for users. Default: `/bin/sh`{.literal}.                                                    |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Default user group               | `--defaultgroup`{.literal}       | Sets the default group for newly created accounts. Default: `ipausers`{.literal}.                                  |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Default e-mail domain            | `--emaildomain`{.literal}        | Sets the email domain for creating addresses based on user accounts. Default: server domain.                       |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Search time limit                | `--searchtimelimit`{.literal}    | Sets the maximum time in seconds for a search before returning results.                                            |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Search size limit                | `--searchrecordslimit`{.literal} | Sets the maximum number of records to return in a search.                                                          |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| User search fields               | `--usersearch`{.literal}         | Defines searchable fields in user entries, impacting server performance if too many attributes are set.            |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Group search fields              | `--groupsearch`{.literal}        | Defines searchable fields in group entries.                                                                        |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Certificate subject base         |                                  | Sets the base DN for creating subject DNs for client certificates during installation.                             |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Default user object classes      | `--userobjectclasses`{.literal}  | Defines object classes for creating user accounts. Must provide a complete list as it overwrites the existing one. |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Default group object classes     | `--groupobjectclasses`{.literal} | Defines object classes for creating group accounts. Must provide a complete list.                                  |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Password expiration notification | `--pwdexpnotify`{.literal}       | Defines the number of days before a password expires for sending a notification.                                   |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Password plug-in features        |                                  | Sets the format of allowable passwords for users.                                                                  |
+----------------------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------+

: Table 4.3. Default user parameters

Show more

### [4.8. Viewing and modifying user and group configuration in the IdM Web UI](#viewing-and-modifying-user-and-group-configuration-in-the-idm-web-ui) {#viewing-and-modifying-user-and-group-configuration-in-the-idm-web-ui .title}

View and modify default user and group attribute settings in the Identity Management (IdM) Web UI. Changes apply to newly created accounts while existing accounts remain unchanged.

**Prerequisites**

-   You are logged in as IdM `admin`{.literal}.

**Procedure**

1.  Open the **IPA Server** tab.

2.  Select the **Configuration** subtab.

3.  The **User Options** section has multiple fields you can review and edit.

4.  For example, to change the default shell for future IdM users from `/bin/sh`{.literal} to `/bin/bash`{.literal}, locate the **Default shell** field, and replace `/bin/sh`{.literal} with `/bin/bash`{.literal}.

5.  In the **Group Options** section, you can only review and edit the **Group search fields** field.

6.  Click the **Save** button at the top of the screen.

    The newly saved configuration will be applied to future IdM user and group accounts. The current accounts remain unchanged.

### [4.9. Viewing and modifying user and group configuration in the IdM CLI](#viewing-and-modifying-user-and-group-configuration-in-the-idm-cli) {#viewing-and-modifying-user-and-group-configuration-in-the-idm-cli .title}

View and modify default user and group attribute settings using the Identity Management (IdM) CLI. Changes apply to newly created accounts while existing accounts remain unchanged.

**Prerequisites**

-   You have the IdM `admin`{.literal} credentials.

**Procedure**

-   The `ipa config-show`{.literal} command displays the most common attribute settings. Use the `--all`{.literal} option for a complete list:

    ``` {.language-plaintext tabindex="-1"}
    [bjensen@server ~]$ ipa config-show --all
    dn: cn=ipaConfig,cn=etc,dc=example,dc=com
    Maximum username length: 32
    Home directory base: /home
    Default shell: /bin/sh
    Default users group: ipausers
    Default e-mail domain: example.com
    Search time limit: 2
    Search size limit: 100
    User search fields: uid,givenname,sn,telephonenumber,ou,title
    Group search fields: cn,description
    Enable migration mode: FALSE
    Certificate Subject base: O=EXAMPLE.COM
    Default group objectclasses: top, groupofnames, nestedgroup, ipausergroup, ipaobject
    Default user objectclasses: top, person, organizationalperson, inetorgperson, inetuser, posixaccount, krbprincipalaux, krbticketpolicyaux, ipaobject, ipasshuser
    Password Expiration Notification (days): 4
    Password plugin features: AllowNThash
    SELinux user map order: guest_u:s0$xguest_u:s0$user_u:s0$staff_u:s0-s0:c0.c1023$unconfined_u:s0-s0:c0.c1023
    Default SELinux user: unconfined_u:s0-s0:c0.c1023
    Default PAC types: MS-PAC, nfs:NONE
    cn: ipaConfig
    objectclass: nsContainer, top, ipaGuiConfig, ipaConfigObject
    ```

-   Use the `ipa config-mod`{.literal} command to modify an attribute. For example, to change the default shell for future IdM users from `/bin/sh`{.literal} to `/bin/bash`{.literal}, enter:

    ``` {.language-plaintext tabindex="-1"}
    [bjensen@server ~]$ ipa config-mod --defaultshell "/bin/bash"
    ```

    For more `ipa config-mod`{.literal} options, see the [Default user parameters](#tab-default-user-parameters "Table 4.3. Default user parameters") table.

    The new configuration will be applied to future IdM user and group accounts. The current accounts remain unchanged.

### [4.10. Additional resources](#modifying-user-and-group-attributes-in-idm_410-additional-resources) {#additional-resources-1 .title}

-   [Managing Directory Server attributes and values in DS 13](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/management_configuration_and_operations/managing-directory-attributes-and-values)

## [Chapter 5. Managing user passwords in IdM](#managing-user-passwords-in-idm) {#chapter-5.-managing-user-passwords-in-idm .title}

Manage Identity Management (IdM) user passwords including changing your own password, resetting other users\' passwords, and configuring password-related features. Control password resets, account lockouts, and authentication tracking.

### [5.1. Who can change IdM user passwords and how](#who-can-change-idm-user-passwords-and-how) {#who-can-change-idm-user-passwords-and-how .title}

Regular users can change only their own passwords and must meet the password policies applicable to the groups of which the user is a member. Administrators can reset any user's password without meeting policies, but these passwords expire on first login unless configured otherwise.

Administrators and users with password change rights can set initial passwords for new users and reset passwords for existing users. These passwords:

-   Do not have to meet the IdM password policies.
-   Expire after the first successful login. When this happens, IdM prompts the user to change the expired password immediately.

Note that the LDAP Directory Manager (DM) user can change user passwords using LDAP tools. A new password can override any IdM password policies. Passwords set by DM do not expire after the first login.

**Additional resources**

-   [Enabling password reset in IdM without prompting the user for a password change at the next login](#enabling-password-reset-in-idm-without-prompting-the-user-for-a-password-change-at-the-next-login "5.7. Enabling password reset in IdM without prompting the user for a password change at the next login")
-   [Defining IdM password policies](#defining-idm-password-policies "Chapter 6. Defining IdM password policies")

### [5.2. Changing your user password in the IdM Web UI](#changing-your-user-password-in-the-idm-web-ui) {#changing-your-user-password-in-the-idm-web-ui .title}

Change your own user password in the Identity Management (IdM) Web UI to maintain account security. The new password must meet the password policies for groups you belong to.

**Prerequisites**

-   Your password has not expired.

**Procedure**

1.  Log in to the IdM Web UI.

2.  In the upper right corner, click the name of the user who is logged into the IdM Web UI.

3.  Select **Change password**.

4.  Enter the current password.

5.  Enter the new password in the **New Password** field.

6.  Confirm the new password by entering it in the **Verify Password** field.

7.  Click **Reset Password**.

    Note

    Alternatively, you can go directly to https://*\<server.idm.example.com*\>/ipa/ui/reset_password.html, and change your password there.

### [5.3. Resetting another user's password in the IdM Web UI](#resetting-another-users-password-in-the-idm-web-ui) {#resetting-another-users-password-in-the-idm-web-ui .title}

Reset another user's password in the Identity Management (IdM) Web UI when they need a new password or have been locked out.

**Prerequisites**

-   You are logged in to the IdM Web UI as an administrative user.

**Procedure**

1.  Select **Identity\>Users**.
2.  Click the name of the user to edit.
3.  Click **Actions** and select **Reset password**.
4.  Enter the new password in the **New Password** field.
5.  Confirm the new password by entering it in the **Verify Password** field.
6.  Click **Reset Password**.

### [5.4. Resetting the Directory Manager user password](#resetting-the-directory-manager-user-password) {#resetting-the-directory-manager-user-password .title}

Reset the Directory Manager password if it is, for example, lost or compromised. This procedure requires `root`{.literal} access to the Identity Management (IdM) servers and must be performed on every server in your topology.

**Prerequisites**

-   You have `root`{.literal} access to all IdM servers.

**Procedure**

1.  On an IdM server, generate a new password hash by using the `pwdhash`{.literal} command. For example:

    ``` {.language-plaintext tabindex="-1"}
    # pwdhash -D /etc/dirsrv/slapd-IDM-EXAMPLE-COM password
    {PBKDF2_SHA256}AAAgABU0bKhyjY53NcxY33ueoPjOUWtl4iyYN5uW...
    ```

    By specifying the path to the Directory Server configuration, you automatically use the password storage scheme set in the `nsslapd-rootpwstoragescheme`{.literal} attribute to encrypt the new password.

2.  Stop all IdM services installed on the server:

    ``` {.language-plaintext tabindex="-1"}
    # ipactl stop
    ```

3.  Edit the `/etc/dirsrv/IDM-EXAMPLE-COM/dse.ldif`{.literal} file on the server and set the `nsslapd-rootpw`{.literal} attribute to the value generated by the `pwdhash`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-rootpw: {PBKDF2_SHA256}AAAgABU0bKhyjY53NcxY33ueoPjOUWtl4iyYN5uW...
    ```

4.  Start all IdM services installed on the server:

    ``` {.language-plaintext tabindex="-1"}
    # ipactl start
    ```

5.  Repeat steps 2-4 on all the remaining IdM replicas in your topology.

### [5.5. Changing your user password or resetting another user's password in IdM CLI](#changing-your-user-password-or-resetting-another-users-password-in-idm-cli) {#changing-your-user-password-or-resetting-another-users-password-in-idm-cli .title}

Change your own password or reset another user's password using the Identity Management (IdM) CLI. Administrators can reset passwords for any user while regular users can only change their own.

**Prerequisites**

-   You have obtained a ticket-granting ticket (TGT) for an IdM user.
-   If you are resetting another user's password, you must have obtained a TGT for an administrative user in IdM.

**Procedure**

-   Enter the `ipa user-mod`{.literal} command with the name of the user and the `--password`{.literal} option. The command will prompt you for the new password.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-mod idm_user --password
    Password:
    Enter Password again to verify:
    --------------------
    Modified user "idm_user"
    --------------------
    ...
    ```

    Note that you can also use the `ipa passwd `{.literal}*`idm_user`{.literal}* command instead of `ipa user-mod`{.literal}.

### [5.6. Additional commands for changing user passwords](#additional-commands-for-changing-user-passwords) {#additional-commands-for-changing-user-passwords .title}

Identity Management (IdM) supports multiple methods for changing user passwords, including PAM services, Kerberos, the IdM API, and LDAP. Each method has different requirements and use cases.

+------------------------+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Command                | Description                                                                                                                | Limitations                                                                            |
+:=======================+:===========================================================================================================================+:=======================================================================================+
| `passwd`{.literal}     | A user can change their own password using PAM service facilities and the `pam_sss`{.literal} module to interact with SSSD | The system must be enrolled in IdM and SSSD must be configured.                        |
+------------------------+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| `kpasswd`{.literal}    | A user can change their own password directly via the Kerberos protocol                                                    | The user must have a valid Kerberos ticket (TGT); does not require system enrollment.  |
+------------------------+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| `ipa passwd`{.literal} | An administrator or user can change a password through the IdM API                                                         | Requires an active Kerberos ticket and the `ipa-client`{.literal} packages installed.  |
+------------------------+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| `ldappasswd`{.literal} | An administrator or user can change a password directly via LDAP                                                           | Requires LDAP credentials (Bind DN) and direct network access to the Directory Server. |
+------------------------+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

: Table 5.1. Additional commands for changing user passwords

Show more

### [5.7. Enabling password reset in IdM without prompting the user for a password change at the next login](#enabling-password-reset-in-idm-without-prompting-the-user-for-a-password-change-at-the-next-login) {#enabling-password-reset-in-idm-without-prompting-the-user-for-a-password-change-at-the-next-login .title}

Grant specific administrators the ability to reset passwords without forcing users to change them on first login. As an Identity Management (IdM) Directory Manager, you can add administrators to the `passSyncManagersDNs`{.literal} attribute, which allows them to perform password resets without triggering the mandatory password change requirement and optionally bypass password policy enforcement.

Warning

Bypassing the password policy can be a security threat. Exercise caution when selecting users to whom you grant these additional privileges.

**Prerequisites**

-   You know the Directory Manager password.

**Procedure**

1.  Enter the `ldapmodify`{.literal} command to modify LDAP entries. Specify the name of the IdM server and the 389 port and press Enter:

    ``` {.language-plaintext tabindex="-1"}
    $ ldapmodify -x -D "cn=Directory Manager" -W -h server.idm.example.com -p 389
    Enter LDAP Password: <password>
    ```

2.  Enter the Directory Manager password.

3.  Enter the distinguished name for the `ipa_pwd_extop`{.literal} password synchronization entry and press Enter:

    ``` {.language-plaintext tabindex="-1"}
    dn: cn=ipa_pwd_extop,cn=plugins,cn=config
    ```

4.  Specify the `modify`{.literal} type of change and press Enter:

    ``` {.language-plaintext tabindex="-1"}
    changetype: modify
    ```

5.  Specify what type of modification you want LDAP to execute and to which attribute. Press Enter:

    ``` {.language-plaintext tabindex="-1"}
    add: passSyncManagersDNs
    ```

6.  Specify the administrative user accounts in the `passSyncManagersDNs`{.literal} attribute. The attribute is multi-valued. For example, to grant the `admin`{.literal} user the password resetting powers of Directory Manager:

    ``` {.language-plaintext tabindex="-1"}
    passSyncManagersDNs: \
    uid=admin,cn=users,cn=accounts,dc=example,dc=com
    ```

7.  Press Enter twice to stop editing the entry.

    The `admin`{.literal} user, listed under `passSyncManagerDNs`{.literal}, now has the additional privileges. Repeat the steps on every Identity Management (IdM) server in the domain.

### [5.8. Checking if an IdM user's account is locked](#checking-if-an-idm-users-account-is-locked) {#checking-if-an-idm-users-account-is-locked .title}

Determine if a user's account is locked due to failed login attempts by comparing their failed login count against the maximum allowed number of failures.

**Prerequisites**

-   You have obtained the ticket-granting ticket (TGT) of an administrative user in IdM.

**Procedure**

1.  Display the status of the user account to see the number of failed logins:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-status example_user
    -----------------------
    Account disabled: False
    -----------------------
      Server: idm.example.com
      Failed logins: 8
      Last successful authentication: N/A
      Last failed authentication: 20220229080317Z
      Time now: 2022-02-29T08:04:46Z
    ----------------------------
    Number of entries returned 1
    ----------------------------
    ```

2.  Display the number of allowed login attempts for a particular user:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa pwpolicy-show --user example_user
      Group: global_policy
      Max lifetime (days): 90
      Min lifetime (hours): 1
      History size: 0
      Character classes: 0
      Min length: 8
      Max failures: 6
      Failure reset interval: 60
      Lockout duration: 600
      Grace login limit: -1
    ```

3.  Compare the number of failed logins as displayed in the output of the `ipa user-status`{.literal} command with the **Max failures** number displayed in the output of the `ipa pwpolicy-show`{.literal} command. If the number of failed logins equals that of maximum allowed login attempts, the user account is locked.

**Additional resources**

-   [Unlocking user accounts after password failures in IdM](#unlocking-user-accounts-after-password-failures-in-idm "5.9. Unlocking user accounts after password failures in IdM")

### [5.9. Unlocking user accounts after password failures in IdM](#unlocking-user-accounts-after-password-failures-in-idm) {#unlocking-user-accounts-after-password-failures-in-idm .title}

Unlock a user account that was locked due to too many failed login attempts.

For security reasons, IdM does not display any warning message that the user account has been locked. Instead, the CLI prompt might continue asking the user for a password again and again.

IdM automatically unlocks the user account after a specified amount of time has passed. Alternatively, you can unlock the user account manually with the following procedure.

**Prerequisites**

-   You have obtained the ticket-granting ticket of an IdM administrative user.

**Procedure**

-   To unlock a user account, use the `ipa user-unlock`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-unlock idm_user
    -----------------------
    Unlocked account "idm_user"
    -----------------------
    ```

    After this, the user can log in again.

**Additional resources**

-   [Checking if an IdM user's account is locked](#checking-if-an-idm-users-account-is-locked "5.8. Checking if an IdM user’s account is locked")

### [5.10. Enabling the tracking of last successful Kerberos authentication for users in IdM](#enabling-the-tracking-of-last-successful-kerberos-authentication-for-users-in-idm) {#enabling-the-tracking-of-last-successful-kerberos-authentication-for-users-in-idm .title}

Enable tracking of last successful Kerberos authentication timestamps for auditing purposes. This feature is disabled by default for performance reasons.

**Prerequisites**

-   You have obtained the ticket-granting ticket (TGT) of an administrative user in IdM.
-   You have `root`{.literal} access to the IdM server on which you are executing the procedure.

**Procedure**

1.  Display the currently enabled password plug-in features:

    ``` {.language-plaintext tabindex="-1"}
    # ipa config-show | grep "Password plugin features"
      Password plugin features: pass:quotes[AllowNThash], pass:quotes[KDC:Disable Last Success]
    ```

    The output shows that the `KDC:Disable Last Success`{.literal} plug-in is enabled. The plug-in hides the last successful Kerberos authentication attempt from being visible in the ipa user-status output.

2.  Add the `--ipaconfigstring=`{.literal}*`feature`{.literal}* parameter for every feature to the `ipa config-mod`{.literal} command that is currently enabled, except for `KDC:Disable Last Success`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # ipa config-mod --ipaconfigstring='AllowNThash'
    ```

    This command enables only the `AllowNThash`{.literal} plug-in. To enable multiple features, specify the `--ipaconfigstring=`{.literal}*`feature`{.literal}* parameter separately for each feature.

3.  Restart IdM:

    ``` {.language-plaintext tabindex="-1"}
    # ipactl restart
    ```

## [Chapter 6. Defining IdM password policies](#defining-idm-password-policies) {#chapter-6.-defining-idm-password-policies .title}

You can use Identity Management (IdM) password policies to define security requirements for your domain and configure custom policies to manage user authentication criteria.

A password policy is a set of rules that passwords must meet. For example, a password policy can define the minimum password length and the maximum password lifetime. All users affected by this policy are required to set a sufficiently long password and change it frequently enough to meet the specified conditions. In this way, password policies help reduce the risk of someone discovering and misusing a user's password.

### [6.1. Password policies in IdM](#password-policies-in-idm) {#password-policies-in-idm .title}

Passwords are the most common way for Identity Management (IdM) users to authenticate to the IdM Kerberos domain. You can use IdM password policies to define password requirements that are automatically enforced by the Kerberos Key Distribution Center (KDC).

A password policy is a set of rules that passwords must meet. For example, a password policy can define the minimum password length and the maximum password lifetime. All users affected by this policy are required to set a sufficiently long password and change it frequently enough to meet the specified conditions. In this way, password policies help reduce the risk of someone discovering and misusing a user's password.

Note

The IdM password policy is set in the underlying LDAP directory, but the KDC enforces the password policy.

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute              | Explanation                                                                                                                                                   | Example                                                                                                                                                                                           |
+:=======================+:==============================================================================================================================================================+:==================================================================================================================================================================================================+
| Max lifetime           | The maximum amount of time in days that a password is valid before a user must reset it. The default value is 90 days.                                        | Max lifetime = 180                                                                                                                                                                                |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        | Note that if the attribute is set to 0, the password never expires.                                                                                           | User passwords are valid only for 180 days. After that, IdM prompts users to change them.                                                                                                         |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Min lifetime           | The minimum amount of time in hours that must pass between two password change operations.                                                                    | Min lifetime = 1                                                                                                                                                                                  |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               | After users change their passwords, they must wait at least 1 hour before changing them again.                                                                                                    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| History size           | The number of previous passwords that are stored. A user cannot reuse a password from their password history but can reuse old passwords that are not stored. | History size = 0                                                                                                                                                                                  |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               | In this case, the password history is empty and users can reuse any of their previous passwords.                                                                                                  |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Character classes      | The number of different character classes the user must use in the password. The character classes are:                                                       | Character classes = 0                                                                                                                                                                             |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        | \* Uppercase characters                                                                                                                                       | The default number of classes required is 0. To configure the number, run the `ipa pwpolicy-mod`{.literal} command with the `--minclasses`{.literal} option.                                      |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        | \* Lowercase characters                                                                                                                                       |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        | \* Digits                                                                                                                                                     |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        | \* Special characters, such as comma (,), period (.), asterisk (\*)                                                                                           |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        | \* Other UTF-8 characters                                                                                                                                     |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        | Using a character three or more times in a row decreases the character class by one. For example:                                                             |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        | \* `Secret1`{.literal} has 3 character classes: uppercase, lowercase, digits                                                                                  |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        | \* `Secret111`{.literal} has 2 character classes: uppercase, lowercase, digits, and a -1 penalty for using `1`{.literal} repeatedly                           |                                                                                                                                                                                                   |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Min length             | The minimum number of characters in a password.                                                                                                               | Min length = 8                                                                                                                                                                                    |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        | If any of the additional password policy options are set, then the minimum length of passwords is 6 characters.                                               | Users cannot use passwords shorter than 8 characters.                                                                                                                                             |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Max failures           | The maximum number of failed login attempts before IdM locks the user account.                                                                                | Max failures = 6                                                                                                                                                                                  |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               | IdM locks the user account when the user enters a wrong password 7 times in a row.                                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Failure reset interval | The amount of time in seconds after which IdM resets the current number of failed login attempts.                                                             | Failure reset interval = 60                                                                                                                                                                       |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               | If the user waits for more than 1 minute after the number of failed login attempts defined in `Max failures`{.literal}, the user can attempt to log in again without risking a user account lock. |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lockout duration       | The amount of time in seconds that the user account is locked after the number of failed login attempts defined in `Max failures`{.literal}.                  | Lockout duration = 600                                                                                                                                                                            |
|                        |                                                                                                                                                               |                                                                                                                                                                                                   |
|                        |                                                                                                                                                               | Users with locked accounts are unable to log in for 10 minutes.                                                                                                                                   |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 6.1. Password Policy Attributes

Show more

Important

Use the English alphabet and common symbols for the character classes requirement if you have a diverse set of hardware that may not have access to international characters and symbols.

**Additional resources**

-   [What characters are valid in a password?](https://access.redhat.com/solutions/3143431)
-   [Additional password policy options in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/defining-idm-password-policies#additional-password-policy-options-in-idm)

### [6.2. Password policy priorities in IdM](#password-policy-priorities-in-idm) {#password-policy-priorities-in-idm .title}

When a user belongs to multiple groups, IdM applies a password policy to the user based on the priority values of the applicable policies.

Password policies help reduce the risk of someone discovering and misusing a user's password. The default password policy is the *global password policy*. You can also create additional group password policies. The global policy rules apply to all users without a group password policy. Group password policies apply to all members of the corresponding user group.

Note that only one password policy can be in effect at a time for any user. If a user has multiple password policies assigned, one of them takes precedence based on priority according to the following rules:

-   Every group password policy has a priority set. The lower the value, the higher the policy's priority. The lowest supported value is `0`{.literal}.
-   If multiple password policies are applicable to a user, the policy with the lowest priority value takes precedence. All rules defined in other policies are ignored.
-   The password policy with the lowest priority value applies to all password policy attributes, even the attributes that are not defined in the policy.

The global password policy does not have a priority value set. It serves as a fallback policy when no group policy is set for a user. The global policy can never take precedence over a group policy.

Note

The `ipa pwpolicy-show --user=user_name`{.literal} command shows which policy is currently in effect for a particular user.

### [6.3. Adding a new password policy in IdM using the WebUI or the CLI](#adding-a-new-password-policy-in-idm-using-the-webui-or-the-cli) {#adding-a-new-password-policy-in-idm-using-the-webui-or-the-cli .title}

Complex password policies help reduce the risk of someone discovering and misusing a user's password. The default password policy is the *global password policy*. You can also create additional group password policies.

#### [6.3.1. Adding a new password policy in the IdM WebUI](#adding-a-new-password-policy-in-the-idm-webui) {#adding-a-new-password-policy-in-the-idm-webui .title}

Create a group-specific password policy in the Identity Management (IdM) WebUI to enforce different password requirements for different user groups. This allows stronger policies for privileged groups.

**Prerequisites**

-   A user group to which the policy applies.
-   A priority assigned to the policy

**Procedure**

1.  Log in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

2.  Select **Policy\>Password Policies**.

3.  Click **Add**.

4.  Define the user group and priority.

5.  Click **Add** to confirm.

    To configure the attributes of the new password policy, see [Password policies in IdM](#password-policies-in-idm "6.1. Password policies in IdM").

**Additional resources**

-   [Password policy priorities in IdM](#password-policy-priorities-in-idm "6.2. Password policy priorities in IdM")

#### [6.3.2. Adding a new password policy in the IdM CLI](#adding-a-new-password-policy-in-the-idm-cli) {#adding-a-new-password-policy-in-the-idm-cli .title}

Create a group-specific password policy using the Identity Management (IdM) CLI to enforce different password requirements for different user groups. This allows stronger policies for privileged groups.

**Prerequisites**

-   A user group to which the policy applies.
-   A priority assigned to the policy

**Procedure**

1.  Open terminal and connect to the IdM server.

2.  Use the `ipa pwpolicy-add`{.literal} command. Specify the user group and priority:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa pwpolicy-add
    Group: group_name
    Priority: priority_level
    ```

3.  Optional. Use the `ipa pwpolicy-find`{.literal} command to verify that the policy has been successfully added:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa pwpolicy-find
    ```

    To configure the attributes of the new password policy, see [Password policies in IdM](#password-policies-in-idm "6.1. Password policies in IdM").

**Additional resources**

-   [Password policy priorities in IdM](#password-policy-priorities-in-idm "6.2. Password policy priorities in IdM")

### [6.4. Additional password policy options in IdM](#additional-password-policy-options-in-idm) {#additional-password-policy-options-in-idm .title}

The `libpwquality`{.literal}-based password policy options in Identity Management (IdM) control character type requirements, repetition limits, monotonic sequence checks, dictionary checks, and username restrictions for user group password policies.

`--maxrepeat`{.literal}
:   Specifies the maximum acceptable number of same consecutive characters in the new password.

`--maxsequence`{.literal}
:   Specifies the maximum length of monotonic character sequences in the new password. Examples of such a sequence are **12345** or **fedcb**. Most such passwords will not pass the simplicity check.

`--dictcheck`{.literal}
:   If nonzero, checks whether the password, with possible modifications, matches a word in a dictionary. Currently `libpwquality`{.literal} performs the dictionary check using the `cracklib`{.literal} library.

`--usercheck`{.literal}
:   If nonzero, checks whether the password, with possible modifications, contains the user name in some form. It is not performed for user names shorter than 3 characters.

`--minclasses`{.literal}
:   Specifies the minimum number of character classes that must be present in the password. The character classes are uppercase characters, lowercase characters, digits, special characters, and other UTF-8 characters. The default value is `0`{.literal}, which means no class requirement is enforced.

`--dcredit`{.literal}
:   Specifies the credit for digits in the password. Use a negative value to set the minimum required number of digits; for example, `--dcredit=-1`{.literal} requires at least one digit. Use a positive value to grant a credit toward the minimum password length for each digit included.

`--ucredit`{.literal}
:   Specifies the credit for uppercase characters in the password. Use a negative value to set the minimum required number of uppercase characters; for example, `--ucredit=-1`{.literal} requires at least one uppercase character. Use a positive value to grant a credit toward the minimum password length for each uppercase character included.

`--lcredit`{.literal}
:   Specifies the credit for lowercase characters in the password. Use a negative value to set the minimum required number of lowercase characters; for example, `--lcredit=-1`{.literal} requires at least one lowercase character. Use a positive value to grant a credit toward the minimum password length for each lowercase character included.

`--ocredit`{.literal}
:   Specifies the credit for other characters in the password, that is, characters that are neither digits nor letters. Use a negative value to set the minimum required number of such characters; for example, `--ocredit=-1`{.literal} requires at least one such character. Use a positive value to grant a credit toward the minimum password length for each such character included.

You cannot apply the additional password policy options to existing passwords. If you apply any of the additional options, IdM automatically sets the `--minlength`{.literal} option, the minimum number of characters in a password, to **6** characters.

Note

In a mixed environment with RHEL 7, RHEL 8, RHEL 9, and RHEL 10 servers, you can enforce the additional password policy settings only on servers running on RHEL 8.4 and later. If a user is logged in to an IdM client and the IdM client is communicating with an IdM server running on RHEL 8.3 or earlier, then the new password policy requirements set by the system administrator will not be applied. To ensure consistent behavior, upgrade or update all servers to RHEL 8.4 and later.

Note

The `--dcredit`{.literal}, `--ucredit`{.literal}, `--lcredit`{.literal}, and `--ocredit`{.literal} options are available on RHEL 10.2 and later. In a mixed environment, servers running an earlier version do not apply these settings. You cannot use these options together with `--minclasses`{.literal}; setting both raises a validation error.

**Additional resources**

-   [Applying additional password policies to an IdM group](#applying-additional-password-policy-options-to-an-idm-group "6.5. Applying additional password policy options to an IdM group")

### [6.5. Applying additional password policy options to an IdM group](#applying-additional-password-policy-options-to-an-idm-group) {#applying-additional-password-policy-options-to-an-idm-group .title}

To enforce stricter password requirements and enhance domain security, you can configure advanced password quality checks for specific user groups in IdM.

The example describes how to strengthen the password policy for the **managers** group by making sure that the new passwords do not contain the users\' respective user names and that the passwords contain no more than two identical characters in succession. You can also optionally require specific character types using the character credit options.

**Prerequisites**

-   You are logged in as an IdM administrator.
-   The **managers** group exists in IdM.
-   The **managers** password policy exists in IdM.

**Procedure**

1.  Apply the user name check to all new passwords suggested by the users in the **managers** group:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa pwpolicy-mod --usercheck=True managers
    ```

    If you do not specify the name of the password policy, the default `global_policy`{.literal} is modified.

2.  Set the maximum number of identical consecutive characters to 2 in the **managers** password policy:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa pwpolicy-mod --maxrepeat=2 managers
    ```

    A password now will not be accepted if it contains more than 2 identical consecutive characters. For example, the **eR873mUi111YJQ** combination is unacceptable because it contains three **1**s in succession.

3.  **Optional:** To require specific character types, use the character credit options. For example, to require at least one digit and at least one uppercase character in the **managers** password policy:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa pwpolicy-mod --dcredit=-1 --ucredit=-1 managers
    ```

    You cannot use the character credit options together with `--minclasses`{.literal}. Setting both raises a validation error.

**Verification**

1.  Verify the `--usercheck`{.literal} and `--maxrepeat`{.literal} options. If you also configured character credit options, the same rejection pattern applies - a password that does not meet the character type requirements is rejected with the `Unspecified password quality failure`{.literal} error message.

2.  Add a test user named **test_user**:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-add test_user
    First name: test
    Last name: user
    ----------------------------
    Added user "test_user"
    ----------------------------
    ```

3.  Add the test user to the **managers** group:

    a.  In the IdM Web UI, click Identity → Groups → User Groups.
    b.  Click **managers**.
    c.  Click `Add`{.literal}.
    d.  In the **Add users into user group \'managers\'** page, check **test_user**.
    e.  Click the `>`{.literal} arrow to move the user to the `Prospective`{.literal} column.
    f.  Click `Add`{.literal}.

4.  Reset the password for the test user:

    a.  Go to Identity → Users.
    b.  Click **test_user**.
    c.  In the `Actions`{.literal} menu, click `Reset Password`{.literal}.
    d.  Enter a temporary password for the user.

5.  On the command line, try to obtain a Kerberos ticket-granting ticket (TGT) for the **test_user**:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit test_user
    ```

    a.  Enter the temporary password.

    b.  The system informs you that you must change your password. Enter a password that contains the user name of **test_user**:

        ``` {.language-plaintext tabindex="-1"}
        Password expired. You must change it now.
        Enter new password:
        Enter it again:
        Password change rejected: Password not changed.
        Unspecified password quality failure while trying to change password.
        Please try again.
        ```

        Note

        Kerberos does not have fine-grained error password policy reporting and, in certain cases, does not provide a clear reason why a password was rejected.

    c.  The system informs you that the entered password was rejected. Enter a password that contains three or more identical characters in succession:

        ``` {.language-plaintext tabindex="-1"}
        Password change rejected: Password not changed.
        Unspecified password quality failure while trying to change password.
        Please try again.

        Enter new password:
        Enter it again:
        ```

    d.  The system informs you that the entered password was rejected. Enter a password that meets the criteria of the **managers** password policy:

        ``` {.language-plaintext tabindex="-1"}
        Password change rejected: Password not changed.
        Unspecified password quality failure while trying to change password.
        Please try again.

        Enter new password:
        Enter it again:
        ```

6.  View the obtained TGT:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    Ticket cache: KCM:0:33945
    Default principal: test_user@IDM.EXAMPLE.COM

    Valid starting       Expires              Service principal
    07/07/2021 12:44:44  07/08/2021 12:44:44  krbtgt@IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    ```

The **managers** password policy now works correctly for users in the **managers** group.

**Additional resources**

-   [Additional password policy options in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/defining-idm-password-policies#additional-password-policy-options-in-idm)
-   [Using an Ansible playbook to apply additional password policy options to an IdM group](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/defining-idm-password-policies-in-ansible#using-an-ansible-playbook-to-apply-additional-password-policy-options-to-an-idm-group)

### [6.6. Additional resources](#defining-idm-password-policies_66-additional-resources) {#additional-resources-2 .title}

-   [Defining IdM password policies using an Ansible playbook](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/defining-idm-password-policies-in-ansible)

## [Chapter 7. Managing expiring password notifications](#managing-expiring-password-notifications) {#chapter-7.-managing-expiring-password-notifications .title}

Notify Identity Management (IdM) users about expiring passwords using the Expiring Password Notification (EPN) tool. Configure automated daily emails or run on-demand checks to help users change their passwords before they expire.

### [7.1. What is the Expiring Password Notification tool](#what-is-the-expiring-password-notification-tool) {#what-is-the-expiring-password-notification-tool .title}

The Expiring Password Notification (EPN) tool identifies Identity Management (IdM) users with expiring passwords and can send automated email notifications, generate reports, or run on a scheduled timer. Use EPN to help users change passwords proactively and avoid account lockouts.

IdM administrators can use EPN to:

-   Display a list of affected users in JSON format, which is created when run in dry-run mode.
-   Calculate how many emails will be sent for a given day or date range.
-   Send password expiration email notifications to users.
-   Configure the `ipa-epn.timer`{.literal} to run the EPN tool daily and send an email to users whose passwords are expiring within the defined future date ranges.
-   Customize the email notification to send to users.

Note

If a user account is disabled, no email notifications are sent if the password is going to expire.

### [7.2. Installing the Expiring Password Notification tool](#installing-the-expiring-password-notification-tool) {#installing-the-expiring-password-notification-tool .title}

Install the Expiring Password Notification (EPN) tool on an Identity Management (IdM) replica or client to enable password expiration email notifications.

**Prerequisites**

-   Install the EPN tool on either an Identity Management (IdM) replica or an IdM client with a local Postfix SMTP server configured as a smart host.

**Procedure**

-   Install the EPN tool:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install ipa-client-epn
    ```

### [7.3. Running the EPN tool to send emails to users whose passwords are expiring](#running-the-epn-tool-to-send-emails-to-users-whose-passwords-are-expiring) {#running-the-epn-tool-to-send-emails-to-users-whose-passwords-are-expiring .title}

Configure and run the EPN tool to send password expiration email notifications to Identity Management (IdM) users.

To do this, follow one of the following methods:

-   Update the `epn.conf`{.literal} configuration file and [enable the ipa-epn.timer tool](#enabling-the-ipa-epn-timer-to-send-an-email-to-all-users-whose-passwords-are-expiring "7.4. Enabling the ipa-epn.timer to send an email to all users whose passwords are expiring").
-   Update the `epn.conf`{.literal} configuration file and run the EPN tool directly on the command line.

Note

The EPN tool is stateless. If the EPN tool fails to email any of the users whose passwords are expiring on a given day, the EPN tool does not save a list of those users.

**Prerequisites**

-   The `ipa-client-epn`{.literal} package is installed. See [Installing the Expiring Password Notification tool](#installing-the-expiring-password-notification-tool "7.2. Installing the Expiring Password Notification tool").
-   Customize the `ipa-epn`{.literal} email template if required. See [Modifying the Expiring Password Notification email template](#modifying-the-expiring-password-notification-email-template "7.5. Modifying the Expiring Password Notification email template").

**Procedure**

1.  Open the `epn.conf`{.literal} configuration file.

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/ipa/epn.conf
    ```

2.  Update the `notify_ttls`{.literal} option as required. The default is to notify users whose passwords are expiring in 28, 14, 7, 3, and 1 day(s).

    ``` {.language-plaintext tabindex="-1"}
    notify_ttls = 28, 14, 7, 3, 1
    ```

    Note

    You must also [activate the `ipa-epn.timer`{.literal} tool](#enabling-the-ipa-epn-timer-to-send-an-email-to-all-users-whose-passwords-are-expiring "7.4. Enabling the ipa-epn.timer to send an email to all users whose passwords are expiring") to ensure that emails are sent.

3.  Configure your SMTP server and port:

    ``` {.language-plaintext tabindex="-1"}
    smtp_server = localhost
    smtp_port = 25
    ```

4.  Specify the email address from which the email expiration notification is sent. Any unsuccessfully delivered emails are returned to this address.

    ``` {.language-plaintext tabindex="-1"}
    mail_from = admin-email@example.com
    ```

5.  Optional: If you want to use an encrypted channel of communication, specify the credentials to be used:

    -   Specify the path to a single file in PEM format containing the certificate to be used by EPN to authenticate with the SMTP server:

        ``` {.language-plaintext tabindex="-1"}
        smtp_client_cert = /etc/pki/tls/certs/client.pem
        ```

        Note

        EPN is an SMTP client. The purpose of the certificate is client authentication, not secure SMTP delivery.

    -   You can specify the path to a file that contains the private key. If not specified, the private key is taken from the certificate file.

        ``` {.language-plaintext tabindex="-1"}
        smtp_client_key = /etc/pki/tls/certs/client.key
        ```

    -   If the private key is encrypted, specify the password for decrypting it.

        ``` {.language-plaintext tabindex="-1"}
        smtp_client_key_pass = Secret123!
        ```

6.  Save the `/etc/ipa/epn.conf`{.literal} file.

7.  Run the EPN tool in dry-run mode to generate a list of the users to whom the password expiration email notification would be sent if you run the tool without the `--dry-run`{.literal} option.

    ``` {.language-plaintext tabindex="-1"}
    # ipa-epn --dry-run
    [
        {
         "uid": "user5",
         "cn": "user 5",
         "krbpasswordexpiration": "2020-04-17 15:51:53",
         "mail": "['user5@ipa.test']"
        }
    ]
    [
        {
         "uid": "user6",
         "cn": "user 6",
         "krbpasswordexpiration": "2020-12-17 15:51:53",
         "mail": "['user5@ipa.test']"
         }
    ]
    The IPA-EPN command was successful
    ```

    Note

    If the list of users returned is very large and you run the tool without the `--dry-run`{.literal} option, this might cause an issue with your email server.

8.  Run the EPN tool without the `--dry-run`{.literal} option to send expiration emails to the list of all the users returned when you ran the EPN tool in dry-run mode:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-epn
    [
      {
         "uid": "user5",
         "cn": "user 5",
         "krbpasswordexpiration": "2020-10-01 15:51:53",
         "mail": "['user5@ipa.test']"
      }
    ]
    [
      {
        "uid": "user6",
        "cn": "user 6",
        "krbpasswordexpiration": "2020-12-17 15:51:53",
        "mail": "['user5@ipa.test']"
      }
    ]
    The IPA-EPN command was successful
    ```

9.  You can add EPN to any monitoring system and invoke it with the `--from-nbdays`{.literal} and `--to-nbdays`{.literal} options to determine how many users passwords are going to expire within a specific time frame:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-epn --from-nbdays 8 --to-nbdays 12
    ```

    Note

    If you invoke the EPN tool with the `--from-nbdays`{.literal} and `--to-nbdays`{.literal} options, it is automatically executed in dry-run mode.

**Verification**

-   Run the EPN tool and verify an email notification is sent.

### [7.4. Enabling the ipa-epn.timer to send an email to all users whose passwords are expiring](#enabling-the-ipa-epn-timer-to-send-an-email-to-all-users-whose-passwords-are-expiring) {#enabling-the-ipa-epn.timer-to-send-an-email-to-all-users-whose-passwords-are-expiring .title}

Enable the `ipa-epn.timer`{.literal} to automatically run the EPN tool daily and send password expiration notifications.

The `ipa-epn.timer`{.literal} parses the `epn.conf`{.literal} file and sends an email to users whose passwords are expiring within the defined future date ranges configured in that file.

**Prerequisites**

-   The `ipa-client-epn`{.literal} package is installed. See [Installing the Expiring Password Notification tool](#installing-the-expiring-password-notification-tool "7.2. Installing the Expiring Password Notification tool")
-   Customize the `ipa-epn`{.literal} email template if required. See [Modifying the Expiring Password Notification email template](#modifying-the-expiring-password-notification-email-template "7.5. Modifying the Expiring Password Notification email template")

**Procedure**

-   Start the `ipa-epn.timer`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start ipa-epn.timer
    ```

    Once you start the timer, by default, the EPN tool is run every day at 1 a.m.

### [7.5. Modifying the Expiring Password Notification email template](#modifying-the-expiring-password-notification-email-template) {#modifying-the-expiring-password-notification-email-template .title}

Customize the EPN email template to change the message content and formatting. You can include user information such as name, ID, and password expiration date.

**Prerequisites**

-   The `ipa-client-epn`{.literal} package is installed.

**Procedure**

1.  Open the EPN message template:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/ipa/epn/expire_msg.template
    ```

2.  Update the template text as required.

    ``` {.language-plaintext tabindex="-1"}
    Hi {{ fullname }},

    Your password will expire on {{ expiration }}.

    Please change it as soon as possible.
    ```

    You can use the following variables in the template.

    -   User ID: uid
    -   Full name: fullname
    -   First name: first
    -   Last name: last
    -   Password expiration date: expiration

3.  Save the message template file.

**Verification**

-   Run the EPN tool and verify the email notification contains the updated text.

## [Chapter 8. Configuring a system account in IdM to change user passwords without requiring a reset](#configuring-a-system-account-in-idm-to-change-user-passwords-without-requiring-a-reset) {#chapter-8.-configuring-a-system-account-in-idm-to-change-user-passwords-without-requiring-a-reset .title}

Use an Identity Management (IdM) system account so an external credential-management system can set user passwords without forcing a reset on first login. You keep IdM password policy enforcement while integrating with external services.

By default, when an IdM administrator resets an IdM user's password, the password expires after the first successful login. However, when integrating your IdM deployment with external credential-management systems to take care of password storage, you may want to ensure that the passwords set by this external system do not expire when used for the first time, as this could be inconvenient for end users. At the same time, bypassing the IdM password policy would introduce a security risk, so keeping password strength and history checks in place on the IdM side is important.

For this scenario, the *system accounts* feature is available in IdM as of RHEL 10.2. Using system accounts you can, for example, delegate the security of managing highly privileged IdM accounts, that is those that possess administrative privileges, to this dedicated, external service, thereby meeting your compliance requirements.

### [8.1. System account management](#system-account-management) {#system-account-management .title}

The `System Accounts Administrators`{.literal} privilege in IdM controls who can create system accounts and configure password-change behavior. Assign it to the right roles so only authorized users can integrate IdM with external credential management.

The `System Accounts Administrators`{.literal} privilege has the following permissions to administer system accounts. The privilege is granted by default to the `Security Architect`{.literal} role in Identity Management (IdM):

-   Create system account objects.
-   Check whether system accounts have passwords defined.
-   Update system account information, including a password.
-   Remove the system account.
-   Allow a system account to change passwords without requiring a reset.
-   Identify which system accounts have the permission to change passwords without requiring a reset.

By default, members of the `admins`{.literal} group have the `System Accounts Administrators`{.literal} privilege.

### [8.2. Configuring a system account in IdM to change user passwords](#configuring-a-system-account-in-idm-to-change-user-passwords) {#configuring-a-system-account-in-idm-to-change-user-passwords .title}

Configure an Identity Management (IdM) system account with the correct privilege and role so it can change IdM user passwords without requiring a reset. This enables your external credential-management system to set passwords that work on first login.

**Prerequisites**

-   You are a member of a role that has the `System Accounts Administrators`{.literal} privilege, for example `admin`{.literal}.

**Procedure**

1.  Obtain your privileged credentials:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit admin
    ```

2.  Create the system account using one of the following options:

    -   To generate a random password to be used for LDAP authentication of the system account, use the `--random`{.literal} option with the `ipa sysaccount-add`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa sysaccount-add 'my-app' --random
        ```

    -   To be prompted for the password of your choice, use the `--password`{.literal} option with `ipa sysaccount-add`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa sysaccount-add 'my-app' --password
        ```

3.  Create a privilege:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa privilege-add 'my-app password change privilege'
    ```

4.  Add the permission to change user passwords to the **my-app password change privilege**:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa privilege-add-permission 'my-app password change privilege' --permission 'System: Change User password'
    ```

5.  Create the **my-app** role:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa role-add 'my-app role'
    ```

6.  Add the **my-app password change privilege** privilege to the **my-app** role:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa role-add-privilege 'my-app role' --privilege 'my-app password change privilege'
    ```

7.  Add the **my-app** system account to the **my-app role** role as member:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa role-add-member 'my-app role' --sysaccounts 'my-app'
    ```

8.  Optional: To allow password changes without reset, enter:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa sysaccount-policy 'my-app' --privileged=true
    ```

**Verification**

1.  Using your external credential-management system, change an IdM user's password.

2.  Log in to IdM as the IdM user:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit idmuser
    ```

3.  When prompted, enter the new password:

    ``` {.language-plaintext tabindex="-1"}
    idmuser's password:
    ```

4.  Verify that you have *idmuser*\'s Kerberos ticket-granting ticket:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Credentials cache: API:0A481BBD-C3AA-473D-B43A-42CD19C7F045
            Principal: idmuser@IDM.EXAMPLE.COM

      Issued                Expires               Principal
    Feb 23 16:06:56 2026  Feb 24 02:04:54 2026  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    ```

    The output confirms that you have a valid Kerberos ticket. You were able to log in without having to reset *idmuser*\'s password.

## [Chapter 9. Granting sudo access to an IdM user on an IdM client](#granting-sudo-access-to-an-idm-user-on-an-idm-client) {#chapter-9.-granting-sudo-access-to-an-idm-user-on-an-idm-client .title}

Configure centralized sudo rules in Identity Management (IdM) to grant users elevated privileges on specific hosts. Manage sudo access using the CLI or Web UI, allow users to run commands as service accounts, and enable GSSAPI authentication for passwordless sudo.

### [9.1. Sudo access on an IdM client](#sudo-access-on-an-idm-client) {#sudo-access-on-an-idm-client .title}

System administrators can grant `sudo`{.literal} access to non-root users on an Identity Management (IdM) client using rules defined locally in `/etc/sudoers`{.literal} or centrally in IdM.

If a Red Hat Enterprise Linux (RHEL) host is enrolled as an Identity Management (IdM) client, you can specify `sudo`{.literal} rules defining which IdM users can perform which commands on the host in the following ways:

-   Locally in the `/etc/sudoers`{.literal} file
-   Centrally in IdM

You can create a **central `sudo`{.literal} rule** for an IdM client using the command line (CLI) and the IdM Web UI.

You can also configure password-less authentication for `sudo`{.literal} using the Generic Security Service Application Programming Interface (GSSAPI), the native way for UNIX-based operating systems to access and authenticate Kerberos services. You can use the `pam_sss_gss.so`{.literal} Pluggable Authentication Module (PAM) to invoke GSSAPI authentication through the SSSD service, allowing users to authenticate to the `sudo`{.literal} command with a valid Kerberos ticket.

**Additional resources**

-   [Managing sudo access](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access)

### [9.2. Granting sudo access to an IdM user on an IdM client using the CLI](#granting-sudo-access-to-an-idm-user-on-an-idm-client-using-the-cli) {#granting-sudo-access-to-an-idm-user-on-an-idm-client-using-the-cli .title}

Create a `sudo`{.literal} rule using the Identity Management (IdM) CLI to grant a user permission to run specific commands with elevated privileges on a particular host.

First, add a `sudo`{.literal} command and then create a `sudo`{.literal} rule for one or more commands. In the example below, you create the *idm_user_reboot* `sudo`{.literal} rule to grant the *idm_user* account the permission to run the `/usr/sbin/reboot`{.literal} command on the *idmclient* machine.

**Prerequisites**

-   You are logged in as IdM administrator.
-   You have created a user account for **idm_user** in IdM and unlocked the account by creating a password for the user. For details on adding a new IdM user using the CLI, see [Adding users using the command line](#adding-users-using-the-command-line "1.2. Adding users using the command line").
-   No local **idm_user** account is present on the **idmclient** host. The **idm_user** user is not listed in the local `/etc/passwd`{.literal} file.

**Procedure**

1.  Retrieve a Kerberos ticket as the IdM `admin`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# kinit admin
    ```

2.  Add the `/usr/sbin/reboot`{.literal} command to the IdM database of `sudo`{.literal} commands:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudocmd-add /usr/sbin/reboot
    -------------------------------------
    Added Sudo Command "/usr/sbin/reboot"
    -------------------------------------
      Sudo Command: /usr/sbin/reboot
    ```

3.  Create a `sudo`{.literal} rule named **idm_user_reboot**:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudorule-add idm_user_reboot
    ---------------------------------
    Added Sudo Rule "idm_user_reboot"
    ---------------------------------
      Rule name: idm_user_reboot
      Enabled: TRUE
    ```

4.  Add the `/usr/sbin/reboot`{.literal} command to the **idm_user_reboot** rule:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudorule-add-allow-command idm_user_reboot --sudocmds '/usr/sbin/reboot'
      Rule name: idm_user_reboot
      Enabled: TRUE
      Sudo Allow Commands: /usr/sbin/reboot
    -------------------------
    Number of members added 1
    -------------------------
    ```

5.  Apply the **idm_user_reboot** rule to the IdM **idmclient** host:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudorule-add-host idm_user_reboot --hosts idmclient.idm.example.com
    Rule name: idm_user_reboot
    Enabled: TRUE
    Hosts: idmclient.idm.example.com
    Sudo Allow Commands: /usr/sbin/reboot
    -------------------------
    Number of members added 1
    -------------------------
    ```

6.  Add the **idm_user** account to the **idm_user_reboot** rule:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudorule-add-user idm_user_reboot --users idm_user
    Rule name: idm_user_reboot
    Enabled: TRUE
    Users: idm_user
    Hosts: idmclient.idm.example.com
    Sudo Allow Commands: /usr/sbin/reboot
    -------------------------
    Number of members added 1
    -------------------------
    ```

7.  Optional: Define the validity of the **idm_user_reboot** rule:

    a.  To define the time at which a `sudo`{.literal} rule starts to be valid, use the `ipa sudorule-mod `{.literal}*`sudo_rule_name`{.literal}* command with the `--setattr sudonotbefore=`{.literal}*`DATE`{.literal}* option. The *DATE* value must follow the **yyyymmddHHMMSSZ** format, with seconds specified explicitly. For example, to set the start of the validity of the **idm_user_reboot** rule to 31 December 2025 12:34:00, enter:

        ``` {.language-plaintext tabindex="-1"}
        [root@idmclient ~]# ipa sudorule-mod idm_user_reboot --setattr sudonotbefore=20251231123400Z
        ```

    b.  To define the time at which a sudo rule stops being valid, use the `--setattr sudonotafter=DATE`{.literal} option. For example, to set the end of the **idm_user_reboot** rule validity to 31 December 2026 12:34:00, enter:

        ``` {.language-plaintext tabindex="-1"}
        [root@idmclient ~]# ipa sudorule-mod idm_user_reboot --setattr sudonotafter=20261231123400Z
        ```

    Note

    Propagating the changes from the server to the client can take a few minutes.

**Verification**

1.  Log in to the **idmclient** host as the **idm_user** account.

2.  Display which `sudo`{.literal} rules the **idm_user** account is allowed to perform.

    ``` {.language-plaintext tabindex="-1"}
    [idm_user@idmclient ~]$ sudo -l
    Matching Defaults entries for idm_user on idmclient:
        !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin,
        env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
        env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE",
        env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES",
        env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE",
        env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY KRB5CCNAME",
        secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

    User idm_user may run the following commands on idmclient:
        (root) /usr/sbin/reboot
    ```

3.  Reboot the machine using `sudo`{.literal}. Enter the password for **idm_user** when prompted:

    ``` {.language-plaintext tabindex="-1"}
    [idm_user@idmclient ~]$ sudo /usr/sbin/reboot
    [sudo] password for idm_user:
    ```

### [9.3. Granting sudo access to an AD user on an IdM client using the CLI](#granting-sudo-access-to-an-ad-user-on-an-idm-client-using-the-cli) {#granting-sudo-access-to-an-ad-user-on-an-idm-client-using-the-cli .title}

You can use Identity Management (IdM) user groups to set access permissions, host-based access control, `sudo`{.literal} rules, and other controls on IdM users. IdM user groups grant and restrict access to IdM domain resources.

You can add both Active Directory (AD) *users* and AD *groups* to IdM user groups. To do that:

1.  Add the AD users or groups to a *non-POSIX* external IdM group.
2.  Add the non-POSIX external IdM group to an IdM *POSIX* group.

You can then manage the privileges of the AD users by managing the privileges of the POSIX group. For example, you can grant `sudo`{.literal} access for a specific command to an IdM POSIX user group on a specific IdM host.

Note

It is also possible to add AD user groups as members to IdM external groups. This might make it easier to define policies for Windows users, by keeping the user and group management within the single AD realm.

Important

Do **not** use ID overrides of AD users for SUDO rules in IdM. ID overrides of AD users represent only POSIX attributes of AD users, not AD users themselves.

You can add ID overrides as group members. However, you can only use this functionality to manage IdM resources in the IdM API. The possibility to add ID overrides as group members is not extended to POSIX environments and you therefore cannot use it for membership in `sudo`{.literal} or host-based access control (HBAC) rules.

Follow this procedure to create the **ad_users_reboot** `sudo`{.literal} rule to grant the **administrator@ad-domain.com** AD user the permission to run the `/usr/sbin/reboot`{.literal} command on the **idmclient** IdM host, which is normally reserved for the `root`{.literal} user. **administrator@ad-domain.com** is a member of the **ad_users_external** non-POSIX group, which is, in turn, a member of the **ad_users** POSIX group.

**Prerequisites**

-   You have obtained the IdM `admin`{.literal} Kerberos ticket-granting ticket (TGT).
-   A cross-forest trust exists between the IdM domain and the **ad-domain.com** AD domain.
-   No local **administrator** account is present on the **idmclient** host: the **administrator** user is not listed in the local `/etc/passwd`{.literal} file.

**Procedure**

1.  Create the ***ad_users*** group that contains the ***ad_users_external*** group with the **administrator@ad-domain** member:

    a.  Optional: Create or select a corresponding group in the AD domain to use to manage AD users in the IdM realm. You can use multiple AD groups and add them to different groups on the IdM side.

    b.  Create the ***ad_users_external*** group and indicate that it contains members from outside the IdM domain by adding the `--external`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        [root@ipaserver ~]# ipa group-add --desc='AD users external map' ad_users_external --external
        -------------------------------
        Added group "ad_users_external"
        -------------------------------
          Group name: ad_users_external
          Description: AD users external map
        ```

        Note

        Ensure that the external group that you specify here is an AD security group with a `global`{.literal} or `universal`{.literal} group scope as defined in the [Active Directory security groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups) document. For example, the **Domain users** or **Domain admins** AD security groups cannot be used because their group scope is `domain local`{.literal}.

    c.  Create the **ad_users** group:

        ``` {.language-plaintext tabindex="-1"}
        [root@ipaserver ~]# ipa group-add --desc='AD users' ad_users
        ----------------------
        Added group "ad_users"
        ----------------------
          Group name: ad_users
          Description: AD users
          GID: 129600004
        ```

    d.  Add the **administrator@ad-domain.com** AD user to **ad_users_external** as an external member:

        ``` {.language-plaintext tabindex="-1"}
        [root@ipaserver ~]# ipa group-add-member ad_users_external --external "administrator@ad-domain.com"
         [member user]:
         [member group]:
          Group name: ad_users_external
          Description: AD users external map
          External member: S-1-5-21-3655990580-1375374850-1633065477-513
        -------------------------
        Number of members added 1
        -------------------------
        ```

        The AD user must be identified by a fully-qualified name, such as `DOMAIN\user_name`{.literal} or `user_name@DOMAIN`{.literal}. The AD identity is then mapped to the AD SID for the user. The same applies to adding AD groups.

    e.  Add **ad_users_external** to **ad_users** as a member:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# ipa group-add-member ad_users --groups ad_users_external
      Group name: ad_users
      Description: AD users
      GID: 129600004
      Member groups: ad_users_external
    -------------------------
    Number of members added 1
    -------------------------
    ```

2.  Grant the members of **ad_users** the permission to run `/usr/sbin/reboot`{.literal} on the **idmclient** host:

    a.  Add the `/usr/sbin/reboot`{.literal} command to the IdM database of `sudo`{.literal} commands:

        ``` {.language-plaintext tabindex="-1"}
        [root@idmclient ~]# ipa sudocmd-add /usr/sbin/reboot
        -------------------------------------
        Added Sudo Command "/usr/sbin/reboot"
        -------------------------------------
          Sudo Command: /usr/sbin/reboot
        ```

    b.  Create a `sudo`{.literal} rule named **ad_users_reboot**:

        ``` {.language-plaintext tabindex="-1"}
        [root@idmclient ~]# ipa sudorule-add ad_users_reboot
        ---------------------------------
        Added Sudo Rule "ad_users_reboot"
        ---------------------------------
          Rule name: ad_users_reboot
          Enabled: True
        ```

    c.  Add the `/usr/sbin/reboot`{.literal} command to the **ad_users_reboot** rule:

        ``` {.language-plaintext tabindex="-1"}
        [root@idmclient ~]# ipa sudorule-add-allow-command ad_users_reboot --sudocmds '/usr/sbin/reboot'
          Rule name: ad_users_reboot
          Enabled: True
          Sudo Allow Commands: /usr/sbin/reboot
        -------------------------
        Number of members added 1
        -------------------------
        ```

    d.  Apply the **ad_users_reboot** rule to the IdM **idmclient** host:

        ``` {.language-plaintext tabindex="-1"}
        [root@idmclient ~]# ipa sudorule-add-host ad_users_reboot --hosts idmclient.idm.example.com
        Rule name: ad_users_reboot
        Enabled: True
        Hosts: idmclient.idm.example.com
        Sudo Allow Commands: /usr/sbin/reboot
        -------------------------
        Number of members added 1
        -------------------------
        ```

    e.  Add the `ad_users`{.literal} group to the **ad_users_reboot** rule:

        ``` {.language-plaintext tabindex="-1"}
        [root@idmclient ~]# ipa sudorule-add-user ad_users_reboot --groups ad_users
        Rule name: ad_users_reboot
        Enabled: TRUE
        User Groups: ad_users
        Hosts: idmclient.idm.example.com
        Sudo Allow Commands: /usr/sbin/reboot
        -------------------------
        Number of members added 1
        -------------------------
        ```

    Note

    Propagating the changes from the server to the client can take a few minutes.

**Verification**

1.  Log in to the **idmclient** host as **administrator@ad-domain.com**, an indirect member of the `ad_users`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh administrator@ad-domain.com@ipaclient
    Password:
    ```

2.  Optional: Display the `sudo`{.literal} commands that `administrator@ad-domain.com`{.literal} is allowed to run:

    ``` {.language-plaintext tabindex="-1"}
    [administrator@ad-domain.com@idmclient ~]$ sudo -l
    Matching Defaults entries for administrator@ad-domain.com on idmclient:
        !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin,
        env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
        env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE",
        env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES",
        env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE",
        env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY KRB5CCNAME",
        secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

    User administrator@ad-domain.com may run the following commands on idmclient:
        (root) /usr/sbin/reboot
    ```

3.  Reboot the machine using `sudo`{.literal}. Enter the password for `administrator@ad-domain.com`{.literal} when prompted:

    ``` {.language-plaintext tabindex="-1"}
    [administrator@ad-domain.com@idmclient ~]$ sudo /usr/sbin/reboot
    [sudo] password for administrator@ad-domain.com:
    ```

**Additional resources**

-   [Active Directory users and Identity Management groups](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html-single/windows_integration_guide/index#trust-win-groups)
-   [Include users and groups from a trusted Active Directory domain into SUDO rules](https://freeipa.readthedocs.io/en/latest/designs/adtrust/sudorules-with-ad-objects.html)

### [9.4. Granting sudo access to an IdM user on an IdM client using the IdM Web UI](#granting-sudo-access-to-an-idm-user-on-an-idm-client-using-the-idm-web-ui) {#granting-sudo-access-to-an-idm-user-on-an-idm-client-using-the-idm-web-ui .title}

In Identity Management (IdM), you can grant `sudo`{.literal} access for a specific command to an IdM user account on a specific IdM host. First, add a `sudo`{.literal} command and then create a `sudo`{.literal} rule for one or more commands.

Complete this procedure to create the `idmuser01_reboot`{.literal} sudo rule to grant the `idmuser01`{.literal} account the permission to run the `/usr/sbin/reboot`{.literal} command on the `client.idm.example.com`{.literal} machine, or `client`{.literal}.

**Prerequisites**

-   You are logged in to the IdM Web UI as `admin`{.literal}.
-   You have created a user account for `idmuser01`{.literal} in IdM and unlocked the account by creating a password for the user. For details on adding a new IdM user using the command line, see [Adding users using the command line](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_idm_users_groups_hosts_and_access_control_rules/index#adding-users-using-the-command-line).
-   No local `idmuser01`{.literal} account is present on the `client`{.literal} host. The `idmuser01`{.literal} user is not listed in the local `/etc/passwd`{.literal} file.
-   The **client.idm.example.com** host exists in IdM.

**Procedure**

1.  Add the `/usr/sbin/reboot`{.literal} command to the IdM database of `sudo`{.literal} commands:

    a.  Navigate to **Policy** → **Sudo** → **Sudo Commands**.

    b.  Click **Add** in the upper right corner to open the **Add sudo command** dialog box.

    c.  Enter the command you want the user to be able to perform using `sudo`{.literal}: `/usr/sbin/reboot`{.literal}.

    d.  Click **Add**.

2.  Use the new `sudo`{.literal} command entry to create a sudo rule to allow **idmuser01** to reboot the **client** machine:

    a.  Navigate to **Policy** → **Sudo** → **Sudo rules**.

    b.  Click **Add** in the upper right corner to open the **Add sudo rule** dialog box.

    c.  Enter the name of the `sudo`{.literal} rule: **idmuser01_reboot**.

    d.  Click **Add and Edit**.

    e.  Specify the user:

        i.  In the **Who** section, check the **Specified Users and Groups** radio button.
        ii. In the **User category the rule applies to** subsection, click **Add** to open the **Add users into sudo rule \"idmuser01_reboot\"** dialog box.
        iii. In the **Add users into sudo rule \"idmuser01_reboot\"** dialog box in the **Available** column, check the **idmuser01** checkbox, and move it to the **Prospective** column.
        iv. Click **Add**.

    f.  Specify the host:

        i.  In the **Access this host** section, check the **Specified Hosts and Groups** radio button.
        ii. In the **Host category this rule applies to** subsection, click **Add** to open the **Add hosts into sudo rule \"idmuser01_reboot\"** dialog box.
        iii. In the **Add hosts into sudo rule \"idmuser01_reboot\"** dialog box in the **Available** column, check the **client.idm.example.com** checkbox, and move it to the **Prospective** column.
        iv. Click **Add**.

    g.  Specify the commands:

        i.  In the **Command category the rule applies to** subsection of the **Run Commands** section, check the **Specified Commands and Groups** radio button.
        ii. In the **Sudo Allow Commands** subsection, click **Add** to open the **Add allow sudo commands into sudo rule \"idmuser01_reboot\"** dialog box.
        iii. In the **Add allow sudo commands into sudo rule \"idmuser01_reboot\"** dialog box in the **Available** column, check the `/usr/sbin/reboot`{.literal} checkbox, and move it to the **Prospective** column.
        iv. Click **Add** to return to the **idm_sudo_reboot** page.

        **Figure 9.1. Adding IdM sudo rule**

    h.  Click **Save** in the top left corner.

        The new rule is enabled by default.

    Note

    Propagating the changes from the server to the client can take a few minutes.

**Verification**

1.  Log in to `client`{.literal} as `idmuser01`{.literal}.

2.  Reboot the machine using `sudo`{.literal}. Enter the password for `idmuser01`{.literal} when prompted:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo /usr/sbin/reboot
    ```

    ``` {.language-plaintext tabindex="-1"}
    [sudo] password for idmuser01:
    ```

    If the `sudo`{.literal} rule is configured correctly, the machine reboots.

### [9.5. Creating a sudo rule on the CLI that runs a command as a service account on an IdM client](#creating-a-sudo-rule-on-the-cli-that-runs-a-command-as-a-service-account-on-an-idm-client) {#creating-a-sudo-rule-on-the-cli-that-runs-a-command-as-a-service-account-on-an-idm-client .title}

Create `sudo`{.literal} rules with *RunAs aliases* using the Identity Management (IdM) CLI to authorize users to run commands as service accounts. You use the *RunAs* functionality to separate separate administrative privileges from service accounts while maintaining auditability for application administration tasks.

For example, you might have an IdM client that hosts a database application, and you need to run commands as the local service account that corresponds to that application.

Use this example to create a `sudo`{.literal} rule on the command line called `run_third-party-app_report`{.literal} to allow the `idm_user`{.literal} account to run the `/opt/third-party-app/bin/report`{.literal} command as the `thirdpartyapp`{.literal} service account on the `idmclient`{.literal} host.

**Prerequisites**

-   You are logged in as IdM administrator.
-   You have created a user account for `idm_user`{.literal} in IdM and unlocked the account by creating a password for the user. For details on adding a new IdM user using the CLI, see [Adding users using the command line](#adding-users-using-the-command-line "1.2. Adding users using the command line").
-   No local `idm_user`{.literal} account is present on the `idmclient`{.literal} host. The `idm_user`{.literal} user is not listed in the local `/etc/passwd`{.literal} file.
-   You have a custom application named `third-party-app`{.literal} installed on the `idmclient`{.literal} host.
-   The `report`{.literal} command for the `third-party-app`{.literal} application is installed in the `/opt/third-party-app/bin/report`{.literal} directory.
-   You have created a local service account named `thirdpartyapp`{.literal} to run commands for the `third-party-app`{.literal} application.

**Procedure**

1.  Retrieve a Kerberos ticket as the IdM `admin`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# kinit admin
    ```

2.  Add the `/opt/third-party-app/bin/report`{.literal} command to the IdM database of `sudo`{.literal} commands:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudocmd-add /opt/third-party-app/bin/report
    ----------------------------------------------------
    Added Sudo Command "/opt/third-party-app/bin/report"
    ----------------------------------------------------
      Sudo Command: /opt/third-party-app/bin/report
    ```

3.  Create a `sudo`{.literal} rule named `run_third-party-app_report`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudorule-add run_third-party-app_report
    --------------------------------------------
    Added Sudo Rule "run_third-party-app_report"
    --------------------------------------------
      Rule name: run_third-party-app_report
      Enabled: TRUE
    ```

4.  Use the `--users=`{.literal}*`<user>`{.literal}* option to specify the RunAs user for the `sudorule-add-runasuser`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudorule-add-runasuser run_third-party-app_report --users=thirdpartyapp
      Rule name: run_third-party-app_report
      Enabled: TRUE
      RunAs External User: thirdpartyapp
    -------------------------
    Number of members added 1
    -------------------------
    ```

    The user (or group specified with the `--groups=*`{.literal} option) can be external to IdM, such as a local service account or an Active Directory user. Do not add a `%`{.literal} prefix for group names.

5.  Add the `/opt/third-party-app/bin/report`{.literal} command to the `run_third-party-app_report`{.literal} rule:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudorule-add-allow-command run_third-party-app_report --sudocmds '/opt/third-party-app/bin/report'
    Rule name: run_third-party-app_report
    Enabled: TRUE
    Sudo Allow Commands: /opt/third-party-app/bin/report
    RunAs External User: thirdpartyapp
    -------------------------
    Number of members added 1
    -------------------------
    ```

6.  Apply the `run_third-party-app_report`{.literal} rule to the IdM `idmclient`{.literal} host:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudorule-add-host run_third-party-app_report --hosts idmclient.idm.example.com
    Rule name: run_third-party-app_report
    Enabled: TRUE
    Hosts: idmclient.idm.example.com
    Sudo Allow Commands: /opt/third-party-app/bin/report
    RunAs External User: thirdpartyapp
    -------------------------
    Number of members added 1
    -------------------------
    ```

7.  Add the `idm_user`{.literal} account to the `run_third-party-app_report`{.literal} rule:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ipa sudorule-add-user run_third-party-app_report --users idm_user
    Rule name: run_third-party-app_report
    Enabled: TRUE
    Users: idm_user
    Hosts: idmclient.idm.example.com
    Sudo Allow Commands: /opt/third-party-app/bin/report
    RunAs External User: thirdpartyapp
    -------------------------
    Number of members added 1
    ```

    Note

    Propagating the changes from the server to the client can take a few minutes.

**Verification**

1.  Log in to the `idmclient`{.literal} host as the `idm_user`{.literal} account.

2.  Test the new sudo rule:

    a.  Display which `sudo`{.literal} rules the `idm_user`{.literal} account is allowed to perform.

        ``` {.language-plaintext tabindex="-1"}
        [idm_user@idmclient ~]$ sudo -l
        Matching Defaults entries for idm_user@idm.example.com on idmclient:
            !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin,
            env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
            env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE",
            env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES",
            env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE",
            env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY KRB5CCNAME",
            secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

        User idm_user@idm.example.com may run the following commands on idmclient:
            (thirdpartyapp) /opt/third-party-app/bin/report
        ```

    b.  Run the `report`{.literal} command as the `thirdpartyapp`{.literal} service account.

        ``` {.language-plaintext tabindex="-1"}
        [idm_user@idmclient ~]$ sudo -u thirdpartyapp /opt/third-party-app/bin/report
        [sudo] password for idm_user@idm.example.com:
        Executing report...
        Report successful.
        ```

### [9.6. Creating a sudo rule in the IdM WebUI that runs a command as a service account on an IdM client](#creating-a-sudo-rule-in-the-idm-webui-that-runs-a-command-as-a-service-account-on-an-idm-client) {#creating-a-sudo-rule-in-the-idm-webui-that-runs-a-command-as-a-service-account-on-an-idm-client .title}

Create `sudo`{.literal} rules with *RunAs aliases* using the Identity Management (IdM) WebUI to authorize users to run commands as service accounts. You can use *RunAs* functionality to separate administrative privileges from service accounts while maintaining auditability for application administration tasks.

For example, you might have an IdM client that hosts a database application, and you need to run commands as the local service account that corresponds to that application.

Use this example to create a `sudo`{.literal} rule in the IdM WebUI called `run_third-party-app_report`{.literal} to allow the `idm_user`{.literal} account to run the `/opt/third-party-app/bin/report`{.literal} command as the `thirdpartyapp`{.literal} service account on the `idmclient`{.literal} host.

**Prerequisites**

-   You are logged in as IdM administrator.
-   You have created a user account for `idm_user`{.literal} in IdM and unlocked the account by creating a password for the user. For details on adding a new IdM user using the CLI, see [Adding users using the command line](#adding-users-using-the-command-line "1.2. Adding users using the command line").
-   No local `idm_user`{.literal} account is present on the `idmclient`{.literal} host. The `idm_user`{.literal} user is not listed in the local `/etc/passwd`{.literal} file.
-   You have a custom application named `third-party-app`{.literal} installed on the `idmclient`{.literal} host.
-   The `report`{.literal} command for the `third-party-app`{.literal} application is installed in the `/opt/third-party-app/bin/report`{.literal} directory.
-   You have created a local service account named `thirdpartyapp`{.literal} to run commands for the `third-party-app`{.literal} application.

**Procedure**

1.  Add the `/opt/third-party-app/bin/report`{.literal} command to the IdM database of `sudo`{.literal} commands:

    a.  Navigate to **Policy** → **Sudo** → **Sudo Commands**.

    b.  Click **Add** in the upper right corner to open the **Add sudo command** dialog box.

    c.  Enter the command: `/opt/third-party-app/bin/report`{.literal}.

    d.  Click **Add**.

2.  Use the new `sudo`{.literal} command entry to create the new `sudo`{.literal} rule:

    a.  Navigate to **Policy** → **Sudo** → **Sudo rules**.

    b.  Click **Add** in the upper right corner to open the **Add sudo rule** dialog box.

    c.  Enter the name of the `sudo`{.literal} rule: **run_third-party-app_report**.

    d.  Click **Add and Edit**.

    e.  Specify the user:

        i.  In the **Who** section, check the **Specified Users and Groups** radio button.

        ii. In the **User category the rule applies to** subsection, click **Add** to open the **Add users into sudo rule \"run_third-party-app_report\"** dialog box.

        iii. In the **Add users into sudo rule \"run_third-party-app_report\"** dialog box in the **Available** column, check the **idm_user** checkbox, and move it to the **Prospective** column.

        iv. Click **Add**.

    f.  Specify the host:

        i.  In the **Access this host** section, check the **Specified Hosts and Groups** radio button.

        ii. In the **Host category this rule applies to** subsection, click **Add** to open the **Add hosts into sudo rule \"run_third-party-app_report\"** dialog box.

        iii. In the **Add hosts into sudo rule \"run_third-party-app_report\"** dialog box in the **Available** column, check the **idmclient.idm.example.com** checkbox, and move it to the **Prospective** column.

        iv. Click **Add**.

    g.  Specify the commands:

        i.  In the **Command category the rule applies to** subsection of the **Run Commands** section, check the **Specified Commands and Groups** radio button.

        ii. In the **Sudo Allow Commands** subsection, click **Add** to open the **Add allow sudo commands into sudo rule \"run_third-party-app_report\"** dialog box.

        iii. In the **Add allow sudo commands into sudo rule \"run_third-party-app_report\"** dialog box in the **Available** column, check the `/opt/third-party-app/bin/report`{.literal} checkbox, and move it to the **Prospective** column.

        iv. Click **Add** to return to the **run_third-party-app_report** page.

    h.  Specify the RunAs user:

        i.  In the **As Whom** section, check the **Specified Users and Groups** radio button.

        ii. In the **RunAs Users** subsection, click **Add** to open the **Add RunAs users into sudo rule \"run_third-party-app_report\"** dialog box.

        iii. In the **Add RunAs users into sudo rule \"run_third-party-app_report\"** dialog box, enter the `thirdpartyapp`{.literal} service account in the **External** box and move it to the **Prospective** column.

        iv. Click **Add** to return to the **run_third-party-app_report** page.

    i.  Click **Save** in the top left corner.

        The new rule is enabled by default.

        **The following image shows the details of a sudo rule created in the IdM Web UI:**

    Note

    Propagating the changes from the server to the client can take a few minutes.

**Verification**

1.  Log in to the `idmclient`{.literal} host as the `idm_user`{.literal} account.

2.  Test the new sudo rule:

    a.  Display which `sudo`{.literal} rules the `idm_user`{.literal} account is allowed to perform.

        ``` {.language-plaintext tabindex="-1"}
        [idm_user@idmclient ~]$ sudo -l
        Matching Defaults entries for idm_user@idm.example.com on idmclient:
            !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin,
            env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
            env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE",
            env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES",
            env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE",
            env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY KRB5CCNAME",
            secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

        User idm_user@idm.example.com may run the following commands on idmclient:
            (thirdpartyapp) /opt/third-party-app/bin/report
        ```

    b.  Run the `report`{.literal} command as the `thirdpartyapp`{.literal} service account.

        ``` {.language-plaintext tabindex="-1"}
        [idm_user@idmclient ~]$ sudo -u thirdpartyapp /opt/third-party-app/bin/report
        [sudo] password for idm_user@idm.example.com:
        Executing report...
        Report successful.
        ```

### [9.7. Enabling GSSAPI authentication for sudo on an IdM client](#enabling-gssapi-authentication-for-sudo-on-an-idm-client) {#enabling-gssapi-authentication-for-sudo-on-an-idm-client .title}

Enable Generic Security Service Application Program Interface (GSSAPI) authentication on an Identity Management (IdM) client for the `sudo`{.literal} and `sudo -i`{.literal} commands using the `pam_sss_gss.so`{.literal} PAM module. With this configuration, IdM users can authenticate to the `sudo`{.literal} command with their Kerberos ticket.

**Prerequisites**

-   You have created a `sudo`{.literal} rule for an IdM user that applies to an IdM host. For this example, you have created the `idm_user_reboot`{.literal} `sudo`{.literal} rule to grant the `idm_user`{.literal} account the permission to run the `/usr/sbin/reboot`{.literal} command on the `idmclient`{.literal} host.
-   You need `root`{.literal} privileges to modify the `/etc/sssd/sssd.conf`{.literal} file and PAM files in the `/etc/pam.d/`{.literal} directory.

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} configuration file.

2.  Add the following entry to the `[domain/`{.literal}*`<domain_name>`{.literal}*`]`{.literal} section.

    ``` {.language-plaintext tabindex="-1"}
    [domain/<domain_name>]
    pam_gssapi_services = sudo, sudo-i
    ```

3.  Save and close the `/etc/sssd/sssd.conf`{.literal} file.

4.  Restart the SSSD service to load the configuration changes.

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# systemctl restart sssd
    ```

5.  Optional: Determine if you have selected the `sssd`{.literal} `authselect`{.literal} profile:

    ``` {.language-plaintext tabindex="-1"}
    # authselect current
    Profile ID: sssd
    ```

6.  If the `sssd`{.literal} `authselect`{.literal} profile is selected, enable GSSAPI authentication:

    ``` {.language-plaintext tabindex="-1"}
    # authselect enable-feature with-gssapi
    ```

7.  If the `sssd`{.literal} `authselect`{.literal} profile is not selected, select it and enable GSSAPI authentication:

    ``` {.language-plaintext tabindex="-1"}
    # authselect select sssd with-gssapi
    ```

**Verification**

1.  Log into the host as the `idm_user`{.literal} account.

    ``` {.language-plaintext tabindex="-1"}
    [root@idm-client ~]# ssh -l idm_user@idm.example.com localhost
    idm_user@idm.example.com's password:
    ```

2.  Verify that you have a ticket-granting ticket as the `idm_user`{.literal} account.

    ``` {.language-plaintext tabindex="-1"}
    [idmuser@idmclient ~]$ klist
    Ticket cache: KCM:1366201107
    Default principal: idm_user@IDM.EXAMPLE.COM

    Valid starting       Expires              Service principal
    01/08/2021 09:11:48  01/08/2021 19:11:48  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
        renew until 01/15/2021 09:11:44
    ```

3.  Optional: If you do not have Kerberos credentials for the `idm_user`{.literal} account, delete your current Kerberos credentials and request the correct ones.

    ``` {.language-plaintext tabindex="-1"}
    [idm_user@idmclient ~]$ kdestroy -A

    [idm_user@idmclient ~]$ kinit idm_user@IDM.EXAMPLE.COM
    Password for idm_user@idm.example.com:
    ```

4.  Reboot the machine using `sudo`{.literal}, without specifying a password.

    ``` {.language-plaintext tabindex="-1"}
    [idm_user@idmclient ~]$ sudo /usr/sbin/reboot
    ```

**Additional resources**

-   [IdM terminology](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/overview-of-idm-and-access-control-in-rhel#idm-terminology)
-   [Granting sudo access to an IdM user on an IdM client using IdM Web UI](#granting-sudo-access-to-an-idm-user-on-an-idm-client-using-the-idm-web-ui "9.4. Granting sudo access to an IdM user on an IdM client using the IdM Web UI")
-   [Granting sudo access to an IdM user on an IdM client using the CLI](#granting-sudo-access-to-an-idm-user-on-an-idm-client-using-the-cli "9.2. Granting sudo access to an IdM user on an IdM client using the CLI")

### [9.8. Enabling GSSAPI authentication and enforcing Kerberos authentication indicators for sudo on an IdM client](#enabling-gssapi-authentication-and-enforcing-kerberos-authentication-indicators-for-sudo-on-an-idm-client) {#enabling-gssapi-authentication-and-enforcing-kerberos-authentication-indicators-for-sudo-on-an-idm-client .title}

Enable GSSAPI authentication and enforce authentication indicator requirements for `sudo`{.literal} on Identity Management (IdM) clients to strengthen privilege escalation security.

You can enable GSSAPI authentication on an Identity Management (IdM) client for PAM-enabled services such as `sudo`{.literal} and `sudo -i`{.literal} using the `pam_sss_gss.so`{.literal} PAM module. Additionally, you can enable only users who have logged in with a smart card to authenticate to those services with their Kerberos ticket.

Note

You can use this procedure as a template to configure GSSAPI authentication with SSSD for other PAM-aware services, and further restrict access to only those users that have a specific authentication indicator attached to their Kerberos ticket.

However, using authentication indicators to restrict access has currently two limitations:

-   Only deployments based on MIT Kerberos support authentication indicators. These deployments include, for example, RHEL IdM, FreeIPA in Fedora, and Samba AD DC in Fedora.
-   Authentication indicators are removed from Kerberos tickets at the realm boundary.

Therefore, if you, for example, want to restrict `sudo`{.literal} access by using `pam_gssapi_indicators_map = sudo:pkinit`{.literal}, you can only apply this restriction to users stored in IdM LDAP. Tickets issued to users stored elsewhere, such as those stored in Active Directory, currently cannot satisfy the `pam_gssapi_indicators_map = sudo:pkinit`{.literal} condition.

**Prerequisites**

-   You have created a `sudo`{.literal} rule for an IdM user that applies to an IdM host. For this example, you have created the `idm_user_reboot`{.literal} `sudo`{.literal} rule to grant the `idm_user`{.literal} account the permission to run the `/usr/sbin/reboot`{.literal} command on the `idmclient`{.literal} host.
-   You have configured smart card authentication for the `idmclient`{.literal} host.
-   You need `root`{.literal} privileges to modify the `/etc/sssd/sssd.conf`{.literal} file and PAM files in the `/etc/pam.d/`{.literal} directory.

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} configuration file.

2.  Add the following entries to the `[domain/`{.literal}*`<domain_name>`{.literal}*`]`{.literal} section.

    ``` {.language-plaintext tabindex="-1"}
    [domain/<domain_name>]
    pam_gssapi_services = sudo, sudo-i
    pam_gssapi_indicators_map = sudo:pkinit, sudo-i:pkinit
    ```

3.  Save and close the `/etc/sssd/sssd.conf`{.literal} file.

4.  Restart the SSSD service to load the configuration changes.

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# systemctl restart sssd
    ```

5.  Determine if you have selected the `sssd`{.literal} `authselect`{.literal} profile:

    ``` {.language-plaintext tabindex="-1"}
    # authselect current
    Profile ID: sssd
    ```

6.  Optional: Select the `sssd`{.literal} `authselect`{.literal} profile:

    ``` {.language-plaintext tabindex="-1"}
    # authselect select sssd
    ```

7.  Enable GSSAPI authentication:

    ``` {.language-plaintext tabindex="-1"}
    # authselect enable-feature with-gssapi
    ```

8.  Configure the system to authenticate only users with smart cards:

    ``` {.language-plaintext tabindex="-1"}
    # authselect with-smartcard-required
    ```

**Verification**

1.  Log into the host as the `idm_user`{.literal} account and authenticate with a smart card.

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient ~]# ssh -l idm_user@idm.example.com localhost
    PIN for smart_card
    ```

2.  Verify that you have a ticket-granting ticket as the smart card user.

    ``` {.language-plaintext tabindex="-1"}
    [idm_user@idmclient ~]$ klist
    Ticket cache: KEYRING:persistent:1358900015:krb_cache_TObtNMd
    Default principal: idm_user@IDM.EXAMPLE.COM

    Valid starting       Expires              Service principal
    02/15/2021 16:29:48  02/16/2021 02:29:48  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
        renew until 02/22/2021 16:29:44
    ```

3.  Display which `sudo`{.literal} rules the `idm_user`{.literal} account is allowed to perform.

    ``` {.language-plaintext tabindex="-1"}
    [idm_user@idmclient ~]$ sudo -l
    Matching Defaults entries for idmuser on idmclient:
        !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin,
        env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
        env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE",
        env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES",
        env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE",
        env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY KRB5CCNAME",
        secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

    User idm_user may run the following commands on idmclient:
        (root) /usr/sbin/reboot
    ```

4.  Reboot the machine using `sudo`{.literal}, without specifying a password.

    ``` {.language-plaintext tabindex="-1"}
    [idm_user@idmclient ~]$ sudo /usr/sbin/reboot
    ```

**Additional resources**

-   [Kerberos authentication indicators](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-kerberos-ticket-policies#kerberos-authentication-indicators)
-   [SSSD options controlling GSSAPI authentication for PAM services](#sssd-options-controlling-gssapi-authentication-for-pam-services "9.9. SSSD options controlling GSSAPI authentication for PAM services")
-   [IdM terminology](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/overview-of-idm-and-access-control-in-rhel#idm-terminology)
-   [Configuring Identity Management for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication)
-   [Kerberos authentication indicators](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-kerberos-ticket-policies#kerberos-authentication-indicators)
-   [Granting sudo access to an IdM user on an IdM client using IdM Web UI](#granting-sudo-access-to-an-idm-user-on-an-idm-client-using-the-idm-web-ui "9.4. Granting sudo access to an IdM user on an IdM client using the IdM Web UI")
-   [Granting sudo access to an IdM user on an IdM client using the CLI](#granting-sudo-access-to-an-idm-user-on-an-idm-client-using-the-cli "9.2. Granting sudo access to an IdM user on an IdM client using the CLI")

### [9.9. SSSD options controlling GSSAPI authentication for PAM services](#sssd-options-controlling-gssapi-authentication-for-pam-services) {#sssd-options-controlling-gssapi-authentication-for-pam-services .title}

Configure GSSAPI authentication for PAM services in Identity Management (IdM) using SSSD options to control which services can use Kerberos tickets and what authentication methods are required.

pam_gssapi_services
:   GSSAPI authentication with SSSD is disabled by default. You can use this option to specify a comma-separated list of PAM services that are allowed to try GSSAPI authentication using the `pam_sss_gss.so`{.literal} PAM module. To explicitly disable GSSAPI authentication, set this option to `-`{.literal}.

pam_gssapi_indicators_map

:   This option only applies to Identity Management (IdM) domains. Use this option to list Kerberos authentication indicators that are required to grant PAM access to a service. Pairs must be in the format *`<PAM_service>`{.literal}*`:_<required_authentication_indicator>_`{.literal}.

    Valid authentication indicators are:

    -   `otp`{.literal} for two-factor authentication
    -   `radius`{.literal} for RADIUS authentication
    -   `pkinit`{.literal} for PKINIT, smart card, or certificate authentication
    -   `hardened`{.literal} for hardened passwords

pam_gssapi_check_upn
:   This option is enabled and set to `true`{.literal} by default. If this option is enabled, the SSSD service requires that the user name matches the Kerberos credentials. If `false`{.literal}, the `pam_sss_gss.so`{.literal} PAM module authenticates every user that is able to obtain the required service ticket.

#### [9.9.1. SSSD GSSAPI configuration examples](#sssd_gssapi_configuration_examples) {#sssd-gssapi-configuration-examples .title}

The following options enable Kerberos authentication for the `sudo`{.literal} and `sudo-i`{.literal} services, requires that `sudo`{.literal} users authenticated with a one-time password, and user names must match the Kerberos principal. Because these settings are in the `[pam]`{.literal} section, they apply to all domains:

``` {.language-plaintext tabindex="-1"}
[pam]
pam_gssapi_services = sudo, sudo-i
pam_gssapi_indicators_map = sudo:otp
pam_gssapi_check_upn = true
```

You can also set these options in individual `[domain]`{.literal} sections to overwrite any global values in the `[pam]`{.literal} section. The following options apply different GSSAPI settings to each domain:

For the `idm.example.com`{.literal} domain

:   -   Enable GSSAPI authentication for the `sudo`{.literal} and `sudo -i`{.literal} services.
    -   Require certificate or smart card authentication authenticators for the `sudo`{.literal} command.
    -   Require one-time password authentication authenticators for the `sudo -i`{.literal} command.
    -   Enforce matching user names and Kerberos principals.

For the `ad.example.com`{.literal} domain

:   -   Enable GSSAPI authentication only for the `sudo`{.literal} service.
    -   Do not enforce matching user names and principals.

``` {.language-plaintext tabindex="-1"}
[domain/idm.example.com]
pam_gssapi_services = sudo, sudo-i
pam_gssapi_indicators_map = sudo:pkinit, sudo-i:otp
pam_gssapi_check_upn = true
...

[domain/ad.example.com]
pam_gssapi_services = sudo
pam_gssapi_check_upn = false
...
```

**Additional resources**

-   [Kerberos authentication indicators](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-kerberos-ticket-policies#kerberos-authentication-indicators)

### [9.10. Troubleshooting GSSAPI authentication for sudo](#troubleshooting-gssapi-authentication-for-sudo) {#troubleshooting-gssapi-authentication-for-sudo .title}

Troubleshoot Identity Management (IdM) GSSAPI authentication failures for `sudo`{.literal} to resolve Kerberos credential, realm resolution, and UPN mismatch issues that prevent Kerberos-based `sudo`{.literal} access.

**Prerequisites**

-   You have enabled GSSAPI authentication for the `sudo`{.literal} service. See [Enabling GSSAPI authentication for sudo on an IdM client](#enabling-gssapi-authentication-for-sudo-on-an-idm-client "9.7. Enabling GSSAPI authentication for sudo on an IdM client").
-   You need `root`{.literal} privileges to modify the `/etc/sssd/sssd.conf`{.literal} file and PAM files in the `/etc/pam.d/`{.literal} directory.

**Procedure**

-   If you see the following error, the Kerberos service might not able to resolve the correct realm for the service ticket based on the host name:

    ``` {.language-plaintext tabindex="-1"}
    Server not found in Kerberos database
    ```

    In this situation, add the hostname directly to `[domain_realm]`{.literal} section in the `/etc/krb5.conf`{.literal} Kerberos configuration file:

    ``` {.language-plaintext tabindex="-1"}
    [idm-user@idm-client ~]$ cat /etc/krb5.conf
    ...

    [domain_realm]
     .example.com = EXAMPLE.COM
     example.com = EXAMPLE.COM
     server.example.com = EXAMPLE.COM
    ```

-   If you see the following error, you do not have any Kerberos credentials:

    ``` {.language-plaintext tabindex="-1"}
    No Kerberos credentials available
    ```

    In this situation, retrieve Kerberos credentials with the `kinit`{.literal} utility or authenticate with SSSD:

    ``` {.language-plaintext tabindex="-1"}
    [idm-user@idm-client ~]$ kinit idm-user@IDM.EXAMPLE.COM
    Password for idm-user@idm.example.com:
    ```

-   If you see either of the following errors in the `/var/log/sssd/sssd_pam.log`{.literal} log file, the Kerberos credentials do not match the username of the user currently logged in:

    ``` {.language-plaintext tabindex="-1"}
    User with UPN [<UPN>] was not found.

    UPN [<UPN>] does not match target user [<username>].
    ```

    In this situation, verify that you authenticated with SSSD, or consider disabling the `pam_gssapi_check_upn`{.literal} option in the `/etc/sssd/sssd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [idm-user@idm-client ~]$ cat /etc/sssd/sssd.conf
    ...

    pam_gssapi_check_upn = false
    ```

-   For additional troubleshooting, you can enable debugging output for the `pam_sss_gss.so`{.literal} PAM module.

    -   Add the `debug`{.literal} option at the end of all `pam_sss_gss.so`{.literal} entries in PAM files, such as `/etc/pam.d/sudo`{.literal} and `/etc/pam.d/sudo-i`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [root@idm-client ~]# cat /etc/pam.d/sudo
        #%PAM-1.0
        auth       sufficient   pam_sss_gss.so   debug
        auth       include      system-auth
        account    include      system-auth
        password   include      system-auth
        session    include      system-auth
        ```

        ``` {.language-plaintext tabindex="-1"}
        [root@idm-client ~]# cat /etc/pam.d/sudo-i
        #%PAM-1.0
        auth       sufficient   pam_sss_gss.so   debug
        auth       include      sudo
        account    include      sudo
        password   include      sudo
        session    optional     pam_keyinit.so force revoke
        session    include      sudo
        ```

    -   Try to authenticate with the `pam_sss_gss.so`{.literal} module and review the console output. In this example, the user did not have any Kerberos credentials.

        ``` {.language-plaintext tabindex="-1"}
        [idm-user@idm-client ~]$ sudo ls -l /etc/sssd/sssd.conf
        pam_sss_gss: Initializing GSSAPI authentication with SSSD
        pam_sss_gss: Switching euid from 0 to 1366201107
        pam_sss_gss: Trying to establish security context
        pam_sss_gss: SSSD User name: idm-user@idm.example.com
        pam_sss_gss: User domain: idm.example.com
        pam_sss_gss: User principal:
        pam_sss_gss: Target name: host@idm.example.com
        pam_sss_gss: Using ccache: KCM:
        pam_sss_gss: Acquiring credentials, principal name will be derived
        pam_sss_gss: Unable to read credentials from [KCM:] [maj:0xd0000, min:0x96c73ac3]
        pam_sss_gss: GSSAPI: Unspecified GSS failure.  Minor code may provide more information
        pam_sss_gss: GSSAPI: No credentials cache found
        pam_sss_gss: Switching euid from 1366200907 to 0
        pam_sss_gss: System error [5]: Input/output error
        ```

### [9.11. Additional resources](#granting-sudo-access-to-an-idm-user-on-an-idm-client_911-additional-resources) {#additional-resources-3 .title}

-   [Using an Ansible playbook to ensure sudo access for an IdM user on an IdM client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/managing-sudo-access-using-an-ansible-playbook#using-an-ansible-playbook-to-ensure-sudo-access-for-an-idm-user-on-an-idm-client)
-   [Managing multiple IdM sudo rules in a single Ansible task](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/managing-sudo-access-using-an-ansible-playbook#managing-multiple-idm-sudo-rules-in-a-single-ansible-task)

## [Chapter 10. Using ldapmodify to manage IdM users externally](#using-ldapmodify-to-manage-idm-users-externally) {#chapter-10.-using-ldapmodify-to-manage-idm-users-externally .title}

You can use the `ldapmodify`{.literal} command to manage Identity Management (IdM) user and group entries as an alternative to the `ipa`{.literal} command-line utilities. The `ldapmodify`{.literal} command supports both interactive input and LDIF files for bulk operations.

### [10.1. Templates for managing IdM user accounts externally](#templates-for-managing-idm-user-accounts-externally) {#templates-for-managing-idm-user-accounts-externally .title}

Use LDIF templates with `ldapmodify`{.literal} to manage Identity Management (IdM) user accounts from an external provisioning system, enabling automated user creation, modification, enabling, disabling, and preservation.

Update specific LDAP attributes with the `ldapmodify`{.literal} utility to manage user accounts and states. Use the provided syntax to perform the following administrative tasks:

-   Adding a new stage user
-   Modifying a user's attribute
-   Enabling a user
-   Disabling a user
-   Preserving a user

The templates are formatted in the LDAP Data Interchange Format (LDIF). LDIF is a standard plain text data interchange format for representing LDAP directory content and update requests.

Using the templates, you can configure the LDAP provider of your provisioning system to manage IdM user accounts.

Templates for adding a new stage user

:   A template for adding a user with **UID and GID assigned automatically**. The distinguished name (DN) of the created entry must start with `uid=user_login`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    dn: uid=user_login,cn=staged users,cn=accounts,cn=provisioning,dc=idm,dc=example,dc=com
    changetype: add
    objectClass: top
    objectClass: inetorgperson
    uid: user_login
    sn: surname
    givenName: first_name
    cn: full_name
    ```

    A template for adding a user with **UID and GID assigned statically**:

    ``` {.language-plaintext tabindex="-1"}
    dn: uid=user_login,cn=staged users,cn=accounts,cn=provisioning,dc=idm,dc=example,dc=com
    changetype: add
    objectClass: top
    objectClass: person
    objectClass: inetorgperson
    objectClass: organizationalperson
    objectClass: posixaccount
    uid: user_login
    uidNumber: UID_number
    gidNumber: GID_number
    sn: surname
    givenName: first_name
    cn: full_name
    homeDirectory: /home/user_login
    ```

    You are not required to specify any IdM object classes when adding stage users. IdM adds these classes automatically after the users are activated.

Templates for modifying existing users

:   -   Modifying a user's attribute:

    ``` {.language-plaintext tabindex="-1"}
    dn: distinguished_name
    changetype: modify
    replace: attribute_to_modify
    attribute_to_modify: new_value
    ```

    -   Disabling a user:

        ``` {.language-plaintext tabindex="-1"}
        dn: distinguished_name
        changetype: modify
        replace: nsAccountLock
        nsAccountLock: TRUE
        ```

    -   Enabling a user:

        ``` {.language-plaintext tabindex="-1"}
        dn: distinguished_name
        changetype: modify
        replace: nsAccountLock
        nsAccountLock: FALSE
        ```

    Updating the `nssAccountLock`{.literal} attribute has no effect on stage and preserved users. Even though the update operation completes successfully, the attribute value remains `nssAccountLock: TRUE`{.literal}.

    -   Preserving a user:

        ``` {.language-plaintext tabindex="-1"}
        dn: distinguished_name
        changetype: modrdn
        newrdn: uid=user_login
        deleteoldrdn: 0
        newsuperior: cn=deleted users,cn=accounts,cn=provisioning,dc=idm,dc=example,dc=com
        ```

Note

Before modifying a user, obtain the user's distinguished name (DN) by searching using the user's login. In the following example, the *user_allowed_to_modify_user_entries* user is a user allowed to modify user and group information, for example **activator** or IdM administrator. The password in the example is this user's password:

``` {.language-plaintext tabindex="-1"}
# ldapsearch -LLL -x -D "uid=user_allowed_to_modify_user_entries,cn=users,cn=accounts,dc=idm,dc=example,dc=com" -w "Secret123" -H ldap://server.idm.example.com -b "cn=users,cn=accounts,dc=idm,dc=example,dc=com" uid=test_user
dn: uid=test_user,cn=users,cn=accounts,dc=idm,dc=example,dc=com
memberOf: cn=ipausers,cn=groups,cn=accounts,dc=idm,dc=example,dc=com
```

**Additional resources**

-   [Adding an IdM stage user defined in an LDIF file](#adding-an-idm-stage-user-defined-in-an-ldif-file "12.3. Adding an IdM stage user defined in an LDIF file")
-   [Adding an IdM stage user directly from the CLI using ldapmodify](#adding-an-idm-stage-user-directly-from-the-cli-using-ldapmodify "12.4. Adding an IdM stage user directly from the CLI using ldapmodify")
-   [Preserving an IdM user with ldapmodify](#preserving-an-idm-user-with-ldapmodify "10.4. Preserving an IdM user with ldapmodify")

### [10.2. Templates for managing IdM group accounts externally](#templates-for-managing-idm-group-accounts-externally) {#templates-for-managing-idm-group-accounts-externally .title}

Use LDAP Data Interchange Format (LDIF) templates with `ldapmodify`{.literal} to manage Identity Management (IdM) user group accounts from an external provisioning system, enabling automated group creation, member management, and deletion.

Modify specific LDAP attributes using the `ldapmodify`{.literal} utility to manage group configurations. Use the provided syntax to perform the following administrative tasks:

-   Creating a new group
-   Deleting an existing group
-   Adding a member to a group
-   Removing a member from a group

The templates are formatted in LDIF, a standard plain text data interchange format for representing LDAP directory content and update requests.

Using the templates, you can configure the LDAP provider of your provisioning system to manage IdM group accounts.

Creating a new group

:   

``` {.language-plaintext tabindex="-1"}
dn: cn=group_name,cn=groups,cn=accounts,dc=idm,dc=example,dc=com
changetype: add
objectClass: top
objectClass: ipaobject
objectClass: ipausergroup
objectClass: groupofnames
objectClass: nestedgroup
objectClass: posixgroup
uid: group_name
cn: group_name
gidNumber: GID_number
```

Modifying groups

:   -   **Deleting an existing group**:

    ``` {.language-plaintext tabindex="-1"}
    dn: group_distinguished_name
    changetype: delete
    ```

    -   **Adding a member to a group**:

        ``` {.language-plaintext tabindex="-1"}
        dn: group_distinguished_name
        changetype: modify
        add: member
        member: uid=user_login,cn=users,cn=accounts,dc=idm,dc=example,dc=com
        ```

        Do not add stage or preserved users to groups. Even though the update operation completes successfully, the users will not be updated as members of the group. Only active users can belong to groups.

    -   **Removing a member from a group**:

    ``` {.language-plaintext tabindex="-1"}
    dn: distinguished_name
    changetype: modify
    delete: member
    member: uid=user_login,cn=users,cn=accounts,dc=idm,dc=example,dc=com
    ```

Note

Before modifying a group, obtain the group's distinguished name (DN) by searching using the group's name.

``` {.language-plaintext tabindex="-1"}
# ldapsearch -YGSSAPI -H ldap://<server.idm.example.com> -b "<cn=groups,cn=accounts,dc=idm,dc=example,dc=com>" "cn=<group_name>"
dn: cn=group_name,cn=groups,cn=accounts,dc=idm,dc=example,dc=com
ipaNTSecurityIdentifier: S-1-5-21-1650388524-2605035987-2578146103-11017
cn: testgroup
objectClass: top
objectClass: groupofnames
objectClass: nestedgroup
objectClass: ipausergroup
objectClass: ipaobject
objectClass: posixgroup
objectClass: ipantgroupattrs
ipaUniqueID: 569bf864-9d45-11ea-bea3-525400f6f085
gidNumber: 1997010017
```

### [10.3. Using ldapmodify command interactively](#using-ldapmodify-command-interactively) {#using-ldapmodify-command-interactively .title}

Modify LDAP entries in Identity Management (IdM) interactively using `ldapmodify`{.literal} by entering LDIF statements directly in the terminal or by loading them from a file.

**Procedure**

1.  In a command line, enter the LDAP Data Interchange Format (LDIF) statement after the `ldapmodify`{.literal} command.

    For example, to change the telephone number for a *`<testuser>`{.literal}*:

    ``` {.language-plaintext tabindex="-1"}
    # ldapmodify -Y GSSAPI -H ldap://<server.example.com>
    dn: uid=testuser,cn=users,cn=accounts,dc=example,dc=com
    changetype: modify
    replace: telephoneNumber
    telephonenumber: 88888888
    ```

    Note that you need to obtain a Kerberos ticket for using `-Y`{.literal} option.

2.  Press `Ctlr+D`{.literal} to exit the interactive mode.

3.  Alternatively, provide an LDIF file after `ldapmodify`{.literal} command:

    The `ldapmodify`{.literal} command reads modification data from an LDIF file

    ``` {.language-plaintext tabindex="-1"}
    # ldapmodify -Y GSSAPI -H ldap://<server.example.com> -f ~/example.ldif
    ```

### [10.4. Preserving an IdM user with ldapmodify](#preserving-an-idm-user-with-ldapmodify) {#preserving-an-idm-user-with-ldapmodify .title}

Deactivate Identity Management (IdM) user accounts using `ldapmodify`{.literal} to preserve user data when employees leave your organization. Preserved users retain their information for auditing while preventing authentication.

**Prerequisites**

-   You can authenticate as an IdM user with a role to preserve users.

**Procedure**

1.  Log in as an IdM user with a role to preserve users:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit admin
    ```

2.  Enter the `ldapmodify`{.literal} command and specify the Generic Security Services API (GSSAPI) as the Simple Authentication and Security Layer (SASL) mechanism to be used for authentication:

    ``` {.language-plaintext tabindex="-1"}
    # ldapmodify -Y GSSAPI
    SASL/GSSAPI authentication started
    SASL username: admin@IDM.EXAMPLE.COM
    SASL SSF: 256
    SASL data security layer installed.
    ```

3.  Enter the `dn`{.literal} of the user you want to preserve:

    ``` {.language-plaintext tabindex="-1"}
    dn: uid=user1,cn=users,cn=accounts,dc=idm,dc=example,dc=com
    ```

4.  Enter **modrdn** as the type of change you want to perform:

    ``` {.language-plaintext tabindex="-1"}
    changetype: modrdn
    ```

5.  Specify the **newrdn** for the user:

    ``` {.language-plaintext tabindex="-1"}
    newrdn: uid=user1
    ```

6.  Indicate that you want to preserve the user:

    ``` {.language-plaintext tabindex="-1"}
    deleteoldrdn: 0
    ```

7.  Specify the **new superior DN**:

    ``` {.language-plaintext tabindex="-1"}
    newsuperior: cn=deleted users,cn=accounts,cn=provisioning,dc=idm,dc=example,dc=com
    ```

    Preserving a user moves the entry to a new location in the directory information tree (DIT). For this reason, you must specify the DN of the new parent entry as the new superior DN.

8.  Press `Enter`{.literal} again to confirm that this is the end of the entry:

    ``` {.language-plaintext tabindex="-1"}
    [Enter]

    modifying rdn of entry "uid=user1,cn=users,cn=accounts,dc=idm,dc=example,dc=com"
    ```

9.  Exit the connection using **Ctrl** + **C**.

**Verification**

-   Verify that the user has been preserved by listing all preserved users:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-find --preserved=true
    --------------
    1 user matched
    --------------
      User login: user1
      First name: First 1
      Last name: Last 1
      Home directory: /home/user1
      Login shell: /bin/sh
      Principal name: user1@IDM.EXAMPLE.COM
      Principal alias: user1@IDM.EXAMPLE.COM
      Email address: user1@idm.example.com
      UID: 1997010003
      GID: 1997010003
      Account disabled: True
      Preserved user: True
    ----------------------------
    Number of entries returned 1
    ----------------------------
    ```

## [Chapter 11. Searching IdM entries using the ldapsearch command](#searching-idm-entries-using-the-ldapsearch-command) {#chapter-11.-searching-idm-entries-using-the-ldapsearch-command .title}

Search Identity Management entries using the `ldapsearch`{.literal} command as an alternative to the `ipa find`{.literal} command. The `ldapsearch`{.literal} command provides direct LDAP-level queries with flexible filtering options.

### [11.1. Using the ldapsearch command](#using-the-ldapsearch-command) {#using-the-ldapsearch-command .title}

Use the `ldapsearch`{.literal} command to query LDAP directories in Identity Management (IdM), returning specific attributes and entries based on search filters and authentication options.

The `ldapsearch`{.literal} command has the following format:

``` {.language-plaintext tabindex="-1"}
# ldapsearch [-x | -Y mechanism] [options] [search_filter] [list_of_attributes]
```

-   To configure the authentication method, specify the `-x`{.literal} option to use simple binds or the `-Y`{.literal} option to set the Simple Authentication and Security Layer (SASL) mechanism. Note that you need to obtain a Kerberos ticket if you are using the `-Y GSSAPI`{.literal} option.
-   The *options* are the `ldapsearch`{.literal} command options described in a table below.
-   The *search_filter* is an LDAP search filter.
-   The *list_of_attributes* is a list of the attributes that the search results return.

For example, you want to search all the entries of a base LDAP tree for the user name *user01*:

``` {.language-plaintext tabindex="-1"}
# ldapsearch -x -H ldap://ldap.example.com -s sub "(uid=user01)"
```

-   The `-x`{.literal} option tells the `ldapsearch`{.literal} command to authenticate with the simple bind. Note that if you do not provide the Distinguish Name (DN) with the `-D`{.literal} option, the authentication is anonymous.
-   The `-H`{.literal} option connects you to the *ldap://ldap.example.com*.
-   The `-s sub`{.literal} option tells the `ldapsearch`{.literal} command to search all the entries, starting from the base DN, for the user with the name *user01*. The *\"(uid=user01)\"* is a filter.

Note that if you do not provide the starting point for the search with the `-b`{.literal} option, the command searches in the default tree. It is specified in the BASE parameter of the `etc/openldap/ldap.conf`{.literal} file.

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                            | Description                                                                                                                                                                                                                                                                                           |
+:==================================+:======================================================================================================================================================================================================================================================================================================+
| -b                                | The starting point for the search. If your search parameters contain an asterisk (\*) or other character, that the command line can interpret into a code, you must wrap the value in single or double quotation marks. For example, `-b cn=user,ou=Product Development,dc=example,dc=com`{.literal}. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -D                                | The Distinguished Name (DN) with which you want to authenticate.                                                                                                                                                                                                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -H                                | An LDAP URL to connect to the server. The `-H`{.literal} option replaces the `-h`{.literal} and `-p`{.literal} options.                                                                                                                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -l                                | The time limit in seconds to wait for a search request to complete.                                                                                                                                                                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -s *scope*                        | The scope of the search. You can choose one of the following for the scope:                                                                                                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                                                                                       |
|                                   | -   `base`{.literal} searches only the entry from the `-b`{.literal} option or defined by the `LDAP_BASEDN`{.literal} environment variable.                                                                                                                                                           |
|                                   | -   `one`{.literal} searches only the children of the entry from the `-b`{.literal} option.                                                                                                                                                                                                           |
|                                   | -   `sub`{.literal} a subtree search from the -b option starting point.                                                                                                                                                                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -W                                | Requests for the password.                                                                                                                                                                                                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -x                                | Disables the default SASL connection to allow simple binds.                                                                                                                                                                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -Y *SASL_mechanism*               | Sets the SASL mechanism for the authentication.                                                                                                                                                                                                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -z *number*                       | The maximum number of entries in the search result.                                                                                                                                                                                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 11.1. The ldapsearch command options

Show more

Note, you must specify one of the authentication mechanisms with the `-x`{.literal} or `-Y`{.literal} option with the `ldapsearch`{.literal} command.

### [11.2. Using the ldapsearch filters](#using-the-ldapsearch-filters) {#using-the-ldapsearch-filters .title}

Narrow `ldapsearch`{.literal} results in Identity Management (IdM) using filter operators and boolean expressions to match specific LDAP attributes or combinations of attributes.

For example, you want the search result to contain all the entries with a common names set to *example*:

``` {.language-plaintext tabindex="-1"}
"(cn=example)"
```

In this case, the *equal sign (=)* is the operator, and *example* is the value.

+--------------------------+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Search type              | Operator             | Description                                                                                                                      |
+:=========================+:=====================+:=================================================================================================================================+
| Equality                 | =                    | Returns the entries with the exact match to the value. For example, *cn=example*.                                                |
+--------------------------+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Substring                | *=string\* string*   | Returns all entries with the substring match. For example, *cn=exa\*l*. The asterisk (\*) indicates zero (0) or more characters. |
+--------------------------+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Greater than or equal to | \>=                  | Returns all entries with attributes that are greater than or equal to the value. For example, *uidNumber \>= 5000*.              |
+--------------------------+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Less than or equal to    | \<=                  | Returns all entries with attributes that are less than or equal to the value. For example, *uidNumber \<= 5000*.                 |
+--------------------------+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Presence                 | =\*                  | Returns all entries with one or more attributes. For example, *cn=\**.                                                           |
+--------------------------+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Approximate              | \~=                  | Returns all entries with the similar to the value attributes. For example, *l\~=san francisco* can return *l=san francisco*.     |
+--------------------------+----------------------+----------------------------------------------------------------------------------------------------------------------------------+

: Table 11.2. The ldapsearch filter operators

Show more

You can use *boolean* operators to combine multiple filters to the `ldapsearch`{.literal} command.

+----------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------+
| Search type          | Operator             | Description                                                                                                              |
+:=====================+:=====================+:=========================================================================================================================+
| AND                  | &                    | Returns all entries where all statements in the filters are true. For example, *(&(filter)(filter)(filter)...​)*.         |
+----------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------+
| OR                   | \|                   | Returns all entries where at least one statement in the filters is true. For example, *(\|(filter)(filter)(filter)...​)*. |
+----------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------+
| NOT                  | !                    | Returns all entries where the statement in the filter is not true. For example, *(!(filter))*.                           |
+----------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------+

: Table 11.3. The ldapsearch filter boolean operators

Show more

### [11.3. Additional resources](#searching-idm-entries-using-the-ldapsearch-command_113-additional-resources) {#additional-resources-4 .title}

-   [Searching entries and tuning searches in RHDS](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/management_configuration_and_operations/searching-entries-and-tuning-searches)
-   [Structure of IPA commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/introduction-to-the-idm-command-line-utilities#structure-of-ipa-commands)

## [Chapter 12. Configuring IdM for external provisioning of users](#configuring-idm-for-external-provisioning-of-users) {#chapter-12.-configuring-idm-for-external-provisioning-of-users .title}

As a system administrator, you can configure Identity Management (IdM) to support the provisioning of users by an external solution for managing identities.

Rather than use the `ipa`{.literal} utility, the administrator of the external provisioning system can access the IdM LDAP using the `ldapmodify`{.literal} utility. The administrator can add individual stage users from the CLI using ldapmodify or using an LDIF file.

The assumption is that you, as an IdM administrator, fully trust your external provisioning system to only add validated users. However, at the same time you do not want to assign the administrators of the external provisioning system the IdM role of `User Administrator`{.literal} to enable them to add new active users directly.

You can configure a script to automatically move the staged users created by the external provisioning system to active users automatically.

### [12.1. Preparing IdM accounts for automatic activation of stage user accounts](#preparing-idm-accounts-for-automatic-activation-of-stage-user-accounts) {#preparing-idm-accounts-for-automatic-activation-of-stage-user-accounts .title}

Configure service accounts with appropriate roles and password policies to enable external provisioning systems to manage Identity Management (IdM) user lifecycle. This automation streamlines user onboarding by allowing external systems to add and activate user accounts programmatically.

In this example, the user account to be used by the external system to add stage users is named **provisionator**. The user account to be used to automatically activate the stage users is named **activator**.

**Prerequisites**

-   The host on which you perform the procedure is enrolled into IdM.

**Procedure**

1.  Log in as IdM administrator:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit admin
    ```

2.  Create a user named **provisionator** with the privileges to add stage users.

    a.  Add the provisionator user account:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa user-add provisionator --first=provisioning --last=account --password
        ```

    b.  Grant the provisionator user the required privileges.

        i.  Create a custom role, `System Provisioning`{.literal}, to manage adding stage users:

            ``` {.language-plaintext tabindex="-1"}
            $ ipa role-add --desc "Responsible for provisioning stage users" "System Provisioning"
            ```

        ii. Add the `Stage User Provisioning`{.literal} privilege to the role. This privilege provides the ability to add stage users:

            ``` {.language-plaintext tabindex="-1"}
            $ ipa role-add-privilege "System Provisioning" --privileges="Stage User Provisioning"
            ```

        iii. Add the provisionator user to the role:

             ``` {.language-plaintext tabindex="-1"}
             $ ipa role-add-member --users=provisionator "System Provisioning"
             ```

        iv. Verify that the provisionator exists in IdM:

            ``` {.language-plaintext tabindex="-1"}
            $ ipa user-find provisionator --all --raw
            --------------
            1 user matched
            --------------
              dn: uid=provisionator,cn=users,cn=accounts,dc=idm,dc=example,dc=com
              uid: provisionator
              ...
            ```

3.  Create a user, **activator**, with the privileges to manage user accounts.

    a.  Add the activator user account:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa user-add activator --first=activation --last=account --password
        ```

    b.  Grant the activator user the required privileges by adding the user to the default `User Administrator`{.literal} role:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa role-add-member --users=activator "User Administrator"
        ```

4.  Create a user group for application accounts:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-add application-accounts
    ```

5.  Update the password policy for the group. The following policy prevents password expiration and lockout for the account but compensates the potential risks by requiring complex passwords:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa pwpolicy-add application-accounts --maxlife=10000 --minlife=0 --history=0 --minclasses=4 --minlength=8 --priority=1 --maxfail=0 --failinterval=1 --lockouttime=0
    ```

6.  Optional: Verify that the password policy exists in IdM:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa pwpolicy-show application-accounts
      Group: application-accounts
      Max lifetime (days): 10000
      Min lifetime (hours): 0
      History size: 0
    ...
    ```

7.  Add the provisioning and activation accounts to the group for application accounts:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-add-member application-accounts --users={provisionator,activator}
    ```

8.  Change the passwords for the user accounts:

    ``` {.language-plaintext tabindex="-1"}
    $ kpasswd provisionator
    $ kpasswd activator
    ```

    Changing the passwords is necessary because new IdM users passwords expire immediately.

**Additional resources**

-   [Managing user accounts using the command line](#managing-user-accounts-using-the-command-line "Chapter 1. Managing user accounts using the command line")
-   [Delegating permissions to user groups to manage users using IdM CLI](#delegating-permissions-to-user-groups-to-manage-users-using-idm-cli "Chapter 32. Delegating permissions to user groups to manage users using IdM CLI")
-   [Defining IdM Password Policies](#defining-idm-password-policies "Chapter 6. Defining IdM password policies")

### [12.2. Configuring automatic activation of IdM stage user accounts](#configuring-automatic-activation-of-idm-stage-user-accounts) {#configuring-automatic-activation-of-idm-stage-user-accounts .title}

Automate the activation of stage user accounts in Identity Management (IdM) by configuring a scheduled script to promote provisioned users to active status. This ensures that new user accounts are automatically activated and available for use shortly after they are created.

Important

It is assumed that the owner of the external provisioning system has already validated the users and that they do not require additional validation on the IdM side before the script adds them to IdM.

It is sufficient to enable the activation process on only one of your IdM servers.

**Prerequisites**

-   The **provisionator** and **activator** accounts exist in IdM. For details, see [Preparing IdM accounts for automatic activation of stage user accounts](#preparing-idm-accounts-for-automatic-activation-of-stage-user-accounts "12.1. Preparing IdM accounts for automatic activation of stage user accounts").
-   You have root privileges on the IdM server on which you are running the procedure.
-   You are logged in as IdM administrator.
-   You trust your external provisioning system.

**Procedure**

1.  Generate a keytab file for the activation account:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-getkeytab -s server.idm.example.com -p "activator" -k /etc/krb5.ipa-activation.keytab
    ```

    If you want to enable the activation process on more than one IdM server, generate the keytab file on one server only. Then copy the keytab file to the other servers.

2.  Create a script, `/usr/local/sbin/ipa-activate-all`{.literal}, with the following contents to activate all users:

    ``` {.language-plaintext tabindex="-1"}
    #!/bin/bash

    kinit -k -i activator

    ipa stageuser-find --all --raw | grep "  uid:" | cut -d ":" -f 2 | while read uid; do ipa stageuser-activate ${uid}; done
    ```

3.  Edit the permissions and ownership of the `ipa-activate-all`{.literal} script to make it executable:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 755 /usr/local/sbin/ipa-activate-all
    # chown root:root /usr/local/sbin/ipa-activate-all
    ```

4.  Create a systemd unit file, `/etc/systemd/system/ipa-activate-all.service`{.literal}, with the following contents:

    ``` {.language-plaintext tabindex="-1"}
    [Unit]
    Description=Scan IdM every minute for any stage users that must be activated

    [Service]
    Environment=KRB5_CLIENT_KTNAME=/etc/krb5.ipa-activation.keytab
    Environment=KRB5CCNAME=FILE:/tmp/krb5cc_ipa-activate-all
    ExecStart=/usr/local/sbin/ipa-activate-all
    ```

5.  Create a systemd timer, `/etc/systemd/system/ipa-activate-all.timer`{.literal}, with the following contents:

    ``` {.language-plaintext tabindex="-1"}
    [Unit]
    Description=Scan IdM every minute for any stage users that must be activated

    [Timer]
    OnBootSec=15min
    OnUnitActiveSec=1min

    [Install]
    WantedBy=multi-user.target
    ```

6.  Reload the new configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

7.  Enable `ipa-activate-all.timer`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable ipa-activate-all.timer
    ```

8.  Start `ipa-activate-all.timer`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start ipa-activate-all.timer
    ```

9.  Optional: Verify that the `ipa-activate-all.timer`{.literal} daemon is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status ipa-activate-all.timer
       ipa-activate-all.timer - Scan IdM every minute for any stage users that must be activated
       Loaded: loaded (/etc/systemd/system/ipa-activate-all.timer; enabled; vendor preset: disabled)
       Active: active (waiting) since Wed 2020-06-10 16:34:55 CEST; 15s ago
       Trigger: Wed 2020-06-10 16:35:55 CEST; 44s left

    Jun 10 16:34:55 server.idm.example.com systemd[1]: Started Scan IdM every minute for any stage users that must be activated.
    ```

### [12.3. Adding an IdM stage user defined in an LDIF file](#adding-an-idm-stage-user-defined-in-an-ldif-file) {#adding-an-idm-stage-user-defined-in-an-ldif-file .title}

Add stage users to Identity Management (IdM) by using LDIF files to provision users from external systems. This helps you to automate user provisioning workflows and integration with external identity sources.

While the example below shows adding one single user, multiple users can be added in one file in bulk mode.

**Prerequisites**

-   IdM administrator has created the **provisionator** account and a password for it. For details, see [Preparing IdM accounts for automatic activation of stage user accounts](#preparing-idm-accounts-for-automatic-activation-of-stage-user-accounts "12.1. Preparing IdM accounts for automatic activation of stage user accounts").

-   You as the external administrator know the password of the **provisionator** account.

-   You can SSH to the IdM server from your LDAP server.

-   You are able to supply the minimal set of attributes that an IdM stage user must have to allow the correct processing of the user life cycle, namely:

    -   The `distinguished name`{.literal} (dn)
    -   The `common name`{.literal} (cn)
    -   The `last name`{.literal} (sn)
    -   The `uid`{.literal}

**Procedure**

1.  On the external server, create an LDIF file that contains information about the new user:

    ``` {.language-plaintext tabindex="-1"}
    dn: uid=stageidmuser,cn=staged users,cn=accounts,cn=provisioning,dc=idm,dc=example,dc=com
    changetype: add
    objectClass: top
    objectClass: inetorgperson
    uid: stageidmuser
    sn: surname
    givenName: first_name
    cn: full_name
    ```

2.  Transfer the LDIF file from the external server to the IdM server:

    ``` {.language-plaintext tabindex="-1"}
    $ scp add-stageidmuser.ldif provisionator@server.idm.example.com:/provisionator/
    Password:
    add-stageidmuser.ldif                                                                                          100%  364   217.6KB/s   00:00
    ```

3.  Use the `SSH`{.literal} protocol to connect to the IdM server as **provisionator**:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh provisionator@server.idm.example.com
    Password:
    ```

4.  On the IdM server, obtain the Kerberos ticket-granting ticket (TGT) for the provisionator account:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit provisionator
    ```

5.  Enter the `ldapadd`{.literal} command with the -f option and the name of the LDIF file. Specify the name of the IdM server and the port number:

    ``` {.language-plaintext tabindex="-1"}
    $ ldapadd -h server.idm.example.com -p 389 -f add-stageidmuser.ldif
    SASL/GSSAPI authentication started
    SASL username: provisionator@IDM.EXAMPLE.COM
    SASL SSF: 256
    SASL data security layer installed.
    adding the entry "uid=stageidmuser,cn=staged users,cn=accounts,cn=provisioning,dc=idm,dc=example,dc=com"
    ```

### [12.4. Adding an IdM stage user directly from the CLI using ldapmodify](#adding-an-idm-stage-user-directly-from-the-cli-using-ldapmodify) {#adding-an-idm-stage-user-directly-from-the-cli-using-ldapmodify .title}

Use the `ldapmodify`{.literal} utility to add stage users directly to Identity Management (IdM) LDAP for automated provisioning workflows. This method is ideal for integrating IdM with external identity management systems and bulk user imports.

**Prerequisites**

-   The IdM administrator has created the **provisionator** account and a password for it. For details, see [Preparing IdM accounts for automatic activation of stage user accounts](#preparing-idm-accounts-for-automatic-activation-of-stage-user-accounts "12.1. Preparing IdM accounts for automatic activation of stage user accounts").

-   You as the external administrator know the password of the **provisionator** account.

-   You can SSH to the IdM server from your LDAP server.

-   You are able to supply the minimal set of attributes that an IdM stage user must have to allow the correct processing of the user life cycle, namely:

    -   The `distinguished name`{.literal} (dn)
    -   The `common name`{.literal} (cn)
    -   The `last name`{.literal} (sn)
    -   The `uid`{.literal}

**Procedure**

1.  Use the `SSH`{.literal} protocol to connect to the IdM server using your IdM identity and credentials:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh provisionator@server.idm.example.com
    Password:
    ```

2.  Obtain the TGT of the **provisionator** account, an IdM user with a role to add new stage users:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit provisionator
    ```

3.  Enter the `ldapmodify`{.literal} command and specify Generic Security Services API (GSSAPI) as the Simple Authentication and Security Layer (SASL) mechanism to use for authentication. Specify the name of the IdM server and the port:

    ``` {.language-plaintext tabindex="-1"}
    # ldapmodify -h server.idm.example.com -p 389 -Y GSSAPI
    SASL/GSSAPI authentication started
    SASL username: provisionator@IDM.EXAMPLE.COM
    SASL SSF: 56
    SASL data security layer installed.
    ```

4.  Enter the `dn`{.literal} of the user you are adding:

    ``` {.language-plaintext tabindex="-1"}
    dn: uid=stageuser,cn=staged users,cn=accounts,cn=provisioning,dc=idm,dc=example,dc=com
    ```

5.  Enter **add** as the type of change you are performing:

    ``` {.language-plaintext tabindex="-1"}
    changetype: add
    ```

6.  Specify the LDAP object class categories required to allow the correct processing of the user life cycle:

    ``` {.language-plaintext tabindex="-1"}
    objectClass: top
    objectClass: inetorgperson
    ```

    You can specify additional object classes.

7.  Enter the `uid`{.literal} of the user:

    ``` {.language-plaintext tabindex="-1"}
    uid: stageuser
    ```

8.  Enter the `cn`{.literal} of the user:

    ``` {.language-plaintext tabindex="-1"}
    cn: Babs Jensen
    ```

9.  Enter the last name of the user:

    ``` {.language-plaintext tabindex="-1"}
    sn: Jensen
    ```

10. Press `Enter`{.literal} again to confirm that this is the end of the entry:

    ``` {.language-plaintext tabindex="-1"}
    [Enter]

    adding new entry "uid=stageuser,cn=staged users,cn=accounts,cn=provisioning,dc=idm,dc=example,dc=com"
    ```

11. Exit the connection using **Ctrl** + **C**.

**Verification**

Verify the contents of the stage entry to make sure your provisioning system added all required POSIX attributes and the stage entry is ready to be activated.

-   To display the new stage user's LDAP attributes, enter the `ipa stageuser-show --all --raw`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa stageuser-show stageuser --all --raw
      dn: uid=stageuser,cn=staged users,cn=accounts,cn=provisioning,dc=idm,dc=example,dc=com
      uid: stageuser
      sn: Jensen
      cn: Babs Jensen
      has_password: FALSE
      has_keytab: FALSE
      nsaccountlock: TRUE
      objectClass: top
      objectClass: inetorgperson
      objectClass: organizationalPerson
      objectClass: person
    ```

    Note that the user is explicitly disabled by the `nsaccountlock`{.literal} attribute.

### [12.5. Additional resources](#configuring-idm-for-external-provisioning-of-users_125-additional-resources) {#additional-resources-5 .title}

-   [Adding an IdM stage user directly from the CLI using ldapmodify](#adding-an-idm-stage-user-directly-from-the-cli-using-ldapmodify "12.4. Adding an IdM stage user directly from the CLI using ldapmodify")
-   [Adding an IdM stage user defined in an LDIF file](#adding-an-idm-stage-user-defined-in-an-ldif-file "12.3. Adding an IdM stage user defined in an LDIF file")
-   [Configuring automatic activation of IdM stage user accounts](#configuring-automatic-activation-of-idm-stage-user-accounts "12.2. Configuring automatic activation of IdM stage user accounts")
-   [Using ldapmodify to manage IdM users externally](#using-ldapmodify-to-manage-idm-users-externally "Chapter 10. Using ldapmodify to manage IdM users externally")

## [Chapter 13. Managing Kerberos principal aliases for users, hosts, and services](#managing-kerberos-principal-aliases-for-users-hosts-and-services) {#chapter-13.-managing-kerberos-principal-aliases-for-users-hosts-and-services .title}

Manage Kerberos principal aliases for users, hosts, and services in Identity Management (IdM) to enable authentication with alternative names. Aliases allow users to log in with multiple names, such as a previous username or an email address.

When you create a new user, host, or service, a Kerberos principal in the following format is automatically added:

-   *user_name@REALM*
-   host/*host_name@REALM*
-   *service_name/host_name@REALM*

Administrators can enable users, hosts, or services to authenticate against Kerberos applications using an alias. This is beneficial in the following scenarios:

-   The user name changed and the user wants to log in using both the previous and new user name.
-   The user needs to log in using the email address even if the IdM Kerberos realm differs from the email domain.

Note that if you rename a user, the object keeps the aliases and the previous canonical principal name.

### [13.1. Adding a Kerberos principal alias](#adding-a-kerberos-principal-alias) {#adding-a-kerberos-principal-alias .title}

You can associate alias names with existing Kerberos principals in an Identity Management (IdM) environment. This enhances security and simplifies authentication processes within the IdM domain.

**Procedure**

-   To add the alias name `useralias`{.literal} to the account `user`{.literal}, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa user-add-principal <user> <useralias>
    --------------------------------
    Added new aliases to user "user"
    --------------------------------
             User login: user
        Principal alias: user@IDM.EXAMPLE.COM, useralias@IDM.EXAMPLE.COM
    ```

    To add an alias to a host or service, use the `ipa host-add-principal`{.literal} or `ipa service-add-principal`{.literal} command respectively instead.

    If you use an alias name to authenticate, use the `-C`{.literal} option with the `kinit`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # kinit -C <useralias>
    Password for <user>@IDM.EXAMPLE.COM:
    ```

### [13.2. Removing a Kerberos principal alias](#removing-a-kerberos-principal-alias) {#removing-a-kerberos-principal-alias .title}

Remove principal Kerberos aliases from users, hosts, or services to clean up authentication credentials after organizational changes.

**Procedure**

-   To remove the alias `useralias`{.literal} from the account `user`{.literal}, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa user-remove-principal <user> <useralias>
    --------------------------------
    Removed aliases from user "user"
    --------------------------------
      User login: user
      Principal alias: user@IDM.EXAMPLE.COM
    ```

    To remove an alias from a host or service, use the `ipa host-remove-principal`{.literal} or `ipa service-remove-principal`{.literal} command respectively instead.

    Note that you cannot remove the canonical principal name:

    ``` {.language-plaintext tabindex="-1"}
    # ipa user-show <user>
      User login: user
      ...
      Principal name: user@IDM.EXAMPLE.COM
      ...

    # ipa user-remove-principal user user
    ipa: ERROR: invalid 'krbprincipalname': at least one value equal to the canonical principal name must be present
    ```

### [13.3. Adding a Kerberos enterprise principal alias](#adding-a-kerberos-enterprise-principal-alias) {#adding-a-kerberos-enterprise-principal-alias .title}

Associate enterprise principal alias names with Kerberos principals in Identity Management (IdM) to provide flexible authentication options across different domains. With this, users can authenticate by using alternative domain suffixes while maintaining a single identity.

``` {.language-plaintext tabindex="-1"}
Enterprise principal aliases can use any domain suffix except for user principal name (UPN) suffixes, NetBIOS names, or domain names of trusted Active Directory forest domains.
```

**Procedure**

-   To add the enterprise principal alias `user@example.com`{.literal} to the `user`{.literal} account:

    ``` {.language-plaintext tabindex="-1"}
    # ipa user-add-principal <user> <user\\@example.com>
    --------------------------------
    Added new aliases to user "user"
    --------------------------------
             User login: user
        Principal alias: user@IDM.EXAMPLE.COM, user\@example.com@IDM.EXAMPLE.COM
    ```

    To add an enterprise alias to a host or service, use the `ipa host-add-principal`{.literal} or `ipa service-add-principal`{.literal} command respectively instead.

    Note

    When adding or removing enterprise principal aliases, escape the @ symbol using two backslashes (\\\\). Otherwise, the shell interprets the @ symbol as part of the Kerberos realm name and leads to the following error:

    ``` {.language-plaintext tabindex="-1"}
    ipa: ERROR: The realm for the principal does not match the realm for this IPA server.
    ```

    If you use an enterprise principal name to authenticate, use the `-E`{.literal} option with the `kinit`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # kinit -E <user@example.com>
    Password for user\@example.com@IDM.EXAMPLE.COM:
    ```

### [13.4. Removing a Kerberos enterprise principal alias](#removing-a-kerberos-enterprise-principal-alias) {#removing-a-kerberos-enterprise-principal-alias .title}

Remove enterprise principal aliases from users, hosts, or services to clean up authentication credentials after organizational changes.

**Procedure**

-   To remove the enterprise principal alias `user@example.com`{.literal} from the account `user`{.literal}, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa user-remove-principal <user> <user\\@example.com>
    --------------------------------
    Removed aliases from user "user"
    --------------------------------
      User login: user
      Principal alias: user@IDM.EXAMPLE.COM
    ```

    To remove an alias from a host or service, use the `ipa host-remove-principal`{.literal} or `ipa service-remove-principal`{.literal} command respectively instead.

    Note

    When adding or removing enterprise principal aliases, escape the @ symbol using two backslashes (\\\\). Otherwise, the shell interprets the @ symbol as part of the Kerberos realm name and leads to the following error:

    ``` {.language-plaintext tabindex="-1"}
    ipa: ERROR: The realm for the principal does not match the realm for this IPA server
    ```

## [Chapter 14. Strengthening Kerberos security with PAC information](#strengthening-kerberos-security-with-pac-information) {#chapter-14.-strengthening-kerberos-security-with-pac-information .title}

Strengthen Kerberos security in Identity Management (IdM) by using Privilege Attribute Certificate (PAC) information to include authorization data in Kerberos tickets. You can also enable Security Identifiers (SIDs) for deployments installed before RHEL 8.5.

### [14.1. Privilege Attribute Certificate (PAC) use in IdM](#privilege-attribute-certificate-pac-use-in-idm) {#privilege-attribute-certificate-pac-use-in-idm .title}

To increase security, Identity Management (IdM) issues Kerberos tickets with Privilege Attribute Certificate (PAC) information by default. A PAC has rich information about a Kerberos principal, including its Security Identifier (SID), group memberships, and home directory information.

SIDs, which Microsoft Active Directory (AD) uses by default, are globally unique identifiers that are never reused. SIDs express multiple namespaces: each domain has a SID, which is a prefix in the SID of each object.

Starting from RHEL 8.5, when you install an IdM server or replica, the installation script generates SIDs for users and groups by default. This allows IdM to work with PAC data. If you installed IdM before RHEL 8.5, and you have not configured a trust with an AD domain, you may not have generated SIDs for your IdM objects.

By evaluating PAC information in Kerberos tickets, you can control resource access with much greater detail. For example, the Administrator account in one domain has a uniquely different SID than the Administrator account in any other domain. In an IdM environment with a trust to an AD domain, you can set access controls based on globally unique SIDs rather than simple user names or UIDs that might repeat in different locations, such as every Linux `root`{.literal} account having a UID of 0.

**Additional resources**

-   [Enabling Security Identifiers (SIDs) in IdM](#enabling-security-identifiers-sids-in-idm "14.2. Enabling Security Identifiers (SIDs) in IdM")

### [14.2. Enabling Security Identifiers (SIDs) in IdM](#enabling-security-identifiers-sids-in-idm) {#enabling-security-identifiers-sids-in-idm .title}

Enable Security Identifiers (SIDs) for existing Identity Management (IdM) objects to support Kerberos security based on Privilege Access Certificate (PAC) information.

This is required for IdM deployments installed before RHEL 8.5 that have not configured an Active Directory trust. As of RHEL 8.6, Kerberos in IdM requires that your IdM objects have SIDs.

**Prerequisites**

-   You installed IdM before RHEL 8.5.
-   You have not run the `ipa-sidgen`{.literal} task, which is part of configuring a trust with an Active Directory domain.
-   You can authenticate as the IdM admin account.

**Procedure**

-   Enable SID usage and trigger the `SIDgen`{.literal} task to generate SIDs for existing users and groups. This task might be resource-intensive:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa config-mod --enable-sid --add-sids
    ```

**Verification**

-   Verify that the IdM `admin`{.literal} user account entry has an `ipantsecurityidentifier`{.literal} attribute with a SID that ends with `-500`{.literal}, the SID reserved for the domain administrator:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa user-show admin --all | grep ipantsecurityidentifier
      ipantsecurityidentifier: S-1-5-21-2633809701-976279387-419745629-500
    ```

**Additional resources**

-   [Privilege Attribute Certificate (PAC) use in IdM](#privilege-attribute-certificate-pac-use-in-idm "14.1. Privilege Attribute Certificate (PAC) use in IdM")
-   [How to solve users unable to authenticate to IPA/IDM with PAC issues - S4U2PROXY_EVIDENCE_TKT_WITHOUT_PAC error (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7052703)
-   [Trust controllers and trust agents](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-a-cross-forest-trust-between-idm-and-ad#trust-controllers-and-trust-agents)
-   [Integrate SID configuration into base IPA installers](https://freeipa.readthedocs.io/en/latest/designs/adtrust/sidconfig.html)

## [Chapter 15. Managing Kerberos ticket policies](#managing-kerberos-ticket-policies) {#chapter-15.-managing-kerberos-ticket-policies .title}

Kerberos ticket policies in Identity Management (IdM) set restrictions on Kerberos ticket access, duration, and renewal. You can configure Kerberos ticket policies for the Key Distribution Center (KDC) running on your IdM server.

### [15.1. The role of the IdM KDC](#the-role-of-the-idm-kdc) {#the-role-of-the-idm-kdc .title}

Identity Management (IdM) authentication relies on the Kerberos Key Distribution Center (KDC), the trusted authority that issues and validates tickets for all users, services, and hosts in the IdM network.

Each IdM user, service, and host acts as a Kerberos client and is identified by a unique Kerberos *principal*:

-   For users: `identifier@REALM`{.literal}, such as `admin@EXAMPLE.COM`{.literal}
-   For services: `service/fully-qualified-hostname@REALM`{.literal}, such as `http/server.example.com@EXAMPLE.COM`{.literal}
-   For hosts: `host/fully-qualified-hostname@REALM`{.literal}, such as `host/client.example.com@EXAMPLE.COM`{.literal}

The following image is a simplification of the communication between a Kerberos client, the KDC, and a Kerberized application that the client wants to communicate with.

1.  A Kerberos client identifies itself to the KDC by authenticating as a Kerberos principal. For example, an IdM user performs `kinit `{.literal}*`username`{.literal}* and provides their password.
2.  The KDC checks for the principal in its database, authenticates the client, and evaluates Kerberos ticket policies to determine whether to grant the request.
3.  The KDC issues the client a ticket-granting ticket (TGT) with a lifecycle and authentication indicators according to the appropriate ticket policy.
4.  With the TGT, the client requests a *service ticket* from the KDC to communicate with a Kerberized service on a target host.
5.  The KDC checks if the client's TGT is still valid, and evaluates the service ticket request against ticket policies.
6.  The KDC issues the client a *service ticket*.
7.  With the service ticket, the client can initiate encrypted communication with the service on the target host.

**Additional resources**

-   [IdM Kerberos ticket policy types](#idm-kerberos-ticket-policy-types "15.2. IdM Kerberos ticket policy types")
-   [Kerberos authentication indicators](#kerberos-authentication-indicators "15.3. Kerberos authentication indicators")

### [15.2. IdM Kerberos ticket policy types](#idm-kerberos-ticket-policy-types) {#idm-kerberos-ticket-policy-types .title}

Identity Management (IdM) uses several Kerberos ticket policy types. You can use these policy types to enforce authentication requirements and control ticket lifecycles across your deployment.

Connection policy

:   To protect Kerberized services with different levels of security, you can define connection policies to enforce rules based on which pre-authentication mechanism a client used to retrieve a ticket-granting ticket (TGT).

    For example, you can require smart card authentication to connect to `client1.example.com`{.literal}, and require two-factor authentication to access the `testservice`{.literal} application on `client2.example.com`{.literal}.

    To enforce connection policies, associate *authentication indicators* with services. Only clients that have the required authentication indicators in their service ticket requests are able to access those services.

Ticket lifecycle policy

:   Each Kerberos ticket has a *lifetime* and a potential *renewal age*: you can renew a ticket before it reaches its maximum lifetime, but not after it exceeds its maximum renewal age.

    The default global ticket lifetime is one day (86400 seconds) and the default global maximum renewal age is one week (604800 seconds). You can adjust these global values.

    You can also define your own ticket lifecycle policies.

**Additional resources**

-   [Managing Kerberos ticket policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-kerberos-ticket-policies)

### [15.3. Kerberos authentication indicators](#kerberos-authentication-indicators) {#kerberos-authentication-indicators .title}

Kerberos authentication indicators identify which pre-authentication mechanism a client used to obtain a ticket-granting ticket (TGT). Services can require specific authentication indicators to enforce security policies like smart card or two-factor authentication.

The indicators are:

`otp`{.literal}
:   two-factor authentication (password + One-Time Password)

`radius`{.literal}
:   RADIUS authentication (commonly for 802.1x authentication)

`pkinit`{.literal}
:   PKINIT, smart card, or certificate authentication

`hardened`{.literal}
:   hardened passwords (SPAKE or FAST)[^\[1\]^](#ftn.idm139997963995360)

The KDC then attaches the authentication indicators from the TGT to any service ticket requests that stem from it. The KDC enforces policies such as service access control, maximum ticket lifetime, and maximum renewable age based on the authentication indicators.

Authentication indicators and IdM services
:   If you associate a service or a host with an authentication indicator, only clients that used the corresponding authentication mechanism to obtain a TGT will be able to access it. The KDC, not the application or service, checks for authentication indicators in service ticket requests, and grants or denies requests based on Kerberos connection policies.

If a service or a host has no authentication indicators assigned to it, it will accept tickets authenticated by any mechanism.

**Additional resources**

-   [Enforcing authentication indicators for an IdM service](#enforcing-authentication-indicators-for-an-idm-service "15.4. Enforcing authentication indicators for an IdM service")
-   [Enabling GSSAPI authentication and enforcing Kerberos authentication indicators for sudo on an IdM client](enabling-gssapi-authentication-and-enforcing-kerberos-authentication-indicators-for-sudo-on-an-idm-client)

\

------------------------------------------------------------------------

[^\[1\]^](#idm139997963995360) A hardened password is protected against brute-force password dictionary attacks by using Single-Party Public-Key Authenticated Key Exchange (SPAKE) pre-authentication and/or Flexible Authentication via Secure Tunneling (FAST) armoring.

### [15.4. Enforcing authentication indicators for an IdM service](#enforcing-authentication-indicators-for-an-idm-service) {#enforcing-authentication-indicators-for-an-idm-service .title}

Enforce authentication indicators for an Identity Management (IdM) service to require specific pre-authentication methods for access. This ensures that only users who authenticated with stronger methods, such as one-time passwords, can access security-critical services.

Authentication mechanisms in IdM vary in their security strength. For example, obtaining a ticket-granting ticket (TGT) using a one-time password (OTP) combined with a password is more secure than using only a password. By associating authentication indicators with a particular IdM service, you can configure the service so that only users who used specific pre-authentication mechanisms to obtain their initial TGT will be able to access it.

In this way, you can configure different IdM services so that:

-   Only users who used a stronger authentication method to obtain their initial TGT, such as a one-time password (OTP), can access services critical to security, such as a VPN.
-   Users who used simpler authentication methods to obtain their initial TGT, such as a password, can only access non-critical services, such as local logins.

**Figure 15.1. Example of authenticating using different technologies**

This procedure describes creating an IdM service and configuring it to require particular Kerberos authentication indicators from incoming service ticket requests.

#### [15.4.1. Creating an IdM service entry and its Kerberos keytab](#creating-an-idm-service-entry-and-its-kerberos-keytab) {#creating-an-idm-service-entry-and-its-kerberos-keytab .title}

Create service entries in Identity Management (IdM) to generate Kerberos principals and enable SSL certificate or Kerberos keytab requests. Service entries establish secure identities for applications and automate credential management without using cleartext passwords.

**Prerequisites**

-   Your service can store a Kerberos principal, an SSL certificate, or both.

**Procedure**

1.  Add an IdM service with the `ipa service-add`{.literal} command to create a Kerberos principal associated with it. For example, to create the IdM service entry for the `testservice`{.literal} application that runs on host `client.example.com`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# ipa service-add testservice/client.example.com
    -------------------------------------------------------------
    Modified service "testservice/client.example.com@EXAMPLE.COM"
    -------------------------------------------------------------
      Principal name: testservice/client.example.com@EXAMPLE.COM
      Principal alias: testservice/client.example.com@EXAMPLE.COM
      Managed by: client.example.com
    ```

2.  Generate and store a Kerberos keytab for the service on the client.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# ipa-getkeytab -k /etc/testservice.keytab -p testservice/client.example.com
    Keytab successfully retrieved and stored in: /etc/testservice.keytab
    ```

**Verification**

1.  Display information about an IdM service with the `ipa service-show`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa service-show testservice/client.example.com
      Principal name: testservice/client.example.com@EXAMPLE.COM
      Principal alias: testservice/client.example.com@EXAMPLE.COM
      Keytab: True
      Managed by: client.example.com
    ```

2.  Display the contents of the service's Kerberos keytab with the `klist`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    [root@server etc]# klist -ekt /etc/testservice.keytab
    Keytab name: FILE:/etc/testservice.keytab
    KVNO Timestamp           Principal
    ---- ------------------- ------------------------------------------------------
       2 04/01/2020 17:52:55 testservice/client.example.com@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
       2 04/01/2020 17:52:55 testservice/client.example.com@EXAMPLE.COM (aes128-cts-hmac-sha1-96)
       2 04/01/2020 17:52:55 testservice/client.example.com@EXAMPLE.COM (camellia128-cts-cmac)
       2 04/01/2020 17:52:55 testservice/client.example.com@EXAMPLE.COM (camellia256-cts-cmac)
    ```

#### [15.4.2. Associating authentication indicators with an IdM service using IdM CLI](#associating-authentication-indicators-with-an-idm-service-using-idm-cli) {#associating-authentication-indicators-with-an-idm-service-using-idm-cli .title}

Require specific authentication methods for accessing services using the Identity Management (IdM) CLI by configuring authentication indicators. With authentication indicators configured, you can enforce stronger authentication like two-factor or smart cards for sensitive services.

For example, you can ensure that only users who used a valid IdM two-factor authentication token with their password when obtaining a Kerberos ticket-granting ticket (TGT) will be able to access that host or service.

Follow this procedure to configure a service to require particular Kerberos authentication indicators from incoming service ticket requests.

When you configure a service, you must specify authentication indicators using the `--auth-ind`{.literal} argument. Common `--auth-ind`{.literal} values include:

otp
:   For two-factor authentication.

radius
:   For RADIUS authentication.

pkinit
:   For PKINIT, smart card, or certificate authentication.

hardened
:   For hardened passwords (SPAKE or FAST).

**Prerequisites**

-   You have created an IdM service entry for a service that runs on an IdM host. See [Creating an IdM service entry and its Kerberos keytab](#creating-an-idm-service-entry-and-its-kerberos-keytab "15.4.1. Creating an IdM service entry and its Kerberos keytab").
-   You have obtained the ticket-granting ticket of an administrative user in IdM.

Warning

Do **not** assign authentication indicators to internal IdM services. The following IdM services cannot perform the interactive authentication steps required by PKINIT and multi-factor authentication methods:

``` {.language-plaintext tabindex="-1"}
host/server.example.com@EXAMPLE.COM
HTTP/server.example.com@EXAMPLE.COM
ldap/server.example.com@EXAMPLE.COM
DNS/server.example.com@EXAMPLE.COM
cifs/server.example.com@EXAMPLE.COM
```

**Procedure**

-   Use the `ipa service-mod`{.literal} command to specify one or more required authentication indicators for a service, identified with the `--auth-ind`{.literal} argument.

    For example, to require that a user was authenticated with smart card or OTP authentication to retrieve a service ticket for the `testservice`{.literal} principal on host `client.example.com`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa service-mod testservice/client.example.com@EXAMPLE.COM --auth-ind otp --auth-ind pkinit
    -------------------------------------------------------------
    Modified service "testservice/client.example.com@EXAMPLE.COM"
    -------------------------------------------------------------
      Principal name: testservice/client.example.com@EXAMPLE.COM
      Principal alias: testservice/client.example.com@EXAMPLE.COM
      Authentication Indicators: otp, pkinit
      Managed by: client.example.com
    ```

-   To remove all authentication indicators from a service, provide an empty list of indicators:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa service-mod testservice/client.example.com@EXAMPLE.COM --auth-ind ''
    ------------------------------------------------------
    Modified service "testservice/client.example.com@EXAMPLE.COM"
    ------------------------------------------------------
      Principal name: testservice/client.example.com@EXAMPLE.COM
      Principal alias: testservice/client.example.com@EXAMPLE.COM
      Managed by: client.example.com
    ```

**Verification**

-   Display information about an IdM service, including the authentication indicators it requires, with the `ipa service-show`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa service-show testservice/client.example.com
      Principal name: testservice/client.example.com@EXAMPLE.COM
      Principal alias: testservice/client.example.com@EXAMPLE.COM
      Authentication Indicators: otp, pkinit
      Keytab: True
      Managed by: client.example.com
    ```

**Additional resources**

-   [Retrieving a Kerberos service ticket for an IdM service](#retrieving-a-kerberos-service-ticket-for-an-idm-service "15.4.4. Retrieving a Kerberos service ticket for an IdM service")
-   [Enabling GSSAPI authentication and enforcing Kerberos authentication indicators for sudo on an IdM client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/granting-sudo-access-to-an-idm-user-on-an-idm-client#enabling-gssapi-authentication-and-enforcing-kerberos-authentication-indicators-for-sudo-on-an-idm-client)

#### [15.4.3. Associating authentication indicators with an IdM service using IdM Web UI](#associating-authentication-indicators-with-an-idm-service-using-idm-web-ui) {#associating-authentication-indicators-with-an-idm-service-using-idm-web-ui .title}

Require specific authentication methods for accessing services using the Identity Management (IdM) Web UI by configuring authentication indicators. With authentication indicators configured, you can enforce stronger authentication like two-factor or smart cards for sensitive services.

For example, you can ensure that only users who used a valid IdM two-factor authentication token with their password when obtaining a Kerberos ticket-granting ticket (TGT) will be able to access that host or service.

Follow this procedure to use the IdM Web UI to configure a host or service to require particular Kerberos authentication indicators from incoming ticket requests.

**Prerequisites**

-   You have logged in to the IdM Web UI as an administrative user.

**Procedure**

1.  Select Identity → Hosts or Identity → Services.

2.  Click the name of the required host or service.

3.  Under `Authentication indicators`{.literal}, select the required authentication method.

    -   For example, selecting `OTP`{.literal} ensures that only users who used a valid IdM two-factor authentication token with their password when obtaining a Kerberos TGT will be able to access the host or service.
    -   If you select both `OTP`{.literal} and `RADIUS`{.literal}, then both users that used a valid IdM two-factor authentication token with their password when obtaining a Kerberos TGT **and** users that used the RADIUS server for obtaining their Kerberos TGT will be allowed access.

4.  Click Save at the top of the page.

**Additional resources**

-   [Retrieving a Kerberos service ticket for an IdM service](#retrieving-a-kerberos-service-ticket-for-an-idm-service "15.4.4. Retrieving a Kerberos service ticket for an IdM service")
-   [Enabling GSSAPI authentication and enforcing Kerberos authentication indicators for sudo on an IdM client](enabling-gssapi-authentication-and-enforcing-kerberos-authentication-indicators-for-sudo-on-an-idm-client)

#### [15.4.4. Retrieving a Kerberos service ticket for an IdM service](#retrieving-a-kerberos-service-ticket-for-an-idm-service) {#retrieving-a-kerberos-service-ticket-for-an-idm-service .title}

Retrieve a Kerberos service ticket for an Identity Management (IdM) service to verify that Kerberos ticket policies, such as required authentication indicators, are enforced correctly for that service.

**Prerequisites**

-   If the service you are working with is not an internal IdM service, you have created a corresponding *IdM service* entry for it. See [Creating an IdM service entry and its Kerberos keytab](#creating-an-idm-service-entry-and-its-kerberos-keytab "15.4.1. Creating an IdM service entry and its Kerberos keytab").
-   You have a Kerberos ticket-granting ticket (TGT).

**Procedure**

-   Use the `kvno`{.literal} command with the `-S`{.literal} option to retrieve a service ticket, and specify the name of the IdM service and the fully-qualified domain name of the host that manages it.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kvno -S testservice client.example.com
    testservice/client.example.com@EXAMPLE.COM: kvno = 1
    ```

    Note

    If you need to access an IdM service and your current ticket-granting ticket (TGT) does not possess the required Kerberos authentication indicators associated with it, clear your current Kerberos credentials cache with the `kdestroy`{.literal} command and retrieve a new TGT:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kdestroy
    ```

    For example, if you initially retrieved a TGT by authenticating with a password, and you need to access an IdM service that has the `pkinit`{.literal} authentication indicator associated with it, destroy your current credentials cache and re-authenticate with a smart card. See [Kerberos authentication indicators](#kerberos-authentication-indicators "15.3. Kerberos authentication indicators").

**Verification**

-   Use the `klist`{.literal} command to verify that the service ticket is in the default Kerberos credentials cache.

    ``` {.language-plaintext tabindex="-1"}
    [root@server etc]# klist_
    Ticket cache: KCM:1000
    Default principal: admin@EXAMPLE.COM

    Valid starting       Expires              Service principal
    04/01/2020 12:52:42  04/02/2020 12:52:39  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    04/01/2020 12:54:07 04/02/2020 12:52:39 testservice/client.example.com@EXAMPLE.COM
    ```

#### [15.4.5. Additional resources](#enforcing-authentication-indicators-for-an-idm-service_1545-additional-resources) {#additional-resources-6 .title}

-   [Kerberos authentication indicators](#kerberos-authentication-indicators "15.3. Kerberos authentication indicators")

### [15.5. Configuring the global ticket lifecycle policy](#configuring-the-global-ticket-lifecycle-policy) {#configuring-the-global-ticket-lifecycle-policy .title}

Adjust the global Kerberos ticket policy in Identity Management (IdM) to set baseline security requirements for all users and services. Global policies help maintain consistent authentication security across your entire environment.

The global ticket policy applies to all service tickets and to users that do not have any per-user ticket policies defined.

While using the `ipa krbtpolicy-mod`{.literal} command, specify at least one of the following arguments:

-   `--maxlife`{.literal} for the maximum ticket lifetime in seconds
-   `--maxrenew`{.literal} for the maximum renewable age in seconds

**Procedure**

1.  To modify the global ticket policy:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-mod --maxlife=$((8*60*60)) --maxrenew=$((24*60*60))
      Max life: 28800
      Max renew: 86400
    ```

    In this example, the maximum lifetime is set to eight hours (8 \* 60 minutes \* 60 seconds) and the maximum renewal age is set to one day (24 \* 60 minutes \* 60 seconds).

2.  Optional: To reset the global Kerberos ticket policy to the default installation values:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-reset
      Max life: 86400
      Max renew: 604800
    ```

**Verification**

-   Display the global ticket policy:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-show
      Max life: 28800
      Max renew: 86640
    ```

**Additional resources**

-   [Configuring the default ticket policy for a user](#configuring-the-default-ticket-policy-for-a-user "15.7. Configuring the default ticket policy for a user")
-   [Configuring individual authentication indicator ticket policies for a user](#configuring-individual-authentication-indicator-ticket-policies-for-a-user "15.8. Configuring individual authentication indicator ticket policies for a user")

### [15.6. Configuring global ticket policies per authentication indicator](#configuring-global-ticket-policies-per-authentication-indicator) {#configuring-global-ticket-policies-per-authentication-indicator .title}

Set different Kerberos ticket lifetimes in Identity Management (IdM) based on authentication method to enforce stronger security for weaker logins while permitting longer sessions for smart card or two-factor authentication.

These global settings apply to all users who do not have individual ticket policies configured. Use the `ipa krbtpolicy-mod`{.literal} command to set maximum lifetime and maximum renewable age values for each authentication indicator.

**Procedure**

-   For example, to set the global two-factor ticket lifetime and renewal age values to one week, and the global smart card ticket lifetime and renewal age values to two weeks:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-mod --otp-maxlife=604800 --otp-maxrenew=604800 --pkinit-maxlife=172800 --pkinit-maxrenew=172800
    ```

**Verification**

-   Display the global ticket policy:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-show
      Max life: 86400
      OTP max life: 604800
      PKINIT max life: 172800
      Max renew: 604800
      OTP max renew: 604800
      PKINIT max renew: 172800
    ```

    Notice that the OTP and PKINIT values are different from the global default `Max life`{.literal} and `Max renew`{.literal} values.

**Additional resources**

-   [Authentication indicator options for the `krbtpolicy-mod`{.literal} command](#authentication-indicator-options-for-the-krbtpolicy-mod-command "15.9. Authentication indicator options for the krbtpolicy-mod command")
-   [Configuring the default ticket policy for a user](#configuring-the-default-ticket-policy-for-a-user "15.7. Configuring the default ticket policy for a user")
-   [Configuring individual authentication indicator ticket policies for a user](#configuring-individual-authentication-indicator-ticket-policies-for-a-user "15.8. Configuring individual authentication indicator ticket policies for a user")

### [15.7. Configuring the default ticket policy for a user](#configuring-the-default-ticket-policy-for-a-user) {#configuring-the-default-ticket-policy-for-a-user .title}

Define custom Kerberos ticket policies for individual users in Identity Management (IdM) to enforce specific security requirements. Per-user policies override global settings and ensure that the maximum ticket lifetime and renewal periods match a user's specific role or risk level.

Use the `ipa krbtpolicy-mod `{.literal}*`username`{.literal}* command, and specify at least one of the following arguments:

-   `--maxlife`{.literal} for the maximum ticket lifetime in seconds
-   `--maxrenew`{.literal} for the maximum renewable age in seconds

**Procedure**

1.  For example, to set the IdM `admin`{.literal} user's maximum ticket lifetime to two days and maximum renewal age to two weeks:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-mod admin --maxlife=172800 --maxrenew=1209600
      Max life: 172800
      Max renew: 1209600
    ```

2.  Optional: To reset the ticket policy for a user:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-reset admin
    ```

**Verification**

-   Display the effective Kerberos ticket policy that applies to a user:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-show admin
      Max life: 172800
      Max renew: 1209600
    ```

**Additional resources**

-   [Configuring the global ticket lifecycle policy](#configuring-the-global-ticket-lifecycle-policy "15.5. Configuring the global ticket lifecycle policy")
-   [Configuring global ticket policies per authentication indicator](#configuring-global-ticket-policies-per-authentication-indicator "15.6. Configuring global ticket policies per authentication indicator")

### [15.8. Configuring individual authentication indicator ticket policies for a user](#configuring-individual-authentication-indicator-ticket-policies-for-a-user) {#configuring-individual-authentication-indicator-ticket-policies-for-a-user .title}

Configure per-authentication indicator Kerberos ticket policies for users in Identity Management (IdM) to apply different ticket lifetime and renewal rules based on authentication method.

For example, you can configure a policy to allow the IdM `admin`{.literal} user to renew a ticket for two days if it was obtained with OTP authentication, and a week if it was obtained with smart card authentication.

These per-authentication indicator settings will override the *user's* default ticket policy, the *global* default ticket policy, and any *global* authentication indicator ticket policy.

Use the `ipa krbtpolicy-mod `{.literal}*`username`{.literal}* command to set custom maximum lifetime and maximum renewable age values for a user's Kerberos tickets depending on the [authentication indicators](#kerberos-authentication-indicators "15.3. Kerberos authentication indicators") attached to them.

**Procedure**

1.  For example, to allow the IdM `admin`{.literal} user to renew a Kerberos ticket for two days if it was obtained with One-Time Password authentication, set the `--otp-maxrenew`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-mod admin --otp-maxrenew=$((2*24*60*60))
      OTP max renew: 172800
    ```

2.  Optional: To reset the ticket policy for a user:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-reset username
    ```

**Verification**

-   Display the effective Kerberos ticket policy that applies to a user:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa krbtpolicy-show admin
      Max life: 28800
      Max renew: 86640
    ```

**Additional resources**

-   [Authentication indicator options for the `krbtpolicy-mod`{.literal} command](#authentication-indicator-options-for-the-krbtpolicy-mod-command "15.9. Authentication indicator options for the krbtpolicy-mod command")
-   [Configuring the default ticket policy for a user](#configuring-the-default-ticket-policy-for-a-user "15.7. Configuring the default ticket policy for a user")
-   [Configuring the global ticket lifecycle policy](#configuring-the-global-ticket-lifecycle-policy "15.5. Configuring the global ticket lifecycle policy")
-   [Configuring global ticket policies per authentication indicator](#configuring-global-ticket-policies-per-authentication-indicator "15.6. Configuring global ticket policies per authentication indicator")

### [15.9. Authentication indicator options for the krbtpolicy-mod command](#authentication-indicator-options-for-the-krbtpolicy-mod-command) {#authentication-indicator-options-for-the-krbtpolicy-mod-command .title}

Configure different Kerberos ticket lifetime policies for each authentication method in Identity Management (IdM) using the `krbtpolicy-mod`{.literal} command. With this, you can set stricter expiration policies for weaker authentication methods and more permissive policies for stronger ones.

+--------------------------+--------------------------------+----------------------------------+
| Authentication indicator | Argument for maximum lifetime  | Argument for maximum renewal age |
+:=========================+:===============================+:=================================+
| `otp`{.literal}          | `--otp-maxlife`{.literal}      | `--otp-maxrenew`{.literal}       |
+--------------------------+--------------------------------+----------------------------------+
| `radius`{.literal}       | `--radius-maxlife`{.literal}   | `--radius-maxrenew`{.literal}    |
+--------------------------+--------------------------------+----------------------------------+
| `pkinit`{.literal}       | `--pkinit-maxlife`{.literal}   | `--pkinit-maxrenew`{.literal}    |
+--------------------------+--------------------------------+----------------------------------+
| `hardened`{.literal}     | `--hardened-maxlife`{.literal} | `--hardened-maxrenew`{.literal}  |
+--------------------------+--------------------------------+----------------------------------+

: Table 15.1. Authentication indicator options for the krbtpolicy-mod command

Show more

## [Chapter 16. Kerberos PKINIT authentication in IdM](#kerberos-pkinit-authentication-in-idm) {#chapter-16.-kerberos-pkinit-authentication-in-idm .title}

Use Public Key Cryptography for Initial Authentication in Kerberos (PKINIT) to authenticate to Identity Management (IdM) using certificates instead of passwords. PKINIT provides stronger authentication by using public key cryptography for Kerberos preauthentication.

### [16.1. Default PKINIT configuration](#default-pkinit-configuration) {#default-pkinit-configuration .title}

The default PKINIT configuration in Identity Management (IdM) varies based on your certificate authority configuration. This configuration determines how servers and clients authenticate by using public key cryptography.

+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| CA configuration                                          | PKINIT configuration                                                                                               |
+:==========================================================+:===================================================================================================================+
| Without a CA, no external PKINIT certificate provided     | Local PKINIT: IdM only uses PKINIT for internal purposes on servers.                                               |
+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Without a CA, external PKINIT certificate provided to IdM | IdM configures PKINIT by using the external Kerberos key distribution center (KDC) certificate and CA certificate. |
+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| With an Integrated CA                                     | IdM configures PKINIT by using the certificate signed by the IdM CA.                                               |
+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

: Table 16.1. Default PKINIT configuration in IdM

Show more

### [16.2. Displaying the current PKINIT configuration](#displaying-the-current-pkinit-configuration) {#displaying-the-current-pkinit-configuration .title}

Display PKINIT configuration settings in Identity Management (IdM) to verify that certificate-based authentication is properly configured. Checking PKINIT status helps troubleshoot authentication issues and validate security policies.

**Procedure**

-   To determine the PKINIT status in your domain, use the `ipa pkinit-status`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa pkinit-status
      Server name: server1.example.com
      PKINIT status: enabled
      [...output truncated...]
      Server name: server2.example.com
      PKINIT status: disabled
      [...output truncated...]
    ```

    The command displays the PKINIT configuration status as `enabled`{.literal} or `disabled`{.literal}:

    -   `enabled`{.literal}: PKINIT is configured using a certificate signed by the integrated IdM CA or an external PKINIT certificate.
    -   `disabled`{.literal}: IdM only uses PKINIT for internal purposes on IdM servers.

-   To list the IdM servers with active Kerberos key distribution centers (KDCs) that support PKINIT for IdM clients, use the `ipa config-show`{.literal} command on any server:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa config-show
      Maximum username length: 32
      Home directory base: /home
      Default shell: /bin/sh
      Default users group: ipausers
      [...output truncated...]
      IPA masters capable of PKINIT: server1.example.com
      [...output truncated...]
    ```

### [16.3. Configuring PKINIT in IdM](#configuring-pkinit-in-idm) {#configuring-pkinit-in-idm .title}

Enable PKINIT on Identity Management (IdM) servers to allow certificate-based Kerberos authentication. PKINIT strengthens security by using public key cryptography for initial authentication instead of passwords alone.

**Prerequisites**

-   Ensure that all IdM servers with a certificate authority (CA) installed are running on the same domain level.

**Procedure**

1.  Check if PKINIT is enabled on the server:

    ``` {.language-plaintext tabindex="-1"}
    # kinit admin

    Password for admin@IDM.EXAMPLE.COM:
    # ipa pkinit-status --server=server.idm.example.com
    1 server matched
    ----------------
    Server name: server.idm.example.com
    PKINIT status:enabled
    ----------------------------
    Number of entries returned 1
    ----------------------------
    ```

    If PKINIT is disabled, you will see the following output:

    ``` {.language-plaintext tabindex="-1"}
    # ipa pkinit-status --server server.idm.example.com
    -----------------
    0 servers matched
    -----------------
    ----------------------------
    Number of entries returned 0
    ----------------------------
    ```

    You can also use the command to find all the servers where PKINIT is enabled if you omit the `--server <server_fqdn>`{.literal} parameter.

2.  If you are using IdM without CA:

    a.  On the IdM server, install the CA certificate that signed the Kerberos key distribution center (KDC) certificate:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-cacert-manage install -t CT,C,C ca.pem
        ```

    b.  To update all IPA hosts, repeat the `ipa-certupdate`{.literal} command on all replicas and clients:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-certupdate
        ```

    c.  Check if the CA certificate has already been added using the `ipa-cacert-manage list`{.literal} command. For example:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-cacert-manage list
        CN=CA,O=Example Organization
        The ipa-cacert-manage command was successful
        ```

    d.  Use the `ipa-server-certinstall`{.literal} utility to install an external KDC certificate. The KDC certificate must meet the following conditions:

        -   It is issued with the common name `CN=`{.literal}*`fully_qualified_domain_name,certificate_subject_base`{.literal}*.

        -   It includes the Kerberos principal `krbtgt/`{.literal}*`REALM_NAME@REALM_NAME`{.literal}*.

        -   It contains the Object Identifier (OID) for KDC authentication: `1.3.6.1.5.2.3.5.`{.literal}

            ``` {.language-plaintext tabindex="-1"}
            # ipa-server-certinstall --kdc kdc.pem kdc.key

            # systemctl restart krb5kdc.service
            ```

    e.  See your PKINIT status:

        ``` {.language-plaintext tabindex="-1"}
        # ipa pkinit-status
          Server name: server1.example.com
          PKINIT status: enabled
          [...output truncated...]
          Server name: server2.example.com
          PKINIT status: disabled
          [...output truncated...]
        ```

3.  If you are using IdM with a CA certificate, enable PKINIT as follows:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-pkinit-manage enable
      Configuring Kerberos KDC (krb5kdc)
      [1/1]: installing X509 Certificate for PKINIT
      Done configuring Kerberos KDC (krb5kdc).
      The ipa-pkinit-manage command was successful
    ```

    If you are using an IdM CA, the command requests a PKINIT KDC certificate from the CA.

### [16.4. Additional resources](#kerberos-pkinit-authentication-in-idm_164-additional-resources) {#additional-resources-7 .title}

-   [PKINIT configuration](https://web.mit.edu/kerberos/krb5-1.13/doc/admin/pkinit.html)

## [Chapter 17. Maintaining IdM Kerberos keytab files](#maintaining-idm-kerberos-keytab-files) {#chapter-17.-maintaining-idm-kerberos-keytab-files .title}

Maintain Identity Management (IdM) Kerberos keytab files to ensure services can authenticate securely with Kerberos.

You can use this information to understand why you should protect these sensitive files, and to troubleshoot communication issues between IdM services.

### [17.1. How Identity Management uses Kerberos keytab files](#how-identity-management-uses-kerberos-keytab-files) {#how-identity-management-uses-kerberos-keytab-files .title}

To authenticate users, hosts, and services to the KDC without human interaction, you can use Identity Management (IdM) Kerberos keytab files. This simplifies service authentication, maintenance, and troubleshooting.

A Kerberos keytab is a file containing Kerberos principals and their corresponding encryption keys.

Every IdM service on an IdM server has a unique Kerberos principal stored in the Kerberos database. For example, if IdM servers `east.idm.example.com`{.literal} and `west.idm.example.com`{.literal} provide DNS services, IdM creates 2 unique DNS Kerberos principals to identify these services, which follow the naming convention `<service>/host.domain.com@REALM.COM`{.literal}:

-   `DNS/east.idm.example.com@IDM.EXAMPLE.COM`{.literal}
-   `DNS/west.idm.example.com@IDM.EXAMPLE.COM`{.literal}

IdM creates a keytab on the server for each of these services to store a local copy of the Kerberos keys, along with their Key Version Numbers (KVNO). For example, the default keytab file `/etc/krb5.keytab`{.literal} stores the `host`{.literal} principal, which represents that machine in the Kerberos realm and is used for login authentication. The KDC generates encryption keys for the different encryption algorithms it supports, such as `aes256-cts-hmac-sha1-96`{.literal} and `aes128-cts-hmac-sha1-96`{.literal}.

You can display the contents of a keytab file with the `klist`{.literal} command:

``` {.language-plaintext tabindex="-1"}
[root@idmserver ~]# klist -ekt /etc/krb5.keytab
Keytab name: FILE:/etc/krb5.keytab
KVNO Timestamp           Principal
---- ------------------- ------------------------------------------------------
   2 02/24/2022 20:28:09 host/idmserver.idm.example.com@IDM.EXAMPLE.COM (aes256-cts-hmac-sha1-96)
   2 02/24/2022 20:28:09 host/idmserver.idm.example.com@IDM.EXAMPLE.COM (aes128-cts-hmac-sha1-96)
   2 02/24/2022 20:28:09 host/idmserver.idm.example.com@IDM.EXAMPLE.COM (camellia128-cts-cmac)
   2 02/24/2022 20:28:09 host/idmserver.idm.example.com@IDM.EXAMPLE.COM (camellia256-cts-cmac)
```

**Additional resources**

-   [Verifying that Kerberos keytab files are in sync with the IdM database](#verifying-that-kerberos-keytab-files-are-in-sync-with-the-idm-database "17.2. Verifying that Kerberos keytab files are in sync with the IdM database")
-   [List of IdM Kerberos keytab files and their contents](#list-of-idm-kerberos-keytab-files-and-their-contents "17.3. List of IdM Kerberos keytab files and their contents")

### [17.2. Verifying that Kerberos keytab files are in sync with the IdM database](#verifying-that-kerberos-keytab-files-are-in-sync-with-the-idm-database) {#verifying-that-kerberos-keytab-files-are-in-sync-with-the-idm-database .title}

Verify that Kerberos keytab files on an Identity Management (IdM) server are in sync with the IdM database to fix service authentication failures caused by outdated Key Version Numbers (KVNOs).

When you change a Kerberos password, IdM automatically generates a new key and increments its KVNO. If a keytab is not updated accordingly, services that rely on it cannot authenticate to the Kerberos Key Distribution Center (KDC). If an IdM service cannot communicate with another service, a stale keytab is a likely cause.

**Prerequisites**

-   You must authenticate as the IdM admin account to retrieve keytab files
-   You must authenticate as the `root`{.literal} account to modify keytab files owned by other users

**Procedure**

1.  Display the KVNO of the principals in the keytab you are verifying. In the following example, the `/etc/named.keytab`{.literal} file has the key for the `DNS/server1.idm.example.com@EXAMPLE.COM`{.literal} principal with a KVNO of 2.

    ``` {.language-plaintext tabindex="-1"}
    [root@server1 ~]# klist -ekt /etc/named.keytab
    Keytab name: FILE:/etc/named.keytab
    KVNO Timestamp           Principal
    ---- ------------------- ------------------------------------------------------
       2 11/26/2021 13:51:11 DNS/server1.idm.example.com@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
       2 11/26/2021 13:51:11 DNS/server1.idm.example.com@EXAMPLE.COM (aes128-cts-hmac-sha1-96)
       2 11/26/2021 13:51:11 DNS/server1.idm.example.com@EXAMPLE.COM (camellia128-cts-cmac)
       2 11/26/2021 13:51:11 DNS/server1.idm.example.com@EXAMPLE.COM (camellia256-cts-cmac)
    ```

2.  Display the KVNO of the principal stored in the IdM database. In this example, the KVNO of the key in the IdM database does not match the KVNO in the keytab.

    ``` {.language-plaintext tabindex="-1"}
    [root@server1 ~]# kvno DNS/server1.idm.example.com@EXAMPLE.COM
    DNS/server1.idm.example.com@EXAMPLE.COM: kvno = 3
    ```

3.  Authenticate as the IdM admin account.

    ``` {.language-plaintext tabindex="-1"}
    [root@server1 ~]# kinit admin
    Password for admin@IDM.EXAMPLE.COM:
    ```

4.  Retrieve an updated Kerberos key for the principal and store it in its keytab. Perform this step as the `root`{.literal} user so you can modify the `/etc/named.keytab`{.literal} file, which is owned by the `named`{.literal} user.

    ``` {.language-plaintext tabindex="-1"}
    [root@server1 ~]# ipa-getkeytab -s server1.idm.example.com -p DNS/server1.idm.example.com -k /etc/named.keytab
    ```

**Verification**

1.  Display the updated KVNO of the principal in the keytab.

    ``` {.language-plaintext tabindex="-1"}
    [root@server1 ~]# klist -ekt /etc/named.keytab
    Keytab name: FILE:/etc/named.keytab
    KVNO Timestamp           Principal
    ---- ------------------- ------------------------------------------------------
       4 08/17/2022 14:42:11 DNS/server1.idm.example.com@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
       4 08/17/2022 14:42:11 DNS/server1.idm.example.com@EXAMPLE.COM (aes128-cts-hmac-sha1-96)
       4 08/17/2022 14:42:11 DNS/server1.idm.example.com@EXAMPLE.COM (camellia128-cts-cmac)
       4 08/17/2022 14:42:11 DNS/server1.idm.example.com@EXAMPLE.COM (camellia256-cts-cmac)
    ```

2.  Display the KVNO of the principal stored in the IdM database and ensure it matches the KVNO from the keytab.

    ``` {.language-plaintext tabindex="-1"}
    [root@server1 ~]# kvno DNS/server1.idm.example.com@EXAMPLE.COM
    DNS/server1.idm.example.com@EXAMPLE.COM: kvno = 4
    ```

**Additional resources**

-   [How Identity Management uses Kerberos keytab files](#how-identity-management-uses-kerberos-keytab-files "17.1. How Identity Management uses Kerberos keytab files")
-   [List of IdM Kerberos keytab files and their contents](#list-of-idm-kerberos-keytab-files-and-their-contents "17.3. List of IdM Kerberos keytab files and their contents")

### [17.3. List of IdM Kerberos keytab files and their contents](#list-of-idm-kerberos-keytab-files-and-their-contents) {#list-of-idm-kerberos-keytab-files-and-their-contents .title}

Reference keytab file locations and their associated principals to understand which services use which authentication credentials in Identity Management (IdM). This information helps troubleshoot authentication issues and verify service configurations.

+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Keytab location                                                                 | Contents                                                                                                   | Purpose                                                                                               |
+:================================================================================+:===========================================================================================================+:======================================================================================================+
| `/etc/krb5.keytab`{.literal}                                                    | `host`{.literal} principal                                                                                 | Verifying user credentials when logging in, used by NFS if there is no `nfs`{.literal} principal      |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| `/etc/dirsrv/ds.keytab`{.literal}                                               | `ldap`{.literal} principal                                                                                 | Authenticating users to the IdM database, securely replicating database contents between IdM replicas |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| `/var/lib/ipa/gssproxy/http.keytab`{.literal}                                   | `HTTP`{.literal} principal                                                                                 | Authenticating to the Apache server                                                                   |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| `/etc/named.keytab`{.literal}                                                   | `DNS`{.literal} principal                                                                                  | Securely updating DNS records                                                                         |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| `/etc/ipa/dnssec/ipa-dnskeysyncd.keytab`{.literal}                              | `ipa-dnskeysyncd`{.literal} principal                                                                      | Keeping OpenDNSSEC synchronized with LDAP                                                             |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| `/etc/pki/pki-tomcat/dogtag.keytab`{.literal}                                   | `dogtag`{.literal} principal                                                                               | Communicating with the Certificate Authority (CA)                                                     |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| `/etc/samba/samba.keytab`{.literal}                                             | `cifs`{.literal} and `host`{.literal} principals                                                           | Communicating with the Samba service                                                                  |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| `/var/lib/sss/keytabs/`{.literal}*`ad-domain.com`{.literal}*`.keytab`{.literal} | Active Directory (AD) domain controller (DCs) principals in the form *`HOSTNAME$@AD-DOMAIN.COM`{.literal}* | Communicating with AD DCs through an IdM-AD Trust                                                     |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

: Table 17.1. Table

Show more

**Additional resources**

-   [How Identity Management uses Kerberos keytab files](#how-identity-management-uses-kerberos-keytab-files "17.1. How Identity Management uses Kerberos keytab files")
-   [Verifying that Kerberos keytab files are in sync with the IdM database](#verifying-that-kerberos-keytab-files-are-in-sync-with-the-idm-database "17.2. Verifying that Kerberos keytab files are in sync with the IdM database")

### [17.4. Viewing the encryption type of your IdM master key](#viewing-the-encryption-type-of-your-idm-master-key) {#viewing-the-encryption-type-of-your-idm-master-key .title}

View the encryption type of the Identity Management (IdM) master key to determine whether your deployment is compatible with FIPS standards.

The master key is the key the IdM KDC uses to encrypt all other Kerberos principals when storing them at rest. As of RHEL 8.7, the encryption type is `aes256-cts-hmac-sha384-192`{.literal}. This encryption type is compatible with the default RHEL 9 FIPS cryptographic policy aiming to comply with FIPS 140-3.

The encryption types used on previous RHEL versions are not compatible with RHEL 9 systems that adhere to FIPS 140-3 standards. To make RHEL 9 systems compatible with a RHEL 8 FIPS 140-2 deployment, see the [AD Domain Users unable to login in to the FIPS-compliant environment](https://access.redhat.com/solutions/7003853) KCS solution.

**Prerequisites**

-   You have `root`{.literal} access to any of the RHEL 8 replicas in the IdM deployment.

**Procedure**

-   On the replica, view the encryption type on the command line:

    ``` {.language-plaintext tabindex="-1"}
    # kadmin.local getprinc K/M | grep -E '^Key:'
    Key: vno 1, aes256-cts-hmac-sha1-96
    ```

    The `aes256-cts-hmac-sha1-96`{.literal} key in the output indicates that the IdM deployment was installed on a server that was running RHEL 8.6 or earlier. The presence of a `aes256-cts-hmac-sha384-192`{.literal} key in the output would indicate that the IdM deployment was installed on a server that was running RHEL 8.7 or later.

## [Chapter 18. Managing Kerberos flags](#managing-kerberos-flags) {#chapter-18.-managing-kerberos-flags .title}

Manage Kerberos flags for service and host principals in Identity Management (IdM) to control delegation behavior, pre-authentication requirements, and ticket issuance. You can view and configure flags from the command line or the IdM Web UI.

### [18.1. Kerberos flags for services and hosts](#kerberos-flags-for-services-and-hosts) {#kerberos-flags-for-services-and-hosts .title}

Kerberos flags define specific aspects of ticket behavior for service and host principals in Identity Management (IdM). Configure flags such as `OK_AS_DELEGATE`{.literal}, `REQUIRES_PRE_AUTH`{.literal}, and `OK_TO_AUTH_AS_DELEGATE`{.literal} to control delegation, pre-authentication requirements, and constrained delegation.

Principals in IdM accept the following Kerberos flags:

-   `OK_AS_DELEGATE`{.literal}

    Use this flag to specify Kerberos tickets trusted for delegation.

    Active directory (AD) clients check the `OK_AS_DELEGATE`{.literal} flag on the Kerberos ticket to determine whether a user credentials can be forwarded or delegated to a specific server. AD forwards the ticket-granting ticket (TGT) only to services or hosts with `OK_AS_DELEGATE`{.literal} configured. With this flag, system security services daemon (SSSD) can add the AD user TGT to the default Kerberos credentials cache on the IdM client machine.

-   `REQUIRES_PRE_AUTH`{.literal}

    Use this flag to specify that only pre-authenticated tickets are allowed to authenticate to a principal.

    With the `REQUIRES_PRE_AUTH`{.literal} flag set, the key distribution center (KDC) requires additional authentication: the KDC issues the TGT for the principal with `REQUIRES_PRE_AUTH`{.literal} only if the TGT has been pre-authenticated.

    You can clear `REQUIRES_PRE_AUTH`{.literal} to disable pre-authentication for selected services or hosts. This lowers the load on the KDC, however slightly increases the possibility of a brute-force attack on a long-term key to succeed.

-   `OK_TO_AUTH_AS_DELEGATE`{.literal}

    Use the `OK_TO_AUTH_AS_DELEGATE`{.literal} flag to specify that the service is allowed to obtain a Kerberos ticket on behalf of a user. Note, that for obtaining other tickets on behalf of the user, the service needs the `OK_AS_DELEGATE`{.literal} flag and a corresponding policy decision allowed on the key distribution center side.

### [18.2. Displaying Kerberos flags from the command line](#displaying-kerberos-flags-from-the-command-line) {#displaying-kerberos-flags-from-the-command-line .title}

Display Kerberos flag settings for a service principal using the `kvno`{.literal} and `klist`{.literal} commands to verify which flags are enabled.

**Procedure**

1.  To find out if `OK_AS_DELEGATE`{.literal} is set for a principal, run the `kvno`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    $ kvno demo/ipa.example.com@EXAMPLE.COM
    ```

2.  To display the flag setting, run the `klist -f`{.literal} command. The `0`{.literal} character means that the `OK_AS_DELEGATE`{.literal} flag is disabled:

    ``` {.language-plaintext tabindex="-1"}
    $ klist -f
    Ticket cache: KEYRING:persistent:0:0
    Default principal: admin@EXAMPLE.COM

    Valid starting      Expires         Service principal
    02/19/2024 09:59:02 02/20/2024 08:21:33 demo/ipa/example.com@EXAMPLE.COM
        Flags: FATO
    ```

### [18.3. Setting and removing Kerberos flags from the command line](#setting-and-removing-kerberos-flags-from-the-command-line) {#setting-and-removing-kerberos-flags-from-the-command-line .title}

Set or remove Kerberos flags for a service principal using the `ipa service-mod`{.literal} command to control delegation and pre-authentication behavior.

The `ipa service-mod`{.literal} command uses the following command options for the flags:

-   `--ok-as-delegate`{.literal} for `OK_AS_DELEGATE`{.literal}
-   `--requires-pre-auth`{.literal} for `REQUIRES_PRE_AUTH`{.literal}
-   `--ok-to-auth-as-delegate`{.literal} for `OK_TO_AUTH_AS_DELEGATE`{.literal}

By setting an option value to `1`{.literal}, you enable a flag for a principle. By setting an option value to `0`{.literal}, you disable the flag.

The following procedure enables and disables the `OK_AS_DELEGATE`{.literal} flag for the `service/ipa.example.com@example.com`{.literal} principal.

**Procedure**

-   To add the `OK_AS_DELEGATE`{.literal} flag for the `service/ipa.example.com@example.com`{.literal} principle, run:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa service-mod service/ipa.example.com@EXAMPLE.COM --ok-as-delegate=1
    ```

-   To remove the `OK_AS_DELEGATE`{.literal} flag from the `service/ipa.example.com@example.com`{.literal} principle, run:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa service-mod service/ipa.example.com@EXAMPLE.COM --ok-as-delegate=0
    ```

### [18.4. Setting Kerberos flags from the Web UI](#setting-kerberos-flags-from-the-web-ui) {#setting-kerberos-flags-from-the-web-ui .title}

Set Kerberos flags for a service principal using the IdM Web UI to control delegation and pre-authentication behavior.

**Procedure**

1.  Select Identity → Services in the menu.

2.  Click on the service to which you want to add the flags.

3.  Check the option that you want to set:

    -   To set the `OK_AS_DELEGATE`{.literal} flag, check **Trusted for delegation**.
    -   To set the `REQUIRES_PRE_AUTH`{.literal} flag, check **Requires pre-authentication**.
    -   To set the `OK_TO_AUTH_AS_DELEGATE`{.literal} flag, check **Trusted to authenticate as user**.

## [Chapter 19. Enabling passkey authentication in IdM environment](#enabling-passkey-authentication-in-idm-environment) {#chapter-19.-enabling-passkey-authentication-in-idm-environment .title}

Enable passkey authentication in your Identity Management (IdM) environment to provide passwordless and multi-factor authentication using FIDO2-compatible devices. Passkey authentication strengthens security by requiring a hardware device with PIN or biometric verification.

This authentication method helps comply with regulatory standards by adding an additional security layer through the combination of hardware (passkey device) and software (IdM passkey enablement). This is particularly valuable in environments where data protection is critical.

If your system is connected to a network with the IdM environment, the passkey authentication method issues a Kerberos ticket automatically, which enables single sign-on (SSO) for an IdM user.

You can use passkey to authenticate through the graphical interface to your operating system. If your system allows you to authenticate with passkey and password, you can skip passkey authentication and authenticate with the password by pressing **Space** on your keyboard followed by the **Enter** key. If you use GNOME Display Manager (GDM), you can press **Enter** to bypass the passkey authentication.

Note that, currently, the passkey authentication in the IdM environment does not support FIDO2 attestation mechanism, which allows for the identification of the particular passkey device.

The following procedures provide instructions on managing and configuring passkey authentication in an IdM environment.

### [19.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   You have a passkey device.

-   Install the `fido2-tools`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install fido2-tools
    ```

-   Set the PIN for the passkey device:

    1.  Connect the passkey device to the USB port.

    2.  List the connected passkey devices:

        ``` {.language-plaintext tabindex="-1"}
        # fido2-token -L
        ```

    3.  Set the PIN for your passkey device by following the command prompts.

        ``` {.language-plaintext tabindex="-1"}
        # fido2-token -C passkey_device
        ```

-   You have installed the `sssd-passkey`{.literal} package.

### [19.2. Registering a passkey device](#registering-a-passkey-device) {#registering-a-passkey-device .title}

Register FIDO2-compatible passkey devices like YubiKey for authentication to Identity Management (IdM). Passkey authentication eliminates password vulnerabilities and provides hardware-backed security for user logins.

**Prerequisites**

-   The PIN for the passkey device is set.

-   Passkey authentication is enabled for an IdM user:

    ``` {.language-plaintext tabindex="-1"}
    # ipa user-add user01 --first=user --last=01 --user-auth-type=passkey
    ```

    Use the `ipa user-mod`{.literal} with the same `--user-auth-type=passkey`{.literal} parameter for an existing IdM user.

-   Access to the physical machine to which the user wants to authenticate.

**Procedure**

1.  Insert the passkey device in the USB port.

2.  Register the passkey for the IdM user:

    ``` {.language-plaintext tabindex="-1"}
    # ipa user-add-passkey user01 --register
    ```

    Follow the application prompts:

    a.  Enter the PIN for the passkey device.

    b.  Touch the device to verify your identity. If you are using a biometric device, ensure to use the same finger with which you registered the device.

        Tip

        It is good practice for users to configure multiple passkey devices as a backup that allows authentication from multiple locations or devices. To ensure the Kerberos ticket is issued during authentication, do not configure more than 12 passkey devices for a user.

**Verification**

1.  Log in to the system with the username you have configured to use passkey authentication. The system prompts you to insert the passkey device:

    ``` {.language-plaintext tabindex="-1"}
    Insert your passkey device, then press ENTER.
    ```

2.  Insert the passkey device into the USB port and enter your PIN when prompted:

    ``` {.language-plaintext tabindex="-1"}
    Enter PIN:
    Creating home directory for user01@example.com.
    ```

3.  Confirm the Kerberos ticket is issued:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    Default principal: user01@IPA.EXAMPLE.COM
    ```

Note, to skip passkey authentication, enter any character in the prompt or enter an empty PIN if user authentication is enabled. The system redirects you to password based authentication.

Note

If you enter the PIN for your passkey device incorrectly 3 times, disconnect the physical token and reconnect it to the USB port and perform a successful authentication. If you do not complete a power cycle, you will not be able to authenticate even if you enter the PIN correctly.

### [19.3. Authentication policies](#authentication-policies) {#authentication-policies .title}

Configure authentication policies in Identity Management (IdM) to control which authentication methods are available for online and offline access. This helps you to enforce security requirements and support diverse authentication scenarios.

Authentication with online connection
:   Uses all online authentication methods that the service provides on the server side. For IdM, AD, or Kerberos services, the default authentication method is Kerberos.

Authentication without online connection
:   Uses authentication methods that are available for a user. You can tune the authentication method with the `local_auth_policy`{.literal} option.

Use the `local_auth_policy`{.literal} option in the `/etc/sssd/sssd.conf`{.literal} file to configure the available online and offline authentication methods. By default, the authentication is performed only with the methods that the server side of the service supports. You can tune the policy with the following values:

-   The `match`{.literal} value enables the matching of offline and online states. For example, the IdM server supports online passkey authentication and `match`{.literal} enables offline and online authentications for the passkey method.
-   The `only`{.literal} value offers only offline methods and ignores the online methods.
-   The `enable`{.literal} and `disable`{.literal} values explicitly define the methods for offline authentication. For example, `enable:passkey`{.literal} enables only passkey for offline authentication.

The following configuration example allows local users to authenticate locally using smart card authentication:

``` {.language-plaintext tabindex="-1"}
[domain/shadowutils]
id_provider = proxy
proxy_lib_name = files
auth_provider = none
local_auth_policy = only
```

The `local_auth_policy`{.literal} option applies to the passkey and smart card authentication methods.

### [19.4. Retrieving an IdM ticket-granting ticket as a passkey user](#retrieving-an-idm-ticket-granting-ticket-as-a-passkey-user) {#retrieving-an-idm-ticket-granting-ticket-as-a-passkey-user .title}

Retrieve a Kerberos ticket-granting ticket (TGT) as a passkey user in Identity Management (IdM) to authenticate securely using your hardware passkey device.

The process uses a Flexible Authentication via Secure Tunneling (FAST) channel to provide a secure connection between the Kerberos client and Kerberos Distribution Center (KDC).

**Prerequisites**

-   You registered your passkey device and configured your authentication policies.

**Procedure**

1.  Initialize the credentials cache by running the following command:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# kinit -n @IDM.EXAMPLE.COM -c FILE:armor.ccache
    ```

    Note that this command creates the armor.ccache file that you need to point to whenever you request a new Kerberos ticket.

2.  Request a Kerberos ticket by running the command:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# kinit -T FILE:armor.ccache <username>@IDM.EXAMPLE.COM
    Enter your PIN:
    ```

    Note

    If you enter the PIN for your passkey device incorrectly 3 times, disconnect the physical token and reconnect it to the USB port and perform a successful authentication. If you do not complete a power cycle, you will not be able to authenticate even if you enter the PIN correctly.

**Verification**

-   Display your Kerberos ticket information:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# klist -C
    Ticket cache: KCM:0:58420
    Default principal: <username>@IDM.EXAMPLE.COM

    Valid starting     Expires            Service principal
    05/09/22 07:48:23  05/10/22 07:03:07  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: fast_avail(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = yes
    08/17/2022 20:22:45  08/18/2022 20:22:43  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: pa_type(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = 153
    ```

    The `pa_type = 153`{.literal} indicates passkey authentication.

## [Chapter 20. Enabling authentication mechanism selection in GDM using SSSD](#authentication-mechanism-selection-in-gdm) {#chapter-20.-enabling-authentication-mechanism-selection-in-gdm-using-sssd .title}

Strengthen organizational security by enabling passwordless GDM authentication for managed users. Replace traditional password-based authentication with external identity providers (EIdP), passkey devices, or smart cards and switch between these methods on the GNOME Display Manager login screen.

Important

Passwordless GDM is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

### [20.1. Passwordless authentication for centrally managed users in GDM](#passwordless-authentication-for-centrally-managed-users-in-gdm) {#passwordless-authentication-for-centrally-managed-users-in-gdm .title}

Passwordless GDM authentication is a technology preview feature that provides several methods for logging in through the GNOME Display Manager (GDM) without a traditional password.

Depending on the system configuration, you can use the following authentication methods:

External identity providers (EIdP)
:   You can use providers such as Keycloak, Google, Microsoft, or GitHub for a unified login experience.

Passkey devices
:   You can use passwordless authentication using FIDO2-compatible devices like YubiKey.

Smart cards
:   You can use physical smart cards.

When the administrator configures multiple authentication methods for users, users can switch between these methods on the GDM login screen.

#### [20.1.1. Current limitations](#current_limitations) {#current-limitations .title}

When using these authentication methods, users might encounter the following behaviors:

EIdP priority over passkey
:   If an administrator configures both an EIdP and a passkey for a user, the IdM server, specifically the KDC, announces only the EIdP. Consequently, the GDM login screen displays only the EIdP option and does not show the passkey.

PIN prompts for passkey devices
:   GDM always prompts the user for a PIN when using a passkey, even if the passkey does not require one. In these cases, a touch is enough to authenticate. The PIN prompt ensures the user is ready to touch the device before the short authentication window expires. Additionally, the interface does not display the number of remaining PIN attempts.

Passkey availability in non-IdM environments
:   If the system is not enrolled in an IdM domain, SELinux security policies might prevent the passkey service from starting. In these environments, the passkey authentication method does not function and the option does not appear on the GDM login screen.

Smart card detection
:   The login option for smart cards only appears in the GDM menu when the user inserts a smart card that contains a valid certificate for their specific account into the reader.

**Additional resources**

-   [Supported smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/understanding-smart-card-authentication#supported-smart-cards)

### [20.2. Enabling authentication mechanism selection in GDM using SSSD](#enabling-authentication-mechanism-selection-in-gdm-using-sssd) {#enabling-authentication-mechanism-selection-in-gdm-using-sssd .title}

Enable credential switching in GNOME Display Manager (GDM) using System Security Services Daemon (SSSD) and authselect. Centrally managed users can then choose between passwordless login options, such as smart cards, passkeys, or external identity providers (EIdP), directly at the login screen.

Before enabling these options in GDM, you must first configure the individual authentication methods and the Identity Management (IdM) server. After these credentials and server-side settings are functional, you can configure the system services to display these options at the login screen.

**Prerequisites**

-   The system is a member of an Identity Management (IdM) domain.
-   You have fulfilled the prerequisites for the specific passwordless authentication methods you want to use, such as configuring the IdM server and enrolling user credentials.
-   You have `root`{.literal} privileges on the system.
-   Have SSSD installed.

**Procedure**

1.  (Optional): View the information about your `authselect`{.literal} profile:

    ``` {.language-plaintext tabindex="-1"}
    $ authselect current
    ```

2.  Depending on your current `authselect`{.literal} profile, do one of the following:

    a.  Select the `sssd`{.literal} profile and enable the switchable authentication feature:

        ``` {.language-plaintext tabindex="-1"}
        # authselect select sssd with-switchable-auth
        ```

    b.  If you are already using the `sssd`{.literal} profile, enable the switchable authentication feature:

        ``` {.language-plaintext tabindex="-1"}
        # authselect enable-feature with-switchable-auth
        ```

        Note

        This command configures the `/etc/pam.d/switchable-auth`{.literal} PAM service file to enable the GDM login screen to display the corresponding passwordless mechanisms that you have previously configured for the user account.

3.  Configure the SSSD PAM responder to authorize the switchable authentication service. Open the `/etc/sssd/sssd.conf`{.literal} file and add the `pam_json_services`{.literal} option to the `[pam]`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    ...
    [pam]
    pam_json_services = gdm-switchable-auth
    ```

4.  Restart the SSSD service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

-   As an administrator, verify the `/etc/sssd/sssd.conf`{.literal} file to confirm the configuration:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /etc/sssd/sssd.conf
    ```

    The output must include the `pam_json_services`{.literal} key set to `gdm-switchable-auth`{.literal} within the `[pam]`{.literal} section.

-   As a user, you can read the `/etc/dconf/db/distro.d/20-authselect`{.literal} file to confirm the configuration:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /etc/dconf/db/distro.d/20-authselect
    ```

    The `[org/gnome/login-screen]`{.literal} section in the output must include the `enable-switchable-authentication`{.literal} key set to `true`{.literal}.

**Additional resources**

-   [Configuring Identity Management for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-server-for-smart-card-authentication)
-   [Configuring smart card authentication using authselect](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-smart-card-authentication-using-authselect)
-   [Enabling passkey authentication in IdM environment](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/enabling-passkey-authentication-in-idm-environment)
-   [Using external identity providers to authenticate to IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/using-external-identity-providers-to-authenticate-to-idm)

## [Chapter 21. Using the KDC Proxy in IdM](#using-the-kdc-proxy-in-idm) {#chapter-21.-using-the-kdc-proxy-in-idm .title}

Some administrators might choose to make the default Kerberos ports inaccessible in their deployment. To allow users, hosts, and services to obtain Kerberos credentials, you can use the `HTTPS`{.literal} service as a proxy that communicates with Kerberos via the `HTTPS`{.literal} port 443.

In Identity Management (IdM), the **Kerberos Key Distribution Center Proxy** (KKDCP) provides this functionality.

On an IdM server, KKDCP is enabled by default and available at `https://`{.literal}*`<server.idm.example.com>`{.literal}*`/KdcProxy`{.literal}. On an IdM client, you must change its Kerberos configuration to access the KKDCP.

### [21.1. Configuring an IdM client to use KKDCP](#configuring-an-idm-client-to-use-kkdcp) {#configuring-an-idm-client-to-use-kkdcp .title}

Configure Identity Management (IdM) clients to use Kerberos Key Distribution Center Proxy (KKDCP) to access Kerberos services through HTTPS port 443. This enables authentication when standard Kerberos ports are blocked by firewalls or network policies.

**Prerequisites**

-   You have `root`{.literal} access to the IdM client.

**Procedure**

1.  Open the `/etc/krb5.conf`{.literal} file for editing.

2.  In the `[realms]`{.literal} section, enter the URL of the KKDCP for the `kdc`{.literal}, `admin_server`{.literal}, and `kpasswd_server`{.literal} options:

    ``` {.language-plaintext tabindex="-1"}
    [realms]
    EXAMPLE.COM = {
      kdc = https://kdc.example.com/KdcProxy
      admin_server = https://kdc.example.com/KdcProxy
      kpasswd_server = https://kdc.example.com/KdcProxy
      default_domain = example.com
    }
    ```

    For redundancy, you can add the parameters `kdc`{.literal}, `admin_server`{.literal}, and `kpasswd_server`{.literal} multiple times to indicate different KKDCP servers.

3.  Restart the `sssd`{.literal} service to make the changes take effect:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

### [21.2. Verifying that KKDCP is enabled on an IdM server](#verifying-that-kkdcp-is-enabled-on-an-idm-server) {#verifying-that-kkdcp-is-enabled-on-an-idm-server .title}

Verify that the Kerberos Key Distribution Center Proxy (KKDCP) is enabled on an Identity Management (IdM) server to confirm that Kerberos clients can authenticate through the HTTPS proxy rather than connecting directly to the KDC.

On an IdM server, KKDCP is automatically enabled each time the Apache web server starts if the attribute and value pair `ipaConfigString=kdcProxyEnabled`{.literal} exists in the directory. When enabled, the symbolic link `/etc/httpd/conf.d/ipa-kdc-proxy.conf`{.literal} is created.

You can verify if the KKDCP is enabled on the IdM server, even as an unprivileged user.

**Procedure**

-   Check that the symbolic link exists:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -l /etc/httpd/conf.d/ipa-kdc-proxy.conf
    lrwxrwxrwx. 1 root root 36 Jun 21  2020 /etc/httpd/conf.d/ipa-kdc-proxy.conf -> /etc/ipa/kdcproxy/ipa-kdc-proxy.conf
    ```

    The output confirms that KKDCP is enabled.

### [21.3. Disabling KKDCP on an IdM server](#disabling-kkdcp-on-an-idm-server) {#disabling-kkdcp-on-an-idm-server .title}

Disable the Kerberos Key Distribution Center Proxy (KKDCP) on Identity Management (IdM) servers to switch to direct KDC connectivity.

**Prerequisites**

-   You have `root`{.literal} access to the IdM server.

**Procedure**

1.  Remove the `ipaConfigString=kdcProxyEnabled`{.literal} attribute and value pair from the directory:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-ldap-updater /usr/share/ipa/kdcproxy-disable.uldif
    Update complete
    The ipa-ldap-updater command was successful
    ```

2.  Restart the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart httpd.service
    ```

    KKDCP is now disabled on the current IdM server.

**Verification**

-   Verify that the symbolic link does not exist:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -l /etc/httpd/conf.d/ipa-kdc-proxy.conf
    ls: cannot access '/etc/httpd/conf.d/ipa-kdc-proxy.conf': No such file or directory
    ```

### [21.4. Re-enabling KKDCP on an IdM server](#re-enabling-kkdcp-on-an-idm-server) {#re-enabling-kkdcp-on-an-idm-server .title}

Restore Kerberos Key Distribution Center Proxy (KKDCP) functionality on an Identity Management (IdM) server to enable clients to obtain Kerberos tickets through HTTPS.

**Prerequisites**

-   You have `root`{.literal} access to the IdM server.

**Procedure**

1.  Add the `ipaConfigString=kdcProxyEnabled`{.literal} attribute and value pair to the directory:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-ldap-updater /usr/share/ipa/kdcproxy-enable.uldif
    Update complete
    The ipa-ldap-updater command was successful
    ```

2.  Restart the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart httpd.service
    ```

    KKDCP is now enabled on the current IdM server.

**Verification**

-   Verify that the symbolic link exists:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -l /etc/httpd/conf.d/ipa-kdc-proxy.conf
    lrwxrwxrwx. 1 root root 36 Jun 21  2020 /etc/httpd/conf.d/ipa-kdc-proxy.conf -> /etc/ipa/kdcproxy/ipa-kdc-proxy.conf
    ```

### [21.5. Configuring the KKDCP server for static targets](#configuring-the-kkdcp-server-for-static-targets) {#configuring-the-kkdcp-server-for-static-targets .title}

Configure the Identity Management (IdM) KKDCP server to use TCP when communicating with Active Directory realms. TCP transport improves reliability when connecting to multiple Kerberos servers in AD environments.

**Prerequisites**

-   You have `root`{.literal} access.

**Procedure**

1.  Set the `use_dns`{.literal} parameter in the `[global]`{.literal} section of the `/etc/ipa/kdcproxy/kdcproxy.conf`{.literal} file to **false**.

    ``` {.language-plaintext tabindex="-1"}
    [global]
    use_dns = false
    ```

2.  Put the proxied realm information into the `/etc/ipa/kdcproxy/kdcproxy.conf`{.literal} file. For example, for the \[AD.*EXAMPLE.COM*\] realm with proxy list the realm configuration parameters as follows:

    ``` {.language-plaintext tabindex="-1"}
    [AD.EXAMPLE.COM]
    kerberos = kerberos+tcp://1.2.3.4:88 kerberos+tcp://5.6.7.8:88
    kpasswd = kpasswd+tcp://1.2.3.4:464 kpasswd+tcp://5.6.7.8:464
    ```

    Important

    The realm configuration parameters must list multiple servers separated by a space, as opposed to `/etc/krb5.conf`{.literal} and `kdc.conf`{.literal}, in which certain options may be specified multiple times.

3.  Restart Identity Management (IdM) services:

    ``` {.language-plaintext tabindex="-1"}
    # ipactl restart
    ```

**Additional resources**

-   [Configure IPA server as a KDC Proxy for AD Kerberos communication (Red Hat Knowledgebase)](https://access.redhat.com/solutions/3347361)

### [21.6. Configuring the KKDCP server with the MIT Kerberos configuration](#configuring-the-kkdcp-server-with-the-mit-kerberos-configuration) {#configuring-the-kkdcp-server-with-the-mit-kerberos-configuration .title}

Configure the Identity Management (IdM) Kerberos Key Distribution Center Proxy (KKDCP) server to enable DNS-based KDC discovery for Active Directory (AD) realms declared in the MIT Kerberos configuration.

**Prerequisites**

-   You have `root`{.literal} access.
-   Your AD realms are declared in the MIT Kerberos configuration (`/etc/krb5.conf`{.literal} or `/etc/krb5.conf.d/`{.literal}).

**Procedure**

1.  In the `/etc/ipa/kdcproxy/kdcproxy.conf`{.literal} file, in the `[global]`{.literal} section, set `configs = mit`{.literal} and `use_dns = true`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [global]
    configs = mit
    use_dns = true
    ```

    The `configs = mit`{.literal} setting imports the MIT Kerberos configuration into kdcproxy, making realms declared there available for DNS-based KDC discovery.

2.  Optional: To re-enable DNS-based KDC discovery for all realms, add the `dns_realm_discovery`{.literal} parameter to the `[global]`{.literal} section.

    Warning

    Red Hat recommends against setting `dns_realm_discovery = true`{.literal}. It restores the pre-CVE-2025-59088 behavior and enables any client to trigger DNS SRV record lookups for arbitrary realm names, which can be exploited to probe internal network addresses and exfiltrate data through server-side request forgery.

    ``` {.language-plaintext tabindex="-1"}
    [global]
    configs = mit
    use_dns = true
    dns_realm_discovery = true
    ```

3.  Restart Identity Management (IdM) services:

    ``` {.language-plaintext tabindex="-1"}
    # ipactl restart
    ```

**Additional resources**

-   [Configure IPA server as a KDC Proxy for AD Kerberos communication (Red Hat Knowledgebase)](https://access.redhat.com/solutions/3347361)
-   [CVE-2025-59088 (Red Hat Security)](https://access.redhat.com/security/cve/cve-2025-59088)

### [21.7. Configuring the KKDCP server with explicit realm declarations](#configuring-the-kkdcp-server-with-explicit-realm-declarations) {#configuring-the-kkdcp-server-with-explicit-realm-declarations .title}

Configure the Identity Management (IdM) KKDCP server to enable DNS-based KDC discovery for Active Directory (AD) realms by declaring them explicitly in the kdcproxy configuration. Use this approach when your AD realms are not defined in the MIT Kerberos configuration, or when `configs = mit`{.literal} is not set.

**Prerequisites**

-   You have `root`{.literal} access.

**Procedure**

1.  In the `/etc/ipa/kdcproxy/kdcproxy.conf`{.literal} file, in the `[global]`{.literal} section, set the `use_dns`{.literal} parameter to **true**:

    ``` {.language-plaintext tabindex="-1"}
    [global]
    use_dns = true
    ```

2.  Add a dedicated section for each Active Directory realm that should use DNS-based KDC discovery. Empty sections are sufficient to add a realm to the allow-list. For example:

    ``` {.language-plaintext tabindex="-1"}
    [SUB1.AD.EXAMPLE.COM]
    [SUB2.AD.EXAMPLE.COM]
    ```

    To include all sub-realms within an AD forest without listing each one individually, use a wildcard section prefixed with `*`{.literal}. For example, `[*AD.`{.literal}*`EXAMPLE.COM`{.literal}*`]`{.literal} matches `AD.`{.literal}*`EXAMPLE.COM`{.literal}*, `SUB.AD.`{.literal}*`EXAMPLE.COM`{.literal}*, and any deeper subdomains within that forest, but does not match `MYAD.`{.literal}*`EXAMPLE.COM`{.literal}*:

    ``` {.language-plaintext tabindex="-1"}
    [*AD.EXAMPLE.COM]
    ```

3.  Optional: If you cannot add dedicated realm sections, you can re-enable DNS-based KDC discovery for all realms by adding the `dns_realm_discovery`{.literal} parameter to the `[global]`{.literal} section.

    Warning

    Red Hat recommends against setting `dns_realm_discovery = true`{.literal}. It restores the pre-CVE-2025-59088 behavior and enables any client to trigger DNS SRV record lookups for arbitrary realm names, which can be exploited to probe internal network addresses and exfiltrate data through server-side request forgery.

    ``` {.language-plaintext tabindex="-1"}
    [global]
    use_dns = true
    dns_realm_discovery = true
    ```

4.  Restart Identity Management (IdM) services:

    ``` {.language-plaintext tabindex="-1"}
    # ipactl restart
    ```

**Additional resources**

-   [Configure IPA server as a KDC Proxy for AD Kerberos communication (Red Hat Knowledgebase)](https://access.redhat.com/solutions/3347361)
-   [CVE-2025-59088 (Red Hat Security)](https://access.redhat.com/security/cve/cve-2025-59088)

## [Chapter 22. Access control in IdM](#access-control-in-idm) {#chapter-22.-access-control-in-idm .title}

Use the access control framework in Identity Management (IdM) to manage who can read, write, and administer entries in the IdM directory. IdM provides self-service rules, delegation rules, and role-based access control (RBAC), all built on LDAP access control instructions (ACIs).

### [22.1. Access control methods in IdM](#access-control-methods-in-idm) {#access-control-methods-in-idm .title}

Choose the appropriate access control method in Identity Management (IdM) to grant users the right level of authority over directory entries.

IdM divides access control methods into the following categories:

Self-service rules
:   Define what operations a user can perform on the user's own personal entry. This access control type only allows write permissions to specific attributes within the user entry. Users can update the values of specific attributes but cannot add or delete the attributes as such.

Delegation rules
:   By using a delegation rule, you can allow a specific user group to perform write, that is edit, operations on specific attributes of users in another user group. Similarly to self-service rules, this form of access control rule is limited to editing the values of specific attributes. It does not grant the ability to add or remove whole entries or control over unspecified attributes.

Role-based access control

:   Creates special access control groups that are then granted much broader authority over all types of entities in the IdM domain. Roles can be granted edit, add, and delete rights, meaning they can be granted complete control over entire entries, not just selected attributes.

    Certain roles are already available in IdM by default, for example `Enrollment Administrator`{.literal}, `IT Security Specialist`{.literal}, and `IT Specialist`{.literal}. You can create additional roles to manage any types of entries, such as hosts, automount configuration, netgroups, DNS settings, and IdM configuration.

**Additional resources**

-   [Using Ansible playbooks to manage self-service rules in IdM](#using-ansible-playbooks-to-manage-self-service-rules-in-idm "Chapter 25. Using Ansible playbooks to manage self-service rules in IdM")
-   [Delegating permissions to user groups to manage users using Ansible playbooks](#delegating-permissions-to-user-groups-to-manage-users-using-ansible-playbooks "Chapter 34. Delegating permissions to user groups to manage users using Ansible playbooks")
-   [Using Ansible playbooks to manage role-based access control in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-ansible-playbooks-to-manage-role-based-access-control-in-idm)

### [22.2. Access control instructions in IdM](#access-control-instructions-in-idm) {#access-control-instructions-in-idm .title}

Use access control instructions (ACIs) in Identity Management (IdM) to define which users can perform specific operations on which LDAP entries. ACIs are based on 389 Directory Server access control and form the foundation of all IdM access control methods.

An ACI has three parts:

Actor
:   The entity that is being granted permission to do something. In LDAP access control models, you can, for example, specify that the ACI rule is applied only when a user binds to the directory using their distinguished name (DN). Such a specification is called the *bind rule*: it defines who the user is and can optionally require other limits on the bind attempt, such as restricting attempts to a certain time of day or a certain machine.

Target
:   The entry that the actor is allowed to perform operations on.

Operation type
:   Determines what kinds of actions the actor is allowed to perform. The most common operations are add, delete, write, read, and search. In IdM, the read and search rights of a non-administrative user are limited, and even more so in the IdM Web UI than the IdM CLI.

When an LDAP operation is attempted, the following occurs:

1.  The IdM client sends user credentials to an IdM server as part of the bind operation.
2.  The IdM server DS checks the user credentials.
3.  The IdM server DS checks the user account to see if the user has a permission to perform the requested operation.

### [22.3. Additional resources](#access-control-in-idm_223-additional-resources) {#additional-resources-8 .title}

-   [Managing self-service rules in IdM using the CLI](#managing-self-service-rules-in-idm-using-the-cli "Chapter 23. Managing self-service rules in IdM using the CLI")
-   [Delegating permissions to user groups to manage users using IdM CLI](#delegating-permissions-to-user-groups-to-manage-users-using-idm-cli "Chapter 32. Delegating permissions to user groups to manage users using IdM CLI")
-   [Managing role-based access controls in IdM using the CLI](#managing-role-based-access-controls-in-idm-using-the-cli "Chapter 35. Managing role-based access controls in IdM using the CLI")

## [Chapter 23. Managing self-service rules in IdM using the CLI](#managing-self-service-rules-in-idm-using-the-cli) {#chapter-23.-managing-self-service-rules-in-idm-using-the-cli .title}

Manage self-service rules in Identity Management (IdM) using the CLI to control which attributes users can edit on their own entries. Self-service rules reduce administrative overhead by allowing users to manage specific personal data independently.

### [23.1. Self-service access control in IdM](#self-service-access-control-in-idm_managing-self-service-rules-in-idm-using-the-cli) {#self-service-access-control-in-idm .title}

Self-service access control rules define which operations an Identity Management (IdM) entity can perform on its IdM Directory Server entry: for example, IdM users have the ability to update their own passwords.

This method of control allows an authenticated IdM entity to edit specific attributes within its LDAP entry, but does not allow `add`{.literal} or `delete`{.literal} operations on the entire entry.

Warning

Be careful when working with self-service access control rules: configuring access control rules improperly can inadvertently elevate an entity's privileges.

### [23.2. Creating self-service rules using the CLI](#creating-self-service-rules-using-the-cli) {#creating-self-service-rules-using-the-cli .title}

Create self-service rules using the Identity Management (IdM) CLI to allow users to manage their own account attributes. Self-service rules reduce administrative burden while allowing users to update specific information.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

-   To add a self-service rule, use the `ipa selfservice-add`{.literal} command and specify the following two options:

    `--permissions`{.literal}
    :   sets the **read** and **write** permissions the Access Control Instruction (ACI) grants.

    `--attrs`{.literal}

    :   sets the complete list of attributes to which this ACI grants permission.

        For example, to create a self-service rule allowing users to modify their own name details:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa selfservice-add "Users can manage their own name details" --permissions=write --attrs=givenname --attrs=displayname --attrs=title --attrs=initials
    -----------------------------------------------------------
    Added selfservice "Users can manage their own name details"
    -----------------------------------------------------------
        Self-service name: Users can manage their own name details
        Permissions: write
        Attributes: givenname, displayname, title, initials
    ```

### [23.3. Editing self-service rules using the CLI](#editing-self-service-rules-using-the-cli) {#editing-self-service-rules-using-the-cli .title}

Modify self-service rules using the Identity Management (IdM) CLI to adjust which attributes users can manage themselves.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Optional: Display existing self-service rules with the `ipa selfservice-find`{.literal} command.

2.  Optional: Display details for the self-service rule you want to modify with the `ipa selfservice-show`{.literal} command.

3.  Use the `ipa selfservice-mod`{.literal} command to edit a self-service rule.

    For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa selfservice-mod "Users can manage their own name details" --attrs=givenname --attrs=displayname --attrs=title --attrs=initials --attrs=surname
    --------------------------------------------------------------
    Modified selfservice "Users can manage their own name details"
    --------------------------------------------------------------
    Self-service name: Users can manage their own name details
    Permissions: write
    Attributes: givenname, displayname, title, initials
    ```

    Important

    Using the `ipa selfservice-mod`{.literal} command overwrites the previously defined permissions and attributes, so always include the complete list of existing permissions and attributes along with any new ones you want to define.

**Verification**

-   Use the `ipa selfservice-show`{.literal} command to display the self-service rule you edited.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa selfservice-show "Users can manage their own name details"
    --------------------------------------------------------------
    Self-service name: Users can manage their own name details
    Permissions: write
    Attributes: givenname, displayname, title, initials
    ```

### [23.4. Deleting self-service rules using the CLI](#deleting-self-service-rules-using-the-cli) {#deleting-self-service-rules-using-the-cli .title}

You can delete self-service rules using the Identity Management (IdM) CLI to revoke user permissions for managing their own attributes. Removing unnecessary self-service rules helps maintain appropriate access control.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

-   Use the `ipa selfservice-del`{.literal} command to delete a self-service rule.

    For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa selfservice-del "Users can manage their own name details"
    -----------------------------------------------------------
    Deleted selfservice "Users can manage their own name details"
    -----------------------------------------------------------
    ```

**Verification**

-   Use the `ipa selfservice-find`{.literal} command to display all self-service rules. The rule you just deleted should be missing.

## [Chapter 24. Managing self-service rules using the IdM Web UI](#managing-self-service-rules-using-the-idm-web-ui) {#chapter-24.-managing-self-service-rules-using-the-idm-web-ui .title}

Manage self-service rules in Identity Management (IdM) using the Web UI to control which attributes users can edit on their own entries. Self-service rules reduce administrative overhead by allowing users to manage specific personal data independently.

### [24.1. Self-service access control in IdM](#self-service-access-control-in-idm_managing-self-service-rules-using-the-idm-web-ui) {#self-service-access-control-in-idm-1 .title}

Self-service access control rules define which operations an Identity Management (IdM) entity can perform on its IdM Directory Server entry: for example, IdM users have the ability to update their own passwords.

This method of control allows an authenticated IdM entity to edit specific attributes within its LDAP entry, but does not allow `add`{.literal} or `delete`{.literal} operations on the entire entry.

Warning

Be careful when working with self-service access control rules: configuring access control rules improperly can inadvertently elevate an entity's privileges.

### [24.2. Creating self-service rules using the IdM Web UI](#creating-self-service-rules-using-the-idm-web-ui) {#creating-self-service-rules-using-the-idm-web-ui .title}

Create self-service rules using the Identity Management (IdM) WebUI to allow users to manage their own account attributes. Self-service rules reduce administrative burden while allowing users to update specific information.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  Open the **IPA Server\>Role-Based Access Control** menu and select **Self Service Permissions**.

2.  Click **Add** at the upper-right of the list of the self-service access rules.

3.  On the **Add Self Service Permission** window, enter the name of the new self-service rule in the **Self-service name** field. Spaces are allowed.

4.  Select the checkboxes next to the attributes you want users to be able to edit.

5.  Optional: If an attribute you want to provide access to is not listed, you can add a listing for it:

    a.  Click the **Add** button.
    b.  On the **Add Custom Attribute** window, enter the attribute name in the **Attribute** text field.
    c.  Click the **OK** button to add the attribute.
    d.  Verify that the new attribute is selected.

6.  Click the **Add** button at the bottom of the form to save the new self-service rule.

    Alternatively, you can save and continue editing the self-service rule by clicking the **Add and Edit** button, or save and add further rules by clicking the **Add and Add another** button.

### [24.3. Editing self-service rules using the IdM Web UI](#editing-self-service-rules-using-the-idm-web-ui) {#editing-self-service-rules-using-the-idm-web-ui .title}

Modify self-service rules using the Identity Management (IdM) WebUI to adjust which attributes users can manage themselves.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  Open the **IPA Server\>Role-Based Access Control** menu and select **Self Service Permissions**.
2.  Click on the name of the self-service rule you want to modify.
3.  The edit page only allows you to edit the list of attributes to you want to add or remove to the self-service rule. Select or deselect the appropriate checkboxes.
4.  Click the **Save** button to save your changes to the self-service rule.

### [24.4. Deleting self-service rules using the IdM Web UI](#deleting-self-service-rules-using-the-idm-web-ui) {#deleting-self-service-rules-using-the-idm-web-ui .title}

You can delete self-service rules using the Identity Management (IdM) WebUI to revoke user permissions for managing their own attributes. Removing unnecessary self-service rules helps maintain appropriate access control.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  Open the **IPA Server\>Role-Based Access Control** menu and select **Self Service Permissions**.
2.  Select the checkbox next to the rule you want to delete, then click on the **Delete** button on the right of the list.
3.  A dialog opens, click on **Delete** to confirm.

## [Chapter 25. Using Ansible playbooks to manage self-service rules in IdM](#using-ansible-playbooks-to-manage-self-service-rules-in-idm) {#chapter-25.-using-ansible-playbooks-to-manage-self-service-rules-in-idm .title}

Define self-service access rules using Ansible to allow Identity Management (IdM) users to modify specific attributes on their own directory entries.

### [25.1. Using Ansible to ensure that a self-service rule is present](#using-ansible-to-ensure-that-a-self-service-rule-is-present) {#using-ansible-to-ensure-that-a-self-service-rule-is-present .title}

Create self-service rules in Identity Management (IdM) using Ansible to enable users to modify specific attributes on their own directory entries, such as display name or initials.

In the example below, the new **Users can manage their own name details** rule grants users the ability to change their own `givenname`{.literal}, `displayname`{.literal}, `title`{.literal} and `initials`{.literal} attributes. This allows them to, for example, change their display name or initials if they want to.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `selfservice-present.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice/selfservice-present.yml selfservice-present-copy.yml
    ```

3.  Open the `selfservice-present-copy.yml`{.literal} Ansible playbook file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipaselfservice`{.literal} task section:

    -   Set the `name`{.literal} variable to the name of the new self-service rule.
    -   Set the `permission`{.literal} variable to a comma-separated list of permissions to grant: `read`{.literal} and `write`{.literal}.
    -   Set the `attribute`{.literal} variable to a list of attributes that users can manage themselves: `givenname`{.literal}, `displayname`{.literal}, `title`{.literal}, and `initials`{.literal}.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Self-service present
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure self-service rule "Users can manage their own name details" is present
        freeipa.ansible_freeipa.ipaselfservice:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: "Users can manage their own name details"
          permission: read, write
          attribute:
          - givenname
          - displayname
          - title
          - initials
    ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-selfservice.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice`{.literal} directory on the control node.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory selfservice-present-copy.yml
    ```

### [25.2. Using Ansible to ensure that a self-service rule is absent](#using-ansible-to-ensure-that-a-self-service-rule-is-absent) {#using-ansible-to-ensure-that-a-self-service-rule-is-absent .title}

Remove self-service rules from Identity Management (IdM) using Ansible to prevent users from modifying specific attributes on their own directory entries.

In the example below, you make sure the **Users can manage their own name details** self-service rule does not exist in IdM. This ensures that users cannot, for example, change their own display name or initials.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `selfservice-absent.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice/selfservice-absent.yml selfservice-absent-copy.yml
    ```

3.  Open the `selfservice-absent-copy.yml`{.literal} Ansible playbook file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipaselfservice`{.literal} task section:

    -   Set the `name`{.literal} variable to the name of the self-service rule.
    -   Set the `state`{.literal} variable to `absent`{.literal}.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Self-service absent
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure self-service rule "Users can manage their own name details" is absent
        freeipa.ansible_freeipa.ipaselfservice:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: "Users can manage their own name details"
          state: absent
    ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-selfservice.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice`{.literal} directory on the control node.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory selfservice-absent-copy.yml
    ```

**Additional resources**

-   [Self-service access control in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-self-service-rules-in-idm-using-the-cli#self-service-access-control-in-idm)

### [25.3. Using Ansible to ensure that a self-service rule has specific attributes](#using-ansible-to-ensure-that-a-self-service-rule-has-specific-attributes) {#using-ansible-to-ensure-that-a-self-service-rule-has-specific-attributes .title}

Add attributes to existing Identity Management (IdM) self-service rules using Ansible to expand which user entry fields users can modify themselves.

In the example below, you ensure the **Users can manage their own name details** self-service rule also has the `surname`{.literal} member attribute.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.

-   The **Users can manage their own name details** self-service rule exists in IdM.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `selfservice-member-present.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice/selfservice-member-present.yml selfservice-member-present-copy.yml
    ```

3.  Open the `selfservice-member-present-copy.yml`{.literal} Ansible playbook file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipaselfservice`{.literal} task section:

    -   Set the `name`{.literal} variable to the name of the self-service rule to modify.
    -   Set the `attribute`{.literal} variable to `surname`{.literal}.
    -   Set the `action`{.literal} variable to `member`{.literal}.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Self-service member present
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure selfservice "Users can manage their own name details" member attribute surname is present
        freeipa.ansible_freeipa.ipaselfservice:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: "Users can manage their own name details"
          attribute:
          - surname
          action: member
    ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-selfservice.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice`{.literal} directory on the control node.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory selfservice-member-present-copy.yml
    ```

**Additional resources**

-   [Self-service access control in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-self-service-rules-in-idm-using-the-cli#self-service-access-control-in-idm)

### [25.4. Using Ansible to ensure that a self-service rule does not have specific attributes](#using-ansible-to-ensure-that-a-self-service-rule-does-not-have-specific-attributes) {#using-ansible-to-ensure-that-a-self-service-rule-does-not-have-specific-attributes .title}

Remove attributes from existing Identity Management (IdM) self-service rules using Ansible to restrict which user entry fields users can modify themselves.

In the example below, you ensure the **Users can manage their own name details** self-service rule does not have the `givenname`{.literal} and `surname`{.literal} member attributes.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

-   The **Users can manage their own name details** self-service rule exists in IdM.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `selfservice-member-absent.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice/selfservice-member-absent.yml selfservice-member-absent-copy.yml
    ```

3.  Open the `selfservice-member-absent-copy.yml`{.literal} Ansible playbook file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipaselfservice`{.literal} task section:

    -   Set the `name`{.literal} variable to the name of the self-service rule you want to modify.
    -   Set the `attribute`{.literal} variable to `givenname`{.literal} and `surname`{.literal}.
    -   Set the `action`{.literal} variable to `member`{.literal}.
    -   Set the `state`{.literal} variable to `absent`{.literal}.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Self-service member absent
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure selfservice "Users can manage their own name details" member attributes givenname and surname are absent
        freeipa.ansible_freeipa.ipaselfservice:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: "Users can manage their own name details"
          attribute:
          - givenname
          - surname
          action: member
          state: absent
    ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-selfservice.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/selfservice`{.literal} directory on the control node.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory selfservice-member-absent-copy.yml
    ```

**Additional resources**

-   [Self-service access control in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-self-service-rules-in-idm-using-the-cli#self-service-access-control-in-idm)

### [25.5. Additional resources](#using-ansible-playbooks-to-manage-self-service-rules-in-idm_255-additional-resources) {#additional-resources-9 .title}

-   [Managing self-service rules in IdM using the CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-self-service-rules-in-idm-using-the-cli)

## [Chapter 26. Managing user groups in IdM CLI](#managing-user-groups-in-idm-cli) {#chapter-26.-managing-user-groups-in-idm-cli .title}

Manage user groups in Identity Management (IdM) using the CLI to organize users with common privileges, password policies, and other characteristics. User groups simplify administration by applying policies to multiple users at once.

A user group in Identity Management (IdM) can include:

-   IdM users
-   other IdM user groups
-   external users, which are users that exist outside of IdM

### [26.1. Different group types in IdM](#the-different-group-types-in-idm_user-groups-cli) {#different-group-types-in-idm .title}

Identity Management (IdM) supports three types of user groups---POSIX, non-POSIX, and external---each suited to different identity store integrations and Linux attribute requirements.

POSIX groups (the default)

:   POSIX groups support Linux POSIX attributes for their members. Note that groups that interact with Active Directory cannot use POSIX attributes.

    POSIX attributes identify users as separate entities. Examples of POSIX attributes relevant to users include `uidNumber`{.literal}, a user number (UID), and `gidNumber`{.literal}, a group number (GID).

Non-POSIX groups

:   Non-POSIX groups do not support POSIX attributes. For example, these groups do not have a GID defined.

    All members of this type of group must belong to the IdM domain.

External groups

:   Use external groups to add group members that exist in an identity store outside of the IdM domain, such as:

    -   A local system
    -   An Active Directory domain
    -   A directory service

    External groups do not support POSIX attributes. For example, these groups do not have a GID defined.

+--------------------------+------------------------------------------------------------------------------------+
| Group name               | Default group members                                                              |
+:=========================+:===================================================================================+
| `ipausers`{.literal}     | All IdM users                                                                      |
+--------------------------+------------------------------------------------------------------------------------+
| `admins`{.literal}       | Users with administrative privileges, including the default `admin`{.literal} user |
+--------------------------+------------------------------------------------------------------------------------+
| `editors`{.literal}      | This is a legacy group that no longer has any special privileges                   |
+--------------------------+------------------------------------------------------------------------------------+
| `trust admins`{.literal} | Users with privileges to manage the Active Directory trusts                        |
+--------------------------+------------------------------------------------------------------------------------+

: Table 26.1. User groups created by default

Show more

When you add a user to a user group, the user gains the privileges and policies associated with the group. For example, to grant administrative privileges to a user, add the user to the `admins`{.literal} group.

Warning

Do not delete the `admins`{.literal} group. As `admins`{.literal} is a pre-defined group required by IdM, this operation causes problems with certain commands.

In addition, IdM creates *user private groups* by default whenever a new user is created in IdM. For more information about private groups, see [Adding users without a private group](adding-users-without-a-user-private-group).

### [26.2. Direct and indirect group members](#direct-and-indirect-group-members_user-groups-cli) {#direct-and-indirect-group-members .title}

You can manage group membership inheritance in Identity Management (IdM) by using direct and indirect members. Nested group structures simplify policy administration by automatically applying group attributes to all member levels.

User group attributes in IdM apply to both direct and indirect members: when group B is a member of group A, all users in group B are considered indirect members of group A.

For example, in the following diagram:

-   User 1 and User 2 are *direct members* of group A.
-   User 3, User 4, and User 5 are *indirect members* of group A.

**Figure 26.1. Direct and Indirect Group Membership**

If you set a password policy for user group A, the policy also applies to all users in user group B.

### [26.3. Adding a user group using IdM CLI](#adding-a-user-group-using-idm-cli) {#adding-a-user-group-using-idm-cli .title}

Create user groups in the Identity Management (IdM) CLI to organize users and manage access control policies collectively. Groups simplify administration by allowing you to assign permissions and roles to multiple users at once.

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

-   Add a user group by using the `ipa group-add `{.literal}*`group_name`{.literal}* command. For example, to create `group_a`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-add group_a
    ---------------------
    Added group "group_a"
    ---------------------
      Group name: group_a
      GID: 1133400009
    ```

    By default, `ipa group-add`{.literal} adds a POSIX user group. To specify a different group type, add options to `ipa group-add`{.literal}:

-   `--nonposix`{.literal} to create a non-POSIX group

-   `--external`{.literal} to create an external group

    For details on group types, see [Different group types in IdM](#the-different-group-types-in-idm_user-groups-cli "26.1. Different group types in IdM").

    You can specify a custom GID when adding a user group by using the `--gid=`{.literal}*`custom_GID`{.literal}* option. If you do this, be careful to avoid ID conflicts. If you do not specify a custom GID, IdM automatically assigns a GID from the available ID range.

### [26.4. Searching for user groups using IdM CLI](#searching-for-user-groups-using-idm-cli) {#searching-for-user-groups-using-idm-cli .title}

Search for existing user groups in Identity Management (IdM) by using the CLI to identify POSIX, non-POSIX, and external groups in your domain.

**Procedure**

-   Display all user groups by using the `ipa group-find`{.literal} command. To specify a group type, add options to `ipa group-find`{.literal}:

    -   Display all POSIX groups using the `ipa group-find --posix`{.literal} command.
    -   Display all non-POSIX groups using the `ipa group-find --nonposix`{.literal} command.
    -   Display all external groups using the `ipa group-find --external`{.literal} command.

**Additional resources**

-   [Different group types in IdM](#the-different-group-types-in-idm_user-groups-cli "26.1. Different group types in IdM")

### [26.5. Deleting a user group using IdM CLI](#deleting-a-user-group-using-idm-cli) {#deleting-a-user-group-using-idm-cli .title}

You can delete user groups using the Identity Management (IdM) CLI. Deleting a group does not delete the group members from IdM.

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

-   Delete a user group by using the `ipa group-del `{.literal}*`group_name`{.literal}* command. For example, to delete group_a:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-del group_a
    --------------------------
    Deleted group "group_a"
    --------------------------
    ```

### [26.6. Adding a member to a user group using IdM CLI](#adding-a-member-to-a-user-group-using-idm-cli) {#adding-a-member-to-a-user-group-using-idm-cli .title}

Add users and user groups as members of a user group in the Identity Management (IdM) CLI to organize permissions and access control efficiently. Group membership simplifies user management by applying policies to multiple users simultaneously.

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

-   Add a member to a user group by using the `ipa group-add-member`{.literal} command.

    Specify the type of member using these options:

    -   `--users`{.literal} adds an IdM user
    -   `--external`{.literal} adds a user that exists outside the IdM domain, in the format of `DOMAIN\user_name`{.literal} or `user_name@domain`{.literal}
    -   `--groups`{.literal} adds an IdM user group

    For example, to add group_b as a member of group_a:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-add-member group_a --groups=group_b
    Group name: group_a
    GID: 1133400009
    Member users: user_a
    Member groups: group_b
    Indirect Member users: user_b
    -------------------------
    Number of members added 1
    -------------------------
    ```

    Members of group_b are now indirect members of group_a.

    Important

    When adding a group as a member of another group, do not create recursive groups. For example, if Group A is a member of Group B, do not add Group B as a member of Group A. Recursive groups can cause unpredictable behavior.

    Note

    After you add a member to a user group, the update may take some time to spread to all clients in your Identity Management environment. This is because when any given host resolves users, groups and netgroups, the `System Security Services Daemon`{.literal} (SSSD) first looks into its cache and performs server lookups only for missing or expired records.

### [26.7. Adding users without a user private group](#adding-users-without-a-user-private-group) {#adding-users-without-a-user-private-group .title}

You can add Identity Management (IdM) users without creating user private groups (UPGs) to control group ID assignments and membership structures. By default, IdM creates a UPG for each new user, but you can disable this behavior globally or for individual users.

UPGs have the following characteristics:

-   The UPG has the same name as the newly created user.
-   The user is the only member of the UPG. The UPG cannot contain any other members.
-   The GID of the private group matches the UID of the user.

However, it is possible to add users without creating a UPG.

#### [26.7.1. Users without a user private group](#users-without-a-user-private-group) {#users-without-a-user-private-group .title}

When an existing NIS or system group already uses the GID that Identity Management (IdM) wants to assign to a user private group (UPG), you must explicitly skip UPG creation to avoid GID conflicts.

You can do this in two ways:

-   Add a new user without a UPG, without disabling private groups globally.
-   Disable UPGs globally for all users, then add a new user.

In both cases, IdM will require specifying a GID when adding new users, otherwise the operation will fail. This is because IdM requires a GID for the new user, but the default user group `ipausers`{.literal} is a non-POSIX group and therefore does not have an associated GID. The GID you specify does not have to correspond to an already existing group.

Note

Specifying the GID does not create a new group. It only sets the GID attribute for the new user, because the attribute is required by IdM.

**Additional resources**

-   [Adding a user without a user private group when private groups are globally enabled](#adding-a-user-without-a-user-private-group-when-private-groups-are-globally-enabled "26.7.2. Adding a user without a user private group when private groups are globally enabled")
-   [Disabling user private groups globally for all users](#disabling-user-private-groups-globally-for-all-users "26.7.3. Disabling user private groups globally for all users")
-   [Adding a user when user private groups are globally disabled](#adding-a-user-when-user-private-groups-are-globally-disabled "26.7.4. Adding a user when user private groups are globally disabled")

#### [26.7.2. Adding a user without a user private group when private groups are globally enabled](#adding-a-user-without-a-user-private-group-when-private-groups-are-globally-enabled) {#adding-a-user-without-a-user-private-group-when-private-groups-are-globally-enabled .title}

Add a user without creating a user private group (UPG) in Identity Management (IdM) by manually specifying a GID. With this, you can share primary groups across multiple users for collaborative file access and permissions management.

**Procedure**

-   To prevent IdM from creating a UPG, add the `--noprivate`{.literal} option to the `ipa user-add`{.literal} command.

    Note that for the command to succeed, you must specify a custom GID. For example, to add a new user with GID 10000:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-add jsmith --first=John --last=Smith --noprivate --gid 10000
    ```

#### [26.7.3. Disabling user private groups globally for all users](#disabling-user-private-groups-globally-for-all-users) {#disabling-user-private-groups-globally-for-all-users .title}

You can disable automatic user private group creation in Identity Management (IdM). Global UPG disabling applies only to new users while existing users are not affected.

**Procedure**

1.  Obtain administrator privileges:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit admin
    ```

2.  IdM uses the Directory Server Managed Entries Plug-in to manage UPGs. List the instances of the plug-in:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa-managed-entries --list
    ```

3.  To ensure IdM does not create UPGs, disable the plug-in instance responsible for managing user private groups:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa-managed-entries -e "UPG Definition" disable
    Disabling Plugin
    ```

    To re-enable the `UPG Definition`{.literal} instance later, use the `ipa-managed-entries -e "UPG Definition" enable`{.literal} command.

4.  Restart Directory Server to load the new configuration.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl restart dirsrv.target
    ```

    To add a user after UPGs have been disabled, you need to specify a GID. For more information, see [Adding a user when user private groups are globally disabled](#adding-a-user-when-user-private-groups-are-globally-disabled "26.7.4. Adding a user when user private groups are globally disabled")

**Verification**

-   To check if UPGs are globally disabled, use the disable command again:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa-managed-entries -e "UPG Definition" disable
    Plugin already disabled
    ```

#### [26.7.4. Adding a user when user private groups are globally disabled](#adding-a-user-when-user-private-groups-are-globally-disabled) {#adding-a-user-when-user-private-groups-are-globally-disabled .title}

When user private groups are disabled globally in Identity Management (IdM), assign a GID manually or use an automember rule to add users. This ensures users have proper group membership for file permissions and resource access.

**Prerequisites**

-   UPGs must be disabled globally for all users. For more information, see [Disabling user private groups globally for all users](#disabling-user-private-groups-globally-for-all-users "26.7.3. Disabling user private groups globally for all users")

**Procedure**

-   To make sure adding a new user succeeds when creating UPGs is disabled, choose one of the following:

    -   Specify a custom GID when adding a new user. The GID does not have to correspond to an already existing user group.

        For example, when adding a user from the command line, add the `--gid`{.literal} option to the `ipa user-add`{.literal} command.

    -   Use an automember rule to add the user to an existing group with a GID. See [Automating group membership using IdM CLI](#automating-group-membership-using-idm-cli "Chapter 29. Automating group membership using IdM CLI").

### [26.8. Adding users or groups as member managers to an IdM user group using the IdM CLI](#adding-users-or-groups-as-member-managers-to-an-idm-user-group-using-the-idm-cli) {#adding-users-or-groups-as-member-managers-to-an-idm-user-group-using-the-idm-cli .title}

Designate users or user groups as member managers using the Identity Management (IdM) CLI to delegate user group membership management. Member managers can add or remove group members without having full administrative privileges.

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   You must have the name of the user or group you are adding as member managers and the name of the group you want them to manage.

**Procedure**

-   Add a user as a member manager to an IdM user group by using the `ipa group-add-member-manager`{.literal} command.

    For example, to add the user `test`{.literal} as a member manager of `group_a`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-add-member-manager group_a --users=test
    Group name: group_a
    GID: 1133400009
    Membership managed by users: test
    -------------------------
    Number of members added 1
    -------------------------
    ```

    User `test`{.literal} can now manage members of `group_a`{.literal}.

-   Add a group as a member manager to an IdM user group by using the `ipa group-add-member-manager`{.literal} command.

    For example, to add the group `group_admins`{.literal} as a member manager of `group_a`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-add-member-manager group_a --groups=group_admins
    Group name: group_a
    GID: 1133400009
    Membership managed by groups: group_admins
    Membership managed by users: test
    -------------------------
    Number of members added 1
    -------------------------
    ```

    Group `group_admins`{.literal} can now manage members of `group_a`{.literal}.

    Note

    After you add a member manager to a user group, the update may take some time to spread to all clients in your Identity Management environment.

**Verification**

-   Using the `ipa group-show`{.literal} command to verify the user and group were added as member managers.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-show group_a
    Group name: group_a
    GID: 1133400009
    Membership managed by groups: group_admins
    Membership managed by users: test
    ```

### [26.9. Viewing group members using IdM CLI](#viewing-group-members-using-idm-cli) {#viewing-group-members-using-idm-cli .title}

View both direct and indirect members of an Identity Management (IdM) user group by using the CLI to understand group membership inheritance across nested groups.

**Procedure**

-   To list members of a group, use the `ipa group-show `{.literal}*`group_name`{.literal}* command. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-show group_a
      ...
      Member users: user_a
      Member groups: group_b
      Indirect Member users: user_b
    ```

    Note

    The list of indirect members does not include external users from trusted Active Directory domains. The Active Directory trust user objects are not visible in the Identity Management interface because they do not exist as LDAP objects within Identity Management.

**Additional resources**

-   [Direct and indirect group members](#direct-and-indirect-group-members_user-groups-cli "26.2. Direct and indirect group members")

### [26.10. Removing a member from a user group using IdM CLI](#removing-a-member-from-a-user-group-using-idm-cli) {#removing-a-member-from-a-user-group-using-idm-cli .title}

Remove users, external users, or nested groups from an Identity Management (IdM) user group by using the CLI to revoke their inherited group privileges.

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Optional: Use the `ipa group-show`{.literal} command to confirm that the group includes the member you want to remove.

2.  Remove a member from a user group by using the `ipa group-remove-member`{.literal} command.

    Specify members to remove using these options:

    -   `--users`{.literal} removes an IdM user
    -   `--external`{.literal} removes a user that exists outside the IdM domain, in the format of `DOMAIN\user_name`{.literal} or `user_name@domain`{.literal}
    -   `--groups`{.literal} removes an IdM user group

    For example, to remove *user1*, *user2*, and *group1* from a group called *group_name*:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-remove-member group_name --users=user1 --users=user2 --groups=group1
    ```

### [26.11. Removing users or groups as member managers from an IdM user group using the IdM CLI](#removing-users-or-groups-as-member-managers-from-an-idm-user-group-using-the-idm-cli) {#removing-users-or-groups-as-member-managers-from-an-idm-user-group-using-the-idm-cli .title}

Remove users or groups as member managers from an Identity Management (IdM) user group by using the CLI to revoke their ability to manage group membership. Member managers can add and remove group members but cannot change the group's attributes.

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   You must have the name of the existing member manager user or group you are removing and the name of the group they are managing.

**Procedure**

-   Remove a user as a member manager of an IdM user group by using the `ipa group-remove-member-manager`{.literal} command.

    For example, to remove the user `test`{.literal} as a member manager of `group_a`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-remove-member-manager group_a --users=test
    Group name: group_a
    GID: 1133400009
    Membership managed by groups: group_admins
    ---------------------------
    Number of members removed 1
    ---------------------------
    ```

    User `test`{.literal} can no longer manage members of `group_a`{.literal}.

-   Remove a group as a member manager of an IdM user group by using the `ipa group-remove-member-manager`{.literal} command.

    For example, to remove the group `group_admins`{.literal} as a member manager of `group_a`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-remove-member-manager group_a --groups=group_admins
    Group name: group_a
    GID: 1133400009
    ---------------------------
    Number of members removed 1
    ---------------------------
    ```

    Group `group_admins`{.literal} can no longer manage members of `group_a`{.literal}.

    Note

    After you remove a member manager from a user group, the update may take some time to spread to all clients in your Identity Management environment.

**Verification**

-   Using the `ipa group-show`{.literal} command to verify the user and group were removed as member managers.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-show group_a
    Group name: group_a
    GID: 1133400009
    ```

### [26.12. Enabling group merging for local and remote groups in IdM](#enabling-group-merging-for-local-and-remote-groups-in-idm) {#enabling-group-merging-for-local-and-remote-groups-in-idm .title}

Enable group merging in Identity Management (IdM) to combine membership from centrally managed and local groups with matching names. Group merging supports legacy applications that require local group memberships while maintaining centralized management.

Groups are either centrally managed, provided by a domain such as IdM or Active Directory (AD), or they are managed on a local system in the `etc/group`{.literal} file. In most cases, users rely on a centrally managed store. However, in some cases software still relies on membership in known groups for managing access control.

If you want to manage groups from a domain controller and from the local `etc/group`{.literal} file, you can enable group merging. You can configure your `nsswitch.conf`{.literal} file to check both the local files and the remote service. If a group appears in both, the list of member users is combined and returned in a single response. The steps below describe how to enable group merging for a user, *idmuser*.

Note

If you are using the `authselect`{.literal} utility, you no longer need to manually edit `nssswitch.conf`{.literal} to enable group merging. It is now integrated into `authselect`{.literal} profiles, eliminating the need for manual changes.

**Procedure**

1.  Add `[SUCCESS=merge]`{.literal} to the `/etc/nsswitch.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # Allow initgroups to default to the setting for group.
    initgroups: sss [SUCCESS=merge] files
    ```

2.  Add the *idmuser* to IdM:

    ``` {.language-plaintext tabindex="-1"}
    # ipa user-add idmuser
    First name: idm
    Last name: user
    ---------------------
    Added user "idmuser"
    ---------------------
    User login: idmuser
    First name: idm
    Last name: user
    Full name: idm user
    Display name: idm user
    Initials: tu
    Home directory: /home/idmuser
    GECOS: idm user
    Login shell: /bin/sh
    Principal name: idmuser@IPA.TEST
    Principal alias: idmuser@IPA.TEST
    Email address: idmuser@ipa.test
    UID: 19000024
    GID: 19000024
    Password: False
    Member of groups: ipausers
    Kerberos keys available: False
    ```

3.  Verify the GID of the local `audio`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    $ getent group audio
    ---------------------
    audio:x:63
    ```

4.  Add the group `audio`{.literal} to IdM:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-add audio --gid 63
    -------------------
    Added group "audio"
    -------------------
    Group name: audio
    GID: 63
    ```

    Note

    The GID you define when adding the `audio`{.literal} group to IdM must be the same as the GID of the local `audio`{.literal} group.

5.  Add *idmuser* user to the IdM `audio`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-add-member audio --users=idmuser
    Group name: audio
    GID: 63
    Member users: idmuser
    -------------------------
    Number of members added 1
    -------------------------
    ```

**Verification**

1.  Log in as the *idmuser*.

2.  Verify the *idmuser* has the local group in their session:

    ``` {.language-plaintext tabindex="-1"}
    $ id idmuser
    uid=1867800003(idmuser) gid=1867800003(idmuser) groups=1867800003(idmuser),63(audio),10(wheel)
    ```

### [26.13. Additional resources](#managing-user-groups-in-idm-cli_2613-additional-resources) {#additional-resources-10 .title}

-   [Using Ansible to give a user ID override access to the local sound card on an IdM client](#using-ansible-to-give-a-user-id-override-access-to-the-local-sound-card-on-an-idm-client "37.12. Using Ansible to give a user ID override access to the local sound card on an IdM client")

## [Chapter 27. Managing user groups in IdM Web UI](#managing-user-groups-in-idm-web-ui) {#chapter-27.-managing-user-groups-in-idm-web-ui .title}

Manage user groups in Identity Management (IdM) using the Web UI to organize users with common privileges, password policies, and other characteristics. User groups simplify administration by applying policies to multiple users at once.

A user group is a set of users with common privileges, password policies, and other characteristics.

A user group in IdM can include:

-   IdM users
-   other IdM user groups
-   external users, which are users that exist outside of IdM

### [27.1. Different group types in IdM](#the-different-group-types-in-idm_user-groups-ui) {#different-group-types-in-idm-1 .title}

Identity Management (IdM) supports three types of user groups---POSIX, non-POSIX, and external---each suited to different identity store integrations and Linux attribute requirements.

POSIX groups (the default)

:   POSIX groups support Linux POSIX attributes for their members. Note that groups that interact with Active Directory cannot use POSIX attributes.

    POSIX attributes identify users as separate entities. Examples of POSIX attributes relevant to users include `uidNumber`{.literal}, a user number (UID), and `gidNumber`{.literal}, a group number (GID).

Non-POSIX groups

:   Non-POSIX groups do not support POSIX attributes. For example, these groups do not have a GID defined.

    All members of this type of group must belong to the IdM domain.

External groups

:   Use external groups to add group members that exist in an identity store outside of the IdM domain, such as:

    -   A local system
    -   An Active Directory domain
    -   A directory service

    External groups do not support POSIX attributes. For example, these groups do not have a GID defined.

+--------------------------+------------------------------------------------------------------------------------+
| Group name               | Default group members                                                              |
+:=========================+:===================================================================================+
| `ipausers`{.literal}     | All IdM users                                                                      |
+--------------------------+------------------------------------------------------------------------------------+
| `admins`{.literal}       | Users with administrative privileges, including the default `admin`{.literal} user |
+--------------------------+------------------------------------------------------------------------------------+
| `editors`{.literal}      | This is a legacy group that no longer has any special privileges                   |
+--------------------------+------------------------------------------------------------------------------------+
| `trust admins`{.literal} | Users with privileges to manage the Active Directory trusts                        |
+--------------------------+------------------------------------------------------------------------------------+

: Table 27.1. User groups created by default

Show more

When you add a user to a user group, the user gains the privileges and policies associated with the group. For example, to grant administrative privileges to a user, add the user to the `admins`{.literal} group.

Warning

Do not delete the `admins`{.literal} group. As `admins`{.literal} is a pre-defined group required by IdM, this operation causes problems with certain commands.

In addition, IdM creates *user private groups* by default whenever a new user is created in IdM. For more information about private groups, see [Adding users without a private group](adding-users-without-a-user-private-group).

### [27.2. Direct and indirect group members](#direct-and-indirect-group-members_user-groups-ui) {#direct-and-indirect-group-members-1 .title}

You can manage group membership inheritance in Identity Management (IdM) by using direct and indirect members. Nested group structures simplify policy administration by automatically applying group attributes to all member levels.

User group attributes in IdM apply to both direct and indirect members: when group B is a member of group A, all users in group B are considered indirect members of group A.

For example, in the following diagram:

-   User 1 and User 2 are *direct members* of group A.
-   User 3, User 4, and User 5 are *indirect members* of group A.

**Figure 27.1. Direct and Indirect Group Membership**

If you set a password policy for user group A, the policy also applies to all users in user group B.

### [27.3. Adding a user group using IdM Web UI](#adding-a-user-group-using-idm-web-ui) {#adding-a-user-group-using-idm-web-ui .title}

Create user groups in the Identity Management (IdM) Web UI to organize users and manage access control policies collectively. Groups simplify administration by allowing you to assign permissions and roles to multiple users at once.

**Prerequisites**

-   You are logged in to the IdM Web UI.

**Procedure**

1.  Click **Identity → Groups**, and select **User Groups** in the left sidebar.

2.  Click **Add** to start adding the group.

3.  Fill out the information about the group. For more information about user group types, see [Different group types in IdM](#the-different-group-types-in-idm_user-groups-ui "27.1. Different group types in IdM").

    You can specify a custom GID for the group. If you do this, be careful to avoid ID conflicts. If you do not specify a custom GID, IdM automatically assigns a GID from the available ID range.

4.  Click **Add** to confirm.

### [27.4. Deleting a user group using IdM Web UI](#deleting-a-user-group-using-idm-web-ui) {#deleting-a-user-group-using-idm-web-ui .title}

You can delete user groups using the Identity Management (IdM) WebUI. Deleting a group does not delete the group members from IdM.

**Prerequisites**

-   You are logged in to the IdM Web UI.

**Procedure**

1.  Click **Identity → Groups** and select **User Groups**.
2.  Select the group to delete.
3.  Click **Delete**.
4.  Click **Delete** to confirm.

### [27.5. Adding a member to a user group using IdM Web UI](#adding-a-member-to-a-user-group-using-idm-web-ui) {#adding-a-member-to-a-user-group-using-idm-web-ui .title}

Add users and user groups as members of a user group in the Identity Management (IdM) Web UI to organize permissions and access control efficiently. Group membership simplifies user management by applying policies to multiple users simultaneously.

**Prerequisites**

-   You are logged in to the IdM Web UI.

**Procedure**

1.  Click **Identity → Groups** and select **User Groups** in the left sidebar.
2.  Click the name of the group.
3.  Select the type of group member you want to add: **Users, User Groups,** or **External**.
4.  Click **Add**.
5.  Select the checkbox next to one or more members you want to add.
6.  Click the right arrow to move the selected members to the group.
7.  Click **Add** to confirm.

### [27.6. Adding users or groups as member managers to an IdM user group using the Web UI](#adding-users-or-groups-as-member-managers-to-an-idm-user-group-using-the-web-ui) {#adding-users-or-groups-as-member-managers-to-an-idm-user-group-using-the-web-ui .title}

Designate users or user groups as member managers using the Identity Management (IdM) Web UI to delegate user group membership management. Member managers can add or remove group members without having full administrative privileges.

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must have the name of the user or group you are adding as member managers and the name of the group you want them to manage.

**Procedure**

1.  Click **Identity → Groups** and select **User Groups** in the left sidebar.

2.  Click the name of the group.

3.  Select the type of group member manager you want to add: **Users** or **User Groups**.

4.  Click **Add**.

5.  Select the checkbox next to one or more members you want to add.

6.  Click the right arrow to move the selected members to the group.

7.  Click **Add** to confirm.

    Note

    After you add a member manager to a user group, the update may take some time to spread to all clients in your Identity Management environment.

**Verification**

-   Verify the newly added user or user group has been added to the member manager list of users or user groups:

### [27.7. Viewing group members using IdM Web UI](#viewing-group-members-using-idm-web-ui) {#viewing-group-members-using-idm-web-ui .title}

View both direct and indirect members of an Identity Management (IdM) user group in the IdM Web UI to understand group membership inheritance across nested groups.

**Prerequisites**

-   You are logged in to the IdM Web UI.

**Procedure**

1.  Select **Identity → Groups**.
2.  Select **User Groups** in the left sidebar.
3.  Click the name of the group you want to view.
4.  Switch between **Direct Membership** and **Indirect Membership**.

**Additional resources**

-   [Direct and indirect group members](#direct-and-indirect-group-members_user-groups-ui "27.2. Direct and indirect group members")

### [27.8. Removing a member from a user group using IdM Web UI](#removing-a-member-from-a-user-group-using-idm-web-ui) {#removing-a-member-from-a-user-group-using-idm-web-ui .title}

Remove users, nested groups, or external members from an Identity Management (IdM) user group in the IdM Web UI to revoke their inherited group privileges.

**Prerequisites**

-   You are logged in to the IdM Web UI.

**Procedure**

1.  Click **Identity → Groups** and select **User Groups** in the left sidebar.
2.  Click the name of the group.
3.  Select the type of group member you want to remove: **Users, User Groups**, or **External**.
4.  Select the checkbox next to the member you want to remove.
5.  Click **Delete**.
6.  Click **Delete** to confirm.

### [27.9. Removing users or groups as member managers from an IdM user group using the Web UI](#removing-users-or-groups-as-member-managers-from-an-idm-user-group-using-the-web-ui) {#removing-users-or-groups-as-member-managers-from-an-idm-user-group-using-the-web-ui .title}

Remove users or groups as member managers from an Identity Management (IdM) user group by using the IdM Web UI to revoke their ability to manage group membership. Member managers can add and remove group members but cannot change the group's attributes.

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must have the name of the existing member manager user or group you are removing and the name of the group they are managing.

**Procedure**

1.  Click **Identity → Groups** and select **User Groups** in the left sidebar.

2.  Click the name of the group.

3.  Select the type of member manager you want to remove: **Users** or **User Groups**.

4.  Select the checkbox next to the member manager you want to remove.

5.  Click **Delete**.

6.  Click **Delete** to confirm.

    Note

    After you remove a member manager from a user group, the update may take some time to spread to all clients in your Identity Management environment.

**Verification**

-   Verify the user or user group has been removed from the member manager list of users or user groups:

## [Chapter 28. Managing user groups using Ansible playbooks](#managing-user-groups-using-ansible-playbooks) {#chapter-28.-managing-user-groups-using-ansible-playbooks .title}

Create and manage IdM user groups using Ansible to organize users with common privileges, password policies, and access rights.

A user group in Identity Management (IdM) can include the following:

-   IdM users
-   other IdM user groups
-   external users, that is users that exist outside of IdM

### [28.1. Ensuring the presence of IdM groups and group members using Ansible playbooks](#ensuring-the-presence-of-idm-groups-and-group-members-using-ansible-playbooks) {#ensuring-the-presence-of-idm-groups-and-group-members-using-ansible-playbooks .title}

Create or verify Identity Management (IdM) groups and add members using Ansible to automate group provisioning and membership management.

**Prerequisites**

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

-   The users you want to reference in your Ansible playbook exist in IdM. For details on ensuring the presence of users using Ansible, see [Managing user accounts using Ansible playbooks](#managing-user-accounts-using-ansible-playbooks "Chapter 3. Managing user accounts using Ansible playbooks").

**Procedure**

1.  Create an Ansible playbook file with the necessary user and group information:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to handle groups
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Create group ops with gid 1234
        freeipa.ansible_freeipa.ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: ops
          gidnumber: 1234

      - name: Create group sysops
        freeipa.ansible_freeipa.ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: sysops
          user:
          - idm_user

      - name: Create group appops
        freeipa.ansible_freeipa.ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: appops

      - name: Add group members sysops and appops to group ops
        freeipa.ansible_freeipa.ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: ops
          group:
          - sysops
          - appops
    ```

    For details about all variables used in the playbook, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-group.md`{.literal} file on the control node.

2.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i path_to_inventory_directory/inventory.file path_to_playbooks_directory/add-group-members.yml
    ```

**Verification**

You can verify if the **ops** group contains **sysops** and **appops** as direct members and **idm_user** as an indirect member by using the `ipa group-show`{.literal} command:

1.  Log into `ipaserver`{.literal} as administrator:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh admin@server.idm.example.com
    Password:
    [admin@server /]$
    ```

2.  Display information about *ops*:

    ``` {.language-plaintext tabindex="-1"}
    ipaserver]$ ipa group-show ops
      Group name: ops
      GID: 1234
      Member groups: sysops, appops
      Indirect Member users: idm_user
    ```

    The **appops** and **sysops** groups - the latter including the **idm_user** user - exist in IdM.

### [28.2. Using Ansible to add multiple IdM groups in a single task](#using-ansible-to-add-multiple-idm-groups-in-a-single-task) {#using-ansible-to-add-multiple-idm-groups-in-a-single-task .title}

Create multiple Identity Management (IdM} groups in a single Ansible task using the `groups`{.literal} batch option available in the `ansible-freeipa`{.literal} `ipagroup`{.literal} module to streamline group provisioning.

Using the `groups`{.literal} option, you can also specify multiple group variables that only apply to a particular group. Define this group by the `name`{.literal} variable, which is the only mandatory variable for the `groups`{.literal} option.

Complete this procedure to ensure the presence of the **sysops** and the **appops** groups in IdM in a single task. Define the sysops group as a nonposix group and the appops group as an external group.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create your Ansible playbook file **add-nonposix-and-external-groups.yml** with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to add nonposix and external groups
      hosts: ipaserver
      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml

      tasks:
      - name: Add nonposix group sysops and external group appops
        freeipa.ansible_freeipa.ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          groups:
          - name: sysops
            nonposix: true
          - name: appops
            external: true
    ```

2.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i <path_to_inventory_directory>/hosts <path_to_playbooks_directory>/add-nonposix-and-external-groups.yml
    ```

**Additional resources**

-   [The group module in `ansible-freeipa`{.literal} upstream docs](https://github.com/freeipa/ansible-freeipa/blob/master/README-group.md)

### [28.3. Using Ansible to enable AD users to administer IdM](#using-ansible-to-enable-ad-users-to-administer-idm) {#using-ansible-to-enable-ad-users-to-administer-idm .title}

Grant Identity Management (IdM) administrative privileges to Active Directory (AD) users by adding their ID overrides to IdM groups, eliminating the need for separate IdM accounts.

In the example below, the user ID override is the override of an AD user that you created in the Default Trust View after you established a trust with AD.

**Prerequisites**

-   You know the IdM `admin`{.literal} password.

-   You have [installed a trust with AD](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/index).

-   The user ID override of the AD user already exists in IdM. If it does not, create it with the `ipa idoverrideuser-add 'default trust view' `{.literal}*`ad_user@ad.example.com`{.literal}* command.

-   The [group to which you are adding the user ID override already exists in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/managing-user-groups-using-ansible-playbooks#ensuring-the-presence-of-idm-groups-and-group-members-using-ansible-playbooks).

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Create an `add-useridoverride-to-group.yml`{.literal} playbook with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to ensure presence of users in a group
      hosts: ipaserver

      tasks:
      - name: Ensure the ad_user@ad.example.com user ID override is a member of the admins group:
        freeipa.ansible_freeipa.ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: admins
          idoverrideuser:
          - ad_user@ad.example.com
    ```

    In the example:

    -   `admins`{.literal} is the name of the IdM POSIX group to which you are adding the **ad_user@ad.example.com** ID override. Members of this group have full administrator privileges.
    -   **ad_user@ad.example.com** is the user ID override of an AD administrator. The user is stored in the AD domain with which a trust has been established.

3.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-group.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/user`{.literal} directory on the control node.

4.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory add-useridoverride-to-group.yml
    ```

**Additional resources**

-   [ID overrides for AD users](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/enabling-ad-users-to-administer-idm#id-overrides-for-ad-users)
-   [Using ID views in Active Directory environments](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/using-id-views-for-active-directory-users)
-   [Enabling AD users to administer IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/enabling-ad-users-to-administer-idm)

### [28.4. Ensuring the presence of member managers in IdM user groups using Ansible playbooks](#ensuring-the-presence-of-member-managers-in-idm-user-groups-using-ansible-playbooks) {#ensuring-the-presence-of-member-managers-in-idm-user-groups-using-ansible-playbooks .title}

Delegate group membership management to specific users or groups, allowing them to add and remove members without full administrative privileges.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

-   You must have the name of the user or group you are adding as member managers and the name of the group you want them to manage.

**Procedure**

1.  Create an Ansible playbook file with the necessary user and group member management information:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to handle membership management
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure user test is present for group_a
        freeipa.ansible_freeipa.ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: group_a
          membermanager_user: test

      - name: Ensure group_admins is present for group_a
        freeipa.ansible_freeipa.ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: group_a
          membermanager_group: group_admins
    ```

2.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i path_to_inventory_directory/inventory.file path_to_playbooks_directory/add-member-managers-user-groups.yml
    ```

**Verification**

You can verify if the **group_a** group contains **test** as a member manager and **group_admins** is a member manager of **group_a** by using the `ipa group-show`{.literal} command:

1.  Log into `ipaserver`{.literal} as administrator:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh admin@server.idm.example.com
    Password:
    [admin@server /]$
    ```

2.  Display information about *managergroup1*:

    ``` {.language-plaintext tabindex="-1"}
    ipaserver]$ ipa group-show group_a
      Group name: group_a
      GID: 1133400009
      Membership managed by groups: group_admins
      Membership managed by users: test
    ```

### [28.5. Ensuring the absence of member managers in IdM user groups using Ansible playbooks](#ensuring-the-absence-of-member-managers-in-idm-user-groups-using-ansible-playbooks) {#ensuring-the-absence-of-member-managers-in-idm-user-groups-using-ansible-playbooks .title}

Automate removing member manager privileges from users or groups when restructuring delegation or revoking administrative responsibilities.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal}.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

-   You must have the name of the existing member manager user or group you are removing and the name of the group they are managing.

**Procedure**

1.  Create an Ansible playbook file with the necessary user and group member management information:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to handle membership management
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure member manager user and group members are absent for group_a
        freeipa.ansible_freeipa.ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: group_a
          membermanager_user: test
          membermanager_group: group_admins
          action: member
          state: absent
    ```

2.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i path_to_inventory_directory/inventory.file path_to_playbooks_directory/ensure-member-managers-are-absent.yml
    ```

**Verification**

You can verify if the **group_a** group does not contain **test** as a member manager and **group_admins** as a member manager of **group_a** by using the `ipa group-show`{.literal} command:

1.  Log into `ipaserver`{.literal} as administrator:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh admin@server.idm.example.com
    Password:
    [admin@server /]$
    ```

2.  Display information about group_a:

    ``` {.language-plaintext tabindex="-1"}
    ipaserver]$ ipa group-show group_a
      Group name: group_a
      GID: 1133400009
    ```

### [28.6. Additional resources](#managing-user-groups-using-ansible-playbooks_286-additional-resources) {#additional-resources-11 .title}

-   [Managing user groups in IdM CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-user-groups-in-idm-cli)

## [Chapter 29. Automating group membership using IdM CLI](#automating-group-membership-using-idm-cli) {#chapter-29.-automating-group-membership-using-idm-cli .title}

Automate group membership in Identity Management (IdM) using the CLI to assign users and hosts to groups based on their attributes. Automatic group membership reduces manual administration by sorting entries into groups as they are created.

For example, you can:

-   Divide employees\' user entries into groups based on the employees\' manager, location, or any other attribute.
-   Divide hosts based on their class, location, or any other attribute.
-   Add all users or all hosts to a single global group.

### [29.1. Benefits of automatic group membership](#benefits-of-automatic-group-membership) {#benefits-of-automatic-group-membership .title}

Automatic group membership in Identity Management (IdM) reduces administrative overhead by assigning users and hosts to groups based on defined criteria.

This helps you to:

-   **Reduce the overhead of manually managing group memberships**

    You no longer have to assign every user and host to groups manually.

-   **Improve consistency in user and host management**

    Users and hosts are assigned to groups based on strictly defined and automatically evaluated criteria.

-   **Simplify the management of group-based settings**

    Various settings are defined for groups and then applied to individual group members, for example `sudo`{.literal} rules, automount, or access control. Adding users and hosts to groups automatically makes managing these settings easier.

### [29.2. Automember rules](#automember-rules) {#automember-rules .title}

Automember rules in Identity Management (IdM) define conditions that automatically assign users and hosts to groups based on their attributes. Understanding automember rules helps you simplify group management and ensure consistent group membership policies.

After creating a rule, the administrator adds conditions to it. These specify which users or hosts get included or excluded from the target group:

-   **Inclusive conditions**

    When a user or host entry meets an inclusive condition, it will be included in the target group.

-   **Exclusive conditions**

    When a user or host entry meets an exclusive condition, it will not be included in the target group.

The conditions are specified as regular expressions in the Perl-compatible regular expressions (PCRE) format. For more information about PCRE, see the `pcresyntax(3)`{.literal} man page on your system.

Note

IdM evaluates exclusive conditions before inclusive conditions. In case of a conflict, exclusive conditions take precedence over inclusive conditions.

An automember rule applies to every entry created in the future. These entries will be automatically added to the specified target group. If an entry meets the conditions specified in multiple automember rules, it will be added to all the corresponding groups.

Existing entries are **not** affected by the new rule.

**Additional resources**

-   [Applying automember rules to existing entries using IdM CLI](#applying-automember-rules-to-existing-entries-using-idm-cli "29.8. Applying automember rules to existing entries using IdM CLI")
-   [Applying automember rules to existing entries using IdM Web UI](#applying-automember-rules-to-existing-entries-using-idm-web-ui "30.6. Applying automember rules to existing entries using IdM Web UI")

### [29.3. Adding an automember rule using IdM CLI](#adding-an-automember-rule-using-idm-cli) {#adding-an-automember-rule-using-idm-cli .title}

Create automember rules in the Identity Management (IdM) CLI to automatically assign new users or hosts to groups based on their attributes. This eliminates manual group assignment and ensures consistent group membership policies.

Existing entries are **not** affected by the new rule. If you want to change existing entries, see [Applying automember rules to existing entries using IdM CLI](#applying-automember-rules-to-existing-entries-using-idm-cli "29.8. Applying automember rules to existing entries using IdM CLI").

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-idm-in-the-web-ui-using-a-kerberos-ticket#using-kinit-to-log-in-to-idm-manually_login-web-ui-krb).
-   The target group of the new rule must exist in IdM.

**Procedure**

1.  Enter the `ipa automember-add`{.literal} command to add an automember rule.

2.  When prompted, specify:

    -   **Automember rule**. This is the target group name.
    -   **Grouping Type**. This specifies whether the rule targets a user group or a host group. To target a user group, enter **group**. To target a host group, enter **hostgroup**.

    For example, to add an automember rule for a user group named **user_group**:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa automember-add
    Automember Rule: user_group
    Grouping Type: group
    --------------------------------
    Added automember rule "user_group"
    --------------------------------
        Automember Rule: user_group
    ```

**Verification**

-   You can display existing automember rules and conditions in IdM using [Viewing existing automember rules using IdM CLI](#viewing-existing-automember-rules-using-idm-cli "29.5. Viewing existing automember rules using IdM CLI").

### [29.4. Adding a condition to an automember rule using IdM CLI](#adding-a-condition-to-an-automember-rule-using-idm-cli) {#adding-a-condition-to-an-automember-rule-using-idm-cli .title}

Add conditions to automember rules in Identity Management (IdM) CLI to automatically assign users or hosts to groups based on their attributes. This simplifies group management and ensures consistent group membership across your environment.

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   The target rule must exist in IdM. For details, see [Adding an automember rule using IdM CLI](#adding-an-automember-rule-using-idm-cli "29.3. Adding an automember rule using IdM CLI").

**Procedure**

1.  Define one or more inclusive or exclusive conditions using the `ipa automember-add-condition`{.literal} command.

2.  When prompted, specify:

    -   **Automember rule**. This is the target rule name. See [Automember rules](#automember-rules "29.2. Automember rules") for details.
    -   **Attribute Key**. This specifies the entry attribute to which the filter will apply. For example, **uid** for users.
    -   **Grouping Type**. This specifies whether the rule targets a user group or a host group. To target a user group, enter **group**. To target a host group, enter **hostgroup**.
    -   **Inclusive regex** and **Exclusive regex**. These specify one or more conditions as regular expressions. If you only want to specify one condition, press **Enter** when prompted for the other.

    For example, the following condition targets all users with any value (.\*) in their user login attribute (**uid**).

    ``` {.language-plaintext tabindex="-1"}
    $ ipa automember-add-condition
    Automember Rule: user_group
    Attribute Key: uid
    Grouping Type: group
    [Inclusive Regex]: .*
    [Exclusive Regex]:
    ----------------------------------
    Added condition(s) to "user_group"
    ----------------------------------
      Automember Rule: user_group
      Inclusive Regex: uid=.*
    ----------------------------
    Number of conditions added 1
    ----------------------------
    ```

    As another example, you can use an automembership rule to target all Windows users synchronized from Active Directory (AD). To achieve this, create a condition that targets all users with **ntUser** in their **objectClass** attribute, which is shared by all AD users:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa automember-add-condition
    Automember Rule: ad_users
    Attribute Key: objectclass
    Grouping Type: group
    [Inclusive Regex]: ntUser
    [Exclusive Regex]:
    -------------------------------------
    Added condition(s) to "ad_users"
    -------------------------------------
      Automember Rule: ad_users
      Inclusive Regex: objectclass=ntUser
    ----------------------------
    Number of conditions added 1
    ----------------------------
    ```

**Verification**

-   You can display existing automember rules and conditions in IdM using [Viewing existing automember rules using IdM CLI](#viewing-existing-automember-rules-using-idm-cli "29.5. Viewing existing automember rules using IdM CLI").

### [29.5. Viewing existing automember rules using IdM CLI](#viewing-existing-automember-rules-using-idm-cli) {#viewing-existing-automember-rules-using-idm-cli .title}

View automember rules by using the Identity Management (IdM) CLI to review which users or hosts are automatically added to specific groups.

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Enter the `ipa automember-find`{.literal} command.

2.  When prompted, specify the **Grouping type**:

    -   To target a user group, enter **group**.

    -   To target a host group, enter **hostgroup**.

        For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa automember-find
    Grouping Type: group
    ---------------
    1 rules matched
    ---------------
      Automember Rule: user_group
      Inclusive Regex: uid=.*
    ----------------------------
    Number of entries returned 1
    ----------------------------
    ```

### [29.6. Deleting an automember rule using IdM CLI](#deleting-an-automember-rule-using-idm-cli) {#deleting-an-automember-rule-using-idm-cli .title}

Delete automember rules using the Identity Management (IdM) CLI to stop automatic group membership assignments. Removing obsolete rules ensures users and hosts are grouped according to current organizational requirements.

Deleting an automember rule also deletes all conditions associated with the rule. To remove only specific conditions from a rule, see [Removing a condition from an automember rule using IdM CLI](#removing-a-condition-from-an-automember-rule-using-idm-cli "29.7. Removing a condition from an automember rule using IdM CLI").

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Enter the `ipa automember-del`{.literal} command.

2.  When prompted, specify:

    -   **Automember rule**. This is the rule you want to delete.
    -   **Grouping rule**. This specifies whether the rule you want to delete is for a user group or a host group. Enter **group** or **hostgroup**.

### [29.7. Removing a condition from an automember rule using IdM CLI](#removing-a-condition-from-an-automember-rule-using-idm-cli) {#removing-a-condition-from-an-automember-rule-using-idm-cli .title}

Delete specific conditions from automember rules using the Identity Management (IdM) CLI to refine automatic group membership criteria.

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Enter the `ipa automember-remove-condition`{.literal} command.

2.  When prompted, specify:

    -   **Automember rule**. This is the name of the rule from which you want to remove a condition.

    -   **Attribute Key**. This is the target entry attribute. For example, **uid** for users.

    -   **Grouping Type**. This specifies whether the condition you want to delete is for a user group or a host group. Enter **group** or **hostgroup**.

    -   **Inclusive regex** and **Exclusive regex**. These specify the conditions you want to remove. If you only want to specify one condition, press **Enter** when prompted for the other.

        For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa automember-remove-condition
    Automember Rule: user_group
    Attribute Key: uid
    Grouping Type: group
    [Inclusive Regex]: .*
    [Exclusive Regex]:
    -----------------------------------
    Removed condition(s) from "user_group"
    -----------------------------------
      Automember Rule: user_group
    ------------------------------
    Number of conditions removed 1
    ------------------------------
    ```

### [29.8. Applying automember rules to existing entries using IdM CLI](#applying-automember-rules-to-existing-entries-using-idm-cli) {#applying-automember-rules-to-existing-entries-using-idm-cli .title}

Rebuild automatic membership in Identity Management (IdM) to apply automember rules retroactively to existing users and hosts. This ensures all entries are correctly assigned to groups based on current rule definitions.

Automember rules apply automatically to user and host entries created after the rules were added. They are not applied retroactively to entries that existed before the rules were added.

To apply automember rules to previously added entries, you have to manually rebuild automatic membership. Rebuilding automatic membership re-evaluates all existing automember rules and applies them either to all user or hosts entries, or to specific entries.

Rebuilding automatic membership **does not** remove user or host entries from groups, even if the entries no longer match the group's inclusive conditions. To remove them manually, see [Removing a member from a user group using IdM CLI](#removing-a-member-from-a-user-group-using-idm-cli "26.10. Removing a member from a user group using IdM CLI") or [Removing IdM host group members using the CLI](#removing-idm-host-group-members-using-the-cli "44.6. Removing IdM host group members using the CLI").

**Prerequisites**

-   You must be logged in as the administrator. For details, see link: [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

-   To rebuild automatic membership, enter the `ipa automember-rebuild`{.literal} command. Use the following options to specify the entries to target:

    -   To rebuild automatic membership for all users, use the `--type=group`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa automember-rebuild --type=group
        --------------------------------------------------------
        Automember rebuild task finished. Processed (9) entries.
        --------------------------------------------------------
        ```

    -   To rebuild automatic membership for all hosts, use the `--type=hostgroup`{.literal} option.

    -   To rebuild automatic membership for a specified user or users, use the `--users=`{.literal}*`target_user`{.literal}* option:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa automember-rebuild --users=target_user1 --users=target_user2
        --------------------------------------------------------
        Automember rebuild task finished. Processed (2) entries.
        --------------------------------------------------------
        ```

    -   To rebuild automatic membership for a specified host or hosts, use the `--hosts=`{.literal}*`client.idm.example.com`{.literal}* option.

### [29.9. Configuring a default automember group using IdM CLI](#configuring-a-default-automember-group-using-idm-cli) {#configuring-a-default-automember-group-using-idm-cli .title}

Configure a default automember group using the Identity Management (IdM) CLI to automatically assign users or hosts that don't match any automember rules to a fallback group. This ensures all entries have at least basic group membership and associated policies.

**Prerequisites**

-   You must be logged in as the administrator. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   The target group you want to set as default exists in IdM.

**Procedure**

1.  Enter the `ipa automember-default-group-set`{.literal} command to configure a default automember group.

2.  When prompted, specify:

    -   **Default (fallback) Group**, which specifies the target group name.

    -   **Grouping Type**, which specifies whether the target is a user group or a host group. To target a user group, enter **group**. To target a host group, enter **hostgroup**.

        For example:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa automember-default-group-set
        Default (fallback) Group: default_user_group
        Grouping Type: group
        ---------------------------------------------------
        Set default (fallback) group for automember "default_user_group"
        ---------------------------------------------------
          Default (fallback) Group: cn=default_user_group,cn=groups,cn=accounts,dc=example,dc=com
        ```

    Note

    To remove the current default automember group, enter the `ipa automember-default-group-remove`{.literal} command.

**Verification**

-   To verify that the group is set correctly, enter the `ipa automember-default-group-show`{.literal} command. The command displays the current default automember group. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa automember-default-group-show
    Grouping Type: group
      Default (fallback) Group: cn=default_user_group,cn=groups,cn=accounts,dc=example,dc=com
    ```

## [Chapter 30. Automating group membership using IdM Web UI](#automating-group-membership-using-idm-web-ui) {#chapter-30.-automating-group-membership-using-idm-web-ui .title}

Automate group membership in Identity Management (IdM) using the Web UI to assign users and hosts to groups based on their attributes. Automatic group membership reduces manual administration by sorting entries into groups as they are created.

For example, you can:

-   Divide employees\' user entries into groups based on the employees\' manager, location, or any other attribute.
-   Divide hosts based on their class, location, or any other attribute.
-   Add all users or all hosts to a single global group.

**Additional resources**

-   [Benefits of automatic group membership](#benefits-of-automatic-group-membership "29.1. Benefits of automatic group membership")

### [30.1. Adding an automember rule using IdM Web UI](#adding-an-automember-rule-using-idm-web-ui) {#adding-an-automember-rule-using-idm-web-ui .title}

Create automember rules in the Identity Management (IdM) Web UI to automatically assign new users or hosts to groups based on their attributes. This eliminates manual group assignment and ensures consistent group membership policies.

Existing entries are **not** affected by the new rule. If you want to change existing entries, see [Applying automember rules to existing entries using IdM Web UI](#applying-automember-rules-to-existing-entries-using-idm-web-ui "30.6. Applying automember rules to existing entries using IdM Web UI").

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must be a member of the `admins`{.literal} group.
-   The target group of the new rule exists in IdM.

**Procedure**

1.  Click **Identity → Automember**, and select either **User group rules** or **Host group rules**.
2.  Click **Add**.
3.  In the **Automember rule** field, select the group to which the rule will apply. This is the target group name.
4.  Click **Add** to confirm.
5.  Optional: You can add conditions to the new rule using the procedure described in [Adding a condition to an automember rule using IdM Web UI](#adding-a-condition-to-an-automember-rule-using-idm-web-ui "30.2. Adding a condition to an automember rule using IdM Web UI").

### [30.2. Adding a condition to an automember rule using IdM Web UI](#adding-a-condition-to-an-automember-rule-using-idm-web-ui) {#adding-a-condition-to-an-automember-rule-using-idm-web-ui .title}

Add conditions to automember rules in Identity Management (IdM) Web UI to automatically assign users or hosts to groups based on their attributes. This simplifies group management and ensures consistent group membership across your environment.

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must be a member of the `admins`{.literal} group.
-   The target rule exists in IdM.

**Procedure**

1.  Click **Identity → Automember**, and select either **User group rules** or **Host group rules**.

2.  Click on the rule to which you want to add a condition.

3.  In the **Inclusive** or **Exclusive** sections, click **Add**.

4.  In the **Attribute** field, select the required attribute, for example *uid*.

5.  In the **Expression** field, define a regular expression.

6.  Click **Add**.

    For example, the following condition targets all users with any value (.\*) in their user ID (uid) attribute.

### [30.3. Viewing existing automember rules and conditions using IdM Web UI](#viewing-existing-automember-rules-and-conditions-using-idm-web-ui) {#viewing-existing-automember-rules-and-conditions-using-idm-web-ui .title}

View automember rules and their conditions by using the Identity Management (IdM) Web UI to review which users or hosts are automatically added to specific groups.

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must be a member of the `admins`{.literal} group.

**Procedure**

1.  Click **Identity → Automember**, and select either **User group rules** or **Host group rules** to view the respective automember rules.
2.  Optional: Click on a rule to see the conditions for that rule in the **Inclusive** or **Exclusive** sections.

### [30.4. Deleting an automember rule using IdM Web UI](#deleting-an-automember-rule-using-idm-web-ui) {#deleting-an-automember-rule-using-idm-web-ui .title}

Delete automember rules using the Identity Management (IdM) WebUI to stop automatic group membership assignments. Removing obsolete rules ensures users and hosts are grouped according to current organizational requirements.

Deleting an automember rule also deletes all conditions associated with the rule. To remove only specific conditions from a rule, see [Removing a condition from an automember rule using IdM Web UI](#removing-a-condition-from-an-automember-rule-using-idm-web-ui "30.5. Removing a condition from an automember rule using IdM Web UI").

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must be a member of the `admins`{.literal} group.

**Procedure**

1.  Click **Identity → Automember**, and select either **User group rules** or **Host group rules** to view the respective automember rules.
2.  Select the checkbox next to the rule you want to remove.
3.  Click **Delete**.
4.  Click **Delete** to confirm.

### [30.5. Removing a condition from an automember rule using IdM Web UI](#removing-a-condition-from-an-automember-rule-using-idm-web-ui) {#removing-a-condition-from-an-automember-rule-using-idm-web-ui .title}

Delete specific conditions from automember rules using the Identity Management (IdM) WebUI to refine automatic group membership criteria.

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must be a member of the `admins`{.literal} group.

**Procedure**

1.  Click **Identity → Automember**, and select either **User group rules** or **Host group rules** to view the respective automember rules.
2.  Click on a rule to see the conditions for that rule in the **Inclusive** or **Exclusive** sections.
3.  Select the checkbox next to the conditions you want to remove.
4.  Click **Delete**.
5.  Click **Delete** to confirm.

### [30.6. Applying automember rules to existing entries using IdM Web UI](#applying-automember-rules-to-existing-entries-using-idm-web-ui) {#applying-automember-rules-to-existing-entries-using-idm-web-ui .title}

Rebuild automatic membership in the IdM Web UI to apply automember rules to user and host entries that existed before the rules were created. This is necessary because automember rules only apply automatically to new entries.

When you rebuild automatic membership, IdM re-evaluates all existing automember rules and applies them either to all user or host entries, or to specific entries that you select.

Note that rebuilding automatic membership **does not** remove entries from groups, even if the entries no longer match the group's inclusive conditions. You can remove them manually using the IdM Web UI.

**Additional resources**

-   [Removing a member from a user group using IdM Web UI](#removing-a-member-from-a-user-group-using-idm-web-ui "27.8. Removing a member from a user group using IdM Web UI")
-   [Removing host group members in the IdM Web UI](#removing-host-group-members-in-the-idm-web-ui "45.5. Removing host group members in the IdM Web UI")

#### [30.6.1. Rebuilding automatic membership for all users or hosts](#rebuilding-automatic-membership-for-all-users-or-hosts) {#rebuilding-automatic-membership-for-all-users-or-hosts .title}

Recalculate and apply automember rules to all users or hosts to correct group memberships after rule changes. This bulk operation ensures all entries belong to the correct groups based on current automember conditions.

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must be a member of the `admins`{.literal} group.

**Procedure**

1.  Select **Identity** → **Users** or **Hosts**.

2.  Click **Actions** → **Rebuild auto membership**.

#### [30.6.2. Rebuilding automatic membership for a single user or host only](#rebuilding-automatic-membership-for-a-single-user-or-host-only) {#rebuilding-automatic-membership-for-a-single-user-or-host-only .title}

Recalculate and apply automember rules to a specific user or host to correct group memberships after rule changes. This ensures the entry belongs to the correct groups based on current automember conditions.

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must be a member of the `admins`{.literal} group.

**Procedure**

1.  Select **Identity** → **Users** or **Hosts**.

2.  Click on the required user or host name.

3.  Click **Actions** → **Rebuild auto membership**.

### [30.7. Configuring a default user group using IdM Web UI](#configuring-a-default-user-group-using-idm-web-ui) {#configuring-a-default-user-group-using-idm-web-ui .title}

Configure a default user group using the Identity Management (IdM) Web UI to automatically assign users that don't match any automember rules to a fallback group. This ensures all users have at least basic group membership and associated policies.

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must be a member of the `admins`{.literal} group.
-   The target user group you want to set as default exists in IdM.

**Procedure**

1.  Click **Identity → Automember**, and select **User group rules**.
2.  In the **Default user group** field, select the group you want to set as the default user group.

### [30.8. Configuring a default host group using IdM Web UI](#configuring-a-default-host-group-using-idm-web-ui) {#configuring-a-default-host-group-using-idm-web-ui .title}

Configure a default host group using the Identity Management (IdM) Web UI to automatically assign hosts that don't match any automember rules to a fallback group. This ensures all hosts have at least basic group membership and associated policies.

**Prerequisites**

-   You are logged in to the IdM Web UI.
-   You must be a member of the `admins`{.literal} group.
-   The target host group you want to set as default exists in IdM.

**Procedure**

1.  Click **Identity → Automember**, and select **Host group rules**.
2.  In the **Default host group** field, select the group you want to set as the default host group.

## [Chapter 31. Using Ansible to automate group membership in IdM](#using-ansible-to-automate-group-membership-in-idm) {#chapter-31.-using-ansible-to-automate-group-membership-in-idm .title}

Configure automember rules using Ansible to automatically assign users and hosts to groups based on their attributes, reducing manual administration. For example, you can:

-   Divide employees\' user entries into groups based on the employees\' manager, location, position or any other attribute.
-   Divide hosts into groups based on their class, location, or any other attribute.
-   Add all users or all hosts to a single global group.

### [31.1. Using Ansible to ensure that an automember rule for an IdM user group is present](#using-ansible-to-ensure-that-an-automember-rule-for-an-idm-user-group-is-present) {#using-ansible-to-ensure-that-an-automember-rule-for-an-idm-user-group-is-present .title}

Create automember rules for Identity Management (IdM) user groups using Ansible to automate the assignment of new users to groups based on their attributes.

In the example below, you ensure the presence of an `automember`{.literal} rule for the **testing_group** user group.

**Prerequisites**

-   The **testing_group** user group exists in IdM.

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Copy the `automember-group-present.yml`{.literal} Ansible playbook file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember/automember-group-present.yml automember-group-present-copy.yml
    ```

3.  Open the `automember-group-present-copy.yml`{.literal} file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipaautomember`{.literal} task section:

    -   Set the `ipaadmin_password`{.literal} variable to the password of the IdM `admin`{.literal}.
    -   Set the `name`{.literal} variable to **testing_group**.
    -   Set the `automember_type`{.literal} variable to **group**.
    -   Ensure that the `state`{.literal} variable is set to `present`{.literal}.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Automember group present example
      hosts: ipaserver
      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure group automember rule admins is present
        freeipa.ansible_freeipa.ipaautomember:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: testing_group
          automember_type: group
          state: present
    ```

5.  Save the file.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory automember-group-present-copy.yml
    ```

### [31.2. Using Ansible to ensure that a specified condition is present in an IdM user group automember rule](#using-ansible-to-ensure-that-a-specified-condition-is-present-in-an-idm-user-group-automember-rule) {#using-ansible-to-ensure-that-a-specified-condition-is-present-in-an-idm-user-group-automember-rule .title}

Add conditions to Identity Management (IdM) user group automember rules using Ansible to define criteria for automatic group membership based on user attributes.

In the example below, you ensure the presence of a UID-related condition in the `automember`{.literal} rule for the **testing_group** group. By specifying the **.\*** condition, you ensure that all future IdM users automatically become members of the **testing_group**.

**Prerequisites**

-   The **testing_group** user group and automember user group rule exist in IdM.

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Copy the `automember-hostgroup-rule-present.yml`{.literal} Ansible playbook file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember/`{.literal} directory and name it, for example, **automember-usergroup-rule-present.yml**:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember/automember-hostgroup-rule-present.yml automember-usergroup-rule-present.yml
    ```

3.  Open the `automember-usergroup-rule-present.yml`{.literal} file for editing.

4.  Adapt the file by modifying the following parameters:

    -   Rename the playbook to correspond to your use case, for example: **Automember user group rule member present**.

    -   Rename the task to correspond to your use case, for example: **Ensure an automember condition for a user group is present**.

    -   Set the following variables in the `freeipa.ansible_freeipa.ipaautomember`{.literal} task section:

        -   Set the `ipaadmin_password`{.literal} variable to the password of the IdM `admin`{.literal}.
        -   Set the `name`{.literal} variable to **testing_group**.
        -   Set the `automember_type`{.literal} variable to `group`{.literal}.
        -   Ensure that the `state`{.literal} variable is set to `present`{.literal}.
        -   Ensure that the `action`{.literal} variable is set to `member`{.literal}.
        -   Set the `inclusive`{.literal} `key`{.literal} variable to `UID`{.literal}.
        -   Set the `inclusive`{.literal} `expression`{.literal} variable to **.**\*

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Automember user group rule member present
      hosts: ipaserver
      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure an automember condition for a user group is present
        freeipa.ansible_freeipa.ipaautomember:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: testing_group
          automember_type: group
          state: present
          action: member
          inclusive:
            - key: UID
              expression: .*
    ```

5.  Save the file.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory automember-usergroup-rule-present.yml
    ```

**Verification**

1.  Log in as an IdM administrator.

    ``` {.language-plaintext tabindex="-1"}
    $ kinit admin
    ```

2.  Add a user, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-add user101 --first user --last 101
    -----------------------
    Added user "user101"
    -----------------------
      User login: user101
      First name: user
      Last name: 101
      ...
      Member of groups: ipausers, testing_group
      ...
    ```

### [31.3. Using Ansible to ensure that a condition is absent from an IdM user group automember rule](#using-ansible-to-ensure-that-a-condition-is-absent-from-an-idm-user-group-automember-rule) {#using-ansible-to-ensure-that-a-condition-is-absent-from-an-idm-user-group-automember-rule .title}

Remove conditions from Identity Management (IdM) user group automember rules using Ansible to prevent specific users from being automatically added to groups.

In the example below, you ensure the absence of a condition in the `automember`{.literal} rule that specifies that users whose `initials`{.literal} are **dp** should be included. The automember rule is applied to the **testing_group** group. By applying the condition, you ensure that no future IdM user whose initials are **dp** becomes a member of the **testing_group**.

**Prerequisites**

-   The **testing_group** user group and automember user group rule exist in IdM.

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Copy the `automember-hostgroup-rule-absent.yml`{.literal} Ansible playbook file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember/`{.literal} directory and name it, for example, **automember-usergroup-rule-absent.yml**:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember/automember-hostgroup-rule-absent.yml automember-usergroup-rule-absent.yml
    ```

3.  Open the `automember-usergroup-rule-absent.yml`{.literal} file for editing.

4.  Adapt the file by modifying the following parameters:

    -   Rename the playbook to correspond to your use case, for example: **Automember user group rule member absent**.

    -   Rename the task to correspond to your use case, for example: **Ensure an automember condition for a user group is absent**.

    -   Set the following variables in the `freeipa.ansible_freeipa.ipaautomember`{.literal} task section:

        -   Set the `ipaadmin_password`{.literal} variable to the password of the IdM `admin`{.literal}.
        -   Set the `name`{.literal} variable to **testing_group**.
        -   Set the `automember_type`{.literal} variable to **group**.
        -   Ensure that the `state`{.literal} variable is set to `absent`{.literal}.
        -   Ensure that the `action`{.literal} variable is set to `member`{.literal}.
        -   Set the `inclusive`{.literal} `key`{.literal} variable to `initials`{.literal}.
        -   Set the `inclusive`{.literal} `expression`{.literal} variable to **dp**.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Automember user group rule member absent
      hosts: ipaserver
      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure an automember condition for a user group is absent
        freeipa.ansible_freeipa.ipaautomember:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: testing_group
          automember_type: group
          state: absent
          action: member
          inclusive:
            - key: initials
              expression: dp
    ```

5.  Save the file.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory automember-usergroup-rule-absent.yml
    ```

**Verification**

1.  Log in as an IdM administrator.

    ``` {.language-plaintext tabindex="-1"}
    $ kinit admin
    ```

2.  View the automember group:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa automember-show --type=group testing_group
     Automember Rule: testing_group
    ```

The absence of an `Inclusive Regex: initials=dp`{.literal} entry in the output confirms that the **testing_group** automember rule does not contain the condition specified.

### [31.4. Using Ansible to ensure that an automember rule for an IdM user group is absent](#using-ansible-to-ensure-that-an-automember-rule-for-an-idm-user-group-is-absent) {#using-ansible-to-ensure-that-an-automember-rule-for-an-idm-user-group-is-absent .title}

Delete automember rules for Identity Management (IdM) user groups using Ansible to disable automatic group assignment based on user attributes.

In the example below, you ensure the absence of an `automember`{.literal} rule for the **testing_group** group.

Note

Deleting an automember rule also deletes all conditions associated with the rule. To remove only specific conditions from a rule, see [Using Ansible to ensure that a condition is absent in an IdM user group automember rule](#using-ansible-to-ensure-that-a-condition-is-absent-from-an-idm-user-group-automember-rule "31.3. Using Ansible to ensure that a condition is absent from an IdM user group automember rule").

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Copy the `automember-group-absent.yml`{.literal} Ansible playbook file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember/automember-group-absent.yml automember-group-absent-copy.yml
    ```

3.  Open the `automember-group-absent-copy.yml`{.literal} file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipaautomember`{.literal} task section:

    -   Set the `ipaadmin_password`{.literal} variable to the password of the IdM `admin`{.literal}.

    -   Set the `name`{.literal} variable to **testing_group**.

    -   Set the `automember_type`{.literal} variable to **group**.

    -   Ensure that the `state`{.literal} variable is set to `absent`{.literal}.

        This is the modified Ansible playbook file for the current example:

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Automember group absent example
          hosts: ipaserver
          vars_files:
          - /home/user_name/MyPlaybooks/secret.yml
          tasks:
          - name: Ensure group automember rule admins is absent
            freeipa.ansible_freeipa.ipaautomember:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: testing_group
              automember_type: group
              state: absent
        ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-automember.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember`{.literal} directory on the control node.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory automember-group-absent.yml
    ```

### [31.5. Using Ansible to ensure that a condition is present in an IdM host group automember rule](#using-ansible-to-ensure-that-a-condition-is-present-in-an-idm-host-group-automember-rule) {#using-ansible-to-ensure-that-a-condition-is-present-in-an-idm-host-group-automember-rule .title}

Add conditions to Identity Management (IdM) host group automember rules using Ansible to automatically assign hosts to groups based on their attributes such as FQDN patterns.

In the example, you ensure that hosts with the `FQDN`{.literal} of **.\*.idm.example.com** are members of the **primary_dns_domain_hosts** host group and hosts whose `FQDN`{.literal} is **.\*.example.org** are not members of the **primary_dns_domain_hosts** host group.

**Prerequisites**

-   The **primary_dns_domain_hosts** host group and automember host group rule exist in IdM.

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Copy the `automember-hostgroup-rule-present.yml`{.literal} Ansible playbook file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember/automember-hostgroup-rule-present.yml automember-hostgroup-rule-present-copy.yml
    ```

3.  Open the `automember-hostgroup-rule-present-copy.yml`{.literal} file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipaautomember`{.literal} task section:

    -   Set the `ipaadmin_password`{.literal} variable to the password of the IdM `admin`{.literal}.
    -   Set the `name`{.literal} variable to **primary_dns_domain_hosts**.
    -   Set the `automember_type`{.literal} variable to **hostgroup**.
    -   Ensure that the `state`{.literal} variable is set to `present`{.literal}.
    -   Ensure that the `action`{.literal} variable is set to `member`{.literal}.
    -   Ensure that the `inclusive`{.literal} `key`{.literal} variable is set to `fqdn`{.literal}.
    -   Set the corresponding `inclusive`{.literal} `expression`{.literal} variable to **.\*.idm.example.com**.
    -   Set the `exclusive`{.literal} `key`{.literal} variable to `fqdn`{.literal}.
    -   Set the corresponding `exclusive`{.literal} `expression`{.literal} variable to **.\*.example.org**.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Automember user group rule member present
      hosts: ipaserver
      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure an automember condition for a user group is present
        freeipa.ansible_freeipa.ipaautomember:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: primary_dns_domain_hosts
          automember_type: hostgroup
          state: present
          action: member
          inclusive:
            - key: fqdn
              expression: .*.idm.example.com
          exclusive:
            - key: fqdn
              expression: .*.example.org
    ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-automember.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automember`{.literal} directory on the control node.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory automember-hostgroup-rule-present-copy.yml
    ```

### [31.6. Additional resources](#using-ansible-to-automate-group-membership-in-idm_316-additional-resources) {#additional-resources-12 .title}

-   [Automating group membership using IdM CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/automating-group-membership-using-idm-cli)

## [Chapter 32. Delegating permissions to user groups to manage users using IdM CLI](#delegating-permissions-to-user-groups-to-manage-users-using-idm-cli) {#chapter-32.-delegating-permissions-to-user-groups-to-manage-users-using-idm-cli .title}

Delegation is one of the access control methods in Identity Management (IdM), along with self-service rules and role-based access control (RBAC). You can use delegation to assign permissions to one group of users to manage entries for another group of users.

### [32.1. Delegation rules](#delegation-rules) {#delegation-rules .title}

You can delegate permissions to user groups to manage users by creating **delegation rules** in Identity Management (IdM).

Delegation rules allow a specific user group to perform write (edit) operations on specific attributes for users in another user group. This form of access control rule is limited to editing the values of a subset of attributes you specify in a delegation rule; it does not grant the ability to add or remove whole entries or control over unspecified attributes.

Delegation rules grant permissions to existing user groups in IdM. You can use delegation to, for example, allow the `managers`{.literal} user group to manage selected attributes of users in the `employees`{.literal} user group.

### [32.2. Creating a delegation rule using IdM CLI](#creating-a-delegation-rule-using-idm-cli) {#creating-a-delegation-rule-using-idm-cli .title}

Create delegation rules using the Identity Management (IdM) CLI to grant specific user groups permission to manage other users. You can distribute administrative tasks across your organization while maintaining centralized oversight.

**Prerequisites**

-   You are logged in as a member of the `admins`{.literal} group.

**Procedure**

-   Enter the `ipa delegation-add`{.literal} command. Specify the following options:

    -   `--group`{.literal}: the group who *is being granted permissions* to the entries of users in the user group.

    -   `--membergroup`{.literal}: the group *whose entries can be edited* by members of the delegation group.

    -   `--permissions`{.literal}: whether users will have the right to view the given attributes (*read*) and add or change the given attributes (*write*). If you do not specify permissions, only the *write* permission will be added.

    -   `--attrs`{.literal}: the attributes which users in the member group are allowed to view or edit.

        For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa delegation-add "basic manager attributes" --permissions=read --permissions=write --attrs=businesscategory --attrs=departmentnumber --attrs=employeetype --attrs=employeenumber --group=managers --membergroup=employees
    -------------------------------------------
    Added delegation "basic manager attributes"
    -------------------------------------------
      Delegation name: basic manager attributes
      Permissions: read, write
      Attributes: businesscategory, departmentnumber, employeetype, employeenumber
      Member user group: employees
      User group: managers
    ```

### [32.3. Viewing existing delegation rules using IdM CLI](#viewing-existing-delegation-rules-using-idm-cli) {#viewing-existing-delegation-rules-using-idm-cli .title}

View delegation rules by using the Identity Management (IdM) CLI to review which user groups have permissions to modify attributes of other groups.

**Prerequisites**

-   You are logged in as a member of the `admins`{.literal} group.

**Procedure**

-   Enter the `ipa delegation-find`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa delegation-find
    --------------------
    1 delegation matched
    --------------------
      Delegation name: basic manager attributes
      Permissions: read, write
      Attributes: businesscategory, departmentnumber, employeenumber, employeetype
      Member user group: employees
      User group: managers
    ----------------------------
    Number of entries returned 1
    ----------------------------
    ```

### [32.4. Modifying a delegation rule using IdM CLI](#modifying-a-delegation-rule-using-idm-cli) {#modifying-a-delegation-rule-using-idm-cli .title}

Update delegation rules using the Identity Management (IdM) CLI to adjust which groups can manage which attributes of a target group.

Important

The `--attrs`{.literal} option overwrites whatever the previous list of supported attributes was, so always include the complete list of attributes along with any new attributes. This also applies to the `--permissions`{.literal} option.

**Prerequisites**

-   You are logged in as a member of the `admins`{.literal} group.

**Procedure**

-   Enter the `ipa delegation-mod`{.literal} command with the desired changes. For example, to add the `displayname`{.literal} attribute to the `basic manager attributes`{.literal} example rule:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa delegation-mod "basic manager attributes" --attrs=businesscategory --attrs=departmentnumber --attrs=employeetype --attrs=employeenumber --attrs=displayname
    ----------------------------------------------
    Modified delegation "basic manager attributes"
    ----------------------------------------------
      Delegation name: basic manager attributes
      Permissions: read, write
      Attributes: businesscategory, departmentnumber, employeetype, employeenumber, displayname
      Member user group: employees
      User group: managers
    ```

### [32.5. Deleting a delegation rule using IdM CLI](#deleting-a-delegation-rule-using-idm-cli) {#deleting-a-delegation-rule-using-idm-cli .title}

Delete delegation rules using the Identity Management (IdM) CLI to revoke user group permissions for managing other users. Removing unnecessary delegation rules helps maintain proper access control.

**Prerequisites**

-   You are logged in as a member of the `admins`{.literal} group.

**Procedure**

-   Enter the `ipa delegation-del`{.literal} command.

-   When prompted, enter the name of the delegation rule you want to delete:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa delegation-del
    Delegation name: basic manager attributes
    ---------------------------------------------
    Deleted delegation "basic manager attributes"
    ---------------------------------------------
    ```

## [Chapter 33. Delegating permissions to user groups to manage users using IdM WebUI](#delegating-permissions-to-user-groups-to-manage-users-using-idm-webui) {#chapter-33.-delegating-permissions-to-user-groups-to-manage-users-using-idm-webui .title}

Delegation is one of the access control methods in Identity Management (IdM), along with self-service rules and role-based access control (RBAC). You can use delegation to assign permissions to one group of users to manage entries for another group of users.

### [33.1. Creating a delegation rule using IdM WebUI](#creating-a-delegation-rule-using-idm-webui) {#creating-a-delegation-rule-using-idm-webui .title}

Create delegation rules using the Identity Management (IdM) WebUI to grant specific user groups permission to manage other users. You can distribute administrative tasks across your organization while maintaining centralized oversight.

**Prerequisites**

-   You are logged in to the IdM Web UI as a member of the `admins`{.literal} group.

**Procedure**

1.  From the **IPA Server\>Role-Based Access Control** menu, click **Delegations**.

2.  Click **Add**.

3.  On the **Add delegation** window, do the following:

    a.  Name the new delegation rule.
    b.  Set the permissions by selecting the checkboxes that indicate whether users will have the right to view the given attributes (*read*) and add or change the given attributes (*write*).
    c.  From the **User group** drop-down menu, select the group *who is being granted permissions* to view or edit the entries of users in the member group.
    d.  On the **Member user group** drop-down menu, select the group *whose entries can be edited* by members of the delegation group.
    e.  In the attributes box, select the checkboxes by the attributes to which you want to grant permissions.
    f.  Click the **Add** button to save the new delegation rule.

### [33.2. Viewing existing delegation rules using IdM WebUI](#viewing-existing-delegation-rules-using-idm-webui) {#viewing-existing-delegation-rules-using-idm-webui .title}

View delegation rules by using the Identity Management (IdM) WebUI to review which user groups have permissions to modify attributes of other groups.

**Prerequisites**

-   You are logged in to the IdM Web UI as a member of the `admins`{.literal} group.

**Procedure**

-   From the **IPA Server\>Role-Based Access Control** menu, click **Delegations**.

### [33.3. Modifying a delegation rule using IdM WebUI](#modifying-a-delegation-rule-using-idm-webui) {#modifying-a-delegation-rule-using-idm-webui .title}

Update delegation rules using the Identity Management (IdM) WebUI to adjust which groups can manage attributes of other groups.

**Prerequisites**

-   You are logged in to the IdM Web UI as a member of the `admins`{.literal} group.

**Procedure**

1.  From the **IPA Server\>Role-Based Access Control** menu, click **Delegations**.

2.  Click the rule you want to modify.

3.  Make the desired changes:

    -   Change the name of the rule.
    -   Change granted permissions by selecting the checkboxes that indicate whether users will have the right to view the given attributes (*read*) and add or change the given attributes (*write*).
    -   In the User group drop-down menu, select the group *who is being granted permissions* to view or edit the entries of users in the member group.
    -   In the **Member user group** drop-down menu, select the group *whose entries can be edited* by members of the delegation group.
    -   In the attributes box, select the checkboxes by the attributes to which you want to grant permissions. To remove permissions to an attribute, uncheck the relevant checkbox.
    -   Click the **Save** button to save the changes.

### [33.4. Deleting a delegation rule using IdM WebUI](#deleting-a-delegation-rule-using-idm-webui) {#deleting-a-delegation-rule-using-idm-webui .title}

Delete delegation rules using the Identity Management (IdM) WebUI to revoke user group permissions for managing other users. Removing unnecessary delegation rules helps maintain proper access control.

**Prerequisites**

-   You are logged in to the IdM Web UI as a member of the `admins`{.literal} group.

**Procedure**

1.  From the **IPA Server\>Role-Based Access Control** menu, click **Delegations**.
2.  Select the checkbox next to the rule you want to remove.
3.  Click **Delete**.
4.  Click **Delete** to confirm.

### [33.5. Additional resources](#delegating-permissions-to-user-groups-to-manage-users-using-idm-webui_335-additional-resources) {#additional-resources-13 .title}

-   [Delegation rules](#delegation-rules "32.1. Delegation rules")

## [Chapter 34. Delegating permissions to user groups to manage users using Ansible playbooks](#delegating-permissions-to-user-groups-to-manage-users-using-ansible-playbooks) {#chapter-34.-delegating-permissions-to-user-groups-to-manage-users-using-ansible-playbooks .title}

Configure delegation rules using Ansible to grant one user group permission to manage entries for another group, distributing administrative responsibilities.

Delegation is one of the access control methods in Identity Management (IdM), along with self-service rules and role-based access control (RBAC).

### [34.1. Using Ansible to ensure that a delegation rule is present](#using-ansible-to-ensure-that-a-delegation-rule-is-present) {#using-ansible-to-ensure-that-a-delegation-rule-is-present .title}

Create delegation rules in Identity Management (IdM) using Ansible to grant one user group permission to manage specific attributes of another group's members.

In the example, the new **basic manager attributes** delegation rule grants the `managers`{.literal} group the ability to read and write the following attributes for members of the `employees`{.literal} group:

-   `businesscategory`{.literal}
-   `departmentnumber`{.literal}
-   `employeenumber`{.literal}
-   `employeetype`{.literal}

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `delegation-present.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/delegation/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/delegation/delegation-present.yml delegation-present-copy.yml
    ```

3.  Open the `delegation-present-copy.yml`{.literal} Ansible playbook file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipadelegation`{.literal} task section:

    -   Set the `name`{.literal} variable to the name of the new delegation rule.
    -   Set the `permission`{.literal} variable to a comma-separated list of permissions to grant: `read`{.literal} and `write`{.literal}.
    -   Set the `attribute`{.literal} variable to a list of attributes the delegated user group can manage: `businesscategory`{.literal}, `departmentnumber`{.literal}, `employeenumber`{.literal}, and `employeetype`{.literal}.
    -   Set the `group`{.literal} variable to the name of the group that is being given access to view or modify attributes.
    -   Set the `membergroup`{.literal} variable to the name of the group whose attributes can be viewed or modified.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to manage a delegation rule
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure delegation "basic manager attributes" is present
        freeipa.ansible_freeipa.ipadelegation:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: "basic manager attributes"
          permission: read, write
          attribute:
          - businesscategory
          - departmentnumber
          - employeenumber
          - employeetype
          group: managers
          membergroup: employees
    ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-delegation.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/ipadelegation`{.literal} directory on the control node.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i ~/MyPlaybooks/inventory delegation-present-copy.yml
    ```

**Additional resources**

-   [Delegation rules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/delegating-permissions-to-user-groups-to-manage-users-using-idm-cli#delegation-rules)

### [34.2. Using Ansible to ensure that a delegation rule is absent](#using-ansible-to-ensure-that-a-delegation-rule-is-absent) {#using-ansible-to-ensure-that-a-delegation-rule-is-absent .title}

Remove delegation rules from Identity Management (IdM) using Ansible to revoke a user group's permission to manage attributes of another group's members.

The example below describes how to make sure the custom **basic manager attributes** delegation rule does not exist in IdM.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks>/
    ```

2.  Make a copy of the `delegation-absent.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/delegation/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/delegation/delegation-present.yml delegation-absent-copy.yml
    ```

3.  Open the `delegation-absent-copy.yml`{.literal} Ansible playbook file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipadelegation`{.literal} task section:

    -   Set the `name`{.literal} variable to the name of the delegation rule.
    -   Set the `state`{.literal} variable to `absent`{.literal}.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Delegation absent
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure delegation "basic manager attributes" is absent
        freeipa.ansible_freeipa.ipadelegation:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: "basic manager attributes"
          state: absent
    ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-delegation.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/ipadelegation`{.literal} directory on the control node.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i ~/MyPlaybooks/inventory delegation-absent-copy.yml
    ```

**Additional resources**

-   [Delegation rules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/delegating-permissions-to-user-groups-to-manage-users-using-idm-cli#delegation-rules)

### [34.3. Using Ansible to ensure that a delegation rule has specific attributes](#using-ansible-to-ensure-that-a-delegation-rule-has-specific-attributes) {#using-ansible-to-ensure-that-a-delegation-rule-has-specific-attributes .title}

Add attributes to existing Identity Management (IdM) delegation rules using Ansible to modify which user entry fields a group can manage for another group's members.

In the example below, you ensure the **basic manager attributes** delegation rule only has the `departmentnumber`{.literal} member attribute.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

-   The **basic manager attributes** delegation rule exists in IdM.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `delegation-member-present.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/delegation/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/delegation/delegation-member-present.yml delegation-member-present-copy.yml
    ```

3.  Open the `delegation-member-present-copy.yml`{.literal} Ansible playbook file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipadelegation`{.literal} task section:

    -   Set the `name`{.literal} variable to the name of the delegation rule to modify.
    -   Set the `attribute`{.literal} variable to `departmentnumber`{.literal}.
    -   Set the `action`{.literal} variable to `member`{.literal}.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Delegation member present
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure delegation "basic manager attributes" member attribute departmentnumber is present
        freeipa.ansible_freeipa.ipadelegation:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: "basic manager attributes"
          attribute:
          - departmentnumber
          action: member
    ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-delegation.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/ipadelegation`{.literal} directory on the control node.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i ~/MyPlaybooks/inventory delegation-member-present-copy.yml
    ```

**Additional resources**

-   [Delegation rules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/delegating-permissions-to-user-groups-to-manage-users-using-idm-cli#delegation-rules)

### [34.4. Using Ansible to ensure that a delegation rule does not have specific attributes](#using-ansible-to-ensure-that-a-delegation-rule-does-not-have-specific-attributes) {#using-ansible-to-ensure-that-a-delegation-rule-does-not-have-specific-attributes .title}

Remove attributes from existing Identity Management (IdM) delegation rules using Ansible to restrict which user entry fields a group can manage for another group's members, limiting undesired access.

In the example, you ensure the **basic manager attributes** delegation rule does not have the `employeenumber`{.literal} and `employeetype`{.literal} member attributes.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

-   The **basic manager attributes** delegation rule exists in IdM.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `delegation-member-absent.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/delegation/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/delegation/delegation-member-absent.yml delegation-member-absent-copy.yml
    ```

3.  Open the `delegation-member-absent-copy.yml`{.literal} Ansible playbook file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipadelegation`{.literal} task section:

    -   Set the `name`{.literal} variable to the name of the delegation rule to modify.
    -   Set the `attribute`{.literal} variable to `employeenumber`{.literal} and `employeetype`{.literal}.
    -   Set the `action`{.literal} variable to `member`{.literal}.
    -   Set the `state`{.literal} variable to `absent`{.literal}.

    This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Delegation member absent
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure delegation "basic manager attributes" member attributes employeenumber and employeetype are absent
        freeipa.ansible_freeipa.ipadelegation:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: "basic manager attributes"
          attribute:
          - employeenumber
          - employeetype
          action: member
          state: absent
    ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-delegation.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/ipadelegation`{.literal} directory on the control node.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i ~/MyPlaybooks/inventory delegation-member-absent-copy.yml
    ```

**Additional resources**

-   [Delegation rules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/delegating-permissions-to-user-groups-to-manage-users-using-idm-cli#delegation-rules)

### [34.5. Additional resources](#delegating-permissions-to-user-groups-to-manage-users-using-ansible-playbooks_345-additional-resources) {#additional-resources-14 .title}

-   [Delegation rules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/delegating-permissions-to-user-groups-to-manage-users-using-idm-cli#delegation-rules)

## [Chapter 35. Managing role-based access controls in IdM using the CLI](#managing-role-based-access-controls-in-idm-using-the-cli) {#chapter-35.-managing-role-based-access-controls-in-idm-using-the-cli .title}

Manage role-based access control (RBAC) in Identity Management (IdM) using the CLI to restrict administrative access to authorized users. Define roles with specific permissions and assign them to users to enforce the principle of least privilege.

### [35.1. Role-based access control in IdM](#role-based-access-control-in-idm) {#role-based-access-control-in-idm .title}

Use role-based access control (RBAC) in Identity Management (IdM) to grant fine-grained administrative authority to users through permissions, privileges, and roles. RBAC provides more granular control than self-service and delegation access methods.

Role-based access control is composed of three parts:

-   **Permissions** grant the right to perform a specific task such as adding or deleting users, modifying a group, and enabling read-access.
-   **Privileges** combine permissions, for example all the permissions needed to add a new user.
-   **Roles** grant a set of privileges to users, user groups, hosts or host groups.

#### [35.1.1. Permissions in IdM](#permissions-in-idm) {#permissions-in-idm .title}

IdM permissions define specific operations on LDAP entries as the base unit of role-based access control (RBAC). Functioning as foundational building blocks of IdM, permissions can be assigned to multiple privileges.

One or more **rights** define what operations are allowed:

-   `write`{.literal}
-   `read`{.literal}
-   `search`{.literal}
-   `compare`{.literal}
-   `add`{.literal}
-   `delete`{.literal}
-   `all`{.literal}

These operations apply to three basic **targets**:

-   `subtree`{.literal}: a domain name (DN); the subtree under this DN
-   `target filter`{.literal}: an LDAP filter
-   `target`{.literal}: DN with possible wildcards to specify entries

Additionally, the following convenience options set the corresponding attribute(s):

-   `type`{.literal}: a type of object (user, group, etc); sets `subtree`{.literal} and `target filter`{.literal}

-   `memberof`{.literal}: members of a group; sets a `target filter`{.literal}

    Note

    Setting the `memberof`{.literal} attribute permission is not applied if the target LDAP entry does not contain any reference to group membership.

-   `targetgroup`{.literal}: grants access to modify a specific group (such as granting the rights to manage group membership); sets a `target`{.literal}

With IdM permissions, you can control which users have access to which objects and even which attributes of these objects. IdM enables you to allow or block individual attributes or change the entire visibility of a specific IdM function, such as users, groups, or sudo, to all anonymous users, all authenticated users, or just a certain group of privileged users.

For example, the flexibility of this approach to permissions is useful for an administrator who wants to limit access of users or groups only to the specific sections these users or groups need to access and to make the other sections completely hidden to them.

Note

A permission cannot contain other permissions.

#### [35.1.2. Default managed permissions](#default-managed-permissions) {#default-managed-permissions .title}

Understand how IdM managed permissions differ from user-created permissions and how to extend them with included or excluded attributes.

Managed permissions are permissions that come by default with IdM. They behave like other permissions created by the user, with the following differences:

-   You cannot delete them or modify their name, location, and target attributes.

-   They have three sets of attributes:

    -   **Default** attributes, the user cannot modify them, as they are managed by IdM
    -   **Included** attributes, which are additional attributes added by the user
    -   **Excluded** attributes, which are attributes removed by the user

A managed permission applies to all attributes that appear in the default and included attribute sets but not in the excluded set.

Note

While you cannot delete a managed permission, setting its bind type to permission and removing the managed permission from all privileges effectively disables it.

Names of all managed permissions start with `System:`{.literal}, for example `System: Add Sudo rule`{.literal} or `System: Modify Services`{.literal}. Earlier versions of IdM used a different scheme for default permissions. For example, the user could not delete them and was only able to assign them to privileges. Most of these default permissions have been turned into managed permissions, however, the following permissions still use the previous scheme:

-   Add Automember Rebuild Membership Task
-   Add Configuration Sub-Entries
-   Add Replication Agreements
-   Certificate Remove Hold
-   Get Certificates status from the CA
-   Read DNA Range
-   Modify DNA Range
-   Read PassSync Managers Configuration
-   Modify PassSync Managers Configuration
-   Read Replication Agreements
-   Modify Replication Agreements
-   Remove Replication Agreements
-   Read LDBM Database Configuration
-   Request Certificate
-   Request Certificate ignoring CA ACLs
-   Request Certificates from a different host
-   Retrieve Certificates from the CA
-   Revoke Certificate
-   Write IPA Configuration

Note

If you attempt to modify a managed permission from the command line, the system does not allow you to change the attributes that you cannot modify, the command fails. If you attempt to modify a managed permission from the Web UI, the attributes that you cannot modify are disabled.

#### [35.1.3. Privileges in IdM](#privileges-in-idm) {#privileges-in-idm .title}

IdM privileges combine multiple permissions required for specific administrative tasks, such as creating users or managing groups.

While a permission provides the rights to do a single operation, there are certain IdM tasks that require multiple permissions to succeed. Therefore, a privilege combines the different permissions required to perform a specific task.

For example, setting up an account for a new IdM user requires the following permissions:

-   Creating a new user entry
-   Resetting a user password
-   Adding the new user to the default IPA users group

Combining these three low-level tasks into a higher level task in the form of a custom privilege named, for example, **Add User** makes it easier for a system administrator to manage roles. IdM already contains several default privileges. Apart from users and user groups, privileges are also assigned to hosts and host groups, as well as network services. This practice permits a fine-grained control of operations by a set of users on a set of hosts using specific network services.

Note

A privilege may not contain other privileges.

#### [35.1.4. Roles in IdM](#roles-in-idm) {#roles-in-idm .title}

IdM roles group privileges together to define what actions specific users or groups can perform in your domain.

In effect, permissions grant the ability to perform given low-level tasks (such as creating a user entry and adding an entry to a group), privileges combine one or more of these permissions needed for a higher-level task (such as creating a new user in a given group). Roles gather privileges together as needed: for example, a User Administrator role would be able to add, modify, and delete users.

Important

Roles are used to classify permitted actions. They are not used as a tool to implement privilege separation or to protect from privilege escalation.

Note

Roles cannot contain other roles.

#### [35.1.5. Predefined roles in Identity Management](#predefined-roles-in-identity-management) {#predefined-roles-in-identity-management .title}

Review the default RBAC roles available in Red Hat Enterprise Linux Identity Management (IdM) to understand which privileges are assigned for common administrative tasks.

IdM provides the following range of pre-defined roles:

+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Role                     | Privilege                                                                                                    | Description                                                                                                    |
+:=========================+:=============================================================================================================+:===============================================================================================================+
| Enrollment Administrator | Host Enrollment                                                                                              | Responsible for client, or host, enrollment                                                                    |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| helpdesk                 | Modify Users and Reset passwords, Modify Group membership                                                    | Responsible for performing simple user administration tasks                                                    |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| IT Security Specialist   | Netgroups Administrators, HBAC Administrator, Sudo Administrator                                             | Responsible for managing security policy such as host-based access controls, sudo rules                        |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| IT Specialist            | Host Administrators, Host Group Administrators, Service Administrators, Automount Administrators             | Responsible for managing hosts                                                                                 |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Security Architect       | Delegation Administrator, Replication Administrators, Write IPA Configuration, Password Policy Administrator | Responsible for managing the Identity Management environment, creating trusts, creating replication agreements |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| User Administrator       | User Administrators, Group Administrators, Stage User Administrators                                         | Responsible for creating users and groups                                                                      |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

: Table 35.1. Predefined Roles in Identity Management

Show more

### [35.2. Managing IdM permissions in the CLI](#managing-idm-permissions-in-the-cli) {#managing-idm-permissions-in-the-cli .title}

Create and configure permissions using the Identity Management (IdM) CLI to define granular access control rules for LDAP operations. Permissions enable you to specify which users can perform specific actions on particular objects and attributes.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Create new permission entries with the `ipa permission-add`{.literal} command. For example, to add a permission named *dns admin*:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa permission-add "dns admin"
    ```

2.  Specify the properties of the permission with the following options:

    -   `--bindtype`{.literal} specifies the bind rule type. This option accepts the `all`{.literal}, `anonymous`{.literal}, and `permission`{.literal} arguments. The `permission`{.literal} bindtype means that only the users who are granted this permission through a role can exercise it.

        For example:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa permission-add "dns admin" --bindtype=all
        ```

        If you do not specify `--bindtype`{.literal}, then `permission`{.literal} is the default value.

        Note

        It is not possible to add permissions with a non-default bind rule type to privileges. You also cannot set a permission that is already present in a privilege to a non-default bind rule type.

    -   `--right`{.literal} lists the rights granted by the permission, it replaces the deprecated `--permissions`{.literal} option. The available values are `add`{.literal}, `delete`{.literal}, `read`{.literal}, `search`{.literal}, `compare`{.literal}, `write`{.literal}, `all`{.literal}.

        You can set multiple attributes by using multiple `--right`{.literal} options or with a comma-separated list inside curly braces. For example:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa permission-add "dns admin" --right=read --right=write
        $ ipa permission-add "dns admin" --right={read,write}
        ```

        Note

        `add`{.literal} and `delete`{.literal} are entry-level operations (for example, deleting a user, adding a group, and so on) while `read`{.literal}, `search`{.literal}, `compare`{.literal} and `write`{.literal} are more attribute-level: you can write to `userCertificate`{.literal} but not read `userPassword`{.literal}.

    -   `--attrs`{.literal} gives the list of attributes over which the permission is granted.

        You can set multiple attributes by using multiple `--attrs`{.literal} options or by listing the options in a comma-separated list inside curly braces. For example:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa permission-add "dns admin" --attrs=description --attrs=automountKey
        $ ipa permission-add "dns admin" --attrs={description,automountKey}
        ```

        The attributes provided with `--attrs`{.literal} must exist and be allowed attributes for the given object type, otherwise the command fails with schema syntax errors.

    -   `--type`{.literal} defines the entry object type to which the permission applies, such as user, host, or service. Each type has its own set of allowed attributes. For example:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa permission-add "manage service" --right=all --type=service --attrs=krbprincipalkey --attrs=krbprincipalname --attrs=managedby
        ```

    -   `--subtree`{.literal} gives a subtree entry; the filter then targets every entry beneath this subtree entry. Provide an existing subtree entry; `--subtree`{.literal} does not accept wildcards or non-existent domain names (DNs). Include a DN within the directory.

        Because IdM uses a simplified, flat directory tree structure, `--subtree`{.literal} can be used to target some types of entries, like automount locations, which are containers or parent entries for other configuration. For example:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa permission-add "manage automount locations" --subtree="ldap://ldap.example.com:389/cn=automount,dc=example,dc=com" --right=write --attrs=automountmapname --attrs=automountkey --attrs=automountInformation
        ```

        Note

        The `--type`{.literal} and `--subtree`{.literal} options are mutually exclusive: you can see the inclusion of filters for `--type`{.literal} as a simplification of `--subtree`{.literal}, intending to make life easier for an admin.

    -   `--filter`{.literal} uses an LDAP filter to identify which entries the permission applies to.

        IdM automatically checks the validity of the given filter. The filter can be any valid LDAP filter, for example:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa permission-add "manage Windows groups" --filter="(!(objectclass=posixgroup))" --right=write --attrs=description
        ```

    -   `--memberof`{.literal} sets the target filter to members of the given group after checking that the group exists. For example, to let the users with this permission modify the login shell of members of the engineers group:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa permission-add ManageShell --right="write" --type=user --attr=loginshell --memberof=engineers
        ```

        Note

        Setting the `memberof`{.literal} attribute permission is not applied if the target LDAP entry does not contain any reference to group membership.

    -   `--targetgroup`{.literal} sets target to the specified user group after checking that the group exists. For example, to let those with the permission write the member attribute in the engineers group (so they can add or remove members):

        ``` {.language-plaintext tabindex="-1"}
        $ ipa permission-add ManageMembers --right="write" --subtree=cn=groups,cn=accounts,dc=example,dc=test --attr=member --targetgroup=engineers
        ```

    -   Optionally, you can specify a target domain name (DN):

        -   `--target`{.literal} specifies the DN to apply the permission to. Wildcards are accepted.
        -   `--targetto`{.literal} specifies the DN subtree where an entry can be moved to.
        -   `--targetfrom`{.literal} specifies the DN subtree from where an entry can be moved.

### [35.3. Command options for existing permissions](#command-options-for-existing-permissions) {#command-options-for-existing-permissions .title}

Manage existing permissions in Identity Management (IdM) using command-line tools to modify access control policies dynamically.

Using these commands, you can view, edit, and delete permissions without recreating roles or privileges:

-   To edit existing permissions, use the `ipa permission-mod`{.literal} command. You can use the same command options as for adding permissions.

-   To find existing permissions, use the `ipa permission-find`{.literal} command. You can use the same command options as for adding permissions.

-   To view a specific permission, use the `ipa permission-show`{.literal} command.

    The `--raw`{.literal} argument shows the raw 389-ds ACI that is generated. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa permission-show <permission> --raw
    ```

-   The `ipa permission-del`{.literal} command deletes a permission completely.

### [35.4. Managing IdM privileges in the CLI](#managing-idm-privileges-in-the-cli) {#managing-idm-privileges-in-the-cli .title}

Create and configure privileges using the Identity Management (IdM) CLI to group related permissions for role-based access control. Privileges simplify access management by bundling multiple permissions into reusable components.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   Existing permissions. For details about permissions, see [Managing IdM permissions in the CLI](#managing-idm-permissions-in-the-cli "35.2. Managing IdM permissions in the CLI").

**Procedure**

1.  Add privilege entries using the `ipa privilege-add`{.literal} command

    For example, to add a privilege named *managing filesystems* with a description:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa privilege-add "managing filesystems" --desc="for filesystems"
    ```

2.  Assign the required permissions to the privilege group with the `privilege-add-permission`{.literal} command

    For example, to add the permissions named *managing automount* and *managing ftp services* to the *managing filesystems* privilege:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa privilege-add-permission "managing filesystems" --permissions="managing automount" --permissions="managing ftp services"
    ```

### [35.5. Command options for existing privileges](#command-options-for-existing-privileges) {#command-options-for-existing-privileges .title}

Manage existing privileges in Identity Management (IdM) using command-line tools to adjust permission bundles assigned to roles.

Using these commands, you can modify access control policies without recreating roles from scratch:

-   To modify existing privileges, use the `ipa privilege-mod`{.literal} command.
-   To find existing privileges, use the `ipa privilege-find`{.literal} command.
-   To view a specific privilege, use the `ipa privilege-show`{.literal} command.
-   The `ipa privilege-remove-permission`{.literal} command removes one or more permissions from a privilege.
-   The `ipa privilege-del`{.literal} command deletes a privilege completely.

### [35.6. Managing IdM roles in the CLI](#managing-idm-roles-in-the-cli) {#managing-idm-roles-in-the-cli .title}

Create and configure roles using the Identity Management (IdM) CLI to assign sets of privileges to users, groups, or hosts. Roles enable delegation of administrative tasks by granting specific capabilities without full administrator access.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   Existing privileges. For details about privileges, see [Managing IdM privileges in the CLI](#managing-idm-privileges-in-the-cli "35.4. Managing IdM privileges in the CLI").

**Procedure**

1.  Add new role entries using the `ipa role-add`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa role-add --desc="User Administrator" useradmin
    ------------------------
    Added role "useradmin"
    ------------------------
    Role name: useradmin
    Description: User Administrator
    ```

2.  Add the required privileges to the role using the `ipa role-add-privilege`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa role-add-privilege --privileges="user administrators" useradmin
    Role name: useradmin
    Description: User Administrator
    Privileges: user administrators
    ----------------------------
    Number of privileges added 1
    ----------------------------
    ```

3.  Add the required members to the role using the `ipa role-add-member`{.literal} command. Allowed member types are: users, groups, hosts and hostgroups. For example, to add the group named *useradmins* to the previously created *useradmin* role:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa role-add-member --groups=useradmins useradmin
    Role name: useradmin
    Description: User Administrator
    Member groups: useradmins
    Privileges: user administrators
    -------------------------
    Number of members added 1
    -------------------------
    ```

### [35.7. Command options for existing roles](#command-options-for-existing-roles) {#command-options-for-existing-roles .title}

Manage existing roles in Identity Management (IdM) using command-line tools to modify user access and administrative capabilities.

Using these commands, you can adjust role membership and privileges without recreating the entire role-based access control structure:

-   To modify existing roles, use the `ipa role-mod`{.literal} command.
-   To find existing roles, use the `ipa role-find`{.literal} command.
-   To view a specific role, use the `ipa role-show`{.literal} command.
-   To remove a member from the role, use the `ipa role-remove-member`{.literal} command.
-   The `ipa role-remove-privilege`{.literal} command removes one or more privileges from a role.
-   The `ipa role-del`{.literal} command deletes a role completely.

### [35.8. Additional resources](#managing-role-based-access-controls-in-idm-using-the-cli_358-additional-resources) {#additional-resources-15 .title}

-   [Using Ansible playbooks to manage role-based access control in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-ansible-playbooks-to-manage-role-based-access-control-in-idm)
-   [Using Ansible playbooks to manage RBAC privileges](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-ansible-playbooks-to-manage-rbac-privileges)
-   [Using Ansible playbooks to manage RBAC permissions in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-ansible-playbooks-to-manage-rbac-permissions-in-idm)

## [Chapter 36. Managing role-based access controls using the IdM Web UI](#managing-role-based-access-controls-using-the-idm-web-ui) {#chapter-36.-managing-role-based-access-controls-using-the-idm-web-ui .title}

Manage role-based access control (RBAC) in Identity Management (IdM) using the Web UI to restrict administrative access to authorized users. Define roles with specific permissions and assign them to users to enforce the principle of least privilege.

### [36.1. Managing permissions in the IdM Web UI](#managing-permissions-in-the-idm-web-ui) {#managing-permissions-in-the-idm-web-ui .title}

Create and configure permissions using the Identity Management (IdM) WebUI to define granular access control rules for LDAP operations. Permissions enable you to specify which users can perform specific actions on particular objects and attributes.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  To add a new permission, open the **IPA Server\>Role-Based Access Control** submenu and select **Permissions**:

2.  The list of permissions opens: Click the **Add** button at the top of the list of the permissions:

3.  The **Add Permission** form opens. Specify the name of the new permission and define its properties.

4.  Select the appropriate bind rule type:

    -   **permission** is the default permission type, granting access through privileges and roles

    -   **all** specifies that the permission applies to all authenticated users

    -   **anonymous** specifies that the permission applies to all users, including unauthenticated users

        Note

        It is not possible to add permissions with a non-default bind rule type to privileges. You also cannot set a permission that is already present in a privilege to a non-default bind rule type.

5.  Choose the rights to grant with this permission in **Granted rights**.

6.  Define the method to identify the target entries for the permission:

    -   **Type** specifies an entry type, such as user, host, or service. If you choose a value for the **Type** setting, a list of all possible attributes which will be accessible through this ACI for that entry type appears under **Effective Attributes**. Defining **Type** sets **Subtree** and **Target DN** to one of the predefined values.

    -   **Subtree** (required) specifies a subtree entry; every entry beneath this subtree entry is then targeted. Provide an existing subtree entry, as **Subtree** does not accept wildcards or non-existent domain names (DNs). For example: `cn=automount,dc=example,dc=com`{.literal}

    -   **Extra target filter** uses an LDAP filter to identify which entries the permission applies to. The filter can be any valid LDAP filter, for example: `(!(objectclass=posixgroup))`{.literal}

        IdM automatically checks the validity of the given filter. If you enter an invalid filter, IdM warns you about this when you attempt to save the permission.

    -   **Target DN** specifies the domain name (DN) and accepts wildcards. For example: `uid=*,cn=users,cn=accounts,dc=com`{.literal}

    -   **Member of group** sets the target filter to members of the given group. After you specify the filter settings and click **Add**, IdM validates the filter. If all the permission settings are correct, IdM will perform the search. If some of the permissions settings are incorrect, IdM will display a message informing you about which setting is set incorrectly.

        Note

        Setting the `memberof`{.literal} attribute permission is not applied if the target LDAP entry does not contain any reference to group membership.

7.  Add attributes to the permission:

    -   If you set **Type**, choose the **Effective attributes** from the list of available ACI attributes.

    -   If you did not use **Type**, add the attributes manually by writing them into the **Effective attributes** field. Add a single attribute at a time; to add multiple attributes, click **Add** to add another input field.

        Important

        If you do not set any attributes for the permission, then the permissions includes all attributes by default.

8.  Finish adding the permissions with the **Add** buttons at the bottom of the form:

    -   Click the **Add** button to save the permission and go back to the list of permissions.
    -   To save the permission and continue adding additional permissions in the same form, click the **Add and Add another** button.
    -   The **Add and Edit** button enables you to save and continue editing the newly created permission.

9.  Optional: You can also edit the properties of an existing permission by clicking its name from the list of permissions to display the **Permission settings** page.

10. Optional: If you need to remove an existing permission, select the checkbox next to its name in the list and click the **Delete** button to display The **Remove permissions** dialog. Click **Delete**.

    Note

    Operations on default managed permissions are restricted: the attributes you cannot modify are disabled in the IdM Web UI and you cannot delete the managed permissions completely.

    However, you can effectively disable a managed permission that has a bind type set to permission, by removing the managed permission from all privileges.

    For example, the following shows how to configure the permission `write`{.literal} on the `member`{.literal} attribute in the `engineers`{.literal} group (so they can add or remove members):

### [36.2. Managing privileges in the IdM WebUI](#managing-privileges-in-the-idm-webui) {#managing-privileges-in-the-idm-webui .title}

Create and configure privileges using the Identity Management (IdM) WebUI to group related permissions for role-based access control. Privileges simplify access management by bundling multiple permissions into reusable components.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  To add a new privilege, open the **IPA Server\>Role-Based Access Control** submenu and select **Privileges**:
2.  The list of privileges opens. Click the **Add** button at the top of the list of privileges.
3.  The **Add Privilege** form opens. Enter the name and a description of the privilege.
4.  Click the **Add and Edit** button to save the new privilege and continue to the privilege configuration page to add permissions.
5.  Click the **Permissions** tab to display a list of permissions included in the selected privilege. Click the **Add** button at the top of the list to add permissions to the privilege:
6.  Select the checkbox next to the name of each permission to add, and use the **\>** button to move the permissions to the **Prospective** column.
7.  Confirm by clicking the **Add** button.
8.  Optional: If you need to remove permissions, select the checkbox next to the relevant permissions and click the **Delete** button to display the **Remove privileges from permissions** dialog. Click **Delete**.
9.  Optional: If you need to delete an existing privilege, select the checkbox next to its name in the list and click the **Delete** button to open the **Remove privileges** dialog. Click **Delete**.

### [36.3. Managing roles in the IdM Web UI](#managing-roles-in-the-idm-web-ui) {#managing-roles-in-the-idm-web-ui .title}

Create and configure roles using the Identity Management (IdM) WebUI to assign sets of privileges to users, groups, or hosts. Roles enable delegation of administrative tasks by granting specific capabilities without full administrator access.

**Prerequisites**

-   Administrator privileges for managing IdM or the **User Administrator** role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  To add a new role, open the **IPA Server\>Role-Based Access Control** submenu and select **Roles**:
2.  The list of roles opens. Click the **Add** button at the top of the list of roles.
3.  The **Add Role** form opens. Enter the role name and a description:
4.  Click the **Add and Edit** button to save the new role and continue to the role configuration page to add privileges and users.
5.  Add members using the **Users**, **Users Groups**, **Hosts**, **Host Groups** or **Services** tabs, by clicking the **Add** button on top of the relevant list(s).
6.  In the window that opens, select the members on the left and use the **\>** button to move them to the **Prospective** column.
7.  Select the **Privileges** tab and click **Add**.
8.  Select the privileges on the left and use the **\>** button to move them to the **Prospective** column.
9.  Click the **Add** button to save.
10. Optional: If you need to remove privileges or members from a role, select the checkbox next to the name of the entity you want to remove and click the **Delete** button. A dialog opens. Click **Delete**.
11. Optional: If you need to remove an existing role, select the checkbox next to its name in the list and click the **Delete** button to display the **Remove roles** dialog. Click **Delete**.

### [36.4. Additional resources](#managing-role-based-access-controls-using-the-idm-web-ui_364-additional-resources) {#additional-resources-16 .title}

-   [Role based access control in IdM](#role-based-access-control-in-idm "35.1. Role-based access control in IdM")

## [Chapter 37. Using an ID view to override a user attribute value on an IdM client](#using-an-id-view-to-override-a-user-attribute-value-on-an-idm-client) {#chapter-37.-using-an-id-view-to-override-a-user-attribute-value-on-an-idm-client .title}

Use ID views to override user attribute values such as login names, home directories, and SSH keys on specific Identity Management (IdM) clients. ID views let administrators customize user attributes per host without changing the centrally stored LDAP data.

For example, you can specify a different home directory for a user on the IdM client that the user most commonly uses, such as `/home/encrypted/username`{.literal} on one client and `/dropbox/username`{.literal} on another, without modifying the user's LDAP entry.

### [37.1. ID views](#id-views) {#id-views .title}

Customize POSIX attributes for users and groups on specific Identity Management (IdM) clients using ID views to support different environment requirements. ID views enable you to override values like UIDs, home directories, and login names without modifying centrally defined user data.

An ID view in Identity Management (IdM) is an IdM client-side view specifying the following information:

-   New values for centrally defined POSIX user or group attributes
-   The client host or hosts on which the new values apply.

An ID view contains one or more overrides. An override is a specific replacement of a centrally defined POSIX attribute value.

You can only define an ID view for an IdM client centrally on IdM servers. You cannot configure client-side overrides for an IdM client locally.

For example, you can use ID views to achieve the following goals:

-   Define different attribute values for different environments. For example, you can allow the IdM administrator or another IdM user to have different home directories on different IdM clients: you can configure `/home/encrypted/username`{.literal} to be this user's home directory on one IdM client and `/dropbox/username`{.literal} on another client. Using ID views in this situation is convenient as alternatively, for example, changing `fallback_homedir`{.literal}, `override_homedir`{.literal} or other home directory variables in the client's `/etc/sssd/sssd.conf`{.literal} file would affect all users.
-   Replace a previously generated attribute value with a different value, such as overriding a user's UID. This ability can be useful when you want to achieve a system-wide change that would otherwise be difficult to do on the LDAP side, for example make 1009 the UID of an IdM user. IdM ID ranges, which are used to generate an IdM user UID, never start as low as 1000 or even 10000. If a reason exists for an IdM user to impersonate a local user with UID 1009 on all IdM clients, you can use ID views to override the UID of this IdM user that was generated when the user was created in IdM.

Important

You can only apply ID views to IdM clients, not to IdM servers.

**Additional resources**

-   [Adding an ID view to override an IdM user home directory on an IdM client](#adding-an-id-view-to-override-an-idm-user-home-directory-on-an-idm-client "37.7. Adding an ID view to override an IdM user home directory on an IdM client")
-   [Using ID views for Active Directory users](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/using-id-views-for-active-directory-users)
-   [SSSD Client-side View](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/sssd-client-side-view)

### [37.2. Potential negative impact of ID views on SSSD performance](#potential-negative-impact-of-id-views-on-sssd-performance) {#potential-negative-impact-of-id-views-on-sssd-performance .title}

ID views can negatively affect the performance of System Security Services Daemon (SSSD) by preventing specific optimizations during group lookups. This performance impact is most apparent when the SSSD cache is empty or recently cleared.

When you define an ID view, IdM places the desired override value in the IdM server's SSSD cache. The SSSD running on an IdM client then retrieves the override value from the server cache.

Applying an ID view can have a negative impact on SSSD performance, because certain optimizations and ID views cannot run at the same time. For example, ID views prevent SSSD from optimizing the process of looking up groups on the server:

-   With ID views, SSSD must check every member on the returned list of group member names if the group name is overridden.
-   Without ID views, SSSD can only collect the user names from the member attribute of the group object.

This negative effect becomes most apparent when the SSSD cache is empty or after you clear the cache, which makes all entries invalid.

### [37.3. Attributes an ID view can override](#attributes-an-id-view-can-override) {#attributes-an-id-view-can-override .title}

ID views in Identity Management (IdM) can override POSIX user and group attributes to customize account properties on specific hosts. This enables per-host customization of login names, UIDs, GIDs, home directories, and other attributes without changing global user definitions.

User and group ID overrides can define new values for the following POSIX attributes:

User attributes

:   -   Login name (`uid`{.literal})
    -   GECOS entry (`gecos`{.literal})
    -   UID number (`uidNumber`{.literal})
    -   GID number (`gidNumber`{.literal})
    -   Login shell (`loginShell`{.literal})
    -   Home directory (`homeDirectory`{.literal})
    -   SSH public keys (`ipaSshPubkey`{.literal})
    -   Certificate (`userCertificate`{.literal})

Group attributes

:   -   Group name (`cn`{.literal})
    -   Group GID number (`gidNumber`{.literal})

### [37.4. Getting help for ID view commands](#getting-help-for-id-view-commands) {#getting-help-for-id-view-commands .title}

Access built-in help documentation for ID view management commands in the Identity Management (IdM) CLI to understand command syntax and available options. This helps you efficiently manage ID views and overrides.

**Prerequisites**

-   You have obtained a Kerberos ticket for an IdM user.

**Procedure**

-   To display all commands used to manage ID views and overrides:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa help idviews
    ID Views

    Manage ID Views

    IPA allows to override certain properties of users and groups[...]
    [...]
    Topic commands:
      idoverridegroup-add          Add a new Group ID override
      idoverridegroup-del          Delete a Group ID override
    [...]
    ```

-   To display detailed help for a particular command, add the `--help`{.literal} option to the command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idview-add --help
    Usage: ipa [global-options] idview-add NAME [options]

    Add a new ID View.
    Options:
      -h, --help      show this help message and exit
      --desc=STR      Description
    [...]
    ```

### [37.5. Using an ID view to override the login name of an IdM user on a specific host](#using-an-id-view-to-override-the-login-name-of-an-idm-user-on-a-specific-host) {#using-an-id-view-to-override-the-login-name-of-an-idm-user-on-a-specific-host .title}

Create an ID view in Identity Management (IdM) to override a user's POSIX attributes, such as their login name, on a specific host without changing the user's global IdM account.

Create an ID view to map the IdM user `idm_user`{.literal} to the alias `user_1234`{.literal} for logins on `client1`{.literal}. This configuration overrides the default username on the specified host, allowing the user to authenticate with localized credentials.

**Prerequisites**

-   You are logged in as IdM administrator.

**Procedure**

1.  On the IdM server, create a new ID view. For example, to create an ID view named `example_for_client1`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idview-add example_for_client1
    ---------------------------
    Added ID View "example_for_client1"
    ---------------------------
      ID View Name: example_for_client1
    ```

2.  Add a user override to the **example_for_client1** ID view. To override the user login:

    -   Enter the `ipa idoverrideuser-add`{.literal} command

    -   Add the name of the ID view

    -   Add the user name, also called the anchor

    -   Add the `--login`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa idoverrideuser-add example_for_client1 idm_user --login=user_1234
        -----------------------------
        Added User ID override "idm_user"
        -----------------------------
          Anchor to override: idm_user
          User login: user_1234
        ```

        For a list of the available options, run `ipa idoverrideuser-add --help`{.literal}.

        Note

        The `ipa idoverrideuser-add --certificate`{.literal} command replaces all existing certificates for the account in the specified ID view. To append an additional certificate, use the `ipa idoverrideuser-add-cert`{.literal} command instead:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa idoverrideuser-add-cert example_for_client1 user --certificate="MIIEATCC..."
        ```

3.  Optional: Using the `ipa idoverrideuser-mod`{.literal} command, you can specify new attribute values for an existing user override.

4.  Apply `example_for_client1`{.literal} to the `client1.idm.example.com`{.literal} host:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idview-apply example_for_client1 --hosts=client1.idm.example.com
    -----------------------------
    Applied ID View "example_for_client1"
    -----------------------------
    hosts: client1.idm.example.com
    ---------------------------------------------
    Number of hosts the ID View was applied to: 1
    ---------------------------------------------
    ```

    Note

    The `ipa idview-apply`{.literal} command also accepts the `--hostgroups`{.literal} option. The option applies the ID view to hosts that belong to the specified host group, but does not associate the ID view with the host group itself. Instead, the `--hostgroups`{.literal} option expands the members of the specified host group and applies the `--hosts`{.literal} option individually to every one of them.

    This means that if a host is added to the host group in the future, the ID view does not apply to the new host.

5.  To apply the new configuration to the IdM client system immediately:

    a.  SSH to the client system as root:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh root@client1
        Password:
        ```

    b.  On the IdM client, clear the SSSD cache:

        ``` {.language-plaintext tabindex="-1"}
        # sss_cache -E
        ```

    c.  On the IdM client, restart the SSSD daemon:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

-   If you have the credentials of **user_1234**, you can use them to log in to the IdM client:

    1.  SSH to the client system using **user_1234** as the login name:

        ``` {.language-plaintext tabindex="-1"}
        # ssh user_1234@client1.idm.example.com
        Password:

        Last login: Sun Jun 21 22:34:25 2020 from 192.168.122.229
        $
        ```

    2.  On the client system, display the working directory:

        ``` {.language-plaintext tabindex="-1"}
        $ pwd
        /home/idm_user/
        ```

-   Alternatively, if you have root credentials on the IdM client, you can use them to check the output of the `id`{.literal} command for **idm_user** and **user_1234**:

    ``` {.language-plaintext tabindex="-1"}
    # id idm_user
    uid=779800003(user_1234) gid=779800003(idm_user) groups=779800003(idm_user)
    # user_1234
    uid=779800003(user_1234) gid=779800003(idm_user) groups=779800003(idm_user)
    ```

### [37.6. Modifying an IdM ID view](#modifying-an-idm-id-view) {#modifying-an-idm-id-view .title}

Update ID view overrides to change POSIX attribute values like home directories or UIDs for specific users on Identity Management (IdM) clients. This way, you can adjust client-specific user configurations without changing centrally defined user data.

In this example, you modify an ID view to enable the user named **idm_user** to use the `/home/user_1234/`{.literal} directory as the user home directory instead of `/home/idm_user/`{.literal} on the **client1.idm.example.com** IdM client.

**Prerequisites**

-   You have root access to the IdM client system.
-   You are logged in as a user with the required privileges, for example **admin**.
-   You have an ID view configured for **idm_user** that applies to the IdM client.

**Procedure**

1.  On the IdM client, create the directory that you want **idm_user** to use on **client1.idm.example.com** as the user home directory:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /home/user_1234/
    ```

2.  On the IdM client, change the ownership of the directory:

    ``` {.language-plaintext tabindex="-1"}
    # chown idm_user:idm_user /home/user_1234/
    ```

3.  On the IdM server, display the ID view, including the hosts to which the ID view is currently applied. To display the ID view named `example_for_client1`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idview-show example_for_client1 --all
      dn: cn=example_for_client1,cn=views,cn=accounts,dc=idm,dc=example,dc=com
      ID View Name: example_for_client1
      User object override: idm_user
      Hosts the view applies to: client1.idm.example.com
      objectclass: ipaIDView, top, nsContainer
    ```

    The output shows that the ID view currently applies to **client1.idm.example.com**.

4.  On the IdM server, modify the user override of the **example_for_client1** ID view. To override the user home directory:

    -   Enter the `ipa idoverrideuser-add`{.literal} command

    -   Add the name of the ID view

    -   Add the user name, also called the anchor

    -   Add the `--homedir`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa idoverrideuser-mod example_for_client1 idm_user --homedir=/home/user_1234
        -----------------------------
        Modified a User ID override "idm_user"
        -----------------------------
          Anchor to override: idm_user
          User login: user_1234
          Home directory: /home/user_1234/
        ```

    For a list of the available options, run `ipa idoverrideuser-mod --help`{.literal}.

5.  To apply the new configuration to the **client1.idm.example.com** system immediately:

    a.  SSH to the IdM client system as root:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh root@client1
        Password:
        ```

    b.  On the IdM client, clear the SSSD cache:

        ``` {.language-plaintext tabindex="-1"}
        # sss_cache -E
        ```

    c.  On the IdM client, restart the SSSD daemon:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

1.  `SSH`{.literal} to the client system as **idm_user**:

    ``` {.language-plaintext tabindex="-1"}
    # ssh idm_user@client1.idm.example.com
    Password:

    Last login: Sun Jun 21 22:34:25 2020 from 192.168.122.229
    [user_1234@client1 ~]$
    ```

2.  On the client system, print the working directory:

    ``` {.language-plaintext tabindex="-1"}
    $ pwd
    /home/user_1234/
    ```

**Additional resources**

-   [Defining global attributes for an AD user by modifying the Default Trust View](#defining-global-attributes-for-an-ad-user-by-modifying-the-default-trust-view "38.2. Defining global attributes for an AD user by modifying the Default Trust View")

### [37.7. Adding an ID view to override an IdM user home directory on an IdM client](#adding-an-id-view-to-override-an-idm-user-home-directory-on-an-idm-client) {#adding-an-id-view-to-override-an-idm-user-home-directory-on-an-idm-client .title}

Create an ID view in Identity Management (IdM) to override POSIX attributes like home directories for specific users on specific clients. With this, you can customize user environments without changing global user settings.

For example, you can create an ID view to override the home directory of an IdM user on an IdM client.

**Prerequisites**

-   You have root access to the IdM client system.
-   You are logged in as a user with the required privileges, for example **admin**.

**Procedure**

1.  On the IdM client, create the directory that you want **idm_user** to use as the user home directory:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /home/user_1234/
    ```

2.  On the IdM client, change the ownership of the directory:

    ``` {.language-plaintext tabindex="-1"}
    # chown idm_user:idm_user /home/user_1234/
    ```

3.  On the IdM server, create an ID view. For example, to create an ID view named **example_for_client1**:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idview-add example_for_client1
    ---------------------------
    Added ID View "example_for_client1"
    ---------------------------
      ID View Name: example_for_client1
    ```

4.  On the IdM server, add a user override to the **example_for_client1** ID view. To override the user home directory:

    -   Enter the `ipa idoverrideuser-add`{.literal} command
    -   Add the name of the ID view
    -   Add the user name, also called the anchor
    -   Add the `--homedir`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idoverrideuser-add example_for_client1 idm_user --homedir=/home/user_1234
    -----------------------------
    Added User ID override "idm_user"
    -----------------------------
      Anchor to override: idm_user
      Home directory: /home/user_1234/
    ```

5.  On the IdM server, apply `example_for_client1`{.literal} to the `client1.idm.example.com`{.literal} host:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idview-apply example_for_client1 --hosts=client1.idm.example.com
    -----------------------------
    Applied ID View "example_for_client1"
    -----------------------------
    hosts: client1.idm.example.com
    ---------------------------------------------
    Number of hosts the ID View was applied to: 1
    ---------------------------------------------
    ```

    Note

    The `ipa idview-apply`{.literal} command also accepts the `--hostgroups`{.literal} option. The option applies the ID view to hosts that belong to the specified host group, but does not associate the ID view with the host group itself. Instead, the `--hostgroups`{.literal} option expands the members of the specified host group and applies the `--hosts`{.literal} option individually to every one of them.

    This means that if a host is added to the host group in the future, the ID view does not apply to the new host.

6.  To apply the new configuration to the IdM client system immediately:

    a.  SSH to the IdM client system as root:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh root@client1
        Password:
        ```

    b.  On the IdM client, clear the SSSD cache:

        ``` {.language-plaintext tabindex="-1"}
        # sss_cache -E
        ```

    c.  On the IdM client, restart the SSSD daemon:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

1.  `SSH`{.literal} to the IdM client system as **idm_user**:

    ``` {.language-plaintext tabindex="-1"}
    # ssh idm_user@client1.idm.example.com
    Password:
    Activate the web console with: systemctl enable --now cockpit.socket

    Last login: Sun Jun 21 22:34:25 2020 from 192.168.122.229
    [idm_user@client1 /]$
    ```

2.  Print the working directory:

    ``` {.language-plaintext tabindex="-1"}
    $ pwd
    /home/user_1234/
    ```

**Additional resources**

-   [Overriding Default Trust View attributes for an AD user on an IdM client with an ID view](#overriding-default-trust-view-attributes-for-an-ad-user-on-an-idm-client-with-an-id-view "38.3. Overriding Default Trust View attributes for an AD user on an IdM client with an ID view")

### [37.8. Applying an ID view to an IdM host group](#applying-an-id-view-to-an-idm-host-group) {#applying-an-id-view-to-an-idm-host-group .title}

Apply an ID view to all hosts in a host group in Identity Management (IdM) to override POSIX attributes for multiple systems simultaneously. This enables consistent user attribute customization across groups of hosts without modifying global user settings.

The `ipa idview-apply`{.literal} command accepts the `--hostgroups`{.literal} option. However, the option acts as a one-time operation that applies the ID view to hosts that currently belong to the specified host group, but does not dynamically associate the ID view with the host group itself. The `--hostgroups`{.literal} option expands the members of the specified host group and applies the `--hosts`{.literal} option individually to every one of them.

If you add a new host to the host group later, you must apply the ID view to the new host manually, using the `ipa idview-apply`{.literal} command with the `--hosts`{.literal} option.

Similarly, if you remove a host from a host group, the ID view is still assigned to the host after the removal. To unapply the ID view from the removed host, you must run the `ipa idview-unapply `{.literal}*`id_view_name`{.literal}*` --hosts=`{.literal}*`name_of_the_removed_host`{.literal}* command. .Prerequisites

-   Ensure that the ID view you want to apply to the host group exists in IdM. For example, to create an ID view to override the GID for an AD user, see [Overriding Default Trust View attributes for an AD user on an IdM client with an ID view](#overriding-default-trust-view-attributes-for-an-ad-user-on-an-idm-client-with-an-id-view "38.3. Overriding Default Trust View attributes for an AD user on an IdM client with an ID view")

**Procedure**

1.  Create a host group and add hosts to it:

    a.  Create a host group. For example, to create a host group named **baltimore**:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa hostgroup-add --desc="Baltimore hosts" baltimore
        ---------------------------
        Added hostgroup "baltimore"
        ---------------------------
        Host-group: baltimore
        Description: Baltimore hosts
        ```

    b.  Add hosts to the host group. For example, to add the **host102** and **host103** to the **baltimore** host group:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa hostgroup-add-member --hosts={host102,host103} baltimore
        Host-group: baltimore
        Description: Baltimore hosts
        Member hosts: host102.idm.example.com, host103.idm.example.com
        -------------------------
        Number of members added 2
        -------------------------
        ```

2.  Apply an ID view to the hosts in the host group. For example, to apply the **example_for_host1** ID view to the **baltimore** host group:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idview-apply --hostgroups=baltimore
    ID View Name: example_for_host1
    -----------------------------------------
    Applied ID View "example_for_host1"
    -----------------------------------------
      hosts: host102.idm.example.com, host103.idm.example.com
    ---------------------------------------------
    Number of hosts the ID View was applied to: 2
    ---------------------------------------------
    ```

3.  Add a new host to the host group and apply the ID view to the new host:

    a.  Add a new host to the host group. For example, to add the **somehost.idm.example.com** host to the **baltimore** host group:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa hostgroup-add-member --hosts=somehost.idm.example.com baltimore
          Host-group: baltimore
          Description: Baltimore hosts
          Member hosts:  host102.idm.example.com, host103.idm.example.com,somehost.idm.example.com
        -------------------------
        Number of members added 1
        -------------------------
        ```

    b.  Optional: Display the ID view information. For example, to display the details about the **example_for_host1** ID view:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa idview-show example_for_host1 --all
          dn: cn=example_for_host1,cn=views,cn=accounts,dc=idm,dc=example,dc=com
          ID View Name: example_for_host1
        [...]
          Hosts the view applies to: host102.idm.example.com, host103.idm.example.com
          objectclass: ipaIDView, top, nsContainer
        ```

        The output shows that the ID view is not applied to **somehost.idm.example.com**, the newly-added host in the **baltimore** host group.

    c.  Apply the ID view to the new host. For example, to apply the **example_for_host1** ID view to **somehost.idm.example.com**:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa idview-apply --host=somehost.idm.example.com
        ID View Name: example_for_host1
        -----------------------------------------
        Applied ID View "example_for_host1"
        -----------------------------------------
          hosts: somehost.idm.example.com
        ---------------------------------------------
        Number of hosts the ID View was applied to: 1
        ---------------------------------------------
        ```

**Verification**

-   Display the ID view information again:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idview-show example_for_host1 --all
      dn: cn=example_for_host1,cn=views,cn=accounts,dc=idm,dc=example,dc=com
      ID View Name: example_for_host1
    [...]
      Hosts the view applies to: host102.idm.example.com, host103.idm.example.com, somehost.idm.example.com
      objectclass: ipaIDView, top, nsContainer
    ```

    The output shows that ID view is now applied to **somehost.idm.example.com**, the newly-added host in the **baltimore** host group.

### [37.9. Migrating NIS domains to Identity Management](#migrating-nis-domains-to-identity-management) {#migrating-nis-domains-to-identity-management .title}

Migrate your NIS domain users and groups to Identity Management (IdM), using ID views to preserve existing host-specific UIDs and GIDs so that file and directory permissions remain intact after migration.

**Prerequisites**

-   You authenticated yourself as an admin using the `kinit admin`{.literal} command.

**Procedure**

1.  Add users and groups in the IdM domain.

    a.  Create users using the `ipa user-add`{.literal} command. For more information, see [Adding users to IdM](#adding-users-using-the-command-line "1.2. Adding users using the command line").
    b.  Create groups using the `ipa group-add`{.literal} command. For more information see: [Adding groups to IdM](#adding-a-user-group-using-idm-cli "26.3. Adding a user group using IdM CLI").

2.  Override IDs IdM generated during the user creation:

    a.  Create a new ID view using `ipa idview-add`{.literal} command. For more information see: [Getting help for ID view commands](#getting-help-for-id-view-commands "37.4. Getting help for ID view commands").
    b.  Add ID overrides for the users and groups to the ID view using `ipa idoverrideuser-add`{.literal} and `idoverridegroup-add`{.literal} respectively.

3.  Assign the ID view to the specific hosts using `ipa idview-apply`{.literal} command.

4.  Decommission the NIS domains.

**Verification**

1.  To check if all users and groups were added to the ID view correctly, use the `ipa idview-show`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idview-show example-view
      ID View Name: example-view
      User object overrides: example-user1
      Group object overrides: example-group
    ```

### [37.10. Using Ansible to override the login name and home directory of an IdM user on a specific host](#using-ansible-to-override-the-login-name-and-home-directory-of-an-idm-user-on-a-specific-host) {#using-ansible-to-override-the-login-name-and-home-directory-of-an-idm-user-on-a-specific-host .title}

Use the `ansible-freeipa`{.literal} `idoverrideuser`{.literal} module to override an Identity Management (IdM) user's POSIX attributes, such as their login name and home directory, on a specific host for custom host-specific configurations.

The procedure uses the example of an ID view that enables an IdM user named **idm_user** to log in to an IdM client named **client1.idm.example.com** by using the **user_1234** login name. Additionally, the ID view modifies the home directory of idm_user so that after logging in to client1, the user home directory is **/home/user_1234/**.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create your Ansible playbook file **add-idoverrideuser-with-name-and-homedir.yml** with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to manage idoverrideuser
      hosts: ipaserver
      become: false
      gather_facts: false
      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml

      tasks:
      - name: Ensure idview_for_client1 is present
        idview:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: idview_for_client1
      - name: Ensure idview_for_client1 is applied to client1.idm.example.com
        idview:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: idview_for_client1
          host: client1.idm.example.com
          action: member
      - name: Ensure idm_user is present in idview_for_client1 with homedir /home/user_1234 and name user_1234
        ipaidoverrideuser:
          ipaadmin_password: "{{ ipaadmin_password }}"
          idview: idview_for_client1
          anchor: idm_user
          name: user_1234
          homedir: /home/user_1234
    ```

2.  Run the playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file::

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i <path_to_inventory_directory>/inventory <path_to_playbooks_directory>/add-idoverrideuser-with-name-and-homedir.yml
    ```

3.  Optional: If you have `root`{.literal} credentials, you can apply the new configuration to the IdM client system immediately:

    a.  SSH to the client system as `root`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh root@client1
        Password:
        ```

    b.  On the IdM client, clear the SSSD cache:

        ``` {.language-plaintext tabindex="-1"}
        # sss_cache -E
        ```

    c.  On the IdM client, restart the SSSD daemon:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart sssd
        ```

**Verification**

1.  `SSH`{.literal} to IdM client as **idm_user**:

    ``` {.language-plaintext tabindex="-1"}
    # ssh idm_user@client1.idm.example.com
    Password:

    Last login: Sun Jun 21 22:34:25 2020 from 192.168.122.229
    [user_1234@client1 ~]$
    ```

2.  Print the working directory:

    ``` {.language-plaintext tabindex="-1"}
    $ pwd
    /home/user_1234/
    ```

**Additional resources**

-   [idoverrideuser](https://github.com/freeipa/ansible-freeipa/blob/master/README-idoverrideuser.md)

### [37.11. Using Ansible to configure an ID view that enables an SSH key login on an IdM client](#using-ansible-to-configure-an-id-view-that-enables-an-ssh-key-login-on-an-idm-client) {#using-ansible-to-configure-an-id-view-that-enables-an-ssh-key-login-on-an-idm-client .title}

Use the `idoverrideuser`{.literal} Ansible module to assign an SSH key to an Identity Management (IdM) user for key-based login on a specific IdM client.

The procedure uses the example of an ID view that enables an IdM user named **idm_user** to log in to an IdM client named **client1.idm.example.com** with an SSH key.

Note

This ID view can be used to enhance a specific HBAC rule.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.\'s SSH public key.

-   The **idview_for_client1** ID view exists.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create your Ansible playbook file **ensure-idoverrideuser-can-login-with-sshkey.yml** with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to manage idoverrideuser
      hosts: ipaserver
      become: false
      gather_facts: false
      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml

      tasks:
      - name: Ensure test user idm_user is present in idview idview_for_client1 with sshpubkey
        ipaidoverrideuser:
          ipaadmin_password: "{{ ipaadmin_password }}"
          idview: idview_for_client1
          anchor: idm_user
          sshpubkey:
          - ssh-rsa AAAAB3NzaC1yc2EAAADAQABAAABgQCqmVDpEX5gnSjKuv97Ay ...
      - name: Ensure idview_for_client1 is applied to client1.idm.example.com
        ipaidview:
          ipaadmin_password:  "{{ ipaadmin_password }}"
          name: idview_for_client1
          host: client1.idm.example.com
          action: member
    ```

2.  Run the playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i <path_to_inventory_directory>/inventory <path_to_playbooks_directory>/ensure-idoverrideuser-can-login-with-sshkey.yml
    ```

3.  Optional: If you have `root`{.literal} credentials, you can apply the new configuration to the IdM client system immediately:

    a.  SSH to the client system as `root`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh root@client1
        Password:
        ```

    b.  On the IdM client, clear the SSSD cache:

        ``` {.language-plaintext tabindex="-1"}
        # sss_cache -E
        ```

    c.  On the IdM client, restart the SSSD daemon:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart sssd
        ```

**Verification**

-   Use the public key to `SSH`{.literal} to the client system:

    ``` {.language-plaintext tabindex="-1"}
    # ssh -i ~/.ssh/id_rsa.pub idm_user@client1.idm.example.com

    Last login: Sun Jun 21 22:34:25 2023 from 192.168.122.229
    [idm_user@client1 ~]$
    ```

The output confirms that you have logged in successfully.

**Additional resources**

-   [idoverrideuser](https://github.com/freeipa/ansible-freeipa/blob/master/README-idoverrideuser.md)

### [37.12. Using Ansible to give a user ID override access to the local sound card on an IdM client](#using-ansible-to-give-a-user-id-override-access-to-the-local-sound-card-on-an-idm-client) {#using-ansible-to-give-a-user-id-override-access-to-the-local-sound-card-on-an-idm-client .title}

Use the `ansible-freeipa`{.literal} `group`{.literal} and `idoverrideuser`{.literal} modules to grant Identity Management (IdM) or AD users access to the sound card on an IdM client by adding them to the local `audio`{.literal} group.

The procedure uses the example of the `Default Trust View`{.literal} ID view to which the **aduser@addomain.com** ID override is added in the first playbook task. In the next playbook task, an **audio** group is created in IdM with the GID of 63, which corresponds to the GID of local `audio`{.literal} groups on RHEL hosts. At the same time, the [aduser@addomain.com](mailto:aduser@addomain.com) ID override is added to the IdM audio group as a member.

**Prerequisites**

-   You have `root`{.literal} access to the IdM client on which you want to perform the first part of the procedure. In the example, this is **client.idm.example.com**.

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  On **client.idm.example.com**, add `[SUCCESS=merge]`{.literal} to the `/etc/nsswitch.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [...]
    # Allow initgroups to default to the setting for group.
    initgroups: sss [SUCCESS=merge] files
    ```

2.  Identify the GID of the local `audio`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    $ getent group audio
    ---------------------
    audio:x:63
    ```

3.  On your Ansible control node, create an **add-aduser-to-audio-group.yml** playbook with a task to add the **aduser@addomain.com** user override to the Default Trust View:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to manage idoverrideuser
      hosts: ipaserver
      become: false

      tasks:
      - name: Add aduser@addomain.com user to the Default Trust View
        ipaidoverrideuser:
          ipaadmin_password: "{{ ipaadmin_password }}"
          idview: "Default Trust View"
          anchor: aduser@addomain.com
    ```

4.  Use another playbook task in the same playbook to add the group **audio** to IdM with the `GID`{.literal} of 63. Add the aduser idoverrideuser to the group:

    ``` {.language-plaintext tabindex="-1"}
      - name: Add the audio group with the aduser member and GID of 63
        ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: audio
          idoverrideuser:
          - aduser@addomain.com
          gidnumber: 63
    ```

5.  Save the file.

6.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory add-aduser-to-audio-group.yml
    ```

**Verification**

1.  Log in to the IdM client as the AD user:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh aduser@addomain.com@client.idm.example.com
    ```

2.  Verify the group membership of the AD user:

    ``` {.language-plaintext tabindex="-1"}
    $ id aduser@addomain.com
    uid=702801456(aduser@addomain.com) gid=63(audio) groups=63(audio)
    ```

**Additional resources**

-   [idoverrideuser](https://github.com/freeipa/ansible-freeipa/blob/master/README-idoverrideuser.md)
-   [ipagroup](https://github.com/freeipa/ansible-freeipa/blob/master/README-group.md)
-   [Enabling group merging for local and remote groups in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-user-groups-in-idm-cli#enabling-group-merging-for-local-and-remote-groups-in-idm)

### [37.13. Using Ansible to ensure an IdM user is present in an ID view with a specific UID](#using-ansible-to-ensure-an-idm-user-is-present-in-an-id-view-with-a-specific-uid) {#using-ansible-to-ensure-an-idm-user-is-present-in-an-id-view-with-a-specific-uid .title}

Use the `idoverrideuser`{.literal} Ansible module to assign a specific UID to an Identity Management (IdM) user in an ID view so that both IdM and local users can share the same files.

If you are working in a lab where you have your own computer but your `/home/`{.literal} directory is in a shared drive exported by a server, you can have two users:

-   One that is system-wide user, stored centrally in Identity Management (IdM).
-   One whose account is local, that is stored on the system in question.

Complete this procedure to use the `ansible-freeipa`{.literal} `idoverrideuser`{.literal} module to:

-   Apply an ID view to host01 named **idview_for_host01**.
-   Ensure, in idview_for_host01, the presence of a user ID override for idm_user with the `UID`{.literal} of **20001**.

**Prerequisites**

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create an Ansible playbook file named `ensure-idmuser-and-local-user-have-access-to-same-files.yml`{.literal} with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Ensure both local user and IdM user have access to same files
      hosts: ipaserver
      become: false
      gather_facts: false

      tasks:
      - name: Ensure idview_for_host1 is applied to host1.idm.example.com
        ipaidview:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: idview_for_host01
          host: host1.idm.example.com
      - name: Ensure idmuser is present in idview_for_host01 with the UID of 20001
        ipaidoverrideuser:
          ipaadmin_password: "{{ ipaadmin_password }}"
          idview: idview_for_host01
          anchor: idm_user
          UID: 20001
    ```

2.  Save the file.

3.  Run the playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory ensure-idmuser-and-local-user-have-access-to-same-files.yml
    ```

**Additional resources**

-   [idoverrideuser](https://github.com/freeipa/ansible-freeipa/blob/master/README-idoverrideuser.md)

### [37.14. Using Ansible to ensure an IdM user can log in to an IdM client with two certificates](#using-ansible-to-ensure-an-idm-user-can-log-in-to-an-idm-client-with-two-certificates) {#using-ansible-to-ensure-an-idm-user-can-log-in-to-an-idm-client-with-two-certificates .title}

Use the `idoverrideuser`{.literal} Ansible module to require smart card authentication for an Identity Management (IdM) user on a specific client.

Complete this procedure to use the `ansible-freeipa`{.literal} `idoverrideuser`{.literal} module to:

-   Apply an ID view to host01 named **idview_for_host01**.
-   Ensure, in idview_for_host01, the presence of a user ID override for **idm_user** with two certificates.

**Prerequisites**

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create your Ansible playbook file `ensure-idmuser-present-in-idview-with-certificates.yml`{.literal} with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Ensure both local user and IdM user have access to same files
      hosts: ipaserver
      become: false
      gather_facts: false

      tasks:
      - name: Ensure idview_for_host1 is applied to host01.idm.example.com
        ipaidview:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: idview_for_host01
          host: host01.idm.example.com

      - name: Ensure an IdM user is present in ID view with two certificates
        ipaidoverrideuser:
          ipaadmin_password: "{{ ipaadmin_password }}"
          idview: idview_for_host01
          anchor: idm_user
          certificate:
          - "{{ lookup('file', 'cert1.b64', rstrip=False) }}"
          - "{{ lookup('file', 'cert2.b64', rstrip=False) }}"
    ```

    The `rstrip=False`{.literal} directive causes the white space not to be removed from the end of the looked-up file.

2.  Save the file.

3.  Run the playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory ensure-idmuser-present-in-idview-with-certificates.yml
    ```

**Additional resources**

-   [idoverrideuser](https://github.com/freeipa/ansible-freeipa/blob/master/README-idoverrideuser.md)

### [37.15. Using Ansible to give an IdM group access to the sound card on an IdM client](#using-ansible-to-give-an-idm-group-access-to-the-sound-card-on-an-idm-client) {#using-ansible-to-give-an-idm-group-access-to-the-sound-card-on-an-idm-client .title}

Use the `ansible-freeipa`{.literal} `idview`{.literal} and `idoverridegroup`{.literal} modules to grant Identity Management (IdM) or AD groups access to the sound card on an IdM client by mapping them to the local `audio`{.literal} group.

The procedure uses the example of the **idview_for_host01** ID view to which the **audio** group ID override is added with the `GID`{.literal} of **63**, which corresponds to the GID of local `audio`{.literal} groups on RHEL hosts. The **idview_for_host01** ID view is applied to an IdM client named **host01.idm.example.com**.

**Prerequisites**

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create an Ansible playbook file named `give-idm-group-access-to-sound-card-on-idm-client.yml`{.literal} with the following content:

    ``` {.language-plaintext tabindex="-1"}
    $ getent group audio
    ---------------------
    audio:x:63
    ```

2.  On your Ansible control node, create an **give-idm-group-access-to-sound-card-on-idm-client.yml** playbook with the following tasks:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to give IdM group access to sound card on IdM client
      hosts: ipaserver
      become: false

      tasks:
      - name: Ensure the audio group exists in IdM
        ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: audio

      - name: Ensure idview_for_host01 exists and is applied to host01.idm.example.com
        ipaidview:
          ipaadmin_password:  "{{ ipaadmin_password }}"
          name: idview_for_host01
          host: host01.idm.example.com

      - name: Add an override for the IdM audio group with GID 63 to idview_for_host01
        ipaidoverridegroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          idview: idview_for_host01
          anchor: audio
          GID: 63
    ```

3.  Save the file.

4.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory give-idm-group-access-to-sound-card-on-idm-client.yml
    ```

**Verification**

1.  On an IdM client, obtain IdM administrator's credentials:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit admin
    Password:
    ```

2.  Create a test IdM user:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-add testuser --first test --last user --password
    User login [tuser]:
    Password:
    Enter Password again to verify:
    ------------------
    Added user "tuser"
    ------------------
    ```

3.  Add the user to the IdM audio group:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-add-member --tuser audio
    ```

4.  Log in to host01.idm.example.com as tuser:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh tuser@host01.idm.example.com
    ```

5.  Verify the group membership of the user:

    ``` {.language-plaintext tabindex="-1"}
    $ id tuser
    uid=702801456(tuser) gid=63(audio) groups=63(audio)
    ```

**Additional resources**

-   [idoverridegroup](https://github.com/freeipa/ansible-freeipa/blob/master/README-idoverridegroup.md)
-   [idview](https://github.com/freeipa/ansible-freeipa/blob/master/README-idview.md)
-   [ipagroup](https://github.com/freeipa/ansible-freeipa/blob/master/README-group.md)
-   [Enabling group merging for local and remote groups in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-user-groups-in-idm-cli#enabling-group-merging-for-local-and-remote-groups-in-idm)

## [Chapter 38. Using ID views for Active Directory users](#using-id-views-for-active-directory-users) {#chapter-38.-using-id-views-for-active-directory-users .title}

You can use ID views to specify new values for the POSIX attributes of your Active Directory (AD) users in an IdM-AD Trust environment.

By default, IdM applies the **Default Trust View** to all AD users. You can configure additional ID views on individual IdM clients to further adjust which POSIX attributes specific users receive.

### [38.1. How the Default Trust View works](#how-the-default-trust-view-works) {#how-the-default-trust-view-works .title}

The **Default Trust View** is the default ID view that is always applied to AD users and groups in trust-based setups. It is created automatically when you establish the trust using the `ipa-adtrust-install`{.literal} command and cannot be deleted.

Note

The Default Trust View only accepts overrides for AD users and groups, not for IdM users and groups.

Using the Default Trust View, you can define custom POSIX attributes for AD users and groups, thus overriding the values defined in AD.

+-----------------+-----------------+--------------------+-----------------+
|                 | Values in AD    | Default Trust View | Result          |
+:================+:================+:===================+:================+
| **Login**       | ad_user         | ad_user            | ad_user         |
+-----------------+-----------------+--------------------+-----------------+
| **UID**         | 111             | 222                | 222             |
+-----------------+-----------------+--------------------+-----------------+
| **GID**         | 111             | (no value)         | 111             |
+-----------------+-----------------+--------------------+-----------------+

: Table 38.1. Applying the Default Trust View

Show more

You can also configure additional ID Views to override the Default Trust View on IdM clients. IdM applies the values from the host-specific ID view on top of the Default Trust View:

-   If an attribute is defined in the host-specific ID view, IdM applies the value from this ID view.
-   If an attribute is not defined in the host-specific ID view, IdM applies the value from the Default Trust View.

+-------------+--------------+--------------------+-----------------------+-------------+
|             | Values in AD | Default Trust View | Host-specific ID view | Result      |
+:============+:=============+:===================+:======================+:============+
| **Login**   | ad_user      | ad_user            | (no value)            | ad_user     |
+-------------+--------------+--------------------+-----------------------+-------------+
| **UID**     | 111          | 222                | 333                   | 333         |
+-------------+--------------+--------------------+-----------------------+-------------+
| **GID**     | 111          | (no value)         | 333                   | 333         |
+-------------+--------------+--------------------+-----------------------+-------------+

: Table 38.2. Applying a host-specific ID view on top of the Default Trust View

Show more

Note

You can only apply host-specific ID views to override the Default Trust View on IdM clients. IdM servers and replicas always apply the values from the Default Trust View.

**Additional resources**

-   [Using an ID view to override a user attribute value on an IdM client](#using-an-id-view-to-override-a-user-attribute-value-on-an-idm-client "Chapter 37. Using an ID view to override a user attribute value on an IdM client")

### [38.2. Defining global attributes for an AD user by modifying the Default Trust View](#defining-global-attributes-for-an-ad-user-by-modifying-the-default-trust-view) {#defining-global-attributes-for-an-ad-user-by-modifying-the-default-trust-view .title}

Modify the Default Trust View in Identity Management (IdM) to override POSIX attributes for Active Directory users across your entire deployment. Global attribute overrides ensure consistent user identity and permissions throughout your environment.

In this example, you set the GID for the AD user `ad_user@ad.example.com`{.literal} to 732000006.

**Prerequisites**

-   You have authenticated as an IdM administrator.
-   A group must exist with the GID or you must set the GID in an ID override for a group.

**Procedure**

1.  As an IdM administrator, create an ID override for the AD user in the Default Trust View that changes the GID number to 732000006:

    ``` {.language-plaintext tabindex="-1"}
    # ipa idoverrideuser-add 'Default Trust View' ad_user@ad.example.com --gidnumber=732000006
    ```

2.  Clear the entry for the `ad_user@ad.example.com`{.literal} user from the SSSD cache on all IdM servers and clients. This removes stale data and allows the new override value to apply.

    ``` {.language-plaintext tabindex="-1"}
    # sssctl cache-expire -u ad_user@ad.example.com
    ```

**Verification**

-   Retrieve information for the `ad_user@ad.example.com`{.literal} user to verify the GID reflects the updated value.

    ``` {.language-plaintext tabindex="-1"}
    # id ad_user@ad.example.com
    uid=702801456(ad_user@ad.example.com) gid=732000006(ad_admins)
    groups=732000006(ad_admins),702800513(domain users@ad.example.com)
    ```

### [38.3. Overriding Default Trust View attributes for an AD user on an IdM client with an ID view](#overriding-default-trust-view-attributes-for-an-ad-user-on-an-idm-client-with-an-id-view) {#overriding-default-trust-view-attributes-for-an-ad-user-on-an-idm-client-with-an-id-view .title}

Apply host-specific ID views to Active Directory (AD) users to override POSIX attributes from the Default Trust View on individual Identity Management (IdM) clients. In this way, you can customize AD user attributes like GIDs or UIDs for specific hosts without affecting the global trust configuration.

For example, you might need to give an AD user a different GID on one particular IdM client. This procedure explains how to set the GID for the `ad_user@ad.example.com`{.literal} AD user on the `client1.idm.example.com`{.literal} IdM client to 732001337.

**Prerequisites**

-   You have root access to the IdM client system.
-   You are logged in as a user with the required privileges, for example the `admin`{.literal} user.

**Procedure**

1.  On the IdM server, create an ID view. For example, to create an ID view named **example_for_client1**:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idview-add example_for_client1
    ---------------------------
    Added ID View "example_for_client1"
    ---------------------------
      ID View Name: example_for_client1
    ```

2.  On the IdM server, sdd a user override to the **example_for_client1** ID view. To override the user's GID:

    -   Enter the `ipa idoverrideuser-add`{.literal} command
    -   Add the name of the ID view
    -   Add the user name, also called the anchor
    -   Add the `--gidnumber=`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idoverrideuser-add example_for_client1 ad_user@ad.example.com --gidnumber=732001337
    -----------------------------
    Added User ID override "ad_user@ad.example.com"
    -----------------------------
      Anchor to override: ad_user@ad.example.com
      GID: 732001337
    ```

3.  On the IdM server, apply `example_for_client1`{.literal} to the `client1.idm.example.com`{.literal} IdM client:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idview-apply example_for_client1 --hosts=client1.idm.example.com
    -----------------------------
    Applied ID View "example_for_client1"
    -----------------------------
    hosts: client1.idm.example.com
    ---------------------------------------------
    Number of hosts the ID View was applied to: 1
    ---------------------------------------------
    ```

    Note

    The `ipa idview-apply`{.literal} command also accepts the `--hostgroups`{.literal} option. The option applies the ID view to hosts that belong to the specified host group, but does not associate the ID view with the host group itself. Instead, the `--hostgroups`{.literal} option expands the members of the specified host group and applies the `--hosts`{.literal} option individually to every one of them.

    This means that if a host is added to the host group in the future, the ID view does not apply to the new host.

4.  On the IdM client, clear the entry for the `ad_user@ad.example.com`{.literal} user from the SSSD cache on the `client1.idm.example.com`{.literal} IdM client. This removes stale data and allows the new override value to apply.

    ``` {.language-plaintext tabindex="-1"}
    # sssctl cache-expire -u ad_user@ad.example.com
    ```

**Verification**

1.  `SSH`{.literal} to the client system as **ad_user@ad.example.com**:

    ``` {.language-plaintext tabindex="-1"}
    # ssh ad_user@ad.example.com@client1.idm.example.com
    ```

2.  On the client system, retrieve information for the `ad_user@ad.example.com`{.literal} user to verify the GID reflects the updated value.

    ``` {.language-plaintext tabindex="-1"}
    [ad_user@ad.example.com@client1 ~]$ id ad_user@ad.example.com
    uid=702801456(ad_user@ad.example.com) gid=732001337(admins2)
    groups=732001337(admins2),702800513(domain users@ad.example.com)
    ```

## [Chapter 39. Adjusting ID ranges manually](#adjusting-id-ranges-manually) {#chapter-39.-adjusting-id-ranges-manually .title}

Adjust Identity Management (IdM) ID ranges manually to control how unique user ID (UID) and group ID (GID) numbers are assigned across your deployment.

By default, IdM automatically assigns ID ranges to prevent ID numbers overlapping between replicas, but you can manually set ranges during server installation or define a replica's DNA ID range when needed.

### [39.1. ID ranges](#id-ranges) {#id-ranges .title}

In Identity Management (IdM), ID numbers are divided into *ID ranges*. Keeping separate numeric ranges for individual servers and replicas eliminates the chance that an ID number issued for an entry is already used by another entry on another server or replica.

Note that there are two distinct types of ID ranges:

-   The IdM ***ID range***, which is assigned during the installation of the first server. This range cannot be modified after it is created. However, you can create a new IdM ID range in addition to the original one.

-   The ***Distributed Numeric Assignment*** (DNA) ID ranges, which can be modified by the user. These have to fit within an existing IdM ID range.

    Replicas can also have a **next** DNA ID range assigned. A replica uses its next range when it runs out of IDs in its current range. Next ranges are not assigned automatically when a replica is deleted and you must assign them manually.

The ranges are updated and shared between the server and replicas by the DNA plug-in, as part of the back end 389 Directory Server instance for the domain.

The DNA range definition is set by two attributes:

-   The server's next available number: the low end of the DNA range
-   The range size: the number of ID's in the DNA range

The initial bottom range is set during the plug-in instance configuration. After that, the plug-in updates the bottom value. Breaking the available numbers into ranges allows the servers to continually assign numbers without overlapping with each other.

**Additional resources**

-   [Automatic ID ranges assignment](#automatic-id-ranges-assignment "39.2. Automatic ID ranges assignment")
-   [Adding a new IdM ID range](#adding-a-new-idm-id-range "39.4. Adding a new IdM ID range")
-   [Assigning DNA ID ranges manually](#assigning-dna-id-ranges-manually "39.11. Assigning DNA ID ranges manually")

### [39.2. Automatic ID ranges assignment](#automatic-id-ranges-assignment) {#automatic-id-ranges-assignment .title}

Identity Management (IdM) automatically assigns ID ranges during installation to ensure unique user and group identifiers across your deployment. Understanding automatic ID range assignment helps you plan capacity and troubleshoot ID conflicts.

IdM ID ranges
:   By default, a local domain IdM ID range (`ipa-local`{.literal}) is automatically assigned during the IdM server installation. The `ipa-server-install`{.literal} command randomly selects and assigns a range of 200,000 IDs from a total of 10,000 possible ranges. Selecting a random range in this way significantly reduces the probability of conflicting IDs in case you decide to merge two separate IdM domains in the future.

Note

Avoid modifying this IdM ID range after it is created. You can manually adjust the Distributed Numeric Assignment (DNA) ID ranges, using the commands described in [Assigning DNA ID ranges manually](#assigning-dna-id-ranges-manually "39.11. Assigning DNA ID ranges manually"). A DNA range matching the IdM ID range is automatically created during installation.

DNA ID ranges
:   If you have a single IdM server installed, it controls the whole DNA ID range. When you install a new replica and the replica requests its own DNA ID range, the initial ID range for the server splits and is distributed between the server and replica: the replica receives half of the remaining DNA ID range that is available on the initial server. The server and replica then use their respective portions of the original ID range for new user or group entries. Also, if the replica is close to depleting its allocated ID range and fewer than 100 IDs remain, the replica contacts the other available servers to request a new DNA ID range.

Important

When you install a replica, it **does not** immediately receive an ID range. A replica receives an ID range the first time the DNA plug-in is used, for example when you first add a user.

If the initial server stops functioning before the replica requests a DNA ID range from it, the replica is unable to contact the server to request the ID range. Attempting to add a new user on the replica then fails. In such situations, [you can find out what ID range is assigned to the disabled server](#displaying-currently-assigned-dna-id-ranges "39.9. Displaying currently assigned DNA ID ranges"), and [assign an ID range to the replica manually](#assigning-dna-id-ranges-manually "39.11. Assigning DNA ID ranges manually").

### [39.3. Assigning the IdM ID range manually during server installation](#assigning-the-idm-id-range-manually-during-server-installation) {#assigning-the-idm-id-range-manually-during-server-installation .title}

You can set a custom ID range during Identity Management (IdM) server installation. Manual ID range assignment gives you control over the numeric space used for user and group identifiers.

Important

Do not set ID ranges that include UID values of 1000 and lower; these values are reserved for system use. Also, do not set an ID range that would include the 0 value; the SSSD service does not handle the 0 ID value.

**Procedure**

-   You can define the IdM ID range manually during server installation by using the following two options with `ipa-server-install`{.literal}:

    -   `--idstart`{.literal} gives the starting value for UID and GID numbers.
    -   `--idmax`{.literal} gives the maximum UID and GID number; by default, the value is the `--idstart`{.literal} starting value plus 199,999.

**Verification**

-   To check if the ID range was assigned correctly, you can display the assigned IdM ID range by using the `ipa idrange-find`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # ipa idrange-find
    ---------------
    1 range matched
    ---------------
      Range name: IDM.EXAMPLE.COM_id_range
      First Posix ID of the range: 882200000
      Number of IDs in the range: 200000
      Range type: local domain range
    ----------------------------
    Number of entries returned 1
    ----------------------------
    ```

### [39.4. Adding a new IdM ID range](#adding-a-new-idm-id-range) {#adding-a-new-idm-id-range .title}

Create a new ID range in Identity Management (IdM) when the original range is depleted to ensure replicas can continue assigning user and group IDs. This prevents ID assignment failures and maintains continuous operation of your IdM deployment.

Important

Adding a new IdM ID range does not create new DNA ID ranges automatically. You must assign new DNA ID ranges to replicas manually as needed. For more information about how to do this, see [assigning DNA ID ranges manually](#assigning-dna-id-ranges-manually "39.11. Assigning DNA ID ranges manually").

**Procedure**

1.  To create a new IdM ID range, use the `ipa idrange-add`{.literal} command. You must specify the new range name, the first ID number of the range, the range size, and the first RID number of the primary and secondary RID range:

    ``` {.language-plaintext tabindex="-1"}
    # ipa idrange-add IDM.EXAMPLE.COM_new_range --base-id 5000 --range-size 1000 --rid-base 300000 --secondary-rid-base 1300000

    ipa: WARNING: Service dirsrv@IDM-EXAMPLE-COM.service requires restart on IPA server <all IPA servers> to apply configuration changes.
    ------------------------------------------
    Added ID range "IDM.EXAMPLE.COM_new_range"
    ------------------------------------------
      Range name: IDM.EXAMPLE.COM_new_range
      First Posix ID of the range: 5000
      Number of IDs in the range: 1000
      First RID of the corresponding RID range: 300000
      First RID of the secondary RID range: 1300000
      Range type: local domain range
    ```

2.  Restart the Directory Server service **on all IdM servers** in the deployment:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart dirsrv@IDM-EXAMPLE-COM.service
    ```

    This ensures that when you create users with UIDs from the new range, they have security identifiers (SIDs) assigned.

3.  Optional: Update the ID range immediately:

    a.  Clear the System Security Services Daemon (SSSD) cache:

        ``` {.language-plaintext tabindex="-1"}
        # sss_cache -E
        ```

    b.  Restart the SSSD daemon:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart sssd
        ```

        Note

        If you do not clear the SSSD cache and restart the service, SSSD only detects the new ID range when it updates the domain list and other configuration data stored on the IdM server.

**Verification**

-   You can check if the new range is set correctly by using the `ipa idrange-find`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # ipa idrange-find
    ----------------
    2 ranges matched
    ----------------
      Range name: IDM.EXAMPLE.COM_id_range
      First Posix ID of the range: 882200000
      Number of IDs in the range: 200000
      Range type: local domain range

      Range name: IDM.EXAMPLE.COM_new_range
      First Posix ID of the range: 5000
      Number of IDs in the range: 1000
      First RID of the corresponding RID range: 300000
      First RID of the secondary RID range: 1300000
      Range type: local domain range
    ----------------------------
    Number of entries returned 2
    ----------------------------
    ```

### [39.5. The role of security and relative identifiers in IdM ID ranges](#the-role-of-security-and-relative-identifiers-in-idm-id-ranges) {#the-role-of-security-and-relative-identifiers-in-idm-id-ranges .title}

Identity Management (IdM) uses security identifiers (SIDs) and relative identifiers (RIDs) derived from its ID ranges to uniquely identify users and groups, ensuring compatibility with Active Directory and preventing SID conflicts when POSIX UIDs and GIDs overlap.

An IdM ID range is defined by several parameters:

-   The range name
-   The first POSIX ID of the range
-   The range size: the number of IDs in the range
-   The first **relative identifier** (RID) of the corresponding **RID range**
-   The first RID of the **secondary RID range**

You can view these values by using the `ipa idrange-show`{.literal} command:

``` {.language-plaintext tabindex="-1"}
$ ipa idrange-show IDM.EXAMPLE.COM_id_range
  Range name: IDM.EXAMPLE.COM_id_range
  First Posix ID of the range: 196600000
  Number of IDs in the range: 200000
  First RID of the corresponding RID range: 1000
  First RID of the secondary RID range: 1000000
  Range type: local domain range
```

Security identifiers

:   The data from the ID ranges of the local domain are used by the IdM server internally to assign unique **security identifiers** (SIDs) to IdM users and groups. The SIDs are stored in the user and group objects. A user's SID consists of the following:

    -   The domain SID
    -   The user's **relative identifier** (RID), which is a four-digit 32-bit value appended to the domain SID

For example, if the domain SID is S-1-5-21-123-456-789 and the RID of a user from this domain is 1008, then the user has the SID of S-1-5-21-123-456-789-1008.

Relative identifiers
:   The RID itself is computed in the following way:

Subtract the first POSIX ID of the range from the user's POSIX UID, and add the first RID of the corresponding RID range to the result. For example, if the UID of *idmuser* is 196600008, the first POSIX ID is 196600000, and the first RID is 1000, then *idmuser*\'s RID is 1008.

Note

The algorithm computing the user's RID checks if a given POSIX ID falls into the ID range allocated before it computes a corresponding RID. For example, if the first ID is 196600000 and the range size is 200000, then the POSIX ID of 1600000 is outside of the ID range and the algorithm does not compute a RID for it.

Secondary relative identifiers
:   In IdM, a POSIX UID can be identical to a POSIX GID. This means that if *idmuser* already exists with the UID of 196600008, you can still create a new *idmgroup* group with the GID of 196600008.

However, a SID can define only one object, a user *or* a group. The SID of S-1-5-21-123-456-789-1008 that has already been created for *idmuser* cannot be shared with *idmgroup*. An alternative SID must be generated for *idmgroup*.

IdM uses a **secondary relative identifier**, or secondary RID, to avoid conflicting SIDs. This secondary RID consists of the following:

-   The secondary RID base
-   A range size; by default identical with the base range size

In the example above, the secondary RID base is set to 1000000. To compute the RID for the newly created *idmgroup*: subtract the first POSIX ID of the range from the user's POSIX UID, and add the first RID of the secondary RID range to the result. *idmgroup* is therefore assigned the RID of 1000008. Consequently, the SID of *idmgroup* is S-1-5-21-123-456-789-1000008.

IdM uses the secondary RID to compute a SID only if a user or a group object was previously created with a manually set POSIX ID. Otherwise, automatic assignment prevents assigning the same ID twice.

**Additional resources**

-   [Using Ansible to add a new local IdM ID range](#using-ansible-to-add-a-new-local-idm-id-range "39.7. Using Ansible to add a new local IdM ID range")

### [39.6. Detecting and fixing ID range issues automatically](#detecting-and-fixing-id-range-issues-automatically) {#detecting-and-fixing-id-range-issues-automatically .title}

Automatically detect and resolve ID range misconfigurations in Identity Management (IdM) to ensure proper SID generation for Kerberos authorization. Fixing range issues prevents authentication failures and maintains secure access to resources.

Kerberos in IdM uses the Privilege Attribute Certificate (PAC) for authorization. For this to function correctly, users and groups must have a Security Identifier (SID) assigned. SIDs can only be generated for entities that are within a valid `ipa-local`{.literal} ID range.

If users or groups are created outside of a defined `ipa-local`{.literal} range, or if an existing range is misconfigured, the SID generation task can fail. This can prevent users from authenticating and obtaining Kerberos tickets.

You can use the `ipa-idrange-fix`{.literal} command-line tool to analyze and repair these inconsistencies. The tool identifies users and groups outside of valid ranges, proposes the creation of new ranges to cover them, and applies the changes upon confirmation.

**Prerequisites**

-   You have `root`{.literal} access to the IdM server where you will run the tool.

    Important

    Red Hat strongly recommends creating a full backup of the system before you apply any changes suggested by the `ipa-idrange-fix`{.literal} tool.

**Procedure**

1.  Run `ipa-idrange-fix`{.literal} to analyze the current ID ranges. You can customize this by using various options, such as:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-idrange-fix --rangegap 300000 --minrange 20 --ridoffset 200000
    ```

    -   `--rangegap <value>`{.literal}: Specifies the maximum gap between IDs to be included in a single proposed range. The default is `200000`{.literal}.

    -   `--minrange <value>`{.literal}: Sets the minimum number of IDs required to form a valid new range. Any group of IDs smaller than this will be listed as outliers for manual resolution. The default is `10`{.literal}.

    -   `--ridoffset <value>`{.literal}: Sets an offset for new RID bases to allow for future expansion of existing ranges. The default is `100000`{.literal}.

        Note

        By default, the `ipa-idrange-fix`{.literal} tool ignores users and groups with IDs below 1000, as these are typically reserved for system accounts. To include these entities in the analysis, which is not recommended, use the `--allowunder1000`{.literal} option.

2.  The tool displays proposed changes, such as creating new ID ranges. Review the proposed changes carefully.

    Note

    `ipa-idrange-fix`{.literal} does not create new SIDs for users and groups who do not have them. To create missing SIDs, see [Enabling Security Identifiers (SIDs) in IdM](#enabling-security-identifiers-sids-in-idm "14.2. Enabling Security Identifiers (SIDs) in IdM").

3.  Enter `yes`{.literal} to apply the changes.

    Important

    Do not run `ipa-idrange-fix`{.literal} with the `--unattended`{.literal} option unless you are certain you want to automatically apply all proposed changes.

**Verification**

1.  Review the log file to see the applied changes:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/ipa/ipa-idrange-fix.log
    ```

2.  Use the `ipa idrange-find --all`{.literal} command to verify that the new ID ranges have been created correctly:

    ``` {.language-plaintext tabindex="-1"}
    # ipa idrange-find --all

    ----------------
    2 ranges matched
    ----------------
    dn: cn=IDM.EXAMPLE.COM_id_range,cn=ranges,cn=accounts,dc=example,dc=com
    Range name: IDM.EXAMPLE.COM_id_range
    First Posix ID of the range: 882200000
    Number of IDs in the range: 200000
    First RID of the corresponding RID range: 1000
    First RID of the secondary RID range: 1000000
    Range type: local domain range
    ipaUniqueID: 569bf864-9d45-11ea-bea3-525400f6f085
    objectclass: ipaIdRange, top

    dn: cn=IDM.EXAMPLE.COM_new_id_range,cn=ranges,cn=accounts,dc=example,dc=com
    Range name: IDM.EXAMPLE.COM_new_id_range
    First Posix ID of the range: 12000000
    Number of IDs in the range: 200000
    First RID of the corresponding RID range: 10000
    First RID of the secondary RID range: 20000000
    Range type: local domain range
    ipaUniqueID: 7a2b3c4d-e5f6-7890-a1b2-c3d4e5f67890
    objectclass: ipaIdRange, top
    ----------------------------
    Number of entries returned 2
    ----------------------------
    ```

### [39.7. Using Ansible to add a new local IdM ID range](#using-ansible-to-add-a-new-local-idm-id-range) {#using-ansible-to-add-a-new-local-idm-id-range .title}

Create a new Identity Management (IdM) ID range with Ansible when the original range is depleted to extend your domain's available user and group IDs.

Note

Adding a new IdM ID range does not create new DNA ID ranges automatically. You need to assign new DNA ID ranges manually as needed. For more information about how to do this, see [Assigning DNA ID ranges manually](#assigning-dna-id-ranges-manually "39.11. Assigning DNA ID ranges manually").

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Create the `idrange-present.yml`{.literal} playbook with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to manage idrange
      hosts: ipaserver
      become: no

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure local idrange is present
        ipaidrange:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: new_id_range
          base_id: 12000000
          range_size: 200000
          rid_base: 1000000
          secondary_rid_base: 200000000
    ```

3.  Save the file.

4.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory idrange-present.yml
    ```

5.  `SSH`{.literal} to `ipaserver`{.literal} and restart the Directory Server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart dirsrv@IDM.EXAMPLE.COM.service
    ```

    This ensures that when you create users with UIDs from the new range, they have security identifiers (SIDs) assigned.

6.  Optional: Update the ID range immediately:

    a.  On `ipaserver`{.literal}, clear the System Security Services Daemon (SSSD) cache:

        ``` {.language-plaintext tabindex="-1"}
        # sss_cache -E
        ```

    b.  On `ipaserver`{.literal}, restart the SSSD daemon:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart sssd
        ```

    Note

    If you do not clear the SSSD cache and restart the service, SSSD only detects the new ID range when it updates the domain list and other configuration data stored on the IdM server.

**Verification**

-   You can check if the new range is set correctly by using the `ipa idrange-find`{.literal} command:

``` {.language-plaintext tabindex="-1"}
# ipa idrange-find
----------------
2 ranges matched
----------------
  Range name: IDM.EXAMPLE.COM_id_range
  First Posix ID of the range: 882200000
  Number of IDs in the range: 200000
  Range type: local domain range

  Range name: IDM.EXAMPLE.COM_new_id_range
  First Posix ID of the range: 12000000
  Number of IDs in the range: 200000
  Range type: local domain range
----------------------------
Number of entries returned 2
----------------------------
```

**Additional resources**

-   [The role of security and relative identifiers in IdM ID ranges](#the-role-of-security-and-relative-identifiers-in-idm-id-ranges "39.5. The role of security and relative identifiers in IdM ID ranges")

### [39.8. Removing an ID range after removing a trust to AD](#removing-an-id-range-after-removing-a-trust-to-ad) {#removing-an-id-range-after-removing-a-trust-to-ad .title}

Manually delete the ID range associated with a removed Active Directory (AD) trust to clean up the Identity Management (IdM) configuration. This action purges unused ID allocations from the system.

Warning

IDs allocated to ID ranges associated with trusted domains might still be used for ownership of files and directories on systems enrolled into IdM.

If you remove the ID range that corresponds to an AD trust that you have removed, you will not be able to resolve the ownership of any files and directories owned by AD users.

**Prerequisites**

-   You have removed a trust to an AD environment.

**Procedure**

1.  Display all the ID ranges that are currently in use:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idrange-find
    ```

2.  Identify the name of the ID range associated with the trust you have removed. The first part of the name of the ID range is the name of the trust, for example `AD.EXAMPLE.COM_id_range`{.literal}.

3.  Remove the range:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idrange-del AD.EXAMPLE.COM_id_range
    ```

4.  Restart the SSSD service to remove references to the ID range you have removed.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl restart sssd
    ```

### [39.9. Displaying currently assigned DNA ID ranges](#displaying-currently-assigned-dna-id-ranges) {#displaying-currently-assigned-dna-id-ranges .title}

Display active and next Distributed Numeric Assignment (DNA) ID ranges in Identity Management (IdM) to monitor UID and GID allocation across your topology. Checking DNA ranges helps prevent conflicts and ensures continuous ID assignment.

**Procedure**

-   To display which DNA ID ranges are configured for the servers in the topology, use the following commands:

    -   `ipa-replica-manage dnarange-show`{.literal} displays the active DNA ID range that is set on all servers or, if you specify a server, only on the specified server, for example:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-replica-manage dnarange-show
        serverA.example.com: 1001-1500
        serverB.example.com: 1501-2000
        serverC.example.com: No range set

        # ipa-replica-manage dnarange-show serverA.example.com
        serverA.example.com: 1001-1500
        ```

    -   `ipa-replica-manage dnanextrange-show`{.literal} displays the next DNA ID range currently set on all servers or, if you specify a server, only on the specified server, for example:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-replica-manage dnanextrange-show
        serverA.example.com: 2001-2500
        serverB.example.com: No on-deck range set
        serverC.example.com: No on-deck range set

        # ipa-replica-manage dnanextrange-show serverA.example.com
        serverA.example.com: 2001-2500
        ```

### [39.10. Manual ID range assignment](#manual-id-range-assignment) {#manual-id-range-assignment .title}

Manual DNA ID range assignment gives you direct control over ID allocation when automatic distribution between Identity Management (IdM) replicas cannot resolve the situation on its own.

This may be necessary for example when:

-   A replica has run out of IDs and the IdM ID range is depleted

    A replica has exhausted the DNA ID range that was assigned to it, and requesting additional IDs failed because no more free IDs are available in the IdM range.

    To solve this situation, extend the DNA ID range assigned to the replica. You can do this in two ways:

    -   Shorten the DNA ID range assigned to a different replica, then assign the newly available values to the depleted replica.
    -   Create a new IdM ID range, then set a new DNA ID range for the replica within this created IdM range.

-   A replica stopped functioning

    A replica's DNA ID range is not automatically retrieved when the replica stops functioning and must be deleted, which means the DNA ID range previously assigned to the replica becomes unavailable. You want to recover the DNA ID range and make it available for other replicas.

    To do this, find out what the ID range values are, before manually assigning that range to a different server. Also, to avoid duplicate UIDs or GIDs, make sure that no ID value from the recovered range was previously assigned to a user or group; you can do this by examining the UIDs and GIDs of existing users and groups.

Note

If you assign a new DNA ID range, the UIDs of the already existing entries on the server or replica stay the same. This does not pose a problem because even if you change the current DNA ID range, IdM keeps a record of what ranges were assigned in the past.

**Additional resources**

-   [Adding a new IdM ID range](#adding-a-new-idm-id-range "39.4. Adding a new IdM ID range")
-   [Displaying currently assigned DNA ID ranges](#displaying-currently-assigned-dna-id-ranges "39.9. Displaying currently assigned DNA ID ranges")
-   [Assigning DNA ID ranges manually](#assigning-dna-id-ranges-manually "39.11. Assigning DNA ID ranges manually")

### [39.11. Assigning DNA ID ranges manually](#assigning-dna-id-ranges-manually) {#assigning-dna-id-ranges-manually .title}

Manually assign Distributed Numeric Assignment (DNA) ID ranges to Identity Management (IdM) replicas to recover ranges from non-functioning replicas or rebalance ID distribution. This ensures all replicas can continue assigning unique user and group IDs without interruption.

When adjusting a DNA ID range manually, make sure that the newly adjusted range is included in the IdM ID range; you can check this using the `ipa idrange-find`{.literal} command. Otherwise, the command fails.

Important

Be careful not to create overlapping ID ranges. If any of the ID ranges you assign to servers or replicas overlap, it could result in two different servers assigning the same ID value to different entries.

**Prerequisites**

-   Optional: If you are recovering a DNA ID range from a non-functioning replica, first find the ID range using the commands described in [Displaying currently assigned DNA ID ranges](#displaying-currently-assigned-dna-id-ranges "39.9. Displaying currently assigned DNA ID ranges").

**Procedure**

-   To define the current DNA ID range for a specified server, use `ipa-replica-manage dnarange-set`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-replica-manage dnarange-set serverA.example.com 1250-1499
    ```

-   To define the next DNA ID range for a specified server, use `ipa-replica-manage dnanextrange-set`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-replica-manage dnanextrange-set serverB.example.com 1500-5000
    ```

**Verification**

-   You can check that the new DNA ranges are set correctly by using the commands described in [Displaying the currently assigned DNA ID ranges](#displaying-currently-assigned-dna-id-ranges "39.9. Displaying currently assigned DNA ID ranges").

### [39.12. Enabling UIDs up to Linux maximum limit for legacy systems compatibility](#enabling-uids-up-to-linux-maximum-limit-for-legacy-systems-compatibility) {#enabling-uids-up-to-linux-maximum-limit-for-legacy-systems-compatibility .title}

Configure User and Group IDs up to the Linux maximum limit of 4,294,967,293 (2\^32-1) in rare Identity Management (IdM) deployments where the standard ID range is insufficient.

Warning

In standard deployments, IdM reserves the 2,147,483,648 - 4,294,836,223 range for subordinate IdS (subIDs). Enabling the 2\^31 to 2\^32-1 UID range requires disabling the subID feature and therefore conflicts with modern Linux capabilities.

**Prerequisites**

-   You are running RHEL 10.1 or later.
-   You have obtained IdM `admin`{.literal} credentials.
-   You have `root`{.literal} permissions on an IdM server.

**Procedure**

1.  Disable the subordinate ID feature:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa config-mod --addattr ipaconfigstring=SubID:Disable
    ```

2.  Remove any existing subordinate ID ranges:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idrange-del <id_range>
    ```

3.  On the IdM server, ensure the internal DNA plugin configuration is correctly removed:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-server-upgrade
    ```

4.  Add a new local ID range that covers the 2\^31 to 2\^32-1 space. Ensure that you define RID bases for this new range so that IdM can generate SIDs properly for users and groups. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa idrange-add IDM.EXAMPLE.COM_new_range --base-id 2200000000 --range-size 200000 --rid-base 1000 --secondary-rid-base 2300000000
    ```

    Note

    You can only disable the subordinate ID feature if no subordinate IDs have been allocated yet.

## [Chapter 40. Managing subID ranges manually](#managing-subid-ranges-manually) {#chapter-40.-managing-subid-ranges-manually .title}

Manage subordinate ID (subID) ranges manually in Identity Management (IdM) to support containerized environments that require user namespace mapping. SubID ranges define the user and group IDs available for container processes.

### [40.1. Generating subID ranges using IdM CLI](#generating-subid-ranges-using-idm-cli) {#generating-subid-ranges-using-idm-cli .title}

Generate and assign subID ranges to Identity Management (IdM) users using the CLI so that each user has a unique, centrally managed block of subordinate UIDs and GIDs.

**Prerequisites**

-   The IdM users exist.
-   You have obtained an IdM `admin`{.literal} ticket-granting ticket (TGT). For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   You have `root`{.literal} access to the IdM host where you are executing the procedure.

**Procedure**

1.  Optional: Check for existing subID ranges:

    ``` {.language-plaintext tabindex="-1"}
    # ipa subid-find
    ```

2.  If a subID range does not exist, select one of the following options:

    -   Generate and assign a subID range to an IdM user:

        ``` {.language-plaintext tabindex="-1"}
        # ipa subid-generate --owner=idmuser

        Added subordinate id "359dfcef-6b76-4911-bd37-bb5b66b8c418"

          Unique ID: 359dfcef-6b76-4911-bd37-bb5b66b8c418
          Description: auto-assigned subid
          Owner: idmuser
          SubUID range start: 2147483648
          SubUID range size: 65536
          SubGID range start: 2147483648
          SubGID range size: 65536
        ```

    -   Generate and assign subID ranges to all IdM users:

        ``` {.language-plaintext tabindex="-1"}
        # /usr/libexec/ipa/ipa-subids --all-users

        Found 2 user(s) without subordinate ids
          Processing user 'user4' (1/2)
          Processing user 'user5' (2/2)
        Updated 2 user(s)
        The ipa-subids command was successful
        ```

3.  Optional: Assign subID ranges to new IdM users by default:

    ``` {.language-plaintext tabindex="-1"}
    # ipa config-mod --user-default-subid=True
    ```

**Verification**

-   Verify that the user has a subID range assigned:

    ``` {.language-plaintext tabindex="-1"}
    # ipa subid-find --owner=idmuser

    1 subordinate id matched

      Unique ID: 359dfcef-6b76-4911-bd37-bb5b66b8c418
      Owner: idmuser
      SubUID range start: 2147483648
      SubUID range size: 65536
      SubGID range start: 2147483648
      SubGID range size: 65536

    Number of entries returned 1
    ```

### [40.2. Generating subID ranges using IdM WebUI interface](#generating-subid-ranges-using-idm-webui-interface) {#generating-subid-ranges-using-idm-webui-interface .title}

Generate and assign subID ranges to Identity Management (IdM) users using the WebUI so that each user has a unique, centrally managed block of subordinate UIDs and GIDs.

**Prerequisites**

-   The IdM user exists.
-   You have obtained an IdM `admin`{.literal} Kerberos ticket (TGT). See [Logging in to IdM in the Web UI: Using a Kerberos ticket](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-idm-in-the-web-ui-using-a-kerberos-ticket) for more details.
-   You have `root`{.literal} access to the IdM host where you are executing the procedure.

**Procedure**

1.  In the IdM WebUI interface expand the **Subordinate IDs** tab and choose the **Subordinate IDs** option.
2.  When the **Subordinate IDs** interface appears, click the **Add** button in the upper-right corner of the interface. The **Add subid** window appears.
3.  In the **Add subid** window choose an owner, that is the user to whom you want to assign a subID range.
4.  Click the **Add** button.

**Verification**

-   View the table under the **Subordinate IDs** tab. A new record shows in the table. The owner is the user to whom you assigned the subID range.

### [40.3. Viewing subID information about IdM users by using IdM CLI](#viewing-subid-information-about-idm-users-by-using-idm-cli) {#viewing-subid-information-about-idm-users-by-using-idm-cli .title}

Search for and view subID ranges assigned to Identity Management (IdM) users by using the CLI.

**Prerequisites**

-   You have configured a subID range on the IdM client. For more information, see [Generating subID ranges using IdM CLI](#generating-subid-ranges-using-idm-cli "40.1. Generating subID ranges using IdM CLI").
-   You have obtained an IdM `admin`{.literal} ticket-granting ticket (TGT). For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

-   To view the details about a subID range:

    -   If you know the unique ID hash of the Identity Management (IdM) user that is the owner of the range:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa subid-show 359dfcef-6b76-4911-bd37-bb5b66b8c418

          Unique ID: 359dfcef-6b76-4911-bd37-bb5b66b8c418
          Owner: idmuser
          SubUID range start: 2147483648
          SubUID range size: 65536
          SubGID range start: 2147483648
          SubGID range size: 65536
        ```

    -   If you know a specific subID from that range:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa subid-match --subuid=2147483670

        1 subordinate id matched

          Unique ID: 359dfcef-6b76-4911-bd37-bb5b66b8c418
          Owner: uid=idmuser
          SubUID range start: 2147483648
          SubUID range size: 65536
          SubGID range start: 2147483648
          SubGID range size: 65536

        Number of entries returned 1
        ```

### [40.4. Listing subID ranges using the getsubid command](#listing-subid-ranges-using-the-getsubid-command) {#listing-subid-ranges-using-the-getsubid-command .title}

List subordinate ID ranges for Identity Management (IdM) or local users using the `getsubids`{.literal} command to verify subID allocation for rootless containers. This helps ensure users have the necessary ID ranges for container operations.

**Prerequisites**

-   The **idmuser** user exists in IdM.
-   The `shadow-utils-subid`{.literal} package is installed.

**Procedure**

1.  Configure the `shadow-utils`{.literal} utility to use IdM subID ranges by setting the `subid`{.literal} variable to the `sss`{.literal} value:

    ``` {.language-plaintext tabindex="-1"}
    # authselect enable-feature with-subid
    ```

    Note

    You can provide only one value for the `subid`{.literal} field. Setting the `subid`{.literal} field to the `file`{.literal} value or no value instead of `sss`{.literal} configures the `shadow-utils`{.literal} utility to use the subID ranges from the `/etc/subuid`{.literal} and `/etc/subgid`{.literal} files.

2.  List the subID range for an IdM user:

    ``` {.language-plaintext tabindex="-1"}
    $ getsubids idmuser
    0: idmuser 2147483648 65536
    ```

    The first value, 2147483648, indicates the subID range start. The second value, 65536, indicates the size of the range.

## [Chapter 41. Managing Hosts in IdM CLI](#managing-hosts-in-idm-cli) {#chapter-41.-managing-hosts-in-idm-cli .title}

Manage hosts and host entries in Identity Management (IdM) using the CLI to control host enrollment, authentication, and participation in the IdM domain. Host entries store identity information that enables hosts to interact with IdM services.

### [41.1. Hosts in IdM](#hosts-in-idm) {#hosts-in-idm .title}

Manage machines as Identity Management (IdM) hosts to establish trust relationships, enforce access policies, and provision shared services like DNS and Kerberos. Host entries in Identity Management (IdM) LDAP enable centralized machine management across your domain.

IdM manages these identities:

-   Users
-   Services
-   Hosts

A host represents a machine. As an IdM identity, a host has an entry in the IdM LDAP, that is the 389 Directory Server instance of the IdM server.

The host entry in IdM LDAP is used to establish relationships between other hosts and even services within the domain. These relationships are part of *delegating* authorization and control to hosts within the domain. Any host can be used in `host-based access control`{.literal} (HBAC) rules.

IdM domain establishes a commonality between machines, with common identity information, common policies, and shared services. Any machine that belongs to a domain functions as a client of the domain, which means it uses the services that the domain provides. IdM domain provides three main services specifically for machines:

-   DNS
-   Kerberos
-   Certificate management

Hosts in IdM are closely connected with the services running on them:

-   Service entries are associated with a host.
-   A host stores both the host and the service Kerberos principals.

### [41.2. Host enrollment](#host-enrollment) {#host-enrollment .title}

Enroll hosts as Identity Management (IdM) clients to enable them to participate in the IdM domain with Kerberos authentication and centralized identity services.

Enrolling a host consists of:

-   Creating a host entry in IdM LDAP: possibly using the `ipa host-add`{.literal} command in IdM CLI, or the equivalent IdM Web UI operation.
-   Configuring IdM services on the host, for example the System Security Services Daemon (SSSD), Kerberos, and certmonger, and joining the host to the IdM domain.

The two actions can be performed separately or together.

If performed separately, they allow for dividing the two tasks between two users with different levels of privilege. This is useful for bulk deployments.

The `ipa-client-install`{.literal} command can perform the two actions together. The command creates a host entry in IdM LDAP if that entry does not exist yet, and configures both the Kerberos and SSSD services for the host. The command brings the host within the IdM domain and allows it to identify the IdM server it will connect to. If the host belongs to a DNS zone managed by IdM, `ipa-client-install`{.literal} adds DNS records for the host too. The command must be run on the client.

**Additional resources**

-   [Options for adding IdM host entries from the IdM CLI](#options-for-adding-idm-host-entries-from-the-idm-cli "41.7. Options for adding IdM host entries from the IdM CLI")
-   [Adding host entries from the Web UI](#adding-host-entries-from-the-web-ui "Chapter 42. Adding host entries from the Web UI")

### [41.3. User privileges required for host enrollment](#user-privileges-required-for-host-enrollment) {#user-privileges-required-for-host-enrollment .title}

Enrolling a host in Identity Management (IdM) requires specific user privileges depending on whether the host entry already exists and whether a one-time password is used. Understanding these requirements prevents enrollment failures and unauthorized machine additions to the domain.

User privileges for optionally manually creating a host entry in IdM LDAP
:   The user privilege required for creating a host entry in IdM LDAP using the `ipa host-add`{.literal} CLI command or the IdM Web UI is `Host Administrators`{.literal}. The `Host Administrators`{.literal} privilege can be obtained through the `IT Specialist`{.literal} role.

User privileges for joining the client to the IdM domain
:   Hosts are configured as IdM clients when running the `ipa-client-install`{.literal} command. The level of credentials required for running the `ipa-client-install`{.literal} command depends on which of the following enrolling scenarios you find yourself in:

-   The host entry in IdM LDAP does not exist. For this scenario, you need a full administrator's credentials or the `Host Administrators`{.literal} role. A full administrator is a member of the `admins`{.literal} group. The `Host Administrators`{.literal} role provides privileges to add hosts and enroll hosts.
-   The host entry in IdM LDAP exists. For this scenario, you need a limited administrator's credentials to run `ipa-client-install`{.literal} successfully. The limited administrator in this case has the `Enrollment Administrator`{.literal} role, which provides the `Host Enrollment`{.literal} privilege.
-   The host entry in IdM LDAP exists, and an OTP has been generated for the host by a full or limited administrator. For this scenario, you can install an IdM client as an ordinary user if you run the `ipa-client-install`{.literal} command with the `--password`{.literal} option, supplying the correct OTP.

After enrollment, IdM hosts authenticate every new session to be able to access IdM resources. Machine authentication is required for the IdM server to trust the machine and to accept IdM connections from the client software installed on that machine. After authenticating the client, the IdM server can respond to its requests.

**Additional resources**

-   [Installing a client using user credentials: interactive installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-client#installing-a-client-by-using-user-credentials-interactive-installation)
-   [Installing a client by using a one-time password: Interactive installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-client#installing-a-client-by-using-a-one-time-password-interactive-installation)

### [41.4. Enrollment and authentication of IdM hosts and users: comparison](#enrollment-and-authentication-of-idm-hosts-and-users-comparison) {#enrollment-and-authentication-of-idm-hosts-and-users-comparison .title}

When enrolling and authenticating in Identity Management (IdM), both users and hosts utilize similar authentication mechanisms, including Kerberos tickets and secure credentials.

-   The enrollment stage:

    -   An administrator can create an LDAP entry for both a user and a host before the user or host actually join IdM: for the stage user, the command is `ipa stageuser-add`{.literal}; for the host, the command is `ipa host-add`{.literal}.

-   A file containing a *key table* or, abbreviated, keytab, a symmetric key resembling to some extent a user password, is created during the execution of the `ipa-client-install`{.literal} command on the host, resulting in the host joining the IdM realm. Analogically, a user is asked to create a password when they activate their account, therefore joining the IdM realm.

-   While the user password is the default authentication method for a user, the keytab is the default authentication method for a host. The keytab is stored in a file on the host.

    +:-----------------------+:-----------------------------------------------------+:---------------------------------------------------------------------------+
    | Action                 | User                                                 | Host                                                                       |
    +------------------------+------------------------------------------------------+----------------------------------------------------------------------------+
    | Pre-enrollment         | \$ **ipa stageuser-add *user_name* \[\--password\]** | \$ **ipa host-add *host_name* \[\--random\]**                              |
    +------------------------+------------------------------------------------------+----------------------------------------------------------------------------+
    | Activating the account | \$ **ipa stageuser-activate *user_name***            | \$ **ipa-client install \[\--password\]** (must be run on the host itself) |
    +------------------------+------------------------------------------------------+----------------------------------------------------------------------------+

    : Table 41.1. User and host enrollment

    Show more

    -   The deployment stage:

-   When a user starts a new session, the user authenticates using a password; similarly, every time it is switched on, the host authenticates by presenting its keytab file. The System Security Services Daemon (SSSD) manages this process in the background.

-   If the authentication is successful, the user or host obtains a Kerberos ticket granting ticket (TGT).

-   The TGT is then used to obtain specific tickets for specific services.

    +:----------------------------------------+:---------------------------------------------------------+:---------------------------------------------------------+
    |                                         | User                                                     | Host                                                     |
    +-----------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
    | Default means of authentication         | **Password**                                             | **Keytabs**                                              |
    +-----------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
    | Starting a session (ordinary user)      | \$ **kinit *user_name***                                 | *\[switch on the host\]*                                 |
    +-----------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
    | The result of successful authentication | **TGT** to be used to obtain access to specific services | **TGT** to be used to obtain access to specific services |
    +-----------------------------------------+----------------------------------------------------------+----------------------------------------------------------+

    : Table 41.2. User and host session authentication

    Show more

TGTs and other Kerberos tickets are generated as part of the Kerberos services and policies defined by the server. The initial granting of a Kerberos ticket, the renewing of the Kerberos credentials, and even the destroying of the Kerberos session are all handled automatically by the IdM services.

Alternative authentication options for IdM hosts

:   Apart from keytabs, IdM supports two other types of machine authentication:

    -   SSH keys. The SSH public key for the host is created and uploaded to the host entry. From there, the System Security Services Daemon (SSSD) uses IdM as an identity provider and can work in conjunction with OpenSSH and other services to reference the public keys located centrally in IdM.
    -   Machine certificates. In this case, the machine uses an SSL certificate that is issued by the IdM server's certificate authority and then stored in IdM's Directory Server. The certificate is then sent to the machine to present when it authenticates to the server. On the client, certificates are managed by a service called certmonger.

**Additional resources**

-   [Certmonger overview](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/obtaining-an-idm-certificate-for-a-service-using-certmonger-assembly#certmonger-overview)

### [41.5. Host operations](#host-operations) {#host-operations .title}

Review prerequisites, contexts, and consequences for common host operations including enrollment, disabling, enabling, and re-enrollment. Understanding these operations helps you manage host lifecycle effectively in your Identity Management (IdM) domain.

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Action                            | What are the prerequisites of the action?                                                                                                                                                                                                                             | When does it make sense to run the command?                                                        | How is the action performed by a system administrator? What command(s) does he run?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+:==================================+:======================================================================================================================================================================================================================================================================+:===================================================================================================+:============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `Enrolling a client`{.literal}    | see [Preparing the system for Identity Management client installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/preparing-the-system-for-idm-server-installation) in *Installing Identity Management* | When you want the host to join the IdM realm.                                                      | Enrolling machines as clients in the IdM domain is a two-part process. A host entry is created for the client (and stored in the 389 Directory Server instance) when the `ipa host-add`{.literal} command is run, and then a keytab is created to provision the client. Both parts are performed automatically by the `ipa-client-install`{.literal} command. It is also possible to perform those steps separately; this allows for administrators to prepare machines and IdM in advance of actually configuring the clients. This allows more flexible deployment scenarios, including bulk deployments. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Disabling a client`{.literal}    | The host must have an entry in IdM. The host needs to have an active keytab.                                                                                                                                                                                          | When you want to remove the host from the IdM realm temporarily, perhaps for maintenance purposes. | `ipa host-disable host_name`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Enabling a client`{.literal}     | The host must have an entry in IdM.                                                                                                                                                                                                                                   | When you want the temporarily disabled host to become active again.                                | `ipa-getkeytab`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Re-enrolling a client`{.literal} | The host must have en entry in IdM.                                                                                                                                                                                                                                   | When the original host has been lost but you have installed a host with the same host name.        | `ipa-client-install --keytab`{.literal} or `ipa-client-install --force-join`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Un-enrolling a client`{.literal} | The host must have an entry in IdM.                                                                                                                                                                                                                                   | When you want to remove the host from the IdM realm permanently.                                   | `ipa-client-install --uninstall`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 41.3. Host operations part 1

Show more

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Action                            | On which machine can the administrator run the command(s)?                                                                                                                      | What happens when the action is performed? What are the consequences for the host's functioning in IdM? What limitations are introduced/removed?                                                                                                                                                                                                                                                                                                                                                                                                      |
+:==================================+:================================================================================================================================================================================+:======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `Enrolling a client`{.literal}    | In the case of a two-step enrollment: `ipa host-add`{.literal} can be run on any IdM client; the second step of `ipa-client-install`{.literal} must be run on the client itself | By default this configures SSSD to connect to an IdM server for authentication and authorization. Optionally one can instead configure the Pluggable Authentication Module (PAM) and the Name Switching Service (NSS) to work with an IdM server over Kerberos and LDAP.                                                                                                                                                                                                                                                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Disabling a client`{.literal}    | Any machine in IdM, even the host itself                                                                                                                                        | The host's Kerberos key and SSL certificate are invalidated, and all services running on the host are disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Enabling a client`{.literal}     | Any machine in IdM. If run on the disabled host, LDAP credentials need to be supplied.                                                                                          | The host's Kerberos key and the SSL certificate are made valid again, and all IdM services running on the host are re-enabled.                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Re-enrolling a client`{.literal} | The host to be re-enrolled. LDAP credentials need to be supplied.                                                                                                               | A new Kerberos key is generated for the host, replacing the previous one.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Un-enrolling a client`{.literal} | The host to be un-enrolled.                                                                                                                                                     | The command unconfigures IdM and attempts to return the machine to its previous state. Part of this process is to unenroll the host from the IdM server. Unenrollment consists of disabling the principal key on the IdM server. The machine principal in `/etc/krb5.keytab`{.literal} (`host/<fqdn>@REALM`{.literal}) is used to authenticate to the IdM server to unenroll itself. If this principal does not exist then unenrollment will fail and an administrator will need to disable the host principal (`ipa host-disable <fqdn>`{.literal}). |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 41.4. Host operations part 2

Show more

### [41.6. Host entry in IdM LDAP](#host-entry-in-idm-ldap) {#host-entry-in-idm-ldap .title}

Store comprehensive host information including services, access controls, and system details in Identity Management (IdM) LDAP host entries to centrally manage your infrastructure. Host entries enable policy enforcement and configuration management across your IdM domain.

An LDAP host entry contains all relevant information about the client within IdM:

-   Service entries associated with the host
-   The host and service principal
-   Access control rules
-   Machine information, such as its physical location and operating system

Note

Note that the IdM Web UI `Identity`{.literal} → `Hosts`{.literal} tab does not show all the information about a particular host stored in the IdM LDAP.

#### [41.6.1. Host entry configuration properties](#host_entry_configuration_properties) {#host-entry-configuration-properties .title}

A host entry can contain information about the host that is outside its system configuration, such as its physical location, MAC address, keys, and certificates.

This information can be set when the host entry is created if it is created manually. Alternatively, most of this information can be added to the host entry after the host is enrolled in the domain.

+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UI Field                      | Command-Line Option                     | Description                                                                                                                                                                                                                                                       |
+:==============================+:========================================+:==================================================================================================================================================================================================================================================================+
| Description                   | `--desc`{.literal}=*description*        | A description of the host.                                                                                                                                                                                                                                        |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Locality                      | `--locality`{.literal}=*locality*       | The geographic location of the host.                                                                                                                                                                                                                              |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Location                      | `--location`{.literal}=*location*       | The physical location of the host, such as its data center rack.                                                                                                                                                                                                  |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Platform                      | `--platform`{.literal}=*string*         | The host hardware or architecture.                                                                                                                                                                                                                                |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Operating system              | `--os`{.literal}=*string*               | The operating system and version for the host.                                                                                                                                                                                                                    |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MAC address                   | `--macaddress`{.literal}=*address*      | The MAC address for the host. This is a multi-valued attribute. The MAC address is used by the NIS plug-in to create a NIS `ethers`{.literal} map for the host.                                                                                                   |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SSH public keys               | `--sshpubkey`{.literal}=*string*        | The full SSH public key for the host. This is a multi-valued attribute, so multiple keys can be set.                                                                                                                                                              |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Principal name (not editable) | `--principalname`{.literal}=*principal* | The Kerberos principal name for the host. This defaults to the host name during the client installation, unless a different principal is explicitly set in the `-p`{.literal}. This can be changed using the command-line tools, but cannot be changed in the UI. |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Set One-Time Password         | `--password`{.literal}=*string*         | This option sets a password for the host which can be used in bulk enrollment.                                                                                                                                                                                    |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \-                            | `--random`{.literal}                    | This option generates a random password to be used in bulk enrollment.                                                                                                                                                                                            |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \-                            | `--certificate`{.literal}=*string*      | A certificate blob for the host.                                                                                                                                                                                                                                  |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \-                            | `--updatedns`{.literal}                 | This sets whether the host can dynamically update its DNS entries if its IP address changes.                                                                                                                                                                      |
+-------------------------------+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 41.5. Host configuration properties

Show more

### [41.7. Options for adding IdM host entries from the IdM CLI](#options-for-adding-idm-host-entries-from-the-idm-cli) {#options-for-adding-idm-host-entries-from-the-idm-cli .title}

Add host entries using the Identity Management (IdM) CLI to register systems in your domain and enable centralized authentication and access control. Host entries are required before systems can be enrolled as IdM clients.

There are a few different scenarios when adding a host to IdM:

-   At its most basic, specify only the client host name to add the client to the Kerberos realm and to create an entry in the IdM LDAP server:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-add client1.example.com
    ```

-   If the IdM server is configured to manage DNS, add the host to the DNS resource records using the `--ip-address`{.literal} option to create a host entry with static IP address.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-add --ip-address=192.168.166.31 client1.example.com
    ```

-   If the host to be added does not have a static IP address or if the IP address is not known at the time the client is configured, use the `--force`{.literal} option with the `ipa host-add`{.literal} command to create a host entry with DHCP.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-add --force client1.example.com
    ```

    For example, laptops may be preconfigured as IdM clients, but they do not have IP addresses at the time they are configured. Using `--force`{.literal} essentially creates a placeholder entry in the IdM DNS service. When the DNS service dynamically updates its records, the host's current IP address is detected and its DNS record is updated.

### [41.8. Deleting host entries from IdM CLI](#deleting-host-entries-from-idm-cli) {#deleting-host-entries-from-idm-cli .title}

Delete host entries using the Identity Management (IdM) CLI to remove systems from your domain when they are no longer needed or have been decommissioned. Deleting host entries removes the host's identity information and, optionally, its associated DNS records.

**Procedure**

-   Use the `host-del`{.literal} command to delete host records. If your IdM domain has integrated DNS, use the `--updatedns`{.literal} option to remove the associated records of any kind for the host from the DNS:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-del --updatedns client1.example.com
    ```

### [41.9. Disabling and Re-enabling Host Entries](#disabling-and-re-enabling-host-entries) {#disabling-and-re-enabling-host-entries .title}

Disable or re-enable host entries in Identity Management (IdM) to control whether hosts can actively participate in the Kerberos domain. Disabling a host preserves its configuration for later reactivation.

#### [41.9.1. Disabling Hosts](#disabling-hosts) {#disabling-hosts .title}

Disable host entries in Identity Management (IdM) to temporarily prevent access during maintenance without permanently deleting configurations. Disabling hosts preserves all settings and allows quick reactivation when needed.

Domain services, hosts, and users can access an active host. There can be situations when it is necessary to remove an active host temporarily, for maintenance reasons, for example. Deleting the host in such situations is not desired as it removes the host entry and all the associated configuration permanently. Instead, choose the option of disabling the host.

Disabling a host prevents domain users from accessing it without permanently removing it from the domain.

**Procedure**

-   Disable a host using the `host-disable`{.literal} command. Disabling a host kills the host's current, active keytabs. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit admin
    $ ipa host-disable client.example.com
    ```

    As a result of disabling a host, the host becomes unavailable to all IdM users, hosts and services.

    Important

    Disabling a host entry not only disables that host. It disables every configured service on that host as well.

#### [41.9.2. Re-enabling Hosts](#re-enabling-hosts) {#re-enabling-hosts .title}

Generate new keytabs for disabled Identity Management (IdM) hosts using `ipa-getkeytab`{.literal} to restore their domain membership. Re-enabling hosts allows them to authenticate and participate in the IdM domain again without reconfiguring the entire host entry.

When a host is disabled, its Kerberos keytabs are invalidated, removing the host from the IdM domain while leaving its configuration entry intact.

**Procedure**

-   To re-enable a host, use the `ipa-getkeytab`{.literal} command, adding:

    -   the `-s`{.literal} option to specify which IdM server to request the keytab from

    -   the `-p`{.literal} option to specify the principal name

    -   the `-k`{.literal} option to specify the file to which to save the keytab.

        For example, to request a new host keytab from `server.example.com`{.literal} for `client.example.com`{.literal}, and store the keytab in the `/etc/krb5.keytab`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        $  ipa-getkeytab -s server.example.com -p host/client.example.com -k /etc/krb5.keytab -D "cn=directory manager" -w password
        ```

        Note

        You can also use the administrator's credentials, specifying `-D "uid=admin,cn=users,cn=accounts,dc=example,dc=com"`{.literal}. It is important that the credentials correspond to a user allowed to create the keytab for the host.

    If the `ipa-getkeytab`{.literal} command is run on an active IdM client or server, then it can be run without any LDAP credentials (`-D`{.literal} and `-w`{.literal}) if the user has a TGT obtained using, for example, `kinit admin`{.literal}. To run the command directly on the disabled host, supply LDAP credentials to authenticate to the IdM server.

### [41.10. Delegating access to hosts and services](#delegating-access-to-hosts-and-services) {#delegating-access-to-hosts-and-services .title}

By delegating access to hosts and services within an Identity Management (IdM) domain, you can retrieve keytabs and certificates for another host or service.

Each host and service has a `managedby`{.literal} entry that lists what hosts and services can manage it. By default, a host can manage itself and all of its services. You can configure a host to manage other hosts, or services on other hosts within the IdM domain.

Note

When you delegate authority of a host to another host through a `managedby`{.literal} entry, it does not automatically grant management rights for all services on that host. You must perform each delegation independently.

**Host and service delegation**

#### [41.10.1. Delegating service management](#delegating-service-management) {#delegating-service-management .title}

Delegate permissions for one host to manage services on another host in Identity Management (IdM) to enable automated service credential management. Service delegation supports distributed administration and automation workflows.

When you delegate permissions to a host to manage another host, it does not automatically include permissions to manage its services. You must delegate service management independently.

**Procedure**

1.  Delegate the management of a service to a specific host by using the `service-add-host`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    ipa service-add-host principal --hosts=<hostname>
    ```

    You must specify the service principal using the `principal`{.literal} argument and the hosts with control using the `--hosts`{.literal} option.

    For example:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa service-add HTTP/web.example.com
    [root@server ~]# ipa service-add-host HTTP/web.example.com --hosts=client1.example.com
    ```

2.  Once the host is delegated authority, the host principal can be used to manage the service:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1 ~]# kinit -kt /etc/krb5.keytab host/client1.example.com
    [root@client1 ~]# ipa-getkeytab -s server.example.com -k /tmp/test.keytab -p HTTP/web.example.com
    Keytab successfully retrieved and stored in: /tmp/test.keytab
    ```

3.  To generate a certificate for the delegated service, create a certificate request on the host with the delegated authority:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1]# kinit -kt /etc/krb5.keytab host/client1.example.com
    [root@client1]# openssl req -newkey rsa:2048 -subj '/CN=web.example.com/O=EXAMPLE.COM' -keyout /etc/pki/tls/web.key -out /tmp/web.csr -nodes
    Generating a 2048 bit RSA private key
    .............................................................+++
    ............................................................................................+++
    Writing new private key to '/etc/pki/tls/private/web.key'
    ```

4.  Use the `cert-request`{.literal} utility to submit the certificate request and load the certification information:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1]# ipa cert-request --principal=HTTP/web.example.com web.csr
    Certificate: MIICETCCAXqgA...[snip]
    Subject: CN=web.example.com,O=EXAMPLE.COM
    Issuer: CN=EXAMPLE.COM Certificate Authority
    Not Before: Tue Feb 08 18:51:51 2011 UTC
    Not After: Mon Feb 08 18:51:51 2016 UTC
    Serial number: 1005
    ```

**Additional resources**

-   [Managing certificates for users, hosts, and services using the integrated IdM CA](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/managing-certificates-for-users-hosts-and-services-by-using-the-integrated-idm-ca)

#### [41.10.2. Delegating host management](#delegating-host-management) {#delegating-host-management .title}

Delegate authority for one host to manage another in Identity Management (IdM) to enable automated keytab retrieval and service management. Host delegation supports automation workflows and reduces manual administrative intervention.

Delegating host management authority creates a `managedby`{.literal} entry. After the `managedby`{.literal} entry is created, the managing host can retrieve a keytab for the host it manages.

**Procedure**

1.  Log in as the admin user:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit admin
    ```

2.  Add the `managedby`{.literal} entry. For example, this delegates authority over *client2* to *client1*:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa host-add-managedby client2.example.com --hosts=client1.example.com
    ```

3.  Obtain a ticket as the host *client1*:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1 ~]# kinit -kt /etc/krb5.keytab host/client1.example.com
    ```

4.  Retrieve a keytab for *client2*:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1 ~]# ipa-getkeytab -s server.example.com -k /tmp/client2.keytab -p host/client2.example.com
    Keytab successfully retrieved and stored in: /tmp/client2.keytab
    ```

#### [41.10.3. Accessing delegated services](#accessing-delegated-services) {#accessing-delegated-services .title}

When a client has delegated authority, it can obtain a keytab for the principal on the local machine for both services and hosts.

With the `kinit`{.literal} command, use the `-k`{.literal} option to load a keytab and the `-t`{.literal} option to specify the keytab. The principal format is `<principal>/hostname@REALM`{.literal}. For a service, replace `<principal>`{.literal} with the service name, for example HTTP. For a host, use `host`{.literal} as the principal.

**Procedure**

-   To access a host:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit -kt /etc/krb5.keytab host/ipa.example.com@EXAMPLE.COM
    ```

-   To access a service:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit -kt /etc/httpd/conf/krb5.keytab HTTP/ipa.example.com@EXAMPLE.COM
    ```

### [41.11. Additional resources](#managing-hosts-in-idm-cli_4111-additional-resources) {#additional-resources-17 .title}

-   [Re-enrolling an IdM client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/re-enrolling-an-idm-client)
-   [Renaming IdM client systems](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/renaming-idm-client-systems)

## [Chapter 42. Adding host entries from the Web UI](#adding-host-entries-from-the-web-ui) {#chapter-42.-adding-host-entries-from-the-web-ui .title}

Add host entries using the Identity Management (IdM) Web UI to register systems in your domain and enable centralized authentication and access control. Host entries are required before systems can be enrolled as IdM clients.

**Procedure**

1.  Open the **Identity** tab, and select the **Hosts** subtab.

2.  Click **Add** at the top of the hosts list.

3.  Enter the machine name and select the domain from the configured zones in the drop-down list. If the host has already been assigned a static IP address, then include that with the host entry so that the DNS entry is fully created.

    The `Class`{.literal} field has no specific purpose at the moment.

    **Add Host Wizard**

    DNS zones can be created in IdM.

    If the IdM server does not manage the DNS server, the zone can be entered manually in the menu area, like a regular text field.

    Note

    Select the **Force** checkbox if you want to skip checking whether the host is resolvable via DNS.

4.  Click the **Add and Edit** button to go directly to the expanded entry page and enter more attribute information. Information about the host hardware and physical location can be included with the host entry.

**Additional resources**

-   [Hosts in IdM](#hosts-in-idm "41.1. Hosts in IdM")
-   [Host enrollment](#host-enrollment "41.2. Host enrollment")
-   [User privileges required for host enrollment](#user-privileges-required-for-host-enrollment "41.3. User privileges required for host enrollment")
-   [Enrollment and authentication of IdM hosts and users: comparison](#enrollment-and-authentication-of-idm-hosts-and-users-comparison "41.4. Enrollment and authentication of IdM hosts and users: comparison")
-   [Host Operations](#host-operations "41.5. Host operations")
-   [Host entry in IdM LDAP](#host-entry-in-idm-ldap "41.6. Host entry in IdM LDAP")

## [Chapter 43. Managing hosts using Ansible playbooks](#managing-hosts-using-ansible-playbooks) {#chapter-43.-managing-hosts-using-ansible-playbooks .title}

Create and manage IdM host entries using Ansible to register machines in your domain with proper DNS information and credentials.

For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-host.md`{.literal} file on the control node.

### [43.1. Ensuring the presence of an IdM host entry with FQDN using Ansible playbooks](#ensuring-the-presence-of-an-idm-host-entry-with-fqdn-using-ansible-playbooks) {#ensuring-the-presence-of-an-idm-host-entry-with-fqdn-using-ansible-playbooks .title}

Ensure the presence of an IdM host entry that is only defined by its `fully-qualified domain name`{.literal} (FQDN) when the host has a dynamic IP address or DNS is managed externally.

Specifying the `FQDN`{.literal} name of the host is enough if at least one of the following conditions applies:

-   The IdM server is not configured to manage DNS.
-   The host does not have a static IP address or the IP address is not known at the time the host is configured. Adding a host defined only by an `FQDN`{.literal} essentially creates a placeholder entry in the IdM DNS service. For example, laptops may be preconfigured as IdM clients, but they do not have IP addresses at the time they are configured. When the DNS service dynamically updates its records, the host's current IP address is detected and its DNS record is updated.

Note

Without Ansible, host entries are created in IdM using the `ipa host-add`{.literal} command. The result of adding a host to IdM is the state of the host being present in IdM. Because of the Ansible reliance on idempotence, to add a host to IdM using Ansible, you must create a playbook in which you define the state of the host as present: **state: present**.

**Prerequisites**

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    cd ~/MyPlaybooks
    ```

2.  Create an **ensure-host-is-present.yml** Ansible playbook file with the `FQDN`{.literal} of the host whose presence in IdM you want to ensure. To simplify this step, you can copy and modify the example in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/host/add-host.yml`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Host present
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Host host01.idm.example.com present
        freeipa.ansible_freeipa.ipahost:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: host01.idm.example.com
          state: present
          force: true
    ```

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory ensure-host-is-present.yml
    ```

    Note

    The procedure results in a host entry in the IdM LDAP server being created but not in enrolling the host into the IdM Kerberos realm. For that, you must deploy the host as an IdM client. For details, see [Installing an Identity Management client using an Ansible playbook](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-identity-management-client-using-an-ansible-playbook).

**Verification**

1.  Log in to your IdM server as `admin`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh admin@server.idm.example.com
    Password:
    ```

2.  Enter the `ipa host-show`{.literal} command and specify the name of the host:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-show host01.idm.example.com
      Host name: host01.idm.example.com
      Principal name: host/host01.idm.example.com@IDM.EXAMPLE.COM
      Principal alias: host/host01.idm.example.com@IDM.EXAMPLE.COM
      Password: False
      Keytab: False
      Managed by: host01.idm.example.com
    ```

The output confirms that **host01.idm.example.com** exists in IdM.

### [43.2. Ensuring the presence of an IdM host entry with DNS information using Ansible playbooks](#ensuring-the-presence-of-an-idm-host-entry-with-dns-information-using-ansible-playbooks) {#ensuring-the-presence-of-an-idm-host-entry-with-dns-information-using-ansible-playbooks .title}

Run the Ansible playbook to add an IdM host entry with its `fully-qualified domain name`{.literal} (FQDN) and IP address.

**Prerequisites**

-   You know the IdM administrator password.

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    cd ~/MyPlaybooks
    ```

2.  Create an **ensure-host-is-present.yml** Ansible playbook file with the `fully-qualified domain name`{.literal} (FQDN) of the host whose presence in IdM you want to ensure. In addition, if the IdM server is configured to manage DNS and you know the IP address of the host, specify a value for the `ip_address`{.literal} parameter. The IP address is necessary for the host to exist in the DNS resource records. To simplify this step, you can copy and modify the example in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/host/host-present.yml`{.literal} file. You can also include other, additional information:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Host present
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure host01.idm.example.com is present
        freeipa.ansible_freeipa.ipahost:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: host01.idm.example.com
          description: Example host
          ip_address: 192.168.0.123
          locality: Lab
          ns_host_location: Lab
          ns_os_version: CentOS 7
          ns_hardware_platform: Lenovo T61
          mac_address:
          - "08:00:27:E3:B1:2D"
          - "52:54:00:BD:97:1E"
          state: present
    ```

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory ensure-host-is-present.yml
    ```

    Note

    The procedure results in a host entry in the IdM LDAP server being created but not in enrolling the host into the IdM Kerberos realm. For that, you must deploy the host as an IdM client. For details, see [Installing an Identity Management client using an Ansible playbook](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-identity-management-client-using-an-ansible-playbook).

**Verification**

1.  Log in to your IdM server as admin:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh admin@server.idm.example.com
    Password:
    ```

2.  Enter the `ipa host-show`{.literal} command and specify the name of the host:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-show host01.idm.example.com
      Host name: host01.idm.example.com
      Description: Example host
      Locality: Lab
      Location: Lab
      Platform: Lenovo T61
      Operating system: CentOS 7
      Principal name: host/host01.idm.example.com@IDM.EXAMPLE.COM
      Principal alias: host/host01.idm.example.com@IDM.EXAMPLE.COM
      MAC address: 08:00:27:E3:B1:2D, 52:54:00:BD:97:1E
      Password: False
      Keytab: False
      Managed by: host01.idm.example.com
    ```

The output confirms **host01.idm.example.com** exists in IdM.

### [43.3. Ensuring the presence of multiple IdM host entries with random passwords using Ansible playbooks](#ensuring-the-presence-of-multiple-idm-host-entries-with-random-passwords-using-ansible-playbooks) {#ensuring-the-presence-of-multiple-idm-host-entries-with-random-passwords-using-ansible-playbooks .title}

Create multiple host entries in a single Ansible task and generate random enrollment passwords for each host.

The `freeipa.ansible_freeipa.ipahost`{.literal} module allows the system administrator to ensure the presence or absence of multiple host entries in IdM using just one Ansible task. In the example below, multiple host entries are only defined by their `fully-qualified domain names`{.literal} (FQDNs). Running the Ansible playbook generates random passwords for the hosts.

**Prerequisites**

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    cd ~/MyPlaybooks
    ```

2.  Create an **ensure-hosts-are-present.yml** Ansible playbook file with the `fully-qualified domain name`{.literal} (FQDN) of the hosts whose presence in IdM you want to ensure. To make the Ansible playbook generate a random password for each host even when the host already exists in IdM and `update_password`{.literal} is limited to `on_create`{.literal}, add the `random: true`{.literal} and `force: true`{.literal} options. To simplify this step, you can copy and modify the example from the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-host.md`{.literal} Markdown file:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Ensure hosts with random password
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Hosts host01.idm.example.com and host02.idm.example.com present with random passwords
        freeipa.ansible_freeipa.ipahost:
          ipaadmin_password: "{{ ipaadmin_password }}"
          hosts:
          - name: host01.idm.example.com
            random: true
            force: true
          - name: host02.idm.example.com
            random: true
            force: true
        register: ipahost
    ```

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory ensure-hosts-are-present.yml
    [...]
    TASK [Hosts host01.idm.example.com and host02.idm.example.com present with random passwords]
    changed: [server.idm.example.com] => {"changed": true, "host": {"host01.idm.example.com": {"randompassword": "0HoIRvjUdH0Ycbf6uYdWTxH"}, "host02.idm.example.com": {"randompassword": "5VdLgrf3wvojmACdHC3uA3s"}}}
    ```

    Note

    To deploy the hosts as IdM clients using random, one-time passwords (OTPs), see [Authorization options for IdM client enrollment using an Ansible playbook](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-client-using-an-ansible-playbook#authorization-options-for-idm-client-enrollment-using-an-ansible-playbook) or [Installing a client by using a one-time password: Interactive installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-client#installing-a-client-by-using-a-one-time-password-interactive-installation).

**Verification**

1.  Log in to your IdM server as admin:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh admin@server.idm.example.com
    Password:
    ```

2.  Enter the `ipa host-show`{.literal} command and specify the name of one of the hosts:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-show host01.idm.example.com
      Host name: host01.idm.example.com
      Password: True
      Keytab: False
      Managed by: host01.idm.example.com
    ```

The output confirms **host01.idm.example.com** exists in IdM with a random password.

### [43.4. Ensuring the presence of an IdM host entry with multiple IP addresses using Ansible playbooks](#ensuring-the-presence-of-an-idm-host-entry-with-multiple-ip-addresses-using-ansible-playbooks) {#ensuring-the-presence-of-an-idm-host-entry-with-multiple-ip-addresses-using-ansible-playbooks .title}

Run the Ansible playbook to create an Identity Management (IdM) host entry with multiple IPv4 and IPv6 addresses when the host has multiple network interfaces.

Note

In contrast to the `ipa host`{.literal} utility, the Ansible `freeipa.ansible_freeipa.ipahost`{.literal} module can ensure the presence or absence of several IPv4 and IPv6 addresses for a host. The `ipa host-mod`{.literal} command cannot handle IP addresses.

**Prerequisites**

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    cd ~/MyPlaybooks
    ```

2.  Create an **ensure-host-with-multiple-IP-addreses-is-present.yml** Ansible playbook file. Specify, as the `name`{.literal} of the `freeipa.ansible_freeipa.ipahost`{.literal} variable, the `fully-qualified domain name`{.literal} (FQDN) of the host whose presence in IdM you want to ensure. Specify each of the multiple IPv4 and IPv6 `ip_address`{.literal} values on a separate line by using the ***ip_address*** syntax. To simplify this step, you can copy and modify the example in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/host/host-member-ipaddresses-present.yml`{.literal} file. You can also include additional information:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Host member IP addresses present
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure host101.example.com IP addresses present
        freeipa.ansible_freeipa.ipahost:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: host01.idm.example.com
          ip_address:
          - 192.168.0.123
          - fe80::20c:29ff:fe02:a1b3
          - 192.168.0.124
          - fe80::20c:29ff:fe02:a1b4
          force: true
    ```

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory ensure-host-with-multiple-IP-addreses-is-present.yml
    ```

    Note

    The procedure creates a host entry in the IdM LDAP server but does not enroll the host into the IdM Kerberos realm. For that, you must deploy the host as an IdM client. For details, see [Installing an Identity Management client using an Ansible playbook](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-identity-management-client-using-an-ansible-playbook).

**Verification**

1.  Log in to your IdM server as admin:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh admin@server.idm.example.com
    Password:
    ```

2.  Enter the `ipa host-show`{.literal} command and specify the name of the host:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-show host01.idm.example.com
      Principal name: host/host01.idm.example.com@IDM.EXAMPLE.COM
      Principal alias: host/host01.idm.example.com@IDM.EXAMPLE.COM
      Password: False
      Keytab: False
      Managed by: host01.idm.example.com
    ```

    The output confirms that **host01.idm.example.com** exists in IdM.

3.  To verify that the multiple IP addresses of the host exist in the IdM DNS records, enter the `ipa dnsrecord-show`{.literal} command and specify the following information:

    -   The name of the IdM domain

    -   The name of the host

        ``` {.language-plaintext tabindex="-1"}
        $ ipa dnsrecord-show idm.example.com host01
        [...]
          Record name: host01
          A record: 192.168.0.123, 192.168.0.124
          AAAA record: fe80::20c:29ff:fe02:a1b3, fe80::20c:29ff:fe02:a1b4
        ```

    The output confirms that all the IPv4 and IPv6 addresses specified in the playbook are correctly associated with the **host01.idm.example.com** host entry.

### [43.5. Ensuring the absence of an IdM host entry using Ansible playbooks](#ensuring-the-absence-of-an-idm-host-entry-using-ansible-playbooks) {#ensuring-the-absence-of-an-idm-host-entry-using-ansible-playbooks .title}

Remove an IdM host entry using Ansible when decommissioning systems or cleaning up stale entries from your domain.

Follow this procedure to ensure the absence of host entries in Identity Management (IdM) using Ansible playbooks.

**Prerequisites**

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Create an Ansible playbook file with the `fully-qualified domain name`{.literal} (FQDN) of the host whose absence from IdM you want to ensure. If your IdM domain has integrated DNS, use the `updatedns: true`{.literal} option to remove the associated records of any kind for the host from the DNS.

    To simplify this step, you can copy and modify the example in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/host/delete-host.yml`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Host absent
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Host host01.idm.example.com absent
        freeipa.ansible_freeipa.ipahost:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: host01.idm.example.com
          updatedns: true
          state: absent
    ```

2.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i path_to_inventory_directory/inventory.file path_to_playbooks_directory/ensure-host-absent.yml
    ```

    Note

    The procedure results in:

    -   The host not being present in the IdM Kerberos realm.
    -   The host entry not being present in the IdM LDAP server.

    To remove the specific IdM configuration of system services, such as System Security Services Daemon (SSSD), from the client host itself, you must run the `ipa-client-install --uninstall`{.literal} command on the client. For details, see [Uninstalling an IdM client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/uninstalling-an-idm-client).

**Verification**

1.  Log into `ipaserver`{.literal} as admin:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh admin@server.idm.example.com
    Password:
    [admin@server /]$
    ```

2.  Display information about *host01.idm.example.com*:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-show host01.idm.example.com
    ipa: ERROR: host01.idm.example.com: host not found
    ```

The output confirms that the host does not exist in IdM.

### [43.6. Additional resources](#managing-hosts-using-ansible-playbooks_436-additional-resources) {#additional-resources-18 .title}

-   [Managing hosts in IdM CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-hosts-in-idm-cli)

## [Chapter 44. Managing host groups using the IdM CLI](#managing-host-groups-using-the-idm-cli) {#chapter-44.-managing-host-groups-using-the-idm-cli .title}

Manage host groups and their members in Identity Management (IdM) using the CLI to organize hosts for easier policy management. Host groups simplify the application of access control rules and other policies to multiple hosts.

### [44.1. Host groups in IdM](#host-groups-in-idm) {#host-groups-in-idm .title}

Understand how IdM host groups centralize control over access policies and other management tasks for sets of hosts with common characteristics. For example, you can define host groups based on company departments, physical locations, or access control requirements.

A host group in IdM can include:

-   IdM servers and clients

-   Other IdM host groups

    Host groups created by default
    :   By default, the IdM server creates the host group `ipaservers`{.literal} for all IdM server hosts.

    Direct and indirect group members
    :   Group attributes in IdM apply to both direct and indirect members: when host group B is a member of host group A, all members of host group B are considered indirect members of host group A.

### [44.2. Viewing IdM host groups using the CLI](#viewing-idm-host-groups-using-the-cli) {#viewing-idm-host-groups-using-the-cli .title}

View host groups and their details by using the Identity Management (IdM) CLI to understand how hosts are organized and confirm group configurations.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

1.  Find all host groups using the `ipa hostgroup-find`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hostgroup-find
    -------------------
    1 hostgroup matched
    -------------------
      Host-group: ipaservers
      Description: IPA server hosts
    ----------------------------
    Number of entries returned 1
    ----------------------------
    ```

2.  To display all attributes of a host group, add the `--all`{.literal} option. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hostgroup-find --all
    -------------------
    1 hostgroup matched
    -------------------
      dn: cn=ipaservers,cn=hostgroups,cn=accounts,dc=idm,dc=local
      Host-group: ipaservers
      Description: IPA server hosts
      Member hosts: xxx.xxx.xxx.xxx
      ipauniqueid: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
      objectclass: top, groupOfNames, nestedGroup, ipaobject, ipahostgroup
    ----------------------------
    Number of entries returned 1
    ----------------------------
    ```

### [44.3. Creating IdM host groups using the CLI](#creating-idm-host-groups-using-the-cli) {#creating-idm-host-groups-using-the-cli .title}

Create host groups using the Identity Management (IdM) CLI to organize and manage multiple hosts as a single unit. Host groups simplify policy application and administrative tasks across your infrastructure.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

-   Add a host group using the `ipa hostgroup-add`{.literal} command.

    For example, to create an IdM host group named *group_name* and give it a description:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hostgroup-add --desc 'My new host group' group_name
    ---------------------
    Added hostgroup "group_name"
    ---------------------
      Host-group: group_name
      Description: My new host group
    ---------------------
    ```

### [44.4. Deleting IdM host groups using the CLI](#deleting-idm-host-groups-using-the-cli) {#deleting-idm-host-groups-using-the-cli .title}

You can delete host groups using the Identity Management (IdM) CLI. Deleting a host group does not delete the group members from IdM.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).

**Procedure**

-   Delete a host group using the `ipa hostgroup-del`{.literal} command.

    For example, to delete the IdM host group named *group_name*:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hostgroup-del group_name
    --------------------------
    Deleted hostgroup "group_name"
    --------------------------
    ```

### [44.5. Adding IdM host group members using the CLI](#adding-idm-host-group-members-using-the-cli) {#adding-idm-host-group-members-using-the-cli .title}

Add hosts to host groups using the Identity Management (IdM) CLI to apply policies and access controls to multiple systems collectively.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   Optional: Use the `ipa hostgroup-find`{.literal} command to find hosts and host groups.

**Procedure**

-   To add a member to a host group, use the `ipa hostgroup-add-member`{.literal} command and provide the relevant information. You can specify the type of member to add using these options:

    -   Use the `--hosts`{.literal} option to add one or more hosts to an IdM host group.

        For example, to add the host named *example_member* to the group named *group_name*:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa hostgroup-add-member group_name --hosts example_member
        Host-group: group_name
        Description: My host group
        Member hosts: example_member
        -------------------------
        Number of members added 1
        -------------------------
        ```

    -   Use the `--hostgroups`{.literal} option to add one or more host groups to an IdM host group.

        For example, to add the host group named *nested_group* to the group named *group_name*:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa hostgroup-add-member group_name --hostgroups nested_group
        Host-group: group_name
        Description: My host group
        Member host-groups: nested_group
        -------------------------
        Number of members added 1
        -------------------------
        ```

    -   You can add multiple hosts and multiple host groups to an IdM host group in one single command using the following syntax:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa hostgroup-add-member group_name --hosts={host1,host2} --hostgroups={group1,group2}
        ```

    Important

    When adding a host group as a member of another host group, do not create recursive groups. For example, if Group A is a member of Group B, do not add Group B as a member of Group A. Recursive groups can cause unpredictable behavior.

### [44.6. Removing IdM host group members using the CLI](#removing-idm-host-group-members-using-the-cli) {#removing-idm-host-group-members-using-the-cli .title}

Remove hosts or nested host groups from an Identity Management (IdM) host group by using the CLI to revoke their membership-based policies and access.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   *Optional*. Use the `ipa hostgroup-find`{.literal} command to confirm that the group includes the member you want to remove.

**Procedure**

-   To remove a host group member, use the `ipa hostgroup-remove-member`{.literal} command and provide the relevant information. You can specify the type of member to remove using these options:

    -   Use the `--hosts`{.literal} option to remove one or more hosts from an IdM host group.

        For example, to remove the host named *example_member* from the group named *group_name*:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa hostgroup-remove-member group_name --hosts example_member
        Host-group: group_name
        Description: My host group
        -------------------------
        Number of members removed 1
        -------------------------
        ```

    -   Use the `--hostgroups`{.literal} option to remove one or more host groups from an IdM host group.

        For example, to remove the host group named *nested_group* from the group named *group_name*:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa hostgroup-remove-member group_name --hostgroups example_member
        Host-group: group_name
        Description: My host group
        -------------------------
        Number of members removed 1
        -------------------------
        ```

        Note

        Removing a group does not delete the group members from IdM.

    -   You can remove multiple hosts and multiple host groups from an IdM host group in one single command using the following syntax:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa hostgroup-remove-member group_name --hosts={host1,host2} --hostgroups={group1,group2}
        ```

### [44.7. Adding IdM host group member managers using the CLI](#adding-idm-host-group-member-managers-using-the-cli) {#adding-idm-host-group-member-managers-using-the-cli .title}

Designate hosts or host groups as member managers using the Identity Management (IdM) CLI to delegate host group membership management. Member managers can add or remove hosts from groups without having full administrative privileges.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   You must have the name of the host or host group you are adding as member managers and the name of the host group you want them to manage.

**Procedure**

1.  Optional: Use the `ipa hostgroup-find`{.literal} command to find hosts and host groups.

2.  To add a member manager to a host group, use the `ipa hostgroup-add-member-manager`{.literal}.

    For example, to add the user named *example_member* as a member manager to the group named *group_name*:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hostgroup-add-member-manager group_name --user example_member
    Host-group: group_name
    Member hosts: server.idm.example.com
    Member host-groups: project_admins
    Member of netgroups: group_name
    Membership managed by users: example_member
    -------------------------
    Number of members added 1
    -------------------------
    ```

3.  Use the `--groups`{.literal} option to add one or more host groups as a member manager to an IdM host group.

    For example, to add the host group named *admin_group* as a member manager to the group named *group_name*:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hostgroup-add-member-manager group_name --groups admin_group
    Host-group: group_name
    Member hosts: server.idm.example.com
    Member host-groups: project_admins
    Member of netgroups: group_name
    Membership managed by groups: admin_group
    Membership managed by users: example_member
    -------------------------
    Number of members added 1
    -------------------------
    ```

    Note

    After you add a member manager to a host group, the update may take some time to spread to all clients in your Identity Management environment.

**Verification**

-   Using the `ipa group-show`{.literal} command to verify the host user and host group were added as member managers.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hostgroup-show group_name
    Host-group: group_name
    Member hosts: server.idm.example.com
    Member host-groups: project_admins
    Membership managed by groups: admin_group
    Membership managed by users: example_member
    ```

### [44.8. Removing IdM host group member managers using the CLI](#removing-idm-host-group-member-managers-using-the-cli) {#removing-idm-host-group-member-managers-using-the-cli .title}

Remove hosts or host groups as member managers from an Identity Management (IdM) host group by using the CLI to revoke their ability to manage group membership. Member managers can add and remove group members but cannot change the attributes of the host group.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   An active Kerberos ticket. For details, see [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line#using-kinit-to-log-in-to-idm-manually_login-cli-krb).
-   You must have the name of the existing member manager host group you are removing and the name of the host group they are managing.

**Procedure**

1.  Optional: Use the `ipa hostgroup-find`{.literal} command to find hosts and host groups.

2.  To remove a member manager from a host group, use the `ipa hostgroup-remove-member-manager`{.literal} command.

    For example, to remove the user named *example_member* as a member manager from the group named *group_name*:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hostgroup-remove-member-manager group_name --user example_member
    Host-group: group_name
    Member hosts: server.idm.example.com
    Member host-groups: project_admins
    Member of netgroups: group_name
    Membership managed by groups: nested_group
    ---------------------------
    Number of members removed 1
    ---------------------------
    ```

3.  Use the `--groups`{.literal} option to remove one or more host groups as a member manager from an IdM host group.

    For example, to remove the host group named *nested_group* as a member manager from the group named *group_name*:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hostgroup-remove-member-manager group_name --groups nested_group
    Host-group: group_name
    Member hosts: server.idm.example.com
    Member host-groups: project_admins
    Member of netgroups: group_name
    ---------------------------
    Number of members removed 1
    ---------------------------
    ```

    Note

    After you remove a member manager from a host group, the update may take some time to spread to all clients in your Identity Management environment.

**Verification**

-   Use the `ipa group-show`{.literal} command to verify that the host user and host group were removed as member managers.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hostgroup-show group_name
    Host-group: group_name
    Member hosts: server.idm.example.com
    Member host-groups: project_admins
    ```

### [44.9. Additional resources](#managing-host-groups-using-the-idm-cli_449-additional-resources) {#additional-resources-19 .title}

-   [Managing host groups using Ansible playbooks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/managing-host-groups-using-ansible-playbooks)

## [Chapter 45. Managing host groups using the IdM Web UI](#managing-host-groups-using-the-idm-web-ui) {#chapter-45.-managing-host-groups-using-the-idm-web-ui .title}

Manage host groups and their members in Identity Management (IdM) using the Web UI to organize hosts for easier policy management. Host groups simplify the application of access control rules and other policies to multiple hosts.

### [45.1. Viewing host groups in the IdM Web UI](#viewing-host-groups-in-the-idm-web-ui) {#viewing-host-groups-in-the-idm-web-ui .title}

View host groups and their members by using the Identity Management (IdM) Web UI to understand how hosts are organized and which hosts or nested groups belong to each host group.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  Click **Identity\>Groups**, and select the **Host Groups** tab. The **Host Groups** page lists the existing host groups and their descriptions. You can also search for a specific host group.
2.  Click on a group in the list to display the hosts that belong to this group. You can limit results to direct or indirect members.
3.  Select the **Host Groups** tab to display the host groups that belong to this group (nested host groups). You can limit results to direct or indirect members.

### [45.2. Creating host groups in the IdM Web UI](#creating-host-groups-in-the-idm-web-ui) {#creating-host-groups-in-the-idm-web-ui .title}

Create host groups using the Identity Management (IdM) WebUI to organize and manage multiple hosts as a single unit. Host groups simplify policy application and administrative tasks across your infrastructure.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  Click **Identity → Groups**, and select the **Host Groups** tab.
2.  Click **Add**. The **Add host group** dialog appears.
3.  Provide the information about the group: name (required) and description (optional).
4.  Click **Add** to confirm.

### [45.3. Deleting host groups in the IdM Web UI](#deleting-host-groups-in-the-idm-web-ui) {#deleting-host-groups-in-the-idm-web-ui .title}

You can delete host groups using the Identity Management (IdM) WebUI. Deleting a host group does not delete the group members from IdM.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  Click **Identity\>Groups** and select the **Host Groups** tab.
2.  Select the IdM host group to remove, and click **Delete**. A confirmation dialog opens.
3.  Click **Delete** to confirm

### [45.4. Adding host group members in the IdM Web UI](#adding-host-group-members-in-the-idm-web-ui) {#adding-host-group-members-in-the-idm-web-ui .title}

Add hosts to host groups using the Identity Management (IdM) Web UI to apply policies and access controls to multiple systems collectively. Host groups simplify administration by managing related systems as a single unit.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  Click **Identity → Groups** and select the **Host Groups** tab.
2.  Click the name of the group to which you want to add members.
3.  Click the tab **Hosts** or **Host groups** depending on the type of members you want to add. The corresponding dialog appears.
4.  Select the hosts or host groups to add, and click the \> arrow button to move them to the **Prospective** column.
5.  Click **Add** to confirm.

### [45.5. Removing host group members in the IdM Web UI](#removing-host-group-members-in-the-idm-web-ui) {#removing-host-group-members-in-the-idm-web-ui .title}

Remove hosts or nested host groups from an Identity Management (IdM) host group in the IdM Web UI to revoke their membership-based policies and access.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  Click **Identity → Groups** and select the **Host Groups** tab.
2.  Click the name of the group from which you want to remove members.
3.  Click the tab **Hosts** or **Host groups** depending on the type of members you want to remove.
4.  Select the checkbox next to the member you want to remove.
5.  Click **Delete**. A confirmation dialog opens.
6.  Click **Delete** to confirm. The selected members are deleted.

### [45.6. Adding IdM host group member managers using the Web UI](#adding-idm-host-group-member-managers-using-the-web-ui) {#adding-idm-host-group-member-managers-using-the-web-ui .title}

Designate users or user groups as member managers using the Identity Management (IdM) Web UI to delegate host group membership management. Member managers can add or remove hosts from groups without having full administrative privileges.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).
-   You must have the name of the host group you are adding as member managers and the name of the host group you want them to manage.

**Procedure**

1.  Click **Identity\>Groups** and select the **Host Groups** tab.

2.  Click the name of the group to which you want to add member managers.

3.  Click the member managers tab **User Groups** or **Users** depending on the type of member managers you want to add. The corresponding dialog appears.

4.  Click **Add**.

5.  Select the users or user groups to add, and click the \> arrow button to move them to the **Prospective** column.

6.  Click **Add** to confirm.

    Note

    After you add a member manager to a host group, the update may take some time to spread to all clients in your Identity Management environment.

**Verification**

-   On the Host Group dialog, verify the user group or user has been added to the member managers list of groups or users.

### [45.7. Removing IdM host group member managers using the Web UI](#removing-idm-host-group-member-managers-using-the-web-ui) {#removing-idm-host-group-member-managers-using-the-web-ui .title}

Remove users or user groups as host group member managers in Identity Management (IdM) by using the IdM Web UI to revoke their ability to manage group membership. Member managers can add and remove group members but cannot change the attributes of the host group.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.
-   You are logged-in to the IdM Web UI. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).
-   You must have the name of the existing member manager host group you are removing and the name of the host group they are managing.

**Procedure**

1.  Click **Identity\>Groups** and select the **Host Groups** tab.

2.  Click the name of the group from which you want to remove member managers.

3.  Click the member managers tab **User Groups** or **Users** depending on the type of member managers you want to remove. The corresponding dialog appears.

4.  Select the user or user groups to remove and click **Delete**.

5.  Click **Delete** to confirm.

    Note

    After you remove a member manager from a host group, the update may take some time to spread to all clients in your Identity Management environment.

**Verification**

-   On the Host Group dialog, verify the user group or user has been removed from the member managers list of groups or users.

### [45.8. Additional resources](#managing-host-groups-using-the-idm-web-ui_458-additional-resources) {#additional-resources-20 .title}

-   [Host groups in IdM](#host-groups-in-idm "44.1. Host groups in IdM")

## [Chapter 46. Configuring host-based access control rules](#configuring-host-based-access-control-rules) {#chapter-46.-configuring-host-based-access-control-rules .title}

Use host-based access control (HBAC) rules to manage which users or user groups can access specified hosts or host groups in your Identity Management (IdM) domain. HBAC rules help you enforce granular access policies by restricting access based on users, hosts, and services.

You can use HBAC rules to achieve the following goals:

-   Limit access to a specified system in your domain to members of a specific user group.
-   Allow only a specific service to be used to access the systems in your domain.

By default, IdM is configured with a default HBAC rule named `allow_all`{.literal}, which allows universal access to every host for every user through every relevant service in the entire IdM domain.

You can fine-tune access to different hosts by replacing the default `allow_all`{.literal} rule with your own set of HBAC rules. For centralized and simplified access control management, you can apply HBAC rules to user groups, host groups, or service groups instead of individual users, hosts, or services.

### [46.1. Configuring HBAC rules in an IdM domain using the WebUI](#configuring-hbac-rules-in-an-idm-domain-using-the-webui) {#configuring-hbac-rules-in-an-idm-domain-using-the-webui .title}

Configure host-based access control (HBAC) rules in your Identity Management (IdM) domain using the WebUI to control which users can access specific hosts and services. Replace the default `allow_all`{.literal} rule with custom HBAC rules to enforce granular access policies.

To configure your domain for host-based access control, complete the following steps:

1.  Create HBAC rules in the IdM WebUI.
2.  Test the new HBAC rules.
3.  Disable the default `allow_all`{.literal} HBAC rule\].

Note

Do not disable the `allow_all`{.literal} rule before creating your custom HBAC rules as if you do so, no users will be able to access any hosts.

#### [46.1.1. Creating HBAC rules in the IdM WebUI](#creating-hbac-rules-in-the-idm-webui) {#creating-hbac-rules-in-the-idm-webui .title}

Create host-based access control (HBAC) rules using the Identity Management (IdM) WebUI to define which users can access specific hosts and services. HBAC rules enforce granular access policies and strengthen your security posture.

For example, this procedure shows you how to grant a single user, *sysadmin*, access to all systems in the domain using any service.

Note

IdM stores the primary group of a user as a numerical value of the `gidNumber`{.literal} attribute instead of a link to an IdM group object. For this reason, an HBAC rule can only reference a user's supplementary groups and not its primary group.

**Prerequisites**

-   User *sysadmin* exists in IdM.

**Procedure**

1.  Select **Policy\>Host-Based Access Control\>HBAC Rules**.

2.  Click Add to start adding a new rule.

3.  Enter a name for the rule, and click Add and Edit to open the HBAC rule configuration page.

4.  In the **Who** area, select **Specified Users and Groups**. Then click Add to add the users or groups.

5.  Select the *sysadmin* user from the list of the **Available** users and click \> to move to the list of **Prospective** users and click Add.

6.  In the **Accessing** area, select **Any Host** to apply the HBAC rule to all hosts.

7.  In the **Via Service** area, select **Any Service** to apply the HBAC rule to all services.

    Note

    Only the most common services and service groups are configured for HBAC rules by default.

    -   To display the list of services that are currently available, select **Policy\>Host-Based Access Control\>HBAC Services**.
    -   To display the list of service groups that are currently available, select **Policy\>Host-Based Access Control\>HBAC Service Groups**.

    To add more services and service groups, see [Adding HBAC Service Entries for Custom HBAC Services](#adding-hbac-service-entries-for-custom-hbac-services "46.3. Adding HBAC service entries for custom HBAC services") and [Adding HBAC Service Groups](#adding-hbac-service-groups "46.4. Adding HBAC service groups").

8.  To save any changes you make on the **HBAC rule** configuration page, click Save at the top of the page.

#### [46.1.2. Testing HBAC rules in the IdM WebUI](#testing-hbac-rules-in-the-idm-webui) {#testing-hbac-rules-in-the-idm-webui .title}

Test your Identity Management (IdM) HBAC rule configuration in the IdM WebUI using simulated scenarios to discover misconfigurations and security risks before deploying rules in production.

Important

Always test custom HBAC rules before you start using them in production.

Note that IdM does not test the effect of HBAC rules on trusted Active Directory (AD) users. Because the IdM LDAP directory does not store the AD data, IdM cannot resolve group membership of AD users when simulating HBAC scenarios.

**Procedure**

1.  Select **Policy\>Host-Based Access Control\>HBAC Test**.

2.  On the **Who** window, specify the user under whose identity you want to perform the test, and click Next.

3.  On the **Accessing** window, specify the host that the user will attempt to access, and click Next.

4.  On the **Via Service** window, specify the service that the user will attempt to use, and click Next.

5.  On the **Rules** window, select the HBAC rules you want to test, and click Next. If you do not select any rule, all rules are tested.

    Select **Include Enabled** to run the test on all rules whose status is **Enabled**. Select **Include Disabled** to run the test on all rules whose status is **Disabled**. To view and change the status of HBAC rules, select **Policy\>Host-Based Access Control\>HBAC Rules**.

    Important

    If the test runs on multiple rules, it passes successfully if at least one of the selected rules allows access.

6.  On the **Run Test** window, click Run Test.

7.  Review the test results:

    -   If you see **ACCESS DENIED**, the user is not granted access in the test.
    -   If you see **ACCESS GRANTED**, the user is able to access the host successfully.

    By default, IdM lists all the tested HBAC rules when displaying the test results.

    -   Select **Matched** to display the rules that allowed successful access.
    -   Select **Unmatched** to display the rules that prevented access.

#### [46.1.3. Disabling HBAC rules in the IdM WebUI](#disabling-hbac-rules-in-the-idm-webui) {#disabling-hbac-rules-in-the-idm-webui .title}

Disable HBAC rules using the Identity Management (IdM) WebUI to temporarily deactivate access policies without permanent deletion. Disabling rules enables testing and troubleshooting while preserving rule configurations.

Note

Disabling HBAC rules is useful when you are configuring custom HBAC rules for the first time. To ensure that your new configuration is not overridden by the default `allow_all`{.literal} HBAC rule, you must disable `allow_all`{.literal}.

**Procedure**

1.  Select **Policy\>Host-Based Access Control\>HBAC Rules**.
2.  Select the HBAC rule you want to disable.
3.  Click Disable.
4.  Click OK to confirm you want to disable the selected HBAC rule.

### [46.2. Configuring HBAC rules in an IdM domain using the CLI](#configuring-hbac-rules-in-an-idm-domain-using-the-cli) {#configuring-hbac-rules-in-an-idm-domain-using-the-cli .title}

Configure host-based access control (HBAC) rules in your Identity Management (IdM) domain using the CLI to control which users can access specific hosts and services. Replace the default `allow_all`{.literal} rule with custom HBAC rules to enforce granular access policies.

To configure your domain for host-based access control, complete the following steps:

1.  Create HBAC rules in the IdM CLI.
2.  Test the new HBAC rules.
3.  Disable the default `allow_all`{.literal} HBAC rule.

Note

Do not disable the `allow_all`{.literal} rule before creating your custom HBAC rules. If you disable it before creating your custom rules, access to all hosts for all users will be denied.

#### [46.2.1. Creating HBAC rules in the IdM CLI](#creating-hbac-rules-in-the-idm-cli) {#creating-hbac-rules-in-the-idm-cli .title}

Create host-based access control (HBAC) rules using the Identity Management (IdM) CLI to define which users can access specific hosts and services. HBAC rules enforce granular access policies and strengthen your security posture.

For example, this procedure shows you how to grant a single user, *sysadmin*, access to all systems in the domain using any service.

Note

IdM stores the primary group of a user as a numerical value of the `gidNumber`{.literal} attribute instead of a link to an IdM group object. For this reason, an HBAC rule can only reference a user's supplementary groups and not its primary group.

**Prerequisites**

-   User *sysadmin* exists in IdM.

**Procedure**

1.  Use the `ipa hbacrule-add`{.literal} command to add the rule.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hbacrule-add
    Rule name: rule_name
    ---------------------------
    Added HBAC rule "rule_name"
    ---------------------------
      Rule name: rule_name
      Enabled: TRUE
    ```

2.  To apply the HBAC rule to the *sysadmin* user only, use the `ipa hbacrule-add-user`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hbacrule-add-user --users=sysadmin
    Rule name: rule_name
      Rule name: rule_name
      Enabled: True
      Users: sysadmin
    -------------------------
    Number of members added 1
    -------------------------
    ```

    Note

    To apply a HBAC rule to all users, use the `ipa hbacrule-mod`{.literal} command and specify the all user category `--usercat=all`{.literal}. Note that if the HBAC rule is associated with individual users or groups, `ipa hbacrule-mod --usercat=all`{.literal} fails. In this situation, remove the users and groups using the `ipa hbacrule-remove-user`{.literal} command.

3.  Specify the target hosts. To apply the HBAC rule to all hosts, use the `ipa hbacrule-mod`{.literal} command and specify the all host category:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hbacrule-mod rule_name --hostcat=all
    ------------------------------
    Modified HBAC rule "rule_name"
    ------------------------------
      Rule name: rule_name
      Host category: all
      Enabled: TRUE
      Users: sysadmin
    ```

    Note

    If the HBAC rule is associated with individual hosts or groups, `ipa hbacrule-mod --hostcat=all`{.literal} fails. In this situation, remove the hosts and groups using the `ipa hbacrule-remove-host`{.literal} command.

4.  Specify the target HBAC services. To apply the HBAC rule to all services, use the `ipa hbacrule-mod`{.literal} command and specify the all service category:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hbacrule-mod rule_name --servicecat=all
    ------------------------------
    Modified HBAC rule "rule_name"
    ------------------------------
      Rule name: rule_name
      Host category: all
      Service category: all
      Enabled: True
      Users: sysadmin
    ```

    Note

    If the HBAC rule is associated with individual services or groups, `ipa hbacrule-mod --servicecat=all`{.literal} fails. In this situation, remove the services and groups using the `ipa hbacrule-remove-service`{.literal} command.

**Verification**

-   Verify that the HBAC rule has been added correctly.

    a.  Use the `ipa hbacrule-find`{.literal} command to verify that the HBAC rule exists in IdM.
    b.  Use the `ipa hbacrule-show`{.literal} command to verify the properties of the HBAC rule.

**Additional resources**

-   [Adding HBAC service entries for custom HBAC services](#adding-hbac-service-entries-for-custom-hbac-services "46.3. Adding HBAC service entries for custom HBAC services")
-   [Adding HBAC service groups](#adding-hbac-service-groups "46.4. Adding HBAC service groups")

#### [46.2.2. Testing HBAC rules in the IdM CLI](#testing-hbac-rules-in-the-idm-cli) {#testing-hbac-rules-in-the-idm-cli .title}

Test your Identity Management (IdM) HBAC rule configuration in the CLI by using simulated scenarios to discover misconfigurations and security risks before deploying rules in production.

Important

Always test custom HBAC rules before you start using them in production.

Note that IdM does not test the effect of HBAC rules on trusted Active Directory (AD) users. Because the IdM LDAP directory does not store the AD data, IdM cannot resolve group membership of AD users when simulating HBAC scenarios.

**Procedure**

-   Use the `ipa hbactest`{.literal} command to test your HBAC rule. You have the option to test a single HBAC rule or multiple HBAC rules.

    -   To test a single HBAC rule:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa hbactest --user=sysadmin --host=server.idm.example.com --service=sudo --rules=rule_name
        ---------------------
        Access granted: True
        ---------------------
          Matched rules: rule_name
        ```

    -   To test multiple HBAC rules:

        a.  Add a second rule only allowing the *sysadmin* to use `ssh`{.literal} on all hosts:

            ``` {.language-plaintext tabindex="-1"}
            $ ipa hbacrule-add --hostcat=all rule2_name
            $ ipa hbacrule-add-user --users sysadmin rule2_name
            $ ipa hbacrule-add-service --hbacsvcs=sshd rule2_name
              Rule name: rule2_name
              Host category: all
              Enabled: True
              Users: admin
              HBAC Services: sshd
            -------------------------
            Number of members added 1
            -------------------------
            ```

        b.  Test multiple HBAC rules by running the following command:

            ``` {.language-plaintext tabindex="-1"}
            $ ipa hbactest --user=sysadmin --host=server.idm.example.com --service=sudo --rules=rule_name --rules=rule2_name
            --------------------
            Access granted: True
            --------------------
              Matched rules: rule_name
              Not matched rules: rule2_name
            ```

            In the output, **Matched rules** list the rules that allowed successful access while **Not matched** rules list the rules that prevented access. Note that if you do not specify the `--rules`{.literal} option, all rules are applied. Using `--rules`{.literal} is useful to independently test each rule.

#### [46.2.3. Disabling HBAC rules in the IdM CLI](#disabling-hbac-rules-in-the-idm-cli) {#disabling-hbac-rules-in-the-idm-cli .title}

Disable HBAC rules using the Identity Management (IdM) CLI to temporarily deactivate access policies without permanent deletion. Disabling rules enables testing and troubleshooting while preserving rule configurations.

Note

Disabling HBAC rules is useful when you are configuring custom HBAC rules for the first time. To ensure that your new configuration is not overridden by the default `allow_all`{.literal} HBAC rule, you must disable `allow_all`{.literal}.

**Procedure**

-   Use the `ipa hbacrule-disable`{.literal} command. For example, to disable the `allow_all`{.literal} rule:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hbacrule-disable allow_all
    ------------------------------
    Disabled HBAC rule "allow_all"
    ------------------------------
    ```

### [46.3. Adding HBAC service entries for custom HBAC services](#adding-hbac-service-entries-for-custom-hbac-services) {#adding-hbac-service-entries-for-custom-hbac-services .title}

You can configure any pluggable authentication module (PAM) service as a host-based access control (HBAC) service to define custom services in HBAC rules beyond the default services and service groups.

The PAM service files are located in the `/etc/pam.d/`{.literal} directory.

Note

Adding a service as an HBAC service is not the same as adding a service to the domain. Adding a service to the domain makes it available to other resources in the domain, but it does not allow you to use the service in HBAC rules.

#### [46.3.1. Adding HBAC service entries for custom HBAC services in the IdM WebUI](#adding-hbac-service-entries-for-custom-hbac-services-in-the-idm-webui) {#adding-hbac-service-entries-for-custom-hbac-services-in-the-idm-webui .title}

Create custom HBAC service entries in the Identity Management (IdM) Web UI to control access to applications and services not included in the default service list. This enables granular host-based access control for your custom services.

**Procedure**

1.  Select **Policy\>Host-Based Access Control\>HBAC Services**.
2.  Click Add to add an HBAC service entry.
3.  Enter a name for the service, and click Add.

#### [46.3.2. Adding HBAC service entries for custom HBAC services in the IdM CLI](#adding-hbac-service-entries-for-custom-hbac-services-in-the-idm-cli) {#adding-hbac-service-entries-for-custom-hbac-services-in-the-idm-cli .title}

Create custom HBAC service entries in the Identity Management (IdM) CLI to control access to applications and services not included in the default service list. This enables granular host-based access control for your custom services.

**Procedure**

-   Use the `ipa hbacsvc-add`{.literal} command. For example, to add an entry for the `tftp`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hbacsvc-add tftp
    -------------------------
    Added HBAC service "tftp"
    -------------------------
      Service name: tftp
    ```

### [46.4. Adding HBAC service groups](#adding-hbac-service-groups) {#adding-hbac-service-groups .title}

HBAC service groups can simplify HBAC rules management. For example, instead of adding individual services to an HBAC rule, you can add a whole service group.

#### [46.4.1. Adding HBAC service groups in the IdM WebUI](#adding-hbac-service-groups-in-the-idm-webui) {#adding-hbac-service-groups-in-the-idm-webui .title}

Create HBAC service groups in the Identity Management (IdM) Web UI to manage multiple related services collectively in access control policies. Service groups simplify HBAC rule management by helping you to apply policies to multiple services at once.

**Procedure**

1.  Select **Policy\>Host-Based Access Control\>HBAC Service Groups**.
2.  Click Add to add an HBAC service group.
3.  Enter a name for the service group, and click Edit.
4.  On the service group configuration page, click Add to add an HBAC service as a member of the group.

#### [46.4.2. Adding HBAC service groups in the IdM CLI](#adding-hbac-service-groups-in-the-idm-cli) {#adding-hbac-service-groups-in-the-idm-cli .title}

Create HBAC service groups in the Identity Management (IdM) CLI to manage multiple related services collectively in access control policies. Service groups simplify HBAC rule management by helping you to apply policies to multiple services at once.

**Procedure**

1.  Use the `ipa hbacsvcgroup-add`{.literal} command in your terminal to add an HBAC service group. For example, to add a group named *login*:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hbacsvcgroup-add
    Service group name: login
    --------------------------------
    Added HBAC service group "login"
    --------------------------------
      Service group name: login
    ```

2.  Use the `ipa hbacsvcgroup-add-member`{.literal} command to add an HBAC service as a member of the group. For example, to add the `sshd`{.literal} service to the *login* group:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa hbacsvcgroup-add-member
    Service group name: login
    [member HBAC service]: sshd
      Service group name: login
      Member HBAC service: sshd
    -------------------------
    Number of members added 1
    -------------------------
    ```

### [46.5. Additional resources](#configuring-host-based-access-control-rules_465-additional-resources) {#additional-resources-21 .title}

-   [Ensuring the presence of host-based access control rules in IdM using Ansible playbooks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/ensuring-the-presence-of-host-based-access-control-rules-in-idm-using-ansible-playbooks)

## [Chapter 47. Defining SELinux user maps](#defining-selinux-user-maps) {#chapter-47.-defining-selinux-user-maps .title}

Learn how SELinux user maps work in IdM, how to configure Security-Enhanced Linux (SELinux) user map order and defaults, and how to map Identity Management (IdM) users to SELinux users by using the IdM Web UI or the IdM CLI.

### [47.1. SELinux contexts and Identity Management](#selinux-contexts-and-identity-management) {#selinux-contexts-and-identity-management .title}

Learn how Security-Enhanced Linux (SELinux) contexts and policy stay on each host while Identity Management (IdM) maps domain users to SELinux user strings at login.

SELinux provides kernel-level mandatory access control (MAC) to govern how processes interact with system resources. Based on the expected behavior of processes and their security implications, administrators and policy writers define *security contexts*. These are labels assigned to every subject, such as processes, and object, such as files, sockets, and hardware on the system.

While the kernel only sees subjects (processes) and objects (files or sockets), the chain of security begins with the *human identity*. When a user logs in using IdM, their network account is mapped to a specific SELinux user. This mapping acts as a bridge: it ensures that every process started by that human inherits a specific security context.

Consequently, a human does not just have access to a file; instead, the human's identity determines their SELinux label, and that label dictates exactly which resources their processes can access. By assigning different contexts to different groups of people, such as administrators, developers, or guests, organisations can ensure that even if a human's session is compromised, the blast radius of a security breach is effectively minimized.

IdM does not create or modify SELinux contexts or policy on client systems. Instead, IdM uses strings that can match contexts already present on target hosts as the basis for mapping IdM users in the domain to SELinux users on a system.

If you create an SELinux user map in IdM, you do not modify the SELinux policy on your hosts:

-   IdM does not apply new security rules on your hosts. The SELinux policy stays local. The rules that define what `staff_u`{.literal} can do compared to `user_u`{.literal} are stored on the individual Linux host, not in the central IdM database.

-   The system maps the IdM user to an SELinux user string, such as `staff_u`{.literal}. When the user logs in to a target host, the host evaluates this string against its local SELinux policy:

    -   If the string matches a local SELinux user, the host applies the corresponding restrictions.
    -   If the string does not match a local SELinux user, the host applies the default SELinux context.

Each SELinux user is associated with one or more SELinux roles. The role is assigned both a multilayer security (MLS) context and a multi-category security (MCS) context. The MLS and MCS contexts confine users so that they can access only certain processes, files, and operations on the system.

The following list maps SELinux users that are available on a system to their allowed roles:

``` {.language-plaintext tabindex="-1"}
                Labelling  MLS/       MLS/
SELinux User    Prefix     MCS Level  MCS Range        SELinux Roles

guest_u         user       s0         s0               guest_r
root            user       s0         s0-s0:c0.c1023   staff_r sysadm_r system_r unconfined_r
staff_u         user       s0         s0-s0:c0.c1023   staff_r sysadm_r system_r unconfined_r
sysadm_u        user       s0         s0-s0:c0.c1023   sysadm_r
system_u        user       s0         s0-s0:c0.c1023   system_r unconfined_r
unconfined_u    user       s0         s0-s0:c0.c1023   system_r unconfined_r
user_u          user       s0         s0               user_r
xguest_u        user       s0         s0               xguest_r
```

SELinux user maps work with the System Security Services Daemon (SSSD) and the `pam_selinux`{.literal} PAM module. When a remote user logs in to a machine, SSSD queries its IdM identity provider for user information, including any SELinux maps. The PAM module then assigns the appropriate SELinux user context. SSSD caching allows the mapping to work while offline.

**Additional resources**

-   [Using SELinux on RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/)

### [47.2. Benefits of mapping IdM users to SELinux users](#benefits-of-mapping-idm-users-to-selinux-users) {#benefits-of-mapping-idm-users-to-selinux-users .title}

Learn how mapping Identity Management (IdM) users to SELinux users centralizes SELinux context assignment and ties it to identity, host, and host-based access policy in the IdM domain.

SELinux users and policies operate at the system level, not the network level. SELinux users are configured independently on each system. While that is acceptable in many environments because SELinux defines common system users and SELinux-aware services define their own policies, it can be problematic when remote users and systems access local resources. Remote users and services might receive a default SELinux context that does not match their intended identity or role.

IdM solves this problem by integrating an identity domain with local SELinux services. IdM can map IdM users to configured SELinux users *per host*, *per host group*, or based on a *host-based access control (HBAC) rule*. Specifically, mapping SELinux and IdM users improves user administration as follows:

-   Remote users can receive appropriate SELinux user contexts based on their IdM group assignments. Administrators can apply the same policies consistently without creating local accounts or reconfiguring SELinux on each host.
-   The SELinux context associated with a user is centralized in IdM.
-   SELinux user context assignment can follow the same policy decisions you already manage in IdM, such as which users are allowed to access which hosts through HBAC rules.
-   Administrators can review and change SELinux user map configuration in one place, including which IdM users, groups, hosts, and host groups are assigned to each SELinux user map.

An SELinux user map links an IdM user to a specific SELinux user on a per-host basis. This allows administrators to assign different security contexts to the same person depending on which system they access.

### [47.3. SELinux user types in IdM](#selinux-user-types-in-idm) {#selinux-user-types-in-idm .title}

Learn how Identity Management (IdM) maintains a central list of SELinux user strings with MLS and MCS ranges that you attach to maps and assign at login.

The core of an SELinux user map is the SELinux user. Each map is associated with an SELinux user. The SELinux users available for mapping are configured centrally in IdM. By default, these include:

-   `unconfined_u`{.literal} (also used as a default for IdM users)
-   `guest_u`{.literal}
-   `xguest_u`{.literal}
-   `user_u`{.literal}
-   `staff_u`{.literal}

You can change this default list: any *native* SELinux user can be added or removed from the central IdM SELinux user list.

In the IdM server configuration, each SELinux user is configured with its user name and its MLS and MCS range, in the form `SELinux_user:MLS[:MCS]`{.literal}. The IdM server uses this format when configuring maps.

**Additional resources**

-   [SELinux contexts and Identity Management](#selinux-contexts-and-identity-management "47.1. SELinux contexts and Identity Management")

### [47.4. HBAC rules and SELinux user maps in IdM](#hbac-rules-and-selinux-user-maps-in-idm) {#hbac-rules-and-selinux-user-maps-in-idm .title}

HBAC rules integrate with SELinux user maps in Identity Management (IdM) so that the same user and host membership controls both access and SELinux context assignment.

You can associate SELinux mapping rules with HBAC rules to simplify administration and avoid duplicating membership in separate map and HBAC definitions. As long as the HBAC rule defines a user and a host, you can use it for an SELinux user map. Linking an SELinux user map to an HBAC rule ensures that the same user and host membership drives both access enforcement and SELinux context assignment.

If an HBAC rule is associated with an SELinux user map, you cannot delete the host-based access control rule until you remove it from the SELinux user map configuration.

Note

The IdM SELinux configuration is flexible. In addition to using HBAC rules, you can assign IdM users and hosts to an SELinux user map explicitly. You can also assign user groups or host groups to SELinux maps.

**Additional resources**

-   [Configuring host-based access control rules](#configuring-host-based-access-control-rules "Chapter 46. Configuring host-based access control rules")

### [47.5. SELinux user map order and default SELinux user](#selinux-user-map-order-and-default-selinux-user) {#selinux-user-map-order-and-default-selinux-user .title}

Learn about how to configure the SELinux user map order and the default SELinux user on the IdM server so that unmapped domain users still receive a valid context and so that the server ranks SELinux users from most confined to least confined.

Important

These settings do not replace individual user maps. They define the global list and fallback only.

The SELinux user map order is a list of SELinux users ranked from most confined to least confined. It is part of the IdM server configuration. An SELinux user map associates an SELinux user on a client with an Identity Management (IdM) user.

Each SELinux user entry uses this format:

``` {.language-plaintext tabindex="-1"}
SELinux_user:MLS[:MCS]
```

Separate individual user entries with a dollar sign (`$`{.literal}).

Because IdM user entries do not require an SELinux map, many entries might be unmapped. The IdM server configuration defines a *default* SELinux user---one of the users from the full SELinux map list---for unmapped IdM user entries so that those users still receive a valid SELinux context. The default SELinux user for unmapped IdM user entries is `unconfined_u`{.literal}, which is consistent with the default SELinux user for system users on Red Hat Enterprise Linux.

Warning

Do not use `unconfined_u`{.literal} as the default IdM SELinux user in production. Because `unconfined_u`{.literal} is subject to only minimal SELinux restrictions, it effectively removes most of the protections SELinux provides. Set the default to a more confined user, such as `guest_u`{.literal}, before deploying.

**Additional resources**

-   [Configuring SELinux user map order and defaults in the IdM Web UI](#configuring-selinux-user-map-order-and-defaults-in-the-idm-web-ui "47.6. Configuring SELinux user map order and defaults in the IdM Web UI")
-   [Configuring SELinux user map order and defaults by using the IdM CLI](#configuring-selinux-user-map-order-and-defaults-by-using-the-idm-cli "47.7. Configuring SELinux user map order and defaults by using the IdM CLI")

### [47.6. Configuring SELinux user map order and defaults in the IdM Web UI](#configuring-selinux-user-map-order-and-defaults-in-the-idm-web-ui) {#configuring-selinux-user-map-order-and-defaults-in-the-idm-web-ui .title}

Use the Identity Management (IdM) Web UI to set the SELinux user map order, the default SELinux user for unmapped IdM entries, and which SELinux users are available for mapping on the IdM server. This controls how strictly unmapped users are confined and which strings maps may use.

**Prerequisites**

-   You are logged in to the IdM Web UI as an administrator.

**Procedure**

1.  Go to **IPA Server** → **Configuration**.

2.  Scroll down to the **SELINUX OPTIONS** section.

3.  Edit the SELinux user configuration: **SELinux user map order**, **Default SELinux user**, or both, as needed.

4.  Click **Update** at the top of the page to save your changes.

**Additional resources**

-   [SELinux user map order and default SELinux user](#selinux-user-map-order-and-default-selinux-user "47.5. SELinux user map order and default SELinux user")
-   [Configuring SELinux user map order and defaults by using the IdM CLI](#configuring-selinux-user-map-order-and-defaults-by-using-the-idm-cli "47.7. Configuring SELinux user map order and defaults by using the IdM CLI")

### [47.7. Configuring SELinux user map order and defaults by using the IdM CLI](#configuring-selinux-user-map-order-and-defaults-by-using-the-idm-cli) {#configuring-selinux-user-map-order-and-defaults-by-using-the-idm-cli .title}

Use the Identity Management (IdM) CLI to set the SELinux user map order, the default SELinux user for unmapped IdM entries, and which SELinux users are available for mapping in IdM. This controls how strictly unmapped users are confined and which strings maps may use.

**Prerequisites**

-   You have administrative credentials to access the IdM CLI.

**Procedure**

1.  Optional: View the SELinux users configured on the IdM server and available for mapping:

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa config-show
    ```

    Example output (excerpt):

    ``` {.language-plaintext tabindex="-1"}
    ...
    SELinux user map order: guest_u:s0$xguest_u:s0$user_u:s0$staff_u:s0-s0:c0.c1023$unconfined_u:s0-s0:c0.c1023
    Default SELinux user: unconfined_u:s0-s0:c0.c1023
    ```

    The list shows available SELinux users from the most confined to the least confined, separated by `$`{.literal}.

2.  To change the list of SELinux users and their order, run `ipa config-mod`{.literal} with the `--ipaselinuxusermaporder`{.literal} option. List SELinux users from most confined to least confined, separated by `$`{.literal}. The following example adds the `sysadm_u`{.literal} user to the SELinux user map order:

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa config-mod --ipaselinuxusermaporder="guest_u:s0$xguest_u:s0$user_u:s0$staff_u:s0-s0:c0.c1023$sysadm_u:s0-s0:c0.c1023$unconfined_u:s0-s0:c0.c1023"
    ```

    Note

    The default SELinux user used for unmapped entries must appear in the user map list or the modification fails. If you change the default, it must be a user that is already in the SELinux map list, or you must update the map list first.

3.  To change the default SELinux user for IdM users that do not have a specific map, run `ipa config-mod`{.literal} with `--ipaselinuxusermapdefault`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa config-mod --ipaselinuxusermapdefault="guest_u:s0"
    ```

**Additional resources**

-   [SELinux user map order and default SELinux user](#selinux-user-map-order-and-default-selinux-user "47.5. SELinux user map order and default SELinux user")

### [47.8. Mapping SELinux users and IdM users in the IdM Web UI](#mapping-selinux-users-and-idm-users-in-the-idm-web-ui) {#mapping-selinux-users-and-idm-users-in-the-idm-web-ui .title}

Create or edit SELinux user maps in the Identity Management (IdM) Web UI to associate an SELinux user context on IdM clients with IdM users, groups, hosts, host groups, or with a single host-based access control (HBAC) rule.

#### [47.8.1. Displaying SELinux user maps in the IdM Web UI](#displaying-selinux-user-maps-in-the-idm-web-ui) {#displaying-selinux-user-maps-in-the-idm-web-ui .title}

An SELinux user map associates an SELinux user string with IdM users and hosts, or with a host-based access control (HBAC) rule that already defines users and hosts. Use the IdM Web UI to review which maps exist in the domain and to open a map to inspect its settings.

**Procedure**

1.  In the IdM Web UI, go to **Policy** → **SELinux User Mappings**.

    The page lists the SELinux user maps that are defined in the domain.

2.  Optional: To inspect the configuration of a map, click its name in the list. The map details show the **General**, **Users**, and **Hosts** settings that apply to that map.

#### [47.8.2. Creating SELinux user maps in the IdM Web UI](#creating-selinux-user-maps-in-the-idm-web-ui) {#creating-selinux-user-maps-in-the-idm-web-ui .title}

You can create a new SELinux user map by using the **Add** workflow in the IdM Web UI. Either assign a host-based access control (HBAC) rule to the map, or assign IdM users and hosts manually. You cannot combine both approaches on the same map.

**Procedure**

1.  In the IdM Web UI, go to **Policy** → **SELinux User Mappings**.

2.  In the list of mappings, click **Add** to create a map.

3.  Enter the map name and the SELinux user. The SELinux user string must match the IdM server configuration exactly, in the form `SELinux_user:MLS[:MCS]`{.literal}.

4.  Click **Add and Edit** to add IdM user information.

5.  Use either an HBAC rule **or** assign users and hosts manually:

    -   To use a host-based access control rule, choose the rule in the drop-down list in the **General** section. Using a host-based access control rule also applies that rule's access controls for which hosts a remote user may use to reach a target machine.

        Note

        Only one host-based access control rule can be assigned. The host-based access control rule must include users and hosts, not only services.

    -   To assign users, user groups, hosts, or host groups directly to the SELinux map:

        a.  In the **Users** and **Hosts** sections, click **Add**.

        b.  In the left column, choose the users, hosts, or groups that you want to add, use the **\>\>** control to move them to the **Prospective** column, and click **Add** to add them to the map.

6.  Click **Update** at the top to save the SELinux user map.

#### [47.8.3. Modifying SELinux user maps in the IdM Web UI](#modifying-selinux-user-maps-in-the-idm-web-ui) {#modifying-selinux-user-maps-in-the-idm-web-ui .title}

If an SELinux user map exists, you can change its HBAC association, add or remove IdM users and hosts that are assigned to it, or delete the map from the IdM Web UI.

**Procedure**

1.  In the IdM Web UI, go to **Policy** → **SELinux User Mappings**.

2.  Click the name of the map that you want to change.

3.  Select one of the following actions based on your needs:

    -   In the **General** section, change the host-based access control (HBAC) rule in the drop-down list.

        Note

        If you assign a new HBAC rule to an existing map, the new HBAC association replaces the previous map configuration for that setting.

    -   To add IdM users, user groups, hosts, or host groups to the map:

        a.  Go to the **Users** or **Hosts** section.

        b.  Click **Add**.

        c.  In the left column, choose the entries that you want to add and use the **\>\>** control to move them to the **Prospective** column.

        d.  Click **Add**.

    -   To remove an assigned user, user group, host, or host group:

        a.  Select the entry in the **Users** or **Hosts** section.
        b.  Use the control that removes the assignment (for example, **Delete**).
        c.  Click **Update** at the top to save your changes.

    -   To delete the SELinux user map entirely, use the **Delete** action for the map in the **SELinux User Mappings** list.

### [47.9. Mapping SELinux users and IdM users in the IdM CLI](#mapping-selinux-users-and-idm-users-in-the-idm-cli) {#mapping-selinux-users-and-idm-users-in-the-idm-cli .title}

Create or edit SELinux user maps in the Identity Management (IdM) CLI to associate an SELinux user context on IdM clients with IdM users, groups, hosts, host groups, or with a single host-based access control (HBAC) rule.

#### [47.9.1. Prerequisites](#prerequisites_2) {#prerequisites-1 .title}

-   You have administrative credentials to access the IdM CLI.

#### [47.9.2. Displaying SELinux user maps by using the IdM CLI](#displaying-selinux-user-maps-by-using-the-idm-cli) {#displaying-selinux-user-maps-by-using-the-idm-cli .title}

An SELinux user map associates an SELinux user string with IdM users and hosts, or with a host-based access control (HBAC) rule that already defines users and hosts. When you use the IdM CLI, you refer to those pieces with options such as `--selinuxuser`{.literal}, `--users`{.literal}, `--groups`{.literal}, `--hosts`{.literal}, `--hostgroups`{.literal}, and `--hbacrule`{.literal}. Use the following steps to list SELinux user maps in the domain and to show the details of one map.

**Procedure**

-   To list all SELinux user maps in the domain:

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa selinuxusermap-find
    ```

-   To display a specific map, run `ipa selinuxusermap-show`{.literal} and pass the map name. Replace `selinux1`{.literal} with the name of your map.

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa selinuxusermap-show selinux1
    ```

#### [47.9.3. Creating SELinux user maps by using the IdM CLI](#creating-selinux-user-maps-by-using-the-idm-cli) {#creating-selinux-user-maps-by-using-the-idm-cli .title}

You can create a new SELinux user map in two ways: run `ipa selinuxusermap-add`{.literal} and then attach IdM users and hosts with `ipa selinuxusermap-add-user`{.literal} and `ipa selinuxusermap-add-host`{.literal}, or create the map in one step by referencing an host-based access control (HBAC) rule with `--hbacrule`{.literal}. The `--selinuxuser`{.literal} value must match the SELinux user string in the IdM server configuration, in the form `SELinux_user:MLS[:MCS]`{.literal}. If you use explicit users and hosts, you must add both users or groups and hosts or host groups for the mapping to be valid. You can repeat CLI options or pass a comma-separated list in braces, for example `--option={val1,val2,val3}`{.literal}.

**Procedure**

-   To create a new map and assign users and hosts with separate commands:

    a.  Create the map record first. Replace `<selinux1>`{.literal} with your map name:

        ``` {.language-plaintext tabindex="-1"}
        [user1@server ~]$ ipa selinuxusermap-add --selinuxuser="xguest_u:s0" <selinux1>
        ```

    b.  Add IdM users to the map.

        ``` {.language-plaintext tabindex="-1"}
        [user1@server ~]$ ipa selinuxusermap-add-user --users=user1 --users=user2 --users=user3 selinux1
        ```

    c.  Add client hosts to the map.

        ``` {.language-plaintext tabindex="-1"}
        [user1@server ~]$ ipa selinuxusermap-add-host --hosts=server.example.com --hosts=test.example.com selinux1
        ```

-   Alternatively, to create a map that references an HBAC rule:

    The `--hbacrule`{.literal} option names the HBAC rule to use. Using a rule applies that rule's access controls for which hosts a remote user may use to access a target host, in addition to applying SELinux contexts after login. The rule must specify users and hosts so that the SELinux map can form the SELinux user, IdM user, and host relationship. Only one HBAC rule can be specified.

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa selinuxusermap-add --hbacrule=webserver --selinuxuser="xguest_u:s0" selinux1
    ```

#### [47.9.4. Modifying SELinux user maps by using the IdM CLI](#modifying-selinux-user-maps-by-using-the-idm-cli) {#modifying-selinux-user-maps-by-using-the-idm-cli .title}

If an SELinux user map exists, you can add or remove IdM users and hosts that are assigned to it, change its HBAC association, or delete the map entirely.

**Procedure**

-   To add IdM users to an existing map:

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa selinuxusermap-add-user --users=user1 selinux1
    ```

    Note

    If you run `ipa selinuxusermap-mod`{.literal} with `--hbacrule`{.literal} on an existing map, the new HBAC association replaces the previous map configuration for that setting.

-   To add client hosts to an existing map:

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa selinuxusermap-add-host --hosts=server.example.com selinux1
    ```

-   To remove an IdM user from a map:

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa selinuxusermap-remove-user --users=user2 selinux1
    ```

-   To remove a client host from a map:

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa selinuxusermap-remove-host --hosts=server.example.com selinux1
    ```

-   To delete an SELinux user map entirely:

    ``` {.language-plaintext tabindex="-1"}
    [user1@server ~]$ ipa selinuxusermap-del selinux1
    ```

### [47.10. Additional resources](#defining-selinux-user-maps_4710-additional-resources) {#additional-resources-22 .title}

-   [Using SELinux on RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/)

## [Chapter 48. Configuring session recording by using the CLI](#configuring-session-recording-by-using-cli) {#chapter-48.-configuring-session-recording-by-using-the-cli .title}

Configure user terminal session recordings using the System Security Services Daemon (SSSD) to audit and monitor user activity. Manage and play back recorded sessions using the `tlog`{.literal} command-line utility.

### [48.1. Session recording overview and components](#session-recording-overview-and-components) {#session-recording-overview-and-components .title}

Session recording captures and saves a user's terminal activity. This provides a detailed, unchangeable record of all commands, output, and error messages, which you can use for auditing, troubleshooting, and investigating a security incident.

SSSD enforces the recording policies you define, and the `tlog`{.literal} utility handles the actual recording and playback.

Components of the session recording

:   

-   **`tlog`{.literal} utility**

    The `tlog`{.literal} utility provides tools for recording and playing back terminal I/O. `tlog-rec-session`{.literal} functions as an intermediary login shell and captures all data between the user's terminal and shell. All `tlog`{.literal} recordings are in JSON format. You can play back recorded sessions using `tlog-play`{.literal}. Note that by default, terminal input recording is disabled for security reasons. For detailed configuration options, see the `/etc/tlog/tlog-rec-session.conf`{.literal} file and the `tlog-rec-session.conf(5)`{.literal} man page on your system.

-   **SSSD**

    SSSD provides a set of daemons that manage access to remote directories and authentication mechanisms. When you configure session recording, SSSD overlays the user's default shell with the `tlog-rec-session`{.literal} program.

Limitations of session recording

:   -   You can configure session recording for the root user, but the root user has the privileges to disable or bypass the recording process, which makes the session recording unreliable for auditing purposes.

    -   Terminal sessions in a GNOME graphical session are not recorded. This is because all terminals within a graphical session share a single audit session ID, which prevents `tlog`{.literal} from distinguishing between them and capturing recordings correctly.

    -   A logging loop can occur when viewing the journal. When a recorded user views the system journal or `/var/log/messages`{.literal}, it generates new logs, which are then recorded and displayed, causing a loop of flooded output.

        To prevent the logging loop, view the journal in real time and filter out the log entries which create the loop:

        ``` {.language-plaintext tabindex="-1"}
        journalctl -f | grep -v 'tlog-rec-session'
        ```

        You can also configure `tlog`{.literal} to limit the output. For details, see `tlog-rec-session.conf`{.literal} man pages.

    -   You must configure session recording on the target host for remote execution. For example, if you want to record a user's session when they use `ssh`{.literal} to connect to a remote system, configure the recording on the remote system they connect to.

    -   All recordings are lost on reboot if `systemd-journald`{.literal} service uses its default configuration to store the journal in-memory.

### [48.2. Enabling and configuring session recording with SSSD from the CLI](#enabling-and-configuring-session-recording-with-sssd-from-the-cli) {#enabling-and-configuring-session-recording-with-sssd-from-the-cli .title}

Enable session recording through SSSD in Identity Management (IdM) to capture terminal activity for specific users or groups. Session recording improves security auditing and helps investigate user activity.

When you configure session recording, you use SSSD to define which users or groups to record by setting the `scope`{.literal} option to one of the following values:

-   `none`{.literal} to record no sessions
-   `some`{.literal} to record only specified users and groups
-   `all`{.literal} to record all users

**Prerequisites**

-   Commands that start with the `#`{.literal} command prompt require administrative privileges provided by `sudo`{.literal} or root user access. For information on how to configure `sudo`{.literal} access, see [Enabling unprivileged users to run certain commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access#enabling-unprivileged-users-to-run-certain-commands).
-   You are using SSSD for authentication.

**Procedure**

1.  Install the `tlog`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tlog
    ```

2.  Open the `sssd-session-recording.conf`{.literal} configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/sssd/conf.d/sssd-session-recording.conf
    ```

3.  Specify the scope of session recording and the users and groups to record. For example:

    ``` {.language-plaintext tabindex="-1"}
    [session_recording]
    scope = some
    users = <user_name_1>, <user_name_2>
    groups = <group_name>
    exclude_users = <user_name_to_exclude>
    exclude_groups = <group_name_to_exclude>
    ```

    For more details, see the `sssd-session-recording(5)`{.literal} man page on your system.

4.  To enable the SSSD profile, run the following command:

    ``` {.language-plaintext tabindex="-1"}
    # authselect select sssd with-tlog
    ```

5.  Restart SSSD to load the configuration changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Additional resources**

-   [Configuring a system for session recording by using RHEL system roles](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/configuring-a-system-for-session-recording-by-using-rhel-system-roles)

### [48.3. Playing back session recordings](#playing-back-session-recordings) {#playing-back-session-recordings .title}

Review terminal session recordings using the `tlog-play`{.literal} utility or the web console to audit user activities and investigate security incidents. Session recordings help ensure compliance and identify unauthorized access attempts.

The system journal stores session recordings. By default, it saves them in-memory, so you lose recordings on reboot unless you configure persistent storage.

You can play back recordings directly from the system journal by using the `tlog-play`{.literal} utility. Alternatively, you can install the `cockpit-session-recording`{.literal} package to manage and play back recordings on the RHEL web console. .Prerequisites \* Terminal sessions have been recorded.

**Procedure**

1.  Optional: List recorded sessions:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl COMM=tlog-rec-session
    ```

2.  Play back a specific session:

    ``` {.language-plaintext tabindex="-1"}
    # tlog-play --reader=journal --journal-id=<recorded_session_id>
    ```

    For more advanced options, such as changing playback speed or fast-forwarding, see the `tlog-play`{.literal} man page on your system.

**Additional resources**

-   [Installing web console add-ons and creating custom pages](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/installing-web-console-add-ons-and-creating-custom-pages)

## [Chapter 49. Managing public SSH keys for users and hosts](#managing-public-ssh-keys-for-users-and-hosts) {#chapter-49.-managing-public-ssh-keys-for-users-and-hosts .title}

Manage public SSH keys for users and hosts in Identity Management (IdM) to centralize SSH key distribution and simplify secure access across your domain. Storing SSH keys in IdM ensures consistent authentication without manually distributing key files.

### [49.1. About the SSH key format](#about-the-ssh-key-format) {#about-the-ssh-key-format .title}

Identity Management (IdM) supports OpenSSH-style and raw RFC 4253-style SSH key formats, providing flexibility when uploading keys.

Note that IdM automatically converts RFC 4253-style keys into OpenSSH-style keys before saving them into the IdM LDAP server.

The IdM server can identify the type of key, such as an RSA or DSA key, from the uploaded key blob. In a key file such as `~/.ssh/known_hosts`{.literal}, a key entry is identified by the hostname and IP address of the server, its type, and the key. For example:

``` {.language-plaintext tabindex="-1"}
host.example.com,1.2.3.4 ssh-rsa AAA...ZZZ==
```

This is different from a user public key entry, which has the elements in the order *type key== comment*:

``` {.language-plaintext tabindex="-1"}
"ssh-rsa ABCD1234...== ipaclient.example.com"
```

A key file, such as `id_rsa.pub`{.literal}, consists of three parts: the key type, the key, and an additional comment or identifier. When uploading a key to IdM, you can upload all three key parts or only the key. If you only upload the key, IdM automatically identifies the key type, such as RSA or DSA, from the uploaded key.

If you use the host public key entry from the `~/.ssh/known_hosts`{.literal} file, you must reorder it to match the format of a user key, *type key== comment*:

``` {.language-plaintext tabindex="-1"}
ssh-rsa AAA...ZZZ== host.example.com,1.2.3.4
```

IdM can determine the key type automatically from the content of the public key. The comment is optional, to make identifying individual keys easier. The only required element is the public key blob.

IdM uses public keys stored in the following OpenSSH-style files:

-   Host public keys are in the `known_hosts`{.literal} file.
-   User public keys are in the `authorized_keys`{.literal} file.

**Additional resources**

-   [RFC 4716](https://www.rfc-editor.org/rfc/rfc4716)
-   [RFC 4253](https://www.rfc-editor.org/rfc/rfc4253)

### [49.2. About IdM and OpenSSH](#about-idm-and-openssh) {#about-idm-and-openssh .title}

Identity Management (IdM) integrates with OpenSSH during server and client installation to centralize SSH key management through SSSD. This integration enables IdM to serve as a universal repository for user and host SSH keys.

During an IdM server or client installation, as part of the install script:

-   An OpenSSH server and client is configured on the IdM client machine.
-   SSSD is configured to store and retrieve user and host SSH keys in cache. This allows IdM to serve as a universal and centralized repository of SSH keys.

If you enable the SSH service during the client installation, an RSA key is created when the SSH service is started for the first time.

Note

When you run the `ipa-client-install`{.literal} install script to add the machine as an IdM client, the client is created with two SSH keys, RSA and DSA.

As part of the installation, you can configure the following:

-   Configure OpenSSH to automatically trust the IdM DNS records where the key fingerprints are stored using the `--ssh-trust-dns`{.literal} option.
-   Disable OpenSSH and prevent the install script from configuring the OpenSSH server using the `--no-sshd`{.literal} option.
-   Prevent the host from creating DNS SSHFP records with its own DNS entries using the `--no-dns-sshfp`{.literal} option.

If you do not configure the server or client during installation, you can manually configure SSSD later. Note that caching SSH keys by SSSD requires administrative privileges on the local machines.

**Additional resources**

-   [Configuring SSSD to Provide a Cache for the OpenSSH Services](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/linux_domain_identity_authentication_and_policy_guide/openssh-sssd)

### [49.3. Generating SSH keys](#generating-ssh-keys) {#generating-ssh-keys .title}

Generate SSH key pairs using the `ssh-keygen`{.literal} utility to enable secure, password-free authentication for users and hosts in Identity Management (IdM). SSH keys provide a more secure alternative to password-based authentication.

**Procedure**

1.  To generate an RSA SSH key, run the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh-keygen -t rsa -C user@example.com
    Generating public/private rsa key pair.
    ```

    Note if generating a host key, replace [user@example.com](mailto:user@example.com) with the required hostname, such as `server.example.com,1.2.3.4`{.literal}.

2.  Specify the file where you are saving the key or press enter to accept the displayed default location.

    ``` {.language-plaintext tabindex="-1"}
    Enter file in which to save the key (/home/user/.ssh/id_rsa):
    ```

    Note if generating a host key, save the key to a different location than the user's `~/.ssh/`{.literal} directory so you do not overwrite any existing keys. for example, `/home/user/.ssh/host_keys`{.literal}.

3.  Specify a passphrase for your private key or press enter to leave the passphrase blank.

    ``` {.language-plaintext tabindex="-1"}
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/user/.ssh/id_rsa.
    Your public key has been saved in /home/user/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:ONxjcMX7hJ5zly8F8ID9fpbqcuxQK+ylVLKDMsJPxGA user4@example.com
    The key's randomart image is:
    +---[RSA 3072]----+
    |         ..o     |
    |         .o +    |
    |     E. .  o =   |
    |    ..o=  o . +  |
    |      +oS. = + o.|
    |    . .o .* B =.+|
    |     o + . X.+.= |
    |      + o o.*+. .|
    |       .   o=o . |
    +----[SHA256]-----+
    ```

    To upload this SSH key, use the public key string stored in the displayed file.

### [49.4. Managing public SSH keys for users](#managing-public-ssh-keys-for-users) {#managing-public-ssh-keys-for-users .title}

Upload public SSH keys to Identity Management (IdM) user entries to enable SSH-based authentication without Kerberos credentials.

Users with the corresponding private key can log into IdM machines directly using SSH. If the private SSH key file is not available on a particular machine, Kerberos credentials can still be used for authentication.

#### [49.4.1. Uploading SSH keys for a user using the IdM Web UI](#uploading-ssh-keys-for-a-user-using-the-idm-web-ui) {#uploading-ssh-keys-for-a-user-using-the-idm-web-ui .title}

Upload a public SSH key to a user entry in Identity Management (IdM) by using the IdM Web UI to enable SSH login to IdM machines without requiring Kerberos credentials.

**Prerequisites**

-   Administrator privileges for managing the IdM Web UI or User Administrator role.

**Procedure**

1.  Log into the IdM Web UI.
2.  Go to the **Identity\>Users** tab.
3.  Click the name of the user to edit.
4.  In the **Account Settings** section, click the SSH public keys **Add** button.
5.  Paste the Base 64-encoded public key string into the **SSH public key** field.
6.  Click **Set**.
7.  Click **Save** at the top of the IdM Web UI window.

**Verification**

-   Under the **Accounts Settings** section, verify the key is listed under **SSH public keys**.

#### [49.4.2. Uploading SSH keys for a user using the IdM CLI](#uploading-ssh-keys-for-a-user-using-the-idm-cli) {#uploading-ssh-keys-for-a-user-using-the-idm-cli .title}

Upload a public SSH key to a user entry in Identity Management (IdM) by using the CLI to enable SSH login to IdM machines without requiring Kerberos credentials.

**Prerequisites**

-   Administrator privileges for managing the IdM CLI or User Administrator role.

**Procedure**

1.  Run the `ipa user-mod`{.literal} command with the `--sshpubkey`{.literal} option to upload the base64-encoded public key to the user entry.

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-mod user --sshpubkey="ssh-rsa AAAAB3Nza...SNc5dv== client.example.com"
    ```

    Note in this example you upload the key type, the key, and the hostname identifier to the user entry.

2.  To upload multiple keys, use `--sshpubkey`{.literal} multiple times. For example, to upload two SSH keys:

    ``` {.language-plaintext tabindex="-1"}
    --sshpubkey="AAAAB3Nza...SNc5dv==" --sshpubkey="RjlzYQo...ZEt0TAo="
    ```

3.  To use command redirection and point to a file that contains the key instead of pasting the key string manually, use the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-mod user --sshpubkey="$(cat ~/.ssh/id_rsa.pub)" --sshpubkey="$(cat ~/.ssh/id_rsa2.pub)"
    ```

**Verification**

-   Run the `ipa user-show`{.literal} command to verify that the SSH public key is associated with the specified user:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-show user
    User login: user
      First name: user
      Last name: user
      Home directory: /home/user
      Login shell: /bin/sh
      Principal name: user@IPA.TEST
      Principal alias: user@IPA.TEST
      Email address: user@ipa.test
      UID: 1118800019
      GID: 1118800019
      SSH public key fingerprint: SHA256:qGaqTZM60YPFTngFX0PtNPCKbIuudwf1D2LqmDeOcuA
                                  user@IPA.TEST (ssh-rsa)
      Account disabled: False
      Password: False
      Member of groups: ipausers
      Subordinate ids: 3167b7cc-8497-4ff2-ab4b-6fcb3cb1b047
      Kerberos keys available: False
    ```

#### [49.4.3. Deleting SSH keys for a user using the IdM Web UI](#deleting-ssh-keys-for-a-user-using-the-idm-web-ui) {#deleting-ssh-keys-for-a-user-using-the-idm-web-ui .title}

You can delete SSH public keys from user profiles using the Identity Management (IdM) WebUI. Deleting invalid keys improves security by preventing unauthorized user authentication.

**Prerequisites**

-   Administrator privileges for managing the IdM Web UI or User Administrator role.

**Procedure**

1.  Log into the IdM Web UI.
2.  Go to the **Identity\>Users** tab.
3.  Click the name of the user to edit.
4.  Under the **Account Settings** section, under **SSH public key**, click **Delete** next to the key you want to remove.
5.  Click **Save** at the top of the page.

**Verification**

-   Under the **Account Settings** section, verify the key is no longer listed under **SSH public keys**.

#### [49.4.4. Deleting SSH keys for a user using the IdM CLI](#deleting-ssh-keys-for-a-user-using-the-idm-cli) {#deleting-ssh-keys-for-a-user-using-the-idm-cli .title}

You can delete SSH public keys from user profiles using the Identity Management (IdM) CLI. Deleting invalid keys improves security by preventing unauthorized user authentication.

**Prerequisites**

-   Administrator privileges for managing the IdM CLI or User Administrator role.

**Procedure**

1.  To delete all SSH keys assigned to a user account, add the `--sshpubkey`{.literal} option to the `ipa user-mod`{.literal} command without specifying any key:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-mod user --sshpubkey=
    ```

2.  To only delete a specific SSH key or keys, use the `--sshpubkey`{.literal} option to specify the keys you want to keep, omitting the key you are deleting.

**Verification**

-   Run the `ipa user-show`{.literal} command to verify that the SSH public key is no longer associated with the specified user:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-show user
    User login: user
      First name: user
      Last name: user
      Home directory: /home/user
      Login shell: /bin/sh
      Principal name: user@IPA.TEST
      Principal alias: user@IPA.TEST
      Email address: user@ipa.test
      UID: 1118800019
      GID: 1118800019
      Account disabled: False
      Password: False
      Member of groups: ipausers
      Subordinate ids: 3167b7cc-8497-4ff2-ab4b-6fcb3cb1b047
      Kerberos keys available: False
    ```

### [49.5. Managing public SSH keys for hosts](#managing-public-ssh-keys-for-hosts) {#managing-public-ssh-keys-for-hosts .title}

Manage public SSH keys for hosts in Identity Management (IdM) to centralize host authentication and simplify SSH access across your domain. Storing host SSH keys in IdM eliminates the need to distribute `known_hosts`{.literal} files manually.

Traditionally, when a host first authenticates to another machine using OpenSSH, an administrator must manually approve the request. The target machine then stores the host's public key in its `known_hosts`{.literal} file and grants automatic access on subsequent connections. By storing host SSH keys centrally in IdM, you avoid managing these files on each machine individually.

#### [49.5.1. Uploading SSH keys for a host using the IdM Web UI](#uploading-ssh-keys-for-a-host-using-the-idm-web-ui) {#uploading-ssh-keys-for-a-host-using-the-idm-web-ui .title}

Upload a public SSH key to a host entry in Identity Management (IdM) by using the IdM Web UI so that OpenSSH can authenticate the host without Kerberos credentials.

**Prerequisites**

-   Administrator privileges for managing the IdM Web UI or User Administrator role.

**Procedure**

1.  You can retrieve the key for your host from a `~/.ssh/known_hosts`{.literal} file. For example:

    ``` {.language-plaintext tabindex="-1"}
    server.example.com,1.2.3.4 ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEApvjBvSFSkTU0WQW4eOweeo0DZZ08F9Ud21xlLy6FOhzwpXFGIyxvXZ52+siHBHbbqGL5+14N7UvElruyslIHx9LYUR/pPKSMXCGyboLy5aTNl5OQ5EHwrhVnFDIKXkvp45945R7SKYCUtRumm0Iw6wq0XD4o+ILeVbV3wmcB1bXs36ZvC/M6riefn9PcJmh6vNCvIsbMY6S+FhkWUTTiOXJjUDYRLlwM273FfWhzHK+SSQXeBp/zIn1gFvJhSZMRi9HZpDoqxLbBB9QIdIw6U4MIjNmKsSI/ASpkFm2GuQ7ZK9KuMItY2AoCuIRmRAdF8iYNHBTXNfFurGogXwRDjQ==
    ```

    You can also generate a host key. See [Generating SSH keys](#generating-ssh-keys "49.3. Generating SSH keys").

2.  Copy the public key from the key file. The full key entry has the form `host name,IP type key==`{.literal}. Only the `key==`{.literal} is required, but you can store the entire entry. To use all elements in the entry, rearrange the entry so it has the order `type key== [host name,IP]`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # cat /home/user/.ssh/host_keys.pub
    ssh-rsa AAAAB3NzaC1yc2E...tJG1PK2Mq++wQ== server.example.com,1.2.3.4
    ```

3.  Log into the IdM Web UI.

4.  Go to the **Identity\>Hosts** tab.

5.  Click the name of the host to edit.

6.  In the **Host Settings** section, click the SSH public keys **Add** button.

7.  Paste the public key for the host into the **SSH public key** field.

8.  Click **Set**.

9.  Click **Save** at the top of the IdM Web UI window.

**Verification**

-   Under the **Hosts Settings** section, verify the key is listed under **SSH public keys**.

#### [49.5.2. Uploading SSH keys for a host using the IdM CLI](#uploading-ssh-keys-for-a-host-using-the-idm-cli) {#uploading-ssh-keys-for-a-host-using-the-idm-cli .title}

Upload a public SSH key to a host entry in Identity Management (IdM) by using the CLI so that OpenSSH can authenticate the host without Kerberos credentials.

Host SSH keys are added to host entries in IdM when the host is created using `ipa host-add`{.literal}, or by modifying the entry later using `ipa host-mod`{.literal}. RSA and DSA host keys are also created automatically by the `ipa-client-install`{.literal} command, unless the SSH service is explicitly disabled in the installation script.

**Prerequisites**

-   Administrator privileges for managing IdM or User Administrator role.

**Procedure**

1.  Run the `host-mod`{.literal} command with the `--sshpubkey`{.literal} option to upload the base64-encoded public key to the host entry.

    Because adding a host key changes the DNS Secure Shell fingerprint (SSHFP) record for the host, use the `--updatedns`{.literal} option to update the host's DNS entry. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-mod --sshpubkey="ssh-rsa RjlzYQo==" --updatedns host1.example.com
    ```

    A real key also usually ends with an equal sign (=) but is longer.

2.  To upload more than one key, enter multiple \--sshpubkey command-line parameters:

    ``` {.language-plaintext tabindex="-1"}
    --sshpubkey="RjlzYQo==" --sshpubkey="ZEt0TAo=="
    ```

    Note that a host can have multiple public keys.

3.  After uploading the host keys, configure SSSD to use Identity Management as one of its identity domains and set up OpenSSH to use the SSSD tools for managing host keys, covered in [Configuring SSSD to Provide a Cache for the OpenSSH Services](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/linux_domain_identity_authentication_and_policy_guide/openssh-sssd).

**Verification**

-   Run the `ipa host-show`{.literal} command to verify that the SSH public key is associated with the specified host:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-show client.ipa.test
    ...
    SSH public key fingerprint: SHA256:qGaqTZM60YPFTngFX0PtNPCKbIuudwf1D2LqmDeOcuA
                                  client@IPA.TEST (ssh-rsa)
    ...
    ```

#### [49.5.3. Deleting SSH keys for a host using the IdM Web UI](#deleting-ssh-keys-for-a-host-using-the-idm-web-ui) {#deleting-ssh-keys-for-a-host-using-the-idm-web-ui .title}

You can delete SSH public keys from host entries using the Identity Management (IdM) WebUI. Deleting invalid keys improves security by preventing unauthorized host authentication.

**Prerequisites**

-   Administrator privileges for managing the IdM Web UI or Host Administrator role.

**Procedure**

1.  Log into the IdM Web UI.
2.  Go to the **Identity\>Hosts** tab.
3.  Click the name of the host to edit.
4.  Under the **Host Settings** section, click **Delete** next to the SSH public key you want to remove.
5.  Click **Save** at the top of the page.

**Verification**

-   Under the **Host Settings** section, verify the key is no longer listed under **SSH public keys**.

#### [49.5.4. Deleting SSH keys for a host using the IdM CLI](#deleting-ssh-keys-for-a-host-using-the-idm-cli) {#deleting-ssh-keys-for-a-host-using-the-idm-cli .title}

You can delete SSH public keys from host entries using the Identity Management (IdM) CLI. Deleting invalid keys improves security by preventing unauthorized host authentication.

**Prerequisites**

-   Administrator privileges for managing the IdM CLI or Host Administrator role.

**Procedure**

-   To delete all SSH keys assigned to a host account, add the `--sshpubkey`{.literal} option to the `ipa host-mod`{.literal} command without specifying any key:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit admin
    $ ipa host-mod --sshpubkey= --updatedns host1.example.com
    ```

    Note that it is good practice to use the `--updatedns`{.literal} option to update the host's DNS entry.

    IdM determines the key type automatically from the key, if the type is not included in the uploaded key.

**Verification**

-   Run the `ipa host-show`{.literal} command to verify that the SSH public key is no longer associated with the specified host:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-show client.ipa.test
      Host name: client.ipa.test
      Platform: x86_64
      Operating system: 4.18.0-240.el8.x86_64
      Principal name: host/client.ipa.test@IPA.TEST
      Principal alias: host/client.ipa.test@IPA.TEST
      Password: False
      Member of host-groups: ipaservers
      Roles: helpdesk
      Member of netgroups: test
      Member of Sudo rule: test2
      Member of HBAC rule: test
      Keytab: True
      Managed by: client.ipa.test, server.ipa.test
      Users allowed to retrieve keytab: user1, user2, user3
    ```

## [Chapter 50. Configuring the domain resolution order to resolve short AD user names](#configuring-the-domain-resolution-order-to-resolve-short-ad-user-names) {#chapter-50.-configuring-the-domain-resolution-order-to-resolve-short-ad-user-names .title}

Configure IdM servers and clients to resolve short Active Directory (AD) usernames and group names without requiring fully qualified domain names. By default, AD users must specify names in the format `user_name@domain.com`{.literal}, but domain resolution order settings simplify authentication.

### [50.1. How domain resolution order works](#how-domain-resolution-order-works) {#how-domain-resolution-order-works .title}

In Identity Management (IdM) environments with an Active Directory (AD) trust, Red Hat recommends that you resolve and authenticate users and groups by specifying their fully qualified names.

For example:

-   *`<idm_username>`{.literal}*`@idm.example.com`{.literal} for IdM users from the `idm.example.com`{.literal} domain
-   *`<ad_username>`{.literal}*`@ad.example.com`{.literal} for AD users from the `ad.example.com`{.literal} domain

By default, if you perform user or group lookups using the *short name* format, such as `ad_username`{.literal}, IdM only searches the IdM domain and fails to find the AD users or groups. To resolve AD users or groups using short names, change the order in which IdM searches multiple domains by setting the `domain resolution order`{.literal} option.

You can set the domain resolution order centrally in the IdM database or in the SSSD configuration of individual clients. IdM evaluates domain resolution order in the following order of priority:

-   The local `/etc/sssd/sssd.conf`{.literal} configuration.
-   The ID view configuration.
-   The global IdM configuration.

**Important considerations**

-   You must use fully qualified usernames if the SSSD configuration on the host includes the `default_domain_suffix`{.literal} option and you want to make a request to a domain not specified with this option.
-   If you use the `domain resolution order`{.literal} option and query the `compat`{.literal} tree, you might receive multiple user IDs (UIDs).

Important

Do not use the `full_name_format`{.literal} SSSD option on IdM clients or IdM servers. Using a non-default value for this option changes how usernames are displayed and might disrupt lookups in an IdM environment.

**Additional resources**

-   [Inconsistent compat user objects for AD users when domain resolution order is set](https://pagure.io/freeipa/issue/7748)
-   [Active Directory Trust for Legacy Linux Clients](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/windows_integration_guide/trust-legacy)

### [50.2. Setting the global domain resolution order on an IdM server](#setting-the-global-domain-resolution-order-on-an-idm-server) {#setting-the-global-domain-resolution-order-on-an-idm-server .title}

Set the global domain resolution order on an Identity Management (IdM) server to control the sequence in which domains are searched when resolving user and group names across all clients in the IdM domain.

Set the domain resolution order to search for users and groups in the following order:

1.  Active Directory (AD) root domain `ad.example.com`{.literal}
2.  AD child domain `subdomain1.ad.example.com`{.literal}
3.  IdM domain `idm.example.com`{.literal}

**Prerequisites**

-   You have configured a trust with an AD environment.

**Procedure**

-   Use the `ipa config-mod --domain-resolution-order`{.literal} command to list the domains to be searched in your preferred order. Separate the domains with a colon (`:`{.literal}).

    ``` {.language-plaintext tabindex="-1"}
    [user@server ~]$ ipa config-mod --domain-resolution-order='ad.example.com:subdomain1.ad.example.com:idm.example.com'
    Maximum username length: 32
    Home directory base: /home
    ...
      Domain Resolution Order: ad.example.com:subdomain1.ad.example.com:idm.example.com
    ...
    ```

**Verification**

-   Verify you can retrieve user information for a user from the `ad.example.com`{.literal} domain using only a short name.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# id <ad_username>
    uid=1916901102(ad_username) gid=1916900513(domain users) groups=1916900513(domain users)
    ```

### [50.3. Setting the domain resolution order for an ID view on an IdM server](#setting-the-domain-resolution-order-for-an-id-view-on-an-idm-server) {#setting-the-domain-resolution-order-for-an-id-view-on-an-idm-server .title}

Set the domain resolution order for an Identity Management (IdM) ID view to control which domain is searched first when resolving user and group names on a specific set of hosts.

Create an ID view named `ADsubdomain1_first`{.literal} for the IdM host `client1.idm.example.com`{.literal} and define a specific domain resolution order. This configuration prioritizes user and group searches in the following sequence:

1.  Active Directory (AD) child domain `subdomain1.ad.example.com`{.literal}
2.  AD root domain `ad.example.com`{.literal}
3.  IdM domain `idm.example.com`{.literal}

Note

The domain resolution order set in an ID view overrides the global domain resolution order, but it does not override any domain resolution order set locally in the SSSD configuration.

**Prerequisites**

-   You have configured a trust with an AD environment.

**Procedure**

1.  Create an ID view with the `--domain-resolution-order`{.literal} option set.

    ``` {.language-plaintext tabindex="-1"}
    [user@server ~]$ ipa idview-add ADsubdomain1_first --desc "ID view for resolving AD subdomain1 first on client1.idm.example.com" --domain-resolution-order subdomain1.ad.example.com:ad.example.com:idm.example.com
    ---------------------------------
    Added ID View "ADsubdomain1_first"
    ---------------------------------
    ID View Name: ADsubdomain1_first
    Description: ID view for resolving AD subdomain1 first on client1.idm.example.com
    Domain Resolution Order: subdomain1.ad.example.com:ad.example.com:idm.example.com
    ```

2.  Apply the ID view to IdM hosts.

    ``` {.language-plaintext tabindex="-1"}
    [user@server ~]$ ipa idview-apply ADsubdomain1_first --hosts client1.idm.example.com
    -----------------------------------
    Applied ID View "ADsubdomain1_first"
    -----------------------------------
      hosts: client1.idm.example.com
    ---------------------------------------------
    Number of hosts the ID View was applied to: 1
    ---------------------------------------------
    ```

**Verification**

1.  Display the details of the ID view.

    ``` {.language-plaintext tabindex="-1"}
    [user@server ~]$ ipa idview-show ADsubdomain1_first --show-hosts
      ID View Name: ADsubdomain1_first
      Description: ID view for resolving AD subdomain1 first on client1.idm.example.com
      Hosts the view applies to: client1.idm.example.com
      Domain resolution order: subdomain1.ad.example.com:ad.example.com:idm.example.com
    ```

2.  Verify you can retrieve user information for a user from the `subdomain1.ad.example.com`{.literal} domain using only a short name.

    ``` {.language-plaintext tabindex="-1"}
    [root@client1 ~]# id <user_from_subdomain1>
    uid=1916901106(user_from_subdomain1) gid=1916900513(domain users) groups=1916900513(domain users)
    ```

### [50.4. Using Ansible to create an ID view with a domain resolution order](#using-ansible-to-create-an-id-view-with-a-domain-resolution-order) {#using-ansible-to-create-an-id-view-with-a-domain-resolution-order .title}

Use the `ansible-freeipa`{.literal} `idview`{.literal} module to add, modify, and delete ID views in your Identity Management (IdM) deployment. For example, you can create an ID view with a domain resolution order to enable short name notation.

Short name notation substitutes a full user name from Active Directory (AD), such as **aduser05@ad.example.com**, with a short login, in this case **aduser05**. That means that when using `SSH`{.literal} to log in to an IdM client, **aduser05** can enter `ssh`{.literal} aduser05@client.idm.example.com instead of `ssh`{.literal} aduser05@ad.example.com@client.idm.example.com. The same applies to other commands, such as `id`{.literal}.

Complete this procedure to use Ansible to:

-   Define a string of colon-separated domains used for short name qualification. In the example, the string is **ad.example.com:idm.example.com**.
-   Create an ID view that instructs SSSD to first search a user name in the first domain identified in the string. In the example, this is **ad.example.com**.
-   Apply the ID view to a specific host. In the example, this is **testhost.idm.example.com**.

Note

You can apply only one ID view to an IdM client. Applying a new ID view automatically removes the previous ID view, if applicable.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to your **\~/MyPlaybooks/** directory and create an Ansible playbook file **add-id-view-with-domain-resolution-order.yml** with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to add idview and apply it to an IdM client
      hosts: ipaserver
      vars_files:
      - /home/<user_name>/MyPlaybooks/secret.yml
      become: false
      gather_facts: false

      tasks:
      - name: Add idview and apply it to testhost.idm.example.com
        ipaidview:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: test_idview
          host: testhost.idm.example.com
          domain_resolution_order: "ad.example.com:ipa.example.com"
    ```

2.  Run the playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory add-id-view-with-domain-resolution-order.yml
    ```

**Verification**

1.  SSH to **testhost.idm.example.com**.

2.  Verify you can retrieve user information for a user from the **ad.example.com** domain using only a short name.

    ``` {.language-plaintext tabindex="-1"}
    [root@testhost ~]# id aduser05
    uid=1916901102(aduser05) gid=1916900513(domain users) groups=1916900513(domain users)
    ```

**Additional resources**

-   [The idview module in `ansible-freeipa`{.literal} upstream docs](https://github.com/freeipa/ansible-freeipa/blob/master/README-idview.md)

### [50.5. Setting the domain resolution order in SSSD on an IdM client](#setting-the-domain-resolution-order-in-sssd-on-an-idm-client) {#setting-the-domain-resolution-order-in-sssd-on-an-idm-client .title}

Set the domain resolution order in the SSSD configuration on an Identity Management (IdM) client to control which domain is searched first when resolving user and group names on that specific host.

Configure IdM host `client2.idm.example.com`{.literal} to prioritize user and group lookups by defining a specific domain resolution order. Establishing this sequence ensures the host queries domains in the following order:

1.  Active Directory (AD) child domain `subdomain1.ad.example.com`{.literal}
2.  AD root domain `ad.example.com`{.literal}
3.  IdM domain `idm.example.com`{.literal}

Note

The domain resolution order in the local SSSD configuration overrides any global and ID view domain resolution order.

**Prerequisites**

-   You have configured a trust with an AD environment.

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} file in a text editor.

2.  Set the `domain_resolution_order`{.literal} option in the `[sssd]`{.literal} section of the file.

    ``` {.language-plaintext tabindex="-1"}
    domain_resolution_order = subdomain1.ad.example.com, ad.example.com, idm.example.com
    ```

3.  Save and close the file.

4.  Restart the SSSD service to load the new configuration settings.

    ``` {.language-plaintext tabindex="-1"}
    [root@client2 ~]# systemctl restart sssd
    ```

**Verification**

-   Verify you can retrieve user information for a user from the `subdomain1.ad.example.com`{.literal} domain using only a short name.

    ``` {.language-plaintext tabindex="-1"}
    [root@client2 ~]# id <user_from_subdomain1>
    uid=1916901106(user_from_subdomain1) gid=1916900513(domain users) groups=1916900513(domain users)
    ```

### [50.6. Additional resources](#configuring-the-domain-resolution-order-to-resolve-short-ad-user-names_506-additional-resources) {#additional-resources-23 .title}

-   [Using an ID view to override a user attribute value on an IdM client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/using-an-id-view-to-override-a-user-attribute-value-on-an-idm-client)

## [Chapter 51. Enabling authentication using AD User Principal Names in IdM](#enabling-authentication-using-ad-user-principal-names-in-idm) {#chapter-51.-enabling-authentication-using-ad-user-principal-names-in-idm .title}

Enable Active Directory (AD) users to authenticate to Identity Management (IdM) using their User Principal Names (UPNs). This simplifies authentication in trusted AD forest environments by supporting UPN-based login.

### [51.1. User principal names in an AD forest trusted by IdM](#user-principal-names-in-an-ad-forest-trusted-by-idm) {#user-principal-names-in-an-ad-forest-trusted-by-idm .title}

Active Directory (AD) users in an Identity Management (IdM) trust can use alternative User Principal Names (UPNs) to authenticate --- for example, their email address instead of the default Kerberos realm login --- by configuring additional UPN suffixes in the AD forest root.

For example, if a company uses the Kerberos realm **AD.EXAMPLE.COM**, the default UPN for a user is `user@ad.example.com`{.literal}. To allow your users to log in using their email addresses, for example `user@`{.literal}**`example.com`{.literal}**, you can configure `EXAMPLE.COM`{.literal} as an alternative UPN in AD. Alternative UPNs (also known as *enterprise UPNs*) are especially convenient if your company has recently experienced a merge and you want to provide your users with a unified logon namespace.

UPN suffixes are only visible for IdM when defined in the AD forest root. As an AD administrator, you can define UPNs with the `Active Directory Domain and Trust`{.literal} utility or the `PowerShell`{.literal} command line tool.

Note

To configure UPN suffixes for users, Red Hat recommends to use tools that perform error validation, such as the `Active Directory Domain and Trust`{.literal} utility.

Red Hat recommends against configuring UPNs through low-level modifications, such as using `ldapmodify`{.literal} commands to set the `userPrincipalName`{.literal} attribute for users, because Active Directory does not validate those operations.

After you define a new UPN on the AD side, run the `ipa trust-fetch-domains`{.literal} command on an IdM server to retrieve the updated UPNs.

IdM stores the UPN suffixes for a domain in the multi-value attribute `ipaNTAdditionalSuffixes`{.literal} of the subtree `cn=trusted_domain_name,cn=ad,cn=trusts,dc=idm,dc=example,dc=com`{.literal}.

**Additional resources**

-   [Ensuring that AD UPNs are up-to-date in IdM](#ensuring-that-ad-upns-are-up-to-date-in-idm "51.2. Ensuring that AD UPNs are up-to-date in IdM")
-   [How to script UPN suffix setup in AD forest root](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adforest)
-   [How to manually modify AD user entries and bypass any UPN suffix validation](https://learn.microsoft.com/en-us/microsoft-365/enterprise/prepare-for-directory-synchronization)
-   [Trust controllers and trust agents](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-a-cross-forest-trust-between-idm-and-ad#trust-controllers-and-trust-agents)

### [51.2. Ensuring that AD UPNs are up-to-date in IdM](#ensuring-that-ad-upns-are-up-to-date-in-idm) {#ensuring-that-ad-upns-are-up-to-date-in-idm .title}

Refresh trusted Active Directory forest information in Identity Management (IdM) after modifying User Principal Name (UPN) suffixes to ensure IdM recognizes updated authentication credentials. This keeps your trust configuration synchronized with Active Directory changes.

**Prerequisites**

-   IdM administrator credentials.

**Procedure**

-   Enter the `ipa trust-fetch-domains`{.literal} command. Note that a seemingly empty output is expected:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# ipa trust-fetch-domains
    Realm-Name: ad.example.com
    -------------------------------
    No new trust domains were found
    -------------------------------
    ----------------------------
    Number of entries returned 0
    ----------------------------
    ```

**Verification**

-   Enter the `ipa trust-show`{.literal} command to verify that the server has fetched the new UPN. Specify the name of the AD realm when prompted:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# ipa trust-show
    Realm-Name: ad.example.com
      Realm-Name: ad.example.com
      Domain NetBIOS name: AD
      Domain Security Identifier: S-1-5-21-796215754-1239681026-23416912
      Trust direction: One-way trust
      Trust type: Active Directory domain
      UPN suffixes: example.com
    ```

    The output shows that the `example.com`{.literal} UPN suffix is now part of the `ad.example.com`{.literal} realm entry.

### [51.3. Gathering troubleshooting data for AD UPN authentication issues](#gathering-troubleshooting-data-for-ad-upn-authentication-issues) {#gathering-troubleshooting-data-for-ad-upn-authentication-issues .title}

Collect detailed User Principal Name (UPN) configuration logs from Active Directory (AD) and Identity Management (IdM) environments to diagnose authentication failures with alternate UPNs. This data helps identify misconfigurations in trust relationships.

**Prerequisites**

-   You must be logged in to an IdM Trust Controller or Trust Agent to retrieve information from an AD domain controller.
-   You need `root`{.literal} permissions to modify the following configuration files, and to restart IdM services.

**Procedure**

1.  Open the `/usr/share/ipa/smb.conf.empty`{.literal} configuration file in a text editor.

2.  Add the following contents to the file.

    ``` {.language-plaintext tabindex="-1"}
    [global]
    log level = 10
    ```

3.  Save and close the `/usr/share/ipa/smb.conf.empty`{.literal} file.

4.  Open the `/etc/ipa/server.conf`{.literal} configuration file in a text editor. If you do not have that file, create one.

5.  Add the following contents to the file.

    ``` {.language-plaintext tabindex="-1"}
    [global]
    debug = True
    ```

6.  Save and close the `/etc/ipa/server.conf`{.literal} file.

7.  Restart the Apache webserver service to apply the configuration changes:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl restart httpd
    ```

8.  Retrieve trust information from your AD domain:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa trust-fetch-domains <ad.example.com>
    ```

9.  Review the debugging output and troubleshooting information in the following log files:

    -   `/var/log/httpd/error_log`{.literal}
    -   `/var/log/samba/log.*`{.literal}

**Additional resources**

-   [Using rpcclient to gather troubleshooting data for AD UPN authentication issues (Red Hat Knowledgebase)](https://access.redhat.com/solutions/5825651)

## [Chapter 52. Enabling AD users to administer IdM](#enabling-ad-users-to-administer-idm) {#chapter-52.-enabling-ad-users-to-administer-idm .title}

Grant Active Directory (AD) users administrative privileges in Identity Management (IdM) by using ID overrides. This allows trusted AD users to perform IdM administrative tasks without creating separate IdM accounts.

### [52.1. ID overrides for AD users](#id-overrides-for-ad-users) {#id-overrides-for-ad-users .title}

ID overrides let Active Directory (AD) users access Identity Management (IdM) resources and self-service features --- such as uploading SSH keys --- without a separate IdM account, by representing the AD user as a member of an IdM group.

An ID override is a record describing what a specific Active Directory user or group properties should look like within a specific ID view, in this case the **Default Trust View**. With this feature, the IdM LDAP server is able to apply access control rules for the IdM group to the AD user.

AD users can use the self service features of IdM UI, for example to upload their SSH keys, or change their personal data. An AD administrator is able to fully administer IdM without having two different accounts and passwords.

Note

Currently, selected features in IdM may still be unavailable to AD users. For example, setting passwords for IdM users as an AD user from the IdM `admins`{.literal} group might fail.

Important

Do **not** use ID overrides of AD users for `sudo`{.literal} rules in IdM. ID overrides of AD users represent only POSIX attributes of AD users, not AD users themselves.

**Additional resources**

-   [Using ID views for Active Directory users](#using-id-views-for-active-directory-users "Chapter 38. Using ID views for Active Directory users")

### [52.2. Using ID overrides to enable AD users to administer IdM](#using-id-overrides-to-enable-ad-users-to-administer-idm) {#using-id-overrides-to-enable-ad-users-to-administer-idm .title}

Create an ID override for an Active Directory (AD) user in the Default Trust View of Identity Management (IdM) to grant that AD user the same administrative rights as an IdM user.

**Prerequisites**

-   A working IdM environment is set up. For details, see [Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/index).
-   A working trust between your IdM environment and AD is set up.
-   You are working on an IdM server configured as a trust controller or a trust agent.

**Procedure**

1.  As an IdM administrator, create an ID override for an AD user in the **Default Trust View**. For example, to create an ID override for the user `ad_user@ad.example.com`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # kinit admin
    # ipa idoverrideuser-add 'default trust view' ad_user@ad.example.com
    ```

2.  Add the ID override from the **Default Trust View** as a member of an IdM group. This must be a non-POSIX group, as it interacts with Active Directory.

    If the group in question is a member of an IdM role, the AD user represented by the ID override gains all permissions granted by the role when using the IdM API, including both the command-line interface and the IdM web UI.

    For example, to add the ID override for the `ad_user@ad.example.com`{.literal} user to the IdM `admins`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    # ipa group-add-member admins --idoverrideusers=ad_user@ad.example.com
    ```

3.  Alternatively, you can add the ID override to a role, such as the **User Administrator** role:

    ``` {.language-plaintext tabindex="-1"}
    # ipa role-add-member 'User Administrator' --idoverrideusers=ad_user@ad.example.com
    ```

**Additional resources**

-   [Using ID views for Active Directory users](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/using-id-views-for-active-directory-users)

### [52.3. Verifying that an AD user can perform correct commands in the IdM CLI](#verifying-that-an-ad-user-can-perform-correct-commands-in-the-idm-cli) {#verifying-that-an-ad-user-can-perform-correct-commands-in-the-idm-cli .title}

Verify that an Active Directory (AD) user can log in to Identity Management (IdM) by using the CLI and perform operations that match the user's assigned IdM role.

**Procedure**

1.  Destroy the current Kerberos ticket of the IdM administrator:

    ``` {.language-plaintext tabindex="-1"}
    # kdestroy -A
    ```

    Note

    The destruction of the Kerberos ticket is required because the GSSAPI implementation in MIT Kerberos chooses credentials from the realm of the target service by preference, which in this case is the IdM realm. This means that if a credentials cache collection, namely the `KCM:`{.literal}, `KEYRING:`{.literal}, or `DIR:`{.literal} type of credentials cache is in use, a previously obtained `admin`{.literal} or any other IdM principal's credentials will be used to access the IdM API instead of the AD user's credentials.

2.  Obtain the Kerberos credentials of the AD user for whom an ID override has been created:

    ``` {.language-plaintext tabindex="-1"}
    # kinit ad_user@AD.EXAMPLE.COM
    Password for ad_user@AD.EXAMPLE.COM:
    ```

3.  Test that the ID override of the AD user enjoys the same privileges stemming from membership in the IdM group as any IdM user in that group. If the ID override of the AD user has been added to the `admins`{.literal} group, the AD user can, for example, create groups in IdM:

    ``` {.language-plaintext tabindex="-1"}
    # ipa group-add some-new-group
    ----------------------------
    Added group "some-new-group"
    ----------------------------
      Group name: some-new-group
      GID: 1997000011
    ```

### [52.4. Using Ansible to enable an AD user to administer IdM](#using-ansible-to-enable-an-ad-user-to-administer-idm) {#using-ansible-to-enable-an-ad-user-to-administer-idm .title}

Use the `ansible-freeipa`{.literal} `idoverrideuser`{.literal} and `group`{.literal} modules to grant an AD user from a trusted domain full Identity Management (IdM) administration rights without maintaining separate accounts.

The procedure uses the example of the `Default Trust View`{.literal} ID view to which the **ad_user@AD.EXAMPLE.COM** ID override is added in the first playbook task. In the next playbook task, the [ad_user@AD.EXAMPLE.COM](mailto:ad_user@AD.EXAMPLE.COM) ID override is added to the IdM `admins`{.literal} group as a member.

**Prerequisites**

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The `ipaserver`{.literal} host in the inventory file is configured as a trust controller or a trust agent.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  On your Ansible control node, create an **enable-ad-admin-to-administer-idm.yml** playbook with a task to add the **ad_user@ad.example.com** user override to the Default Trust View:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Enable AD administrator to act as a FreeIPA admin
      hosts: ipaserver
      become: false
      gather_facts: false

      tasks:
      - name: Ensure idoverride for ad_user@ad.example.com in 'Default Trust View'
        ipaidoverrideuser:
          ipaadmin_password: "{{ ipaadmin_password }}"
          idview: "Default Trust View"
          anchor: ad_user@ad.example.com
    ```

    In the example:

    -   **ad_user@ad.example.com** is the user ID override of an AD user that is stored in the AD domain with which a trust has been established.

2.  Use another playbook task in the same playbook to add the AD administrator user ID override to the `admins`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
      - name: Add the AD administrator as a member of admins
        ipagroup:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: admins
          idoverrideuser:
          - ad_user@ad.example.com
    ```

    In the example:

    -   `admins`{.literal} is the name of the default IdM POSIX group to which you are adding the **ad_user@ad.example.com** ID override. Members of this group have full administrator privileges.

3.  Save the file.

4.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory enable-ad-admin-to-administer-idm.yml
    ```

**Verification**

1.  Log in to the IdM client as the AD Administrator:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh ad_user@ad.example.com@client.idm.example.com
    ```

2.  Verify that you have obtained a valid ticket-granting ticket (TGT):

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    Ticket cache: KCM:325600500:99540
    Default principal: ad_user@AD.EXAMPLE.COM
    Valid starting Expires Service principal
    02/04/2024 11:54:16 02/04/2024 21:54:16 krbtgt/AD.EXAMPLE.COM@AD.EXAMPLE.COM
    renew until 02/05/2024 11:54:16
    ```

3.  Verify your `admin`{.literal} privileges in IdM:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-add testuser --first=test --last=user
    ------------------------
    Added user "tuser"
    ------------------------
      User login: tuser
      First name: test
      Last name: user
      Full name: test user
    [...]
    ```

**Additional resources**

-   [idoverrideuser](https://github.com/freeipa/ansible-freeipa/blob/master/README-idoverrideuser.md)
-   [ipagroup](https://github.com/freeipa/ansible-freeipa/blob/master/README-group.md)
-   [Enabling AD users to administer IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/enabling-ad-users-to-administer-idm)

## [Chapter 53. Using external identity providers to authenticate to IdM](#using-external-identity-providers-to-authenticate-to-idm) {#chapter-53.-using-external-identity-providers-to-authenticate-to-idm .title}

You can associate users with external identity providers (IdP) that support the OAuth 2 device authorization flow.

When these users authenticate with the SSSD they receive RHEL Identity Management (IdM) single sign-on capabilities with Kerberos tickets after performing authentication and authorization at the external IdP.

Notable features include:

-   Adding, modifying, and deleting references to external IdPs with `ipa idp-*`{.literal} commands.

-   Enabling IdP authentication for users with the `ipa user-mod --user-auth-type=idp`{.literal} command.

    What is supported

    :   

-   Logging in remotely via SSH with the `keyboard-interactive`{.literal} authentication method enabled, which allows calling Pluggable Authentication Module (PAM) libraries.

-   Logging in locally with the console through the `logind`{.literal} service.

-   Retrieving a Kerberos ticket-granting ticket (TGT) with the `kinit`{.literal} utility.

    What is currently not supported

    :   

-   Logging in to the IdM WebUI directly. To log in to the IdM WebUI, you must first acquire a Kerberos ticket.

-   Logging in to Cockpit WebUI directly. To log in to the Cockpit WebUI, you must first acquire a Kerberos ticket.

### [53.1. The benefits of connecting IdM to an external IdP](#the-benefits-of-connecting-idm-to-an-external-idp) {#the-benefits-of-connecting-idm-to-an-external-idp .title}

You can delegate Kerberos ticket issuance to an external identity provider (IdP) so that users from external sources, such as cloud services, can access RHEL systems in your Identity Management (IdM) environment.

You can use this feature to expand IdM's capabilities and allow users stored in external identity providers (IdPs) to access Linux systems managed by IdM.

### [53.2. How IdM incorporates logins via external IdPs](#how-idm-incorporates-logins-via-external-idps) {#how-idm-incorporates-logins-via-external-idps .title}

SSSD 2.7.0 contains the `sssd-idp`{.literal} package, which implements the `idp`{.literal} Kerberos pre-authentication method. This authentication method follows the OAuth 2.0 Device Authorization Grant flow to delegate authorization decisions to external IdPs:

1.  An IdM client user initiates OAuth 2.0 Device Authorization Grant flow, for example, by attempting to retrieve a Kerberos TGT with the `kinit`{.literal} utility at the command line.

2.  A special code and website link are sent from the Authorization Server to the IdM KDC backend.

3.  The IdM client displays the link and the code to the user. In this example, the IdM client outputs the link and code on the command line.

4.  The user opens the website link in a browser, which can be on another host, a mobile phone, and so on:

    a.  The user enters the special code.
    b.  If necessary, the user logs in to the OAuth 2.0-based IdP.
    c.  The user is prompted to authorize the client to access information.

5.  The user confirms access at the original device prompt. In this example, the user hits the Enter key at the command line.

6.  The IdM KDC backend polls the OAuth 2.0 Authorization Server for access to user information.

**Additional resources**

-   [Authentication against external identity providers](https://freeipa.readthedocs.io/en/latest/workshop/12-external-idp-support.html)
-   [RFC 8628: OAuth 2.0 Device Authorization Grant](https://www.rfc-editor.org/rfc/rfc8628)

### [53.3. Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider) {#creating-a-reference-to-an-external-identity-provider .title}

You can create IdP references in IdM to connect external identity providers (IdPs) to your Identity Management (IdM) environment. You can create a reference called **my-keycloak-idp** to an IdP based on the Keycloak template. For more reference templates, see [Example references to different external IdPs in IdM](#example-references-to-different-external-idps-in-idm "53.4. Example references to different external IdPs in IdM").

**Prerequisites**

-   You have registered IdM as an OAuth application to your external IdP, and obtained a client ID.
-   You can authenticate as the IdM admin account.

**Procedure**

1.  Authenticate as the IdM admin on an IdM server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit admin
    ```

2.  Create a reference called `my-keycloak-idp`{.literal} to an IdP based on the Keycloak template, where the `--base-url`{.literal} option specifies the URL to the Keycloak server in the format `server-name.$DOMAIN:$PORT/prefix`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idp-add my-keycloak-idp \
                     --provider keycloak --organization main \
                     --base-url keycloak.idm.example.com:8443/auth \
                     --client-id id13778
    ------------------------------------------------
    Added Identity Provider reference "my-keycloak-idp"
    ------------------------------------------------
      Identity Provider reference name: my-keycloak-idp
      Authorization URI: https://keycloak.idm.example.com:8443/auth/realms/main/protocol/openid-connect/auth
      Device authorization URI: https://keycloak.idm.example.com:8443/auth/realms/main/protocol/openid-connect/auth/device
      Token URI: https://keycloak.idm.example.com:8443/auth/realms/main/protocol/openid-connect/token
      User info URI: https://keycloak.idm.example.com:8443/auth/realms/main/protocol/openid-connect/userinfo
      Client identifier: ipa_oidc_client
      Scope: openid email
      External IdP user identifier attribute: email
    ```

**Verification**

-   Verify that the output of the `ipa idp-show`{.literal} command shows the IdP reference you have created.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idp-show my-keycloak-idp
    ```

**Additional resources**

-   [Example references to different external IdPs in IdM](#example-references-to-different-external-idps-in-idm "53.4. Example references to different external IdPs in IdM")
-   [Options for the ipa idp-\* commands to manage external identity providers in IdM](#options-for-the-ipa-idp-commands-to-manage-external-identity-providers-in-idm "53.5. Options for the ipa idp-* commands to manage external identity providers in IdM")
-   [The \--provider option in the ipa idp-\* commands](#the-provider-option-in-the-ipa-idp-commands "53.10. The --provider option in the ipa idp-* commands")

### [53.4. Example references to different external IdPs in IdM](#example-references-to-different-external-idps-in-idm) {#example-references-to-different-external-idps-in-idm .title}

The following table lists examples of the `ipa idp-add`{.literal} command for creating references to different IdPs in IdM.

+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Identity provider                               | Important options                | Command example                                                                                                                                                                                                                               |
+:================================================+:=================================+:==============================================================================================================================================================================================================================================+
| Microsoft Identity Platform, Microsoft Entra ID | `--provider microsoft`{.literal} | `# ipa idp-add my-entra-id-idp \ --provider microsoft \ --organization main \ --client-id <entra_client_id>`{.literallayout}                                                                                                                  |
|                                                 |                                  |                                                                                                                                                                                                                                               |
|                                                 | `--organization`{.literal}       |                                                                                                                                                                                                                                               |
+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Google                                          | `--provider google`{.literal}    | `# ipa idp-add my-google-idp \ --provider google \ --client-id <google_client_id>`{.literallayout}                                                                                                                                            |
+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GitHub                                          | `--provider github`{.literal}    | `# ipa idp-add my-github-idp \ --provider github \ --client-id <github_client_id>`{.literallayout}                                                                                                                                            |
+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keycloak, Red Hat Single Sign-On                | `--provider keycloak`{.literal}  | `# ipa idp-add my-keycloak-idp \ --provider keycloak \ --organization main \ --base-url keycloak.idm.example.com:8443/auth \ --client-id <keycloak_client_id>`{.literallayout}                                                                |
|                                                 |                                  |                                                                                                                                                                                                                                               |
|                                                 | `--organization`{.literal}       | Note                                                                                                                                                                                                                                          |
|                                                 |                                  |                                                                                                                                                                                                                                               |
|                                                 | `--base-url`{.literal}           | The Quarkus version of Keycloak 17 and later have removed the `/auth/`{.literal} portion of the URI. If you use the non-Quarkus distribution of Keycloak in your deployment, include `/auth/`{.literal} in the `--base-url`{.literal} option. |
+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Okta                                            | `--provider okta`{.literal}      | `# ipa idp-add my-okta-idp \ --provider okta --base-url dev-12345.okta.com \ --client-id <okta_client_id>`{.literallayout}                                                                                                                    |
+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

**Additional resources**

-   [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "53.3. Creating a reference to an external identity provider")
-   [Options for the ipa idp-\* commands to manage external identity providers in IdM](#options-for-the-ipa-idp-commands-to-manage-external-identity-providers-in-idm "53.5. Options for the ipa idp-* commands to manage external identity providers in IdM")
-   [The \--provider option in the ipa idp-\* commands](#the-provider-option-in-the-ipa-idp-commands "53.10. The --provider option in the ipa idp-* commands")
-   [Configure IdM to use Google as external IdP (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7073951)
-   [Configure IdM to use Microsoft Entra ID as external IdP (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7073948)
-   [Configure IdM to use GitHub as external IdP (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7072954)

### [53.5. Options for the ipa idp-\* commands to manage external identity providers in IdM](#options-for-the-ipa-idp-commands-to-manage-external-identity-providers-in-idm) {#options-for-the-ipa-idp--commands-to-manage-external-identity-providers-in-idm .title}

The following examples show how to configure references to external IdPs based on the different IdP templates. Use the following options to specify your settings:

`--provider`{.literal}
:   the predefined template for one of the known identity providers

`--client-id`{.literal}
:   the OAuth 2.0 client identifier issued by the IdP during application registration. As the application registration procedure is specific to each IdP, refer to their documentation for details. If the external IdP is Red Hat Single Sign-On (SSO), see [Creating an OpenID Connect Client](https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html-single/server_administration_guide/index#proc-creating-oidc-client_server_administration_guide).

`--base-url`{.literal}
:   base URL for IdP templates, required by Keycloak and Okta

`--organization`{.literal}
:   Domain or Organization ID from the IdP, required by Microsoft Entra ID

`--secret`{.literal}
:   *(optional)* Use this option if you have configured your external IdP to require a secret from confidential OAuth 2.0 clients. If you use this option when creating an IdP reference, you are prompted for the secret interactively. Protect the client secret as a password.

**Additional resources**

-   [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "53.3. Creating a reference to an external identity provider")
-   [Example references to different external IdPs in IdM](#example-references-to-different-external-idps-in-idm "53.4. Example references to different external IdPs in IdM")
-   [The \--provider option in the ipa idp-\* commands](#the-provider-option-in-the-ipa-idp-commands "53.10. The --provider option in the ipa idp-* commands")

### [53.6. Managing references to external IdPs](#managing-references-to-external-idps) {#managing-references-to-external-idps .title}

After you create a reference to an external identity provider (IdP), you can find, show, modify, and delete that reference. This example shows you how to manage a reference to an external IdP named `keycloak-server1`{.literal}.

**Prerequisites**

-   You can authenticate as the IdM admin account.
-   You have created a reference to an external IdP in IdM. See [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "53.3. Creating a reference to an external identity provider").

**Procedure**

1.  Authenticate as the IdM admin on an IdM server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit admin
    ```

2.  Manage the IdP reference.

    -   To find an IdP reference whose entry includes the string `keycloak`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa idp-find keycloak
        ```

    -   To display an IdP reference named `my-keycloak-idp`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa idp-show my-keycloak-idp
        ```

    -   To modify an IdP reference, use the `ipa idp-mod`{.literal} command. For example, to change the secret for an IdP reference named `my-keycloak-idp`{.literal}, specify the `--secret`{.literal} option to be prompted for the secret:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa idp-mod my-keycloak-idp --secret
        ```

    -   To delete an IdP reference named `my-keycloak-idp`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa idp-del my-keycloak-idp
        ```

### [53.7. Enabling an IdM user to authenticate via an external IdP](#enabling-an-idm-user-to-authenticate-via-an-external-idp) {#enabling-an-idm-user-to-authenticate-via-an-external-idp .title}

To enable an IdM user to authenticate via an external identity provider (IdP), associate the external IdP reference you have previously created with the user account. This example associates the external IdP reference `keycloak-server1`{.literal} with the user `idm-user-with-external-idp`{.literal}.

**Prerequisites**

-   You have created a reference to an external IdP in IdM. See [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "53.3. Creating a reference to an external identity provider").

**Procedure**

-   Modify the IdM user entry to associate an IdP reference with the user account:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa user-mod idm-user-with-external-idp \
                   --idp my-keycloak-idp \
                   --idp-user-id idm-user-with-external-idp@idm.example.com \
                   --user-auth-type=idp
    ---------------------------------
    Modified user "idm-user-with-external-idp"
    ---------------------------------
      User login: idm-user-with-external-idp
      First name: Test
      Last name: User1
      Home directory: /home/idm-user-with-external-idp
      Login shell: /bin/sh
      Principal name: idm-user-with-external-idp@idm.example.com
      Principal alias: idm-user-with-external-idp@idm.example.com
      Email address: idm-user-with-external-idp@idm.example.com
      UID: 35000003
      GID: 35000003
      User authentication types: idp
      External IdP configuration: keycloak
      External IdP user identifier: idm-user-with-external-idp@idm.example.com
      Account disabled: False
      Password: False
      Member of groups: ipausers
      Kerberos keys available: False
    ```

**Verification**

-   Verify that the output of the `ipa user-show`{.literal} command for that user displays references to the IdP:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa user-show idm-user-with-external-idp
      User login: idm-user-with-external-idp
      First name: Test
      Last name: User1
      Home directory: /home/idm-user-with-external-idp
      Login shell: /bin/sh
      Principal name: idm-user-with-external-idp@idm.example.com
      Principal alias: idm-user-with-external-idp@idm.example.com
      Email address: idm-user-with-external-idp@idm.example.com
      ID: 35000003
      GID: 35000003
      User authentication types: idp
      External IdP configuration: keycloak
      External IdP user identifier: idm-user-with-external-idp@idm.example.com
      Account disabled: False
      Password: False
      Member of groups: ipausers
      Kerberos keys available: False
    ```

### [53.8. Retrieving an IdM ticket-granting ticket as an external IdP user](#retrieving-an-idm-ticket-granting-ticket-as-an-external-idp-user) {#retrieving-an-idm-ticket-granting-ticket-as-an-external-idp-user .title}

If you have delegated authentication for an Identity Management (IdM) user to an external identity provider (IdP), the IdM user can request a Kerberos ticket-granting ticket (TGT) by authenticating to the external IdP.

Complete this procedure to:

1.  Retrieve and store an anonymous Kerberos ticket locally.
2.  Request the TGT for the **idm-user-with-external-idp** user by using `kinit`{.literal} with the `-T`{.literal} option to enable Flexible Authentication via Secure Tunneling (FAST) channel to provide a secure connection between the Kerberos client and Kerberos Distribution Center (KDC).

**Prerequisites**

-   You have created a reference to an external IdP in IdM. See [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "53.3. Creating a reference to an external identity provider").
-   You have associated an external IdP reference with the user account. See [Enabling an IdM user to authenticate via an external IdP](#enabling-an-idm-user-to-authenticate-via-an-external-idp "53.7. Enabling an IdM user to authenticate via an external IdP").
-   The user that you are initially logged in as has write permissions on a directory in the local filesystem.

**Procedure**

1.  Use Anonymous PKINIT to obtain a Kerberos ticket and store it in a file named `./fast.ccache`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    $ kinit -n -c ./fast.ccache
    ```

2.  Optional: View the retrieved ticket:

    ``` {.language-plaintext tabindex="-1"}
    $ klist -c fast.ccache
    Ticket cache: FILE:fast.ccache
    Default principal: WELLKNOWN/ANONYMOUS@WELLKNOWN:ANONYMOUS

    Valid starting       Expires              Service principal
    03/03/2024 13:36:37  03/04/2024 13:14:28  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    ```

3.  Begin authenticating as the IdM user, using the `-T`{.literal} option to enable the FAST communication channel.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# kinit -T ./fast.ccache idm-user-with-external-idp
    Authenticate at https://oauth2.idp.com:8443/auth/realms/master/device?user_code=YHMQ-XKTL and press ENTER.:
    ```

4.  In a browser, authenticate as the user at the website provided in the command output.

5.  At the command line, press the Enter key to finish the authentication process.

**Verification**

-   Display your Kerberos ticket information and confirm that the line `config: pa_type`{.literal} shows `152`{.literal} for pre-authentication with an external IdP.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# klist -C
    Ticket cache: KCM:0:58420
    Default principal: idm-user-with-external-idp@IDM.EXAMPLE.COM

    Valid starting     Expires            Service principal
    05/09/22 07:48:23  05/10/22 07:03:07  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: fast_avail(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = yes
    08/17/2022 20:22:45  08/18/2022 20:22:43  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: pa_type(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = 152
    ```

    The `pa_type = 152`{.literal} indicates external IdP authentication.

### [53.9. Logging in to an IdM client via SSH as an external IdP user](#logging-in-to-an-idm-client-via-ssh-as-an-external-idp-user) {#logging-in-to-an-idm-client-via-ssh-as-an-external-idp-user .title}

To log in to an IdM client by using SSH as an external identity provider (IdP) user, begin the login process on the command line. When prompted, authenticate at the website associated with the IdP, and finish the process at the Identity Management (IdM) client.

**Prerequisites**

-   You have created a reference to an external IdP in IdM. See [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "53.3. Creating a reference to an external identity provider").
-   You have associated an external IdP reference with the user account. See [Enabling an IdM user to authenticate via an external IdP](#enabling-an-idm-user-to-authenticate-via-an-external-idp "53.7. Enabling an IdM user to authenticate via an external IdP").

**Procedure**

1.  Attempt to log in to the IdM client via SSH.

    ``` {.language-plaintext tabindex="-1"}
    [user@client ~]$ ssh idm-user-with-external-idp@client.idm.example.com
    (idm-user-with-external-idp@client.idm.example.com) Authenticate at https://oauth2.idp.com:8443/auth/realms/main/device?user_code=XYFL-ROYR and press ENTER.
    ```

2.  In a browser, authenticate as the user at the website provided in the command output.

3.  At the command line, press the Enter key to finish the authentication process.

**Verification**

-   Display your Kerberos ticket information and confirm that the line `config: pa_type`{.literal} shows `152`{.literal} for pre-authentication with an external IdP.

    ``` {.language-plaintext tabindex="-1"}
    [idm-user-with-external-idp@client ~]$ klist -C
    Ticket cache: KCM:0:58420
    Default principal: idm-user-with-external-idp@IDM.EXAMPLE.COM

    Valid starting     Expires            Service principal
    05/09/22 07:48:23  05/10/22 07:03:07  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: fast_avail(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = yes
    08/17/2022 20:22:45  08/18/2022 20:22:43  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: pa_type(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = 152
    ```

### [53.10. The \--provider option in the ipa idp-\* commands](#the-provider-option-in-the-ipa-idp-commands) {#the---provider-option-in-the-ipa-idp--commands .title}

The following identity providers (IdPs) support OAuth 2.0 device authorization grant flow:

-   Microsoft Identity Platform, Microsoft Entra ID
-   Google
-   GitHub
-   Keycloak, including Red Hat Single Sign-On (SSO)
-   Okta

When using the `ipa idp-add`{.literal} command to create a reference to one of these external IdPs, you can specify the IdP type with the `--provider`{.literal} option, which expands into additional options as described below:

`--provider=microsoft`{.literal}

:   Microsoft Entra ID IdPs allow parametrization based on the Microsoft Entra ID tenant ID, which you can specify with the `--organization`{.literal} option to the `ipa idp-add`{.literal} command. If you need support for the live.com IdP, specify the option `--organization common`{.literal}.

    Choosing `--provider=microsoft`{.literal} expands to use the following options. The value of the `--organization`{.literal} option replaces the string `${ipaidporg}`{.literal} in the table.

    +--------------------------------+-----------------------------------------------------------------------------------+
    | Option                         | Value                                                                             |
    +:===============================+:==================================================================================+
    | `--auth-uri=URI`{.literal}     | `https://login.microsoftonline.com/${ipaidporg}/oauth2/v2.0/authorize`{.literal}  |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--dev-auth-uri=URI`{.literal} | `https://login.microsoftonline.com/${ipaidporg}/oauth2/v2.0/devicecode`{.literal} |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--token-uri=URI`{.literal}    | `https://login.microsoftonline.com/${ipaidporg}/oauth2/v2.0/token`{.literal}      |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--userinfo-uri=URI`{.literal} | `https://graph.microsoft.com/oidc/userinfo`{.literal}                             |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--keys-uri=URI`{.literal}     | `https://login.microsoftonline.com/common/discovery/v2.0/keys`{.literal}          |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--scope=STR`{.literal}        | `openid email`{.literal}                                                          |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--idp-user-id=STR`{.literal}  | `email`{.literal}                                                                 |
    +--------------------------------+-----------------------------------------------------------------------------------+

    Show more

`--provider=google`{.literal}

:   Choosing `--provider=google`{.literal} expands to use the following options:

    +--------------------------------+--------------------------------------------------------------+
    | Option                         | Value                                                        |
    +:===============================+:=============================================================+
    | `--auth-uri=URI`{.literal}     | `https://accounts.google.com/o/oauth2/auth`{.literal}        |
    +--------------------------------+--------------------------------------------------------------+
    | `--dev-auth-uri=URI`{.literal} | `https://oauth2.googleapis.com/device/code`{.literal}        |
    +--------------------------------+--------------------------------------------------------------+
    | `--token-uri=URI`{.literal}    | `https://oauth2.googleapis.com/token`{.literal}              |
    +--------------------------------+--------------------------------------------------------------+
    | `--userinfo-uri=URI`{.literal} | `https://openidconnect.googleapis.com/v1/userinfo`{.literal} |
    +--------------------------------+--------------------------------------------------------------+
    | `--keys-uri=URI`{.literal}     | `https://www.googleapis.com/oauth2/v3/certs`{.literal}       |
    +--------------------------------+--------------------------------------------------------------+
    | `--scope=STR`{.literal}        | `openid email`{.literal}                                     |
    +--------------------------------+--------------------------------------------------------------+
    | `--idp-user-id=STR`{.literal}  | `email`{.literal}                                            |
    +--------------------------------+--------------------------------------------------------------+

    Show more

`--provider=github`{.literal}

:   Choosing `--provider=github`{.literal} expands to use the following options:

    +--------------------------------+--------------------------------------------------------------+
    | Option                         | Value                                                        |
    +:===============================+:=============================================================+
    | `--auth-uri=URI`{.literal}     | `https://github.com/login/oauth/authorize`{.literal}         |
    +--------------------------------+--------------------------------------------------------------+
    | `--dev-auth-uri=URI`{.literal} | `https://github.com/login/device/code`{.literal}             |
    +--------------------------------+--------------------------------------------------------------+
    | `--token-uri=URI`{.literal}    | `https://github.com/login/oauth/access_token`{.literal}      |
    +--------------------------------+--------------------------------------------------------------+
    | `--userinfo-uri=URI`{.literal} | `https://openidconnect.googleapis.com/v1/userinfo`{.literal} |
    +--------------------------------+--------------------------------------------------------------+
    | `--keys-uri=URI`{.literal}     | `https://api.github.com/user`{.literal}                      |
    +--------------------------------+--------------------------------------------------------------+
    | `--scope=STR`{.literal}        | `user`{.literal}                                             |
    +--------------------------------+--------------------------------------------------------------+
    | `--idp-user-id=STR`{.literal}  | `login`{.literal}                                            |
    +--------------------------------+--------------------------------------------------------------+

    Show more

`--provider=keycloak`{.literal}

:   With Keycloak, you can define multiple realms or organizations. Since it is often a part of a custom deployment, both base URL and realm ID are required, and you can specify them with the `--base-url`{.literal} and `--organization`{.literal} options to the `ipa idp-add`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# ipa idp-add MySSO --provider keycloak \
        --org main --base-url keycloak.domain.com:8443/auth \
        --client-id <your-client-id>
    ```

    Choosing `--provider=keycloak`{.literal} expands to use the following options. The value you specify in the `--base-url`{.literal} option replaces the string `${ipaidpbaseurl}`{.literal} in the table, and the value you specify for the `` --organization `option replaces the string `${ipaidporg} ``{.literal}.

    +--------------------------------+----------------------------------------------------------------------------------------------+
    | Option                         | Value                                                                                        |
    +:===============================+:=============================================================================================+
    | `--auth-uri=URI`{.literal}     | `https://${ipaidpbaseurl}/realms/${ipaidporg}/protocol/openid-connect/auth`{.literal}        |
    +--------------------------------+----------------------------------------------------------------------------------------------+
    | `--dev-auth-uri=URI`{.literal} | `https://${ipaidpbaseurl}/realms/${ipaidporg}/protocol/openid-connect/auth/device`{.literal} |
    +--------------------------------+----------------------------------------------------------------------------------------------+
    | `--token-uri=URI`{.literal}    | `https://${ipaidpbaseurl}/realms/${ipaidporg}/protocol/openid-connect/token`{.literal}       |
    +--------------------------------+----------------------------------------------------------------------------------------------+
    | `--userinfo-uri=URI`{.literal} | `https://${ipaidpbaseurl}/realms/${ipaidporg}/protocol/openid-connect/userinfo`{.literal}    |
    +--------------------------------+----------------------------------------------------------------------------------------------+
    | `--scope=STR`{.literal}        | `openid email`{.literal}                                                                     |
    +--------------------------------+----------------------------------------------------------------------------------------------+
    | `--idp-user-id=STR`{.literal}  | `email`{.literal}                                                                            |
    +--------------------------------+----------------------------------------------------------------------------------------------+

    Show more

`--provider=okta`{.literal}

:   After registering a new organization in Okta, a new base URL is associated with it. You can specify this base URL with the `--base-url`{.literal} option to the `ipa idp-add`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# ipa idp-add MyOkta --provider okta --base-url dev-12345.okta.com --client-id <your-client-id>
    ```

    Choosing `--provider=okta`{.literal} expands to use the following options. The value you specify for the `--base-url`{.literal} option replaces the string `${ipaidpbaseurl}`{.literal} in the table.

    +--------------------------------+-----------------------------------------------------------------+
    | Option                         | Value                                                           |
    +:===============================+:================================================================+
    | `--auth-uri=URI`{.literal}     | `https://${ipaidpbaseurl}/oauth2/v1/authorize`{.literal}        |
    +--------------------------------+-----------------------------------------------------------------+
    | `--dev-auth-uri=URI`{.literal} | `https://${ipaidpbaseurl}/oauth2/v1/device/authorize`{.literal} |
    +--------------------------------+-----------------------------------------------------------------+
    | `--token-uri=URI`{.literal}    | `https://${ipaidpbaseurl}/oauth2/v1/token`{.literal}            |
    +--------------------------------+-----------------------------------------------------------------+
    | `--userinfo-uri=URI`{.literal} | `https://${ipaidpbaseurl}/oauth2/v1/userinfo`{.literal}         |
    +--------------------------------+-----------------------------------------------------------------+
    | `--scope=STR`{.literal}        | `openid email`{.literal}                                        |
    +--------------------------------+-----------------------------------------------------------------+
    | `--idp-user-id=STR`{.literal}  | `email`{.literal}                                               |
    +--------------------------------+-----------------------------------------------------------------+

    Show more

**Additional resources**

-   [Pre-populated IdP templates](https://freeipa.readthedocs.io/en/latest/designs/external-idp/idp-api.html#pre-populated-idp-templates)

### [53.11. Additional resources](#using-external-identity-providers-to-authenticate-to-idm_5311-additional-resources) {#additional-resources-24 .title}

-   [Using Ansible to delegate authentication for IdM users to external identity providers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-ansible-to-delegate-authentication-for-idm-users-to-external-identity-providers)

## [Chapter 54. Using constrained delegation in IdM](#using-constrained-delegation-in-idm) {#chapter-54.-using-constrained-delegation-in-idm .title}

Configure constrained delegation using Ansible to enable one service to access other services on your behalf. You grant only limited authority for one service instead of giving full access to all your credentials.

### [54.1. Constrained delegation in Identity Management](#constrained-delegation-in-identity-management) {#constrained-delegation-in-identity-management .title}

Understand how constrained delegation allows services to act on behalf of users with limited authority, without requiring full credential delegation.

The Service for User to Proxy (`S4U2proxy`{.literal}) extension provides a service that obtains a service ticket to another service on behalf of a user. This feature is known as **constrained delegation**. The second service is typically a proxy performing some work on behalf of the first service, under the authorization context of the user. Using constrained delegation eliminates the need for the user to delegate their full ticket-granting ticket (TGT).

Identity Management (IdM) traditionally uses the Kerberos `S4U2proxy`{.literal} feature to allow the web server framework to obtain an LDAP service ticket on the user's behalf. The IdM-AD trust system also uses constrained delegation to obtain a `cifs`{.literal} principal.

You can use the `S4U2proxy`{.literal} feature to configure a web console client to allow an IdM user that has authenticated with a smart card to achieve the following:

-   Run commands with superuser privileges on the RHEL host on which the web console service is running without being asked to authenticate again.
-   Access a remote host using `SSH`{.literal} and access services on the host without being asked to authenticate again.

**Additional resources**

-   [S4U2proxy](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sfu/bde93b0e-f3c9-4ddf-9f44-e1453be7af5a)
-   [Service constrained delegation](https://www.freeipa.org/page/V4/Service_Constraint_Delegation)

### [54.2. Configuring smart-card authentication for SSH logins in the web console](#configuring-smart-card-authentication-for-ssh-logins-in-the-web-console) {#configuring-smart-card-authentication-for-ssh-logins-in-the-web-console .title}

After logging in to a user account on the RHEL web console, you can connect to remote machines by using the SSH protocol. You can use the constrained delegation feature to use SSH without being asked to authenticate again.

In this example, the web console session runs on `myhost.idm.example.com`{.literal}. Configure the console to access `remote.idm.example.com`{.literal} by using SSH on behalf of the authenticated user.

**Prerequisites**

-   You have obtained an IdM `admin`{.literal} ticket-granting ticket (TGT) on `myhost.idm.example.com`{.literal}.
-   You have `root`{.literal} access to `remote.idm.example.com`{.literal}.
-   The host that runs the web console is a member of an IdM domain.

**Procedure**

1.  In the **Terminal** page, verify that the web console has created a Service for User to Proxy (S4U2proxy) Kerberos ticket in the user session:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    …
    Valid starting     Expires            Service principal
    05/20/25 09:19:06 05/21/25 09:19:06 HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
    …
    ```

2.  Create a list of the target hosts that the delegation rule can access:

    a.  Create a service delegation target:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationtarget-add cockpit-target
        ```

    b.  Add the target host to the delegation target:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationtarget-add-member cockpit-target \
          --principals=host/remote.idm.example.com@IDM.EXAMPLE.COM
        ```

3.  Allow `cockpit`{.literal} sessions to access the target host list by creating a service delegation rule and adding the HTTP service Kerberos principal to it:

    a.  Create a service delegation rule:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationrule-add cockpit-delegation
        ```

    b.  Add the web console client to the delegation rule:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationrule-add-member cockpit-delegation \
          --principals=HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
        ```

    c.  Add the delegation target to the delegation rule:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationrule-add-target cockpit-delegation \
          --servicedelegationtargets=cockpit-target
        ```

4.  Enable Kerberos authentication on the `remote.idm.example.com`{.literal} host:

    a.  Connect through SSH to `remote.idm.example.com`{.literal} as `root`{.literal}.
    b.  Add the `GSSAPIAuthentication yes`{.literal} line to the `/etc/ssh/sshd_config`{.literal} file.

5.  Restart the `sshd`{.literal} service on `remote.idm.example.com`{.literal} so that the changes take effect immediately:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl try-restart sshd.service
    ```

**Verification**

-   In the web console, navigate to the **Terminal** page and connect to the remote host by using SSH. If the constrained delegation is configured correctly, no additional authentication is required:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh remote.idm.example.com
    ```

**Additional resources**

-   [Logging in to the web console with smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users#logging-in-to-the-web-console-with-smart-cards)
-   [Constrained delegation in Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-constrained-delegation-in-idm#constrained-delegation-in-identity-management)

### [54.3. Using Ansible to configure smart-card authentication for SSH logins in the web console](#using-ansible-to-configure-smart-card-authentication-for-SSH-logins-in-the-web-console) {#using-ansible-to-configure-smart-card-authentication-for-ssh-logins-in-the-web-console .title}

After logging in to the web console, you can connect to remote machines by using the SSH protocol. You can use the `servicedelegation*`{.literal} Ansible modules to configure the web console for the constrained delegation feature to allow SSH connections without additional authentication.

In this example, the web console session runs on `myhost.idm.example.com`{.literal}. You configure it to access `remote.idm.example.com`{.literal} by using SSH on behalf of the authenticated user.

**Prerequisites**

-   You have obtained an IdM `admin`{.literal} ticket-granting ticket (TGT) on `myhost.idm.example.com`{.literal}.

-   You have `root`{.literal} access to `remote.idm.example.com`{.literal}.

-   The host that runs the web console is a member of an IdM domain.

-   You have configured your Ansible control node to meet the following requirements:

    -   You have installed the `ansible-freeipa`{.literal} package.

    -   The example assumes you have created an Ansible inventory file with the fully-qualified domain name (FQDN) of the IdM server in the `~/`{.literal}*`MyPlaybooks`{.literal}*`/`{.literal} directory.

    -   The example assumes that the `secret.yml`{.literal} Ansible vault stores the admin password in the `ipaadmin_password`{.literal} variable.

        See the `/usr/share/doc/ansible-freeipa/playbooks/servicedelegationtarget`{.literal} and `/usr/share/doc/ansible-freeipa/playbooks/servicedelegationrule`{.literal} directories for example playbooks and the `README-servicedelegationrule.md`{.literal} and `README-servicedelegationtarget.md`{.literal} files in the `/usr/share/doc/ansible-freeipa/`{.literal} directory for more information.

-   The target node, that is the node on which the `ansible-freeipa`{.literal} module runs, is part of the IdM domain as an IdM client, server, or replica.

**Procedure**

1.  Navigate to your `~/`{.literal}*`MyPlaybooks`{.literal}*`/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Store your sensitive variables in an encrypted file:

    a.  Create the vault:

        ``` {.language-plaintext tabindex="-1"}
        $ ansible-vault create secret.yml
        New Vault password: <vault_password>
        Confirm New Vault password: <vault_password>
        ```

    b.  After the `ansible-vault create`{.literal} command opens an editor, enter the sensitive data in the *`<key>`{.literal}*`: `{.literal}*`<value>`{.literal}* format:

        ``` {.language-plaintext tabindex="-1"}
        ipaadmin_password: <admin_password>
        ```

    c.  Save the changes, and close the editor. Ansible encrypts the data in the vault.

3.  In the **Terminal** page, verify that the web console has created a Service for User to Proxy (S4U2proxy) Kerberos ticket in the user session:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    …
    Valid starting     Expires            Service principal
    05/20/25 09:19:06 05/21/25 09:19:06 HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
    …
    ```

4.  Create a `web-console-smart-card-ssh.yml`{.literal} playbook with the following content:

    a.  Create a task that ensures the presence of a delegation target:

        ``` {.language-yaml tabindex="-1"}
        ---
        - name: Playbook to create a constrained delegation target
          hosts: ipaserver

          vars_files:
          - /home/user_name/MyPlaybooks/secret.yml
          tasks:
          - name: Ensure servicedelegationtarget web-console-delegation-target is present
            ipaservicedelegationtarget:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: web-console-delegation-target
        ```

    b.  Add a task that adds the target host to the delegation target:

        ``` {.language-yaml tabindex="-1"}
          - name: Ensure servicedelegationtarget web-console-delegation-target member principal host/remote.idm.example.com@IDM.EXAMPLE.COM is present
            ipaservicedelegationtarget:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: web-console-delegation-target
              principal: host/remote.idm.example.com@IDM.EXAMPLE.COM
              action: member
        ```

    c.  Add a task that ensures the presence of a delegation rule:

        ``` {.language-yaml tabindex="-1"}
          - name: Ensure servicedelegationrule delegation-rule is present
            ipaservicedelegationrule:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: web-console-delegation-rule
        ```

    d.  Add a task that ensures that the Kerberos principal of the web console client service is a member of the constrained delegation rule:

        ``` {.language-yaml tabindex="-1"}
          - name: Ensure the Kerberos principal of the web console client service is added to the servicedelegationrule web-console-delegation-rule
            ipaservicedelegationrule:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: web-console-delegation-rule
              principal: HTTP/myhost.idm.example.com
              action: member
        ```

    e.  Add a task that ensures that the constrained delegation rule is associated with the web-console-delegation-target delegation target:

        ``` {.language-yaml tabindex="-1"}
          - name: Ensure a constrained delegation rule is associated with a specific delegation target
            ipaservicedelegationrule:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: web-console-delegation-rule
              target: web-console-delegation-target
              action: member
        ```

    f.  Add a task that enable Kerberos authentication on `remote.idm.example.com`{.literal}:

        ``` {.language-yaml tabindex="-1"}
          - name: Enable Kerberos authentication
            hosts: remote.idm.example.com
            vars:
              sshd_config:
                GSSAPIAuthentication: true
            roles:
              - role: rhel-system-roles.sshd
        ```

5.  Save the file.

6.  Run the Ansible Playbook. Specify the playbook file, the file storing the password protecting the `secret.yml`{.literal} file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory web-console-smart-card-ssh.yml
    ```

**Verification**

-   In the web console, navigate to the **Terminal** page and connect to the remote host by using SSH. If the constrained delegation is configured correctly, no additional authentication is required:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh remote.idm.example.com
    ```

**Additional resources**

-   [Logging in to the web console with smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users#logging-in-to-the-web-console-with-smart-cards)
-   [Constrained delegation in Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-constrained-delegation-in-idm#constrained-delegation-in-identity-management)

### [54.4. Configuring a web console to allow a user authenticated with a smart card to run sudo without being asked to authenticate again](#configuring-a-web-console-to-allow-a-user-authenticated-with-a-smart-card-to-run-sudo-without-being-asked-to-authenticate-again) {#configuring-a-web-console-to-allow-a-user-authenticated-with-a-smart-card-to-run-sudo-without-being-asked-to-authenticate-again .title}

Configure constrained delegation in Identity Management (IdM) so that smart card-authenticated web console users can run `sudo`{.literal} without re-authenticating.

After you have logged in to a user account on the RHEL web console, as an IdM system administrator you might need to run commands with superuser privileges. You can use the [constrained delegation](#constrained-delegation-in-identity-management "54.1. Constrained delegation in Identity Management") feature to run `sudo`{.literal} on the system without being asked to authenticate again.

In the example below, the web console session runs on the **myhost.idm.example.com** host.

**Prerequisites**

-   You have obtained an IdM `admin`{.literal} ticket-granting ticket (TGT).

-   The web console service is present in IdM.

-   The **myhost.idm.example.com** host is present in IdM.

-   You have enabled `admin`{.literal} `sudo`{.literal} access to domain administrators on the IdM server.

-   The web console has created an `S4U2Proxy`{.literal} Kerberos ticket in the user session. To verify that this is the case, log in to the web console as an IdM user, open the `Terminal`{.literal} page, and enter:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    Ticket cache: FILE:/run/user/1894000001/cockpit-session-3692.ccache
    Default principal: user@IDM.EXAMPLE.COM

    Valid starting     Expires            Service principal
    07/30/21 09:19:06 07/31/21 09:19:06 HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
    07/30/21 09:19:06  07/31/21 09:19:06  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
            for client HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
    ```

**Procedure**

1.  Create a list of the target hosts that can be accessed by the delegation rule:

    a.  Create a service delegation target:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationtarget-add cockpit-target
        ```

    b.  Add the target host to the delegation target:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationtarget-add-member cockpit-target \
          --principals=host/myhost.idm.example.com@IDM.EXAMPLE.COM
        ```

2.  Allow `cockpit`{.literal} sessions to access the target host list by creating a service delegation rule and adding the `HTTP`{.literal} service Kerberos principal to it:

    a.  Create a service delegation rule:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationrule-add cockpit-delegation
        ```

    b.  Add the web console service to the delegation rule:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationrule-add-member cockpit-delegation \
          --principals=HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
        ```

    c.  Add the delegation target to the delegation rule:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationrule-add-target cockpit-delegation \
          --servicedelegationtargets=cockpit-target
        ```

3.  Enable `pam_sss_gss`{.literal}, the PAM module for authenticating users over the Generic Security Service Application Program Interface (GSSAPI) in cooperation with the System Security Services Daemon (SSSD):

    a.  Open the `/etc/sssd/sssd.conf`{.literal} file for editing.

    b.  Specify that `pam_sss_gss`{.literal} can provide authentication for the `sudo`{.literal} and `sudo -i`{.literal} commands in IdM your domain:

        ``` {.language-plaintext tabindex="-1"}
        [domain/idm.example.com]
        pam_gssapi_services = sudo, sudo-i
        ```

    c.  Save and exit the file.

    d.  Open the `/etc/pam.d/sudo`{.literal} file for editing.

    e.  Insert the following line to the top of the `#%PAM-1.0`{.literal} list to allow, but not require, GSSAPI authentication for `sudo`{.literal} commands:

        ``` {.language-plaintext tabindex="-1"}
        auth sufficient pam_sss_gss.so
        ```

    f.  Save and exit the file.

4.  Restart the `SSSD`{.literal} service so that the above changes take effect immediately:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl restart sssd
    ```

**Additional resources**

-   [Logging in to the web console with smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users#logging-in-to-the-web-console-with-smart-cards)
-   [Constrained delegation in Identity Management](#constrained-delegation-in-identity-management "54.1. Constrained delegation in Identity Management")

### [54.5. Using Ansible to configure a web console to allow a user authenticated with a smart card to run sudo without being asked to authenticate again](#using-ansible-to-configure-a-web-console-to-allow-a-user-authenticated-with-a-smart-card-to-run-sudo-without-being-asked-to-authenticate-again) {#using-ansible-to-configure-a-web-console-to-allow-a-user-authenticated-with-a-smart-card-to-run-sudo-without-being-asked-to-authenticate-again .title}

Configure constrained delegation in Identity Management (IdM) using Ansible so that smart card-authenticated web console users can run `sudo`{.literal} without re-authenticating.

After you have logged in to a user account on the RHEL web console, as an Identity Management (IdM) system administrator you might need to run commands with superuser privileges. You can use the [constrained delegation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-constrained-delegation-in-idm#constrained-delegation-in-identity-management) feature to run `sudo`{.literal} on the system without being asked to authenticate again.

Follow this procedure to use the `ipaservicedelegationrule`{.literal} and `ipaservicedelegationtarget`{.literal} `ansible-freeipa`{.literal} modules to configure a web console to use constrained delegation. In the example below, the web console session runs on the **myhost.idm.example.com** host.

**Prerequisites**

-   You have obtained an IdM `admin`{.literal} ticket-granting ticket (TGT) by authenticating to the web console session with a smart card..

-   The web console service has been enrolled into IdM.

-   The **myhost.idm.example.com** host is present in IdM.

-   You have [enabled `admin`{.literal} `sudo`{.literal} access to domain administrators on the IdM server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/configuring-sso-authentication-for-the-rhel-web-console-in-the-idm-domain).

-   The web console has created an `S4U2Proxy`{.literal} Kerberos ticket in the user session. To verify that this is the case, log in to the web console as an IdM user, open the `Terminal`{.literal} page, and enter:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    Ticket cache: FILE:/run/user/1894000001/cockpit-session-3692.ccache
    Default principal: user@IDM.EXAMPLE.COM

    Valid starting     Expires            Service principal
    07/30/21 09:19:06 07/31/21 09:19:06 HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
    07/30/21 09:19:06  07/31/21 09:19:06  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
            for client HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
    ```

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  On your Ansible control node, navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Create a `web-console-smart-card-sudo.yml`{.literal} playbook with the following content:

    a.  Create a task that ensures the presence of a delegation target:

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Playbook to create a constrained delegation target
          hosts: ipaserver

          vars_files:
          - /home/user_name/MyPlaybooks/secret.yml
          tasks:
          - name: Ensure servicedelegationtarget named sudo-web-console-delegation-target is present
            freeipa.ansible_freeipa.ipaservicedelegationtarget:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: sudo-web-console-delegation-target
        ```

    b.  Add a task that adds the target host to the delegation target:

        ``` {.language-plaintext tabindex="-1"}
          - name: Ensure that a member principal named host/myhost.idm.example.com@IDM.EXAMPLE.COM is present in a service delegation target named sudo-web-console-delegation-target
            freeipa.ansible_freeipa.ipaservicedelegationtarget:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: sudo-web-console-delegation-target
              principal: host/myhost.idm.example.com@IDM.EXAMPLE.COM
              action: member
        ```

    c.  Add a task that ensures the presence of a delegation rule:

        ``` {.language-plaintext tabindex="-1"}
          - name: Ensure servicedelegationrule named sudo-web-console-delegation-rule is present
            freeipa.ansible_freeipa.ipaservicedelegationrule:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: sudo-web-console-delegation-rule
        ```

    d.  Add a task that ensures that the Kerberos principal of the web console service is a member of the constrained delegation rule:

        ``` {.language-plaintext tabindex="-1"}
          - name: Ensure the Kerberos principal of the web console service is added to the service delegation rule named sudo-web-console-delegation-rule
            freeipa.ansible_freeipa.ipaservicedelegationrule:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: sudo-web-console-delegation-rule
              principal: HTTP/myhost.idm.example.com
              action: member
        ```

    e.  Add a task that ensures that the constrained delegation rule is associated with the sudo-web-console-delegation-target delegation target:

        ``` {.language-plaintext tabindex="-1"}
          - name: Ensure a constrained delegation rule is associated with a specific delegation target
            freeipa.ansible_freeipa.ipaservicedelegationrule:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: sudo-web-console-delegation-rule
              target: sudo-web-console-delegation-target
              action: member
        ```

3.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-servicedelegationrule.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/servicedelegationtarget`{.literal} directory on the control node.

4.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory web-console-smart-card-sudo.yml
    ```

5.  Enable `pam_sss_gss`{.literal}, the PAM module for authenticating users over the Generic Security Service Application Program Interface (GSSAPI) in cooperation with the System Security Services Daemon (SSSD):

    a.  Open the `/etc/sssd/sssd.conf`{.literal} file for editing.

    b.  Specify that `pam_sss_gss`{.literal} can provide authentication for the `sudo`{.literal} and `sudo -i`{.literal} commands in IdM your domain:

        ``` {.language-plaintext tabindex="-1"}
        [domain/idm.example.com]
        pam_gssapi_services = sudo, sudo-i
        ```

    c.  Save and exit the file.

    d.  Open the `/etc/pam.d/sudo`{.literal} file for editing.

    e.  Insert the following line to the top of the `#%PAM-1.0`{.literal} list to allow, but not require, GSSAPI authentication for `sudo`{.literal} commands:

        ``` {.language-plaintext tabindex="-1"}
        auth sufficient pam_sss_gss.so
        ```

    f.  Save and exit the file.

6.  Restart the `SSSD`{.literal} service so that the above changes take effect immediately:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl restart sssd
    ```

**Additional resources**

-   [Constrained delegation in Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-constrained-delegation-in-idm#constrained-delegation-in-identity-management)

### [54.6. Additional resources](#using-constrained-delegation-in-idm_546-additional-resources) {#additional-resources-25 .title}

-   [Managing remote systems in the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/managing-remote-systems-in-the-web-console)

## [Chapter 55. Using resource-based constrained delegation in IdM](#using-resource-based-constrained-delegation-in-idm) {#chapter-55.-using-resource-based-constrained-delegation-in-idm .title}

Use resource-based constrained delegation (RBCD) in Identity Management (IdM) to control service access delegation at the resource level.

Unlike general constrained delegation, RBCD allows the service owner to grant delegation permissions rather than requiring a domain administrator. This is especially useful in IdM and Active Directory (AD) trust environments where delegation must span across forests.

Since 2019, Microsoft AD enforces the use of RBCD when both target and proxy services belong to different forests.

### [55.1. Resource-based constrained delegation in IdM](#resource-based-constrained-delegation-in-idm) {#resource-based-constrained-delegation-in-idm .title}

Resource-based constrained delegation (RBCD) in Identity Management (IdM) gives service owners direct control over which services can delegate user credentials to their service, removing the need for domain administrator involvement in each delegation decision.

RBCD versus general constrained delegation

:   Resource-based constrained delegation (RBCD) differs from general constrained delegation in multiple aspects:

    -   Granularity: In RBCD, delegation is specified at the resource level.
    -   Access granting responsibility: in RBCD, access is controlled by the service owner rather than by the Kerberos administrator.

In general constrained delegation, the Service for User to Proxy (`S4U2proxy`{.literal}) extension obtains a service ticket for another service on behalf of a user. The second service is typically a proxy performing work on behalf of the first service, under the authorization context of the user. Using constrained delegation eliminates the need for the user to delegate their full ticket-granting ticket (TGT).

How IdM uses constrained delegation
:   Identity Management (IdM) traditionally uses the Kerberos `S4U2proxy`{.literal} feature to allow the web server framework to obtain an LDAP service ticket on a user's behalf.

When IdM integrates with Active Directory (AD), the IdM framework also uses constrained delegation to operate on behalf of a user towards various services, including SMB and DCE RPC end-points on both the IdM and AD sides.

How IdM can use RBCD
:   When an application in an IdM domain operates on behalf of users against a different service, it requires a delegation permission. In general constrained delegation, this requires the domain administrator to explicitly create a rule to allow a first service to delegate user credentials to the next service. Using RBCD, the delegation permission can be created by the owner of the service to which the credentials are delegated.

For IdM-AD integration, when both services are part of the same IdM domain, the RBCD permission can be granted on the IdM side.

Important

Currently, only services in the IdM domain can be configured with RBCD rules. If the target service is part of an AD domain, the permission can only be granted on the AD side. As AD domain controllers cannot resolve IdM service information to create the rule, this is not currently supported.

### [55.2. Using RBCD to delegate access to a service](#using-rbcd-to-delegate-access-to-a-service) {#using-rbcd-to-delegate-access-to-a-service .title}

Use resource-based constrained delegation (RBCD) in Identity Management (IdM) to grant one service the ability to act on behalf of a user towards another service, without requiring domain administrator intervention.

Delegate user credentials from the `HTTP/client.example.test`{.literal} web service to the `nfs/client.example.test`{.literal} file server on the same host. Since hosts manage their own local services, apply the RBCD rule directly to the `client.example.test`{.literal} host object.

**Prerequisites**

-   You have access to the `/etc/krb5.keytab`{.literal} file of the `client.example.test`{.literal} host.
-   A `nfs/client.example.test`{.literal} service keytab exists.
-   A keytab `/path/to/web-service.keytab`{.literal} for `HTTP/client.example.test`{.literal} exists.

**Procedure**

1.  On the `client.example.test`{.literal} host, obtain a Kerberos ticket:

    ``` {.language-plaintext tabindex="-1"}
    # kinit -k
    ```

2.  Define the RBCD ACL:

    ``` {.language-plaintext tabindex="-1"}
    # ipa service-add-delegation nfs/client.example.test HTTP/client.example.test

    -------------------------------------------------------
    Added new resource delegation to the service principal "nfs/client.example.test@EXAMPLE.TEST"
    -------------------------------------------------------
      Principal name: nfs/client.example.test@EXAMPLE.TEST
      Delegation principal: HTTP/client.example.test@EXAMPLE.TEST
    ```

**Verification**

To verify that the delegation is set up correctly, you can simulate a `testuser`{.literal} user logging in through the `HTTP`{.literal} service and performing a protocol transition to the `NFS`{.literal} service.

1.  View the NFS service to verify that the delegation rule is present:

    ``` {.language-plaintext tabindex="-1"}
    # ipa service-show nfs/client.example.test

      Principal name: nfs/client.example.test@EXAMPLE.TEST
      Principal alias: nfs/client.example.test@EXAMPLE.TEST
      Delegation principal: HTTP/client.example.test@EXAMPLE.TEST
      Keytab: True
      Managed by: client.example.test
    ```

2.  Obtain a Kerberos ticket for the HTTP service principal:

    ``` {.language-plaintext tabindex="-1"}
    # kinit -kt http.keytab HTTP/client.example.test
    ```

3.  Verify that the ticket granting ticket is present:

    ``` {.language-plaintext tabindex="-1"}
    # klist -f
    Ticket cache: KCM:0:99799
    Default principal: HTTP/client.example.test@EXAMPLE.TEST

    Valid starting       Expires              Service principal
    10/13/2023 14:39:23  10/14/2023 14:05:07  krbtgt/EXAMPLE.TEST@EXAMPLE.TEST
        Flags: FIA
    ```

4.  Perform a protocol transition on behalf of `testuser`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # kvno -U testuser -P nfs/client.example.test
    nfs/client.example.test@EXAMPLE.TEST: kvno = 1
    ```

5.  Verify that tickets obtained during protocol transition on behalf of `testuser`{.literal} are present:

    ``` {.language-plaintext tabindex="-1"}
    # klist -f
    Ticket cache: KCM:0:99799
    Default principal: HTTP/client.example.test@EXAMPLE.TEST

    Valid starting       Expires              Service principal
    10/13/2023 14:39:38  10/14/2023 14:05:07  HTTP/client.example.test@EXAMPLE.TEST
        for client testuser@EXAMPLE.TEST, Flags: FAT
    10/13/2023 14:39:23  10/14/2023 14:05:07  krbtgt/EXAMPLE.TEST@EXAMPLE.TEST
        Flags: FIA
    10/13/2023 14:39:38  10/14/2023 14:05:07  nfs/client.example.test@EXAMPLE.TEST
        for client testuser@EXAMPLE.TEST, Flags: FAT
    ```

## [Legal Notice](#idm139997968406128) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
