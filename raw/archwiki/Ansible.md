---
{"title": "Ansible", "url": "https://wiki.archlinux.org/title/Ansible", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Ansible

From [www.ansible.com](https://www.ansible.com/overview/how-ansible-works):

Ansible is a radically simple IT automation engine that automates cloud provisioning, configuration management, application deployment, intra-service orchestration, and many other IT needs.

## Installation {#Installation}

On the control machine (master), [install](../en/Help:Reading.html#Installation_of_packages "Install") the [ansible-core](https://archlinux.org/packages/?name=ansible-core) package. Additionally, you can install the [ansible](https://archlinux.org/packages/?name=ansible) package, which provides a range of community curated collections.

On the managed machines (nodes), where you want to automate deployment or configuration tasks, [python](https://archlinux.org/packages/?name=python) is required and it may be necessary to indicate the specific [#Python binary location](#Python_binary_location) in some circumstances. A way to communicate with the node is also necessary, this is usually [SSH](../en/Secure_Shell.html "SSH"). Note that a functioning [SSH key](../en/SSH_keys.html#Copying_the_public_key_to_the_remote_server "SSH keys") setup eases the use of Ansible but is not required.

**Tip** You may want to install syntax highlighting of Ansible files (e.g. [vim-ansible](https://archlinux.org/packages/?name=vim-ansible) for [vim](../en/Vim.html "Vim"))

## Basic usage {#Basic_usage}

### Configuration {#Configuration}

Ansible parameters are set in the configuration file which can either be `ansible.cfg` in the current directory, `.ansible.cfg` in the home directory or `/etc/ansible/ansible.cfg`, whichever it finds first.

A base config can be generated with:

    $ ansible-config init --disabled > ansible.cfg

### Inventory {#Inventory}

The infrastructure is listed in the Ansible inventory file, which defaults to being saved in the location `/etc/ansible/hosts` or one can specify a different inventory file using the `-i` command line switch. For instance, the following inventory defines a cluster with 7 nodes organized into two groups:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ansible/hosts
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[control]
192.168.12.1
foo-[a:c].example.org
localhost ansible_connection=local

[managed]
192.168.12.2
192.168.12.3
```

One can assign specific attributes to every node in the infrastructure file at the corresponding line or in the `ansible.cfg` configuration file. By default Ansible executes playbooks over SSH, the `ansible_connection` parameter extends the connection to:

-   `local` to deploy the playbook to the control machine itself
-   `docker` deploys the playbook directly into Docker containers

Check [Ansible - intro inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html) for details.

### Ping {#Ping}

You may check if all the nodes listed in the inventory are alive by

    $ ansible all -m ping

### Playbook {#Playbook}

Playbooks are the main organizational unit to configure and deploy the whole infrastructure. Check [the official document](https://docs.ansible.com/ansible/latest/user_guide/playbooks.html) for more details. Here is an extremely simple demonstration, where the administrator of the above inventory wants to perform a full system upgrade on a set of Arch Linux hosts. First, create a playbook file, with YAML formatting (*always* 2 spaces indentation):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
syu.yml
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
---
- name: All hosts up-to-date
  hosts: control managed
  become: true

  tasks:
    - name: Full system upgrade
      community.general.pacman:
        update_cache: true
        upgrade: true
```

Then, run the playbook script:

    $ ansible-playbook --ask-become-pass syu.yml

### Vault {#Vault}

A [vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html#vault) can be used to keep sensitive data in an encrypted form in playbooks or roles, rather than in plaintext. The vault password can be stored in plaintext in a file, for example *`vault_pass.txt`* containing *`myvaultpassword`*, to be used later on as a command parameter:

    $ ansible-playbook site.yml --vault-id vault_pass.txt

In order to encrypt the content *`the var content`* of a variable named *`varname`* using the password stored in *`vault_pass.txt`*, the following command should be used:

    $ ansible-vault encrypt_string --vault-id vault_pass.txt 'the var content' --name varname

More securely, to avoid inputting the variable content in the command line and be prompted for it instead, one can use:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ ansible-vault encrypt_string --vault-id vault_pass.txt --stdin-name varname
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Reading plaintext input from stdin. (ctrl-d to end input)
```

The command returns directly the protected variable that can be inserted into a playbook. Encrypted and non-encrypted variables can coexist in a YAML file as illustrated below:

    notsecret: myvalue

    mysecret: !vault |
              $ANSIBLE_VAULT;1.1;AES256
              66386439653236336462626566653063336164663966303231363934653561363964363833313662
              6431626536303530376336343832656537303632313433360a626438346336353331386135323734
              62656361653630373231613662633962316233633936396165386439616533353965373339616234
              3430613539666330390a313736323265656432366236633330313963326365653937323833366536
              3462

    other_not_secret: othervalue

### Package management {#Package_management}

#### Official repositories {#Official_repositories}

Ansible has a [pacman module](https://docs.ansible.com/ansible/latest/collections/community/general/pacman_module.html) (provided by the [ansible](https://archlinux.org/packages/?name=ansible) package) to handle installation, removal and system upgrades with [pacman](../en/Pacman.html "Pacman").

#### AUR {#AUR}

For the [Arch User Repository](../en/Arch_User_Repository.html "Arch User Repository") *(AUR)*, it is required to use the external module [ansible-aur](https://github.com/kewlfft/ansible-aur). See the README for use and installation instructions.

While Ansible expects to ssh as root, AUR helpers do not allow executing operations as root, they all fail with \"you cannot perform this operation as root\". For Ansible automation, it is therefore recommended to create a user, for example named *aur_builder*, that has no need for password with pacman in [sudoers](../en/Sudo.html#Configuration "Sudoers"). This can be done in Ansible with the following actions:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
task.yml
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
- user: name=aur_builder

- lineinfile:
     path: /etc/sudoers.d/aur_builder-allow-to-sudo-pacman
     state: present
     line: "aur_builder ALL=(ALL) NOPASSWD: /usr/bin/pacman"
     validate: /usr/sbin/visudo -cf %s
     create: yes
```

Then, AUR helpers or [makepkg](../en/Makepkg.html "Makepkg") can be used associated with the Ansible parameters `become: yes` and `become_user: aur_builder`

## Tips and tricks {#Tips_and_tricks}

### User account creation {#User_account_creation}

Ansible can manage user accounts and in particular it is able to create new ones. This is achieved in playbooks with the [user module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/user_module.html) which takes an optional `password` argument to set the user\'s password. It is the **hashed value of the password** that needs to be provided to the module.

The hashing can simply be performed on the fly within Ansible using one of its internal [hash-filters](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#hash-filters):

    - user:
      name: user_name
      password: "{{ 'user_password' | password_hash('sha512', 'mypermsalt') }}"
      shell: /usr/bin/nologin

**Tip** The salt should be fixed and explicitly supplied as a second parameter of the hash function for the operation to be idempotent (can be repeated without changing the state of the system).

With this approach it is recommended to vault-encrypt *user_password* so that it does not appear in plain text, see [#Vault](#Vault). However, an encrypted variable cannot be piped directly and will first need to be assigned to another one that will be piped.

Alternatively, the hashing can be performed outside Ansible. The following commands return respectively the [MD5](https://en.wikipedia.org/wiki/MD5 "wikipedia:MD5") and the [SHA512](https://en.wikipedia.org/wiki/SHA-2 "wikipedia:SHA-2") hashed values of *user_password*:

    $ openssl passwd -1 user_password

    $ python -c 'import crypt; print(crypt.crypt("user_password", crypt.mksalt(crypt.METHOD_SHA512)))'

### Python binary location {#Python_binary_location}

Ansible requires [Python](../en/Python.html "Python") on the target machine. By default Ansible assumes it can find a `/usr/bin/python` on the remote system that is a 2.X or 3.X version, specifically 2.6 or higher.

If some of your modules specifically require Python2, you need to inform Ansible about its location by setting the `ansible_python_interpreter` variable in the inventory file. This can be done by using host groups in the inventory:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ansible/hosts
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[archlinux]
server1
server2

[debian]
server3

[archlinux:vars]
ansible_python_interpreter=/usr/bin/python2
```

More information about Python version support in Ansible is available in [\[1\]](https://docs.ansible.com/ansible/latest/reference_appendices/python_3_support.html), [\[2\]](https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-handle-not-having-a-python-interpreter-at-usr-bin-python-on-a-remote-machine) and [\[3\]](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters).

## Troubleshooting {#Troubleshooting}

### Unarchive {#Unarchive}

The `unarchive` module unpacks an archive. However *tar* files are not well supported and several outstanding issues are reported in [GitHub - unarchive](https://github.com/ansible/ansible/labels/m%3Aunarchive). In particular when the parameter `keep_newer` is set to `yes`, idempotence is not observed. In case you face an issue with the module, you can use instead the *zip* format which is better integrated in Ansible.

## See also {#See_also}

-   [https://www.ansible.com/resources/videos/quick-start-video](https://www.ansible.com/resources/videos/quick-start-video) - Ansible concept in 12 minutes
-   [https://docs.ansible.com/ansible/latest/collections/community/general/pacman_module.html](https://docs.ansible.com/ansible/latest/collections/community/general/pacman_module.html) - Official documentation of the pacman module
