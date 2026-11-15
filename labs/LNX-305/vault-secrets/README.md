# Lab: keep secrets in Git with Ansible Vault

You will encrypt one file and one single value under a vault ID label, remove the plain-text copies, and prove that a
playbook can use the secrets while the output and the repository never show them.

## Starting state

`setup` writes `.vault_pass` (the vault password, mode 600), `plain/secrets.yml` and `plain/api_token.txt` (the secrets in
clear), `group_vars/all/vars.yml` (which refers to `vault_db_password` by indirection), `site.yml` (writes
`out/app.conf` from the secrets, with `no_log` already on) and a blank `answers.txt`.

## Your task

1. Make `group_vars/all/vault.yml` from `plain/secrets.yml` and encrypt the whole file with vault ID label `lab`, using
   the password file: `--vault-id lab@.vault_pass` and `--encrypt-vault-id lab` (use an absolute path or a path relative
   to your working directory).
2. Create one more file in `group_vars/all/` that holds `api_token` as an inline `!vault` value, made with
   `ansible-vault encrypt_string` under the same label. The value is the text in `plain/api_token.txt` without its newline.
3. Delete `plain/`. No plain-text secret may remain anywhere in your working directory except the rendered `out/` files.
4. Run `ansible-playbook site.yml --vault-id lab@.vault_pass`. Look at the first lines of your encrypted files.
5. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-305/vault-secrets/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-305/vault-secrets/check
```

## Notes

- The vault password here is for the lab only. In real work it comes from a prompt, a keyring or a client script, and the
  password file never enters the repository.
- The header looks like `$ANSIBLE_VAULT;1.2;AES256;lab`: format, version, cipher, label.
- The lab needs the package `ansible-core`.
- Reading material: [the lesson](lesson:LNX-305-T04). Afterwards, try [the quiz](quiz:LNX-305-T04).
