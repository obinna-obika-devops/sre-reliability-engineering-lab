#!/usr/bin/env python3
"""Guarded remediation: restart one Kubernetes deployment and verify rollout."""
import argparse
import re
import subprocess
import sys

NAME_RE = re.compile(r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$")


def valid_name(value: str) -> str:
    if len(value) > 63 or not NAME_RE.fullmatch(value):
        raise argparse.ArgumentTypeError("must be a valid Kubernetes DNS label")
    return value


def build_commands(namespace: str, deployment: str, timeout: int):
    target = f"deployment/{deployment}"
    return [
        ["kubectl", "-n", namespace, "rollout", "restart", target],
        ["kubectl", "-n", namespace, "rollout", "status", target, f"--timeout={timeout}s"],
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("namespace", type=valid_name)
    parser.add_argument("deployment", type=valid_name)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not 10 <= args.timeout <= 900:
        parser.error("timeout must be between 10 and 900 seconds")

    commands = build_commands(args.namespace, args.deployment, args.timeout)
    if args.dry_run:
        for command in commands:
            print("DRY RUN:", " ".join(command))
        return 0

    try:
        subprocess.run(commands[0], check=True)
        subprocess.run(commands[1], check=True)
    except subprocess.CalledProcessError as exc:
        print(f"remediation failed with exit code {exc.returncode}", file=sys.stderr)
        return exc.returncode or 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
