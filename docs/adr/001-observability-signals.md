# ADR-001: Prometheus-first service reliability signals

## Status
Accepted

## Decision
Use application-level Prometheus metrics as the primary demo signal source, with OpenTelemetry-compatible tracing added as a complementary path.

## Context
The lab must be inexpensive to run locally while demonstrating production SRE practices. Metrics provide a simple foundation for SLOs, alerting and error-budget analysis.

## Consequences
This keeps the lab portable and observable without requiring a managed monitoring platform. In production, the same signals can be exported to managed Prometheus/OpenTelemetry backends with retention, access control and high availability added according to requirements.
