# Lab: show a window on a virtual display and capture it

GUI programs can be tested on a machine with no screen, if an X server renders into memory. You will finish a small Xlib
program, run it under `xvfb-run`, and prove from a screenshot that it drew what it should.

## Starting state

`setup` writes `src/app.c`, which opens the display and creates a 200x100 window but never maps it, and a blank
`answers.txt`. GTK and Qt programs follow the same pattern, but a plain Xlib program keeps the lab free of large dependencies.

## Your task

1. In `src/app.c` set the window background to red, map the window, flush the connection and wait four seconds.
   Build with `cc -o app src/app.c -lX11`.
2. Run it on a private virtual display and capture the screen:
   `xvfb-run -a -s "-screen 0 320x240x24" bash -c './app & sleep 2; import -window root shot.png; wait'`
3. Check a pixel: `convert shot.png -format '%[pixel:p{10,10}]' info:` should print `srgb(255,0,0)`.
4. Fill in `answers.txt`. Think about how the same idea applies to a GTK program (`GDK_BACKEND=x11`) and to Qt
   (`QT_QPA_PLATFORM=offscreen`).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/xvfb-gui/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/xvfb-gui/check
```

## Notes

- The lab needs `gcc`, `libx11-dev`, `xvfb` (which provides `xvfb-run`; also `xauth`) and `imagemagick`.
- Reading material: [the lesson](lesson:LNX-220-T12). Afterwards, try [the quiz](quiz:LNX-220-T12).
