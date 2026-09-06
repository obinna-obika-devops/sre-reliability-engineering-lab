# Capacity planning

Track four signals: traffic, latency, saturation and headroom.

## Method
1. Establish baseline requests/second and resource usage.
2. Measure p95/p99 latency at increasing concurrency.
3. Identify the first saturation point for CPU, memory or downstream dependencies.
4. Keep a defined operating headroom target rather than running at the limit.
5. Re-test after major architecture or workload changes.

## Example
If a pod sustains 50 requests/s at the latency objective and peak demand is 180 requests/s, a first-order capacity estimate is 4 pods. Add explicit headroom and validate with load testing rather than treating this arithmetic as a production guarantee.
