# Lab: write an ansible-freeipa inventory, a policy playbook and a drift check

You will describe an IdM deployment as code: the inventory for a server, a replica and clients, a playbook that
creates groups and an HBAC and sudo policy idempotently, and a script that detects drift. The grader parses the
YAML and applies the rules a reviewer would apply. No Ansible run is needed.

## Starting state

`setup` writes stubs: `inventory.yml`, `policy.yml` and `drift.sh`, all with a `TODO`.

## Your task

1. `inventory.yml` (YAML inventory): groups `ipaserver` (one host), `ipareplicas` (at least one host) and `ipaclients`
   (at least one host); group variables for `ipaserver`: `ipaserver_domain: lab.test`, `ipaserver_realm: LAB.TEST`,
   `ipaserver_setup_dns: true`, `ipaserver_no_hbac_allow: true`; and `ipaadmin_password` and `ipadm_password` that are
   Jinja references to vaulted variables (for example `"{{ vault_ipaadmin_password }}"`), never literal secrets.
2. `policy.yml`: one play with `hosts: ipaserver`, `gather_facts: false`, `become: false`, and at least these tasks,
   every one using the collection prefix `freeipa.ansible_freeipa.` and an explicit `state`:
   - `ipagroup` creates `dba`, then a second `ipagroup` task adds the user `alice` with `action: member`;
   - `ipahostgroup` creates `dbservers`;
   - `ipasudocmd` creates `/usr/bin/systemctl`, `ipasudocmdgroup` creates `pgctl` with that command as a member;
   - `ipahbacrule` creates `db-ssh` for group `dba`, hostgroup `dbservers` and service `sshd`;
   - `ipasudorule` creates `dba-restart` for group `dba`, hostgroup `dbservers` and `allow_sudocmdgroup: [pgctl]`.
   Set the admin password once with `module_defaults` (the action group `freeipa.ansible_freeipa.modules`) or on every
   task, always as a Jinja reference.
3. `drift.sh`: a script that runs the policy playbook with `--check --diff` against `inventory.yml` and exits
   non-zero when any task would change something (look for `changed=` in the recap and `grep` for a non-zero count).

## Success criteria

- No literal passwords anywhere; the vault is the only source.
- Membership is edited with `action: member`, not by replacing the whole list.
- The playbook is idempotent by construction: every task states the desired state.
- The drift script uses check mode, shows the diff, and fails when drift exists.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-301/freeipa-playbook/setup
# ...write the three files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-301/freeipa-playbook/check
```

## Notes

- The grader needs `python3-yaml`. On a control node: `ansible-playbook -i inventory.yml policy.yml --check --diff`.
- Reading material: [the lesson](lesson:LNX-301-T09). Afterwards, try [the quiz](quiz:LNX-301-T09).
