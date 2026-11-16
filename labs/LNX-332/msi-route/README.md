# Lab: encode and decode x86 MSI messages

A message-signalled interrupt is a memory write whose address picks the target CPU and whose data picks the vector. KVM's routing table stores exactly these two numbers for each MSI route. `setup` writes `msi.py`; implement `encode` and `decode` following the bit layout in the file and reject values the hardware cannot express.

The layout follows the Intel and AMD manuals for the xAPIC format (to verify the level and trigger bit details against the current SDM; x2APIC and remapped formats differ).
