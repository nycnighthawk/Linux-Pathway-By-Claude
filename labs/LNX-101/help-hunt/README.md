# Lab: find answers in help text and the manual

Six questions, each answerable from the machine in under a minute: from a command's built-in help, from the shell's own
knowledge, or from the standard layout of the manual. The goal is to build the habit of looking before guessing.

## Starting state

`setup` creates in your working directory (`$LAB_DIR`) a small command named `syncer` whose `--help` text describes its
options and exit statuses, and `answers.txt`, a key=value sheet with six question marks.

## Your task

Fill in `answers.txt` (keep one `key=value` per line, no spaces):

| Key | Question |
|---|---|
| `retries_default` | What is the default number of retries of `syncer`? |
| `quiet_flag` | What is the short form of its quiet option, written with its dash? |
| `config_error_exit` | Which exit status does it use when the configuration file cannot be read? |
| `help_stream` | Does `syncer --help` print to `stdout` or to `stderr`? (Redirect one of them and see.) |
| `manual_section_file_formats` | Which manual section number holds file formats such as the account database? |
| `cd_kind` | What does the shell say `cd` is: `alias`, `builtin`, `file` or `function`? |

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-101/help-hunt/setup
# ...fill in answers.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-101/help-hunt/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes.
Afterwards, use `man` or the `info` viewer to find a command's exit status section, and search the manual index for a
task you do not know the command name for.

## Notes

- `type -t NAME` prints how the shell interprets a name; `man 5 passwd` and `man passwd` open different pages.
- The container image used by the CI job may ship without manual pages, so this lab does not depend on them.
- Reading material: [the lesson](lesson:LNX-101-T10). Afterwards, try [the quiz](quiz:LNX-101-T10).
