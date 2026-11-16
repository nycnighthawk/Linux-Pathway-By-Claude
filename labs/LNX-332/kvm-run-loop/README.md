# Lab: the run loop of a minimal VMM

Every KVM-based VMM is a loop around `KVM_RUN`. `setup` writes `vmm.py` with a scripted guest standing in for `struct kvm_run`. Implement `run_vm` so that serial output, port reads, an exit-code write and the terminal exits follow the rules in the file.

On a real host the same loop is a dozen lines of C around `ioctl(vcpu_fd, KVM_RUN, 0)` and a `switch` on `run->exit_reason` (see the kernel's KVM API document).
