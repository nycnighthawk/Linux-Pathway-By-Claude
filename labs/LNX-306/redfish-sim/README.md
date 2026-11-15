# Lab: drive a Redfish BMC with curl

`setup` starts a small mock Redfish service on a random local port, with generated credentials in `bmc.env` (`BMC_URL`, `BMC_USER`, `BMC_PASSWORD`). It stops itself after ten minutes; run `setup` again to restart it with a clean state. No hardware is involved.

## Your task

Write an executable script `bmc-pxe-once.sh` in the lab directory that:

1. Loads its settings from `bmc.env` (never paste the password into the script).
2. Reads the power state of `/redfish/v1/Systems/1` with `curl`.
3. Sets a one-time network boot: `PATCH` the system with `Boot.BootSourceOverrideTarget` = `Pxe` and `Boot.BootSourceOverrideEnabled` = `Once`.
4. Restarts the machine with a `POST` to `Actions/ComputerSystem.Reset` (a `ForceRestart` if it is on, `On` if it is off; do not use `ForceOff`).
5. Exits 0 on success and non-zero if any request fails (`curl -f`, `set -e`).

Explore first: `. ./bmc.env; curl -s -u "$BMC_USER:$BMC_PASSWORD" "$BMC_URL/redfish/v1/Systems/1"`. The reply lists the allowable values for the boot target and the reset types.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/redfish-sim/setup
# ...write bmc-pxe-once.sh...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/redfish-sim/check
```

## Notes

- Needs `python3` and `curl`. The mock is `mockbmc.py`, about 100 lines; read it to see how little a Redfish client needs.
- Real BMCs use HTTPS (so add `--cacert`, not `-k`, once you have the BMC's certificate) and differ in system ids and allowed values; read them from the service, do not assume `Systems/1`.
- Reading material: [the lesson](lesson:LNX-306-T07). Afterwards, try [the quiz](quiz:LNX-306-T07).
