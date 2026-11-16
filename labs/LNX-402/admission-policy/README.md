# Lab: an admission decision in code

A policy engine evaluates rules like these at admission. `setup` writes `admit.py` with a stub; implement the six rules from its docstring so a pod is allowed only when it uses the approved registry, runs unprivileged as non-root, cannot escalate privilege, avoids host networking and has verified signatures, unless its namespace is exempt.

Real clusters express this with Pod Security levels, Kyverno or CEL policies; this model is only the decision logic (the exact Pod Security restricted rules are broader, to verify).

## Run it

`bin/lpc course lab LNX-402 admission-policy`, or edit `admit.py` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-402-T04).
