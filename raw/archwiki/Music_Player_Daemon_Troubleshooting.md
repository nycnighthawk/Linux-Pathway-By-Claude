---
{"title": "Music Player Daemon/Troubleshooting", "url": "https://wiki.archlinux.org/title/Music_Player_Daemon/Troubleshooting", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Music Player Daemon/Troubleshooting

## Troubleshooting {#Troubleshooting}

### Autodetection failed {#Autodetection_failed}

During the start of MPD, it tries to auto detect your set-up and configure output and volume control accordingly. Though this mostly goes well, it will fail for some systems. It may help to tell MPD specifically what to use as output and mixer control. If you copied `/etc/mpd.conf` over from `/etc/mpd.conf.example` as mentioned above, you can simply uncomment:

Example for `alsa` output type and ALSA mixer:

    audio_output {
        type            "alsa"
        name            "My ALSA Device"
        device          "hw:0,0"    # optional
        format          "44100:16:2"    # optional
        mixer_type      "hardware"
        mixer_device        "default"
        mixer_control       "PCM"
    }

**Note** In case of permission problems when using ESD with MPD, run:

    # chsh -s /bin/true mpd

### MPD hangs on first startup {#MPD_hangs_on_first_startup}

This is a common error that\'s caused by corrupt mp3 tags. Here is an experimental way to solve this issue. Requirements:

-   kid3
-   easytag

This method is very tedious, especially with a huge database. Just as a baseline it took 2.5h to fix a 16GB database.

#### EasyTAG {#EasyTAG}

The purpose of [easytag](https://archlinux.org/packages/?name=easytag) here is that easytag detects the error in the tags, but like MPD it hangs and dies. The trick here is that easy tags actually tells you what file is causing the problem on the status bar. Before starting easytag make sure to have a terminal close to be ready to kill easy tag to avoid a hang. Once you are ready, on the tree view select the directory where all your music is located. By default easytag starts to search all subdirectories for mp3 files. Once you notice that easytag stopped scanning for songs, make note of the culprit and kill easytag.

**Note** This task can also be achieved by editing mpd\'s configuration file and setting \"log_level\" from \"default\" to \"verbose\". restart mpd and look up the last entry in mpd\'s log file after mpd hangs. It is recommended to set \"log_level\" back to \"default\" after debugging, since the log file grows fast.

#### Kid3 {#Kid3}

Here is where [kid3](https://archlinux.org/packages/?name=kid3) comes in handy. With kid3 go to the offending song and rewrite one of the tags. then save the file. This should force kid3 to rewrite the whole tag again fixing the problem with MPD and easy tag hanging.

Repeat this procedure until your music library is done.

### Cannot connect to mpd: host \"localhost\" not found: Temporary failure in name resolution {#Cannot_connect_to_mpd:_host_\"localhost\"_not_found:_Temporary_failure_in_name_resolution}

Cannot connect to MPD (with ncmpcpp), if you are disconnected from network. Solution is [disable IPv6](../../en/Disable_IPv6.html "Disable IPv6") or add line to /etc/hosts

    ::1 localhost.localdomain localhost

### Binding to IPV6 before IPV4 {#Binding_to_IPV6_before_IPV4}

If on startup, mpd displays the following message:

    listen: bind to '0.0.0.0:6600' failed: Address already in use (continuing anyway, because binding to '[::]:6600' succeeded)

it means mpd binds to the ipv6 interface before binding to ipv4. If you want to use your ipv4 interface, hardcode it in `mpd.conf`, like:

    bind_to_address "0.0.0.0"

Several binds can also be specified, for example, to have mpd listen both to localhost and to the external IP of your network card:

    bind_to_address "127.0.0.1"
    bind_to_address "192.168.1.13"

### daemon: cannot setgid for user \"mpd\": Operation not permitted {#daemon:_cannot_setgid_for_user_\"mpd\":_Operation_not_permitted}

The error is stating that the user starting the process does not have permissions to become another user (mpd) which the configuration has told the process to run as.

To solve the issue, simply [start](../../en/Help:Reading.html#Control_of_systemd_units "Start") `mpd.service` as the [root user](../../en/Root_user.html "Root user") instead of starting a [user unit](../../en/User_unit.html "User unit").

### daemon: fatal_error: Failed to set group NN: Operation not permitted {#daemon:_fatal_error:_Failed_to_set_group_NN:_Operation_not_permitted}

The error is stating that mpd cannot set the group. This is if you have set any other group in `/etc/mpd.conf` than the default: mpd. This is because of the default `mpd.service` file. It starts mpd as user mpd (and if no group specified with the default group of this user as stated in your `/etc/passwd`) and therefore mpd does not have any rights to change its group.

#### First fix {#First_fix}

In `/etc/mpd.conf` comment out the `group=` part or change it to `group=mpd`

#### Second fix {#Second_fix}

[Extend the unit](../../en/Extend_the_unit.html "Extend the unit") `mpd.service` and add your desired group. E.g. run mpd with the group \"audio\":

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/mpd.service.d/group.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
Group=audio
```

#### Third fix {#Third_fix}

Change the default group of the user mpd in your `/etc/passwd`.

### MPD & ALSA {#MPD_&_ALSA}

Sometimes, when using other audio outputs, e.g: some web pages containing Flash applets, MPD is rendered unable to play (until it is restarted). The error comes up in mpd\'s log:

    Error opening alsa device "hw:0,0": Device or resource busy

Reasons for this may be:

-   The sound card does not support hardware mixing (uses **dmix** plugin)
-   An application does not work with ALSA\'s default settings

For a detailed description, it is recommended to take a look at [this](https://mpd.wikia.com/wiki/Alsa) link.

This problem may be solved by adding the following lines to `mpd.conf`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
mpd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
audio_output {
        type                    "alsa"
        name                    "Sound Card"
        options                 "dev=dmixer"
        device                  "plug:dmix"
}
```

To make the changes have effect, [restart](../../en/Help:Reading.html#Control_of_systemd_units "Restart") `mpd.service`.

#### High CPU usage with ALSA {#High_CPU_usage_with_ALSA}

When using MPD with ALSA, users may experience MPD taking up lots of CPU (around 20-30%). This is caused by most sound cards supporting 48kHz and most music being 44.1kHz, thus forcing MPD to resample it. This operation takes lots of CPU cycles and results into high usage.

For most users the problem should be solved by telling MPD not to use resampling by adding `auto_resample "no"` into audio_output-part of `/etc/mpd.conf`.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
mpd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
audio_output {
   type         "alsa"
   name         "My ALSA Device"
   auto_resample    "no"
}
```

Although it may not give as drastic a speedup, enabling mmap may still speed things up:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
mpd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
audio_output {
   type         "alsa"
   name         "My ALSA Device"
   use_mmap     "yes"
}
```

Some users might also want to tell dmix to use 44kHz as well. More info about tuning performance of your MPD can be found on the [MPD wiki](https://mpd.wikia.com/wiki/Tuning)

#### Playing audio files with different rate (works for EMU 0202/0204/0404) {#Playing_audio_files_with_different_rate_(works_for_EMU_0202/0204/0404)}

To play audio files of different rate with automatic card rate change install [pulseaudio](https://archlinux.org/packages/?name=pulseaudio) and [pulseaudio-alsa](https://archlinux.org/packages/?name=pulseaudio-alsa) and keep using [ALSA](../../en/Advanced_Linux_Sound_Architecture.html "ALSA") as output:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
mpd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
audio_output {
    type          "alsa"
    name          "Emu 0202 USB"
    device        "hw:2,0"
}
```

### Changing user {#Changing_user}

Changing the group that MPD runs as may result in errors like:

    output: Failed to open "My ALSA Device"

    [alsa]: Failed to open ALSA device "default": No such file or directory

or

    player_thread: problems opening audio device while playing "Song Name.mp3"

This is because the MPD users need to be part of the *audio* group to access sound devices under `/dev/snd/`. To fix it add user make the MPD user part of the *audio* group:

    # gpasswd -a 'mpd' audio

### MPD includes music from hidden folders in database {#MPD_includes_music_from_hidden_folders_in_database}

MPD includes hidden folders in its database such as repetitive backups of music made by [syncthing](https://archlinux.org/packages/?name=syncthing) such as `.stfolder`. To correct for this, create a `.mpdignore` file in the same directory with a list of folders or files to ignore on each line as per the [mpd documentation](https://www.musicpd.org/doc/html/user.html#the-music-directory-and-the-database).
