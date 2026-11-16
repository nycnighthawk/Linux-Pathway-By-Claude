# Lab: a Deployment that passes the restricted level

Write `deploy.yaml` (a Deployment named `api` in namespace `shop`) and `answer.txt` in `$LAB_DIR`.

The Deployment must have:
- Pod template annotation `checksum/config` (any non-empty value).
- `automountServiceAccountToken: false`.
- Pod security context: `runAsNonRoot: true`, `runAsUser: 10001`, `seccompProfile.type: RuntimeDefault`.
- One container `api` (image `registry.example/api:2.1`) with `allowPrivilegeEscalation: false`, `capabilities.drop: [ALL]`, `readOnlyRootFilesystem: true`.
- Environment variable `LOG_LEVEL` from key `log-level` of ConfigMap `api-config` (`configMapKeyRef`).
- Secret `api-db` mounted as a volume at `/etc/secrets`, `readOnly`, `defaultMode: 0400` (256 decimal).
- An `emptyDir` volume mounted at `/tmp`.
- Resources: requests cpu `250m` and memory `256Mi`; limits memory `256Mi` and **no CPU limit**.

`answer.txt` holds one line `qos=<Guaranteed|Burstable|BestEffort>` for the Pod this produces.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-313/restricted-deployment/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-313/restricted-deployment/check
```

Needs `python3` and `PyYAML`. Reading: [the lesson](lesson:LNX-313-T02), then [the quiz](quiz:LNX-313-T02).
