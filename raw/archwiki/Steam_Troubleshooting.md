---
{"title": "Steam/Troubleshooting", "url": "https://wiki.archlinux.org/title/Steam/Troubleshooting", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Steam/Troubleshooting

1.  Make sure that you have followed [Steam#Installation](../../en/Steam.html#Installation "Steam").
2.  If the Steam client / a game is not starting and/or you have error message about a library, read [#Steam runtime](#Steam_runtime) and see [#Debugging shared libraries](#Debugging_shared_libraries).
3.  If the issue is related to networking, make sure that you have forwarded the [required ports for Steam](https://help.steampowered.com/en/faqs/view/2EA8-4D75-DA21-31EB).
4.  If the issue is about a game, consult [Steam/Game-specific troubleshooting](../../en/Steam/Game-specific_troubleshooting.html "Steam/Game-specific troubleshooting").

## Steam runtime {#Steam_runtime}

Steam for Linux ships with its own set of libraries called the [Steam runtime](https://github.com/ValveSoftware/steam-runtime). By default Steam launches all Steam Applications within the runtime environment. The Steam runtime is located at `~/.steam/root/ubuntu12_32/steam-runtime/`.

If you mix the Steam runtime libraries with system libraries you will run into binary incompatibility issues, see [steam-for-linux issue #4768](https://github.com/ValveSoftware/steam-for-linux/issues/4768). Binary incompatibility can lead to the Steam client and games not starting (manifesting as a crash, as hanging or silently returning), audio issues and various other problems.

The [steam](https://archlinux.org/packages/?name=steam) package offers two ways to launch Steam:

-   `/usr/bin/steam` (alias `steam`), which overrides runtime libraries known to cause problems via the `LD_PRELOAD` [environment variable](../../en/Environment_variable.html "Environment variable") (see [ld.so(8)](https://man.archlinux.org/man/ld.so.8)).
-   `/usr/lib/steam/steam`, the default Steam launch script

As the Steam runtime libraries are older they can lack newer features, e.g. the OpenAL version of the Steam runtime lacks [HRTF](../../en/Gaming.html#Binaural_audio_with_OpenAL "Gaming") and surround71 support.

### Steam native runtime {#Steam_native_runtime}

**Warning** Using the Steam native runtime is not recommended as it might break some games due to binary incompatibility and it might miss some libraries present in the Steam runtime.

The [steam-native-runtime](https://aur.archlinux.org/packages/steam-native-runtime/)^AUR^ package depends on over 130 packages to pose a native replacement of the Steam runtime, some games may however still require additional packages.

This package provides the `steam-native` script, which launches Steam with the `STEAM_RUNTIME=0` environment variable and `-compat-force-slr off` flag, making it ignore its runtime and only use system libraries.

**Note** This will only apply to games that use the Steam Linux Runtime 1 and Steam itself, if developers choose to use Steam Linux Runtime 3 or newer, take for example Barony, the only way to escape that will be to either launch the game not from Steam or modify the launch arguments to something like `./<game_executable>; exit; %command%`, which launches the game in system environment since runtimes are only applied for `%command%`.

You can also use the Steam native runtime without [steam-native-runtime](https://aur.archlinux.org/packages/steam-native-runtime/)^AUR^ by manually installing just the packages you need. See [#Finding missing runtime libraries](#Finding_missing_runtime_libraries).

## Debugging shared libraries {#Debugging_shared_libraries}

To see the shared libraries required by a program or a shared library run the `ldd` command on it, see [ldd(1)](https://man.archlinux.org/man/ldd.1). The `LD_LIBRARY_PATH` and `LD_PRELOAD` [environment variables](../../en/Environment_variables.html "Environment variables") can alter which shared libraries are loaded, see [ld.so(8)](https://man.archlinux.org/man/ld.so.8). To correctly debug a program or shared library it is therefore important that these environment variables in your debug environment match the environment you wish to debug.

If you figure out a missing library you can use [pacman](../../en/Pacman.html "Pacman") or [pkgfile](../../en/Pkgfile.html "Pkgfile") to search for packages that contain the missing library.

### Finding missing game libraries {#Finding_missing_game_libraries}

If a game fails to start, a possible reason is that it is missing required libraries. You can find out what libraries it requests by running `ldd `*`game_executable`*. *`game_executable`* is likely located somewhere in `~/.steam/root/steamapps/common/`. Please note that most of these \"missing\" libraries are actually already included with Steam, and do not need to be installed globally.

### Finding missing runtime libraries {#Finding_missing_runtime_libraries}

If individual games or Steam itself is failing to launch when using `steam-native` you are probably missing libraries. To find the required libraries run:

    $ cd ~/.steam/root/ubuntu12_32
    $ file * | grep ELF | cut -d: -f1 | LD_LIBRARY_PATH=. xargs ldd | grep 'not found' | sort | uniq

Alternatively, run Steam with `steam` and use the following command to see which non-system libraries Steam is using (not all of these are part of the Steam runtime):

    $ for i in $(pgrep steam); do sed '/\.local/!d;s/.*  //g' /proc/$i/maps; done | sort | uniq

## Debugging Steam {#Debugging_Steam}

**This article or section is out of date.**

**Reason:** Steam no longer redirects stdout and stderr to `/tmp/dumps/`*`USER`*`_stdout.txt` by default. See: [steam-for-linux issue 7114](https://github.com/ValveSoftware/steam-for-linux/issues/7114) A similar effect can be achieved by starting steam with `steam 2>&1 ` (Discuss in [Talk:Steam/Troubleshooting](../../en/Talk:Steam/Troubleshooting.html))

The Steam launcher redirects its stdout and stderr to `/tmp/dumps/`*`USER`*`_stdout.txt`. This means you do not have to run Steam from the command-line to see that output.

It is possible to debug Steam to gain more information which could be useful to find out why something does not work.

You can set `DEBUGGER` environment variable with one of `gdb`, `cgdb`, `valgrind`, `callgrind`, `strace` and then start `steam`.

For example with [gdb](https://archlinux.org/packages/?name=gdb)

    $ DEBUGGER=gdb steam

`gdb` will open, then type `run` which will start `steam` and once crash happens you can type `backtrace` to see call stack.

## Runtime issues {#Runtime_issues}

### \'GLBCXX_3.X.XX\' not found when using Bumblebee {#'GLBCXX_3.X.XX'_not_found_when_using_Bumblebee}

This error is likely caused because Steam packages its own out of date `libstdc++.so.6`. See [#Finding missing runtime libraries](#Finding_missing_runtime_libraries) about working around the bad library. See also [steam-for-linux issue 3773](https://github.com/ValveSoftware/steam-for-linux/issues/3773).

### Steam\>Warning: failed to init SDL thread priority manager: SDL not found {#Steam>Warning:_failed_to_init_SDL_thread_priority_manager:_SDL_not_found}

Solution: [install](../../en/Help:Reading.html#Installation_of_packages "Install") the [lib32-sdl2](https://aur.archlinux.org/packages/lib32-sdl2/)^AUR^ package.

### Game crashes immediately {#Game_crashes_immediately}

This is likely due to [#Steam runtime](#Steam_runtime) issues, see [#Debugging shared libraries](#Debugging_shared_libraries).

Disabling the in-game Steam Overlay in the game properties might help.

And finally, if those do not work, you should check Steam\'s output for any error from the game. You may encounter the following:

-   `munmap_chunk(): invalid pointer`
-   `free(): invalid pointer`

In these cases, try replacing the `libsteam_api.so` file from the problematic game with one of a game that works. This error usually happens for games that were not updated recently when Steam runtime is disabled. This error has been encountered with AYIM, Bastion and Monaco.

If the game crashes with

`terminate called after throwing an instance of 'dxvk::DxvkError'`

it\'s likely that conflicting versions of Vulkan are [installed](https://www.reddit.com/r/archlinux/comments/s1vjjg/comment/hsb10ac/?context=3). [lib32-vulkan-intel](https://archlinux.org/packages/?name=lib32-vulkan-intel) and NVIDIA Vulkan drivers are mutually exclusive. This is solved by uninstalling the unneeded driver. To obtain information about the chipset vendor one can run:

    # lshw -C display | grep vendor

To get a list of installed packages

    # pacman -Qs vulkan

### Game and Steam crashes after game start {#Game_and_Steam_crashes_after_game_start}

If the following error is output:

    failed to dlopen engine.so error=/home/GAMEPATH/bin/libgcc_s.so.1: version `GCC_7.0.0' not found (required by /usr/lib32/libopenal.so.1)

Moving the incompatible lib can be a workaround.

    $ mv .local/share/Steam/steamapps/common/GAME/bin/libgcc_s.so.1 .local/share/Steam/steamapps/common/GAME/bin/libgcc_s.so.1.b

### Some games freeze at start when in focus {#Some_games_freeze_at_start_when_in_focus}

A combination of using `ForceFullCompositionPipeline`, specific Proton versions and NVIDIA driver version 535 is known [to freeze some games](https://github.com/ValveSoftware/Proton/issues/6869) [using DXVK/Vulkan](https://github.com/doitsujin/dxvk/issues/3670) at launch under Xorg. Using Alt+Tab allows bringing Steam in focus, and the game seems to run properly in the background. Solution: disable `ForceFullCompositionPipeline` or downgrade NVIDIA drivers.

### Version \`CURL_OPENSSL_3\` not found {#Version_`CURL_OPENSSL_3`_not_found}

This is because [curl](https://archlinux.org/packages/?name=curl) alone is not compatible with previous versions. You need to install the compatibility libraries:

One of the following messages may show up:

    # Nuclear Throne
    ./nuclearthrone: /usr/lib32/libcurl.so.4: version `CURL_OPENSSL_3' not found (required by ./nuclearthrone)

    # Devil Daggers
    ./devildaggers: /usr/lib/libcurl.so.4: version `CURL_OPENSSL_3' not found (required by ./devildaggers)

You need to install either [libcurl-compat](https://archlinux.org/packages/?name=libcurl-compat) or [lib32-libcurl-compat](https://archlinux.org/packages/?name=lib32-libcurl-compat) and link the compatibility library manually:

    # Nuclear Throne
    $ ln -s /usr/lib32/libcurl-compat.so.4.4.0 "LIBRARY/steamapps/common/Nuclear Throne/lib/libcurl.so.4"

    # Devil Daggers
    $ ln -s /usr/lib/libcurl-compat.so.4.4.0 LIBRARY/steamapps/common/devildaggers/lib64/libcurl.so.4

### Steam webview/game browser not working in native runtime (Black screen) {#Steam_webview/game_browser_not_working_in_native_runtime_(Black_screen)}

**The factual accuracy of this article or section is disputed.**

**Reason:** Symlinking libs in `/usr` is horrible and not a solution. (Discuss in [Talk:Steam/Troubleshooting](../../en/Talk:Steam/Troubleshooting.html))

Since the new Steam Friends UI update, the client webview is not working correctly with the native-runtime.

    ./steamwebhelper: error while loading shared libraries: libpcre.so.3: cannot open shared object file: No such file or directory

It can be solved preloading glib libraries; Those do not require libpcre and selinux to work.

    $ LD_PRELOAD="/usr/lib/libgio-2.0.so.0 /usr/lib/libglib-2.0.so.0" steam-native

Alternatively, you may create a symbolic link to the native Arch libpcre library.

    # ln -s /usr/lib/libpcre.so /usr/lib64/libpcre.so.3

Since update from around 3/3/2022, there are some reports of black screen still persisting after applying above workaround.

The workaround for now is to run Steam with the `-no-cef-sandbox` option. More information can be found in Github Steam-For-Linux repository Issue [#8451](https://github.com/ValveSoftware/steam-for-linux/issues/8451) and [#8420](https://github.com/ValveSoftware/steam-for-linux/issues/8420).

### Steam: An X Error occurred {#Steam:_An_X_Error_occurred}

When using an NVIDIA GPU and proprietary drivers, Steam may fail to start and (if run from the terminal) produce errors of the form:

    Steam: An X Error occurred
    X Error of failed request:  GLXBadContext
    Major opcode of failed request:  151
    Serial number of failed request:  51
    xerror_handler: X failed, continuing

Ensure the *lib32-* [NVIDIA](../../en/NVIDIA.html "NVIDIA") driver for your card is installed, and matches the main package version with:

    # pacman -Qs nvidia

You may need to change which [mirrors](../../en/Mirrors.html "Mirrors") you are using to install the drivers if they do not match.

If you are using AMD, have enabled 10-bit color depth, and are having this problem. You will likely need to disable 10-bit color depth.

Another issue that causes this error message can be [solved by removing the config.vdf file](https://github.com/ValveSoftware/steam-for-linux/issues/4340#issuecomment-258593713):

    $ rm ~/.local/share/Steam/config/config.vdf

### Steam: Compatibility tool configuration failed {#Steam:_Compatibility_tool_configuration_failed}

If you are trying to run a native game using Proton but get a Steam compatibility tool error immediately after starting the game, you might have to reinstall the runtime.

1.  Navigate to your Steam library.
2.  In the dropdown above your game list check the *Tools* option to make them visible.
3.  Search for *Proton*, right click on each installed tool, visit *Properties*, open the *Local files* tab and click *Verify integrity of tool files* for each entry.
4.  Search for *Steam Linux Runtime* and repeat the same procedure. If none are available, install the latest *Steam Linux Runtime - Soldier*.

### Game starts but closes immediately with custom kernel {#Game_starts_but_closes_immediately_with_custom_kernel}

Make sure that you have enabled *User namespace* in *General setup -\> Namespaces support*.

### Steam Library won\'t start {#Steam_Library_won't_start}

Opening the Steam library either displays nothing, or a brief splash, but no window appears. Running `/usr/bin/steam` in a terminal window gives this error:

    Assertion 'device' failed at src/libsystemd/sd-device/device-private.c:103, function device_get_tags_generation(). Aborting.

Bugs reports are filed: [#79006](https://bugs.archlinux.org/task/79006)

See also discussion at: [Steam failing to launch since systemd 253.5-2 update](https://bbs.archlinux.org/viewtopic.php?id=287033)

A workaround is to install [lib32-libnm](https://archlinux.org/packages/?name=lib32-libnm).

### Periodic lag spikes with Proton Steam Play {#Periodic_lag_spikes_with_Proton_Steam_Play}

[Low framerate after around 30 minutes of playing](https://github.com/ValveSoftware/steam-for-linux/issues/11446) can be worked around by changing the game\'s launch options to `LD_PRELOAD="" %COMMAND%` to disable the Steam overlay.

## Graphical issues {#Graphical_issues}

### Black main screen on Intel iGPUs {#Black_main_screen_on_Intel_iGPUs}

On some systems that use Intel integrated graphics running Steam on [Wayland](../../en/Wayland.html "Wayland") will make only the webviews not render, with functional dropdowns and other menus. Going to *Steam -\> Settings -\> Interface*, then disabling *Enable GPU accelerated rendering in web views* might fix the problem.

### Blurry text and graphics with Xwayland and HiDPI {#Blurry_text_and_graphics_with_Xwayland_and_HiDPI}

When Steam runs as an [Xwayland](../../en/Wayland.html#Xwayland "Xwayland") client under a compositor that uses [HiDPI](../../en/HiDPI.html "HiDPI") scaling, you may find that Steam and games are rendered at half resolution and then upscaled to fit the HiDPI screen. This results in blurry graphics.

One option is to run Steam under a nested [gamescope](../../en/Gamescope.html "Gamescope") compositor. Install the [gamescope](https://archlinux.org/packages/?name=gamescope) package:

    $ gamescope -f -m 1 -e -- steam -gamepadui

This runs Steam in \"big picture\" mode (actually Steam Deck mode), in fullscreen, without scaling (i.e. at full resolution). The same settings should also propagate to games run under Steam.

Another option is to configure your compositor to prevent Xwayland from scaling applications entirely. For example, [Hyprland](../../en/Hyprland.html "Hyprland") users can add

    xwayland {
      force_zero_scaling = true
    }

to the hyprland.conf file to prevent Xwayland from scaling any applications. Note that **all** applications that use Xwayland will stop scaling, and so on HiDPI displays, text and other elements in those applications may become too small to be comfortably viewed.

Newer versions of Steam read their scale from the [Xorg](../../en/Xorg.html "Xorg") *Xft.dpi* resource directly rather than querying the compositor, so their UI will stay tiny even with *force_zero_scaling* enabled. To fix this, set *Xft.dpi* explicitly with [xorg-xrdb](https://archlinux.org/packages/?name=xorg-xrdb), for example to get 2x scaling:

    $ echo "Xft.dpi: 192" | xrdb -merge -

This should run before starting Steam (e.g. as part of hyprland\'s autostart) so it takes effect for the whole Xwayland session.

     Xft.dpi: 96 → scale 1.0 (default/unscaled)
     Xft.dpi: 144 → scale 1.5 (144/96)
     Xft.dpi: 192 → scale 2.0 (192/96)

### Steam flicker/blink with black screen not loading Store/Library or other pages {#Steam_flicker/blink_with_black_screen_not_loading_Store/Library_or_other_pages}

When Steam is started on Wayland (not confirmed X11) with dual graphics in some cases Steam client is unstable display black screen and flicker/blink. This is due to the option `PrefersNonDefaultGPU` being enabled in the [desktop entry](../../en/Desktop_entry.html "Desktop entry").

#### Fix by editing desktop entry {#Fix_by_editing_desktop_entry}

First, [make a user copy of the desktop entry](../../en/Desktop_entries.html#Modify_desktop_files "Desktop entries") for Steam (from `/usr/share/applications/steam.desktop`). Then, change the option:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.local/share/applications/steam.desktop
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
PrefersNonDefaultGPU=false
...
```

If opened, close Steam and relaunch.

**Tip** Some desktop environments provide a GUI for editing application options. For KDE Plasma: Right click on .desktop file \> Edit application\... \> select tab \"Application\" \> Advanced Options \> Uncheck option \"Run using dedicated graphics card\".

#### Bypass desktop entry {#Bypass_desktop_entry}

The desktop entry options do not take effect if you start Steam from the terminal, bypassing the issue.

    $ steam &

Ampersand (&) at the end is to run Steam in background, terminal can be closed after Steam starts.

## Audio issues {#Audio_issues}

If the sections below do not address the issue, using the [#Steam native runtime](#Steam_native_runtime) might help.

### Configure PulseAudio {#Configure_PulseAudio}

Games that explicitly depend on ALSA can break PulseAudio. Follow the directions for [PulseAudio#ALSA](../../en/PulseAudio.html#ALSA "PulseAudio") to make these games use PulseAudio instead.

If you are using [PipeWire](../../en/PipeWire.html "PipeWire"), then instead install [lib32-pipewire](https://archlinux.org/packages/?name=lib32-pipewire) and set up [PipeWire#PulseAudio clients](../../en/PipeWire.html#PulseAudio_clients "PipeWire").

### No audio or 756 Segmentation fault {#No_audio_or_756_Segmentation_fault}

**This article or section is out of date.**

**Reason:** This was fixed in 2016. Is this still relevant today? (Discuss in [Talk:Steam/Troubleshooting](../../en/Talk:Steam/Troubleshooting.html))

First [#Configure PulseAudio](#Configure_PulseAudio) and see if that resolves the issue. If you do not have audio in the videos which play within the Steam client, it is possible that the ALSA libraries packaged with Steam are not working.

Attempting to playback a video within the Steam client results in an error similar to:

    ALSA lib pcm_dmix.c:1018:(snd_pcm_dmix_open) unable to open slave

A workaround is to rename or delete the `alsa-lib` folder and the `libasound.so.*` files. They can be found at:

    ~/.steam/steam/ubuntu12_32/steam-runtime/i386/usr/lib/i386-linux-gnu/

An alternative workaround is to add the `libasound.so.*` library to the `LD_PRELOAD` environment variable:

    $ LD_PRELOAD='/usr/$LIB/libasound.so.2 '${LD_PRELOAD} steam

If audio still will not work, adding the PulseAudio libraries to the `LD_PRELOAD` variable may help:

    $ LD_PRELOAD='/usr/$LIB/libpulse.so.0 /usr/$LIB/libpulse-simple.so.0 '${LD_PRELOAD} steam

Be advised that their names may change over time. If so, it is necessary to take a look in

    ~/.steam/ubuntu12_32/steam-runtime/i386/usr/lib/i386-linux-gnu

and find the new libraries and their versions.

Bugs reports have been filed: [#3376](https://github.com/ValveSoftware/steam-for-linux/issues/3376) and [#3504](https://github.com/ValveSoftware/steam-for-linux/issues/3504)

### FMOD sound engine {#FMOD_sound_engine}

**The factual accuracy of this article or section is disputed.**

**Reason:** No source / bug report. (Discuss in [Talk:Steam/Troubleshooting](../../en/Talk:Steam/Troubleshooting.html))

The [FMOD](https://www.fmod.com/) audio middleware package is a bit buggy, and as a result games using it may have sound problems.

It usually occurs when an unused sound device is used as default for ALSA. See [Advanced Linux Sound Architecture#Set the default sound card](../../en/Advanced_Linux_Sound_Architecture.html#Set_the_default_sound_card "Advanced Linux Sound Architecture").

Affected games: Hotline Miami, Hotline Miami 2, Transistor

### PulseAudio & OpenAL: Audio streams cannot be moved between devices {#PulseAudio_&_OpenAL:_Audio_streams_cannot_be_moved_between_devices}

If you use [PulseAudio](../../en/PulseAudio.html "PulseAudio") and cannot move an audio stream between sinks, it might be because recent OpenAL versions default to disallow audio streams from being moved. Try to add the following to your `~/.alsoftrc`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.alsoftrc
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[pulse]
allow-moves=true
```

### Cracking Microphone in Steam Voice and Games {#Cracking_Microphone_in_Steam_Voice_and_Games}

If you experience cracking with your audio input while using Steam Voice or in games, you can try to launch Steam with the environment variable `PULSE_LATENCY_MSEC=30`

## Steam client issues {#Steam_client_issues}

### Cannot browse filesystem to add a library folder or library folder appears as empty {#Cannot_browse_filesystem_to_add_a_library_folder_or_library_folder_appears_as_empty}

If the file chooser is empty when trying add a library folder, or if a previously set up folder now appears with 0 games installed, this can be the result of an incorrect timestamp on the root directory or in the library folder. Timestamps can be checked with *stat*:

    $ stat path

If the timestamp is in the future, run

    $ touch path

to reinitialize it to the current date, then re-run Steam.

### Cannot add library folder because of missing execute permissions {#Cannot_add_library_folder_because_of_missing_execute_permissions}

If you add another Steam library folder on another drive, you might get the error message:

    New Steam library folder must be on a filesystem mounted with execute permissions

Make sure you are mounting the filesystem with the correct flags in your `/etc/fstab`, usually by adding `exec` to the list of mount parameter. The parameter must occur after any `user` or `users` parameter since these can imply `noexec`.

This error might also occur if your library folder does not contain a `steamapps` directory. Previous versions used `SteamApps` instead, so ensure the name is fully lowercase.

This error can also occur because of Steam runtime issues and may be fixed following the [#Finding missing runtime libraries](#Finding_missing_runtime_libraries) section or due to no space being left on the device. For debugging purposes it might be useful to run Steam from the console and observe the log.

### Unusually slow download speed {#Unusually_slow_download_speed}

If your Steam (games, software...) download speed through the client is unusually slow, but browsing the Steam store and streaming videos is unaffected, installing a DNS cache program, such as [dnsmasq](../../en/Dnsmasq.html "Dnsmasq") can help [\[1\]](https://steamcommunity.com/app/221410/discussions/2/616189106498372437/).

Something else that might help would be disabling [IPv6](../../en/IPv6.html "IPv6"). See [\[2\]](https://github.com/ValveSoftware/steam-for-linux/issues/6126) for more information.

Another potential fix is to disable HTTP2 [\[3\]](https://github.com/ValveSoftware/steam-for-linux/issues/10248) by creating the file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.steam/steam/steam_dev.cfg
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
@nClientDownloadEnableHTTP2PlatformLinux 0
```

To increase the server connections at the potential cost of negatively affecting speeds, add:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.steam/steam/steam_dev.cfg
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
@fDownloadRateImprovementToAddAnotherConnection 1.0
```

### \"Needs to be online\" error {#\"Needs_to_be_online\"_error}

**This article or section is out of date.**

**Reason:** *nscd* was removed in [glibc 2.38-4](https://gitlab.archlinux.org/archlinux/packaging/packages/glibc/-/commit/25032a8abb2760257c3dceb78e649a0a2c4e3ab2). (Discuss in [Talk:Steam/Troubleshooting](../../en/Talk:Steam/Troubleshooting.html))

**This article or section needs expansion.**

**Reason:** Unclear why enabling nscd can help (Discuss in [Talk:Steam/Troubleshooting#Needs to be online error: Enabling nscd.service](../../en/Talk:Steam/Troubleshooting.html#Needs_to_be_online_error:_Enabling_nscd.service "Talk:Steam/Troubleshooting"))

If the Steam launcher refuses to start and you get an error saying: \"*Fatal Error: Steam needs to be online to update*\" while you are online, then there might be issues with name resolving.

Try installing [lib32-systemd](https://archlinux.org/packages/?name=lib32-systemd), [lib32-libcurl-compat](https://archlinux.org/packages/?name=lib32-libcurl-compat), [nss-mdns](https://archlinux.org/packages/?name=nss-mdns), [lib32-nss](https://archlinux.org/packages/?name=lib32-nss), [lib32-glu](https://archlinux.org/packages/?name=lib32-glu) or [lib32-dbus](https://archlinux.org/packages/?name=lib32-dbus).

This may also be as simple as DNS resolution not correctly working and is not always obvious since modern browsers will use their own DNS servers. Follow [Domain name resolution](../../en/Domain_name_resolution.html "Domain name resolution").

Steam may have issues if *systemd-resolved* is providing DNS resolution. Make sure [lib32-systemd](https://archlinux.org/packages/?name=lib32-systemd) is present to resolve this.

If DNS resolution works but the Steam launcher still shows the same error message, [enabling](../../en/Help:Reading.html#Control_of_systemd_units "Enabling") DNS caching e.g. via the \"Name Service Caching Daemon\", `nscd.service`, has shown to work around this issue.

It is unclear what exactly running `nscd` does to make it work again though. Please check the [talk page](../../en/Talk:Steam/Troubleshooting.html#Needs_to_be_online_error:_Enabling_nscd.service "Talk:Steam/Troubleshooting") for more info.

### Steam forgets password {#Steam_forgets_password}

Related: [steam-for-linux#5030](https://github.com/ValveSoftware/steam-for-linux/issues/5030)

Steam for Linux has a bug which causes it to forget the password of some users.

As a workaround, after logging in to Steam, run

    # chattr +i ~/.steam/registry.vdf

This will set the file\'s immutable bit so Steam cannot modify, delete, or rename it and thus not log you out.

### Preventing crash memory dumps {#Preventing_crash_memory_dumps}

Every time Steam crashes, it writes a memory dump to `/tmp/dumps/`. If Steam falls into a crash loop, the dump files can become quite large. When `/tmp` is mounted as [tmpfs](../../en/Tmpfs.html "Tmpfs"), memory and swap file can be consumed needlessly.

To prevent this, link `/tmp/dumps/` to `/dev/null`:

    # ln -s /dev/null /tmp/dumps

Or alternatively, create and modify permissions on `/tmp/dumps`. Then Steam will be unable to write dump files to the directory.

    # mkdir /tmp/dumps
    # chmod 600 /tmp/dumps

This also has the added benefit of Steam not uploading these dumps to Valve\'s servers.

### Steam license problem with playing videos {#Steam_license_problem_with_playing_videos}

Steam uses [Google\'s Widevine DRM](https://en.wikipedia.org/wiki/Widevine "w:Widevine") for some videos. If it is not installed you will get the following error:

    This video requires a license to play which cannot be retrieved. This may be a temporary network condition. Please restart the video to try again.

To solve this issue follow the [*Streaming Videos on Steam* support page](https://help.steampowered.com/en/faqs/view/2FC3-54BF-465F-E556#15).

### No context menu for joining/inviting friends {#No_context_menu_for_joining/inviting_friends}

Since the new Steam Friends UI update, it may be the case that in the right-click menu the entries for \"Join Game\", \"Invite to Game\" and \"View Game Info\" are missing.

In order to fix this, it maybe be necessary to install [lsof](https://archlinux.org/packages/?name=lsof).

### Slow and unresponsive user interface {#Slow_and_unresponsive_user_interface}

If you experience extremely slow and sluggish performance when using the Steam client it might help to disable the *Enable GPU accelerated rendering in web views* option under the *Interface* tab in the Steam client settings.

The friends list can also cause this problem. Two workarounds are mentioned in [https://github.com/ValveSoftware/steam-for-linux/issues/7245](https://github.com/ValveSoftware/steam-for-linux/issues/7245):

-   Moving the friends list to another monitor [\[4\]](https://github.com/ValveSoftware/steam-for-linux/issues/7245#issuecomment-663629964).
-   Disabling animated avatars. Open Settings and navigate to Friends & Chat. Set *Enable Animated Avatars & Animated Avatar Frames in your Friends List and Chat \> OFF* [\[5\]](https://github.com/ValveSoftware/steam-for-linux/issues/7245#issuecomment-813443906).

### Steam fails to start correctly {#Steam_fails_to_start_correctly}

One troubleshooting step is to run

    $ steam --reset

This can fix various issues that come with a broken install.

### Missing taskbar menu {#Missing_taskbar_menu}

If clicking your Steam taskbar icon does not give you a menu, it may be necessary to install the [libappindicator-gtk2](https://aur.archlinux.org/packages/libappindicator-gtk2/)^AUR^ and [lib32-libappindicator-gtk2](https://aur.archlinux.org/packages/lib32-libappindicator-gtk2/)^AUR^ packages and restart Steam.

### \"Your browser does not support the minimum set of features required to watch this broadcast\" error {#\"Your_browser_does_not_support_the_minimum_set_of_features_required_to_watch_this_broadcast\"_error}

See [steam-for-linux issue 6780](https://github.com/ValveSoftware/steam-for-linux/issues/6780)

If you get an error stating \"*Your browser does not support the minimum set of features required to watch this broadcast*\" when attempting to watch a stream/broadcast try the following troubleshooting steps:

1.  Navigate to *Community \> Broadcasts*. If the page displays \"*Updating Steam*\" wait a few minutes to see if the process completes and cancel it after a while in case it does not. Now test if you are able to watch broadcasts, e.g. by clicking on one of the ones display under *Community \> Broadcasts*.
2.  Start a broadcast while in Big Picture mode (*View \> Big Picture Mode*). If a broadcast starts fine while in Big Picture mode check if it still works after switching back to the main interface.
3.  Trigger the Steam client to directly unlock H.264 decoding using the following command: `steam steam://unlockh264/`. The Steam client should start headless and run the unlock command. Wait a minute to be sure the process completes, then close and relaunch the Steam client.

### Using system titlebar and frame {#Using_system_titlebar_and_frame}

Currently Steam client tries to manage its windows itself, but it does it improperly, see [steam-for-linux#1040](https://github.com/ValveSoftware/steam-for-linux/issues/1040). As a workaround you can use [steamwm](https://github.com/dscharrer/steamwm) project. Run Steam like this: `./steamwm.cpp steam`. Also the project provides a skin that removes unnative control buttons and frame, but leaves default skin decorations.

### More selective DPMS inhibition {#More_selective_DPMS_inhibition}

By default, the Steam client totally disables screensaving when it is running, whether a game is launched or not.

A workaround to this issue is provided by [steam-screensaver-fix](https://aur.archlinux.org/packages/steam-screensaver-fix/)^AUR^: run `steam-screensaver-fix-native` or `steam-screensaver-fix-runtime`.

This will allow your screen to turn off if Steam is running, but will keep inhibiting the screensaver if a game is launched.

See [Issue 5607](https://github.com/ValveSoftware/steam-for-linux/issues/5607) at Valve\'s GitHub for the details.

### Enabling fractional scaling {#Enabling_fractional_scaling}

If the text and icons in the Steam client window are too small to read on your display, it may be beneficial to enable fractional scaling. The Steam client has a settings option to enable it, at *Settings \> Interface \> Scale text and icons to match monitor settings*. Enabling this should tell the client to use the system\'s fractional scaling settings.

However, if this does not automatically work, there is a command line parameter to force fractional scaling. Running Steam with the `-forcedesktopscaling 1.5` flag will scale the client to 1.5x size. This value can be changed to the correct scaling factor for your monitor. If you wish to make this change permanent, you can edit the `Exec` field in the `steam.desktop` file.

### Steam Beta crashes {#Steam_Beta_crashes}

If you are using Steam Beta (which can be confirmed with the presence of `You are in the 'publicbeta' client beta` in the logs) and encounter breaking bugs, manually switch back to non-Beta:

    $ rm -f ~/.local/share/Steam/package/beta

Report the issue after looking for duplicates at [https://github.com/ValveSoftware/steam-for-linux](https://github.com/ValveSoftware/steam-for-linux).

### Cannot access store page (client displays error -105 or -102) {#Cannot_access_store_page_(client_displays_error_-105_or_-102)}

If the store page is inaccessible but other networking features (such as game downloads) are working, it may be a DNS resolution failure. A possible solution is to ensure [systemd-resolved](../../en/Systemd-resolved.html "Systemd-resolved") is enabled and started, then create the `/etc/resolv.conf` symlink as explained in [systemd-resolved#DNS](../../en/Systemd-resolved.html#DNS "Systemd-resolved").

\
Other solution would be to flush DNS as explained here [\[6\]](https://askubuntu.com/a/929478):

Run `resolvectl flush-caches` or `systemd-resolve --flush-caches` as root.

### Steam client restarts while a game is running {#Steam_client_restarts_while_a_game_is_running}

A work around is to disable the *Enable GPU accelerated rendering in web views* option under the *Interface* tab in the Steam client settings.

## Steam Remote Play issues {#Steam_Remote_Play_issues}

See [Steam#Steam Remote Play](../../en/Steam.html#Steam_Remote_Play "Steam").

### Remote Play does not work from Arch Linux host to Arch Linux guest {#Remote_Play_does_not_work_from_Arch_Linux_host_to_Arch_Linux_guest}

Chances are you are missing [lib32-libcanberra](https://aur.archlinux.org/packages/lib32-libcanberra/)^AUR^. Once you [install](../../en/Help:Reading.html#Installation_of_packages "Install") that, it should work as expected.

With that, Steam should no longer crash when trying to launch a game through Remote Play.

### Hardware decoding not available {#Hardware_decoding_not_available}

Remote Play hardware decoding uses `vaapi`, but Steam requires `libva2_32bit`, where as Arch defaults to 64bit.

As a basic set, this is [libva](https://archlinux.org/packages/?name=libva) and [lib32-libva](https://archlinux.org/packages/?name=lib32-libva). Intel graphics users will also require both [libva-intel-driver](https://archlinux.org/packages/?name=libva-intel-driver) and [lib32-libva-intel-driver](https://archlinux.org/packages/?name=lib32-libva-intel-driver).

For more information about vaapi see [hardware video acceleration](../../en/Hardware_video_acceleration.html "Hardware video acceleration").

It may also be necessary to remove the Steam runtime version of libva, in order to force it to use system libraries. The current library in use can be found by using:

    $ pgrep steam | xargs -I {} cat /proc/{}/maps | grep libva

If this shows locations in `~/.local/Share/steam` Steam is still using its packaged version of libva. This can be rectified by deleting the libva library files at `~/.local/share/Steam/ubuntu12_32/steam-runtime/i386/usr/lib/i386-linux-gnu/libva*`, so that Steam falls back to the system libraries.

### Big Picture Mode minimizes itself after losing focus {#Big_Picture_Mode_minimizes_itself_after_losing_focus}

This can occur when you play a game via Remote Play or if you have a multi-monitor setup and move the mouse outside of BPM\'s window. To prevent this, set the `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0` environment variable and restart Steam.

See also the [steam-for-linux issue 4769](https://github.com/ValveSoftware/steam-for-linux/issues/4769).

## Other issues {#Other_issues}

### Steam Library in NTFS partition {#Steam_Library_in_NTFS_partition}

**Note** The kernel [NTFS](../../en/NTFS.html "NTFS") driver is vastly more performant than the [NTFS-3G](../../en/NTFS-3G.html "NTFS-3G") [FUSE](../../en/FUSE.html "FUSE") driver [\[7\]](https://openbenchmarking.org/result/2009092-NE-NTFSCOMPA56). So, for gaming scenario, it is better to uninstall [ntfs-3g](https://archlinux.org/packages/?name=ntfs-3g) package as GUI file managers driven by [udisks](../../en/Udisks.html "Udisks") prefer it when present.

If your Steam library resides in [NTFS](../../en/NTFS.html "NTFS") partition it is probable that games residing there could not start.

The trouble is that Wine uses a colon in its `$WINEPREFIX/dosdevices` directory, and when mounted with the `windows_names` option, is instructed to not create such colon names which can confuse Windows. Not adding it is not that unsafe: Windows will act fine besides being unable to open the symlink (which it will not need to do anyways); `chkdsk` may delete the link, but it is easily recreated.

Better workaround: mount without `windows_names`. This option is often added by GUI file explorers via [udisks](../../en/Udisks.html "Udisks") for caution, but adding a real [fstab](../../en/Fstab.html "Fstab") line will give it a proper way to do so.

1.  Run `genfstab -U /` and extract the line containing the ntfs partition, e.g.

        UUID=12345678ABCDEF00 /run/media/user/Gamez ntfs3 rw,uid=1000,gid=1000,windows_names 0 0

2.  Write the line into `/etc/fstab`, editing it to use the proper options without `windows_names`. With the earlier example, we would write

        UUID=12345678ABCDEF00 /run/media/user/Gamez ntfs3 rw,uid=1000,gid=1000 0 0

3.  Unmount the partition, then remount.

Alternatively, disable udisks use of `windows_names` globally following instructions in [udisks#NTFS file creation failing (filename-dependent)](../../en/Udisks.html#NTFS_file_creation_failing_(filename-dependent) "Udisks").

Other workaround: move the `steamapps/common/Proton `*`x`*`.`*`y`* and `steamapps/compatdata` to a non-NTFS drive, then create symbolic link in their original locations. You may be wasting some space on your otherwise important Linux drive, however.

    $ mv SteamLibrary/steamapps/common/Proton\ x.y /home/user/dir/
    $ mv SteamLibrary/steamapps/compatdata /home/user/dir/
    $ ln -s /home/user/dir/Proton\ x.y/ SteamLibrary/steamapps/common/Proton\ x.y
    $ ln -s /home/user/dir/compatdata/ SteamLibrary/steamapps/compatdata

You could also tell Proton to use a custom location for the prefix via the `STEAM_COMPAT_DATA_PATH` environment variable which you could set via the game launch options. Before you start the game make sure the directory exists.

### Wrong ELF class {#Wrong_ELF_class}

If you see this message in Steam\'s console output

    ERROR: ld.so: object '~/.local/share/Steam/ubuntu12_32/gameoverlayrenderer.so' from LD_PRELOAD cannot be preloaded (wrong ELF class: ELFCLASS32): ignored.

you can safely ignore it. It is not really any error: Steam includes both 64- and 32-bit versions of some libraries and only one version will load successfully. This \"error\" is displayed even when Steam (and the in-game overlay) is working perfectly.

### Multiple monitors setup {#Multiple_monitors_setup}

**This article or section needs expansion.**

**Reason:** Is this Nvidia-only? Can this be reproduced by anyone? Is there an upstream report? (Discuss in [Talk:Steam/Troubleshooting](../../en/Talk:Steam/Troubleshooting.html))

A setup with multiple monitors may prevent games from starting. Try to disable all additional displays, and then run a game. You can enable them after the game successfully started.

Also you can try running Steam with this environment variable set:

    $ export LD_LIBRARY_PATH=/usr/lib32/nvidia:/usr/lib/nvidia:$LD_LIBRARY_PATH

### Text is corrupt or missing {#Text_is_corrupt_or_missing}

Try installing [lib32-fontconfig](https://archlinux.org/packages/?name=lib32-fontconfig), [ttf-liberation](https://archlinux.org/packages/?name=ttf-liberation), [xorg-fonts-misc](https://archlinux.org/packages/?name=xorg-fonts-misc) (Steam updater window shows void squares instead of all non-Latin characters if this package not installed) and [wqy-zenhei](https://archlinux.org/packages/?name=wqy-zenhei) (for Asian characters), then restart Steam to see whether the problem is solved.

**Note**

-   Steam for Linux does not follow system-level font configurations.[\[8\]](https://github.com/ValveSoftware/steam-for-linux/issues/10422#issuecomment-1944396010) Thus, modify user-level configuration if you want change fontconfig for Steam.

-   When Steam cannot find the Arial font, font-config likes to fall back onto the Helvetica bitmap font. Steam does not render this and possibly other bitmap fonts correctly, so either removing problematic fonts or [disabling bitmap fonts](../../en/Font_configuration.html#Disable_bitmap_fonts "Font configuration") will most likely fix the issue without installing the Arial or ArialBold fonts. The font being used in place of Arial can be found with the command:

        $ fc-match -v Arial

### SetLocale(\'en_US.UTF-8\') fails at game startup or typing non-ASCII characters does not work in the Steam client {#SetLocale('en_US.UTF-8')_fails_at_game_startup_or_typing_non-ASCII_characters_does_not_work_in_the_Steam_client}

You need to generate the `en_US.UTF-8 UTF-8` locale. See [Locale#Generating locales](../../en/Locale.html#Generating_locales "Locale").

### Missing libc {#Missing_libc}

**The factual accuracy of this article or section is disputed.**

**Reason:** Issue #3730 is closed. Is `$HOME` ending in a slash still relevant? (Discuss in [Talk:Steam/Troubleshooting](../../en/Talk:Steam/Troubleshooting.html))

This could be due to a corrupt Steam executable. Check the output of:

    $ ldd ~/.local/share/Steam/ubuntu12_32/steam

Should `ldd` claim that it is not a dynamic executable, then Steam likely corrupted the binary during an update. The following should fix the issue:

    $ cd ~/.local/share/Steam/
    $ ./steam.sh --reset

If it does not, try to delete the `~/.local/share/Steam/` directory and launch Steam again, telling it to reinstall itself.

This error message can also occur due to a bug in Steam which occurs when your `$HOME` directory ends in a slash (Valve GitHub [issue 3730](https://github.com/ValveSoftware/steam-for-linux/issues/3730)). This can be fixed by editing `/etc/passwd` and changing `/home/`*`username`*`/` to `/home/`*`username`*, then logging out and in again. Afterwards, Steam should repair itself automatically.

### Games do not launch on older Intel hardware {#Games_do_not_launch_on_older_Intel_hardware}

[source](https://steamcommunity.com/app/8930/discussions/1/540744299927655197/)

On older Intel hardware which does not support OpenGL 3, such as Intel GMA chips or Westmere CPUs, games may immediately crash when run. It appears as a `gameoverlayrenderer.so` error in `/tmp/dumps/mobile_stdout.txt`, but looking in `/tmp/gameoverlayrenderer.log` it shows a GLXBadFBConfig error.

This can be fixed, by forcing the game to use a later version of OpenGL than it wants. Add `MESA_GL_VERSION_OVERRIDE=3.1 MESA_GLSL_VERSION_OVERRIDE=140` to your [launch options](../../en/Launch_option.html "Launch option").

### Mesa: Game does not launch, complaining about OpenGL version supported by the card {#Mesa:_Game_does_not_launch,_complaining_about_OpenGL_version_supported_by_the_card}

Some games are badly programmed, to use any OpenGL version above 3.0. With Mesa, an application has to request a specific core profile. If it does not make such a request, only OpenGL 3.0 and lower are available.

This can be fixed, by forcing the game to use a version of OpenGL it actually needs. Add `MESA_GL_VERSION_OVERRIDE=4.1 MESA_GLSL_VERSION_OVERRIDE=410` to your [launch options](../../en/Launch_option.html "Launch option").

### 2K games do not run on XFS partitions {#2K_games_do_not_run_on_XFS_partitions}

**This article or section needs expansion.**

**Reason:** Seems to be a general issue, e.g. [\[9\]](https://github.com/ValveSoftware/Source-1-Games/issues/1685) (Discuss in [Talk:Steam/Troubleshooting](../../en/Talk:Steam/Troubleshooting.html))

If you are running 2K games such as Civilization 5 on [XFS](../../en/XFS.html "XFS") partitions, then the game may not start or run properly due to how the game loads files as it starts. [\[10\]](https://bbs.archlinux.org/viewtopic.php?id=185222)

### Steam controller not being detected correctly {#Steam_controller_not_being_detected_correctly}

See [Gamepad#Steam Controller](../../en/Gamepad.html#Steam_Controller "Gamepad").

### Steam controller makes a game crash {#Steam_controller_makes_a_game_crash}

See [Gamepad#Steam Controller makes a game crash or not recognized](../../en/Gamepad.html#Steam_Controller_makes_a_game_crash_or_not_recognized "Gamepad").

### Steam hangs on \"Installing breakpad exception handler\...\" {#Steam_hangs_on_\"Installing_breakpad_exception_handler...\"}

[BBS#177245](https://bbs.archlinux.org/viewtopic.php?id=177245)

You have an NVIDIA GPU and Steam has the following output:

    Running Steam on arch rolling 64-bit
    STEAM_RUNTIME is enabled automatically
    Installing breakpad exception handler for appid(steam)/version(0_client)

Then nothing else happens. Ensure you have the correct drivers installed as well as their 32-bit versions (the 64-bit and 32-bit variants have to have the same versions): see [NVIDIA#Installation](../../en/NVIDIA.html#Installation "NVIDIA").

### Killing standalone compositors when launching games {#Killing_standalone_compositors_when_launching_games}

Utilizing the `%command%` switch, you can kill standalone compositors (such as [Xcompmgr](../../en/Xcompmgr.html "Xcompmgr") or [picom](../../en/Picom.html "Picom")) - which can cause lag and tearing in some games on some systems - and relaunch them after the game ends by adding the following to your game\'s launch options.

    killall compositor && %command%; nohup compositor &

You can also add -options to `%command%` or *`compositor`*, of course.

Steam will latch on to any processes launched after `%command%` and your Steam status will show as in game. So in this example, we run the compositor through `nohup` so it is not attached to Steam (it will keep running if you close Steam) and follow it with an ampersand so that the line of commands ends, clearing your Steam status.

If your compositor supports running in daemon mode, you can use it instead. For example, [picom(1)](https://man.archlinux.org/man/picom.1) has the `--daemon` / `-b` option to daemonize its process:

    killall picom && %command%; picom -b

### Symbol lookup error using DRI3 {#Symbol_lookup_error_using_DRI3}

Steam outputs this error and exits.

    symbol lookup error: /usr/lib/libxcb-dri3.so.0: undefined symbol: xcb_send_request_with_fds

To work around this, run Steam with `LIBGL_DRI3_DISABLE=1`, disabling DRI3 for Steam.

### Launching games on NVIDIA Optimus laptops {#Launching_games_on_NVIDIA_Optimus_laptops}

**This article or section is out of date.**

**Reason:** Was for using bumblebee : what is the equivalent for recommended setup now, using prime-run instead does not work (Discuss in [Talk:Steam/Troubleshooting](../../en/Talk:Steam/Troubleshooting.html))

To be able to play games which require using NVIDIA GPU (for example, Hitman 2016) on Optimus enabled laptop, you should start game with *primusrun* prefix in launch options. Otherwise, game will not work.

Right click the game in your Steam library and select *Properties \> GENERAL \> LAUNCH OPTIONS*. Change options to

    primusrun %command%

Running Steam with *primusrun* used to work. While Steam has changed some behavior that now running Steam with *primusrun* would not have effect on launching games. As a result, you need to set launch options for each game (and you do NOT have to run Steam with *primusrun*).

For *primusrun*, VSYNC is enabled by default it could result in a mouse input delay lag, slightly decrease performance and in-game FPS might be locked to a refresh rate of a monitor/display. In order to disable VSYNC for primusrun default value of option `vblank_mode` needs to be overridden by environment variable.

    vblank_mode=0 primusrun %command%

Same with optirun that uses primus as a bridge.

    vblank_mode=0 optirun -b primus %command%

If that did not work try:

    LD_PRELOAD="libpthread.so.0 libGL.so.1" __GL_THREADED_OPTIMIZATIONS=1 optirun %command%

For more details see [Bumblebee#Primusrun mouse delay (disable VSYNC)](../../en/Bumblebee.html#Primusrun_mouse_delay_(disable_VSYNC) "Bumblebee").

### HiDPI {#HiDPI}

[HiDPI](../../en/HiDPI.html "HiDPI") support should work out of the box, although on some systems it is necessary to [force it](../../en/HiDPI.html#Steam "HiDPI") setting the `-forcedesktopscaling `*`factor`* cli option or the `STEAM_FORCE_DESKTOPUI_SCALING` environment variable to set the desired scale factor.

### Protocol support under KDE Plasma {#Protocol_support_under_KDE_Plasma}

If you are getting an error after running a game through web browser *(or executing the link through xdg-open)*

    Error — KIOExec
    File not found: steam://run/440

Go to *System Settings -\> Applications -\> File Associations*, add new, select `inode` group and name it `vnd.kde.service.steam`, then under *Application Preference Order* you have to add Steam. Apply changes, It should be working now.

### The game crashes when using Steam Linux Runtime - Soldier {#The_game_crashes_when_using_Steam_Linux_Runtime_-_Soldier}

**This article or section is out of date.**

**Reason:** Was a fix 2021-03 : is this still relevant today? (Discuss in [Talk:Steam/Troubleshooting](../../en/Talk:Steam/Troubleshooting.html))

Since Proton 5.13 Steam uses the Steam Linux Runtime - Soldier by default. Some games crash when using it.

To bypass it, you can:

-   Manually [build](https://github.com/ValveSoftware/Proton#alternative-building-without-the-steam-runtime) a proton without the Steam Runtime
-   Replace the Soldier entry point script:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.steam/steam/steamapps/common/SteamLinuxRuntime_soldier/_v2-entry-point
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/bash

shift 2
exec "${@}"
```

### Games running with Proton 5.13+ have no Internet connectivity {#Games_running_with_Proton_5.13+_have_no_Internet_connectivity}

If you are using [systemd-resolved](../../en/Systemd-resolved.html "Systemd-resolved") as your DNS resolver, ensure you have created the `resolv.conf` symlink as described in [systemd-resolved#DNS](../../en/Systemd-resolved.html#DNS "Systemd-resolved").

The file should contain something similar to:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/resolv.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# This is /run/systemd/resolve/stub-resolv.conf managed by man:systemd-resolved(8).
# Do not edit.
```

### \"could not determine 32/64 bit of java\" {#\"could_not_determine_32/64_bit_of_java\"}

A forgotten install of the [linux-steam-integration](https://aur.archlinux.org/packages/linux-steam-integration/)^AUR^ package caused this with at least one game. Early on there were conflicts between the system and the Steam runtime versions of some libraries, and that package helped resolve some of them. It is unclear whether it is still helpful, but uninstalling it resolved the above error message for Project Zomboid. The solution was discovered by noticing that running the `projectzomboid.sh` command from the command line worked, but switching the launch options to `sh -xc 'echo %command%; declare -p'` showed Steam was trying to run the exact same command, but there were a lot of `lsi-`-prefixed libraries inserted in the preload and path.

### Stuttering with Vulkan {#Stuttering_with_Vulkan}

If you notice a constant intense stutter every 1-2 seconds, there may be conflicts in your vsync settings. Manually configuring vsync in the parameters will possibly fix it.

Go to the game properties and configure it in Launch Options:

    DXVK_FRAME_RATE=60 %command%

### Force OpenGL emulation {#Force_OpenGL_emulation}

Some, especially older games might not work with the default Vulkan ([DXVK](../../en/Wine.html#DXVK "DXVK")) wrapper Proton uses. Try running the application with WineD3D OpenGL wrapper instead:

    PROTON_USE_WINED3D=1 %command%

### File picker does not see anything but Steam library {#File_picker_does_not_see_anything_but_Steam_library}

See [FS#78625](https://bugs.archlinux.org/task/78625). You need to install [xdg-desktop-portal](https://archlinux.org/packages/?name=xdg-desktop-portal).

### DirectX errors on hybrid graphics {#DirectX_errors_on_hybrid_graphics}

For laptop with Intel/NVIDIA [Hybrid graphics](../../en/Hybrid_graphics.html "Hybrid graphics") encountering the following error:

    A d3d11-compatible gpu (feature level 11.0, shader model 5.0) is required to run the engine.

It\'s probably because your game is running on the iGPU instead of the dedicated GPU and you need to configure [PRIME](../../en/PRIME.html "PRIME"). If it\'s still not doing it, try using [Direct3D instead of DXVK](#Force_OpenGL_emulation).

### No Internet Connection when downloading {#No_Internet_Connection_when_downloading}

If you see *No Internet Connection* while downloading games, a possible solution is clearing the download cache (*Steam \> Settings \> Downloads \> Clear Download Cache*).

### Poor performance or stuttering after launching Steam {#Poor_performance_or_stuttering_after_launching_Steam}

If you experience reduced performance or stuttering, lasting anywhere from a few seconds to a couple of minutes after launching Steam, it may be cased by bugged or outdated Proton installations.

Remove bugged Proton installed under app ID 0: `~/.steam/root/steamapps/compatdata/0`. You may also need to remove outdated and problematic Proton versions, including custom ones like GE-Proton, especially `5.21-GE-1`.

For more details, see [steam-for-linux#8114](https://github.com/ValveSoftware/steam-for-linux/issues/8114).

### Very long startup and slow user interface response {#Very_long_startup_and_slow_user_interface_response}

Steam\'s use of `steamloopback.host` in its Chromium backend to refer to itself. Due to the way *systemd-resolvd* attempts to resolve this host (via `mdns` by default for some users) this issue can hang the interface. This causes very long startups (if it ever starts) and a slow-responding (or not at all) user interface. This issue can temporary be addressed by editing `/etc/nsswitch.conf` to change `mdns` to `mdns_minimal` and restarting systemd-resolvd. For more details, see [\[11\]](https://github.com/ValveSoftware/steam-for-linux/issues/10879).

## See also {#See_also}

-   [Multimedia and Games / Arch Linux Forums](https://bbs.archlinux.org/viewforum.php?id=32)
-   [ValveSoftware/steam-for-linux](https://github.com/ValveSoftware/steam-for-linux) -- Issue tracking for the Steam for Linux client
-   [Steam Community discussions of the game](https://steamcommunity.com/)
-   [Steam Support FAQ](https://help.steampowered.com/en/)
