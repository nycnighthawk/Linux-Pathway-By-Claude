# Guide lab: plan a live migration

A real live migration needs two hypervisors that can reach each other, and a shared runner cannot offer that. This is a guided exercise with success criteria: you write a migration plan for two hosts you control (or invent a consistent pair), and the grader checks that the plan is complete and internally consistent. The evidence is in doing it for real if you have the hardware.

## Starting state

`setup` writes `migration-plan.txt` in your working directory (`$LAB_DIR`) with question marks.

## Your task

| Key | What to put |
|---|---|
| `guest`, `source_host`, `dest_host` | names; the two hosts must differ |
| `shared_storage` | `yes` when both hosts open the same image, otherwise `no` |
| `hosts_identical` | `yes` only if both hosts have the same CPU model |
| `cpu_model` | `host-model`, `host-passthrough` or `named-baseline`; passthrough is allowed only when the hosts are identical |
| `machine_type_pinned` | `yes`: the guest uses a versioned machine type |
| `downtime_ms` | the downtime budget, 20 to 5000 |
| `postcopy`, `tls` | `yes` or `no`; explain to yourself why |
| `firewall_ports` | what the destination must allow; include the QEMU range 49152-49215 |
| `migrate_command` | one `virsh migrate` line with `--live` and a `qemu+ssh://` or `qemu+tls://` destination; add `--copy-storage-all` or `-inc` when storage is not shared, `--postcopy` when you chose it and `--tls` when you chose it; never `--unsafe` |
| `verify_steps`, `abort_plan` | at least six words each |

## Success criteria

- You compared the CPUs with `virsh cpu-compare` or `virsh hypervisor-cpu-baseline` before choosing the CPU model.
- You can say what state the guest is in on both hosts if the network fails half way, for pre-copy and for post-copy.
- You watched `virsh domjobinfo` during at least one migration (or can explain each field).
- You rehearsed the evacuation before you needed it.

## Grade it

`bin/lpc course lab LNX-308 migration-plan` checks the starting state and the structure of the sample answer; to grade your own plan run `check` with `LAB_DIR` set to the directory that holds `migration-plan.txt`.

## Notes

- This lab is not run by CI (environment S: two hypervisors are needed); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-308-T05). Afterwards, try [the quiz](quiz:LNX-308-T05).
