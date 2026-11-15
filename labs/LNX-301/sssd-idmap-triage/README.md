# Lab: triage five SSSD identity problems from recorded evidence

Each case in `cases.txt` is a trimmed record of a real kind of failure: command output, `sssd.conf` excerpts and log
lines. You decide the cause, name the first command you would run, work out one ID mapping by hand and fix one
`sssd.conf` option. Nothing runs on your machine.

## Starting state

`setup` writes `cases.txt`, `answers.txt` (with question marks) and `sssd-fix.conf` (a stub).

## Your task

1. `answers.txt`, one line per key:
   - `case_a_cause`, `case_b_cause`, `case_c_cause`: one of `stale-cache`, `different-idmap-backends`,
     `missing-posix-attributes`, `slice-too-small`, `server-unreachable`.
   - `case_c_first_command`: the command you would run first, as typed (it must name `sss_cache` and a user or `-E`).
   - `case_d_uid`: the UID SSSD computes for the user with RID 1105 in slice 3 (use the range settings in case D).
   - `case_d_rid_250001`: `mapped` or `unmapped`, for a RID of 250001 with the same settings.
   - `case_e_first_command`: the command for the slow login in case E (it must name `sssctl domain-status`).
   - `debug_level_for_auth`: the SSSD debug level Red Hat suggests as the starting point for authentication.
2. `sssd-fix.conf`: a `[domain/corp.example.com]` section that fixes case B by making SSSD read the numbers from the
   directory (`ldap_id_mapping = False`) and that confines identities to a safe range with `min_id = 10000` and
   `max_id = 2000000`.

## Success criteria

- The causes match the evidence; the commands are the ones the lesson recommends first.
- The arithmetic of case D is exact.
- The grader accepts `sssd-fix.conf` as valid INI with the three options in the right section.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-301/sssd-idmap-triage/setup
# ...read cases.txt, fill answers.txt and sssd-fix.conf...
LAB_DIR=$PWD /path/to/repo/labs/LNX-301/sssd-idmap-triage/check
```

## Notes

- Reading material: [the lesson](lesson:LNX-301-T08). Afterwards, try [the quiz](quiz:LNX-301-T08).
