# Lab: a two-dimensional page walk

With nested paging, every guest page-table address is itself translated by the hypervisor's tables. `setup` writes `eptwalk.py`, a toy with two levels on each side. Implement `ept_walk` and `translate`, counting each table entry read.

Why it matters: with two levels each, a walk costs 8 reads instead of 2; with four levels each it is 24. That is why huge pages and TLB tags matter, and an EPT violation is how the hypervisor learns that a guest-physical page has no host backing.
