# Lab: one image, three platforms

`setup` writes `pipeline.yaml`, the description of an image pipeline that should build one source image and deliver it to libvirt (qcow2), VirtualBox (VDI or VMDK) and KubeVirt (a container disk). It has the usual defects: no checksum, no first-boot seed, a raw VirtualBox format, a floating container tag, the wrong owner for the disk file, and different smoke tests per platform. Fix it until `check` passes. The sample checksum in the solution is a placeholder, not the hash of a real image.

## Run it

`bin/lpc course lab LNX-405 image-pipeline`, or edit `pipeline.yaml` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-405-T02).
