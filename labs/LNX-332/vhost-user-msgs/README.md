# Lab: parse a vhost-user message stream

vhost-user sends the virtio control plane over a Unix socket: a 12-byte header (request, flags, payload size) plus a payload; descriptors travel as ancillary data and are not modelled here. `setup` writes `vhostmsg.py`. Implement `parse` (with strict validation) and `negotiate` (feature intersection and the protocol-features bit).

The message numbers and flag layout follow the protocol document (to verify against the current version). A back end that trusts the size field or the version is a bug.
