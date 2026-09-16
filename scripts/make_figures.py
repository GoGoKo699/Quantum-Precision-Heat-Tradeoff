#!/usr/bin/env python3
"""Rebuild the two reader-facing SVG figures from the canonical model and qph.

Run from any directory with the development dependencies installed:
    python scripts/make_figures.py

The curve samples the proved limiting function. No finite optimization,
experimental data, or new scientific reference data are generated.
"""
from __future__ import annotations

import argparse
from html import escape
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from qph.core import crossover


def resource_boundary(destination: Path) -> None:
    """Draw the exact-return model using selectable, accessible SVG text."""
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="520" '
        'viewBox="0 0 1040 520" role="img" '
        'aria-labelledby="resource-title resource-desc">',
        '<title id="resource-title">Resource boundary of the quantum operation</title>',
        '<desc id="resource-desc">An equally likely binary input qubit S, fixed '
        'workspace A, and complete Gibbs reservoir B begin independently. One '
        'input-independent unitary produces the approximate target on S, restores '
        'the ensemble-average marginal of A, and changes the energy of B. Final '
        'correlations are allowed. There is no free input label for the controller. '
        'All reservoir systems, including those used for recovery, are charged '
        'in the mean heat.</desc>',
        '<rect width="1040" height="520" rx="14" fill="#ffffff"/>',
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#475569"/></marker></defs>',
        '<g font-family="DejaVu Sans, Arial, sans-serif" fill="#172b45">',
    ]

    def text(x: int, y: int, words: str, *, size: int = 20,
             bold: bool = False, center: bool = False) -> None:
        attributes = ' font-weight="700"' if bold else ""
        attributes += ' text-anchor="middle"' if center else ""
        parts.append(
            f'<text x="{x}" y="{y}" font-size="{size}"{attributes}>'
            f'{escape(words)}</text>'
        )

    text(520, 43, "The resource boundary", size=30, bold=True, center=True)
    text(38, 87, "INDEPENDENT INPUTS", bold=True)
    text(500, 87, "FIXED OPERATION", bold=True, center=True)
    text(694, 87, "FINAL SYSTEMS", bold=True)

    parts.append(
        '<rect x="380" y="106" width="240" height="312" rx="12" '
        'fill="#f1f5f9" stroke="#bdcad9" stroke-width="2"/>'
    )
    text(500, 187, "One preset", size=23, center=True)
    text(500, 227, "unitary U", size=29, bold=True, center=True)
    text(500, 263, "on S + A + B", size=23, center=True)
    text(500, 327, "No input label", center=True)
    text(500, 355, "for the controls", center=True)

    rows = (
        (106, "#edf5ff", "#cbdcf0",
         ("Input S", "|x⟩, x = 0 or 1", "Equal probabilities"),
         ("Retained S", "Approximate target", "Max. trace error ≤ ε")),
        (216, "#eff9f4", "#c7e1d4",
         ("Workspace A", "Fixed initial state", "May be nonthermal"),
         ("Returned A", "Ensemble marginal", "Equals its initial state")),
        (326, "#fff6e9", "#ebd6b4",
         ("Reservoir B", "Complete Gibbs reservoir", "Recovery systems included"),
         ("Spent reservoir B", "All energy changes", "Count toward mean heat")),
    )
    for y, fill, border, supplied, final in rows:
        for x, width in ((24, 300), (678, 338)):
            parts.append(
                f'<rect x="{x}" y="{y}" width="{width}" height="92" '
                f'rx="10" fill="{fill}" stroke="{border}" stroke-width="2"/>'
            )
        for start, end in ((330, 371), (626, 669)):
            parts.append(
                f'<path d="M {start} {y+46} H {end}" stroke="#475569" '
                'stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>'
            )
        for x, labels in ((38, supplied), (694, final)):
            text(x, y+28, labels[0], size=23, bold=True)
            text(x, y+56, labels[1])
            text(x, y+81, labels[2])

    text(520, 450, "Final correlations are allowed; only A’s ensemble marginal returns.",
         center=True)
    parts.append(
        '<rect x="24" y="467" width="992" height="37" rx="8" '
        'fill="#172b45"/>'
        '<g fill="#ffffff">'
    )
    text(520, 492, "Mean heat = energy change of all B · reservoir Hamiltonian fixed at boundaries",
         size=19, center=True)
    parts.append('</g></g></svg>\n')
    destination.write_text("\n".join(parts), encoding="utf-8")


