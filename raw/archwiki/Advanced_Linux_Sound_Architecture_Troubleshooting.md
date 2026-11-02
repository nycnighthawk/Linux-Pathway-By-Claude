---
{"title": "Advanced Linux Sound Architecture/Troubleshooting", "url": "https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture/Troubleshooting", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Advanced Linux Sound Architecture/Troubleshooting

The [alsa-utils](https://archlinux.org/packages/?name=alsa-utils) package contains the [alsa-info.sh](https://docs.kernel.org/sound/hd-audio/notes.html#alsa-info) script, which can be used to gather detailed data on the ALSA state.

**Tip** Run `alsa-info.sh` with [root user](../../en/Root_user.html "Root user") privileges and share its output if you ask for help.

See also [SoundcardTesting](https://www.alsa-project.org/main/index.php/SoundcardTesting).

## Volume {#Volume}

### Output is muted after reboot {#Output_is_muted_after_reboot}

Run the following command:

    # alsactl restore

If the problem persists, verify that the `Auto-Mute` option in [alsamixer(1)](https://man.archlinux.org/man/alsamixer.1) is set to `Disabled`.

### Volume is too low {#Volume_is_too_low}

Run `alsamixer` and try to increase the value of the sliders, unmuting channels if necessary. Note that if you have many sliders, you may have to scroll to the right to see any missing sliders.

If all the sliders are maxed out, and the volume is still too low, you can try running the following script to reset your codec settings:

    $ wget -O hda-analyzer.py https://git.alsa-project.org/?p=alsa.git;a=blob_plain;f=hda-analyzer/run.py

Close the analyzer, and when prompted as to whether you want to reset the codecs, say \"yes\".

If the volume is still too low, run `alsamixer` again: resetting the codecs may have caused new sliders to become enabled and some of them may be set to a low value.

### Volume is still too low {#Volume_is_still_too_low}

If you are facing low volume even after maxing out your speakers/headphones, you can give the softvol plugin a try. Add the following to `/etc/asound.conf`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/asound.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
pcm.!default {
    type plug
    slave.pcm "softvol"
}

pcm.softvol {
    type softvol
    slave {
        pcm "dmix"
    }
    control {
        name "Pre-Amp"
        card 0
    }
    min_dB -5.0
    max_dB 20.0
    resolution 6
}
```

**Tip** If this configuration does not work, try to change `type plug` with `type hw`.

After the changes are loaded successfully, you will see a `Pre-Amp` section in *alsamixer*. You can adjust the levels there.

**Note**

-   Setting a high value for `Pre-Amp` can cause sound distortion, so adjust it according to the level that suits you.
-   Some audio codecs may need to have settings adjusted in the HDA Analyzer (see [#Volume is too low](#Volume_is_too_low)) in order to achieve proper volume without distortion. Checking the HP option under widget control in the Playback Switch (Node\[0x14\] PIN in the ALC892 codec, for instance) can sometimes improve audio quality and volume significantly.

### Random lack of sound on startup {#Random_lack_of_sound_on_startup}

You can quickly test sound by running `speaker-test`. If there is no sound, you may see something similar to:

    ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave
    Playback open error: -16
    Device or resource busy

If you have no sound on startup, this may be because your system has multiple sound cards, and their order may sometimes change on startup. If this is the case, try [setting the default sound card](../../en/Advanced_Linux_Sound_Architecture.html#Set_the_default_sound_card "ALSA").

If you use [MPD](../../en/Music_Player_Daemon.html "MPD") and the above configuration tips do not work, try following [https://mpd.wikia.com/wiki/Configuration#ALSA_MPD_software_volume_control](https://mpd.wikia.com/wiki/Configuration#ALSA_MPD_software_volume_control).

## Microphone {#Microphone}

### No microphone input {#No_microphone_input}

In [alsamixer(1)](https://man.archlinux.org/man/alsamixer.1), make sure that all the volume levels are up under recording, and that *CAPTURE* is toggled active on the microphone (e.g. *Mic*, *Internal Mic*) and/or on *Capture* (in *alsamixer*, select these items and press `Space`). Try making positive *Mic Boost* and raising *Capture* and *Digital* levels higher; this may make static or distortion, but then you can adjust them back down once you are hearing *something* when you record.

As the [PulseAudio](../../en/PulseAudio.html "PulseAudio") wrapper is shown as \"default\" in *alsamixer*, you may have to press `F6` to select your actual sound card first. You may also need to enable and increase the volume of *Line-in* in the *Playback* section.

To test the microphone, run these commands (see [arecord(1)](https://man.archlinux.org/man/arecord.1) for further information):

    $ arecord --duration=5 --format=dat test-mic.wav
    $ aplay test-mic.wav

Alternatively, you can run this command:

    $ arecord -vv --format=dat /dev/null

alongside *alsamixer* to easily identify channel which you should select and unmute.

To test a particular device, use the `--device` parameter followed by the hardware PCM name in the form `hw:`*`C`*`,`*`D`* for card *C* device *D*, or `plughw:`*`C`*`,`*`D`* for plugged hardware. For instance:

    $ arecord -vvv --format=dat --device=plughw:0,0 /dev/null

If all fails, you may want to eliminate hardware failure by testing the microphone with a different device.

For at least some computers, muting a microphone (MM) simply means its input does not go immediately to the speakers. It still receives input.

Some programs use try to use OSS as the main input software. If you have enabled the `snd_pcm_oss`, `snd_mixer_oss` or `snd_seq_oss` [kernel modules](../../en/Kernel_modules.html "Kernel modules") previously (they are not loaded by default), try unloading them.

See also:

-   [#Wrong model autodetection](#Wrong_model_autodetection)
-   [Record from mic](https://alsa.opensrc.org/Record_from_mic)

### Setting the default microphone/capture device {#Setting_the_default_microphone/capture_device}

Some applications (Pidgin, Adobe Flash) do not provide an option to change the capture device. It becomes a problem if your microphone is on a separate device (e.g. USB webcam or microphone) than your internal sound card. To change only the default capture device, leaving the default playback device as is, you can modify your `~/.asoundrc` file to include the following:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.asoundrc
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
pcm.usb
{
    type hw
    card U0x46d0x81d
}

pcm.!default
{
    type asym
    playback.pcm
    {
        type plug
        slave.pcm "dmix"
    }
    capture.pcm
    {
        type plug
        slave.pcm "usb"
    }
}
```

Replace *U0x46d0x81d* with your capture device\'s card name in ALSA. You can use `arecord -L` to list all the capture devices detected by ALSA.

### Internal microphone not working {#Internal_microphone_not_working}

First make sure the volume is enabled under the `Capture` view in *alsamixer*. In some cases, the \"Internal Microphone\" is not displayed in the capture list available when pressing F4. If so, specifying the card number given by `aplay -l` to start *alsamixer* (for example `alsamixer -c 0` ) can make it appear.

## Audio quality {#Audio_quality}

### Crackling sound through mini-jack (headphones connector) {#Crackling_sound_through_mini-jack_(headphones_connector)}

Following [Advanced Linux Sound Architecture#Simultaneous output](../../en/Advanced_Linux_Sound_Architecture.html#Simultaneous_output "Advanced Linux Sound Architecture") might lead to crackling sound through headphones or external speakers. This can be fixed by muting **or** setting the volume to `0%` on *Mic*. Use [alsamixer(1)](https://man.archlinux.org/man/alsamixer.1) or [amixer(1)](https://man.archlinux.org/man/amixer.1):

    $ amixer sset "Mic" 0%
    $ amixer sset "Mic" mute

### Popping sound after resuming from suspension {#Popping_sound_after_resuming_from_suspension}

You might hear a popping sound after resuming the computer from suspension. This can be fixed by editing `/etc/pm/sleep.d/90alsa` and removing the line that says `aplay -d 1 /dev/zero`

### Sound skipping during playback {#Sound_skipping_during_playback}

Run `alsamixer`, and if channels exist for nonexistent output devices then disable them (e.g. *alsamixer* showing a center speaker but you not having one).

### Poor sound quality or clipping {#Poor_sound_quality_or_clipping}

If you experience poor sound quality, try setting the PCM volume (in *alsamixer*) to a level such that gain is 0.

If `snd_usb_audio` driver has been loaded, you could try to enable `softvol`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/asound.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
pcm.!default {
    type plug
    slave.pcm "softvol"
}
pcm.dmixer {
    type dmix
    ipc_key 1024
    slave {
        pcm "hw:0"
        period_size 4096
        buffer_size 131072
        rate 50000
    }
    bindings {
        0 0
        1 1
    }
}
pcm.dsnooper {
    type dsnoop
    ipc_key 1024
    slave {
        pcm "hw:0"
        channels 2
        period_size 4096
        buffer_size 131072
        rate 50000
    }
    bindings {
        0 0
        1 1
        }
}
pcm.softvol {
  type softvol
  slave { pcm "dmixer" }
  control {
    name "Master"
    card 0
  }
}
ctl.!default {
  type hw
  card 0
}
ctl.softvol {
  type hw
  card 0
}
ctl.dmixer {
  type hw
  card 0
}
```

### Pops when starting and stopping playback {#Pops_when_starting_and_stopping_playback}

Some modules (e.g. `snd_hda_intel`) can power off your sound card when it is not used. This might cause audible click noises---like a crack/pop/scratch---at each power-down/up depending on the device (sometimes even when moving the volume slider or opening and closing windows on some desktop environments).

For more information, see [Power management#Audio](../../en/Power_management.html#Audio "Power management") and [#Power saving](#Power_saving).

## Hardware and cards {#Hardware_and_cards}

### HD Audio {#HD_Audio}

For more information, see [Module snd-hda-intel](https://docs.kernel.org/sound/alsa-configuration.html#module-snd-hda-intel) and the output of `modinfo --field=parm snd_hda_intel | column --separator=':' --table`.

See also:

-   [Advanced Linux Sound Architecture#Driver configuration](../../en/Advanced_Linux_Sound_Architecture.html#Driver_configuration "Advanced Linux Sound Architecture")
-   [Intel High Definition Audio](https://en.wikipedia.org/wiki/Intel_High_Definition_Audio "wikipedia:Intel High Definition Audio") **(HD Audio)**

#### Power saving {#Power_saving}

[Power saving](https://docs.kernel.org/sound/hd-audio/notes.html#power-saving) is enabled by default and might cause the following issues:

-   [#Pops when starting and stopping playback](#Pops_when_starting_and_stopping_playback)
-   [PC speaker#The HD Audio power-saving mode mutes the PC speaker](../../en/PC_speaker.html#The_HD_Audio_power-saving_mode_mutes_the_PC_speaker "PC speaker")
-   [VirtualBox/Install Arch Linux as a guest#Linux guests have slow/laggy audio](../../en/VirtualBox/Install_Arch_Linux_as_a_guest.html#Linux_guests_have_slow/laggy_audio "VirtualBox/Install Arch Linux as a guest")

To completely disable the power-saving mode for the `snd_hda_intel` module, use the following [kernel module parameters](../../en/Kernel_module_parameter.html "Kernel module parameter"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/alsa-base.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
options snd_hda_intel power_save=0 power_save_controller=N
```

#### Codec probing {#Codec_probing}

A [codec](https://en.wikipedia.org/wiki/Codec "wikipedia:Codec") is a hardware component of an HD Audio sound card. One card might incorporate more than one codec, one codec might correspond to more than one ALSA device.

A *codec slot* is a number (it begins from zero) identifying the codec on a given sound card. You can get the codec slot number from `/proc/asound/card`***`i`***`/codec#`***`s`*** file and `/sys/class/sound/hwC`***`i`***`D`***`s`***`/` directory names---here *`i`* is a card index, and *`s`* is a codec slot.

**Note** Do not confuse HD Audio card *codec slot* with [OSS](../../en/Open_Sound_System.html "OSS") *slot number*, which corresponds to the ALSA [card index](../../en/Advanced_Linux_Sound_Architecture.html#Card_index "Advanced Linux Sound Architecture").

To disable a codec---and subsequently all of the related ALSA devices---[use](https://docs.kernel.org/sound/hd-audio/notes.html#codec-probing-problem) the `probe_mask` option of the `snd_hda_intel` module.

#### Wrong model autodetection {#Wrong_model_autodetection}

Wrong model autodetection might cause the following issues:

-   [#No microphone input](#No_microphone_input)
-   Microphone is not detected if it is plugged in a combined headset/microphone 4-pole 3.5 mm [TRRS](https://en.wikipedia.org/wiki/Phone_connector_(audio)#TRRS "wikipedia:Phone connector (audio)") jack

**Tip** If your chip is [ALC22x/23x/25x/269/27x/28x/29x](https://docs.kernel.org/sound/hd-audio/models.html#alc22x-23x-25x-269-27x-28x-29x-and-vendor-specific-alc3xxx-models) or [ALC66x/67x/892](https://docs.kernel.org/sound/hd-audio/models.html#alc66x-67x-892), then try `dell-headset-multi`, even if the hardware is not from Dell.

-   No headphone output

See [HD-Audio Codec-Specific Models](https://docs.kernel.org/sound/hd-audio/models.html) for possible `model` strings for a given sound card chip.

The sound card chip can be found in:

-   [alsamixer(1)](https://man.archlinux.org/man/alsamixer.1)---see *Chip:* in the upper-left corner,
-   output of `grep 'Codec:' /proc/asound/card*/codec#*`,
-   output of `grep . /sys/class/sound/hwC?D?/chip_name`,
-   `/proc/asound/pcm` file.

To force, use the `model` option of the `snd_hda_intel` module.

#### Message Signaled Interrupts {#Message_Signaled_Interrupts}

Whether [Message Signaled Interrupts](https://en.wikipedia.org/wiki/Message_Signaled_Interrupts "wikipedia:Message Signaled Interrupts") (MSI) should be enabled or not [hardly depends](https://docs.kernel.org/sound/hd-audio/notes.html#interrupt-handling) on the hardware. In the case of wrong autodetection different kinds of bad things could happen:

-   erroneous disablement might lead to the sound card is not detected;
-   erroneous enablement might lead to poor audio quality (stuttering), or even kernel lockup.

To check the MSI capability status, run `lspci -vv -nn -d ::0401` and `lspci -vv -nn -d ::0403` with [root user](../../en/Root_user.html "Root user") privileges.

**Tip**

-   See [Advanced Linux Sound Architecture#Cards and modules](../../en/Advanced_Linux_Sound_Architecture.html#Cards_and_modules "Advanced Linux Sound Architecture") for more information.
-   MSI on HD Audio cards are controlled by the `enable_msi` option of the `snd_hda_intel` module.

#### DMA pointer {#DMA_pointer}

Click noises (crackling, popping) on input and/or output of an HD Audio card might be caused by [DMA position problem](https://docs.kernel.org/sound/hd-audio/notes.html#dma-position-problem). Try to change the `position_fix` option of the `snd_hda_intel` module.

#### Fix wrong audio pin mapping {#Fix_wrong_audio_pin_mapping}

If the mappings to your audio pins(plugs) do not correspond but ALSA works fine, you could try HDA Analyzer \-- a pyGTK2 GUI for HD-audio control can be found [at the ALSA wiki](https://www.alsa-project.org/main/index.php/HDA_Analyzer). Try tweaking the Widget Control section of the PIN nodes, to make microphones IN and headphone jacks OUT. Referring to the Config Defaults heading is a good idea.

**Note** The script is incompatible with Python 3, which is the default Python implementation on Arch Linux. In order to use the script, replace all occurrences of `python` in the `run.py` file with `python2` to point the script to the Python 2 version. Then make the script [executable](../../en/File_permissions_and_attributes.html#Changing_permissions "Chmod") and run it.

### Verifying output parameters {#Verifying_output_parameters}

Check the contents of `/proc/asound/card`***`C`***`/pcm`***`P`***`p/sub`***`S`***`/hw_params`, where *`C`*, *`P`*, and *`S`* are system dependent. In order to find this file, execute the following command chain while outputting something via [ALSA](../../en/Advanced_Linux_Sound_Architecture.html "ALSA"):

    $ find /proc/asound/ -name hw_params \
    | xargs -I FILE grep -v -l "closed" FILE \
    | grep '/proc/asound/card./pcm.p/sub./hw_params'

**Note** If nothing is playing there should be no results.

Here is an example output for audio with a [bit depth](https://en.wikipedia.org/wiki/Audio_bit_depth "wikipedia:Audio bit depth") of 24 bits and a [sampling frequency](https://en.wikipedia.org/wiki/Sampling_frequency "wikipedia:Sampling frequency") of 44.1 [kilohertz](https://en.wikipedia.org/wiki/Hertz "wikipedia:Hertz"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ cat /proc/asound/card1/pcm0p/sub0/hw_params
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
access: RW_INTERLEAVED
format: S24_3LE
subformat: STD
channels: 2
rate: 44100 (44100/1)
period_size: 5513
buffer_size: 22050
```

For more information see the [Proc asound documentation](https://alsa.opensrc.org/Proc_asound_documentation).

### S/PDIF output does not work {#S/PDIF_output_does_not_work}

[S/PDIF](https://en.wikipedia.org/wiki/S/PDIF "wikipedia:S/PDIF") (IEC958) utilizes two modes:

-   *Audio* mode is digital PCM signal, so the receiver just converts the data with [digital-to-analog converter](https://en.wikipedia.org/wiki/Digital-to-analog_converter "wikipedia:Digital-to-analog converter") (DAC).

&nbsp;

-   *Non-audio* mode is an encoded bitstream, so the receiver must decode the data first, and put it to DAC then. [Dolby Digital](https://en.wikipedia.org/wiki/Dolby_Digital "wikipedia:Dolby Digital") and [DTS Digital Surround](https://en.wikipedia.org/wiki/DTS_Digital_Surround "wikipedia:DTS Digital Surround") are examples of encoded bitstream formats.

ALSA should detect appropriate mode automatically, but if it fails, you can force the mode with [iecset(1)](https://man.archlinux.org/man/iecset.1) (`on`---*audio*, `off`---*non-audio*):

    # iecset audio on
    # iecset audio off

For more information, see [DigitalOut](https://alsa.opensrc.org/DigitalOut).

### HDMI {#HDMI}

**This article or section is a candidate for merging with [ALSA](../../en/Advanced_Linux_Sound_Architecture.html "ALSA").**

**Notes:** This section has almost nothing related to HDMI per se: it is sorta TL;DR for the main article (list devices, test sound, set the default device; remap). (Discuss in [Talk:Advanced Linux Sound Architecture/Troubleshooting](../../en/Talk:Advanced_Linux_Sound_Architecture/Troubleshooting.html))

#### HDMI output does not work {#HDMI_output_does_not_work}

The procedure described below can be used to test HDMI audio. Before proceeding, make sure you have enabled and unmuted the output with `alsamixer`.

Connect your PC to the Display via HDMI cable and enable the display with [xrandr](../../en/Xrandr.html "Xrandr").

Use `aplay -l` to discover the card and device number. For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ aplay -l
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
**** List of PLAYBACK Hardware Devices ****
card 0: SB [HDA ATI SB], device 0: ALC892 Analog [ALC892 Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 0: SB [HDA ATI SB], device 1: ALC892 Digital [ALC892 Digital]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: Generic [HD-Audio Generic], device 3: HDMI 0 [HDMI 0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

Send sound to the device. Following the example in the previous step, you would send sound to **`card 1`**, **`device 3`**:

    $ aplay -D plughw:1,3 /usr/share/sounds/alsa/Front_Center.wav

If aplay does not output any errors, but still no sound is heard, \"reboot\" the receiver, monitor or tv set. Since the HDMI interface executes a handshake on connection, it might have noticed before that there was no audio stream embedded, and disabled audio decoding. If you are using a standalone window manager, you may need to have sound playing while plugging in the HDMI cable.

mplay and other application could be configured to use special HDMI device as audio output. But flashplugin could only use default device. The following method is used to override default device. But you need to change it back when your TV is disconnected from HDMI port.

If the test is successful, create or edit your `~/.asoundrc` file to set HDMI as the default audio device.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.asoundrc
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
pcm.!default {
    type hw
    card 1
    device 3
}
```

Or if the above configuration does not work try:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.asoundrc
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
defaults.pcm.card 1
defaults.pcm.device 3
defaults.ctl.card 1
```

Or if you alternatively succeed with

    $ speaker-test -Dplug:hdmi

for your HDMI or DisplayPort port the following configuration will work (successfully tested on Lenovo ThinkPad T430s):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.asoundrc
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
pcm.!default {
    type plug
    slave.pcm "hdmi"
}
```

#### HDMI 5.1 sound goes to wrong speakers {#HDMI_5.1_sound_goes_to_wrong_speakers}

Sound can be redirected to the intended speakers using ALSA\'s `remap` function.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/asound.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
pcm.!hdmi-remap {
    type asym
    playback.pcm {
        type plug
        slave.pcm "remap-surround51"
    }
}

pcm.!remap-surround51 {
    type route
    slave.pcm "hw:0,3"
    ttable {
        0.0= 1
        1.1= 1
        2.4= 1
        3.5= 1
        4.2= 1
        5.3= 1
    }
}
```

## Applications {#Applications}

### SDL: No sound with SDL applications {#SDL:_No_sound_with_SDL_applications}

If you get no sound using SDL based applications, try setting the [environment variable](../../en/Environment_variable.html "Environment variable") `SDL_AUDIODRIVER` to `alsa`.

### OpenAL: No sound in applications that use OpenAL {#OpenAL:_No_sound_in_applications_that_use_OpenAL}

OpenAL defaults to PulseAudio. To instruct it to try ALSA first:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/openal/alsoft.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
drivers=alsa,pulse
```

### Others: Generic application problems {#Others:_Generic_application_problems}

For other applications who insist on their own audio setup, e.g., XMMS or MPlayer, you would need to set their specific options.

For [MPlayer](../../en/MPlayer.html "MPlayer") or [mpv](../../en/Mpv.html "Mpv"), add the following line to the respective configuration file:

    ao=alsa

Eg. for XMMS2, go into their options and make sure the sound driver is set to ALSA, not oss.

To do this in XMMS:

-   Open XMMS
    -   Options \> Preferences.
    -   Choose the ALSA output plugin.

For applications which do not provide a ALSA output, you can use aoss from the alsa-oss package. To use aoss, when you run the program, prefix it with `aoss`, e.g.:

    aoss realplay

pcm.!default{ \... } doesnt work for me anymore. but this does:

    pcm.default pcm.dmixer

## Other issues {#Other_issues}

### Simultaneous playback problems {#Simultaneous_playback_problems}

If you are having problems with simultaneous playback, and if [PulseAudio](../../en/PulseAudio.html "PulseAudio") is installed, its default configuration is set to \"hijack\" the soundcard. Some users of ALSA may not want to use [PulseAudio](../../en/PulseAudio.html "PulseAudio") and are quite content with their current ALSA settings. One fix is to edit `/etc/asound.conf` and comment out the following lines:

    # Use PulseAudio by default
    pcm.!default {
        type pulse
        fallback "sysdefault"
        hint {
            show on
            description "Default ALSA Output (currently PulseAudio Sound Server)"
        }
    }

Commenting the following out also may help:

    ctl.!default {
        type pulse
        fallback "sysdefault"
    }

This may be a much simpler solution than completely uninstalling [PulseAudio](../../en/PulseAudio.html "PulseAudio").

Effectively, here is an example of a working `/etc/asound.conf`:

    pcm.dmixer {
        type dmix
        ipc_key 1024
        ipc_key_add_uid 0
        ipc_perm 0660
    }
    pcm.dsp {
        type plug
        slave.pcm "dmix"
    }

**Note** This `/etc/asound.conf` file was intended for and used successfully with a global [MPD](../../en/Music_Player_Daemon.html "MPD") configuration. See [#Problems with availability to only one user at a time](#Problems_with_availability_to_only_one_user_at_a_time).

**Note** Alternatively, if you do **not** have PulseAudio installed, and just want to get `dmix` to work with vanilla ALSA, see the [upstream documentation](https://www.alsa-project.org/main/index.php/Asoundrc#dmix). In particular, you probably want to replace `dsp` in the above config with `!default`. Also, if you notice this causes certain applications to skip while playing (i.e. sound \"glitchy\"), and complain about underrun occurring, you may want to tweak the `slave.buffer_size` inside `pcm.dmixer`.

### Removing old ALSA state file (asound.state) {#Removing_old_ALSA_state_file_(asound.state)}

The [alsa-utils](https://archlinux.org/packages/?name=alsa-utils) package provides `alsa-store.service` which automatically stores the current ALSA state to `/var/lib/alsa/asound.state` upon system shutdown. This can be problematic for users who are trying to reset their current ALSA state as the `asound.state` file will be recreated with the current state upon every shutdown (e.g., attempting to remove user-defined channels from the mixer). The `alsa-store.service` service may be temporarily disabled by creating the following empty file:

    # mkdir -p /etc/alsa
    # touch /etc/alsa/state-daemon.conf

The presence of `state-daemon.conf` prevents `alsa-store.service` from saving `asound.state` during shutdown. After disabling this service, the `asound.state` file may be removed as such:

    # rm /var/lib/alsa/asound.state

After rebooting, the previous ALSA state should be lost and the current state should be reset to defaults. Re-enable `alsa-store.service` by deleting the condition file we created:

    # rm /etc/alsa/state-daemon.conf

On the next shutdown, the `asound.state` file should be recreated with ALSA defaults. The file may also be generated immediately using:

    # alsactl store

If you want to clean ALSA state without rebooting, you can use `rmmod` to remove the sound driver module, then manually delete the unwanted entries in `asound.state`, and then use `modprobe` to reinstall the sound driver module.

### Problems with availability to only one user at a time {#Problems_with_availability_to_only_one_user_at_a_time}

You might find that only one user can use the dmixer at a time. This is probably ok for most, but for those who run [mpd](../../en/Music_Player_Daemon.html "Mpd") as a separate user this poses a problem. When mpd is playing a normal user cannot play sounds though the dmixer. While it is quite possible to just run mpd under a user\'s login account, another solution has been found. Adding the line `ipc_key_add_uid 0` to the `pcm.dmixer` block disables this locking. The following is a snippet from `asound.conf`, the rest is the same as above.

    ...
    pcm.dmixer {
        type dmix
        ipc_key 1024
        ipc_key_add_uid 0
        ipc_perm 0660
    slave {
     ...

### Crackling/popping on Dell laptops {#Crackling/popping_on_Dell_laptops}

Check if you have [i8kutils](https://aur.archlinux.org/packages/i8kutils/)^AUR^ installed and if anything (e.g. `i8kmon.service`) is reading or writing to the interface exposed by the module, as i8kutils BIOS system calls block the kernel for a moment on some systems. See warning in [Fan speed control#Dell laptops](../../en/Fan_speed_control.html#Dell_laptops "Fan speed control") for more details.
