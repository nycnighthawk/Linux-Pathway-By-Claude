# Lab: scrape, alert and collect

Write four files in `$LAB_DIR`.

1. `servicemonitor.yaml`: a `ServiceMonitor` `shop-api` in namespace `monitoring` (API `monitoring.coreos.com/v1`) that selects Services labelled `app: api` in namespace `shop`,
   scrapes the port named `metrics` at path `/metrics` every `15s`.
2. `rules.yaml`: a `PrometheusRule` `shop-api-slo` with one group containing an alert `ApiErrorBudgetBurn` that fires when the 5-minute **and** the 1-hour error ratio
   (`http_requests_total` with `status=~"5.."` over all requests, in `rate(...[5m])` and `rate(...[1h])` forms) both exceed `14.4 * 0.001`, `for: 2m`, label `severity: page`, and annotations `summary` and `runbook_url`.
3. `otel-collector.yaml`: an OpenTelemetry Collector configuration with receiver `otlp` (protocols `grpc` and `http`), processors `memory_limiter` and `batch`
   (in that order in every pipeline), exporters `otlp/tempo` (endpoint `tempo.observability:4317`, tls insecure) and `prometheus` (endpoint `0.0.0.0:8889`),
   and two pipelines: `traces` (otlp, memory_limiter and batch, otlp/tempo) and `metrics` (otlp, memory_limiter and batch, prometheus).
4. `answer.txt`: `counter_series=<n>` for a counter with labels method (4 values), route (10) and status class (5); `histogram_series=<n>` for a histogram with 10 explicit buckets (the `+Inf` bucket is an eleventh)
   labelled by route (10 values) and method (4 values), counting every bucket series including `+Inf` plus `_sum` and `_count`.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-313/telemetry-config/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-313/telemetry-config/check
```

Needs `python3` and `PyYAML`. Reading: [the lesson](lesson:LNX-313-T09), then [the quiz](quiz:LNX-313-T09).
