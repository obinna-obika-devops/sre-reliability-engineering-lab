# SRE Interview Walkthrough

## 60-second explanation

This lab demonstrates the reliability loop around a small Python service: define service objectives, instrument the application, detect unhealthy behavior, respond with runbooks and safe automation, deliberately inject failure, and verify recovery. The emphasis is on the operating model rather than simply deploying monitoring tools.

## Reliability model

The service exposes health, readiness and Prometheus metrics. Alerting is based on observable symptoms such as errors and latency. Kubernetes adds probes, autoscaling and disruption protection. Controlled fault injection provides a way to test whether detection and recovery behavior works as expected.

## SLO discussion

An SLO turns reliability into an engineering target. Rather than attempting undefined '100% uptime,' an SLO creates an explicit reliability objective and an error budget. That budget can influence release velocity: healthy budget allows normal delivery, while excessive burn should shift engineering attention toward reliability.

## Incident response

A useful alert must lead to an action. Runbooks provide a repeatable first-response path, while remediation automation should be narrow, observable and idempotent. Recovery is followed by validation and learning rather than stopping when the alert clears.

## Chaos engineering

Failure injection is controlled and disabled by default. The purpose is not to randomly break systems; it is to test a hypothesis about how the system behaves under a known failure mode and verify detection, mitigation and recovery.

## Failure scenarios to discuss

- Elevated HTTP error rate
- Latency degradation
- Pod crash/restart behavior
- Capacity pressure
- Unhealthy deployment
- Loss of an instance during normal traffic

## What I would add at enterprise scale

- Multi-window burn-rate alerts
- Distributed tracing and centralized logs
- Paging/incident-management integration
- Service ownership metadata
- Automated canary analysis
- Regional resilience tests
- Capacity forecasting from historical demand
- Game-day automation and documented recovery evidence

## Key takeaway

SRE is not just monitoring. It connects service objectives, telemetry, safe change, incident response, capacity, automation and learning into a measurable reliability practice.