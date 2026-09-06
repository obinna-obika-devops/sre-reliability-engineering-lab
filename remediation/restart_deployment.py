#!/usr/bin/env python3
"""Safe demo remediation: restart a named Kubernetes deployment once."""
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("namespace")
parser.add_argument("deployment")
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

cmd = ["kubectl", "-n", args.namespace, "rollout", "restart", f"deployment/{args.deployment}"]
if args.dry_run:
    print("DRY RUN:", " ".join(cmd))
else:
    subprocess.run(cmd, check=True)
    subprocess.run(["kubectl", "-n", args.namespace, "rollout", "status", f"deployment/{args.deployment}", "--timeout=120s"], check=True)
