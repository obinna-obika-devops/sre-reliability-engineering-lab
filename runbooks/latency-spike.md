# Incident runbook: latency spike

## Trigger
`HighLatency` indicates sustained p99 latency above 500 ms.

## Triage
- Inspect p50/p95/p99 trends.
- Check CPU throttling, memory pressure and replica count.
- Identify slow dependencies or external calls.
- Compare latency before and after the latest release.

## Mitigation
Reduce load, roll back a correlated change, or scale when resource saturation is demonstrated. Avoid blind restarts because they can hide the signal without fixing the cause.

## Recovery
Verify p99 returns below the objective and that no secondary error-rate increase occurs.
