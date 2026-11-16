# Lab: the device side of a split virtqueue

`setup` writes `virtq.py` with a descriptor table, an available ring and a handler callback. Implement `process`: consume new available entries (with 16-bit index wrap), follow each chain, total the readable and writable bytes, report the used length, and refuse malformed chains (a `next` loop or an index outside the table) instead of hanging.

The guest controls every number the device reads, so the validation is the security-relevant part of a real back end.
