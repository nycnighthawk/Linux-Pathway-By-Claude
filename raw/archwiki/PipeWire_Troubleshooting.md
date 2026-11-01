---
{"title": "PipeWire/Troubleshooting", "url": "https://wiki.archlinux.org/title/PipeWire/Troubleshooting", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# PipeWire/Troubleshooting

Before continuing check the obvious ones:

1.  Did you select the right sound card?
2.  Is the volume up (soft- and hardware)?
3.  Are the cables connected to the right ports?
4.  Is the USB sound card connected directly to the computer?
5.  Have you turned up the microphone volume, connected it and enabled the XLR phantom amplifier?
6.  Is the surround sound messed up? Then first [uninstall](../../en/Pacman.html#Removing_packages "Uninstall") UCM configurations package [alsa-ucm-conf](https://archlinux.org/packages/?name=alsa-ucm-conf). See [PulseAudio/Examples#Disabling UCM/\"HiFi\"](../../en/PulseAudio/Examples.html#Disabling_UCM/%22HiFi%22 "PulseAudio/Examples").
7.  [Restart](../../en/Help:Reading.html#Control_of_systemd_units "Restart") `pipewire.service` and `pipewire-pulse.service` [user unit](../../en/User_unit.html "User unit").

## Volume {#Volume}

### No sound in various applications but sound in browser {#No_sound_in_various_applications_but_sound_in_browser}

**The factual accuracy of this article or section is disputed.**

**Reason:** Issue\'s root cause is guessed not verified. Only application mute issue? (Discuss in [Talk:PipeWire/Troubleshooting](../../en/Talk:PipeWire/Troubleshooting.html))

Use `mpv` to check for installed codecs working

    $ mpv --ao=alsa test_file.mpv
    $ mpv --ao=pcm test_file.mpv
    $ mpv --ao=jack test_file.mpv
    $ mpv --ao=pulse test_file.mpv
    $ mpv --ao=openal test_file.mpv

If some or all of the above tests produce sound and the following does not

    $ mpv --ao=pipewire test_file.mpv

it might be that `pipewire` channel is muted. Install `pavucontrol` and run it.

Select the appropriate source in the Configuration tab, select it again in the Output device tab and then use Mute button to mute and unmute the source while `mpv --ao=pipewire test.mp4` video is running.

Alternatively, remove `~/.local/state/wireplumber/` and restart pipewire `systemctl --user restart pipewire pipewire-pulse wireplumber.service`

### Low volume {#Low_volume}

After replacing PulseAudio with Pipewire, sound may work fine, but after a reboot, the volume becomes intolerably low.

Open `alsamixer`, use `F6` to select the proper soundcard, and make sure the ALSA volumes are at 100%. `alsactl` should maintain this setting after reboot.

### Device volume for SDDM and LightDM users is not restored on login {#Device_volume_for_SDDM_and_LightDM_users_is_not_restored_on_login}

If you use [SDDM](../../en/SDDM.html "SDDM") or [LightDM](../../en/LightDM.html "LightDM") and notice that your audio volume level is not properly restored after logging in, mask PipeWire for the display manager\'s user, since WirePlumber running under the display manager can interfere with your user\'s WirePlumber session.

    # systemctl --user -M user@ mask pipewire.socket

Replace *`user`* with `sddm` for SDDM or `lightdm` for LightDM.

For more details, see this [Debian Wiki article](https://wiki.debian.org/PipeWire#Device_volume_for_SDDM_users_is_not_restored_on_login).

## Microphone {#Microphone}

### Microphone is not detected by PipeWire {#Microphone_is_not_detected_by_PipeWire}

If you are using a built in microphone of a laptop, or connected using the headphone jack: First make sure the analog input is enabled in the profile in use. You can check the profile in [pavucontrol](https://archlinux.org/packages/?name=pavucontrol) (and possibly in your desktop environment sound settings). In pavucontrol, on the Configuration tab, under \"Built-in Audio\" (or similar) make sure \"Analog Stereo Duplex\" is selected. If you use an advanced sound setup such as 5.1 or sound over HDMI, make sure a profile that includes \"+ Analog Stereo Input\" is selected.

PipeWire\'s `alsa-monitor` module uses [alsa-card-profiles](https://archlinux.org/packages/?name=alsa-card-profiles) to detect devices by default. If this is not working for you, try to turn off `api.alsa.use-acp`, or optionally turn on `api.alsa.use-ucm` in [wireplumber](https://archlinux.org/packages/?name=wireplumber):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/wireplumber/wireplumber.conf.d/alsa-config.conf (or ~/.config/wireplumber/wireplumber.conf.d/alsa-config.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
monitor.alsa.properties = {
  # Use ALSA-Card-Profile devices. They use UCM or the profile
  # configuration to configure the device and mixer settings.
  # alsa.use-acp = true
  # Use UCM instead of profile when available. Can be disabled
  # to skip trying to use the UCM profile.
  alsa.use-ucm = true
}
```

With [pipewire-media-session](https://archlinux.org/packages/?name=pipewire-media-session):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pipewire/media-session.d/alsa-monitor.conf (or ~/.config/pipewire/media-session.d/alsa-monitor.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
rules = [
    {
        ...
        actions = {
        update-props = {
            ...
            api.alsa.use-acp = false
...
```

Then, restart WirePlumber and check available devices:

**This article or section is out of date.**

**Reason:** Option `--list-targets` is no longer available in the recent versions of `pw-record`; in order to list objects use either `wpctl status` or `pw-cli ls` or `pw-dump` instead. (Discuss in [Talk:PipeWire/Troubleshooting](../../en/Talk:PipeWire/Troubleshooting.html))

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ pw-record --list-targets
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Available targets ("*" denotes default): 62
    58: description="Built-in Audio" prio=1872
    60: description="Built-in Audio" prio=2000
*   62: description="Built-in Audio (Loopback PCM)" prio=1984
```

An alternative solution suggested in [this PipeWire issue](https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/2332) is to add the microphone manually. First of all, make sure the microphone is detected by ALSA.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ arecord -l
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
**** List of CAPTURE Hardware Devices ****
card card_number: card_name, device device_number: device_name
  ...
```

Choose your microphone from the list, and to further test the microphone, run the following commands.

    $ arecord --duration=5 --format=dat --device=hw:card_number,device_number test-mic.wav # record from the mic
    $ aplay test-mic.wav # play it

If the microphone is working with `arecord`, but not detected by PipeWire, try to add a configuration file to manually add this device.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pipewire/pipewire.conf.d/microphone.conf (or ~/.config/pipewire/pipewire.conf.d/microphone.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
context.objects = [
    { factory = adapter
        args = {
            factory.name           = api.alsa.pcm.source
            node.name              = "microphone"
            node.description       = "Undetected Microphone"
            media.class            = "Audio/Source"
            api.alsa.path          = "hw:card_number,device_number"
        }
    }
]
```

And then restart PipeWire to reload the configuration.

## Audio quality {#Audio_quality}

### Crackling due to powersaving {#Crackling_due_to_powersaving}

Crackling may be caused by the [wikipedia:HECI](https://en.wikipedia.org/wiki/HECI "wikipedia:HECI") Controller being power managed. Runtime PM may be diabled with [powertop](../../en/Powertop.html "Powertop").

### Audio is distorted {#Audio_is_distorted}

-   For microphones, try navigating to the card that is having issues after running `alsamixer` and use the arrow keys to reduce any \"Mic Boost\" or \"Internal Mic Boost\" options.
-   Follow [#Changing the default sample rate](#Changing_the_default_sample_rate), reducing the sample rate to `44100` (44.1 kHz).

### Changing the default sample rate {#Changing_the_default_sample_rate}

By default PipeWire sets a fixed global sample rate of 48kHz. If you need to change it, you can set a new default (although it isn\'t recommended):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pipewire/pipewire.conf.d/sample-rate.conf (or ~/.config/pipewire/pipewire.conf.d/sample-rate.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
context.properties = {
    default.clock.rate = sample_rate
}
```

This, however, isn\'t recommended as this will affect latencies as the quantum values aren\'t re-calculated automatically. You will have to change these yourself if you want to preserve the same ratio. To quote the documentation:

*The default clock rate determines the real time duration of the min/max/default quantums. You might want to change the quantums when you change the default clock rate to maintain the same duration for the quantums.*

Keep in mind that the rates of the streams will remain the same. All that PipeWire will be doing here is resampling to meet your new rate. So the 48kHz streams that would\'ve been left unaltered will now be resampled.

If you have gear that can handle different sample rates, it is instead recommended to leave the defaults and follow as indicated here: [#Changing the allowed sample rate(s)](#Changing_the_allowed_sample_rate(s))

### Changing the allowed sample rate(s) {#Changing_the_allowed_sample_rate(s)}

PipeWire can also change dynamically the output sample rates supported by your DAC. The sample rate follows the sample rate of the audio stream being played. For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pipewire/pipewire.conf.d/sample-rate.conf (or ~/.config/pipewire/pipewire.conf.d/sample-rate.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
context.properties = {
    default.clock.allowed-rates = [ 44100 48000 88200 96000 176400 192000 352800 384000 ]
}
```

Say the default sample rate is `48000`, which is the default. Normally if a stream outputs audio at 44100Hz (i.e. a music player playing a song at CD quality), Pipewire will resample the stream to 48kHz. However, if you have `44100` in this list, Pipewire will instead do the following. Pipewire will see that the stream is at 44100Hz, then check if `44100` is in the allowed rates and that the receiving output device (i.e. DAC) supports the rate. **In such case, the DAC will play the song losslessly.** If the rate isn\'t in the list or if the DAC doesn\'t support the rate, PipeWire will simply fall back to resampling the stream to the default sample rate.

According to [the developer](https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/1523): \"PipeWire allows up to 16 different sample rates and will switch when possible\". That means, with configuration above, **no resampling is done** when supported. Since PipeWire [0.3.61](https://gitlab.freedesktop.org/pipewire/pipewire/-/releases/0.3.61#pipewire) up to 32 different sample rates can be configured.

### Getting allowed sample rate(s) {#Getting_allowed_sample_rate(s)}

Consult your hardware manual for supported values of your DAC. Supported rates by the kernel driver codec are listed with the following command.

    $ grep -E 'Codec|Audio Output|rates' /proc/asound/card*/codec#*

If your DAC does not report codec information, you can try to obtain supported rates like this:

    $ grep -m1 -Hn "" /proc/asound/card?/stream? | tee /dev/tty | awk -F':' '{print $1}' | xargs grep 'Rates'

**Note** Although your DAC chip may report rates higher than advertised in specification, some of them were designed for exotic modes like USB to I2S

### Checking currently used sample rate {#Checking_currently_used_sample_rate}

To check which output sample rate is being used for a card run:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ grep rate: /proc/asound/card?/pcm??/sub?/hw_params
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/proc/asound/card1/pcm0p/sub0/hw_params:rate: 96000 (96000/1)
```

In `pcm0p` or `pcm0c` `c` is short for \"capture\" and `p` is for \"playback\".

Command:

    $ pw-top

also shows currently used sample rate for each card and audio stream.

**Tip** If your DAC will not switch to a higher rate, after setting default.clock.allowed-rates, it may mean that system cannot read rates supported by DAC. In such case you can still try setting default.clock.rate

## Hardware and cards {#Hardware_and_cards}

### Issues with JBL Quantum 350 Wireless and Discord {#Issues_with_JBL_Quantum_350_Wireless_and_Discord}

Symptom: Audio not working when Discord initiates the sound output / configuration. If existing sound is playing then Discord audio works. An error like

    spa.alsa: front:0p: (125 suppressed) snd_pcm_avail after recover: Broken pipe

will be present in the [journalctl](../../en/Systemd/Journal.html "Journalctl").

There are (at least) two possible solutions, one is increasing `api.alsa.headroom` (e.g. setting it to 512) or setting an appropriate `api.alsa.start-delay`. An example doing this for a JBL Quantum 350 wireless device is

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.config/wireplumber/wireplumber.conf.d/52-jbl-quantum-350-discord-fix.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
monitor.alsa.rules = [
   {
     matches = [
       {
         node.name = "alsa_output.usb-JBL_JBL_Quantum350_Wireless-00.analog-stereo"
       }
     ]
     actions = {
       update-props = {
         api.alsa.start-delay = 500
       }
     }
   }
 ]
```

and [restart](../../en/Help:Reading.html#Control_of_systemd_units "Restart") the `wireplumber.service` [user unit](../../en/User_unit.html "User unit") on the machine.

### XiiSound / HAVIT Fuxi-H3 (040b:0897) {#XiiSound_/_HAVIT_Fuxi-H3_(040b:0897)}

This USB headset has several quirks with PipeWire and WirePlumber:

-   Audio only works at 100% volume --- the hardware volume range is too narrow (0.00dB to 0.39dB) and PipeWire\'s dB mapping collapses any lower volume to silence.
-   Left channel is silent --- the device exposes a secondary ALSA mixer control (`PCM,1`, numid=10) for the left channel that WirePlumber does not initialize, leaving it at 0%.
-   Microphone initializes muted --- WirePlumber may start the capture source with mute enabled.

**Fix 1 --- Force software mixer:**

Create

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.config/wireplumber/wireplumber.conf.d/51-fuxi-h3-fix.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
monitor.alsa.rules = [
   {
     matches = [
       {
         device.name = "alsa_card.usb-XiiSound_Technology_Corporation_Fuxi-H3-00"
       }
     ]
     actions = {
       update-props = {
         api.alsa.soft-mixer = true
         api.alsa.ignore-dB = true
         api.alsa.split-enable = false
       }
     }
   }
 ]
```

and [restart](../../en/Help:Reading.html#Control_of_systemd_units "Restart") the `wireplumber.service` [user unit](../../en/User_unit.html "User unit") on the machine.

**Fix 2 --- Restore left channel:**

    $ amixer -c 0 cset numid=10 100

**Fix 3 --- Unmute microphone:**

    $ pactl set-source-mute alsa_input.usb-XiiSound_Technology_Corporation_Fuxi-H3-00.mono-fallback 0

**Persist across reboots:**

    # alsactl store 0

### No sound devices show up in KDE Plasma {#No_sound_devices_show_up_in_KDE_Plasma}

PipeWire clients (including the desktop environment) may rely on the [XDG_RUNTIME_DIR](https://specifications.freedesktop.org/basedir-spec/latest/#variables) [environment variable](../../en/Environment_variable.html "Environment variable") to connect to the PipeWire daemon. [\[1\]](https://docs.pipewire.org/page_daemon.html) If you experience no sound devices immediately after login, it may be because this variable has manually been set to the wrong path.

Although this be resolved by manually restarting PipeWire, other issues can still occur such as being unable to screen share in Chromium (with `pipewire context failed`). `XDG_RUNTIME_DIR` is automatically set by [pam_systemd(8)](https://man.archlinux.org/man/pam_systemd.8), so you should remove any instances of it being set in your initialization files.

### No sound during streaming to RAOP devices (Sonos etc.) {#No_sound_during_streaming_to_RAOP_devices_(Sonos_etc.)}

Set up mDNS hostname resolution using either [Avahi](../../en/Avahi.html "Avahi") or [systemd-resolved](../../en/Systemd-resolved.html "Systemd-resolved").

### Missing realtime priority/crackling under load after suspend {#Missing_realtime_priority/crackling_under_load_after_suspend}

**This article or section is being considered for removal.**

**Reason:** Said bug was fixed after moving to the [new freedesktop.org repo](https://gitlab.freedesktop.org/pipewire/rtkit/-/merge_requests/35) in 2023. (Discuss in [Talk:PipeWire/Troubleshooting](../../en/Talk:PipeWire/Troubleshooting.html))

Due to a [bug from 2011](https://github.com/heftig/rtkit/issues/13) in rtkit, suspend events cause PipeWire\'s realtime priority to be revoked and not restored. To disable the protection which causes this, [edit](../../en/Systemd.html#Editing_provided_units "Edit") `rtkit-daemon.service`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/rtkit-daemon.service.d/override.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
ExecStart=
ExecStart=/usr/lib/rtkit-daemon --no-canary
```

Then restart the `rtkit-daemon.service` unit and `pipewire.service` user unit, along with the media session service.

### Simultaneous output to multiple sinks on the same sound card {#Simultaneous_output_to_multiple_sinks_on_the_same_sound_card}

Create a copy of `/usr/share/alsa-card-profile/mixer/profile-sets/default.conf` so that changes persist across updates. Here we define a profile joining the two default mappings for Analog and HDMI.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/usr/share/alsa-card-profile/mixer/profile-sets/multiple.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[General]
auto-profiles = no

[Mapping analog-stereo]
device-strings = front:%f
channel-map = left,right
paths-output = analog-output analog-output-lineout analog-output-speaker analog-output-headphones analog-output-headphones-2
paths-input = analog-input-front-mic analog-input-rear-mic analog-input-internal-mic analog-input-dock-mic analog-input analog-input-mic analog-input-linein analog-input-aux analog-input-video analog-input-tvtuner analog-input-fm analog-input-mic-line analog-input-headphone-mic analog-input-headset-mic
priority = 15

[Mapping hdmi-stereo]
description = Digital Stereo (HDMI)
device-strings = hdmi:%f
paths-output = hdmi-output-0
channel-map = left,right
priority = 9
direction = output

[Profile multiple]
description = Analog Stereo Duplex + Digital Stereo (HDMI) Output
output-mappings = analog-stereo hdmi-stereo
input-mappings = analog-stereo
```

Then configure your session manager to use the new card-profile for matching devices. Identifying information can be found using `pw-dump` or [wpctl](../../en/WirePlumber.html#Obtain_interface_name_for_rules_matching "WirePlumber").

For [wireplumber](https://archlinux.org/packages/?name=wireplumber):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/wireplumber/wireplumber.conf.d/alsa-custom.conf (or ~/.config/wireplumber/wireplumber.conf.d/alsa-custom.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
monitor.alsa.rules = [
  {
    matches = [
      {
        device.nick = "HDA Intel PCH"
      }
    ]
    actions = {
      update-props = {
        api.alsa.use-acp = true
        api.acp.auto-profile = false
        api.acp.auto-port = false
        device.profile-set = "multiple.conf"
        device.profile = "multiple"
      }
    }
  }
]
```

For [pipewire-media-session](https://archlinux.org/packages/?name=pipewire-media-session):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pipewire/media-session.d/alsa-monitor.conf (or ~/.config/pipewire/media-session.d/alsa-monitor.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
rules = [
    {
        matches = [ { alsa.card_name = "HDA Intel PCH" } ]
        actions = {
            update-props = {
                api.alsa.use-acp = true
                device.profile-set = "multiple.conf"
                device.profile = "multiple"
                api.acp.auto-profile = false
                api.acp.auto-port = false
            }
        }
    }
]
```

### High latency with USB DACs (e.g. Schiit DACs) {#High_latency_with_USB_DACs_(e.g._Schiit_DACs)}

Changing sample rates or formats might help reduce latency with some DACs such as Schiit Hel 2.[\[2\]](https://www.reddit.com/r/osugame/comments/msifdd/usb_dacamp_and_audio_lag/)

For [pipewire-media-session](https://archlinux.org/packages/?name=pipewire-media-session):

Copy the default configuration file `/usr/share/pipewire/media-session.d/alsa-monitor.conf` into `/etc/pipewire/media-session.d/` (or `~/.config/pipewire/media-session.d/`). Then append a new rule-block similar to the following one:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pipewire/media-session.d/alsa-monitor.conf (or ~/.config/pipewire/media-session.d/alsa-monitor.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
rules = {
    ...
    {
        matches = [
            {
                node.name = "alsa_output.name-of-node"
            }
        ]
        actions = {
            update-props = {
                audio.format = "S24_3LE"
                audio.rate = 96000
                # Following value should be doubled until audio does not cut out or other issues stop occurring
                api.alsa.period-size = 128
...
```

For [wireplumber](https://archlinux.org/packages/?name=wireplumber):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/wireplumber/wireplumber.conf.d/update-rate-and-format.conf (or ~/.config/wireplumber/wireplumber.conf.d/update-rate-and-format.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
monitor.alsa.rules = [
  {
    matches = [
      {
        node.name = "alsa_output.name-of-node"
      }
    ]
    actions = {
      update-props = {
        audio.format = "S24_3LE"
        audio.rate = 96000
        # Following value should be doubled until audio does not cut out or other issues stop occurring
        api.alsa.period-size = 128
      }
    }
  }
]
```

`alsa_output.`*`name-of-node`* node can be obtained using `pw-top`.

Your DAC might support a different format or sample rate. You can check what your DAC supports by querying [ALSA](../../en/Advanced_Linux_Sound_Architecture.html "ALSA"):

First get the card number of your DAC:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ aplay -l
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
card 3: S2 [Schiit Hel 2], device 0: USB Audio [USB Audio]
  Subdevices: 0/1
  Subdevice #0: subdevice #0
...
```

So in this example it would be card 3. Get all supported sample rates and formats:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ cat /proc/asound/cardX/streamX
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
Playback:
  ...
  Interface 1
    Altset 1
    Format: S16_LE
    Channels: 2
    Endpoint: 0x05 (5 OUT) (ASYNC)
    Rates: 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000
    Data packet interval: 125 us
    Bits: 16
    ...
  Interface 1
    Altset 2
    Format: S24_3LE
    Channels: 2
    Endpoint: 0x05 (5 OUT) (ASYNC)
    Rates: 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000
    Data packet interval: 125 us
    Bits: 24
    ...
  Interface 1
    Altset 3
    Format: S32_LE
    Channels: 2
    Endpoint: 0x05 (5 OUT) (ASYNC)
    Rates: 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000
    Data packet interval: 125 us
    Bits: 32
    ...
...
```

In this case `S16_LE, S24_3LE, S32_LE` are the supported formats and `44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000` are the supported sample rates across all formats.

### No sound from USB DAC until 30% volume {#No_sound_from_USB_DAC_until_30%_volume}

Some USB DACs will have no sound output until a certain level of volume is reached [\[3\]](https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/1117). Typically, this is around 15% to 30%, which may result in an uncomfortably loud initial volume and the inability to maintain a low volume. The solution is to ignore hardware mixer volume control by setting `api.alsa.soft-mixer` for the device to `true`.

To achieve this with [wireplumber](https://archlinux.org/packages/?name=wireplumber), use:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/wireplumber/wireplumber.conf.d/alsa-soft-mixer.conf (or ~/.config/wireplumber/wireplumber.conf.d/alsa-soft-mixer.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
monitor.alsa.rules = [
  {
    matches = [
      {
        device.name = "alsa_card.name-of-device"
      }
    ]
    actions = {
      update-props = {
        # Do not use the hardware mixer for volume control. It
        # will only use software volume. The mixer is still used
        # to mute unused paths based on the selected port.
        api.alsa.soft-mixer = true
      }
    }
  }
]
```

Refer to [WirePlumber#Obtain interface name for rules matching](../../en/WirePlumber.html#Obtain_interface_name_for_rules_matching "WirePlumber") to find the correct value to replace `"alsa_card.`*`name-of-device`*`"`.

Alternatively, you may specify `"~alsa_card.*"` to apply the rules to all your audio devices.

Then, restart pipewire, e.g. by running `systemctl --user restart pipewire`. Set your master volume in `alsamixer`, then save the settings by running `alsactl store` as root. You should now be able to use your volume mixer as normal.

### Realtime audio does not work {#Realtime_audio_does_not_work}

If `RTKit error: org.freedesktop.DBus.Error.AccessDenied` shows up in the [status](../../en/Unit_status.html "Unit status") of the `pipewire.service` [user unit](../../en/User_unit.html "User unit"), then the priority of the pipewire daemon was not changed to realtime. See [\[4\]](https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/1069) for this issue.

### External sound card not activated after reconnect {#External_sound_card_not_activated_after_reconnect}

Check `~/.config/pipewire/media-session.d/default-profile` if there is any entry with default profile \"off\" and remove it. If that does not help, remove all files from `~/.config/pipewire/media-session.d/` and [restart](../../en/Help:Reading.html#Control_of_systemd_units "Restart") the `pipewire.service` [user unit](../../en/User_unit.html "User unit").

### No Sound or pactl info shows Failure: Connection refused {#No_Sound_or_pactl_info_shows_Failure:_Connection_refused}

It means applications are unable to connect to the PipeWire-Pulse service check if the `pipewire-pulse.service` [user unit](../../en/User_unit.html "User unit") is running.

If that does not fix it, run `strace -f -o /tmp/pipe.txt pactl info` and pastebin `/tmp/pipe.txt` while seeking help on IRC ([#pipewire](ircs://irc.oftc.net/pipewire) on OFTC) or the mailing-lists.

### Sound does not automatically switch when connecting a new device {#Sound_does_not_automatically_switch_when_connecting_a_new_device}

To automatically switch to newly connected devices, create this file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pipewire/pipewire-pulse.conf.d/switch-on-connect.conf (or ~/.config/pipewire/pipewire-pulse.conf.d/switch-on-connect.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
pulse.cmd = [
    { cmd = "load-module" args = "module-switch-on-connect" }
]
```

Then [restart](../../en/Help:Reading.html#Control_of_systemd_units "Restart") the `pipewire-pulse.service` with [systemctl \--user](../../en/Systemctl_--user.html "Systemctl --user") and check that `module-switch-on-connect` is loaded.

### No sound after connecting to Bluetooth device {#No_sound_after_connecting_to_Bluetooth_device}

As of 2020-12-07, if there is no sound after connecting a Bluetooth device, you might need to switch the default sink and/or move a sink input to the correct sink. Use `pactl list sinks` to list the available sinks and `pactl set-default-sink` to switch the default sink to the Bluetooth device. This can be automated via [udev](../../en/Udev.html "Udev") using a script similar to [this one](https://gist.github.com/tinywrkb/04e7fd644afa9b92d33a3a99ab07ee9e).

See this [Reddit thread](https://www.reddit.com/r/archlinux/comments/jydd02/pipewirepulse_03164_in_testing_now_replaces/gd3m7fu/?context=3) for a discussion of the issue. According to author of the script, the headset profile (HSP) might still have problems.

## Bluetooth {#Bluetooth}

### Low audio quality on Bluetooth {#Low_audio_quality_on_Bluetooth}

In case Bluetooth playback stutters, check the [unit status](../../en/Unit_status.html "Unit status") of the `pipewire.service` [user unit](../../en/User_unit.html "User unit") for errors similar as below:

    Feb 17 18:23:01 HOST pipewire[249297]: (bluez_input.18:54:CF:04:00:56.a2dp-sink-60) client too slow! rate:512/48000 pos:370688 status:triggered

If they appear, check the currently selected codec using `pactl list sinks` and try changing it by setting `bluez5.codec` to one of `sbc aac ldac aptx aptx_hd`. You can also try mSBC support (fixes mic on Sony 1000XM3, i.e. Headphones WH-1000XM3 and Earbuds WF-1000XM3), and the SBC-XQ codec.

**Note** Headphones like the WH-1000XM3 refuse to advertise any codecs other than SBC/SBC-XQ if \"Sound Quality Mode\" is set to \"Priority On Stable Connection\" instead of \"Prioritize Sound Quality\" in the companion app.

With [wireplumber](https://archlinux.org/packages/?name=wireplumber):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/wireplumber/wireplumber.conf.d/bluez-config.conf (or ~/.config/wireplumber/wireplumber.conf.d/bluez-config.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
monitor.bluez.properties = {
  bluez5.enable-sbc-xq = true
  bluez5.enable-msbc = true
  bluez5.codecs = [ sbc sbc_xq ]
}
```

With [pipewire-media-session](https://archlinux.org/packages/?name=pipewire-media-session):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pipewire/media-session.d/bluez-monitor.conf (or ~/.config/pipewire/media-session.d/bluez-monitor.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
properties = {
  ...
  bluez5.enable-msbc = true
  bluez5.enable-sbc-xq = true
  bluez5.codecs = [sbc sbc_xq]
...
```

Restart PipeWire by [restarting](../../en/Help:Reading.html#Control_of_systemd_units "Restart") the `pipewire.service` [user unit](../../en/User_unit.html "User unit") for the changes to take effect.

## Applications {#Applications}

### Terminal bell not working {#Terminal_bell_not_working}

From PipeWire\'s perspective, one must have the module x11.bell loaded. This shall be the configuration default (see also in configuration files mentioned above). Check if you have package [pipewire-x11-bell](https://archlinux.org/packages/?name=pipewire-x11-bell) installed. Also, your window manager might influence the terminal bell, e.g., for xfwm, check in the xfwm-terminal settings that \"Audible bell\" is activated. Now, restart pipewire service:

    $ systemctl --user restart pipewire

You can try if the terminal bell works with:

    $ echo $'\a'

### OBS (etc.) display nothing, even if they ask for a window/screen {#OBS_(etc.)_display_nothing,_even_if_they_ask_for_a_window/screen}

If you are sure that you have [xdg-desktop-portal](https://archlinux.org/packages/?name=xdg-desktop-portal) installed as well as either [xdg-desktop-portal-gtk](https://archlinux.org/packages/?name=xdg-desktop-portal-gtk) or [xdg-desktop-portal-kde](https://archlinux.org/packages/?name=xdg-desktop-portal-kde), check the running state of the daemons.

In OBS, if everything is working, you should see this in `stdout`:

    ...
    info: [pipewire] desktop selected, setting up screencast
    info: [pipewire] created stream 0x5632d7456850
    info: [pipewire] playing stream…

For multi-monitor setups the [slurp](https://archlinux.org/packages/?name=slurp) package will allow to capture of all the screens.

### FMOD games crashing under PipeWire {#FMOD_games_crashing_under_PipeWire}

Some games that use an old version of the [FMOD audio engine](https://en.wikipedia.org/wiki/FMOD "wikipedia:FMOD"), like [Pillars of Eternity](https://en.wikipedia.org/wiki/Pillars_of_Eternity "wikipedia:Pillars of Eternity"), invoke `pulseaudio --check` and crash if the PulseAudio binary is not present. A workaround is to symlink `/bin/pulseaudio` to `/bin/true`.[\[5\]](https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/1514)

    # ln -s /bin/true /bin/pulseaudio

Note that if you wish to reinstall PulseAudio, you need to remove the symlink.

### No notification sounds from Discord {#No_notification_sounds_from_Discord}

This might cause by having the min.quantum too low, try setting it to more than 700. You can make an override for Discord specifically by appending the following rule to the pulse.rules section of pipewire-pulse.conf.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pipewire/pipewire-pulse.conf (or ~/.config/pipewire/pipewire-pulse.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
pulse.rules = [
  ...
    {
        # Discord notification sounds fix
        matches = [ { application.process.binary = "Discord" } ]
        actions = {
            update-props = {
                pulse.min.quantum      = 1024/48000     # 21ms
            }
        }
    }
...
```

### Audio cutting out when multiple streams start playing {#Audio_cutting_out_when_multiple_streams_start_playing}

This problem can typically be diagnosed by reading the [journal](../../en/Systemd/Journal.html "Journal") of the `pipewire-pulse.service` [user unit](../../en/User_unit.html "User unit") and finding lines similar to:

    pipewire-pulse[21740]: pulse-server 0x56009b9d5de0: [Nightly] UNDERFLOW channel:0 offset:370676 underrun:940

According to the [official PipeWire troubleshooting guide](https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Troubleshooting#underrununderflow-and-broken-pipe-errors), to solve this problem for [wireplumber](https://archlinux.org/packages/?name=wireplumber):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/wireplumber/wireplumber.conf.d/alsa-config.conf (or ~/.config/wireplumber/wireplumber.conf.d/alsa-config.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
monitor.alsa.rules = [
  {
    matches = [
      {
        node.name = "~alsa_output.*"
      }
    ]
    actions = {
      update-props = {
        api.alsa.period-size   = 1024
        api.alsa.headroom      = 8192
      }
    }
  }
]
```

With [pipewire-media-session](https://archlinux.org/packages/?name=pipewire-media-session):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pipewire/media-session.d/alsa-monitor.conf (or ~/.config/pipewire/media-session.d/alsa-monitor.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
api.alsa.headroom = 1024
```

If you experience audio stuttering because of kernel page locking or late scheduling see [Gaming#Tweaking kernel parameters for response time consistency](../../en/Gaming.html#Tweaking_kernel_parameters_for_response_time_consistency "Gaming").

## Other issues {#Other_issues}

### Auto-switching is not working {#Auto-switching_is_not_working}

If auto-switching is not working it may be an issue with [WirePlumber](../../en/WirePlumber.html "WirePlumber") state. As suggested by [this comment](https://gitlab.freedesktop.org/pipewire/wireplumber/-/issues/191#note_1252549) you can delete [WirePlumber](../../en/WirePlumber.html "WirePlumber")\'s local state and restart the daemon to see if that helps:

    $ rm -r ~/.local/state/wireplumber/

Then [restart](../../en/Help:Reading.html#Control_of_systemd_units "Restart") the `wireplumber.service` [user unit](../../en/User_unit.html "User unit").

### Audio problems after standby {#Audio_problems_after_standby}

If the sound is missing or otherwise garbled after waking the machine up from sleep, your sound card may not have suspended correctly. A temporary fix is to restart Pipewire and Wireplumber:

    # systemctl --user restart pipewire pipewire-pulse wireplumber

### Increasing RLIMIT_MEMLOCK {#Increasing_RLIMIT_MEMLOCK}

    Dec 13 11:11:11 HOST pipewire-pulse[99999]: Failed to mlock memory 0x7f4f659d8000 32832: This is not a problem but for best performance, consider increasing RLIMIT_MEMLOCK

Install [realtime-privileges](https://archlinux.org/packages/?name=realtime-privileges) and add your own user to the `realtime` group.

Alternatively, increasing memlock from 64kB to 128kB seems enough to fix this. If you are running `pipewire-pulse` under [systemd/User](../../en/Systemd/User.html "Systemd/User"), add:

    username   soft    memlock 64
    username    hard    memlock 128

to `/etc/security/limits.d/username.conf`

### Noticeable audio delay or audible pop/crack when starting playback {#Noticeable_audio_delay_or_audible_pop/crack_when_starting_playback}

This is caused by node suspension when inactive.

With [wireplumber](https://archlinux.org/packages/?name=wireplumber), create a new file to overwrite the default configuration:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/wireplumber/wireplumber.conf.d/disable-suspension.conf (or ~/.config/wireplumber/wireplumber.conf.d/disable-suspension.conf)
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
monitor.alsa.rules = [
  {
    matches = [
      {
        # Matches all sources
        node.name = "~alsa_input.*"
      },
      {
        # Matches all sinks
        node.name = "~alsa_output.*"
      }
    ]
    actions = {
      update-props = {
        session.suspend-timeout-seconds = 0
      }
    }
  }
]
# bluetooth devices
monitor.bluez.rules = [
  {
    matches = [
      {
        # Matches all sources
        node.name = "~bluez_input.*"
      },
      {
        # Matches all sinks
        node.name = "~bluez_output.*"
      }
    ]
    actions = {
      update-props = {
        session.suspend-timeout-seconds = 0
      }
    }
  }
]
```

Restart `pipewire.service` and `wireplumber.service` to apply changes.

Instead of disabling suspension entirely, you can also change the timeout value to the desired number of seconds of delay before source suspension.

Some devices implement their own detection of silence and suspension. For them disabling node suspention alone won\'t work. It\'s possible to work around them by adding a small amount of noise, making it so the output never goes fully silent:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
.../disable-suspension.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
    session.suspend-timeout-seconds = 0,  # 0 disables suspend
    dither.method = "wannamaker3", # add dither of desired shape
    dither.noise = 2, # add additional bits of noise
...
```

It may be necessary to play with `dither.noise` and `dither.method` parameters to make it so the noise is sufficiently silent and simultaneously loud enough to prevent detection of silence. See [PipeWire documentation](https://docs.pipewire.org/page_man_pipewire-client_conf_5.html#client_conf__dither_noise).

With [pipewire-media-session](https://archlinux.org/packages/?name=pipewire-media-session):

Disable this by editing `/etc/pipewire/media-session.d/*-monitor.conf` depending on where the delay occurs and changing property `session.suspend-timeout-seconds` to 0 to disable or experiment with other values and see what works.

Alternatively you can comment out the line `suspend-node` in `/etc/pipewire/media-session.d/media-session.conf`.

[Restart](../../en/Help:Reading.html#Control_of_systemd_units "Restart") both `pipewire.service` and `pipewire-pulse.service` to apply these changes, or alternatively reboot.

### No sound until after first playback attempt {#No_sound_until_after_first_playback_attempt}

When PipeWire is started using socket activation, some PipeWire-native applications may attempt to play audio before [WirePlumber](../../en/WirePlumber.html "WirePlumber") configures the nodes, resulting in an error, for example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ mpv -v /path/to/file
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[ao/pipewire] PipeWire does not have any audio sinks, skipping
[ao] Failed to initialize audio driver 'pipewire'
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ journalctl --user -u mpd.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
output: Failed to play on "PipeWire" (pipewire): no target node available
exception: Failed to open audio output
```

As a workaround, you can [enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable") the `pipewire.service` [user unit](../../en/User_unit.html "User unit").
