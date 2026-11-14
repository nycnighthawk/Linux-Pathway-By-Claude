# Lab: reach a private host through a bastion with ProxyJump

Two OpenSSH servers run on this machine under your control: a **bastion** on `127.0.0.1:2201` that allows forwarding,
and a **target** on `127.0.0.2:2202` that you are meant to reach only through the bastion.

## Starting state

`setup` generates a key pair (`keys/id_lab`), host keys for both servers, starts both `sshd` processes with private
configuration files (`sshd_bastion.conf`, `sshd_target.conf`, logs `bastion.log`, `target.log`), writes `known_hosts`
with both host keys, and writes a skeleton `ssh_config` whose `target` block lacks the jump and the safety options.
Stop the servers afterwards with `kill $(cat bastion.pid) $(cat target.pid)`.

## Your task

Edit `ssh_config` so that `ssh -F ssh_config target 'echo reached-target'` works and:

1. reaches `target` through `bastion` with `ProxyJump`;
2. authenticates with the key `keys/id_lab` and offers **only** that key (`IdentityFile`, `IdentitiesOnly yes`);
3. verifies both servers' host keys against the pre-built `known_hosts` file (`UserKnownHostsFile`, `StrictHostKeyChecking yes`).

Use `ssh -F ssh_config -G target` to see the effective options, and `ssh -v` to follow a connection.

## Grade it

`bin/lpc course lab LNX-201 ssh-jump` runs the whole cycle. To grade your own file run `check` with `LAB_DIR` set to
the directory that holds `ssh_config`. The grader also looks into `bastion.log` for a forward to the target, so a
direct connection does not pass.

## Notes

- For each option the first value obtained wins, so put general `Host *` defaults after, not before, specific values you want to override, or use them only for options you do not set elsewhere.
- Relative paths in `IdentityFile` are taken from the directory you run `ssh` in; the examples use absolute paths.
- The lab needs the packages `openssh-server` and `openssh-client` and runs as root or as any user with permission to start `sshd` on high ports.
- Reading material: [the lesson](lesson:LNX-201-T07). Afterwards, try [the quiz](quiz:LNX-201-T07).
