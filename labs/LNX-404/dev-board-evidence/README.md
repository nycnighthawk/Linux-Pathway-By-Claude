# Guide lab: Boot your kernel and test your change on a real board

Run the work on a physical development board that you own (a common single-board computer is fine) with a serial console. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `board` | vendor and model of the board |
| `soc_arch` | CPU architecture, `uname -m` |
| `serial_console` | yes if you captured the boot log over a serial adapter |
| `baud` | serial speed |
| `logic_level_volts` | adapter signal level you confirmed in the board documentation |
| `kernel_release` | `uname -r` on the board |
| `dtb_used` | the device tree file booted |
| `boot_to_init` | yes if the log shows init starting |
| `your_change_exercised` | yes if you ran your driver or patch on the board |
| `differences_from_qemu` | count of behaviours that differed from the emulator |
| `recovery_method` | how you recover from a bad kernel |
| `boot_log_saved` | yes if the full log is kept with your notes |

## Success criteria

- You checked the board documentation for voltage and pin layout before connecting.
- You can recover from a kernel that does not boot.
- You wrote down every difference from the emulator and its cause.
- You have the boot log saved.

## Grade it

`bin/lpc course lab LNX-404 dev-board-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment H: real hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-404-T05).
