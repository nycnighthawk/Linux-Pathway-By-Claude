# Guide lab: a field report on firmware, console and locale

Firmware and physical consoles cannot be tested from a script on a shared runner, so this is a guided exercise with
success criteria. Do it on a real machine or on a virtual machine whose firmware menu you can reach. The grader only
checks that your report is complete and well formed; the evidence is on the machine.

## Starting state

`setup` writes `report.txt` in your working directory (`$LAB_DIR`) with six question marks.

## Your task

Find each value on the machine and write it in `report.txt`:

| Key | How to find it |
|---|---|
| `boot_mode` | `uefi` if `/sys/firmware/efi` exists, otherwise `bios` |
| `secure_boot` | `mokutil --sb-state`, or the firmware menu: `enabled`, `disabled` or `unsupported` |
| `console_device` | the `console=` argument in `/proc/cmdline`; without one, the device you are looking at (`tty1`) |
| `keyboard_layout` | `localectl status`, or the layout name of the console keymap |
| `timezone` | `timedatectl`, an `Area/City` name or `UTC` |
| `firmware_menu_key` | the key shown at power-on, or the hypervisor's documentation, for entering setup |

## Success criteria

- You entered the firmware setup menu at least once, changed the boot order or a boot option, and set it back.
- You booted once with a modified kernel command line from the boot menu and saw the change in `/proc/cmdline`.
- Every key in the report holds a value you read yourself.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/console-firmware/setup
# ...fill in report.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/console-firmware/check
```

In CI the lab is skipped because it needs a person and hardware. The harness still proves, locally, that `check` fails
on the starting state and passes after `solution/apply`.

## Notes

- Reading material: [the lesson](lesson:LNX-102-T11). Afterwards, try [the quiz](quiz:LNX-102-T11).
