# LNX-402 Capstone brief: Cloud-Native Platform

## Scenario

Example Corp is moving its applications to Kubernetes and has asked you to build the platform under them. The team wants clusters it understands, changes that arrive only from Git, a rehearsed upgrade and restore, policy that blocks unsafe or unsigned workloads, visibility into every layer, and proof that the same platform works on a managed service and survives a week of abuse. You deliver the platform as a Git repository and evidence of each stage.

## What you deliver

One repository and one evidence folder, with one stage per milestone. Do the milestones in order; each builds on the one before.

| # | Milestone | Environment | Graded by |
|---|---|---|---|
| 1 | Two clusters with Cilium and Gateway API | nested VMs | lab `cluster-pair` in CI, plus your running clusters |
| 2 | GitOps with Argo CD | container (kind) or your clusters | lab `gitops-layout` in CI, plus your repository |
| 3 | Upgrade and etcd restore drill | nested VMs | lab `upgrade-plan` in CI, plus a recorded drill |
| 4 | Policy and signed images | container | lab `admission-policy` in CI, plus policy tests |
| 5 | Observability | container | lab `alert-rules` in CI, plus dashboards as code |
| 6 | Same platform on managed Kubernetes | cloud account | lab `managed-k8s-evidence` structure, plus your comparison notes |
| 7 | Week-long soak and chaos test | time | lab `soak-chaos-evidence` structure, plus your log |
| 8 | 100+ node scale test | shared hardware or simulation | lab `scale-test-evidence` structure, plus your measurements |

Each milestone page lists the lessons from earlier courses it relies on. Read those first; this course adds integration, not new theory.

## Marking rubric (100 points)

| Area | Points | Full marks |
|---|---:|---|
| Cluster build | 15 | Two clusters with distinct ranges, Cilium, a role-split gateway; a rebuild from the repository gives the same result |
| GitOps | 15 | Everything except the bootstrap is reconciled from Git; no plain secrets; sync order explicit; rollback shown by reverting a commit |
| Upgrade and restore | 15 | One minor version upgrade in the supported order and a restore from snapshot with recovery point stated |
| Policy | 10 | Pod security level, custom rules and signature verification, with tests of accept and reject |
| Observability | 10 | Metrics, traces and flows linked; alerts for missing targets and expiring certificates |
| Managed cluster | 10 | Same repository with a small documented overlay; no static keys; teardown shown |
| Soak, chaos and scale | 15 | Plan written first, honest limits, findings with owners |
| Repository quality | 10 | Small reviewed commits, README that lets a stranger rebuild, no secrets, licences stated |

Pass is 70. Anything that cannot be shown (for example a stage you could not run) must be said plainly with the reason; unconfirmed claims are marked "(to verify)" and are not marked down for that.

## Score levels

Each rubric area is marked at one of four levels, so two markers reach the same number.

| Level | Share of the area's points | What it looks like |
|---|---:|---|
| Full | 100% | Everything in the Full marks column, with evidence a stranger can check |
| Most | 70% | It works, but one element of Full marks is missing or its evidence is thin |
| Some | 40% | A design or partial build exists, but the working evidence is missing |
| None | 0% | Not attempted, or the evidence does not support the claim |

A substitute from the fallback table below is marked the same way, but cannot score above Most for that area.

## Resources and time budget

These are planning estimates, not limits. Record your actual figures in the README.

| Item | Estimate |
|---|---|
| Lab host | 32 GB RAM and 8 cores for two small clusters of three nodes each; 64 GB makes milestone 3 more comfortable |
| Time | about 140 hours: milestones 1 to 5 about 15 to 20 each, 6 about 15, 7 one calendar week plus about 15 hours of work, 8 about 15 |
| Cloud | one small managed cluster for a few days; set a spending alert and tear it down the same week, expect a few tens of US dollars |
| Scale test | 100+ nodes need shared hardware or a simulator; real nodes are not required |

## If you cannot run a milestone

| Milestone | Substitute | Area affected |
|---|---|---|
| 6 Managed Kubernetes | Apply the same overlay to a third local cluster that imitates the provider parts, and list what the real provider would change | Managed cluster |
| 7 Week-long soak | Run seventy-two hours with the same plan and chaos steps, and state the limits honestly | Soak, chaos and scale |
| 8 100+ nodes | Use a simulated-node tool (for example KWOK) and label every result as simulated | Soak, chaos and scale |

## Rules

- Original work. You may follow vendor and project documentation but write your own code and prose.
- Never commit passwords, private keys, tokens or cloud access keys.
- The grader labs are sanity checks. Passing them is necessary, not sufficient: the repository and evidence are what is marked.
- Keep a list of everything you create in a cloud account and delete it at the end of milestone 6.
- State clearly whether nodes in the scale test are real or simulated.
