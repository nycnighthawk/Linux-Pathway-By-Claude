# Guide lab: a Windows client, a mapped drive and a shared printer

A Windows client joined to a domain, group policy and a printer driver cannot be created on a shared Linux runner, so this is a guided exercise with success criteria. Use a Windows 10 or 11 Pro virtual machine and a Samba AD DC and file/print server (or a Windows Server) in a lab, or a host at work. If you have none, record `none` where the key allows it and work through the criteria on paper. The grader checks that your report is complete and well formed; the evidence is on the machines.

## Starting state

`setup` writes `report.txt` in your working directory (`$LAB_DIR`) with eight question marks.

## Your task

| Key | How to find it |
|---|---|
| `dc_found_via` | how the client located its domain controller: `srv` (DNS SRV records), `netbios` or `hosts` (a manual entry; avoid) |
| `gpresult_shows_policy` | `yes` if `gpresult /r` on the client lists the policy you linked, `no` if not |
| `drive_mechanism` | `logon-script`, `gpp` (group policy preferences), `dfs` or `redirection` |
| `smbstatus_auth` | on the server, how `smbstatus` shows the mapped-drive session was authenticated: `krb5` or `ntlm` |
| `printer_queue_type` | `ipp-driverless`, `raw` or `postscript`, as defined with `lpadmin` and `cups options` |
| `driver_source` | where the Windows client got its driver: `inbox-ipp`, `print$` or `staged` |
| `point_and_print_restriction` | `enabled` if the client policy restricts driver installation from servers, otherwise `disabled` |
| `test_page_printed` | `yes` or `no` |

## Success criteria

- The client joined with the DC addressed through DNS and located it with SRV records; you can show `nltest /dsgetdc:acme.example` or `gpresult /r`.
- A drive letter is mapped for members of one group only, and `smbstatus` shows a Kerberos session.
- The Samba print server has `[printers]` and `[print$]`, and a queue that Windows can connect to by `\\server\queue`.
- You can say why a standard user could not install a vendor driver from the server, and one way to avoid needing to.
- You can explain which share holds drivers and what `cups options = raw` changes.
- Every key holds a value you read yourself.

## Grade it

`bin/lpc course lab LNX-302 windows-clients-printing-guide` checks the starting state and the structure of the sample answer; to grade your own report run `check` with `LAB_DIR` set to the directory that holds `report.txt`.

## Notes

- This lab is not run by CI (environment S: self-hosted); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-302-T07). Afterwards, try [the quiz](quiz:LNX-302-T07).
