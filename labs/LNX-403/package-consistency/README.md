# Lab: four package formats that agree

`setup` writes the packaging of one service in four formats: an RPM spec, a Debian directory, a Flatpak manifest and a Containerfile, plus a `VERSION` file. They disagree and are missing things: versions drift, the Flatpak source has no checksum, the Debian control lacks dependency substitution and copyright, and the image uses a floating base, one stage and root. Fix them until `check` passes. (The placeholder checksum in the sample solution is not a real hash; in your own work compute it from the release tarball.)

## Run it

`bin/lpc course lab LNX-403 package-consistency`, or edit the files in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-403-T03).
