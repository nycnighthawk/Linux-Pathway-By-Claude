---
{"title": "Security hardening", "guide": "security_hardening", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/security_hardening/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Security hardening {#security-hardening .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Enhancing security of Red Hat Enterprise Linux 10 systems {#enhancing-security-of-red-hat-enterprise-linux-10-systems .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140263476979072)

**Abstract**

Learn the processes and practices for securing Red Hat Enterprise Linux servers and workstations against local and remote intrusion, exploitation, and malicious activity. By using these approaches and tools, you can create a more secure computing environment for the data center, workplace, and home.

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

## [Chapter 1. Switching RHEL to FIPS mode](#switching-rhel-to-fips-mode) {#chapter-1.-switching-rhel-to-fips-mode .title}

To enable the cryptographic module self-checks mandated by the Federal Information Processing Standard (FIPS) 140-3, you must operate RHEL 10 in FIPS mode. The only correct way to switch the system to FIPS mode is to enable it during the RHEL installation.

Switching a system to FIPS mode after installation is not supported in Red Hat Enterprise Linux 10. In particular, setting the `FIPS`{.literal} system-wide cryptographic policy is not sufficient to enable FIPS mode and guarantee compliance with the FIPS 140 standard. The `fips-mode-setup`{.literal} tool, which used the `FIPS`{.literal} policy for enabling FIPS mode, has been removed from RHEL.

To turn off FIPS mode, you must reinstall the system without enabling FIPS mode during the installation process.

### [1.1. Federal Information Processing Standards 140 and FIPS mode](#federal-information-processing-standards-140-and-fips-mode) {#federal-information-processing-standards-140-and-fips-mode .title}

The Federal Information Processing Standard (FIPS) 140 is a government standard specifying cryptographic module security. FIPS mode enables required self-checks for compliance.

The FIPS Publication 140 is a series of computer security standards developed by the National Institute of Standards and Technology (NIST). It ensures the quality of cryptographic modules. The FIPS 140 standard ensures that cryptographic tools implement their algorithms correctly. Runtime cryptographic algorithms and integrity self-tests are some mechanisms that ensure a system uses compliant cryptography.

#### [1.1.1. RHEL in FIPS mode](#rhel_in_fips_mode) {#rhel-in-fips-mode .title}

To ensure that your RHEL system generates and uses all cryptographic keys only with FIPS-approved algorithms, you must switch RHEL to FIPS mode.

To enable FIPS mode, start the installation in FIPS mode. This avoids cryptographic key material regeneration and compliance reevaluation when converting deployed systems. Additionally, components that change their algorithm choices based on FIPS mode choose the correct algorithms. For example, LUKS disk encryption uses the PBKDF2 key derivation function (KDF) during installation in FIPS mode. Otherwise, it chooses the non-FIPS-compliant Argon2 KDF. Therefore, a non-FIPS installation with disk encryption is either not compliant or potentially unbootable when switched to FIPS mode after installation.

To operate a FIPS-compliant system, create all cryptographic key material in FIPS mode. Furthermore, the cryptographic key material must never leave the FIPS environment unless it is securely wrapped and never unwrapped in non-FIPS environments.

#### [1.1.2. FIPS mode status](#fips_mode_status) {#fips-mode-status .title}

The `fips=1`{.literal} boot option on the kernel command line determines whether FIPS mode is enabled. The system-wide cryptographic policy automatically follows this setting unless you explicitly set it by using the `update-crypto-policies --set FIPS`{.literal} command. Systems with a separate partition for `/boot`{.literal} additionally require a `boot=UUID=<uuid-of-boot-disk>`{.literal} kernel command line argument. The installation program performs the required changes when started in FIPS mode.

Enforcement of restrictions required in FIPS mode depends on the contents of the `/proc/sys/crypto/fips_enabled`{.literal} file. If the file contains `1`{.literal}, RHEL core cryptographic components switch to mode, in which they use only FIPS-approved implementations of cryptographic algorithms. If `/proc/sys/crypto/fips_enabled`{.literal} contains `0`{.literal}, the cryptographic components do not enable their FIPS mode.

#### [1.1.3. FIPS in crypto-policies](#fips_in_crypto_policies) {#fips-in-crypto-policies .title}

The FIPS system-wide cryptographic policy helps configure higher-level restrictions. Communication protocols supporting cryptographic agility do not announce ciphers that the system refuses when selected. For example, the ChaCha20 algorithm is not FIPS-approved. The FIPS cryptographic policy ensures that TLS servers and clients do not announce the `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`{.literal} TLS cipher suite because any attempt to use it fails.

If you operate RHEL in FIPS mode and use an application providing its own FIPS-mode-related configuration options, ignore these options and the corresponding application guidance. The system running in FIPS mode and the system-wide cryptographic policies enforce only FIPS-compliant cryptography. For example, the Node.js `--enable-fips`{.literal} and `--force-fips`{.literal} options are not supported. Do not use these options. On RHEL, Node.js follows the system FIPS mode and uses FIPS-certified OpenSSL libraries provided by RHEL. Using these options causes Node.js to exit with an explanatory error message, regardless of whether the system is running in FIPS mode.

#### [1.1.4. RHEL 10.0 OpenSSL FIPS indicators](#rhel_10_0_openssl_fips_indicators) {#rhel-10.0-openssl-fips-indicators .title}

Because RHEL introduced OpenSSL FIPS indicators before the OpenSSL upstream did, and both designs differ, the indicators might change in a future minor version of RHEL 10. After the potential adoption of the upstream API, the RHEL 10.0 indicators might return an error message \"unsupported\" instead of a result. See the *OpenSSL FIPS Indicators* GitHub document for details.

Note

For the certification status of RHEL 10 cryptographic modules according to the FIPS 140-3 requirements, see the Product compliance Red Hat Customer Portal page. The requirements are defined by the National Institute of Standards and Technology (NIST) Cryptographic Module Validation Program (CMVP). Look for the FIPS - Federal Information Processing Standards section.

**Additional resources**

-   [FIPS - Federal Information Processing Standards (Red Hat Customer Portal)](https://access.redhat.com/compliance/fips)
-   [Product compliance (Red Hat Customer Portal)](https://access.redhat.com/en/compliance)
-   [RHEL system-wide cryptographic policies](#using-system-wide-cryptographic-policies "Chapter 2. Using system-wide cryptographic policies")
-   [FIPS publications at NIST Computer Security Resource Center](https://csrc.nist.gov/publications/fips)
-   [Federal Information Processing Standards Publication: FIPS 140-3 (NIST)](https://doi.org/10.6028/NIST.FIPS.140-3)
-   [OpenSSL FIPS Indicators (Github)](https://github.com/openssl/openssl/blob/master/doc/designs/fips_indicator.md)

### [1.2. Installing the system with FIPS mode enabled](#installing-the-system-with-fips-mode-enabled) {#installing-the-system-with-fips-mode-enabled .title}

To enable the cryptographic module self-checks mandated by the Federal Information Processing Standard (FIPS) 140, enable FIPS mode during the Red Hat Enterprise Linux system installation.

Warning

After you complete the setup of FIPS mode, you cannot disable FIPS mode without putting the system into an inconsistent state. If your scenario requires this change, the only correct way is a complete re-installation of the system.

**Procedure**

1.  Add the `fips=1`{.literal} option to the kernel command line at the start of the system installation when the Red Hat Enterprise Linux boot window opens and displays available boot options.

    a.  On UEFI systems, press the e key, move the cursor to the end of the `linuxefi`{.literal} kernel command line, and add `fips=1`{.literal} to the end of this line, for example:

        ``` {.language-plaintext tabindex="-1"}
        linuxefi /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64 rd.live.\
        check quiet fips=1
        ```

    b.  On BIOS systems, press the Tab key, move the cursor to the end of the kernel command line, and add `fips=1`{.literal} to the end of this line, for example:

        ``` {.language-plaintext tabindex="-1"}
        > vmlinuz initrd=initrd.img inst.stage2=hd:LABEL=RHEL-10-0-BaseOS-x86_64 rd.live.check quiet fips=1
        ```

2.  During the software selection stage, do not install any third-party software.

3.  After the installation, the system starts in FIPS mode automatically.

**Verification**

-   After the system starts, check that FIPS mode is enabled:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /proc/sys/crypto/fips_enabled
    1
    ```

**Additional resources**

-   [Customizing boot options](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/optional-customizing-boot-options#optional-customizing-boot-options)

### [1.3. Enabling FIPS mode with RHEL image builder](#enabling-fips-mode-with-rhel-image-builder) {#enabling-fips-mode-with-rhel-image-builder .title}

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

### [1.4. Creating a bootable disk image for a FIPS-enabled system](#enabling-the-fips-mode-to-perform-an-anaconda-installation) {#creating-a-bootable-disk-image-for-a-fips-enabled-system .title}

You can create a disk image and enable FIPS mode when performing an Anaconda installation. You must add the `fips=1`{.literal} kernel argument when booting the disk image.

**Prerequisites**

-   You have Podman installed on your host machine.
-   You have `virt-install`{.literal} installed on your host machine.
-   You have root access to run the `bootc-image-builder`{.literal} tool, and run the containers in `--privileged`{.literal} mode, to build the images.

**Procedure**

1.  Create a `01-fips.toml`{.literal} to configure FIPS enablement, for example:

    ``` {.language-plaintext tabindex="-1"}
    # Enable FIPS
    kargs = ["fips=1"]
    ```

2.  Create a Containerfile with the following instructions to enable the `fips=1`{.literal} kernel argument and adjust the cryptographic policies:

    ``` {.language-plaintext tabindex="-1"}
    FROM quay.io/<namespace>/<image>:latest
    # Enable fips=1 kernel argument: https://bootc-dev.github.io/bootc/building/kernel-arguments.html
    COPY 01-fips.toml /usr/lib/bootc/kargs.d/
    # Install and enable the FIPS crypto policy
    RUN dnf install -y crypto-policies-scripts && update-crypto-policies --no-reload --set FIPS
    ```

3.  Before running the container, initialize the `output`{.literal} folder. Use the `-p`{.literal} argument to ensure that the command does not fail if the directory already exists:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p ./output
    ```

4.  Create your bootc *`<image>`{.literal}* compatible base disk image by using `Containerfile`{.literal} in the current directory:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
        --rm \
        -it \
        --privileged \
        --pull=newer \
        --security-opt label=type:unconfined_t \
        -v ./config.toml:/config.toml \
        -v ./output:/output \
        -v /var/lib/containers/storage:/var/lib/containers/storage \
        registry.redhat.io/rhel10/bootc-image-builder:latest \
        --type iso \
        quay.io/<namespace>/<image>:<tag>
    ```

5.  Enable FIPS mode during the system installation:

    a.  When booting the RHEL Anaconda installer, on the installation screen, press the TAB key and add the `fips=1`{.literal} kernel argument. After the installation, the system starts in FIPS mode automatically.

**Verification**

-   After login in to the system, check that FIPS mode is enabled:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /proc/sys/crypto/fips_enabled
    1
    $ update-crypto-policies --show
    FIPS
    ```

**Additional resources**

-   [Installing the system with FIPS mode enabled](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/switching-rhel-to-fips-mode#installing-the-system-with-fips-mode-enabled)

### [1.5. List of RHEL applications using cryptography that is not compliant with FIPS 140-3](#list-of-rhel-applications-using-cryptography-that-is-not-compliant-with-fips-140-3) {#list-of-rhel-applications-using-cryptography-that-is-not-compliant-with-fips-140-3 .title}

Review the RHEL applications that use cryptography that is not compliant with FIPS 140-3. To pass all relevant cryptographic certifications, such as FIPS 140-3, use libraries from the core cryptographic components set.

These libraries, except for `libgcrypt`{.literal}, also follow the RHEL system-wide cryptographic policies.

See the [RHEL core cryptographic components](https://access.redhat.com/articles/3655361) Red Hat Knowledgebase article for information about the core cryptographic components. It explains how they are selected, how they integrate with the operating system, and how they support hardware security modules and smart cards. It also describes how cryptographic certifications apply to them.

The following RHEL 10 applications use cryptography that is not compliant with FIPS 140-3:

Bacula
:   Implements the CRAM-MD5 authentication protocol.

Cyrus SASL
:   Uses the SCRAM-SHA-1 authentication method.

curl
:   Supports NTLM authentication which uses MD4 and MD5.

Dovecot
:   Uses SCRAM-SHA-1.

Emacs
:   Uses SCRAM-SHA-1.

FreeRADIUS
:   Uses MD5 and SHA-1 for authentication protocols.

Ghostscript
:   Custom cryptography implementation (MD5, RC4, SHA-2, AES) to encrypt and decrypt documents.

GnuPG
:   The package uses the `libgcrypt`{.literal} module, which is not validated.

GRUB2
:   Supports legacy firmware protocols requiring SHA-1 and includes the `libgcrypt`{.literal} library.

iPXE
:   Implements TLS stack.

Kerberos
:   Preserves support for SHA-1 (interoperability with Windows).

Lasso
:   The `lasso_wsse_username_token_derive_key()`{.literal} key derivation function (KDF) uses SHA-1.

libgcrypt
:   The module is deprecated. It is no longer validated since RHEL 10.0.

MariaDB, MariaDB Connector
:   The `mysql_native_password`{.literal} authentication plugin uses SHA-1.

MySQL
:   `mysql_native_password`{.literal} uses SHA-1.

OpenIPMI
:   The RAKP-HMAC-MD5 authentication method is not approved for FIPS usage and does not work in FIPS mode.

Ovmf (UEFI firmware), Edk2, shim
:   Full cryptographic stack (an embedded copy of the OpenSSL library).

Perl
:   Uses HMAC, HMAC-SHA1, HMAC-MD5, SHA-1, and SHA-224.

Pidgin
:   Implements DES and RC4 ciphers.

Poppler
:   Can save PDFs with signatures, passwords, and encryption based on non-allowed algorithms if they are present in the original PDF (for example, MD5, RC4, and SHA-1).

PostgreSQL
:   Implements Blowfish, DES, and MD5. A KDF uses SHA-1.

QAT Engine
:   Uses a mix of hardware and software implementation of cryptographic primitives (RSA, EC, DH, AES, and others).

Ruby
:   Provides insecure MD5 and SHA-1 library functions.

Samba
:   Preserves support for RC4 and DES (interoperability with Windows).

Sequoia
:   Uses the deprecated OpenSSL API, which does not work in FIPS mode.

Syslinux
:   Firmware passwords use SHA-1.

SWTPM
:   Explicitly disables FIPS mode in its OpenSSL usage.

Unbound
:   DNS specification requires that DNSSEC resolvers use a SHA-1-based algorithm in DNSKEY records for validation.

Valgrind
:   AES, SHA hashes.[^\[1\]^](#ftn.idm140263467354960)

zip
:   Custom cryptography implementation (insecure PKWARE encryption algorithm) to encrypt and decrypt archives by using a password.

**Additional resources**

-   [FIPS - Federal Information Processing Standards (Red Hat Customer Portal)](https://access.redhat.com/compliance/fips)
-   [RHEL core cryptographic components (Red Hat Knowledgebase)](https://access.redhat.com/articles/3655361)
-   [FIPS 140-3 changes for PKCS #12 (Red Hat Blog)](https://www.redhat.com/en/blog/fips-140-3-changes-pkcs-12)

\

------------------------------------------------------------------------

[^\[1\]^](#idm140263467354960) Re-implements in software hardware-offload operations, such as AES-NI or SHA-1 and SHA-2 on ARM.

## [Chapter 2. Using system-wide cryptographic policies](#using-system-wide-cryptographic-policies) {#chapter-2.-using-system-wide-cryptographic-policies .title}

The system-wide cryptographic policies component configures the core cryptographic subsystems, which cover the TLS, IPsec, SSH, DNSSEC, and Kerberos protocols. As an administrator, you can select one of the provided cryptographic policies for your system.

### [2.1. System-wide cryptographic policies](#system-wide-cryptographic-policies) {#system-wide-cryptographic-policies .title}

The RHEL system-wide cryptographic policies configure core subsystems, such as TLS and SSH, which ensures that applications reject weak algorithms by default. The four predefined policies are `DEFAULT`{.literal}, `LEGACY`{.literal}, `FUTURE`{.literal}, and `FIPS`{.literal}.

When a system-wide policy is configured, applications in RHEL follow it and deny using algorithms and protocols that do not meet the policy, unless you explicitly request the application to do so. The policy applies to the default behavior of applications when running with the system-provided configuration. You can override it if required.

#### [2.1.1. Predefined cryptographic policies](#predefined_cryptographic_policies) {#predefined-cryptographic-policies .title}

RHEL 10 contains the following predefined policies:

`DEFAULT`{.literal}
:   The default system-wide cryptographic policy level offers secure settings for current threat models. It allows the TLS 1.2 and 1.3 protocols, and the IKEv2 and SSH2 protocols. The RSA keys and Diffie-Hellman parameters are accepted if they are at least 2048 bits long. TLS ciphers that use the RSA key exchange are rejected.

`LEGACY`{.literal}
:   Ensures maximum compatibility with Red Hat Enterprise Linux 6 and earlier; it is less secure due to an increased attack surface. CBC-mode ciphers are allowed to be used with SSH. It allows TLS 1.2 and 1.3, and IKEv2 and SSH2. The RSA keys and Diffie-Hellman parameters are accepted if they are at least 2048 bits long. SHA-1 signatures are allowed outside TLS. Ciphers that use the RSA key exchange are accepted.

`FUTURE`{.literal}

:   A stricter forward-looking security level intended for testing a possible future policy. This policy does not allow the use of SHA-1 in DNSSEC or as an HMAC. SHA2-224 and SHA3-224 hashes are rejected. 128-bit ciphers are disabled. CBC-mode ciphers are disabled except in Kerberos. It allows TLS 1.2 and 1.3, and IKEv2 and SSH2. The RSA keys and Diffie-Hellman parameters are accepted if they are at least 3072 bits long. If your system communicates on the public internet, you might face interoperability problems.

    Important

    A cryptographic key used by a certificate on the Customer Portal API does not meet the requirements by the `FUTURE`{.literal} system-wide cryptographic policy. Because of this, the `redhat-support-tool`{.literal} utility does not work with this policy level at the moment.

    To work around this problem, use the `DEFAULT`{.literal} cryptographic policy while connecting to the Customer Portal API.

`FIPS`{.literal}

:   Conforms with the FIPS 140 requirements. Red Hat Enterprise Linux systems in FIPS mode use this policy.

    Note

    Your system is not FIPS-compliant after you set the `FIPS`{.literal} cryptographic policy. The only correct way to make your RHEL system compliant with the FIPS 140 standards is by installing it in FIPS mode.

    RHEL also provides the `FIPS:OSPP`{.literal} system-wide subpolicy, which contains further restrictions for cryptographic algorithms required by the Common Criteria (CC) certification. The system becomes less interoperable after you set this subpolicy. For example, you cannot use RSA and DH keys shorter than 3072 bits, additional SSH algorithms, and several TLS groups. Setting `FIPS:OSPP`{.literal} also prevents connecting to Red Hat Content Delivery Network (CDN) structure. Furthermore, you cannot integrate Active Directory (AD) into the IdM deployments that use `FIPS:OSPP`{.literal}. Communication between RHEL hosts that use `FIPS:OSPP`{.literal} and AD domains might not work, or some AD accounts might not be able to authenticate.

    Note

    Your system is not CC-compliant after you set the `FIPS:OSPP`{.literal} cryptographic subpolicy. The only correct way to make your RHEL system compliant with the CC standard is by following the guidance provided in the `cc-config`{.literal} package.

Red Hat continuously adjusts all policy levels so that all libraries provide secure defaults, except when using the `LEGACY`{.literal} policy. Even though the `LEGACY`{.literal} profile does not provide secure defaults, it does not include any algorithms that are easily exploitable. As such, the set of enabled algorithms or acceptable key sizes in any provided policy might change during the lifetime of Red Hat Enterprise Linux.

Such changes reflect new security standards and new security research. If you must ensure interoperability with a specific system for the whole lifetime of Red Hat Enterprise Linux, opt out from the system-wide cryptographic policies for components that interact with that system. Alternatively, re-enable specific algorithms by using custom cryptographic policies.

The specific algorithms and ciphers described as allowed in the policy levels are available only if an application supports them:

+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
|                                                                                           | `LEGACY`{.literal}                    | `DEFAULT`{.literal}                  | `FIPS`{.literal}                     | `FUTURE`{.literal}                   |
+:==========================================================================================+:======================================+:=====================================+:=====================================+:=====================================+
| **IKEv1**                                                                                 | no                                    | no                                   | no                                   | no                                   |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| **3DES**                                                                                  | no                                    | no                                   | no                                   | no                                   |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| **RC4**                                                                                   | no                                    | no                                   | no                                   | no                                   |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| **DH**                                                                                    | min. 2048-bit                         | min. 2048-bit                        | min. 2048-bit                        | min. 3072-bit                        |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| **RSA**                                                                                   | min. 2048-bit                         | min. 2048-bit                        | min. 2048-bit                        | min. 3072-bit                        |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| **DSA**                                                                                   | no                                    | no                                   | no                                   | no                                   |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| **TLS v1.1 and older**                                                                    | no                                    | no                                   | no                                   | no                                   |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| **TLS v1.2 and newer**                                                                    | yes                                   | yes                                  | yes                                  | yes                                  |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| **SHA-1 in digital signatures and certificates**                                          | yes[^\[a\]^](#ftn.idm140263474645200) | no                                   | no                                   | no                                   |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| **CBC mode ciphers**                                                                      | yes                                   | no[^\[b\]^](#ftn.idm140263471018752) | no[^\[c\]^](#ftn.idm140263470138192) | no[^\[d\]^](#ftn.idm140263470135696) |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| **Symmetric ciphers with keys \< 256 bits**                                               | yes                                   | yes                                  | yes                                  | no                                   |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| [^\[a\]^](#idm140263474645200) SHA-1 signatures are disabled in TLS contexts              |                                       |                                      |                                      |                                      |
|                                                                                           |                                       |                                      |                                      |                                      |
| [^\[b\]^](#idm140263471018752) CBC ciphers are disabled for SSH                           |                                       |                                      |                                      |                                      |
|                                                                                           |                                       |                                      |                                      |                                      |
| [^\[c\]^](#idm140263470138192) CBC ciphers are disabled for all protocols except Kerberos |                                       |                                      |                                      |                                      |
|                                                                                           |                                       |                                      |                                      |                                      |
| [^\[d\]^](#idm140263470135696) CBC ciphers are disabled for all protocols except Kerberos |                                       |                                      |                                      |                                      |
+-------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+

: Table 2.1. Cipher suites and protocols enabled in the cryptographic policies

Show more

You can find further details about cryptographic policies and covered applications in the `crypto-policies(7)`{.literal} man page on your system.

#### [2.1.2. Post-quantum cryptography](#post_quantum_cryptography) {#post-quantum-cryptography .title}

RHEL 10.0 introduced post-quantum cryptography (PQC) in its core cryptographic subsystems. The purpose of PQC is to safeguard the confidentiality, integrity, and authenticity of digital communication and stored data against future attacks that use cryptographically relevant quantum computers (CRQCs).

While CRQCs are not currently operational, continued advances in quantum computing might render classic cryptographic algorithms such as RSA and elliptic curve cryptography computationally feasible to break. PQC algorithms mitigate this anticipated long-term security risk by providing quantum-resistant equivalents. You can prevent the current risk of \"harvest now, decrypt later\" attacks by configuring RHEL with PQC.

Starting with RHEL 10.1, post-quantum cryptography (PQC) algorithms are enabled by default in all predefined policy levels. To turn off support for post-quantum cryptography, apply the `NO-PQ`{.literal} subpolicy to your selected cryptographic policy.

**Additional resources**

-   [Product compliance (Red Hat Customer Portal)](https://access.redhat.com/en/compliance)
-   [Common Criteria (Red Hat Customer Portal)](https://access.redhat.com/en/compliance/common-criteria)
-   [Enable SHA-1 signatures in OpenSSL on Red Hat Enterprise Linux 10 (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7105593)
-   [Post-quantum cryptography in Red Hat Enterprise Linux 10 (Red Hat Blog)](https://www.redhat.com/en/blog/post-quantum-cryptography-red-hat-enterprise-linux-10)
-   [Interoperability of RHEL 10 post-quantum cryptography (Red Hat Knowledgebase)](https://access.redhat.com/articles/7119430)
-   [Red Hat's path to post-quantum cryptography (Red Hat Blog)](https://www.redhat.com/en/blog/red-hats-path-post-quantum-cryptography)
-   [How Red Hat is integrating post-quantum cryptography into our products (Red Hat Blog)](https://www.redhat.com/en/blog/how-red-hat-integrating-post-quantum-cryptography-our-products)

### [2.2. Changing the system-wide cryptographic policy](#changing-the-system-wide-cryptographic-policy) {#changing-the-system-wide-cryptographic-policy .title}

You can change the system-wide cryptographic policy on your system by using the `update-crypto-policies`{.literal} tool and restarting your system. With `update-crypto-policies`{.literal}, you can quickly switch between predefined policies such as DEFAULT, LEGACY, or FUTURE.

The `update-crypto-policies(8)`{.literal} man page on your system provides the reference of all options, corresponding files, and per-application details.

**Prerequisites**

-   You have root privileges on the system.

**Procedure**

1.  Optional: Display the current cryptographic policy:

    ``` {.language-plaintext tabindex="-1"}
    $ update-crypto-policies --show
    DEFAULT
    ```

2.  Set the new cryptographic policy:

    ``` {.language-plaintext tabindex="-1"}
    # update-crypto-policies --set <POLICY>
    <POLICY>
    ```

    Replace *`<POLICY>`{.literal}* with the policy or subpolicy you want to set, for example, `FUTURE`{.literal}, `LEGACY`{.literal}, or `FIPS:OSPP`{.literal}.

3.  Restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

-   Display the current cryptographic policy:

    ``` {.language-plaintext tabindex="-1"}
    $ update-crypto-policies --show
    <POLICY>
    ```

**Additional resources**

-   [System-wide cryptographic policies](#system-wide-cryptographic-policies "2.1. System-wide cryptographic policies")

### [2.3. Switching the system-wide cryptographic policy to mode compatible with earlier releases](#switching-the-system-wide-cryptographic-policy-to-mode-compatible-with-earlier-releases) {#switching-the-system-wide-cryptographic-policy-to-mode-compatible-with-earlier-releases .title}

Switch to the `LEGACY`{.literal} cryptographic policy if environments require compatibility with systems such as RHEL 6 or earlier. This action sacrifices security for interoperability with insecure protocols.

Warning

Switching to the `LEGACY`{.literal} policy results in a less secure system and applications.

**Prerequisites**

-   Commands that start with the `#`{.literal} command prompt require administrative privileges provided by `sudo`{.literal} or root user access. For information on how to configure `sudo`{.literal} access, see [Enabling unprivileged users to run certain commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access#enabling-unprivileged-users-to-run-certain-commands).

**Procedure**

1.  To switch the system-wide cryptographic policy to `LEGACY`{.literal}, enter:

    ``` {.language-plaintext tabindex="-1"}
    # update-crypto-policies --set LEGACY
    Setting system policy to LEGACY
    ```

    For the list of available cryptographic policies, see the `update-crypto-policies(8)`{.literal} man page on your system.

2.  To make your cryptographic settings effective for already running services and applications, restart the system:

    ``` {.language-plaintext tabindex="-1"}
    $ reboot
    ```

**Verification**

-   After the restart, verify the current policy is set to `LEGACY`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ update-crypto-policies --show
    LEGACY
    ```

**Next steps**

-   For defining custom cryptographic policies, see the `Custom Policies`{.literal} section in the `update-crypto-policies(8)`{.literal} man page and the `Crypto Policy Definition Format`{.literal} section in the `crypto-policies(7)`{.literal} man page on your system.

### [2.4. Configuring system-wide cryptographic policies in the web console](#setting-up-system-wide-cryptographic-policies-in-the-web-console) {#configuring-system-wide-cryptographic-policies-in-the-web-console .title}

You can configure system-wide cryptographic policies in the RHEL web console. This provides a graphical interface for changing policies such as DEFAULT, LEGACY, or FUTURE.

Besides the three predefined system-wide cryptographic policies, you can also apply a combination of the `LEGACY`{.literal} policy and the `AD-SUPPORT`{.literal} subpolicy through the graphical interface. The `LEGACY:AD-SUPPORT`{.literal} policy is the `LEGACY`{.literal} policy with less secure settings. These settings improve interoperability for Active Directory services.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   Commands that start with the `#`{.literal} command prompt require administrative privileges provided by `sudo`{.literal} or root user access. For information on how to configure `sudo`{.literal} access, see [Enabling unprivileged users to run certain commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access#enabling-unprivileged-users-to-run-certain-commands).

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  In the **Configuration** card of the **Overview** page, click your current policy value next to **Crypto policy**.

3.  In the **Change crypto policy** dialog window, click the policy you want to start using on your system.

4.  Click the Apply and reboot button.

**Verification**

-   After the restart, log back in to web console, and check that the **Crypto policy** value corresponds to the one you selected.

    Alternatively, you can enter the `update-crypto-policies --show`{.literal} command to display the current system-wide cryptographic policy.

### [2.5. Examples of opting out of system-wide cryptographic policies](#excluding-an-application-from-following-systemwide-crypto-policies) {#examples-of-opting-out-of-system-wide-cryptographic-policies .title}

Review examples demonstrating how to opt out of system-wide crypto policies for applications such as OpenSSH and wget. Use these methods when specific applications require legacy ciphers or protocols.

You can customize cryptographic settings used by your application by configuring supported cipher suites and protocols directly in the application.

You can also remove a symlink related to your application from the `/etc/crypto-policies/back-ends`{.literal} directory and replace it with your customized cryptographic settings. This configuration prevents system-wide cryptographic policies from being applied to applications that use the excluded back end. Furthermore, this modification is not supported by Red Hat.

curl

:   To specify ciphers used by the `curl`{.literal} tool, use the `--ciphers`{.literal} option and provide a colon-separated list of ciphers as a value. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ curl <https://example.com> --ciphers '@SECLEVEL=0:DES-CBC3-SHA:RSA-DES-CBC3-SHA'
    ```

    See the `curl(1)`{.literal} man page for more information.

Libreswan
:   See the [Enabling legacy ciphers and algorithms in Libreswan](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/setting-up-an-ipsec-vpn#enabling-legacy-ciphers-and-algorithms-in-libreswan) section in the *Securing networks* document for detailed information.

Mozilla Firefox
:   Even though you cannot opt out of system-wide cryptographic policies in the Mozilla Firefox web browser, you can further restrict supported ciphers and TLS versions in the Firefox's Configuration Editor. Type `about:config`{.literal} in the address bar and change the value of the `security.tls.version.min`{.literal} option as required. Setting `security.tls.version.min`{.literal} to `1`{.literal} allows TLS 1.0 as the minimum required, `security.tls.version.min 2`{.literal} enables TLS 1.1, and so on.

OpenSSH server

:   To opt out of the system-wide cryptographic policies for your OpenSSH server, specify the cryptographic policy in a drop-in configuration file located in the `/etc/ssh/sshd_config.d/`{.literal} directory. Use a two-digit number prefix smaller than 50, so that it lexicographically precedes the `50-redhat.conf`{.literal} file, and a `.conf`{.literal} suffix, for example, `49-crypto-policy-override.conf`{.literal}.

    See the `sshd_config(5)`{.literal} man page for more information.

OpenSSH client

:   To opt out of system-wide cryptographic policies for your OpenSSH client, perform one of the following tasks:

    -   For a given user, override the global `ssh_config`{.literal} with a user-specific configuration in the `~/.ssh/config`{.literal} file.
    -   For the entire system, specify the cryptographic policy in a drop-in configuration file. Place the file in the `/etc/ssh/ssh_config.d/`{.literal} directory. Use a two-digit number prefix smaller than 50, so that it lexicographically precedes the `50-redhat.conf`{.literal} file. Use a `.conf`{.literal} suffix, for example, `49-crypto-policy-override.conf`{.literal}.

    See the `ssh_config(5)`{.literal} man page for more information.

wget

:   To customize cryptographic settings used by the wget network downloader, use the `--secure-protocol`{.literal} and `--ciphers`{.literal} options. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ wget --secure-protocol=TLSv1_1 --ciphers="SECURE128" <https://example.com>
    ```

    See the HTTPS (SSL/TLS) Options section of the `wget(1)`{.literal} man page for more information.

### [2.6. Customizing system-wide cryptographic policies with subpolicies](#customizing-systemwide-cryptographic-policies-with-subpolicies) {#customizing-system-wide-cryptographic-policies-with-subpolicies .title}

Adjust the set of enabled cryptographic algorithms or protocols on the system. In RHEL, you can either apply custom subpolicies on top of an existing system-wide cryptographic policy or define such a policy from scratch.

The concept of scoped policies enables different sets of algorithms for different back ends. You can limit each configuration directive to specific protocols, libraries, or services.

Furthermore, you can use wildcard characters in directives, for example, an asterisk to specify multiple values. For the complete syntax reference, see the `Custom Policies`{.literal} section in the `update-crypto-policies(8)`{.literal} man page and the `Crypto Policy Definition Format`{.literal} section in the `crypto-policies(7)`{.literal} man page on your system.

-   The `/etc/crypto-policies/state/CURRENT.pol`{.literal} file lists all settings in the currently applied system-wide cryptographic policy after wildcard expansion.
-   To make your cryptographic policy more strict, consider using values listed in the `/usr/share/crypto-policies/policies/FUTURE.pol`{.literal} file.
-   You can find example subpolicies in the `/usr/share/crypto-policies/policies/modules/`{.literal} directory.

**Procedure**

1.  Checkout to the `/etc/crypto-policies/policies/modules/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cd /etc/crypto-policies/policies/modules/
    ```

2.  Create subpolicies for your adjustments, for example:

    ``` {.language-plaintext tabindex="-1"}
    # touch <MYCRYPTO-1>.pmod
    # touch <SCOPES-AND-WILDCARDS>.pmod
    ```

    Important

    Use upper-case letters in file names of policy modules.

3.  Open the policy modules in a text editor of your choice and insert options that modify the system-wide cryptographic policy, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi <MYCRYPTO-1>.pmod
    ```

    ``` {.language-plaintext tabindex="-1"}
    min_rsa_size = 3072
    hash = SHA2-384 SHA2-512 SHA3-384 SHA3-512
    ```

    ``` {.language-plaintext tabindex="-1"}
    # vi <SCOPES-AND-WILDCARDS>.pmod
    ```

    ``` {.language-plaintext tabindex="-1"}
    # Disable the AES-128 cipher, all modes
    cipher = -AES-128-*

    # Disable CHACHA20-POLY1305 for the TLS protocol (OpenSSL, GnuTLS, NSS, and OpenJDK)
    cipher@TLS = -CHACHA20-POLY1305

    # Allow using the FFDHE-1024 group with the SSH protocol (libssh and OpenSSH)
    group@SSH = FFDHE-1024+

    # Disable all CBC mode ciphers for the SSH protocol (libssh and OpenSSH)
    cipher@SSH = -*-CBC

    # Allow the AES-256-CBC cipher in applications using libssh
    cipher@libssh = AES-256-CBC+
    ```

4.  Save the changes in the module files.

5.  Apply your policy adjustments to the `DEFAULT`{.literal} system-wide cryptographic policy level:

    ``` {.language-plaintext tabindex="-1"}
    # update-crypto-policies --set DEFAULT:<MYCRYPTO-1>:<SCOPES-AND-WILDCARDS>
    ```

6.  To make your cryptographic settings effective for already running services and applications, restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

-   Check that the `/etc/crypto-policies/state/CURRENT.pol`{.literal} file contains your changes, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /etc/crypto-policies/state/CURRENT.pol | grep rsa_size
    min_rsa_size = 3072
    ```

**Additional resources**

-   [How to customize cryptographic policies in RHEL 8.2 (Red Hat blog)](https://www.redhat.com/en/blog/how-customize-crypto-policies-rhel-82)

### [2.7. Creating and setting a custom system-wide cryptographic policy](#creating-and-setting-a-custom-system-wide-cryptographic-policy) {#creating-and-setting-a-custom-system-wide-cryptographic-policy .title}

Apply custom subpolicies on top of an existing system-wide policy to modify enabled cryptographic algorithms or protocols. By using this granular customization, you can ensure that your system adheres to your specific security requirements.

**Procedure**

1.  Create a policy file for your customizations:

    ``` {.language-plaintext tabindex="-1"}
    # cd /etc/crypto-policies/policies/
    # touch <MYPOLICY>.pol
    ```

    Alternatively, start by copying one of the four predefined policy levels:

    ``` {.language-plaintext tabindex="-1"}
    # cp /usr/share/crypto-policies/policies/DEFAULT.pol /etc/crypto-policies/policies/<MYPOLICY>.pol
    ```

2.  Edit the file with your custom cryptographic policy in a text editor of your choice to fit your requirements, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/crypto-policies/policies/<MYPOLICY>.pol
    ```

    See the `Custom Policies`{.literal} section in the `update-crypto-policies(8)`{.literal} man page and the `Crypto Policy Definition Format`{.literal} section in the `crypto-policies(7)`{.literal} man page on your system for the complete syntax reference.

3.  Switch the system-wide cryptographic policy to your custom level:

    ``` {.language-plaintext tabindex="-1"}
    # update-crypto-policies --set <MYPOLICY>
    ```

4.  To make your cryptographic settings effective for already running services and applications, restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Additional resources**

-   [How to customize cryptographic policies in RHEL 8.2 (Red Hat blog)](https://www.redhat.com/en/blog/how-customize-crypto-policies-rhel-82)

### [2.8. Disabling post-quantum algorithms system-wide](#disabling-post-quantum-algorithms-system-wide) {#disabling-post-quantum-algorithms-system-wide .title}

From RHEL 10.1, post-quantum cryptography (PQC) algorithms are enabled in all predefined policies by default. You can turn them off by applying the `NO-PQ`{.literal} subpolicy.

**Prerequisites**

-   Commands that start with the `#`{.literal} command prompt require administrative privileges provided by `sudo`{.literal} or root user access. For information on how to configure `sudo`{.literal} access, see [Enabling unprivileged users to run certain commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access#enabling-unprivileged-users-to-run-certain-commands).

**Procedure**

1.  Apply the `NO-PQ`{.literal} cryptographic subpolicy on top of your current system-wide policy, for example:

    ``` {.language-plaintext tabindex="-1"}
    # update-crypto-policies --show
    DEFAULT
    # update-crypto-policies --set DEFAULT:NO-PQ
    ```

2.  To make your cryptographic settings effective for already running services and applications, restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

**Verification**

-   Check that the `/etc/crypto-policies/state/CURRENT.pol`{.literal} file does not contain PQC algorithm strings `MLKEM`{.literal}, `MLDSA`{.literal}, and `KEM-ECDH`{.literal}, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /etc/crypto-policies/state/CURRENT.pol | grep MLKEM
    ```

    The output of the previous command must be empty.

### [2.9. Enhancing security with the FUTURE cryptographic policy using the crypto_policies RHEL system role](#enhancing-security-with-the-future-cryptographic-policy-using-the-cryptopolicies-rhel-system-role) {#enhancing-security-with-the-future-cryptographic-policy-using-the-crypto_policies-rhel-system-role .title}

You can use the `crypto_policies`{.literal} RHEL system role to configure the `FUTURE`{.literal} cryptographic policy on your managed nodes.

The `FUTURE`{.literal} policy helps to achieve, for example:

Future-proofing against emerging threats
:   Anticipates advancements in computational power.

Enhanced security
:   Stronger encryption standards require longer key lengths and more secure algorithms.

Compliance with high-security standards
:   In some industries, for example, in healthcare, telco, and finance the data sensitivity is high, and availability of strong cryptography is critical.

Typically, `FUTURE`{.literal} is suitable for environments handling highly sensitive data, preparing for future regulations, or adopting long-term security strategies.

Warning

Legacy systems and software do not have to support the more modern and stricter algorithms and protocols enforced by the `FUTURE`{.literal} policy. For example, older systems might not support TLS 1.3 or larger key sizes. This could lead to interoperability problems.

Also, using strong algorithms usually increases the computational workload, which could negatively affect your system performance.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configure cryptographic policies
      hosts: managed-node-01.example.com
      tasks:
        - name: Configure the FUTURE cryptographic security policy on the managed node
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.crypto_policies
          vars:
            - crypto_policies_policy: FUTURE
            - crypto_policies_reboot_ok: true
    ```

    The settings specified in the example playbook include the following:

    `crypto_policies_policy: `{.literal}*`FUTURE`{.literal}*
    :   Configures the required cryptographic policy (`FUTURE`{.literal}) on the managed node. It can be either the base policy or a base policy with some subpolicies. The specified base policy and subpolicies have to be available on the managed node. The default value is `null`{.literal}, which means that the configuration is not changed and the `crypto_policies`{.literal} RHEL system role only collects the Ansible facts.

    `crypto_policies_reboot_ok: `{.literal}*`true`{.literal}*
    :   Causes the system to reboot after the cryptographic policy change to ensure all of the services and applications read the new configuration files. The default value is `false`{.literal}.

    For details about the role variables and the cryptographic configuration options, see the `/usr/share/ansible/roles/rhel-system-roles.crypto_policies/README.md`{.literal} file and the `update-crypto-policies(8)`{.literal} and `crypto-policies(7)`{.literal} manual pages on the control node.

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

1.  On the control node, create another playbook named, for example, `verify_playbook.yml`{.literal}:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Verification
      hosts: managed-node-01.example.com
      tasks:
        - name: Verify active cryptographic policy
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.crypto_policies
        - name: Display the currently active cryptographic policy
          ansible.builtin.debug:
            var: crypto_policies_active
    ```

    The settings specified in the example playbook include the following:

    `crypto_policies_active`{.literal}
    :   An exported Ansible fact that contains the currently active policy name in the format as accepted by the `crypto_policies_policy`{.literal} variable.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/verify_playbook.yml
    ```

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/verify_playbook.yml
    TASK [debug] **************************
    ok: [host] => {
        "crypto_policies_active": "FUTURE"
    }
    ```

    The `crypto_policies_active`{.literal} variable shows the active policy on the managed node.

## [Chapter 3. Configuring applications to use cryptographic hardware through PKCS #11](#configuring-applications-to-use-cryptographic-hardware-through-pkcs-11) {#chapter-3.-configuring-applications-to-use-cryptographic-hardware-through-pkcs-11 .title}

Configure applications to use cryptographic hardware such as smart cards and HSMs through the consistent PKCS #11 API. Isolating secrets on hardware helps provide an additional layer of security.

### [3.1. Cryptographic hardware support through PKCS #11](#cryptographic-hardware-support-through-pkcs-11) {#cryptographic-hardware-support-through-pkcs-11 .title}

In RHEL, you can use the PKCS #11 API standard and the `p11-kit`{.literal} tool to access cryptographic tokens such as smart cards and hardware security modules (HSMs). By isolating keys on these dedicated devices, you ensure your sensitive data is managed securely.

Public-Key Cryptography Standard (PKCS) #11 defines an application programming interface (API) to cryptographic devices that hold cryptographic information and perform cryptographic functions.

PKCS #11 introduces the *cryptographic token*, an object that presents each hardware or software device to applications in a unified manner. Applications view devices such as smart cards and hardware security modules as PKCS #11 cryptographic tokens. Smart cards are typically used by persons, while hardware security modules are typically used by computers.

A PKCS #11 token can store various object types including a certificate; a data object; and a public, private, or secret key. These objects are uniquely identifiable through the PKCS #11 Uniform Resource Identifier (URI) scheme.

A PKCS #11 URI is a standard way to identify a specific object in a PKCS #11 module according to the object attributes, so you can configure all libraries and applications with the same configuration string in the form of a URI.

RHEL provides the OpenSC PKCS #11 driver for smart cards by default. However, hardware tokens and HSMs can have their own PKCS #11 modules that do not have a counterpart in the system. You can register such PKCS #11 modules with the `p11-kit`{.literal} tool. This tool acts as a wrapper over the registered smart-card drivers in the system.

To make your own PKCS #11 module work on the system, add a new text file to the `/etc/pkcs11/modules/`{.literal} directory.

You can add your own PKCS #11 module into the system by creating a new text file in the `/etc/pkcs11/modules/`{.literal} directory. For example, the OpenSC configuration file in `p11-kit`{.literal} looks as follows:

``` {.language-plaintext tabindex="-1"}
$ cat /usr/share/p11-kit/modules/opensc.module
module: opensc-pkcs11.so
```

**Additional resources**

-   [The PKCS #11 URI Scheme (IETF.org)](https://tools.ietf.org/html/rfc7512)
-   [Controlling access to smart cards (Red Hat Blog)](https://access.redhat.com/blogs/766093/posts/1976313)

### [3.2. Authenticating by SSH keys stored on a smart card](#authenticating-by-ssh-keys-stored-on-a-smart-card) {#authenticating-by-ssh-keys-stored-on-a-smart-card .title}

Use SSH keys stored on a smart card for authentication to add a physical layer of protection to your credentials. This method provides enhanced security against unauthorized access.

You can create and store ECDSA and RSA keys on a smart card and authenticate by the smart card on an OpenSSH client. Smart-card authentication replaces the default password authentication.

**Prerequisites**

-   On the client side, the `opensc`{.literal} package is installed and the `pcscd`{.literal} service is running.

**Procedure**

1.  List all keys provided by the OpenSC PKCS #11 module including their PKCS #11 URIs and save the output to the `keys.pub`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh-keygen -D pkcs11: > keys.pub
    ```

2.  Transfer the public key to the remote server. Use the `ssh-copy-id`{.literal} command with the `keys.pub`{.literal} file created in the previous step:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh-copy-id -f -i keys.pub <username@ssh-server-example.com>
    ```

3.  Connect to *`<ssh-server-example.com>`{.literal}* by using the ECDSA key. You can use just a subset of the URI, which uniquely references your key, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i "pkcs11:id=%01?module-path=/usr/lib64/pkcs11/opensc-pkcs11.so" <ssh-server-example.com>
    Enter PIN for 'SSH key':
    [ssh-server-example.com] $
    ```

    Because OpenSSH uses the `p11-kit-proxy`{.literal} wrapper and the OpenSC PKCS #11 module is registered to the `p11-kit`{.literal} tool, you can simplify the previous command:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i "pkcs11:id=%01" <ssh-server-example.com>
    Enter PIN for 'SSH key':
    [ssh-server-example.com] $
    ```

    If you skip the `id=`{.literal} part of a PKCS #11 URI, OpenSSH loads all keys that are available in the proxy module. This can reduce the amount of typing required:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i pkcs11: <ssh-server-example.com>
    Enter PIN for 'SSH key':
    [ssh-server-example.com] $
    ```

4.  Optional: You can use the same URI string in the `~/.ssh/config`{.literal} file to make the configuration permanent:

    ``` {.language-plaintext tabindex="-1"}
    $ cat ~/.ssh/config
    IdentityFile "pkcs11:id=%01?module-path=/usr/lib64/pkcs11/opensc-pkcs11.so"
    $ ssh <ssh-server-example.com>
    Enter PIN for 'SSH key':
    [ssh-server-example.com] $
    ```

    The `ssh`{.literal} client utility now automatically uses this URI and the key from the smart card.

### [3.3. Application settings for authentication with certificates on smart cards](#configuring-applications-for-authentication-with-certificates-on-smart-cards) {#application-settings-for-authentication-with-certificates-on-smart-cards .title}

You can configure applications such as `curl`{.literal} to authenticate using certificates stored on a smart card. This robust method helps protect your system with physical security credentials.

Authentication by using smart cards in applications might increase security and simplify automation. You can integrate the Public Key Cryptography Standard (PKCS) #11 URIs into your application by using the following methods:

-   The `Firefox`{.literal} web browser automatically loads the `p11-kit-proxy`{.literal} PKCS #11 module. This means that every supported smart card in the system is automatically detected. For using TLS client authentication, no additional setup is required and keys and certificates from a smart card are automatically used when a server requests them.

-   If your application uses the `GnuTLS`{.literal} or `NSS`{.literal} library, it already supports PKCS #11 URIs. Also, applications that rely on the `OpenSSL`{.literal} library can access cryptographic hardware modules, including smart cards, through the PKCS #11 provider installed by the `pkcs11-provider`{.literal} package.

-   Applications that require working with private keys on smart cards and that do not use `NSS`{.literal}, `GnuTLS`{.literal}, nor `OpenSSL`{.literal} can use the `p11-kit`{.literal} API directly. This enables them to work with cryptographic hardware modules, including smart cards, rather than using the PKCS #11 API of specific PKCS #11 modules.

-   With the `wget`{.literal} network downloader, you can specify PKCS #11 URIs instead of paths to locally stored private keys and certificates. This might simplify creation of scripts for tasks that require safely stored private keys and certificates. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ wget --private-key 'pkcs11:token=softhsm;id=%01;type=private?pin-value=111111' --certificate 'pkcs11:token=softhsm;id=%01;type=cert' https://example.com/
    ```

-   You can also specify PKCS #11 URI when using the `curl`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    $ curl --key 'pkcs11:token=softhsm;id=%01;type=private?pin-value=111111' --cert 'pkcs11:token=softhsm;id=%01;type=cert' https://example.com/
    ```

    Note

    A PIN is a security measure that controls access to keys stored on a smart card. Because the configuration file contains the PIN in plain text form, consider additional protection to prevent an attacker from reading the PIN. For example, you can use the `pin-source`{.literal} attribute and provide a `file:`{.literal} URI for reading the PIN from a file. See [RFC 7512: PKCS #11 URI Scheme Query Attribute Semantics](https://datatracker.ietf.org/doc/html/rfc7512#section-2.4) for more information. Note that using a command path as a value of the `pin-source`{.literal} attribute is not supported.

See the `curl(1)`{.literal}, `wget(1)`{.literal}, `p11-kit(8)`{.literal}, and `provider-pkcs11(7)`{.literal} man pages on your system for details and additional examples.

### [3.4. Using HSMs protecting private keys in Apache](#using-hsms-protecting-private-keys-in-apache) {#using-hsms-protecting-private-keys-in-apache .title}

The Apache HTTP server can work with private keys stored on hardware security modules (HSMs), which helps to prevent the keys\' disclosure and man-in-the-middle attacks. Note that this usually requires high-performance HSMs for busy servers.

For secure communication in the form of the HTTPS protocol, the Apache HTTP server (`httpd`{.literal}) uses the OpenSSL library. OpenSSL does not support PKCS #11 natively. To use HSMs, you must install the `pkcs11-provider`{.literal} package, which provides access to PKCS #11 modules. You can use a PKCS #11 URI instead of a regular file name to specify a server key and a certificate in the `/etc/httpd/conf.d/ssl.conf`{.literal} configuration file, for example:

``` {.language-plaintext tabindex="-1"}
SSLCertificateFile    "pkcs11:id=%01;token=softhsm;type=cert"
SSLCertificateKeyFile "pkcs11:id=%01;token=softhsm;type=private?pin-value=111111"
```

Install the `httpd-manual`{.literal} package to obtain complete documentation for the Apache HTTP Server, including TLS configuration. The directives available in the `/etc/httpd/conf.d/ssl.conf`{.literal} configuration file are described in detail in the `/usr/share/httpd/manual/mod/mod_ssl.html`{.literal} file.

## [Chapter 4. Controlling access to smart cards by using polkit](#controlling-access-to-smart-cards-by-using-polkit) {#chapter-4.-controlling-access-to-smart-cards-by-using-polkit .title}

Configure the `polkit`{.literal} framework in RHEL to control access to smart cards. This provides fine-grained control and mitigates threats that built-in mechanisms, such as PINs, PIN pads, and biometrics, cannot prevent.

System administrators can configure `polkit`{.literal} to fit specific scenarios, such as smart-card access for non-privileged or non-local users or services.

### [4.1. Smart-card access control through polkit](#smart-card-access-control-through-polkit) {#smart-card-access-control-through-polkit .title}

With the `polkit`{.literal} authorization manager, you can define precise policies for securing smart cards. Administrators can use this framework to control which users can perform specific privileged operations with the card.

The Personal Computer/Smart Card (PC/SC) protocol specifies a standard for integrating smart cards and their readers into computing systems. In RHEL, the `pcsc-lite`{.literal} package provides middleware to access smart cards that use the PC/SC API. A part of this package, the `pcscd`{.literal} (PC/SC Smart Card) daemon, ensures that the system can access a smart card by using the PC/SC protocol.

Because access-control mechanisms built into smart cards, such as PINs, PIN pads, and biometrics, do not cover all possible threats, RHEL uses the `polkit`{.literal} framework for more robust access control. The `polkit`{.literal} authorization manager can grant access to privileged operations. In addition to granting access to disks, you can use `polkit`{.literal} also to specify policies for securing smart cards. For example, you can define which users can perform which operations with a smart card.

After installing the `pcsc-lite`{.literal} package and starting the `pcscd`{.literal} daemon, the system enforces policies defined in the `/usr/share/polkit-1/actions/`{.literal} directory. The default system-wide policy is in the `/usr/share/polkit-1/actions/org.debian.pcsc-lite.policy`{.literal} file. Polkit policy files use the XML format and the syntax is described in the `polkit(8)`{.literal} man page.

The `polkitd`{.literal} service monitors the `/etc/polkit-1/rules.d/`{.literal} and `/usr/share/polkit-1/rules.d/`{.literal} directories for any changes in rule files stored in these directories. The files contain authorization rules in JavaScript format. System administrators can add custom rule files in both directories, and `polkitd`{.literal} reads them in lexical order based on their file name. If two files have the same names, then the file in `/etc/polkit-1/rules.d/`{.literal} is read first.

### [4.2. Troubleshooting problems related to PC/SC and polkit](#troubleshooting-problems-related-to-pcsc-and-polkit) {#troubleshooting-problems-related-to-pcsc-and-polkit .title}

You can troubleshoot smart-card authentication failures by checking the Journal log for messages related to the `pcscd`{.literal} daemon and the `polkit`{.literal} authorization framework. This helps identify policy or access denials.

Polkit policies that are automatically enforced after you install the `pcsc-lite`{.literal} package and start the `pcscd`{.literal} daemon might ask for authentication in the user's session. This occurs even if the user does not directly interact with a smart card. In GNOME, you can see the following error message:

``` {.language-plaintext tabindex="-1"}
Authentication is required to access the PC/SC daemon
```

Note that the system can install the `pcsc-lite`{.literal} package as a dependency when you install other packages related to smart cards such as `opensc`{.literal}.

If your scenario does not require any interaction with smart cards and you want to prevent displaying authorization requests for the PC/SC daemon, you can remove the `pcsc-lite`{.literal} package. Keeping the minimum of necessary packages is a good security practice anyway.

If you use smart cards, start troubleshooting by checking the rules in the system-provided policy file at `/usr/share/polkit-1/actions/org.debian.pcsc-lite.policy`{.literal}. You can add your custom rule files to the policy in the `/etc/polkit-1/rules.d/`{.literal} directory, for example, `03-allow-pcscd.rules`{.literal}. Note that the rule files use the JavaScript syntax, the policy file is in the XML format.

To understand what authorization requests the system displays, check the Journal log, for example:

``` {.language-plaintext tabindex="-1"}
$ journalctl -b | grep pcsc
…
Process 3087 (user: 1001) is NOT authorized for action: access_pcsc
…
```

The previous log entry means that the user is not authorized to perform an action by the policy. You can solve this denial by adding a corresponding rule to `/etc/polkit-1/rules.d/`{.literal}.

You can search also for log entries related to the `polkitd`{.literal} unit, for example:

``` {.language-plaintext tabindex="-1"}
$ journalctl -u polkit
…
polkitd[NNN]: Error compiling script /etc/polkit-1/rules.d/00-debug-pcscd.rules
…
polkitd[NNN]: Operator of unix-session:c2 FAILED to authenticate to gain authorization for action org.debian.pcsc-lite.access_pcsc for unix-process:4800:14441 [/usr/libexec/gsd-smartcard] (owned by unix-user:group)
…
```

In the previous output, the first entry means that the rule file contains some syntax error. The second entry means that the user failed to gain the access to `pcscd`{.literal}.

You can also list all applications that use the PC/SC protocol by a short script. Create an executable file, for example, `pcsc-apps.sh`{.literal}, and insert the following code:

``` {.language-plaintext tabindex="-1"}
#!/bin/bash

cd /proc

for p in [0-9]*
do
    if grep libpcsclite.so.1.0.0 $p/maps &> /dev/null
    then
        echo -n "process: "
        cat $p/cmdline
        echo " ($p)"
    fi
done
```

Run the script as `root`{.literal}:

``` {.language-plaintext tabindex="-1"}
# ./pcsc-apps.sh
process: /usr/libexec/gsd-smartcard (3048)
enable-sync --auto-ssl-client-auth --enable-crashpad (4828)
…
```

### [4.3. Displaying more detailed information about polkit authorization to PC/SC](#displaying-more-detailed-information-about-polkit-authorization-to-pcsc) {#displaying-more-detailed-information-about-polkit-authorization-to-pcsc .title}

In the default configuration, the `polkit`{.literal} authorization framework sends only limited information to the Journal log. You can extend `polkit`{.literal} log entries related to the PC/SC protocol by adding new rules.

**Prerequisites**

-   You have installed the `pcsc-lite`{.literal} package on your system.
-   The `pcscd`{.literal} daemon is running.

**Procedure**

1.  Create a new file in the `/etc/polkit-1/rules.d/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # touch /etc/polkit-1/rules.d/00-test.rules
    ```

2.  Edit the file in an editor of your choice, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/polkit-1/rules.d/00-test.rules
    ```

3.  Insert the following lines:

    ``` {.language-plaintext tabindex="-1"}
    polkit.addRule(function(action, subject) {
      if (action.id == "org.debian.pcsc-lite.access_pcsc" ||
        action.id == "org.debian.pcsc-lite.access_card") {
        polkit.log("action=" + action);
        polkit.log("subject=" + subject);
      }
    });
    ```

    Save the file, and exit the editor.

4.  Restart the `pcscd`{.literal} and `polkit`{.literal} services:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart pcscd.service pcscd.socket polkit.service
    ```

**Verification**

1.  Make an authorization request for `pcscd`{.literal}. For example, open the Mozilla Firefox web browser or use the `pkcs11-tool -L`{.literal} command provided by the `opensc`{.literal} package.

2.  Display the extended log entries, for example:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u polkit --since "1 hour ago"
    polkitd[1224]: <no filename>:4: action=[Action id='org.debian.pcsc-lite.access_pcsc']
    polkitd[1224]: <no filename>:5: subject=[Subject pid=2020481 user=user' groups=user,wheel,mock,wireshark seat=null session=null local=true active=true]
    ```

### [4.4. Additional resources](#controlling-access-to-smart-cards-by-using-polkit_44-additional-resources) {#additional-resources .title}

-   [Controlling access to smart cards (Red Hat Blog)](https://www.redhat.com/en/blog/controlling-access-smart-cards)

## [Chapter 5. Scanning the system for configuration compliance](#scanning-the-system-for-configuration-compliance) {#chapter-5.-scanning-the-system-for-configuration-compliance .title}

Scan your RHEL configuration against specific rules defined in a compliance policy. With these checklists, you can ensure that your environment adheres to strict security requirements.

Security professionals define the compliance policy by specifying the required settings for a computing environment, often in the form of a checklist.

Compliance policies can vary substantially across organizations and even across different systems within the same organization. Differences among these policies are based on the purpose of each system and its importance for the organization. Custom software settings and deployment characteristics also raise a need for custom policy checklists.

### [5.1. Configuration compliance tools in RHEL](#configuration-compliance-tools-in-rhel) {#configuration-compliance-tools-in-rhel .title}

RHEL 10 provides configuration-compliance tools for automated compliance audits. These tools are based on the SCAP standard. They are designed for automated tailoring of compliance policies.

OpenSCAP

:   The OpenSCAP library includes the `oscap`{.literal} command-line utility. Use it to:

    -   perform configuration scans on a local system

    -   validate configuration compliance content

    -   generate reports and guides based on scans and evaluations

        With `oscap`{.literal}, you can scan systems. This assesses their alignment with security policies in `scap-security-guide`{.literal}. You can also run automated remediation. This configures the system to align with a selected policy.

        Important

        You can experience memory-consumption problems while using OpenSCAP. This can stop the program early. It can also prevent generating result files.

SCAP Security Guide (SSG)
:   The `scap-security-guide`{.literal} package provides collections of security policies for Linux systems. The guidance consists of practical hardening advice. It links to government requirements where applicable. The project bridges the gap between general policy requirements and specific implementation guidelines.

Script Check Engine (SCE)
:   SCE is an extension to the SCAP protocol. With SCE, administrators can write security content by using a scripting language such as Bash, Python, and Ruby. The SCE extension is in the `openscap-engine-sce`{.literal} package. SCE itself is not part of the SCAP standard.

You can also perform automated compliance audits on multiple systems remotely. Use the OpenSCAP solution for Red Hat Satellite.

**Additional resources**

-   [Red Hat Security Demos: Creating Customized Security Policy Content to Automate Security Compliance](https://2020-summit-labs.gitlab.io/rhel-custom-security-content/)
-   [Red Hat Security Demos: Defend Yourself with RHEL Security Technologies](https://github.com/RedHatDemos/SecurityDemos/blob/master/2020Labs/RHELSecurity/documentation/README.adoc)
-   [Managing security compliance in Red Hat Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/latest/html/managing_security_compliance/index)
-   [OpenSCAP memory-consumption problems (Red Hat Knowledgebase)](https://access.redhat.com/articles/6999111)

### [5.2. Configuration compliance scanning](#configuration-compliance-scanning) {#configuration-compliance-scanning .title}

Verify if your Red Hat Enterprise Linux systems adhere to security baselines, such as industry standards or internal policies, by performing a configuration compliance scan. You can scan local and remote systems, containers, and container images using OpenSCAP and the SCAP Security Guide.

#### [5.2.1. Configuration compliance in RHEL](#configuration-compliance-in-rhel) {#configuration-compliance-in-rhel .title}

Use configuration compliance scanning to conform to a baseline defined by a specific organization. For example, if you are a payment processor, you can align your systems with the Payment Card Industry Data Security Standard (PCI-DSS). You can also perform a scan to harden your system security.

Follow the Security Content Automation Protocol (SCAP) content in the SCAP Security Guide package, as it aligns with Red Hat best practices for affected components.

The SCAP Security Guide package provides content which conforms to the SCAP 1.2 and SCAP 1.3 standards. The `openscap scanner`{.literal} utility is compatible with both SCAP 1.2 and SCAP 1.3 content provided in the SCAP Security Guide package.

Important

Performing a configuration compliance scanning does not guarantee the system is compliant.

The SCAP Security Guide suite provides profiles for several platforms in the form of data stream documents. A data stream is a file that contains definitions, benchmarks, profiles, and individual rules. Each rule specifies the applicability and requirements for compliance. RHEL provides several profiles for compliance with security policies. In addition to the industry standard, Red Hat data streams also contain information for remediation of failed rules. Data streams use the following structure:

``` {.language-plaintext tabindex="-1"}
Data stream
   ├── xccdf
   |      ├── benchmark
   |            ├── profile
   |            |    ├──rule reference
   |            |    └──variable
   |            ├── rule
   |                 ├── human readable data
   |                 ├── ocil reference
   ├── ocil          ├── cpe reference
   └── cpe           └── remediation
```

A profile is a set of rules based on a security policy, such as PCI-DSS and Health Insurance Portability and Accountability Act (HIPAA). After you select a profile, you can then perform an automated audit of the system for compliance with that profile.

You can also modify, or *tailor*, a profile to customize certain rules, for example, password length.

**Additional resources**

-   [Customizing a security profile with autotailor](#customizing-a-security-profile-with-autotailor "5.5. Customizing a security profile with autotailor")

#### [5.2.2. Possible results of an OpenSCAP scan](#possible-results-of-an-openscap-scan) {#possible-results-of-an-openscap-scan .title}

Understanding possible results of an OpenSCAP scan, such as Pass, Fail, or Not Applicable, helps you interpret compliance reports accurately.

Depending on the data stream and profile applied to an OpenSCAP scan and the various properties of your system, each rule produces a specific result:

Pass
:   The scan did not find any conflicts with this rule.

Fail
:   The scan found a conflict with this rule.

Not checked
:   OpenSCAP does not perform an automatic evaluation of this rule. Check whether your system conforms to this rule manually.

Not applicable
:   This rule does not apply to the current configuration.

Not selected
:   This rule is not part of the profile. OpenSCAP does not evaluate this rule and does not display these rules in the results.

Error
:   The scan encountered an error. For additional information, you can enter the `oscap`{.literal} command with the `--verbose DEVEL`{.literal} option. File a support case on the [Red Hat Customer Portal](https://access.redhat.com/support/cases/) or open a ticket in the [RHEL project in Red Hat Jira](https://issues.redhat.com/projects/RHEL/issues).

Unknown
:   The scan encountered an unexpected situation. For additional information, you can enter the `oscap`{.literal} command with the `--verbose DEVEL`{.literal} option. File a support case on the [Red Hat Customer Portal](https://access.redhat.com/support/cases/) or open a ticket in the [RHEL project in Red Hat Jira](https://issues.redhat.com/projects/RHEL/issues).

#### [5.2.3. Viewing profiles for configuration compliance](#viewing-profiles-for-configuration-compliance) {#viewing-profiles-for-configuration-compliance .title}

Before you decide to use profiles for scanning or remediation, you can list them and check their detailed descriptions by using the `oscap info`{.literal} subcommand.

**Prerequisites**

-   The `openscap-scanner`{.literal} and `scap-security-guide`{.literal} packages are installed.

**Procedure**

1.  List all available files with security compliance profiles provided by the SCAP Security Guide project:

    ``` {.language-plaintext tabindex="-1"}
    $ ls /usr/share/xml/scap/ssg/content/
    ssg-rhel10-ds.xml
    ```

2.  Display detailed information about a selected data stream by using the `oscap info`{.literal .command} subcommand. XML files containing data streams are indicated by the `-ds`{.literal} string in their names. In the `Profiles`{.literal} section, you can find a list of available profiles and their IDs:

    ``` {.language-plaintext tabindex="-1"}
    $ oscap info /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    Profiles:
    …
      Title: Australian Cyber Security Centre (ACSC) ISM Official - Top Secret
            Id: xccdf_org.ssgproject.content_profile_ism_o_top_secret
        Title: PCI-DSS v4.0.1 Control Baseline for Red Hat Enterprise Linux 10
            Id: xccdf_org.ssgproject.content_profile_pci-dss
        Title: Red Hat STIG for Red Hat Enterprise Linux 10
            Id: xccdf_org.ssgproject.content_profile_stig

    …
    ```

3.  Select a profile from the data stream file and display additional details about the selected profile. To do so, use `oscap info`{.literal .command} with the `--profile`{.literal} option followed by the last section of the ID displayed in the output of the previous command. For example, the ID of the HIPPA profile is `xccdf_org.ssgproject.content_profile_hipaa`{.literal}, and the value for the `--profile`{.literal .option} option is `hipaa`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ oscap info --profile hipaa /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    …
    Profile
        Title: Health Insurance Portability and Accountability Act (HIPAA)

        Description: The HIPAA Security Rule establishes U.S. national standards to protect individuals' electronic personal health information that is created, received, used, or maintained by a covered entity.
    …
    ```

**Additional resources**

-   [OpenSCAP memory consumption problems](https://access.redhat.com/articles/6999111)

#### [5.2.4. Assessing configuration compliance with a specific baseline](#assessing-configuration-compliance-with-a-specific-baseline) {#assessing-configuration-compliance-with-a-specific-baseline .title}

You can determine whether your system or a remote system conforms to a specific baseline, and save the results in a report by using the `oscap`{.literal} command-line tool.

**Prerequisites**

-   The `openscap-scanner`{.literal .package} and `scap-security-guide`{.literal .package} packages are installed.
-   You know the ID of the profile within the baseline with which the system should comply. To find the ID, see the [Viewing profiles for configuration compliance](#viewing-profiles-for-configuration-compliance "5.2.3. Viewing profiles for configuration compliance") section.

**Procedure**

1.  Scan the local system for compliance with the selected profile and save the scan results to a file:

    ``` {.language-plaintext tabindex="-1"}
    $ oscap xccdf eval --report <scan_report.html> --profile <profile_ID> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    Replace:

    -   *`<scan_report.html>`{.literal}* with the file name where `oscap`{.literal} saves the scan results.
    -   *`<profile_ID>`{.literal}* with the profile ID with which the system should comply, for example, `hipaa`{.literal}.

2.  Optional: Scan a remote system for compliance with the selected profile and save the scan results to a file:

    ``` {.language-plaintext tabindex="-1"}
    $ oscap-ssh <username>@<hostname> <port> xccdf eval --report <scan_report.html> --profile <profile_ID> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    Replace:

    -   *`<username>`{.literal}*`@`{.literal}*`<hostname>`{.literal}* with the user name and hostname of the remote system.
    -   *`<port>`{.literal}* with the port number through which you can access the remote system.
    -   *`<scan_report.html>`{.literal}* with the file name where `oscap`{.literal} saves the scan results.
    -   *`<profile_ID>`{.literal}* with the profile ID with which the system should comply, for example, `hipaa`{.literal}.

**Additional resources**

-   [OpenSCAP memory consumption problems](https://access.redhat.com/articles/6999111)

#### [5.2.5. Assessing security compliance of a container or a container image with a specific baseline](#assessing-security-compliance-of-a-container-or-a-container-image-with-a-specific-baseline) {#assessing-security-compliance-of-a-container-or-a-container-image-with-a-specific-baseline .title}

Assess the compliance of a container or container image with security baselines. Supported baselines include Payment Card Industry Data Security Standard (PCI-DSS) and Health Insurance Portability and Accountability Act (HIPAA). This also helps identify vulnerabilities.

**Prerequisites**

-   The `openscap-utils`{.literal} and `scap-security-guide`{.literal} packages are installed.
-   You have root access to the system.

**Procedure**

1.  Find the ID of a container or a container image:

    a.  To find the ID of a container:

        ``` {.language-plaintext tabindex="-1"}
        # podman ps -a
        ```

    b.  To find the ID of a container image:

        ``` {.language-plaintext tabindex="-1"}
        # podman images
        ```

2.  Evaluate the container or container image against a profile and save the results:

    ``` {.language-plaintext tabindex="-1"}
    # oscap-podman <ID> xccdf eval --report <scan_report.html> --profile <profile_ID> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    Replace:

    -   *`<ID>`{.literal}* with the ID of your container or container image
    -   *`<scan_report.html>`{.literal}* with the file name where `oscap`{.literal} saves the scan results
    -   *`<profile_ID>`{.literal}* with the profile ID with which the system should comply, for example, `hipaa`{.literal} or `pci-dss`{.literal}

**Verification**

-   Open the results in a browser:

    ``` {.language-plaintext tabindex="-1"}
    $ firefox <scan_report.html> &
    ```

    Note

    The rules marked as `notapplicable`{.literal} apply only to bare metal and virtual systems and not to containers or container images.

### [5.3. Configuration compliance remediation](#configuration-compliance-remediation) {#configuration-compliance-remediation .title}

To automatically align your system with a specific profile, you can perform a remediation. You can remediate the system to align with any profile provided by the SCAP Security Guide.

#### [5.3.1. Remediating the system to align with a specific baseline](#remediating-the-system-to-align-with-a-specific-baseline) {#remediating-the-system-to-align-with-a-specific-baseline .title}

Remediate your RHEL system to align with a specific security baseline by using the `oscap xccdf eval --remediate`{.literal} command. This automatically fixes configuration rules defined in the SCAP Security Guide.

For details on listing available profiles, see the [Viewing profiles for configuration compliance](#viewing-profiles-for-configuration-compliance "5.2.3. Viewing profiles for configuration compliance") section.

Warning

Remediations are supported on RHEL systems in the default configuration. Remediating a system that has been altered after installation might render the system nonfunctional or noncompliant with the required security profile. Red Hat does not provide any automated method to revert changes made by security-hardening remediations.

Test the effects of the remediation before applying it on production systems.

**Prerequisites**

-   The `openscap-scanner`{.literal} and `scap-security-guide`{.literal} packages are installed.

**Procedure**

1.  Remediate the system:

    ``` {.language-plaintext tabindex="-1"}
    # oscap xccdf eval --profile <profile_ID> --remediate /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    Replace *`<profile_ID>`{.literal}* with the profile ID with which the system should comply, for example, `hipaa`{.literal}.

2.  Restart your system.

**Verification**

1.  Evaluate compliance of the system with the profile, and save the scan results to a file:

    ``` {.language-plaintext tabindex="-1"}
    $ oscap xccdf eval --report <scan_report.html> --profile <profile_ID> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    Replace:

    -   *`<scan_report.html>`{.literal}* with the file name where `oscap`{.literal} saves the scan results.
    -   *`<profile_ID>`{.literal}* with the profile ID with which the system should comply, for example, `hipaa`{.literal}.

#### [5.3.2. Remediating the system to align with a specific baseline by using an SSG Ansible Playbook](#remediating-the-system-to-align-with-a-specific-baseline-using-an-ssg-ansible-playbook) {#remediating-the-system-to-align-with-a-specific-baseline-by-using-an-ssg-ansible-playbook .title}

Use an Ansible Playbook provided by the SCAP Security Guide project to remediate your system against a specific security baseline. This helps ensure consistency and automation across multiple systems.

Warning

Remediations are supported on RHEL systems in the default configuration. Remediating a system that has been altered after installation might render the system nonfunctional or noncompliant with the required security profile. Red Hat does not provide any automated method to revert changes made by security-hardening remediations.

Test the effects of the remediation before applying it on production systems.

**Prerequisites**

-   The `scap-security-guide`{.literal} package is installed.
-   The `ansible-core`{.literal} package is installed. See the [Ansible Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/) for more information.
-   The `rhc-worker-playbook`{.literal} package is installed.
-   You know the ID of the profile according to which you want to remediate your system. For details, see [Viewing profiles for configuration compliance](#viewing-profiles-for-configuration-compliance "5.2.3. Viewing profiles for configuration compliance").

**Procedure**

1.  Remediate your system to align with a selected profile by using Ansible:

    ``` {.language-plaintext tabindex="-1"}
    # ANSIBLE_COLLECTIONS_PATH=/usr/share/rhc-worker-playbook/ansible/collections/ansible_collections/ ansible-playbook -i "localhost," -c local /usr/share/scap-security-guide/ansible/rhel10-playbook-<profile_ID>.yml
    ```

    The `ANSIBLE_COLLECTIONS_PATH`{.literal} environment variable is necessary for the command to run the playbook.

    Replace *`<profile_ID>`{.literal}* with the profile ID of the selected profile.

2.  Restart the system.

**Verification**

-   Evaluate the compliance of the system with the selected profile, and save the scan results to a file:

    ``` {.language-plaintext tabindex="-1"}
    # oscap xccdf eval --profile <profile_ID> --report <scan_report.html> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    Replace *`<scan_report.html>`{.literal}* with the file name where `oscap`{.literal} saves the scan results.

**Additional resources**

-   [Ansible Documentation](https://docs.ansible.com/)

#### [5.3.3. Creating a remediation Ansible Playbook to align the system with a specific baseline](#creating-a-remediation-ansible-playbook-to-align-the-system-with-a-specific-baseline) {#creating-a-remediation-ansible-playbook-to-align-the-system-with-a-specific-baseline .title}

You can create an Ansible Playbook containing only the remediations required to align your system with a specific baseline. This playbook is smaller because it does not cover requirements that are already satisfied.

Creating the playbook does not modify your system in any way, because you only prepare a file for later application.

**Prerequisites**

-   The `scap-security-guide`{.literal} package is installed.
-   The `ansible-core`{.literal} package is installed. See the [Ansible Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/) for more information.
-   The `rhc-worker-playbook`{.literal} package is installed.
-   You know the ID of the profile according to which you want to remediate your system. For details, see [Viewing profiles for configuration compliance](#viewing-profiles-for-configuration-compliance "5.2.3. Viewing profiles for configuration compliance").

**Procedure**

1.  Scan the system and save the results:

    ``` {.language-plaintext tabindex="-1"}
    # oscap xccdf eval --profile <profile_ID> --results <profile_results.xml> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    Replace: \* *`<profile_ID>`{.literal}* with the profile ID with which the system should comply, for example, `hipaa`{.literal} \* *`<profile_results.xml>`{.literal}* with the path to the file where `oscap`{.literal} saves the results

2.  Find the value of the result ID in the file with the results:

    ``` {.language-plaintext tabindex="-1"}
    # oscap info <profile_results.xml>
    ```

3.  Generate an Ansible Playbook based on the file generated in step 1:

    ``` {.language-plaintext tabindex="-1"}
    # oscap xccdf generate fix --fix-type ansible --result-id xccdf_org.open-scap_testresult_xccdf_org.ssgproject.content_profile_<profile_ID> --output <profile_remediations.yml> <profile_results.xml>
    ```

    Replace *`<profile_remediations.yml>`{.literal}* with the path to the file where `oscap`{.literal} saves rules that failed the scan.

4.  Review the generated *`<profile_remediations.yml>`{.literal}* file.

5.  Remediate your system to align with a selected profile by using Ansible:

    ``` {.language-plaintext tabindex="-1"}
    # ANSIBLE_COLLECTIONS_PATH=/usr/share/rhc-worker-playbook/ansible/collections/ansible_collections/ ansible-playbook -i "localhost," -c local <profile_remediations.yml>`
    ```

    The `ANSIBLE_COLLECTIONS_PATH`{.literal} environment variable is necessary for the command to run the playbook.

    Warning

    Remediations are supported on RHEL systems in the default configuration. Remediating a system that has been altered after installation might render the system nonfunctional or noncompliant with the required security profile. Red Hat does not provide any automated method to revert changes made by security-hardening remediations.

    Test the effects of the remediation before applying it on production systems.

**Verification**

-   Evaluate the compliance of the system with the selected profile, and save the scan results to a file:

    ``` {.language-plaintext tabindex="-1"}
    # oscap xccdf eval --profile <profile_ID> --report <scan_report.html> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    Replace *`<scan_report.html>`{.literal}* with the file name where `oscap`{.literal} saves the scan results.

**Additional resources**

-   [Ansible Documentation](https://docs.ansible.com/)

### [5.4. Performing a hardened installation of RHEL with Kickstart](#performing-a-hardened-installation-of-rhel-with-kickstart) {#performing-a-hardened-installation-of-rhel-with-kickstart .title}

To make your system compliant with a specific security profile, such as DISA STIG, CIS, or ANSSI, you can prepare a Kickstart file that defines the hardened configuration. Customize it with a tailoring file, and run an automated installation of the hardened system.

**Prerequisites**

-   The `openscap-scanner`{.literal} is installed on your system.
-   The `scap-security-guide`{.literal} package is installed on your system, and the package version corresponds to the version of RHEL that you want to install. Because all supported RHEL versions use the same SCAP Security Guide version, update the package before generating the Kickstart file.

**Procedure**

1.  Find the ID of the security profile from the data stream file:

    ``` {.language-plaintext tabindex="-1"}
    $ oscap info /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    Profiles:
    …
      Title: Australian Cyber Security Centre (ACSC) Essential Eight
        Id: xccdf_org.ssgproject.content_profile_e8
      Title: Health Insurance Portability and Accountability Act (HIPAA)
        Id: xccdf_org.ssgproject.content_profile_hipaa
      Title: PCI-DSS v3.2.1 Control Baseline for Red Hat Enterprise Linux 10
        Id: xccdf_org.ssgproject.content_profile_pci-dss
    …
    ```

2.  Optional: If you want to customize your hardening with XCCDF Tailoring file you can use the `autotailor`{.literal} command provided in the `openscap-utils`{.literal} package. For more information, see [Customizing a security profile with autotailor](#customizing-a-security-profile-with-autotailor "5.5. Customizing a security profile with autotailor").

3.  Generate the Kickstart file from the SCAP source data stream:

    ``` {.language-plaintext tabindex="-1"}
    $ oscap xccdf generate fix --profile <profile_ID> --output <kickstart_file>.cfg --fix-type kickstart /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    Replace *`<profile_ID>`{.literal}* with the profile ID with which the system should comply, for example, `hipaa`{.literal}.

    If you are using a tailoring file, embed the tailoring file into the generated Kickstart file by using the `--tailoring-file tailoring.xml`{.literal} option and your custom profile ID, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ oscap xccdf generate fix --tailoring-file tailoring.xml --profile <custom_profile_ID> --output <kickstart_file>.cfg --fix-type kickstart ./ssg-rhel10-ds.xml
    ```

4.  Review and, if necessary, manually modify the generated *`<kickstart_file>.cfg`{.literal}* to fit the needs of your deployment. Follow the instructions in the comments in the file.

    Note

    Some changes might affect the compliance of the systems installed by the Kickstart file. For example, some security policies require defined partitions or specific packages and services.

5.  Use the Kickstart file for your installation. For the installation program to use the Kickstart, the Kickstart can be served through a web server, provided in PXE, or embedded into the ISO image. For detailed steps, see the [Semi-automated installations: Making Kickstart files available to the RHEL installer](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/semi-automated-installations-making-kickstart-files-available-to-the-rhel-installer) chapter in the Automatically installing RHEL document.

6.  After the installation finishes, the system reboots automatically. After the reboot, log in and review the installation SCAP report saved in the `/root`{.literal} directory.

**Verification**

-   Scan the system for compliance and save the report in a HTML file for review:

    -   With the original profile:

        ``` {.language-plaintext tabindex="-1"}
        # oscap xccdf eval --report report.html --profile <profile_ID> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
        ```

    -   With the tailored profile:

        ``` {.language-plaintext tabindex="-1"}
        # oscap xccdf eval --report report.html --tailoring-file tailoring.xml --profile <custom_profile_ID> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
        ```

### [5.5. Customizing a security profile with autotailor](#customizing-a-security-profile-with-autotailor) {#customizing-a-security-profile-with-autotailor .title}

To align with internal security standards, you can customize a RHEL security profile by selecting or removing existing rules. While you can modify parameters such as password length, you cannot define entirely new rules during customization.

By using the `autotailor`{.literal} utility, you create an XCCDF tailoring file that contains all of the modifications of the original profile. Then, when you are scanning, remediating, or installing a system in accordance with a SCAP profile, you pass this tailoring file to the `oscap`{.literal} command-line utility.

Note that you cannot define new rules when customizing a profile.

**Prerequisites**

-   The `openscap-utils`{.literal} package is installed on your system.
-   You know the ID of the profile within the baseline which you want to customize. To find the ID, see the [Viewing profiles for configuration compliance](#viewing-profiles-for-configuration-compliance "5.2.3. Viewing profiles for configuration compliance") section.

**Procedure**

1.  Create a tailoring file for your profile by using the `autotailor`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ autotailor \ --select=<rule_ID_1> \ --select=<rule_ID_2> \ --unselect=<rule_ID_3> \ --var-value=<value_ID_1>=<value_1> \ --var-value=<value_ID_2>=<value_2> \ --output=<tailoring.xml> \ --tailored-profile-id=<custom_profile_ID> \ /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml <profile_ID>
    ```

    Where:

    -   *`<customization_options>`{.literal}* are the modifications of the profile. Use one or more of the following options:

        `--select=`{.literal}*`<rule_ID>`{.literal}*
        :   Add an existing rule to the profile.

        `--unselect=`{.literal}*`<rule_ID>`{.literal}*
        :   Remove a rule from the profile.

        `--var-value=`{.literal}*`<value_ID>`{.literal}*`=`{.literal}*`<value>`{.literal}*
        :   Override a pre-set value. For example, to set `var_sshd_max_sessions`{.literal} to `10`{.literal}, use `--var-value=var_sshd_max_sessions=10`{.literal}.

    -   *`<tailoring.xml>`{.literal}* is the file name where `autotailor`{.literal} saves the tailoring.

    -   *`<custom_profile_ID>`{.literal}* is the profile ID within which the `autotailor`{.literal} saves customizations, for example, `custom_cis`{.literal}.

    -   *`<profile_ID>`{.literal}* is the profile ID with which the system should comply, for example, `cis`{.literal}.

    Note

    For all profile, rule, and variable XCCDF IDs, you can use either a full namespaced identifier or a shortened ID that `autotailor`{.literal} automatically augments with the namespace prefix. For example, `cis`{.literal} is equivalent to `xccdf_org.ssgproject.content_profile_cis`{.literal}.

    You can override the default namespace `org.ssgproject.content`{.literal} by using the `--id-namespace`{.literal} option.

2.  Optional: Create a tailoring file based on the customizations defined in the [JSON Tailoring](https://github.com/ComplianceAsCode/schemas/blob/v2/tailoring/schema.json) format:

    ``` {.language-plaintext tabindex="-1"}
    $ autotailor --output=<tailoring.xml> --json-tailoring=<json_tailoring.json>
    ```

    Replace *`<json_tailoring.json>`{.literal}* with the file name with JSON Tailoring definitions.

    Note

    You can mix `--json-tailoring`{.literal} with `--select`{.literal}, `--unselect`{.literal}, and `--var-value`{.literal} command-line customizations. In that case, command-line customizations have priority over JSON Tailoring.

### [5.6. SCAP Security Guide profiles supported in RHEL 10](#scap-security-guide-profiles-supported-in-rhel-10) {#scap-security-guide-profiles-supported-in-rhel-10 .title}

Review the SCAP Security Guide profiles supported in RHEL 10, such as HIPAA, STIG, and CIS. To accommodate hardening components updated with new capabilities, use only the SCAP content provided in your specific minor release.

SCAP content changes to reflect these updates, but it is not always compatible with earlier versions.

Note

You can get the information relevant for the version of `scap-security-guide`{.literal} RPM installed on your system by using the `oscap info`{.literal} command. For more information, see [Viewing profiles for configuration compliance](#viewing-profiles-for-configuration-compliance "5.2.3. Viewing profiles for configuration compliance").

+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Profile name                                                                                                                        | Profile ID                                                                               | Policy version       |
+:====================================================================================================================================+:=========================================================================================+:=====================+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Enhanced Level                                        | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_enhanced`{.literal}**     | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 High Level                                            | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_high`{.literal}**         | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Intermediary Level                                    | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_intermediary`{.literal}** | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Minimal Level                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_minimal`{.literal}**      | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| BSI SYS.1.1 and SYS.1.3                                                                                                             | `xccdf_org.ssgproject.content_profile_`{.literal}**`bsi`{.literal}**                     | 2022                 |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 2 - Server                                                                      | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis`{.literal}**                     | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 1 - Server                                                                      | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_server_l1`{.literal}**           | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 1 - Workstation                                                                 | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_workstation_l1`{.literal}**      | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 2 - Workstation                                                                 | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_workstation_l2`{.literal}**      | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) Essential Eight                                                                             | `xccdf_org.ssgproject.content_profile_`{.literal}**`e8`{.literal}**                      | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Health Insurance Portability and Accountability Act (HIPAA)                                                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`hipaa`{.literal}**                   | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Base                                                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o`{.literal}**                   | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Secret                                                                       | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o_secret`{.literal}**            | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Top Secret                                                                   | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o_top_secret`{.literal}**        | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| PCI-DSS v4.0.1 Control Baseline for Red Hat Enterprise Linux 10                                                                     | `xccdf_org.ssgproject.content_profile_`{.literal}**`pci-dss`{.literal}**                 | 4.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| The Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat Enterprise Linux 10          | `xccdf_org.ssgproject.content_profile_`{.literal}**`stig`{.literal}**                    | V1R2                 |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| The Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) with GUI for Red Hat Enterprise Linux 10 | `xccdf_org.ssgproject.content_profile_`{.literal}**`stig_gui`{.literal}**                | V1R2                 |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+

: Table 5.1. SCAP Security Guide profiles supported in RHEL 10.3

Show more

+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Profile name                                                                                                                        | Profile ID                                                                               | Policy version       |
+:====================================================================================================================================+:=========================================================================================+:=====================+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Enhanced Level                                        | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_enhanced`{.literal}**     | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 High Level                                            | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_high`{.literal}**         | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Intermediary Level                                    | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_intermediary`{.literal}** | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Minimal Level                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_minimal`{.literal}**      | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| BSI SYS.1.1 and SYS.1.3                                                                                                             | `xccdf_org.ssgproject.content_profile_`{.literal}**`bsi`{.literal}**                     | 2022                 |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 2 - Server                                                                      | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis`{.literal}**                     | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 1 - Server                                                                      | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_server_l1`{.literal}**           | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 1 - Workstation                                                                 | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_workstation_l1`{.literal}**      | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 2 - Workstation                                                                 | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_workstation_l2`{.literal}**      | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) Essential Eight                                                                             | `xccdf_org.ssgproject.content_profile_`{.literal}**`e8`{.literal}**                      | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Health Insurance Portability and Accountability Act (HIPAA)                                                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`hipaa`{.literal}**                   | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Base                                                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o`{.literal}**                   | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Secret                                                                       | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o_secret`{.literal}**            | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Top Secret                                                                   | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o_top_secret`{.literal}**        | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| PCI-DSS v4.0.1 Control Baseline for Red Hat Enterprise Linux 10                                                                     | `xccdf_org.ssgproject.content_profile_`{.literal}**`pci-dss`{.literal}**                 | 4.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| The Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat Enterprise Linux 10          | `xccdf_org.ssgproject.content_profile_`{.literal}**`stig`{.literal}**                    | V1R2                 |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| The Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) with GUI for Red Hat Enterprise Linux 10 | `xccdf_org.ssgproject.content_profile_`{.literal}**`stig_gui`{.literal}**                | V1R2                 |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+

: Table 5.2. SCAP Security Guide profiles supported in RHEL 10.2

Show more

+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Profile name                                                                                                                        | Profile ID                                                                               | Policy version       |
+:====================================================================================================================================+:=========================================================================================+:=====================+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Enhanced Level                                        | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_enhanced`{.literal}**     | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 High Level                                            | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_high`{.literal}**         | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Intermediary Level                                    | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_intermediary`{.literal}** | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Minimal Level                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_minimal`{.literal}**      | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| BSI SYS.1.1 and SYS.1.3                                                                                                             | `xccdf_org.ssgproject.content_profile_`{.literal}**`bsi`{.literal}**                     | 2022                 |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 2 - Server                                                                      | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis`{.literal}**                     | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 1 - Server                                                                      | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_server_l1`{.literal}**           | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 1 - Workstation                                                                 | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_workstation_l1`{.literal}**      | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 2 - Workstation                                                                 | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_workstation_l2`{.literal}**      | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) Essential Eight                                                                             | `xccdf_org.ssgproject.content_profile_`{.literal}**`e8`{.literal}**                      | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Health Insurance Portability and Accountability Act (HIPAA)                                                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`hipaa`{.literal}**                   | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Base                                                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o`{.literal}**                   | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Secret                                                                       | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o_secret`{.literal}**            | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Top Secret                                                                   | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o_top_secret`{.literal}**        | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| PCI-DSS v4.0.1 Control Baseline for Red Hat Enterprise Linux 10                                                                     | `xccdf_org.ssgproject.content_profile_`{.literal}**`pci-dss`{.literal}**                 | 4.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| The Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat Enterprise Linux 10          | `xccdf_org.ssgproject.content_profile_`{.literal}**`stig`{.literal}**                    | vendor               |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| The Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) with GUI for Red Hat Enterprise Linux 10 | `xccdf_org.ssgproject.content_profile_`{.literal}**`stig_gui`{.literal}**                | vendor               |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+

: Table 5.3. SCAP Security Guide profiles supported in RHEL 10.1

Show more

+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Profile name                                                                                                                        | Profile ID                                                                               | Policy version       |
+:====================================================================================================================================+:=========================================================================================+:=====================+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Enhanced Level                                        | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_enhanced`{.literal}**     | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 High Level                                            | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_high`{.literal}**         | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Intermediary Level                                    | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_intermediary`{.literal}** | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| French National Agency for the Security of Information Systems (ANSSI) BP-028 Minimal Level                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`anssi_bp28_minimal`{.literal}**      | 2.0                  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| BSI SYS.1.1 and SYS.1.3                                                                                                             | `xccdf_org.ssgproject.content_profile_`{.literal}**`bsi`{.literal}**                     | 2022                 |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 2 - Server                                                                      | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis`{.literal}**                     | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 1 - Server                                                                      | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_server_l1`{.literal}**           | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 1 - Workstation                                                                 | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_workstation_l1`{.literal}**      | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| CIS Red Hat Enterprise Linux 10 Benchmark for Level 2 - Workstation                                                                 | `xccdf_org.ssgproject.content_profile_`{.literal}**`cis_workstation_l2`{.literal}**      | 1.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) Essential Eight                                                                             | `xccdf_org.ssgproject.content_profile_`{.literal}**`e8`{.literal}**                      | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Health Insurance Portability and Accountability Act (HIPAA)                                                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`hipaa`{.literal}**                   | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Base                                                                         | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o`{.literal}**                   | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Secret                                                                       | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o_secret`{.literal}**            | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| Australian Cyber Security Centre (ACSC) ISM Official - Top Secret                                                                   | `xccdf_org.ssgproject.content_profile_`{.literal}**`ism_o_top_secret`{.literal}**        | not versioned        |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| PCI-DSS v4.0.1 Control Baseline for Red Hat Enterprise Linux 10                                                                     | `xccdf_org.ssgproject.content_profile_`{.literal}**`pci-dss`{.literal}**                 | 4.0.1                |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| The Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat Enterprise Linux 10          | `xccdf_org.ssgproject.content_profile_`{.literal}**`stig`{.literal}**                    | V1R2                 |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+
| The Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) with GUI for Red Hat Enterprise Linux 10 | `xccdf_org.ssgproject.content_profile_`{.literal}**`stig_gui`{.literal}**                | V1R2                 |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+----------------------+

: Table 5.4. SCAP Security Guide profiles supported in RHEL 10.0

Show more

### [5.7. Additional resources](#scanning-the-system-for-configuration-compliance_57-additional-resources) {#additional-resources-1 .title}

-   [The OpenSCAP project page](http://www.open-scap.org)
-   [The SCAP Security Guide (SSG) project page](https://www.open-scap.org/security-policies/scap-security-guide/)
-   [Using OpenSCAP for security compliance and vulnerability scanning - aA hands-on lab](https://lab.redhat.com/tracks/openscap)
-   [Red Hat Security Demos: Creating Customized Security Policy Content to Automate Security Compliance](https://2020-summit-labs.gitlab.io/rhel-custom-security-content/)
-   [Red Hat Security Demos: Defend Yourself with RHEL Security Technologies](https://github.com/RedHatDemos/SecurityDemos/blob/master/2020Labs/RHELSecurity/documentation/README.adoc)
-   [National Institute of Standards and Technology (NIST) SCAP page](http://scap.nist.gov/)
-   [Managing security compliance in Red Hat Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.18/html/managing_security_compliance/index)

## [Chapter 6. Ensuring system integrity with Keylime](#ensuring-system-integrity-with-keylime) {#chapter-6.-ensuring-system-integrity-with-keylime .title}

With Keylime, you can continuously monitor the integrity of remote systems and verify the state of systems at boot. You can also send encrypted files to the monitored systems, and specify automated actions triggered whenever a monitored system fails the integrity test.

### [6.1. Remote system integrity monitoring](#remote-system-integrity-monitoring) {#remote-system-integrity-monitoring .title}

To quickly detect unauthorized changes and verify that your remote infrastructure is in a trusted state, use Keylime to monitor system integrity. With Keylime, you can continuously validate your systems by comparing measurements of boot components and runtime files against a known-good baseline.

#### [6.1.1. Components and mechanisms for remote system validation](#how-keylime-works) {#components-and-mechanisms-for-remote-system-validation .title}

To establish a trusted cryptographic foundation for remote attestation in RHEL, you rely on the Keylime architecture. Its core components, the verifier, registrar, tenant, and agent, interact with Trusted Platform Module (TPM) technology to dynamically build and maintain a continuous chain of trust.

A TPM acts as the root of this trust. It is a hardware, firmware, or virtual component with integrated cryptographic keys.

Important

Keylime running in a virtual machine or using a virtual TPM depends upon the integrity of the underlying host. Ensure you trust the host environment before relying upon Keylime measurements in a virtual environment.

To achieve your system security goals, you can configure agents to perform the following monitoring actions:

Verify system state at boot
:   Keylime measured boot verifies the system state when the system boots.

Continuously monitor runtime integrity
:   Keylime runtime integrity monitoring continuously monitors the system where the agent is deployed and measures the integrity of the files included in the allowlist and not included in the excludelist.

To perform these actions, the system relies on three main components:

Verifier
:   Initially and continuously verifies the integrity of the systems that run the agent. You can deploy the verifier from a package, as a container, or by using the `keylime_server`{.literal} RHEL system role.

Registrar
:   Serves as a secure database that stores the unique TPM identity data for all registered agents, including their Endorsement Key (EK), Attestation Key (AK), and related identification certificates. You can deploy the registrar from a package, as a container, or by using the `keylime_server`{.literal} RHEL system role.

Agent
:   Deployed to the remote systems that are measured by the verifier.

In addition, you can use the `keylime_tenant`{.literal} utility for many functions, including provisioning the agents on your target systems.

#### [6.1.2. Keylime attestation models for remote monitoring](#keylime-attestation-models-for-remote-monitoring) {#keylime-attestation-models-for-remote-monitoring .title}

To establish a trusted remote monitoring strategy for your infrastructure, you use either the pull or push attestation model. You achieve the same goal of system integrity validation with either option, although they operate by using different network mechanics and scaling behaviors.

The pull model

:   Traditional Keylime attestation uses the pull model, where the verifier service initiates the attestation process by periodically polling remote systems. The verifier establishes an inbound network connection to the Keylime agent to retrieve Trusted Platform Module (TPM) quotes, Integrity Measurement Architecture (IMA) logs, and the UEFI event log. The pull model uses mutual TLS (mTLS) authentication to ensure secure communication between Keylime components. The verifier holds the connection open while retrieving and evaluating the measurements. It validates the TPM quote by checking its cryptographic signature against the agent's registered attestation key, which confirms that the reported PCR values are authentic and untampered. It then replays each event log to reconstruct expected PCR values and compares them against the values reported in the quote. During UEFI event log evaluation, the verifier validates the boot sequence by checking each boot component measurement against a reference state. When evaluating the IMA log, it detects unauthorized or modified software by comparing recorded file measurements against the runtime policy. If any reconstructed PCR value does not match the quote, or if any measurement fails a policy check, the attestation fails.

    The pull model provides almost instant detection of network or Keylime agent failures, but it requires each monitored node to be reachable and have the necessary inbound ports open. By using this model, you can also deploy secure payloads to send encrypted information or configuration files to agents as soon as they are verified.

    **Figure 6.1. Connections between Keylime components through configurations in the pull model**

    Keylime ensures the integrity of the monitored systems in a chain of trust by using keys and certificates exchanged between the components and the tenant. For a secure foundation of this chain, use a certificate authority (CA) that you can trust.

    Note

    If the agent receives no key and certificate, it generates a key and a self-signed certificate with no involvement from the CA.

    **Figure 6.2. Connections between Keylime components certificates and keys in the pull model**

The push model

:   In push model attestation, the Keylime verifier operates as a passive validator. The Keylime agent service initiates the attestation process by sending measurements to the verifier at a defined interval. The agent establishes an outbound connection to the verifier to provide the necessary TPM quotes, IMA logs, and the UEFI event log. The push model uses a TPM challenge-and-response process, Proof of Possession (PoP), to verify agent authenticity. Unlike in the pull model, the verifier acknowledges receipt of the data immediately and processes attestation results independently. It validates the TPM quote by checking its cryptographic signature against the agent's registered attestation key, which confirms that the reported PCR values are authentic and untampered. It then replays each event log to reconstruct expected PCR values and compares them against the values reported in the quote. During UEFI event log evaluation, the verifier validates the boot sequence by checking each boot component measurement against a reference state. When evaluating the IMA log, it detects unauthorized or modified software by comparing recorded file measurements against the runtime policy. If any reconstructed PCR value does not match the quote, or if any measurement fails a policy check, the attestation fails.

    The verifier never connects to the agent, which makes the push model suitable specifically for edge computing and NAT-protected environments where the verifier service cannot directly reach the remote systems. Although the push model increases security by removing inbound ports, it does not support the delivery of secure payloads.

    **Figure 6.3. Connections between Keylime components certificates and keys in the push model**

    **Figure 6.4. Differences between network configuration for the pull and push model**

The technical specifications for each model detail their operational differences.

+--------------------------+-----------------------------------------------------------+------------------------------------------------------+
| Attribute                | Pull model (default)                                      | Push model                                           |
+:=========================+:==========================================================+:=====================================================+
| **Initiator**            | The Keylime verifier requests data from the Keylime agent | The Keylime agent sends data to the Keylime verifier |
+--------------------------+-----------------------------------------------------------+------------------------------------------------------+
| **Agent package**        | `keylime-agent-rust`{.literal}                            | `keylime-agent-rust-push`{.literal}                  |
+--------------------------+-----------------------------------------------------------+------------------------------------------------------+
| **Network direction**    | Inbound to the Keylime agent (port 9002)                  | Inbound to the Keylime verifier (port 8881)          |
+--------------------------+-----------------------------------------------------------+------------------------------------------------------+
| **Agent listening port** | Yes (9002 must be open)                                   | No                                                   |
+--------------------------+-----------------------------------------------------------+------------------------------------------------------+
| **Scalability**          | Limited by verifier's polling capacity                    | High (load is distributed across agents)             |
+--------------------------+-----------------------------------------------------------+------------------------------------------------------+
| **Real-time detection**  | Immediate (verifier knows if poll fails)                  | Delayed (based on timeouts)                          |
+--------------------------+-----------------------------------------------------------+------------------------------------------------------+
| **API version**          | REST API 2.x                                              | REST API 3.0 (asynchronous)                          |
+--------------------------+-----------------------------------------------------------+------------------------------------------------------+

: Table 6.1. Technical specifications for Keylime attestation models

Show more

#### [6.1.3. Considerations for choosing the right Keylime attestation model](#considerations-for-choosing-the-right-keylime-attestation-model) {#considerations-for-choosing-the-right-keylime-attestation-model .title}

To determine the best fit for your architecture, from stable data centers to edge deployments, you can assess how specific network use cases and environmental factors align with each Keylime attestation model. This choice directly affects how you configure the verifier and agents.

The **pull model** is best suited for environments where the network is managed, stable, and transparent.

-   Corporate data centers: Best for servers on a flat, internal network where the verifier has direct access to every node.
-   Isolated air-gapped networks: Ideal for high-security environments where the verifier strictly controls all communication.
-   Secret and script delivery (secure payloads): Required if the verifier must deliver sensitive configuration files, keys, or scripts to the agent immediately after a successful attestation.
-   Centralized monitoring architecture: Preferred when integrating with existing infrastructure management tools that rely on a central server to poll or ping clients for status updates.
-   Real-time failure forensics: Used when the verifier must immediately detect a network drop or an agent service failure, which is critical for high-availability systems.

The **push model** is designed for distributed, restricted, or dynamic network architectures.

-   Edge and Internet of Things (IoT) deployments: Ideal for devices in remote branches or field locations that must connect to the verifier through external gateways.
-   Cloud instances behind NAT: Used for virtual machines in public clouds that have outbound internet access but lack a public IP address for inbound connections.
-   Zero trust device onboarding: Best for environments where devices must prove their integrity to a central service before receiving access to network resources.
-   Hardened stealth nodes: Used when security policies forbid any listening services or open inbound ports on the monitored system to minimize the attack surface.
-   Massively scalable fleets: Preferred for environments with tens of thousands of agents, because it offloads the scheduling and timing tasks from the verifier to the individual nodes.
-   Dynamic network environments: Ideal for mobile devices or systems with frequently changing IP addresses, because the agent initiates the connection regardless of its current network location.

The following factors determine whether to use the pull or push attestation model:

+-----------------------------------+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Decision factor                   | Pull model (default)                                                            | Push model                                                                             |
+:==================================+:================================================================================+:=======================================================================================+
| **Network reachability**          | Requires direct network access from the verifier to agents.                     | Works across complex network topologies, NATs, and firewalls.                          |
+-----------------------------------+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| **Inbound firewall requirements** | Requires opening an inbound port on each agent node.                            | Requires no open inbound ports on agent nodes.                                         |
+-----------------------------------+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| **Scalability**                   | Lower (the verifier manages polling timers and connection load for every agent) | Higher (attestation scheduling is offloaded to agents, which increases fleet capacity) |
+-----------------------------------+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| **Failure detection**             | Active polling (verifier detects unreachable agents during scheduled polls)     | Timeout-based (verifier flags agents that miss scheduled push intervals)               |
+-----------------------------------+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| **Deployment environment**        | Static data centers with fixed IP addresses                                     | Edge, IoT, dynamic, and public cloud environments                                      |
+-----------------------------------+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

: Table 6.2. Decision factors for Keylime attestation models

Show more

### [6.2. Deploying Keylime verifier from a package](#deploying-keylime-verifier-from-a-package) {#deploying-keylime-verifier-from-a-package .title}

Deploy the Keylime verifier from a package to establish the core integrity monitoring component. The verifier acts as the verification authority for target systems - agents.

The verifier is the most critical component in Keylime. It performs initial and periodic checks of system integrity to ensure that monitored agents remain in a trusted state. In the pull model, the verifier also supports bootstrapping cryptographic keys and secure payloads with the agent.

The behavior of the Keylime verifier depends on the selected attestation model:

Pull model
:   The verifier actively polls the agent. It initiates an outbound connection and waits for a response before evaluating the measurements.

Push model
:   The verifier acts as a listener for inbound connections from agents. It accepts the incoming data, acknowledges it immediately, and evaluates the measurements independently. This decoupled approach allows the verifier to handle a significantly higher volume of requests without keeping connections open while processing the data.

Important

To maintain the chain of trust, keep the system that runs the verifier secure and under your control.

You can install the verifier on a separate system or on the same system as the Keylime registrar, depending on your requirements. Running the verifier and registrar on separate systems provides better performance.

Note

To keep the configuration files organized within the drop-in directories, use file names with a two-digit number prefix, for example `/etc/keylime/verifier.conf.d/00-verifier-ip.conf`{.literal}. The configuration processing reads the files inside the drop-in directory in lexicographic order and sets each option to the last value it reads.

**Prerequisites**

-   You have `root`{.literal} permissions and network connection to the system or systems on which you want to install Keylime components.

-   You have valid keys and certificates from your certificate authority.

-   If you use pull model attestation:

    -   The verifier's host has outbound access to all monitored agents on port 9002.
    -   The verifier's host is reachable on port 8881 by the tenant.
    -   The verifier has both server and client certificates for mTLS.

-   If you use push model attestation:

    -   The verifier's host is reachable on port 8881 by all monitored agents and the tenant.
    -   The verifier has a server certificate to prove its own identity to agents.

-   Optional: You have access to the databases where Keylime saves data from the verifier. You can use any of the following database management systems:

    -   SQLite (default)
    -   PostgreSQL
    -   MySQL
    -   MariaDB

**Procedure**

1.  Install the Keylime verifier:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install keylime-verifier
    ```

2.  Define the IP address and port of verifier by creating a new `.conf`{.literal} file in the `/etc/keylime/verifier.conf.d/`{.literal} directory, for example, `/etc/keylime/verifier.conf.d/00-verifier-ip.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [verifier]
    ip = <verifier_IP_address>
    ```

    -   Replace *`<verifier_IP_address>`{.literal}* with the verifier's IP address. Alternatively, use `ip = *`{.literal} or `ip = 0.0.0.0`{.literal} to bind the verifier to all available IP addresses.
    -   Optionally, you can also change the verifier's port from the default value `8881`{.literal} by using the `port`{.literal} option.

3.  Optional: Configure the verifier's database. The default configuration uses an SQLite database in the verifier's `/var/lib/keylime/cv_data.sqlite/`{.literal} directory. You can define a different database by creating a new `.conf`{.literal} file in the `/etc/keylime/verifier.conf.d/`{.literal} directory, for example, `/etc/keylime/verifier.conf.d/00-db-url.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [verifier]
    database_url = <protocol>://<name>:<password>@<ip_address_or_hostname>/<properties>
    ```

    Replace *`<protocol>://<name>:<password>@<ip_address_or_hostname>/<properties>`{.literal}* with the URL of the database, for example, `postgresql://verifier:UQ?nRNY9g7GZzN7@198.51.100.1/verifierdb`{.literal}.

    Ensure that the credentials you use provide the permissions for Keylime to create the database structure.

4.  Add certificates and keys to the verifier. You can either let Keylime generate them, or use existing keys and certificates:

    -   With the default `tls_dir = generate`{.literal} option, Keylime generates new certificates for the verifier, registrar, and tenant in the `/var/lib/keylime/cv_ca/`{.literal} directory.

    -   To load existing keys and certificates in the configuration, define their location in the verifier configuration. The certificates must be accessible by the `keylime`{.literal} user, under which the Keylime services are running.

        Create a new `.conf`{.literal} file in the `/etc/keylime/verifier.conf.d/`{.literal} directory, for example, `/etc/keylime/verifier.conf.d/00-keys-and-certs.conf`{.literal}, with the following content:

        ``` {.language-plaintext tabindex="-1"}
        [verifier]
        tls_dir = /var/lib/keylime/cv_ca
        server_key = </path/to/server_key>
        server_key_password = <passphrase1>
        server_cert = </path/to/server_cert>
        trusted_client_ca = ['</path/to/ca/cert1>', '</path/to/ca/cert2>']
        client_key = </path/to/client_key>
        client_key_password = <passphrase2>
        client_cert = </path/to/client_cert>
        trusted_server_ca = ['</path/to/ca/cert3>', '</path/to/ca/cert4>']
        ```

        Note

        Use absolute paths to define key and certificate locations. Alternatively, relative paths are resolved from the directory defined in the `tls_dir`{.literal} option.

5.  **For push model only:** Configure the verifier for the push model attestation.

    Note

    The mode setting affects all agents on the verifier. A verifier in push mode expects agents to submit attestation data, it does not poll agents. A single verifier cannot operate in both modes simultaneously.

    You can either use a drop-in configuration file, set the mode in the verifier's configuration file, or use an environment variable:

    -   Set the verifier's `mode`{.literal} option by creating a new `.conf`{.literal} file in the `/etc/keylime/verifier.conf.d/`{.literal} directory, for example, `/etc/keylime/verifier.conf.d/00-push-mode.conf`{.literal}, with the following content:

        ``` {.language-plaintext tabindex="-1"}
        [verifier]
        mode = push
        ```

    -   Set the verifier's `mode`{.literal} option to `push`{.literal} in the `./etc/keylime/verifier.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [verifier]
        mode = push
        ```

    -   To configure the verifier by using environment variable, inject the variable directly into the `systemd`{.literal} service environment.

        Open the `systemd`{.literal} configuration editor for the verifier service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl edit keylime_verifier
        ```

        Add the variable to the `Service`{.literal} environment:

        ``` {.language-plaintext tabindex="-1"}
        [Service]
        Environment="KEYLIME_VERIFIER_MODE=push"
        ```

        After you save the changes, the `systemd`{.literal} service automatically updates and reloads the modified verifier service profile.

6.  Open the port in firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-port 8881/tcp
    # firewall-cmd --runtime-to-permanent
    ```

    If you use a different port, replace `8881`{.literal} with the port number defined in the `.conf`{.literal} file.

7.  Start the verifier service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now keylime_verifier
    ```

    Note

    In the default configuration, start the `keylime_verifier`{.literal} before starting the `keylime_registrar`{.literal} service because the verifier creates the CA and certificates for the other Keylime components. This order is not necessary when you use custom certificates.

**Verification**

1.  Check that the `keylime_verifier`{.literal} service is active and running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status keylime_verifier
    ```

    ``` {.language-plaintext tabindex="-1"}
    keylime_verifier.service - The Keylime verifier
         Loaded: loaded (/usr/lib/systemd/system/keylime_verifier.service; disabled; vendor preset: disabled)
         Active: active (running) since Wed 2022-11-09 10:10:08 EST; 1min 45s ago
    ```

2.  **For push model only:** Check that the verifier is configured for push model attestation:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u keylime_verifier -b
    ...
    keylime.verifier - INFO - Starting Keylime verifier in PUSH mode...
    ...
    ```

**Next steps**

-   [Deploying the Keylime registrar from a package](#deploying-keylime-registrar-from-a-package "6.4. Deploying Keylime registrar from a package").

### [6.3. Deploying Keylime verifier as a container](#deploying-keylime-verifier-as-a-container) {#deploying-keylime-verifier-as-a-container .title}

Configure the Keylime verifier as a container instead of the RPM method, without any binaries or packages on the host. The container deployment provides better isolation, modularity, and reproducibility of Keylime components.

The Keylime verifier performs initial and periodic checks of system integrity to ensure monitored agents remain in a trusted state. In the pull model, the verifier also supports bootstrapping cryptographic keys and delivering secure payloads to the agent.

The behavior of the Keylime verifier depends on the selected attestation model:

The pull model
:   The verifier actively polls the agent. It initiates an outbound connection and waits for a response before evaluating the measurements.

The push model
:   The verifier acts as a listener for inbound connections from agents. It accepts the incoming data, acknowledges it immediately, and evaluates the measurements independently. This decoupled approach allows the verifier to handle a significantly higher volume of requests without keeping connections open while processing the data.

After you start the container, the Keylime verifier is deployed with default configuration files. You can customize the configuration by using one or more of following methods:

-   Mounting the host's directories that contain the configuration files to the container.
-   Modifying the environment variables directly on the container. Modifying the environment variables overrides the values from the configuration files.

**Prerequisites**

-   The `podman`{.literal} package and its dependencies are installed on the system.

-   The user that executes `podman`{.literal} commands has read access to the local configuration files and certificates that will be mounted into the container.

-   If you use pull model attestation:

    -   The verifier's host has outbound access to all monitored agents on port 9002.
    -   The verifier's host is reachable on port 8881 by the tenant.
    -   The verifier has both server and client certificates for mTLS.

-   If you use push model attestation:

    -   The verifier's host is reachable on port 8881 by all monitored agents and the tenant.
    -   The verifier has a server certificate to prove its own identity to agents.

-   Optional: You have access to a database where Keylime saves data from the verifier. You can use any of the following database management systems:

    -   SQLite (default)
    -   PostgreSQL
    -   MySQL
    -   MariaDB

-   You have valid keys and certificates from your certificate authority.

**Procedure**

1.  Optional: Install the `keylime-verifier`{.literal} package to access the configuration files. You can configure the container without this package, but it might be easier to modify the configuration files provided with the package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install keylime-verifier
    ```

2.  Bind the verifier to all available IP addresses by creating a new `.conf`{.literal} file in the `/etc/keylime/verifier.conf.d/`{.literal} directory, for example, `/etc/keylime/verifier.conf.d/00-verifier-ip.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [verifier]
    ip = *
    ```

    -   Optionally, you can also change the verifier's port from the default value `8881`{.literal} by using the `port`{.literal} option.

3.  Optional: Configure the verifier's database. The default configuration uses an SQLite database in the verifier's `/var/lib/keylime/cv_data.sqlite/`{.literal} directory. You can define a different database by creating a new `.conf`{.literal} file in the `/etc/keylime/verifier.conf.d/`{.literal} directory, for example, `/etc/keylime/verifier.conf.d/00-db-url.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [verifier]
    database_url = <protocol>://<name>:<password>@<ip_address_or_hostname>/<properties>
    ```

    Replace *`<protocol>://<name>:<password>@<ip_address_or_hostname>/<properties>`{.literal}* with the URL of the database, for example, `postgresql://verifier:UQ?nRNY9g7GZzN7@198.51.100.1/verifierdb`{.literal}.

    Ensure that the credentials you use have the permissions for Keylime to create the database structure.

4.  Add certificates and keys to the verifier. You can either let Keylime generate them, or use existing keys and certificates:

    -   With the default `tls_dir = generate`{.literal} option, Keylime generates new certificates for the verifier, registrar, and tenant in the `/var/lib/keylime/cv_ca/`{.literal} directory.

    -   To load existing keys and certificates in the configuration, define their location in the verifier configuration. The certificates must be accessible by the `keylime`{.literal} user, under which the Keylime processes are running.

        Create a new `.conf`{.literal} file in the `/etc/keylime/verifier.conf.d/`{.literal} directory, for example, `/etc/keylime/verifier.conf.d/00-keys-and-certs.conf`{.literal}, with the following content:

        ``` {.language-plaintext tabindex="-1"}
        [verifier]
        tls_dir = /var/lib/keylime/cv_ca
        server_key = </path/to/server_key>
        server_cert = </path/to/server_cert>
        trusted_client_ca = ['</path/to/ca/cert1>', '</path/to/ca/cert2>']
        client_key = </path/to/client_key>
        client_cert = </path/to/client_cert>
        trusted_server_ca = ['</path/to/ca/cert3>', '</path/to/ca/cert4>']
        ```

        Note

        Use absolute paths to define key and certificate locations. Alternatively, relative paths are resolved from the directory defined in the `tls_dir`{.literal} option.

5.  **For the push model only:** Configure the verifier for the push model attestation.

    Note

    The mode setting affects all agents on the verifier. A verifier in push mode expects agents to submit attestation data, it does not poll agents. A single verifier cannot operate in both modes simultaneously.

    You can either use a drop-in configuration file, or set the mode in the verifier's configuration file:

    -   Set the verifier's `mode`{.literal} option by creating a new `.conf`{.literal} file in the `/etc/keylime/verifier.conf.d/`{.literal} directory, for example, `/etc/keylime/verifier.conf.d/00-push-mode.conf`{.literal}, with the following content:

        ``` {.language-plaintext tabindex="-1"}
        [verifier]
        mode = push
        ```

    -   Set the verifier's `mode`{.literal} option to `push`{.literal} in the `./etc/keylime/verifier.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [verifier]
        mode = push
        ```

6.  Open the port in firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-port 8881/tcp
    # firewall-cmd --runtime-to-permanent
    ```

    If you use a different port, replace `8881`{.literal} with the port number defined in the `.conf`{.literal} file.

    For the **push model**, the port must be open to the network segments where the agents are located.

7.  Run the container:

    -   **In the push model:**

        ``` {.language-plaintext tabindex="-1"}
        $ podman run --name keylime-verifier \
          -p 8881:8881 \
          -v /etc/keylime/verifier.conf.d:/etc/keylime/verifier.conf.d:Z \
          -v /var/lib/keylime/cv_ca:/var/lib/keylime/cv_ca:Z \
          -d \
          -e KEYLIME_VERIFIER_MODE=push
          registry.redhat.io/rhel10/keylime-verifier
        ```

        -   The `-p`{.literal} option opens the default port `8881`{.literal} on the host and on the container.

        -   The `-v`{.literal} option creates a bind mount for the directory to the container.

            -   With the `Z`{.literal} option, Podman marks the content with a private unshared label. This means only the current container can use the private volume.

        -   The `-d`{.literal} option runs the container detached and in the background.

        -   You can override configuration options with environment variables by using the option `-e KEYLIME_VERIFIER_<ENVIRONMENT_VARIABLE>_=`{.literal}*`<value>`{.literal}*. To modify additional options, insert the `-e`{.literal} option separately for each environment variable. For a complete list of environment variables and their default values, see [Keylime configuration](#keylime-environment-variables "6.13. Keylime configuration").

    -   **In the pull model:**

        ``` {.language-plaintext tabindex="-1"}
        $ podman run --name keylime-verifier \
          -p 8881:8881 \
          -v /etc/keylime/verifier.conf.d:/etc/keylime/verifier.conf.d:Z \
          -v /var/lib/keylime/cv_ca:/var/lib/keylime/cv_ca:Z \
          -d \
          -e KEYLIME_VERIFIER_SERVER_KEY_PASSWORD=<passphrase1> \
          -e KEYLIME_VERIFIER_CLIENT_KEY_PASSWORD=<passphrase2> \
          registry.redhat.io/rhel10/keylime-verifier
        ```

        -   The `-p`{.literal} option opens the default port `8881`{.literal} on the host and on the container.

        -   The `-v`{.literal} option creates a bind mount for the directory to the container.

            -   With the `Z`{.literal} option, Podman marks the content with a private unshared label. This means only the current container can use the private volume.

        -   The `-d`{.literal} option runs the container detached and in the background.

        -   The option `-e KEYLIME_VERIFIER_SERVER_KEY_PASSWORD=`{.literal}*`<passphrase1>`{.literal}* defines the server key passphrase.

        -   The option `-e KEYLIME_VERIFIER_CLIENT_KEY_PASSWORD=`{.literal}*`<passphrase2>`{.literal}* defines the client key passphrase.

        -   You can override configuration options with environment variables by using the option `-e KEYLIME_VERIFIER_`{.literal}*`<ENVIRONMENT_VARIABLE>`{.literal}*`=`{.literal}*`<value>`{.literal}*. To modify additional options, insert the `-e`{.literal} option separately for each environment variable. For a complete list of environment variables and their default values, see [Keylime configuration](#keylime-environment-variables "6.13. Keylime configuration").

**Verification**

-   Check that the container is running:

    ``` {.language-plaintext tabindex="-1"}
    $ podman ps -a
    CONTAINER ID  IMAGE                                                     COMMAND           CREATED         STATUS         PORTS                   NAMES
    80b6b9dbf57c  registry.redhat.io/rhel10/keylime-verifier:latest  keylime_verifier  14 seconds ago  Up 14 seconds  0.0.0.0:8881->8881/tcp  keylime-verifier
    ```

-   **For the push model only:** Check that the verifier is configured for the push model attestation:

    ``` {.language-plaintext tabindex="-1"}
    # podman logs keylime-verifier | grep -i "push mode"
    ...
    keylime.verifier - INFO - Starting Keylime verifier in PUSH mode...
    ...
    ```

**Next steps**

-   [Deploy the Keylime registrar as a container](#deploying-keylime-registrar-as-a-container "6.5. Deploying Keylime registrar as a container")

**Additional resources**

-   [Remote system integrity monitoring](#remote-system-integrity-monitoring "6.1. Remote system integrity monitoring")
-   [Deploying Keylime verifier from a package](#deploying-keylime-verifier-from-a-package "6.2. Deploying Keylime verifier from a package")

### [6.4. Deploying Keylime registrar from a package](#deploying-keylime-registrar-from-a-package) {#deploying-keylime-registrar-from-a-package .title}

Deploy the Keylime registrar from a package to securely store and manage identity and key information about agents. Keeping the registrar secure helps maintain the chain of trust.

The registrar is the Keylime component that contains a database of all agents, and it hosts the public keys of the TPM vendors. After the registrar's HTTPS service accepts trusted platform module (TPM) public keys, it presents an interface to obtain these public keys for checking quotes.

Important

To maintain the chain of trust, keep the system that runs the registrar secure and under your control.

You can install the registrar on a separate system or on the same system as the Keylime verifier, depending on your requirements. Running the verifier and registrar on separate systems provides better performance.

Note

To keep the configuration files organized within the drop-in directories, use file names with a two-digit number prefix, for example `/etc/keylime/registrar.conf.d/00-registrar-ip.conf`{.literal}. The configuration processing reads the files inside the drop-in directory in lexicographic order and sets each option to the last value it reads.

**Prerequisites**

-   You have network access to the systems where the Keylime verifier is installed and running. For more information, see

[Section 6.2, "Deploying Keylime verifier from a package"](#deploying-keylime-verifier-from-a-package "6.2. Deploying Keylime verifier from a package").

-   You have `root`{.literal} permissions and network connection to the system or systems on which you want to install Keylime components.

-   You have access to the database where Keylime saves data from the registrar. You can use any of the following database management systems:

    -   SQLite (default)
    -   PostgreSQL
    -   MySQL
    -   MariaDB

-   You have valid keys and certificates from your certificate authority.

**Procedure**

1.  Install the Keylime registrar:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install keylime-registrar
    ```

2.  Define the IP address and port of the registrar by creating a new `.conf`{.literal} file in the `/etc/keylime/registrar.conf.d/`{.literal} directory, for example, `/etc/keylime/registrar.conf.d/00-registrar-ip.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [registrar]
    ip = <registrar_IP_address>
    ```

    -   Replace *`<registrar_IP_address>`{.literal}* with the registrar's IP address. Alternatively, use `ip = *`{.literal} or `ip = 0.0.0.0`{.literal} to bind the registrar to all available IP addresses.
    -   Optionally, change the port to which the Keylime agents connect by using the `port`{.literal} option. The default value is `8890`{.literal}.
    -   Optionally, change the TLS port to which the Keylime verifier and tenant connect by using the `tls_port`{.literal} option. The default value is `8891`{.literal}.

3.  Optional: Configure the registrar's database for the list of agents. The default configuration uses an SQLite database in the registrar's `/var/lib/keylime/reg_data.sqlite`{.literal} directory. You can create a new `.conf`{.literal} file in the `/etc/keylime/registrar.conf.d/`{.literal} directory, for example, `/etc/keylime/registrar.conf.d/00-db-url.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [registrar]
    database_url = <protocol>://<name>:<password>@<ip_address_or_hostname>/<properties>
    ```

    Replace *`<protocol>://<name>:<password>@<ip_address_or_hostname>/<properties>`{.literal}* with the URL of the database, for example, `postgresql://registrar:EKYYX-bqY2?#raXm@198.51.100.1/registrardb`{.literal}.

    Ensure that the credentials you use have the permissions for Keylime to create the database structure.

4.  Add certificates and keys to the registrar:

    -   You can use the default configuration and load the keys and certificates to the `/var/lib/keylime/reg_ca/`{.literal} directory.

    -   Alternatively, you can define the location of the keys and certificates in the configuration. Create a new `.conf`{.literal} file in the `/etc/keylime/registrar.conf.d/`{.literal} directory, for example, `/etc/keylime/registrar.conf.d/00-keys-and-certs.conf`{.literal}, with the following content:

        ``` {.language-plaintext tabindex="-1"}
        [registrar]
        tls_dir = /var/lib/keylime/reg_ca
        server_key = </path/to/server_key>
        server_key_password = <passphrase1>
        server_cert = </path/to/server_cert>
        trusted_client_ca = ['</path/to/ca/cert1>', '</path/to/ca/cert2>']
        ```

        Note

        Use absolute paths to define key and certificate locations. Alternatively, you can define a directory in the `tls_dir`{.literal} option and use paths relative to that directory.

5.  Open the ports in firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-port 8890/tcp --add-port 8891/tcp
    # firewall-cmd --runtime-to-permanent
    ```

    If you use a different port, replace `8890`{.literal} or `8891`{.literal} with the port number defined in the `.conf`{.literal} file.

6.  Start the `keylime_registrar`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now keylime_registrar
    ```

    Note

    In the default configuration, start the `keylime_verifier`{.literal} before starting the `keylime_registrar`{.literal} service because the verifier creates the CA and certificates for the other Keylime components. This order is not necessary when you use custom certificates.

**Verification**

-   Check that the `keylime_registrar`{.literal} service is active and running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status keylime_registrar
    ● keylime_registrar.service - The Keylime registrar service
         Loaded: loaded (/usr/lib/systemd/system/keylime_registrar.service; disabled; vendor preset: disabled)
         Active: active (running) since Wed 2022-11-09 10:10:17 EST; 1min 42s ago
    ...
    ```

**Next steps**

-   [Deploying Keylime tenant from a package](#deploying-keylime-tenant-from-a-package "6.8. Deploying Keylime tenant from a package")

### [6.5. Deploying Keylime registrar as a container](#deploying-keylime-registrar-as-a-container) {#deploying-keylime-registrar-as-a-container .title}

Configure the Keylime registrar as a container instead of the RPM method, without any binaries or packages on the host. The container deployment provides better isolation, modularity, and reproducibility of Keylime components.

The registrar is the Keylime component that contains a database of all agents, and it hosts the public keys of the trusted platform module (TPM) vendors. After the registrar's HTTPS service accepts TPM public keys, it presents an interface to obtain these public keys for checking quotes.

After you start the container, the Keylime registrar is deployed with default configuration files. You can customize the configuration by using one or more of following methods:

-   Mounting the host's directories that contain the configuration files to the container. This is available in all versions of RHEL 9.
-   Modifying the environment variables directly on the container. This is available in RHEL 9.3 and later versions. Modifying the environment variables overrides the values from the configuration files.

**Prerequisites**

-   The `podman`{.literal} package and its dependencies are installed on the system.

-   Optional: You have access to a database where Keylime saves data from the registrar. You can use any of the following database management systems:

    -   SQLite (default)
    -   PostgreSQL
    -   MySQL
    -   MariaDB

-   You have valid keys and certificates from your certificate authority.

**Procedure**

1.  Optional: Install the `keylime-registrar`{.literal} package to access the configuration files. You can configure the container without this package, but it might be easier to modify the configuration files provided with the package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install keylime-registrar
    ```

2.  Bind the registrar to all available IP addresses by creating a new `.conf`{.literal} file in the `/etc/keylime/registrar.conf.d/`{.literal} directory, for example, `/etc/keylime/registrar.conf.d/00-registrar-ip.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [registrar]
    ip = *
    ```

    -   Optionally, change the port to which the Keylime agents connect by using the `port`{.literal} option. The default value is `8890`{.literal}.
    -   Optionally, change the TLS port to which the Keylime tenant connects by using the `tls_port`{.literal} option. The default value is `8891`{.literal}.

3.  Optional: Configure the registrar's database for the list of agents. The default configuration uses an SQLite database in the registrar's `/var/lib/keylime/reg_data.sqlite`{.literal} directory. You can create a new `.conf`{.literal} file in the `/etc/keylime/registrar.conf.d/`{.literal} directory, for example, `/etc/keylime/registrar.conf.d/00-db-url.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [registrar]
    database_url = <protocol>://<name>:<password>@<ip_address_or_hostname>/<properties>
    ```

    Replace *`<protocol>://<name>:<password>@<ip_address_or_hostname>/<properties>`{.literal}* with the URL of the database, for example, `postgresql://registrar:EKYYX-bqY2?#raXm@198.51.100.1/registrardb`{.literal}.

    Ensure that the credentials you use have the permissions for Keylime to create the database structure.

4.  Add certificates and keys to the registrar:

    -   You can use the default configuration and load the keys and certificates to the `/var/lib/keylime/reg_ca/`{.literal} directory.

    -   Alternatively, you can define the location of the keys and certificates in the configuration. Create a new `.conf`{.literal} file in the `/etc/keylime/registrar.conf.d/`{.literal} directory, for example, `/etc/keylime/registrar.conf.d/00-keys-and-certs.conf`{.literal}, with the following content:

        ``` {.language-plaintext tabindex="-1"}
        [registrar]
        tls_dir = /var/lib/keylime/reg_ca
        server_key = </path/to/server_key>
        server_cert = </path/to/server_cert>
        trusted_client_ca = ['</path/to/ca/cert1>', '</path/to/ca/cert2>']
        ```

        Note

        Use absolute paths to define key and certificate locations. Alternatively, you can define a directory in the `tls_dir`{.literal} option and use paths relative to that directory.

5.  Open the ports in firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-port 8890/tcp --add-port 8891/tcp
    # firewall-cmd --runtime-to-permanent
    ```

    If you use a different port, replace `8890`{.literal} or `8891`{.literal} with the port number defined in the `.conf`{.literal} file.

6.  Run the container:

    ``` {.language-plaintext tabindex="-1"}
    $ podman run --name keylime-registrar \
      -p 8890:8890 \
      -p 8891:8891 \
      -v /etc/keylime/registrar.conf.d:/etc/keylime/registrar.conf.d:Z \
      -v /var/lib/keylime/reg_ca:/var/lib/keylime/reg_ca:Z \
      -d \
      -e KEYLIME_REGISTRAR_SERVER_KEY_PASSWORD=<passphrase1> \
      registry.access.redhat.com/rhel9/keylime-registrar
    ```

    -   The `-p`{.literal} option opens the default ports `8890`{.literal} and `8881`{.literal} on the host and on the container.

    -   The `-v`{.literal} option creates a bind mount for the directory to the container.

        -   With the `Z`{.literal} option, Podman marks the content with a private unshared label. This means only the current container can use the private volume.

    -   The `-d`{.literal} option runs the container detached and in the background.

    -   The option `-e KEYLIME_VERIFIER_SERVER_KEY_PASSWORD=`{.literal}*`<passphrase1>`{.literal}* defines the server key passphrase.

    -   You can override configuration options with environment variables by using the option `-e KEYLIME_REGISTRAR__`{.literal}*`<ENVIRONMENT_VARIABLE>`{.literal}*`=`{.literal}*`<value>`{.literal}*. To modify additional options, insert the `-e`{.literal} option separately for each environment variable. For a complete list of environment variables and their default values, see [Section 6.13, "Keylime configuration"](#keylime-environment-variables "6.13. Keylime configuration").

**Verification**

-   Check that the container is running:

    ``` {.language-plaintext tabindex="-1"}
    $ podman ps -a
    CONTAINER ID  IMAGE                               COMMAND            CREATED             STATUS             PORTS                                           NAMES
    07d4b4bff1b6  localhost/keylime-registrar:latest  keylime_registrar  12 seconds ago      Up 12 seconds      0.0.0.0:8881->8881/tcp, 0.0.0.0:8891->8891/tcp  keylime-registrar
    ```

**Next steps**

-   [Deploying Keylime tenant from a package](#deploying-keylime-tenant-from-a-package "6.8. Deploying Keylime tenant from a package").

**Additional resources**

-   [Remote system integrity monitoring](#remote-system-integrity-monitoring "6.1. Remote system integrity monitoring")
-   [Deploying Keylime registrar from a package](#deploying-keylime-registrar-from-a-package "6.4. Deploying Keylime registrar from a package")

### [6.6. Deploying a Keylime server by using RHEL system roles](#deploying-a-keylime-server-by-using-rhel-system-roles) {#deploying-a-keylime-server-by-using-rhel-system-roles .title}

You can configure the verifier and registrar, which are the Keylime server components, by using the `keylime_server`{.literal} RHEL system role. The `keylime_server`{.literal} role installs and configures both the verifier and registrar components together on each node.

For more information about Keylime, see [Remote system integrity monitoring](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/ensuring-system-integrity-with-keylime#remote-system-integrity-monitoring).

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook that defines the required role:

    a.  Create a new YAML file and open it in a text editor, for example:

        ``` {.language-plaintext tabindex="-1"}
        # vi keylime-playbook.yml
        ```

    b.  Insert the following content:

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Manage keylime servers
          hosts: all
          vars:
            keylime_server_verifier_ip: "{{ ansible_host }}"
            keylime_server_registrar_ip: "{{ ansible_host }}"
            keylime_server_verifier_tls_dir: <ver_tls_directory>
            keylime_server_verifier_server_cert: <ver_server_certfile>
            keylime_server_verifier_server_key: <ver_server_key>
            keylime_server_verifier_server_key_passphrase: <ver_server_key_passphrase>
            keylime_server_verifier_trusted_client_ca: <ver_trusted_client_ca_list>
            keylime_server_verifier_client_cert: <ver_client_certfile>
            keylime_server_verifier_client_key: <ver_client_key>
            keylime_server_verifier_client_key_passphrase: <ver_client_key_passphrase>
            keylime_server_verifier_trusted_server_ca: <ver_trusted_server_ca_list>
            keylime_server_registrar_tls_dir: <reg_tls_directory>
            keylime_server_registrar_server_cert: <reg_server_certfile>
            keylime_server_registrar_server_key: <reg_server_key>
            keylime_server_registrar_server_key_passphrase: <reg_server_key_passphrase>
            keylime_server_registrar_trusted_client_ca: <reg_trusted_client_ca_list>
          roles:
            - rhel-system-roles.keylime_server
        ```

        You can learn more about the variables in [Variables for the keylime_server RHEL system role](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/ensuring-system-integrity-with-keylime#variables-for-the-keylime-server-rhel-system-role).

2.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook <keylime-playbook.yml>
    ```

**Verification**

1.  Check that the `keylime_verifier`{.literal} service is active and running on the managed host:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status keylime_verifier
    ● keylime_verifier.service - The Keylime verifier
         Loaded: loaded (/usr/lib/systemd/system/keylime_verifier.service; disabled; vendor preset: disabled)
         Active: active (running) since Wed 2022-11-09 10:10:08 EST; 1min 45s ago
    ```

2.  Check that the `keylime_registrar`{.literal} service is active and running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status keylime_registrar
    ● keylime_registrar.service - The Keylime registrar service
         Loaded: loaded (/usr/lib/systemd/system/keylime_registrar.service; disabled; vendor preset: disabled)
         Active: active (running) since Wed 2022-11-09 10:10:17 EST; 1min 42s ago
    ...
    ```

**Next steps**

[Deploying Keylime tenant from a package](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/ensuring-system-integrity-with-keylime#deploying-keylime-tenant-from-a-package)

### [6.7. Variables for the keylime_server RHEL system role](#variables-for-the-keylime-server-rhel-system-role) {#variables-for-the-keylime_server-rhel-system-role .title}

When setting up a Keylime server by using the `keylime_server`{.literal} RHEL system role, you can customize the following variables for registrar and verifier.

List of `keylime_server`{.literal} RHEL system role variables for configuring the Keylime verifier:

`keylime_server_verifier_ip`{.literal}
:   Defines the IP address of the verifier.

`keylime_server_verifier_tls_dir`{.literal}
:   Specifies the directory where the keys and certificates are stored. If set to default, the verifier uses the `/var/lib/keylime/cv_ca`{.literal} directory.

`keylime_server_verifier_server_key_passphrase`{.literal}
:   Specifies a passphrase to decrypt the server private key. If the value is empty, the private key is not encrypted.

`keylime_server_verifier_server_cert`{.literal}: Specifies the Keylime verifier server certificate file.

`keylime_server_verifier_trusted_client_ca`{.literal}
:   Defines the list of trusted client CA certificates. You must store the files in the directory set in the `keylime_server_verifier_tls_dir`{.literal} option.

`keylime_server_verifier_client_key`{.literal}
:   Defines the file containing the Keylime verifier private client key.

`keylime_server_verifier_client_key_passphrase`{.literal}
:   Defines the passphrase to decrypt the client private key file. If the value is empty, the private key is not encrypted.

`keylime_server_verifier_client_cert`{.literal}
:   Defines the Keylime verifier client certificate file.

`keylime_server_verifier_trusted_server_ca`{.literal}
:   Defines the list of trusted server CA certificates. You must store the files in the directory set in the `keylime_server_verifier_tls_dir`{.literal} option.

List of registrar variables for setting up keylime_server RHEL system role:

`keylime_server_registrar_ip`{.literal}
:   Defines the IP address of the registrar.

`keylime_server_registrar_tls_dir`{.literal}
:   Specifies the directory where you store the keys and certificates for the registrar. If you set it to default, the registrar uses the `/var/lib/keylime/reg_ca`{.literal} directory.

`keylime_server_registrar_server_key`{.literal}
:   Defines the Keylime registrar private server key file.

`keylime_server_registrar_server_key_passphrase`{.literal}
:   Specifies the passphrase to decrypt the server private key of the registrar. If the value is empty, the private key is not encrypted.

`keylime_server_registrar_server_cert`{.literal}
:   Specifies the Keylime registrar server certificate file.

`keylime_server_registrar_trusted_client_ca`{.literal}
:   Defines the list of trusted client CA certificates. You must store the files in the directory set in the `keylime_server_registrar_tls_dir`{.literal} option.

### [6.8. Deploying Keylime tenant from a package](#deploying-keylime-tenant-from-a-package) {#deploying-keylime-tenant-from-a-package .title}

Keylime uses the `keylime_tenant`{.literal} utility for many functions, including provisioning the agents on the target systems. You can install `keylime_tenant`{.literal} on any system, including the systems that run other Keylime components, or on a separate system, depending on your requirements.

For additional advanced options for the `keylime_tenant`{.literal} utility, enter the `keylime_tenant -h`{.literal} command.

**Prerequisites**

-   You have `root`{.literal} permissions and network connection to the system or systems on which you want to install Keylime components.

-   You have network access to the systems where the other Keylime components are configured:

    Verifier
    :   For more information, see [Section 6.2, "Deploying Keylime verifier from a package"](#deploying-keylime-verifier-from-a-package "6.2. Deploying Keylime verifier from a package").

    Registrar
    :   For more information, see [Section 6.4, "Deploying Keylime registrar from a package"](#deploying-keylime-registrar-from-a-package "6.4. Deploying Keylime registrar from a package").

**Procedure**

1.  Install the Keylime tenant:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install keylime-tenant
    ```

2.  Define the tenant's connection to the Keylime verifier by editing the `/etc/keylime/tenant.conf.d/00-verifier-ip.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [tenant]
    verifier_ip = <verifier_ip>
    ```

    -   Replace *`<verifier_ip>`{.literal}* with the IP address to the verifier's system.
    -   If the verifier uses a different port than the default value `8881`{.literal}, add the `verifier_port = `{.literal}*`<verifier_port>`{.literal}* setting.

3.  Define the tenant's connection to the Keylime registrar by editing the `/etc/keylime/tenant.conf.d/00-registrar-ip.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [tenant]
    registrar_ip = <registrar_ip>
    ```

    -   Replace *`<registrar_ip>`{.literal}* with the IP address to the registrar's system.
    -   If the registrar uses a different port than the default value `8891`{.literal}, add the `registrar_port = `{.literal}*`<registrar_port>`{.literal}* setting.

4.  Add certificates and keys to the tenant:

    a.  You can use the default configuration and load the keys and certificates to the `/var/lib/keylime/cv_ca`{.literal} directory.

    b.  Alternatively, you can define the location of the keys and certificates in the configuration. Create a new `.conf`{.literal} file in the `/etc/keylime/tenant.conf.d/`{.literal} directory, for example, `/etc/keylime/tenant.conf.d/00-keys-and-certs.conf`{.literal}, with the following content:

        ``` {.language-plaintext tabindex="-1"}
        [tenant]
        tls_dir = /var/lib/keylime/cv_ca
        client_key = tenant-key.pem
        client_key_password = <passphrase1>
        client_cert = tenant-cert.pem
        trusted_server_ca = ['</path/to/ca/cert>']
        ```

        The `trusted_server_ca`{.literal} parameter accepts paths to the verifier and registrar server CA certificate. You can provide multiple comma-separated paths, for example if the verifier and registrar use different CAs.

        Note

        Use absolute paths to define key and certificate locations. Alternatively, you can define a directory in the `tls_dir`{.literal} option and use paths relative to that directory.

5.  Optional: If the trusted platform module (TPM) endorsement key (EK) cannot be verified by using certificates in the `/var/lib/keylime/tpm_cert_store`{.literal} directory, add the certificate to that directory. This can occur particularly when using virtual machines with emulated TPMs.

**Verification**

1.  Check the status of the verifier:

    ``` {.language-plaintext tabindex="-1"}
    # keylime_tenant -c cvstatus
    Reading configuration from ['/etc/keylime/logging.conf']
    2022-10-14 12:56:08.155 - keylime.tpm - INFO - TPM2-TOOLS Version: 5.2
    Reading configuration from ['/etc/keylime/tenant.conf']
    2022-10-14 12:56:08.157 - keylime.tenant - INFO - Setting up client TLS...
    2022-10-14 12:56:08.158 - keylime.tenant - INFO - Using default client_cert option for tenant
    2022-10-14 12:56:08.158 - keylime.tenant - INFO - Using default client_key option for tenant
    2022-10-14 12:56:08.178 - keylime.tenant - INFO - TLS is enabled.
    2022-10-14 12:56:08.178 - keylime.tenant - WARNING - Using default UUID d432fbb3-d2f1-4a97-9ef7-75bd81c00000
    2022-10-14 12:56:08.221 - keylime.tenant - INFO - Verifier at 127.0.0.1 with Port 8881 does not have agent d432fbb3-d2f1-4a97-9ef7-75bd81c00000.
    ```

    If correctly configured, and if no agent is configured, the verifier responds that it does not recognize the default agent UUID.

2.  Check the status of the registrar:

    ``` {.language-plaintext tabindex="-1"}
    # keylime_tenant -c regstatus
    Reading configuration from ['/etc/keylime/logging.conf']
    2022-10-14 12:56:02.114 - keylime.tpm - INFO - TPM2-TOOLS Version: 5.2
    Reading configuration from ['/etc/keylime/tenant.conf']
    2022-10-14 12:56:02.116 - keylime.tenant - INFO - Setting up client TLS...
    2022-10-14 12:56:02.116 - keylime.tenant - INFO - Using default client_cert option for tenant
    2022-10-14 12:56:02.116 - keylime.tenant - INFO - Using default client_key option for tenant
    2022-10-14 12:56:02.137 - keylime.tenant - INFO - TLS is enabled.
    2022-10-14 12:56:02.137 - keylime.tenant - WARNING - Using default UUID d432fbb3-d2f1-4a97-9ef7-75bd81c00000
    2022-10-14 12:56:02.171 - keylime.registrar_client - CRITICAL - Error: could not get agent d432fbb3-d2f1-4a97-9ef7-75bd81c00000 data from Registrar Server: 404
    2022-10-14 12:56:02.172 - keylime.registrar_client - CRITICAL - Response code 404: agent d432fbb3-d2f1-4a97-9ef7-75bd81c00000 not found
    2022-10-14 12:56:02.172 - keylime.tenant - INFO - Agent d432fbb3-d2f1-4a97-9ef7-75bd81c00000 does not exist on the registrar. Please register the agent with the registrar.
    2022-10-14 12:56:02.172 - keylime.tenant - INFO - {"code": 404, "status": "Agent d432fbb3-d2f1-4a97-9ef7-75bd81c00000 does not exist on registrar 127.0.0.1 port 8891.", "results": {}}
    ```

    If correctly configured, and if no agent is configured, the registrar responds that it does not recognize the default agent UUID.

**Next steps**

Depending on the attestation model you choose, configure the corresponding agent on systems you want to monitor:

-   [Deploying Keylime pull-model agent from a package](#deploying-keylime-agent-from-a-package "6.9. Deploying Keylime pull-model agent from a package")
-   [Deploying Keylime push-model agent from a package](#deploying-keylime-push-model-agent-from-a-package "6.10. Deploying Keylime push-model agent from a package")

### [6.9. Deploying Keylime pull-model agent from a package](#deploying-keylime-agent-from-a-package) {#deploying-keylime-pull-model-agent-from-a-package .title}

To continuously monitor system integrity, deploy the Keylime pull-model agent. With this configuration, the target system reports its security state when polled by the verifier.

By default, the Keylime pull-model agent stores all its data in the `/var/lib/keylime/`{.literal} directory of the monitored system.

Note

To keep the configuration files organized within the drop-in directories, use file names with a two-digit number prefix, for example `/etc/keylime/agent.conf.d/00-registrar-ip.conf`{.literal}. The configuration processing reads the files inside the drop-in directory in lexicographic order and sets each option to the last value it reads.

**Prerequisites**

-   You have `root`{.literal} permissions to the monitored system.

-   The monitored system has a Trusted Platform Module (TPM). To verify, enter the `tpm2_pcrread`{.literal} command. If the output returns several hashes, a TPM is available.

-   You have network access to the systems where the other Keylime components are configured:

    Verifier
    :   For more information, see [Deploying Keylime verifier from a package](#deploying-keylime-verifier-from-a-package "6.2. Deploying Keylime verifier from a package").

    Registrar
    :   For more information, see [Deploying Keylime registrar from a package](#deploying-keylime-registrar-from-a-package "6.4. Deploying Keylime registrar from a package").

    Tenant
    :   For more information, see [Deploying Keylime tenant from a package](#deploying-keylime-tenant-from-a-package "6.8. Deploying Keylime tenant from a package").

-   Integrity measurement architecture (IMA) is enabled on the monitored system. For more information, see [Enhancing security with the kernel integrity subsystem](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/enhancing-security-with-the-kernel-integrity-subsystem).

**Procedure**

1.  Install the Keylime pull-model agent:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install keylime-agent-rust
    ```

    This command installs the `keylime-agent-rust`{.literal} package.

2.  Define the agent's IP address and port in the configuration files. Create a new `.conf`{.literal} file in the `/etc/keylime/agent.conf.d/`{.literal} directory, for example, `/etc/keylime/agent.conf.d/00-agent-ip.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [agent]
    ip = '<agent_IP_address>'
    ```

    Note

    The Keylime agent configuration uses the TOML format, which is different from the INI format used for configuration of the other components. Therefore, enter values in valid TOML syntax, for example, paths in single quotation marks and arrays of multiple paths in square brackets.

    -   Replace *`<agent_IP_address>`{.literal}* with the agent's IP address. Alternatively, use `ip = '*'`{.literal} or `ip = '0.0.0.0'`{.literal} to bind the agent to all available IP addresses.
    -   Optionally, you can also change the agent's port from the default value `9002`{.literal} by using the `port = '`{.literal}*`<agent_port>`{.literal}*`'`{.literal} option.

3.  Define the registrar's IP address and port in the configuration files. Create a new `.conf`{.literal} file in the `/etc/keylime/agent.conf.d/`{.literal} directory, for example, `/etc/keylime/agent.conf.d/00-registrar-ip.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [agent]
    registrar_ip = '<registrar_IP_address>'
    ```

    -   Replace *`<registrar_IP_address>`{.literal}* with the registrar's IP address.
    -   Optionally, you can also change the registrar's port from the default value `8890`{.literal} by using the `registrar_port = '`{.literal}*`<registrar_port>`{.literal}*`'`{.literal} option.

4.  Define the agent's universally unique identifier (UUID). The default UUID in the configuration file is a hard-coded placeholder value shared by all installations. You must override it before deploying the agent to avoid registration conflicts between agents.

    Create a new `.conf`{.literal} file in the `/etc/keylime/agent.conf.d/`{.literal} directory, for example, `/etc/keylime/agent.conf.d/00-agent-uuid.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [agent]
    uuid = '<agent_UUID>'
    ```

    -   Replace *`<agent_UUID>`{.literal}* with one of the following strings:

        -   `hash_ek`{.literal} - Keylime derives the UUID from a SHA-256 hash of the public Endorsement Key (EK) in PEM format. Use this option for most deployments.
        -   `generate`{.literal} - Keylime generates a random UUID at first startup.
        -   A specific UUID string, for example `d432fbb3-d2f1-4a97-9ef7-abcdef012345`{.literal}. You can use the `uuidgen`{.literal} utility to generate one.

5.  Optional: Load existing keys and certificates for the agent. If the agent receives no `server_key`{.literal} and `server_cert`{.literal}, it generates its own key and a self-signed certificate.

    Define the location of the keys and certificates in the configuration. Create a new `.conf`{.literal} file in the `/etc/keylime/agent.conf.d/`{.literal} directory, for example, `/etc/keylime/agent.conf.d/00-keys-and-certs.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [agent]
    server_key = '</path/to/server_key>'
    server_key_password = '<passphrase1>'
    server_cert = '</path/to/server_cert>'
    trusted_client_ca = '[</path/to/ca/cert3>, </path/to/ca/cert4>]'
    ```

    Note

    Use absolute paths to define key and certificate locations. The Keylime agent does not accept relative paths.

6.  Open the port in firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-port 9002/tcp
    # firewall-cmd --runtime-to-permanent
    ```

    If you use a different port, replace `9002`{.literal} with the port number defined in the `.conf`{.literal} file.

7.  Enable and start the `keylime_agent`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now keylime_agent
    ```

8.  Optional: On the Keylime tenant system, verify the agent configuration and its connection to the registrar.

    ``` {.language-plaintext tabindex="-1"}
    # keylime_tenant -c regstatus --uuid <agent_uuid>
    ```

    Replace *`<agent_uuid>`{.literal}* with the agent's UUID. If you configured the agent to dynamically generate its UUID by using `hash_ek`{.literal} or `generate`{.literal}, retrieve the generated UUID from the local agent's log output by using `journalctl -u keylime_agent`{.literal}.

    If the registration is successful, the output displays the agent's IP address and port, followed by `"operational_state": "Registered"`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    Reading configuration from ['/etc/keylime/logging.conf']
    ...
    ==\n-----END CERTIFICATE-----\n", "ip": "127.0.0.1", "port": 9002, "regcount": 1, "operational_state": "Registered"}}}
    ```

9.  Create a new IMA policy by entering the following content into the `/etc/ima/ima-policy`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # PROC_SUPER_MAGIC = 0x9fa0
    dont_measure fsmagic=0x9fa0
    # SYSFS_MAGIC = 0x62656572
    dont_measure fsmagic=0x62656572
    # DEBUGFS_MAGIC = 0x64626720
    dont_measure fsmagic=0x64626720
    # TMPFS_MAGIC = 0x01021994
    dont_measure fsmagic=0x1021994
    # RAMFS_MAGIC
    dont_measure fsmagic=0x858458f6
    # DEVPTS_SUPER_MAGIC=0x1cd1
    dont_measure fsmagic=0x1cd1
    # BINFMTFS_MAGIC=0x42494e4d
    dont_measure fsmagic=0x42494e4d
    # SECURITYFS_MAGIC=0x73636673
    dont_measure fsmagic=0x73636673
    # SELINUX_MAGIC=0xf97cff8c
    dont_measure fsmagic=0xf97cff8c
    # SMACK_MAGIC=0x43415d53
    dont_measure fsmagic=0x43415d53
    # NSFS_MAGIC=0x6e736673
    dont_measure fsmagic=0x6e736673
    # EFIVARFS_MAGIC
    dont_measure fsmagic=0xde5e81e4
    # CGROUP_SUPER_MAGIC=0x27e0eb
    dont_measure fsmagic=0x27e0eb
    # CGROUP2_SUPER_MAGIC=0x63677270
    dont_measure fsmagic=0x63677270
    # OVERLAYFS_MAGIC
    # when containers are used we almost always want to ignore them
    dont_measure fsmagic=0x794c7630
    # MEASUREMENTS
    measure func=BPRM_CHECK
    measure func=FILE_MMAP mask=MAY_EXEC
    measure func=MODULE_CHECK uid=0
    ```

    This policy targets runtime monitoring of executed applications. You can adjust this policy according to your scenario. You can find the MAGIC constants in the `statfs(2)`{.literal} man page.

10. Update kernel parameters:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel DEFAULT --args 'ima_appraise=log ima_canonical_fmt ima_policy=tcb ima_template=ima-ng'
    ```

11. Reboot the system to apply the new IMA policy.

**Verification**

-   Verify that the agent is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status keylime_agent
    ● keylime_agent.service - The Keylime compute agent
         Loaded: loaded (/usr/lib/systemd/system/keylime_agent.service; enabled; preset: disabled)
         Active: active (running) since ...
    ```

**Next steps**

After the agent is configured on all systems you want to monitor, you can deploy Keylime to perform one or both of the following functions:

-   [Configuring Keylime for runtime monitoring](#configuring-keylime-for-runtime-monitoring "6.11. Configuring Keylime for runtime monitoring")
-   [Configuring Keylime for measured boot attestation](#configuring-keylime-for-measured-boot-attestation "6.12. Configuring Keylime for measured boot attestation")

**Additional resources**

-   [Remote system integrity monitoring](#remote-system-integrity-monitoring "6.1. Remote system integrity monitoring")
-   [Deploying Keylime push-model agent from a package](#deploying-keylime-push-model-agent-from-a-package "6.10. Deploying Keylime push-model agent from a package")
-   [Integrity Measurement Architecture (IMA) Wiki](https://sourceforge.net/p/linux-ima/wiki/Home/)

### [6.10. Deploying Keylime push-model agent from a package](#deploying-keylime-push-model-agent-from-a-package) {#deploying-keylime-push-model-agent-from-a-package .title}

To continuously monitor system integrity in environments where the verifier lacks direct network access to agents, deploy the Keylime push-model agent. With this configuration, the agent proactively submits attestation data to the verifier.

The push-model agent is a separate package from the standard Keylime pull-model agent. Only one agent type can run on a system at a time.

By default, the Keylime push-model agent stores all its data in the `/var/lib/keylime/`{.literal} directory of the monitored system.

Note

To keep the configuration files organized within the drop-in directories, use file names with a two-digit number prefix, for example `/etc/keylime/agent.conf.d/00-verifier-url.conf`{.literal}. The configuration processing reads the files inside the drop-in directory in lexicographic order and sets each option to the last value it reads.

**Prerequisites**

-   You have `root`{.literal} permissions to the monitored system.

-   The monitored system has a Trusted Platform Module (TPM). To verify, enter the `tpm2_pcrread`{.literal} command. If the output returns several hashes, a TPM is available.

-   You have network access from the agent to the systems where the other Keylime components are configured:

    Verifier
    :   The verifier must be configured in push mode so that it accepts inbound attestation connections from agents. For more information, see [Deploying Keylime verifier from a package](#deploying-keylime-verifier-from-a-package "6.2. Deploying Keylime verifier from a package").

    Registrar
    :   For more information, see [Deploying Keylime registrar from a package](#deploying-keylime-registrar-from-a-package "6.4. Deploying Keylime registrar from a package").

    Tenant
    :   For more information, see [Deploying Keylime tenant from a package](#deploying-keylime-tenant-from-a-package "6.8. Deploying Keylime tenant from a package").

-   The verifier's CA certificate is available on the monitored system. You can copy it from the verifier, where it is typically located at `/var/lib/keylime/cv_ca/cacert.crt`{.literal}.

-   Integrity measurement architecture (IMA) is enabled on the monitored system. For more information, see [Enhancing security with the kernel integrity subsystem](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/enhancing-security-with-the-kernel-integrity-subsystem).

**Procedure**

1.  Install the Keylime push-model agent:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install keylime-agent-rust-push
    ```

    This command installs the `keylime-agent-rust-push`{.literal} package and its dependencies, including `keylime-agent-rust-common`{.literal} and `keylime-base`{.literal}.

2.  Define the verifier's URL in the configuration files. Create a new `.conf`{.literal} file in the `/etc/keylime/agent.conf.d/`{.literal} directory, for example, `/etc/keylime/agent.conf.d/00-verifier-url.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [agent]
    verifier_url = 'https://<verifier_IP_address>:8881'
    ```

    Note

    The Keylime agent configuration uses the TOML format, which is different from the INI format used for configuration of the other components. Therefore, enter values in valid TOML syntax, for example, paths in single quotation marks and arrays of multiple paths in square brackets.

    -   Replace *`<verifier_IP_address>`{.literal}* with the verifier's IP address or hostname.
    -   Optionally, you can also change the verifier's port from the default value `8881`{.literal}.

3.  Define the path to the verifier's CA certificate. If the verifier's CA certificate is already at the default location (`/var/lib/keylime/cv_ca/cacert.crt`{.literal}), this step can be skipped. Otherwise, create a new `.conf`{.literal} file in the `/etc/keylime/agent.conf.d/`{.literal} directory, for example, `/etc/keylime/agent.conf.d/00-verifier-tls.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [agent]
    verifier_tls_ca_cert = '/var/lib/keylime/cv_ca/cacert.crt'
    ```

    -   Replace the path with the actual location of the verifier's CA certificate on the monitored system.

4.  Define the registrar's IP address and port in the configuration files. Create a new `.conf`{.literal} file in the `/etc/keylime/agent.conf.d/`{.literal} directory, for example, `/etc/keylime/agent.conf.d/00-registrar-ip.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [agent]
    registrar_ip = '<registrar_IP_address>'
    ```

    -   Replace *`<registrar_IP_address>`{.literal}* with the registrar's IP address.
    -   Optionally, you can also change the registrar's port from the default value `8890`{.literal} by using the `registrar_port = `{.literal}*`<registrar_port>`{.literal}* option. Note that port values are integers and must not be quoted.

5.  Optional: If TLS is enabled on the registrar, configure TLS for the registrar connection. Create a new `.conf`{.literal} file in the `/etc/keylime/agent.conf.d/`{.literal} directory, for example, `/etc/keylime/agent.conf.d/00-registrar-tls.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [agent]
    registrar_tls_enabled = true
    registrar_tls_port = 8891
    registrar_tls_ca_cert = '/var/lib/keylime/cv_ca/cacert.crt'
    ```

    -   Replace `8891`{.literal} with the registrar's TLS port if it differs from the default.
    -   Replace the certificate path with the actual location of the CA certificate used to verify the registrar's server certificate.

6.  Define the agent's universally unique identifier (UUID). The default UUID in the configuration file is a hard-coded placeholder value shared by all installations. You must override it before deploying the agent to avoid registration conflicts between agents.

    Create a new `.conf`{.literal} file in the `/etc/keylime/agent.conf.d/`{.literal} directory, for example, `/etc/keylime/agent.conf.d/00-agent-uuid.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [agent]
    uuid = '<agent_UUID>'
    ```

    -   Replace *`<agent_UUID>`{.literal}* with one of the following strings:

        -   `hash_ek`{.literal} - Keylime derives the UUID from a SHA-256 hash of the public Endorsement Key (EK) in PEM format. Use this option for most deployments.
        -   `generate`{.literal} - Keylime generates a random UUID at first startup.
        -   A specific UUID string, for example `d432fbb3-d2f1-4a97-9ef7-abcdef012345`{.literal}. You can use the `uuidgen`{.literal} utility to generate one.

7.  Optional: Define the attestation interval. Create a new `.conf`{.literal} file in the `/etc/keylime/agent.conf.d/`{.literal} directory, for example, `/etc/keylime/agent.conf.d/00-attestation-interval.conf`{.literal}, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [agent]
    attestation_interval_seconds = 5
    ```

    The `attestation_interval_seconds`{.literal} parameter sets a fallback interval, which defaults to `60`{.literal} seconds. The verifier automatically overrides this parameter during normal operations by sending the `seconds_to_next_attestation`{.literal} value in its response. If a response does not contain this value, or during initial agent startup, the agent uses `attestation_interval_seconds`{.literal} to schedule its next push.

    Set `attestation_interval_seconds`{.literal} below the verifier's timeout limit. By default, this limit is `10`{.literal} seconds, calculated as `quote_interval * 5`{.literal}. If the fallback value exceeds this limit, the verifier marks the agent as timed out.

8.  If the standard pull-model agent was previously installed, disable it to prevent it from starting on boot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl disable keylime_agent
    ```

    Important

    Starting the push-model agent automatically stops the pull-model agent if it is running. However, you must disable the pull-model agent to ensure it does not start on reboot.

9.  Enable and start the `keylime_push_model_agent`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now keylime_push_model_agent
    ```

10. Optional: On the Keylime tenant system, verify the agent configuration and its connection to the registrar.

    ``` {.language-plaintext tabindex="-1"}
    # keylime_tenant -c regstatus --uuid <agent_uuid>
    ```

    Replace *`<agent_uuid>`{.literal}* with the agent's UUID. If you configured the agent to dynamically generate its UUID by using `hash_ek`{.literal} or `generate`{.literal}, retrieve the generated UUID from the local agent's log output by using `journalctl -u keylime_push_model_agent`{.literal}.

    If the registration is successful, the output displays the agent's IP address and port, followed by `"operational_state": "Registered"`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    Reading configuration from ['/etc/keylime/logging.conf']
    ...
    ==\n-----END CERTIFICATE-----\n", "ip": "127.0.0.1", "port": 9002, "regcount": 1, "operational_state": "Registered"}}
    ```

    Note

    For push-model agents, the output omits the `operational_state`{.literal} field. Additionally, the `ip`{.literal} and `port`{.literal} fields return `null`{.literal} because the registrar does not need to track inbound connection details for push-model agents.

**Verification**

-   Verify that the push-model agent is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status keylime_push_model_agent
    ● keylime_push_model_agent.service - The Keylime push model agent
       Loaded: loaded (/usr/lib/systemd/system/keylime_push_model_agent.service; enabled; preset: disabled)
       Active: active (running) since ...
    ```

**Next steps**

After the agent is configured on all systems you want to monitor, you can deploy Keylime to perform one or both of the following functions:

-   [Configuring Keylime for runtime monitoring](#configuring-keylime-for-runtime-monitoring "6.11. Configuring Keylime for runtime monitoring")
-   [Configuring Keylime for measured boot attestation](#configuring-keylime-for-measured-boot-attestation "6.12. Configuring Keylime for measured boot attestation")

**Additional resources**

-   [Remote system integrity monitoring](#remote-system-integrity-monitoring "6.1. Remote system integrity monitoring")
-   [Deploying Keylime pull-model agent from a package](#deploying-keylime-agent-from-a-package "6.9. Deploying Keylime pull-model agent from a package")
-   [Integrity Measurement Architecture (IMA) Wiki](https://sourceforge.net/p/linux-ima/wiki/Home/)

### [6.11. Configuring Keylime for runtime monitoring](#configuring-keylime-for-runtime-monitoring) {#configuring-keylime-for-runtime-monitoring .title}

To verify that the state of monitored systems is correct, set up the Keylime agent on the monitored systems.

Important

Runtime monitoring relies on the Linux kernel Integrity Measurement Architecture (IMA) to measure files upon access. An overly broad IMA policy might increase I/O operations and CPU usage. To minimize the performance impact on your system, configure the IMA policy to measure only critical files.

When provisioning the agent, you can also define a file that Keylime sends to the monitored system. Keylime encrypts the file sent to the agent, and decrypts it only if the agent's system complies with the TPM policy and with the IMA allowlist.

Important

Secure payload delivery is only available with pull-model attestation. The push model does not support delivering encrypted files to the agent. Do not use the `--cert`{.literal} option with push-model agents. If you specify this option, the system generates certificates but never delivers them to the agent.

You can make Keylime ignore changes of specific files or within specific directories by configuring a Keylime excludelist. The excluded files are still measured by IMA.

The allowlist and excludelist are combined into the Keylime runtime policy.

**Prerequisites**

-   You have network access to the systems where the Keylime components are configured:

    Verifier
    :   For more information, see [Deploying Keylime verifier from a package](#deploying-keylime-verifier-from-a-package "6.2. Deploying Keylime verifier from a package").

    Registrar
    :   For more information, see [Deploying Keylime registrar from a package](#deploying-keylime-registrar-from-a-package "6.4. Deploying Keylime registrar from a package").

    Tenant
    :   For more information, see [Deploying Keylime tenant from a package](#deploying-keylime-tenant-from-a-package "6.8. Deploying Keylime tenant from a package").

    Agent

    :   -   If you use pull model attestation: For more information, see [Deploying Keylime pull-model agent from a package](#deploying-keylime-agent-from-a-package "6.9. Deploying Keylime pull-model agent from a package").
        -   If you use push model attestation: For more information, see [Deploying Keylime push-model agent from a package](#deploying-keylime-push-model-agent-from-a-package "6.10. Deploying Keylime push-model agent from a package").

**Procedure**

1.  On the monitored system where the Keylime agent is configured and running, install the `python3-keylime`{.literal} package, which contains the `keylime-policy`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y install python3-keylime
    ```

2.  Create a runtime policy from the current state of the agent system:

    ``` {.language-plaintext tabindex="-1"}
    # keylime-policy create runtime --ima-measurement --rootfs '/' --ramdisk-dir '/boot/' --output <policy.json>
    ```

    In this command,

    -   Replace *`<policy.json>`{.literal}* with the file name of the runtime policy.

    -   The following directories are automatically excluded from measurement:

        -   `/sys`{.literal}
        -   `/run`{.literal}
        -   `/proc`{.literal}
        -   `/lost+found`{.literal}
        -   `/dev`{.literal}
        -   `/media`{.literal}
        -   `/snap`{.literal}
        -   `/mnt`{.literal}
        -   `/var`{.literal}
        -   `/tmp`{.literal}

    -   Optionally, you can exclude additional specific paths from measurement by adding a `--excludelist `{.literal}*`<excludelist.txt>`{.literal}* option. The excludelist accepts Python regular expressions with one regular expression per line. See [Regular expression operations at docs.python.org](https://docs.python.org/3/library/re.html#regular-expression-syntax) for the complete list of special characters.

3.  Copy the generated runtime policy to the system where the `keylime_tenant`{.literal} utility is configured, for example:

    ``` {.language-plaintext tabindex="-1"}
    # scp <policy.json> root@<tenant.ip>:/root/<policy.json>
    ```

4.  On the system where the Keylime tenant is configured, provision the agent by using the `keylime_tenant`{.literal} utility:

    -   **If you use pull model attestation:**

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command add --targethost <agent_ip> --uuid <agent_uuid> --runtime-policy <policy.json> --cert default
        ```

        -   Replace *`<agent_ip>`{.literal}* with the agent's IP address.

        -   Replace *`<agent_uuid>`{.literal}* with the agent's UUID.

        -   Replace *`<policy.json>`{.literal}* with the path to the Keylime runtime policy file.

        -   With the `--cert`{.literal} option, the tenant generates and signs a certificate for the agent by using the CA certificates and keys located in the specified directory, or the default `/var/lib/keylime/ca/`{.literal} directory. If the directory contains no CA certificates and keys, the tenant will generate them automatically according to the configuration in the `/etc/keylime/ca.conf`{.literal} file and save them to the specified directory. The tenant then sends these keys and certificates to the agent.

            When generating CA certificates or signing agent certificates, you might be prompted for the password to access the CA private key: `Please enter the password to decrypt your keystore:`{.literal}.

            Note

            Keylime encrypts the file sent to the agent, and decrypts it only if the agent's system complies with the TPM policy and the IMA allowlist. By default, Keylime decompresses sent `.zip`{.literal} files.

        As an example, with the following command, `keylime_tenant`{.literal} provisions a new Keylime agent at `127.0.0.1`{.literal} with UUID `d432fbb3-d2f1-4a97-9ef7-75bd81c00000`{.literal} and loads a runtime policy `policy.json`{.literal}. It also generates a certificate in the default directory and sends the certificate file to the agent. Keylime decrypts the file only if the TPM policy configured in `/etc/keylime/verifier.conf`{.literal} is satisfied:

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command add --targethost 127.0.0.1 --uuid d432fbb3-d2f1-4a97-9ef7-75bd81c00000 --runtime-policy policy.json --cert default
        ```

    -   **If you use push model attestation:**

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command add --push-model --uuid <agent_uuid> --runtime-policy <policy.json>
        ```

        -   Replace *`<agent_uuid>`{.literal}* with the agent's UUID.
        -   Replace *`<policy.json>`{.literal}* with the path to the Keylime runtime policy file.
        -   The `--push-model`{.literal} option indicates the agent uses push model attestation. Because the verifier does not connect to the agent in the push model, you do not need to specify the agent's IP address with the `--targethost`{.literal} option.
        -   Push-model agents authenticate by using TPM-based Proof of Possession (PoP), not mTLS client certificates.

        As an example, with the following command, `keylime_tenant`{.literal} provisions a new push-model Keylime agent with UUID `d432fbb3-d2f1-4a97-9ef7-75bd81c00000`{.literal} and loads a runtime policy `policy.json`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command add --push-model --uuid d432fbb3-d2f1-4a97-9ef7-75bd81c00000 --runtime-policy policy.json
        ```

**Verification**

1.  Optional: Reboot the monitored system to verify that the settings are persistent.

2.  Verify a successful attestation of the agent:

    -   **If you use pull model attestation:**

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command cvstatus --uuid <agent_uuid>
        ```

        Replace *`<agent_uuid>`{.literal}* with the agent's UUID.

        If the value of `operational_state`{.literal} is `Get Quote`{.literal} and `attestation_count`{.literal} is nonzero, the attestation of this agent is successful:

        ``` {.language-plaintext tabindex="-1"}
        ...
        {"<agent_uuid>": {"operational_state": "Get Quote"..."attestation_count": 5
        ...
        ```

        If the value of `operational_state`{.literal} is `Invalid Quote`{.literal} or `Failed`{.literal} attestation fails, the command displays output similar to the following:

        ``` {.language-plaintext tabindex="-1"}
        {"<agent_uuid>": {"operational_state": "Invalid Quote", ... "ima.validation.ima-ng.not_in_allowlist", "attestation_count": 5, "last_received_quote": 1684150329, "last_successful_attestation": 1684150327}}
        ```

    -   **If you use push model attestation**:

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command cvstatus --push-model --uuid <agent_uuid>
        ```

        Replace *`<agent_uuid>`{.literal}* with the agent's UUID.

        Push-model agents do not use the `operational_state`{.literal} field. Instead, check the `attestation_status`{.literal} field, which returns `PENDING`{.literal}, `PASS`{.literal}, `FAIL`{.literal}, or `TIMEOUT`{.literal}. If the value of `attestation_status`{.literal} is `PASS`{.literal} and `attestation_count`{.literal} is nonzero, the attestation of this agent is successful:

        ``` {.language-plaintext tabindex="-1"}
        {"<agent_uuid>": {"attestation_status": "PASS", "attestation_count": 5, ...}}
        ```

3.  If the attestation fails, display more details in the verifier log:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl --unit keylime_verifier
    keylime.tpm - INFO - Checking IMA measurement list...
    keylime.ima - WARNING - File not found in allowlist: /root/bad-script.sh
    keylime.ima - ERROR - IMA ERRORS: template-hash 0 fnf 1 hash 0 good 781
    keylime.cloudverifier - WARNING - agent D432FBB3-D2F1-4A97-9EF7-75BD81C00000 failed, stopping polling
    ```

**Next steps**

-   To modify the configuration of an already registered agent, use the `keylime_tenant --command update`{.literal} command. For push-model agents, include the `--push-model`{.literal} option with the `update`{.literal} command.
-   To stop Keylime from monitoring a node, use the `keylime_tenant --command delete --uuid `{.literal}*`<agent_uuid>`{.literal}* command. The `delete`{.literal} command works identically for both pull-model and push-model agents and does not require the `--push-model`{.literal} option.

**Additional resources**

-   [Enhancing security with the kernel integrity subsystem](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/enhancing-security-with-the-kernel-integrity-subsystem)

### [6.12. Configuring Keylime for measured boot attestation](#configuring-keylime-for-measured-boot-attestation) {#configuring-keylime-for-measured-boot-attestation .title}

To ensure your system boots into a trusted state, configure Keylime to compare UEFI boot event measurements against known-good reference values.

**Prerequisites**

-   You have network access to the systems where the Keylime components are configured:

    Verifier
    :   For more information, see [Deploying Keylime verifier from a package](#deploying-keylime-verifier-from-a-package "6.2. Deploying Keylime verifier from a package").

    Registrar
    :   For more information, see [Deploying Keylime registrar from a package](#deploying-keylime-registrar-from-a-package "6.4. Deploying Keylime registrar from a package").

    Tenant
    :   For more information, see [Deploying Keylime tenant from a package](#deploying-keylime-tenant-from-a-package "6.8. Deploying Keylime tenant from a package").

    Agent

    :   -   If you use pull model attestation: For more information, see [Deploying Keylime agent from a package](#deploying-keylime-agent-from-a-package "6.9. Deploying Keylime pull-model agent from a package").
        -   If you use push model attestation: For more information, see [Deploying Keylime push-model agent from a package](#deploying-keylime-push-model-agent-from-a-package "6.10. Deploying Keylime push-model agent from a package").

-   Unified Extensible Firmware Interface (UEFI) is enabled on the agent system.

**Procedure**

1.  On the monitored system where the Keylime agent is configured and running, install the `python3-keylime`{.literal} package, which contains the `keylime-policy`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y install python3-keylime
    ```

2.  On the monitored system, generate a policy from the measured boot log of the current state of the system by using the `keylime-policy`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    # keylime-policy create measured-boot --eventlog-file /sys/kernel/security/tpm0/binary_bios_measurements --output <measured_boot_reference_state.json>
    ```

    -   Replace *`<measured_boot_reference_state.json>`{.literal}* with the path where `keylime-policy`{.literal} saves the generated policy.

    -   If your UEFI system does not have Secure Boot enabled, pass the `--without-secureboot`{.literal} argument.

        Important

        The policy generated with `keylime-policy`{.literal} is based on the current state of the system and is very strict. Any modifications of the system including kernel updates and system updates will change the boot process and the system will fail the attestation.

3.  Copy the generated policy to the system where the `keylime_tenant`{.literal} utility is configured, for example:

    ``` {.language-plaintext tabindex="-1"}
    # scp root@<agent_ip>:<measured_boot_reference_state.json> <measured_boot_reference_state.json>
    ```

4.  On the system where the Keylime tenant is configured, provision the agent by using the `keylime_tenant`{.literal} utility:

    -   **If you use pull model attestation:**

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command add --targethost <agent_ip> --uuid <agent_uuid> --mb-policy <measured_boot_reference_state.json> --cert default
        ```

        -   Replace *`<agent_ip>`{.literal}* with the agent's IP address.
        -   Replace *`<agent_uuid>`{.literal}* with the agent's UUID.
        -   Replace *`<measured_boot_reference_state.json>`{.literal}* with the path to the measured boot policy.
        -   With the `--cert`{.literal} option, the tenant generates and signs a certificate for the agent.

        If you configure measured boot in combination with runtime monitoring, provide all the options from both use cases when entering the `keylime_tenant --command add`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command add --targethost <agent_ip> --uuid <agent_uuid> --runtime-policy <policy.json> --mb-policy <measured_boot_reference_state.json> --cert default
        ```

    -   **If you use push model attestation:**

        ``` {.language-plaintext tabindex="-1"}
         # keylime_tenant --command add --push-model --uuid <agent_uuid> --mb-policy <measured_boot_reference_state.json>
        ```

        -   Replace *`<agent_uuid>`{.literal}* with the agent's UUID.
        -   Replace *`<measured_boot_reference_state.json>`{.literal}* with the path to the measured boot policy.
        -   The `--push-model`{.literal} option indicates the agent uses push model attestation. Because the verifier does not connect to the agent in the push model, you do not need to specify the agent's IP address with the `--targethost`{.literal} option.

        If you configure measured boot in combination with runtime monitoring, provide all the options from both use cases when entering the `keylime_tenant --command add`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command add --push-model --uuid <agent_uuid> --runtime-policy <policy.json> --mb-policy <measured_boot_reference_state.json>
        ```

**Verification**

1.  Reboot the monitored system and verify a successful attestation of the agent:

    -   **If you use pull model attestation:**

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command cvstatus --uuid <agent_uuid>
        ```

        Replace *`<agent_uuid>`{.literal}* with the agent's UUID.

        If the value of `operational_state`{.literal} is `Get Quote`{.literal} and `attestation_count`{.literal} is nonzero, the attestation of this agent is successful.

        ``` {.language-plaintext tabindex="-1"}
        ...
        {"<agent_uuid>": {"operational_state": "Get Quote"..."attestation_count": 5
        ...
        ```

        If the value of `operational_state`{.literal} is `Invalid Quote`{.literal} or `Failed`{.literal} attestation fails, the command displays output similar to the following:

        ``` {.language-plaintext tabindex="-1"}
        {"<agent_uuid>": {"operational_state": "Invalid Quote", ... "ima.validation.ima-ng.not_in_allowlist", "attestation_count": 5, "last_received_quote": 1684150329, "last_successful_attestation": 1684150327}}
        ```

    -   **If you use push model attestation**:

        ``` {.language-plaintext tabindex="-1"}
        # keylime_tenant --command cvstatus --push-model --uuid <agent_uuid>
        ```

        Replace *`<agent_uuid>`{.literal}* with the agent's UUID.

        Push-model agents do not use the `operational_state`{.literal} field. Instead, check the `attestation_status`{.literal} field, which returns `PENDING`{.literal}, `PASS`{.literal}, `FAIL`{.literal}, or `TIMEOUT`{.literal}. If the value of `attestation_status`{.literal} is `PASS`{.literal} and `attestation_count`{.literal} is nonzero, the attestation of this agent is successful:

        ``` {.language-plaintext tabindex="-1"}
        {"<agent_uuid>": {"attestation_status": "PASS", "attestation_count": 5, ...}}
        ```

2.  If the attestation fails, display more details in the verifier log:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u keylime_verifier
    {"d432fbb3-d2f1-4a97-9ef7-75bd81c00000": {"operational_state": "Tenant Quote Failed", ... "last_event_id": "measured_boot.invalid_pcr_0", "attestation_count": 0, "last_received_quote": 1684487093, "last_successful_attestation": 0}}
    ```

**Next steps**

-   To modify the configuration of an already registered agent, use the `keylime_tenant --command update`{.literal} command. For push-model agents, include the `--push-model`{.literal} option with the `update`{.literal} command.
-   To stop Keylime from monitoring a node, use the `keylime_tenant --command delete --targethost `{.literal}*`<agent_ip>`{.literal}*` --uuid `{.literal}*`<agent_uuid>`{.literal}* command. The `delete`{.literal} command works identically for both pull-model and push-model agents and does not require the `--push-model`{.literal} option.

### [6.13. Keylime configuration](#keylime-environment-variables) {#keylime-configuration .title}

To safely customize Keylime components, logging, and certificate authorities without modifying default configuration files, you can use drop-in files or environment variables. These methods prevent configuration errors and let you override settings in both standard and containerized deployments.

You can pass environment variables to a container by using the `-e`{.literal} option with the `podman run`{.literal} command.

The environment variables have the following syntax:

``` {.language-plaintext tabindex="-1"}
KEYLIME_<SECTION>_<ENVIRONMENT_VARIABLE>=<value>
```

Where:

-   *`<SECTION>`{.literal}* is the section of the Keylime configuration file.
-   *`<ENVIRONMENT_VARIABLE>`{.literal}* is the environment variable.
-   *`<value>`{.literal}* is the value to which you want to set the environment variable.

For example, `-e KEYLIME_VERIFIER_MAX_RETRIES=6`{.literal} sets the `max_retries`{.literal} configuration option in the `[verifier]`{.literal} section to `6`{.literal}.

#### [6.13.1. General verifier configuration](#general_verifier_configuration) {#general-verifier-configuration .title}

To customize the verifier, you can add configuration drop-in files in the `/etc/keylime/verifier.conf.d/`{.literal} directory. These drop-in files keep your custom settings separate from the default configuration to prevent errors during system updates.

+:--------------------------------------------+:-------------------------------------------------------------+:-------------------------------------------------------------------------------------+
| Configuration option                        | Environment variable                                         | Default value                                                                        |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `auto_migrate_db`{.literal}                 | `KEYLIME_VERIFIER_AUTO_MIGRATE_DB`{.literal}                 | `True`{.literal}                                                                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `client_cert`{.literal}                     | `KEYLIME_VERIFIER_CLIENT_CERT`{.literal}                     | `default`{.literal}                                                                  |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `client_key_password`{.literal}             | `KEYLIME_VERIFIER_CLIENT_KEY_PASSWORD`{.literal}             |                                                                                      |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `client_key`{.literal}                      | `KEYLIME_VERIFIER_CLIENT_KEY`{.literal}                      | `default`{.literal}                                                                  |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `database_pool_sz_ovfl`{.literal}           | `KEYLIME_VERIFIER_DATABASE_POOL_SZ_OVFL`{.literal}           | `5,10`{.literal}                                                                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `database_url`{.literal}                    | `KEYLIME_VERIFIER_DATABASE_URL`{.literal}                    | `sqlite`{.literal}                                                                   |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `durable_attestation_import`{.literal}      | `KEYLIME_VERIFIER_DURABLE_ATTESTATION_IMPORT`{.literal}      |                                                                                      |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `enable_agent_mtls`{.literal}               | `KEYLIME_VERIFIER_ENABLE_AGENT_MTLS`{.literal}               | `True`{.literal}                                                                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `exponential_backoff`{.literal}             | `KEYLIME_VERIFIER_EXPONENTIAL_BACKOFF`{.literal}             | `True`{.literal}                                                                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `ignore_tomtou_errors`{.literal}            | `KEYLIME_VERIFIER_IGNORE_TOMTOU_ERRORS`{.literal}            | `False`{.literal}                                                                    |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `ip`{.literal}                              | `KEYLIME_VERIFIER_IP`{.literal}                              | `127.0.0.1`{.literal}                                                                |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `max_retries`{.literal}                     | `KEYLIME_VERIFIER_MAX_RETRIES`{.literal}                     | `5`{.literal}                                                                        |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `max_upload_size`{.literal}                 | `KEYLIME_VERIFIER_MAX_UPLOAD_SIZE`{.literal}                 | `104857600`{.literal}                                                                |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `measured_boot_evaluate`{.literal}          | `KEYLIME_VERIFIER_MEASURED_BOOT_EVALUATE`{.literal}          | `once`{.literal}                                                                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `measured_boot_imports`{.literal}           | `KEYLIME_VERIFIER_MEASURED_BOOT_IMPORTS`{.literal}           | `[]`{.literal}                                                                       |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `measured_boot_policy_name`{.literal}       | `KEYLIME_VERIFIER_MEASURED_BOOT_POLICY_NAME`{.literal}       | `accept-all`{.literal}                                                               |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `num_workers`{.literal}                     | `KEYLIME_VERIFIER_NUM_WORKERS`{.literal}                     | `0`{.literal}                                                                        |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `persistent_store_encoding`{.literal}       | `KEYLIME_VERIFIER_PERSISTENT_STORE_ENCODING`{.literal}       |                                                                                      |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `persistent_store_format`{.literal}         | `KEYLIME_VERIFIER_PERSISTENT_STORE_FORMAT`{.literal}         | `json`{.literal}                                                                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `persistent_store_url`{.literal}            | `KEYLIME_VERIFIER_PERSISTENT_STORE_URL`{.literal}            |                                                                                      |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `port`{.literal}                            | `KEYLIME_VERIFIER_PORT`{.literal}                            | `8881`{.literal}                                                                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `quote_interval`{.literal}                  | `KEYLIME_VERIFIER_QUOTE_INTERVAL`{.literal}                  | `2`{.literal}                                                                        |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `registrar_ip`{.literal}                    | `KEYLIME_VERIFIER_REGISTRAR_IP`{.literal}                    | `127.0.0.1`{.literal}                                                                |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `registrar_port`{.literal}                  | `KEYLIME_VERIFIER_REGISTRAR_PORT`{.literal}                  | `8891`{.literal}                                                                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `request_timeout`{.literal}                 | `KEYLIME_VERIFIER_REQUEST_TIMEOUT`{.literal}                 | `60.0`{.literal}                                                                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `require_allow_list_signatures`{.literal}   | `KEYLIME_VERIFIER_REQUIRE_ALLOW_LIST_SIGNATURES`{.literal}   | `True`{.literal}                                                                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `retry_interval`{.literal}                  | `KEYLIME_VERIFIER_RETRY_INTERVAL`{.literal}                  | `2`{.literal}                                                                        |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `server_cert`{.literal}                     | `KEYLIME_VERIFIER_SERVER_CERT`{.literal}                     | `default`{.literal}                                                                  |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `server_key_password`{.literal}             | `KEYLIME_VERIFIER_SERVER_KEY_PASSWORD`{.literal}             | `default`{.literal}                                                                  |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `server_key`{.literal}                      | `KEYLIME_VERIFIER_SERVER_KEY`{.literal}                      | `default`{.literal}                                                                  |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `severity_labels`{.literal}                 | `KEYLIME_VERIFIER_SEVERITY_LABELS`{.literal}                 | `["info", "notice", "warning", "error", "critical", "alert", "emergency"]`{.literal} |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `severity_policy`{.literal}                 | `KEYLIME_VERIFIER_SEVERITY_POLICY`{.literal}                 | `[{"event_id": ".*", "severity_label" : "emergency"}]`{.literal}                     |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `signed_attributes`{.literal}               | `KEYLIME_VERIFIER_SIGNED_ATTRIBUTES`{.literal}               |                                                                                      |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `time_stamp_authority_certs_path`{.literal} | `KEYLIME_VERIFIER_TIME_STAMP_AUTHORITY_CERTS_PATH`{.literal} |                                                                                      |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `time_stamp_authority_url`{.literal}        | `KEYLIME_VERIFIER_TIME_STAMP_AUTHORITY_URL`{.literal}        |                                                                                      |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `tls_dir`{.literal}                         | `KEYLIME_VERIFIER_TLS_DIR`{.literal}                         | `generate`{.literal}                                                                 |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `transparency_log_sign_algo`{.literal}      | `KEYLIME_VERIFIER_TRANSPARENCY_LOG_SIGN_ALGO`{.literal}      | `sha256`{.literal}                                                                   |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `transparency_log_url`{.literal}            | `KEYLIME_VERIFIER_TRANSPARENCY_LOG_URL`{.literal}            |                                                                                      |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `trusted_client_ca`{.literal}               | `KEYLIME_VERIFIER_TRUSTED_CLIENT_CA`{.literal}               | `default`{.literal}                                                                  |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `trusted_server_ca`{.literal}               | `KEYLIME_VERIFIER_TRUSTED_SERVER_CA`{.literal}               | `default`{.literal}                                                                  |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `uuid`{.literal}                            | `KEYLIME_VERIFIER_UUID`{.literal}                            | `default`{.literal}                                                                  |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `version`{.literal}                         | `KEYLIME_VERIFIER_VERSION`{.literal}                         | `2.0`{.literal}                                                                      |
+---------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------+

: Table 6.3. \[verifier\] section

Show more

+:---------------------------------------------+:--------------------------------------------------------------------------+:---------------------+
| Configuration option                         | Environment variable                                                      | Default value        |
+----------------------------------------------+---------------------------------------------------------------------------+----------------------+
| `enabled_revocation_notifications`{.literal} | `KEYLIME_VERIFIER_REVOCATIONS_ENABLED_REVOCATION_NOTIFICATIONS`{.literal} | `[agent]`{.literal}  |
+----------------------------------------------+---------------------------------------------------------------------------+----------------------+
| `webhook_url`{.literal}                      | `KEYLIME_VERIFIER_REVOCATIONS_WEBHOOK_URL`{.literal}                      |                      |
+----------------------------------------------+---------------------------------------------------------------------------+----------------------+

: Table 6.4. \[revocations\] section

Show more

#### [6.13.2. Additional verifier configuration for the push model](#additional_verifier_configuration_for_the_push_model) {#additional-verifier-configuration-for-the-push-model .title}

To customize the verifier for the push model, you can add configuration drop-in files in the `/etc/keylime/verifier.conf.d/`{.literal} directory. These drop-in files keep your custom settings separate from the default configuration to prevent errors during system updates.

The `quote_interval`{.literal} option is a general verifier option used by both pull and push models. In the push model, it is used to derive the agent attestation timeout threshold.

Rate-limiting options protect the verifier against denial-of-service attacks in the push model, where the verifier accepts inbound connections from all agents.

+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configuration option                               | Environment variable                                                | Default value     | Description                                                                                                                                                                                                                                            |
+:===================================================+:====================================================================+:==================+:=======================================================================================================================================================================================================================================================+
| `mode`{.literal}                                   | `KEYLIME_VERIFIER_MODE`{.literal}                                   | `pull`{.literal}  | Attestation mode. Set to `push`{.literal} to enable push-model attestation. A single verifier cannot operate in both modes simultaneously.                                                                                                             |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `quote_interval`{.literal}                         | `KEYLIME_VERIFIER_QUOTE_INTERVAL`{.literal}                         | `2`{.literal}     | Interval in seconds between attestation checks. In the pull model, this is the polling interval. In the push model, the agent timeout is derived as `quote_interval * 5`{.literal}. Agents that do not attest within this period are marked as failed. |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `challenge_lifetime`{.literal}                     | `KEYLIME_VERIFIER_CHALLENGE_LIFETIME`{.literal}                     | `1800`{.literal}  | Lifetime in seconds (30 minutes) for PoP challenges sent to agents. Challenges that are not answered within this period expire.                                                                                                                        |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `verification_timeout`{.literal}                   | `KEYLIME_VERIFIER_VERIFICATION_TIMEOUT`{.literal}                   | `0`{.literal}     | Maximum time in seconds permitted for evidence verification to complete. A value of `0`{.literal} means the timeout is determined automatically.                                                                                                       |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `session_lifetime`{.literal}                       | `KEYLIME_VERIFIER_SESSION_LIFETIME`{.literal}                       | `180`{.literal}   | Lifetime in seconds for authenticated push-model sessions. After this period, the agent must re-authenticate using PoP.                                                                                                                                |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `extend_token_on_attestation`{.literal}            | `KEYLIME_VERIFIER_EXTEND_TOKEN_ON_ATTESTATION`{.literal}            | `true`{.literal}  | When enabled, successful attestation extends the session token lifetime, preventing re-authentication for agents that are actively attesting.                                                                                                          |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `auto_recover_attestation_failures`{.literal}      | `KEYLIME_VERIFIER_AUTO_RECOVER_ATTESTATION_FAILURES`{.literal}      | `false`{.literal} | Whether to allow push-model agents to automatically recover from attestation failures without manual intervention.                                                                                                                                     |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `shutdown_drain_timeout`{.literal}                 | `KEYLIME_VERIFIER_SHUTDOWN_DRAIN_TIMEOUT`{.literal}                 | `10`{.literal}    | Time in seconds to wait for in-flight push-model requests to complete during verifier shutdown.                                                                                                                                                        |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `session_create_rate_limit_per_ip`{.literal}       | `KEYLIME_VERIFIER_SESSION_CREATE_RATE_LIMIT_PER_IP`{.literal}       | `50`{.literal}    | Maximum number of session creation requests allowed per IP address within the rate limit window.                                                                                                                                                       |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `session_create_rate_limit_window_ip`{.literal}    | `KEYLIME_VERIFIER_SESSION_CREATE_RATE_LIMIT_WINDOW_IP`{.literal}    | `60`{.literal}    | Time window in seconds for IP-based rate limiting.                                                                                                                                                                                                     |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `session_create_rate_limit_per_agent`{.literal}    | `KEYLIME_VERIFIER_SESSION_CREATE_RATE_LIMIT_PER_AGENT`{.literal}    | `15`{.literal}    | Maximum number of session creation requests allowed per agent UUID within the rate limit window.                                                                                                                                                       |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `session_create_rate_limit_window_agent`{.literal} | `KEYLIME_VERIFIER_SESSION_CREATE_RATE_LIMIT_WINDOW_AGENT`{.literal} | `60`{.literal}    | Time window in seconds for per-agent rate limiting.                                                                                                                                                                                                    |
+----------------------------------------------------+---------------------------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 6.5. \[verifier\] section

Show more

#### [6.13.3. Registrar configuration](#registrar_configuration) {#registrar-configuration .title}

To customize the registrar, you can add configuration drop-in files in the `/etc/keylime/registrar.conf.d/`{.literal} directory. These drop-in files keep your custom settings separate from the default configuration to prevent errors during system updates.

+:--------------------------------------------+:--------------------------------------------------------------+:-------------------------------------+
| Configuration option                        | Environment variable                                          | Default value                        |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `auto_migrate_db`{.literal}                 | `KEYLIME_REGISTRAR_AUTO_MIGRATE_DB`{.literal}                 | `True`{.literal}                     |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `database_pool_sz_ovfl`{.literal}           | `KEYLIME_REGISTRAR_DATABASE_POOL_SZ_OVFL`{.literal}           | `5,10`{.literal}                     |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `database_url`{.literal}                    | `KEYLIME_REGISTRAR_DATABASE_URL`{.literal}                    | `sqlite`{.literal}                   |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `durable_attestation_import`{.literal}      | `KEYLIME_REGISTRAR_DURABLE_ATTESTATION_IMPORT`{.literal}      |                                      |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `ip`{.literal}                              | `KEYLIME_REGISTRAR_IP`{.literal}                              | `127.0.0.1`{.literal}                |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `persistent_store_encoding`{.literal}       | `KEYLIME_REGISTRAR_PERSISTENT_STORE_ENCODING`{.literal}       |                                      |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `persistent_store_format`{.literal}         | `KEYLIME_REGISTRAR_PERSISTENT_STORE_FORMAT`{.literal}         | `json`{.literal}                     |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `persistent_store_url`{.literal}            | `KEYLIME_REGISTRAR_PERSISTENT_STORE_URL`{.literal}            |                                      |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `port`{.literal}                            | `KEYLIME_REGISTRAR_PORT`{.literal}                            | `8890`{.literal}                     |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `prov_db_filename`{.literal}                | `KEYLIME_REGISTRAR_PROV_DB_FILENAME`{.literal}                | `provider_reg_data.sqlite`{.literal} |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `server_cert`{.literal}                     | `KEYLIME_REGISTRAR_SERVER_CERT`{.literal}                     | `default`{.literal}                  |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `server_key_password`{.literal}             | `KEYLIME_REGISTRAR_SERVER_KEY_PASSWORD`{.literal}             | `default`{.literal}                  |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `server_key`{.literal}                      | `KEYLIME_REGISTRAR_SERVER_KEY`{.literal}                      | `default`{.literal}                  |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `signed_attributes`{.literal}               | `KEYLIME_REGISTRAR_SIGNED_ATTRIBUTES`{.literal}               | `ek_tpm,aik_tpm,ekcert`{.literal}    |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `time_stamp_authority_certs_path`{.literal} | `KEYLIME_REGISTRAR_TIME_STAMP_AUTHORITY_CERTS_PATH`{.literal} |                                      |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `time_stamp_authority_url`{.literal}        | `KEYLIME_REGISTRAR_TIME_STAMP_AUTHORITY_URL`{.literal}        |                                      |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `tls_dir`{.literal}                         | `KEYLIME_REGISTRAR_TLS_DIR`{.literal}                         | `default`{.literal}                  |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `tls_port`{.literal}                        | `KEYLIME_REGISTRAR_TLS_PORT`{.literal}                        | `8891`{.literal}                     |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `transparency_log_sign_algo`{.literal}      | `KEYLIME_REGISTRAR_TRANSPARENCY_LOG_SIGN_ALGO`{.literal}      | `sha256`{.literal}                   |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `transparency_log_url`{.literal}            | `KEYLIME_REGISTRAR_TRANSPARENCY_LOG_URL`{.literal}            |                                      |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `trusted_client_ca`{.literal}               | `KEYLIME_REGISTRAR_TRUSTED_CLIENT_CA`{.literal}               | `default`{.literal}                  |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+
| `version`{.literal}                         | `KEYLIME_REGISTRAR_VERSION`{.literal}                         | `2.0`{.literal}                      |
+---------------------------------------------+---------------------------------------------------------------+--------------------------------------+

: Table 6.6. \[registrar\] section

Show more

#### [6.13.4. Tenant configuration](#tenant_configuration) {#tenant-configuration .title}

To customize the tenant, you can add configuration drop-in files in the `/etc/keylime/tenant.conf.d/`{.literal} directory. These drop-in files keep your custom settings separate from the default configuration to prevent errors during system updates.

+:---------------------------------------+:------------------------------------------------------+:--------------------------------------------+
| Configuration option                   | Environment variable                                  | Default value                               |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `accept_tpm_encryption_algs`{.literal} | `KEYLIME_TENANT_ACCEPT_TPM_ENCRYPTION_ALGS`{.literal} | `ecc, rsa`{.literal}                        |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `accept_tpm_hash_algs`{.literal}       | `KEYLIME_TENANT_ACCEPT_TPM_HASH_ALGS`{.literal}       | `sha512, sha384, sha256`{.literal}          |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `accept_tpm_signing_algs`{.literal}    | `KEYLIME_TENANT_ACCEPT_TPM_SIGNING_ALGS`{.literal}    | `ecschnorr, rsassa`{.literal}               |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `client_cert`{.literal}                | `KEYLIME_TENANT_CLIENT_CERT`{.literal}                | `default`{.literal}                         |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `client_key_password`{.literal}        | `KEYLIME_TENANT_CLIENT_KEY_PASSWORD`{.literal}        |                                             |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `client_key`{.literal}                 | `KEYLIME_TENANT_CLIENT_KEY`{.literal}                 | `default`{.literal}                         |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `ek_check_script`{.literal}            | `KEYLIME_TENANT_EK_CHECK_SCRIPT`{.literal}            |                                             |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `enable_agent_mtls`{.literal}          | `KEYLIME_TENANT_ENABLE_AGENT_MTLS`{.literal}          | `True`{.literal}                            |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `exponential_backoff`{.literal}        | `KEYLIME_TENANT_EXPONENTIAL_BACKOFF`{.literal}        | `True`{.literal}                            |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `max_payload_size`{.literal}           | `KEYLIME_TENANT_MAX_PAYLOAD_SIZE`{.literal}           | `1048576`{.literal}                         |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `max_retries`{.literal}                | `KEYLIME_TENANT_MAX_RETRIES`{.literal}                | `5`{.literal}                               |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `mb_refstate`{.literal}                | `KEYLIME_TENANT_MB_REFSTATE`{.literal}                |                                             |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `registrar_ip`{.literal}               | `KEYLIME_TENANT_REGISTRAR_IP`{.literal}               | `127.0.0.1`{.literal}                       |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `registrar_port`{.literal}             | `KEYLIME_TENANT_REGISTRAR_PORT`{.literal}             | `8891`{.literal}                            |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `request_timeout`{.literal}            | `KEYLIME_TENANT_REQUEST_TIMEOUT`{.literal}            | `60`{.literal}                              |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `require_ek_cert`{.literal}            | `KEYLIME_TENANT_REQUIRE_EK_CERT`{.literal}            | `True`{.literal}                            |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `retry_interval`{.literal}             | `KEYLIME_TENANT_RETRY_INTERVAL`{.literal}             | `2`{.literal}                               |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `tls_dir`{.literal}                    | `KEYLIME_TENANT_TLS_DIR`{.literal}                    | `default`{.literal}                         |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `tpm_cert_store`{.literal}             | `KEYLIME_TENANT_TPM_CERT_STORE`{.literal}             | `/var/lib/keylime/tpm_cert_store`{.literal} |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `trusted_server_ca`{.literal}          | `KEYLIME_TENANT_TRUSTED_SERVER_CA`{.literal}          | `default`{.literal}                         |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `verifier_ip`{.literal}                | `KEYLIME_TENANT_VERIFIER_IP`{.literal}                | `127.0.0.1`{.literal}                       |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `verifier_port`{.literal}              | `KEYLIME_TENANT_VERIFIER_PORT`{.literal}              | `8881`{.literal}                            |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+
| `version`{.literal}                    | `KEYLIME_TENANT_VERSION`{.literal}                    | `2.0`{.literal}                             |
+----------------------------------------+-------------------------------------------------------+---------------------------------------------+

: Table 6.7. \[tenant\] section

Show more

#### [6.13.5. CA configuration](#ca_configuration) {#ca-configuration .title}

To customize the certificate authorities, you can add configuration drop-in files in the `/etc/keylime/ca.conf.d/`{.literal} directory. These drop-in files keep your custom settings separate from the default configuration to prevent errors during system updates.

+:------------------------------+:-----------------------------------------+:------------------------------------------+
| Configuration option          | Environment variable                     | Default value                             |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `cert_bits`{.literal}         | `KEYLIME_CA_CERT_BITS`{.literal}         | `2048`{.literal}                          |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `cert_ca_lifetime`{.literal}  | `KEYLIME_CA_CERT_CA_LIFETIME`{.literal}  | `3650`{.literal}                          |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `cert_ca_name`{.literal}      | `KEYLIME_CA_CERT_CA_NAME`{.literal}      | `Keylime Certificate Authority`{.literal} |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `cert_country`{.literal}      | `KEYLIME_CA_CERT_COUNTRY`{.literal}      | `US`{.literal}                            |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `cert_crl_dist`{.literal}     | `KEYLIME_CA_CERT_CRL_DIST`{.literal}     | `http://localhost:38080/crl`{.literal}    |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `cert_lifetime`{.literal}     | `KEYLIME_CA_CERT_LIFETIME`{.literal}     | `365`{.literal}                           |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `cert_locality`{.literal}     | `KEYLIME_CA_CERT_LOCALITY`{.literal}     | `Lexington`{.literal}                     |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `cert_org_unit`{.literal}     | `KEYLIME_CA_CERT_ORG_UNIT`{.literal}     | `53`{.literal}                            |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `cert_organization`{.literal} | `KEYLIME_CA_CERT_ORGANIZATION`{.literal} | `MITLL`{.literal}                         |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `cert_state`{.literal}        | `KEYLIME_CA_CERT_STATE`{.literal}        | `MA`{.literal}                            |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `password`{.literal}          | `KEYLIME_CA_PASSWORD`{.literal}          | `default`{.literal}                       |
+-------------------------------+------------------------------------------+-------------------------------------------+
| `version`{.literal}           | `KEYLIME_CA_VERSION`{.literal}           | `2.0`{.literal}                           |
+-------------------------------+------------------------------------------+-------------------------------------------+

: Table 6.8. \[ca\] section

Show more

#### [6.13.6. General agent configuration](#general_agent_configuration) {#general-agent-configuration .title}

To customize the agent, you can add configuration drop-in files in the `/etc/keylime/agent.conf.d/`{.literal} directory. These drop-in files keep your custom settings separate from the default configuration to prevent errors during system updates. The agent configuration uses the TOML format.

+:--------------------------------------------+:----------------------------------------------------------+:-------------------------------------------------+
| Configuration option                        | Environment variable                                      | Default value                                    |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `contact_ip`{.literal}                      | `KEYLIME_AGENT_CONTACT_IP`{.literal}                      | `127.0.0.1`{.literal}                            |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `contact_port`{.literal}                    | `KEYLIME_AGENT_CONTACT_PORT`{.literal}                    | `9002`{.literal}                                 |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `dec_payload_file`{.literal}                | `KEYLIME_AGENT_DEC_PAYLOAD_FILE`{.literal}                | `decrypted_payload`{.literal}                    |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `ek_handle`{.literal}                       | `KEYLIME_AGENT_EK_HANDLE`{.literal}                       | `generate`{.literal}                             |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `enable_agent_mtls`{.literal}               | `KEYLIME_AGENT_ENABLE_AGENT_MTLS`{.literal}               | `true`{.literal}                                 |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `enable_insecure_payload`{.literal}         | `KEYLIME_AGENT_ENABLE_INSECURE_PAYLOAD`{.literal}         | `false`{.literal}                                |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `enable_revocation_notifications`{.literal} | `KEYLIME_AGENT_ENABLE_REVOCATION_NOTIFICATIONS`{.literal} | `true`{.literal}                                 |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `enc_keyname`{.literal}                     | `KEYLIME_AGENT_ENC_KEYNAME`{.literal}                     | `derived_tci_key`{.literal}                      |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `exponential_backoff`{.literal}             | `KEYLIME_AGENT_EXPONENTIAL_BACKOFF`{.literal}             | `true`{.literal}                                 |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `extract_payload_zip`{.literal}             | `KEYLIME_AGENT_EXTRACT_PAYLOAD_ZIP`{.literal}             | `true`{.literal}                                 |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `ip`{.literal}                              | `KEYLIME_AGENT_IP`{.literal}                              | `127.0.0.1`{.literal}                            |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `max_retries`{.literal}                     | `KEYLIME_AGENT_MAX_RETRIES`{.literal}                     | `4`{.literal}                                    |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `measure_payload_pcr`{.literal}             | `KEYLIME_AGENT_MEASURE_PAYLOAD_PCR`{.literal}             | `-1`{.literal}                                   |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `payload_script`{.literal}                  | `KEYLIME_AGENT_PAYLOAD_SCRIPT`{.literal}                  | `autorun.sh`{.literal}                           |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `port`{.literal}                            | `KEYLIME_AGENT_PORT`{.literal}                            | `9002`{.literal}                                 |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `registrar_ip`{.literal}                    | `KEYLIME_AGENT_REGISTRAR_IP`{.literal}                    | `127.0.0.1`{.literal}                            |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `registrar_port`{.literal}                  | `KEYLIME_AGENT_REGISTRAR_PORT`{.literal}                  | `8890`{.literal}                                 |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `retry_interval`{.literal}                  | `KEYLIME_AGENT_RETRY_INTERVAL`{.literal}                  | `2`{.literal}                                    |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `revocation_actions`{.literal}              | `KEYLIME_AGENT_REVOCATION_ACTIONS`{.literal}              | `[]`{.literal}                                   |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `revocation_cert`{.literal}                 | `KEYLIME_AGENT_REVOCATION_CERT`{.literal}                 | `default`{.literal}                              |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `revocation_notification_ip`{.literal}      | `KEYLIME_AGENT_REVOCATION_NOTIFICATION_IP`{.literal}      | `127.0.0.1`{.literal}                            |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `revocation_notification_port`{.literal}    | `KEYLIME_AGENT_REVOCATION_NOTIFICATION_PORT`{.literal}    | `8992`{.literal}                                 |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `run_as`{.literal}                          | `KEYLIME_AGENT_RUN_AS`{.literal}                          | `keylime:tss`{.literal}                          |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `secure_size`{.literal}                     | `KEYLIME_AGENT_SECURE_SIZE`{.literal}                     | `1m`{.literal}                                   |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `server_cert`{.literal}                     | `KEYLIME_AGENT_SERVER_CERT`{.literal}                     | `default`{.literal}                              |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `server_key_password`{.literal}             | `KEYLIME_AGENT_SERVER_KEY_PASSWORD`{.literal}             |                                                  |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `server_key`{.literal}                      | `KEYLIME_AGENT_SERVER_KEY`{.literal}                      | `default`{.literal}                              |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `tls_dir`{.literal}                         | `KEYLIME_AGENT_TLS_DIR`{.literal}                         | `default`{.literal}                              |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `tpm_encryption_alg`{.literal}              | `KEYLIME_AGENT_TPM_ENCRYPTION_ALG`{.literal}              | `rsa`{.literal}                                  |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `tpm_hash_alg`{.literal}                    | `KEYLIME_AGENT_TPM_HASH_ALG`{.literal}                    | `sha256`{.literal}                               |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `tpm_ownerpassword`{.literal}               | `KEYLIME_AGENT_TPM_OWNERPASSWORD`{.literal}               |                                                  |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `tpm_signing_alg`{.literal}                 | `KEYLIME_AGENT_TPM_SIGNING_ALG`{.literal}                 | `rsassa`{.literal}                               |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `trusted_client_ca`{.literal}               | `KEYLIME_AGENT_TRUSTED_CLIENT_CA`{.literal}               | `default`{.literal}                              |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `uuid`{.literal}                            | `KEYLIME_AGENT_UUID`{.literal}                            | `d432fbb3-d2f1-4a97-9ef7-75bd81c00000`{.literal} |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+
| `version`{.literal}                         | `KEYLIME_AGENT_VERSION`{.literal}                         | `2.0`{.literal}                                  |
+---------------------------------------------+-----------------------------------------------------------+--------------------------------------------------+

: Table 6.9. \[agent\] section

Show more

#### [6.13.7. Additional agent configuration for the push model](#additional_agent_configuration_for_the_push_model) {#additional-agent-configuration-for-the-push-model .title}

To customize the agent for the push model, you can add configuration drop-in files in the `/etc/keylime/agent.conf.d/`{.literal} directory. These drop-in files keep your custom settings separate from the default configuration to prevent errors during system updates. The agent configuration uses the TOML format.

The push-model agent, provided by the `keylime-agent-rust-push`{.literal} package, shares the same configuration file as the default pull-model agent. The following options are specific to or primarily relevant for push-model deployments. Some options behave differently in push-model attestation. These differences are noted in the Description column.

Exponential backoff options control retry behavior when the agent encounters errors such as network failures or verifier unavailability.

Warning

Disabling TLS verification exposes your infrastructure to man-in-the-middle attacks. Never enable the options that bypass TLS checks in a production environment. Use these insecure settings only in a testing environment to troubleshoot deployment issues.

+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configuration option                             | Environment variable                                           | Default value                                                | Description                                                                                                                                                                                                                                                                                                                                                                                              |
+:=================================================+:===============================================================+:=============================================================+:=========================================================================================================================================================================================================================================================================================================================================================================================================+
| `verifier_url`{.literal}                         | `KEYLIME_AGENT_VERIFIER_URL`{.literal}                         | [`https://localhost:8881`{.literal}](https://localhost:8881) | URL of the Keylime verifier, including schema, host, and port. Must use HTTPS.                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `verifier_tls_ca_cert`{.literal}                 | `KEYLIME_AGENT_VERIFIER_TLS_CA_CERT`{.literal}                 | `default`{.literal}                                          | Path to the CA certificate used to verify the verifier's TLS server certificate. When set to `default`{.literal}, the path `cv_ca/cacert.crt`{.literal} relative to `keylime_dir`{.literal} is used.                                                                                                                                                                                                     |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `attestation_interval_seconds`{.literal}         | `KEYLIME_AGENT_ATTESTATION_INTERVAL_SECONDS`{.literal}         | `60`{.literal}                                               | Fallback interval in seconds between push attestation cycles. The verifier dynamically overrides this parameter by returning `seconds_to_next_attestation`{.literal} in its response payload. The agent uses `attestation_interval_seconds`{.literal} during initial startup or when no verifier response exists. This value must be lower than the verifier's timeout (`quote_interval * 5`{.literal}). |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `registrar_tls_enabled`{.literal}                | `KEYLIME_AGENT_REGISTRAR_TLS_ENABLED`{.literal}                | `false`{.literal}                                            | Enable TLS for communication between the push model agent and the registrar. When enabled, the agent uses TLS with server verification when communicating with the registrar.                                                                                                                                                                                                                            |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `registrar_tls_port`{.literal}                   | `KEYLIME_AGENT_REGISTRAR_TLS_PORT`{.literal}                   | `8891`{.literal}                                             | TLS port of the registrar. Used when `registrar_tls_enabled`{.literal} is set to `true`{.literal}.                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `registrar_tls_ca_cert`{.literal}                | `KEYLIME_AGENT_REGISTRAR_TLS_CA_CERT`{.literal}                | `default`{.literal}                                          | CA certificate for verifying the registrar's TLS server certificate. Used when `registrar_tls_enabled`{.literal} is set to `true`{.literal}. When set to `default`{.literal}, the path `cv_ca/cacert.crt`{.literal} relative to `keylime_dir`{.literal} is used.                                                                                                                                         |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `api_versions`{.literal}                         | `KEYLIME_AGENT_API_VERSIONS`{.literal}                         | `default`{.literal}                                          | The push-model agent always uses API version 3.0 regardless of this setting. Any configured value is silently overridden.                                                                                                                                                                                                                                                                                |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `registrar_api_versions`{.literal}               | `KEYLIME_AGENT_REGISTRAR_API_VERSIONS`{.literal}               | `default`{.literal}                                          | API versions to use when communicating with the registrar. The agent negotiates the best mutually supported version.                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `certification_keys_server_identifier`{.literal} | `KEYLIME_AGENT_CERTIFICATION_KEYS_SERVER_IDENTIFIER`{.literal} | `ak`{.literal}                                               | Server identifier used for Attestation Key (AK) certification data.                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `uefi_logs_evidence_version`{.literal}           | `KEYLIME_AGENT_UEFI_LOGS_EVIDENCE_VERSION`{.literal}           | `2.1`{.literal}                                              | Evidence version to use for UEFI event logs sent during attestation.                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ek_handle`{.literal}                            | `KEYLIME_AGENT_EK_HANDLE`{.literal}                            | `""`{.literal}                                               | EK handle on the TPM. The push-model agent always uses auto-detection (empty string), ignoring any configured value. Custom EK handles (for example, `"0x81000000"`{.literal}) are only supported by the pull-model agent.                                                                                                                                                                               |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `exponential_backoff_initial_delay`{.literal}    | `KEYLIME_AGENT_EXPONENTIAL_BACKOFF_INITIAL_DELAY`{.literal}    | `10000`{.literal}                                            | Initial retry delay in milliseconds (10 seconds).                                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `exponential_backoff_max_retries`{.literal}      | `KEYLIME_AGENT_EXPONENTIAL_BACKOFF_MAX_RETRIES`{.literal}      | `5`{.literal}                                                | Maximum number of retry attempts.                                                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `exponential_backoff_max_delay`{.literal}        | `KEYLIME_AGENT_EXPONENTIAL_BACKOFF_MAX_DELAY`{.literal}        | `300000`{.literal}                                           | Maximum delay in milliseconds between retries (5 minutes).                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `tls_accept_invalid_certs`{.literal}             | `KEYLIME_AGENT_TLS_ACCEPT_INVALID_CERTS`{.literal}             | `false`{.literal}                                            | Accept invalid TLS certificates (for example, self-signed, expired, wrong CA). Must be used only in a testing environment.                                                                                                                                                                                                                                                                               |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `tls_accept_invalid_hostnames`{.literal}         | `KEYLIME_AGENT_TLS_ACCEPT_INVALID_HOSTNAMES`{.literal}         | `false`{.literal}                                            | Accept TLS certificates where the hostname does not match the certificate's subject or SAN fields. Must be used only in a testing environment.                                                                                                                                                                                                                                                           |
+--------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 6.10. \[agent\] section

Show more

#### [6.13.8. Logging configuration](#logging_configuration) {#logging-configuration .title}

To customize the logging, you can add configuration drop-in files in the `/etc/keylime/logging.conf.d/`{.literal} directory. These drop-in files keep your custom settings separate from the default configuration to prevent errors during system updates.

+:---------------------+:------------------------------------+:---------------------+
| Configuration option | Environment variable                | Default value        |
+----------------------+-------------------------------------+----------------------+
| `version`{.literal}  | `KEYLIME_LOGGING_VERSION`{.literal} | `2.0`{.literal}      |
+----------------------+-------------------------------------+----------------------+

: Table 6.11. \[logging\] section

Show more

+:---------------------+:-----------------------------------------+:-------------------------+
| Configuration option | Environment variable                     | Default value            |
+----------------------+------------------------------------------+--------------------------+
| `keys`{.literal}     | `KEYLIME_LOGGING_LOGGERS_KEYS`{.literal} | `root,keylime`{.literal} |
+----------------------+------------------------------------------+--------------------------+

: Table 6.12. \[loggers\] section

Show more

+:---------------------+:------------------------------------------+:---------------------------+
| Configuration option | Environment variable                      | Default value              |
+----------------------+-------------------------------------------+----------------------------+
| `keys`{.literal}     | `KEYLIME_LOGGING_HANDLERS_KEYS`{.literal} | `consoleHandler`{.literal} |
+----------------------+-------------------------------------------+----------------------------+

: Table 6.13. \[handlers\] section

Show more

+:---------------------+:--------------------------------------------+:----------------------+
| Configuration option | Environment variable                        | Default value         |
+----------------------+---------------------------------------------+-----------------------+
| `keys`{.literal}     | `KEYLIME_LOGGING_FORMATTERS_KEYS`{.literal} | `formatter`{.literal} |
+----------------------+---------------------------------------------+-----------------------+

: Table 6.14. \[formatters\] section

Show more

+:---------------------+:--------------------------------------------------------+:-----------------------------------------------------------------------------+
| Configuration option | Environment variable                                    | Default value                                                                |
+----------------------+---------------------------------------------------------+------------------------------------------------------------------------------+
| `datefmt`{.literal}  | `KEYLIME_LOGGING_FORMATTER_FORMATTER_DATEFMT`{.literal} | `%Y-%m-%d %H:%M:%S`{.literal}                                                |
+----------------------+---------------------------------------------------------+------------------------------------------------------------------------------+
| `format`{.literal}   | `KEYLIME_LOGGING_FORMATTER_FORMATTER_FORMAT`{.literal}  | `%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s`{.literal} |
+----------------------+---------------------------------------------------------+------------------------------------------------------------------------------+

: Table 6.15. \[formatter_formatter\] section

Show more

+:---------------------+:-------------------------------------------------+:---------------------------+
| Configuration option | Environment variable                             | Default value              |
+----------------------+--------------------------------------------------+----------------------------+
| `handlers`{.literal} | `KEYLIME_LOGGING_LOGGER_ROOT_HANDLERS`{.literal} | `consoleHandler`{.literal} |
+----------------------+--------------------------------------------------+----------------------------+
| `level`{.literal}    | `KEYLIME_LOGGING_LOGGER_ROOT_LEVEL`{.literal}    | `INFO`{.literal}           |
+----------------------+--------------------------------------------------+----------------------------+

: Table 6.16. \[logger_root\] section

Show more

+:----------------------+:-------------------------------------------------------------+:--------------------------+
| Configuration option  | Environment variable                                         | Default value             |
+-----------------------+--------------------------------------------------------------+---------------------------+
| `args`{.literal}      | `KEYLIME_LOGGING_HANDLER_CONSOLEHANDLER_ARGS`{.literal}      | `(sys.stdout,)`{.literal} |
+-----------------------+--------------------------------------------------------------+---------------------------+
| `class`{.literal}     | `KEYLIME_LOGGING_HANDLER_CONSOLEHANDLER_CLASS`{.literal}     | `StreamHandler`{.literal} |
+-----------------------+--------------------------------------------------------------+---------------------------+
| `formatter`{.literal} | `KEYLIME_LOGGING_HANDLER_CONSOLEHANDLER_FORMATTER`{.literal} | `formatter`{.literal}     |
+-----------------------+--------------------------------------------------------------+---------------------------+
| `level`{.literal}     | `KEYLIME_LOGGING_HANDLER_CONSOLEHANDLER_LEVEL`{.literal}     | `INFO`{.literal}          |
+-----------------------+--------------------------------------------------------------+---------------------------+

: Table 6.17. \[handler_consoleHandler\] section

Show more

+:---------------------+:----------------------------------------------------+:---------------------+
| Configuration option | Environment variable                                | Default value        |
+----------------------+-----------------------------------------------------+----------------------+
| `handlers`{.literal} | `KEYLIME_LOGGING_LOGGER_KEYLIME_HANDLERS`{.literal} |                      |
+----------------------+-----------------------------------------------------+----------------------+
| `level`{.literal}    | `KEYLIME_LOGGING_LOGGER_KEYLIME_LEVEL`{.literal}    | `INFO`{.literal}     |
+----------------------+-----------------------------------------------------+----------------------+
| `qualname`{.literal} | `KEYLIME_LOGGING_LOGGER_KEYLIME_QUALNAME`{.literal} | `keylime`{.literal}  |
+----------------------+-----------------------------------------------------+----------------------+

: Table 6.18. \[logger_keylime\] section

Show more

## [Chapter 7. Checking integrity with AIDE](#checking-integrity-with-aide) {#chapter-7.-checking-integrity-with-aide .title}

Use the Advanced Intrusion Detection Environment (AIDE) utility in RHEL to create a file database and check system file integrity. This capability helps detect intrusions by reporting unauthorized changes.

### [7.1. Installing AIDE](#installing-aide) {#installing-aide .title}

To start file-integrity checking with AIDE, you must install the corresponding package and initiate the AIDE database.

**Prerequisites**

-   The `AppStream`{.literal} repository is enabled.

**Procedure**

1.  Install the `aide`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install aide
    ```

2.  Generate an initial database:

    ``` {.language-plaintext tabindex="-1"}
    # aide --init
    Start timestamp: 2024-07-08 10:39:23 -0400 (AIDE 0.16)
    AIDE initialized database at /var/lib/aide/aide.db.new.gz

    Number of entries:  55856

    ---------------------------------------------------
    The attributes of the (uncompressed) database(s):
    ---------------------------------------------------

    /var/lib/aide/aide.db.new.gz
    …
      SHA512   : mZaWoGzL2m6ZcyyZ/AXTIowliEXWSZqx
                 IFYImY4f7id4u+Bq8WeuSE2jasZur/A4
                 FPBFaBkoCFHdoE/FW/V94Q==
    ```

3.  Optional: In the default configuration, the `aide --init`{.literal} command checks just a set of directories and files defined in the `/etc/aide.conf`{.literal} file. To include additional directories or files in the AIDE database, and to change their watched parameters, edit `/etc/aide.conf`{.literal} accordingly.

4.  To start using the database, remove the `.new`{.literal} substring from the initial database file name:

    ``` {.language-plaintext tabindex="-1"}
    # mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
    ```

5.  Optional: To change the location of the AIDE database, edit the `/etc/aide.conf`{.literal} file and modify the `DBDIR`{.literal} value. For additional security, store the database, configuration, and the `/usr/sbin/aide`{.literal} binary file in a secure location such as a read-only media.

### [7.2. Performing integrity checks with AIDE](#performing-integrity-checks-with-aide) {#performing-integrity-checks-with-aide .title}

Use Advanced Intrusion Detection Environment (AIDE) to perform file-integrity checks by comparing the current file state against its internal database. This check produces a report detailing changes since the last run. You can use the `crond`{.literal} service to schedule regular checks with AIDE.

**Prerequisites**

-   AIDE is properly installed and its database is initialized. See [Installing AIDE](#installing-aide "7.1. Installing AIDE")

**Procedure**

1.  To initiate a manual check:

    ``` {.language-plaintext tabindex="-1"}
    # aide --check
    Start timestamp: 2024-07-08 10:43:46 -0400 (AIDE 0.16)
    AIDE found differences between database and file system!!

    Summary:
      Total number of entries:  55856
      Added entries:        0
      Removed entries:      0
      Changed entries:      1

    ---------------------------------------------------
    Changed entries:
    ---------------------------------------------------

    f   ...      ..S : /root/.viminfo

    ---------------------------------------------------
    Detailed information about changes:
    ---------------------------------------------------

    File: /root/.viminfo
      SELinux  : system_u:object_r:admin_home_t:s | unconfined_u:object_r:admin_home
                 0                                | _t:s0
    …
    ```

2.  At a minimum, configure the system to run AIDE weekly. Optimally, run AIDE daily. For example, to schedule a daily execution of AIDE at *04:05* a.m. by using the `cron`{.literal} command, add the following line to the `/etc/crontab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
     05 4 * * * root /usr/sbin/aide --check
    ```

    See the `cron(8)`{.literal} man page on your system for details on the `crond`{.literal} scheduling daemon.

### [7.3. Updating an AIDE database](#updating-an-aide-database) {#updating-an-aide-database .title}

Update the AIDE database after making legitimate system changes, such as installing a software update. This action prevents false positives during subsequent integrity checks.

**Prerequisites**

-   AIDE is properly installed and its database is initialized. See [Installing AIDE](#installing-aide "7.1. Installing AIDE")

**Procedure**

1.  Update your baseline AIDE database:

    ``` {.language-plaintext tabindex="-1"}
    # aide --update
    ```

    The `aide --update`{.literal} command creates the `/var/lib/aide/aide.db.new.gz`{.literal} database file.

2.  To start using the updated database for integrity checks, remove the `.new`{.literal} substring from the file name.

### [7.4. File-integrity tools: AIDE and IMA](#file-integrity-tools-aide-and-ima) {#file-integrity-tools-aide-and-ima .title}

Compare file integrity tools, AIDE and Integrity Measurement Architecture (IMA), to select the one that best fits your scenario. This helps you decide on the appropriate method for checking and preserving file integrity.

+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Question  | Advanced Intrusion Detection Environment (AIDE)                                                                                                                    | Integrity Measurement Architecture (IMA)                                                                                       |
+:==========+:===================================================================================================================================================================+:===============================================================================================================================+
| What      | AIDE is a utility that creates a database of files and directories on the system. This database serves for checking file integrity and detect intrusion detection. | IMA detects if a file is altered by checking file measurement (hash values) compared to previously stored extended attributes. |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| How       | AIDE uses rules to compare the integrity state of the files and directories.                                                                                       | IMA uses file hash values to detect the intrusion.                                                                             |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Why       | Detection - AIDE detects if a file is modified by verifying the rules.                                                                                             | Detection and Prevention - IMA detects and prevents an attack by replacing the extended attribute of a file.                   |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Usage     | AIDE detects a threat when the file or directory is modified.                                                                                                      | IMA detects a threat when someone tries to alter the entire file.                                                              |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Extension | AIDE checks the integrity of files and directories on the local system.                                                                                            | IMA ensures security on the local and remote systems.                                                                          |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

: Table 7.1. Comparison between AIDE and IMA

Show more

### [7.5. Configuring file integrity checks with the aide RHEL system role](#configuring-file-integrity-checks-with-the-aide-rhel-system-role) {#configuring-file-integrity-checks-with-the-aide-rhel-system-role .title}

You can configure Advanced Intrusion Detection Environment (AIDE) consistently across multiple systems by using the `aide`{.literal} RHEL system role. The role automatically installs the `aide`{.literal} package on all managed nodes.

Depending on your configuration, the `aide`{.literal} role can perform the following actions:

-   Initialize the AIDE database and store it on the control node
-   Run AIDE integrity checks on the managed nodes
-   Update the AIDE database and store it on the control node

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configure system integrity
      hosts: managed-node-01.example.com
      tasks:
        - name: Configure file integrity checks with AIDE
          ansible.builtin.include_role:
            name: rhel-system-roles.aide.aide
          vars:
            aide_db_fetch_dir: files
            aide_init: true
            aide_check: false
            aide_update: false
            aide_cron_check: true
            aide_cron_interval: 0 12 * * *
    ```

    The settings specified in the example playbook include the following:

    `aide_db_fetch_dir: files`{.literal}
    :   Specifies the directory on the Ansible Control Node (ACN) for storing the AIDE database fetched from the remote nodes. With the default `files`{.literal} value, the role stores the database in the same directory as the playbook. To store the database files somewhere else, specify a different path.

    `aide_check: false`{.literal}
    :   Runs an integrity check on the remote nodes.

    `aide_update: false`{.literal}
    :   Updates the AIDE database and stores it on the control node.

    `aide_cron_check: true`{.literal}
    :   Configures a periodic `cron`{.literal} job that activates AIDE integrity checks on the managed nodes.

    `aide_cron_interval: 0 12 * * *`{.literal}

    :   Sets the interval for the `cron`{.literal} job in the format *`<minute> <hour> <day_of_month> <month> <day of week>`{.literal}*. The value `0 12 * * *`{.literal} sets it to run every day at noon.

        For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.aide/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

### [7.6. Additional resources](#checking-integrity-with-aide_76-additional-resources) {#additional-resources-2 .title}

-   [Enhancing security with the kernel integrity subsystem](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/enhancing-security-with-the-kernel-integrity-subsystem)

## [Chapter 8. Managing sudo access](#managing-sudo-access) {#chapter-8.-managing-sudo-access .title}

Manage `sudo`{.literal} access to allow non-root users to securely use administrative commands without logging into the root account. Proper configuration helps control privileges and limits exposure.

### [8.1. User authorizations in sudoers](#user-authorizations-in-sudoers) {#user-authorizations-in-sudoers .title}

In RHEL, the `/etc/sudoers`{.literal} file and the `/etc/sudoers.d/`{.literal} directory store user and group authorizations for the `sudo`{.literal} command. You can use these configurations to specify which users can enter administrative commands on specific hosts.

You can apply rules to individual users and user groups. To simplify configurations for groups of hosts, commands, and users, you can use aliases. The `/etc/sudoers`{.literal} file defines default aliases in the first section.

When a user enters a command with `sudo`{.literal} for which the user does not have authorization, the system records a message that contains the string *`<username>`{.literal}*` : user NOT in sudoers`{.literal} to the journal log.

The default `/etc/sudoers`{.literal} file provides information and examples of authorizations. You can activate a specific example rule by uncommenting the corresponding line. The section with user authorizations is marked with the following introduction:

``` {.language-plaintext tabindex="-1"}
## Next comes the main part: which users can run what software on
## which machines  (the sudoers file can be shared between multiple
## systems).
```

You can create new `sudoers`{.literal} authorizations and modify existing authorizations by using the following format:

``` {.language-plaintext tabindex="-1"}
<username> <hostname.example.com>=(<run_as_user>:<run_as_group>) <path/to/command>
```

Where:

-   *`<username>`{.literal}* is the user that enters the command, for example, `user1`{.literal}. If the value starts with `%`{.literal}, it defines a group, for example, `%group1`{.literal}.
-   *`<hostname.example.com>`{.literal}* is the name of the host on which the rule applies.
-   The section `(`{.literal}*`<run_as_user>`{.literal}*`:`{.literal}*`<run_as_group>`{.literal}*`)`{.literal} defines the user or group as which the command is executed. If you omit this section, *`<username>`{.literal}* can use the command as root.
-   *`<path/to/command>`{.literal}* is the complete absolute path to the command. You can also limit the user to only performing a command with specific options and arguments by adding those options after the command path. If you do not specify any options, the user can use the command with all options.

You can apply the rule to all users, hosts, or commands by replacing any of these variables with `ALL`{.literal}.

Warning

With overly permissive rules, such as `ALL ALL=(ALL) ALL`{.literal}, all users can run all commands as all users on all hosts. This presents serious security risks.

You can specify the arguments negatively by using the `!`{.literal} operator. For example, `!root`{.literal} specifies all users except root. Note that allowing specific users, groups, and commands is more secure than disallowing specific users, groups, and commands. This is because allow rules also block new unauthorized users or groups.

Warning

Avoid using negative rules for commands because users can overcome such rules by renaming commands with the `alias`{.literal} command.

The system reads the `/etc/sudoers`{.literal} file from beginning to end. Therefore, if the file contains multiple entries for a user, the entries are applied in order. In case of conflicting values, the system uses the last match, even if it is not the most specific match.

To preserve the rules during system updates and for easier fixing of errors, enter new rules by creating new files in the `/etc/sudoers.d/`{.literal} directory. Do not enter rules directly to the `/etc/sudoers`{.literal} file. The system reads the files in the `/etc/sudoers.d`{.literal} directory when it reaches the following line in the `/etc/sudoers`{.literal} file:

``` {.language-plaintext tabindex="-1"}
#includedir /etc/sudoers.d
```

Note that the number sign (`#`{.literal}) at the beginning of this line is part of the syntax and does not mean the line is a comment. The names of files in that directory must not contain a period and must not end with a tilde (`~`{.literal}).

For more information, see the `sudo(8)`{.literal} and `sudoers(5)`{.literal} man pages on your system.

### [8.2. Granting sudo access to a user](#granting-sudo-access-to-a-user) {#granting-sudo-access-to-a-user .title}

In RHEL, you can allow non-root users to enter administrative commands by granting them `sudo`{.literal} access. This ensures that users can perform privileged tasks securely without requiring the root user's password.

When users need to perform an administrative command, they can precede that command with `sudo`{.literal}. If the user has authorization for the command, the command is executed as if they were root.

Be aware of the following limitations:

-   Only users listed in the `/etc/sudoers`{.literal} configuration file can use the `sudo`{.literal} command.
-   The command is executed in the shell of the user, not in the root shell. However, there are some exceptions such as when full `sudo`{.literal} privileges are granted to any user. In such cases, users can switch to and run the commands in root shell. For example:
-   `sudo -i`{.literal}
-   `sudo su -`{.literal}

**Prerequisites**

-   You have root access to the system.

**Procedure**

1.  As root, open the `/etc/sudoers`{.literal} file.

    ``` {.language-plaintext tabindex="-1"}
    # visudo
    ```

    The `/etc/sudoers`{.literal} file defines the policies applied by the `sudo`{.literal} command.

2.  In the `/etc/sudoers`{.literal} file, find the lines that grant `sudo`{.literal} access to users in the administrative `wheel`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    ## Allows people in group wheel to run all commands
    %wheel        ALL=(ALL)       ALL
    ```

3.  Ensure the line that starts with `%wheel`{.literal} is not commented out with the number sign (`#`{.literal}).

4.  Save any changes, and exit the editor.

5.  Add users you want to grant `sudo`{.literal} access to into the administrative `wheel`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
     # usermod --append -G wheel <username>
    ```

    Replace *`<username>`{.literal}* with the name of the user.

**Verification**

-   Verify that the user is in the administrative `wheel`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    # id <username>
    uid=5000(<username>) gid=5000(<username>) groups=5000(<username>),10(wheel)
    ```

### [8.3. Enabling unprivileged users to run certain commands](#enabling-unprivileged-users-to-run-certain-commands) {#enabling-unprivileged-users-to-run-certain-commands .title}

As an administrator, you can allow unprivileged users to enter certain commands on specific workstations by configuring a policy in the `/etc/sudoers.d/`{.literal} directory. This helps improve security compared to granting full `sudo`{.literal} access.

Specifying a policy allowing only certain commands is more secure than granting full `sudo`{.literal} access to a user or giving someone the root password for the following reasons:

-   More granular control over privileged actions. You can allow a user to perform certain actions on specific hosts instead of giving them full administrative access.
-   Better logging. When a user performs an action with `sudo`{.literal}, the action is logged with their user name, not just root.
-   Transparent control. You can set email notifications whenever a user attempts to use `sudo`{.literal} privileges.

For additional details and examples, see the `sudoers(5)`{.literal} man pages on your system.

**Prerequisites**

-   You have root access to the system.

**Procedure**

1.  As root, create a new `sudoers.d/`{.literal} directory under `/etc/`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /etc/sudoers.d/
    ```

2.  Create a new file in the `/etc/sudoers.d/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # visudo -f /etc/sudoers.d/<filename>
    ```

    The file opens automatically.

3.  Add the following line to the `/etc/sudoers.d/`{.literal}*`<filename>`{.literal}* file:

    ``` {.language-plaintext tabindex="-1"}
    <username> <hostname.example.com> = (<run_as_user>:<run_as_group>) <path/to/command>
    ```

    -   Replace *`<username>`{.literal}* with the name of the user.

    -   Replace *`<hostname.example.com>`{.literal}* with the URL of the host.

    -   Replace `(`{.literal}*`<run_as_user>`{.literal}*`:`{.literal}*`<run_as_group>`{.literal}*`)`{.literal} with the user or group as which the command can be run. If you omit this section, *`<username>`{.literal}* can run the command as root.

    -   Replace *`<path/to/command>`{.literal}* with the complete absolute path to the command. You can also limit the user to only performing a command with specific options and arguments by adding those options after the command path. If you do not specify any options, the user can use the command with all options.

    -   To allow two and more commands on the same host on one line, you can list them separated by a comma followed by a space.

        For example, to allow `user1`{.literal} to run the `dnf`{.literal} and `reboot`{.literal} commands on `host1.example.com`{.literal}, enter `user1 host1.example.com = /bin/dnf, /sbin/reboot`{.literal}.

4.  Optional: To receive email notifications every time the user attempts to use `sudo`{.literal} privileges, add the following lines to the file:

    ``` {.language-plaintext tabindex="-1"}
    Defaults    mail_always
    Defaults    mailto="<email@example.com>"
    ```

5.  Save the changes, and exit the editor.

**Verification**

1.  To verify if a user can run a command with `sudo`{.literal} privileges, switch the account:

    ``` {.language-plaintext tabindex="-1"}
    # su <username> -
    ```

2.  As the user, enter the command with the `sudo`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo <command>
    [sudo] password for <username>:
    ```

    Enter the user's `sudo`{.literal} password.

3.  If the privileges are configured correctly, the system displays the list of commands and options. For example, with the `dnf`{.literal} command, it shows the following output:

    ``` {.language-plaintext tabindex="-1"}
    …
    usage: dnf [options] COMMAND
    …
    ```

    If the system returns the error message *`<username>`{.literal}*` is not in the sudoers file. This incident will be reported`{.literal}, the file for *`<username>`{.literal}* in `/etc/sudoers.d/`{.literal} does not exist.

    If the system returns the error message *`<username>`{.literal}*` is not allowed to run sudo on `{.literal}*`<host.example.com>`{.literal}*, the configuration was not completed correctly. Ensure that you are logged in as root and that the configuration was performed correctly.

    If the system returns the error message `Sorry, user `{.literal}*`<username>`{.literal}*` is not allowed to execute '`{.literal}*`<path/to/command>`{.literal}*`' as root on `{.literal}*`<host.example.com>`{.literal}*`.`{.literal}, the command is not correctly defined in the rule for the user.

### [8.4. Applying custom sudoers configuration by using RHEL system roles](#applying-custom-sudoers-configuration-by-using-rhel-system-roles) {#applying-custom-sudoers-configuration-by-using-rhel-system-roles .title}

You can use the `sudo`{.literal} RHEL system role to apply custom `sudoers`{.literal} configuration on your managed nodes. That way, you can define which users can run which commands on which hosts, with better configuration efficiency and more granular control.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: "Configure sudo"
      hosts: managed-node-01.example.com
      tasks:
        - name: "Apply custom /etc/sudoers configuration"
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.sudo
          vars:
            sudo_sudoers_files:
              - path: "/etc/sudoers"
                user_specifications:
                  - users:
                      - <user_name>
                    hosts:
                      - <host_name>
                    commands:
                      - <path_to_command_binary>
    ```

    The settings specified in the playbook include the following:

    `users`{.literal}
    :   The list of users that the rule applies to.

    `hosts`{.literal}
    :   The list of hosts that the rule applies to. You can use `ALL`{.literal} for all hosts.

    `commands`{.literal}
    :   The list of commands that the rule applies to. You can use `ALL`{.literal} for all commands.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.sudo/README.md`{.literal} file on the control node.

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

1.  On the managed node, verify that the playbook applied the new rules.

    ``` {.language-plaintext tabindex="-1"}
    # cat /etc/sudoers | tail -n1
    <user_name> <host_name>= <path_to_command_binary>
    ```

## [Chapter 9. Configuring automated unlocking of encrypted volumes by using policy-based decryption](#configuring-automated-unlocking-of-encrypted-volumes-by-using-policy-based-decryption) {#chapter-9.-configuring-automated-unlocking-of-encrypted-volumes-by-using-policy-based-decryption .title}

Policy-Based Decryption (PBD) enables unlocking encrypted root and secondary storage volumes on physical and virtual machines. PBD uses a variety of unlocking methods, such as user passwords, Trusted Platform Module (TPM) devices, PKCS #11 devices, or a network server.

PBD allows combining different unlocking methods into a policy, which makes it possible to unlock the same volume in different ways. The current implementation of the PBD in Red Hat Enterprise Linux consists of the Clevis framework and plugins called *pins*. Each pin provides a separate unlocking capability. Currently, the following pins are available:

`tang`{.literal}
:   Allows unlocking volumes by using a network server.

`tpm2`{.literal}
:   Allows unlocking volumes by using a TPM2 policy.

`pkcs11`{.literal}
:   Allows unlocking volumes by using a PKCS #11 URI.

`trustee`{.literal}
:   Allows unlocking volumes by using a Trustee Key Broker Service (KBS) server.

`sss`{.literal}
:   Allows deploying high-availability systems by using the Shamir's Secret Sharing (SSS) cryptographic scheme.

### [9.1. Network-bound disk encryption](#network-bound-disk-encryption) {#network-bound-disk-encryption .title}

The Network-bound Disc Encryption (NBDE) is a subcategory of Policy-Based Decryption (PBD) that allows binding encrypted volumes to a special network server. The current implementation of the NBDE includes a Clevis pin for the Tang server and the Tang server itself.

Clevis and Tang are generic client and server components that provide network-bound encryption. In RHEL, they are used in conjunction with LUKS to encrypt and decrypt root and non-root storage volumes, thereby accomplishing Network-bound Disk Encryption.

#### [9.1.1. NBDE components](#nbde_components) {#nbde-components .title}

In RHEL, NBDE is implemented through the following components and technologies:

**Figure 9.1. NBDE scheme when using a LUKS1-encrypted volume. LUKSmeta is not used for LUKS2 volumes.**

Tang
:   Tang is a server for binding data to network presence. It makes a system containing your data available when the system is bound to a certain secure network. Tang is stateless and does not require TLS or authentication. Unlike escrow-based solutions, where the server stores all encryption keys and has knowledge of every key ever used, Tang never interacts with any client keys. Therefore, it never gains any identifying information from the client.

Clevis
:   Clevis is a pluggable framework for automated decryption. In NBDE, Clevis provides automated unlocking of LUKS volumes. The `clevis`{.literal} package provides the client side of the feature.

Clevis pin
:   A Clevis pin is a plugin into the Clevis framework. One of such pins is a plugin that implements interactions with the NBDE server - Tang.

José
:   Both client- and server-side components use the José library to perform encryption and decryption operations.

LUKSMeta

:   The LUKS version 2 (LUKS2) is the default disk-encryption format in RHEL. Therefore, the provisioning state for NBDE is stored as a token in a LUKS2 header. The leveraging of provisioning state for NBDE by the `luksmeta`{.literal} package is used only for volumes encrypted with LUKS1.

    The Clevis pin for Tang supports both LUKS1 and LUKS2 without requiring specification. Clevis can encrypt plain text files but you have to use the `cryptsetup`{.literal} tool for encrypting block devices.

#### [9.1.2. NBDE principles](#nbde_principles) {#nbde-principles .title}

When you begin provisioning NBDE, the Clevis pin for Tang server gets a list of the Tang server's advertised asymmetric keys. Alternatively, since the keys are asymmetric, a list of Tang's public keys can be distributed out of band so that clients can operate without access to the Tang server. This mode is called *offline provisioning*.

The Clevis pin for Tang uses one of the public keys to generate a unique, cryptographically strong encryption key. Once the data is encrypted by using this key, the key is discarded. The Clevis client should store the state produced by this provisioning operation in a convenient location. This process of encrypting data is the *provisioning step*.

When the client is ready to access its data, it loads the metadata produced in the provisioning step, and it responds to recover the encryption key. This process is the *recovery step*.

In NBDE, Clevis binds a LUKS volume by using a pin so that it can be automatically unlocked. After successful completion of the binding process, the disk can be unlocked using the provided Dracut unlocker.

For more information, see the `tang(8)`{.literal}, `clevis(1)`{.literal}, `jose(1)`{.literal}, and `clevis-luks-unlockers(7)`{.literal} man pages on your system.

Note

If the `kdump`{.literal} kernel crash dumping mechanism is set to save the content of the system memory to a LUKS-encrypted device, you are prompted for a password. This happens during the second kernel boot.

**Additional resources**

-   [NBDE (Network-Bound Disk Encryption) Technology (Red Hat Knowledgebase)](https://access.redhat.com/articles/6987053)
-   [How to configure Network-Bound Disk Encryption with multiple LUKS devices (Clevis + Tang unlocking) (Red Hat Knowledgebase)](https://access.redhat.com/articles/4500491)

### [9.2. Deploying a Tang server](#deploying-a-tang-server) {#deploying-a-tang-server .title}

You can use a Tang server to unlock LUKS-encrypted volumes on Clevis-enabled clients automatically. In the minimalist scenario, you deploy a Tang server by installing its package and entering a single command.

**Prerequisites**

-   Commands that start with the `#`{.literal} command prompt require administrative privileges provided by `sudo`{.literal} or root user access. For information on how to configure `sudo`{.literal} access, see [Enabling unprivileged users to run certain commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access#enabling-unprivileged-users-to-run-certain-commands).

**Procedure**

1.  Install the `tang`{.literal} package and its dependencies:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tang
    ```

2.  Start and enable the `tangd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable tangd.socket --now
    ```

    Because `tangd`{.literal} uses the `systemd`{.literal} socket activation mechanism, the server starts as soon as the first connection comes in. A new set of cryptographic keys is automatically generated at the first start. To perform cryptographic operations such as manual key generation, use the `jose`{.literal} utility as described in the `jose(1)`{.literal} man page on your system.

**Verification**

-   On your NBDE client, verify that your Tang server works correctly by using the following command. The command must return the identical message you pass for encryption and decryption:

    ``` {.language-plaintext tabindex="-1"}
    # echo test | clevis encrypt tang '{"url":"<tang.server.example.com:80>"}' -y | clevis decrypt
    test
    ```

**Next steps**

-   For deployments on a different port than 80, see [Deploying a Tang server with SELinux in enforcing mode](#deploying-a-tang-server-with-selinux-in-enforcing-mode "9.3. Deploying a Tang server with SELinux in enforcing mode").

### [9.3. Deploying a Tang server with SELinux in enforcing mode](#deploying-a-tang-server-with-selinux-in-enforcing-mode) {#deploying-a-tang-server-with-selinux-in-enforcing-mode .title}

A different service on your server might occupy port 80, which the Tang server uses by default. In this case, you can deploy Tang on a custom port. Ideally, run it as a confined service in SELinux enforcing mode.

**Prerequisites**

-   The `policycoreutils-python-utils`{.literal} package and its dependencies are installed.
-   The `firewalld`{.literal} service is running.

**Procedure**

1.  To install the `tang`{.literal} package and its dependencies, enter the following command as `root`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tang
    ```

2.  Pick an unoccupied port, for example, *7500/tcp*, and allow the `tangd`{.literal} service to bind to that port:

    ``` {.language-plaintext tabindex="-1"}
    # semanage port -a -t tangd_port_t -p tcp 7500
    ```

    Note that a port can be used only by one service at a time.

3.  Open the port in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-port=7500/tcp
    # firewall-cmd --runtime-to-permanent
    ```

4.  Enable the `tangd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable tangd.socket
    ```

5.  Create an override file:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl edit tangd.socket
    ```

6.  An editor screen opens with an empty `override.conf`{.literal} file located in the `/etc/systemd/system/tangd.socket.d/`{.literal} directory. Change the default port for the Tang server from 80 to the previously picked number. Insert the following code snippet between the lines starting with `# Anything between here`{.literal} and `# Lines below this`{.literal}. Otherwise, the system discards your changes:

    ``` {.language-plaintext tabindex="-1"}
    [Socket]
    ListenStream=
    ListenStream=7500
    ```

7.  Save the changes and exit the editor. In the default `vi`{.literal} editor, you can do that by pressing Esc to switch into command mode, entering `:wq`{.literal}, and pressing Enter.

8.  Reload the changed configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

9.  Check that your configuration is working:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl show tangd.socket -p Listen
    Listen=[::]:7500 (Stream)
    ```

10. Start the `tangd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart tangd.socket
    ```

    Because `tangd`{.literal} uses the `systemd`{.literal} socket activation mechanism, the server starts as soon as the first connection comes in. A new set of cryptographic keys is automatically generated at the first start. To perform cryptographic operations such as manual key generation, use the `jose`{.literal} utility as described in the `jose(1)`{.literal} man page on your system.

**Verification**

-   On your NBDE client, verify that your Tang server works correctly by using the following command. The command must return the identical message you pass for encryption and decryption:

    ``` {.language-plaintext tabindex="-1"}
    # echo test | clevis encrypt tang '{"url":"<tang.server.example.com:7500>"}' -y | clevis decrypt
    test
    ```

### [9.4. Rotating Tang server keys and updating bindings on clients](#rotating-tang-server-keys-and-updating-bindings-on-clients) {#rotating-tang-server-keys-and-updating-bindings-on-clients .title}

For security reasons, rotate your Tang server keys and update existing bindings on clients periodically. The precise interval at which you should rotate them depends on your application, key sizes, and institutional policy.

Warning

Removing the old keys while clients are still using them can result in data loss. If you accidentally remove such keys, use the `clevis luks regen`{.literal} command on the clients, and provide your LUKS password manually.

**Prerequisites**

-   A Tang server is running.
-   The `clevis`{.literal} and `clevis-luks`{.literal} packages are installed on your clients.

**Procedure**

1.  Rename all keys in the `/var/db/tang`{.literal} key database directory to have a leading `.`{.literal} to hide them from advertisement. Note that the file names in the following example differs from unique file names in the key database directory of your Tang server:

    ``` {.language-plaintext tabindex="-1"}
    # cd /var/db/tang
    # ls -l
    -rw-r--r--. 1 root root 349 Feb  7 14:55 UV6dqXSwe1bRKG3KbJmdiR020hY.jwk
    -rw-r--r--. 1 root root 354 Feb  7 14:55 y9hxLTQSiSB5jSEGWnjhY8fDTJU.jwk
    # mv UV6dqXSwe1bRKG3KbJmdiR020hY.jwk .UV6dqXSwe1bRKG3KbJmdiR020hY.jwk
    # mv y9hxLTQSiSB5jSEGWnjhY8fDTJU.jwk .y9hxLTQSiSB5jSEGWnjhY8fDTJU.jwk
    ```

2.  Check that you renamed and therefore hid all keys from the Tang server advertisement:

    ``` {.language-plaintext tabindex="-1"}
    # ls -l
    total 0
    ```

3.  Generate new keys using the `/usr/libexec/tangd-keygen`{.literal} command in `/var/db/tang`{.literal} on the Tang server:

    ``` {.language-plaintext tabindex="-1"}
    # /usr/libexec/tangd-keygen /var/db/tang
    # ls /var/db/tang
    3ZWS6-cDrCG61UPJS2BMmPU4I54.jwk zyLuX6hijUy_PSeUEFDi7hi38.jwk
    ```

4.  Check that your Tang server advertises the signing key from the new key pair, for example:

    ``` {.language-plaintext tabindex="-1"}
    # tang-show-keys 7500
    3ZWS6-cDrCG61UPJS2BMmPU4I54
    ```

5.  On your NBDE clients, use the `clevis luks report`{.literal} command to check if the keys advertised by the Tang server remains the same. You can identify slots with the relevant binding using the `clevis luks list`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks list -d /dev/sda2
    1: tang '{"url":"http://tang.srv"}'
    # clevis luks report -d /dev/sda2 -s 1
    ...
    Report detected that some keys were rotated.
    Do you want to regenerate luks metadata with "clevis luks regen -d /dev/sda2 -s 1"? [ynYN]
    ```

6.  To regenerate LUKS metadata for the new keys, either press `y`{.literal} to the prompt of the previous command or use the `clevis luks regen`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks regen -d /dev/sda2 -s 1
    ```

7.  When you are sure that all old clients use the new keys, you can remove the old keys from the Tang server, for example:

    ``` {.language-plaintext tabindex="-1"}
    # cd /var/db/tang
    # rm .*.jwk
    ```

**Next steps**

Alternatively, you can rotate Tang keys by using the `nbde_server`{.literal} RHEL system role. See [Using the nbde_server system role for setting up multiple Tang servers](#using-the-nbde-server-rhel-system-role-for-setting-up-multiple-tang-servers "9.19.1. Using the nbde_server RHEL system role for setting up multiple Tang servers") for more information.

### [9.5. Configuring automated unlocking by using a Tang key in the web console](#configuring-automated-unlocking-by-using-a-tang-key-in-the-web-console) {#configuring-automated-unlocking-by-using-a-tang-key-in-the-web-console .title}

You can configure automated unlocking of a LUKS-encrypted storage device by using a key provided by a Tang server in the RHEL web console GUI.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   The `cockpit-storaged`{.literal} and `clevis-luks`{.literal} packages are installed on your system.

-   The `cockpit.socket`{.literal} service is running at port 9090.

-   A Tang server is available. See [Deploying a Tang server with SELinux in enforcing mode](#deploying-a-tang-server-with-selinux-in-enforcing-mode "9.3. Deploying a Tang server with SELinux in enforcing mode") for details.

-   You have `root`{.literal} privileges or permissions to enter administrative commands with `sudo`{.literal}.

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Switch to administrative access, provide your credentials, and click Storage. In the **Storage** table, click the disk that contains an encrypted volume you plan to add to unlock automatically.

3.  In the following page with details of the selected disk, click + in the **Keys** section to add a Tang key:

4.  Select `Tang keyserver`{.literal} as `Key source`{.literal}, provide the address of your Tang server, and a password that unlocks the LUKS-encrypted device. Click Add to confirm.

    The following dialog window provides a command to verify that the key hash matches.

5.  On the Tang server, use the `tang-show-keys`{.literal} command to display the key hash for comparison. In this example, the Tang server is running on the port *7500*:

    ``` {.language-plaintext tabindex="-1"}
    # tang-show-keys 7500
    x100_1k6GPiDOaMlL3WbpCjHOy9ul1bSfdhI3M08wO0
    ```

6.  Click Trust key when the key hashes in the web console and in the output of previously listed commands are the same.

**Next steps**

-   After you select an encrypted root file system and a Tang server, you can skip several manual steps. You do not need to add the `rd.neednet=1`{.literal} parameter to the kernel command line, install the `clevis-dracut`{.literal} package, or regenerate an initial RAM disk (`initrd`{.literal}). For non-root file systems, the web console enables the `remote-cryptsetup.target`{.literal} and `clevis-luks-akspass.path`{.literal} systemd units. It also installs the `clevis-systemd`{.literal} package and adds the `_netdev`{.literal} parameter to the `fstab`{.literal} and `crypttab`{.literal} configuration files.

**Verification**

1.  In the **Storage** table in the RHEL web console, check that the newly added Tang key is now listed in the **Keys** section with the `Keyserver`{.literal} type.

2.  Verify that the bindings are available for the early boot, for example:

    ``` {.language-plaintext tabindex="-1"}
    # lsinitrd | grep clevis-luks
    lrwxrwxrwx   1 root     root           48 Jan  4 02:56 etc/systemd/system/cryptsetup.target.wants/clevis-luks-askpass.path -> /usr/lib/systemd/system/clevis-luks-askpass.path
    …
    ```

**Additional resources**

-   [Getting started with the RHEL web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console)

### [9.6. Basic NBDE and TPM2 encryption-client operations](#basic-nbde-and-tpm2-encryption-client-operations) {#basic-nbde-and-tpm2-encryption-client-operations .title}

You can learn basic functionality provided by Clevis on examples containing plain text files. You can also use them for troubleshooting your NBDE or Clevis+TPM deployments.

The Clevis framework can encrypt plain text files and decrypt both ciphertext in the JSON Web Encryption (JWE) format and LUKS-encrypted block devices. Clevis clients can use either Tang network servers, Trusted Platform Module 2.0 (TPM 2.0) chips, or PKCS #11 devices for cryptographic operations.

Encryption client bound to a Tang server

:   -   To check that a Clevis encryption client binds to a Tang server, use the `clevis encrypt tang`{.literal} subcommand:

    ``` {.language-plaintext tabindex="-1"}
    $ clevis encrypt tang '{"url":"http://tang.srv:port"}' < input-plain.txt > secret.jwe
    The advertisement contains the following signing keys:

    _OsIk0T-E2l6qjfdDiwVmidoZjA

    Do you wish to trust these keys? [ynYN] y
    ```

    Change the *`http://tang.srv:port`{.literal}* URL in the previous example to match the URL of the server where `tang`{.literal} is installed. The *`secret.jwe`{.literal}* output file contains your encrypted ciphertext in the JWE format. This ciphertext is read from the *`input-plain.txt`{.literal}* input file.

    Alternatively, if your configuration requires a noninteractive communication with a Tang server without SSH access, you can download an advertisement and save it to a file:

    ``` {.language-plaintext tabindex="-1"}
    $ curl -sfg http://tang.srv:port/adv -o adv.jws
    ```

    Use the advertisement in the *`adv.jws`{.literal}* file for any following tasks, such as encryption of files or messages:

    ``` {.language-plaintext tabindex="-1"}
    $ echo 'hello' | clevis encrypt tang '{"url":"http://tang.srv:port","adv":"adv.jws"}'
    ```

    -   To decrypt data, use the `clevis decrypt`{.literal} command and provide the ciphertext (JWE):

        ``` {.language-plaintext tabindex="-1"}
        $ clevis decrypt < secret.jwe > output-plain.txt
        ```

    -   The `clevis`{.literal}, `clevis decrypt`{.literal}, and `clevis encrypt tang`{.literal} commands without any arguments show the built-in CLI help, for example:

        ``` {.language-plaintext tabindex="-1"}
        $ clevis encrypt tang
        Usage: clevis encrypt tang CONFIG < PLAINTEXT > JWE
        …
        ```

    -   For more information and examples, see the `clevis-encrypt-tang(1)`{.literal}, `clevis-luks-unlockers(7)`{.literal}, and `clevis(1)`{.literal} man pages on your system.

Encryption client that uses TPM 2.0

:   -   To encrypt by using a TPM 2.0 chip, use the `clevis encrypt tpm2`{.literal} subcommand with the only argument in form of the JSON configuration object:

    ``` {.language-plaintext tabindex="-1"}
    $ clevis encrypt tpm2 '{}' < input-plain.txt > secret.jwe
    ```

    To choose a different hierarchy, hash, and key algorithms, specify configuration properties, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ clevis encrypt tpm2 '{"hash":"sha256","key":"rsa"}' < input-plain.txt > secret.jwe
    ```

    -   To decrypt the data, provide the ciphertext in the JSON Web Encryption (JWE) format:

        ``` {.language-plaintext tabindex="-1"}
        $ clevis decrypt < secret.jwe > output-plain.txt
        ```

    -   The pin also supports sealing data to a Platform Configuration Registers (PCR) state. That way, the data can only be unsealed if the PCR hashes values match the policy used when sealing.

        For example, to seal the data to the PCR with index 0 and 7 for the SHA-256 bank:

        ``` {.language-plaintext tabindex="-1"}
        $ clevis encrypt tpm2 '{"pcr_bank":"sha256","pcr_ids":"0,7"}' < input-plain.txt > secret.jwe
        ```

        Warning

        Hashes in PCRs can be rewritten, causing you to no longer be able to unlock your encrypted volume. For this reason, add a strong passphrase that allows you to unlock the encrypted volume manually even when a value in a PCR changes.

        If the system cannot automatically unlock your encrypted volume after an upgrade of the `shim-x64`{.literal} package, follow the steps in the [Clevis TPM2 no longer decrypts LUKS devices after a restart](https://access.redhat.com/solutions/6175492) Red Hat Knowledgebase solution.

    -   For more information, see the `clevis-encrypt-tpm2(1)`{.literal} and `clevis-luks-bind(1)`{.literal} man pages on your system.

### [9.7. Configuring NBDE clients for automated unlocking of LUKS-encrypted volumes](#configuring-nbde-clients-for-automated-unlocking-of-luks-encrypted-volumes) {#configuring-nbde-clients-for-automated-unlocking-of-luks-encrypted-volumes .title}

With the Clevis framework, you can configure clients for automated unlocking of LUKS-encrypted volumes when a selected Tang server is available. This creates an NBDE (Network-Bound Disk Encryption) deployment.

**Prerequisites**

-   A Tang server is running and available.

**Procedure**

1.  To automatically unlock an existing LUKS-encrypted volume, install the `clevis-luks`{.literal} subpackage:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install clevis-luks
    ```

2.  Identify the LUKS-encrypted volume for PBD. In the following example, the block device is referred as */dev/sda2*:

    ``` {.language-plaintext tabindex="-1"}
    # lsblk
    NAME                                          MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
    sda                                             8:0    0    12G  0 disk
    ├─sda1                                          8:1    0     1G  0 part  /boot
    └─sda2                                          8:2    0    11G  0 part
      └─luks-40e20552-2ade-4954-9d56-565aa7994fb6 253:0    0    11G  0 crypt
        ├─rhel-root                               253:0    0   9.8G  0 lvm   /
        └─rhel-swap                               253:1    0   1.2G  0 lvm   [SWAP]
    ```

3.  Bind the volume to a Tang server using the `clevis luks bind`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks bind -d /dev/sda2 tang '{"url":"http://tang.srv"}'
    The advertisement contains the following signing keys:

    _OsIk0T-E2l6qjfdDiwVmidoZjA

    Do you wish to trust these keys? [ynYN] y
    You are about to initialize a LUKS device for metadata storage.
    Attempting to initialize it may result in data loss if data was
    already written into the LUKS header gap in a different format.
    A backup is advised before initialization is performed.

    Do you wish to initialize /dev/sda2? [yn] y
    Enter existing LUKS password:
    ```

    This command performs four steps:

    a.  Creates a new key with the same entropy as the LUKS master key.
    b.  Encrypts the new key with Clevis.
    c.  Stores the Clevis JWE object in the LUKS2 header token or uses LUKSMeta if the non-default LUKS1 header is used.
    d.  Enables the new key for use with LUKS.

    Note

    The binding procedure assumes that the header contains at least one free LUKS password slot. The `clevis luks bind`{.literal} command takes one of the slots.

    Now, you can unlock the volume with your existing password as well as with the Clevis policy.

4.  To enable the early boot system to process the disk binding, use the `dracut`{.literal} tool on an already installed system. In RHEL, Clevis produces a generic `initrd`{.literal} (initial RAM disk) without host-specific configuration options and does not automatically add parameters such as `rd.neednet=1`{.literal} to the kernel command line. If your configuration relies on a Tang pin that requires network during early boot, use the `--hostonly-cmdline`{.literal} argument and `dracut`{.literal} adds `rd.neednet=1`{.literal} when it detects a Tang binding:

    a.  Install the `clevis-dracut`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install clevis-dracut
        ```

    b.  Regenerate the initial RAM disk:

        ``` {.language-plaintext tabindex="-1"}
        # dracut -fv --regenerate-all --hostonly-cmdline
        ```

    c.  Alternatively, create a .conf file in the `/etc/dracut.conf.d/`{.literal} directory, and add the `hostonly_cmdline=yes`{.literal} option to the file. Then, you can use `dracut`{.literal} without `--hostonly-cmdline`{.literal}, for example:

        ``` {.language-plaintext tabindex="-1"}
        # echo "hostonly_cmdline=yes" > /etc/dracut.conf.d/clevis.conf
        # dracut -fv --regenerate-all
        ```

    d.  If your scenario requires that networking for a Tang pin is available during early boot, use the `grubby`{.literal} tool on the system where Clevis is installed:

        ``` {.language-plaintext tabindex="-1"}
        # grubby --update-kernel=ALL --args="rd.neednet=1"
        ```

**Verification**

1.  Verify that the Clevis JWE object is successfully placed in a LUKS header:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks list -d /dev/sda2
    1: tang '{"url":"http://tang.srv:port"}'
    ```

2.  Check that the bindings are available for the early boot, for example:

    ``` {.language-plaintext tabindex="-1"}
    # lsinitrd | grep clevis-luks
    lrwxrwxrwx   1 root     root           48 Jan  4 02:56 etc/systemd/system/cryptsetup.target.wants/clevis-luks-askpass.path -> /usr/lib/systemd/system/clevis-luks-askpass.path
    …
    ```

**Additional resources**

-   [Network boot options](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/boot-options-reference#network-boot-options)
-   [Looking forward to Linux network configuration in the initial RAM disk (initrd) (Red Hat Enable Sysadmin)](https://www.redhat.com/sysadmin/network-confi-initrd)

### [9.8. Configuring NBDE clients with static IP configuration](#configuring-nbde-clients-with-static-ip-configuration) {#configuring-nbde-clients-with-static-ip-configuration .title}

To use NBDE for clients with static IP configuration (without DHCP), you must pass your network configuration to the Dracut tool manually.

**Prerequisites**

-   A Tang server is running and available.

-   The NBDE client is configured for automated unlocking of encrypted volumes by the Tang server.

    For details, see [Configuring NBDE clients for automated unlocking of LUKS-encrypted volumes](#configuring-nbde-clients-for-automated-unlocking-of-luks-encrypted-volumes "9.7. Configuring NBDE clients for automated unlocking of LUKS-encrypted volumes").

**Procedure**

1.  You can provide your static network configuration as a value for the `kernel-cmdline`{.literal} option in a `dracut`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    # dracut -fv --regenerate-all --kernel-cmdline "ip=192.0.2.10::192.0.2.1:255.255.255.0::ens3:none nameserver=192.0.2.100"
    ```

2.  Alternatively, create a .conf file in the `/etc/dracut.conf.d/`{.literal} directory with the static network information and then regenerate the initial RAM disk image:

    ``` {.language-plaintext tabindex="-1"}
    # cat /etc/dracut.conf.d/static_ip.conf
    kernel_cmdline="ip=192.0.2.10::192.0.2.1:255.255.255.0::ens3:none nameserver=192.0.2.100"
    # dracut -fv --regenerate-all
    ```

### [9.9. Configuring manual enrollment of LUKS-encrypted volumes by using a TPM 2.0 policy](#configuring-manual-enrollment-of-luks-encrypted-volumes-by-using-a-tpm2-policy) {#configuring-manual-enrollment-of-luks-encrypted-volumes-by-using-a-tpm-2.0-policy .title}

Configure unlocking of LUKS-encrypted volumes by using a Trusted Platform Module 2.0 (TPM 2.0) policy.

The `clevis-encrypt-tpm2(1)`{.literal} man page on your system provides a complete reference of available parameters.

**Prerequisites**

-   An accessible TPM 2.0-compatible device.
-   A system with the 64-bit Intel or 64-bit AMD architecture.

**Procedure**

1.  Install the `clevis-luks`{.literal} subpackage:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install clevis-luks
    ```

2.  Identify the LUKS-encrypted volume for PBD. In the following example, the block device is referred as */dev/sda2*:

    ``` {.language-plaintext tabindex="-1"}
    # lsblk
    NAME                                          MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
    sda                                             8:0    0    12G  0 disk
    ├─sda1                                          8:1    0     1G  0 part  /boot
    └─sda2                                          8:2    0    11G  0 part
      └─luks-40e20552-2ade-4954-9d56-565aa7994fb6 253:0    0    11G  0 crypt
        ├─rhel-root                               253:0    0   9.8G  0 lvm   /
        └─rhel-swap                               253:1    0   1.2G  0 lvm   [SWAP]
    ```

3.  Bind the volume to a TPM 2.0 device with the `clevis luks bind`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks bind -d /dev/sda2 tpm2 '{"hash":"sha256","key":"rsa"}'
    …
    Do you wish to initialize /dev/sda2? [yn] y
    Enter existing LUKS password:
    ```

    This command performs four steps:

    a.  Creates a new key with the same entropy as the LUKS master key.
    b.  Encrypts the new key with Clevis.
    c.  Stores the Clevis JWE object in the LUKS2 header token or uses LUKSMeta if the non-default LUKS1 header is used.
    d.  Enables the new key for use with LUKS.

    Note

    The binding procedure assumes that there is at least one free LUKS password slot. The `clevis luks bind`{.literal} command takes one of the slots.

    Alternatively, if you want to seal data to specific Platform Configuration Registers (PCR) states, add the `pcr_bank`{.literal} and `pcr_ids`{.literal} values to the `clevis luks bind`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks bind -d /dev/sda2 tpm2 '{"hash":"sha256","key":"rsa","pcr_bank":"sha256","pcr_ids":"0,1"}'
    ```

    Important

    The data can only be unsealed if PCR hash values match the policy used when sealing. Because the hashes can be rewritten, add a strong passphrase that enables you to unlock the encrypted volume manually. This is necessary when a value in a PCR changes.

    If the system cannot automatically unlock your encrypted volume after an upgrade of the `shim-x64`{.literal} package, follow the steps in the [Clevis TPM2 no longer decrypts LUKS devices after a restart](https://access.redhat.com/solutions/6175492) Red Hat Knowledgebase solution.

4.  To enable the early boot system to process the disk binding, use the `dracut`{.literal} command on an already installed system:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install clevis-dracut
    # dracut -fv --regenerate-all
    ```

**Verification**

-   Verify that the Clevis JWE object is successfully placed in a LUKS header:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks list -d /dev/sda2
    1: tpm2 '{"hash":"sha256","key":"rsa"}'
    ```

### [9.10. Configuring unlocking of LUKS-encrypted volumes by using a PKCS #11 pin](#configuring-unlocking-of-luks-encrypted-volumes-by-using-a-pkcs-11-pin) {#configuring-unlocking-of-luks-encrypted-volumes-by-using-a-pkcs-11-pin .title}

You can configure unlocking of LUKS-encrypted volumes by using a device compatible with PKCS #11, which can be either a smart card or a hardware security module (HSM).

Automated unlocking of encrypted volumes with a Clevis Public-Key Cryptography Standards (PKCS) #11 pin also requires changes in the `/etc/crypttab`{.literal} file. These changes configure the `systemd`{.literal} manager to use an `AF_UNIX`{.literal} socket to wait for the key for unlocking the volumes. This avoids prompting the user through the console.

The Clevis PKCS #11 unit file configures the socket in the `/run/systemd/clevis-pkcs11.sock`{.literal} file for sending and receiving the information about disk unlocking. For disks unlocked through a Clevis PKCS #11 pin, you must configure the socket file as a key file. See the `clevis-encrypt-pkcs11(1)`{.literal} man page on your system for more information.

**Prerequisites**

-   The PKCS #11 device is already configured and accessible.
-   The `clevis-pin-pkcs11`{.literal} package is installed.
-   The volume has at least one free LUKS password slot for the `clevis luks bind`{.literal} command.

**Procedure**

1.  Identify the LUKS-encrypted volume for PBD. In the following example, the block device is referred as */dev/sda2*:

    ``` {.language-plaintext tabindex="-1"}
    # lsblk
    NAME                                          MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
    sda                                             8:0    0    12G  0 disk
    ├─sda1                                          8:1    0     1G  0 part  /boot
    └─sda2                                          8:2    0    11G  0 part
      └─luks-40e20552-2ade-4954-9d56-565aa7994fb6 253:0    0    11G  0 crypt
        ├─rhel-root                               253:0    0   9.8G  0 lvm   /
        └─rhel-swap                               253:1    0   1.2G  0 lvm   [SWAP]
    ```

2.  Identify the URI of the PKCS #11 device you want to use for unlocking volumes, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs11-tool -L | grep uri
    uri             : pkcs11:model=PKCS%2315%20emulated;manufacturer=piv_II;serial=42facd1f749ece7f;token=clevis
    uri             : pkcs11:model=PKCS%2315%20emulated;manufacturer=OpenPGP%20project;serial=000f06080f4f;token=OpenPGP%20card%20%28User%20PIN%29
    ```

3.  Bind the volume to a PKCS #11 device with the `clevis luks bind`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks bind -d /dev/sda2 pkcs11 '{"uri":"pkcs11:model=PKCS%2315%20emulated;manufacturer=OpenPGP%20project;serial=000f06080f4f;token=OpenPGP%20card%20%28User%20PIN%29;id=%03;object=Authentication%20key;type=public"}'
    …
    Do you wish to initialize /dev/sda2? [yn] y
    Enter existing LUKS password:
    ```

    This command performs the following steps:

    a.  Creates a new key with the same entropy as the LUKS master key.
    b.  Encrypts the new key with Clevis.
    c.  Stores the Clevis JWE object in the LUKS2 header token or uses LUKSMeta if the non-default LUKS1 header is used.
    d.  Enables the new key for use with LUKS.

4.  Optionally: If your scenario requires specifying the module to use, add the module-path URI parameter:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks bind -d /dev/sda2 pkcs11 '{"uri":"pkcs11:module-path=/usr/lib64/libykcs11.so.2";model=PKCS%2315%20emulated;manufacturer=OpenPGP%20project;serial=000f06080f4f;token=OpenPGP%20card%20%28User%20PIN%29;id=%03;object=Authentication%20key;type=public}'
    ```

5.  Enable the `clevis-luks-pkcs11-askpass.socket`{.literal} unit:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now clevis-luks-pkcs11-askpass.socket
    ```

6.  Open the `/etc/crypttab`{.literal} file in a text editor and identify the line containing the LUKS-encrypted volume you want to unlock by the PKCS #11 pin, for example:

    ``` {.language-plaintext tabindex="-1"}
    luks-6e38d5e1-7f83-43cc-819a-7416bcbf9f84 UUID=6e38d5e1-7f83-43cc-819a-7416bcbf9f84 - -
    ```

7.  Replace the dashes with the `/run/systemd/clevis-pkcs11.sock`{.literal} file path and the `keyfile-timeout`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    luks-6e38d5e1-7f83-43cc-819a-7416bcbf9f84 UUID=6e38d5e1-7f83-43cc-819a-7416bcbf9f84 /run/systemd/clevis-pkcs11.sock keyfile-timeout=30s
    ```

    The `keyfile-timeout`{.literal} option provides a fall-through mechanism for when an unlocking error occurs and the system requires entering the passphrase manually through the console.

8.  Save the changes and exit the editor.

9.  To enable the early boot system to process the disk binding, which is required for unlocking root file systems, use the `dracut`{.literal} tool on an already installed system:

    ``` {.language-plaintext tabindex="-1"}
    # dracut -fv --regenerate-all
    ```

10. Restart the system.

    During the following boot process, the system prompts for the PKCS #11 device PIN and decrypts the corresponding configured encrypted disk only in case you enter the correct PIN.

**Verification**

1.  Instead of manually testing the boot process, you can encrypt and decrypt a text message with the following command:

    ``` {.language-plaintext tabindex="-1"}
    # echo "top secret" | clevis encrypt pkcs11 '{"uri":"pkcs11:module-path=/usr/lib64/libykcs11.so.2?pin-value=<PIN>"}' | clevis decrypt
    ```

    Replace *`<PIN>`{.literal}* with a PIN value. You must enter this PIN value to decrypt the message.

2.  Verify that the Clevis JWE object is successfully placed in a LUKS header, for example:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks list -d /dev/sda2
    1: pkcs11 '{"uri": "pkcs11:model=PKCS%2315%20emulated;manufacturer=piv_II;
    serial=0a35ba26b062b9c5;token=clevis;id=%02;object=Encryption%20Key?
    module-path=/usr/lib64/libykcs11.so.2"}'
    ```

### [9.11. Removing a Clevis pin from a LUKS-encrypted volume](#removing-a-clevis-pin-from-a-luks-encrypted-volume-manually) {#removing-a-clevis-pin-from-a-luks-encrypted-volume .title}

You can remove the metadata created by the `clevis luks bind`{.literal} command and also wipe a key slot that contains a passphrase added by Clevis.

In RHEL, you can use a single command to remove both the metadata created by the binding step and wipe the key slot on a selected device. See the `clevis-luks-unbind(1)`{.literal} man page for more information.

**Prerequisites**

-   A LUKS-encrypted volume with a Clevis binding.

**Procedure**

-   Remove a Clevis pin from a LUKS-encrypted volume, for example:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks unbind -d /dev/sda2 -s 1
    ```

**Verification**

-   The output of the `clevis luks list`{.literal} command is empty, for example:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks list -d /dev/sda2
    ```

    Alternatively, you can check that an output of the `cryptsetup luksDump`{.literal} command does not contain the `clevis`{.literal} string.

### [9.12. Configuring automated enrollment of LUKS-encrypted volumes by using Kickstart](#configuring-automated-enrollment-of-luks-encrypted-volumes-by-using-kickstart) {#configuring-automated-enrollment-of-luks-encrypted-volumes-by-using-kickstart .title}

You can configure an automated installation process that uses Clevis for the enrollment of LUKS-encrypted volumes.

You can adapt this procedure to use a TPM 2.0 policy instead of a Tang server.

**Procedure**

1.  Instruct Kickstart to partition the disk so that LUKS encryption is enabled with a temporary password for all mount points except `/boot`{.literal}. The password is temporary for this step of the enrollment process.

    ``` {.language-plaintext tabindex="-1"}
    part /boot --fstype="xfs" --ondisk=vda --size=256
    part / --fstype="xfs" --ondisk=vda --grow --encrypted --passphrase=temppass
    ```

    Note that OSPP-compliant systems require a more complex configuration, for example:

    ``` {.language-plaintext tabindex="-1"}
    part /boot --fstype="xfs" --ondisk=vda --size=256
    part / --fstype="xfs" --ondisk=vda --size=2048 --encrypted --passphrase=temppass
    part /var --fstype="xfs" --ondisk=vda --size=1024 --encrypted --passphrase=temppass
    part /tmp --fstype="xfs" --ondisk=vda --size=1024 --encrypted --passphrase=temppass
    part /home --fstype="xfs" --ondisk=vda --size=2048 --grow --encrypted --passphrase=temppass
    part /var/log --fstype="xfs" --ondisk=vda --size=1024 --encrypted --passphrase=temppass
    part /var/log/audit --fstype="xfs" --ondisk=vda --size=1024 --encrypted --passphrase=temppass
    ```

2.  Install the related Clevis packages by listing them in the `%packages`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    %packages
    clevis-dracut
    clevis-luks
    clevis-systemd
    %end
    ```

3.  Optional: To ensure that you can unlock the encrypted volume manually when required, [add a strong passphrase to the volume](https://access.redhat.com/solutions/230993) before you remove the temporary passphrase.

4.  Call `clevis luks bind`{.literal} to perform binding in the `%post`{.literal} section. Afterward, remove the temporary password:

    ``` {.language-plaintext tabindex="-1"}
    %post
    clevis luks bind -y -k - -d /dev/vda2 \
    tang '{"url":"http://tang.srv"}' <<< "temppass"
    cryptsetup luksRemoveKey /dev/vda2 <<< "temppass"
    dracut -fv --regenerate-all
    %end
    ```

    If your configuration relies on a Tang pin that requires network during early boot, you must modify the `dracut`{.literal} command. You must also modify it if you use NBDE clients with static IP configurations. See [Configuring NBDE clients with static IP configuration](#configuring-nbde-clients-with-static-ip-configuration "9.8. Configuring NBDE clients with static IP configuration") for details.

    Warning

    The `cryptsetup luksRemoveKey`{.literal} command prevents any further administration of a LUKS2 device. You can recover a removed master key by using the `dmsetup`{.literal} command only for LUKS1 devices. See the `dmsetup(8)`{.literal} man page on your system for more information.

**Additional resources**

-   [Automatically installing RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/index)

### [9.13. Configuring automated unlocking of a LUKS-encrypted removable storage device](#configuring-automated-unlocking-of-a-luks-encrypted-removable-storage-device) {#configuring-automated-unlocking-of-a-luks-encrypted-removable-storage-device .title}

You can configure an automated unlocking process of a LUKS-encrypted USB storage device.

You can adapt this procedure to use a TPM 2.0 policy instead of a Tang server.

**Procedure**

1.  Install the `clevis-udisks2`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install clevis-udisks2
    ```

2.  Restart the system, and then perform the binding step using the `clevis luks bind`{.literal} command as described in [Configuring NBDE clients for automated unlocking of LUKS-encrypted volumes](#configuring-nbde-clients-for-automated-unlocking-of-luks-encrypted-volumes "9.7. Configuring NBDE clients for automated unlocking of LUKS-encrypted volumes"), for example:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks bind -d /dev/sdb1 tang '{"url":"http://tang.srv"}'
    ```

**Verification**

1.  The LUKS-encrypted removable device can be now unlocked automatically in your GNOME desktop session.

2.  The device bound to a Clevis policy can be also unlocked by the `clevis luks unlock`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    # clevis luks unlock -d /dev/sdb1
    ```

### [9.14. Deploying high-availability NBDE systems](#deploying-high-availability-nbde-systems) {#deploying-high-availability-nbde-systems .title}

Tang provides two methods for building high-availability deployments of Network-bound Disc Encryption (NBDE): client redundancy and key sharing.

Client redundancy (recommended)
:   Clients should be configured with the ability to bind to multiple Tang servers. In this setup, each Tang server has its own keys and clients can decrypt by contacting a subset of these servers. Clevis already supports this workflow through its `sss`{.literal} plugin. Use this method for a secure high-availability deployment.

Key sharing
:   For redundancy purposes, more than one instance of Tang can be deployed. To configure a second or any subsequent instance, install the `tang`{.literal} packages and copy the key directory to the new host by using `rsync`{.literal} over `SSH`{.literal}. This method of sharing keys increases the risk of key compromise and requires additional automation infrastructure.

High-available NBDE that uses Shamir's Secret Sharing

:   Shamir's Secret Sharing (SSS) is a cryptographic scheme that divides a secret into several unique parts. To reconstruct the secret, a number of parts is required. The number is called the threshold and SSS is also referred to as a thresholding scheme.

    Clevis provides an implementation of SSS. It creates a key and divides it into several pieces. Each piece is encrypted using another pin including even SSS recursively. Additionally, you define the threshold `t`{.literal}. If an NBDE deployment decrypts at least `t`{.literal} pieces, then it recovers the encryption key and the decryption process succeeds. When Clevis detects a smaller number of parts than specified in the threshold, it prints an error message.

**Example 9.1. Redundancy with two Tang servers**

The following command decrypts a LUKS-encrypted device when at least one of two Tang servers is available:

``` {.language-plaintext tabindex="-1"}
# clevis luks bind -d /dev/sda1 sss '{"t":1,"pins":{"tang":[{"url":"http://tang1.srv"},{"url":"http://tang2.srv"}]}}'
```

The previous command used the following configuration scheme:

``` {.language-plaintext tabindex="-1"}
{
    "t":1,
    "pins":{
        "tang":[
            {
                "url":"http://tang1.srv"
            },
            {
                "url":"http://tang2.srv"
            }
        ]
    }
}
```

In this configuration, the SSS threshold `t`{.literal} is set to `1`{.literal} and the `clevis luks bind`{.literal} command successfully reconstructs the secret if at least one from two listed `tang`{.literal} servers is available.

**Example 9.2. Shared secret on a Tang server and a TPM device**

The following command successfully decrypts a LUKS-encrypted device when both the `tang`{.literal} server and the `tpm2`{.literal} device are available:

``` {.language-plaintext tabindex="-1"}
# clevis luks bind -d /dev/sda1 sss '{"t":2,"pins":{"tang":[{"url":"http://tang1.srv"}], "tpm2": {"pcr_ids":"0,7"}}}'
```

The configuration scheme with the SSS threshold \'t\' set to \'2\' is now:

``` {.language-plaintext tabindex="-1"}
{
    "t":2,
    "pins":{
        "tang":[
            {
                "url":"http://tang1.srv"
            }
        ],
        "tpm2":{
            "pcr_ids":"0,7"
        }
    }
}
```

For details and more examples, see the `High Availability`{.literal} section in the `tang(8)`{.literal} man page, the `Shamir’s Secret Sharing`{.literal} section in the `clevis(1)`{.literal} man page, and the `clevis-encrypt-sss(1)`{.literal} man page on your system.

### [9.15. Deployment of virtual machines in a NBDE network](#deployment-of-virtual-machines-in-a-nbde-network) {#deployment-of-virtual-machines-in-a-nbde-network .title}

When you configure Network-bound Disc Encryption (NBDE) for virtual machines, use only secure practices in production environments.

The `clevis luks bind`{.literal} command does not change the LUKS master key. This implies that if you create a LUKS-encrypted image for use in a virtual machine or cloud environment, all the instances that run this image share a master key. This is extremely insecure and should be avoided at all times.

This is not a limitation of Clevis but a design principle of LUKS. If your scenario requires having encrypted root volumes in a cloud, perform the installation process for each instance of Red Hat Enterprise Linux in the cloud as well. The images cannot be shared without also sharing a LUKS master key.

To deploy automated unlocking in a virtualized environment, use tools such as Lorax or `virt-install`{.literal} together with a Kickstart file or another automated provisioning tool. This ensures that each encrypted VM has a unique master key.

**Additional resources**

-   [Configuring automated enrollment of LUKS-encrypted volumes by using Kickstart](#configuring-automated-enrollment-of-luks-encrypted-volumes-by-using-kickstart "9.12. Configuring automated enrollment of LUKS-encrypted volumes by using Kickstart")

### [9.16. Building automatically-enrollable VM images for cloud environments by using NBDE](#building-automatically-enrollable-vm-images-for-cloud-environments-by-using-nbde) {#building-automatically-enrollable-vm-images-for-cloud-environments-by-using-nbde .title}

Deploying automatically-enrollable encrypted images in a cloud environment has unique challenges. Reduce the number of instances started from a single image. This avoids sharing the LUKS master key.

Create customized images. Do not share them in public repositories. Use them as a base for a limited number of instances. Your deployment's security policies should define the exact number of instances. Base this number on your risk tolerance for the LUKS master key attack vector.

To build LUKS-enabled automated deployments, use Lorax or virt-install with a Kickstart file. This ensures master key uniqueness during the image building process.

Cloud environments enable two Tang server deployment options:

-   You can easily deploy the Tang server within the cloud environment. However, the Tang server shares infrastructure with the data storage of other systems. The Tang server's private key and the Clevis metadata might be stored on the same physical disk. If someone accesses this disk, they can compromise the encrypted data.
-   The Tang server can be deployed outside of the cloud on independent infrastructure with a VPN link between the two infrastructures.

Important

Always keep the data storage location physically separate from the Tang server. This separation prevents the Tang server's private key from being accidentally combined with the Clevis metadata. It also gives you local control of the Tang server if the cloud infrastructure is at risk.

### [9.17. Deploying Tang as a container](#deploying-tang-as-a-container) {#deploying-tang-as-a-container .title}

The `tang`{.literal} container image provides Tang-server decryption capabilities for Clevis clients that run either in Red Hat OpenShift Container Platform (OCP) clusters or in separate virtual machines.

**Prerequisites**

-   The `podman`{.literal} package and its dependencies are installed on the system.
-   You have logged in on the `registry.redhat.io`{.literal} container catalog using the `podman login registry.redhat.io`{.literal} command. See [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication) for more information.
-   The Clevis client is installed on systems containing LUKS-encrypted volumes that you want to automatically unlock by using a Tang server.

**Procedure**

1.  Pull the `tang`{.literal} container image from the `registry.redhat.io`{.literal} registry:

    ``` {.language-plaintext tabindex="-1"}
    # podman pull registry.redhat.io/rhel10/tang
    ```

2.  Run the container, specify its port, and specify the path to the Tang keys. The following example runs the `tang`{.literal} container, specifies the port *7500*, and indicates a path to the Tang keys of the `/var/db/tang`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # podman run -d -p 7500:7500 -v tang-keys:/var/db/tang --name tang registry.redhat.io/rhel10/tang
    ```

    Note that Tang uses port 80 by default but this might collide with other services such as the Apache HTTP server.

3.  Optional: For increased security, rotate the Tang keys periodically. You can use the `tangd-rotate-keys`{.literal} script, for example:

    ``` {.language-plaintext tabindex="-1"}
    # podman run --rm -v tang-keys:/var/db/tang registry.redhat.io/rhel10/tang tangd-rotate-keys -v -d /var/db/tang
    Rotated key 'rZAMKAseaXBe0rcKXL1hCCIq-DY.jwk' -> .'rZAMKAseaXBe0rcKXL1hCCIq-DY.jwk'
    Rotated key 'x1AIpc6WmnCU-CabD8_4q18vDuw.jwk' -> .'x1AIpc6WmnCU-CabD8_4q18vDuw.jwk'
    Created new key GrMMX_WfdqomIU_4RyjpcdlXb0E.jwk
    Created new key _dTTfn17sZZqVAp80u3ygFDHtjk.jwk
    Keys rotated successfully.
    ```

**Verification**

-   On a system that contains LUKS-encrypted volumes for automated unlocking by the presence of the Tang server, verify that the Clevis client works correctly. Check that it can encrypt and decrypt a plain text message using Tang:

    ``` {.language-plaintext tabindex="-1"}
    # echo test | clevis encrypt tang '{"url":"http://localhost:7500"}' | clevis decrypt
    The advertisement contains the following signing keys:

    x1AIpc6WmnCU-CabD8_4q18vDuw

    Do you wish to trust these keys? [ynYN] y
    test
    ```

    The previous example command shows the `test`{.literal} string at the end of its output when a Tang server is available on the *localhost* URL and communicates through port *7500*.

**Additional resources**

-   [Configuring automated unlocking of encrypted volumes by using policy-based decryption](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-by-using-policy-based-decryption)

### [9.18. Automated unlocking of encrypted volumes by using a Trustee attestation server](#automated-unlocking-of-encrypted-volumes-by-using-a-trustee-attestation-server) {#automated-unlocking-of-encrypted-volumes-by-using-a-trustee-attestation-server .title}

You can automate encryption and decryption of LUKS volumes with remote attestation through the Trustee Key Broker Service (KBS). The Clevis pin `trustee`{.literal} protects disk encryption keys. Your platform must prove its integrity to a remote server before a key is released.

Confidential computing workloads require that disk encryption keys are never exposed. Do not expose them to the infrastructure provider or to any untrusted software. In these environments, LUKS volumes can only be decrypted after the platform proves its integrity through remote attestation.

Without the `trustee`{.literal} pin, Clevis cannot bind LUKS volumes to a Trustee attestation server. Operators must implement custom key retrieval workflows outside the standard Clevis and LUKS tools.

The `trustee`{.literal} pin addresses two primary use cases:

-   Confidential clusters for OpenShift, where cluster nodes run inside Trusted Execution Environments (TEEs). They must unlock their encrypted root volumes after attestation.
-   Confidential VMs with KubeVirt or OpenShift Virtualization, where guest VMs running inside TEEs must decrypt their virtual disks without operator intervention.

In both scenarios, the Trustee server acts as the policy enforcement point. It releases the disk encryption key only when the platform's attestation is validated. The attestation evidence is checked against reference values.

RHEL provides the Clevis pin `trustee`{.literal} through the `clevis-pin-trustee`{.literal} package. When you bind a LUKS volume with the `trustee`{.literal} pin, Clevis stores the encryption key on a remote Trustee server. You can only retrieve this key after the machine passes attestation. This proves it is running in a genuine Trusted Execution Environment (TEE).

The `trustee`{.literal} pin integrates with the standard Clevis framework through the `clevis-encrypt-trustee`{.literal} and `clevis-decrypt-trustee`{.literal} commands. The pin also includes the `60clevis-pin-trustee`{.literal} dracut module for automated root volume unlocking during early boot.

Administrators can bind LUKS-encrypted volumes to Trustee servers. Use the `clevis luks bind -d `{.literal}*`<device>`{.literal}*` trustee '`{.literal}*`<config>`{.literal}*`'`{.literal} command. The configuration specifies:

-   server URLs
-   resource path for the encryption key
-   optional parameters such as TLS certificates, retry count, and attestation data

**Example 9.3. Binding an encrypted volume to Trustee servers**

The following command binds the encrypted volume at `/dev/sda2`{.literal} to the servers `https://trustee1.example.com`{.literal} and `https://trustee2.example.com`{.literal}:

``` {.language-plaintext tabindex="-1"}
# clevis luks bind -d /dev/sda2 trustee '{"servers":[{"url":"https://trustee1.example.com:8080","cert":"/etc/pki/tls/certs/trustee1.pem"}, "url":"https://trustee2.example.com:8080","cert":"/etc/pki/tls/certs/trustee2.pem"}],"path":"default/mycluster/rootkey","num_retries":5,"initdata":"{\"cc_eventlog\":\"value1\"}"}'
```

After you bind the volume, the dracut `initramfs`{.literal} module automatically unlocks it during early boot. This triggers the `trustee-attester`{.literal} binary. The binary performs remote attestation and retrieves the decryption key from the Trustee KBS. The standard Clevis commands work with the `trustee`{.literal} pin: `clevis luks list`{.literal}, `clevis luks unbind`{.literal}, and `clevis luks unlock`{.literal}. You can combine `trustee`{.literal} with other pins (`tang`{.literal} and `tpm2`{.literal}) within the SSS pin. This enables multifactor or multi-policy unlock setups.

**Additional resources**

-   [Deploying Red Hat build of Trustee](https://docs.redhat.com/en/documentation/openshift_sandboxed_containers/latest#Deploying%20Red%20Hat%20build%20of%20Trustee)
-   [Introducing Confidential Containers Trustee: Attestation Services Solution Overview and Use Cases](https://www.redhat.com/en/blog/introducing-confidential-containers-trustee-attestation-services-solution-overview-and-use-cases)

### [9.19. Configuring NBDE by using RHEL system roles](#configuring-nbde-by-using-rhel-system-roles) {#configuring-nbde-by-using-rhel-system-roles .title}

You can use the `nbde_client`{.literal} and `nbde_server`{.literal} RHEL system roles for automated deployments of Policy-Based Decryption (PBD) solutions by using Clevis and Tang.

The `rhel-system-roles`{.literal} package contains these system roles, the related examples, and the reference documentation.

#### [9.19.1. Using the nbde_server RHEL system role for setting up multiple Tang servers](#using-the-nbde-server-rhel-system-role-for-setting-up-multiple-tang-servers) {#using-the-nbde_server-rhel-system-role-for-setting-up-multiple-tang-servers .title}

By using the `nbde_server`{.literal} system role, you can deploy and manage a Tang server as part of an automated disk encryption solution.

This role supports the following features:

-   Rotating Tang keys
-   Deploying and backing up Tang keys

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Deploy a Tang server
      hosts: tang.server.example.com
      tasks:
      - name: Install and configure periodic key rotation
        ansible.builtin.include_role:
            name: redhat.rhel_system_roles.nbde_server
        vars:
          nbde_server_rotate_keys: yes
          nbde_server_manage_firewall: true
          nbde_server_manage_selinux: true
    ```

    This example playbook ensures deploying of your Tang server and a key rotation.

    The settings specified in the example playbook include the following:

    `nbde_server_manage_firewall: true`{.literal}
    :   Use the `firewall`{.literal} system role to manage ports used by the `nbde_server`{.literal} role.

    `nbde_server_manage_selinux: true`{.literal}

    :   Use the `selinux`{.literal} system role to manage ports used by the `nbde_server`{.literal} role.

        For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.nbde_server/README.md`{.literal} file on the control node.

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

-   On your Network-Bound Disk Encryption (NBDE) client, verify that your Tang server works correctly by using the following command. The command must return the identical message you pass for encryption and decryption:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'echo test | clevis encrypt tang '{"url":"<tang.server.example.com>"}' -y | clevis decrypt'
    test
    ```

#### [9.19.2. Setting up Clevis clients with DHCP by using the nbde_client RHEL system role](#setting-up-clevis-clients-with-dhcp-by-using-the-nbdeclient-rhel-system-role) {#setting-up-clevis-clients-with-dhcp-by-using-the-nbde_client-rhel-system-role .title}

With the `nbde_client`{.literal} system role you can deploy multiple Clevis clients in an automated way.

This role supports binding a LUKS-encrypted volume to one or more Network-Bound (NBDE) servers - Tang servers. You can either preserve the existing volume encryption with a passphrase or remove the passphrase. After removing the passphrase, you can then unlock the volume only using NBDE. This is useful when a volume is initially encrypted by using a temporary key or password that you remove after you provision the system.

If you provide both a passphrase and a key file, the role uses what you have provided first. If it does not find any of these valid, it attempts to retrieve a passphrase from an existing binding.

Policy-Based Decryption (PBD) defines a binding as a mapping of a device to a slot. This means that you can have multiple bindings for the same device. The default slot is slot 1.

Note

The `nbde_client`{.literal} system role supports only Tang bindings. Therefore, you cannot use it for TPM2 bindings.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   A volume that is already encrypted by using LUKS.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configure clients for unlocking of encrypted volumes by Tang servers
      hosts: managed-node-01.example.com
      tasks:
        - name: Create NBDE client bindings
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.nbde_client
          vars:
            nbde_client_bindings:
              - device: /dev/rhel/root
                encryption_key_src: /etc/luks/keyfile
                nbde_client_early_boot: true
                state: present
                servers:
                  - http://server1.example.com
                  - http://server2.example.com
              - device: /dev/rhel/swap
                encryption_key_src: /etc/luks/keyfile
                servers:
                  - http://server1.example.com
                  - http://server2.example.com
    ```

    This example playbook configures Clevis clients for automated unlocking of two LUKS-encrypted volumes when at least one of two Tang servers is available.

    The settings specified in the example playbook include the following:

    `state: present`{.literal}
    :   The values of `state`{.literal} indicate the configuration after you run the playbook. Use the `present`{.literal} value for either creating a new binding or updating an existing one. Contrary to a `clevis luks bind`{.literal} command, you can use `state: present`{.literal} also for overwriting an existing binding in its device slot. The `absent`{.literal} value removes a specified binding.

    `nbde_client_early_boot: true`{.literal}

    :   The `nbde_client`{.literal} role ensures that networking for a Tang pin is available during early boot by default. If your scenario requires to disable this feature, add the `nbde_client_early_boot: false`{.literal} variable to your playbook.

        For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.nbde_client/README.md`{.literal} file on the control node.

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

1.  On your NBDE client, check that the encrypted volume intended for automatic unlocking by your Tang servers contains the corresponding information in its LUKS pins:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'clevis luks list -d /dev/rhel/root'
    1: tang '{"url":"<http://server1.example.com/>"}'
    2: tang '{"url":"<http://server2.example.com/>"}'
    ```

2.  If you do not use the `nbde_client_early_boot: false`{.literal} variable, verify that the bindings are available for the early boot, for example:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'lsinitrd | grep clevis-luks'
    lrwxrwxrwx   1 root     root           48 Jan  4 02:56 etc/systemd/system/cryptsetup.target.wants/clevis-luks-askpass.path -> /usr/lib/systemd/system/clevis-luks-askpass.path
    …
    ```

#### [9.19.3. Setting up static-IP Clevis clients by using the nbde_client RHEL system role](#setting-up-static-ip-clevis-clients-by-using-the-nbdeclient-rhel-system-role) {#setting-up-static-ip-clevis-clients-by-using-the-nbde_client-rhel-system-role .title}

The `nbde_client`{.literal} RHEL system role supports only scenarios with Dynamic Host Configuration Protocol (DHCP). On a Network-Bound Disk Encryption (NBDE) client with static IP configuration, you must pass your network configuration as a kernel boot parameter.

Typically, administrators want to reuse a playbook and not maintain individual playbooks for each host to which Ansible assigns static IP addresses during early boot. In this case, you can use variables in the playbook and provide the settings in an external file. As a result, you need only one playbook and one file with the settings.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   A volume that is already encrypted by using LUKS.

**Procedure**

1.  Create a file with the network settings of your hosts, for example, `static-ip-settings-clients.yml`{.literal}, and add the values you want to dynamically assign to the hosts:

    ``` {.language-yaml tabindex="-1"}
    clients:
      managed-node-01.example.com:
        ip_v4: 192.0.2.1
        gateway_v4: 192.0.2.254
        netmask_v4: 255.255.255.0
        interface: enp1s0
      managed-node-02.example.com:
        ip_v4: 192.0.2.2
        gateway_v4: 192.0.2.254
        netmask_v4: 255.255.255.0
        interface: enp1s0
    ```

2.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    - name: Configure clients for unlocking of encrypted volumes by Tang servers
      hosts: managed-node-01.example.com,managed-node-02.example.com
      vars_files:
        - ~/static-ip-settings-clients.yml
      tasks:
        - name: Create NBDE client bindings
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.network
          vars:
            nbde_client_bindings:
              - device: /dev/rhel/root
                encryption_key_src: /etc/luks/keyfile
                servers:
                  - http://server1.example.com
                  - http://server2.example.com
              - device: /dev/rhel/swap
                encryption_key_src: /etc/luks/keyfile
                servers:
                  - http://server1.example.com
                  - http://server2.example.com

        - name: Configure a Clevis client with static IP address during early boot
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.bootloader
          vars:
            bootloader_settings:
              - kernel: ALL
                options:
                  - name: ip
                    value: "{{ clients[inventory_hostname]['ip_v4'] }}::{{ clients[inventory_hostname]['gateway_v4'] }}:{{ clients[inventory_hostname]['netmask_v4'] }}::{{ clients[inventory_hostname]['interface'] }}:none"
    ```

    This playbook reads certain values dynamically for each host listed in the `~/static-ip-settings-clients.yml`{.literal} file.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.network/README.md`{.literal} file on the control node.

3.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

4.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Additional resources**

-   [Looking forward to Linux network configuration in the initial ramdisk (initrd)](https://www.redhat.com/sysadmin/network-confi-initrd)

## [Chapter 10. Blocking and allowing applications by using fapolicyd](#blocking-and-allowing-applications-by-using-fapolicyd) {#chapter-10.-blocking-and-allowing-applications-by-using-fapolicyd .title}

Use the `fapolicyd`{.literal} framework to implement an application allowlist solution that helps increase system security. Setting and enforcing a policy that either allows or denies application execution based on a rule set efficiently prevents the execution of unknown and potentially malicious software.

### [10.1. The fapolicyd framework structure](#introduction-to-fapolicyd) {#the-fapolicyd-framework-structure .title}

The `fapolicyd`{.literal} software framework controls the execution of applications based on a user-defined policy. This is one of the most efficient ways to prevent running untrusted and possibly malicious applications on the system.

Components and trust

:   The `fapolicyd`{.literal} framework provides the following components:

    -   `fapolicyd`{.literal} service
    -   `fapolicyd`{.literal} command-line utilities, such as the `fapolicyd-cli`{.literal} command and the `fagenrules`{.literal} script
    -   `fapolicyd`{.literal} RPM plugin

    The administrator can define `allow`{.literal} and `deny`{.literal} execution rules for any application with the option to audit based on a path, hash, MIME type, or trust.

    The `fapolicyd`{.literal} framework introduces the concept of trust. An application is trusted when the system package manager correctly installs it and therefore registered in the system RPM database. The `fapolicyd`{.literal} daemon uses the RPM database as a list of trusted binaries and scripts.

    The `fapolicyd`{.literal} RPM plugin registers any system update that is handled by either the DNF or RPM package manager. The plugin notifies the `fapolicyd`{.literal} daemon about changes in this database. Other ways of adding applications require the creation of custom rules and restarting the `fapolicyd`{.literal} service.

    For more information, see the `fapolicyd`{.literal}-related man pages listed by using the `man -k fapolicyd`{.literal} command on your system.

Configuration files and directories

:   The `fapolicyd`{.literal} service configuration is located in the `/etc/fapolicyd/`{.literal} directory with the following structure:

    -   The `/etc/fapolicyd/fapolicyd.trust`{.literal} file contains a list of trusted files. You can also use multiple trust files in the `/etc/fapolicyd/trust.d/`{.literal} directory.
    -   The `/etc/fapolicyd/rules.d/`{.literal} directory contains files with `allow`{.literal} and `deny`{.literal} execution rules. The `fagenrules`{.literal} script merges these component rules files to the `/etc/fapolicyd/compiled.rules`{.literal} file.
    -   The `fapolicyd.conf`{.literal} file contains the daemon's configuration options. This file is useful primarily for performance-tuning purposes.

Rules

:   Rules in `/etc/fapolicyd/rules.d/`{.literal} are organized in several files, each representing a different policy goal. The numbers at the beginning of the corresponding file names determine the order in `/etc/fapolicyd/compiled.rules`{.literal}:

    +:----------------------------------+:----------------------------------+
    | 10                                | language rules                    |
    +-----------------------------------+-----------------------------------+
    | 20                                | Dracut-related rules              |
    +-----------------------------------+-----------------------------------+
    | 21                                | rules for updaters                |
    +-----------------------------------+-----------------------------------+
    | 30                                | patterns                          |
    +-----------------------------------+-----------------------------------+
    | 40                                | ELF rules                         |
    +-----------------------------------+-----------------------------------+
    | 41                                | shared objects rules              |
    +-----------------------------------+-----------------------------------+
    | 42                                | trusted ELF rules                 |
    +-----------------------------------+-----------------------------------+
    | 70                                | trusted language rules            |
    +-----------------------------------+-----------------------------------+
    | 72                                | shell rules                       |
    +-----------------------------------+-----------------------------------+
    | 90                                | deny execute rules                |
    +-----------------------------------+-----------------------------------+
    | 95                                | allow open rules                  |
    +-----------------------------------+-----------------------------------+

    Show more

    For more information and examples, see the documentation installed with the `fapolicyd`{.literal} package in the `/usr/share/doc/fapolicyd/`{.literal} directory, the `/usr/share/fapolicyd/sample-rules/README-rules`{.literal} file, and the `fapolicyd.rules(5)`{.literal} and `fagenrules(8)`{.literal} man pages on your system.

Integrity checking

:   You can use one of the following ways for `fapolicyd`{.literal} integrity checking:

    -   File-size checking
    -   Comparing SHA-256 hashes
    -   Integrity Measurement Architecture (IMA) subsystem

    By default, `fapolicyd`{.literal} does no integrity checking. Integrity checking based on the file size is fast, but an attacker can replace the content of the file and preserve its byte size. Computing and checking SHA-256 checksums is more secure, but it affects the performance of the system. The `integrity = ima`{.literal} option in `fapolicyd.conf`{.literal} requires support for files\' extended attributes (also known as *`xattr`{.literal}*) on all file systems containing executable files.

**Additional resources**

-   [Enhancing security with the kernel integrity subsystem](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/enhancing-security-with-the-kernel-integrity-subsystem)

### [10.2. Deploying fapolicyd](#deploying-fapolicyd) {#deploying-fapolicyd .title}

When deploying the `fapolicyd`{.literal} application allowlisting framework, you can either try your configuration in permissive mode first or directly enable the service in the default configuration.

**Procedure**

1.  Install the `fapolicyd`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install fapolicyd
    ```

2.  Set the Audit subsystem for recording `fapolicyd`{.literal} events:

    ``` {.language-plaintext tabindex="-1"}
    # auditctl -w /etc/fapolicyd/ -p wa -k fapolicyd_changes
    # service try-restart auditd
    ```

3.  Optional: To try your configuration first, change mode to permissive.

    a.  Open the `/etc/fapolicyd/fapolicyd.conf`{.literal} file in a text editor of your choice, for example:

        ``` {.language-plaintext tabindex="-1"}
        # vi /etc/fapolicyd/fapolicyd.conf
        ```

    b.  Change the value of the `permissive`{.literal} option from `0`{.literal} to `1`{.literal}, save the file, and exit the editor:

        ``` {.language-plaintext tabindex="-1"}
        permissive = 1
        ```

        Alternatively, you can debug your configuration by using the `fapolicyd --debug-deny --permissive`{.literal} command before you start the service. See the [Troubleshooting problems related to fapolicyd](#troubleshooting-problems-related-to-fapolicyd "10.6. Troubleshooting problems related to fapolicyd") section for more information.

4.  Enable and start the `fapolicyd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now fapolicyd
    ```

5.  If you enabled permissive mode through `/etc/fapolicyd/fapolicyd.conf`{.literal}:

    a.  Use your applications.

    b.  Check Audit logs for `fanotify`{.literal} denials, for example:

        ``` {.language-plaintext tabindex="-1"}
        # ausearch -ts recent -m fanotify
        ```

    c.  When debugged, disable permissive mode by changing the corresponding value back to `permissive = 0`{.literal}, and restart the service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart fapolicyd
        ```

**Verification**

1.  Verify that the `fapolicyd`{.literal} service is running correctly:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status fapolicyd
    ● fapolicyd.service - File Access Policy Daemon
         Loaded: loaded (/usr/lib/systemd/system/fapolicyd.service; enabled; preset: disabled)
         Active: active (running) since Tue 2024-10-08 05:53:50 EDT; 11s ago
    …
    Oct 08 05:53:51 machine1.example.com fapolicyd[4974]: Loading trust data from rpmdb backend
    Oct 08 05:53:51 machine1.example.com fapolicyd[4974]: Loading trust data from file backend
    Oct 08 05:53:51 machine1.example.com fapolicyd[4974]: Starting to listen for events
    ```

2.  Log in as a user without root privileges, and check that `fapolicyd`{.literal} is working, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /bin/ls /tmp
    $ /tmp/ls
    bash: /tmp/ls: Operation not permitted
    ```

**Additional resources**

-   [No FANOTIFY event seen in the audit log despite fapolicyd blocking operations (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7052379)

### [10.3. Marking files as trusted using an additional source of trust](#marking-files-as-trusted-using-an-additional-source-of-trust) {#marking-files-as-trusted-using-an-additional-source-of-trust .title}

The `fapolicyd`{.literal} framework trusts files contained in the RPM database. You can mark additional files as trusted by modifying sources of trust.

You can modify the `/etc/fapolicyd/fapolicyd.trust`{.literal} plain text file or files in the `/etc/fapolicyd/trust.d`{.literal} directory, either directly using a text editor or through `fapolicyd-cli`{.literal} commands. See the `fapolicyd.trust(13)`{.literal} and `fapolicyd-cli(8)`{.literal} man pages on your system for more details.

Note

For performance reasons, mark files as trusted using `fapolicyd.trust`{.literal} or `trust.d/`{.literal} rather than write custom `fapolicyd`{.literal} rules.

**Prerequisites**

-   The `fapolicyd`{.literal} framework is deployed on your system.

**Procedure**

1.  Copy your custom binary to the required directory, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /bin/ls /tmp
    $ /tmp/ls
    bash: /tmp/ls: Operation not permitted
    ```

2.  Mark your custom binary as trusted, and store the corresponding entry to the `myapp`{.literal} file in `/etc/fapolicyd/trust.d/`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # fapolicyd-cli --file add /tmp/ls --trust-file myapp
    ```

    -   If you skip the `--trust-file`{.literal} option, then the previous command adds the corresponding line to `/etc/fapolicyd/fapolicyd.trust`{.literal}.

    -   To mark all existing files in a directory as trusted, provide the directory path as an argument of the `--file`{.literal} option, for example:

        ``` {.language-plaintext tabindex="-1"}
        # fapolicyd-cli --file add /tmp/my_bin_dir/ --trust-file myapp
        ```

3.  Update the `fapolicyd`{.literal} database:

    ``` {.language-plaintext tabindex="-1"}
    # fapolicyd-cli --update
    ```

    Note

    Changing the content of a trusted file or directory changes its checksum, and therefore,`fapolicyd`{.literal} no longer considers it trusted.

    To restore trust in the new content, refresh the file trust database by using the `fapolicyd-cli --file update`{.literal} command. If you do not provide any argument, the entire database refreshes. Alternatively, you can specify a path to a specific file or directory. Then, update the database by using `fapolicyd-cli --update`{.literal}.

**Verification**

1.  Check that you can run your custom binary, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ /tmp/ls
    ls
    ```

### [10.4. Adding custom allow and deny rules for fapolicyd](#adding-custom-allow-and-deny-rules-for-fapolicyd) {#adding-custom-allow-and-deny-rules-for-fapolicyd .title}

The default set of `fapolicyd`{.literal} rules does not affect system functions. For custom scenarios, mark additional files as trusted or add custom rules. Examples include storing binaries in non-standard directories or adding applications without DNF or RPM.

**Prerequisites**

-   The `fapolicyd`{.literal} framework is deployed on your system.

**Procedure**

1.  Copy your custom binary to the required directory, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /bin/ls /tmp
    $ /tmp/ls
    bash: /tmp/ls: Operation not permitted
    ```

2.  Stop the `fapolicyd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop fapolicyd
    ```

3.  Use debug mode to identify a corresponding rule. Because the output of the `fapolicyd --debug`{.literal} command is verbose and you can stop it only by pressing Ctrl+C or killing the corresponding process, redirect the error output to a file. In this case, you can limit the output only to access denials by using the `--debug-deny`{.literal} option instead of `--debug`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # fapolicyd --debug-deny 2> fapolicy.output &
    [1] 51341
    ```

    Alternatively, you can run `fapolicyd`{.literal} debug mode in another session.

4.  Repeat the command that `fapolicyd`{.literal} denied:

    ``` {.language-plaintext tabindex="-1"}
    $ /tmp/ls
    bash: /tmp/ls: Operation not permitted
    ```

5.  Stop debug mode by resuming it in the foreground and pressing Ctrl+C:

    ``` {.language-plaintext tabindex="-1"}
    # fg
    fapolicyd --debug 2> fapolicy.output
    ^C
    …
    ```

    Alternatively, kill the process of `fapolicyd`{.literal} debug mode:

    ``` {.language-plaintext tabindex="-1"}
    # kill 51341
    ```

6.  Find a rule that denies the execution of your application:

    ``` {.language-plaintext tabindex="-1"}
    # cat fapolicy.output | grep 'deny_audit'
    …
    rule=13 dec=deny_audit perm=execute auid=0 pid=6855 exe=/usr/bin/bash : path=/tmp/ls ftype=application/x-executable trust=0
    ```

7.  Locate the file that contains a rule that denies the execution of your custom binary. In this case, the `deny_audit perm=execute`{.literal} rule belongs to the `90-deny-execute.rules`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # ls /etc/fapolicyd/rules.d/
    10-languages.rules  40-bad-elf.rules       72-shell.rules
    20-dracut.rules     41-shared-obj.rules    90-deny-execute.rules
    21-updaters.rules   42-trusted-elf.rules   95-allow-open.rules
    30-patterns.rules   70-trusted-lang.rules

    # cat /etc/fapolicyd/rules.d/90-deny-execute.rules
    # Deny execution for anything untrusted

    deny_audit perm=execute all : all
    ```

8.  Add a new `allow`{.literal} rule to a file with a lower number prefix than `90-deny-execute.rules`{.literal} in the `/etc/fapolicyd/rules.d/`{.literal} directory. Rules are processed in alphanumeric order by filename.

    a.  Create the rule file and open it in a text editor of your choice, for example:

        ``` {.language-plaintext tabindex="-1"}
        # touch /etc/fapolicyd/rules.d/80-myapps.rules
        # vi /etc/fapolicyd/rules.d/80-myapps.rules
        ```

    b.  Insert the following rule to the `80-myapps.rules`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        allow perm=execute exe=/usr/bin/bash trust=1 : path=/tmp/ls ftype=application/x-executable trust=0
        ```

        Alternatively, you can allow executions of all binaries in the `/tmp`{.literal} directory by adding the following rule to the rule file in `/etc/fapolicyd/rules.d/`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        allow perm=execute exe=/usr/bin/bash trust=1 : dir=/tmp/ trust=0
        ```

        Important

        To make a rule effective recursively on all directories under the specified directory, add a trailing slash to the `dir=`{.literal} parameter value. In the previous example, use `/tmp/`{.literal} instead of `/tmp`{.literal}.

9.  Prevent changes in the content of your custom binary

    a.  Define the required rule using an SHA-256 checksum:

        ``` {.language-plaintext tabindex="-1"}
        $ sha256sum /tmp/ls
        780b75c90b2d41ea41679fcb358c892b1251b68d1927c80fbc0d9d148b25e836  ls
        ```

    b.  Change the rule to the following definition:

        ``` {.language-plaintext tabindex="-1"}
        allow perm=execute exe=/usr/bin/bash trust=1 : sha256hash=780b75c90b2d41ea41679fcb358c892b1251b68d1927c80fbc0d9d148b25e836
        ```

10. Check that the list of compiled rules differs from the rule set in `/etc/fapolicyd/rules.d/`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # fagenrules --check
    /usr/sbin/fagenrules: Rules have changed and should be updated
    ```

11. Update the list, which is stored in the `/etc/fapolicyd/compiled.rules`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # fagenrules --load
    ```

12. Check that your custom rule is in the list of `fapolicyd`{.literal} rules before the rule that denied the execution:

    ``` {.language-plaintext tabindex="-1"}
    # fapolicyd-cli --list
    ...
    13. allow perm=execute exe=/usr/bin/bash trust=1 : path=/tmp/ls ftype=application/x-executable trust=0
    14. deny_audit perm=execute all : all
    …
    ```

13. Start the `fapolicyd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start fapolicyd
    ```

**Verification**

1.  Check that your custom binary can be now executed, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ /tmp/ls
    ls
    ```

**Next steps**

For basic scenarios, see [Marking files as trusted using an additional source of trust](#marking-files-as-trusted-using-an-additional-source-of-trust "10.3. Marking files as trusted using an additional source of trust"). In more advanced scenarios such as allowing to run a custom binary only for specific user and group identifiers, add new custom rules to the `/etc/fapolicyd/rules.d/`{.literal} directory.

For more information and examples, see the documentation installed with the `fapolicyd`{.literal} package in the `/usr/share/doc/fapolicyd/`{.literal} directory, the `/usr/share/fapolicyd/sample-rules/README-rules`{.literal} file, and the `fapolicyd.rules(5)`{.literal} and `fagenrules(8)`{.literal} man pages on your system.

### [10.5. Enabling fapolicyd integrity checks](#enabling-fapolicyd-integrity-checks) {#enabling-fapolicyd-integrity-checks .title}

By default, `fapolicyd`{.literal} does not perform integrity checking. You can configure `fapolicyd`{.literal} to perform integrity checks by comparing either file sizes or SHA-256 hashes. You can also set integrity checks by using the Integrity Measurement Architecture (IMA) subsystem.

**Prerequisites**

-   The `fapolicyd`{.literal} framework is deployed on your system.

**Procedure**

1.  Open the `/etc/fapolicyd/fapolicyd.conf`{.literal} file in a text editor of your choice, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/fapolicyd/fapolicyd.conf
    ```

2.  Change the value of the `integrity`{.literal} option from `none`{.literal} to `sha256`{.literal}, save the file, and exit the editor:

    ``` {.language-plaintext tabindex="-1"}
    integrity = sha256
    ```

3.  Restart the `fapolicyd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart fapolicyd
    ```

**Verification**

1.  Back up the file used for the verification:

    ``` {.language-plaintext tabindex="-1"}
    # cp /bin/more /bin/more.bak
    ```

2.  Change the content of the `/bin/more`{.literal} binary:

    ``` {.language-plaintext tabindex="-1"}
    # cat /bin/less > /bin/more
    ```

3.  Attempt to use the changed binary as a regular user and verify `fapolicyd`{.literal} denies the operation:

    ``` {.language-plaintext tabindex="-1"}
    # su example.user
    $ /bin/more /etc/redhat-release
    bash: /bin/more: Operation not permitted
    ```

4.  Revert the changes:

    ``` {.language-plaintext tabindex="-1"}
    # mv -f /bin/more.bak /bin/more
    ```

### [10.6. Troubleshooting problems related to fapolicyd](#troubleshooting-problems-related-to-fapolicyd) {#troubleshooting-problems-related-to-fapolicyd .title}

The `fapolicyd`{.literal} application framework provides tools for troubleshooting the most common problems and you can also add applications installed with the `rpm`{.literal} command to the trust database.

Running `fapolicyd`{.literal} on a system with containers

:   Because the `fapolicyd`{.literal} framework does not fully support namespaces and containers, you must use a workaround on systems running containers. To prevent startup failures of containers because of `fapolicyd`{.literal}, create the `/etc/fapolicyd/rules.d/25-runc.rules`{.literal} file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    allow perm=any pattern=ld_so exe=/usr/bin/runc : all
    allow perm=any uid=0 pattern=ld_so exe=/runc : trust=1
    ```

    Save the file, run the `fagenrules`{.literal} script, and enter the `fapolicyd-cli --reload-rules`{.literal} command to apply the changes. Alternatively, you can remove the `tmpfs`{.literal} value from the `watch_fs`{.literal} option in the `/etc/fapolicyd/fapolicyd.conf`{.literal} file and restart the `fapolicyd`{.literal} service by using the `systemctl restart fapolicyd`{.literal} command. Note that this alternative approach lowers the system security.

Installing applications by using RPM

:   If you install an application by using the `rpm`{.literal} command, you have to perform a manual refresh of the `fapolicyd`{.literal} RPM database:

    1.  Install your *\<application\>*:

        ``` {.language-plaintext tabindex="-1"}
        # rpm -i <application>.rpm
        ```

    2.  Refresh the database:

        ``` {.language-plaintext tabindex="-1"}
        # fapolicyd-cli --update
        ```

        If you skip this step, the system can freeze and must be restarted.

Service status

:   If `fapolicyd`{.literal} does not work correctly, check the service status:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status fapolicyd
    ```

`fapolicyd-cli`{.literal} checks and listings

:   The `--check-config`{.literal}, `--check-watch_fs`{.literal}, and `--check-trustdb`{.literal} options help you find syntax errors, not-yet-watched file systems, and file mismatches, for example:

    ``` {.language-plaintext tabindex="-1"}
    # fapolicyd-cli --check-config
    Daemon config is OK

    # fapolicyd-cli --check-trustdb
    /etc/selinux/targeted/contexts/files/file_contexts miscompares: size sha256
    /etc/selinux/targeted/policy/policy.31 miscompares: size sha256
    ```

    -   Use the `--list`{.literal} option to check the current list of rules and their order:

        ``` {.language-plaintext tabindex="-1"}
        # fapolicyd-cli --list
        …
        9. allow perm=execute all : trust=1
        10. allow perm=open all : ftype=%languages trust=1
        11. deny_audit perm=any all : ftype=%languages
        12. allow perm=any all : ftype=text/x-shellscript
        13. deny_audit perm=execute all : all
        …
        ```

Debug mode

:   Debug mode provides detailed information about matched rules, database status, and more. To switch `fapolicyd`{.literal} to debug mode:

    1.  Stop the `fapolicyd`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl stop fapolicyd
        ```

    2.  Use debug mode to identify a corresponding rule:

        ``` {.language-plaintext tabindex="-1"}
        # fapolicyd --debug
        ```

        Because the output of the `fapolicyd --debug`{.literal} command is verbose, you can redirect the error output to a file:

        ``` {.language-plaintext tabindex="-1"}
        # fapolicyd --debug 2> fapolicy.output
        ```

        Alternatively, to limit the output only to entries when `fapolicyd`{.literal} denies access, use the `--debug-deny`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        # fapolicyd --debug-deny
        ```

Removing the `fapolicyd`{.literal} database

:   To solve problems related to the `fapolicyd`{.literal} database, try to remove the database file:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop fapolicyd
    # fapolicyd-cli --delete-db
    ```

    Warning

    Do not remove the `/var/lib/fapolicyd/`{.literal} directory. The `fapolicyd`{.literal} framework automatically restores only the database file in this directory.

Dumping the `fapolicyd`{.literal} database

:   The `fapolicyd`{.literal} contains entries from all enabled trust sources. You can check the entries after dumping the database:

    ``` {.language-plaintext tabindex="-1"}
    # fapolicyd-cli --dump-db
    ```

Application pipe

:   -   In rare cases, removing the `fapolicyd`{.literal} pipe file can solve a lockup:

        ``` {.language-plaintext tabindex="-1"}
        # rm -f /var/run/fapolicyd/fapolicyd.fifo
        ```

### [10.7. Preventing users from executing untrustworthy code by using the fapolicyd RHEL system role](#preventing-users-from-executing-untrustworthy-code-by-using-the-fapolicyd-rhel-system-role) {#preventing-users-from-executing-untrustworthy-code-by-using-the-fapolicyd-rhel-system-role .title}

You can automate the installation and configuration of the `fapolicyd`{.literal} service by using the `fapolicyd`{.literal} RHEL system role.

With this role, you can remotely configure the service to allow users to run only trusted applications. For example, you can limit execution to applications listed in the RPM database and in an allow list. Additionally, the service can perform integrity checks before it runs an allowed application.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configuring fapolicyd
      hosts: managed-node-01.example.com
      tasks:
        - name: Allow only executables installed from RPM database and specific files
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.fapolicyd
          vars:
            fapolicyd_setup_permissive: false
            fapolicyd_setup_integrity: sha256
            fapolicyd_setup_trust: rpmdb,file
            fapolicyd_add_trusted_file:
              - <path_to_allowed_command>
              - <path_to_allowed_service>
    ```

    The settings specified in the example playbook include the following:

    `fapolicyd_setup_permissive: `{.literal}*`<true|false>`{.literal}* 
    :   Enables or disables sending policy decisions to the kernel for enforcement. Set this variable for debugging and testing purposes to `false`{.literal}.

    `fapolicyd_setup_integrity: `{.literal}*`<type_type>`{.literal}*

    :   Defines the integrity checking method. You can set one of the following values:

        -   `none`{.literal} (default): Disables integrity checking.
        -   `size`{.literal}: The service compares only the file sizes of allowed applications.
        -   `ima`{.literal}: The service checks the SHA-256 hash that the kernel's Integrity Measurement Architecture (IMA) stored in a file's extended attribute. Additionally, the service performs a size check. Note that the role does not configure the IMA kernel subsystem. To use this option, you must manually configure the IMA subsystem.
        -   `sha256`{.literal}: The service compares the SHA-256 hash of allowed applications.

    `fapolicyd_setup_trust: `{.literal}*`<trust_backends>`{.literal}* 
    :   Defines the list of trust back ends. If you include the `file`{.literal} back end, specify the allowed executable files in the `fapolicyd_add_trusted_file`{.literal} list.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.fapolicyd.README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml --syntax-check
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Start a binary application that is not on the allow list as a user:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m command -a 'su -c "/bin/not_authorized_application " <user_name>'
    bash: line 1: /bin/not_authorized_application: Operation not permitted non-zero return code
    ```

## [Chapter 11. Protecting systems against intrusive USB devices](#protecting-systems-against-intrusive-usb-devices) {#chapter-11.-protecting-systems-against-intrusive-usb-devices .title}

Use USBGuard to protect your Red Hat Enterprise Linux system against intrusive USB devices. This framework helps prevent attacks, such as those involving malware or trojans loaded onto USB drives.

### [11.1. USBGuard intrusion prevention](#usbguard) {#usbguard-intrusion-prevention .title}

Use the USBGuard software framework to protect your systems against intrusive USB devices. USBGuard uses lists of allowed and blocked devices. It is based on the USB device authorization feature in the kernel.

The USBGuard framework provides the following components:

-   The system service component. It has an IPC interface for dynamic interaction and policy enforcement.
-   The command-line interface. Use it to interact with a running `usbguard`{.literal} system service.
-   The rule language. Use it to write USB device authorization policies.
-   The C++ API. Use it to interact with the system service component in a shared library.

The `usbguard`{.literal} system service configuration file is `/etc/usbguard/usbguard-daemon.conf`{.literal}. It includes options to authorize users and groups to use the IPC interface.

Important

The system service provides the USBGuard public IPC interface. In Red Hat Enterprise Linux, only the root user can access this interface by default.

Limit access to the IPC interface. Set one of these options:

-   `IPCAccessControlFiles`{.literal}
-   `IPCAllowedUsers`{.literal} and `IPCAllowedGroups`{.literal}

Do not leave the Access Control List (ACL) unconfigured. An unconfigured ACL exposes the IPC interface to all local users. They can then manipulate USB device authorization and modify the USBGuard policy.

### [11.2. Installing USBGuard](#installing-usbguard) {#installing-usbguard .title}

Install the USBGuard framework to begin defining policies that govern which USB devices are allowed to connect to your Red Hat Enterprise Linux system. This is the first step in defending against physical security breaches.

**Procedure**

1.  Install the `usbguard`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install usbguard
    ```

2.  Create an initial rule set:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard generate-policy > /etc/usbguard/rules.conf
    ```

3.  Start the `usbguard`{.literal} daemon and ensure that it starts automatically on boot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now usbguard
    ```

**Verification**

1.  Verify that the `usbguard`{.literal} service is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status usbguard
    ● usbguard.service - USBGuard daemon
       Loaded: loaded (/usr/lib/systemd/system/usbguard.service; enabled; vendor preset: disabled)
       Active: active (running) since Thu 2019-11-07 09:44:07 CET; 3min 16s ago
         Docs: man:usbguard-daemon(8)
     Main PID: 6122 (usbguard-daemon)
        Tasks: 3 (limit: 11493)
       Memory: 1.2M
       CGroup: /system.slice/usbguard.service
               └─6122 /usr/sbin/usbguard-daemon -f -s -c /etc/usbguard/usbguard-daemon.conf

    Nov 07 09:44:06 localhost.localdomain systemd[1]: Starting USBGuard daemon...
    Nov 07 09:44:07 localhost.localdomain systemd[1]: Started USBGuard daemon.
    ```

2.  List USB devices recognized by USBGuard:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard list-devices
    4: allow id 1d6b:0002 serial "0000:02:00.0" name "xHCI Host Controller" hash...
    ```

### [11.3. Blocking and authorizing a USB device by using the CLI](#blocking-and-authorizing-a-usb-device-by-using-cli) {#blocking-and-authorizing-a-usb-device-by-using-the-cli .title}

You can set USBGuard to allow, block, or reject a specific USB device by using the `usbguard`{.literal} command. This setting persists while USBGuard is running.

USBGuard uses the terms *`block`{.literal}* and *`reject`{.literal}* with the following meanings:

*`block`{.literal}*
:   Do not interact with this device for now.

*`reject`{.literal}*
:   Ignore this device as if it does not exist.

For more information, see the built-in help listed by using the `usbguard --help`{.literal} command and the `usbguard(1)`{.literal} man page on your system.

**Prerequisites**

-   The `usbguard`{.literal} service is installed and running.

**Procedure**

1.  Determine the ID of the USB device by listing the devices recognized by USBGuard:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard list-devices
    1: allow id 1d6b:0002 serial "0000:00:06.7" name "EHCI Host Controller" hash "JDOb0BiktYs2ct3mSQKopnOOV2h9MGYADwhT+oUtF2s=" parent-hash "4PHGcaDKWtPjKDwYpIRG722cB9SlGz9l9Iea93+Gt9c=" via-port "usb1" with-interface 09:00:00
    ...
    6: block id 1b1c:1ab1 serial "000024937962" name "Voyager" hash "CrXgiaWIf2bZAU+5WkzOE7y0rdSO82XMzubn7HDb95Q=" parent-hash "JDOb0BiktYs2ct3mSQKopnOOV2h9MGYADwhT+oUtF2s=" via-port "1-3" with-interface 08:06:50
    ```

2.  Authorize a device to interact with the system:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard allow-device <ID>
    ```

3.  Deauthorize and remove a device:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard reject-device <ID>
    ```

4.  Deauthorize and retain a device:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard block-device <ID>
    ```

### [11.4. Permanently blocking and authorizing a USB device](#permanently-blocking-and-authorizing-a-usb-device) {#permanently-blocking-and-authorizing-a-usb-device .title}

You can permanently block and authorize a USB device by using the `-p`{.literal} option. This adds a device-specific rule to the current policy and persists across restarts and reboots.

USBGuard uses the terms *`block`{.literal}* and *`reject`{.literal}* with the following meanings:

*`block`{.literal}*
:   Do not interact with this device for now.

*`reject`{.literal}*
:   Ignore this device as if it does not exist.

**Prerequisites**

-   The `usbguard`{.literal} service is installed and running.

**Procedure**

1.  Configure SELinux to allow the `usbguard`{.literal} daemon to write rules.

    a.  Display the `semanage`{.literal} Booleans relevant to `usbguard`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        # semanage boolean -l | grep usbguard
        usbguard_daemon_write_conf     (off  ,  off)  Allow usbguard to daemon write conf
        usbguard_daemon_write_rules    (on   ,   on)  Allow usbguard to daemon write rules
        ```

    b.  If the `usbguard_daemon_write_rules`{.literal} Boolean is turned off, turn it on.

        ``` {.language-plaintext tabindex="-1"}
        # semanage boolean -m --on usbguard_daemon_write_rules
        ```

2.  Determine the ID of the USB device by listing the devices recognized by USBGuard:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard list-devices
    1: allow id 1d6b:0002 serial "0000:00:06.7" name "EHCI Host Controller" hash "JDOb0BiktYs2ct3mSQKopnOOV2h9MGYADwhT+oUtF2s=" parent-hash "4PHGcaDKWtPjKDwYpIRG722cB9SlGz9l9Iea93+Gt9c=" via-port "usb1" with-interface 09:00:00
    ...
    6: block id 1b1c:1ab1 serial "000024937962" name "Voyager" hash "CrXgiaWIf2bZAU+5WkzOE7y0rdSO82XMzubn7HDb95Q=" parent-hash "JDOb0BiktYs2ct3mSQKopnOOV2h9MGYADwhT+oUtF2s=" via-port "1-3" with-interface 08:06:50
    ```

3.  Permanently authorize a device to interact with the system:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard allow-device <ID> -p
    ```

4.  Permanently deauthorize and remove a device:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard reject-device <ID> -p
    ```

5.  Permanently deauthorize and retain a device:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard block-device <ID> -p
    ```

**Verification**

1.  Check that the USBGuard rules include the changes you made.

    ``` {.language-plaintext tabindex="-1"}
    # usbguard list-rules
    ```

### [11.5. Creating a custom policy for USB devices](#creating-a-custom-policy-for-usb-devices) {#creating-a-custom-policy-for-usb-devices .title}

Create a custom USBGuard policy to meet your specific security requirements. By defining multiple rules, you gain fine-grained control over which USB devices are authorized to interact with your system.

**Prerequisites**

-   The `usbguard`{.literal} service is installed and running.
-   The `/etc/usbguard/rules.conf`{.literal} file contains an initial rule set generated by the `usbguard generate-policy`{.literal} command.

**Procedure**

1.  Create a policy which authorizes the currently connected USB devices, and store the generated rules to the `rules.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard generate-policy --no-hashes > ./rules.conf
    ```

    The `--no-hashes`{.literal} option does not generate hash attributes for devices. Avoid hash attributes in your configuration settings because they might not be persistent.

2.  In the `rules.conf`{.literal} file, add, remove, or edit the rules as required by using a text editor. For example, the following rule allows only devices with a single mass storage interface to interact with the system:

    ``` {.language-plaintext tabindex="-1"}
    allow with-interface equals { 08:*:* }
    ```

    See the `usbguard-rules.conf(5)`{.literal} man page for a detailed rule-language description and more examples.

3.  Install the updated policy:

    ``` {.language-plaintext tabindex="-1"}
    # install -m 0600 -o root -g root rules.conf /etc/usbguard/rules.conf
    ```

4.  Restart the `usbguard`{.literal} daemon to apply your changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart usbguard
    ```

**Verification**

1.  Check that your custom rules are in the active policy, for example:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard list-rules
    …
    4: allow with-interface 08:*:*
    …
    ```

### [11.6. Creating a structured custom policy for USB devices](#creating-a-structured-custom-policy-for-usb-devices) {#creating-a-structured-custom-policy-for-usb-devices .title}

Create a structured custom USBGuard policy in RHEL to manage complex security scenarios. By organizing rules into separate configuration files, you ensure easier maintenance and comprehensive security coverage.

You can organize your custom USBGuard policy in several `.conf`{.literal} files within the `/etc/usbguard/rules.d/`{.literal} directory. The `usbguard-daemon`{.literal} then combines the main `rules.conf`{.literal} file with the `.conf`{.literal} files within the directory in alphabetical order.

**Prerequisites**

-   The `usbguard`{.literal} service is installed and running.

**Procedure**

1.  Create a policy which authorizes the currently connected USB devices, and store the generated rules to a new `.conf`{.literal} file, for example, *`<policy.conf>`{.literal}*.

    ``` {.language-plaintext tabindex="-1"}
    # usbguard generate-policy --no-hashes > ./<policy.conf>
    ```

    The `--no-hashes`{.literal} option does not generate hash attributes for devices. Avoid hash attributes in your configuration settings because they might not be persistent.

2.  Open the *`<policy.conf>`{.literal}* file with a text editor of your choice, and select the lines with the rules that you want to record, for example:

    ``` {.language-plaintext tabindex="-1"}
    …
    allow id 04f2:0833 serial "" name "USB Keyboard" via-port "7-2" with-interface { 03:01:01 03:00:00 } with-connect-type "unknown"
    …
    ```

3.  Copy the selected lines into a separate `.conf`{.literal} file.

    Note

    The two digits at the beginning of the file name specify the order in which the daemon reads the configuration files.

    For example, to copy the rules for your keyboards into a new `.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # grep "USB Keyboard" ./<policy.conf> > ./<10keyboards.conf>
    ```

4.  Install the new policy to the `/etc/usbguard/rules.d/`{.literal} directory.

    ``` {.language-plaintext tabindex="-1"}
    # install -m 0600 -o root -g root <10keyboards.conf> /etc/usbguard/rules.d/<10keyboards.conf>
    ```

5.  Move the rest of the lines to the main `rules.conf`{.literal} file.

    ``` {.language-plaintext tabindex="-1"}
    # grep -v "USB Keyboard" ./policy.conf > ./rules.conf
    ```

6.  Install the remaining rules.

    ``` {.language-plaintext tabindex="-1"}
    # install -m 0600 -o root -g root rules.conf /etc/usbguard/rules.conf
    ```

7.  Restart the `usbguard`{.literal} daemon to apply your changes.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart usbguard
    ```

**Verification**

1.  Display all active USBGuard rules.

    ``` {.language-plaintext tabindex="-1"}
    # usbguard list-rules
    …
    15: allow id 04f2:0833 serial "" name "USB Keyboard" hash "kxM/iddRe/WSCocgiuQlVs6Dn0VEza7KiHoDeTz0fyg=" parent-hash "2i6ZBJfTl5BakXF7Gba84/Cp1gslnNc1DM6vWQpie3s=" via-port "7-2" with-interface { 03:01:01 03:00:00 } with-connect-type "unknown"
    …
    ```

2.  Display the contents of the `rules.conf`{.literal} file and all the `.conf`{.literal} files in the `/etc/usbguard/rules.d/`{.literal} directory.

    ``` {.language-plaintext tabindex="-1"}
    # cat /etc/usbguard/rules.conf /etc/usbguard/rules.d/*.conf
    ```

3.  Verify that the active rules contain all the rules from the files and are in the correct order.

### [11.7. Authorizing users and groups to use the USBGuard IPC interface](#authorizing-users-and-groups-to-use-the-usbguard-ipc-interface) {#authorizing-users-and-groups-to-use-the-usbguard-ipc-interface .title}

Authorize specific users or groups to use the USBGuard public IPC interface in RHEL to allow non-root management of USB devices. Grant access by using the `usbguard add-user`{.literal} subcommand or editing the configuration file to prevent unauthorized manipulation of USB device authorization policies.

**Prerequisites**

-   The `usbguard`{.literal} service is installed and running.
-   The `/etc/usbguard/rules.conf`{.literal} file contains an initial rule set generated by the `usbguard generate-policy`{.literal} command.

**Procedure**

1.  Edit the `/etc/usbguard/usbguard-daemon.conf`{.literal} file with the rules you want to add. For example, to allow all users in the `wheel`{.literal} group to use the IPC interface, add this line:

    ``` {.language-plaintext tabindex="-1"}
    IPCAllowGroups=wheel
    ```

2.  You can add users or groups also with the `usbguard`{.literal} command. For example, the following command enables a user to have full access to the `Devices`{.literal} and `Exceptions`{.literal} sections and to list and modify the current policy:

    ``` {.language-plaintext tabindex="-1"}
    # usbguard add-user <user_name> --devices ALL --policy modify,list --exceptions ALL
    ```

    Replace *`<user_name>`{.literal}* with the user name that should receive these permissions.

    You can remove the granted permissions for a user by using the `usbguard remove-user `{.literal}*`<user_name>`{.literal}* command.

3.  Restart the `usbguard`{.literal} daemon to apply your changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart usbguard
    ```

### [11.8. Logging USBguard authorization events to the Linux Audit log](#logging-usbguard-authorization-events-to-the-linux-audit-log) {#logging-usbguard-authorization-events-to-the-linux-audit-log .title}

By default, the `usbguard`{.literal} daemon logs events to the `/var/log/usbguard/usbguard-audit.log`{.literal} file. You can integrate logging of USBguard authorization events to the standard Linux Audit log.

**Prerequisites**

-   The `usbguard`{.literal} service is installed and running.
-   The `auditd`{.literal} service is running.

**Procedure**

1.  In the `/etc/usbguard/usbguard-daemon.conf`{.literal} file, change the `AuditBackend`{.literal} option from `FileAudit`{.literal} to `LinuxAudit`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    AuditBackend=LinuxAudit
    ```

2.  Restart the `usbguard`{.literal} daemon to apply the configuration change:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart usbguard
    ```

**Verification**

1.  Query the `audit`{.literal} daemon log for a USB authorization event, for example:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -ts recent -m USER_DEVICE
    ```

## [Legal Notice](#idm140263476979072) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
