---
{"title": "Steam/Game-specific troubleshooting", "url": "https://wiki.archlinux.org/title/Steam/Game-specific_troubleshooting", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Steam/Game-specific troubleshooting

See [Steam/Troubleshooting](../../en/Steam/Troubleshooting.html "Steam/Troubleshooting") first.

This page assumes familiarity with the [Steam#Directory structure](../../en/Steam.html#Directory_structure "Steam"), [Steam#Launch options](../../en/Steam.html#Launch_options "Steam"), [environment variables](../../en/Environment_variables.html "Environment variables"), the [Steam runtime](../../en/Steam_runtime.html "Steam runtime") and [shared libraries](../../en/Steam/Troubleshooting.html#Debugging_shared_libraries "Steam/Troubleshooting"). The *`GAME`* pseudo-variable is used to refer to a game\'s directory. When the text reads \"*run the game with `FOO=bar`*\" it is implied that you either update your launch options or run the game from the command-line with the environment variable.

## Contributing {#Contributing}

-   Use \"game directory\" or the *`GAME`* pseudo-variable to refer to a game\'s directory.
-   Link bug reports and sources of workarounds.

## Other sources {#Other_sources}

The following links offer even more fixes and tweaks for various games which would otherwise exceed this article\'s purpose:

-   [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Home)

For games running with Proton, you can check ProtonDB which lists a lot of useful user reports for specific games. You can filter searched reports by Linux distribution and by hardware. Users also describe if they had to apply tweaks.

-   [ProtonDB](https://www.protondb.com/) crowdsourced Linux compatibility reports.

## Common steps {#Common_steps}

### OpenSSL 1.0 setup {#OpenSSL_1.0_setup}

**This article or section is out of date.**

**Reason:** The linked bug report is from 2017, are there still games affected? (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

Some Steam games are built against OpenSSL 1.0. ([FS#53618](https://bugs.archlinux.org/task/53618))

Install [lib32-openssl-1.0](https://aur.archlinux.org/packages/lib32-openssl-1.0/)^AUR^ and run the game with `LD_LIBRARY_PATH=/usr/lib/openssl-1.0`.

### Missing libcurl.so.4 or version CURL_OPENSSL_3 not found {#Missing_libcurl.so.4_or_version_CURL_OPENSSL_3_not_found}

[Install](../../en/Help:Reading.html#Installation_of_packages "Install") [lib32-libcurl-compat](https://archlinux.org/packages/?name=lib32-libcurl-compat) and run the game with `LD_PRELOAD=libcurl.so.3`.

### Steam Link {#Steam_Link}

Currently Steam Link does not work with Wayland. You will only see a blank screen or even flickering when connecting to a Steam host running on Wayland. So you have to disable Wayland, for example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/gdm/custom.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
WaylandEnable=false
```

And restart the login manager before continuing.

### Squares or invisible symbols, special characters and cyrillic letters in Source-based games {#Squares_or_invisible_symbols,_special_characters_and_cyrillic_letters_in_Source-based_games}

Any special character may produce a square or an empty space mark in the game, main menu and game console. In practice, any characters other than latin ones are not working. The problem is that `Bitstream Vera Sans` is configured as the system primary default font for latin sans-serif fonts.

First, make sure that per-user font customization files are enabled, i.e. the following file exist:

    /etc/fonts/conf.d/50-user.conf

Next, create `fonts.conf` file in your fontconfig directory with the following content or if the file already exist, append only the alias section to the file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.config/fontconfig/fonts.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
 <alias>
  <family>sans-serif</family>
   <prefer>
    <family>DejaVu Sans</family>
    <family>Verdana</family>
    <family>Arial</family>
    <family>Albany AMT</family>
    <family>Luxi Sans</family>
    <family>Nimbus Sans L</family>
    <family>Nimbus Sans</family>
    <family>Helvetica</family>
    <family>Lucida Sans Unicode</family>
    <family>BPG Glaho International</family> 
    <family>Tahoma</family> 
   </prefer>
 </alias>
</fontconfig>
```

### PipeWire & FMOD {#PipeWire_&_FMOD}

If you are using PipeWire and do not have any sound in games utilising FMOD as an audio backend then you may require [pipewire-alsa](https://archlinux.org/packages/?name=pipewire-alsa). Such games include Project Zomboid, Don\'t Starve, and Unrailed.

You will see similar to the following in your logs if this affects you.

    [00:00:01]: FMOD Error: An invalid object handle was used.
    [00:00:10]: FMOD Error: Can't play event dontstarve/HUD/click_mouseover: An invalid object handle was used.

### tcmalloc.cc error in Source 1 games {#tcmalloc.cc_error_in_Source_1_games}

If games such as like Counter-Strike Source, Portal, Team Fortress 2 crash at startup with the following error:

    src/tcmalloc.cc:278] Attempt to free invalid pointer 0x9e13ad0
    ~/.local/share/Steam/steamapps/common/Team Fortress 2/hl2.sh: line 72:  6280 Aborted                 (core dumped) ${GAME_DEBUGGER} "${GAMEROOT}"/${GAMEEXE} "$@"

Install [lib32-gperftools](https://aur.archlinux.org/packages/lib32-gperftools/)^AUR^, and point the crashing game to the proper library using:

    LD_PRELOAD=/usr/lib32/libtcmalloc_minimal.so

From this [steam community post](https://steamcommunity.com/app/440/discussions/0/3815166265396512006/).

### Crash with Unity games {#Crash_with_Unity_games}

Games using Unity, e.g. Papers Please, Vampire Survivors, expect [PulseAudio](../../en/PulseAudio.html "PulseAudio") to be installed and will quietly crash with SIGSEGV on running if it is not installed. You can also use [PipeWire](../../en/PipeWire.html "PipeWire") with [pipewire-pulse](https://archlinux.org/packages/?name=pipewire-pulse).

### Split lock detection / mitigation {#Split_lock_detection_/_mitigation}

Split lock detection is a warning to aid developers, mitigation on the other hand is designed to hinder performance in order to encourage developers to write better code. This results in significantly reduced performance under a myriad of gaming scenarios[\[1\]](https://www.phoronix.com/news/Linux-Splitlock-Hurts-Gaming), including Counter-Strike Source engine games and games using BattleEye anti-cheat.

Since kernel 6.2, a new sysctl tunable[\[2\]](https://lore.kernel.org/lkml/20221212191524.553244-1-dave.hansen@linux.intel.com/) of `split_lock_mitigate = 1` is available (by default) to enable mitigation, instead of the older[\[3\]](https://www.phoronix.com/news/Linux-5.19-Split-Lock)`split_lock_detect=on` [kernel parameter](../../en/Kernel_parameter.html "Kernel parameter").

Upon setting:

    # echo "kernel.split_lock_mitigate = 0" > /etc/sysctl.d/99-splitlock.conf

The kernel will log Steam / Cef lock splitting, but without the sequential access penalty.

**Note** Disabling split lock mitigation may have negative impact on overall system performance. It is therefore suggested to use `sysctl` to toggle the flag only when necessary.

Additionally, [GameMode](../../en/GameMode.html "GameMode") can be used to toggle this kernel parameter at runtime.

## Games {#Games}

### 7 Days To Die {#7_Days_To_Die}

If the game crashes on start, add the following to Steam launch options:

    LD_PRELOAD="libpthread.so.0 libGL.so.1" __GL_THREADED_OPTIMIZATIONS=1 %command% -force-glcore

If the game does not recognize your screen\'s resolution, launch the game with **Game Launcher** and check the **Unity screen selector** option to correct the resolution. This will give you a GUI in which you can select the correct screen when the game is started.

**Note** The game tends to crash or disfunction in windowed mode. It may be advisable to run it in full screen mode.

If that does not help try running the game in **32-bit** mode by checking the respective option in the Game-engine in the launcher options.

It will help the game performance if the **GLCore** option is checked in launcher options.

**Note** The game does accept `.dll` mods if installing mods. However, this requires an override for your Proton prefix. Use Protontricks to access `winecfg` for the prefix 7 Days is using, go to libraries, and add *winhttp* as an override. This at least works for Harmony DLL mods.

### Age of Wonders 3 {#Age_of_Wonders_3}

If game fails to start at launch you will need to create a pthread_yield.so file. Do the following in a text editor:

    extern int sched_yield(void);

    int pthread_yield()
    {
        return sched_yield();
    }

Then save file as a pthread_yield.c then issue following command in terminal in the directory that has the file:

    $ gcc -m32 -shared -fPIC pthread_yield.c -o pthread_yield.so

Copy pthread_yield.so in the AOW3 game directory and then edit the AoW3Launcher.sh file and add the following:

    export LD_PRELOAD="pthread_yield.so"

Do this at the bottom of the file but before exec ./AoW3Launcher after this the game should then launch as normal.

### Alien Isolation {#Alien_Isolation}

#### Missing libpcre.so.3 and libidn.so.11 {#Missing_libpcre.so.3_and_libidn.so.11}

    $ ln -s /usr/lib/libpcre.so 'GAME/lib/x86_64/libpcre.so.3'
    $ ln -s /usr/lib/libidn.so 'GAME/lib/x86_64/libidn.so.11'

Append `./lib/x86_64` to your `LD_LIBRARY_PATH`.[\[4\]](https://steamcommunity.com/app/214490/discussions/0/154644705028020291/)

#### Missing libcrypt.so.1 {#Missing_libcrypt.so.1}

Install the package [libxcrypt-compat](https://archlinux.org/packages/?name=libxcrypt-compat). [\[5\]](https://github.com/FeralInteractive/ferallinuxscripts/issues/3)

### Amnesia: The Dark Descent {#Amnesia:_The_Dark_Descent}

Dependencies: [\[6\]](https://steamcommunity.com/app/221410/discussions/0/864957183198111387/)

-   [lib32-freealut](https://aur.archlinux.org/packages/lib32-freealut/)^AUR^
-   [lib32-glu](https://archlinux.org/packages/?name=lib32-glu)
-   [lib32-libxmu](https://archlinux.org/packages/?name=lib32-libxmu)
-   [lib32-sdl_ttf](https://aur.archlinux.org/packages/lib32-sdl_ttf/)^AUR^

#### Gamepad not working {#Gamepad_not_working}

The version of libSDL2 shipped with the game seems to be out-of-date and may not support your gamepad yet. Simply remove or rename `<install_dir>/game/lib64/libSDL2-2.0.so.0`, the linker will fall back to using the up-to-date version from `/usr/lib`.

### Amnesia: Rebirth {#Amnesia:_Rebirth}

**The factual accuracy of this article or section is disputed.**

**Reason:** There should be no reason for rebooting, but some services might have to be (re)started. (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

If you encounter a popup with `Fatal Error: Fmod could not be initialized!!` on startup which immediately closes the game and you are using [PipeWire](../../en/PipeWire.html "PipeWire"), [install](../../en/Help:Reading.html#Installation_of_packages "Install") these packages if they are not already: [pulseaudio-alsa](https://archlinux.org/packages/?name=pulseaudio-alsa), [lib32-libpulse](https://archlinux.org/packages/?name=lib32-libpulse) and [lib32-alsa-plugins](https://archlinux.org/packages/?name=lib32-alsa-plugins). Reboot and re-open the game.

### And Yet It Moves {#And_Yet_It_Moves}

Dependencies:

-   [lib32-libjpeg6-turbo](https://aur.archlinux.org/packages/lib32-libjpeg6-turbo/)^AUR^
-   [lib32-libpng12](https://aur.archlinux.org/packages/lib32-libpng12/)^AUR^
-   [lib32-libtheora](https://aur.archlinux.org/packages/lib32-libtheora/)^AUR^
-   [lib32-libtiff4](https://aur.archlinux.org/packages/lib32-libtiff4/)^AUR^

#### Game does not start {#Game_does_not_start}

When the game refuses to launch and prints one of the following error messages:

    readlink: extra operand ‘Yet’
    Try 'readlink --help' for more information.

    This script must be run as a user with write priviledges to game directory.

Open *`GAME`*`/AndYetItMovesSteam.sh` and surround `${BASH_SOURCE[0]} ` in the following line with double quotes.

    ayim_dir="$(dirname "$(readlink -f ${BASH_SOURCE[0]})")"

### Anomaly Warzone Earth {#Anomaly_Warzone_Earth}

#### Leave fullscreen {#Leave_fullscreen}

There are no in-game settings for this, but fullscreen can be toggled with `Alt+Enter`

#### Infinite loading {#Infinite_loading}

Create file `loadfix.c` next to the game executable: [src](https://steamcommunity.com/app/282070/discussions/0/610573751159186268/?ctp=4#c530647080133257413)

    #define _GNU_SOURCE
    #include <dlfcn.h>
    #include <semaphore.h>
    #include <stdio.h>
    #include <time.h>
    #include <unistd.h>
    static int (*_realSemTimedWait)(sem_t *, const struct timespec *) = NULL;

    int sem_timedwait(sem_t *sem, const struct timespec *abs_timeout)
    {
        if (abs_timeout->tv_nsec >= 1000000000)
        {
            //fprintf(stderr, "to: %lu:%lu\n", abs_timeout->tv_sec, abs_timeout->tv_nsec);
            ((struct timespec *)abs_timeout)->tv_nsec -= 1000000000;
            ((struct timespec *)abs_timeout)->tv_sec++;
        }
        return _realSemTimedWait(sem, abs_timeout);
    }

    __attribute__((constructor)) void init(void)
    {
        _realSemTimedWait = dlsym(RTLD_NEXT, "sem_timedwait");
    }

Compile with `gcc -m32 -o loadfix.so loadfix.c -ldl -shared -fPIC -Wall -Wextra`

Launch with `LD_PRELOAD=$LD_PRELOAD:./loadfix.so %command%`

#### Gamepad not working {#Gamepad_not_working_2}

You have to enable keyboard control and map gamepad to keys.

Config for Steam: `steam://controllerconfig/91200/1498735506`

### Aquaria {#Aquaria}

#### Mouse pointer gets stuck in one direction {#Mouse_pointer_gets_stuck_in_one_direction}

If the mouse pointer gets stuck in one direction, make sure *`GAME`*`/usersettings.xml` contains `<JoystickEnabled on="0" />`.

If that does not fix the issue, try unplugging any joysticks or joystick adapter devices you have plugged in.

### ARK: Survival Evolved {#ARK:_Survival_Evolved}

#### Game does not start, displays text window with unreadable text {#Game_does_not_start,_displays_text_window_with_unreadable_text}

Run the game with `MESA_GL_VERSION_OVERRIDE=4.0 MESA_GLSL_VERSION_OVERRIDE=400`.

#### Gray water {#Gray_water}

Download the TheCenter map and copy `Water_DepthBlur_MIC.uasset` from that map into TheIsland as described [here](https://www.gamingonlinux.com/articles/heres-a-way-to-fix-the-broken-water-in-ark-survival-evolved-on-linux.10530)^\[[dead\ link](https://en.wikipedia.org/wiki/Wikipedia:Link_rot "wikipedia:Wikipedia:Link rot")\ 2024-07-30---HTTP 404\]^.

Ragnarok uses TheIsland\'s texture, so the same procedure fixes the issue on Ragnarok as well.

#### Segmentation fault on startup {#Segmentation_fault_on_startup}

Caused by the games packaged libopenal. Use system libopenal to solve the segfault by running the game with with `LD_PRELOAD=/usr/lib/libopenal.so.1`

#### Crash on joining a game {#Crash_on_joining_a_game}

Set steam to \'offline mode\' and try again

### Audiosurf 2 {#Audiosurf_2}

#### error. unable to load song \<filename\> ,came back with zero duration {#error._unable_to_load_song_<filename>_,came_back_with_zero_duration}

If you get this in your log, install [pulseaudio-alsa](https://archlinux.org/packages/?name=pulseaudio-alsa).

### BADLAND: Game of the Year Edition {#BADLAND:_Game_of_the_Year_Edition}

Refer to [#Missing libcurl.so.4 or version CURL_OPENSSL_3 not found](#Missing_libcurl.so.4_or_version_CURL_OPENSSL_3_not_found).

### Barony {#Barony}

#### Broken/Incorrect Textures {#Broken/Incorrect_Textures}

Use the following launch options:

    LD_PRELOAD="$LD_PRELOAD ./libSDL2-2.0.so.0 ./libSDL2_ttf-2.0.so.0 ./libSDL2_image-2.0.so.0" %command%

The issue is caused by a newer version of SDL than what the game bundles, this workaround simply has the game use the bundled libraries instead, as described [here](https://github.com/TurningWheel/Barony/issues/568).

### BATTLETECH {#BATTLETECH}

#### Game freezes after opening studio credits (opening cinematic does not play) {#Game_freezes_after_opening_studio_credits_(opening_cinematic_does_not_play)}

Try installing [libbsd](https://archlinux.org/packages/?name=libbsd) (as suggested in the [Paradox forums](https://forum.paradoxplaza.com/forum/threads/battletech-black-screen-after-initial-credit-logos-linux.1312273/post-26187776)).

#### Game does not start {#Game_does_not_start_2}

Try deleting *`BATTLETECH`*`/BattleTech_Data/plugins/x86_64/libc.so.6`, this should make the game run again.

### Beat Cop {#Beat_Cop}

#### \"BeatCop.x86_64\" is not responding {#\"BeatCop.x86_64\"_is_not_responding}

Run `BeatCop.x86` instead of `BeatCop.x86_64`.

### Binding of Isaac: Rebirth {#Binding_of_Isaac:_Rebirth}

#### No sound {#No_sound}

**Note** This also helps with Never Alone (Kisima Ingitchuna) and No Time to Explain.

Prepend `/usr/lib` to `LD_LIBRARY_PATH`.

Adjust the audio levels in the game options.

### BioShock Infinite {#BioShock_Infinite}

#### Game launching on wrong monitor in fullscreen mode {#Game_launching_on_wrong_monitor_in_fullscreen_mode}

Add the following launch option:

    --eon_force_display=1

Various more fixes and tweaks can be found [here](https://pcgamingwiki.com/wiki/BioShock_Infinite)

#### Audio crackling {#Audio_crackling}

Change the launch options to

    PULSE_LATENCY_MSEC=60 %command%

Discussion on the variable can be found in [Proton issue #1209](https://github.com/ValveSoftware/Proton/issues/1209). Lower values maintain lower audio latency but crackling may still occur; higher values are more likely to eliminate crackling but allow for higher audio latency.

### BLACKHOLE {#BLACKHOLE}

Refer to [#Missing libcurl.so.4 or version CURL_OPENSSL_3 not found](#Missing_libcurl.so.4_or_version_CURL_OPENSSL_3_not_found).

### Black Mesa {#Black_Mesa}

If the game have crashing on start, install [lib32-gperftools](https://aur.archlinux.org/packages/lib32-gperftools/)^AUR^ for 32bit version of `libtcmalloc_minimal.so.4` which is needed [Source](https://steamcommunity.com/app/362890/discussions/1/340412628175324858/?ctp=7).

Also add this to the game\'s launch command line in Steam\'s preferences:

    %command% -oldgameui

### Block\'hood {#Block'hood}

#### White screen on startup {#White_screen_on_startup}

When launched the game may only display a white screen with no interface and no way to play the game. Add \"-screen-fullscreen 0\" to launch options.

### The Book of Unwritten Tales {#The_Book_of_Unwritten_Tales}

Dependencies:

-   [lib32-jasper](https://aur.archlinux.org/packages/lib32-jasper/)^AUR^
-   [lib32-libxaw](https://aur.archlinux.org/packages/lib32-libxaw/)^AUR\[[broken\ link](../../en/Help:Procedures.html#Fix_broken_package_links "Help:Procedures"):\ package\ not\ found\]^

If the game does not start, uncheck: *Properties \> Enable Steam Community In-Game*.

The game is known to segfault when opening the settings and possibly during or before playing. A workaround from the [Steam discussions](https://steamcommunity.com/app/221410/discussions/3/846939071081758230/#p2) is to replace the game\'s `RenderSystem_GL.so` with one from Debian\'s repositories. To do that download [this deb file](https://launchpad.net/ubuntu/+archive/primary/+files/libogre-1.7.4_1.7.4-3_i386.deb), and extract it with [dpkg](https://archlinux.org/packages/?name=dpkg):

    $ dpkg -x libogre-*.deb outdir

Now replace *`GAME`*`/lib/32/RenderSystem_GL.so` with the one extracted from the `.deb` package.

### BRAIN/OUT {#BRAIN/OUT}

If the game does not start with error message saying \"invalid app configuration\". Go to the game directory:

    $ cd ~/.steam/steam/steamapps/common/BrainOut/

Run the game directly:

    $ java -jar brainout-steam.jar

You need to have steam running in the background.

### The Book of Unwritten Tales: The Critter Chronicles {#The_Book_of_Unwritten_Tales:_The_Critter_Chronicles}

See [#The Book of Unwritten Tales](#The_Book_of_Unwritten_Tales).

To prevent the game from crashing at the end credits, change the size of the credits image as described [here](https://steamcommunity.com/app/221830/discussions/0/828925849276110960/#c810921273836530791).

### Borderlands 2 {#Borderlands_2}

**Warning** The Linux native version of Borderlands 2 does not have working Steam multiplayer, cannot use Steam Cloud saves made on the Windows version, does not support the *Commander Lilith & the Fight for Sanctuary* DLC, and has several other issues. Most players report via [ProtonDB](https://www.protondb.com/app/49520), that Proton overall works best.

#### Proton troubleshooting {#Proton_troubleshooting}

##### Game crashes instantly on launch {#Game_crashes_instantly_on_launch}

Borderlands 2 is a 32-bit DirectX 9 based game, therefore it is possible on 64-bit installs to be missing 32-bit Vulkan drivers. Installing the [steam-native-runtime](https://archlinux.org/packages/?name=steam-native-runtime) or specifically the appropriate multilib drivers ([lib32-nvidia-utils](https://archlinux.org/packages/?name=lib32-nvidia-utils) or [lib32-vulkan-radeon](https://archlinux.org/packages/?name=lib32-vulkan-radeon) for NVIDIA and AMD Radeon respectively) may resolve the issue.

#### Linux Native troubleshooting {#Linux_Native_troubleshooting}

##### Migrating saves from other platforms {#Migrating_saves_from_other_platforms}

Borderlands 2 does not support cross-platform Steam Cloud syncing, you have to manually copy the files between platforms. Save locations can be found [here](https://pcgamingwiki.com/wiki/Borderlands_2#Game_data). Make sure your user can access the files.

##### Using Ctrl Key {#Using_Ctrl_Key}

Borderlands 2 does not allow the `Ctrl` key to be used by default. The game seems to be accessing keycodes and not keysyms, therefore xmodmap has no affect. A workaround is using *setkeycodes* to map the Ctrl-scancode to some other key, as described in [Map scancodes to keycodes#Using setkeycodes](../../en/Map_scancodes_to_keycodes.html#Using_setkeycodes "Map scancodes to keycodes"). I use `setkeycodes 0x1d 56` (as root) to map Ctrl to Alt before starting the game and `setkeycodes 0x1d 29` to restore the default.

##### Logging into SHiFT {#Logging_into_SHiFT}

Out of the box you will not be able to log into SHiFT since the game expects certificates to be in `/usr/lib/ssl`, which is where Ubuntu stores them. Arch however uses `/etc/ssl`. To resolve the problem, run the game with `SSL_CERT_DIR=/etc/ssl/certs`.

##### Game crashes nearly instantly {#Game_crashes_nearly_instantly}

The game crashes in libopenal directly after launch.

Possible solution 0: Run the game with the `-nostartupmovies` flag. It no longer crashes in libopenal with a general protection error.

Possible solution 1: As of lib32-openal version 1.18.0-1, the game crashes instantly. The possible solutions are to downgrade lib32-openal to 1.17.2-1, or to start the game with `LD_PRELOAD='$HOME/.steam/root/ubuntu12_32/steam-runtime/i386/usr/lib/i386-linux-gnu/libopenal.so.1'`.

In case there are messages like this in the terminal:

    [  671.617205] Borderlands2[2772]: segfault at 0 ip           (null) sp 00000000ff9a462c error 14 in Borderlands2[8048000+235a000]

The following change may help ([source](https://steamcommunity.com/app/49520/discussions/0/348292787746982160/)):

    LD_PRELOAD='./libcxxrt.so:/usr/$LIB/libstdc++.so.6' %command%

Possible solution 2: Launch steam as `steam-native` as described in [#Steam native runtime](../../en/Steam/Troubleshooting.html#Steam_native_runtime "Steam/Troubleshooting"). If the game still fails to launch even after installing the [steam-native-runtime](https://aur.archlinux.org/packages/steam-native-runtime/)^AUR^ meta package, then you might be missing some libraries. You can find those missing libraries as described in [#Debugging shared libraries](../../en/Steam/Troubleshooting.html#Debugging_shared_libraries "Steam/Troubleshooting").

### Borderlands: The Pre-Sequel {#Borderlands:_The_Pre-Sequel}

See [#Borderlands 2](#Borderlands_2).

#### Keyboard not working {#Keyboard_not_working}

This can occur with certain window managers e.g. [dwm](../../en/Dwm.html "Dwm"). Try a different [window manager](../../en/Window_manager.html "Window manager"), or install [wmname](https://archlinux.org/packages/?name=wmname) and run:

    $ wmname LG3D

see [Java#Impersonate another window manager](../../en/Java.html#Impersonate_another_window_manager "Java") for more information.

#### Not starting via Steam {#Not_starting_via_Steam}

If the game appears as *Running*, then syncs and closes when you launch it from Steam, try creating a `steam_appid.txt` in the game directory containing `261640`. This should resolve the issue and let you start the game directly from the game directory. If that does not work, try using the [steam-native-runtime](https://aur.archlinux.org/packages/steam-native-runtime/)^AUR^.

### Celeste {#Celeste}

#### Steam overlay is missing text {#Steam_overlay_is_missing_text}

Add the following [launch option](../../en/Launch_option.html "Launch option") (as documented [in this issue](https://github.com/ValveSoftware/steam-for-linux/issues/7889#issuecomment-917554177)):

    -gldevice:Vulkan

### Chaos Engine {#Chaos_Engine}

Set your [launch options](../../en/Launch_option.html "Launch option") to:

    LD_PRELOAD="/usr/lib32/libpng16.so.16" %command%

If such error is seen in terminal output of steam-native:

    /home/username/.local/share/Steam/steamapps/common/Chaos engine/TheChaosEngineSteam: /home/username/.local/share/Steam/steamapps/common/Chaos engine/lib/libz.so.1: version `ZLIB_1.2.9' not found (required by /usr/lib32/libpng16.so.16)
    /home/username/.local/share/Steam/steamapps/common/Chaos engine/TheChaosEngineSteam: /home/username/.local/share/Steam/steamapps/common/Chaos engine/lib/libz.so.1: version `ZLIB_1.2.3.4' not found (required by /usr/lib32/libpng16.so.16)

Then link the system libz.so:

    $ cd ~/.local/share/Steam/steamapps/common/Chaos\ engine/lib
    $ mv libz.so.1 libz.so.1.old
    $ ln -s /lib/libz.so.1

### Cities in Motion 2 {#Cities_in_Motion_2}

#### Dialog boxes fail to display properly {#Dialog_boxes_fail_to_display_properly}

You will not be able to read or see anything, and you will have this in your logs:

    Fontconfig error: "/etc/fonts/conf.d/10-scale-bitmap-fonts.conf", line 69: non-double matrix element
    Fontconfig error: "/etc/fonts/conf.d/10-scale-bitmap-fonts.conf", line 69: wrong number of matrix elements

A workaround for the bug [FS#35039](https://bugs.archlinux.org/task/35039) is to remove line 69 from `/etc/fonts/conf.d/10-scale-bitmap-fonts.conf` (i.e. `<double>0</double> <name>pixelsizefixupfactor</name>`).

### Cities Skylines {#Cities_Skylines}

#### Game not starting {#Game_not_starting}

If you set `ELECTRON_OZONE_PLATFORM_HINT=auto` [environment variables](../../en/Environment_variables.html "Environment variables") globally, because you want to switch all your [Electron](../../en/Electron.html "Electron") apps use [Wayland](../../en/Wayland.html "Wayland") natively, you should know that the game launcher of Cities Skylines currently is [Electron](../../en/Electron.html "Electron")-based and compiled as [x11](../../en/Xorg.html "X11")-only, without [Wayland](../../en/Wayland.html "Wayland") support. So it will crashed when you try to start it. As workaround you should set `ELECTRON_OZONE_PLATFORM_HINT=x11 %command%` to the [Steam](../../en/Steam.html "Steam")\'s command line for this game. So the game will work using [Xwayland](../../en/Wayland.html#Xwayland "Xwayland").

If you set `$XDG_DATA_HOME` to something other than `$HOME/.local/share`, Cities Skylines will put some files in `$XDG_DATA_HOME/Paradox Interactive` and some hard-coded in `~/.local/share/Paradox Interactive`. Unset the variable to fix this issue.

#### Textures not rendering properly {#Textures_not_rendering_properly}

Run the game with `UNITY_DISABLE_GRAPHICS_DRIVER_WORKAROUNDS=yes`.

#### Game crashes in loading screen when Node Controller or Intersection Marking tool are enabled in Content Manager {#Game_crashes_in_loading_screen_when_Node_Controller_or_Intersection_Marking_tool_are_enabled_in_Content_Manager}

If the game crashes with one or both of the above mods enabled when loading a save or starting a new game but works fine with both mods disabled, install [mono](https://archlinux.org/packages/?name=mono).

### Civilization V {#Civilization_V}

Run the game with `LD_PRELOAD=/usr/lib32/libopenal.so.1 %command%`.[\[7\]](https://steamcommunity.com/app/8930/discussions/0/1621726179576099775/) If `libopenal.so.1` is not in `/usr/lib32`, you may need to install [lib32-openal](https://aur.archlinux.org/packages/lib32-openal/)^AUR^ after making sure [multilib](../../en/Official_repositories.html#multilib "Multilib") is enabled.

For old versions of PulseAudio (\<12.0), use `LD_PRELOAD='./libcxxrt.so:/usr/$LIB/libstdc++.so.6:/usr/lib32/libopenal.so.1' %command%`.[\[8\]](https://github.com/ValveSoftware/steam-for-linux/issues/4379)

If you are experiencing heavy lag (less than 1fps) or the game crashes on startup, try adding the following paths to LD_PRELOAD: `'/usr/$LIB/libgcc_s.so.1 /usr/$LIB/libxcb.so.1 /usr/$LIB/libgpg-error.so ./libcxxrt.so /usr/lib32/libstdc++.so.6 /usr/lib32/libopenal.so.1'`.[\[9\]](https://forum.manjaro.org/t/civ-v-wont-launch-after-update/10825/6)^\[[dead\ link](https://en.wikipedia.org/wiki/Wikipedia:Link_rot "wikipedia:Wikipedia:Link rot")\ 2021-05-17---HTTP 404\]^

#### Stuttering sound with PulseAudio {#Stuttering_sound_with_PulseAudio}

See [PulseAudio/Troubleshooting#Laggy sound](../../en/PulseAudio/Troubleshooting.html#Laggy_sound "PulseAudio/Troubleshooting").

#### Segfault with high core count CPU {#Segfault_with_high_core_count_CPU}

The Linux port of Civ V experiences a bug which induces segfaults when running on a CPU with \>8 logical cores. This includes many common CPUs, especially Ryzen 7 and i7 series parts. To diagnose this problem, check the output of dmesg:

    # journalctl -k | grep -E "Civ5XP.*segfault"

One solution is to run `taskset -c 0-7 steam steam://rungameid/8930`, which limits the number of cores that the game can access[\[10\]](https://steamcommunity.com/app/8930/discussions/0/1693788384127278334/). It is convenient to run this in the launch options:

    LD_PRELOAD=/usr/lib32/libopenal.so.1 taskset -c 0-7 %command%

Another solution is to set `MaxSimultaneousThreads` to `16` in `config.ini`, which is stored in the game directory.[\[11\]](https://www.reddit.com/r/civ5/comments/5z77jr/game_crashes_randomly_on_linux_amd_ryzen/)

#### Game crashes after intro video with \"Unable to load texture (LoadingBaseGame.dds)\" / configuration reset at startup {#Game_crashes_after_intro_video_with_\"Unable_to_load_texture_(LoadingBaseGame.dds)\"_/_configuration_reset_at_startup}

The issue is a result of the game calling some file in a case-insensitive manner.

The solution is either to install the game on a case-insensitive file system like VFAT, or on a mount point for [ciopfs](https://aur.archlinux.org/packages/ciopfs/)^AUR^.

It is not enough the game is in a case-insensitive filesystem, but also the configuration/data directory at \"\~/.local/share/Aspyr/Sid Meier\'s Civilization 5\" needs to be in a case-insensitive filesystem or mount point. If the data directory is in a case-sensitive filesystem, the game will not work correctly and symptoms such as configuration getting constantly reset can be observed.

#### Steam Overlay not working {#Steam_Overlay_not_working}

An invisible Steam Overlay can be fixed by preloading the overlay renderer in the launch options:

    LD_PRELOAD='/home/username/.local/share/Steam/ubuntu12_32/gameoverlayrenderer.so' %command%

#### Crashes during \_\_memcpy_ssse3 {#Crashes_during_memcpy_ssse3}

This appears to be a memory alignment bug that can be corrected by compiling the libraries with `-mstackrealign`. GDB can also be used to run it as-is with the following launch options:

    LD_PRELOAD=/usr/lib/libcurl.so.4 /bin/gdb -windows -batch -return-child-result -nx -eval-command="run" -exec=%command%

### Civilization: Beyond earth {#Civilization:_Beyond_earth}

If you are getting an instant crash/close upon launch, make sure you have the following packages installed:

-   [lib32-libcurl-compat](https://archlinux.org/packages/?name=lib32-libcurl-compat)
-   [lib32-libcurl-gnutls](https://archlinux.org/packages/?name=lib32-libcurl-gnutls)
-   [lib32-openal](https://aur.archlinux.org/packages/lib32-openal/)^AUR^

You also need an older version of lib32-tbb which provides libtbb.so.2. To get this:

1.  Download the [libtbb2 deb-package](https://archive.ubuntu.com/ubuntu/pool/universe/t/tbb/libtbb2_4.2~20130725-1.1ubuntu1_i386.deb) from the Ubuntu archive.
2.  Unpack `libtbb.so.2` from `libtbb2_4.2_20130725-1.1ubuntu1_i386.deb/data.tar.xz/usr/lib` into the game directory.

Note that if you have a globally installed 32-bit libtbb.so.2, you will need to run the game with:

1.  Run the game with `LD_PRELOAD='./libtbb.so.2'`.

To force it to use this version. This version also resolves crashes with the following backtrace:

       #0  0x08b71d06 in FireGrafix::DynamicsLock<Graphics::BuildingSkinnedDataDynamicConsts>::DynamicsLock(Graphics::SurfaceSet**, FireGrafix::SurfaceSetPoolAllocator*, unsigned short) ()
       #1  0x08c25ffc in cvLandmarkVisSystem::cvLandmarkVisDynamicConstantUpdaterSS::HandleBuildingShaderSkinned(Graphics::FGXShaderPackageInstanceView*, FireGrafix::FGXModelNode*, FGXVector4*) ()
       #2  0x08c25f34 in cvLandmarkVisSystem::cvLandmarkVisDynamicConstantUpdaterSS::UpdateNode(Graphics::FGXShaderPackageInstanceView*, FireGrafix::FGXModelNode*, FGXVector4*) ()
       #3  0x08c25e2c in FireGrafix::FGXModelRenderByNodeSSExample_Shadow<cvLandmarkVisSystem::cvLandmarkVisDynamicConstantUpdaterSS, 2, FireGrafix::FGXModelRenderEndSuperclass>::RenderNode(unsigned int*, FireGrafix::FGX_SPIV_GENERIC*, FireGrafix::FGXModelNode*, FGXVector4*) ()
       #4  0x08c24ff5 in cvLandmarkVisSystem::LandmarkRenderJob::Execute(unsigned int) ()
       #5  0x093d26d9 in Platform::JobTask::execute() ()
       #6  0xf749f3c0 in ?? () from /usr/lib32/libtbb.so.2
       #7  0xf7497551 in ?? () from /usr/lib32/libtbb.so.2
       #8  0xf7495fc3 in ?? () from /usr/lib32/libtbb.so.2
       #9  0xf7491b7e in ?? () from /usr/lib32/libtbb.so.2
       #10 0xf7491db7 in ?? () from /usr/lib32/libtbb.so.2
       #11 0xf78f4346 in start_thread () from /usr/lib32/libpthread.so.0
       #12 0xf7716026 in clone () from /usr/lib32/libc.so.6

### Civilization VI {#Civilization_VI}

Although there is a native [#Civilization VI Linux version](#Civilization_VI_Linux_version), many users report better performance with the [#Civilization VI Windows version](#Civilization_VI_Windows_version).

#### Civilization VI Linux version {#Civilization_VI_Linux_version}

Either run with steam-native, launch option `LD_PRELOAD='/usr/lib/libfreetype.so.6:/usr/lib/libbrotlicommon.so.1:/usr/lib/libbrotlidec.so.1' %command%`, and go to *Properties \> Compatibility*, check \"Force the use of a specific Steam Play compatiblity tool\" and select \"Steam Linux runtime\".

If you are using [Wayland](../../en/Wayland.html "Wayland"), you might need to also set `QT_QPA_PLATFORM=xcb`, as the game\'s launcher uses a version of Qt which only supports Xorg (see [Wayland#Qt](../../en/Wayland.html#Qt "Wayland")), another way is to replace the bundled Qt with one provided by Arch Linux [\[12\]](https://www.patreon.com/posts/running-civ6-53028614). Some versions of the game also seem to require adding `SDL_VIDEODRIVER=x11` and will otherwise refuse to start with an error message that reads \"An unrecoverable error has occurred, and Civilization VI cannot continue.\"

**This article or section is out of date.**

**Reason:** The OpenSSL 1.0 package has been dropped, is this game still affected? (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

Follow [#OpenSSL 1.0 setup](#OpenSSL_1.0_setup).

Ensure that Steam Workshop mods are disabled as certain ones may cause issues following loading.

##### Steam Overlay not working {#Steam_Overlay_not_working_2}

Since the introduction of the new launcher, the steam overlay does not work in this game. To get it working again, simlpy skip the launcher as described in [#Launcher unable to load page](#Launcher_unable_to_load_page).

##### If Segfault Immediately on Start {#If_Segfault_Immediately_on_Start}

This is a strange corner case which happens infrequently at best (and the prerequisites for reproducing it are unknown), but the crash would look like this:

1.  Immediate segfault on start, before any windows get created
2.  The game creates `~/.local/share/aspyr-media/Sid Meier's Civilization VI/AppOptions.txt`
3.  The string `AppHost::BugSubmissionPackager::BugSubmissionPackager` appears in the backtrace output when running the game under [gdb](https://archlinux.org/packages/?name=gdb)
    1.  To run under [gdb](https://archlinux.org/packages/?name=gdb), first launch a shell and change into the game directory.
    2.  Then `echo 289070 > steam_appid.txt` *(otherwise the game will not launch outside of Steam itself)*
    3.  Then run something like `gdb -ex run -ex bt -ex quit --args ./Civ6 ./Civ6`
    4.  The relevant info towards the end of the output should look like this:

&nbsp;

       Thread 3 "Civ6" received signal SIGSEGV, Segmentation fault.
       [Switching to Thread 0x7fffe5d06700 (LWP 12315)]
       0x000000000201121e in AppHost::BugSubmissionPackager::BugSubmissionPackager(unsigned long, String::BasicT<Platform::StaticHeapAllocator<5, 0>, (String::Encoding)4> const&, String::BasicT<Platform::StaticHeapAllocator<5, 0>, (String::Encoding)0> const&, AppHost::ModuleVersionInfo const&) ()
       #0  0x000000000201121e in AppHost::BugSubmissionPackager::BugSubmissionPackager(unsigned long, String::BasicT<Platform::StaticHeapAllocator<5, 0>, (String::Encoding)4> const&, String::BasicT<Platform::StaticHeapAllocator<5, 0>, (String::Encoding)0> const&, AppHost::ModuleVersionInfo const&) ()
       #1  0x000000000200c796 in AppHost::_INTERNAL::SetupFXSPlatform(AppHost::AppEnvironment const*, AppHost::AppOptions*)
           ()
       #2  0x000000000200fea0 in AppHost::RunApp(int, char**, AppHost::Application*) ()
       #3  0x000000000200f9bc in AppHost::RunApp(char*, AppHost::Application*) ()
       #4  0x0000000001112d98 in WinMain ()
       #5  0x00000000010bdab0 in ?? ()
       #6  0x00000000010bfb31 in ThreadHANDLE::ThreadProc(void*) ()
       #7  0x00007ffff473e08a in start_thread () from /usr/lib/libpthread.so.0
       #8  0x00007ffff38f747f in clone () from /usr/lib/libc.so.6

If all of that is the case for you, the fix is pretty simple. Edit `~/.local/share/aspyr-media/Sid Meier's Civilization VI/AppOptions.txt` and change the line reading `EnableBugCollection 1` to `EnableBugCollection 0`.

Presumably this fix will prevent any automated bug reports from reaching Aspyr, should you encounter crashes/bugs in the future, but it will at least let the game launch properly.

##### If Crash with Error \"undefined symbol FT_Done_MM_Var\" {#If_Crash_with_Error_\"undefined_symbol_FT_Done_MM_Var\"}

If the game crashed with:

    ./GameGuide/Civ6: symbol lookup error: /usr/lib/libfontconfig.so.1: undefined symbol: FT_Done_MM_Var

The solution is to set launch options to:

    LD_PRELOAD=/usr/lib/libfreetype.so.6 %command%

##### If the game ends up being a grey-color blank screen {#If_the_game_ends_up_being_a_grey-color_blank_screen}

The solution is to disable mods.

##### If the computer becomes irresponsive after \"Loading\" screen {#If_the_computer_becomes_irresponsive_after_\"Loading\"_screen}

This may be caused by amdgpu driver crash due to insuffcient video memory. If running an integrated graphics (eg. AMD Renoir), try allocating more memory in your BIOS.

##### Multi-monitor and wayland: mismatched resolution {#Multi-monitor_and_wayland:_mismatched_resolution}

Wayland does not define a primary monitor, so the game will show the available resolutions of an arbitrary monitor; it may not have the same size and the mouse may be off. A solution is to set an Xwayland monitor as primary.

To find the list of Xwayland monitors: `xrandr --listmonitors`

To set (eg) the XWAYLAND4 monitor as the primary: `xrandr --output XWAYLAND4 --primary`

##### Launcher window is huge (wrong scaling) {#Launcher_window_is_huge_(wrong_scaling)}

If the launcher window is huge (sometimes bigger than the screen), then the scaling is wrong. Add `QT_AUTO_SCREEN_SCALE_FACTOR=0` to the launch options and on next start the launcher should be usable.

##### Launcher unable to load page {#Launcher_unable_to_load_page}

The launcher often shows errors like `Error loading page`. It is possible to bypass the launcher by editing the games startup configuration `~/.local/share/Steam/steamapps/common/Sid Meier's Civilization VI/Civ6` and changing the line `./GameGuide/Civ6` to `./Civ6Sub`.

#### Civilization VI Windows version {#Civilization_VI_Windows_version}

To play the Windows version of Civ VI, first you must [force Proton usage](../../en/Steam.html#Force_Proton_usage "Steam"). Then, you need to bypass the launcher which is buggy through proton. To skip the launcher, right click on the game, click *Properties*, and set the following *Launch options*:

    eval $( echo "%command%" | sed "s/2KLauncher\/LauncherPatcher.exe'.*/Base\/Binaries\/Win64Steam\/CivilizationVI.exe'/" )

### The Clockwork Man {#The_Clockwork_Man}

Requires [lib32-libidn](https://aur.archlinux.org/packages/lib32-libidn/)^AUR^ (pulled in by [steam-native-runtime](https://aur.archlinux.org/packages/steam-native-runtime/)^AUR^).

### Company of Heroes 2 {#Company_of_Heroes_2}

Make sure you have [lib32-gconf](https://aur.archlinux.org/packages/lib32-gconf/)^AUR^ installed.

#### Missing libpcre.so.3 and libidn.so.11 {#Missing_libpcre.so.3_and_libidn.so.11_2}

Like with [#Alien Isolation](#Alien_Isolation) you need to symlink `/usr/lib/libpcre.so` to *`GAME`*`/lib/`*`arch`*`/libpcre.so.3`, as well as `/usr/lib/libidn.so` to *`GAME`*`/lib/`*`arch`*`/libidn.so.11`, otherwise the game will fail to start.

### Cossacks 3 {#Cossacks_3}

#### No sound {#No_sound_2}

Use the steam-runtime, e.g. set the [launch options](https://support.steampowered.com/kb_article.php?ref=1040-JWMT-2947) to:

    ~/.steam/root/ubuntu12_32/steam-runtime/run.sh %command%

#### Flashing screen with primus {#Flashing_screen_with_primus}

Set `PRIMUS_SYNC=2`in the launch options.

### Counter-Strike: Source (CS:S) {#Counter-Strike:_Source_(CS:S)}

#### Invisible symbols, special characters and cyrillic letters {#Invisible_symbols,_special_characters_and_cyrillic_letters}

Check [#Squares or invisible symbols, special characters and cyrillic letters in Source-based games](#Squares_or_invisible_symbols,_special_characters_and_cyrillic_letters_in_Source-based_games)

### Counter-Strike: Global Offensive (CS:GO) {#Counter-Strike:_Global_Offensive_(CS:GO)}

#### Game cannot launch and crash with black screen {#Game_cannot_launch_and_crash_with_black_screen}

[CSGO not running on my Arch](https://bbs.archlinux.org/viewtopic.php?pid=2035227#p2035227)

This problem was found after the kernel update to 5.17: the game does not start properly.

A possible workaround is to change `~/.local/share/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/panorama/videos`, rename it to `videos.bak`, then add `-novid` to the startup parameters. The game will lose the background of the main game interface, but can run normally.

#### Game starts on the wrong screen {#Game_starts_on_the_wrong_screen}

[csgo-osx-linux issue #60](https://github.com/ValveSoftware/csgo-osx-linux/issues/60)

If it happens, go into fullscreen windowed or windowed mode and drag the window to the correct monitor. Then go back into fullscreen, the game should now be on the correct monitor.

#### Cannot reach bottom of the screen on menus {#Cannot_reach_bottom_of_the_screen_on_menus}

[csgo-osx-linux issue #594](https://github.com/ValveSoftware/csgo-osx-linux/issues/594)

If you have a secondary monitor you might have a part of your lower screen you cannot reach in menus. If on GNOME you can try to open the overview (Super key) and drag the game to the other monitor and back.

If you are not on GNOME or dragging the window back and forth did not work you can try to [install](../../en/Help:Reading.html#Installation_of_packages "Install") [wmctrl](https://archlinux.org/packages/?name=wmctrl) and run this command, where X and Y is the offset of the window and H and W is the size.

    $ wmctrl -r "Counter-Strike: Global Offensive - OpenGL" -e 0,X,Y,W,H

**Example** (Secondary monitor: On the left, 2560x1600. Gaming monitor: On the right, 2560x1440) :

    $ wmctrl -r "Counter-Strike: Global Offensive - OpenGL" -e 0,2560,0,1600,1200

Here X and Y are 2560,0 to move the window to the monitor on the right and W and H are 1600,1200 is set to match the in-game resolution.

#### Sound is played slightly delayed {#Sound_is_played_slightly_delayed}

[csgo-osx-linux issue #45](https://github.com/ValveSoftware/csgo-osx-linux/issues/45)

See [PulseAudio/Troubleshooting#Laggy sound](../../en/PulseAudio/Troubleshooting.html#Laggy_sound "PulseAudio/Troubleshooting") for a possible solution.

#### Mouse not working in-game {#Mouse_not_working_in-game}

If your mouse works in the main menu but not in-game, run the game with `SDL_VIDEO_X11_DGAMOUSE=0`. [\[13\]](https://bbs.archlinux.org/viewtopic.php?id=184905) If it still does not work, turn off \"Raw Input\" in the in-game settings.

#### Brightness slider not working {#Brightness_slider_not_working}

[Install](../../en/Help:Reading.html#Installation_of_packages "Install") [xorg-xrandr](https://archlinux.org/packages/?name=xorg-xrandr) and run `xrandr` to find out the name of your connected display output.

Edit *`GAME`*`/csgo.sh` and add the following lines (adapt *output_name*):

    # gamma correction
    xrandr --output output_name --gamma 1.6:1.6:1.6 # play with values if required
    STATUS=42
    while [$STATUS -eq 42]; do
     ...
    done
    # restore gamma
    xrandr --output output_name --gamma 1:1:1
    exit $STATUS

#### Microphone not working {#Microphone_not_working}

[csgo-osx-linux issue #573](https://github.com/ValveSoftware/csgo-osx-linux/issues/573#issuecomment-174016722)

CS:GO uses the default PulseAudio sound device ignoring what is configured in Steam settings.

First find out the source name of your microphone (it should start with `alsa_input.`):

    $ pacmd list-sources

Then set the default device (change the name accordingly):

    $ pacmd set-default-source device_name

Also lower the microphone level to 60% otherwise you will get some nasty background noise and you will be difficult to understand (change the name accordingly):

    $ pacmd set-source-volume device_name 0x6000

#### Mouse is unrensponsive or moves slowly {#Mouse_is_unrensponsive_or_moves_slowly}

Set launch options to:

    vblank_mode=0 %command%

Works with almost any other game.

#### Game crashes on startup with game controller plugged in {#Game_crashes_on_startup_with_game_controller_plugged_in}

-   The solution is to add `-nojoy` to the launch options: [csgo-osx-linux issue #1757](https://github.com/ValveSoftware/csgo-osx-linux/issues/1757)

&nbsp;

-   Another solution: delete startup video: [csgo-osx-linux issue #2659](https://github.com/ValveSoftware/csgo-osx-linux/issues/2659#issuecomment-934357559)

#### Some texts are missing or mis-positioned {#Some_texts_are_missing_or_mis-positioned}

[Generate](../../en/Locale.html#Generating_locales "Locale") the `en_US.UTF-8` locale will solve the problem.

#### Stuck on map loading \"Initializing World\"/\"Loading Resources\" with AMD Radeon RX 6000 series {#Stuck_on_map_loading_\"Initializing_World\"/\"Loading_Resources\"_with_AMD_Radeon_RX_6000_series}

[csgo-osx-linux issue #2801](https://github.com/ValveSoftware/csgo-osx-linux/issues/2801)

When using the amdgpu driver, some users [\[14\]](https://community.amd.com/t5/graphics/amd-csgo-loading-bug-on-current-graphics-hardware-drivers/m-p/474323) experience a problem with map loading taking longer than one minute and being stuck on \"Initializing World\" or \"Loading Resources\". You can try the following workaround:

Create the file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/udev/rules.d/70-amdgpu-mclk.rules
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
KERNEL=="card0", SUBSYSTEM=="drm", DRIVERS=="amdgpu", ATTR{device/power_dpm_force_performance_level}="manual", ATTR{device/pp_dpm_mclk}="1 2 3"
```

This disables the lowest memory clock state \"0\".

Activate immediately by [reloading udev rules](../../en/Udev.html#Loading_new_rules "Udev").

### Creeper World 3: Arc Eternal {#Creeper_World_3:_Arc_Eternal}

#### Game does not start {#Game_does_not_start_3}

**The factual accuracy of this article or section is disputed.**

**Reason:** Would this not be fixed by using native versions instead of the Steam runtime? (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

Search for `Player.log` (might be in `~/.config/unity3d/Knuckle Cracker LLC/Creeper World 3/`).

If it says somewhere in `Player.log`:

    FMOD failed to get number of drivers ... An error occured that was not supposed to.  Contact support.

Unity is probably having problem with some PulseAudio libraries.

Remove or rename all instances of libpulse-simple\* files in `/usr/lib`, `/usr/lib32`, `~/.steam/steam/ubuntu12_32/steam-runtime/i386/usr/lib/i386-linux-gnu/`, `~/.steam/steam/ubuntu12_32/steam-runtime/amd64/usr/lib/x86_64-linux-gnu/`.

### CrossCode {#CrossCode}

#### If FontConfig errors on start {#If_FontConfig_errors_on_start}

    ...
    Fontconfig error: "/etc/fonts/fonts.conf", line 6: invalid attribute 'translate'
    Fontconfig error: "/etc/fonts/fonts.conf", line 6: invalid attribute 'selector'
    Fontconfig error: "/etc/fonts/fonts.conf", line 7: invalid attribute 'xmlns:its'
    Fontconfig error: "/etc/fonts/fonts.conf", line 7: invalid attribute 'version'
    Fontconfig warning: "/etc/fonts/fonts.conf", line 9: unknown element "description"
    Fontconfig warning: "/etc/fonts/conf.d/10-hinting-slight.conf", line 4: unknown element "its:rules"
    Fontconfig warning: "/etc/fonts/conf.d/10-hinting-slight.conf", line 5: unknown element "its:translateRule"
    Fontconfig error: "/etc/fonts/conf.d/10-hinting-slight.conf", line 5: invalid attribute 'translate'
    Fontconfig error: "/etc/fonts/conf.d/10-hinting-slight.conf", line 5: invalid attribute 'selector'
    Fontconfig error: "/etc/fonts/conf.d/10-hinting-slight.conf", line 6: invalid attribute 'xmlns:its'
    Fontconfig error: "/etc/fonts/conf.d/10-hinting-slight.conf", line 6: invalid attribute 'version'
    Fontconfig warning: "/etc/fonts/conf.d/10-hinting-slight.conf", line 8: unknown element "description"
    Fontconfig warning: "/etc/fonts/conf.d/10-scale-bitmap-fonts.conf", line 4: unknown element "its:rules"
    Fontconfig warning: "/etc/fonts/conf.d/10-scale-bitmap-fonts.conf", line 5: unknown element "its:translateRule"
    ...

Download the latest version of nwjs from [here](https://nwjs.io/) and extract its contents into your CrossCode directory, overwriting the files.

Be sure to rename `nw` to `CrossCode` after.

This solution was documented to work with CrossCode 1.2 and nwjs 0.41.2 and is based on [this steam post](https://steamcommunity.com/app/368340/discussions/1/1727575977598417554/)

#### Crash during startup : X server probably went away {#Crash_during_startup_:_X_server_probably_went_away}

If the game crashes on startup, with the logs ending with a line like the following:

    [19142:19142:0315/222104.782993:ERROR:chrome_browser_main_extra_parts_x11.cc(62)] X IO error received (X server probably went away)

Add `--disable-gpu` to the launch options (as documented [in this steam post](https://steamcommunity.com/app/368340/discussions/1/1733213724900972605/?&ctp=6#c3185738591085997507)).

### Crusader Kings II {#Crusader_Kings_II}

#### No audio {#No_audio}

SDL uses [PulseAudio](../../en/PulseAudio.html "PulseAudio") by default, so to use it with [ALSA](../../en/Advanced_Linux_Sound_Architecture.html "ALSA") you need to [set](../../en/Environment_variables.html#Graphical_environment "Environment variables") the `SDL_AUDIODRIVER=alsa` environment variable.

#### Oddly sized starting window {#Oddly_sized_starting_window}

You can make full screen mode the default by setting `fullscreen=yes` in `~/.paradoxinteractive/Crusader Kings II/settings.txt`.

#### DLCs not detected {#DLCs_not_detected}

If the DLC tab in the launcher is not selectable, rename the `DLC` directory in the game directory to `dlc`.

#### Game takes ages to start {#Game_takes_ages_to_start}

If you are using a NVIDIA graphics card, make sure you have enabled the [DRM kernel mode setting](../../en/NVIDIA.html#DRM_kernel_mode_setting "NVIDIA").

#### Game does not start at all {#Game_does_not_start_at_all}

If the game stopped launching after Patch 3.3 (when the game became 64-bit only), install [onetbb](https://archlinux.org/packages/?name=onetbb).

### Crypt of the NecroDancer {#Crypt_of_the_NecroDancer}

#### Crashes after splash screen {#Crashes_after_splash_screen}

The following error occurs if launching Steam from the terminal.

    FMOD ERROR: UpdateFMOD SystemUpdate: This command failed because System::init or System::setDriver was not called.

This error is solved by installing [pulseaudio-alsa](https://archlinux.org/packages/?name=pulseaudio-alsa).

#### Game does not launch at all (Wayland) {#Game_does_not_launch_at_all_(Wayland)}

On Wayland, it is currently (as of May 2024) necessary to add `SDL_VIDEODRIVER=x11` to your launch options. If you have not added any launch options, also add `%command%` at the end of your launch options. Game should launch normally.

### The Curious Expedition {#The_Curious_Expedition}

#### Game stuck on loading screen {#Game_stuck_on_loading_screen}

The Electron shipped with this game is too old for Arch Linux.

Install [electron](https://archlinux.org/packages/?name=electron) and run the game with `electron resources/app.asar`.

### Death Road To Canada {#Death_Road_To_Canada}

#### No music {#No_music}

Prepend `/usr/lib` to `LD_LIBRARY_PATH`.

### Deus Ex: Mankind Divided {#Deus_Ex:_Mankind_Divided}

**This article or section is out of date.**

**Reason:** The OpenSSL 1.0 package has been dropped, is this game still affected? (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

Follow [#OpenSSL 1.0 setup](#OpenSSL_1.0_setup).

Requires [libidn11](https://aur.archlinux.org/packages/libidn11/)^AUR^ & [librtmp0](https://aur.archlinux.org/packages/librtmp0/)^AUR^.

Also if you use Bumblebee set your [launch options](../../en/Launch_option.html "Launch option") to:

    LD_PRELOAD="$LD_PRELOAD:libpthread.so.0:libGL.so.1" __GL_THREADED_OPTIMIZATIONS=1  optirun %command%

If the game will not activate and you are running [systemd-resolved](../../en/Systemd-resolved.html "Systemd-resolved") and Proton, follow [Steam/Troubleshooting#Games running with Proton 5.13+ have no Internet connectivity](../../en/Steam/Troubleshooting.html#Games_running_with_Proton_5.13+_have_no_Internet_connectivity "Steam/Troubleshooting").

### Dirt {#Dirt}

**This article or section is out of date.**

**Reason:** The OpenSSL 1.0 package has been dropped, is this game still affected? (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

Follow [#OpenSSL 1.0 setup](#OpenSSL_1.0_setup).

### Dirt Rally {#Dirt_Rally}

Run the beta version: right click on the game, then *Properties... \> Betas*, enter the code: \"feraldirtsupport\" and click *Check Code*, finally, choose *feral_support_branch* as the version.

To use the native libraries, [installing](../../en/Help:Reading.html#Installation_of_packages "Install") [gconf](https://aur.archlinux.org/packages/gconf/)^AUR^ and [libldap24](https://aur.archlinux.org/packages/libldap24/)^AUR^ is required.

If you use [Wayland](../../en/Wayland.html "Wayland"), start the game with `SDL_VIDEODRIVER=x11`. Similarly, if you use [PipeWire](../../en/PipeWire.html "PipeWire"), start the game with `SDL_AUDIODRIVER=pulseaudio` - other backends might also work, but the default one does not.

Due to changes in how linking works, the game might not properly load its bundled dependencies. To fix this, you can either run the game with `LD_LIBRARY_PATH="`*`GAME`*`/lib/x86_64/"` or symlink the libraries from *`GAME`*`/lib/x86_64/*` to *`GAME`*`/lib/*`.[\[15\]](https://github.com/FeralInteractive/ferallinuxscripts/issues/3#issuecomment-326052969)

The game may also segfault if you use an AMD Zen 3 or newer CPU. To fix this you can hack together a small shared library to replace the `mprotect` function and make sure the allocated memory has the `PROT_READ` access flag.[\[16\]](https://news.ycombinator.com/item?id=25821288). Here is an example:

    $ cat game.c
    #include <sys/mman.h>
    #include <unistd.h>
    #include <sys/syscall.h>

    int mprotect(void *addr, size_t len, int prot) {
      if (prot == PROT_EXEC) {
        prot |= PROT_READ;
      }
      return syscall(__NR_mprotect, addr, len, prot);
    }

You can then compile the library and move the shared object to the game libraries:

    $ gcc game.c -shared -o game.so
    $ mv game.so GAME/lib/

After that you can add `LD_PRELOAD=game.so` to the game launch options.

### Divinity: Original Sin - Enhanced Edition {#Divinity:_Original_Sin_-_Enhanced_Edition}

#### Game does not start when using Bumblebee optirun or primusrun {#Game_does_not_start_when_using_Bumblebee_optirun_or_primusrun}

Edit *`GAME`*`/runner.sh` to use primusrun:

    LD_LIBRARY_PATH="." primusrun ./EoCApp

#### Game does not work with mesa {#Game_does_not_work_with_mesa}

It is a known bug and they have no intention of fixing it, see [the bug](https://bugs.freedesktop.org/show_bug.cgi?id=93551).

Workaround[\[17\]](https://www.gamingonlinux.com/articles/divinity-original-sin-may-soon-work-with-mesa-drivers.8867/comment_id=81524)^\[[dead\ link](https://en.wikipedia.org/wiki/Wikipedia:Link_rot "wikipedia:Wikipedia:Link rot")\ 2024-07-30---HTTP 404\]^ (see [step by step guide](https://bugs.freedesktop.org/show_bug.cgi?id=93551#c46))

Get the following file: [https://bugs.freedesktop.org/attachment.cgi?id=125302](https://bugs.freedesktop.org/attachment.cgi?id=125302) and rename it to `divos-hack.c`

Then execute:

    $ gcc -s -O2 -shared -fPIC -o divos-hack.{so,c} -ldl

Copy the `divos-hack.so` to the *game* directory.

For GOG version, go to the said game directory and run Divinity with the following command:

    $ allow_glsl_extension_directive_midshader=true LD_PRELOAD="divos-hack.so" ./runner.sh

For *steam*, open a console, change to the divinity directory with

    $ cd ~/.steam/steam/steamapps/common/Divinity Original Sin Enhanced Edition

Launch steam and got o the preferences of the game, and open the \"Set Launch Options\" dialogue. There, put the following

    allow_glsl_extension_directive_midshader=true LD_PRELOAD="divos-hack.so:$LD_PRELOAD" %command%

Then just start the game.

### Doki Doki Literature Club {#Doki_Doki_Literature_Club}

Linux version is shipped with the Windows version, but can only be installed with Steam Play.

Native version can be started with this launch option: `./DDLC.sh # %command%`

### Don\'t Starve Together {#Don't_Starve_Together}

If you get a crash on start in `libX11.so.6.4.0`, the problem is likely a bug in SDL1.3. Unfortunately, DST is statically linked and we cannot use `LD_PRELOAD` to replace libSDL with something newer. The bug has been reported to the developer, but a possible workaround is [to patch `XGetICValues()` to not crash when it is incorrectly given a null parameter.](https://forums.kleientertainment.com/klei-bug-tracker/dont-starve-together/crash-on-startup-r32786/?do=findComment&comment=49731)

### Dota 2 {#Dota_2}

Dependencies:

-   [libudev0](https://aur.archlinux.org/packages/libudev0/)^AUR\[[broken\ link](../../en/Help:Procedures.html#Fix_broken_package_links "Help:Procedures"):\ package\ not\ found\]^
-   [libpng12](https://aur.archlinux.org/packages/libpng12/)^AUR^

#### In-game font is unreadable {#In-game_font_is_unreadable}

Run the game with `MESA_GL_VERSION_OVERRIDE=2.1`.

#### Error with libpangoft2 {#Error_with_libpangoft2}

1.  [Install](../../en/Help:Reading.html#Installation_of_packages "Install") the [pango](https://archlinux.org/packages/?name=pango) package.
2.  Remove `libpango-1.0.so` and `libpangoft2-1.0.so` in *`GAME`*`/game/bin/linuxsteamrt64`.
3.  If you are using Bumblebee add `LD_PRELOAD="libpthread.so.0 libGL.so.1" __GL_THREADED_OPTIMIZATIONS=1 optiru` to your [launch options](../../en/Launch_option.html "Launch option").

#### The game does not start {#The_game_does_not_start}

If you run the game from the terminal and, although no error is shown, try disabling: *Steam \> Settings \> In-Game \> Enable Steam Community In-Game*.

Apparently the game [#The Book of Unwritten Tales](#The_Book_of_Unwritten_Tales) has the same problem. It also describes a workaround that is untested in Dota 2.

#### Game runs on the wrong screen {#Game_runs_on_the_wrong_screen}

See [GitHub Dota 2 issue #11](https://github.com/ValveSoftware/Dota-2/issues/11)

#### Game does not start with libxcb-dri3 error message {#Game_does_not_start_with_libxcb-dri3_error_message}

After a recent Mesa update, Dota 2 stopped working. The error message is:

    SDL_GL_LoadLibrary(NULL) failed: Failed loading libGL.so.1: /usr/lib32/libxcb-dri3.so.0: undefined symbol: xcb_send_fd

#### Game has no audio {#Game_has_no_audio}

This might happen because Dota 2 is trying to output through ALSA, which has already been taken over by PulseAudio. Try installing [pulseaudio-alsa](https://archlinux.org/packages/?name=pulseaudio-alsa) and setting in-game audio output to \'Default\'.

#### Steam overlay {#Steam_overlay}

Steam distributes a copy of libxcb which is incompatible with the latest xorg libxcb. See [\[18\]](https://github.com/ValveSoftware/steam-for-linux/issues/3199), [\[19\]](https://github.com/ValveSoftware/steam-for-linux/issues/3093).

#### Clear or disable shader cache for troubleshooting purposes {#Clear_or_disable_shader_cache_for_troubleshooting_purposes}

To clear shader cache delete delete the 570 (Dota\'s app ID) directory under the steam shadercache directory e.g.

    /home/username/steam/steamapps/shadercache/

To disable shader cache add the following to dota\'s launch options:

    -vulkan_disable_steam_shader_cache

#### Chinese tips and player names not shown {#Chinese_tips_and_player_names_not_shown}

The Chinese characters in tips and player names are displayed as block characters.

The problem is caused by the font packages: [ttf-dejavu](https://archlinux.org/packages/?name=ttf-dejavu), [ttf-liberation](https://archlinux.org/packages/?name=ttf-liberation) and [ttf-ms-fonts](https://aur.archlinux.org/packages/ttf-ms-fonts/)^AUR^.

See [GitHub Steam issue #1688](https://github.com/ValveSoftware/Dota-2/issues/1688)

#### Chinese input method problem {#Chinese_input_method_problem}

Dota2 is compatible with [IBus](../../en/IBus.html "IBus") and [Fcitx](../../en/Fcitx.html "Fcitx"). XIM support Should be enabled.

    XMODIFIERS=@im=fcitx %command%

### Devil Daggers {#Devil_Daggers}

Refer to [#Missing libcurl.so.4 or version CURL_OPENSSL_3 not found](#Missing_libcurl.so.4_or_version_CURL_OPENSSL_3_not_found).

### Drox Operative {#Drox_Operative}

If the game fails to start with \"Couldn\'t find Database/database.dbl!\", manually extract the assets. assets003.zip will overwrite some files from the previous files.

    $ cd "~/.steam/root/steamapps/common/Drox Operative/Assets"
    $ unzip assets00[123].zip

### Dungeon Souls {#Dungeon_Souls}

For AMD cards this game crashes on launch, unless you start it like this:

    R600_DEBUG=mono %command%

### Dying Light {#Dying_Light}

#### Game crashes on startup {#Game_crashes_on_startup}

The game runs with the Steam setting \"Force the use of a specific Steam Play compatibility tool\" \> \"Steam Linux Runtime\"

### Dynamite Jack {#Dynamite_Jack}

Requires [lib32-sdl](https://aur.archlinux.org/packages/lib32-sdl/)^AUR^.

#### Sound Issues {#Sound_Issues}

When running on 64-bit Arch Linux, there may be \"pops and hisses\" when running Dynamite Jack. This could be caused by not having `STEAM_RUNTIME=0` set. (However, even with `STEAM_RUNTIME=0` set, the game may still sometimes start with this issue. Exiting and restarting the game seems to make the problem go away.)

#### Game does not start {#Game_does_not_start_4}

If running steam with the `STEAM_RUNTIME=0`, Dynamite Jack may have a problem starting. Check the steam error messages for this message:

    /home/username/.steam/root/steamapps/common/Dynamite Jack/bin/main: error while loading shared libraries: libSDL-1.2.so.0: cannot open shared object file: No such file or directory

Install [lib32-sdl](https://aur.archlinux.org/packages/lib32-sdl/)^AUR^ from [multilib](../../en/Official_repositories.html#multilib "Multilib") and Dynamite Jack should start up.

### Empire Total War {#Empire_Total_War}

#### Weird unreadable fonts {#Weird_unreadable_fonts}

Open `~/.local/share/feral-interactive/Empire/preferences`, then find `UsePBOSurfaces` and change it from 1 to 0.

### Euro Truck Simulator 2 {#Euro_Truck_Simulator_2}

#### Shows only a black screen {#Shows_only_a_black_screen}

Select safe mode when the game starts up.

### Factorio {#Factorio}

The game doesn\'t use NVIDIA graphics by default. To enable, add the following to the launch options:

    __GLX_VENDOR_LIBRARY_NAME=nvidia __NV_PRIME_RENDER_OFFLOAD=1 %command%

See this [forum post](https://forums.factorio.com/viewtopic.php?t=116640).

### Firewatch {#Firewatch}

If Firewatch starts but does not show anything, try running Steam with

    $ STEAM_RUNTIME_PREFER_HOST_LIBRARIES=0 steam

### Football Manager 2014 {#Football_Manager_2014}

This game will not run when installed on an [XFS](../../en/XFS.html "XFS") or ReiserFS filesystem. Workaround is to install on an ext4 filesystem.

### FORCED {#FORCED}

Requires [lib32-glu](https://archlinux.org/packages/?name=lib32-glu).

This game has 32-bit and 64-bit binaries. For some reason, Steam will launch the 32-bit binary even on 64-bit Arch Linux. When manually launching the 64-bit binary, the game starts, but cannot connect to Steam account, so you cannot play. So install 32-bits dependencies, and launch the game from Steam.

### For the King {#For_the_King}

#### With steam-native {#With_steam-native}

Starts with black page. Requires to be told to use the libSDL2 shipping with Steam

Add to Steam launch options for game:

    LD_PRELOAD=~/.local/share/Steam/ubuntu12_32/steam-runtime/amd64/usr/lib/x86_64-linux-gnu/libSDL2-2.0.so.0 %command%

Note however, that this disables the Steam overlay as a side effect.

#### With steam-runtime {#With_steam-runtime}

It works out of the box.

For the full experience, run FTK via steam-runtime instead of steam-native.

### FTL: Faster than Light {#FTL:_Faster_than_Light}

#### Compatibility {#Compatibility}

After installation, FTL may fail to run due to a \'Text file busy\' error (characterised in Steam by your portrait border going green then blue again). The easiest way to mend this is to just reboot your system. Upon logging back in FTL should run.

The Steam overlay in FTL does not function as it is not a 3D accelerated game. Because of this the desktop notifications will be visible. If playing in fullscreen, therefore, these notifications in some systems may steal focus and revert you back to windowed mode with no way of going back to fullscreen without relaunching. The binaries for FTL on Steam have no DRM and it is possible to run the game *without* Steam running, so in some cases that may be optimum - just ensure that you launch FTL via the launcher script in *`GAME`*`/data/` rather than the FTL binary in the \$arch directory.

#### Problems with open-source video driver {#Problems_with_open-source_video_driver}

FTL may fail to run if you are using an opensource driver for your video card. There are two solutions: install a proprietary video driver or delete (rename if you are unsure) the library \"libstdc++.so.6\" inside *`GAME`*`/data/amd64/lib`. This is if you are using a 64bit system. In case you are using a 32bit system you have to remove (rename) the same library located into *`GAME`*`/data/x86/lib`.

#### Artifacts when launching, Problems with openGL {#Artifacts_when_launching,_Problems_with_openGL}

Using the open source drivers, ATI for radeon cards, the game can display artifacts on screen. Run the game with `MESA_GL_VERSION_OVERRIDE=3.0 %command%`

### Game Dev Tycoon {#Game_Dev_Tycoon}

#### Game does not start {#Game_does_not_start_5}

You might get an error about missing `libudev.so.0`.

Run the game with `LD_PRELOAD=/usr/lib/libudev.so.1`.

### Garry\'s Mod {#Garry's_Mod}

#### Game does not start {#Game_does_not_start_6}

When an error about a missing `client.so` appears, try the following:

    $ cd ~/.steam/root/steamapps/common/GarrysMod/bin/
    $ ln -s libawesomium-1-7.so.0 libawesomium-1-7.so.2
    $ ln -s ../garrysmod/bin/client.so ./

If the error mentions a missing library for `libgconf-2.so.4`, install [lib32-gconf](https://aur.archlinux.org/packages/lib32-gconf/)^AUR^.

#### Opening some menus causes the game to crash {#Opening_some_menus_causes_the_game_to_crash}

Most menus work fine, but ones with checkboxes (LAN multiplayer, mounted games list) do not work at all. This is a bug in the menu code.

If you prefer the default menu style and do not mind a hacky solution: [Simon311](https://github.com/Facepunch/garrysmod-issues/issues/86#issuecomment-30935491) has written code with instructions to fix it.

If you do not care for the default menu style and want a more stable but feature-incomplete solution, Facepunch developer [robotboy655](https://github.com/robotboy655/gmod-lua-menu) has written a new menu.

#### Game crashes after attempting to join server {#Game_crashes_after_attempting_to_join_server}

While in the process of joining a server, downloading resources, etc, the game seems to hang and after a while, perhaps during the \"sending client info\" portion the game crashes, usually without any error messages. Error does not give much information, however, the process for Garry\'s mod is killed.

This issue arises more often when joining servers with many addons like DarkRP servers specifically.

The problem seems to correlate with a weak GPU and the game is timing out from the server, so if the GPU is the problem, lowering the graphics settings to the minimum should fix the problem.

The problem seems to be related to RAM usage, once you hit around 2GB of RAM used, the game will crash. Servers with many addons have much more RAM usage, and lowering graphics settings to the minimum lowers RAM usage and mitigates crashes.

Using the experimental x86-64 branch may help mitigate this issue, however keep in mind that some addons may return errors while using this branch.

### Gods will be watching {#Gods_will_be_watching}

**This article or section is out of date.**

**Reason:** The OpenSSL 1.0 package has been dropped, is this game still affected? (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

Follow [#OpenSSL 1.0 setup](#OpenSSL_1.0_setup).

### GRID Autosport {#GRID_Autosport}

**This article or section is out of date.**

**Reason:** The OpenSSL 1.0 package has been dropped, is this game still affected? (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

Follow [#OpenSSL 1.0 setup](#OpenSSL_1.0_setup).

#### Black screen when trying to play {#Black_screen_when_trying_to_play}

Run the game with `LC_ALL=C.UTF-8`.

### Guns of Icarus Online {#Guns_of_Icarus_Online}

If you encounter problems, check out the error log:

    ~/.config/unity3d/Muse Games/GunsOfIcarusOnline/Player.log

#### version \`CURL_OPENSSL_4\' not found (required by /usr/lib/libdebuginfod.so.1) {#version_`CURL_OPENSSL_4'_not_found_(required_by_/usr/lib/libdebuginfod.so.1)}

Install the package [lib32-libcurl-compat](https://archlinux.org/packages/?name=lib32-libcurl-compat) and include \'libcurl.so.4\' in your LD_PRELOAD in your shell environment like so:

    export LD_PRELOAD=$LD_PRELOAD libcurl.so.4

### Hack \'n\' Slash {#Hack_'n'_Slash}

#### Crashes when trying to load a game {#Crashes_when_trying_to_load_a_game}

Prepend `/usr/lib` to `LD_LIBRARY_PATH`.

### Hacker Evolution {#Hacker_Evolution}

Requires [lib32-sdl2_mixer](https://aur.archlinux.org/packages/lib32-sdl2_mixer/)^AUR^.

### Half-Life {#Half-Life}

#### Invisible text {#Invisible_text}

Half-Life uses microsoft fonts to display text, see [Microsoft fonts](../../en/Microsoft_fonts.html "Microsoft fonts") for ways to install them.

### Half-Life 2 and episodes {#Half-Life_2_and_episodes}

#### Cyrillic fonts problem {#Cyrillic_fonts_problem}

This problem can be solved by deleting \"Helvetica\" font.

### Hammerwatch {#Hammerwatch}

#### The game does not start via Steam {#The_game_does_not_start_via_Steam}

Prepend `/usr/lib` to `LD_LIBRARY_PATH`.

#### No sound {#No_sound_3}

Hammerwatch opens with a popup: \"Sound Error\" \-- \"Could not initialize OpenAL, no sounds will be played. Try updating your OpenAL drivers.\"

OpenAL, which Hammerwatch uses, defaults to PulseAudio. To change that, add the following line to `/etc/openal/alsoft.conf`:

    drivers=alsa,pulse

This way, Hammerwatch will use ALSA. This solution was found [here](https://stackoverflow.com/questions/9547396/what-does-al-lib-pulseaudio-c612-context-did-not-connect-access-denied-me).

### Harvest: Massive Encounter {#Harvest:_Massive_Encounter}

Dependencies:

-   [lib32-sfml](https://aur.archlinux.org/packages/lib32-sfml/)^AUR\[[broken\ link](../../en/Help:Procedures.html#Fix_broken_package_links "Help:Procedures"):\ package\ not\ found\]^
-   [lib32-libjpeg6-turbo](https://aur.archlinux.org/packages/lib32-libjpeg6-turbo/)^AUR^
-   [lib32-nvidia-cg-toolkit](https://archlinux.org/packages/?name=lib32-nvidia-cg-toolkit)
-   [lib32-gtk2](https://aur.archlinux.org/packages/lib32-gtk2/)^AUR^
-   [lib32-libvorbis](https://archlinux.org/packages/?name=lib32-libvorbis)
-   [lib32-openal](https://aur.archlinux.org/packages/lib32-openal/)^AUR^

#### Compatibility {#Compatibility_2}

If the game refuses to launch and throws you into a library installer loop, run the `Harvest` executable instead of the `run_harvest` script.

### Hatoful Boyfriend {#Hatoful_Boyfriend}

#### Japanese text invisible {#Japanese_text_invisible}

Install [wqy-microhei](https://archlinux.org/packages/?name=wqy-microhei) and [wqy-microhei-lite](https://archlinux.org/packages/?name=wqy-microhei-lite).

### HEARTBEAT {#HEARTBEAT}

#### If FontConfig Errors on Start {#If_FontConfig_Errors_on_Start_2}

Follow the same process described in [#CrossCode](#CrossCode).

### HuniePop {#HuniePop}

#### Game crashes upon launch {#Game_crashes_upon_launch}

Install [lsb-release](https://archlinux.org/packages/?name=lsb-release).

### Hyper Light Drifter {#Hyper_Light_Drifter}

#### The controller does not work {#The_controller_does_not_work}

[Install](../../en/Help:Reading.html#Installation_of_packages "Install") [lib32-sdl2](https://aur.archlinux.org/packages/lib32-sdl2/)^AUR^ and run the game with `LD_PRELOAD=libSDL2.so`.

See the following Steam Community discussions:

-   [Controller Issues](https://steamcommunity.com/app/257850/discussions/1/365163686036494421)
-   [Common Bugs + Known Issues](https://steamcommunity.com/app/257850/discussions/1/365163686045397160/)

It is suggested to run the *next_update* branch to get new fixes, there however currently is a libcurl segfault keeping it from starting without special workarounds.

#### Missing libcurl.so.4 or version CURL_OPENSSL_3 not found {#Missing_libcurl.so.4_or_version_CURL_OPENSSL_3_not_found_2}

Refer to [#Missing libcurl.so.4 or version CURL_OPENSSL_3 not found](#Missing_libcurl.so.4_or_version_CURL_OPENSSL_3_not_found).

### Rome Total War Remastered {#Rome_Total_War_Remastered}

#### Slowness of loading screen for open-source drivers {#Slowness_of_loading_screen_for_open-source_drivers}

[Install](../../en/Help:Reading.html#Installation_of_packages "Install") [vulkan-swrast](https://archlinux.org/packages/?name=vulkan-swrast) and then change the renderer option in the game launcher to llvmpipe after a system restart.

Once done the loading screen scene would then be fixed and should load up as normal for open-source drivers.

### Imperator: Rome {#Imperator:_Rome}

Paradox Launcher freezes or crashes after start. Set your launch options to:

    LD_PRELOAD=/usr/lib/libc.so.6 %command%

If the screen freezes every \~3 seconds, run:

    # chmod o-rx /dev/input/

After playing, undo it with:

    # chmod o+rx /dev/input/

### The Impossible Game {#The_Impossible_Game}

Dependencies:

-   [lib32-sdl2](https://aur.archlinux.org/packages/lib32-sdl2/)^AUR^
-   [lib32-sdl2_image](https://aur.archlinux.org/packages/lib32-sdl2_image/)^AUR^

### The Inner World {#The_Inner_World}

Requires [java-commons-codec](https://aur.archlinux.org/packages/java-commons-codec/)^AUR^ for sound support.

#### Bringing up the inventory or main menu {#Bringing_up_the_inventory_or_main_menu}

Hold the tab key.

##### Cutscenes {#Cutscenes}

The game has cutscenes. It starts directly with a cutscene before you start the actual game in the backyard. To see these cutscenes you need to use Oracle\'s [Java](../../en/Java.html "Java") instead of the OpenJDK.

Furthermore you need the package [ffmpeg-compat-55](https://aur.archlinux.org/packages/ffmpeg-compat-55/)^AUR^.

There seem to be problems with the Steam overlay. Try to run the game directly with *`GAME`*`/TIW_start.sh`.

Note that cutscenes open in a new window. So pay attention to that and switch to the new window to enjoy the movies.

See the [Steam Forums](https://steamcommunity.com/app/251430/discussions/0/611701360817206606/#c611701360827509770) for details.

### Insurgency {#Insurgency}

#### Game does not start {#Game_does_not_start_7}

Set the following launch option:

    LD_PRELOAD='/usr/$LIB/libstdc++.so.6:/usr/$LIB/libgcc_s.so.1:/usr/$LIB/libxcb.so.1:/usr/$LIB/libgpg-error.so' %command%

### Interloper {#Interloper}

Requires [alsa-lib](https://archlinux.org/packages/?name=alsa-lib).

#### Game does not start {#Game_does_not_start_8}

The game can sometimes segfault due to an incompatibility with the Steam Runtime\'s `libasound.so.2`.

### Invisible Apartment {#Invisible_Apartment}

Requires [qt5-multimedia](https://archlinux.org/packages/?name=qt5-multimedia).

#### Game does not start {#Game_does_not_start_9}

If the game does not run when you launch it via Steam, try to directly run `./ia1` in the game directory.

### Joe Danger 2: The Movie {#Joe_Danger_2:_The_Movie}

Requires [lib32-libpulse](https://archlinux.org/packages/?name=lib32-libpulse).

#### Compatibility {#Compatibility_3}

Game only worked after obtaining from the [Humble Bundle](https://www.humblebundle.com/) directly and [lib32-libpulse](https://archlinux.org/packages/?name=lib32-libpulse) was installed.

### Kerbal Space Program {#Kerbal_Space_Program}

See [Kerbal Space Program](../../en/Kerbal_Space_Program.html "Kerbal Space Program").

### Killing Floor {#Killing_Floor}

#### Cannot change screen resolution {#Cannot_change_screen_resolution}

If trying to modify the resolution in-game crashes your desktop environment, edit `~/.killingfloor/System/KillingFloor.ini`:

    [WinDrv.WindowsClient]
    WindowedViewportX=width
    WindowedViewportY=height
    FullscreenViewportX=width
    FullscreenViewportY=height
    MenuViewportX=width
    MenuViewportY=height

    [SDLDrv.SDLClient]
    WindowedViewportX=width
    WindowedViewportY=height
    FullscreenViewportX=width
    FullscreenViewportY=height
    MenuViewportX=width
    MenuViewportY=height

#### Windowed mode {#Windowed_mode}

Uncheck fullscreen in the options menu, and press `Ctrl+g` to stop mouse capturing.

#### Stuttering sound {#Stuttering_sound}

KillingFloor comes with its own OpenAL library *`GAME`*`/System/openal.so`.

Back it up, [install](../../en/Help:Reading.html#Installation_of_packages "Install") [openal](https://archlinux.org/packages/?name=openal) or [lib32-openal](https://aur.archlinux.org/packages/lib32-openal/)^AUR^ (if using a 64bit system).

Then symlink the installed system library (`/usr/lib32/libopenal.so.1` or `/usr/lib/libopenal.so.1`) to `openal.so`.

### Left for Dead 2 {#Left_for_Dead_2}

#### Missing Chinese font {#Missing_Chinese_font}

L4D2 looks for the [WenQuanYi](https://en.wikipedia.org/wiki/WenQuanYi "wikipedia:WenQuanYi") font to render Chinese text with. You can either install a package that provides the font, such as [wqy-zenhei](https://archlinux.org/packages/?name=wqy-zenhei) or [ttf-ms-fonts](https://aur.archlinux.org/packages/ttf-ms-fonts/)^AUR^, or configure a [fallback font](../../en/Font_configuration.html#Match_tests "Font configuration"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/fonts/local.conf (or ~/.config/fontconfig/fonts.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
         <match target="pattern">
                <test qual="any" name="family">
                        <string>WenQuanYi Zen Hei</string>
                </test>
                <edit name="family" mode="assign" binding="same">
                        <string>Source Han Sans CN</string>
                </edit>
        </match>
...
```

#### Game Light Too Dark {#Game_Light_Too_Dark}

Reasons of too dim in-game environment light varies, one of which is dedicated GPU is not employed.

According to multiple steam [guide](https://steamcommunity.com/sharedfiles/filedetails/?id=2816736620), please run this game using NVIDIA GPU **with 32-bit libraries support**.

### Lethal League {#Lethal_League}

Requires [lib32-glew1.10](https://aur.archlinux.org/packages/lib32-glew1.10/)^AUR^.

### Life is Strange {#Life_is_Strange}

Requires [sdl2_image](https://archlinux.org/packages/?name=sdl2_image) [librtmp0](https://aur.archlinux.org/packages/librtmp0/)^AUR^ [libidn11](https://aur.archlinux.org/packages/libidn11/)^AUR^ [libxcrypt-compat](https://archlinux.org/packages/?name=libxcrypt-compat) [lib32-libxcrypt-compat](https://archlinux.org/packages/?name=lib32-libxcrypt-compat) [gconf](https://aur.archlinux.org/packages/gconf/)^AUR^.

### Little Racers STREET {#Little_Racers_STREET}

Install [sdl2_mixer](https://archlinux.org/packages/?name=sdl2_mixer).

Move/backup *`GAME`*`/lib64/libSDL2_mixer-2.0.so.0`.

Symlink `/usr/lib/libSDL2_mixer-2.0.so.0` to *`GAME`*`/lib64/libSDL2_mixer-2.0.so.0`.

### The Long Dark {#The_Long_Dark}

#### Game does not start {#Game_does_not_start_10}

The 64-bit version fails to start. Either use the 32-bit version `tld.x86` in the game directory or start the 64-bit version like so:

    LD_PRELOAD=~/.steam/root/ubuntu12_32/steam-runtime/amd64/usr/lib/x86_64-linux-gnu/libSDL2-2.0.so.0 ./tld.x86_64

#### Game starts, but some overlay text is missing and cutscenes shows black screen {#Game_starts,_but_some_overlay_text_is_missing_and_cutscenes_shows_black_screen}

In addition to the command above, add the following to the Steam launch command:

    -screen-fullscreen 0 -screen-width WIDTH_PIXELS -screen-height HEIGHT_PIXELS

For example, if you have a screen resolution of 1280x720 and are launching the x64 version from the terminal (within the directory which contains the binaries), the full command would be:

    $ LD_PRELOAD=~/.steam/root/ubuntu12_32/steam-runtime/amd64/usr/lib/x86_64-linux-gnu/libSDL2-2.0.so.0 ./tld.x86_64 -screen-fullscreen 0 -screen-width 1280 -screen-height 720

and from Steam, the complete game [launch options](../../en/Launch_option.html "Launch option") would be:

    LD_PRELOAD=~/.steam/root/ubuntu12_32/steam-runtime/amd64/usr/lib/x86_64-linux-gnu/libSDL2-2.0.so.0 %command% -screen-fullscreen 0 -screen-width 1280 -screen-height 720

#### Cutscenes are still black {#Cutscenes_are_still_black}

Turn off Vertical Sync in the Display options, and/or set POST FX to Low in the Quality options, and/or turn global Quality options down a notch.

#### Cursor disappears {#Cursor_disappears}

Go to Options \> Controls, and set mouse locking to unlocked.

The options is visible only if you are navigating using your (invisible) mouse. It will not show up when navigating with a controller. One solution is to go to Options -\> Controls with a controller before switching to the mouse and trying to blindly it the setting.

### Grand Theft Auto V {#Grand_Theft_Auto_V}

#### BattleEye connection issues {#BattleEye_connection_issues}

**The factual accuracy of this article or section is disputed.**

**Reason:** The solution here probably does not work, as the Windows and Proton versions are distinct and according to user reports. Players may get to Online for a few minutes at maximum, whether or not having the environment variable set, which may confuse users to thinking Online mode works. You may try this workaround at your own discretion, however this section should be removed in case it is established Online does not work. It has been clearly established before GTA V only supports the Windows version of BattlEye. GTA V compatibility with Proton is tracked here: [https://github.com/ValveSoftware/Proton/issues/37](https://github.com/ValveSoftware/Proton/issues/37) (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

See [#BattlEye](#BattlEye).

Modify launch options to include `PROTON_BATTLEYE_RUNTIME`:

    PROTON_BATTLEYE_RUNTIME=~/.local/share/Steam/steamapps/common/Proton\ BattlEye\ Runtime/ %command%

#### Game crashes in Online {#Game_crashes_in_Online}

If you experience crashes in GTA Online (e.g. when creating a new character), set these launch options:

    PROTON_NO_ESYNC=1 WINEDLLOVERRIDES=winedbg.exe=d %command%

#### Graphical Issues using a NVIDIA GPU {#Graphical_Issues_using_a_NVIDIA_GPU}

Try launch options: -force-glcore42 -force-clamped

### Magicka 2 {#Magicka_2}

#### Indefinitely stuck at start {#Indefinitely_stuck_at_start}

The game does not start if the output of the command \"ip -s link\" is longer than 4096 characters. That is because, in the function bitsquid::network_info(char\*), where they query the networking information, they do not handle that case correctly. See [this picture](https://i.imgur.com/AOTLoTY.png) for reference. It was reported to upstream (Pieces Interactive) but Magicka 2 does not seem to be maintained anymore.

A dirty fix is to wrap your ip binary, as such:

    #!/bin/sh
    if [ "$*" = "-s link" ]; then
        echo "<paste a smaller subset of the normal output>"
    else
        /path/to/your/real/ip "$@"
    fi

### Mark of the Ninja {#Mark_of_the_Ninja}

#### Bad sound {#Bad_sound}

Prepend `/usr/lib` to `LD_LIBRARY_PATH`.

### Metro: Last Light {#Metro:_Last_Light}

**This article or section is out of date.**

**Reason:** References the AMD Catalyst driver, which has been abandoned for a while. (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

The game does not allow you to change its resolution on a multi-monitor setup on GNOME with the AMD Catalyst drivers. A temporary workaround is to disable the side monitors. Jason over at [unencumbered by facts](https://unencumberedbyfacts.com/2013/11/20/multiple-monitor-gaming-on-linux/) managed to get it working with his multi-monitor setup using a single display server, he however is using NVIDIA.

### Metro: 2033 Redux {#Metro:_2033_Redux}

#### No sound {#No_sound_4}

Install [pulseaudio-alsa](https://archlinux.org/packages/?name=pulseaudio-alsa).

#### No image {#No_image}

Try setting `r_fullscreen off` in `~/.local/share/Steam/steamapps/common/Metro 2033 Redux/user.cfg`.

### Middle-earth: Shadow of Mordor {#Middle-earth:_Shadow_of_Mordor}

#### Floating heads {#Floating_heads}

Run the game with `__GL_ShaderPortabilityWarnings=0`.

### Mount & Blade: Warband {#Mount_&_Blade:_Warband}

#### Segmentation fault (core dumped) with Wayland {#Segmentation_fault_(core_dumped)_with_Wayland}

Use [Xorg](../../en/Xorg.html "Xorg") instead, or force the session to use `xcb` as `QT_QPA_PLATFORM`.

#### DLC chooser {#DLC_chooser}

Requires building [qt5-tools](https://archlinux.org/packages/?name=qt5-tools).

#### Crash on startup {#Crash_on_startup}

Set launch options to:

    LD_LIBRARY_PATH="." %command%

### Move or Die {#Move_or_Die}

#### No Sound {#No_Sound_5}

Install [lib32-libpulse](https://archlinux.org/packages/?name=lib32-libpulse). Remove file \"Move or Die/Love/linux32/libogg.so.0\"

### Multiwinia {#Multiwinia}

Requires [lib32-openal](https://aur.archlinux.org/packages/lib32-openal/)^AUR^.

#### Crash on startup {#Crash_on_startup_2}

If Multiwinia crashes on startup on X64 systems, force launching the 32-bit executable by replacing *`GAME`*`/run_steam.sh` with the following script:

    #!/bin/sh
    ./multiwinia.bin.x86

See [\[20\]](https://steamcommunity.com/app/1530/discussions/0/864969481950542663/#c558746995160431396).

### Natural Selection 2 {#Natural_Selection_2}

[sndio](https://archlinux.org/packages/?name=sndio) is required, furthermore, you must also execute

    $ ln -s /usr/lib/libsndio.so x64/libsndio.so.6.1

within the root of the NS2 directory. This is because NS2 uses an older outdated version of sndio, but it is still compatible with the new version, thankfully.

For a more minimal solution, one can attempt to set the audio driver used through the environment variable `SDL_AUDIODRIVER`. For example, `SDL_AUDIODRIVER=sndio` or `SDL_AUDIODRIVER=alsa`.

The environment variable `SDL_VIDEODRIVER` must not be set to `wayland`. Try setting `SDL_VIDEODRIVER` to `x11` if it still does not work.

### No Man\'s Sky {#No_Man's_Sky}

#### Black screen at start {#Black_screen_at_start}

Edit `~/Steam/SteamApps/common/No Man's Sky/Binaries/SETTINGS/TKGRAPHICSSETTINGS.MXML` and set `FullScreen` to `false` and `Borderless` to `true`.

#### White screen at start {#White_screen_at_start}

If you get a white screen, it may seem like the game has froze, but it has not. Hold down `e` to continue.

### Nuclear Throne {#Nuclear_Throne}

Refer to [#Missing libcurl.so.4 or version CURL_OPENSSL_3 not found](#Missing_libcurl.so.4_or_version_CURL_OPENSSL_3_not_found).

### OneShot {#OneShot}

#### Game fails to start {#Game_fails_to_start}

This problem occurs because the game use outdated libraries. Go to the game directory and remove `libdrm.so.2`, `libGLdispatch.so.0`, `libstdc++.so.6`, `librt.so.1`, `libcrypt.so.1` and `libcrypto.so.1.1`. Those files usually have an equivalent already installed on the system.

#### File \_\_\_\_\_\_\_ will not run {#File_will_not_run}

The executable \_\_\_\_\_\_\_ may fail when run from the Documents directory. It also exists in the game directory and will run from there.

#### Game fails to start on Wayland {#Game_fails_to_start_on_Wayland}

Run the game with `GDK_BACKEND=x11`.

### Oxygen Not Included {#Oxygen_Not_Included}

#### World generation hangs {#World_generation_hangs}

This problem occurs with locales that use comas instead of dots to separate decimals.

Set launch options in steam to `LANG=C.UTF-8 %command%`.[\[21\]](https://steamcommunity.com/app/457140/discussions/3/1488866180617243731/#c1488866813753688864)

#### Graphics errors, corruption and lines through tiles {#Graphics_errors,_corruption_and_lines_through_tiles}

This is a result of using the [Zink](../../en/OpenGL.html#OpenGL_over_Vulkan_(Zink) "OpenGL") MESA driver. If you have this globally enabled, disable it specifically for this game and launch it normally.

### Pandora: First Contact {#Pandora:_First_Contact}

#### Launch issue {#Launch_issue}

If the game refuses to launch at start you will need to replace bundled libraries by those from the main system.

Replace the bundled files in the game binaries directory with symlinks to `libcurl.so.4.8.0`, `libcurl.so.4`, `libglfw.so.3.4` and `libglfw.so.3` from `/usr/lib/` to allow the game to launch as normal.

**Note** Some systems will not have [glfw](https://archlinux.org/packages/?name=glfw) pre-installed: you will need to [install](../../en/Help:Reading.html#Installation_of_packages "Install") it, then the files will be available in `/usr/lib/`.

### Patrick\'s Parabox {#Patrick's_Parabox}

#### Blank Screen {#Blank_Screen}

Add the following to Steam launch options:

    LD_PRELOAD=Patrick\'s\ Parabox_Data/Plugins/libfmodstudio.so %command%

### Penumbra: Overture {#Penumbra:_Overture}

Dependencies:

-   [lib32-glu](https://archlinux.org/packages/?name=lib32-glu)
-   [lib32-libvorbis](https://archlinux.org/packages/?name=lib32-libvorbis)
-   [lib32-libxft](https://archlinux.org/packages/?name=lib32-libxft)
-   [lib32-openal](https://aur.archlinux.org/packages/lib32-openal/)^AUR^
-   [lib32-sdl_image](https://aur.archlinux.org/packages/lib32-sdl_image/)^AUR^
-   [lib32-sdl_ttf](https://aur.archlinux.org/packages/lib32-sdl_ttf/)^AUR^

#### Windowed mode {#Windowed_mode_2}

There is no in-game option to change to the windowed mode, you will have to edit `~/.frictionalgames/Penumbra/Overture/settings.cfg` to activate it.

Find `FullScreen="true"` and change it to `FullScreen="false"`, after this the game should start in windowed mode.

### Portal 2 {#Portal_2}

#### Game does not start {#Game_does_not_start_11}

Several OpenGL-related errors (such as `PROBLEM: You appear to have OpenGL 1.4.0, but we need at least 2.0.0!` or `libGL error: driver pointer missing`) are caused by Portal 2 bundling an old libstdc++ file. This error is especially common with open source Radeon drivers (`radeonsi`).

A problem with libstdc can be fixed by running the game with `LD_PRELOAD='/usr/$LIB/libstdc++.so.6'`.

#### Resolution too low {#Resolution_too_low}

When the game starts with a resolution so low that you cannot reach the game settings, run the game in windowed mode using the `-windowed` flag.

#### Missing non Latin font {#Missing_non_Latin_font}

The phenomenon is no menu in Portal. Portal and Portal2 use Helvetica, add the following lines to `~/.config/fontconfig/fonts.conf`:

    <match target="pattern">
        <test qual="any" name="family">
            <string>Helvetica</string>
        </test>
        <edit name="family" mode="assign" binding="same">
            <string>Source Han Sans CN</string>
        </edit>
    </match>

You can replace \"Source Han Sans CN\" by your favoriate and existing font.

### Prison Architect {#Prison_Architect}

#### ALSA error when using PulseAudio or PipeWire {#ALSA_error_when_using_PulseAudio_or_PipeWire}

The error:

    ALSA lib pcm_dmix.c:1018:(snd_pcm_dmix_open) unable to open slave

was resolved by installing:

-   [pulseaudio-alsa](https://archlinux.org/packages/?name=pulseaudio-alsa)
-   [lib32-libpulse](https://archlinux.org/packages/?name=lib32-libpulse)
-   [pipewire-alsa](https://archlinux.org/packages/?name=pipewire-alsa)

per [PulseAudio#ALSA](../../en/PulseAudio.html#ALSA "PulseAudio").

Alternatively, if running the game through Steam, you can force the game to be ran through proton, and that can resolve other audio errors.

You can do this by opening the game\'s properties through steam, and under \"general\" tick the \"Force the use of a specific Steam Play comparability tool\", and then select a proton version from the dropdown below

#### Game only starting in safe mode {#Game_only_starting_in_safe_mode}

If the game does not start, but Steam thinks it is running, probably the Paradox launcher has problems running properly. If this is the case, you will find some processes running in background:

`$ ps -ef | grep paradoxlauncher`

Kill them all, then modify the game startup options as follows:

    LD_PRELOAD=/usr/lib64/libc.so %command%

Eventually, if the above option has not worked, an option to skip it:

    ./PrisonArchitect %command%

Note: even if we are using another executable to start the game, `%command%` has to be added at the end of the command to trick Steam.

### Project Zomboid {#Project_Zomboid}

#### No sound {#No_sound_6}

Prepend `/usr/lib` to `LD_LIBRARY_PATH`.

In the game, go to the options and set all audio to the proper volume.

### Redshirt {#Redshirt}

Requires [lib32-libpulse](https://archlinux.org/packages/?name=lib32-libpulse) if you use PulseAudio.

### Revenge of the Titans {#Revenge_of_the_Titans}

Requires [libxtst](https://archlinux.org/packages/?name=libxtst) and [lib32-libxtst](https://archlinux.org/packages/?name=lib32-libxtst).

### Rise of the Tomb Raider {#Rise_of_the_Tomb_Raider}

Run in an X session.

#### Game does not start {#Game_does_not_start_12}

If running in X session is not available or is not preferred, another alternative is to create the script:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/usr/local/bin/pulseaudio
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh
exit 0
```

and make it [executable](../../en/Help:Reading.html#Make_executable "Executable").

After this the game was found to have loaded on Linux according to some game testers.

### Risk of Rain {#Risk_of_Rain}

Refer to [#Missing libcurl.so.4 or version CURL_OPENSSL_3 not found](#Missing_libcurl.so.4_or_version_CURL_OPENSSL_3_not_found).

### Rock Boshers DX: Directors Cut {#Rock_Boshers_DX:_Directors_Cut}

Requires [lib32-libcaca](https://aur.archlinux.org/packages/lib32-libcaca/)^AUR^.

### Saints Row: The Third {#Saints_Row:_The_Third}

#### Impossible to save custom display settings {#Impossible_to_save_custom_display_settings}

Although game settings menu allows to choose custom display settings, the game may have problems saving them.

In such case, adjust these settings manually in the game\'s configuration file `~/.local/share/Steam/steamapps/common/Saints Row the Third/display.ini`.

The comments in this file explain well all the settings and acceptable values.

#### Incorrect screen resolution in game {#Incorrect_screen_resolution_in_game}

This can occur when game is launched in a multi-head environment, with some monitors rotated, etc., so the game detects available screen resolutions incorrectly.

In such case, adjust `ResolutionWidth` and `ResolutionHeight` options in the `display.ini` file. Also, one must set option `VerifyResolution = false`.

### Saints Row IV {#Saints_Row_IV}

#### Game fails to launch after update to new NVIDIA drivers {#Game_fails_to_launch_after_update_to_new_NVIDIA_drivers}

**The factual accuracy of this article or section is disputed.**

**Reason:** General settings not specific to this game (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

Run the game with `/usr/lib32/libGLX_nvidia.so` appended to the `LD_PRELOAD`.

#### Game causes GPU lockup with mesa drivers {#Game_causes_GPU_lockup_with_mesa_drivers}

Saints Rows IV can cause a GPU lockup when trying to play on certain AMD hardware using open source drivers: [Bug 93475](https://bugs.freedesktop.org/show_bug.cgi?id=93475).

A workaround is to run the game with `R600_DEBUG=nosb`.

### Serious Sam 3: BFE {#Serious_Sam_3:_BFE}

#### No audio {#No_audio_2}

Try running:

    # mkdir -p /usr/lib/i386-linux-gnu/alsa-lib/
    # ln -s /usr/lib32/alsa-lib/libasound_module_pcm_pulse.so /usr/lib/i386-linux-gnu/alsa-lib/

If that does not work, try tweaking `~/.alsoftrc` as proposed by the [Steam community](https://steamcommunity.com/app/221410/discussions/3/846940248238406974/) (Serious Sam 3: BFE uses OpenAL to output sound). If you are not using PulseAudio, you may want to write the following configuration:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.alsoftrc
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[general]
drivers = alsa
[alsa]
device = default
capture = default
mmap = true
```

### SJ-19 Learns to Love {#SJ-19_Learns_to_Love}

If the game crashes at startup with this error in Steam\'s output:

    /home/username/.local/share/Steam/steamapps/common/SJ-19 Learns To Love/sj-19-linux/sj-19-learns-to-love.x86_64: error while loading shared libraries: libsteam_api.so: cannot open shared object file: No such file or directory

Right click the game in steam, select Properties, and set this in Launch Options:

    LD_LIBRARY_PATH=./sj-19-linux %command%

### Slay the Spire {#Slay_the_Spire}

If the game does not start or crashes at startup, install [xorg-xrandr](https://archlinux.org/packages/?name=xorg-xrandr).

If the game crashes with the xrandr stacktrace:

    Caused by: java.lang.ArrayIndexOutOfBoundsException: 0
    at org.lwjgl.opengl.XRandR.findPrimary(XRandR.java:326)
    at org.lwjgl.opengl.XRandR.ScreentoDisplayMode(XRandR.java:315)

It is likely due to a [known bug in LWJGL](https://github.com/LWJGL/lwjgl/issues/112#issuecomment-291598776). The workaround is to change the xrandr configuration to only contain the resolution (For example: `2560x1440_60.00` should become `2560x1440`.

If the game does not move sink input, you can edit the following file to allow sink moves:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.alsoftrc
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[pulse]
allow-moves=yes
```

### Stick Fight: The Game {#Stick_Fight:_The_Game}

If the game does not launch, try appending `PROTON_USE_WINED3D=1 %command%` to force using WINE direct3D. To do this you must have [wine](https://archlinux.org/packages/?name=wine) installed.

### Songbringer {#Songbringer}

#### Launch error with Wayland {#Launch_error_with_Wayland}

Install [glfw](https://archlinux.org/packages/?name=glfw) and run the game with `LD_PRELOAD=/usr/lib/libglfw.so.3`.

### Space Pirates and Zombies {#Space_Pirates_and_Zombies}

Requires [lib32-openal](https://aur.archlinux.org/packages/lib32-openal/)^AUR^.

#### No audio {#No_audio_3}

Try running:

    # mkdir -p /usr/lib/i386-linux-gnu/alsa-lib/
    # ln -s /usr/lib32/alsa-lib/libasound_module_pcm_pulse.so /usr/lib/i386-linux-gnu/alsa-lib/

If that does not work, try tweaking `~/.alsoftrc` as proposed by the Steam community (Serious Sam 3: BFE uses OpenAL to output sound). If you are not using PulseAudio, you may want to write the following configuration:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.alsoftrc
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[general]
drivers = alsa
[alsa]
device = default
capture = default
mmap = true
```

### Spacechem {#Spacechem}

Dependencies:

-   [lib32-sdl_mixer](https://aur.archlinux.org/packages/lib32-sdl_mixer/)^AUR^
-   [lib32-sdl_image](https://aur.archlinux.org/packages/lib32-sdl_image/)^AUR^
-   [lib32-sqlite](https://archlinux.org/packages/?name=lib32-sqlite)

#### Game crash {#Game_crash}

The shipped x86 version of Spacechem does not work on x64 with the game\'s own libSDL\* files, and crashes with some strange output.

To solve this just remove the three files `libSDL-1.2.so.0`, `libSDL_image-1.2.so.0`, `libSDL_mixer-1.2.so.0` from the game directory.

### Splice {#Splice}

Requires [glu](https://archlinux.org/packages/?name=glu).

### The Stanley Parable {#The_Stanley_Parable}

#### Game will not start {#Game_will_not_start}

As discussed in the Steam store page, remove `bin/libstdc++.so.6` from the game directory.

### Shadow Tactics: Blades of the Shogun {#Shadow_Tactics:_Blades_of_the_Shogun}

Dependencies:

-   [lib32-libstdc++5](https://aur.archlinux.org/packages/lib32-libstdc%2B%2B5/)^AUR^
-   [lib32-libxcursor](https://archlinux.org/packages/?name=lib32-libxcursor)
-   [lib32-libxrandr](https://archlinux.org/packages/?name=lib32-libxrandr)

### Stardew Valley {#Stardew_Valley}

#### Unable to move or input text {#Unable_to_move_or_input_text}

When in game, you are stuck in your bed as you cannot move your character or you cannot enter text into the input fields when starting a new game. This is a bug with the SDL2 lib bundled with the game.

Install [sdl2](https://aur.archlinux.org/packages/sdl2/)^AUR^.

Modify this config line:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.steam/steam/steamapps/common/Stardew\ Valley/MonoGame.Framework.dll.config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
<dllmap dll="SDL2.dll" os="linux" cpu="x86-64" target="./lib64/libSDL2-2.0.so.0"/>
```

To this (the period is removed at the beginning of target):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.steam/steam/steamapps/common/Stardew\ Valley/MonoGame.Framework.dll.config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
<dllmap dll="SDL2.dll" os="linux" cpu="x86-64" target="/lib64/libSDL2-2.0.so.0"/>
```

### Steel Storm: Burning Retribution {#Steel_Storm:_Burning_Retribution}

#### Start with black screen {#Start_with_black_screen}

The game by default tries to launch in fullscreen mode with a resolution of 1024x768, which does not work on some devices (for example the Samsung Series9 laptop with Intel hd4000 video).

Run the game in windowed mode by using the `-window` flag. Then change the resolution in-game.

### Stellaris {#Stellaris}

#### No window opening, only sound {#No_window_opening,_only_sound}

Happens with some AMD GPU and mesa combination, set `multi_sampling=0` in `~/.local/share/Paradox Interactive/Stellaris/settings.txt`.

On some window managers (e.g. Xmonad) you should set `fullScreen=no`.

#### Immediate crash to desktop {#Immediate_crash_to_desktop}

##### Steam using Proton instead of Linux Runtime {#Steam_using_Proton_instead_of_Linux_Runtime}

To diagnose, run Steam in a terminal and launch Stellaris. Ignore any errors mentioning \"LD_PRELOAD\" and look for this error:

    /home/username/.local/share/Steam/steamapps/common/Stellaris/dowser.exe: /home/username/.local/share/Steam/steamapps/common/Stellaris/dowser.exe: cannot execute binary file

If you see that error then the solution is to force Steam to use the Linux runtime for Stellaris:

1.  Right-click on Stellaris and select \"Properties\...\"
2.  Select the \"Compatibility\" tab.
3.  Select \"Force the use of a specific Steam Play compatibility tool\".
4.  Select \"Steam Linux Runtime 1.0 (scout)\"

##### Missing libnss_sss.so.2 {#Missing_libnss_sss.so.2}

It seems that Stellaris requires a 32bit libnss_sss.so.2 to operate. You can confirm if this is your problem by running

    $ strace ~/.local/share/Steam/steamapps/common/Stellaris/stellaris 2>&1 | grep sss

and seeing if you get output like

    openat(AT_FDCWD, "/usr/lib32/tls/i686/sse2/libnss_sss.so.2", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = -1 ENOENT (No such file or directory)

If this is indeed your problem, download the libnss-sss package from Ubuntu\'s repository [\[22\]](https://packages.ubuntu.com/bionic/i386/libnss-sss/download), extract the libnss_sss.so.2 from the downloaded package, and place it at \~/.local/share/Steam/steamapps/common/Stellaris. The game should now load properly.

#### Game instantly crashes to desktop on Wayland {#Game_instantly_crashes_to_desktop_on_Wayland}

Append `SDL_VIDEODRIVER=x11` to your launch options.

#### Launcher is blank {#Launcher_is_blank}

This is a recurring problem on Linux following the Machine Age expansion. If this happens to you, back up all your custom empires and savegames (found in `$XDG_DATA_HOME/Paradox Interactive/Stellaris/` and `$XDG_DATA_HOME/Steam/userdata/`*`your_user_ID`*`/281990/remote/` for cloud saves). If you have no other Paradox games installed, then remove the Paradox Interactive directory underneath `$XDG_DATA_HOME/`.

If you have other Paradox games installed, then do not remove the entire Paradox directory. Just remove the Stellaris directory and the launcher-v2 directory.

Attempt to run the game again. The launcher should open normally after re-downloading. Once the game launches properly, close the game and put your empires and savegames back in their directories from where you got them.

### Stephen\'s Sausage Roll {#Stephen's_Sausage_Roll}

#### No sound {#No_sound_7}

If using [native libraries](../../en/Steam/Troubleshooting.html#Steam_native_runtime "Steam/Troubleshooting") and [libpulse](https://archlinux.org/packages/?name=libpulse) is installed, Unity may try to use that library for sound and fail. To test if this is the problem, try removing [libpulse](https://archlinux.org/packages/?name=libpulse) or renaming the package files that are named `libpulse-simple*`. To see which [libpulse](https://archlinux.org/packages/?name=libpulse) files are relevant, run:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ pacman -Qql libpulse | grep /usr/lib/libpulse-simple
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/usr/lib/libpulse-simple.so
/usr/lib/libpulse-simple.so.0
/usr/lib/libpulse-simple.so.0.1.0
```

If renaming any of those files works for you, you can proceed with the following instructions (revert any renaming you just did). Browse to the game\'s directory:

    $ cd "$HOME/.steam/root/steamapps/common/Stephen's Sausage Roll"

And create a sub-directory that we can use to hold 0-byte look-alike library files:

    $ mkdir noload/

Use `touch` to create 0-byte versions of the above files that we want the dynamic linker to skip, e.g.:

    $ touch noload/{libpulse-simple.so,libpulse-simple.so.0,libpulse-simple.so.0.1.0}

**Note** Only a 0-byte `libpulse-simple.so.0` file may be required.

After you have created these 0-byte files, you can now attempt to run the game binary directly, telling the dynamic linker to use our 0-byte files:

    $ LD_LIBRARY_PATH="noload/:$LD_LIBRARY_PATH" ./Sausage.x86_64

If everything works up to this point, prepend `noload/` to your `LD_LIBRARY_PATH`.

Again, this should work because Steam checks for a `noload/` directory relative to the game\'s directory. The dynamic linker should respect the `$LD_LIBRARY_PATH` variable and fail to load the necessary [libpulse](https://archlinux.org/packages/?name=libpulse) files. The game should then fallback to plain ALSA.

### Superbrothers: Sword & Sworcery EP {#Superbrothers:_Sword_&_Sworcery_EP}

Dependencies:

-   [lib32-glu](https://archlinux.org/packages/?name=lib32-glu)
-   [lib32-libpulse](https://archlinux.org/packages/?name=lib32-libpulse) if you use PulseAudio

The game bundles an outdated version of libstdc++ which prevents the game from starting. [\[23\]](https://steamcommunity.com/app/204060/discussions/0/364039785161291413) The following can be observed when you run Steam and S&S from the terminal:

    libGL error: unable to load driver: i965_dri.so
    libGL error: driver pointer missing
    libGL error: failed to load driver: i965
    libGL error: unable to load driver: i965_dri.so
    libGL error: driver pointer missing
    libGL error: failed to load driver: i965
    libGL error: unable to load driver: swrast_dri.so
    libGL error: failed to load driver: swrast

To solve this problem remove *`GAME`*`/lib/libstdc++.so.6*`. After that the game will use the libstdc++ from Steam.

### System Shock 2 {#System_Shock_2}

You get these errors when running it with the native client:

    C:\windows\system32\winedevice.exe: symbol lookup error: /usr/lib32/libX11.so.6: undefined symbol: xcb_wait_for_reply64
    C:\windows\system32\wineboot.exe: symbol lookup error: /usr/lib32/libX11.so.6: undefined symbol: xcb_wait_for_reply64

Just delete or rename the libxcb library it got shipped with:

    mv /mnt/olhdd/steam/steamapps/common/SS2/lib/libxcb.so.1{,.old}
    mv /mnt/olhdd/steam/steamapps/common/SS2/lib/libxcb.so.1.1.0{,.old}

#### Game does not launch {#Game_does_not_launch}

If you encounter the game not launching, do the following:

1.  Move `libsteam_api.so` from the `SS2/Bin` directory within the main Steam common directory and transfer it to the `SS2` main game directory, not the `SS2/Bin` subdirectory.
2.  Put `LD_PRELOAD='/usr/$LIB/libxcb.so.1' %command%` into the [launch options](../../en/Launch_option.html "Launch option").

Once all of these have been implemented, the game should work.

#### Resolution fix {#Resolution_fix}

You may encounter some resolution problems with this game on Steam not working properly in full screen mode. Do the following:

1.  Open `cam.cfg` in the `SS2` directory, you may have to search for it via the search mode while in the game directory.
2.  Place `game_screen_size 1024 768` or `game_screen_size 1920 1080` depending on your resolution and put `game_full_screen 1` into bottom of the `cam.cfg` file.
3.  Go to `cam_ext.cfg` and next to the display setting place a semicolon prefix next to the `use_d3d_display` option so it should be like this: `;use_d3d_display`

It should then properly not go off-screen and should stay full screen within the active main screen.

### Sven Co-op {#Sven_Co-op}

#### No sound in-game (FMOD ex error code 60) {#No_sound_in-game_(FMOD_ex_error_code_60)}

If using [PipeWire](../../en/PipeWire.html "PipeWire"), make sure you have installed [lib32-pipewire](https://archlinux.org/packages/?name=lib32-pipewire).

### Tabletop Simulator {#Tabletop_Simulator}

#### CJK characters not showing in game {#CJK_characters_not_showing_in_game}

Install [wqy-microhei](https://archlinux.org/packages/?name=wqy-microhei) and [wqy-microhei-lite](https://archlinux.org/packages/?name=wqy-microhei-lite).

### Team Fortress 2 {#Team_Fortress_2}

As of an update in September 2023, the game will not have the correct version of `tcmalloc` and will silently crash during launch.

Follow the fix outlined in [#tcmalloc.cc error in Source 1 games](#tcmalloc.cc_error_in_Source_1_games)

#### HRTF setup {#HRTF_setup}

Assuming HRTF (head-related transfer function) has been properly set up in the operating system, HRTF will not be enabled unless you disable the original processing. To do so, add this to your autoexec

    dsp_slow_cpu 1

For best results, also change the following:

    snd_spatialize_roundrobin 1
    dsp_enhance_stereo 0
    snd_pitchquality 1

#### Loading screen freeze {#Loading_screen_freeze}

If you are a non-English (speaking) user, you have to enable \"en_US.UTF-8\" in the locale.gen! Generate a new locale after that.

#### No audio {#No_audio_4}

It happens if there is no PulseAudio in your system. If you want to use [ALSA](../../en/Advanced_Linux_Sound_Architecture.html "ALSA"), you need to launch Steam or the game directly with `SDL_AUDIODRIVER=alsa` (From [SteamCommunity](https://steamcommunity.com/app/221410/discussions/0/882966056462819091/#c882966056470753683)).

If it still does not work, you may also need to set the environment variable AUDIODEV. For instance `AUDIODEV=Live`. Use `aplay -l` to list the available sound cards.

#### Slow loading textures {#Slow_loading_textures}

If you are using Chris\' FPS Configs or any other FPS config, you may have set `mat_picmip` to `2`. This spawns multiple threads for texture loading, which may cause more jittering and lag on Linux, especially on alternative kernels. Try setting it to `-1`, the default.

#### \"Invalid color format\" Error at loading screen on integrated Intel Atom/BayTrail HD Graphics {#\"Invalid_color_format\"_Error_at_loading_screen_on_integrated_Intel_Atom/BayTrail_HD_Graphics}

Add the following to the game startup options:

    -force_vendor_id 0x10DE -force_device_id 0x1180

These options deceive the game engine that we are having a NVIDIA GPU, not Intel/AMD.

#### Wrong mouse sensitivity {#Wrong_mouse_sensitivity}

TF2 ships with an old version of libSDL2.so. Following [mastercomfig](https://docs.mastercomfig.com/page/os/linux/#native-libraries)\'s guide helps using the Steam Runtime instead of using the bundled libSDL2 version and updates the Steam Runtime by using the Distribution shipped version.

### Terraria {#Terraria}

See the KNOWN ISSUES & WORKAROUNDS​ section of the [release announcement](https://forums.terraria.org/index.php?threads/terraria-1-3-0-8-can-mac-linux-come-out-play.30287/).

#### Input Issues {#Input_Issues}

The symptoms of this problem are: When moving after standing still, your character seems to vary their speed, if wearing running boots they do not activate. When jumping with an item for double jumping sometimes you double jump even if you just jumped once. Going up/down ropes seems slow/choppy.

The solution is to preload the system SDL2 libraries: `LD_PRELOAD='/usr/$LIB/libSDL2-2.0.so:/usr/lib32/libSDL2-2.0.so'` For more information: [Terraria Forums](https://forums.terraria.org/index.php?threads/keyboard-input-bug-involving-linux.56763/page-2#post-1533051)^\[[dead\ link](https://en.wikipedia.org/wiki/Wikipedia:Link_rot "wikipedia:Wikipedia:Link rot")\ 2021-05-17---HTTP 403\]^

### This War of Mine {#This_War_of_Mine}

#### Game does not start {#Game_does_not_start_13}

This happens because of an incompatibility with the newer version of `lib32-curl`. To fix the problem, set your [launch options](../../en/Launch_option.html "Launch option") to:

    LD_PRELOAD=./libcurl.so.4 %command%

#### Sound glitches with Steam native {#Sound_glitches_with_Steam_native}

The bundled `libOpenAL` might not work correctly, try symlinking `/usr/lib32/libopenal.so` to *`GAME`*`/libOpenAL.so`.

### Ticket to Ride {#Ticket_to_Ride}

**This article or section is out of date.**

**Reason:** [lib32-gstreamer0.10-base](https://aur.archlinux.org/packages/lib32-gstreamer0.10-base/)^AUR\[[broken\ link](../../en/Help:Procedures.html#Fix_broken_package_links "Help:Procedures"):\ package\ not\ found\]^ is [flagged for deletion](https://lists.archlinux.org/hyperkitty/list/aur-requests@lists.archlinux.org/message/JIP24NM32G52WITZO7C2BPFL7B7LDLWA/) and does not exist in the multilib-alucryd repository. (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

Dependencies:

-   [lib32-gstreamer0.10-base](https://aur.archlinux.org/packages/lib32-gstreamer0.10-base/)^AUR\[[broken\ link](../../en/Help:Procedures.html#Fix_broken_package_links "Help:Procedures"):\ package\ not\ found\]^
-   [lib32-pangox-compat](https://aur.archlinux.org/packages/lib32-pangox-compat/)^AUR^

As lib32-gstreamer0.10-base is quite hard to build you can use [multilib-alucryd](../../en/Unofficial_user_repositories.html#alucryd "Unofficial user repositories") repo for this package

### The Tiny Bang Story {#The_Tiny_Bang_Story}

#### Missing libGLEW.so.1.6 {#Missing_libGLEW.so.1.6}

    # ln -s /usr/lib32/libGLEW.so.1.10.0 /usr/lib32/libGLEW.so.1.6

### Tomb Raider (2013) {#Tomb_Raider_(2013)}

#### Game immediately closes {#Game_immediately_closes}

Tomb Raider has a very heavy amount of dependency on the Steam runtime, the easiest solution is to just run it using the runtime.

If this does not solve the problem, look up the shared library dependencys of the main executable. Go into your steam directory and do

    $ ldd steamapps/common/Tomb\ Raider/bin/TombRaider | grep found

Note all missing librarys and try installing them from the standard repositories and the AUR. If after that you are still missing librarys you can search on the web for them and download corresponding packaged *.rpm* x86 (32bit) files and extract them into `steamapps/common/Tomb\ Raider/lib/i686/` to provide the missing librarys. Run *ldd* again and see whether you have all the necessary librarys installed. If there are no more missing librarys and the added librarys are of the correct version, architecture and 32/64bit word length and are placed on one of the linkers search paths then the game should work.

Another alternative to this is to do the following in the Launch options:

    LD_LIBRARY_PATH="$HOME/.local/share/Steam/steamapps/common/Tomb Raider/lib/i686:$LD_LIBRARY_PATH" %command%

#### Steam Controller not working in-game {#Steam_Controller_not_working_in-game}

If your Steam Controller is correctly recognized and paired but still not working in-game try the following:

-   In Steam, non Big Screen, go to *Settings \> Account \> Beta participation \> Change\...* and in the dropdown select box select Steam Beta Update
-   Restart Steam
-   Go to Big Screen and start Tomb Raider

Correctly recognized means you can control the desktop mouse and Steam in Big Picture mode and the controller is shown in the Big Picture settings.

#### Failed to Initialize Direct3D {#Failed_to_Initialize_Direct3D}

This can happen when switching monitors.

You need to manually edit the preferences file (found in \~/.local/share/feral-interactive/Tomb Raider/) and change the ExclusiveFullscreen option to 0. After this you should be able to successfully start the game (after which you may exit and revert that option to a 1 to restore fullscreen).

#### Stuck at the start menu {#Stuck_at_the_start_menu}

Tomb Raider for Linux will not start if there are any active VPNs that use TUN devices. This is because it makes incorrect assumptions about the return value of `getifaddrs()`. The only reason it calls `getifaddrs()` is to get the MAC address for a Version 1 UUID, and fall back to a different algorithm if `getifaddrs()` returns no interfaces at all.

One optional solution for such a situation is listed down below, which fixes assumptions made by Tomb Raiders about the output of `getifaddrs()` (see [tomb_raider_vpn_fix/releases](https://github.com/PinkPandaKatie/tomb_raider_vpn_fix/releases) for the original code):

    #include <stdio.h>
    #include <errno.h>
    #include <ifaddrs.h>

    int getifaddrs(struct ifaddrs **ifap) {
       fprintf(stderr, "\n\n\n---------------- dummied out getifaddrs()!\n\n\n");
       *ifap = NULL;
       return 0;
    }

    void freeifaddrs(struct ifaddrs *ifap) {
       /* do nothing */
    }

Compile it using

    $ gcc -m32 -fPIC -shared file_name.c -o file_name.so -ldl -Wall

Then use the following launch option:

    env LD_PRELOAD=$LD_PRELOAD:path/to/file_name.so %command%

### Torchlight 2 {#Torchlight_2}

#### Libfreetype/libfontconfig Incompatibility {#Libfreetype/libfontconfig_Incompatibility}

If you are experiencing issues with launching games such as Torchlight 2 or Civilization IV, it could be due to using a newer libfontconfig than the game currently supports.

Right click the game in Steam, and set the following as its launch option:

    LD_PRELOAD=/usr/lib/libfreetype.so.6 %command%

then attempt launching the game.

Alternately, re-naming or deleting these 2 files will force it to use your system\'s libraries:

    Torchlight 2/game/lib/libfreetype.so.6
    Torchlight 2/game/lib64/libfreetype.so.6

#### Locale incompatibility {#Locale_incompatibility}

Some users report that Torchlight 2 does not work if you do not have en_US.UTF8 in your locale.

Double check you have generated the locale needed in [Steam Installation Requirements](../../en/Steam.html#Installation "Steam").

### Tower Unite {#Tower_Unite}

#### Graphical glitches {#Graphical_glitches}

This is a known issue, and it occurs because the shaders had not been ported to Linux yet by the developers. To minimize glitches and make the game playable add `-opengl4` to your [launch options](../../en/Launch_option.html "Launch option"), set Ocean Quality to \"Potato\" and Effects Quality to \"Low\" in the game settings.

### Towns / Towns Demo {#Towns_/_Towns_Demo}

Requires [Java](../../en/Java.html "Java").

### Transistor {#Transistor}

#### Crash on launch / FMOD binding crash / audio issues {#Crash_on_launch_/_FMOD_binding_crash_/_audio_issues}

Run the game with:

    LD_PRELOAD='/usr/lib/libstdc++.so.6:/usr/lib/libgcc_s.so.1:/usr/lib/libxcb.so.1:/usr/lib/libasound.so.2'

Otherwise, run the game via shell and set up proper audio device for FMOD, as discussed in [\[24\]](https://steamcommunity.com/app/237930/discussions/2/620695877176333955/).

Also, check out this thread [\[25\]](https://steamcommunity.com/app/237930/discussions/2/492378265893557247/).

#### Game does not start on Wayland {#Game_does_not_start_on_Wayland}

The game will not start with SDL set to use Wayland. You can have only the game run in X11 by adding the following launch options in Steam:

    SDL_VIDEODRIVER=x11 %command%

### Transmissions: Element 120 {#Transmissions:_Element_120}

Dependencies:

-   [lib32-libgcrypt15](https://aur.archlinux.org/packages/lib32-libgcrypt15/)^AUR^
-   [lib32-libpng12](https://aur.archlinux.org/packages/lib32-libpng12/)^AUR^

#### Troubleshooting {#Troubleshooting}

Make sure you have all libraries installed. Above the standard set required by Steam runtime, the game requires few additional ones. The typical error message that indicates that is

    AppFramework : Unable to load module vguimatsurface.so!

To find missing dependencies go into the game directory and run:

    LD_LIBRARY_PATH=bin ldd bin/vguimatsurface.so

Look for entries that say *not found*.

### Transport Fever 2 {#Transport_Fever_2}

#### Game will not launch {#Game_will_not_launch}

Rename or delete the following files in game directory (`~/.steam/steam/steamapps/common/Transport Fever 2`) as discussed in [\[26\]](https://steamcommunity.com/app/1066780/discussions/0/1740010344363244243/)

-   `libstdc++.so.6`
-   `libstdc++.so.6.0.25`

### Trine 2 {#Trine_2}

#### Sound {#Sound}

**The factual accuracy of this article or section is disputed.**

**Reason:** General settings not specific to this game (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

If sound plays choppy, try:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/openal/alsoft.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
drivers=pulse,alsa
frequency=48000
```

#### Resolution {#Resolution}

If the game resolution is wrong when using a dual monitor setup and you cannot see the whole window edit `~/.frozenbyte/Trine2/options.txt` and change the options `ForceFullscreenWidth` and `ForceFullscreenHeight` to the resolution of your monitor on which you want to play the game.

### Tropico 5 {#Tropico_5}

#### Blank screen with sound only on startup {#Blank_screen_with_sound_only_on_startup}

Run the game with `MESA_GL_VERSION_OVERRIDE=4.0 MESA_GLSL_VERSION_OVERRIDE=400`.

### Unbound: Worlds Apart {#Unbound:_Worlds_Apart}

If your controller does not work, try selecting the game in your inventory, click the gear icon on the right, then Properties, Controller, and select Disable Steam Input in the dropdown.

### Unity of Command {#Unity_of_Command}

Requires [lib32-pango](https://archlinux.org/packages/?name=lib32-pango).

#### Squares {#Squares}

If squares are shown instead of text, try removing *`GAME`*`/bin/libpangoft2-1.0.so.0`.

#### No audio {#No_audio_5}

If you get this error:

    ALSA lib dlmisc.c:254:(snd1_dlobj_cache_get) Cannot open shared library /usr/lib/i386-linux-gnu/alsa-lib/libasound_module_pcm_pulse.so

Try running:

    # mkdir -p /usr/lib/i386-linux-gnu/alsa-lib/
    # ln -s /usr/lib32/alsa-lib/libasound_module_pcm_pulse.so /usr/lib/i386-linux-gnu/alsa-lib/

### Unity3D {#Unity3D}

Games based on the Unity3D engine, like *War For The Overworld* or *Pixel Piracy* may need the package [lsb-release](https://archlinux.org/packages/?name=lsb-release) to understand that they run on Linux and work properly.

#### Locale settings {#Locale_settings}

Games made in C# often have a problem with some locales (e.g. Russian, German) because developers do not specify locale-agnostic number formatting. This can result in some game screens loading only partially, problems with online features or other bugs.

**The factual accuracy of this article or section is disputed.**

**Reason:** Would this not be fixed with only setting `LC_NUMERIC`? (Discuss in [Talk:Steam/Game-specific troubleshooting](../../en/Talk:Steam/Game-specific_troubleshooting.html))

To work around this, run the game with `LC_ALL=C.UTF-8`.

Affected games: *FORCED, Gone Home, Ichi, Nimble Quest, Syder Arcade*.

#### Unity 5 sound problems {#Unity_5_sound_problems}

The sound system in Unity 5 changed and to be able to play games created with it you must most likely install and run [PulseAudio](../../en/PulseAudio.html "PulseAudio").

Another solution is to disable the Steam runtime: in the launch options for the game, write this: `LD_LIBRARY_PATH="" %command%`

Another solution is to prevent Unity from trying to use PulseAudio using [pulsenomore](https://aur.archlinux.org/packages/pulsenomore/)^AUR^. Once it is installed, use the following as launch options :`/usr/bin/pulsenomore %command%`

Affected games: *Kerbal Space Program, SUPERHOT, ClusterTruck*

#### Game launching on wrong monitor in fullscreen mode {#Game_launching_on_wrong_monitor_in_fullscreen_mode_2}

Unity games that do not support monitor selection will most likely launch the game on a wrong monitor.

The problem is that Unity games write the default parameter `<pref name="UnitySelectMonitor" type="int">-1</pref>` to the game config file.

This will lead to the game launching on a non-primary monitor.

When changing to value into `<pref name="UnitySelectMonitor" type="int">`**`0`**`</pref>` for the according game, the game will start on the correct (primary) monitor.

A Unity game config file usually resides in `~/.config/unity3d/`*`CompanyName`*`/`*`ProductName`*`/prefs`.

Affected games: *Cities: Skylines, Tabletop Simulator, Assault Android Cactus, Wasteland 2, Tyranny, Beat Cop*.

Be aware that some games do not support setting that parameter, it will simply be ignored. This is the case for *Pillars of Eternity*, *Kentucky Route Zero*, *Sunless Sea*.

#### Chinese/Japanese/Korean display bug {#Chinese/Japanese/Korean_display_bug}

Install [wqy-microhei](https://archlinux.org/packages/?name=wqy-microhei) and [wqy-microhei-lite](https://archlinux.org/packages/?name=wqy-microhei-lite). Then

    $ fc-cache -fv

#### Game does not respond {#Game_does_not_respond}

Add the following line to your [launch options](../../en/Launch_option.html "Launch option") :

    SDL_DYNAMIC_API=/usr/lib/libSDL2-2.0.so %command%

#### No window opens on Wayland {#No_window_opens_on_Wayland}

See [Unity3D#No window opens: Desktop is 0 x 0 @ 0 Hz](../../en/Unity3D.html#No_window_opens:_Desktop_is_0_x_0_@_0_Hz "Unity3D").

### Unrest {#Unrest}

Requires [fluidsynth](https://archlinux.org/packages/?name=fluidsynth).

### Volgarr the Viking {#Volgarr_the_Viking}

Delete the `lib` directory in the game directory to get rid of the libGL errors.

### War Thunder {#War_Thunder}

#### No audio {#No_audio_6}

If there is no audio after launching the game, install [pulseaudio-alsa](https://archlinux.org/packages/?name=pulseaudio-alsa).

#### Blank screen {#Blank_screen_2}

If having a green or blank screen on startup, run the game with `MESA_GL_VERSION_OVERRIDE=4.1COMPAT`. [\[27\]](https://forum.warthunder.com/index.php?/topic/267809-linux-potential-workaround-for-mesa-drivers-black-screen/)^\[[dead\ link](https://en.wikipedia.org/wiki/Wikipedia:Link_rot "wikipedia:Wikipedia:Link rot")\ 2023-07-30---HTTP 404\]^ [\[28\]](http://forum.warthunder.com/index.php?search_term=0030709&app=core&module=search&do=search&fromMainBar=1&search_app=forums%3Aforum%3A920&sort_field=&sort_order=&search_in=posts)^\[[dead\ link](https://en.wikipedia.org/wiki/Wikipedia:Link_rot "wikipedia:Wikipedia:Link rot")\ 2020-04-03---HTTP 404\]^

#### Launcher fails to auto-close {#Launcher_fails_to_auto-close}

When running through Steam a startup option must be set or the War Thunder Launcher will not auto-close when the game exits. Doing so will prevent it from being reported as the running game on the Steam Community, and more importantly running up CPU and RAM usage in the background. Put `XMODIFIERS="" %command%` in the Launch Options/Parameters of War Thunder on Steam.

### Victor Vran {#Victor_Vran}

#### Launch failure {#Launch_failure}

The game might die on launch with the following (or similar) console print:

    Auto configuration failed
    4034673992:error:25066067:DSO support routines:DLFCN_LOAD:could not load the shared library:dso_dlfcn.c:185:filename(libssl_conf.so): libssl_conf.so: cannot open shared object file: No such file or directory

Add the following line to your [launch options](../../en/Launch_option.html "Launch option"):

    OPENSSL_CONF=/dev/null %command%

### Warhammer 40,000: Dawn of War II {#Warhammer_40,000:_Dawn_of_War_II}

Dependencies:

-   [alsa-lib](https://archlinux.org/packages/?name=alsa-lib)
-   [librtmp0](https://aur.archlinux.org/packages/librtmp0/)^AUR^

The start script does not point to the right direction of `libasound.so.2`.

To fix it open *`GAME`*`/DawnOfWar2.sh` and replace the following lines:

    HAS_LSB_RELEASE=$(command -v lsb_release)
    if [ -n "${HAS_LSB_RELEASE}" ] && [ "$(lsb_release -c | cut -f2)" = "trusty" ]; then
        LD_PRELOAD_ADDITIONS="/usr/lib/x86_64-linux-gnu/libasound.so.2:${LD_PRELOAD_ADDITIONS}"
    fi 

with:

    LD_PRELOAD_ADDITIONS="/usr/lib64/libasound.so.2:${LD_PRELOAD_ADDITIONS}"

### Wasteland 2 {#Wasteland_2}

If Wasteland 2 immediately exits when you try to launch it there may not be enough system file descriptors available. To increase the descriptor limit, edit `/etc/security/limits.conf` and add the line:

    * hard nofile 524288

Then reboot for the new limit to take effect, Wasteland 2 should now launch and this setting might also fix other games.

### We Were Here {#We_Were_Here}

#### Stuck on black screen or logo on launch {#Stuck_on_black_screen_or_logo_on_launch}

Add `-screen-fullscreen 0` to launch options. [\[29\]](https://steamcommunity.com/app/582500/discussions/1/1470840994974091613/)

### Worms W.M.D {#Worms_W.M.D}

The game includes a script with a minor workaround included in the `Run.sh` script, however this workaround alone does not usually work. The game seems to be trying to use libraries which depend on out-of date libraries. It also depends on [libcurl-gnutls](https://archlinux.org/packages/?name=libcurl-gnutls). It is unlikely the game will run on modern systems or be updated again by the developer.

As of today (Jan/2026) the steps below will not work, left as a reference. A newer solution exists in [the BBS](https://bbs.archlinux.org/viewtopic.php?id=307036) which is similar (simpler).

Add a script called myrun.sh to the game directory (\~/.local/share/Steam/steamapps/common/WormsWMD on a standard steam install). Remember to make it executable (chmod +x)

Add the script to the game launch options in Steam

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
Launch options
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
./myrun.sh %command%
```

Run the game using the \"Play Worms W.M.D\" option.

The current working script is as follows

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
myrun.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/bash

_libraries=(
    lib/libQt5*.so.5
    /usr/lib/libwavpack.so.1
    "$STEAM_RUNTIME"/amd64/lib/x86_64-linux-gnu/libdbus-1.so.3
    "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libcurl-gnutls.so.4
    "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libidn.so.11
    "$STEAM_RUNTIME"/lib/x86_64-linux-gnu/libgcrypt.so.11
    "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/librtmp.so.0
)

export LD_PRELOAD="${_libraries[@]}"

exec "$@" > ~/worms-stdout.log 2> ~/worms-stderr.log
```

So, editing the script is needed. At the moment (2/2024) the following works on a system, however this may change at any time (edit `STEAM_RUNTIME` and `WORMSWMDINSTALLDIR` as required):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
Run.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/bash

export LOGFILE=${HOME}/wormswmd.log

export LC_ALL=C.UTF-8
export LD_LIBRARY_PATH="/usr/lib:/usr/local/lib"

export STEAM_ROOT=~/.steam
export PLATFORM=bin32
export STEAM_RUNTIME=$STEAM_ROOT/$PLATFORM/steam-runtime

export WORMSWMDINSTALLDIR=${HOME}/.steamapps/steamapps/common/WormsWMD

export LD_PRELOAD="$(
        printf "%s " "$WORMSWMDINSTALLDIR"/lib/libQt5*.so* \
                ${HOME}/.steam/steam/ubuntu12_32/steam-runtime/amd64/lib/x86_64-linux-gnu/libdbus-1.so.3 \
                ${HOME}/.steam/steam/ubuntu12_32/steam-runtime/amd64/lib/x86_64-linux-gnu/libdbus-1.so.3.5.8 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libcurl-gnutls.so.4 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libidn.so.11 \
                "$STEAM_RUNTIME"/lib/x86_64-linux-gnu/libgcrypt.so.11 \
                "$STEAM_RUNTIME"/lib/x86_64-linux-gnu/libwrap.so.0 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/librtmp.so.0 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libhogweed.so.4 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libnettle.so.6 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libsndfile.so.1 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libFLAC.so.8 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libpulse.so.0 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libjson.so.0 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libpulsecommon-1.1.so \
        lib/libicuuc.so.56
)"

chmod a+x ./Worms\ W.M.Dx64
./Worms\ W.M.Dx64 >> $LOGFILE
```

Now the game should run from Steam using the \"Play Worms W.M.D (Run.sh)\" option.

You may also try to run `Worms W.M.Dx64` directly but this is unlikely to work because of the reasons stated above, or run the script `Run.sh` from a terminal to see what libraries it is missing currently if the above script is not working for you.

If the game crashes after playing the intro movies, add the Steam Runtime dbus libraries to the game\'s library directory (but this is already covered by the `LD_PRELOAD` in the example `Run.sh`):

    $ ln -s ~/.steam/steam/ubuntu12_32/steam-runtime/amd64/lib/x86_64-linux-gnu/*dbus* ~/.steam/steam/steamapps/common/WormsWMD/lib

See also Steam community discussions [\[30\]](https://steamcommunity.com/app/327030/discussions/2/133257959065155871/), [\[31\]](https://steamcommunity.com/app/327030/discussions/1/343785380902286766/) and [\[32\]](https://steamcommunity.com/app/327030/discussions/0/4033601726325456210/).

Steam overlay does not seem to work at the moment, possibly the game is still looking for some incompatible libraries.

On some systems there are terrain bugs where holes in terrain are not rendered properly and worms can fall through terrain unexpectedly. These bugs can make the game unplayable in many situations and there is no known fix for them.

### Witcher 2: Assassin of Kings {#Witcher_2:_Assassin_of_Kings}

Dependencies:

-   [lib32-gnutls](https://archlinux.org/packages/?name=lib32-gnutls)
-   [lib32-libcurl-compat](https://archlinux.org/packages/?name=lib32-libcurl-compat)
-   [lib32-libcurl-gnutls](https://archlinux.org/packages/?name=lib32-libcurl-gnutls)
-   [lib32-sdl2_image](https://aur.archlinux.org/packages/lib32-sdl2_image/)^AUR^
-   [lib32-sdl2](https://aur.archlinux.org/packages/lib32-sdl2/)^AUR^

#### Game does not start {#Game_does_not_start_14}

The game will not start with SDL set to use wayland. You can have only the game run in x11 by adding the following launch options in steam:

    SDL_VIDEODRIVER=x11 %command%

If the game does not run, enable error messages:

    $ LIBGL_DEBUG=verbose ./witcher2

### Wizardry 6: Bane of the Cosmic Forge {#Wizardry_6:_Bane_of_the_Cosmic_Forge}

Requires [DOSBox](../../en/DOSBox.html "DOSBox").

To fix the crash at start, open *`GAME`*`/dosbox_linux/launch_wizardry6.sh` and:

1.  comment the line `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./libs`
2.  change the beginning of the line starting with `exec ./dosbox` to `exec dosbox`

### World of Goo {#World_of_Goo}

#### Changing resolution {#Changing_resolution}

To change the game resolution edit the *Graphics display* section in *`GAME`*`/properties/config.txt`. For example:

    <!-- Graphics display -->
    <param name="screen_width" value="1680" />
    <param name="screen_height" value="1050" />
    <param name="color_depth" value="0" />
    <param name="fullscreen" value="true" />
    <param name="ui_inset" value="10" />

### X3: Terran Conflict {#X3:_Terran_Conflict}

#### Game crashes on startup {#Game_crashes_on_startup_2}

The game may crash on startup because it is linked to libz version 1.2.9, while the latest version of this library in Arch Linux is higher. The following message in the terminals appears in this case:

    ./X3TC_config: lib/libz.so.1: version 'ZLIB_1.2.9' not found (required by /usr/lib32/libpng16.so.16

Renaming or removing lib/libz.so.1 may help.

### X Rebirth {#X_Rebirth}

#### Game crashes on startup {#Game_crashes_on_startup_3}

The game may crash on startup because it is linked to the shadergl function of the game. Do the follow in the `.../steamapps/common/X Rebirth/shadergl/shaders/common.fh` file.

    --- ./common.fh.orig
    +++ ./common.fh

    @@ -574 +574 @@
    -       /*      OUT_COLOR.rgb *= 0.0001; OUT_COLOR.rgb += half3(specstr);/**/   \
    +       /*      OUT_COLOR.rgb *= 0.0001; OUT_COLOR.rgb += half3(specstr);*/     \

    @@ -622 +622 @@
    -       /*      OUT_COLOR.rgb *= 0.0001; OUT_COLOR.rgb += LightColor.xyz/ 10;/**/       \
    +       /*      OUT_COLOR.rgb *= 0.0001; OUT_COLOR.rgb += LightColor.xyz/ 10;*/ \

After this workaround is implemented the game should load as normal.

### XCOM {#XCOM}

Dependencies:

-   [librtmp0](https://aur.archlinux.org/packages/librtmp0/)^AUR^
-   [sdl2_image](https://archlinux.org/packages/?name=sdl2_image) (required to enable keyboard functionality in-game)

#### Hangs on startup {#Hangs_on_startup}

If you are running a [hybrid graphics](../../en/Hybrid_graphics.html "Hybrid graphics") system, try:

    __GL_THREADED_OPTIMIZATIONS=0 primusrun %command%

#### Graphical glitches on Intel HD {#Graphical_glitches_on_Intel_HD}

XCOM: Enemy Unknown may not recognize the SDL2 shared libraries shipped with the Steam runtime. Check if the binary finds all required files and install missing packages if necessary ([sdl2](https://aur.archlinux.org/packages/sdl2/)^AUR^ and [sdl2_image](https://archlinux.org/packages/?name=sdl2_image)).

    ldd binaries/linux/game.x86_64 

### XCOM 2 {#XCOM_2}

#### Unable to start with steam native {#Unable_to_start_with_steam_native}

Needs `libgconf-2.so.4` which is not available in arch repositories, loading it from steams runtime seems to work.

    LD_PRELOAD="$HOME/.local/share/Steam/ubuntu12_32/steam-runtime/usr/lib/x86_64-linux-gnu/libgconf-2.so.4" %command%

#### Unable to start needs command line launch option {#Unable_to_start_needs_command_line_launch_option}

If having `libgconf-2.so.4` in the game directory but the game still does not work put the following in the launch options.

    LD_LIBRARY_PATH=./lib/x86_64/:../lib/x86_64/ %command% -allowconsole

If the above command on Steam does not work for you then its possible that this may work as an alternative.

    LD_LIBRARY_PATH=/usr/lib:$HOME/.local/share/Steam/ubuntu12_32/steam-runtime/amd64/lib/x86_64-linux-gnu/:$HOME/.steam/steam/steamapps/common/XCOM\ 2/lib/x86_64/ %command%

## Anti-cheat {#Anti-cheat}

Anti-cheat software is a common component of modern games. There are many anti-cheat implementations, most of which target Windows. Some may work without any further configuration. Consult [are we anti cheat yet](https://areweanticheatyet.com/) for a comprehensive and crowd-sourced list of games using anti-cheats and their compatibility with GNU/Linux or Wine/Proton.

### BattlEye {#BattlEye}

BattlEye is a cross platform anti-cheat software used by Grand Theft Auto: Online. Native runtime binaries can be installed directly from the Steam store.

**Note** BattlEye will degrade system performance unless [#Split lock detection / mitigation](#Split_lock_detection_/_mitigation) is disabled.
