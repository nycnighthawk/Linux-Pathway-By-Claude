# Lab: write a minimal CNI plugin

Complete the shell plugin `minimal` in your working directory (`$LAB_DIR`) so it follows the CNI contract. The check drives it like a runtime would, using a real network namespace.

## Starting state

`setup` writes `minimal`, which prints an error for every command. It needs `iproute2`, root rights and network namespace support.

## Your task

The configuration JSON on stdin has `cniVersion`, `name`, `type`, `bridge` (bridge name), `address` (such as `10.22.0.5/24`) and `gateway` (such as `10.22.0.1`).

1. `VERSION`: print `{"cniVersion":"1.0.0","supportedVersions":["0.4.0","1.0.0"]}`.
2. `ADD`: create the bridge if it does not exist and give it the gateway address (with the prefix length of `address`); create a veth pair; move one end into `CNI_NETNS` as `CNI_IFNAME`; give it `address`; set loopback and the interface up; add a default route via `gateway`; attach the host end (named `veth` plus the first 8 characters of `CNI_CONTAINERID`) to the bridge and bring it up; print a result JSON `{"cniVersion":"1.0.0","interfaces":[{"name":"<ifname>","sandbox":"<netns>"}],"ips":[{"address":"<address>","gateway":"<gateway>","interface":0}]}`.
3. `DEL`: delete the host-side veth; exit 0 even if it is already gone. Run it twice and it must still exit 0.
4. Any other command: print `{"cniVersion":"1.0.0","code":4,"msg":"unsupported command"}` and exit 1.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/minimal-cni/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/minimal-cni/check
```

Reading: [the lesson](lesson:LNX-312-T02); then [the quiz](quiz:LNX-312-T02).
