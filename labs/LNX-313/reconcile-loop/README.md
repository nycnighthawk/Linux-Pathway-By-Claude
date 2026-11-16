# Lab: write the reconcile function of a WebApp operator

You implement the heart of an operator without Go or a cluster: `reconciler.py` in `$LAB_DIR`, tested against a small in-memory API (`fakeapi.py`, provided).
A `WebApp` object has `spec: {image, replicas, host (optional)}`. Your `reconcile(api, ns, name)` must:

1. Return quietly if the WebApp does not exist.
2. If it is being deleted (`metadata.deletionTimestamp`): remove its uid from `api.external`, remove the finalizer `webapp.example/cleanup`, and return.
3. Otherwise make sure the finalizer is present and the uid is registered in `api.external`.
4. Ensure a Deployment and a Service named like the WebApp, each with an owner reference (`{kind: WebApp, name, uid}`); the Deployment has `spec.replicas` and `spec.image` from the WebApp.
   Ensure an Ingress with the same name exists only while `spec.host` is set (create it with `spec.host`; delete it when the host is removed).
5. Set the status through `api.update_status`: `readyReplicas` from the Deployment's status (0 if none), `observedGeneration` equal to the WebApp's generation, and a condition `{type: Available, status: "True"/"False"}` (true when `readyReplicas == replicas`).
6. Be idempotent: a second call with nothing changed must perform **no writes** (`api.writes` stays the same). Write only when something differs.

The check runs seven scenarios (create, steady state, scale, host on and off, child deleted by hand, ready status, deletion with the finalizer).

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-313/reconcile-loop/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-313/reconcile-loop/check
```

Needs `python3`. Reading: [the lesson](lesson:LNX-313-T08), then [the quiz](quiz:LNX-313-T08).
