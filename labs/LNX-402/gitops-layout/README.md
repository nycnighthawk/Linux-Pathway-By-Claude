# Lab: a GitOps repository layout that reconciles safely

`setup` writes a small platform repository: a root Application, an ApplicationSet for the clusters, a CRD application and a Secret. It has the defects that cause real outages: a root application pointing at a misspelt path, floating `HEAD`, sync without prune and self-heal, a cluster missing from the set, CRDs with no early sync wave, and a plain-text password in Git. Fix the files until `check` passes.

## Run it

`bin/lpc course lab LNX-402 gitops-layout`, or edit the files in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-402-T02).
