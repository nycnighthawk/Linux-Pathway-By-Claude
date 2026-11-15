# Lab: write the pre-join check script that stops a bad realm join early

Most failed AD joins are decided before `realm join` runs: wrong DNS, a short host name, a drifting clock, a blocked
port. You will write `prejoin.sh DOMAIN`, a script that tests exactly those four things and says which one failed.
The grader runs it against five simulated hosts by putting stand-in `hostname`, `dig`, `chronyc` and `nc` programs
first in the `PATH`, so no domain controller is needed.

## Starting state

`setup` creates `prejoin.sh` (a stub that always fails) and a directory `stubbin/` with the stand-in commands. The
stand-ins read the scenario from environment variables (`STUB_FQDN`, `STUB_SRV`, `STUB_SKEW`, `STUB_CLOSED`); look at
them to see what each command prints.

## Your task

`prejoin.sh DOMAIN` must print one line per check, in this order, and exit 0 only when all four pass:

| Line | Passes when |
|---|---|
| `OK fqdn` / `FAIL fqdn: <reason>` | `hostname -f` returns a name with a dot, ending in `.DOMAIN` (case-insensitive), whose first label is at most 15 characters and is not `localhost` |
| `OK srv` / `FAIL srv: <reason>` | `dig +short SRV _ldap._tcp.dc._msdcs.DOMAIN` returns at least one record (`priority weight port host.`) |
| `OK skew` / `FAIL skew: <reason>` | the `System time` line of `chronyc tracking` is within 120 seconds of NTP time, in either direction |
| `OK ports` / `FAIL ports: <reason>` | `nc -z -w 2 HOST PORT` succeeds for ports 53, 88, 389 and 464 on the host of the first SRV record; the reason names every closed port. When there is no SRV record, print `SKIP ports` and fail overall |

## Success criteria

- Healthy host: four `OK` lines, exit 0.
- Clock four hundred seconds off: `FAIL skew` and exit non-zero, the other three still `OK`.
- No SRV record: `FAIL srv`, `SKIP ports`, non-zero.
- Short host name: `FAIL fqdn`.
- A host whose first label has 20 characters: `FAIL fqdn`.
- Port 88 closed: `FAIL ports` naming 88.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-301/prejoin-checks/setup
# ...write prejoin.sh...
LAB_DIR=$PWD /path/to/repo/labs/LNX-301/prejoin-checks/check
```

## Notes

- The same four checks catch most realm-join failures described in the lesson; `realm discover` is the next step after
  they pass.
- Reading material: [the lesson](lesson:LNX-301-T04). Afterwards, try [the quiz](quiz:LNX-301-T04).
