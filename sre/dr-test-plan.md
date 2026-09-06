# Disaster recovery test plan

## Objectives
Validate that backups are restorable, recovery procedures are documented, and recovery objectives are measurable.

## Test sequence
1. Record current service and dependency state.
2. Create a disposable restore target.
3. Restore the latest known-good backup.
4. Validate application health and critical data integrity.
5. Measure RTO and RPO achieved.
6. Record gaps and remediation owners.

## Guardrails
Never perform destructive recovery tests against production without an approved change and tested rollback path.

## Targets
Reference target: RTO 60 minutes, RPO 15 minutes. These are lab objectives and must be adjusted to business requirements in a real environment.
