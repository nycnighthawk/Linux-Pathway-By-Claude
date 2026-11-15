# Lab: dated snapshots, promotion and rollback

`setup` creates a working repository `source/` holding `site-a` 1.0 with its metadata, and keeps `site-a` 1.1 in `incoming/`. Take two dated snapshots as the source changes, point two environments at them, and prove that production does not see the new package until you promote it.

## Starting state

`source/` is a valid RPM repository (with `repodata/`); `incoming/site-a-1.1-1.noarch.rpm` is the next version.

## Your task

1. Take snapshot `snapshots/2026-11-01` of `source/` with hard links (`cp -al source snapshots/2026-11-01`) and make it read-only (`chmod -R a-w`).
2. Add `site-a` 1.1 to `source/`, run `createrepo_c --update source`, and take `snapshots/2026-11-08` the same way.
3. Create `channels/prod` as a symlink to the older snapshot and `channels/dev` as a symlink to the newer one (relative targets such as `../snapshots/2026-11-01`).
4. Promote prod by re-pointing the link to the newer snapshot, then roll it back by pointing it at the older one again. The final state must have prod on 2026-11-01 and dev on 2026-11-08. Write each pointer change as a line in `promotions.log` (date, environment, snapshot).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-304/snapshot-promote/setup
# ...do the steps...
LAB_DIR=$PWD /path/to/repo/labs/LNX-304/snapshot-promote/check
```

## Notes

- Needs `createrepo-c` and `rpm`. Hard links need both directories on one filesystem.
- Reading material: [the lesson](lesson:LNX-304-T05). Afterwards, try [the quiz](quiz:LNX-304-T05).
