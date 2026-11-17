# Course content review before v1.0

Date: 2026-11-17. Scope: all 33 built courses (LNX-101 to LNX-332 and the capstones LNX-401 to LNX-405): 330 lesson pages, 1,751 quiz questions, 330 labs and five capstone briefs.

This review checks each course for breadth, depth, clarity, correctness, structure, active learning, the exercises (breadth, depth, relevance, answers and explanations) and capstone difficulty. Each finding names a course and a file. The **Status** column says whether this branch fixes it ("Fixed") or leaves it for later ("Open").

## Summary

The material is broad and mostly accurate. Every course maps to its taxonomy topics, every lesson has a lab and a quiz, and `lpc course check` passes. LNX-101, LNX-204, LNX-220 and LNX-301 to LNX-305 read best: they explain the reasoning, work an example and list failure patterns.

The weak points fall into five groups:

1. **Quizzes could be passed by test-taking tricks rather than knowledge.**
   - In most courses the correct answer sat at one position. In LNX-309 it was always choice A. In LNX-311, LNX-314, LNX-315 and LNX-330 it was always choice B. In LNX-312 it was always A.
   - In 73% of all questions the correct answer was clearly the longest choice. The worst cases were LNX-309 (36 of 37 questions), LNX-306 (96%) and LNX-304 (95%).
2. **Some facts were wrong or stale.** Ten corrections were needed. Three of them would mislead a working admin:
   - the GRUB UEFI path (LNX-102)
   - the fencing-delay placement (LNX-309)
   - the Microsoft Secure Boot certificate status after the 2026 expiry (LNX-303)
3. **Three kernel and virtualisation courses had almost no active learning.**
   - LNX-330 had self-check questions in only 2 of its 11 lessons.
   - LNX-331 and LNX-332 had none.
   - No lesson in any course gave answers to its self-check questions.
4. **The capstone briefs had problems:**
   - They gave only a "full marks" description for each rubric area, so there were no levels in between.
   - They gave no resource or time budget, and only a vague rule for milestones the learner cannot control.
   - The course site never published the briefs, so a learner on the site could not see the rubric.
5. **Depth varies.**
   - LNX-102, LNX-103, LNX-104 and LNX-201 to LNX-203 are accurate but read like reference cards, at about 80 to 115 words per course hour.
   - LNX-313, LNX-309 and LNX-332 are thin for their stated hours.
   - Readers are sent to the topic syntheses for depth, but those syntheses are not published on the course site.

This branch fixes groups 1 to 4 where that can be done mechanically or with bounded writing. Group 5, and finishing the work on answer-length cues, need authoring time. They are listed below as open items for after v1.0.

## Metrics

Words per hour = lesson words divided by course hours. Longest-answer share = the share of single-answer questions where the correct choice is at least 1.3 times longer than any other choice, measured after this branch. Lower is better; about 25% would be chance.

