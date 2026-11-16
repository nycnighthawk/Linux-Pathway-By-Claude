# Lab: the lifecycle of an estate host as code

`setup` writes `lifecycle.py` with a `plan` function that raises `NotImplementedError`. Implement it so each lifecycle action returns the ordered steps listed in the docstring: provision, patch (canary first), upgrade and decommission, with an extra replica check for IdM servers.

The order is the lesson: remove a host from monitoring before its certificates are revoked, and revoke its credentials before its DNS and inventory records go, so that nothing authenticates or alerts against a ghost.

## Run it

`bin/lpc course lab LNX-401 host-lifecycle`, or edit `lifecycle.py` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-401-T03).
