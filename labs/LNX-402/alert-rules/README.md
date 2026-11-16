# Lab: alerting rules that catch silent failure

`setup` writes `rules.yaml` with two weak alerts: a raw error count, and a node alert with no waiting time, severity, summary or runbook. Extend and repair it until `check` passes. The most important rule is the one for missing targets: a scrape target that vanishes produces no `up == 0` series, so alert on a count that falls below what the inventory expects. If `promtool` is installed the grader also runs it.

## Run it

`bin/lpc course lab LNX-402 alert-rules`, or edit `rules.yaml` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-402-T05).
