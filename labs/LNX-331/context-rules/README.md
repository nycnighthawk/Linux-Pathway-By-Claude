# Lab: what may run in which context?

Kernel code runs in different **contexts**, and each forbids some operations. The rules below are the ones in the kernel's driver documentation; this lab tests whether you can apply them (to verify specifics for your kernel version).

## Facts

- `hardirq` (interrupt handler), `softirq` (including tasklets and network receive) and `timer` callbacks (which run in softirq context) are *atomic*: they cannot sleep.
- A `workqueue` item runs in a kernel thread; a `threaded_irq` handler runs in its own thread; `syscall` is code running for a user process. These may sleep.
- Sleeping operations: `msleep`, `mutex_lock`, an allocation with `GFP_KERNEL` (it may wait for memory).
- `GFP_ATOMIC` allocations and `spin_lock_irqsave` are legal anywhere.
- `copy_to_user` needs a user address space and may fault and sleep, so it is only valid in the context of the calling user process.

## Your task

Fill every line of `allowed.txt` with `yes` or `no`, and choose a mechanism for each of the four scenarios in `choices.txt`.
