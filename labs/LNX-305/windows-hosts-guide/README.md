# Guide lab: manage a Windows host from a Linux control node

A Windows host, a domain and the certificates for remote management cannot be created on a shared Linux runner, so this
is a guided exercise with success criteria. Use a Windows Server evaluation virtual machine, a cloud instance or a
host at work. If you have none, record `none` where the key allows it and work through the criteria on paper. The grader
checks that your report is complete and well formed; the evidence is on the Windows host.

## Starting state

`setup` writes `report.txt` in your working directory (`$LAB_DIR`) with nine question marks.

## Your task

| Key | How to find it |
|---|---|
| `connection_plugin` | the value of `ansible_connection` you used: `winrm`, `psrp` or `ssh` |
| `transport` | the authentication method: for example `kerberos`, `ntlm`, `negotiate`, `certificate`, `credssp`, `basic` or `publickey` |
| `port` | the port you connected to: 5985, 5986 or 22 |
| `cert_validation` | `validate` if the server certificate was checked, `ignore` if you switched checking off |
| `win_ping_result` | the result of `ansible windows -m ansible.windows.win_ping` |
| `windows_edition` | the OS caption reported by the facts of the host |
| `feature_changed_first_run` | `yes` if a `win_feature` task reported `changed` the first time |
| `feature_changed_second_run` | the same task the second time |
| `become_method` | `runas` if you escalated, otherwise `none` |

## Success criteria

- You can reach the host with an encrypted transport and an identity-based or key-based authentication, not Basic over HTTP.
- `win_ping` returns `pong`, and you gathered facts with `ansible.windows.setup`.
- You installed a Windows feature with `win_feature`; the second run reported no change.
- You can explain why the Python `command` and `shell` modules do not work on Windows, and what `win_shell` reports by default.
- If you set `cert_validation=ignore` you can say what that exposes and how to replace it.
- You can describe the double-hop problem and one way to avoid it.
- Every key holds a value you read yourself.

## Grade it

`bin/lpc course lab LNX-305 windows-hosts-guide` checks the starting state and the structure of the sample answer; to
grade your own report run `check` with `LAB_DIR` set to the directory that holds `report.txt`.

## Notes

- This lab is not run by CI (environment S: self-hosted); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-305-T09). Afterwards, try [the quiz](quiz:LNX-305-T09).
