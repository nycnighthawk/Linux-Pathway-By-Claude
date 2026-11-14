# Lab: a swap file that the kernel would accept, and a zram configuration

You will prepare a swap **file** correctly (no holes, strict mode, a label) without activating it, and write the
persistent configuration for swap on a file and for compressed swap in RAM.

## Starting state

`setup` writes a blank `answers.txt` and removes earlier results under your working directory (`$LAB_DIR`).

## Your task

1. Create `swapfile`, 64 MiB, with `dd if=/dev/zero` (a file made with `truncate` has holes and `swapon` would refuse it),
   mode `0600`, then `mkswap -L labswap swapfile`.
2. Write `fstab` with one line that activates `/swapfile` as swap with priority 10 (`defaults,pri=10`), dump and pass
   both 0, and mount point `none`.
3. Write `zram-generator.conf` with a `[zram0]` section: size half of RAM (`zram-size = ram / 2`), compression
   `zstd`, and swap priority 100 so that it fills before the disk swap.
4. Fill in `answers.txt`: the command that lists active swap areas, the command that creates and sizes a zram device,
   and the sysctl that sets how eagerly the kernel swaps (the name, not a value).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/swap-zram/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/swap-zram/check
```

## Notes

- `blkid -p swapfile` reads the swap signature without activating anything.
- `du --apparent-size` and `du` should agree for a file without holes.
- Reading material: [the lesson](lesson:LNX-103-T04). Afterwards, try [the quiz](quiz:LNX-103-T04).
