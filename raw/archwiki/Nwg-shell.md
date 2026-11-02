---
{"title": "Nwg-shell", "url": "https://wiki.archlinux.org/title/Nwg-shell", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Nwg-shell

The [nwg-shell](https://nwg-piotr.github.io/nwg-shell/) project aims to create a consistent, GTK based user interface for the [Sway](../en/Sway.html "Sway") Wayland Compositor.

It also supports [Hyprland](../en/Hyprland.html "Hyprland") since version 0.5.0 [\[1\]](https://github.com/nwg-piotr/nwg-shell/releases/tag/v0.5.0).

**Note** Hyprland support is an addition to the shell, not a standalone feature.

## Installation {#Installation}

The `nwg-shell` components can be [installed](../en/Help:Reading.html#Installation_of_packages "Install") with the [nwg-shell](https://archlinux.org/packages/?name=nwg-shell) (meta) package.

**Note**

-   Support for Hyprland requires a few additional packages. Check the list of optional dependencies for the [nwg-shell](https://archlinux.org/packages/?name=nwg-shell) package.
-   Most components of the `nwg-shell` can also be installed and used standalone. See [#Shell components](#Shell_components) for a full list of components.

The `nwg-shell-installer` script (see [#Configuration](#Configuration)) also expects a [web browser](../en/Web_browser.html "Web browser"), a [file manager](../en/List_of_applications/Utilities.html#File_managers "List of applications/Utilities") and a [text editor](../en/Text_editor.html "Text editor") to be installed **before** being run in order to setup keybindings properly. The suggested ones are [firefox](https://archlinux.org/packages/?name=firefox), [thunar](https://archlinux.org/packages/?name=thunar) and [typobuster](https://archlinux.org/packages/?name=typobuster) but other ones can be installed instead.

## Configuration {#Configuration}

The [nwg-shell](https://archlinux.org/packages/?name=nwg-shell) package provides the `nwg-shell-installer` script which can be run to interactively generate a default configuration for every `nwg-shell` components as well as a custom configuration for `Sway/Hyprland`.

**Warning** The `nwg-shell-installer` script is made to be run on fresh installations as it will restore/overwrite configurations and style sheets of each `nwg-shell` components as well as overwrite the `Sway` (or `Hyprland`) main configuration (a backup of the main `Sway/Hyprland` configuration file is created by the script beforehand).

For Sway, run:

    $ nwg-shell-installer -a

For Sway and Hyprland:

    $ nwg-shell-installer -a -hypr

**Note** The `nwg-shell-installer` script expects a [web browser](../en/Web_browser.html "Web browser"), a [file manager](../en/List_of_applications/Utilities.html#File_managers "List of applications/Utilities") and a [text editor](../en/Text_editor.html "Text editor") to be installed **before** being run in order to setup keybindings properly. The suggested ones are [firefox](https://archlinux.org/packages/?name=firefox), [thunar](https://archlinux.org/packages/?name=thunar) and [typobuster](https://archlinux.org/packages/?name=typobuster) but other ones can be installed instead.

Alternatively, one can modify each `nwg-shell`components\' configurations and style sheets graphically or by modifying the related files under `~/.config/`*`component_name`*.

Finally, one can [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") the `greetd.service` (so [greetd](../en/Greetd.html "Greetd") will be started at boot) and [set up the `nwg-hello` greeter](../en/Greetd.html#nwg-hello "Greetd").

## Shell components {#Shell_components}

The [nwg-shell](https://archlinux.org/packages/?name=nwg-shell) package provides the following `nwg-shell` components:

**Note** Most of these components can be installed and used standalone.

-   **azote** --- Wallpaper manager for wlroots-based compositors and some other WMs.

[https://github.com/nwg-piotr/azote](https://github.com/nwg-piotr/azote) \|\| [azote](https://archlinux.org/packages/?name=azote)

-   **gopsuinfo** --- A gopsutil-based command to display system usage info as text in panels like Waybar or icon/text in tint2 and nwg-panel executors.

[https://github.com/nwg-piotr/gopsuinfo](https://github.com/nwg-piotr/gopsuinfo) \|\| [gopsuinfo](https://archlinux.org/packages/?name=gopsuinfo)

-   **nwg-bar** --- GTK3-based button bar for wlroots-based compositors.

[https://github.com/nwg-piotr/nwg-bar](https://github.com/nwg-piotr/nwg-bar) \|\| [nwg-bar](https://archlinux.org/packages/?name=nwg-bar)

-   **nwg-clipman** --- a GTK3-based GUI for cliphist.

[https://github.com/nwg-piotr/nwg-clipman](https://github.com/nwg-piotr/nwg-clipman) \|\| [nwg-clipman](https://archlinux.org/packages/?name=nwg-clipman)

-   **nwg-displays** --- Output management utility for sway and Hyprland.

[https://github.com/nwg-piotr/nwg-displays](https://github.com/nwg-piotr/nwg-displays) \|\| [nwg-displays](https://archlinux.org/packages/?name=nwg-displays)

-   **nwg-dock** --- GTK3-based dock for Sway.

[https://github.com/nwg-piotr/nwg-dock](https://github.com/nwg-piotr/nwg-dock) \|\| [nwg-dock](https://archlinux.org/packages/?name=nwg-dock)

-   **nwg-dock-hyprland** --- GTK3-based dock for Hyprland.

[https://github.com/nwg-piotr/nwg-dock-hyprland](https://github.com/nwg-piotr/nwg-dock-hyprland) \|\| [nwg-dock-hyprland](https://archlinux.org/packages/?name=nwg-dock-hyprland)

-   **nwg-drawer** --- Application drawer for wlroots-based Wayland compositors.

[https://github.com/nwg-piotr/nwg-drawer](https://github.com/nwg-piotr/nwg-drawer) \|\| [nwg-drawer](https://archlinux.org/packages/?name=nwg-drawer)

-   **nwg-hello** --- GTK3-based greeter for greetd written in python.

[https://github.com/nwg-piotr/nwg-hello](https://github.com/nwg-piotr/nwg-hello) \|\| [nwg-hello](https://archlinux.org/packages/?name=nwg-hello)

-   **nwg-icon-picker** --- GTK icon chooser with a text search option.

[https://github.com/nwg-piotr/nwg-icon-picker](https://github.com/nwg-piotr/nwg-icon-picker) \|\| [nwg-icon-picker](https://archlinux.org/packages/?name=nwg-icon-picker)

-   **nwg-look** --- GTK3 settings editor adapted to work in the wlroots environment.

[https://github.com/nwg-piotr/nwg-look](https://github.com/nwg-piotr/nwg-look) \|\| [nwg-look](https://archlinux.org/packages/?name=nwg-look)

-   **nwg-menu** --- MenuStart plugin to nwg-panel, also capable of working standalone.

[https://github.com/nwg-piotr/nwg-menu](https://github.com/nwg-piotr/nwg-menu) \|\| [nwg-menu](https://archlinux.org/packages/?name=nwg-menu)

-   **nwg-panel** --- GTK3-based panel for sway and Hyprland Wayland compositors.

[https://github.com/nwg-piotr/nwg-panel](https://github.com/nwg-piotr/nwg-panel) \|\| [nwg-panel](https://archlinux.org/packages/?name=nwg-panel)

-   **nwg-readme-browser** --- WebKitGTK-based README file browser.

[https://github.com/nwg-piotr/nwg-readme-browser](https://github.com/nwg-piotr/nwg-readme-browser) \|\| [nwg-readme-browser](https://archlinux.org/packages/?name=nwg-readme-browser)

-   **nwg-shell** --- Installer & meta-package for the nwg-shell project: a GTK3-based shell for Sway and Hyprland Wayland compositors.

[https://github.com/nwg-piotr/nwg-shell](https://github.com/nwg-piotr/nwg-shell) \|\| [nwg-shell](https://archlinux.org/packages/?name=nwg-shell)

-   **nwg-shell-config** --- nwg-shell configuration utility.

[https://github.com/nwg-piotr/nwg-shell-config](https://github.com/nwg-piotr/nwg-shell-config) \|\| [nwg-shell-config](https://archlinux.org/packages/?name=nwg-shell-config)

-   **nwg-shell-wallpapers** --- Selection of wallpapers contributed to the nwg-shell project.

[https://github.com/nwg-piotr/nwg-shell-wallpapers](https://github.com/nwg-piotr/nwg-shell-wallpapers) \|\| [nwg-shell-wallpapers](https://archlinux.org/packages/?name=nwg-shell-wallpapers)
