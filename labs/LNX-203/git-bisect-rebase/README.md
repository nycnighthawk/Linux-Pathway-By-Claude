# Lab: find a regression with bisect, then ship a clean fix

Your clone in `work/` has ten commits. The tag `v1.0` marks a commit known to be healthy, and `./test.sh` exits 0 while the configuration is healthy. Somewhere after `v1.0` a commit broke it. While you were busy, a teammate pushed one more commit to `origin/main`.

## Starting state

`setup` creates a bare repository `origin.git` and a clone `work/` (with a local identity configured) in your working directory (`$LAB_DIR`).

## Your task

1. Find the first bad commit with `git bisect` (`git bisect run ./test.sh` does it unattended) and write its **full hash** into `bad_commit.txt` in the lab directory (next to `work/`, not inside it). Then run `git bisect reset`.
2. In `work/`, create the branch `feature/fix-bug` and commit a fix that removes the faulty line from `app.conf`. The commit message needs a subject of at most 50 characters, no trailing period, then a blank line and a short body that says why.
3. Fetch, then **rebase** the branch onto the current `origin/main` (no merge commits).
4. Push the branch to `origin` with `git push -u origin feature/fix-bug`.

## Grade it

`bin/lpc course lab LNX-203 git-bisect-rebase` runs the whole cycle. To grade your work run `check` with `LAB_DIR` set to the directory that holds `work/` and `origin.git`.

## Notes

- `git bisect start BAD GOOD` marks both ends in one command; `git rev-parse refs/bisect/bad` prints the hash it found before you reset.
- `git commit -m "subject" -m "body"` writes a two-paragraph message.
- If you need to start over, run `setup` again; it recreates everything.
- The lab needs the package `git`.
- Reading material: [the lesson](lesson:LNX-203-T06). Afterwards, try [the quiz](quiz:LNX-203-T06).
