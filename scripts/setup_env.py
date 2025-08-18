#!/usr/bin/env python3
"""Interactive .env generator.

Reads .env.example, prompts for each key with default values, writes .env,
then verifies that all keys were written.
"""
from __future__ import annotations

import re
from pathlib import Path

EXAMPLE_PATH = Path(__file__).resolve().parent.parent / ".env.example"
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"


def parse_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    current_key: str | None = None
    current_value: list[str] = []
    pattern = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)=(.*)$")

    for raw_line in path.read_text().splitlines():
        line = raw_line.rstrip()
        if current_key is not None:
            if line.endswith('"'):
                current_value.append(line[:-1])
                env[current_key] = "\n".join(current_value)
                current_key = None
                current_value = []
            else:
                current_value.append(line)
            continue

        if not line or line.lstrip().startswith('#'):
            continue

        match = pattern.match(line)
        if not match:
            continue

        key, value = match.groups()
        value = value.lstrip()
        if value.startswith('"') and not value.endswith('"'):
            current_key = key
            current_value = [value[1:]]
        else:
            env[key] = value.strip('"')

    return env


def prompt_user(values: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, default in values.items():
        prompt = f"{key} [{default}]: " if default else f"{key}: "
        entered = input(prompt)
        result[key] = entered if entered else default
    return result


def write_env(values: dict[str, str]) -> None:
    lines: list[str] = []
    for key, val in values.items():
        if "\n" in val:
            lines.append(f'{key}="{val}"')
        else:
            lines.append(f'{key}="{val}"')
    ENV_PATH.write_text("\n".join(lines) + "\n")


def verify(values: dict[str, str]) -> bool:
    written = parse_env(ENV_PATH)
    return all(k in written and written[k] == v for k, v in values.items())


def main() -> None:
    if not EXAMPLE_PATH.exists():
        raise FileNotFoundError(".env.example not found")

    defaults = parse_env(EXAMPLE_PATH)
    if ENV_PATH.exists():
        current = parse_env(ENV_PATH)
        defaults.update({k: current.get(k, v) for k, v in defaults.items()})

    values = prompt_user(defaults)
    write_env(values)
    if verify(values):
        print(f"Wrote {ENV_PATH} with {len(values)} keys")
    else:
        print("Verification failed: .env contents do not match inputs")


if __name__ == "__main__":
    main()
