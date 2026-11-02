---
{"title": "GNOME/Troubleshooting", "url": "https://wiki.archlinux.org/title/GNOME/Troubleshooting", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# GNOME/Troubleshooting

## Shell freezes {#Shell_freezes}

In the event of a shell freeze (which might be caused by certain appearance tweaks, malfunctioning extensions or perhaps a lack of available memory), restarting the shell by pressing `Alt+F2` and then entering `r` may not be possible.

In this case, try switching to another TTY (`Ctrl+Alt+F2`) and entering the following command: `pkill -HUP gnome-shell`. It may take a few seconds before the shell successfully restarts. On X11, restarting the shell in this fashion should not log the user out, but it is a good idea to try and ensure that all work is saved anyway; on Wayland (currently the default), restarting the shell kills the whole session, so everything will be lost.

If this fails, the [Xorg](../../en/Xorg.html "Xorg") server will need to be restarted either by `pkill X` for console logins or by [restarting](../../en/Help:Reading.html#Control_of_systemd_units "Restart") `gdm.service` for GDM logins. Bear in mind that restarting the Xorg server will log the user out, so try to ensure that all work is saved before attempting this.

## Incorrect application defaults {#Incorrect_application_defaults}

When installing applications for the first time you may find that GNOME has the wrong application associated to a certain protocols - for instance, *easytag* becomes the folder handler instead of [GNOME Files](../../en/GNOME_Files.html "GNOME Files").

For GNOME Files see the following page: [GNOME Files#Files is no longer the default file manager](../../en/GNOME_Files.html#Files_is_no_longer_the_default_file_manager "GNOME Files").

To query the current associated application and recommended apps for pdfs in this case run:

    $ xdg-mime query default application/pdf

To change the default app for pdfs to Document Viewer, run the following command:

    $ xdg-mime default org.gnome.Evince.desktop application/pdf

For other applications, default handler settings are detailed on the following page: [Default applications](../../en/Default_applications.html "Default applications").

**Note**

There is another mime type association command. If the current associated app queried using `xdg-mime query default <mime-type>` is already correct, but still the wrong app is handling the type, try this:

-   Check the `gio` association by running: `gio mime application/pdf`
-   Change the association, if needed, using `gio mime application/pdf org.gnome.Evince.desktop` to Document Viewer

## Search does not list any local files {#Search_does_not_list_any_local_files}

In order for Gnome\'s localsearch tool to index your local files, they must be stored in an [XDG compliant directory](https://specifications.freedesktop.org/basedir-spec/latest/) (such as \'Documents\' or \'Music\'). For more information, see [XDG user directories](../../en/XDG_user_directories.html "XDG user directories").

You can also configure localsearch to recursively search inside specific directories. These can be specified via *Settings \> Search \> Search locations*.

## GNOME Online Accounts settings page does not show properly {#GNOME_Online_Accounts_settings_page_does_not_show_properly}

In some cases, due to interactions with Alacarte (menu editor), GNOME Online accounts settings page would not show. If that happens, \"Restore System Configuration\" in Alacarte can restore missing functions to gnome-control-center. (See [https://bugzilla.redhat.com/show_bug.cgi?id=1520431](https://bugzilla.redhat.com/show_bug.cgi?id=1520431).)

## GNOME Online Accounts blank pop-up window when logging in {#GNOME_Online_Accounts_blank_pop-up_window_when_logging_in}

Some services require authentication to log in (Google, Microsoft, etc.), so in some situations (such as Nvidia drivers) the popup will go blank instead of redirecting to the login page. To solve this problem, temporarily disable WebKit Composite.

    $ WEBKIT_DISABLE_COMPOSITING_MODE=1 gnome-control-center online-accounts

## Cannot change settings in dconf-editor {#Cannot_change_settings_in_dconf-editor}

When one cannot set settings in [dconf](https://archlinux.org/packages/?name=dconf), it is possible their dconf user settings are corrupt. In this case it is best to delete the user dconf files in `~/.config/dconf/user*` and set the settings in dconf-editor after.

## When an extension breaks the shell {#When_an_extension_breaks_the_shell}

When enabling shell extensions causes GNOME breakage, you should first remove the *user-theme* and *auto-move-windows* extensions from their installation directory.

The installation directory could be one of `~/.local/share/gnome‑shell/extensions`, `/usr/share/gnome‑shell/extensions` or `/usr/local/share/gnome‑shell/extensions`. Removing these two extension-containing folders may fix the breakage. Otherwise, isolate the problem extension with trial‑and‑error.

Removing or adding an extension-containing folder to the aforementioned directories removes or adds the corresponding extension to your system. Details on GNOME Shell extensions are available at the [GNOME web site.](https://wiki.gnome.org/Projects/GnomeShell/Extensions)

If you have trouble with uninstalling an extension via [extensions.gnome.org/local](https://extensions.gnome.org/local/), then probably they have been installed as system-wide extensions with the [gnome-shell-extensions](https://archlinux.org/packages/?name=gnome-shell-extensions) package. Removing the package again obviously affects all user accounts.

## Extensions do not work after GNOME 3 update {#Extensions_do_not_work_after_GNOME_3_update}

**Note** Please bear in mind that whilst the methods below will allow you to **try** and activate an extension with an unsupported version of GNOME Shell, it is by no means a guarantee that the extension will work successfully. The most likely outcome of trying to activate such an extension is that GNOME Shell will crash and then restart.

Before trying the workarounds below, check if an update is available for the extension by visiting [extensions.gnome.org/local](https://extensions.gnome.org/local).

If there is no update for your current GNOME version yet, use the following command to disable version validation for extensions:

    $ gsettings set org.gnome.shell disable-extension-version-validation true

Alternatively, you could modify the extension itself, changing the supported shell version to satisfy the version validation. See the method below.

Locate the folder where your extensions are installed. It might be `~/.local/share/gnome-shell/extensions` or `/usr/share/gnome-shell/extensions`.

Edit each occurrence of `metadata.json` which appears in each extension sub-folder.

  --------------------------- ----------------------------
  Insert:                     `"shell-version": ["3.x"]`
  Instead of (for example):   `"shell-version": ["3.4"]`
  --------------------------- ----------------------------

`"3.x"` indicates the extension works with every shell version. If it breaks, you will know to change it back.

## Keyboard shortcut do not work with only conky running {#Keyboard_shortcut_do_not_work_with_only_conky_running}

The GNOME shell keyboard shortcuts like `Alt+F2`, `Alt+F1`, and the media key shortcuts do not work if conky is the only program running. However, if another application like *gedit* is running, then the keyboard shortcuts work.

Solution: edit `.conkyrc`

    own_window yes
    own_window_transparent yes
    own_window_argb_visual yes
    own_window_type dock
    own_window_class Conky
    own_window_hints undecorated,below,sticky,skip_taskbar,skip_pager

## Unable to apply stored configuration for monitors {#Unable_to_apply_stored_configuration_for_monitors}

If you encounter this message try to disable the *xrandr* `gnome-settings-daemon plugin`:

    $ dconf write /org/gnome/settings-daemon/plugins/xrandr/active false

## Consistent cursor theme {#Consistent_cursor_theme}

See [Cursor themes#Desktop environments](../../en/Cursor_themes.html#Desktop_environments "Cursor themes").

## Windows cannot be modified with Alt-Key + mouse-button {#Windows_cannot_be_modified_with_Alt-Key_+_mouse-button}

In GNOME 3.6 and above, the mouse button modifier (the key that allows you to drag a window from a location other than the titlebar) is the `Super` key instead of the `Alt` key which was used in the past. The change was made in response to the following [bug report](https://bugzilla.gnome.org/show_bug.cgi?id=607797).

To change the mouse button modifier back to the `Alt` key, execute the following:

    $ gsettings set org.gnome.desktop.wm.preferences mouse-button-modifier '<Alt>'

**Note** It is not possible to change this with *System settings* \> *Keyboard* \> *Shortcuts*

## Slow loading of system icons/slow GDM login {#Slow_loading_of_system_icons/slow_GDM_login}

Problems with the loading of system icons, such the ones in the title bar of Files, might be solved by executing the following command:

    # gdk-pixbuf-query-loaders --update-cache

Running the aforementioned command may also fix repeated occurrences of the \"Oh no! Something has gone wrong!\" error screen and/or very slow loading and login with GDM as described in the following [forum thread](https://bbs.archlinux.org/viewtopic.php?pid=1414157).

## Artifacts when maximizing windows {#Artifacts_when_maximizing_windows}

Maximizing windows may cause artifacts as of GNOME 3.12.0 - see the following [forum thread](https://bbs.archlinux.org/viewtopic.php?id=183617) and [bug report](https://bugzilla.gnome.org/show_bug.cgi?id=728385). A solution is detailed in the following section: [#Tear-free video with Intel HD Graphics](#Tear-free_video_with_Intel_HD_Graphics).

## Tear-free video with Intel HD Graphics {#Tear-free_video_with_Intel_HD_Graphics}

DRI3

According to a [bug report](https://bugzilla.gnome.org/show_bug.cgi?id=711028#c2), DRI3 includes the `buffer_age` extension that allows GNOME Shell\'s Mutter compositor to sync windows to vblank in an efficient way. Since version `1:2.99.917+682+g4eaab17-1`, DRI3 is enabled by default in [xf86-video-intel](https://archlinux.org/packages/?name=xf86-video-intel) [\[1\]](https://gitlab.archlinux.org/archlinux/packaging/packages/xf86-video-intel/-/commit/ef20fe3ac9109d5d51ad39e6a87d85ade2646605).

Intel TearFree

Enabling the [Xorg Intel TearFree option](../../en/Intel_graphics.html#Tearing "Intel graphics") is a known workaround for tearing problems on Intel adapters. However, the way this option acts increases memory consumption and lowers performance, see [the original bug report\'s final comment](https://bugs.freedesktop.org/show_bug.cgi?id=37686#c123).

Mutter tweaks

**Note** This workaround has been [reported](https://bugzilla.gnome.org/show_bug.cgi?id=711028#c0) to have side effects and may not fix tearing in all cases.

GNOME Shell\'s Mutter compositor has a tweak known to address tearing problems (see [the original suggestion for this fix](https://bugzilla.gnome.org/show_bug.cgi?id=657071#c1) and its mention in [the Freedesktop bug report](https://bugs.freedesktop.org/show_bug.cgi?id=37686#c59)). To enable this tweak, append the following line to `/etc/environment`: `CLUTTER_PAINT=disable-clipped-redraws:disable-culling`. Then restart the Xorg server.

Disable fullscreen unredirect

GNOME Shell does by default unredirect fullscreen applications. This may result in tearing. You can disable this with the gnome shell extension [gnome-shell-extension-disable-unredirect](https://aur.archlinux.org/packages/gnome-shell-extension-disable-unredirect/)^AUR^.

## Window opens behind other windows when using multiple monitors {#Window_opens_behind_other_windows_when_using_multiple_monitors}

This is possibly a bug in GNOME Shell which causes new windows to open behind others. To fix this issue, one can run the following command:

    $ gsettings set org.gnome.shell.overrides workspaces-only-on-primary false

## Lock button fails to re-enable touchpad {#Lock_button_fails_to_re-enable_touchpad}

Some laptops have a touchpad lock button that disables the touchpad so that users can type without worrying about touching the touchpad. Currently, it appears that although GNOME can lock the touchpad by pressing this button, it cannot unlock it. If the touchpad gets locked you can run the following to unlock it:

    $ xinput set-prop "SynPS/2 Synaptics TouchPad" "Device Enabled" 1

## GNOME Shell keyboard sources menu not visible {#GNOME_Shell_keyboard_sources_menu_not_visible}

A menu showing the keyboard input sources (for example \'en\' for an English keyboard layout) should be visible next to the status area containing icons for network, volume and power sources. If the keyboard sources menu is not visible, this is probably because you have configured your [Xorg](../../en/Xorg.html "Xorg") keyboard layout in a way which GNOME does not recognise.

To ensure that the menu is visible, remove any Xorg keyboard configuration you might have created and set the keyboard locale using [localectl](../../en/Keyboard_configuration_in_Xorg.html#Using_localectl "Keyboard configuration in Xorg").

Upon running the command and then logging out, you should find that the keyboard input sources menu is visible in GDM and in the GNOME Shell desktop. See [Input sources in GNOME](https://blogs.gnome.org/mclasen/2012/09/21/input-sources-in-gnome/) for more information.

## Mouse cursor missing {#Mouse_cursor_missing}

When using a separate [window manager](../../en/Window_manager.html "Window manager") with *gnome-settings-daemon*, the mouse cursor may vanish. Run:

    $ gsettings set org.gnome.settings-daemon.plugins.cursor active false

## No restart button in session menu when screen is locked {#No_restart_button_in_session_menu_when_screen_is_locked}

If [XScreenSaver](../../en/XScreenSaver.html "XScreenSaver") is installed, ensure that it is not running at startup, see [GNOME#Autostart](../../en/GNOME.html#Autostart "GNOME").

## PulseAudio system-wide causes delay in GNOME and GDM {#PulseAudio_system-wide_causes_delay_in_GNOME_and_GDM}

If you are running [PulseAudio](../../en/PulseAudio.html "PulseAudio") in system-wide mode, the PulseAudio 7.0 upgrade breaks [GDM](../../en/GDM.html "GDM") and GNOME. See [this forum post](https://bbs.archlinux.org/viewtopic.php?id=203051) for more information.

## GNOME crashes when trying to reorder applications in the GNOME Shell Dash {#GNOME_crashes_when_trying_to_reorder_applications_in_the_GNOME_Shell_Dash}

The dash is the \"toolbar\" that appears, by default, [on the left](https://en.wikipedia.org/wiki/GNOME_Shell#Design_components "wikipedia:GNOME Shell") when you click Activities. Applications can be reordered in the dash by dragging and dropping. If this fails, and/or causes GNOME to crash, try [changing your icon theme](https://bbs.archlinux.org/viewtopic.php?id=171689).

## No H264 Video in GNOME Video Player (Totem) {#No_H264_Video_in_GNOME_Video_Player_(Totem)}

See [Codecs and containers#No H264, mpg4 or Musepack (.mpc) in Totem Player](../../en/Codecs_and_containers.html#No_H264,_mpg4_or_Musepack_(.mpc)_in_Totem_Player "Codecs and containers").

## No suspend on LID closure {#No_suspend_on_LID_closure}

GNOME defaults to this behaviour about suspension:

-   No external monitor attached, computer goes in suspension when LID closes.
-   External monitor attached, computer does not go in suspension when LID closes.

Currently [gnome-tweaks](https://archlinux.org/packages/?name=gnome-tweaks) is not able to modify the behaviour on the second case, when a monitor is connected to the computer. While it can inhibit suspension with no monitor attached.

**Note** Behaviour on LID closure is controlled also by systemd. See [Power management#ACPI events](../../en/Power_management.html#ACPI_events "Power management").

## gnome-shell / gnome-session crashes on session startup {#gnome-shell_/_gnome-session_crashes_on_session_startup}

Sometimes `gnome-session` crashes immediately after login. This might be more visible on wayland and it might seem as if every second login attempt fails. The problem can be temporarily worked around by removing the files in `~/.config/gnome-session/saved-session`. A more lasting work-around is to disable the session manager\'s `auto-save-session` feature:

    $ gsettings set org.gnome.SessionManager auto-save-session false

## Low OpenGL performance and stuttering {#Low_OpenGL_performance_and_stuttering}

-   With proprietary NVIDIA driver

[This](https://bugzilla.gnome.org/show_bug.cgi?id=781835) bug is much likely the cause of it. You should revert `383ba566bd7c2a76d0856015a66e47caedef06b6 ` commit in [mutter](https://archlinux.org/packages/?name=mutter). Use [ABS](../../en/Arch_build_system.html "ABS") for this and add `git revert -n 383ba566bd7c2a76d0856015a66e47caedef06b6` to the `prepare()` function in the [PKGBUILD](../../en/PKGBUILD.html "PKGBUILD") or simply install [mutter-performance](https://aur.archlinux.org/packages/mutter-performance/)^AUR^ instead.

-   With free drivers

If video playback stutters (a bit), try *GNOME on Xorg* instead of Wayland.

## GNOME Wayland session not available {#GNOME_Wayland_session_not_available}

GNOME Wayland does not support more than one GPU for output yet, [falling back](https://bugzilla.gnome.org/show_bug.cgi?id=771442) on GNOME X11.

If your displays are only connected to one of your video devices, add this to your [system environment variables](../../en/Environment_variables.html#Using_pam_env "Environment variables"):

    MUTTER_ALLOW_HYBRID_GPUS=1

See also [GDM#Wayland and the proprietary NVIDIA driver](../../en/GDM.html#Wayland_and_the_proprietary_NVIDIA_driver "GDM").

## gnome-control-center is empty and does not list any categories {#gnome-control-center_is_empty_and_does_not_list_any_categories}

Under alternative window managers (i3 for example), *gnome-control-center* starts as an empty window. You need to set the variable `XDG_CURRENT_DESKTOP` to `GNOME` to start it (either in a script or exporting the variable in `~/.profile`).

    export XDG_CURRENT_DESKTOP=GNOME
    gnome-control-center &

## GNOME freezes for a second after using a Function (Fn) key shortcut {#GNOME_freezes_for_a_second_after_using_a_Function_(Fn)_key_shortcut}

This is a problem with the brazilian portuguese ABNT 2 keyboard. If you have the brazilian portuguese enabled, GNOME might experience this problem. To fix this issue and keep using this keyboard layout, un-map the scroll lock button by commenting this line at `/usr/share/X11/xkb/symbols/br`:

    modifier_map Mod3   { Scroll_Lock };

And restart the session (log out and in).

## Zoom in/out keyboard shortcuts do not work on some applications {#Zoom_in/out_keyboard_shortcuts_do_not_work_on_some_applications}

`Ctrl+Plus` and `Ctrl+Minus` keyboard shortcuts for zoom in/out functions do not work out of the box on some GNOME applications, such as Files and GNOME Terminal.

In such cases, open up GNOME Tweaks ([gnome-tweaks](https://archlinux.org/packages/?name=gnome-tweaks)) and navigate to Keyboard & Mouse \> Additional Layout Options button \> Layout of numeric keypad. Change the `Disabled` value to `Hexadecimal`.

## Printers configuration does not work in GNOME settings {#Printers_configuration_does_not_work_in_GNOME_settings}

[CUPS](../../en/CUPS.html "CUPS") and [system-config-printer](https://archlinux.org/packages/?name=system-config-printer) should be installed

## Screen reader does not work {#Screen_reader_does_not_work}

Install [espeak-ng](https://archlinux.org/packages/?name=espeak-ng). Alternatively, [festival](https://archlinux.org/packages/?name=festival) can be used

## GNOME Software does not show Arch Linux packages {#GNOME_Software_does_not_show_Arch_Linux_packages}

[packagekit](https://archlinux.org/packages/?name=packagekit) integration is [voluntarily disabled](https://gitlab.archlinux.org/archlinux/packaging/packages/gnome-software/-/commit/df4431b3707e05832e49b9b9c3164ac53e0e3a6f) and [considered unsupported](https://github.com/archlinux/archinstall/issues/1321#issuecomment-1151343223); see also [archlinux/packaging/packages/gnome-software#4](https://gitlab.archlinux.org/archlinux/packaging/packages/gnome-software/-/issues/4).

## Right click does not work in touchpad {#Right_click_does_not_work_in_touchpad}

In touchpads where the buttons are divided (e.g. buttonless touchpads), tapping with one finger on the right side - or any other place - of the touchpad can give you the behavior of the left button, when right button is expected.

As of GNOME 3.28, the default behavior of touchpads is a two-finger tap emulate the mouse\'s right button. This behavior can be changed in GNOME Tweaks ([gnome-tweaks](https://archlinux.org/packages/?name=gnome-tweaks)) by going in *Keyboard & Mouse* in the left-side menu and then *Mouse Click Emulation* option.

The following values are available for click method:

Fingers
:   default value, two-fingers top to emulate right click button (default)

Area
:   tap button-right for the right click behavior and button-middle for middle click

Disabled
:   no mouse click emulation

Alternatively, this behavior can be changed in the command-line interface using *gsettings*. For instance, to set *areas* click method:

    $ gsettings set org.gnome.desktop.peripherals.touchpad click-method areas

## Device Security setting panel erratic behavior {#Device_Security_setting_panel_erratic_behavior}

See [GNOME#Device Security Settings](../../en/GNOME.html#Device_Security_Settings "GNOME").

## Cursor size or theme issues on Wayland {#Cursor_size_or_theme_issues_on_Wayland}

**This article or section is a candidate for merging with [Wayland#Qt](../../en/Wayland.html#Qt "Wayland").**

**Notes:** Looks like this issue is not specific to GNOME. (Discuss in [Talk:GNOME/Troubleshooting](../../en/Talk:GNOME/Troubleshooting.html))

The cursor settings might not be set for some [Qt](../../en/Qt.html "Qt") applications like Telegram[\[2\]](https://gitlab.gnome.org/GNOME/gnome-shell/-/issues/5894)[\[3\]](https://github.com/telegramdesktop/tdesktop/issues/25075#issuecomment-1250020362). This may result in cursors being of the wrong theme, size and not being able to resize the window.

Set the `XCURSOR_THEME` and `XCURSOR_SIZE` [environment variables](../../en/Environment_variables.html "Environment variables") manually (e.g., `XCURSOR_THEME=Adwaita`, `XCURSOR_PATH=/usr/share/icons` or `XCURSOR_SIZE=24`).

You can also use inline getting of current system\'s cursor size:

    $ XCURSOR_SIZE="$(gsettings get org.gnome.desktop.interface cursor-size)" _executable

If mentioned variables does not work on Wayland (for example in Telegram), try also adding `QT_QPA_PLATFORM=xcb`

## Force software rendering of GNOME {#Force_software_rendering_of_GNOME}

If you experience problems with your GPU driver, you can force software rendering of the GNOME session with the following [environment variables](../../en/Environment_variables.html "Environment variables"):

For Wayland session:

    MESA_LOADER_DRIVER_OVERRIDE=kms_swrast

For X11 session:

    LIBGL_ALWAYS_SOFTWARE=1
