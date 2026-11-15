# Lab: sign a user certificate and harden sshd_config around it

You will act as the certificate authority: sign a user's public key for eight hours with two principals, then write an
sshd policy that trusts that CA and nothing else, and check it with sshd's own test mode. No daemon is started.

## Starting state

`setup` generates `ca/user_ca` (the CA key pair), `user/id_ed25519` (Alice's key pair) and `hostkey`, plus a permissive
`sshd_config`, an empty `auth_principals/` directory and a blank `answers.txt`.

## Your task

1. Sign Alice's public key with the CA: key id `alice@lab`, principals `alice` and `deploy`, valid for 8 hours. The result is
   `user/id_ed25519-cert.pub`. Inspect it with `ssh-keygen -L -f`.
2. Edit `sshd_config`: no root login, no password or keyboard-interactive login, no X11 forwarding, `MaxAuthTries 3`,
   `AuthenticationMethods publickey`, `TrustedUserCAKeys` pointing at `ca/user_ca.pub`, and an `AuthorizedPrincipalsFile`
   of `auth_principals/%u` (use absolute paths).
3. Create `auth_principals/alice` containing the single line `deploy`, so Alice may log in to her account with the `deploy` principal.
4. Print the effective configuration with `sshd -T -f sshd_config` (needs `/run/sshd`, which the check creates) and fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-204/ssh-certificates/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-204/ssh-certificates/check
```

## Notes

- The lab needs `openssh-client` and `openssh-server` (for `sshd -T`) and root, so `sshd` can read the host key.
- The principal check is the one that surprises people: with no principals file, only the account name matches.
- See [the lesson](lesson:LNX-204-T03) and [the quiz](quiz:LNX-204-T03).
