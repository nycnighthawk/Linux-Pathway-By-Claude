---
{"title": "Composing a customized RHEL system image", "guide": "composing_a_customized_rhel_system_image", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/composing_a_customized_rhel_system_image/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Composing a customized RHEL system image {#composing-a-customized-rhel-system-image .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Creating customized system images with RHEL image builder on RHEL 10.0 {#creating-customized-system-images-with-rhel-image-builder-on-rhel-10.0 .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139688764001040)

**Abstract**

RHEL image builder is a tool for creating deployment-ready customized system images: installation disks, virtual machines, cloud vendor-specific images, and others. By using RHEL image builder, you can create these images faster compared to manual procedures, because it eliminates the specific configurations required for each output type.

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

## [Chapter 1. RHEL image builder description](#image-builder-description) {#chapter-1.-rhel-image-builder-description .title}

You can create customized RHEL system images, including for cloud platforms, by using RHEL image builder. It automatically handles setup details for each output type, making image creation faster than manual methods. You can access it by using the `image-builder`{.literal} CLI or the RHEL web console.

Important

The `image-builder`{.literal} tool is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Do not use them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

The `image-builder`{.literal} tool has the following characteristics:

-   It provides a simpler installation and environment configuration.
-   You can work with a container-friendly daemonless model, removing the complexity of a client/server architecture.
-   You can use the `image-builder`{.literal} tool for automated pipelines and container-based builds.
-   You can create a container image to use as a portable environment to build other images.

### [1.1. RHEL image builder terminology](#image-builder-terminology) {#rhel-image-builder-terminology .title}

RHEL image builder uses specific terminology for its core concepts.

Blueprint

:   A blueprint is a description of a customized system image. It lists the packages and customizations that will be part of the system. You can edit blueprints with customizations and save them as a particular version. When you create a system image from a blueprint, the image is associated with the blueprint in the RHEL image builder interface.

    Create blueprints in the TOML format.

Compose
:   Composes are individual builds of a system image, based on a specific version of a particular blueprint. Compose as a term refers to the system image, the logs from its creation, inputs, metadata, and the process itself.

Customizations
:   Customizations are specifications for the image that are not packages. This includes users, groups, and SSH keys.

### [1.2. RHEL image builder output formats](#image-builder-mage-builder-output-formats) {#rhel-image-builder-output-formats .title}

RHEL image builder can create images in multiple output formats shown in the table.

+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| Description                 | CLI name                              | File extension                | Architecture                                                                    |
+:============================+:======================================+:==============================+:================================================================================+
| Amazon Web Services         | `ami`{.literal}                       | `.ami`{.literal .filename}    | `aarch64`{.literal}, `x86_64`{.literal}                                         |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| Disk Archive                | `tar`{.literal}                       | `.tar`{.literal .filename}    | `aarch64`{.literal}, `x86_64`{.literal}, `ppc64le`{.literal}, `s390x`{.literal} |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| Google Cloud                | `gce`{.literal}                       | `.tar.gz`{.literal .filename} | `x86_64`{.literal}                                                              |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| Microsoft Azure             | `vhd`{.literal}                       | `.vhd`{.literal .filename}    | `aarch64`{.literal}, `x86_64`{.literal}                                         |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| OpenStack                   | `qcow2`{.literal}                     | `.qcow2`{.literal .filename}  | `aarch64`{.literal}, `x86_64`{.literal}, `ppc64le`{.literal}, `s390x`{.literal} |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| Oracle Cloud Infrastructure | `.oci`{.literal .filename}            | `.qcow2`{.literal .filename}  | `x86_64`{.literal}                                                              |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| QEMU Image                  | `qcow2`{.literal}                     | `.qcow2`{.literal .filename}  | `aarch64`{.literal}, `x86_64`{.literal}, `ppc64le`{.literal}, `s390x`{.literal} |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| RHEL Installer              | `image-installer`{.literal}           | `.iso`{.literal .filename}    | `aarch64`{.literal}, `x86_64`{.literal}                                         |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| VMware vSphere              | `vmdk`{.literal}                      | `.vmdk`{.literal .filename}   | `x86_64`{.literal}                                                              |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| VMware vSphere              | `ova`{.literal}                       | `.ova`{.literal .filename}    | `x86_64`{.literal}                                                              |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| Vagrant                     | `vagrant-libvirt`{.literal .filename} | `.qcow2`{.literal .filename}  | `aarch64`{.literal}, `x86_64`{.literal}                                         |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+
| Windows Subsystem for Linux | `wsl`{.literal}                       | `.wsl`{.literal .filename}    | `aarch64`{.literal}, `x86_64`{.literal}                                         |
+-----------------------------+---------------------------------------+-------------------------------+---------------------------------------------------------------------------------+

: Table 1.1. RHEL image builder output formats

Show more

To check the supported types, run the command:

``` {.language-plaintext tabindex="-1"}
# image-builder list
```

### [1.3. Supported architectures for image builds](#supported-architectures-for-image-builds) {#supported-architectures-for-image-builds .title}

RHEL image builder supports building images for several architectures.

The supported architectures include:

-   AMD and Intel 64-bit (`x86_64`{.literal})
-   ARM64 (`aarch64`{.literal})
-   IBM Z (`s390x`{.literal})
-   IBM POWER systems (`ppc64`{.literal})

However, RHEL image builder does not support multi-architecture builds. It only builds images of the same system architecture that it is running on. For example, if RHEL image builder is running on an `x86_64`{.literal} system, it can only build images for the `x86_64`{.literal} architecture.

### [1.4. Additional resources](#image-builder-description_14-additional-resources) {#additional-resources .title}

-   [RHEL image builder additional documentation index](https://access.redhat.com/articles/7080686)

## [Chapter 2. Installing RHEL image builder](#installing-rhel-image-builder) {#chapter-2.-installing-rhel-image-builder .title}

RHEL image builder is a tool for creating custom system images. Before using RHEL image builder, you must install it.

### [2.1. RHEL image builder system requirements](#image-builder-system-requirements-adoc) {#rhel-image-builder-system-requirements .title}

The host that runs RHEL image builder must meet the minimum system requirements.

+----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Parameter            | Minimal Required Value                                                                                                                 |
+:=====================+:=======================================================================================================================================+
| System type          | A dedicated host or virtual machine. RHEL image builder is not supported in containers, including Red Hat Universal Base Images (UBI). |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Processor            | 2 cores                                                                                                                                |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Memory               | 4 GiB                                                                                                                                  |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Disk space           | 20 GiB of free space in the `/var/cache/`{.literal} filesystem                                                                         |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Access privileges    | root                                                                                                                                   |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Network              | Internet connectivity to the Red Hat Content Delivery Network (CDN).                                                                   |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------+

: Table 2.1. RHEL image builder system requirements

Show more

Note

If you do not have internet connectivity, use RHEL image builder in isolated networks. For that, you must override the default repositories to point to your local repositories to not connect to Red Hat Content Delivery Network (CDN). Ensure that you have your content mirrored internally or use Red Hat Satellite.

**Additional resources**

-   [Configuring RHEL image builder repositories](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10\/html/composing_a_customized_rhel_system_image/setting-repositories)
-   [Provisioning Using a Red Hat Image Builder Image](https://docs.redhat.com/en/documentation/red_hat_satellite/6.6/html/provisioning_guide/provisioning_using_a_red_hat_image_builder_image)

### [2.2. Installing RHEL image builder](#installing-image-builder) {#installing-rhel-image-builder .title}

Install RHEL image builder to have access to all the `image-builder`{.literal} packages functionalities.

**Prerequisites**

-   You are logged in to the Red Hat Enterprise Linux host on which you want to install RHEL image builder.
-   The Red Hat Enterprise Linux host is subscribed to Red Hat Subscription Manager (RHSM) or Red Hat Satellite.
-   You have enabled the `BaseOS`{.literal} and `AppStream`{.literal} repositories to be able to install the RHEL image builder packages.

**Procedure**

1.  Install RHEL image builder and other necessary packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install image-builder cockpit-image-builder
    ```

    -   `image-builder`{.literal} is a service to build customized RHEL operating system images and enables access to the CLI interface.
    -   `cockpit-image-builder`{.literal} is a package that enables access to the Web UI interface. The web console is installed as a dependency of the `cockpit-image-builder`{.literal} package.

2.  If you want to use RHEL image builder in the web console, enable and start it.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now cockpit.socket
    ```

    The `image-builder`{.literal} and `cockpit`{.literal} services start automatically on first access.

**Verification**

-   Verify that the installation works by running `image-builder`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder list
    ```

## [Chapter 3. Configuring RHEL image builder repositories](#setting-repositories) {#chapter-3.-configuring-rhel-image-builder-repositories .title}

You can add repositories or override the default base repositories.

You can use the following types of repositories in RHEL image builder:

Official repository overrides
:   Use these to download base system RPMs from a custom mirror, instead of the Red Hat Content Delivery Network (CDN). Official repositories overrides disables the default repositories, and your custom mirror must contain all the necessary packages.

Custom third-party repositories
:   Use these to include packages that are not available in the official RHEL repositories.

### [3.1. Adding additional repositories to RHEL image builder](#adding-custom-third-party-repositories-to-rhel-image-builder) {#adding-additional-repositories-to-rhel-image-builder .title}

You can add custom repositories to your image during the image-building process by using the `image-builder-cli`{.literal} tool.

Depending on your repository requirements, use one of the following options:

-   `--extra-repo`{.literal}: Use for standard, unauthenticated custom repositories.

-   `--force-repo-dir`{.literal}: Use to completely override the built-in repositories with a local directory containing custom repository definitions, such as Satellite or EUS repositories. The build process uses these repositories only to download packages, and does not configure or include them in the final output artifact.

    Note

    If you use `--force-repo-dir`{.literal}, only the specific distributions defined within your custom repository directory are available to the image builder. If you override the base repositories, you must explicitly define both the BaseOS and AppStream repositories in your configuration file, or the image build fails.

**Prerequisites**

-   You have the URL of the custom repository.
-   Optional: If you use the `--force-repo-dir`{.literal} option, you must have a local directory that contains a JSON configuration file named exactly after the distribution version you are building. For example, `rhel-98.json`{.literal} for RHEL 9.8.

**Procedure**

-   Build the image and include additional repositories to RHEL image builder by using one of the following options:

    -   Add standard repositories by using `--extra-repo`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        $ image-builder build <image-type> \
        --extra-repo=https://server.example.com/<your-repo>/_ \
        ```

        The repository content becomes available during the image building, and the dependency solver gets packages from the repository. For example, if the repository contains a `libc`{.literal} or `kernel`{.literal} with higher version, their content is selected over the default repositories.

    -   Override base repositories by using \--force-repo-dir:

        Use this option to completely override default configurations, such as when building images with Extended Update Support (EUS) repositories or custom Satellite configurations.

        1.  Create a directory, for example, `/tmp/custom-repos/`{.literal}.

        2.  Inside that directory, create a JSON file. The file name must match the specific RHEL distribution name, for example, `rhel-96.json`{.literal} for RHEL 9.6.

        3.  Define the repository structures for your architecture within this file. The file must include definitions for both BaseOS and AppStream to build properly, though you can add extra custom repositories here as well. For example, to build using EUS repositories:

            ``` {.language-plaintext tabindex="-1"}
            {
                "x86_64": [
                    {
                        "name": "baseos",
                        "metalink": "",
                        "baseurl": "https://cdn.redhat.com/content/dist/rhel10/10/x86_64/baseos/os/",
                        "mirrorlist": "",
                        "gpgkey": "file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release",
                        "check_gpg": true,
                        "metadata_expire": "",
                        "rhsm": true
                    },
                    {
                        "name": "appstream",
                        "metalink": "",
                        "baseurl": "https://cdn.redhat.com/content/dist/rhel10/10/x86_64/appstream/os/",
                        "mirrorlist": "",
                        "gpgkey": "file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release",
                        "check_gpg": true,
                        "metadata_expire": "",
                        "rhsm": true
                    },
                    {
                      "name": "kernel-rt",
                      "baseurl": "https://cdn.redhat.com/content/dist/rhel10/10/x86_64/rt/os",
                      "gpgkey":  "file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release",
                      "rhsm": true,
                      "check_gpg": true
                }
                ]
            }
            ```

        4.  Run the build command, pointing to the **directory** containing your JSON file. Do not point directly to the file itself:

            ``` {.language-plaintext tabindex="-1"}
            $ image-builder build <image-type> --distro=rhel-10.2 --force-repo-dir=/tmp/custom-repos/
            ```

            After the image building process finishes, the image is available for your use at the directory where you create it.

**Verification**

-   Check the build logs and the dependency solver logs generated during the build process to confirm that the package was fetched from your specified repository URL rather than the default Red Hat repositories.

### [3.2. Adding third-party repositories with specific distributions to RHEL image builder](#adding-third-party-repositories-with-specific-distributions-to-rhel-image-builder) {#adding-third-party-repositories-with-specific-distributions-to-rhel-image-builder .title}

You can add custom repositories and specify a distribution to your image by using the `image-builder`{.literal} tool and with `--extra-repo`{.literal} flag.

**Prerequisites**

-   You have the custom repository URL.

**Procedure**

-   Build the image, and add the extra repository source and the chosen distribution system to RHEL image builder:

    ``` {.language-plaintext tabindex="-1"}
    $ image-builder build <image-type> \
    --extra-repo https://server.example.com/<your-repo>/_ \
    --distro rhel-10.0
    ```

### [3.3. Overriding a system repository during image build](#overriding-a-system-repository) {#overriding-a-system-repository-during-image-build .title}

Override the default base repositories during image build.

**Prerequisites**

-   You have a custom repository that is accessible from your host system.

**Procedure**

1.  Build the image, and add the extra repository to RHEL image builder:

    ``` {.language-plaintext tabindex="-1"}
    $ image-builder build <image-type> \
    --force-repo=https://server.example.com/<your-repo>/_
    ```

    Warning

    The RHEL image builder tool uses the repositories that you defined to solve all dependencies, which could cause issues for your system.

### [3.4. Configuring and using Satellite CV as a content source](#configuring-and-using-satellite-cv-as-a-content-source) {#configuring-and-using-satellite-cv-as-a-content-source .title}

You can use Satellite's content views (CV) as custom repositories to build images with RHEL image builder. With custom repositories, you can configure your Satellite-registered hosts to pull packages from your local Satellite repositories instead of the Red Hat Content Delivery Network (CDN).

**Prerequisites**

-   You have installed RHEL image builder. See [Installing RHEL image builder](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/installing-rhel-image-builder#installing-image-builder).
-   The host running RHEL image builder is registered to Red Hat Satellite and has access to the required Content Views. See [Registering hosts to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html/managing_hosts/registering-hosts-to-satellite).
-   You have downloaded or located the GPG public key used by your Satellite organization to sign packages, which is typically available by using your Satellite Server's web interface or at `/etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release`{.literal}.

**Procedure**

1.  Locate your Satellite repository base URLs for your content view by logging in to the Red Hat Satellite web UI or checking your host's repository configuration. You need both the `BaseOS`{.literal} and `AppStream`{.literal} URLs.

    -   **BaseOS repository URL example**

        ``` {.language-plaintext tabindex="-1"}
        https://satellite6.example.com/pulp/content/<your_org>/<your_env>/<your_cv>/content/dist/rhel10/10/x86_64/baseos/os
        ```

    -   **AppStream repository URL example**

        ``` {.language-plaintext tabindex="-1"}
        https://satellite6.example.com/pulp/content/<your_org>/<your_env>/<your_cv>/content/dist/rhel10/10/x86_64/appstream/os
        ```

2.  Create a custom repository directory and configuration file. Because Satellite repositories require Red Hat Subscription Management (RHSM) certificates for authentication, you must define them in a custom repository configuration file instead of passing them directly by using the command-line flags.

    a.  Create a directory to store your repository overrides:

        ``` {.language-plaintext tabindex="-1"}
        $ mkdir ./repos
        ```

    b.  Create a YAML file inside that directory matching your host's distribution architecture. The file must use the `.yaml`{.literal} or `.json`{.literal} extension, for example, `repos/rhel-10.2.yaml`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        x86_64:
         - name: "RHEL 10 BaseOS - Satellite"
           baseurl: "https://satellite6.example.com/pulp/content/<your_org>/<your_env>/<your_cv>/content/dist/rhel10/10/x86_64/baseos/os"
           rhsm: true
           check_gpg: true
           gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

         - name: "RHEL 10 AppStream - Satellite"
           baseurl: "https://satellite6.example.com/pulp/content/<your_org>/<your_env>/<your_cv>/content/dist/rhel10/10/x86_64/appstream/os"
           rhsm: true
           check_gpg: true
           gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
        ```

3.  Build the image and point to the directory containing your custom repository file by using the `--force-repo-dir`{.literal} flag:

    ``` {.language-plaintext tabindex="-1"}
    $ image-builder build <image-type> \
    --force-repo-dir=./repos \
    --blueprint <blueprint_name>.toml
    ```

**Additional resources**

-   [Managing content views](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html/managing_content/managing_content_views_content-management)
-   [Image Builder with Satellite Repository -- CDN used instead of Satellite when building RHEL images](https://access.redhat.com/solutions/7140182)

### [3.5. Using Satellite CV as repositories to build images in RHEL image builder](#using-satellite-cv-as-repositories-to-build-images-in-rhel-image-builder) {#using-satellite-cv-as-repositories-to-build-images-in-rhel-image-builder .title}

Configure RHEL image builder to use Satellite's content views (CV) as repositories to build your custom images.

**Prerequisites**

-   You have integrated Satellite with RHEL web console. See [Enabling the RHEL web console on Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html/managing_hosts/host-management-and-monitoring-by-using-cockpit#Enabling_Cockpit_on_Server_managing-hosts).

**Procedure**

1.  In the Satellite web UI, navigate to **Content**, locate **Products**, select your **Product**, and click the repository you want to use.
2.  Search for the secured URL (HTTPS) in the `Published`{.literal} field and copy it.
3.  Use the URL that you copied as a base URL for the Red Hat image builder repository. See [Adding custom third-party repositories to RHEL image builder](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/setting-repositories#adding-custom-third-party-repositories-to-rhel-image-builder).

**Next steps**

-   Build the image. See [Creating a system image by using RHEL image builder in the web console interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-gui).

## [Chapter 4. Creating system images by using the RHEL image builder CLI](#creating-system-images-with-cli) {#chapter-4.-creating-system-images-by-using-the-rhel-image-builder-cli .title}

RHEL image builder is a tool for creating custom system images. To control RHEL image builder and create your custom system images, you can use the command line (CLI) or the web console interface.

### [4.1. Introducing the RHEL image builder command-line interface](#introducing-the-rhel-image-builder-command-line-interface) {#introducing-the-rhel-image-builder-command-line-interface .title}

You can use the RHEL image builder command-line interface (CLI) to create blueprints, by running the `image-builder`{.literal} command with the suitable options and subcommands.

By default, you must run the `image-builder`{.literal} command as a root user.

The workflow for the command line can be summarized as follows:

1.  Create a blueprint or export an existing blueprint definition to a plain text file.
2.  Optional: Edit this file in a text editor.
3.  Import the blueprint text file back into image builder.
4.  Run a compose to build an image from the blueprint.
5.  Export the image file to download it.

Apart from the basic subcommands to create a blueprint, you can use the `image-builder`{.literal} command with many subcommands to examine the state of configured blueprints and composes.

### [4.2. RHEL image builder blueprint format](#rhel-image-builder-blueprint-format) {#rhel-image-builder-blueprint-format .title}

With RHEL image builder, you can use blueprints in both the `.toml`{.literal} and `.json`{.literal} formats.

A typical blueprint file includes the following elements:

The blueprint metadata

:   ``` {.language-plaintext tabindex="-1"}
    name = "<blueprint_name>"
    description = "<long_form_description_text>"
    version = "<version>"
    ```

    The *`<blueprint_name>`{.literal}* and *`<long_form_description_text>`{.literal}* fields are the name and description for your blueprint.

    The *`<version>`{.literal}* is a version number according to the Semantic Versioning scheme, and is present only once for the entire blueprint file.

Groups to include in the image

:   ``` {.language-plaintext tabindex="-1"}
    [[groups]]
    name = "<group_name>"
    ```

    The *`<group_name>`{.literal}* entry describes a group of packages to be installed into the image. Groups use the following package categories:

    -   Mandatory

    -   Default

    -   Optional

        The *`group-name`{.literal}* is the name of the group, for example, **anaconda-tools**, **widget**, **wheel**, or **users**. Blueprints install the mandatory and default packages. There is no mechanism for selecting optional packages.

Packages to include in the image

:   ``` {.language-plaintext tabindex="-1"}
    [[packages]]
    name = "<package_name>"
    version = "<package_version>"
    ```

    *`package-name`{.literal}* is the name of the package, such as `httpd`{.literal .package}, `gdb-doc`{.literal .package}, or `coreutils`{.literal .package}.

    *`package-version`{.literal}* is a version to use. In this field, you can specify ‎`dnf`{.literal} version constraints as follows:

    -   For a specific version, use the exact version number, such as `8.7.0`{.literal}.

    -   For the latest available version, use the asterisk `*`{.literal}.

    -   For the latest minor version, use a format such as `8.*`{.literal}.

        Repeat this block for every package to include.

        Note

        There are no differences between packages and modules in the RHEL image builder tool. RHEL image builder treats both as RPM Package Manager (RPM) package dependencies.

### [4.3. Creating a blueprint by using the command line](#creating-a-blueprint-by-using-the-command-line-interface) {#creating-a-blueprint-by-using-the-command-line .title}

You can create a new blueprint by using the command line (CLI). The blueprint describes the final image and its customizations, such as packages and kernel customizations.

**Prerequisites**

-   You are logged in as the root user or a user who is a member of the `weldr`{.literal} group

**Procedure**

1.  Create a plain text file with the following contents:

    ``` {.language-plaintext tabindex="-1"}
    name = "<blueprint_name>"
    description = "<long_form_description>"
    version = "<0.0.1>"
    modules = []
    groups = []
    ```

    Replace *`<blueprint_name>`{.literal}* and *`<long_form_description>`{.literal}* with a name and description for your blueprint.

    Replace *`<0.0.1>`{.literal}* with a version number according to the Semantic Versioning scheme.

2.  For every package that you want to be included in the blueprint, add the following lines to the file:

    ``` {.language-plaintext tabindex="-1"}
    [[packages]]
    name = "<package_name>"
    version = "<package_version>"
    ```

    Replace *`<package_name>`{.literal}* with the name of the package, such as `httpd`{.literal}, `gdb-doc`{.literal}, or `coreutils`{.literal}.

    Optionally, replace *`<package_version>`{.literal}* with the version to use. This field supports `dnf`{.literal .command} version specifications:

    -   For a specific version, use the exact version number such as `9.6.0`{.literal}.
    -   For the latest available version, use the asterisk `*`{.literal}
    -   For the latest minor version, use formats such as `9.*`{.literal}.

3.  Customize your blueprints to suit your needs. For example, disable Simultaneous Multi Threading (SMT), add the following lines to the blueprint file:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.kernel]
    append = "nosmt=force"
    ```

    For additional customizations available, see [Supported image customizations](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/supported-image-customizations).

    Note that `[]`{.literal} and `[[]]`{.literal} are different data structures expressed in TOML.

    -   The `[customizations.kernel]`{.literal} header represents a single table that defines collection of keys and their corresponding value pairs, for example: `append = "nosmt=force"`{.literal}.
    -   The `[[packages]]`{.literal} header represents an array of tables. The first instance defines the array and its first table element, such as `name = "package-name"`{.literal} and `version = "package-version"`{.literal}. Each subsequent instance adds a new element in the order that you define them.

4.  Save the file, for example, as *`<blueprint_name>`{.literal}*`.toml`{.literal} and close the text editor.

**Additional resources**

-   [Composing a customized RHEL system image with proxy server (Red Hat Knowledgebase)](https://access.redhat.com/solutions/5720761)

### [4.4. Creating a system image with RHEL image builder on the command line](#creating-a-system-image-with-rhel-image-builder-in-the-command-line-interface) {#creating-a-system-image-with-rhel-image-builder-on-the-command-line .title}

To build a customized RHEL image by using the RHEL image builder command-line interface, you must specify a blueprint and an image type. Optionally, you can also specify a distribution.

If you do not specify a distribution, it uses the same distribution and version as the host system. The architecture is also the same as the one on the host.

**Prerequisites**

-   You have a blueprint prepared for the image.

**Procedure**

1.  Optional: List the image formats you can create:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder list
    ```

2.  Start the compose:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder build <image_type> --blueprint <blueprint_name>
    ```

    -   Replace *`<blueprint_name>`{.literal}* with the name of the blueprint, and *`<image_type>`{.literal}* with the type of the image.
    -   If you do not specify a distro, `image-builder`{.literal} uses the same distribution and version as the host system.

**Result**

The compose process takes some minutes to complete. You can follow the image building steps until the image is ready.

After the image building process finishes, the image is available for your use at the directory where you create it.

### [4.5. Basic RHEL image builder command-line commands](#basic-rhel-image-builder-command-line-commands) {#basic-rhel-image-builder-command-line-commands .title}

Use the RHEL image builder command-line interface to run these basic `image-builder`{.literal} commands.

List all available images

:   ``` {.language-plaintext tabindex="-1"}
    # image-builder list
    ```

Filter images by name

:   ``` {.language-plaintext tabindex="-1"}
    # image-builder list-images --filter "rhel"
    ```

Filter by distribution and architecture

:   ``` {.language-plaintext tabindex="-1"}
    # image-builder list-images --filter "distro:rhel-10" --filter "arch:s390x"
    ```

    Note

    The `--filter`{.literal} argument does not support multiple `key:value`{.literal} pairs within a single expression. To combine multiple filters and narrow down your results, pass each filter individually using a separate `--filter`{.literal} flag.

Change output format

:   ``` {.language-plaintext tabindex="-1"}
    # image-builder list-images --filter "distro:rhel-10" --format=json | jq
    ```

    ``` {.language-plaintext tabindex="-1"}
    # image-builder list-images --filter "distro:rhel-10" --format=shell
    ```

Building images

:   ``` {.language-plaintext tabindex="-1"}
    # image-builder build <image-type>
    ```

    *\<image-type\>* is the image type supported for RHEL image builder, such as `qcow2`{.literal}, `wsl`{.literal}, and so on.

Specify a distribution

:   ``` {.language-plaintext tabindex="-1"}
    # image-builder build <image-type> --distro <distro>
    ```

Show the progress of the image creation and detailed steps

:   ``` {.language-plaintext tabindex="-1"}
    # image-builder build <image-type> --distro <distro> --with-buildlog
    ```

Cross-architecture build

:   ``` {.language-plaintext tabindex="-1"}
    # image-builder build <image-type> --arch=riscv64
    ```

Add a custom repository to the build

:   ``` {.language-plaintext tabindex="-1"}
    # image-builder build <image-type> --extra-repo=<file:///path/to/my/repo>
    ```

### [4.6. Enabled services on custom images](#enabled-services-on-custom-images) {#enabled-services-on-custom-images .title}

When you configure a custom image by using RHEL image builder to the RHEL version and image type determine the default services that the image uses.

For example, use the `ami`{.literal} image type to enable the `sshd`{.literal}, `chronyd`{.literal}, and `cloud-init`{.literal} services by default. If these services are not enabled, the custom image does not boot.

+-----------------------------------+---------------------------------------------------------------------------------+
| Image type                        | Default enabled Services                                                        |
+:==================================+:================================================================================+
| `ami`{.literal}                   | sshd, cloud-init, cloud-init-local, cloud-config, cloud-final                   |
+-----------------------------------+---------------------------------------------------------------------------------+
| `openstack`{.literal}             | sshd, cloud-init, cloud-init-local, cloud-config, cloud-final                   |
+-----------------------------------+---------------------------------------------------------------------------------+
| `qcow2`{.literal}                 | cloud-init                                                                      |
+-----------------------------------+---------------------------------------------------------------------------------+
| `tar`{.literal}                   | Do not enable extra services by default                                         |
+-----------------------------------+---------------------------------------------------------------------------------+
| `vhd`{.literal}                   | sshd, chronyd, waagent, cloud-init, cloud-init-local, cloud-config, cloud-final |
+-----------------------------------+---------------------------------------------------------------------------------+
| `vmdk`{.literal}                  | sshd, chronyd, vmtoolsd, cloud-init                                             |
+-----------------------------------+---------------------------------------------------------------------------------+

: Table 4.1. Enabled services to support image type creation

Show more

Note

You can customize which services to enable during the system boot. However, the customization does not override services enabled by default for the mentioned image types.

**Additional resources**

-   [Supported image customizations](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/supported-image-customizations)

## [Chapter 5. Supported image customizations](#supported-image-customizations) {#chapter-5.-supported-image-customizations .title}

You can customize your image by adding customizations to your blueprint, such as adding an additional RPM package, enabling a service, or customizing a kernel command line parameter.

You can use several image customizations within blueprints. By using the customizations, you can add packages and groups to the image that are not available in the default packages. To use these options, configure the customizations in the blueprint and import (push) it to the RHEL image builder.

### [5.1. Selecting a distribution](#selecting-a-distribution) {#selecting-a-distribution .title}

You can use the `distro`{.literal} field to specify the distribution to use when composing your images or solving dependencies in the blueprint.

If you leave the distro field empty, the blueprint uses the host distribution. Use repository overrides to download base system RPMs from a custom mirror instead of the Red Hat Content Delivery Network (CDN). This disables the default repositories, so your custom mirror must contain all necessary packages.

You can build images for older major versions on a newer system. For example, you can use a RHEL 10 host to create RHEL 9 and RHEL 8 images. However, you cannot build images for newer major versions on an older system.

Important

You cannot build an operating system image that differs from the RHEL image builder host. For example, you cannot use a RHEL system to build Fedora or CentOS images.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize the blueprint with the RHEL distribution to always build the specified RHEL image:

    ``` {.language-plaintext tabindex="-1"}
    name = "blueprint_name"
    description = "blueprint_version"
    version = "0.1"
    distro = "different_minor_version"
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    name = "tmux"
    description = "tmux image with openssh"
    version = "1.2.16"
    distro = "rhel-9.6"
    ```

    Replace `"`{.literal}*`different_minor_version`{.literal}*`"`{.literal} to build a different minor version, for example, if you want to build a RHEL 9.6 image, use `distro = "rhel-96"`{.literal}. On RHEL 9.5 image, you can build minor versions such as RHEL 9.4, RHEL 9.3, and earlier releases.

### [5.2. Selecting a package group](#selecting-a-package-group) {#selecting-a-package-group .title}

Customize the blueprint with package groups. The `groups`{.literal} list describes the groups of packages that you want to install into the image.

Package groups are defined in the repository metadata, each group with a descriptive name and an ID. Use the ID to list a group. Groups categorize packages as mandatory, default, or optional. The blueprint installs only mandatory and default packages, and you cannot select optional packages.

The `name`{.literal} attribute is a required string and must match exactly the package group ID in the repositories.

Note

Currently, there are no differences between packages and modules. Both are treated as RPM package dependencies.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize your blueprint with a package group:

    ``` {.language-plaintext tabindex="-1"}
    [[groups]]
    name = "<group_name>"
    ```

    Replace *`group_name`{.literal}* with the name of the group. For example:

    ``` {.language-plaintext tabindex="-1"}
    [[groups]]
    name = "anaconda-tools"
    ```

### [5.3. Selecting a package](#selecting-a-package) {#selecting-a-package .title}

Customize the blueprint with packages and modules. The `name`{.literal} attribute is a mandatory string that can be an exact match, or a filesystem glob that uses `*`{.literal} for wildcards, and `?`{.literal} for character matching.

The optional `version`{.literal} attribute accepts an exact match or a glob pattern using `*`{.literal} for wildcards, and `?`{.literal} for character matching. If you do not enter a version, the system uses the latest version in the repositories.

When you use a virtual provider as the package name, the version glob must be `*`{.literal}. Consequently, you are not able to freeze the blueprint because the provider expands into multiple packages with their own names and versions.

Note

Currently, there are no differences between packages and modules. RHEL image builder treat both as an RPM package dependencies.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize your blueprint with a package:

    ``` {.language-plaintext tabindex="-1"}
    [[packages]]
    name = "<package_name>"
    ```

    Replace *`package_name`{.literal}* with the name of the package. For example, the `tmux-2.9a`{.literal} and the `openssh-server-8.*`{.literal} packages.

    ``` {.language-plaintext tabindex="-1"}
    [[packages]]
    name = "tmux"
    version = "2.9a"

    [[packages]]
    name = "openssh-server"
    version = "8.*"
    ```

### [5.4. Embedding a container](#embedding-a-container) {#embedding-a-container .title}

You can customize your blueprint to embed the latest RHEL container. The containers list contains objects with a source, and optionally, the `tls-verify`{.literal} attribute.

The container list entries describe the container images to be embedded into the image.

-   `source`{.literal} - Mandatory field. Reference to the container image at a registry. This example uses the `registry.access.redhat.com`{.literal} registry. You can specify a tag version. The default tag version is the latest.
-   `name`{.literal} - The name of the container in the local registry.
-   `tls-verify`{.literal} - Boolean field. The tls-verify boolean field controls the Transport Layer Security. The default value is true.

The embedded containers do not start automatically. To start it, create `systemd`{.literal} unit files or `quadlets`{.literal} with the file customization.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   To embed a container from `registry.access.redhat.com/ubi10/ubi:latest`{.literal} and a container from your host, add the following customization to your blueprint:

    ``` {.language-plaintext tabindex="-1"}
    [[containers]]
    source = "registry.access.redhat.com/ubi10/ubi:latest"
    name = local_name
    tls-verify = true

    [[containers]]
    source = "localhost/test:latest"
    local-storage = true
    ```

    You can access protected container resources by using a `containers-auth.json`{.literal} file. See [Container registry credentials](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/working-with-container-registries#container-registries).

### [5.5. Setting the image hostname](#setting-the-image-hostname) {#setting-the-image-hostname .title}

The `customizations.hostname`{.literal} is an optional string that you can use to configure the final image hostname. This customization is optional, and if you do not set it, the blueprint uses the default hostname.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize the blueprint to configure the hostname:

    ``` {.language-plaintext tabindex="-1"}
    [customizations]
    hostname = "<base_image>"
    ```

### [5.6. Specifying additional users](#specifying-additional-users) {#specifying-additional-users .title}

Add a user to the image, and optionally, set their SSH key. All fields for this section are optional except for the `name`{.literal}.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize the blueprint to add a user to the image:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.user]]
    name = "<user_name>"
    description = "<user_description>"
    password = "<password_hash>"
    key = "<public_ssh_key>"
    home = "/home/<user_name>/"
    shell = "/usr/bin/bash"
    groups = ["users", "wheel"]
    uid = <uid_number>
    gid = <gid_number>
    ```

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.user]]
    name = "admin"
    description = "Administrator account"
    password = "$6$CHO2$3rN8eviE2t50lmVyBYihTgVRHcaecmeCk31L..."
    key = "PUBLIC SSH KEY"
    home = "/srv/widget/"
    shell = "/usr/bin/bash"
    groups = ["widget", "users", "wheel"]
    uid = 1200
    gid = 1200
    expiredate = 12345
    ```

    The GID is optional and must already exist in the image. Optionally, a package creates it, or the blueprint creates the GID by using the `[[customizations.group]]`{.literal} entry.

    Replace *`password_hash`{.literal}* with the actual `password hash`{.literal}. To generate the an encrypted password, use the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ mkpasswd -m sha-512
    ```

    Replace the other placeholders with suitable values.

    Enter the `name`{.literal} value and omit any lines you do not need.

    Repeat this block for every user to include.

### [5.7. Specifying additional groups](#specifying-additional-groups) {#specifying-additional-groups .title}

Specify a group for the resulting system image. Both the `name`{.literal} and the `gid`{.literal} attributes are mandatory.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize the blueprint with a group:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.group]]
    name = "<group_name>"
    gid = <number>
    ```

    Repeat this block for every group to include. For example:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.group]]
    name = "widget"
    gid = 1130
    ```

### [5.8. Setting SSH key for existing users](#setting-ssh-key-for-existing-users) {#setting-ssh-key-for-existing-users .title}

You can use `[[customizations.sshkey]]`{.literal} to set an SSH key for the existing users in the final image. Both `user`{.literal} and `key`{.literal} attributes are mandatory.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize the blueprint by setting an SSH key for existing users:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.sshkey]]
    user = "root"
    key = "PUBLIC-SSH-KEY"
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.sshkey]]
    user = "root"
    key = "SSH key for root"
    ```

### [5.9. Appending a kernel argument](#appending-a-kernel-argument) {#appending-a-kernel-argument .title}

You can append arguments to the boot loader kernel command line. By default, RHEL image builder builds a default kernel into the image. However, you can customize the kernel by configuring it in the blueprint.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Append a kernel boot parameter option to the defaults:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.kernel]
    append = "<kernel_option>"
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.kernel]
    name = "kernel-debug"
    append = "nosmt=force"
    ```

### [5.10. Building RHEL images by using the real-time kernel](#building-rhel-images-by-using-the-real-time-kernel) {#building-rhel-images-by-using-the-real-time-kernel .title}

Build a RHEL image by using the real-time kernel (`kernel-rt`{.literal}). Override a repository by using `.json`{.literal} from the `/usr/share/image-builder/repositories/`{.literal} directory to build an image that selects `kernel-rt`{.literal} as the default kernel. Deploy the image to a system and use the real-time kernel features.

Note

The real-time kernel runs on AMD64 and Intel 64 server platforms that are certified to run Red Hat Enterprise Linux.

**Prerequisites**

-   Your system is registered, and RHEL is attached to a RHEL for Real Time subscription.

**Procedure**

1.  Create a `kernel.json`{.literal} file to include the RT kernel repository:

    ``` {.language-plaintext tabindex="-1"}
        {
          "name": "kernel-rt",
          "baseurl": "https://cdn.redhat.com/content/dist/rhel10/10/x86_64/rt/os",
          "gpgkey": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n\nmQINBEr………fg==\n=UZd/\n-----END PGP PUBLIC KEY BLOCK-----\n",
          "rhsm": true,
          "check_gpg": true
        },
    ```

2.  Create a blueprint. In the blueprint, add the \"\[customizations.kernel\]\" customization. The following is an example that contains the \"\[customizations.kernel\]\" in the blueprint:

    ``` {.language-plaintext tabindex="-1"}
    name = "rt-kernel-image"
    description = ""
    version = "2.0.0"
    modules = []
    groups = []
    distro = "rhel-10.0"
    [[customizations.user]]
    name = "admin"
    password = "admin"
    groups = ["users", "wheel"]
    [customizations.kernel]
    name = "kernel-rt"
    append = ""
    ```

3.  Build your image from the blueprint you created. The following example builds a `.qcow2`{.literal} image:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder build qcow2 -- blueprint rt-kernel-image --data-dir kernel.json
    ```

4.  Deploy the image that you built to the system where you want to use the real-time kernel features.

**Verification**

-   After booting a VM from the image, verify that the image correctly selected `kernel-rt`{.literal} as the default kernel.

    ``` {.language-plaintext tabindex="-1"}
    $ cat /proc/cmdline
    BOOT_IMAGE=(hd0,got3)/vmlinuz-6.12.0-0.el10_0_.x86_64+rt...
    ```

### [5.11. Setting time zone and NTP](#setting-time-zone-and-ntp) {#setting-time-zone-and-ntp .title}

You can customize your blueprint to configure the time zone and the Network Time Protocol (NTP).

Both `timezone`{.literal} and `ntpservers`{.literal} attributes are optional strings. If you do not customize the time zone, the system uses Universal Time Coordinated (UTC). If you do not set NTP servers, the system uses the default distribution.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize the blueprint with the `timezone`{.literal} and the `ntpservers`{.literal} you want:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.timezone]
    timezone = "TIMEZONE"
    ntpservers = "NTP_SERVER"
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.timezone]
    timezone = "US/Eastern"
    ntpservers = ["0.north-america.pool.ntp.org", "1.north-america.pool.ntp.org"]
    ```

    Note

    Some image types, such as Google Cloud, already have NTP servers configured. You cannot override it because the image requires the NTP servers to boot in the selected environment. However, you can customize the time zone in the blueprint.

### [5.12. Customizing the locale settings](#customizing-the-locale-settings) {#customizing-the-locale-settings .title}

You can customize the locale settings for your resulting system image. Both `language`{.literal} and `keyboard`{.literal} attributes are mandatory. The first language you add is the primary language, and the remaining languages are secondary.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Set the locale settings:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.locale]
    languages = ["<language>"]
    keyboard = "<keyboard>"
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.locale]
    languages = ["en_US.UTF-8"]
    keyboard = "us"
    ```

