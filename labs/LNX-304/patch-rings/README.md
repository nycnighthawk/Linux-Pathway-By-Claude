# Lab: assign patch rings

`setup` writes `fleet.csv`, an inventory of 40 hosts (`host,service,env,role,pair,freeze`). Write `rings.csv` (`host,ring`) assigning every host to ring 0 to 4 so that the policy holds. Use any tool you like (a shell loop, awk, a spreadsheet, Python).

## Starting state

`fleet.csv` has web, api, batch, cache and db hosts (db hosts come in primary and replica pairs sharing a `pair` id), two `lab` hosts, and two `appliance` hosts with `freeze=yes`.

## Policy

1. Ring 0 is exactly the hosts with `env=lab`.
2. Ring 4 is exactly the hosts with `freeze=yes`.
3. Ring 1 (the canary) has 5 or 6 hosts and contains at least one host of each service: web, api, batch, cache and db. The db host in ring 1 must be a replica.
4. In every db pair the replica's ring must be lower than the primary's ring.
5. Every host appears exactly once; rings 1, 2 and 3 are all non-empty; ring 3 is the largest.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-304/patch-rings/setup
# ...write rings.csv...
LAB_DIR=$PWD /path/to/repo/labs/LNX-304/patch-rings/check
```

## Notes

- Needs `python3`. The check reads both files and reports each broken rule.
- Reading material: [the lesson](lesson:LNX-304-T07). Afterwards, try [the quiz](quiz:LNX-304-T07).
