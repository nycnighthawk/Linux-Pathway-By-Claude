# Lab: compute a rate, write an alert rule and route it

A Prometheus server evaluates rules; Alertmanager routes the result. You will first compute by hand what `rate()` would give from two scrapes, then write the rule and the routing configuration for an error-ratio alert. No servers are started: the grader parses your YAML.

## Starting state

`setup` writes `scrapes.txt` (two scrapes of `http_requests_total` for code 200 and 500, 300 seconds apart) and an `answers.txt` with question marks.

## Your task

1. Fill in `answers.txt`: `total_rate_per_s` (increase of all codes over the elapsed seconds, one decimal), `error_ratio_pct` (increase of code 500 over increase of all codes, in percent), `range_vector_for_5m` (the selector text) and `metric_type`.
2. Write `alerts.yml`: a group with an alert on the 5xx ratio of `http_requests_total` using `rate()` and a `for` of at least five minutes, a `severity` label of `page` or `ticket`, and a `runbook_url` annotation.
3. Write `alertmanager.yml`: a root route with a receiver and `group_by`, and a sub-route that sends `severity="page"` to a second receiver. Both receivers must be defined.

If `promtool` is installed, also run `promtool check rules alerts.yml`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-307/prometheus-rules/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-307/prometheus-rules/check
```

## Notes

- Needs `python3` with PyYAML. Reading material: [the lesson](lesson:LNX-307-T03). Afterwards, try [the quiz](quiz:LNX-307-T03).