-   List the values supported by the languages:

    ``` {.language-plaintext tabindex="-1"}
    $ localectl list-locales
    ```

-   List the values supported by the keyboard:

    ``` {.language-plaintext tabindex="-1"}
    $ localectl list-keymaps
    ```

### [5.13. Customizing firewall](#customizing-firewall) {#customizing-firewall .title}

Set the firewall for the resulting system image. By default, the firewall blocks incoming connections, except for services that you explicitly enabled ports, such as `sshd`{.literal}.

If you do not want to use the `[customizations.firewall]`{.literal} or `[customizations.firewall.services]`{.literal}, either remove the attributes or set them to an empty list `[]`{.literal}. If you only want to use the default firewall setup, you can omit the customization from the blueprint.

Note

The Google template explicitly disables the firewall for their environment. You cannot override this behavior by setting the blueprint.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize the blueprint with the following settings to open other ports and services:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.firewall]
    ports = ["<ports>"]
    ```

    Where `ports`{.literal} is an optional list of strings that contain ports or a range of ports and protocols to open. You can configure the ports by using the `port:protocol`{.literal} format, or you can configure the port ranges by using the `portA-portB:protocol`{.literal} format. For example:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.firewall]
    ports = ["22:tcp", "80:tcp", "imap:tcp", "53:tcp", "53:udp", "30000-32767:tcp", "30000-32767:udp"]
    ```

    You can use numeric ports or their names from the `/etc/services`{.literal} to enable or disable port lists.

