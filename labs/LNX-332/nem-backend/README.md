# Lab: a backend contract and an exit mapping

A VMM that supports several accelerators defines one table of operations and maps each host exit onto its own events. `setup` writes `nem.py` with the list of required operations. Implement `missing_ops` (a completeness check that would run at start-up) and `map_exit` (unmapped exits must be loud).

This is a toy: the operation list and event names are illustrative, not VirtualBox's actual NEM interface. Read the real interface in the source tree before writing a patch (to verify).
