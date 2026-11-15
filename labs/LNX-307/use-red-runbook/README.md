# Lab: read a host with USE and write the runbook

A recorded snapshot of a host and a summary of a service are in your working directory. You will apply the USE and RED methods by reading, then write a short runbook for the alert that the snapshot would trigger. Nothing here touches the host.

## Starting state

`setup` writes `snapshot.txt` (utilisation, saturation and errors per resource), `service.txt` (RED numbers), `answers.txt` with question marks and a `runbook.md` template. `$LAB_DIR` is your working directory.

## Your task

1. Fill in `answers.txt`: `bottleneck` (the resource above 90 percent utilisation with the deepest saturation), `check_order` (the three USE signals, comma separated, in the order you would read them), `service_symptom` (`rate`, `errors` or `latency`: which RED signal is bad) and `first_method` (`RED` or `USE`: which one do you start with for the service).
2. Rewrite `runbook.md` with lines starting `Alert:`, `Impact:`, `Checks:`, `Action:`, `Rollback:` and `Owner:`, and at least three numbered checks (`1. command : what the result means`), at least one using a real disk tool.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-307/use-red-runbook/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-307/use-red-runbook/check
```

## Notes

- The lab needs no extra packages. Reading material: [the lesson](lesson:LNX-307-T01). Afterwards, try [the quiz](quiz:LNX-307-T01).