-   Specify which firewall services to enable or disable in the `customizations.firewall.service`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.firewall.services]
    enabled = ["<services>"]
    disabled = ["<services>"]
    ```

-   You can check the available firewall services:

    ``` {.language-plaintext tabindex="-1"}
    $ firewall-cmd --get-services
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.firewall.services]
    enabled = ["ftp", "ntp", "dhcp"]
    disabled = ["telnet"]
    ```

    Note

    The services listed in `firewall.services`{.literal} are different from the `service-names`{.literal} available in the `/etc/services`{.literal} file.

### [5.14. Enabling or disabling services](#enabling-or-disabling-services) {#enabling-or-disabling-services .title}

You can control which services to enable during boot time. Some image types have preset services that you cannot override to ensure the image works correctly.

The `[customizations.services]`{.literal} settings add to existing services in image templates but do not replace them.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize which services to enable during boot time:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.services]
    enabled = ["services"]
    disabled = ["services"]
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.services]
    enabled = ["sshd", "cockpit.socket", "httpd"]
    disabled = ["postfix", "telnetd"]
    ```

### [5.15. Kickstart file injection in an ISO image](#injecting-a-kickstart-file-in-an-iso-image) {#kickstart-file-injection-in-an-iso-image .title}

You can use the `[customizations.installer]`{.literal} customization to add your Kickstart file to ISO installers builds, such as `image installer`{.literal}, for bare metal deployments.

Warning

Booting the ISO on a machine with an existing operating system or data can be destructive, because it configures the Kickstart to automatically reformat the first disk on the system.

You can choose the following options to add your own Kickstart file:

-   Setting all values during the installation process.

-   Enabling the `unattended = true`{.literal} field in the Kickstart, and getting a fully unattended installation with defaults.

-   Injecting your own Kickstart by using the Kickstart field. This results in a fully unattended installation if you specify all required fields. Otherwise, the installation program prompts you for missing fields.

    The Anaconda installer ISO image types support the following blueprint customization:

    ``` {.language-plaintext tabindex="-1"}
    [customizations.installer]
    unattended = true
    sudo-nopasswd = ["user", "%wheel"]
    ```

    `unattended`{.literal}: Creates a Kickstart file that fully automates the installation. This includes setting the following options by default:

-   text display mode

-   `en_US.UTF-8`{.literal} language and locale

-   `us keyboard`{.literal} layout

-   `UTC time zone`{.literal}

-   `zerombr`{.literal}, `clearpart`{.literal}, and `autopart`{.literal} to automatically wipe and partition the first disk

-   network options to enable `dhcp`{.literal} and `auto-activation`{.literal}

The following is an example:

``` {.language-plaintext tabindex="-1"}
liveimg --url file:///run/install/repo/liveimg.tar.gz
lang en_US.UTF-8
keyboard us
timezone UTC
zerombr
clearpart --all --initlabel
text
autopart --type=plain --fstype=xfs --nohome
reboot --eject
network --device=link --bootproto=dhcp --onboot=on --activate
```

`sudo-nopasswd`{.literal}: Use to add a Kickstart snippet configured to create `/etc/sudoers.d`{.literal} drop-in files, enabling specified users and `%`{.literal} prefixed groups to run sudo without a password.

For example, setting the value to `["user", "%wheel"]`{.literal} creates the following Kickstart `%post`{.literal} section:

``` {.language-plaintext tabindex="-1"}
%post
echo -e "user\tALL=(ALL)\tNOPASSWD: ALL" > "/etc/sudoers.d/user"
chmod 0440 /etc/sudoers.d/user
echo -e "%wheel\tALL=(ALL)\tNOPASSWD: ALL" > "/etc/sudoers.d/%wheel"
chmod 0440 /etc/sudoers.d/%wheel
restorecon -rvF /etc/sudoers.d
%end
```

As an alternative, you can include a custom Kickstart by using the following customization:

``` {.language-plaintext tabindex="-1"}
[customizations.installer.kickstart]
contents = """
text --non-interactive
zerombr
clearpart --all --initlabel --disklabel=gpt
autopart --noswap --type=lvm
network --bootproto=dhcp --device=link --activate --onboot=on
"""
```

`image-builder`{.literal} automatically adds the command that installs the system: `liveimg`{.literal}, if it is relevant for the `image-installer`{.literal} image type. You cannot use the `[customizations.installer.kickstart]`{.literal} customization in combination with any other installer customizations.

### [5.16. Specifying a partition mode](#specifying-a-partition-mode) {#specifying-a-partition-mode .title}

Use the `partitioning_mode`{.literal} variable to select how to partition the disk image that you are building.

You can customize your image with the following supported modes:

-   `auto-lvm`{.literal}: It uses the raw partition mode, unless there is one or more filesystem customizations. In that case, it uses the LVM partition mode.
-   `lvm`{.literal}: It always uses the LVM partition mode, even when there is no extra mount points.
-   `raw`{.literal}: It uses raw partitions even when there are one or more mount points.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   You can customize your blueprint with the `partitioning_mode`{.literal} variable by using the following customization:

    ``` {.language-plaintext tabindex="-1"}
    [customizations]
    partitioning_mode = "lvm"
    ```

### [5.17. Custom file system configuration specification](#specifying-a-custom-filesystem-configuration) {#custom-file-system-configuration-specification .title}

You can specify a custom filesystem configuration in your blueprints and therefore create images with a specific disk layout, instead of the default layout configuration.

By using the non-default layout configuration in your blueprints, you can benefit from:

-   Security benchmark compliance
-   Protection against out-of-disk errors
-   Improved performance
-   Consistency with existing setups

Note

The OSTree systems do not support filesystem customizations, because OSTree images have their own mount rule, such as read-only. The following image types are not supported:

-   `image-installer`{.literal}

Additionally, the following image types do not support filesystem customizations, because these image types do not create partitioned operating system images:

-   `tar`{.literal}
-   `container`{.literal}

For release distributions before 9.4, the blueprint supports the following `mountpoints`{.literal} and their sub-directories:

-   `/`{.literal} is the root mount point
-   `/var`{.literal}
-   `/home`{.literal}
-   `/opt`{.literal}
-   `/srv`{.literal}
-   `/usr`{.literal}
-   `/app`{.literal}
-   `/data`{.literal}
-   `/tmp`{.literal}

You cannot specify arbitrary custom mount points on the following mount points and their sub-directories:

-   `/bin`{.literal}
-   `/boot/efi`{.literal}
-   `/dev`{.literal}
-   `/etc`{.literal}
-   `/lib`{.literal}
-   `/lib64`{.literal}
-   `/lost+found`{.literal}
-   `/proc`{.literal}
-   `/run`{.literal}
-   `/sbin`{.literal}
-   `/sys`{.literal}
-   `/sysroot`{.literal}
-   `/var/lock`{.literal}
-   `/var/run`{.literal}

You can customize the filesystem in the blueprint for the `/usr`{.literal} custom mount point, but its subdirectory is not allowed.

If you have more than one partition in the customized image, you can create images with a customized file system partition on LVM and resize those partitions at runtime. To do this, you can specify a customized filesystem configuration in your blueprint and therefore create images with the required disk layout. The default filesystem layout remains unchanged if you use plain images without file system customization, and `cloud-init`{.literal} resizes the root partition.

The blueprint automatically converts the file system customization to an LVM partition.

You can use the custom file blueprint customization to create new files or to replace existing files. The parent directory of the file you specify must exist otherwise, the image build fails. Specify the parent directory in the `[[customizations.directories]]`{.literal} customization to ensure that it exists.

Warning

Combining file customizations with other blueprint customizations might affect their functioning or override the file customizations.

#### [5.17.1. Custom files specification in the blueprint](#custom_files_specification_in_the_blueprint) {#custom-files-specification-in-the-blueprint .title}

With the `[[customizations.files]]`{.literal} blueprint customization you can create new text files, or modify existing files. This can override the existing content.

-   Set user and group ownership for the file you are creating.
-   Set the mode permission in the octal format.

You cannot create or replace the following files:

-   `/etc/fstab`{.literal}
-   `/etc/shadow`{.literal}
-   `/etc/passwd`{.literal}
-   `/etc/group`{.literal}

You can create customized files and directories in your image by using the `[[customizations.files]]`{.literal} and the `[[customizations.directories]]`{.literal} blueprint customizations. You can use these customizations only in the `/etc`{.literal} directory.

Warning

If you use the `customizations.directories`{.literal} with a directory path that already exists in the image with `mode`{.literal}, `user`{.literal}, or `group`{.literal} already set, the image build fails to prevent changing the ownership or permissions of the existing directory.

#### [5.17.2. Custom directories specification in the blueprint](#custom_directories_specification_in_the_blueprint) {#custom-directories-specification-in-the-blueprint .title}

You can use the `[[customizations.directories]]`{.literal} blueprint customization to create or modify directories.

With the customization, you can:

-   Create new directories.
-   Set user and group ownership for the directory you are creating.
-   Set the directory mode permission in the octal format.
-   Ensure that parent directories are created as needed.

With the `[[customizations.files]]`{.literal} blueprint customization you can:

-   Create new text files.
-   Modify existing files. This can override the existing content.
-   Set user and group ownership for the file you are creating.
-   Set the mode permission in the octal format.

Note

You cannot create or replace the following files:

-   `/etc/fstab`{.literal}
-   `/etc/shadow`{.literal}
-   `/etc/passwd`{.literal}
-   `/etc/group`{.literal}

The following customizations are available:

-   Customize the filesystem configuration in your blueprint:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.filesystem]]
    mountpoint = "MOUNTPOINT"
    minsize = MINIMUM-PARTITION-SIZE
    ```

    The `MINIMUM-PARTITION-SIZE`{.literal} value has no default size format. The blueprint customization supports the following values and units: kB to TB and KiB to TiB. For example, you can define the mount point size in bytes:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.filesystem]]
    mountpoint = "/var"
    minsize = 1073741824
    ```

-   Define the mount point size by using units. For example:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.filesystem]]
    mountpoint = "/opt"
    minsize = "20 GiB"
    ```

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.filesystem]]
    mountpoint = "/var"
    minsize = "1 GiB"
    ```

-   Define the minimum partition by setting `minsize`{.literal}. For example:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.filesystem]]
    mountpoint = "/var"
    minsize = 2147483648
    ```

-   Create customized directories under the `/etc`{.literal} directory for your image by using `[[customizations.directories]]`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.directories]]
    path = "/etc/directory_name"
    mode = "octal_access_permission"
    user = "user_string_or_integer"
    group = "group_string_or_integer"
    ensure_parents = boolean
    ```

    The blueprint entries are described as follows:

    -   `path`{.literal} Mandatory. Enter the path to the directory that you want to create. It must be an absolute path under the `/etc`{.literal} directory.
    -   `mode`{.literal} Optional. Set the access permission on the directory, in the octal format. If you do not specify a permission, it defaults to `0755`{.literal}. The leading zero is optional.
    -   `user`{.literal} Optional. Set a user as the owner of the directory. If you do not specify a user, it defaults to `root`{.literal}. You can specify the user as a string or as an integer.
    -   `group`{.literal} Optional. Set a group as the owner of the directory. If you do not specify a group, it defaults to `root`{.literal}. You can specify the group as a string or as an integer.
    -   `ensure_parents`{.literal} Optional. Specify whether you want to create parent directories as needed. If you do not specify a value, it defaults to `false`{.literal}.

-   Create a customized file under the `/etc`{.literal} directory for your image by using `[[customizations.directories]]`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.files]]
    path = "/etc/directory_name"
    mode = "octal_access_permission"
    user = "user_string_or_integer"
    group = "group_string_or_integer"
    data = "Hello world!"
    ```

    The blueprint entries are described as follows:

    -   `path`{.literal} Mandatory. Enter the path to the file that you want to create. It must be an absolute path under the `/etc`{.literal} directory.
    -   `mode`{.literal} Optional. Set the access permission on the file in the octal format. If you do not specify a permission, it defaults to `0644`{.literal}. The leading zero is optional.
    -   `user`{.literal} Optional. Set a user as the owner of the file. If you do not specify a user, it defaults to `root`{.literal}. You can specify the user as a string or as an integer.
    -   `group`{.literal} Optional. Set a group as the owner of the file. If you do not specify a group, it defaults to `root`{.literal}. You can specify the group as a string or as an integer.
    -   `data`{.literal} Optional. Specify the content of a plain text file. If you do not specify any content, it creates an empty file.

### [5.18. Volume groups and logical volumes naming specification in the blueprint](#specify-volume-groups-and-logical-volumes-naming-in-the-blueprint) {#volume-groups-and-logical-volumes-naming-specification-in-the-blueprint .title}

You can specify the names of volume groups and logical volumes in the blueprint.

You can use RHEL image builder for the following operations:

-   Create RHEL disk images with an advanced partitioning layout. You can create disk images with custom mount points, LVM-based partitions, and LVM-based SWAP. For example, change the size of the `/`{.literal} and the `/boot`{.literal} directories by using the `config.toml`{.literal} file.
-   Select which file system to use. You can choose between `ext4`{.literal} and `xfs`{.literal}.
-   Add swap partitions and LVs. The disk images can contain LV-based SWAP.
-   Change the names of LVM entities. The Logical Volumes (LV) and Volume Groups (VG) inside the images can have custom names.

The following options are not supported:

-   Multiple PVs or VGs in one image.
-   SWAP files
-   Mount options for non-physical partitions, such as `/dev/shm`{.literal}, and `/tmp`{.literal}.

You can add custom names for VG and LG where the file systems reside, for example:

``` {.language-plaintext tabindex="-1"}
[[customizations.disk.partitions]]
type = "plain"
label = "data"
mountpoint = "/data"
fs_type = "ext4"
minsize = "50 GiB"

[[customizations.disk.partitions]]
type = "lvm"
name = "mainvg"
minsize = "20 GiB"

[[customizations.disk.partitions.logical_volumes]]
name = "rootlv"
mountpoint = "/"
label = "root"
fs_type = "ext4"
minsize = "2 GiB"

[[customizations.disk.partitions.logical_volumes]]
name = "homelv"
mountpoint = "/home"
label = "home"
fs_type = "ext4"
minsize = "2 GiB"

[[customizations.disk.partitions.logical_volumes]]
name = "swaplv"
fs_type = "swap"
minsize = "1 GiB"
```

## [Chapter 6. Creating system images by using RHEL image builder web console interface](#creating-system-images-with-gui) {#chapter-6.-creating-system-images-by-using-rhel-image-builder-web-console-interface .title}

RHEL image builder is a tool for creating custom system images. To control RHEL image builder and create your custom system images, you can use the web console interface.

### [6.1. Accessing the RHEL image builder dashboard in the RHEL web console](#accessing-the-rhel-image-builder-dashboard-in-the-rhel-web-console) {#accessing-the-rhel-image-builder-dashboard-in-the-rhel-web-console .title}

With the **cockpit-image-builder** plugin for the RHEL web console, you can manage image builder blueprints and composes by using a graphical interface.

**Prerequisites**

-   You must have root access to the system.
-   You installed RHEL image builder.
-   You installed the `cockpit-image-builder`{.literal} package.

**Procedure**

1.  On the host, open `https://localhost:9090/`{.literal} in a web browser.

2.  Log in to the web console as the root user.

3.  To display the RHEL image builder controls, click the **Image Builder** button, in the upper-left corner of the window.

    The RHEL image builder dashboard opens, listing existing blueprints, if any.

**Additional resources**

-   [Managing systems using the RHEL web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/index)

