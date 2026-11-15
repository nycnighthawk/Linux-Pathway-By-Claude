# Guide lab: manage a Windows server from a Linux control node with Kerberos

A Windows host, a domain and the Kerberos plumbing for remote management cannot be created on a shared Linux runner, so this is a guided exercise with success criteria. Use a Windows Server evaluation VM joined to a lab domain (a Samba AD DC is enough for the Kerberos side), or a host at work. If you have none, record `none` where the key allows it and work through the criteria on paper. The grader checks that your report is complete and well formed; the evidence is on the control node and the Windows host.

## Starting state

`setup` writes `report.txt` in your working directory (`$LAB_DIR`) with ten question marks.

## Your task

| Key | How to find it |
|---|---|
| `connection_plugin` | the `ansible_connection` value you used: `psrp`, `winrm` or `ssh` |
| `authentication` | `kerberos`, `ntlm`, `certificate`, `credssp`, `basic` or `publickey` |
| `inventory_host_form` | `fqdn` or `ip`: what the inventory used as the host name |
| `ticket_source` | `kinit` (interactive ticket) or `keytab` |
| `cert_validation` | `validate` if the server certificate was checked, `ignore` if you switched checking off |
| `win_ping_result` | the result of `ansible windows -m ansible.windows.win_ping` |
| `feature_changed_first_run` | `yes` if a `win_feature` task reported `changed` the first time |
| `feature_changed_second_run` | the same task the second time |
| `double_hop_fix` | the approach you used or would use for a task that reads a share on a second server: `become`, `delegation`, `credssp` or `fetch` |
| `shell_task_idempotent` | `yes` or `no`: did a plain `win_shell` task report no change on the second run without `changed_when`? |

## Success criteria

- You reach the host with an encrypted transport and Kerberos or key authentication, not Basic over HTTP.
- The inventory names the host by its FQDN, so the service principal exists; `win_ping` returns `pong`.
- You installed a feature with `win_feature` and the second run reported no change.
- You can say why `win_shell` breaks idempotence and how `changed_when` repairs it.
- You can describe the double hop and name two ways around it.
- If you set `cert_validation=ignore` you can say what it exposes and how to replace it.
- Every key holds a value you read yourself.

## Grade it

`bin/lpc course lab LNX-302 ansible-windows-guide` checks the starting state and the structure of the sample answer; to grade your own report run `check` with `LAB_DIR` set to the directory that holds `report.txt`.

## Notes

- This lab is not run by CI (environment S: self-hosted); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-302-T08). Afterwards, try [the quiz](quiz:LNX-302-T08).
