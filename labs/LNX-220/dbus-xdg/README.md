# Lab: a D-Bus service started by name, configured through XDG directories

You will build a small GDBus service, tell a private session bus how to start it on demand, and give it a per-user
configuration file in the XDG location. The grader starts its own session bus, so nothing on your desktop is touched.

## Starting state

`setup` writes `src/server.c`. The service owns `org.example.Lab`, exports `/org/example/Lab` with a method
`Echo(s) -> s` and a read-only property `Greeting`, and reads its greeting from `$XDG_CONFIG_HOME/lab/greeting`
(through `g_get_user_config_dir()`, default `~/.config`).

## Your task

1. Build it: `cc -o server src/server.c $(pkg-config --cflags --libs gio-2.0)`.
2. Create `share/dbus-1/services/org.example.Lab.service` with a `[D-BUS Service]` section: `Name=org.example.Lab` and
   `Exec=` set to the absolute path of `server`.
3. Create `xdg/config/lab/greeting` containing `Howdy`.
4. Try it in a throwaway session bus:
   `XDG_CONFIG_HOME=$PWD/xdg/config XDG_DATA_DIRS=$PWD/share:/usr/share dbus-run-session -- busctl --user call org.example.Lab /org/example/Lab org.example.Lab Echo s there`.
   The reply should be `s "Howdy, there"`. Explore with `busctl --user tree org.example.Lab` and `introspect`.
5. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/dbus-xdg/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/dbus-xdg/check
```

## Notes

- The lab needs `gcc`, `pkg-config`, `libglib2.0-dev`, `dbus` (for `dbus-run-session`) and `systemd` tools for `busctl`.
- Reading material: [the lesson](lesson:LNX-220-T09). Afterwards, try [the quiz](quiz:LNX-220-T09).
