# Lab: configure OpenSSH and PowerShell 7 remoting for a Windows server

You will write the server-side configuration that makes a Windows host reachable by key-only SSH with PowerShell 7 remoting, and the PowerShell script that applies the two Windows-specific settings that trip up Linux administrators: the default shell and the permissions of the administrators' key file. The grader is a Python script, so it runs the same way on the Windows runner as on Linux; it inspects your files and does not need a Windows server.

## Starting state

`setup` writes `sshd_config` (password logins on, no PowerShell subsystem), a stub `harden-keys.ps1` and `answers.txt`.

## Your task

1. `sshd_config`: `PubkeyAuthentication yes`, `PasswordAuthentication no`, a `Subsystem powershell` line that starts `pwsh.exe -sshs` through the 8.3 short path `C:/Progra~1/PowerShell/7/pwsh.exe`, and, after those global lines, a `Match Group administrators` block that sets `AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys`.
2. `harden-keys.ps1`: sets the string value `DefaultShell` under `HKLM:\SOFTWARE\OpenSSH` to `C:\Program Files\PowerShell\7\pwsh.exe`; resets the ACL of `$env:ProgramData\ssh\administrators_authorized_keys` with `icacls` (`/inheritance:r`, full control for `Administrators` and `SYSTEM` only); and, if it writes the key file, uses `-Encoding ascii` or `utf8NoBOM`, never the UTF-16 default of Windows PowerShell 5.1.
3. `answers.txt`: `transport_switch` (the `Enter-PSSession` parameter that selects SSH), `event_log_channel` (where the OpenSSH server logs on Windows), `pwsh_preinstalled_on_server_2025` (`yes` or `no`) and `delegation_with_ssh` (`yes` or `no`: can an SSH remoting session reach a third server with the caller's identity).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-302/ssh-pwsh-remoting/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-302/ssh-pwsh-remoting/check
```

On a Windows machine run the two scripts with `python`. They need only Python 3.

## Notes

- On a real server: `Get-WindowsCapability -Online -Name 'OpenSSH.Server*' | Add-WindowsCapability -Online`, `Start-Service sshd`, `sshd -T`, and from Linux `Enter-PSSession -HostName win01 -UserName alice -KeyFilePath ~/.ssh/id_ed25519`.
- Reading material: [the lesson](lesson:LNX-302-T06). Afterwards, try [the quiz](quiz:LNX-302-T06).
