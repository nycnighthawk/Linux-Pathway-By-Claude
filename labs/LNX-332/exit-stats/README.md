# Lab: rank VM exits and choose the first action

`setup` writes `exits.txt`, a summary in the style of `perf kvm stat report`, and an empty `report.txt`. Fill in the report: total exits, the top reason by count, the top reason by time (guest idle `HLT` excluded), its share of non-idle time, and the first action to try.

The mapping is a rule of thumb: `EPT_VIOLATION` suggests huge pages or pre-faulting, I/O and MMIO exits suggest ioeventfd or an in-kernel back end, APIC MSR writes and external interrupts suggest interrupt virtualisation, `HLT` suggests halt polling. Real systems need more evidence than a single table.
