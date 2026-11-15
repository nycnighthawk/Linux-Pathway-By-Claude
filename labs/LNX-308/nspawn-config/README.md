# Lab: configure a system container the same way in nspawn and Incus

You describe one build container twice: as the files `systemd-nspawn` and systemd read, and as an Incus profile. The checks are the safe defaults for a container that must not be a back door to the host.

## Starting state

`setup` writes `bld.nspawn`, `limits.conf` and `incus-profile.yaml` into your working directory (`$LAB_DIR`), each with TODO comments.

## Your task

| File | Requirement |
|---|---|
| `bld.nspawn` | `[Exec]` boots the container's init (`Boot=yes`) inside a user namespace (`PrivateUsers=pick`); `[Network]` gives it a virtual Ethernet pair; `[Files]` mounts `/srv/src` read-only at `/src` |
| `limits.conf` | the service drop-in sets `MemoryMax=1G`, `TasksMax=512` and `Delegate=yes` |
| `incus-profile.yaml` | `limits.memory: 1GiB`, `limits.cpu: "2"`, not privileged, and a disk device that exposes `/srv/src` read-only at `/src` |

Do not add broad capabilities and do not bind the source directory read-write.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-308/nspawn-config/setup
# ...edit the three files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-308/nspawn-config/check
```

## Notes

- Needs `python3` and PyYAML. On a real host the files go to `/etc/systemd/nspawn/bld.nspawn` and `/etc/systemd/system/systemd-nspawn@bld.service.d/limits.conf`, followed by `systemctl daemon-reload` and `machinectl start bld`; the profile is loaded with `incus profile edit`.
- Reading material: [the lesson](lesson:LNX-308-T06). Afterwards, try [the quiz](quiz:LNX-308-T06).
