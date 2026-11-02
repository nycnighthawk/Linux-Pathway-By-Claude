---
{"title": "Red Hat Enterprise Linux 10 Security Technical Implementation Guide", "url": "https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_RHEL_10_V1R3_STIG.zip", "retrieved": "2026-11-02", "license": "US-Gov-PD"}
---

# Red Hat Enterprise Linux 10 Security Technical Implementation Guide

## V-280094 RHEL 10 must disable the debug-shell systemd service. {#V-280094}

Severity: medium · Rule: SV-280094r1184607_rule · STIG ID: RHEL-10-700970 · CCI-002235

**Discussion.** The debug-shell requires no authentication and provides root privileges to anyone who has physical access to the machine. While this feature is disabled by default, masking it adds an additional layer of assurance that it will not be enabled via a dependency in systemd. This also prevents attackers with physical access from trivially bypassing security on the machine through valid troubleshooting configurations and gaining root access when the system is rebooted.

**Check.**

```
Verify RHEL 10 is configured to mask the debug-shell systemd service with the following command:

$ sudo systemctl status debug-shell.service
o debug-shell.service
        Loaded: masked (Reason: Unit debug-shell.service is masked.)
        Active: inactive (dead)

If the "debug-shell.service" is loaded and not masked, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mask the debug-shell systemd service with the following command:

$ sudo systemctl disable --now debug-shell.service
$ sudo systemctl mask --now debug-shell.service
```

## V-280931 RHEL 10 must ensure cryptographic verification of vendor software packages. {#V-280931}

Severity: medium · Rule: SV-280931r1268241_rule · STIG ID: RHEL-10-001020 · CCI-003992

**Discussion.** Cryptographic verification of vendor software packages ensures that all software packages are obtained from a valid source and protects against spoofing that could lead to installation of malware on the system. Red Hat cryptographically signs all software packages, including updates, with a GNU Privacy Guard (GPG) key to verify that they are valid.

**Check.**

```
Verify RHEL 10 ensures cryptographic verification of vendor software packages.

Confirm Red Hat package-signing keys are installed on the system and verify their fingerprints match vendor values.

Note: For RHEL 10 software packages, Red Hat uses GPG keys labeled "release key 2", "auxiliary key 3", and "release key 4". The keys are defined in key file "/etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release" by default.

List Red Hat GPG keys installed on the system:

$ sudo rpm -q --queryformat "%{SUMMARY}\n" gpg-pubkey | grep -i "red hat"
Red Hat, Inc. (release key 2) <security@redhat.com> public key
Red Hat, Inc. (auxiliary key 3) <security@redhat.com> public key
Red Hat, Inc. (release key 4) <security@redhat.com> public key

If Red Hat GPG keys "release key 2", "auxiliary key 3", and "release key 4" are not installed, or if the key file "/etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release" is missing, this is a finding.

List key fingerprints of installed Red Hat GPG keys:

$ sq inspect /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
/etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release: OpenPGP Certificate.

      Fingerprint: 567E347AD0044ADE55BA8A5F199E2F91FD431D51
  Public-key algo: RSA
  Public-key size: 4096 bits
    Creation time: 2009-10-22 11:59:55 UTC
        Key flags: certification, signing

           UserID: Red Hat, Inc. (release key 2) <security@redhat.com>

Note: There is another block of armored OpenPGP data.
Note: This is a non-standard extension to OpenPGP.

/etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release: OpenPGP Certificate.

      Fingerprint: 7E4624258C406535D56D6F135054E4A45A6340B3
  Public-key algo: RSA
  Public-key size: 4096 bits
    Creation time: 2022-03-09 21:56:46 UTC
        Key flags: certification, signing

           UserID: Red Hat, Inc. (auxiliary key 3) <security@redhat.com>

Note: There is another block of armored OpenPGP data.
Note: This is a non-standard extension to OpenPGP.

/etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release: OpenPGP Certificate.

      Fingerprint: FCD355B305707A62DA143AB6E422397E50FE8467A2A95343D246D6276AFEDF8F
  Public-key algo: ML-DSA-87+Ed448
    Creation time: 2025-10-08 17:40:03 UTC
        Key flags: certification, signing

           UserID: Red Hat, Inc. (release key 4) <security@redhat.com>

Compare key fingerprints of installed Red Hat GPG keys with fingerprints listed for RHEL 10 on the Red Hat "Product Signing Keys" webpage at https://access.redhat.com/security/team/key.

If key fingerprints do not match, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to ensure cryptographic verification of vendor software packages.

Install Red Hat package-signing keys on the system and verify their fingerprints match vendor values.

Insert the RHEL 10 installation disc or attach the RHEL 10 installation image to the system. Mount the disc or image to make the contents accessible inside the system.

Assuming the mounted location is "/media/cdrom", use the following command to copy the Red Hat GPG key file onto the system:

$ sudo cp /media/cdrom/RPM-GPG-KEY-redhat-release /etc/pki/rpm-gpg/

Import Red Hat GPG keys from the key file into the system keyring:

$ sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

Using the steps listed in the Check Text, confirm the newly imported keys show as installed on the system and verify their fingerprints match vendor values.
```

## V-280932 RHEL 10 must check the GNU Privacy Guard (GPG) signature of software packages originating from external software repositories before installation. {#V-280932}

Severity: high · Rule: SV-280932r1275251_rule · STIG ID: RHEL-10-001030 · CCI-003992

**Discussion.** Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and has been provided by a trusted vendor.

All software packages must be signed with a cryptographic key recognized and approved by the organization.

Verifying the authenticity of software prior to installation validates the integrity of the software package received from a vendor.

**Check.**

```
Verify RHEL 10 dnf always checks the GPG signature of software packages originating from external software repositories before installation with the following command:

$ sudo grep -w gpgcheck /etc/dnf/dnf.conf
gpgcheck=1

If "gpgcheck" is not set to either "1", "true", or "yes" (keywords containing letters are case insensitive), or if the option is missing or commented out, ask the system administrator how the GPG signatures of software packages are being verified.

If no process to verify GPG signatures has been approved by the organization, this is a finding.
```

**Fix.**

```
Configure RHEL 10 dnf to always check the GPG signature of software packages originating from external software repositories before installation.

Add or update the following line in the [main] section of the "/etc/dnf/dnf.conf" file:

gpgcheck=1

Note: Any of the following are acceptable: "1", "true", or "yes" (keywords containing letters are case insensitive).
```

## V-280933 RHEL 10 must check the GNU Privacy Guard (GPG) signature of locally installed software packages before installation. {#V-280933}

Severity: high · Rule: SV-280933r1275252_rule · STIG ID: RHEL-10-001040 · CCI-003992

**Discussion.** Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor.

All software packages must be signed with a cryptographic key recognized and approved by the organization.

Verifying the authenticity of software prior to installation validates the integrity of the software package received from a vendor.

**Check.**

```
Verify RHEL 10 dnf always checks the GPG signature of locally installed software packages before installation with the following command:

$ sudo grep localpkg_gpgcheck /etc/dnf/dnf.conf
localpkg_gpgcheck=1

If "localpkg_gpgcheck" is not set to either "1", "true", or "yes" (keywords containing letters are case insensitive), or if the option is missing or commented out, ask the system administrator how the GPG signatures of local software packages are being verified.

If no process to verify GPG signatures has been approved by the organization, this is a finding.
```

**Fix.**

```
Configure RHEL 10 dnf to always check the GPG signature of local software packages before installation.

Add or update the following line in the [main] section of the "/etc/dnf/dnf.conf" file:

localpkg_gpgcheck=1

Note: Any of the following are acceptable: "1", "true", or "yes" (keywords containing letters are case insensitive).
```

## V-280934 RHEL 10 must have GNU Privacy Guard (GPG) signature verification enabled for all software repositories. {#V-280934}

Severity: high · Rule: SV-280934r1275255_rule · STIG ID: RHEL-10-001050 · CCI-003992

**Discussion.** Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and has been provided by a trusted vendor.

All software packages must be signed with a cryptographic key recognized and approved by the organization.

Verifying the authenticity of software prior to installation validates the integrity of the software package received from a vendor.

**Check.**

```
Verify RHEL 10 software repositories defined in "/etc/yum.repos.d/" have been configured with "gpgcheck" enabled with the following command:

$ sudo grep -w gpgcheck /etc/yum.repos.d/*.repo | more
gpgcheck = 1

If "gpgcheck" for software packages and repositories is not set to either "1", "true", or "yes" (keywords containing letters are case insensitive), or if the option is missing or commented out, ask the system administrator how the GPG signatures of local software packages are being verified.

If no process to verify GPG signatures has been approved by the organization, this is a finding.
```

**Fix.**

```
Configure RHEL 10 software repositories defined in "/etc/yum.repos.d/" to have "gpgcheck" enabled with the following command:

$ sudo sed -i 's/gpgcheck\s*=.*/gpgcheck=1/g' /etc/yum.repos.d/*

Note: Any of the following are acceptable: "1", "true", or "yes" (keywords containing letters are case insensitive).
```

## V-280935 RHEL 10 must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information on local disk partitions that requires at-rest protection. {#V-280935}

Severity: high · Rule: SV-280935r1184775_rule · STIG ID: RHEL-10-000510 · CCI-002476 CCI-001199 CCI-002475

**Discussion.** RHEL 10 systems handling data that requires "data-at-rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest.

Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields).

Satisfies: SRG-OS-000405-GPOS-00184, SRG-OS-000185-GPOS-00079, SRG-OS-000404-GPOS-00183

**Check.**

```
Note: If there is a documented and approved reason for not having data-at-rest encryption at the operating system level, such as encryption provided by a hypervisor or a disk storage array in a virtualized environment, this requirement is not applicable.

Verify RHEL 10 prevents unauthorized disclosure or modification of all information requiring at-rest protection by using disk encryption.

List all block devices in tree-like format:

$ sudo lsblk --tree
NAME                                            MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
sda                                               8:0    0   64G  0 disk
+-sda1                                            8:1    0  600M  0 part  /boot/efi
+-sda2                                            8:2    0    1G  0 part  /boot
+-sda3                                            8:3    0 62.4G  0 part
  +-rhel-root                                   253:0    0   23G  0 lvm
  ¦ +-luks-9f886368-bf3e-4d17-86ed-a71dd6571bb4 253:2    0   23G  0 crypt /
  +-rhel-swap                                   253:1    0  6.4G  0 lvm   [SWAP]
  +-rhel-var_tmp                                253:3    0    3G  0 lvm
  ¦ +-luks-c98555c8-0462-4b97-9afa-6db8c4bfee3b 253:14   0    3G  0 crypt /var/tmp
  +-rhel-var_log_audit                          253:4    0   10G  0 lvm
  ¦ +-luks-4e45e1ad-5337-42c4-a19f-ee12ccc1d502 253:9    0   10G  0 crypt /var/log/audit
  +-rhel-tmp                                    253:5    0    2G  0 lvm
  ¦ +-luks-2d7e1b45-73c4-4282-8838-15a897e0d04e 253:11   0    2G  0 crypt /tmp
  +-rhel-home                                   253:6    0   10G  0 lvm
  ¦ +-luks-ca2261ed-7b00-4b7b-84cd-8cd6d8fa4b28 253:12   0   10G  0 crypt /home
  +-rhel-var                                    253:7    0    5G  0 lvm
  ¦ +-luks-51150299-f295-4145-b8f0-ebe9c6dfd5a0 253:13   0    5G  0 crypt /var
  +-rhel-var_log                                253:8    0    3G  0 lvm
    +-luks-c651f493-9fdc-4c6e-a711-0a4f03149661 253:10   0    3G  0 crypt /var/log

Verify that the block device tree for each persistent filesystem, excluding the /boot and /boot/efi filesystems, has at least one parent block device of type "crypt" and that the encryption type is LUKS:

$ sudo cryptsetup status luks-9f886368-bf3e-4d17-86ed-a71dd6571bb4
/dev/mapper/luks-9f886368-bf3e-4d17-86ed-a71dd6571bb4 is active and is in use.
  type:    LUKS2
  cipher:  aes-xts-plain64
  keysize: 512 bits
  key location: keyring
  device:  /dev/mapper/rhel-root
  sector size:  512
  offset:  32768 sectors
  size:    48201728 sectors
  mode:    read/write
  flags:   discards

If there are persistent filesystems (other than /boot or /boot/efi) whose block device trees do not have a crypt block device of type LUKS, ask the administrator to indicate how persistent filesystems are encrypted.

If there is no evidence that persistent filesystems are encrypted, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent unauthorized modification of all information at rest by using disk encryption.

Encrypting a partition in an already installed system is more difficult, because existing partitions will have to be resized and changed.

To encrypt an entire partition, dedicate a partition for encryption in the partition layout.
```

## V-280936 RHEL 10 must use a separate file system for the system audit data path. {#V-280936}

Severity: low · Rule: SV-280936r1184726_rule · STIG ID: RHEL-10-000520 · CCI-001849

**Discussion.** Placing "/var/log/audit" in its own partition enables better separation between audit files and other system files and helps ensure that auditing cannot be halted due to the partition running out of space.

**Check.**

```
Verify RHEL 10 uses a separate file system/partition for the system audit data path with the following command:

Note: /var/log/audit is used as the example as it is a common location.

$ mount | grep /var/log/audit
/dev/mapper/rootvg-varlogaudit on /var/log/audit type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota)
Note: Options displayed for mount may differ.

If no line is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use a separate file system for the system audit data path by migrating "/var/log/audit" onto a separate file system.
```

## V-280937 RHEL 10 must use a separate file system for user home directories (such as "/home" or an equivalent). {#V-280937}

Severity: medium · Rule: SV-280937r1184727_rule · STIG ID: RHEL-10-000530 · CCI-002385

**Discussion.** Ensuring that "/home" is mounted on its own partition enables the setting of more restrictive mount options and helps ensure that users cannot trivially fill partitions used for log or audit data storage.

**Check.**

```
Verify RHEL 10 uses a separate file system/partition for "/home" with the following command:

$ mount | grep /home
/dev/mapper/luks-ca2261ed-7b00-4b7b-84cd-8cd6d8fa4b28 on /home type xfs (rw,nodev,nosuid,noexec,seclabel)
Note: Options displayed for mount may differ.

If a separate entry for "/home" is not in use, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use a separate file system for user home directories by migrating the "/home" directory onto a separate file system/partition.
```

## V-280938 RHEL 10 must use a separate file system for "/tmp". {#V-280938}

Severity: medium · Rule: SV-280938r1184728_rule · STIG ID: RHEL-10-000540 · CCI-002385

**Discussion.** The "/tmp" partition is used as temporary storage by many programs. Placing "/tmp" in its own partition enables the setting of more restrictive mount options, which can help protect programs that use it.

**Check.**

```
Verify RHEL 10 uses a separate file system/partition for "/tmp" with the following command:

$ mount | grep /tmp
/dev/mapper/luks-2d7e1b45-73c4-4282-8838-15a897e0d04e on /tmp type xfs(rw,nodev,nosuid,noexec,seclabel)

Note: Options displayed for mount may differ.

If a separate entry for "/tmp" is not in use, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use a separate file system for temporary storage directories by migrating the "/tmp" path onto a separate file system.
```

## V-280939 RHEL 10 must use a separate file system for "/var". {#V-280939}

Severity: medium · Rule: SV-280939r1184729_rule · STIG ID: RHEL-10-000550 · CCI-002385

**Discussion.** Ensuring that "/var" is mounted on its own partition enables the setting of more restrictive mount options. This helps protect system services such as daemons or other programs that use it. It is not uncommon for the "/var" directory to contain world-writable directories installed by other software packages.

**Check.**

```
Verify RHEL 10 uses a separate file system/partition for "/var" with the following command:

$ mount | grep /var
/dev/mapper/luks-51150299-f295-4145-b8f0-ebe9c6dfd5a0 on /var type xfs (rw,nodev,relatime,seclabel,attr2)
Note: Options displayed for mount may differ.

If a separate entry for "/var" is not in use, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use a separate file system for the "/var" directory by migrating the "/var" path onto a separate file system.
```

## V-280940 RHEL 10 must use a separate file system for "/var/log". {#V-280940}

Severity: medium · Rule: SV-280940r1184730_rule · STIG ID: RHEL-10-000560 · CCI-002385

**Discussion.** Placing "/var/log" in its own partition enables better separation between log files and other files in "/var/".

**Check.**

```
Verify RHEL 10 uses a separate file system/partition for "/var/log" with the following command:

$ mount | grep /var/log
/dev/mapper/luks-c651f493-9fdc-4c6e-a711-0a4f03149661 on /var/log type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)
Note: Options displayed for mount may differ.

If a separate entry for "/var/log" is not in use, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use a separate file system for log file directories by migrating the "/var/log" path onto a separate file system.
```

## V-280941 RHEL 10 must use a separate file system for "/var/tmp". {#V-280941}

Severity: medium · Rule: SV-280941r1184731_rule · STIG ID: RHEL-10-000570 · CCI-002385

**Discussion.** The "/var/tmp" partition is used as temporary storage by many programs. Placing "/var/tmp" in its own partition enables the setting of more restrictive mount options, which can help protect programs that use it.

**Check.**

```
Verify RHEL 10 uses a separate file system/partition for "/var/tmp" with the following command:

$ mount | grep /var/tmp
/dev/mapper/luks-c98555c8-0462-4b97-9afa-6db8c4bfee3b on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)
Note: Options displayed for mount may differ.

If a separate entry for "/var/tmp" is not in use, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use a separate file system for the "/var/tmp" path by migrating "/var/tmp" onto a separate file system.
```

## V-280942 RHEL 10 must remove all software components after updated versions have been installed. {#V-280942}

Severity: medium · Rule: SV-280942r1275258_rule · STIG ID: RHEL-10-200000 · CCI-002617

**Discussion.** Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by some adversaries.

**Check.**

```
Verify RHEL 10 removes all software components after updated versions have been installed with the following command:

$ sudo grep -i clean_requirements_on_remove /etc/dnf/dnf.conf
clean_requirements_on_remove=True

If "clean_requirements_on_remove" is not set to either "1", "true", or "yes" (keywords containing letters are case insensitive), this is a finding.
```

**Fix.**

```
Configure RHEL 10 to remove all software components after updated versions have been installed.

Edit the file "/etc/dnf/dnf.conf" by adding or editing the following line:

 clean_requirements_on_remove=True

Note: Any of the following are acceptable: "1", "true", or "yes" (keywords containing letters are case insensitive).
```

## V-280943 RHEL 10 must not have the "nfs-utils" package installed. {#V-280943}

Severity: medium · Rule: SV-280943r1165184_rule · STIG ID: RHEL-10-200010 · CCI-000381

**Discussion.** The "nfs-utils" package provides a daemon for the kernel Network File System (NFS) server and related tools. This package also contains the "showmount" program. The "showmount" program queries the mount daemon on a remote host for information about the NFS server on the remote host. For example, "showmount" can display the clients that are mounted on that host.

**Check.**

```
Verify RHEL 10 does not have the "nfs-utils" package installed with the following command:

$ sudo dnf list --installed nfs-utils
Error: No matching Packages to list

If the "nfs-utils" package is installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have the "nfs-utils" package installed with the following command:

$ sudo dnf -y remove nfs-utils
```

## V-280944 RHEL 10 must not have the "telnet-server" package installed. {#V-280944}

Severity: high · Rule: SV-280944r1184749_rule · STIG ID: RHEL-10-200020 · CCI-000381

**Discussion.** It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities are often overlooked and therefore, may remain unsecure. They increase the risk to the platform by providing additional attack vectors.

The telnet service provides an unencrypted remote access service, which does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to log in using this service, the privileged user password could be compromised.

Removing the "telnet-server" package decreases the risk of accidental (or intentional) activation of the telnet service.

**Check.**

```
Verify RHEL 10 does not have the "telnet-server" package installed with the following command:

$ sudo dnf list --installed telnet-server
Error: No matching Packages to list

If the "telnet-server" package is installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have the "telnet-server" package installed with the following command:

$ sudo dnf -y remove telnet-server
```

## V-280945 RHEL 10 must not have the "gssproxy" package installed. {#V-280945}

Severity: medium · Rule: SV-280945r1184750_rule · STIG ID: RHEL-10-200030 · CCI-000381

**Discussion.** It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors.

Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations (e.g., key missions, functions).

The gssproxy package is a proxy for GSS API credential handling and could expose secrets on some networks. It is not needed for normal function of the operating system.

**Check.**

```
Note: If Network File System (NFS) mounts are authorized and in use on the system, this control is not applicable.

Verify RHEL 10 does not have the "gssproxy" package installed with the following command:

$ sudo dnf list --installed gssproxy
Error: No matching Packages to list

If the "gssproxy" package is installed and is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have the "gssproxy" package installed with the following command:

$ sudo dnf -y remove gssproxy
```

## V-280946 RHEL 10 must not have the tuned package installed. {#V-280946}

Severity: medium · Rule: SV-280946r1184751_rule · STIG ID: RHEL-10-200040 · CCI-000381

**Discussion.** It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors.

Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions).

The tuned package contains a daemon that tunes the system settings dynamically. It does so by monitoring the usage of several system components periodically. Based on that information, components will then be put into lower or higher power savings modes to adapt to the current usage. The tuned package is not needed for normal operating system operations.

**Check.**

```
Verify RHEL 10 does not have the tuned package installed with the following command:

$ sudo dnf list --installed tuned
Error: No matching Packages to list

If the "tuned" package is installed and is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have the tuned package installed with the following command:

$ sudo dnf -y remove tuned
```

## V-280948 RHEL 10 must not have the unbound package installed. {#V-280948}

Severity: medium · Rule: SV-280948r1197218_rule · STIG ID: RHEL-10-200060 · CCI-000381

**Discussion.** If the system is not a Domain Name Server (DNS), it should not have a DNS server package installed to decrease the attack surface of the system.

**Check.**

```
Verify RHEL 10 does not have a DNS package installed with the following command:

$ sudo dnf list --installed unbound
Error: No matching Packages to list

If the "unbound" package is installed, and the information system security officer lacks a documented requirement for a DNS, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have the unbound package installed with the following command:

$ sudo dnf -y remove unbound
```

## V-280949 RHEL 10 must not have the "tftp" package installed. {#V-280949}

Severity: high · Rule: SV-280949r1195338_rule · STIG ID: RHEL-10-200070 · CCI-000197

**Discussion.** It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities are often overlooked and therefore, may remain unsecure. They increase the risk to the platform by providing additional attack vectors.

If Trivial File Transfer Protocol (TFTP) is required for operational support (such as transmission of router configurations), its use must be documented with the information system security manager, restricted to only authorized personnel, and have access control rules established.

**Check.**

```
Verify RHEL 10 does not have the "tftp" package installed with the following command:

$ sudo dnf list --installed tftp
Error: No matching Packages to list

If the "tftp" package is installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have the "tftp" package installed with the following command:

$ sudo dnf -y remove tftp
```

## V-280950 RHEL 10 must not have the "gdm" package installed. {#V-280950}

Severity: medium · Rule: SV-280950r1165205_rule · STIG ID: RHEL-10-200080 · CCI-000381

**Discussion.** Unnecessary service packages must not be installed to decrease the attack surface of the system. A graphical environment is unnecessary for certain types of systems including a virtualization hypervisor.

**Check.**

```
Verify RHEL 10 does not have the "gdm" package installed with the following command:

$ sudo dnf list --installed gdm
Error: No matching Packages to list

If the "gdm" package is installed and the need for a GUI interface has not been documented with the information system security officer, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have the "gdm" package installed with the following command:

$ sudo dnf -y remove gdm
```

## V-280951 RHEL 10 must not have a File Transfer Protocol (FTP) server package installed. {#V-280951}

Severity: high · Rule: SV-280951r1273560_rule · STIG ID: RHEL-10-200090 · CCI-000197 CCI-000381

**Discussion.** The FTP service provides an unencrypted remote access that does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to log in using this service, the privileged user password could be compromised. Secure Shell (SSH) or other encrypted file transfer methods must be used in place of this service.

Removing the "vsftpd" package decreases the risk of accidental activation.

Satisfies: SRG-OS-000074-GPOS-00042, SRG-OS-000095-GPOS-00049

**Check.**

```
Verify RHEL 10 does not have an FTP server package installed with the following command:

$ sudo dnf list --installed vsftpd
Error: No matching Packages to list

If the "vsftpd" package is installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have the FTP package installed with the following command:

$ sudo dnf -y remove vsftpd
```

## V-280952 RHEL 10 must have the "subscription-manager" package installed. {#V-280952}

Severity: medium · Rule: SV-280952r1268241_rule · STIG ID: RHEL-10-200500 · CCI-003992

**Discussion.** The Red Hat Subscription Manager application manages software subscriptions and software repositories for installed software products on the local system. It communicates with backend servers, such as the Red Hat Customer Portal or an on-premise instance of Subscription Asset Manager, to register the local system and grant access to software resources determined by the subscription entitlement.

**Check.**

```
Note: If the system is not an internet connected system, this requirement is not applicable.

Verify RHEL 10 has the "subscription-manager" package installed with the following command:

$ sudo dnf list --installed subscription-manager
Installed Packages
subscription-manager.x86_64                      1.30.6.1-1.el10_0                       @rhel-10-for-x86_64-baseos-rpms

If the "subscription-manager" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "subscription-manager" package installed with the following command:

$ sudo dnf -y install subscription-manager
```

## V-280953 RHEL 10 must have the "nss-tools" package installed. {#V-280953}

Severity: medium · Rule: SV-280953r1195342_rule · STIG ID: RHEL-10-200510 · CCI-000381

**Discussion.** Network Security Services (NSS) is a set of libraries designed to support cross-platform development of security-enabled client and server applications. Install the "nss-tools" package to install command-line tools to manipulate the NSS certificate and key database.

**Check.**

```
Verify RHEL 10 has the "nss-tools" package installed with the following command:

$ sudo dnf list --installed nss-tools
Installed Packages
nss-tools.x86_64                           3.112.0-4.el10_0                           @rhel-10-for-x86_64-appstream-rpms

If the "nss-tools" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "nss-tools" package installed with the following command:

$ sudo dnf -y install nss-tools
```

## V-280954 RHEL 10 must have the "s-nail" package installed. {#V-280954}

Severity: medium · Rule: SV-280954r1195344_rule · STIG ID: RHEL-10-200520 · CCI-001744

**Discussion.** The "s-nail" package provides the mail command required to allow sending email notifications of unauthorized configuration changes to designated personnel.

**Check.**

```
Verify RHEL 10 is configured to allow sending email notifications.

Verify the "s-nail" package is installed on the system with the following command:

$ sudo dnf list --installed s-nail
Installed Packages
s-nail.x86_64                             14.9.24-12.el10                             @rhel-10-for-x86_64-appstream-rpms

If the "s-nail" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "s-nail" package installed with the following command:

$ sudo dnf -y install s-nail
```

## V-280955 RHEL 10 must have the "firewalld" package installed. {#V-280955}

Severity: medium · Rule: SV-280955r1273561_rule · STIG ID: RHEL-10-200530 · CCI-000382

**Discussion.** The "firewalld" package provides an easy and effective way to block/limit remote access to the system via ports, services, and protocols.

Remote access services, such as those providing remote access to network devices and information systems, that lack automated control capabilities increase risk and make remote user access management difficult at best.

Remote access is access to DoW nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganizational-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.

RHEL 10 functionality (e.g., Secure Shell [SSH]) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).

Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115, SRG-OS-000298-GPOS-00116, SRG-OS-000480-GPOS-00232

**Check.**

```
Verify RHEL 10 has the "firewalld" package installed.

Run the following command to determine if the "firewalld" package is installed:

$ dnf list --installed firewalld
Installed Packages
firewalld.noarch                             2.3.1-1.el10_0                              @rhel-10-for-x86_64-baseos-rpms

If the "firewall" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "firewalld" package installed with the following command:

$ sudo dnf -y install firewalld
```

## V-280956 RHEL 10 must have the "firewalld" service set to active. {#V-280956}

Severity: medium · Rule: SV-280956r1273562_rule · STIG ID: RHEL-10-200531 · CCI-000382 CCI-002314

**Discussion.** "Firewalld" provides an easy and effective way to block/limit remote access to the system via ports, services, and protocols.

Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best.

Remote access is access to DoW nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.

RHEL 10 functionality (e.g., Remote Desktop Protocol [RDP]) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).

Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115, SRG-OS-000480-GPOS-00232

**Check.**

```
Verify RHEL 10 is configured so that "firewalld" is active with the following command:

$ systemctl is-active firewalld
active

If the "firewalld" service is not active, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "firewalld" service set to active.

To enable the "firewalld" service, run the following command:

$ sudo systemctl enable --now firewalld
```

## V-280957 RHEL 10 must employ a deny-all, allow-by-exception policy for allowing connections to other systems. {#V-280957}

Severity: medium · Rule: SV-280957r1273563_rule · STIG ID: RHEL-10-200532 · CCI-002314

**Discussion.** Failure to restrict network connectivity only to authorized systems permits inbound connections from malicious systems. It also permits outbound connections that may facilitate exfiltration of DoW data.

RHEL 10 incorporates the "firewalld" daemon, which allows for many different configurations. One of these configurations is zones. Zones can be used in a deny-all, allow-by-exception approach. The default "drop" zone will drop all incoming network packets unless it is explicitly allowed by the configuration file or is related to an outgoing network connection.

**Check.**

```
Verify RHEL 10 is configured so that "firewalld" employs a deny-all, allow-by-exception policy for allowing connections to other systems with the following commands (using ens133 as an example interface):

$ sudo  firewall-cmd --state
running

$ sudo firewall-cmd --get-active-zones
drop (default)
   interfaces: ens33

$  sudo firewall-cmd --info-zone=drop | grep target
  target: DROP

$ sudo firewall-cmd --permanent --info-zone=drop | grep target
   target: DROP

If no zones are active on the RHEL 10 interfaces or if runtime and permanent targets are set to an option other than "DROP", this is a finding.

Verify the permanent configuration is valid and there are no misconfigured zones or rules with the following command:

$ sudo firewall-cmd --check-config
success

If this command does not return "success", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the "firewalld" daemon employs a deny-all, allow-by-exception policy with the following commands (using ens133 as an example interface):

Start by adding the exceptions that are required for mission functionality to the "drop" zone. If SSH access on port 22 is needed, for example, run the following: 

$ sudo firewall-cmd --permanent --add-service=ssh --zone=drop

Reload the firewall rules to update the runtime configuration from the "--permanent" changes made above:

$ sudo firewall-cmd --reload

Set the default zone to the drop zone:

$ sudo firewall-cmd --set-default-zone=drop
Note: This is a runtime and permanent change.

Add any interfaces to the newly modified "drop" zone:

$ sudo firewall-cmd --permanent --zone=drop --change-interface=ens33

Reload the firewall rules for changes to take effect:

$ sudo firewall-cmd --reload
```

## V-280958 RHEL 10 must have the "chrony" package installed. {#V-280958}

Severity: medium · Rule: SV-280958r1195348_rule · STIG ID: RHEL-10-200540 · CCI-004923

**Discussion.** Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate.

**Check.**

```
Verify RHEL 10 has the "chrony" package installed with the following command:

$ sudo dnf list --installed chrony
Installed Packages
chrony.x86_64                                           4.6.1-1.el10                                           @anaconda

If the "chrony" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "chrony" package installed with the following command:

$ sudo dnf -y install chrony
```

## V-280959 RHEL 10 must enable the chronyd service. {#V-280959}

Severity: medium · Rule: SV-280959r1165232_rule · STIG ID: RHEL-10-200541 · CCI-004923

**Discussion.** Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate.

Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.

**Check.**

```
Verify RHEL 10 sets the chronyd service to active with the following command:

$ systemctl is-active chronyd
active

If the chronyd service is not active, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable the chronyd service with the following command:

$ sudo systemctl enable --now chronyd
```

## V-280960 RHEL 10 must disable the chrony daemon from acting as a server. {#V-280960}

Severity: medium · Rule: SV-280960r1165235_rule · STIG ID: RHEL-10-200542 · CCI-000382 CCI-000381

**Discussion.** Minimizing the exposure of the server functionality of the chrony daemon diminishes the attack surface.

Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000095-GPOS-00049

**Check.**

```
Verify RHEL 10 disables the chrony daemon from acting as a server with the following command:

$ sudo grep -w port /etc/chrony.conf
port 0

If the "port" option is not set to "0", is commented out, or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable the chrony daemon from acting as a server by adding/modifying the following line in the "/etc/chrony.conf" file:

port 0

Restart the chronyd service with the following command for the changes to take effect:

$ sudo systemctl restart chronyd
```

## V-280961 RHEL 10 must disable network management of the chrony daemon. {#V-280961}

Severity: medium · Rule: SV-280961r1165238_rule · STIG ID: RHEL-10-200543 · CCI-000382 CCI-000381

**Discussion.** Not exposing the management interface of the chrony daemon on the network diminishes the attack space.

Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000095-GPOS-00049

**Check.**

```
Verify RHEL 10 disables network management of the chrony daemon with the following command:

$ sudo grep -w cmdport /etc/chrony.conf
cmdport 0

If the "cmdport" option is not set to "0", is commented out, or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable network management of the chrony daemon by adding/modifying the following line in the "/etc/chrony.conf" file:

cmdport 0

Restart the chronyd service with the following command for the changes to take effect:

$ sudo systemctl restart chronyd
```

## V-280962 RHEL 10 must have the USBGuard package installed. {#V-280962}

Severity: medium · Rule: SV-280962r1195350_rule · STIG ID: RHEL-10-200560 · CCI-001958

**Discussion.** The USBGuard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the "usbguard-rules.conf" file. The policy and the authorization state of USB devices can be modified during runtime using the USBGuard tool.

The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.

**Check.**

```
Verify RHEL 10 has USBGuard installed on the operating system with the following command:

$ sudo dnf list --installed usbguard
Installed Packages
usbguard.x86_64                             1.1.3-6.el10                              @rhel-10-for-x86_64-appstream-rpms

If the USBGuard package is not installed, ask the SA to indicate how unauthorized peripherals are being blocked.

If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.

If the system is a virtual machine with no virtual or physical USB peripherals attached, this is not a finding.
```

**Fix.**

```
Configure RHEL 10 to have the USBGuard package installed with the following command:

$ sudo dnf -y install usbguard

Enable the service to start on boot and then start it with the following commands:

$ sudo systemctl enable usbguard
$ sudo systemctl start usbguard

Verify the status of the service with the following command:

$ sudo systemctl status usbguard

Note: USBGuard must be configured to allow authorized devices once it is enabled on RHEL 10.
```

## V-280963 RHEL 10 must have the USBGuard package enabled. {#V-280963}

Severity: medium · Rule: SV-280963r1165244_rule · STIG ID: RHEL-10-200561 · CCI-001958 CCI-003959

**Discussion.** The USBGuard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the "usbguard-rules.conf" file. The policy and the authorization state of USB devices can be modified during runtime using the USBGuard tool.

The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.

Satisfies: SRG-OS-000378-GPOS-00163, SRG-OS-000690-GPOS-00140

**Check.**

```
Note: If the system is virtual machine with no virtual or physical USB peripherals attached, this is not applicable.

Verify RHEL 10 has USBGuard enabled with the following command:

$ systemctl is-active usbguard
active

If USBGuard is not active, ask the SA to indicate how unauthorized peripherals are being blocked.

If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the USBGuard service enabled by running the following command:

$ sudo systemctl enable --now usbguard
```

## V-280964 RHEL 10 must block unauthorized peripherals before establishing a connection. {#V-280964}

Severity: medium · Rule: SV-280964r1165247_rule · STIG ID: RHEL-10-200562 · CCI-001958

**Discussion.** The USBGuard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the "usbguard-rules.conf" file. The policy and the authorization state of USB devices can be modified during runtime using the usbguard tool.

The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.

**Check.**

```
Note: If the system is virtual machine with no virtual or physical USB peripherals attached, this is not applicable.

Verify RHEL 10 USBGuard has a policy configured.

Confirm the setting with the following command:

$ sudo usbguard list-rules
allow id 1d6b:0001 serial

If the command does not return results, or an error is returned, ask the SA to indicate how unauthorized peripherals are being blocked.

If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable the blocking of unauthorized peripherals with the following command:

Note: This command must be run from a root shell and will create an allowlist for any USB devices currently connected to the system.

# usbguard generate-policy --no-hash > /etc/usbguard/rules.conf

Note: Enabling and starting usbguard without properly configuring it for an individual system will immediately prevent any access over a USB device such as a keyboard or mouse.
```

## V-280965 RHEL 10 must enable audit logging for the USBGuard daemon. {#V-280965}

Severity: medium · Rule: SV-280965r1273564_rule · STIG ID: RHEL-10-200563 · CCI-000169 CCI-000172

**Discussion.** Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records.

DoW has defined the list of events for which RHEL 10 will provide an audit record generation capability as the following:

1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels).

2) Access actions, such as successful and unsuccessful login attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logins from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system.

3) All account creations, modifications, disabling, and terminations.

4) All kernel module load, unload, and restart actions.

Satisfies: SRG-OS-000062-GPOS-00031, SRG-OS-000471-GPOS-00215

**Check.**

```
Note: If the system is a virtual machine with no virtual or physical USB peripherals attached, this is not applicable.

Verify RHEL 10 audit logging is enabled for the USBGuard daemon. 

Confirm the setting with the following command:

$ sudo grep AuditBackend /etc/usbguard/usbguard-daemon.conf
AuditBackend=LinuxAudit

If "AuditBackend" is not set to "LinuxAudit", this is a finding.
```

**Fix.**

```
Configure RHEL 10 USBGuard AuditBackend to use the audit system.

Add or edit the following line in "/etc/usbguard/usbguard-daemon.conf":

AuditBackend=LinuxAudit
```

## V-280966 RHEL 10 must have the "policycoreutils" package installed. {#V-280966}

Severity: medium · Rule: SV-280966r1195352_rule · STIG ID: RHEL-10-200570 · CCI-001084

**Discussion.** Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. 

Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters.

The "policycoreutils" package contains the policy core utilities that are required for basic operation of an SELinux-enabled system. These utilities include "load_policy" to load SELinux policies, "setfile" to label filesystems, "newrole" to switch roles, and "run_init" to run "/etc/init.d" scripts in the proper context.

**Check.**

```
Verify RHEL 10 has the "policycoreutils" package installed with the following command:

$ sudo dnf list --installed policycoreutils
Installed Packages
policycoreutils.x86_64                                       3.8-1.el10                                        @anaconda

If the "policycoreutils" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "policycoreutils" package installed with the following command:

$ sudo dnf -y install policycoreutils
```

## V-280967 RHEL 10 must have the "policycoreutils-python-utils" package installed. {#V-280967}

Severity: medium · Rule: SV-280967r1195354_rule · STIG ID: RHEL-10-200580 · CCI-000381

**Discussion.** The "policycoreutils-python-utils" package is required to operate and manage an SELinux environment and its policies. It provides utilities such as "semanage", "audit2allow", "audit2why", "chcat", and "sandbox".

**Check.**

```
Verify RHEL 10 has the "policycoreutils-python-utils" service package installed with the following command:

$ sudo dnf list --installed policycoreutils-python-utils
Installed Packages
policycoreutils-python-utils.noarch                                3.8-1.el10                                 @AppStream

If the "policycoreutils-python-utils" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "policycoreutils-python-utils" service package installed with the following command:

$ sudo dnf -y install policycoreutils-python-utils
```

## V-280968 RHEL 10 must have the "sudo" package installed. {#V-280968}

Severity: medium · Rule: SV-280968r1195356_rule · STIG ID: RHEL-10-200590 · CCI-002235

**Discussion.** The "sudo" package is a program designed to allow a system administrator to give limited root privileges to users and log root activity. The basic philosophy is to give as few privileges as possible but still allow system users to complete their work.

**Check.**

```
Verify RHEL 10 has the "sudo" package installed with the following command:

$ sudo dnf list --installed sudo
Installed Packages
sudo.x86_64                             1.9.15-8.p5.el10_0.2                             @rhel-10-for-x86_64-baseos-rpms

If the "sudo" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "sudo" package installed with the following command:

$ sudo dnf -y install sudo
```

## V-280969 RHEL 10 must have the "fapolicy" module installed. {#V-280969}

Severity: medium · Rule: SV-280969r1195358_rule · STIG ID: RHEL-10-200600 · CCI-001774 CCI-001764

**Discussion.** The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as allowlisting.

Using an allowlist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. Verification of allowlisted software occurs prior to execution or at system startup.

User home directories/folders may contain information of a sensitive nature. Nonprivileged users should coordinate any sharing of information with a system administrator through shared resources.

RHEL 10 ships with many optional packages. One such package is a file access policy daemon called "fapolicyd". This is a userspace daemon that determines access rights to files based on attributes of the process and file. It can be used to either blocklist or allowlist processes or file access.

Proceed with caution with enforcing the use of this daemon. Improper configuration may render the system nonfunctional. The "fapolicyd" API is not namespace aware and can cause issues when launching or running containers.

Satisfies: SRG-OS-000370-GPOS-00155, SRG-OS-000368-GPOS-00154

**Check.**

```
Verify RHEL 10 has the "fapolicyd" package installed with the following command:

$ sudo dnf list --installed fapolicyd
Installed Packages
fapolicyd.x86_64                            1.3.3-102.el10                            @rhel-10-for-x86_64-appstream-rpms

If the "fapolicyd" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "fapolicyd" package installed with the following command:

$ sudo dnf -y install fapolicyd
```

## V-280970 RHEL 10 must enable the "fapolicy" module. {#V-280970}

Severity: medium · Rule: SV-280970r1165265_rule · STIG ID: RHEL-10-200601 · CCI-001774 CCI-001764

**Discussion.** The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as allowlisting.

Using an allowlist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. Verification of allowlisted software occurs prior to execution or at system startup.

User home directories/folders may contain information of a sensitive nature. Nonprivileged users should coordinate any sharing of information with a system administrator through shared resources.

RHEL 10 ships with many optional packages. One such package is a file access policy daemon called "fapolicyd". The "fapolicyd" is a userspace daemon that determines access rights to files based on attributes of the process and file. It can be used to either blocklist or allowlist processes or file access.

Proceed with caution with enforcing the use of this daemon. Improper configuration may render the system nonfunctional. The "fapolicyd" application programming interface (API) is not namespace aware and can cause issues when launching or running containers.

Satisfies: SRG-OS-000370-GPOS-00155, SRG-OS-000368-GPOS-00154

**Check.**

```
Verify RHEL 10 "fapolicyd" is active with the following command:

$ systemctl is-active fapolicyd
active

If the "fapolicyd" module is not active, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable "fapolicyd" with the following command:

$ systemctl enable --now fapolicyd
```

## V-280971 RHEL 10 must be configured to employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs. {#V-280971}

Severity: medium · Rule: SV-280971r1184780_rule · STIG ID: RHEL-10-200602 · CCI-001764 CCI-001774

**Discussion.** The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as allowlisting.

Using an allowlist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. Verification of allowlisted software occurs prior to execution or at system startup.

User home directories/folders may contain information of a sensitive nature. Nonprivileged users should coordinate any sharing of information with a system administrator through shared resources.

RHEL 10 ships with many optional packages. One such package is a file access policy daemon called "fapolicyd". The "fapolicyd" is a userspace daemon that determines access rights to files based on attributes of the process and file. It can be used to either block list or allowlist processes or file access.

Proceed with caution with enforcing the use of this daemon. Improper configuration may render the system nonfunctional. The "fapolicyd" application programming interface (API) is not namespace aware and can cause issues when launching or running containers.

Satisfies: SRG-OS-000368-GPOS-00154, SRG-OS-000370-GPOS-00155

**Check.**

```
Verify the RHEL 10 "fapolicyd" employs a deny-all, permit-by-exception policy.

Check that "fapolicyd" is in enforcement mode with the following command:

$ sudo grep permissive /etc/fapolicyd/fapolicyd.conf

permissive = 0

If "fapolicyd" is not running in enforcement mode, this is a finding.

Check that "fapolicyd" employs a deny-all policy on system mounts with the following commands:

$ sudo tail /etc/fapolicyd/compiled.rules

allow exe=/usr/bin/python3.7 : ftype=text/x-python
deny_audit perm=any pattern=ld_so : all
deny perm=any all : all

If "fapolicyd" is not running with a deny-all, permit-by-exception policy, this is a finding.

Note: "deny_log" or "deny_audit" options meet the security requirements. These options will generate higher volumes of logs.
```

**Fix.**

```
Configure RHEL 10 to employ a deny-all, permit-by-exception application allow listing policy with "fapolicyd".

With the "fapolicyd" installed and enabled, configure the daemon to function in permissive mode until the allow list is built correctly to avoid system lockout. Do this by editing the "/etc/fapolicyd/fapolicyd.conf" file with the following line:

permissive = 1

Build the allow list in a file within the "/etc/fapolicyd/rules.d" directory, ensuring the last rule implements a deny-all policy, such as "deny perm=any all : all".

Once it is determined the allow list is built correctly, set the "fapolicyd" to enforcing mode by editing the "permissive" line in the /etc/fapolicyd/fapolicyd.conf file.

permissive = 0
```

## V-280972 RHEL 10 must have the "pcsc-lite" package installed. {#V-280972}

Severity: medium · Rule: SV-280972r1268242_rule · STIG ID: RHEL-10-200610 · CCI-004046

**Discussion.** The "pcsc-lite" package must be installed if it is to be available for multifactor authentication using smart cards.

**Check.**

```
Note: If the system administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable.

Verify RHEL 10 has the "pcsc-lite" package installed with the following command:

$ sudo dnf list --installed pcsc-lite
Installed Packages
pcsc-lite.x86_64                                         2.2.3-2.el10                                          @anaconda

If the "pcsc-lite" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "pcsc-lite" package installed with the following command:

$ sudo dnf -y install pcsc-lite
```

## V-280973 RHEL 10 must have the "pcscd" socket set to active. {#V-280973}

Severity: medium · Rule: SV-280973r1268242_rule · STIG ID: RHEL-10-200611 · CCI-004046

**Discussion.** The information system ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device.

The daemon program for pcsc-lite and the MuscleCard framework is pcscd. It is a resource manager that coordinates communications with smart card readers and smart cards and cryptographic tokens that are connected to the system.

**Check.**

```
Verify RHEL 10 has the "pcscd" socket set to active with the following command:

$ systemctl is-active pcscd.socket
active

If the "pcscd" socket is not active, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "pcscd" socket set to active with the following command:

$ sudo systemctl enable --now pcscd.socket
```

## V-280974 RHEL 10 must have the "pcsc-lite-ccid" package installed. {#V-280974}

Severity: medium · Rule: SV-280974r1268242_rule · STIG ID: RHEL-10-200612 · CCI-004046

**Discussion.** The "pcsc-lite-ccid" package must be installed if it is to be available for multifactor authentication using smart cards.

**Check.**

```
Verify RHEL 10 has the "pcsc-lite-ccid" package installed with the following command:

$ sudo dnf list --installed pcsc-lite-ccid
Installed Packages
pcsc-lite-ccid.x86_64                                       1.6.0-2.el10                                       @anaconda

If the "pcsc-lite-ccid" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "pcsc-lite-ccid" package installed with the following command:

$ sudo dnf -y install pcsc-lite-ccid
```

## V-280975 RHEL 10 must have the "opensc" package installed. {#V-280975}

Severity: medium · Rule: SV-280975r1273565_rule · STIG ID: RHEL-10-200620 · CCI-004046 CCI-001953

**Discussion.** The use of Personal Identity Verification (PIV) credentials facilitates standardization and reduces the risk of unauthorized access.

The DoW has mandated the use of the common access card (CAC) to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems.

Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000376-GPOS-00161

**Check.**

```
Verify RHEL 10 has the "opensc" package installed with the following command:

$ sudo dnf list --installed opensc
Installed Packages
opensc.x86_64                               0.26.1-1.el10                                @rhel-10-for-x86_64-baseos-rpm

If the "opensc" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "opensc" package installed with the following command:

$ sudo dnf -y install opensc
```

## V-280976 RHEL 10 must use the common access card (CAC) smart card driver. {#V-280976}

Severity: medium · Rule: SV-280976r1165283_rule · STIG ID: RHEL-10-200621 · CCI-000764 CCI-000766 CCI-000765 CCI-004045

**Discussion.** Smart card login provides two-factor authentication stronger than that provided by a username and password combination. Smart cards leverage public key infrastructure to provide and verify credentials. Configuring the smart card driver helps to prevent the use of unauthorized smart cards.

Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000109-GPOS-00056, SRG-OS-000108-GPOS-00055

**Check.**

```
Verify RHEL 10 loads the CAC driver with the following command:

$ sudo opensc-tool --get-conf-entry app:default:card_drivers
cac

If "cac" is not listed as a card driver, or no line is returned for "card_drivers", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to load the CAC driver:

$ sudo opensc-tool --set-conf-entry app:default:card_drivers:cac

Restart the pcscd service with the following command for the changes to take effect:

$ sudo systemctl restart pcscd
```

## V-280977 RHEL 10 must have the Advanced Intrusion Detection Environment (AIDE) package installed. {#V-280977}

Severity: medium · Rule: SV-280977r1195366_rule · STIG ID: RHEL-10-200630 · CCI-002696

**Discussion.** Without verification of the security functions, security functions may not operate correctly, and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. 

Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (e.g., permissions, privileges), setting events to be audited, and setting intrusion detection parameters.

**Check.**

```
Verify RHEL 10 has the AIDE package installed with the following command:

$ sudo dnf list --installed aide
Installed Packages
aide.x86_64                             0.18.6-8.el10_0.2                             @rhel-10-for-x86_64-appstream-rpms

If AIDE is not installed, ask the system administrator how file integrity checks are performed on the system.

If no application is installed to perform integrity checks, this is a finding.

If AIDE is installed, determine if it has been initialized with the following command:

$ sudo /usr/sbin/aide --check

If the output is "Couldn't open file /var/lib/aide/aide.db.gz for reading", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that "AIDE" is installed and initialized, and then perform a manual check.

Install AIDE:

$ sudo dnf -y install aide

Initialize AIDE:

$ sudo /usr/sbin/aide --init

Example output:

Start timestamp: 2025-04-03 10:09:04 -0600 (AIDE 0.16)
AIDE initialized database at /var/lib/aide/aide.db.new.gz

Number of entries:      86833

---------------------------------------------------
The attributes of the (uncompressed) database(s):
---------------------------------------------------

/var/lib/aide/aide.db.new.gz
  MD5      : coZUtPHhoFoeD7+k54fUvQ==
  SHA1     : DVpOEMWJwo0uPgrKZAygIUgSxeM=
  SHA256   : EQiZH0XNEk001tcDmJa+5STFEjDb4MPE
             TGdBJ/uvZKc=
  SHA512   : 86KUqw++PZhoPK0SZvT3zuFq9yu9nnPP
             toei0nENVELJ1LPurjoMlRig6q69VR8l
             +44EwO9eYyy9nnbzQsfG1g==

End timestamp: 2025-04-03 10:09:57 -0600 (run time: 0m 53s)

The new database must be renamed to be read by AIDE:

$ sudo mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz

Perform a manual check:

$ sudo /usr/sbin/aide --check

Example output:

2025-04-03 10:16:08 -0600 (AIDE 0.16)
AIDE found NO differences between database and filesystem. Looks okay!!

...
```

## V-280978 RHEL 10 must use cryptographic mechanisms to protect the integrity of audit tools. {#V-280978}

Severity: high · Rule: SV-280978r1165289_rule · STIG ID: RHEL-10-200631 · CCI-001496

**Discussion.** Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.

Audit tools include, but are not limited to, vendor-provided and open-source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.

It is not uncommon for attackers to replace the audit tools or inject code into the existing tools to provide the capability to hide or erase system activity from the audit logs.

To address this risk, audit tools must be cryptographically signed to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.

**Check.**

```
Verify RHEL 10 Advanced Intrusion Detection Environment (AIDE) is properly configured to protect the integrity of the audit tools.

Verify the explicit rules for the audit tools with the following command:

$ sudo grep /usr/sbin/au /etc/aide.conf
/usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512

If AIDE is not installed, ask the system administrator (SA) how file integrity checks are performed on the system.

If any of the audit tools listed above do not have a corresponding line, ask the SA to indicate what cryptographic mechanisms are being used to protect the integrity of the audit tools.

If there is no evidence of integrity protection, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use cryptographic mechanisms to protect the integrity of audit tools.

Add or update the following lines to "/etc/aide.conf" to protect the integrity of the audit tools.

/usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512
```

## V-280979 RHEL 10 must use a file integrity tool that is configured to use FIPS 140-3-approved cryptographic hashes for validating file contents and directories. {#V-280979}

Severity: medium · Rule: SV-280979r1165292_rule · STIG ID: RHEL-10-200632 · CCI-002475

**Discussion.** RHEL 10 installation media ships with an optional file integrity tool called Advanced Intrusion Detection Environment (AIDE). AIDE is highly configurable at install time. This requirement assumes the "aide.conf" file is under the "/etc" directory.

File integrity tools use cryptographic hashes for verifying that file contents and directories have not been altered. These hashes must be FIPS 140-3-approved cryptographic hashes.

**Check.**

```
Verify RHEL 10 AIDE is configured to use FIPS 140-3 file hashing.

Verify global default hash settings with the following command:

$ sudo grep -iE 'sha|md5|rmd' /etc/aide.conf | grep -v ^#
FIPSR = p+i+n+u+g+s+m+ftype+growing+acl+selinux+xattrs+sha512
ALLXTRAHASHES = sha512
/usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512
NORMAL = FIPSR+sha512
LSPP = FIPSR+sha512
DATAONLY =  R+sha512
/etc/gshadow  NORMAL
/etc/shadow   NORMAL

If any hashes other than "sha512" are present, this is a finding.

Confirm no legacy hashes exist with the following command:

$ sudo grep -iE 'md5|sha1|whirlpool|tiger' /etc/aide.conf | grep -v ^#

If any uncommented lines are returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the file integrity tool uses FIPS 140-3 cryptographic hashes for validating file and directory contents.

If AIDE is installed, ensure the "sha512" rule is present on all uncommented file and directory selection lists, and that no legacy hashes exist. 

By default, AIDE excludes log files such as "/var/log" and other volatile files to reduce unnecessary notifications.
```

## V-280980 RHEL 10 must routinely check the baseline configuration for unauthorized changes and notify the system administrator when anomalies in the operation of any security functions are discovered. {#V-280980}

Severity: medium · Rule: SV-280980r1165295_rule · STIG ID: RHEL-10-200633 · CCI-001744 CCI-002699 CCI-002702

**Discussion.** Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security.

Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's information management officer (IMO)/information system security officer (ISSO) and system administrators (SAs) must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item.

Notifications provided by information systems include messages to local computer consoles and/or hardware indications such as lights.

This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection.

Satisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000446-GPOS-00200, SRG-OS-000447-GPOS-00201

**Check.**

```
Verify RHEL 10 routinely executes a file integrity scan for changes to the system baseline. The command used in the example will use a daily occurrence.

Check the cron directories for scripts controlling the execution and notification of results of the file integrity application. For example, if AIDE is installed on the system, use the following commands:

$ sudo ls -al /etc/cron.* | grep aide
-rwxr-xr-x 1 root root 29 Nov 22 2015 aide

$ sudo grep aide /etc/crontab /var/spool/cron/root
/etc/crontab: 30 04 * * * root usr/sbin/aide
/var/spool/cron/root: 30 04 * * * root usr/sbin/aide

$ sudo more /etc/cron.daily/aide
#!/bin/bash
/usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily aide integrity check run" root@sysname.mil

If the file integrity application does not exist, a script file controlling the execution of the file integrity application does not exist, or the file integrity application does not notify designated personnel of changes, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to automatically run the file integrity tool on the system at least weekly and notify designated personnel if baseline configurations are changed in an unauthorized manner. 

The AIDE tool can be configured to email designated personnel with the use of the cron system.

The following example output is generic. It will set cron to run AIDE daily and to send email at the completion of the analysis:

$ sudo more /etc/cron.daily/aide

#!/bin/bash
/usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily aide integrity check run" root@sysname.mil
```

## V-280981 RHEL 10 must be configured so that the file integrity tool verifies Access Control Lists (ACLs). {#V-280981}

Severity: medium · Rule: SV-280981r1165298_rule · STIG ID: RHEL-10-200634 · CCI-002475

**Discussion.** RHEL 10 installation media ships with an optional file integrity tool called Advanced Intrusion Detection Environment (AIDE). AIDE is highly configurable at install time. This requirement assumes the "aide.conf" file is under the "/etc" directory.

ACLs can provide permissions beyond those permitted through the file mode and must be verified by the file integrity tools.

**Check.**

```
Verify RHEL 10 AIDE is verifying ACLs.

Verify ACL settings for all uncommented file and directory selection lists with the following command:

$ sudo grep -E '^[^#]*acl' /etc/aide.conf
FIPSR = p+i+n+u+g+s+m+growing+acl+selinux+xattrs+sha512
/usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512
DIR = p+i+n+u+g+acl+selinux+xattrs
PERMS = p+i+u+g+acl+selinux

Open the file and verify no additional uncommented file and directory selection lines are missing the "acl" rule.

If the "acl" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or ACLs are not being checked by another file integrity tool, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the file integrity tool checks file and directory ACLs.

If AIDE is installed, ensure the "acl" rule is present on all uncommented file and directory selection lists.
```

## V-280982 RHEL 10 must be configured so that the file integrity tool verifies extended attributes. {#V-280982}

Severity: medium · Rule: SV-280982r1165301_rule · STIG ID: RHEL-10-200635 · CCI-002475

**Discussion.** RHEL 10 installation media ships with an optional file integrity tool called Advanced Intrusion Detection Environment (AIDE). AIDE is highly configurable at install time. This requirement assumes the "aide.conf" file is under the "/etc" directory.

Extended attributes in file systems are used to contain arbitrary data and file metadata with security implications.

**Check.**

```
Verify RHEL 10 AIDE is configured to verify extended attributes with the following command:

$ sudo grep -E '^[^#]*xattrs' /etc/aide.conf
FIPSR = p+i+n+u+g+s+m+growing+acl+selinux+xattrs+sha512
/usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512
/usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512
DIR = p+i+n+u+g+acl+selinux+xattrs

Open the file and verify that no additional uncommented file and directory selection lines are missing the "xattrs" rule.

If the "xattrs" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or extended attributes are not being checked by another file integrity tool, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the file integrity tool checks file and directory extended attributes.

If AIDE is installed, ensure the "xattrs" rule is present on all uncommented file and directory selection lists.
```

## V-280983 RHEL 10 must have the "rsyslog" package installed. {#V-280983}

Severity: medium · Rule: SV-280983r1273566_rule · STIG ID: RHEL-10-200640 · CCI-001851 CCI-000154

**Discussion.** The "rsyslogd" is a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support local and remote logging. Couple this utility with "gnutls" (which is a secure communications library implementing the Secure Sockets Layer [SSL], Transport Layer Security [TLS], and Datagram TLS [DTLS] protocols), to create a method to securely encrypt and off-load auditing.

Satisfies: SRG-OS-000479-GPOS-00224, SRG-OS-000051-GPOS-00024

**Check.**

```
Verify RHEL 10 has the "rsyslog" package installed with the following command:

$ sudo dnf list --installed rsyslog
Installed Packages
rsyslog.x86_64                                        8.2412.0-1.el10                                         @AppStream

If the "rsyslog" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "rsyslog" package installed with the following command:

$ sudo dnf -y install rsyslog
```

## V-280984 RHEL 10 must have the rsyslog service set to active. {#V-280984}

Severity: medium · Rule: SV-280984r1165307_rule · STIG ID: RHEL-10-200641 · CCI-000133

**Discussion.** The rsyslog service must be running to provide logging services, which are essential to system administration.

**Check.**

```
Verify RHEL 10 rsyslog is active with the following command:

$ systemctl is-active rsyslog
active

If the rsyslog service is not active, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable the rsyslog service with the following command:

$ sudo systemctl enable --now rsyslog
```

## V-280985 RHEL 10 must be configured to forward audit records via Transmission Control Protocol (TCP) to a different system or media from the system being audited via rsyslog. {#V-280985}

Severity: medium · Rule: SV-280985r1197221_rule · STIG ID: RHEL-10-200642 · CCI-001851

**Discussion.** Information stored in one location is vulnerable to accidental or incidental deletion or alteration.

Off-loading is a common process in information systems with limited audit storage capacity.

RHEL 10 installation media provides "rsyslogd", a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (a secure communications library implementing the Secure Sockets Layer [SSL], Transport Layer Security [TLS], and Datagram TLS [DTLS] protocols) creates a method to securely encrypt and off-load auditing.

The rsyslog provides three ways to forward message: the traditional User Datagram Protocol (UDP) transport, which is extremely lossy but standard; the plain TCP-based transport, which loses messages only during certain situations but is widely available; and the Reliable Event Logging Protocol (RELP) transport, which does not lose messages but is currently available only as part of the rsyslogd 3.15.0 and above.

Examples of each configuration:

UDP *.* @remotesystemname
TCP *.* @@remotesystemname
RELP *.* :omrelp:remotesystemname:2514

Note that a port number was given as there is no standard port for RELP.

**Check.**

```
Verify RHEL 10 audit system off-loads audit records onto a different system or media from the system being audited via rsyslog using TCP with the following commands:

To check for legacy configuration syntax, perform the following:

$ sudo grep -ir '@@' /etc/rsyslog.conf /etc/rsyslog.d/

To check for Rainer script syntax, perform the following:

$ sudo grep -rq 'type="omfwd"' /etc/rsyslog.conf /etc/rsyslog.d/

If a remote server is not configured, or the line is commented out, ask the system administrator to indicate how the audit logs are off-loaded to a different system or media. 

If there is no evidence that the audit logs are being off-loaded to another system or media, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to off-load audit records onto a different system or media from the system being audited via TCP using rsyslog by specifying the remote logging server in "/etc/rsyslog.conf" or "/etc/rsyslog.d/[customfile].conf" with the name or IP address of the log aggregation server.

Using legacy "@host:port" syntax example:
*.* @@[remoteloggingserver]:[port]

Using Rainer script example:
action(
    type="omfwd"
    target="logserver.example.com"
    port="514"
    protocol="tcp"
    action.resumeRetryCount="-1"
    queue.type="linkedList"
    que.size="10000"
)

Note: The Rainer script above does not contain the required encryption settings.
```

## V-280986 RHEL 10 must be configured so that the rsyslog daemon does not accept log messages from other servers unless the server is being used for log aggregation. {#V-280986}

Severity: medium · Rule: SV-280986r1184782_rule · STIG ID: RHEL-10-200643 · CCI-002385

**Discussion.** Unintentionally running a rsyslog server accepting remote messages puts the system at increased risk. Malicious rsyslog messages sent to the server could exploit vulnerabilities in the server software, introduce misleading information into the system's logs, or fill the system's storage, leading to a denial of service.

If the system is intended to be a log aggregation server, its use must be documented with the information system security officer.

**Check.**

```
Note: If the SA can demonstrate that another tool (e.g., SPLUNK) is being used to manage log off-load and aggregation in lieu of rsyslog, this check is not applicable.

Verify RHEL 10 is not configured to receive remote logs using rsyslog.

Verify the setting with the following commands:

$ ss -tulnp | grep rsyslog

If no output is returned, rsyslog is not listening for remote logs.

If output appears, check for configured ports (514 is the default for syslog).

Check for remote logging configuration in rsyslog by examining the rsyslog configuration files:

$ sudo grep -E 'InputTCPServerRun|UDPServerRun|RELPServerRun|imtcp|imudp|imrelp' /etc/rsyslog.conf /etc/rsyslog.d/*

If this command returns uncommented lines enabling network listeners, the system is accepting remote logs. If this system is not documented and authorized as a log aggregation server, this is a finding.

Note: An error about no files or directories from the above commands may be returned. This is not a finding. Additionally, if a port option used together with a target and protocol is returned from inside an action block, this is not a finding.
```

**Fix.**

```
Configure RHEL 10 to not receive remote logs using rsyslog.

Remove the lines in "/etc/rsyslog.conf" and any files in the "/etc/rsyslog.d" directory that match any of the following:

InputTCPServerRun
UDPServerRun
RELPServerRun
module(load="imtcp")
module(load="imudp")
module(load="imrelp")
input(type="imudp" port="514")
input(type="imtcp" port="514")
input(type="imrelp" port="514")

Restart the rsyslog daemon with the following command for the changes to take effect:

$ sudo systemctl restart rsyslog.service
```

## V-280987 RHEL 10 must authenticate the remote logging server for off-loading audit logs via "rsyslog". {#V-280987}

Severity: medium · Rule: SV-280987r1195371_rule · STIG ID: RHEL-10-200644 · CCI-001851

**Discussion.** Information stored in one location is vulnerable to accidental or incidental deletion or alteration.

Off-loading is a common process in information systems with limited audit storage capacity.

RHEL 10 installation media provides "rsyslogd", a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (a secure communications library implementing the Secure Sockets Layer (SSL), Transport Layer Security (TLS), and Datagram TLS (DTLS) protocols) creates a method to securely encrypt and off-load auditing.

The "rsyslog" supported authentication modes include:
- anon - Anonymous authentication.
- x509/fingerprint - Certificate fingerprint authentication.
- x509/certvalid - Certificate validation only.
- x509/name - Certificate validation and subject name authentication.

Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224

**Check.**

```
Verify RHEL 10 authenticates the remote logging server for off-loading audit logs with the following command:

$ sudo grep -r -E 'streamdriver.authmode|streamdriver.permittedpeer|tls.authmode|tls.permittedpeer' /etc/rsyslog.conf /etc/rsyslog.d/
/etc/rsyslog.d/99-forwarding.conf:        streamdriver.authmode="x509/name"

If the variable name "streamdriver.authmode" is present in an omfwd statement block, this is not a finding. However, if the "streamdriver.authmode" variable is in a module block, this is a finding.

If the value of the "$ActionSendStreamDriverAuthMode" or "streamdriver.authmode" or "tls.authmode" option is not set to "x509/name", or the line is commented out, ask the system administrator to indicate how the audit logs are off-loaded to a different system or media.

Additionally, if the permittedpeer is not specified in either of the following formats, this is a finding:
streamdriver.permittedpeer="rsyslog.server.example.com"
tls.permittedpeer="rsyslog.server.example.com"

If there is no evidence that the transfer of the audit logs being off-loaded to another system or media is encrypted, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to authenticate the remote logging server for off-loading audit logs by setting the following options in "/etc/rsyslog.d/99-forwarding.conf":

streamdriver.authmode="x509/name"

Specify the logserver to prevent man-in-the-middle attacks in the following format:
streamdriver.permittedpeer="rsyslog.server.example.com"
```

## V-280988 RHEL 10 must encrypt the transfer of audit records off-loaded onto a different system or media from the system being audited via rsyslog. {#V-280988}

Severity: medium · Rule: SV-280988r1195374_rule · STIG ID: RHEL-10-200645 · CCI-001851

**Discussion.** Information stored in one location is vulnerable to accidental or incidental deletion or alteration.

Off-loading is a common process in information systems with limited audit storage capacity.

RHEL 10 installation media provides "rsyslogd", a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (a secure communications library implementing the Secure Sockets Layer [SSL], Transport Layer Security [TLS], and Datagram TLS [DTLS] protocols) creates a method to securely encrypt and off-load auditing. When this utility is coupled with the omfwd module, it can use the ossl network stream driver, which leverages the OpenSSL library for Transport Layer Security (TLS) to securely encrypt and off-load auditing.

"Rsyslog" supported authentication modes include:
- anon - Anonymous authentication.
- x509/fingerprint - Certificate fingerprint authentication.
- x509/certvalid - Certificate validation only.
- x509/name - Certificate validation and subject name authentication.

Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224

**Check.**

```
Verify RHEL 10 encrypts audit records offloaded onto a different system via rsyslog using the modern "omfwd" action.

Search for active TLS-enabling configurations within "omfwd" action blocks with the following command:

$ sudo grep -rE 'tls="on"|StreamDriver.Mode\s*=\s*"1"' /etc/rsyslog.conf /etc/rsyslog.d/

If an active TCP-based "omfwd" forwarding rule exists on the system but the command above returns no active configuration lines, or if all results are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to encrypt off-loaded audit records via rsyslog by enabling TLS within the "omfwd" action rule.

Edit the configuration file containing the "omfwd" rule (e.g., /etc/rsyslog.d/99-forwarding.conf) and add the tls="on" parameter.

Example:
action(
  type="omfwd"
  target="logserver.example.com"
  protocol="tcp"
  port="6514"
  tls="on"
)

After applying the configuration, restart the rsyslog service:
$ sudo systemctl restart rsyslog
```

## V-280989 RHEL 10 must encrypt, via the gtls driver, the transfer of audit records off-loaded onto a different system or media from the system being audited via rsyslog. {#V-280989}

Severity: medium · Rule: SV-280989r1197222_rule · STIG ID: RHEL-10-200646 · CCI-001851

**Discussion.** Information stored in one location is vulnerable to accidental or incidental deletion or alteration.

Off-loading is a common process in information systems with limited audit storage capacity.

RHEL 10 installation media provides "rsyslogd", a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (a secure communications library implementing the Secure Sockets Layer [SSL], Transport Layer Security [TLS], and Datagram TLS [DTLS] protocols) creates a method to securely encrypt and off-load auditing. When this utility is coupled with the omfwd module, it can use the ossl network stream driver, which leverages the OpenSSL library for Transport Layer Security (TLS) to securely encrypt and off-load auditing.

Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224

**Check.**

```
Verify RHEL 10 explicitly defines a TLS driver (gtls or ossl) for encrypted rsyslog off-loading.

Search for an explicitly defined stream driver within "omfwd" action blocks with the following command:

$ sudo grep -rE 'StreamDriver\s*=\s*"(gtls|ossl)"' /etc/rsyslog.conf /etc/rsyslog.d/

If TLS-based "omfwd" forwarding is configured, but the command above returns no active configuration lines specifying either "gtls" or "ossl" within the action block, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to explicitly define a TLS driver for rsyslog to use for encrypting off-loaded audit records. The "ossl" driver is required for environments operating in FIPS mode.

Add the "streamdriver" parameter to the "omfwd" action rule in its configuration file (e.g., /etc/rsyslog.d/99-forwarding.conf).

Example:
action(
  type="omfwd"
  streamdriver="ossl"
  target="logserver.example.com"
  protocol="tcp"
  port="6514"
  tls="on"
)

After applying the configuration, restart the rsyslog service:
$ sudo systemctl restart rsyslog
```

## V-280990 RHEL 10 must monitor all remote access methods. {#V-280990}

Severity: medium · Rule: SV-280990r1268219_rule · STIG ID: RHEL-10-200647 · CCI-000067

**Discussion.** Logging remote access methods can be used to trace the decrease in the risks associated with remote user access management. It can also be used to spot cyberattacks and ensure ongoing compliance with organizational policies surrounding the use of remote access methods.

**Check.**

```
Verify RHEL 10 monitors all remote access methods with the following command:

$ sudo grep -rE '(auth.\*|authpriv.\*|daemon.\*)' /etc/rsyslog.conf /etc/rsyslog.d/
/etc/rsyslog.conf:authpriv.*                                              /var/log/secure

If "auth.*", "authpriv.*", or "daemon.*" are not configured to be logged, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to monitor all remote access methods.

Add or update the following lines to the "/etc/rsyslog.conf" file or a file in "/etc/rsyslog.d":

auth.*;authpriv.*;daemon.* /var/log/secure

Restart the "rsyslog" service with the following command for the changes to take effect:

$ sudo systemctl restart rsyslog.service
```

## V-280991 RHEL 10 must use cron logging. {#V-280991}

Severity: medium · Rule: SV-280991r1273567_rule · STIG ID: RHEL-10-200648 · CCI-000133

**Discussion.** Cron logging can be used to trace the successful or unsuccessful execution of cron jobs. It can also be used to spot intrusions into the use of the cron facility by unauthorized and malicious users.

**Check.**

```
Verify RHEL 10 rsyslog is configured to log cron events with the following command:

Note: If another logging package is used, substitute the utility configuration file for "/etc/rsyslog.conf" or "/etc/rsyslog.d/*.conf" files.

$ grep -s "cron.\*" /etc/rsyslog.conf /etc/rsyslog.d/*.conf
/etc/rsyslog.d/99-cron-stig.conf:cron.* action(type="omfile" file="/var/log/cron")

If the command does not return a line demonstrating logging to /var/log/cron, perform a functional cron test.

Inject a message into the cron logging facility with the following command:

$ logger -p cron.info "STIG-TEST-CRON-LOGGING"

Check if it successfully wrote to the dedicated log file with the following command:

$ sudo grep "STIG-TEST-CRON-LOGGING" /var/log/cron
Jul 16 11:33:00 RHEL10Sim pdosadmin[33692]: STIG-TEST-CRON-LOGGING

If "rsyslog" is not logging messages for the cron facility or all facilities, this is a finding.
```

**Fix.**

```
Configure RHEL 10 rsyslog to log all cron messages by adding or updating the following line to "/etc/rsyslog.conf" or a configuration file in the /etc/rsyslog.d/ directory:

cron.* /var/log/cron

The rsyslog daemon must be restarted for the changes to take effect:

$ sudo systemctl restart rsyslog.service
```

## V-280992 RHEL 10 must have the packages required for encrypting off-loaded audit logs installed. {#V-280992}

Severity: medium · Rule: SV-280992r1268232_rule · STIG ID: RHEL-10-200650 · CCI-000803

**Discussion.** The "rsyslog-gnutls" package provides Transport Layer Security (TLS) support for the rsyslog daemon, which enables secure remote logging.

**Check.**

```
Verify RHEL 10 has the "rsyslog-gnutls" package installed with the following command:

$ sudo dnf list --installed rsyslog-gnutls
Installed Packages
rsyslog-gnutls.x86_64                                     8.2412.0-1.el10                                     @AppStream

If the "rsyslog-gnutls" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "rsyslog-gnutls" package installed with the following command:

$ sudo dnf -y install rsyslog-gnutls
```

## V-280993 RHEL 10 must have the "audit" package installed. {#V-280993}

Severity: medium · Rule: SV-280993r1268225_rule · STIG ID: RHEL-10-200660 · CCI-000169 CCI-000130 CCI-000131 CCI-000132 CCI-000133 CCI-000134 CCI-000135 CCI-000154 CCI-000158 CCI-001876 CCI-001464 CCI-001487 CCI-001914 CCI-001875 CCI-001877 CCI-001878 CCI-001879 CCI-001880 CCI-001881 CCI-001882 CCI-001889 CCI-003938 CCI-002884 CCI-000172

**Discussion.** Without establishing what type of events occurred, along with the source, location, and outcome, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack.

Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked.

Associating event types with detected events in audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured RHEL 10 system.

Satisfies: SRG-OS-000062-GPOS-00031, SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000122-GPOS-00063, SRG-OS-000254-GPOS-00095, SRG-OS-000255-GPOS-00096, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000358-GPOS-00145, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000475-GPOS-00220

**Check.**

```
Verify RHEL 10 has the "audit" service package installed with the following command:

$ sudo dnf list --installed audit
Installed Packages
audit.x86_64                                           4.0.3-1.el10                                            @anaconda

If the "audit" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "audit" service package installed with the following command:

$ sudo dnf -y install audit
```

## V-280994 RHEL 10 must enable the audit service. {#V-280994}

Severity: medium · Rule: SV-280994r1268225_rule · STIG ID: RHEL-10-200661 · CCI-000169 CCI-000130 CCI-000131 CCI-000132 CCI-000133 CCI-000134 CCI-000135 CCI-000154 CCI-000158 CCI-001876 CCI-001464 CCI-001487 CCI-001914 CCI-001875 CCI-001877 CCI-001878 CCI-001879 CCI-001880 CCI-001881 CCI-001882 CCI-001889 CCI-003938 CCI-002884 CCI-000172

**Discussion.** Without establishing what type of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Ensuring the auditd service is active ensures audit records generated by the kernel are appropriately recorded.

Additionally, a properly configured audit subsystem ensures that actions of individual system users can be uniquely traced to those users so they can be held accountable for their actions.

Satisfies: SRG-OS-000062-GPOS-00031, SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000122-GPOS-00063, SRG-OS-000254-GPOS-00095, SRG-OS-000255-GPOS-00096, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000358-GPOS-00145, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000475-GPOS-00220

**Check.**

```
Verify RHEL 10 enables the audit service to produce audit records with the following command:

$ systemctl status auditd.service
o auditd.service - Security Audit Logging Service
     Loaded: loaded (/usr/lib/systemd/system/auditd.service; enabled; preset: enabled)
     Active: active (running) since Wed 2025-10-01 14:00:21 EDT; 1 week 6 days ago

If the audit service is not "active" and "running", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable the auditd service with the following command:

$ sudo systemctl enable --now auditd
```

## V-280995 RHEL 10 must have the "audispd-plugins" package installed. {#V-280995}

Severity: low · Rule: SV-280995r1195383_rule · STIG ID: RHEL-10-200662 · CCI-001851

**Discussion.** The "audispd-plugins" package provides plugins for the real-time interface to the audit subsystem, "audispd". These plugins can do such things as relay events to remote machines or analyze events for suspicious behavior.

**Check.**

```
Verify RHEL 10 has the "audispd-plugins" package installed with the following command:

$ sudo dnf list --installed audispd-plugins
Installed Packages
audispd-plugins.x86_64                           4.0.3-1.el10                            @rhel-10-for-x86_64-baseos-rpms

If the "audispd-plugins" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "audispd-plugins" package installed with the following command:

$ sudo dnf -y install audispd-plugins
```

## V-280996 RHEL 10 must have the "libreswan" package installed. {#V-280996}

Severity: medium · Rule: SV-280996r1268232_rule · STIG ID: RHEL-10-200680 · CCI-000803

**Discussion.** Providing the ability for remote users or systems to initiate a secure virtual private network connection protects information when it is transmitted over a wide area network.

**Check.**

```
Note: If there is no operational need for Libreswan to be installed, this rule is not applicable.

Verify RHEL 10 has the "libreswan" service package installed with the following command:

$ sudo dnf list --installed libreswan
Installed Packages
libreswan.x86_64                                         5.2-1.el10_0                                         @AppStream

If the "libreswan" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "libreswan" service package installed with the following command:

$ sudo dnf -y install libreswan
```

## V-280997 RHEL 10 must notify designated personnel if baseline configurations are changed in an unauthorized manner. {#V-280997}

Severity: medium · Rule: SV-280997r1195387_rule · STIG ID: RHEL-10-200690 · CCI-000139

**Discussion.** The "postfix" package provides the mail command required to allow sending email notifications of unauthorized configuration changes to designated personnel.

**Check.**

```
Verify RHEL 10 is configured to allow sending email notifications.

Note: The "postfix" package provides the "mail" command that is used to send email messages.

Verify that the "postfix" package is installed on the system:

$ sudo dnf list --installed postfix
Installed Packages
postfix.x86_64                                         2:3.8.5-8.el10                                         @AppStream

If the "postfix" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to notify designated personnel if baseline configurations are changed in an unauthorized manner.

Install the postfix package with the following command:

$ sudo dnf -y install postfix
```

## V-280998 RHEL 10 must have mail aliases to notify the information system security officer (ISSO) and system administrator (SA) (at a minimum) of an audit processing failure. {#V-280998}

Severity: medium · Rule: SV-280998r1208794_rule · STIG ID: RHEL-10-200691 · CCI-000139

**Discussion.** It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected.

Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.

This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.

**Check.**

```
Verify RHEL 10 is configured to notify the appropriate interactive users of an audit processing failure.

Find the alias maps that are being used with the following command:

$ postconf alias_maps
alias_maps = lmdb:/etc/aliases

Query the Postfix alias maps for an alias for the root user with the following command:

$ postmap -q root lmdb:/etc/aliases
ISSO

If an alias is not set, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have mail aliases notify the ISSO and SA (at a minimum) of an audit processing failure.

Edit the aliases map file (by default /etc/aliases) used by Postfix and configure a root alias (using the user ISSO as an example):

root:    ISSO

Update the aliases database with the following command:

$ sudo newaliases
```

## V-280999 RHEL 10 must be configured to prevent unrestricted mail relaying. {#V-280999}

Severity: medium · Rule: SV-280999r1165352_rule · STIG ID: RHEL-10-200692 · CCI-000381

**Discussion.** If unrestricted mail relaying is permitted, unauthorized senders could use this host as a mail relay to send spam or for other unauthorized activity.

**Check.**

```
Note: If postfix is not installed, this is not applicable.

Verify RHEL 10 is configured to prevent unrestricted mail relaying with the following command:

$ postconf -n smtpd_client_restrictions
smtpd_client_restrictions = permit_mynetworks,reject

If the "smtpd_client_restrictions" parameter contains any entries other than "permit_mynetworks" and "reject", and the additional entries have not been documented with the information system security officer, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the postfix configuration file restricts client connections to the local network with the following command:

$ sudo postconf -e 'smtpd_client_restrictions = permit_mynetworks,reject'
```

## V-281000 RHEL 10 must have the "cronie" package installed. {#V-281000}

Severity: medium · Rule: SV-281000r1195389_rule · STIG ID: RHEL-10-200700 · CCI-000381

**Discussion.** The "cronie" package must be installed if it is to be available for multifactor authentication using smart cards.

**Check.**

```
Verify RHEL 10 has the "cronie" package installed with the following command:

$ sudo dnf list --installed cronie
Installed Packages
cronie.x86_64                                           1.7.0-9.el10                                           @anaconda

If the "cronie" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "cronie" package installed with the following command:

$ sudo dnf -y install cronie
```

## V-281001 RHEL 10 must have a Secure Shell (SSH) server installed for all networked systems. {#V-281001}

Severity: medium · Rule: SV-281001r1195391_rule · STIG ID: RHEL-10-200720 · CCI-002418 CCI-002421 CCI-002420 CCI-002422

**Discussion.** Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and read or altered.

This requirement applies to internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification.

Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, logical means (cryptography) do not have to be employed, and vice versa.

Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190

**Check.**

```
Verify RHEL 10 has the "openssh-server" package installed with the following command:

$ sudo dnf list --installed openssh-server
Installed Packages
openssh-server.x86_64                                      9.9p1-7.el10_0                                      @anaconda

If the "openssh-server" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "openssh-server" package installed with the following command:

$ sudo dnf -y install openssh-server
```

## V-281002 RHEL 10 must, for all networked systems, have and implement Secure Shell (SSH) to protect the confidentiality and integrity of transmitted and received information. {#V-281002}

Severity: medium · Rule: SV-281002r1184641_rule · STIG ID: RHEL-10-200721 · CCI-002418 CCI-002421 CCI-002420 CCI-002422

**Discussion.** Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered.

This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification.

Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.

Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190

**Check.**

```
Verify RHEL 10 "sshd" is active with the following command:

$ systemctl is-active sshd
active

If the "sshd" service is not active, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable the sshd service by running the following command:

$ systemctl enable --now sshd
```

## V-281003 RHEL 10 must have the "openssh-clients" package installed. {#V-281003}

Severity: medium · Rule: SV-281003r1195393_rule · STIG ID: RHEL-10-200722 · CCI-000381

**Discussion.** This package includes utilities to make encrypted connections and transfer files securely to Secure Shell (SSH) servers.

**Check.**

```
Verify RHEL 10 has the "openssh-clients" package installed with the following command:

$ sudo dnf list --installed openssh-clients
Installed Packages
openssh-clients.x86_64                                     9.9p1-7.el10_0                                      @anaconda

If the "openssh-clients" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "openssh-clients" package installed with the following command:

$ sudo dnf -y install openssh-clients
```

## V-281005 RHEL 10 must have the "pkcs11-provider" package installed. {#V-281005}

Severity: medium · Rule: SV-281005r1273568_rule · STIG ID: RHEL-10-200730 · CCI-000765 CCI-004046 CCI-001954

**Discussion.** Without the use of multifactor authentication (MFA), the ease of access to privileged functions is greatly increased. MFA requires using two or more factors to achieve authentication. A privileged account is defined as an information system account with authorizations of a privileged user. The DoW common access card (CAC) with DoW-approved PKI is an example of MFA.

Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000375-GPOS-00160, SRG-OS-000377-GPOS-00162

**Check.**

```
Note: If the system administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable.

Verify RHEL 10 has the "pkcs11-provider" package installed with the following command:

$ sudo dnf list --installed pkcs11-provider
Installed Packages
pkcs11-provider.x86_64                           1.0-3.el10_0                            @rhel-10-for-x86_64-baseos-rpms

If the "pkcs11-provider" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "pkcs11-provider" package installed with the following command:

$ sudo dnf -y install pkcs11-provider
```

## V-281006 RHEL 10 must have the "gnutls-utils" package installed. {#V-281006}

Severity: medium · Rule: SV-281006r1195397_rule · STIG ID: RHEL-10-200740 · CCI-000381

**Discussion.** "GnuTLS" is a secure communications library implementing the Secure Sockets Layer (SSL), Transport Layer Security (TLS), and Datagram TLS (DTLS) protocols and technologies around them. It provides a simple C language application programming interface (API) to access the secure communications protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP, and other required structures. This package contains command line TLS client and server and certificate manipulation tools.

**Check.**

```
Verify RHEL 10 has the "gnutls-utils" package installed with the following command:

$ sudo dnf list --installed gnutls-utils
Installed Packages
gnutls-utils.x86_64                         3.8.9-9.el10_0.14                         @rhel-10-for-x86_64-appstream-rpms

If the "gnutls-utils" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "gnutls-utils" package installed with the following command:

$ sudo dnf -y install gnutls-utils
```

## V-281007 RHEL 10 must have the "crypto-policies" package installed. {#V-281007}

Severity: high · Rule: SV-281007r1195399_rule · STIG ID: RHEL-10-300000 · CCI-002450 CCI-002890 CCI-003123

**Discussion.** Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data.

Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174

**Check.**

```
Verify RHEL 10 has the "crypto-policies" package installed with the following command:

$ sudo dnf list --installed crypto-policies
Installed Packages
crypto-policies.noarch                  20250214-1.gitfd9b9b9.el10_0.1                   @rhel-10-for-x86_64-baseos-rpms

If the "crypto-policies" package is not installed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have the "crypto-policies" package installed with the following command:

$ sudo dnf -y install crypto-policies
```

## V-281008 RHEL 10 must implement a FIPS 140-3-compliant systemwide cryptographic policy. {#V-281008}

Severity: high · Rule: SV-281008r1268222_rule · STIG ID: RHEL-10-300010 · CCI-000068 CCI-002450 CCI-002890 CCI-003123

**Discussion.** Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data.

Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174

**Check.**

```
Verify RHEL 10 is set to use a FIPS 140-3-compliant systemwide cryptographic policy.

Verify the current systemwide crypto-policy with the following command:

$ update-crypto-policies --show
FIPS

If the systemwide crypto-policy is not set to "FIPS", this is a finding.

Verify the current minimum crypto-policy configuration with the following commands:

$ sudo grep -E 'rsa_size|hash' /etc/crypto-policies/state/CURRENT.pol
hash = SHA2-256 SHA2-384 SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256
min_rsa_size = 2048

If the "hash" values do not include at least the following FIPS 140-3-compliant algorithms, this is a finding:

"SHA2-256 SHA2-384 SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256"

If any algorithms include "SHA1" or a hash value less than "224", this is a finding.

If the "min_rsa_size" is not set to a value of at least "2048", this is a finding.

If these commands do not return any output, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use a FIPS 140-3-compliant systemwide cryptographic policy.

Set the systemwide crypto-policy to FIPS with the following command:

$ sudo update-crypto-policies --set FIPS
Setting system policy to FIPS

Note: Systemwide crypto-policies are applied on application startup. It is recommended to restart the system for the change of policies to fully take place.
```

## V-281009 RHEL 10 must enable FIPS mode. {#V-281009}

Severity: high · Rule: SV-281009r1268222_rule · STIG ID: RHEL-10-000500 · CCI-000068 CCI-000877 CCI-001453 CCI-002890 CCI-003123 CCI-002450 CCI-002418

**Discussion.** Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government because this provides assurance they have been tested and validated.

Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000125-GPOS-00065, SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000396-GPOS-00176, SRG-OS-000423-GPOS-00187, SRG-OS-000478-GPOS-00223

**Check.**

```
Verify RHEL 10 is in FIPS mode with the following command:

$ cat /proc/sys/crypto/fips_enabled
1

If the command does not return "1", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to implement FIPS mode.

If this check fails on an installed system, it is a permanent finding until the system is reinstalled with "fips=1" during installation.

Red Hat 10 does not support switching to strict FIPS mode after installation.
```

## V-281010 RHEL 10 must be configured so that Secure Shell (SSH) clients use only DoW-approved encryption ciphers employing FIPS 140-3-validated cryptographic hash algorithms to protect the confidentiality of SSH client connections. {#V-281010}

Severity: high · Rule: SV-281010r1273569_rule · STIG ID: RHEL-10-300030 · CCI-000068 CCI-000877 CCI-001453 CCI-002890 CCI-003123 CCI-002418

**Discussion.** Without cryptographic integrity protections, information can be altered by unauthorized users without detection.

Remote access (e.g., Remote Desktop Protocol [RDP]) is access to DoW nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganizational-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.

Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions that use asymmetric cryptography. This enables distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.

RHEL 10 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the "/etc/sysconfig/sshd" file. The employed algorithms can be viewed in the "/etc/crypto-policies/back-ends/openssh.config" file.

Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000125-GPOS-00065, SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000423-GPOS-00187

**Check.**

```
Verify RHEL 10 SSH clients are configured to use only ciphers employing FIPS 140-3-approved algorithms.

To verify the ciphers in the systemwide SSH configuration file, use the following command:

$ sudo grep -i Ciphers /etc/crypto-policies/back-ends/openssh.config
Ciphers aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr

If the cipher entries in the "openssh.config" file have any ciphers other than "aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr", or they are missing or commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH clients to use only ciphers employing FIPS 140-3-approved algorithms.

Reinstall crypto-policies with the following command:

$ sudo dnf -y reinstall crypto-policies

Set the crypto-policy to FIPS with the following command:

$ sudo update-crypto-policies --set FIPS
Setting system policy to FIPS

Note: Systemwide crypto policies are applied on application startup. It is recommended to restart the system for the change of policies to fully take place.
```

## V-281011 RHEL 10 must be configured so that Secure Shell (SSH) servers use only DoW-approved encryption ciphers employing FIPS 140-3-validated cryptographic hash algorithms to protect the confidentiality of SSH server connections. {#V-281011}

Severity: high · Rule: SV-281011r1273570_rule · STIG ID: RHEL-10-300040 · CCI-000877 CCI-001453

**Discussion.** Without cryptographic integrity protections, unauthorized users can alter information without detection.

Remote access (e.g., Remote Desktop Protocol [RDP]) is access to DoW nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganizational-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.

Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions that use asymmetric cryptography. This enables distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.

RHEL 10 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the "/etc/sysconfig/sshd" file. The employed algorithms can be viewed in the "/etc/crypto-policies/back-ends/opensshserver.config" file.

Satisfies: SRG-OS-000125-GPOS-00065, SRG-OS-000250-GPOS-00093

**Check.**

```
Verify RHEL 10 SSH servers are configured to use only ciphers employing FIPS 140-3-approved algorithms.

To verify the ciphers in the systemwide SSH configuration file, use the following command:

$ sudo grep -i Ciphers /etc/crypto-policies/back-ends/opensshserver.config
Ciphers aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr

If the cipher entries in the "opensshserver.config" file have any ciphers other than "aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr", or they are missing or commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH servers to use only ciphers employing FIPS 140-3-approved algorithms.

Reinstall crypto-policies with the following command:

$ sudo dnf -y reinstall crypto-policies

Set the crypto-policy to FIPS with the following command:

$ sudo update-crypto-policies --set FIPS
Setting system policy to FIPS

Note: Systemwide crypto policies are applied on application startup. It is recommended to restart the system for the change of policies to fully take place.
```

## V-281012 RHEL 10 must be configured so that Secure Shell (SSH) clients use only DoW-approved Message Authentication Codes (MACs) employing FIPS 140-3-validated cryptographic hash algorithms to protect the confidentiality of SSH client connections. {#V-281012}

Severity: high · Rule: SV-281012r1273571_rule · STIG ID: RHEL-10-300050 · CCI-000877 CCI-001453

**Discussion.** Without cryptographic integrity protections, information can be altered by unauthorized users without detection.

Remote access (e.g., Remote Desktop Protocol [RDP]) is access to DoW nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganizational-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.

Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions that use asymmetric cryptography. This enables distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.

RHEL 10 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the "/etc/sysconfig/sshd" file. The employed algorithms can be viewed in the "/etc/crypto-policies/back-ends/openssh.config" file.

Satisfies: SRG-OS-000125-GPOS-00065, SRG-OS-000250-GPOS-00093

**Check.**

```
Verify RHEL 10 SSH clients are configured to use only MACs employing FIPS 140-3-approved algorithms.

To verify the MACs in the systemwide SSH configuration file, use the following command:

$ sudo grep -i MACs /etc/crypto-policies/back-ends/openssh.config
MACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512

If the MACs entries in the "openssh.config" file have any hashes other than "hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512", or they are missing or commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH clients to use only MACs employing FIPS 140-3-approved algorithms.

Reinstall crypto-policies with the following command:

$ sudo dnf -y reinstall crypto-policies

Set the crypto-policy to FIPS with the following command:

$ sudo update-crypto-policies --set FIPS
Setting system policy to FIPS

Note: Systemwide crypto policies are applied on application startup. It is recommended to restart the system for the change of policies to fully take place.
```

## V-281013 RHEL 10 must be configured so that Secure Shell (SSH) servers use only DoW-approved Message Authentication Codes (MACs) employing FIPS 140-3-validated cryptographic hash algorithms to protect the confidentiality of SSH server connections. {#V-281013}

Severity: high · Rule: SV-281013r1273572_rule · STIG ID: RHEL-10-300060 · CCI-000877 CCI-001453

**Discussion.** Without cryptographic integrity protections, information can be altered by unauthorized users without detection.

Remote access (e.g., Remote Desktop Protocol [RDP]) is access to DoW nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.

Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.

RHEL 10 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the "/etc/sysconfig/sshd" file. The employed algorithms can be viewed in the "/etc/crypto-policies/back-ends/opensshserver.config" file.

Satisfies: SRG-OS-000125-GPOS-00065, SRG-OS-000250-GPOS-00093

**Check.**

```
Verify RHEL 10 SSH servers are configured to use only MACs employing FIPS 140-3-approved algorithms with the following command:

$ sudo grep -i MACs /etc/crypto-policies/back-ends/opensshserver.config
MACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512

If the MACs entries in the "opensshserver.config" file have any hashes other than "hmac-sha2-512" and "hmac-sha2-256", the order differs from the example above, or they are missing or commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH servers to use only MACs employing FIPS 140-3-approved algorithms.

Reinstall crypto-policies with the following command:

$ sudo dnf -y reinstall crypto-policies

Set the crypto-policy to FIPS with the following command:

$ sudo update-crypto-policies --set FIPS
Setting system policy to FIPS

Note: Systemwide crypto policies are applied on application startup. It is recommended to restart the system for the change of policies to fully take place.
```

## V-281014 RHEL 10 must use FIPS 140-3-approved cryptographic algorithms for IP tunnels. {#V-281014}

Severity: high · Rule: SV-281014r1268222_rule · STIG ID: RHEL-10-300070 · CCI-000068

**Discussion.** Overriding the systemwide cryptographic policy makes the behavior of the Libreswan service violate expectations and makes system configuration more fragmented.

**Check.**

```
Note: If the IPsec service is not installed, this requirement is not applicable.

Verify RHEL 10 sets the IPsec service to use the systemwide cryptographic policy with the following command:

$ sudo grep include /etc/ipsec.conf /etc/ipsec.d/*.conf
/etc/ipsec.conf:include /etc/crypto-policies/back-ends/libreswan.config

If the ipsec configuration file does not contain "include /etc/crypto-policies/back-ends/libreswan.config", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that Libreswan uses the systemwide cryptographic policy.

Add the following line to "/etc/ipsec.conf":

include /etc/crypto-policies/back-ends/libreswan.config
```

## V-281015 RHEL 10 must implement DoW-approved encryption in the bind package. {#V-281015}

Severity: high · Rule: SV-281015r1273573_rule · STIG ID: RHEL-10-300080 · CCI-002418 CCI-002422

**Discussion.** Without cryptographic integrity protections, information can be altered by unauthorized users without detection.

Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.

RHEL 10 incorporates systemwide crypto policies by default. The employed algorithms can be viewed in the "/etc/crypto-policies/back-ends/" directory.

Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000426-GPOS-00190

**Check.**

```
Note: If the "bind" package is not installed, this requirement is not applicable.

Verify RHEL 10 BIND uses the systemwide cryptographic policy with the following command:

$ sudo grep include /etc/named.conf
include "/etc/crypto-policies/back-ends/bind.config";'

If BIND is installed and the BIND config file does not contain the include "/etc/crypto-policies/back-ends/bind.config" directive, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 BIND to use the systemwide cryptographic policy.

Add the following line to the "options" section in "/etc/named.conf":

include "/etc/crypto-policies/back-ends/bind.config";
```

## V-281016 RHEL 10 cryptographic policy must not be overridden. {#V-281016}

Severity: high · Rule: SV-281016r1273577_rule · STIG ID: RHEL-10-300090 · CCI-002450 CCI-002890 CCI-003123

**Discussion.** Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data.

Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174

**Check.**

```
Verify RHEL 10 cryptographic policies are not overridden.

Verify the configured policy matches the generated policy with the following command:

$ sudo update-crypto-policies --check
The configured policy matches the generated policy

If the returned message does not match the above, but instead matches the following, this is a finding:

The configured policy does NOT match the generated policy

List all of the crypto backends configured on the system with the following command:

$ ls -l /etc/crypto-policies/back-ends/ 
lrwxrwxrwx. 1 root root  40 Nov 13 16:29 bind.config -> /usr/share/crypto-policies/FIPS/bind.txt
lrwxrwxrwx. 1 root root  42 Nov 13 16:29 gnutls.config -> /usr/share/crypto-policies/FIPS/gnutls.txt
lrwxrwxrwx. 1 root root  40 Nov 13 16:29 java.config -> /usr/share/crypto-policies/FIPS/java.txt
lrwxrwxrwx. 1 root root  46 Nov 13 16:29 javasystem.config -> /usr/share/crypto-policies/FIPS/javasystem.txt
lrwxrwxrwx. 1 root root  40 Nov 13 16:29 krb5.config -> /usr/share/crypto-policies/FIPS/krb5.txt
lrwxrwxrwx. 1 root root  45 Nov 13 16:29 libreswan.config -> /usr/share/crypto-policies/FIPS/libreswan.txt
lrwxrwxrwx. 1 root root  42 Nov 13 16:29 libssh.config -> /usr/share/crypto-policies/FIPS/libssh.txt
-rw-r--r--. 1 root root 398 Nov 13 16:29 nss.config
lrwxrwxrwx. 1 root root  43 Nov 13 16:29 openssh.config -> /usr/share/crypto-policies/FIPS/openssh.txt
lrwxrwxrwx. 1 root root  49 Nov 13 16:29 opensshserver.config -> /usr/share/crypto-policies/FIPS/opensshserver.txt
lrwxrwxrwx. 1 root root  46 Nov 13 16:29 opensslcnf.config -> /usr/share/crypto-policies/FIPS/opensslcnf.txt
lrwxrwxrwx. 1 root root  43 Nov 13 16:29 openssl.config -> /usr/share/crypto-policies/FIPS/openssl.txt
lrwxrwxrwx. 1 root root  48 Nov 13 16:29 openssl_fips.config -> /usr/share/crypto-policies/FIPS/openssl_fips.txt

If the paths do not point to the respective files under "/usr/share/crypto-policies/FIPS" path, this is a finding.

Note: If there is an operational need to use a subpolicy that causes the links to the crypto backends to break, this is a finding, and exceptions must be made by the authorizing official and documented with the information system security officer.
```

**Fix.**

```
Configure RHEL 10 to correctly implement the systemwide cryptographic policies by reinstalling the crypto-policies package contents.

Reinstall crypto-policies with the following command:

$ sudo dnf -y reinstall crypto-policies

Set the crypto-policy to FIPS with the following command:

$ sudo update-crypto-policies --set FIPS
Setting system policy to FIPS

Note: Systemwide crypto policies are applied on application startup. It is recommended to restart the system for the change of policies to fully take place.
```

## V-281017 RHEL 10 must be configured so that the "/etc/group" file is owned by root. {#V-281017}

Severity: medium · Rule: SV-281017r1268226_rule · STIG ID: RHEL-10-400000 · CCI-000213

**Discussion.** The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.

**Check.**

```
Verify RHEL 10 is configured so that "/etc/group" file is owned by "root" with the following command:

$ sudo stat -c "%U %n" /etc/group
root /etc/group

If the "/etc/group" file does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the owner of the file "/etc/group" is set to "root" by running the following command:

$ sudo chown root /etc/group
```

## V-281018 RHEL 10 must be configured so that the "/etc/group" file is group-owned by "root". {#V-281018}

Severity: medium · Rule: SV-281018r1268226_rule · STIG ID: RHEL-10-400005 · CCI-000213

**Discussion.** The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/group" file is group-owned by "root" with the following command:

$ sudo stat -c "%G %n" /etc/group
root /etc/group

If the "/etc/group" file does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the group of the file "/etc/group" is set to "root" by running the following command:

$ sudo chgrp root /etc/group
```

## V-281019 RHEL 10 must be configured so that the "/etc/group-" file is owned by "root". {#V-281019}

Severity: medium · Rule: SV-281019r1268226_rule · STIG ID: RHEL-10-400010 · CCI-000213

**Discussion.** The "/etc/group-" file is a backup file of "/etc/group", and as such contains information regarding groups that are configured on the system. Protection of this file is important for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/group-" file is owned by "root" with the following command:

$ sudo stat -c "%U %n" /etc/group-
root /etc/group-

If the "/etc/group-" file does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the owner of the "/etc/group-" file is set to "root" by running the following command:

$ sudo chown root /etc/group-
```

## V-281020 RHEL 10 must be configured so that the "/etc/group-" file is group-owned by "root". {#V-281020}

Severity: medium · Rule: SV-281020r1268226_rule · STIG ID: RHEL-10-400015 · CCI-000213

**Discussion.** The "/etc/group-" file is a backup file of "/etc/group", and as such contains information regarding groups that are configured on the system. Protection of this file is important for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/group-" file is group-owned by "root" with the following command:

$ sudo stat -c "%G %n" /etc/group-
root /etc/group-

If the "/etc/group-" file does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the group of the "/etc/group-" file is set to "root" by running the following command:

$ sudo chgrp root /etc/group-
```

## V-281021 RHEL 10 must be configured so that the "/etc/gshadow" file is owned by "root". {#V-281021}

Severity: medium · Rule: SV-281021r1268226_rule · STIG ID: RHEL-10-400020 · CCI-000213

**Discussion.** The "/etc/gshadow" file contains group password hashes. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/gshadow" file is owned by "root" with the following command:

$ sudo stat -c "%U %n" /etc/gshadow
root /etc/gshadow

If the "/etc/gshadow" file does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the owner of the file "/etc/gshadow" is set to "root" by running the following command:

$ sudo chown root /etc/gshadow
```

## V-281022 RHEL 10 must be configured so that the "/etc/gshadow" file is group-owned by "root". {#V-281022}

Severity: medium · Rule: SV-281022r1268226_rule · STIG ID: RHEL-10-400025 · CCI-000213

**Discussion.** The "/etc/gshadow" file contains group password hashes. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/gshadow" file is group-owned by "root" with the following command:

$ sudo stat -c "%G %n" /etc/gshadow
root /etc/gshadow

If the "/etc/gshadow" file does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the group of the "/etc/gshadow" file is set to "root" by running the following command:

$ sudo chgrp root /etc/gshadow
```

## V-281023 RHEL 10 must be configured so that the "/etc/gshadow-" file is owned by "root". {#V-281023}

Severity: medium · Rule: SV-281023r1268226_rule · STIG ID: RHEL-10-400030 · CCI-000213

**Discussion.** The "/etc/gshadow-" file is a backup of "/etc/gshadow", and as such contains group password hashes. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/gshadow-" file is owned by "root" with the following command:

$ sudo stat -c "%U %n" /etc/gshadow-
root /etc/gshadow-

If the "/etc/gshadow-" file does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the owner of the "/etc/gshadow-" file is set to "root" by running the following command:

$ sudo chown root /etc/gshadow-
```

## V-281024 RHEL 10 must be configured so that the "/etc/gshadow-" file is group-owned by "root". {#V-281024}

Severity: medium · Rule: SV-281024r1268226_rule · STIG ID: RHEL-10-400035 · CCI-000213

**Discussion.** The "/etc/gshadow-" file is a backup of "/etc/gshadow", and as such contains group password hashes. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/gshadow-" file is group-owned by "root" with the following command:

$ sudo stat -c "%G %n" /etc/gshadow-
root /etc/gshadow-

If the "/etc/gshadow-" file does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the group of the "/etc/gshadow-" file is set to "root" by running the following command:

$ sudo chgrp root /etc/gshadow-
```

## V-281025 RHEL 10 must be configured so that the "/etc/passwd" file is owned by "root". {#V-281025}

Severity: medium · Rule: SV-281025r1268226_rule · STIG ID: RHEL-10-400040 · CCI-000213

**Discussion.** The "/etc/passwd" file contains information about the users that are configured on the system. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/passwd" file is owned by "root" with the following command:

$ sudo stat -c "%U %n" /etc/passwd
root /etc/passwd

If the "/etc/passwd" file does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the owner of the "/etc/passwd" file is set to "root" by running the following command:

$ sudo chown root /etc/passwd
```

## V-281026 RHEL 10 must be configured so that the "/etc/passwd" file is group-owned by "root". {#V-281026}

Severity: medium · Rule: SV-281026r1268226_rule · STIG ID: RHEL-10-400045 · CCI-000213

**Discussion.** The "/etc/passwd" file contains information about the users that are configured on the system. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/passwd" file is group-owned by "root" with the following command:

$ sudo stat -c "%G %n" /etc/passwd
root /etc/passwd

If the "/etc/passwd" file does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the group of the "/etc/passwd" file is set to "root" by running the following command:

$ sudo chgrp root /etc/passwd
```

## V-281027 RHEL 10 must be configured so that the "/etc/passwd-" file is owned by "root". {#V-281027}

Severity: medium · Rule: SV-281027r1268226_rule · STIG ID: RHEL-10-400050 · CCI-000213

**Discussion.** The "/etc/passwd-" file is a backup file of "/etc/passwd", and as such contains information about the users that are configured on the system. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/passwd-" file is owned by "root" with the following command:

$ sudo stat -c "%U %n" /etc/passwd-
root /etc/passwd-

If the "/etc/passwd-" file does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the owner of the "/etc/passwd-" file is set to "root" by running the following command:

$ sudo chown root /etc/passwd-
```

## V-281028 RHEL 10 must be configured so that the "/etc/passwd-" file is group-owned by "root". {#V-281028}

Severity: medium · Rule: SV-281028r1268226_rule · STIG ID: RHEL-10-400055 · CCI-000213

**Discussion.** The "/etc/passwd-" file is a backup file of "/etc/passwd", and as such contains information about the users that are configured on the system. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/passwd-" file is group-owned by "root" with the following command:

$ sudo stat -c "%G %n" /etc/passwd-
root /etc/passwd-

If the "/etc/passwd-" file does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the group of the "/etc/passwd-" file is set to "root" by running the following command:

$ sudo chgrp root /etc/passwd-
```

## V-281029 RHEL 10 must be configured so that the "/etc/shadow" file is owned by "root". {#V-281029}

Severity: medium · Rule: SV-281029r1268226_rule · STIG ID: RHEL-10-400060 · CCI-000213

**Discussion.** The "/etc/shadow" file contains the list of local system accounts and stores password hashes. Protection of this file is critical for system security. Failure to give ownership of this file to "root" provides the designated owner with access to sensitive information, which could weaken the system security posture.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/shadow" file is owned by "root" with the following command:

$ sudo stat -c "%U %n" /etc/shadow
root /etc/shadow

If the "/etc/shadow" file does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the owner of the "/etc/shadow" file is set to "root" by running the following command:

$ sudo chown root /etc/shadow
```

## V-281030 RHEL 10 must be configured so that the "/etc/shadow" file is group-owned by "root". {#V-281030}

Severity: medium · Rule: SV-281030r1268226_rule · STIG ID: RHEL-10-400065 · CCI-000213

**Discussion.** The "/etc/shadow" file stores password hashes. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/shadow" file is group-owned by "root" with the following command:

$ sudo stat -c "%G %n" /etc/shadow
root /etc/shadow

If the "/etc/shadow" file does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the group of the "/etc/shadow" file is set to "root" by running the following command:

$ sudo chgrp root /etc/shadow
```

## V-281031 RHEL 10 must be configured so that the "/etc/shadow-" file is owned by "root". {#V-281031}

Severity: medium · Rule: SV-281031r1268226_rule · STIG ID: RHEL-10-400070 · CCI-000213

**Discussion.** The "/etc/shadow-" file is a backup file of "/etc/shadow", and as such contains the list of local system accounts and password hashes. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/shadow-" file is owned by "root" with the following command:

$ sudo stat -c "%U %n" /etc/shadow-
root /etc/shadow-

If the "/etc/shadow-" file does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the owner of the "/etc/shadow-" file is set to "root" by running the following command:

$ sudo chown root /etc/shadow-
```

## V-281032 RHEL 10 must be configured so that the "/etc/shadow-" file is group-owned by "root". {#V-281032}

Severity: medium · Rule: SV-281032r1268226_rule · STIG ID: RHEL-10-400075 · CCI-000213

**Discussion.** The "/etc/shadow-" file is a backup file of "/etc/shadow", and as such contains the list of local system accounts and password hashes. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/shadow-" file is group-owned by "root" with the following command:

$ sudo stat -c "%G %n" /etc/shadow-
root /etc/shadow-

If the "/etc/shadow-" file does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the group of the "/etc/shadow-" file is set to "root" by running the following command:

$ sudo chgrp root /etc/shadow-
```

## V-281033 RHEL 10 must be configured so that the "/var/log" directory is owned by "root". {#V-281033}

Severity: medium · Rule: SV-281033r1165454_rule · STIG ID: RHEL-10-400080 · CCI-001314

**Discussion.** Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the RHEL 10 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives.

The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.

**Check.**

```
Verify RHEL 10 is configured so that the "/var/log" directory is owned by "root" with the following command:

$ stat -c "%U %n" /var/log
root /var/log

If "/var/log" does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the owner of the directory "/var/log" is set to "root" by running the following command:

$ sudo chown root /var/log
```

## V-281034 RHEL 10 must be configured so that the "/var/log" directory is group-owned by "root". {#V-281034}

Severity: medium · Rule: SV-281034r1165457_rule · STIG ID: RHEL-10-400085 · CCI-001314

**Discussion.** Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the RHEL 10 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives.

The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.

**Check.**

```
Verify RHEL 10 is configured so that the "/var/log" directory is group-owned by "root" with the following command:

$ stat -c "%G %n" /var/log
root /var/log

If "/var/log" does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the group owner of the directory "/var/log" is set to "root" by running the following command:

$ sudo chgrp root /var/log
```

## V-281035 RHEL 10 must be configured so that the "/var/log/"messages file is owned by root. {#V-281035}

Severity: medium · Rule: SV-281035r1165460_rule · STIG ID: RHEL-10-400090 · CCI-001314

**Discussion.** Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the RHEL 10 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives.

The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.

**Check.**

```
Verify RHEL 10 is configured so that the "/var/log/messages" file is owned by root with the following command:

$ stat -c "%U %n" /var/log/messages
root /var/log/messages

If "/var/log/messages" does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the owner of the "/var/log/messages" file is set to "root" by running the following command:

$ sudo chown root /var/log/messages
```

## V-281036 RHEL 10 must be configured so that the "/var/log/messages" file is group-owned by "root". {#V-281036}

Severity: medium · Rule: SV-281036r1165463_rule · STIG ID: RHEL-10-400095 · CCI-001314

**Discussion.** Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the RHEL 10 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives.

The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.

**Check.**

```
Verify RHEL 10 is configured so that the "/var/log/messages" file is group-owned by "root" with the following command:

$ stat -c "%G %n" /var/log/messages
root /var/log/messages

If "/var/log/messages" does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the group owner of the "/var/log/messages" file is set to "root" by running the following command:

$ sudo chgrp root /var/log/messages
```

## V-281037 RHEL 10 must be configured so that system commands are owned by "root". {#V-281037}

Severity: medium · Rule: SV-281037r1165466_rule · STIG ID: RHEL-10-400100 · CCI-001499

**Discussion.** If RHEL 10 allowed any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.

This requirement applies to RHEL 10 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.

**Check.**

```
Verify RHEL 10 is configured so that the system commands contained in the following directories are owned by "root" with the following command:

$ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/libexec /usr/local/bin /usr/local/sbin ! -user root -exec stat -L -c "%U %n" {} \;

If any system commands are found to not be owned by root, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the system commands are protected from unauthorized access.

Run the following command, replacing "[FILE]" with any system command file not owned by "root".

$ sudo chown root [FILE]
```

## V-281038 RHEL 10 must be configured so that system commands are group-owned by root or a system account. {#V-281038}

Severity: medium · Rule: SV-281038r1184683_rule · STIG ID: RHEL-10-400105 · CCI-001499

**Discussion.** If RHEL 10 allowed any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.

This requirement applies to RHEL 10 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.

**Check.**

```
Verify RHEL 10 is configured so that the system commands contained in the following directories are group-owned by "root", or a required system account, with the following command:

$ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/libexec /usr/local/bin /usr/local/sbin ! -group root -exec stat -L -c "%G %n" {} \;

If any system commands are returned and are not group-owned by "root" or a required system account, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the system commands are protected from unauthorized access.

Run the following command, replacing "[FILE]" with any system command file not group-owned by "root" or a required system account.

$ sudo chgrp root [FILE]
```

## V-281039 RHEL 10 must be configured so that library files are owned by "root". {#V-281039}

Severity: medium · Rule: SV-281039r1165472_rule · STIG ID: RHEL-10-400110 · CCI-001499

**Discussion.** If RHEL 10 allowed any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.

This requirement applies to RHEL 10 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.

**Check.**

```
Verify RHEL 10 is configured so that the systemwide shared library files are owned by "root" with the following command:

$ sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -user root ! -type d -exec stat -L -c "%U %n" {} \;

If any systemwide shared library file is not owned by root, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the systemwide shared library files (/lib, /lib64, /usr/lib, and /usr/lib64) are protected from unauthorized access.

Run the following command, replacing "[FILE]" with any library file not owned by "root".

$ sudo chown root [FILE]
```

## V-281040 RHEL 10 must be configured so that library files are group-owned by "root" or a system account. {#V-281040}

Severity: medium · Rule: SV-281040r1184734_rule · STIG ID: RHEL-10-400115 · CCI-001499

**Discussion.** If RHEL 10 allowed any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.

This requirement applies to RHEL 10 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.

**Check.**

```
Verify RHEL 10 is configured so that the systemwide shared library files are group-owned by "root"  or a system account with the following command:

$ sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -group root ! -type d -exec stat -L -c "%G %n" {} \;

If any systemwide shared library file is returned and is not group-owned by "root" or a required system account, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the systemwide shared library files (/lib, /lib64, /usr/lib, and /usr/lib64) are protected from unauthorized access.

Run the following command, replacing "[FILE]" with any library file not group-owned by "root".

$ sudo chgrp root [FILE]
```

## V-281041 RHEL 10 must be configured so that library directories are owned by "root". {#V-281041}

Severity: medium · Rule: SV-281041r1165478_rule · STIG ID: RHEL-10-400120 · CCI-001499

**Discussion.** If RHEL 10 allowed any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.

This requirement applies to RHEL 10 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.

**Check.**

```
Verify RHEL 10 is configured so that the systemwide shared library directories are owned by "root" with the following command:

$ sudo find /lib /lib64 /usr/lib /usr/lib64 ! -user root -type d -exec stat -c "%U %n" {} \;

If any systemwide shared library directory is not owned by "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the systemwide shared library directories (/lib, /lib64, /usr/lib, and /usr/lib64) are protected from unauthorized access.

Run the following command, replacing "[DIRECTORY]" with any library directory not owned by "root".

$ sudo chown root [DIRECTORY]
```

## V-281042 RHEL 10 must be configured so that library directories are group-owned by "root" or a system account. {#V-281042}

Severity: medium · Rule: SV-281042r1184676_rule · STIG ID: RHEL-10-400125 · CCI-001499

**Discussion.** If RHEL 10 allowed any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.

This requirement applies to RHEL 10 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.

**Check.**

```
Verify RHEL 10 is configured so that the systemwide shared library directories are group-owned by "root" or a system account with the following command:

$ sudo find /lib /lib64 /usr/lib /usr/lib64 ! -group root -type d -exec stat -c "%G %n" {} \;

If any systemwide shared library directory is returned and is not group-owned by "root" or a required system account, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the systemwide shared library directories (/lib, /lib64, /usr/lib and /usr/lib64) are protected from unauthorized access.

Run the following command, replacing "[DIRECTORY]" with any library directory not group-owned by "root".

$ sudo chgrp root [DIRECTORY]
```

## V-281043 RHEL 10 must be configured so that cron configuration file directories are owned by root. {#V-281043}

Severity: medium · Rule: SV-281043r1184617_rule · STIG ID: RHEL-10-400130 · CCI-002696

**Discussion.** Service configuration files enable or disable features of their respective services, which if configured incorrectly could lead to insecure and vulnerable configurations. Therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.

**Check.**

```
Verify RHEL 10 ownership of all cron configuration files with the following command:

$ stat -c "%U %n" /etc/cron*
root /etc/cron.d
root /etc/cron.daily
root /etc/cron.deny
root /etc/cron.hourly
root /etc/cron.monthly
root /etc/crontab
root /etc/cron.weekly

If any crontab is not owned by root, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that cron configuration file directories are owned by root with the following command:

$ sudo chown root [cron config file]
```

## V-281044 RHEL 10 must be configured so that cron configuration files directories are group-owned by root. {#V-281044}

Severity: medium · Rule: SV-281044r1268226_rule · STIG ID: RHEL-10-400135 · CCI-000213

**Discussion.** Service configuration files enable or disable features of their respective services, which if configured incorrectly can lead to insecure and vulnerable configurations. Therefore, service configuration files should be owned by the correct group to prevent unauthorized changes.

**Check.**

```
Verify RHEL 10 group ownership of all cron configuration files with the following command:

$ stat -c "%G %n" /etc/cron*
root /etc/cron.d
root /etc/cron.daily
root /etc/cron.deny
root /etc/cron.hourly
root /etc/cron.monthly
root /etc/crontab
root /etc/cron.weekly

If any crontab is not group-owned by "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that any cron configuration file directories are group-owned by "root" with the following command:

$ sudo chgrp root [cron config file]
```

## V-281045 RHEL 10 must be configured so that world-writable directories are owned by root, sys, bin, or an application user. {#V-281045}

Severity: medium · Rule: SV-281045r1268233_rule · STIG ID: RHEL-10-400140 · CCI-001090

**Discussion.** If a world-writable directory is not owned by root, sys, bin, or an application user identifier (UID), unauthorized users may be able to modify files created by others.

The only authorized public directories are temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.

**Check.**

```
Verify RHEL 10 world-writable directories are owned by root, a system account, or an application account with the following command:

$ sudo find / -xdev -type d -perm -0002 -uid +999 -exec stat -c "%U, %u, %A, %n" {} \; 2>/dev/null

If output indicates that world-writable directories are owned by any account other than root or an approved system account, this is a finding.
```

**Fix.**

```
Configure RHEL 10 public directories to be owned by root or a system account to prevent unauthorized and unintended information transferred via shared system resources.

Use the following command template to set ownership of public directories to root or a system account:

$ sudo chown [root or system account] [Public Directory]
```

## V-281046 RHEL 10 must be configured so that all system device files are correctly labeled to prevent unauthorized modification. {#V-281046}

Severity: medium · Rule: SV-281046r1268226_rule · STIG ID: RHEL-10-400145 · CCI-000213

**Discussion.** If an unauthorized or modified device is allowed to exist on the system, the system may perform unintended or unauthorized operations.

**Check.**

```
Verify RHEL 10 is configured so that all system device files are correctly labeled to prevent unauthorized modification.

List all device files on the system that are incorrectly labeled with the following commands:

Note: Device files are normally found under "/dev", but applications may place device files in other directories and may necessitate a search of the entire system.

$ sudo find /dev -context *:device_t:* \( -type c -o -type b \) -printf "%p %Z\n"

$ sudo find /dev -context *:unlabeled_t:* \( -type c -o -type b \) -printf "%p %Z\n"

Note: There are device files, such as "/dev/vmci", that are used when the operating system is a host virtual machine. They will not be owned by a user on the system and require the "device_t" label to operate. These device files are not a finding.

If there is output from either of these commands, other than already noted, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that all system device files are correctly labeled to prevent unauthorized modification.

Restore the SELinux policy for the affected device file from the system policy database using the following command:

$ sudo restorecon -v <device_path>

Substitute "<device_path>" with the path to the affected device file (from the output of the previous commands). An example device file path would be "/dev/ttyUSB0". 

If the output of the above command does not indicate that the device was relabeled to a more specific SELinux type label, the SELinux policy of the system must be updated with more specific policy for the device class specified. 

If a package was used to install support for a device class, that package could be reinstalled using the following command:

$ sudo dnf reinstall <package_name>

If a package was not used to install the SELinux policy for a given device class, it must be generated manually and provide specific type labels.
```

## V-281047 RHEL 10 must be configured so that the Secure Shell (SSH) server configuration file is group-owned by "root". {#V-281047}

Severity: medium · Rule: SV-281047r1268226_rule · STIG ID: RHEL-10-400150 · CCI-000213

**Discussion.** Service configuration files enable or disable features of their respective services, which if configured incorrectly can lead to insecure and vulnerable configurations. Therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/ssh/sshd_config" file and the contents of "/etc/ssh/sshd_config.d" are group-owned by "root" with the following command:

$ sudo find /etc/ssh/sshd_config /etc/ssh/sshd_config.d -exec stat -c "%G %n" {} \;
root /etc/ssh/sshd_config
root /etc/ssh/sshd_config.d
root /etc/ssh/sshd_config.d/50-cloud-init.conf
root /etc/ssh/sshd_config.d/50-redhat.conf

If the "/etc/ssh/sshd_config" file or "/etc/ssh/sshd_config.d" or any files in the "sshd_config.d" directory do not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the "/etc/ssh/sshd_config" file and the contents of "/etc/ssh/sshd_config.d" are group-owned by "root" with the following command:

$ sudo chgrp root /etc/ssh/sshd_config /etc/ssh/sshd_config.d
```

## V-281048 RHEL 10 must be configured so that the Secure Shell (SSH) server configuration file is owned by "root". {#V-281048}

Severity: medium · Rule: SV-281048r1268226_rule · STIG ID: RHEL-10-400155 · CCI-000213

**Discussion.** Service configuration files enable or disable features of their respective services, which if configured incorrectly can lead to insecure and vulnerable configurations. Therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/ssh/sshd_config" file and the contents of "/etc/ssh/sshd_config.d" are owned by root with the following command:

$ sudo find /etc/ssh/sshd_config /etc/ssh/sshd_config.d -exec stat -c "%U %n" {} \;
root /etc/ssh/sshd_config
root /etc/ssh/sshd_config.d
root /etc/ssh/sshd_config.d/50-cloud-init.conf
root /etc/ssh/sshd_config.d/50-redhat.conf

If the "/etc/ssh/sshd_config" file or "/etc/ssh/sshd_config.d" or any files in the "sshd_config.d" directory do not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the "/etc/ssh/sshd_config" file and the contents of "/etc/ssh/sshd_config.d" are owned by "root" with the following command:

$ sudo chown -R root /etc/ssh/sshd_config /etc/ssh/sshd_config.d
```

## V-281049 RHEL 10 must ensure that all local interactive user home directories are group-owned by the home directory owner's primary group. {#V-281049}

Severity: medium · Rule: SV-281049r1268226_rule · STIG ID: RHEL-10-400160 · CCI-000213 CCI-002385

**Discussion.** If the group identifier (GID) of a local interactive user's home directory is not the same as the primary GID of the user, this would allow unauthorized access to the user's files. Users who share the same group may not be able to access files that they legitimately should be able to access.

Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000420-GPOS-00186

**Check.**

```
Verify RHEL 10 interactive users' home directories are group-owned by the user's primary GID with the following command:

Note: This may miss local interactive users that have been assigned a privileged user identifier (UID). Evidence of interactive use may be obtained from several log files containing system login information. The returned directory "/home/disauser" is used as an example.

$ sudo ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd)
drwxr-x--- 2 disauser admin 4096 Jun 5 12:41 disauser

Check the user's primary group with the following command:

$ sudo grep $(grep disauser /etc/passwd | awk -F: '{print $4}') /etc/group
admin:x:250:disauser,doduser,nsauser

If the user home directory referenced in "/etc/passwd" is not group-owned by that user's primary GID, this is a finding.
```

**Fix.**

```
Configure RHEL 10 interactive users' home directories to be group-owned by the user's primary GID.

Change the group owner of a local interactive user's home directory to the group found in "/etc/passwd". To change the group owner of a local interactive user's home directory, use the following command:

Note: The example will be for the user "disauser", who has a home directory of "/home/disauser" and has a primary group of users.

$ sudo chgrp users /home/disauser
```

## V-281050 RHEL 10 must enforce group ownership of audit logs by "root" or by a restricted logging group to prevent unauthorized read access. {#V-281050}

Severity: medium · Rule: SV-281050r1184685_rule · STIG ID: RHEL-10-400165 · CCI-000162 CCI-000163 CCI-000164 CCI-001314

**Discussion.** Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality.

Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084

**Check.**

```
Verify RHEL 10 audit logs are group-owned by "root" or a restricted logging group.

Determine where the audit logs are stored with the following command:

$ sudo grep -iw log_file /etc/audit/auditd.conf
log_file = /var/log/audit/audit.log

Using the location of the audit log file, determine if the audit log is group-owned by "root" using the following command:

$ sudo stat -c "%G %n" /var/log/audit/audit.log
root /var/log/audit/audit.log

If the audit log is not group-owned by "root" or the configured alternative logging group, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent unauthorized read access by ensuring that audit logs are group-owned by root or by a restricted logging group.

Change the group of the directory of "/var/log/audit" to be owned by a correct group.

Identify the group that is configured to own audit logs:

$ sudo grep -P '^[ ]*log_group[ ]+=.*$' /etc/audit/auditd.conf

Change the ownership to that group:

$ sudo chgrp ${GROUP} /var/log/audit
```

## V-281051 RHEL 10 must enforce "root" ownership of the audit log directory to prevent unauthorized read access. {#V-281051}

Severity: medium · Rule: SV-281051r1165508_rule · STIG ID: RHEL-10-400170 · CCI-000162 CCI-000163 CCI-000164 CCI-001314

**Discussion.** Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality.

Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084

**Check.**

```
Verify RHEL 10 audit logs directory is owned by "root".

Determine where the audit logs are stored with the following command:

$ sudo grep -iw log_file /etc/audit/auditd.conf
log_file = /var/log/audit/audit.log

Using the location of the audit log file, determine if the audit log directory is owned by "root" using the following command:

$ sudo stat -c '%U %n' /var/log/audit
root /var/log/audit

If the audit log directory is not owned by "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent unauthorized read access by ensuring the audit log directory is "root" owned with the following command:

$ sudo chown root /var/log/audit
```

## V-281052 RHEL 10 must enforce "root" ownership of audit logs to prevent unauthorized access. {#V-281052}

Severity: medium · Rule: SV-281052r1165511_rule · STIG ID: RHEL-10-400175 · CCI-000162 CCI-000163 CCI-000164 CCI-001314

**Discussion.** Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality.

Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084

**Check.**

```
Verify RHEL 10 enforces "root" ownership of audit logs to prevent unauthorized access.

Determine where the audit logs are stored with the following command:

$ sudo grep "^log_file" /etc/audit/auditd.conf
log_file = /var/log/audit/audit.log

Using the location of the audit log file, determine if the audit log files are owned by "root" using the following command:

$ sudo ls -la /var/log/audit/audit.log
rw-------. 2 root root 237923 Jun 11 11:56 /var/log/audit/audit.log

If the audit logs are not owned by "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce "root" ownership of audit logs to prevent unauthorized access with the following command:

$ sudo chown root [audit_log_file]

Replace "[audit_log_file]" with the correct audit log path. By default this location is "/var/log/audit/audit.log".
```

## V-281053 RHEL 10 must enforce group ownership by "root" or a restricted logging group for audit log files to prevent unauthorized access. {#V-281053}

Severity: medium · Rule: SV-281053r1165514_rule · STIG ID: RHEL-10-400180 · CCI-000162 CCI-000163 CCI-000164 CCI-001314

**Discussion.** Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality.

Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084

**Check.**

```
Verify RHEL 10 enforces group ownership by "root" or a restricted logging group for audit log files to prevent unauthorized access.

Determine where the audit logs are stored with the following command:

$ sudo grep "^log_file" /etc/audit/auditd.conf
log_file = /var/log/audit/audit.log

Determine the audit log group by running the following command:

$ sudo grep -P '^[ ]*log_group[ ]+=.*$' /etc/audit/auditd.conf
log_group = root

Check that the audit log file is owned by the correct group. Run the following command to display the owner of the audit log file:

$ sudo stat -c "%n %G" /var/log/audit/audit.log
/var/log/audit/audit.log root

The audit log file must be owned by the "log_group" or by "root" if the "log_group" is not specified.

If audit log files are owned by the incorrect group, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce group ownership by "root" or a restricted logging group for audit log files to prevent unauthorized access.

Identify the group that is configured to own the audit log:

$ sudo grep -P '^[ ]*log_group[ ]+=.*$' /etc/audit/auditd.conf

Change the ownership to that group using the following command:

$ sudo chgrp ${log_group} ${log_file}
```

## V-281054 RHEL 10 must set mode "0600" or less permissive for the audit logs file to prevent unauthorized access to the audit log. {#V-281054}

Severity: medium · Rule: SV-281054r1197224_rule · STIG ID: RHEL-10-400185 · CCI-000162 CCI-000163 CCI-000164 CCI-001314

**Discussion.** Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the RHEL 10 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives.

The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.

Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084

**Check.**

```
Verify RHEL 10 audit logs have a mode of "0600".

Determine where the audit logs are stored with the following command:

$ sudo grep "^log_file" /etc/audit/auditd.conf
log_file = /var/log/audit/audit.log

Using the location of the audit log file, determine the mode of each audit log with the following command:

$ sudo find /var/log/audit/ -type f -exec stat -c '%a %n' {} \;
600 /var/log/audit/audit.log

If the audit logs have a mode more permissive than "0600", this is a finding.
```

**Fix.**

```
Configure RHEL 10 audit logs to have a mode of "0600" with the following command:

Replace "[audit_log_file]" with the path to each audit log file. By default, these logs are located in "/var/log/audit/":

$ sudo chmod 0600 /var/log/audit/[audit_log_file]

Check the group that owns the system audit logs:

$ sudo grep -iw log_group /etc/audit/auditd.conf

If "log_group" is set to a user other than "root", configure the permissions the following way:

$ sudo chmod 0640 $log_file
$ sudo chmod 0440 $log_file.*

Otherwise, configure the permissions the following way:

$ sudo chmod 0600 $log_file
$ sudo chmod 0400 $log_file.*
```

## V-281055 RHEL 10 must enforce the audit log directory to have a mode of "0750" or less permissive to prevent unauthorized read access. {#V-281055}

Severity: medium · Rule: SV-281055r1165520_rule · STIG ID: RHEL-10-400190 · CCI-000162 CCI-000163 CCI-000164

**Discussion.** If users can write to audit logs, audit trails can be modified or destroyed.

Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029

**Check.**

```
Verify RHEL 10 enforces the audit log directory to have a mode of "0750" or less permissive to prevent unauthorized read access.

Determine where the audit logs are stored with the following command:

$ sudo grep "^log_file" /etc/audit/auditd.conf
log_file = /var/log/audit/audit.log

Find the group that owns audit logs:

$ sudo grep "^log_group" /etc/audit/auditd.conf
log_group = root

Run the following command to check the mode of the system audit logs:

$ sudo stat -c "%a %n" [audit_log_directory]

Replace "[audit_log_directory]" to the correct audit log directory path; by default this location is "/var/log/audit".

If the log_group is "root" or is not set, the correct permissions are "0700".
 
If the log_group is owned by anyone other than "root", the correct permissions are "0750".

If audit logs have a more permissive mode than is required, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the audit log directories have a mode of "0750" or less permissive to prevent unauthorized read access with the following command:

$ sudo chmod 0700 /var/log/audit

Note: The correct permissions are "0700" if the directory is owned by "root"; otherwise, the correct permissions are "0750".

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281056 RHEL 10 must enforce root ownership of the "/etc/audit/" directory. {#V-281056}

Severity: medium · Rule: SV-281056r1165523_rule · STIG ID: RHEL-10-400195 · CCI-000171

**Discussion.** The "/etc/audit/" directory contains files that ensure the proper auditing of command execution, privilege escalation, file manipulation, and more. Protection of this directory is critical for system security.

**Check.**

```
Verify RHEL 10 enforces root ownership of the "/etc/audit/" directory with the following command:

$ sudo stat -c "%U %n" /etc/audit/
root /etc/audit/

If the "/etc/audit/" directory does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the "/etc/audit/" directory is owned by "root" with the following command:

$ sudo chown root /etc/audit/
```

## V-281057 RHEL 10 must enforce root group ownership of the "/etc/audit/" directory. {#V-281057}

Severity: medium · Rule: SV-281057r1165526_rule · STIG ID: RHEL-10-400200 · CCI-000171

**Discussion.** The "/etc/audit/" directory contains files that ensure the proper auditing of command execution, privilege escalation, file manipulation, and more. Protection of this directory is critical for system security.

**Check.**

```
Verify RHEL 10 enforces root group ownership of the "/etc/audit/" directory with the following command:

$ sudo stat -c "%G %n" /etc/audit/
root /etc/audit/

If "/etc/audit/" does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the "/etc/audit/" directory is group-owned by "root" with the following command:

$ sudo chgrp root /etc/audit/
```

## V-281058 RHEL 10 must enforce mode "755" or less permissive for system commands. {#V-281058}

Severity: medium · Rule: SV-281058r1165529_rule · STIG ID: RHEL-10-400205 · CCI-001499

**Discussion.** If RHEL 10 allowed any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.

This requirement applies to RHEL 10 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.

**Check.**

```
Verify RHEL 10 is configured so that the system commands contained in the following directories have mode "755" or less permissive with the following command:

$ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/libexec /usr/local/bin /usr/local/sbin -perm /022 -exec ls -l {} \;

If any system commands are found to be group-writable or world-writable, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the system commands to be protected from unauthorized access.

Run the following command, replacing "[FILE]" with any system command with a mode more permissive than "755".

$ sudo chmod 755 [FILE]
```

## V-281059 RHEL 10 must enforce mode "755" or less permissive on library directories. {#V-281059}

Severity: medium · Rule: SV-281059r1165532_rule · STIG ID: RHEL-10-400210 · CCI-001499

**Discussion.** If RHEL 10 allowed any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.

This requirement applies to RHEL 10 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.

**Check.**

```
Verify RHEL 10 is configured so that the systemwide shared library directories have mode "755" or less permissive with the following command:

$ sudo find -L /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type d -exec ls -l {} \;

If any systemwide shared library file is found to be group-writable or world-writable, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the systemwide shared library directories (/lib, /lib64, /usr/lib, and /usr/lib64) are protected from unauthorized access.

Run the following command, replacing "[DIRECTORY]" with any library directory with a mode more permissive than "755".

$ sudo chmod 755 [DIRECTORY]
```

## V-281060 RHEL 10 must enforce mode "755" or less permissive for library files. {#V-281060}

Severity: medium · Rule: SV-281060r1165535_rule · STIG ID: RHEL-10-400215 · CCI-001499

**Discussion.** If RHEL 10 allowed any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.

This requirement applies to RHEL 10 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.

**Check.**

```
Verify RHEL 10 is configured so that the systemwide shared library files contained in the following directories have mode "755" or less permissive with the following command:

$ sudo find -L /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type f -exec ls -l {} \;

If any systemwide shared library file is found to be group-writable or world-writable, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the library files are protected from unauthorized access. Run the following command, replacing "[FILE]" with any library file with a mode more permissive than "755".

$ sudo chmod 755 [FILE]
```

## V-281061 RHEL 10 must enforce mode "0755" or less permissive for the "/var/log" directory. {#V-281061}

Severity: medium · Rule: SV-281061r1165538_rule · STIG ID: RHEL-10-400220 · CCI-001314

**Discussion.** Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the RHEL 10 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives.

The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.

**Check.**

```
Verify RHEL 10 is configured so that the "/var/log" directory has a mode of "0755" or less permissive with the following command:

$ stat -c '%a %n' /var/log
755 /var/log

If "/var/log" does not have a mode of "0755" or less permissive, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the "/var/log" directory has a mode of "0755" by running the following command:

$ sudo chmod 0755 /var/log
```

## V-281062 RHEL 10 must enforce mode "0640" or less permissive for the "/var/log/messages" file. {#V-281062}

Severity: medium · Rule: SV-281062r1165541_rule · STIG ID: RHEL-10-400225 · CCI-001314

**Discussion.** Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the RHEL 10 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives.

The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.

**Check.**

```
Verify RHEL 10 is configured so that the "/var/log/messages" file has a mode of "0640" or less permissive with the following command:

$ stat -c '%a %n' /var/log/messages
600 /var/log/messages

If "/var/log/messages" does not have a mode of "0640" or less permissive, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the "/var/log/messages" file has a mode of "0640" by running the following command:

$ sudo chmod 0640 /var/log/messages
```

## V-281063 RHEL 10 must be configured to prohibit modification of permissions for cron configuration files and directories from the operating system defaults. {#V-281063}

Severity: medium · Rule: SV-281063r1195403_rule · STIG ID: RHEL-10-400230 · CCI-000381

**Discussion.** If the permissions of cron configuration files or directories are modified from the operating system defaults, it may be possible for individuals to insert unauthorized cron jobs that perform unauthorized actions, including potentially escalating privileges.

**Check.**

```
Verify RHEL 10 is configured so that the owner, group, and mode of cron configuration files and directories match the operating system defaults with the following command:

$ rpm --verify cronie crontabs | awk '! ($2 == "c" && $1 ~ /^.\..\.\.\.\..\./) {print $0}'

If the command returns any output, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prohibit modification of permissions for cron configuration files and directories from the operating system defaults with the following commands:

$ sudo dnf reinstall cronie crontabs
$ rpm --setugids cronie crontabs
$ rpm --setperms cronie crontabs
```

## V-281064 RHEL 10 must enforce mode "0740" or less permissive for local initialization files. {#V-281064}

Severity: medium · Rule: SV-281064r1268226_rule · STIG ID: RHEL-10-400235 · CCI-000213

**Discussion.** Local initialization files are used to configure the user's shell environment upon login. Malicious modification of these files could compromise accounts upon login.

**Check.**

```
Verify RHEL 10 is configured so that all local initialization files have a mode of "0740" or less permissive with the following command:

Note: The example will be for the "disauser" user, who has a home directory of "/home/disauser".

$ sudo find /home -maxdepth 2 -type f -name ".*" -exec stat -c "%n %a" {} \; | awk '$2 > 740'
/home/disauser/.bash_profile 770 

If any local initialization files are returned, this indicates a mode more permissive than "0740", and this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that all local initialization files have a mode of "0740" or less permissive with the following command:

Note: The example will be for the "disauser" user, who has a home directory of "/home/disauser".

$ sudo chmod 0740 /home/disauser/.<INIT_FILE>
```

## V-281065 RHEL 10 must enforce mode "0750" or less permissive for local interactive user home directories. {#V-281065}

Severity: medium · Rule: SV-281065r1268226_rule · STIG ID: RHEL-10-400240 · CCI-000213

**Discussion.** Excessive permissions on local interactive user home directories may allow unauthorized access to user files by other users.

**Check.**

```
Verify RHEL 10 is configured so that the assigned home directory of all local interactive users has a mode of "0750" or less permissive with the following command:

Note: This may miss interactive users that have been assigned a privileged user identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system login information.

$ stat -L -c '%a %n' $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) 2>/dev/null
700 /home/disauser

If home directories referenced in "/etc/passwd" do not have a mode of "0750" or less permissive, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the mode of interactive user's home directories is set to "0750". 

To change the mode of a local interactive user's home directory, use the following command:

Note: The example will be for the user "disauser".

$ sudo chmod 0750 /home/disauser
```

## V-281066 RHEL 10 must enforce mode "0644" or less permissive for the "/etc/group" file to prevent unauthorized access. {#V-281066}

Severity: medium · Rule: SV-281066r1268226_rule · STIG ID: RHEL-10-400245 · CCI-000213

**Discussion.** The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/group" file has mode "0644" or less permissive with the following command:

$ sudo stat -c "%a %n" /etc/group
644 /etc/group

If a value of "0644" or less permissive is not returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the mode of the file "/etc/group" is set to "0644" by running the following command:

$ sudo chmod 0644 /etc/group
```

## V-281067 RHEL 10 must enforce mode "0644" or less permissive for the "/etc/group-" file to prevent unauthorized access. {#V-281067}

Severity: medium · Rule: SV-281067r1268226_rule · STIG ID: RHEL-10-400250 · CCI-000213

**Discussion.** The "/etc/group-" file is a backup file of "/etc/group", and as such contains information regarding groups that are configured on the system. Protection of this file is important for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/group-" file has mode "0644" or less permissive with the following command:

$ sudo stat -c "%a %n" /etc/group-
644 /etc/group-

If a value of "0644" or less permissive is not returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the mode of the "/etc/group-" file is set to "0644" by running the following command:

$ sudo chmod 0644 /etc/group-
```

## V-281068 RHEL 10 must enforce mode "0000" or less permissive for the "/etc/gshadow" file to prevent unauthorized access. {#V-281068}

Severity: medium · Rule: SV-281068r1268226_rule · STIG ID: RHEL-10-400255 · CCI-000213

**Discussion.** The "/etc/gshadow" file contains group password hashes. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/gshadow" file has mode "0000" with the following command:

$ sudo stat -c "%a %n" /etc/gshadow
0 /etc/gshadow

If a value of "0" is not returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the mode of the "/etc/gshadow" file is set to "0000" by running the following command:

$ sudo chmod 0000 /etc/gshadow
```

## V-281069 RHEL 10 must enforce mode "0000" or less permissive for the "/etc/gshadow-" file to prevent unauthorized access. {#V-281069}

Severity: medium · Rule: SV-281069r1268226_rule · STIG ID: RHEL-10-400260 · CCI-000213

**Discussion.** The "/etc/gshadow-" file is a backup of "/etc/gshadow", and as such contains group password hashes. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/gshadow-" file has mode "0000" with the following command:

$ sudo stat -c "%a %n" /etc/gshadow-
0 /etc/gshadow-

If a value of "0" is not returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the mode of the "/etc/gshadow-" file is set to "0000" by running the following command:

$ sudo chmod 0000 /etc/gshadow-
```

## V-281070 RHEL 10 must enforce mode "0644" or less permissive for the "/etc/passwd" file to prevent unauthorized access. {#V-281070}

Severity: medium · Rule: SV-281070r1268226_rule · STIG ID: RHEL-10-400265 · CCI-000213

**Discussion.** If the "/etc/passwd" file is writable by a group-owner or the world, the risk of its compromise is increased. The file contains the list of accounts on the system and associated information, and protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/passwd" file has mode "0644" or less permissive with the following command:

$ sudo stat -c "%a %n" /etc/passwd
644 /etc/passwd

If a value of "0644" or less permissive is not returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the mode of the file "/etc/passwd" is set to "0644" by running the following command:

$ sudo chmod 0644 /etc/passwd
```

## V-281071 RHEL 10 must enforce mode "0644" or less permissive for "/etc/passwd-" file to prevent unauthorized access. {#V-281071}

Severity: medium · Rule: SV-281071r1268226_rule · STIG ID: RHEL-10-400270 · CCI-000213

**Discussion.** The "/etc/passwd-" file is a backup file of "/etc/passwd", and as such contains information about the users that are configured on the system. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/passwd-" file has mode "0644" or less permissive with the following command:

$ sudo stat -c "%a %n" /etc/passwd-
644 /etc/passwd-

If a value of "0644" or less permissive is not returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the mode of the "/etc/passwd-" file is set to "0644" by running the following command:

$ sudo chmod 0644 /etc/passwd-
```

## V-281072 RHEL 10 must enforce mode "0000" or less permissive for "/etc/shadow-" file to prevent unauthorized access. {#V-281072}

Severity: medium · Rule: SV-281072r1268226_rule · STIG ID: RHEL-10-400275 · CCI-000213

**Discussion.** The "/etc/shadow-" file is a backup file of "/etc/shadow", and as such contains the list of local system accounts and password hashes. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/shadow-" file has mode "0000" with the following command:

$ sudo stat -c "%a %n" /etc/shadow-
0 /etc/shadow-

If a value of "0" is not returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the mode of the "/etc/shadow-" file is set to "0000" by running the following command:

$ sudo chmod 0000 /etc/shadow-
```

## V-281073 RHEL 10 must be configured so that a sticky bit is set on all public directories. {#V-281073}

Severity: medium · Rule: SV-281073r1273578_rule · STIG ID: RHEL-10-400280 · CCI-001090

**Discussion.** Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection.

This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoW or other government agencies.

**Check.**

```
Verify RHEL 10 is configured so that all world-writable directories have the sticky bit set with the following command:

$ sudo find / -type d \( -perm -0002 -a ! -perm -1000 \) -print 2>/dev/null
drwxrwxrwt 7 root root 4096 Jul 26 11:19 /tmp

If any of the returned directories are world-writable and do not have the sticky bit set, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that all world-writable directories have the sticky bit set to prevent unauthorized and unintended information transferred via shared system resources.

Set the sticky bit on all world-writable directories using the following command (replace "[World-Writable Directory]" with any directory path missing the sticky bit):

$ chmod a+t [World-Writable Directory]
```

## V-281074 RHEL 10 must be configured so that all local files and directories have a valid group owner. {#V-281074}

Severity: medium · Rule: SV-281074r1268226_rule · STIG ID: RHEL-10-400285 · CCI-000213

**Discussion.** Files without a valid group owner may be unintentionally inherited if a group is assigned the same group identifier (GID) as the GID of the files without a valid group owner.

**Check.**

```
Verify RHEL 10 is configured so that all local files and directories have a valid group with the following command:

$ df --local -P | awk {'if (NR!=1) print $6'} | sudo xargs -I '{}' find '{}' -xdev -nogroup

If any files on the system do not have an assigned group, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that all local files and directories have a valid group owner.

Either remove all files and directories from RHEL 10 that do not have a valid group, or assign a valid group to all files and directories on the system with the "chgrp" command:

$ sudo chgrp <group> <file>
```

## V-281075 RHEL 10 must be configured so that all local files and directories must have a valid owner. {#V-281075}

Severity: medium · Rule: SV-281075r1268226_rule · STIG ID: RHEL-10-400290 · CCI-000213

**Discussion.** Unowned files and directories may be unintentionally inherited if a user is assigned the same user identifier (UID) as the UID of the unowned files.

**Check.**

```
Verify RHEL 10 is configured so that all local files and directories have a valid owner with the following command:

$ df --local -P | awk {'if (NR!=1) print $6'} | sudo xargs -I '{}' find '{}' -xdev -nouser

If any files on the system do not have an assigned owner, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that all local files and directories must have a valid owner.

Either remove all files and directories that do not have a valid user from the system, or assign a valid user to all unowned files and directories on RHEL 10 with the "chown" command:

$ sudo chown <user> <file>
```

## V-281076 RHEL 10 must enforce mode "0000" for "/etc/shadow" to prevent unauthorized access. {#V-281076}

Severity: medium · Rule: SV-281076r1268226_rule · STIG ID: RHEL-10-400295 · CCI-000213

**Discussion.** The "/etc/shadow" file contains the list of local system accounts and stores password hashes. Protection of this file is critical for system security. Failure to give ownership of this file to "root" provides the designated owner with access to sensitive information, which could weaken the system security posture.

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/shadow" file has mode "0000" with the following command:

$ sudo stat -c "%a %n" /etc/shadow
0 /etc/shadow

If a value of "0" is not returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce mode "0000" for "/etc/shadow" to prevent unauthorized access.

Change the mode of the file "/etc/shadow" to "0000" by running the following command:

$ sudo chmod 0000 /etc/shadow
```

## V-281077 RHEL 10 must be configured so that audit tools are owned by "root". {#V-281077}

Severity: medium · Rule: SV-281077r1165586_rule · STIG ID: RHEL-10-400300 · CCI-001493 CCI-001494 CCI-001495

**Discussion.** Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information.

RHEL 10 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools.

Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.

Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099

**Check.**

```
Verify RHEL 10 audit tools are owned by "root" with the following command:

$ sudo stat -c "%U %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/auditd /sbin/rsyslogd /sbin/augenrules
root /sbin/auditctl
root /sbin/aureport
root /sbin/ausearch
root /sbin/auditd
root /sbin/rsyslogd
root /sbin/augenrules

If any audit tools do not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the audit tools are owned by "root" by running the following command:

$ sudo chown root [audit_tool]

Replace "[audit_tool]" with each audit tool not owned by "root".
```

## V-281078 RHEL 10 must be configured so that audit tools are group-owned by "root". {#V-281078}

Severity: medium · Rule: SV-281078r1165589_rule · STIG ID: RHEL-10-400305 · CCI-001493 CCI-001494 CCI-001495

**Discussion.** Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data; therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information.

RHEL 10 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools.

Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.

Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099

**Check.**

```
Verify RHEL 10 audit tools are group-owned by "root" with the following command:

$ sudo stat -c "%G %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/auditd /sbin/rsyslogd /sbin/augenrules
root /sbin/auditctl
root /sbin/aureport
root /sbin/ausearch
root /sbin/auditd
root /sbin/rsyslogd
root /sbin/augenrules

If any audit tools do not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the audit tools are group-owned by "root" by running the following command:

$ sudo chgrp root [audit_tool]

Replace "[audit_tool]" with each audit tool not group-owned by "root".
```

## V-281079 RHEL 10 must set the umask value to "077" for all local interactive user accounts. {#V-281079}

Severity: medium · Rule: SV-281079r1268226_rule · STIG ID: RHEL-10-400310 · CCI-000213

**Discussion.** The umask controls the default access mode assigned to newly created files. A umask of "077" limits new files to mode 600 or less permissive. Although umask can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0". This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.

**Check.**

```
Verify RHEL 10 sets the default umask for all local interactive users to "077".

Identify the locations of all local interactive user home directories by looking at the "/etc/passwd" file.

Check all local interactive user initialization files for interactive users with the following command:

Note: The example is for a system that is configured to create users' home directories in the "/home" directory.

$ sudo find /home -maxdepth 2 -type f -name ".[^.]*" -exec grep -iH -d skip --exclude=.bash_history umask {} \;
/home/disauser/.bash_history:grep -i umask /etc/bashrc /etc/csh.cshrc /etc/profile
/home/disauser/.bash_history:grep -i umask /etc/login.defs

If any local interactive user initialization files are found to have a umask statement that sets a value less restrictive than "077", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to set the umask value for all local interactive user accounts to "077".

Remove the umask statement from all local interactive users' initialization files.

If the account is for an application, the requirement for a umask less restrictive than "077" can be documented with the information system security officer. However, the user agreement for access to the account must specify that the local interactive user must log in to their account first and then switch the user to the application account with the correct option to gain the account's environment variables.
```

## V-281080 RHEL 10 must define default permissions for the bash shell. {#V-281080}

Severity: medium · Rule: SV-281080r1268226_rule · STIG ID: RHEL-10-400315 · CCI-000213

**Discussion.** The "umask" controls the default access mode assigned to newly created files. A "umask" of "077" limits new files to mode "600" or less permissive. Although "umask" can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0". 

This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.

**Check.**

```
Verify RHEL 10 "umask" setting is configured correctly in the "/etc/bashrc" file with the following command:

Note: If the value of the "umask" parameter is set to "000" in the "/etc/bashrc" file, the Severity is raised to a CAT I.

$ sudo grep umask /etc/bashrc
[ `umask` -eq 0 ] && umask 077

If the value for the "umask" parameter is not "077", or the "umask" parameter is missing or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to define default permissions for all authenticated users using the bash shell.

Add or edit the lines for the "umask" parameter in the "/etc/bashrc" file to "077":

umask 077
```

## V-281081 RHEL 10 must define default permissions for the c shell. {#V-281081}

Severity: medium · Rule: SV-281081r1268226_rule · STIG ID: RHEL-10-400320 · CCI-000213

**Discussion.** The "umask" controls the default access mode assigned to newly created files. A "umask" of "077" limits new files to mode "600" or less permissive. Although "umask" can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0". 

This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.

**Check.**

```
Verify the RHEL 10 "umask" setting is configured correctly in the "/etc/csh.cshrc" file with the following command:

Note: If the value of the "umask" parameter is set to "000" in the "/etc/csh.cshrc" file, the Severity is raised to a CAT I.

$ sudo grep umask /etc/csh.cshrc
umask 077

If the value for the "umask" parameter is not "077", or the "umask" parameter is missing or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to define default permissions for all authenticated users using the c shell.

Add or edit the lines for the "umask" parameter in the "/etc/csh.cshrc" file to "077":

umask 077
```

## V-281082 RHEL 10 must define default permissions for all authenticated users in such a way that the user can read and modify only their own files. {#V-281082}

Severity: medium · Rule: SV-281082r1268226_rule · STIG ID: RHEL-10-400325 · CCI-000213

**Discussion.** Setting the most restrictive default permissions ensures that when new accounts are created, they do not have unnecessary access.

**Check.**

```
Verify RHEL 10 defines default permissions for all authenticated users in such a way that the user can only read and modify their own files with the following command:

Note: If the value of the "umask" parameter is set to "000" in "/etc/login.defs" file, the Severity is raised to a CAT I.

$ sudo grep -i umask /etc/login.defs
umask 077

If the value for the "umask" parameter is not "077", or the "umask" parameter is missing or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to define default permissions for all authenticated users in such a way that the user can read and modify only their own files.

Add or edit the lines for the "umask" parameter in the "/etc/login.defs" file to "077":

umask 077
```

## V-281083 RHEL 10 must define default permissions for the system default profile. {#V-281083}

Severity: medium · Rule: SV-281083r1268226_rule · STIG ID: RHEL-10-400330 · CCI-000213

**Discussion.** The "umask" controls the default access mode assigned to newly created files. A "umask" of "077" limits new files to mode "600" or less permissive. "Although umask" can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0". 

This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.

**Check.**

```
Verify the RHEL 10 "umask" setting is configured correctly in the "/etc/profile" file with the following command:

Note: If the value of the "umask" parameter is set to "000" in the "/etc/profile" file, the Severity is raised to a CAT I.

$ sudo grep umask /etc/profile
umask 077

If the value for the "umask" parameter is not "077", or the "umask" parameter is missing or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to define default permissions for all authenticated users in such a way that the user can read and modify only their own files.

Add or edit the lines for the "umask" parameter in the "/etc/profile" file to "077":

umask 077
```

## V-281084 RHEL 10 must enforce that all local initialization files configured by systemd-tmpfiles have mode "0600" or less permissive. {#V-281084}

Severity: medium · Rule: SV-281084r1268226_rule · STIG ID: RHEL-10-400335 · CCI-000213

**Discussion.** Excessive permissions on local interactive user home directories may allow unauthorized access to user files by other users.

**Check.**

```
Verify RHEL 10 enforces that all local initialization files configured by systemd-tmpfiles have mode "0600" or less permissive.

Check that all files from "/usr/share/rootfiles/" are overridden correctly in RHEL 10:
 
$ sudo grep /usr/share/rootfiles/ /etc/tmpfiles.d/*.conf
C /root/.bash_logout   600 root root - /usr/share/rootfiles/.bash_logout
C /root/.bash_profile  600 root root - /usr/share/rootfiles/.bash_profile
C /root/.bashrc        600 root root - /usr/share/rootfiles/.bashrc
C /root/.cshrc         600 root root - /usr/share/rootfiles/.cshrc
C /root/.tcshrc        600 root root - /usr/share/rootfiles/.tcshrc
 
If any files are not configured to "600", or if no files are found by grep, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce that all local initialization files configured by systemd-tmpfiles have mode "0600" or less permissive.

Ensure the following lines are in a ".conf" file under "/etc/tmpfiles.d/":
 
C /root/.bash_logout   600 root root - /usr/share/rootfiles/.bash_logout
C /root/.bash_profile  600 root root - /usr/share/rootfiles/.bash_profile
C /root/.bashrc        600 root root - /usr/share/rootfiles/.bashrc
C /root/.cshrc         600 root root - /usr/share/rootfiles/.cshrc
C /root/.tcshrc        600 root root - /usr/share/rootfiles/.tcshrc
```

## V-281085 RHEL 10 must enforce mode "0600" or less permissive for Secure Shell (SSH) private host key files. {#V-281085}

Severity: medium · Rule: SV-281085r1268226_rule · STIG ID: RHEL-10-400340 · CCI-000213

**Discussion.** If an unauthorized user obtains the private SSH host key file, the host could be impersonated.

**Check.**

```
Verify RHEL 10 enforces mode "0600" for SSH private host key files with the following command:

$ sudo stat -c "%a %n" /etc/ssh/*_key
600 /etc/ssh/ssh_host_ecdsa_key
600 /etc/ssh/ssh_host_ed25519_key
600 /etc/ssh/ssh_host_rsa_key

If any private host key file has a mode more permissive than "0600", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce mode "0600" for SSH private host key files with the following command:

$ sudo chmod 0600 /etc/ssh/ssh_host*key

Restart the SSH daemon for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281086 RHEL 10 must enforce "root" group ownership of the "/boot/grub2/grub.cfg" file. {#V-281086}

Severity: medium · Rule: SV-281086r1268226_rule · STIG ID: RHEL-10-400345 · CCI-000213

**Discussion.** The "root" group is a highly privileged group. Furthermore, the group owner of this file should not have any access privileges anyway.

**Check.**

```
Verify RHEL 10 enforces group ownership of the "/boot/grub2/grub.cfg" file with the following command:

$ sudo stat -c "%G %n" /boot/grub2/grub.cfg
root /boot/grub2/grub.cfg

If the "/boot/grub2/grub.cfg" file does not have a group owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce group ownership of the "/boot/grub2/grub.cfg" file.

Change the group owner of the file "/boot/grub2/grub.cfg" to "root" by running the following command:

$ sudo chgrp root /boot/grub2/grub.cfg
```

## V-281087 RHEL 10 must enforce "root" ownership of the "/boot/grub2/grub.cfg" file. {#V-281087}

Severity: medium · Rule: SV-281087r1268226_rule · STIG ID: RHEL-10-400350 · CCI-000213

**Discussion.** The " /boot/grub2/grub.cfg" file stores sensitive system configuration. Protection of this file is critical for system security.

**Check.**

```
Verify RHEL 10 enforces ownership of the "/boot/grub2/grub.cfg" file with the following command:

$ sudo stat -c "%U %n" /boot/grub2/grub.cfg
root /boot/grub2/grub.cfg

If the "/boot/grub2/grub.cfg" file does not have an owner of "root", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce ownership of the "/boot/grub2/grub.cfg" file.

Change the owner of the "/boot/grub2/grub.cfg" file to "root" by running the following command:

$ sudo chown root /boot/grub2/grub.cfg
```

## V-281088 RHEL 10 must prevent device files from being interpreted on file systems that contain user home directories. {#V-281088}

Severity: medium · Rule: SV-281088r1165619_rule · STIG ID: RHEL-10-400355 · CCI-001764

**Discussion.** The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.

**Check.**

```
Verify RHEL 10 is configured so that "/home" is mounted with the "nodev" option with the following command:

Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is automatically a finding, as the "nodev" option cannot be used on the "/" system.

$ mount | grep /home
/dev/mapper/luks-ca2261ed-7b00-4b7b-84cd-8cd6d8fa4b28 on /home type xfs (rw,nodev,nosuid,noexec,seclabel)

If the "/home" file system is mounted without the "nodev" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent device files from being interpreted on file systems that contain user home directories.

Modify "/etc/fstab" to use the "nodev" option on the "/home" directory.
```

## V-281089 RHEL 10 must prevent files with the "setuid" and "setgid" bit set from being executed on file systems that contain user home directories. {#V-281089}

Severity: medium · Rule: SV-281089r1165622_rule · STIG ID: RHEL-10-400360 · CCI-001764

**Discussion.** The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/home" is mounted with the "nosuid" option with the following command:

Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is automatically a finding, as the "nosuid" option cannot be used on the "/" system.

$ mount | grep /home
/dev/mapper/luks-ca2261ed-7b00-4b7b-84cd-8cd6d8fa4b28 on /home type xfs (rw,nodev,nosuid,noexec,seclabel)

If the "/home" file system is mounted without the "nosuid" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent files with the "setuid" and "setgid" bit set from being executed on file systems that contain user home directories.

Modify "/etc/fstab" to use the "nosuid" option on the "/home" directory.
```

## V-281090 RHEL 10 must prevent code from being executed on file systems that contain user home directories. {#V-281090}

Severity: medium · Rule: SV-281090r1268226_rule · STIG ID: RHEL-10-400365 · CCI-000213

**Discussion.** The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/home" is mounted with the "noexec" option with the following command:

Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is automatically a finding, as the "noexec" option cannot be used on the "/" system.

$ mount | grep /home
/dev/mapper/luks-ca2261ed-7b00-4b7b-84cd-8cd6d8fa4b28 on /home type xfs (rw,nodev,nosuid,noexec,seclabel)

If the "/home" file system is mounted without the "noexec" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent code from being executed on file systems that contain user home directories.

Modify "/etc/fstab" to use the "noexec" option on the "/home" directory.
```

## V-281091 RHEL 10 must mount "/var/log/audit" with the "nodev" option. {#V-281091}

Severity: medium · Rule: SV-281091r1165628_rule · STIG ID: RHEL-10-400400 · CCI-001764

**Discussion.** The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.

**Check.**

```
Verify RHEL 10 is configured so that "/var/log/audit" is mounted with the "nodev" option:

$ mount | grep /var/log/audit
/dev/mapper/luks-4e45e1ad-5337-42c4-a19f-ee12ccc1d502 on /var/log/audit type xfs (rw,nodev,nosuid,noexec,seclabel)

If the "/var/log/audit" file system is mounted without the "nodev" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/var/log/audit" with the "nodev" option.

Modify "/etc/fstab" to use the "nodev" option on the "/var/log/audit" directory.
```

## V-281092 RHEL 10 must mount "/var/log/audit" with the "noexec" option. {#V-281092}

Severity: medium · Rule: SV-281092r1165631_rule · STIG ID: RHEL-10-400405 · CCI-001764

**Discussion.** The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/var/log/audit" is mounted with the "noexec" option:

$ mount | grep /var/log/audit
/dev/mapper/luks-4e45e1ad-5337-42c4-a19f-ee12ccc1d502 on /var/log/audit type xfs (rw,nodev,nosuid,noexec,seclabel)

If the "/var/log/audit" file system is mounted without the "noexec" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/var/log/audit" with the "noexec" option.

Modify "/etc/fstab" to use the "noexec" option on the "/var/log/audit" directory.
```

## V-281093 RHEL 10 must mount "/var/log/audit" with the "nosuid" option. {#V-281093}

Severity: medium · Rule: SV-281093r1165634_rule · STIG ID: RHEL-10-400410 · CCI-001764

**Discussion.** The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/var/log/audit" is mounted with the "nosuid" option:

$ mount | grep /var/log/audit
/dev/mapper/luks-4e45e1ad-5337-42c4-a19f-ee12ccc1d502 on /var/log/audit type xfs (rw,nodev,nosuid,noexec,seclabel)

If the "/var/log/audit" file system is mounted without the "nosuid" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/var/log/audit" with the "nosuid" option.

Modify "/etc/fstab" to use the "nosuid" option on the "/var/log/audit" directory.
```

## V-281094 RHEL 10 must enforce a mode of "0755" or less permissive for audit tools. {#V-281094}

Severity: medium · Rule: SV-281094r1165637_rule · STIG ID: RHEL-10-400450 · CCI-001493 CCI-001494 CCI-001495

**Discussion.** Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information.

RHEL 10 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools.

Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.

Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099

**Check.**

```
Verify RHEL 10 is configured so that the audit tools have a mode of "0755" or less with the following command:

$ stat -c "%a %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/auditd /sbin/rsyslogd /sbin/augenrules
755 /sbin/auditctl
755 /sbin/aureport
755 /sbin/ausearch
755 /sbin/auditd
755 /sbin/rsyslogd
755 /sbin/augenrules

If any of the audit tool files have a mode more permissive than "0755", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the audit tools to have a mode of "0755" by running the following command:

$ sudo chmod 0755 [audit_tool]

Replace "[audit_tool]" with each audit tool that has a mode more permissive than "0755".
```

## V-281095 RHEL 10 must prohibit local initialization files from executing world-writable programs. {#V-281095}

Severity: medium · Rule: SV-281095r1184678_rule · STIG ID: RHEL-10-400500 · CCI-000381

**Discussion.** If user startup files execute world-writable programs, especially in unprotected directories, they could be maliciously modified to destroy user files or otherwise compromise the system at the user level. If the system is compromised at the user level, it is easier to elevate privileges to eventually compromise the system at the root and network level.

**Check.**

```
Verify RHEL 10 local initialization files do not execute world-writable programs with the following command:

Note: The example will be for a system that is configured to create user home directories in the "/home" directory.

$ sudo find /home -perm -002 -type f -name ".[^.]*" -exec ls -ld {} \;

If any local initialization files are found to reference world-writable files, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that local initialization files do not execute world-writable programs with the following command:

$ sudo chmod 0755 <file>
```

## V-281096 RHEL 10 must enable the systemd-journald service. {#V-281096}

Severity: medium · Rule: SV-281096r1165643_rule · STIG ID: RHEL-10-500000 · CCI-001665

**Discussion.** In the event of a system failure, RHEL 10 must preserve any information necessary to determine cause of failure and return to operations with least disruption to system processes.

**Check.**

```
Verify RHEL 10 enables the systemd-journald service with the following command:

$ systemctl is-active systemd-journald
active

If the systemd-journald service is not active, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable the systemd-journald service.

To enable the systemd-journald service, run the following command:

$ sudo systemctl enable --now systemd-journald
```

## V-281097 RHEL 10 must enable auditing of processes that start prior to the audit daemon. {#V-281097}

Severity: medium · Rule: SV-281097r1268226_rule · STIG ID: RHEL-10-500005 · CCI-000213

**Discussion.** Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information available only if auditing is enabled before a given process is created.

**Check.**

```
Verify RHEL 10 is configured so that GRUB 2 enables auditing of processes that start prior to the audit daemon with the following commands:

Check that the current GRUB 2 configuration enables auditing:

$ sudo grubby --info=ALL | grep args | grep -v 'audit=1'

If any output is returned, this is a finding.

Check that auditing is enabled by default to persist in kernel updates:

$ sudo grep audit /etc/default/grub
GRUB_CMDLINE_LINUX="audit=1"

If "audit" is not set to "1", is missing, or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable auditing of processes that start prior to the audit daemon with the following command:

$ sudo grubby --update-kernel=ALL --args="audit=1"

Add or modify the following line in "/etc/default/grub" to ensure the configuration survives kernel updates:

GRUB_CMDLINE_LINUX="audit=1"
```

## V-281098 RHEL 10 must audit local events. {#V-281098}

Severity: medium · Rule: SV-281098r1268225_rule · STIG ID: RHEL-10-500010 · CCI-000169

**Discussion.** Without establishing what type of events occurred, along with the source, location, and outcome, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack.

If option "local_events" is not set to "yes", only events from the network will be aggregated.

**Check.**

```
Verify that RHEL 10 generates audit records for local events with the following command:

$ sudo grep local_events /etc/audit/auditd.conf
local_events = yes

If "local_events" is not set to "yes", the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records for local events by adding or updating the following line in "/etc/audit/auditd.conf":

local_events = yes

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281099 RHEL 10 must write audit records to disk. {#V-281099}

Severity: medium · Rule: SV-281099r1165652_rule · STIG ID: RHEL-10-500015 · CCI-000163

**Discussion.** Audit data must be synchronously written to disk to ensure log integrity. This setting ensures that all audit event data is written to disk.

**Check.**

```
Verify the RHEL 10 audit system is configured to write logs to the disk with the following command:

$ sudo grep write_logs /etc/audit/auditd.conf
write_logs = yes

If "write_logs" does not have a value of "yes", the line is commented out, or the line is missing, this is a finding.
```

**Fix.**

```
Configure the RHEL 10 audit system to write log files to the disk.

Edit the "/etc/audit/auditd.conf" file and add or update the "write_logs" option to "yes":

write_logs = yes

Restart the audit daemon with the following command for changes to take effect:

$ sudo service auditd restart
```

## V-281100 RHEL 10 must log username information when unsuccessful login attempts occur. {#V-281100}

Severity: medium · Rule: SV-281100r1165655_rule · STIG ID: RHEL-10-500020 · CCI-000044

**Discussion.** Without auditing of these events, it may be harder or impossible to identify what an attacker did after an attack.

**Check.**

```
Verify RHEL 10 "/etc/security/faillock.conf" is configured to log username information when unsuccessful login attempts occur with the following command:

$ sudo grep audit /etc/security/faillock.conf
audit

If the "audit" option is not set, is missing, or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to log username information when unsuccessful login attempts occur.

Enable the feature using the following command:

$ sudo authselect enable-feature with-faillock

Add/modify the "/etc/security/faillock.conf" file to match the following line:

audit
```

## V-281101 RHEL 10 must allow only the information system security manager (ISSM) (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited. {#V-281101}

Severity: medium · Rule: SV-281101r1195411_rule · STIG ID: RHEL-10-500025 · CCI-000171

**Discussion.** Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

**Check.**

```
Verify RHEL 10 sets the files in directory "/etc/audit/rules.d/" and "/etc/audit/auditd.conf" file to have a mode of "0640" or less permissive with the following command:

$ sudo find /etc/audit/rules.d/ /etc/audit/audit.rules /etc/audit/auditd.conf -type f -exec stat -c "%a %n" {} \;
600 /etc/audit/rules.d/audit.rules
640 /etc/audit/audit.rules
640 /etc/audit/auditd.conf

If the audit configuration files have a mode more permissive than those shown, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the files in directory "/etc/audit/rules.d/" and the "/etc/audit/auditd.conf" file have a mode of "0640" with the following commands:

$ sudo chmod 0600 /etc/audit/rules.d/audit.rules
$ sudo chmod 0640 /etc/audit/rules.d/[customrulesfile].rules
$ sudo chmod 0640 /etc/audit/auditd.conf
```

## V-281102 RHEL 10 must allocate an "audit_backlog_limit" of sufficient size to capture processes that start prior to the audit daemon. {#V-281102}

Severity: medium · Rule: SV-281102r1195414_rule · STIG ID: RHEL-10-500030 · CCI-000130 CCI-000135 CCI-000169 CCI-001464 CCI-001849 CCI-002884 CCI-000172

**Discussion.** Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

Allocating an "audit_backlog_limit" of sufficient size is critical in maintaining a stable boot process. With an insufficient limit allocated, the system is susceptible to boot failures and crashes.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000254-GPOS-00095, SRG-OS-000341-GPOS-00132, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 allocates a sufficient "audit_backlog_limit" to capture processes that start prior to the audit daemon with the following command:

$ grep -oP 'audit_backlog_limit=\K[0-9]+' /proc/cmdline
8192

If the command returns any outputs, and "audit_backlog_limit" is less than "8192", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to allocate sufficient "audit_backlog_limit" to capture processes that start prior to the audit daemon with the following command:

$ sudo grubby --update-kernel=ALL --args=audit_backlog_limit=8192

The setting will be applied on reboot.
```

## V-281103 RHEL 10 must take appropriate action when a critical audit processing failure occurs. {#V-281103}

Severity: medium · Rule: SV-281103r1166261_rule · STIG ID: RHEL-10-500035 · CCI-000139

**Discussion.** It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected.

Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.

**Check.**

```
Verify the RHEL 10 audit service is configured to panic on a critical error with the following command:

$ sudo grep "\-f" /etc/audit/audit.rules
-f 2

If the value for "-f" is not "2", and availability is not documented as an overriding concern, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to shut down when auditing failures occur.

Add the following line to the bottom of the "/etc/audit/rules.d/audit.rules" file:

-f 2
```

## V-281104 RHEL 10 must take action when allocated audit record storage volume reaches 75 percent of the audit record storage capacity. {#V-281104}

Severity: medium · Rule: SV-281104r1273579_rule · STIG ID: RHEL-10-500040 · CCI-001855

**Discussion.** If action is not taken when storage volume reaches 75 percent utilization, the auditing system may fail when the storage volume reaches capacity.

**Check.**

```
Verify RHEL 10 takes action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following command:

$ sudo grep -w space_left /etc/audit/auditd.conf
space_left = 25%

If the value of the "space_left" keyword is not set to 25 percent of the storage volume allocated to audit logs, or if the line is commented out, ask the system administrator to indicate how the system is taking action if the allocated storage is about to reach capacity. 

If the "space_left" value is not configured to the correct value, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to initiate an action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity by adding/modifying the following line in the /etc/audit/auditd.conf file:

space_left  = 25%

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281105 RHEL 10 must label all off-loaded audit logs before sending them to the central log server. {#V-281105}

Severity: medium · Rule: SV-281105r1166267_rule · STIG ID: RHEL-10-500045 · CCI-000132 CCI-001851

**Discussion.** Enriched logging is needed to determine who, what, and when events occur on a system. Without this, determining root cause of an event will be much more difficult.

When audit logs are not labeled before they are sent to a central log server, the audit data will not be able to be analyzed and tied back to the correct system.

Satisfies: SRG-OS-000039-GPOS-00017, SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224

**Check.**

```
Verify the RHEL 10 audit daemon is configured to label all off-loaded audit logs with the following command:

$ sudo grep name_format /etc/audit/auditd.conf
name_format = hostname

If the "name_format" option is not "hostname", "fqd", or "numeric", or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that all off-loaded audit logs are labeled before sending them to the central log server.

Edit the "/etc/audit/auditd.conf" file and add or update the "name_format" option:

name_format = hostname

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281106 RHEL 10 must allocate audit record storage capacity to store at least one week's worth of audit records. {#V-281106}

Severity: low · Rule: SV-281106r1166270_rule · STIG ID: RHEL-10-500100 · CCI-001849 CCI-001851

**Discussion.** To ensure RHEL 10 systems have a sufficient storage capacity in which to write the audit logs, RHEL 10 must be able to allocate audit record storage capacity.

The task of allocating audit record storage capacity is usually performed during initial installation of RHEL 10.

Satisfies: SRG-OS-000341-GPOS-00132, SRG-OS-000342-GPOS-00133

**Check.**

```
Verify RHEL 10 allocates audit record storage capacity to store at least one week of audit records when audit records are not immediately sent to a central audit record storage facility.

Note: The partition size needed to capture a week of audit records is based on the activity level of the system and the total storage capacity available. Typically 10GB of storage space for audit records should be sufficient.

Determine which partition the audit records are being written to with the following command:

$ sudo grep -w log_file /etc/audit/auditd.conf
log_file = /var/log/audit/audit.log

Check the size of the partition that audit records are written to with the following command and verify whether it is sufficiently large:

$ df -h /var/log/audit/
Filesystem                                             Size  Used Avail Use% Mounted on
/dev/mapper/luks-4e45e1ad-5337-42c4-a19f-ee12ccc1d502   10G  263M  9.7G   3% /var/log/audit

If the audit record partition is not allocated for sufficient storage capacity, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to allocate enough storage capacity for at least one week of audit records when audit records are not immediately sent to a central audit record storage facility.

If audit records are stored on a partition made specifically for audit records, resize the partition with sufficient space to contain one week of audit records.

If audit records are not stored on a partition made specifically for audit records, a new partition with sufficient space must be created.
```

## V-281107 RHEL 10 must take action when allocated audit record storage volume reaches 95 percent of the audit record storage capacity. {#V-281107}

Severity: medium · Rule: SV-281107r1273580_rule · STIG ID: RHEL-10-500105 · CCI-001855

**Discussion.** If action is not taken when storage volume reaches 95 percent utilization, the auditing system may fail when the storage volume reaches capacity.

**Check.**

```
Verify RHEL 10 takes action when allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity with the following command:

$ sudo grep -w admin_space_left /etc/audit/auditd.conf
admin_space_left = 5%

If the value of the "admin_space_left" keyword is not set to 5 percent of the storage volume allocated to audit logs, or if the line is commented out, ask the system administrator to indicate how the system is taking action if the allocated storage is about to reach capacity. 

If the "admin_space_left" value is not configured to the correct value, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to initiate an action when allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity by adding/modifying the following line in the /etc/audit/auditd.conf file:

admin_space_left = 5%

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281108 RHEL 10 must take action when allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity. {#V-281108}

Severity: medium · Rule: SV-281108r1166276_rule · STIG ID: RHEL-10-500110 · CCI-001855

**Discussion.** If action is not taken when storage volume reaches 95 percent utilization, the auditing system may fail when the storage volume reaches capacity.

**Check.**

```
Verify RHEL 10 is configured to take action if allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity with the following command:

$ sudo grep admin_space_left_action /etc/audit/auditd.conf
admin_space_left_action = single

If the value of the "admin_space_left_action" is not set to "single", or if the line is commented out, ask the system administrator (SA) to indicate how the system is providing real-time alerts to the SA and information system security officer (ISSO).

If there is no evidence that real-time alerts are configured on the system, this is a finding.
```

**Fix.**

```
Configure RHEL 10 auditd service to take action if allocated audit record storage volume reaching 95 percent of the repository maximum audit record storage capacity.

Edit the following line in "/etc/audit/auditd.conf" to ensure the system is forced into single user mode if the audit record storage volume is about to reach maximum capacity:

admin_space_left_action = single

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281109 RHEL 10 must take appropriate action when the internal event queue is full. {#V-281109}

Severity: medium · Rule: SV-281109r1184691_rule · STIG ID: RHEL-10-500115 · CCI-001851

**Discussion.** The audit system must have an action set up in case the internal event queue becomes full so that no data is lost. Information stored in one location is vulnerable to accidental or incidental deletion or alteration.

Off-loading is a common process in information systems with limited audit storage capacity.

Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224

**Check.**

```
Verify the RHEL 10 audit system is configured to take an appropriate action when the internal event queue is full:

$ sudo grep overflow_action /etc/audit/auditd.conf
overflow_action = syslog

If the value of the "overflow_action" option is not set to "syslog", "single", or "halt", or the line is commented out, ask the system administrator to indicate how the audit logs are off-loaded to a different system or media.

If there is no evidence that the audit system is configured to off-load the audit logs to another system or media, and if the overflow action is not set to take appropriate action if the internal event queue becomes full, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to take appropriate action when the internal event queue is full.

Edit the "/etc/audit/auditd.conf" file and add or update the "overflow_action" option:

overflow_action = syslog

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281110 RHEL 10 must produce audit records containing information to establish the identity of any individual or process associated with the event. {#V-281110}

Severity: medium · Rule: SV-281110r1166282_rule · STIG ID: RHEL-10-500120 · CCI-001487

**Discussion.** Without establishing what type of events occurred, along with the source, location, and outcome, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack.

Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked.

Enriched logging aids in making sense of who, what, and when events occur on a system. Without this, determining root cause of an event will be much more difficult.

**Check.**

```
Verify the RHEL 10 audit system is configured to resolve audit information before writing to disk with the following command:

$ sudo grep log_format /etc/audit/auditd.conf
log_format = ENRICHED

If the "log_format" option is not "ENRICHED", or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 audit system to resolve audit information before writing to disk.

Edit the "/etc/audit/auditd.conf" file and add or update the "log_format" option:

log_format = ENRICHED

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281111 RHEL 10 must periodically flush audit records to disk to ensure that audit records are not lost. {#V-281111}

Severity: medium · Rule: SV-281111r1166285_rule · STIG ID: RHEL-10-500125 · CCI-000154

**Discussion.** If option "freq" is not set to a value that requires audit records to be written to disk after a threshold number is reached, audit records may be lost.

**Check.**

```
Verify RHEL 10 is configured to flush audit records to disk after every 100 records with the following command:

$ sudo grep freq /etc/audit/auditd.conf
freq = 100

If "freq" is not set to a value of "100" or greater, the value is missing, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to flush audit records to disk by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

freq = 100

Restart the audit daemon with the following command for changes to take effect:

$ sudo service auditd restart
```

## V-281113 RHEL 10 must notify the system administrator (SA) and information system security officer (ISSO) (at a minimum) when allocated audit record storage volume 75 percent utilization. {#V-281113}

Severity: medium · Rule: SV-281113r1184746_rule · STIG ID: RHEL-10-500205 · CCI-001855

**Discussion.** If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.

**Check.**

```
Verify RHEL 10 notifies the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following command:

$ sudo grep -w space_left_action /etc/audit/auditd.conf
space_left_action = email

If the value of the "space_left_action" is not set to "email", or if the line is commented out, ask the SA to indicate how the system is providing real-time alerts to the SA and ISSO.

If there is no evidence that real-time alerts are configured on the system, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to initiate an action to notify the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity by adding/modifying the following line in the "/etc/audit/auditd.conf" file.

space_left_action = email

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281114 RHEL 10 must notify the system administrator (SA) and/or information system security officer (ISSO) (at a minimum) of an audit processing failure. {#V-281114}

Severity: medium · Rule: SV-281114r1166294_rule · STIG ID: RHEL-10-500210 · CCI-000139 CCI-001855

**Discussion.** It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected.

Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.

This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.

Satisfies: SRG-OS-000046-GPOS-00022, SRG-OS-000343-GPOS-00134

**Check.**

```
Verify RHEL 10 is configured to notify the SA and/or ISSO (at a minimum) of an audit processing failure with the following command:

$ sudo grep action_mail_acct /etc/audit/auditd.conf
action_mail_acct = root

If the value of the "action_mail_acct" keyword is not set to "root" and/or other accounts for security personnel, the "action_mail_acct" keyword is missing, or the retuned line is commented out, ask the SA to indicate how they and the ISSO are notified of an audit process failure. 

If there is no evidence of the proper personnel being notified of an audit processing failure, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to notify the SA and/or ISSO (at a minimum) of an audit processing failure.

Edit the following line in "/etc/audit/auditd.conf" to ensure administrators are notified via email for those situations:

action_mail_acct = root

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281115 RHEL 10 must log Secure Shell (SSH) connection attempts and failures to the server. {#V-281115}

Severity: medium · Rule: SV-281115r1268219_rule · STIG ID: RHEL-10-500215 · CCI-000067

**Discussion.** SSH provides several logging levels with varying amounts of verbosity. "DEBUG" is specifically not recommended other than strictly for debugging SSH communications because it provides so much data that it is difficult to identify important security information. "INFO" or "VERBOSE" level is the basic level that only records login activity of SSH users. In many situations, such as incident response, it is important to determine when a particular user was active on a system. The logout record can eliminate users who disconnected, which helps narrow the field.

**Check.**

```
Verify RHEL 10 logs SSH connection attempts and failures to the server with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*loglevel'
/etc/ssh/sshd_config.d/90-sshd.conf:LogLevel VERBOSE

If a value of "VERBOSE" is not returned, or the line is commented out or missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to log connection attempts by adding or modifying the following line in "/etc/ssh/sshd_config" or in a file in "/etc/ssh/sshd_config.d":

LogLevel VERBOSE

Restart the SSH daemon with the following command for the settings to take effect:

$ sudo systemctl restart sshd.service
```

## V-281116 RHEL 10 must generate audit records for successful and unsuccessful uses of the "execve" system call. {#V-281116}

Severity: medium · Rule: SV-281116r1166300_rule · STIG ID: RHEL-10-500300 · CCI-002233 CCI-002234 CCI-004188

**Discussion.** Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. 

Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.

Satisfies: SRG-OS-000326-GPOS-00126, SRG-OS-000327-GPOS-00127, SRG-OS-000755-GPOS-00220

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "execve" system call with the following command:

$ sudo auditctl -l | grep execve
-a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -F key=execpriv
-a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -F key=execpriv
-a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -F key=execpriv
-a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -F key=execpriv

If the command does not return all lines, or the lines are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "execve" system call.

Add or update the following file system rules to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -k execpriv
-a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k execpriv
-a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -k execpriv
-a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k execpriv

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281117 RHEL 10 must generate audit records for successful and unsuccessful uses of the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls. {#V-281117}

Severity: medium · Rule: SV-281117r1184680_rule · STIG ID: RHEL-10-500310 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining syscalls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000458-GPOS-00203, SRG-OS-000462-GPOS-00206, SRG-OS-000463-GPOS-00207, SRG-OS-000471-GPOS-00215, SRG-OS-000474-GPOS-00219, SRG-OS-000466-GPOS-00210, SRG-OS-000468-GPOS-00212, SRG-OS-000064-GPOS-00033

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls with the following command:

$ sudo auditctl -l | grep xattr
-a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod
-a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod

-a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod
-a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod

If both the "b32" and "b64" audit rules are not defined for the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls, or if any of the lines returned are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls by adding or updating the following lines to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod
-a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod

-a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod
-a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281118 RHEL 10 must generate audit records for successful and unsuccessful uses of "umount" system calls. {#V-281118}

Severity: medium · Rule: SV-281118r1166306_rule · STIG ID: RHEL-10-500320 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "umount" command with the following command:

$ sudo auditctl -l | grep /usr/bin/umount
-a always,exit -S all -F path=/usr/bin/umount -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-mount

If the command does not return an audit rule for "umount", or any of the lines returned are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "umount" command by adding or updating the following rules in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/umount -F perm=x -F auid>=1000 -F auid!=unset -k privileged-mount

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281119 RHEL 10 must generate audit records for successful and unsuccessful uses of the "chacl" command. {#V-281119}

Severity: medium · Rule: SV-281119r1166309_rule · STIG ID: RHEL-10-500330 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "chacl" command with the following command:

$ sudo auditctl -l | grep chacl
-a always,exit -S all -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_mod

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "chacl" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=unset -k perm_mod

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281120 RHEL 10 must generate audit records for successful and unsuccessful uses of the "setfacl" command. {#V-281120}

Severity: medium · Rule: SV-281120r1166312_rule · STIG ID: RHEL-10-500340 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "setfacl" command with the following command:

$ sudo auditctl -l | grep setfacl
-a always,exit -S all -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_mod

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "setfacl" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=unset -k perm_mod

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281121 RHEL 10 must generate audit records for successful and unsuccessful uses of the "chcon" command. {#V-281121}

Severity: medium · Rule: SV-281121r1166315_rule · STIG ID: RHEL-10-500350 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "chcon" command with the following command:

$ sudo auditctl -l | grep chcon
-a always,exit -S all -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_mod

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "chcon" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=unset -k perm_mod

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281122 RHEL 10 must generate audit records for successful and unsuccessful uses of the "semanage" command. {#V-281122}

Severity: medium · Rule: SV-281122r1166318_rule · STIG ID: RHEL-10-500360 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "semanage" command with the following command:

$ sudo auditctl -l | grep semanage
-a always,exit -S all -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix-update

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "semanage" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281123 RHEL 10 must generate audit records for successful and unsuccessful uses of the "setfiles" command. {#V-281123}

Severity: medium · Rule: SV-281123r1166321_rule · STIG ID: RHEL-10-500370 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "setfiles" command with the following command:

$ sudo auditctl -l | grep setfiles
-a always,exit -S all -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix-update

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "setfiles" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281124 RHEL 10 must generate audit records for successful and unsuccessful uses of the "setsebool" command. {#V-281124}

Severity: medium · Rule: SV-281124r1166324_rule · STIG ID: RHEL-10-500380 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "setsebool" command with the following command:

$ sudo auditctl -l | grep setsebool
-a always,exit -S all -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful use of the "setsebool " command by adding or updating the following rules in the "/etc/audit/rules.d/audit.rules" file:

-a always,exit -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281125 RHEL 10 must generate audit records for successful and unsuccessful uses of the "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" system calls. {#V-281125}

Severity: medium · Rule: SV-281125r1197225_rule · STIG ID: RHEL-10-500390 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining syscalls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000458-GPOS-00203, SRG-OS-000461-GPOS-00205

**Check.**

```
Verify RHEL 10 is configured to audit successful/unsuccessful attempts to use the "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" system calls with the following command:

$ sudo auditctl -l | grep 'open\|truncate\|creat'
-a always,exit -F arch=b32 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access
-a always,exit -F arch=b64 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access

-a always,exit -F arch=b32 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access
-a always,exit -F arch=b64 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access

If the output does not produce rules containing "-F exit=-EPERM", this is a finding.

If the output does not produce rules containing "-F exit=-EACCES", this is a finding.

If the command does not return an audit rule for "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at", or any of the lines returned are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful use of the "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" system calls by adding or updating the following rules in the "/etc/audit/rules.d/audit.rules" file:

-a always,exit -F arch=b32 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access
-a always,exit -F arch=b64 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access

-a always,exit -F arch=b32 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access
-a always,exit -F arch=b64 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281126 RHEL 10 must generate audit records for successful and unsuccessful uses of the "delete_module" system call. {#V-281126}

Severity: medium · Rule: SV-281126r1166330_rule · STIG ID: RHEL-10-500400 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "delete_module" system call with the following command:

$ sudo auditctl -l | grep delete_module
-a always,exit -F arch=b32 -S delete_module -F auid>=1000 -F auid!=-1 -F key=module_chng
-a always,exit -F arch=b64 -S delete_module -F auid>=1000 -F auid!=-1 -F key=module_chng

If both the "b32" and "b64" audit rules are not defined for the "delete_module" system call, or any of the lines returned are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful use of the "delete_module" system call by adding or updating the following rules in the "/etc/audit/rules.d/audit.rules" file:

-a always,exit -F arch=b32 -S delete_module -F auid>=1000 -F auid!=unset -k module_chng
-a always,exit -F arch=b64 -S delete_module -F auid>=1000 -F auid!=unset -k module_chng

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281127 RHEL 10 must generate audit records for successful and unsuccessful uses of the "init_module" and "finit_module" system calls. {#V-281127}

Severity: medium · Rule: SV-281127r1208796_rule · STIG ID: RHEL-10-500410 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining syscalls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "init_module" and "finit_module" syscalls with the following command:

$ sudo auditctl -l | grep init_module
-a always,exit -F arch=b32 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng
-a always,exit -F arch=b64 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng

If both the "b32" and "b64" audit rules are not defined for the "init_module" and "finit_module" system calls, or any of the lines returned are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful use of the "init_module" and "finit_module" system calls by adding or updating the following rules in the "/etc/audit/rules.d/audit.rules" file:

-a always,exit -F arch=b32 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng
-a always,exit -F arch=b64 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281128 RHEL 10 must generate audit records for successful and unsuccessful uses of the "chage" command. {#V-281128}

Severity: medium · Rule: SV-281128r1166336_rule · STIG ID: RHEL-10-500420 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "chage" command with the following command:

$ sudo auditctl -l | grep chage
-a always,exit -S all -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-chage

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "chage" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=unset -k privileged-chage

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281129 RHEL 10 must generate audit records for successful and unsuccessful uses of the "chsh" command. {#V-281129}

Severity: medium · Rule: SV-281129r1166339_rule · STIG ID: RHEL-10-500430 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "chsh" command with the following command:

$ sudo auditctl -l | grep chsh
-a always,exit -S all -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "chsh" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281130 RHEL 10 must generate audit records for successful and unsuccessful uses of the "crontab" command. {#V-281130}

Severity: medium · Rule: SV-281130r1166342_rule · STIG ID: RHEL-10-500440 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "crontab" command with the following command:

$ sudo auditctl -l | grep crontab
-a always,exit -S all -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-crontab

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "crontab" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=unset -k privileged-crontab

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281131 RHEL 10 must generate audit records for successful and unsuccessful uses of the "gpasswd" command. {#V-281131}

Severity: medium · Rule: SV-281131r1273581_rule · STIG ID: RHEL-10-500450 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 generates audit records for the execution of the "gpasswd" command with the following command:

$ sudo auditctl -l | grep '/usr/bin/gpasswd'

-a always,exit -F arch=b32 -F path=/usr/bin/gpasswd -F perm=x -F key=privileged-gpasswd
-a always,exit -F arch=b64 -F path=/usr/bin/gpasswd -F perm=x -F key=privileged-gpasswd

If the command does not return these lines, or the lines are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "gpasswd" command by adding or updating the following rules in "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -F path=/usr/bin/gpasswd -F perm=x -k privileged-gpasswd
-a always,exit -F arch=b64 -F path=/usr/bin/gpasswd -F perm=x -k privileged-gpasswd

To load the rules to the kernel immediately, use the following command:

$ sudo augenrules --load
```

## V-281132 RHEL 10 must generate audit records for successful and unsuccessful uses of the "kmod" command. {#V-281132}

Severity: medium · Rule: SV-281132r1166348_rule · STIG ID: RHEL-10-500460 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "kmod" command with the following command:

$ sudo auditctl -l | grep kmod
-a always,exit -S all -F path=/usr/bin/kmod -F perm=x -F auid>=1000 -F auid!=-1 -F key=modules

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "kmod" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/kmod -F perm=x -F auid>=1000 -F auid!=unset -k modules

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281133 RHEL 10 must generate audit records for successful and unsuccessful uses of the "newgrp" command. {#V-281133}

Severity: medium · Rule: SV-281133r1166351_rule · STIG ID: RHEL-10-500470 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "newgrp" command with the following command:

$ sudo auditctl -l | grep newgrp
-a always,exit -S all -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "newgrp" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281134 RHEL 10 must generate audit records for successful and unsuccessful uses of the "pam_timestamp_check" command. {#V-281134}

Severity: medium · Rule: SV-281134r1166354_rule · STIG ID: RHEL-10-500480 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "pam_timestamp_check" command with the following command:

$ sudo auditctl -l | grep timestamp
-a always,exit -S all -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-pam_timestamp_check

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "pam_timestamp_check" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=unset -k privileged-pam_timestamp_check

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281135 RHEL 10 must generate audit records for successful and unsuccessful uses of the "passwd" command. {#V-281135}

Severity: medium · Rule: SV-281135r1273582_rule · STIG ID: RHEL-10-500490 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 generates audit records for successful and unsuccessful uses of the "passwd" command with the following command:

$ sudo auditctl -l | grep '/usr/bin/passwd'

-a always,exit -F arch=b32 -F path=/usr/bin/passwd -F perm=x -F key=privileged-passwd
-a always,exit -F arch=b64 -F path=/usr/bin/passwd -F perm=x -F key=privileged-passwd

If the command does not return these lines, or the lines are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "passwd" command by adding or updating the following rules in "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -F path=/usr/bin/passwd -F perm=x -k privileged-passwd
-a always,exit -F arch=b64 -F path=/usr/bin/passwd -F perm=x -k privileged-passwd

To load the rules to the kernel immediately, use the following command:

$ sudo augenrules --load
```

## V-281136 RHEL 10 must generate audit records for successful and unsuccessful uses of the "postdrop" command. {#V-281136}

Severity: medium · Rule: SV-281136r1166360_rule · STIG ID: RHEL-10-500500 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "postdrop" command with the following command:

$ sudo auditctl -l | grep postdrop
-a always,exit -S all -F path=/usr/sbin/postdrop -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix-update

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "postdrop" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/postdrop -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281137 RHEL 10 must generate audit records for successful and unsuccessful uses of the "postqueue" command. {#V-281137}

Severity: medium · Rule: SV-281137r1197226_rule · STIG ID: RHEL-10-500510 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "postqueue" command with the following command:

$ sudo auditctl -l | grep postqueue
-a always,exit -S all -F path=/usr/sbin/postqueue -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix-update

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "postqueue" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/postqueue -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281138 RHEL 10 must generate audit records for successful and unsuccessful uses of the ssh-agent command. {#V-281138}

Severity: medium · Rule: SV-281138r1197227_rule · STIG ID: RHEL-10-500520 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "ssh-agent" command with the following command:

$ sudo auditctl -l | grep ssh-agent
-a always,exit -S all -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-ssh

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "ssh-agent" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=unset -k privileged-ssh

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281139 RHEL 10 must generate audit records for successful and unsuccessful uses of the "ssh-keysign" command. {#V-281139}

Severity: medium · Rule: SV-281139r1197228_rule · STIG ID: RHEL-10-500530 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "ssh-keysign" command with the following command:

$ sudo auditctl -l | grep ssh-keysign
-a always,exit -S all -F path=/usr/libexec/openssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-ssh

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "ssh-keysign" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/libexec/openssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=unset -k privileged-ssh

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281140 RHEL 10 must generate audit records for successful and unsuccessful uses of the "su" command. {#V-281140}

Severity: medium · Rule: SV-281140r1197229_rule · STIG ID: RHEL-10-500540 · CCI-000130 CCI-000135 CCI-000169 CCI-000172 CCI-002884 CCI-004188

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210, SRG-OS-000755-GPOS-00220

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "su" command with the following command:

$ sudo auditctl -l | grep '/usr/bin/su\b'
-a always,exit -S all -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-priv_change

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "su" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=unset -k privileged-priv_change

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281141 RHEL 10 must generate audit records for successful and unsuccessful uses of the "sudo" command. {#V-281141}

Severity: medium · Rule: SV-281141r1197230_rule · STIG ID: RHEL-10-500550 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172 CCI-004188

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210, SRG-OS-000755-GPOS-00220

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "sudo" command with the following command:

$ sudo auditctl -l | grep '/usr/bin/sudo\b'
-a always,exit -S all -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "sudo" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281142 RHEL 10 must generate audit records for successful and unsuccessful uses of the "sudoedit" command. {#V-281142}

Severity: medium · Rule: SV-281142r1197231_rule · STIG ID: RHEL-10-500560 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172 CCI-004188

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000755-GPOS-00220

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "sudoedit" command with the following command:

$ sudo auditctl -l | grep /usr/bin/sudoedit
-a always,exit -S all -F path=/usr/bin/sudoedit -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "sudoedit" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/bin/sudoedit -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281143 RHEL 10 must generate audit records for successful and unsuccessful uses of the "unix_chkpwd" command. {#V-281143}

Severity: medium · Rule: SV-281143r1197232_rule · STIG ID: RHEL-10-500570 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "unix_chkpwd" command with the following command:

$ sudo auditctl -l | grep unix_chkpwd
-a always,exit -S all -F path=/usr/sbin/unix_chkpwd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix-update

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "unix_chkpwd" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/unix_chkpwd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281144 RHEL 10 must generate audit records for successful and unsuccessful uses of the "unix_update" command. {#V-281144}

Severity: medium · Rule: SV-281144r1166384_rule · STIG ID: RHEL-10-500580 · CCI-000130 CCI-000135 CCI-000169 CCI-000172 CCI-002884

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "unix_update" command with the following command:

$ sudo auditctl -l | grep unix_update
-a always,exit -S all -F path=/usr/sbin/unix_update -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix-update

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "unix_update" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/unix_update -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281145 RHEL 10 must generate audit records for successful and unsuccessful uses of the "userhelper" command. {#V-281145}

Severity: medium · Rule: SV-281145r1197233_rule · STIG ID: RHEL-10-500590 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "userhelper" command with the following command:

$ sudo auditctl -l | grep userhelper
-a always,exit -S all -F path=/usr/sbin/userhelper -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix-update

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "userhelper" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/userhelper -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281146 RHEL 10 must generate audit records for successful and unsuccessful uses of the "usermod" command. {#V-281146}

Severity: medium · Rule: SV-281146r1197235_rule · STIG ID: RHEL-10-500600 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "usermod" command with the following command:

$ sudo auditctl -l | grep usermod
-a always,exit -S all -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-usermod

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "usermod" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=unset -k privileged-usermod

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281147 RHEL 10 must generate audit records for successful and unsuccessful uses of the "mount" command. {#V-281147}

Severity: medium · Rule: SV-281147r1273584_rule · STIG ID: RHEL-10-500610 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining syscalls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "mount" command with the following command:

$ sudo auditctl -l | grep mount
-a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=unset -k privileged-mount
-a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=unset -k privileged-mount

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "mount" command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=unset -k privileged-mount
-a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=unset -k privileged-mount

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281148 RHEL 10 must generate audit records for successful and unsuccessful uses of the "init" command. {#V-281148}

Severity: medium · Rule: SV-281148r1166396_rule · STIG ID: RHEL-10-500620 · CCI-000172

**Discussion.** Misuse of the "init" command may cause availability issues for the system.

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "init" command with the following command:

$ sudo auditctl -l | grep /usr/sbin/init
-a always,exit -S all -F path=/usr/sbin/init -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-init

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful uses of the "init" command by adding or updating the following rule in the "/etc/audit/rules.d/audit.rules" file:

-a always,exit -F path=/usr/sbin/init -F perm=x -F auid>=1000 -F auid!=unset -k privileged-init

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281149 RHEL 10 must generate audit records for successful and unsuccessful uses of the "poweroff" command. {#V-281149}

Severity: medium · Rule: SV-281149r1166399_rule · STIG ID: RHEL-10-500630 · CCI-000172

**Discussion.** Misuse of the "poweroff" command may cause availability issues for the system.

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "poweroff" command with the following command:

$ sudo auditctl -l | grep poweroff
-a always,exit -S all -F path=/usr/sbin/poweroff -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-poweroff

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful uses of the "poweroff" command by adding or updating the following rule in the "/etc/audit/rules.d/audit.rules" file:

-a always,exit -F path=/usr/sbin/poweroff -F perm=x -F auid>=1000 -F auid!=unset -k privileged-poweroff

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281150 RHEL 10 must generate audit records for successful and unsuccessful uses of the "reboot" command. {#V-281150}

Severity: medium · Rule: SV-281150r1166402_rule · STIG ID: RHEL-10-500640 · CCI-000172

**Discussion.** Misuse of the "reboot" command may cause system availability issues.

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "reboot" command with the following command:

$ sudo auditctl -l | grep reboot
-a always,exit -S all -F path=/usr/sbin/reboot -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-reboot

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful uses of the "reboot" command by adding or updating the following rule in the "/etc/audit/rules.d/audit.rules" file:

-a always,exit -F path=/usr/sbin/reboot -F perm=x -F auid>=1000 -F auid!=unset -k privileged-reboot

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281151 RHEL 10 must generate audit records for successful and unsuccessful uses of the shutdown command. {#V-281151}

Severity: medium · Rule: SV-281151r1166405_rule · STIG ID: RHEL-10-500650 · CCI-000172

**Discussion.** Misuse of the shutdown command may cause availability issues for the system.

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "shutdown" command with the following command:

$ sudo cat /etc/audit/rules.d/* | grep shutdown
-a always,exit -S all -F path=/usr/sbin/shutdown -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-shutdown

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful uses of the "shutdown" command by adding or updating the following rule in the "/etc/audit/rules.d/audit.rules" file:

-a always,exit -F path=/usr/sbin/shutdown -F perm=x -F auid>=1000 -F auid!=unset -k privileged-shutdown

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281152 RHEL 10 must generate audit records for successful and unsuccessful uses of the "umount" system call. {#V-281152}

Severity: medium · Rule: SV-281152r1166408_rule · STIG ID: RHEL-10-500660 · CCI-000130 CCI-000169 CCI-002884 CCI-000172

**Discussion.** The changing of file permissions could indicate that a user is attempting to gain access to information that would otherwise be disallowed. Auditing discretionary access control (DAC) modifications can facilitate the identification of patterns of abuse among both authorized and unauthorized users.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 generates an audit record for all uses of the "umount" system call with the following command:

$ sudo auditctl -l | grep b32 | grep 'umount\b'
-a always,exit -F arch=b32 -S umount -F auid>=1000 -F auid!=-1 -F key=privileged-umount

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful uses of the "umount" system call by adding or updating the following rules in "/etc/audit/audit.rules" and adding the following rules to "/etc/audit/rules.d/perm_mod.rules" or updating the existing rules in files in the "/etc/audit/rules.d/" directory:

-a always,exit -F arch=b32 -S umount -F auid>=1000 -F auid!=unset -k privileged-umount

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281153 RHEL 10 must generate audit records for successful and unsuccessful uses of the "umount2" system call. {#V-281153}

Severity: medium · Rule: SV-281153r1166411_rule · STIG ID: RHEL-10-500670 · CCI-000130 CCI-000169 CCI-002884 CCI-000172

**Discussion.** The changing of file permissions could indicate that a user is attempting to gain access to information that would otherwise be disallowed. Auditing discretionary access control (DAC) modifications can facilitate the identification of patterns of abuse among both authorized and unauthorized users.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215

**Check.**

```
Verify RHEL 10 generates an audit record for all uses of the "umount2" system call with the following command:

$ sudo auditctl -l | grep umount2
-a always,exit -F arch=b64 -S umount2 -F auid>=1000 -F auid!=-1 -F key=privileged-umount
-a always,exit -F arch=b32 -S umount2 -F auid>=1000 -F auid!=-1 -F key=privileged-umount

If no line is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful uses of the "umount2" system call by adding or updating the following rules in a file in "/etc/audit/rules.d":

-a always,exit -F arch=b32 -S umount2 -F auid>=1000 -F auid!=unset -k privileged-umount
-a always,exit -F arch=b64 -S umount2 -F auid>=1000 -F auid!=unset -k privileged-umount

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281154 RHEL 10 must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers". {#V-281154}

Severity: medium · Rule: SV-281154r1273585_rule · STIG ID: RHEL-10-500680 · CCI-000018 CCI-000130 CCI-000135 CCI-000169 CCI-000015 CCI-002884 CCI-000172 CCI-001403 CCI-001404 CCI-001405 CCI-002130

**Discussion.** The actions taken by system administrators must be audited to keep a record of what was executed on the system, as well as for accountability purposes. Editing the "sudoers" file may be sign of an attacker trying to establish persistent methods to a system. Auditing the editing of the "sudoers" files mitigates this risk.

Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221

**Check.**

```
Verify RHEL 10 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers" with the following command:

$ sudo auditctl -l | grep '/etc/sudoers[^.]'
-a always,exit -F arch=b32 -F path=/etc/sudoers -F perm=wa -F key=identity
-a always,exit -F arch=b32 -F path=/etc/sudoers -F perm=wa -F key=identity

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers".

Add or update the following file system rule to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -F path=/etc/sudoers -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/sudoers -F perm=wa -F key=identity

Restart the audit daemon with the following command for the changes to take effect:

$ sudo augenrules --load
```

## V-281155 RHEL 10 must generate audit records for all account creations, modifications, disabling, and termination events that affect the "/etc/sudoers.d/" directory. {#V-281155}

Severity: medium · Rule: SV-281155r1273586_rule · STIG ID: RHEL-10-500690 · CCI-000018 CCI-000130 CCI-000135 CCI-000169 CCI-000015 CCI-002884 CCI-000172 CCI-001403 CCI-001404 CCI-001405 CCI-002130

**Discussion.** The actions taken by system administrators must be audited to keep a record of what was executed on the system, as well as for accountability purposes. Editing the "sudoers" file may be a sign of an attacker trying to establish persistent methods to a system. Auditing the editing of the "sudoers" files mitigates this risk.

Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221

**Check.**

```
Verify RHEL 10 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers.d/" with the following command:

$ sudo auditctl -l | grep /etc/sudoers.d
-a always,exit -F arch=b32 -F path=/etc/sudoers.d -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/sudoers.d -F perm=wa -F key=identity

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers.d/".

Add or update the following file system rule to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -F path=/etc/sudoers.d -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/sudoers.d -F perm=wa -F key=identity

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281156 RHEL 10 must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/group". {#V-281156}

Severity: medium · Rule: SV-281156r1166420_rule · STIG ID: RHEL-10-500700 · CCI-000018 CCI-000130 CCI-000135 CCI-000169 CCI-000015 CCI-002884 CCI-000172 CCI-001403 CCI-001404 CCI-001405 CCI-002130

**Discussion.** In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications must be investigated for legitimacy.

Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221

**Check.**

```
Verify RHEL 10 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/group" with the following command:

$ sudo auditctl -l | egrep '(/etc/group)'
-a always,exit -F arch=b32 -F path=/etc/group -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/group -F perm=wa -F key=identity

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/group".

Add or update the following file system rule to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -F path=/etc/group -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/group -F perm=wa -F key=identity

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281157 RHEL 10 must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/gshadow". {#V-281157}

Severity: medium · Rule: SV-281157r1166423_rule · STIG ID: RHEL-10-500710 · CCI-000018 CCI-000130 CCI-000135 CCI-000169 CCI-000015 CCI-002884 CCI-000172 CCI-001403 CCI-001404 CCI-001405 CCI-002130

**Discussion.** In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications should be investigated for legitimacy.

Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221

**Check.**

```
Verify RHEL 10 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/gshadow" with the following command:

$ sudo auditctl -l | egrep '(/etc/gshadow)'
-a always,exit -F arch=b32 -F path=/etc/gshadow -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/gshadow -F perm=wa -F key=identity

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/gshadow".

Add or update the following file system rule to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -F path=/etc/gshadow -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/gshadow -F perm=wa -F key=identity

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281158 RHEL 10 must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/security/opasswd". {#V-281158}

Severity: medium · Rule: SV-281158r1273587_rule · STIG ID: RHEL-10-500720 · CCI-000018 CCI-000130 CCI-000135 CCI-000169 CCI-000015 CCI-002884 CCI-000172 CCI-001403 CCI-001404 CCI-001405 CCI-002130

**Discussion.** In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications should be investigated for legitimacy.

Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221

**Check.**

```
Verify RHEL 10 generates audit records for modifications to "/etc/security/opasswd" with the following command:

$ sudo auditctl -l | grep '/etc/security/opasswd'

-a always,exit -F arch=b32 -F path=/etc/security/opasswd -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/security/opasswd -F perm=wa -F key=identity

If the command does not return these lines, or the lines are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records for all modifications to "/etc/security/opasswd" by adding or updating the following rules in "/etc/audit/rules.d/identity.rules":

-a always,exit -F arch=b32 -F path=/etc/security/opasswd -F perm=wa -k identity
-a always,exit -F arch=b64 -F path=/etc/security/opasswd -F perm=wa -k identity

To load the rules to the kernel immediately, use the following command:

$ sudo augenrules --load
```

## V-281159 RHEL 10 must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd". {#V-281159}

Severity: medium · Rule: SV-281159r1166429_rule · STIG ID: RHEL-10-500730 · CCI-000018 CCI-000130 CCI-000135 CCI-000169 CCI-000015 CCI-002884 CCI-000172 CCI-001403 CCI-001404 CCI-001405 CCI-002130

**Discussion.** In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications should be investigated for legitimacy.

Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221, SRG-OS-000274-GPOS-00104, SRG-OS-000275-GPOS-00105, SRG-OS-000276-GPOS-00106, SRG-OS-000277-GPOS-00107

**Check.**

```
Verify RHEL 10 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd" with the following command:

$ sudo auditctl -l | egrep '(/etc/passwd)'
-a always,exit -F arch=b32 -F path=/etc/passwd -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/passwd -F perm=wa -F key=identity

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd".

Add or update the following file system rule to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -F path=/etc/passwd -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/passwd -F perm=wa -F key=identity

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281160 RHEL 10 must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/shadow". {#V-281160}

Severity: medium · Rule: SV-281160r1184695_rule · STIG ID: RHEL-10-500740 · CCI-000018 CCI-000130 CCI-000135 CCI-000169 CCI-000015 CCI-002884 CCI-000172 CCI-001403 CCI-001404 CCI-001405 CCI-002130

**Discussion.** In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications should be investigated for legitimacy.

Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221

**Check.**

```
Verify RHEL 10 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/shadow" with the following command:

$ sudo auditctl -l | egrep '(/etc/shadow)'
-a always,exit -F arch=b32 -F path=/etc/shadow -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/shadow -F perm=wa -F key=identity

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/shadow".

Add or update the following file system rule to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -F path=/etc/shadow -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/etc/shadow -F perm=wa -F key=identity

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281161 RHEL 10 must generate audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/faillock". {#V-281161}

Severity: medium · Rule: SV-281161r1166435_rule · STIG ID: RHEL-10-500750 · CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Satisfies: SRG-OS-000392-GPOS-00172, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218

**Check.**

```
Verify RHEL 10 generates audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/faillock" with the following command:

$ sudo auditctl -l | grep /var/log/faillock
-a always,exit -F arch=b32 -F path=/var/log/faillock -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/var/log/faillock -F perm=wa -F key=identity

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/faillock".

Add or update the following file system rule to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -F path=/var/log/faillock -F perm=wa -F key=identity
-a always,exit -F arch=b64 -F path=/var/log/faillock -F perm=wa -F key=identity

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281162 RHEL 10 must generate audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/lastlog". {#V-281162}

Severity: medium · Rule: SV-281162r1166438_rule · STIG ID: RHEL-10-500760 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218, SRG-OS-000470-GPOS-00214

**Check.**

```
Verify RHEL 10 generates audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/lastlog" with the following command:

$ sudo auditctl -l | grep /var/log/lastlog
-a always,exit -F arch=b32 -F path=/var/log/lastlog -F perm=wa -F key=logins
-a always,exit -F arch=b64 -F path=/var/log/lastlog -F perm=wa -F key=logins

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/lastlog".

Add or update the following file system rule to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -F path=/var/log/lastlog -F perm=wa -F key=logins
-a always,exit -F arch=b64 -F path=/var/log/lastlog -F perm=wa -F key=logins

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281163 RHEL 10 must generate audit records for all uses of the "chmod", "fchmod", "fchmodat", and "fchmodat2" syscalls. {#V-281163}

Severity: medium · Rule: SV-281163r1166441_rule · STIG ID: RHEL-10-500780 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining syscalls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "chmod", "fchmod", "fchmodat", and "fchmodat2" syscalls with the following command:

$ sudo auditctl -l | grep chmod
-a always,exit -F arch=b32 -S chmod,fchmod,fchmodat,fchmodat2 -F auid>=1000 -F auid!=unset -k perm_mod
-a always,exit -F arch=b64 -S chmod,fchmod,fchmodat,fchmodat2 -F auid>=1000 -F auid!=unset -k perm_mod

If both the "b32" and "b64" audit rules are not defined for the "chmod", "fchmod", "fchmodat", and "fchmodat2" syscalls, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "chmod", "fchmod", "fchmodat", and "fchmodat2" syscalls.

Add or update the following rules in "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -S chmod,fchmod,fchmodat,fchmodat2 -F auid>=1000 -F auid!=unset -k perm_mod

-a always,exit -F arch=b64 -S chmod,fchmod,fchmodat,fchmodat2 -F auid>=1000 -F auid!=unset -k perm_mod

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281164 RHEL 10 must generate audit records for all uses of the "chown", "fchown", "fchownat", and "lchown" syscalls. {#V-281164}

Severity: medium · Rule: SV-281164r1166444_rule · STIG ID: RHEL-10-500790 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining syscalls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203, SRG-OS-000474-GPOS-00219

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "chown", "fchown", "fchownat", and "lchown" syscalls with the following command:

$ sudo auditctl -l | grep chown
-a always,exit -F arch=b32 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_mod
-a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_mod

If both the "b32" and "b64" audit rules are not defined for the "chown", "fchown", "fchownat", and "lchown" syscalls, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful/unsuccessful attempts to use the "chown", "fchown", "fchownat", and "lchown"" syscalls.

Add or update the following rules in "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b32 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_mod
-a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_mod

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281165 RHEL 10 must generate audit records for all uses of the "rename", "unlink", "rmdir", "renameat", "renameat2", and "unlinkat" system calls. {#V-281165}

Severity: medium · Rule: SV-281165r1166447_rule · STIG ID: RHEL-10-500810 · CCI-000130 CCI-000135 CCI-000169 CCI-002884 CCI-000172

**Discussion.** Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining syscalls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210, SRG-OS-000467-GPOS-00211, SRG-OS-000468-GPOS-00212

**Check.**

```
Verify RHEL 10 is configured to audit successful/unsuccessful attempts to use the "rename", "unlink", "rmdir", "renameat", "renameat2", and "unlinkat" system calls with the following command:

$ sudo auditctl -l | grep 'rename\|unlink\|rmdir'
-a always,exit -F arch=b32 -S rename,unlink,rmdir,renameat,renameat2,unlinkat -F auid>=1000 -F auid!=unset -k delete
-a always,exit -F arch=b64 -S rename,unlink,rmdir,renameat,renameat2,unlinkat -F auid>=1000 -F auid!=unset -k delete

If the command does not return an audit rule for "rename", "unlink", "rmdir", "renameat", and "unlinkat", or any of the lines returned are commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate an audit event for any successful/unsuccessful use of the "rename", "unlink", "rmdir", "renameat", "renameat2", and "unlinkat" system calls by adding or updating the following rules in the "/etc/audit/rules.d/audit.rules" file:

-a always,exit -F arch=b32 -S rename,unlink,rmdir,renameat,renameat2,unlinkat -F auid>=1000 -F auid!=unset -k delete
-a always,exit -F arch=b64 -S rename,unlink,rmdir,renameat,renameat2,unlinkat -F auid>=1000 -F auid!=unset -k delete

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-281166 RHEL 10 must require authentication upon booting into single-user and maintenance modes. {#V-281166}

Severity: medium · Rule: SV-281166r1273588_rule · STIG ID: RHEL-10-600000 · CCI-000213

**Discussion.** To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoW-approved PKIs, all DoW systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. 

Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.

Password protection on the boot loader configuration ensures users with physical access cannot trivially alter important bootloader settings. These include which kernel to use and whether to enter single-user mode.

**Check.**

```
Verify that RHEL 10 requires a password for the GRUB 2 bootloader to prevent unauthorized modifications to boot parameters.

Check the unified configuration file where the GRUB 2 password is stored:

# sudo grep -iw "GRUB2_PASSWORD" /boot/grub2/user.cfg
GRUB2_PASSWORD=grub.pbkdf2.sha512.[password_hash]

If the "GRUB2_PASSWORD" entry does not exist, is commented out, or if the hash does not begin with "grub.pbkdf2.sha512", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to require a grub bootloader password for the grub superuser account.

Generate an encrypted grub2 password for the grub superuser account with the following command:

$ sudo grub2-setpassword
Enter password:
Confirm password:
```

## V-281167 RHEL 10 must require a unique superusers name upon booting into single-user and maintenance modes. {#V-281167}

Severity: medium · Rule: SV-281167r1268226_rule · STIG ID: RHEL-10-600010 · CCI-000213

**Discussion.** Having a nondefault grub superuser username makes password-guessing attacks less effective.

**Check.**

```
Verify RHEL 10 requires a unique superusers name upon booting into single-user and maintenance modes.

Verify that the boot loader superuser account has been set with the following command:

$ sudo grep -A1 "superusers" /etc/grub2.cfg
set superusers="<accountname>"
export superusers
password_pbkdf2 <accountname> ${GRUB2_PASSWORD}

Verify <accountname> is not a common name such as root, admin, or administrator.

If superusers contains easily guessable usernames, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have a unique username for the grub superuser account.

Edit the "/etc/grub.d/01_users" file and add or modify the following lines with a nondefault username for the superuser account:

set superusers="<accountname>"
export superusers

Once the superuser account has been added, update the "grub.cfg" file by regenerating the GRUB configuration with the following command:

$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg --update-bls-cmdline

Reboot the system:

$ sudo reboot
```

## V-281168 RHEL 10 must not assign an interactive login shell for system accounts. {#V-281168}

Severity: medium · Rule: SV-281168r1273589_rule · STIG ID: RHEL-10-600020 · CCI-002696

**Discussion.** Ensuring shells are not given to system accounts upon login makes it more difficult for attackers to use system accounts.

**Check.**

```
Verify that RHEL 10 system accounts do not have an interactive login shell.

Run the following command to list any system account (UID < 1000) that has an interactive shell, excluding authorized system utility accounts (root, sync, shutdown, halt):

$ $ awk -F: '(($3 > 0 && $3 < 1000) && $1 !~ /^(halt|sync|shutdown)$/ && $7 !~ /(nologin|false)$/) {print $1 ":" $3 ":" $7}' /etc/passwd

If the command returns any output, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that all noninteractive accounts on the system do not have an interactive shell assigned to them.

If the system account needs a shell assigned for mission operations, document the need with the information system security officer (ISSO).

Run the following command to disable the interactive shell for a specific noninteractive user account:

$ sudo usermod --shell /usr/sbin/nologin <user>
```

## V-281169 RHEL 10 user account passwords for new users or password changes must have a 180-day maximum password lifetime restriction in /etc/login.defs. {#V-281169}

Severity: medium · Rule: SV-281169r1273590_rule · STIG ID: RHEL-10-600100 · CCI-004066

**Discussion.** Any password, no matter how complex, can eventually be cracked; therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.

Setting the password maximum age ensures users are required to periodically change their passwords. Requiring shorter password lifetimes increases the risk of users writing down the password in a convenient location subject to physical compromise.

**Check.**

```
Verify that RHEL 10 enforces a 180-day maximum password lifetime for new user accounts by running the following command:

$ sudo grep -i pass_max_days /etc/login.defs
PASS_MAX_DAYS 180

If the "PASS_MAX_DAYS" parameter value is greater than "180", or commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce a 180-day maximum password lifetime.

Add, or modify the following line in the "/etc/login.defs" file:

PASS_MAX_DAYS 180
```

## V-281170 RHEL 10 must, for user account passwords, have a 180-day maximum password lifetime restriction {#V-281170}

Severity: medium · Rule: SV-281170r1273591_rule · STIG ID: RHEL-10-600110 · CCI-004066

**Discussion.** Any password, no matter how complex, can eventually be cracked; therefore, passwords need to be changed periodically. If RHEL 10 does not limit the lifetime of passwords and force users to change their passwords, there is the risk that RHEL 10 passwords could be compromised.

**Check.**

```
Verify RHEL 10 enforces a 180-day maximum time period for existing user account passwords with the following commands:

$ sudo awk -F: '$5 > 180 {print $1 " " $5}' /etc/shadow

$ sudo awk -F: '$5 <= 0 {print $1 " " $5}' /etc/shadow

If any results are returned that are not associated with a system account, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce a 180-day maximum password lifetime restriction on user account passwords.

Set the 180-day maximum password lifetime restriction with the following command:

$ sudo passwd -x 180 [user]
```

## V-281171 RHEL 10 must assign a home directory for local interactive user accounts upon creation. {#V-281171}

Severity: medium · Rule: SV-281171r1166465_rule · STIG ID: RHEL-10-600120 · CCI-002824

**Discussion.** If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.

**Check.**

```
Verify RHEL 10 assigns a home directory for local interactive user accounts upon creation with the following command:

$ sudo grep -i create_home /etc/login.defs
CREATE_HOME yes

If the value for "CREATE_HOME" parameter is not set to "yes", the line is missing, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to assign home directories to all new local interactive users by setting the "CREATE_HOME" parameter in "/etc/login.defs" to "yes" as follows:

CREATE_HOME yes
```

## V-281172 RHEL 10 must not allow duplicate user IDs (UIDs) to exist for interactive users. {#V-281172}

Severity: medium · Rule: SV-281172r1166468_rule · STIG ID: RHEL-10-600130 · CCI-000764 CCI-000804

**Discussion.** To ensure accountability and prevent unauthenticated access, interactive users must be identified and authenticated to prevent potential misuse and compromise of the system.

Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062

**Check.**

```
Verify RHEL 10 contains no duplicate UIDs for interactive users with the following command:

$ sudo awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd

If output is produced and the accounts listed are interactive user accounts, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not allow duplicate UIDs to exist for interactive users.

Edit the file "/etc/passwd", and provide each interactive user account that has a duplicate UID with a unique UID.
```

## V-281173 RHEL 10 must automatically expire temporary accounts within 72 hours. {#V-281173}

Severity: medium · Rule: SV-281173r1166471_rule · STIG ID: RHEL-10-600140 · CCI-001682 CCI-000016

**Discussion.** Temporary accounts are privileged or nonprivileged accounts that are established during pressing circumstances, such as new software or hardware configuration or an incident response, where the need for prompt account activation requires bypassing normal account authorization procedures. If any inactive temporary accounts are left enabled on the system and are not manually removed or automatically expired within 72 hours, the security posture of the system will be degraded and exposed to exploitation by unauthorized users or insider threat actors.

Temporary accounts are different from emergency accounts. Emergency accounts, also known as "last resort" or "break glass" accounts, are local login accounts enabled on the system for emergency use by authorized system administrators to manage a system when standard login methods are failing or not available. Emergency accounts are not subject to manual removal or scheduled expiration requirements.

The automatic expiration of temporary accounts may be extended as needed by the circumstances, but it must not be extended indefinitely. A documented permanent account should be established for privileged users who need long-term maintenance accounts.

Satisfies: SRG-OS-000123-GPOS-00064, SRG-OS-000002-GPOS-00002

**Check.**

```
Verify RHEL 10 automatically expires temporary accounts within 72 hours.

For every existing temporary account, run the following command to obtain its account expiration information:

$ sudo chage -l <temporary_account_name> | grep -i "account expires"

Verify each of these accounts has an expiration date set within 72 hours.

If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to expire temporary accounts after 72 hours with the following command:

$ sudo chage -E $(date -d +3days +%Y-%m-%d) <temporary_account_name>
```

## V-281174 RHEL 10 must assign a primary group to all interactive users. {#V-281174}

Severity: medium · Rule: SV-281174r1166474_rule · STIG ID: RHEL-10-600150 · CCI-000764

**Discussion.** If a user is assigned the group identifier (GID) of a group that does not exist on the system, and a group with the GID is subsequently created, the user may have unintended rights to any files associated with the group.

**Check.**

```
Verify RHEL 10 interactive users have a valid GID.

Check that the interactive users have a valid GID with the following command:

$ sudo pwck -r

If pwck reports "no group" for any interactive user, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that all GIDs referenced in "/etc/passwd" are defined in "/etc/group".

Edit the file "/etc/passwd" and ensure that every user's GID is a valid GID.
```

## V-281175 RHEL 10 must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity. {#V-281175}

Severity: medium · Rule: SV-281175r1197238_rule · STIG ID: RHEL-10-600160 · CCI-003627 CCI-003628

**Discussion.** Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system.

Disabling inactive accounts ensures accounts that may not have been responsibly removed are not available to attackers who may have compromised their credentials.

Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained.

Satisfies: SRG-OS-000118-GPOS-00060, SRG-OS-000590-GPOS-00110

**Check.**

```
Verify RHEL 10 account identifiers (individuals, groups, roles, and devices) are disabled after 35 days of inactivity.

Check the account inactivity value by performing the following command:

$ sudo grep -i inactive /etc/default/useradd
INACTIVE=35

If "INACTIVE" is set to "-1", a value greater than "35", or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable account identifiers after 35 days of inactivity after the password expiration.

Run the following command to change the configuration for "useradd":

$ sudo useradd -D -f 35

A recommendation is 35 days, but a lower value is acceptable.
```

## V-281176 RHEL 10 must be configured so that all local interactive user initialization file executable search path statements do not contain statements that will reference a working directory other than user home directories. {#V-281176}

Severity: medium · Rule: SV-281176r1166480_rule · STIG ID: RHEL-10-600170 · CCI-003980

**Discussion.** The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory (other than the user's home directory), executables in these directories may be executed instead of system commands.

This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon or two consecutive colons, this is interpreted as the current working directory. If deviations from the default system search path for the local interactive user are required, they must be documented with the information system security officer (ISSO).

**Check.**

```
Verify RHEL 10 local interactive user initialization file executable search path statements do not contain statements that will reference a working directory other than user home directories with the following commands:

$ sudo find /home -maxdepth 2 -type f -name ".[^.]*" -exec grep -iH path= {} \;
PATH="$HOME/.local/bin:$HOME/bin:$PATH"

If any local interactive user initialization files have executable search path statements that include directories outside of their home directory, and this is not documented with the ISSO as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that all local interactive user initialization file executable search path statements do not contain statements that will reference a working directory other than user home directories.

Edit the local interactive user initialization files to change any PATH variable statements that reference directories other than their home directory.

If a local interactive user requires path variables to reference a directory owned by the application, it must be documented with the ISSO.
```

## V-281177 RHEL 10 must assign a home directory to all local interactive users in the "/etc/passwd" file. {#V-281177}

Severity: medium · Rule: SV-281177r1184748_rule · STIG ID: RHEL-10-600180 · CCI-002385

**Discussion.** If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.

**Check.**

```
Verify RHEL 10 interactive users have a home directory assigned with the following command:

$ sudo awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $3, $6}' /etc/passwd
nsauser:x:1000:1000:nsauser:/home/nsauser:/bin/bash
disauser:x:1001:1001:disauser:/home/disauser:/bin/bash
doduser:x:1002:1002:doduser:/home/doduser:/bin/bash

Inspect the output and verify that all interactive users (normally users with a user identifier [UID] greater than 1000) have a home directory defined.

If a user's home directory is not defined, this is a finding.
```

**Fix.**

```
Configure RHEL 10 interactive users to have a home directory assigned in the "/etc/passwd" file.

Create and assign home directories to all local interactive users on RHEL 10 that do not have a home directory assigned.
```

## V-281178 RHEL 10 must ensure that all local interactive user home directories defined in the "/etc/passwd" file must exist. {#V-281178}

Severity: medium · Rule: SV-281178r1195418_rule · STIG ID: RHEL-10-600190 · CCI-002385

**Discussion.** If a local interactive user has a home directory defined that does not exist, the user may be given access to the / directory as the current working directory upon login. This could create a denial of service because the user would not be able to access their login configuration files, and it may give them visibility to system files they normally would not be able to access.

**Check.**

```
Verify RHEL 10 interactive users' home directories exist on the system with the following command:

$ sudo pwck -r
user 'mailnull': directory 'var/spool/mqueue' does not exist

The output should not return any interactive users.

If an interactive user's home directory does not exist, this is a finding.
```

**Fix.**

```
Configure RHEL 10 interactive users' home directories to exist on the system.

Create home directories to all local interactive users that do not have a home directory assigned. Use the following commands to create the user home directory assigned in "/etc/ passwd":

Note: The example will be for the user "disauser", who has a home directory of "/home/disauser", a user identifier (UID) of "disauser", and a group identifier (GID) of "users assigned" in "/etc/passwd".

$ sudo mkdir /home/disauser
$ sudo chown disauser /home/disauser
$ sudo chgrp users /home/disauser
$ sudo chmod 0750 /home/disauser
```

## V-281179 RHEL 10 must enforce a delay of at least four seconds between login prompts following a failed login attempt. {#V-281179}

Severity: medium · Rule: SV-281179r1166489_rule · STIG ID: RHEL-10-600200 · CCI-002238

**Discussion.** Increasing the time between a failed authentication attempt and reprompting to enter credentials helps to slow a single-threaded brute-force attack.

**Check.**

```
Verify RHEL 10 enforces a delay of at least four seconds between console login prompts following a failed login attempt with the following command:

$ sudo grep -i fail_delay /etc/login.defs
FAIL_DELAY 4

If the value of "FAIL_DELAY" is not set to "4" or greater, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce a delay of at least four seconds between login prompts following a failed console login attempt.

Modify the "/etc/login.defs" file to set the "FAIL_DELAY" parameter to "4" or greater:

FAIL_DELAY 4
```

## V-281180 RHEL 10 must enforce a 24-hours minimum password lifetime restriction for passwords for new users or password changes in "/etc/login.defs". {#V-281180}

Severity: medium · Rule: SV-281180r1166492_rule · STIG ID: RHEL-10-600210 · CCI-004066

**Discussion.** Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.

Setting the minimum password age protects against users cycling back to a favorite password after satisfying the password reuse requirement.

**Check.**

```
Verify RHEL 10 enforces 24 hours as the minimum password lifetime for new user accounts.

Check for the value of "PASS_MIN_DAYS" in "/etc/login.defs" with the following command:

$ sudo grep -i pass_min_days /etc/login.defs
PASS_MIN_DAYS 1

If the "PASS_MIN_DAYS" parameter value is not "1" or greater or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce 24 hours as the minimum password lifetime.

Add the following line in "/etc/login.defs" (or modify the line to have the required value):

PASS_MIN_DAYS 1
```

## V-281181 RHEL 10 must enforce that passwords be created with a minimum of 15 characters. {#V-281181}

Severity: medium · Rule: SV-281181r1273592_rule · STIG ID: RHEL-10-600220 · CCI-004066

**Discussion.** The shorter the password, the lower the number of possible combinations that must be tested before the password is compromised.

Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to increase exponentially the time and/or resources required to compromise the password.

RHEL 10 uses "pwquality" as a mechanism to enforce password complexity. Configurations are set in the "etc/security/pwquality.conf" file.

The "minlen", sometimes noted as minimum length, acts as a "score" of complexity based on the credit components of the "pwquality" module. By setting the credit components to a negative value, those components will not only be required but will not count toward the total "score" of "minlen". This will enable "minlen" to require a 15-character minimum.

The DoW minimum password requirement is 15 characters.

**Check.**

```
Verify RHEL 10 enforces a minimum 15-character password length with the following command:

$ sudo grep -s minlen /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf
/etc/security/pwquality.conf:minlen = 15

If the command does not return a "minlen" value of "15" or greater, does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce a minimum 15-character password length.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "minlen" parameter:

minlen = 15
```

## V-281182 RHEL 10 must enforce password complexity by requiring at least one special character to be used. {#V-281182}

Severity: medium · Rule: SV-281182r1195424_rule · STIG ID: RHEL-10-600230 · CCI-004066

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that must be tested before the password is compromised.

RHEL 10 uses "pwquality" as a mechanism to enforce password complexity. Note that to require special characters without degrading the "minlen" value, the credit value must be expressed as a negative number in "/etc/security/pwquality.conf".

**Check.**

```
Verify RHEL 10 enforces password complexity by requiring that at least one special character be used with the following command:

$ sudo grep -s ocredit /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf
/etc/security/pwquality.conf:# ocredit = 0

If the value of "ocredit" is a positive number or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce password complexity by requiring that at least one special character be used by setting the "ocredit" option.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "ocredit" parameter:

ocredit = -1
```

## V-281183 RHEL 10 must enforce password complexity by requiring that at least one lowercase character be used. {#V-281183}

Severity: medium · Rule: SV-281183r1195427_rule · STIG ID: RHEL-10-600240 · CCI-004066

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that must be tested before the password is compromised.

Requiring a minimum number of lowercase characters makes password guessing attacks more difficult by ensuring a larger search space.

**Check.**

```
Verify RHEL 10 enforces password complexity by requiring that at least one lowercase character be used with the following command:

$ sudo grep -s lcredit /etc/security/pwquality.conf /etc/security/pwquality.conf/*.conf
/etc/security/pwquality.conf:lcredit = -1

If the value of "lcredit" is a positive number or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce password complexity by requiring that at least one lowercase character be used by setting the "lcredit" option.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "lcredit" parameter:

lcredit = -1
```

## V-281184 RHEL 10 must enforce password complexity by requiring that at least one uppercase character be used. {#V-281184}

Severity: medium · Rule: SV-281184r1197239_rule · STIG ID: RHEL-10-600250 · CCI-004066

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that must be tested before the password is compromised.

Requiring a minimum number of uppercase characters makes password guessing attacks more difficult by ensuring a larger search space.

Satisfies: SRG-OS-000069-GPOS-00037, SRG-OS-000070-GPOS-00038

**Check.**

```
Verify RHEL 10 enforces password complexity by requiring that at least one uppercase character be used.

Check the value for "ucredit" with the following command:

$ sudo grep -s ucredit /etc/security/pwquality.conf /etc/security/pwquality.conf/*.conf
/etc/security/pwquality.conf:ucredit = -1

If the value of "ucredit" is a positive number or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce password complexity by requiring that at least one uppercase character be used by setting the "ucredit" option.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "ucredit" parameter:

ucredit = -1
```

## V-281185 RHEL 10 must require the change of at least eight characters when passwords are changed. {#V-281185}

Severity: medium · Rule: SV-281185r1195433_rule · STIG ID: RHEL-10-600260 · CCI-004066

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute–force attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that must be tested before the password is compromised.

Requiring a minimum number of different characters during password changes ensures that newly changed passwords should not resemble previously compromised ones.

Note that passwords that are changed on compromised systems will still be compromised.

**Check.**

```
Verify RHEL 10 requires the change of at least eight characters when passwords are changed by checking the value of the "difok" option in "/etc/security/pwquality.conf" with the following command:

$ sudo grep difok -s /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf
/etc/security/pwquality.conf:difok = 8

If the value of "difok" is set to less than "8" or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to require the change of at least eight of the total number of characters when passwords are changed by setting the "difok" option.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "difok" parameter:

difok = 8
```

## V-281186 RHEL 10 must enforce that passwords have a 24 hours/1 day minimum lifetime restriction in "/etc/shadow". {#V-281186}

Severity: medium · Rule: SV-281186r1184622_rule · STIG ID: RHEL-10-600270 · CCI-004066

**Discussion.** Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy for password reuse.

**Check.**

```
Verify the minimum time period between password changes for each user account is one day or greater with the following command:

$ sudo awk -F: '$4 < 1 {printf "%s %d\n", $1, $4}' /etc/shadow

If any results are returned that are not associated with a system account, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that noncompliant accounts enforce a 24 hours/1 day minimum password lifetime:

$ sudo passwd -n 1 [user]
```

## V-281187 RHEL 10 must require the maximum number of repeating characters of the same character class to be limited to four when passwords are changed. {#V-281187}

Severity: medium · Rule: SV-281187r1195436_rule · STIG ID: RHEL-10-600280 · CCI-004066 CCI-004065

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password.

Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex a password is, the greater the number of possible combinations that must be tested before the password is compromised.

Satisfies: SRG-OS-000072-GPOS-00040, SRG-OS-000730-GPOS-00190

**Check.**

```
Verify RHEL 10 limits the value of the "maxclassrepeat" option in "/etc/security/pwquality.conf" with the following command:

$ sud grep -s maxclassrepeat /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf
/etc/security/pwquality.conf:maxclassrepeat = 4

If the value of "maxclassrepeat" is set to "0" or more than "4" or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to require the change of the number of repeating characters of the same character class when passwords are changed by setting the "maxclassrepeat" option.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "maxclassrepeat" parameter:

maxclassrepeat = 4
```

## V-281188 RHEL 10 must require that the maximum number of repeating characters be limited to three when passwords are changed. {#V-281188}

Severity: medium · Rule: SV-281188r1195439_rule · STIG ID: RHEL-10-600290 · CCI-004066

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password.

Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex a password is, the greater the number of possible combinations that must be tested before the password is compromised.

**Check.**

```
Verify RHEL 10 limits the value of the "maxrepeat" option in "/etc/security/pwquality.conf" with the following command:

$ sudo grep -s maxrepeat /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf
/etc/security/pwquality.conf:maxrepeat = 3

If the value of "maxrepeat" is set to more than "3" or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to require the change of the number of repeating consecutive characters when passwords are changed by setting the "maxrepeat" option.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "maxrepeat" parameter:

maxrepeat = 3
```

## V-281189 RHEL 10 must require the change of at least four character classes when passwords are changed. {#V-281189}

Severity: medium · Rule: SV-281189r1195442_rule · STIG ID: RHEL-10-600300 · CCI-004066

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password. 

Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex a password is, the greater the number of possible combinations that must be tested before the password is compromised.

**Check.**

```
Verify RHEL 10 sets the value of the "minclass" option in "/etc/security/pwquality.conf" with the following command:

$ sudo grep -s minclass /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf
/etc/security/pwquality.conf:minclass = 4

If the value of "minclass" is set to less than "4" or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to require the change of at least four character classes when passwords are changed by setting the "minclass" option.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "minclass" parameter:

minclass = 4
```

## V-281190 RHEL 10 must enforce password complexity by requiring that at least one numeric character be used. {#V-281190}

Severity: medium · Rule: SV-281190r1195445_rule · STIG ID: RHEL-10-600310 · CCI-004066

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that must be tested before the password is compromised.

Requiring digits makes password guessing attacks more difficult by ensuring a larger search space.

**Check.**

```
Verify RHEL 10 enforces password complexity by requiring that at least one numeric character be used.

Check the value for "dcredit" with the following command:

$ sudo grep -s dcredit /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf
/etc/security/pwquality.conf:dcredit = -1

If the value of "dcredit" is a positive number or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce password complexity by requiring that at least one numeric character be used by setting the "dcredit" option.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "dcredit" parameter:

dcredit = -1
```

## V-281191 RHEL 10 must prevent the use of dictionary words for passwords. {#V-281191}

Severity: medium · Rule: SV-281191r1195448_rule · STIG ID: RHEL-10-600320 · CCI-004066

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

If RHEL 10 allows the user to select passwords based on dictionary words, this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.

Satisfies: SRG-OS-000480-GPOS-00225, SRG-OS-000072-GPOS-00040

**Check.**

```
Verify RHEL 10 prevents the use of dictionary words for passwords with the following command:

$ sudo grep -s dictcheck /etc/security/pwquality.conf /etc/pwquality.conf.d/*.conf
/etc/security/pwquality.conf:dictcheck=1

If "dictcheck" does not have a value other than "0" or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent the use of dictionary words for passwords.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "dictcheck" parameter:

dictcheck=1
```

## V-281192 RHEL 10 must allow only the root account to have unrestricted access to the system. {#V-281192}

Severity: medium · Rule: SV-281192r1268226_rule · STIG ID: RHEL-10-600400 · CCI-000213

**Discussion.** An account has root authority if it has a user identifier (UID) of "0". Multiple accounts with a UID of "0" afford more opportunity for potential intruders to guess a password for a privileged account. Proper configuration of sudo is recommended to afford multiple system administrators access to root privileges in an accountable manner.

**Check.**

```
Verify RHEL 10 is configured so that only the "root" account has a UID "0" assignment with the following command:

$ awk -F: '$3 == 0 {print $1}' /etc/passwd
root

If any accounts other than "root" have a UID of "0", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that only the "root" account has a UID assignment of "0".

Change the UID of any account on the system, other than "root", that has a UID of "0".

If the account is associated with system commands or applications, the UID should be changed to one greater than "0" but less than "1000". Otherwise, assign a UID of greater than "1000" that has not already been assigned.
```

## V-281193 RHEL 10 must enforce password complexity rules for the "root" account. {#V-281193}

Severity: medium · Rule: SV-281193r1166531_rule · STIG ID: RHEL-10-600405 · CCI-004066

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that must be tested before the password is compromised.

Satisfies: SRG-OS-000072-GPOS-00040, SRG-OS-000071-GPOS-00039, SRG-OS-000070-GPOS-00038, SRG-OS-000266-GPOS-00101, SRG-OS-000078-GPOS-00046, SRG-OS-000480-GPOS-00225, SRG-OS-000069-GPOS-00037

**Check.**

```
Verify RHEL 10 enforces password complexity rules for the "root" account.

Check if "root" user is required to use complex passwords with the following command:

$ sudo grep enforce_for_root /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf
/etc/security/pwquality.conf:enforce_for_root

If "enforce_for_root" is commented out or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce password complexity on the "root" account.

Add or update the following line in the "/etc/security/pwquality.conf" file or a configuration file in the "/etc/security/pwquality.conf.d/" directory to contain the "enforce_for_root" parameter:

enforce_for_root
```

## V-281194 RHEL 10 must automatically lock an account when three unsuccessful login attempts occur. {#V-281194}

Severity: medium · Rule: SV-281194r1166534_rule · STIG ID: RHEL-10-600410 · CCI-002238 CCI-000044

**Discussion.** By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.

Satisfies: SRG-OS-000329-GPOS-00128, SRG-OS-000021-GPOS-00005

**Check.**

```
Verify RHEL 10 is configured to lock an account after three unsuccessful login attempts with the following command:

$ sudo grep 'deny =' /etc/security/faillock.conf
deny = 3

If the "deny" option is not set to "3" or less (but not "0"), or is missing or commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to lock an account when three unsuccessful login attempts occur.

Add/modify the "/etc/security/faillock.conf" file to match the following line:

deny = 3
```

## V-281195 RHEL 10 must automatically lock the root account until the root account is released by an administrator when three unsuccessful login attempts occur during a 15-minute time period. {#V-281195}

Severity: medium · Rule: SV-281195r1166537_rule · STIG ID: RHEL-10-600415 · CCI-002238 CCI-000044

**Discussion.** By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, also known as brute-forcing, is reduced. Limits are imposed by locking the account.

Satisfies: SRG-OS-000329-GPOS-00128, SRG-OS-000021-GPOS-00005

**Check.**

```
Verify RHEL 10 is configured to lock the root account after three unsuccessful login attempts with the following command:

$ sudo grep even_deny_root /etc/security/faillock.conf
even_deny_root

If the "even_deny_root" option is not set or is missing or commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to lock out the "root" account after a number of incorrect login attempts using "pam_faillock.so".

Enable the feature using the following command:

$ sudo authselect enable-feature with-faillock

Edit the "/etc/security/faillock.conf" by uncommenting or adding the following line:

even_deny_root
```

## V-281196 RHEL 10 must automatically lock an account when three unsuccessful login attempts occur during a 15-minute time period. {#V-281196}

Severity: medium · Rule: SV-281196r1166540_rule · STIG ID: RHEL-10-600420 · CCI-002238 CCI-000044

**Discussion.** By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.

Satisfies: SRG-OS-000329-GPOS-00128, SRG-OS-000021-GPOS-00005

**Check.**

```
Verify RHEL 10 locks an account after three unsuccessful login attempts within a period of 15 minutes with the following command:

$ sudo grep fail_interval /etc/security/faillock.conf
fail_interval = 900

If the "fail_interval" option is not set to "900" or less (but not "0"), the line is commented out, or the line is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to lock out the "root" account after a number of incorrect login attempts within 15 minutes using "pam_faillock.so". 

Enable the feature using the following command:

$ authselect enable-feature with-faillock

Edit the "/etc/security/faillock.conf" file as follows:

fail_interval = 900
```

## V-281197 RHEL 10 must maintain an account lock until the locked account is released by an administrator. {#V-281197}

Severity: medium · Rule: SV-281197r1166543_rule · STIG ID: RHEL-10-600425 · CCI-002238 CCI-000044

**Discussion.** By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.

Satisfies: SRG-OS-000329-GPOS-00128, SRG-OS-000021-GPOS-00005

**Check.**

```
Verify RHEL 10 is configured to lock an account after three unsuccessful login attempts until released by an administrator with the following command:

$ sudo grep 'unlock_time =' /etc/security/faillock.conf
unlock_time = 0

If the "unlock_time" option is not set to "0", or the line is missing or commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to lock an account after three unsuccessful login attempts until released by an administrator with the following command:

$ authselect enable-feature with-faillock

Edit the "/etc/security/faillock.conf" file as follows:

unlock_time = 0
```

## V-281198 RHEL 10 must ensure account lockouts persist. {#V-281198}

Severity: medium · Rule: SV-281198r1166546_rule · STIG ID: RHEL-10-600430 · CCI-000044 CCI-002238

**Discussion.** Having lockouts persist across reboots ensures that an account is unlocked only by an administrator. If the lockouts did not persist across reboots, an attacker could reboot the system to continue brute force attacks against the accounts on the system.

Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128

**Check.**

```
Verify RHEL 10 is configured so that the "/etc/security/faillock.conf" file uses a nondefault "faillock" directory to ensure contents persist after reboot with the following command:

$ sudo grep -w dir /etc/security/faillock.conf
dir = /var/log/faillock

If the "dir" option is not set to a nondefault documented tally log directory, is commented out, or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to maintain the contents of the "faillock" directory after a reboot.

Add/modify the "/etc/security/faillock.conf" file to match the following line:

dir = /var/log/faillock
```

## V-281199 RHEL 10 must not have unauthorized accounts. {#V-281199}

Severity: medium · Rule: SV-281199r1268226_rule · STIG ID: RHEL-10-600450 · CCI-000213

**Discussion.** Having lockouts persist across reboots ensures that account is unlocked only by an administrator. If the lockouts did not persist across reboots, an attacker could reboot the system to continue brute force attacks against the accounts on the system.

**Check.**

```
Verify RHEL 10 has no unauthorized local interactive user accounts with the following command:

$ less /etc/passwd
root:x:0:0:root:/root:/bin/bash
...
nsauser:x:1000:1000:nsauser:/home/nsauser:/bin/bash
doduser:x:1001:1001:doduser:/home/doduser:/bin/bash

Interactive user accounts generally will have a user ID (UID) of 1000 or greater, a home directory in a specific partition, and an interactive shell.

Obtain the list of interactive user accounts authorized to be on the system from the system administrator or information system security officer and compare it to the list of local interactive user accounts on the system.

If there are unauthorized local user accounts on the system, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have no unauthorized local interactive user accounts with the following command, where <unauthorized_user> is the unauthorized account:

$ sudo userdel  <unauthorized_user>
```

## V-281200 RHEL 10 must not allow blank or null passwords. {#V-281200}

Severity: medium · Rule: SV-281200r1166552_rule · STIG ID: RHEL-10-600455 · CCI-004066

**Discussion.** If an account has an empty password, anyone could log in and run commands with the privileges of that account. Accounts with empty passwords must never be used in operational environments.

**Check.**

```
Verify RHEL 10 prohibits the use of null passwords with the following command:

$ sudo grep -i nullok /etc/pam.d/system-auth /etc/pam.d/password-auth

If output is produced, this is a finding.

If the system administrator (SA) can demonstrate that the required configuration is contained in a PAM configuration file included or substacked from the "system-auth" file, this is not a finding.
```

**Fix.**

```
Configure RHEL 10 to prohibit the use of null passwords.

If PAM is managed with "authselect", use the following command to remove instances of "nullok":

$ sudo authselect enable-feature without-nullok

Otherwise, remove any instances of the "nullok" option in the "/etc/pam.d/password-auth" and "/etc/pam.d/system-auth" files to prevent logins with empty passwords.

Note: Manual changes to the listed file may be overwritten by the "authselect" program.
```

## V-281201 RHEL 10 must not have accounts configured with blank or null passwords. {#V-281201}

Severity: medium · Rule: SV-281201r1166555_rule · STIG ID: RHEL-10-600460 · CCI-004066

**Discussion.** If an account has an empty password, anyone could log in and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.

**Check.**

```
Verify RHEL 10 prohibits null or blank passwords with the following command:

$ sudo awk -F: '!$2 {print $1}' /etc/shadow

If the command returns any results, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that all accounts have a password, or lock the account with the following commands:

Perform a password reset:

$ sudo passwd [username]

To lock an account:

$ sudo passwd -l [username]
```

## V-281202 RHEL 10 must have a unique group ID (GID) for each group in "/etc/group". {#V-281202}

Severity: medium · Rule: SV-281202r1166558_rule · STIG ID: RHEL-10-600470 · CCI-000764

**Discussion.** To ensure accountability and prevent unauthenticated access, groups must be identified uniquely to prevent potential misuse and compromise of the system.

**Check.**

```
Verify RHEL 10 contains no duplicate GIDs for interactive users with the following command:

 $  cut -d : -f 3 /etc/group | uniq -d

If the system has duplicate GIDs, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to contain no duplicate GIDs for interactive users.

Edit the file "/etc/group", and provide each group that has a duplicate GID with a unique GID.
```

## V-281203 RHEL 10 must limit the number of concurrent sessions to 10 for all accounts and/or account types. {#V-281203}

Severity: low · Rule: SV-281203r1166561_rule · STIG ID: RHEL-10-600475 · CCI-000054

**Discussion.** Operating system management includes the ability to control the number of users and user sessions that use an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to denial-of-service (DoS) attacks.

This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system.

**Check.**

```
Verify RHEL 10 limits the number of concurrent sessions to "10" for all accounts and/or account types with the following command:

$ sudo grep -rs maxlogins /etc/security/limits.conf /etc/security/limits.d/*.conf | grep -v '#'
/etc/security/limits.d/maxlogins.conf:* hard maxlogins 10

This can be set as a global domain (with the * wildcard) but may be set differently for multiple domains.

If the "maxlogins" item is missing or commented out, or the value is set greater than "10" and is not documented with the information system security officer as an operational requirement for all domains that have the "maxlogins" item assigned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to limit the number of concurrent sessions to "10" for all accounts and/or account types.

Add the following line to the top of "/etc/security/limits.conf" or in a ".conf" file defined in "/etc/security/limits.d/":

* hard maxlogins 10
```

## V-281204 RHEL 10 must ensure the password complexity module in the system-auth file is configured for three or fewer retries. {#V-281204}

Severity: medium · Rule: SV-281204r1197240_rule · STIG ID: RHEL-10-600485 · CCI-004066

**Discussion.** Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system.

RHEL 10 uses "pwquality" as a mechanism to enforce password complexity. This is set in both of the following: 

"/etc/pam.d/password-auth"
"/etc/pam.d/system-auth"

By limiting the number of attempts to meet the pwquality module complexity requirements before returning with an error, the system will audit abnormal attempts at password changes.

**Check.**

```
Verify RHEL 10 is configured to limit the "pwquality" retry option to "3" with the following command:

$ sudo grep -w retry /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf 
retry = 3 

If the value of "retry" is set to "0" or greater than "3", is commented out, or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to limit the "pwquality" retry option to "3".

Add or update the following line in the "/etc/security/pwquality.conf" file or a file in the "/etc/security/pwquality.conf.d/" directory to contain the "retry" parameter:

retry = 3
```

## V-281205 RHEL 10 must restrict the use of the "su" command. {#V-281205}

Severity: medium · Rule: SV-281205r1166567_rule · STIG ID: RHEL-10-600500 · CCI-002038 CCI-002165

**Discussion.** The "su" program allows commands to be run with a substitute user and group ID. It is commonly used to run commands as the root user. Limiting access to such commands is considered a good security practice.

Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000312-GPOS-00123

**Check.**

```
Verify RHEL 10 requires users to be members of the "wheel" group to run "su".

Verify the configuration with the following command:

$ sudo grep pam_wheel /etc/pam.d/su
auth             required        pam_wheel.so use_uid

If a line for "pam_wheel.so" does not exist or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to require users to be in the "wheel" group to run the "su" command.

Edit the configuration file:

$ sudo vi /etc/pam.d/su

Add the following lines:

auth    required    pam_wheel.so use_uid
$ sed '/^[[:space:]]*#[[:space:]]*auth[[:space:]]\+required[[:space:]]\+pam_wheel\.so[[:space:]]\+use_uid$/s/^[[:space:]]*#//' -i /etc/pam.d/su

If necessary, create a "wheel" group and add administrative users to the group.
```

## V-281206 RHEL 10 must be configured to not bypass password requirements for privilege escalation. {#V-281206}

Severity: medium · Rule: SV-281206r1166570_rule · STIG ID: RHEL-10-600510 · CCI-002038

**Discussion.** Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate.

Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158

**Check.**

```
Verify RHEL 10 is not configured to bypass password requirements for privilege escalation with the following command:

$ sudo grep pam_succeed_if /etc/pam.d/sudo

If any occurrences of "pam_succeed_if" are returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to require users to supply a password for privilege escalation.

Remove any occurrences of " pam_succeed_if " in the "/etc/pam.d/sudo" file.
```

## V-281207 RHEL 10 must restrict privilege elevation to authorized personnel. {#V-281207}

Severity: medium · Rule: SV-281207r1166573_rule · STIG ID: RHEL-10-600520 · CCI-002696

**Discussion.** If the "sudoers" file is not configured correctly, any user defined on the system can initiate privileged actions on the target system.

**Check.**

```
Verify RHEL 10 restricts privilege elevation to authorized personnel with the following command:

$ sudo grep -riw ALL /etc/sudoers /etc/sudoers.d/ | grep -v "#"

If the either of the following entries is returned, this is a finding:

ALL     ALL=(ALL) ALL
ALL     ALL=(ALL:ALL) ALL
```

**Fix.**

```
Configure RHEL 10 to restrict privilege elevation to authorized personnel.

Remove the following entries from the "/etc/sudoers" file or configuration file under "/etc/sudoers.d/":

ALL     ALL=(ALL) ALL
ALL     ALL=(ALL:ALL) ALL
```

## V-281208 RHEL 10 must require users to reauthenticate for privilege escalation. {#V-281208}

Severity: medium · Rule: SV-281208r1166576_rule · STIG ID: RHEL-10-600530 · CCI-002038

**Discussion.** Without reauthentication, users may access resources or perform tasks for which they do not have authorization.

When operating systems provide the capability to escalate a functional capability, it is critical that the user reauthenticate.

Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158

**Check.**

```
Verify RHEL 10 "/etc/sudoers" has no occurrences of "!authenticate" with the following command:

$ sudo grep -ir '!authenticate' /etc/sudoers /etc/sudoers.d/

If any occurrences of "!authenticate" are returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not allow users to execute privileged actions without authenticating.

Remove any occurrence of "!authenticate" found in the "/etc/sudoers" file or files in the "/etc/sudoers.d" directory:

$ sudo sed -i '/\!authenticate/ s/^/# /g' /etc/sudoers /etc/sudoers.d/*
```

## V-281209 RHEL 10 must require reauthentication when using the "sudo" command. {#V-281209}

Severity: medium · Rule: SV-281209r1166579_rule · STIG ID: RHEL-10-600540 · CCI-002038

**Discussion.** Without reauthentication, users may access resources or perform tasks for which they do not have authorization.

When operating systems provide the capability to escalate a functional capability, it is critical that the organization requires the user to reauthenticate when using the "sudo" command.

If the value is set to an integer less than "0", the user's time stamp will not expire, and the user will not have to reauthenticate for privileged actions until the user's session is terminated.

Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158

**Check.**

```
Verify RHEL 10 requires reauthentication when using the "sudo" command to elevate privileges with the following command:

$ sudo grep -ir 'timestamp_timeout' /etc/sudoers /etc/sudoers.d/
/etc/sudoers:Defaults timestamp_timeout=0

If results are returned from more than one file location, this is a finding.

If "timestamp_timeout" is set to a negative number, is commented out, or no results are returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to reauthenticate "sudo" commands after the specified timeout.

Add the following line to "/etc/sudoers" or a file in "/etc/sudoers.d":

Defaults timestamp_timeout=0
```

## V-281210 RHEL 10 must use the invoking user's password for privilege escalation when using "sudo". {#V-281210}

Severity: medium · Rule: SV-281210r1166582_rule · STIG ID: RHEL-10-600550 · CCI-002038

**Discussion.** If the "rootpw", "targetpw", or "runaspw" flags are defined and not disabled, by default the operating system will prompt the invoking user for the "root" user password.

**Check.**

```
Verify RHEL 10 sudoers security policy is configured to use the invoking user's password for privilege escalation with the following command:

$ sudo grep -irE '(!rootpw|!targetpw|!runaspw)' /etc/sudoers /etc/sudoers.d/ | grep -v '#'
/etc/sudoers:Defaults !targetpw
/etc/sudoers:Defaults !rootpw
/etc/sudoers:Defaults !runaspw

If no results are returned, this is a finding.

If results are returned from more than one file location, this is a finding.

If "Defaults !targetpw" is not defined, this is a finding.

If "Defaults !rootpw" is not defined, this is a finding.

If "Defaults !runaspw" is not defined, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use the invoking user's password for privilege escalation when using "sudo".

Define the following in the Defaults section of the /etc/sudoers file or a single configuration file in the /etc/sudoers.d/ directory:

Defaults !targetpw
Defaults !rootpw
Defaults !runaspw
```

## V-281211 RHEL 10 must require users to provide a password for privilege escalation. {#V-281211}

Severity: high · Rule: SV-281211r1166585_rule · STIG ID: RHEL-10-600560 · CCI-002038

**Discussion.** Without reauthentication, users may access resources or perform tasks for which they do not have authorization.

When operating systems provide the capability to escalate a functional capability, it is critical that the user reauthenticate.

Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158

**Check.**

```
Verify RHEL 10 has no occurrences of "NOPASSWD" in "/etc/sudoers" with the following command:

$ sudo grep -ir nopasswd /etc/sudoers /etc/sudoers.d/ | grep -v '#'

If any occurrences of "NOPASSWD" are returned from the command and have not been documented with the information system security officer as an organizationally defined administrative group using multifactor authentication, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not allow users to execute privileged actions without authenticating with a password.

Remove any occurrence of "NOPASSWD" found in the "/etc/sudoers" file or files in the "/etc/sudoers.d" directory:

$ sudo find /etc/sudoers /etc/sudoers.d -type f -exec sed -i '/NOPASSWD/ s/^/# /g' {} \;
```

## V-281212 RHEL 10 must configure the use of the pam_faillock.so module in the "/etc/pam.d/system-auth" file. {#V-281212}

Severity: medium · Rule: SV-281212r1166588_rule · STIG ID: RHEL-10-600600 · CCI-000044

**Discussion.** If the pam_faillock.so module is not loaded, the system will not correctly lock out accounts to prevent password guessing attacks.

**Check.**

```
Verify RHEL 10 includes the use of the pam_faillock.so module in the "/etc/pam.d/system-auth" file:

$ sudo grep pam_faillock.so /etc/pam.d/system-auth
auth required pam_faillock.so preauth
auth required pam_faillock.so authfail
account required pam_faillock.so

If the pam_faillock.so module is not present in the "/etc/pam.d/system-auth" file with the "preauth" line listed before pam_unix.so, this is a finding.

If the system administrator can demonstrate that the required configuration is contained in a PAM configuration file included or substacked from the "system-auth" file, this is not a finding.
```

**Fix.**

```
Configure RHEL 10 to include the use of the pam_faillock.so module in the "/etc/pam.d/system-auth" file.

If PAM is managed with authselect, enable the feature with the following command:

$ sudo authselect enable-feature with-faillock

Otherwise, add/modify the appropriate sections of the "/etc/pam.d/system-auth" file to match the following lines:

Note: The "preauth" line must be listed before pam_unix.so.

auth required pam_faillock.so preauth
auth required pam_faillock.so authfail
account required pam_faillock.so
```

## V-281213 RHEL 10 must configure the use of the pam_faillock.so module in the "/etc/pam.d/password-auth" file. {#V-281213}

Severity: medium · Rule: SV-281213r1166591_rule · STIG ID: RHEL-10-600610 · CCI-000044

**Discussion.** If the pam_faillock.so module is not loaded, the system will not correctly lock out accounts to prevent password guessing attacks.

**Check.**

```
Verify RHEL 10 includes the pam_faillock.so module in the "/etc/pam.d/password-auth" file:

$ sudo grep pam_faillock.so /etc/pam.d/password-auth
auth required pam_faillock.so preauth
auth required pam_faillock.so authfail
account required pam_faillock.so

If the pam_faillock.so module is not present in the "/etc/pam.d/password-auth" file with the "preauth" line listed before pam_unix.so, this is a finding.

If the system administrator can demonstrate that the required configuration is contained in a Pluggable Authentication Module (PAM) configuration file included or substacked from the "system-auth" file, this is not a finding.
```

**Fix.**

```
Configure RHEL 10 to include the use of the pam_faillock.so module in the "/etc/pam.d/password-auth" file. If PAM is managed with "authselect", enable the feature with the following command:

$ sudo authselect enable-feature with-faillock

Otherwise, add/modify the appropriate sections of the "/etc/pam.d/password-auth" file to match the following lines:

Note: The "preauth" line must be listed before pam_unix.so.

auth required pam_faillock.so preauth
auth required pam_faillock.so authfail
account required pam_faillock.so
```

## V-281214 RHEL 10 must ensure the password complexity module is enabled in the "password-auth" file. {#V-281214}

Severity: medium · Rule: SV-281214r1166594_rule · STIG ID: RHEL-10-600620 · CCI-004066

**Discussion.** Enabling Pluggable Authentication Module (PAM) password complexity permits enforcement of strong passwords and consequently makes the system less prone to dictionary attacks.

Satisfies: SRG-OS-000069-GPOS-00037, SRG-OS-000070-GPOS-00038

**Check.**

```
Verify RHEL 10 uses "pwquality" to enforce the password complexity rules in the "password-auth" file with the following command:

$ sudo grep pam_pwquality /etc/pam.d/password-auth
password required pam_pwquality.so

If the command does not return a line containing the value "pam_pwquality.so", or the line is commented out, this is a finding.

If the system administrator can demonstrate that the required configuration is contained in a PAM configuration file included or substacked from the "system-auth" file, this is not a finding.
```

**Fix.**

```
Configure RHEL 10 to use "pwquality" to enforce password complexity rules.

Add the following line to the "/etc/pam.d/password-auth" file (or modify the line to have the required value):

password required pam_pwquality.so
```

## V-281215 RHEL 10 must ensure the password complexity module is enabled in the "system-auth" file. {#V-281215}

Severity: medium · Rule: SV-281215r1166597_rule · STIG ID: RHEL-10-600630 · CCI-004066

**Discussion.** Enabling Pluggable Authentication Module (PAM) password complexity permits enforcement of strong passwords and consequently makes the system less prone to dictionary attacks.

**Check.**

```
Verify RHEL 10 uses "pwquality" to enforce the password complexity rules in the "system-auth" file with the following command:

$ sudo grep pam_pwquality /etc/pam.d/system-auth
password required pam_pwquality.so

If the command does not return a line containing the value "pam_pwquality.so", or the line is commented out, this is a finding.

If the system administrator can demonstrate that the required configuration is contained in a PAM configuration file included or substacked from the "system-auth" file, this is not a finding.
```

**Fix.**

```
Configure RHEL 10 to use "pwquality" to enforce password complexity rules.

Add the following line to the "/etc/pam.d/system-auth" file (or modify the line to have the required value):

password required pam_pwquality.so
```

## V-281216 RHEL 10 must enable the Pluggable Authentication Module (PAM) interface for SSHD. {#V-281216}

Severity: high · Rule: SV-281216r1166600_rule · STIG ID: RHEL-10-600640 · CCI-000877

**Discussion.** When "UsePAM" is set to "yes", PAM runs through account and session types properly. This is important when restricted access to services based on IP, time, or other factors of the account is needed. Additionally, this ensures users can inherit certain environment variables on login or disallow access to the server.

**Check.**

```
Verify RHEL 10 SSHD is configured to allow for the "UsePAM" interface with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*usepam'
UsePAM yes

If the "UsePAM" keyword is set to "no", is missing, or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSHD to use the "UsePAM" interface by adding or modifying the following line in "/etc/ssh/sshd_config" or in a file in "/etc/ssh/sshd_config.d".

UsePAM yes

Restart the SSH daemon with the following command for the settings to take effect:

$ sudo systemctl restart sshd.service
```

## V-281217 RHEL 10 must ensure that the pam_unix.so module is configured in the password-auth file to use a FIPS 140-3-approved cryptographic hashing algorithm for system authentication. {#V-281217}

Severity: medium · Rule: SV-281217r1273593_rule · STIG ID: RHEL-10-600650 · CCI-004062 CCI-000803

**Discussion.** Unapproved mechanisms that are used for authentication to the cryptographic module are not verified; therefore, they cannot be relied on to provide confidentiality or integrity, and DoW data may be compromised.

RHEL 10 systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules.

FIPS 140-3 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DoW requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.

Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061

**Check.**

```
Verify RHEL 10 configures the pam_unix.so module to use sha512 in "/etc/pam.d/password-auth" with the following command:

$ sudo grep "^password.*pam_unix.so.*sha512" /etc/pam.d/password-auth
password sufficient pam_unix.so sha512

If "sha512" is missing, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use the sha512 cryptographic hashing algorithm for local account passwords.

Edit/modify the following line in the "/etc/pam.d/password-auth" file to include the sha512 option for pam_unix.so:

password sufficient pam_unix.so sha512
```

## V-281218 RHEL 10 must be configured to use a sufficient number of hashing rounds for the shadow password suite. {#V-281218}

Severity: medium · Rule: SV-281218r1166606_rule · STIG ID: RHEL-10-600700 · CCI-004062 CCI-000803

**Discussion.** Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text.

Using more hashing rounds makes password cracking attacks more difficult.

Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061

**Check.**

```
Verify RHEL 10 uses a sufficient number of rounds for the shadow password suite hashing algorithm with the following command:

$ sudo grep rounds /etc/pam.d/system-auth
password sufficient pam_unix.so sha512 rounds=100000

If the setting is not configured or "rounds" is less than 100000, this a finding.
```

**Fix.**

```
Configure RHEL 10 to use a sufficient number of hashing rounds for shadow password suite.

Add or modify the following line in "/etc/pam.d/system-auth" and set "rounds" to 100000:

password sufficient pam_unix.so sha512 rounds=100000
```

## V-281219 RHEL 10 must be configured to use a FIPS 140-3-approved cryptographic hashing algorithm for system authentication by ensuring that the pam_unix.so module is configured in the "system-auth" file. {#V-281219}

Severity: medium · Rule: SV-281219r1273594_rule · STIG ID: RHEL-10-600710 · CCI-004062 CCI-000803

**Discussion.** Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DoW data may be compromised.

RHEL 10 systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules.

FIPS 140-3 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DoW requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.

Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061

**Check.**

```
Verify RHEL 10 is configured to use a FIPS 140-3-approved cryptographic hashing algorithm in "/etc/pam.d/system-auth" via the pam_unix.so module with the following command:

$ sudo grep "^password.*pam_unix.so.*sha512" /etc/pam.d/system-auth
password sufficient pam_unix.so sha512

If "sha512" is missing, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use a FIPS 140-3-approved cryptographic hashing algorithm for system authentication in "/etc/pam.d/system-auth" via the "pam_unix.so" module.

Edit/modify the following line in the "/etc/pam.d/system-auth" file to include the sha512 option for pam_unix.so:

password sufficient pam_unix.so sha512
```

## V-281220 RHEL 10 must be configured so that password-auth uses a sufficient number of hashing rounds. {#V-281220}

Severity: medium · Rule: SV-281220r1166612_rule · STIG ID: RHEL-10-600720 · CCI-004062 CCI-000803

**Discussion.** Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text.

Using more hashing rounds makes password cracking attacks more difficult.

Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061

**Check.**

```
Verify RHEL 10 is configured to use a sufficient number of rounds for password hashing with the following command:

$ sudo grep rounds /etc/pam.d/password-auth
password sufficient pam_unix.so sha512 rounds=100000

If the setting is not configured or "rounds" is less than "100000", this a finding.
```

**Fix.**

```
Configure RHEL 10 to use "100000" hashing rounds for hashing passwords.

Add or modify the following line in "/etc/pam.d/password-auth" and set "rounds" to "100000":

password sufficient pam_unix.so sha512 rounds=100000
```

## V-281221 RHEL 10 must employ FIPS 140-3-approved cryptographic hashing algorithms for all stored passwords. {#V-281221}

Severity: high · Rule: SV-281221r1208797_rule · STIG ID: RHEL-10-600730 · CCI-004062 CCI-000803

**Discussion.** The system must use a strong hashing algorithm to store the password.

Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.

Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061

**Check.**

```
Verify RHEL 10 employs FIPS 140-3-approved cryptographic hashing algorithms for all stored passwords for interactive user accounts with the following command:

$ sudo cut -d: -f1,2 /etc/shadow
nsauser:$6$kcOnRq/5$NUEYPuyL.wghQwWssXRcLRFiiru7f5JPV6GaJhNC2aK5F3PZpE/BCCtwrxRc/AInKMNX3CdMw11m9STiql12f/

Password hashes "!" or "*" indicate inactive accounts not available for login and are not evaluated.

If any interactive user password hash does not begin with "$6", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to employ FIPS 140-3-approved cryptographic hashing algorithms for all stored passwords.

Lock all interactive user accounts not using SHA-512 hashing until the passwords can be regenerated with SHA-512.
```

## V-281222 RHEL 10 must be configured to use the shadow file to store only encrypted representations of passwords. {#V-281222}

Severity: high · Rule: SV-281222r1273622_rule · STIG ID: RHEL-10-600740 · CCI-004062

**Discussion.** Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text.

This setting ensures user and group account administration utilities are configured to store only encrypted representations of passwords. Additionally, the "crypt_style" configuration option ensures the use of a strong hashing algorithm that makes password cracking attacks more difficult.

The default for Red Hat 10 is yescrypt. Although yescrypt is structurally built using an outer layer of SHA-256 (which is a NIST-approved algorithm), the yescrypt algorithm as a whole is not recognized or validated by the National Institute of Standards and Technology (NIST) Cryptographic Module Validation Program (CMVP).

**Check.**

```
Verify RHEL 10 is configured so that the shadow file stores only encrypted representations of passwords with a hash value of SHA512 with the following command:

$ sudo grep -i encrypt_method /etc/login.defs
ENCRYPT_METHOD SHA512

If "ENCRYPT_METHOD" does not have a value of "SHA512", or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to store only SHA512 encrypted representations of passwords.

Add or update the following line in the "/etc/login.defs" file:

ENCRYPT_METHOD SHA512
```

## V-281223 RHEL 10 must be configured so that user and group account administration utilities are configured to store only encrypted representations of passwords. {#V-281223}

Severity: high · Rule: SV-281223r1273596_rule · STIG ID: RHEL-10-600750 · CCI-004062

**Discussion.** Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text.

This setting ensures user and group account administration utilities are configured to store only encrypted representations of passwords. Additionally, the "crypt_style" configuration option ensures the use of a strong hashing algorithm that makes password cracking attacks more difficult.

**Check.**

```
Note: If the libuser package is not installed, this requirement is not applicable.

Verify RHEL 10 user and group account administration utilities are configured to store only encrypted representations of passwords with the following command:

$ sudo grep -i "^crypt_style" /etc/libuser.conf
crypt_style = sha512

If the "crypt_style" variable is not set to "sha512", is not in the defaults section, is commented out, or does not exist, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use the SHA-512 algorithm for password hashing.

Add or change the following line in the "[defaults]" section of the "/etc/libuser.conf" file:

crypt_style = sha512
```

## V-281224 RHEL 10 must display the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a Secure Shell (SSH) login. {#V-281224}

Severity: medium · Rule: SV-281224r1273597_rule · STIG ID: RHEL-10-700010 · CCI-000213

**Discussion.** The warning message reinforces policy awareness during the login process and facilitates possible legal action against attackers. Alternatively, systems whose ownership should not be obvious should ensure use of a banner that does not provide easy attribution.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 is configured so that any SSH connection to the operating system displays the Standard Mandatory DoW Notice and Consent Banner before granting access to the system.

Check for the location of the banner file currently being used with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*banner'
/etc/ssh/sshd_config.d/10-stig.conf:Banner /etc/issue

If the line is commented out or the file is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to display the Standard Mandatory DoW Notice and Consent Banner before granting access to the system via SSH.

Edit a file in "/etc/ssh/sshd_config.d" to uncomment or add the banner keyword and configure it to point to a file that will contain the login banner (this file may be named differently or be in a different location if using a version of SSH that is provided by a third-party vendor).

An example configuration line is:

Banner /etc/issue
```

## V-281225 RHEL 10 must display the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a graphical user login. {#V-281225}

Severity: medium · Rule: SV-281225r1273598_rule · STIG ID: RHEL-10-700020 · CCI-000048 CCI-001384 CCI-001385 CCI-001386 CCI-001387 CCI-001388

**Discussion.** Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.

System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist.

The banner must be formatted in accordance with applicable DoW policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters:

"You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.

By using this IS (which includes any device attached to this IS), you consent to the following conditions:

-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.

-At any time, the USG may inspect and seize data stored on this IS.

-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.

-This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.

-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."

Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 displays the Standard Mandatory DoW Notice and Consent Banner before granting access to the operating system via a graphical user login with the following command:

$ gsettings get org.gnome.login-screen banner-message-text
banner-message-text=
'You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.\nBy using this IS (which includes any device attached to this IS), you consent to the following conditions:\n-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.\n-At any time, the USG may inspect and seize data stored on this IS.\n-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.\n-This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.\n-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. '

Note: The "\n " characters are for formatting only. They will not be displayed on the graphical interface.

If the banner does not match the Standard Mandatory DoW Notice and Consent Banner exactly, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to display the Standard Mandatory DoW Notice and Consent Banner before granting access to the system.

Add the following lines to the [org/gnome/login-screen] section of the "/etc/dconf/db/local.d/01-banner-message":

banner-message-text='You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.\nBy using this IS (which includes any device attached to this IS), you consent to the following conditions:\n-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.\n-At any time, the USG may inspect and seize data stored on this IS.\n-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.\n-This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.\n-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. '

Note: The "\n " characters are for formatting only. They will not be displayed on the graphical interface.

Run the following command to update the database:

$ sudo dconf update
```

## V-281226 RHEL 10 must prevent a user from overriding the banner-message-enable setting for the graphical user interface. {#V-281226}

Severity: medium · Rule: SV-281226r1268215_rule · STIG ID: RHEL-10-700030 · CCI-000048 CCI-001384 CCI-001385 CCI-001386 CCI-001387 CCI-001388

**Discussion.** Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.

For U.S. Government systems, system use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist.

Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 prevents a user from overriding settings for graphical user interfaces with the following command:

$ gsettings writable org.gnome.login-screen banner-message-enable
false

If "banner-message-enable" is writable, or the result is "true", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent a user from overriding the banner setting for graphical user interfaces.

Create a database to contain the systemwide graphical user login settings (if it does not already exist) with the following command:

$ sudo vi /etc/dconf/db/local.d/locks/session

Add the following setting to prevent nonprivileged users from modifying it:

/org/gnome/login-screen/banner-message-enable

Run the following command to update the database:

$ sudo dconf update
```

## V-281227 RHEL 10 must display the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a command line user login. {#V-281227}

Severity: medium · Rule: SV-281227r1273599_rule · STIG ID: RHEL-10-700040 · CCI-000048 CCI-001384 CCI-001385 CCI-001386 CCI-001387 CCI-001388

**Discussion.** Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.

System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist.

Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088

**Check.**

```
Verify RHEL 10 displays the Standard Mandatory DoW Notice and Consent Banner before granting access to the operating system via a command line login screen with the following command:

$ cat /etc/issue

If the banner is set correctly, it will return the following text:

"You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.

By using this IS (which includes any device attached to this IS), you consent to the following conditions:

-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.

-At any time, the USG may inspect and seize data stored on this IS.

-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.

-This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.

-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."

If the banner text does not match the Standard Mandatory DoW Notice and Consent Banner exactly, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to display the Standard Mandatory DoW Notice and Consent Banner before granting access to the system via command line login.

Edit the "/etc/issue" file to replace the default text with the Standard Mandatory DoW Notice and Consent Banner. The DoW-required text is:

"You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.

By using this IS (which includes any device attached to this IS), you consent to the following conditions:

-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.

-At any time, the USG may inspect and seize data stored on this IS.

-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.

-This IS includes security measures (e.g., authentication and access controls) to protect USG interests -- not for your personal benefit or privacy.

-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."
```

## V-281228 RHEL 10 must prevent special devices on file systems that are imported via Network File System (NFS). {#V-281228}

Severity: medium · Rule: SV-281228r1268226_rule · STIG ID: RHEL-10-700100 · CCI-000213

**Discussion.** The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Note: If no NFS mounts are configured, this requirement is not applicable.

Verify RHEL 10 has the "nodev" option configured for all NFS mounts with the following command:

$ sudo grep nfs /etc/fstab
192.168.22.2:/mnt/export /data nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5:krb5i:krb5p

If the system is mounting file systems via NFS and the "nodev" option is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent special devices on file systems that are imported via NFS.

Update each NFS mounted file system to use the "nodev" option on file systems that are being imported via NFS.
```

## V-281229 RHEL 10 must prevent code from being executed on file systems that are imported via Network File System (NFS). {#V-281229}

Severity: medium · Rule: SV-281229r1268226_rule · STIG ID: RHEL-10-700105 · CCI-000213

**Discussion.** The "noexec" mount option causes the system not to execute binary files. This option must be used for mounting any file system not containing approved binary as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Note: If no NFS mounts are configured, this requirement is not applicable.

Verify RHEL 10 has the "noexec" option configured for all NFS mounts with the following command:

$ sudo grep nfs /etc/fstab
192.168.22.2:/mnt/export /data nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5:krb5i:krb5p

If the system is mounting file systems via NFS and the "noexec" option is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent code from being executed on file systems that are imported via NFS.

Update each NFS mounted file system to use the "noexec" option on file systems that are being imported via NFS.
```

## V-281230 RHEL 10 must prevent files with the "setuid" and "setgid" bit set from being executed on file systems that are imported via Network File System (NFS). {#V-281230}

Severity: medium · Rule: SV-281230r1268226_rule · STIG ID: RHEL-10-700110 · CCI-000213

**Discussion.** The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Note: If no NFS mounts are configured, this requirement is not applicable.

Verify RHEL 10 has the "nosuid" option configured for all NFS mounts with the following command:

$ sudo grep nfs /etc/fstab
192.168.22.2:/mnt/export /data nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5:krb5i:krb5p

If the system is mounting file systems via NFS and the "nosuid" option is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent files with the "setuid" and "setgid" bit set from being executed on file systems that are imported via NFS.

Update each NFS mounted file system to use the "nosuid" option on file systems that are being imported via NFS.
```

## V-281231 RHEL 10 must be configured so that the Network File System (NFS) is configured to use RPCSEC_GSS. {#V-281231}

Severity: medium · Rule: SV-281231r1268226_rule · STIG ID: RHEL-10-700115 · CCI-000213

**Discussion.** When an NFS server is configured to use RPCSEC_SYS, a selected userid and groupid are used to handle requests from the remote user. The userid and groupid could mistakenly or maliciously be set incorrectly. The RPCSEC_GSS method of authentication uses certificates on the server and client systems to more securely authenticate the remote mount request.

**Check.**

```
Note: If no NFS mounts are configured, this requirement is not applicable.

Verify RHEL 10 has the "sec" option configured for all NFS mounts with the following command:

$ sudo grep nfs /etc/fstab
192.168.22.2:/mnt/export /data nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5p:krb5i:krb5

If the system is mounting file systems via NFS and has the sec option without the "krb5:krb5i:krb5p" settings, the "sec" option has the "sys" setting, or the "sec" option is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the "/etc/fstab" file "sec" option is defined for each NFS mounted file system, and the "sec" option does not have the "sys" setting.

Ensure the "sec" option is defined as "krb5p:krb5i:krb5".
```

## V-281232 RHEL 10 must mount "/boot" with the "nodev" option. {#V-281232}

Severity: medium · Rule: SV-281232r1166648_rule · STIG ID: RHEL-10-700120 · CCI-001764

**Discussion.** The only legitimate location for device files is the "/dev" directory located on the root partition. The only exception to this is chroot jails.

**Check.**

```
Verify RHEL 10 is configured so that the "/boot" mount point has the "nodev" option with the following command:

$ mount | grep '\s/boot\s'
/dev/sda1 on /boot type xfs (rw,nodev,nosuid,relatime,seclabel,attr2)

If the "/boot" file system does not have the "nodev" option set, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/boot" with the "nodev" option.

Modify "/etc/fstab" to use the "nodev" option on the "/boot" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /boot
```

## V-281233 RHEL 10 must prevent files with the "setuid" and "setgid" bit set from being executed on the "/boot" directory. {#V-281233}

Severity: medium · Rule: SV-281233r1166651_rule · STIG ID: RHEL-10-700125 · CCI-001764

**Discussion.** The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that the "/boot" directory is mounted with the "nosuid" option with the following command:

$ mount | grep '\s/boot\s'
/dev/sda1 on /boot type xfs (rw,nodev,nosuid,relatime,seclabel,attr2)

If the "/boot" file system does not have the "nosuid" option set, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent files with the "setuid" and "setgid" bit set from being executed on the "/boot" directory.

Modify "/etc/fstab" to use the "nosuid" option on the "/boot" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /boot
```

## V-281234 RHEL 10 must prevent files with the "setuid" and "setgid" bit set from being executed on the "/boot/efi" directory. {#V-281234}

Severity: medium · Rule: SV-281234r1268226_rule · STIG ID: RHEL-10-700130 · CCI-000213

**Discussion.** The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Note: For systems that use BIOS and for vfat systems, this requirement is not applicable.

Verify RHEL 10 is configured so that the "/boot/efi "directory is mounted with the "nosuid" option with the following command:

$ mount | grep '\s/boot/efi\s'
/dev/sda1 on /boot/efi type vfat (rw,nosuid,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=winnt,errors=remount-ro)

If the "/boot/efi" file system does not have the "nosuid" option set, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent files with the "setuid" and "setgid" bit set from being executed on the "/boot/efi" directory.

Modify "/etc/fstab" to use the "nosuid" option on the "/boot/efi" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /boot/efi
```

## V-281235 RHEL 10 must mount "/dev/shm" with the "nodev" option. {#V-281235}

Severity: medium · Rule: SV-281235r1166657_rule · STIG ID: RHEL-10-700135 · CCI-001764

**Discussion.** The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.

**Check.**

```
Verify RHEL 10 is configured so that "/dev/shm" is mounted with the "nodev" option with the following command:

$ mount | grep /dev/shm
tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel)

If the "/dev/shm" file system is mounted without the "nodev" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/dev/shm" with the "nodev" option.

Modify "/etc/fstab" to use the "nodev" option on the "/dev/shm" file system.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /dev/shm
```

## V-281236 RHEL 10 must mount "/dev/shm" with the "noexec" option. {#V-281236}

Severity: medium · Rule: SV-281236r1166660_rule · STIG ID: RHEL-10-700140 · CCI-001764

**Discussion.** The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/dev/shm" is mounted with the "noexec" option with the following command:

$ mount | grep /dev/shm
tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel)

If the "/dev/shm" file system is mounted without the "noexec" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/dev/shm" with the "noexec" option.

Modify "/etc/fstab" to use the "noexec" option on the "/dev/shm" file system.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /dev/shm
```

## V-281237 RHEL 10 must mount "/dev/shm" with the "nosuid" option. {#V-281237}

Severity: medium · Rule: SV-281237r1166663_rule · STIG ID: RHEL-10-700145 · CCI-001764

**Discussion.** The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/dev/shm" is mounted with the "nosuid" option with the following command:

$ mount | grep /dev/shm
tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel)

If the "/dev/shm" file system is mounted without the "nosuid" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/dev/shm" with the "nosuid" option.

Modify "/etc/fstab" to use the "nosuid" option on the "/dev/shm" file system.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /dev/shm
```

## V-281238 RHEL 10 must mount "/tmp" with the "nodev" option. {#V-281238}

Severity: medium · Rule: SV-281238r1166666_rule · STIG ID: RHEL-10-700150 · CCI-001764

**Discussion.** The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.

**Check.**

```
Verify RHEL 10 is configured so that "/tmp" is mounted with the "nodev" option:

$ mount | grep /tmp
/dev/mapper/luks-c98555c8-0462-4b97-9afa-6db8c4bfee3b on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)

If the "/tmp" file system is mounted without the "nodev" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/tmp" with the "nodev" option.

Modify "/etc/fstab" to use the "nodev" option on the "/tmp" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /tmp
```

## V-281239 RHEL 10 must mount "/tmp" with the "noexec" option. {#V-281239}

Severity: medium · Rule: SV-281239r1166669_rule · STIG ID: RHEL-10-700155 · CCI-001764

**Discussion.** The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/tmp" is mounted with the "noexec" option:

$ mount | grep /tmp
/dev/mapper/luks-c98555c8-0462-4b97-9afa-6db8c4bfee3b on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)

If the "/tmp" file system is mounted without the "noexec" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/tmp" with the "noexec" option.

Modify "/etc/fstab" to use the "noexec" option on the "/tmp" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /tmp
```

## V-281240 RHEL 10 must mount "/tmp" with the "nosuid" option. {#V-281240}

Severity: medium · Rule: SV-281240r1166672_rule · STIG ID: RHEL-10-700160 · CCI-001764

**Discussion.** The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/tmp" is mounted with the "nosuid" option:

$ mount | grep /tmp
/dev/mapper/luks-c98555c8-0462-4b97-9afa-6db8c4bfee3b on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)

If the "/tmp" file system is mounted without the "nosuid" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/tmp" with the "nosuid" option.

Modify "/etc/fstab" to use the "nosuid" option on the "/tmp" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /tmp
```

## V-281241 RHEL 10 must mount "/var" with the "nodev" option. {#V-281241}

Severity: medium · Rule: SV-281241r1166675_rule · STIG ID: RHEL-10-700165 · CCI-001764

**Discussion.** The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.

**Check.**

```
Verify RHEL 10 is configured so that "/var" is mounted with the "nodev" option:

$ mount | grep /var
/dev/mapper/luks-51150299-f295-4145-b8f0-ebe9c6dfd5a0 on /var type xfs (rw,nodev,relatime,seclabel,attr2)

If the "/var" file system is mounted without the "nodev" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/var" with the "nodev" option.

Modify "/etc/fstab" to use the "nodev" option on the "/var" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /var
```

## V-281242 RHEL 10 must mount "/var/log" with the "nodev" option. {#V-281242}

Severity: medium · Rule: SV-281242r1166678_rule · STIG ID: RHEL-10-700170 · CCI-001764

**Discussion.** The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.

**Check.**

```
Verify RHEL 10 is configured so that "/var/log" is mounted with the "nodev" option:

$ mount | grep /var/log
/dev/mapper/luks-c651f493-9fdc-4c6e-a711-0a4f03149661 on /var/log type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)

If the "/var/log" file system is mounted without the "nodev" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/var/log" with the "nodev" option.

Modify "/etc/fstab" to use the "nodev" option on the "/var/log" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /var/log
```

## V-281243 RHEL 10 must mount "/var/log" with the "noexec" option. {#V-281243}

Severity: medium · Rule: SV-281243r1166681_rule · STIG ID: RHEL-10-700175 · CCI-001764

**Discussion.** The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/var/log" is mounted with the "noexec" option:

$ mount | grep /var/log
/dev/mapper/luks-c651f493-9fdc-4c6e-a711-0a4f03149661 on /var/log type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)

If the "/var/log" file system is mounted without the "noexec" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/var/log" with the "noexec" option.

Modify "/etc/fstab" to use the "noexec" option on the "/var/log" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /var/log
```

## V-281244 RHEL 10 must mount "/var/log" with the "nosuid" option. {#V-281244}

Severity: medium · Rule: SV-281244r1166684_rule · STIG ID: RHEL-10-700180 · CCI-001764

**Discussion.** The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/var/log" is mounted with the "nosuid" option:

$ mount | grep /var/log
/dev/mapper/luks-c651f493-9fdc-4c6e-a711-0a4f03149661 on /var/log type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)

If the "/var/log" file system is mounted without the "nosuid" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/var/log" with the "nosuid" option.

Modify "/etc/fstab" to use the "nosuid" option on the "/var/log" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /var/log
```

## V-281245 RHEL 10 must mount "/var/tmp" with the "nodev" option. {#V-281245}

Severity: medium · Rule: SV-281245r1166687_rule · STIG ID: RHEL-10-700185 · CCI-001764

**Discussion.** The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.

**Check.**

```
Verify RHEL 10 is configured so that "/var/tmp" is mounted with the "nodev" option:

$ mount | grep /var/tmp
/dev/mapper/luks-c98555c8-0462-4b97-9afa-6db8c4bfee3b on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)

If the "/var/tmp" file system is mounted without the "nodev" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/var/tmp" with the "nodev" option.

Modify "/etc/fstab" to use the "nodev" option on the "/var/tmp" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /var/tmp
```

## V-281246 RHEL 10 must mount "/var/tmp" with the "noexec" option. {#V-281246}

Severity: medium · Rule: SV-281246r1166690_rule · STIG ID: RHEL-10-700190 · CCI-001764

**Discussion.** The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/var/tmp" is mounted with the "noexec" option:

$ mount | grep /var/tmp
/dev/mapper/luks-c98555c8-0462-4b97-9afa-6db8c4bfee3b on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)

If the "/var/tmp" file system is mounted without the "noexec" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/var/tmp" with the "noexec" option.

Modify "/etc/fstab" to use the "noexec" option on the "/var/tmp" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /var/tmp
```

## V-281247 RHEL 10 must mount "/var/tmp" with the "nosuid" option. {#V-281247}

Severity: medium · Rule: SV-281247r1166693_rule · STIG ID: RHEL-10-700195 · CCI-001764

**Discussion.** The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

**Check.**

```
Verify RHEL 10 is configured so that "/var/tmp" is mounted with the "nosuid" option:

$ mount | grep /var/tmp
/dev/mapper/luks-c98555c8-0462-4b97-9afa-6db8c4bfee3b on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2)

If the "/var/tmp" file system is mounted without the "nosuid" option, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to mount "/var/tmp" with the "nosuid" option.

Modify "/etc/fstab" to use the "nosuid" option on the "/var/tmp" directory.

To reload all implicit mount units and update the dependency graph so that new options will apply correctly at next remount, run the following command:

$ sudo systemctl daemon-reload

Use the following command to apply the changes immediately without a reboot:

$ sudo mount -o remount /var/tmp
```

## V-281248 RHEL 10 must prevent special devices on nonroot local partitions. {#V-281248}

Severity: medium · Rule: SV-281248r1166696_rule · STIG ID: RHEL-10-700200 · CCI-001764

**Discussion.** The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.

The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.

**Check.**

```
Verify RHEL 10 is configured so that all nonroot local partitions are mounted with the "nodev" option with the following command:

$ sudo mount | grep '^/dev\S* on /\S' | grep --invert-match 'nodev'

If any output is produced, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that "/etc/fstab" uses the "nodev" option on all nonroot local partitions.
```

## V-281249 RHEL 10 must enable the SELinux targeted policy. {#V-281249}

Severity: medium · Rule: SV-281249r1197242_rule · STIG ID: RHEL-10-700400 · CCI-002696

**Discussion.** Setting the SELinux policy to "targeted" or a more specialized policy ensures the system will confine processes that are likely to be targeted for exploitation, such as network or system services.

Note: During the development or debugging of SELinux modules, it is common to temporarily place nonproduction systems in "permissive" mode. In such temporary cases, SELinux policies should be developed, and once work is completed, the system should be reconfigured to "targeted".

**Check.**

```
Verify RHEL 10 SELINUX is using the targeted policy with the following command:

$ sestatus | grep policy
Loaded policy name:             targeted

If the loaded policy name is not "targeted", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use the targeted SELINUX policy.

Edit the file "/etc/selinux/config" and add or modify the following line:

SELINUXTYPE=targeted

A reboot is required for the changes to take effect.
```

## V-281250 RHEL 10 must elevate the SELinux context when an administrator calls the sudo command. {#V-281250}

Severity: medium · Rule: SV-281250r1184704_rule · STIG ID: RHEL-10-700410 · CCI-002235

**Discussion.** Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. 

Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters.

This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality.

Preventing nonprivileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges.

Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Nonprivileged users are individuals who do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from nonprivileged users.

**Check.**

```
Verify RHEL 10 elevates the SELinux context when an administrator calls the sudo command with the following command:

This command must be run as root:

$ sudo grep -r sysadm_r /etc/sudoers /etc/sudoers.d
%{designated_group_or_user_name} ALL=(ALL) TYPE=sysadm_t ROLE=sysadm_r ALL

If a designated sudoers administrator group or account(s) is not configured to elevate the SELinux type and role to "sysadm_t" and "sysadm_r" with the use of the sudo command, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to elevate the SELinux context when an administrator calls the sudo command.

Edit a file in the "/etc/sudoers.d" directory with the following command:

$ sudo visudo -f /etc/sudoers.d/ 

Use the following example to build the file in the "/etc/sudoers.d" directory to allow any administrator belonging to a designated sudoers admin group to elevate their SELinux context with the use of the sudo command:

%{designated_group_or_user_name} ALL=(ALL) TYPE=sysadm_t ROLE=sysadm_r ALL

Remove any configurations that conflict with the above from the following locations:

/etc/sudoers
/etc/sudoers.d/
```

## V-281251 RHEL 10 must use a Linux Security Module configured to enforce limits on system services. {#V-281251}

Severity: medium · Rule: SV-281251r1166705_rule · STIG ID: RHEL-10-700420 · CCI-002696 CCI-001084

**Discussion.** Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. 

Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters.

This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality.

Satisfies: SRG-OS-000445-GPOS-00199, SRG-OS-000134-GPOS-00068

**Check.**

```
Verify RHEL 10 enforces correct operation of security functions through the use of SELinux with the following command:

$ getenforce
Enforcing

If SELINUX is not set to "Enforcing", this is a finding.

Verify SELinux is configured to be enforcing at boot.

$ sudo grep "SELINUX=" /etc/selinux/config | grep -v '#'
SELINUX=enforcing

If an uncommented SELinux line is missing or not set to "enforcing", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enforce correct operation of security functions.

Edit the file "/etc/selinux/config" and add or modify the following line:

 SELINUX=enforcing

A reboot is required for the changes to take effect.
```

## V-281252 RHEL 10 must configure SELinux context type to allow the use of a nondefault faillock tally directory. {#V-281252}

Severity: medium · Rule: SV-281252r1166708_rule · STIG ID: RHEL-10-700430 · CCI-000044

**Discussion.** Not having the correct SELinux context on the faillock directory may lead to unauthorized access to the directory.

**Check.**

```
Note: If the system does not have SELinux enabled and enforcing a targeted policy, or if the pam_faillock module is not configured for use, this requirement is not applicable.

Verify RHEL 10 SELinux context type allows the use of a nondefault faillock tally directory.

Verify the location of the nondefault tally directory for the pam_faillock module with the following command:

$ sudo grep -w dir /etc/security/faillock.conf
dir = /var/log/faillock

Check the security context type of the nondefault tally directory with the following command:

$ ls -Zd /var/log/faillock
unconfined_u:object_r:faillog_t:s0 /var/log/faillock

If the security context type of the nondefault tally directory is not "faillog_t", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to allow the use of a nondefault faillock tally directory while SELinux enforces a targeted policy.

Enable the feature using the following command:

$ sudo authselect enable-feature with-faillock

Create a nondefault faillock tally directory (if it does not already exist) with the following example:

$ sudo mkdir /var/log/faillock

Add/modify the "/etc/security/faillock.conf" file to match the following line:

dir = /var/log/faillock

Update "/etc/selinux/targeted/contexts/files/file_contexts.local" with "faillog_t" context type for the nondefault faillock tally directory with the following command:

$ sudo semanage fcontext -a -t faillog_t "/var/log/faillock(/.*)?"

Update the context type of the nondefault faillock directory/subdirectories and files with the following command:

$ sudo restorecon -R -v /var/log/faillock
```

## V-281253 RHEL 10 must be configured so that Secure Shell (SSH) public host key files have mode "0644" or less permissive. {#V-281253}

Severity: medium · Rule: SV-281253r1184654_rule · STIG ID: RHEL-10-700500 · CCI-002696

**Discussion.** If a public host key file is modified by an unauthorized user, the SSH service may be compromised.

**Check.**

```
Verify RHEL 10 SSH public host key files have a mode of "0644" or less permissive with the following command:

Note: SSH public key files may be found in other directories on the system depending on the installation.

$ sudo stat -c "%a %n" /etc/ssh/*.pub
644 /etc/ssh/ssh_host_dsa_key.pub
644 /etc/ssh/ssh_host_ecdsa_key.pub
644 /etc/ssh/ssh_host_ed25519_key.pub
644 /etc/ssh/ssh_host_rsa_key.pub

If any "key.pub" file has a mode more permissive than "0644", this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH public host key files to have mode "0644" or less permissive.

Change the mode of public host key files under "/etc/ssh" to "0644" with the following command:

$ sudo chmod 0644 /etc/ssh/*key.pub

Restart the SSH daemon with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281254 RHEL 10 must be configured so that the Secure Shell (SSH) daemon does not allow Generic Security Service Application Program Interface (GSSAPI) authentication. {#V-281254}

Severity: medium · Rule: SV-281254r1184754_rule · STIG ID: RHEL-10-700510 · CCI-001813

**Discussion.** GSSAPI authentication is used to provide additional authentication mechanisms to applications. Allowing GSSAPI authentication through SSH exposes the system's GSSAPI to remote hosts, increasing the attack surface of the system.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 SSH daemons do not allow GSSAPI authentication with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*gssapiauthentication'
/etc/ssh/sshd_config.d/10-stig.conf:GSSAPIAuthentication no
/etc/ssh/sshd_config.d/50-redhat.conf:GSSAPIAuthentication yes

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i gssapiauthentication
gssapiauthentication no

If the "GSSAPIAuthentication" keyword is not set to "no" in a drop-in that lexicographically precedes 50-redhat.conf, no output is returned, and the use of GSSAPI authentication has not been documented with the information system security officer, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH daemons to not allow GSSAPI authentication.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

GSSAPIAuthentication no

Restart the SSH service with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281255 RHEL 10 must be configured so that the Secure Shell (SSH) daemon does not allow Kerberos authentication. {#V-281255}

Severity: medium · Rule: SV-281255r1184755_rule · STIG ID: RHEL-10-700520 · CCI-001813

**Discussion.** Kerberos authentication for SSH is often implemented using Generic Security Service Application Program Interface (GSSAPI). If Kerberos is enabled through SSH, the SSH daemon provides a means of access to the system's Kerberos implementation. Vulnerabilities in the system's Kerberos implementations may be subject to exploitation.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 SSH daemons do not allow Kerberos authentication with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*kerberosauthentication'
/etc/ssh/sshd_config.d/10-stig.conf:KerberosAuthentication no

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i kerberosauthentication
kerberosauthentication no

If the "KerberosAuthentication" keyword is not set to "no" in a drop-in that lexicographically precedes 50-redhat.conf, no output is returned, and the use of Kerberos authentication has not been documented with the information system security officer, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH daemons to not allow Kerberos authentication.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

KerberosAuthentication no

Restart the SSH service with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281256 RHEL 10 must be configured so that the Secure Shell (SSH) daemon does not allow rhosts authentication. {#V-281256}

Severity: medium · Rule: SV-281256r1184756_rule · STIG ID: RHEL-10-700530 · CCI-002696

**Discussion.** SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 SSH daemons do not allow rhosts authentication with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*ignorerhosts'
/etc/ssh/sshd_config.d/10-stig.conf:IgnoreRhosts yes

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i ignorerhosts
ignorerhosts yes

If the "IgnoreRhosts" keyword is not set to "yes" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH daemons to not allow rhosts authentication.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

IgnoreRhosts yes

Restart the SSH service with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281257 RHEL 10 must be configured so that the Secure Shell (SSH) daemon does not allow known hosts authentication. {#V-281257}

Severity: medium · Rule: SV-281257r1184757_rule · STIG ID: RHEL-10-700540 · CCI-002696

**Discussion.** Configuring the "IgnoreUserKnownHosts" setting for the SSH daemon provides additional assurance that remote login via SSH will require a password, even in the event of misconfiguration elsewhere.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 SSH daemons do not allow known hosts authentication with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*ignoreuserknownhosts'
/etc/ssh/sshd_config.d/10-stig.conf:IgnoreUserKnownHosts yes

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i ignoreuserknownhosts
ignoreuserknownhosts yes

If the "IgnoreUserKnownHosts" keyword is not set to "yes" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH daemons to not allow known hosts authentication.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

IgnoreUserKnownHosts yes

Restart the SSH service with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281258 RHEL 10 must be configured so that the Secure Shell (SSH) daemon disables remote X connections for interactive users. {#V-281258}

Severity: medium · Rule: SV-281258r1184758_rule · STIG ID: RHEL-10-700550 · CCI-002696

**Discussion.** When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the sshd proxy display is configured to listen on the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the DISPLAY environment variable to localhost. This prevents remote hosts from connecting to the proxy display.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 SSH daemons do not allow X11Forwarding with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*x11forwarding'
/etc/ssh/sshd_config.d/10-stig.conf:X11forwarding no
/etc/ssh/sshd_config.d/50-redhat.conf:X11Forwarding yes

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i x11forwarding
x11forwarding no

If the "X11forwarding" keyword is not set to "no" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, and X11 forwarding is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH daemons to not allow X11 forwarding.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

X11forwarding no

Restart the SSH service with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281259 RHEL 10 must be configured so that the Secure Shell (SSH) daemon performs strict mode checking of home directory configuration files. {#V-281259}

Severity: medium · Rule: SV-281259r1184759_rule · STIG ID: RHEL-10-700560 · CCI-002696

**Discussion.** If other users have access to modify user-specific SSH configuration files, they may be able to log in to the system as another user.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 SSH daemons perform strict mode checking of home directory configuration files with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*strictmodes'
/etc/ssh/sshd_config.d/10-stig.conf:StrictModes yes

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i strictmodes
strictmodes yes

If the "StrictModes" keyword is not set to "yes" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH daemons to perform strict mode checking of home directory configuration files.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

StrictModes yes

Restart the SSH service with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281260 RHEL 10 must be configured so that the Secure Shell (SSH) daemon displays the date and time of the last successful account login upon an SSH login. {#V-281260}

Severity: medium · Rule: SV-281260r1184760_rule · STIG ID: RHEL-10-700570 · CCI-002696

**Discussion.** Providing users with feedback on when account accesses last occurred facilitates user recognition and reporting of unauthorized account use.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 SSH daemons provide users with feedback on when account accesses last occurred with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*printlastlog'
/etc/ssh/sshd_config.d/10-stig.conf:PrintLastLog yes

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i printlastlog
printlastlog yes

If the "PrintLastLog" keyword is not set to "yes" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH daemons to provide users with feedback on when account accesses last occurred.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

PrintLastLog yes

Restart the SSH service with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281261 RHEL 10 must be configured so that the Secure Shell (SSH) daemon prevents remote hosts from connecting to the proxy display. {#V-281261}

Severity: medium · Rule: SV-281261r1184761_rule · STIG ID: RHEL-10-700580 · CCI-002696

**Discussion.** When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the sshd proxy display is configured to listen on the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the "DISPLAY" environment variable to localhost. This prevents remote hosts from connecting to the proxy display.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 SSH daemons prevent remote hosts from connecting to the proxy display with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*x11uselocalhost'
/etc/ssh/sshd_config.d/10-stig.conf:X11UseLocalhost yes

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i x11uselocalhost
x11uselocalhost yes

If the "X11UseLocalhost" keyword is not set to "yes" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSH daemons to prevent remote hosts from connecting to the proxy display.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

X11UseLocalhost yes

Restart the SSH service with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281262 RHEL 10 must be configured so that Secure Shell (SSH) server configuration files' permissions are not modified. {#V-281262}

Severity: medium · Rule: SV-281262r1268226_rule · STIG ID: RHEL-10-700590 · CCI-000213

**Discussion.** Service configuration files enable or disable features of their respective services, which if configured incorrectly can lead to insecure and vulnerable configurations. Therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 is configured so that SSH server configuration files' permissions are not modified.

Check the permissions of the "/etc/ssh/sshd_config" file with the following command:

$ sudo rpm --verify openssh-server | awk '! ($2 == "c" && $1 ~ /^.\..\.\.\.\..\./) {print $0}'

If the command returns any output, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that SSH server configuration files' permissions are not modified.

Run the following commands to restore the correct permissions of OpenSSH server configuration files:

$ sudo rpm --setugids openssh-server
$ sudo rpm --setperms openssh-server
```

## V-281263 RHEL 10 must be configured so that SSHD accepts public key authentication. {#V-281263}

Severity: medium · Rule: SV-281263r1273600_rule · STIG ID: RHEL-10-700600 · CCI-000765 CCI-000766

**Discussion.** Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. A privileged account is defined as an information system account with authorizations of a privileged user. A DoW common access card (CAC) with DoW-approved PKI is an example of multifactor authentication.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055

**Check.**

```
Note: If the system administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable.

Verify RHEL 10 SSH daemons accept public key encryption with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*pubkeyauthentication'
/etc/ssh/sshd_config.d/10-stig.conf:PubkeyAuthentication yes

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i pubkeyauthentication
pubkeyauthentication yes

If the "PubkeyAuthentication" keyword is not set to "yes" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to accept public key authentication.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

PubkeyAuthentication yes

Restart the SSH daemon with the following command for the settings to take effect:

$ sudo systemctl restart sshd.service
```

## V-281264 RHEL 10 must be configured so that SSHD does not allow blank passwords. {#V-281264}

Severity: medium · Rule: SV-281264r1268229_rule · STIG ID: RHEL-10-700610 · CCI-000766

**Discussion.** If an account has an empty password, anyone could log in and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

Satisfies: SRG-OS-000106-GPOS-00053, SRG-OS-000480-GPOS-00229

**Check.**

```
Verify RHEL 10 remote access using SSH prevents logging on with a blank password with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*permitemptypasswords'
/etc/ssh/sshd_config.d/10-stig.conf:PermitEmptyPasswords no

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i permitemptypasswords
permitemptypasswords no

If the "PermitEmptyPasswords" keyword is not set to "no" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent SSH users from logging on with blank passwords. 

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

PermitEmptyPasswords no

Restart the SSH daemon with the following command for the settings to take effect:

$ sudo systemctl restart sshd.service
```

## V-281265 RHEL 10 must not permit direct logins to the root account using remote access via Secure Shell (SSH). {#V-281265}

Severity: medium · Rule: SV-281265r1184765_rule · STIG ID: RHEL-10-700620 · CCI-004045

**Discussion.** Even though the communications channel may be encrypted, an additional layer of security is gained by extending the policy of not logging directly on as root. In addition, logging in with a user-specific account provides individual accountability of actions performed on the system and helps to minimize direct attack attempts on root's password.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 remote access using SSH prevents users from logging on directly as "root" with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*permitrootlogin'
/etc/ssh/sshd_config.d/10-stig.conf:PermitRootLogin no

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i permitrootlogin
permitrootlogin no

If the "PermitRootLogin" keyword is not set to "no" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent SSH users from logging on directly as root.

In "/etc/ssh/sshd_config.d", create a drop-in file that will lexicographically precede 50-redhat.conf and add the following line:

PermitRootLogin no

Restart the SSH daemon with the following command for the settings to take effect:

$ sudo systemctl restart sshd.service
```

## V-281266 RHEL 10 must not allow a noncertificate trusted host Secure Shell (SSH) login to the system. {#V-281266}

Severity: medium · Rule: SV-281266r1268226_rule · STIG ID: RHEL-10-700630 · CCI-000213

**Discussion.** SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 does not allow a noncertificate trusted host SSH login to the system with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*hostbasedauthentication'
/etc/ssh/sshd_config.d/10-stig.conf:HostbasedAuthentication no

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i hostbasedauthentication
hostbasedauthentication no

If the "HostbasedAuthentication" keyword is not set to "no" in a drop-in that lexicographically precedes 50-redhat.conf, or no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not allow a noncertificate trusted host SSH login to the system.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

HostbasedAuthentication no

Restart the SSH daemon with the following command for the settings to take effect:

$ sudo systemctl restart sshd.service
```

## V-281267 RHEL 10 must not allow users to override Secure Shell (SSH) environment variables. {#V-281267}

Severity: high · Rule: SV-281267r1184767_rule · STIG ID: RHEL-10-700640 · CCI-000381

**Discussion.** SSH environment options potentially allow users to bypass access restriction in some configurations.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

**Check.**

```
Verify RHEL 10 disables unattended or automatic login via SSH with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*permituserenvironment'
/etc/ssh/sshd_config.d/10-stig.conf:PermitUserEnvironment no

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i permituserenvironment
permituserenvironment no

If the "PermitUserEnvironment" keyword is not set to "no" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable unattended or automatic login via SSH.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

PermitUserEnvironment no

Restart the SSH daemon with the following command for the setting to take effect:

$ sudo systemctl restart sshd.service
```

## V-281268 RHEL 10 must force a frequent session key renegotiation for Secure Shell (SSH) connections to the server. {#V-281268}

Severity: high · Rule: SV-281268r1184768_rule · STIG ID: RHEL-10-700650 · CCI-002418 CCI-000068 CCI-002421

**Discussion.** Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered.

This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification.

Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.

Session key regeneration limits the chances of a session key becoming compromised.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000033-GPOS-00014, SRG-OS-000424-GPOS-00188

**Check.**

```
Verify RHEL 10 SSH servers are configured to force frequent session key renegotiation with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*rekeylimit'
/etc/ssh/sshd_config.d/10-stig.conf:RekeyLimit 1G 1h

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i rekeylimit
rekeylimit 1073741824 3600

If the "RekeyLimit" keyword is not set to "1G 1h" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to force a frequent session key renegotiation for SSH connections to the server.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

RekeyLimit 1G 1h

Restart the SSH daemon with the following command for the settings to take effect:

$ sudo systemctl restart sshd.service
```

## V-281269 RHEL 10 must be configured so that all network connections associated with Secure Shell (SSH) traffic terminate after becoming unresponsive. {#V-281269}

Severity: medium · Rule: SV-281269r1184769_rule · STIG ID: RHEL-10-700660 · CCI-001133 CCI-002361

**Discussion.** Terminating an idle SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. Quickly terminating an idle SSH session will also free up resources committed by the managed network element.

Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.

RHEL 10 uses "/etc/ssh/sshd_config" for configurations of OpenSSH. Within the sshd_config, the product of the values of "ClientAliveInterval" and "ClientAliveCountMax" are used to establish the inactivity threshold. The "ClientAliveInterval" is a timeout interval in seconds after which if no data has been received from the client, sshd will send a message through the encrypted channel to request a response from the client. The "ClientAliveCountMax" is the number of client alive messages that may be sent without sshd receiving any messages back from the client. If this threshold is met, sshd will disconnect the client. For more information on these settings and others, refer to the sshd_config man pages.

OpenSSH uses the first occurrence of a keyword it sees, and drop-in files are read in lexicographical order at the start of the configuration. Red Hat recommends using drop-in files rather than changing base configuration files.

Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109

**Check.**

```
Verify RHEL 10 network connections associated with SSH traffic terminate after becoming unresponsive. 

Set the "ClientAliveCountMax" to "1" by performing the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientalivecountmax'
/etc/ssh/sshd_config.d/10-stig.conf:ClientAliveCountMax 1

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i clientalivecountmax
clientalivecountmax 1

If the "ClientAliveCountMax" keyword is not set to a value of "1" in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to automatically terminate all network connections associated with SSH traffic at the end of a session or after 10 minutes of inactivity.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

ClientAliveCountMax 1

Restart the SSH daemon with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281270 RHEL 10 must forward mail from postmaster to the root account using a postfix alias. {#V-281270}

Severity: medium · Rule: SV-281270r1166762_rule · STIG ID: RHEL-10-700670 · CCI-000139

**Discussion.** It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected.

Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.

**Check.**

```
Verify RHEL 10 notifies administrators in the event of an audit processing failure.

Check that the "/etc/aliases" file has a defined value for "root".

$ sudo grep "postmaster:\s*root$" /etc/aliases
postmaster:     root

If the command does not return a line, or the line is commented out, ask the system administrator to indicate how they and the information systems security officer are notified of an audit process failure. 

If there is no evidence of the proper personnel being notified of an audit processing failure, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to have a valid email address as an alias for the root account.

Append the following line to "/etc/aliases":

postmaster: root

Run the following command:

$ sudo newaliases
```

## V-281271 RHEL 10 must not have a "shosts.equiv" file on the system. {#V-281271}

Severity: medium · Rule: SV-281271r1268226_rule · STIG ID: RHEL-10-700680 · CCI-000213

**Discussion.** The "shosts.equiv" files are used to configure host-based authentication for the system via Secure Shell (SSH). Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.

**Check.**

```
Verify RHEL 10 does not have a "shosts.equiv" file on the system with the following command:

$ sudo find / -name shosts.equiv

If a "shosts.equiv" file is found, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have a "shosts.equiv" file on the system.

Remove any found "shosts.equiv" files from the system:

$ sudo rm /[path]/[to]/[file]/shosts.equiv
```

## V-281272 RHEL 10 must not have any ".shosts" files on the system. {#V-281272}

Severity: medium · Rule: SV-281272r1268226_rule · STIG ID: RHEL-10-700690 · CCI-000213

**Discussion.** The ".shosts" files are used to configure host-based authentication for individual users or the system via Secure Shell (SSH). Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.

**Check.**

```
Verify RHEL 10 does not have any ".shosts" files on the system with the following command:

$ sudo find / -name .shosts

If a ".shosts" file is found, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have any ".shosts" files on the system.

Remove any found ".shosts" files from the system with the following command:

$ sudo rm /[path]/[to]/[file]/.shosts
```

## V-281273 RHEL 10 must prevent a user from overriding the disabling of the graphical user interface automount function. {#V-281273}

Severity: medium · Rule: SV-281273r1184699_rule · STIG ID: RHEL-10-700700 · CCI-000778 CCI-001958

**Discussion.** Without identifying and authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity.

Peripherals include, but are not limited to, such devices as flash drives, external storage, and printers.

Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 disables the ability of the user to override the graphical user interface automount setting.

Determine which profile the system database is using with the following command:

$ sudo grep system-db /etc/dconf/profile/user
system-db:local

Check that the automount setting is locked from nonprivileged user modification with the following command:

Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used.

$ sudo grep 'automount-open' /etc/dconf/db/local.d/locks/*
/org/gnome/desktop/media-handling/automount-open

If the command does not return at least the example result, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the GNOME desktop does not allow a user to change the setting that disables automated mounting of removable media.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/locks/00-security-settings-lock" file to prevent user modification:

$ sudo vi /etc/dconf/db/local.d/locks/00-security-settings-lock

/org/gnome/desktop/media-handling/automount-open

Update the dconf system databases:

$ sudo dconf update
```

## V-281274 RHEL 10 must prevent a user from overriding the disabling of the graphical user interface autorun function. {#V-281274}

Severity: medium · Rule: SV-281274r1197245_rule · STIG ID: RHEL-10-700710 · CCI-000778 CCI-001958

**Discussion.** Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., Transport Layer Security [TLS], WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.

Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 disables ability of the user to override the graphical user interface autorun setting.

Check that the autorun setting is set to prevent user modification with the following command:

$ gsettings writable org.gnome.desktop.media-handling autorun-never
false

If "autorun-never" is writable, the result is "true". 

If this is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the GNOME desktop does not allow a user to change the setting that disables autorun on removable media.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/locks/00-security-settings-lock" file to prevent user modification:

$ sudo vi /etc/dconf/db/local.d/locks/00-security-settings-lock

/org/gnome/desktop/media-handling/autorun-never

Update the dconf system databases:

$ sudo dconf update
```

## V-281275 RHEL 10 must not allow unattended or automatic login via the graphical user interface. {#V-281275}

Severity: high · Rule: SV-281275r1268226_rule · STIG ID: RHEL-10-700720 · CCI-000213

**Discussion.** Failure to restrict system access to authenticated users negatively impacts operating system security.

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 does not allow an unattended or automatic login to the system via a graphical user interface.

Check for the value of the "AutomaticLoginEnable" in the "/etc/gdm/custom.conf" file with the following command:

$  grep -i automaticlogin /etc/gdm/custom.conf
AutomaticLoginEnable=false

If the value of "AutomaticLoginEnable" is not set to "false", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the GNOME desktop display manager disables automatic login.

Update the "/etc/gdm/custom.conf" file to disable automatic login to the GNOME desktop:

$ sudo vi /etc/gdm/custom.conf

[daemon]
AutomaticLoginEnable=false
```

## V-281276 RHEL 10 must prevent a user from overriding the disabling of the graphical user smart card removal action. {#V-281276}

Severity: medium · Rule: SV-281276r1166780_rule · STIG ID: RHEL-10-700730 · CCI-000056 CCI-000057

**Discussion.** A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence.

The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, RHEL 10 must provide users with the ability to manually invoke a session lock so users can secure their session if they must temporarily vacate the immediate physical vicinity.

Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 disables ability of the user to override the smart card removal action setting with the following command:

$ gsettings writable org.gnome.settings-daemon.peripherals.smartcard removal-action
false

If "removal-action" is writable and the result is "true", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent a user from overriding the disabling of the graphical user smart card removal action.

Add the following line to "/etc/dconf/db/local.d/locks/00-security-settings-lock" to prevent user override of the smart card removal action:

/org/gnome/settings-daemon/peripherals/smartcard/removal-action

Update the dconf system databases:

$ sudo dconf update
```

## V-281277 RHEL 10 must prevent a user from overriding the screensaver lock-enabled setting for the graphical user interface. {#V-281277}

Severity: medium · Rule: SV-281277r1166783_rule · STIG ID: RHEL-10-700740 · CCI-000056 CCI-000057

**Discussion.** A session timeout lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems must be able to identify when a user's session has idled and take action to initiate the session lock.

The session lock is implemented at the point where session activity can be determined and/or controlled.

Implementing session settings will have little value if a user is able to manipulate these settings from the defaults prescribed in the other requirements of this implementation guide.

Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 prevents a user from overriding the screensaver lock-enabled setting with the following command:

$ gsettings writable org.gnome.desktop.screensaver lock-enabled
false

If "lock-enabled" is writable, and the result is "true", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent a user from overriding settings for graphical user interfaces.

Create a database to contain the systemwide screensaver settings (if it does not already exist) with the following command:

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/locks/session" file to prevent nonprivileged users from modifying the screensaver lock:

$ sudo vi /etc/dconf/db/local.d/locks/session

/org/gnome/desktop/screensaver/lock-enabled

Run the following command to update the database:

$ sudo dconf update
```

## V-281278 RHEL 10 must automatically lock graphical user sessions after 10 minutes of inactivity. {#V-281278}

Severity: medium · Rule: SV-281278r1208799_rule · STIG ID: RHEL-10-700750 · CCI-000057 CCI-000060

**Discussion.** A session timeout lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, the GNOME desktop can be configured to identify when a user's session has idled and take action to initiate a session lock.

Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 initiates a session lock after a 10-minute period of inactivity for graphical user interfaces with the following command:

$ sudo gsettings get org.gnome.desktop.session idle-delay
uint32 600

If "idle-delay" is set to "0" or a value greater than "600", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to initiate a screensaver after a 10-minute period of inactivity for graphical user interfaces.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/00-screensaver" file to prevent nonprivileged users from modifying the screensaver idle-delay setting:

$ sudo vi /etc/dconf/db/local.d/00-screensaver

[org/gnome/desktop/session]
# Set the lock time out to 900 seconds before the session is considered idle
idle-delay=uint32 600

Update the system databases:

$ sudo dconf update
```

## V-281279 RHEL 10 must prevent a user from overriding the session idle-delay setting for the graphical user interface. {#V-281279}

Severity: medium · Rule: SV-281279r1166789_rule · STIG ID: RHEL-10-700760 · CCI-000057 CCI-000060

**Discussion.** A session timeout lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, the GNOME desktop can be configured to identify when a user's session has idled and take action to initiate the session lock. Therefore, users should not be allowed to change session settings.

Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 prevents a user from overriding settings for session idle delay with the following command:

$ gsettings writable org.gnome.desktop.session idle-delay
false

If "idle-delay" is writable, and the result is "true", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent a user from overriding settings for graphical user interfaces.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/locks/session" file to prevent nonprivileged users from modifying the idle-delay lock:

$ sudo vi /etc/dconf/db/local.d/locks/session

/org/gnome/desktop/session/idle-delay

Run the following command to update the database:

$ sudo dconf update
```

## V-281280 RHEL 10 must initiate a session lock for graphical user interfaces when the screensaver is activated. {#V-281280}

Severity: medium · Rule: SV-281280r1166792_rule · STIG ID: RHEL-10-700770 · CCI-000057 CCI-000060

**Discussion.** A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence.

Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 initiates a session lock for graphical user interfaces when the screensaver is activated with the following command:

$ gsettings get org.gnome.desktop.screensaver lock-delay
uint32 5

If the "uint32" setting is not set to "5" or less, or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to initiate a session lock for graphical user interfaces when a screensaver is activated.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Create a database to contain the systemwide screensaver settings (if it does not already exist) with the following command:

$ sudo vi /etc/dconf/db/local.d/00-screensaver

[org/gnome/desktop/screensaver]
lock-delay=uint32 5

The "uint32" must be included along with the integer key values as shown.

Update the system databases:

$ sudo dconf update
```

## V-281281 RHEL 10 must prevent a user from overriding the session lock-delay setting for the graphical user interface. {#V-281281}

Severity: medium · Rule: SV-281281r1166795_rule · STIG ID: RHEL-10-700780 · CCI-000057 CCI-000060

**Discussion.** A session timeout lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, the GNOME desktop can be configured to identify when a user's session has idled and take action to initiate the session lock. Therefore, users should not be allowed to change session settings.

Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 prevents a user from overriding settings for the screensaver lock delay with the following command:

$ gsettings writable org.gnome.desktop.screensaver lock-delay
false

If "lock-delay" is writable, and the result is "true", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent a user from overriding settings for graphical user interfaces.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/locks/session" file to prevent nonprivileged users from modifying the lock-delay setting:

$ sudo vi /etc/dconf/db/local.d/locks/session

/org/gnome/desktop/screensaver/lock-delay

Run the following command to update the database:

$ sudo dconf update
```

## V-281282 RHEL 10 must conceal, via the session lock, information previously visible on the display with a publicly viewable image. {#V-281282}

Severity: medium · Rule: SV-281282r1166798_rule · STIG ID: RHEL-10-700790 · CCI-000060

**Discussion.** Setting the screensaver mode to blank-only conceals the contents of the display from passersby.

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 prevents a user from overriding settings a blank screensaver with the following command:

$ gsettings writable org.gnome.desktop.screensaver picture-uri
false

If "picture-uri" is writable, and the result is "true", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent a user from overriding the picture-uri setting for graphical user interfaces.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/00-security-settings" file to prevent a user from overriding the "picture-uri" setting:

$ sudo vi /etc/dconf/db/local.d/00-security-settings

[org/gnome/desktop/screensaver]
picture-uri=''

Update the "/etc/dconf/db/local.d/locks/00-security-settings-lock" file to prevent a user from modifying the lock applied to the "picture-uri" setting:

$ sudo vi /etc/dconf/db/local.d/locks/00-security-settings-lock

/org/gnome/desktop/screensaver/picture-uri

Update the dconf system databases:

$ sudo dconf update
```

## V-281283 RHEL 10 must ensure effective dconf policy matches the policy keyfiles. {#V-281283}

Severity: medium · Rule: SV-281283r1268226_rule · STIG ID: RHEL-10-700800 · CCI-000213

**Discussion.** Unlike text-based keyfiles, the binary database is impossible to check through most automated and all manual means; therefore, to evaluate dconf configuration, both must be true at the same time. Configuration files must be compliant, and the database must be more recent than those keyfiles, which gives confidence that it reflects them.

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 ensures effective dconf policy matches the policy keyfiles.

Check the last modification time of the local databases, comparing it to the last modification time of the related keyfiles. The following command will check every dconf database and compare its modification time to the related system keyfiles:

$ function dconf_needs_update { for db in $(find /etc/dconf/db -maxdepth 1 -type f); do db_mtime=$(stat -c %Y "$db"); keyfile_mtime=$(stat -c %Y "$db".d/* | sort -n | tail -1); if [ -n "$db_mtime" ] && [ -n "$keyfile_mtime" ] && [ "$db_mtime" -lt "$keyfile_mtime" ]; then echo "$db needs update"; return 1; fi; done; }; dconf_needs_update

If the command has any output, then a dconf database needs to be updated, and this is a finding.
```

**Fix.**

```
Configure RHEL 10 to ensure that the effective dconf policy matches the policy keyfiles.

Update the dconf databases by running the following command:

$ sudo dconf update
```

## V-281284 RHEL 10 must prevent a user from overriding the disable-restart-buttons setting for the graphical user interface. {#V-281284}

Severity: medium · Rule: SV-281284r1197247_rule · STIG ID: RHEL-10-700810 · CCI-002696

**Discussion.** A user who is at the console can reboot the system at the login screen. If restart or shutdown buttons are pressed at the login screen, this can create the risk of short-term loss of availability of systems due to reboot.

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 prevents a user from overriding the disable-restart-buttons setting for graphical user interfaces:

$ gsettings writable org.gnome.login-screen disable-restart-buttons
false

If "disable-restart-buttons" is writable, and the result is "true", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent a user from overriding the disable-restart-buttons setting for graphical user interfaces.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/locks/session" file to prevent nonprivileged users from modifying the disable-restart-buttons setting:

$ sudo vi /etc/dconf/db/local.d/locks/session

/org/gnome/login-screen/disable-restart-buttons

Run the following command to update the database:

$ sudo dconf update
```

## V-281285 RHEL 10 must prevent a user from overriding the Ctrl-Alt-Del sequence settings for the graphical user interface. {#V-281285}

Severity: medium · Rule: SV-281285r1197249_rule · STIG ID: RHEL-10-700820 · CCI-002385

**Discussion.** A locally logged-in user who presses Ctrl-Alt-Del when at the console can reboot the system. If accidentally pressed, as could happen in the case of a mixed operating system environment, this can create the risk of short-term loss of systems' availability due to unintentional reboot.

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 users cannot enable the Ctrl-Alt-Del sequence in the GNOME desktop:

$ gsettings writable org.gnome.settings-daemon.plugins.media-keys logout
false

If "logout" is writable and the result is "true", this is a finding.

If GNOME is configured to shut down when Ctrl-Alt-Del is pressed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disallow the user changing the Ctrl-Alt-Del sequence in the GNOME desktop.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/locks/session" file to prevent nonprivileged users from modifying the Ctrl-Alt-Del setting:

$ sudo vi /etc/dconf/db/local.d/locks/session

/org/gnome/settings-daemon/plugins/media-keys/logout

Run the following command to update the database:

$ sudo dconf update
```

## V-281286 RHEL 10 must disable the ability of a user to accidentally press Ctrl-Alt-Del and cause a system to shut down or reboot. {#V-281286}

Severity: medium · Rule: SV-281286r1166810_rule · STIG ID: RHEL-10-700830 · CCI-002385

**Discussion.** A locally logged-in user who presses Ctrl-Alt-Del, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of mixed operating system environments, this can create the risk of short-term loss of availability of systems due to unintentional reboot.

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 is configured to ignore the Ctrl-Alt-Del sequence in the GNOME desktop with the following command:

Check that the Ctrl-Alt-Del sequence settings for the graphical user interface cannot be overridden with the following command:

$ gsettings get org.gnome.settings-daemon.plugins.media-keys logout
@as []

If the GNOME desktop is configured to shut down when Ctrl-Alt-Del is pressed, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to ignore the Ctrl-Alt-Del sequence in the GNOME desktop.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/00-media-keys" file to set the media-keys logout setting as an empty string array:

$ sudo vi /etc/dconf/db/local.d/00-media-keys

[org/gnome/settings-daemon/plugins/media-keys]
logout=@as []

Run the following command to update the database:

$ sudo dconf update
```

## V-281287 RHEL 10 must disable the user list at login for graphical user interfaces. {#V-281287}

Severity: medium · Rule: SV-281287r1166813_rule · STIG ID: RHEL-10-700840 · CCI-000381

**Discussion.** Leaving the user list enabled is a security risk because it allows anyone with physical access to the system to enumerate known user accounts without authenticated access to the system.

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 disables the user login list for graphical user interfaces with the following command:

$ gsettings get org.gnome.login-screen disable-user-list
true

If the setting is "false", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable the user list at login for graphical user interfaces.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Create a database to contain the systemwide screensaver settings (if it does not already exist) with the following command:

$ sudo vi /etc/dconf/db/local.d/02-login-screen

[org/gnome/login-screen]
disable-user-list=true

Update the system databases:

$ sudo dconf update
```

## V-281288 RHEL 10 must be configured to disable USB mass storage. {#V-281288}

Severity: medium · Rule: SV-281288r1166816_rule · STIG ID: RHEL-10-700850 · CCI-000778 CCI-001958

**Discussion.** USB mass storage permits easy introduction of unknown devices, thereby facilitating malicious activity.

Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163

**Check.**

```
Verify RHEL 10 disables the ability to load the USB Storage kernel module with the following command:

$ sudo grep -rs usb-storage /etc/modprobe.conf /etc/modprobe.d/*
/etc/modprobe.d/usb-storage.conf:install usb-storage /bin/false
/etc/modprobe.d/usb-storage.conf:blacklist usb-storage

If the command does not return any output, or either line is commented out, and use of USB Storage is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent the usb-storage kernel module from being loaded.

Add the following lines to the file "/etc/modprobe.d/usb-storage.conf" (or create "usb-storage.conf" if it does not exist):

$ sudo vi /etc/modprobe.d/usb-storage.conf

install usb-storage /bin/false
blacklist usb-storage
```

## V-281289 RHEL 10 must disable Bluetooth. {#V-281289}

Severity: medium · Rule: SV-281289r1273601_rule · STIG ID: RHEL-10-700860 · CCI-000381 CCI-001443

**Discussion.** This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with RHEL 10 systems. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR keyboards, mice and pointing devices, and near field communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. 

Wireless peripherals must meet DoW requirements for wireless data transmission and be approved for use by the authorizing official. Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that must be protected, modification of communications with these wireless peripherals may be used to compromise the RHEL 10 operating system.

Satisfies: SRG-OS-000095-GPOS-00049, SRG-OS-000300-GPOS-00118

**Check.**

```
Verify RHEL 10 disables the ability to load the Bluetooth kernel module with the following command:

$ sudo grep -rs bluetooth /etc/modprobe.conf /etc/modprobe.d/*
/etc/modprobe.d/bluetooth.conf:install bluetooth /bin/false
/etc/modprobe.d/bluetooth.conf:blacklist bluetooth

If the command does not return any output, or the lines are commented out, and use of Bluetooth is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable the Bluetooth adapter when not in use.

Add the following lines to the file "/etc/modprobe.d/bluetooth.conf" (or create "bluetooth.conf" if it does not exist):

$ sudo vi /etc/modprobe.d/bluetooth.conf

install bluetooth /bin/false
blacklist bluetooth

Reboot the system for the settings to take effect.
```

## V-281290 RHEL 10 must disable wireless network adapters. {#V-281290}

Severity: medium · Rule: SV-281290r1273602_rule · STIG ID: RHEL-10-700870 · CCI-001444 CCI-001443 CCI-002421 CCI-002418

**Discussion.** This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with RHEL 10 systems. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR keyboards, mice and pointing devices, and near field communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. 

Wireless peripherals must meet DoW requirements for wireless data transmission and be approved for use by the authorizing official. Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that must be protected, modification of communications with these wireless peripherals may be used to compromise the RHEL 10 operating system.

Satisfies: SRG-OS-000299-GPOS-00117, SRG-OS-000300-GPOS-00118, SRG-OS-000424-GPOS-00188, SRG-OS-000481-GPOS-00481

**Check.**

```
Note: This requirement is not applicable for systems that do not have physical wireless network radios.

Verify RHEL 10 disables wireless interfaces on the system with the following command:

$ nmcli device status
DEVICE                    TYPE            STATE                    CONNECTION
virbr0                      bridge         connected             virbr0
wlp7s0                    wifi              connected            wifiSSID
enp6s0                    ethernet     disconnected        --
p2p-dev-wlp7s0     wifi-p2p     disconnected        --
lo                             loopback    unmanaged           --
virbr0-nic                tun              unmanaged          --

If a wireless interface is configured and has not been documented and approved by the information system security officer, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable all wireless network interfaces with the following command:

$ nmcli radio all off
```

## V-281291 RHEL 10 must disable the graphical user interface automounter unless required. {#V-281291}

Severity: medium · Rule: SV-281291r1166825_rule · STIG ID: RHEL-10-700880 · CCI-000778 CCI-001958

**Discussion.** Automatically mounting file systems permits easy introduction of unknown devices, thereby facilitating malicious activity.

Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 disables the graphical user interface automount function.

Disable the setting with the following command:

$ gsettings get org.gnome.desktop.media-handling automount-open
false

If "automount-open" is set to "true" and is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 GNOME to disable automated mount of removable media.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/00-security-settings" database file with the following lines:

$ sudo vi /etc/dconf/db/local.d/00-security-settings

[org/gnome/desktop/media-handling]
automount-open=false

Update the dconf system databases:

$ sudo dconf update
```

## V-281292 RHEL 10 must disable the graphical user interface autorunner unless required. {#V-281292}

Severity: low · Rule: SV-281292r1166828_rule · STIG ID: RHEL-10-700890 · CCI-000778 CCI-001958

**Discussion.** Automatically running applications when media is inserted allows for the easy introduction of unknown data, thereby facilitating malicious activity.

Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163

**Check.**

```
Note: This requirement assumes the use of the RHEL 10 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is not applicable.

Verify RHEL 10 disables the graphical user interface autorun function.

Disable the setting with the following command:

$ gsettings get org.gnome.desktop.media-handling autorun-never
true

If "autorun-never" is set to "false" and is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 GNOME to disable autorunning of removable media.

Note: The example below is using the database "local" for the system. If the system is using another database in "/etc/dconf/profile/user", the file should be created under the appropriate subdirectory.

Update the "/etc/dconf/db/local.d/00-security-settings" database to disable the GUI autorun function:

$ sudo vi /etc/dconf/db/local.d/00-security-settings

[org/gnome/desktop/media-handling]
autorun-never=true

Update the dconf system databases:

$ sudo dconf update
```

## V-281293 RHEL 10 must implement nonexecutable data to protect its memory from unauthorized code execution. {#V-281293}

Severity: medium · Rule: SV-281293r1166831_rule · STIG ID: RHEL-10-700900 · CCI-002824

**Discussion.** ExecShield uses the segmentation feature on all x86 systems to prevent execution in memory higher than a certain address. It writes an address as a limit in the code segment descriptor, to control where code can be executed, on a per-process basis. When the kernel places a process's memory regions such as the stack and heap higher than this address, the hardware prevents execution in that address range. This is enabled by default on the latest Red Hat and Fedora systems if supported by the hardware.

**Check.**

```
Verify RHEL 10 implements nonexecutable data to protect its memory from unauthorized code execution.

Run the following command:

$ sudo grep ^flags /proc/cpuinfo | grep -Ev '([^[:alnum:]])(nx)([^[:alnum:]]|$)'

If any output is returned, this is a finding.

Run the following command:

$ sudo grubby --info=ALL | grep args | grep -E '([^[:alnum:]])(noexec)([^[:alnum:]])'

If any output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to implement nonexecutable data to protect its memory from unauthorized code execution.

Update the GRUB 2 bootloader configuration.

Run the following command:

$ sudo grubby --update-kernel=ALL --remove-args=noexec
```

## V-281295 RHEL 10 must automatically exit interactive command shell user sessions after 10 minutes of inactivity. {#V-281295}

Severity: medium · Rule: SV-281295r1273603_rule · STIG ID: RHEL-10-700920 · CCI-001133

**Discussion.** Terminating an idle interactive command shell user session within a short time period reduces the window of opportunity for unauthorized personnel to take control of it when left unattended in a virtual terminal or physical console.

Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000029-GPOS-00010

**Check.**

```
Verify RHEL 10 is configured to exit interactive command shell user sessions after 10 minutes of inactivity or less with the following command:

$ sudo grep -i tmout /etc/profile /etc/profile.d/*.sh
/etc/profile.d/tmout.sh:declare -xr TMOUT=600

If "TMOUT" is not set to "600" or less in a script located in the "/etc/'profile.d/" directory, is missing, or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to exit interactive command shell user sessions after 10 minutes of inactivity.

Add or edit the following line in "/etc/profile.d/tmout.sh":

#!/bin/bash

declare -xr TMOUT=600
```

## V-281296 RHEL 10 must be configured with a timeout interval for the Secure Shell (SSH) daemon. {#V-281296}

Severity: medium · Rule: SV-281296r1184670_rule · STIG ID: RHEL-10-700930 · CCI-001133 CCI-002361 CCI-002891

**Discussion.** Terminating an idle SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element.

Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.

RHEL 10 uses "/etc/ssh/sshd_config" for configurations of OpenSSH. Within the "sshd_config", the product of the values of "ClientAliveInterval" and "ClientAliveCountMax" are used to establish the inactivity threshold. 

The "ClientAliveInterval" is a timeout interval in seconds after which if no data has been received from the client, sshd will send a message through the encrypted channel to request a response from the client. 

The "ClientAliveCountMax" is the number of client alive messages that may be sent without sshd receiving any messages back from the client. If this threshold is met, sshd will disconnect the client. 

For more information on these settings and others, refer to the sshd_config man pages.

Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109, SRG-OS-000395-GPOS-00175

**Check.**

```
Verify RHEL 10 is configured with an SSH timeout interval.

Verify the "ClientAliveInterval" variable is set to a value of "600" or less by performing the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientaliveinterval'
/etc/ssh/sshd_config.d/10-stig.conf::ClientAliveInterval 600

Verify the runtime setting with the following command:

$ sudo sshd -T | grep -i clientaliveinterval
clientaliveinterval 600

If the "ClientAliveInterval" keyword is not set to a value of "600" or less in a drop-in that lexicographically precedes 50-redhat.conf, or if no output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to automatically terminate all network connections associated with SSH traffic at the end of a session or after 10 minutes of inactivity.

Note: This setting must be applied in conjunction with RHEL-10-700660 to function correctly.

In "/etc/ssh/sshd_config.d", create a drop file that will lexicographically precede 50-redhat.conf and add the following line:

ClientAliveInterval 600

Restart the SSH daemon with the following command for the changes to take effect:

$ sudo systemctl restart sshd.service
```

## V-281297 RHEL 10 must not default to the graphical display manager unless approved. {#V-281297}

Severity: medium · Rule: SV-281297r1166843_rule · STIG ID: RHEL-10-700940 · CCI-000381

**Discussion.** Unnecessary service packages must not be installed to decrease the attack surface of the system. Graphical display managers have a long history of security vulnerabilities and must not be used unless approved and documented.

**Check.**

```
Verify RHEL 10 is configured to boot to the command line with the following command:

$ systemctl get-default
multi-user.target

If the system default target is not set to "multi-user.target", and the information system security officer lacks a documented requirement for a graphical user interface, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to boot to the command line by setting the default target to "multi-user" with the following command:

$ sudo systemctl set-default multi-user.target
```

## V-281298 RHEL 10 must disable the systemd Ctrl-Alt-Delete burst key sequence. {#V-281298}

Severity: high · Rule: SV-281298r1273604_rule · STIG ID: RHEL-10-700950 · CCI-002235

**Discussion.** A locally logged-on user who presses Ctrl-Alt-Delete when at the console can reboot the system. If accidentally pressed, as could happen in the case of a mixed operating system environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. 

In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.

**Check.**

```
Verify RHEL 10 is configured to not reboot the system when Ctrl-Alt-Delete is pressed seven times within two seconds with the following command:

$ sudo grep -iR CtrlAltDelBurstAction /etc/systemd/system*
/etc/systemd/system.conf.d/55-CtrlAltDel-BurstAction.conf:CtrlAltDelBurstAction=none

If the "CtrlAltDelBurstAction" is not set to "none", is commented out, or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable the CtrlAltDelBurstAction by adding it to a drop file in a "/etc/systemd/system.conf.d/" configuration file:

If no drop file exists, create one with the following command:

$ sudo mkdir -p /etc/systemd/system.conf.d && sudo vi /etc/systemd/system.conf.d/55-CtrlAltDel-BurstAction.conf

Edit the file to contain the setting by adding the following text:

[Manager]
CtrlAltDelBurstAction=none

Reload the daemon for this change to take effect.

$ sudo systemctl daemon-reload
```

## V-281299 RHEL 10 must disable the x86 Ctrl-Alt-Delete key sequence. {#V-281299}

Severity: high · Rule: SV-281299r1166849_rule · STIG ID: RHEL-10-700960 · CCI-002235

**Discussion.** A locally logged-on user who presses Ctrl-Alt-Delete when at the console can reboot the system. If accidentally pressed, as could happen in the case of a mixed operating system environment, this can create the risk of short-term loss of systems availability due to unintentional reboot. 

In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.

**Check.**

```
Verify RHEL 10 is not configured to reboot the system when Ctrl-Alt-Delete is pressed with the following command:

$ sudo systemctl status ctrl-alt-del.target
o ctrl-alt-del.target
        Loaded: masked (Reason: Unit ctrl-alt-del.target is masked.)
        Active: inactive (dead)

If the "ctrl-alt-del.target" is loaded and not masked, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable the "ctrl-alt-del.target" with the following command:

$ sudo systemctl disable --now ctrl-alt-del.target
$ sudo systemctl mask --now ctrl-alt-del.target
```

## V-281300 RHEL 10 must disable the ability of systemd to spawn an interactive boot process. {#V-281300}

Severity: medium · Rule: SV-281300r1167050_rule · STIG ID: RHEL-10-700980 · CCI-000381

**Discussion.** Using interactive or recovery boot, the console user could disable auditing, firewalls, or other services, weakening system security.

**Check.**

```
Verify RHEL 10 is configured so that the current GRUB 2 configuration disables the ability of systemd to spawn an interactive boot process with the following command:

$ sudo grubby --info=ALL | grep args | grep 'systemd.confirm_spawn'

If any output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that the current GRUB 2 configuration disables the ability of systemd to spawn an interactive boot process with the following command:

$ sudo grubby --update-kernel=ALL --remove-args="systemd.confirm_spawn"
```

## V-281301 RHEL 10 must disable virtual system calls. {#V-281301}

Severity: medium · Rule: SV-281301r1184700_rule · STIG ID: RHEL-10-700990 · CCI-001084

**Discussion.** System calls are special routines in the Linux kernel, which userspace applications ask to do privileged tasks. Invoking a system call is an expensive operation because the processor must interrupt the currently executing task and switch context to kernel mode and then back to userspace after the system call completes. Virtual system calls map into user space a page that contains some variables and the implementation of some system calls. This allows the system calls to be executed in userspace to alleviate the context-switching expense.

Virtual system calls provide an opportunity of attack for a user who has control of the return instruction pointer. Disabling virtual system calls help to prevent return-oriented programming attacks via buffer overflows and overruns.

**Check.**

```
Verify RHEL 10 is configured so that the current GRUB 2 configuration disables virtual system calls with the following command:

$ sudo grubby --info=ALL | grep args | grep -v 'vsyscall=none'

If any output is returned, this is a finding.

Check that virtual system calls are disabled by default to persist in kernel updates with the following command:

$ sudo grep vsyscall /etc/default/grub
GRUB_CMDLINE_LINUX="vsyscall=none"

If "vsyscall" is not set to "none", is missing or commented out, and is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable virtual system calls with the following command:

$ sudo grubby --update-kernel=ALL --args="vsyscall=none"
```

## V-281302 RHEL 10 must clear the page allocator to prevent use-after-free attacks. {#V-281302}

Severity: medium · Rule: SV-281302r1167056_rule · STIG ID: RHEL-10-701000 · CCI-001084

**Discussion.** Poisoning writes an arbitrary value to freed pages, so any modification or reference to that page after being freed or before being initialized will be detected and prevented. This prevents many types of use-after-free vulnerabilities at little performance cost. It also prevents data leakage and detection of corrupted memory.

**Check.**

```
Verify RHEL 10 is configured so that the current GRUB 2 configuration enables page poisoning to mitigate use-after-free vulnerabilities.

Check that the current GRUB 2 configuration has page poisoning enabled with the following command:

$ sudo grubby --info=ALL | grep args | grep -v 'page_poison=1'

If any output is returned, this is a finding.

Check that page poisoning is enabled by default to persist in kernel updates with the following command:

$ sudo grep page_poison /etc/default/grub
GRUB_CMDLINE_LINUX="page_poison=1"

If "page_poison" is not set to "1", is missing or commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable page poisoning with the following commands:

$ sudo grubby --update-kernel=ALL --args="page_poison=1"
```

## V-281303 RHEL 10 must clear memory when it is freed to prevent use-after-free attacks. {#V-281303}

Severity: medium · Rule: SV-281303r1167059_rule · STIG ID: RHEL-10-701010 · CCI-001084

**Discussion.** Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can be either hardware-enforced or software-enforced, with hardware providing the greater strength of mechanism.

Poisoning writes an arbitrary value to freed pages, so any modification or reference to that page after being freed or before being initialized will be detected and prevented. This prevents many types of use-after-free vulnerabilities at little performance cost. It also prevents data leakage and detection of corrupted memory.

"init_on_free" is a Linux kernel boot parameter that enhances security by initializing memory regions when they are freed, preventing data leakage. This process ensures that stale data in freed memory cannot be accessed by malicious programs.

SLUB canaries add a randomized value (canary) at the end of SLUB-allocated objects to detect memory corruption caused by buffer overflows or underflows. Redzoning adds padding (red zones) around SLUB-allocated objects to detect overflows or underflows by triggering a fault when adjacent memory is accessed. SLUB canaries are often more efficient and provide stronger detection against buffer overflows compared to redzoning. SLUB canaries are supported in hardened Linux kernels such as the ones provided by Linux-hardened.

SLAB objects are blocks of physically contiguous memory. SLUB is the unqueued SLAB allocator.

**Check.**

```
Verify RHEL 10 is configured so that the current GRUB2 configuration mitigates use-after-free vulnerabilities by employing memory poisoning.

Check that the current GRUB2 configuration mitigates use-after-free vulnerabilities by employing memory poisoning with the following command:

$ sudo grubby --info=ALL | grep args | grep -v init_on_free=1

If any output is returned, this is a finding.

Check that page poisoning is enabled by default to persist in kernel updates with the following command:

$ sudo grep grub_cmdline_linux /etc/default/grub
GRUB_CMDLINE_LINUX="... init_on_free=1"

If "init_on_free=1" is missing or commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable "init_on_free" with the following command:

$ sudo grubby --update-kernel=ALL --args="init_on_free=1"
```

## V-281304 RHEL 10 must enable mitigations against processor-based vulnerabilities. {#V-281304}

Severity: medium · Rule: SV-281304r1167062_rule · STIG ID: RHEL-10-701020 · CCI-002824 CCI-000381

**Discussion.** Kernel page-table isolation is a kernel feature that mitigates the Meltdown security vulnerability and hardens the kernel against attempts to bypass kernel address space layout randomization (KASLR).

Satisfies: SRG-OS-000433-GPOS-00193, SRG-OS-000095-GPOS-00049

**Check.**

```
Verify RHEL 10 enables kernel page-table isolation with the following command:

$ sudo grubby --info=ALL | grep args | grep -v 'pti=on'

If any output is returned, this is a finding.

Check that kernel page-table isolation is enabled by default to persist in kernel updates:

$ sudo grep pti /etc/default/grub
GRUB_CMDLINE_LINUX="pti=on"

If "pti" is not set to "on", is missing, or is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable kernel page-table isolation with the following command:

$ sudo grubby --update-kernel=ALL --args="pti=on"
```

## V-281305 RHEL 10 must restrict access to the kernel message buffer. {#V-281305}

Severity: medium · Rule: SV-281305r1273605_rule · STIG ID: RHEL-10-701030 · CCI-001082 CCI-001090

**Discussion.** Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection.

This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoW or other government agencies.

There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.

Restricting access to the kernel message buffer limits access to only root. This prevents attackers from gaining additional system information as a nonprivileged user.

Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069

**Check.**

```
Verify RHEL 10 is configured to restrict access to the kernel message buffer.

Check the status of the "kernel.dmesg_restrict" kernel parameter with the following command:

$ sudo sysctl kernel.dmesg_restrict
kernel.dmesg_restrict = 1

If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to restrict access to the kernel message buffer.

Create a drop-in if it does not already exist:

$ sudo vi /etc/sysctl.d/99-dmesg_restrict.conf

Add the following to the file:

kernel.dmesg_restrict = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281306 RHEL 10 must prevent kernel profiling by nonprivileged users. {#V-281306}

Severity: medium · Rule: SV-281306r1273606_rule · STIG ID: RHEL-10-701040 · CCI-001082 CCI-001090

**Discussion.** Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection.

This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoW or other government agencies.

There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.

Setting the "kernel.perf_event_paranoid" kernel parameter to "2" prevents attackers from gaining additional system information as a nonprivileged user.

Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069

**Check.**

```
Verify RHEL 10 is configured to prevent kernel profiling by nonprivileged users.

Check the status of the "kernel.perf_event_paranoid" kernel parameter:

$ sudo sysctl kernel.perf_event_paranoid
kernel.perf_event_paranoid = 2

If "kernel.perf_event_paranoid" is not set to "2" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent kernel profiling by nonprivileged users.

Create a drop-in if it does not already exist:

$ sudo vi /etc/sysctl.d/99-kernel_perf_event_paranoid.conf

Add the following to the file:

kernel.perf_event_paranoid = 2

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281307 RHEL 10 must prevent the loading of a new kernel for later execution. {#V-281307}

Severity: high · Rule: SV-281307r1268241_rule · STIG ID: RHEL-10-701050 · CCI-003992

**Discussion.** Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and has been provided by a trusted vendor.

Disabling kexec_load prevents an unsigned kernel image (that could be a windows kernel or modified vulnerable kernel) from being loaded. Kexec can be used to subvert the entire secureboot process and should be avoided at all costs, especially because it can load unsigned kernel images.

**Check.**

```
Verify RHEL 10 is configured to disable kernel image loading.

Check the status of the "kernel.kexec_load_disabled" kernel parameter with the following command:

$ sudo sysctl kernel.kexec_load_disabled
kernel.kexec_load_disabled = 1

If "kernel.kexec_load_disabled" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable kernel image loading.

Create a drop-in if it does not already exist:

$ sudo vi /etc/sysctl.d/99-kernel_kexec_load_disabled.conf

Add the following to the file:

kernel.kexec_load_disabled = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281308 RHEL 10 must restrict exposed kernel pointer address access. {#V-281308}

Severity: medium · Rule: SV-281308r1167074_rule · STIG ID: RHEL-10-701060 · CCI-001082 CCI-002824

**Discussion.** Exposing kernel pointers (through procfs or "seq_printf()") exposes kernel writable structures, which may contain functions pointers. If a write vulnerability occurs in the kernel, allowing write access to any of this structure, the kernel can be compromised. This option disallows any program without the CAP_SYSLOG capability to get the addresses of kernel pointers by replacing them with "0".

Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000433-GPOS-00192

**Check.**

```
Verify RHEL 10 is configured to restrict exposed kernel pointer address access.

Verify the runtime status of the "kernel.kptr_restrict" kernel parameter with the following command:

$ sudo sysctl kernel.kptr_restrict 
kernel.kptr_restrict = 1

If "kernel.kptr_restrict" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to restrict exposed kernel pointer address access.

Create a drop-in if it does not already exist:

$ sudo vi /etc/sysctl.d/99-kernel_kptr_restrict.conf

Add the following to the file:

kernel.kptr_restrict = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281309 RHEL 10 must enable kernel parameters to enforce discretionary access control (DAC) on hardlinks. {#V-281309}

Severity: medium · Rule: SV-281309r1184631_rule · STIG ID: RHEL-10-701070 · CCI-002165 CCI-002235

**Discussion.** By enabling the "fs.protected_hardlinks" kernel parameter, users can no longer create soft or hard links to files they do not own. Disallowing such hardlinks mitigates vulnerabilities based on insecure file systems accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat().

Satisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123, SRG-OS-000324-GPOS-00125

**Check.**

```
Verify RHEL 10 is configured to enable DAC on hardlinks.

Check the status of the "fs.protected_hardlinks" kernel parameter with the following command:

$ sudo sysctl fs.protected_hardlinks
fs.protected_hardlinks = 1

If "fs.protected_hardlinks" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable DAC on hardlinks.

Create a drop-in if it does not already exist:

$ sudo vi /etc/sysctl.d/99-fs_protected_hardlinks.conf

Add the following to the file:

fs.protected_hardlinks = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281310 RHEL 10 must enable kernel parameters to enforce discretionary access control (DAC) on symlinks. {#V-281310}

Severity: medium · Rule: SV-281310r1167080_rule · STIG ID: RHEL-10-701080 · CCI-002165 CCI-002235

**Discussion.** By enabling the "fs.protected_symlinks" kernel parameter, symbolic links are permitted to be followed only when outside a sticky world-writable directory, or when the user identifier (UID) of the link and follower match, or when the directory owner matches the symlink's owner. Disallowing such symlinks helps mitigate vulnerabilities based on insecure file systems accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat().

Satisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123, SRG-OS-000324-GPOS-00125

**Check.**

```
Verify RHEL 10 is configured to enable DAC on symlinks.

Check the status of the "fs.protected_symlinks" kernel parameter with the following command:

$ sudo sysctl fs.protected_symlinks
fs.protected_symlinks = 1

If "fs.protected_symlinks" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable DAC on symlinks with the following:

Create a drop-in if it does not already exist:

$ sudo vi /etc/sysctl.d/99-fs_protected_symlinks.conf

Add the following to the file:

fs.protected_symlinks = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281311 RHEL 10 must disable the "kernel.core_pattern". {#V-281311}

Severity: medium · Rule: SV-281311r1167083_rule · STIG ID: RHEL-10-701090 · CCI-000381

**Discussion.** A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.

**Check.**

```
Verify RHEL 10 disables storing core dumps.

Check the status of the "kernel.core_pattern" kernel parameter with the following command:

$ sudo sysctl kernel.core_pattern
kernel.core_pattern = |/bin/false

If "kernel.core_pattern" is not set to "|/bin/false", or a line is not returned and the need for core dumps is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable storing core dumps. 

Create a drop-in if it does not already exist:

$ sudo vi /etc/sysctl.d/99-kernel_core_pattern.conf

Add the following to the file:

kernel.core_pattern = |/bin/false

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281312 RHEL 10 must be configured to disable the Controller Area Network (CAN) kernel module. {#V-281312}

Severity: medium · Rule: SV-281312r1167086_rule · STIG ID: RHEL-10-701100 · CCI-000381

**Discussion.** Disabling CAN protects the system against exploitation of any flaws in its implementation.

**Check.**

```
Verify RHEL 10 disables the ability to load the CAN kernel module with the following command:

$ sudo grep -rs can /etc/modprobe.conf /etc/modprobe.d/* | grep -v '#'
/etc/modprobe.d/can.conf:install can /bin/false
/etc/modprobe.d/can.conf:blacklist can

If the command does not return any output, or the lines are commented out, and use of CAN is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable the ability to load the CAN kernel module.

Create a drop-in if it does not already exist:

$ sudo vi /etc/modprobe.d/can.conf

Add the following lines to the file:

install can /bin/false
blacklist can
```

## V-281313 RHEL 10 must disable the Stream Control Transmission Protocol (SCTP) kernel module. {#V-281313}

Severity: medium · Rule: SV-281313r1184770_rule · STIG ID: RHEL-10-701110 · CCI-000381

**Discussion.** It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors.

Failing to disconnect unused protocols can result in a system compromise.

The SCTP is a transport layer protocol, designed to support the idea of message-oriented communication, with several streams of messages within one connection. Disabling SCTP protects the system against exploitation of any flaws in its implementation.

**Check.**

```
Verify RHEL 10 disables the ability to load the sctp kernel module with the following command:

$ sudo grep -rs sctp /etc/modprobe.conf /etc/modprobe.d/* | grep -v '#'
/etc/modprobe.d/sctp-blacklist.conf:install sctp /bin/false
/etc/modprobe.d/sctp-blacklist.conf:blacklist sctp

If the command does not return any output, or the lines are commented out, and use of sctp is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable the ability to load the sctp kernel module.

Create a drop-in if it does not already exist:

$ sudo vi /etc/modprobe.d/sctp.conf

Add the following lines to the file:

install sctp /bin/false
blacklist sctp
```

## V-281314 RHEL 10 must disable the Transparent Inter Process Communication (TIPC) kernel module. {#V-281314}

Severity: medium · Rule: SV-281314r1184771_rule · STIG ID: RHEL-10-701120 · CCI-000381

**Discussion.** It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors.

Failing to disconnect unused protocols can result in a system compromise.

The TIPC is a protocol that is specially designed for intra-cluster communication. It can be configured to transmit messages either on User Datagram Protocol (UDP) or directly across Ethernet. Message delivery is sequence guaranteed, loss free, and flow controlled. Disabling TIPC protects the system against exploitation of any flaws in its implementation.

**Check.**

```
Verify RHEL 10 disables the ability to load the tipc kernel module with the following command:

$ sudo grep -rs tipc /etc/modprobe.conf /etc/modprobe.d/* | grep -v '#'
/etc/modprobe.d/tipc-blacklist.conf:install tipc /bin/false
/etc/modprobe.d/tipc-blacklist.conf:blacklist tipc

If the command does not return any output, or the lines are commented out, and use of tipc is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable the ability to load the tipc kernel module.

Create a drop-in if it does not already exist:

$ sudo vi /etc/modprobe.d/tipc.conf

Add the following lines to the file:

install tipc /bin/false
blacklist tipc
```

## V-281315 RHEL 10 must implement address space layout randomization (ASLR) to protect its memory from unauthorized code execution. {#V-281315}

Severity: medium · Rule: SV-281315r1208802_rule · STIG ID: RHEL-10-701130 · CCI-002824

**Discussion.** ASLR makes it more difficult for an attacker to predict the location of attack code they have introduced into a process's address space during an attempt at exploitation. Additionally, ASLR makes it more difficult for an attacker to know the location of existing code to repurpose it using return-oriented programming techniques.

**Check.**

```
Verify RHEL 10 is implementing ASLR.

Check the status of the "kernel.randomize_va_space" kernel parameter with the following command:

$ sudo sysctl kernel.randomize_va_space
kernel.randomize_va_space = 2

If "kernel.randomize_va_space" is not set to "2", this is a finding.

Check that the configuration files are present to enable this kernel parameter.

$ sudo grep -rs kernel.randomize_va_space /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf
/etc/sysctl.d/99-kernel_randomize_va_space.conf:kernel.randomize_va_space = 2

If "kernel.randomize_va_space" is not set to "2", is missing or commented out, this is a finding.

If conflicting results are returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to implement ASLR.

$ echo 'kernel.randomize_va_space = 2' | sudo tee /etc/sysctl.d/99-kernel_randomize_va_space.conf

Remove any configurations that conflict with the above from the following locations: 

/run/sysctl.d/*.conf
/usr/local/lib/sysctl.d/*.conf
/usr/lib/sysctl.d/*.conf
/lib/sysctl.d/*.conf
/etc/sysctl.conf
/etc/sysctl.d/*.conf

Issue the following command to make the changes take effect:

$ sudo sysctl --system
```

## V-281316 RHEL 10 must restrict usage of ptrace to descendant processes. {#V-281316}

Severity: medium · Rule: SV-281316r1167098_rule · STIG ID: RHEL-10-701140 · CCI-001082

**Discussion.** Unrestricted usage of ptrace allows compromised binaries to run ptrace on other processes of the user. The attacker can then steal sensitive information from the target processes (e.g., SSH sessions, web browser, etc.) without any additional assistance from the user (i.e., without resorting to phishing).

**Check.**

```
Verify RHEL 10 restricts the usage of ptrace to descendant processes.

Check the status of the "kernel.yama.ptrace_scope" kernel parameter with the following command:

$ sysctl kernel.yama.ptrace_scope
kernel.yama.ptrace_scope = 1

If the network parameter "kernel.yama.ptrace_scope" is not equal to "1", or nothing is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to restrict the usage of ptrace to descendant processes.

Create the drop-in if it does not already exist:

$ sudo vi /etc/sysctl.d/99-kernel_yama.ptrace_scope.conf

Add the following line to the file:

kernel.yama.ptrace_scope = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281317 RHEL 10 must disable core dump backtraces. {#V-281317}

Severity: medium · Rule: SV-281317r1167101_rule · STIG ID: RHEL-10-701150 · CCI-000381

**Discussion.** A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers or system operators trying to debug problems.

Enabling core dumps on production systems is not recommended; however, there may be overriding operational requirements to enable advanced debugging. Permitting temporary enablement of core dumps during such situations must be reviewed through local needs and policy.

**Check.**

```
Note: If kernel dumps are disabled in accordance with RHEL-10-701090, this requirement is not applicable.

Verify RHEL 10 disables core dump backtraces by issuing the following command:

$ sudo grep -ir ProcessSizeMax /etc/systemd/ | grep -v '#'
/etc/systemd/coredump.conf:ProcessSizeMax=0

If the "ProcessSizeMax" item is missing or the value is anything other than "0", and the need for core dumps is not documented with the information system security officer as an operational requirement for all domains that have the "core" item assigned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable core dump backtraces.

Create or edit the setting in a drop-in configuration file:

$ sudo vi /etc/systemd/coredump.conf:

Add the following line:

ProcessSizeMax=0
```

## V-281318 RHEL 10 must disable storing core dumps. {#V-281318}

Severity: medium · Rule: SV-281318r1167104_rule · STIG ID: RHEL-10-701160 · CCI-000381

**Discussion.** A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers or system operators trying to debug problems. 

Enabling core dumps on production systems is not recommended; however, there may be overriding operational requirements to enable advanced debugging. Permitting temporary enablement of core dumps during such situations must be reviewed through local needs and policy.

**Check.**

```
Note: If kernel dumps are disabled in accordance with RHEL-10-701090, this requirement is not applicable.

Verify RHEL 10 disables storing core dumps for all users by issuing the following command:

$ sudo grep -ir storage /etc/systemd/ | grep -v '#'
/etc/systemd/coredump.conf:Storage=none

If the "Storage" item is missing or the value is anything other than "none", and the need for core dumps is not documented with the information system security officer as an operational requirement for all domains that have the "core" item assigned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable storing core dumps for all users.

Create or edit the setting in a drop-in configuration file:

$ sudo vi /etc/systemd/coredump.conf

Add the following line:

Storage=none
```

## V-281319 RHEL 10 must disable core dumps for all users. {#V-281319}

Severity: medium · Rule: SV-281319r1184633_rule · STIG ID: RHEL-10-701170 · CCI-000381

**Discussion.** A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.

**Check.**

```
Note: If kernel dumps are disabled in accordance with RHEL-10-701090, this requirement is not applicable.

Verify RHEL 10 disables core dumps for all users by issuing the following command:

$ sudo grep -r core /etc/security/ | grep -v '#'
/etc/security/limits.d/core_dumps.conf:* hard core 0

This can be set as a global domain (with the * wildcard) but may be set differently for multiple domains.

If the "core" item is missing or the value is anything other than "0", and the need for core dumps is not documented with the information system security officer as an operational requirement for all domains that have the "core" item assigned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable core dumps for all users.

Create or edit the setting in a drop-in configuration file:

$ sudo vi /etc/security/limits.d/core_dumps.conf

Add the following line:

* hard core 0

Remove any entries for users or groups with a value set to anything other than "0".
```

## V-281320 RHEL 10 must disable acquiring, saving, and processing core dumps. {#V-281320}

Severity: medium · Rule: SV-281320r1184635_rule · STIG ID: RHEL-10-701180 · CCI-002165

**Discussion.** A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.

**Check.**

```
Note: If kernel dumps are disabled in accordance with RHEL-10-701090, this requirement is not applicable.

Verify RHEL 10 is not configured to acquire, save, or process core dumps with the following command:

$ sudo systemctl status systemd-coredump.socket
o systemd-coredump.socket
    Loaded: masked (Reason: Unit systemd-coredump.socket is masked.)
    Active: inactive (dead)
    ...

If the "systemd-coredump.socket" is loaded and not masked, and the need for core dumps is not documented with the information system security officer as an operational requirement, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable the systemd-coredump.socket with the following command:

$ sudo systemctl mask --now systemd-coredump.socket
Created symlink /etc/systemd/system/systemd-coredump.socket -> /dev/null

Reload the daemon for this change to take effect.

$ sudo systemctl daemon-reload
```

## V-281321 RHEL 10 must implement nonexecutable data to protect its memory from unauthorized code execution. {#V-281321}

Severity: medium · Rule: SV-281321r1167113_rule · STIG ID: RHEL-10-701190 · CCI-002824

**Discussion.** ExecShield uses the segmentation feature on all x86 systems to prevent execution in memory higher than a certain address. It writes an address as a limit in the code segment descriptor, to control where code can be executed, on a per-process basis. When the kernel places a process's memory regions, such as the stack and heap, higher than this address, the hardware prevents execution in that address range. This is enabled by default on the latest Red Hat and Fedora systems if supported by the hardware.

Checking "dmesg" will return a false-positive if the system has generated enough kernel messages that the "(Execute Disable) protection: active" line is no longer present in the output from "dmesg(1)". A better way to ensure that ExecShield is enabled is to first ensure all processors support the NX feature, and then to check that "noexec" was not passed to the kernel command line.

**Check.**

```
Verify RHEL 10 enables ExecShield.

Run the following command:

$ sudo grep ^flags /proc/cpuinfo | grep -Ev '([^[:alnum:]])(nx)([^[:alnum:]]|$)'

If any output is returned, this is a finding.

Run the following command:

$ sudo grubby --info=ALL | grep args | grep -E '([^[:alnum:]])(noexec)([^[:alnum:]])'

If any output is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable ExecShield.

If "/proc/cpuinfo" shows that one or more processors do not enable ExecShield (lack the "nx" feature flag), verify the NX/XD feature is not disabled in the BIOS or UEFI. If it is disabled, enable it.

If the "noexec" option is present on the kernel command line, update the GRUB 2 bootloader configuration to remove it by running the following command:

$ sudo grubby --update-kernel=ALL --remove-args=noexec
```

## V-281322 RHEL 10 must disable the kdump service. {#V-281322}

Severity: medium · Rule: SV-281322r1167116_rule · STIG ID: RHEL-10-701200 · CCI-001665

**Discussion.** Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps consume a considerable amount of disk space and may result in denial of service by exhausting the available space on the target file system partition. Unless the system is used for kernel development or testing, there is little need to run the kdump service.

**Check.**

```
Verify RHEL 10 disables the kdump service in system boot configuration with the following command:

$ sudo systemctl is-enabled  kdump
masked

Verify the kdump service is not active (i.e., not running) through current runtime configuration with the following command:

$ sudo systemctl is-active kdump
failed

Verify the kdump service is masked with the following command:

$ sudo systemctl show  kdump  | grep "LoadState\|UnitFileState"
LoadState=masked
UnitFileState=masked

If the "kdump" service is loaded or active and is not masked, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable and mask the kdump service.

To disable the kdump service, run the following command:

$ sudo systemctl disable --now kdump
Removed '/etc/systemd/system/multi-user.target.wants/kdump.service'.

To mask the kdump service, run the following command:

$ sudo systemctl mask --now kdump
Created symlink '/etc/systemd/system/kdump.service' ? '/dev/null'.
```

## V-281323 RHEL 10 must disable file system automount function. {#V-281323}

Severity: medium · Rule: SV-281323r1273607_rule · STIG ID: RHEL-10-701210 · CCI-000778 CCI-001958

**Discussion.** Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity.

Peripherals include, but are not limited to, such devices as flash drives, external storage, and printers.

Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163

**Check.**

```
Note: If the "autofs" service is not installed, this requirement is not applicable.

Verify RHEL 10 is configured so that the file system automount function has been disabled with the following command:

$ systemctl is-enabled  autofs
not-found

If the returned value is not "masked", "disabled", or "not-found", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to disable the ability to automount devices.

The "autofs" service can be disabled with the following command:

$ sudo systemctl mask --now autofs.service
```

## V-281324 RHEL 10 must enable certificate-based smart card authentication. {#V-281324}

Severity: medium · Rule: SV-281324r1273608_rule · STIG ID: RHEL-10-701220 · CCI-004046 CCI-000765 CCI-000766

**Discussion.** Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. A privileged account is defined as an information system account with authorizations of a privileged user. The DoW Common Access Card (CAC) with DoW-approved public key infrastructure (PKI) is an example of multifactor authentication.

Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055

**Check.**

```
Note: If the system administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable.

Verify RHEL 10 enables smart cards in the System Security Services Daemon (SSSD) with the following command:

$ sudo grep -ir pam_cert_auth /etc/sssd/sssd.conf /etc/sssd/conf.d/
/etc/sssd/conf.d/sssd.conf:pam_cert_auth = True

If "pam_cert_auth" is not set to "True", the line is commented out, or the line is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable certificate-based smart card authentication.

Edit the file "/etc/sssd/sssd.conf" or a configuration file in "/etc/sssd/conf.d" and add or edit the following line:

pam_cert_auth = True
```

## V-281325 RHEL 10 must implement certificate status checking for multifactor authentication. {#V-281325}

Severity: medium · Rule: SV-281325r1273609_rule · STIG ID: RHEL-10-701230 · CCI-004046 CCI-001954 CCI-004047

**Discussion.** Using an authentication device, such as a DoW common access card (CAC) or token that is separate from the information system, ensures that even if the information system is compromised, credentials stored on the authentication device will not be affected.

Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DoW CAC.

RHEL 10 includes multiple options for configuring certificate status checking but for this requirement focuses on the System Security Services Daemon (SSSD). By default, SSSD performs Online Certificate Status Protocol (OCSP) checking and certificate verification using a sha256 digest function.

Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000377-GPOS-00162, SRG-OS-000705-GPOS-00150

**Check.**

```
Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable.

Verify RHEL 10 implements OCSP and is using the proper digest value on the system with the following command:

$ sudo grep -irs certificate_verification /etc/sssd/sssd.conf /etc/sssd/conf.d/ | grep -v "^#"
/etc/sssd/conf.d/certificate_verification.conf:certificate_verification = ocsp_dgst=sha512

If the certificate_verification line is missing from the [sssd] section, or is missing "ocsp_dgst=sha512", ask the SA to indicate what type of multifactor authentication is being used and how the system implements certificate status checking. 

If there is no evidence of certificate status checking being used, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to implement certificate status checking for multifactor authentication.

Review the "/etc/sssd/conf.d/certificate_verification.conf" file to determine if the system is configured to prevent OCSP or certificate verification.

Add the following line to the [sssd] section of the "/etc/sssd/conf.d/certificate_verification.conf" file:

certificate_verification = ocsp_dgst=sha512

Set the correct ownership and permissions on the "/etc/sssd/conf.d/certificate_verification.conf" file by running these commands:

$ sudo chown root:root "/etc/sssd/conf.d/certificate_verification.conf"
$ sudo chmod 600 "/etc/sssd/conf.d/certificate_verification.conf"

Restart the "sssd" service with the following command for the changes to take effect: 

$ sudo systemctl restart sssd.service
```

## V-281326 RHEL 10 must, for PKI-based authentication, enforce authorized access to the corresponding private key. {#V-281326}

Severity: medium · Rule: SV-281326r1184637_rule · STIG ID: RHEL-10-701240 · CCI-000186

**Discussion.** If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure.

The cornerstone of the PKI is the private key used to encrypt or digitally sign information.

If the private key is stolen, this will lead to the compromise of the authentication and nonrepudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user.

Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.

**Check.**

```
Note: If the system administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable.

Verify RHEL 10 SSH private key files have a passcode.

For each private key stored on the system, use the following command:

$ sudo ssh-keygen -y -f /path/to/file

The expected output is a password prompt:
 "Enter passphrase:"

If the password prompt is not displayed, and the contents of the key are displayed, this is a finding.
```

**Fix.**

```
Configure RHEL 10, for PKI-based authentication, enforces authorized access to the corresponding private key.

Create a new private and public key pair that uses a passcode with the following command:

$ sudo ssh-keygen -N [passphrase]
```

## V-281327 RHEL 10 must require authentication to access emergency mode. {#V-281327}

Severity: medium · Rule: SV-281327r1273610_rule · STIG ID: RHEL-10-701250 · CCI-000213

**Discussion.** To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoW-approved PKIs, all DoW systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. 

Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.

This requirement prevents attackers with physical access from trivially bypassing security on the machine and gaining root access. Such accesses are further prevented by configuring the bootloader password.

**Check.**

```
Verify RHEL 10 requires authentication for emergency mode with the following command:

$ sudo grep systemd-sulogin /usr/lib/systemd/system/emergency.service 
# ExecStart=-/usr/lib/systemd/systemd-sulogin-shell emergency

If the line is not returned from the default "systemd" file, use the following command to look for modifications to "emergency.service":

$ sudo grep systemd-sulogin /etc/systemd/system/emergency.service.d/*.conf 
ExecStart=-/usr/lib/systemd/systemd-sulogin-shell emergency

If the line is not returned from either location, this is a finding.

Note: The configuration setting can be in either the default location or the drop-in file but not in both locations.
```

**Fix.**

```
Configure RHEL 10 to require authentication for emergency mode.

Create a directory for supplementary configuration files: 

$ sudo mkdir /etc/systemd/system/emergency.service.d/

Copy the original "emergency.service" file to the new directory with:

$ sudo cp  /usr/lib/systemd/system/emergency.service  /etc/systemd/system/emergency.service.d/emergency.service.conf

Open the new file:

$ sudo vi /etc/systemd/system/emergency.service.d/emergency.service.conf

Add or modify the following line in the new file:

ExecStart=-/usr/lib/systemd/systemd-sulogin-shell emergency

Comment out or remove the ExecStart and ExecStartPre lines in "/usr/lib/systemd/system/emergency.service" as they can only exist in one location.

Apply changes to unit files without rebooting the system:

$ sudo systemctl daemon-reload
```

## V-281328 RHEL 10 must require authentication to access single-user mode. {#V-281328}

Severity: medium · Rule: SV-281328r1273611_rule · STIG ID: RHEL-10-701260 · CCI-000213

**Discussion.** To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoW-approved PKIs, all DoW systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. 

Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.

This requirement prevents attackers with physical access from trivially bypassing security on the machine and gaining root access. Such accesses are further prevented by configuring the bootloader password.

**Check.**

```
Verify RHEL 10 requires authentication for single-user mode with the following command:

$ sudo grep systemd-sulogin /usr/lib/systemd/system/rescue.service
# ExecStart=-/usr/lib/systemd/systemd-sulogin-shell rescue

If the line is not returned from the default "systemd" file, use the following command to look for modifications to "rescue.service":

$ sudo grep systemd-sulogin /etc/systemd/system/rescue.service.d/*.conf 
ExecStart=-/usr/lib/systemd/systemd-sulogin-shell rescue

If the line is not returned from either location, this is a finding.

Note: The configuration setting can be in either the default location or the drop-in file but not in both locations.
```

**Fix.**

```
Configure RHEL 10 to require authentication for single-user mode.

Create a directory for supplementary configuration files: 

$ sudo mkdir /etc/systemd/system/rescue.service.d/

Copy the original "rescue.service" file to the new directory with:

$ sudo cp  /usr/lib/systemd/system/rescue.service  /etc/systemd/system/rescue.service.d/rescue.service.conf

Open the new file:

$ sudo vi /etc/systemd/system/rescue.service.d/rescue.service.conf

Add or modify the following line in the new file:

ExecStart=-/usr/lib/systemd/systemd-sulogin-shell rescue

Comment out or remove the "ExecStart" and "ExecStartPre" lines in "/usr/lib/systemd/system/rescue.service" as they can only exist in one location.

Apply changes to unit files without rebooting the system:

$ sudo systemctl daemon-reload
```

## V-281329 RHEL 10 must, for PKI-based authentication, validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor. {#V-281329}

Severity: medium · Rule: SV-281329r1273613_rule · STIG ID: RHEL-10-701270 · CCI-000185 CCI-004068 CCI-004909 CCI-004910

**Discussion.** Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted.

A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and Domain Name System Security Extensions (DNSSEC).

When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a certification authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA.

This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.

Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000384-GPOS-00167, SRG-OS-000775-GPOS-00230, SRG-OS-000780-GPOS-00240

**Check.**

```
Note: If the system administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable.

Verify RHEL 10, for PKI-based authentication, has valid certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

Check that the system has a valid DOD root CA installed with the following command:

$ sudo openssl x509 -text -in /etc/sssd/pki/sssd_auth_ca_db.pem
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 1 (0x1)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = US, O = U.S. Government, OU = DoW, OU = PKI, CN = DoD Root CA 3
        Validity
        Not Before: Mar 20 18:46:41 2012 GMT
        Not After: Dec 30 18:46:41 2029 GMT
        Subject: C = US, O = U.S. Government, OU = DoW, OU = PKI, CN = DoD Root CA 3
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption

If the root CA file is not a DoW-issued certificate with a valid date and installed in the "/etc/sssd/pki/sssd_auth_ca_db.pem" location, this is a finding.
```

**Fix.**

```
Configure RHEL 10, for PKI-based authentication, to validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

Obtain a valid copy of the DoW root CA file from the PKI CA certificate bundle from cyber.mil and copy the DoW_PKE_CA_chain.pem into the following file:

/etc/sssd/pki/sssd_auth_ca_db.pem
```

## V-281330 RHEL 10 must map the authenticated identity to the user or group account for public key infrastructure (PKI)-based authentication. {#V-281330}

Severity: medium · Rule: SV-281330r1167140_rule · STIG ID: RHEL-10-701280 · CCI-000187

**Discussion.** Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.

**Check.**

```
Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable.

Verify RHEL 10 maps the authenticated identity to the user or group account for PKI-based authentication.

Verify the certificate of the user or group is mapped to the corresponding user or group in the "sssd.conf" file with the following command:

$ sudo find /etc/sssd/sssd.conf /etc/sssd/conf.d/ -type f -exec cat {} \;
[certmap/testing.test/rule_name]
matchrule =<SAN>.*EDIPI@mil
maprule = (userCertificate;binary={cert!bin})
domains = testing.test

If the certmap section does not exist, ask the SA to indicate how certificates are mapped to accounts.

If there is no evidence of certificate mapping, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to map the authenticated identity to the user or group account by adding or modifying the certmap section of the "/etc/sssd/sssd.conf" file based on the following example:

[certmap/testing.test/rule_name]
matchrule = .*EDIPI@mil
maprule = (userCertificate;binary={cert!bin})
domains = testing.test

Restart the "sssd" service with the following command for the changes to take effect:

$ sudo systemctl restart sssd.service
```

## V-281331 RHEL 10 must prohibit the use of cached authenticators after one day. {#V-281331}

Severity: medium · Rule: SV-281331r1167143_rule · STIG ID: RHEL-10-701290 · CCI-002007

**Discussion.** If cached authentication information is out of date, the validity of the authentication information may be questionable.

**Check.**

```
Verify RHEL 10 System Security Services Daemon (SSSD) prohibits the use of cached authentications after one day with the following command:

Note: Cached authentication settings should be configured even if smart card authentication is not used on the system.

Determine if SSSD allows cached authentications with the following command:

$ sudo grep -irs cache_credentials /etc/sssd/sssd.conf /etc/sssd/conf.d/ | grep -v "^#"
cache_credentials = true

If "cache_credentials" is set to "false" or missing from the configuration file, this is not a finding and no further checks are required.

If "cache_credentials" is set to "true", check that SSSD prohibits the use of cached authentications after one day with the following command:

$ sudo grep -irs offline_credentials_expiration /etc/sssd/sssd.conf /etc/sssd/conf.d/ | grep -v "^#"
offline_credentials_expiration = 1

If "offline_credentials_expiration" is not set to a value of "1", this is a finding.
```

**Fix.**

```
Configure RHEL 10 SSSD to prohibit the use of cached authentications after one day.

Edit the file "/etc/sssd/sssd.conf" or a configuration file in "/etc/sssd/conf.d" and add or edit the following line just below the line [pam]:

offline_credentials_expiration = 1

Restart the "sssd" service with the following command for the changes to take effect: 

$ sudo systemctl restart sssd.service
```

## V-281332 RHEL 10 must control remote access methods. {#V-281332}

Severity: medium · Rule: SV-281332r1167146_rule · STIG ID: RHEL-10-800000 · CCI-000382 CCI-002314

**Discussion.** To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems.

Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by one component.

To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business.

Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115

**Check.**

```
Verify RHEL 10 controls remote access methods by inspecting the firewall configuration.

Inspect the list of enabled firewall ports and verify they are configured correctly by running the following command:

$ sudo firewall-cmd --list-all

Ask the system administrator for the site or program Ports, Protocols, and Services Management Component Local Service Assessment (PPSM CLSA). Verify the services allowed by the firewall match the PPSM CLSA.

If there are additional ports, protocols, or services that are not in the PPSM CLSA, or there are ports, protocols, or services that are prohibited by the PPSM Category Assurance List (CAL), or there are no firewall rules configured, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to allow approved settings and/or running services to comply with the PPSM CLSA for the site or program and the PPSM CAL.

To open a port for a service, configure "firewalld" using the following command:

$ sudo firewall-cmd --permanent --add-port=port_number/tcp
or
$ sudo firewall-cmd --permanent --add-service=service_name
```

## V-281333 RHEL 10 must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the Ports, Protocols, and Services Management (PPSM) Category Assignments List (CAL) and vulnerability assessments. {#V-281333}

Severity: medium · Rule: SV-281333r1167149_rule · STIG ID: RHEL-10-800010 · CCI-000382

**Discussion.** To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary ports, protocols, and services on information systems.

**Check.**

```
Verify RHEL 10 is configured to prohibit or restrict the use of functions, ports, protocols, and/or services as defined in the PPSM CAL and vulnerability assessments.

Inspect the firewall configuration and running services to verify they are configured to prohibit or restrict the use of functions, ports, protocols, and/or services that are unnecessary or prohibited.

Check which services are currently active with the following command:

$ sudo firewall-cmd --list-all-zones

Ask the system administrator for the site or program PPSM Component Local Service Assessment (CLSA). Verify the services allowed by the firewall match the PPSM CLSA.

If there are additional ports, protocols, or services that are not in the PPSM CLSA, or there are ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prohibit or restrict the use of functions, ports, protocols, and/or services as defined in the PPSM CAL and vulnerability assessments.

Update the host's firewall settings and/or running services to comply with the PPSM CLSA for the site or program and the PPSM CAL.

Run the following command to load the newly created rule(s):

$ sudo firewall-cmd --reload
```

## V-281334 RHEL 10 must enforce that network interfaces not be in promiscuous mode. {#V-281334}

Severity: medium · Rule: SV-281334r1167152_rule · STIG ID: RHEL-10-800020 · CCI-002418

**Discussion.** Network interfaces in promiscuous mode allow for the capture of all network traffic visible to the system. If unauthorized individuals can access these applications, it may allow them to collect information such as login IDs, passwords, and key exchanges between systems.

If the system is being used to perform a network troubleshooting function, the use of these tools must be documented with the information systems security officer (ISSO) and restricted to authorized personnel only.

**Check.**

```
Verify RHEL 10 network interfaces are not in promiscuous mode with the following command:

$ sudo ip link | grep -i promisc

If network interfaces are found on the system in promiscuous mode and their use has not been approved by the ISSO and documented, this is a finding.
```

**Fix.**

```
Configure RHEL 10 network interfaces to turn off promiscuous mode unless approved by the ISSO and documented.

Set the promiscuous mode of an interface to "off" with the following command:

$ sudo ip link set dev <devicename> multicast off promisc off
```

## V-281335 RHEL 10 must disable access to the network bpf system call from nonprivileged processes. {#V-281335}

Severity: medium · Rule: SV-281335r1167155_rule · STIG ID: RHEL-10-800030 · CCI-001082

**Discussion.** Loading and accessing the packet filters programs and maps using the bpf() system call has the potential to reveal sensitive information about the kernel state.

**Check.**

```
Verify RHEL 10 prevents privilege escalation through the kernel by disabling access to the bpf system call.

Check the status of the "kernel.unprivileged_bpf_disabled" kernel parameter with the following command:

$ sysctl kernel.unprivileged_bpf_disabled
kernel.unprivileged_bpf_disabled = 1

If "kernel.unprivileged_bpf_disabled" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent privilege escalation through the kernel by disabling access to the bpf system call.

Create the drop-in file if it does not already exist:

$ sudo vi /etc/sysctl.d/99-kernel_unprivileged_bpf_disabled

Add the following line to the file:

kernel.unprivileged_bpf_disabled = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281336 RHEL 10 must securely compare internal information system clocks at least every 24 hours. {#V-281336}

Severity: medium · Rule: SV-281336r1273614_rule · STIG ID: RHEL-10-800040 · CCI-004923 CCI-004926 CCI-001890 CCI-004922

**Discussion.** Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate.

Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.

Depending on the infrastructure being used, the "pool" directive may not be supported.

Authoritative time sources include the United States Naval Observatory (USNO) time servers, a time server designated for the appropriate DoW network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

Satisfies: SRG-OS-000355-GPOS-00143, SRG-OS-000356-GPOS-00144, SRG-OS-000359-GPOS-00146, SRG-OS-000785-GPOS-00250

**Check.**

```
Verify RHEL 10 is securely comparing internal information system clocks at least every 24 hours with an NTP server with the following commands:

$ sudo grep maxpoll /etc/chrony.conf
server 0.us.pool.ntp.mil iburst maxpoll 16

If the "maxpoll" option is set to a number greater than 16, or the line is missing or commented out, this is a finding.

Verify the "chrony.conf" file is configured to an authoritative DoW time source by running the following command:

$ sudo grep -i server /etc/chrony.conf
server 0.us.pool.ntp.mil

If the parameter "server" is not set or is not set to an authoritative DoW time source, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to securely compare internal information system clocks at least every 24 hours with an NTP server by adding/modifying the following line in the "/etc/chrony.conf" file:

server [ntp.server.name] iburst maxpoll 16
```

## V-281337 RHEL 10 must enable hardening for the Berkeley Packet Filter (BPF) just-in-time compiler. {#V-281337}

Severity: medium · Rule: SV-281337r1167161_rule · STIG ID: RHEL-10-800050 · CCI-002824

**Discussion.** When hardened, the extended BPF just-in-time (JIT) compiler will randomize any kernel addresses in the BPF programs and maps, and will not expose the JIT addresses in "/proc/kallsyms".

**Check.**

```
Verify RHEL 10 enables hardening for the BPF JIT compiler.

Check the status of the "net.core.bpf_jit_harden" parameter with the following command:

$ sudo sysctl net.core.bpf_jit_harden
net.core.bpf_jit_harden = 2

If "net.core.bpf_jit_harden" is not equal to "2" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to enable hardening for the BPF JIT compiler.

Create the drop-in file if it does not already exist:

$ sudo vi /etc/sysctl.d/99-net_core-bpf_jit_harden.conf

Add the following line to the file:

net.core.bpf_jit_harden = 2

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281338 RHEL 10 must have at least two name servers configured for systems using Domain Name Server (DNS) resolution. {#V-281338}

Severity: medium · Rule: SV-281338r1167164_rule · STIG ID: RHEL-10-800060 · CCI-002385

**Discussion.** To provide availability for name resolution services, multiple redundant name servers are mandated. A failure in name resolution could lead to the failure of security functions requiring name resolution, which may include time synchronization, centralized authentication, and remote system logging.

**Check.**

```
Note: If the system is running in a cloud platform and the cloud provider gives a single, highly available IP address for DNS configuration, this control is not applicable.

Verify RHEL 10 has at least two name servers configured for systems using DNS resolution.

Verify the name servers used by the system with the following command:

$ sudo grep nameserver /etc/resolv.conf
nameserver 192.168.1.2
nameserver 192.168.1.3

If fewer than two lines are returned that are not commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use two or more name servers for DNS resolution based on the DNS mode of the system.

If the NetworkManager DNS mode is set to "none", add the following lines to "/etc/resolv.conf":

nameserver [name server 1]
nameserver [name server 2]

Replace [name server 1] and [name server 2] with the IPs of two different DNS resolvers.

If the NetworkManager DNS mode is set to "default", add two DNS servers to a NetworkManager connection using the following command:

$ nmcli connection modify [connection name] ipv4.dns [name server 1],[name server 2]

Replace [name server 1] and [name server 2] with the IPs of two different DNS resolvers.

Replace [connection name] with a valid NetworkManager connection name on the system. 

Replace ipv4 with ipv6 if IPv6 DNS servers are used.
```

## V-281339 RHEL 10 must not have unauthorized IP tunnels configured. {#V-281339}

Severity: medium · Rule: SV-281339r1268226_rule · STIG ID: RHEL-10-800070 · CCI-000213

**Discussion.** IP tunneling mechanisms can be used to bypass network filtering. If tunneling is required, it must be documented with the information system security officer (ISSO).

**Check.**

```
Verify RHEL 10 does not have unauthorized IP tunnels configured.

Determine if the IPsec service is active with the following command:

$ systemctl is-active ipsec
Inactive

If the IPsec service is active, check for configured IPsec connections ("conn"), with the following command:

$ sudo grep -rni conn /etc/ipsec.conf /etc/ipsec.d/

Verify any returned results are documented with the ISSO.

If the IPsec tunnels are active and not approved, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not have unauthorized IP tunnels configured.

Remove all unapproved tunnels from the system, or document them with the ISSO.
```

## V-281340 RHEL 10 must be configured to use Transmission Control Protocol (TCP) syncookies. {#V-281340}

Severity: medium · Rule: SV-281340r1167170_rule · STIG ID: RHEL-10-800080 · CCI-002385 CCI-001095

**Discussion.** Denial of service (DoS) is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity.

Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00071

**Check.**

```
Verify RHEL 10 is configured to use Internet Protocol version 4 (IPv4) TCP syncookies.

Check the value of all "net.ipv4.tcp_syncookies" variables with the following command:

$ sudo sysctl net.ipv4.tcp_syncookies
net.ipv4.tcp_syncookies = 1

If the network parameter "ipv4.tcp_syncookies" is not equal to "1", or nothing is returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use TCP syncookies.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/99-ipv4_tcp_syncookies.conf

Add the following line to the file:

net.ipv4.tcp_syncookies = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281341 RHEL 10 must ignore Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages. {#V-281341}

Severity: medium · Rule: SV-281341r1167173_rule · STIG ID: RHEL-10-800090 · CCI-002385 CCI-001096

**Discussion.** ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.

This feature of the IPv4 protocol has few legitimate uses. It should be disabled unless absolutely required.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00072

**Check.**

```
Verify RHEL 10 will not accept IPv4 ICMP redirect messages.

Check the value of all "net.ipv4.conf.all.accept_redirects" variables with the following command:

$ sudo sysctl net.ipv4.conf.all.accept_redirects
net.ipv4.conf.all.accept_redirects = 0

If "net.ipv4.conf.all.accept_redirects" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to ignore IPv4 ICMP redirect messages.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/99-ipv4_accept_redirects.conf

Add the following line to the file:

net.ipv4.conf.all.accept_redirects = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281342 RHEL 10 must not forward Internet Protocol version 4 (IPv4) source-routed packets. {#V-281342}

Severity: medium · Rule: SV-281342r1167176_rule · STIG ID: RHEL-10-800100 · CCI-002385 CCI-001097

**Discussion.** Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4 forwarding is enabled and the system is functioning as a router.

Accepting source-routed packets in the IPv4 protocol has few legitimate uses. It must be disabled unless it is absolutely required.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00073

**Check.**

```
Verify RHEL 10 will not accept IPv4 source-routed packets.

Check the value of the "net.ipv4.conf.all.accept_source_route" variable with the following command:

$ sudo sysctl net.ipv4.conf.all.accept_source_route
net.ipv4.conf.all.accept_source_route = 0

If "net.ipv4.conf.all.accept_source_route" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to ignore IPv4 source-routed packets.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/99-ipv4_accept_source.conf

Add the following line to the file:

net.ipv4.conf.all.accept_source_route = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281343 RHEL 10 must log Internet Protocol version 4 (IPv4) packets with impossible addresses. {#V-281343}

Severity: medium · Rule: SV-281343r1167179_rule · STIG ID: RHEL-10-800110 · CCI-002385 CCI-001098

**Discussion.** The presence of "martian" packets (which have impossible addresses), as well as spoofed packets, source-routed packets, and redirects, could be a sign of nefarious network activity. Logging these packets enables this activity to be detected.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00074

**Check.**

```
Verify RHEL 10 logs IPv4 martian packets.

Check the value of the "net.ipv4.conf.all.log_martians" variable with the following command:

$ sudo sysctl net.ipv4.conf.all.log_martians
net.ipv4.conf.all.log_martians = 1

If "net.ipv4.conf.all.log_martians" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to log martian packets on IPv4 interfaces.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/99-ipv4_log_martians.conf

Add the following line to the file:

net.ipv4.conf.all.log_martians=1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281344 RHEL 10 must log Internet Protocol version 4 (IPv4) packets with impossible addresses by default. {#V-281344}

Severity: medium · Rule: SV-281344r1167182_rule · STIG ID: RHEL-10-800120 · CCI-002385 CCI-001099

**Discussion.** The presence of "martian" packets (which have impossible addresses) as well as spoofed packets, source-routed packets, and redirects, could be a sign of nefarious network activity. Logging these packets enables this activity to be detected.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00075

**Check.**

```
Verify RHEL 10 logs IPv4 martian packets by default.

Check the value of the "net.ipv4.conf.default.log_martians" variable with the following command:

$ sudo sysctl net.ipv4.conf.default.log_martians
net.ipv4.conf.default.log_martians = 1

If "net.ipv4.conf.default.log_martians" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to log martian packets on IPv4 interfaces by default.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/99-ipv4_log_martians.conf

Add the following line to the file:

net.ipv4.conf.default.log_martians=1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281345 RHEL 10 must use reverse path filtering on all Internet Protocol version 4 (IPv4) interfaces. {#V-281345}

Severity: medium · Rule: SV-281345r1167185_rule · STIG ID: RHEL-10-800130 · CCI-002385 CCI-001100

**Discussion.** Enabling reverse path filtering drops packets with source addresses that should not have been able to be received on the interface on which they were received. It must not be used on systems that are routers for complicated networks but is helpful for end hosts and routers serving small networks.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00076

**Check.**

```
Verify RHEL 10 uses reverse path filtering on all IPv4 interfaces.

Check the value of the "net.ipv4.conf.all.rp_filter" variable with the following command:

$ sudo sysctl net.ipv4.conf.all.rp_filter
net.ipv4.conf.all.rp_filter = 1

If "net.ipv4.conf.all.rp_filter" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use reverse path filtering on all IPv4 interfaces.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/99-ipv4_rp_filter.conf

Add the following line to the file:

net.ipv4.conf.all.rp_filter = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281346 RHEL 10 must prevent Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages from being accepted. {#V-281346}

Severity: medium · Rule: SV-281346r1197251_rule · STIG ID: RHEL-10-800140 · CCI-002385 CCI-001101

**Discussion.** ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.

This feature of the IPv4 protocol has few legitimate uses. It must be disabled unless absolutely required.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00077

**Check.**

```
Verify RHEL 10 will not accept IPv4 ICMP redirect messages.

Check the value of the default "net.ipv4.conf.default.accept_redirects" variable with the following command:

$ sudo sysctl net.ipv4.conf.default.accept_redirects
net.ipv4.conf.default.accept_redirects = 0

If "net.ipv4.conf.default.accept_redirects" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent IPv4 ICMP redirect messages from being accepted.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/99-ipv4_accept_redirects.conf

Add the following line to the file:

net.ipv4.conf.default.accept_redirects = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281347 RHEL 10 must not forward Internet Protocol version 4 (IPv4) source-routed packets by default. {#V-281347}

Severity: medium · Rule: SV-281347r1167191_rule · STIG ID: RHEL-10-800150 · CCI-002385 CCI-001102

**Discussion.** Source-routed packets allow the source of the packet to suggest routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures.

Accepting source-routed packets in the IPv4 protocol has few legitimate uses. It must be disabled unless it is absolutely required, such as when IPv4 forwarding is enabled and the system is legitimately functioning as a router.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00078

**Check.**

```
Verify RHEL 10 does not accept IPv4 source-routed packets by default.

Check the value of the "net.ipv4.conf.default.accept_source_route" variable with the following command:

$ sudo sysctl net.ipv4.conf.default.accept_source_route
net.ipv4.conf.default.accept_source_route = 0

If "net.ipv4.conf.default.accept_source_route" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not forward IPv4 source-routed packets by default.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/99-ipv4_accept_source_route.conf

Add the following line to the file:

net.ipv4.conf.default.accept_source_route = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281348 RHEL 10 must use a reverse-path filter for Internet Protocol version 4 (IPv4) network traffic when possible by default. {#V-281348}

Severity: medium · Rule: SV-281348r1167194_rule · STIG ID: RHEL-10-800160 · CCI-002385 CCI-001103

**Discussion.** Enabling reverse path filtering drops packets with source addresses that should not have been able to be received on the interface on which they were received. It must not be used on systems that are routers for complicated networks but is helpful for end hosts and routers serving small networks.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00079

**Check.**

```
Verify RHEL 10 uses reverse path filtering on IPv4 interfaces.

Check the value of the "net.ipv4.conf.default.rp_filter" with the following command:

$ sudo sysctl net.ipv4.conf.default.rp_filter
net.ipv4.conf.default.rp_filter = 1

If the returned line does not have a value of "1", or a line is not returned, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to use reverse path filtering on IPv4 interfaces by default.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv4_rp_filter.conf

Add the following line to the file:

net.ipv4.conf.default.rp_filter = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281349 RHEL 10 must not respond to Internet Control Message Protocol (ICMP) echoes sent to a broadcast address. {#V-281349}

Severity: medium · Rule: SV-281349r1167197_rule · STIG ID: RHEL-10-800170 · CCI-002385 CCI-001104

**Discussion.** Responding to broadcast (ICMP) echoes facilitates network mapping and provides a vector for amplification attacks.

Ignoring ICMP echo requests (pings) sent to broadcast or multicast addresses makes the system slightly more difficult to enumerate on the network.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00080

**Check.**

```
Verify RHEL 10 ignores ICMP echoes sent to a broadcast address.

Check the value of the "net.ipv4.icmp_echo_ignore_broadcasts" variable with the following command:

$ sudo sysctl net.ipv4.icmp_echo_ignore_broadcasts
net.ipv4.icmp_echo_ignore_broadcasts = 1

If "net.ipv4.icmp_echo_ignore_broadcasts" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to ignore Internet Protocol version 4 (IPv4) ICMP echoes sent to a broadcast address.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv4_icmp_echo_ignore_broadcasts.conf

Add the following line to the file:

net.ipv4.icmp_echo_ignore_broadcasts = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281350 RHEL 10 must limit the number of bogus Internet Control Message Protocol (ICMP) response errors logs. {#V-281350}

Severity: medium · Rule: SV-281350r1167200_rule · STIG ID: RHEL-10-800180 · CCI-002385 CCI-001105

**Discussion.** Some routers will send responses to broadcast frames that violate RFC-1122, which fills up a log file system with many useless error messages. An attacker may take advantage of this and attempt to flood the logs with bogus error logs. Ignoring bogus ICMP error responses reduces log size, although some activity would not be logged.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00081

**Check.**

```
Verify RHEL 10 limits the number of bogus ICMP response errors logs.

Check the value of the "net.ipv4.icmp_ignore_bogus_error_response" variables with the following command:

$ sudo sysctl net.ipv4.icmp_ignore_bogus_error_responses
net.ipv4.icmp_ignore_bogus_error_responses = 1

If "net.ipv4.icmp_ignore_bogus_error_response" is not set to "1" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not log bogus ICMP errors.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv4_icmp_ignore_bogus_error_responses.conf

Add the following line to the file:

net.ipv4.icmp_ignore_bogus_error_responses = 1

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281351 RHEL 10 must not send Internet Control Message Protocol (ICMP) redirects. {#V-281351}

Severity: medium · Rule: SV-281351r1184698_rule · STIG ID: RHEL-10-800190 · CCI-002385 CCI-001106

**Discussion.** ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology.

The ability to send ICMP redirects is only appropriate for systems acting as routers.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00082

**Check.**

```
Verify RHEL 10 does not send IPv4 ICMP redirect messages.

Check the value of the "net.ipv4.conf.all.send_redirects" variables with the following command:

$ sudo sysctl net.ipv4.conf.all.send_redirects
net.ipv4.conf.all.send_redirects = 0

If "net.ipv4.conf.all.send_redirects" is not set to "0" and is not documented with the information system security officer as an operational requirement or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not send IPv4 ICMP redirect messages.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv4_send_redirects.conf

Add the following line to the file:

net.ipv4.conf.all.send_redirects = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281352 RHEL 10 must not allow interfaces to perform Internet Control Message Protocol (ICMP) redirects by default. {#V-281352}

Severity: medium · Rule: SV-281352r1184706_rule · STIG ID: RHEL-10-800200 · CCI-002385 CCI-001107

**Discussion.** ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology.

The ability to send ICMP redirects is only appropriate for systems acting as routers.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00083

**Check.**

```
Verify RHEL 10 does not allow interfaces to perform Internet Protocol version 4 (IPv4) ICMP redirects by default.

Check the value of the "net.ipv4.conf.default.send_redirects" variables with the following command:

$ sudo sysctl net.ipv4.conf.default.send_redirects
net.ipv4.conf.default.send_redirects=0

If "net.ipv4.conf.default.send_redirects" is not set to "0" and is not documented with the information system security officer as an operational requirement or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not allow interfaces to perform IPv4 ICMP redirects by default.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv4_send_redirects.conf

Add the following line to the file:

net.ipv4.conf.default.send_redirects = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281353 RHEL 10 must not enable Internet Protocol version 4 (IPv4) packet forwarding unless the system is a router. {#V-281353}

Severity: medium · Rule: SV-281353r1167209_rule · STIG ID: RHEL-10-800210 · CCI-002385 CCI-001108

**Discussion.** Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this capability is used when not required, system network information may be transmitted unnecessarily across the network.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00084

**Check.**

```
Verify RHEL 10 is not performing IPv4 packet forwarding unless the system is a router.

Check that "net.ipv4.conf.all.forwarding" is disabled using the following command:

$ sudo sysctl net.ipv4.conf.all.forwarding
net.ipv4.conf.all.forwarding = 0

If "net.ipv4.conf.all.forwarding" is not set to "0" and is not documented with the information system security officer as an operational requirement or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not allow IPv4 packet forwarding unless the system is a router.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv4_forwarding.conf

Add the following line to the file:

net.ipv4.conf.all.forwarding = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281354 RHEL 10 must not accept router advertisements on all Internet Protocol version 6 (IPv6) interfaces. {#V-281354}

Severity: medium · Rule: SV-281354r1167212_rule · STIG ID: RHEL-10-800220 · CCI-002385 CCI-001109

**Discussion.** An illicit router advertisement message could result in a man-in-the-middle attack.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00085

**Check.**

```
Note: If IPv6 is disabled on the system, this requirement is not applicable.

Verify RHEL 10 does not accept router advertisements on all IPv6 interfaces, unless the system is a router.

Check that "net.ipv6.conf.all.accept_ra" is set to not accept router advertisements by using the following command:

$ sudo sysctl net.ipv6.conf.all.accept_ra
net.ipv6.conf.all.accept_ra = 0

If "net.ipv6.conf.all.accept_ra" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not accept router advertisements on all IPv6 interfaces, unless the system is a router.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv4_accept_ra.conf

Add the following line to the file:

net.ipv6.conf.all.accept_ra = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281355 RHEL 10 must ignore IPv6 Internet Control Message Protocol (ICMP) redirect messages. {#V-281355}

Severity: medium · Rule: SV-281355r1167215_rule · STIG ID: RHEL-10-800230 · CCI-002385 CCI-001110

**Discussion.** An illicit ICMP redirect message could result in a man-in-the-middle attack.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00086

**Check.**

```
Note: If IPv6 is disabled on the system, this requirement is not applicable.

Verify RHEL 10 ignores IPv6 ICMP redirect messages.

Check the value of the "net.ipv6.conf.all.accept_redirects" variable with the following command:

$ sysctl net.ipv6.conf.all.accept_redirects
net.ipv6.conf.all.accept_redirects = 0

If "net.ipv6.conf.all.accept_redirects" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to ignore Internet Protocol version 6 (IPv6) ICMP redirect messages.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv6_accept_redirects.conf

Add the following line to the file:

net.ipv6.conf.all.accept_redirects = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281356 RHEL 10 must not forward Internet Protocol version 6 (IPv6) source-routed packets. {#V-281356}

Severity: medium · Rule: SV-281356r1167218_rule · STIG ID: RHEL-10-800240 · CCI-002385 CCI-001111

**Discussion.** Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00087

**Check.**

```
Note: If IPv6 is disabled on the system, this requirement is not applicable.

Verify RHEL 10 does not accept IPv6 source-routed packets.

Check the value of the "net.ipv6.conf.all.accept_source_route" variable with the following command:

$ sudo sysctl net.ipv6.conf.all.accept_source_route
net.ipv6.conf.all.accept_source_route = 0

If "net.ipv6.conf.all.accept_source_route" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not accept IPv6 source-routed packets.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv6_accept_source_route.conf

Add the following line to the file:

net.ipv6.conf.all.accept_source_route = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281357 RHEL 10 must not enable Internet Protocol version 6 (IPv6) packet forwarding unless the system is a router. {#V-281357}

Severity: medium · Rule: SV-281357r1167221_rule · STIG ID: RHEL-10-800250 · CCI-002385 CCI-001112

**Discussion.** IP forwarding permits the kernel to forward packets from one network interface to another. The ability to forward packets between two networks is only appropriate for systems acting as routers.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00088

**Check.**

```
Note: If IPv6 is disabled on the system, this requirement is not applicable.

Verify RHEL 10 is not performing IPv6 packet forwarding unless the system is a router.

Check the value of the "net.ipv6.conf.all.forwarding" variable with the following command:

$ sudo sysctl net.ipv6.conf.all.forwarding
net.ipv6.conf.all.forwarding = 0

If "net.ipv6.conf.all.forwarding" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not allow IPv6 packet forwarding unless the system is a router.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv6_forwarding.conf

Add the following line to the file:

net.ipv6.conf.all.forwarding = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281358 RHEL 10 must not accept router advertisements on all Internet Protocol version 6 (IPv6) interfaces by default. {#V-281358}

Severity: medium · Rule: SV-281358r1167224_rule · STIG ID: RHEL-10-800260 · CCI-002385 CCI-001113

**Discussion.** An illicit router advertisement message could result in a man-in-the-middle attack.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00089

**Check.**

```
Note: If IPv6 is disabled on the system, this requirement is not applicable.

Verify RHEL 10 does not accept router advertisements on all IPv6 interfaces by default, unless the system is a router.

Check the value of the "net.ipv6.conf.default.accept_ra" variable with the following command:

$ sudo sysctl net.ipv6.conf.default.accept_ra
net.ipv6.conf.default.accept_ra = 0

If "net.ipv6.conf.default.accept_ra" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not accept router advertisements on all IPv6 interfaces by default, unless the system is a router.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv6_accept_ra.conf

Add the following line to the file:

net.ipv6.conf.default.accept_ra = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281359 RHEL 10 must prevent Internet Protocol version 6 (IPv6) Internet Control Message Protocol (ICMP) redirect messages from being accepted. {#V-281359}

Severity: medium · Rule: SV-281359r1167227_rule · STIG ID: RHEL-10-800270 · CCI-002385 CCI-001114

**Discussion.** ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00090

**Check.**

```
Note: If IPv6 is disabled on the system, this requirement is not applicable.

Verify RHEL 10 prevents IPv6 ICMP redirect messages from being accepted.

Check the value of the "net.ipv6.conf.default.accept_redirects" variables with the following command:

$ sudo sysctl net.ipv6.conf.default.accept_redirects
net.ipv6.conf.default.accept_redirects = 0

If "net.ipv6.conf.default.accept_redirects" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to prevent IPv6 ICMP redirect messages from being accepted.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv6_accept_redirects.conf

Add the following line to the file:

net.ipv6.conf.default.accept_redirects = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281360 RHEL 10 must not forward Internet Protocol version 6 (IPv6) source-routed packets by default. {#V-281360}

Severity: medium · Rule: SV-281360r1167230_rule · STIG ID: RHEL-10-800280 · CCI-002385 CCI-001115

**Discussion.** Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router.

Accepting source-routed packets in the IPv6 protocol has few legitimate uses. It must be disabled unless it is absolutely required.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00091

**Check.**

```
Note: If IPv6 is disabled on the system, this requirement is not applicable.

Verify RHEL 10 does not accept IPv6 source-routed packets by default.

Check the value of the "net.ipv6.conf.default.accept_source_route" variables with the following command:

$ sudo sysctl net.ipv6.conf.default.accept_source_route
net.ipv6.conf.default.accept_source_route = 0

If "net.ipv6.conf.default.accept_source_route" is not set to "0" or is missing, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to not accept IPv6 source-routed packets by default.

Create a configuration file if it does not already exist:

$ sudo vi /etc/sysctl.d/ipv6_accept_source_route.conf

Add the following line to the file:

net.ipv6.conf.default.accept_source_route = 0

Reload settings from all system configuration files with the following command:

$ sudo sysctl --system
```

## V-281361 RHEL 10 must protect against or limit the effects of denial-of-service (DoS) attacks by ensuring that rate-limiting measures on impacted network interfaces are implemented. {#V-281361}

Severity: medium · Rule: SV-281361r1167233_rule · STIG ID: RHEL-10-800290 · CCI-002385

**Discussion.** DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity.

This requirement addresses the configuration of RHEL 10 to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.

**Check.**

```
Verify RHEL 10 protects against or limits the effects of DoS attacks by ensuring rate-limiting measures on impacted network interfaces are implemented.

Check that "nftables" is configured to allow rate limits on any connection to the system with the following command:

$ sudo grep -i firewallbackend /etc/firewalld/firewalld.conf
# FirewallBackend
FirewallBackend=nftables

If "nftables" is not set to "FirewallBackend", this is a finding.
```

**Fix.**

```
Configure RHEL 10 so that "nftables" is the default "firewallbackend" for "firewalld" by adding or editing the following line in "/etc/firewalld/firewalld.conf":

FirewallBackend=nftables

Establish rate-limiting rules based on organization-defined types of DoS attacks on impacted network interfaces.
```

## V-281362 RHEL 10 must configure a DNS processing mode in Network Manager to avoid conflicts with other Domain Name Server (DNS) managers and to not leak DNS queries to untrusted networks. {#V-281362}

Severity: medium · Rule: SV-281362r1167236_rule · STIG ID: RHEL-10-800300 · CCI-002385 CCI-001115

**Discussion.** To ensure that DNS resolver settings are respected, a DNS mode in Network Manager must be configured. The following are common DNS values in "NetworkManager.conf [main]":

- default: NetworkManager will update "/etc/resolv.conf" to reflect the nameservers provided by currently active connections.
- none: NetworkManager will not modify "/etc/resolv.conf". Used when DNS is managed manually or by another service.
- systemd-resolved: Uses "systemd-resolved" to manage DNS.
- dnsmasq: Enables the internal "dnsmasq" plugin.

Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00091

**Check.**

```
Verify RHEL 10 has a DNS mode configured in Network Manager.

$ NetworkManager --print-config
[main]
dns=none

If the dns key under "main" does not exist or is set to "dnsmasq", this is a finding.

Note: If RHEL 10 is configured to use a DNS resolver other than Network Manager, the configuration must be documented and approved by the information system security officer.
```

**Fix.**

```
Configure RHEL 10 to use a DNS mode in Network Manager.

In "/etc/NetworkManager/NetworkManager.conf", add the following line in the "[main]" section:

dns = none

Where <dns processing mode> is default, none, or systemd-resolved.

Network Manager must be reloaded for the change to take effect:

$ sudo systemctl reload NetworkManager
```

## V-281363 RHEL 10 must be configured to operate in secure mode if the Trivial File Transfer Protocol (TFTP) server service is required. {#V-281363}

Severity: medium · Rule: SV-281363r1195454_rule · STIG ID: RHEL-10-800310 · CCI-000197

**Discussion.** Restricting TFTP to a specific directory prevents remote users from copying, transferring, or overwriting system files.

**Check.**

```
Note: If a TFTP server is not installed, this rule is not applicable.

Verify RHEL 10 is configured to operate in secure mode if the TFTP server service is required.

Determine if the TFTP server is installed with the following command:

$ sudo dnf list installed | grep tftp-server
tftp-server.x86_64                                   5.2-48.el10                     @rhel-10-for-x86_64-appstream-rpms

Verify that the TFTP daemon, if "tftp.server" is installed, is configured to operate in secure mode with the following command:

$ systemctl cat tftp.service | grep -i execstart
ExecStart=/usr/sbin/in.tftpd -s /var/lib/tftpboot

Note: The "-s" option ensures that the TFTP server serves only files from the specified directory, which is a security measure to prevent unauthorized access to other parts of the file system.

If the TFTP server is installed, but the TFTP daemon is not configured to operate in secure mode, and tftp is not documented as critical to the mission with the information system security officer, this is a finding.
```

**Fix.**

```
Configure RHEL 10 TFTP to operate in secure mode with the following command:

$ sudo systemctl edit tftp.service

In the editor, enter the following:

[Service]
ExecStart=/usr/sbin/in.tftpd -s /var/lib/tftpboot

After making changes, reload the systemd daemon and restart the TFTP service as follows:

$ sudo systemctl daemon-reload
$ sudo systemctl restart tftp.service
```

## V-281364 RHEL 10 must enforce mode "0640" or less for the "/etc/audit/auditd.conf" file to prevent unauthorized access. {#V-281364}

Severity: medium · Rule: SV-281364r1167242_rule · STIG ID: RHEL-10-900000 · CCI-000171

**Discussion.** Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

**Check.**

```
Verify RHEL 10 enforces the mode of "/etc/audit/auditd.conf" with the following command:

$ sudo stat -c "%a %n" /etc/audit/auditd.conf
640 /etc/audit/auditd.conf

If "/etc/audit/auditd.conf" does not have a mode of "0640", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to set the mode of the "/etc/audit/auditd.conf" file to "0640" with the following command:

$ sudo chmod 0640 /etc/audit/auditd.conf
```

## V-281365 RHEL 10 must prevent unauthorized changes to the audit system. {#V-281365}

Severity: medium · Rule: SV-281365r1167245_rule · STIG ID: RHEL-10-900100 · CCI-000162 CCI-000163 CCI-000164

**Discussion.** Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality.

Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit RHEL 10 system activity.

In immutable mode, unauthorized users cannot execute changes to the audit system to potentially hide malicious activity and then put the audit rules back. A system reboot would be noticeable, and a system administrator could then investigate the unauthorized changes.

Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029

**Check.**

```
Verify the RHEL 10 audit system prevents unauthorized changes with the following command:

$ sudo grep "^\s*[^#]" /etc/audit/audit.rules | tail -1
-e 2

If the audit system is not set to be immutable by adding the "-e 2" option to the end of "/etc/audit/audit.rules", this is a finding.
```

**Fix.**

```
Configure RHEL 10 to protect the audit system from unauthorized changes.

Set the audit rules to be immutable by adding the following line to end of "/etc/audit/rules.d/audit.rules":

-e 2

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```

## V-282965 RHEL 10 must be a vendor-supported release. {#V-282965}

Severity: high · Rule: SV-282965r1197252_rule · STIG ID: RHEL-10-001000 · CCI-003376

**Discussion.** An operating system release is considered "supported" if the vendor continues to provide security patches for the product. With an unsupported release, it will not be possible to resolve security issues discovered in the system software.

Red Hat offers the Extended Update Support (EUS) add-on to a Red Hat Enterprise Linux subscription, for a fee, for customers who wish to standardize on a specific minor release for an extended period.

End-of-life dates for Red Hat Linux 10 releases are as follows:
- Current end of Full Support for Red Hat Linux 10 is 31 May 2030.
- Current end of Maintenance Support for Red Hat Linux 10 is 31 May 2035.
- Current end of Extended Life Cycle Support (ELS) for Red Hat Linux 9 is 31 May 2038.

**Check.**

```
Verify RHEL 10 is a vendor-supported version with the following command:

$ cat /etc/redhat-release
Red Hat Enterprise Linux release 10.0 (Coughlan)

If the installed version of RHEL 10 is not supported, this is a finding.
```

**Fix.**

```
Upgrade to a supported version of RHEL 10.
```

## V-288827 RHEL 10 must implement DoW-approved encryption in the OpenSSL package. {#V-288827}

Severity: high · Rule: SV-288827r1273576_rule · STIG ID: RHEL-10-300085 · CCI-001453

**Discussion.** Without cryptographic integrity protections, information can be altered by unauthorized users without detection.

Remote access (e.g., RDP) is access to DoW nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.

Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.

The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/openssl.config file.

**Check.**

```
Verify the RHEL 10 OpenSSL library is configured to use only ciphers employing FIPS 140-3-approved algorithms with the following command:

$ grep -i opensslcnf.config /etc/pki/tls/openssl.cnf
.include = /etc/crypto-policies/back-ends/opensslcnf.config

If the "opensslcnf.config" is not defined in the "/etc/pki/tls/openssl.cnf" file, this is a finding.
```

**Fix.**

```
Configure the RHEL 10 OpenSSL library to use the systemwide cryptographic policy.

Edit the "/etc/pki/tls/openssl.cnf" and add or modify the following line:

.include = /etc/crypto-policies/back-ends/opensslcnf.config
```

## V-288828 RHEL 10 must generate audit records for successful and unsuccessful uses of the "useradd" command. {#V-288828}

Severity: medium · Rule: SV-288828r1273583_rule · STIG ID: RHEL-10-500605 · CCI-000130

**Discussion.** Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way.

The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary because these affect performance. More rules lead to poorer performance. The performance can be helped, however, by combining system calls into one rule whenever possible.

Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210

**Check.**

```
Verify RHEL 10 is configured to audit the execution of the "useradd" command with the following command:

$ sudo auditctl -l | grep useradd
-a always,exit -S all -F path=/usr/sbin/useradd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-useradd

If the command does not return a line, or the line is commented out, this is a finding.
```

**Fix.**

```
Configure RHEL 10 to generate audit records upon successful and unsuccessful attempts to use the "useradd " command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/useradd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-useradd

Restart the audit daemon with the following command for the changes to take effect:

$ sudo service auditd restart
```
