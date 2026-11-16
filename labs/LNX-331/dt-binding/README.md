# Lab: which driver binds to which device tree node?

The platform bus matches a node's `compatible` list against each driver's `of_match_table`. `setup` writes `board.dts`, a small device tree, and `drivers.txt`, the match tables of five drivers.

## Rules (as in the kernel's device tree documentation; to verify for your tree)

- A node is considered only if it has no `status` property or `status = "okay"`. Any other status (such as `"disabled"`) means the node gets no device.
- The `compatible` property is a list, **most specific first**. The kernel tries the strings in order, and the first string that some driver lists decides the match. Later strings are fallbacks.
- A node no driver matches stays unbound (`none`).

## Your task

Fill `bindings.txt`: one line per node in file order, `<node@unit> <driver or none> <first reg cell as written>`. Two of the six nodes end up unbound, for different reasons.
