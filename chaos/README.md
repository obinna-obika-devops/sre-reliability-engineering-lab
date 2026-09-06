# Chaos experiment: pod failure

## Hypothesis
If one API pod disappears, the service remains available because three replicas, readiness probes and a PodDisruptionBudget maintain serving capacity.

## Procedure
1. Deploy the workload and verify all replicas are ready.
2. Apply `pod-kill.yaml` in a disposable test namespace.
3. Observe request success rate and pod replacement.
4. Confirm the error budget was not materially consumed.

## Abort criteria
Stop the experiment if multiple replicas become unavailable or customer-impacting errors exceed the agreed test threshold.

## Success criteria
Traffic remains served, a replacement pod becomes Ready, and the system returns to steady state automatically.
