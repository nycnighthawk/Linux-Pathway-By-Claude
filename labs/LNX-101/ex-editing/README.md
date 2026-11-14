# Lab: edit a file with an ex script

You rarely need a full-screen session to change a file in a predictable way. Vim can run in a silent, non-interactive
mode that reads colon commands from a file, which is how the same edit can be repeated, reviewed and automated. You
will write that script, answer three questions about nano's shortcut bar, and set the default editor.

## Starting state

`setup` creates in your working directory (`$LAB_DIR`):

- `before.txt`, a small configuration file;
- `keys.vim`, `nano_keys.txt` and `editor.env`, each with comments and a TODO.

## Your task

1. Write `keys.vim`: one ex command per line, run by Vim against a copy of `before.txt`, so that the result is exactly:
   - every line that contains the word "debug" in any letter case is gone;
   - the port `8080` is `9090`;
   - every `old.example.com` is `new.example.org`;
   - no line has trailing blanks;
   - a final line `[extra]` is added at the end of the file;
   - the buffer is written and Vim quits.
2. In `nano_keys.txt`, give the keys, written as `^` plus a letter, for write out (save), exit and search.
3. In `editor.env`, write one line that exports `EDITOR` as `vim` or `nano`.

The grader runs `vim -Es -u NONE -N work.txt < keys.vim` on a copy of `before.txt`. Test it yourself the same way.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-101/ex-editing/setup
# ...write the three files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-101/ex-editing/check
```

In CI the harness runs `setup`, proves `check` fails, copies `solution/` over the work directory, and proves `check` passes.
Afterwards, open `before.txt` in Vim and make the same changes with normal-mode commands, counting keystrokes, then
compare the two approaches.

## Notes

- The lab needs the `vim` package (a minimal `vi` may lack some commands).
- Reading material: [the lesson](lesson:LNX-101-T07). Afterwards, try [the quiz](quiz:LNX-101-T07).
