# Guide lab: a field report on a wireless client

Radios, access points and an authentication server cannot be tested on a shared runner, so this is a guided exercise
with success criteria. Use a laptop or a virtual machine with a passed-through adapter if you have one; if the machine
has no wireless adapter, record `none` where the key says so and do the criteria on paper. The grader only checks that
your report is complete and well formed; the evidence is on the machine.

## Starting state

`setup` writes `report.txt` in your working directory (`$LAB_DIR`) with six question marks.

## Your task

| Key | How to find it |
|---|---|
| `wifi_device` | the interface of type wifi in `nmcli device status`, or `iw dev`; `none` if there is no adapter |
| `rfkill_state` | `rfkill list wifi`: `unblocked`, `soft-blocked` or `hard-blocked`; `none` if nothing is listed |
| `regdomain` | the `country` line of `iw reg get` (two letters, or `00` for the world default) |
| `security_mode` | `nmcli -f SSID,SECURITY device wifi list` for the network you use (`open`, `wpa2-personal`, `wpa3-personal`, `wpa2-enterprise`, `wpa3-enterprise`, `wep`), or `none` |
| `eap_method` | `nmcli connection show <profile> | grep 802-1x.eap` (`peap`, `ttls`, `tls`), or `none` for a personal or open network |
| `server_cert_validated` | `yes` if the profile sets `802-1x.ca-cert`, `no` if it does not, `na` for a network without 802.1X |

## Success criteria

- You switched the radio off and on again with `nmcli radio wifi off` and `on`, and saw `rfkill list` follow.
- You read the regulatory domain and, if it was `00`, understood why some channels may be missing.
- For one enterprise profile (yours or an example from a classmate or the lesson), you can say which EAP method it uses,
  where the password is stored, and whether the client would notice a rogue access point.
- Every key in the report holds a value you read yourself.

## Grade it

`bin/lpc course lab LNX-201 wifi-field-report` checks the starting state and the structure of the sample answer;
to grade your own report run `check` with `LAB_DIR` set to the directory that holds `report.txt`.

## Notes

- This lab is not run by CI (environment H: hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-201-T09). Afterwards, try [the quiz](quiz:LNX-201-T09).
