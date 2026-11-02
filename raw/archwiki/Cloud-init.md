---
{"title": "Cloud-init", "url": "https://wiki.archlinux.org/title/Cloud-init", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Cloud-init

[Cloud-init](https://cloud-init.io/) is a package that contains utilities for early initialization of cloud instances. It is needed in Arch Linux images that are built with the intention of being launched in cloud environments like OpenStack, [AWS](../en/Arch_Linux_AMIs_for_Amazon_Web_Services.html "AWS") etc.

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [cloud-init](https://archlinux.org/packages/?name=cloud-init) package.

If you intend to use the [growpart module](https://cloudinit.readthedocs.io/en/latest/reference/modules.html#growpart) you will also need the [cloud-guest-utils](https://archlinux.org/packages/?name=cloud-guest-utils) package.

## Configuration {#Configuration}

This section only discusses the most basic settings. For a full list of available configuration options, please see the [cloud-init documentation](https://cloudinit.readthedocs.io).

The main configuration file is `/etc/cloud/cloud.cfg`. Optionally, additional `*.cfg` files to be loaded can be placed in `/etc/cloud/cloud.cfg.d`. All of their contents will be [merged](https://cloudinit.readthedocs.io/en/latest/reference/merging.html).

The default configuration shipped with cloud-init 19.3 and later should work out of the box with most major cloud environments. In rough terms, it does the following:

-   Disable the root user, create a user `arch` for logging in
-   Rely on cloud-init\'s built-in detection for data sources
-   Run all modules known to work on Arch Linux

Depending on the use case, the default configuration might need to be adapted.

### Default user configuration {#Default_user_configuration}

The default configuration includes the following contents (comments omitted for brevity):

    users:
       - default

The users to be added to the system. The special name `default` is just a reference to the `default_user` in the `system_info` section (see below), but [the syntax](https://cloudinit.readthedocs.io/en/latest/reference/examples.html#including-users-and-groups) supports configuring arbitrary users with many options. The first user in this list will be considered the \"default\" user by other modules, for example the one that sets up SSH keys passed in from the cloud environment.

    disable_root: true

Disable root SSH access. You may also delete the root user password on the cloud image:

    # passwd -d root

    system_info:
       default_user:
         name: arch
         lock_passwd: true
         gecos: arch Cloud User
         groups: [wheel, adm]
         sudo: ["ALL=(ALL) NOPASSWD:ALL"]
         shell: /bin/bash

This is the specification of the distribution\'s default user:

-   the default user\'s name will be `arch`
-   the default user is password locked, which means you can only log into the instance with the SSH keys configured during boot
-   the default user will be added to the groups `adm` and `wheel`
-   the default user is allowed passwordless `sudo` usage
-   the default user\'s shell is `/bin/bash`

Note that the user specified here will only be created if the special user \"default\" is included in the `users:` section above (or the section is omitted entirely).

### Configuring data sources {#Configuring_data_sources}

Data Sources define how the instance metadata is pulled during boot. This depends on the cloud environment (OpenStack, AWS, OpenNebula etc.) you are running your instance in. Under the hood, this translates to a corresponding module which implements a few methods defined in a common interface.

The default configuration specifies no data sources, which means that cloud-init will attempt to auto-detect the cloud environment. However, some environments cannot be detected or may require special configuration to work. In this case, the data sources to be used can be explictly specified and configured. Refer to the [list of known data sources](https://cloudinit.readthedocs.io/en/latest/reference/datasources.html#known-sources) in the documentation.

To specify a list of data sources to be used in your `/etc/cloud/cloud.cfg` add something like this:

    datasource_list: [ NoCloud, ConfigDrive, OpenNebula, Azure, AltCloud, OVF, MAAS, GCE, OpenStack, CloudSigma, Ec2, CloudStack, None ]

This instructs cloud-init what modules to load while trying to download instance metadata. Optionally further configuration parameters may be passed specific to each datasource as follows:

    datasource:
      OpenStack:
        metadata_urls: [ 'http://169.254.169.254:80' ]
        dsmode: net

The above configuration tells OpenStack datasource to use the url `http://169.254.169.254:80` to download metadata and to run after network initialization, both of which are the default behaviour and may be omitted.

### Modules {#Modules}

Cloud-init comes with a [set of modules](https://cloudinit.readthedocs.io/en/latest/reference/modules.html) that can be enabled or disabled in the configuration. The default configuration enables all modules that are known to work on Arch Linux. Omitted modules include e.g. those specific to other distributions or operating systems.

The fact that a module is enabled usually does not mean that it will actually do anything. It will however check if any configuration relevant to it was passed in, e.g. from the cloud environment via the data source. Only then it will attempt to act. As such, enabling all modules usually helps to maximize compatibility with cloud environments. Nevertheless, modules known to be not needed can be removed from configuration, e.g. to improve start-up times. You can use `cloud-init analyze` on a booted instance to see how much time was spent on individual modules.

Some modules declare to cloud-init which distributions they have been verified for. Even if you specify that you want to run them, they will refuse to run unless the distribution specified in `cloud.cfg` is one of the verified distributions for that module. If you need to override this behavior to run a module on Arch anyway, add the module to the `unverified_modules` section in the cloud config, e.g.:

    unverified_modules: ['ssh-import-id']

## systemd integration {#systemd_integration}

Package cloud-init provides four [systemd.service(5)](https://man.archlinux.org/man/systemd.service.5), two [systemd.target(5)](https://man.archlinux.org/man/systemd.target.5), and a [systemd.generator(7)](https://man.archlinux.org/man/systemd.generator.7), whose dependencies are constructed in a way that they are activated in the sequence listed:

-   `cloud-init-generator`. Determines availability of any data source and enables or disables `cloud-init.target`
-   `cloud-init-local.service`. Only requires the filesystems to be up. Executes `cloud-init init --local`
-   `cloud-init-main.service`. Requires the network to be up. Executes `cloud-init init --all-stages`
-   `cloud-config.target`. Corresponds to the cloud-config upstart event \"to inform third parties that cloud-config is available\"
-   `cloud-config.service`. Executes `cloud-init modules --mode=config`
-   `cloud-final.service`. Executes `cloud-init modules --mode=final`
-   `cloud-init.target`. Reached when all services have been started

The [Uplink Labs EC2 images](../en/Arch_Linux_AMIs_for_Amazon_Web_Services.html "Arch Linux AMIs for Amazon Web Services") have all of them enabled, although that appears to be overkill due to the dependencies. When preparing an image, enabling `cloud-init-main.service` and `cloud-final.service` should be sufficient. Note that this does not mean that the cloud-init services will actually be run - that still depends on the generator enabling the `cloud-init.target` on early boot.

See also the [cloud-init boot stages documentation](https://cloudinit.readthedocs.io/en/latest/explanation/boot.html) for more information.

## Using {#Using}

### Archiso {#Archiso}

**This article or section is a candidate for merging with [Install Arch Linux via SSH#Installation on a headless server](../en/Install_Arch_Linux_via_SSH.html#Installation_on_a_headless_server "Install Arch Linux via SSH").**

**Notes:** It gives more details and illustrates Archiso\'s cloud-init usage on bare metal. (Discuss in [Talk:Cloud-init](../en/Talk:Cloud-init.html))

Here is how to test an [Archiso](../en/Archiso.html "Archiso") with cloud-init (see [archlinux/archiso#27](https://gitlab.archlinux.org/archlinux/archiso/-/issues/27)) using [QEMU](../en/QEMU.html "QEMU"):

Create a `user-data` file in YAML format for cloud-init containing username(s) and public SSH key(s). You can either use the convenient `create_cloud-init.sh` script proposed in [archiso Merge Request #117](https://gitlab.archlinux.org/archlinux/archiso/-/merge_requests/117/diffs), or just hand write as below, as-is or adding any [additional options shown on the cloud-init documentation](https://cloudinit.readthedocs.io/en/latest/reference/examples.html). Beware that the `#cloud-config` is NOT a YAML comment, but is required to be present by cloud-init.

    #cloud-config
    users:
      - name: vorburger
        ssh_authorized_keys:
          - ssh-rsa (...)

We can use `meta-data` as well, but do not have to, so we can just make that an empty file (but it has to exist):

    $ touch meta-data

Then build a `cloud-init.iso` containing (only) the `user-data` and `meta-data` using *xorriso* from [libisoburn](https://archlinux.org/packages/?name=libisoburn):

    $ xorriso -as genisoimage -output cloud-init.iso -volid CIDATA -joliet -rock user-data meta-data

Now add this `cloud-init.iso` as an additional second drive to the VM, using e.g. `qemu-system-x86_64 ... -cdrom cloud-init.iso`, or if using [archiso](../en/Archiso.html "Archiso") then with the `run_archiso -c`.

You should then be able to SSH into the machine using as the chosen user and public key supplied in `user-data`. Note that it may take a moment to be available, due to a delay at the boot menu; e.g. the standard releng `archlinux*.iso` will wait there for 30s at start-up. For frequent re-testing of new instances with changing hostkeys, `ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null` may be handy.

**Tip** [Cloud-init\'s nocloud documenation](https://cloudinit.readthedocs.io/en/latest/reference/datasources/nocloud.html) explains an alternative approach, based on using `-smbios type=1,serial=ds=nocloud`. This can be accomplished locally on a host running QEMU and an ad hoc Python webserver as described in the [cloud-init tutorial](https://cloudinit.readthedocs.io/en/latest/tutorial/qemu.html). To boot on bare metal you could just \"burn\" two separate USB sticks, for `archlinux*.iso` and `cloud-init.iso`, and boot from `archlinux*.iso`. When doing this, cloud-init will run using the configuration on `cloud-init.iso`.

## Troubleshooting {#Troubleshooting}

### FAQ {#FAQ}

[The cloud-init FAQ](https://cloudinit.readthedocs.io/en/latest/reference/faq.html) has useful information about how to debug cloud-init, including where its log files are, and how to re-run datasource detection and cloud-init during development.

### Unmounted image {#Unmounted_image}

The first thing to check is often if the cloud-init image (ISO) is seen, with `lsblk` and `mount`.

### \"device /dev/sr0 with label cidata not a valid seed\" {#\"device_/dev/sr0_with_label_cidata_not_a_valid_seed\"}

`datasourcenocloud.py warning device /dev/sr0 with label cidata not a valid seed` appears when the nocloud datasource sees an ISO that e.g. only contains `user-data` but no `meta-data` - both are required, even if one is empty.

### \"unhandled non-multipart \[\...\] ssh_authorized_keys\" {#\"unhandled_non-multipart_[...]_ssh_authorized_keys\"}

`unhandled non-multipart (text-x-not-multipart) userdata 'b'ssh_authorized_keys` appears when `user-data` YAML does not start with `#cloud-config` (no space, apparently; even though `yamllint` will tell you that it is `missing starting space in comment`).

## See also {#See_also}

-   [cloud-init documentation](https://cloudinit.readthedocs.io/en/latest/)
