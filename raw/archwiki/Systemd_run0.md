---
{"title": "Systemd/run0", "url": "https://wiki.archlinux.org/title/Systemd/run0", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Systemd/run0

Related articles

-   [Users and groups](../../en/Users_and_groups.html "Users and groups")
-   [sudo](../../en/Sudo.html "Sudo")
-   [doas](../../en/Doas.html "Doas")

[run0(1)](https://man.archlinux.org/man/run0.1) is a privilege elevation tool. It is implemented as an alternative invocation mode of [systemd-run(1)](https://man.archlinux.org/man/systemd-run.1). run0 provides a safer and more robust alternative to the [sudo](../../en/Sudo.html "Sudo") mechanism, without relying on [suid](../../en/Security.html#SUID_and_SGID_files "Suid") binaries. It uses [polkit](../../en/Polkit.html "Polkit") for authentication.

## Installation {#Installation}

*run0* is installed with [systemd](../../en/Systemd.html "Systemd").

[Install](../../en/Help:Reading.html#Installation_of_packages "Install") [polkit](https://archlinux.org/packages/?name=polkit), as it is required to handle authorization.

## Configuration {#Configuration}

*run0* does not have a configuration file. Configuration is done with [Polkit#Actions](../../en/Polkit.html#Actions "Polkit") and [Polkit#Authorization rules](../../en/Polkit.html#Authorization_rules "Polkit").

Default [Polkit#Administrator identities](../../en/Polkit.html#Administrator_identities "Polkit") grants group `wheel` the `addAdminRule`, therefore consider to add your user to the [wheel](../../en/Users_and_groups.html#User_groups "Users and groups") group to authenticate as your own user.

### Authentication caching {#Authentication_caching}

*sudo*-like authentication can be cached for a short period by the `ExpirationSeconds` setting in [polkitd.conf(5)](https://man.archlinux.org/man/polkitd.conf.5) (by default 5 minutes). Unlike *sudo*, invoking *run0* again does not reset the expiration countdown. Allowing *run0* to be cached requires installing the following *polkit* rule:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/polkit-1/rules.d/90-run0-password-caching.rules
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/* Allow authentication caching for run0 */
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.systemd1.manage-units") {
        return polkit.Result.AUTH_ADMIN_KEEP;
    }
});
```

## Usage {#Usage}

To use *run0*, simply prefix a command and its arguments with `run0` and a space:

    $ run0 cmd

For example, to use pacman:

    $ run0 pacman -Syu

To launch an interactive shell (similar to `sudo -i` or `su -l`), just type `run0`.

With the `--empower` option, privileged commands are run as the current user, avoiding a full root context. This is useful to run a command with privileges but still have all created files and directories be owned by your current user.

Options for `systemd-run` also apply. See [systemd-run(1)](https://man.archlinux.org/man/systemd-run.1) and [run0(1)](https://man.archlinux.org/man/run0.1).

**Tip** See [Security#SUID-free](../../en/Security.html#SUID-free "Security") for an advanced usage example.

## See also {#See_also}

-   [run0 announcement on Mastodon](https://mastodon.social/@pid_eins/112353324518585654)
-   [polkit authentication caching support](https://github.com/polkit-org/polkit/commit/7d44d62a02f090a5a71c4ca10d58c7c2b54881eb)
-   [polkitd: add support for INI config file and use it for auth expiration timer](https://github.com/polkit-org/polkit/pull/604/changes)
