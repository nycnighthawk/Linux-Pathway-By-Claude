# Lab: build and promote a PostgreSQL streaming-replication standby

`setup` starts a throw-away PostgreSQL primary on `127.0.0.1:55432` (as the `postgres` user, under `/tmp/pglab`) with a small `orders` table. You write `make-standby.sh`; the grader runs it, checks replication, and then promotes the standby. Needs root (it uses `runuser`) and the PostgreSQL server package.

## Your task

Complete `make-standby.sh` (it sources `env.sh` for `PGBIN`, `PGLAB`, `PRIMARY_PORT`, `STANDBY_PORT`). Run every PostgreSQL command as the `postgres` user (`runuser -u postgres -- ...`):

1. Create a role with the `REPLICATION` attribute.
2. Allow it to replicate from `127.0.0.1` in the primary's `pg_hba.conf` and reload.
3. Take a base backup with `pg_basebackup -X stream -R` into `$PGLAB/standby`.
4. Give the standby its own `port` (`$STANDBY_PORT`) and socket directory in `postgresql.conf`, then start it.

The grader then verifies that the standby is in recovery and streaming, that the existing and a new row are there, that writes on the standby are refused, and that promotion works.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && sudo LAB_DIR=$PWD /path/to/repo/labs/LNX-309/pg-replica/setup
# ...edit make-standby.sh...
sudo LAB_DIR=$PWD /path/to/repo/labs/LNX-309/pg-replica/check
```

## Notes

- Trust authentication is for the lab only; production uses `scram-sha-256` or certificates and TLS.
- Old versions used `recovery.conf`; PostgreSQL 12 and later use `standby.signal`, written by `-R` (to verify for your version).
- Reading material: [the lesson](lesson:LNX-309-T04). Afterwards, try [the quiz](quiz:LNX-309-T04).