def limiting_curve(destination: Path) -> None:
    """Sample only qph.core.crossover; the logarithmic view excludes r = 0."""
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 18,
        "axes.labelsize": 19,
        "xtick.labelsize": 18,
        "ytick.labelsize": 18,
        "text.color": "#172b45",
        "axes.labelcolor": "#172b45",
        "xtick.color": "#172b45",
        "ytick.color": "#172b45",
        "axes.edgecolor": "#64748b",
        "svg.fonttype": "none",
        "svg.hashsalt": "qph-limiting-curve-v1",
    })
    ratios = np.geomspace(0.001, 100, 501)
    heat = np.array([crossover(float(r)) for r in ratios])

    fig = plt.figure(figsize=(11.5, 5.5), facecolor="white")
    ax = fig.add_axes([0.085, 0.235, 0.89, 0.545], facecolor="white")
    fig.text(0.085, 0.92, "Optimal limiting heat",
             fontsize=24, weight="bold")
    fig.text(0.975, 0.92,
             r"$s\to0,\quad \epsilon/s^2\to r,\quad \epsilon>0$",
             ha="right", fontsize=18)
    fig.text(0.085, 0.813, r"$F(r)$", fontsize=20)
    fig.text(0.975, 0.813, r"Heat unit: $k_{\mathrm{B}}T\ln 2$",
             ha="right", fontsize=18)

    ax.plot(ratios, heat, color="#1265ac", linewidth=3.2)
    ax.set_xscale("log")
    ax.set_xlim(0.001, 100)
    ax.set_ylim(0, 1.03)
    ax.set_xticks([0.001, 0.01, 0.1, 1, 10, 100],
                  ["0.001", "0.01", "0.1", "1", "10", "100"])
    ax.set_yticks([0, 0.5, 1], ["0", "0.5", "1"])
    ax.minorticks_off()
    ax.grid(color="#dce3eb", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(length=5, pad=7)
    ax.set_xlabel(r"Error ratio $r = \epsilon/s^2$ (log scale)", labelpad=12)

    fig.text(0.5, 0.035, r"$F(0)=1$; domain: finite $r\geq0$.",
             ha="center", fontsize=18)
    fig.savefig(destination, format="svg", facecolor="white", metadata={
        "Date": None,
        "Title": "Optimal limiting heat for the precision–heat task",
        "Description": (
            "The established function F(r) from qph.core.crossover, for "
            "s tending to zero and positive epsilon with epsilon/s^2 tending "
            "to finite r. The horizontal axis is logarithmic and displays "
            "0.001 through 100; F(0) equals 1. Vertical heat is measured in "
            "units of k_B T ln 2. This is an optimal limiting law, not an "
            "exact finite optimum or experimental data."
        ),
        "Creator": "scripts/make_figures.py; matplotlib",
    })
    plt.close(fig)
    # A direct title/description also serves SVG viewers that ignore metadata.
    svg = destination.read_text(encoding="utf-8")
    start = svg.index(">", svg.index("<svg"))
    svg = (
        svg[:start]
        + ' role="img" aria-labelledby="curve-title curve-desc"'
        + svg[start:start+1]
        + '\n <title id="curve-title">Optimal limiting heat</title>'
        + '\n <desc id="curve-desc">F(r) decreases from F(0) = 1 toward zero. '
          'The curve is the established limiting law as s tends to zero and '
          'positive epsilon divided by s squared tends to finite r. The '
          'logarithmic horizontal axis displays r from 0.001 to 100. Heat '
          'is in units of k_B T ln 2.</desc>'
        + svg[start+1:]
    )
    # Matplotlib adds whitespace to path-data lines; keep generated diffs clean.
    svg = "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"
    destination.write_text(svg, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT/"docs"/"figures")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, draw in (("resource-boundary.svg", resource_boundary),
                       ("limiting-crossover.svg", limiting_curve)):
        path = args.output_dir/name
        draw(path)
        print(f"Written to {path}")


if __name__ == "__main__":
    main()
