# Lab: write a tiny lockdep

The kernel's lockdep finds *possible* deadlocks without waiting for one. In this lab you write the core idea in Python.

`minilockdep.py` has a `check(trace)` stub. A trace is a list of `(task, "lock" | "unlock", name)` events. Implement:

- a list of locks currently held per task;
- when a task locks `B` while holding `A`, record the ordering edge `A -> B`;
- if the same task locks something it already holds, report that lock at once (self-deadlock);
- report a cycle as soon as an edge closes one, and return the lock names in the cycle;
- return `None` for a safe trace.

Note the third test: the two tasks run one after the other, so the program never hangs, but the *orderings* `A -> B` and `B -> A` are inconsistent and a different interleaving would deadlock. That is exactly the case lockdep exists for.
