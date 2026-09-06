# Recruiter / Interview Walkthrough

This page provides a quick review path through the SRE and reliability engineering evidence in this repository.

## 5-minute review path

1. Read `README.md` for the reliability loop and system architecture.
2. Inspect `app/` for the instrumented service and tests.
3. Inspect `observability/` for metrics, alerting and dashboards.
4. Inspect `kubernetes/` for probes, scaling, disruption controls and network policy.
5. Inspect `chaos/` and `remediation/` for controlled failure and recovery automation.
6. Inspect `sre/` and `runbooks/` for SLOs, incident management and operational response.
7. Inspect `.github/workflows/` for automated validation and security checks.

## What this project proves

This repository demonstrates the full reliability loop rather than monitoring alone: define reliability targets, observe system behavior, detect failure, mitigate safely, validate recovery and learn from incidents.

Key engineering themes include:

- SLIs, SLOs and error budgets
- Prometheus metrics and alert rules
- Grafana and OpenTelemetry patterns
- Kubernetes reliability controls
- controlled fault injection
- incident response and runbooks
- safe automated remediation
- capacity awareness and recovery validation

## Interview discussion points

### Why use SLOs instead of only uptime dashboards?
An SLO turns reliability into an explicit engineering target tied to user-visible behavior. Error budgets then help teams balance reliability work against release velocity.

### How should remediation automation be designed?
Automation should be narrow, idempotent, observable and reversible. It should act only on well-understood failure modes and escalate when confidence is low.

### What is the role of chaos testing?
Controlled failure testing validates assumptions before a real incident. Experiments should have clear boundaries, success criteria, abort conditions and observability.

### What would productionization add?
A real environment would add production telemetry backends, paging/on-call integration, service ownership, real traffic-based SLOs, multi-region recovery testing, security-reviewed automation permissions and post-incident tracking.

## Validation

```bash
make test
make run
```

Or run the local stack:

```bash
docker compose -f deploy/docker-compose.yml up --build
```

## Scope and integrity

This is a portfolio/reference implementation. It demonstrates production-minded SRE practices without claiming real customer traffic or production incident history that is not explicitly evidenced here.