### [6.2. Creating a blueprint in the web console interface](#creating-a-blueprint-in-the-web-console-interface) {#creating-a-blueprint-in-the-web-console-interface .title}

Before creating your customized RHEL system image, you must create a blueprint. All customizations are optional.

**Prerequisites**

-   You opened the RHEL image builder application from the web console in a browser. See [Accessing RHEL image builder GUI in the RHEL web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-gui).

**Procedure**

1.  On the RHEL image builder dashboard, click **Create image blueprint**.

    a.  On the `Image output`{.literal} page, select from the following options then click **Next**.:

        -   `Release`{.literal} version
        -   `Architecture`{.literal}
        -   `Select target environment`{.literal}

2.  Optional: On the `OpenSCAP profile`{.literal} page, select the command to install missing OpenSCAP security profile packages.

    After finishing the installation, refresh the page to check the **Enable FIPS mode**. Click **Next**.

3.  Optional: On the `File system configuration`{.literal} page, select `Manually configure partitions`{.literal} to add mount points, such as `/var`{.literal}, `/home`{.literal}, and `/tmp`{.literal}, and specify `Minimum size partition`{.literal}. Click **Next**.

4.  Fill the fields on the following optional pages, and click **Next**. to move to the next page.

5.  On the `Review`{.literal} page, review the details and click **Create blueprint** or **Create blueprint and build image(s)**.

### [6.3. Importing a blueprint in the RHEL image builder web console interface](#importing-a-blueprint-in-the-rhel-image-builder-web-console-interface) {#importing-a-blueprint-in-the-rhel-image-builder-web-console-interface .title}

You can import and use an already existing blueprint. The system automatically resolves all the dependencies.

**Prerequisites**

-   You have opened the RHEL image builder app from the web console in a browser.
-   You have a blueprint that you want to import to use in the RHEL image builder web console interface.

**Procedure**

1.  On the RHEL image builder dashboard, click Import blueprint. The `Import blueprint`{.literal} wizard opens.
2.  From the `Upload`{.literal} field, either drag or upload an existing blueprint. This blueprint can be in either `TOML`{.literal} or `JSON`{.literal} format.
3.  Click Import. The dashboard lists the blueprint you imported.

**Verification**

When you click the blueprint you imported, you have access to a dashboard with all the customizations for the blueprint that you imported.

-   To verify the packages that have been selected for the imported blueprint, navigate to the `Packages`{.literal} tab.

    -   To list all the package dependencies, click All. The list is searchable and can be ordered.

**Next steps**

-   Optional: To modify any customization:

    -   From the `Customizations`{.literal} dashboard, click the customization you want to make a change to. Optionally, you can click Edit blueprint to navigate to all the available customization options.

**Additional resources**

-   [Creating a system image by using RHEL image builder in the web console interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-gui)

### [6.4. Exporting a blueprint from the RHEL image builder web console interface](#exporting-a-blueprint-from-the-rhel-image-builder-web-console-interface) {#exporting-a-blueprint-from-the-rhel-image-builder-web-console-interface .title}

You can export a blueprint to use the customizations in another system. You can export the blueprint in the `TOML`{.literal} or in `JSON`{.literal} format. Both formats work on the CLI and also in the API interface.

**Prerequisites**

-   You have opened the RHEL image builder app from the web console in a browser.
-   You have a blueprint that you want to export.

**Procedure**

1.  On the image builder dashboard, select the blueprint you want to export.

2.  Click `Export blueprint`{.literal}. The `Export blueprint`{.literal} wizard opens.

3.  Click the Export button to download the blueprint as a file or click the Copy button to copy the blueprint to the clipboard.

    a.  Optional: Click the Copy button to copy the blueprint.

**Verification**

-   Open the exported blueprint in a text editor to inspect and review it.

### [6.5. Creating a system image by using RHEL image builder in the web console interface](#creating-a-system-image-by-using-rhel-image-builder-in-the-web-console-interface) {#creating-a-system-image-by-using-rhel-image-builder-in-the-web-console-interface .title}

You can create a customized RHEL system image from a customized blueprint by completing these steps.

**Prerequisites**

-   You opened the RHEL image builder app from the web console in a browser.
-   You created a blueprint.

**Procedure**

1.  In the RHEL image builder dashboard, click the blueprint tab.

2.  On the blueprint table, find the blueprint you want to build an image.

3.  On the right side of the chosen blueprint, click **Create Image**. The **Create image** dialog wizard opens.

4.  On the **Image output** page, complete the following steps:

    a.  From the **Select a blueprint** list, select the image type you want.

    b.  From the **Image output type** list, select the image output type you want.

        Depending on the image type you select, you need to add further details.

5.  Click **Next**.

6.  On the **Review** page, review the details about the image creation and click **Create image**.

    The image build starts and takes up to 20 minutes to complete.

**Verification**

After the image finishes building, you can:

-   Download the image.

    -   On the RHEL image builder dashboard, click the `Node options (⫶)`{.literal} menu and select **Download image**.

-   Download the logs of the image to inspect the elements and verify if any issue is found.

    -   On the RHEL image builder dashboard, click the `Node options (⫶)`{.literal} menu and select **Download logs**.

## [Chapter 7. Creating a boot ISO installer image with RHEL image builder](#creating-iso-images-with-image-builder) {#chapter-7.-creating-a-boot-iso-installer-image-with-rhel-image-builder .title}

You can use RHEL image builder to create bootable ISO Installer images. These images consist of a `.tar`{.literal} file that has a root file system. You can use the bootable ISO image to install the file system to a bare-metal server.

RHEL image builder builds a manifest that creates a boot ISO that contains a root file system. To create the ISO image, select the image type **image-installer**. RHEL image builder builds a `.tar`{.literal} file with the following content:

-   A standard Anaconda installer ISO
-   An embedded RHEL system tar file
-   A default Kickstart file that installs the commit with minimal default requirements

The created installer ISO image includes a pre-configured system image that you can install directly to a bare-metal server.

### [7.1. Creating a boot ISO installer image using the RHEL image builder CLI](#creating-a-boot-iso-installer-image-using-the-rhel-image-builder-cli) {#creating-a-boot-iso-installer-image-using-the-rhel-image-builder-cli .title}

You can create a customized boot ISO installer image by using the RHEL image builder command-line interface. The resulting image is an `.iso`{.literal} file that contains a `.tar`{.literal} file, which you can install on your operating system.

The `.iso`{.literal} file is configured to boot Anaconda and install the `.tar`{.literal} file for configuring the system. You can use the created ISO image file on a hard disk or to boot in a virtual machine, such as an HTTP Boot or a USB installation.

Warning

