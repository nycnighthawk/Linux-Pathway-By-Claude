# Lab: express HBAC rules, sudo rules and a replica topology, and prove them with a decision table

IdM policy is data: users and hosts are grouped, rules join the groups, and a test (`ipa hbactest`, `sudo -l`) tells
you the verdict. You will write that data for a small estate and the grader will evaluate it exactly as the policy
engine would, against a table of access questions. Nothing is installed.

## Starting state

`setup` writes `inventory.yaml` (the facts: users and their groups, hosts and host groups, servers and their roles)
and `policy.yaml`, which holds only the default `allow_all` rule.

## Your task

Edit `policy.yaml`:

1. `hbac_rules`: replace the default with rules so that members of `dba` may use `sshd` on hosts in `dbservers`,
   members of `web` may use `sshd` on hosts in `webservers`, and members of `admins` may use any service on any host
   (use the categories `usercat`, `hostcat`, `svccat` set to `all` where it fits). `contractors` get no access. The
   `allow_all` rule must be disabled (`enabled: false`) or removed.
2. `sudo_cmdgroups` and `sudo_rules`: `dba` may run `/usr/bin/systemctl restart postgresql` on `dbservers`
   (define a command group and refer to it); `web` may run `/usr/bin/systemctl restart nginx` on `webservers`;
   `admins` may run any command on any host (`cmdcat: all`).
3. `topology`: for the suffix `domain`, a list of segments (pairs of servers) so that every server has at least two
   connections and the graph is connected; for suffix `ca`, segments only between CA servers; name exactly one CA
   server as `ca_renewal_master`.

## Success criteria

- Every row of the decision table (twelve HBAC and nine sudo questions) comes out as expected.
- `allow_all` no longer grants access.
- The topology has no single point of failure and no server with more than four segments.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-301/idm-hbac-sudo/setup
# ...edit policy.yaml...
LAB_DIR=$PWD /path/to/repo/labs/LNX-301/idm-hbac-sudo/check
```

## Notes

- The grader needs `python3-yaml`. The rule schema is shown in the comments at the top of `policy.yaml`.
- On a real domain the same policy is built with `ipa hbacrule-add`, `ipa sudorule-add` and
  `ipa topologysegment-add`, and checked with `ipa hbactest`.
- Reading material: [the lesson](lesson:LNX-301-T06). Afterwards, try [the quiz](quiz:LNX-301-T06).
