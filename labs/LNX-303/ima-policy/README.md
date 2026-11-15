# Lab: write a staged IMA policy

`sample-policy` shows what a hasty administrator copied from a blog post: it appraises every file read by root and measures programs. Replace it with a policy that is safe to roll out.

## Starting state

`setup` writes `sample-policy` into `$LAB_DIR`. Nothing is loaded into a kernel; you write the files you would install.

## Your task

1. `ima-policy`: exclude the pseudo filesystems first (procfs `0x9fa0`, sysfs `0x62656572`, tmpfs `0x1021994`; debugfs `0x64626720` and securityfs `0x73636673` are good additions), as `dont_measure` and `dont_appraise` rules. Then measure executed programs (`BPRM_CHECK`), executable mappings (`MMAP_CHECK` with `mask=MAY_EXEC`) and modules. Then appraise programs, libraries and modules with `appraise_type=imasig`. Do not appraise general file reads.
2. `cmdline.txt`: one line of kernel parameters for the first stage of the rollout: log mode for appraisal, a SHA-256 or stronger hash, and lockdown at the integrity level.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/ima-policy/setup
# ...write the files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/ima-policy/check
```

## Notes

- Rule order matters: the first rule that matches a file decides. The kernel reads the policy once; a line it cannot parse is an error.
- On a throwaway VM you can load a policy by writing it to `/sys/kernel/security/ima/policy`; do not do this on a machine you need.
- Reading material: [the lesson](lesson:LNX-303-T04). Afterwards, try [the quiz](quiz:LNX-303-T04).
