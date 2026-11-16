# Guide lab: Evidence for the platform on managed Kubernetes

Deploy the same GitOps-defined platform to a managed Kubernetes service in a cloud account that you own, compare it with the self-built clusters, and remove it. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `provider` | the managed service you used |
| `kubernetes_minor` | minor version of the managed cluster, `kubectl version`, e.g. 31 |
| `self_built_minor` | minor version of your kubeadm clusters |
| `gitops_bootstrap_ok` | yes if the controller synced the platform repository without manual kubectl apply of platform parts |
| `shared_checks_passed` | number of checks from your self-built suite that passed unchanged |
| `shared_checks_total` | total checks in the suite |
| `overlay_differences` | number of settings that had to live in a provider overlay |
| `workload_identity` | yes if workloads reach cloud APIs without static keys |
| `static_keys_in_repo` | yes if any long-lived cloud key is in Git; you want no |
| `overlapping_addons` | add-ons the provider installs that duplicate yours |
| `hourly_cost_usd` | cost per hour of the running cluster from the billing console |
| `teardown_verified` | yes if a listing by tag shows nothing left |

## Success criteria

- The platform repository is the same commit on all three clusters except for the overlay.
- You wrote down each overlay setting and why it is provider specific.
- Costs were limited with a budget alert before the cluster was created.
- You tore everything down and listed by tag to prove it.

## Grade it

`bin/lpc course lab LNX-402 managed-k8s-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment K: a cloud account); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-402-T06).
