# Lab: add a Flatpak remote and restrict an application's permissions

You will add a remote from a `.flatpakrepo` file to a private per-user installation, set its priority, and write a
permission override for an application, without installing anything on the host.

## Starting state

`setup` creates `lab.flatpakrepo` (a title, a `file://` URL and a base64 signing key), an empty `repo/` directory and a
blank `answers.txt`. `$LAB_DIR` is your working directory. The remote cannot be listed because the repository is empty,
so flatpak prints a warning when you add it. That is expected.

## Your task

Run `export XDG_DATA_HOME=$PWD/xdg` first. flatpak then keeps its per-user installation under `xdg/flatpak/`.

1. Add the remote: `flatpak --user remote-add labrepo lab.flatpakrepo`. Keep signature verification on.
2. Give the remote priority 5 with `flatpak --user remote-modify`, then show it with `flatpak --user remotes -d`.
3. For the application `org.example.Lab` create a per-user override that removes host filesystem access, grants
   read-only access to the user's documents folder and removes network access (`flatpak --user override ...`).
   Check it with `flatpak --user override --show org.example.Lab`.
4. Fill in `answers.txt`: the option that makes `flatpak remotes` print details, the directory of the default system
   installation, the command that removes runtimes nothing needs, and the command that changes permissions.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-104/flatpak-remotes/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-104/flatpak-remotes/check
```

## Notes

- The remote record is in `xdg/flatpak/repo/config`; the override is a small file in `xdg/flatpak/overrides/`.
- `--no-gpg-verify` exists for tests; a real remote should always have a key.
- The lab needs the package `flatpak`.
- Reading material: [the lesson](lesson:LNX-104-T04). Afterwards, try [the quiz](quiz:LNX-104-T04).