The installation (`.iso`{.literal}) image type does not accept partition customization. If you try to manually configure the filesystem customization, it is not applied to any system built by the (`.iso`{.literal}) image. ISO image built with file system customizations might cause Kickstart errors, and the installation does not reboot automatically. For more information, see [Automate a RHEL ISO installation generated by image builder](https://access.redhat.com/solutions/6977658).

**Prerequisites**

-   You have created a blueprint for the image and customized it with a user included and pushed it back into RHEL image builder. See [Supported image customizations](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/supported-image-customizations).

**Procedure**

1.  Create the ISO image:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder build iso --blueprint <blueprint_name>
    ```

    -   *`<blueprint_name>`{.literal}* with the name of the blueprint you created

    -   *`<image_installer>`{.literal}* is the image type

        The compose process starts and might take some minutes complete.

        RHEL image builder builds an `.iso`{.literal} file that contains a `.tar`{.literal} file. The `.tar`{.literal} file is the image that is installed for the operating system. The `.iso`{.literal} is configured to boot Anaconda and install the `.tar`{.literal} file to configure the system.

**Next steps**

j In the directory where you downloaded the image file.

1.  Locate the `.iso`{.literal} image that you built.

2.  Mount the ISO image.

    ``` {.language-plaintext tabindex="-1"}
    $ mount -o ro <path_to_iso> /mnt
    ```

    You can find the `.tar`{.literal} file at the `/mnt/liveimg.tar.gz`{.literal} directory.

3.  List the `.tar`{.literal} file content:

    ``` {.language-plaintext tabindex="-1"}
    $ tar ztvf /mnt/liveimg.tar.gz
    ```

**Additional resources**

-   [Creating system images with RHEL image builder command-line interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-cli)
-   [Creating a bootable installation medium for RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/creating-a-bootable-installation-medium-for-rhel)

### [7.2. Creating a boot ISO installer image by using RHEL image builder in the GUI](#creating-a-boot-iso-installer-image-by-using-rhel-image-builder-in-the-gui) {#creating-a-boot-iso-installer-image-by-using-rhel-image-builder-in-the-gui .title}

You can build a customized boot ISO installer image by using the RHEL image builder GUI. You can use the resulting ISO image file on a hard disk or boot it in a virtual machine. For example, in an Hypertext Transfer Protocol (HTTP) Boot or a Universal Serial Bus (USB) installation.

Warning

The installation (`.iso`{.literal}) image type does not accept partitions customization. If you try to manually configure the filesystem customization, it is not applied to any system built by the installation image. Mounting an ISO image built with RHEL image builder file system customizations causes an error in the Kickstart, and the installation does not reboot automatically. For more information, see [Automate a RHEL ISO installation generated by image builder](https://access.redhat.com/solutions/6977658).

**Prerequisites**

-   You have opened the RHEL image builder app from the web console in a browser.
-   You have created a blueprint for your image. See [Creating a RHEL image builder blueprint in the web console interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-gui).

**Procedure**

1.  On the RHEL image builder dashboard, locate the blueprint that you want to use to build your image. Optionally, enter the blueprint name or a part of it into the search box at the upper left, and click **Enter**.

2.  On the right side of the blueprint, click the corresponding Create Image button.

    The **Create image** dialog wizard opens.

3.  On the **Create image** dialog wizard:

    a.  In the **Image Type** list, select `"RHEL Installer (.iso)"`{.literal}.

    b.  Click Next.

    c.  On the **Review** tab, click **Create**.

        After the build process is complete, you can see the image build complete status.

**Verification**

After the image is successfully created, you can download it.

1.  Click **Download** to save the `"RHEL Installer (.iso)"`{.literal} image to your system.

2.  Navigate to the folder where you downloaded the `"RHEL Installer (.iso)"`{.literal} image.

3.  Locate the `.tar`{.literal} image you downloaded.

4.  Extract the `"RHEL Installer (.iso)"`{.literal} image content.

    ``` {.language-plaintext tabindex="-1"}
    $ tar -xf <content>.tar
    ```

**Additional resources**

-   [Creating a bootable installation medium for RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/creating-a-bootable-installation-medium-for-rhel)

### [7.3. Installing a bootable ISO to a medium and booting it](#installing-a-bootable-iso-to-a-media-and-booting-it) {#installing-a-bootable-iso-to-a-medium-and-booting-it .title}

Install the bootable ISO image you created by using RHEL image builder on a bare metal system.

**Prerequisites**

-   You created the bootable ISO image by using RHEL image builder.
-   You have downloaded the bootable ISO image.
-   You installed the `dd`{.literal} tool.
-   You have a USB flash drive with enough capacity for the ISO image. The required size varies depending on the packages you selected in your blueprint, but the minimum size is 8 GB.

**Procedure**

1.  Write the bootable ISO image directly to the USB drive using the `dd`{.literal} tool. For example:

    ``` {.language-plaintext tabindex="-1"}
    dd if=installer.iso of=/dev/sdX
    ```

    Where `installer.iso`{.literal} is the ISO image file name and `/dev/sdX`{.literal} is your USB flash drive device path.

2.  Insert the flash drive into a USB port of the computer you want to boot.

3.  Boot the ISO image from the USB flash drive.

    When the installation environment starts, you might need to complete the installation manually, similarly to the default Red Hat Enterprise Linux installation.

**Additional resources**

-   [Booting the installation media](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/booting-the-installation-media-)
-   [Customizing your installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/customizing-the-system-in-the-installer)
-   [Creating a bootable USB device on Linux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/creating-a-bootable-installation-medium-for-rhel#creating-a-bootable-usb-device-on-linux)

## [Chapter 8. Creating a network installer image by using RHEL image builder](#creating-a-network-installer-image-by-using-rhel-image-builder) {#chapter-8.-creating-a-network-installer-image-by-using-rhel-image-builder .title}

Automate registration and deployment by using RHEL image builder to create Anaconda network installer ISO images. By embedding activation keys, you can generate pre-configured, self-registering images tailored for nightly builds and specific environments.

### [8.1. Benefits of the network installer image](#benefits-of-the-network-installer-image) {#benefits-of-the-network-installer-image .title}

When deploying new systems across an organization, you can generate custom network installer images with embedded configurations to ensure automatic compliance, security, and consistent registration from day one.

Automated registration
:   By injecting activation keys into the blueprint, the resulting image ensures the system is automatically registered and attached to subscriptions during installation.

Minimized footprint
:   The `image-builder`{.literal} tool removes unnecessary files from the Anaconda file system, resulting in a lightweight, optimized boot image.

Security
:   Generating images based on the latest nightly builds ensures that the images contain no Common Vulnerabilities and Exposures (CVEs) from day one.

Customization
:   Unlike static images from the Red Hat Customer Portal, these images are tailored to your specific organizational requirements and repositories.

### [8.2. Overview of ISO image types in RHEL image builder](#overview-of-iso-image-types-in-rhel-image-builder) {#overview-of-iso-image-types-in-rhel-image-builder .title}

To evaluate the differences between the available ISO image types, review the following table to select the optimal installation method for your network bandwidth and customization needs.

+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Image type                                        | Description                                                                                                                        | Use case                                                                                                         |
+:==================================================+:===================================================================================================================================+:=================================================================================================================+
| Image Installer (`image-installer`{.literal})     | A bootable ISO file that contains a predefined system image. It installs a specific payload directly to the disk.                  | Fast, repeatable deployments of a base image with minimal configuration during installation.                     |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Network Installer (`network-installer`{.literal}) | A lightweight bootable ISO file that contains the Anaconda installer but downloads packages from a repository during installation. | Highly customized installations where you must select packages or use activation keys at the time of deployment. |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

Show more

### [8.3. Creating a network installer image by using the image-builder cli](#creating-a-network-installer-image-by-using-the-cli) {#creating-a-network-installer-image-by-using-the-image-builder-cli .title}

Build a customized Anaconda network installer image by using the `image-builder`{.literal} CLI to generate lightweight, repeatable boot images directly from the command line.

**Prerequisites**

-   You have installed the `image-builder`{.literal} package.
-   The host system has a valid Red Hat subscription.
-   Optional: You have an activation key to enable automated registration during the installation process.

**Procedure**

1.  Create a blueprint file in the TOML (Tom's Obvious, Minimal Language) format, and define the blueprint name, description, and any required customizations:

    ``` {.language-plaintext tabindex="-1"}
    name = "network-installer-example"
    description = "A customized RHEL 10 network installer"
    version = "0.0.1"
    ```

2.  Save the file, for example, as *`<blueprint_name>`{.literal}*`.toml`{.literal}, and close the text editor.

3.  Start the image build process, specifying `network-installer`{.literal} as the image type:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder build --distro rhel-10.2 network-installer --blueprint network-installer-example
    ```

    The compose process takes some minutes to complete. After the image-building process finishes, the image is available for your use in the directory where you created it.

### [8.4. Creating a network installer image by using the web console](#creating-a-network-installer-image-by-using-the-web-console) {#creating-a-network-installer-image-by-using-the-web-console .title}

When managing operating system deployments through a graphical interface, you can build a customized Anaconda network installer image by using the RHEL web console to provision lightweight, subscription-ready systems across your environment.

**Prerequisites**

-   You have a RHEL system with the web console installed and enabled. For more information, see [Installing RHEL image builder](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/installing-rhel-image-builder#installing-image-builder).
-   You have active Red Hat subscription credentials or an activation key and organization ID.
-   The Red Hat Enterprise Linux host is subscribed to Red Hat Subscription Manager (RHSM) or Red Hat Satellite.

**Procedure**

1.  On the host, log in to the RHEL web console.

    ``` {.language-plaintext tabindex="-1"}
    https://localhost:9090
    ```

2.  Log in to the web console as the `root`{.literal} user, and in the navigation menu, select **Image builder**.

3.  Click **Create blueprint**.

4.  On the **Image output** page, perform the following actions:

    a.  Select the architecture.
    b.  Select the `network-installer`{.literal} image type.
    c.  Click **Next**.

5.  Optional: On the **Details** page, enter a name for the blueprint. The default naming is a timestamp of the blueprint creation. Click **Next**.

6.  On the **Review** page, review the details and click **Create blueprint and build image**.

    The image generation process starts. When the image creation finishes, you can interact with the image in the following ways:

    -   Create a VM.
    -   Download the image file to your local machine or deploy it directly to your target environment.
    -   Check the image artifact files in the web console browser.

**Verification**

1.  Click **Create VM**.

    You are redirected to the **Create new virtual machine** wizard with prepopulated details for the VM creation.

2.  Click **Create and run**.

    The web console starts a VM with the bootable image that you created.

3.  Log in to the VM with the credentials that you created in the blueprint.

4.  Verify the `bootc`{.literal} status on the booted system:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo bootc status
    ```

## [Chapter 9. Creating pre-hardened images with RHEL image builder OpenSCAP integration](#creating-pre-hardened-images-with-image-builder) {#chapter-9.-creating-pre-hardened-images-with-rhel-image-builder-openscap-integration .title}

RHEL image builder on-premise supports the OpenSCAP integration. This integration enables the production of pre-hardened RHEL images.

By configuring a blueprint, you can perform the following actions:

-   Customize it with a set of predefined security profiles
-   Add a set of packages or add-on files
-   Build a customized RHEL image ready to deploy on your chosen platform that is more suitable for your environment

Red Hat provides regularly updated versions of the security hardening profiles that you can choose when you build your systems so that you can meet your current deployment guidelines.

### [9.1. The OpenSCAP blueprint customization](#the-openscap-blueprint-customization) {#the-openscap-blueprint-customization .title}

By using the OpenSCAP blueprint customization, you can generate blueprints from the `scap-security-guide`{.literal} for specific security profiles and build pre-hardened images.

Creating a customized blueprint with OpenSCAP involves the following high-level steps:

-   Modify the mount points and configure the file system layout according to your specific requirements.
-   In the blueprint, select the OpenSCAP profile. This configures the image to trigger the remediation during the image build in accordance with the selected profile. Also, during the image build, OpenSCAP applies a `pre-first-boot`{.literal} remediation.

To use the `OpenSCAP`{.literal} blueprint customization in your image blueprints, you need to provide the following information:

-   The data stream path to the `datastream`{.literal} remediation instructions. The data stream files from `scap-security-guide`{.literal} package are located in the `/usr/share/xml/scap/ssg/content/`{.literal} directory.
-   The `profile_id`{.literal} of the required security profile. The `profile_id`{.literal} field accepts both long and short forms, such as `cis`{.literal} or `xccdf_org.ssgproject.content_profile_cis`{.literal}. See [SCAP Security Guide profiles supported in RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#scap-security-guide-profiles-supported-in-rhel-10) for more details.

The following example is a snippet with the `OpenSCAP`{.literal} remediation stage:

``` {.language-plaintext tabindex="-1"}
[customizations.openscap]
# If you want to use the data stream from the 'scap-security-guide' package
# the 'datastream' key could be omitted.
# datastream = "/usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml"
profile_id = "xccdf_org.ssgproject.content_profile_cis"
```

You can find more details about the `SCAP`{.literal} source data stream from the `scap-security-guide`{.literal} package, including the list of security profiles it provides, by using the command:

``` {.language-plaintext tabindex="-1"}
# oscap info /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
```

For your convenience, the `OpenSCAP`{.literal} tool can generate the hardening blueprint for any profile available in `scap-security-guide`{.literal} data streams.

For example, the command:

``` {.language-plaintext tabindex="-1"}
# oscap xccdf generate fix --profile=cis --fix-type=blueprint /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
```

generates a blueprint for CIS profile similar to the following example:

``` {.language-plaintext tabindex="-1"}
# Blueprint for CIS Red Hat Enterprise Linux 10.0 Benchmark for Level 2 - Server

# Profile Description:
# This profile defines a baseline that aligns to the "Level 2 - Server"
# configuration from the Center for Internet Security® Red Hat Enterprise
# Linux 10 Benchmark™, v3.0.0, released 2023-10-30.
# This profile includes Center for Internet Security®
# Red Hat Enterprise Linux 10.0 CIS Benchmarks™ content.
#
# Profile ID:  xccdf_org.ssgproject.content_profile_cis
# Benchmark ID:  xccdf_org.ssgproject.content_benchmark_RHEL-10.0
# Benchmark Version:  0.1.74
# XCCDF Version:  1.2

name = "hardened_xccdf_org.ssgproject.content_profile_cis"
description = "CIS Red Hat Enterprise Linux 10.0 Benchmark for Level 2 - Server"
version = "0.1.74"

[customizations.openscap]
profile_id = "xccdf_org.ssgproject.content_profile_cis"
# If your hardening data stream is not part of the 'scap-security-guide' package
# provide the absolute path to it (from the root of the image filesystem).
# datastream = "/usr/share/xml/scap/ssg/content/ssg-xxxxx-ds.xml"

[[customizations.filesystem]]
mountpoint = "/home"
size = 1073741824

[[customizations.filesystem]]
mountpoint = "/tmp"
size = 1073741824

[[customizations.filesystem]]
mountpoint = "/var"
size = 3221225472

[[customizations.filesystem]]
mountpoint = "/var/tmp"
size = 1073741824

[[packages]]
name = "aide"
version = "*"

[[packages]]
name = "libselinux"
version = "*"

[[packages]]
name = "audit"
version = "*"

[customizations.kernel]
append = "audit_backlog_limit=8192 audit=1"

[customizations.services]
enabled = ["auditd","crond","firewalld","systemd-journald","rsyslog"]
disabled = []
masked = ["nfs-server","rpcbind","autofs","bluetooth","nftables"]
```

Note

Do not use this exact blueprint snippet for image hardening. It does not reflect a complete profile. As Red Hat constantly updates and refines security requirements for each profile in the `scap-security-guide`{.literal} package, it makes sense to always re-generate the initial template by using the most up-to-date version of the data stream provided for your system.

Now you can customize the blueprint or use it as it is to build an image.

By using RHEL image builder, you can generate the necessary configurations for the stage based on your blueprint customization. This action adds two packages to the image:

-   `openscap-scanner`{.literal} is the `OpenSCAP`{.literal} tool.

-   `scap-security-guide`{.literal} is the package that contains the remediation and evaluation instructions.

    The remediation stage uses the `scap-security-guide`{.literal} package for the datastream because this package is installed on the image by default. If you want to use a different datastream, add the necessary package to the blueprint and specify the path to the datastream in the `oscap`{.literal} configuration.

### [9.2. Creating a pre-hardened image with RHEL image builder](#creating-a-pre-hardened-image-with-rhel-image-builder) {#creating-a-pre-hardened-image-with-rhel-image-builder .title}

Use RHEL image builder on-premise to create pre-hardened RHEL images with support to the OpenSCAP integration.

By configuring a blueprint, you can perform the following actions:

-   Create images that are pre-hardened and compliant with a specific profile
-   Deploy the pre-hardened images in a Virtual Machine (VM), or a bare-metal environment, for example.

**Prerequisites**

-   You are logged in as the root user or a user who is a member of the `weldr`{.literal} group.
-   The `openscap`{.literal} and `scap-security-guide`{.literal} packages are installed.

**Procedure**

1.  Create a hardening blueprint in the Tom's Obvious Minimal Language (TOML) format, using the `OpenSCAP`{.literal} tool and `scap-security-guide`{.literal} content, and modify it if necessary:

    ``` {.language-plaintext tabindex="-1"}
    # oscap xccdf generate fix --profile=<profileID> --fix-type=<blueprint> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml > cis.toml
    ```

    Replace *`<profileID>`{.literal}* with the profile ID that the system should comply with, for example, `cis`{.literal}.

2.  Start the build of hardened image:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder build <image_type> --blueprint <blueprint_name>
    ```

    Replace *`<image_type>`{.literal}* with any image type, for example, `qcow2`{.literal}.

    After the image build is ready, you can use your pre-hardened image on your deployments. See [Creating a virtual machine from a Kernel-based Virtual Machine (KVM) guest image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-and-deploying-guest-images-wht-image-builder#creating-a-virtual-machine-from-a-kvm-guest-image).

**Verification**

After you deploy your pre-hardened image, you can perform a configuration compliance scan to verify that the image is aligned with the selected security profile.

Important

Performing a configuration compliance scanning does not guarantee the system is compliant. For more information, see [Configuration compliance scanning](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#configuration-compliance-scanning).

**Additional resources**

-   [Scanning the system for configuration compliance and vulnerabilities](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance)

### [9.3. Customizing a pre-hardened image with RHEL image builder](#customizing-a-pre-hardened-image-with-rhel-image-builder) {#customizing-a-pre-hardened-image-with-rhel-image-builder .title}

You can customize a security profile by changing rule, such as password length, removing or selecting rules to implement internal policies. You cannot define new rules by customizing a profile.

Building an image from the blueprint creates a tailoring file and saves it to `/usr/share/xml/oscap-tailoring/tailoring.xml`{.literal} with a new tailoring profile ID. The new profile ID have `tailoring`{.literal} appended as a suffix to the base profile. For example, if you use the Center for Internet Security (CIS) (`cis`{.literal}) base profile, the profile ID is `xccdf_org.ssgproject.content_profile_cis_tailoring`{.literal}.

**Prerequisites**

-   You are logged in as the root user or a user who is a member of the `weldr`{.literal} group.
-   The `openscap`{.literal} and `scap-security-guide`{.literal} packages are installed.

**Procedure**

1.  Create a hardening blueprint in the TOML format from a selected profile. For example:

    ``` {.language-plaintext tabindex="-1"}
    # oscap xccdf generate fix --profile=<profileID> --fix-type=blueprint /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml > <profileID>tailored.toml
    ```

2.  Append the tailoring section with the customized rule set to the blueprint. The tailoring customization only affects the default selected or unselected state of rules in the base profile without changing the state of other rules.

    ``` {.language-plaintext tabindex="-1"}
    # Blueprint for CIS Red Hat Enterprise Linux 10.0 Benchmark for Level 2 - Server
    # ...
    [customizations.openscap.tailoring]
    selected = [ "xccdf_org.ssgproject.content_bind_crypto_policy" ]
    unselected = [ "grub2_password" ]
    ```

3.  Start the build of a hardened image:

    ``` {.language-plaintext tabindex="-1"}
    # *image-builder build <image_type> --blueprint <blueprintProfileID> *
    ```

    Replace *`<image_type>`{.literal}* with any image type, for example, `qcow2`{.literal}.

    After the image build is ready, use your pre-hardened image on your deployments.

**Verification**

After you deploy your pre-hardened image, you can perform a configuration compliance scan to verify that the image is aligned with the selected security profile.

Important

Performing a configuration compliance scanning does not guarantee the system is compliant. For more information, see [Configuration compliance scanning](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#configuration-compliance-scanning).

**Additional resources**

-   [Scanning the system for configuration compliance and vulnerabilities](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance)

## [Chapter 10. Enabling FIPS mode with RHEL image builder](#enabling-fips-mode-with-rhel-image-builder) {#chapter-10.-enabling-fips-mode-with-rhel-image-builder .title}

You can create a customized image and boot a FIPS-enabled RHEL image. Before you compose the image, you must change the value of the `fips`{.literal} directive in your blueprint.

**Prerequisites**

-   You are logged in as the root user or a user who is a member of the `weldr`{.literal} group.

**Procedure**

1.  Create a plain text file in the Tom's Obvious, Minimal Language (TOML) format with the following content:

    ``` {.language-plaintext tabindex="-1"}
    name = "system-fips-mode-enabled"
    description = "blueprint with FIPS enabled"
    version = "0.0.1"

    [customizations]
    fips = true

    [[customizations.user]]
    name = "admin"
    password = "admin"
    groups = ["users", "wheel"]
    ```

2.  Build the customized RHEL image:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder build image-type --blueprint blueprint-name
    ```

**Verification**

1.  Log in to the system image with the username and password that you configured in your blueprint.

2.  Check if FIPS mode is enabled:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /proc/sys/crypto/fips_enabled
    1
    ```

## [Chapter 11. Generating a WSL 2 image with RHEL image builder](#generating-wsl2-image-with-rhel-image-builder) {#chapter-11.-generating-a-wsl-2-image-with-rhel-image-builder .title}

You can use the RHEL image builder to create a Windows Subsystem for Linux (WSL). After building the image in the `.wsl`{.literal} format, you can deploy it locally by double-clicking the image.

Windows Subsystem for Linux (WSL) runs Linux distributions alongside your Windows environment. WSL images support the following image customizations:

-   `cloud-init`{.literal}
-   distro
-   packages
-   modules
-   groups
-   minimal

Note that WSL images do not support the locale and file system customizations. You cannot configure file system and storage options because WSL instances do not have their own disk images by design.

**Prerequisites**

-   An existing blueprint.
-   A Windows system with the `wsl`{.literal} command installed. See [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

**Procedure**

1.  Build the customized RHEL image:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder build wsl --blueprint <blueprint-name>
    ```

2.  Download the image:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder image <UUID>
    ```

    RHEL image builder downloads the image to the current directory path. The UUID and the image size are displayed:

    ``` {.language-plaintext tabindex="-1"}
    $ UUID-image-name. type: size MB
    ```

    The image filename defaults to using the unique identifier included in the filename, such as `af9e8627867e-image.wsl`{.literal}. The unique identifier number is provided to the `wsl.exe`{.literal} utility.

3.  Import the `wsl`{.literal} image to the Microsoft Windows system and start the image installation.

**Additional resources**

-   [Getting started with RHEL on WSL](https://developers.redhat.com/articles/2025/05/20/getting-started-rhel-windows-subsystem-linux)

## [Chapter 12. Preparing and deploying a KVM Guest Image by using RHEL image builder](#creating-and-deploying-guest-images-wht-image-builder) {#chapter-12.-preparing-and-deploying-a-kvm-guest-image-by-using-rhel-image-builder .title}

Use RHEL image builder to create a `.qcow2`{.literal} image that you can deploy on a Kernel-based Virtual Machine (KVM) based hypervisor.

Creating a customized KVM guest image involves the following high-level steps:

1.  Create a blueprint for the `.qcow2`{.literal} image.
2.  Create a `.qcow2`{.literal} image by using RHEL image builder.
3.  Create a virtual machine from the KVM guest image.

### [12.1. Creating customized KVM guest images by using RHEL image builder](#creating-customized-kvm-guest-images-by-using-rhel-image-builder) {#creating-customized-kvm-guest-images-by-using-rhel-image-builder .title}

You can create a customized `.qcow2`{.literal} Kernel-based Virtual Machine (KVM) guest image by using the GUI RHEL image builder.

**Prerequisites**

-   You must be in the `root`{.literal} or `weldr`{.literal} group to access the system.
-   The `cockpit-image-builder`{.literal} package is installed.
-   On a RHEL system, you have opened the RHEL image builder dashboard of the web console.
-   You have created a blueprint. See [Creating a blueprint in the web console interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-cli).

**Procedure**

1.  Click the blueprint name you created.
2.  Select the tab **Images**.
3.  Click **Create Image** to create your customized image. The **Create Image** window opens.
4.  From the **Type** drop-down menu list, select `QEMU Image(.qcow2)`{.literal}.
5.  Set the size that you want the image to be when instantiated and click **Create**.
6.  A small pop-up on the upper right side of the window informs you that the image creation has been added to the queue. After the image creation process is complete, you can see the **Image build complete** status.

**Verification**

-   Click the breadcrumbs icon and select the **Download** option. RHEL image builder downloads the KVM guest image `.qcow2`{.literal} file to your default download location.

**Additional resources**

-   [Creating a blueprint in the web console interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-gui)

### [12.2. Creating a virtual machine from a KVM guest image](#creating-a-virtual-machine-from-a-kvm-guest-image) {#creating-a-virtual-machine-from-a-kvm-guest-image .title}

Create a new VM from a KVM Guest Image by using the `.qcow2`{.literal} image that you created by using RHEL image builder. The customized image already has `cloud-init`{.literal} installed and enabled.

**Prerequisites**

-   You created a `.qcow2`{.literal} image by using RHEL image builder.
-   You have the `qemu-kvm`{.literal} package installed on your system. You can check if the `/dev/kvm`{.literal} device is available on your system, and if virtualization features are enabled in the firmware.
-   You have the `libvirt`{.literal} and `virt-install`{.literal} packages installed on your system.
-   You have the `genisoimage`{.literal} utility, which is provided by the `xorriso`{.literal} package, installed on your system.

**Procedure**

1.  Move the `.qcow2`{.literal} image that you created by using RHEL image builder to the `/var/lib/libvirt/images/`{.literal} directory.

2.  Create a directory, for example, `cloudinitiso`{.literal}, and navigate to this newly created directory:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir cloudinitiso
    $ cd cloudinitiso
    ```

3.  Create a file named `meta-data`{.literal}. Add the following information to this file:

    ``` {.language-plaintext tabindex="-1"}
    instance-id: citest
    local-hostname: vmname
    ```

4.  Create a file named `user-data`{.literal}. Add the following information to the file:

    ``` {.language-plaintext tabindex="-1"}
    # cloud-config
    user: admin
    password: password
    chpasswd: {expire: False}
    ssh_pwauth: True
    ssh_authorized_keys:
      - ssh-rsa AAA...fhHQ== your.email@example.com
    ```

    `ssh_authorized_keys`{.literal} is your SSH public key. You can find your SSH public key in `~/.ssh/`{.literal}*`id_rsa.pub\`{.literal}*.

5.  Use the `genisoimage`{.literal} utility to create an ISO image that includes the `user-data`{.literal} and `meta-data`{.literal} files.

    ``` {.language-plaintext tabindex="-1"}
    # genisoimage -output cloud-init.iso -volid cidata -joliet -rock user-data meta-data

    I: -input-charset not specified, using utf-8 (detected in locale settings)
    Total translation table size: 0
    Total rockridge attributes bytes: 331
    Total directory bytes: 0
    Path table size(bytes): 10
    Max brk space used 0
    183 extents written (0 MB)
    ```

6.  Create a new VM from the KVM Guest Image by using the `virt-install`{.literal} command. Include the ISO image you created in step 4 as an attachment to the VM image.

    ``` {.language-plaintext tabindex="-1"}
    # virt-install \
        --memory 4096 \
        --vcpus 4 \
        --name myvm \
        --disk rhel-10-x86_64-kvm.qcow2,device=disk,bus=virtio,format=qcow2 \
        --disk cloud-init.iso,device=cdrom \
        --os-variant rhel 10 \
        --virt-type kvm \
        --graphics none \
        --import
    ```

    -   `--graphics`{.literal} none means it is a headless RHEL 10 VM.
    -   `--vcpus 4`{.literal} means that it uses 4 virtual CPUs.
    -   `--memory 4096`{.literal} means it uses 4096 MB RAM.

7.  The VM installation starts:

    ``` {.language-plaintext tabindex="-1"}
    Starting install...
    Connected to domain mytestcivm
    ...
    [  OK  ] Started Execute cloud user/final scripts.
    [  OK  ] Reached target Cloud-init target.

    Red Hat Enterprise Linux 10 (Ootpa)
    Kernel 4.18.0-221.el8.x86_64 on an x86_64
    ```

**Verification**

After the boot is complete, the VM shows a text login interface. To log in to the local console of the VM, you can use the details from the `user-data`{.literal} file:

1.  Enter `admin`{.literal} as a username and press Enter.

2.  Enter `password`{.literal} as password and press Enter.

    After the login authentication is complete, you have access to the VM by using the CLI.

**Additional resources**

-   [Preparing RHEL to host virtual machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/preparing-rhel-to-host-virtual-machines)
-   [Setting up container storage by using cloud-init](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_cloud-init_for_rhel/setting-up-container-storage-by-using-cloud-init)

## [Chapter 13. Creating Vagrant boxes with RHEL image builder](#creating-vagrant-boxes-with-rhel-image-builder) {#chapter-13.-creating-vagrant-boxes-with-rhel-image-builder .title}

With RHEL image builder, you can choose between the `vagrant-libvirt`{.literal} or `vagrant-virtualbox`{.literal} image types to create Vagrant boxes.

RHEL image builder generates pre-configured images optimized for different hypervisors:

-   `vagrant-libvirt`{.literal} creates a QCOW2-based image for `libvirt`{.literal}
-   `vagrant-virtualbox`{.literal} creates a VMDK-based image for `VirtualBox`{.literal}

The pre-configured images include the `vagrant`{.literal} user with sudo privileges. This configuration simplifies administrative tasks within the Vagrant box.

The images are supported in the following architectures: `aarch64`{.literal} and `x86_64`{.literal}.

### [13.1. Building Vagrant images for the libvirt and VirtualBox back ends](#building-vagrant-images-for-the-libvirt-and-virtualbox-backends) {#building-vagrant-images-for-the-libvirt-and-virtualbox-back-ends .title}

You can use RHEL image builder to create custom Vagrant boxes for different providers by using the `vagrant-libvirt`{.literal} and `vagrant-virtualbox`{.literal} image types.

The `vagrant-libvirt`{.literal} image type creates a `QCOW2`{.literal}-based box for use with the `libvirt`{.literal} provider. The `vagrant-virtualbox`{.literal} image type creates a box compatible with the `VirtualBox`{.literal} provider. You can customize the image type by using blueprint customizations.

**Prerequisites**

-   RHEL image builder is installed and running.
-   You have a blueprint file ready to build.
-   For the `libvirt box`{.literal}: A host system with the `libvirt`{.literal} hypervisor is installed and running.
-   For the `VirtualBox`{.literal} box: A host system with `VirtualBox`{.literal} is installed.

**Procedure**

1.  Build the Vagrant box image:

    -   For `libvirt`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo image-builder build --distro rhel-10.0 vagrant-libvirt
        ```

    -   For `VirtualBox`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo image-builder build - -distro <distro-name> vagrant-virtualbox
        ```

        This creates a `.box`{.literal} file.

2.  Import the new `.box`{.literal} file to your local Vagrant environment. You must explicitly set the `provider`{.literal} to `virtualbox`{.literal} because it is not the standard provider.

    ``` {.language-plaintext tabindex="-1"}
    $ vagrant box add --provider=virtualbox <path/to/box> --name=<box-name>
    ```

    Replace `path/to/image-name.box`{.literal} with the actual path to your file and *`<box_name>`{.literal}* with a name such as `rhel10-vagrant`{.literal}.

3.  Create a new directory for your project, and initialize Vagrant:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir <my_vagrant_project>
    $ cd <my_vagrant_project>
    $ vagrant init <box-name>
    ```

    This creates the `Vagrantfile`{.literal} configuration file and sets its default box to *\<box-name\>*.

4.  Launch the virtual machine by using Vagrant:

    ``` {.language-plaintext tabindex="-1"}
    $ vagrant up
    ```

## [Chapter 14. Creating stateless images with RHEL image builder](#creating-stateless-images-with-rhel-image-builder) {#chapter-14.-creating-stateless-images-with-rhel-image-builder .title}

Use RHEL image builder to create stateless images. After building the image in the `pxe-tar-xz`{.literal} format, you can use the resulting stateless PXE image output in PXE or UEFI HTTP network boot environments. For more information, see the `README`{.literal} contained within the generated tarball file.

### [14.1. Building a PXE-bootable RHEL image with image builder CLI](#building-a-pxe-bootable-rhel-image-with-image-builder-cli) {#building-a-pxe-bootable-rhel-image-with-image-builder-cli .title}

Use the RHEL image builder CLI and a customized blueprint to create a RHEL image for PXE deployments. The tar file includes kernel, `initrd`{.literal}, and root file system components. Stateless PXE images are available for the 64-bit ARM and 64-bit x86 architectures and support some customizations.

**Prerequisites**

-   An existing customized blueprint.

**Procedure**

1.  Build the customized RHEL image:

    ``` {.language-plaintext tabindex="-1"}
    $ image-builder build pxe-tar-xz --blueprint <blueprint-name>
    ```

    RHEL image builder creates the image in the current directory path:

    ``` {.language-plaintext tabindex="-1"}
    <os>-pxe-tar-xz-<architecture>.tar.xz
    ```

2.  Extract the image components to your boot server. Locate the tar file. If the tool created a directory, enter that directory to find the `.tar.xz`{.literal} file. Then, extract it to your TFTP root:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo tar -xJf <image-name>.tar.xz -C /var/lib/tftpboot/rhel-pxe/
    ```

### [14.2. Booting a stateless image in a PXE boot environment with an HTTP server](#booting-a-stateless-image-in-a-pxe-boot-environment-with-an-http-server) {#booting-a-stateless-image-in-a-pxe-boot-environment-with-an-http-server .title}

Serve the `rootfs.img`{.literal} image by using HTTP for faster and more reliable transfers than TFTP alone.

**Prerequisites**

-   An *`<os>`{.literal}*`-pxe-tar-xz-`{.literal}*`<architecture>`{.literal}*`.tar.xz`{.literal} image exists.

-   The target system has enough memory to hold the kernel, initrd, and `rootfs`{.literal} simultaneously.

-   2GiB of capacity for small images, but it varies depending on the workload.

    Warning

    Insufficient RAM can result in a kernel panic during the boot process.

**Procedure**

1.  Prepare the TFTP server by placing the `vmlinuz`{.literal}, `initrd.img`{.literal}, and `rootfs.img`{.literal} files in the root directory of your TFTP server.

2.  Modify the `grub.cfg`{.literal} configuration, replacing the `HTTP-SERVER`{.literal} placeholder with the actual URL of your HTTP server.

3.  Serve the `rootfs.img`{.literal} by using HTTP inside the directory containing the `rootfs.img`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ python3 -m http.server 8000
    ```

### [14.3. Booting a stateless image in a PXE boot environment with a combined image](#booting-a-stateless-image-in-a-pxe-boot-environment-with-a-combined-image) {#booting-a-stateless-image-in-a-pxe-boot-environment-with-a-combined-image .title}

Eliminate the need for a separate HTTP server by merging the root filesystem into the initial ramdisk.

**Prerequisites**

-   A PXE stateless image exists.

-   The target system has enough memory to hold the kernel, initrd, and `rootfs`{.literal} simultaneously.

-   2GiB of capacity for small images, but it varies depending on the workload.

    Warning

    Insufficient RAM can result in a kernel panic during the boot process.

**Procedure**

1.  Create the rootfs CPIO archive:

    ``` {.language-plaintext tabindex="-1"}
    $ echo rootfs.img | cpio -c --quiet -L -o > rootfs.cpio
    ```

2.  Concatenate the `initrd.img`{.literal} and `rootfs.cpio`{.literal} images:

    ``` {.language-plaintext tabindex="-1"}
    $ cat initrd.img rootfs.cpio > combined.img
    ```

3.  Boot the system by using the resulting `combined.img`{.literal} file as your initrd in your PXE configuration.

    Note

    Using a combined image significantly increases the initial network payload. Because the entire root filesystem is transferred during the PXE phase, ensure your network bandwidth can handle the increased traffic, especially when booting multiple systems simultaneously.

## [Chapter 15. Pushing a container to a registry and embedding it into an image](#creating-and-registering-a-container-to-embed-to-image) {#chapter-15.-pushing-a-container-to-a-registry-and-embedding-it-into-an-image .title}

With RHEL image builder, you can build security-hardened images by using the OpenSCAP tool. You can take advantage of the support for container customization in the blueprints to create a container and embed it directly into the image you create.

### [15.1. Customizing a blueprint to embed a container into an image](#blueprint-customization-to-embed-a-container-into-an-image) {#customizing-a-blueprint-to-embed-a-container-into-an-image .title}

Embed a container from [registry.access.redhat.com](https://catalog.redhat.com/en/software/containers/ubi10/ubi/66f2b46b122803e4937d11ae) by adding a container customization to your blueprint. RHEL image builder pulls the container during the image build and stores the container in the image.

The default local container storage location depends on the image type, so that all supported `container-tools`{.literal}, such as Podman, can work with it.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

-   Customize your blueprint with the container:

``` {.language-plaintext tabindex="-1"}
[[containers]]
source = "registry.access.redhat.com/ubi10/ubi:latest"
name =  "_<local_name>_"
tls-verify = true
```

-   `source`{.literal} - Mandatory field. It is a reference to the container image at a registry. This example uses the `registry.access.redhat.com`{.literal} registry. You can specify a tag version. The default tag version is the `latest`{.literal}.

-   `name`{.literal} - The name of the container in the local registry.

-   `tls-verify`{.literal} - Boolean field. The `tls-verify`{.literal} boolean field controls the transport layer security. The default value is `true`{.literal}.

    To access protected container resources, you can use a `containers-auth.json`{.literal} file.

### [15.2. Pushing a container artifact directly to a container registry](#pushing-a-container-artifact-directly-to-a-container-registry) {#pushing-a-container-artifact-directly-to-a-container-registry .title}

You can push container artifacts directly to a container registry after you build them by using the RHEL image builder CLI.

**Prerequisites**

-   Access to [quay.io registry](https://quay.io). This example uses the `quay.io`{.literal} container registry as a target registry, but you can use a container registry of your choice.

**Procedure**

1.  Configure a `registry-config.toml`{.literal} file to select the container provider. The credentials are optional.

    ``` {.language-plaintext tabindex="-1"}
    provider = "<container_provider>"
    [settings]
    tls_verify = false
    username = "<admin>"
    password = "<your_password>"
    ```

2.  Create a blueprint in the `.toml`{.literal} format. This is a blueprint for the container in which you install an `nginx`{.literal} package into the blueprint.

    ``` {.language-plaintext tabindex="-1"}
    name = "simple-container"
    description = "Simple RHEL container"
    version = "0.0.1"
    [[packages]]
    name = "nginx"
    version = "*"
    ```

3.  Build the container image, by passing the registry and the repository to the `image-builder`{.literal} tool as arguments.

    ``` {.language-plaintext tabindex="-1"}
    # image-builder build --blueprint <simple-container> --extra-repo "quay.io:8080/<namespace>/<repository>" --extra-repo registry-config.toml
    ```

    Note

    Building the container image takes time because of resolving dependencies of the customized packages.

4.  After the image build finishes, the container you created is available in [quay.io](https://quay.io).

**Verification**

1.  Open [quay.io](https://quay.io) and click `Repository Tags`{.literal}. You can see details about the container you created, such as:

    -   Last modified
    -   Image size
    -   The `manifest ID`{.literal} that you can copy to the clipboard.

2.  Copy the `manifest ID`{.literal} value to build the image in which you want to embed a container.

**Additional resources**

-   [Image tags overview documentation](https://docs.redhat.com/en/documentation/red_hat_quay/3.14/html/about_quay_io/image-tags-overview)

### [15.3. Building an image and pulling the container into the image](#building-an-image-and-pulling-the-container-into-the-image) {#building-an-image-and-pulling-the-container-into-the-image .title}

After you create a container image, build your customized image and pull the container image into it. Use the `container customization`{.literal} specification in the blueprint and the `container name`{.literal} for the final image. It fetches the container image and add it to the local Podman container storage.

**Prerequisites**

-   You created a container image and pushed it into your local `quay.io`{.literal} container registry instance. See [Pushing a container artifact directly to a container registry](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-and-registering-a-container-to-embed-to-image).
-   You have access to [registry.access.redhat.com](https://access.redhat.com/terms-based-registry).
-   You have a container `manifest ID`{.literal}.
-   You have the `qemu-kvm`{.literal} and `qemu-img`{.literal} packages installed.

**Procedure**

1.  Create a blueprint to build a `qcow2`{.literal} image. The blueprint must contain the `[[`{.literal}*`containers`{.literal}*`]]`{.literal} customization.

    ``` {.language-plaintext tabindex="-1"}
    name = "image"
    description = "A qcow2 image with a container"
    version = "0.0.1"
    distro = "rhel-10"
    [[packages]]
    name = "podman"
    version = "*"
    [[containers]]
    source = "registry.access.redhat.com/ubi10:8080/image/container/container-image@sha256:manifest-ID-from-Repository-tag: tag-version"
    name =  "source"
    tls-verify = true
    ```

2.  Build the container image:

    ``` {.language-plaintext tabindex="-1"}
    # image-builder build qcow2 --blueprint <blueprint>
    ```

    Note

    Building the image takes time because it checks the container on `quay.io`{.literal} registry.

    You can use the `qcow2`{.literal} image you created and downloaded to create a VM.

**Verification**

1.  Locate the resulting `qcow2`{.literal} image.

2.  Start the `qcow2`{.literal} image in a VM. See [Creating a virtual machine from a KVM guest image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/preparing-and-uploading-ami-images-to-aws).

3.  The `qemu`{.literal} wizard opens. Log in to the `qcow2`{.literal} image by entering the username and password. These can be the username and password you configured in the `.qcow2`{.literal} blueprint in the `customizations.user`{.literal} section, or created at boot time with `cloud-init`{.literal}.

4.  Run the container image and open a shell prompt inside the container:

    ``` {.language-plaintext tabindex="-1"}
    # podman run -it registry.access.redhat.com/ubi10:8080/<organization>/<repository>/bin/bash/
    ```

    `registry.access.redhat.com`{.literal} is the target registry, *`<organization>`{.literal}* is the organization, and `repository`{.literal} is the location to push the container when it finishes building.

5.  Check that the packages you added to the blueprint are available:

    ``` {.language-plaintext tabindex="-1"}
    # type -a nginx
    ```

    The output shows you the `nginx`{.literal} package path.

**Additional resources**

-   [Red Hat Container Registry Authentication](https://access.redhat.com/articles/RegistryAuthentication)
-   [Accessing and Configuring the Red Hat Registry](https://docs.redhat.com/en/documentation/openshift_container_platform/3.11/html/configuring_clusters/install-config-configuring-red-hat-registry)
-   [Building, running, and managing containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/index)

## [Chapter 16. Preparing and uploading cloud images by using RHEL image builder](#creating-cloud-images-with-image-builder) {#chapter-16.-preparing-and-uploading-cloud-images-by-using-rhel-image-builder .title}

RHEL image builder can create custom system images ready for use on various cloud platforms. To use your customized RHEL system image in a cloud environment, create the image with RHEL image builder, choose the output type, configure your system, and upload the image to your cloud account.

You can push customized image clouds by using the `Image Builder`{.literal} application in the RHEL web console, available for a subset of the service providers that RHEL image builder supports, such as **AWS** and **Microsoft Azure** clouds.

## [Chapter 17. Preparing and uploading AMI images to AWS](#preparing-and-uploading-ami-images-to-aws) {#chapter-17.-preparing-and-uploading-ami-images-to-aws .title}

You can create custom images and update them, either manually or automatically, on the AWS cloud with RHEL image builder.

### [17.1. Preparing to manually upload AWS AMI images](#preparing-to-manually-upload-aws-ami-images) {#preparing-to-manually-upload-aws-ami-images .title}

Before uploading an Amazon Machine Image (AMI) to Amazon Web Services (AWS), you must configure a system for uploading the images.

**Prerequisites**

-   A writable [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html#creating-bucket) prepared.

-   AWS authentication configured using one of the following methods:

    -   **Static credentials**: An Access Key ID and Secret Access Key configured in the AWS IAM account manager. You must have an Access Key ID configured in the [AWS IAM account manager](https://aws.amazon.com/iam/).
    -   **Dynamic credentials**: Short-lived credentials managed by using AWS IAM Identity Center (SSO).

**Procedure**

1.  Install Python 3 and the `pip`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install python3 python3-pip
    ```

2.  Install the [AWS command-line tools](https://aws.amazon.com/cli/) with `pip`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ pip3 install awscli
    ```

3.  Configure your AWS CLI authentication profile:

    -   **Configuring static credentials (AWS Access Keys)**: The command line prompts you to provide your credentials, region, and output format:

        ``` {.language-plaintext tabindex="-1"}
        $ aws configure
        ```

        ``` {.language-plaintext tabindex="-1"}
        AWS Access Key ID [None]:
        AWS Secret Access Key [None]:
        Default region name [None]:
        Default output format [None]:
        ```

    -   **Configuring dynamic credentials (AWS SSO / IAM Identity Center)**: If your organization uses short-lived dynamic credentials, log in to a separate profile. If you are running the CLI over a remote SSH session, include the `--remote`{.literal} flag:

        ``` {.language-plaintext tabindex="-1"}
        $ aws login --region eu-central-1 --profile auth --remote
        ```

        Follow the prompt link to authenticate in your browser. This creates an entry in your `~/.aws/config`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [profile auth]
        region = eu-central-1
        login_session = arn:aws:sts::12345678910:assumed-role/12345678910-admin/<username>
        ```

        Important

        `image-builder`{.literal} uses the AWS SDK for Go v2, which does not natively support dynamic credentials. If you attempt to upload by using only the profile above, the credentials are silently ignored, resulting in the following error: \"Getting: operation error S3: CreateMultipartUpload, get identity: get credentials: failed to refresh cached credentials, no EC2 IMDS role found...​\" To bypass this limitation, configure your `[default]`{.literal} or another designated profile to use `credential_process`{.literal}. This maps the dynamic session tokens to static-style credentials that `image-builder`{.literal} can read. Add the following to your `~/.aws/config`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [default]
        region = eu-central-1
        credential_process = aws configure export-credentials --profile auth --format process
        ```

4.  Define a name for your bucket and create a bucket:

    ``` {.language-plaintext tabindex="-1"}
    $ BUCKET=<bucketname>
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ aws s3 mb s3://$BUCKET
    ```

    Replace *`<bucketname>`{.literal}* with the actual bucket name. It must be a globally unique name.

5.  To grant Simple Storage Service (S3) access permission, create a `vmimport`{.literal} role in the AWS Identity and Access Management (IAM), if not already.

    a.  Create a `trust-policy.json`{.literal} file with the trust policy configuration in JSON format. For example:

        ``` {.language-plaintext tabindex="-1"}
        {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {
                    "Service": "vmie.amazonaws.com"
                },
                "Action": "sts:AssumeRole",
                "Condition": {
                    "StringEquals": {
                        "sts:Externalid": "vmimport"
                    }
                }
            }]
        }
        ```

    b.  Create a `role-policy.json`{.literal} file with the role policy configuration in JSON format:

        ``` {.language-plaintext tabindex="-1"}
        {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Action": ["s3:GetBucketLocation", "s3:GetObject", "s3:ListBucket"],
                "Resource": ["arn:aws:s3:::%s", "arn:aws:s3:::%s/"] }, { "Effect": "Allow", "Action": ["ec2:ModifySnapshotAttribute", "ec2:CopySnapshot", "ec2:RegisterImage", "ec2:Describe"],
                "Resource": "*"
            }]
        }
        ```

        ``` {.language-plaintext tabindex="-1"}
        $BUCKET $BUCKET
        ```

    c.  Create a role for your Amazon Web Services account, by using the `trust-policy.json`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        $ aws iam create-role --role-name vmimport --assume-role-policy-document \file://trust-policy.json
        ```

    d.  Embed an inline policy document by using the `role-policy.json`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        $ aws iam put-role-policy --role-name vmimport --policy-name vmimport --policy-document \file://role-policy.json
        ```

**Verification**

-   Verify the bucket was created:

    ``` {.language-plaintext tabindex="-1"}
    $ aws s3 ls | grep $BUCKET
    ```

-   Verify the `vmimport`{.literal} role was created:

    ``` {.language-plaintext tabindex="-1"}
    $ aws iam get-role --role-name vmimport
    ```

**Additional resources**

-   [Using high-level S3 commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)
-   [Best practices for IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
-   [Security best practices for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

### [17.2. Manually uploading an AMI image to AWS by using the CLI](#manually-uploading-an-ami-image-to-aws-by-using-the-cli) {#manually-uploading-an-ami-image-to-aws-by-using-the-cli .title}

You can use RHEL image builder to build AMI images and manually upload them directly to the Amazon AWS Cloud service provider by using the CLI.

**Prerequisites**

-   You have created static or dynamic credentials by using the `credential_process`{.literal} workaround configured on the local system. See [Preparing to manually upload AWS AMI images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/preparing-and-uploading-ami-images-to-aws#preparing-to-manually-upload-aws-ami-images).
-   You have an `Access Key ID`{.literal} configured in the [AWS IAM](https://aws.amazon.com/iam/) account manager.
-   You have a writable [S3 bucket](https://aws.amazon.com/s3/) prepared.
-   You have a defined blueprint.

**Procedure**

1.  Build the image:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo image-builder build ami \
      --blueprint <blueprint_name> \
      --aws-region us-east-1 \
      --aws-bucket <example_bucket> \
      --aws-ami-name <image_name>
    ```

2.  Upload the image to AWS. For standalone raw images, use the upload command:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo image-builder upload rhel-10.1-ami-x86_64.raw \
    --to=aws --aws-region=eu-central-1 \
    --aws-bucket=<my_bucket> --aws-ami-name <image_name>
    ```

    If you configured dynamic credentials with the default profile workaround, the `upload`{.literal} command automatically uses the configured `credential_process`{.literal} flow.

**Verification**

1.  Check the image available [EC2](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Images:sort=name) in the AWS console and selecting the correct region.
2.  On the dashboard, select your image and click Launch.

**Troubleshooting**

-   If the build or upload command fails with an authentication or permission error, you must confirm that your AWS CLI profile has valid credentials and that your IAM user or role can access the S3 bucket and the EC2 VM Import/Export API.
-   If the command reports that the bucket is missing, not accessible, or in the wrong location, you must verify that the bucket name matches `--aws-bucket`{.literal} and that the bucket exists in the same AWS Region you pass to `--aws-region`{.literal}.
-   If AWS rejects the import with a service role error, you must create the `vmimport`{.literal} IAM role and trust policy that VM Import/Export requires, as described in [Required service role to import a VM](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#vmimport-role).

**Additional resources**

-   [Required service role to import a VM](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#vmimport-role)

### [17.3. Creating and automatically uploading images to the AWS Cloud AMI](#creating-and-automatically-uploading-images-to-the-aws-cloud-ami) {#creating-and-automatically-uploading-images-to-the-aws-cloud-ami .title}

You can create a RAW image by using the RHEL image builder and select **Upload to AWS** to automatically upload the image to the Amazon AWS Cloud AMI service provider.

**Prerequisites**

-   You must have `root`{.literal} or `wheel`{.literal} group user access to the system.
-   You have opened the RHEL image builder interface of the RHEL web console in a browser.
-   You have created a RHEL image builder blueprint.
-   You must have an Access Key ID configured in the AWS Identity and Access Management (IAM) account manager.
-   You must have a writable AWS Simple Storage Service (S3) bucket prepared.

**Procedure**

1.  In the RHEL image builder dashboard, select your blueprint in **blueprint name**. Select the **Images** tab, and click **Create Image**.

2.  From the **Type** drop-down menu list, select `Amazon Machine Image Disk (.raw)`{.literal}, check **Upload to AWS**, and click **Next**.

    Note

    If you do not know your `Secret Key`{.literal}, generate a new `Access Key ID`{.literal}.

3.  Enter your `AWS access key ID`{.literal} and `AWS secret access key`{.literal} in the corresponding fields. Click **Next**.

4.  Enter the `Image name`{.literal}, `Amazon S3 bucket`{.literal} name, and `AWS region`{.literal}, then click **Next**.

5.  Review the information and click **Finish**. Wait for the **Image build complete** status.

6.  In the AWS console, navigate to [Service→EC2](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Images:sort=name), select the correct region, and verify your image shows `Available`{.literal} status.

7.  Select your image, click **Launch**, choose an instance type, and click **Review and Launch**.

8.  Review instance details, select or create a key pair, click **Launch**, and wait for the instance status to change to **running**:

    -   To create a new key pair, select **Create a new key pair**, enter a name, and click **Download Key Pair**.

**Verification**

-   Connect to your instance by using SSH:

    ``` {.language-plaintext tabindex="-1"}
    $ chmod 400 <your_instance_name>.pem
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i <your-instance_name>.pem \\
    ec2-user@<your-instance-IP-address>
    ```

    a.  Type `yes`{.literal} to confirm the connection.

-   Check if you can perform any actions while connected to your instance by using SSH.

**Additional resources**

-   [Open a case on Red Hat Customer Portal](https://access.redhat.com/support/cases/#/case/new/open-case?intcmp=hp%7Ca%7Ca3%7Ccase&caseCreate=true)
-   [Connecting to your Linux instance by using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
-   [Required Permissions for IAM Users](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#iam-permissions-image)
-   [Creating a blueprint in the web console interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-cli#creating-a-blueprint-by-using-the-command-line-interface)
-   [AWS IAM account manager](https://aws.amazon.com/iam/)
-   [AWS S3 bucket](https://aws.amazon.com/s3/)

## [Chapter 18. Preparing and uploading VHD images to Microsoft Azure](#preparing-and-uploading-vhd-images-to-microsoft-azure) {#chapter-18.-preparing-and-uploading-vhd-images-to-microsoft-azure .title}

You can create custom images and update them, either manually or automatically, on the Microsoft Azure cloud by using RHEL image builder.

### [18.1. Preparing to upload Microsoft Azure VHD images manually](#preparing-to-manually-upload-microsoft-azure-vhd-images) {#preparing-to-upload-microsoft-azure-vhd-images-manually .title}

To create a virtual hard drive (VHD) image that you can manually upload to the `Microsoft Azure`{.literal} cloud, you can use RHEL image builder.

**Prerequisites**

-   You must have a Microsoft Azure resource group and storage account.
-   You have Python installed. The `AZ CLI`{.literal} tool depends on Python.

**Procedure**

1.  Import the Microsoft repository key:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo rpm --import https://packages.microsoft.com/keys/microsoft-2025.asc
    ```

2.  Create a `packages-microsoft-com-prod`{.literal} repository:

    ``` {.language-plaintext tabindex="-1"}
    [azure-cli]
    name=Azure CLI
    baseurl=https://packages.microsoft.com/yumrepos/packages.microsoft.com/rhel/10/prod/
    enabled=1
    gpgcheck=1
    gpgkey=https://packages.microsoft.com/keys/microsoft.asc
    ```

3.  Install Microsoft Azure CLI. The downloaded version of the Microsoft Azure CLI package can vary depending on the currently available version.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install azure-cli
    ```

4.  Run Microsoft Azure CLI:

    ``` {.language-plaintext tabindex="-1"}
    $ az login
    ```

    The command line shows the following message: `Note, we have launched a browser for you to login. For old experience with device code, use az login --use-device-code`{.literal}. Then, the command line opens the [Login](https://microsoft.com/devicelogin) from where you can log in.

    Note

    If you are running a remote (SSH) session, the login page link does not open in the browser. In this case, you can copy the link to a browser and log in to authenticate your remote session. To sign in, use a web browser to open the [Login](https://microsoft.com/devicelogin) page and enter the device code to authenticate.

5.  List the keys for the storage account in Microsoft Azure and make note of the value `key1`{.literal} from the output of the previous command.

    ``` {.language-plaintext tabindex="-1"}
    $ az storage account keys list --resource-group <resource_group_name> --account-name <account_name>
    ```

    Replace *`resource-group-name`{.literal}* with the name of your Microsoft Azure resource group and *`storage-account-name`{.literal}* with the name of your Microsoft Azure storage account.

    a.  To list the available resources using the following command:

        ``` {.language-plaintext tabindex="-1"}
        $ az resource list
        ```

6.  Create a storage container:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage container create --account-name <storage_account_name> \
    --account-key <key1_value> --name <storage_account_name>
    ```

    Replace *`storage-account-name`{.literal}* with the name of the storage account.

**Additional resources**

-   [Microsoft Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?view=azure-cli-latest&pivots=dnf)

### [18.2. Manually uploading VHD images to Microsoft Azure cloud](#manually-uploading-vhd-images-to-microsoft-azure-cloud) {#manually-uploading-vhd-images-to-microsoft-azure-cloud .title}

Create your customized virtual hard drive (VHD) image, and manually upload it to the Microsoft Azure cloud. When you create a `.vhd`{.literal} image by using the CLI, RHEL image builder writes temporary files to the `/var`{.literal} subdirectory.

Note

The partition and filesystem configurations in your blueprint determine `.vhd`{.literal} image size. Insufficient storage might cause a "No space left on device" error. Ensure `/var`{.literal} has at least 15 to 20 GB of free space.

**Prerequisites**

-   Your system must be configured for uploading Microsoft Azure VHD images.
-   You have an Azure access key storage account.

**Procedure**

1.  Create a `azure.toml`{.literal} blueprint, and add the following information to it:

    ``` {.language-plaintext tabindex="-1"}
    provider = "azure"

    [settings]
    storageAccount = "<your-storage-account-name>"
    storageAccessKey = "<storage-access-key-you-copied-in-the-Azure-portal>"
    container = "<your-storage-container-name>"
    ```

2.  Build the image, passing the following arguments:

    ``` {.language-plaintext tabindex="-1"}
    $ image-builder build <your-blueprint> vhd <your-image-key> azure.toml
    ```

    Replace *\<your-image-key\>* with the name of the image that you want.

3.  Push the image to Microsoft Azure and create an instance from it:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage blob upload --account-name <account-name> --container-name <container-name> --file <image-disk>.vhd --name image-disk.vhd --type page
    ```

4.  After the upload to the Microsoft Azure Blob storage completes, create a Microsoft Azure image from it. The images that you create with RHEL image builder generate hybrid images that support `V1 = BIOS`{.literal} and `V2 = UEFI`{.literal}. Use `--hyper-v-generation`{.literal} to specify instance type. `V1`{.literal} is the default.

    ``` {.language-plaintext tabindex="-1"}
    $ az image create --resource-group resource_group_name --name image-disk.vhd --os-type linux --location location \
    --source https://$account_name.blob.core.windows.net/container_name/image-disk.vhd
    - Running
    ```

**Verification**

1.  Create an instance either with the Microsoft Azure portal, or a command similar to the following:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm create --resource-group resource_group_name --location location --name vm_name --image image-disk.vhd(--admin-username azure-user --generate-ssh-keys*
    - Running
    ```

2.  Use your private key by using SSH to access the resulting instance. Log in as `azure-user`{.literal}.

**Additional resources**

-   [Composing an image for the `.vhd`{.literal} format fails (Red Hat Knowledgebase)](https://access.redhat.com/solutions/6955577)

### [18.3. Creating and automatically uploading VHD images to Microsoft Azure cloud](#creating-and-automatically-uploading-vhd-images-to-microsoft-azure-cloud) {#creating-and-automatically-uploading-vhd-images-to-microsoft-azure-cloud .title}

By using RHEL image builder, you can create `.vhd`{.literal} images, which are automatically uploaded to an Azure Blob Storage in the Microsoft Azure Cloud service provider.

**Prerequisites**

-   You have root access to the system.
-   You have access to the RHEL image builder interface of the RHEL web console.
-   You created a blueprint. See [Creating a RHEL image builder blueprint in the web console interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-gui#creating-a-blueprint-in-the-web-console-interface).
-   You have a [Microsoft Storage Account](https://portal.azure.com/#create/Microsoft.StorageAccount) created.
-   You have a writable [Blob Storage](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts) prepared.

**Procedure**

1.  In the RHEL image builder dashboard, select your blueprint, click the **Images** tab, and click **Create Image** to create your customized `.vhd`{.literal} image.
2.  Select `Microsoft Azure (.vhd)`{.literal} from the **Type** drop-down, check **Upload to Azure**, enter the **Image Size**, and click **Next**.
3.  Enter your **Storage account** name and your **Storage access key** then, click **Next**.
4.  Review the configuration and click **Create**. The RHEL image builder and upload processes start.
5.  In the [Microsoft Azure portal](https://portal.azure.com) navigate to **Storage accounts** \> **Containers** and verify if your `.vhd`{.literal} is present.

**Verification**

1.  In the Azure portal search bar, type **Images** and click **+Create**. Configure the following details:

    -   Select your resource group and enter an image name.
    -   Set **OS type** to Linux and VM generation to **Gen 2**.
    -   Under **Storage Blob**, browse to select your VHD file.
    -   Choose an **Account Type**, for example, Standard SSD.

2.  Click **Review + Create**, and then **Create**. Wait for the image creation to complete.

3.  Click **Go to resource**, then click **Create VM**. Enter a VM name, configure the **Size** and **Administrator account** sections, then click **Review + Create** and **Create**.

4.  After the deployment finishes, retrieve the public IP address and connect by using SSH.

    \$ **ssh *\<username\>*@*\<public-IP-address\>***

**Additional resources**

-   [Microsoft Azure Storage Documentation](https://docs.microsoft.com/en-us/azure/storage/)
-   [Create an Azure storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal)

## [Chapter 19. Preparing and uploading VMDK custom images to vSphere](#preparing-and-uploading-vmdk-custom-images-to-vsphere) {#chapter-19.-preparing-and-uploading-vmdk-custom-images-to-vsphere .title}

You can create custom images and update them, either manually or automatically, to the VMware vSphere cloud by using RHEL image builder.

### [19.1. Creating and automatically uploading customized RHEL VMDK images by using image builder](#creating-and-automatically-uploading-customized-rhel-vmdk-images-by-using-image-builder) {#creating-and-automatically-uploading-customized-rhel-vmdk-images-by-using-image-builder .title}

With RHEL image builder, you can create customized system images in the Open Virtualization Format (OVA), and automatically upload these images to the VMware vSphere client.

The OVA (`.ova`{.literal}) is a `.vmdk`{.literal} image with additional metadata about the virtual hardware, which contains a minimal template to make it easier to import images into vSphere. The `.ovf`{.literal} (Open Virtualization Format) package is part of the vSphere `.ova`{.literal} image. After RHEL image builder finishes importing the `.ova`{.literal} image in the vSphere client, you can configure it with any additional hardware, such as network, disks, and CD-ROMs.

You can import the Open virtualization format (`.ova`{.literal}) image by using either the vSphere GUI or the `govc`{.literal} client. To upload the image by using the `govc`{.literal} client, see [Uploading VMDK images and creating a RHEL virtual machine in vSphere](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/preparing-and-uploading-vmdk-custom-images-to-vsphere#uploading-vmdk-images-and-creating-a-rhel-virtual-machine-in-vsphere).

**Prerequisites**

-   You opened the RHEL image builder app from the web console in a browser.
-   You created a blueprint.

**Procedure**

1.  In the RHEL image builder dashboard, click the `Blueprint`{.literal} tab.

2.  On the blueprint table, find the blueprint you want to build an image.

3.  On the right side of the chosen blueprint, click **Create Image**. The **Create image** dialog wizard opens.

4.  On the **Image output** page, complete the following steps:

    a.  From the **Select a blueprint** list, select the image type you want.
    b.  From the **Image output type** list, select the image output type you want.
    c.  Optional: Check **Upload to VMware** checkbox to upload the image directly to VMware.
    d.  Enter a size for the image.
    e.  Click **Next**.

5.  On the **Upload to VMware** page, enter the following information:

    a.  **Image name**: Enter the image name.
    b.  **Host**: Enter the VMware vSphere instance URL where you want to upload the image file.
    c.  **Cluster**: Enter the cluster name page where you want to upload the image.
    d.  **Datacenter**: The data center name where you want to upload the image.
    e.  **Datastore**: The data store name where you want to upload the image.
    f.  **Folder**: Folder name where you want to upload the image.
    g.  Click **Next**.

6.  On the **Review** page, review the details about the image creation and click **Create**.

    The image creation starts, showing the progress of this image creation and the subsequent upload to the VMware vSphere client.

### [19.2. Uploading VMDK images and creating a RHEL virtual machine in vSphere](#uploading-vmdk-images-and-creating-a-rhel-virtual-machine-in-vsphere) {#uploading-vmdk-images-and-creating-a-rhel-virtual-machine-in-vsphere .title}

With RHEL image builder, you can create customized VMware vSphere system images, either in the Open virtualization Format (`.ova`{.literal}) or in the Virtual Disk (`.vmdk`{.literal}) format.

You can upload customized images to the VMware vSphere client. You can upload the `.vmdk`{.literal} or `.ova`{.literal} image to VMware vSphere using the `govc import.vmdk`{.literal} CLI tool. The `vmdk`{.literal} you create contains the `cloud-init`{.literal} package installed, and you can use it to provision users by using user data, for example.

Note

Uploading `vmdk`{.literal} images by using the VMware vSphere GUI is not supported.

**Prerequisites**

-   You created a blueprint with username and password customizations.
-   You created a VMware vSphere image either in the `.ova`{.literal} or the `.vmdk`{.literal} format by using RHEL image builder and downloaded it to your host system.
-   You installed and configured the `govc`{.literal} CLI tool to be able to use the `import.vmdk`{.literal} command.

**Procedure**

1.  Configure the following values in the user environment with the GOVC environment variables:

    ``` {.language-plaintext tabindex="-1"}
    GOVC_URL
    GOVC_DATACENTER
    GOVC_FOLDER
    GOVC_DATASTORE
    GOVC_RESOURCE_POOL
    GOVC_NETWORK
    ```

2.  Navigate to the directory where you downloaded your VMware vSphere image.

3.  Launch the VMware vSphere image on vSphere by following the steps:

    a.  Import the VMware vSphere image into vSphere:

        ``` {.language-plaintext tabindex="-1"}
        $ govc import.vmdk ./api.vmdk <folder-name>
        ```

        -   For the `.ova`{.literal} format:

            ``` {.language-plaintext tabindex="-1"}
            $ govc import.ova ./api.ova <folder-name>
            ```

    b.  Create the VM in vSphere without powering it on:

        ``` {.language-plaintext tabindex="-1"}
        govc vm.create \
        -net.adapter=vmxnet3 \
        -m=4096 -c=2 -g=rhel8_64Guest \
        -firmware=efi -disk="<folder-name>/api.vmdk” \
        -disk.controller=scsi -on=false \
         vmname
        ```

        For the `.ova`{.literal} format, replace the line `-firmware=efi -disk="`{.literal}*`folder_name`{.literal}*`/api.vmdk”`{.literal} with `-firmware=efi -disk=”`{.literal}*`<folder-name>`{.literal}*`/api.ova”`{.literal}

    c.  Power-on the VM:

        ``` {.language-plaintext tabindex="-1"}
        $ govc vm.power -on <vm-name>
        ```

    d.  Retrieve the VM IP address:

        ``` {.language-plaintext tabindex="-1"}
        $ govc vm.ip <vm-name>
        ```

    e.  Use SSH to log in to the VM, using the username and password you specified in your blueprint:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh admin@ <vm-ip-address>
        ```

        Note

        Using images copied with the `govc datastore.upload`{.literal} command is not supported. The vSphere GUI does not support `import.vmdk`{.literal} command or direct, so `.vmdk`{.literal} images are not usable from the vSphere GUI.

### [19.3. Creating and automatically uploading VMDK images to vSphere using image builder GUI](#creating-and-automatically-uploading-vmdk-images-to-vsphere-using-image-builder-gui) {#creating-and-automatically-uploading-vmdk-images-to-vsphere-using-image-builder-gui .title}

You can build VMware images by using the RHEL image builder Graphical User Interface (GUI) tool and automatically push the images directly to your vSphere instance. This avoids the need to download the image file and push it manually.

The `vmdk`{.literal} that you create contains the `cloud-init`{.literal} package installed, and you can use it to provision users by using user data, for example. To build `.vmdk`{.literal} images by using RHEL image builder and push them directly to the vSphere instances service provider, follow the steps:

**Prerequisites**

-   You are a member of the `root`{.literal} or the `weldr`{.literal} group.
-   You have opened [RHEL image builder](https://localhost:9090) in a browser.
-   You have created a blueprint.
-   You have a vSphere Account.

**Procedure**

1.  For the blueprint you created, click the **Images** tab .

2.  Click **Create Image** to create your customized image.

    The **Image type** window opens.

3.  In the **Image type** window:

    a.  From the dropdown menu, select the Type: VMware vSphere (`.vmdk`{.literal}).
    b.  Check the **Upload to VMware** checkbox to upload your image to vSphere.
    c.  Optional: Set the size of the image you want to instantiate. The minimal default size is 2 GB.
    d.  Click **Next**.

4.  In the **Upload to VMware** window, under **Authentication**, enter the following details:

    a.  **Username**: username of the vSphere account.
    b.  **Password**: password of the vSphere account.

5.  In the **Upload to VMware** window, under **Destination**, enter the following details about the image upload destination:

    a.  **Image name**: a name for the image.
    b.  **Host**: The URL of your VMware vSphere.
    c.  **Cluster**: The name of the cluster.
    d.  **Data center**: The name of the data center.
    e.  **Data store**: The name of the Data store.
    f.  Click **Next**.

6.  In the **Review** window, review the details of the image creation and click **Finish**.

    You can click **Back** to modify any incorrect details.

    RHEL image builder adds the compose of a RHEL vSphere image to the queue, and creates and uploads the image to the Cluster on the vSphere instance you specified.

    After the process is complete, you can see the **Image build complete** status.

**Verification**

1.  Create a Virtual Machine (VM) from the image you uploaded and log in to it.

2.  Access VMware vSphere Client and search for the image in the Cluster.

3.  Select the image, open its menu, and click `New Virtual Machine`{.literal}.

4.  In the **New Virtual Machine** window, configure the following details:

    a.  Select `New Virtual Machine`{.literal}, and specify a name and a folder for your VM.
    b.  Select a computer resource and storage. For example, select `NFS-Node1`{.literal}.
    c.  Select compatibility, `BIOS`{.literal} only, a guest operating system. For example, *`Linux`{.literal}* and *`Red Hat Fedora (64-bit)`{.literal}*.
    d.  In **Customize hardware**, delete the default New Hard Disk and select an `Existing Hard Disk`{.literal} disk image:

5.  Review the configuration and click **Finish**.

6.  Navigate to the **VMs** tab, select the VM, and click **Start**.

7.  Log in with the credentials you created in the blueprint.

8.  Optional: Verify that the packages you added to the blueprint are installed. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm -qa | grep firefox
    ```

**Additional resources**

-   [Introduction to vSphere Installation and Setup](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vcenter-installation-and-setup/introduction-to-vsphere-installation-and-setup.html)

## [Chapter 20. Preparing and uploading custom GCE images to Google Cloud](#preparing-and-uploading-custom-gce-images-to-gcp) {#chapter-20.-preparing-and-uploading-custom-gce-images-to-google-cloud .title}

With RHEL image builder, you can build a Google Compute Engine (GCE) image, provide credentials for your user or Google Cloud service account, and then upload the GCE image directly to the Google Cloud environment.

### [20.1. Configuring and uploading a gce image to Google Cloud by using the CLI](#configuring-and-uploading-a-gce-image-to-gcp-by-using-the-cli) {#configuring-and-uploading-a-gce-image-to-google-cloud-by-using-the-cli .title}

Configure a configuration file with credentials to upload your Google Compute Engine (GCE) image to Google Cloud by using the RHEL image builder CLI.

**Prerequisites**

-   You have a valid Google account and credentials to upload your image to Google Cloud. The credentials can be from a user account or a service account. The account associated with the credentials must have at least the following identity and access management (IAM) roles assigned:

    -   `roles/storage.admin`{.literal} - to create and delete storage objects
    -   `roles/compute.storageAdmin`{.literal} - to import a VM image to Compute Engine.

-   You have an existing Google Cloud bucket.

    Warning

    You cannot manually import GCE image to Google Cloud, because such images do not boot. You must use either `gcloud`{.literal} or RHEL image builder to upload it.

**Procedure**

1.  Use a text editor to create a `gcp-config.toml`{.literal} configuration file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    provider = "gcp"
    [settings]
    bucket = "<gcp_bucket>"
    region = "<gcp_storage_region>"
    object = "<object_key>"
    credentials = "<gcp_credentials>"
    ```

    -   *`<gcp_bucket>`{.literal}* points to an existing bucket. This field stores the intermediate storage object of the image to be uploaded.

    -   *`<gcp_storage_region>`{.literal}* is both a regular Google storage region and a dual or multi-region.

    -   *`<object_key>`{.literal}* is the name of an intermediate storage object. It must not exist before the upload, and when the upload process finishes, it is deleted . If the object name does not end with `.tar.gz`{.literal}, the object name automatically adds the extension.

    -   *`<gcp_credentials>`{.literal}* is a `Base64-encoded`{.literal} scheme of the credentials JSON file downloaded from Google Cloud. The credentials determine which project the Google Cloud uploads the image to.

        Note

        Specifying *`<gcp_credentials>`{.literal}* in the `gcp-config.toml`{.literal} file is optional if you use a different mechanism to authenticate with Google Cloud. For other authentication methods, see [Authenticating with Google Cloud](https://osbuild.org/docs/user-guide/uploading-cloud-images/uploading-to-gcp#authenticating-with-gcp).

2.  Retrieve the *`<gcp_credentials>`{.literal}* from the JSON file downloaded from Google Cloud.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo base64 -w 0 cee-gcp-nasa-476a1fa485b7.json
    ```

3.  Create a compose with an additional image name and cloud provider profile:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo image-builder build gce --blueprint <blueprint_name> <image_key> gcp-config.toml
    ```

    The image build, upload, and cloud registration processes can take up to ten minutes to complete.

**Verification**

-   Verify that the image status is FINISHED:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo image-builder compose status
    ```

**Additional resources**

-   [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam)
-   [Create storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets)

### [20.2. How RHEL image builder sorts the authentication order of different Google Cloud credentials](#how-rhel-image-builder-sorts-the-authentication-order-of-different-gcp-credentials) {#how-rhel-image-builder-sorts-the-authentication-order-of-different-google-cloud-credentials .title}

You can use several different types of credentials with RHEL image builder to authenticate with Google Cloud. If you set RHEL image builder configuration to authenticate with Google Cloud by using multiple sets of credentials, it uses the credentials in an order of preference.

The order of preference is as follows:

1.  Credentials specified with the `image-builder`{.literal} command in the configuration file.

2.  `Application Default Credentials`{.literal} from the `Google Cloud SDK`{.literal} library, which tries to automatically find a way to authenticate by using the following options:

    a.  If you set the *GOOGLE_APPLICATION_CREDENTIALS* environment variable, Application Default Credentials tries to load and use credentials from the file that the variable points to.

    b.  Application Default Credentials tries to authenticate by using the service account attached to the resource that is running the code. For example, Google Compute Engine VM.

        Note

        You must use the Google Cloud credentials to determine which Google Cloud project to upload the images to. To upload to different projects, specify the credentials in `gcp-config.toml`{.literal} with the `image-builder`{.literal} command.

## [Chapter 21. Preparing and uploading custom images directly to OCI](#preparing-and-uploading-custom-images-directly-to-oci) {#chapter-21.-preparing-and-uploading-custom-images-directly-to-oci .title}

You can create custom images and automatically update them to the Oracle Cloud Infrastructure (OCI) instance by using RHEL image builder.

### [21.1. Creating and automatically uploading custom images to OCI](#creating-and-automatically-uploading-custom-images-to-oci) {#creating-and-automatically-uploading-custom-images-to-oci .title}

With RHEL image builder, you can build customized images and automatically push them directly to your Oracle Cloud Infrastructure (OCI) instance. Then, you can start an image instance from the OCI dashboard.

**Prerequisites**

-   You have `root`{.literal} or `weldr`{.literal} group user access to the system.
-   You have an [Oracle Cloud](https://www.oracle.com/cloud/sign-in.html) account.
-   You must have security access in an **OCI policy**.
-   You have created an OCI Bucket in the `OCI_REGION`{.literal} of your choice.

**Procedure**

1.  Open the RHEL image builder interface of the web console in a browser.

2.  Click **Create blueprint**. The **Create blueprint** wizard opens.

3.  On the **Details** page, enter a name for the blueprint, and optionally, a description. Click **Next**.

4.  On the **Packages** page, select the components and packages that you want to include in the image. Click **Next**.

5.  On the **Customizations** page, configure the customizations that you want for your blueprint. Click **Next**.

6.  On the **Review** page, click **Create**.

7.  To create an image, click **Create Image**. The **Create image** wizard opens.

8.  On the **Image output** page, complete the following steps:

    a.  From the **\"Select a blueprint\"** drop-down menu, select the blueprint you want.
    b.  From the **\"Image output type\"** drop-down menu, select `Oracle Cloud Infrastructure (.qcow2)`{.literal}.
    c.  Check the **Upload to OCI** checkbox to upload your image to the OCI.
    d.  Enter the **\"image size\"**. Click **Next**.

9.  On the **Upload to OCI - Authentication** page, enter the following mandatory details:

    a.  User OCID: You can find it in the Console on the page showing the user's details.
    b.  Private key

10. On the **Upload to OCI - Destination** page, enter the following mandatory details and click **Next**.

    -   Image name: a name for the image that you want to upload.
    -   OCI bucket
    -   Bucket namespace
    -   Bucket region
    -   Bucket compartment
    -   Bucket tenancy

11. Review the details in the wizard and click **Finish**.

    RHEL image builder adds the compose of a RHEL `.qcow2`{.literal} image to the queue.

**Verification**

1.  Access the [OCI dashboard](https://www.oracle.com/cloud/) and click **Custom Images**.
2.  Select the **Compartment** you specified for the image and locate the image in the **Import image** table.
3.  Click the image name and verify the image information.

**Additional resources**

-   [Managing custom images in the OCI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm)
-   [Managing buckets in the OCI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm)

## [Chapter 22. Preparing and uploading customized QCOW2 images directly to OpenStack](#preparing-and-uploading-customized-qcow2-images-directly-to-openstack) {#chapter-22.-preparing-and-uploading-customized-qcow2-images-directly-to-openstack .title}

You can create custom `.qcow2`{.literal} images with RHEL image builder and manually upload them to the OpenStack cloud deployments.

### [22.1. Uploading QCOW2 images to OpenStack](#uploading-qcow2-images-to-openstack) {#uploading-qcow2-images-to-openstack .title}

With the RHEL image builder tool, you can create customized `.qcow2`{.literal} images that are suitable for uploading to OpenStack cloud deployments and starting instances there. RHEL image builder creates images in the QCOW2 format, but with further changes specific to OpenStack.

**Prerequisites**

-   You have created a blueprint.

**Procedure**

1.  Start the compose of a `QCOW2`{.literal} image.

    ``` {.language-plaintext tabindex="-1"}
    # image-builder build qcow2 --blueprint blueprint_name
    ```

2.  Access the OpenStack dashboard and click +Create Image.

3.  On the left menu, select the `Admin`{.literal} tab.

4.  From the `System Panel`{.literal}, click `Image`{.literal}.

    The `Create An Image`{.literal} wizard opens.

5.  In the `Create An Image`{.literal} wizard:

    a.  Enter a name for the image
    b.  Click `Browse`{.literal} to upload the `QCOW2`{.literal} image.
    c.  From the `Format`{.literal} dropdown list, select the `QCOW2 - QEMU Emulator`{.literal}.
    d.  Click Create Image.

6.  On the left menu, select the `Project`{.literal} tab.

    a.  From the `Compute`{.literal} menu, select `Instances`{.literal}.

    b.  Click the Launch Instance button.

        The `Launch Instance`{.literal} wizard opens.

    c.  On the `Details`{.literal} page, enter a name for the instance. Click Next.

    d.  On the `Source`{.literal} page, select the name of the image you uploaded. Click Next.

    e.  On the `Flavor`{.literal} page, select the machine resources that best fit your needs. Click Launch.

7.  You can run the image instance using any mechanism such as the CLI or OpenStack web UI from the image. Use your private key by using SSH to access the resulting instance. Log in as `cloud-user`{.literal}.

## [Chapter 23. Preparing and uploading customized RHEL images to the Alibaba Cloud](#preparing-and-uploading-customized-rhel-images-to-the-alibaba-cloud) {#chapter-23.-preparing-and-uploading-customized-rhel-images-to-the-alibaba-cloud .title}

You can upload customized `.ami`{.literal} images that you created by using RHEL image builder to the Alibaba Cloud.

### [23.1. Creating an instance of a customized RHEL image using Alibaba Cloud](#creating-an-instance-of-a-customized-rhel-image-using-alibaba-cloud) {#creating-an-instance-of-a-customized-rhel-image-using-alibaba-cloud .title}

You can create instances of a customized RHEL image by using the Alibaba ECS Console.

**Prerequisites**

-   You have activated [OSS](https://www.alibabacloud.com/help/doc-detail/31884.htm?spm=a2c63.p38356.879954.10.7c0a64baufqGup#task-njz-hf4-tdb) and uploaded your custom image.
-   You have successfully imported your image to ECS Console.

**Procedure**

1.  Log in to the [ECS console.](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A%2F%2Fecs.console.aliyun.com%2F%3Fspm%3Da2c63.p38356.879954.13.7c0a64bajaDXMi)

2.  On the left-side menu, select **Instances**.

3.  In the upper-right corner, click **Create Instance**. A new window opens.

4.  Complete all the required information. See [Creating an instance by using the custom launch](https://www.alibabacloud.com/help/doc-detail/87190.htm?spm=a2c63.p38356.879954.13.581344d6KkTITK#task-vwq-5g4-r2b) for more details.

5.  Click **Create Instance** and confirm the order.

    Note

    You can see the option **Create Order** instead of **Create Instance**, depending on your subscription.

    As a result, you have an active instance ready for deployment from the `Alibaba ECS Console`{.literal}.

**Additional resources**

-   [Creating an instance by using a custom image](https://www.alibabacloud.com/help/doc-detail/25465.htm?spm=a2c63.p38356.b99.108.6f3f33f9vAQ1Vb)

### [23.2. Importing images to Alibaba Cloud](#importing-images-to-alibaba-cloud) {#importing-images-to-alibaba-cloud .title}

You can import a customized Alibaba RHEL image that you created by using RHEL image builder to the Elastic Compute Service (ECS).

**Prerequisites**

-   Your system is configured for uploading Alibaba images.
-   You have created an `ami`{.literal} image by using RHEL image builder.
-   You have a bucket. See [Creating a bucket](https://www.alibabacloud.com/help/doc-detail/31885.htm?spm=a2c63.p38356.b99.19.5c3f465a0WnfaV).
-   You have an [active Alibaba Account](https://account.alibabacloud.com/register/intl_register.htm?spm=a2c63.p38356.879954.7.2ce96962qvmvAi).
-   You activated [OSS](https://www.alibabacloud.com/help/doc-detail/31884.htm?spm=a2c63.p38356.879954.10.7c0a64baufqGup#task-njz-hf4-tdb).
-   You have uploaded the image to Object Storage Service (OSS).

**Procedure**

1.  Log in to the [ECS console](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A%2F%2Fecs.console.aliyun.com%2F%3Fspm%3Da2c63.p38356.879954.13.7c0a64bajaDXMi), click Images, then click Import Image. A dialog window opens.
2.  Confirm the correct region and enter the following information:

-   `OSS Object Address`{.literal}: Obtain from [OSS Object Address](https://www.alibabacloud.com/help/doc-detail/31912.htm?spm=5176.2020520101.0.0.34cc7d33vYKnS3).

-   `Image Name`{.literal}, `Operating System`{.literal}, `System Disk Size`{.literal}, `System Architecture`{.literal}.

-   `Platform`{.literal}: Red Hat

    1.  Optional: Provide `Image Format`{.literal} (`qcow2`{.literal} or `ami`{.literal}), `Image Description`{.literal}, and `Add Images of Data Disks`{.literal} details.

    2.  Click **OK** and wait for the import to complete.

    3.  Log in to the OSS console and select your bucket from the left menu.

    4.  Click the **Files**, then click **Upload**.

    5.  Configure **Upload To** to the current or specified directory, and **File ACL** for permission type.

    6.  Click **Upload**, select your image, then click **Open**.

        `ECS`{.literal} Console imports the customized image.

**Additional resources**

-   [Instructions for importing images](https://www.alibabacloud.com/help/doc-detail/48226.htm)
-   [Creating an instance from custom images](https://www.alibabacloud.com/help/doc-detail/25542.htm?spm=a2c63.p38356.879954.20.7c0a64batcdSMD#ImportImage)
-   [Upload an object](https://www.alibabacloud.com/help/doc-detail/31886.htm?spm=a2c63.p38356.b99.20.454c5dc4qRcnad)

### [23.3. Uploading customized RHEL images to Alibaba](#uploading-customized-rhel-images-to-alibaba) {#uploading-customized-rhel-images-to-alibaba .title}

You can upload a customized `AMI`{.literal} image you created by using RHEL image builder to the Object Storage Service (OSS).

**Prerequisites**

-   Your system is configured for uploading Alibaba images.
-   You have created an `ami`{.literal} image by using RHEL image builder.
-   You have a bucket. See [Creating a bucket](https://www.alibabacloud.com/help/doc-detail/31885.htm?spm=a2c63.p38356.b99.19.5c3f465a0WnfaV).
-   You have an [active Alibaba Account](https://account.alibabacloud.com/register/intl_register.htm?spm=a2c63.p38356.879954.7.2ce96962qvmvAi).
-   You activated [OSS](https://www.alibabacloud.com/help/doc-detail/31884.htm?spm=a2c63.p38356.879954.10.7c0a64baufqGup#task-njz-hf4-tdb).

**Procedure**

1.  Log in to the [OSS console](https://oss.console.aliyun.com/?spm=a2c63.p38356.879954.10.2171455fhuA3H5).

2.  In the Bucket menu on the left, select the bucket to which you want to upload an image.

3.  In the upper right menu, click the Files tab.

4.  Click Upload. A dialog window opens on the right side. Configure the following:

    -   **Upload To**: Choose to upload the file to the **Current** directory or to a **Specified** directory.
    -   **File ACL**: Choose the type of permission of the uploaded file.

5.  Click Upload.

6.  Select the image you want to upload to the OSS Console.

7.  Click Open.

**Additional resources**

-   [Upload an object](https://www.alibabacloud.com/help/doc-detail/31886.htm?spm=a2c63.p38356.b99.20.454c5dc4qRcnad)
-   [Creating an instance from custom images](https://www.alibabacloud.com/help/doc-detail/25542.htm?spm=a2c63.p38356.879954.20.7c0a64batcdSMD#ImportImage)
-   [Importing images](https://www.alibabacloud.com/help/doc-detail/48226.htm)

### [23.4. Preparing to upload customized RHEL images to Alibaba Cloud](#preparing-to-upload-customized-rhel-images-to-alibaba-cloud) {#preparing-to-upload-customized-rhel-images-to-alibaba-cloud .title}

To deploy a customized RHEL image to the Alibaba Cloud, first, you must verify the customized image. The image requires a specific configuration to boot, because Alibaba Cloud custom images must meet certain requirements.

Note

RHEL image builder generates images that conform to the requirements of Alibaba. However, you must use the Alibaba `image_check`{.literal} tool to verify the format compliance of your image.

**Prerequisites**

-   You must have created an Alibaba image by using RHEL image builder.

**Procedure**

1.  Connect to the system containing the image that you want to check by using the Alibaba `image_check`{.literal} tool.

2.  Download the `image_check`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    $ curl -O https://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/73848/cn_zh/1557459863884/image_check
    ```

3.  Change the file permission of the image compliance tool:

    ``` {.language-plaintext tabindex="-1"}
    # chmod +x image_check
    ```

4.  Run the command to start the image compliance tool checkup:

    ``` {.language-plaintext tabindex="-1"}
    # ./image_check
    ```

    The tool verifies the system configuration and generates a report that in your screen. The `image_check`{.literal} tool saves this report in the same folder where the image compliance tool is running.

**Troubleshooting**

-   If any of the **Detection Items** fail, follow the instructions in the command line to correct them.

**Additional resources**

-   [Image Compliance Tool](https://www.alibabacloud.com/help/doc-detail/73848.htm)

## [Legal Notice](#idm139688764001040) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
