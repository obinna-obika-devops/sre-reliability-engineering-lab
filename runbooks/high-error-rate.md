# Incident runbook: high error rate

## Trigger
`HighErrorRate` fires when the 5-minute `/api` 5xx ratio exceeds 1% for 5 minutes.

## Triage
1. Confirm alert and check request volume.
2. Check recent deployments and configuration changes.
3. Compare application logs with dependency health.
4. Check pod restarts, CPU/memory pressure and readiness failures.

## Mitigation
- If correlated with a release, pause rollout or roll back.
- If a dependency is degraded, reduce traffic or enable the documented fallback.
- Scale only when saturation is the limiting factor; scaling does not fix application defects.

## Recovery
Confirm error rate and latency return below SLO thresholds, then monitor for at least one alert evaluation window.

## Follow-up
Create an incident record and capture timeline, customer impact, contributing factors and preventive actions.
