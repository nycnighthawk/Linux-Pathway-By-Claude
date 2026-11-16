# Lab (planning guide): firmware, vTPM and a confidential guest

Confidential computing needs specific CPUs, so this lab is a design exercise with a shape-checked answer. `setup` writes `requirements.txt` with two guests and the host facts.

## Your task

1. Guest A (Windows 11): fill the `a_*` keys in `report.txt` and write `guest-a.xml` with the `os`, `features` and `tpm` elements: UEFI firmware, Secure Boot, SMM on, a TPM 2.0 emulator whose state persists.
2. Guest B (untrusted-host payroll service): fill the `b_*` keys and write `guest-b.xml` with UEFI and a `launchSecurity` element for SEV-SNP (`cbitpos`, `reducedPhysBits`, hex `policy`). Say in `b_attestation_step` what happens before a secret is released.

## Success criteria

The check parses the report and both XML fragments. The attestation sentence should say what the guest presents and what the relying party does with it.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/firmware-trust-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/firmware-trust-guide/check
```

Needs `python3`. Reading: [the lesson](lesson:LNX-315-T05); then [the quiz](quiz:LNX-315-T05).
