# Guide lab: size a cluster and check the quorum arithmetic

Building a Proxmox VE or oVirt cluster needs at least three machines and shared storage, more than a shared runner provides. This is a guided design exercise: you fill in a cluster design sheet for a cluster you will build (or one you invent) and the grader checks that the numbers and the choices are consistent.

## Starting state

`setup` writes `cluster-plan.txt` in your working directory (`$LAB_DIR`) with question marks.

## Your task

| Key | What to put |
|---|---|
| `platform` | `proxmox-ve`, `ovirt`, `openstack`, `cloudstack`, `kubevirt`, `incus` or `pacemaker` |
| `nodes`, `qdevice` | node count; `yes` if an external tie-break vote is added |
| `votes`, `quorum_needed`, `failures_tolerated` | the arithmetic: one vote per node plus one for a qdevice, a strict majority, and the votes you can lose |
| `cluster_network` | at least three words: dedicated link, its speed, a second link |
| `separate_storage_network`, `shared_storage` | `yes` or `no` |
| `fencing` | `watchdog`, `ipmi`, `power-switch`, `storage-lease` or `none` |
| `ha_enabled` | `yes` or `no`; yes needs a fencing method, shared storage and three voters |
| `maintenance_rule` | at least five words on how you patch without losing quorum |

## Success criteria

- You can explain why two nodes without a tie-break stop when either fails.
- You can say what happens to a node that loses quorum while it runs HA guests, and how long it takes.
- You built (or read the documentation for) the cluster with `pvecm create` and `pvecm add`, or `hosted-engine --deploy`, and read `pvecm status`.
- Your plan keeps the cluster heartbeat off the storage and migration links.

## Grade it

`bin/lpc course lab LNX-308 cluster-plan` checks the starting state and the structure of the sample answer; to grade your own sheet run `check` with `LAB_DIR` set to the directory that holds `cluster-plan.txt`.

## Notes

- This lab is not run by CI (environment S: several machines are needed); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-308-T08). Afterwards, try [the quiz](quiz:LNX-308-T08).
