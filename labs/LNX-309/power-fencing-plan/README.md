# Lab: a power fencing design review

You are reviewing the fencing plan for a two-node cluster (`node1`, `node2`). Each server has an onboard management controller (BMC) that is powered from the same feed as the server, and the room has one switched power distribution unit (PDU) on a different feed. `setup` writes `fencing-plan.txt` with `?` in every field. Replace each `?` with the right answer. No hardware is needed; the grader reads the file.

## Fields

| Field | What to decide |
|---|---|
| `primary_device`, `second_device` | device type: `bmc`, `switched_pdu`, `ssh_login`, `watchdog` |
| `primary_shares_power_with_node`, `second_device_independent_feed` | `yes` or `no` |
| `management_network` | `separate_from_cluster_link` or `same_as_cluster_link` |
| `ssh_login_device_in_production` | `never` or `allowed` |
| `level1`, `level2` | which device is tried first and second |
| `dual_psu_outlets_same_level` | `yes` or `no` for a server with two PDU outlets |
| `two_node_delay_on` | `node_to_sacrifice` or `node_to_keep` |
| `test_device_command` | the command that tests the device on demand |
| `test_real_failure` | `cut_cluster_link_or_block_corosync` or `read_the_config` |
| `bad_test` | the test the documentation advises against, `local_interface_down_only` |
| `credentials_rotation_in_runbook`, `monitor_fence_device` | `yes` or `no` |
| `retest_interval_months` | an integer from 1 to 6 |
| `sbd_watchdog_timeout_seconds`, `sbd_stonith_watchdog_timeout_seconds` | for a fallback watchdog level with a quorum device: integers that respect the 30 s sync timeout and the doubling rule |

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-309/power-fencing-plan/setup
# ...edit fencing-plan.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-309/power-fencing-plan/check
```

## Notes

- Reading material: [the lesson](lesson:LNX-309-T06). Afterwards, try [the quiz](quiz:LNX-309-T06).
