# Lab: write and check KubeVirt manifests offline

A cluster is not required. You write a `VirtualMachine` that uses an instance type, a preference, an imported data volume and a cloud-init seed, plus a migration object, and answer five architecture questions. A PyYAML checker reads the files.

## Your task

`setup` writes `requirements.txt` with the exact requirements. Create `vm.yaml` and `migrate.yaml` and fill `report.txt`.

If you have a cluster with KubeVirt, apply the manifests and watch `kubectl get dv,vm,vmi,vmim`.

## Success criteria

The checker confirms the run strategy, the instance type and preference references, the data volume source and access mode, the volumes and disks, the masquerade network, the label and the migration object, then the report answers.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/kubevirt-vm-manifest/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/kubevirt-vm-manifest/check
```

Needs `python3` and PyYAML. Reading: [the lesson](lesson:LNX-315-T09); then [the quiz](quiz:LNX-315-T09).
