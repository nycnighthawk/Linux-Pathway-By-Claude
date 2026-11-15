# Lab: plan a safe cloud deployment

This is a design exercise (no cloud account needed; on a real account the same plan becomes an OpenTofu configuration). You will provision a web tier of six instances across three availability zones. Complete `cloud-plan.txt`.

## Starting state

`setup` writes `cloud-plan.txt` with a `?` for each field.

## Your task

Replace each `?` with one of the allowed values.

| Field | Allowed values (choose the safe one) |
|---|---|
| `image_source` | `own_account` or `public_unknown` |
| `image_selection` | `filter_by_tag` (newest image that passed tests) or `fixed_id` |
| `image_build` | `pipeline` or `by_hand` |
| `user_data_secrets` | `none` or `some` |
| `secret_delivery` | `secret_manager`, `user_data` or `baked_in_image` |
| `instance_identity` | `role` (platform-bound) or `static_keys` |
| `metadata_service` | `token_required` or `open` |
| `metadata_pod_access` | `blocked` or `allowed` (containers on the node reaching the metadata address) |
| `admin_access` | `federated_or_session_manager`, `shared_key` or `password` |
| `public_ip` | `none` (behind a load balancer) or `every_instance` |
| `zones` | an integer, at least 3 |
| `persistent_data` | `separate_volume` or `root_disk` |
| `ephemeral_disk_use` | `disposable_only` or `databases` |
| `root_credentials_for_automation` | `never` or `sometimes` |
| `state_backend` | `remote_locked` or `local_file` |
| `plan_review` | `required` or `skipped` |
| `rollout` | `rolling_replace` or `edit_in_place` |

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/cloud-plan/setup
# ...edit cloud-plan.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/cloud-plan/check
```

## Notes

- Optional extension on a free-tier account: write the OpenTofu for the plan and run `tofu plan` (do not apply without checking costs). Platform names for the controls differ (to verify per cloud).
- Reading material: [the lesson](lesson:LNX-306-T10). Afterwards, try [the quiz](quiz:LNX-306-T10).