| Course | Hours | Lessons | Lesson words | Words/hour | Quiz questions | Labs | Longest-answer share |
|---|---:|---:|---:|---:|---:|---:|---:|
| LNX-101 | 40 | 10 | 9711 | 242 | 70 | 10 | 52% |
| LNX-102 | 60 | 11 | 5340 | 89 | 69 | 11 | 52% |
| LNX-103 | 50 | 11 | 5799 | 115 | 72 | 11 | 68% |
| LNX-104 | 30 | 6 | 3322 | 110 | 42 | 6 | 61% |
| LNX-201 | 50 | 9 | 4527 | 90 | 63 | 9 | 50% |
| LNX-202 | 60 | 11 | 5355 | 89 | 77 | 11 | 51% |
| LNX-203 | 50 | 7 | 3872 | 77 | 49 | 7 | 55% |
| LNX-204 | 60 | 11 | 6732 | 112 | 64 | 11 | 85% |
| LNX-220 | 60 | 12 | 7178 | 119 | 60 | 12 | 73% |
| LNX-301 | 60 | 10 | 5471 | 91 | 70 | 10 | 88% |
| LNX-302 | 50 | 10 | 6946 | 138 | 70 | 10 | 85% |
| LNX-303 | 60 | 11 | 7347 | 122 | 77 | 11 | 89% |
| LNX-304 | 50 | 10 | 4878 | 97 | 61 | 10 | 95% |
| LNX-305 | 60 | 9 | 6974 | 116 | 60 | 9 | 70% |
| LNX-306 | 60 | 11 | 5074 | 84 | 66 | 11 | 96% |
| LNX-307 | 50 | 10 | 5645 | 112 | 67 | 10 | 70% |
| LNX-308 | 40 | 8 | 4992 | 124 | 48 | 8 | 83% |
| LNX-309 | 40 | 6 | 3196 | 79 | 37 | 6 | 0% (was 97%) |
| LNX-310 | 50 | 11 | 7613 | 152 | 66 | 11 | 66% |
| LNX-311 | 70 | 12 | 5994 | 85 | 61 | 12 | 53% |
| LNX-312 | 50 | 13 | 5570 | 111 | 65 | 13 | 69% |
| LNX-313 | 50 | 10 | 3652 | 73 | 50 | 10 | 67% |
| LNX-314 | 45 | 10 | 5193 | 115 | 50 | 10 | 55% |
| LNX-315 | 60 | 11 | 5471 | 91 | 55 | 11 | 68% |
| LNX-320 | 70 | 13 | 6958 | 99 | 78 | 13 | 86% |
| LNX-330 | 40 | 11 | 5569 | 139 | 67 | 11 | 80% |
| LNX-331 | 60 | 13 | 6356 | 105 | 77 | 13 | 77% |
| LNX-332 | 48 | 12 | 4328 | 90 | 60 | 12 | 80% |
| LNX-401 to 405 | 80 to 140 | 6 to 8 | 1334 to 1804 | 11 to 16 | none | 6 to 8 | n/a |

Notes on the table:

- Low words per hour is expected for the capstones, which are project time.
- For the 1xx to 3xx courses, the time goes to labs and the syntheses. Even so, 73 to 90 words per hour (LNX-313, LNX-203, LNX-309, LNX-306, LNX-311, LNX-332) is thin for a 40 to 70 hour course.

## Findings by severity

### Critical: wrong facts that would mislead an administrator

| # | Course and file | Finding | Status |
|---|---|---|---|
| C1 | LNX-102 `lessons/LNX-102-T04.md` | The lesson told learners to run `grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg` on UEFI. On RHEL 9 and later, and Fedora 34 and later, that file is a stub that loads `/boot/grub2/grub.cfg`. Overwriting it leaves a menu that later kernel updates no longer maintain. | Fixed: one command for BIOS and UEFI, and a note on the stub |
| C2 | LNX-309 `lessons/LNX-309-T06.md`, `quizzes/LNX-309-T06.yaml` (`delay`), lab `power-fencing-plan`, `synth/LNX-309/LNX-309-T02.md` and `-T06.md` | The material said to put `pcmk_delay_base` on the device that fences the node you are willing to lose. The delay applies to fencing actions that *target* that node, so the delayed node gets time to fence its peer and survives. The advice was therefore backwards. Red Hat's own wording ("a delay on one node makes that node more likely to be fenced") is easy to misread in the same way. | Fixed in the lesson, quiz, lab check, lab solution and both syntheses. Before release, confirm with a two-node test (cut the link, watch which node is fenced) |
| C3 | LNX-303 `lessons/LNX-303-T03.md` | The lesson said Microsoft's 2011 Secure Boot certificates are "due to be replaced". They reached their expiry dates in 2026. | Fixed. The lesson now explains that firmware does not check expiry, that the real risk is a db without the 2023 CA, and how to check and update it. Exact dates are still marked (to verify) |

### High: errors in teaching or assessment

