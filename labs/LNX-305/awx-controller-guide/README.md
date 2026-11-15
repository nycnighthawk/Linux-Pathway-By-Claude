# Guide lab: run a playbook through AWX or an automation controller

A controller needs a database, a message path, container images and often a Kubernetes cluster, so it cannot be
started on a shared runner. This is a guided exercise with success criteria. Use a laptop cluster (minikube or kind with the
AWX Operator), a spare virtual machine, or a trial of Ansible Automation Platform. If you have none of these, record
`none` where the key allows it and work through the criteria on paper with the vendor documentation. The grader checks
that your report is complete and well formed; the evidence is on your controller.

## Starting state

`setup` writes `report.txt` in your working directory (`$LAB_DIR`) with ten question marks.

## Your task

| Key | How to find it |
|---|---|
| `controller_flavour` | `awx`, `aap`, `controller` (a standalone automation controller) or `none` |
| `organization` | the organization that owns the objects you created |
| `inventory_hosts` | the number of hosts in the inventory you created, or `none` |
| `credential_type` | the type of the credential attached to your job template |
| `project_scm` | `git` or `manual`: where the project gets its playbooks |
| `job_template` | the name of the template you launched |
| `execution_environment` | the container image the job ran in (shown on the job details page) |
| `job_status` | `successful`, `failed` or `none` |
| `role_granted` | the role you gave a test team on the template (`Execute` is the usual choice) |
| `check_mode_run` | `yes` if you launched one job with check mode enabled |

## Success criteria

- An organization, an inventory with at least one host, a machine credential, a project from a Git repository and a job
  template exist, and you launched the template and read its event output.
- A test user in a team with only the Execute role can launch the template but cannot read the credential secret.
- You can say which execution environment the job used and what would break if a collection were missing from it.
- You launched one job in check mode and compared it with the real run.
- You know whether your controller is upstream AWX (no support contract, releases paused at the time of writing) or a supported product.
- Every key holds a value you read yourself.

## Grade it

`bin/lpc course lab LNX-305 awx-controller-guide` checks the starting state and the structure of the sample answer; to
grade your own report run `check` with `LAB_DIR` set to the directory that holds `report.txt`.

## Notes

- This lab is not run by CI (environment S: self-hosted); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-305-T08). Afterwards, try [the quiz](quiz:LNX-305-T08).
