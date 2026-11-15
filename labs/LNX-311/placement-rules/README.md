# Lab: placement rules and autoscaling for three workloads

Three manifests in your working directory (`$LAB_DIR`) are incomplete. Complete them.

## Starting state

`setup` writes `gpu-job.yaml`, `web.yaml` and `hpa.yaml` with missing placement rules, and `replicas.txt` with a question.

## Your task

1. `gpu-job.yaml`: the pod must tolerate the taint `dedicated=gpu:NoSchedule` and require nodes labelled `pool=gpu` (a `nodeSelector`).
2. `web.yaml`: containers must have CPU and memory requests equal to limits (Guaranteed QoS), and a topology spread constraint over `topology.kubernetes.io/zone` with `maxSkew: 1` and `whenUnsatisfiable: ScheduleAnyway`.
3. `hpa.yaml`: an `autoscaling/v2` HPA for Deployment `web` with `minReplicas: 3`, `maxReplicas: 12`, CPU utilisation target 70, and a scale-down stabilisation window of 300 seconds.
4. `replicas.txt`: replace `answer=` with the HPA's desired replica count for the data in the file.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/placement-rules/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/placement-rules/check
```

Needs Python 3 with PyYAML. Reading: [the lesson](lesson:LNX-311-T05); then [the quiz](quiz:LNX-311-T05).