| # | Course and file | Finding | Status |
|---|---|---|---|
| H1 | All 28 taught courses, `quizzes/*.yaml` | The correct answer sat at one position. Examples: LNX-309 always A, LNX-311, LNX-314, LNX-315 and LNX-330 always B, LNX-312 always A. Overall, 74% of answers were at A or B. | Fixed. The choices in 1,545 questions were shuffled deterministically, and lettered explanations ("A) correct: ...") were re-lettered with them. Questions whose choices refer to other choices ("Both", "All of the above") or whose explanations name an option by its position were left in place. Each course is now between 27% and 40% on its most common position (LNX-309 is 25%). `lpc course check` now warns if one position holds more than 45% of a course's answers |
| H2 | 25 courses, `quizzes/*.yaml` | The correct answer is clearly the longest choice in 73% of questions, so test-wise learners can pass without the knowledge. | Partly fixed. LNX-309 was rewritten: new, plausible distractors of similar length, with each wrong choice explained. Its share fell from 97% to 0%. **Open** for the others; LNX-306, LNX-304, LNX-303, LNX-301, LNX-320, LNX-204 and LNX-302 (85 to 96%) are the first to tackle |
| H3 | LNX-330 (9 of 11 lessons), LNX-331 (all 13), LNX-332 (all 12) | These lessons had no self-check, and ended in a bare "Lab" paragraph without links to the lab and quiz. | Fixed. Each of the 34 lessons now has three or four self-check questions with answers, and a "Do the lab, then the quiz" section that links both |
| H4 | All taught courses | No lesson gave answers to its self-check questions, so a learner could not tell whether their answer was right. | Fixed for the 34 lessons above. **Open** for the rest. Adding an answers block to the roughly 290 other lessons is the single biggest gain in active learning still available |
| H5 | LNX-401 to LNX-405 `brief.md` | The rubric gave only a "full marks" description per area. There were no levels in between, so two markers could give very different scores. | Fixed. A common four-level scale (Full 100%, Most 70%, Some 40%, None 0%) was added to every brief |
| H6 | LNX-401 to LNX-405 `brief.md` | No hardware, time or cost budget was given. LNX-401 needs about eleven VMs. LNX-404 and LNX-405 need hardware and outside reviewers. The only fallback rule was "say it plainly", which did not say how a substitute is marked. | Fixed. Each brief now has a resources and time budget and a fallback table for milestones outside the learner's control (genuine AD, cloud, 30 days, a week-long soak, 100+ nodes, real users, upstream review, a board, a multi-day fuzzing run, a VFIO device, VirtualBox). A substitute is capped at the "Most" level, and passing stays achievable |
| H7 | `tools/lpc/course_site.py` | The capstone briefs, which hold the scenario and the rubric, were never rendered to the course site. Milestone pages said "See the brief for the rubric." with no link. | Fixed. The site now builds `brief.html` and links it from the course page. All 32 milestone pages link to it |
| H8 | LNX-330 `lessons/LNX-330-T01.md` | The worked example used `git tag --contains <mainline commit>` to see whether a stable kernel has a fix. Stable backports are new commits with new IDs, so that command never finds them. | Fixed in the lesson, the synthesis and the lab README: find the backport with `git log --grep=<id>` on the stable branch first, because backports record "commit <id> upstream". The lab data is unchanged; it now stands for the backport's tags |

### Medium: precision, consistency and structure

