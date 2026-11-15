# Lab: write safe unattended installation files

`setup` writes a deliberately unsafe `ks.cfg` and an empty `user-data`. Fix the Kickstart file and complete the Ubuntu autoinstall file so that both pass the rules below. Nothing is installed; the check reads the files.

## Starting state

`ks.cfg` wipes every disk and sets a plaintext root password. `user-data` is empty.

## Your task

1. `ks.cfg`: keep it in text mode; add `ignoredisk --only-use=vda` and make `clearpart` use `--drives=vda`; replace the root password with `rootpw --lock` and add an `sshkey --username=ops "ssh-ed25519 ..."` line and a `user --name=ops --groups=wheel` line; add `selinux --enforcing`, `firewall --enabled --ssh`, `services --enabled=sshd,chronyd` and `reboot`; make `%packages` contain `@core` and `chrony`; give `%post` a `--log=` option. Every section ends with `%end`.
2. `user-data`: a `#cloud-config` document with an `autoinstall:` mapping: `version: 1`, `identity` (hostname, username `ops` and a hashed password beginning with `$6$` or `$y$`), `ssh` with `allow-pw: false` and at least one authorized key, `storage` with a `layout` (name `lvm` or `direct`), `packages` including `chrony`, and `late-commands` (a non-empty list).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/unattended-install/setup
# ...edit ks.cfg and user-data...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/unattended-install/check
```

## Notes

- Needs `python3` and `python3-yaml`. If `ksvalidator` (pykickstart) is installed, the check also runs it as an extra.
- Reading material: [the lesson](lesson:LNX-306-T01). Afterwards, try [the quiz](quiz:LNX-306-T01).
