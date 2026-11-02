---
{"title": "Signed kernel modules", "url": "https://wiki.archlinux.org/title/Signed_kernel_modules", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Signed kernel modules

Related articles

-   [Kernel](../en/Kernel.html "Kernel")
-   [Kernel module](../en/Kernel_module.html "Kernel module")
-   [Kernel/Arch Build System](../en/Kernel/Arch_Build_System.html "Kernel/Arch Build System")

[Signed](https://docs.kernel.org/admin-guide/module-signing.html) [kernel modules](../en/Kernel_modules.html "Kernel modules") provide a mechanism for the kernel to verify the integrity of a module.

## Overview {#Overview}

The Linux kernel distinguishes and keeps separate the verification of modules from requiring or forcing modules to verify before allowing them to be loaded. Kernel modules fall into 2 classes:

-   Standard *in-tree* modules which come with the kernel source code. They are compiled during the normal kernel build.
-   *Out-of-tree* modules which are not part of the kernel source distribution. They are built outside of the kernel tree, requiring the kernel headers package for each kernel they are to be built for. They can be built manually for a specific kernel and packaged, or they can be built whenever needed using [DKMS](../en/Dynamic_Kernel_Module_Support.html "DKMS").

During a standard kernel compilation, the kernel build tools create a private/public key pair and sign every in-tree module (using the private key). The public key is saved in the kernel itself. When a module is subsequently loaded, the public key can then be used to verify that the module is unchanged.

The kernel can be enabled to always verify modules and report any failures to standard logs. The choice to permit the loading and use of a module which could not be verified can be either compiled into kernel or turned on at runtime using a [kernel parameter](../en/Kernel_parameter.html "Kernel parameter") as explained below.

## Summary of what needs to be done {#Summary_of_what_needs_to_be_done}

The starting point is based on a custom kernel package as outlined in [Kernel/Arch build system](../en/Kernel/Arch_build_system.html "Kernel/Arch build system"). We will modify the build to sign the standard in-tree kernel modules and to provide the prerequisites for signing and verifying out-of-tree modules.

**Note**

The goal is to have:

-   In-tree modules signed during the standard kernel build process. The standard kernel build creates a fresh public/private key pair on each build.
-   Out-of-tree modules are signed and the associated public key is compiled into the kernel. We will create a separate public/private key pair on each build.

Each kernel build needs to made aware of the key pair to be used for signing out-of-tree modules. A kernel configuration parameter is now used to make the kernel aware of additional signing keys: `CONFIG_SYSTEM_TRUSTED_KEYS="/path/to/oot-signing_keys.pem"`.

Keys and signing tools will be stored in the current module build directory. Nothing needs to be done to clean this as removal is handled by the standard module cleanup. The private and public keys are both installed in `/usr/lib/modules/`*`kernel_version`*`-`*`build`*`/certs-local`.

## Kernel configuration {#Kernel_configuration}

`CONFIG_SYSTEM_TRUSTED_KEYS` will be updated automatically using the script `genkeys.py` provided below. In addition, the following configuration options should be set either manually by editing the `.config` file, or via `make menuconfig` in the Linux `src` directory and subsequently copying the updated `.config` file back to the build file `config`. It is preferable to use elliptic curve type keys and zstd compression.

    CONFIG_MODULE_SIG=y
      Enable Loadable module suppot --->
      Module Signature Verification           -  activate

    CONFIG_MODULE_SIG_FORCE=n
      Require modules to be validly signed -> leave off (for now)

            This allows the decision to enforce verified modules only as boot command line.
            If you are comfortable all is working then by all means change this to 'y'
            Command line version of this is : module.sig_enforce=1

    CONFIG_MODULE_SIG_HASH=sha512
      Automatically sign all modules  - activate
      Which hash algorithm    -> SHA-512
      openssl 3.2+ and kernel 6.7+ bring support for SHA3-xxx (e.g. SHA3-512)
      
    CONFIG_MODULE_COMPRESS_ZSTD=y
      Compress modules on installation        - activate
      Compression algorithm (ZSTD)

    CONFIG_MODULE_SIG_KEY_TYPE_ECDSA=y
      Cryptographic API --->
      Certificates for Signature Checking --->
      Type of module signing key to be generated -> ECDSA

    CONFIG_MODULE_ALLOW_MISSING_NAMESPACE_IMPORTS=n
      Enable Loadable module support --->
      Allow loading of modules with missing namespace imports - set to no

### Kernel command line {#Kernel_command_line}

When you have confirmed that the modules are being signed and that the kernel works as it should, you can enable the following [kernel parameter](../en/Kernel_parameter.html "Kernel parameter") to require that the kernel only permits verified modules to be loaded:

    module.sig_enforce=1

Before forcing verified modules on, please confirm that the system logs do not show any module signature failures being reported.

## Tools needed {#Tools_needed}

### kernel build package {#kernel_build_package}

In the directory where the kernel package is built:

    $ mkdir certs-local

This directory will provide the tools to create the keys, as well as signing kernel modules.

Put these files into `certs-local`:

-   `x509.oot.genkey`
-   `genkeys.py`
-   `install-certs.py`
-   `sign_module.py`
-   `lib/arg_parse.py`
-   `lib/refresh_needed.py`
-   `lib/class_genkeys.py`
-   `lib/get_key_hash.py`
-   `lib/signer_class.py`
-   `lib/update_config.py`
-   `lib/utils.py`

**Note** These files are available from the links provided in [#Files required](#Files_required).

The file `genkeys.py` and its companion configuration file `x509.oot.genkey` are used to create key pairs.

`genkeys.py` also provides the kernel with the key information by updating the configuration file(s) used to build the kernel.

The script `sign_module.py` signs out-of-tree kernel modules. It can be run manually and is invoked by `dkms/kernel-sign.sh`. It handles modules compressed with xzand gzip and depends on python-zstandard to help handle those compressed with zstd.

`genkeys.py` will create the key pairs in a directory named by date-time

`genkeys.py` will check and update kernel configs given by the `--config` config(s) option. It takes either a single config file, or a shell glob for multiple files. e.g. `--config 'conf/config.*'`. All configs will be updated with the same key. The default keytype is ec (elliptic curve) and the default hash is sha512. These can be changed with command line options. See `genkeys.py -h` for more details.

It also creates a soft link `current` to the same directory holding the current key pairs.

`install-certs.py` is to be called from the `package_headers()` function of PKGBUILD to install the signing keys. Example is given below.

### DKMS support {#DKMS_support}

#### Native DKMS method {#Native_DKMS_method}

DKMS natively supports signing built modules, as long as your kernel headers include the `sign-file` program in the `scripts` directory (most archkernel based PKGBUILDs, including the official ones).

You then need to let it know where your signing key and x509 certificate (on a regular Kernel build, these will be in `certs/signing_key.pem` and `certs/signing_key.x509`) are in `/etc/dkms/framework.conf`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/dkms/framework.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# $kernel_source_dir resolves to /lib/modules/`uname -r`/build
mok_signing_key=$kernel_source_dir/certs/signing_key.pem
mok_certificate=$kernel_source_dir/certs/signing_key.x509
```

In this example, it\'ll look into the per-kernel `certs` directory, so either put your signing key/cert there, or if you\'re using a custom PKGBUILD, just install it from the kernel:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
PKGBUILD
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
_package-headers() {
   # ...
   
   # copy signing keys for dkms
   install -Dt "$builddir/certs" -m 400 certs/signing_key.*
}
```

Depending on your level of security paranoia, you definitely don\'t want to distribute these keys, but that goes for the certs-local method as well.

\

#### certs-local method {#certs-local_method}

    $ mkdir certs-local/dkms

Add 2 files to the `dkms` directory:

-   `kernel-sign.conf`
-   `kernel-sign.sh`

These will be installed in `/etc/dkms` and provide the means for DKMS to automatically sign modules using the local key. This is the recommended way to sign out-of-tree kernel modules. As explained below, once this is installed, all that is needed is for DKMS to automatically sign modules is to make a soft link for each module to the configuration file.

    $ cd /etc/dkms
    # ln -s kernel-sign.conf module_name.conf

For example:

    # ln -s kernel-sign.conf vboxdrv.conf

The link creation can easily be added to an arch package to simplify further if desired.

## Modify PKGBUILD {#Modify_PKGBUILD}

We need to make changes to kernel build as follows:

### prepare() {#prepare()}

Add the following to the top of the `prepare()` function:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
PKGBUILD
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
prepare() {

    msg2 "Rebuilding local signing key..."
    ../certs-local/genkeys.py -v --config config

    ... 
}
```

The default key regeneration refresh period is 7 days, but this can be changed on the command line. So if you want to create new keys monthly, then add \"\--refresh 30days\" as an argument to genekeys.py. You can refresh on every build by using \"\--refresh always\". Refresh units can be seconds,minutes,hours,days or weeks.

### \_package-headers() {#package-headers()}

Add the following to the bottom of the `_package-headers()` function:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
PKGBUILD
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
_package-headers() {

    ...

    #
    # Out-of-tree module signing
    # This is run in the kernel source / build directory
    #
    msg2 "Local Signing certs for out-of-tree modules..."

    certs_local_src="../../certs-local" 
    certs_local_dst="${builddir}/certs-local"
    $certs_local_src/install-certs.py $certs_local_dst

    # DKMS tools
    dkms_src="$certs_local_src/dkms"
    dkms_dst="${pkgdir}/etc/dkms"
    mkdir -p $dkms_dst

    rsync -a $dkms_src/{kernel-sign.conf,kernel-sign.sh} $dkms_dst/
}
```

## Files required {#Files_required}

The 5 supporting files referenced above are available for download from the [github.com/gene-git/Arch-SKM](https://github.com/gene-git/Arch-SKM/tree/master) repository:

**Note** There is also an aur version of these files available ([arch-sign-modules](https://aur.archlinux.org/packages/arch-sign-modules/)^AUR^). After building and install they can be found at `/usr/src/certs-local`

-   [certs-local/x509.oot.genkey](https://github.com/gene-git/Arch-SKM/blob/master/certs-local/x509.oot.genkey)
-   [certs-local/genkeys.py](https://github.com/gene-git/Arch-SKM/blob/master/certs-local/genkeys.py)
-   [certs-local/install-certs.py](https://github.com/gene-git/Arch-SKM/blob/master/certs-local/install-certs.py)
-   [certs-local/sign_module.py](https://github.com/gene-git/Arch-SKM/blob/master/certs-local/sign_module.py)
-   [certs-local/lib/signer_class.py](https://github.com/gene-git/Arch-SKM/blob/master/certs-local/lib/signer_class.py)
-   [certs-local/lib/utils.py](https://github.com/gene-git/Arch-SKM/blob/master/certs-local/lib/utils.py)
-   [certs-local/dkms/kernel-sign.conf](https://github.com/gene-git/Arch-SKM/blob/master/certs-local/dkms/kernel-sign.conf)
-   [certs-local/dkms/kernel-sign.sh](https://github.com/gene-git/Arch-SKM/blob/master/certs-local/dkms/kernel-sign.sh)

Remember to ensure that the scripts are [executable](../en/Help:Reading.html#Make_executable "Executable").

## Helper scripts {#Helper_scripts}

**The factual accuracy of this article or section is disputed.**

**Reason:** The [arch-sign-modules](https://aur.archlinux.org/packages/arch-sign-modules/)^AUR^ package comes from a fork of the [Arch-SKM](https://github.com/gene-git/Arch-SKM/tree/master) repository which is used in the previous sections. It is not clear what is wrong with the original repository nor why changes resulted in a fork instead of fixing/improving the original repository. (Discuss in [Talk:Signed kernel modules](../en/Talk:Signed_kernel_modules.html))

[arch-sign-modules](https://aur.archlinux.org/packages/arch-sign-modules/)^AUR^ builds:

-   [linux-hardened](https://archlinux.org/packages/?name=linux-hardened)
-   [linux-lts](https://archlinux.org/packages/?name=linux-lts)
-   [linux-zen](https://archlinux.org/packages/?name=linux-zen)
-   [linux](https://archlinux.org/packages/?name=linux)
-   [linux-libre](https://aur.archlinux.org/packages/linux-libre/)^AUR^

& other AUR kernels.

The ***abk*** helper script reduces the manual steps for building a fully signed custom kernel to 3 commands to ***Update*** / ***Build*** & ***Install*** the kernel:

    abk -u kernel-name
    abk -b kernel-name
    abk -i kernel-name

With signed kernel module support for:

-   [zfs-dkms](https://aur.archlinux.org/packages/zfs-dkms/)^AUR^ [nvidia-beta-dkms](https://aur.archlinux.org/packages/nvidia-beta-dkms/)^AUR^ [lkrg-dkms](https://aur.archlinux.org/packages/lkrg-dkms/)^AUR^ [nvidia-open-dkms](https://archlinux.org/packages/?name=nvidia-open-dkms)
