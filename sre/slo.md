# SLOs and error budget

## Availability

Target: **99.9%** monthly successful requests for `/api`.

A 30-day month has 43,200 minutes. A 99.9% objective permits roughly **43.2 minutes** of unavailability per month.

Error budget = `1 - SLO = 0.1%` of eligible requests.

## Latency

Target: **99% of requests under 500 ms**.

## Burn-rate thinking

Use short and long windows to distinguish a brief spike from sustained budget consumption. A sustained high burn rate should trigger mitigation and potentially freeze risky changes.

## Error-budget policy

- Healthy budget: normal delivery velocity.
- Budget warning: review risky changes and increase monitoring.
- Budget exhausted: prioritize reliability work, rollback unsafe changes, and require an explicit risk review before non-essential releases.

The objective is to balance feature velocity with user-visible reliability rather than maximizing uptime at any cost.
