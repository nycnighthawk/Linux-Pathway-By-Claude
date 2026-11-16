# Lab: triage a kernel release listing

`setup` writes `releases.json` (a saved copy of the kernel.org release data from 16 November 2026), `maintainers.txt` (an excerpt in `MAINTAINERS` format) and `tags.txt` (the output of `git tag --contains` for a fix). No network is needed.

## Your task

Fill `report.txt` (key=value):

1. `latest_stable`: the newest stable version.
2. `eol_stable`: the stable branch (major.minor) that is already end of life.
3. `longterm_count` and `oldest_longterm`: how many longterm branches are listed and the oldest one (major.minor).
4. `mainline_phase`: `rc` or `release`, for the mainline entry.
5. `fix_cc_tag`: the e-mail tag that nominates a fix for stable.
6. `base_tree`: the git tree to base a patch for `drivers/net/widget/core.c` on (the `T:` URL of the matching entry).
7. `mailing_list`: the list address (`L:`) that must receive it.
8. `first_6_6_tag`: the first v6.6.x tag that contains the fix in `tags.txt`.

## Success criteria

The check recomputes every answer from the data files.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-330/release-triage/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-330/release-triage/check
```

Reading: [the lesson](lesson:LNX-330-T01); then [the quiz](quiz:LNX-330-T01).
