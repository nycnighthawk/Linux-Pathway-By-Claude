# Lab: an estate description that agrees with itself

The capstone keeps the whole estate in one file. `setup` writes `estate.yaml` with several defects. Edit it until `check` passes.

## Rules the grader enforces

- Host names and addresses are unique, and every address is inside `subnet`.
- Two hosts carry the `idm-server` role (a primary and a replica), one carries `samba-dc`, one `repo`, one `monitoring`.
- Six member servers exist besides the identity servers, from at least two families and three family/release pairs.
- The two realms and their DNS zones differ, a trust has a valid type and direction, and the NTP server is an inventory host.
- Every member runs `node-exporter`.
- `play_order` lists each stage once: DNS and time first, the trust after both directories, clients after the repository and the IdM server, monitoring last.

## Run it

`bin/lpc course lab LNX-401 estate-model`, or edit `estate.yaml` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-401-T01).
