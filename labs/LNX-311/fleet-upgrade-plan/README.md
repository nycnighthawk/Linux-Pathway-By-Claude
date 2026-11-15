# Guide: plan the upgrades for a fleet

This is a paper exercise (environment S): you compute facts about a fleet from `fleet.csv` in your working directory (`$LAB_DIR`), then check them.

## Starting state

`setup` writes `fleet.csv` (cluster name, Kubernetes minor, environment) and an empty `plan.txt`. Policy: the **latest minor is 1.36**; the three newest minors (1.36, 1.35, 1.34) are in support; the control plane moves one minor at a time.

## Your task

Fill `plan.txt` with `key=value` lines:

- `out_of_support`: cluster names whose minor is below 1.34, sorted, comma separated
- `upgrade_steps_total`: the sum, over all clusters, of the single-minor steps needed to reach 1.36
- `first_wave`: the names of all `dev` clusters, sorted, comma separated (the canary wave)
- `max_steps_cluster`: the cluster that needs the most steps (ties: alphabetical first)

Success criteria: the values match the fleet. Then write two sentences in `notes.txt` on what you would do about the oldest cluster.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/fleet-upgrade-plan/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/fleet-upgrade-plan/check
```

Reading: [the lesson](lesson:LNX-311-T12); then [the quiz](quiz:LNX-311-T12).
