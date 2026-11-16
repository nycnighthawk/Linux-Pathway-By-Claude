# LNX-401 Capstone brief: Enterprise Estate as Code

## Scenario

You are the new platform engineer at Example Corp. The company runs a FreeIPA-based IdM domain for Linux and keeps a separate Active Directory forest for Windows. Today nobody can say what servers exist, how they were built or whether a rebuilt host would behave like the old one. The board wants the whole estate described in a Git repository, a rehearsed lifecycle for every host, a month of evidence that it can be operated, a cloud extension, and a written review of any incident along the way.

## What you deliver

One repository, six milestones, each with evidence. Do the milestones in order; each builds on the one before.

| # | Milestone | Environment | Graded by |
|---|---|---|---|
| 1 | IdM, Samba AD, six mixed servers, repository, monitoring | nested VM | lab `estate-model` in CI, plus your running estate |
| 2 | The same estate against a genuine Windows AD with a trust | self-provided | lab `ad-trust-evidence` structure, plus your notes and trace files |
| 3 | Provision, harden, patch, upgrade, decommission | nested VM | lab `host-lifecycle` in CI, plus a recorded run |
| 4 | Thirty days of operations | time | lab `ops-log-30d` structure, plus your daily log |
| 5 | The baseline in a public cloud | cloud account | lab `cloud-baseline-evidence` structure, plus teardown proof |
| 6 | Post-incident review | container | lab `incident-review` in CI, plus the review text |

Each milestone page lists the lessons from earlier courses it relies on. Read those first; this course adds no new theory, only the integration.

## Marking rubric (100 points)

| Area | Points | Full marks |
|---|---:|---|
| Estate description and build order | 20 | One inventory is the single source of truth; the stage order is explicit; a clean rebuild from the repository gives the same estate |
| Identity correctness | 15 | Samba and IdM both work; the trust is tested in layers; the genuine AD run has trace evidence |
| Lifecycle | 20 | All four actions are scripted with preconditions and checks; decommission leaves nothing in directory, CA, DNS, monitoring or inventory |
| Operations | 15 | A full month of log, objectives written first, at least one repeated manual task automated, weekly handovers |
| Cloud extension | 10 | Provider parts separated from estate parts; no secrets in the repository; teardown proven |
| Incident review | 10 | Blameless, numerically consistent, every cause has an owned action |
| Repository quality | 10 | Small reviewed commits, a README that lets a stranger rebuild, no secrets, licences stated |

Pass is 70. Anything that cannot be shown (for example a stage you could not run) must be said plainly with the reason; unconfirmed claims are marked "(to verify)" and are not marked down for that.

## Rules

- Original work. You may follow vendor documentation but write your own code and prose.
- Never commit passwords, keytabs, private keys or cloud access keys. Use a secrets tool.
- Keep a list of everything you built in the cloud and delete it at the end of milestone 5.
- Use the grader labs as sanity checks. Passing them is necessary, not sufficient.