| # | Course and file | Finding | Status |
|---|---|---|---|
| M1 | LNX-102 `lessons/LNX-102-T03.md` | The lesson said `Requires=` means "fail or stop if it fails". In fact a failed start only blocks the dependent unit when `After=` is also set, and an explicit stop or restart of the required unit is passed on. `BindsTo=` was missing. | Fixed |
| M2 | LNX-204 `lessons/LNX-204-T06.md` | The example ruleset accepted ICMPv6 but no ICMPv4, although the text warns that dropping ICMP breaks transfers. The text also said to drop forwarded traffic, but the example had no `forward` chain. | Fixed: ICMPv4 essentials accepted, and a `forward` chain with policy drop |
| M3 | LNX-301 `lessons/LNX-301-T04.md` | "Samba has no global catalog" is inaccurate. Samba serves one on port 3268, but it lacks the RFC 2307 attributes by default, which is why `ad_enable_gc = False` is used. | Fixed in the lesson and in the quiz question `samba-gc` |
| M4 | LNX-302 `lessons/LNX-302-T09.md` | Self-check question 4 asked why to *leave* NFSv3 enabled on a Kerberos server, while the lesson says to disable it. | Fixed: the question now asks why to disable it |
| M5 | LNX-220 `lessons/LNX-220-T03.md` | Self-check question 4 asked about `Requires:` in `.pc` files, which the lesson did not teach. | Fixed: the example and text now cover `Requires:` and `Requires.private:` |
| M6 | LNX-104 `lessons/LNX-104-T03.md` | `dnf config-manager --set-enabled` is DNF 4 syntax and fails on Fedora 41 and later, which use DNF 5. | Fixed: DNF 5 form added |
| M7 | 44 questions in LNX-102, LNX-103, LNX-104, LNX-201 and LNX-202 | The explanations had fewer than six words (for example "profile followed by the name."), so they did not say why the answer is right. | Fixed: all 44 rewritten. `lpc course check` now warns on explanations under six words |
| M8 | LNX-102, 103, 104, 201, 202, 203 | No lesson has a worked example. LNX-204, LNX-220 and most 3xx courses have one per lesson. | Open: add one short scenario per lesson |
| M9 | LNX-204, 220, 301, 303, 304, 306, 308, 311 to 314 | There is no "common failure patterns" section, or it is named differently ("Common mistakes", "What goes wrong"). The build plan's lesson template names it. | Open: rename for consistency, and add it where missing |
| M10 | All courses | Almost no quiz question is a scenario ("a host shows X; what do you check first?"). Nearly all are recall. | Open: aim for about one scenario question in three, starting with the 3xx operations courses |
| M11 | LNX-302 T08 and LNX-305 T09 | Both teach Ansible for Windows with overlapping content. | Open: keep the depth in LNX-305 and cross-link it from LNX-302 |
| M12 | All courses | Lessons say "This lesson follows the topic synthesis `synth/...`", but the course site does not publish the syntheses, so readers of the site cannot follow that pointer. | Open: decide whether to publish the syntheses or drop the pointer (an owner decision on audience and licence) |
| M13 | LNX-331 `lessons/LNX-331-T03.md`, `-T04.md` | The examples use `pcim_iomap_regions` / `pcim_iomap_table` and `del_timer_sync`. Recent kernels deprecate them in favour of `pcim_iomap_region` and `timer_delete_sync`. | Open: add a version note (to verify against the kernel the course targets) |
| M14 | LNX-332 `lessons/LNX-332-T05.md` | The vhost-user setup list omits the protocol-feature negotiation (`GET_PROTOCOL_FEATURES`, `SET_PROTOCOL_FEATURES`), and real front ends often send `SET_OWNER` before `SET_FEATURES`. | Open |

### Low: polish

| # | Course and file | Finding | Status |
|---|---|---|---|
| L1 | Most lessons in LNX-330 to LNX-332 and the capstones | The header boilerplate "(to verify)" appears on every page, which dilutes the marker for real uncertainties. | Open: keep the marker only on specific claims |
| L2 | LNX-102 `quizzes/LNX-102-T09.yaml` (`dir`) | Newer TuneD releases also read `/etc/tuned/profiles`. | The explanation now says so (to verify) |
| L3 | LNX-104 `lessons/LNX-104-T04.md` | RHEL 10 delivering Firefox and Thunderbird as Flatpaks needs a release-notes check. | Marked |
| L4 | LNX-202 `lessons/LNX-202-T05.md` | "The control agent exists before 3.1.8" was an oddly specific claim. | Reworded to the deprecation in Kea 3.x (to verify) |

## Capstone difficulty

