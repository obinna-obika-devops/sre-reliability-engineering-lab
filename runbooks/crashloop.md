# Incident runbook: CrashLoopBackOff

1. Inspect `kubectl describe pod` for events and probe failures.
2. Read the previous container logs.
3. Check image/config/secret changes.
4. Verify resource limits are not causing OOM kills.
5. Roll back only when evidence points to the release.
6. Confirm replacement pods pass readiness before declaring recovery.

Do not delete repeatedly without collecting evidence; preserve the failure signal.
