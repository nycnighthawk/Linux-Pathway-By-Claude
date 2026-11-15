# Lab: plan content views for 200 hosts

This is a design exercise (no Satellite server needed). You run 200 Enterprise Linux hosts across two sites and want weekly, approved patching. Complete the plan so that the design is small, safe and operable.

## Starting state

`setup` writes `content-plan.txt` into `$LAB_DIR` with a `?` for each field.

## Your task

Replace each `?` with a value that satisfies the rules.

| Field | Rule |
|---|---|
| `environments` | comma list of 3 or 4 lifecycle environments after Library; the last must be `prod` |
| `base_views` | an integer, 1 to 3 (content views for the operating system) |
| `composite_views` | `none`, or a number up to 3 |
| `errata_filter` | `date` (an errata date cutoff reproduces a dated snapshot) or `type` |
| `promotion_approval` | `required` |
| `publish_and_promote` | `automated` (a pipeline does both steps and records who approved) |
| `canary_percent` | an integer, 1 to 10: the share of prod hosts that gets a version first |
| `retention_versions` | an integer, 3 to 10: versions kept per view, plus any in an environment |
| `emergency_path` | `incremental` |
| `capsules` | `per_site` |
| `registration` | `activation_key` |
| `backup_test_months` | an integer, 1 to 6: how often a restore of the server is tested |
| `owner` | a named team |

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-304/content-view-plan/setup
# ...edit content-plan.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-304/content-view-plan/check
```

## Notes

- Reading material: [the lesson](lesson:LNX-304-T06). Afterwards, try [the quiz](quiz:LNX-304-T06).
