---
{"title": "Installing and using dynamic programming languages", "guide": "installing_and_using_dynamic_programming_languages", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/installing_and_using_dynamic_programming_languages/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Installing and using dynamic programming languages {#installing-and-using-dynamic-programming-languages .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Installing and using Python and PHP in Red Hat Enterprise Linux 10 {#installing-and-using-python-and-php-in-red-hat-enterprise-linux-10 .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139798033256144)

**Abstract**

Install and use Python 3. Install the PHP scripting language, use PHP with the Apache HTTP Server or the nginx web server, and run a PHP script from a command-line interface.

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

## [Chapter 1. Installing and using Python](#installing-and-using-python) {#chapter-1.-installing-and-using-python .title}

Python is a high-level programming language that supports multiple programming paradigms, such as object-oriented, imperative, functional, and procedural paradigms. Python has dynamic semantics and can be used for general-purpose programming.

Many installed packages on Red Hat Enterprise Linux are written in Python. Examples include packages for system tools, data analysis, and web applications. To use these packages, you must have the `python*`{.literal} packages installed.

### [1.1. Python versions](#python-versions) {#python-versions .title}

To select the appropriate environment for developing and running your applications, review Python versions available in Red Hat Enterprise Linux (RHEL) 10.

Python 3.12 is the default Python implementation in RHEL 10. Python 3.12 is distributed in a non-modular `python3`{.literal} RPM package in the BaseOS repository and is usually installed by default. Python 3.12 will be supported for the whole life cycle of RHEL 10.

Additional versions of Python 3 will be distributed as non-modular RPM packages with a shorter life cycle through the AppStream repository in minor RHEL 10 releases. You will be able to install these additional Python 3 versions in parallel with Python 3.12.

The unversioned `python`{.literal} command points to the default Python 3.12 version.

**Additional resources**

-   [Red Hat Enterprise Linux Life Cycle](https://access.redhat.com/support/policy/updates/errata)
-   [Red Hat Enterprise Linux Application Streams Life Cycle](https://access.redhat.com/support/policy/updates/rhel-app-streams-life-cycle)

### [1.2. Installing Python 3](#installing-python-3) {#installing-python-3 .title}

To develop and run Python applications, install Python 3 on your RHEL 10 system. The default Python implementation is usually installed by default. However, you can also install it manually.

**Procedure**

-   To install Python 3.12, enter:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install python3
    ```

**Verification**

-   Verify the Python version installed on your system:

    ``` {.language-plaintext tabindex="-1"}
    $ python3 --version
    ```

### [1.3. Installing additional Python 3 packages](#installing-additional-python-3-packages) {#installing-additional-python-3-packages .title}

To extend the capabilities of your applications and scripts, install additional Python 3 packages on your RHEL 10 system. Packages prefixed with `python3-`{.literal} contain add-on modules for the default Python 3.12 version.

**Procedure**

-   To install, for example, the `Requests`{.literal} module for Python 3.12, enter:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install python3-requests
    ```

-   To install the `pip`{.literal} package installer from Python 3.12, enter:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install python3-pip
    ```

**Additional resources**

-   [Upstream documentation about Python add-on modules](https://docs.python.org/3/tutorial/modules.html)

### [1.4. Installing additional Python 3 tools for developers](#installing-additional-python-3-tools-for-developers) {#installing-additional-python-3-tools-for-developers .title}

To get additional Python tools for developers, use the CodeReady Linux Builder (CRB) repository. Install the `python3`{.literal} packages that provide the tools you need.

Important

The content in the CodeReady Linux Builder repository is unsupported by Red Hat.

The CRB repository contains, for example, the following packages:

-   `python3-pytest`{.literal}
-   `python3-idle`{.literal}
-   `python3-debug`{.literal}
-   `python3-cython`{.literal}

Note

Not all upstream Python-related packages are available in RHEL.

**Procedure**

1.  Enable the CodeReady Linux Builder repository:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable codeready-builder-for-rhel-10-x86_64-rpms
    ```

2.  Install, for example, the `python3-cython`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install python3-cython
    ```

**Additional resources**

-   [How to enable and make use of content within CodeReady Linux Builder](https://access.redhat.com/articles/4348511)

### [1.5. Using Python](#using-python) {#using-python .title}

To install or interact with packages providing system tools, tools for data analysis, or web applications written in Python, run the Python interpreter or Python-related commands.

**Prerequisites**

-   Python is installed.

-   If you want to download and install third-party applications, install the `python3-pip`{.literal} package.

    Warning

    Installing Python packages with `pip`{.literal} as the root user places files in system locations. This can override RHEL libraries and might cause system instability or conflicts with supported packages. Red Hat does not support software installed by using `pip`{.literal} at the system level. To avoid these issues, use `pip`{.literal} within a virtual environment or install packages as a non-root user with the `--user`{.literal} option.

**Procedure**

-   To run the Python 3.12 interpreter or related commands, use, for example, the following commands:

    ``` {.language-plaintext tabindex="-1"}
    $ python3
    $ python3 -m venv --help
    $ python3 -m pip install <package>
    $ pip3 install <package>
    ```

### [1.6. Additional resources](#installing-and-using-python_16-additional-resources) {#additional-resources .title}

-   [Changing the python3 interpreter on RHEL](#changing-the-python3-interpreter-on-rhel "Chapter 2. Changing the python3 interpreter on RHEL")
-   [Packaging Python 3 RPMs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/installing_and_using_dynamic_programming_languages/index#packaging-python-3-rpm)
-   [Modifying interpreter directives in Python scripts](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/packaging_and_distributing_software/modifying-interpreter-directives-in-python-scripts)

## [Chapter 2. Changing the python3 interpreter on RHEL](#changing-the-python3-interpreter-on-rhel) {#chapter-2.-changing-the-python3-interpreter-on-rhel .title}

Run a specific Python version with `python3`{.literal} or `python`{.literal} without changing the system Python interpreter.

### [2.1. System Python on RHEL](#system-python-on-rhel) {#system-python-on-rhel .title}

Core Red Hat Enterprise Linux tools depend on the system Python version that ships with the operating system. Do not change the system default Python interpreter at `/usr/bin/python3`{.literal}.

Many installed packages and system utilities are tightly coupled with the tested system Python. For example, Dandified YUM (DNF), the package manager that installs and updates software on Red Hat Enterprise Linux, is a Python application. Changing the system default Python environment can break DNF and leave the system unable to manage packages.

Other critical components, including firewall managers, system initializers, and printer drivers, also rely on the default system Python. An unsupported change can cause these tools to fail without warning.

On Red Hat Enterprise Linux 9 and later, use of the `alternatives`{.literal} command to change the system `python3`{.literal} interpreter is unsupported. To run a different Python version when you enter `python3`{.literal} or `python`{.literal}, create a symbolic link in a directory that appears earlier in your `PATH`{.literal} environment variable. This approach does not modify system packages, nor affects other users when you configure a user-specific link.

### [2.2. Changing the python3 interpreter by using symbolic links](#changing-the-python3-interpreter-by-using-symbolic-links) {#changing-the-python3-interpreter-by-using-symbolic-links .title}

Point the `python3`{.literal} or `python`{.literal} command to a specific Python interpreter by creating a symbolic link in `/usr/local/bin/`{.literal} or `~/.local/bin/`{.literal}.

**Prerequisites**

-   The Python interpreter you want to use is installed on the system. For example, `/usr/bin/python3.14`{.literal} from the AppStream repository.
-   You have root permissions on your system to create symbolic links.
-   Your `~/.local/bin/`{.literal} directory exists, or you can create it.

**Procedure**

-   To install the Python version, for example, Python 3.14, run:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install python3.14
    ```

-   Create a symbolic link for the `python3`{.literal} command, use one of the following options.

    -   For all users on the system, create a symbolic link in `/usr/local/bin/`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # ln -s /usr/bin/python3.14 /usr/local/bin/python3
        ```

    -   For your user account only, create the `~/.local/bin/`{.literal} directory if it does not exist and add a symbolic link:

        ``` {.language-plaintext tabindex="-1"}
        $ mkdir -p ~/.local/bin
        ```

        ``` {.language-plaintext tabindex="-1"}
        $ ln -s /usr/bin/python3.14 ~/.local/bin/python3
        ```

-   To create a symbolic link for the unversioned `python`{.literal} command, use one of the following options.

    -   For all users on the system, run:

        ``` {.language-plaintext tabindex="-1"}
        # ln -s /usr/bin/python3.14 /usr/local/bin/python
        ```

    -   For your user account only, run:

        ``` {.language-plaintext tabindex="-1"}
        $ ln -s /usr/bin/python3.14 ~/.local/bin/python
        ```

-   To remove the override, delete the symbolic link, use one of the following options.

    -   For a system-wide override, run:

        ``` {.language-plaintext tabindex="-1"}
        # rm /usr/local/bin/python3
        ```

    -   For a user-specific override, run:

        ``` {.language-plaintext tabindex="-1"}
        $ rm ~/.local/bin/python3
        ```

**Verification**

1.  Verify that the `python3`{.literal} command resolves to your chosen interpreter:

    ``` {.language-plaintext tabindex="-1"}
    $ python3 --version
    ```

    ``` {.language-plaintext tabindex="-1"}
    Python <version>
    ```

2.  Verify the symbolic link:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -l /usr/local/bin/python3
    ```

    ``` {.language-plaintext tabindex="-1"}
    lrwxrwxrwx. 1 root root 19 Jun 23 09:06 /usr/local/bin/python3 -> /usr/bin/python3.14
    ```

3.  Verify that `/usr/local/bin/`{.literal} or `~/.local/bin/`{.literal} appears before `/usr/bin/`{.literal} in your `PATH`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ echo $PATH
    ```

    ``` {.language-plaintext tabindex="-1"}
    /home/user/.local/bin:/home/user/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin
    ```

### [2.3. Using env in Python interpreter directives](#using-env-in-python-interpreter-directives) {#using-env-in-python-interpreter-directives .title}

Start Python scripts with `#!/usr/bin/env python3`{.literal} to run the first `python3`{.literal} command in `PATH`{.literal}.

A hard-coded interpreter directive such as `#!/usr/bin/python3`{.literal} always uses the system Python at `/usr/bin/python3`{.literal}. This interpreter does not use symbolic links in `/usr/local/bin/`{.literal} and `~/.local/bin/`{.literal}, or a Python interpreter from a virtual environment.

When you start a script with `#!/usr/bin/env python3`{.literal}, the `env`{.literal} utility searches the `PATH`{.literal} variable and runs the first matching `python3`{.literal} executable. This follows a system-wide or user-specific symbolic link and supports virtual environments when their `bin`{.literal} directory is first in `PATH`{.literal}.

Use the same approach with the unversioned `python`{.literal} command when your script must run with `#!/usr/bin/env python`{.literal}.

When you package Python scripts as RPM packages, interpreter directives must meet packaging requirements.

**Additional resources**

-   [Python versions](#python-versions "1.1. Python versions")
-   [Installing Python 3](#installing-python-3 "1.2. Installing Python 3")
-   [Using Python](#using-python "1.5. Using Python")
-   [Modifying interpreter directives in Python scripts](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/packaging_and_distributing_software/modifying-interpreter-directives-in-python-scripts)
-   [How to change the meaning of python and python3 on RHEL](https://developers.redhat.com/articles/2025/09/30/how-change-meaning-python-and-python3-rhel)

## [Chapter 3. Packaging Python 3 RPMs](#packaging-python-3-rpms) {#chapter-3.-packaging-python-3-rpms .title}

You can install Python packages on your system by using the DNF package manager. DNF uses the RPM package format, which offers more downstream control over the software.

Packaging a Python project into an RPM package provides the following advantages compared to native Python packages:

-   Dependencies on Python and non-Python packages are possible and strictly enforced by the DNF package manager.
-   You can cryptographically sign the packages. With cryptographic signing, you can verify, integrate, and test contents of RPM packages with the rest of the operating system.
-   You can run tests during the build process.

The packaging format of native Python packages follows the specifications published by the Python Packaging Authority (PyPA). Historically, most Python projects used the `distutils`{.literal} or `setuptools`{.literal} utilities for packaging and defined package information in the `setup.py`{.literal} file. However, options for creating native Python packages have evolved over time:

To package Python software, whether the project uses `setup.py`{.literal} or `pyproject.toml`{.literal}, use pyproject RPM macros from the `pyproject-rpm-macros`{.literal} package.

### [3.1. A spec file description for an example Python package](#a-spec-file-description-for-an-example-python-package) {#a-spec-file-description-for-an-example-python-package .title}

Review the notes about Python RPM `spec`{.literal} file specifics in the following example of the `python3-pello`{.literal} package.

The RPM `spec`{.literal} file for Python projects has some specifics compared to non-Python RPM `spec`{.literal} files. For example, it is recommended for any RPM package name of a Python library to include the `python3-`{.literal} prefix.

**Example 3.1. An example `spec`{.literal} file for the program written in Python**

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

    Using the `setup.py build`{.literal} and `setup.py install`{.literal} commands from the `setuptools`{.literal} package is deprecated. For modern projects, use the `pyproject`{.literal} RPM macros from the `pyproject-rpm-macros`{.literal} package. For more information, see [Packaging Python projects with pyproject RPM macros](#packaging-python-projects-with-pyproject-rpm-macros "3.4. Packaging Python projects with pyproject RPM macros").

-   The `%check`{.literal} section runs the tests of the packaged project. The exact command depends on the project itself, but you can use the `%pytest`{.literal} macro to run the `pytest`{.literal} command in an RPM-friendly way.

### [3.2. Common macros for Python 3 RPMs](#common-macros-for-python-3-rpms) {#common-macros-for-python-3-rpms .title}

In a Python RPM `spec`{.literal} file, always use the macros for Python 3 RPMs rather than hardcoding their values.

You can redefine which Python 3 version is used in these macros. To do so, define the `python3_pkgversion`{.literal} macro at the top of your `spec`{.literal} file. For more information, see [A `spec`{.literal} file description for an example Python package](#a-spec-file-description-for-an-example-python-package "3.1. A spec file description for an example Python package"). If you define the `python3_pkgversion`{.literal} macro, the macro values in the following table match that Python 3 version.

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

: Table 3.1. Macros for Python 3 RPMs

Show more

**Additional resources**

-   [Python macros in upstream documentation](https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_201x/#_macros)

### [3.3. Using automatically generated dependencies for Python RPMs](#using-automatically-generated-dependencies-for-python-rpms) {#using-automatically-generated-dependencies-for-python-rpms .title}

Enable automatic generation of dependencies for Python RPMs by using upstream-provided metadata.

**Prerequisites**

-   A `spec`{.literal} file for the RPM exists. For more information, see [A `spec`{.literal} file description for an example Python package](#a-spec-file-description-for-an-example-python-package "3.1. A spec file description for an example Python package").

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

### [3.4. Packaging Python projects with pyproject RPM macros](#packaging-python-projects-with-pyproject-rpm-macros) {#packaging-python-projects-with-pyproject-rpm-macros .title}

Package Python projects that use a `pyproject.toml`{.literal} or a `setup.py`{.literal} file into RPM packages by using `pyproject`{.literal} RPM macros from the CodeReady Linux Builder (CRB) repository.

#### [3.4.1. pyproject RPM macros for Python packaging](#pyproject-rpm-macros-for-python-packaging) {#pyproject-rpm-macros-for-python-packaging .title}

Package Python projects into RPM packages by using `pyproject`{.literal} RPM macros. These macros work with projects that define metadata in `setup.py`{.literal}, `pyproject.toml`{.literal}, or both, and invoke a standards-based build backend through a standardized protocol.

Many upstream Python projects no longer rely on a `setup.py`{.literal} script. Instead, they store project metadata in `pyproject.toml`{.literal} and use a build backend, such as `setuptools`{.literal}, `flit-core`{.literal}, `hatchling`{.literal}, or `poetry-core`{.literal}. The `pyproject`{.literal} RPM macros invoke any compliant build backend through a standardized protocol instead of calling `setup.py`{.literal} directly.

The `pyproject`{.literal} RPM macros reuse upstream metadata whenever possible. For example, they can generate `BuildRequires`{.literal} from the build-system requirements in `pyproject.toml`{.literal} instead of listing the same dependencies manually in the `spec`{.literal} file.

The `pyproject-rpm-macros`{.literal} package is available in the CodeReady Linux Builder (CRB) repository. The `%pyproject_buildrequires`{.literal} macro adds a generated `BuildRequires`{.literal} on that package during package builds. CRB content is unsupported by Red Hat. The macros are updated as needed to follow emerging Python packaging standards.

Use `pyproject`{.literal} RPM macros to package Python projects, whether the upstream project defines metadata in `setup.py`{.literal}, `pyproject.toml`{.literal}, or both.

#### [3.4.2. Preparing to use pyproject RPM macros](#preparing-to-use-pyproject-rpm-macros) {#preparing-to-use-pyproject-rpm-macros .title}

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

#### [3.4.3. Common pyproject RPM macros for Python 3 RPMs](#common-pyproject-rpm-macros-for-python-3-rpms) {#common-pyproject-rpm-macros-for-python-3-rpms .title}

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

: Table 3.2. Common pyproject RPM macros for Python 3 RPMs

Show more

The table lists commonly used macros. For all macros and their options, see the `/usr/share/doc/pyproject-rpm-macros/README.md`{.literal} file provided by the `pyproject-rpm-macros`{.literal} package.

#### [3.4.4. A spec file description for a Python package with pyproject RPM macros](#a-spec-file-description-for-a-python-package-with-pyproject-rpm-macros) {#a-spec-file-description-for-a-python-package-with-pyproject-rpm-macros .title}

Use an annotated RPM `spec`{.literal} file example to package a Python project that defines metadata in `setup.py`{.literal}, `pyproject.toml`{.literal}, or both. The example shows `pyproject`{.literal} RPM macros for build requirements, wheel builds, installation, and automated file lists.

**Example 3.2. An example `spec`{.literal} file for a Python library built with pyproject RPM macros**

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

For commonly used macros, see [Common pyproject RPM macros for Python 3 RPMs](#common-pyproject-rpm-macros-for-python-3-rpms "3.4.3. Common pyproject RPM macros for Python 3 RPMs"). For all macros and their options, see the `/usr/share/doc/pyproject-rpm-macros/README.md`{.literal} file provided by the `pyproject-rpm-macros`{.literal} package.

**Additional resources**

-   [Installing additional Python 3 tools for developers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/installing_and_using_dynamic_programming_languages/index#installing-additional-python-3-tools-for-developers)
-   [Using automatically generated dependencies for Python RPMs](#using-automatically-generated-dependencies-for-python-rpms "3.3. Using automatically generated dependencies for Python RPMs")
-   [How to enable and make use of content within CodeReady Linux Builder](https://access.redhat.com/articles/4348511)

## [Chapter 4. Installing Tcl/Tk](#installing-tcl-tk) {#chapter-4.-installing-tcltk .title}

`Tcl`{.literal} is a dynamic programming language, while `Tk`{.literal} is a graphical user interface (GUI) toolkit. They provide a powerful and easy-to-use platform for developing cross-platform applications with graphical interfaces.

As a dynamic programming language, `Tcl`{.literal} provides simple and flexible syntax for writing scripts. The `tcl`{.literal} package provides the interpreter for this language and the C library. You can use `Tk`{.literal} as GUI toolkit that provides a set of tools and widgets for creating graphical interfaces. You can use various user interface elements such as buttons, menus, dialog boxes, text boxes, and canvas for drawing graphics. `Tk`{.literal} is the GUI for many dynamic programming languages.

### [4.1. Installing Tcl](#installing-tcl) {#installing-tcl .title}

To develop and run cross-platform software applications and scripts, install the `Tcl`{.literal} dynamic programming language on your RHEL 10 system. The default `Tcl`{.literal} implementation is usually installed by default. However, you can also install it manually.

**Procedure**

-   To install `Tcl`{.literal}, use:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tcl
    ```

**Verification**

-   To verify the Tcl version installed on your system, run the interpreter `tclsh`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ tclsh
    ```

-   In the interpreter run this command:

    ``` {.language-plaintext tabindex="-1"}
    % info patchlevel
    8.6
    ```

-   You can exit the interpreter interface by pressing Ctrl+C

### [4.2. Installing Tk](#installing-tk) {#installing-tk .title}

To get a set of tools and widgets for creating graphical user interfaces (GUIs), install the `Tk`{.literal} toolkit. You can use `Tk`{.literal} for different dynamic applications. The default `Tk`{.literal} toolkit implementation is usually installed by default. However, you can also install it manually.

**Procedure**

-   Install the `Tk`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tk
    ```

**Verification**

-   To verify the `Tk`{.literal} version installed on your system, run the window shell `wish`{.literal}. You need to be running a graphical display:

    ``` {.language-plaintext tabindex="-1"}
    $ wish
    ```

-   In the shell run this command:

    ``` {.language-plaintext tabindex="-1"}
    % puts $tk_version
    8.6
    ```

-   You can exit the interpreter interface by pressing Ctrl+C

### [4.3. Additional resources](#installing-tcl-tk_43-additional-resources) {#additional-resources-1 .title}

-   [Tcl/Tk manual](https://www.tcl.tk/man/tcl8.6/)
-   [Tcl/Tk documentation web page](https://www.tcl.tk/doc/)

## [Chapter 5. Using the PHP scripting language](#using-the-php-scripting-language) {#chapter-5.-using-the-php-scripting-language .title}

Hypertext Preprocessor (PHP) is a general-purpose scripting language mainly used for server-side scripting. You can use PHP to run the PHP code by using a web server.

### [5.1. Installing the PHP scripting language](#installing-the-php-scripting-language) {#installing-the-php-scripting-language .title}

To develop and deploy server-side web applications, install PHP on your system.

In RHEL 10, the PHP scripting language is available as the `php`{.literal} RPM package in the following versions:

-   PHP 8.3
-   PHP 8.4 available since RHEL 10.2

**Prerequisites**

-   You have root privileges.

**Procedure**

-   Install the PHP packages:

    -   For PHP 8.3, enter:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install php
        ```

    -   For PHP 8.4, enter:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install php8.4
        ```

**Additional resources**

-   [Managing software with the DNF tool](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/index)

### [5.2. Upgrading from a RHEL 10 version of PHP 8.3 to PHP 8.4](#upgrading-from-a-rhel-10-version-of-php-8-3-to-php-8-4) {#upgrading-from-a-rhel-10-version-of-php-8.3-to-php-8.4 .title}

You can upgrade your PHP scripting language from version 8.3 to 8.4 to access new features and improvements.

For notable changes and enhancements, see the [release note](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/10.2_release_notes/new-features-and-enhancements#Jira-RHEL-105827) in the RHEL 10.2 Release Notes document.

Note

Using the ‎`--allowerasing`{.literal} option can unexpectedly remove PHP extensions. To avoid removing required extensions, list your installed PHP extensions, remove the existing ‎`php`{.literal} packages, and then install PHP 8.4 together with the extensions that you need.

**Prerequisites**

-   You have root privileges.

**Procedure**

1.  List the currently installed PHP packages and extensions:

    ``` {.language-plaintext tabindex="-1"}
    # dnf list --installed php-\*
    ```

2.  Note the installed extensions from the output of the previous command.

3.  Remove the existing PHP packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf remove php\*
    ```

4.  Install PHP 8.4 along with the extensions that you noted previously:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install php8.4-common php8.4-cli <extension_name> <extension_name>
    ```

### [5.3. Using the PHP scripting language with a web server](#using-the-php-scripting-language-with-a-web-server) {#using-the-php-scripting-language-with-a-web-server .title}

To host and deliver dynamic web applications, you can configure the Apache HTTP Server or the `nginx`{.literal} web server to process PHP scripts by using FastCGI Process Manager (FPM).

#### [5.3.1. Using PHP with the Apache HTTP Server](#using-php-with-the-apache-http-server) {#using-php-with-the-apache-http-server .title}

In Red Hat Enterprise Linux 10, you can use the `Apache HTTP Server`{.literal} to run PHP as a `FastCGI`{.literal} process server. As an alternative PHP `FastCGI`{.literal} daemon, you can use `FastCGI Process Manager`{.literal} (FPM) to manage high website loads. PHP uses `FastCGI Process Manager`{.literal} by default in RHEL 10.

**Prerequisites**

-   The PHP scripting language is installed on your system.

**Procedure**

-   Configure the `Apache HTTP Server`{.literal} and `php-fpm`{.literal} to run PHP scripts.

    a.  Install the `httpd`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install httpd
        ```

    b.  Start the `Apache HTTP Server`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl start httpd
        ```

        Or, if the `Apache HTTP Server`{.literal} is already running on your system, restart the `httpd`{.literal} service after installing PHP:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart httpd
        ```

    c.  Start the `php-fpm`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl start php-fpm
        ```

    d.  Optional: Enable both services to start at boot time:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable php-fpm httpd
        ```

    e.  To obtain information about your PHP settings, create the `index.php`{.literal} file with the following content in the `/var/www/html/`{.literal} directory:

        ``` {.language-plaintext tabindex="-1"}
        # echo '<?php phpinfo(); ?>' > /var/www/html/index.php
        ```

    f.  To run the `index.php`{.literal} file, point the browser to:

        ``` {.language-plaintext tabindex="-1"}
        http://<hostname>/
        ```

    g.  Optional: Adjust configuration if you have specific requirements:

        -   `/etc/httpd/conf/httpd.conf`{.literal} - generic `httpd`{.literal} configuration
        -   `/etc/httpd/conf.d/php.conf`{.literal} - PHP-specific configuration for `httpd`{.literal}
        -   `/usr/lib/systemd/system/httpd.service.d/php-fpm.conf`{.literal} - by default, the `php-fpm`{.literal} service is started with `httpd`{.literal}
        -   `/etc/php-fpm.conf`{.literal} - FPM main configuration
        -   `/etc/php-fpm.d/www.conf`{.literal} - default `www`{.literal} pool configuration

-   Run the \"Hello, World!\" PHP script using the Apache HTTP Server.

    a.  Create a `hello`{.literal} directory for your project in the `/var/www/html/`{.literal} directory:

        ``` {.language-plaintext tabindex="-1"}
        # mkdir hello
        ```

    b.  Create a `hello.php`{.literal} file in the `/var/www/html/hello/`{.literal} directory with the following content:

        ``` {.language-plaintext tabindex="-1"}
        # <!DOCTYPE html>
        <html>
        <head>
        <title>Hello, World! Page</title>
        </head>
        <body>
        <?php
            echo 'Hello, World!';
        ?>
        </body>
        </html>
        ```

    c.  Start the `Apache HTTP Server`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl start httpd
        ```

    d.  To run the `hello.php`{.literal} file, point the browser to:

        ``` {.language-plaintext tabindex="-1"}
        http://<hostname>/hello/hello.php
        ```

        As a result, a web page with the \"Hello, World!\" text is displayed.

        See `httpd(8)`{.literal}, `httpd.conf(5)`{.literal}, and `php-fpm(8)`{.literal} man pages for more information.

**Additional resources**

-   [Configuring the Apache HTTP web server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/setting-up-the-apache-http-web-server)

#### [5.3.2. Using PHP with the nginx web server](#using-php-with-the-nginx-web-server) {#using-php-with-the-nginx-web-server .title}

Configure the `nginx`{.literal} web server to process PHP scripts on your RHEL 10 system.

**Prerequisites**

-   The PHP scripting language is installed on your system.

**Procedure**

-   Configure the `nginx`{.literal} web server and `php-fpm`{.literal} to run PHP scripts.

    a.  Install the `nginx`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install nginx
        ```

    b.  Start the `nginx`{.literal} server:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl start nginx
        ```

        Or, if the `nginx`{.literal} server is already running on your system, restart the `nginx`{.literal} service after installing PHP:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart nginx
        ```

    c.  Start the `php-fpm`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl start php-fpm
        ```

    d.  Optional: Enable both services to start at boot time:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable php-fpm nginx
        ```

    e.  To obtain information about your PHP settings, create the `index.php`{.literal} file with the following content in the `/usr/share/nginx/html/`{.literal} directory:

        ``` {.language-plaintext tabindex="-1"}
        # echo '<?php phpinfo(); ?>' > /usr/share/nginx/html/index.php
        ```

    f.  To run the `index.php`{.literal} file, point the browser to:

        ``` {.language-plaintext tabindex="-1"}
        http://<hostname>/
        ```

    g.  Optional: Adjust configuration if you have specific requirements:

        -   `/etc/nginx/nginx.conf`{.literal} - `nginx`{.literal} main configuration
        -   `/etc/nginx/conf.d/php-fpm.conf`{.literal} - FPM configuration for `nginx`{.literal}
        -   `/etc/php-fpm.conf`{.literal} - FPM main configuration
        -   `/etc/php-fpm.d/www.conf`{.literal} - default `www`{.literal} pool configuration

-   Run the \"Hello, World!\" PHP script using the nginx server.

    a.  Create a `hello`{.literal} directory for your project in the `/usr/share/nginx/html/`{.literal} directory:

        ``` {.language-plaintext tabindex="-1"}
        # mkdir hello
        ```

    b.  Create a `hello.php`{.literal} file in the `/usr/share/nginx/html/hello/`{.literal} directory with the following content:

        ``` {.language-plaintext tabindex="-1"}
        # <!DOCTYPE html>
        <html>
        <head>
        <title>Hello, World! Page</title>
        </head>
        <body>
        <?php
            echo 'Hello, World!';
        ?>
        </body>
        </html>
        ```

    c.  Start the `nginx`{.literal} server:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl start nginx
        ```

    d.  To run the `hello.php`{.literal} file, point the browser to:

        ``` {.language-plaintext tabindex="-1"}
        http://<hostname>/hello/hello.php
        ```

        As a result, a web page with the \"Hello, World!\" text is displayed.

        See `nginx(8)`{.literal} and `php-fpm(8)`{.literal} man pages for more information.

**Additional resources**

-   [Configuring NGINX](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/setting-up-and-configuring-nginx)

### [5.4. Running a PHP script using the command line](#running-a-php-script-using-the-command-line) {#running-a-php-script-using-the-command-line .title}

A PHP script is usually run by using a web server. However, you can also run the script by using the command line.

**Prerequisites**

-   The PHP scripting language is installed on your system.

**Procedure**

1.  Open a text editor and create a PHP file named `hello.php`{.literal} with the following content:

    ``` {.language-plaintext tabindex="-1"}
    <?php
        echo 'Hello, World!';
    ?>
    ```

2.  At the command line, change to the directory containing `hello.php`{.literal}.

3.  Run the PHP script from the command line:

    ``` {.language-plaintext tabindex="-1"}
    $ php hello.php
    Hello, World!
    ```

    See `php(1)`{.literal} man pages for more information.

## [Legal Notice](#idm139798033256144) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
