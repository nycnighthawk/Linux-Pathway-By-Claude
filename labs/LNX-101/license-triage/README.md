# Lab: triage a component inventory by licence

You maintain an appliance image, and a colleague has handed you an inventory of ten components with their SPDX licence
identifiers. Before the image ships, you must say which licence family each component is in and whether you owe anyone
the corresponding source.

## Starting state

`setup` writes `components.csv` into your working directory (`$LAB_DIR`). Its columns are:

| Column | Meaning |
|---|---|
| `component` | name of the component |
| `spdx` | its SPDX licence identifier |
| `distributed` | `yes` if a copy leaves your organisation inside the image or a download |
| `network_service` | `yes` if users interact with a modified copy over a network |

## Your task

1. Create `decision.csv` with the header `component,family,source_offer` and one row per component, in any order.
   - `family` is one of `permissive`, `weak-copyleft`, `strong-copyleft` or `network-copyleft`. Treat MIT, BSD and
     Apache as permissive; LGPL, MPL and CDDL as weak copyleft; GPL as strong copyleft; AGPL as network copyleft.
   - `source_offer` is `yes` when you must offer the corresponding source and `no` otherwise. Weak and strong copyleft
     create the duty only when the component is distributed. Network copyleft creates it when the component is
     distributed or when it is run as a network service. Permissive licences create no source duty (they still need
     their notices kept, which is outside this lab).
2. Create `distro.txt` whose first line is the `ID` and `VERSION_ID` of the system you are working on, taken from
   `/etc/os-release`, separated by a single space.

You may write the files by hand or with a script. A short `awk` program is enough.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-101/license-triage/setup
# ...create decision.csv and distro.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-101/license-triage/check
```

In CI the harness runs `setup`, proves `check` fails, applies `solution/apply`, and proves `check` passes.

## Notes

- This is a teaching rule of thumb, not legal advice. Real obligations depend on the exact licence text, on how
  components are combined, and on a lawyer's reading.
- Reading material: [the lesson](lesson:LNX-101-T01). Afterwards, try [the quiz](quiz:LNX-101-T01).
