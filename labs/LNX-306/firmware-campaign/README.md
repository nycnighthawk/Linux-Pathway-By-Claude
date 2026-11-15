# Lab: plan a BMC firmware campaign (hardware)

This lab is hardware-dependent (environment H). The graded part is a planning exercise that needs no server; the practical part needs a spare, sacrificial server (or a lab board) with console access and the vendor's update tool. Do the practical part only on a machine that you can afford to lose, with supervision.

## Starting state

`setup` writes `firmware-campaign.txt` with a `?` for each field. You are updating the BMC firmware of 120 servers of 3 models.

## Your task

Replace each `?`.

| Field | Rule |
|---|---|
| `firmware_source` | `vendor_site` (the server vendor's own support site) or `mirror_unverified` |
| `verify_image` | `checksum_or_signature` or `none` |
| `read_release_notes` | `yes` |
| `group_by` | `model_and_version` |
| `first_test_target` | `sacrificial_machine` or `production_machine` |
| `test_console_access` | `yes` (serial-over-LAN or remote KVM open during the update) |
| `config_backup` | `yes` |
| `pilot_size` | an integer from 1 to 6 |
| `wave_sizes` | comma list of two or more integers, not decreasing; pilot plus waves must add up to 120 |
| `stop_rule` | `pause_on_any_failure` or `continue` |
| `power_protection` | `ups_or_stable` |
| `interrupt_update` | `never` |
| `preserve_config_check` | `yes` (verify whether settings are kept or reset) |
| `post_update_checks` | comma list including `version`, `network`, `accounts`, `event_log` and `power_control` |
| `default_account_after` | `absent` |
| `signed_images_only` | `yes` |
| `record_in_inventory` | `yes` |

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/firmware-campaign/setup
# ...edit firmware-campaign.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/firmware-campaign/check
```

## Practical part (not graded)

On a sacrificial server: read the firmware version (`ipmitool mc info`, or a Redfish query of the manager), read the vendor's release notes, back up the configuration, update with the vendor's tool while watching the console, and run the post-update checks. Write down how long the BMC was unreachable (to verify per vendor).

## Notes

- Reading material: [the lesson](lesson:LNX-306-T11). Afterwards, try [the quiz](quiz:LNX-306-T11).
