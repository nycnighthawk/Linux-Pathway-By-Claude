# Lab: write a toy eBPF verifier

The kernel does not trust eBPF programs. Before one runs, the **verifier** walks every possible path through it, tracking what each register holds, and rejects anything that could read uninitialised data, loop forever, access memory out of bounds, dereference a possible NULL, leak a kernel pointer or fall off the end.

`miniverifier.py` defines a tiny instruction set (see its docstring) and a `verify(prog)` stub. Implement it:

- explore **both** sides of every conditional jump (use a work list of `(pc, register types)`),
- track a type per register: `uninit`, `scalar`, `ctx`, `mapval` or `mapval_or_null`,
- after `call_lookup` the result may be NULL; only the fall-through side of `jeq_null` makes it a usable `mapval`,
- a call destroys `r1` to `r5`,
- reject backward jumps (no loops), loads outside the object, uninitialised reads, pointer arithmetic, returning a pointer and running off the end.

Return `None` for a safe program or a message containing one of the keywords listed in the docstring. The real verifier does the same job with far richer state (value ranges, stack slots, reference tracking), which is why its source is large.
