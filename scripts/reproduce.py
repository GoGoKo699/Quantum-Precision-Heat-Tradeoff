#!/usr/bin/env python3
"""Reproduce the finite benchmark and selected crossover points."""
from pathlib import Path
import argparse
import json
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import numpy as np
import scipy
from qph.core import auxiliary_allowance, collision, crossover, device_metrics, j2, lower_bound, recovery_heat


def calculate() -> dict:
    strict = lower_bound(0.05, 0.0001)
    allowance = auxiliary_allowance(16, 0.0001)
    _, _, _, b = collision(1e-5, 1e-10)
    return {
        "units": "Q/(k_B T ln 2)",
        "strict_lower_bound": strict,
        "auxiliary_entropy_allowance_bits": allowance,
        "strict_with_return_allowance": strict-allowance,
        "relaxed_device": device_metrics(0.05, 0.0025),
        "crossover": {str(r): crossover(r) for r in [0, 0.01, 0.1, 1, 10, 100]},
        "finite_recovery": {"s": 1e-5, "epsilon": 1e-10, "steps": 2048,
                            "heat": recovery_heat(b, 2048), "infimum_upper_bound": j2(b)},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT/"results"/"generated.json")
    args = parser.parse_args()
    result = {"environment": {"python": platform.python_version(),
                               "numpy": np.__version__, "scipy": scipy.__version__},
              "calculations": calculate()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result["calculations"], indent=2, sort_keys=True))
    print(f"Written to {args.output}")


if __name__ == "__main__":
    main()
