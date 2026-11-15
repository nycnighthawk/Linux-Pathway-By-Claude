# Lab: design the safeguards of a bare-metal provisioning platform

This is a design exercise (no racks needed). You will run Foreman or MAAS for 400 servers in two data centres. Complete `baremetal-plan.txt` so that the platform is safe, recoverable and connected to the rest of the stack.

## Starting state

`setup` writes `baremetal-plan.txt` with a `?` for each field.

## Your task

Replace each `?`.

| Field | Rule |
|---|---|
| `inventory_key` | `serial` or `bmc_mac` (a key that survives replacing a network card) |
| `lifecycle_states` | comma list in this order: `racked,discovered,prepared,ready,deployed,in_service,released,retired` |
| `prepare_tests` | comma list including `memory`, `disk` and `network` |
| `default_boot` | `disk` |
| `build_mode_default` | `off` |
| `build_mode_approval` | `required` |
| `discovery_auto_install` | `no` |
| `bmc_network` | `isolated` |
| `bmc_default_credentials` | `changed` |
| `bmc_rotation_days` | an integer from 30 to 180 |
| `dhcp_snooping` | `enabled` |
| `install_source` | `pinned_snapshot` |
| `templates_in_git` | `yes` |
| `reinstall_role` | `separate` (reinstalling is a different permission from viewing) |
| `wipe_on_release` | `yes` |
| `platform_backup_test_months` | an integer from 1 to 6 |
| `vm_ownership` | `iac` (virtual machines belong to infrastructure as code, physical ones to the platform) |

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/baremetal-plan/setup
# ...edit baremetal-plan.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/baremetal-plan/check
```

## Notes

- Reading material: [the lesson](lesson:LNX-306-T06). Afterwards, try [the quiz](quiz:LNX-306-T06).
