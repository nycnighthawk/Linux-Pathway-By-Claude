# Lab: make the merged variables come out right

You will predict and then repair how Ansible merges variables from groups and hosts, and read the result with the
inspection command that an operator uses. Nothing connects to a machine: the lab only reads the inventory.

## Starting state

`setup` writes `ansible.cfg`, an inventory directory with five hosts in groups `prod`, `web`, `db`, `rack_a` and `edge`,
`group_vars` files that disagree on purpose, and a blank `answers.txt`. `$LAB_DIR` is your working directory.

## Your task

1. Run `ansible-inventory --graph --vars` and `ansible-inventory --host web01` to see where you are.
2. `web02` must listen on port 8081 while `web01` stays on 8080 and `db01` on 8443. Use a host variable file.
3. `rack_a` and `edge` both set `log_level` and sit at the same depth, so the alphabetical rule picks a winner you did not
   choose. Make `edge` win for `web01` and `web02` by giving the group a priority in the inventory source. A group
   variable file does not work for this setting, so put it in `inventory/hosts.yml`.
4. `prod` must replace the NTP list with `ntp1.example.org` then `ntp2.example.org` for every host in it.
5. Fill in `answers.txt`: the command that prints the merged variables of one host, the source that beats every other,
   the variable that settles ties between groups, the filter that merges dictionaries explicitly, and the lowest-ranking source.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-305/inventory-precedence/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-305/inventory-precedence/check
```

## Notes

- The lab needs the package `ansible-core` (the container installs it from apt).
- A list defined in a more specific group replaces the whole list from a less specific one; it does not append.
- Reading material: [the lesson](lesson:LNX-305-T01). Afterwards, try [the quiz](quiz:LNX-305-T01).
