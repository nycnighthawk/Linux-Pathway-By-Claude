---
{"title": "Packaging and distributing software", "guide": "packaging_and_distributing_software", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/packaging_and_distributing_software/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Packaging and distributing software {#packaging-and-distributing-software .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Packaging software by using the RPM package management system {#packaging-software-by-using-the-rpm-package-management-system .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139736916204400)

**Abstract**

Package software into an RPM package by using the RPM package manager. Prepare source code for packaging, package software, and investigate advanced packaging scenarios, such as packaging Python projects or RubyGems packages into RPM packages.

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

## [Chapter 1. Introduction to RPM](#introduction-to-rpm) {#chapter-1.-introduction-to-rpm .title}

The RPM Package Manager (RPM) is a package management system that runs on Red Hat Enterprise Linux (RHEL), CentOS, and Fedora. You can use RPM to distribute, manage, and update software that you create for any of these operating systems.

The RPM package management system has the following advantages over distributing software in conventional archive files:

-   RPM manages software in the form of packages that you can install, update, or remove independently of each other, which makes the maintenance of an operating system easier.
-   RPM simplifies the distribution of software because RPM packages are standalone binary files, similar to compressed archives. These packages are built for a specific operating system and hardware architecture. RPMs contain files such as compiled executables and libraries that are placed into the appropriate paths on the filesystem when the package is installed.

With RPM, you can perform the following tasks:

-   Install, upgrade, and remove packaged software.
-   Query detailed information about packaged software.
-   Verify the integrity of packaged software.
-   Build your own packages from software sources and complete build instructions.
-   Digitally sign your packages by using the GNU Privacy Guard (GPG) utility.
-   Publish your packages in a DNF repository.

In RHEL, RPM is fully integrated into the higher-level package management software, such as DNF or PackageKit. Although RPM provides its own command-line interface, most users need to interact with RPM only through this software. However, when building RPM packages, you must use the RPM utilities such as `rpmbuild(8)`{.literal}.

### [1.1. RPM packages](#rpm-packages) {#rpm-packages .title}

An RPM package consists of an archive of files and metadata used to install and erase these files on Red Hat Enterprise Linux (RHEL).

Specifically, the RPM package contains the following parts:

-   GPG signature

    The GPG signature is used to verify the integrity of the package.

-   Header (package metadata)

    The RPM package manager uses this metadata to determine package dependencies, where to install files, and other information.

-   Payload

    The payload is a `cpio`{.literal} archive that contains files to install to the system.

There are two types of RPM packages. Both types share the file format and tooling, but have different contents and serve different purposes:

-   Source RPM (SRPM)

    An SRPM contains source code and a `spec`{.literal} file, which describes how to build the source code into a binary RPM. Optionally, the SRPM can contain patches to source code.

-   Binary RPM

    A binary RPM contains the binaries built from the sources and patches.

### [1.2. Listing RPM packaging utilities](#listing-rpm-packaging-utilities) {#listing-rpm-packaging-utilities .title}

In addition to the `rpmbuild(8)`{.literal} program for building packages, RPM provides other utilities to make the process of creating packages on Red Hat Enterprise Linux (RHEL) easier.

**Prerequisites**

-   The `rpmdevtools`{.literal} package has been installed:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rpmdevtools
    ```

**Procedure**

-   Use one of the following methods to list RPM packaging utilities:

    -   To list certain utilities provided by the `rpmdevtools`{.literal} package and their short descriptions, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ rpm -qi rpmdevtools
        ```

    -   To list all utilities, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ rpm -ql rpmdevtools | grep ^/usr/bin
        ```

## [Chapter 2. Setting up RPM packaging workspace](#setting-up-rpm-packaging-workspace) {#chapter-2.-setting-up-rpm-packaging-workspace .title}

To build RPM packages, you must first create a special workspace that consists of directories used for different packaging purposes.

### [2.1. Configuring RPM packaging workspace](#configuring-rpm-packaging-workspace) {#configuring-rpm-packaging-workspace .title}

Prepare your environment for software packaging by configuring an RPM packaging workspace.

To configure the RPM packaging workspace, set up a directory layout by using the `rpmdev-setuptree`{.literal} utility.

**Prerequisites**

-   You installed the `rpmdevtools`{.literal} package, which provides utilities for packaging RPMs:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rpmdevtools
    ```

**Procedure**

1.  Run the `rpmdev-setuptree`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    $ rpmdev-setuptree
    ```

2.  Configure packaging workspace directories:

    ``` {.language-plaintext tabindex="-1"}
    $ tree ~/rpmbuild/
    ```

    ``` {.language-plaintext tabindex="-1"}
    /home/user/rpmbuild/
    |-- BUILD
    |-- RPMS
    |-- SOURCES
    |-- SPECS
    `-- SRPMS

    5 directories, 0 files
    ```

**Additional resources**

-   [RPM packaging workspace directories](#rpm-packaging-workspace-directories "2.2. RPM packaging workspace directories")

### [2.2. RPM packaging workspace directories](#rpm-packaging-workspace-directories) {#rpm-packaging-workspace-directories .title}

Review the following directories that the `rpmdev-setuptree`{.literal} utility creates to configure the RPM packaging workspace.

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Directory                         | Purpose                                                                                                                                                                                |
+:==================================+:=======================================================================================================================================================================================+
| `BUILD`{.literal}                 | Contains build artifacts compiled from the source files from the `SOURCES`{.literal} directory.                                                                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `RPMS`{.literal}                  | Binary RPMs are created under the `RPMS`{.literal} directory in subdirectories for different architectures. For example, in the `x86_64`{.literal} or `noarch`{.literal} subdirectory. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `SOURCES`{.literal}               | Contains compressed source code archives and patches. The `rpmbuild`{.literal} command then searches for these archives and patches in this directory.                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `SPECS`{.literal}                 | Contains `spec`{.literal} files created by the packager. These files are then used for building packages.                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `SRPMS`{.literal}                 | When you use the `rpmbuild`{.literal} command to build an SRPM instead of a binary RPM, the resulting SRPM is created under this directory.                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 2.1. RPM packaging workspace directories

Show more

## [Chapter 3. RPM macros](#rpm-macros) {#chapter-3.-rpm-macros .title}

An RPM macro is a straight text substitution that, in addition to simple literal substitution, can perform various string operations, evaluate expressions, interact with the operating system (OS), and other actions.

### [3.1. Displaying the built-in RPM macros](#displaying-the-built-in-rpm-macros) {#displaying-the-built-in-rpm-macros .title}

Display the list of built-in RPM macros on your Red Hat Enterprise Linux (RHEL) system. RPM provides multiple built-in macros that you can use to simplify package maintenance and make it consistent across packages.

**Procedure**

-   Display the built-in RPM macros:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm --showrc|grep "<builtin>”
    ```

### [3.2. Displaying RPM distribution macros](#displaying-rpm-distribution-macros) {#displaying-rpm-distribution-macros .title}

Display the RPM distribution macros for your Red Hat Enterprise Linux (RHEL) system.

Different distributions provide distinct sets of recommended RPM macros based on the language implementation of the software being packaged or the specific guidelines of the distribution. The sets of recommended RPM macros are often provided as RPM packages, ready to be installed by using the DNF package manager. You can find the installed macro files in the `/usr/lib/rpm/macros.d/`{.literal} directory.

For more information, see the `rpm`{.literal} man page on your system.

**Procedure**

1.  Display the raw RPM macro definitions:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm --showrc
    ```

2.  Determine what a macro does and how it can be helpful when packaging RPMs:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm --showrc | grep <macro_name>
    ```

3.  Optional: Display information about the RPMs macros for your system version of RPM:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm -ql rpm | grep macros
    ```

### [3.3. Customizing RPM behavior by using macros](#customizing-rpm-behavior-with-macros) {#customizing-rpm-behavior-by-using-macros .title}

Customize RPM behavior by editing the RPM macros.

You can override any macros, except the built-in macros, in the `~/.rpmmacros`{.literal} file with your custom macros. Any changes that you make affect every build on every system sharing the same home directory.

Note

To override macros on a per-machine basis, put these macros in a `/etc/rpm/macros.*`{.literal} file.

Warning

It is not recommended to use new macros that you defined in the `~/.rpmmacros`{.literal} file in packaging. Such macros would not be present on other machines, where users might want to try to rebuild your package.

**Procedure**

-   Customize a macro:

    ``` {.language-plaintext tabindex="-1"}
    %_topdir /opt/<directory>/rpmbuild
    ```

    You can create the *`<directory>`{.literal}*, including all subdirectories, by using the `rpmdev-setuptree`{.literal} utility.

    Note that the value of this macro is by default `~/rpmbuild`{.literal}.

### [3.4. Defining custom RPM macros in a spec file](#defining-custom-macros-in-spec) {#defining-custom-rpm-macros-in-a-spec-file .title}

Define custom RPM macros to simplify package maintenance and make it consistent across packages, in addition to using the built-in and distribution RPM macros. RPM `spec`{.literal} files can use either the `%define`{.literal} and `%global`{.literal} macros.

The differences between the `%define`{.literal} and `%global`{.literal} macros are the following:

-   `%define`{.literal} has global scope, except when used in a parametric macro, where its scope is local to this macro. The body of the `%define`{.literal} macro is expanded when used.
-   `%global`{.literal} has global scope. The body of the `%global`{.literal} macro is expanded at definition time.

Important

Use `%global`{.literal} macros for the following actions:

-   To avoid multiple redundant evaluations
-   To define global macros inside parametric macros

Otherwise, use `%define`{.literal} macros.

The `%define`{.literal} and `%global`{.literal} macro use the `%global `{.literal}*`<name>`{.literal}*` `{.literal}*`<body>`{.literal}* or `%define `{.literal}*`<name>`{.literal}*`[(opts)] `{.literal}*`<body>`{.literal}* pattern:

-   All whitespace, the preceding and succeeding, that surrounds *`<body>`{.literal}* is removed during the macro expansion.

-   The macro name might be composed of alphanumeric characters and the underscore (`_`{.literal}) character.

-   Inclusion of the `(opts)`{.literal} field is optional:

    -   Simple macros do not contain the `(opts)`{.literal} field. In this case, only recursive macro expansion is performed.
    -   Parametric options are function-like macros that accept arguments and possible options. For more details, see the `/usr/share/doc/rpm/macros.md`{.literal} file.

Important

Macros are evaluated and expanded everywhere in the `spec`{.literal} file, even on lines commented by using the hash (`#`{.literal}) and in `spec`{.literal} file sections, such as `%changelog`{.literal}.

To escape macro expansion, you can use the `%dnl`{.literal} macro which comments out everything up to the next new line.

You can also escape macro expansion by placing a second percent sign (`%`{.literal}) in front of the macro, for example `%%{name}`{.literal}.

For more information about macros, see the `/usr/share/doc/rpm/macros.md`{.literal} file.

**Procedure**

-   Define the macro. For example, you can include the following line in the RPM `spec`{.literal} file.

    ``` {.language-plaintext tabindex="-1"}
    %define date 20241114
    %define upstream_version 2.5.4-pre1
    ```

### [3.5. Common RPM directives in the %files section of spec](#rpm-directives-in-the-spec-files-section) {#common-rpm-directives-in-the-files-section-of-spec .title}

Use the following RPM directives in the `%files`{.literal} section of a `spec`{.literal} file.

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Macro                             | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+:==================================+:================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `%license`{.literal}              | The `%license`{.literal} macro identifies the file listed as a license. RPM installs and labels this file as the license, for example, `%license LICENSE`{.literal}.                                                                                                                                                                                                                                                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%doc`{.literal}                  | The `%doc`{.literal} macro identifies a file listed as a documentation file. RPM installs and labels this file as the documentation file, for example, `%doc README`{.literal}.                                                                                                                                                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   | Important                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   | Documentation can be excluded during package installation, for example, to conserve disk space on images. License files might look like documentation files, but they must always be installed with the software. Therefore, you must use the `%license`{.literal} macro instead of `%doc`{.literal} for license files.                                                                                                                                                                         |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   | The `%doc`{.literal} macro is used for documentation about the packaged software, code examples, and various accompanying items. Note that if code examples are included, you must be careful when removing executable mode from the file.                                                                                                                                                                                                                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%dir`{.literal}                  | The `%dir`{.literal} macro ensures that the path is a directory owned by the RPM package. The RPM file manifest then accurately detects which directories to clean up during the uninstall operation.                                                                                                                                                                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   | Example usage:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   | `%dir %{_libdir}/%{name}`{.screen}                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%config(noreplace)`{.literal}    | The `%config(noreplace)`{.literal} macro ensures that the file is a configuration file. This file, therefore, must not be overwritten or replaced during a package installation or update if the file has been modified from the original installation checksum. If there is a change, the file will be created with `.rpmnew`{.literal} appended at the end of the filename upon upgrade or installation. Therefore, the pre-existing or modified file on the target system remains unchanged. |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   | Example usage:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   | `%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf`{.screen}                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 3.1. %files section directives

Show more

**Additional resources**

-   [Body items of a spec file](#spec-body-items "6.1.2. Body items of a spec file")

### [3.6. The %autosetup and %setup macros](#autosetup-and-setup-macros) {#the-autosetup-and-setup-macros .title}

Use the `%autosetup`{.literal} macro to unpack the source archives and apply patches automatically instead of manually specifying each patch by using the `%patch`{.literal} directive.

Important

`%autosetup`{.literal} applies patches in the order they appear in the `spec`{.literal} file. Always consider keeping sources and patches sorted by their number in `spec`{.literal} to avoid unexpected actions. Alternatively, avoid the numbering entirely by using `%patchlist`{.literal} or non-numbered `Patch`{.literal} entries.

You can also use the `%setup`{.literal} macro to unpack the source archives for building RPM packages.

Important

Use the `%autosetup`{.literal} macro whenever possible, instead of the `%setup`{.literal} macro.

#### [3.6.1. The %autosetup macro options](#autosetup-macro-options) {#the-autosetup-macro-options .title}

Use the following `%autosetup`{.literal} macro options to control its behavior. `%autosetup`{.literal} also accepts all `%setup`{.literal} macro options.

Note

You can combine the `%autosetup`{.literal} macro options.

For more information, see the `patch(1)`{.literal} man page on your system.

+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Macro option                           | Description                                                                                                                                                                                            |
+:=======================================+:=======================================================================================================================================================================================================+
| `-v`{.literal}                         | Use the `-v`{.literal} option to enable the verbosity of the `%autosetup`{.literal} macro.                                                                                                             |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-N`{.literal}                         | Use the `-N`{.literal} option to disable automatic patch application.                                                                                                                                  |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-S`{.literal}*`<vcs_name>`{.literal}* | Use the `-S`{.literal}*`<vcs_name>`{.literal}* option to specify the version control system (VCS) to use, for example, `git_am`{.literal}, `git`{.literal}, `patch`{.literal}, or `gendiff`{.literal}. |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-p`{.literal}                         | Use the `-p`{.literal} option to control patch prefix stripping. For more information, see the `patch(1)`{.literal} man page on your system.                                                           |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 3.2. The %autosetup macro options

Show more

#### [3.6.2. The %autopatch macro options](#autopatch-macro-options) {#the-autopatch-macro-options .title}

The `%autopatch`{.literal} macro applies all patches in the order stated in a `spec`{.literal} file. Use the following `%autopatch`{.literal} macro options to control its behavior.

Note

You can combine the `%autopatch`{.literal} macro options.

For more information, see the `patch(1)`{.literal} man page on your system.

+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Macro option                                | Description                                                                                                                                  |
+:============================================+:=============================================================================================================================================+
| `-v`{.literal}                              | Use the `-v`{.literal} option to enable the verbosity of the `%autopatch`{.literal} macro.                                                   |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| `-p`{.literal}                              | Use the `-p`{.literal} option to control patch prefix stripping. For more information, see the `patch(1)`{.literal} man page on your system. |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| `-m`{.literal}*`<patch_number>`{.literal}*  | Use the `-m`{.literal}*`<patch_number>`{.literal}* option to apply a range of patches starting from the specified patch number.              |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| `-M`{.literal}*`<patch_number`{.literal}*\> | Use the `-M`{.literal}*`<patch_number`{.literal}*`>`{.literal} to apply a range of patches up to the specified patch number.                 |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

: Table 3.3. The %autopatch macro options

Show more

#### [3.6.3. The %setup macro options](#setup-macro-options) {#the-setup-macro-options .title}

Use the following `%setup`{.literal} macro options for controlling the unpacking of source archives.

Note

You can combine the `%setup`{.literal} macro options.

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Macro option                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+:==================================+:============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `-q`{.literal}                    | Use the `-q`{.literal} option to limit the verbosity of the `%setup`{.literal} macro. Pass this option as the first option to the `%setup`{.literal} macro.                                                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-n`{.literal}                    | Use the `-n`{.literal} option to specify the name of the directory from an expanded source code archive.                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | For example, you can use this option when the directory from the expanded source code archive has a different name from what is expected (`%{`{.literal}*`<name>`{.literal}*`}-%{`{.literal}*`<version>`{.literal}*`` }), which can lead to an error of the `%setup ``{.literal} macro. For example, if the package name is `cello`{.literal}, but the source code archive name is `hello-1.0.tgz`{.literal}, and it contains the `hello/`{.literal} directory, the `spec`{.literal} file must have the following contents: |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | `Name: cello Source0: https://example.com/%{name}/release/hello-%{version}.tar.gz ... %prep %setup -n hello`{.screen}                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-c`{.literal}                    | Use the `-c`{.literal} option to create a directory and then change to this directory before unpacking any sources, for example:                                                                                                                                                                                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | `/usr/bin/mkdir -p cello-1.0 cd 'cello-1.0'`{.screen}                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | The directory is not changed after archive expansion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-D`{.literal}                    | Use the `-D`{.literal} option to disable deletion of the source code directory. You can use this option, for example, if the `%setup`{.literal} macro is used several times. With the `-D`{.literal} option, the following lines are not used:                                                                                                                                                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | `rm -rf 'cello-1.0'`{.screen}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-T`{.literal}                    | Use the `-T`{.literal} option to skip the default action of the `%setup`{.literal} macro, which includes unpacking of the first source archive. This option removes the following line from the script:                                                                                                                                                                                                                                                                                                                     |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | `/usr/bin/gzip -dc '/builddir/build/SOURCES/cello-1.0.tar.gz' | /usr/bin/tar -xvvof -`{.screen}                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-b`{.literal}                    | Use the `-b`{.literal} (before) option to expand specific sources before entering the working directory.                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | For example, examples are provided in a separate `cello-1.0-examples.tar.gz`{.literal} archive, which expands into `cello-1.0/examples`{.literal}. In this case, use `-b 1`{.literal} to expand `Source1`{.literal} before entering the working directory:                                                                                                                                                                                                                                                                  |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | `Source0: https://example.com/%{name}/release/%{name}-%{version}.tar.gz Source1: %{name}-%{version}-examples.tar.gz ... %prep %setup -b 1`{.screen}                                                                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-a`{.literal}                    | Use the `-a`{.literal} (after) to expand specific sources after entering the working directory. The argument is a source number from the `spec`{.literal} file preamble section.                                                                                                                                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | For example, the `cello-1.0.tar.gz`{.literal} archive contains an empty `examples`{.literal} directory. The examples are shipped in a separate `examples.tar.gz`{.literal} archive, and they expand into the directory with the same name. In this case, use `-a 1`{.literal} to expand `Source1`{.literal} after entering the working directory:                                                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | `Source0: https://example.com/%{name}/release/%{name}-%{version}.tar.gz Source1: examples.tar.gz ... %prep %setup -a 1`{.screen}                                                                                                                                                                                                                                                                                                                                                                                            |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 3.4. The %setup macro options

Show more

## [Chapter 4. Creating software for RPM packaging](#creating-software-for-rpm-packaging) {#chapter-4.-creating-software-for-rpm-packaging .title}

Prepare your software source code for RPM packaging on Red Hat Enterprise Linux (RHEL).

### [4.1. What is source code](#what-is-source-code) {#what-is-source-code .title}

Source code is human-readable instructions to the computer that describe how to perform a computation. Source code is expressed by using a programming language.

The following versions of the `Hello World`{.literal} program written in three different programming languages cover major RPM Package Manager use cases:

-   `Hello World`{.literal} written in Bash

    The *bello* project implements `Hello World`{.literal} in Bash. The implementation contains only the `bello`{.literal} shell script. The purpose of this program is to output `Hello World`{.literal} on the command line.

    The `bello`{.literal} file has the following contents:

    ``` {.language-plaintext tabindex="-1"}
    #!/bin/bash

    printf "Hello World\n"
    ```

-   `Hello World`{.literal} written in Python

    The *pello* project implements `Hello World`{.literal} in Python. The implementation contains only the `pello.py`{.literal} program. The purpose of the program is to output `Hello World`{.literal} on the command line.

    The `pello.py`{.literal} file has the following contents:

    ``` {.language-plaintext tabindex="-1"}
    #!/usr/bin/python3

    print("Hello World")
    ```

-   `Hello World`{.literal} written in C

    The *cello* project implements `Hello World`{.literal} in C. The implementation contains only the `cello.c`{.literal} and `Makefile`{.literal} files. The resulting `tar.gz`{.literal} archive therefore has two files in addition to the `LICENSE`{.literal} file. The purpose of the program is to output `Hello World`{.literal} on the command line.

    The `cello.c`{.literal} file has the following contents:

    ``` {.language-plaintext tabindex="-1"}
    #include <stdio.h>

    int main(void) {
        printf("Hello World\n");
        return 0;
    }
    ```

Note

The packaging process is different for each version of the `Hello World`{.literal} program.

### [4.2. Methods of creating software](#methods-of-creating-software) {#methods-of-creating-software .title}

You can convert the human-readable source code into machine code by natively compiling or interpreting software.

#### [4.2.1. Natively compiled software](#natively-compiled-software) {#natively-compiled-software .title}

Natively compiled software is software written in a programming language that compiles to machine code with a resulting binary executable file. Natively compiled software is standalone software.

Note

Natively compiled RPM packages are architecture-specific.

If you compile such software on a computer that uses a 64-bit (x86_64) AMD or Intel processor, it does not run on a 32-bit (x86) AMD or Intel processor. The resulting package has the architecture specified in its name.

#### [4.2.2. Interpreted software](#interpreted-software) {#interpreted-software .title}

Some programming languages, such as Bash or Python, do not compile to machine code. Instead, a language interpreter or a language virtual machine executes the programs\' source code step-by-step without prior transformations.

Note

Software written entirely in interpreted programming languages is not architecture-specific. Therefore, the resulting RPM package has the `noarch`{.literal} string in its name.

You can either raw-interpret or byte-compile software written in interpreted languages:

-   Raw-interpreted software

    You do not need to compile this type of software. Raw-interpreted software is directly executed by the interpreter.

-   Byte-compiled software

    You must first compile this type of software into bytecode, which is then executed by the language virtual machine.

    Note

    Some byte-compiled languages can be either raw-interpreted or byte-compiled.

Note that the way you build and package software by using RPM is different for these two software types.

### [4.3. Building software from source](#building-software-from-source) {#building-software-from-source .title}

Build software written in compiled languages from source code into executable software artifacts.

#### [4.3.1. Building software from natively compiled code](#building-software-from-natively-compiled-code) {#building-software-from-natively-compiled-code .title}

Build software written in a compiled language into an executable by using manual or automated building.

##### [4.3.1.1. Manually building a sample C program](#manually-building-a-sample-c-program) {#manually-building-a-sample-c-program .title}

Manually build software written in a compiled language.

A sample `Hello World`{.literal} program written in C (`cello.c`{.literal}) has the following contents:

``` {.language-plaintext tabindex="-1"}
#include <stdio.h>

int main(void) {
    printf("Hello World\n");
    return 0;
}
```

**Procedure**

1.  Invoke the C compiler from the GNU Compiler Collection to compile the source code into binary:

    ``` {.language-plaintext tabindex="-1"}
    $ gcc -g -o cello cello.c
    ```

2.  Run the resulting binary `cello`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ./cello
    ```

    ``` {.language-plaintext tabindex="-1"}
    Hello World
    ```

##### [4.3.1.2. Setting automated building for a sample C program](#setting-automated-building-for-a-sample-c-program) {#setting-automated-building-for-a-sample-c-program .title}

In practice, all software uses automated building. Configure automated building by creating the `Makefile`{.literal} file and then running the GNU `make`{.literal} utility.

**Procedure**

1.  Create the `Makefile`{.literal} file with the following content in the same directory as `cello.c`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    cello:
        gcc -g -o cello cello.c
    clean:
        rm cello
    ```

    Note that the lines under `cello:`{.literal} and `clean:`{.literal} must begin with a tabulation character (tab).

2.  Build the software:

    ``` {.language-plaintext tabindex="-1"}
    $ make
    ```

    ``` {.language-plaintext tabindex="-1"}
    make: 'cello' is up to date.
    ```

3.  Because a build is already available in the current directory, repeat the following steps:

    a.  Enter the `make clean`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        $ make clean
        ```

        ``` {.language-plaintext tabindex="-1"}
        rm cello
        ```

    b.  Enter the `make`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        $ make
        ```

        ``` {.language-plaintext tabindex="-1"}
        gcc -g -o cello cello.c
        ```

        Note that trying to build the program again at this point has no effect because the GNU `make`{.literal} system detects the existing binary:

        ``` {.language-plaintext tabindex="-1"}
        $ make
        ```

        ``` {.language-plaintext tabindex="-1"}
        make: 'cello' is up to date.
        ```

4.  Run the program:

    ``` {.language-plaintext tabindex="-1"}
    $ ./cello
    ```

    ``` {.language-plaintext tabindex="-1"}
    Hello World
    ```

#### [4.3.2. Interpreting source code](#interpreting-source-code) {#interpreting-source-code .title}

Byte-compile a source code written in a compiled language and make a source code written in a shell scripting language directly executable.

Byte-compiling

:   The procedure for byte-compiling software varies depending on the following factors:

    -   Programming language
    -   Language's virtual machine
    -   Tools and processes used with that language

    Note

    You can byte-compile software written, for example, in Python. Python software intended for distribution is often byte-compiled, but not in the way described in this document. The described procedure aims not to conform to the community standards, but to be simple.

    You can also raw-interpret Python source code. However, the byte-compiled version is faster. Therefore, RPM packagers prefer to package the byte-compiled version for distribution to end users.

Raw-interpreting
:   Software written in shell scripting languages, such as Bash, is always executed by raw-interpreting.

##### [4.3.2.1. Byte-compiling a sample Python program](#byte-compiling-a-sample-python-program) {#byte-compiling-a-sample-python-program .title}

Byte-compile a sample Python source code to improve software performance. Python code can also be raw-interpreted, but byte-compiled code runs faster.

By choosing byte-compiling over raw-interpreting of Python source code, you can create faster software.

A sample `Hello World`{.literal} program written in the Python programming language (`pello.py`{.literal}) has the following contents:

``` {.language-plaintext tabindex="-1"}
print("Hello World")
```

**Procedure**

1.  Byte-compile the `pello.py`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ python -m compileall pello.py
    ```

2.  Verify that a byte-compiled version of the file is created:

    ``` {.language-plaintext tabindex="-1"}
    $ ls pass:[pycache]
    ```

    ``` {.language-plaintext tabindex="-1"}
    pello.cpython-311.pyc
    ```

    Note that the package version in the output might differ depending on which Python version is installed.

3.  Run the program in `pello.py`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ python pello.py
    ```

    ``` {.language-plaintext tabindex="-1"}
    Hello World
    ```

##### [4.3.2.2. Raw-interpreting a sample Bash program](#raw-interpreting-a-sample-bash-program) {#raw-interpreting-a-sample-bash-program .title}

Make a Bash source code directly executable.

A sample `Hello World`{.literal} program written in Bash shell built-in language (`bello`{.literal}) has the following contents:

``` {.language-plaintext tabindex="-1"}
#!/bin/bash

printf "Hello World\n"
```

Note

The **shebang** (`#!`{.literal}) sign at the top of the `bello`{.literal} file is not part of the programming language source code.

Use the **shebang** to turn a text file into an executable. The system program loader parses the line containing the **shebang** to get a path to the binary executable, which is then used as the programming language interpreter.

**Procedure**

1.  Make the file with source code executable:

    ``` {.language-plaintext tabindex="-1"}
    $ chmod +x bello
    ```

2.  Run the created file:

    ``` {.language-plaintext tabindex="-1"}
    $ ./bello
    ```

    ``` {.language-plaintext tabindex="-1"}
    Hello World
    ```

## [Chapter 5. Preparing software for RPM packaging](#preparing-software-for-rpm-packaging) {#chapter-5.-preparing-software-for-rpm-packaging .title}

To prepare a piece of software for packaging with RPM, you can first patch the software, create a `LICENSE`{.literal} file for it, and archive it as a tarball.

### [5.1. Patching software](#patching-software) {#patching-software .title}

When packaging software, you might need to make certain changes to the original source code, such as fixing a bug or changing a configuration file. In RPM packaging, you can instead leave the original source code intact and apply patches on it.

A patch is a piece of text that updates a source code file. The patch has a *diff* format, because it represents the difference between two versions of the text. You can create a patch by using the `diff`{.literal} utility, and then apply the patch to the source code by using the `patch`{.literal} utility.

Note

Software developers often use version control systems such as Git to manage their code base. Such tools offer their own methods of creating diffs or patching software.

#### [5.1.1. Creating a patch file for a sample C program](#creating-a-patch-file-sample-c) {#creating-a-patch-file-for-a-sample-c-program .title}

Create a patch from the original source code of a sample `Hello world`{.literal} program written in C (`cello.c`{.literal}) by using the `diff`{.literal} utility. You can then apply this patch to make changes to the packaged software without making changes to the original source code.

**Prerequisites**

-   You installed the `diff`{.literal} utility on your system:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install diffutils
    ```

**Procedure**

1.  Back up the original source code:

    ``` {.language-plaintext tabindex="-1"}
    $ cp -p cello.c cello.c.orig
    ```

    The `-p`{.literal .option} option preserves mode, ownership, and timestamps.

2.  Modify `cello.c`{.literal} as needed:

    ``` {.language-plaintext tabindex="-1"}
    #include <stdio.h>

    int main(void) {
        printf("Hello World from my very first patch!\n");
        return 0;
    }
    ```

3.  Generate a patch:

    ``` {.language-plaintext tabindex="-1"}
    $ diff -Naur cello.c.orig cello.c
    ```

    ``` {.language-plaintext tabindex="-1"}
    --- cello.c.orig        2016-05-26 17:21:30.478523360 -0500
    +++ cello.c     2016-05-27 14:53:20.668588245 -0500
    @@ -1,6 +1,6 @@
     #include<stdio.h>

     int main(void){
    -    printf("Hello World!\n");
    +    printf("Hello World from my very first patch!\n");
         return 0;
     }
    \ No newline at end of file
    ```

    Lines that start with `+`{.literal} replace the lines that start with `-`{.literal}.

    Note

    Using the `Naur`{.literal .option} options with the `diff`{.literal .command} command is recommended because it fits the majority of use cases:

    -   `-N`{.literal .option} (`--new-file`{.literal .option})

        The `-N`{.literal .option} option handles absent files as empty files.

    -   `-a`{.literal .option} (`--text`{.literal .option})

        The `-a`{.literal .option} option treats all files as text. As a result, the `diff`{.literal .command} utility does not ignore the files it classified as binaries.

    -   `-u`{.literal .option} (`-U NUM`{.literal .option} or `--unified[=NUM]`{.literal .option})

        The `-u`{.literal .option} option returns output in the form of output NUM (default 3) lines of unified context. This is a compact and an easily readable format commonly used in patch files.

    -   `-r`{.literal .option} (`--recursive`{.literal .option})

        The `-r`{.literal .option} option recursively compares any subdirectories that the `diff`{.literal} utility found.

    However, note that in this particular case, only the `-u`{.literal} option is necessary.

4.  Save the patch to a file:

    ``` {.language-plaintext tabindex="-1"}
    $ diff -Naur cello.c.orig cello.c > cello.patch
    ```

5.  Restore the original `cello.c`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ mv cello.c.orig cello.c
    ```

    Important

    You must retain the original `cello.c`{.literal} because the RPM package manager uses the original file, not the modified one, when building an RPM package. For more information, see [Working with spec files](#working-with-spec-files "6.4. Working with spec files").

#### [5.1.2. Patching a sample C program](#patching-sample-c) {#patching-a-sample-c-program .title}

Apply code patches to a sample `Hello world`{.literal} program written in C (`cello.c`{.literal}) by using the `patch`{.literal} utility.

**Prerequisites**

-   You installed the `patch`{.literal} utility on your system:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install patch
    ```

-   You created a patch from the original source code. For instructions, see [Creating a patch file for a sample C program](#creating-a-patch-file-sample-c "5.1.1. Creating a patch file for a sample C program").

**Procedure**

1.  Redirect the patch file to the `patch`{.literal .command} command:

    ``` {.language-plaintext tabindex="-1"}
    $ patch < cello.patch
    ```

    ``` {.language-plaintext tabindex="-1"}
    patching file cello.c
    ```

2.  Check that the contents of `cello.c`{.literal} now reflect the change:

    ``` {.language-plaintext tabindex="-1"}
    $ cat cello.c
    ```

    ``` {.language-plaintext tabindex="-1"}
    #include<stdio.h>

    int main(void){
        printf("Hello World from my very first patch!\n");
        return 1;
    }
    ```

**Verification**

1.  Build the patched `cello.c`{.literal} program:

    ``` {.language-plaintext tabindex="-1"}
    $ make
    ```

    ``` {.language-plaintext tabindex="-1"}
    gcc -g -o cello cello.c
    ```

2.  Run the built `cello.c`{.literal} program:

    ``` {.language-plaintext tabindex="-1"}
    $ ./cello
    ```

    ``` {.language-plaintext tabindex="-1"}
    Hello World from my very first patch!
    ```

### [5.2. Creating a LICENSE file](#creating-a-license-file) {#creating-a-license-file .title}

To enable appropriate software usage, create a license file containing the necessary copyright and legal information for your RPM package. For packaging purposes, you must also supply the license file with the software you are packaging.

It is recommended that you distribute your software with a software license. The software license file informs users of what they can and cannot do with a source code. Having no license for your source code means that you retain all rights to this code and no one can reproduce, distribute, or create derivative works from your source code.

**Procedure**

-   Create the `LICENSE`{.literal} file with the required license statement:

    ``` {.language-plaintext tabindex="-1"}
    $ vim LICENSE
    ```

    For example, the GPLv3 `LICENSE`{.literal} file has the following text:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /tmp/LICENSE
    ```

    ``` {.language-plaintext tabindex="-1"}
    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with this program. If not, see \http://www.gnu.org/licenses/.
    ```

**Additional resources**

-   [Source code examples](https://github.com/redhat-developer/rpm-packaging-guide/tree/master/example-code)

### [5.3. Creating a source code archive for distribution](#creating-a-source-code-archive-for-distribution) {#creating-a-source-code-archive-for-distribution .title}

To prepare your software for distribution, put your source code and necessary components into an archive file.

An archive file is a file with the `.tar.gz`{.literal} or `.tgz`{.literal} suffix. Putting source code into the archive is a common way to release the software to be later packaged for distribution.

#### [5.3.1. Creating a source code archive for a sample Bash program](#creating-an-archive-for-sample-bash) {#creating-a-source-code-archive-for-a-sample-bash-program .title}

To prepare a sample Bash program for distribution, put the source code and necessary components into an archive file.

The *bello* project is a `Hello World`{.literal} file in Bash. The following example contains only the `bello`{.literal} shell script. Therefore, the resulting `tar.gz`{.literal} archive has only one file in addition to the `LICENSE`{.literal} file.

Note

The `patch`{.literal} file is not distributed in the archive with the program. The RPM package manager applies the patch when the RPM is built. The patch will be placed into the `~/rpmbuild/SOURCES/`{.literal} directory together with the `tar.gz`{.literal} archive.

**Prerequisites**

-   Assume that the `0.1`{.literal} version of the `bello`{.literal} program is used.
-   You created a `LICENSE`{.literal} file. For instructions, see [Creating a LICENSE file](#creating-a-license-file "5.2. Creating a LICENSE file").

**Procedure**

1.  Move all required files into a single directory:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir bello-0.1
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ mv ~/bello bello-0.1/
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ mv LICENSE bello-0.1/
    ```

2.  Create the archive for distribution:

    ``` {.language-plaintext tabindex="-1"}
    $ tar -cvzf bello-0.1.tar.gz bello-0.1
    ```

    ``` {.language-plaintext tabindex="-1"}
    bello-0.1/
    bello-0.1/LICENSE
    bello-0.1/bello
    ```

3.  Move the created archive to the `~/rpmbuild/SOURCES/`{.literal} directory, which is the default directory where the `rpmbuild`{.literal} command stores the files for building packages:

    ``` {.language-plaintext tabindex="-1"}
    $ mv bello-0.1.tar.gz ~/rpmbuild/SOURCES/
    ```

**Additional resources**

-   [Hello World written in Bash](#hello-world-bash)

#### [5.3.2. Creating a source code archive for a sample Python program](#creating-an-archive-for-sample-python) {#creating-a-source-code-archive-for-a-sample-python-program .title}

To prepare a sample Python program for distribution, put the source code and necessary components into an archive file.

The *pello* project is a `Hello World`{.literal} file in Python. The following example contains only the `pello.py`{.literal} program. Therefore, the resulting `tar.gz`{.literal} archive has only one file in addition to the `LICENSE`{.literal} file.

Note

The `patch`{.literal} file is not distributed in the archive with the program. The RPM package manager applies the patch when the RPM is built. The patch will be placed into the `~/rpmbuild/SOURCES/`{.literal} directory together with the `tar.gz`{.literal} archive.

**Prerequisites**

-   Assume that the `0.1.1`{.literal} version of the `pello`{.literal} program is used.
-   You created a `LICENSE`{.literal} file. For instructions, see [Creating a LICENSE file](#creating-a-license-file "5.2. Creating a LICENSE file").

**Procedure**

1.  Move all required files into a single directory:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir pello-0.1.1
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ mv pello.py pello-0.1.1/
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ mv LICENSE pello-0.1.1/
    ```

2.  Create the archive for distribution:

    ``` {.language-plaintext tabindex="-1"}
    $ tar -cvzf pello-0.1.1.tar.gz pello-0.1.1
    ```

    ``` {.language-plaintext tabindex="-1"}
    pello-0.1.1/
    pello-0.1.1/LICENSE
    pello-0.1.1/pello.py
    ```

3.  Move the created archive to the `~/rpmbuild/SOURCES/`{.literal} directory, which is the default directory where the `rpmbuild`{.literal} command stores the files for building packages:

    ``` {.language-plaintext tabindex="-1"}
    $ mv pello-0.1.1.tar.gz ~/rpmbuild/SOURCES/
    ```

**Additional resources**

-   [Hello World written in Python](#hello-world-python)

#### [5.3.3. Creating a source code archive for a sample C program](#creating-an-archive-for-sample-c) {#creating-a-source-code-archive-for-a-sample-c-program .title}

To prepare a sample C program for distribution, put the source code and necessary components into an archive file.

The *cello* project is a `Hello World`{.literal} file in C. The following example contains only the `cello.c`{.literal} and the `Makefile`{.literal} files. Therefore, the resulting `tar.gz`{.literal} archive has two files in addition to the `LICENSE`{.literal} file.

Note

The `patch`{.literal} file is not distributed in the archive with the program. The RPM package manager applies the patch when the RPM is built. The patch will be placed into the `~/rpmbuild/SOURCES/`{.literal} directory together with the `tar.gz`{.literal} archive.

**Prerequisites**

-   Assume that the `1.0`{.literal} version of the `cello`{.literal} program is used.
-   You created a `LICENSE`{.literal} file. For instructions, see [Creating a LICENSE file](#creating-a-license-file "5.2. Creating a LICENSE file").

**Procedure**

1.  Move all required files into a single directory:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir cello-1.0
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ mv cello.c cello-1.0/
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ mv Makefile cello-1.0/
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ mv LICENSE cello-1.0/
    ```

2.  Create the archive for distribution:

    ``` {.language-plaintext tabindex="-1"}
    $ tar -cvzf cello-1.0.tar.gz cello-1.0
    ```

    ``` {.language-plaintext tabindex="-1"}
    cello-1.0/
    cello-1.0/Makefile
    cello-1.0/cello.c
    cello-1.0/LICENSE
    ```

3.  Move the created archive to the `~/rpmbuild/SOURCES/`{.literal} directory, which is the default directory where the `rpmbuild`{.literal} command stores the files for building packages:

    ``` {.language-plaintext tabindex="-1"}
    $ mv cello-1.0.tar.gz ~/rpmbuild/SOURCES/
    ```

**Additional resources**

-   [Hello World written in C](#hello-world-c)

## [Chapter 6. Packaging software with RPM](#packaging-software-with-rpm) {#chapter-6.-packaging-software-with-rpm .title}

Learn the basics of the packaging process with the RPM package manager.

### [6.1. About spec files](#about-spec-files) {#about-spec-files .title}

A `spec`{.literal} file is a file with instructions that the `rpmbuild`{.literal} utility uses to build an RPM package.

The `spec`{.literal} file provides necessary information to the build system by defining instructions in a series of sections. These sections are defined in the *Preamble* and the *Body* part of the `spec`{.literal} file:

-   The *Preamble* section contains a series of metadata items that are used in the *Body* section.
-   The *Body* section represents the main part of the instructions.

#### [6.1.1. Preamble items of a spec file](#spec-preamble-items) {#preamble-items-of-a-spec-file .title}

Use the following directives in the *Preamble* section of the RPM `spec`{.literal} file.

+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Directive                 | Definition                                                                                                                                                                                                                                                                                                                                                                                                         |
+:==========================+:===================================================================================================================================================================================================================================================================================================================================================================================================================+
| `Name`{.literal}          | A base name of the package that must match the `spec`{.literal} file name.                                                                                                                                                                                                                                                                                                                                         |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Version`{.literal}       | An upstream version number of the software.                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Release`{.literal}       | The number of times the version of the package was released.                                                                                                                                                                                                                                                                                                                                                       |
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                           | Set the initial value to `1%{?dist}`{.literal} and increase it with each new release of the package. Reset to `1`{.literal} when a new `Version`{.literal} of the software is built.                                                                                                                                                                                                                               |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Summary`{.literal}       | A brief one-line summary of the package.                                                                                                                                                                                                                                                                                                                                                                           |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `License`{.literal}       | A license of the software being packaged.                                                                                                                                                                                                                                                                                                                                                                          |
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                           | The exact format for how to label the `License`{.literal} in your `spec`{.literal} file varies depending on which RPM-based Linux distribution guidelines you are following, for example, GPLv3+.                                                                                                                                                                                                                  |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `URL`{.literal}           | A full URL for more information about the software, for example, an upstream project website for the software being packaged.                                                                                                                                                                                                                                                                                      |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Source`{.literal}        | A path or URL to the compressed archive of the unpatched upstream source code. This link must point to an accessible and reliable storage of the archive, for example, the upstream page, not the packager's local storage.                                                                                                                                                                                        |
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                           | You can apply the `Source`{.literal} directive either with or without numbers at the end of the directive name. If there is no number given, the number is assigned to the entry internally. You can also give the numbers explicitly, for example, `Source0`{.literal}, `Source1`{.literal}, `Source2`{.literal}, `Source3`{.literal}, and so on.                                                                 |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Patch`{.literal}         | A name of the first patch to apply to the source code, if necessary.                                                                                                                                                                                                                                                                                                                                               |
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                           | You can apply the `Patch`{.literal} directive either with or without numbers at the end of the directive name. If there is no number given, the number is assigned to the entry internally. You can also give the numbers explicitly, for example, `Patch0`{.literal}, `Patch1`{.literal}, `Patch2`{.literal}, `Patch3`{.literal}, and so on.                                                                      |
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                           | You can apply the patches individually by using the `%patch0`{.literal}, `%patch1`{.literal}, `%patch2`{.literal} macro, and so on. Macros are applied within the `%prep`{.literal} directive in the *Body* section of the RPM `spec`{.literal} file. Alternatively, you can use the `%autopatch`{.literal} macro that automatically applies all patches in the order they are given in the `spec`{.literal} file. |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `BuildArch`{.literal}     | An architecture that the software will be built for.                                                                                                                                                                                                                                                                                                                                                               |
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                           | If the software is not architecture-dependent, for example, if you wrote the software entirely in an interpreted programming language, set the value to `BuildArch: noarch`{.literal}. If you do not set this value, the software automatically inherits the architecture of the machine on which it is built, for example, `x86_64`{.literal}.                                                                    |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `BuildRequires`{.literal} | A comma- or whitespace-separated list of packages required to build the program written in a compiled language. There can be multiple entries of `BuildRequires`{.literal}, each on its own line in the SPEC file.                                                                                                                                                                                                 |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Requires`{.literal}      | A comma- or whitespace-separated list of packages required by the software to run once installed. There can be multiple entries of `Requires`{.literal}, each on its own line in the `spec`{.literal} file.                                                                                                                                                                                                        |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ExcludeArch`{.literal}   | If a piece of software cannot operate on a specific processor architecture, you can exclude this architecture in the `ExcludeArch`{.literal} directive.                                                                                                                                                                                                                                                            |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Conflicts`{.literal}     | A comma- or whitespace-separated list of packages that must not be installed on the system in order for your software to function properly when installed. There can be multiple entries of `Conflicts`{.literal}, each on its own line in the `spec`{.literal} file.                                                                                                                                              |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Obsoletes`{.literal}     | The `Obsoletes`{.literal} directive changes the way updates work depending on the following factors:                                                                                                                                                                                                                                                                                                               |
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                           | -   If you use the `rpm`{.literal} command directly on a command line, it removes all packages that match obsoletes of packages being installed, or the update is performed by an update or dependency solver.                                                                                                                                                                                                     |
|                           | -   If you use the updates or dependency resolver (DNF), packages containing matching `Obsoletes:`{.literal} are added as updates and replace the matching packages.                                                                                                                                                                                                                                               |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Provides`{.literal}      | If you add the `Provides`{.literal} directive to the package, this package can be referred to by dependencies other than its name.                                                                                                                                                                                                                                                                                 |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 6.1. The Preamble section directives

Show more

#### [6.1.2. Body items of a spec file](#spec-body-items) {#body-items-of-a-spec-file .title}

Use the following directives in the *Body* section of the RPM `spec`{.literal} file.

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Directive                | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+:=========================+:=========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `%description`{.literal} | A full description of the software packaged in the RPM. This description can span multiple lines and can be broken into paragraphs.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%prep`{.literal}        | A command or series of commands to prepare the software for building, for example, for unpacking the archive in the `Source`{.literal} directive. The `%prep`{.literal} directive can contain a shell script.                                                                                                                                                                                                                                                                                                                                                                            |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%conf`{.literal}        | A command or series of commands to configure the software for building.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%build`{.literal}       | A command or series of commands for building the software into machine code (for compiled languages) or bytecode (for some interpreted languages).                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%install`{.literal}     | A command or series of commands that the `rpmbuild`{.literal} utility will use to install the software into the `BUILDROOT`{.literal} directory once the software has been built. These commands copy the build artifacts from the `%_builddir`{.literal} directory, where the build happens, to the `%buildroot`{.literal} directory that contains the directory structure with the files to be packaged. This includes copying files from `~/rpmbuild/BUILD`{.literal} to `~/rpmbuild/BUILDROOT`{.literal} and creating the necessary directories in `~/rpmbuild/BUILDROOT`{.literal}. |
|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                          | The `%buildroot`{.literal} directory is an empty base directory, which resembles the end user's system directory layout. In `%buildroot`{.literal}, you can create any directories that will contain the installed files. To create such directories, you can use RPM macros without having to hardcode the paths.                                                                                                                                                                                                                                                                       |
|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                          | Note that `%install`{.literal} is only run when you create a package, not when you install it. For more information, see [Working with spec files](#working-with-spec-files "6.4. Working with spec files").                                                                                                                                                                                                                                                                                                                                                                             |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%check`{.literal}       | A command or series of commands for testing the software, for example, unit tests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%files`{.literal}       | A list of files, provided by the RPM package, to be installed in the user's system and their full path location on the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                          | During the build, if there are files in the `%buildroot`{.literal} directory that are not listed in `%files`{.literal}, you will receive a warning about possible unpackaged files.                                                                                                                                                                                                                                                                                                                                                                                                      |
|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                          | Within the `%files`{.literal} section, you can indicate the role of various files by using built-in macros. This is useful for querying the package file manifest metadata by using the `rpm`{.literal} command. For example, to indicate that the `LICENSE`{.literal} file is a software license file, use the `%license`{.literal} macro.                                                                                                                                                                                                                                              |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%changelog`{.literal}   | A record of changes that happened to the package between different `Version`{.literal} or `Release`{.literal} builds. These changes include a list of date-stamped entries for each Version-Release of the package. These entries log packaging changes, not software changes, for example, adding a patch or changing the build procedure in the `%build`{.literal} section.                                                                                                                                                                                                            |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 6.2. The Body section items

Show more

#### [6.1.3. Advanced spec file items](#spec-advanced-items) {#advanced-spec-file-items .title}

A `spec`{.literal} file can contain advanced items, such as Scriptlets, File triggers, and Triggers. These directives influence not only the `spec`{.literal} file, but also the target operating system on which the resulting RPM is installed by updating the system with information from the RPM.

Scriptlets, File Triggers, and Triggers take effect at different points during the installation process on the target system, not the build process:

-   Scriptlets are unconditionally executed before or after the package is installed or deleted.
-   Triggers are conditionally executed when their specified trigger condition matches other packages on the installed system or in a transaction.
-   File triggers are conditionally executed when their specified path prefix matches other files on the installed system or in a transaction.

##### [6.1.3.1. Scriptlets directives](#spec-scriptlets-directive) {#scriptlets-directives .title}

Scriptlets are arbitrary programs that execute at pre-determined slots related to a package's lifetime, for example, before or after the package is installed or deleted. Use scriptlets only for tasks that cannot be done at build time or in a startup script.

By default, scriptlets are short shell scripts declared by the various `%pre`{.literal} or `%post`{.literal} directives in a `spec`{.literal} file.

Common scriptlet directives are similar to the `spec`{.literal} file section headers, such as `%build`{.literal} or `%install`{.literal}. They are defined by multi-line segments of code, which are often written as a standard `POSIX`{.literal} shell script. However, they can also be written in other programming languages that RPM accepts for the target machine's distribution.

##### [6.1.3.2. Scriptlets directives execution order](#scriptlet-directives-description) {#scriptlets-directives-execution-order .title}

Review the order in which scriptlets are executed during the package upgrade.

+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| Directive                         | Description                                                                                           |
+:==================================+:======================================================================================================+
| `%pretrans`{.literal}             | The `%pretrans`{.literal} scriptlet is executed before installing or removing a package.              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| `%pre`{.literal}                  | The `%pre`{.literal} scriptlet is executed before installing a package on the target system.          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| `%post`{.literal}                 | The `%post`{.literal} scriptlet is executed after a package was installed on the target system.       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| `%preun`{.literal}                | The `%preun`{.literal} scriptlet is executed before uninstalling a package from the target system.    |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| `%postun`{.literal}               | The `%postun`{.literal} scriptlet is executed after a package was uninstalled from the target system. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| `%posttrans`{.literal}            | The `%posttrans`{.literal} scriptlet is executed at the end of a transaction.                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+

: Table 6.3. Scriptlets directives

Show more

##### [6.1.3.3. Turning off scriptlets execution](#turning-off-a-scriptlet-execution) {#turning-off-scriptlets-execution .title}

Turn off the execution of any scriptlet by using the `--no`{.literal} option with the scriptlet name.

Use the `--noscripts`{.literal} option to turn off the execution of all the following scriptlets:

-   `--nopre`{.literal}
-   `--nopost`{.literal}
-   `--nopreun`{.literal}
-   `--nopostun`{.literal}
-   `--nopretrans`{.literal}
-   `--noposttrans`{.literal}
-   `--nopreuntrans`{.literal}
-   `--nopostuntrans`{.literal}

For more information, see the `rpm`{.literal} man page on your system.

**Procedure**

-   Turn off the scriptlet execution:

    ``` {.language-plaintext tabindex="-1"}
    # rpm --no<scriptlet_name>
    ```

    For example, to turn off the execution of the `%pretrans`{.literal} scriptlet, enter:

    ``` {.language-plaintext tabindex="-1"}
    # rpm --nopretrans
    ```

##### [6.1.3.4. Example macros for scriptlets](#scriptlets-macros) {#example-macros-for-scriptlets .title}

The following are example macros that you can use for scriptlets in a `spec`{.literal} file. These macros are real-world macros provided by the `systemd-rpm-macros`{.literal} package. You can use these macros for packaging `systemd`{.literal}-related things. You can also apply similar principles to other packages.

Packages that contain `systemd`{.literal} unit files must use scriptlets to properly handle `systemd`{.literal} services. `systemd`{.literal} packages provide a set of macros to handle `systemd`{.literal} scriptlet operations. For example:

``` {.language-plaintext tabindex="-1"}
%post
%systemd_post httpd.service

%preun
%systemd_preun httpd.service
```

These macros expand to the following in a package:

``` {.language-plaintext tabindex="-1"}
$ rpm --eval "%systemd_preun httpd.service"
```

``` {.language-plaintext tabindex="-1"}
if [ $1 -eq 0 ] && [ -x "/usr/lib/systemd/systemd-update-helper" ]; then
    # Package removal, not upgrade
    /usr/lib/systemd/systemd-update-helper remove-system-units httpd.service || :
fi
```

Note

The way macros behave is subject to change. For example, macros\' behavior can change with a package's development.

#### [6.1.4. The Epoch directive](#spec-epoch-directive) {#the-epoch-directive .title}

If setting the `Version`{.literal} `spec`{.literal} file directive is not enough for comparing package versions, you can use an `Epoch`{.literal} directive. For example, you can use `Epoch`{.literal} to resolve upgrade path issues that occurred because of the upstream change in a version numbering scheme in an incompatible manner.

`Epoch`{.literal} is a numeric field. If you assign a value to `Epoch`{.literal}, it adds a qualifier that RPM uses when comparing package versions. Not having the `Epoch`{.literal} directive listed in a `spec`{.literal} file means `Epoch`{.literal} is not set. This is contrary to the common belief that not setting `Epoch`{.literal} results in an `Epoch`{.literal} of `0`{.literal}. However, for processing purposes, if you do not set `Epoch`{.literal}, RPM treats it the same as if the `Epoch`{.literal} was set to `0`{.literal}, and vice versa.

Important

Using `Epoch`{.literal} in a `spec`{.literal} file is usually omitted because, in the majority of cases, introducing an `Epoch`{.literal} value distorts the expected RPM behavior when comparing versions of packages. Therefore, consider using `Epoch`{.literal} as a last resort.

For example, you installed the `foobar`{.literal} package with `Epoch: 1`{.literal} and `Version: 1.0`{.literal}. Another packager packages `foobar`{.literal} with `Version: 2.0`{.literal}, but without the `Epoch`{.literal} directive. As a result, the new version is never considered an update because the `Epoch`{.literal} version is preferred over the traditional `Name-Version-Release`{.literal} marker that signifies versioning for RPM packages.

#### [6.1.5. Package versioning essentials](#package-naming-essentials) {#package-versioning-essentials .title}

The essential part of the package description is the information defined in the `Name`{.literal}, `Version`{.literal}, and `Release`{.literal} (`NVR`{.literal}) `spec`{.literal} file directives. RPM uses this information to compare package versions and track package dependencies.

When working with RPMs, you can also see mentions of `EVR`{.literal} (`epoch-version-release)`{.literal}, `NEVR`{.literal} (`name-epoch-version-release`{.literal}), and `NEVRA`{.literal} (`name-epoch-version-release-architecture`{.literal}). `EVR`{.literal} is the full version information of the package that RPM always uses for comparison. RPM compares one component at a time, starting from the first component. RPM stops the comparison when it finds a difference in components. For example, if `Epoch`{.literal} differs, RPM does not compare the rest of the `EVR`{.literal} components.

You can display the `NVR`{.literal} information for a specific package by querying the RPM database, for example:

``` {.language-plaintext tabindex="-1"}
# rpm -q bash
bash-4.4.19-7.el8.x86_64
```

Here, `bash`{.literal} is the package name, `4.4.19`{.literal} is the version, and `7.el8`{.literal} is the release. The `x86_64`{.literal} marker is the package architecture. Unlike `NVR`{.literal}, the architecture marker is not under direct control of the RPM packager, but is defined by the `rpmbuild`{.literal} build environment. The exception to this is the architecture-independent `noarch`{.literal} package.

Note

The `rpm -q`{.literal} command displays the package information in the `NEVRA`{.literal} format by default.

**Additional resources**

-   [Preamble items of a spec file](#spec-preamble-items "6.1.1. Preamble items of a spec file")

### [6.2. spec file conditionals](#spec-file-conditionals) {#spec-file-conditionals .title}

Enable conditional inclusion of various sections of the `spec`{.literal} file by using `spec`{.literal} file conditionals.

Conditionals usually deal with the following aspects:

-   Architecture-specific sections.
-   Operating system-specific sections.
-   Compatibility issues between various versions of operating systems.

You can use `spec`{.literal} conditionals for different purposes, for example:

-   Conditional expression (`%if`{.literal}). You can use `%if`{.literal} for multiple purposes. It can have, for example, the following syntax:

    -   "If expression is true, then do some action":

        ``` {.language-plaintext tabindex="-1"}
        %if expression
        ...
        %endif
        ```

    -   "If expression is true, then do some action, otherwise, another action":

        ``` {.language-plaintext tabindex="-1"}
        %if expression
        ...
        %elsif expression
        ...
        %else
        ...
        %endif
        ```

    -   `%if`{.literal} can also be followed by an arbitrary number of `%elif`{.literal} conditionals (nested `%elsif`{.literal}), for example:

        ``` {.language-plaintext tabindex="-1"}
        %if expression
        %elif expression
        ...
        %else
        %endif
        ```

-   System architecture (`%ifarch`{.literal}, `%ifnarch`{.literal}). `%ifarch`{.literal} tests whether the current target system architecture matches. You can use `%ifarch`{.literal} to build RPM packages for multiple platforms, for example:

    ``` {.language-plaintext tabindex="-1"}
    %ifarch s390 s390x
    BuildRequires: s390utils-devel
    %endif
    ```

-   Operating system (`%ifos`{.literal}, `%ifnos`{.literal}). `%ifos`{.literal} controls `spec`{.literal} file processing according to the build target operating system.

#### [6.2.1. Example usage of the %if conditionals](#example-usage-of-the-if-conditionals) {#example-usage-of-the-if-conditionals .title}

Review the following examples that demonstrate how you can use `%if`{.literal} conditionals within your `spec`{.literal} file.

**Example 6.1. Using the %if conditional to handle compatibility between Red Hat Enterprise Linux 10 and other operating systems**

``` {.language-plaintext tabindex="-1"}
%if 0%{?rhel} == 10
sed -i '/AS_FUNCTION_DESCRIBE/ s/^/#/' configure.in
sed -i '/AS_FUNCTION_DESCRIBE/ s/^/#/' acinclude.m4
%endif
```

When building a package on RHEL 10, this conditional comments out `AS_FUNCTION_DESCRIBE`{.literal} lines from `autoconf`{.literal} scripts being considered when the `%rhel`{.literal} macro's value is set to `10`{.literal}.

**Example 6.2. Using the %if conditional to handle definition of macros**

``` {.language-plaintext tabindex="-1"}
%define ruby_archive %{name}-%{ruby_version}
%if 0%{?milestone:1}%{?revision:1} != 0
%define ruby_archive %{ruby_archive}-%{?milestone}%{?!milestone:%{?revision:r%{revision}}}
%endif
```

This conditional handles the definition of macros. If the `%milestone`{.literal} or the `%revision`{.literal} macros are set, the `%ruby_archive`{.literal} macro, which defines the name of the upstream archive, is redefined.

#### [6.2.2. Specialized variants of %if conditionals](#specialized-variants-of-if-conditionals) {#specialized-variants-of-if-conditionals .title}

Review the following specialized `%if`{.literal} conditional statements that you can use within your `spec`{.literal} file to specify system architectures or operating systems.

The specialized variants of the `%if`{.literal} conditionals include the `%ifarch`{.literal}, `%ifnarch`{.literal}, and `%ifos`{.literal} conditionals. These conditionals are commonly used and, therefore, have their own macros.

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Conditional                       | Description                                                                                                                                                                                                                                   |
+:==================================+:==============================================================================================================================================================================================================================================+
| `%ifarch`{.literal}               | Use the `%ifarch`{.literal} conditional to begin a block of the `spec`{.literal} file that is architecture-specific. The conditional is followed by one or more architecture specifiers, each separated by commas or whitespace, for example: |
|                                   |                                                                                                                                                                                                                                               |
|                                   | `%ifarch i386 sparc ... %endif`{.screen}                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                               |
|                                   | All the contents of the `spec`{.literal} file between `%ifarch`{.literal} and `%endif`{.literal} are processed only on the 32-bit AMD and Intel architectures or Sun SPARC-based systems.                                                     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%ifnarch`{.literal}              | The `%ifnarch`{.literal} conditional has a reverse logic than `%ifarch`{.literal} conditional.                                                                                                                                                |
|                                   |                                                                                                                                                                                                                                               |
|                                   | `%ifnarch aarch64 ... %endif`{.screen}                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                                               |
|                                   | All the contents of the `spec`{.literal} file between `%ifnarch`{.literal} and `%endif`{.literal} are processed only if not done on a system with the 64-bit ARM architecture.                                                                |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%ifos`{.literal}                 | Use the `%ifos`{.literal} conditional to control processing based on the operating system of the build. The conditional can be followed by one or more operating system names, for example:                                                   |
|                                   |                                                                                                                                                                                                                                               |
|                                   | `%ifos linux ...​ %endif`{.screen}                                                                                                                                                                                                             |
|                                   |                                                                                                                                                                                                                                               |
|                                   | All the contents of the spec file between `%ifos`{.literal} and `%endif`{.literal} are processed only if the build was done on a Linux system.                                                                                                |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 6.4. Table

Show more

#### [6.2.3. Additional resources](#spec-file-conditionals_623-additional-resources) {#additional-resources .title}

-   [About spec files](#about-spec-files "6.1. About spec files")

### [6.3. BuildRoots](#buildroots) {#buildroots .title}

A `buildroot`{.literal} is a `chroot`{.literal} environment that acts as the `root`{.literal} directory for RPM build artifacts. Structuring these artifacts to match the target hierarchy ensures that the RPM preserves the correct file system layout during installation.

The files in `buildroot`{.literal} are later put into the RPM payload. This payload becomes the main part of the RPM. When the RPM package is installed on the end user's system, these files are extracted in the `root`{.literal} directory, preserving the correct hierarchy.

Note

The `rpmbuild`{.literal} program has its own defaults. Overriding these defaults can cause certain issues. Therefore, avoid defining your own value of the `buildroot`{.literal} macro. Use the default `%{buildroot}`{.literal} macro instead.

### [6.4. Working with spec files](#working-with-spec-files) {#working-with-spec-files .title}

To package new software with RPM, you must create a `spec`{.literal} file.

You can create the `spec`{.literal} file in one of the following ways:

-   Write the new `spec`{.literal} file manually from scratch.
-   Use the `rpmdev-newspec`{.literal} utility. This utility creates an unpopulated `spec`{.literal} file, where you fill the necessary directives and fields.

Note

Some programmer-focused text editors pre-populate a new `spec`{.literal} file with their own `spec`{.literal} template. The `rpmdev-newspec`{.literal} utility provides an editor-agnostic method.

#### [6.4.1. Creating a new spec file for sample Bash, Python, and C programs](#creating-spec-files-for-sample-programs) {#creating-a-new-spec-file-for-sample-bash-python-and-c-programs .title}

Create a `spec`{.literal} file for each of the three sample implementations of the `Hello World!`{.literal} program by using the `rpmdev-newspec`{.literal} utility.

**Prerequisites**

-   The following `Hello World!`{.literal} program implementations were placed into the `~/rpmbuild/SOURCES`{.literal} directory:

    -   [bello-0.1.tar.gz](https://github.com/redhat-developer/rpm-packaging-guide/raw/master/example-code/bello-0.1.tar.gz)
    -   [pello-0.1.2.tar.gz](https://github.com/redhat-developer/rpm-packaging-guide/raw/master/example-code/pello-0.1.2.tar.gz)
    -   [cello-1.0.tar.gz](https://github.com/redhat-developer/rpm-packaging-guide/raw/master/example-code/cello-1.0.tar.gz) ([cello-output-first-patch.patch](https://raw.githubusercontent.com/redhat-developer/rpm-packaging-guide/master/example-code/cello-output-first-patch.patch))

**Procedure**

1.  Navigate to the `~/rpmbuild/SPECS`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/rpmbuild/SPECS
    ```

2.  Create a `spec`{.literal} file for each of the three implementations of the `Hello World!`{.literal} program:

    ``` {.language-plaintext tabindex="-1"}
    $ rpmdev-newspec bello
    ```

    ``` {.language-plaintext tabindex="-1"}
    bello.spec created; type minimal, rpm version >= 4.11.
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ rpmdev-newspec cello
    ```

    ``` {.language-plaintext tabindex="-1"}
    cello.spec created; type minimal, rpm version >= 4.11.
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ rpmdev-newspec pello
    ```

    ``` {.language-plaintext tabindex="-1"}
    pello.spec created; type minimal, rpm version >= 4.11.
    ```

    The `~/rpmbuild/SPECS/`{.literal} directory now contains three `spec`{.literal} files named `bello.spec`{.literal}, `cello.spec`{.literal}, and `pello.spec`{.literal}.

3.  Examine the created files.

    The directives in the files represent those described in [About spec files](#about-spec-files "6.1. About spec files"). In the following sections, you will populate a particular section in the output files of `rpmdev-newspec`{.literal}.

#### [6.4.2. Modifying an original spec file](#modifying-an-original-spec-file) {#modifying-an-original-spec-file .title}

Provide necessary instructions for the `rpmbuild`{.literal} utility by modifying the original output `spec`{.literal} file generated by the `rpmdev-newspec`{.literal} utility. `rpmbuild`{.literal} then uses these instructions to build an RPM package.

**Prerequisites**

-   The unpopulated `~/rpmbuild/SPECS/<name>.spec`{.literal} `spec`{.literal} file was created by using the `rpmdev-newspec`{.literal} utility. For more information, see [Creating a new spec file for sample Bash, Python, and C programs](#creating-spec-files-for-sample-programs "6.4.1. Creating a new spec file for sample Bash, Python, and C programs").

**Procedure**

1.  Open the `~/rpmbuild/SPECS/<name>.spec`{.literal} file provided by the `rpmdev-newspec`{.literal} utility.

2.  Populate the following directives of the `spec`{.literal} file *Preamble* section:

    -   `Name`{.literal}: `Name`{.literal} was already specified as an argument to `rpmdev-newspec`{.literal}.

    -   `Version`{.literal}: Set `Version`{.literal} to match the upstream release version of the source code.

    -   `Release`{.literal}: `Release`{.literal} is automatically set to `1%{?dist}`{.literal}, which is initially `1`{.literal}.

    -   `Summary`{.literal}: Enter a one-line explanation of the package.

    -   `License`{.literal}: Enter the software license associated with the source code.

    -   `URL`{.literal}: Enter the URL to the upstream software website. For consistency, use the `%{name}`{.literal} RPM macro variable and the `https://example.com/%{name}`{.literal} format.

    -   `Source`{.literal}: Enter the URL to the upstream software source code. Link directly to the software version being packaged.

        Note

        The example URLs in this documentation include hard-coded values that could possibly change in the future. Similarly, the release version can change as well. To simplify these potential future changes, use the `%{name}`{.literal} and `%{version}`{.literal} macros. By using these macros, you need to update only one field in the `spec`{.literal} file.

    -   `BuildRequires`{.literal}: Specify build-time dependencies for the package.

    -   `Requires`{.literal}: Specify run-time dependencies for the package.

    -   `BuildArch`{.literal}: Specify the software architecture.

3.  Populate the following directives of the `spec`{.literal} file *Body* section. You can think of these directives as section headings, because these directives can define multi-line, multi-instruction, or scripted tasks to occur.

    -   `%description`{.literal}: Enter the full description of the software.

    -   `%prep`{.literal}: Enter a command or series of commands to prepare software for building.

    -   `%conf`{.literal}: Enter a command or series of commands to configure software for building.

    -   `%build`{.literal}: Enter a command or series of commands for building software.

    -   `%install`{.literal}: Enter a command or series of commands that instruct the `rpmbuild`{.literal} command on how to install the software into the `BUILDROOT`{.literal} directory.

    -   `%files`{.literal}: Specify the list of files, provided by the RPM package, to be installed on your system.

    -   `%changelog`{.literal}: Enter the list of datestamped entries for each `Version-Release`{.literal} of the package.

        Start the first line of the `%changelog`{.literal} section with an asterisk (`*`{.literal}) character followed by `Day-of-Week Month Day Year Name Surname <email> - Version-Release`{.literal}.

        For the actual change entry, follow these rules:

        -   Each change entry can contain multiple items, one for each change.
        -   Each item starts on a new line.
        -   Each item begins with a hyphen (`-`{.literal}) character.

**Additional resources**

-   [Preamble items of a spec file](#spec-preamble-items "6.1.1. Preamble items of a spec file")
-   [Body items of a spec file](#spec-body-items "6.1.2. Body items of a spec file")

#### [6.4.3. An example spec file for a sample Bash program](#example-spec-for-sample-bash) {#an-example-spec-file-for-a-sample-bash-program .title}

Review the following annotated example `spec`{.literal} file for a sample program written in the Bash programming language (`bello`{.literal}).

To install `bello`{.literal}, you must create the destination directory and install the executable `bash`{.literal} script file there. Therefore, you can use the `install`{.literal} command in the `%install`{.literal} section. You can use RPM macros to do this without hardcoding paths.

**Example 6.3. An example spec file for the bello program**

``` {.language-plaintext tabindex="-1"}
Name:           bello
Version:        0.1
Release:        1%{?dist}
Summary:        Hello World example implemented in bash script

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

Requires:       bash

BuildArch:      noarch

%description
The long-tail description for our Hello World Example implemented in
bash script.

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org> - 0.1-1
- First bello package
- Example second item in the changelog for version-release 0.1-1
```

-   The `BuildRequires`{.literal} directive, which specifies build-time dependencies for the package, was deleted because there is no building step for `bello`{.literal}. Bash is a raw interpreted programming language, and the files are just installed to their location on the system.
-   The `Requires`{.literal} directive, which specifies run-time dependencies for the package, includes only `bash`{.literal}, because the `bello`{.literal} script requires only the `bash`{.literal} shell environment to run.
-   The `%build`{.literal} section, which specifies how to build the software, is blank, because the `bash`{.literal} script does not need to be built.

**Additional resources**

-   [What is source code](#what-is-source-code "4.1. What is source code")

#### [6.4.4. An example spec file for a sample Python program](#example-spec-for-sample-python) {#an-example-spec-file-for-a-sample-python-program .title}

Review the following annotated example `spec`{.literal} file for a sample program written in the Python programming language (`pello`{.literal}).

This example of creating a wrapper script in-line in the `spec`{.literal} file shows that the `spec`{.literal} file itself is scriptable. This wrapper script executes the Python byte-compiled code by using the `here`{.literal} document.

**Example 6.4. An example spec file for the pello program**

``` {.language-plaintext tabindex="-1"}
Name:           pello
Version:        0.1.1
Release:        1%{?dist}
Summary:        Hello World example implemented in Python

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

BuildRequires:  python
Requires:       python
Requires:       bash

BuildArch:      noarch

%description
The long-tail description for our Hello World Example implemented in Python.

%prep
%setup -q

%build

python -m compileall %{name}.py

%install

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}

cat > %{buildroot}/%{_bindir}/%{name} <<EOF
#!/bin/bash
/usr/bin/python /usr/lib/%{name}/%{name}.pyc
EOF

chmod 0755 %{buildroot}/%{_bindir}/%{name}

install -m 0644 %{name}.py* %{buildroot}/usr/lib/%{name}/

%files
%license LICENSE
%dir /usr/lib/%{name}/
%{_bindir}/%{name}
/usr/lib/%{name}/%{name}.py*

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org> - 0.1.1-1
  - First pello package
```

-   The `Requires`{.literal} directive, which specifies run-time dependencies for the package, includes two packages:

    -   The `python`{.literal} package required to execute the byte-compiled code at runtime.
    -   The `bash`{.literal} package required to execute the small entry-point script.

-   The `BuildRequires`{.literal} directive, which specifies build-time dependencies for the package, includes only the `python`{.literal} package. The `pello`{.literal} program requires `python`{.literal} to perform the byte-compile build process.

-   The `%build`{.literal} section, which specifies how to build the software, creates a byte-compiled version of the script. Note that in real-world packaging, it is usually done automatically, depending on the distribution used.

-   The `%install`{.literal} section corresponds to the fact that you must install the byte-compiled file into a library directory on the system so that it can be accessed.

**Additional resources**

-   [What is source code](#what-is-source-code "4.1. What is source code")

#### [6.4.5. An example spec file for a sample C program](#example-spec-for-sample-c) {#an-example-spec-file-for-a-sample-c-program .title}

Review the following annotated example `spec`{.literal} file for a sample program written in the C programming language (`cello`{.literal}).

You can install the `cello`{.literal} program by using the `%make_install`{.literal} macro. This is possible because the `Makefile`{.literal} file for the `cello`{.literal} program is available.

**Example 6.5. An example spec file for the cello program**

``` {.language-plaintext tabindex="-1"}
Name:           cello
Version:        1.0
Release:        1%{?dist}
Summary:        Hello World example implemented in C

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

Patch0:         cello-output-first-patch.patch

BuildRequires:  gcc
BuildRequires:  make

%description
The long-tail description for our Hello World Example implemented in
C.

%prep
%setup -q

%patch0

%build
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.0-1
- First cello package
```

-   The `BuildRequires`{.literal} directive, which specifies build-time dependencies for the package, includes the following packages required to perform the compilation build process:

    -   `gcc`{.literal}
    -   `make`{.literal}

-   The `Requires`{.literal} directive, which specifies run-time dependencies for the package, is omitted in this example. All runtime requirements are handled by `rpmbuild`{.literal}, and the `cello`{.literal} program does not require anything outside of the core C standard libraries.

-   The `%build`{.literal} section reflects the fact that in this example the `Makefile`{.literal} file for the **cello** program was written. Therefore, you can use the GNU make command. However, you must remove the call to `%configure`{.literal} because you did not provide a configure script.

**Additional resources**

-   [What is source code](#what-is-source-code "4.1. What is source code")

### [6.5. Building RPMs](#building-rpms) {#building-rpms .title}

Build RPM packages for sample `bello`{.literal}, `pello`{.literal}, and `cello`{.literal} programs by using the `rpmbuild`{.literal} utility.

Different use cases require different combinations of arguments to the `rpmbuild`{.literal} command. The following are the main use cases:

-   Building source RPMs.

-   Building binary RPMs:

    -   Rebuilding a binary RPM from a source RPM.
    -   Building a binary RPM from the `spec`{.literal} file.

Note

When using the `rpmbuild`{.literal} command, a certain directory and file structure is expected, which is the same as the structure that was configured by the `rpmdev-setuptree`{.literal} utility.

#### [6.5.1. Building a source RPM](#building-source-rpms) {#building-a-source-rpm .title}

Put a source code of the `bello`{.literal}, `pello`{.literal}, and `cello`{.literal} sample programs into Source RPM (SRPM) packages by using the `rpmbuild`{.literal} utility.

Building Source RPMs (SRPMs) has the following advantages:

-   You can preserve the exact source of a certain `Name-Version-Release`{.literal} (`NVR`{.literal}) of an RPM file that was deployed to an environment. This includes the exact `spec`{.literal} file, the source code, and all relevant patches. This is useful for tracking and debugging purposes.
-   You can build a binary RPM on a different hardware platform or architecture.

**Prerequisites**

-   You installed the `rpmbuild`{.literal} utility on your system:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rpm-build
    ```

-   You placed the following `Hello World!`{.literal} implementations into the `~/rpmbuild/SOURCES/`{.literal} directory:

    -   [bello-0.1.tar.gz](https://github.com/redhat-developer/rpm-packaging-guide/raw/master/example-code/bello-0.1.tar.gz)
    -   [pello-0.1.2.tar.gz](https://github.com/redhat-developer/rpm-packaging-guide/raw/master/example-code/pello-0.1.2.tar.gz)
    -   [cello-1.0.tar.gz](https://github.com/redhat-developer/rpm-packaging-guide/raw/master/example-code/cello-1.0.tar.gz) ( [cello-output-first-patch.patch](https://raw.githubusercontent.com/redhat-developer/rpm-packaging-guide/master/example-code/cello-output-first-patch.patch) )

-   A `spec`{.literal} file for the program that you want to package exists.

**Procedure**

1.  Navigate to the `~/rpmbuild/SPECS/`{.literal} directive, which contains the created `spec`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/rpmbuild/SPECS/
    ```

2.  Build the source RPM by entering the `rpmbuild`{.literal} command with the specified `spec`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ rpmbuild -bs <specfile>
    ```

    The `-bs`{.literal} option stands for the *build source*.

    For example, to build source RPMs for the `bello`{.literal}, `pello`{.literal}, and `cello`{.literal} programs, complete the following steps:

    a.  Build a source RPM for the `bello`{.literal} program:

        ``` {.language-plaintext tabindex="-1"}
        $ rpmbuild -bs bello.spec
        ```

        ``` {.language-plaintext tabindex="-1"}
        Wrote: /home/admiller/rpmbuild/SRPMS/bello-0.1-1.el8.src.rpm
        ```

    b.  Build a source RPM for the `pello`{.literal} program:

        ``` {.language-plaintext tabindex="-1"}
        $ rpmbuild -bs pello.spec
        ```

        ``` {.language-plaintext tabindex="-1"}
        Wrote: /home/admiller/rpmbuild/SRPMS/pello-0.1.2-1.el8.src.rpm
        ```

    c.  Build a source RPM for the `cello`{.literal} program:

        ``` {.language-plaintext tabindex="-1"}
        $ rpmbuild -bs cello.spec
        ```

        ``` {.language-plaintext tabindex="-1"}
        Wrote: /home/admiller/rpmbuild/SRPMS/cello-1.0-1.el8.src.rpm
        ```

**Verification**

-   Verify that the `rpmbuild/SRPMS`{.literal} directory includes the resulting source RPMs. The directory is a part of the structure expected by `rpmbuild`{.literal}.

**Additional resources**

-   [Working with spec files](#working-with-spec-files "6.4. Working with spec files")

#### [6.5.2. Rebuilding a binary RPM from a source RPM](#rebuilding-binary-rpm-from-srpm) {#rebuilding-a-binary-rpm-from-a-source-rpm .title}

Rebuild binary RPM packages for sample `bello`{.literal}, `pello`{.literal}, and `cello`{.literal} programs from their source RPM (SRPM) packages by using the `rpmbuild`{.literal} utility. You can then install and run the binary packages on multiple systems.

The output generated when creating the binary RPM is verbose, which is helpful for debugging. The output varies for different examples and corresponds to their `spec`{.literal} files.

The resulting binary RPMs are located in either of the following directories:

-   `~/rpmbuild/RPMS/YOURARCH`{.literal}, where `YOURARCH`{.literal} is your architecture
-   `~/rpmbuild/RPMS/noarch/`{.literal}, if the package is not architecture-specific

**Prerequisites**

-   You installed the `rpmbuild`{.literal} utility on your system:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rpm-build
    ```

**Procedure**

1.  Navigate to the `~/rpmbuild/SRPMS/`{.literal} directive, which contains the SRPM:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/rpmbuild/SRPMS/
    ```

2.  Rebuild the binary RPM from the SRPM:

    ``` {.language-plaintext tabindex="-1"}
    $ rpmbuild --rebuild <srpm>
    ```

    For example, to rebuild `bello`{.literal}, `pello`{.literal}, and `cello`{.literal} from their SRPMs, complete the following steps:

    a.  Rebuild the `bello`{.literal} program:

        ``` {.language-plaintext tabindex="-1"}
        $ rpmbuild --rebuild bello-0.1-1.el8.src.rpm
        ```

    b.  Rebuild the `pello`{.literal} program:

        ``` {.language-plaintext tabindex="-1"}
        $ rpmbuild --rebuild pello-0.1.2-1.el8.src.rpm
        ```

    c.  Rebuild the `cello`{.literal} program:

        ``` {.language-plaintext tabindex="-1"}
        $ rpmbuild --rebuild cello-1.0-1.el8.src.rpm
        ```

    Note

    Invoking `rpmbuild --rebuild`{.literal} involves the following processes:

    -   Installing the contents of the SRPM (the `spec`{.literal} file and the source code) into the `~/rpmbuild/`{.literal} directory.
    -   Building an RPM by using the installed contents.
    -   Removing the `spec`{.literal} file and the source code.

    You can retain the `spec`{.literal} file and the source code after building either of the following ways:

    -   When building the RPM, use the `rpmbuild`{.literal} command with the `--recompile`{.literal} option instead of the `--rebuild`{.literal} option.

    -   Install SRPMs for the `bello`{.literal}, `pello`{.literal}, and `cello`{.literal} programs:

        1.  Install the SRPM for `bello`{.literal}:

            ``` {.language-plaintext tabindex="-1"}
            $ rpm -Uvh ~/rpmbuild/SRPMS/bello-0.1-1.el8.src.rpm
            ```

            ``` {.language-plaintext tabindex="-1"}
            Updating / installing...
               1:bello-0.1-1.el8               [100%]
            ```

        2.  Install the SRPM for `pello`{.literal}:

            ``` {.language-plaintext tabindex="-1"}
            $ rpm -Uvh ~/rpmbuild/SRPMS/pello-0.1.2-1.el8.src.rpm
            ```

            ``` {.language-plaintext tabindex="-1"}
            Updating / installing...
            ...1:pello-0.1.2-1.el8              [100%]
            ```

        3.  Install the SRPM for `cello`{.literal}:

            ``` {.language-plaintext tabindex="-1"}
            $ rpm -Uvh ~/rpmbuild/SRPMS/cello-1.0-1.el8.src.rpm
            ```

            ``` {.language-plaintext tabindex="-1"}
            Updating / installing...
            ...1:cello-1.0-1.el8            [100%]
            ```

#### [6.5.3. Building a binary RPM from a spec file](#building-binary-rpm-from-spec) {#building-a-binary-rpm-from-a-spec-file .title}

Build binary RPMs for sample `bello`{.literal}, `pello`{.literal}, and `cello`{.literal} programs from their `spec`{.literal} files by using the `rpmbuild`{.literal} command.

**Prerequisites**

-   You have installed the `rpmbuild`{.literal} utility on your system:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rpm-build
    ```

**Procedure**

1.  Navigate to the `~/rpmbuild/SPECS/`{.literal} directive, which contains `spec`{.literal} files:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/rpmbuild/SPECS/
    ```

2.  Build the binary RPM from its `spec`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ rpmbuild -bb <spec_file>
    ```

    For example, to build `bello`{.literal}, `pello`{.literal}, and `cello`{.literal} binary RPMs from their `spec`{.literal} files, complete the following steps:

    a.  Build the `bello`{.literal} program:

        ``` {.language-plaintext tabindex="-1"}
        $ rpmbuild -bb bello.spec
        ```

    b.  Build the `pello`{.literal} program:

        ``` {.language-plaintext tabindex="-1"}
        $ rpmbuild -bb pello.spec
        ```

    c.  Build the `cello`{.literal} program:

        ``` {.language-plaintext tabindex="-1"}
        $ rpmbuild -bb cello.spec
        ```

### [6.6. Logging RPM activity to syslog](#logging-rpm-activity-to-syslog) {#logging-rpm-activity-to-syslog .title}

Log any RPM activity or transaction by using the System Logging protocol (`syslog`{.literal}).

**Prerequisites**

-   The `syslog`{.literal} plug-in is installed on the system:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rpm-plugin-syslog
    ```

    Note

    The default location for the `syslog`{.literal} messages is the `/var/log/messages`{.literal} file. However, you can configure `syslog`{.literal} to use another location to store the messages.

**Procedure**

1.  Open the file that you configured to store the `syslog`{.literal} messages.

    Alternatively, if you use the default `syslog`{.literal} configuration, open the `/var/log/messages`{.literal} file.

2.  Search for new lines including the `[RPM]`{.literal} string.

### [6.7. Extracting RPM content](#extracting-rpm-content) {#extracting-rpm-content .title}

To access the contents of a software package, extract the RPM files.

In some cases, for example, if a package required by RPM is damaged, you might need to extract the content of the package. In such cases, if an RPM installation is still working despite the damage, you can use the `rpm2archive`{.literal} utility to convert an `.rpm`{.literal} file to a tar archive to use the content of the package.

Note

If the RPM installation is severely damaged, you can use the `rpm2cpio`{.literal} utility to convert the RPM package file to a `cpio`{.literal} archive.

**Procedure**

-   Convert the RPM file to the tar archive:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm2archive <filename>.rpm
    ```

    The resulting file has the `.tgz`{.literal} suffix. For example, to create an archive from the `bash`{.literal} package, complete the following steps:

    a.  Convert the `bash`{.literal} RPM package to the tar archive:

        ``` {.language-plaintext tabindex="-1"}
        $ rpm2archive bash-4.4.19-6.el8.x86_64.rpm
        ```

    b.  Display the contents of the archive file:

        ``` {.language-plaintext tabindex="-1"}
        $ ls bash-4.4.19-6.el8.x86_64.rpm.tgz
        ```

        ``` {.language-plaintext tabindex="-1"}
        bash-4.4.19-6.el8.x86_64.rpm.tgz
        ```

### [6.8. Signing RPM packages](#signing-rpm-packages) {#signing-rpm-packages .title}

Sign RPM packages to ensure no third party can alter their content.

You can sign an RPM package by using either of the following software:

-   Sequoia PGP supports the OpenPGP standard. RPM also uses Sequoia PGP to verify software signatures.
-   GNU Privacy Guard (GnuPG) supports older OpenPGP standard versions, which makes GnuPG more compatible with RHEL 9 and earlier versions.

Warning

Starting from version 10.1, RHEL supports OpenPGPv6 and RPMv6 signatures. These signatures are not compatible with earlier versions of RHEL. RPM on these versions ignore such signatures. If a package contains the RPMv4 signature, RPM uses it instead.

However, in RHEL 9.7 and later RHEL 9 versions, you can enable support for OpenPGPv6 and RPMv6 signatures by using the `multisig`{.literal} DNF plugin.

#### [6.8.1. Signing RPM packages with GnuPG](#signing-rpm-packages-with-gpg) {#signing-rpm-packages-with-gnupg .title}

Sign RPM packages by using the GNU Privacy Guard (GnuPG) to ensure no third party can alter their content.

##### [6.8.1.1. Creating an OpenPGP key for signing packages with GnuPG](#creating-a-gpg-key) {#creating-an-openpgp-key-for-signing-packages-with-gnupg .title}

To sign an RPM package by using the GNU Privacy Guard (GnuPG) software, create an OpenPGP key first.

**Prerequisites**

-   You have the `rpm-sign`{.literal} and `pinentry`{.literal} packages installed on your system.

**Procedure**

1.  Generate an OpenPGP key pair:

    ``` {.language-plaintext tabindex="-1"}
    $ gpg --gen-key
    ```

2.  Check the generated key pair:

    ``` {.language-plaintext tabindex="-1"}
    $ gpg --list-keys
    ```

3.  Export the public key:

    ``` {.language-plaintext tabindex="-1"}
    $ gpg --export -a '<public_key_name>' > RPM-GPG-KEY-pmanager
    ```

**Next steps**

1.  [Configure RPM to sign a package with GnuPG](#configuring-rpm-to-sign-a-package-with-gpg "6.8.1.2. Configuring RPM to sign a package with GnuPG").
2.  [Add a signature to an RPM package](#adding-a-signature-to-an-rpm-package-gpg "6.8.1.3. Adding a signature to an RPM package").

##### [6.8.1.2. Configuring RPM to sign a package with GnuPG](#configuring-rpm-to-sign-a-package-with-gpg) {#configuring-rpm-to-sign-a-package-with-gnupg .title}

To sign an RPM package by using the GNU Privacy Guard (GnuPG) software, configure RPM by specifying the `%_gpg_name`{.literal} RPM macro.

**Prerequisites**

-   You created an OpenPGP key for GnuPG, For more information, see [Creating an OpenPGP key for signing packages with GnuPG](#creating-a-gpg-key "6.8.1.1. Creating an OpenPGP key for signing packages with GnuPG").

**Procedure**

-   Define the `%_gpg_name`{.literal} macro in your `$HOME/.rpmmacros`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    %_gpg_name <key_ID>
    ```

    A valid key ID value for GnuPG can be a key fingerprint, full name, or email address you provided when creating the key.

**Next steps**

-   [Add a signature to an RPM package](#adding-a-signature-to-an-rpm-package-gpg "6.8.1.3. Adding a signature to an RPM package").

##### [6.8.1.3. Adding a signature to an RPM package](#adding-a-signature-to-an-rpm-package-gpg) {#adding-a-signature-to-an-rpm-package .title}

Packages are commonly built without signatures. Add your signature to the package to ensure no third party can alter its content before the package is released.

**Prerequisites**

-   You created an OpenPGP key for GnuPG. For more information, see [Creating an OpenPGP key for signing packages with GnuPG](#creating-a-gpg-key "6.8.1.1. Creating an OpenPGP key for signing packages with GnuPG").
-   You configured RPM for signing packages. For more information, see [Configuring RPM to sign a package with GnuPG](#configuring-rpm-to-sign-a-package-with-gpg "6.8.1.2. Configuring RPM to sign a package with GnuPG").
-   You have the `rpm-sign`{.literal} package installed on your system.

**Procedure**

-   Add a signature to a package:

    ``` {.language-plaintext tabindex="-1"}
    $ rpmsign --addsign <package-name>.rpm
    ```

**Verification**

1.  Import the [exported OpenPGP public key](#creating-a-gpg-key "6.8.1.1. Creating an OpenPGP key for signing packages with GnuPG") into the RPM keyring:

    ``` {.language-plaintext tabindex="-1"}
    # rpmkeys --import RPM-GPG-KEY-pmanager
    ```

2.  Display the key ID with GnuPG:

    ``` {.language-plaintext tabindex="-1"}
    $ gpg --list-keys
    ```

    ``` {.language-plaintext tabindex="-1"}
    [...]
    pub   rsa3072 2025-05-13 [SC] [expires: 2028-05-12]
          A8AF1C39AC67A1501450734F6DE8FC866DE0394D
    [...]
    ```

    The key ID is the 40-character string in the command output, for example, `A8AF1C39AC67A1501450734F6DE8FC866DE0394D`{.literal}.

3.  Verify that the RPM file has the corresponding signature:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm -Kv <package_name>.rpm
    ```

    ``` {.language-plaintext tabindex="-1"}
    <package_name>.rpm:
        Header V4 RSA/SHA256 Signature, key ID 6de0394d: OK
        Header SHA256 digest: OK
        Header SHA1 digest: OK
        Payload SHA256 digest: OK
        MD5 digest: OK
    ```

    The signature key ID matches the last part of the OpenPGP key ID.

#### [6.8.2. Signing RPM packages with Sequoia PGP](#signing-rpm-packages-with-sequoia-pgp) {#signing-rpm-packages-with-sequoia-pgp .title}

Sign RPM packages by using Sequoia PGP to ensure no third party can alter their content.

##### [6.8.2.1. Creating an OpenPGP key for signing packages with Sequoia PGP](#creating-an-openpgp-key) {#creating-an-openpgp-key-for-signing-packages-with-sequoia-pgp .title}

To sign packages by using the Sequoia PGP software, create an OpenPGP key first.

**Procedure**

1.  Install the Sequoia PGP tools:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install sequoia-sq
    ```

2.  Generate an OpenPGP key pair:

    ``` {.language-plaintext tabindex="-1"}
    $ sq key generate --own-key --userid <key_name>
    ```

3.  Check the generated key pair:

    ``` {.language-plaintext tabindex="-1"}
    $ sq key list
    ```

4.  Export the public key:

    ``` {.language-plaintext tabindex="-1"}
    $ sq cert export --cert-userid '<key_name>' > RPM-PGP-KEY-pmanager
    ```

**Next steps**

1.  [Configure RPM to sign a package with Sequoia PGP](#configuring-rpm-for-sequoia "6.8.2.2. Configuring RPM to sign a package with Sequoia PGP").
2.  [Add a signature to an RPM package](#adding-a-signature-to-an-rpm-package-sequoia "6.8.2.3. Adding a signature to an RPM package").

##### [6.8.2.2. Configuring RPM to sign a package with Sequoia PGP](#configuring-rpm-for-sequoia) {#configuring-rpm-to-sign-a-package-with-sequoia-pgp .title}

To sign an RPM package with the Sequoia PGP software, configure the RPM to use Sequoia PGP and specify the `%_gpg_name`{.literal} macro.

**Prerequisites**

-   You have the `rpm-sign`{.literal} package installed on your system.

**Procedure**

1.  Copy the `macros.rpmsign-sequoia`{.literal} file to the `/etc/rpm`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp /usr/share/doc/rpm/macros.rpmsign-sequoia /etc/rpm/
    ```

2.  Get a valid OpenPGP key fingerprint value from the output of key listing:

    ``` {.language-plaintext tabindex="-1"}
    $ sq cert list --cert-userid '<key_name>'
    ```

    ``` {.language-plaintext tabindex="-1"}
     - 7E4B52101EB3DB08967A1E5EB595D12FDA65BA50
       - created 2025-05-13 10:33:29 UTC
       - will expire 2028-05-13T03:59:50Z

       - [    ✓    ] <key_name>
    ```

    The key fingerprint is a 40-character string on the first line of the output, for example, `7E4B52101EB3DB08967A1E5EB595D12FDA65BA50`{.literal}.

3.  Define the `%_gpg_name`{.literal} macro in your `$HOME/.rpmmacros`{.literal} file as follows:

    ``` {.language-plaintext tabindex="-1"}
    %_gpg_name <key_fingerprint>
    ```

    Note that you can also use the full key ID instead of the fingerprint.

    Note

    Unlike GnuPG, Sequoia PGP accepts only the full key ID or fingerprint.

**Next steps**

-   [Add a signature to an RPM package](#adding-a-signature-to-an-rpm-package-sequoia "6.8.2.3. Adding a signature to an RPM package").

##### [6.8.2.3. Adding a signature to an RPM package](#adding-a-signature-to-an-rpm-package-sequoia) {#adding-a-signature-to-an-rpm-package-1 .title}

Packages are commonly built without signatures. Add your signature to the package to ensure no third party can alter its content before the package is released.

**Prerequisites**

-   You created an OpenPGP key. For more information, see [Creating an OpenPGP key for signing packages with Sequoia PGP](#creating-an-openpgp-key "6.8.2.1. Creating an OpenPGP key for signing packages with Sequoia PGP").
-   You configured RPM for signing packages. For more information, see [Configuring RPM to sign a package with Sequoia PGP](#configuring-rpm-for-sequoia "6.8.2.2. Configuring RPM to sign a package with Sequoia PGP").
-   You have the `rpm-sign`{.literal} package installed on your system.

**Procedure**

-   Add a signature to a package:

    ``` {.language-plaintext tabindex="-1"}
    $ rpmsign --addsign <package-name>.rpm
    ```

**Verification**

1.  Import the [exported OpenPGP public key](#creating-an-openpgp-key "6.8.2.1. Creating an OpenPGP key for signing packages with Sequoia PGP") into the RPM keyring:

    ``` {.language-plaintext tabindex="-1"}
    # rpmkeys --import RPM-PGP-KEY-pmanager
    ```

2.  Display the key fingerprint of the signing key:

    ``` {.language-plaintext tabindex="-1"}
    $ sq key list --cert-userid <key_name>
    ```

    ``` {.language-plaintext tabindex="-1"}
     - 7E4B52101EB3DB08967A1E5EB595D12FDA65BA50
       - user ID: <key_name> (authenticated)
       - created 2025-05-13 10:33:29 UTC
       - will expire 2028-05-13T03:59:50Z
       - usable for signing
       - @softkeys/7E4B52101EB3DB08967A1E5EB595D12FDA65BA50: available, unlocked

       - 78E56DD2E12E02CFEEA27F8B9FE57972D6BCEA6F
         - created 2025-05-13 10:33:29 UTC
         - will expire 2028-05-13T03:59:50Z
         - usable for decryption
         - @softkeys/7E4B52101EB3DB08967A1E5EB595D12FDA65BA50: available, unlocked
       - C06E45F8ABC3E59F44A9E811578DDDB66422E345
         - created 2025-05-13 10:33:29 UTC
         - will expire 2028-05-13T03:59:50Z
         - usable for signing
         - @softkeys/7E4B52101EB3DB08967A1E5EB595D12FDA65BA50: available, unlocked
       - E0BD231AB350AD6802D44C0A270E79FFC39C3B25
         - created 2025-05-13 10:33:29 UTC
         - will expire 2028-05-13T03:59:50Z
         - usable for signing
         - @softkeys/7E4B52101EB3DB08967A1E5EB595D12FDA65BA50: available, unlocked
    ```

    The key fingerprint is usually a signing subkey in the `sq key list --cert-userid `{.literal}*`<key_name>`{.literal}* command output, for example, `E0BD231AB350AD6802D44C0A270E79FFC39C3B25`{.literal}.

3.  Verify that the RPM file has the corresponding signature, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm -Kv <package_name>.rpm
    ```

    ``` {.language-plaintext tabindex="-1"}
    <package_name>.rpm:
        Header V4 EdDSA/SHA512 Signature, key ID c39c3b25: OK
        Header SHA256 digest: OK
        Header SHA1 digest: OK
        Payload SHA256 digest: OK
        MD5 digest: OK
    ```

    The signature key ID matches the last part of the key fingerprint.

#### [6.8.3. Signing RPM packages with Sequoia PGP by using PQC](#signing-packages-with-pqc) {#signing-rpm-packages-with-sequoia-pgp-by-using-pqc .title}

Sign RPM packages with PQC algorithms by using Sequoia PGP to ensure no third party can alter their content.

Post-quantum cryptography (PQC) is a set of algorithms designed to withstand attacks from quantum computers, thereby enhancing software security.

The RPM package manager uses the OpenPGP standard to sign packages. OpenPGPv6 introduces support for hybrid keys and signatures. They combine the current cryptographic algorithm with the PQC algorithm, preventing a single point of failure and increasing trust in the resulting signature.

Starting from version 10.1, RHEL supports RPMv6 signatures. With this format, you can add multiple OpenPGP signatures to a package, increasing the redundancy on the RPM level.

You can combine both RPMv4 and RPMv6 signatures to sign the package. With this feature, you can use different RPM versions to verify the same signature. Starting from RHEL 10.1, RPM verifies only the RPMv6 signatures, if such exist, and ignores the RPMv4 ones. If no RPMv6 signatures are present in the package, RPM uses the RPMv4 signatures. In earlier RHEL versions, RPM verifies RPMv4 signatures and ignores RPMv6 ones by default. In RHEL 9.7 and later RHEL 9 versions, you can enable support for RPMv6 signatures.

##### [6.8.3.1. Creating a PQC key](#creating-a-pqc-key) {#creating-a-pqc-key .title}

To sign packages by using post-quantum cryptography (PQC) algorithms, create a hybrid key pair with Sequoia PGP first.

When generating a PQC key, you can specify different PQC algorithms. For example, the following procedure uses the `ML-DSA-87-Ed448`{.literal} algorithm.

**Procedure**

1.  Install the Sequoia PGP tools:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install sequoia-sq
    ```

2.  Generate an OpenPGP key pair:

    ``` {.language-plaintext tabindex="-1"}
    $ sq key generate --own-key --expiration=never \ --cannot-authenticate --cannot-encrypt \ --email <vendor_email> --name "<vendor_name>" \ --cipher-suite mldsa87 --profile rfc9580
    ```

    Replace *\<vendor_email\>* and *\<vendor_name\>* with the email and the name of the software vendor that provides the RPM package.

    This command generates a primary key and a signing subkey.

3.  Check the generated key pair:

    ``` {.language-plaintext tabindex="-1"}
    $ sq key list --cert-email <vendor_email>
    ```

    ``` {.language-plaintext tabindex="-1"}
     - <ml_dsa_fingerprint>
       - user IDs:
         - <vendor_email> (authenticated)
         - <vendor_name> (authenticated)
       - created 2025-10-03 14:36:44 UTC
       - usable for signing
       - @softkeys/<ml_dsa_fingerprint>: available, unlocked

       - <subkey_fingerprint>
         - created 2025-10-03 14:36:44 UTC
         - usable for signing
         - @softkeys/<subkey_fingerprint>: available, unlocked
    ```

4.  Export the PQC OpenPGP certificate:

    ``` {.language-plaintext tabindex="-1"}
    $ sq cert export --cert-email '<vendor_email>' > RPM-PGP-KEY-VENDOR
    ```

**Next steps**

-   [Configure RPM for PQC](#configuring-rpm-for-pqc "6.8.3.2. Configuring RPM for PQC").

##### [6.8.3.2. Configuring RPM for PQC](#configuring-rpm-for-pqc) {#configuring-rpm-for-pqc .title}

After you generated a PQC key you want to use to sign a package, configure RPM to use this key.

Configure RPM outside of the build system on a separate signing server. RPM requires macros to support signing packages with Sequoia PGP. These macros are available in a template file.

**Prerequisites**

-   You created a PQC key pair. For more information, see [Creating a PQC key](#creating-a-pqc-key "6.8.3.1. Creating a PQC key").
-   You have the `rpm-sign`{.literal} package installed on your system.

**Procedure**

1.  Copy the `macros.rpmsign-sequoia`{.literal} file to the `/etc/rpm`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp /usr/share/doc/rpm/macros.rpmsign-sequoia /etc/rpm/
    ```

2.  Check the generated key pair:

    ``` {.language-plaintext tabindex="-1"}
    $ sq key list --cert-email <vendor_email>
    ```

    ``` {.language-plaintext tabindex="-1"}
     - <ml_dsa_fingerprint>
       - user IDs:
         - <vendor_email> (authenticated)
         - <vendor_name> (authenticated)
       - created 2025-10-03 14:36:44 UTC
       - usable for signing
       - @softkeys/<ml_dsa_fingerprint>: available, unlocked

       - <subkey_fingerprint>
         - created 2025-10-03 14:36:44 UTC
         - usable for signing
         - @softkeys/<subkey_fingerprint>: available, unlocked
    ```

3.  Export the key fingerprint to the `~/.rpmmacros`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ echo "%_gpg_name <ml_dsa_fingerprint>" > ~/.rpmmacros
    ```

**Next steps**

-   [Add multiple signatures to a package](#adding-multiple-signatures-to-packages "6.8.3.3. Adding multiple signatures to an RPM").

##### [6.8.3.3. Adding multiple signatures to an RPM](#adding-multiple-signatures-to-packages) {#adding-multiple-signatures-to-an-rpm .title}

To enhance software security, add multiple RPMv6 signatures to an RPM package.

Starting from version 10.1, RHEL supports RPMv6 signatures. With this format, you can add multiple signatures to an RPM package. This results in enhanced security if either of the keys gets compromised or either of the cryptographic algorithms is rendered insecure.

You can run the `rpmsign --addsign --rpmv6`{.literal} command multiple times to sign the RPM with multiple different keys. Note that the first RPMv6 signature, usually generated with an OpenPGPv4 RSA key and compatible with the RPMv4, is also stored as an RPMv4 signature. This allows older RPM versions to trust the package signature.

Important

Always consider adding an RPMv4-compatible signature to the package before adding any RPMv6 signatures that use PQC algorithms. This ensures that the package has a signature that RPM on RHEL versions earlier than RHEL 10.1 can verify.

**Prerequisites**

-   You generated a PQC key pair. For more information, see [Creating a PQC key](#creating-a-pqc-key "6.8.3.1. Creating a PQC key").
-   You configured RPM to use the PQC key. For more information, see [Configuring RPM for PQC](#configuring-rpm-for-pqc "6.8.3.2. Configuring RPM for PQC").

**Procedure**

1.  Add a signature to a package:

    ``` {.language-plaintext tabindex="-1"}
    $ rpmsign --addsign --rpmv6 <package_name>.rpm
    ```

2.  To sign the package with multiple RPMv6 signatures, repeat the first step.

**Verification**

1.  Import the [exported PQC OpenPGP certificate](#creating-a-pqc-key "6.8.3.1. Creating a PQC key") into the RPM keyring:

    ``` {.language-plaintext tabindex="-1"}
    # rpmkeys --import RPM-PGP-KEY-VENDOR
    ```

2.  Verify that the RPM file has the corresponding signatures, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ rpmkeys -Kv <package_name>.rpm
    ```

    ``` {.language-plaintext tabindex="-1"}
    <package_name>.rpm:
        Header OpenPGP V6 ML-DSA-87+Ed448/SHA512 signature, key fingerprint: <ml_dsa_fingerprint>: OK
        Header OpenPGP V4 RSA/SHA512 signature, key fingerprint: <rsa_fingerprint>: OK
        Header SHA256 digest: OK
        Payload SHA256 digest: OK
    ```

## [Chapter 7. Packaging Python 3 RPMs](#packaging-python-3-rpms) {#chapter-7.-packaging-python-3-rpms .title}

You can install Python packages on your system by using the DNF package manager. DNF uses the RPM package format, which offers more downstream control over the software.

Packaging a Python project into an RPM package provides the following advantages compared to native Python packages:

-   Dependencies on Python and non-Python packages are possible and strictly enforced by the DNF package manager.
-   You can cryptographically sign the packages. With cryptographic signing, you can verify, integrate, and test contents of RPM packages with the rest of the operating system.
-   You can run tests during the build process.

The packaging format of native Python packages follows the specifications published by the Python Packaging Authority (PyPA). Historically, most Python projects used the `distutils`{.literal} or `setuptools`{.literal} utilities for packaging and defined package information in the `setup.py`{.literal} file. However, options for creating native Python packages have evolved over time:

To package Python software, whether the project uses `setup.py`{.literal} or `pyproject.toml`{.literal}, use pyproject RPM macros from the `pyproject-rpm-macros`{.literal} package.

### [7.1. A spec file description for an example Python package](#a-spec-file-description-for-an-example-python-package) {#a-spec-file-description-for-an-example-python-package .title}

Review the notes about Python RPM `spec`{.literal} file specifics in the following example of the `python3-pello`{.literal} package.

The RPM `spec`{.literal} file for Python projects has some specifics compared to non-Python RPM `spec`{.literal} files. For example, it is recommended for any RPM package name of a Python library to include the `python3-`{.literal} prefix.

**Example 7.1. An example `spec`{.literal} file for the program written in Python**

``` {.language-plaintext tabindex="-1"}
%global python3_pkgversion 3

Name:           python-pello
Version:        1.0.2
Release:        1%{?dist}
Summary:        Example Python library

License:        MIT
URL:            https://github.com/fedora-python/Pello
Source:         %{url}/archive/v%{version}/Pello-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel

# Build dependencies need to be specified manually
BuildRequires:  python%{python3_pkgversion}-setuptools

# Test dependencies need to be specified manually
# Runtime dependencies need to be BuildRequired manually to run tests during build
BuildRequires:  python%{python3_pkgversion}-pytest >= 3

%global _description %{expand:
Pello is an example package with an executable that prints Hello World! on the command line.}

%description %_description

%package -n python%{python3_pkgversion}-pello
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pello %_description

%prep
%autosetup -p1 -n Pello-%{version}

%build
# The macro only supports projects with setup.py
%py3_build

%install
# The macro only supports projects with setup.py
%py3_install

%check
%pytest

# Note that there is no %%files section for python-pello
%files -n python%{python3_pkgversion}-pello
%doc README.md
%license LICENSE.txt
%{_bindir}/pello_greeting

# The library files needed to be listed manually
%{python3_sitelib}/pello/

# The metadata files needed to be listed manually
%{python3_sitelib}/Pello-*.egg-info/
```

-   By defining the `python3_pkgversion`{.literal} macro, you set which Python version this package will be built for. To build for the default Python version `3.12`{.literal}, remove the line.

-   When packaging a Python project into RPM, always add the `python-`{.literal} prefix to the original name of the project. The project name here is `Pello`{.literal} and, therefore, the name of the Source RPM (SRPM) is `python-pello`{.literal}.

-   `BuildRequires`{.literal} specifies what packages are required to build and test this package. In `BuildRequires`{.literal}, always include `python3-devel`{.literal} and other tools that you need to build Python packages. Also list the projects that your software requires, such as `python3-setuptools`{.literal}. Add any runtime and testing dependencies that you need to run tests in the `%check`{.literal} section.

-   When choosing a name for the binary RPM (the package that users will be able to install), add a versioned Python prefix. Use the `python3-`{.literal} prefix for the default Python 3.12. You can use the `%{python3_pkgversion}`{.literal} macro, which evaluates to `3`{.literal} for the default Python version `3.12`{.literal} unless you set it to an explicit version, for example, when a later version of Python is available (see footnote 1).

-   The `%py3_build`{.literal} and `%py3_install`{.literal} macros run the `setup.py build`{.literal} and `setup.py install`{.literal} commands, respectively, with additional arguments to specify installation locations, the interpreter to use, and other details.

    Note

    Using the `setup.py build`{.literal} and `setup.py install`{.literal} commands from the `setuptools`{.literal} package is deprecated. For modern projects, use the `pyproject`{.literal} RPM macros from the `pyproject-rpm-macros`{.literal} package. For more information, see [Packaging Python projects with pyproject RPM macros](#packaging-python-projects-with-pyproject-rpm-macros "7.4. Packaging Python projects with pyproject RPM macros").

-   The `%check`{.literal} section runs the tests of the packaged project. The exact command depends on the project itself, but you can use the `%pytest`{.literal} macro to run the `pytest`{.literal} command in an RPM-friendly way.

### [7.2. Common macros for Python 3 RPMs](#common-macros-for-python-3-rpms) {#common-macros-for-python-3-rpms .title}

In a Python RPM `spec`{.literal} file, always use the macros for Python 3 RPMs rather than hardcoding their values.

You can redefine which Python 3 version is used in these macros. To do so, define the `python3_pkgversion`{.literal} macro at the top of your `spec`{.literal} file. For more information, see [A `spec`{.literal} file description for an example Python package](#a-spec-file-description-for-an-example-python-package "7.1. A spec file description for an example Python package"). If you define the `python3_pkgversion`{.literal} macro, the macro values in the following table match that Python 3 version.

+-----------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Macro                 | Normal Definition                   | Description                                                                                                                                                                        |
+:======================+:====================================+:===================================================================================================================================================================================+
| %{python3_pkgversion} | 3                                   | The Python version that is used by all other macros. Redefine this macro when you build for a different Python version than the default.                                           |
+-----------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| %{python3}            | /usr/bin/python3                    | The Python 3 interpreter.                                                                                                                                                          |
+-----------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| %{python3_version}    | 3.12                                | The major.minor version of the Python 3 interpreter.                                                                                                                               |
+-----------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| %{python3_sitelib}    | /usr/lib/python3.12/site-packages   | The location where pure-Python modules are installed.                                                                                                                              |
+-----------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| %{python3_sitearch}   | /usr/lib64/python3.12/site-packages | The location where modules containing architecture-specific extension modules are installed.                                                                                       |
+-----------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| %py3_build            |                                     | Expands to the `setup.py build`{.literal .command} command with arguments suitable for an RPM package.                                                                             |
+-----------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| %py3_install          |                                     | Expands to the `setup.py install`{.literal .command} command with arguments suitable for an RPM package.                                                                           |
+-----------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| %{py3_shebang_flags}  | sP                                  | The default set of flags for the Python interpreter directives macro, `%py3_shebang_fix`{.literal}.                                                                                |
+-----------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| %py3_shebang_fix      |                                     | Changes Python interpreter directives to `#! %{python3}`{.literal}, preserves any existing flags (if found), and adds flags defined in the `%{py3_shebang_flags}`{.literal} macro. |
+-----------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 7.1. Macros for Python 3 RPMs

Show more

**Additional resources**

-   [Python macros in upstream documentation](https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_201x/#_macros)

### [7.3. Using automatically generated dependencies for Python RPMs](#using-automatically-generated-dependencies-for-python-rpms) {#using-automatically-generated-dependencies-for-python-rpms .title}

Enable automatic generation of dependencies for Python RPMs by using upstream-provided metadata.

**Prerequisites**

-   A `spec`{.literal} file for the RPM exists. For more information, see [A `spec`{.literal} file description for an example Python package](#a-spec-file-description-for-an-example-python-package "7.1. A spec file description for an example Python package").

**Procedure**

1.  Include one of the following directories in the resulting RPM:

    -   `.dist-info`{.literal}

    -   `.egg-info`{.literal}

        The RPM build process automatically generates virtual `pythonX.Ydist`{.literal} provides from these directories, for example:

        ``` {.language-plaintext tabindex="-1"}
        python3.12dist(pello)
        ```

        The Python dependency generator then reads the upstream metadata and generates runtime requirements for each RPM package using the generated `pythonX.Ydist`{.literal} virtual provides. Example of a generated requirements tag:

        ``` {.language-plaintext tabindex="-1"}
        Requires: python3.12dist(requests)
        ```

2.  Inspect the generated `Requires`{.literal}.

3.  To remove some of the generated `Requires`{.literal}, modify the upstream-provided metadata in the `%prep`{.literal} section of the `spec`{.literal} file.

4.  To disable the automatic requirements generator, include the `%{?python_disable_dependency_generator}`{.literal} macro immediately before the main package's `%description`{.literal} declaration.

**Additional resources**

-   [Automatically generated dependencies](https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_201x/#_automatically_generated_dependencies)

### [7.4. Packaging Python projects with pyproject RPM macros](#packaging-python-projects-with-pyproject-rpm-macros) {#packaging-python-projects-with-pyproject-rpm-macros .title}

Package Python projects that use a `pyproject.toml`{.literal} or a `setup.py`{.literal} file into RPM packages by using `pyproject`{.literal} RPM macros from the CodeReady Linux Builder (CRB) repository.

#### [7.4.1. pyproject RPM macros for Python packaging](#pyproject-rpm-macros-for-python-packaging) {#pyproject-rpm-macros-for-python-packaging .title}

Package Python projects into RPM packages by using `pyproject`{.literal} RPM macros. These macros work with projects that define metadata in `setup.py`{.literal}, `pyproject.toml`{.literal}, or both, and invoke a standards-based build backend through a standardized protocol.

Many upstream Python projects no longer rely on a `setup.py`{.literal} script. Instead, they store project metadata in `pyproject.toml`{.literal} and use a build backend, such as `setuptools`{.literal}, `flit-core`{.literal}, `hatchling`{.literal}, or `poetry-core`{.literal}. The `pyproject`{.literal} RPM macros invoke any compliant build backend through a standardized protocol instead of calling `setup.py`{.literal} directly.

The `pyproject`{.literal} RPM macros reuse upstream metadata whenever possible. For example, they can generate `BuildRequires`{.literal} from the build-system requirements in `pyproject.toml`{.literal} instead of listing the same dependencies manually in the `spec`{.literal} file.

The `pyproject-rpm-macros`{.literal} package is available in the CodeReady Linux Builder (CRB) repository. The `%pyproject_buildrequires`{.literal} macro adds a generated `BuildRequires`{.literal} on that package during package builds. CRB content is unsupported by Red Hat. The macros are updated as needed to follow emerging Python packaging standards.

Use `pyproject`{.literal} RPM macros to package Python projects, whether the upstream project defines metadata in `setup.py`{.literal}, `pyproject.toml`{.literal}, or both.

#### [7.4.2. Preparing to use pyproject RPM macros](#preparing-to-use-pyproject-rpm-macros) {#preparing-to-use-pyproject-rpm-macros .title}

To package Python projects with pyproject RPM macros, enable the CodeReady Linux Builder (CRB) repository on the build host and configure `%pyproject_buildrequires`{.literal} in your RPM spec file.

Important

Red Hat does not support content in the CodeReady Linux Builder repository.

**Prerequisites**

-   You have root permissions on the build host.
-   The system is registered with Red Hat Subscription Manager.

**Procedure**

1.  Enable the CodeReady Linux Builder repository on the build host:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable codeready-builder-for-rhel-10-x86_64-rpms
    ```

2.  In the RPM `spec`{.literal} file, add `BuildRequires: python3-devel`{.literal} and use the `%pyproject_buildrequires`{.literal} macro in the `%generate_buildrequires`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    BuildRequires: python3-devel

    %generate_buildrequires
    %pyproject_buildrequires
    ```

#### [7.4.3. Common pyproject RPM macros for Python 3 RPMs](#common-pyproject-rpm-macros-for-python-3-rpms) {#common-pyproject-rpm-macros-for-python-3-rpms .title}

In a Python RPM `spec`{.literal} file, use `pyproject`{.literal} RPM macros to build projects that define metadata in `setup.py`{.literal}, `pyproject.toml`{.literal}, or both.

You can redefine which Python 3 version the macros use by defining the `python3_pkgversion`{.literal} macro at the top of your `spec`{.literal} file, for example `%global python3_pkgversion 3.14`{.literal}. Omit this macro to build for the default Python 3 version.

Place `%pyproject_buildrequires`{.literal} in the `%generate_buildrequires`{.literal} section of the `spec`{.literal} file. RPM runs the macro in that section to generate build requirements from upstream metadata before the build starts.

+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Macro                    | Description                                                                                                                                       |
+:=========================+:==================================================================================================================================================+
| %pyproject_buildrequires | Expands build requirements from upstream metadata. Use options such as `-g test`{.literal} to include dependencies from a named dependency group. |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| %pyproject_wheel         | Builds a wheel package by using the upstream-specified build backend.                                                                             |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| %pyproject_install       | Installs the built wheel package into the build root.                                                                                             |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| %pyproject_save_files    | Saves the list of installed files for use in the `%files`{.literal} section. Use `-l`{.literal} to assert that a license file is found.           |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| %pyproject_check_import  | Verifies that the installed package can be imported during the `%check`{.literal} section.                                                        |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| %pyproject_files         | Expands to the file list saved by `%pyproject_save_files`{.literal}. Use it with the `-f`{.literal} option in the `%files`{.literal} section.     |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 7.2. Common pyproject RPM macros for Python 3 RPMs

Show more

The table lists commonly used macros. For all macros and their options, see the `/usr/share/doc/pyproject-rpm-macros/README.md`{.literal} file provided by the `pyproject-rpm-macros`{.literal} package.

#### [7.4.4. A spec file description for a Python package with pyproject RPM macros](#a-spec-file-description-for-a-python-package-with-pyproject-rpm-macros) {#a-spec-file-description-for-a-python-package-with-pyproject-rpm-macros .title}

Use an annotated RPM `spec`{.literal} file example to package a Python project that defines metadata in `setup.py`{.literal}, `pyproject.toml`{.literal}, or both. The example shows `pyproject`{.literal} RPM macros for build requirements, wheel builds, installation, and automated file lists.

**Example 7.2. An example `spec`{.literal} file for a Python library built with pyproject RPM macros**

``` {.language-plaintext tabindex="-1"}
Name:           python-pello
Version:        1.0.2
Release:        1%{?dist}
Summary:        Example Python library

License:        MIT
URL:            https://example.com/Pello
Source:         %{url}/archive/v%{version}/Pello-%{version}.tar.gz

BuildArch:      noarch

%description %_description
Pello is an example package with an executable that prints Hello World! on the command line.

%package -n python3-pello
Summary:        %{summary}

%description -n python3-pello
Pello is an example package with an executable that prints Hello World! on the command line.

%prep
%autosetup -p1 -n Pello-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pello

%check
%pyproject_check_import
%pytest

%files -n python3-pello -f %{pyproject_files}
```

-   The `%pyproject_buildrequires`{.literal} macro in the `%generate_buildrequires`{.literal} section creates build requirements from upstream metadata.
-   The `%pyproject_wheel`{.literal} macro builds a wheel package by using the upstream-specified build backend.
-   The `%pyproject_install`{.literal} macro installs the wheel into the build root.
-   The `%pyproject_save_files -l pello`{.literal} macro records installed files. The `-l`{.literal} option verifies that a license file is present. The `pello`{.literal} argument lists the importable module named `pello`{.literal}.
-   The `%check`{.literal} section runs `%pyproject_check_import`{.literal} to verify importability and `%pytest`{.literal} to run tests.
-   The `%files`{.literal} section uses `-f %{pyproject_files}`{.literal} to include the file list generated by `%pyproject_save_files`{.literal}.

For commonly used macros, see [Common pyproject RPM macros for Python 3 RPMs](#common-pyproject-rpm-macros-for-python-3-rpms "7.4.3. Common pyproject RPM macros for Python 3 RPMs"). For all macros and their options, see the `/usr/share/doc/pyproject-rpm-macros/README.md`{.literal} file provided by the `pyproject-rpm-macros`{.literal} package.

**Additional resources**

-   [Installing additional Python 3 tools for developers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/installing_and_using_dynamic_programming_languages/index#installing-additional-python-3-tools-for-developers)
-   [Using automatically generated dependencies for Python RPMs](#using-automatically-generated-dependencies-for-python-rpms "7.3. Using automatically generated dependencies for Python RPMs")
-   [How to enable and make use of content within CodeReady Linux Builder](https://access.redhat.com/articles/4348511)

## [Chapter 8. Modifying interpreter directives in Python scripts](#modifying-interpreter-directives-in-python-scripts) {#chapter-8.-modifying-interpreter-directives-in-python-scripts .title}

Modify the packaged Python scripts so that they conform to the expected format.

In Red Hat Enterprise Linux (RHEL) 10, executable Python scripts are expected to use interpreter directives, also known as hashbangs or shebangs, that explicitly specify at a minimum the major Python version. For example:

``` {.language-plaintext tabindex="-1"}
#!/usr/bin/python3
#!/usr/bin/python3.12
```

The `/usr/lib/rpm/redhat/brp-mangle-shebangs`{.literal} `buildroot`{.literal} policy (BRP) script is run automatically when building any RPM package, and attempts to correct interpreter directives in all executable files. The BRP script generates errors when encountering a Python script with an ambiguous interpreter directive, for example, `#!/usr/bin/python`{.literal} or `#!/usr/bin/env python`{.literal}.

**Prerequisites**

-   Some of the interpreter directives in your Python scripts cause a build error.

**Procedure**

-   Depending on your scenario, modify interpreter directives by performing one of the following steps:

    -   Use the following macro in the `%prep`{.literal} section of your `spec`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        %py3_shebang_fix <SCRIPTNAME> ...
        ```

        *SCRIPTNAME* can be any file, directory, or a list of files and directories.

        As a result, all listed files and all `.py`{.literal} files in listed directories have their interpreter directives modified to point to `%{python3}`{.literal}. Existing flags from the original interpreter directive will be preserved and additional flags defined in the `%{py3_shebang_flags}`{.literal} macro will be added. You can redefine the `%{py3_shebang_flags}`{.literal} macro in your `spec`{.literal} file to change the flags that will be added.

    -   Modify the packaged Python scripts so that they conform to the expected format.

**Additional resources**

-   [Interpreter invocation](https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_interpreter_invocation)

## [Chapter 9. Packaging Ruby gems](#packaging-ruby-gems) {#chapter-9.-packaging-ruby-gems .title}

Package Ruby projects as RPM files.

Ruby is an interpreted general-purpose programming language. Programs written in Ruby are typically packaged by using the RubyGems software, which provides a specific Ruby packaging format.

Packages created by RubyGems are called gems. You can re-package gems into RPM packages.

Note

This documentation refers to terms related to the RubyGems concept with the `gem`{.literal} prefix, for example, `.gemspec`{.literal} is used for the *gem specification*, and terms related to RPM are unqualified.

### [9.1. How RubyGems relate to RPM](#how-rubygems-relate-to-rpm) {#how-rubygems-relate-to-rpm .title}

RubyGems use metadata similar to RPM packages. You can re-package gems into RPMs to seamlessly integrate them with Red Hat Enterprise Linux (RHEL).

RubyGems represent the native packaging format for the Ruby programming language. This format shares terminology with RPM packages, such as `spec`{.literal} files, package names, and dependencies. By re-packaging gems into RPM packages, you can satisfy system dependencies by installing the packaged gem.

To conform with the rest of the RHEL distribution, packages created by RubyGems must comply with specific rules:

-   Package names must follow the `rubygem-%{gem_name}`{.literal} pattern.
-   The interpreter directive must use the `#!/usr/bin/ruby`{.literal} string.

### [9.2. RubyGems spec file conventions](#rubygems-spec-file-conventions) {#rubygems-spec-file-conventions .title}

Review an example RubyGems `spec`{.literal} file structure and specifics that you must follow when creating such `spec`{.literal} file.

The RubyGems `spec`{.literal} file must meet the following conventions:

-   The file contains a definition of `%{gem_name}`{.literal}, which is the name from the gem's specification.

-   The source of the package must be the full URL to the released gem archive.

-   The version of the package must be the gem's version.

-   The file contains the following `BuildRequires:`{.literal} directive:

    ``` {.language-plaintext tabindex="-1"}
    BuildRequires: rubygems-devel
    ```

    The `rubygems-devel`{.literal} package contains macros needed for a build.

-   The file does not contain any additional `rubygem(foo)`{.literal} `Requires`{.literal} or `Provides`{.literal} directives because these directives are autogenerated from the gem metadata.

#### [9.2.1. RubyGems spec file example](#rubygems-spec-file-example) {#rubygems-spec-file-example .title}

Review the details of the following RubyGems-specific part of an example `spec`{.literal} file for building gems. Note that the remaining part of the `spec`{.literal} file follows the generic `spec`{.literal} file guidelines.

**Example 9.1. A RubyGems-specific part of an example spec file**

``` {.language-plaintext tabindex="-1"}
%prep
%setup -q -n  %{gem_name}-%{version}

# Modify the gemspec if necessary
# Also apply patches to code if necessary
%patch 0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# If there were programs installed:
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

# If there are C extensions, copy them to the extdir.
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
```

#### [9.2.2. RubyGems spec file directives](#rubygems-spec-file-directives) {#rubygems-spec-file-directives .title}

Review the following specifics of particular items in the RubyGems-specific part of the `spec`{.literal} file.

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Directive            | RubyGems specifics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+:=====================+:============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `%prep`{.literal}    | RPM can directly unpack gem archives. The `%setup -n %{gem_name}-%{version}`{.literal} macro provides the directory into which the gem is unpacked. At the same directory level, the `%{gem_name}-%{version}.gemspec`{.literal} file is automatically created. You can use this file to perform the following actions:                                                                                                                                                                                                                                      |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                      | -   Modify the `.gemspec`{.literal} file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      | -   Apply patches to the code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%build`{.literal}   | This section includes commands for building the software into machine code. The `%gem_install`{.literal} macro operates only on gem archives. Therefore, you must first re-create the archive by using the `gem build ../%{gem_name}-%{version}.gemspec`{.literal} command. The recreated gem file is then used by `%gem_install`{.literal} to build and install the gem code into the default `./%{gem_dir}`{.literal} temporary directory. Before being installed, the built sources are placed into a temporary directory that is created automatically. |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%install`{.literal} | The installation is performed into the `%{buildroot}`{.literal} hierarchy. You can create the necessary directories and then copy the installed code from the temporary directories into the `%{buildroot}`{.literal} hierarchy. If the gem creates shared objects, they are moved into the architecture-specific `%{gem_extdir_mri}`{.literal} path.                                                                                                                                                                                                       |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.1. RubyGems\' spec directives specifics

Show more

#### [9.2.3. Additional resources](#rubygems-spec-file-conventions_923-additional-resources) {#additional-resources-1 .title}

-   [Fedora packaging guidelines for Ruby](https://docs.fedoraproject.org/en-US/packaging-guidelines/Ruby/)

### [9.3. RubyGems macros](#rubygems-macros) {#rubygems-macros .title}

Review the following macros useful for packages created by RubyGems. These macros are provided by the `rubygems-devel`{.literal} package.

+-------------------------------+----------------------------------------------------------------------+-----------------------------------------------+
| Macro name                    | Extended path                                                        | Usage                                         |
+:==============================+:=====================================================================+:==============================================+
| `%{gem_dir}`{.literal}        | `/usr/share/gems`{.literal}                                          | Top directory for the gem structure.          |
+-------------------------------+----------------------------------------------------------------------+-----------------------------------------------+
| `%{gem_instdir}`{.literal}    | `%{gem_dir}/gems/%{gem_name}-%{version}`{.literal}                   | Directory with the actual content of the gem. |
+-------------------------------+----------------------------------------------------------------------+-----------------------------------------------+
| `%{gem_libdir}`{.literal}     | `%{gem_instdir}/lib`{.literal}                                       | The library directory of the gem.             |
+-------------------------------+----------------------------------------------------------------------+-----------------------------------------------+
| `%{gem_cache}`{.literal}      | `%{gem_dir}/cache/%{gem_name}-%{version}.gem`{.literal}              | The cached gem.                               |
+-------------------------------+----------------------------------------------------------------------+-----------------------------------------------+
| `%{gem_spec}`{.literal}       | `%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec`{.literal} | The gem specification file.                   |
+-------------------------------+----------------------------------------------------------------------+-----------------------------------------------+
| `%{gem_docdir}`{.literal}     | `%{gem_dir}/doc/%{gem_name}-%{version}`{.literal}                    | The RDoc documentation of the gem.            |
+-------------------------------+----------------------------------------------------------------------+-----------------------------------------------+
| `%{gem_extdir_mri}`{.literal} | `%{_libdir}/gems/ruby/%{gem_name}-%{version}`{.literal}              | The directory for gem extension.              |
+-------------------------------+----------------------------------------------------------------------+-----------------------------------------------+

: Table 9.2. RubyGems\' macros

Show more

### [9.4. Using gem2rpm to generate a spec file](#using-gem2rpm) {#using-gem2rpm-to-generate-a-spec-file .title}

Create an RPM `spec`{.literal} file for building gems by using the `gem2rpm`{.literal} utility.

#### [9.4.1. Creating an RPM spec file for a Ruby gem](#creating-spec-with-gem2rpm) {#creating-an-rpm-spec-file-for-a-ruby-gem .title}

Generate an RPM `spec`{.literal} file for a RubyGems package by using the `gem2rpm`{.literal} utility.

**Prerequisites**

-   You have the `gem2rpm`{.literal} utility installed on your system:

    ``` {.language-plaintext tabindex="-1"}
    $ gem install gem2rpm
    ```

**Procedure**

1.  Download a gem in its latest version and generate the RPM `spec`{.literal} file for this gem:

    ``` {.language-plaintext tabindex="-1"}
    $ gem2rpm --fetch <gem_name> > <gem_name>.spec
    ```

2.  Edit the generated `spec`{.literal} file to add the missing information, for example, a license and a changelog.

**Additional resources**

-   [Building RPMs](#building-rpms "6.5. Building RPMs")

#### [9.4.2. Using custom gem2rpm templates to generate a spec file](#using-custom-gem2rpm-templates-to-generate-spec) {#using-custom-gem2rpm-templates-to-generate-a-spec-file .title}

`gem2rpm`{.literal} templates are standard [Embedded Ruby (ERB)](https://docs.ruby-lang.org/en/3.3/ERB.html) files that RPM `spec`{.literal} files can be generated from. Edit the template from which the RPM `spec`{.literal} file is generated instead of editing the generated `spec`{.literal} file.

**Prerequisites**

-   You have the `gem2rpm`{.literal} utility installed on your system:

    ``` {.language-plaintext tabindex="-1"}
    $ gem install gem2rpm
    ```

**Procedure**

1.  Display all `gem2rpm`{.literal} built-in templates:

    ``` {.language-plaintext tabindex="-1"}
    $ gem2rpm --templates
    ```

2.  Select one of the built-in templates and save it as a custom template:

    ``` {.language-plaintext tabindex="-1"}
    $ gem2rpm -t <template> -T > rubygem-<gem_name>.spec.template
    ```

    Note that for RHEL 10 Beta, the `fedora-27-rawhide`{.literal} template is recommended.

3.  Edit the template as needed. For more information, see [gem2rpm template variables](#gem2rpm-template-variables "9.4.3. gem2rpm template variables").

4.  Generate the `spec`{.literal} file by using the edited template:

    ``` {.language-plaintext tabindex="-1"}
    $ gem2rpm -t rubygem-<gem_name>.spec.template <gem_name>-<latest_version>.gem > <gem_name>-GEM.spec
    ```

**Additional resources**

-   [Building RPMs](#building-rpms "6.5. Building RPMs")

#### [9.4.3. gem2rpm template variables](#gem2rpm-template-variables) {#gem2rpm-template-variables .title}

Review the following variables included in the `gem2rpm`{.literal} template for RPM `spec`{.literal} file generation.

+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Variable                             | Explanation                                                                                                                          |
+:=====================================+:=====================================================================================================================================+
| `package`{.literal}                  | The `Gem::Package`{.literal} variable for the gem.                                                                                   |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| `spec`{.literal}                     | The `Gem::Specification`{.literal} variable for the gem (the same as `format.spec`{.literal}).                                       |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| `config`{.literal}                   | The `Gem2Rpm::Configuration`{.literal} variable that can redefine default macros or rules used in `spec`{.literal} template helpers. |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| `runtime_dependencies`{.literal}     | The `Gem2Rpm::RpmDependencyList`{.literal} variable that provides a list of package runtime dependencies.                            |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| `development_dependencies`{.literal} | The `Gem2Rpm::RpmDependencyList`{.literal} variable that provides a list of package development dependencies.                        |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| `tests`{.literal}                    | The `Gem2Rpm::TestSuite`{.literal} variable that provides a list of test frameworks allowing their execution.                        |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| `files`{.literal}                    | The `Gem2Rpm::RpmFileList`{.literal} variable that provides an unfiltered list of files in a package.                                |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| `main_files`{.literal}               | The `Gem2Rpm::RpmFileList`{.literal} variable that provides a list of files suitable for the main package.                           |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| `doc_files`{.literal}                | The `Gem2Rpm::RpmFileList`{.literal} variable that provides a list of files suitable for the `-doc`{.literal} subpackage.            |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.3. Variables in the gem2rpm template

Show more

## [Legal Notice](#idm139736916204400) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
