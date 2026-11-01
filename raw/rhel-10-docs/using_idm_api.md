---
{"title": "Using IdM API", "guide": "using_idm_api", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_idm_api/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Using IdM API {#using-idm-api .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Using IdM API with Python scripts {#using-idm-api-with-python-scripts .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139879850443184)

**Abstract**

The IdM API contains examples for using various types of request. Administrators and developers can use the IdM API to write custom scripts in Python to integrate IdM with third-party applications.

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

## [Chapter 1. Introduction to IdM API](#introduction-to-idm-api) {#chapter-1.-introduction-to-idm-api .title}

You can access the services of the Red Hat Identity Management with command-line and web-based interfaces. With the Identity Management API, you can interact with Identity Management services through the third-party applications and scripts that are written in Python.

The Identity Management API has the JavaScript Object Notation Remote Procedure Call (JSON-RPC) interface. To use the automation for various important parts, access the Identity Management API through Python. For example, you can retrieve metadata from the server with all available commands.

## [Chapter 2. Basics of IdM API](#basics-of-idm-api) {#chapter-2.-basics-of-idm-api .title}

You can use the IdM API to automate access to your IdM environment with custom scripts. This reduces manual effort and ensures consistent identity management across your infrastructure.

### [2.1. Initializing IdM API](#initializing-idm-api) {#initializing-idm-api .title}

To use the IdM API, first initialize it in your environment. Proper initialization establishes the connection to IdM services and enables your scripts to run API commands.

**Prerequisites**

-   The IdM server or IdM client package is installed.
-   A valid Kerberos ticket is issued.

**Procedure**

1.  To initialize the IdM API, include the following code in the beginning of your script:

    ``` {.language-plaintext tabindex="-1"}
    from ipalib import api

    api.bootstrap(context="server")
    api.finalize()
    ```

2.  To establish a connection with the LDAP server, add the following logic to your script after API initialization:

    ``` {.language-plaintext tabindex="-1"}
    if api.env.in_server:
        api.Backend.ldap2.connect()
    else:
        api.Backend.rpcclient.connect()
    ```

    -   If you run your script on the IdM server, this logic allows your script to connect directly to LDAP server.
    -   If you run your script on the IdM client, the script uses the Remote Procedure Call (RPC) client.

**Additional resources**

-   [IdM API context](#idm-api-context "2.6. IdM API context")

### [2.2. Running IdM API commands](#running-idm-api-commands) {#running-idm-api-commands .title}

You can run IdM API commands within your script to automate identity management tasks. Use the `api.Command`{.literal} structure to run commands and retrieve information about users, groups, and other IdM objects.

**Prerequisites**

-   The IdM API is initialized. For more information, see [Initializing IdM API](#initializing-idm-api "2.1. Initializing IdM API").

**Procedure**

-   To list the information about a user, include the following code in your script:

    ``` {.language-plaintext tabindex="-1"}
    api.Command.user_show("user_name", no_members=True, all=True)
    ```

    In this example, you also pass arguments and options to the command `user_show`{.literal}.

**Additional resources**

-   [IPA API Commands](https://freeipa.readthedocs.io/en/latest/api/commands.html)

### [2.3. IdM API commands output structure](#idm-api-commands-output-structure) {#idm-api-commands-output-structure .title}

Each IdM API command returns output in four sections. Understanding this structure helps you parse command results and handle responses in your automation scripts.

**IdM API output structure**

`result`{.literal}
:   This section provides the result of the command. It contains various details about the command operation, such as options and arguments which were passed to the command.

`values`{.literal}
:   This section indicates the argument for the command.

`messages`{.literal}
:   This section shows various information which `ipa`{.literal} tool provides after the execution of the command.

`summary`{.literal}
:   This section shows the summary for the operation.

In this example, your script executes the `add_user`{.literal} command:

``` {.language-plaintext tabindex="-1"}
api.Command.user_add("test", givenname="a", sn="b")
```

The output structure of that command is below:

``` {.language-plaintext tabindex="-1"}
{
    "result": {
        "displayname": ["a b"],
        "objectclass": [
            "top",
            "person",
            "organizationalperson",
            "inetorgperson",
            "inetuser",
            "posixaccount",
            "krbprincipalaux",
            "krbticketpolicyaux",
            "ipaobject",
            "ipasshuser",
            "ipaSshGroupOfPubKeys",
            "mepOriginEntry",
            "ipantuserattrs",
        ],
        "cn": ["a b"],
        "gidnumber": ["1445000004"],
        "mail": ["test@ipa.test"],
        "krbprincipalname": [ipapython.kerberos.Principal("test@IPA.TEST")],
        "loginshell": ["/bin/sh"],
        "initials": ["ab"],
        "uid": ["test"],
        "uidnumber": ["1445000004"],
        "sn": ["b"],
        "krbcanonicalname": [ipapython.kerberos.Principal("test@IPA.TEST")],
        "homedirectory": ["/home/test"],
        "givenname": ["a"],
        "gecos": ["a b"],
        "ipauniqueid": ["9f9c1df8-5073-11ed-9a56-fa163ea98bb3"],
        "mepmanagedentry": [
            ipapython.dn.DN("cn=test,cn=groups,cn=accounts,dc=ipa,dc=test")
        ],
        "has_password": False,
        "has_keytab": False,
        "memberof_group": ["ipausers"],
        "dn": ipapython.dn.DN("uid=test,cn=users,cn=accounts,dc=ipa,dc=test"),
    },
    "value": "test",
    "messages": [
        {
            "type": "warning",
            "name": "VersionMissing",
            "message": "API Version number was not sent, forward compatibility not guaranteed. Assuming server's API version, 2.248",
            "code": 13001,
            "data": {"server_version": "2.248"},
        }
    ],
    "summary": 'Added user "test"',
}
```

### [2.4. Listing the IdM API commands and parameters](#listing-the-idm-api-commands-and-parameters) {#listing-the-idm-api-commands-and-parameters .title}

You can list information about IdM API commands and their parameters by using `command_show`{.literal} and `param_show`{.literal}. This helps you discover available commands and understand the required inputs for your scripts.

**Prerequisites**

-   The IdM API is initialized. For more information, see [Initializing IdM API](#initializing-idm-api "2.1. Initializing IdM API").

**Procedure**

1.  To display information about `user_add`{.literal} command, run the following code:

    ``` {.language-plaintext tabindex="-1"}
    api.Command.command_show("user_add")
    ```

    The result for this command is as follows:

    ``` {.language-plaintext tabindex="-1"}
    {
        "result": {
            "name": "user_add",
            "version": "1",
            "full_name": "user_add/1",
            "doc": "Add a new user.",
            "topic_topic": "user/1",
            "obj_class": "user/1",
            "attr_name": "add",
        },
        "value": "user_add",
        "messages": [
            {
                "type": "warning",
                "name": "VersionMissing",
                "message": "API Version number was not sent, forward compatibility not guaranteed. Assuming server's API version, 2.251",
                "code": 13001,
                "data": {"server_version": "2.251"},
            }
        ],
        "summary": None,
    }
    ```

2.  To display information about the `givenname`{.literal} parameter for the `user_add`{.literal} command, run the following code:

    ``` {.language-plaintext tabindex="-1"}
    api.Command.param_show("user_add", name="givenname")
    ```

    The result for this command is as follows:

    ``` {.language-plaintext tabindex="-1"}
    {
        "result": {
            "name": "givenname",
            "type": "str",
            "positional": False,
            "cli_name": "first",
            "label": "First name",
        },
        "value": "givenname",
        "messages": [
            {
                "type": "warning",
                "name": "VersionMissing",
                "message": "API Version number was not sent, forward compatibility not guaranteed. Assuming server's API version, 2.251",
                "code": 13001,
                "data": {"server_version": "2.251"},
            }
        ],
        "summary": None,
    }
    ```

### [2.5. Using batches for running IdM API commands](#using-batches-for-executing-idm-api-commands) {#using-batches-for-running-idm-api-commands .title}

You can run multiple IdM API commands with a single call by using the `batch`{.literal} command. Batching improves performance and reduces network overhead when performing bulk operations such as creating multiple users.

**Prerequisites**

-   The IdM API is initialized. For more information, see [Initializing IdM API](#initializing-idm-api "2.1. Initializing IdM API").

**Procedure**

-   To create 100 IdM users in one batch, include the following code in your script:

    ``` {.language-plaintext tabindex="-1"}
    batch_args = []
    for i in range(100):
        user_id = "user%i" % i
        args = [user_id]
        kw = {
            'givenname' : user_id,
            'sn' : user_id
        }
        batch_args.append({
            'method' : 'user_add',
            'params' : [args, kw]
        })
    ret = api.Command.batch(*batch_args)
    ```

### [2.6. IdM API context](#idm-api-context) {#idm-api-context .title}

IdM API context determines which plug-ins the API uses. Selecting the correct context ensures your scripts use the appropriate validation and execution methods for your environment.

**IdM API context**

`server`{.literal}
:   Set of plug-ins which validate arguments and options that are passed to IdM API commands for execution.

`client`{.literal}
:   Set of plug-ins which validate arguments and options that are forwarded to the IdM server for execution.

`installer`{.literal}
:   Set of plug-ins which are specific to the installation process.

`updates`{.literal}
:   Set of plug-ins which are specific to the updating process.

## [Chapter 3. IdM API and IdM CLI commands comparison](#idm-api-and-idm-cli-commands-comparison) {#chapter-3.-idm-api-and-idm-cli-commands-comparison .title}

Understanding differences between IdM API and IdM CLI commands helps you translate CLI knowledge to API usage and avoid common errors in your scripts.

The IdM API commands are different from the `ipa`{.literal} tool commands:

Command naming structure
:   The `ipa`{.literal} CLI commands use the hyphen, as in `user-add`{.literal}, but IdM API commands use the underscore instead, as in `user_add`{.literal}.

Parameter naming
:   The parameters are different for IdM CLI commands and IdM API commands. For example, the IdM CLI `user-add`{.literal} command has a parameter `first`{.literal} but the IdM API `user_add`{.literal} command has a parameter `givenname`{.literal}.

Date format

:   The following date formats are available for IdM CLI:

    -   `%Y%m%d%H%M%SZ`{.literal}

    -   `%Y-%m-%dT%H:%M:%SZ`{.literal}

    -   `%Y-%m-%dT%H:%MZ`{.literal}

    -   `%Y-%m-%dZ`{.literal}

    -   `%Y-%m-%d %H:%M:%SZ`{.literal}

    -   `%Y-%m-%d %H:%MZ`{.literal}

        Additionally, the IdM API can use the Python built-in class `datetime`{.literal}.

Useful CLI tools:

-   The `console`{.literal} starts an interactive Python console, which you can use to run IdM API commands.
-   The `help`{.literal} command shows description of the topics and the commands and includes various examples.
-   The `show-mapping`{.literal} command shows the mapping between CLI parameter names and LDAP attributes.

## [Chapter 4. IdM API example scenarios](#idm-api-example-scenarios) {#chapter-4.-idm-api-example-scenarios .title}

Use these code examples as templates to build your own automation scripts for managing users, groups, and access control. These example demonstrate common scenarios for using IdM API commands.

### [4.1. Managing users with IdM API commands](#managing-users-with-idm-api-commands) {#managing-users-with-idm-api-commands .title}

You can manage IdM users programmatically with the IdM API commands. Automating user management tasks reduces manual effort and ensures consistent user provisioning across your environment.

Creating an IdM user

:   In this example, you create an IdM user with the username `exampleuser`{.literal} and the supported user `one-time password (OTP)`{.literal} authentication.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.user_add("exampleuser", givenname="Example", sn="User", ipauserauthtype="otp")
    ```

Showing an IdM user information

:   In this example, you display all available information about the IdM user `exampleuser`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.user_show("exampleuser", all=True)
    ```

Modifying an IdM user

:   In this example, you change the e-mail address for the IdM user `exampleuser`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.user_mod("exampleuser", mail="exampleuser@example.org")
    ```

Searching for an IdM user

:   In this example, you search for all IdM users that match `exampleuser`{.literal} in the IdM group `admins`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.user_find(criteria="exampleuser", in_group="admins")
    ```

Deleting an IdM user

:   In this example, you delete the IdM user `exampleuser`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.user_del("exampleuser")
    ```

    To restore the user in future, use the `preserve`{.literal} option. If you use this option, you can restore the user with the `user_undel`{.literal} command.

Adding and removing a certificate for an IdM user

:   You can add or remove `Base64 encoded`{.literal} certificate for a user with the `user_add_cert`{.literal} and `user_remove_cert`{.literal} commands. In this example, you add a certificate for a user `exampleuser`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    args = ["exampleuser"]
    kw = {
        "usercertificate": """
          MIICYzCCAcygAwIBAgIBADANBgkqhkiG9w0BAQUFADAuMQswCQYDVQQGEwJVUzEMMAoGA1UEC
          hMDSUJNMREwDwYDVQQLEwhMb2NhbCBDQTAeFw05OTEyMjIwNTAwMDBaFw0wMDEyMjMwNDU5NT
          laMC4xCzAJBgNVBAYTAlVTMQwwCgYDVQQKEwNJQk0xETAPBgNVBAsTCExvY2FsIENBMIGfMA0
          GCSqGSIb3DQEBATOPA4GNADCBiQKBgQD2bZEo7xGaX2/0GHkrNFZvlxBou9v1Jmt/PDiTMPve
          8r9FeJAQ0QdvFST/0JPQYD20rH0bimdDLgNdNynmyRoS2S/IInfpmf69iyc2G0TPyRvmHIiOZ
          bdCd+YBHQi1adkj17NDcWj6S14tVurFX73zx0sNoMS79q3tuXKrDsxeuwIDAQABo4GQMIGNME
          sGCVUdDwGG+EIBDQQ+EzxHZW5lcmF0ZWQgYnkgdGhlIFNlY3VyZVdheSBTZWN1cml0eSBTZXJ
          2ZXIgZm9yIE9TLzM5MCAoUkFDRikwDgYDVR0PAQH/BAQDAgAGMA8GA1UdEwEB/wQFMAMBAf8w
          HQYDVR0OBBYEFJ3+ocRyCTJw067dLSwr/nalx6YMMA0GCSqGSIb3DQEBBQUAA4GBAMaQzt+za
          j1GU77yzlr8iiMBXgdQrwsZZWJo5exnAucJAEYQZmOfyLiMD6oYq+ZnfvM0n8G/Y79q8nhwvu
          xpYOnRSAXFp6xSkrIOeZtJMY1h00LKp/JX3Ng1svZ2agE126JHsQ0bhzN5TKsYfbwfTwfjdWA
          Gy6Vf1nYi/rO+ryMO
        """
    }

    api.Command.user_add_cert(*args, **kw)
    ```

Enabling and disabling an IdM user

:   You can enable or disable an IdM user with the `user_enable`{.literal} and `user_disable`{.literal} commands. In this example, you disable the IdM user `exampleuser`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.user_disable("exampleuser")
    ```

### [4.2. Managing groups with IdM API commands](#managing-groups-with-idm-api-commands) {#managing-groups-with-idm-api-commands .title}

You can manage IdM groups programmatically with the IdM API commands. Automating group management helps you efficiently organize users and control access to resources.

Creating an IdM group

:   In this example, you create an IdM group `developers`{.literal}, with a specified Group ID number.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_add("developers", gidnumber=500, description="Developers")
    ```

Adding a user as a member to an IdM group

:   In this example, you add the `admin`{.literal} user to the `developers`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_add_member("developers", user="admin")
    ```

Adding a service as a member to an IdM group

:   In this example, you add the `HTTP/server.ipa.test`{.literal} service to the `developers`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_add_member("developers", service="HTTP/server.ipa.test")
    ```

Adding a group as a subgroup to an IdM group

:   In this example, you add another group, `admins`{.literal}, to the `developers`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_add_member("developers", group="admins")
    ```

Adding IdM group managers

:   In this example, you add the `bob`{.literal} user as a group manager for the `developers`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_add_member_manager("developers", user="bob")
    ```

Finding an IdM group

:   You can search for an IdM group using various parameters. In this example, you find all groups that the user `bob`{.literal} is managing.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_find(membermanager_user="bob")
    ```

Displaying IdM group information

:   In this example, you display group information about the `developers`{.literal} group, without the members list.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_show("developers", no_members=True)
    ```

Modifying an IdM group

:   In this example, you convert a non-POSIX group `testgroup`{.literal} to a POSIX group.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_mod("testgroup", posix=True)
    ```

Removing members from an IdM group

:   In this example, you remove the `admin`{.literal} user from the `developers`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_remove_member("developers", user="admin")
    ```

Removing IdM group managers

:   In this example, you remove the user `bob`{.literal} as a manager from the `developers`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_remove_member_manager("developers", user="bob")
    ```

Removing an IdM group

:   In this example, you remove the `developers`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.group_del("developers")
    ```

### [4.3. Managing access control with IdM API commands](#managing-access-control-with-idm-api-commands) {#managing-access-control-with-idm-api-commands .title}

You can manage IdM access control programmatically with the IdM API commands. Automating permissions, privileges, and roles ensures consistent security policies and simplifies delegation of administrative tasks.

Adding a permission for creating users

:   In this example, you add a permission for creating users.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.permission_add("Create users", ipapermright='add', type='user')
    ```

Adding a permission for managing group membership

:   In this example, you add a permission for adding users to groups.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.permission_add("Manage group membership", ipapermright='write', type='group', attrs="member")
    ```

Adding a privilege for the user creation process

:   In this example, you add a privilege for creating users, adding them to groups, and managing user certificates.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.permission_add("Create users", ipapermright='add', type='user')
    api.Command.permission_add("Manage group membership", ipapermright='write', type='group', attrs="member")
    api.Command.permission_add("Manage User certificates", ipapermright='write', type='user', attrs='usercertificate')

    api.Command.privilege_add("User creation")
    api.Command.privilege_add_permission("User creation", permission="Create users")
    api.Command.privilege_add_permission("User creation", permission="Manage group membership")
    api.Command.privilege_add_permission("User creation", permission="Manage User certificates")
    ```

Adding a role using a privilege

:   In this example, you add a role using the privilege created in the previous example.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.role_add("usermanager", description="Users manager")
    api.Command.role_add_privilege("usermanager", privilege="User creation")
    ```

Assigning a role to a user

:   In this example, you assign the `usermanager`{.literal} role to the user `bob`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.role_add_member("usermanager", user="bob")
    ```

Assigning a role to a group

:   In this example, you assign the `usermanager`{.literal} role to the `managers`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.role_add_member("usermanager", group="managers")
    ```

### [4.4. Managing sudo rules with IdM API commands](#managing-sudo-rules-with-idm-api-commands) {#managing-sudo-rules-with-idm-api-commands .title}

You can manage sudo rules programmatically with the IdM API commands. Automating sudo rule management helps you control privilege escalation and enforce consistent security policies across your hosts.

Creating a sudo rule

:   In this example, you create a sudo rule that holds time change commands.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudorule_add("timechange")
    ```

Creating a sudo command

:   In this example, you create the `date`{.literal} sudo command.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudocmd_add("/usr/bin/date")
    ```

Attaching a sudo command to a sudo rule

:   In this example, you attach the `date`{.literal} sudo command to the `timechange`{.literal} sudo rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudorule_add_allow_command("timechange", sudocmd="/usr/bin/date")
    ```

Creating and attaching groups of sudo commands

:   In this example, you create multiple sudo commands, add them to a newly created `timecmds`{.literal} sudo command group, and attach the group to the `timechange`{.literal} sudo rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudocmd_add("/usr/bin/date")
    api.Command.sudocmd_add("/usr/bin/timedatectl")
    api.Command.sudocmd_add("/usr/sbin/hwclock")
    api.Command.sudocmdgroup_add("timecmds")
    api.Command.sudocmdgroup_add_member("timecmds", sudocmd="/usr/bin/date")
    api.Command.sudocmdgroup_add_member("timecmds", sudocmd="/usr/bin/timedatectl")
    api.Command.sudocmdgroup_add_member("timecmds", sudocmd="/usr/sbin/hwclock")
    api.Command.sudorule_add_allow_command("timechange", sudocmdgroup="timecmds")
    ```

Denying sudo commands

:   In this example, you deny the `rm`{.literal} command to be run as sudo.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudocmd_add("/usr/bin/rm")
    api.Command.sudorule_add_deny_command("timechange", sudocmd="/usr/bin/rm")
    ```

Adding a user to a sudo rule

:   In this example, you add the user `bob`{.literal} to the `timechange`{.literal} sudo rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudorule_add_user("timechange", user="bob")
    ```

Making a sudo rule available only for a specified host

:   In this example, you restrict the `timechange`{.literal} rule to be available only for the `client.ipa.test`{.literal} host.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudorule_add_host("timechange", host="client.ipa.test")
    ```

Setting sudo rules to be run as a different user

:   By default, sudo rules are run as `root`{.literal}. In this example, you set the `timechange`{.literal} sudo rule to be run as the `alice`{.literal} user instead.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudorule_add_runasuser("timechange", user="alice")
    ```

Setting sudo rules to be run as a group

:   In this example, you set the `timechange`{.literal} sudo rule to be run as the `sysadmins`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudorule_add_runasgroup("timechange", group="sysadmins")
    ```

Setting a sudo option for a sudo rule

:   In this example, you set a sudo option for the `timechange`{.literal} sudo rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudorule_add_option("timechange", ipasudoopt="logfile='/var/log/timechange_log'")
    ```

Enabling a sudo rule

:   In this example, you enable the `timechange`{.literal} sudo rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudorule_enable("timechange")
    ```

Disabling a sudo rule

:   In this example, you disable the `timechange`{.literal} sudo rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.sudorule_disable("timechange")
    ```

### [4.5. Managing Host-based Access Control with IdM API commands](#managing-host-based-access-control-with-idm-api-commands) {#managing-host-based-access-control-with-idm-api-commands .title}

You can manage Host-based Access Control (HBAC) rules programmatically with the IdM API commands. Automating HBAC configuration helps you control which users can access specific services on designated hosts.

Creating an HBAC rule

:   In this example, you create a base rule that will handle SSH service access.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.hbacrule_add("sshd_rule")
    ```

Adding a user to an HBAC rule

:   In this example, you add the user `john`{.literal} to the `sshd_rule`{.literal} HBAC rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.hbacrule_add_user("sshd_rule", user="john")
    ```

Adding a group to an HBAC rule

:   In this example, you add the group `developers`{.literal} to the `sshd_rule`{.literal} HBAC rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.hbacrule_add_user("sshd_rule", group="developers")
    ```

Removing a user from an HBAC rule

:   In this example, you remove the user `john`{.literal} from the `sshd_rule`{.literal} HBAC rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.hbacrule_remove_user("sshd_rule", user="john")
    ```

Registering a new target HBAC service

:   You must register a target service before you can attach it to an HBAC rule. In this example, you register the `chronyd`{.literal} service.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.hbacsvc_add("chronyd")
    ```

Attaching a registered service to an HBAC rule

:   In this example, you attach the `sshd`{.literal} service to the `sshd_rule`{.literal} HBAC rule. This service is registered in IPA by default, so there is no need to register it using `hbacsvc_add`{.literal} beforehand.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.hbacrule_add_service("sshd_rule", hbacsvc="sshd")
    ```

Adding a host to an HBAC rule

:   In this example, you add `workstations`{.literal} host group to the `sshd_rule`{.literal} HBAC rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.hbacrule_add_host("sshd_rule", hostgroup="workstations")
    ```

Testing an HBAC rule

:   In this example, you use the `sshd_rule`{.literal} HBAC rule against the `workstation.ipa.test`{.literal} host. It targets the service `sshd`{.literal} that comes from the user `john`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.hbactest(user="john", targethost="workstation.ipa.test", service="sshd", rules="sshd_rule")
    ```

Enabling an HBAC rule

:   In this example, you enable the `sshd_rule`{.literal} HBAC rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.hbacrule_enable("sshd_rule")
    ```

Disabling an HBAC rule

:   In this example, you disable the `sshd_rule`{.literal} HBAC rule.

    ``` {.language-plaintext tabindex="-1"}
    api.Command.hbacrule_disable("sshd_rule")
    ```

## [Chapter 5. Auditing IdM API operations](#auditing-idm-api-operations) {#chapter-5.-auditing-idm-api-operations .title}

Identity Management (IdM) servers use the `systemd`{.literal} journal to create audit records of all IdM API operations. Querying these logs helps you track who performed actions, troubleshoot issues, and meet compliance requirements.

### [5.1. Overview of IdM API auditing](#overview-of-idm-api-auditing) {#overview-of-idm-api-auditing .title}

An IdM server records any use of the Identity Management (IdM) API in the `systemd`{.literal} journal. This unified logging method helps you audit API operations and identify security events across your IdM deployment.

The `systemd`{.literal} journal allows for centralized collection of logs from individual systems, which can then be queried and filtered.

Each log entry is tagged with an `IPA.API`{.literal} marker and contains the following details in a structured format:

-   The authenticated Kerberos principal that performed the action, or `` ` if the operation was performed by the `root ``{.literal} user directly on the server through LDAPI.
-   The name of the API command that was executed.
-   The result of the execution, which is either `SUCCESS`{.literal} or an exception name.
-   An LDAP backend instance identifier, which is the same for all operations performed as part of the same request.
-   A list of arguments and options passed to the command, in JSON format.

You can query these entries with the `journalctl`{.literal} utility. Using `journalctl`{.literal} with the `-x`{.literal} option provides a more detailed, human-readable explanation of the log entry, including links to the relevant documentation.

Note

All IdM API audit entries have a `MESSAGE_ID`{.literal} property set to the application UID `6d70f1b493df36478bc3499257cd3b17`{.literal}.

### [5.2. Viewing the IdM API audit logs](#viewing-the-idm-api-audit-logs) {#viewing-the-idm-api-audit-logs .title}

You can view the IdM API audit logs by querying the `systemd`{.literal} journal. Filtering and inspecting these logs helps you investigate specific operations and understand the details of API calls.

**Prerequisites**

-   You have root access to the IdM server.

**Procedure**

1.  To see a list of all IdM API operations recorded in the journal, filter the journal for the `IPA.API`{.literal} marker:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -g IPA.API
    May 23 10:30:15 idmserver.idm.example.com /usr/bin/ipa[247422]: [IPA.API] [autobind]: user_del: SUCCESS [ldap2_140328582446688] {"uid": ["example_user"], "continue": false, "version": "2.253"}
    May 23 10:32:01 idmserver.idm.example.com /usr/bin/ipa[247555]: [IPA.API] admin@IDM.EXAMPLE.COM: user_add: SUCCESS [ldap2_140328582446999] {"uid": ["new_user"], "givenname": "New", "sn": "User", "cn": "New User"}
    May 23 10:33:10 idmserver.idm.example.com /mod_wsgi[247035]: [IPA.API] admin@IDM.EXAMPLE.COM: ping: SUCCESS [ldap2_139910420944784] {"version": "2.253"}
    May 23 10:34:05 idmserver.idm.example.com /usr/bin/ipa[247888]: [IPA.API] [autobind]: group_add_member: SUCCESS [ldap2_140328582447111] {"cn": "admins", "user": "new_user"}
    ```

    The output shows a summary of each API call, including the user, the command, the result, the unique connection ID, and the parameters used.

2.  Identify the unique identifier for the specific entry you want to inspect. For example, the `user_del`{.literal} call has the LDAP backend instance identifier `ldap2_140328582446688`{.literal}.

3.  Use `journalctl`{.literal} with the `-x`{.literal} option and the unique identifier value to get a detailed explanation of the user deletion log entry:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -x -g ldap2_140328582446688
    May 23 10:30:15 idmserver.idm.example.com /usr/bin/ipa[255232]: [IPA.API] [autobind]: user_del: SUCCESS [ldap2_140328582446688] {"uid": ["example_user"], "continue": false, "version": "2.253"}
    -- Subject: IdM API command was executed and result of its execution was audited
    -- Defined-by: FreeIPA
    -- Support: https://lists.fedorahosted.org/archives/list/freeipa-users@lists.fedorahosted.org/
    -- Documentation: man:ipa(1)
    -- Documentation: https://freeipa.readthedocs.io/en/latest/api/index.html
    -- Documentation: https://freeipa.readthedocs.io/en/latest/api/user_del.html

    -- Identity Management provides an extensive API that allows to manage all aspects of IdM deployments.

    -- The following information about the API command executed is available:

    -- [IPA.API] [autobind]: user_del: SUCCESS [ldap2_140328582446688] {"uid": ["example_user"], "continue": false, "version": "2.253"}

    -- The command was executed by '/usr/bin/ipa' utility. If the utility name
    -- is '/mod_wsgi`, then this API command came from a remote source through the IdM
    -- API end-point.

    -- The message includes following fields:

    --   - executable name and PID ('/mod_wsgi' for HTTP end-point; in this case it
    --     was '/usr/bin/ipa' command)

    --   - '[IPA.API]' marker to allow searches with 'journalctl -g IPA.API'

    --   - authenticated Kerberos principal or '[autobind]' marker for LDAPI-based
    --     access as root. In this case it was '[autobind]'

    --   - name of the command executed, in this case 'user_del'

    --   - result of execution: SUCCESS or an exception name. In this case it was
    --     'SUCCESS'

    --   - LDAP backend instance identifier. The identifier will be the same for all
    --     operations performed under the same request. This allows to identify operations
    --     which were executed as a part of the same API request instance. For API
    --     operations that didn't result in LDAP access, there will be
    --     '[no_connection_id]' marker.

    --   - finally, a list of arguments and options passed to the command is provided
    --     in JSON format.

    -- ---------
    -- The following list of arguments and options were passed to the command
    -- 'user_del' by the '[autobind]' actor:
    --
    -- {"uid": ["example_user"], "continue": false, "version": "2.253"}
    -- ---------

    -- A detailed information about Identity Management API can be found at upstream documentation API reference:
    -- https://freeipa.readthedocs.io/en/latest/api/index.html

    -- For details on the IdM API command 'user_del' see
    -- https://freeipa.readthedocs.io/en/latest/api/user_del.html
    ```

## [Legal Notice](#idm139879850443184) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
