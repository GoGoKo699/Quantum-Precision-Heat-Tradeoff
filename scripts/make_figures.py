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
        '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="824" '
        'viewBox="0 0 600 824" role="img" '
        'aria-labelledby="resource-title resource-desc">',
        '<title id="resource-title">Resource boundary of the quantum operation</title>',
        '<desc id="resource-desc">An equally likely binary input qubit S, fixed '
        'workspace A, and complete Gibbs reservoir B begin independently. One '
        'input-independent unitary produces the approximate target on S, restores '
        'the ensemble-average marginal of A, and changes the energy of B. Final '
        'correlations are allowed. There is no free input label for the controller. '
        'All reservoir systems, including those used for recovery, are charged '
        'in the mean heat.</desc>',
        '<rect width="600" height="824" rx="14" fill="#ffffff"/>',
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#475569"/></marker></defs>',
        '<g font-family="DejaVu Sans, Arial, sans-serif" fill="#172b45">',
    ]

    def text(x: int, y: int, words: str, *, size: int = 24,
             bold: bool = False, center: bool = False) -> None:
        attributes = ' font-weight="700"' if bold else ""
        attributes += ' text-anchor="middle"' if center else ""
        parts.append(
            f'<text x="{x}" y="{y}" font-size="{size}"{attributes}>'
            f'{escape(words)}</text>'
        )

    text(300, 46, "The resource boundary", size=30, bold=True, center=True)
    text(300, 85, "One preset unitary on S + A + B", center=True)
    text(300, 121, "No free input label for the controls", center=True)
    text(35, 169, "SUPPLIED", bold=True)
    text(315, 169, "FINAL", bold=True)

    rows = (
        (190, "#edf5ff", "#cbdcf0",
         ("Input S", "|x⟩, x = 0 or 1", "equal probabilities"),
         ("Retained S", "approximate target", "max trace error ≤ ε")),
        (348, "#eff9f4", "#c7e1d4",
         ("Workspace A", "fixed initial state", "need not be Gibbs"),
         ("Returned A", "ensemble marginal", "equals initial state")),
        (506, "#fff6e9", "#ebd6b4",
         ("Reservoir B", "initial Gibbs state", "complete reservoir"),
         ("Spent reservoir B", "recovery systems", "included from start")),
    )
    for y, fill, border, supplied, final in rows:
        for x, width in ((20, 244), (302, 278)):
            parts.append(
                f'<rect x="{x}" y="{y}" width="{width}" height="140" '
                f'rx="10" fill="{fill}" stroke="{border}" stroke-width="2"/>'
            )
        parts.append(
            f'<path d="M 268 {y+70} H 295" stroke="#475569" '
            'stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>'
        )
        for x, labels in ((35, supplied), (315, final)):
            text(x, y+35, labels[0], bold=True)
            text(x, y+76, labels[1])
            text(x, y+111, labels[2])

    text(300, 685, "Final correlations are allowed", center=True)
    parts.append(
        '<rect x="20" y="712" width="560" height="92" rx="10" '
        'fill="#172b45"/>'
        '<g fill="#ffffff">'
    )
    text(300, 749, "Mean heat = energy change of all B", bold=True, center=True)
    text(300, 783, "Reservoir Hamiltonian fixed at boundaries", center=True)
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

    fig = plt.figure(figsize=(6.5, 5.8), facecolor="white")
    ax = fig.add_axes([0.14, 0.25, 0.82, 0.48], facecolor="white")
    fig.text(0.5, 0.94, "Optimal limiting heat", ha="center",
             fontsize=22, weight="bold")
    fig.text(0.5, 0.862,
             r"$s\to0,\quad \epsilon/s^2\to r,\quad \epsilon>0$",
             ha="center", fontsize=19)
    fig.text(0.14, 0.773, r"$F(r)$", fontsize=20)
    fig.text(0.96, 0.773, r"Heat unit: $k_{\mathrm{B}}T\ln 2$",
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
    ax.set_xlabel(r"Error ratio $r = \epsilon/s^2$ (log scale)", labelpad=14)

    fig.text(0.5, 0.061, r"$F(0)=1$; domain: finite $r\geq0$.",
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