| Capstone | Hours | Verdict before | After this branch |
|---|---:|---|---|
| LNX-401 Enterprise estate | 120 | Fair in scope, but needs about eleven VMs, a genuine AD and thirty days, with no budget or fallback | Budget given (64 GB host, or 32 GB with four members). Fallbacks: Samba as the trust partner, 14 days, a local cloud image |
| LNX-402 Kubernetes platform | 140 | The hardest. A 100+ node scale test and a week of soaking are not realistic for one learner | KWOK simulation allowed if labelled; 72-hour soak; a local stand-in for the managed cluster |
| LNX-403 Linux service product | 80 | Reasonable, but "releases and user issues" depends on real users | A peer files the issues; at least three releases over four weeks |
| LNX-404 Kernel contribution | 100 | Upstream review and a real board are outside the learner's control | A mock review if the list is silent; QEMU `virt` in place of a board; a 12-hour fuzz run |
| LNX-405 Virtualisation engineering | 120 | VFIO needs a spare device, and VirtualBox has thin sources | Nested vIOMMU passthrough allowed; VirtualBox target may be dropped with a reason |

The milestone pages are short (about 200 words: goal, prerequisites, steps, acceptance). That works for capstones because they reuse earlier lessons. Still, each page should get one "common traps" line, and the acceptance criteria should name the evidence file the grader reads. **Open.**

The graders for environments O, S, K and H check only that the evidence files have the right structure (for example `labs/LNX-401/ops-log-30d`), so the marking depends on human review. The briefs already say that passing a grader is necessary but not sufficient, and this branch leaves that unchanged.

## Thin sources and claims to verify

Where the sources are thin:

- **VirtualBox.**
  - LNX-315-T07 rests on project pages and news sites (cyberus-technology.de, linuxiac.com) for the KVM backend.
  - LNX-332-T10 and T11 have no catalogued source, only web citations, so their claims rest on project pages alone.
  - LNX-405 milestone 2 inherits this.
  - Action: re-check `VBoxManage` syntax, the state of the KVM backend and the `kvm.enable_virt_at_load` kernel version against current Oracle and kernel documentation before release.
- **Kernel API names** in LNX-331 change between releases (see M13).

Specific claims still marked (to verify) in lesson text, apart from the header boilerplate:

- LNX-202-T05: the Kea control agent deprecation and removal version.
- LNX-302-T06: PowerShell 7.6 LTS on .NET 10.
- LNX-302-T07: Point and Print defaults after PrintNightmare.
- LNX-302-T08: the `win_dsc` resource ecosystem.
- LNX-302-T10: Windows directory hardening enforcement phases.
- LNX-303-T03: the exact Secure Boot certificate dates.
- LNX-303-T04: the IMA script-execution mitigation.
- LNX-303-T09: OpenBao and Vault compatibility.
- LNX-305-T08: the state of AWX releases (24.6.1).
- LNX-306-T07: IPMI cipher suite 17 per vendor.
- LNX-306-T10: cloud swap guidance.
- LNX-306-T11: BMC dual-image fallback.
- LNX-308-T07: the nested CPU model flags.
- LNX-308-T08: Proxmox and oVirt facts.
- LNX-309-T06: the fencing-delay direction (see C2).
- LNX-312-T09: Linkerd distribution terms and Istio ambient gaps.
- LNX-313-T01: the native sidecar requirements.
- LNX-315-T07: the kernel version for `enable_virt_at_load`.

## What changed in this branch

- **Quizzes.**
  - Choices shuffled in 1,545 questions, with lettered explanations remapped. Every lettered explanation still agrees with its answer key; 957 were checked by script.
  - 44 explanations rewritten.
  - All 37 LNX-309 questions rewritten with balanced distractors.
- **Lessons.** Corrections C1 to C3, H8 and M1 to M6 (including the matching synthesis text for C2 and H8), and self-checks with answers in 34 lessons.
- **Capstones.**
  - Score levels, resource budgets and fallback tables in all five briefs.
  - All 32 milestone pages link to the brief.
  - The brief is published on the course site.
- **Tooling (`tools/lpc/course.py`).** `lpc course check` now:
  - warns on answer-position skew and on explanations under six words;
  - fails when a lettered explanation calls a different choice correct than the answer key does.

## Recommended order for the open items

1. H2: rewrite distractors course by course, starting with the 85 to 96% courses. It takes about two hours per course.
2. H4: add self-check answers to the remaining lessons.
3. M8 and M10: worked examples in the 1xx and 2xx courses, and scenario questions in the 3xx courses.
4. M12: decide whether the syntheses are published.
