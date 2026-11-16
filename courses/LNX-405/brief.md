# LNX-405 Capstone brief: Build and Run a Hypervisor Stack

## Scenario

A company wants to own its virtualisation stack end to end: a small, auditable VMM for untrusted workloads, a single image pipeline for the three platforms its teams use, a latency-sensitive VM for one product, a passed-through accelerator for another, and a security team that understands how guests break out. You build and document each piece and contribute one test upstream.

## What you deliver

One repository and one evidence folder, with one stage per milestone. Do the milestones in order; each builds on the one before.

| # | Milestone | Environment | Graded by |
|---|---|---|---|
| 1 | A VMM that boots Linux with virtio-blk and virtio-net | nested VM | lab `vmm-layout` in CI, plus your VMM and its CI |
| 2 | One image pipeline for libvirt, VirtualBox and KubeVirt | nested VM | lab `image-pipeline` in CI, plus your pipeline runs |
| 3 | Pinned, hugepage-backed VM that meets a latency target | shared hardware | lab `latency-vm-evidence` structure, plus your measurements |
| 4 | VFIO passthrough of a real device | hardware | lab `vfio-evidence` structure, plus your notes |
| 5 | A feature or test for QEMU or KVM selftests, sent for review | people and time | lab `upstream-test-evidence` structure, plus archive links |
| 6 | VM-escape CVE analysis and mitigations write-up | container | lab `cve-writeup` in CI, plus your write-up |

Each milestone page lists the lessons from earlier courses it relies on. Read those first; this course adds integration, not new theory.

## Marking rubric (100 points)

| Area | Points | Full marks |
|---|---:|---|
| VMM and tests | 25 | Boots a guest to a shell with virtio-blk and virtio-net; every guest-supplied length and address validated; CI boots it and fails on timeout; malformed-input tests |
| Image pipeline | 15 | One source, one checksum, three targets, identical smoke tests, pinned images, no secrets |
| Latency tuning | 15 | Target written first, one change at a time, a long loaded measurement, an honest result |
| VFIO | 10 | Group understood, nothing weakened without a stated reason, device restored |
| Upstream test | 15 | Test fails without the fix, follows the project's guide, every comment answered |
| Escape analysis | 10 | Accurate, defensive, layered mitigations, no exploit code |
| Repository quality | 10 | Small reviewed commits, a README that lets a stranger rebuild each stage, licences stated |

Pass is 70. Anything that cannot be shown (for example a stage you could not run) must be said plainly with the reason; unconfirmed claims are marked "(to verify)" and are not marked down for that.

## Rules

- Original work. You may follow vendor and project documentation but write your own code and prose.
- Never commit passwords, private keys, tokens or cloud access keys.
- The grader labs are sanity checks. Passing them is necessary, not sufficient: the repository and evidence are what is marked.
- Choose C or Rust for the VMM; the graders are language-neutral models of the same logic.
- Use only a vulnerability that is public and fixed in the write-up, and include no exploit code.
- Do not pass through a device the host depends on.
