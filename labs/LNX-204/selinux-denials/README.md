# Lab: read three SELinux denials and choose the smallest fix

Three services fail with "permission denied" although file modes are right. An audit excerpt holds their AVC records.
For each you decide whether the cause is a boolean, a file label or a port type, and you write the command that fixes
it persistently. Nothing here needs SELinux to be enabled: you read records and write commands.

## Starting state

`setup` writes `audit.log` (three AVC denials from `httpd_t`) and a blank `answers.txt`.

## Your task

1. Save the interpreted records: `ausearch -if audit.log -m AVC -i > denials.txt`.
2. Work out each cause from the source context, target context and class:
   - `php-fpm` cannot connect to PostgreSQL on port 5432;
   - `nginx` cannot read `/srv/web/index.html`, which has the wrong type after being moved;
   - `nginx` cannot bind port 8081.
3. Fill in `answers.txt` with the persistent fix for each, the command that applies the label, how to make only `httpd_t`
   permissive, and one phrase on why `chcon` is not the persistent fix.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-204/selinux-denials/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-204/selinux-denials/check
```

## Notes

- The lab needs the `auditd` package for `ausearch`. On a real host you would also pipe records into `audit2why`.
- Prefer a boolean, then a label, then a port, and a custom module last. See [the lesson](lesson:LNX-204-T04) and [the quiz](quiz:LNX-204-T04).
