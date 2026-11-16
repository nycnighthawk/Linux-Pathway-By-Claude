# Lab (guide): diagnose a stuck live migration and write the command

`setup` writes a sampled `virsh domjobinfo` log from a migration that never finishes, and the cluster's constraints in `context.txt`. No hypervisors are needed.

## Your task

1. Read the log: does the migration converge, and what limits it?
2. Fill `report.txt`: the first fix, whether auto-converge is allowed, whether dirty limit satisfies the policy, the last-resort strategy and its risk, and the downtime target.
3. Write `migrate.sh` with one `virsh migrate` command that follows the constraints (and the downtime setting if you use a second command).

## Success criteria

The check reads your answers and flags. It never runs `virsh`. Remember that the bandwidth value is in MiB/s and that the 25 Gbit link is shared by nothing else.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/migration-tuning-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/migration-tuning-guide/check
```

Reading: [the lesson](lesson:LNX-315-T11); then [the quiz](quiz:LNX-315-T11).
